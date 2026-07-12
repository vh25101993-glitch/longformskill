#!/usr/bin/env python3
"""Validate Longform desk-research project files and core evidence integrity."""
from __future__ import annotations
import argparse, csv, re
from pathlib import Path

REQUIRED = ["research_brief.md","research_plan.csv","source_register.csv","evidence_ledger.csv","data_dictionary.csv","chart_manifest.csv","claim_audit.csv","uncertainty_register.csv","paper.md"]
TOKEN = re.compile(r"\{\{[A-Z0-9_]+\}\}")
VAGUE = re.compile(r"\b(nguồn tổng hợp|nhiều nguồn|theo nghiên cứu)\b", re.I)


def rows(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def yes(v: str) -> bool:
    return str(v).strip().lower() in {"yes","true","1","y","có","co"}


def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("project"); args = p.parse_args()
    root = Path(args.project).expanduser().resolve(); errors=[]; warnings=[]
    for name in REQUIRED:
        if not (root/name).exists(): errors.append(f"Missing required file: {name}")
    if errors:
        for x in errors: print("ERROR:", x)
        return 2
    paper=(root/"paper.md").read_text(encoding="utf-8", errors="replace")
    if TOKEN.search(paper): errors.append("Raw placeholder found in paper.md")
    if VAGUE.search(paper): warnings.append("Vague source phrase found")
    source_ids={r.get("source_id","").strip() for r in rows(root/"source_register.csv") if r.get("source_id","").strip()}
    claims=rows(root/"evidence_ledger.csv"); claim_ids=set()
    for i,r in enumerate(claims,2):
        cid=r.get("claim_id","").strip(); cls=r.get("claim_class","").strip().upper(); sid=r.get("source_id","").strip()
        if not cid: warnings.append(f"row {i}: missing claim_id"); continue
        if cid in claim_ids: errors.append(f"Duplicate claim_id: {cid}")
        claim_ids.add(cid)
        if cls in {"FACT","DERIVED"} and not sid: errors.append(f"{cid}: {cls} missing source_id")
        if sid and sid not in source_ids: errors.append(f"{cid}: unknown source_id {sid}")
        if cls=="DERIVED" and not r.get("formula","").strip(): errors.append(f"{cid}: DERIVED missing formula")
        if r.get("data_status","").strip().lower() in {"interpolated","estimated","forecast"} and not r.get("notes","").strip(): warnings.append(f"{cid}: estimated data missing disclosure")
    for i,r in enumerate(rows(root/"chart_manifest.csv"),2):
        cid=r.get("chart_id","").strip() or f"row {i}"
        if not r.get("source_ids","").strip(): errors.append(f"Chart {cid}: missing source_ids")
        if not r.get("unit","").strip(): warnings.append(f"Chart {cid}: missing unit")
        if not r.get("limitations","").strip(): warnings.append(f"Chart {cid}: missing limitations")
    audit={r.get("claim_id","").strip():r for r in rows(root/"claim_audit.csv") if r.get("claim_id","").strip()}
    for cid in claim_ids:
        r=audit.get(cid)
        if not r: warnings.append(f"{cid}: no claim_audit row"); continue
        if r.get("final_status","").strip().lower()=="verified" and (not yes(r.get("citation_present","")) or not yes(r.get("source_entails_claim",""))): errors.append(f"{cid}: Verified without citation entailment")
    for x in errors: print("ERROR:",x)
    for x in warnings: print("WARNING:",x)
    if errors: print(f"FAIL: {len(errors)} errors, {len(warnings)} warnings"); return 2
    if warnings: print(f"PASS WITH WARNINGS: {len(warnings)}"); return 1
    print("PASS"); return 0

if __name__ == "__main__": raise SystemExit(main())
