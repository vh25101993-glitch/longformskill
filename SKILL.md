---
name: longform
aliases:
  - longform-report
  - financial-desk-research
  - desk-research-finance
  - paper-research
  - longform-desk-research
description: Nghiên cứu bàn đa nguồn evidence-first và xuất bản báo cáo kinh tế - tài chính dạng paper/HTML dài. Dùng cho so sánh quốc tế, chính sách trước-sau, lịch sử tài sản/premium-spread, tổng hợp nhiều tài liệu, hoặc báo cáo HTML/PDF/DOCX có nguồn, biểu đồ và QA.
---

# Longform Financial-Economic Desk Research

Phiên bản này hợp nhất:

- **Research engine:** query matrix, source hierarchy, evidence ledger, data dictionary, comparability, uncertainty register và claim-level audit.
- **Publishing engine:** dark Longform HTML, KPI cards, Chart.js/ECharts, minimap, timeline, glossary, **Scenario & Sensitivity Lab**, print mode và QA Playwright.

Mục tiêu: báo cáo vừa **paper-ready** về kết cấu, vừa **audit-ready** về bằng chứng.

## Khi nào kích hoạt

Dùng workflow đầy đủ cho:

- desk/deep research, paper nghiên cứu, data analysis report;
- báo cáo kinh tế - tài chính dài nhiều chương;
- so sánh quốc gia/giai đoạn/chỉ tiêu;
- chính sách trước/sau mốc, timeline và cơ chế truyền dẫn;
- lịch sử tài sản, CAGR/YoY, premium/spread, regime;
- tổng hợp nhiều báo cáo, đồng thuận/bất đồng, forecast comparison;
- HTML/PDF/DOCX chuyên sâu cần nguồn và QA.

Câu hỏi ngắn dùng mode `compact`, nhưng vẫn giữ quy tắc không bịa dữ liệu.

## Output modes

- `research-package`: brief + source register + evidence ledger + data dictionary + claim audit.
- `paper`: Markdown/DOCX/PDF.
- `html`: Longform dark article/dashboard.
- `paper+html`: hai đầu ra dùng cùng dataset đã audit.
- `compact`: phân tích ngắn có nguồn và caveat.

## 10 nguyên tắc bất biến

1. Không bịa dữ liệu; thiếu thì ghi rõ thiếu.
2. Nội suy/ước lượng/dự báo phải gắn nhãn.
3. Không trộn định nghĩa, đơn vị, kỳ hoặc tần suất.
4. Không suy nhân quả từ tương quan.
5. Không gán tỷ trọng đóng góp nếu không có mô hình.
6. Claim trọng yếu phải có provenance cụ thể.
7. Dữ liệu hiện tại phải được kiểm tra lại, không dùng trí nhớ.
8. Chart và text dùng cùng dataset đã audit.
9. Kết luận/khuyến nghị không mạnh hơn bằng chứng.
10. Bản cuối không chứa placeholder, prompt hoặc hướng dẫn nội bộ.

## Năm lớp phát biểu

| Lớp | Nhãn | Quy tắc |
|---|---|---|
| Dữ kiện nguồn | `FACT` | Có nguồn, kỳ, đơn vị |
| Số tính toán | `DERIVED` | Có công thức và đầu vào |
| Diễn giải | `INFERENCE` | Có luận cứ và mức chắc chắn |
| Kịch bản | `SCENARIO` | Có giả định, trigger, horizon |
| Khuyến nghị | `RECOMMENDATION` | Có target, evidence, risk, KPI |

## Hai trục chất lượng

- **Số liệu thật:** mọi số, ngày, tỷ lệ, chỉ số được fact-check.
- **Học thuật thật:** mọi lý thuyết/cơ chế có tác giả, tác phẩm hoặc nguồn gốc đúng.

# Workflow 6 bước

## Bước 1 — Research specification, outline và theme

Tạo `research_brief.md`, chốt:

- câu hỏi trung tâm + 3-8 câu hỏi phụ;
- phạm vi địa lý/thời gian/đối tượng;
- unit of analysis, tần suất, biến và công thức;
- breakpoint và cơ sở chọn;
- audience, output mode, completion criteria;
- family theme/hero mood nếu xuất HTML.

Chọn profile:

- `asset-history`
- `policy-before-after`
- `cross-country-development`
- `industry-market`
- `document-consensus`
- `custom`

