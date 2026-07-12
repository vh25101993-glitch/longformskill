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

## Pattern kế thừa từ các báo cáo mẫu

- Báo cáo lịch sử tài sản: regime map, CAGR/YoY, spread/premium, benchmark, uncertainty.
- Báo cáo policy trước/sau: glossary, timeline, breakpoint, before-after matrix, evidence chain, đính chính thuật ngữ.
- Báo cáo cross-country: phase classification, comparability, Data Quality, exceptions, target-country roadmap.
- Longform gốc: two-axis fact/academic checking, dark HTML, minimap, charts, citations và Playwright QA.

Đây là clean-room workflow: học từ cấu trúc đầu ra và phương pháp nghiên cứu phổ quát, không sao chép hidden prompt hoặc source code độc quyền.
