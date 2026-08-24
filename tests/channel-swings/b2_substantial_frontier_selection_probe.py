#!/usr/bin/env python3
"""Exact coverage and hostile-mutation probe for the post-exhaustion B2 frontier."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FRONTIER = ROOT / "lab/process/b2-substantial-frontier-selection.json"
REGISTER = ROOT / "lab/process/phenomenology-disposition-register-v0.1.json"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
CBRS = ROOT / "lab/process/selected-k77-cbrs1ab-action-owned-bf-normalization-obstruction.json"
W154 = ROOT / "explorations/W154-reverse-engineered-source-action-2026-07-14.md"
W229 = ROOT / "explorations/W229-close-a2-source-action-znu-completion-2026-07-14.md"

LEDGER_SHA = "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b"
REGISTER_SHA = "759eb1dcad644a7ed28d7b56d1fbbf43e1d2065af7352105cb02ccde0bf2d728"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path):
    return json.loads(path.read_text())


def checks(frontier: dict, register: dict, cbrs: dict, w154: str, w229: str) -> list[str]:
    errors: list[str] = []
    basis = frontier.get("basis", {})
    gate = register.get("exhaustion_evaluation", {})
    dispositions = register.get("terminal_row_dispositions", [])
    b2 = [row for row in dispositions if row.get("bucket") == "B2"]
    arcs = frontier.get("arcs", [])

    if sha256(LEDGER) != LEDGER_SHA or basis.get("ledger_sha256") != LEDGER_SHA:
        errors.append("ledger digest drift")
    if sha256(REGISTER) != REGISTER_SHA or basis.get("disposition_register_sha256") != REGISTER_SHA:
        errors.append("register digest drift")
    if not (gate.get("exhausted") is True and gate.get("b2_selectable") is True):
        errors.append("B2 selection gate is not derived true")
    if (gate.get("denominator_rows"), gate.get("terminal_rows"), gate.get("open_rows")) != (91, 91, 0):
        errors.append("terminal denominator drift")
    if len(b2) != 52 or basis.get("b2_rows") != 52:
        errors.append("B2 row count drift")
    if len(arcs) != 6 or [a.get("rank") for a in arcs] != list(range(1, 7)):
        errors.append("six-arc ranked frontier missing")

    assigned_rows = [row for arc in arcs for row in arc.get("rows", [])]
    expected_rows = [row["row_id"] for row in b2]
    if len(assigned_rows) != len(set(assigned_rows)) or set(assigned_rows) != set(expected_rows):
        errors.append("B2 row assignment is not exact and unique")
    assigned_requirements = [req for arc in arcs for req in arc.get("requirement_ids", [])]
    expected_requirements = sorted({req for row in b2 for req in row.get("named_requirements", [])})
    if len(assigned_requirements) != len(set(assigned_requirements)) or set(assigned_requirements) != set(expected_requirements):
        errors.append("named-requirement assignment is not exact and unique")
    if len(expected_requirements) != 95:
        errors.append("named-requirement denominator drift")

    roots = [arc for arc in arcs if not arc.get("depends_on")]
    if [arc.get("id") for arc in roots] != ["ACTION-VACUUM-STABILIZER-OWNER"]:
        errors.append("frontier no longer has one sequential action root")
    selected = frontier.get("selected_first_owner_gate", {})
    if selected.get("candidate") != "W154/W229-CONDITIONAL-BRANCH3-ACTION":
        errors.append("first qualification candidate drift")
    if "CBRS-1AC" not in selected.get("forbidden_inference", ""):
        errors.append("synthetic CBRS-1AC fence missing")
    if cbrs.get("verdict", {}).get("current_first_action_cbrs1_class") != "OWNER_EXHAUSTED_WITHOUT_LOCAL_SOLUTION":
        errors.append("first-action owner exhaustion not preserved")
    if cbrs.get("next_gate", "").find("ADMIT_NO_SYNTHETIC_CBRS1AC") < 0:
        errors.append("CBRS next-gate synthetic fence drift")
    if "(9,5)" not in w154 or "H41 unbuilt" not in w154:
        errors.append("W154 K95/H41 ceiling missing")
    if "(9,5)" not in w229 or "H41 unbuilt" not in w229:
        errors.append("W229 K95/H41 ceiling missing")

    scale = frontier.get("next_run_scale_receipt", {})
    if scale.get("recommended_scale") != "big_swing" or not scale.get("overall_scale_down_reason"):
        errors.append("next-run scale-down receipt missing")
    excluded = scale.get("excluded_arc_dispositions", [])
    if len(excluded) != 5 or any(row.get("limiting_predicate") != "dependency" or not row.get("evidence") for row in excluded):
        errors.append("downstream dependency dispositions incomplete")
    for protected in (
        "ledger_verdict_change", "source_ownership_change",
        "prediction_or_confirmation_change", "claim_status_change",
        "canon_verdict_change", "public_posture_change",
    ):
        if frontier.get(protected) != "none":
            errors.append(f"protected effect moved: {protected}")
    return errors


def selftest(frontier: dict, register: dict, cbrs: dict, w154: str, w229: str) -> None:
    mutations = []
    x = copy.deepcopy(frontier); x["arcs"][0]["rows"].append(x["arcs"][1]["rows"][0]); mutations.append(x)
    x = copy.deepcopy(frontier); x["arcs"][0]["requirement_ids"].remove("U1-1"); mutations.append(x)
    x = copy.deepcopy(frontier); x["arcs"][1]["depends_on"] = []; mutations.append(x)
    x = copy.deepcopy(frontier); x["selected_first_owner_gate"]["candidate"] = "CBRS-1AC"; mutations.append(x)
    x = copy.deepcopy(frontier); x["selected_first_owner_gate"]["forbidden_inference"] = ""; mutations.append(x)
    x = copy.deepcopy(frontier); x["next_run_scale_receipt"]["overall_scale_down_reason"] = ""; mutations.append(x)
    x = copy.deepcopy(frontier); x["next_run_scale_receipt"]["excluded_arc_dispositions"].pop(); mutations.append(x)
    x = copy.deepcopy(frontier); x["canon_verdict_change"] = "changed"; mutations.append(x)
    caught = sum(bool(checks(x, register, cbrs, w154, w229)) for x in mutations)
    if caught != len(mutations):
        raise SystemExit(f"SELFTEST_FAIL caught {caught}/{len(mutations)}")
    print(f"SELFTEST_PASS caught {caught}/{len(mutations)} hostile mutations")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    frontier, register, cbrs = load(FRONTIER), load(REGISTER), load(CBRS)
    w154, w229 = W154.read_text(), W229.read_text()
    errors = checks(frontier, register, cbrs, w154, w229)
    if errors:
        raise SystemExit("FAIL\n" + "\n".join(f"- {e}" for e in errors))
    print("PASS 52/52 B2 rows; 95/95 named requirements; six arcs; one root")
    if args.selftest:
        selftest(frontier, register, cbrs, w154, w229)


if __name__ == "__main__":
    main()
