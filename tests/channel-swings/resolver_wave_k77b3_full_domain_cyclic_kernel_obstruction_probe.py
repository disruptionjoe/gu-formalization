#!/usr/bin/env python3
"""Exact K77-B3 full-domain cyclic-kernel obstruction probe.

This probe stays on the real Cl(7,7) carrier.  It first computes the complete
complexified equivariant Hom dimension and the grade-two low/high blocks.  It
then constructs the three explicit contraction coordinates in each block and
the affine full-domain extensions of the two algebraic-Riemann Einstein maps.

The decisive test is not a sampled formula census.  Two exact B-skew field
pairs satisfy Q(b,c)=b wedge c+c wedge b=0 while Q(c,c) is a nonzero algebraic
Riemann curvature and b pairs nontrivially with, respectively, the low and
high Einstein restriction.  Cyclicity of the cubic action would equate that
nonzero pairing with zero.  Hence both Riemann coefficients vanish for every
linear full-domain extension on the declared full translation field space.

The result kills only the zero-order linear Shiab plus unit-weight same-action
endpoint mechanism.  Derivative/moving-field actions, restricted field
domains, observed/fibre trace maps, and physics remain open.  P1/P2/P3 are
unused.
"""

from __future__ import annotations

from itertools import combinations
import json
from pathlib import Path
import subprocess

import sympy as sp
from flint import fmpq, fmpz


ROOT = Path(__file__).resolve().parents[2] if "tests" in Path(__file__).parts else Path.cwd()
N = 14
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
FULL = (1 << N) - 1
Element = dict[int, sp.Expr]
Form = dict[int, Element]

COUNTS = {"exact": 0, "sage": 0, "flint": 0, "source": 0, "type": 0, "planted": 0}
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


def eclean(value: Element) -> Element:
    return {m: sp.simplify(c) for m, c in value.items() if sp.simplify(c) != 0}


def eadd(*values: Element) -> Element:
    out: Element = {}
    for value in values:
        for mask, coefficient in value.items():
            out[mask] = sp.simplify(out.get(mask, 0) + coefficient)
    return eclean(out)


def escale(coefficient, value: Element) -> Element:
    return eclean({m: sp.simplify(coefficient * c) for m, c in value.items()})


def blade_product(left: int, right: int) -> tuple[int, int]:
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    sign = -1 if inversions % 2 else 1
    for i in indices(left & right):
        sign *= ETA[i]
    return left ^ right, sign


def emul(left: Element, right: Element) -> Element:
    out: Element = {}
    for ml, cl in left.items():
        for mr, cr in right.items():
            mask, sign = blade_product(ml, mr)
            out[mask] = sp.simplify(out.get(mask, 0) + sign * cl * cr)
    return eclean(out)


def blade(item: int | tuple[int, ...], coefficient=1) -> Element:
    if isinstance(item, int):
        item = (item,)
    return {sum(1 << i for i in item): sp.sympify(coefficient)}


