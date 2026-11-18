# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

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

> …

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
| **Bước / hành vi được đo** | (Kỹ sư cổng điền offline metric) | Hành động ghi sau đề xuất của trợ lý: hoàn tiền (`issue_refund`) và ghi/phạt lỗi cho hãng (`file_carrier_fault`) |
| **Thước đo** (một câu, có đơn vị) | | Tỉ lệ hành động tự động hoàn tiền hoặc ghi/phạt hãng bị hãng đối tác khiếu nại (Dispute Rate, đơn vị %), cùng số hãng có tranh chấp độc lập trong cùng ca |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | Portal kết nối CSKH đối tác và sổ khiếu nại hãng: mã ticket, mã hãng, loại hành động (`issue_refund`, `file_carrier_fault`), thời điểm hành động, trạng thái tranh chấp. Kết quả tranh chấp do hãng đối tác xác nhận và CSKH đối chiếu |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | Số hành động tự động bị xác nhận tranh chấp trong ca chia cho tổng hành động tự động cùng loại trong ca, nhân 100. Ca thiếu dữ liệu phản hồi không coi là ca đạt mà được đánh dấu "không xác nhận đủ"; hai hãng hoặc nhiều hơn cùng phát sinh tranh chấp trong cùng ca được đếm riêng |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Theo ca 8 giờ và tổng hợp cuối ngày; báo động vàng khi dispute rate vượt 0,5%; báo động đỏ khi dispute rate vượt 1% hoặc có từ 2 hãng khiếu nại cùng lúc |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | Không phát hiện ngay thiệt hại do phản hồi tranh chấp có độ trễ 24–48 giờ; không đo được tranh chấp khách hàng/chủ shop chưa gửi tới hãng hoặc lỗi chưa được ghi nhận trong portal |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | | |
| `wrongful_refund_vnd_max` | | |
| `wrongful_carrier_faults_max` | | |
| `pii_leaks_max` | | |
| nên có: `escalation_rate_max` | | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý không được tự hoàn vượt ngân sách Finance còn lại trong ngày, không được ghi lỗi hãng khi thiếu nguyên nhân ghi nhận trong tracking, không được gửi `phone`, `name` hoặc `street` sang hãng và không được tự duyệt khoản ngoại lệ đã có quy định chuyển người.
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
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` ____ · `roi_min` ____ · `queue_stuck_max` ____
- Ngày xem lại tiêu chí: `__________` · Ai dự: `__________` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
