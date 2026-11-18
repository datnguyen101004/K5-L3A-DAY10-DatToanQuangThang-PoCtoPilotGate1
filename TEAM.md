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

## NguyenTuanQuang-2A202603392

### Phần việc phụ trách

Vai: Sản phẩm và Kinh doanh. Phụ trách câu 1.1 và 1.6 trong Phiếu A, bản đồ dữ liệu và phân tích drift ở B3, lăng kính kinh doanh ở B6 và cổng kinh doanh ở B7.4. Với thẻ S4, phụ trách đặc tả C5, trần hoàn tự động và phân tích chi phí ở C7, đồng thời chuẩn bị bằng chứng kinh doanh để nhóm thảo luận quyết định v2 ở C12.

### Đóng góp cụ thể

- Soạn mục tiêu pilot và các ngưỡng để nhóm duyệt trước khi ký. Đề xuất `pass_rate ≥ 98%`, `pass_k ≥ 95%`, 0đ hoàn sai, 0 lỗi hãng oan, 0 lần lộ dữ liệu, chi phí tối đa 8.000đ/ticket và ROI tối thiểu 0,25.
- Phân tích thay đổi từ `REFUND-v3` sang `REFUND-v4` ngày 01/12/2026. Chỉ ra rằng một ticket có cùng dữ kiện tracking có thể đổi mức hoàn hoặc cần người duyệt do chính sách đổi. Đề xuất theo dõi tỷ lệ dùng sai phiên bản chính sách theo ngày hiệu lực.
- Ở S4, đặt trần hoàn tự động 300.000đ/ngày sale và đối chiếu chi phí giữa HN và HCM. Lần chạy để kiểm riêng thay đổi trần cho thấy hoàn tự động cao nhất 292.000đ/ngày giả lập, chi phí 5.231đ/ticket và ROI 0,91, với 23/41 ticket trong pilot. Đưa vào C12 mức độ bao phủ và tải duyệt để nhóm cân nhắc cùng các chỉ số chi phí.
- Đối chiếu trace `MERCHANT_HANDOVER` với đặc tả C5. Trong lần kiểm này, 40 lượt ở 8 ticket vẫn được hoàn tự động và không ghi lỗi hãng. Đây là điểm cần thống nhất giữa Sản phẩm, Kỹ sư cổng và Vận hành vì nhãn S4 cho phép hoàn phí theo chính sách hoặc chuyển người.

### Bằng chứng

