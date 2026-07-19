#!/usr/bin/env python3
"""Validate Longform desk-research files, evidence integrity and publication graph."""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

REQUIRED = [
    "research_brief.md",
    "research_plan.csv",
    "source_register.csv",
    "evidence_ledger.csv",
    "data_dictionary.csv",
    "chart_manifest.csv",
    "claim_audit.csv",
    "uncertainty_register.csv",
    "chapter_schema.csv",
    "claim_graph.csv",
    "counterpoints.csv",
    "narrative_manifest.csv",
    "recommendation_matrix.csv",
    "paper.md",
]

TOKEN = re.compile(r"\{\{[A-Z0-9_]+\}\}")
VAGUE = re.compile(r"\b(nguồn tổng hợp|nhiều nguồn|theo nghiên cứu)\b", re.I)

CLAIM_CLASSES = {"FACT", "DERIVED", "INFERENCE", "SCENARIO", "RECOMMENDATION"}
EPISTEMIC_STATUSES = {
    "VERIFIED",
    "QUALIFIED",
    "DISPUTED",
    "AUTHOR_VIEW",
    "INSUFFICIENT_EVIDENCE",
}
CONTENT_ROLES = {
    "THESIS",
    "MECHANISM",
    "MILESTONE",
    "EVIDENCE",
    "COUNTERPOINT",
    "CAVEAT",
    "TAKEAWAY",
}
GRAPH_RELATIONS = {
    "SUPPORTS",
    "CONTRADICTS",
    "QUALIFIES",
    "DERIVED_FROM",
    "EXPLAINS",
    "APPLIES_TO",
    "REFERENCES",
    "SYNTHESIZES",
    "SUPERSEDES",
}
CHAPTER_MODES = {"reader", "research", "reader-with-research-toggle"}
CHAPTER_STATUSES = {"DRAFT", "AUDITED", "PUBLISHED"}
COUNTERPOINT_STATUSES = {"QUALIFIED", "DISPUTED"}
VISUAL_TYPES = {
    "TIMELINE",
    "MECHANISM_STEPPER",
    "POLICY_CASCADE",
    "CAUSE_EFFECT_NETWORK",
    "SCENARIO_PATH",
    "BEFORE_AFTER",
    "CHART",
}
VISUAL_LAYOUTS = {"STATIC", "STICKY_SCROLL", "STEPPER", "DASHBOARD", "SCENARIO_LAB"}
DATA_MODES = {
    "VERIFIED_DATA",
    "ILLUSTRATIVE_MECHANISM",
    "MIXED_WITH_DISCLOSURE",
}


def rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def yes(value: str) -> bool:
    return str(value).strip().lower() in {"yes", "true", "1", "y", "có", "co"}


def values(value: str) -> list[str]:
    """Parse semicolon, pipe or whitespace separated ID lists."""
    text = str(value or "").strip()
    if not text:
        return []
    return [part.strip() for part in re.split(r"[;|\s]+", text) if part.strip()]


def unique_id_rows(
    data: list[dict[str, str]],
    field: str,
    label: str,
    errors: list[str],
    warnings: list[str],
) -> set[str]:
    found: set[str] = set()
    for index, row in enumerate(data, 2):
        item_id = row.get(field, "").strip()
        if not item_id:
            warnings.append(f"{label} row {index}: missing {field}")
            continue
        if item_id in found:
            errors.append(f"Duplicate {label} ID: {item_id}")
        found.add(item_id)
    return found


