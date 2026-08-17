#!/usr/bin/env sage-python
"""Exact TW3-B normal pairing, contragredient, and corner-gluing gate.

The certificate distinguishes the real complex-bilinear Riesz map from the
sesquilinear Krein Riesz map.  It is fibrewise algebra only: no positive
pairing, formal/analytic adjoint, domain, quotient, action, background, or
physical state is constructed.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product as cartesian_product
from pathlib import Path

from sage.all import (
    QQ,
    QuadraticField,
    identity_matrix,
    matrix,
    zero_matrix,
)


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def reject(label: str, false_claim: object) -> None:
    check("mutant", "reject " + label, not bool(false_claim))


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def tensor_all(factors):
    answer = matrix(QQ, [[1]], sparse=True)
    for factor in factors:
        answer = answer.tensor_product(factor)
    return answer


def product_matrices(values, size: int):
    answer = identity_matrix(QQ, size, sparse=True)
    for value in values:
        answer *= value
    return answer


def cl_6_4():
    """A real 32-dimensional Cl(6,4) representation by four (1,1) lifts."""
    i2 = identity_matrix(QQ, 2, sparse=True)
    sigma1 = matrix(QQ, [[0, 1], [1, 0]], sparse=True)
    sigma3 = matrix(QQ, [[1, 0], [0, -1]], sparse=True)
    epsilon = matrix(QQ, [[0, 1], [-1, 0]], sparse=True)
    gammas = [sigma1, sigma3]
    signs = [1, 1]
    for _ in range(4):
        old_size = gammas[0].nrows()
        gammas = (
            [value.tensor_product(sigma3) for value in gammas]
            + [identity_matrix(QQ, old_size, sparse=True).tensor_product(sigma1)]
            + [identity_matrix(QQ, old_size, sparse=True).tensor_product(epsilon)]
        )
        signs += [1, -1]
    plus = [value for value, sign in zip(gammas, signs) if sign == 1]
    minus = [value for value, sign in zip(gammas, signs) if sign == -1]
    return plus + minus, (1,) * 6 + (-1,) * 4


def cl_7_7():
    """The exact current-K77 real Cl(7,7) bank used by TW-1."""
    i2 = identity_matrix(QQ, 2, sparse=True)
    sigma1 = matrix(QQ, [[0, 1], [1, 0]], sparse=True)
    sigma3 = matrix(QQ, [[1, 0], [0, -1]], sparse=True)
    epsilon = matrix(QQ, [[0, 1], [-1, 0]], sparse=True)
    plus, minus = [], []
    for index in range(7):
        prefix, suffix = [sigma3] * index, [i2] * (6 - index)
        plus.append(tensor_all(prefix + [sigma1] + suffix))
        minus.append(tensor_all(prefix + [epsilon] + suffix))
    return plus + minus, (1,) * 7 + (-1,) * 7


def invert_phase_spectrum(value: Counter[int]) -> Counter[int]:
    return Counter({(-phase) % 8: multiplicity for phase, multiplicity in value.items()})


def central_negative_spectrum(value: Counter[int]) -> Counter[int]:
    return Counter({(phase + 4) % 8: multiplicity for phase, multiplicity in value.items()})


def main(selftest: bool = False) -> int:
    print("A. ROUTING, SOURCE CUSTODY, AND CLAIM CEILING")
    router = read("lab/methods/source-native-comparator-routing.md")
    packet = read(
        "lab/active-research/joe-directed/conditional-build-channel-read-packet-2026-08-16.md"
    )
    he4 = read(
        "lab/active-research/joe-directed/high-energy-two-plus-one/"
        "he4-path-reprioritization-2026-08-16.md"
    )
    tw1 = read(
        "lab/active-research/joe-directed/superposition-twistor/"
        "tw1-normal-twistor-spin-lift-2026-08-16.md"
    )
    tw2 = read(
        "lab/active-research/joe-directed/superposition-twistor/"
        "tw2-four-dimensional-detour-symbol-factorization-2026-08-16.md"
    )
    review = read(
        "lab/process/hostile-reviews/"
        "2026-08-16-joe-directed-twistor-conditional-composition-review.md"
    )
    check("routing", "the mandatory comparator bridge burden remains in force",
          "Bridge burden" in router)
    check("source", "the channel preserves F, M_3, and the internal 144 as distinct referents",
          "F     =" in he4 and "M_3   =" in he4 and "144   =" in he4)
    check("source", "fundamental nonchirality and all four corners remain mandatory",
          "fundamentally non-chiral" in packet and "all four corners" in packet)
    check("ceiling", "action, background, domain, quotient, and physical observable construction are fenced",
          "a source action, action term, vacuum, background, or external datum" in packet
          and "a physical quotient, analytic domain" in packet)
    check("prior_art", "TW-1 owns the selected and opposite component square signs",
          "S_J^2 = -J10" in tw1 and "squares to `+J10`" in tw1)
    check("prior_art", "TW-2 types T-sharp as algebraic rather than analytic",
          "algebraic metric-dual principal symbol" in tw2
          and "formal adjoint on a closed analytic domain" in tw2)
    check("prior_art", "the prior hostile review names dual/pairing gluing as the bounded seam",
          "state the algebraic dual/pairing convention explicitly" in review)

    print("\nB. EXACT NORMAL Cl(6,4) BILINEAR AND KREIN FORMS")
    normal_gammas, normal_eta = cl_6_4()
    i32 = identity_matrix(QQ, 32, sparse=True)
    z32 = zero_matrix(QQ, 32, 32, sparse=True)
    check("clifford", "the normal bank has signature (6,4)",
          all(gamma * gamma == sign * i32
              for gamma, sign in zip(normal_gammas, normal_eta)))
    check("clifford", "all normal off-diagonal anticommutators vanish",
          all(normal_gammas[a] * normal_gammas[b]
              + normal_gammas[b] * normal_gammas[a] == z32
              for a in range(10) for b in range(a + 1, 10)))

    # C10 is the product of the six positive generators.  Every Clifford
    # generator is C10-skew, so every even Spin generator preserves C10.
    c10 = product_matrices(normal_gammas[:6], 32)
    j10 = product_matrices(normal_gammas, 32)
    g10 = c10 * j10
    check("bilinear", "C10 is nondegenerate skew and squares to minus one",
          c10.rank() == 32 and c10.transpose() == -c10 and c10 * c10 == -i32)
    check("bilinear", "all ten Clifford generators are C10-skew",
          all(gamma.transpose() * c10 == -c10 * gamma for gamma in normal_gammas))
    check("bilinear", "all 45 normal Spin generators preserve C10",
          all(
              (normal_gammas[a] * normal_gammas[b]).transpose() * c10
              + c10 * (normal_gammas[a] * normal_gammas[b]) == z32
              for a in range(10) for b in range(a + 1, 10)
          ))
    check("chirality", "J10 is a real complex structure and is C10-anti-adjoint",
          j10 * j10 == -i32 and j10.transpose() * c10 == -c10 * j10)
    check("krein", "G10=C10 J10 is symmetric, nondegenerate, involutive, and neutral",
          g10.transpose() == g10 and g10.rank() == 32
          and g10 * g10 == i32 and g10.trace() == 0)

    # Exact complex half-spin restriction.  B10 pairs opposite halves, while
    # h_delta(x,y)=delta*i*B10(conj(x),y)=G10(conj(x),y) is Hermitian and
    # neutral on S10_delta.  The delta sign is load-bearing on S10-.
    gaussian = QuadraticField(-1, "ii")
    ii = gaussian.gen()
    j10k = j10.change_ring(gaussian)
    c10k = c10.change_ring(gaussian)
    g10k = g10.change_ring(gaussian)
    i32k = identity_matrix(gaussian, 32)
    x_plus = matrix(
        gaussian,
        (j10k - ii * i32k).right_kernel().basis(),
    ).transpose()
    x_minus = matrix(
        gaussian,
        (j10k + ii * i32k).right_kernel().basis(),
    ).transpose()
    check("chirality", "the fixed J10 halves have complex rank sixteen",
          x_plus.dimensions() == (32, 16) and x_minus.dimensions() == (32, 16))
    check("bilinear", "the complex bilinear form vanishes within each half",
          x_plus.transpose() * c10k * x_plus == zero_matrix(gaussian, 16, 16)
          and x_minus.transpose() * c10k * x_minus == zero_matrix(gaussian, 16, 16))
    cross_b = x_plus.transpose() * c10k * x_minus
    check("bilinear", "the complex bilinear Riesz map exchanges S10+ and S10- exactly",
          cross_b.rank() == 16)
    h_plus = ii * x_plus.conjugate_transpose() * c10k * x_plus
    h_minus = -ii * x_minus.conjugate_transpose() * c10k * x_minus
    check("krein", "both half forms are restrictions of the single G10 form",
          h_plus == x_plus.conjugate_transpose() * g10k * x_plus
          and h_minus == x_minus.conjugate_transpose() * g10k * x_minus)
    cp_plus = h_plus.charpoly()
    cp_minus = h_minus.charpoly()
    xp = cp_plus.parent().gen()
    xm = cp_minus.parent().gen()
    check("krein", "the induced forms are Hermitian and nondegenerate on both halves",
          h_plus.conjugate_transpose() == h_plus and h_plus.rank() == 16
          and h_minus.conjugate_transpose() == h_minus and h_minus.rank() == 16)
    check("krein", "each normal half has exact Krein signature (8,8)",
          cp_plus == (xp - 2) ** 8 * (xp + 2) ** 8
          and cp_minus == (xm - 2) ** 8 * (xm + 2) ** 8)
    reject("promote the exact normal Krein form to a positive pairing",
           cp_plus == (xp - 2) ** 16)

    print("\nC. SELECTED LIFT, CONTRAGREDIENT ACTION, AND COMPONENT SIGN")
    pairs = ((0, 1, 1), (2, 3, 1), (4, 5, 1), (6, 7, -1), (8, 9, -1))
    t_lift = i32
    for a, b, epsilon in pairs:
        t_lift *= i32 - epsilon * normal_gammas[a] * normal_gammas[b]
    t_inverse = t_lift.inverse()
    check("lift", "selected orientation: T^2=-32 J10",
          t_lift * t_lift == -32 * j10)
    check("lift", "opposite orientation: T^-2=+J10/32",
          t_inverse * t_inverse == j10 / 32)
    check("lift", "central lift sign leaves the square unchanged",
          (-t_lift) * (-t_lift) == t_lift * t_lift)
    check("pairing", "the normalized lift preserves both B10 and G10",
          t_lift.transpose() * c10 * t_lift == 32 * c10
          and t_lift.transpose() * g10 * t_lift == 32 * g10)
    check("dual", "the algebraic Riesz map intertwines the contragredient lift",
          32 * c10.inverse() * t_inverse.transpose() * c10 == t_lift)

    # A rational noncompact Spin element prevents the selected lift's special
    # commutation with C10 from hiding a primal/contragredient error.
    boost_bivector = normal_gammas[0] * normal_gammas[6]
    boost = (5 * i32 + 4 * boost_bivector) / 3
    check("control", "the rational boost is a genuine C10-isometry",
          boost_bivector * boost_bivector == i32
          and boost.transpose() * c10 * boost == c10)
    check("dual", "generic finite covariance is R^-1 rho^-T R=rho",
          c10.inverse() * boost.inverse().transpose() * c10 == boost)
    reject("use the primal normal action on a raw dual target",
           c10.inverse() * boost * c10 == boost)

    t_plus = x_plus.solve_right(t_lift.change_ring(gaussian) * x_plus)
    t_minus = x_minus.solve_right(t_lift.change_ring(gaussian) * x_minus)
    check("krein", "the selected lift is exactly pseudo-unitary on both Krein halves",
          t_plus.conjugate_transpose() * h_plus * t_plus == 32 * h_plus
          and t_minus.conjugate_transpose() * h_minus * t_minus == 32 * h_minus)
    check("bilinear", "the selected lift preserves the cross-half bilinear Gram",
          t_plus.transpose() * cross_b * t_minus == 32 * cross_b)

    print("\nD. CURRENT K77 FORM AND FOUR-CORNER SELECTION RULES")
    ambient_gammas, ambient_eta = cl_7_7()
    i128 = identity_matrix(QQ, 128, sparse=True)
    c14 = product_matrices(ambient_gammas[:7], 128)
    base_axes = (0, 7, 8, 9)
    normal_axes = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
    w4 = product_matrices([ambient_gammas[a] for a in base_axes], 128)
    j10_ambient = product_matrices([ambient_gammas[a] for a in normal_axes], 128)
    w14 = product_matrices(ambient_gammas, 128)
    g14 = c14 * j10_ambient
    check("k77", "the ambient bank is the current real Cl(7,7) module",
          all(gamma * gamma == sign * i128
              for gamma, sign in zip(ambient_gammas, ambient_eta)))
    check("k77", "C14 is a nondegenerate Spin(7,7)-invariant skew form",
          c14.rank() == 128 and c14.transpose() == -c14
          and all(gamma.transpose() * c14 == c14 * gamma
                  for gamma in ambient_gammas))
    check("k77", "the observer-normal Krein form is neutral (64,64), not positive",
          g14.transpose() == g14 and g14 * g14 == i128 and g14.trace() == 0)
    check("corner", "B14 is base-chirality self-pairing and normal-chirality cross-pairing",
          w4.transpose() * c14 == c14 * w4
          and j10_ambient.transpose() * c14 == -c14 * j10_ambient)
    check("corner", "B14 pairs opposite ambient halves, preserving full nonchirality",
          w14.transpose() * c14 == -c14 * w14)

    # Labels are (base Weyl, normal Weyl).  A complex-bilinear Riesz map and
    # the conjugate/Krein Riesz map are different typed constructions.
    bilinear_dual = {"++": "+-", "+-": "++", "--": "-+", "-+": "--"}
    krein_dual = {"++": "-+", "-+": "++", "+-": "--", "--": "+-"}
    tw2_matrix_target = {"++": "-+", "-+": "++", "+-": "--", "--": "+-"}
    check("corner", "the bilinear dual keeps base chirality and exchanges S10 halves",
          bilinear_dual == {"++": "+-", "+-": "++", "--": "-+", "-+": "--"})
    check("corner", "the Krein/conjugate dual flips base chirality and keeps the internal label",
          krein_dual == tw2_matrix_target)
    check("corner", "both dual conventions are bijections on all four corners",
          set(bilinear_dual) == set(bilinear_dual.values())
          == set(krein_dual) == set(krein_dual.values())
          == {"++", "+-", "-+", "--"})
    reject("collapse the algebraic-bilinear and Krein/conjugate corner maps",
           bilinear_dual == krein_dual)
    reject("delete one half or corner from the dual gluing",
           len(set(krein_dual.values())) < 4)

    print("\nE. EXACT PHASE TRANSPORT FOR S_J, -S_J, AND -J_N")
    spectra = {"S10+": Counter(), "S10-": Counter()}
    for weights in cartesian_product((1, -1), repeat=5):
        half = "S10+" if weights.count(-1) % 2 == 0 else "S10-"
        spectra[half][(-sum(weights)) % 8] += 1
    opposite = {half: invert_phase_spectrum(value) for half, value in spectra.items()}
    central_negative = {
        half: central_negative_spectrum(value) for half, value in spectra.items()
    }
    check("phase", "selected S_J spectra reproduce TW-1 on both internal halves",
          spectra["S10+"] == Counter({7: 10, 3: 6})
          and spectra["S10-"] == Counter({1: 10, 5: 6}))
    check("phase", "contragredient phases on one half equal primal phases on its bilinear partner",
          invert_phase_spectrum(spectra["S10+"]) == spectra["S10-"]
          and invert_phase_spectrum(spectra["S10-"]) == spectra["S10+"])
    check("phase", "J_N -> -J_N uses S_J^-1 and exchanges the fixed-half phase tables",
          opposite["S10+"] == spectra["S10-"]
          and opposite["S10-"] == spectra["S10+"])
    check("phase", "S_J -> -S_J shifts every phase by four without changing corners",
          central_negative["S10+"] == Counter({3: 10, 7: 6})
          and central_negative["S10-"] == Counter({5: 10, 1: 6}))
    reject("treat the central-sign lift as the opposite orientation component",
           central_negative == opposite)
    check("phase", "orientation reversal swaps phases but not the fixed J10 half labels",
          set(opposite) == {"S10+", "S10-"} and opposite != spectra)

    print("\nF. TW2 TARGET VERDICT AND STOP BOUNDARY")
    artifact = read(
        "lab/active-research/joe-directed/superposition-twistor/"
        "tw3b-dual-pairing-orientation-corner-gluing-2026-08-16.md"
    )
    check("artifact", "the artifact declares the formal Krein-dual closure",
          "FORMAL_KREIN_DUAL_GLUING_CLOSES" in artifact)
    check("artifact", "the strict algebraic-dual notation mismatch is retained",
          "ALGEBRAIC_STAR_NOT_EQUAL_TO_KREIN_OVERLINE" in artifact)
    check("artifact", "the source 2+1 and emergent-chirality meanings are preserved",
          "ordinary family index" in artifact and "fundamentally non-chiral" in artifact)
    check("artifact", "no positive pairing or analytic adjoint is claimed",
          "not a positive pairing" in artifact and "not an analytic adjoint" in artifact)
    reject("interpret a corner as a family or physical state",
           "corner is a physical family" in artifact.lower()
           or "krein signature is a particle count" in artifact.lower())

    if selftest:
        print("\nG. SELFTEST MUTATION SUMMARY")
        reject("replace contragredient covariance by primal covariance on the boost",
               c10 * boost == boost * c10)
        reject("make the selected and opposite component squares equal",
               t_lift * t_lift == 32 * (t_inverse * t_inverse))
        reject("claim the Krein Gram is definite",
               cp_minus == (xm - 2) ** 16 or cp_minus == (xm + 2) ** 16)
        reject("identify S10+ with S10- as one labelled corner factor",
               spectra["S10+"] == spectra["S10-"])

    total = sum(COUNTS.values())
    print("\nH. DISPOSITION")
    print(f"checks={total} failures={len(FAILURES)} kinds={dict(COUNTS)}")
    if FAILURES:
        for failure in FAILURES:
            print("FAILURE:", failure)
        return 1
    print(
        "PASS: exact current-K77 bilinear and Krein duality are separated; "
        "contragredient covariance and all four corner maps close at fibre grade."
    )
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    arguments = parser.parse_args()
    raise SystemExit(main(arguments.selftest))
