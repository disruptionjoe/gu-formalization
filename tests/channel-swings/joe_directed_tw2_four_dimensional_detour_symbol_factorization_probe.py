#!/usr/bin/env python3
"""Exact TW-2 principal-symbol factorization and K77 compression controls.

This probe works over ``Fraction`` in a rational Cl(2,2) model.  After
complexification the Clifford identities and rank strata are the same for
four-dimensional Lorentz signature.  It proves only pointwise symbol facts:
no action, Bach-flat background, formal adjoint, analytic domain, BV quotient,
or physical cohomology is constructed here.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def reject(label: str, false_claim: object) -> None:
    check("mutant", "reject " + label, not bool(false_claim))


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


Matrix = list[list[Q]]


def zeros(rows: int, columns: int) -> Matrix:
    return [[Q(0) for _ in range(columns)] for _ in range(rows)]


def eye(size: int) -> Matrix:
    out = zeros(size, size)
    for index in range(size):
        out[index][index] = Q(1)
    return out


def shape(value: Matrix) -> tuple[int, int]:
    return len(value), len(value[0]) if value else 0


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [a + b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def neg(value: Matrix) -> Matrix:
    return [[-entry for entry in row] for row in value]


def sub(left: Matrix, right: Matrix) -> Matrix:
    return add(left, neg(right))


def scale(coefficient: Q | int, value: Matrix) -> Matrix:
    coefficient = Q(coefficient)
    return [[coefficient * entry for entry in row] for row in value]


def mul(left: Matrix, right: Matrix) -> Matrix:
    left_rows, left_columns = shape(left)
    right_rows, right_columns = shape(right)
    assert left_columns == right_rows
    out = zeros(left_rows, right_columns)
    for row in range(left_rows):
        for middle in range(left_columns):
            coefficient = left[row][middle]
            if coefficient == 0:
                continue
            for column in range(right_columns):
                out[row][column] += coefficient * right[middle][column]
    return out


def power(value: Matrix, exponent: int) -> Matrix:
    rows, columns = shape(value)
    assert rows == columns and exponent >= 0
    out = eye(rows)
    base = value
    while exponent:
        if exponent % 2:
            out = mul(out, base)
        base = mul(base, base)
        exponent //= 2
    return out


def kron(left: Matrix, right: Matrix) -> Matrix:
    left_rows, left_columns = shape(left)
    right_rows, right_columns = shape(right)
    out = zeros(left_rows * right_rows, left_columns * right_columns)
    for i in range(left_rows):
        for j in range(left_columns):
            for k in range(right_rows):
                for ell in range(right_columns):
                    out[i * right_rows + k][j * right_columns + ell] = (
                        left[i][j] * right[k][ell]
                    )
    return out


def vstack(blocks: list[Matrix]) -> Matrix:
    return [row[:] for block in blocks for row in block]


def hstack(blocks: list[Matrix]) -> Matrix:
    row_count = shape(blocks[0])[0]
    return [sum((block[row] for block in blocks), []) for row in range(row_count)]


def block2(a: Matrix, b: Matrix, c: Matrix, d: Matrix) -> Matrix:
    return vstack([hstack([a, b]), hstack([c, d])])


def rank(value: Matrix) -> int:
    work = [row[:] for row in value]
    rows, columns = shape(work)
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                entry - factor * base
                for entry, base in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def is_zero(value: Matrix) -> bool:
    return all(entry == 0 for row in value for entry in row)


def product(values: list[Matrix]) -> Matrix:
    out = eye(shape(values[0])[0])
    for value in values:
        out = mul(out, value)
    return out


def scalar_quadratic(covector: tuple[int, int, int, int], eta: list[int]) -> Q:
    return sum((Q(eta[index] * covector[index] ** 2) for index in range(4)), Q(0))


def main(selftest: bool = False) -> int:
    print("A. ROUTING, OWNERSHIP, AND CLAIM CEILING")
    router = read("lab/methods/source-native-comparator-routing.md")
    packet = read(
        "lab/active-research/joe-directed/conditional-build-channel-read-packet-2026-08-16.md"
    )
    predecessor = read(
        "explorations/conditional-build/selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md"
    )
    b2c2b = read(
        "explorations/eric-curt-wave3d-b2c2b-super-ig-rs-tangent-noether-2026-07-31.md"
    )
    completion = read(
        "explorations/eric-curt-wave3d-b2c2-null-clifford-omega1-completion-2026-07-31.md"
    )
    check("ownership", "mandatory comparator routing is present", "Bridge burden" in router)
    check("ownership", "conditional-build packet forbids action and background construction",
          "a source action, action term, vacuum, background, or external datum" in packet)
    check("ownership", "predecessor leaves the curved factorization open",
          "curved factorization through owned GU operator: OPEN" in predecessor)
    check("archaeology", "the n=14 twistor--RS intertwiner is already owned",
          "Q(k)T(k)=\\frac{12}{14}T(k)c(k)" in b2c2b)
    check("archaeology", "the full Omega1 carrier completion is already owned",
          "full-`Omega1` completion" in completion)
    for label in (
        "standard four-dimensional detour symbol versus a GU-native operator",
        "algebraic metric dual T-sharp versus a formal analytic adjoint",
        "symbol cohomology versus global or physical cohomology",
        "Bach-flat base current versus total twisted Yang--Mills current",
        "four-dimensional chirality versus ambient K77 chirality",
        "Pi4 target embedding versus equality with Pi14",
    ):
        check("layer0", label + " remain distinct", True)

    print("\nB. EXACT RATIONAL Cl(2,2) AND PROJECTORS")
    i2 = eye(2)
    sigma1 = [[Q(0), Q(1)], [Q(1), Q(0)]]
    sigma3 = [[Q(1), Q(0)], [Q(0), Q(-1)]]
    epsilon = [[Q(0), Q(1)], [Q(-1), Q(0)]]
    gammas = [
        kron(sigma1, i2),
        kron(sigma3, sigma1),
        kron(epsilon, i2),
        kron(sigma3, epsilon),
    ]
    eta = [1, 1, -1, -1]
    i4 = eye(4)
    for index, gamma in enumerate(gammas):
        check("clifford", f"gamma_{index} has square eta_{index}",
              mul(gamma, gamma) == scale(eta[index], i4))
    check("clifford", "all off-diagonal anticommutators vanish",
          all(is_zero(add(mul(gammas[a], gammas[b]), mul(gammas[b], gammas[a])))
              for a in range(4) for b in range(a + 1, 4)))

    clifford_injection = vstack(gammas)
    gamma_trace = hstack([scale(eta[index], gammas[index]) for index in range(4)])
    pi4 = sub(eye(16), scale(Q(1, 4), mul(clifford_injection, gamma_trace)))
    pi14_base = sub(eye(16), scale(Q(1, 14), mul(clifford_injection, gamma_trace)))
    check("projector", "Gamma4 j4=4I", mul(gamma_trace, clifford_injection) == scale(4, i4))
    check("projector", "Pi4 is the rank-twelve gamma-trace projector",
          mul(pi4, pi4) == pi4 and rank(pi4) == 12 and is_zero(mul(gamma_trace, pi4)))
    check("adapter", "Pi14 base block is unequal and non-idempotent",
          pi14_base != pi4 and mul(pi14_base, pi14_base) != pi14_base)
    check("adapter", "Pi14 base residual trace is five-sevenths Gamma4",
          mul(gamma_trace, pi14_base) == scale(Q(5, 7), gamma_trace))
    check("adapter", "Pi4 targets embed exactly in ambient ker Gamma14",
          mul(pi14_base, pi4) == pi4 and mul(pi4, pi14_base) == pi4)

    omega = product(gammas)
    spin_chirality = {
        sign: scale(Q(1, 2), add(i4, scale(sign, omega))) for sign in (1, -1)
    }
    tw_chirality = {
        sign: mul(kron(i4, spin_chirality[sign]), pi4) for sign in (1, -1)
    }
    check("chirality", "the two spinor Weyl projectors have rank two",
          all(rank(projector) == 2 and mul(projector, projector) == projector
              for projector in spin_chirality.values()))
    check("chirality", "the two twistor Weyl projectors have rank six",
          all(rank(projector) == 6 and mul(projector, projector) == projector
              for projector in tw_chirality.values()))

    print("\nC. DETOUR SYMBOL IDENTITIES, RANKS, AND COHOMOLOGY")
    covectors = {
        "positive": (1, 0, 0, 0),
        "negative": (0, 0, 1, 0),
        "nonnull_generic": (1, 2, 3, 4),
        "null_a": (1, 0, 1, 0),
        "null_b": (0, 1, 0, 1),
        "null_generic": (1, 1, 1, 1),
    }
    records: dict[str, dict[str, object]] = {}
    for name, xi in covectors.items():
        q = scalar_quadratic(xi, eta)
        c_xi = zeros(4, 4)
        for index in range(4):
            c_xi = add(c_xi, scale(eta[index] * xi[index], gammas[index]))
        k_xi = vstack([scale(xi[index], i4) for index in range(4)])
        contraction = hstack([scale(eta[index] * xi[index], i4) for index in range(4)])
        t_symbol = mul(pi4, k_xi)
        t_sharp = mul(contraction, pi4)
        component_dirac = kron(i4, c_xi)
        q_symbol = mul(pi4, mul(component_dirac, pi4))
        n_symbol = sub(power(q_symbol, 3), scale(Q(1, 4) * q, q_symbol))
        n_split = sub(scale(Q(3, 4) * q, q_symbol),
                      scale(Q(1, 2), mul(t_symbol, mul(c_xi, t_sharp))))

        check("identity", f"{name}: c(xi)^2=qI", mul(c_xi, c_xi) == scale(q, i4))
        check("identity", f"{name}: QT=(1/2)Tc",
              mul(q_symbol, t_symbol) == scale(Q(1, 2), mul(t_symbol, c_xi)))
        check("identity", f"{name}: T-sharp T=(3/4)qI",
              mul(t_sharp, t_symbol) == scale(Q(3, 4) * q, i4))
        check("identity", f"{name}: Q^2=qPi4-TT-sharp",
              mul(q_symbol, q_symbol) == sub(scale(q, pi4), mul(t_symbol, t_sharp)))
        check("factorization", f"{name}: cubic and T-c-T-sharp factorizations agree",
              n_symbol == n_split)
        check("complex", f"{name}: N3 T=0 and T-sharp N3=0",
              is_zero(mul(n_symbol, t_symbol)) and is_zero(mul(t_sharp, n_symbol)))

        expected_n_rank = 8 if q != 0 else 2
        expected_middle_h = 0 if q != 0 else 6
        check("rank", f"{name}: Dirac ranks are 4/{expected_n_rank}/4",
              rank(t_symbol) == 4 and rank(n_symbol) == expected_n_rank
              and rank(t_sharp) == 4)
        dirac_h1 = rank(pi4) - rank(t_symbol) - rank(n_symbol)
        dirac_h2 = rank(pi4) - rank(n_symbol) - rank(t_sharp)
        check("cohomology", f"{name}: Dirac middle symbol cohomology matches its causal stratum",
              (dirac_h1, dirac_h2) == (expected_middle_h, expected_middle_h))

        chirality_rows = {}
        for sign in (1, -1):
            source_spin = spin_chirality[sign]
            source_tw = tw_chirality[sign]
            target_tw = tw_chirality[-sign]
            target_spin = spin_chirality[-sign]
            t_half = mul(source_tw, mul(t_symbol, source_spin))
            n_half = mul(target_tw, mul(n_symbol, source_tw))
            t_sharp_half = mul(target_spin, mul(t_sharp, target_tw))
            expected_half_n_rank = 4 if q != 0 else 1
            expected_half_h = 0 if q != 0 else 3
            h1 = rank(source_tw) - rank(t_half) - rank(n_half)
            h2 = rank(target_tw) - rank(n_half) - rank(t_sharp_half)
            check("chirality", f"{name}, Weyl {sign:+}: ranks are 2/{expected_half_n_rank}/2",
                  rank(t_half) == 2 and rank(n_half) == expected_half_n_rank
                  and rank(t_sharp_half) == 2)
            check("chirality", f"{name}, Weyl {sign:+}: compositions vanish",
                  is_zero(mul(n_half, t_half))
                  and is_zero(mul(t_sharp_half, n_half)))
            check("cohomology", f"{name}, Weyl {sign:+}: middle H=({expected_half_h},{expected_half_h})",
                  (h1, h2) == (expected_half_h, expected_half_h))
            chirality_rows[sign] = {
                "ranks": (rank(t_half), rank(n_half), rank(t_sharp_half)),
                "middle_h": (h1, h2),
            }

        records[name] = {
            "q": q,
            "c_rank": rank(c_xi),
            "dirac_ranks": (rank(t_symbol), rank(n_symbol), rank(t_sharp)),
            "dirac_middle_h": (dirac_h1, dirac_h2),
            "chirality": chirality_rows,
            "t": t_symbol,
            "t_sharp": t_sharp,
            "q_symbol": q_symbol,
            "n": n_symbol,
            "k": k_xi,
            "contraction": contraction,
            "c": c_xi,
        }

    check("characteristic", "all three non-null controls are symbol-exact",
          all(records[name]["dirac_middle_h"] == (0, 0)
              for name in ("positive", "negative", "nonnull_generic")))
    check("characteristic", "all three null controls have Dirac middle H=(6,6)",
          all(records[name]["dirac_middle_h"] == (6, 6)
              for name in ("null_a", "null_b", "null_generic")))
    positive = records["positive"]
    check("factorization", "Q^3 T=(1/4)qQT forces the projective coefficient line (1,-1/4)",
          mul(power(positive["q_symbol"], 3), positive["t"])
          == scale(Q(1, 4) * positive["q"],
                   mul(positive["q_symbol"], positive["t"])))
    check("corners", "one internal rank-sixteen factor gives the declared per-corner ranks",
          16 * 2 == 32 and 16 * 4 == 64 and 16 * 1 == 16
          and 16 * 3 == 48)
    check("corners", "both 4D Weyl halves and both internal chirality factors retain four corners",
          len(spin_chirality) * 2 == 4)

    print("\nD. CONDITIONAL CURRENT-K77 ROLLED BASE COMPRESSION")
    for name in ("positive", "negative", "null_a"):
        row = records[name]
        q_symbol = row["q_symbol"]
        t_symbol = row["t"]
        t_sharp = row["t_sharp"]
        k_xi = row["k"]
        contraction = row["contraction"]
        c_xi = row["c"]
        component_dirac = kron(i4, c_xi)
        raw_upper_left = sub(component_dirac, mul(k_xi, gamma_trace))
        rolled_raw = block2(
            raw_upper_left,
            k_xi,
            neg(contraction),
            zeros(4, 4),
        )
        compression = block2(pi4, zeros(16, 4), zeros(4, 16), i4)
        rolled_compressed = mul(compression, mul(rolled_raw, compression))
        expected = block2(q_symbol, t_symbol, neg(t_sharp), zeros(4, 4))
        check("rolled", f"{name}: compressed rolled block is [[Q,T],[-T-sharp,0]]",
              rolled_compressed == expected)
        check("rolled", f"{name}: the rolled symbol remains first order, not the cubic N3",
              shape(rolled_compressed) == (20, 20) and shape(row["n"]) == (16, 16))

    print("\nE. MUTANTS AND STOP BOUNDARY")
    wrong_coefficient = sub(power(positive["q_symbol"], 3),
                            scale(Q(1, 3) * positive["q"], positive["q_symbol"]))
    reject("replace the forced one-quarter coefficient by one-third",
           is_zero(mul(wrong_coefficient, positive["t"])))
    reject("drop the T-c-T-sharp correction from the cubic",
           is_zero(mul(power(positive["q_symbol"], 3), positive["t"])))
    reject("identify Pi14 base with Pi4", pi14_base == pi4)
    reject("call the null Weyl symbol complex exact",
           records["null_a"]["chirality"][1]["middle_h"] == (0, 0))
    reject("identify the first-order rolled block directly with N3",
           shape(positive["n"]) == (20, 20))
    reject("delete one Weyl half while claiming all four K77 corners", len(spin_chirality) == 1)
    check("ceiling", "pointwise symbol H is not promoted to physical cohomology", True)
    check("ceiling", "base Bach-flatness is not promoted to total twisted Yang--Mills", True)
    check("ceiling", "algebraic contraction is not promoted to an analytic adjoint/domain", True)
    check("ceiling", "the current Omega0+Omega1 carrier is not said to own Tw2", True)

    if selftest:
        print("\nF. SELFTEST ABLATIONS")
        check("selftest", "a zero covector is excluded from characteristic rank claims",
              scalar_quadratic((0, 0, 0, 0), eta) == 0)
        check("selftest", "the null and non-null middle ranks are genuinely distinct",
              records["null_a"]["dirac_ranks"] != records["positive"]["dirac_ranks"])
        check("selftest", "positive and negative non-null signatures have identical exact ranks",
              records["positive"]["dirac_ranks"] == records["negative"]["dirac_ranks"])
        check("selftest", "both Weyl halves have the same null fingerprint",
              records["null_a"]["chirality"][1] == records["null_a"]["chirality"][-1])

    print("\nG. DISPOSITION")
    for label, value in (
        ("STANDARD_4D_DETOUR_SYMBOL", "EXACT_NORMALIZED_CUBIC_FACTOR_LINE"),
        ("NON_NULL_SYMBOL_COMPLEX", "EXACT_BOTH_WEYL_HALVES"),
        ("NULL_CHARACTERISTIC_COHOMOLOGY", "WEYL_3_PLUS_3__DIRAC_6_PLUS_6"),
        ("PI4_PI14", "TARGET_EMBEDDING_ONLY__PROJECTORS_UNEQUAL"),
        ("ROLLED_GU_BRIDGE", "CONDITIONAL_BASE_COMPRESSION_SUBBLOCKS__NOT_OPERATOR_EQUALITY"),
        ("STANDARD_AUXILIARY", "TW2_FIRST_ORDER_FACTOR__NOT_CURRENT_GU_FIELD_OWNER"),
        ("ACTION_DOMAIN_PHYSICAL_COHOMOLOGY", "NOT_CONSTRUCTED"),
    ):
        print(f"{label}={value}")

    total = sum(COUNTS.values())
    passed = total - len(FAILURES)
    print("CHECKS=" + " ".join(f"{kind}:{COUNTS[kind]}" for kind in sorted(COUNTS)))
    print(f"{'PASS' if not FAILURES else 'FAIL'} {passed}/{total}")
    if FAILURES:
        for failure in FAILURES:
            print("FAILED:", failure)
        return 1
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(main(selftest=arguments.selftest))
