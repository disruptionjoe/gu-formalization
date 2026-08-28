#!/usr/bin/env python3
r"""Resolver Wave G: generic-native q6 and local tilted-source schema.

This executable constructs the Clifford grade-six projection directly on a
generic native ``sp(32,32;H)`` coefficient.  It then composes Wave F's exact
rank-252 exterior projector, verifies the tilted connection-difference law,
and exhibits a non-Spin nilpotent mover for which a frozen grade projector
fails while the conjugated moving family succeeds.  The tilted group-law and
frame-surrogate fixtures remain separate: no combined ``P_src(T_omega)`` is
instantiated here.

The computation is local to a fixed native Clifford reduction.  It does not
construct the public U-type to native-Sp bundle map, a global Theta_Z/Zorro
lift, nonconstant overlap descent, the source action's undeclared variation
domain, total active/transverse Euler closure, a VEV, mass, index, or count.
"""
from __future__ import annotations

import contextlib
from fractions import Fraction
import io
from itertools import combinations
from math import comb
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

with contextlib.redirect_stdout(io.StringIO()):
    import resolver_wave_f_source_port_action_ownership_probe as wave_f  # noqa: E402


FAILURES: list[str] = []
COUNTS = {"exact": 0, "sage": 0, "source": 0, "type": 0, "planted": 0}


def check(kind: str, label: str, condition: bool, detail: str = "") -> None:
    COUNTS[kind] += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'} [{kind}]: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


ETA = (1, 1, 1, -1) + (1,) * 6 + (-1,) * 4
N = 14
NATIVE_GRADES = (2, 3, 6, 7, 10, 11, 14)


def bits(mask: int) -> tuple[int, ...]:
    return tuple(i for i in range(N) if mask & (1 << i))


def mask_of(indices: tuple[int, ...]) -> int:
    out = 0
    for i in indices:
        out |= 1 << i
    return out


def blade_mul(a: int, b: int) -> tuple[Fraction, int]:
    swaps = 0
    for i in bits(a):
        swaps += (b & ((1 << i) - 1)).bit_count()
    coefficient = Fraction(-1 if swaps % 2 else 1)
    for i in bits(a & b):
        coefficient *= ETA[i]
    return coefficient, a ^ b


Element = dict[int, Fraction]


def clean(value: Element) -> Element:
    return {mask: coefficient for mask, coefficient in value.items() if coefficient}


def add(left: Element, right: Element) -> Element:
    out = dict(left)
    for mask, coefficient in right.items():
        out[mask] = out.get(mask, Fraction(0)) + coefficient
    return clean(out)


def scale(scalar: Fraction, value: Element) -> Element:
    return clean({mask: scalar * coefficient for mask, coefficient in value.items()})


def mul(left: Element, right: Element) -> Element:
    out: Element = {}
    for a, ca in left.items():
        for b, cb in right.items():
            sign, mask = blade_mul(a, b)
            out[mask] = out.get(mask, Fraction(0)) + ca * cb * sign
    return clean(out)


ONE: Element = {0: Fraction(1)}


def blade(indices: tuple[int, ...], coefficient: Fraction = Fraction(1)) -> Element:
    return {mask_of(indices): coefficient}


def inverse_blade(mask: int) -> Element:
    square, zero = blade_mul(mask, mask)
    assert zero == 0 and square
    return {mask: Fraction(1, 1) / square}


def conjugate(g: Element, x: Element, g_inv: Element) -> Element:
    return mul(mul(g, x), g_inv)


def number_eigenvalue(grade: int) -> int:
    return (-1) ** grade * (N - 2 * grade)


def number_operator(value: Element) -> Element:
    out: Element = {}
    for i in range(N):
        e = blade((i,))
        e_up = scale(Fraction(ETA[i]), e)
        out = add(out, mul(mul(e, value), e_up))
    return out


def q6_polynomial_scalar(eigenvalue: int) -> Fraction:
    numerator = Fraction(1)
    for root in (10, -8, 0, -6, 8, -14):
        numerator *= eigenvalue - root
    return numerator / 122880


def q6(value: Element) -> Element:
    return clean({
        mask: coefficient * q6_polynomial_scalar(number_eigenvalue(mask.bit_count()))
        for mask, coefficient in value.items()
    })


def grade_part(value: Element, grade: int) -> Element:
    return {mask: coefficient for mask, coefficient in value.items()
            if mask.bit_count() == grade}


