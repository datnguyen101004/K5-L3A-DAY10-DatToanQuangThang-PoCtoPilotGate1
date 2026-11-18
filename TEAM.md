# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): DatToanQuangThang
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-DatToanQuangThang-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S4

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Phạm Nguyễn Tất Đạt | 2A202603401 | Kỹ sư cổng | Có |
|   2 | Nguyễn Ngọc Toàn | 2A202603405 | Kỹ sư cổng | Không |
|   3 | Nguyễn Tuấn Quang | 2A202603392 | Sản phẩm và kinh doanh | Không |
|   4 | Kiều Văn Thắng | 2A202603424 | Vận hành và pháp lý | Không |

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

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