Xem `references/desk_research_01_protocol.md`.

## Bước 2 — Source plan và evidence acquisition

Mỗi câu hỏi phụ có query matrix: mục tiêu, từ khóa, nguồn ưu tiên, dữ liệu cần trích, stopping rule và gap.

Thứ tự nguồn:

1. văn bản/cơ quan thống kê/ngân hàng trung ương/bộ ngành;
2. World Bank, IMF, OECD, BIS, UN, Eurostat;
3. cơ quan quản lý, sở giao dịch, báo cáo doanh nghiệp;
4. paper/working paper/journal gốc;
5. tổ chức nghiên cứu có phương pháp rõ;
6. Reuters/FT/Bloomberg và báo chí uy tín;
7. nguồn tổng hợp chỉ để định hướng.

Ghi claim vào `evidence_ledger.csv` ngay khi thu thập. Claim trọng yếu nên cross-check hai nguồn độc lập khi khả thi.

Xem `references/desk_research_01_protocol.md` và `desk_research_02_data.md`.

## Bước 3 — Data normalization và Data Quality

Bắt buộc có:

- `source_register.csv`
- `data_dictionary.csv`
- `uncertainty_register.csv`

Kiểm tra: actual/derived/interpolated/estimated/forecast; current/constant price; FX/PPP; missing/duplicate/outlier/revision; break in series; comparability giữa quốc gia/giai đoạn.

Báo cáo phải công bố độ phủ, tỷ lệ missing/nội suy, độ trễ, khác biệt định nghĩa và claim không đủ điều kiện kết luận.

Không nội suy chỉ để làm chart đẹp.

Xem `references/desk_research_02_data.md`.

## Bước 4 — Analysis, paper composition và HTML

Logic bắt buộc:

> Bối cảnh → dữ liệu → so sánh → cơ chế → phản chứng → hàm ý → hành động.

Cấu trúc mặc định:

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

Quy tắc:

- Executive Summary có 3-7 phát hiện định lượng và 2-5 caveat.
- Mỗi chương có câu hỏi dẫn, evidence, interpretation, mini-conclusion và risk of interpretation.
- Timeline dùng ngày/mốc chính xác.
- Glossary bắt buộc khi có thuật ngữ dễ nhầm.
- So sánh quốc tế phải có comparability matrix.
- Asset history tách price return, FX effect, premium/spread, transaction cost và real return khi có dữ liệu.
- Policy analysis dùng chain: policy → channel → intermediate indicator → outcome → side effect.
- Khi tồn tại quan hệ định lượng có thể bảo vệ được, HTML phải có **Scenario & Sensitivity Lab** để người đọc điều chỉnh giả định và quan sát kết quả. Biến `FACT` chỉ làm baseline; biến người dùng thay đổi phải gắn nhãn `SCENARIO`.
- Không tạo mô hình tương tác chỉ để làm báo cáo sinh động. Nếu không có công thức, hệ số hoặc logic truyền dẫn đủ cơ sở, dùng kịch bản rời rạc Bear/Base/Bull và công bố giới hạn thay vì tạo đường cong giả.

Tone: **người kể chuyện số liệu, không áp đặt kết luận**.

Xem `references/desk_research_03_analysis.md`.

## Bước 5 — Audit bốn lớp

### 5A. Fact/data

Trích mọi claim có số; đối chiếu text-table-chart; kiểm tra source, unit, period, frequency, nominal/real, mean/median và mốc luật/chính sách.

### 5B. Academic/mechanism

Mỗi lý thuyết có nguồn gốc; không bịa framework; causal mechanism phải có supporting evidence và alternative explanations.

### 5C. Citation/provenance

Claim trọng yếu có claim ID; chart/table có source note; derived metric có formula/input; citation phải hỗ trợ đúng entity, metric và period.

### 5D. Editorial

Narrative liền mạch; chương cân đối theo bằng chứng; không lặp; kết luận không mạnh hơn evidence.

Chỉ publish khi quality score ≥85/100 và không có hard fail.

Xem `references/desk_research_04_audit_templates.md`.

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

Mỗi lab tối thiểu phải có:

