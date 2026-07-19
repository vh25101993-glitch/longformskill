---
name: longform
aliases:
  - longform-report
  - financial-desk-research
  - desk-research-finance
  - paper-research
  - longform-desk-research
  - research-atlas
  - financial-economic-atlas
description: >-
  Nghiên cứu bàn đa nguồn evidence-first và xuất bản báo cáo kinh tế - tài chính
  dạng paper, HTML dài hoặc Research Atlas có thể tái sử dụng. Dùng cho so sánh
  quốc tế, chính sách trước-sau, lịch sử tài sản, tổng hợp nhiều tài liệu, cổng
  tri thức nhiều module, hoặc báo cáo HTML/PDF/DOCX có nguồn, biểu đồ và QA.
---

# Longform Financial-Economic Desk Research

Phiên bản này hợp nhất ba lớp:

- **Research engine:** query matrix, source hierarchy, evidence ledger, data dictionary, comparability, uncertainty register và claim-level audit.
- **Publishing engine:** dark Longform HTML, KPI cards, Chart.js/ECharts, minimap, timeline, glossary, Scenario & Sensitivity Lab, print mode và QA Playwright.
- **Knowledge architecture:** module, chapter, question, claim, source, misconception, pathway, thesis, glossary, case và interaction rules có ID ổn định để tái sử dụng xuyên báo cáo.

Mục tiêu: đầu ra vừa **paper-ready**, **audit-ready**, vừa có thể nâng cấp thành **knowledge base / Research Atlas** khi quy mô nội dung đủ lớn.

## Khi nào kích hoạt

Dùng workflow đầy đủ cho:

- desk/deep research, paper nghiên cứu, data analysis report;
- báo cáo kinh tế - tài chính dài nhiều chương;
- so sánh quốc gia, giai đoạn, chỉ tiêu hoặc chế độ kinh tế;
- chính sách trước/sau mốc, timeline và cơ chế truyền dẫn;
- lịch sử tài sản, CAGR/YoY, premium/spread, regime;
- tổng hợp nhiều báo cáo, đồng thuận/bất đồng, forecast comparison;
- HTML/PDF/DOCX chuyên sâu cần nguồn và QA;
- atlas, handbook, knowledge base hoặc cổng nghiên cứu nhiều module.

Câu hỏi ngắn dùng mode `compact`, nhưng vẫn giữ quy tắc không bịa dữ liệu.

## Output modes

- `research-package`: brief + source register + evidence ledger + data dictionary + claim audit.
- `paper`: Markdown/DOCX/PDF.
- `html`: Longform dark article/dashboard.
- `paper+html`: hai đầu ra dùng cùng dataset đã audit.
- `atlas`: Research Atlas có dữ liệu chuẩn hóa và nhiều cửa vào tra cứu.
- `paper+html+atlas`: paper, HTML và atlas dùng chung source of truth.
- `compact`: phân tích ngắn có nguồn và caveat.

## Profile

- `asset-history`
- `policy-before-after`
- `cross-country-development`
- `industry-market`
- `document-consensus`
- `knowledge-atlas`
- `custom`

# 12 nguyên tắc bất biến

1. Không bịa dữ liệu; thiếu thì ghi rõ thiếu.
2. Nội suy, ước lượng, mô phỏng và dự báo phải gắn nhãn.
3. Không trộn định nghĩa, đơn vị, kỳ hoặc tần suất.
4. Không suy nhân quả từ tương quan.
5. Không gán tỷ trọng đóng góp nếu không có mô hình.
6. Claim trọng yếu phải có provenance cụ thể.
7. Dữ liệu hiện tại phải được kiểm tra lại, không dùng trí nhớ.
8. Chart và text dùng cùng dataset đã audit.
9. Kết luận và recommendation không mạnh hơn bằng chứng.
10. Bản cuối không chứa placeholder, prompt hoặc hướng dẫn nội bộ.
11. HTML là view; JSON/CSV đã audit là source of truth khi xuất Atlas.
12. ID của module, chapter, claim, source và question phải ổn định qua các phiên bản.

## Năm lớp phát biểu

