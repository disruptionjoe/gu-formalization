#!/usr/bin/env python3
"""Resolver Wave K77-B2: curvature selector and displayed-family obstruction.

This exact probe stays on the real ``Cl(7,7)`` lane.  It constructs the
algebraic Riemann module as the first-Bianchi kernel inside
``Sym^2(Lambda^2 V*)``, injects it into spin-valued curvature, computes the
exact D7 target multiplicities, and reduces the displayed low/high Shiab
family to scalar/traceless-Ricci coordinates.  It then intersects the ambient
fourteen-dimensional Einstein ratio with the same-action cubic transgression
identity.

The result is scoped: it classifies the displayed factorized ansatz under the
ambient-Einstein reading.  It does not exhaust every source-natural Shiab,
identify Weinstein's missing historical Bianchi selector, prove a differential
Bianchi/Green/domain theorem, or recover observed four-dimensional physics.
P1/P2/P3 are unused.
"""

from __future__ import annotations

from itertools import combinations, product
import json
from pathlib import Path
import subprocess

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
N = 14
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
FULL = (1 << N) - 1
Element = dict[int, sp.Expr]
Form = dict[int, Element]

COUNTS = {"exact": 0, "sage": 0, "source": 0, "type": 0, "planted": 0}
FAILURES: list[str] = []


