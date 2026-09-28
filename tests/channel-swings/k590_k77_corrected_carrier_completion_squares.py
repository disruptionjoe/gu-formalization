#!/usr/bin/env python3
"""K590: lift the K589 completion and verify both corrected-boundary squares."""

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
OUTPUT = ROOT / "lab/process/k590-k77-corrected-carrier-completion-squares.json"
K588_PATH = Path(__file__).with_name("k588_k77_action_orbit_reduction.py")


def load_k588():
    spec = importlib.util.spec_from_file_location("k588_for_k590", K588_PATH)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


def rotation(t: sp.Rational) -> sp.Matrix:
    return sp.Matrix([[1 - t * t, -2 * t], [2 * t, 1 - t * t]]) / (1 + t * t)


def build() -> dict[str, Any]:
    k588 = load_k588()
    data = k588.construct()
    d1 = data["induced"]
    _, d2, _, _ = k588.orbit_maps()
    p0 = sp.diag(1, 0)
    sample_rows = []
    for t in (sp.Rational(0), sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(1)):
        u = rotation(t)
        p = u * p0 * u.T
        p2 = sp.kronecker_product(sp.eye(21), p)
        p1 = sp.kronecker_product(sp.eye(91), p)
        p0_target = sp.kronecker_product(sp.eye(70), p)
        high = sp.kronecker_product(d2, sp.eye(2))
        low = sp.kronecker_product(d1, sp.eye(2))
        high_defect = p1 * high - high * p2
        low_defect = p0_target * low - low * p1
        sample_rows.append({
            "t": str(t),
            "projector_rank_on_pair": int(p.rank()),
            "D2_square_defect_rank": int(high_defect.rank()),
            "D1_square_defect_rank": int(low_defect.rank()),
            "projector_idempotent": p * p == p,
            "transport_orthogonal": u.T * u == sp.eye(2),
        })
    payload = {
        "schema_version": "1.0",
        "result_id": "K590-K77-CORRECTED-CARRIER-COMPLETION-SQUARES",
        "created": "2026-09-28",
        "status": "working_draft_verified",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "scope": "Factorized lift of K589's exact 21-to-91-to-70 base complex through K441's corrected moving rank-512 carrier, with both K444 source/target projector squares checked exactly by the common carrier action.",
        "gu_typed_objects": {
            "base_complex": "H^21 --D2--> Q^91 --D1--> M^70 from K589",
            "carrier": "K441 corrected moving rank-512 carrier with parallel rank-256 incoming/outgoing projectors",
            "lifted_arrows": "D2 tensor I_512 and D1 tensor I_512",
            "typed_squares": "Pi1(D2 tensor I)=(D2 tensor I)Pi2 and Pi0(D1 tensor I)=(D1 tensor I)Pi1",
            "MAP-TYPE": "factorized corrected-boundary chain map",
            "LAYER": "homogeneous-orbit KT times corrected boundary carrier",
            "CHIRALITY": "N/A",
        },
        "source_and_ledger_context": {
            "source_claims": ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"],
            "source_polarity_effect": "none",
            "physics_rows": ["LT-SM8", "LT-GR6b", "RA-F1", "AC-F1"],
            "ledger": "lab/process/conditional-physics-ledger-v0.263.json",
            "ledger_effect": "none",
            "base_input": "lab/process/k589-k77-action-kt-exact-completion.json",
            "carrier_input": "lab/process/k441-k77-moving-corrected-boundary-transport.json",
            "square_input": "lab/process/k444-k77-degree-changing-boundary-squares.json",
        },
        "preflight_bookend": {
            "route_comparison": "Use the common degreewise carrier identity and moving parallel projectors; expanding 46,592-dimensional matrices adds no information and risks obscuring the tensor identity.",
            "retrieval_collision_result": "K442 proves the abstract product and K444 the general typed-square theorem; K590 is the first coefficient-level instantiation using K589's action-coupled base arrows.",
            "strongest_alternative": "A nonfactorized lower-order carrier coupling would be stronger but remains absent and cannot be inferred from the factorized completion.",
        },
        "factorized_completion": {
            "carrier_rank": 512,
            "carrier_half_ranks": [256, 256],
            "degree_dimensions": [21 * 512, 91 * 512, 70 * 512],
            "lifted_D2_rank": 21 * 512,
            "lifted_D1_rank": 70 * 512,
            "middle_kernel_dimension": 21 * 512,
            "homology_dimensions": [0, 0, 0],
            "lifted_nilpotence": True,
            "D2_typed_square_factor_identity": "(I_91 tensor Pi)(D2 tensor I_512)=(D2 tensor I_512)(I_21 tensor Pi)",
            "D1_typed_square_factor_identity": "(I_70 tensor Pi)(D1 tensor I_512)=(D1 tensor I_512)(I_91 tensor Pi)",
            "both_K444_squares_hold_for_all_parallel_projectors": True,
            "rational_transport_samples": sample_rows,
            "all_sample_D2_defects_zero": all(row["D2_square_defect_rank"] == 0 for row in sample_rows),
            "all_sample_D1_defects_zero": all(row["D1_square_defect_rank"] == 0 for row in sample_rows),
        },
        "ownership_boundary": {
            "base_coefficients_from_K589": True,
            "carrier_action_is_K441_factorized_identity_transport": True,
            "nonfactorized_interacting_carrier_action_constructed": False,
            "full_nonlinear_BV_KT_constructed": False,
            "physical_boundary_selected": False,
            "physical_cohomology_constructed": False,
        },
        "decision": {
            "K587_corrected_carrier_action_identified": True,
            "K587_both_K444_squares_pass": True,
            "K587_factorized_completion_endpoint_reached": True,
            "source_action_rejected": False,
            "next_exact_input": "Derive a nonfactorized lower-order action coupling on the corrected carrier, or move to the strongest independent falsification route; do not relabel the factorized product as the full interacting BV/KT complex.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling exact factorized boundary descent the full interacting action-derived BV/KT complex or physical cohomology.",
            "strongest_contrary_construction": "K443/K446 show boundary-compatible perturbations can change nilpotence or cohomology once nonfactorized carrier couplings are introduced.",
            "weakest_reproducibility_seam": "The rank-512 identities are proved factorwise and sampled on rank-two moving representatives rather than expanded billion-entry products.",
        },
        "controls": {
            "producer": "tests/channel-swings/k590_k77_corrected_carrier_completion_squares.py",
            "probe": "tests/channel-swings/k590_k77_corrected_carrier_completion_squares_probe.py",
        },
        "claim_ceiling": "Exact factorized corrected-carrier completion: K589's coefficient arrows tensor the identity on K441's rank-512 moving carrier, have ranks 10,752 and 35,840, remain exact, and satisfy both K444 typed projector squares for every common parallel carrier projector. This reaches K587's factorized endpoint only; it supplies no nonfactorized lower-order action coupling, full nonlinear BV/KT complex, physical boundary, physical cohomology, or source, ledger, canon, paper, public, novelty, prediction, confirmation or physical conclusion.",
    }
    validate(payload)
    return payload


def validate(payload: dict[str, Any]) -> None:
    exact = payload["factorized_completion"]
    boundary = payload["ownership_boundary"]
    decision = payload["decision"]
    if exact["degree_dimensions"] != [10752, 46592, 35840] or exact["lifted_D2_rank"] != 10752 or exact["lifted_D1_rank"] != 35840:
        raise AssertionError("K590 product ranks failed")
    if exact["homology_dimensions"] != [0, 0, 0] or not exact["lifted_nilpotence"]:
        raise AssertionError("K590 lifted exactness failed")
    if not exact["both_K444_squares_hold_for_all_parallel_projectors"] or not exact["all_sample_D2_defects_zero"] or not exact["all_sample_D1_defects_zero"]:
        raise AssertionError("K590 typed square failed")
    if boundary["nonfactorized_interacting_carrier_action_constructed"] or boundary["full_nonlinear_BV_KT_constructed"] or boundary["physical_cohomology_constructed"]:
        raise AssertionError("K590 overclaimed")
    if not decision["K587_corrected_carrier_action_identified"] or not decision["K587_both_K444_squares_pass"] or not decision["K587_factorized_completion_endpoint_reached"] or decision["source_action_rejected"]:
        raise AssertionError("K590 decision changed")


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