| Lớp | Nhãn | Quy tắc |
|---|---|---|
| Dữ kiện nguồn | `FACT` | Có nguồn, kỳ, đơn vị |
| Số tính toán | `DERIVED` | Có công thức và đầu vào |
| Diễn giải | `INFERENCE` | Có luận cứ và mức chắc chắn |
| Kịch bản | `SCENARIO` | Có giả định, trigger, horizon |
| Khuyến nghị | `RECOMMENDATION` | Có target, evidence, risk, KPI |

## Phân loại dữ liệu định lượng

Mọi giá trị phải phân loại là một trong:

- `observed`
- `derived`
- `interpolated`
- `estimated`
- `forecast`
- `simulation`
- `scenario`
- `heuristic-score`

Mỗi giá trị cần có `value`, `unit`, `period`, `frequency`, `geography`, `dataType`, `sourceId/sourceIds`, `transformation` và ngày truy cập khi áp dụng.

Không trình bày heuristic score như xác suất. Ví dụ đúng: `score 80/100 theo bộ quy tắc`; ví dụ sai: `xác suất 80%`, trừ khi có mô hình xác suất và bằng chứng hiệu chỉnh.

## Hai trục chất lượng

- **Số liệu thật:** mọi số, ngày, tỷ lệ và chỉ số được fact-check.
- **Học thuật thật:** mọi lý thuyết và cơ chế có nguồn gốc đúng, điều kiện áp dụng và phản chứng.

# Workflow 6 bước

## Bước 1 — Research specification, outline, theme và architecture decision

Tạo `research_brief.md`, chốt:

- câu hỏi trung tâm + 3-8 câu hỏi phụ;
- phạm vi địa lý, thời gian và đối tượng;
- unit of analysis, tần suất, biến và công thức;
- breakpoint và cơ sở chọn;
- audience, output mode, completion criteria;
- family theme/hero mood nếu xuất HTML;
- profile và quyết định có kích hoạt `research-atlas` hay không.

### Atlas activation test

Kích hoạt Atlas khi có ít nhất một điều kiện:

- từ 8 chương hoặc nhiều module;
- từ 20 claim trọng yếu, 20 nguồn hoặc 10 thuật ngữ;
- cần nhiều cửa vào: câu hỏi, thuật ngữ, hiểu nhầm, case hoặc pathway;
- người dùng yêu cầu cổng tri thức, handbook, atlas hoặc hệ thống tái sử dụng;
- dữ liệu/claim/chart dự kiến được dùng lại trong báo cáo sau.

Không kích hoạt Atlas chỉ để tăng độ phức tạp giao diện.

Nếu bật Atlas, xác định trước:

- danh sách module;
- hệ ID;
- entity graph;
- schemaVersion;
- planned/published/reviewed chapter counts;
- các cửa vào cần có: Question Router, Claim Explorer, Glossary, Source Registry, Misconception Library, Pathway, Thesis Map, Case Explorer hoặc Lab.

Xem:

- `references/desk_research_01_protocol.md`
- `references/research_atlas.md`

## Bước 2 — Source plan, evidence acquisition và entity registration

Mỗi câu hỏi phụ có query matrix: mục tiêu, từ khóa, nguồn ưu tiên, dữ liệu cần trích, stopping rule và gap.

Thứ tự nguồn:

1. văn bản, cơ quan thống kê, ngân hàng trung ương, bộ ngành;
2. World Bank, IMF, OECD, BIS, UN, Eurostat;
3. cơ quan quản lý, sở giao dịch, báo cáo doanh nghiệp;
4. paper, working paper, journal gốc;
5. tổ chức nghiên cứu có phương pháp rõ;
6. Reuters, FT, Bloomberg và báo chí uy tín;
7. nguồn tổng hợp chỉ để định hướng.

Ghi claim vào `evidence_ledger.csv` ngay khi thu thập. Claim trọng yếu nên cross-check hai nguồn độc lập khi khả thi.

### Claim registry

Đơn vị kiểm chứng là claim, không phải đoạn văn. Mỗi claim có:

- stable ID;
- text;
- `FACT/DERIVED/INFERENCE/SCENARIO/RECOMMENDATION`;
- claim type;
- status;
- confidence;
- conditions;
- source IDs;
- counter-evidence;
- limitation;
- chapter/module liên quan.

