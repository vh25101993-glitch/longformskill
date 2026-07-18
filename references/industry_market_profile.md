# Industry-Market Profile

## Mục tiêu

Profile `industry-market` dùng để lập bản đồ một ngành theo cả hai góc nhìn:

1. **Industrial system:** tài nguyên, hạ tầng, công nghệ, năng lực sản xuất, chuỗi cung ứng và quyền kiểm soát.
2. **Commercial market:** quy mô doanh thu/chi tiêu, phân khúc khách hàng, cạnh tranh, vốn, adoption và profit pool.

Một báo cáo tốt phải trả lời đồng thời:

- Ngành gồm những lớp nào?
- Ai kiểm soát từng lớp và tại sao?
- Quy mô nào đang được đo: revenue, spend, investment hay economic impact?
- Giá trị và lợi nhuận tập trung ở đâu?
- Nút thắt nào có thể dịch chuyển theo thời gian?
- Người mua nào tạo cầu thực tế và ROI?
- Rủi ro nào có thể làm sai dự báo?

## Research questions tối thiểu

1. Taxonomy nào mô tả ngành mà không double count?
2. Market-size estimate nào thực sự so sánh được?
3. Value chain gồm bao nhiêu lớp, economics của mỗi lớp là gì?
4. Technology, deployment và vertical segmentation khác nhau thế nào?
5. Quốc gia/khu vực nào kiểm soát nghiên cứu, thiết kế, sản xuất, vốn, phân phối và quy định?
6. Top company cạnh tranh bằng asset/moat nào?
7. Dòng vốn, capex, M&A và adoption đang ở giai đoạn nào?
8. Bottleneck và profit pool hiện tại là gì; có thể dịch chuyển sang đâu?
9. Bear/Base/Bull hoặc các scenario chiến lược là gì?
10. Hàm ý khác nhau cho doanh nghiệp, nhà đầu tư và chính sách là gì?

## Output package

```text
research_brief.md
source_register.csv
evidence_ledger.csv
data_dictionary.csv
market_size_reconciliation.csv
taxonomy_bridge.csv
company_event_register.csv
data_vintage_audit.csv
chart_manifest.csv
claim_audit.csv
uncertainty_register.csv
paper.md và/hoặc index.html
qa_report.md
```

## Cấu trúc báo cáo

### 1. Cover/meta

Ghi rõ:

- title/subtitle;
- reference period;
- as-of date;
- geography;
- profile;
- output version;
- nguồn chủ đạo;
- disclaimer.

Cover, footer, version và copyright không được mâu thuẫn thời gian.

### 2. Executive snapshot

Dùng 5-7 phát hiện định lượng và 3-5 caveat. Nên có:

- market-size range;
- growth/adoption;
- top bottleneck;
- top profit pool;
- concentration/geographic dependency;
- scenario signal;
- target-country implication khi có.

Mỗi phát hiện phải map tới claim ID.

### 3. Scope, definitions và taxonomy

Định nghĩa rõ:

- ngành được tính từ đâu đến đâu;
- loại dòng tiền được đo;
- lớp bị loại trừ;
- technology/deployment/vertical/geography có giao cắt hay loại trừ nhau;
- fiscal/calendar year;
- actual/estimate/forecast.

### 4. Data Quality và market-size reconciliation

Công bố:

- source hierarchy;
- độ phủ thời gian/địa lý/phân khúc;
- data lag;
- actual vs estimate;
- taxonomy disagreement;
- overlap risk;
- reconciliation range;
- claim bị loại vì không đủ bằng chứng.

Không dùng câu “đã đối chiếu hai nguồn” nếu evidence ledger không cho thấy hai source IDs.

### 5. Market size, growth và forecast

- Trình bày range giữa các estimate so sánh được.
- Ghi CAGR formula và endpoint.
- Forecast có base/upside/downside hoặc confidence range có cơ sở.
- Không coi forecast vendor là FACT.
- Tách current market revenue khỏi long-run economic impact.

### 6. Value chain và layer economics

Mỗi layer có:

- inputs/outputs;
- representative companies;
- revenue model;
- gross margin/capital intensity nếu có;
- concentration;
- switching cost;
- bargaining power;
- dependencies;
- bottleneck;
- data confidence.

### 7. Segmentation đa trục

#### Technology

Ví dụ: traditional ML, GenAI, vision, NLP, robotics. Thường giao cắt; không cộng máy móc.

#### Deployment

