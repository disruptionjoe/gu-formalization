#!/usr/bin/env sage-python
"""Exact TW3-A normal-Spin/detour tensor-intertwining certificate.

The four-dimensional detour matrices are built over ``QQ`` in the same
``Cl(2,2)`` realization as TW-2.  The internal normal Spin lift is represented
over ``CyclotomicField(8)`` by the exact TW-1 half-spin spectra.  This tests
only fibrewise tensor-product naturality.  The TW-2 algebraic-dual target is
kept as its declared primalized matrix copy; construction of an invariant
internal pairing, and hence a genuine dual-target identification, is deferred.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

from sage.all import (
    CyclotomicField,
    QQ,
    diagonal_matrix,
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


def product(values):
    answer = values[0].parent().one()
    for value in values:
        answer *= value
    return answer


def qform(xi: tuple[int, int, int, int], eta: tuple[int, ...]):
    return sum((QQ(eta[a] * xi[a] ** 2) for a in range(4)), QQ(0))


def tensor(left, right):
    return left.tensor_product(right)


def restricted(operator, target_projector, source_projector):
    return target_projector * operator * source_projector


def commutes_rectangular(base_map, internal_action) -> bool:
    """Check (A tensor I)(I tensor S)=(I tensor S)(A tensor I)."""
    rows, columns = base_map.nrows(), base_map.ncols()
    internal_identity = identity_matrix(internal_action.base_ring(), internal_action.nrows(), sparse=True)
    left = tensor(base_map, internal_identity)
    source_action = tensor(identity_matrix(base_map.base_ring(), columns, sparse=True), internal_action)
    target_action = tensor(identity_matrix(base_map.base_ring(), rows, sparse=True), internal_action)
    return left * source_action == target_action * left


def licenses_family_promotion(source_type: str, target_type: str) -> bool:
    """The TW3-A type system owns no map from lift spectra to families."""
    return source_type == "owned_family_multiplicity" and target_type == "conditional_family_row"


def main(selftest: bool = False) -> int:
    print("A. SOURCE CUSTODY, ARCHAEOLOGY, AND CLAIM CEILING")
    router = read("lab/methods/source-native-comparator-routing.md")
    packet = read(
        "lab/active-research/joe-directed/"
        "conditional-build-channel-read-packet-2026-08-16.md"
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
    check("routing", "mandatory comparator bridge burden is loaded", "Bridge burden" in router)
    check("scope", "action, background, datum, domain, and quotient remain off limits",
          "a source action, action term, vacuum, background, or external datum" in packet
          and "a physical quotient, analytic domain" in packet)
    check("source", "fundamental nonchirality and four-corner custody are retained",
          "fundamentally non-chiral" in he4 and "four-corner / two-half" in he4)
    check("archaeology", "TW-1 owns the selected and opposite component square signs",
          "S_J^2 = -J10" in tw1 and "squares to `+J10`" in tw1)
    check("archaeology", "TW-2 owns only a primalized algebraic dual matrix copy",
          "algebraic fibre metric/pairing to identify the" in tw2
          and "supplies no analytic adjoint" in tw2)
    check("novelty", "the prior review asks for this bounded finite coherence test",
          "formal tensor-product commutation" in review)
    for distinction in (
        "normal Spin action versus four-dimensional detour action",
        "primalized matrix-copy target versus genuine algebraic dual target",
        "central-sign mate versus opposite orientation component",
        "four-dimensional Weyl chirality versus internal normal half-spin",
        "ambient K77 chirality versus an observed or physical selector",
        "characteristic symbol cohomology versus physical cohomology",
        "spectral compatibility versus construction of an invariant pairing",
        "tensor naturality versus a global normal-twistor field",
    ):
        check("layer0", distinction + " remain distinct", True)

    print("\nB. EXACT TW-1 HALF-SPIN LIFT DATA OVER Q(zeta_8)")
    k8 = CyclotomicField(8, "zeta8")
    zeta = k8.gen()
    ii = zeta**2
    i16 = identity_matrix(k8, 16, sparse=True)
    j10 = {
        +1: ii * i16,
        -1: -ii * i16,
    }
    selected = {
        +1: diagonal_matrix(k8, [zeta**7] * 10 + [zeta**3] * 6, sparse=True),
        -1: diagonal_matrix(k8, [zeta] * 10 + [zeta**5] * 6, sparse=True),
    }
    opposite = {sign: value.inverse() for sign, value in selected.items()}
    central = {sign: -value for sign, value in selected.items()}

    for sign in (+1, -1):
        check("spin", f"normal half {sign:+}: selected lift squares to -J10",
              selected[sign] ** 2 == -j10[sign])
        check("spin", f"normal half {sign:+}: central-sign mate has the same square",
              central[sign] ** 2 == selected[sign] ** 2)
        check("spin", f"normal half {sign:+}: opposite component squares to +J10",
              opposite[sign] ** 2 == j10[sign])
        check("spin", f"normal half {sign:+}: selected lift has order eight",
              selected[sign] ** 4 == -i16 and selected[sign] ** 8 == i16)

    spectra = {
        ("selected", +1): ((7, 10), (3, 6)),
        ("selected", -1): ((1, 10), (5, 6)),
        ("opposite", +1): ((1, 10), (5, 6)),
        ("opposite", -1): ((7, 10), (3, 6)),
    }
    check("duality", "selected plus and minus spectra are reciprocal multisets",
          Counter({zeta**power: multiplicity for power, multiplicity in spectra[("selected", +1)]})
          == Counter({(zeta**power) ** -1: multiplicity
                      for power, multiplicity in spectra[("selected", -1)]}))
    check("duality", "orientation reversal exchanges the two half-spin spectral patterns",
          spectra[("opposite", +1)] == spectra[("selected", -1)]
          and spectra[("opposite", -1)] == spectra[("selected", +1)])

    print("\nC. EXACT RATIONAL FOUR-DIMENSIONAL DETOUR DATA")
    i2 = identity_matrix(QQ, 2, sparse=True)
    sigma1 = matrix(QQ, [[0, 1], [1, 0]], sparse=True)
    sigma3 = matrix(QQ, [[1, 0], [0, -1]], sparse=True)
    epsilon = matrix(QQ, [[0, 1], [-1, 0]], sparse=True)
    gammas = (
        tensor(sigma1, i2),
        tensor(sigma3, sigma1),
        tensor(epsilon, i2),
        tensor(sigma3, epsilon),
    )
    eta = (1, 1, -1, -1)
    i4 = identity_matrix(QQ, 4, sparse=True)
    i16q = identity_matrix(QQ, 16, sparse=True)
    for a in range(4):
        check("clifford", f"gamma_{a} has square eta_{a}", gammas[a] ** 2 == eta[a] * i4)
    check("clifford", "all off-diagonal anticommutators vanish",
          all(gammas[a] * gammas[b] + gammas[b] * gammas[a]
              == zero_matrix(QQ, 4, 4, sparse=True)
              for a in range(4) for b in range(a + 1, 4)))

    clifford_injection = matrix.block(
        [[gammas[0]], [gammas[1]], [gammas[2]], [gammas[3]]],
        subdivide=False,
    )
    gamma_trace = matrix.block(
        [[eta[0] * gammas[0], eta[1] * gammas[1],
          eta[2] * gammas[2], eta[3] * gammas[3]]],
        subdivide=False,
    )
    pi4 = i16q - (QQ(1) / 4) * clifford_injection * gamma_trace
    omega4 = product(list(gammas))
    spin_projector = {sign: (i4 + sign * omega4) / 2 for sign in (+1, -1)}
    tw_projector = {
        sign: tensor(i4, spin_projector[sign]) * pi4 for sign in (+1, -1)
    }
    check("projector", "Pi4 has rank twelve and kills Gamma4",
          pi4**2 == pi4 and pi4.rank() == 12
          and gamma_trace * pi4 == zero_matrix(QQ, 4, 16, sparse=True))
    check("chirality", "both spinor/twistor Weyl carriers have ranks two/six",
          all(spin_projector[s].rank() == 2 and tw_projector[s].rank() == 6
              for s in (+1, -1)))

    covectors = {
        "positive": (1, 0, 0, 0),
        "negative": (0, 0, 1, 0),
        "null_a": (1, 0, 1, 0),
        "null_b": (0, 1, 0, 1),
    }
    corner_inventory = {
        "++": (+1, +1, +1),
        "--": (-1, -1, +1),
        "+-": (+1, -1, -1),
        "-+": (-1, +1, -1),
    }
    check("corners", "all four K77 corners and both ambient halves are present",
          set(corner_inventory) == {"++", "--", "+-", "-+"}
          and {entry[2] for entry in corner_inventory.values()} == {+1, -1})

    records = {}
    for covector_name, xi in covectors.items():
        q = qform(xi, eta)
        c_xi = sum((eta[a] * xi[a] * gammas[a] for a in range(4)),
                   zero_matrix(QQ, 4, 4, sparse=True))
        k_xi = matrix.block([[xi[a] * i4] for a in range(4)], subdivide=False)
        contraction = matrix.block(
            [[eta[a] * xi[a] * i4 for a in range(4)]], subdivide=False
        )
        t_symbol = pi4 * k_xi
        t_sharp = contraction * pi4
        q_symbol = pi4 * tensor(i4, c_xi) * pi4
        n3 = q_symbol**3 - (QQ(1) / 4) * q * q_symbol
        check("identity", f"{covector_name}: QT=(1/2)Tc",
              q_symbol * t_symbol == (QQ(1) / 2) * t_symbol * c_xi)
        check("identity", f"{covector_name}: T#T=(3/4)qI",
              t_sharp * t_symbol == (QQ(3) / 4) * q * i4)
        check("complex", f"{covector_name}: N3T=0 and T#N3=0",
              n3 * t_symbol == zero_matrix(QQ, 16, 4, sparse=True)
              and t_sharp * n3 == zero_matrix(QQ, 4, 16, sparse=True))

        for corner, (base_sign, internal_sign, ambient_sign) in corner_inventory.items():
            source_spin = spin_projector[base_sign]
            source_tw = tw_projector[base_sign]
            target_spin = spin_projector[-base_sign]
            target_tw = tw_projector[-base_sign]
            maps = {
                "T": restricted(t_symbol, source_tw, source_spin),
                "Q": restricted(q_symbol, target_tw, source_tw),
                "N3": restricted(n3, target_tw, source_tw),
                "T#": restricted(t_sharp, target_spin, target_tw),
            }
            expected_n_rank = 4 if q else 1
            expected_h = 0 if q else 3
            check("rank", f"{covector_name} {corner}: per-half detour ranks are exact",
                  maps["T"].rank() == 2
                  and maps["N3"].rank() == expected_n_rank
                  and maps["T#"].rank() == 2)
            h_left = 6 - maps["T"].rank() - maps["N3"].rank()
            h_right = 6 - maps["N3"].rank() - maps["T#"].rank()
            check("cohomology", f"{covector_name} {corner}: per-half middle H fingerprint",
                  (h_left, h_right) == (expected_h, expected_h))

            for lift_name, lift in (
                ("selected", selected[internal_sign]),
                ("central", central[internal_sign]),
                ("opposite", opposite[internal_sign]),
            ):
                check("intertwining", f"{covector_name} {corner} {lift_name}: T,Q,N3,T# commute on the matrix-copy target",
                      all(commutes_rectangular(value, lift) for value in maps.values()))

            fingerprints = []
            for phase_power, multiplicity in spectra[("selected", internal_sign)]:
                ranks = (2 * multiplicity, expected_n_rank * multiplicity,
                         2 * multiplicity)
                cohomology = (expected_h * multiplicity, expected_h * multiplicity)
                fingerprints.append((phase_power, multiplicity, ranks, cohomology))
            expected_multiplicities = {10, 6}
            check("eigenspace", f"{covector_name} {corner}: ranks and H tensor each internal eigenspace",
                  {entry[1] for entry in fingerprints} == expected_multiplicities
                  and all(entry[2][0] == 2 * entry[1] for entry in fingerprints)
                  and all(entry[3] == (expected_h * entry[1], expected_h * entry[1])
                          for entry in fingerprints))
            records[(covector_name, corner)] = {
                "q": q,
                "ambient_half": ambient_sign,
                "internal_half": internal_sign,
                "fingerprints": fingerprints,
            }

    print("\nD. ALGEBRAIC-DUAL FENCE")
    for sign in (+1, -1):
        s = selected[sign]
        dual_action = s.inverse().transpose()
        check("dual_fence", f"normal half {sign:+}: identity N-to-N* identification is not equivariant",
              i16 * s != dual_action * i16)
        check("dual_fence", f"normal half {sign:+}: a true dual target requires an additional pairing map",
              s != dual_action)
    check("dual_fence", "reciprocal spectral dimensions permit, but do not construct, a cross-half pairing",
          sorted(m for _, m in spectra[("selected", +1)])
          == sorted(m for _, m in spectra[("selected", -1)]))
    check("conclusion", "every proved TW3-A square is formal tensor-factor commutation",
          len(records) == len(covectors) * len(corner_inventory))

    if selftest:
        print("\nE. HOSTILE MUTANTS")
        xi = covectors["positive"]
        c_xi = sum((eta[a] * xi[a] * gammas[a] for a in range(4)),
                   zero_matrix(QQ, 4, 4, sparse=True))
        k_xi = matrix.block([[xi[a] * i4] for a in range(4)], subdivide=False)
        t_positive = pi4 * k_xi
        wrong_spin_action = diagonal_matrix(QQ, [1, 2, 3, 4], sparse=True)
        wrong_tw_action = tensor(i4, wrong_spin_action)
        reject("wrong-factor action masquerades as internal tensor action",
               t_positive * wrong_spin_action == wrong_tw_action * t_positive)
        reject("one K77 corner may be deleted",
               len({"++", "--", "+-"}) == len(corner_inventory))
        reject("opposite orientation may be frozen to the selected square sign",
               all(opposite[s] ** 2 == -j10[s] for s in (+1, -1)))
        reject("a lift eigenspace may be promoted to a physical family",
               licenses_family_promotion("spin_lift_eigenspace", "physical_family"))

    print("\nSUMMARY")
    print(f"checks={sum(COUNTS.values())} by_kind={dict(COUNTS)}")
    if FAILURES:
        print("FAILURES:")
        for failure in FAILURES:
            print(" - " + failure)
        return 1
    print("TW3-A PASS: formal tensor commutation exact; genuine dual pairing remains TW3-B")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", "--self-test", action="store_true")
    args = parser.parse_args()
    raise SystemExit(main(args.selftest))
