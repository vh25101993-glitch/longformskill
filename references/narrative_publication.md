# Narrative Publication Layer

Tài liệu này mở rộng Longform từ research report/dashboard thành interactive digital publication, nhưng không thay thế workflow 6 bước, evidence ledger, chart manifest, uncertainty register hoặc QA.

## 1. Nguyên tắc kiến trúc

```text
Research question
→ Evidence ledger
→ Claim graph
→ Chapter schema
→ Counterpoint
→ Narrative manifest
→ Reader/Research renderer
```

Nguồn dữ liệu chuẩn vẫn là:

- `evidence_ledger.csv` cho claim;
- `source_register.csv` cho source;
- `chart_manifest.csv` cho analytical visual;
- `uncertainty_register.csv` cho limitation/risk.

Các file mới chỉ tổ chức quan hệ và cách xuất bản.

## 2. Chapter schema

File: `chapter_schema.csv`

| Field | Required | Meaning |
|---|---:|---|
| `chapter_id` | yes | ID ổn định, ví dụ `ch12` |
| `chapter_number` | yes | Thứ tự hiển thị |
| `title` | yes | Tiêu đề |
| `guiding_question` | yes | Câu hỏi chương cần trả lời |
| `provisional_thesis` | yes | Luận đề ban đầu |
| `section_ids` | no | Danh sách section, phân tách `;` |
| `claim_ids` | yes | Claim dùng trong chương |
| `centerpiece_visual_id` | no | Tối đa một visual |
| `counterpoint_id` | no | Counterpoint chính |
| `related_chapter_ids` | no | Cross-reference |
| `mini_conclusion` | yes | Câu trả lời sau evidence |
| `takeaway` | yes | Một câu ngắn |
| `reader_summary` | yes | Tóm tắt cho Reader mode |
| `research_disclosure` | yes | Method/caveat cho Research mode |
| `default_mode` | yes | `reader`, `research`, `reader-with-research-toggle` |
| `status` | yes | `DRAFT`, `AUDITED`, `PUBLISHED` |

### Quy tắc

- Guiding question phải có thể trả lời bằng evidence trong chapter.
- Provisional thesis và mini-conclusion có thể khác nhau; nếu giống nhau, vẫn phải chứng minh bằng claim.
- `claim_ids` không được tham chiếu claim ngoài evidence ledger.
- `centerpiece_visual_id` phải tồn tại trong `narrative_manifest.csv`.
- Không nhiều hơn một centerpiece/chapter.
- `takeaway` không được mạnh hơn mini-conclusion.

## 3. Claim graph

File: `claim_graph.csv`

| Field | Required | Meaning |
|---|---:|---|
| `edge_id` | yes | ID duy nhất |
| `from_claim_id` | yes | Claim nguồn |
| `relation` | yes | Quan hệ |
| `to_claim_id` | yes | Claim đích |
| `rationale` | yes | Vì sao quan hệ tồn tại |
| `source_ids` | conditional | Nguồn hỗ trợ edge nếu cần |
| `status` | yes | `DRAFT`, `AUDITED`, `REJECTED` |

Allowed relations:

- `SUPPORTS`
- `CONTRADICTS`
- `QUALIFIES`
- `DERIVED_FROM`
- `EXPLAINS`
- `APPLIES_TO`
- `REFERENCES`
- `SYNTHESIZES`
- `SUPERSEDES`

Không dùng edge để thay thế citation. Một claim vẫn phải có provenance riêng.

## 4. Counterpoint object

File: `counterpoints.csv`

Mỗi counterpoint cần hai vị thế mạnh nhất, không dựng “straw man”.

| Field | Meaning |
|---|---|
| `counterpoint_id` | ID |
| `chapter_id` | Chapter sở hữu |
| `question` | Câu hỏi tranh luận |
| `position_a_label` | Tên vị thế A |
| `position_a_claim_ids` | Evidence cho A |
| `position_b_label` | Tên vị thế B |
| `position_b_claim_ids` | Evidence cho B |
| `synthesis` | Tổng hợp/điều kiện đúng |
| `epistemic_status` | Thường là `DISPUTED` hoặc `QUALIFIED` |
| `conditions_to_revise` | Trigger sửa kết luận |

Counterpoint hard fail nếu:

- thiếu một vị thế;
- vị thế không có claim;
- claim không tồn tại;
- synthesis khẳng định tuyệt đối trong khi status là `DISPUTED`.

## 5. Narrative manifest

File: `narrative_manifest.csv`

| Field | Meaning |
|---|---|
| `visual_id` | ID visual |
| `chapter_id` | Chapter |
| `title` | Title |
| `narrative_question` | Câu hỏi visual trả lời |
| `visual_type` | `TIMELINE`, `MECHANISM_STEPPER`, `POLICY_CASCADE`, `CAUSE_EFFECT_NETWORK`, `SCENARIO_PATH`, `BEFORE_AFTER`, `CHART` |
| `layout` | `STATIC`, `STICKY_SCROLL`, `STEPPER`, `DASHBOARD`, `SCENARIO_LAB` |
| `centerpiece` | yes/no |
| `step_ids` | Danh sách step |
| `claim_ids` | Claims |
| `source_ids` | Sources |
| `data_mode` | `VERIFIED_DATA`, `ILLUSTRATIVE_MECHANISM`, `MIXED_WITH_DISCLOSURE` |
| `reader_summary` | Tóm tắt ngắn |
| `research_disclosure` | Method/source/formula/caveat |
| `fallback_table` | ID hoặc mô tả fallback |
| `keyboard_support` | yes/no |
| `reduced_motion` | yes/no |
| `print_fallback` | yes/no |
| `limitations` | Hạn chế |

