#!/usr/bin/env python3
"""Create a research project scaffold for the Longform desk-research workflow."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

PROFILES = {
    "asset-history",
    "policy-before-after",
    "cross-country-development",
    "industry-market",
    "document-consensus",
    "knowledge-atlas",
    "custom",
}

FILES = {
    "research_plan.csv": "question_id,research_question,query_local_language,query_english,preferred_domains,source_type,expected_metric_or_document,status,gap\n",
    "source_register.csv": "source_id,title,publisher,url,publication_date,access_date,source_tier,geography,coverage_period,methodology_url,paywall,notes\n",
    "evidence_ledger.csv": "claim_id,section,claim_text,claim_class,importance,metric,value,unit,geography,period,frequency,source_id,source_location,source_type,data_status,formula,input_claim_ids,comparability,confidence,contradiction,alternative_explanations,notes,audit_status\n",
    "data_dictionary.csv": "variable,definition,unit,frequency,geography,source_id,transformation,base_year,actual_or_estimated,comparability_notes\n",
    "chart_manifest.csv": "chart_id,title,analytical_question,chart_type,metrics,unit,geography,period,frequency,source_ids,transformations,data_status,interpretation,limitations,fallback_table\n",
    "claim_audit.csv": "claim_id,citation_present,source_entails_claim,unit_period_match,cross_checked,contradiction_resolved,final_status,auditor_note\n",
    "recommendation_matrix.csv": "recommendation_id,recommendation,target,priority,evidence_claim_ids,mechanism,expected_impact,risks_tradeoffs,owner,horizon,kpi_validation,trigger_to_revise\n",
    "uncertainty_register.csv": "risk_id,issue,affected_claims_or_charts,type,likelihood,impact,mitigation,disclosure_text,status\n",
}

ATLAS_ENTITY_FILES = {
    "modules": "modules.json",
    "chapters": "chapters.json",
    "claims": "claims.json",
    "sources": "sources.json",
    "questions": "questions.json",
    "misconceptions": "misconceptions.json",
    "pathways": "pathways.json",
    "theses": "theses.json",
    "glossary": "glossary.json",
    "cases": "cases.json",
    "interaction_rules": "interaction_rules.json",
}


def write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def create_atlas_scaffold(out: Path, topic: str) -> None:
    atlas = out / "atlas"
    atlas.mkdir(parents=True, exist_ok=True)

    for label, filename in ATLAS_ENTITY_FILES.items():
        write_json(atlas / filename, {label: []})

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    write_json(
        atlas / "atlas_manifest.json",
        {
            "schemaVersion": "1.0.0",
            "atlasVersion": "0.1.0",
            "title": topic,
            "generatedAt": generated_at,
            "counts": {label: 0 for label in ATLAS_ENTITY_FILES},
            "files": ATLAS_ENTITY_FILES,
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--profile", required=True, choices=sorted(PROFILES))
    parser.add_argument("--out", required=True)
    parser.add_argument(
        "--atlas",
        action="store_true",
        help="Create the atlas JSON package. Enabled automatically for knowledge-atlas.",
    )
    args = parser.parse_args()

    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)

    for name, header in FILES.items():
        (out / name).write_text(header, encoding="utf-8")

    atlas_enabled = args.atlas or args.profile == "knowledge-atlas"
    atlas_note = "enabled" if atlas_enabled else "disabled"
    (out / "research_brief.md").write_text(
        "# Research Brief\n\n"
        f"## Topic\n\n{args.topic}\n\n"
        f"## Profile\n\n{args.profile}\n\n"
        f"## Research Atlas\n\n{atlas_note}\n\n"
        "## Central question\n\n"
        "## Sub-questions\n\n"
        "## Scope and definitions\n\n"
        "## Completion criteria\n",
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

    if atlas_enabled:
        create_atlas_scaffold(out, args.topic)

    print(f"Created research scaffold: {out}")
    if atlas_enabled:
        print(f"Created Research Atlas scaffold: {out / 'atlas'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
