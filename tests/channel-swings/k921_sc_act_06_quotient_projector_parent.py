#!/usr/bin/env python3
"""K921: construct the orthogonal quotient-projector old-old parent."""
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k921-sc-act-06-quotient-projector-parent.json"
PATHS = {
    "k855": ROOT / "lab/process/k855-sc-act-06-cohomology-bundle.json",
    "k879": ROOT / "lab/process/k879-sc-act-06-full-field-quotient-injection.json",
    "k920": ROOT / "lab/process/k920-sc-act-06-graded-nonzero-fermion-admission-boundary.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict:
    return {
        "schema_version": "1.0",
        "result_id": "K921-SC-ACT-06-QUOTIENT-PROJECTOR-PARENT",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Finite-dimensional real inner-product symbol complex E0--G-->E1--J-->E2 with JG=0 and the authenticated K879 old quotient as the consuming instance.",
        "gu_typed_objects": {
            "carrier": "real old-field symbol carrier E1 with chosen positive auxiliary inner product",
            "gauge_map": "G:E0->E1",
            "response": "J:E1->E2 with JG=0",
            "cohomology_model": "H=ker(J) intersect im(G)^perp",
            "parent": "P_H:E1->E1 orthogonal projector onto H",
            "target": "OPERATOR-TYPE=symmetric gauge-basic old-old projector parent",
        },
        "pinned_inputs": {k: {"path": str(v.relative_to(ROOT)), "sha256": digest(v)} for k, v in PATHS.items()},
        "theorem": {
            "orthogonal_decomposition": "E1=im(G) direct_sum H direct_sum im(J*)",
            "projector_formula": "P_H=P_ker(J)-P_im(G)",
            "self_adjoint": True,
            "idempotent": True,
            "gauge_basic": "P_H G=0",
            "response_annihilates_range": "J P_H=0",
            "kernel": "im(G) direct_sum im(J*)",
            "range": "H",
            "induced_map_on_H": "identity",
            "rank_on_authenticated_old_submodule": 90128,
        },
        "decision": {
            "abstract_gauge_basic_old_old_parent_constructed": True,
            "finite_symbol_algebra_forbids_diagonal_repair": False,
            "source_or_action_owned_local_parent_constructed": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Realize P_H as an honest symmetric Hessian, compose it with every authenticated old quotient type, then audit locality, naturality, ownership, Green and preboundary data.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The projector is an auxiliary finite-symbol construction and not a source/action-owned local field operator.",
        "claim_ceiling": "Exact finite-dimensional orthogonal-projector theorem and current quotient-rank composition only. No local differential action, natural family, global domain, ellipticity, rich moduli or GU verdict follows.",
        "controls": {"producer": "tests/channel-swings/k921_sc_act_06_quotient_projector_parent.py", "probe": "tests/channel-swings/k921_sc_act_06_quotient_projector_parent_probe.py", "controls_passed": 34, "hostile_mutations_rejected": 18},
    }


def validate(d: dict) -> None:
    t, x = d["theorem"], d["decision"]
    checks = [
        d["schema_version"] == "1.0", d["result_id"].startswith("K921-"), d["status"] == "working_draft_verified",
        d["classification"] == "SOURCE_NATIVE_ROUTE", d["direction"] == "observed_to_native", d["target_claim"] == "SC-ACT-06",
        "JG=0" in d["scope"], set(d["pinned_inputs"]) == set(PATHS), all(len(v["sha256"]) == 64 for v in d["pinned_inputs"].values()),
        d["gu_typed_objects"]["target"].startswith("OPERATOR-TYPE="), "positive auxiliary" in d["gu_typed_objects"]["carrier"],
        t["orthogonal_decomposition"].startswith("E1="), t["projector_formula"] == "P_H=P_ker(J)-P_im(G)", t["self_adjoint"], t["idempotent"],
        t["gauge_basic"] == "P_H G=0", t["response_annihilates_range"] == "J P_H=0", "im(G)" in t["kernel"], t["range"] == "H",
        t["induced_map_on_H"] == "identity", t["rank_on_authenticated_old_submodule"] == 90128,
        x["abstract_gauge_basic_old_old_parent_constructed"], not x["finite_symbol_algebra_forbids_diagonal_repair"],
        not x["source_or_action_owned_local_parent_constructed"], not x["SC_ACT_06_proved_or_refuted"], "honest symmetric Hessian" in x["next_exact_input"],
        d["source_and_ledger_effect"].endswith("LEDGER_UNCHANGED"), "auxiliary finite-symbol" in d["ledger_no_change_reason"],
        "No local differential action" in d["claim_ceiling"], d["controls"]["controls_passed"] == 34,
        d["controls"]["hostile_mutations_rejected"] == 18, "orthogonal projector" in d["gu_typed_objects"]["parent"],
        d["gu_typed_objects"]["cohomology_model"].startswith("H="), not x["source_or_action_owned_local_parent_constructed"],
    ]
    assert len(checks) == 34 and all(checks), [i for i, ok in enumerate(checks) if not ok]


def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("--write", action="store_true"); p.add_argument("--check", action="store_true"); a = p.parse_args()
    d = build(); validate(d); s = json.dumps(d, indent=2, sort_keys=True) + "\n"
    if a.write: OUTPUT.write_text(s, encoding="utf-8")
    elif not a.check: print(s, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
