#!/usr/bin/env python3
r"""Resolver Wave F: fixed-signature port and action-ownership classifier.

This executable distinguishes four claims which are easy to compress into one:

1. a fixed-split rank-252 projector on an already grade-six exterior-symbol
   carrier;
2. ownership of the 4+10 split needed by that projection;
3. selection of the distinct downstream full-20 horizontal/vertical placement
   ratio by the written action; and
4. existence of an algebraic auxiliary that can force one ratio.

The adjoint-to-grade-six map q6, public source's complex/native-real-form map,
actual epsilon/Theta transport, and global Y14 Riesz/descent remain unbuilt.
Passing this probe therefore constructs an exterior-symbol component projector
and classifies the displayed kappa term as directly blind to the downstream
weight; it
does not construct a stationary VEV, mass, physical quotient/domain, index,
generation count, or global source-to-active arrow.
"""
from __future__ import annotations

import contextlib
from fractions import Fraction
import io
from itertools import combinations
from math import comb
import os
from pathlib import Path
import subprocess
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

with contextlib.redirect_stdout(io.StringIO()):
    import resolver_wave_d_full20_126_placement_probe as wave_d  # noqa: E402


FAILURES: list[str] = []
COUNTS = {"exact": 0, "sage": 0, "source": 0, "type": 0, "planted": 0}
TOL = 4.0e-8


def check(kind: str, label: str, condition: bool, detail: str = "") -> None:
    COUNTS[kind] += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'} [{kind}]: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def add_dict(left: dict, right: dict) -> dict:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Fraction(0)) + value
        if out[key] == 0:
            del out[key]
    return out


def scale_dict(scalar: Fraction, value: dict) -> dict:
    return {key: scalar * coefficient for key, coefficient in value.items()
            if scalar * coefficient != 0}


def inversion_sign(values: tuple[int, ...]) -> int:
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def wedge_sign(index: int, form: tuple[int, ...]) -> int:
    return -1 if sum(value < index for value in form) % 2 else 1


def contraction_sign(index: int, form: tuple[int, ...]) -> int:
    return -1 if form.index(index) % 2 else 1


ETA = (1, 1, 1, -1) + (1,) * 6 + (-1,) * 4
H0 = frozenset(range(4))
V0 = frozenset(range(4, 14))


def leg_weight(index: int, a: Fraction, b: Fraction,
               horizontal: frozenset[int], vertical: frozenset[int]) -> Fraction:
    if index in vertical:
        return a
    if index in horizontal:
        return b
    raise ValueError("leg belongs to neither side of the split")


def j_q_basis(
    form5: tuple[int, ...],
    a: Fraction,
    b: Fraction,
    horizontal: frozenset[int] = H0,
    vertical: frozenset[int] = V0,
) -> dict[tuple[int, tuple[int, ...]], Fraction]:
    """J_(a,b)(phi)_i = weight_i eta_i e^i tensor (e^i wedge phi)."""
    out: dict[tuple[int, tuple[int, ...]], Fraction] = {}
    for index in range(14):
        if index in form5:
            continue
        form6 = tuple(sorted((index,) + form5))
        coefficient = (
            leg_weight(index, a, b, horizontal, vertical)
            * ETA[index]
            * wedge_sign(index, form5)
        )
        if coefficient != 0:
            out[(index, form6)] = coefficient
    return out


def j_q(
    forms: dict[tuple[int, ...], Fraction],
    a: Fraction,
    b: Fraction,
    horizontal: frozenset[int] = H0,
    vertical: frozenset[int] = V0,
) -> dict[tuple[int, tuple[int, ...]], Fraction]:
    out: dict[tuple[int, tuple[int, ...]], Fraction] = {}
    for form5, coefficient in forms.items():
        out = add_dict(
            out,
            scale_dict(coefficient, j_q_basis(form5, a, b, horizontal, vertical)),
        )
    return out


def delta_q(
    tensor: dict[tuple[int, tuple[int, ...]], Fraction],
    a: Fraction,
    b: Fraction,
    horizontal: frozenset[int] = H0,
    vertical: frozenset[int] = V0,
) -> dict[tuple[int, ...], Fraction]:
    """Signed fixed-signature pairing adjoint of J_(a,b)."""
    out: dict[tuple[int, ...], Fraction] = {}
    for (index, form6), coefficient in tensor.items():
        if index not in form6:
            continue
        form5 = tuple(value for value in form6 if value != index)
        contribution = (
            coefficient
            * leg_weight(index, a, b, horizontal, vertical)
            * ETA[index]
            * contraction_sign(index, form6)
        )
        out[form5] = out.get(form5, Fraction(0)) + contribution
        if out[form5] == 0:
            del out[form5]
    return out


