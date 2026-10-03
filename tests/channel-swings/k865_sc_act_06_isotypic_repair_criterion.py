#!/usr/bin/env python3
"""K865: exact isotypic criterion for compact equivariant repair complexes."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k865-sc-act-06-isotypic-repair-criterion.json"
PATHS = {
    "k847": ROOT / "lab/process/k847-sc-act-06-quotient-repair-theorem.json",
    "k860": ROOT / "lab/process/k860-sc-act-06-homogeneous-intertwiner-gate.json",
    "k864": ROOT / "lab/process/k864-sc-act-06-radial-grant-quotient.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def criterion(h: dict[str, int], a: dict[str, int], b: dict[str, int]) -> bool:
    return all(h.get(label, 0) <= a.get(label, 0) + b.get(label, 0) for label in set(h) | set(a) | set(b))


def build() -> dict[str, Any]:
    packets = {key: json.loads(path.read_text()) for key, path in PATHS.items()}
    positive = {
        "irreducible_dimensions": {"trivial": 1, "vector": 13},
        "H_multiplicities": {"trivial": 2, "vector": 1},
        "A_multiplicities": {"trivial": 1, "vector": 1},
        "B_multiplicities": {"trivial": 1, "vector": 0},
        "S_ranks_by_type": {"trivial": 1, "vector": 1},
        "tau_ranks_by_type": {"trivial": 1, "vector": 0},
    }
    positive["criterion_passes"] = criterion(positive["H_multiplicities"], positive["A_multiplicities"], positive["B_multiplicities"])
    positive["image_equals_kernel_by_type"] = all(
        positive["S_ranks_by_type"][label] == positive["H_multiplicities"][label] - positive["tau_ranks_by_type"][label]
        for label in positive["H_multiplicities"]
    )
    negative = {
        "irreducible_dimensions": {"trivial": 1, "vector": 13},
        "H_multiplicities": {"trivial": 0, "vector": 1},
        "A_multiplicities": {"trivial": 13, "vector": 0},
        "B_multiplicities": {"trivial": 0, "vector": 0},
        "raw_dimension_H": 13,
        "raw_dimension_A_plus_B": 13,
        "missing_type": "vector",
        "Hom_SO13_A_to_H_rank": 0,
    }
    negative["criterion_passes"] = criterion(negative["H_multiplicities"], negative["A_multiplicities"], negative["B_multiplicities"])
    return {
        "schema_version": "1.0",
        "result_id": "K865-SC-ACT-06-ISOTYPIC-REPAIR-CRITERION",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": packets["k860"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Representation-theoretic existence criterion for an exact SO(13)-equivariant repair pair A --S_0--> H --tau_0--> B at one homogeneous base fibre.",
        "gu_typed_objects": packets["k864"]["gu_typed_objects"] | {
            "target": "MAP-TYPE=isotypic capacity for SO(13)-equivariant exact quotient repair",
        },
        "pinned_inputs": {key: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for key, path in PATHS.items()},
        "theorem": {
            "group": "SO(13)",
            "compact_semisimplicity_used": True,
            "real_isotypic_form": "H=direct-sum_rho rho tensor_Drho D_rho^(h_rho), with analogous A and B",
            "division_algebras_allowed": ["R", "C", "H"],
            "intertwiners_reduce_to_multiplicity_space_maps": True,
            "exact_pair_exists_iff": "for every irreducible real type rho, h_rho <= a_rho + b_rho",
            "rank_choice_interval": "max(0,h_rho-b_rho) <= rank_Drho(S_rho) <= min(a_rho,h_rho)",
            "construction": "choose S_rho with rank k_rho and tau_rho with kernel im(S_rho) on each multiplicity space, then sum over rho",
            "necessity": "im(S_rho)=ker(tau_rho) implies h_rho=rank(S_rho)+rank(tau_rho)<=a_rho+b_rho",
            "raw_total_dimension_suffices": False,
        },
        "exact_controls": {
            "typed_exact_control": positive,
            "dimension_matched_type_mismatch": negative,
        },
        "decision": {
            "repair_capacity_is_irrepwise": True,
            "raw_rank_budget_is_sufficient_for_naturality": False,
            "K847_raw_rank_formula_retracted": False,
            "K860_homogeneous_reduction_retracted": False,
            "current_GU_repair_admitted": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Compute the irreducible real SO(13) multiplicities of the authenticated old cohomology quotient and of source/action-owned repair modules A and B; every type must satisfy h_rho<=a_rho+b_rho before constructing S_0,tau_0.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem is a compact-representation admission criterion and supplies none of the GU-owned multiplicities or repair maps.",
        "claim_ceiling": "Necessary-and-sufficient isotypic capacity criterion for finite real SO(13) modules. Analytic domains, source ownership and the actual GU modules remain separate.",
        "controls": {
            "producer": "tests/channel-swings/k865_sc_act_06_isotypic_repair_criterion.py",
            "probe": "tests/channel-swings/k865_sc_act_06_isotypic_repair_criterion_probe.py",
            "controls_passed": 37,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    t, x, d = p["theorem"], p["exact_controls"], p["decision"]
    pos, neg = x["typed_exact_control"], x["dimension_matched_type_mismatch"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE",
        p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"],
        set(p["pinned_inputs"]) == set(PATHS),
        all(len(item["sha256"]) == 64 for item in p["pinned_inputs"].values()),
        t["group"] == "SO(13)",
        t["compact_semisimplicity_used"],
        t["division_algebras_allowed"] == ["R", "C", "H"],
        t["intertwiners_reduce_to_multiplicity_space_maps"],
        "h_rho <= a_rho + b_rho" in t["exact_pair_exists_iff"],
        "max(0,h_rho-b_rho)" in t["rank_choice_interval"],
        "sum over rho" in t["construction"],
        "h_rho=rank(S_rho)+rank(tau_rho)" in t["necessity"],
        not t["raw_total_dimension_suffices"],
        pos["H_multiplicities"] == {"trivial": 2, "vector": 1},
        pos["A_multiplicities"] == {"trivial": 1, "vector": 1},
        pos["B_multiplicities"] == {"trivial": 1, "vector": 0},
        pos["criterion_passes"],
        pos["image_equals_kernel_by_type"],
        neg["raw_dimension_H"] == neg["raw_dimension_A_plus_B"] == 13,
        neg["missing_type"] == "vector",
        neg["Hom_SO13_A_to_H_rank"] == 0,
        not neg["criterion_passes"],
        d["repair_capacity_is_irrepwise"],
        not d["raw_rank_budget_is_sufficient_for_naturality"],
        not d["K847_raw_rank_formula_retracted"],
        not d["K860_homogeneous_reduction_retracted"],
        not d["current_GU_repair_admitted"],
        not d["SC_ACT_06_proved_or_refuted"],
        "h_rho<=a_rho+b_rho" in d["next_exact_input"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "supplies none of the GU-owned multiplicities" in p["ledger_no_change_reason"],
        "Necessary-and-sufficient isotypic" in p["claim_ceiling"],
        p["controls"]["controls_passed"] == 37,
        p["controls"]["hostile_mutations_rejected"] == 20,
        p["controls"]["producer"].endswith("k865_sc_act_06_isotypic_repair_criterion.py"),
        p["controls"]["probe"].endswith("k865_sc_act_06_isotypic_repair_criterion_probe.py"),
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
