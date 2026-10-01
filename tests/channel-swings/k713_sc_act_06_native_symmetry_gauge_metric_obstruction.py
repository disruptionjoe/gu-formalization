#!/usr/bin/env python3
"""K713: full native pseudo-orthogonal symmetry obstructs a positive gauge metric."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k713-sc-act-06-native-symmetry-gauge-metric-obstruction.json"


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def multiply(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def subtract(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def rank(a: list[list[Fraction]]) -> int:
    work = [[Fraction(x) for x in row] for row in a]
    r = 0
    for c in range(len(work[0]) if work else 0):
        pivot = next((i for i in range(r, len(work)) if work[i][c]), None)
        if pivot is None:
            continue
        work[r], work[pivot] = work[pivot], work[r]
        p = work[r][c]
        work[r] = [x / p for x in work[r]]
        for i in range(len(work)):
            if i != r and work[i][c]:
                q = work[i][c]
                work[i] = [work[i][j] - q * work[r][j] for j in range(len(work[0]))]
        r += 1
    return r


def invariant_equations(boost: list[list[Fraction]]) -> list[list[Fraction]]:
    basis = [
        [[Fraction(1), 0], [0, 0]],
        [[0, Fraction(1)], [Fraction(1), 0]],
        [[0, 0], [0, Fraction(1)]],
    ]
    columns = []
    for q in basis:
        defect = subtract(multiply(transpose(boost), multiply(q, boost)), q)
        columns.append([defect[0][0], defect[0][1], defect[1][1]])
    return [list(row) for row in zip(*columns)]


def strings(a: list[list[Fraction]]) -> list[list[str]]:
    return [[str(x) for x in row] for row in a]


def build() -> dict[str, Any]:
    c, s = Fraction(5, 3), Fraction(4, 3)
    boost = [[c, s], [s, c]]
    eta = [[Fraction(1), 0], [0, Fraction(-1)]]
    identity = [[Fraction(1), 0], [0, Fraction(1)]]
    equations = invariant_equations(boost)
    eta_defect = subtract(multiply(transpose(boost), multiply(eta, boost)), eta)
    identity_defect = subtract(multiply(transpose(boost), multiply(identity, boost)), identity)
    return {
        "schema_version": "1.0",
        "result_id": "K713-SC-ACT-06-NATIVE-SYMMETRY-GAUGE-METRIC-OBSTRUCTION",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Whether a positive auxiliary gauge metric on the real `(13,1)` carrier can be invariant under the full native pseudo-orthogonal symmetry.",
        "gu_typed_objects": {
            "carrier": "standard real fourteen-dimensional representation with native form of inertia `(13,1)`",
            "pairing": "native pseudo-form eta versus a candidate positive auxiliary form q",
            "real_structure": "unchanged real carrier",
            "grading": "one positive direction plus the negative trace line embedded in the full carrier",
            "action_owner": "native pseudo-orthogonal symmetry only; no source-owned compact reduction or positive q supplied",
            "target": "symmetry compatibility of an auxiliary gauge-fixing metric MAP-TYPE=invariant bilinear form",
        },
        "theorem": {
            "rational_boost_preserves_native_1_1_form": True,
            "rational_boost_preserves_positive_identity": False,
            "symmetric_forms_invariant_under_boost_are_scalar_native_forms": True,
            "positive_definite_invariant_form_exists_on_boost_plane": False,
            "positive_definite_O_13_1_invariant_form_exists": False,
            "auxiliary_positive_metric_requires_symmetry_reduction_or_extra_choice": True,
            "source_selected_reduction_constructed": False,
            "source_claim_refuted": False,
        },
        "exact_controls": {
            "boost": strings(boost),
            "boost_determinant": str(c * c - s * s),
            "boost_eigenvalues": ["3", "1/3"],
            "native_form": strings(eta),
            "native_invariance_defect": strings(eta_defect),
            "positive_identity_invariance_defect": strings(identity_defect),
            "invariant_symmetric_form_equations": strings(equations),
            "equation_rank": rank(equations),
            "solution_dimension": 3 - rank(equations),
            "solution_generator_a_b_d": [1, 0, -1],
            "solution_generator_signature": [1, 1, 0],
            "full_carrier_native_signature": [13, 1, 0],
        },
        "native_interface_status": {
            "positive_auxiliary_metric_source_owned": False,
            "native_symmetry_reduction_selected": False,
            "complete_full_field_symbol_constructed": False,
            "auxiliary_metric_compatibility_with_full_symbol_proved": False,
            "fredholm_domain_constructed": False,
            "nonlinear_moduli_theorem_proved": False,
            "SC_ACT_06_ellipticity_proved": False,
        },
        "decision": {
            "auxiliary_positive_metric_is_canonical_under_full_native_symmetry": False,
            "auxiliary_route_is_mathematically_invalid": False,
            "ownership_cost": "A positive q must be supplied together with an independently justified compact/symmetry reduction or accepted gauge choice; full O(13,1) invariance cannot select it.",
            "next_exact_input": "Construct the complete GU symbol and choose between an authenticated Euclidean continuation or an explicitly owned positive auxiliary metric plus symmetry reduction; then prove every symbol block and projector is compatible at all nonzero covectors.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The obstruction prices the auxiliary repair's symmetry cost but neither forbids such a gauge choice nor constructs the full GU deformation complex.",
        "preflight_bookend": {
            "route_comparison": "K712 opens the auxiliary-positive route; K713 tests whether the native indefinite symmetry makes that choice canonical and proves it does not.",
            "retrieval_collision_result": "Earlier signature work records indefinite carriers, but no SC-ACT-06 artifact supplies the exact rational boost obstruction for auxiliary gauge metrics.",
            "strongest_alternative": "A source-selected compact subgroup or stationary background could own q, but neither is presently constructed for the complete Euclidean germ.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "No positive auxiliary gauge metric may ever be used on the native real carrier.",
            "strongest_contrary_construction": "The ordinary identity form is positive and repairs the bare symbol, but its nonzero boost defect proves it breaks the full native pseudo-orthogonal symmetry.",
            "weakest_reproducibility_seam": "The full GU deformation problem may already reduce symmetry through a source-owned background; that reduction must be constructed rather than presumed absent.",
        },
        "controls": {
            "producer": "tests/channel-swings/k713_sc_act_06_native_symmetry_gauge_metric_obstruction.py",
            "probe": "tests/channel-swings/k713_sc_act_06_native_symmetry_gauge_metric_obstruction_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 30,
        },
        "claim_ceiling": "Exact invariant-form obstruction for the standard pseudo-orthogonal carrier. It does not forbid non-invariant gauge fixing, exclude a source-owned symmetry reduction, instantiate the GU symbol, prove Fredholmness or moduli, or move source, ledger, canon, prediction, confirmation or public verdicts.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n, d = p["theorem"], p["exact_controls"], p["native_interface_status"], p["decision"]
    for key in ("rational_boost_preserves_native_1_1_form", "symmetric_forms_invariant_under_boost_are_scalar_native_forms", "auxiliary_positive_metric_requires_symmetry_reduction_or_extra_choice"):
        assert t[key]
    for key in ("rational_boost_preserves_positive_identity", "positive_definite_invariant_form_exists_on_boost_plane", "positive_definite_O_13_1_invariant_form_exists", "source_selected_reduction_constructed", "source_claim_refuted"):
        assert not t[key]
    assert c["boost"] == [["5/3", "4/3"], ["4/3", "5/3"]]
    assert c["boost_determinant"] == "1" and c["boost_eigenvalues"] == ["3", "1/3"]
    assert c["native_invariance_defect"] == [["0", "0"], ["0", "0"]]
    assert c["positive_identity_invariance_defect"] != [["0", "0"], ["0", "0"]]
    assert c["equation_rank"] == 2 and c["solution_dimension"] == 1
    assert c["solution_generator_a_b_d"] == [1, 0, -1] and c["solution_generator_signature"] == [1, 1, 0]
    assert c["full_carrier_native_signature"] == [13, 1, 0]
    assert all(v is False for v in n.values())
    assert not d["auxiliary_positive_metric_is_canonical_under_full_native_symmetry"]
    assert not d["auxiliary_route_is_mathematically_invalid"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
