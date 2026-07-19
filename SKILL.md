---
name: longform
aliases:
  - longform-report
  - financial-desk-research
  - desk-research-finance
  - paper-research
  - longform-desk-research
description: Nghiên cứu bàn đa nguồn evidence-first và xuất bản báo cáo kinh tế - tài chính dạng paper/HTML dài, có evidence audit, chapter schema, claim graph, counterpoint, narrative centerpiece, sticky-scroll, Reader/Research mode và QA.
---

# Longform Financial-Economic Desk Research

Skill hợp nhất ba lớp:

- **Research engine:** query matrix, source hierarchy, evidence ledger, data dictionary, comparability, uncertainty register và claim-level audit.
- **Knowledge engine:** chapter schema, claim graph, counterpoint object, cross-chapter relations và epistemic status.
- **Publishing engine:** dark Longform HTML, KPI/chart/table, minimap, narrative centerpiece, sticky-scroll, Reader/Research mode, Scenario & Sensitivity Lab, print và QA Playwright.

Mục tiêu: báo cáo vừa **paper-ready**, **audit-ready** và **publication-ready**.

## Khi nào kích hoạt

Dùng workflow đầy đủ cho desk/deep research, báo cáo kinh tế-tài chính nhiều chương, chính sách trước-sau, lịch sử tài sản, so sánh quốc tế, tổng hợp nhiều tài liệu, report HTML/PDF/DOCX có nguồn, hoặc interactive digital publication.

Câu hỏi ngắn dùng mode `compact`, nhưng vẫn giữ quy tắc không bịa dữ liệu.

## Output modes

- `research-package`: brief + source/evidence/data/audit + publication manifests.
- `paper`: Markdown/DOCX/PDF.
- `html`: Longform article/dashboard có Reader/Research mode.
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
8. Text, table, chart và narrative visual dùng cùng dataset đã audit.
9. Kết luận/khuyến nghị không mạnh hơn bằng chứng.
10. Bản cuối không chứa placeholder, prompt hoặc hướng dẫn nội bộ.

## Taxonomy claim hai chiều

### Evidence class

| Nhãn | Quy tắc |
|---|---|
| `FACT` | Có nguồn, kỳ, đơn vị |
| `DERIVED` | Có công thức và input claim IDs |
| `INFERENCE` | Có luận cứ và mức chắc chắn |
| `SCENARIO` | Có giả định, trigger, horizon |
| `RECOMMENDATION` | Có target, evidence, risk, KPI |

### Epistemic status

`VERIFIED`, `QUALIFIED`, `DISPUTED`, `AUTHOR_VIEW`, `INSUFFICIENT_EVIDENCE`.

### Content role

`THESIS`, `MECHANISM`, `MILESTONE`, `COUNTERPOINT`, `CAVEAT`, `TAKEAWAY`, `EVIDENCE`.

# Workflow 6 bước

## Bước 1 — Research specification, outline và theme

Tạo `research_brief.md`, chốt:

- câu hỏi trung tâm + 3-8 câu hỏi phụ;
- phạm vi địa lý/thời gian/đối tượng;
- unit of analysis, tần suất, biến và công thức;
- breakpoint và cơ sở chọn;
- audience, output mode, completion criteria;
- family theme/hero mood nếu xuất HTML;
- **chapter map sơ bộ:** guiding question, thesis, centerpiece dự kiến và related chapters.

Chọn profile: `asset-history`, `policy-before-after`, `cross-country-development`, `industry-market`, `document-consensus`, `custom`.

## Bước 2 — Source plan và evidence acquisition

Mỗi câu hỏi phụ có query matrix: mục tiêu, từ khóa, nguồn ưu tiên, dữ liệu cần trích, stopping rule và gap.

Ưu tiên nguồn: cơ quan chính thức → tổ chức quốc tế → regulator/exchange/company filing → paper gốc → tổ chức nghiên cứu có phương pháp → Reuters/FT/Bloomberg → nguồn tổng hợp để định hướng.

Ghi claim vào `evidence_ledger.csv` ngay khi thu thập. Claim trọng yếu nên cross-check hai nguồn độc lập khi khả thi. Không tạo chapter narrative trước khi có evidence inventory tối thiểu.

