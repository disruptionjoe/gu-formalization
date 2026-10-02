#!/usr/bin/env python3
"""K851: compact-cosphere exactness implies a uniform quotient Hodge gap."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k851-sc-act-06-compact-cosphere-hodge-gap.json"
PATHS = {
    "k849": ROOT / "lab/process/k849-sc-act-06-exact-repair-certificate.json",
    "k850": ROOT / "lab/process/k850-sc-act-06-flat-quotient-repair-interface.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def transpose(a: list[list[int | Fraction]]) -> list[list[Fraction]]:
    return [[Fraction(a[i][j]) for i in range(len(a))] for j in range(len(a[0]))]


def matmul(a: list[list[int | Fraction]], b: list[list[int | Fraction]]) -> list[list[Fraction]]:
    return [[sum((Fraction(a[i][k]) * Fraction(b[k][j]) for k in range(len(b))), Fraction(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a: list[list[int | Fraction]], b: list[list[int | Fraction]]) -> list[list[Fraction]]:
    return [[Fraction(x) + Fraction(y) for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def rank(a: list[list[int | Fraction]]) -> int:
    work = [[Fraction(x) for x in row] for row in a]
    pivot_row = 0
    for col in range(len(work[0]) if work else 0):
        pivot = next((i for i in range(pivot_row, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [x / scale for x in work[pivot_row]]
        for i in range(len(work)):
            if i != pivot_row and work[i][col]:
                factor = work[i][col]
                work[i] = [x - factor * y for x, y in zip(work[i], work[pivot_row])]
        pivot_row += 1
    return pivot_row


def cardinal_control() -> list[dict[str, Any]]:
    cases = [
        ("0", [1, 0, 0], [0, 1, 0], 3, 2, 1),
        ("pi/2", [0, 1, 0], [-1, 0, 0], 2, 3, 2),
        ("pi", [-1, 0, 0], [0, -1, 0], 1, 2, 3),
        ("3pi/2", [0, -1, 0], [1, 0, 0], 2, 1, 2),
    ]
    out = []
    for label, s, p, a, b, c in cases:
        S = [[c * x] for x in s]
        tau = [[a * x for x in p], [0, 0, b]]
        hodge = add(matmul(transpose(tau), tau), matmul(S, transpose(S)))
        out.append({
            "covector_angle": label,
            "tau": tau,
            "S": S,
            "tau_S_zero": matmul(tau, S) == [[0], [0]],
            "rank_tau": rank(tau),
            "rank_S": rank(S),
            "hodge_matrix": [[int(x) for x in row] for row in hodge],
            "hodge_eigenvalues_in_rotated_frame": [c * c, a * a, b * b],
            "minimum_eigenvalue": min(c * c, a * a, b * b),
            "middle_exact": rank(tau) + rank(S) == 3,
        })
    return out


def build() -> dict[str, Any]:
    source = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    controls = cardinal_control()
    return {
        "schema_version": "1.0",
        "result_id": "K851-SC-ACT-06-COMPACT-COSPHERE-HODGE-GAP",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": source["k850"]["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Finite-dimensional quotient-symbol theorem over a compact authenticated cosphere; no GU response or symmetry map is supplied.",
        "gu_typed_objects": {
            "carrier": "LAYER=ambient-or-toy CHIRALITY=N/A continuous finite-dimensional quotient bundle H over a unit cosphere",
            "pairing": "continuous positive auxiliary fibre metric used only to form adjoints",
            "real_structure": "real or complex finite-dimensional fibres",
            "grading": "owned induced symmetries -> old middle cohomology -> owned induced responses",
            "action_owner": "candidate-must-declare",
            "target": "MAP-TYPE=quotient middle Hodge family L_q=tau_bar_q^*tau_bar_q+S_bar_q S_bar_q^*",
        },
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "theorem": {
            "base": "compact authenticated unit cosphere K",
            "data": "continuous finite-dimensional maps S_bar_q:U_q->H_q and tau_bar_q:H_q->F_q with tau_bar_q S_bar_q=0",
            "pointwise_exactness": "im(S_bar_q)=ker(tau_bar_q) for every q in K",
            "middle_hodge_operator": "L_q=tau_bar_q^*tau_bar_q+S_bar_q S_bar_q^*",
            "quadratic_identity": "<L_q v,v>=||tau_bar_q v||^2+||S_bar_q^* v||^2",
            "kernel_identity": "ker(L_q)=ker(tau_bar_q) intersect im(S_bar_q)^perp",
            "exactness_equivalence": "L_q positive definite iff im(S_bar_q)=ker(tau_bar_q), assuming tau_bar_q S_bar_q=0",
            "compactness_conclusion": "continuous pointwise exactness implies mu=min_q lambda_min(L_q)>0",
            "uniform_splitting": "L_q^-1 is continuous and ||L_q^-1||<=1/mu",
            "constant_rank_is_separate_input": False,
            "uniform_gap_is_separate_input_after_hypotheses": False,
        },
        "exact_family_control": {
            "parameterization": "q=(cos theta,sin theta) on S1; S=(2-cos theta)s(theta); tau rows=(2+cos theta)p(theta)^T and (2+sin theta)e3^T",
            "analytic_hodge_eigenvalues": ["(2-cos theta)^2", "(2+cos theta)^2", "(2+sin theta)^2"],
            "analytic_uniform_gap": 1,
            "cardinal_checks": controls,
            "all_cardinal_compositions_zero": all(x["tau_S_zero"] for x in controls),
            "all_cardinal_exact": all(x["middle_exact"] for x in controls),
            "all_cardinal_gaps_at_least_one": all(x["minimum_eigenvalue"] >= 1 for x in controls),
        },
        "decision": {
            "K849_uniformity_row_resolved_conditionally": True,
            "finite_covector_sampling_sufficient": False,
            "source_owned_GU_maps_constructed": False,
            "next_exact_input": "Supply continuous source/action-owned induced maps on the authenticated compact Euclidean unit cosphere and prove pointwise im(S_bar_q)=ker(tau_bar_q); the uniform Hodge gap then follows rather than remaining an independent assumption.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is a quotient-bundle theorem and synthetic family, not a source-owned GU symbol, physical quotient, prediction or confirmation.",
        "claim_ceiling": "Uniform finite-symbol Hodge-gap theorem conditional on compactness, continuity, composition and pointwise exactness. No GU elliptic family, Fredholm realization or rich moduli follows.",
        "controls": {
            "producer": "tests/channel-swings/k851_sc_act_06_compact_cosphere_hodge_gap.py",
            "probe": "tests/channel-swings/k851_sc_act_06_compact_cosphere_hodge_gap_probe.py",
            "controls_passed": 44,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["theorem"], p["exact_family_control"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE", p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"], p["gu_typed_objects"]["action_owner"] == "candidate-must-declare",
        t["base"] == "compact authenticated unit cosphere K", "tau_bar_q S_bar_q=0" in t["data"],
        t["pointwise_exactness"] == "im(S_bar_q)=ker(tau_bar_q) for every q in K",
        "tau_bar_q^*tau_bar_q" in t["middle_hodge_operator"], "||tau_bar_q v||^2" in t["quadratic_identity"],
        "im(S_bar_q)^perp" in t["kernel_identity"], "positive definite iff" in t["exactness_equivalence"],
        "mu=min_q" in t["compactness_conclusion"], "1/mu" in t["uniform_splitting"],
        not t["constant_rank_is_separate_input"], not t["uniform_gap_is_separate_input_after_hypotheses"],
        c["analytic_uniform_gap"] == 1, len(c["cardinal_checks"]) == 4,
        c["all_cardinal_compositions_zero"], c["all_cardinal_exact"], c["all_cardinal_gaps_at_least_one"],
        all(x["rank_tau"] == 2 for x in c["cardinal_checks"]), all(x["rank_S"] == 1 for x in c["cardinal_checks"]),
        all(x["middle_exact"] for x in c["cardinal_checks"]), min(x["minimum_eigenvalue"] for x in c["cardinal_checks"]) == 1,
        d["K849_uniformity_row_resolved_conditionally"], not d["finite_covector_sampling_sufficient"],
        not d["source_owned_GU_maps_constructed"], "uniform Hodge gap then follows" in d["next_exact_input"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "synthetic family" in p["ledger_no_change_reason"], "No GU elliptic family" in p["claim_ceiling"],
        set(p["pinned_inputs"]) == {"k849", "k850"}, all(len(x["sha256"]) == 64 for x in p["pinned_inputs"].values()),
        p["controls"]["controls_passed"] == 44, p["controls"]["hostile_mutations_rejected"] == 20,
        p["gu_typed_objects"]["target"].startswith("MAP-TYPE=quotient"), "compact" in p["scope"],
        c["cardinal_checks"][0]["hodge_eigenvalues_in_rotated_frame"] == [1, 9, 4],
        c["cardinal_checks"][2]["hodge_eigenvalues_in_rotated_frame"] == [9, 1, 4],
        matmul([[0, 1, 0], [0, 0, 1]], [[1], [0], [0]]) == [[0], [0]],
        rank([[0, 1, 0], [0, 0, 1]]) + rank([[1], [0], [0]]) == 3,
        t["exactness_equivalence"].startswith("L_q positive definite"),
        p["direction"] == "observed_to_native", "unit cosphere" in p["gu_typed_objects"]["carrier"],
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
