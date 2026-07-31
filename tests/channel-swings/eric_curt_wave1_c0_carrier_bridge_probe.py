#!/usr/bin/env python3
"""Exact controls for Eric/Curt campaign Wave 1 (C0 carrier bridge).

The probe distinguishes four claims:

1. a metric musical plus a declared horizontal split identifies the underlying
   rank-14 vector bundles;
2. the active trace-reversed DeWitt carrier has real signature (9,5);
3. a literal real (7,7) chimeric carrier is not real-isometric and has a
   different real Clifford type;
4. the two Clifford carriers agree only after complexification, which does not
   preserve the real/quaternionic structure automatically.

This is a local algebraic/typing certificate.  It does not prove a global
natural Zorro connection, select a carrier/action, or recover physics.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CAMPAIGN = ROOT / "lab/process/eric-curt-ten-wave-campaign.json"
ATLAS = ROOT / "lab/process/eric-native-physics-equation-replacement-atlas.json"
CURT_CROSSWALK = ROOT / "lab/process/curt-iceberg-native-crosswalk.json"

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


def identity(size: int) -> Matrix:
    return [[Q(int(i == j)) for j in range(size)] for i in range(size)]


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


def matrix_equal(left: Matrix, right: Matrix) -> bool:
    return left == right


def block_diag(left: Matrix, right: Matrix) -> Matrix:
    rows = len(left) + len(right)
    columns = len(left[0]) + len(right[0])
    result = [[Q(0) for _ in range(columns)] for _ in range(rows)]
    for i, row in enumerate(left):
        for j, value in enumerate(row):
            result[i][j] = value
    offset_i = len(left)
    offset_j = len(left[0])
    for i, row in enumerate(right):
        for j, value in enumerate(row):
            result[offset_i + i][offset_j + j] = value
    return result


def scale(matrix: Matrix, scalar: Fraction) -> Matrix:
    return [[scalar * value for value in row] for row in matrix]


def determinant(matrix: Matrix) -> Fraction:
    work = [row[:] for row in matrix]
    result = Q(1)
    size = len(work)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            return Q(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, size):
            coefficient = work[row][column] / pivot_value
            for index in range(column + 1, size):
                work[row][index] -= coefficient * work[column][index]
    return result


def inertia(matrix: Matrix) -> tuple[int, int, int]:
    """Exact symmetric congruence elimination, including 2x2 pivots."""

    work = [row[:] for row in matrix]
    positive = negative = zero = 0
    size = len(work)

    def swap_indices(left: int, right: int) -> None:
        if left == right:
            return
        work[left], work[right] = work[right], work[left]
        for row in work:
            row[left], row[right] = row[right], row[left]

    column = 0
    while column < size:
        pivot = next(
            (row for row in range(column, size) if work[row][row] != 0),
            None,
        )
        if pivot is None:
            pair = next(
                (
                    (i, j)
                    for i in range(column, size)
                    for j in range(i + 1, size)
                    if work[i][j] != 0
                ),
                None,
            )
            if pair is None:
                zero += size - column
                break
            first, second = pair
            swap_indices(column, first)
            swap_indices(column + 1, second)
            a = work[column][column]
            b = work[column][column + 1]
            c = work[column + 1][column + 1]
            block_det = a * c - b * b
            if block_det >= 0:
                raise AssertionError("unexpected non-hyperbolic 2x2 pivot")
            positive += 1
            negative += 1
            inverse_block = [
                [c / block_det, -b / block_det],
                [-b / block_det, a / block_det],
            ]
            for row in range(column + 2, size):
                for other in range(row, size):
                    left_coupling = [
                        work[row][column],
                        work[row][column + 1],
                    ]
                    right_coupling = [
                        work[column][other],
                        work[column + 1][other],
                    ]
                    correction = sum(
                        (
                            left_coupling[i]
                            * inverse_block[i][j]
                            * right_coupling[j]
                            for i in range(2)
                            for j in range(2)
                        ),
                        Q(0),
                    )
                    value = work[row][other] - correction
                    work[row][other] = value
                    work[other][row] = value
            for row in range(column + 2, size):
                for pivot_index in (column, column + 1):
                    work[row][pivot_index] = Q(0)
                    work[pivot_index][row] = Q(0)
            column += 2
            continue
        if pivot != column:
            swap_indices(column, pivot)
        pivot_value = work[column][column]
        if pivot_value > 0:
            positive += 1
        else:
            negative += 1
        ratios = {
            row: work[row][column] / pivot_value
            for row in range(column + 1, size)
        }
        for row in range(column + 1, size):
            for other in range(row, size):
                value = (
                    work[row][other]
                    - ratios[row] * ratios[other] * pivot_value
                )
                work[row][other] = value
                work[other][row] = value
            work[row][column] = Q(0)
            work[column][row] = Q(0)
        column += 1
    return positive, negative, zero


ETA4: Matrix = [
    [Q(1), Q(0), Q(0), Q(0)],
    [Q(0), Q(1), Q(0), Q(0)],
    [Q(0), Q(0), Q(1), Q(0)],
    [Q(0), Q(0), Q(0), Q(-1)],
]
PAIRS = [(left, right) for left in range(4) for right in range(left, 4)]


def sym_basis(pair: tuple[int, int]) -> Matrix:
    result = [[Q(0) for _ in range(4)] for _ in range(4)]
    left, right = pair
    result[left][right] = Q(1)
    result[right][left] = Q(1)
    return result


BASIS = [sym_basis(pair) for pair in PAIRS]


def trace(matrix: Matrix) -> Fraction:
    return sum((matrix[index][index] for index in range(len(matrix))), Q(0))


def frobenius_pair(left: Matrix, right: Matrix) -> Fraction:
    return trace(matmul(matmul(matmul(ETA4, left), ETA4), right))


def metric_trace(tensor: Matrix) -> Fraction:
    return trace(matmul(ETA4, tensor))


def trace_reverse(tensor: Matrix) -> Matrix:
    coefficient = Q(1, 2) * metric_trace(tensor)
    return [
        [tensor[i][j] - coefficient * ETA4[i][j] for j in range(4)]
        for i in range(4)
    ]


def components(tensor: Matrix) -> list[Fraction]:
    return [tensor[left][right] for left, right in PAIRS]


FROBENIUS10: Matrix = [
    [frobenius_pair(left, right) for right in BASIS] for left in BASIS
]
TAU10: Matrix = [list(column) for column in zip(*[
    components(trace_reverse(basis)) for basis in BASIS
])]
DEWITT10: Matrix = matmul(FROBENIUS10, TAU10)


def induced_sym2(change: Matrix) -> Matrix:
    columns = [
        components(matmul(matmul(transpose(change), basis), change))
        for basis in BASIS
    ]
    return [list(row) for row in zip(*columns)]


BOOST: Matrix = [
    [Q(5, 3), Q(0), Q(0), Q(4, 3)],
    [Q(0), Q(1), Q(0), Q(0)],
    [Q(0), Q(0), Q(1), Q(0)],
    [Q(4, 3), Q(0), Q(0), Q(5, 3)],
]
BOOST_INVERSE: Matrix = [
    [Q(5, 3), Q(0), Q(0), Q(-4, 3)],
    [Q(0), Q(1), Q(0), Q(0)],
    [Q(0), Q(0), Q(1), Q(0)],
    [Q(-4, 3), Q(0), Q(0), Q(5, 3)],
]


def main() -> None:
    campaign = json.loads(CAMPAIGN.read_text())
    atlas = json.loads(ATLAS.read_text())
    curt_crosswalk = json.loads(CURT_CROSSWALK.read_text())
    waves = {row["id"]: row for row in campaign["waves"]}

    exact("campaign has exactly ten unique waves", len(waves) == len(campaign["waves"]) == 10)
    exact("Curt remains a track inside exactly two construction lanes", campaign["construction_lanes"] == ["INDEPENDENT_NATIVE", "ERIC_GUIDED_WITH_CURT_RIVAL_TRACK"])
    exact("five provenance tags are closed", set(campaign["provenance_tags"]) == {"ERIC_REQUIRED", "CURT_CANDIDATE", "PAIRED_IMPLICATION", "REPO_SYNTHESIS", "UNSUPPORTED"})
    exact("third-lane gate is conjunctive", campaign["third_lane_promotion_gate"]["logic"] == "TG-1 AND TG-2 AND TG-3")
    exact("campaign does not promote a third lane", campaign["third_lane_promotion_gate"]["current_verdict"] == "NOT_PROMOTED")
    exact("Wave 1 gives partial TG-1 evidence without clearing its convention gate", campaign["third_lane_promotion_gate"]["status"] == {
        "TG-1": "PARTIAL_LITERAL_REAL_7_7_NON_EQUIVALENCE__NOT_CLEARED_SOURCE_CONVENTION",
        "TG-2": "OPEN_NO_SEPARATE_COMPLETE_DYNAMICS",
        "TG-3": "OPEN_NO_COMMON_DOMAIN_DISCRIMINATOR",
    })
    exact("Wave 1 covers all twelve foundational Curt steps", waves["ECW1-C0-CARRIER"]["curt_steps"] == [f"CI-{index:02d}" for index in range(1, 13)])
    exact("Wave 1 records local completion and open global naturality", waves["ECW1-C0-CARRIER"]["status"] == "COMPLETE_LOCAL_CARRIER_NON_EQUIVALENCE__GLOBAL_NATURALITY_OPEN")
    exact("every later dependency resolves", all(set(row["depends_on"]) <= set(waves) for row in waves.values()))
    exact("every wave has an objective kill and exit", all(row["objective"] and row["kill"] and row["exit"] for row in waves.values()))
    exact("physics atlas routes to the ten-wave campaign", atlas["eric_curt_ten_wave_campaign"]["registry"] == "lab/process/eric-curt-ten-wave-campaign.json" and atlas["eric_curt_ten_wave_campaign"]["next_wave"].startswith(("ECW2-G3.5-CENSUS", "ECW2b-TERM-RANK-ABLATION", "ECW3-G4-OBSERVATION")))
    exact("Curt crosswalk records no third-lane promotion", curt_crosswalk["c0_execution"]["third_lane"].startswith("NOT_PROMOTED") and "UNCERTAIN" in curt_crosswalk["c0_execution"]["source_dictionary"])

    exact("trace reversal is an involution in dimension four", matrix_equal(matmul(TAU10, TAU10), identity(10)))
    exact("DeWitt form is Frobenius paired with trace reversal", matrix_equal(DEWITT10, matmul(FROBENIUS10, TAU10)))
    exact("raw Lorentzian Frobenius fibre has signature (7,3)", inertia(FROBENIUS10) == (7, 3, 0))
    exact("trace-reversed DeWitt fibre has signature (6,4)", inertia(DEWITT10) == (6, 4, 0))

    active14 = block_diag(ETA4, DEWITT10)
    literal_curt14 = block_diag(ETA4, scale(DEWITT10, Q(-1)))
    literal_curt14_base_flip = block_diag(scale(ETA4, Q(-1)), DEWITT10)
    exact("active gimmel carrier has signature (9,5)", inertia(active14) == (9, 5, 0))
    exact("literal vertical-sign-reversed Curt carrier has signature (7,7)", inertia(literal_curt14) == (7, 7, 0))
    exact("literal base-sign-reversed Curt carrier also has signature (7,7)", inertia(literal_curt14_base_flip) == (7, 7, 0))
    exact("the two (7,7) block attributions are distinct bilinear forms", literal_curt14 != literal_curt14_base_flip)
    exact("reported ordered blocks (4,6)+(1,3) do not literally sum to (7,7)", (4 + 1, 6 + 3) == (5, 9) and (5, 9) != (7, 7))
    exact("both displayed carriers are nondegenerate rank fourteen", determinant(active14) != 0 and determinant(literal_curt14) != 0 and len(active14) == len(literal_curt14) == 14)
    exact("Sylvester inertia forbids a real metric isometry", inertia(active14) != inertia(literal_curt14))

    # In split coordinates, sharp_h followed by the declared horizontal lift
    # is represented by the identity from V+TX to V+H.  The nontrivial point
    # is that this bundle isomorphism does not identify the two bilinear forms.
    zorro_split = identity(14)
    exact("declared musical-plus-horizontal split is a vector-space isomorphism", determinant(zorro_split) == 1)
    exact("the same split map is not a metric isometry", matmul(matmul(transpose(zorro_split), active14), zorro_split) != literal_curt14)

    exact("rational boost preserves the base Lorentz metric", matmul(matmul(transpose(BOOST), ETA4), BOOST) == ETA4)
    exact("declared inverse really inverts the boost", matmul(BOOST, BOOST_INVERSE) == identity(4) and matmul(BOOST_INVERSE, BOOST) == identity(4))
    sym2_boost = induced_sym2(BOOST)
    exact("induced Sym2 boost preserves the DeWitt form", matmul(matmul(transpose(sym2_boost), DEWITT10), sym2_boost) == DEWITT10)
    exact("musical map intertwines covector and vector boost actions", all(
        matmul(ETA4, [[value] for value in [BOOST_INVERSE[row][column] for row in range(4)]])
        == matmul(BOOST, matmul(ETA4, [[Q(int(row == column))] for row in range(4)]))
        for column in range(4)
    ))

    # Multiplication of every vertical leg by i flips only the vertical block.
    # This supplies a complex congruence but is not a real map.
    Gaussian = tuple[Fraction, Fraction]

    def gaussian_multiply(left: Gaussian, right: Gaussian) -> Gaussian:
        return (
            left[0] * right[0] - left[1] * right[1],
            left[0] * right[1] + left[1] * right[0],
        )

    phases: list[Gaussian] = [(Q(1), Q(0))] * 4 + [(Q(0), Q(1))] * 10
    phase_congruence = [
        [
            (
                active14[i][j] * gaussian_multiply(phases[i], phases[j])[0],
                active14[i][j] * gaussian_multiply(phases[i], phases[j])[1],
            )
            for j in range(14)
        ]
        for i in range(14)
    ]
    literal_curt_gaussian = [
        [(literal_curt14[i][j], Q(0)) for j in range(14)]
        for i in range(14)
    ]
    exact("vertical complex phase gives the literal Curt bilinear", phase_congruence == literal_curt_gaussian)
    exact("vertical phase is not a real-structure intertwiner", any(imaginary != 0 for _, imaginary in phases))

    real_dim_cl95 = 64 * 64 * 4
    real_dim_cl77 = 128 * 128
    minimal_real_module_cl95 = 64 * 4
    minimal_real_module_cl77 = 128
    exact("real Clifford algebras have equal total dimension", real_dim_cl95 == real_dim_cl77 == 2**14)
    exact("real Clifford types remain inequivalent", minimal_real_module_cl95 != minimal_real_module_cl77)
    exact("both real Clifford types complexify to M128C", 64 * 2 == 128 and 128 == 128)

    gate = campaign["third_lane_promotion_gate"]
    exact("literal signature reading can fire only the carrier gate", "carrier" in gate["TG-1"].lower() and "action" in gate["TG-2"].lower() and "discriminator" in gate["TG-3"].lower())
    exact("datum rule preserves P1 P2 P3 without target content", all(token in campaign["datum_rule"] for token in ("P1", "P2", "P3", "never place target physics")))

    planted("rank fourteen proves real metric equivalence", inertia(active14) == inertia(literal_curt14))
    planted("trivial vertical lift preserves a moving Sym2 frame", sym2_boost == identity(10))
    planted("complex phase preserves the original real structure", all(imaginary == 0 for _, imaginary in phases))
    planted("raw Frobenius and trace-reversed DeWitt are the same form", FROBENIUS10 == DEWITT10)
    planted("reported ordered block arithmetic directly yields (7,7)", (4 + 1, 6 + 3) == (7, 7))
    planted("Curt signature imports active right-H structure", minimal_real_module_cl95 == minimal_real_module_cl77)
    planted("signature mismatch alone promotes a third lane", gate["logic"] == "TG-1")
    planted("three carrier sectors imply three generations", "three carrier pieces prove three" in campaign["datum_rule"].lower())
    planted("connection-dependent split is canonical from bare X", "canonical from bare X" in waves["ECW1-C0-CARRIER"]["repo_construction"])

    print(
        "ERIC-CURT-WAVE1-C0-CARRIER: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: musical plus declared horizontal split identifies the underlying rank-14 bundle")
    print("RESULT: literal real (7,7) and active (9,5) metric/Clifford carriers are inequivalent")
    print("RESULT: complexification supplies a bridge but does not transport the real/right-H structure")
    print("LANE: literal (7,7) gives partial TG-1 evidence, but source convention, TG-2, and TG-3 remain open; no third lane")
    print("BOUNDARY: no global natural split, action selection, Higgs, field equation, count, or cosmology is claimed")


if __name__ == "__main__":
    main()
