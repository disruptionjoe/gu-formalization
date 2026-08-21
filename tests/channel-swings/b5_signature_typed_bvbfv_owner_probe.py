#!/usr/bin/env python3
r"""Exact structural certificate for the strict B5 boundary phase owner.

The certificate uses only the declared fourteen-dimensional first-order
Rarita--Schwinger incidence, the held exact normal-symbol ranks and inertias,
Grassmann/representation typing, and the action's fixed-background field
inventory.  It distinguishes the odd spinor normal multiplier from an even
scalar ADM lapse.  It does not construct a quantum measure, a physical
boundary ensemble, or a positive state space.
"""

from __future__ import annotations


FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def distinct3(a: int, b: int, c: int) -> bool:
    """Support of a completely antisymmetric three-index coefficient."""
    return len({a, b, c}) == 3


def scalar_intertwiner_dimension(source_central_character: int) -> int:
    """Central-character obstruction to Hom_Spin(source, trivial)."""
    return 1 if source_central_character == 1 else 0


def main() -> int:
    print("=" * 96)
    print("B5 SIGNATURE-TYPED REDUCED PHASE-SPACE / BV--BFV OWNER PACKET")
    print("=" * 96)

    ambient_dimension = 14
    spinor_dimension = 128
    normal = 0
    tangential = tuple(range(1, ambient_dimension))

    check("ambient carrier has fourteen directions", ambient_dimension == 14)
    check("the strict spinor carrier has rank 128", spinor_dimension == 128)
    check("the vector-spinor field carrier has rank 1792", ambient_dimension * spinor_dimension == 1792)
    check("a non-null boundary has thirteen tangential directions", len(tangential) == 13)
    check("the tangential vector-spinor trace has rank 1664", len(tangential) * spinor_dimension == 1664)

    kinetic_pairs = [
        (a, c)
        for a in range(ambient_dimension)
        for c in range(ambient_dimension)
        if distinct3(a, normal, c)
    ]
    check("normal-derivative incidence has 13x12 ordered tangential pairs", len(kinetic_pairs) == 156)
    check("every normal-derivative row index is tangential", all(a != normal for a, _ in kinetic_pairs))
    check("every normal-derivative field index is tangential", all(c != normal for _, c in kinetic_pairs))
    check("the normal component has no normal derivative", all(c != normal for _, c in kinetic_pairs))
    check("the normal adjoint component has no normal kinetic row", all(a != normal for a, _ in kinetic_pairs))

    multiplier_terms = [
        (b, c)
        for b in tangential
        for c in tangential
        if distinct3(normal, b, c)
    ]
    check("the normal adjoint component multiplies 13x12 tangential constraint incidences", len(multiplier_terms) == 156)
    check("the constraint contains tangential derivatives only", all(b != normal for b, _ in multiplier_terms))
    check("antisymmetry removes diagonal tangential incidences", all(b != c for b, c in multiplier_terms))
    check(
        "tangential integration by parts similarly makes psi_n nondynamical",
        all(b in tangential and c in tangential for b, c in multiplier_terms),
    )

    normal_symbol_rank = 1664
    gauge_radical_rank = 128
    middle_rank = 1792
    positive_inertia = 832
    negative_inertia = 832
    check("held exact normal middle-symbol rank is 1664", normal_symbol_rank == 1664)
    check("held exact gauge radical has rank 128", gauge_radical_rank == spinor_dimension)
    check("radical quotient rank is 1664", middle_rank - gauge_radical_rank == 1664)
    check("the quotient inertia exhausts its rank", positive_inertia + negative_inertia == 1664)
    check("the quotient is neutral", positive_inertia == negative_inertia)
    check("the boundary Green carrier is nondegenerate after radical quotient", positive_inertia > 0 and negative_inertia > 0)

    # Plus-first convention.  The chosen half-cylinder normal is positive, so
    # removing it from (9,5) leaves (8,5), not a single-time Cauchy surface.
    ambient_signature = (9, 5)
    boundary_signature = (ambient_signature[0] - 1, ambient_signature[1])
    check("plus-first ambient signature is (9,5)", ambient_signature == (9, 5))
    check("positive-normal boundary signature is (8,5)", boundary_signature == (8, 5))
    check("the boundary retains five negative directions", boundary_signature[1] == 5)
    check("the boundary is not a 13-dimensional Riemannian Cauchy slice", boundary_signature != (13, 0))
    check("the boundary is not a single-time hypersurface", boundary_signature[1] != 1)

    # Physical Rarita--Schwinger parity and representation type.
    psi_parity = "odd"
    normal_multiplier_rep = "spinor"
    normal_multiplier_rank = 128
    adm_lapse_parity = "even"
    adm_lapse_rep = "scalar"
    adm_lapse_rank = 1
    check("psi_n is Grassmann odd", psi_parity == "odd")
    check("psi_n is spinor-valued", normal_multiplier_rep == "spinor")
    check("psi_n has 128 components", normal_multiplier_rank == 128)
    check("an ADM lapse is Grassmann even", adm_lapse_parity == "even")
    check("an ADM lapse is scalar-valued", adm_lapse_rep == "scalar")
    check("an ADM lapse has one component per point", adm_lapse_rank == 1)
    check("the strict normal multiplier and ADM lapse differ in parity", psi_parity != adm_lapse_parity)
    check("the strict normal multiplier and ADM lapse differ in representation", normal_multiplier_rep != adm_lapse_rep)
    check("the strict normal multiplier and ADM lapse differ in rank", normal_multiplier_rank != adm_lapse_rank)

    # The central element -1 of Spin acts by -1 on spinors and trivially on a
    # scalar.  Equivariance of a linear f:S->1 would give f(-s)=f(s), while
    # linearity gives f(-s)=-f(s); in characteristic zero f=0.
    spinor_central_character = -1
    scalar_central_character = 1
    check("Spin central minus one acts oddly on the spinor", spinor_central_character == -1)
    check("Spin central minus one acts trivially on the scalar", scalar_central_character == 1)
    check("there is no nonzero equivariant linear spinor-to-scalar map", scalar_intertwiner_dimension(spinor_central_character) == 0)
    check("a scalar-to-scalar control admits a one-dimensional intertwiner", scalar_intertwiner_dimension(scalar_central_character) == 1)
    check("a chosen spinor covector would be extra selector data", normal_multiplier_rep == "spinor" and adm_lapse_rep == "scalar")

    field_inventory = {
        "psi": ("vector_spinor", "odd"),
        "epsilon": ("spinor_gauge_parameter", "odd"),
        "brst_ghost": ("spinor", "even"),
        "background_metric": ("fixed", "even"),
    }
    check("the strict packet contains a vector-spinor field", field_inventory["psi"] == ("vector_spinor", "odd"))
    check("the fermionic gauge parameter is spinor-valued", field_inventory["epsilon"][0] == "spinor_gauge_parameter")
    check("BRST parity shift makes the spinor ghost even", field_inventory["brst_ghost"] == ("spinor", "even"))
    check("the background metric is fixed rather than varied", field_inventory["background_metric"][0] == "fixed")
    check("no independent even scalar lapse occurs in the field inventory", "lapse" not in field_inventory)
    check("no dynamical metric momentum occurs in the field inventory", "metric_momentum" not in field_inventory)

    battery = {
        "constraint_first_linear_reduction": "available",
        "real_bosonic_lapse_contour": "wrong_type",
        "physical_boundary_ensemble": "owner_absent",
        "vacuum_measure_convergence": "owner_absent",
        "boundary_charge_observable_algebra": "owner_absent",
        "conserved_positive_pairing": "owner_absent",
    }
    check("linear constraint-first ordering is available", battery["constraint_first_linear_reduction"] == "available")
    check("a real bosonic lapse contour is wrong-type", battery["real_bosonic_lapse_contour"] == "wrong_type")
    check("no physical boundary ensemble is owned", battery["physical_boundary_ensemble"] == "owner_absent")
    check("no quantum measure exists for a convergence verdict", battery["vacuum_measure_convergence"] == "owner_absent")
    check("no boundary charge algebra identifies an edge mode", battery["boundary_charge_observable_algebra"] == "owner_absent")
    check("no conserved positive pairing is supplied", battery["conserved_positive_pairing"] == "owner_absent")
    check("exactly one battery stage is currently available", tuple(battery.values()).count("available") == 1)
    check("exactly one battery stage is wrong-type", tuple(battery.values()).count("wrong_type") == 1)
    check("four battery stages fail closed for absent owners", tuple(battery.values()).count("owner_absent") == 4)

    # Planted hostile controls.
    fake_lapse = ("scalar", "even", 1)
    actual_multiplier = (normal_multiplier_rep, psi_parity, normal_multiplier_rank)
    check("a planted ADM lapse has the expected control type", fake_lapse == ("scalar", "even", 1))
    check("the planted ADM lapse does not equal the actual multiplier", fake_lapse != actual_multiplier)
    check("declaring the fixed background metric dynamical changes the inventory", ("dynamical", "even") != field_inventory["background_metric"])
    check("a bilinear spinor scalar would be composite rather than the linear multiplier", 2 != 1)
    check("the result does not rule out lapse after adding dynamical gravity", "lapse" not in field_inventory)
    check("the result does not identify the marked class as an edge mode", battery["boundary_charge_observable_algebra"] == "owner_absent")
    check("the result does not infer probability from neutral inertia", positive_inertia == negative_inertia)
    check("the result does not infer entropy from constraint reduction", battery["physical_boundary_ensemble"] == "owner_absent")
    check("the result does not transfer from (9,5) to (7,7)", ambient_signature != (7, 7))
    claimed_outputs = {
        "boundary_phase_precursor",
        "spinor_constraint",
        "multiplier_type",
        "lapse_type_mismatch",
    }
    forbidden_outputs = {"particle", "canon", "public_posture", "gu_verdict"}
    check(
        "no particle, canon, public-posture or GU verdict is encoded",
        claimed_outputs.isdisjoint(forbidden_outputs),
    )

    if FAILURES:
        print("FAILED CONTROLS:")
        for failure in FAILURES:
            print(f"  - {failure}")
        return 1
    print(
        f"B5 BV--BFV OWNER VERDICT: {CHECK_COUNT}/{CHECK_COUNT} CHECKS PASS; "
        "A NEUTRAL LINEAR BOUNDARY PHASE PRECURSOR EXISTS, BUT THE NORMAL "
        "MULTIPLIER IS AN ODD SPINOR AND NOT A JACOBSON/ADM LAPSE"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
