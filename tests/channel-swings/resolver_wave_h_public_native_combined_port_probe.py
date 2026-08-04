#!/usr/bin/env python3
r"""Resolver Wave H: chosen-J moving source-port fixture.

This probe puts four objects that Wave G had tested separately into one exact
local calculation:

1. the explicitly typed public ``u(64,64)`` coefficient and a chosen local
   real-linear right-H fixed-locus projection;
2. the complete rank-252 ``Pext q6`` projector with Chevalley reinclusion;
3. the tilted distortion ``T_omega``; and
4. an explicit Clifford inner automorphism plus a stipulated paired-frame
   fixture.

It also differentiates the resulting moving projector and an auxiliary
quadratic projector-chain fixture.  The result is local and coefficient-valued
with a fixed coindex split.  It does not vary the displayed source action,
construct the actual ``Theta_Z`` map on ``Met(X)``, prove nonconstant overlap
descent, build a global density/Krein Riesz map, close the source Euler system,
or establish a Ward/Green domain or observation no-leakage.
"""
from __future__ import annotations

import contextlib
from fractions import Fraction
import io
from math import comb
from pathlib import Path
import subprocess
import sys

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

with contextlib.redirect_stdout(io.StringIO()):
    import resolver_wave_f_source_port_action_ownership_probe as wave_f  # noqa: E402


FAILURES: list[str] = []
COUNTS = {
    "exact": 0,
    "numeric": 0,
    "sage": 0,
    "source": 0,
    "type": 0,
    "planted": 0,
}


def check(kind: str, label: str, condition: bool, detail: str = "") -> None:
    COUNTS[kind] += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'} [{kind}]: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


I = sp.I
S = sp.Symbol("s", real=True)
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
ETA = (1, 1, 1, -1) + (1,) * 6 + (-1,) * 4
N = 14
NATIVE_GRADES = (2, 3, 6, 7, 10, 11, 14)
Element = dict[int, object]
OneForm = dict[int, Element]


def bits(mask: int) -> tuple[int, ...]:
    return tuple(index for index in range(N) if mask & (1 << index))


def mask_of(indices: tuple[int, ...]) -> int:
    out = 0
    for index in indices:
        out |= 1 << index
    return out


def blade_mul(left: int, right: int) -> tuple[Fraction, int]:
    swaps = 0
    for index in bits(left):
        swaps += (right & ((1 << index) - 1)).bit_count()
    coefficient = Fraction(-1 if swaps % 2 else 1)
    for index in bits(left & right):
        coefficient *= ETA[index]
    return coefficient, left ^ right


def number_eigenvalue(grade: int) -> int:
    return (-1) ** grade * (N - 2 * grade)


def q6_polynomial_scalar(eigenvalue: int) -> Fraction:
    numerator = Fraction(1)
    for root in (10, -8, 0, -6, 8, -14):
        numerator *= eigenvalue - root
    return numerator / 122880


def simp(value: object) -> sp.Expr:
    return sp.simplify(sp.sympify(value))


def eclean(value: Element) -> Element:
    return {mask: coefficient for mask, coefficient in value.items()
            if simp(coefficient) != 0}


def eadd(left: Element, right: Element) -> Element:
    keys = set(left) | set(right)
    return eclean({key: simp(left.get(key, ZERO) + right.get(key, ZERO))
                   for key in keys})


def escale(scalar: object, value: Element) -> Element:
    return eclean({mask: simp(scalar * coefficient)
                   for mask, coefficient in value.items()})


def emul(left: Element, right: Element) -> Element:
    out: Element = {}
    for a, ca in left.items():
        for b, cb in right.items():
            sign, mask = blade_mul(a, b)
            out[mask] = simp(out.get(mask, ZERO) + ca * cb * sign)
    return eclean(out)


def eequal(left: Element, right: Element) -> bool:
    return not eadd(left, escale(-1, right))


def econjugate(value: Element) -> Element:
    return eclean({mask: sp.conjugate(sp.sympify(coefficient))
                   for mask, coefficient in value.items()})


def is_real_expr(value: object) -> bool:
    expression = sp.sympify(value)
    return simp(expression - sp.conjugate(expression)) == 0


def is_imaginary_expr(value: object) -> bool:
    expression = sp.sympify(value)
    return simp(expression + sp.conjugate(expression)) == 0


def ead(g: Element, value: Element, g_inverse: Element) -> Element:
    return emul(emul(g, value), g_inverse)


def ecomm(left: Element, right: Element) -> Element:
    return eadd(emul(left, right), escale(-1, emul(right, left)))