Status mặc định:

- `verified`
- `qualified`
- `disputed`
- `interpretation`
- `behavioral-hypothesis`
- `insufficient-evidence`

### Source registry

Mỗi nguồn có source ID, tác giả, năm, publisher, source tier, URL, ngày truy cập, geography, period, claim IDs và module IDs.

Nếu cùng một nguồn xuất hiện ở nhiều module, dùng cùng một source ID; không nhân bản bản ghi.

Xem:

- `references/desk_research_01_protocol.md`
- `references/desk_research_02_data.md`
- `references/research_atlas.md`

## Bước 3 — Data normalization, Data Quality và referential integrity

Bắt buộc có:

- `source_register.csv`
- `data_dictionary.csv`
- `uncertainty_register.csv`

Kiểm tra:

- actual/derived/interpolated/estimated/forecast/simulation/scenario;
- current/constant price;
- FX/PPP;
- missing/duplicate/outlier/revision;
- break in series;
- comparability giữa quốc gia/giai đoạn;
- data vintage;
- entity, metric, period và frequency.

Báo cáo phải công bố độ phủ, tỷ lệ missing/nội suy, độ trễ, khác biệt định nghĩa và claim không đủ điều kiện kết luận.

Không nội suy chỉ để làm chart đẹp.

### Atlas integrity

Nếu bật Atlas, kiểm tra:

- ID duy nhất toàn hệ thống;
- mọi foreign key tồn tại;
- không có source, claim, chapter hoặc question mồ côi, trừ entity `draft`;
- planned, published và reviewed không bị gộp;
- KPI được tính tự động từ dữ liệu;
- mọi thesis liên kết tới claim đã audit;
- mọi pathway có mechanism, behavior/exposure và outcome/damage;
- mọi question có reading path hợp lệ;
- mọi interaction rule có modelVersion.

Xem:

- `references/desk_research_02_data.md`
- `references/research_atlas.md`

## Bước 4 — Analysis, paper composition, HTML và Atlas views

Logic bắt buộc:

> Câu hỏi → bối cảnh → dữ liệu → so sánh → cơ chế → phản chứng → hàm ý → hành động → giới hạn.

Với Atlas, mọi đơn vị quan trọng phải truy vết được theo:

> QUESTION → CLAIM → EVIDENCE → MECHANISM → COUNTER-EVIDENCE → APPLICATION → EXPOSURE → LIMITATION.

### Cấu trúc paper/HTML mặc định

1. Cover/meta
2. Executive Summary
3. Scope & Definitions
4. Methodology & Data Quality
5. Historical/Institutional Context
6. Core Performance
7. Comparisons
8. Attribution & Diagnosis
9. Alternative Explanations
10. Findings
11. Recommendations & Action Plan
12. Uncertainty & Limitations
13. Sources
14. Appendix/Data Dictionary

### Quy tắc chương

- Executive Summary có 3-7 phát hiện định lượng và 2-5 caveat.
- Mỗi chương có câu hỏi dẫn, evidence, interpretation, counterpoint, mini-conclusion và risk of interpretation.
- Timeline dùng ngày/mốc chính xác.
- Glossary bắt buộc khi có thuật ngữ dễ nhầm.
- So sánh quốc tế phải có comparability matrix.
- Asset history tách price return, FX effect, premium/spread, transaction cost và real return khi có dữ liệu.
- Policy analysis dùng chain: policy → channel → intermediate indicator → outcome → side effect.
- Tone: **người kể chuyện số liệu, không áp đặt kết luận**.

### Atlas views

Khi bật Atlas, chọn các view phù hợp:

- **Module/Project Map:** cấu trúc chủ đề và quan hệ module.
- **Question Router:** bắt đầu từ câu hỏi đời sống hoặc quyết định thực tế.
- **Claim Explorer:** claim, status, confidence, evidence, counter-evidence và limitation.
- **Misconception Library:** hiểu nhầm → correction → explanation → pathway.
- **Causal/Exposure Pathway:** macro/trigger → misinterpretation/mechanism → behavior/exposure → balance sheet → damage/outcome.
- **Thesis Map:** kết luận tổng hợp xuyên module.
- **Case Explorer:** case, period, mechanism, evidence và giới hạn so sánh.
- **Glossary:** thuật ngữ, bản dịch, định nghĩa, chương và nguồn.
- **Source Registry:** lọc theo tier, module, claim, period và tổ chức.
- **Global Search:** title, question, claim, term và source.