1. **Baseline:** giá trị gốc, nguồn, kỳ và trạng thái `FACT`/`DERIVED`.
2. **Controls:** 1-5 biến; mỗi biến có label, đơn vị, min, max, step, default và lý do chọn miền.
3. **Model:** một hàm tính thuần, công thức công khai, không dùng số ngẫu nhiên và không gọi mạng.
4. **Outputs:** KPI kết quả cập nhật trực tiếp, có đơn vị và quy tắc làm tròn.
5. **Dynamic chart:** ít nhất một trong các dạng:
   - one-way sensitivity line với điểm hiện tại;
   - tornado chart theo thay đổi so với baseline;
   - breakeven curve;
   - two-way heatmap nếu dùng ECharts hoặc plugin đã khóa phiên bản;
   - waterfall bridge từ baseline sang scenario.
6. **Actions:** Reset; preset Bear/Base/Bull khi phù hợp; xuất JSON/CSV là tùy chọn.
7. **Disclosure:** nhãn `SCENARIO`, công thức, giả định giữ nguyên, limitation và fallback table.

Quy tắc kỹ thuật:

- `input[type="range"]` phải đi cùng ô số hoặc `<output>`; hỗ trợ bàn phím và mobile.
- Cập nhật bằng `chart.data` + `chart.update('none')`; không tạo lại chart sau mỗi lần kéo.
- Dùng `requestAnimationFrame` hoặc debounce khi có nhiều control.
- Một biến được chọn làm trục x; các biến còn lại giữ tại giá trị hiện hành để biểu diễn quan hệ ceteris paribus.
- Không trộn điểm scenario vào chuỗi actual mà không phân biệt màu/nét/legend.
- Mọi giá trị sinh từ control là `SCENARIO` hoặc `DERIVED-SCENARIO`, không được trình bày như forecast chính thức.
- Xem `references/interactive_sensitivity.md`; các chart tĩnh khác vẫn dùng `references/chart_recipes.md`.

### QA bắt buộc

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

Với Scenario & Sensitivity Lab, kiểm tra thêm:

- thay đổi từng control làm KPI và chart thay đổi đúng chiều theo công thức;
- Reset khôi phục baseline;
- preset không vượt min/max;
- output không sinh `NaN`, `Infinity` hoặc đơn vị sai;
- chart resize đúng tại 390 px, 768 px và desktop;
- fallback table hiển thị được khi Chart.js/ECharts không tải.

### Research package tối thiểu

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

# Profile architecture

- **Asset history:** Summary → Scope/Data → Data Quality → Regimes → Return/Volatility → Benchmark → Premium/Spread → Attribution → Scenarios → Limitations.
- **Policy before/after:** Summary → Glossary → Data Quality → Timeline → Before/After → Outcomes → Evidence Chain → Counterfactual → Lessons → Action Matrix.
- **Cross-country:** Summary → Phase criteria → Comparability → Data Quality → Macro Context → Household Finance → Comparison → Drivers/Exceptions → Target-country roadmap.
- **Document consensus:** Document map → Consensus matrix → Disagreement matrix → Forecast comparison → Assumption audit → Data vintage → Implications/Risks.

# Recommendation matrix bắt buộc

Mỗi recommendation có: hành động, target, priority, evidence claim IDs, mechanism, impact basis, risks/trade-offs, owner, horizon, KPI/validation và trigger to revise.

Không đưa lời khuyên đầu tư cá nhân hóa khi dữ liệu/suitability không đủ.

# Chart manifest bắt buộc

Mỗi chart ghi: chart ID, title, analytical question, type, metrics, unit, geography, period/frequency, source IDs, transformations, data status, interpretation, limitations và fallback table.

Với chart tương tác bổ sung: `interactive=true`, input parameters, baseline, min/max/step, formula/model version, output metrics, preset definitions, assumptions held constant và expected direction. Chart manifest phải đủ để tái tạo cùng kết quả từ cùng input.

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
- placeholder/JS error/chart trống/overlap;
- control không hoạt động, sinh `NaN`/`Infinity`, hoặc kết quả không khớp công thức;
- scenario chart không công bố baseline, miền giả định, đơn vị hoặc limitation;
- trộn dữ liệu `FACT` và `SCENARIO` khiến người đọc hiểu nhầm;
- recommendation mạnh hơn bằng chứng;
- lộ prompt hoặc hướng dẫn nội bộ.

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

# Tài nguyên

Publishing engine hiện có:

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