### Chọn visual type

| Analytical need | Preferred visual |
|---|---|
| Diễn biến theo thời gian | Timeline/sticky timeline |
| Cơ chế nhiều bước | Mechanism stepper |
| Chính sách truyền qua kênh | Policy cascade |
| Nhiều quan hệ hỗ trợ/phản bác | Cause-effect network |
| Kịch bản có giả định | Scenario path/lab |
| So sánh hai trạng thái | Before-after |
| Tra cứu nhiều series | Analytical chart/dashboard |

## 6. Narrative centerpiece

Centerpiece không đồng nghĩa với chart lớn nhất. Nó là visual trả lời trực tiếp guiding question.

### Điều kiện bắt buộc

- có analytical/narrative question;
- có claim mapping;
- có source mapping;
- có interpretation và limitation;
- tạo thêm khả năng hiểu, không chỉ lặp bảng;
- có fallback.

### Không dùng centerpiece khi

- chapter chỉ có một số liệu đơn giản;
- visual không làm rõ cơ chế;
- thiếu dữ liệu để bảo vệ thứ tự/quan hệ;
- mục tiêu là tra cứu chính xác nhiều chỉ tiêu.

## 7. Sticky-scroll

Dùng khi thứ tự bước là một phần của lập luận.

### Minimum viable structure

```html
<section class="sticky-story" data-story-id="china-transition">
  <div class="story-steps">
    <article class="story-step is-active" tabindex="0" data-panel="panel-1">
      <span class="story-kicker">2015–2016</span>
      <h3>Cảnh báo</h3>
      <p>...</p>
    </article>
    <article class="story-step" tabindex="0" data-panel="panel-2">...</article>
    <article class="story-step" tabindex="0" data-panel="panel-3">...</article>
  </div>

  <div class="story-stage" aria-live="polite">
    <div class="story-panel is-active" id="panel-1">...</div>
    <div class="story-panel" id="panel-2">...</div>
    <div class="story-panel" id="panel-3">...</div>
  </div>
</section>
```

### Accessibility

- Step dùng `article`, `button` hoặc phần tử focusable.
- `aria-current="step"` cho active step.
- Không phụ thuộc chỉ vào màu.
- `aria-live="polite"` cho stage nếu nội dung thay đổi.
- Với `prefers-reduced-motion`, bỏ smooth transition.
- No-JS: hiển thị tất cả panel tuyến tính.
- Print: hiển thị tất cả step và panel.
- Mobile: một cột, stage không sticky.

### Không tạo false precision

Nếu visual mô tả cơ chế định tính:

```html
<div class="visual-disclosure">
  Minh họa cơ chế — không phải dữ liệu quan sát theo tỷ lệ.
</div>
```

## 8. Reader/Research mode

### Data attributes

```html
<body data-view-mode="reader">
  <div class="mode-switch" role="group" aria-label="Chế độ đọc">
    <button data-set-view="reader" aria-pressed="true">Reader</button>
    <button data-set-view="research" aria-pressed="false">Research</button>
  </div>

  <p>Narrative dùng chung.</p>

  <div class="reader-only">Tóm tắt dễ đọc.</div>

  <aside class="research-only claim-meta">
    <code>CLM-090</code>
    <span>FACT · VERIFIED</span>
    <a href="#src-053">SRC-053</a>
  </aside>
</body>
```

### Reader mode phải giữ

- conclusion;
- caveat trọng yếu;
- source rút gọn cho claim quan trọng;
- đơn vị/kỳ của số liệu;
- disclosure khi visual là minh họa.

### Research mode bổ sung

- claim ID;
- claim class;
- epistemic status;
- source/location;
- formula/input claims;
- graph relations;
- uncertainty;
- fallback data;
- model version.

### Anti-pattern

- Viết hai phiên bản số liệu riêng.
- Reader mode ẩn limitation làm thay đổi kết luận.
- Research mode chỉ thêm mã ID nhưng không thêm provenance.
- Toggle làm mất state của chart hoặc scenario lab.

## 9. Mapping từ research package sang renderer

```text
evidence_ledger.csv
  → claims

source_register.csv
  → sources

chart_manifest.csv
  → analytical visuals

chapter_schema.csv
  → chapter navigation + narrative order

claim_graph.csv
  → related claims + support/contradiction panel

counterpoints.csv
  → debate component

narrative_manifest.csv
  → centerpiece + sticky/stepper renderer

uncertainty_register.csv
  → caveat and limitation panels
```

Không copy số liệu thủ công vào nhiều component. Renderer phải tham chiếu cùng claim.

## 10. QA checklist

### Schema

- [ ] Chapter IDs unique.
- [ ] Claim IDs trong chapter tồn tại.
- [ ] Centerpiece/counterpoint references tồn tại.
- [ ] Claim graph endpoints tồn tại.
- [ ] Relation thuộc allowed set.
- [ ] Counterpoint có hai phía.
- [ ] Tối đa một centerpiece/chapter.

### Reader/Research

- [ ] Toggle có `aria-pressed`.
- [ ] Keyboard hoạt động.
- [ ] Preference lưu cục bộ.
- [ ] No-JS vẫn đọc được.
- [ ] Reader giữ caveat trọng yếu.
- [ ] Research hiện provenance và uncertainty.
- [ ] Print mode được xác định rõ.

### Sticky-scroll

- [ ] Ít nhất 3 step.
- [ ] Step order có ý nghĩa.
- [ ] Mỗi step map claim/source.
- [ ] Focus/scroll cùng cập nhật active panel.
- [ ] Reduced motion.
- [ ] Mobile one-column.
- [ ] Print/no-JS fallback.
- [ ] Fallback chronology/table.
