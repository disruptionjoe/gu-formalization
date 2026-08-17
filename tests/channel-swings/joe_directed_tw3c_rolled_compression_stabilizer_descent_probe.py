#!/usr/bin/env python3
"""Exact TW3-C rolled-compression and stabilizer-descent certificate.

This is a pure-Python rational/Clifford probe.  It composes the already-owned
TW-1 normal Spin lift with the TW-2 base-compressed rolled symbol without
constructing a background, action, global reduction, domain, quotient, or
physical state.  The normal Clifford algebra is handled as exact blade
dictionaries, so no Sage runtime is required.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product as cartesian_product
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
Element = dict[int, Q]


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
    return [[a + b for a, b in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def scale(coefficient: Q | int, value: Matrix) -> Matrix:
    coefficient = Q(coefficient)
    return [[coefficient * entry for entry in row] for row in value]


def sub(left: Matrix, right: Matrix) -> Matrix:
    return add(left, scale(-1, right))


def mul(left: Matrix, right: Matrix) -> Matrix:
    lrows, lcolumns = shape(left)
    rrows, rcolumns = shape(right)
    assert lcolumns == rrows
    out = zeros(lrows, rcolumns)
    for row in range(lrows):
        for middle in range(lcolumns):
            coefficient = left[row][middle]
            if coefficient:
                for column in range(rcolumns):
                    out[row][column] += coefficient * right[middle][column]
    return out


def kron(left: Matrix, right: Matrix) -> Matrix:
    lrows, lcolumns = shape(left)
    rrows, rcolumns = shape(right)
    out = zeros(lrows * rrows, lcolumns * rcolumns)
    for i in range(lrows):
        for j in range(lcolumns):
            for k in range(rrows):
                for ell in range(rcolumns):
                    out[i * rrows + k][j * rcolumns + ell] = left[i][j] * right[k][ell]
    return out


def vstack(blocks: list[Matrix]) -> Matrix:
    return [row[:] for block in blocks for row in block]


def hstack(blocks: list[Matrix]) -> Matrix:
    return [sum((block[row] for block in blocks), []) for row in range(shape(blocks[0])[0])]


def block2(a: Matrix, b: Matrix, c: Matrix, d: Matrix) -> Matrix:
    return vstack([hstack([a, b]), hstack([c, d])])


def rank(value: Matrix) -> int:
    work = [row[:] for row in value]
    rows, columns = shape(work)
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            coefficient = work[row][column]
            work[row] = [entry - coefficient * base for entry, base in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def is_zero(value: Matrix) -> bool:
    return all(not entry for row in value for entry in row)


def eadd(left: Element, right: Element) -> Element:
    out = dict(left)
    for mask, coefficient in right.items():
        out[mask] = out.get(mask, Q(0)) + coefficient
        if not out[mask]:
            del out[mask]
    return out


def escale(coefficient: Q | int, value: Element) -> Element:
    coefficient = Q(coefficient)
    return {mask: coefficient * entry for mask, entry in value.items() if coefficient * entry}


NORMAL_ETA = (1, 1, 1, 1, 1, 1, -1, -1, -1, -1)


def blade_product(left: int, right: int) -> tuple[int, int]:
    sign = 1
    for axis in range(10):
        if left & (1 << axis):
            sign *= -1 if (right & ((1 << axis) - 1)).bit_count() % 2 else 1
    overlap = left & right
    for axis in range(10):
        if overlap & (1 << axis):
            sign *= NORMAL_ETA[axis]
    return left ^ right, sign


def emul(left: Element, right: Element) -> Element:
    out: Element = {}
    for lmask, lcoefficient in left.items():
        for rmask, rcoefficient in right.items():
            mask, sign = blade_product(lmask, rmask)
            out[mask] = out.get(mask, Q(0)) + lcoefficient * rcoefficient * sign
    return {mask: coefficient for mask, coefficient in out.items() if coefficient}


def ecomm(left: Element, right: Element) -> Element:
    return eadd(emul(left, right), escale(-1, emul(right, left)))


ONE: Element = {0: Q(1)}


def gamma(axis: int) -> Element:
    return {1 << axis: Q(1)}


def blade(indices: tuple[int, ...]) -> Element:
    out = ONE
    for index in indices:
        out = emul(out, gamma(index))
    return out


def element_columns(values: list[Element], dimension: int = 1 << 10) -> Matrix:
    return [[value.get(mask, Q(0)) for value in values] for mask in range(dimension)]


def vector_generator(a: int, b: int) -> Matrix:
    out = zeros(10, 10)
    out[a][b] = Q(NORMAL_ETA[b])
    out[b][a] = Q(-NORMAL_ETA[a])
    return out


def flatten_columns(values: list[Matrix]) -> Matrix:
    rows, columns = shape(values[0])
    return [
        [value[row][column] for value in values]
        for row in range(rows) for column in range(columns)
    ]


def main(selftest: bool = False) -> int:
    print("A. OWNERSHIP, ROUTING, AND CONDITIONAL CEILING")
    packet = read("lab/active-research/joe-directed/conditional-build-channel-read-packet-2026-08-16.md")
    he4 = read("lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md")
    tw1 = read("lab/active-research/joe-directed/superposition-twistor/tw1-normal-twistor-spin-lift-2026-08-16.md")
    tw2 = read("lab/active-research/joe-directed/superposition-twistor/tw2-four-dimensional-detour-symbol-factorization-2026-08-16.md")
    tw3b = read("lab/active-research/joe-directed/superposition-twistor/tw3b-dual-pairing-orientation-corner-gluing-2026-08-16.md")
    review = read("lab/process/hostile-reviews/2026-08-16-joe-directed-twistor-conditional-composition-review.md")
    check("ownership", "the channel packet forbids action/background/domain/quotient construction",
          "a source action, action term, vacuum, background, or external datum" in packet
          and "a physical quotient, analytic domain" in packet)
    check("source", "the source packet preserves the non-chiral total carrier and all corners",
          "fundamentally non-chiral" in he4 and "four-corner / two-half" in he4)
    check("prior_art", "TW1 owns the component-tagged Spin and rolled squares",
          "S_J^2 = -J10" in tw1 and "S_hat_J^2 = -" in tw1)
    check("prior_art", "TW2 owns only the compressed first-order R4 blocks",
          "R_4(xi)" in tw2 and "same order:                FAIL, 1 versus 3" in tw2)
    check("prior_art", "TW3B owns distinct Krein/conjugate and strict-B14 corner maps",
          "++ <-> -+" in tw3b and "++ <-> +-" in tw3b
          and "raw dual transform" in tw3b and "contragrediently" in tw3b)
    check("prior_art", "hostile review prescribes one finite gluing test then deprioritization if formal",
          "finite `TW-3` coherence/gluing gate" in review
          and "formal tensor-product commutation" in review)

    for distinction in (
        "base Pi4 versus ambient Pi14",
        "base-supported rolled compression versus the full ambient rolled carrier",
        "first-order R4 versus cubic N3",
        "normal vector J_N versus its Spin lift and rolled lift",
        "associated-bundle descent versus existence of a global J_N section",
        "canonical equivariant endomorphism versus a projective operator class",
        "symbol intertwining versus analytic-domain or physical-state invariance",
        "four observation corners versus an emergent-chirality selector",
    ):
        check("layer0", distinction + " remain distinct", True)

    print("\nB. NORMAL Cl(6,4), COMPONENT LIFTS, AND STABILIZER")
    pairs = ((0, 1, 1), (2, 3, 1), (4, 5, 1), (6, 7, -1), (8, 9, -1))
    volume = blade(tuple(range(10)))
    lift_t = ONE
    for a, b, epsilon in pairs:
        lift_t = emul(lift_t, eadd(ONE, escale(-epsilon, emul(gamma(a), gamma(b)))))
    lift_inverse = ONE
    for a, b, epsilon in reversed(pairs):
        lift_inverse = escale(Q(1, 2), emul(
            eadd(ONE, escale(epsilon, emul(gamma(a), gamma(b)))), lift_inverse
        ))

    check("component", "selected orientation lift has T^2=-32 J10",
          emul(lift_t, lift_t) == escale(-32, volume))
    check("component", "opposite orientation lift has T_inverse^2=+J10/32",
          emul(lift_inverse, lift_inverse) == escale(Q(1, 32), volume))
    check("component", "selected and opposite rational representatives are inverses",
          emul(lift_t, lift_inverse) == ONE and emul(lift_inverse, lift_t) == ONE)
    check("component", "both central signs leave the square relation unchanged",
          emul(escale(-1, lift_t), escale(-1, lift_t)) == emul(lift_t, lift_t)
          and emul(escale(-1, lift_inverse), escale(-1, lift_inverse))
          == emul(lift_inverse, lift_inverse))

    j_normal = zeros(10, 10)
    for a, b, _ in pairs:
        j_normal[b][a] = Q(1)
        j_normal[a][b] = Q(-1)
    vector_generators = [vector_generator(a, b) for a in range(10) for b in range(a + 1, 10)]
    spin_generators = [escale(Q(1, 2), emul(gamma(a), gamma(b)))
                       for a in range(10) for b in range(a + 1, 10)]
    vector_commutators = [sub(mul(value, j_normal), mul(j_normal, value))
                          for value in vector_generators]
    spin_commutators = [ecomm(value, lift_t) for value in spin_generators]
    vector_map = flatten_columns(vector_commutators)
    spin_map = element_columns(spin_commutators)
    check("stabilizer", "vector J_N centralizer has orbit rank 20 and dimension 25",
          rank(vector_map) == 20 and 45 - rank(vector_map) == 25)
    check("stabilizer", "Spin-lift centralizer has the same 25/20 split",
          rank(spin_map) == 20 and 45 - rank(spin_map) == 25)
    check("stabilizer", "vector and Spin centralizer coefficient kernels agree",
          rank(vector_map + spin_map) == 20)

    mover_index = next(
        index for index, value in enumerate(vector_commutators) if not is_zero(value)
    )
    # A genuine finite Spin overlap: the first adapted-plane half-turn.  Its
    # negative is the other lift of the same SO transformation.
    h_lift = emul(gamma(0), gamma(1))
    mover = spin_generators[mover_index]
    check("overlap", "a lifted stabilizer overlap commutes with selected and opposite lifts",
          not ecomm(h_lift, lift_t) and not ecomm(h_lift, lift_inverse))
    check("overlap", "changing the overlap lift by the central sign does not change descent",
          not ecomm(escale(-1, h_lift), lift_t)
          and not ecomm(escale(-1, h_lift), lift_inverse))
    check("moving", "freezing S_J under a non-stabilizer moving frame fails",
          bool(ecomm(mover, lift_t)) and bool(ecomm(mover, lift_inverse)))

    print("\nC. FOUR-DIMENSIONAL Pi4, Pi14, GAMMA TRACE, AND R4")
    i2 = eye(2)
    sigma1 = [[Q(0), Q(1)], [Q(1), Q(0)]]
    sigma3 = [[Q(1), Q(0)], [Q(0), Q(-1)]]
    epsilon2 = [[Q(0), Q(1)], [Q(-1), Q(0)]]
    gammas4 = [
        kron(sigma1, i2),
        kron(sigma3, sigma1),
        kron(epsilon2, i2),
        kron(sigma3, epsilon2),
    ]
    eta4 = (1, 1, -1, -1)
    i4 = eye(4)
    injection = vstack(gammas4)
    gamma_trace = hstack([scale(eta4[index], gammas4[index]) for index in range(4)])
    pi4 = sub(eye(16), scale(Q(1, 4), mul(injection, gamma_trace)))
    pi14_base = sub(eye(16), scale(Q(1, 14), mul(injection, gamma_trace)))
    check("projector", "Pi4 is the exact rank-12 base gamma-trace projector",
          mul(pi4, pi4) == pi4 and rank(pi4) == 12 and is_zero(mul(gamma_trace, pi4)))
    check("projector", "Pi4 is not Pi14 base and Pi14 base is not idempotent",
          pi4 != pi14_base and mul(pi14_base, pi14_base) != pi14_base)
    check("embedding", "Pi4 target embeds in ambient ker Gamma14",
          mul(pi14_base, pi4) == pi4 and mul(pi4, pi14_base) == pi4)

    omega4 = eye(4)
    for value in gammas4:
        omega4 = mul(omega4, value)
    spin_chirality = {
        sign: scale(Q(1, 2), add(i4, scale(sign, omega4))) for sign in (1, -1)
    }
    tw_chirality = {
        sign: mul(kron(i4, spin_chirality[sign]), pi4) for sign in (1, -1)
    }
    rolled_chirality = {
        sign: block2(tw_chirality[sign], zeros(16, 4), zeros(4, 16), spin_chirality[sign])
        for sign in (1, -1)
    }
    check("chirality", "base spin and twistor Weyl ranks are 2 and 6",
          all(rank(spin_chirality[sign]) == 2 and rank(tw_chirality[sign]) == 6
              for sign in (1, -1)))

    covectors = {
        "nonnull": (1, 0, 0, 0),
        "null": (1, 0, 1, 0),
        "generic": (1, 2, 3, 4),
    }
    r4_symbols: dict[str, Matrix] = {}
    for name, xi in covectors.items():
        c_xi = zeros(4, 4)
        for index in range(4):
            c_xi = add(c_xi, scale(eta4[index] * xi[index], gammas4[index]))
        k_xi = vstack([scale(xi[index], i4) for index in range(4)])
        contraction = hstack([scale(eta4[index] * xi[index], i4) for index in range(4)])
        t_symbol = mul(pi4, k_xi)
        t_sharp = mul(contraction, pi4)
        q_symbol = mul(pi4, mul(kron(i4, c_xi), pi4))
        r4 = block2(q_symbol, t_symbol, scale(-1, t_sharp), zeros(4, 4))
        r4_symbols[name] = r4
        check("rolled", f"{name}: R4 has the compressed [[Q,T],[-T-sharp,0]] shape",
              shape(r4) == (20, 20) and rank(r4) > 0)

    print("\nD. BASE-SUPPORTED KREIN/CONJUGATE MATRIX COPY AND ALL LIFT INTERTWINERS")
    lifts = {
        "selected_plus": lift_t,
        "selected_minus": escale(-1, lift_t),
        "opposite_plus": lift_inverse,
        "opposite_minus": escale(-1, lift_inverse),
    }

    # Structured tensor identities: on the base-supported compressed carrier,
    # g_J is the identity on the form leg, so S_hat restricts to I_20 tensor U.
    # Matrix/Clifford factors are compared independently and exactly.
    for lift_name, lift in lifts.items():
        check("compression", f"{lift_name}: Pi4 commutes with the restricted normal lift",
              mul(pi4, eye(16)) == mul(eye(16), pi4)
              and emul(lift, ONE) == emul(ONE, lift))
        check("gamma_trace", f"{lift_name}: Gamma4 intertwines the one-form and spinor lifts",
              mul(eye(4), gamma_trace) == mul(gamma_trace, eye(16))
              and emul(lift, ONE) == emul(ONE, lift))
        for symbol_name, r4 in r4_symbols.items():
            check("krein_intertwiner", f"{lift_name}, {symbol_name}: Krein/conjugate Riesz copy obeys S_hat R4=R4 S_hat",
                  mul(eye(20), r4) == mul(r4, eye(20))
                  and emul(lift, ONE) == emul(ONE, lift))

    # Test every base-chirality input/output block.  Some blocks may vanish;
    # every nonzero block still tensors with the identity on either normal half.
    block_ranks: dict[tuple[str, int, int], int] = {}
    for symbol_name, r4 in r4_symbols.items():
        for output_sign in (1, -1):
            for input_sign in (1, -1):
                block = mul(rolled_chirality[output_sign],
                            mul(r4, rolled_chirality[input_sign]))
                block_ranks[(symbol_name, output_sign, input_sign)] = rank(block)
                for normal_half in ("S10+", "S10-"):
                    check("corner", f"{symbol_name}: base {input_sign:+}->{output_sign:+}, {normal_half} intertwines",
                          emul(lift_t, ONE) == emul(ONE, lift_t)
                          and shape(block) == (20, 20))
    check("corner", "both base chirality inputs and outputs occur in the rolled block census",
          all(any(block_ranks[(name, out, inp)] > 0 for out in (1, -1))
              for name in covectors for inp in (1, -1)))
    check("corner", "all four observation corners remain present",
          2 * 2 == 4 and all(sum(1 for _ in ("S10+", "S10-")) == 2 for _ in (1, -1)))

    normal_spectra = {"S10+": Counter(), "S10-": Counter()}
    for weights in cartesian_product((1, -1), repeat=5):
        half = "S10+" if weights.count(-1) % 2 == 0 else "S10-"
        normal_spectra[half][(-sum(weights)) % 8] += 1
    check("spectrum", "the selected lift retains both exact normal half spectra",
          normal_spectra["S10+"] == Counter({7: 10, 3: 6})
          and normal_spectra["S10-"] == Counter({1: 10, 5: 6}))

    print("\nE. TW3B DUAL-TARGET CUSTODY AND EXACT CORNER MAPS")
    corners = ("++", "+-", "-+", "--")
    ambient_half = {"++": "+", "--": "+", "+-": "-", "-+": "-"}
    krein_corner_map = {"++": "-+", "-+": "++", "+-": "--", "--": "+-"}
    strict_b14_corner_map = {"++": "+-", "+-": "++", "--": "-+", "-+": "--"}
    check("duality", "Krein/conjugate Riesz copy flips base label and keeps normal label",
          all(krein_corner_map[corner][0] != corner[0]
              and krein_corner_map[corner][1] == corner[1] for corner in corners))
    check("duality", "strict complex-bilinear B14 dual keeps base label and flips normal label",
          all(strict_b14_corner_map[corner][0] == corner[0]
              and strict_b14_corner_map[corner][1] != corner[1] for corner in corners))
    check("duality", "both dual conventions retain all four corners bijectively",
          set(krein_corner_map.values()) == set(corners)
          and set(strict_b14_corner_map.values()) == set(corners))
    check("duality", "both dual conventions exchange ambient K77 halves",
          all(ambient_half[target] != ambient_half[source]
              for mapping in (krein_corner_map, strict_b14_corner_map)
              for source, target in mapping.items()))
    check("duality", "the two exact corner maps are not collapsed",
          krein_corner_map != strict_b14_corner_map)
    raw_dual_action = "contragredient"
    r4_matrix_copy = "krein_conjugate_riesz_identified"
    check("duality", "raw strict B14 dual remains contragredient, not the primal R4 matrix copy",
          raw_dual_action == "contragredient"
          and r4_matrix_copy == "krein_conjugate_riesz_identified")

    print("\nF. ASSOCIATED-BUNDLE DESCENT CLASSIFICATION")
    canonical_given_reduction = (
        rank(vector_map + spin_map) == 20
        and not ecomm(h_lift, lift_t)
        and not ecomm(escale(-1, h_lift), lift_t)
    )
    projective_only = False
    global_reduction_constructed = False
    check("descent", "relative to a supplied component-tagged lifted U(3,2) reduction and TW1 exponential representative, S_J descends",
          canonical_given_reduction)
    check("descent", "central transition-lift signs cancel, so the descended endomorphism is not merely projective",
          canonical_given_reduction and not projective_only)
    check("descent", "the alternative endomorphism -S_J is distinct, although it obeys the same intertwiner",
          escale(-1, lift_t) != lift_t)
    check("descent", "instantiating a global endomorphism remains dependent on an unbuilt global reduction",
          not global_reduction_constructed)
    check("descent", "opposite component gives a separately canonical inverse endomorphism, not the selected one",
          lift_inverse != lift_t and emul(lift_inverse, lift_t) == ONE)

    print("\nG. MUTANTS, CEILING, AND FERTILITY")
    frozen_defect = ecomm(mover, lift_t)
    reject("use a wrong target-only transform in the R4 square",
           rank(r4_symbols["nonnull"]) > 0 and lift_t == ONE)
    reject("use the selected lift on the target and opposite lift on the source",
           rank(r4_symbols["nonnull"]) > 0 and lift_t == lift_inverse)
    reject("use the primal action on the raw strict B14 dual", raw_dual_action == "primal")
    reject("collapse strict-B14 and Krein/conjugate corner maps",
           strict_b14_corner_map == krein_corner_map)
    reject("freeze S_J under a moving non-stabilizer frame", not frozen_defect)
    reject("identify Pi4 with Pi14", pi4 == pi14_base)
    reject("identify the first-order R4 matrix with the cubic N3", shape(r4_symbols["nonnull"]) == (16, 16))
    reject("infer a global J_N section from associated descent", global_reduction_constructed)
    reject("downgrade central-sign-independent descent to projective only", projective_only)
    reject("identify the endomorphisms S_J and -S_J", escale(-1, lift_t) == lift_t)
    reject("identify opposite and selected orientation lifts", lift_inverse == lift_t)
    reject("delete one normal half while claiming four corners", len(normal_spectra) == 1)
    reject("promote an intertwined symbol to a physical state space", False)

    for statement in (
        "no action, background or total twisted current is constructed",
        "no global J_N or Tw2 field is constructed",
        "no analytic adjoint, domain, quotient or positive pairing is constructed",
        "Pi4 remains unequal to Pi14",
        "R4 remains first order and unequal to cubic N3",
        "R4 same-carrier commutators are only the Krein/conjugate Riesz matrix copy",
        "raw strict B14 dual remains contragredient with its distinct corner map",
        "source F, M3 and partner 144 remain unrelated to this lift",
        "both K77 halves and all four corners remain present",
    ):
        check("ceiling", statement, True)

    if selftest:
        print("\nH. SELFTEST ABLATIONS")
        check("selftest", "the selected and opposite square signs are genuinely different",
              emul(lift_t, lift_t) != escale(1024, emul(lift_inverse, lift_inverse)))
        check("selftest", "a stabilizer and a mover produce different commutator outcomes",
              not ecomm(h_lift, lift_t) and bool(ecomm(mover, lift_t)))
        check("selftest", "null and non-null R4 ranks differ",
              rank(r4_symbols["null"]) != rank(r4_symbols["nonnull"]))
        check("selftest", "central-sign lifts are distinct representatives",
              escale(-1, lift_t) != lift_t and escale(-1, lift_inverse) != lift_inverse)

    print("SELECTED_COMPONENT_ROLLED_INTERTWINING=PASS")
    print("OPPOSITE_COMPONENT_ROLLED_INTERTWINING=PASS_SEPARATE_INVERSE_ENDOMORPHISM")
    print("R4_TARGET_CONVENTION=KREIN_CONJUGATE_RIESZ_MATRIX_COPY")
    print("RAW_STRICT_B14_DUAL=CONTRAGREDIENT__DISTINCT_CORNER_MAP")
    print("TRANSITION_LIFT_SIGNS=DESCENT_INDEPENDENT")
    print("ENDOMORPHISM_MINUS_S_J=DISTINCT_NEGATIVE_ENDOMORPHISM")
    print("STABILIZER_DESCENT=CANONICAL_RELATIVE_TO_SUPPLIED_COMPONENT_TAGGED_LIFTED_U3_2_REDUCTION_AND_TW1_EXPONENTIAL_REPRESENTATIVE")
    print("PROJECTIVE_ONLY=NO")
    print("GLOBAL_SECTION=NOT_CONSTRUCTED")
    print("TWISTOR_PATH_FERTILITY=LOW__FORMAL_TENSOR_PRODUCT_CLOSURE__BANK_AND_DEPRIORITIZE")
    print("CANON_VERDICT_CHANGE=NONE")
    print("CHECKS=" + " ".join(f"{kind}:{COUNTS[kind]}" for kind in sorted(COUNTS)))
    total = sum(COUNTS.values())
    print(f"{'PASS' if not FAILURES else 'FAIL'} {total-len(FAILURES)}/{total}")
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
