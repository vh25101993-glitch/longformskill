---
name: financial-html
aliases:
  - financial-economics-html
  - financial-dashboard-html
  - financial-report-html
  - financial-html-narrative
description: Tạo HTML tài chính tương tác từ phân tích đã có, kết hợp dashboard định lượng với narrative layer, claim graph, counterpoint, financial centerpiece, progressive disclosure và Reader/Research mode.
---

# Financial HTML — Narrative Research Dashboard

## Mục tiêu

Chuyển phân tích tài chính, BCTC, vĩ mô hoặc ngành thành HTML có ba lớp:

1. **Evidence:** nguồn, kỳ, đơn vị, công thức, uncertainty.
2. **Analytical:** KPI, bảng, chart, valuation và sensitivity.
3. **Narrative:** chapter question, thesis, claim graph, counterpoint, centerpiece và takeaway.

Không viết lại hoặc phát minh số liệu. Nếu đầu vào thiếu evidence mapping, giữ nhãn `INSUFFICIENT_EVIDENCE` và công bố giới hạn.

## Khi nào kích hoạt

Dùng khi người dùng yêu cầu:

- tạo HTML từ phân tích BCTC;
- tạo dashboard tài chính/vĩ mô/ngành;
- trình bày nghiên cứu tài chính thành HTML tương tác;
- nâng cấp HTML hiện có bằng narrative, claim graph hoặc Reader/Research mode;
- tạo financial report có thể in/PDF và kiểm toán dữ liệu.

## Input tối thiểu

- nội dung phân tích đã hoàn tất hoặc dataset;
- entity/company/topic;
- period;
- source notes hoặc evidence ledger nếu có;
- chart/table cần giữ lại.

Nếu có research package Longform, tái sử dụng trực tiếp:

```text
evidence_ledger.csv
chart_manifest.csv
uncertainty_register.csv
chapter_schema.csv
claim_graph.csv
counterpoints.csv
narrative_manifest.csv
```

## Workflow 6 bước

### Bước 1 — Content inventory

- xác định report type: `quarterly-financials`, `company-deep-dive`, `bank`, `securities`, `industry`, `macro`, `valuation-tool`, `dashboard`;
- liệt kê KPI, bảng, chart, conclusion và caveat;
- chốt Reader mode là mặc định, Research mode là lớp audit;
- xác định 1–3 câu hỏi trung tâm.

### Bước 2 — Evidence mapping

- gắn claim ID cho conclusion trọng yếu;
- giữ taxonomy `FACT`, `DERIVED`, `INFERENCE`, `SCENARIO`, `RECOMMENDATION`;
- ghi `VERIFIED`, `QUALIFIED`, `DISPUTED`, `AUTHOR_VIEW`, `INSUFFICIENT_EVIDENCE`;
- `DERIVED` phải có formula và input claim IDs;
- chart và text dùng cùng claim IDs/dataset.

### Bước 3 — Financial chapter composition

Mỗi chapter có:

1. `chapter_id` và `chapter_type`;
2. guiding question;
3. provisional thesis;
4. evidence claims;
5. analytical chart/table;
6. strongest counterpoint;
7. resolving metrics;
8. mini-conclusion;
9. monitoring metrics;
10. takeaway và supporting claim IDs.

Dùng chapter type trong `references/financial_html_narrative.md`.

### Bước 4 — Narrative publication design

#### Claim graph

Quan hệ cho phép:

`SUPPORTS`, `CONTRADICTS`, `QUALIFIES`, `EXPLAINS`, `DERIVED_FROM`, `SYNTHESIZES`, `DEPENDS_ON`, `INVALIDATES_IF`.

Mỗi conclusion trọng yếu phải có evidence edge. `INVALIDATES_IF` phải có trigger quan sát được.

#### Counterpoint

Không tạo mục “rủi ro” chung chung. Mỗi counterpoint phải có:

- hai position;
- claim IDs hai phía;
- strongest evidence;
- resolving metrics;
- synthesis và unresolved condition.

#### Financial centerpiece

Chỉ dùng 1–3 centerpiece có giá trị giải thích:

- earnings bridge;
- cash-conversion cascade;
- balance-sheet pressure map;
- credit-quality cascade;
- funding-to-NIM mechanism;
- capital constraint path;
- market-liquidity chain;
- policy timeline hoặc scenario path khi phù hợp.

Không dùng sticky-scroll thay chart tiêu chuẩn.

#### Progressive disclosure

- Level 1: KPI, chart, insight, counterpoint rút gọn, takeaway, caveat trọng yếu.
- Level 2: nguồn, kỳ, đơn vị, formula, fallback table, limitation.
- Level 3: claim IDs, graph, uncertainty, contradictory evidence, audit status.

Reader mode không được che caveat có thể thay đổi conclusion.

### Bước 5 — HTML engineering

- dark financial layout, mobile-first;
- fixed/pill navigation và scroll progress nếu báo cáo dài;
- Reader/Research toggle dùng cùng DOM/data;
- disclosure bằng `details/summary` hoặc button có ARIA;
- charts bằng Chart.js/ECharts, có fallback table;
- centerpiece dùng `assets/financial_narrative_components.html`;
- print mở disclosure, hủy sticky, giữ source/limitation;
- không horizontal scroll.

### Bước 6 — QA

Chạy các kiểm tra hiện có của Longform và bổ sung:

```bash
python "$SKILL_DIR/scripts/qa_financial_publication.py" publication.json
node "$SKILL_DIR/scripts/qa_article.js" --url=file://report/index.html --output=/tmp/qa-shots
```

Kiểm tra:

- schema và reference integrity;
- conclusion/takeaway có evidence edge;
- counterpoint có hai phía và resolving metrics;
- centerpiece có claim/source/formula và fallback;
- Reader/Research toggle;
- keyboard/reduced-motion;
- 390 px, 768 px, desktop và print;
- không `NaN`, `Infinity`, overlap, clipping hoặc horizontal overflow.

## Quy tắc theo report type

### BCTC quý

- chapter schema bắt buộc;
- tối thiểu 2 counterpoint;
- 1–2 centerpiece;
- earnings quality và cash flow không được bỏ qua nếu dữ liệu có sẵn.

### Ngân hàng

- bắt buộc tách growth, NIM/funding, asset quality, credit cost và capital;
- NPL phải đọc cùng stage-2, coverage và write-off khi có;
- valuation P/B phải liên kết ROE bền vững và cost of equity.

### Công ty chứng khoán

- tách brokerage, margin, proprietary trading và IB;
- kết quả tự doanh không được trình bày như recurring nếu không đủ evidence;
- theo dõi market liquidity và capital usage.

### Doanh nghiệp phi tài chính

- tách reported và normalized earnings;
- kiểm tra CFO/LNST, working capital, capex và FCF;
- leverage/liquidity phải có trigger.

## Hard fail

Không publish nếu:

- số trọng yếu không có provenance;
- chart và text dùng số khác nhau;
- actual/derived/scenario bị trộn;
- takeaway không có supporting claim;
- counterpoint không có claim mapping;
- valuation không có formula/input;
- centerpiece trình bày số không có source/formula;
- illustrative mechanism bị hiểu như dữ liệu thực;
- Reader mode che caveat trọng yếu;
- Research mode gây horizontal overflow;
- JS/chart/toggle/disclosure không hoạt động.

## Tài nguyên

- `references/financial_html_narrative.md`
- `assets/financial_narrative_components.html`
- `schemas/financial_html_publication.schema.json`
- `scripts/qa_financial_publication.py`
- `references/narrative_publication.md`
- `assets/narrative_components.html`
