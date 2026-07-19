# Longform Report — Skill

Skill tạo **báo cáo tự nghiên cứu dạng paper và interactive article HTML dài**: evidence-first, chapter-based, dark theme, Chart.js/ECharts, minimap, progress bar, presentation mode, **Scenario & Sensitivity Lab**, narrative centerpiece, sticky-scroll và **Reader/Research mode**.

Mỗi báo cáo đứng trên ba lớp phối hợp:

- **Research engine** — query matrix, source hierarchy, evidence ledger, data dictionary, uncertainty register và audit bốn lớp.
- **Knowledge engine** — chapter schema, claim graph, counterpoint object và cross-chapter relations.
- **Publishing engine** — article/dashboard, narrative visual, sticky-scroll, Reader/Research mode, print và QA Playwright.

> Trong agent, skill được gọi qua `/longform-report` hoặc `/longform`.

## Cấu trúc

```text
longformskill/
├── SKILL.md
├── assets/
│   ├── article_template.html
│   └── narrative_components.html
├── schemas/
│   └── publication.schema.json
├── references/
│   ├── components.md
│   ├── chart_recipes.md
│   ├── interactive_sensitivity.md
│   ├── narrative_publication.md
│   ├── themes.md
│   ├── navigation.md
│   ├── citations.md
│   ├── fact_check.md
│   ├── academic_foundations.md
│   ├── desk_research_01_protocol.md
│   ├── desk_research_02_data.md
│   ├── desk_research_03_analysis.md
│   └── desk_research_04_audit_templates.md
├── scripts/
│   ├── init_research_project.py
│   ├── qa_research_project.py
│   └── qa_article.js
└── agents/
    └── openai.yaml
```

## Workflow 6 bước

| Bước | Nội dung |
|---|---|
| 1 | Research specification, outline, theme và chapter map |
| 2 | Source plan, query matrix và evidence acquisition |
| 3 | Data normalization, data quality và uncertainty register |
| 4 | Analysis, chapter composition, claim graph, counterpoint và narrative centerpiece |
| 5 | Audit fact/data, academic/mechanism, provenance/graph và editorial/narrative |
| 6 | Output engineering, Reader/Research mode, sticky-scroll và technical QA |

Workflow cũ không bị thay thế. Các lớp publication mới được tạo **sau evidence acquisition và normalization**, dùng cùng dataset đã audit.

## Research package

```text
research-project/
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
├── recommendation_matrix.csv
├── paper.md hoặc index.html
└── qa_report.md
```

## Khởi tạo và kiểm tra

```bash
python "$SKILL_DIR/scripts/init_research_project.py" \
  --topic "Chính sách BĐS Trung Quốc trước và sau 2016" \
  --profile policy-before-after \
  --out ./research-project

python "$SKILL_DIR/scripts/qa_research_project.py" ./research-project
```

Validator kiểm tra thêm:

- chapter ID và claim ID không trùng;
- claim graph không trỏ đến node không tồn tại;
- relation type hợp lệ;
- counterpoint có đủ hai phía và evidence mapping;
- narrative visual tham chiếu chapter, claim và source hợp lệ;
- `illustrative-mechanism` có disclosure;
- sticky-scroll có đủ step, mobile fallback và accessibility note.

## Reader/Research mode

- **Reader mode:** ưu tiên câu hỏi dẫn, narrative, visual, takeaway và caveat trọng yếu.
- **Research mode:** hiện claim ID, evidence class, epistemic status, source, formula, uncertainty và graph relations.

Hai mode dùng cùng DOM/data để tránh lệch số liệu.

## Narrative centerpiece

Một chương chỉ nên có tối đa một centerpiece chính. Các pattern ưu tiên:

- sticky timeline;
- mechanism stepper;
- policy cascade;
- cause-effect network;
- scenario path;
- before/after scroller.

Dùng `assets/narrative_components.html` làm drop-in component và xem quy tắc chi tiết tại `references/narrative_publication.md`.

## Hai trục chất lượng giữ nguyên

| Trục | Đối tượng |
|---|---|
| **Số liệu thật** | số, ngày, tỷ lệ, chỉ số, mốc luật/chính sách |
| **Học thuật thật** | lý thuyết, cơ chế, tác giả, tác phẩm và bằng chứng nhân quả |

Các lớp mới bổ sung **graph integrity** và **narrative integrity**, không làm giảm yêu cầu fact-check hiện có.

## Cài đặt

```bash
git clone https://github.com/vh25101993-glitch/longformskill.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/longform-report"
```

Tên thư mục nên là `longform-report` để biến `$SKILL_DIR` và các lệnh nội bộ hoạt động nhất quán.
