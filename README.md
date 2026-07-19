# Longform Financial-Economic Research — Skill

Skill tạo báo cáo nghiên cứu kinh tế - tài chính dạng **paper, HTML dài và Research Atlas**. Hệ thống kết hợp:

- nghiên cứu đa nguồn và evidence ledger;
- claim-level audit, source registry và data dictionary;
- Chart.js/ECharts, minimap, presentation mode và Scenario & Sensitivity Lab;
- kiến trúc tri thức tái sử dụng: module, chapter, question, claim, source, misconception, pathway, thesis, glossary, case và interaction rules.

> Trong agent, skill được gọi qua `/longform` hoặc các alias trong `SKILL.md`.

## Cấu trúc chính

```text
longform-report/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── article_template.html
├── references/
│   ├── academic_foundations.md
│   ├── chart_recipes.md
│   ├── citations.md
│   ├── components.md
│   ├── desk_research_01_protocol.md
│   ├── desk_research_02_data.md
│   ├── desk_research_03_analysis.md
│   ├── desk_research_04_audit_templates.md
│   ├── fact_check.md
│   ├── industry_market_profile.md
│   ├── interactive_sensitivity.md
│   ├── navigation.md
│   ├── research_atlas.md
│   └── themes.md
└── scripts/
    ├── init_research_project.py
    ├── qa_article.js
    ├── qa_research_atlas.py
    └── qa_research_project.py
```

## Khởi tạo project thông thường

```bash
python "$SKILL_DIR/scripts/init_research_project.py" \
  --topic "[TOPIC]" \
  --profile custom \
  --out ./research-project
```

## Khởi tạo Research Atlas

```bash
python "$SKILL_DIR/scripts/init_research_project.py" \
  --topic "[TOPIC]" \
  --profile knowledge-atlas \
  --out ./research-project
```

Profile `knowledge-atlas` tự tạo thư mục `atlas/` và các JSON entity files. Có thể dùng `--atlas` với profile khác khi cần.

## QA

### Research package

```bash
python "$SKILL_DIR/scripts/qa_research_project.py" ./research-project
```

### Research Atlas

```bash
python "$SKILL_DIR/scripts/qa_research_atlas.py" ./research-project/atlas
```

### HTML

`qa_article.js` cần Playwright:

```bash
npm install playwright --prefix /tmp/qa-runner
npx playwright install chromium
node "$SKILL_DIR/scripts/qa_article.js" \
  --url=file://$PWD/index.html \
  --output=/tmp/qa-shots
```

## Nguyên tắc

- Không bịa dữ liệu.
- Dữ liệu quan sát, tính toán, ước lượng, mô phỏng và kịch bản phải được gắn nhãn.
- Claim trọng yếu phải có provenance.
- Chart và text dùng cùng dataset đã audit.
- HTML là view; JSON/CSV đã audit là source of truth khi xuất Atlas.
- Không trình bày heuristic score như xác suất nếu chưa có mô hình xác suất được hiệu chỉnh.
