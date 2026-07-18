# Audit, Quality Rubric and Templates

## Citation audit

Mỗi claim trọng yếu phải vượt qua 5 câu hỏi:

1. Citation có tồn tại và truy cập được không?
2. Nguồn có thực sự entail claim không?
3. Entity, metric, unit, geography và period có khớp không?
4. Claim có bỏ qua caveat quan trọng của nguồn không?
5. Có nguồn đối nghịch hoặc revision mới hơn không?

Claim audit dùng trạng thái `Verified`, `Needs revision`, `Rejected`.

## Quality rubric — 100 điểm

| Hạng mục | Điểm |
|---|---:|
| Research specification & coverage | 10 |
| Source quality & provenance | 15 |
| Data quality & comparability | 15 |
| Analysis & causal discipline | 15 |
| Citation entailment | 15 |
| Editorial structure & coherence | 10 |
| Charts/tables & dataset consistency | 10 |
| Recommendations, risks & uncertainty | 5 |
| Technical/visual QA | 5 |

Chỉ publish khi tổng điểm ≥85 và không có hard fail.

Đối với profile `industry-market`, phần Data quality & comparability chỉ được chấm tối đa nếu có market-size reconciliation, data-vintage audit và taxonomy bridge.

## Hard fail

- Claim trọng yếu không có provenance.
- Nội suy/estimate/forecast không gắn nhãn.
- Text, table và chart dùng số khác nhau.
- Trộn đơn vị, định nghĩa hoặc kỳ dữ liệu.
- Dùng causal language khi chỉ có correlation.
- Attribution định lượng không có phương pháp.
- Citation không hỗ trợ claim.
- Dùng dữ liệu cũ như dữ liệu hiện tại.
- Raw placeholder, JS error, chart trống, clipping/overflow.
- Recommendation mạnh hơn evidence.
- Lộ prompt/hướng dẫn nội bộ.

### Hard fail bổ sung cho industry-market

- Đặt valuation/funding/M&A vào sai năm hoặc sai loại giao dịch.
- Dùng funding round size như cumulative capital raised hoặc ngược lại.
- Xếp minority/strategic investment vào M&A khi không có giao dịch mua lại.
- Dùng một tổng thị trường rồi phân bổ các lớp từ nguồn khác taxonomy mà không có reconciliation bridge.
- Tổng lớp con không khớp lớp cha ngoài sai số làm tròn mà không giải thích.
- Một vertical/technology segment lớn hơn parent category nhưng vẫn trình bày như cấu trúc cộng dồn.
- Trộn revenue, spend, investment, capex, transaction value và valuation trong cùng tổng hoặc chart so sánh mà không cảnh báo.
- Gắn số liệu xảy ra năm `t+1` vào cột năm `t`.
- Báo cáo phát hành sau khi năm dữ liệu đã kết thúc nhưng vẫn dùng estimate nửa năm mà không giải thích vì sao chưa thay bằng actual.
- Cover, footer, version hoặc câu hẹn cập nhật mâu thuẫn về thời gian.
- Công bố uncertainty band hoặc tỷ lệ ngân sách khuyến nghị mà không có cơ sở phương pháp/benchmark.

## Recommendation matrix

```csv
recommendation_id,recommendation,target,priority,evidence_claim_ids,mechanism,expected_impact,risks_tradeoffs,owner,horizon,kpi_validation,trigger_to_revise
```

## Chart manifest

```csv
chart_id,title,analytical_question,chart_type,metrics,unit,geography,period,frequency,source_ids,transformations,data_status,interpretation,limitations,fallback_table
```

## Claim audit

```csv
claim_id,citation_present,source_entails_claim,unit_period_match,cross_checked,contradiction_resolved,final_status,auditor_note
```

## Data dictionary

```csv
variable,definition,unit,frequency,geography,source_id,transformation,base_year,actual_or_estimated,comparability_notes
```

## Evidence ledger

```csv
claim_id,section,claim_text,claim_class,importance,metric,value,unit,geography,period,frequency,source_id,source_location,source_type,data_status,formula,input_claim_ids,comparability,confidence,contradiction,alternative_explanations,notes,audit_status
```