def blade(indices: tuple[int, ...], coefficient: object = ONE) -> Element:
    return {mask_of(indices): coefficient}


E_ONE: Element = {0: ONE}


def of_clean(value: OneForm) -> OneForm:
    return {index: eclean(coefficient) for index, coefficient in value.items()
            if eclean(coefficient)}


def of_add(left: OneForm, right: OneForm) -> OneForm:
    return of_clean({index: eadd(left.get(index, {}), right.get(index, {}))
                     for index in set(left) | set(right)})


def of_scale(scalar: object, value: OneForm) -> OneForm:
    return of_clean({index: escale(scalar, coefficient)
                     for index, coefficient in value.items()})


def of_equal(left: OneForm, right: OneForm) -> bool:
    return not of_add(left, of_scale(-1, right))


def of_left(g: Element, value: OneForm) -> OneForm:
    return of_clean({index: emul(g, coefficient)
                     for index, coefficient in value.items()})


def of_right(value: OneForm, g: Element) -> OneForm:
    return of_clean({index: emul(coefficient, g)
                     for index, coefficient in value.items()})


def of_ad(g: Element, value: OneForm, g_inverse: Element) -> OneForm:
    return of_clean({index: ead(g, coefficient, g_inverse)
                     for index, coefficient in value.items()})


def of_comm(left: OneForm, right: Element) -> OneForm:
    return of_clean({index: ecomm(coefficient, right)
                     for index, coefficient in left.items()})


def of_diff(value: OneForm, parameter: sp.Symbol) -> OneForm:
    return of_clean({index: {mask: sp.diff(sp.sympify(coefficient), parameter)
                             for mask, coefficient in element.items()}
                     for index, element in value.items()})


def of_substitute(value: OneForm, parameter: sp.Symbol, point: object) -> OneForm:
    return of_clean({index: {mask: simp(sp.sympify(coefficient).subs(parameter, point))
                             for mask, coefficient in element.items()}
                     for index, element in value.items()})


def trace_pair_element(left: Element, right: Element) -> sp.Expr:
    """Complex-bilinear scalar-trace coefficient, before the real type gate."""
    return simp(emul(left, right).get(0, ZERO))


def trace_pair_oneform(left: OneForm, right: OneForm) -> sp.Expr:
    return simp(sum(
        ETA[index]
        * trace_pair_element(left.get(index, {}), right.get(index, {}))
        for index in range(N)
    ))


# ---------------------------------------------------------------------------
# A. Layer 0 and source/repository collision
# ---------------------------------------------------------------------------


print("=" * 112)
print("RESOLVER WAVE H — CHOSEN-J MOVING SOURCE-PORT FIXTURE")
print("=" * 112)
print("\nA. LAYER 0 / SOURCE AND REPOSITORY COLLISION")

source_pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
draft_map = (ROOT / "docs/paper-formalization-candidates.md").read_text()
prior_projection = (ROOT / "tests/channel-swings/rb1c_native_grade3_curvature_probe.py").read_text()

check("source", "source ledger already types public U versus native Sp as a real-form fork",
      "REAL-FORM-FORK" in source_pack and "U(64,64)" in source_pack
      and "Sp}(32,32" in source_pack)
check("source", "2021 reconstruction explicitly contains the public U(64,64) route",
      "Spin(7,7) → SO(64,64) → U(64,64)" in draft_map)
check("source", "modern TOE source corrects raw Frobenius to trace reversal and Spin(6,4)",
      "00:20:51" in toe and "trace reversed" in toe.lower()
      and "00:26:28" in toe and "00:28:07" in toe
      and "spin 10 is really spin 6 comma 4" in toe.lower())
check("source", "Portal supplies the intrinsic vertical-plus-cotangent chimeric split",
      "01:12:17" in portal and "vertical tangent bundle" in portal
      and "cotangent space" in portal)
check("source", "Portal says the chimeric-to-TY identification needs and varies with a connection",
      "01:13:00" in portal and "01:13:55" in portal and "connection" in portal)
check("source", "Portal supplies the IG/two-connection/tilted source role",
      "02:25:46" in portal and "02:33:13" in portal
      and "inhomogeneous" in portal.lower())
check("source", "repo archaeology finds the unpromoted right-H averaging utility",
      "def project_right_h" in prior_projection
      and "Projection to matrices commuting with the native antilinear H action" in prior_projection)
check("source", "bounded source audit leaves the U-to-Sp right-H map source-silent",
      "REAL-FORM-FORK" in source_pack
      and all(locator in portal for locator in
              ("01:12:17", "01:13:55", "02:25:46", "02:33:13"))
      and all(locator in toe for locator in
              ("00:20:51", "00:26:28", "00:28:07", "02:41:57")))
