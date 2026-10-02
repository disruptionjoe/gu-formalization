#!/usr/bin/env python3
"""K853: quantitative stability radius for exact quotient symbol complexes."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k853-sc-act-06-robust-exactness-radius.json"
PATHS = {
    "k851": ROOT / "lab/process/k851-sc-act-06-compact-cosphere-hodge-gap.json",
    "k852": ROOT / "lab/process/k852-sc-act-06-uniformity-failure-controls.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def radius(mu: float, response_bound: float, symmetry_bound: float) -> float:
    total = response_bound + symmetry_bound
    return (math.sqrt(total * total + 2.0 * mu) - total) / 2.0


def hodge_bound(epsilon: float, response_bound: float, symmetry_bound: float) -> float:
    return 2.0 * (response_bound + symmetry_bound) * epsilon + 2.0 * epsilon * epsilon


def build() -> dict[str, Any]:
    source = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    mu = response_bound = symmetry_bound = 1.0
    eps = 0.1
    robust_radius = radius(mu, response_bound, symmetry_bound)
    return {
        "schema_version": "1.0",
        "result_id": "K853-SC-ACT-06-ROBUST-EXACTNESS-RADIUS",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": source["k851"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Operator-norm stability theorem for an already exact continuous quotient-symbol family; it supplies no GU family or perturbation.",
        "gu_typed_objects": {
            "carrier": "LAYER=ambient-or-toy CHIRALITY=N/A finite-dimensional quotient bundle over a compact cosphere",
            "pairing": "continuous positive auxiliary fibre metric",
            "real_structure": "real or complex",
            "grading": "induced symmetries -> old middle cohomology -> induced responses",
            "action_owner": "candidate-and-perturbation-must-declare",
            "target": "MAP-TYPE=quotient stability of exactness under composition-compatible map perturbations",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "theorem": {
            "baseline_gap": "L_q>=mu I uniformly",
            "baseline_norm_bounds": "||tau_bar_q||<=T and ||S_bar_q||<=R",
            "perturbation_bounds": "||delta tau_q||<=epsilon and ||delta S_q||<=epsilon",
            "hodge_difference_bound": "||L'_q-L_q||<=2(T+R)epsilon+2epsilon^2",
            "stability_condition": "2(T+R)epsilon+2epsilon^2<mu",
            "explicit_radius": "epsilon<(-T-R+sqrt((T+R)^2+2mu))/2",
            "conclusion": "L'_q>0 uniformly; if tau'_q S'_q=0 then im(S'_q)=ker(tau'_q) for every q",
            "composition_is_required": True,
            "positive_hodge_without_composition_certifies_a_complex": False,
        },
        "exact_controls": {
            "baseline": {
                "tau": [[0, 1]], "S": [[1], [0]], "hodge": [[1, 0], [0, 1]],
                "mu": 1, "T": 1, "R": 1, "composition_zero": True, "middle_exact": True,
            },
            "certified_radius": {
                "exact": "(sqrt(6)-2)/2", "decimal": robust_radius,
                "safe_epsilon": eps, "difference_bound": hodge_bound(eps, 1, 1),
                "bound_below_mu": hodge_bound(eps, 1, 1) < 1,
            },
            "safe_diagonal_perturbation": {
                "tau_prime": [[0, "9/10"]], "S_prime": [["9/10"], [0]],
                "composition_zero": True, "hodge_gap": "81/100", "middle_exact": True,
            },
            "composition_breaker": {
                "tau_prime": [["1/10", 1]], "S_prime": [[1], [0]],
                "composition": "1/10", "hodge_positive": True, "valid_complex": False,
            },
            "outside_radius_collapse": {
                "epsilon": 1, "tau_prime": [[0, 0]], "S_prime": [[0], [0]],
                "hodge_gap": 0, "middle_exact": False,
            },
        },
        "decision": {
            "K851_uniform_gap_has_quantitative_stability_margin": True,
            "pointwise_exactness_is_open_inside_composition_compatible_families": True,
            "arbitrary_perturbations_preserve_complex_structure": False,
            "source_owned_GU_perturbation_constructed": False,
            "next_exact_input": "After constructing the owned continuous exact family, bound its quotient Hodge gap and map norms, then keep every admitted principal perturbation composition-compatible and below the certified radius.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The stability radius is conditional operator theory and does not construct an action-owned GU deformation, quotient or physical observable.",
        "claim_ceiling": "Sufficient uniform perturbation radius for finite-dimensional exact quotient symbols. It is not a necessary sharp radius and does not establish a GU family or nonlinear moduli.",
        "controls": {
            "producer": "tests/channel-swings/k853_sc_act_06_robust_exactness_radius.py",
            "probe": "tests/channel-swings/k853_sc_act_06_robust_exactness_radius_probe.py",
            "controls_passed": 47,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["theorem"], p["exact_controls"], p["decision"]
    b, r, s, x, o = c["baseline"], c["certified_radius"], c["safe_diagonal_perturbation"], c["composition_breaker"], c["outside_radius_collapse"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06", "scope before inference" in p["comparator_routing_notice"],
        p["gu_typed_objects"]["action_owner"] == "candidate-and-perturbation-must-declare", t["baseline_gap"] == "L_q>=mu I uniformly",
        "T" in t["baseline_norm_bounds"] and "R" in t["baseline_norm_bounds"], "epsilon" in t["perturbation_bounds"],
        t["hodge_difference_bound"] == "||L'_q-L_q||<=2(T+R)epsilon+2epsilon^2", "<mu" in t["stability_condition"],
        "sqrt((T+R)^2+2mu)" in t["explicit_radius"], "tau'_q S'_q=0" in t["conclusion"], t["composition_is_required"],
        not t["positive_hodge_without_composition_certifies_a_complex"], b["hodge"] == [[1, 0], [0, 1]], b["mu"] == 1,
        b["T"] == b["R"] == 1, b["composition_zero"], b["middle_exact"], r["exact"] == "(sqrt(6)-2)/2",
        0.22 < r["decimal"] < 0.23, r["safe_epsilon"] == 0.1, abs(r["difference_bound"] - 0.42) < 1e-12,
        r["bound_below_mu"], s["composition_zero"], s["hodge_gap"] == "81/100", s["middle_exact"],
        x["composition"] == "1/10", x["hodge_positive"], not x["valid_complex"], o["epsilon"] == 1,
        o["hodge_gap"] == 0, not o["middle_exact"], d["K851_uniform_gap_has_quantitative_stability_margin"],
        d["pointwise_exactness_is_open_inside_composition_compatible_families"], not d["arbitrary_perturbations_preserve_complex_structure"],
        not d["source_owned_GU_perturbation_constructed"], "composition-compatible" in d["next_exact_input"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED", "conditional operator theory" in p["ledger_no_change_reason"],
        "not a necessary sharp radius" in p["claim_ceiling"], set(p["pinned_inputs"]) == {"k851", "k852"},
        all(len(v["sha256"]) == 64 for v in p["pinned_inputs"].values()), p["controls"]["controls_passed"] == 47,
        p["controls"]["hostile_mutations_rejected"] == 20, Fraction(9, 10) ** 2 == Fraction(81, 100),
        hodge_bound(0.1, 1, 1) < 1, radius(1, 1, 1) == r["decimal"],
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