UX bắt buộc:

- non-linear navigation nhưng có breadcrumb và nút trở về atlas;
- progressive disclosure cho nội dung chi tiết;
- cross-link theo ID, không copy-paste nội dung cùng một claim;
- mỗi chapter hiển thị related questions, claims, terms, cases và sources;
- mobile không scroll ngang; bảng rộng có card fallback;
- minimap, presentation mode và section IDs đồng bộ.

Xem:

- `references/desk_research_03_analysis.md`
- `references/research_atlas.md`

## Bước 5 — Audit bốn lớp

### 5A. Fact/data

Trích mọi claim có số; đối chiếu text-table-chart; kiểm tra source, unit, period, frequency, nominal/real, mean/median và mốc luật/chính sách.

### 5B. Academic/mechanism

Mỗi lý thuyết có nguồn gốc; không bịa framework; causal mechanism phải có supporting evidence, conditions và alternative explanations.

### 5C. Citation/provenance

Claim trọng yếu có claim ID; chart/table có source note; derived metric có formula/input; citation phải hỗ trợ đúng entity, metric và period.

### 5D. Editorial/knowledge architecture

- Narrative liền mạch; chương cân đối theo bằng chứng; không lặp.
- Kết luận không mạnh hơn evidence.
- Entity không bị nhân bản không cần thiết.
- Cross-link đúng ID.
- Question Router, pathway và thesis phản ánh đúng claim registry.
- Heuristic score không bị mô tả như xác suất.

Chỉ publish khi quality score ≥85/100 và không có hard fail.

Xem:

- `references/desk_research_04_audit_templates.md`
- `references/research_atlas.md`

## Bước 6 — Output engineering và technical QA

### HTML Longform

- copy `assets/article_template.html`;
- mỗi chương là một `<section>`;
- component density 2-4/chương;
- KPI, table, chart, callout, timeline, glossary, scenario/sensitivity lab;
- numbered citations cho bài nhiều số;
- minimap/progress/presentation đồng bộ section;
- responsive mobile-first, print mode, lazy loading;
- chart có source, unit, period, transformation, limitation và fallback table.

Theme mặc định: dark slate-900; Amber cho bài tư duy/nhân quả, Blue cho policy/data.

### Scenario & Sensitivity Lab

Kích hoạt khi báo cáo có ít nhất một kết quả phụ thuộc rõ vào giả định có thể thay đổi, ví dụ: tăng trưởng doanh thu, biên lợi nhuận, NIM, cost of credit, lãi suất, tỷ giá, multiple, cap rate, lạm phát hoặc chi phí vốn.

Mỗi lab tối thiểu có:

1. **Baseline:** giá trị gốc, nguồn, kỳ và trạng thái `FACT/DERIVED`.
2. **Controls:** 1-5 biến; label, đơn vị, min, max, step, default và cơ sở chọn miền.
3. **Model:** hàm tính thuần, công thức công khai, không dùng số ngẫu nhiên và không gọi mạng.
4. **Outputs:** KPI cập nhật trực tiếp, có đơn vị và quy tắc làm tròn.
5. **Dynamic chart:** one-way sensitivity, tornado, breakeven, two-way heatmap hoặc waterfall.
6. **Actions:** Reset; preset Bear/Base/Bull khi phù hợp; xuất JSON/CSV là tùy chọn.
7. **Disclosure:** nhãn `SCENARIO`, công thức, giả định giữ nguyên, limitation và fallback table.

Quy tắc kỹ thuật:

- range input đi cùng ô số hoặc `<output>`;
- hỗ trợ bàn phím và mobile;
- cập nhật chart bằng `chart.data` + `chart.update('none')`;
- dùng `requestAnimationFrame` hoặc debounce khi nhiều control;
- không trộn scenario vào actual nếu không phân biệt rõ;
- mọi output từ control là `SCENARIO` hoặc `DERIVED-SCENARIO`.

