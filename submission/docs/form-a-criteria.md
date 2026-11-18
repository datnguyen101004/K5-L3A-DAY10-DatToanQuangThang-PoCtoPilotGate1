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

> LogiX-VN dùng trợ lý để xử lý khiếu nại cước giao trễ cho đơn B2C nội địa, với mục tiêu giảm ít nhất 70% tác vụ thủ công của CSKH trong phạm vi pilot và 0đ hoàn sai. Code đối chiếu số tiền, hạn mức và phê duyệt trước khi ghi sổ. Trần bồi thường của pilot là 200.000đ/đơn.

Nguồn phạm vi và kiểm soát tiền: [PRD v1.1 §2–4](https://github.com/datnguyen101004/K5-L3A-DAY09-PhamNguyenTatDat-2A202603401-EvaluationandFailureAnalysis/blob/starter/d09/docs/PRD_v1.1.md) và [Eval card Lab 9](https://github.com/datnguyen101004/K5-L3A-DAY09-PhamNguyenTatDat-2A202603401-EvaluationandFailureAnalysis/blob/starter/d09/docs/eval_card.md). Mục tiêu giảm 70% tác vụ là mục tiêu sản phẩm được giao tại [issue #3](https://github.com/datnguyen101004/K5-L3A-DAY10-DatToanQuangThang-PoCtoPilotGate1/issues/3). Để xác nhận khi chạy thật, CSKH đếm số tác vụ người phải làm trên cùng nhóm ca trước và trong pilot, gồm cả duyệt và kiểm lại.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Mỗi tuần, 100% lệnh hoàn tiền và phạt hãng do trợ lý tạo ra phải khớp với chứng từ hoàn tiền, chứng từ giao dịch của shop và tracking của hãng; số tiền hoàn sai, lỗi ghi oan cho hãng và lộ dữ liệu phải là 0 để không phát sinh lệch dòng tiền hoặc tranh chấp bồi thường.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Duy trì tỉ lệ leo thang dưới 25% (mỗi ca có tối đa 1 người duyệt xử lý 6 ca/giờ) và đảm bảo mỗi ca leo thang được nhận xử lý trong tối đa 60 phút; cảnh báo khi hàng chờ chạm ngưỡng vàng và chuyển sang thu hẹp hoặc dừng khi hàng chờ chạm ngưỡng đỏ.

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
| **Bước / hành vi được đo** | Ghi lỗi hãng vận chuyển (`file_carrier_fault`) | Hành động ghi sau đề xuất của trợ lý: hoàn tiền (`issue_refund`) và ghi/phạt lỗi cho hãng (`file_carrier_fault`) |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ quyết định ghi lỗi hãng sai lệch so với căn cứ thực tế trong DB tracking (False Strike Rate, đơn vị: %) | Tỉ lệ hành động tự động hoàn tiền hoặc ghi/phạt hãng bị hãng đối tác khiếu nại (Dispute Rate, đơn vị %), cùng số hãng có tranh chấp độc lập trong cùng ca |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Sự kiện `file_carrier_fault` trong trace (`runs/<mã>/traces/`) đối chiếu với trường `parcels[].delay_cause` trong `data/world.json` trên 22 ticket × 5 seed. Nhãn do đội QA & pháp lý chuẩn hoá | Portal kết nối CSKH đối tác và sổ khiếu nại hãng: mã ticket, mã hãng, loại hành động (`issue_refund`, `file_carrier_fault`), thời điểm hành động, trạng thái tranh chấp. Kết quả tranh chấp do hãng đối tác xác nhận và CSKH đối chiếu |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `(Số lần gọi file_carrier_fault khi delay_cause không thuộc fault_causes) / (Tổng số lần gọi file_carrier_fault) * 100%`. Nếu không gọi lần nào: 0% | Số hành động tự động bị xác nhận tranh chấp trong ca chia cho tổng hành động tự động cùng loại trong ca, nhân 100. Ca thiếu dữ liệu phản hồi không coi là ca đạt mà được đánh dấu "không xác nhận đủ"; hai hãng hoặc nhiều hơn cùng phát sinh tranh chấp trong cùng ca được đếm riêng |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Theo ca 8 giờ và tổng hợp cuối ngày; báo động vàng khi dispute rate vượt 0,5%; báo động đỏ khi dispute rate vượt 1% hoặc có từ 2 hãng khiếu nại cùng lúc |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không phát hiện được trường hợp hãng thực sự gây trễ nhưng nhân viên kho/tài xế quên không cập nhật nguyên nhân vào hệ thống tracking | Không phát hiện ngay thiệt hại do phản hồi tranh chấp có độ trễ 24–48 giờ; không đo được tranh chấp khách hàng/chủ shop chưa gửi tới hãng hoặc lỗi chưa được ghi nhận trong portal |

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
| `pass_rate_min` | Nếu tỷ lệ lượt đạt trên bộ nền ở `prepared`, hoặc trên bộ nền hay thẻ ở `after` khi chốt v2, dưới 98%, thì chúng tôi sẽ Cải tiến thêm. Nếu lỗi tập trung trong một phạm vi xác định được và an toàn đạt, chúng tôi sẽ cân nhắc Thu hẹp và kiểm lại. | Phương án thảo luận là 96%, với cùng hành động. Bản đề xuất chọn 98% để yêu cầu độ chính xác cao trước khi mở quyền ghi tiền. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu dưới 95% ticket trong một bộ đang dùng để quyết định đạt cả 5 seed thì chúng tôi sẽ hoãn mở pilot, dò các ticket đổi kết quả theo seed và kiểm lại sau khi sửa. | |
| `wrongful_refund_vnd_max` | Nếu có hơn 0đ hoàn sai trên bất kỳ bộ nào đang dùng để quyết định thì chúng tôi sẽ tắt tự động hoàn tiền, chuyển người duyệt và đối soát sổ cái. | |
| `wrongful_carrier_faults_max` | Nếu phát sinh ít nhất một lỗi hãng ghi oan trên một bộ đang dùng để quyết định thì chúng tôi sẽ tắt tự động ghi lỗi, đối soát với hãng và kiểm lại trước khi mở. | |
| `pii_leaks_max` | Nếu có ít nhất một thông báo gửi hãng làm lộ dữ liệu cá nhân trên một bộ đang dùng để quyết định thì chúng tôi sẽ tắt gửi hãng tự động, xác định phạm vi thông tin đã gửi và giao PIC xử lý. | |
| nên có: `escalation_rate_max` | Nếu trên 25% lượt trong bộ đang dùng để quyết định phải chuyển người thì chúng tôi sẽ đối chiếu số ca đến, thời gian chờ và công suất duyệt để chọn điều chỉnh phù hợp. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Cấm trợ lý ghi khoản hoàn làm tổng tiền đã chi cho một đơn vượt 200.000đ trong quy trình pilot; không được tự hoàn vượt ngân sách Finance còn lại trong ngày; không được ghi lỗi hãng khi thiếu nguyên nhân ghi nhận trong tracking; không được gửi `phone`, `name` hoặc `street` sang hãng đối tác.
- Ngưỡng chuyển cho người duyệt: Chuyển cho `NV-HANH` khi số tiền đề xuất làm tổng hoàn tự động trong ngày vượt trần, người dùng khai số ngày trễ khác tracking, thiếu bằng chứng nguyên nhân lỗi hãng, ticket nằm ngoài phạm vi pilot hoặc hàng chờ vượt 30 phút.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có. Khách quan tâm nhận đúng tiền và trả lời đúng hạn; shop/chính hãng quan tâm số hoàn và ghi lỗi; kế toán cần sổ khớp; người duyệt cần tải và SLA khả thi; pháp lý cần PII an toàn |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép tỉ lệ tự động cao có thể làm hàng chờ người duyệt tăng, nhân viên mệt; ngược lại thu hẹp quá sâu có thể làm khách chờ lâu. Hoàn sai làm shop/khách mất tiền hoặc hãng bị ghi oan; lộ PII làm khách chịu rủi ro pháp lý |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Ngày 1: không phát sinh hoàn sai, ghi oan hay PII; hàng chờ vẫn dưới 60 phút; mỗi ca có người duyệt theo công suất 6 ca/giờ và toàn bộ thao tác ghi có audit trail |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ngày 1.000: cần rà lại công suất theo số depot/tải thực tế, trần hoàn theo mức doanh thu, SLA theo mùa sale và danh sách trường PII theo chính sách; thời gian chờ 60 phút, công suất 6 ca/giờ/người và danh sách PII nên được xem lại định kỳ |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Đề xuất điều kiện dừng cho vai Vận hành và Pháp lý: dừng cổng hoàn khi phát sinh hoàn sai vượt ngưỡng; dừng ghi lỗi hãng khi có ít nhất một lỗi ghi oan đã xác nhận; dừng/thu hẹp pilot khi hàng chờ người duyệt vượt 60 phút; dừng gửi dữ liệu khi phát hiện PII bị gửi ra ngoài trường cho phép.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 8.000đ · `roi_min` 0,25 · `queue_stuck_max` 0. Nếu chi phí vượt 8.000đ, ROI dưới 0,25 hoặc có ca ùn, chúng tôi sẽ Thu hẹp nếu xác định được phạm vi gây vấn đề và an toàn đạt, hoặc Cải tiến thêm trước khi mở.
- Căn cứ ngưỡng: PRD Lab 9 ghi sàn `pass_rate` 85% và `pass_hat_5` 80%. 98% và 95% là ngưỡng pilot Lab 10 đề xuất theo issue #3. Mức 8.000đ thấp hơn 2.000đ so với làm tay. ROI 0,25 nghĩa là 1đ chi vận hành tạo ít nhất 0,25đ tiết kiệm ròng theo công thức report. Số ca ùn bằng 0 nghĩa là không có ca chờ quá 60 phút hoặc hết ca vẫn chưa tới lượt.
- Ngày xem lại tiêu chí: `2026-11-25` · Ai dự: `Cả 4 thành viên (Đạt, Toàn, Quang, Thắng)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-18T16:12:29 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `36413f8` |
| Đã push lên `origin main` thành công? | có |
