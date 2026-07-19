# Financial HTML Narrative Layer

Tài liệu này mở rộng Financial HTML từ dashboard định lượng thành **financial research publication** có narrative layer, claim graph, counterpoint, narrative centerpiece và progressive disclosure. Mọi thành phần vẫn dùng cùng evidence ledger, chart manifest, uncertainty register và dataset đã audit.

## 1. Nguyên tắc kiến trúc

Financial HTML có ba lớp, không thay thế lẫn nhau:

1. **Evidence layer:** nguồn, số liệu, công thức, kỳ, đơn vị, uncertainty.
2. **Analytical layer:** KPI, bảng, chart, valuation, scorecard, sensitivity.
3. **Narrative layer:** guiding question, thesis, claim graph, counterpoint, centerpiece, takeaway.

Không tạo số liệu mới cho narrative. Text, chart và centerpiece phải resolve từ cùng claim IDs.

## 2. Chapter schema theo báo cáo tài chính

Mỗi chương phải trả lời một câu hỏi tài chính rõ ràng:

```text
chapter_id
chapter_type
title
guiding_question
provisional_thesis
claim_ids
centerpiece_visual_id
counterpoint_id
mini_conclusion
risk_of_interpretation
monitoring_metrics
takeaway
```

### Chapter type chuẩn

- `overview`
- `earnings-quality`
- `revenue-growth`
- `margin-cost`
- `cash-flow`
- `balance-sheet`
- `liquidity-leverage`
- `asset-quality`
- `funding-nim`
- `capital-adequacy`
- `segment-analysis`
- `valuation`
- `scenario-risk`
- `investment-conclusion`

### Cấu trúc chương

```text
Guiding question
→ provisional thesis
→ KPI evidence
→ analytical chart/table
→ narrative centerpiece nếu cần
→ strongest counterpoint
→ indicator that resolves the debate
→ mini-conclusion
→ monitoring metrics
→ takeaway
```

## 3. Claim graph tài chính

### Relation type chung

- `SUPPORTS`
- `CONTRADICTS`
- `QUALIFIES`
- `EXPLAINS`
- `DERIVED_FROM`
- `SYNTHESIZES`
- `DEPENDS_ON`
- `INVALIDATES_IF`

### Ví dụ doanh nghiệp phi tài chính

```text
Revenue growth SUPPORTS earnings growth
Gross-margin compression QUALIFIES revenue growth
Receivables growth CONTRADICTS cash-conversion improvement
CFO DERIVED_FROM reported cash-flow statement
Valuation conclusion DEPENDS_ON normalized EPS and target multiple
Investment thesis INVALIDATES_IF leverage trigger is breached
```

### Ví dụ ngân hàng

```text
Credit growth SUPPORTS NII growth
CASA recovery EXPLAINS lower cost of funds
Stage-2 loans QUALIFY stable NPL ratio
Credit cost CONTRADICTS apparent operating leverage
ROE SYNTHESIZES NIM, fee income, opex, credit cost and capital
P/B thesis DEPENDS_ON sustainable ROE and cost of equity
```

### Quy tắc

- Mỗi conclusion trọng yếu phải có ít nhất một incoming edge.
- `DERIVED_FROM` phải trỏ đến input claim IDs và formula.
- `INVALIDATES_IF` phải có trigger định lượng hoặc điều kiện quan sát được.
- Không dùng graph để ngụ ý nhân quả khi evidence chỉ là tương quan.

## 4. Counterpoint object

Mỗi counterpoint gồm:

```text
counterpoint_id
chapter_id
question
main_position
main_claim_ids
opposing_position
opposing_claim_ids
strongest_evidence_a
strongest_evidence_b
resolving_metrics
synthesis
unresolved_condition
status
```

### Ví dụ

**Question:** NIM ổn định có phản ánh sức mạnh hoạt động?

- Main position: CASA phục hồi và chi phí vốn giảm hỗ trợ NIM.
- Opposing position: NIM có thể được giữ bằng lợi suất cho vay cao hơn và khẩu vị rủi ro lớn hơn.
- Resolving metrics: cost of funds, yield on earning assets, stage-2 ratio, credit cost.

Counterpoint không được là một danh sách rủi ro chung chung. Phải chỉ rõ dữ liệu nào có thể phân định hai lập luận.

## 5. Narrative centerpiece

Mỗi báo cáo Financial HTML dùng tối đa 1–3 centerpiece. Không dùng sticky-scroll thay cho chart tiêu chuẩn.

### Doanh nghiệp phi tài chính

#### Earnings bridge

```text
Revenue
→ gross profit
→ selling expense
→ G&A
→ financial result
→ tax
→ net profit
```

#### Cash-conversion cascade

```text
Net profit
→ non-cash adjustments
→ working-capital movement
→ CFO
→ capex
→ free cash flow
```

#### Balance-sheet pressure map

```text
Inventory + receivables + capex
→ funding need
→ debt
→ interest expense
→ liquidity risk
```

