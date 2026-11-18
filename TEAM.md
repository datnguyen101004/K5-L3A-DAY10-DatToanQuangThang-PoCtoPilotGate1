# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): DatToanQuangThang
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-DatToanQuangThang-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Phạm Nguyễn Tất Đạt | 2A202603401 | Kỹ sư cổng | Có |
|   2 | Nguyễn Ngọc Toàn | 2A202603405 | Kỹ sư cổng | Không |
|   3 | Nguyễn Tuấn Quang | 2A202603392 | Sản phẩm và kinh doanh | Không |
|   4 | Kiều Văn Thắng |2A202603424 | Vận hành và pháp lý | Không |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## PhamNguyenTatDat-2A202603401

### Phần việc phụ trách

Vai: Kỹ sư cổng 1 (Lead Gate Engineer) kiêm Trưởng nhóm.
Phụ trách:
- Khối 1: Chọn PRD v1.1 và Eval Card từ Lab 9 làm bản quy chuẩn; thiết kế Offline Metric cho bước ghi lỗi hãng (Câu 1.3, Phiếu A mục A2); thảo luận và giải thích khoảng tin cậy (Câu 1.5, Phiếu A mục A3); chủ trì ký niêm phong Bản tiêu chí chấp nhận (`config/acceptance_criteria.json`).
- Khối 2: Chạy đánh giá mốc base và so cổng mốc nền (Câu 2.1, Phiếu B mục B1); phân tích trace ca lỗi `T-002@55` (Câu 2.2, Phiếu B mục B2); tham gia Pre-mortem 4 lăng kính (Câu 2.5); lập trình các cổng an toàn trong `lab10/guards.py` (`pre_guard` và `write_gate`) (Câu 2.6, Phiếu B mục B7.1); chốt mốc `prepared` bằng `checkpoint` và đánh giá mốc prepared; cùng nhóm ra Quyết định Gate 1 v1 (Phiếu B mục B8).

### Đóng góp cụ thể

- Thiết kế chỉ số False Strike Rate (Tỉ lệ phạt oan hãng vận chuyển) đo lường mức bước đối chiếu trực tiếp dữ liệu tracking.
- Phân tích nguyên nhân gốc của `T-002@55` bắt nguồn từ lỗi `FM-03: ticket_trust` (LLM tin số ngày khách khai khống hơn tracking DB).
- Lập trình 3 cổng phòng ngừa trong `lab10/guards.py`:
  1. Cổng đối chiếu quyền lợi DB (`H.entitlement_vnd`), chặn hoàn tiền vượt quyền lợi.
  2. Cổng bảo vệ hãng vận chuyển, chặn ghi phạt khi tracking không ghi nhận lỗi hãng.
  3. Cổng lọc PII (`recipient_contact`) đối với đơn hàng quà tặng khi gửi thông báo sang đối tác.
- Chốt mốc checkpoint `prepared` đạt 100% pass trên 22 ticket bộ nền (110/110 trials), 0đ hoàn oan, 0 lỗi hãng oan, 0 rò rỉ PII.

### Bằng chứng

- Commit ký tiêu chí: `Sign acceptance criteria`.
- Mã lần chạy base & prepared trong `runs/`.
- File code cổng: `lab10/guards.py` và bản chụp `lab10/guards_round1.py`.

### Exit ticket

- Một điều học được: Thấu hiểu tầm quan trọng của việc "ký tiêu chí trước khi nhìn kết quả đo" để loại bỏ hoàn toàn thiên kiến xác nhận (confirmation bias), và việc dựng cổng kiểm soát cấp hệ thống (system-level guards) nằm ngoài model prompt là lá chắn tin cậy nhất để ngăn chặn hallucination.
- Một điều còn chưa chắc: Khi đưa vào môi trường production tải cao với nhiều trường hợp đơn phức tạp (giao nhiều chặng, đổi địa chỉ giữa chừng), cơ chế đồng bộ giữa tracking DB và sổ cái đối soát có thể gặp độ trễ dẫn đến phán đoán sai lệch.

## KieuVanThang-2A202603424

### Phần việc phụ trách

Vai: Chuyên viên Vận hành và Pháp lý.

Phụ trách:
- Khối 1: Mục tiêu hai nhân sự cốt lõi, telemetry production, điều kiện dừng và ranh giới an toàn.
- Khối 2: HAZOP, checklist 9 nhóm việc, pre-mortem, cổng vận hành/pháp lý, Runbook 1–3 và giờ cao điểm.
- Khối 3: Thẻ S4, HAZOP mở rộng, giả định môi trường, điều chỉnh staffing và stop conditions, Risk register, Runbook 4–5 và hoàn tất submission.

### Đóng góp cụ thể

- Xác lập PIC, approver và công suất duyệt cho ca thường và ca sale.
- Thêm cơ chế hai người duyệt trong cấu hình vòng 2; giữ SLA chờ 60 phút và ngưỡng gọi hỗ trợ khi chờ đạt 30 phút.
- Thêm điều kiện dừng khi tổng hoàn ngày sale chạm 300.000đ, đồng thời giữ nguyên trần/lock vòng 1.
- Hoàn thiện phần riêng S4 trong Phiếu C, fault tree vận hành/pháp lý, risk register và runbook phục hồi/nâng cấp.

### Bằng chứng

- `R-S4-before-20261118-165250-123c47`, `R-S4-prepared-20261118-165250-123c47`, `R-S4-after-20261118-165250-123c47`
- `R-S4-grade-20261118-165250-123c47`
- Mục C1, C3, C4, C5, C7, C9, C10, C11 và C12 trong `templates/form-c-incident.md`
- Cấu hình `operations` và `legal` trong `config/operating_gates.json`

### Exit ticket

- Một điều học được: tải cao làm người duyệt trở thành bộ phận chặn ngang với model/tool; staffing, SLA và thủ tục dừng phải được đo và duy trì cùng cổng kỹ thuật.
- Một điều còn chưa chắc: người dự phòng có thực sự sẵn sàng trong ca sale và phản hồi tranh chấp hãng/shop sau 24–48 giờ production chưa được mô phỏng đầy đủ.