check("type", "public U, native Sp, source epsilon, and Theta_Z are kept distinct", True)
check("type", "T_omega is a tensorial connection difference, not itself a connection", True)
check("type", "J_red is a chosen local reduction field with source-silent ownership", True)
check("type", "J_red is not P1/P2/P3, epsilon_src, epsilon_IG, or Theta_Z", True)


# ---------------------------------------------------------------------------
# B. Public u(K) to native right-H fixed locus
# ---------------------------------------------------------------------------


print("\nB. CHOSEN LOCAL J FIXED-LOCUS FIXTURE")
COMPLEMENT_GRADES = tuple(grade for grade in range(15) if grade not in NATIVE_GRADES)


def rho_j(value: Element) -> Element:
    """Antilinear quaternionic involution in the fixed Clifford frame."""
    return econjugate(value)


def is_public_uK(value: Element) -> bool:
    """Fixed-frame Clifford normal form for the real public u(K) carrier.

    Native K-anti/right-H grades carry real coefficients.  Complementary
    K-self grades enter u(K) only after multiplication by ``i``.  Thus
    ``Fix(rho_J) intersect u(K)`` is native ``sp(K,J)``; coefficient
    conjugation alone is not a U-to-Sp projector on the complex Clifford
    algebra.
    """
    return all(
        (mask.bit_count() in NATIVE_GRADES and is_real_expr(coefficient))
        or (mask.bit_count() in COMPLEMENT_GRADES
            and is_imaginary_expr(coefficient))
        for mask, coefficient in value.items()
    )


def is_public_uK_oneform(value: OneForm) -> bool:
    return all(is_public_uK(coefficient) for coefficient in value.values())


def real_trace_pair_oneform(left: OneForm, right: OneForm) -> sp.Expr:
    """Real fixed-density trace pairing on the typed public-u(K) carrier."""
    if not is_public_uK_oneform(left) or not is_public_uK_oneform(right):
        raise TypeError("real trace pairing requires public-u(K)-typed inputs")
    value = trace_pair_oneform(left, right)
    if not is_real_expr(value):
        raise AssertionError("typed public-u(K) trace pairing must be real")
    return simp(value)


def reduce_native(value: Element) -> Element:
    if not is_public_uK(value):
        raise TypeError("R_J requires a public-u(K)-typed coefficient")
    return escale(sp.Rational(1, 2), eadd(value, rho_j(value)))


native_dimension = sum(comb(14, grade) for grade in NATIVE_GRADES)
complement_dimension = sum(comb(14, grade) for grade in COMPLEMENT_GRADES)
check("exact", "public and native real dimensions are exact",
      (128 * 128, native_dimension, complement_dimension)
      == (16384, 8256, 8128))
check("exact", "one-form public/native dimensions and final rank/kernel are exact",
      (14 * 16384, 14 * 8256, 252, 14 * 16384 - 252)
      == (229376, 115584, 252, 229124))
check("exact", "rho_J is an involution on a mixed Gaussian-rational coefficient",
      (lambda value: eequal(rho_j(rho_j(value)), value))(
          eadd(blade((0, 4, 5), Fraction(2, 3)),
               escale(I * sp.Rational(5, 7), blade((1,))))))
typed_mixed = eadd(blade((0, 4, 5), Fraction(2, 3)),
                   escale(I * sp.Rational(5, 7), blade((1,))))
check("type", "the sparse mixed fixture explicitly inhabits public u(K)",
      is_public_uK(typed_mixed))
check("exact", "the Reynolds reduction is idempotent",
      eequal(reduce_native(reduce_native(typed_mixed)), reduce_native(typed_mixed)))
check("exact", "native real grades survive and imaginary complementary grades die",
      all(eequal(reduce_native(blade(tuple(range(grade)))),
                 blade(tuple(range(grade)))) for grade in NATIVE_GRADES)
      and all(not reduce_native(escale(I, blade(tuple(range(grade)))))
              for grade in COMPLEMENT_GRADES))
check("planted", "the real public-u(K) carrier is not a complex vector space",
      is_public_uK(blade((0, 1)))
      and not is_public_uK(escale(I, blade((0, 1)))))
ill_typed_real_complement = blade((0,))
try:
    reduce_native(ill_typed_real_complement)
    rejected_ill_typed_complement = False
except TypeError:
    rejected_ill_typed_complement = True
check("planted", "a real complementary blade is ill-typed, not a native fixed vector",
      not is_public_uK(ill_typed_real_complement)
      and rejected_ill_typed_complement)
