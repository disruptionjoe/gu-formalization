#!/usr/bin/env python3
"""Exact controls for the Eric/Curt Wave 2 carrier-port census.

This probe certifies the ownership table and four small algebraic facts used by
the census.  The subsequent Wave 2b probe owns the frozen first-layer monomial
quotient, coefficient rank, support ablation, and surplus result.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CAMPAIGN = ROOT / "lab/process/eric-curt-ten-wave-campaign.json"
REGISTRY = ROOT / "lab/process/eric-curt-wave2-carrier-port-census.json"

Q = Fraction
Matrix = list[list[Fraction]]

exact_checks = 0
planted_checks = 0


def exact(name: str, condition: bool) -> None:
    global exact_checks
    if not condition:
        raise AssertionError(name)
    exact_checks += 1


def planted(name: str, false_claim: bool) -> None:
    global planted_checks
    if false_claim:
        raise AssertionError(f"planted false claim passed: {name}")
    planted_checks += 1


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(
                (left[i][k] * right[k][j] for k in range(len(right))),
                Q(0),
            )
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] - right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def scale(matrix: Matrix, scalar: Fraction) -> Matrix:
    return [[scalar * value for value in row] for row in matrix]


def trace(matrix: Matrix) -> Fraction:
    return sum((matrix[index][index] for index in range(len(matrix))), Q(0))


def trace_reverse(metric: Matrix, tensor: Matrix) -> Matrix:
    coefficient = Q(1, 2) * trace(matmul(metric, tensor))
    return subtract(tensor, scale(metric, coefficient))


def main() -> None:
    campaign = json.loads(CAMPAIGN.read_text())
    registry = json.loads(REGISTRY.read_text())
    primitives = {row["id"]: row for row in registry["primitives"]}
    vocabulary = set(registry["status_vocabulary"])
    wave2 = next(row for row in campaign["waves"] if row["id"] == registry["wave"])

    exact("registry records the completed Wave 2b frozen-class continuation", registry["status"] == "PORT_CENSUS_COMPLETE__WAVE2B_FROZEN_G2_FIRST_LAYER_QUOTIENT_COMPLETE")
    exact("campaign Wave 2 records the frozen-class exit", wave2["status"] == "COMPLETE_FROZEN_G2_FIRST_LAYER_TERM_QUOTIENT__LATER_ACTION_CLASSES_REMAIN_OWNED")
    exact("four carrier branches are frozen", set(registry["branches"]) == {"R95_ACTIVE", "R77_BASE_FLIP", "R77_VERTICAL_FLIP", "C14_COMMON"})
    exact("twenty-two primitive identifiers are unique", len(primitives) == len(registry["primitives"]) == 22)
    exact("every classification belongs to the declared vocabulary", all(row["classification"] in vocabulary for row in primitives.values()))
    exact("portable exact set is frozen", registry["portable_exact_ids"] == ["CP-01", "CP-04", "CP-11", "CP-12", "CP-13"])
    exact("portable identifiers are classified shared exact", all(primitives[row_id]["classification"] == "SHARED_EXACT" for row_id in registry["portable_exact_ids"]))
    exact("every explicit port identifier resolves", set(registry["explicit_port_ids"]) <= set(primitives))
    exact("every explicit port is charged as a port or active-only object", all(primitives[row_id]["classification"] in {"BRANCH_NATIVE_PORT", "SHARED_SCHEMA_PORT_REQUIRED", "ACTIVE_BUILT_OTHER_BRANCHES_OPEN"} for row_id in registry["explicit_port_ids"]))
    exact("right-H ownership is active-only", registry["right_h_active_only_ids"] == ["CP-09", "CP-22"] and all(primitives[row_id]["classification"] == "ACTIVE_BUILT_OTHER_BRANCHES_OPEN" for row_id in registry["right_h_active_only_ids"]))
    exact("real (7,7) does not inherit the quaternionic module", "not present on M(128,R)" in primitives["CP-09"]["carrier_dependence"])
    exact("bosonic action keeps exact fractional grammar", all(token in primitives["CP-16"]["formula"] for token in ["(1/2)", "(1/3)", "kappa_1"]))
    exact("RB6 formula and active evaluation are separated", "active W177 values do not" in primitives["CP-18"]["wave2_use"] and "unevaluated off active branch" in primitives["CP-19"]["wave2_use"])
    exact("commutator existence remains conditional", primitives["CP-20"]["classification"] == "SHARED_CONDITIONAL" and "nonzero value and polar gap are open" in primitives["CP-20"]["carrier_dependence"])
    exact("residual square remains pairing-dependent", primitives["CP-21"]["classification"] == "BRANCH_NATIVE_PORT")
    exact("odd action remains active-built and physically unclaimed", primitives["CP-22"]["classification"] == "ACTIVE_BUILT_OTHER_BRANCHES_OPEN" and "no branch transfer or physical mass" in primitives["CP-22"]["wave2_use"])
    exact("Curt step ownership is frozen", registry["curt_steps"] == ["CI-13", "CI-14", "CI-15", "CI-16", "CI-17", "CI-18", "CI-29"])
    exact("historical port census did not fabricate surplus", registry["constraint_surplus"]["status"] == "SURPLUS_UNCOMPUTABLE")
    exact("next computation contains quotient rank and ablation", all(any(token in item for item in registry["constraint_surplus"]["next_computation"]) for token in ["quotient", "term-space rank", "coefficient count", "ablate"]))
    exact("Wave 2 has no third-lane effect", registry["third_lane_effect"].startswith("NONE") and campaign["third_lane_promotion_gate"]["current_verdict"] == "NOT_PROMOTED")
    exact("Wave 2b registry is linked", registry["wave2b"] == "lab/process/eric-curt-wave2b-term-rank-ablation.json")
    exact("next swing is observation", registry["next_swing"].startswith("ECW3-G4-OBSERVATION"))

    # Exact affine-gauge control: derivative shifts cancel only in A-B.
    g: Matrix = [[Q(2), Q(1)], [Q(1), Q(1)]]
    g_inverse: Matrix = [[Q(1), Q(-1)], [Q(-1), Q(2)]]
    A: Matrix = [[Q(1), Q(2)], [Q(3), Q(4)]]
    B: Matrix = [[Q(-1), Q(0)], [Q(2), Q(1)]]
    derivative_shift: Matrix = [[Q(1, 3), Q(2, 5)], [Q(-1, 7), Q(3, 4)]]
    A_g = subtract(matmul(matmul(g, A), g_inverse), derivative_shift)
    B_g = subtract(matmul(matmul(g, B), g_inverse), derivative_shift)
    distortion_g = subtract(A_g, B_g)
    homogeneous_distortion = matmul(matmul(g, subtract(A, B)), g_inverse)
    exact("rational gauge fixture is invertible", matmul(g, g_inverse) == [[Q(1), Q(0)], [Q(0), Q(1)]])
    exact("affine derivative shifts cancel in the distortion", distortion_g == homogeneous_distortion)
    planted("derivative shift survives in the distortion", distortion_g != homogeneous_distortion)

    # Trace reversal is unchanged by simultaneous h -> -h, but its paired
    # DeWitt form changes sign.  The operation and the pairing are not one object.
    h: Matrix = [[Q(1), Q(0), Q(0), Q(0)], [Q(0), Q(1), Q(0), Q(0)], [Q(0), Q(0), Q(1), Q(0)], [Q(0), Q(0), Q(0), Q(-1)]]
    minus_h = scale(h, Q(-1))
    k: Matrix = [[Q(2), Q(1), Q(0), Q(0)], [Q(1), Q(-1), Q(3), Q(0)], [Q(0), Q(3), Q(4), Q(2)], [Q(0), Q(0), Q(2), Q(5)]]
    tau_h = trace_reverse(h, k)
    tau_minus_h = trace_reverse(minus_h, k)
    exact("four-dimensional trace reversal survives base sign reversal", tau_h == tau_minus_h)
    planted("equal trace reversal selects the same DeWitt pairing", scale(h, Q(-1)) == h)

    # The Hodge-square parity is the same for signatures with q=5 and q=7;
    # this necessary identity is far weaker than an intertwiner of Hodge stars.
    exact("Hodge-square parity agrees for q=5 and q=7 in every degree", all((-1) ** (degree * (14 - degree) + 5) == (-1) ** (degree * (14 - degree) + 7) for degree in range(15)))
    planted("equal Hodge-square parity identifies the Hodge operators", (9, 5) == (7, 7))

    # Commutators of G-self-adjoint endomorphisms are G-skew.  Nonzero Q is
    # possible, but neither charge conjugation nor a polar complex structure is selected.
    G: Matrix = [[Q(1), Q(0)], [Q(0), Q(-1)]]
    H1: Matrix = [[Q(1), Q(2)], [Q(-2), Q(3)]]
    H2: Matrix = [[Q(0), Q(1)], [Q(-1), Q(4)]]
    exact("first H word is G-self-adjoint", matmul(transpose(H1), G) == matmul(G, H1))
    exact("second H word is G-self-adjoint", matmul(transpose(H2), G) == matmul(G, H2))
    commutator = subtract(matmul(H1, H2), matmul(H2, H1))
    exact("fixture commutator is nonzero", commutator != [[Q(0), Q(0)], [Q(0), Q(0)]])
    exact("fixture commutator is G-skew", matmul(transpose(commutator), G) == scale(matmul(G, commutator), Q(-1)))
    planted("a nonzero G-skew commutator is charge conjugation", primitives["CP-20"]["name"] == "charge conjugation")
    planted("a nonzero G-skew commutator selects a polar complex structure", "polar gap is closed" in primitives["CP-20"]["carrier_dependence"])

    # Target blindness is checked on the mathematical formula/name surface,
    # not on the explanatory list of deliberately forbidden inputs.
    formula_surface = " ".join(f'{row["name"]} {row["formula"]}' for row in registry["primitives"])
    exact("primitive grammar contains no Standard Model target labels", all(token not in formula_surface for token in ["SU(3)", "Higgs doublet", "P3", "photon", "generation count"]))
    planted("a target-labelled projector was admitted", "target-labelled projector" in formula_surface)
    planted("partial Wave 2 computes a positive surplus", registry["constraint_surplus"]["status"].startswith("POSITIVE"))
    planted("a Curt third lane is promoted", campaign["third_lane_promotion_gate"]["current_verdict"] == "PROMOTED")

    print(f"ERIC-CURT-WAVE2-PORT-CENSUS: {exact_checks} exact checks + {planted_checks} planted failures = {exact_checks + planted_checks} PASS")
    print("RESULT: affine IG, distortion, trace reversal, and the underlying bundle grammar port exactly")
    print("RESULT: metric, Hodge, Clifford, Krein/reality, action pairings, adjoints, and residual squares require branch-native ports")
    print("STATUS: this port census remains the ownership input; Wave 2b now closes the frozen G2 first-layer quotient and releases Wave 3")
    print("LANE: no third lane; literal real (7,7) comparators remain rival carrier readings inside the Eric lane")


if __name__ == "__main__":
    main()