### Ngân hàng

#### Credit-quality cascade

```text
Credit growth
→ stage-2 loans
→ NPL
→ provisioning
→ credit cost
→ net profit
```

#### Funding-to-NIM mechanism

```text
CASA / deposit mix
→ cost of funds
→ NIM
→ NII
→ PPOP
```

#### Capital constraint path

```text
RWA growth
→ CAR
→ lending capacity
→ ROE
→ justified P/B
```

### Công ty chứng khoán

```text
Market liquidity
→ brokerage revenue
→ margin balance
→ margin interest income
→ capital risk
→ ROE
```

### Manifest bắt buộc

Mỗi centerpiece phải ghi trong `narrative_manifest.csv`:

- `visual_id`
- `chapter_id`
- `visual_type`
- `layout`
- `data_mode`
- `claim_ids`
- `source_ids`
- `step_ids`
- `trigger`
- `mobile_fallback`
- `print_fallback`
- `accessibility_note`
- `limitations`

`data_mode` cho Financial HTML:

- `verified-data`
- `derived-data`
- `scenario-data`
- `illustrative-mechanism`

## 6. Progressive disclosure

Financial HTML dùng ba mức disclosure.

### Level 1 — Reader surface

- KPI trọng yếu
- chart chính
- insight ngắn
- counterpoint rút gọn
- takeaway
- caveat trọng yếu

### Level 2 — Expandable evidence

- nguồn
- kỳ và đơn vị
- cách tính
- chart fallback table
- limitation
- resolving metrics

### Level 3 — Research mode

- claim ID
- evidence class
- epistemic status
- formula và input claim IDs
- graph relations
- uncertainty mapping
- contradictory evidence
- audit status

Không giấu caveat trọng yếu trong disclosure đóng. Reader mode vẫn phải thấy rủi ro có thể thay đổi kết luận.

## 7. Reader / Research mode

Hai mode dùng cùng DOM và data.

```html
<html data-view="reader">
```

Reader mode ẩn chi tiết audit bằng CSS; Research mode mở chúng. Toggle phải:

- dùng `button` thật;
- có `aria-pressed`;
- lưu trạng thái trong `localStorage` nếu có;
- không làm chart resize sai;
- vẫn hiển thị đầy đủ khi print.

## 8. Financial HTML layout

Thứ tự mặc định:

1. Hero + company/period/meta
2. Executive verdict
3. KPI scorecard
4. Chapter navigation
5. Earnings / core operation
6. Cash flow and earnings quality
7. Balance sheet / asset quality
8. Liquidity, leverage or capital
9. Segment / business drivers
10. Valuation and scenarios
11. Counterpoints and thesis breakers
12. Monitoring dashboard
13. Methodology, sources and data dictionary

Mỗi chapter có `data-chapter-id` và liên kết tới chapter schema.

## 9. Kích hoạt theo loại báo cáo

### Báo cáo BCTC quý

- chapter schema: bắt buộc
- claim graph: bắt buộc cho conclusion chính
- counterpoint: tối thiểu 2
- centerpiece: 1–2
- progressive disclosure: bắt buộc

### Phân tích doanh nghiệp dài hạn

- counterpoint: bắt buộc mỗi thesis lớn
- centerpiece: 2–3
- thesis breakers và monitoring metrics: bắt buộc

### Dashboard ngắn/cập nhật định kỳ

- chapter schema tối giản
- graph chỉ cho KPI conclusion
- không bắt buộc sticky-scroll
- Reader/Research và disclosure vẫn bắt buộc

## 10. QA Financial Narrative

### Structural

- chapter ID duy nhất;
- mọi claim/counterpoint/visual reference tồn tại;
- conclusion có supporting edge;
- counterpoint có claim IDs hai phía;
- resolving metrics không rỗng;
- centerpiece có mobile và print fallback.

### Financial integrity

- metric cùng định nghĩa, kỳ, unit;
- normalized và reported earnings tách rõ;
- actual, derived, forecast và scenario không trộn;
- valuation conclusion có formula/input;
- thesis breaker có trigger quan sát được;
- chart và narrative cùng claim IDs.

### Interaction

- Reader/Research toggle không làm mất dữ liệu;
- disclosure dùng `details/summary` hoặc button có ARIA;
- sticky step hoạt động bằng scroll, click và keyboard;
- mobile không có horizontal scroll;
- print mở toàn bộ disclosure và hủy sticky;
- reduced motion được tôn trọng.

## 11. Hard fail bổ sung

Không publish Financial HTML nếu:

- takeaway không có evidence edge;
- counterpoint chỉ là nhận xét không có claim mapping;
- centerpiece hiển thị số không có source hoặc formula;
- dữ liệu minh họa bị trình bày như số liệu thực;
- Reader mode che caveat làm thay đổi conclusion;
- valuation/scenario không phân biệt actual và assumption;
- label chart, node hoặc callout bị cắt/chồng lấn;
- Research mode gây overflow ngang.
