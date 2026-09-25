#!/usr/bin/env python3
"""K489 native Neumann-word M-orthogonalization.

For a zero-bath K162 seed ``phi`` let ``v_n = G^n phi`` and
``S = (1-G)^-1``.  K170 proves that the ``v_n`` occupy mutually orthogonal
bath-number sectors.  This makes the physical Gram on ``(phi, G phi)``
exactly computable from ``B = sum_(n>=1) ||v_n||^2`` and exposes the corrected
M-orthogonal first-tail direction.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = ROOT / "lab/process/k489-native-neumann-word-m-orthogonalization.json"


def load_k170():
    path = HERE / "k170_direct_gram_reference_shape_slice.py"
    spec = importlib.util.spec_from_file_location("k170_for_k489", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K170 = load_k170()


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sector_bounds(charge: tuple[int, int], multiplicity: int) -> dict[str, Any]:
    one_lower, one_upper = K170.point_profile_norm_sq_interval()
    first_lower = multiplicity * one_lower
    first_upper = multiplicity * one_upper
    tail_upper = Fraction(81, 3520)
    b_lower = first_lower
    b_upper = first_upper + tail_upper
    a_lower = 1 + b_lower
    a_upper = 1 + b_upper
    corrected_lower = b_lower / (1 + b_lower)
    corrected_upper = b_upper / (1 + b_upper)
    if not 0 < b_lower <= b_upper < 1:
        raise AssertionError("native word-tail interval left the proved branch")
    return {
        "charge": list(charge),
        "seed": "Omega" if charge == (0, 0) else "d_1^*Omega",
        "first_word_multiplicity": multiplicity,
        "first_word_norm_sq_interval": [qstr(first_lower), qstr(first_upper)],
        "unresolved_word_two_plus_norm_sq_upper": qstr(tail_upper),
        "B_tail_mass_interval": [qstr(b_lower), qstr(b_upper)],
        "A_total_Gram_interval": [qstr(a_lower), qstr(a_upper)],
        "M_Gram_block_formula": "[[A,B],[B,B]] with A=1+B",
        "naive_Gphi_is_M_orthogonal_to_phi": False,
        "naive_M_cross_interval": [qstr(b_lower), qstr(b_upper)],
        "corrected_tail_vector": "t=G phi-(B/A) phi",
        "corrected_projection_coefficient_interval": [
            qstr(b_lower / (1 + b_lower)),
            qstr(b_upper / (1 + b_upper)),
        ],
        "corrected_tail_M_norm_sq_identity": "<t,Mt>=B/A",
        "corrected_tail_M_norm_sq_interval": [qstr(corrected_lower), qstr(corrected_upper)],
        "two_vector_Gram_determinant_identity": "det([[A,B],[B,B]])=B",
        "two_vector_Gram_positive": True,
    }


def build() -> dict[str, Any]:
    q00 = sector_bounds((0, 0), 2)
    q10 = sector_bounds((1, 0), 1)
    return {
        "schema_version": "1.0",
        "result_id": "K489-NATIVE-NEUMANN-WORD-M-ORTHOGONALIZATION",
        "created": "2026-09-25",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "scope": "The actual K139 chart and K162 q00/q10 zero-bath seed orbits. The result corrects the first Neumann-word tail to the physical M=S* S orthogonal complement; it is not a complete K162 complement or a combined-form floor.",
        "gu_typed_objects": {
            "result": "native first-word M-orthogonalization MAP-TYPE=projection",
            "carrier": "K162 q00 and q10 zero-bath seed cyclic Neumann-word subspaces on the K139 positive Fock carrier",
            "pairing": "physical Gram M=S* S with S=(1-G_256)^-1",
            "form": "none in K489; K490 evaluates only the K168 shape component",
            "target": "first corrected tail line for a future K473 complete-complement split",
        },
        "exact_theorem": {
            "word_vectors": "v_n=G^n phi",
            "orthogonality": "<v_n,v_m>=0 for n!=m",
            "S_phi": "sum_(n>=0) v_n",
            "S_G_phi": "sum_(n>=1) v_n",
            "A": "sum_(n>=0)||v_n||^2",
            "B": "sum_(n>=1)||v_n||^2=A-1",
            "M_block": "[[A,B],[B,B]]",
            "corrected_tail": "t=G phi-(B/A)phi",
            "M_orthogonality": "<phi,Mt>=0",
            "corrected_norm": "<t,Mt>=B/A",
            "free_word_tail_equals_M_orthogonal_tail": False,
        },
        "native_sectors": [q00, q10],
        "decision": {
            "actual_native_split_attempted": True,
            "naive_free_word_tail_rejected": True,
            "first_corrected_M_orthogonal_line_constructed": True,
            "complete_M_orthogonal_complement_constructed": False,
            "combined_K139_K168_floor_emitted": False,
            "next_exact_input": "Evaluate the cancellation-safe base R0 form and its cross on the corrected K489 tail graph, then enlarge the corrected graph to a complete K162 complement before applying K473.",
        },
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Exact native K139/K162 two-vector Gram identity and outward q00/q10 projection intervals. The free bath-word tail is not the physical M-orthogonal tail; the corrected first line is explicit. No complete complement, base R0 form/cross, combined K139/K168 floor, K152 interval, source, ledger, canon, paper, public or physical conclusion follows.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.write:
        OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    if args.demo or not args.write:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