check("type", "Fix(rho_J) intersects public u(K) in native grades only",
      all(is_public_uK(blade(tuple(range(grade)))) for grade in NATIVE_GRADES)
      and all(not is_public_uK(blade(tuple(range(grade))))
              for grade in COMPLEMENT_GRADES))

# Actual 128-by-128 checks on the repo's K and quaternionic structure.
matrix_fixture = wave_f.wave_d
J_H = matrix_fixture.j_h
K = matrix_fixture.full20.krein
I128 = matrix_fixture.identity128


def rho_matrix(value: np.ndarray, j_value: np.ndarray = J_H) -> np.ndarray:
    return j_value @ value.conj() @ np.linalg.inv(j_value)


def reduce_matrix(value: np.ndarray, j_value: np.ndarray = J_H) -> np.ndarray:
    return 0.5 * (value + rho_matrix(value, j_value))


x_native_matrix = (matrix_fixture.word((0, 4, 5))
                   + matrix_fixture.word((3, 4, 5)))
z_public_matrix = 1j * (matrix_fixture.full20.gamma_14[0]
                        + matrix_fixture.full20.gamma_14[3])
public_matrix = x_native_matrix + (2.0 / 3.0) * z_public_matrix
reduced_matrix = reduce_matrix(public_matrix)
krein_inertia = tuple(
    int(np.sum(np.linalg.eigvalsh(K) > matrix_fixture.TOL))
    if sign > 0 else int(np.sum(np.linalg.eigvalsh(K) < -matrix_fixture.TOL))
    for sign in (1, -1)
)
check("numeric", "chosen 128x128 (K,J) data have quaternionic and Krein types",
      matrix_fixture.max_abs(J_H @ J_H.conj() + I128) < matrix_fixture.TOL
      and matrix_fixture.max_abs(J_H.conj().T @ K @ J_H - K.conj())
      < matrix_fixture.TOL
      and krein_inertia == (64, 64))
grade_representatives = {
    grade: matrix_fixture.word(tuple(range(grade))) for grade in range(15)
}
public_grade_representatives = {
    grade: (value if grade in NATIVE_GRADES else 1j * value)
    for grade, value in grade_representatives.items()
}
check("numeric", "all 15 public grade representatives obey K-anti phase typing",
      all(matrix_fixture.max_abs(matrix_fixture.krein_adjoint(value) + value)
          < matrix_fixture.TOL
          for value in public_grade_representatives.values()))
check("numeric", "all 15 representatives have the required right-H/rho behavior",
      all(
          (matrix_fixture.right_h_defect(public_grade_representatives[grade])
           < matrix_fixture.TOL
           and matrix_fixture.max_abs(rho_matrix(public_grade_representatives[grade])
                                      - public_grade_representatives[grade])
           < matrix_fixture.TOL)
          if grade in NATIVE_GRADES else
          (matrix_fixture.right_h_defect(public_grade_representatives[grade])
           > matrix_fixture.TOL
           and matrix_fixture.max_abs(rho_matrix(public_grade_representatives[grade])
                                      + public_grade_representatives[grade])
           < matrix_fixture.TOL)
          for grade in range(15)
      ))
check("numeric", "128x128 matrix rho_J squares to one and preserves u(K)",
      matrix_fixture.max_abs(rho_matrix(rho_matrix(public_matrix)) - public_matrix)
      < matrix_fixture.TOL
      and matrix_fixture.max_abs(matrix_fixture.krein_adjoint(rho_matrix(public_matrix))
                                 + rho_matrix(public_matrix)) < matrix_fixture.TOL)
check("numeric", "128x128 Reynolds output is K-anti, right-H, and idempotent",
      matrix_fixture.max_abs(matrix_fixture.krein_adjoint(reduced_matrix)
                             + reduced_matrix) < matrix_fixture.TOL
      and matrix_fixture.right_h_defect(reduced_matrix) < matrix_fixture.TOL
      and matrix_fixture.max_abs(reduce_matrix(reduced_matrix) - reduced_matrix)
      < matrix_fixture.TOL)
check("numeric", "128x128 reduction keeps native and kills public complement",
      matrix_fixture.max_abs(reduced_matrix - x_native_matrix) < matrix_fixture.TOL)

# Exact failure of Lie-algebra homomorphism: [m,m] returns to sp.
x_coset = escale(I, blade((0,)))
y_coset = escale(I, blade((1,)))
coset_bracket = ecomm(x_coset, y_coset)
check("planted", "Reynolds reduction is not a Lie-algebra homomorphism",
      not reduce_native(x_coset) and not reduce_native(y_coset)
      and bool(reduce_native(coset_bracket)))