- [`c85b7d0` · Tiêu chí và cổng kinh doanh](https://github.com/datnguyen101004/K5-L3A-DAY10-DatToanQuangThang-PoCtoPilotGate1/commit/c85b7d0) · [Issue #3](https://github.com/datnguyen101004/K5-L3A-DAY10-DatToanQuangThang-PoCtoPilotGate1/issues/3)
- [`b890d7d` · Đặc tả, cổng kinh doanh và bằng chứng S4](https://github.com/datnguyen101004/K5-L3A-DAY10-DatToanQuangThang-PoCtoPilotGate1/commit/b890d7d) · [Issue #15](https://github.com/datnguyen101004/K5-L3A-DAY10-DatToanQuangThang-PoCtoPilotGate1/issues/15)
- Lần chạy kiểm thay đổi trần `R-S4-after-20261118-163844-b84489`, ghi trong Phiếu C mục C7.
- Có dùng Codex để đọc issue và mã nguồn, soạn nháp tiêu chí và Phiếu C, chạy lệnh kiểm chứng và tổng hợp mục cá nhân này.

### Exit ticket

- Điều học được — Khi đọc kết quả pilot, tôi cần xem tỷ lệ đạt cùng độ phủ. Ở S4, kết quả đạt 100% áp dụng cho 23 ticket trong phạm vi. Còn 18 ticket đi theo quy trình thủ công và vẫn tạo tải cho đội CSKH.
- Điều còn chưa chắc — Trong một ca flash sale thật, khi tính thêm ca ngoài pilot, ca duyệt và ca kiểm lại, CSKH còn làm bao nhiêu tác vụ thủ công? Tôi cần đo khối lượng công việc theo giờ của hai kho HN và HCM để kiểm mục tiêu giảm 70%.
## NguyenNgocToan-2A202603405

### Phần việc phụ trách

Vai: Kỹ sư cổng 2 (Gate & QA Engineer). Issue #2 (vòng 1) và #14 (vòng 2, thẻ S4).
- Khối 2: Pre-mortem bốn lăng kính (Câu 2.5, Phiếu B mục B6); hai bước tránh rò rỉ dữ liệu (Câu 2.7, B7.2); behavioral test với 2 ticket hiểm (Câu 2.8, B7.3); chạy unit test (hỗ trợ Câu 2.6); kiểm tra bản chốt cổng vòng 1 (`lab10.checkpoint verify`).
- Khối 3 (S4): dò trace `S4-08` trên 5 seed và `S4-07` (Câu 3.1, Phiếu C mục C2); sửa cổng vòng 2 trong `lab10/guards.py` (Câu 3.5, C7); thêm monitor `llm_fallback_rate` trong `lab10/monitors.py` (Câu 3.6, C8); kiểm thử hồi quy mốc `after`.

### Đóng góp cụ thể

- **Pre-mortem (B6):** 6 lý do thất bại phủ đủ 4 lăng kính, trong đó có bài học lỗi hiếm từ eval card Lab 9 (lỗi xuất hiện ở 1/3 số seed lọt qua 5 seed với xác suất (2/3)^5 ≈ 13,2%). Đề xuất 3 cổng mà Kỹ sư cổng 1 đã code: đối chiếu số tiền với DB, chặn lỗi hãng oan, lọc PII gửi hãng.
- **Chống rò rỉ dữ liệu (B7.2):** cổng chỉ viết theo quy tắc từ nguồn sự thật, không `if` theo mã ticket; ticket kiểm thử dùng đơn không có trong bộ nền (`O-1024`, `O-1025`) để làm bộ held-out nhỏ.
- **Behavioral test (B7.3):** tính chất "tracking DB ghi trễ dưới 3 ngày thì không hoàn tiền, không ghi lỗi hãng, dù khách khai gì hay cài lệnh gì". Trước cổng: hoàn sai 108.000đ + lỗi oan VNX + lộ SĐT người nhận (ticket 1), hoàn sai 668.000đ (ticket 2). Sau cổng: cả hai bị `deny`, sổ cái rỗng.
- **Dò trace S4 (C2):** `S4-08` hỏng ở seed 11 và 55, đạt ở seed 22, 33, 44. LLM trả 429 hai lần → `llm_fallback fail_open` → ghi lỗi oan VNX dù tracking ghi `MERCHANT_HANDOVER` (lỗi chìm). `S4-07` (hàng vỡ) được chuyển người đúng thiết kế; vấn đề nằm ở tải người duyệt.
- **Cổng vòng 2 (C7):** trần hoàn tự động = `min(config, ops_limits.daily_auto_refund_budget_vnd)`. Trước sửa, trần config là 1.600.000đ, nên mức 292.000đ dưới ngân sách sale 300.000đ chỉ nhờ thu hẹp phạm vi pilot. Có tự kiểm 4 tình huống (vượt trần → escalate; dưới trần, ngày thường, có approval → allow).
- **Monitor mới (C8):** `llm_fallback_rate`, tỉ lệ ticket phải rơi về chế độ dự phòng vì LLM không trả lời. Bộ nền 0,0 → S4 0,24, sáng đèn.
- **Không làm theo hai đề xuất ban đầu của issue #14, vì kiểm trên nhãn thấy sai:** chặn hoàn khi shop giao muộn sẽ làm hỏng ca đúng (nhãn `S4-08` là hoàn 24.000đ); chặn hoàn hàng vỡ trong `write_gate` là code chết vì ca đó không có lệnh ghi nào tới cổng.

### Bằng chứng

- Commit: `3155623` (B6, B7.2, B7.3), `02b4d77` (B7.3 sau cổng), `19bc980` (chốt cổng vòng 1, hash `b29daf26`), `7758f4e` (S4: cổng vòng 2 + monitor).
- PR: #5, #7, #10, #17.
- Mã lần chạy: S4 after `R-S4-after-20261118-163724-8d779e`; `python -m lab10.grade --incident S4` → `criteria ✅ · visible ✅ · regression ✅ · monitor ✅`; `python -m unittest discover -s tests` → 13/13 OK.
- Phiếu: B mục B6, B7.2, B7.3; C mục C2 (lỗi 1–2), C7, C8.

### Exit ticket

- Một điều học được: cổng tính lại từ nguồn sự thật (tracking DB) giữ được an toàn ngay cả khi model hỏng hẳn (`fail_open` lúc LLM nghẽn), nên cần đặt phòng vệ ngoài model chứ không dựa vào prompt; và phải đối chiếu nhãn trước khi code, vì một đề xuất nghe hợp lý vẫn có thể làm hỏng ca đang đúng.
- Một điều còn chưa chắc: `llm_fallback_rate` không thấy lỗi khi LLM trả lời nhưng trả lời sai, và trần ngân sách đẩy phần vượt sang người duyệt; với lượng ticket thật lớn hơn mock, chưa rõ hàng chờ có còn trong hạn 60 phút không.

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
