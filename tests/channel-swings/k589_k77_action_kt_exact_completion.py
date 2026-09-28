#!/usr/bin/env python3
"""K589: complete K588 with the source-owned stabilizer inclusion."""

from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k589-k77-action-kt-exact-completion.json"
K588_PATH = Path(__file__).with_name("k588_k77_action_orbit_reduction.py")


def load_k588():
    spec = importlib.util.spec_from_file_location("k588_for_k589", K588_PATH)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


def build() -> dict[str, Any]:
    k588 = load_k588()
    data = k588.construct()
    d1 = data["induced"]
    _, d2, stabilizer, complement = k588.orbit_maps()
    kernel = sp.Matrix.hstack(*d1.nullspace())
    payload = {
        "schema_version": "1.0",
        "result_id": "K589-K77-ACTION-KT-EXACT-COMPLETION",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "scope": "Exact finite completion of K588's induced action-orbit arrow by the independently source-owned odd-odd stabilizer inclusion. It is the homogeneous-orbit coefficient complex coupled to the selected Hessian embedding, not a full interacting functional BV/KT complex.",
        "gu_typed_objects": {
            "degree_two": "H^21 odd-odd so(3,4) stabilizer relations",
            "degree_one": "Q^91 labelled primitive epsilon variations",
            "degree_zero": "M^70 selected orbit-complement tangent",
            "D2": "canonical stabilizer inclusion H^21->Q^91",
            "D1": "K588 induced action-orbit quotient LB=A:Q^91->M^70",
            "MAP-TYPE": "exact finite homogeneous-orbit KT completion",
            "LAYER": "source-owned orbit reducibility plus selected first-action tangent coupling",
            "CHIRALITY": "N/A",
        },
        "source_and_ledger_context": {
            "source_claims": ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"],
            "source_polarity_effect": "none",
            "physics_rows": ["LT-SM8", "LT-GR6b", "RA-F1", "AC-F1"],
            "ledger": "lab/process/conditional-physics-ledger-v0.263.json",
            "ledger_effect": "none",
            "reduction_input": "lab/process/k588-k77-action-orbit-reduction.json",
            "stabilizer_input": "lab/process/selected-k77-stabilizer-koszul-tate-resolution-gate.json",
        },
        "preflight_bookend": {
            "route_comparison": "Use the source-owned stabilizer inclusion already paired with the orbit quotient; an arbitrary basis of ker(D1) would prove existence but lose the epsilon/stabilizer interpretation.",
            "retrieval_collision_result": "The stabilizer gate owns D2 and K588 owns D1=LB; no predecessor verifies their coefficient-level composition after action coupling.",
            "strongest_alternative": "A nullspace-generated D2 is algebraically sufficient but not independently source-owned and is retained only as a basis comparison.",
        },
        "exact_completion": {
            "dimensions": [21, 91, 70],
            "D2_shape": [d2.rows, d2.cols],
            "D2_rank": int(d2.rank()),
            "D2_nonzero_entries": len(d2.todok()),
            "D1_shape": [d1.rows, d1.cols],
            "D1_rank": int(d1.rank()),
            "D1_nonzero_entries": len(d1.todok()),
            "D1_D2_zero": d1 * d2 == sp.zeros(70, 21),
            "kernel_D1_dimension": len(d1.nullspace()),
            "image_D2_dimension": int(d2.rank()),
            "kernel_D1_equals_image_D2": kernel.columnspace() == d2.columnspace(),
            "homology_dimensions": [21 - int(d2.rank()), 91 - int(d2.rank()) - int(d1.rank()), 70 - int(d1.rank())],
            "euler_characteristic": 21 - 91 + 70,
            "stabilizer_pairs": [list(pair) for pair in stabilizer],
            "complement_pair_count": len(complement),
            "higher_linear_reducibility": 0,
        },
        "ownership_boundary": {
            "D2_source_owned_by_epsilon_orbit_stabilizer": True,
            "D1_action_coupled_through_K588": True,
            "finite_homogeneous_orbit_exactness": True,
            "nonlinear_functional_KT_properness": False,
            "physical_cohomology_constructed": False,
        },
        "decision": {
            "K587_rank21_adjacent_arrow_constructed": True,
            "K587_base_exact_completion_constructed": True,
            "selected_source_action_rejected": False,
            "next_exact_input": "Tensor D2 and D1 with the corrected rank-512 carrier identity and verify both moving source/target K444 projector squares and product ranks.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling finite homogeneous-orbit exactness a nonlinear functional BV/KT properness theorem or physical cohomology computation.",
            "strongest_contrary_construction": "The same finite ranks can fail away from the selected orbit-type stratum; K425 proves transverse behavior is not identified by frozen data.",
            "weakest_reproducibility_seam": "The labelled odd-odd/complement basis is canonical only relative to the selected coordinate axes already fixed by the stabilizer gate.",
        },
        "controls": {
            "producer": "tests/channel-swings/k589_k77_action_kt_exact_completion.py",
            "probe": "tests/channel-swings/k589_k77_action_kt_exact_completion_probe.py",
        },
        "claim_ceiling": "Exact coefficient-level finite completion 0->H^21->Q^91->M^70->0: the source-owned odd-odd stabilizer inclusion has rank 21, K588's induced action-orbit quotient has rank 70, their composition vanishes and im(D2)=ker(D1). This closes K587's base coefficient interface on the selected homogeneous orbit. It does not prove nonlinear/global functional properness, supply the corrected-carrier action, construct physical cohomology, or move any source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }
    validate(payload)
    return payload


def validate(payload: dict[str, Any]) -> None:
    exact = payload["exact_completion"]
    boundary = payload["ownership_boundary"]
    decision = payload["decision"]
    if exact["dimensions"] != [21, 91, 70] or exact["D2_rank"] != 21 or exact["D1_rank"] != 70:
        raise AssertionError("K589 rank profile failed")
    if not exact["D1_D2_zero"] or not exact["kernel_D1_equals_image_D2"]:
        raise AssertionError("K589 exactness failed")
    if exact["homology_dimensions"] != [0, 0, 0] or exact["euler_characteristic"] != 0:
        raise AssertionError("K589 homology failed")
    if not boundary["D2_source_owned_by_epsilon_orbit_stabilizer"] or not boundary["D1_action_coupled_through_K588"]:
        raise AssertionError("K589 ownership failed")
    if boundary["nonlinear_functional_KT_properness"] or boundary["physical_cohomology_constructed"]:
        raise AssertionError("K589 overclaimed")
    if not decision["K587_rank21_adjacent_arrow_constructed"] or not decision["K587_base_exact_completion_constructed"] or decision["selected_source_action_rejected"]:
        raise AssertionError("K589 decision changed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