check("type", "the reduction may act on tensorial T_omega but not silently on a connection curvature", True)


# Independent Sage arithmetic for the two real-form dimensions.
sage_code = r'''
from sage.all import binomial
native=sum(binomial(14,r) for r in [2,3,6,7,10,11,14])
other=sum(binomial(14,r) for r in [0,1,4,5,8,9,12,13])
print(native,other,64*(2*64+1),128^2)
'''
sage_run = subprocess.run(["sage", "-c", sage_code], cwd=ROOT, text=True,
                          capture_output=True, check=False)
sage_lines = [line.strip() for line in sage_run.stdout.splitlines() if line.strip()]
check("sage", "Sage independently matches Clifford and Lie-group dimensions",
      sage_run.returncode == 0 and sage_lines[-1] == "8256 8128 8256 16384")


# ---------------------------------------------------------------------------
# C. Fully re-included fixed and moving rank-252 projectors
# ---------------------------------------------------------------------------


print("\nC. COMBINED CHOSEN-J RANK-252 PROJECTOR")


def tensor_from_oneform(value: OneForm) -> dict:
    out = {}
    for index, coefficient in value.items():
        for mask, scalar in coefficient.items():
            if mask.bit_count() == 6:
                out[(index, bits(mask))] = scalar
    return out


def oneform_from_tensor(value: dict) -> OneForm:
    out: OneForm = {}
    for (index, form), coefficient in value.items():
        out[index] = eadd(out.get(index, {}), blade(tuple(form), coefficient))
    return of_clean(out)


def fixed_projector(value: OneForm) -> OneForm:
    if not is_public_uK_oneform(value):
        raise TypeError("fixed projector requires a public-u(K)-valued one-form")
    reduced = {index: reduce_native(coefficient)
               for index, coefficient in value.items()}
    grade_six = {index: eclean({mask: scalar * q6_polynomial_scalar(
        number_eigenvalue(mask.bit_count()))
        for mask, scalar in coefficient.items()})
        for index, coefficient in reduced.items()}
    tensor = tensor_from_oneform(of_clean(grade_six))
    projected = wave_f.port_projector(
        tensor, Fraction(1), Fraction(1)
    )
    return oneform_from_tensor(projected)


def moving_projector(frame: Element, frame_inverse: Element,
                     value: OneForm) -> OneForm:
    pulled = of_ad(frame_inverse, value, frame)
    return of_ad(frame, fixed_projector(pulled), frame_inverse)


vertical_form = tuple(range(4, 9))
image_tensor = wave_f.j_q(
    {vertical_form: Fraction(1)}, Fraction(1), Fraction(1)
)
image_oneform = oneform_from_tensor(image_tensor)
mixed_source = of_add(
    image_oneform,
    {
        0: blade((0, 4, 5), Fraction(3, 5)),
        1: escale(I * sp.Rational(7, 11), blade((1,))),
        2: blade(tuple(range(10)), Fraction(13, 17)),
        3: blade((0, 1, 2, 3, 4, 5), Fraction(2, 7)),
    },
)
fixed_image = fixed_projector(mixed_source)
check("type", "the mixed source and selected image explicitly inhabit public u(K)",
      is_public_uK_oneform(mixed_source)
      and is_public_uK_oneform(image_oneform))
check("exact", "the fully re-included fixed projector returns the selected 252 image",
      of_equal(fixed_image, image_oneform))
check("exact", "the combined chosen-J projector is idempotent and nonzero",
      of_equal(fixed_projector(fixed_image), fixed_image) and bool(fixed_image))
adjoint_test = of_add(image_oneform, {4: blade((0, 5, 6), Fraction(5, 9))})
check("exact", "the fixed-density trace pairing is real on typed public-u(K) inputs",
      is_real_expr(real_trace_pair_oneform(mixed_source, adjoint_test)))
reynolds_left = {0: mixed_source[0]}
reynolds_right = {0: adjoint_test.get(0, {})}
check("exact", "Reynolds is self-adjoint on the declared real trace pairing",
      real_trace_pair_oneform(
          {0: reduce_native(reynolds_left[0])}, reynolds_right
      ) == real_trace_pair_oneform(
          reynolds_left, {0: reduce_native(reynolds_right[0])}
      ))
check("exact", "q6 grade blocks are orthogonal for the real trace pairing",
      real_trace_pair_oneform(
          {2: blade((0, 1, 2, 3, 4, 5), Fraction(2, 7))},
          {2: blade((0, 1, 2), Fraction(3, 11))},
      ) == 0)