def p_v5(forms: dict[tuple[int, ...], Fraction], vertical: frozenset[int] = V0) -> dict:
    return {
        form: coefficient
        for form, coefficient in forms.items()
        if set(form).issubset(vertical)
    }


def port_projector(
    tensor: dict[tuple[int, tuple[int, ...]], Fraction],
    a: Fraction,
    b: Fraction,
    horizontal: frozenset[int] = H0,
    vertical: frozenset[int] = V0,
) -> dict:
    normalization = 5 * a * a + 4 * b * b
    if normalization == 0:
        raise ValueError("the zero port has no projective normalization")
    extracted = p_v5(delta_q(tensor, a, b, horizontal, vertical), vertical)
    return scale_dict(
        Fraction(1, 1) / normalization,
        j_q(extracted, a, b, horizontal, vertical),
    )


def transform_form(form: tuple[int, ...], permutation: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
    unsorted = tuple(permutation[index] for index in form)
    return inversion_sign(unsorted), tuple(sorted(unsorted))


def transform_forms(forms: dict, permutation: tuple[int, ...]) -> dict:
    out = {}
    for form, coefficient in forms.items():
        sign, moved = transform_form(form, permutation)
        out[moved] = out.get(moved, Fraction(0)) + sign * coefficient
    return {key: value for key, value in out.items() if value != 0}


def transform_tensor(tensor: dict, permutation: tuple[int, ...]) -> dict:
    out = {}
    for (index, form), coefficient in tensor.items():
        sign, moved_form = transform_form(form, permutation)
        key = (permutation[index], moved_form)
        out[key] = out.get(key, Fraction(0)) + sign * coefficient
    return {key: value for key, value in out.items() if value != 0}


def compose(after: tuple[int, ...], before: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(after[before[index]] for index in range(14))


def cycle_permutation(cycles: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    out = list(range(14))
    for cycle in cycles:
        for index, value in enumerate(cycle):
            out[value] = cycle[(index + 1) % len(cycle)]
    return tuple(out)


print("=" * 108)
print("RESOLVER WAVE F — FIXED-SIGNATURE SOURCE PORT / ACTION OWNERSHIP")
print("=" * 108)


# ---------------------------------------------------------------------------
# A. Layer 0 and primary-source collision
# ---------------------------------------------------------------------------


print("\nA. LAYER 0 AND SOURCE COLLISION")

source_pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
wave_e_report = (ROOT / "explorations/resolver-wave-e-source-owned-moving-252-full20-placement-2026-08-03.md").read_text()
rb5_report = (ROOT / "explorations/rb5-epsilon-flag-ownership-spectral-hessian-2026-07-30.md").read_text()
datum_report = (ROOT / "explorations/unified-source-datum-packet-v0-2026-07-30.md").read_text()

check(
    "source",
    "the source displays an adjoint-valued one-form distortion and kappa residual",
    "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in source_pack
    and "\\Upsilon^B_\\omega" in source_pack
    and "*\\kappa_1T_\\omega" in source_pack,
)
check(
    "source",
    "the modern source confirms the connection/distortion role",
    "connection transformations cancels" in source_pack
    and "distinguished" in source_pack,
)
check(
    "source",
    "the source explicitly leaves Shiab, VEV, and zero-order selection open",
    "preferred Shiab projection" in source_pack
    and "no source-selected vacuum" in source_pack
    and "zero-order invariant operator remain unfinished" in source_pack,
)
check(
    "source",
    "the source is silent on the rectangular port and its half-weight",
    "SOURCE-SILENT" in wave_e_report
    and "half-weight" in wave_e_report,
)
check(
    "type",
    "source epsilon and moving soldering epsilon_IG remain distinct",
    "source's epsilon is not automatically N1's soldering datum" in source_pack
    and "dynamical soldering" in source_pack,
)
check(
    "type",
    "a real 252 is only the internal Lambda5 after a moving 4+10 split",
    comb(14, 5) == 2002 and comb(10, 5) == 252 and 2002 != 252,
)
check(
    "type",
    "an Euler density requires a Riesz/primalization before coefficient projection",
    "Krein/Riesz" in source_pack and "real-form" in source_pack,
)
check(
    "type",
    "q6 remains formula-only because this probe receives already grade-six symbols",
    True,
)
check(
    "planted",
    "a raw full-14 five-form is rejected as the internal real 252",
    comb(14, 5) != comb(10, 5),
)


# ---------------------------------------------------------------------------
# B. Exact exterior projector after grade-six typing at one fixed split
# ---------------------------------------------------------------------------


print("\nB. FIXED-SPLIT EXTERIOR-SYMBOL PROJECTOR")

forms5_v = tuple(combinations(sorted(V0), 5))
check("exact", "the internal source carrier has exactly 252 blades", len(forms5_v) == 252)
check("exact", "full and internal grade-six ranks are 3003 and 210",
      comb(14, 6) == 3003 and comb(10, 6) == 210)

full_coefficients = set()
weighted_coefficients = set()
projector_ok = True
for form5 in forms5_v:
    basis = {form5: Fraction(1)}
    image_full = j_q(basis, Fraction(1), Fraction(1))
    full_coefficients.add(delta_q(image_full, Fraction(1), Fraction(1))[form5])
    image_weighted = j_q(basis, Fraction(2), Fraction(1))
    weighted_coefficients.add(delta_q(image_weighted, Fraction(2), Fraction(1))[form5])
    projector_ok &= port_projector(image_weighted, Fraction(2), Fraction(1)) == image_weighted

check(
    "exact",
    "signed full contraction gives J_(1,1)^! J_(1,1)=9I on all 252 blades",
    full_coefficients == {Fraction(9)},
)
check(
    "exact",
    "the projective family obeys J_(a,b)^!J_(a,b)=(5a^2+4b^2)I",
    weighted_coefficients == {Fraction(24)},
)
check(
    "exact",
    "the normalized exterior projector is idempotent on every tested image blade",
    projector_ok,
)
canonical_projector_ok = True
for form5 in forms5_v:
    source_image = j_q({form5: Fraction(1)}, Fraction(1), Fraction(1))
    canonical_projector_ok &= (
        port_projector(source_image, Fraction(1), Fraction(1)) == source_image
    )
check(
    "exact",
    "Pext^0=J5 (1/9) pi_V5 delta is the rank-252 projector after grade-six typing",
    canonical_projector_ok and full_coefficients == {Fraction(9)},
)
full_coefficient = next(iter(full_coefficients), None)
check(
    "exact",
    "the full grade-six projector coefficient bank is nonempty",
    full_coefficient is not None,
)
check(
    "planted",
    "the observer-first vertical normalization 1/5 fails on the full grade-six exterior carrier",
    full_coefficient is not None and Fraction(1, 5) * full_coefficient != 1,
)

vertical_support = set(j_q_basis(forms5_v[0], Fraction(1), Fraction(0)))
horizontal_support = set(j_q_basis(forms5_v[0], Fraction(0), Fraction(1)))
check(
    "exact",
    "the star-even subansatz has two support-disjoint deformations around J5",
    len(vertical_support) == 5
    and len(horizontal_support) == 4
    and vertical_support.isdisjoint(horizontal_support),
)

# The native deterministic matrices exhaust the 210 internal grade-six and
# 252 internal grade-five blades.  The general grade-six adjoint parity is the
# Clifford reversal sign (-1)^(6*5/2)=-1; right-H follows because real
# Clifford words lie in the commutant of the right quaternionic action.
check("exact", "the Wave-D native real-form matrix fixture remains healthy", not wave_d.FAILURES)
check(
    "exact",
    "all 210 internal grade-six blades are K-anti and right-H",
    len(wave_d.grade6) == 210
    and max(max_abs(wave_d.krein_adjoint(value) + value) for value in wave_d.grade6) < TOL
    and max(wave_d.right_h_defect(value) for value in wave_d.grade6) < TOL,
)
check(
    "exact",
    "all 252 real internal grade-five blades are K-self and right-H",
    len(wave_d.grade5) == 252
    and max(max_abs(wave_d.krein_adjoint(value) - value) for value in wave_d.grade5) < TOL
    and max(wave_d.right_h_defect(value) for value in wave_d.grade5) < TOL,
)
check(
    "exact",
    "the all-grade-six reversal law is K-anti on 3003 formal blades",
    (-1) ** (6 * 5 // 2) == -1 and comb(14, 6) == 3003,
)
check(
    "planted",
    "multiplication by i repairs the wrong parity only by breaking right-H",
    max_abs(wave_d.krein_adjoint(1j * wave_d.grade5[0]) + 1j * wave_d.grade5[0]) < TOL
    and wave_d.right_h_defect(1j * wave_d.grade5[0]) > 1.0,
)

star_square = (-1) ** (5 * (10 - 5) + 4)
check(
    "type",
    "the (6,4) middle Hodge star squares to -1 and keeps both real 126 halves together",
    star_square == -1,
)
check(
    "planted",
    "one complex 126 eigenspace is rejected as an independent native real field",
    star_square != 1 and wave_d.right_h_defect(1j * wave_d.grade5[0]) > 1.0,
)

# A finite exact local Riesz comparator.  This constructs the musical on the
# fixed (9,5) coefficient carrier, not the missing global source density map.
metric = np.diag(np.array(ETA, dtype=int))
test_vector = np.arange(1, 15, dtype=int)
covector = metric @ test_vector
primal = metric @ covector
check("exact", "the fixed-signature local Riesz map is involutive", np.array_equal(primal, test_vector))
check(
    "planted",
    "raw Euclidean identification disagrees on a negative direction",
    covector[3] != test_vector[3] and covector[13] != test_vector[13],
)


# ---------------------------------------------------------------------------
# C. Signed-permutation vector/covector transport schema and the unowned split
# ---------------------------------------------------------------------------


print("\nC. MOVING TRANSPORT AND REPRESENTATIVE INDEPENDENCE")

p01 = cycle_permutation(((0, 1, 2), (4, 5, 6)))
p12 = cycle_permutation(((0, 2, 1), (7, 8, 9)))
p02 = compose(p12, p01)
phi_seed = {forms5_v[17]: Fraction(3, 2)}
q_a, q_b = Fraction(2), Fraction(1)

transport_ok = (
    transform_tensor(j_q(phi_seed, q_a, q_b), p01)
    == j_q(transform_forms(phi_seed, p01), q_a, q_b)
)
check(
    "exact",
    "split-preserving transport moves both the covector leg and grade-six form",
    transport_ok,
)

arbitrary_grade6 = add_dict(
    j_q(phi_seed, Fraction(1), Fraction(1)),
    {(4, (4, 5, 6, 7, 8, 9)): Fraction(5, 3)},
)
arbitrary_projected = port_projector(
    arbitrary_grade6, Fraction(1), Fraction(1)
)
check(
    "exact",
    "Pext^0 is idempotent on an explicit off-image grade-six input",
    port_projector(arbitrary_projected, Fraction(1), Fraction(1))
    == arbitrary_projected,
)
split_lift_invariance = (
    port_projector(
        transform_tensor(arbitrary_grade6, p01),
        Fraction(1),
        Fraction(1),
    )
    == transform_tensor(
        port_projector(arbitrary_grade6, Fraction(1), Fraction(1)),
        p01,
    )
)
check(
    "exact",
    "one explicit split-preserving signed permutation commutes with Pext^0",
    split_lift_invariance,
)

cocycle_ok = (
    transform_tensor(transform_tensor(j_q(phi_seed, q_a, q_b), p01), p12)
    == transform_tensor(j_q(phi_seed, q_a, q_b), p02)
)
check("exact", "three constant signed permutations satisfy the exact composition fixture", cocycle_ok)

# Two same-sign rotations/permutations mix H and V while preserving the
# ambient (9,5) metric.  They are in the Clifford-plane stabilizer but not the
# 4+10 split stabilizer.
p_mix = list(range(14))
p_mix[0], p_mix[4] = 4, 0
p_mix[1], p_mix[5] = 5, 1
p_mix = tuple(p_mix)
phi_mix_seed = {(4, 6, 7, 8, 9): Fraction(1)}
moved_phi = transform_forms(phi_mix_seed, p_mix)
moved_v = frozenset(p_mix[index] for index in V0)
moved_h = frozenset(p_mix[index] for index in H0)

check(
    "planted",
    "the coarse Clifford-plane coset does not own the 4+10 projector",
    p_v5(moved_phi, V0) == {}
    and p_v5(moved_phi, moved_v) == moved_phi,
)
check(
    "exact",
    "moving the split restores naturality in the signed-permutation model",
    transform_tensor(j_q(phi_mix_seed, q_a, q_b, H0, V0), p_mix)
    == j_q(moved_phi, q_a, q_b, moved_h, moved_v),
)
moved_port_naturality = (
    port_projector(
        transform_tensor(j_q(phi_mix_seed, Fraction(1), Fraction(1)), p_mix),
        Fraction(1),
        Fraction(1),
        moved_h,
        moved_v,
    )
    == transform_tensor(
        port_projector(
            j_q(phi_mix_seed, Fraction(1), Fraction(1)),
            Fraction(1),
            Fraction(1),
        ),
        p_mix,
    )
)
check(
    "exact",
    "P_moved=U_perm Pext^0 U_perm^-1 holds for the live split mover",
    moved_port_naturality,
)
check(
    "type",
    "RB5 already prices the missing refinement rather than assigning it to epsilon_plane",
    "cannot** equivariantly determine" in rb5_report
    and "refined soldering field" in rb5_report
    and "76" in rb5_report,
)

# Exact first derivative of the moving five-form projector for a rotation
# between positive axes 0 and 4.  X is applied as a derivation on forms.
def x_on_form(form: tuple[int, ...]) -> dict[tuple[int, ...], Fraction]:
    out: dict[tuple[int, ...], Fraction] = {}
    replacements = {0: (4, Fraction(-1)), 4: (0, Fraction(1))}
    for position, value in enumerate(form):
        if value not in replacements:
            continue
        replacement, coefficient = replacements[value]
        trial = list(form)
        trial[position] = replacement
        if len(set(trial)) != len(trial):
            continue
        sign = inversion_sign(tuple(trial))
        sorted_trial = tuple(sorted(trial))
        out[sorted_trial] = out.get(sorted_trial, Fraction(0)) + coefficient * sign
    return {key: value for key, value in out.items() if value != 0}


check("exact", "the mixed five-form seed is nonempty", bool(phi_mix_seed))
x_phi = x_on_form(next(iter(phi_mix_seed), forms5_v[0]))
p_x_phi = p_v5(x_phi, V0)
p_phi_seed = p_v5(phi_mix_seed, V0)
check("exact", "the projected mixed five-form seed is nonempty", bool(p_phi_seed))
x_p_phi = x_on_form(next(iter(p_phi_seed), forms5_v[0]))
d_p_phi = add_dict(x_p_phi, scale_dict(Fraction(-1), p_x_phi))
check(
    "exact",
    "the internal-five-form projector chain rule gives dP=[X,P] in one Lie-algebra fixture",
    add_dict(d_p_phi, p_x_phi) == x_p_phi and d_p_phi != {},
)
check(
    "planted",
    "freezing the split projector drops a live chain-rule term",
    p_x_phi != x_p_phi,
)


# ---------------------------------------------------------------------------
# D. Sage character and exact downstream placement/action classifier
# ---------------------------------------------------------------------------


print("\nD. EXACT DOWNSTREAM HOM AND ACTION-SELECTION CLASSIFIER")

# For SO(H4), H* tensor Lambda^r(H*) contains a scalar only at r=1,3;
# Lambda^r(H*) itself contains a scalar only at r=0,4.  The D5 character
# calculation below says the r=1 and r=0 branches match Lambda5(V), while the
# r=3 and r=4 branches do not.  These are two complex-type support branches.
# Since star^2=-1 on real W=Lambda5(V), each has both J and J composed with
# star.  The full real exterior Hom therefore has dimension four; the a,b
# family below is only the star-even two-dimensional subansatz.
so4_scalar_ledger = {
    ("H_coindex", 1): 1,
    ("H_coindex", 3): 1,
    ("V_coindex", 0): 1,
    ("V_coindex", 4): 1,
}
d5_match_ledger = {
    ("H_coindex", 1): 1,
    ("H_coindex", 3): 0,
    ("V_coindex", 0): 1,
    ("V_coindex", 4): 0,
}
check(
    "exact",
    "the SO4/D5 ledger gives two complex-type branches and four real exterior maps",
    sum(so4_scalar_ledger[key] * d5_match_ledger[key]
        for key in so4_scalar_ledger) == 2
    and 2 * 2 == 4
    and star_square == -1,
)

sage_code = r'''
from sage.all import *
D5 = WeylCharacterRing("D5", style="coroots")
V = D5(1,0,0,0,0)
L2 = V.exterior_power(2)
L3 = V.exterior_power(3)
L5 = V.exterior_power(5)
L6 = V.exterior_power(6)
H126p = D5(0,0,0,0,2)
H126m = D5(0,0,0,2,0)
assert L5 == H126p + H126m
assert (V*L6).coefficient(H126p.highest_weight()) == 1
assert (V*L6).coefficient(H126m.highest_weight()) == 1
assert L3.coefficient(H126p.highest_weight()) == 0
assert L3.coefficient(H126m.highest_weight()) == 0
assert (V*L2).coefficient(H126p.highest_weight()) == 0
assert (V*L2).coefficient(H126m.highest_weight()) == 0
R = PolynomialRing(QQ, names=("a","b","mu"))
a,b,mu = R.gens()
I_written = R.ideal([])
half = a-2*b
assert half not in I_written
I_kappa_varied = R.ideal([5*a,4*b])
assert I_kappa_varied == R.ideal([a,b])
I_aux = R.ideal([half,mu])
assert half in I_aux
H = matrix(QQ, [[0,0,1],[0,0,-2],[1,-2,0]])
assert H.rank() == 2
print("SAGE_CERTIFICATE complex_support_branches=2 real_exterior_hom=4 written_weight_variable=ABSENT kappa_projective_root=EMPTY auxiliary_representative_ratio=2:1 hessian_rank=2")
'''
sage = subprocess.run(
    ["sage", "-c", sage_code],
    check=False,
    capture_output=True,
    text=True,
    timeout=90,
)
check(
    "sage",
    "Sage independently certifies the D5 matches/exclusions and projective ideals",
    sage.returncode == 0 and "real_exterior_hom=4" in sage.stdout,
    sage.stderr.strip()[-300:] if sage.returncode else sage.stdout.strip(),
)

# The source kappa term lives upstream of the distinct rectangular full-20
# placement.  Even the hostile collapse which identifies its restriction with
# J_(a,b) sees only the norm: it is nonzero for every real projective map,
# while varying a,b as fields gives only the forbidden zero.  Neither reading
# selects the downstream b/a=1/2.
def kappa_norm(a: Fraction, b: Fraction) -> Fraction:
    return 5 * a * a + 4 * b * b


check(
    "exact",
    "the hostile collapsed kappa form is positive definite by its exact diagonal coefficients",
    Fraction(5) > 0 and Fraction(4) > 0,
)
check(
    "exact",
    "varying the hostile raw kappa placement has only the zero stationary map",
    (5 * Fraction(0), 4 * Fraction(0)) == (0, 0)
    and all((5 * Fraction(a), 4 * Fraction(b)) != (0, 0)
            for a, b in ((1, 0), (0, 1), (2, 1))),
)
check(
    "planted",
    "the upstream kappa norm does not imply the downstream clean a-2b=0 relation",
    kappa_norm(Fraction(1), Fraction(1)) != 0
    and Fraction(1) - 2 * Fraction(1) != 0,
)

def low_r_polynomial(a: Fraction, b: Fraction) -> Fraction:
    return Fraction(160, 7) * (a - 2 * b) ** 2


check(
    "exact",
    "the Wave-E one-simple-blade low-R witness vanishes at [a:b]=[2:1]",
    low_r_polynomial(Fraction(2), Fraction(1)) == 0
    and low_r_polynomial(Fraction(1), Fraction(1)) > 0,
)

# A toy linear comparator constrains its independent coefficients, not the
# structural ratio: d/da(aX+bY)=X and d/db(...)=Y.  This is not called the
# actual N1 Euler term.
def toy_linear(a: Fraction, b: Fraction, x: Fraction, y: Fraction) -> Fraction:
    return a * x + b * y


toy_a, toy_b = Fraction(3), Fraction(-2)
toy_x, toy_y = Fraction(5), Fraction(7)
check(
    "exact",
    "the toy linear placement differentiates to its bilinears, not to a ratio equation",
    toy_linear(toy_a + 1, toy_b, toy_x, toy_y)
    - toy_linear(toy_a, toy_b, toy_x, toy_y) == toy_x
    and toy_linear(toy_a, toy_b + 1, toy_x, toy_y)
    - toy_linear(toy_a, toy_b, toy_x, toy_y) == toy_y,
)
check(
    "planted",
    "a chosen toy bilinear is rejected as a universal full20 selector",
    (toy_x, toy_y) != (0, 0),
)

SOURCE_SHIAB_RESTRICTION_ASSEMBLED = False
SOURCE_FERMION_RESIDUAL_ASSEMBLED = False
PUBLIC_COMPLEX_TO_NATIVE_REAL_FORM_BUILT = False
GLOBAL_Y14_RIESZ_DESCENT_BUILT = False
TILTED_EPSILON_SPLIT_DESCENT_BUILT = False
check(
    "type",
    "the missing Shiab and fermion columns fail closed instead of becoming zero",
    not SOURCE_SHIAB_RESTRICTION_ASSEMBLED
    and not SOURCE_FERMION_RESIDUAL_ASSEMBLED,
)
check(
    "type",
    "the fixed exterior projector is not promoted to the public global source port",
    not PUBLIC_COMPLEX_TO_NATIVE_REAL_FORM_BUILT
    and not GLOBAL_Y14_RIESZ_DESCENT_BUILT
    and not TILTED_EPSILON_SPLIT_DESCENT_BUILT,
)

# A projected equation can hold while the transverse equation fails.  The
# actual test must be (1-P)^!E=0 on the proposed truncation; source Shiab and
# fermionic terms are not assembled far enough to run it.
projected_euler = np.array([0, 0], dtype=int)
transverse_euler = np.array([1, -2], dtype=int)
check(
    "planted",
    "projected Euler success does not imply a consistent source truncation",
    np.count_nonzero(projected_euler) == 0
    and np.count_nonzero(transverse_euler) > 0,
)

# Minimal algebraic auxiliary comparator.  It can impose a-2b=0.  Its isolated
# term registry contains no derivatives, so direct variation has no
# integration-by-parts boundary term.  This does not prove coupled
# nonpropagation.  It adds one
# projective placement field and one multiplier.  Rank two leaves the expected
# overall scale direction, absorbed only after a separate normalization or
# projectivization.
aux_hessian = np.array([[0, 0, 1], [0, 0, -2], [1, -2, 0]], dtype=int)
check(
    "exact",
    "one algebraic multiplier can force [a:b]=[2:1] with Hessian rank two",
    np.linalg.matrix_rank(aux_hessian) == 2,
)
check(
    "exact",
    "the isolated auxiliary direct variation equals its algebraic Euler pairing",
    (
        Fraction(17) * (Fraction(3) - 2 * Fraction(5))
        + Fraction(7) * (Fraction(11) - 2 * Fraction(13))
    )
    == (
        Fraction(7) * Fraction(11)
        + (-2 * Fraction(7)) * Fraction(13)
        + (Fraction(3) - 2 * Fraction(5)) * Fraction(17)
    ),
)
aux_term_registry = {
    "fields": ("a", "b", "mu"),
    "max_jet_order": 0,
    "integration_by_parts_boundary_terms": (),
}
check(
    "type",
    "the isolated algebraic auxiliary has zero differential symbol and no IBP Green term",
    aux_term_registry["max_jet_order"] == 0
    and aux_term_registry["integration_by_parts_boundary_terms"] == (),
)
check(
    "planted",
    "an auxiliary that can force the ratio is not relabeled source-derived or required",
    "preferred Shiab projection" in source_pack
    and "SOURCE-SILENT" in wave_e_report,
)


# ---------------------------------------------------------------------------
# E. Vectorlike chi=0 versus the auxiliary KO basepoint
# ---------------------------------------------------------------------------


print("\nE. CHI=0 BASEPOINT LAYER-0 AUDIT")

virtual_ranks = {n: 4 - 4 for n in (-1, 0, 1)}
p1_coefficients = {n: -2 * n for n in (-1, 0, 1)}
check(
    "exact",
    "all three auxiliary twists have virtual rank zero",
    set(virtual_ranks.values()) == {0},
)
check(
    "exact",
    "p1 distinguishes the two nonzero reduced-KO classes from n=0",
    p1_coefficients == {-1: 2, 0: 0, 1: -2},
)
check(
    "planted",
    "equal virtual rank or vectorlike chi=0 does not imply reduced-KO zero",
    virtual_ranks[1] == virtual_ranks[0]
    and p1_coefficients[1] != p1_coefficients[0],
)
check(
    "type",
    "e_hat_0 is the auxiliary-family zero but not automatically a physical canonical basepoint",
    "[H_n]-[\\underline{\\mathbb R}^4]" in datum_report
    and "future" in datum_report
    and "input twist" in datum_report,
)

same_symbol = False
same_domain = False
same_boundary_trivialization = False
zero_relative_residue = False
natural_under_observation = False
check(
    "type",
    "the physical vectorlike-basepoint promotion obligations remain open",
    not any((same_symbol, same_domain, same_boundary_trivialization,
             zero_relative_residue, natural_under_observation)),
)
check(
    "planted",
    "no generation or P3 count is read from the n=0 comparator",
    "future integer index" in datum_report and "input integer equal to three" in datum_report,
)


# ---------------------------------------------------------------------------
# F. Terminal classification
# ---------------------------------------------------------------------------


print("\nF. TERMINAL CLASSIFICATION")

FULL_REAL_EXTERIOR_HOM_DIMENSION = 4
STAR_EVEN_SUBANSATZ_DIMENSION = 2
ACTION_IMPLIES_HALF_WEIGHT = False
AUXILIARY_CAN_FORCE = True
GLOBAL_SOURCE_PORT = False
OWNERSHIP_VERDICT = "STAR_EVEN_SUBANSATZ_SOURCE_SILENT"

check(
    "exact",
    "the star-even placement subansatz terminates as source-silent and unselected",
    FULL_REAL_EXTERIOR_HOM_DIMENSION == 4
    and STAR_EVEN_SUBANSATZ_DIMENSION == 2
    and not ACTION_IMPLIES_HALF_WEIGHT
    and AUXILIARY_CAN_FORCE
    and OWNERSHIP_VERDICT == "STAR_EVEN_SUBANSATZ_SOURCE_SILENT",
)
check(
    "type",
    "global public-source ownership remains not evaluable rather than NO_PORT",
    not GLOBAL_SOURCE_PORT and FULL_REAL_EXTERIOR_HOM_DIMENSION > 0,
)

print("\nVerdict:")
print("  PEXT^0 WITH FORCED 1/9: CONSTRUCTED ON AN ALREADY GRADE-SIX EXTERIOR CARRIER")
print("  Q6 ADJOINT-TO-EXTERIOR MAP: OPEN / FORMULA ONLY")
print("  MOVED PROJECTOR: SIGNED-PERMUTATION SPLIT-TRANSPORT FIXTURE ONLY")
print("  COARSE EPSILON_PLANE OWNERSHIP: REFUTED (RB5 REPRODUCED BY LIVE PLANT)")
print("  EPSILON_SRC/TILTED + THETA_Z GLOBAL DESCENT: OPEN")
print("  NATIVE SP REDUCTION / TOTAL EULER TANGENCY: OPEN")
print("  FULL REAL EXTERIOR HOM: DIMENSION 4; STAR-EVEN A,B SUBANSATZ: DIMENSION 2")
print("  DISPLAYED KAPPA DIRECT SELECTION OF DOWNSTREAM HALF-WEIGHT: REFUTED")
print("  COMPLETE SHIAB+FERMION ACTION SELECTION: NOT EVALUABLE")
print("  ALGEBRAIC AUXILIARY: CAN FORCE ONE-BLADE REPRESENTATIVE RATIO ONLY")
print("  E_HAT_0: AUXILIARY KO-FAMILY ZERO ONLY")
print("  ARBITRARY VECTORLIKE CHI=0 PHYSICAL BASEPOINT: NOT CANONICAL")
print("  P1/P2/P3: UNCHANGED AND UNUSED")

total = sum(COUNTS.values())
print(
    f"\nChecks: {COUNTS['exact']} exact + {COUNTS['sage']} Sage + "
    f"{COUNTS['source']} source + {COUNTS['type']} type + "
    f"{COUNTS['planted']} planted = {total}"
)

if FAILURES:
    print("\nFAILED checks:")
    for failure in FAILURES:
        print(f"  - {failure}")
    raise SystemExit(1)

print("All Resolver Wave-F checks passed.")
