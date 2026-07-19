# Research Atlas Architecture

Tài liệu này định nghĩa chế độ `research-atlas` cho skill `longform`. Mục tiêu là chuyển một báo cáo dài từ sản phẩm HTML đơn lẻ thành một hệ thống tri thức có thể tra cứu, kiểm chứng, liên kết và tái sử dụng trong các báo cáo sau.

## 1. Khi nào kích hoạt

Kích hoạt khi có ít nhất một trong các điều kiện:

- Chủ đề có từ 8 chương trở lên hoặc chia thành nhiều module.
- Có từ 20 claim trọng yếu, 20 nguồn hoặc 10 thuật ngữ cần quản trị.
- Người dùng cần cổng tra cứu, knowledge base, atlas, handbook hoặc website nghiên cứu nhiều bài.
- Nội dung cần nhiều cửa vào: câu hỏi, thuật ngữ, hiểu nhầm, case study, cơ chế hoặc công cụ tương tác.
- Dữ liệu, claim hoặc biểu đồ dự kiến được tái sử dụng trong các sản phẩm tiếp theo.

Không kích hoạt chỉ để làm giao diện phức tạp. Báo cáo ngắn, câu hỏi một lần hoặc chủ đề không có quan hệ dữ liệu đủ rõ dùng mode `compact`, `paper` hoặc `html` thông thường.

## 2. Chuỗi lập luận chuẩn

Mỗi đơn vị phân tích quan trọng phải có thể truy vết theo chuỗi:

```text
QUESTION
→ CLAIM
→ EVIDENCE
→ MECHANISM
→ COUNTER-EVIDENCE / ALTERNATIVE EXPLANATION
→ APPLICATION
→ PERSONAL / BUSINESS / POLICY EXPOSURE
→ LIMITATION
```

Đơn vị kiểm chứng là `claim`, không phải đoạn văn.

## 3. Các thực thể cốt lõi

### 3.1 Module

```json
{
  "id": "M01",
  "slug": "main-street-vs-wall-street",
  "title": "Main Street vs Wall Street",
  "summary": "...",
  "version": "1.0.0",
  "publicationStatus": "public",
  "maturity": "reviewed",
  "plannedChapters": 18,
  "publishedChapters": 18,
  "reviewedChapters": 18,
  "chapterIds": ["M01-C01"],
  "topicIds": ["TOPIC-001"]
}
```

Không dùng một biến `chapters` để đồng thời biểu thị số chương dự kiến, đã xuất bản và đã kiểm duyệt.

### 3.2 Chapter

```json
{
  "id": "M01-C01",
  "moduleId": "M01",
  "number": 1,
  "stage": "A",
  "title": "...",
  "leadQuestion": "...",
  "summary": "...",
  "claimIds": ["CLM-001"],
  "visualIds": ["VIS-001"],
  "sourceIds": ["SRC-001"],
  "caseIds": [],
  "takeaway": "...",
  "riskOfInterpretation": "..."
}
```

### 3.3 Claim

```json
{
  "id": "CLM-001",
  "moduleId": "M01",
  "chapterIds": ["M01-C01"],
  "statementClass": "FACT",
  "claimType": "mechanism",
  "text": "...",
  "status": "verified",
  "confidence": "high",
  "conditions": [],
  "sourceIds": ["SRC-001"],
  "counterEvidenceIds": [],
  "limitations": []
}
```

Giá trị `status` khuyến nghị:

- `verified`: bằng chứng trực tiếp, phù hợp entity/metric/period.
- `qualified`: đúng trong điều kiện đã nêu.
- `disputed`: nguồn đáng tin cậy bất đồng đáng kể.
- `interpretation`: diễn giải có luận cứ, không phải dữ kiện quan sát.
- `behavioral-hypothesis`: giả thuyết hành vi cần nêu giới hạn.
- `insufficient-evidence`: chưa đủ điều kiện kết luận.

`confidence` không thay thế `status`. Confidence phải dựa trên chất lượng, độ trực tiếp, tính nhất quán và độ phủ của bằng chứng.

### 3.4 Source

```json
{
  "id": "SRC-001",
  "title": "...",
  "authors": ["..."],
  "year": 2026,
  "publisher": "IMF",
  "sourceTier": "T2",
  "url": "...",
  "accessedAt": "2026-07-19",
  "geography": ["Global"],
  "period": "2020-2026",
  "claimIds": ["CLM-001"],
  "moduleIds": ["M01"]
}
```