Xem `references/interactive_sensitivity.md`.

### Rules-based Diagnostic Lab

Với Atlas có thể dùng rule table để xếp hạng regime, mechanism, bias hoặc policy diagnosis khi:

- input và quy tắc có thể công khai;
- mỗi rule liên kết tới claim/source;
- output có modelVersion;
- score được mô tả là heuristic, không phải xác suất;
- có limitation và điều kiện bác bỏ;
- không lưu dữ liệu cá nhân nếu không cần thiết.

Mỗi rules lab nên có:

- input definitions;
- rule table;
- score aggregation;
- output interpretation;
- supporting claim IDs;
- counter-signals;
- modelVersion;
- disclosure.

### QA HTML bắt buộc

```bash
# Không còn placeholder
grep -oE "{{[A-Z_0-9]+}}" {project}/{slug}/index.html | sort -u

# Canvas count = new Chart count
grep -c "<canvas" {project}/{slug}/index.html
grep -c "new Chart" {project}/{slug}/index.html

# Playwright QA
node "$SKILL_DIR/scripts/qa_article.js" \
  --url=file://{project}/{slug}/index.html \
  --output=/tmp/qa-shots
```

Sửa mọi raw token, JS error, chart trống, nav sai, clipping/overflow trước khi hoàn thành.

Với interactive lab, kiểm tra thêm:

- từng control làm KPI/chart thay đổi đúng chiều theo công thức;
- Reset khôi phục baseline;
- preset không vượt min/max;
- output không sinh `NaN`, `Infinity` hoặc đơn vị sai;
- chart resize đúng tại 390 px, 768 px và desktop;
- fallback table hiển thị khi chart library không tải.

### QA Atlas bắt buộc

```bash
python "$SKILL_DIR/scripts/qa_research_atlas.py" \
  ./research-project/atlas
```

Kiểm tra thêm:

- duplicate ID và broken reference;
- verified claim thiếu nguồn;
- thesis phụ thuộc claim chưa audit;
- pathway thiếu mechanism/exposure/outcome;
- manifest counts mâu thuẫn dữ liệu;
- module count gộp planned/published/reviewed;
- heuristic score bị gọi là probability;
- quantitative value thiếu dataType hoặc source.

## Research package tối thiểu

```text
project/
├── research_brief.md
├── research_plan.csv
├── source_register.csv
├── evidence_ledger.csv
├── data_dictionary.csv
├── chart_manifest.csv
├── claim_audit.csv
├── uncertainty_register.csv
├── paper.md hoặc index.html
└── qa_report.md
```

Khởi tạo và QA:

```bash
python "$SKILL_DIR/scripts/init_research_project.py" \
  --topic "[TOPIC]" --profile custom --out ./research-project

python "$SKILL_DIR/scripts/qa_research_project.py" ./research-project
```

## Research Atlas package

```text
project/
├── research_brief.md
├── research_plan.csv
├── source_register.csv
├── evidence_ledger.csv
├── data_dictionary.csv
├── chart_manifest.csv
├── claim_audit.csv
├── uncertainty_register.csv
├── atlas/
│   ├── atlas_manifest.json
│   ├── modules.json
│   ├── chapters.json
│   ├── claims.json
│   ├── sources.json
│   ├── questions.json
│   ├── misconceptions.json
│   ├── pathways.json
│   ├── theses.json
│   ├── glossary.json
│   ├── cases.json
│   └── interaction_rules.json
├── index.html
└── qa_report.md
```

`atlas_manifest.json` khai báo `schemaVersion`, `generatedAt`, counts và đường dẫn file. Mọi KPI atlas phải được tính từ các entity files, không nhập lặp thủ công.

# Profile architecture

- **Asset history:** Summary → Scope/Data → Data Quality → Regimes → Return/Volatility → Benchmark → Premium/Spread → Attribution → Scenarios → Limitations.
- **Policy before/after:** Summary → Glossary → Data Quality → Timeline → Before/After → Outcomes → Evidence Chain → Counterfactual → Lessons → Action Matrix.
- **Cross-country:** Summary → Phase criteria → Comparability → Data Quality → Macro Context → Household Finance → Comparison → Drivers/Exceptions → Target-country roadmap.
- **Document consensus:** Document map → Consensus matrix → Disagreement matrix → Forecast comparison → Assumption audit → Data vintage → Implications/Risks.
- **Knowledge atlas:** Module Map → Question Router → Core Chapters → Claim Explorer → Misconceptions → Pathways → Cases → Thesis Map → Glossary → Source Registry → Labs → Methodology/Limitations.