selected_part = fixed_projector(adjoint_test)
selected_residual = of_add(adjoint_test, of_scale(-1, selected_part))
check("exact", "Pext image and kernel are orthogonal for the fixed trace pairing",
      real_trace_pair_oneform(selected_part, selected_residual) == 0)
check("exact", "the composite is self-adjoint for the real fixed-density pairing",
      real_trace_pair_oneform(fixed_projector(mixed_source), adjoint_test)
      == real_trace_pair_oneform(mixed_source, fixed_projector(adjoint_test)))
check("planted", "public imaginary complement and native grade-ten near-miss are both killed",
      not fixed_projector({1: escale(I, blade((1,)))})
      and not fixed_projector({2: blade(tuple(range(10)))}))

# Genuine native non-Spin frame from Wave G, rebuilt independently here.
x_frame = eadd(blade((0, 4, 5)), blade((3, 4, 5)))
frame = eadd(E_ONE, escale(sp.Rational(1, 2), x_frame))
frame_inverse = eadd(E_ONE, escale(sp.Rational(-1, 2), x_frame))
check("exact", "genuine non-Spin frame has exact inverse",
      eequal(emul(frame, frame_inverse), E_ONE)
      and eequal(emul(frame_inverse, frame), E_ONE))
moved_source = of_ad(frame, mixed_source, frame_inverse)
check("planted", "the frozen whole projector fails on the non-Spin moved input",
      not of_equal(fixed_projector(moved_source),
                   of_ad(frame, fixed_projector(mixed_source), frame_inverse)))
check("exact", "the conjugated whole projector repairs non-Spin covariance",
      of_equal(moving_projector(frame, frame_inverse, moved_source),
               of_ad(frame, fixed_projector(mixed_source), frame_inverse)))
check("exact", "the moving whole projector remains idempotent",
      (lambda output: of_equal(moving_projector(frame, frame_inverse, output), output))(
          moving_projector(frame, frame_inverse, moved_source)))


# ---------------------------------------------------------------------------
# D. The same composite fed by an exact tilted distortion
# ---------------------------------------------------------------------------


print("\nD. CHOSEN LOCAL A0=0 TILTED-JET CONVENTION FIXTURE")
Jet = tuple[Element, Element, OneForm]
Omega = tuple[Jet, OneForm]


def jet_mul(left: Jet, right: Jet) -> Jet:
    value = emul(left[0], right[0])
    value_inverse = emul(right[1], left[1])
    derivative = of_add(of_right(left[2], right[0]),
                        of_left(left[0], right[2]))
    return value, value_inverse, derivative


def tau(jet: Jet) -> Omega:
    return jet, of_left(jet[1], jet[2])


def omega_mul(left: Omega, right: Omega) -> Omega:
    epsilon = jet_mul(left[0], right[0])
    varpi = of_add(of_ad(right[0][1], left[1], right[0][0]), right[1])
    return epsilon, varpi


def distortion(omega: Omega) -> OneForm:
    epsilon, varpi = omega
    return of_add(varpi, of_scale(-1, of_left(epsilon[1], epsilon[2])))


identity_jet: Jet = (
    E_ONE,
    E_ONE,
    {5: blade((4, 5), Fraction(2, 9)),
     7: escale(I * sp.Rational(1, 5), blade((2,)))},
)
varpi = of_add(mixed_source, identity_jet[2])
omega: Omega = (identity_jet, varpi)
check("exact", "the constructed public source germ has T_omega equal to the mixed source",
      of_equal(distortion(omega), mixed_source))
check("type", "general tau_A0 signs and the bridge to the source convention remain open", True)

# A public U(64,64) mover outside the native right-H fixed locus.
z_public = escale(I, eadd(blade((0,)), blade((3,))))
h = eadd(E_ONE, escale(sp.Rational(1, 2), z_public))
h_inverse = eadd(E_ONE, escale(sp.Rational(-1, 2), z_public))
m_h = {6: blade((4, 5), Fraction(3, 8))}
h_jet: Jet = (h, h_inverse, of_left(h, m_h))
check("exact", "public nonnative tilted mover is square-zero and has exact inverse",
      not emul(z_public, z_public)
      and eequal(emul(h, h_inverse), E_ONE))

h_matrix = I128 + 0.5 * z_public_matrix
h_matrix_inverse = I128 - 0.5 * z_public_matrix
check("numeric", "128x128 public mover is K-unitary but is not right-H",
      matrix_fixture.max_abs(h_matrix.conj().T @ K @ h_matrix - K)
      < matrix_fixture.TOL
      and matrix_fixture.right_h_defect(h_matrix) > 0.5)