Tầng nguồn mặc định:

1. `T1`: văn bản, dataset hoặc paper gốc.
2. `T2`: tổ chức quốc tế, ngân hàng trung ương, cơ quan thống kê.
3. `T3`: journal/working paper có phương pháp rõ.
4. `T4`: sở giao dịch, doanh nghiệp, tổ chức ngành.
5. `T5`: Reuters, FT, Bloomberg và financial media uy tín.
6. `T6`: báo cáo môi giới, blog chuyên gia hoặc nguồn tổng hợp; chủ yếu dùng định hướng, không làm nguồn duy nhất cho claim trọng yếu.

### 3.5 Question

```json
{
  "id": "Q-001",
  "group": "Lạm phát và sức mua",
  "question": "Vì sao CPI thấp hơn cảm nhận lạm phát của hộ gia đình?",
  "shortAnswer": "...",
  "moduleIds": ["M02", "M04"],
  "chapterIds": ["M02-C03"],
  "claimIds": ["CLM-014"],
  "conceptIds": ["TERM-009"],
  "misconceptionIds": ["MIS-002"],
  "readingPath": ["M02-C03", "M04-C02"]
}
```

Question Router cho phép người đọc bắt đầu từ vấn đề thực tế thay vì phải biết cấu trúc module.

### 3.6 Misconception

```json
{
  "id": "MIS-001",
  "wrongBelief": "Lạm phát giảm nghĩa là giá sẽ giảm.",
  "correction": "Lạm phát giảm tốc không đồng nghĩa mức giá chung giảm.",
  "explanation": "...",
  "moduleIds": ["M02"],
  "claimIds": ["CLM-018"],
  "pathwayIds": ["PATH-001"]
}
```

Nội dung giao diện mặc định hiển thị ngắn; phần cơ chế và nguồn dùng progressive disclosure.

### 3.7 Damage / Exposure Pathway

```json
{
  "id": "PATH-001",
  "title": "Nhầm giảm tốc lạm phát với giảm giá",
  "steps": {
    "macro": "Lạm phát giảm tốc",
    "misinterpretation": "Kỳ vọng giá quay lại mức cũ",
    "behavior": "Trì hoãn điều chỉnh ngân sách",
    "balanceSheet": "Tiết kiệm thực không đủ",
    "damage": "Thiếu hụt tài chính dài hạn"
  },
  "misconceptionIds": ["MIS-001"],
  "claimIds": ["CLM-018"],
  "moduleIds": ["M02"]
}
```

Có thể thay `balanceSheet` bằng `businessExposure` hoặc `policyExposure` tùy đối tượng nghiên cứu.

### 3.8 Thesis

```json
{
  "id": "TH-001",
  "text": "Cùng một cú sốc vĩ mô tạo tác động khác nhau tùy cấu trúc bảng cân đối.",
  "layers": ["MACRO", "MARKETS", "MONEY"],
  "moduleIds": ["M01", "M04"],
  "claimIds": ["CLM-041", "CLM-112"]
}
```

Thesis là kết luận tổng hợp xuyên module, không được tạo ra nếu claim nền chưa qua audit.

### 3.9 Glossary Term

```json
{
  "id": "TERM-001",
  "term": "Output gap",
  "vi": "Khoảng sản lượng",
  "definition": "Chênh lệch giữa sản lượng thực tế và sản lượng tiềm năng.",
  "moduleIds": ["M03"],
  "chapterIds": ["M03-C02"],
  "sourceIds": ["SRC-021"]
}
```

### 3.10 Interaction Rule

```json
{
  "id": "RULE-001",
  "labId": "LAB-001",
  "inputVariable": "energyShock",
  "condition": ">= 2",
  "scoreEffects": {
    "stagflation": 2,
    "costPushInflation": 3
  },
  "claimIds": ["CLM-067"],
  "sourceIds": ["SRC-031"],
  "modelVersion": "1.0.0"
}
```

Điểm từ rules table là heuristic score, không phải xác suất. Giao diện phải ghi rõ `score 80/100 theo bộ quy tắc`, không ghi `xác suất 80%` nếu chưa có mô hình xác suất được hiệu chỉnh.

## 4. Phân loại dữ liệu

Mỗi giá trị định lượng phải có tối thiểu:

```json
{
  "value": 9.1,
  "unit": "%",
  "period": "2022-06",
  "frequency": "monthly",
  "geography": "United States",
  "dataType": "observed",
  "sourceId": "SRC-123",
  "transformation": "none",
  "accessedAt": "2026-07-19",
  "confidence": "high"
}
```

`dataType` cho phép:

- `observed`
- `derived`
- `interpolated`
- `estimated`
- `forecast`
- `simulation`
- `scenario`
- `heuristic-score`

Không trộn `observed` với `scenario` trong cùng series mà không phân biệt legend, nét, vùng nền và source note.

## 5. Package mặc định

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

`atlas_manifest.json` là điểm vào duy nhất, khai báo version, generatedAt, schemaVersion, counts và đường dẫn file.

## 6. Metrics

Mọi KPI phải tính từ dữ liệu, không nhập lặp thủ công:

```text
moduleCount = count(modules)
chapterCount = count(chapters where publicationStatus = published)
claimCount = count(claims)
verifiedClaimCount = count(claims where status = verified)
sourceCount = count(unique sources)
chartCount = count(chart manifest)
questionCount = count(questions)
```

Khi hiển thị, phải nói rõ mẫu số và định nghĩa. Ví dụ `18/24 chương đã xuất bản`, không chỉ ghi `24 chương`.

## 7. Giao diện và điều hướng

Atlas nên có các cửa vào:

- Project/module map.
- Question Router.
- Claim Explorer.
- Misconception Library.
- Causal/Exposure Pathways.
- Thesis Map.
- Case Explorer.
- Glossary.
- Source Registry.
- Global search.

Quy tắc UX:

- Non-linear navigation nhưng luôn có breadcrumb và nút trở về atlas.
- Nội dung chi tiết dùng progressive disclosure.
- Cross-link theo ID, không copy-paste cùng một nội dung ở nhiều nơi.
- Mỗi chapter có related questions, claims, terms, cases và sources.
- Mobile không có scroll ngang; bảng rộng có card fallback.
- Presentation mode dùng cùng section IDs với minimap.

## 8. Kiểm tra toàn vẹn dữ liệu

Bắt buộc kiểm tra:

1. Mọi ID duy nhất trong phạm vi atlas.
2. Mọi foreign key tham chiếu tới entity tồn tại.
3. Không có source, claim, chapter hoặc question mồ côi trừ khi được gắn `draft`.
4. Claim `verified` có ít nhất một nguồn phù hợp; claim trọng yếu nên có hai nguồn độc lập khi khả thi.
5. Claim `disputed` có bằng chứng hoặc nguồn cho các phía bất đồng.
6. Thesis chỉ liên kết tới claim đã audit.
7. Mọi chart có source, unit, period, transformation, status và fallback table.
8. Mọi số liệu có `dataType`; simulation/scenario/heuristic phải gắn nhãn.
9. Các KPI cấp atlas khớp số lượng thực tế.
10. Không dùng từ `probability` hoặc `% chance` cho heuristic score.
11. `planned`, `published`, `reviewed` không bị gộp.
12. Global search index bao phủ title, question, claim, term và source.

Chạy:

```bash
python "$SKILL_DIR/scripts/qa_research_atlas.py" ./research-project/atlas
```

## 9. Hard fail riêng cho Atlas

Không publish nếu:

- Broken reference hoặc duplicate ID.
- Claim verified không có nguồn.
- KPI thủ công mâu thuẫn với dữ liệu.
- Dùng heuristic score như xác suất.
- Không phân biệt planned/published/reviewed.
- Không phân biệt observed/derived/simulation/scenario.
- Nội dung trùng lặp giữa module thay vì liên kết entity.
- Question Router dẫn tới đường đọc không tồn tại.
- Pathway thiếu ít nhất một trong các lớp mechanism, behavior/exposure và damage/outcome.
- Atlas không có manifest hoặc schema version.

## 10. Nguyên tắc mở rộng

- Thêm module mới không được yêu cầu sửa schema cũ nếu không có migration version.
- ID ổn định qua các phiên bản; đổi tiêu đề không đổi ID.
- Mọi thay đổi rules table phải tăng `modelVersion`.
- Mọi thay đổi schema phải tăng `schemaVersion` và ghi migration note.
- Source trùng giữa các module dùng cùng một `sourceId`.
- Claim trùng phải hợp nhất hoặc ghi quan hệ `supports`, `qualifies`, `contradicts`.
- HTML là view; JSON/CSV đã audit là source of truth.