## Bước 3 — Data normalization và Data Quality

Bắt buộc giữ:

- `source_register.csv`
- `evidence_ledger.csv`
- `data_dictionary.csv`
- `chart_manifest.csv`
- `uncertainty_register.csv`

Kiểm tra actual/derived/interpolated/estimated/forecast; current/constant price; FX/PPP; missing/duplicate/outlier/revision; break in series; comparability giữa quốc gia/giai đoạn. Không nội suy chỉ để làm chart đẹp.

Bổ sung vào evidence ledger: `epistemic_status`, `content_role`, `chapter_ids`, `visual_ids`, `counterpoint_ids`.

## Bước 4 — Analysis, chapter composition và publication design

Logic bắt buộc toàn bài:

> Bối cảnh → dữ liệu → so sánh → cơ chế → phản chứng → hàm ý → hành động.

Mỗi chương phải có:

1. `chapter_id`, title và guiding question;
2. provisional thesis;
3. evidence claim IDs;
4. mechanism hoặc comparison;
5. strongest counterpoint;
6. mini-conclusion và risk of interpretation;
7. takeaway;
8. related chapters;
9. tối đa một narrative centerpiece chính.

Tạo các publication manifests:

- `chapter_schema.csv`
- `claim_graph.csv`
- `counterpoints.csv`
- `narrative_manifest.csv`

### Claim graph

Quan hệ cho phép: `SUPPORTS`, `CONTRADICTS`, `QUALIFIES`, `DERIVED_FROM`, `EXPLAINS`, `APPLIES_TO`, `REFERENCES`, `SYNTHESIZES`, `SUPERSEDES`.

Mỗi edge phải có source/evidence basis hoặc ghi rõ là quan hệ biên tập.

### Counterpoint object

Mỗi counterpoint gồm: question, position A, position B, claim IDs hai phía, strongest evidence, synthesis, unresolved condition và status. Không dùng “ý kiến trái chiều” chung chung không có evidence mapping.

### Narrative centerpiece

Chỉ dùng khi visual giải quyết một câu hỏi kể chuyện rõ ràng. Các loại ưu tiên: `sticky-timeline`, `mechanism-stepper`, `policy-cascade`, `cause-effect-network`, `scenario-path`, `before-after-scroller`.

Mỗi centerpiece phải có trong `narrative_manifest.csv`: chapter ID, visual type, claim IDs, source IDs, data mode, steps, trigger, fallback, accessibility note và limitation.

- `verified-data`: dữ liệu có provenance.
- `illustrative-mechanism`: minh họa cơ chế, không được trình bày như số liệu thực.

### Scenario & Sensitivity Lab

Khi có quan hệ định lượng bảo vệ được, cho phép người đọc điều chỉnh giả định. Baseline dùng `FACT`/`DERIVED`; giá trị từ control dùng `SCENARIO` hoặc `DERIVED-SCENARIO`. Nếu không có công thức đủ cơ sở, dùng Bear/Base/Bull rời rạc và công bố giới hạn.

## Bước 5 — Audit bốn lớp

### 5A. Fact/data

Đối chiếu text-table-chart-narrative visual; kiểm tra source, unit, period, frequency, nominal/real và mốc chính sách.

### 5B. Academic/mechanism

Mỗi lý thuyết/cơ chế có nguồn gốc; causal mechanism phải có supporting evidence và alternative explanations.

### 5C. Citation/provenance và graph integrity

- Claim trọng yếu có claim ID.
- Chart/table/visual có source note.
- Derived metric có formula/input.
- Citation hỗ trợ đúng entity, metric và period.
- Claim graph không có node mồ côi hoặc edge trỏ tới ID không tồn tại.
- Counterpoint tham chiếu claim hợp lệ ở cả hai phía.
- Chapter không dùng claim chưa audit làm thesis/takeaway mà không disclosure.

### 5D. Editorial/narrative

Narrative liền mạch; chương cân đối theo bằng chứng; không lặp; centerpiece thực sự làm rõ luận điểm; takeaway không mạnh hơn evidence; Reader mode không che giấu caveat trọng yếu.

Chỉ publish khi quality score ≥85/100 và không có hard fail.

## Bước 6 — Output engineering và technical QA