def require(
    row: dict[str, str],
    fields: list[str],
    label: str,
    errors: list[str],
) -> None:
    for field in fields:
        if not row.get(field, "").strip():
            errors.append(f"{label}: missing {field}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project")
    args = parser.parse_args()

    root = Path(args.project).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    for name in REQUIRED:
        if not (root / name).exists():
            errors.append(f"Missing required file: {name}")

    if errors:
        for item in errors:
            print("ERROR:", item)
        return 2

    paper = (root / "paper.md").read_text(encoding="utf-8", errors="replace")
    if TOKEN.search(paper):
        errors.append("Raw placeholder found in paper.md")
    if VAGUE.search(paper):
        warnings.append("Vague source phrase found in paper.md")

    source_rows = rows(root / "source_register.csv")
    source_ids = unique_id_rows(
        source_rows, "source_id", "source", errors, warnings
    )

    chapter_rows = rows(root / "chapter_schema.csv")
    chapter_ids = unique_id_rows(
        chapter_rows, "chapter_id", "chapter", errors, warnings
    )

    claims = rows(root / "evidence_ledger.csv")
    claim_ids = unique_id_rows(
        claims, "claim_id", "claim", errors, warnings
    )

    for index, row in enumerate(claims, 2):
        claim_id = row.get("claim_id", "").strip()
        if not claim_id:
            continue

        claim_class = row.get("claim_class", "").strip().upper()
        epistemic = row.get("epistemic_status", "").strip().upper()
        content_role = row.get("content_role", "").strip().upper()
        source_id = row.get("source_id", "").strip()
        chapter_id = row.get("chapter_id", "").strip()

        if claim_class not in CLAIM_CLASSES:
            errors.append(f"{claim_id}: invalid claim_class {claim_class or '<blank>'}")
        if epistemic not in EPISTEMIC_STATUSES:
            errors.append(
                f"{claim_id}: invalid epistemic_status {epistemic or '<blank>'}"
            )
        if content_role not in CONTENT_ROLES:
            errors.append(
                f"{claim_id}: invalid content_role {content_role or '<blank>'}"
            )
        if chapter_id and chapter_id not in chapter_ids:
            errors.append(f"{claim_id}: unknown chapter_id {chapter_id}")
        if claim_class in {"FACT", "DERIVED"} and not source_id:
            errors.append(f"{claim_id}: {claim_class} missing source_id")
        if source_id and source_id not in source_ids:
            errors.append(f"{claim_id}: unknown source_id {source_id}")
        if claim_class == "DERIVED" and not row.get("formula", "").strip():
            errors.append(f"{claim_id}: DERIVED missing formula")
        if epistemic == "VERIFIED" and not source_id:
            errors.append(f"{claim_id}: VERIFIED missing source_id")
        if row.get("data_status", "").strip().lower() in {
            "interpolated",
            "estimated",
            "forecast",
        } and not row.get("notes", "").strip():
            warnings.append(f"{claim_id}: estimated data missing disclosure")

        for related in values(row.get("input_claim_ids", "")):
            if related not in claim_ids:
                errors.append(f"{claim_id}: unknown input_claim_id {related}")
        for related in values(row.get("related_claim_ids", "")):
            if related not in claim_ids:
                errors.append(f"{claim_id}: unknown related_claim_id {related}")

    graph_rows = rows(root / "claim_graph.csv")
    unique_id_rows(graph_rows, "edge_id", "claim graph edge", errors, warnings)

    for index, row in enumerate(graph_rows, 2):
        edge_id = row.get("edge_id", "").strip() or f"row {index}"
        from_claim = row.get("from_claim_id", "").strip()
        to_claim = row.get("to_claim_id", "").strip()
        relation = row.get("relation", "").strip().upper()
        require(
            row,
            ["from_claim_id", "relation", "to_claim_id", "rationale", "status"],
            f"Graph edge {edge_id}",
            errors,
        )
        if from_claim and from_claim not in claim_ids:
            errors.append(f"Graph edge {edge_id}: unknown from_claim_id {from_claim}")
        if to_claim and to_claim not in claim_ids:
            errors.append(f"Graph edge {edge_id}: unknown to_claim_id {to_claim}")
        if relation and relation not in GRAPH_RELATIONS:
            errors.append(f"Graph edge {edge_id}: invalid relation {relation}")
        if from_claim and to_claim and from_claim == to_claim:
            errors.append(f"Graph edge {edge_id}: self-reference is not allowed")
        for source_id in values(row.get("source_ids", "")):
            if source_id not in source_ids:
                errors.append(f"Graph edge {edge_id}: unknown source_id {source_id}")

    counterpoint_rows = rows(root / "counterpoints.csv")
    counterpoint_ids = unique_id_rows(
        counterpoint_rows,
        "counterpoint_id",
        "counterpoint",
        errors,
        warnings,
    )

    for index, row in enumerate(counterpoint_rows, 2):
        counterpoint_id = row.get("counterpoint_id", "").strip() or f"row {index}"
        require(
            row,
            [
                "chapter_id",
                "question",
                "position_a_label",
                "position_a_claim_ids",
                "position_b_label",
                "position_b_claim_ids",
                "synthesis",
                "epistemic_status",
                "conditions_to_revise",
            ],
            f"Counterpoint {counterpoint_id}",
            errors,
        )
        chapter_id = row.get("chapter_id", "").strip()
        if chapter_id and chapter_id not in chapter_ids:
            errors.append(
                f"Counterpoint {counterpoint_id}: unknown chapter_id {chapter_id}"
            )
        epistemic = row.get("epistemic_status", "").strip().upper()
        if epistemic and epistemic not in COUNTERPOINT_STATUSES:
            errors.append(
                f"Counterpoint {counterpoint_id}: invalid epistemic_status {epistemic}"
            )
        for field in ("position_a_claim_ids", "position_b_claim_ids"):
            for claim_id in values(row.get(field, "")):
                if claim_id not in claim_ids:
                    errors.append(
                        f"Counterpoint {counterpoint_id}: unknown claim_id {claim_id}"
                    )

    narrative_rows = rows(root / "narrative_manifest.csv")
    visual_ids = unique_id_rows(
        narrative_rows, "visual_id", "narrative visual", errors, warnings
    )
    centerpiece_counts: Counter[str] = Counter()

    for index, row in enumerate(narrative_rows, 2):
        visual_id = row.get("visual_id", "").strip() or f"row {index}"
        require(
            row,
            [
                "chapter_id",
                "title",
                "narrative_question",
                "visual_type",
                "layout",
                "centerpiece",
                "claim_ids",
                "source_ids",
                "data_mode",
                "reader_summary",
                "research_disclosure",
                "fallback_table",
                "keyboard_support",
                "reduced_motion",
                "print_fallback",
                "limitations",
            ],
            f"Narrative visual {visual_id}",
            errors,
        )

        chapter_id = row.get("chapter_id", "").strip()
        visual_type = row.get("visual_type", "").strip().upper()
        layout = row.get("layout", "").strip().upper()
        data_mode = row.get("data_mode", "").strip().upper()

        if chapter_id and chapter_id not in chapter_ids:
            errors.append(
                f"Narrative visual {visual_id}: unknown chapter_id {chapter_id}"
            )
        if visual_type and visual_type not in VISUAL_TYPES:
            errors.append(
                f"Narrative visual {visual_id}: invalid visual_type {visual_type}"
            )
        if layout and layout not in VISUAL_LAYOUTS:
            errors.append(
                f"Narrative visual {visual_id}: invalid layout {layout}"
            )
        if data_mode and data_mode not in DATA_MODES:
            errors.append(
                f"Narrative visual {visual_id}: invalid data_mode {data_mode}"
            )
        if yes(row.get("centerpiece", "")) and chapter_id:
            centerpiece_counts[chapter_id] += 1

        for claim_id in values(row.get("claim_ids", "")):
            if claim_id not in claim_ids:
                errors.append(
                    f"Narrative visual {visual_id}: unknown claim_id {claim_id}"
                )
        for source_id in values(row.get("source_ids", "")):
            if source_id not in source_ids:
                errors.append(
                    f"Narrative visual {visual_id}: unknown source_id {source_id}"
                )

        if layout == "STICKY_SCROLL":
            step_ids = values(row.get("step_ids", ""))
            if len(step_ids) < 3:
                errors.append(
                    f"Narrative visual {visual_id}: STICKY_SCROLL needs >=3 step_ids"
                )
            for field in ("keyboard_support", "reduced_motion", "print_fallback"):
                if not yes(row.get(field, "")):
                    errors.append(
                        f"Narrative visual {visual_id}: STICKY_SCROLL requires {field}=yes"
                    )
            if not row.get("fallback_table", "").strip():
                errors.append(
                    f"Narrative visual {visual_id}: STICKY_SCROLL missing fallback_table"
                )

    for chapter_id, count in centerpiece_counts.items():
        if count > 1:
            errors.append(f"{chapter_id}: more than one centerpiece visual ({count})")

    for index, row in enumerate(chapter_rows, 2):
        chapter_id = row.get("chapter_id", "").strip() or f"row {index}"
        require(
            row,
            [
                "chapter_number",
                "title",
                "guiding_question",
                "provisional_thesis",
                "claim_ids",
                "mini_conclusion",
                "takeaway",
                "reader_summary",
                "research_disclosure",
                "default_mode",
                "status",
            ],
            f"Chapter {chapter_id}",
            errors,
        )

        mode = row.get("default_mode", "").strip()
        status = row.get("status", "").strip().upper()
        if mode and mode not in CHAPTER_MODES:
            errors.append(f"Chapter {chapter_id}: invalid default_mode {mode}")
        if status and status not in CHAPTER_STATUSES:
            errors.append(f"Chapter {chapter_id}: invalid status {status}")

        for claim_id in values(row.get("claim_ids", "")):
            if claim_id not in claim_ids:
                errors.append(f"Chapter {chapter_id}: unknown claim_id {claim_id}")
        for related in values(row.get("related_chapter_ids", "")):
            if related not in chapter_ids:
                errors.append(
                    f"Chapter {chapter_id}: unknown related_chapter_id {related}"
                )

        centerpiece = row.get("centerpiece_visual_id", "").strip()
        if centerpiece:
            if centerpiece not in visual_ids:
                errors.append(
                    f"Chapter {chapter_id}: unknown centerpiece_visual_id {centerpiece}"
                )
            matching = [
                item
                for item in narrative_rows
                if item.get("visual_id", "").strip() == centerpiece
            ]
            if matching and not yes(matching[0].get("centerpiece", "")):
                errors.append(
                    f"Chapter {chapter_id}: referenced visual {centerpiece} is not marked centerpiece"
                )

        counterpoint = row.get("counterpoint_id", "").strip()
        if counterpoint and counterpoint not in counterpoint_ids:
            errors.append(
                f"Chapter {chapter_id}: unknown counterpoint_id {counterpoint}"
            )

    chart_rows = rows(root / "chart_manifest.csv")
    unique_id_rows(chart_rows, "chart_id", "chart", errors, warnings)

    for index, row in enumerate(chart_rows, 2):
        chart_id = row.get("chart_id", "").strip() or f"row {index}"
        chapter_id = row.get("chapter_id", "").strip()
        if chapter_id and chapter_id not in chapter_ids:
            errors.append(f"Chart {chart_id}: unknown chapter_id {chapter_id}")
        if not row.get("source_ids", "").strip():
            errors.append(f"Chart {chart_id}: missing source_ids")
        if not row.get("unit", "").strip():
            warnings.append(f"Chart {chart_id}: missing unit")
        if not row.get("limitations", "").strip():
            warnings.append(f"Chart {chart_id}: missing limitations")
        if not row.get("fallback_table", "").strip():
            warnings.append(f"Chart {chart_id}: missing fallback_table")
        for source_id in values(row.get("source_ids", "")):
            if source_id not in source_ids:
                errors.append(f"Chart {chart_id}: unknown source_id {source_id}")
        for claim_id in values(row.get("claim_ids", "")):
            if claim_id not in claim_ids:
                errors.append(f"Chart {chart_id}: unknown claim_id {claim_id}")

    audit_rows = rows(root / "claim_audit.csv")
    audit = {
        row.get("claim_id", "").strip(): row
        for row in audit_rows
        if row.get("claim_id", "").strip()
    }
    for claim_id in claim_ids:
        row = audit.get(claim_id)
        if not row:
            warnings.append(f"{claim_id}: no claim_audit row")
            continue
        if row.get("final_status", "").strip().lower() == "verified":
            if not yes(row.get("citation_present", "")) or not yes(
                row.get("source_entails_claim", "")
            ):
                errors.append(
                    f"{claim_id}: Verified without citation entailment"
                )

    for item in errors:
        print("ERROR:", item)
    for item in warnings:
        print("WARNING:", item)

    if errors:
        print(f"FAIL: {len(errors)} errors, {len(warnings)} warnings")
        return 2
    if warnings:
        print(f"PASS WITH WARNINGS: {len(warnings)}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