## Research plan and registers

```csv
question_id,research_question,query_local_language,query_english,preferred_domains,source_type,expected_metric_or_document,status,gap
```

```csv
source_id,title,publisher,url,publication_date,access_date,source_tier,geography,coverage_period,methodology_url,paywall,notes
```

```csv
risk_id,issue,affected_claims_or_charts,type,likelihood,impact,mitigation,disclosure_text,status
```

## Market-size reconciliation

```csv
estimate_id,metric_name,value,unit,reference_year,forecast_year,publisher,publication_date,scope_definition,included_layers,excluded_layers,geography,methodology,actual_or_forecast,overlap_risk,comparability_group,confidence,notes
```

## Company-event register

```csv
event_id,company,event_type,event_date,announcement_date,deal_status,value,unit,pre_or_post_money,primary_or_secondary,cumulative_or_incremental,source_id,source_location,as_of_date,notes
```

`event_type` dùng enum gợi ý: `public_market_cap`, `private_valuation`, `funding_round`, `cumulative_funding`, `strategic_investment`, `m_and_a`, `capex_commitment`, `revenue`, `run_rate_revenue`.

## Taxonomy bridge

```csv
parent_metric,parent_value,parent_unit,child_metric,child_value,child_unit,axis,value_chain_or_technology_or_deployment_or_vertical_or_geography,mutually_exclusive,overlap_adjustment,reconciled_value,source_ids,notes
```

## Data-vintage audit

```csv
item_id,metric_or_event,reference_period,publication_date,access_date,as_of_date,actual_or_estimate,fiscal_or_calendar,revision_checked,label_in_output,pass_fail,note
```

## Paper outline

```markdown
# Executive Summary
## 1. Scope & Definitions
## 2. Methodology & Data Quality
## 3. Historical/Institutional Context
## 4. Core Performance
## 5. Comparisons
## 6. Attribution & Diagnosis
## 7. Alternative Explanations
## 8. Findings
## 9. Recommendations & Action Plan
## 10. Uncertainty & Limitations
## Evidence & Sources
## Appendix & Data Dictionary
```

## Industry-market paper outline

```markdown
# Executive Snapshot
## 1. Scope, Definitions & Taxonomy
## 2. Data Quality, Vintage & Market-Size Reconciliation
## 3. Market Size, Growth & Forecast Range
## 4. Value Chain & Layer Economics
## 5. Technology Segmentation
## 6. Deployment Model
## 7. Buyer Verticals & Use Cases
## 8. Geography & Industrial Clusters
## 9. Competitive Landscape & Company Map
## 10. Funding, M&A, Capex & Adoption
## 11. Bottlenecks, Profit Pools & Bargaining Power
## 12. Alternative Explanations
## 13. Scenarios & Triggers
## 14. Stakeholder Action Matrix
## 15. Uncertainty & Limitations
## Evidence & Sources
## Appendix, Data Dictionary & Reconciliation Tables
```

## Pattern kế thừa từ các báo cáo mẫu

- Báo cáo lịch sử tài sản: regime map, CAGR/YoY, spread/premium, benchmark, uncertainty.
- Báo cáo policy trước/sau: glossary, timeline, breakpoint, before-after matrix, evidence chain, đính chính thuật ngữ.
- Báo cáo cross-country: phase classification, comparability, Data Quality, exceptions, target-country roadmap.
- Báo cáo industry-market: cover/TOC rõ, executive snapshot, phân khúc đa trục, value-chain map, company landscape, funding/adoption, stakeholder action matrix và uncertainty section.
- Longform gốc: two-axis fact/academic checking, dark HTML, minimap, charts, citations và Playwright QA.

Không kế thừa các lỗi benchmark như false precision, kỳ dữ liệu sai, taxonomy giao cắt nhưng cộng dồn, hoặc tuyên bố cross-check mà không có claim-level provenance.

Đây là clean-room workflow: học từ cấu trúc đầu ra và phương pháp nghiên cứu phổ quát, không sao chép hidden prompt hoặc source code độc quyền.
