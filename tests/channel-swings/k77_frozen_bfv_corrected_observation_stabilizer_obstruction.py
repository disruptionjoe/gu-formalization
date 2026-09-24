#!/usr/bin/env python3
"""Exact stabilizer obstruction for the frozen K77 BFV/observation bridge.

The result is deliberately narrow: it tests equivariant maps from the
published rank-70 frozen BFV orbit into the supplied full spinor trace lift.
It does not construct a quotient differential, Green domain, or BFV
cohomology, and it does not constrain symmetry-broken or reduced images.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k77-frozen-bfv-corrected-observation-stabilizer-obstruction.json"
BFV = ROOT / "lab/process/selected-k77-full-bfv-master-equation-gate.json"
SLICE = ROOT / "lab/process/corrected-observation-gauge-slice-green-compatibility.json"
QUOTIENT = ROOT / "lab/process/corrected-observation-quotient-slice-compatibility.json"
GREEN = ROOT / "lab/process/selected-k77-coupled-green-domain.json"
K77_TYPE = ROOT / "lab/process/w154-w229-k77-action-owner-qualification.json"


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dot(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum((x * y for x, y in zip(left, right)), Fraction())


def b3_casimir(weight: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    """Return (lambda,lambda+2 rho) for B3 with long roots of square two."""
    rho = (Fraction(5, 2), Fraction(3, 2), Fraction(1, 2))
    return dot(weight, tuple(x + 2 * r for x, r in zip(weight, rho)))


def build() -> dict[str, Any]:
    bfv = json.loads(BFV.read_text())
    slice_gate = json.loads(SLICE.read_text())
    quotient_gate = json.loads(QUOTIENT.read_text())
    green = json.loads(GREEN.read_text())
    k77_type = json.loads(K77_TYPE.read_text())

    geometry = bfv["constraint_geometry"]
    gauge_dimension = bfv["carrier"]["gauge_dimension"]
    stabilizer_dimension = geometry["stabilizer_dimension"]
    orbit_dimension = geometry["rank_at_frozen_distortion"]
    even_dimension = odd_dimension = 7
    even_bivectors = even_dimension * (even_dimension - 1) // 2
    mixed_dimension = even_dimension * odd_dimension
    full_spinor_dimension = k77_type["real_form_qualification"]["k77"]["irreducible_real_spinor_dimension"]
    b3_spinor_dimension = 8
    spinor_multiplicity = full_spinor_dimension // b3_spinor_dimension

    weights = {
        "trivial": (Fraction(0), Fraction(0), Fraction(0)),
        "vector": (Fraction(1), Fraction(0), Fraction(0)),
        "spinor": (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)),
    }
    casimirs = {name: b3_casimir(weight) for name, weight in weights.items()}
    source_spectrum = {casimirs["trivial"], casimirs["vector"]}
    target_spectrum = {casimirs["spinor"]}

    return {
        "schema_version": "1.0",
        "result_id": "K77-FROZEN-BFV-CORRECTED-OBSERVATION-STABILIZER-OBSTRUCTION",
        "created": "2026-09-24",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "Test whether the published rank-70 frozen K77 BFV orbit can supply the corrected observation trace-lift gauge image through an odd-axis so(3,4)-equivariant linear intertwiner.",
        "typed_objects": {
            "source": "tangent to the full so(7,7) gauge orbit at the published frozen distortion",
            "source_dimension": orbit_dimension,
            "target": "the supplied abstract corrected-observation trace lift im(j_B), conditionally realized as the full K77 real spinor carrier S for this frozen representation test",
            "target_dimension": full_spinor_dimension,
            "pairing": "none used; the selected Green pairing and common analytic domain remain open",
            "real_structure": "published real Cl(7,7) spinor restricted to the odd-axis Spin(3,4) stabilizer",
            "grading": "odd-axis stabilizer type: trivial/vector source summands versus spinor target summands",
            "action_owner": "published frozen K77 full BFV action fixture",
        },
        "assumptions": {
            "trace_carrier_realization": "choose the abstract corrected-observation trace carrier S to be the full irreducible real 128-spinor of Cl(7,7); this realization is tested, not source-selected",
            "stabilizer_action": "restrict the standard Spin(7,7) spin action to the published odd-axis Spin(3,4) stabilizer",
            "map_class": "real linear odd-axis so(3,4)-equivariant maps from the full frozen orbit tangent to im(j_B)",
            "background": "the one published frozen distortion at which the BFV orbit has rank 70",
        },
        "input_audit": {
            "bfv_evidence": "lab/process/selected-k77-full-bfv-master-equation-gate.json",
            "slice_evidence": "lab/process/corrected-observation-gauge-slice-green-compatibility.json",
            "quotient_evidence": "lab/process/corrected-observation-quotient-slice-compatibility.json",
            "green_dimension_evidence": "lab/process/selected-k77-coupled-green-domain.json",
            "K77_real_spinor_type_evidence": "lab/process/w154-w229-k77-action-owner-qualification.json",
            "gauge_algebra": bfv["carrier"]["gauge_algebra"],
            "gauge_dimension": gauge_dimension,
            "stabilizer": geometry["stabilizer"],
            "stabilizer_basis": geometry["stabilizer_basis"],
            "representative_selection_law": slice_gate["theorem"]["coset_constancy"],
            "quotient_descent_is_distinct": quotient_gate["decision"]["quotient_descent_and_representative_selection_distinguished"],
        },
        "orbit_decomposition": {
            "ambient_split": "R^(7,7)=E_even direct-sum O_odd with the stabilizer acting only on O_odd",
            "lie_algebra_split": "Lambda^2(E_even) direct-sum (E_even tensor O_odd) direct-sum Lambda^2(O_odd)",
            "stabilizer_summand": "Lambda^2(O_odd)=so(3,4)",
            "stabilizer_dimension": stabilizer_dimension,
            "orbit_summands": "Lambda^2(E_even) direct-sum (E_even tensor O_odd)",
            "trivial_copies": even_bivectors,
            "trivial_dimension_each": 1,
            "vector_copies": even_dimension,
            "vector_dimension_each": odd_dimension,
            "orbit_dimension_replay": even_bivectors + mixed_dimension,
            "ambient_dimension_replay": stabilizer_dimension + even_bivectors + mixed_dimension,
        },
        "target_restriction": {
            "full_real_spinor_dimension": full_spinor_dimension,
            "odd_axis_real_spinor_dimension": b3_spinor_dimension,
            "odd_axis_spinor_copies": spinor_multiplicity,
            "decomposition": "16 copies of the irreducible real 8-spinor of Spin(3,4)",
            "trace_lift_has_trivial_or_vector_summand": False,
        },
        "casimir_certificate": {
            "complexified_type": "B3=so(7,C)",
            "normalization": "(lambda,lambda+2*rho) with long roots of squared length 2",
            "rho": ["5/2", "3/2", "1/2"],
            "weights": {name: [qstr(x) for x in weight] for name, weight in weights.items()},
            "eigenvalues": {name: qstr(value) for name, value in casimirs.items()},
            "source_target_spectra_disjoint": source_spectrum.isdisjoint(target_spectrum),
            "intertwiner_law": "an so(3,4)-equivariant map commutes with the quadratic Casimir",
        },
        "decision": {
            "equivariant_hom_rank": 0,
            "nonzero_full_orbit_to_trace_intertwiner_exists": False,
            "full_frozen_orbit_can_equal_trace_lift_image_equivariantly": False,
            "representative_slice_route": "obstructed for the full frozen rank-70 orbit under odd-axis so(3,4) equivariance",
            "quotient_descent_route": "open; it may use a different target differential and parameter map u",
            "green_compatible_route": "open; no Green-self-adjoint right inverse or common analytic domain is derived",
        },
        "retained_repairs": [
            "use a smaller stabilizer-compatible constraint or reduced gauge image rather than the full frozen orbit",
            "supply a different target differential and test quotient descent P*d_action=d_target*u",
            "choose and justify a symmetry-broken or non-equivariant representative map",
            "move off the frozen background and derive the actual differential representation",
            "construct the proper reducible BFV/Koszul-Tate complex and physical cohomology",
            "supply a source-owned complement or observation map on a different common carrier",
        ],
        "release_test": {
            "gauge_dimension_is_91": gauge_dimension == 91,
            "stabilizer_dimension_is_21": stabilizer_dimension == 21,
            "orbit_dimension_is_70": orbit_dimension == 70,
            "orbit_decomposition_replays_70": even_bivectors + mixed_dimension == 70,
            "ambient_decomposition_replays_91": stabilizer_dimension + even_bivectors + mixed_dimension == 91,
            "full_spinor_dimension_is_128": full_spinor_dimension == 128,
            "target_multiplicity_replays_128": spinor_multiplicity * b3_spinor_dimension == 128,
            "casimir_eigenvalues_are_0_6_21_over_4": casimirs == {"trivial": 0, "vector": 6, "spinor": Fraction(21, 4)},
            "source_target_casimirs_are_disjoint": source_spectrum.isdisjoint(target_spectrum),
            "quotient_and_slice_remain_distinct": quotient_gate["decision"]["quotient_descent_and_representative_selection_distinguished"],
            "no_green_domain_claim": True,
            "no_source_ledger_canon_paper_public_or_physical_effect": True,
        },
        "claim_ceiling": "Exact representation-theoretic obstruction for an odd-axis so(3,4)-equivariant linear map from the published full rank-70 frozen BFV orbit to the conditional realization of the abstract corrected-observation trace lift as the full real 128-spinor: the source is 21 trivial plus seven vector modules, the target is spinor-isotypic, and disjoint quadratic-Casimir spectra force Hom=0. The full-spinor trace realization is tested, not source-selected. This does not obstruct quotient descent with a different target differential, a reduced gauge image, a non-equivariant or symmetry-broken choice, a moving-background differential, proper BFV cohomology, a different source-owned complement, or any Green-domain construction. No source, ledger, canon, paper, public, novelty or physical GU verdict follows.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    orbit = payload["orbit_decomposition"]
    target = payload["target_restriction"]
    casimir = payload["casimir_certificate"]
    decision = payload["decision"]
    assert payload["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY"
    assert payload["direction"] == "observed_to_native"
    assert payload["assumptions"]["trace_carrier_realization"].endswith("tested, not source-selected")
    assert orbit["trivial_copies"] == 21
    assert orbit["vector_copies"] == 7
    assert orbit["vector_dimension_each"] == 7
    assert orbit["orbit_dimension_replay"] == 70
    assert orbit["ambient_dimension_replay"] == 91
    assert target["full_real_spinor_dimension"] == 128
    assert target["odd_axis_real_spinor_dimension"] == 8
    assert target["odd_axis_spinor_copies"] == 16
    assert target["trace_lift_has_trivial_or_vector_summand"] is False
    assert casimir["eigenvalues"] == {"trivial": "0", "vector": "6", "spinor": "21/4"}
    assert casimir["source_target_spectra_disjoint"] is True
    assert decision["equivariant_hom_rank"] == 0
    assert decision["nonzero_full_orbit_to_trace_intertwiner_exists"] is False
    assert decision["full_frozen_orbit_can_equal_trace_lift_image_equivariantly"] is False
    assert decision["quotient_descent_route"].startswith("open")
    assert decision["green_compatible_route"].startswith("open")
    assert len(payload["retained_repairs"]) == 6
    assert all(payload["release_test"].values())
    assert "tested, not source-selected" in payload["claim_ceiling"]
    assert "non-equivariant" in payload["claim_ceiling"]
    assert "No source, ledger, canon" in payload["claim_ceiling"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    if args.write:
        OUTPUT.write_text(json.dumps(payload, indent=2) + "\n")
    print("K77 stabilizer obstruction passed: Hom_so(3,4)(21*1 + 7*7, 16*8_spin)=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