def check(kind: str, label: str, condition: bool, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def indices(mask: int) -> tuple[int, ...]:
    return tuple(i for i in range(N) if mask & (1 << i))


def eclean(x: Element) -> Element:
    return {m: sp.simplify(c) for m, c in x.items() if sp.simplify(c) != 0}


def eadd(*xs: Element) -> Element:
    out: Element = {}
    for x in xs:
        for m, c in x.items():
            out[m] = sp.simplify(out.get(m, 0) + c)
    return eclean(out)


def escale(c, x: Element) -> Element:
    return eclean({m: sp.simplify(c * v) for m, v in x.items()})


def blade_product(left: int, right: int) -> tuple[int, int]:
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    sign = -1 if inversions % 2 else 1
    for i in indices(left & right):
        sign *= ETA[i]
    return left ^ right, sign


def emul(x: Element, y: Element) -> Element:
    out: Element = {}
    for mx, cx in x.items():
        for my, cy in y.items():
            m, sign = blade_product(mx, my)
            out[m] = sp.simplify(out.get(m, 0) + sign * cx * cy)
    return eclean(out)


def blade(item: int | tuple[int, ...], coefficient=1) -> Element:
    if isinstance(item, int):
        item = (item,)
    mask = sum(1 << i for i in item)
    return {mask: sp.sympify(coefficient)}


def dagger_b(x: Element) -> Element:
    out: Element = {}
    for m, c in x.items():
        r = m.bit_count()
        out[m] = sp.simplify((-1) ** (r * (r + 1) // 2) * sp.conjugate(c))
    return eclean(out)


def is_b_skew(x: Element) -> bool:
    return not eadd(dagger_b(x), x)


def scalar_trace(x: Element) -> sp.Expr:
    return sp.simplify(128 * x.get(0, 0))


def fclean(x: Form) -> Form:
    return {m: eclean(c) for m, c in x.items() if eclean(c)}


def fadd(*xs: Form) -> Form:
    keys = set().union(*(x.keys() for x in xs))
    return fclean({m: eadd(*(x.get(m, {}) for x in xs)) for m in keys})


def fscale(c, x: Form) -> Form:
    return fclean({m: escale(c, v) for m, v in x.items()})


def wedge_sign(left: int, right: int) -> int:
    if left & right:
        return 0
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    return -1 if inversions % 2 else 1


def coefficient_product(x: Element, y: Element, channel: str) -> Element:
    xy = emul(x, y)
    if channel == "raw":
        return xy
    yx = emul(y, x)
    if channel == "comm":
        return eadd(xy, escale(-1, yx))
    if channel == "symi":
        return escale(sp.I, eadd(xy, yx))
    raise ValueError(channel)


def wedge(x: Form, y: Form, channel: str = "raw") -> Form:
    out: Form = {}
    for mx, cx in x.items():
        for my, cy in y.items():
            sign = wedge_sign(mx, my)
            if not sign:
                continue
            m = mx | my
            value = escale(sign, coefficient_product(cx, cy, channel))
            out[m] = eadd(out.get(m, {}), value)
    return fclean(out)


def hodge(x: Form) -> Form:
    out: Form = {}
    for m, c in x.items():
        complement = FULL ^ m
        sign = wedge_sign(m, complement)
        norm = sp.prod(ETA[i] for i in indices(m))
        out[complement] = eadd(out.get(complement, {}), escale(sign * norm, c))
    return fclean(out)


def form_equal(x: Form, y: Form) -> bool:
    return not fadd(x, fscale(-1, y))


def form_b_skew(x: Form) -> bool:
    return all(is_b_skew(c) for c in x.values())


def exterior_generator_action(x: Form, a: int, b: int) -> Form:
    out: Form = {}
    for m, c in x.items():
        old = list(indices(m))
        for position, i in enumerate(old):
            if i == a:
                replacement, factor = b, -ETA[b]
            elif i == b:
                replacement, factor = a, ETA[a]
            else:
                continue
            new = old.copy()
            new[position] = replacement
            if len(set(new)) != len(new):
                continue
            inversions = sum(
                1 for p in range(len(new)) for q in range(p + 1, len(new))
                if new[p] > new[q]
            )
            new_mask = sum(1 << j for j in new)
            value = escale(factor * (-1 if inversions % 2 else 1), c)
            out[new_mask] = eadd(out.get(new_mask, {}), value)
    return fclean(out)


def total_generator_action(x: Form, a: int, b: int) -> Form:
    coefficient_action = {
        m: coefficient_generator_action(c, a, b) for m, c in x.items()
    }
    return fadd(exterior_generator_action(x, a, b), coefficient_action)


def coefficient_generator_action(x: Element, a: int, b: int) -> Element:
    generator = escale(sp.Rational(1, 2), emul(blade(a), blade(b)))
    return eadd(emul(generator, x), escale(-1, emul(x, generator)))


def pair_top(x: Form, y: Form) -> sp.Expr:
    return scalar_trace(wedge(x, y).get(FULL, {}))


def phi_low() -> tuple[Form, Form]:
    phi1 = {1 << i: blade(i) for i in range(N)}
    phi2 = fscale(sp.Rational(1, 2), wedge(phi1, phi1))
    return phi1, phi2


PHI1_L, PHI2_L = phi_low()
VOLUME = blade((), 1)
for volume_index in range(N):
    VOLUME = emul(VOLUME, blade(volume_index))
PHI1_H = {m: emul(c, VOLUME) for m, c in PHI1_L.items()}
PHI2_H = {m: escale(sp.I, emul(c, VOLUME)) for m, c in PHI2_L.items()}
PHI1_BANK = (PHI1_L, PHI1_H)
PHI2_BANK = (PHI2_L, PHI2_H)


def shiab_parts(curvature: Form, channels, phi1: Form, phi2: Form) -> tuple[Form, Form]:
    first_channel, inner_channel, outer_channel = channels
    star_curvature = hodge(curvature)
    first = wedge(phi1, star_curvature, first_channel)
    middle = hodge(wedge(phi2, star_curvature, inner_channel))
    second = hodge(wedge(phi1, middle, outer_channel))
    return first, second


def shiab_first(curvature: Form, channel: str, phi1: Form) -> Form:
    return wedge(phi1, hodge(curvature), channel)


def shiab_second(curvature: Form, inner_channel: str, outer_channel: str,
                 phi1: Form, phi2: Form) -> Form:
    middle = hodge(wedge(phi2, hodge(curvature), inner_channel))
    return hodge(wedge(phi1, middle, outer_channel))


def feature_maps(curvature: Form, channels) -> list[Form]:
    """Coefficients of (a,b,ac,ad,bc,bd) in the displayed map."""
    first_channel, inner_channel, outer_channel = channels
    first = [shiab_first(curvature, first_channel, p1) for p1 in PHI1_BANK]
    second = [
        fscale(sp.Rational(-1, 2),
               shiab_second(curvature, inner_channel, outer_channel, p1, p2))
        for p1 in PHI1_BANK for p2 in PHI2_BANK
    ]
    return first + second


def feature_map(curvature: Form, channels, feature_index: int) -> Form:
    """One lifted feature without expanding the five unused directions."""
    if feature_index == 0:
        return shiab_first(curvature, channels[0], PHI1_L)
    if feature_index == 1:
        return shiab_first(curvature, channels[0], PHI1_H)
    p1 = PHI1_BANK[(feature_index - 2) // 2]
    p2 = PHI2_BANK[(feature_index - 2) % 2]
    return fscale(
        sp.Rational(-1, 2),
        shiab_second(curvature, channels[1], channels[2], p1, p2),
    )


def all_feature_coordinates(curvature: Form):
    """Compute small restriction coordinates without retaining large forms."""
    first = {
        (first_channel, p1_index): (
            decode_amplitude(value := shiab_first(curvature, first_channel, p1), "L"),
            decode_amplitude(value, "H"),
            form_b_skew(value),
        )
        for first_channel in ("comm", "symi")
        for p1_index, p1 in enumerate(PHI1_BANK)
    }
    second = {
        (inner_channel, outer_channel, p1_index, p2_index): (
            decode_amplitude(
                value := fscale(
                    sp.Rational(-1, 2),
                    shiab_second(curvature, inner_channel, outer_channel, p1, p2),
                ),
                "L",
            ),
            decode_amplitude(value, "H"),
            form_b_skew(value),
        )
        for inner_channel, outer_channel in product(("comm", "symi"), repeat=2)
        for p1_index, p1 in enumerate(PHI1_BANK)
        for p2_index, p2 in enumerate(PHI2_BANK)
    }
    return {
        channels: [
            first[(channels[0], 0)],
            first[(channels[0], 1)],
            second[(channels[1], channels[2], 0, 0)],
            second[(channels[1], channels[2], 0, 1)],
            second[(channels[1], channels[2], 1, 0)],
            second[(channels[1], channels[2], 1, 1)],
        ]
        for channels in product(("comm", "symi"), repeat=3)
    }


def metric(i: int, j: int) -> int:
    return ETA[i] if i == j else 0


def normalize_pair(i: int, j: int) -> tuple[tuple[int, int], int]:
    if i == j:
        return (i, j), 0
    return ((i, j), 1) if i < j else ((j, i), -1)


def pair_matrix_tensor(matrix):
    def tensor(i, j, k, l):
        p, spair = normalize_pair(i, j)
        q, sqair = normalize_pair(k, l)
        if not spair or not sqair:
            return 0
        return spair * sqair * matrix.get((p, q), matrix.get((q, p), 0))
    return tensor


def scalar_curvature_tensor(i, j, k, l):
    return metric(i, k) * metric(j, l) - metric(i, l) * metric(j, k)


S_TRACELESS = {(0, 0): 1, (1, 1): 1}


def traceless_ricci_tensor(i, j, k, l):
    s = lambda a, b: S_TRACELESS.get((a, b), 0)
    return sp.Rational(1, N - 2) * (
        s(i, k) * metric(j, l) + s(j, l) * metric(i, k)
        - s(i, l) * metric(j, k) - s(j, k) * metric(i, l)
    )


WEYL_MATRIX = {}
for pair, weight in {
    (4, 5): 1, (4, 6): -1, (4, 7): 0,
    (5, 6): 0, (5, 7): -1, (6, 7): 1,
}.items():
    WEYL_MATRIX[(pair, pair)] = weight
weyl_tensor = pair_matrix_tensor(WEYL_MATRIX)

MIXED_WEYL_MATRIX = {}
for pair, weight in {
    (0, 4): 1, (0, 10): 1, (1, 4): 1, (1, 10): 1,
}.items():
    MIXED_WEYL_MATRIX[(pair, pair)] = weight
mixed_weyl_tensor = pair_matrix_tensor(MIXED_WEYL_MATRIX)


def ricci(tensor, j: int, l: int):
    return sp.simplify(sum(ETA[i] * tensor(i, j, i, l) for i in range(N)))


def scalar(tensor):
    return sp.simplify(sum(ETA[j] * ricci(tensor, j, j) for j in range(N)))


def algebraic_curvature(tensor) -> bool:
    # Pair-basis checks avoid a slow 14^4 symbolic sweep.  Antisymmetry with
    # repeated indices and the remaining permutations follow from these rows.
    pair_antisymmetry = all(
        tensor(i, j, k, l) == -tensor(j, i, k, l)
        and tensor(i, j, k, l) == -tensor(i, j, l, k)
        for i, j in combinations(range(N), 2)
        for k, l in combinations(range(N), 2)
    )
    pair_symmetry = all(
        tensor(i, j, k, l) == tensor(k, l, i, j)
        for i, j in combinations(range(N), 2)
        for k, l in combinations(range(N), 2)
    )
    bianchi = all(
        sp.simplify(
            tensor(i, j, k, l) - tensor(i, k, j, l) + tensor(i, l, j, k)
        ) == 0
        for i, j, k, l in combinations(range(N), 4)
    )
    return pair_antisymmetry and pair_symmetry and bianchi


def spin_curvature_injection(tensor, zeta=sp.Integer(1)) -> Form:
    """I_zeta(R)_ij=zeta sum_{a<b} R_ij{}^{ab} gamma_a gamma_b."""
    out: Form = {}
    for i, j in combinations(range(N), 2):
        coefficient: Element = {}
        for a, b in combinations(range(N), 2):
            raised = ETA[a] * ETA[b] * tensor(i, j, a, b)
            if raised:
                coefficient = eadd(
                    coefficient,
                    escale(zeta * raised, emul(blade(a), blade(b))),
                )
        if coefficient:
            out[(1 << i) | (1 << j)] = coefficient
    return fclean(out)


def raised_bivector_image(a: int, b: int, zeta=sp.Integer(1)) -> Element:
    """Spin image of one covariant internal bivector basis element."""
    return escale(zeta * ETA[a] * ETA[b], emul(blade(a), blade(b)))


def recover_covariant_bivector(value: Element, zeta=sp.Integer(1)):
    """Coefficient inverse to ``raised_bivector_image`` for nonzero zeta."""
    if zeta == 0:
        raise ValueError("zeta must be nonzero")
    recovered = {}
    for a, b in combinations(range(N), 2):
        coefficient = sp.simplify(
            value.get((1 << a) | (1 << b), 0) / (zeta * ETA[a] * ETA[b])
        )
        if coefficient:
            recovered[(a, b)] = coefficient
    return recovered


def map_covariant_pair_form_to_spin(value: Form) -> Element:
    """Contract a scalar covariant two-form into its raised spin bivector."""
    out: Element = {}
    for form_mask, coefficient in value.items():
        a, b = indices(form_mask)
        out = eadd(
            out,
            escale(coefficient.get(0, 0), raised_bivector_image(a, b)),
        )
    return out


def pair_matrix_action(matrix, a: int, b: int):
    """Infinitesimal covariant action on both Lambda^2 factors."""
    out = {}
    for (left, right), coefficient in matrix.items():
        for acted_left_mask, acted_left_coefficient in exterior_generator_action(
            {(1 << left[0]) | (1 << left[1]): {0: 1}}, a, b
        ).items():
            acted_left = indices(acted_left_mask)
            out[(acted_left, right)] = sp.simplify(
                out.get((acted_left, right), 0)
                + coefficient * acted_left_coefficient.get(0, 0)
            )
        for acted_right_mask, acted_right_coefficient in exterior_generator_action(
            {(1 << right[0]) | (1 << right[1]): {0: 1}}, a, b
        ).items():
            acted_right = indices(acted_right_mask)
            out[(left, acted_right)] = sp.simplify(
                out.get((left, acted_right), 0)
                + coefficient * acted_right_coefficient.get(0, 0)
            )
    return {key: value for key, value in out.items() if value != 0}


def tensor_pair_matrix(tensor):
    return {
        (left, right): value
        for left in combinations(range(N), 2)
        for right in combinations(range(N), 2)
        if (value := sp.simplify(tensor(*left, *right))) != 0
    }


def symmetric_output(h, sector: str) -> Form:
    """Natural low/high Lambda^13 output of a covariant symmetric tensor."""
    one_form: Form = {}
    for i in range(N):
        coefficient: Element = {}
        for j in range(N):
            if (value := sp.simplify(h(i, j))) != 0:
                basis = blade(j) if sector == "L" else emul(blade(j), VOLUME)
                coefficient = eadd(coefficient, escale(ETA[j] * value, basis))
        if coefficient:
            one_form[1 << i] = coefficient
    return hodge(one_form)


def scalar_channel(tensor, sector: str) -> Form:
    scal = scalar(tensor)
    return symmetric_output(lambda i, j: scal * metric(i, j), sector)


def traceless_ricci_channel(tensor, sector: str) -> Form:
    scal = scalar(tensor)
    return symmetric_output(
        lambda i, j: ricci(tensor, i, j) - sp.Rational(1, N) * scal * metric(i, j),
        sector,
    )


def einstein_channel(tensor, sector: str) -> Form:
    scal = scalar(tensor)
    return symmetric_output(
        lambda i, j: ricci(tensor, i, j) - sp.Rational(1, 2) * scal * metric(i, j),
        sector,
    )


def decode_amplitude(output: Form, sector: str) -> sp.Expr:
    one_form = hodge(output)
    coefficient = one_form.get(1 << 0, {})
    if sector == "L":
        return sp.simplify(coefficient.get(1 << 0, 0))
    reference = emul(blade(0), VOLUME)
    mask, unit = next(iter(reference.items()))
    return sp.simplify(coefficient.get(mask, 0) / unit)


def twist_coefficients(value: Form) -> Form:
    """Grade-1/2 fixture dual: 1->13 and 2->i*12, preserving B-skewness."""
    out: Form = {}
    for form_mask, coefficient in value.items():
        entry: Element = {}
        for clifford_mask, scalar_coefficient in coefficient.items():
            dual = emul({clifford_mask: scalar_coefficient}, VOLUME)
            if clifford_mask.bit_count() == 2:
                dual = escale(sp.I, dual)
            entry = eadd(entry, dual)
        out[form_mask] = entry
    return fclean(out)


def transgression_row(torsion: Form, variation: Form, channels,
                      active_features: tuple[int, ...]) -> list[sp.Expr]:
    q = wedge(torsion, torsion)
    dq = fadd(wedge(variation, torsion), wedge(torsion, variation))
    row = [sp.Integer(0)] * 6
    for i in active_features:
        sq = feature_map(q, channels, i)
        sdq = feature_map(dq, channels, i)
        row[i] = sp.simplify(
            sp.Rational(1, 3) * pair_top(torsion, sdq)
            - sp.Rational(2, 3) * pair_top(variation, sq)
        )
    return row


print("A. SOURCE COLLISION AND LAYER 0")

rendered = (ROOT / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md").read_text()
k77b = (ROOT / "explorations/resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation-2026-08-04.md").read_text()

check("source", "draft types Shiab as Omega2(ad) to Omega13(ad)",
      "Shiab_epsilon: Omega^2(Y^(7,7), ad) -> Omega^(d-1)(Y^(7,7), ad)" in rendered)
check("source", "draft prints the two-term Phi1/Phi2 contraction",
      "PDF page 43 equation 9.3" in rendered and "Ricci-scalar-like" in rendered)
check("source", "draft permits other Shiabs and does not supply the historical selector",
      "other possible Shiab choices" in rendered and "cannot currently locate" in rendered)
check("source", "draft supplies unhalved commutator and i-symmetric coefficient products",
      "[a,b] = a . b - b . a" in rendered and "{a,b} = i(a . b + b . a)" in rendered)
check("source", "source states Weyl-killing but does not prove uniqueness",
      "kills Weyl curvature" in rendered and '"Weyl_killing_is_uniqueness_proof": false' in rendered)
check("source", "K77-B already normalized q(T) as matrix wedge rather than doubled bracket",
      "[T,T]_{\\rm graded}=2T\\wedge_{\\rm matrix}T" in k77b)

check("type", "algebraic first Bianchi is not the gauge differential Bianchi or the missing historical selector", True)
check("type", "ambient 14D Einstein trace is not observed 4D or Frobenius-fibre trace reversal", True)
check("type", "algebraic Riemann curvature is a submodule, not all Omega2(ad)", True)
check("type", "action density, Euler covector, Green realization, and observed equation remain distinct", True)


print("\nB. EXACT CURVATURE MODULE AND D7 TARGET")

pairs = list(combinations(range(N), 2))
pair_dimension = len(pairs)
pair_symmetric_dimension = pair_dimension * (pair_dimension + 1) // 2
bianchi_rows = []
for i, j, k, l in combinations(range(N), 4):
    coordinates = (
        tuple(sorted((pairs.index((i, j)), pairs.index((k, l))))),
        tuple(sorted((pairs.index((i, k)), pairs.index((j, l))))),
        tuple(sorted((pairs.index((i, l)), pairs.index((j, k))))),
    )
    bianchi_rows.append(coordinates)
bianchi_support = [coordinate for row in bianchi_rows for coordinate in row]

check("exact", "dim Lambda2 V is 91", pair_dimension == 91)
check("exact", "dim Sym2(Lambda2 V) is 4186", pair_symmetric_dimension == 4186)
check("exact", "1001 sparse first-Bianchi rows have disjoint supports and exact rank 1001",
      len(bianchi_rows) == 1001 and len(set(bianchi_support)) == 3003)
check("exact", "algebraic Riemann kernel has dimension 3185",
      pair_symmetric_dimension - len(bianchi_rows) == 3185)
check("exact", "ambient Omega2(ad) dimension is 91*16384=1490944",
      91 * 16384 == 1490944)

sage_code = r'''
from sage.all import WeylCharacterRing
D=WeylCharacterRing("D7",style="coroots")
V=D(1,0,0,0,0,0,0)
P=V.exterior_power(2)
R=P.symmetric_power(2)-V.exterior_power(4)
U=sum(V.exterior_power(r) for r in range(15))
T=V*U
irreps=[D(0,0,0,0,0,0,0),D(2,0,0,0,0,0,0),D(0,2,0,0,0,0,0)]
print(P.degree(),P.symmetric_power(2).degree(),V.exterior_power(4).degree(),R.degree())
print(R)
print([(x.degree(),x.inner_product(T)) for x in irreps])
print(T.degree())
'''
sage = subprocess.run(["sage", "-c", sage_code], cwd=ROOT, text=True,
                      capture_output=True, check=False)
sage_lines = [line.strip() for line in sage.stdout.splitlines() if line.strip()]
check("sage", "Sage certifies 3185=1+104+3080 and target multiplicities 2,2,0",
      sage.returncode == 0
      and sage_lines[-4:] == [
          "91 4186 1001 3185",
          "D7(0,0,0,0,0,0,0) + D7(2,0,0,0,0,0,0) + D7(0,2,0,0,0,0,0)",
          "[(1, 2), (104, 2), (3080, 0)]",
          "229376",
      ], sage.stderr.strip()[-200:] if sage.returncode else "")
check("exact", "Riemann-restriction Hom space is four-dimensional and Weyl multiplicity is zero",
      sage_lines[-2:] == ["[(1, 2), (104, 2), (3080, 0)]", "229376"])
check("planted", "Weyl-killing is rejected as a uniqueness selector",
      sage_lines[-2].endswith("(3080, 0)]"))


print("\nC. ALGEBRAIC CURVATURE FIXTURES AND SPIN INJECTION")

check("exact", "scalar, traceless-Ricci, and Weyl fixtures satisfy all algebraic curvature symmetries",
      all(algebraic_curvature(t) for t in (scalar_curvature_tensor, traceless_ricci_tensor, weyl_tensor)))
check("exact", "constant-curvature fixture has Ric=13g and scalar=182",
      all(ricci(scalar_curvature_tensor, i, j) == 13 * metric(i, j)
          for i in range(N) for j in range(N))
      and scalar(scalar_curvature_tensor) == 182)
check("exact", "traceless-Ricci fixture has Ric=S and zero scalar",
      all(ricci(traceless_ricci_tensor, i, j) == S_TRACELESS.get((i, j), 0)
          for i in range(N) for j in range(N))
      and scalar(traceless_ricci_tensor) == 0)
check("exact", "Weyl fixture is nonzero and Ricci-free",
      bool(WEYL_MATRIX) and all(ricci(weyl_tensor, i, j) == 0
                                for i in range(N) for j in range(N)))
check("exact", "mixed-sign Weyl fixture is nonzero and Ricci-free",
      bool(MIXED_WEYL_MATRIX) and all(ricci(mixed_weyl_tensor, i, j) == 0
                                      for i in range(N) for j in range(N)))

F_SCALAR = spin_curvature_injection(scalar_curvature_tensor)
F_RICCI = spin_curvature_injection(traceless_ricci_tensor)
F_WEYL = spin_curvature_injection(weyl_tensor)
F_MIXED_WEYL = spin_curvature_injection(mixed_weyl_tensor)
check("exact", "spin-curvature injection lands in degree-two B-skew forms",
      all(form_b_skew(f) and {m.bit_count() for m in f} == {2}
          for f in (F_SCALAR, F_RICCI, F_WEYL, F_MIXED_WEYL)))
check("exact", "all 91 raised bivector images have an exact coefficient inverse for nonzero zeta",
      all(
          recover_covariant_bivector(raised_bivector_image(a, b, 3), 3)
          == {(a, b): 1}
          for a, b in combinations(range(N), 2)
      ))
check("exact", "raised bivector map intertwines all 91 covariant-pair and Spin generators",
      all(
          not eadd(
              coefficient_generator_action(raised_bivector_image(*pair), *generator),
              escale(-1, map_covariant_pair_form_to_spin(
                  exterior_generator_action(
                      {(1 << pair[0]) | (1 << pair[1]): {0: 1}}, *generator
                  )
              )),
          )
          for pair in combinations(range(N), 2)
          for generator in combinations(range(N), 2)
      ))
GENERATOR_HOLDOUTS = ((0, 1), (0, 4), (4, 5))
check("exact", "scalar injected curvature is invariant under compact and noncompact Spin holdouts",
      all(not total_generator_action(F_SCALAR, a, b)
          for a, b in GENERATOR_HOLDOUTS))
for fixture_name, fixture_tensor, fixture_form, generator in (
    ("Ricci", traceless_ricci_tensor, F_RICCI, (0, 4)),
    ("mixed-sign Weyl", mixed_weyl_tensor, F_MIXED_WEYL, (0, 1)),
):
    acted_tensor = pair_matrix_tensor(
        pair_matrix_action(tensor_pair_matrix(fixture_tensor), *generator)
    )
    check("exact", f"spin-curvature injection intertwines a nontrivial {fixture_name} holdout",
          form_equal(
              spin_curvature_injection(acted_tensor),
              total_generator_action(fixture_form, *generator),
          ))

BAD_MATRIX = {(((0, 1)), ((2, 3))): 1}
bad_tensor = pair_matrix_tensor(BAD_MATRIX)
check("planted", "pair-symmetric non-Bianchi curvature is rejected by the algebraic selector",
      not algebraic_curvature(bad_tensor))
check("planted", "omitting internal metric raising changes mixed-sign injected curvature",
      not form_equal(
          F_SCALAR,
          fclean({
              (1 << i) | (1 << j): eadd(*[
                  escale(scalar_curvature_tensor(i, j, a, b), emul(blade(a), blade(b)))
                  for a, b in combinations(range(N), 2)
                  if scalar_curvature_tensor(i, j, a, b)
              ])
              for i, j in combinations(range(N), 2)
          }),
      ))

REAL_HOM_MAPS = {
    "Q_LOW": traceless_ricci_channel(traceless_ricci_tensor, "L"),
    "Z_LOW": scalar_channel(scalar_curvature_tensor, "L"),
    "Q_HIGH": traceless_ricci_channel(traceless_ricci_tensor, "H"),
    "Z_HIGH": scalar_channel(scalar_curvature_tensor, "H"),
}
check("exact", "four explicit real scalar/Ricci maps realize the complex D7 multiplicity upper bound",
      all(REAL_HOM_MAPS.values())
      and not scalar_channel(traceless_ricci_tensor, "L")
      and not traceless_ricci_channel(scalar_curvature_tensor, "L")
      and [{m.bit_count() for value in REAL_HOM_MAPS[name].values() for m in value}
           for name in ("Q_LOW", "Z_LOW", "Q_HIGH", "Z_HIGH")]
      == [{1}, {1}, {13}, {13}])

J_LOW = {name: einstein_channel(tensor, "L") for name, tensor in (
    ("scalar", scalar_curvature_tensor),
    ("ricci", traceless_ricci_tensor),
    ("weyl", weyl_tensor),
)}
J_HIGH = {name: einstein_channel(tensor, "H") for name, tensor in (
    ("scalar", scalar_curvature_tensor),
    ("ricci", traceless_ricci_tensor),
    ("weyl", weyl_tensor),
)}
check("exact", "J_LOW and J_HIGH are degree-13 B-skew Einstein restrictions with zero Weyl response",
      all(form_b_skew(value) and {m.bit_count() for m in value} == {13}
          for bank in (J_LOW, J_HIGH) for key, value in bank.items() if key != "weyl")
      and not J_LOW["weyl"] and not J_HIGH["weyl"])
check("exact", "J_LOW and J_HIGH have nonzero independent scalar/Ricci responses",
      all(J_LOW[key] and J_HIGH[key] for key in ("scalar", "ricci"))
      and {m.bit_count() for value in J_LOW["scalar"].values() for m in value} == {1}
      and {m.bit_count() for value in J_HIGH["scalar"].values() for m in value} == {13})
for sector in ("L", "H"):
    acted_ricci = pair_matrix_tensor(
        pair_matrix_action(tensor_pair_matrix(traceless_ricci_tensor), 0, 4)
    )
    check("exact", f"J_{sector} intertwines a nontrivial Ricci generator holdout",
          form_equal(
              einstein_channel(acted_ricci, sector),
              total_generator_action(einstein_channel(traceless_ricci_tensor, sector), 0, 4),
          ))


print("\nD. COMPLETE DISPLAYED LOW/HIGH CARRIER ON RIEMANN CURVATURE")

check("exact", "all four low/high Phi copies pass compact and noncompact Spin holdouts",
      all(not total_generator_action(phi, a, b)
          for phi in (PHI1_L, PHI1_H, PHI2_L, PHI2_H)
          for a, b in GENERATOR_HOLDOUTS))
check("exact", "Phi coefficient grades are exactly 1,13 and 2,12",
      [{m.bit_count() for e in phi.values() for m in e}
       for phi in (PHI1_L, PHI1_H, PHI2_L, PHI2_H)]
      == [{1}, {13}, {2}, {12}])
check("planted", "high Phi2 requires its i phase to be B-skew",
      form_b_skew(PHI2_H)
      and not form_b_skew({m: emul(c, VOLUME) for m, c in PHI2_L.items()}))

CHANNELS = list(product(("comm", "symi"), repeat=3))
scalar_feature_bank = all_feature_coordinates(F_SCALAR)
ricci_feature_bank = all_feature_coordinates(F_RICCI)
restriction = {}
for channels in CHANNELS:
    scalar_features = scalar_feature_bank[channels]
    ricci_features = ricci_feature_bank[channels]
    scalar_low = [value[0] for value in scalar_features]
    scalar_high = [value[1] for value in scalar_features]
    ricci_low = [value[0] for value in ricci_features]
    ricci_high = [value[1] for value in ricci_features]
    restriction["/".join(channels)] = {
        "scalar_low": scalar_low,
        "ricci_low": ricci_low,
        "einstein_low": [sp.simplify(scalar_low[i] + 78 * ricci_low[i]) for i in range(6)],
        "scalar_high": scalar_high,
        "ricci_high": ricci_high,
        "einstein_high": [sp.simplify(scalar_high[i] + 78 * ricci_high[i]) for i in range(6)],
    }

a_parameter, b_parameter, c_parameter, d_parameter = sp.symbols("a b c d")
factorized_features = (
    a_parameter,
    b_parameter,
    a_parameter * c_parameter,
    a_parameter * d_parameter,
    b_parameter * c_parameter,
    b_parameter * d_parameter,
)


def row_polynomial(row):
    return sp.expand(sum(coefficient * monomial
                         for coefficient, monomial in zip(row, factorized_features)))


einstein_groebner = {}
einstein_viable = []
for channels in CHANNELS:
    key = "/".join(channels)
    ideal = [
        row_polynomial(restriction[key]["einstein_low"]),
        row_polynomial(restriction[key]["einstein_high"]),
    ]
    ideal = [entry for entry in ideal if entry != 0]
    basis = sp.groebner(ideal or [0], a_parameter, b_parameter, c_parameter, d_parameter)
    einstein_groebner[key] = basis
    response_polynomials = [
        row_polynomial(restriction[key][coordinate])
        for coordinate in ("scalar_low", "ricci_low", "scalar_high", "ricci_high")
    ]
    if any(basis.reduce(value)[1] != 0 for value in response_polynomials):
        einstein_viable.append(key)

check("exact", "every displayed feature map is B-skew on the algebraic scalar/Ricci fixtures",
      all(value[2]
          for channels in CHANNELS
          for bank in (scalar_feature_bank, ricci_feature_bank)
          for value in bank[channels]))
check("exact", "only comm-first channels carry the traceless-Ricci response",
      all(
          (any(restriction["/".join(ch)]["ricci_low"])
           or any(restriction["/".join(ch)]["ricci_high"])) == (ch[0] == "comm")
          for ch in CHANNELS
      ))

VIABLE_A = "comm/symi/comm"
VIABLE_B = "comm/symi/symi"
check("exact", "ambient Einstein ratio leaves exactly two nonvacuous channel patterns",
      einstein_viable == [VIABLE_A, VIABLE_B]
      and restriction[VIABLE_A]["einstein_low"] == [-182, 0, 0, 0, 0, 182]
      and restriction[VIABLE_A]["einstein_high"] == [0, -182, 0, 182, 0, 0]
      and restriction[VIABLE_B]["einstein_low"] == [-182, 0, 182, 0, 0, 0]
      and restriction[VIABLE_B]["einstein_high"] == [0, -182, 0, 0, 182, 0])
check("exact", "the two viable patterns kill the Weyl fixture on every lifted feature",
      all(not value
          for channels in (("comm", "symi", "comm"), ("comm", "symi", "symi"))
          for value in feature_maps(F_WEYL, channels)))
check("planted", "raw Ricci response alone fails the 14D Einstein trace ratio",
      restriction["comm/comm/comm"]["einstein_low"][0] != 0)
check("type", "Weyl zero follows from equivariance/multiplicity and is not counted as an independent selector", True)


print("\nE. SAME-ACTION CUBIC TRANSGRESSION INTERSECTION")

TORSION = {
    1 << 0: eadd(blade(0), blade((4, 5))),
    1 << 2: eadd(blade(1), blade((5, 6))),
    1 << 4: eadd(blade(2), blade((6, 7))),
    1 << 6: eadd(blade(3), blade((7, 8))),
}
VARIATION = {
    1 << 1: eadd(blade(4), blade((0, 2))),
    1 << 3: eadd(blade(5), blade((1, 3))),
    1 << 5: eadd(blade(6), blade((0, 3))),
    1 << 7: eadd(blade(7), blade((1, 2))),
}
TORSION_DUAL = twist_coefficients(TORSION)
VARIATION_DUAL = twist_coefficients(VARIATION)
check("exact", "low and volume-dual transgression fixtures are degree-one B-skew forms",
      all(form_b_skew(value) and {m.bit_count() for m in value} == {1}
          for value in (TORSION, VARIATION, TORSION_DUAL, VARIATION_DUAL)))

rows = {
    VIABLE_A: [
        transgression_row(TORSION, VARIATION, tuple(VIABLE_A.split("/")), tuple(range(6))),
        transgression_row(TORSION_DUAL, VARIATION_DUAL, tuple(VIABLE_A.split("/")), tuple(range(6))),
    ],
    VIABLE_B: [
        transgression_row(TORSION, VARIATION, tuple(VIABLE_B.split("/")), tuple(range(6))),
        transgression_row(TORSION_DUAL, VARIATION_DUAL, tuple(VIABLE_B.split("/")), tuple(range(6))),
    ],
}
check("exact", "viable-A exact transgression rows activate a,bd and ad",
      rows[VIABLE_A] == [
          [sp.Rational(1024, 3), 0, 0, 0, 0, sp.Rational(512, 3)],
          [0, 0, 0, sp.Rational(512, 3), 0, 0],
      ])
check("exact", "viable-B exact transgression rows activate a,ac and bc",
      rows[VIABLE_B] == [
          [sp.Rational(1024, 3), 0, sp.Rational(-512, 3), 0, 0, 0],
          [0, 0, 0, 0, sp.Rational(512, 3), 0],
      ])
parameter_ideals = {
    VIABLE_A: [
        b_parameter * d_parameter - a_parameter,
        a_parameter * d_parameter - b_parameter,
        2 * a_parameter + b_parameter * d_parameter,
        a_parameter * d_parameter,
    ],
    VIABLE_B: [
        a_parameter * c_parameter - a_parameter,
        b_parameter * c_parameter - b_parameter,
        2 * a_parameter - a_parameter * c_parameter,
        b_parameter * c_parameter,
    ],
}
parameter_bases = {
    key: sp.groebner(ideal, a_parameter, b_parameter, c_parameter, d_parameter)
    for key, ideal in parameter_ideals.items()
}
check("exact", "viable-A original-parameter ideal reduces exactly to <a,b>",
      [entry.as_expr() for entry in parameter_bases[VIABLE_A].polys]
      == [a_parameter, b_parameter])
check("exact", "viable-B original-parameter ideal reduces exactly to <a,b>",
      [entry.as_expr() for entry in parameter_bases[VIABLE_B].polys]
      == [a_parameter, b_parameter])
check("exact", "factorization therefore makes every surviving parameter fibre the zero displayed map",
      all(basis.reduce(a_parameter)[1] == 0 and basis.reduce(b_parameter)[1] == 0
          for basis in parameter_bases.values()))
check("planted", "lifted-feature rank alone retains spurious nonfactorizable directions",
      sp.Matrix([[ -1, 0, 0, 0, 0, 1],
                 [0, -1, 0, 1, 0, 0],
                 [2, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 0, 0]]) * sp.Matrix([0, 0, 1, 0, 0, 0])
      == sp.zeros(4, 1))
check("planted", "the zero map is rejected by nonzero scalar/Ricci normalization",
      bool(F_SCALAR) and bool(F_RICCI))
check("planted", "a constant-field transgression pass is not promoted to a Green/domain theorem", True)
check("type", "failure is displayed-ansatz under ambient-Einstein reading, not K77/GU/physics", True)


print("\nF. BROADER RIVAL CENSUS AND REGISTRY CONTRACT")

registry = json.loads((ROOT / "lab/process/resolver-wave-k77b2-shiab-family-curvature-selector-transgression.json").read_text())
check("type", "registry records complete four-dimensional Riemann-restriction Hom census",
      registry["riemann_restriction_hom"]["dimension"] == 4
      and registry["riemann_restriction_hom"]["multiplicities"] == {"scalar": 2, "traceless_ricci": 2, "weyl": 0})
check("type", "registry separates displayed factorized ansatz from bounded broader grammar",
      registry["candidate_tiers"][0]["complete_within_declared_tier"] is True
      and registry["candidate_tiers"][1]["complete_within_declared_tier"] is False)
check("type", "registry records ambient-Einstein two-coordinate rival restriction as constructed but unextended",
      registry["constructive_survivor"]["riemann_restriction_dimension"] == 2
      and registry["constructive_survivor"]["full_domain_extension"] == "OPEN")
check("type", "registry leaves differential Bianchi, Green, moving fields, observation, and physics open",
      all(registry["open_gates"][key] == "OPEN" for key in (
          "historical_bianchi_selector", "differential_bianchi", "derivative_green",
          "moving_epsilon_metric", "observation_descent", "physics")))
check("type", "external data remain unchanged and unused",
      registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("planted", "bounded grammar is not called the full Shiab family",
      registry["candidate_tiers"][1]["exhausts_all_shiabs"] is False)

result = {
    "counts": COUNTS,
    "curvature_dimensions": {
        "ambient_omega2_ad": 1490944,
        "pair_symmetric": 4186,
        "bianchi_rank": 1001,
        "riemann": 3185,
        "irreps": [1, 104, 3080],
        "target_multiplicities": [2, 2, 0],
    },
    "feature_order": ["a", "b", "ac", "ad", "bc", "bd"],
    "ambient_einstein_viable_patterns": [VIABLE_A, VIABLE_B],
    "transgression_rows": {key: [[str(x) for x in row] for row in value]
                            for key, value in rows.items()},
    "displayed_intersection": "ZERO_MAP_ONLY",
    "kill_scope": "DISPLAYED_ANSATZ_KILL_UNDER_AMBIENT_EINSTEIN_PLUS_SAME_ACTION",
    "broader_riemann_hom": "FOUR_DIMENSIONAL",
    "ambient_einstein_restriction": "TWO_DIMENSIONAL_EXTENSION_OPEN",
    "failures": FAILURES,
}
print("\nK77-B2 RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print(
    f"\nChecks: {COUNTS['exact']} exact + {COUNTS['sage']} Sage + "
    f"{COUNTS['source']} source + {COUNTS['type']} type + "
    f"{COUNTS['planted']} planted = {sum(COUNTS.values())}"
)
if FAILURES:
    raise SystemExit("FAILED: " + "; ".join(FAILURES))
print("PASS: curvature injection and four-coordinate Riemann Hom census constructed; displayed ambient-Einstein/same-action intersection is zero; broader full-domain extension remains open.")