Ví dụ: public cloud, private/on-prem, edge. Chỉ cộng khi nhóm loại trừ nhau trong nguồn.

#### Buyer/vertical

Ví dụ: finance, health, retail, manufacturing. Ghi rõ đây là spend/revenue/use-case adoption gì.

#### Geography

Tách nghiên cứu, thiết kế, sản xuất, vốn, data center, application demand và regulation.

### 8. Competitive landscape

Không chỉ xếp hạng theo valuation. Dùng company map với:

- layer;
- customer;
- product;
- proprietary asset;
- distribution;
- monetization;
- capital requirement;
- key dependency;
- regulatory exposure;
- moat durability;
- failure mode.

### 9. Funding, M&A, capex và adoption

Tách bốn loại dữ liệu:

- funding/private investment;
- strategic investment;
- M&A;
- internal capex.

Adoption phải ghi sample, survey population, geography, question wording và mức độ triển khai. “Có sử dụng AI” không đồng nghĩa production deployment hoặc positive ROI.

### 10. Bottlenecks và profit pools

Dùng framework:

```text
Pricing power ≈ scarcity × switching cost × capital barrier × utilization × control of distribution
```

Đây là khung phân tích, không phải công thức thống kê. Nếu chấm điểm, công bố weights, scale, evidence và sensitivity.

### 11. Alternative explanations

Tối thiểu phản biện:

- capex boom có thể đi trước demand;
- market-size growth có thể do taxonomy mở rộng;
- adoption survey có thể đo thử nghiệm thay vì ROI;
- model performance có thể commoditize;
- regulatory/geopolitical changes có thể đổi chuỗi cung ứng;
- company valuation không chứng minh sustainable profit.

### 12. Scenarios

Mỗi scenario có:

- assumptions;
- horizon;
- pathway;
- leading indicators;
- trigger;
- invalidation condition;
- winners/losers;
- confidence.

Không gán probability chính xác nếu không có cơ sở.

### 13. Stakeholder action matrix

#### Enterprise/C-suite

Ưu tiên use case, data readiness, architecture, vendor concentration, governance và ROI measurement.

#### Investor/capital allocator

Tập trung unit economics, capex intensity, valuation basis, bottleneck durability, cyclicality và downside trigger. Không biến report ngành thành khuyến nghị mua/bán cá nhân hóa.

#### Policy maker

Tập trung capability gap, infrastructure, talent, standards, competition, security và target-country comparative advantage.

Mỗi action có owner, horizon, KPI, risk và trigger to revise.

## Visual system

### Paper/PDF

- cover;
- TOC;
- page number;
- figure/table numbering;
- source note dưới chart;
- appendix;
- tránh trang gần như trống trừ khi chủ ý phân chương.

### HTML

- hero/meta;
- KPI cards;
- fixed nav + progress + minimap;
- responsive tables;
- interactive charts chỉ khi có mô hình hợp lệ;
- print/PDF mode;
- fallback table;
- không horizontal overflow ở 390/768/desktop.

## Benchmark lessons incorporated

Các pattern hữu ích được giữ lại:

- cover và mục lục rõ như một research paper;
- executive summary có hộp phát hiện chính;
- phân khúc theo value chain, technology, deployment, vertical và geography;
- phần riêng về funding/M&A/adoption;
- recommendation tách theo stakeholder;
- uncertainty section và next verification steps;
- mật độ chart/table đủ để người đọc kiểm tra narrative.

Các lỗi không được kế thừa:

- dữ liệu năm sau đặt trong cột năm trước;
- estimate cũ không thay bằng actual dù báo cáo đã cập nhật;
- market size và layer total không reconcile;
- vertical market lớn hơn parent layer nhưng không giải thích taxonomy;
- strategic investment bị gọi là M&A;
- funding round bị gọi là cumulative funding;
- uncertainty band và budget ratio tự đặt;
- nguồn chỉ liệt kê cuối báo cáo nhưng không map claim-level;
- tiêu đề/phiên bản/câu hẹn cập nhật mâu thuẫn về thời gian.

## Completion gate

Profile chỉ đạt `PASS` khi:

- 3 map bắt buộc hoàn thành;
- market-size reconciliation hoàn thành;
- data-vintage audit không có hard fail;
- company-event register phân loại đúng;
- chart/text/table dùng cùng dataset;
- recommendation có evidence IDs;
- uncertainty và alternative explanations được công bố;
- paper/HTML qua visual QA.
