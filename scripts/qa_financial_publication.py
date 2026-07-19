#!/usr/bin/env python3
"""Validate Financial HTML narrative publication JSON without external dependencies."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

RELATIONS = {
    "SUPPORTS", "CONTRADICTS", "QUALIFIES", "EXPLAINS",
    "DERIVED_FROM", "SYNTHESIZES", "DEPENDS_ON", "INVALIDATES_IF",
}
EVIDENCE_CLASSES = {"FACT", "DERIVED", "INFERENCE", "SCENARIO", "RECOMMENDATION"}
DATA_MODES = {"verified-data", "derived-data", "scenario-data", "illustrative-mechanism"}


def nonempty(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def unique_ids(items, key, label, errors):
    seen = set()
    for index, item in enumerate(items):
        value = item.get(key, "")
        if not nonempty(value):
            errors.append(f"{label}[{index}] missing {key}")
            continue
        if value in seen:
            errors.append(f"Duplicate {key}: {value}")
        seen.add(value)
    return seen


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("publication", help="Path to publication.json")
    args = parser.parse_args()
    path = Path(args.publication).expanduser().resolve()
    if not path.exists():
        print(f"ERROR: file not found: {path}")
        return 2

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: invalid JSON: {exc}")
        return 2

    errors, warnings = [], []
    for key in ("report", "chapters", "claims", "edges", "counterpoints", "visuals"):
        if key not in data:
            errors.append(f"Missing top-level key: {key}")

    if errors:
        for item in errors:
            print("ERROR:", item)
        return 2

    chapters = data.get("chapters") or []
    claims = data.get("claims") or []
    edges = data.get("edges") or []
    counterpoints = data.get("counterpoints") or []
    visuals = data.get("visuals") or []

    chapter_ids = unique_ids(chapters, "chapterId", "chapters", errors)
    claim_ids = unique_ids(claims, "claimId", "claims", errors)
    counterpoint_ids = unique_ids(counterpoints, "counterpointId", "counterpoints", errors)
    visual_ids = unique_ids(visuals, "visualId", "visuals", errors)

    incoming = {claim_id: [] for claim_id in claim_ids}
    outgoing = {claim_id: [] for claim_id in claim_ids}

    for claim in claims:
        cid = claim.get("claimId", "")
        evidence_class = claim.get("evidenceClass", "")
        if evidence_class not in EVIDENCE_CLASSES:
            errors.append(f"{cid}: invalid evidenceClass {evidence_class}")
        for chapter_id in claim.get("chapterIds", []):
            if chapter_id not in chapter_ids:
                errors.append(f"{cid}: unknown chapterId {chapter_id}")
        if evidence_class == "DERIVED":
            if not nonempty(claim.get("formula")):
                errors.append(f"{cid}: DERIVED missing formula")
            if not claim.get("inputClaimIds"):
                errors.append(f"{cid}: DERIVED missing inputClaimIds")
        for input_id in claim.get("inputClaimIds", []):
            if input_id not in claim_ids:
                errors.append(f"{cid}: unknown inputClaimId {input_id}")
        if evidence_class == "FACT" and not claim.get("sourceIds"):
            errors.append(f"{cid}: FACT missing sourceIds")

    for index, edge in enumerate(edges):
        source = edge.get("fromClaimId", "")
        target = edge.get("toClaimId", "")
        relation = edge.get("relation", "")
        if source not in claim_ids:
            errors.append(f"edge[{index}]: unknown fromClaimId {source}")
        if target not in claim_ids:
            errors.append(f"edge[{index}]: unknown toClaimId {target}")
        if relation not in RELATIONS:
            errors.append(f"edge[{index}]: invalid relation {relation}")
        if not nonempty(edge.get("basis")):
            errors.append(f"edge[{index}]: missing basis")
        if relation == "INVALIDATES_IF" and not nonempty(edge.get("trigger")):
            errors.append(f"edge[{index}]: INVALIDATES_IF missing trigger")
        if source in outgoing:
            outgoing[source].append(edge)
        if target in incoming:
            incoming[target].append(edge)

    for chapter in chapters:
        chapter_id = chapter.get("chapterId", "")
        required_text = [
            "title", "guidingQuestion", "provisionalThesis", "miniConclusion",
            "riskOfInterpretation", "takeaway",
        ]
        for field in required_text:
            if not nonempty(chapter.get(field)):
                errors.append(f"{chapter_id}: missing {field}")
        chapter_claims = chapter.get("claimIds", [])
        if not chapter_claims:
            errors.append(f"{chapter_id}: missing claimIds")
        for claim_id in chapter_claims:
            if claim_id not in claim_ids:
                errors.append(f"{chapter_id}: unknown claimId {claim_id}")
        for claim_id in chapter.get("takeawayClaimIds", []):
            if claim_id not in claim_ids:
                errors.append(f"{chapter_id}: unknown takeawayClaimId {claim_id}")
            elif not incoming.get(claim_id) and not outgoing.get(claim_id):
                errors.append(f"{chapter_id}: takeaway claim {claim_id} has no graph edge")
        if not chapter.get("monitoringMetrics"):
            errors.append(f"{chapter_id}: missing monitoringMetrics")
        visual_id = chapter.get("centerpieceVisualId")
        if visual_id and visual_id not in visual_ids:
            errors.append(f"{chapter_id}: unknown centerpieceVisualId {visual_id}")
        for counterpoint_id in chapter.get("counterpointIds", []):
            if counterpoint_id not in counterpoint_ids:
                errors.append(f"{chapter_id}: unknown counterpointId {counterpoint_id}")

    for counterpoint in counterpoints:
        cid = counterpoint.get("counterpointId", "")
        chapter_id = counterpoint.get("chapterId", "")
        if chapter_id not in chapter_ids:
            errors.append(f"{cid}: unknown chapterId {chapter_id}")
        for field in ("question", "mainPosition", "opposingPosition", "synthesis"):
            if not nonempty(counterpoint.get(field)):
                errors.append(f"{cid}: missing {field}")
        for side in ("mainClaimIds", "opposingClaimIds"):
            values = counterpoint.get(side, [])
            if not values:
                errors.append(f"{cid}: missing {side}")
            for claim_id in values:
                if claim_id not in claim_ids:
                    errors.append(f"{cid}: unknown {side} claim {claim_id}")
        if not counterpoint.get("resolvingMetrics"):
            errors.append(f"{cid}: missing resolvingMetrics")

    for visual in visuals:
        vid = visual.get("visualId", "")
        chapter_id = visual.get("chapterId", "")
        if chapter_id not in chapter_ids:
            errors.append(f"{vid}: unknown chapterId {chapter_id}")
        mode = visual.get("dataMode", "")
        if mode not in DATA_MODES:
            errors.append(f"{vid}: invalid dataMode {mode}")
        for claim_id in visual.get("claimIds", []):
            if claim_id not in claim_ids:
                errors.append(f"{vid}: unknown claimId {claim_id}")
        if mode in {"verified-data", "scenario-data"} and not visual.get("sourceIds"):
            errors.append(f"{vid}: {mode} missing sourceIds")
        if mode == "derived-data":
            derived = [c for c in visual.get("claimIds", []) if next((x for x in claims if x.get("claimId") == c and x.get("evidenceClass") == "DERIVED"), None)]
            if not derived:
                errors.append(f"{vid}: derived-data has no DERIVED claim")
        for field in ("mobileFallback", "printFallback", "accessibilityNote", "limitations"):
            if not nonempty(visual.get(field)):
                errors.append(f"{vid}: missing {field}")
        if visual.get("layout") == "sticky-scroll" and len(visual.get("stepIds", [])) < 3:
            warnings.append(f"{vid}: sticky-scroll has fewer than 3 steps")
        if mode == "illustrative-mechanism" and "illustr" not in str(visual.get("limitations", "")).lower() and "minh họa" not in str(visual.get("limitations", "")).lower():
            warnings.append(f"{vid}: illustrative mechanism disclosure may be unclear")

    for claim_id in claim_ids:
        if not incoming.get(claim_id) and not outgoing.get(claim_id):
            warnings.append(f"{claim_id}: orphan claim in graph")

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