# Recommendation matrix bắt buộc

Mỗi recommendation có:

- hành động;
- target;
- priority;
- evidence claim IDs;
- mechanism;
- impact basis;
- risks/trade-offs;
- owner;
- horizon;
- KPI/validation;
- trigger to revise.

Không đưa lời khuyên đầu tư cá nhân hóa khi dữ liệu hoặc suitability không đủ.

# Chart manifest bắt buộc

Mỗi chart ghi:

- chart ID;
- title;
- analytical question;
- type;
- metrics;
- unit;
- geography;
- period/frequency;
- source IDs;
- transformations;
- data status;
- interpretation;
- limitations;
- fallback table.

Với chart tương tác bổ sung:

- `interactive=true`;
- input parameters;
- baseline;
- min/max/step;
- formula/model version;
- output metrics;
- preset definitions;
- assumptions held constant;
- expected direction.

Chart manifest phải đủ để tái tạo cùng kết quả từ cùng input.

# Hard fail

Không publish nếu:

- số liệu trọng yếu không có provenance;
- nội suy/ước lượng không gắn nhãn;
- text và chart mâu thuẫn;
- trộn đơn vị/định nghĩa;
- causal attribution không có phương pháp;
- mốc chính sách chưa xác minh;
- citation không hỗ trợ claim;
- dùng dữ liệu cũ như hiện tại;
- placeholder, JS error, chart trống hoặc overlap;
- control không hoạt động, sinh `NaN/Infinity`, hoặc kết quả không khớp công thức;
- scenario chart không công bố baseline, miền giả định, đơn vị hoặc limitation;
- trộn `FACT` và `SCENARIO` khiến người đọc hiểu nhầm;
- recommendation mạnh hơn bằng chứng;
- lộ prompt hoặc hướng dẫn nội bộ.

Hard fail riêng cho Atlas:

- duplicate ID hoặc broken reference;
- claim `verified` không có nguồn;
- KPI thủ công mâu thuẫn entity data;
- heuristic score bị trình bày như xác suất;
- không phân biệt planned/published/reviewed;
- không phân biệt observed/derived/simulation/scenario;
- cùng một claim bị copy thành nhiều entity thay vì liên kết;
- Question Router dẫn tới reading path không tồn tại;
- pathway thiếu mechanism, behavior/exposure hoặc damage/outcome;
- Atlas không có manifest hoặc schemaVersion.

# Lệnh gọi mẫu

```text
/longform "Sự phát triển tài chính cá nhân tại Mỹ, Nhật, Hàn Quốc, Trung Quốc và Việt Nam" --profile cross-country-development --output paper+html
```

```text
/longform "Chính sách BĐS Trung Quốc trước và sau 2016" --profile policy-before-after --output html
```

```text
/longform "Giá vàng SJC 2009-2025 và premium so với vàng thế giới" --profile asset-history --output paper+html
```

```text
/longform "Economic Life Atlas: vĩ mô, chính sách, thị trường, hành vi và tài chính cá nhân" --profile knowledge-atlas --output paper+html+atlas
```

# Tài nguyên

Publishing engine:

- `assets/article_template.html`
- `references/components.md`
- `references/chart_recipes.md`
- `references/interactive_sensitivity.md`
- `references/themes.md`
- `references/navigation.md`
- `references/citations.md`
- `references/fact_check.md`
- `references/academic_foundations.md`
- `scripts/qa_article.js`

Desk Research extension:

- `references/desk_research_01_protocol.md`
- `references/desk_research_02_data.md`
- `references/desk_research_03_analysis.md`
- `references/desk_research_04_audit_templates.md`
- `scripts/init_research_project.py`
- `scripts/qa_research_project.py`

Research Atlas extension:

- `references/research_atlas.md`
- `scripts/qa_research_atlas.py`
