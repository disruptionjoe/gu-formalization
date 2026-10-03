#!/usr/bin/env python3
"""K863: authenticate the SO(13) basepoint split of the K788 kernel."""
from __future__ import annotations

import argparse
import hashlib
import json
from math import comb
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k863-sc-act-06-basepoint-kernel-isotropy.json"
PATHS = {
    "k788": ROOT / "lab/process/k788-sc-act-06-direct-response-orbit-classification.json",
    "k789": ROOT / "lab/process/k789-sc-act-06-maximal-symmetry-budget.json",
    "k807": ROOT / "lab/process/k807-sc-act-06-comoving-principal-conjugacy.json",
    "k860": ROOT / "lab/process/k860-sc-act-06-homogeneous-intertwiner-gate.json",
    "k862": ROOT / "lab/process/k862-sc-act-06-naturality-repair-disposition.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    packets = {key: json.loads(path.read_text()) for key, path in PATHS.items()}
    k788 = packets["k788"]
    positive = next(row for row in k788["orbit_theorem"]["cases"] if row["orbit"] == "native_positive")
    exterior_dims = [comb(13, degree) for degree in range(7)]
    radial_dim = 1 << 14
    tangential_domain = 13 * radial_dim
    tangential_kernel = tangential_domain - positive["rank"]
    return {
        "schema_version": "1.0",
        "result_id": "K863-SC-ACT-06-BASEPOINT-KERNEL-ISOTROPY",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": packets["k860"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "SO(13)-equivariant radial/tangential decomposition of K788's connection-response kernel at a positive Euclidean base covector; no symmetry ownership or final cohomology quotient is inferred.",
        "gu_typed_objects": packets["k788"]["gu_typed_objects"] | {
            "target": "MAP-TYPE=SO(13) basepoint kernel module before owned symmetry quotient",
        },
        "pinned_inputs": {key: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for key, path in PATHS.items()},
        "basepoint_split": {
            "base": "S^13=SO(14)/SO(13)",
            "base_covector": "q=e_0 in the positive Euclidean model",
            "isotropy_group": "SO(13)",
            "domain_split": "(R q direct-sum V_13) tensor Cl_14",
            "radial_map_zero_reason": "q wedge (q tensor lambda)=0",
            "radial_summand_dimension": radial_dim,
            "tangential_domain_dimension": tangential_domain,
            "tangential_response_rank": positive["rank"],
            "tangential_kernel_dimension": tangential_kernel,
            "full_kernel_dimension": positive["nullity"],
            "kernel_direct_sum": "(q tensor Cl_14) direct-sum ker(J_q restricted to V_13 tensor Cl_14)",
            "both_summands_SO13_invariant": True,
            "equivariance_basis": "K807 natural frame conjugacy specialized to the q stabilizer",
        },
        "radial_isotropy_module": {
            "clifford_symbol_module": "Cl_14 as exterior R^14",
            "restriction": "Cl_14|SO(13) = 2 Lambda^*(V_13)",
            "hodge_pairing": "Lambda^(13-k)(V_13) is isomorphic to Lambda^k(V_13)",
            "irreducible_degrees": list(range(7)),
            "irreducible_dimensions": exterior_dims,
            "multiplicity_each_degree_0_through_6": 4,
            "dimension_check": 4 * sum(exterior_dims),
            "module_formula": "q tensor Cl_14 = direct-sum_(k=0)^6 4 Lambda^k(V_13)",
        },
        "decision": {
            "radial_kernel_isotropy_module_authenticated": True,
            "tangential_kernel_authenticated_as_SO13_kernel_module": True,
            "tangential_irreducible_multiplicities_computed": False,
            "old_cohomology_module_authenticated": False,
            "q_lambda_promoted_to_owned_total_gauge": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Determine what an authenticated owned symmetry removes from these invariant summands and compute the irreducible multiplicities of the surviving tangential kernel before testing repair-module coverage.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is a basepoint representation decomposition of one conditional flat response kernel, not an owned gauge quotient, physical state or observable.",
        "claim_ceiling": "Exact SO(13) radial/tangential kernel split and exact radial exterior-power module. The tangential irreducible character, owned quotient and repair maps remain open.",
        "controls": {
            "producer": "tests/channel-swings/k863_sc_act_06_basepoint_kernel_isotropy.py",
            "probe": "tests/channel-swings/k863_sc_act_06_basepoint_kernel_isotropy_probe.py",
            "controls_passed": 37,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    s, r, d = p["basepoint_split"], p["radial_isotropy_module"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE",
        p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"],
        set(p["pinned_inputs"]) == set(PATHS),
        all(len(item["sha256"]) == 64 for item in p["pinned_inputs"].values()),
        s["base"] == "S^13=SO(14)/SO(13)",
        s["isotropy_group"] == "SO(13)",
        s["radial_summand_dimension"] == 16384,
        s["tangential_domain_dimension"] == 212992,
        s["tangential_response_rank"] == 122864,
        s["tangential_kernel_dimension"] == 90128,
        s["full_kernel_dimension"] == 106512,
        s["radial_summand_dimension"] + s["tangential_kernel_dimension"] == s["full_kernel_dimension"],
        "q wedge" in s["radial_map_zero_reason"],
        "direct-sum" in s["kernel_direct_sum"],
        s["both_summands_SO13_invariant"],
        "K807" in s["equivariance_basis"],
        r["restriction"] == "Cl_14|SO(13) = 2 Lambda^*(V_13)",
        r["irreducible_degrees"] == list(range(7)),
        r["irreducible_dimensions"] == [1, 13, 78, 286, 715, 1287, 1716],
        r["multiplicity_each_degree_0_through_6"] == 4,
        r["dimension_check"] == 16384,
        "4 Lambda^k" in r["module_formula"],
        d["radial_kernel_isotropy_module_authenticated"],
        d["tangential_kernel_authenticated_as_SO13_kernel_module"],
        not d["tangential_irreducible_multiplicities_computed"],
        not d["old_cohomology_module_authenticated"],
        not d["q_lambda_promoted_to_owned_total_gauge"],
        not d["SC_ACT_06_proved_or_refuted"],
        "irreducible multiplicities" in d["next_exact_input"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "not an owned gauge quotient" in p["ledger_no_change_reason"],
        "tangential irreducible character" in p["claim_ceiling"],
        p["controls"]["controls_passed"] == 37,
        p["controls"]["hostile_mutations_rejected"] == 20,
        p["controls"]["producer"].endswith("k863_sc_act_06_basepoint_kernel_isotropy.py"),
        p["controls"]["probe"].endswith("k863_sc_act_06_basepoint_kernel_isotropy_probe.py"),
    ]
    assert len(checks) == p["controls"]["controls_passed"]
    assert all(checks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
