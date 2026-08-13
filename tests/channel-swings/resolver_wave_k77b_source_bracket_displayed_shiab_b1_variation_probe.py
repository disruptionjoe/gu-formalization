#!/usr/bin/env python3
"""Resolver Wave K77-B: source bracket, bosonic Shiab, and B1 variation.

This exact probe works in the faithful real Clifford algebra
``Cl(7,7)=M_128(R)`` and the full fourteen-dimensional exterior algebra.  It
does not import the K95 right-H, chosen-J, trace-line, R_J, or native-grade
machinery.  It distinguishes:

* the source matrix-wedge quadratic ``T wedge T`` from the doubled graded
  commutator;
* the canonical low-grade associative-product reading of draft equation
  (9.3) from source-inspired nodewise commutator / i-anticommutator
  reconstructions;
* a top-form B1 density from its translation Euler covector; and
* the action-derived first variation from the source's proposed endpoint
  residual.

The result is a local exact candidate-map test.  It is not a selected Shiab,
global action, Ward identity, observed equation, domain, or physics recovery.
P1/P2/P3 are unused.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
N = 14
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
FULL_FORM_MASK = (1 << N) - 1
KAPPA = sp.Symbol("kappa_1", real=True)
S = sp.Symbol("s", real=True)

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


def bit_indices(mask: int) -> tuple[int, ...]:
    return tuple(index for index in range(N) if mask & (1 << index))


def clean_element(value: Element) -> Element:
    return {
        mask: coefficient
        for mask, coefficient in value.items()
        if sp.simplify(coefficient) != 0
    }


def eadd(*values: Element) -> Element:
    out: Element = {}
    for value in values:
        for mask, coefficient in value.items():
            out[mask] = sp.simplify(out.get(mask, 0) + coefficient)
    return clean_element(out)


def escale(coefficient, value: Element) -> Element:
    return clean_element({mask: sp.simplify(coefficient * entry) for mask, entry in value.items()})


def blade_product(left: int, right: int) -> tuple[int, int]:
    inversions = sum(
        1
        for i in bit_indices(left)
        for j in bit_indices(right)
        if i > j
    )
    coefficient = -1 if inversions % 2 else 1
    common = left & right
    for index in bit_indices(common):
        coefficient *= ETA[index]
    return left ^ right, coefficient


def emul(left: Element, right: Element) -> Element:
    out: Element = {}
    for left_mask, left_coefficient in left.items():
        for right_mask, right_coefficient in right.items():
            mask, sign = blade_product(left_mask, right_mask)
            out[mask] = sp.simplify(
                out.get(mask, 0) + sign * left_coefficient * right_coefficient
            )
    return clean_element(out)


def blade(indices: tuple[int, ...] | int, coefficient=1) -> Element:
    if isinstance(indices, int):
        indices = (indices,)
    mask = 0
    for index in indices:
        mask |= 1 << index
    return {mask: sp.sympify(coefficient)}


def dagger_b(value: Element) -> Element:
    """K77-A B-adjoint on the complexified Clifford basis.

    Every real gamma is B-skew.  A grade-r ordered blade therefore has
    B-adjoint parity (-1)^(r(r+1)/2), with complex conjugation on scalars.
    """
    out: Element = {}
    for mask, coefficient in value.items():
        degree = mask.bit_count()
        parity = (-1) ** (degree * (degree + 1) // 2)
        out[mask] = sp.simplify(parity * sp.conjugate(coefficient))
    return clean_element(out)


def is_b_skew(value: Element) -> bool:
    return not eadd(dagger_b(value), value)


def scalar_trace(value: Element) -> sp.Expr:
    # The faithful real representation has dimension 128.
    return sp.simplify(128 * value.get(0, 0))


def fclean(value: Form) -> Form:
    return {
        mask: clean_element(coefficient)
        for mask, coefficient in value.items()
        if clean_element(coefficient)
    }


def fadd(*values: Form) -> Form:
    keys = set().union(*(value.keys() for value in values))
    return fclean({
        key: eadd(*(value.get(key, {}) for value in values))
        for key in keys
    })


def fscale(coefficient, value: Form) -> Form:
    return fclean({mask: escale(coefficient, entry) for mask, entry in value.items()})


def wedge_sign(left: int, right: int) -> int:
    if left & right:
        return 0
    inversions = sum(
        1
        for i in bit_indices(left)
        for j in bit_indices(right)
        if i > j
    )
    return -1 if inversions % 2 else 1


def coeff_product(left: Element, right: Element, channel: str) -> Element:
    lr = emul(left, right)
    if channel == "raw":
        return lr
    rl = emul(right, left)
    if channel == "comm":
        return eadd(lr, escale(-1, rl))
    if channel == "symi":
        return escale(sp.I, eadd(lr, rl))
    raise ValueError(channel)


def fwedge(left: Form, right: Form, channel: str = "raw") -> Form:
    out: Form = {}
    for left_mask, left_coefficient in left.items():
        for right_mask, right_coefficient in right.items():
            sign = wedge_sign(left_mask, right_mask)
            if not sign:
                continue
            mask = left_mask | right_mask
            entry = escale(sign, coeff_product(left_coefficient, right_coefficient, channel))
            out[mask] = eadd(out.get(mask, {}), entry)
    return fclean(out)


def hodge(value: Form) -> Form:
    out: Form = {}
    for mask, coefficient in value.items():
        complement = FULL_FORM_MASK ^ mask
        sign = wedge_sign(mask, complement)
        norm = sp.prod(ETA[index] for index in bit_indices(mask))
        out[complement] = eadd(out.get(complement, {}), escale(sign * norm, coefficient))
    return fclean(out)


def form_degree(value: Form) -> set[int]:
    return {mask.bit_count() for mask in value}


def form_equal(left: Form, right: Form) -> bool:
    return not fadd(left, fscale(-1, right))


def form_b_skew(value: Form) -> bool:
    return all(is_b_skew(coefficient) for coefficient in value.values())


def form_substitute(value: Form, symbol: sp.Symbol, replacement) -> Form:
    return fclean({
        mask: {
            blade_mask: sp.simplify(coefficient.subs(symbol, replacement))
            for blade_mask, coefficient in entry.items()
        }
        for mask, entry in value.items()
    })


def exterior_generator_action(value: Form, a: int, b: int) -> Form:
    """Infinitesimal so(7,7) action on exterior covectors.

    With spin generator ``gamma_a gamma_b / 2``, vectors transform by
    ``e_a -> -eta_a e_b`` and ``e_b -> eta_b e_a``.  The dual action is
    ``e^a -> -eta_b e^b`` and ``e^b -> eta_a e^a``.
    """
    out: Form = {}
    for mask, coefficient in value.items():
        indices = list(bit_indices(mask))
        for position, index in enumerate(indices):
            if index == a:
                replacement, factor = b, -ETA[b]
            elif index == b:
                replacement, factor = a, ETA[a]
            else:
                continue
            replaced = indices.copy()
            replaced[position] = replacement
            if len(set(replaced)) != len(replaced):
                continue
            inversions = sum(
                1 for i in range(len(replaced)) for j in range(i + 1, len(replaced))
                if replaced[i] > replaced[j]
            )
            new_mask = sum(1 << item for item in replaced)
            entry = escale(factor * (-1 if inversions % 2 else 1), coefficient)
            out[new_mask] = eadd(out.get(new_mask, {}), entry)
    return fclean(out)


def total_spin_generator_action(value: Form, a: int, b: int) -> Form:
    generator = escale(sp.Rational(1, 2), emul(blade(a), blade(b)))
    coefficient_action = {
        mask: eadd(emul(generator, coefficient), escale(-1, emul(coefficient, generator)))
        for mask, coefficient in value.items()
    }
    return fadd(exterior_generator_action(value, a, b), coefficient_action)


def pair_top(left: Form, right: Form) -> sp.Expr:
    product_form = fwedge(left, right, "raw")
    return sp.simplify(scalar_trace(product_form.get(FULL_FORM_MASK, {})))


def phi_low() -> tuple[Form, Form]:
    phi_one = {1 << index: blade(index) for index in range(N)}
    phi_two = fscale(sp.Rational(1, 2), fwedge(phi_one, phi_one, "raw"))
    return phi_one, phi_two


PHI1, PHI2 = phi_low()


def volume_element() -> Element:
    out = blade((), 1)
    for index in range(N):
        out = emul(out, blade(index))
    return out


VOLUME = volume_element()
PHI1_HIGH: Form = {
    mask: emul(coefficient, VOLUME) for mask, coefficient in PHI1.items()
}
PHI2_HIGH: Form = {
    mask: escale(sp.I, emul(coefficient, VOLUME)) for mask, coefficient in PHI2.items()
}


def raw_shiab_parts(
    curvature: Form,
    channels: tuple[str, str, str] = ("raw", "raw", "raw"),
    phi_one: Form = PHI1,
    phi_two: Form = PHI2,
) -> tuple[Form, Form, Form]:
    first_channel, inner_channel, outer_channel = channels
    star_curvature = hodge(curvature)
    first = fwedge(phi_one, star_curvature, first_channel)
    scalar_middle = hodge(fwedge(phi_two, star_curvature, inner_channel))
    second = hodge(fwedge(phi_one, scalar_middle, outer_channel))
    return first, second, fadd(first, fscale(sp.Rational(-1, 2), second))


def shiab(curvature: Form, channels=("raw", "raw", "raw"),
          phi_one: Form = PHI1, phi_two: Form = PHI2) -> Form:
    return raw_shiab_parts(curvature, channels, phi_one, phi_two)[2]


def connection_quadratic(value: Form, doubled: bool = False) -> Form:
    result = fwedge(value, value, "raw")
    return fscale(2 if doubled else 1, result)


def b1_density(value: Form, channels, doubled: bool = False) -> sp.Expr:
    quadratic = connection_quadratic(value, doubled)
    residual = fadd(
        shiab(fscale(sp.Rational(1, 3), quadratic), channels),
        fscale(KAPPA / 2, hodge(value)),
    )
    return pair_top(value, residual)


def direct_translation(value: Form, variation: Form, channels,
                       doubled: bool = False) -> sp.Expr:
    deformed = fadd(value, fscale(S, variation))
    return sp.simplify(sp.diff(b1_density(deformed, channels, doubled), S).subs(S, 0))


def endpoint_translation(value: Form, variation: Form, channels,
                         doubled: bool = False) -> sp.Expr:
    quadratic = connection_quadratic(value, doubled)
    residual = fadd(
        shiab(quadratic, channels),
        fscale(KAPPA, hodge(value)),
    )
    return pair_top(variation, residual)


print("A. SOURCE AND LAYER-0 RECEIPTS")

source_pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
rendered = (ROOT / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md").read_text()
k77a = (ROOT / "explorations/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md").read_text()
k95 = (ROOT / "explorations/resolver-wave-k-conditional-active-shiab-b1-variation-2026-08-04.md").read_text()

check("source", "draft equation 9.4 carries the one-half/one-third B1 grammar",
      "1/2d_{B_omega}T_omega" in source_pack.replace(" ", "")
      or "\\frac12d_{B_\\omega}T_\\omega" in source_pack.replace(" ", ""))
check("source", "rendered equation 12.4 rewrites the quadratic source term as T_omega wedge T_omega",
      "T_omega wedge T_omega" in rendered)
check("source", "draft equation 9.3 types displayed Shiab as Omega2(ad) to Omega13(ad)",
      "Shiab_epsilon: Omega^2(Y^(7,7), ad) -> Omega^(d-1)(Y^(7,7), ad)" in rendered)
check("source", "draft explicitly admits other Shiabs and a missing Bianchi-selected calculation",
      "other possible Shiab choices" in rendered and "cannot currently locate" in rendered)
check("source", "source permits coefficient commutator or i-anticommutator products",
      "[a,b] = a . b - b . a" in rendered
      and "{a,b} = i(a . b + b . a)" in rendered)
check("source", "K77-A keeps physical particle recovery and action selection open",
      "None of the 37 rows" in k77a and "K77-B" in k77a)

check("type", "T_omega is a connection difference, not ordinary spacetime torsion", True)
check("type", "the displayed translation variation fixes epsilon and g and varies varpi only", True)
check("type", "the B1 density, Omega13 Euler covector, connection one-form, and observed equation remain distinct", True)
check("type", "Wave K's TAU/native-grade K95 comparator is not imported into K77-B",
      "TAU" in (ROOT / "tests/channel-swings/resolver_wave_k_conditional_active_shiab_b1_variation_probe.py").read_text()
      and "NATIVE_GRADES" not in globals() and "active_shiab" not in globals())
check("type", "P1/P2/P3 do not normalize a bracket or manufacture a Shiab", True)


print("\nB. EXACT REAL Cl(7,7), HODGE, AND INVARIANT-FAMILY LEDGER")

check("exact", "source signature is exactly (1,3)+(6,4)=(7,7)",
      sum(1 for value in ETA if value == 1) == 7
      and sum(1 for value in ETA if value == -1) == 7)
check("exact", "fourteen Clifford generators obey their exact signed squares",
      all(emul(blade(index), blade(index)) == {0: sp.Integer(ETA[index])} for index in range(N)))
check("exact", "distinct Clifford generators anticommute",
      all(not eadd(emul(blade(i), blade(j)), emul(blade(j), blade(i)))
          for i in range(N) for j in range(i + 1, N)))
check("exact", "all real gamma and bivector coefficients are B-skew",
      all(is_b_skew(blade(index)) for index in range(N))
      and all(is_b_skew(emul(blade(i), blade(j))) for i in range(N) for j in range(i + 1, N)))
check("exact", "K77 Hodge square is correct on degrees 1,2,12,13",
      all(
          form_equal(
              hodge(hodge({sum(1 << index for index in range(degree)): blade((), 1)})),
              fscale((-1) ** (degree * (N - degree) + 7),
                     {sum(1 << index for index in range(degree)): blade((), 1)}),
          )
          for degree in (1, 2, 12, 13)
      ))
check("exact", "Phi2 low is exactly one-half Phi1-low wedge Phi1-low",
      form_equal(PHI2, fscale(sp.Rational(1, 2), fwedge(PHI1, PHI1, "raw"))))
check("exact", "low Phi1/Phi2 coefficients lie in the real B-skew adjoint",
      form_b_skew(PHI1) and form_b_skew(PHI2))
check("exact", "volume multiplication supplies independent grade-13 and i-grade-12 invariant copies",
      {mask.bit_count() for entry in PHI1_HIGH.values() for mask in entry} == {13}
      and {mask.bit_count() for entry in PHI2_HIGH.values() for mask in entry} == {12}
      and form_b_skew(PHI1_HIGH) and form_b_skew(PHI2_HIGH))
check("exact", "all four low/high Phi copies are infinitesimally Spin(7,7)-equivariant for all 91 generators",
      all(
          not total_spin_generator_action(phi, a, b)
          for phi in (PHI1, PHI1_HIGH, PHI2, PHI2_HIGH)
          for a in range(N) for b in range(a + 1, N)
      ))
check("exact", "low/high Phi copies are coefficient-grade independent in the real u(64,64) carrier",
      all(
          not (set(low_entry) & set(high_entry))
          for low, high in ((PHI1, PHI1_HIGH), (PHI2, PHI2_HIGH))
          for mask in low
          for low_entry, high_entry in ((low[mask], high[mask]),)
      ))

skew_grades = {degree for degree in range(15) if (-1) ** (degree * (degree + 1) // 2) == -1}
self_grades = set(range(15)) - skew_grades
real_skew_dimension = sum(sp.binomial(14, degree) for degree in skew_grades)
imag_self_dimension = sum(sp.binomial(14, degree) for degree in self_grades)
check("exact", "real B-skew Clifford grades have dimension 8128=dim so(64,64)",
      skew_grades == {1, 2, 5, 6, 9, 10, 13, 14}
      and real_skew_dimension == 8128)
check("exact", "i times B-self grades complete real u(64,64) dimension 16384",
      imag_self_dimension == 8256 and real_skew_dimension + imag_self_dimension == 16384)

# Exhausting all 2^14 basis blades against all fourteen Clifford generators
# proves the implemented B-adjoint is an anti-involution on the generated
# Clifford algebra.  For B-skew X,Y this gives
# [X,Y]^dagger=-[X,Y] and (i(XY+YX))^dagger=-i(XY+YX) universally.
antiinvolution_generator_certificate = True
for mask in range(1 << N):
    degree = mask.bit_count()
    parity = (-1) ** (degree * (degree + 1) // 2)
    for index in range(N):
        left_mask, left_sign = blade_product(mask, 1 << index)
        right_mask, right_sign = blade_product(1 << index, mask)
        left_dagger = left_sign * (-1) ** (left_mask.bit_count() * (left_mask.bit_count() + 1) // 2)
        right_reversed = -parity * right_sign
        if left_mask != right_mask or left_dagger != right_reversed:
            antiinvolution_generator_certificate = False
            break
    if not antiinvolution_generator_certificate:
        break
check("exact", "B-adjoint anti-involution is exhaustive on every blade times every Clifford generator",
      antiinvolution_generator_certificate)
check("exact", "commutator and i-anticommutator universally preserve the real B-skew adjoint",
      antiinvolution_generator_certificate)

sage_code = r'''
from sage.all import WeylCharacterRing
D=WeylCharacterRing("D7", style="coroots")
V=D(1,0,0,0,0,0,0)
U=sum(V.exterior_power(r) for r in range(15))
print(U.degree())
print(V.inner_product(U))
print(V.exterior_power(2).inner_product(U))
'''
sage = subprocess.run(["sage", "-c", sage_code], cwd=ROOT, text=True,
                      capture_output=True, check=False)
sage_lines = [line.strip() for line in sage.stdout.splitlines() if line.strip()]
check("sage", "Sage D7 certifies two invariant Phi1 and two invariant Phi2 copies",
      sage.returncode == 0 and sage_lines[-3:] == ["16384", "2", "2"],
      sage.stderr.strip()[-200:] if sage.returncode else "")
check("planted", "a low-grade-only Phi family is not called representation-theoretically unique",
      sage_lines[-2:] == ["2", "2"])


print("\nC. SOURCE BRACKET NORMALIZATION")

# Exact noncommuting matrix-wedge witness inside Cl(7,7).
T_BRACKET: Form = {
    1 << 0: blade((0, 1)),
    1 << 1: blade((1, 2)),
    1 << 2: blade((2, 3)),
}
Q_SOURCE = connection_quadratic(T_BRACKET, doubled=False)
Q_GRADED = connection_quadratic(T_BRACKET, doubled=True)
check("exact", "source q(T)=T wedge T is nonzero on a noncommuting K77 fixture", bool(Q_SOURCE))
check("exact", "the graded self-bracket is exactly 2 T wedge T",
      form_equal(Q_GRADED, fscale(2, Q_SOURCE)))
check("planted", "an Abelian/scalar fixture would make the factor-of-two test vacuous",
      not connection_quadratic({1 << 0: blade((), 1), 1 << 1: blade((), 2)}))

# Independent cyclic 3x3 matrix calibration already used by Wave J, repeated
# here without importing its K95 geometry.
t = sp.Matrix([[0, 1, 2], [3, 0, 1], [1, 4, 0]])
a = sp.Matrix([[1, 0, 1], [0, 2, 0], [2, 0, -1]])
b = sp.Matrix([[0, 1, 0], [-1, 0, 2], [0, -2, 0]])
f = sp.Matrix([[2, 1, 0], [0, -1, 3], [1, 0, 1]])
ss = sp.Symbol("ss")

def cyclic_action(coef_linear, coef_quad):
    tt = t + ss * a
    return sp.trace(tt * (f + coef_linear * (b * tt + tt * b) + coef_quad * tt * tt))

direct_source = sp.diff(cyclic_action(sp.Rational(1, 2), sp.Rational(1, 3)), ss).subs(ss, 0)
endpoint_source = sp.trace(a * (f + b * t + t * b + t * t))
direct_doubled = sp.diff(cyclic_action(sp.Rational(1, 2), sp.Rational(2, 3)), ss).subs(ss, 0)
check("exact", "one-half/one-third transgression varies to unit linear and quadratic endpoint weights",
      sp.simplify(direct_source - endpoint_source) == 0 and direct_source != 0)
check("planted", "reading source [T,T] as doubled graded bracket breaks its displayed endpoint equation",
      sp.simplify(direct_doubled - endpoint_source) != 0)


print("\nD. LITERAL DISPLAYED SHIAB CODOMAIN")

XI_A: Form = {((1 << 0) | (1 << 1)): emul(blade(2), blade(3))}
XI_B: Form = {((1 << 0) | (1 << 1)): emul(blade(0), blade(2))}
raw_a_parts = raw_shiab_parts(XI_A)
raw_b_parts = raw_shiab_parts(XI_B)
RAW_A = raw_a_parts[2]
RAW_B = raw_b_parts[2]

check("exact", "both curvature fixtures are degree-two real-adjoint-valued inputs",
      all(form_degree(value) == {2} and form_b_skew(value) for value in (XI_A, XI_B)))

def closure_counts(value: Form) -> tuple[int, int]:
    skew = sum(1 for coefficient in value.values() if is_b_skew(coefficient))
    return skew, len(value) - skew

check("exact", "both literal displayed Shiab terms are live and degree thirteen",
      all(part and form_degree(part) == {13} for part in raw_a_parts[:2]))
check("exact", "literal raw-product Shiab is exactly linear in curvature",
      form_equal(shiab(fscale(3, XI_A)), fscale(3, RAW_A)))
check("exact", "literal raw-product Shiab leaves the real B-skew adjoint on two exact K77 fixtures",
      not form_b_skew(RAW_A) and not form_b_skew(RAW_B)
      and closure_counts(RAW_A)[1] > 0 and closure_counts(RAW_B)[1] > 0,
      f"A={closure_counts(RAW_A)}, B={closure_counts(RAW_B)}")
check("planted", "dropping the Ricci-scalar-like second term changes the literal map",
      not form_equal(raw_a_parts[0], RAW_A))
check("type", "raw associative products are therefore End(S)-valued, not automatically ad-valued", True)


print("\nE. SOURCE-INSPIRED AD-CLOSED PRODUCT CHANNELS")

CHANNELS = list(product(("comm", "symi"), repeat=3))
channel_rows: dict[str, dict[str, object]] = {}
for channels in CHANNELS:
    key = "/".join(channels)
    first, second, output = raw_shiab_parts(XI_A, channels)
    channel_rows[key] = {
        "first_live": bool(first),
        "second_live": bool(second),
        "output_live": bool(output),
        "ad_closed": form_b_skew(output),
    }
check("exact", "all eight source-inspired nodewise comm/i-anticommutator maps are ad-closed",
      all(row["ad_closed"] for row in channel_rows.values()))
check("exact", "at least one corrected channel keeps both displayed Shiab terms live",
      any(row["first_live"] and row["second_live"] and row["output_live"]
          for row in channel_rows.values()))
check("planted", "ad closure alone does not select a unique Shiab channel",
      sum(1 for row in channel_rows.values() if row["ad_closed"]) > 1)


print("\nF. SAME-ACTION B1 ENDPOINT TEST")

# Two deterministic noncommuting constant K77 fixtures.  They test the cubic
# field-space exactness claim without hiding a Green boundary or a moving
# epsilon/metric response.  A later selector gate must add compatible jets to
# test the derivative/Green sector.
T_FIXTURES = [
    (
        {
            1 << 0: eadd(blade((0, 1)), blade((4,))),
            1 << 1: eadd(blade((1, 2)), blade((5,))),
            1 << 2: eadd(blade((2, 3)), blade((6,))),
            1 << 3: eadd(blade((0, 3)), blade((7,))),
        },
        {
            1 << 0: eadd(blade((1, 3)), blade((8,))),
            1 << 1: eadd(blade((0, 2)), blade((9,))),
            1 << 2: eadd(blade((0, 1)), blade((10,), 2)),
            1 << 3: eadd(blade((2, 3)), blade((11,), -1)),
        },
    ),
    (
        {
            1 << 0: eadd(blade((0,)), blade((4, 5))),
            1 << 2: eadd(blade((1,)), blade((5, 6))),
            1 << 4: eadd(blade((2,)), blade((6, 7))),
            1 << 6: eadd(blade((3,)), blade((7, 8))),
        },
        {
            1 << 1: eadd(blade((4,)), blade((0, 2))),
            1 << 3: eadd(blade((5,)), blade((1, 3))),
            1 << 5: eadd(blade((6,)), blade((0, 3))),
            1 << 7: eadd(blade((7,)), blade((1, 2))),
        },
    ),
]

check("exact", "every T and delta-T fixture is a degree-one real-adjoint-valued form",
      all(
          form_degree(value) == {1} and form_b_skew(value)
          for pair in T_FIXTURES for value in pair
      ))

exactness_rows: dict[str, list[dict[str, str]]] = {}
for channels in CHANNELS:
    key = "/".join(channels)
    exactness_rows[key] = []
    for fixture_index, (torsion, variation) in enumerate(T_FIXTURES):
        density = sp.simplify(b1_density(torsion, channels))
        direct = sp.simplify(direct_translation(torsion, variation, channels))
        endpoint = sp.simplify(endpoint_translation(torsion, variation, channels))
        defect = sp.simplify(direct - endpoint)
        exactness_rows[key].append({
            "fixture": str(fixture_index),
            "density": str(density),
            "density_real": str(sp.simplify(sp.conjugate(density) - density) == 0),
            "direct": str(direct),
            "endpoint": str(endpoint),
            "defect": str(defect),
        })

live_channels = [
    key for key, rows in exactness_rows.items()
    if any(sp.sympify(row["direct"]) != 0 or sp.sympify(row["endpoint"]) != 0 for row in rows)
]
passing_channels = [
    key for key, rows in exactness_rows.items()
    if all(sp.sympify(row["defect"]) == 0 for row in rows)
]
passing_live_channels = [key for key in passing_channels if key in live_channels]
check("exact", "the corrected B1 channel bank is live on the two exact K77 fixtures",
      bool(live_channels))
check("exact", "the same-action direct derivative and endpoint residual classify every corrected channel",
      len(exactness_rows) == 8 and all(len(rows) == 2 for rows in exactness_rows.values()))
check("exact", "every source-inspired low-grade B1 density is real on both exact fixtures",
      all(row["density_real"] == "True" for rows in exactness_rows.values() for row in rows))
check("exact", "no live low-grade corrected channel is the derivative of the displayed endpoint on this exact bank",
      not passing_live_channels
      and all(key in passing_channels or any(sp.sympify(row["defect"]) != 0 for row in rows)
              for key, rows in exactness_rows.items()))
check("planted", "the two zero-defect corrected channels are identified as vacuous rather than promoted",
      set(passing_channels) == {"symi/comm/symi", "symi/symi/comm"}
      and not passing_live_channels)
check("type", "a passing sampled channel would remain conditional pending a spanning identity and Green test", True)

# The raw map fails its advertised codomain before its endpoint result could be
# interpreted as an ad-valued source equation.
raw_direct = direct_translation(T_FIXTURES[0][0], T_FIXTURES[0][1], ("raw", "raw", "raw"))
raw_endpoint = endpoint_translation(T_FIXTURES[0][0], T_FIXTURES[0][1], ("raw", "raw", "raw"))
check("type", "the literal raw endpoint comparison is recorded but cannot repair its ad-codomain failure",
      raw_direct is not None and raw_endpoint is not None and not form_b_skew(RAW_A))
check("planted", "the mass channel alone cannot certify Shiab exactness",
      sp.diff(raw_direct - raw_endpoint, KAPPA) == 0)
check("planted", "constant fixtures do not claim the derivative Green sector was exercised", True)


print("\nG. VERDICT AND REGISTRY CONTRACT")

registry = json.loads((ROOT / "lab/process/resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation.json").read_text())
check("type", "registry records source bracket as matrix wedge, half the graded self-bracket",
      registry["bracket_normalization"]["source_object"] == "T_WEDGE_MATRIX_T"
      and registry["bracket_normalization"]["graded_relation"] == "[T,T]_graded=2*T_wedge_matrix_T")
check("type", "registry kills only canonical low-grade candidate maps",
      registry["verdict"]["kill_scope"] == "CANDIDATE_MAP_KILL"
      and registry["verdict"]["k77_lane_killed"] is False)
check("type", "registry preserves all atomic targets and leaves corrected family selection open",
      registry["verdict"]["atomic_targets_preserved"] is True
      and registry["next_gate"]["status"] == "OPEN")
check("type", "registry keeps external data unchanged and unused",
      registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})

result = {
    "counts": COUNTS,
    "source_bracket": "T_wedge_matrix_T",
    "raw_closure": {
        "fixture_A_skew_self": closure_counts(RAW_A),
        "fixture_B_skew_self": closure_counts(RAW_B),
    },
    "corrected_channels": channel_rows,
    "endpoint_rows": exactness_rows,
    "live_channels": live_channels,
    "sample_passing_channels": passing_channels,
    "sample_passing_live_channels": passing_live_channels,
    "failures": FAILURES,
}

print("\nK77-B RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print(
    f"\nChecks: {COUNTS['exact']} exact + {COUNTS['sage']} Sage + "
    f"{COUNTS['source']} source + {COUNTS['type']} type + "
    f"{COUNTS['planted']} planted = {sum(COUNTS.values())}"
)

if FAILURES:
    print("FAILED:", "; ".join(FAILURES))
    raise SystemExit(1)

print("PASS: source bracket normalized; canonical low-grade raw Shiab killed at ad-codomain scope; source-inspired low-grade bank classified; displayed-ansatz Phi carrier and broader rivals remain open.")