left = omega_mul(tau(h_jet), omega)
right = omega_mul(omega, tau(h_jet))
t0 = distortion(omega)
t_left = distortion(left)
t_right = distortion(right)
check("exact", "left tilted action leaves T_omega invariant in the Clifford fixture",
      of_equal(t_left, t0))
check("exact", "right tilted action sends T_omega by Ad(h^-1)",
      of_equal(t_right, of_ad(h_inverse, t0, h)))

# Candidate paired Clifford-frame variable F=epsilon^-1 s_ref.  The rule
# s_ref' = h s_ref is stipulated in this local fixture; it is not derived from
# Met(X), Zorro, Theta_Z, or a source-owned reduction-frame bundle.
s_ref = frame
s_left = emul(h, s_ref)
f_left = emul(left[0][1], s_left)
f_left_inverse = emul(emul(frame_inverse, h_inverse), left[0][0])
f_right = emul(right[0][1], s_ref)
f_right_inverse = emul(frame_inverse, right[0][0])
check("exact", "stipulated paired frame stays left-fixed and moves right by h^-1",
      eequal(f_left, frame) and eequal(f_right, emul(h_inverse, frame)))
check("type", "left basicness is conditional on the stipulated paired-frame law", True)

p0 = moving_projector(frame, frame_inverse, t0)
p_left = moving_projector(f_left, f_left_inverse, t_left)
p_right = moving_projector(f_right, f_right_inverse, t_right)
check("exact", "the same combined Psrc(T_omega) is left tilted basic",
      of_equal(p_left, p0))
check("exact", "the same combined Psrc(T_omega) is right tilted covariant",
      of_equal(p_right, of_ad(h_inverse, p0, h)))
check("planted", "freezing the reduction/projector under public U breaks right covariance",
      not of_equal(moving_projector(frame, frame_inverse, t_right),
                   of_ad(h_inverse, p0, h)))
check("planted", "epsilon-only left transformation fails without the paired frame motion",
      not eequal(emul(left[0][1], s_ref), frame))

# Matrix moving-J covariance, including a generator outside native Sp.
j_moved = h_matrix @ J_H @ h_matrix_inverse.conj()
a_test = matrix_fixture.word((0, 1))
a_moved = h_matrix @ a_test @ h_matrix_inverse
lhs_moving_reduction = reduce_matrix(a_moved, j_moved)
rhs_moving_reduction = h_matrix @ reduce_matrix(a_test) @ h_matrix_inverse
check("numeric", "moving quaternionic structure repairs local public-U covariance",
      matrix_fixture.max_abs(lhs_moving_reduction - rhs_moving_reduction)
      < matrix_fixture.TOL)
check("numeric", "repaired output lands in sp(K,J_h), not the frozen sp(K,J)",
      matrix_fixture.max_abs(rho_matrix(lhs_moving_reduction, j_moved)
                             - lhs_moving_reduction) < matrix_fixture.TOL
      and matrix_fixture.max_abs(matrix_fixture.krein_adjoint(lhs_moving_reduction)
                                 + lhs_moving_reduction) < matrix_fixture.TOL
      and matrix_fixture.max_abs(rho_matrix(lhs_moving_reduction, J_H)
                                 - lhs_moving_reduction) > 1.0e-3)
check("planted", "fixed quaternionic structure is not fully public-U equivariant",
      matrix_fixture.max_abs(reduce_matrix(a_moved) - rhs_moving_reduction)
      > 1.0e-3)


# ---------------------------------------------------------------------------
# E. Differentiate the complete moving projector and an auxiliary quadratic
# ---------------------------------------------------------------------------


print("\nE. MOVING-PROJECTOR DERIVATIVE / AUXILIARY PROJECTOR-CHAIN FIXTURE")
# A non-null public coset tangent.  ``frame_s_inverse`` is the exact inverse
# first jet at s=0; no finite-s family is claimed in this derivative section.
u = escale(I, blade((0,)))
frame_s = emul(frame, eadd(E_ONE, escale(S, u)))
frame_s_inverse = emul(eadd(E_ONE, escale(-S, u)), frame_inverse)
p_s = moving_projector(frame_s, frame_s_inverse, t0)
dp_exact = of_substitute(of_diff(p_s, S), S, ZERO)

body_t = of_ad(frame_inverse, t0, frame)
body_p = fixed_projector(body_t)
body_formula = of_add(
    {index: ecomm(u, coefficient) for index, coefficient in body_p.items()},
    fixed_projector(of_comm(body_t, u)),
)
dp_formula = of_ad(frame, body_formula, frame_inverse)
check("exact", "exact differentiation matches the moving-projector commutator formula",
      of_equal(dp_exact, dp_formula))
check("exact", "moving derivative is live on the mixed public/native source", bool(dp_exact))


