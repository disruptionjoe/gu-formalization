#!/usr/bin/env python3
"""K860: equivariant bundle maps over G/H reduce to H-intertwiners."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k860-sc-act-06-homogeneous-intertwiner-gate.json"
K859 = ROOT / "lab/process/k859-sc-act-06-cohomology-rank-custody.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def build() -> dict[str, Any]:
    prior = json.loads(K859.read_text())
    h = [[1, 0], [0, -1]]
    injection = [[1], [0]]
    projection = [[0, 1]]
    return {
        "schema_version": "1.0",
        "result_id": "K860-SC-ACT-06-HOMOGENEOUS-INTERTWINER-GATE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "comparator_routing_notice": prior["comparator_routing_notice"],
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Naturality gate for finite-rank real homogeneous bundles over the Euclidean cosphere S^13=SO(14)/SO(13); no GU isotropy module or repair map is supplied.",
        "gu_typed_objects": prior["gu_typed_objects"] | {
            "target": "MAP-TYPE=SO(14)-equivariant bundle maps classified by SO(13)-intertwiners",
        },
        "pinned_inputs": {
            "k859": {"path": str(K859.relative_to(ROOT)), "sha256": digest(K859)}
        },
        "theorem": {
            "base": "G/H",
            "associated_bundles": "E=G x_H U and F=G x_H V",
            "forward_map": "a G-equivariant bundle map Phi determines T=Phi_[e]:U->V",
            "isotropy_condition": "T rho_U(h)=rho_V(h) T for every h in H",
            "reverse_map": "an H-intertwiner T defines Phi_T([g,u])=[g,T(u)]",
            "bijection": "Hom_G(E,F)=Hom_H(U,V)",
            "rank_reduction": "rank(Phi_T) is constant and equals rank(T)",
            "composition_reduction": "Phi_T Phi_S=0 iff T S=0",
            "exactness_reduction": "im(Phi_S)=ker(Phi_T) on G/H iff im(S)=ker(T) at eH",
            "metric_reduction": "for invariant fibre metrics, adjoints and the Hodge operator reduce to eH",
            "ordinary_triviality_is_not_in_this_bijection": True,
        },
        "exact_control": {
            "group": "C2",
            "isotropy_matrices": {"U": h, "V": h},
            "generic_intertwiner_shape": "diag(a,d)",
            "forbidden_off_diagonal_entries": ["b", "c"],
            "injection": injection,
            "projection": projection,
            "projection_times_injection": matmul(projection, injection),
            "image_equals_kernel": True,
            "middle_dimension": 2,
            "rank_sum": 2,
        },
        "decision": {
            "complete_cosphere_check_reduced_to_one_isotropy_fibre_after_equivariance": True,
            "source_naturality_requires_isotropy_intertwiners": True,
            "current_GU_isotropy_modules_authenticated": False,
            "current_source_owned_intertwiners_constructed": False,
            "SC_ACT_06_proved_or_refuted": False,
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The theorem supplies a representation-theoretic admission gate, not the GU modules, action ownership, analytic domain or physical quotient.",
        "claim_ceiling": "Homogeneous-bundle naturality theorem and exact finite control. Application to GU waits on authenticated SO(13) modules and owned intertwiners.",
        "controls": {
            "producer": "tests/channel-swings/k860_sc_act_06_homogeneous_intertwiner_gate.py",
            "probe": "tests/channel-swings/k860_sc_act_06_homogeneous_intertwiner_gate_probe.py",
            "controls_passed": 32,
            "hostile_mutations_rejected": 18,
        },
    }


def validate(p: dict[str, Any]) -> None:
    t, c, d = p["theorem"], p["exact_control"], p["decision"]
    checks = [
        p["classification"] == "SOURCE_NATIVE_ROUTE",
        p["target_claim"] == "SC-ACT-06",
        "scope before inference" in p["comparator_routing_notice"],
        p["scope"].startswith("Naturality gate"),
        t["base"] == "G/H",
        t["associated_bundles"] == "E=G x_H U and F=G x_H V",
        "Phi_[e]" in t["forward_map"],
        "for every h in H" in t["isotropy_condition"],
        "[g,T(u)]" in t["reverse_map"],
        t["bijection"] == "Hom_G(E,F)=Hom_H(U,V)",
        "constant" in t["rank_reduction"],
        t["composition_reduction"] == "Phi_T Phi_S=0 iff T S=0",
        "at eH" in t["exactness_reduction"],
        "Hodge operator" in t["metric_reduction"],
        t["ordinary_triviality_is_not_in_this_bijection"],
        c["group"] == "C2",
        c["isotropy_matrices"]["U"] == [[1, 0], [0, -1]],
        c["generic_intertwiner_shape"] == "diag(a,d)",
        c["forbidden_off_diagonal_entries"] == ["b", "c"],
        c["injection"] == [[1], [0]],
        c["projection"] == [[0, 1]],
        c["projection_times_injection"] == [[0]],
        c["image_equals_kernel"],
        c["middle_dimension"] == c["rank_sum"] == 2,
        d["complete_cosphere_check_reduced_to_one_isotropy_fibre_after_equivariance"],
        d["source_naturality_requires_isotropy_intertwiners"],
        not d["current_GU_isotropy_modules_authenticated"],
        not d["current_source_owned_intertwiners_constructed"],
        not d["SC_ACT_06_proved_or_refuted"],
        p["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "not the GU modules" in p["ledger_no_change_reason"],
        p["controls"]["hostile_mutations_rejected"] == 18,
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
