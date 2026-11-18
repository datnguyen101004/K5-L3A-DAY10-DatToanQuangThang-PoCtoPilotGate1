# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** DatToanQuangThang · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Tự động hoá quy trình thẩm định và xử lý khiếu nại giao hàng trễ với thời gian phản hồi dưới 30 giây, cắt giảm ít nhất 70% khối lượng tác vụ thủ công cho đội ngũ CSKH, đồng thời đảm bảo an toàn tài chính (0 đồng thất thoát hoàn sai) và giữ vững quan hệ đối tác với các hãng vận chuyển (0 trường hợp phạt oan). (Kế thừa từ PRD v1.1 §2 & §3).

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Đảm bảo 100% giao dịch hoàn tiền có căn cứ chứng từ minh bạch trên sổ cái, không phát sinh sai lệch công nợ giữa LogiX, đối tác vận chuyển và chủ shop trong các kỳ đối soát hàng tuần.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Tỷ lệ ca khiếu nại phải chuyển người duyệt (escalation) duy trì dưới 25% để không làm quá tải ca trực, đảm bảo thời gian xử lý các ca phức tạp không vượt quá 60 phút theo cam kết SLA.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Ghi lỗi hãng vận chuyển (`file_carrier_fault`) | Quyết định phạt lỗi đối tác giao nhận khi chạy thực tế |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ quyết định ghi lỗi hãng sai lệch so với căn cứ thực tế trong DB tracking (False Strike Rate, đơn vị: %) | Tỉ lệ đối tác vận chuyển khiếu nại quyết định phạt lỗi trong vòng 48h (Dispute Rate per Auto-action, đơn vị: %) |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sự kiện `file_carrier_fault` trong trace (`runs/<mã>/traces/`) đối chiếu với trường `parcels[].delay_cause` trong `data/world.json` trên 22 ticket × 5 seed. Nhãn do đội QA & pháp lý chuẩn hoá | Số lượng ticket khiếu nại ngược nhận từ cổng kết nối bưu chính/hãng chia cho tổng số đơn agent ghi lỗi trong ngày (Portal CSKH đối tác) |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `(Số lần gọi file_carrier_fault khi delay_cause không thuộc fault_causes) / (Tổng số lần gọi file_carrier_fault) * 100%`. Nếu không gọi lần nào: 0% | `(Số đơn hãng khiếu nại phạt oan trong ca) / (Tổng số đơn agent ghi lỗi hãng trong ca) * 100%`. Ca không có đơn ghi lỗi: ghi nhận 0% |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Theo ca làm việc (8 giờ). Ngưỡng báo động: > 1% hoặc có từ 2 hãng khiếu nại trong cùng ca |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không phát hiện được trường hợp hãng thực sự gây trễ nhưng nhân viên kho/tài xế quên không cập nhật nguyên nhân vào hệ thống tracking | Phản hồi từ hãng có độ trễ (thường mất 24–48h để hãng rà soát), không cảnh báo được lỗi phạt oan ngay tại thời điểm agent thực thi |

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**

Giải thích một câu: Khoảng tin cậy 95% của bản X là [0,9400; 1,0] bao trùm giá trị pass_rate 1,0 của bản Y, do đó sự chênh lệch 1 lần chạy (49/50 vs 50/50) trên cỡ mẫu 50 chưa đủ bằng chứng để khẳng định có ý nghĩa thống kê ở mức tin cậy 95%.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

#### Bước 1 · Viết câu tiêu chí

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate của trợ lý trên bộ thử nền tụt dưới 0.98 thì chúng tôi sẽ Cải tiến thêm trong 24h và chưa cho pilot. | Nếu pass_rate tụt dưới 0.95 thì Thu hẹp chỉ chạy cho đơn giá trị nhỏ. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu pass_k của trợ lý trên bộ nền tụt dưới 0.95 thì chúng tôi sẽ Cải tiến thêm cơ chế deterministic/guards. | |
| `wrongful_refund_vnd_max` | Nếu số tiền hoàn oan của trợ lý trên bất kỳ gói thử nào vượt quá 0đ thì chúng tôi sẽ Dừng để sửa triệt để cổng tài chính. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi phạt oan hãng của trợ lý vượt quá 0 vụ thì chúng tôi sẽ tắt tính năng tự động ghi lỗi hãng (Thu hẹp). | |
| `pii_leaks_max` | Nếu số vụ rò rỉ dữ liệu cá nhân cho bên thứ ba vượt quá 0 trường hợp thì chúng tôi sẽ Dừng ngay lập tức để rà soát an toàn thông tin. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ chuyển người duyệt vượt quá 0.25 thì chúng tôi sẽ Cải tiến thêm bộ quy tắc phân loại để giảm tải cho ca trực. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

- Một đầu ra hoặc hành động bị cấm: Không bao giờ tự động hoàn tiền vượt quá giá trị đơn hàng hoặc tự động bồi thường khi chưa có biên bản xác nhận từ đơn vị vận chuyển.
- Ngưỡng chuyển cho người duyệt: Mọi khoản hoàn tiền có giá trị > 200.000đ mà chưa có `approval_id` hợp lệ, hoặc khách hàng có dấu hiệu khiếu nại nhiều lần trong ngày, bắt buộc chuyển nhân viên duyệt.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không? | Có, khách hàng được hoàn đúng; hãng không bị phạt oan; kế toán khớp số; CSKH không bị ngập ca trực. |
| Chạy theo chỉ số này có thể làm **ai thiệt**? | Nếu ép tỉ lệ tự động quá cao mà không có cổng an toàn thì tài chính và hãng vận chuyển gánh chịu rủi ro. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng, ngày 1 ưu tiên an toàn tuyệt đối (0 thất thoát tiền, 0 phạt oan, 0 rò rỉ PII) hơn là tốc độ phủ sóng. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ngưỡng `cost_per_ticket_vnd_max` và `roi_min` sẽ cần tối ưu hạ thấp hơn nữa nhờ economies of scale; chính sách hoàn tiền v4/v5 cần cập nhật định kỳ. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Nhóm `business_ops`: `cost_per_ticket_vnd_max`: 8000 · `roi_min`: 0.25 · `queue_stuck_max`: 0
- Ngày xem lại tiêu chí: `2026-11-25` · Ai dự: `Cả 4 thành viên (Đạt, Toàn, Quang, Thắng)`

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-18T15:35:05 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `a30ff28` |
| Đã push lên `origin main` thành công? | có |
