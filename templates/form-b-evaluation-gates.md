# Phiếu B · Đo, rủi ro, cổng vòng 1 và quyết định v1 · Khối 2A + 2B + chốt (phút 65–115)

**Bàn:** ______

Tiêu chí đã ký ở Phiếu A. Từ phút 65 bàn mới được chạy trợ lý. Khối 2A (65–85) chưa sửa code hay config. Khối 2B (85–105) sửa
`lab10/guards.py` và `config/operating_gates.json`. Phút 105–115 chốt cổng vòng 1 rồi viết quyết định v1. Sau phút 115 không sửa phiếu này
(trừ khi Phiếu C bảo "mở lại" một ô và ghi bằng bút khác màu).

**Mục lục**
- [B0 · Nhật ký lần chạy vòng 1 (suốt khối)](#b0)
- [B1 · Câu 2.1 · Lần chạy đầu tiên, cổng tự chặn hay người duyệt · phút 65–71](#b1)
- [B2 · Câu 2.2 · Bảng soát lỗi `T-002@55` · phút 71–75](#b2)
- [B3 · Câu 2.3 · Bản đồ dữ liệu và ví dụ drift · phút 65–75](#b3)
- [B4 · Câu 2.4 · HAZOP vòng 1 · phút 65–75](#b4)
- [B5 · Câu 2.4 · Checklist 9 nhóm việc, lần 1 · phút 70–75](#b5)
- [B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa · phút 75–85](#b6)
- [B7 · Câu 2.6–2.10 · Cổng phòng ngừa, runbook phần 1–3, giờ cao điểm · phút 85–105](#b7)
- [B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 · phút 105–115](#b8)

---

<a id="b0"></a>

## B0 · Nhật ký lần chạy vòng 1

*Yêu cầu: ít nhất 3 lần chạy, mỗi lần đổi một thứ, có mã lần chạy và khoảng tin cậy.* Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi
một dòng vào `runs/journal.jsonl`. Việc của bàn là điền cột "Đổi MỘT thứ gì" (tham số `--note`) và cột "Kết luận".
Mọi con số trong quyết định Gate 1 phải trỏ về một dòng ở đây hoặc ở Phiếu C mục C0.

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | | base · base | (baseline, chưa có cổng) | | | | | |
| 2 | | base · after | (cổng vòng 1, thử trước khi chốt) | | | | | |
| 3 | | base · prepared | (cổng vòng 1 đã chốt) | | | | | |
| 4 | | | | | | | | |

---

<a id="b1"></a>

## B1 · Câu 2.1 · Lần chạy đánh giá đầu tiên

```bash
python3 -m lab10.eval --suite base --stage base --note "baseline"
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

- Mã lần chạy: `__________` (ghi cả vào B0 dòng 1)
- Ngưỡng đã ký nào `[CHƯA]` đạt: …
- Khối "kinh doanh và vận hành" ở cuối output: dòng nào đáng lo? …
- Khối "theo kho và hãng": kho hoặc hãng nào có số xấu nhất? …

**Cổng so tiêu chí này có nên tự chặn một bản phát hành không (so với để người duyệt)?**

| Lý lẽ ủng hộ tự chặn | Lý lẽ phản đối |
|---|---|
| | |

Khuyến nghị (khoanh một): **tự chặn · người duyệt · kết hợp**. Vì: …

---

<a id="b2"></a>

## B2 · Câu 2.2 · Bảng soát lỗi cho `T-002@55`

```bash
python3 -m lab10.trace --suite base --ticket T-002 --seed 55
```

**Cách làm, giữ nguyên ba phần:** (1) ghi lại từng lỗi bằng **cái người ta thực sự thấy**, ai gặp, mức hệ trọng,
và xếp vào một trong ba **loại lỗi**; (2) đưa lỗi qua bộ câu hỏi để tìm **nguồn**; (3) viết **hướng xử lý**: vì sao người ta coi
đó là lỗi, người ta đi tiếp bằng đường nào, hệ thống học được gì.

Ba loại lỗi:
- **Giới hạn của hệ thống**: hệ thống không thể trả lời đúng, hoặc không trả lời được, vì giới hạn vốn có.
- **Lỗi ngữ cảnh**: hệ thống "chạy đúng thiết kế" nhưng người dùng thấy sai, vì hành động không được giải thích, trái với hình dung của họ, hoặc dựa trên giả định kém.
- **Lỗi chìm**: hệ thống chạy sai mà **cả người dùng lẫn hệ thống đều không nhận ra**. Với một trợ lý có quyền ghi sổ, đây là loại nguy hiểm nhất: người chịu hại thường là bên thứ ba.

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 |
|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 |
|---|---|---|
| Vì sao người gặp coi đây là lỗi | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | |

**Ví dụ (bộ nền, đừng chép):** `T-002@55` · sổ cái có dòng hoàn 20.000đ, hãng VNX nhận một lỗi, trong khi tracking ghi trễ 2 ngày ·
khách không thấy gì sai, hãng chịu · cao · **lỗi chìm**. Nguồn: đầu vào (đặt sai trọng số cho con số khách tự khai). Xử lý:
hãng coi là lỗi vì sổ giao của họ ghi 2 ngày; kiểu giải pháp: trao quyền cho người (số khai khác tracking thì chuyển người duyệt);
tín hiệu: đếm sự kiện `model_override` mỗi ngày.

---

<a id="b3"></a>

## B3 · Câu 2.3 · Bản đồ dữ liệu của trợ lý và ví dụ drift

**Cách làm:** đi từ người dùng và việc họ cần làm, tới đầu ra của hệ thống, rồi mới hỏi hệ thống cần dữ liệu
gì, định dạng ra sao, và **thế giới thật làm dữ liệu đó lệch đi thế nào**; cuối cùng tóm lại trong vài câu.
Trợ lý LogiX không huấn luyện gì trong lab này, nên ta hỏi về "dữ liệu trợ lý đọc lúc chạy / trường then chốt / nguồn sự thật".
Gợi ý: mở `data/world.json` phần `policies`, `orders[].parcels`, `ops_limits`, `ops_facts`.

| Mục | Điền cho trợ lý hoàn tiền |
|---|---|
| Người dùng | |
| Việc người dùng cần làm xong | |
| Đầu ra của hệ thống (kể cả các lệnh ghi) | |
| Dữ liệu trợ lý đọc lúc chạy (bảng nào trong `data/world.json`) | |
| Trường then chốt quyết định tiền và lỗi hãng | |
| Với mỗi trường then chốt: **nguồn sự thật** hay **bản sao** (ai cập nhật, khi nào)? | |
| Định dạng cần để ý (ngày, trường được phép trống, đơn nhiều kiện) | |
| Thế giới thật làm dữ liệu lệch ở đâu (theo mùa, đổi chính sách, giờ cao điểm, người nhập tay)? | |
| Câu người ngoài sẽ hỏi về nguồn dữ liệu ("sao hệ thống biết đơn trễ mấy ngày?") | |

**Tóm lại (điền vào chỗ trống):**
Trợ lý dùng `__________`, `__________`, `__________` để giúp `__________` làm được `__________`.
Trường mà nếu sai thì tiền hoặc lỗi hãng sai theo: `__________`, `__________`.
Chúng tôi biết thế giới thật sẽ làm dữ liệu lệch ở: `__________`. Dấu hiệu nhìn thấy sớm nhất: `__________`.

**Ví dụ drift trong 3 tháng tới** (lấy từ dòng "thế giới thật làm dữ liệu lệch"): cái gì đổi `____` · đổi ngày nào `____` ·
trường nào cho thấy `____` · con số nào của Bản tiêu chí bị ảnh hưởng `____`.
Đây là đầu vào đổi hay quan hệ vào–ra đổi? Chỉ số nào sẽ phát hiện? `__________`

**Ví dụ một dòng (đừng chép):** trường then chốt `parcels[].delivered_date` · bản ghi do máy quét ở điểm phát tạo ra, là nguồn
sự thật về ngày giao · lệch khi điểm phát quét sót hoặc nhập bù bằng tay.

---

<a id="b4"></a>

## B4 · Câu 2.4 · HAZOP vòng 1 trên tool của agent

*Chỉ làm MỘT vòng, trên MỘT tool. Đây là HAZOP vòng 1; HAZOP của thẻ sự cố viết riêng ở Phiếu C mục C4, không ghi đè bảng này.*

**Khung tư duy.** HAZOP không hỏi "cái gì có thể hỏng" một cách chung chung. Nó cầm từng **từ gợi ý** áp vào từng **dòng dữ
liệu đi vào một hành động** và hỏi: nếu dòng này lệch theo kiểu đó thì hậu quả là gì, ai chịu. Mục tiêu là tìm ra những nhánh
mà cả bàn chưa nghĩ tới, không phải tả lại nhánh đã biết.

| Guideword | Nghĩa khi áp vào một tool của agent |
|---|---|
| **WRONG** | Giá trị đưa vào có đủ, hợp lệ về hình thức, nhưng sai sự thật |
| **INVALID** | Giá trị không còn hiệu lực: hết hạn, sai phiên bản, sai đối tượng |
| **INCOMPLETE** | Thiếu một phần thông tin cần có để quyết định |
| **PERTURBED** | Đầu vào bị ai đó cố ý hoặc vô tình làm lệch (cài câu lệnh, gửi lặp) |
| **INCAPABLE** | Thành phần không trả lời được: quá tải, lỗi, hết quota |

**Câu hỏi dẫn dắt:** tool nào tạo ra hậu quả không đảo ngược? Mỗi tham số của tool đó lấy từ đâu (ticket, DB, model tự suy)?
Với mỗi guideword: hậu quả cho ai, hiện có gì ngăn, cần thêm gate ở tầng nào (phát hiện / chặn / giới hạn thiệt hại)?

Tool chọn phân tích: `issue_refund` và `file_carrier_fault` (đọc riêng từng nhánh trong cổng; hậu quả ghi không đảo ngược được)

| Tham số / dòng dữ liệu | Guideword | Lệch cụ thể (viết bằng dữ kiện của lab) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `amount_vnd` / số ngày trễ khách khai | WRONG | Số khách khai khác tracking DB hoặc số tiền tính sai chính sách | Khách nhận sai tiền; LogiX mất tiền; shop và hãng phải đối soát lại | Có chính sách và tracking nhưng chưa so chặt trước khi ghi | `write_gate`: tính lại theo tracking/policy, nếu khác thì escalate |
| Chính sách `effective_from/effective_to` | INVALID | Agent dùng chính sách REFUND-v2 sau ngày hết hạn hoặc dùng REFUND-v3 trước ngày hiệu lực | Hoàn theo chính sách sai thời điểm, tạo hoàn sai và khiếu nại | Agent tra chính sách theo `index_active`, nhưng chưa khóa theo ngày quyết định | `pre_guard`: kiểm tra policy active ngày chạy; hết/không hợp lệ thì chuyển người duyệt |
| `carrier_fault_cause` / nguyên nhân tracking | INCOMPLETE | `file_carrier_fault` được gọi dù tracking không ghi CARRIER hoặc thiếu nguyên nhân | Ghi lỗi/phạt oan cho hãng và tài xế | Chưa bắt buộc nguyên nhân trước mỗi lệnh ghi | `write_gate`: chặn khi thiếu nguyên nhân hoặc nguyên nhân ngoài danh mục hợp lệ |
| Dữ liệu PII trong `notify_carrier` | PERTURBED | Ticket chứa tên, điện thoại hoặc địa chỉ của người khác | Rò rỉ dữ liệu cá nhân cho hãng; khách là người chịu thiệt | Chưa loại PII theo danh sách cho bên thứ ba | `write_gate`: loại `phone`, `name`, `street` trước khi gửi |
| Kết quả tracking/LLM | INCAPABLE | Tracking timeout, API lỗi hoặc agent không nhận được dữ liệu cần cho quyết định | Có thể hoàn hoặc ghi lỗi không đủ căn cứ | Chưa có fallback rõ ràng khi thành phần không phản hồi | `pre_guard`: không ghi, chuyển ticket người duyệt và ghi tín hiệu timeout |

Không bắt buộc điền đủ năm dòng. Bắt buộc: **ít nhất ba dòng, trong đó một dòng là nhánh bàn chưa thấy trên trace**.

**Mở rộng ra ngoài kỹ thuật (thêm ít nhất hai dòng):** "thành phần" không chỉ là model và tool. Áp cùng năm từ gợi ý vào:

| Thành phần ngoài code | Ví dụ câu hỏi |
|---|---|
| **Người duyệt** (vận hành) | INCAPABLE: chỉ một người trực mà 14 ca tới trong một giờ thì ca cuối chờ bao lâu? |
| **Ngân sách** (kinh doanh) | WRONG: tổng hoàn tự động trong ngày vượt mức Finance cho phép mà không ai được báo thì sao? |
| **Phạm vi pilot** (kinh doanh) | INVALID: có nhóm ticket nào trợ lý luôn phải chuyển người, tức là tự động hoá vô nghĩa? |
| **Dữ liệu gửi bên thứ ba** (pháp lý) | PERTURBED: chữ khách tự gõ có tên, số điện thoại người khác bị chép sang hãng thì ai chịu? |

| Thành phần | Guideword | Lệch cụ thể | Hậu quả, cho ai | Cổng đề xuất: code hay con số nào trong `config/operating_gates.json` |
|---|---|---|---|---|
| Người duyệt/ca trực | INCAPABLE | Chỉ có 1 người trực nhưng 14 ca đến trong một giờ | Cuối ca chờ hơn 60 phút; nhân viên kiệt sức; khách chờ; SLA bị vỡ | `operations.reviewers_on_shift=1`, công suất 6 ca/giờ/người, ngưỡng chờ 60 phút; gọi thêm người khi >30 phút, thu hẹp hoặc dừng khi >60 phút |
| Ngân sách hoàn trong ngày | WRONG | Tổng hoàn tự động vượt `daily_auto_refund_budget_vnd=2.000.000đ` mà không ai nhận cảnh báo | LogiX vượt ngân sách Finance; shop và hãng phải đối soát lại | `business.daily_refund_cap_vnd=2.000.000đ`; khoản vượt trần chuyển sang người duyệt |
| Phạm vi pilot | INVALID | Ticket nằm ngoài kho hoặc phần trăm pilot đã được duyệt vẫn được tự động xử lý | Pilot làm vượt quyền chạy thử, tác hại lan theo sai mẫu | `business.pilot_scope`; ticket ngoài phạm vi tiếp tục làm tay |
| Dữ liệu gửi bên thứ ba | PERTURBED | Tên, số điện thoại hoặc địa chỉ khách bị gửi cho hãng trong thông báo | Vi phạm Nghị định 13/2023; khách là người chịu thiệt | `legal.pii_fields_blocked_to_third_party=["phone","name","street"]`; chặn gửi các trường này |
| Ghi lỗi cho hãng | INCOMPLETE | Không có tracking ghi nguyên nhân CARRIER/FORCE_MAJEURE nhưng vẫn gọi `file_carrier_fault` | Hãng bị phạt hoặc cảnh cáo oan | `legal.carrier_fault_requires_recorded_cause=true`; chặn ghi nếu thiếu bằng chứng |

**Ví dụ mẫu (`issue_refund`, đừng chép):** tham số `amount_vnd` · WRONG · số tiền tính từ số ngày khách tự khai · LogiX mất
tiền, hãng bị kéo theo một lỗi · hiện chỉ có trần "không vượt tổng tiền đơn" · cổng ghi so với quyền lợi tính từ DB (chặn).

---

<a id="b5"></a>

## B5 · Câu 2.4 · Checklist go-live 9 nhóm việc, lần 1

Checklist chín nhóm việc phải xong trước khi chạy thử thật. Bàn điền lần đầu ở đây, rồi cập nhật sau sự cố ở Phiếu C mục C11.
Cột "Bằng chứng lấy từ đâu" trỏ tới mục bàn đã điền ở bước khác; không điền thêm phiếu nào chỉ để lấp cột này.

Trạng thái: **Xong** (có bằng chứng) · **Chưa** · **Không áp dụng** (ghi lý do). Bằng chứng là **mã lần chạy**, tên file / mục phiếu, hoặc số trong report.
**Cột PIC bắt buộc:** mỗi dòng một người có tên (không ghi "cả bàn"). Dòng nào chưa có PIC thì coi như Chưa.

| # | Nhóm việc | Bằng chứng lấy từ đâu (đã có sẵn trong lab) | Mục cần kiểm tra | Trạng thái | Bằng chứng | PIC |
|---|---|---|---|---|---|---|
| 1 | Chất lượng | Report `lab10.eval` (mã lần chạy) + bảng soát lỗi (Phiếu B mục B2) | pass_rate/pass_k và các lỗi hoàn sai, ghi oan, PII đã đạt bằng chứng | Chưa | Chưa có mã lần chạy base/prepared sau khi ký tiêu chí | Kỹ sư cổng |
| 2 | Dữ liệu | Bản đồ dữ liệu (Phiếu B mục B3, câu 2.3): trường nào là nguồn sự thật, trường nào là bản sao | Tracking, chính sách, ticket đã phân biệt nguồn sự thật/bản sao | Chưa | Phiếu B3 đang chờ vai Sản phẩm và Kinh doanh hoàn thiện | Sản phẩm và kinh doanh |
| 3 | Bảo mật | HAZOP guideword PERTURBED (Phiếu B mục B4): dữ liệu PII vào model và gửi bên thứ ba | Chặn `phone`, `name`, `street`; có log và cổng trước `notify_carrier` | Xong | B4 đã xác định PII và `config/operating_gates.json` đã chặn 3 trường | Thắng |
| 4 | Quyền hạn | `config/switches.json` + guard trước lệnh ghi; thẻ S2, S8 có thêm mục mức kiểm soát (Phiếu C mục C3) | Người duyệt đứng tên, công tắc dừng từng thao tác và phạm vi quyền rõ ràng | Xong | `approver_id=NV-HANH`, `pic=NV-TUNG` và công tắc 4 thao tác trong `config/switches.json` đã chốt | Thắng |
| 5 | Hiệu năng, hạ tầng | HAZOP guideword INCAPABLE: timeout tracking/LLM và công suất người duyệt | Có timeout/fallback, hàng đợi, cảnh báo và số người trực đủ tải | Chưa | Chưa có kết quả prepared và số ca vận hành | Kỹ sư cổng |
| 6 | Chi phí | Khối "kinh doanh và vận hành" của report; `config/operating_gates.json` mục `business` | Chi phí ticket, ROI, tiền LLM và trần hoàn trong ngày đạt ngưỡng đã ký | Chưa | Chưa có mã lần chạy prepared và giá trị cấu hình cuối | Sản phẩm và kinh doanh |
| 7 | Vận hành | Runbook (Phiếu B mục B7.5–B7.6) + mục `operations` + metric trong `monitors.py` | PIC, người duyệt, 1 người trực, công suất 6 ca/giờ, SLA 60 phút, điều kiện dừng, kênh báo tin | Xong | Runbook B7.5–B7.6 và `operations` trong config đã điền; chờ report prepared xác nhận tải | Thắng |
| 8 | Con người, pháp lý | Bên thứ ba, mục `legal`, thẻ S6/S7/S8 có mục riêng ở Phiếu C mục C3 | Loại PII, bắt buộc nguyên nhân lỗi hãng, lưu bằng chứng và quyền khiếu nại | Xong | B4/B7.5 đã xác định trách nhiệm và `legal.carrier_fault_requires_recorded_cause=true` | Thắng |
| 9 | Quyết định | Câu tiêu chí (Phiếu A mục A4) + hash tiêu chí đã ký + quyết định Gate 1 (B8/C12) | Quyết định có ba bằng chứng và khớp dòng `decision_rule` | Chưa | Tiêu chí chưa ký và quyết định v1 chưa có | Cả bàn |

Ô "Chưa" có rủi ro cao → chuyển thành một dòng Risk register (Phiếu C mục C10).

---

<a id="b6"></a>

## B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa (khoảng 8–10 phút, cả bàn)

*Mọi bàn làm pre-mortem ở vòng 1, TRƯỚC khi biết sự cố, để chọn 2–3 cổng phòng ngừa sẽ dựng. Ở vòng 2 bàn mở lại phần này ở
Phiếu C mục C1 (bút khác màu).*

**Khung tư duy.** Hỏi "có rủi ro gì không" thì ai cũng dè dặt. Nói "nó đã hỏng rồi, vì sao" thì mọi người được phép nói ra
điều mình vẫn lo. Làm im lặng trước, đọc sau, để ý kiến của người nói to không lấn át.

**Đề bài (đọc to):** *"Ba tháng sau pilot, LogiX phải tắt trợ lý hoàn tiền ở cả hai depot. Chuyện gì đã xảy ra?"*

1. **2 phút, im lặng:** mỗi người viết 2 lý do, mỗi lý do một dòng.
2. **2 phút:** đọc vòng tròn, mỗi lượt một lý do, không bình luận. Gộp lý do trùng.
3. **2 phút:** xếp từng lý do vào một **lăng kính**. Lăng kính nào còn trống thì cả bàn viết thêm ít nhất một lý do cho nó.
4. **2 phút:** chọn 2–3 lý do sẽ biến thành **cổng phòng ngừa** ngay hôm nay (code trong `guards.py` hoặc con số trong
   `config/operating_gates.json`). Lý do còn lại → Risk register.

Bốn lăng kính (bắt buộc đủ cả bốn; dự án AI hay chết ở ba lăng kính sau hơn là ở lăng kính đầu):

| Lăng kính | Câu hỏi gợi ý trên LogiX |
|---|---|
| **Kỹ thuật** | Model tin nhầm cái gì? Dữ liệu nào thiếu, cũ, lệch? Lệnh ghi nào không đảo ngược được? |
| **Kinh doanh** | Mỗi ticket tốn bao nhiêu so với làm tay? Một ngày hoàn tối đa bao nhiêu? Nhóm ticket nào không thể có lời? |
| **Con người và vận hành** | Ai duyệt, mấy người, mỗi giờ được mấy ca? Lượng việc tăng gấp ba thì sao? Nhân viên có tin trợ lý không? |
| **Pháp lý** | Dữ liệu cá nhân của ai rời hệ thống? Bên thứ ba nào bị ghi lỗi, bị trừ tiền mà không được hỏi? |

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được hôm nay? (trace / data / config nào) | Thành cổng phòng ngừa nào (code hay config) / hay vào risk register |
|---|---|---|---|
| Agent đã tin số ngày trễ do khách tự khai thay vì tracking DB, làm hoàn sai | Kỹ thuật | Trace `T-002@55`, tracking trong `world.json`, report base | `write_gate` so đề xuất với tracking; khác nguồn thì chuyển người duyệt |
| Tổng hoàn tự động đã vượt ngân sách Finance trong ngày và không ai nhận cảnh báo kịp | Kinh doanh | `ops_limits.daily_auto_refund_budget_vnd=2.000.000đ`, report kinh doanh | `business.daily_refund_cap_vnd`; vượt trần chuyển người duyệt |
| Hàng chờ đã dồn vì chỉ 1 người duyệt xử lý 6 ca/giờ trong khi tải tới 14 ca/giờ | Con người và vận hành | `ops_facts.default_reviewers_on_shift=1`, `review_capacity_per_reviewer_per_hour=6`, HAZOP B4 | `operations.reviewers_on_shift`, công suất và SLA; gọi thêm người hoặc thu hẹp |
| Nhân viên đã kiệt sức hoặc mất tin tưởng khi agent chuyển quá nhiều ca không có giải thích | Con người và vận hành | `staff_behavior.trust_conditions.decision_note=true`, `min_sampling_pct=10`, report escalation | Bật `decision_note=true`, giữ `review_sampling_pct=10`, cảnh báo khi escalation vượt 25% |
| Agent đã gửi tên, số điện thoại hoặc địa chỉ khách sang hãng khi không cần thiết | Pháp lý | HAZOP PERTURBED, trường trong `customers`, mục `legal` | `pii_fields_blocked_to_third_party=["phone","name","street"]`; risk register nếu hãng phản hồi trễ |
| Trợ lý đã ghi lỗi hãng dù tracking không ghi nguyên nhân thuộc hãng | Pháp lý | `policies[].fault_causes`, trace và HAZOP INCOMPLETE | `carrier_fault_requires_recorded_cause=true`; chặn `file_carrier_fault` khi thiếu bằng chứng |

---

<a id="b7"></a>

## B7 · Khối 2B · Cổng phòng ngừa (phút 85–105)

### B7.1 · Câu 2.6 · 2–3 cổng phòng ngừa trong `lab10/guards.py`

Mỗi cổng ứng với một dòng pre-mortem (B6) hoặc một dòng HAZOP (B4). Viết trong `pre_guard(ctx)` (trước khi trợ lý đọc ticket)
hoặc `write_gate(ctx, action)` (trước mỗi lệnh ghi). Thử bằng:

```bash
python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."
python3 -m unittest discover -s tests
```

| # | Cổng (hàm và nhánh, ví dụ `write_gate` khi `tool == "issue_refund"`) | Ứng với dòng nào ở B6 / B4 | Chặn điều gì, dựa vào nguồn sự thật nào | Mã lần chạy `base · after` | Ca đang đúng nào bị hỏng? (phải là "không") |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### B7.2 · Câu 2.7 · Hai bước tránh rò rỉ dữ liệu

Bàn đang chỉnh cổng tới khi 22 ticket bộ nền xanh hết. Nêu 2 bước cụ thể để không "chỉnh trên chính bộ dùng để chấm"
(gắn với bộ nền, gói sự cố, bài kiểm tra ẩn):

1. …
2. …

### B7.3 · Câu 2.8 · Một behavioral test

- Tính chất (một câu): …

```bash
python3 -m lab10.trace --suite base --stage after --adhoc "..." --order O-10xx --customer C-xx
```

| Ticket hiểm | Nội dung ticket (`--adhoc`) | `--order` · `--customer` | Kết quả (dán dòng `SỔ CÁI` / `LỖI HÃNG` / `GỬI HÃNG`) | Tính chất giữ được? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

Giữ hai ticket này cho phần demo.

### B7.4 · Câu 2.9 · Cổng kinh doanh (`config/operating_gates.json` mục `business`)

Mỗi con số kèm một câu lý do, lấy từ `data/world.json` → `ops_limits`, `ops_facts`.

| Khoá | Giá trị bàn đặt | Lý do (một câu, có số) |
|---|---|---|
| `business.daily_refund_cap_vnd` | | |
| `business.cost_budget_per_ticket_vnd` | | |
| `business.pilot_scope` (all / warehouse / percent) | | |
| `business.roi_min` | | |

### B7.5 · Câu 2.10 · Cổng con người, vận hành, pháp lý + Runbook phần 1–3

Điền `config/operating_gates.json` mục `operations` và `legal` (PIC, người duyệt, số người trực mỗi ca, công suất duyệt mỗi giờ,
thời gian chờ tối đa, điều kiện dừng, kênh báo tin; trường dữ liệu cá nhân không gửi cho bên thứ ba; ghi lỗi cho hãng phải có
nguyên nhân trong tracking). Rồi viết runbook dưới đây **khớp với các con số đó**.

*Runbook là tờ giấy người trực ca cầm lúc 23h khi có chuyện. Nó trả lời: nhìn con số nào, ngưỡng nào thì làm gì, ai được quyết.
Phần 1–3 và mục Giờ cao điểm viết ở vòng 1. Phần 4–5 viết ở vòng 2 (Phiếu C mục C11). Mọi con số phải khớp `config/operating_gates.json` và report.*
*Mỗi phần trả lời bốn câu hỏi: ai chịu trách nhiệm, nhìn gì, ngưỡng nào, làm gì.* **Người viết (vai Vận hành và pháp lý):** Thắng

#### Runbook 1 · Ai chịu trách nhiệm

| Vai | Tên / mã nhân viên (lấy từ `data/world.json` → `staff`) | Được quyền làm gì | Liên lạc qua kênh nào |
|---|---|---|---|
| PIC của trợ lý (một người) | Lê Thanh Tùng (`NV-TUNG`) — Giám sát vận hành, giữ công tắc tắt trợ lý | Quyết định dừng/thu hẹp pilot, kích hoạt cổng, xác nhận hệ thống đã tắt thao tác ghi | Teams `#pilot-gate1` |
| Người duyệt đứng tên các khoản vượt hạn mức | Trần Thị Hạnh (`NV-HANH`) — Trưởng ca CSKH | Duyệt khoản ngoại lệ, hoàn tiền vượt hạn mức hoặc trường hợp nguồn dữ liệu không nhất quán | Teams `#pilot-gate1`; ticket leo thang trong hệ thống |
| Người giữ công tắc tắt từng thao tác ghi | Lê Thanh Tùng (`NV-TUNG`) | Tắt `issue_refund`, `file_carrier_fault`, `notify_carrier` hoặc `send_reply` theo công tắc trong `config/switches.json` | Teams `#pilot-gate1`; xác nhận lại bằng log hệ thống |
| Người nhận khiếu nại của bên thứ ba (hãng, shop, người nhận quà) | Phạm Kiều Oanh (`NV-OANH`) — Kế toán đối soát | Tiếp nhận/đối soát tranh chấp, xác nhận dữ liệu hoàn sai hoặc PII gửi sai, phối hợp khôi phục bằng chứng | Teams `#pilot-gate1`; portal đối tác và sổ đối soát |

Số người trực duyệt mỗi ca: 1 (`NV-HANH`) · Mỗi giờ duyệt được: 6 ca/người · Phạm vi pilot: theo `business.pilot_scope`, khởi đầu `all`, được thu hẹp theo kho hoặc tỷ lệ khi cần

#### Runbook 2 · Nhìn con số nào, ngưỡng nào thì làm gì

Mỗi dòng một tín hiệu. Cột "Lấy ở đâu" phải là một dòng trong report của `lab10.eval` / `lab10.grade` hoặc một chỉ số trong `lab10/monitors.py`.

| Tín hiệu | Lấy ở đâu | Bình thường | Ngưỡng VÀNG → việc làm | Ngưỡng ĐỎ → việc làm | Ai quyết |
|---|---|---|---|---|---|
| Thời gian chờ người duyệt lâu nhất | Report `lab10.eval`/`lab10.grade`, khối kinh doanh-vận hành | Dưới 30 phút | Từ 30–60 phút: gọi `NV-HANH` hỗ trợ, ghi log hàng chờ, tạm thời chuyển ca sang người duyệt | Trên 60 phút: thu hẹp phạm vi hoặc dừng tự động hóa | `NV-TUNG`, tham vấn `NV-HANH` |
| Số ca bị ùn | Report kinh doanh-vận hành; `queue_stuck` | 0 ca | Có 1 ca bị chờ hơn 30 phút hoặc số hàng chờ tiến dần tới công suất 6 ca/giờ | Có ca chờ hơn 60 phút hoặc hàng chờ vẫn tăng sau khi có 1 người duyệt | `NV-TUNG` |
| Chi phí mỗi ticket so với làm tay | Report, `cost_per_ticket_vnd` và `ops_facts.manual_cost_per_ticket_vnd=10.000đ` | Chi phí ticket không vượt 10.000đ và ROI đạt ngưỡng đã ký | Chi phí gần giới hạn, chưa vượt làm tay: theo dõi 1 ca và giảm kiểm lại thủ công | Chi phí vượt làm tay hoặc ROI âm sau thu hẹp: dừng cải tiến, báo Sản phẩm & Kinh doanh | `NV-TUNG` phối hợp Sản phẩm |
| Tổng tiền hoàn tự động trong ngày so với trần | Report, `ctx.tools.auto_refund_today_vnd`, `business.daily_refund_cap_vnd` | Dưới 80% trần trong ngày | Từ 80–100% trần: chuyển khoản ngoại lệ và giảm `pilot_scope` nếu tải tăng | Vượt trần: dừng `issue_refund`, ticket chuyển `NV-HANH` duyệt | `NV-HANH` duyệt; `NV-TUNG` giữ công tắc |
| Tiền hoàn sai | Report `wrongful_refund_vnd`, tiêu chí đã ký (`wrongful_refund_vnd_max`) | 0đ | Chưa dùng ngưỡng vàng; bất kỳ tiền hoàn sai phát sinh đều coi là cảnh báo đỏ | Mọi sai khác 0đ sau xác nhận: dừng `issue_refund`, đảo ngược/đối soát theo quy trình | `NV-TUNG`, phối hợp `NV-OANH` |
| Lỗi ghi oan cho hãng / lộ dữ liệu cá nhân | Report, tiêu chí `wrongful_carrier_faults_max`/`pii_leaks_max`, monitor pháp lý | 0 lỗi/0 PII | Có 1 khiếu nại nghi ngờ nhưng chưa xác nhận: giữ trong hàng kiểm tra, tắt hoặc thu hẹp | Có bằng chứng ghi oan hoặc PII lộ: dừng `file_carrier_fault`/`notify_carrier` | `NV-TUNG`; `NV-OANH` xác nhận đối tác |
| Dispute Rate với hãng | Telemetry portal, Câu 1.4 | Dưới 0,5% | 0,5–1% trong ca: tăng kiểm tra mẫu 10–50%, báo cho `NV-HANH` | Trên 1% hoặc từ 2 hãng khiếu nại: tắt ghi lỗi/phạt hãng, mở điều tra | `NV-TUNG`, `NV-OANH` |

#### Runbook 3 · Điều kiện dừng và cách dừng

- Dừng một phần (tắt một thao tác ghi, thu hẹp phạm vi) khi:
  - thời gian chờ người duyệt vượt 60 phút;
  - tổng hoàn sai, PII hoặc tranh chấp hãng đạt bất kỳ ngưỡng đỏ đã xác nhận;
  - tổng hoàn tự động vượt trần hoặc ROI/chi phí rơi ngoài ngưỡng đã ký.
- Dừng hẳn khi:
  - phát hiện ít nhất một lỗi hoàn sai nghiêm trọng chưa thể đảo ngược;
  - xác nhận lộ PII cho bên thứ ba;
  - xác nhận có lỗi ghi/phạt oan cho hãng;
  - hàng chờ vẫn vượt 60 phút sau khi đã thu hẹp và gọi hỗ trợ.
- Cách dừng, từng bước (công tắc nào trong `config/switches.json`, dòng nào trong `config/operating_gates.json`):
  1. `NV-TUNG` xác nhận tín hiệu đỏ bằng report/portal và ghi giờ phát hiện.
  2. Tắt công tắc tương ứng trong `config/switches.json`:
     `issue_refund` cho hoàn sai/ngân sách;
     `file_carrier_fault` cho ghi lỗi oan;
     `notify_carrier` cho rò rỉ PII;
     `send_reply` nếu nội dung phản hồi có thể gây hiểu sai.
  3. Cập nhật `operations.stop_conditions`, `business.pilot_scope` và hẹn thông báo trong `Teams #pilot-gate1`.
  4. Chuyển toàn bộ ticket đang chờ sang `NV-HANH` hoặc xử lý tay; `NV-OANH` đối soát hoàn/phạt và hãng.
  5. Ghi mã thời điểm dừng, ticket bị ảnh hưởng và người xác nhận vào report/runbook.
- Từ tín hiệu đỏ đến lúc dừng xong tối đa 5 phút; người bấm: `NV-TUNG`
- Khi đã dừng, ticket đang chờ đi đâu, ai xử lý: Chuyển sang hàng duyệt tay của `NV-HANH`; `NV-OANH` đối soát dòng tiền và dữ liệu với hãng/shop
- Điều kiện để bật lại, ai ký: Nguyên nhân đã xác định, cổng/test đã chạy lại thành công, không còn vi phạm an toàn và có log đã khôi phục; `NV-TUNG` và `NV-HANH` ký xác nhận; `NV-OANH` ký phần đối soát pháp lý/dòng tiền

### B7.6 · Giờ cao điểm (bắt buộc với thẻ S4; các thẻ khác nên có)

Lượng ticket có thể dồn gấp ba trong một giờ (ngày sale, sau bão). Viết trước, khi chưa biết sự cố.

| Câu hỏi | Trả lời (có số, có tên) |
|---|---|
| Giờ cao điểm là khi nào, bao nhiêu ticket mỗi giờ (dựa vào `ops_facts`)? | Kích hoạt khi lượng ticket tăng gấp 3 trong 1 giờ, ví dụ ngày sale hoặc sau bão; tải cao điểm chỉ được xác nhận bằng report thực tế, không giả định cố định 42 ca/giờ |
| Ai trực giờ cao điểm, mấy người (khớp `operations.reviewers_on_shift`)? | `NV-HANH` trực ca chính và duyệt tối đa 6 ca/giờ; `NV-TUNG` giám sát và giữ công tắc dừng; ít nhất 1 người duyệt cho pilot bình thường |
| Ngưỡng nào thì **gọi thêm người** (hàng chờ bao nhiêu ca, chờ lâu nhất bao nhiêu phút)? Ai gọi? | Gọi thêm khi có ca chờ 30–60 phút hoặc hàng chờ làm công suất hiện tại vượt 6 ca/giờ/người. `NV-TUNG` gọi/điều người hỗ trợ; `NV-HANH` xác nhận tỷ lệ leo thang và SLA |
| Ngưỡng nào thì **thu hẹp** phạm vi (khoá `business.pilot_scope`) hoặc **tắt** một thao tác ghi (`config/switches.json`)? Ai quyết? | Thu hẹp/tắt khi hàng chờ vượt 60 phút, hoàn sai/PII/ghi oan phát sinh, hoặc tải làm vượt trần tài chính. `NV-TUNG` bấm công tắc; `NV-HANH` duyệt cao điểm và `NV-OANH` xác nhận tranh chấp bên ngoài |
| Thêm người thì chi phí mỗi ticket và ROI thay đổi thế nào (đọc report)? | Mỗi người trực thêm tốn 30.000đ/ca giữ chỗ. Chi phí ticket phải so với `manual_cost_per_ticket_vnd=10.000đ`; nếu chi phí vượt làm tay hoặc ROI không đạt, không thêm người mà thu hẹp theo kho/tỷ lệ |

---

<a id="b8"></a>

## B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 (phút 105–115)

Làm đúng thứ tự:

```bash
python3 -m lab10.checkpoint
python3 -m lab10.eval --suite base --stage prepared
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

**Khung tư duy.** Gate 1 "đạt" khi **quyết định khớp bằng chứng và khớp tiêu chí đã ký trước**. Tiếp tục, Thu hẹp, Cải tiến
thêm, Dừng đều có thể là quyết định đạt. Quyết định không đạt là quyết định mà con số trong report không đỡ được.
Chỉ chọn Tiếp tục khi mọi chỉ số bắt buộc đều đạt.

Ba câu tự vấn trước khi viết: (1) Rủi ro còn lại có chấp nhận được như hiện trạng không? (2) Cần thêm biện pháp nào, tốn
bao nhiêu thời gian? (3) Có phần nào của dự án không nên làm tiếp?

| | **v1** (phút 105–115, TRƯỚC khi nhận thẻ sự cố) |
|---|---|
| Commit ký tiêu chí (message `Sign acceptance criteria`; hash commit, tuỳ chọn) | |
| Hash chốt cổng vòng 1 (8 ký tự lệnh `lab10.checkpoint` in ra, tuỳ chọn) | |
| Mã lần chạy dùng làm bằng chứng | bộ nền, mốc base: ________ · bộ nền với cổng vòng 1 (prepared): ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | Tại mục kinh doanh-vận hành của report prepared: ghi từng dòng `[VƯỢT]` thực tế; nếu không có dòng vượt trần, ghi rõ "Không còn dòng vượt trần nào". Không suy ra trạng thái từ tiêu chí trước khi chạy report |
| Thẩm định vận hành của Trưởng ca CSKH | So sánh: số ca leo thang trong report prepared với công suất 1 người × 6 ca/giờ và SLA 60 phút. Nếu số ca tới/giờ × thời gian xử lý làm hàng chờ dự kiến vượt 60 phút, `NV-TUNG` thu hẹp pilot hoặc gọi thêm người; không chọn Tiếp tục |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Đọc khối "theo kho và hãng" ở cuối output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | Kho/hãng: ____ · Số xấu nhất (hoàn sai, lỗi hãng, PII, hàng chờ hoặc chi phí): ____ · Quyết định thay đổi khi chỉ nhìn phân khúc: có / không; lý do: ____ |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | Mã lần chạy prepared: ____ · Chỉ số: ____ · Giá trị thực tế: ____ · So ngưỡng đã ký: đạt / chưa đạt |
| Bằng chứng 2: hàng chờ và công suất duyệt | Mã lần chạy prepared: ____ · Số ca leo thang: ____ · Công suất thực tế: ____ ca/giờ · Hàng chờ dài nhất: ____ phút · Kết quả: đạt / chưa đạt SLA 60 phút |
| Bằng chứng 3: chi phí, ROI hoặc pháp lý | Mã lần chạy prepared: ____ · Chi phí/ROI/hoàn sai/lỗi hãng/PII: ____ · So ngưỡng đã ký: đạt / chưa đạt |
| Khớp dòng nào trong `decision_rule` đã ký? | Ghi nguyên văn một dòng `decision_rule` tương ứng với quyết định đã chọn; không viết quyết định chung chung |
| Nếu Thu hẹp: cắt phần nào, vì sao | Phạm vi cắt cụ thể (kho, tỷ lệ hoặc loại ticket): ____ · Tỷ lệ cắt: ____ · Lý do gắn với vượt trần hoặc SLA: ____ |
| Nếu Cải tiến thêm: giả thuyết cụ thể + hạn | Giả thuyết: ____ · Biện pháp sửa: ____ · Hạn hoàn thành: ____ · Tiêu chí xem lại: ____ |
| Nếu Dừng: bài học ghi lại | Rủi ro chính đã xác nhận: ____ · Dòng tiêu chí bị vượt: ____ · Thao tác đã tắt: ____ · Biện pháp xử lý khi đã dừng: ____ |
| Một bằng chứng còn thiếu (thứ bộ nền chưa đo được) | Ghi bằng chứng production chưa thể lấy từ 22 ticket × 5 seed, ví dụ phản hồi hãng 24–48 giờ, tranh chấp thực tế, tải khung giờ cao điểm hoặc sai lệch trong thời gian dài |
| Ngày quyết định lại (trừ khi Dừng) | ____ / ____ / ____ · Người theo dõi: `NV-TUNG` hoặc người được bàn ghi nhận |
| PIC ký | Lê Thanh Tùng (`NV-TUNG`) · Trạng thái ký: ký / chưa ký · Giờ ký: ____ |

Xong v1 thì lưu và đẩy một bản (sau mốc này không sửa cột v1):

```bash
git add lab10/guards.py lab10/guards_round1.py config/operating_gates.json config/operating_gates.round1.json config/round1.lock templates/form-b-evaluation-gates.md
git commit -m "LAB 10: chốt cổng vòng 1, quyết định v1"
git push -u origin main
```