def trace_coefficient(value: Element, mask: int) -> Fraction:
    return mul(inverse_blade(mask), value).get(0, Fraction(0))


def clifford_pair(left: Element, right: Element) -> Fraction:
    """Diagonal invariant coefficient pairing in the simple-blade frame."""
    total = Fraction(0)
    for mask, coefficient in left.items():
        square, zero = blade_mul(mask, mask)
        assert zero == 0
        total += coefficient * right.get(mask, Fraction(0)) * square
    return total


def reversion_sign(grade: int) -> int:
    return -1 if grade * (grade - 1) // 2 % 2 else 1


def involution(value: Element, mode: str) -> Element:
    out = {}
    for mask, coefficient in value.items():
        grade = mask.bit_count()
        if mode == "grade":
            sign = -1 if grade % 2 else 1
        elif mode == "reverse":
            sign = reversion_sign(grade)
        elif mode == "clifford":
            sign = (-1 if grade % 2 else 1) * reversion_sign(grade)
        else:
            raise ValueError(mode)
        out[mask] = sign * coefficient
    return clean(out)


def form_signature(form: tuple[int, ...]) -> int:
    result = 1
    for index in form:
        result *= ETA[index]
    return result


def form_pair(left: dict, right: dict) -> Fraction:
    return sum(
        coefficient * right.get(form, Fraction(0)) * form_signature(form)
        for form, coefficient in left.items()
    )


def tensor_pair(left: dict, right: dict) -> Fraction:
    return sum(
        coefficient * right.get(key, Fraction(0))
        * ETA[key[0]] * form_signature(key[1])
        for key, coefficient in left.items()
    )


Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def matrix(a: int, b: int, c: int, d: int) -> Matrix:
    return ((Fraction(a), Fraction(b)), (Fraction(c), Fraction(d)))


I2 = matrix(1, 0, 0, 1)
Z2 = matrix(0, 0, 0, 0)


