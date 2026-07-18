# Analysis, Causality and Report Architecture

## Thang sức mạnh bằng chứng

1. Descriptive coincidence
2. Temporal ordering
3. Mechanism evidence
4. Cross-sectional/time-series consistency
5. Natural experiment/event study
6. Econometric identification
7. Replicated evidence

Ngôn ngữ phải tương ứng: levels 1-2 dùng “đồng thời/liên quan/phù hợp với giả thuyết”; levels 3-4 dùng “có khả năng/bằng chứng hỗ trợ”; levels 5-7 mới có thể dùng “tác động”, đồng thời nêu phương pháp và giới hạn.

## Evidence chain

`Policy/cause -> transmission channel -> intermediate indicator -> outcome -> side effect`

Mỗi mũi tên cần claim IDs riêng. Không nối chuỗi chỉ bằng narrative.

## Alternative explanations

Mỗi claim causal quan trọng phải có 1-3 alternative explanations và cách phân biệt bằng timing, comparison, control variable, event window, source-specific evidence hoặc sensitivity test.

## Quantified attribution

Chỉ cho phép khi có regression/decomposition, accounting identity, Shapley/variance decomposition, transparent expert scoring kèm weights/sensitivity, hoặc nguồn ngoài công bố phương pháp. Không viết “A đóng góp 40-45%” từ trực giác.

## Scenario analysis

Mỗi scenario có assumptions, trigger, horizon, pathway, variables affected, probability band nếu có căn cứ và invalidation condition. Không trộn scenario với forecast point estimate.

# Report architecture

## Module chung

1. Cover/meta
2. Executive Summary
3. Research Objective
4. Scope & Definitions
5. Methodology
6. Dataset/Data Quality
7. Historical/Institutional Context
8. Core Performance
9. Comparisons
10. Attribution & Diagnosis
11. Alternative Explanations
12. Scenarios
13. Findings
14. Recommendations & Action Plan
15. Uncertainty & Limitations
16. Evidence & Sources
17. Appendix/Data Dictionary

## Profile: asset-history

Bắt buộc đánh giá total return, CAGR, YoY, drawdown, volatility, endpoint sensitivity, FX, inflation, premium/spread, transaction cost, regime và benchmark.

## Profile: policy-before-after

Bắt buộc xác minh breakpoint, so sánh công cụ trước/sau, transmission channel, outcomes, side effects, alternative explanations và counterfactual.

## Profile: cross-country-development

Bắt buộc công bố phase criteria, comparability matrix, thay đổi chỉ tiêu theo thu nhập, trường hợp ngoại lệ và vị trí của target country.

## Profile: industry-market

Profile này phải kết hợp **bản đồ công nghiệp** và **market research**, không chỉ kể tên doanh nghiệp hoặc trình bày một TAM duy nhất.

### Kiến trúc mặc định

1. Cover/meta và as-of date
2. Executive snapshot: 5-7 phát hiện định lượng, 3-5 caveat, market-map thumbnail
3. Scope, taxonomy và định nghĩa chỉ tiêu
4. Data Quality, data vintage và market-size reconciliation
5. Market size, growth và forecast range
6. Value chain: layer, economics, margin structure, capital intensity, concentration
7. Technology segmentation
8. Deployment model: cloud/private/edge hoặc taxonomy phù hợp
9. Buyer/vertical segmentation và use cases
10. Geography, industrial clusters và dependencies
11. Competitive landscape và company strategy map
12. Funding, M&A, capex và adoption
13. Bottlenecks, profit pools, switching costs và bargaining power
14. Alternative explanations và anti-thesis
15. Scenarios, triggers và invalidation conditions
16. Stakeholder action matrix
17. Uncertainty, source register và appendix

### Ba bản đồ bắt buộc

1. **Value-chain map:** tài nguyên đầu vào -> hạ tầng -> nền tảng -> phân phối -> ứng dụng/dịch vụ.
2. **Geographic-control map:** nơi nghiên cứu, thiết kế, sản xuất, vốn, triển khai và kiểm soát pháp lý.
3. **Demand map:** buyer, use case, deployment model, willingness-to-pay, adoption và rào cản.

Không được dùng một trục thay cho trục khác. Một quốc gia dẫn đầu nghiên cứu không tự động dẫn đầu sản xuất hoặc thương mại hóa; một vertical market không phải là một lớp cộng dồn của value chain nếu taxonomy giao cắt.

### Market-size discipline

- Tách rõ market revenue, enterprise spend, private investment, corporate investment, capex, M&A và valuation.
- Dùng range hoặc nhóm estimate so sánh được; không hòa trộn vendor forecast khác taxonomy thành một con số chính xác giả.
- Nếu tổng các lớp bằng TAM, phải có bridge và quy tắc loại trùng.
- Nếu một segment lớn hơn parent category, giải thích giao cắt taxonomy hoặc sửa dữ liệu.
- Mọi forecast có source vintage, methodology và confidence.

### Competition and company map

Mỗi công ty nên được mô tả theo các trường: layer, product, buyer, distribution, proprietary asset, dependence, capital intensity, monetization, switching cost, regulatory exposure và key risk.

Bảng valuation/funding phải tách event date, post-money/pre-money, round size, cumulative funding, public market cap và strategic commitment. Không xếp strategic investment vào M&A.

### Stakeholder action matrix

Tối thiểu tách ba nhóm khi phù hợp:

- doanh nghiệp/C-suite;
- nhà đầu tư hoặc capital allocator;
- nhà hoạch định chính sách/định chế công.

Mỗi hành động có target, evidence IDs, owner, horizon, KPI, trade-off và trigger to revise. Không đưa tỷ lệ ngân sách cứng nếu không có benchmark phù hợp theo ngành và quy mô.

### Visual package tối thiểu

- 1 value-chain map;
- 1 market-size/growth chart có forecast shading;
- 1 segmentation chart;
- 1 geography chart/map;
- 1 competition/company map;
- 1 funding/adoption chart;
- 1 bottleneck/profit-pool chart;
- 1 scenario chart hoặc discrete scenario matrix;
- bảng fallback cho mọi chart.

Với paper/PDF dài, ưu tiên cover, mục lục, header/footer, page number, figure/table numbering và source note. Với HTML, giữ navigation/minimap/progress và responsive layout.

Xem `references/industry_market_profile.md` và `references/desk_research_02_data.md`.

## Profile: document-consensus

Document map → Consensus matrix → Disagreement matrix → Forecast comparison → Assumption audit → Data vintage → Implications/Risks.

# Editorial style

Mỗi chương phải trả lời một câu hỏi rõ, dùng cấu trúc: câu hỏi dẫn → evidence → interpretation → counter-evidence → mini-conclusion → risk of interpretation.

- Không dùng tiêu đề chung chung như “Phân tích sâu”.
- Không lặp cùng một con số ở nhiều chương nếu không có mục đích.
- Executive Summary chỉ chứa kết luận đã được chứng minh trong thân bài.
- Executive Summary của profile `industry-market` nên có hộp 5 phát hiện chính, nhưng mỗi phát hiện phải map đến claim ID và caveat.
- Recommendation phải gắn evidence IDs, owner, horizon, KPI và revision trigger.
- Bản cuối không để lộ prompt, placeholder hoặc hướng dẫn nội bộ.