### Reader/Research mode

**Reader mode** mặc định:

- ưu tiên guiding question, narrative, visual và takeaway;
- ẩn claim ID, formula và chi tiết provenance khỏi luồng chính;
- vẫn giữ caveat trọng yếu và link nguồn tối thiểu.

**Research mode**:

- hiện claim ID, evidence class, epistemic status, source, formula/input, uncertainty, graph relations và counterpoint mapping.

Hai mode phải dùng cùng DOM/data; không tạo hai bản nội dung có thể lệch số liệu.

### Sticky-scroll

- desktop: narrative steps và sticky visual đồng bộ bằng `IntersectionObserver`;
- mobile: hủy sticky, xếp dọc step → visual/detail;
- hỗ trợ keyboard, reduced motion và print fallback;
- mỗi step có `data-step`, claim IDs và fallback prose;
- không dùng sticky-scroll nếu chỉ có 1-2 mốc hoặc visual không đổi theo step.

Dùng `assets/narrative_components.html` và `references/narrative_publication.md`.

### QA bắt buộc

- không còn `{{TOKEN}}`;
- chart/canvas khớp;
- không JS error, chart trống, clipping/overflow;
- section/minimap/presentation đồng bộ;
- Reader/Research toggle hoạt động và không làm mất nội dung;
- sticky step active đúng khi scroll/click/keyboard;
- mobile 390 px, tablet 768 px, desktop và print hợp lệ;
- fallback table/prose hiện khi chart hoặc JS không tải;
- không sinh `NaN`/`Infinity`;
- graph/schema validator pass.

Khởi tạo và QA:

```bash
python "$SKILL_DIR/scripts/init_research_project.py" \
  --topic "[TOPIC]" --profile custom --out ./research-project

python "$SKILL_DIR/scripts/qa_research_project.py" ./research-project

node "$SKILL_DIR/scripts/qa_article.js" \
  --url=file://./research-project/index.html \
  --output=/tmp/qa-shots
```

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
├── chapter_schema.csv
├── claim_graph.csv
├── counterpoints.csv
├── narrative_manifest.csv
├── paper.md hoặc index.html
└── qa_report.md
```

## Chart manifest bắt buộc

Mỗi chart ghi: chart ID, title, analytical question, type, metrics, unit, geography, period/frequency, source IDs, transformations, data status, interpretation, limitations và fallback table. Chart tương tác bổ sung input parameters, baseline, min/max/step, formula/model version, outputs, presets, assumptions held constant và expected direction.

## Hard fail

Không publish nếu:

- số liệu trọng yếu không có provenance;
- nội suy/ước lượng không gắn nhãn;
- text, table, chart hoặc narrative visual mâu thuẫn;
- trộn đơn vị/định nghĩa;
- causal attribution không có phương pháp;
- citation không hỗ trợ claim;
- claim graph có ID/edge không hợp lệ;
- counterpoint chỉ có một phía hoặc không có evidence mapping;
- centerpiece dùng dữ liệu minh họa nhưng không gắn `illustrative-mechanism`;
- Reader mode ẩn caveat làm thay đổi bản chất kết luận;
- sticky-scroll không có mobile/print fallback;
- placeholder/JS error/chart trống/overlap;
- control sinh `NaN`/`Infinity` hoặc kết quả không khớp công thức;
- trộn `FACT` và `SCENARIO` khiến người đọc hiểu nhầm;
- recommendation mạnh hơn bằng chứng;
- lộ prompt hoặc hướng dẫn nội bộ.

## Tài nguyên

- `assets/article_template.html`
- `assets/narrative_components.html`
- `schemas/publication.schema.json`
- `references/components.md`
- `references/chart_recipes.md`
- `references/interactive_sensitivity.md`
- `references/narrative_publication.md`
- `references/themes.md`
- `references/navigation.md`
- `references/citations.md`
- `references/fact_check.md`
- `references/academic_foundations.md`
- `references/desk_research_01_protocol.md`
- `references/desk_research_02_data.md`
- `references/desk_research_03_analysis.md`
- `references/desk_research_04_audit_templates.md`
- `scripts/init_research_project.py`
- `scripts/qa_research_project.py`
- `scripts/qa_article.js`
