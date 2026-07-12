# Desk Research Protocol & Evidence Ledger

## 1. Decompose the question

Tạo cây câu hỏi tối đa 3 tầng:

- Central question
  - Descriptive: điều gì đã xảy ra?
  - Comparative: khác nhau ở đâu?
  - Causal/mechanism: vì sao?
  - Evaluative: hiệu quả/rủi ro?
  - Prescriptive: nên làm gì và kiểm chứng thế nào?

Mỗi nhánh phải có deliverable rõ: data series, legal text, timeline, literature, case hoặc benchmark.

## 2. Query matrix

Mỗi dòng trong `research_plan.csv` gồm: `question_id`, `research_question`, `query_local_language`, `query_english`, `preferred_domains`, `source_type`, `expected_metric_or_document`, `status`, `gap`.

Tìm bằng ngôn ngữ gốc khi nghiên cứu quốc gia khác.

## 3. Source hierarchy

1. **Tier A — Primary/official:** luật, nghị định, cơ quan thống kê, central bank, ministry, regulator, exchange, official database.
2. **Tier B — International authoritative:** World Bank, IMF, OECD, BIS, UN, Eurostat, IEA, WTO.
3. **Tier C — Academic/original research:** journal, NBER/CEPR/working papers, university research, methodology notes.
4. **Tier D — Market/industry:** filings, rating agencies, associations, vendors có phương pháp rõ.
5. **Tier E — Reputable news:** Reuters, FT, Bloomberg, WSJ, major national outlets.
6. **Tier F — Discovery only:** blogs, aggregators, Wikipedia, search snippets; không dùng làm nguồn duy nhất cho claim trọng yếu.

## 4. Cross-check rule

- Legal/policy date: official text + one independent confirmation.
- Current market data: official/direct data feed; secondary source chỉ dùng cho context.
- Historical series: methodology note + alternative series comparison khi có.
- Contested estimates: hiển thị range và định nghĩa riêng của từng nguồn.

## 5. Stopping rule

Một nhánh hoàn tất khi:

- answerable by evidence;
- không còn xung đột định nghĩa chưa giải quyết;
- không che giấu bất đồng nguồn trọng yếu;
- nguồn mới bổ sung rất ít thông tin;
- evidence ledger đủ để audit.

## 6. Research gap handling

Dùng một trong bốn nhãn:

- `NOT_FOUND` — chưa tìm thấy;
- `NOT_AVAILABLE` — dữ liệu không công bố;
- `NOT_COMPARABLE` — định nghĩa không tương thích;
- `LOW_CONFIDENCE` — chỉ có estimate/secondary evidence.

Không lấp khoảng trống bằng số tưởng tượng.

# Evidence ledger

Evidence ledger là nguồn sự thật duy nhất cho claim định lượng và claim chính sách.

## Schema

| Field | Meaning |
|---|---|
| claim_id | ID duy nhất, ví dụ `C-023` |
| section | Chương dự kiến |
| claim_text | Claim ngắn, một ý |
| claim_class | FACT / DERIVED / INFERENCE / SCENARIO / RECOMMENDATION |
| importance | Critical / High / Medium / Low |
| metric | Tên biến |
| value | Giá trị |
| unit | Đơn vị |
| geography | Phạm vi địa lý |
| period | Năm/quý/tháng/ngày |
| frequency | Daily/Monthly/Quarterly/Annual/Event |
| source_id | Link tới source register |
| source_location | Page/table/series/code |
| source_type | Primary/Official/Academic/Market/News |
| data_status | Actual/Revised/Derived/Interpolated/Estimated/Forecast |
| formula | Công thức nếu derived |
| comparability | High/Medium/Low |
| confidence | High/Medium/Low |
| contradiction | Có nguồn trái chiều hay không |
| notes | Caveat |
| audit_status | Pending/Verified/Rejected |

## Quy tắc

- Một claim chỉ chứa một đơn vị logic.
- Claim Critical/High cần citation trực tiếp.
- Claim derived phải tham chiếu claim đầu vào.
- Claim inference phải liệt kê supporting claim IDs và alternative explanation.
- Claim recommendation phải liệt kê evidence basis.
- Không xóa claim bị bác bỏ; đổi trạng thái `Rejected` để giữ audit trail.

## Ví dụ derived

```text
claim_id: C-041
claim_class: DERIVED
claim_text: CAGR giá tài sản giai đoạn 2009-2025 là X%/năm
formula: (end_value / start_value)^(1/16) - 1
inputs: C-012, C-013
rounding: 2 decimals
```

## Ví dụ inference

```text
claim_id: C-078
claim_class: INFERENCE
claim_text: Premium nội địa mở rộng chủ yếu trong các giai đoạn hạn chế nguồn cung
supporting_claims: C-051, C-052, C-060
alternative_explanations: FX volatility, retail demand, measurement timing
confidence: Medium
```
