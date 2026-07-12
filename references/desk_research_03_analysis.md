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

Executive Summary → Scope/taxonomy → Data Quality → Market size/growth → Structure/competition → Economics → Drivers → Risks/scenarios → Implications.

## Profile: document-consensus

Document map → Consensus matrix → Disagreement matrix → Forecast comparison → Assumption audit → Data vintage → Implications/Risks.

# Editorial style

Mỗi chương phải trả lời một câu hỏi rõ, dùng cấu trúc: câu hỏi dẫn → evidence → interpretation → counter-evidence → mini-conclusion → risk of interpretation.

- Không dùng tiêu đề chung chung như “Phân tích sâu”.
- Không lặp cùng một con số ở nhiều chương nếu không có mục đích.
- Executive Summary chỉ chứa kết luận đã được chứng minh trong thân bài.
- Recommendation phải gắn evidence IDs, owner, horizon, KPI và revision trigger.
- Bản cuối không để lộ prompt, placeholder hoặc hướng dẫn nội bộ.