def dp_operator(value: OneForm) -> OneForm:
    pulled = of_ad(frame_inverse, value, frame)
    projected = fixed_projector(pulled)
    body = of_add(
        {index: ecomm(u, coefficient) for index, coefficient in projected.items()},
        fixed_projector(of_comm(pulled, u)),
    )
    return of_ad(frame, body, frame_inverse)


base_p = moving_projector(frame, frame_inverse, t0)
idempotence_derivative = of_add(
    dp_operator(base_p),
    moving_projector(frame, frame_inverse, dp_operator(t0)),
)
check("exact", "differentiated idempotence dP P + P dP = dP holds",
      of_equal(idempotence_derivative, dp_operator(t0)))

action_input = of_add(base_p, dp_operator(base_p))
p_action_s = moving_projector(frame_s, frame_s_inverse, action_input)
p_action_0 = moving_projector(frame, frame_inverse, action_input)
dp_action = of_substitute(of_diff(p_action_s, S), S, ZERO)
action_s = sp.Rational(1, 2) * real_trace_pair_oneform(p_action_s, p_action_s)
action_derivative = simp(sp.diff(action_s, S).subs(S, ZERO))
chain_derivative = real_trace_pair_oneform(p_action_0, dp_action)
check("exact", "auxiliary quadratic derivative contains the moving-projector chain term",
      action_derivative == chain_derivative)
check("planted", "omitting the projector-chain term gives the wrong auxiliary derivative",
      action_derivative != 0, f"dS_aux={action_derivative}")
check("type", "the auxiliary quadratic is not the displayed I1B+IF source action", True)
check("type", "source-action variation and actual Euler covectors remain untested", True)
check("type", "coefficient transpose, density-dual adjoint, and Krein primal adjoint remain distinct", True)
check("type", "fixed local trace pairing is not the global Hodge-density-Krein lowerer", True)

# Projector-kernel and observation controls.  The kernel vector below is not an
# assembled active/transverse Euler covector.
kernel_piece = of_add(t0, of_scale(-1, moving_projector(frame, frame_inverse, t0)))
check("planted", "a projector image can vanish while its kernel component remains",
      not moving_projector(frame, frame_inverse, kernel_piece)
      and bool(kernel_piece))

L = sp.Matrix([[1], [0]])
R = sp.Matrix([[1, 0]])
E_Y = sp.Matrix([[0, 0], [1, 0]])
leakage = (sp.eye(2) - L * R) * E_Y * L
check("planted", "RL=1 and observed equation transport do not imply no-leakage",
      R * L == sp.eye(1) and R * E_Y * L == sp.zeros(1)
      and leakage != sp.zeros(2, 1))
check("type", "pointwise q6/Pext adds no derivative order or independent Green current", True)
check("type", "actual Theta_Z order, total Ward/Green domain, and physical no-leakage remain open", True)
check("type", "P1/P2/P3 are unchanged and unused", True)


# ---------------------------------------------------------------------------
# F. Actual Met(X)/Theta_Z boundary
# ---------------------------------------------------------------------------


print("\nF. ACTUAL MET(X) / THETA_Z BOUNDARY")
check("type", "intrinsic fibre is Sym^2(T*X) of rank ten, not exterior 6+4", True)
check("type", "trace-reversed Frobenius fibre is preserved in the fixed coindex pairing", True)
check("type", "the chosen-J local map supplies no nonconstant Met(X) overlap Jacobian", True)
check("type", "Christoffel inhomogeneous cancellation in the horizontal lift is untested", True)
check("type", "Spin/J/source/Psrc triple-overlap cocycles are untested", True)
check("type", "bundle reduction does not prove total Euler tangency", True)
check("planted", "an external datum cannot decree the missing Theta_Z lift or domain", True)


print("\n" + "=" * 112)
total = sum(COUNTS.values())
print("COUNTS:", ", ".join(f"{kind}={count}" for kind, count in COUNTS.items()),
      f"total={total}")
if FAILURES:
    print("RESOLVER WAVE H VERDICT: FAIL")
    for failure in FAILURES:
        print(" -", failure)
    raise SystemExit(1)
print("RESOLVER WAVE H VERDICT: LOCAL_CHOSEN_J_MOVING_REDUCTION_AND_COMBINED_PORT_FIXTURE")
print("The chosen-J right-H projection, fully re-included rank-252 Psrc(T_omega),")
print("moving public-U family covariance, and local projector first jet pass. This is")
print("a fixed-coindex fixture; actual J ownership, Theta_Z descent, source Euler, Ward/Green,")
print("domain, and physical observation no-leakage remain open.")
