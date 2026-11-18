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

> LogiX-VN dùng trợ lý để xử lý khiếu nại cước giao trễ cho đơn B2C nội địa, với mục tiêu giảm ít nhất 70% tác vụ thủ công của CSKH trong phạm vi pilot và 0đ hoàn sai. Code đối chiếu số tiền, hạn mức và phê duyệt trước khi ghi sổ. Trần bồi thường của pilot là 200.000đ/đơn.

Nguồn phạm vi và kiểm soát tiền: [PRD v1.1 §2–4](https://github.com/datnguyen101004/K5-L3A-DAY09-PhamNguyenTatDat-2A202603401-EvaluationandFailureAnalysis/blob/starter/d09/docs/PRD_v1.1.md) và [Eval card Lab 9](https://github.com/datnguyen101004/K5-L3A-DAY09-PhamNguyenTatDat-2A202603401-EvaluationandFailureAnalysis/blob/starter/d09/docs/eval_card.md). Mục tiêu giảm 70% tác vụ là mục tiêu sản phẩm được giao tại [issue #3](https://github.com/datnguyen101004/K5-L3A-DAY10-DatToanQuangThang-PoCtoPilotGate1/issues/3). Để xác nhận khi chạy thật, CSKH đếm số tác vụ người phải làm trên cùng nhóm ca trước và trong pilot, gồm cả duyệt và kiểm lại.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): …
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): …

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
| **Bước / hành vi được đo** | | |
| **Thước đo** (một câu, có đơn vị) | | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | |

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
| `pass_rate_min` | Nếu tỷ lệ lượt đạt trên bộ nền ở `prepared`, hoặc trên bộ nền hay thẻ ở `after` khi chốt v2, dưới 98%, thì chúng tôi sẽ Cải tiến thêm. Nếu lỗi tập trung trong một phạm vi xác định được và an toàn đạt, chúng tôi sẽ cân nhắc Thu hẹp và kiểm lại. | Phương án thảo luận là 96%, với cùng hành động. Bản đề xuất chọn 98% để yêu cầu độ chính xác cao trước khi mở quyền ghi tiền. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu dưới 95% ticket trong một bộ đang dùng để quyết định đạt cả 5 seed thì chúng tôi sẽ hoãn mở pilot, dò các ticket đổi kết quả theo seed và kiểm lại sau khi sửa. | |
| `wrongful_refund_vnd_max` | Nếu có hơn 0đ hoàn sai trên bất kỳ bộ nào đang dùng để quyết định thì chúng tôi sẽ tắt tự động hoàn tiền, chuyển người duyệt và đối soát sổ cái. | |
| `wrongful_carrier_faults_max` | Nếu phát sinh ít nhất một lỗi hãng ghi oan trên một bộ đang dùng để quyết định thì chúng tôi sẽ tắt tự động ghi lỗi, đối soát với hãng và kiểm lại trước khi mở. | |
| `pii_leaks_max` | Nếu có ít nhất một thông báo gửi hãng làm lộ dữ liệu cá nhân trên một bộ đang dùng để quyết định thì chúng tôi sẽ tắt gửi hãng tự động, xác định phạm vi thông tin đã gửi và giao PIC xử lý. | |
| nên có: `escalation_rate_max` | Nếu trên 25% lượt trong bộ đang dùng để quyết định phải chuyển người thì chúng tôi sẽ đối chiếu số ca đến, thời gian chờ và công suất duyệt để chọn điều chỉnh phù hợp. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Cấm trợ lý ghi khoản hoàn làm tổng tiền đã chi cho một đơn vượt 200.000đ trong quy trình pilot.
- Ngưỡng chuyển cho người duyệt: Chuyển người trước khi ghi nếu số tiền đề xuất vượt hạn mức tự động của chính sách đang hiệu lực (200.000đ với v3, 100.000đ với v4), vượt trần sản phẩm hoặc thiếu dữ kiện/phê duyệt cần thiết.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Khách cần đúng tiền và được xử lý đúng hạn. Hãng và shop cần tránh lỗi oan, lộ thông tin và ghi sai bên chịu tiền. Người duyệt cần hàng chờ trong SLA. Kế toán cần số tiền khớp sổ cái. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép tỷ lệ chuyển người xuống có thể khiến khách đủ điều kiện bị từ chối hoặc hãng chịu lỗi oan. Chuyển người quá nhiều lại dồn việc cho CSKH. Đọc cả ca hợp lệ, thời gian chờ và phân khúc bên cạnh tỷ lệ chung. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Ngày 1 cần giữ các trần an toàn, đủ người duyệt và kênh đối soát hoạt động. Mục tiêu giảm thao tác thủ công được kiểm lại bằng dữ liệu pilot. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Giữ 0 cho ba chỉ số an toàn. Đề xuất đánh giá lại ngân sách mỗi ticket, ROI và tải người duyệt theo dữ liệu từng kho/ca. Cập nhật bộ kiểm khi phiên bản chính sách đổi để kiểm đúng quyền lợi hiện hành. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 8.000đ · `roi_min` 0,25 · `queue_stuck_max` 0. Nếu chi phí vượt 8.000đ, ROI dưới 0,25 hoặc có ca ùn, chúng tôi sẽ Thu hẹp nếu xác định được phạm vi gây vấn đề và an toàn đạt, hoặc Cải tiến thêm trước khi mở.
- Căn cứ ngưỡng: PRD Lab 9 ghi sàn `pass_rate` 85% và `pass_hat_5` 80%. 98% và 95% là ngưỡng pilot Lab 10 đề xuất theo issue #3. Mức 8.000đ thấp hơn 2.000đ so với làm tay. ROI 0,25 nghĩa là 1đ chi vận hành tạo ít nhất 0,25đ tiết kiệm ròng theo công thức report. Số ca ùn bằng 0 nghĩa là không có ca chờ quá 60 phút hoặc hết ca vẫn chưa tới lượt.
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