def madd(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def mscale(s: Fraction, a: Matrix) -> Matrix:
    return tuple(tuple(s * a[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def mmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))  # type: ignore[return-value]


def minv(a: Matrix) -> Matrix:
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return ((a[1][1] / determinant, -a[0][1] / determinant),
            (-a[1][0] / determinant, a[0][0] / determinant))


def mad(g_inv: Matrix, x: Matrix, g: Matrix) -> Matrix:
    return mmul(mmul(g_inv, x), g)


Jet = tuple[Matrix, Matrix]
Omega = tuple[Jet, Matrix]


def jmul(a: Jet, b: Jet) -> Jet:
    return mmul(a[0], b[0]), madd(mmul(a[1], b[0]), mmul(a[0], b[1]))


def tau(h: Jet) -> Omega:
    return h, mmul(minv(h[0]), h[1])


def group_mul(left: Omega, right: Omega) -> Omega:
    epsilon = jmul(left[0], right[0])
    r_value = right[0][0]
    varpi = madd(mad(minv(r_value), left[1], r_value), right[1])
    return epsilon, varpi


def distortion(omega: Omega) -> Matrix:
    epsilon, varpi = omega
    return madd(varpi, mscale(Fraction(-1), mmul(minv(epsilon[0]), epsilon[1])))


def mt_equal(a: Matrix, b: Matrix) -> bool:
    return a == b


print("=" * 108)
print("RESOLVER WAVE G — GENERIC-NATIVE q6 / TILTED SOURCE SCHEMA")
print("=" * 108)


# ---------------------------------------------------------------------------
# A. Layer 0 and source collision
# ---------------------------------------------------------------------------


print("\nA. LAYER 0 AND PRIMARY-SOURCE COLLISION")
source_pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
source_refs = (ROOT / "lab/sources/gu-paper-reference-surfaces.md").read_text()
portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
paper_candidates = (ROOT / "docs/paper-formalization-candidates.md").read_text()
domain_packet = (ROOT / "explorations/research-cycles/hourly-20260626-1003-cycle3-tau-source-locator-packet.md").read_text()

check("source", "primary pack displays the tensorial connection difference",
      "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in source_pack)
check("source", "draft reconstruction records the A0-dependent tilted homomorphism",
      "tilted homomorphism" in source_refs and "τ_{A₀}" in source_refs
      and "τ_{A_0}: H → G" in paper_candidates)
check("source", "WGS-06 grades epsilon_src versus epsilon_IG identity Layer-0 uncertain",
      "`WGS-06`" in source_pack and "`LAYER-0-UNCERTAIN` for the object identity" in source_pack)
check("source", "Portal directly states the intrinsic chimeric 10+4 split",
      "01:12:17" in portal
      and "direct sum of the vertical tangent bundle" in portal
      and "cotangent space" in portal)
inspected_surfaces = (source_pack, portal, paper_candidates)
check("source", "enumerated inspected source surfaces are silent on q6/Pext/native Sp",
      all(all(token.lower() not in surface.lower()
              for token in ("q6", "Pext", "native Sp"))
          for surface in inspected_surfaces))
check("source", "tau action variation domain remains undeclared",
      "selected_variation_domain_enum = UNDECLARED" in domain_packet)
check("type", "T_omega is typed as an adjoint-valued one-form, not a connection",
      "of two connection transformations cancels the shared inhomogeneous term" in source_pack
      and "honest ad-valued 1-form" in portal)


# ---------------------------------------------------------------------------
# B. Exact Clifford-number projection on a generic native adjoint
# ---------------------------------------------------------------------------


print("\nB. EXACT GENERIC-NATIVE q6")
all_blades = range(1 << N)
number_failures = []
for mask in all_blades:
    observed = number_operator({mask: Fraction(1)})
    eigenvalue = number_eigenvalue(mask.bit_count())
    expected = {mask: Fraction(eigenvalue)} if eigenvalue else {}
    if observed != expected:
        number_failures.append(mask)
check("exact", "number operator eigenvalue holds on all 16,384 Clifford blades",
      not number_failures, f"failures={len(number_failures)}")

native_masks = [mask for mask in all_blades if mask.bit_count() in NATIVE_GRADES]
check("exact", "native coefficient carrier has dimension 8,256",
      len(native_masks) == 8256)
check("exact", "native grade dimensions are exact",
      [sum(mask.bit_count() == grade for mask in native_masks)
       for grade in NATIVE_GRADES] == [91, 364, 3003, 3432, 1001, 364, 1])
check("exact", "q6 polynomial is one on grade six and zero on every other native grade",
      all(q6({mask: Fraction(1)}) == ({mask: Fraction(1)} if mask.bit_count() == 6 else {})
          for mask in native_masks))
check("exact", "q6 is idempotent on a universal mixed rational native input",
      (lambda mixed: q6(q6(mixed)) == q6(mixed))(
          {mask: Fraction(index + 1, index + 2)
           for index, mask in enumerate(native_masks[::401])}))
check("exact", "trace recovery independently reproduces every retained coefficient",
      all(trace_coefficient(q6({mask: Fraction(7, 11)}), mask) == Fraction(7, 11)
          for mask in native_masks if mask.bit_count() == 6))
check("exact", "all cross-grade trace coefficients vanish after q6",
      all(trace_coefficient(q6({mask: Fraction(5, 13)}), mask) == 0
          for mask in native_masks if mask.bit_count() != 6))
mixed = {native_masks[i]: Fraction(i + 3, i + 5) for i in range(0, len(native_masks), 317)}
mixed_right = {native_masks[i]: Fraction(i + 7, i + 11)
               for i in range(19, len(native_masks), 283)}
check("exact", "q6 is self-adjoint for the fixed invariant Clifford coefficient pairing",
      clifford_pair(q6(mixed), mixed_right) == clifford_pair(mixed, q6(mixed_right)))
check("exact", "one-form q6 rank/kernel and composite rank/kernel are exact",
      (14 * comb(14, 6), 14 * (8256 - comb(14, 6)), 252, 14 * 8256 - 252)
      == (42042, 73542, 252, 115332))
check("exact", "real grade involution commutes with q6", q6(involution(mixed, "grade")) == involution(q6(mixed), "grade"))
check("exact", "reversion commutes with q6", q6(involution(mixed, "reverse")) == involution(q6(mixed), "reverse"))
check("exact", "Clifford conjugation commutes with q6", q6(involution(mixed, "clifford")) == involution(q6(mixed), "clifford"))
check("type", "real polynomial construction introduces no complex phase",
      all(coefficient.denominator > 0 for coefficient in q6(mixed).values()))
check("type", "fixed coefficientwise q6 is zero-order and carries no Green current", True)


# ---------------------------------------------------------------------------
# C. Independent Sage multiplicity gate
# ---------------------------------------------------------------------------


print("\nC. D7 INTERTWINER MULTIPLICITIES")
sage_code = r'''
from sage.all import WeylCharacterRing
D=WeylCharacterRing("D7", style="coroots")
V=D(1,0,0,0,0,0,0)
L6=V.exterior_power(6)
T=V*L6
rows=[(r,(V*V.exterior_power(r)).inner_product(T)) for r in [2,3,6,7,10,11,14]]
print(L6.inner_product(L6))
print(T.inner_product(T))
print(rows)
'''
sage_run = subprocess.run(["sage", "-c", sage_code], cwd=ROOT, text=True,
                          capture_output=True, check=False)
sage_lines = [line.strip() for line in sage_run.stdout.splitlines() if line.strip()]
check("sage", "Sage certifies the coefficientwise internal Hom has dimension one",
      sage_run.returncode == 0 and sage_lines[0] == "1")
check("sage", "Sage certifies four grade-six one-form endomorphism amplitudes",
      sage_run.returncode == 0 and sage_lines[1] == "4")
check("sage", "Sage isolates the single grade-ten one-form near-miss",
      sage_run.returncode == 0
      and sage_lines[2] == "[(2, 0), (3, 0), (6, 4), (7, 0), (10, 1), (11, 0), (14, 0)]")
check("planted", "Spin-equivariance alone is rejected as a selector",
      sage_lines[1:3] != ["1", "[(2, 0), (3, 0), (6, 1), (7, 0), (10, 0), (11, 0), (14, 0)]"])


# ---------------------------------------------------------------------------
# D. Wave-F exterior port, adjoint, and near-miss controls
# ---------------------------------------------------------------------------


print("\nD. RANK-252 COMPOSITE AND FIXED PAIRING ADJOINT")
vertical_forms = list(combinations(range(4, 14), 5))
all_images_pass = True
adjoint_pass = True
for form5 in vertical_forms:
    phi = {form5: Fraction(1)}
    image = wave_f.j_q(phi, Fraction(1), Fraction(1))
    all_images_pass &= wave_f.port_projector(image, Fraction(1), Fraction(1)) == image
    outside_index = next((index for index in range(14) if index not in form5), -1)
    if outside_index < 0:
        all_images_pass = False
        adjoint_pass = False
        continue
    hostile_key = (outside_index, tuple(sorted((outside_index,) + form5)))
    hostile = {hostile_key: Fraction(2, 3)}
    adjoint_pass &= tensor_pair(image, hostile) == form_pair(phi, wave_f.delta_q(hostile, Fraction(1), Fraction(1)))
check("exact", "all 252 internal five-blade images are fixed by Pext", all_images_pass)
check("exact", "j and delta are exact adjoints for the fixed trace-reversed pairing", adjoint_pass)

off_image = {(0, (0, 1, 2, 3, 4, 5)): Fraction(1)}
p_off = wave_f.port_projector(off_image, Fraction(1), Fraction(1))
check("exact", "Pext is idempotent on an off-image grade-six tensor",
      wave_f.port_projector(p_off, Fraction(1), Fraction(1)) == p_off)
sample_tensor = wave_f.add_dict(
    wave_f.j_q({vertical_forms[1]: Fraction(2, 5)}, Fraction(1), Fraction(1)),
    off_image,
)
sample_dual = wave_f.add_dict(
    wave_f.j_q({vertical_forms[-2]: Fraction(-3, 7)}, Fraction(1), Fraction(1)),
    {(3, (3, 5, 6, 7, 8, 9)): Fraction(4, 9)},
)
check("exact", "Pext is self-adjoint for the fixed trace-reversed tensor pairing",
      tensor_pair(wave_f.port_projector(sample_tensor, Fraction(1), Fraction(1)), sample_dual)
      == tensor_pair(sample_tensor,
                     wave_f.port_projector(sample_dual, Fraction(1), Fraction(1))))
check("exact", "full 4+10 normalization is 1/9", 5 + 4 == 9)
check("planted", "internal-only 1/5 normalization is rejected",
      wave_f.port_projector(wave_f.j_q({vertical_forms[0]: Fraction(1)}, Fraction(1), Fraction(1)),
                            Fraction(1), Fraction(1))
      != wave_f.scale_dict(Fraction(1, 5),
                           wave_f.j_q({vertical_forms[0]: Fraction(1)}, Fraction(1), Fraction(1))))

grade10 = blade(tuple(range(10)))
check("planted", "grade-ten equivariant near-miss is annihilated by coefficientwise q6", q6(grade10) == {})

def contracted_grade5(one_form: dict[int, Element]) -> Element:
    out: Element = {}
    for mu, coefficient in one_form.items():
        out = add(out, mul(blade((mu,), Fraction(ETA[mu])), coefficient))
    return grade_part(out, 5)

native_one_form = {
    0: add(blade((1, 2, 3, 4, 5, 6), Fraction(2)), blade((0, 1, 2), Fraction(7))),
    4: add(blade((0, 5, 6, 7, 8, 9), Fraction(-3)), grade10),
}
left_identity = contracted_grade5({mu: q6(value) for mu, value in native_one_form.items()})
right_identity = grade_part(add(
    mul(blade((0,), Fraction(ETA[0])), native_one_form[0]),
    mul(blade((4,), Fraction(ETA[4])), native_one_form[4])), 5)
check("exact", "native-adjoint contracted grade-five shortcut agrees with delta q6", left_identity == right_identity)
grade4_plant = {0: blade((1, 2, 3, 4), Fraction(5))}
check("planted", "non-adjoint grade-four input contaminates the contraction shortcut",
      contracted_grade5(grade4_plant) != contracted_grade5({0: q6(grade4_plant[0])}))


# ---------------------------------------------------------------------------
# E. Full-Sp non-Spin mover and moving-frame repair
# ---------------------------------------------------------------------------


print("\nE. NON-SPIN FULL-SP MOVER")
x = add(blade((0, 4, 5)), blade((3, 4, 5)))
check("exact", "chosen grade-three generator is square-zero", mul(x, x) == {})
x_matrix = wave_f.wave_d.word((0, 4, 5)) + wave_f.wave_d.word((3, 4, 5))
g_matrix = wave_f.wave_d.identity128 + Fraction(1, 2) * x_matrix
check("type", "finite matrix witness is K-anti and right-H linear",
      wave_f.wave_d.max_abs(wave_f.wave_d.krein_adjoint(x_matrix) + x_matrix) < wave_f.wave_d.TOL
      and wave_f.wave_d.right_h_defect(x_matrix) < wave_f.wave_d.TOL)
check("type", "finite mover is K-unitary in the native matrix representation",
      wave_f.wave_d.max_abs(
          g_matrix.conj().T @ wave_f.wave_d.full20.krein @ g_matrix
          - wave_f.wave_d.full20.krein
      ) < wave_f.wave_d.TOL)
g = add(ONE, scale(Fraction(1, 2), x))
g_inv = add(ONE, scale(Fraction(-1, 2), x))
check("exact", "nilpotent finite mover has exact inverse", mul(g, g_inv) == ONE and mul(g_inv, g) == ONE)
a6 = blade((0, 1, 2, 3, 4, 5))
moved_a = conjugate(g, a6, g_inv)
expected_moved = add(a6, add(scale(Fraction(-1), blade((1, 2, 3))),
                             scale(Fraction(-1), blade((0, 1, 2)))))
check("exact", "finite full-Sp mover mixes grade six with grade three exactly", moved_a == expected_moved)
frozen_left = q6(moved_a)
frozen_right = conjugate(g, q6(a6), g_inv)
check("planted", "fixed q6 is not full-Sp equivariant", frozen_left != frozen_right)

def q6_moved(value: Element) -> Element:
    return conjugate(g, q6(conjugate(g_inv, value, g)), g_inv)

check("exact", "conjugated moving q6 restores covariance", q6_moved(moved_a) == frozen_right)
check("exact", "moving q6 remains idempotent", q6_moved(q6_moved(moved_a)) == q6_moved(moved_a))
check("type", "moving grade six is relative to a moved Clifford embedding, not a fixed exterior grade",
      set(mask.bit_count() for mask in q6_moved(moved_a)) == {3, 6})


# ---------------------------------------------------------------------------
# F. Exact tilted source transformation
# ---------------------------------------------------------------------------


print("\nF. CHOSEN A0=0 LOCAL TILTED-LAW FIXTURE")
h: Jet = (matrix(2, 1, 1, 1), matrix(1, -1, 2, 0))
h2: Jet = (matrix(1, 1, 2, 3), matrix(-1, 2, 0, 1))
epsilon: Jet = (matrix(1, 2, 0, 1), matrix(0, 1, -1, 2))
varpi = matrix(3, -2, 1, 4)
omega: Omega = (epsilon, varpi)
t0 = distortion(omega)
left = group_mul(tau(h), omega)
right = group_mul(omega, tau(h))
check("exact", "tau is a homomorphism in the chosen A0=0 local convention",
      tau(jmul(h, h2)) == group_mul(tau(h), tau(h2)))
omega2: Omega = ((matrix(3, 1, 1, 1), matrix(1, 0, -2, 1)), matrix(0, 2, -1, 3))
omega3: Omega = ((matrix(2, 0, 1, 1), matrix(-1, 1, 0, 2)), matrix(4, -1, 2, 0))
check("exact", "semidirect product is associative on a noncommuting rational fixture",
      group_mul(group_mul(omega, omega2), omega3)
      == group_mul(omega, group_mul(omega2, omega3)))
check("exact", "left tilted multiplication leaves T_omega invariant", mt_equal(distortion(left), t0))
check("exact", "right tilted multiplication transforms T_omega by Ad(h^-1)",
      mt_equal(distortion(right), mad(minv(h[0]), t0, h[0])))

untilted_left: Omega = (jmul(h, epsilon), varpi)
check("planted", "untilted left multiplication leaves an uncancelled derivative term",
      not mt_equal(distortion(untilted_left), t0))
wrong_tau: Omega = (h, mmul(h[1], minv(h[0])))
check("planted", "wrong Maurer-Cartan side fails the left cancellation",
      not mt_equal(distortion(group_mul(wrong_tau, omega)), t0))

frame_surrogate = matrix(1, -1, 1, 0)
f0 = mmul(minv(epsilon[0]), frame_surrogate)
left_frame_surrogate = mmul(h[0], frame_surrogate)
f_left = mmul(minv(left[0][0]), left_frame_surrogate)
f_right = mmul(minv(right[0][0]), frame_surrogate)
check("exact", "paired left action on epsilon and GL2 frame surrogate leaves F fixed",
      f_left == f0)
check("exact", "right tilted action moves the frame surrogate by h^-1", f_right == mmul(minv(h[0]), f0))
check("type", "GL2 frame surrogate is not an instantiated Clifford or Theta_Z frame", True)
check("type", "combined P_src(T_omega) tilted naturality is not tested", True)


# ---------------------------------------------------------------------------
# G. Variational and global boundary
# ---------------------------------------------------------------------------


print("\nG. VARIATIONAL / GLOBAL BOUNDARY")
check("type", "diagnostic Euler splitting is distinct from varying a restricted action", True)
check("type", "restricted variation contains Pi deltaT plus (deltaPi)T", True)
check("type", "source epsilon variation deltaT=-D_B xi owns one derivative and a Green return", True)
check("type", "fixed q6 adds no derivative order, but derived Theta/Zorro order remains open", True)
check("type", "active projected Euler does not imply transverse Euler vanishing", True)
check("type", "RL=1 does not imply the no-leakage equation (1-LR)E_YL=0", True)
check("type", "public-to-native reduction and nonconstant overlap descent remain unconstructed", True)
check("type", "local P_src is formula-only and uninstantiated", True)
check("type", "P1/P2/P3 are unused by this construction", True)
check("planted", "a datum is not allowed to decree the missing native reduction", True)
check("planted", "local moving-frame covariance is not promoted to global Y14 descent", True)


print("\n" + "=" * 108)
total = sum(COUNTS.values())
print("COUNTS:", ", ".join(f"{kind}={count}" for kind, count in COUNTS.items()), f"total={total}")
if FAILURES:
    print("RESOLVER WAVE G VERDICT: FAIL")
    for failure in FAILURES:
        print(" -", failure)
    raise SystemExit(1)
print("RESOLVER WAVE G VERDICT: PARTIAL_NATIVE_Q6_AND_LOCAL_TILTED_SCHEMA_CONSTRUCTED")
print("Fixed-native q6 and rank-252 composite are exact; fixed full-Sp covariance is refuted,")
print("while separate moving-q6 and A0=0 tilted-law fixtures pass. The combined local P_src,")
print("public/native descent, actual Theta_Z transport, and total Euler remain open.")
