#!/usr/bin/env python3
"""Validate a Longform Research Atlas package.

Usage:
    python scripts/qa_research_atlas.py ./research-project/atlas

The validator is dependency-free and focuses on referential integrity,
claim/source coverage, data-status disclosure, and manifest counts.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

REQUIRED_FILES = {
    "atlas_manifest.json",
    "modules.json",
    "chapters.json",
    "claims.json",
    "sources.json",
    "questions.json",
    "misconceptions.json",
    "pathways.json",
    "theses.json",
    "glossary.json",
    "cases.json",
    "interaction_rules.json",
}

ENTITY_FILES = {
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

VALID_CLAIM_STATUS = {
    "verified",
    "qualified",
    "disputed",
    "interpretation",
    "behavioral-hypothesis",
    "insufficient-evidence",
}

VALID_DATA_TYPES = {
    "observed",
    "derived",
    "interpolated",
    "estimated",
    "forecast",
    "simulation",
    "scenario",
    "heuristic-score",
}

REFERENCE_FIELDS = {
    "moduleIds": "modules",
    "chapterIds": "chapters",
    "claimIds": "claims",
    "sourceIds": "sources",
    "questionIds": "questions",
    "misconceptionIds": "misconceptions",
    "pathwayIds": "pathways",
    "thesisIds": "theses",
    "caseIds": "cases",
    "conceptIds": "glossary",
    "termIds": "glossary",
    "ruleIds": "interaction_rules",
}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def load_json(path: Path, report: Report) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        report.error(f"Missing file: {path.name}")
    except json.JSONDecodeError as exc:
        report.error(f"Invalid JSON in {path.name}: line {exc.lineno}, column {exc.colno}")
    return None


def as_records(payload: Any, label: str, report: Report) -> list[dict[str, Any]]:
    if payload is None:
        return []
    if isinstance(payload, list):
        records = payload
    elif isinstance(payload, dict) and isinstance(payload.get(label), list):
        records = payload[label]
    elif isinstance(payload, dict) and isinstance(payload.get("items"), list):
        records = payload["items"]
    else:
        report.error(f"{ENTITY_FILES[label]} must be an array or contain '{label}'/'items' array")
        return []

    clean: list[dict[str, Any]] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            report.error(f"{ENTITY_FILES[label]}[{index}] is not an object")
        else:
            clean.append(record)
    return clean


def iter_nested(value: Any) -> Iterable[Any]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from iter_nested(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_nested(child)


def validate_ids(data: dict[str, list[dict[str, Any]]], report: Report) -> dict[str, set[str]]:
    indexes: dict[str, set[str]] = {}
    global_ids: list[str] = []

    for label, records in data.items():
        ids: list[str] = []
        for index, record in enumerate(records):
            entity_id = record.get("id")
            if not isinstance(entity_id, str) or not entity_id.strip():
                report.error(f"{ENTITY_FILES[label]}[{index}] has no valid id")
                continue
            ids.append(entity_id)
            global_ids.append(entity_id)

        duplicates = [key for key, count in Counter(ids).items() if count > 1]
        for entity_id in duplicates:
            report.error(f"Duplicate id in {ENTITY_FILES[label]}: {entity_id}")
        indexes[label] = set(ids)

    cross_duplicates = [key for key, count in Counter(global_ids).items() if count > 1]
    for entity_id in cross_duplicates:
        report.error(f"ID is not globally unique: {entity_id}")

    return indexes


def validate_references(
    data: dict[str, list[dict[str, Any]]],
    indexes: dict[str, set[str]],
    report: Report,
) -> None:
    for label, records in data.items():
        for record in records:
            owner = record.get("id", f"unknown-{label}")
            for node in iter_nested(record):
                if not isinstance(node, dict):
                    continue
                for field, target_label in REFERENCE_FIELDS.items():
                    if field not in node:
                        continue
                    refs = node[field]
                    if refs is None:
                        continue
                    if isinstance(refs, str):
                        refs = [refs]
                    if not isinstance(refs, list):
                        report.error(f"{owner}.{field} must be a string or array")
                        continue
                    for ref in refs:
                        if not isinstance(ref, str):
                            report.error(f"{owner}.{field} contains a non-string reference")
                        elif ref not in indexes.get(target_label, set()):
                            report.error(f"Broken reference: {owner}.{field} -> {ref}")


def validate_modules(records: list[dict[str, Any]], report: Report) -> None:
    for record in records:
        owner = record.get("id", "unknown-module")
        planned = record.get("plannedChapters")
        published = record.get("publishedChapters")
        reviewed = record.get("reviewedChapters")
        values = (planned, published, reviewed)
        if any(value is not None and not isinstance(value, int) for value in values):
            report.error(f"{owner}: planned/published/reviewed chapter counts must be integers")
        if all(isinstance(value, int) for value in values):
            if reviewed > published or published > planned:
                report.error(f"{owner}: expected reviewed <= published <= planned")
        if "chapters" in record and not any(key in record for key in ("plannedChapters", "publishedChapters", "reviewedChapters")):
            report.warn(f"{owner}: ambiguous 'chapters' count; split planned/published/reviewed")


def validate_claims(records: list[dict[str, Any]], report: Report) -> None:
    for record in records:
        owner = record.get("id", "unknown-claim")
        status = record.get("status")
        if status not in VALID_CLAIM_STATUS:
            report.error(f"{owner}: invalid or missing claim status '{status}'")

        source_ids = record.get("sourceIds") or []
        if status == "verified" and not source_ids:
            report.error(f"{owner}: verified claim has no sourceIds")
        if status == "disputed" and len(source_ids) < 2 and not record.get("counterEvidenceIds"):
            report.warn(f"{owner}: disputed claim should expose evidence for competing views")
        if record.get("statementClass") in {"FACT", "DERIVED"} and not source_ids:
            report.error(f"{owner}: {record.get('statementClass')} claim has no sourceIds")


def validate_theses(records: list[dict[str, Any]], claims: dict[str, dict[str, Any]], report: Report) -> None:
    for record in records:
        owner = record.get("id", "unknown-thesis")
        claim_ids = record.get("claimIds") or []
        if not claim_ids:
            report.error(f"{owner}: thesis has no supporting claimIds")
        for claim_id in claim_ids:
            claim = claims.get(claim_id)
            if claim and claim.get("status") in {"insufficient-evidence"}:
                report.error(f"{owner}: depends on unaudited/insufficient claim {claim_id}")


def validate_pathways(records: list[dict[str, Any]], report: Report) -> None:
    for record in records:
        owner = record.get("id", "unknown-pathway")
        steps = record.get("steps")
        if not isinstance(steps, dict):
            report.error(f"{owner}: pathway requires a steps object")
            continue
        has_mechanism = any(key in steps for key in ("macro", "mechanism", "trigger"))
        has_exposure = any(key in steps for key in ("behavior", "balanceSheet", "businessExposure", "policyExposure"))
        has_outcome = any(key in steps for key in ("damage", "outcome", "consequence"))
        if not (has_mechanism and has_exposure and has_outcome):
            report.error(f"{owner}: pathway must include mechanism, exposure/behavior, and outcome/damage")


def validate_data_disclosure(data: dict[str, list[dict[str, Any]]], report: Report) -> None:
    for label, records in data.items():
        for record in records:
            owner = record.get("id", f"unknown-{label}")
            for node in iter_nested(record):
                if not isinstance(node, dict) or "value" not in node:
                    continue
                quantitative_keys = {"unit", "period", "dataType", "sourceId", "sourceIds", "transformation"}
                if not quantitative_keys.intersection(node):
                    continue
                data_type = node.get("dataType")
                if data_type not in VALID_DATA_TYPES:
                    report.error(f"{owner}: quantitative value has invalid/missing dataType '{data_type}'")
                if data_type in {"observed", "derived", "interpolated", "estimated", "forecast"}:
                    if not node.get("sourceId") and not node.get("sourceIds"):
                        report.error(f"{owner}: {data_type} value has no source reference")


def validate_interaction_rules(records: list[dict[str, Any]], report: Report) -> None:
    for record in records:
        owner = record.get("id", "unknown-rule")
        if not record.get("modelVersion"):
            report.error(f"{owner}: interaction rule has no modelVersion")
        text = json.dumps(record, ensure_ascii=False).lower()
        if "probability" in text or "% chance" in text:
            report.warn(f"{owner}: verify that heuristic scoring is not described as probability")
        if record.get("outputType") == "probability" and not record.get("calibrationEvidence"):
            report.error(f"{owner}: probability output requires calibrationEvidence")


def validate_manifest(
    manifest: Any,
    data: dict[str, list[dict[str, Any]]],
    report: Report,
) -> None:
    if not isinstance(manifest, dict):
        report.error("atlas_manifest.json must be an object")
        return
    if not manifest.get("schemaVersion"):
        report.error("atlas_manifest.json has no schemaVersion")
    counts = manifest.get("counts")
    if not isinstance(counts, dict):
        report.error("atlas_manifest.json has no counts object")
        return
    for label, records in data.items():
        declared = counts.get(label)
        if declared is not None and declared != len(records):
            report.error(f"Manifest count mismatch for {label}: declared {declared}, actual {len(records)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Longform Research Atlas package")
    parser.add_argument("atlas_dir", type=Path, help="Path to the atlas directory")
    parser.add_argument("--strict-warnings", action="store_true", help="Return failure when warnings exist")
    args = parser.parse_args()

    report = Report()
    atlas_dir: Path = args.atlas_dir
    if not atlas_dir.is_dir():
        print(f"ERROR: atlas directory does not exist: {atlas_dir}", file=sys.stderr)
        return 2

    present = {path.name for path in atlas_dir.iterdir() if path.is_file()}
    for filename in sorted(REQUIRED_FILES - present):
        report.error(f"Missing required file: {filename}")

    payloads = {
        label: load_json(atlas_dir / filename, report)
        for label, filename in ENTITY_FILES.items()
    }
    data = {label: as_records(payload, label, report) for label, payload in payloads.items()}
    manifest = load_json(atlas_dir / "atlas_manifest.json", report)

    indexes = validate_ids(data, report)
    validate_references(data, indexes, report)
    validate_modules(data["modules"], report)
    validate_claims(data["claims"], report)
    claim_index = {record.get("id"): record for record in data["claims"] if record.get("id")}
    validate_theses(data["theses"], claim_index, report)
    validate_pathways(data["pathways"], report)
    validate_data_disclosure(data, report)
    validate_interaction_rules(data["interaction_rules"], report)
    validate_manifest(manifest, data, report)

    print("Research Atlas QA")
    print(f"Directory: {atlas_dir}")
    print(f"Entities: {sum(len(records) for records in data.values())}")
    print(f"Errors: {len(report.errors)}")
    print(f"Warnings: {len(report.warnings)}")

    for message in report.errors:
        print(f"ERROR: {message}")
    for message in report.warnings:
        print(f"WARNING: {message}")

    if report.errors or (args.strict_warnings and report.warnings):
        return 1
    print("PASS: atlas package passed integrity checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