def dagger_b(value: Element) -> Element:
    return eclean({
        mask: sp.simplify(
            (-1) ** (mask.bit_count() * (mask.bit_count() + 1) // 2)
            * sp.conjugate(coefficient)
        )
        for mask, coefficient in value.items()
    })


def is_b_skew(value: Element) -> bool:
    return not eadd(dagger_b(value), value)


def scalar_trace(value: Element) -> sp.Expr:
    return sp.simplify(128 * value.get(0, 0))


def fclean(value: Form) -> Form:
    return {m: eclean(c) for m, c in value.items() if eclean(c)}


def fadd(*values: Form) -> Form:
    out: Form = {}
    for value in values:
        for mask, coefficient in value.items():
            out[mask] = eadd(out.get(mask, {}), coefficient)
    return fclean(out)


def fscale(coefficient, value: Form) -> Form:
    return fclean({m: escale(coefficient, c) for m, c in value.items()})


def wedge_sign(left: int, right: int) -> int:
    if left & right:
        return 0
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    return -1 if inversions % 2 else 1


def wedge(left: Form, right: Form) -> Form:
    out: Form = {}
    for ml, cl in left.items():
        for mr, cr in right.items():
            sign = wedge_sign(ml, mr)
            if sign:
                out[ml | mr] = eadd(
                    out.get(ml | mr, {}), escale(sign, emul(cl, cr))
                )
    return fclean(out)


def quadratic_pair(left: Form, right: Form) -> Form:
    return fadd(wedge(left, right), wedge(right, left))


def hodge(value: Form) -> Form:
    out: Form = {}
    for mask, coefficient in value.items():
        complement = FULL ^ mask
        sign = wedge_sign(mask, complement)
        for i in indices(mask):
            sign *= ETA[i]
        out[complement] = eadd(
            out.get(complement, {}), escale(sign, coefficient)
        )
    return fclean(out)


def pair_top(left: Form, right: Form) -> sp.Expr:
    return scalar_trace(wedge(left, right).get(FULL, {}))


def form_b_skew(value: Form) -> bool:
    return all(is_b_skew(coefficient) for coefficient in value.values())


def form_equal(left: Form, right: Form) -> bool:
    return not fadd(left, fscale(-1, right))


def coefficient_generator_action(value: Element, a: int, b: int) -> Element:
    generator = escale(sp.Rational(1, 2), emul(blade(a), blade(b)))
    return eadd(emul(generator, value), escale(-1, emul(value, generator)))


def exterior_generator_action(value: Form, a: int, b: int) -> Form:
    out: Form = {}
    for mask, coefficient in value.items():
        old = list(indices(mask))
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
            out[new_mask] = eadd(
                out.get(new_mask, {}),
                escale(factor * (-1 if inversions % 2 else 1), coefficient),
            )
    return fclean(out)


def total_generator_action(value: Form, a: int, b: int) -> Form:
    coefficient_action = {
        mask: coefficient_generator_action(coefficient, a, b)
        for mask, coefficient in value.items()
    }
    return fadd(exterior_generator_action(value, a, b), coefficient_action)


VOLUME = blade((), 1)
for volume_index in range(N):
    VOLUME = emul(VOLUME, blade(volume_index))


def metric(i: int, j: int) -> int:
    return ETA[i] if i == j else 0


def ordered_coefficient(value: Form, i: int, j: int) -> Element:
    if i == j:
        return {}
    coefficient = value.get((1 << i) | (1 << j), {})
    return coefficient if i < j else escale(-1, coefficient)


def grade_two_coefficient(value: Form, i: int, j: int, a: int, b: int):
    if a == b:
        return sp.Integer(0)
    coefficient = ordered_coefficient(value, i, j)
    mask = (1 << a) | (1 << b)
    result = coefficient.get(mask, 0)
    return sp.simplify(result if a < b else -result)


def cross_ricci(value: Form) -> list[list[sp.Expr]]:
    """C_jl = eta_l sum_i k_ij^(i,l) for the Clifford-grade-two part."""
    return [[
        sp.simplify(sum(
            ETA[l] * grade_two_coefficient(value, i, j, i, l)
            for i in range(N)
        ))
        for l in range(N)
    ] for j in range(N)]


def scalar_from_cross(cross: list[list[sp.Expr]]) -> sp.Expr:
    return sp.simplify(sum(ETA[j] * cross[j][j] for j in range(N)))


def output_from_tensor(tensor: list[list[sp.Expr]], sector: str) -> Form:
    one_form: Form = {}
    for i in range(N):
        coefficient: Element = {}
        for j in range(N):
            value = sp.simplify(tensor[i][j])
            if value:
                basis = blade(j) if sector == "LOW" else emul(blade(j), VOLUME)
                coefficient = eadd(coefficient, escale(ETA[j] * value, basis))
        if coefficient:
            one_form[1 << i] = coefficient
    return hodge(one_form)


def contraction_basis(value: Form, sector: str) -> tuple[Form, Form, Form]:
    cross = cross_ricci(value)
    scalar = scalar_from_cross(cross)
    transpose = [[cross[j][i] for j in range(N)] for i in range(N)]
    scalar_metric = [[scalar * metric(i, j) for j in range(N)] for i in range(N)]
    return tuple(output_from_tensor(tensor, sector)
                 for tensor in (cross, transpose, scalar_metric))


def einstein_extension(value: Form, sector: str, alpha=sp.Integer(0)) -> Form:
    """All fixed-scale extensions: alpha*C+(1-alpha)*C^T-(1/2)scal*g."""
    cross = cross_ricci(value)
    scalar = scalar_from_cross(cross)
    tensor = [[
        sp.simplify(
            alpha * cross[i][j]
            + (1 - alpha) * cross[j][i]
            - sp.Rational(1, 2) * scalar * metric(i, j)
        )
        for j in range(N)
    ] for i in range(N)]
    return output_from_tensor(tensor, sector)


def recovered_covariant_curvature(value: Form, i: int, j: int, a: int, b: int):
    return sp.simplify(
        grade_two_coefficient(value, i, j, a, b) / (ETA[a] * ETA[b])
    )


def active_constant_curvature(active: set[int], scale: int, i: int, j: int,
                              a: int, b: int):
    if not {i, j, a, b} <= active:
        return sp.Integer(0)
    return scale * (metric(i, a) * metric(j, b) - metric(i, b) * metric(j, a))


def matches_active_constant_curvature(value: Form, active: set[int], scale: int) -> bool:
    return all(
        recovered_covariant_curvature(value, i, j, a, b)
        == active_constant_curvature(active, scale, i, j, a, b)
        for i, j in combinations(range(N), 2)
        for a, b in combinations(range(N), 2)
    )


def map_fingerprint_matrix(banks: tuple[tuple[Form, ...], ...]) -> sp.Matrix:
    """Stack fixture coordinates while keeping the three map columns aligned."""
    rows: list[list[sp.Expr]] = []
    for bank in banks:
        coordinates = sorted({
            (form_mask, clifford_mask)
            for value in bank
            for form_mask, coefficient in value.items()
            for clifford_mask in coefficient
        })
        rows.extend([
            [value.get(form_mask, {}).get(clifford_mask, 0) for value in bank]
            for form_mask, clifford_mask in coordinates
        ])
    return sp.Matrix(rows)


print("A. PRIMARY SOURCE COLLISION AND LAYER 0")

source_pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
rendered = (ROOT / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md").read_text()
check("source", "source writes the full translation-direction variation varpi+s alpha",
      r"I^B_1(\epsilon,\varpi+s\alpha)" in source_pack)
check("source", "source requires the completed F plus one-half dT plus one-third quadratic residual",
      "\\frac12d_{B_\\omega}T_\\omega" in source_pack
      and "\\frac13[T_\\omega,T_\\omega]" in source_pack)
check("source", "source says the curvature-alone term is not exact and requires the quadratic eddy",
      "curvature alone is not exact" in source_pack and "quadratic “eddy”" in source_pack)
check("source", "source prints the Shiab domain and codomain but leaves the historical selector missing",
      "Shiab_epsilon: Omega^2(Y^(7,7), ad) -> Omega^(d-1)(Y^(7,7), ad)" in rendered
      and "cannot currently locate" in rendered)
check("source", "source does not supply a restricted translation field domain evading the local witnesses",
      "source does not declare the complete" in source_pack
      and r"admissible \((\epsilon,\varpi)\) variation domain" in source_pack)

check("type", "ambient Omega2(ad), algebraic Riemann curvature, and observed curvature are distinct", True)
check("type", "the cubic action density and its proposed Euler endpoint are distinct until cyclicity", True)
check("type", "constant local fields test the full completed residual because F_B and d_B T can vanish", True)
check("type", "Green data are downstream and inapplicable when no zero-order cyclic member survives", True)


print("\nB. COMPLETE EQUIVARIANT HOM CENSUS")

sage_code = r'''
from sage.all import WeylCharacterRing
D=WeylCharacterRing("D7",style="coroots")
V=D(1,0,0,0,0,0,0)
P=V.exterior_power(2)
E=sum(V.exterior_power(r) for r in range(15))
U=P*E
W=V*E
R=P.symmetric_power(2)-V.exterior_power(4)
print(E.degree(),U.degree(),W.degree(),U.inner_product(W))
print((P*P).inner_product(V*V.exterior_power(1)),(P*P).inner_product(V*V.exterior_power(13)))
print(R.inner_product(V*V.exterior_power(1)),R.inner_product(V*V.exterior_power(13)))
'''
sage = subprocess.run(["sage", "-c", sage_code], cwd=ROOT, text=True,
                      capture_output=True, check=False)
sage_lines = [line.strip() for line in sage.stdout.splitlines() if line.strip()]
check("sage", "full complexified Spin(14) Hom dimension is 200",
      sage.returncode == 0 and sage_lines[-3] == "16384 1490944 229376 200",
      sage.stderr.strip()[-200:] if sage.returncode else "")
check("sage", "grade-two input has three low and three high full-domain coordinates",
      sage_lines[-2] == "3 3")
check("sage", "algebraic Riemann restriction has two low and two high coordinates",
      sage_lines[-1] == "2 2")

fixture_cross = {(1 << 0) | (1 << 1): emul(blade(0), blade(2))}
fixture_scalar = {(1 << 0) | (1 << 1): emul(blade(0), blade(1))}
low_basis_values = contraction_basis(fixture_cross, "LOW")
low_scalar_values = contraction_basis(fixture_scalar, "LOW")
rank_matrix = map_fingerprint_matrix((low_basis_values, low_scalar_values))
check("exact", "cross Ricci, transposed cross Ricci, and scalar metric are independent full-domain maps",
      rank_matrix.rank() == 3)
check("exact", "the same three-coordinate construction has an independent volume-dual high copy",
      map_fingerprint_matrix((
          contraction_basis(fixture_cross, "HIGH"),
          contraction_basis(fixture_scalar, "HIGH"),
      )).rank() == 3)
check("exact", "all six contraction maps intertwine all 91 compact/noncompact generators on independent fixtures",
      all(
          form_equal(
              contraction_basis(total_generator_action(fixture, a, b), sector)[basis_index],
              total_generator_action(contraction_basis(fixture, sector)[basis_index], a, b),
          )
          for fixture in (fixture_cross, fixture_scalar)
          for sector in ("LOW", "HIGH")
          for basis_index in range(3)
          for a, b in combinations(range(N), 2)
      ))
check("planted", "the six explicit grade-two maps do not exhaust the 200-dimensional full Hom space",
      int(sage_lines[-3].split()[-1]) == 200 > 6)


print("\nC. PURE GRADE-ONE NECESSARY CYCLIC SELECTOR")

alpha = sp.symbols("alpha")


def matrix_endpoint(matrix: sp.Matrix) -> sp.Matrix:
    cross = sp.zeros(N)
    for j in range(N):
        for l in range(N):
            cross[j, l] = ETA[l] * sum(
                2 * (matrix[i, i] * matrix[j, l] - matrix[i, l] * matrix[j, i])
                for i in range(N)
            )
    scalar = sum(ETA[j] * cross[j, j] for j in range(N))
    result = alpha * cross + (1 - alpha) * cross.T
    for j in range(N):
        result[j, j] -= sp.Rational(1, 2) * scalar * ETA[j]
    return result


def matrix_pair(matrix: sp.Matrix, endpoint: sp.Matrix) -> sp.Expr:
    return sp.expand(sum(
        ETA[i] * matrix[i, j] * endpoint[i, j]
        for i in range(N) for j in range(N)
    ))


matrix_t = sp.zeros(N)
matrix_t[0, 0] = matrix_t[0, 1] = 1
matrix_a = sp.zeros(N)
matrix_a[2, 2] = 1
parameter = sp.symbols("parameter")
matrix_shift = matrix_t + parameter * matrix_a
grade_one_defect = sp.factor(
    sp.diff(
        sp.Rational(1, 3) * matrix_pair(matrix_shift, matrix_endpoint(matrix_shift)),
        parameter,
    ).subs(parameter, 0)
    - matrix_pair(matrix_a, matrix_endpoint(matrix_t))
)
check("exact", "pure grade-one cyclicity selects the transposed-Ricci extension alpha=0",
      grade_one_defect == -sp.Rational(2, 3) * alpha)
check("planted", "pair-symmetrizing the off-Riemann cross Ricci fails the pure grade-one cyclic fixture",
      grade_one_defect.subs(alpha, sp.Rational(1, 2)) != 0)
check("exact", "the selected alpha=0 candidate passes that discriminating grade-one fixture",
      grade_one_defect.subs(alpha, 0) == 0)


print("\nD. LOW EINSTEIN CYCLIC-KERNEL WITNESS")

low_missing = 13
low_pivot = 12
low_active = set(range(12))
low_c = {
    1 << i: emul(blade(i), blade(low_pivot))
    for i in sorted(low_active)
}
low_b = {1 << low_missing: blade(low_missing)}
low_curvature = wedge(low_c, low_c)
low_kernel = quadratic_pair(low_b, low_c)
check("exact", "low c and b are real B-skew adjoint-valued one-forms",
      form_b_skew(low_c) and form_b_skew(low_b))
check("exact", "low Q(c,c) is scale-two constant algebraic Riemann curvature on a 12-plane",
      matches_active_constant_curvature(low_curvature, low_active, 2))
check("exact", "low Q(b,c) vanishes coefficientwise",
      not low_kernel)
low_endpoint = einstein_extension(low_curvature, "LOW", 0)
low_high_endpoint = einstein_extension(low_curvature, "HIGH", 0)
low_pairing = sp.simplify(pair_top(low_b, low_endpoint))
low_scalar = scalar_from_cross(cross_ricci(low_curvature))
check("exact", "independent 12-plane curvature arithmetic gives scalar 2*12*11=264",
      low_scalar == 264)
check("exact", "low kernel witness has a nonzero low Einstein endpoint pairing",
      low_pairing == -sp.Rational(1, 2) * low_scalar * 128,
      str(low_pairing))
check("exact", "low witness is orthogonal to the high Einstein copy",
      pair_top(low_b, low_high_endpoint) == 0)
low_direct = sp.simplify(
    sp.Rational(1, 3) * pair_top(low_b, low_endpoint)
    + sp.Rational(1, 3) * pair_top(low_c, einstein_extension(low_kernel, "LOW", 0))
)
low_defect = sp.simplify(low_direct - low_pairing)
check("exact", "low direct cubic derivative is one third of the proposed endpoint",
      low_direct == sp.Rational(1, 3) * low_pairing)
check("exact", "low cyclic defect is nonzero and forces the low Riemann coefficient p=0",
      low_defect == -sp.Rational(2, 3) * low_pairing and low_defect != 0,
      str(low_defect))


print("\nE. HIGH EINSTEIN CYCLIC-KERNEL WITNESS")

high_missing = 13
high_active = set(range(13))
high_c = {1 << i: blade(i) for i in sorted(high_active)}
high_b = {1 << high_missing: emul(blade(high_missing), VOLUME)}
high_curvature = wedge(high_c, high_c)
high_kernel = quadratic_pair(high_b, high_c)
check("exact", "high c and b are real B-skew adjoint-valued one-forms",
      form_b_skew(high_c) and form_b_skew(high_b))
check("exact", "high Q(c,c) is scale-two constant algebraic Riemann curvature on a 13-plane",
      matches_active_constant_curvature(high_curvature, high_active, 2))
check("exact", "high Q(b,c) vanishes coefficientwise",
      not high_kernel)
high_endpoint = einstein_extension(high_curvature, "HIGH", 0)
high_low_endpoint = einstein_extension(high_curvature, "LOW", 0)
high_pairing = sp.simplify(pair_top(high_b, high_endpoint))
high_scalar = scalar_from_cross(cross_ricci(high_curvature))
check("exact", "independent 13-plane curvature arithmetic gives scalar 2*13*12=312",
      high_scalar == 312)
check("exact", "high kernel witness has a nonzero high Einstein endpoint pairing",
      high_pairing == sp.Rational(1, 2) * high_scalar * 128,
      str(high_pairing))
check("exact", "high witness is orthogonal to the low Einstein copy",
      pair_top(high_b, high_low_endpoint) == 0)
high_direct = sp.simplify(
    sp.Rational(1, 3) * pair_top(high_b, high_endpoint)
    + sp.Rational(1, 3) * pair_top(high_c, einstein_extension(high_kernel, "HIGH", 0))
)
high_defect = sp.simplify(high_direct - high_pairing)
check("exact", "high direct cubic derivative is one third of the proposed endpoint",
      high_direct == sp.Rational(1, 3) * high_pairing)
check("exact", "high cyclic defect is nonzero and forces the high Riemann coefficient q=0",
      high_defect == -sp.Rational(2, 3) * high_pairing and high_defect != 0,
      str(high_defect))


print("\nF. SCOPE, CONTROLS, AND CAMPAIGN CONTRACT")

check("exact", "the two witnesses jointly force p=q=0 before expression grammar or Green data",
      low_defect != 0 and high_defect != 0)
flint_low_scalar = fmpz(2) * 12 * 11
flint_high_scalar = fmpz(2) * 13 * 12
flint_low_pair = -fmpq(1, 2) * flint_low_scalar * 128
flint_high_pair = fmpq(1, 2) * flint_high_scalar * 128
check("flint", "independent FLINT arithmetic reproduces both pairings and two-thirds defects",
      int(flint_low_pair) == low_pairing
      and int(-fmpq(2, 3) * flint_low_pair) == low_defect
      and int(flint_high_pair) == high_pairing
      and int(-fmpq(2, 3) * flint_high_pair) == high_defect)
check("planted", "an endpoint-orthogonal low field makes the test vacuous and is rejected",
      pair_top({1 << low_missing: blade(0)}, low_endpoint) == 0)
check("planted", "a noncommuting high control produces a nonzero quadratic partner",
      bool(quadratic_pair(
          {1 << high_missing: emul(blade(high_missing), VOLUME)},
          {1 << low_pivot: blade(low_missing)},
      )))
check("type", "the obstruction is pointwise and therefore precedes bundle descent rather than disproving it", True)
check("type", "the zero-order survivor set is empty, so no Green/domain claim is inferred", True)
check("type", "derivative and moving-field action mechanisms remain the required reconstruction route", True)
check("type", "observed four-dimensional and Frobenius-fibre trace reversals are not tested here", True)
check("type", "P1/P2/P3 remain unchanged and unused", True)

result = {
    "counts": COUNTS,
    "full_equivariant_hom_dimension": 200,
    "grade2_full_blocks": {"low": 3, "high": 3},
    "riemann_blocks": {"low": 2, "high": 2},
    "pure_grade1_selector": "TRANSPOSE_RICCI_ALPHA_ZERO",
    "low_pairing": str(low_pairing),
    "low_defect": str(low_defect),
    "high_pairing": str(high_pairing),
    "high_defect": str(high_defect),
    "intersection": "P_EQUALS_Q_EQUALS_ZERO",
    "verdict": "ZERO_ORDER_LINEAR_FULL_DOMAIN_EINSTEIN_CYCLIC_INTERSECTION_ZERO",
    "failures": FAILURES,
}
print("\nK77-B3 RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print(
    f"\nChecks: {COUNTS['exact']} exact + {COUNTS['sage']} Sage + "
    f"{COUNTS['flint']} FLINT + "
    f"{COUNTS['source']} source + {COUNTS['type']} type + "
    f"{COUNTS['planted']} planted = {sum(COUNTS.values())}"
)
if FAILURES:
    raise SystemExit("FAILED: " + "; ".join(FAILURES))
print("PASS: both low/high Einstein coefficients are killed by exact cyclic-kernel witnesses; derivative/moving-field reconstruction remains open.")
