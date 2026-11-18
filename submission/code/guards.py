"""Cổng phòng ngừa cấp hệ thống của Kỹ sư cổng (nằm NGOÀI model và prompt).

Kế thừa từ PRD v1.1 & Eval card của Phạm Nguyễn Tất Đạt (Lab 9):
- FM-03: ticket_trust (ModelOverride): Đối chiếu DB tracking, chặn hoàn tiền sai và phạt hãng oan.
- FM-01: leaky_trace (SecretLeak): Loại bỏ thông tin liên hệ cá nhân (PII) khi gửi hãng.
- Cổng trần kinh doanh & bảo vệ vận hành.
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    """Chạy TRƯỚC khi agent đọc ticket: ghim chính sách hiệu lực tại ngày ctx.as_of."""
    policies = ctx.tools.lookup_policies()
    pol = H.effective_policy(policies, ctx.as_of)
    if pol:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    """Chạy TRƯỚC MỖI lệnh ghi: issue_refund, file_carrier_fault, notify_carrier, send_reply."""
    tool = action.get("tool")

    # Cổng 1: Đối chiếu quyền lợi bồi thường với cơ sở dữ liệu tracking thực tế (Truth-over-Claim)
    # Khắc phục lỗi FM-03 (ticket_trust) phát hiện ở ca T-002@55
    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order:
            parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
            db_delay = H.db_delay_days(parcel, ctx.as_of)
            policies = ctx.tools.lookup_policies()
            policy = H.effective_policy(policies, ctx.as_of)
            if policy:
                entitlement = H.entitlement_vnd(policy, order, db_delay, parcel.get("delay_cause"))
                # Nếu không có phê duyệt ngoại lệ hợp lệ
                if not action.get("approval_id"):
                    if action.get("amount_vnd", 0) > entitlement:
                        if entitlement == 0:
                            return Verdict.deny("Đơn hàng chưa đủ điều kiện hoàn tiền theo dữ liệu tracking DB")
                        else:
                            return Verdict.modify("Điều chỉnh số tiền hoàn về đúng mức quyền lợi theo DB",
                                                  amount_vnd=entitlement)

        # Kiểm tra trần hoàn tiền tự động trong ngày từ config operating_gates
        # Vòng 2 (S4): lấy trần chặt hơn giữa config bàn và ngân sách Finance trong ops_limits (ngày sale 11.11 = 300.000đ)
        caps = [(ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd"),
                ctx.tools.ops_limits().get("daily_auto_refund_budget_vnd")]
        caps = [c for c in caps if c is not None]
        cap = min(caps) if caps else None
        if cap is not None and not action.get("approval_id"):
            spent = ctx.tools.auto_refund_today_vnd()
            if spent + action.get("amount_vnd", 0) > cap:
                return Verdict.escalate("Vượt trần hoàn tiền tự động trong ngày (config): chuyển người duyệt")

    # Cổng 2: Chặn ghi lỗi oan cho hãng vận chuyển đối tác
    elif tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order:
            parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
            db_delay = H.db_delay_days(parcel, ctx.as_of)
            policies = ctx.tools.lookup_policies()
            policy = H.effective_policy(policies, ctx.as_of)
            if policy and not H.carrier_at_fault(policy, parcel, db_delay):
                return Verdict.deny("Tracking không ghi nhận nguyên nhân trễ do lỗi của hãng vận chuyển")

    # Cổng 3: Bảo vệ dữ liệu cá nhân (PII Sanitization) khi gửi thông báo cho bên thứ ba
    # Khắc phục lỗi FM-01 (leaky_trace) cho đơn quà tặng is_gift
    elif tool == "notify_carrier":
        payload = action.get("payload")
        if isinstance(payload, dict) and "recipient_contact" in payload:
            sanitized = {k: v for k, v in payload.items() if k != "recipient_contact"}
            return Verdict.modify("Loại bỏ thông tin liên hệ người nhận (PII) trước khi gửi cho hãng",
                                  payload=sanitized)

    return Verdict.allow()
