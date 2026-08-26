#!/usr/bin/env python3
"""Exact corpus and logic probe for the TWG-1 theory-wide gravity contract."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REG_PATH = ROOT / "lab/process/theory-wide-gravity-falsifier-contract.json"


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text())


def sha256(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


checks = 0


def check(label: str, condition: bool) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)
    print(f"PASS {checks:02d} {label}")


reg = load_json("lab/process/theory-wide-gravity-falsifier-contract.json")
ledger = load_json(reg["input_pins"]["ledger"]["path"])
recovery = load_json(reg["input_pins"]["recovery_no_go_register"]["path"])
qualification = load_json(reg["input_pins"]["w154_w229_owner_qualification"]["path"])
bucket = load_json(reg["input_pins"]["strongfield_bucket_disposition"]["path"])
source_text = (ROOT / reg["input_pins"]["source_claim_register"]["path"]).read_text()
artifact = (ROOT / reg["artifact"]).read_text()


# A. Pinned input currency.
for key in (
    "ledger",
    "source_claim_register",
    "recovery_no_go_register",
    "w154_w229_owner_qualification",
    "strongfield_bucket_disposition",
):
    pin = reg["input_pins"][key]
    check(f"pin {key} matches exact bytes", sha256(pin["path"]) == pin["sha256"])


# B. The ledger object and the current branch no-go remain exactly scoped.
lt_gr9 = next(row for row in ledger["rows"] if row["id"] == "LT-GR9")
check("LT-GR9 remains NEEDS", lt_gr9["verdict"] == "NEEDS")
check("LT-GR9 remains MISSING_CONSTRUCTION", lt_gr9["reason_kind"] == "MISSING_CONSTRUCTION")
check("LT-GR9 kill scope is only the realization bridge", lt_gr9["kill_scope"] == "SCOPED_STRONGFIELD_REALIZATION_BRIDGE_ONLY")
gr_nogo = next(target for target in recovery["targets"] if target["id"] == "RECOVERY-NOGO-GR-W229-VACUUM")
check("W229 gravity result remains branch-local", gr_nogo["current_grade"] == "branch-local NO_GO")
check("W229 gravity challenge closes bounded only", gr_nogo["challenge_state"] == "BOUNDED_NO_GO")
check("W229 final swing is bounded no-go", gr_nogo["completed_swings"][-1]["result"] == "BOUNDED_NO_GO")


# C. The released action census is complete as a census, not as a strong-field construction.
claim_ids = reg["input_pins"]["source_claim_register"]["action_claim_ids"]
check("released action claim IDs are exactly SC-ACT-01 through SC-ACT-06", claim_ids == [f"SC-ACT-0{i}" for i in range(1, 7)])
for claim_id in claim_ids:
    check(f"source register contains {claim_id}", source_text.count(f"- id: {claim_id}\n") == 1)
check("W154/W229 is not admitted as K77 action owner", qualification["admission_result"]["candidate_admitted"] is False)
check("no canonical real K95-to-K77 action bridge exists", qualification["real_form_qualification"]["canonical_real_spin_equivariant_action_bridge"] is False)
check("the current named B2 owner set is empty", qualification["root_candidate_rebuild"]["current_named_root_candidate_set"] == [])


# D. All five forward strong-field owners are still missing.
requirements = reg["strongfield_requirements"]
check("strong-field requirement IDs are SF-1 through SF-5", [row["id"] for row in requirements] == [f"SF-{i}" for i in range(1, 6)])
check("all strong-field requirements remain missing", {row["current_state"] for row in requirements} == {"MISSING"})
lt_disp = next(row for row in bucket["dispositions"] if row["row_id"] == "LT-GR9")
check("bucket disposition names the same five requirements", lt_disp["named_requirements"] == [f"SF-{i}" for i in range(1, 6)])
check("LT-GR9 remains precise B2 nonadmission", lt_disp["bucket"] == "B2" and lt_disp["outcome"] == "PRECISE_NONADMISSION")


# E. Quantifier hierarchy: a scoped branch kill never self-promotes.
domains = {row["id"]: row for row in reg["falsification_domains"]}
check("D0 branch is killed but not theory-wide", domains["D0-W229-RECORD-CURRENT"]["current_result"] == "BOUNDED_NO_GO" and domains["D0-W229-RECORD-CURRENT"]["theory_wide"] is False)
check("D1 is the only theory-wide frozen target", domains["D1-GU-AS-RELEASED-STRONGFIELD"]["theory_wide"] is True)
check("D1 verdict is not adjudicated", domains["D1-GU-AS-RELEASED-STRONGFIELD"]["current_result"] == "NOT_ADJUDICATED")
check("arbitrary future completions are rejected as a target", domains["D2-ARBITRARY-FUTURE-COMPLETIONS"]["current_result"] == "INVALID_FALSIFICATION_TARGET")


def adjudicate(*, domain_complete: bool, native_forward: bool, universal_obstruction: bool, target_import: bool) -> str:
    if target_import:
        return "INVALID_TARGET_IMPORT"
    if universal_obstruction and domain_complete and native_forward:
        return "THEORY_WIDE_KILL"
    if universal_obstruction:
        return "SCOPED_OR_PREMATURE_NO_GO"
    return "NOT_KILLED"


check("planted branch promotion is refused", adjudicate(domain_complete=False, native_forward=False, universal_obstruction=True, target_import=False) == "SCOPED_OR_PREMATURE_NO_GO")
check("planted imported-metric promotion is refused", adjudicate(domain_complete=True, native_forward=False, universal_obstruction=True, target_import=True) == "INVALID_TARGET_IMPORT")
check("a complete native universal obstruction would fire", adjudicate(domain_complete=True, native_forward=True, universal_obstruction=True, target_import=False) == "THEORY_WIDE_KILL")
check("absence of a universal obstruction does not kill", adjudicate(domain_complete=True, native_forward=True, universal_obstruction=False, target_import=False) == "NOT_KILLED")


# F. Artifact and change ceiling.
check("artifact declares exact target claim", "target_claim: GU-AS-RELEASED-STRONGFIELD" in artifact)
check("artifact refuses current target adjudication", "target_claim_verdict: NOT_ADJUDICATED" in artifact)
check("artifact contains typed object declaration", "```gu-typed-objects" in artifact)
check("artifact names all three kill horns", all(token in artifact for token in ("K1-NONEXISTENCE", "K2-UNIVERSAL-PHYSICAL-RESIDUAL", "K3-UNIVERSAL-OBSERVABLE-CONFLICT")))
check("all protected effects remain none", set(reg["changes"].values()) == {"none"})
check("canonical effect remains pending integration", reg["canonical_effect"] == "pending_integration")
check("scheduled steering remains unchanged", reg["steering_effect"] == "unchanged")

print(f"TWG-1 theory-wide gravity falsifier contract: {checks}/{checks} PASS")
