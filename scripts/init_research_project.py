#!/usr/bin/env python3
"""Create a research project scaffold for the Longform desk-research workflow."""
from __future__ import annotations

import argparse
from pathlib import Path

PROFILES = {
    "asset-history",
    "policy-before-after",
    "cross-country-development",
    "industry-market",
    "document-consensus",
    "custom",
}

FILES = {
    "research_plan.csv": (
        "question_id,research_question,query_local_language,query_english,"
        "preferred_domains,source_type,expected_metric_or_document,status,gap\n"
    ),
    "source_register.csv": (
        "source_id,title,publisher,url,publication_date,access_date,source_tier,"
        "geography,coverage_period,methodology_url,paywall,notes\n"
    ),
    "evidence_ledger.csv": (
        "claim_id,chapter_id,section,claim_text,claim_class,epistemic_status,"
        "content_role,importance,metric,value,unit,geography,period,frequency,"
        "source_id,source_location,source_type,data_status,formula,input_claim_ids,"
        "related_claim_ids,comparability,confidence,contradiction,"
        "alternative_explanations,notes,audit_status\n"
    ),
    "data_dictionary.csv": (
        "variable,definition,unit,frequency,geography,source_id,transformation,"
        "base_year,actual_or_estimated,comparability_notes\n"
    ),
    "chart_manifest.csv": (
        "chart_id,chapter_id,title,analytical_question,chart_type,visual_role,"
        "metrics,unit,geography,period,frequency,source_ids,claim_ids,"
        "transformations,data_status,interactive,input_parameters,baseline,"
        "formula_model_version,output_metrics,preset_definitions,"
        "assumptions_held_constant,expected_direction,interpretation,"
        "limitations,fallback_table\n"
    ),
    "claim_audit.csv": (
        "claim_id,citation_present,source_entails_claim,unit_period_match,"
        "cross_checked,contradiction_resolved,epistemic_status_valid,"
        "graph_relations_valid,final_status,auditor_note\n"
    ),
    "recommendation_matrix.csv": (
        "recommendation_id,recommendation,target,priority,evidence_claim_ids,"
        "mechanism,expected_impact,risks_tradeoffs,owner,horizon,kpi_validation,"
        "trigger_to_revise\n"
    ),
    "uncertainty_register.csv": (
        "risk_id,issue,affected_claims_or_charts,type,likelihood,impact,"
        "mitigation,disclosure_text,status\n"
    ),
    "chapter_schema.csv": (
        "chapter_id,chapter_number,title,guiding_question,provisional_thesis,"
        "section_ids,claim_ids,centerpiece_visual_id,counterpoint_id,"
        "related_chapter_ids,mini_conclusion,takeaway,reader_summary,"
        "research_disclosure,default_mode,status\n"
    ),
    "claim_graph.csv": (
        "edge_id,from_claim_id,relation,to_claim_id,rationale,source_ids,status\n"
    ),
    "counterpoints.csv": (
        "counterpoint_id,chapter_id,question,position_a_label,"
        "position_a_claim_ids,position_b_label,position_b_claim_ids,synthesis,"
        "epistemic_status,conditions_to_revise\n"
    ),
    "narrative_manifest.csv": (
        "visual_id,chapter_id,title,narrative_question,visual_type,layout,"
        "centerpiece,step_ids,claim_ids,source_ids,data_mode,reader_summary,"
        "research_disclosure,fallback_table,keyboard_support,reduced_motion,"
        "print_fallback,limitations\n"
    ),
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--profile", required=True, choices=sorted(PROFILES))
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    for name, header in FILES.items():
        (out / name).write_text(header, encoding="utf-8")

    (out / "research_brief.md").write_text(
        (
            "# Research Brief\n\n"
            f"## Topic\n\n{args.topic}\n\n"
            f"## Profile\n\n{args.profile}\n\n"
            "## Central question\n\n"
            "## Sub-questions\n\n"
            "## Scope and definitions\n\n"
            "## Unit of analysis, variables and formulas\n\n"
            "## Breakpoints and rationale\n\n"
            "## Source hierarchy and stopping rule\n\n"
            "## Chapter architecture\n\n"
            "## Publication mode\n\n"
            "Default: `reader-with-research-toggle`\n\n"
            "## Narrative centerpiece criteria\n\n"
            "## Completion criteria\n"
        ),
        encoding="utf-8",
    )
    (out / "paper.md").write_text(
        f"# {args.topic}\n\n> Profile: `{args.profile}`\n",
        encoding="utf-8",
    )
    (out / "qa_report.md").write_text(
        "# QA Report\n\nStatus: NOT RUN\n",
        encoding="utf-8",
    )

    print(f"Created research scaffold: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
