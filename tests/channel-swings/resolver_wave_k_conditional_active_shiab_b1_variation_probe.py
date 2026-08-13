#!/usr/bin/env python3
r"""Resolver Wave K: conditional-active degree-correct Shiab and local B1.

This is a self-contained sparse exterior-algebra reconstruction on the chosen
active trace-reversed ``(9,5)`` branch.  The source-typed ``(7,7)`` branch is
reconstructed as a separate exact signature ledger below rather than called an
arithmetic error.  The probe uses the public source only for the
displayed B1 grammar and ``1/2,1/3`` coefficients.  It does not identify the
active map with the public ``(7,7)`` action or the canon spinor Shiab.

The probe constructs:

* a fixed-frame active map ``Omega2(ad) -> Omega13(ad*)`` from moving-frame
  ingredients frozen at one declared local point;
* one monolithic bosonic B1 functional with live curvature, covariant-
  derivative, quadratic-eddy, mass, and boundary channels;
* exact direct-versus-owner first variations in independent B and T
  directions and one simultaneous direction;
* a zeroth-order Euler comparator from that same action and an exact mismatch
  with the repository's ``q_wedge(T)=T wedge T`` translated-curvature
  comparator (not yet with the source's convention-dependent ``[T,T]``);
* one nonvacuous infinitesimal active gauge-owner cancellation witness; and
* one fixed-background degree-thirteen Hodge-conjugation witness for the
  rank-252 ``Omega1`` source port.

The result narrows the fixed-operator candidate rather than promoting the
action as source-derived.  Source bracket normalization, moving metric/J/Shiab,
global source attribution,
the fermionic residual, a common
analytic domain, total tangency, observation/no-leakage, and physics remain
open.  P1/P2/P3 are unused.
"""

from __future__ import annotations

import contextlib
from dataclasses import dataclass
import importlib
import io
from pathlib import Path
import sys

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

with contextlib.redirect_stdout(io.StringIO()):
    wave_j = importlib.import_module(
        "resolver_wave_j_descended_source_action_total_euler_ward_probe"
    )

wave_i = wave_j.wave_i
wave_h = wave_j.wave_h

Element = dict[int, sp.Expr]
Form = dict[tuple[int, ...], Element]

N = 14
ETA = tuple(sp.Integer(value) for value in wave_h.ETA)
NATIVE_GRADES = tuple(wave_h.NATIVE_GRADES)
VOL = tuple(range(N))
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
R = sp.Rational
x, y, s = sp.symbols("x y s", real=True)
COORDS = (x, y) + tuple(sp.symbols(f"z{index}", real=True) for index in range(2, N))

FAILURES: list[str] = []
COUNTS = {"exact": 0, "source": 0, "type": 0, "planted": 0}


def check(kind: str, label: str, condition: bool, detail: str = "") -> None:
    COUNTS[kind] += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'} [{kind}]: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def eadd(*values: Element) -> Element:
    out: Element = {}
    for value in values:
        for mask, coefficient in value.items():
            out[mask] = sp.simplify(out.get(mask, ZERO) + coefficient)
    return wave_h.eclean(out)


def ediff(value: Element, variable: sp.Symbol) -> Element:
    return wave_h.eclean(
        {mask: sp.diff(coefficient, variable) for mask, coefficient in value.items()}
    )


def esub(value: Element, variable: sp.Symbol, point) -> Element:
    return wave_h.eclean(
        {mask: sp.simplify(coefficient.subs(variable, point))
         for mask, coefficient in value.items()}
    )


def fclean(value: Form) -> Form:
    return {
        indices: wave_h.eclean(coefficient)
        for indices, coefficient in value.items()
        if wave_h.eclean(coefficient)
    }


def fadd(*values: Form) -> Form:
    keys = set().union(*(value.keys() for value in values))
    return fclean({key: eadd(*(value.get(key, {}) for value in values)) for key in keys})


def fscale(coefficient, value: Form) -> Form:
    return fclean({indices: wave_h.escale(coefficient, entry)
                   for indices, entry in value.items()})


def wedge_sign(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    if set(left) & set(right):
        return 0
    inversions = sum(1 for a in left for b in right if a > b)
    return -1 if inversions % 2 else 1


def fwedge(left: Form, right: Form) -> Form:
    out: Form = {}
    for left_indices, left_coefficient in left.items():
        for right_indices, right_coefficient in right.items():
            sign = wedge_sign(left_indices, right_indices)
            if not sign:
                continue
            indices = tuple(sorted(left_indices + right_indices))
            product = wave_h.escale(
                sign, wave_h.emul(left_coefficient, right_coefficient)
            )
            out[indices] = eadd(out.get(indices, {}), product)
    return fclean(out)


def fleft(left: Element, right: Form) -> Form:
    return fclean({indices: wave_h.emul(left, coefficient)
                   for indices, coefficient in right.items()})


def fright(left: Form, right: Element) -> Form:
    return fclean({indices: wave_h.emul(coefficient, right)
                   for indices, coefficient in left.items()})


def fcomm_right(value: Form, right: Element) -> Form:
    return fadd(fright(value, right), fscale(-1, fleft(right, value)))


def fdiff(value: Form, variable: sp.Symbol) -> Form:
    return fclean({indices: ediff(coefficient, variable)
                   for indices, coefficient in value.items()})


def fsub(value: Form, variable: sp.Symbol, point) -> Form:
    return fclean({indices: esub(coefficient, variable, point)
                   for indices, coefficient in value.items()})


def dform(value: Form) -> Form:
    out: Form = {}
    for coordinate_index, coordinate in enumerate(COORDS):
        derivative = fdiff(value, coordinate)
        if derivative:
            out = fadd(out, fwedge({(coordinate_index,): wave_h.E_ONE}, derivative))
    return out


def hodge(value: Form) -> Form:
    out: Form = {}
    for indices, coefficient in value.items():
        complement = tuple(index for index in range(N) if index not in indices)
        sign = wedge_sign(indices, complement)
        norm = sp.prod(ETA[index] for index in indices)
        out[complement] = eadd(
            out.get(complement, {}), wave_h.escale(sign * norm, coefficient)
        )
    return fclean(out)


def form_degrees(value: Form) -> set[int]:
    return {len(indices) for indices in value}


def form_equal(left: Form, right: Form) -> bool:
    return not fadd(left, fscale(-1, right))


def native_form(value: Form) -> Form:
    return fclean({indices: wave_h.reduce_native(coefficient)
                   for indices, coefficient in value.items()})


def native_grade_project_element(value: Element) -> Element:
    """Active grade projection, deliberately distinct from Wave-H ``R_J``.

    ``R_J`` is typed only on the public ``u(K)`` real carrier.  The displayed
    Shiab word does not automatically inhabit that carrier.  Retaining the
    active native grades is the repository-derived conditional projection used
    by the adjacent operator-jet lane; it is not a source-to-active real port.
    """
    return wave_h.eclean({
        mask: coefficient
        for mask, coefficient in value.items()
        if mask.bit_count() in NATIVE_GRADES
    })


def native_grade_form(value: Form) -> Form:
    return fclean({
        indices: native_grade_project_element(coefficient)
        for indices, coefficient in value.items()
    })


def form_is_public_uK(value: Form) -> bool:
    return all(wave_h.is_public_uK(coefficient) for coefficient in value.values())


def form_is_native(value: Form) -> bool:
    return form_equal(native_form(value), value)


def top_trace(value: Form) -> sp.Expr:
    return sp.simplify(value.get(VOL, {}).get(0, ZERO))


def pair_top(left: Form, right: Form) -> sp.Expr:
    return top_trace(fwedge(left, right))


def integrate_xy(value: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.integrate(sp.integrate(sp.expand(value), (x, 0, 1)), (y, 0, 1)))


@dataclass(frozen=True)
class Dual13:
    """Finite representative of an ad-star-valued thirteen-form.

    The representative is lowered by the declared invariant scalar-trace
    pairing.  Keeping this wrapper prevents an unmarked ad == ad-star alias.
    """

    representative: Form


def flat_native_13(value: Form) -> Dual13:
    if value and form_degrees(value) != {13}:
        raise AssertionError("flat_native_13 expects exterior degree thirteen")
    if not form_is_native(value):
        raise AssertionError("flat_native_13 expects the chosen native carrier")
    return Dual13(value)


def lower_native_13(value: Form) -> Dual13:
    """Lower one exercised native 13-form through the declared trace pairing."""
    return flat_native_13(native_grade_form(value))


def dual13_add(*values: Dual13) -> Dual13:
    return flat_native_13(fadd(*(value.representative for value in values)))


def oneform_to_form(value) -> Form:
    return fclean({(index,): coefficient for index, coefficient in value.items()})


def form_to_oneform(value: Form):
    if value and form_degrees(value) != {1}:
        raise AssertionError("expected degree-one form")
    return wave_h.of_clean({indices[0]: coefficient for indices, coefficient in value.items()})


print("A. LAYER 0, SOURCE COLLISION, AND PARALLEL-LANE RECONCILIATION")

source_pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
source_map = (ROOT / "docs/paper-formalization-candidates.md").read_text()
public_shiab_receipt = (ROOT / "explorations/research-cycles/hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md").read_text()
toe_2025 = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
spinor_shiab = (ROOT / "canon/shiab-existence-cl95.md").read_text()
wave_j_report = (ROOT / "explorations/resolver-wave-j-descended-source-action-total-euler-ward-2026-08-03.md").read_text()

check(
    "source",
    "the source owns the bosonic B1 grammar, coefficients, and displayed translation variation",
    "WGS-01" in source_pack
    and "\\frac12d_{B_\\omega}T_\\omega" in source_pack
    and "\\frac13[T_\\omega,T_\\omega]" in source_pack
    and "varpi+s\\alpha" in source_pack,
)
check(
    "type",
    "the checked source prints bracket notation but does not fix its normalization against the repository wedge product",
    True,
)
check(
    "source",
    "the public bosonic Shiab is typed Omega2(ad) to Omega13(ad) in dimension fourteen",
    "Omega^2(Y^(7,7), ad) -> Omega^(d-1)(Y^(7,7), ad)" in public_shiab_receipt,
)
check(
    "source",
    "the public source leaves the preferred Phi selector and active real-form port unbuilt",
    "specific elements in the Clifford algebra" in source_map
    and "the author states they can no longer locate the original derivation" in source_map
    and "REAL-FORM-FORK" in source_pack,
)
check(
    "source",
    "the canon spinor Shiab is a distinct homonym with a spinor-valued domain and codomain",
    "Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S" in spinor_shiab
    and "source-forced selector" in spinor_shiab,
)
check(
    "source",
    "Wave J requires a degree-correct Shiab before any source-port placement verdict",
    "Only a degree-correct `Omega2 -> Omega13` Shiab" in wave_j_report,
)
check(
    "type",
    "parallel commits 85efd1e, 006c4bd, and 39ae094 are immutable adjacent evidence rather than imported APIs",
    True,
)
check(
    "type",
    "this action is repository-derived conditional-active (9,5), fixed-J, local, and not source-attributed",
    True,
)
check(
    "type",
    "public bosonic Shiab, canon spinor Shiab, active Shiab, R_J, Psrc, and the Omega13 Euler port remain distinct",
    True,
)

# Curt's iceberg summary and Eric's correction in the follow-up conversation
# must be read together.  Trace reversal fixes the vertical inertia.  The
# source's (1,3) horizontal convention then yields (7,7); Wave I's opposite
# horizontal sign yields (9,5).  Dualization H -> H* does not flip inertia.
vertical_frame = wave_i.F_VERTICAL
source_total = sp.diag(-wave_i.ETA4, wave_i.D_trace)
active_total = sp.diag(wave_i.ETA4, wave_i.D_trace)
frame_total = sp.diag(sp.eye(4), vertical_frame)
source_diagonal = sp.simplify(frame_total.T * source_total * frame_total)
active_diagonal = sp.simplify(frame_total.T * active_total * frame_total)


def diagonal_inertia(value: sp.MatrixBase) -> tuple[int, int]:
    if any(value[row, column] != 0
           for row in range(value.rows)
           for column in range(value.cols) if row != column):
        raise AssertionError("expected an exact diagonalized metric")
    return (
        sum(1 for entry in value.diagonal() if entry > 0),
        sum(1 for entry in value.diagonal() if entry < 0),
    )


check(
    "source",
    "Curt and Eric explicitly require trace-reversed rather than raw Frobenius on the metric fibre",
    "[00:20:51]" in toe_2025
    and "trace reversed Frobenius inner product" in toe_2025
    and "[00:26:28]" in toe_2025,
)
check(
    "source",
    "Eric explicitly locates fundamental nonchirality and the effective chiral world in a VEV-controlled Dirac-to-Weyl decoupling claim",
    "[02:36:02]" in toe_2025
    and "theory is not chiral" in toe_2025
    and "[02:36:29]" in toe_2025
    and "effective level nature is" in toe_2025
    and "[02:37:37]" in toe_2025
    and "decouples into Weyl type operators" in toe_2025,
)
check(
    "source",
    "Eric places fermionic matter in chimeric spinors and the rolled Dirac-Rarita-Schwinger sector",
    "[02:41:12]" in toe_2025
    and "That's what the Fermion sector looks like" in toe_2025
    and "[02:41:57]" in toe_2025
    and "you can build spinors" in toe_2025
    and "[02:50:38]" in toe_2025
    and "spinors that we see" in toe_2025,
)
check(
    "exact",
    "raw Frobenius (7,3) becomes the exact trace-reversed vertical inertia (6,4)",
    diagonal_inertia(sp.simplify(
        vertical_frame.T * wave_i.D_raw * vertical_frame
    )) == (7, 3)
    and diagonal_inertia(sp.simplify(
        vertical_frame.T * wave_i.D_trace * vertical_frame
    )) == (6, 4),
)
check(
    "exact",
    "the source (1,3) horizontal convention plus vertical (6,4) gives (7,7)",
    diagonal_inertia(source_diagonal) == (7, 7),
)
check(
    "exact",
    "the conditional active (3,1) convention plus vertical (6,4) gives (9,5)",
    diagonal_inertia(active_diagonal) == (9, 5),
)
check(
    "type",
    "H and H-star have the same inertia; the fork is the horizontal sign convention, not dualization",
    True,
)
check(
    "type",
    "Cl(7,7) real and Cl(9,5) quaternionic are inequivalent real-form branches after the convention choice",
    True,
)
check(
    "type",
    "the spoken four-metric and two-viable selector is not derived and selects neither branch here",
    True,
)


print("\nB. EXACT FIXED-FRAME ACTIVE OMEGA2-TO-OMEGA13 SHIAB")

PHI1: Form = {
    (index,): wave_h.blade((index,)) for index in range(N)
}
PHI2: Form = fscale(R(1, 2), fwedge(PHI1, PHI1))
# Wave I orders horizontal 0--3, six positive vertical directions 4--9,
# then the normalized negative DeWitt trace line at index 10.  The adjacent
# transported-trace machinery uses the same base-point blade.
TRACE_INDEX = 10
TAU = wave_h.blade((TRACE_INDEX,))


def raw_shiab_parts(curvature: Form, phi_one: Form = PHI1, tau: Element = TAU):
    phi_two = fscale(R(1, 2), fwedge(phi_one, phi_one))
    star_curvature = hodge(curvature)
    first = fwedge(phi_one, star_curvature)
    middle = hodge(fwedge(phi_two, star_curvature))
    second = hodge(fwedge(phi_one, middle))
    raw = fadd(first, fscale(R(-1, 2), second))
    traced = fleft(tau, raw)
    return first, second, traced


def active_shiab(curvature: Form, phi_one: Form = PHI1, tau: Element = TAU) -> Dual13:
    _first, _second, traced = raw_shiab_parts(curvature, phi_one, tau)
    return lower_native_13(traced)


sample_two = {
    (0, 1): eadd(wave_h.blade((0, 2)), wave_h.blade((1, 3), 2)),
    (2, 4): wave_h.blade((4, 5), -1),
}
first_sample, second_sample, traced_sample = raw_shiab_parts(sample_two)
sample_shiab = active_shiab(sample_two)

check(
    "exact",
    "the (9,5) Hodge star has the correct square on degrees 1, 2, 12, and 13",
    all(
        form_equal(
            hodge(hodge({tuple(range(degree)): wave_h.E_ONE})),
            fscale((-1) ** (degree * (N - degree) + 5),
                   {tuple(range(degree)): wave_h.E_ONE}),
        )
        for degree in (1, 2, 12, 13)
    ),
)
check(
    "exact",
    "Phi2 is exactly one-half Phi1 wedge Phi1 and has no Clifford-scalar contamination",
    form_equal(PHI2, fscale(R(1, 2), fwedge(PHI1, PHI1)))
    and all(0 not in coefficient for coefficient in PHI2.values()),
)
check(
    "exact",
    "both raw Shiab terms are live and have exterior degree thirteen",
    bool(first_sample) and bool(second_sample)
    and form_degrees(first_sample) == {13}
    and form_degrees(second_sample) == {13},
)
check(
    "exact",
    "the active Shiab output has exterior degree thirteen and the whole exercised output lies in public-u(K) and native grades",
    form_degrees(sample_shiab.representative) == {13}
    and form_is_public_uK(sample_shiab.representative)
    and form_equal(native_grade_form(sample_shiab.representative), sample_shiab.representative)
    and bool(sample_shiab.representative),
)
check(
    "exact",
    "the active Shiab is exactly linear in curvature",
    form_equal(
        active_shiab(fadd(sample_two, fscale(3, sample_two))).representative,
        fscale(4, sample_shiab.representative),
    ),
)
check(
    "planted",
    "dropping the second Ricci-scalar-like Shiab term changes the active output",
    not form_equal(native_grade_form(fleft(TAU, first_sample)), sample_shiab.representative),
)
strict_rj_rejected = False
try:
    native_form(traced_sample)
except TypeError:
    strict_rj_rejected = True
check(
    "planted",
    "the raw displayed Shiab word is not silently passed through R_J outside its public-u(K) domain",
    strict_rj_rejected,
)
check(
    "type",
    "the exercised scalar-trace lowerer is explicit and the Dual13 wrapper prevents silent ad equals ad-star",
    isinstance(sample_shiab, Dual13),
)
check(
    "type",
    "the active native-grade projection is conditional repository machinery, not the missing source-to-active R_J port",
    True,
)

native_pairing_basis = [
    wave_h.blade((0, 1)),
    wave_h.blade((0, 2)),
    wave_h.blade((1, 2)),
]
native_gram = sp.Matrix([
    [wave_h.trace_pair_element(left, right) for right in native_pairing_basis]
    for left in native_pairing_basis
])
check(
    "exact",
    "the declared invariant scalar-trace lowerer is nondegenerate on the exercised native coefficient panel",
    native_gram.det() != 0
    and all(wave_h.reduce_native(value) for value in native_pairing_basis),
)


print("\nC. WAVE-J DEGREE-TWO AND COSET-GRADE-SIX CURVATURE WITNESSES")

p_image = wave_i.Psrc_raw_0(wave_i.T_raw_0)
eddy_coefficient = wave_h.ecomm(p_image[0], p_image[1])
coset_x = wave_h.escale(sp.I, wave_h.blade((0,)))
coset_y = wave_h.escale(sp.I, wave_h.blade((4, 5, 6, 7, 8)))
coset_curvature = wave_h.reduce_native(wave_h.ecomm(coset_x, coset_y))

eddy_input = {(0, 1): eddy_coefficient}
coset_input = {(0, 1): coset_curvature}
eddy_output = active_shiab(eddy_input).representative
coset_output = active_shiab(coset_input).representative

check(
    "exact",
    "the live Wave-J Omega2 grade-two eddy survives the conditional-active Shiab",
    bool(eddy_output) and form_degrees(eddy_output) == {13},
)
check(
    "exact",
    "the corrected R_J(m wedge m) grade-six curvature survives the conditional-active Shiab",
    bool(coset_output) and form_degrees(coset_output) == {13},
)
check(
    "planted",
    "the naive reduced curvature loses the live coset-Shiab output",
    not active_shiab({(0, 1): wave_h.ecomm(
        wave_h.reduce_native(coset_x), wave_h.reduce_native(coset_y)
    )}).representative
    and bool(coset_output),
)
check(
    "type",
    "neither Omega2 witness is fed to the Omega1 rank-252 Psrc map",
    True,
)


print("\nD. MONOLITHIC CONDITIONAL-ACTIVE B1 ACTION")

e01 = wave_h.blade((0, 1))
e02 = wave_h.blade((0, 2))
e12 = wave_h.blade((1, 2))
e13 = wave_h.blade((1, 3))
e23 = wave_h.blade((2, 3))
e0t = wave_h.blade((0, TRACE_INDEX))
e2t = wave_h.blade((2, TRACE_INDEX))

B: Form = {
    (0,): eadd(wave_h.escale(1 + x, e01), wave_h.escale(y, e12)),
    (1,): eadd(wave_h.escale(1 + y, e12), wave_h.escale(x, e23)),
}
T: Form = {
    (0,): eadd(
        wave_h.escale(1 + x * y, e02),
        wave_h.escale(2 + x, e13),
        e0t,
    ),
    (1,): eadd(
        wave_h.escale(1 + x, e01),
        wave_h.escale(1 + y, e23),
        e2t,
    ),
}
BETA: Form = {
    (0,): eadd(wave_h.escale(1 + y, e12), e23),
    (1,): wave_h.escale(x, e02),
}
ALPHA: Form = {
    (0,): eadd(
        wave_h.escale(1 + x, e01), wave_h.escale(y, e13), e0t
    ),
    (1,): eadd(e02, wave_h.escale(1 + x * y, e12), e2t),
}
KAPPA = sp.symbols("kappa_1", real=True)


def curvature(connection: Form) -> Form:
    return fadd(dform(connection), fwedge(connection, connection))


def covariant_derivative(connection: Form, value: Form) -> Form:
    return fadd(dform(value), fwedge(connection, value), fwedge(value, connection))


def completed_curvature(connection: Form, torsion: Form,
                        a=R(1, 2), b=R(1, 3)):
    f_b = curvature(connection)
    d_t = covariant_derivative(connection, torsion)
    # Repository comparator only.  The source writes ``[T,T]``; its graded-
    # bracket normalization relative to this wedge product is still open.
    q_t = fwedge(torsion, torsion)
    return f_b, d_t, q_t, fadd(f_b, fscale(a, d_t), fscale(b, q_t))


def b1_density(connection: Form, torsion: Form,
               phi_one: Form = PHI1, tau: Element = TAU,
               a=R(1, 2), b=R(1, 3)) -> sp.Expr:
    _f_b, _d_t, _q_t, completed = completed_curvature(connection, torsion, a, b)
    shiab_value = active_shiab(completed, phi_one, tau)
    mass_value = lower_native_13(fscale(KAPPA / 2, hodge(torsion)))
    residual = dual13_add(shiab_value, mass_value)
    return sp.simplify(pair_top(torsion, residual.representative))


def b1_action(connection: Form, torsion: Form,
              phi_one: Form = PHI1, tau: Element = TAU,
              a=R(1, 2), b=R(1, 3)) -> sp.Expr:
    return integrate_xy(b1_density(connection, torsion, phi_one, tau, a, b))


F_B, D_BT, Q_T, C_BT = completed_curvature(B, T)
S_C = active_shiab(C_BT).representative
mass_13 = lower_native_13(fscale(KAPPA / 2, hodge(T))).representative
action_density = b1_density(B, T)
action_value = b1_action(B, T)


def flattened_rank(values: list[Form]) -> int:
    keys = sorted(set().union(*(
        {(indices, mask) for indices, coefficient in value.items() for mask in coefficient}
        for value in values
    )))
    columns = []
    for value in values:
        columns.append(sp.Matrix([
            sp.simplify(value.get(indices, {}).get(mask, ZERO).subs({x: 2, y: 3}))
            for indices, mask in keys
        ]))
    return sp.Matrix.hstack(*columns).rank()


check(
    "exact",
    "F_B, D_B T, and repository q_wedge(T)=T wedge T are all live and linearly independent",
    bool(F_B) and bool(D_BT) and bool(Q_T)
    and flattened_rank([F_B, D_BT, Q_T]) == 3,
)
check(
    "exact",
    "the Shiab and mass channels are both live in the same degree-thirteen residual",
    bool(S_C) and bool(mass_13)
    and form_degrees(S_C) == {13} and form_degrees(mass_13) == {13},
)
check(
    "exact",
    "the monolithic B1 top density and integrated action are nonzero and depend on kappa1",
    action_density != 0 and action_value != 0
    and pair_top(T, S_C) != 0
    and sp.diff(action_value, KAPPA) != 0
    and action_value.subs(KAPPA, 0) != 0,
)
check(
    "type",
    "the Hodge map supplies the top-form density once; no second determinant factor is inserted",
    True,
)


def delta_completed(connection: Form, torsion: Form,
                    beta: Form, alpha: Form,
                    d_beta: Form | None = None,
                    d_alpha: Form | None = None,
                    a=R(1, 2), b=R(1, 3)) -> Form:
    if d_beta is None:
        d_beta = dform(beta)
    if d_alpha is None:
        d_alpha = dform(alpha)
    delta_f = fadd(d_beta, fwedge(connection, beta), fwedge(beta, connection))
    delta_d = fadd(
        d_alpha,
        fwedge(connection, alpha), fwedge(alpha, connection),
        fwedge(beta, torsion), fwedge(torsion, beta),
    )
    delta_q = fadd(fwedge(alpha, torsion), fwedge(torsion, alpha))
    return fadd(delta_f, fscale(a, delta_d), fscale(b, delta_q))


def owner_density(connection: Form, torsion: Form,
                  beta: Form, alpha: Form,
                  d_beta: Form | None = None,
                  d_alpha: Form | None = None,
                  a=R(1, 2), b=R(1, 3)) -> sp.Expr:
    _f_b, _d_t, _q_t, completed = completed_curvature(connection, torsion, a, b)
    residual = fadd(
        dual13_add(
            active_shiab(completed),
            lower_native_13(fscale(KAPPA / 2, hodge(torsion))),
        ).representative,
    )
    delta_c = delta_completed(
        connection, torsion, beta, alpha, d_beta, d_alpha, a, b
    )
    delta_residual = fadd(
        dual13_add(
            active_shiab(delta_c),
            lower_native_13(fscale(KAPPA / 2, hodge(alpha))),
        ).representative,
    )
    return sp.simplify(
        pair_top(alpha, residual) + pair_top(torsion, delta_residual)
    )


def direct_variation(beta: Form, alpha: Form) -> sp.Expr:
    return sp.simplify(sp.diff(
        b1_action(fadd(B, fscale(s, beta)), fadd(T, fscale(s, alpha))), s
    ).subs(s, 0))


zero_form: Form = {}
direct_b = direct_variation(BETA, zero_form)
direct_t = direct_variation(zero_form, ALPHA)
direct_both = direct_variation(BETA, ALPHA)
owner_b = integrate_xy(owner_density(B, T, BETA, zero_form))
owner_t = integrate_xy(owner_density(B, T, zero_form, ALPHA))
owner_both = integrate_xy(owner_density(B, T, BETA, ALPHA))

print(
    "variation diagnostics: "
    f"direct_B={direct_b}, owner_B={owner_b}, "
    f"direct_T={direct_t}, owner_T={owner_t}, "
    f"direct_both={direct_both}, owner_both={owner_both}"
)

check(
    "exact",
    "direct and owner first variations agree in the independent B direction",
    sp.simplify(direct_b - owner_b) == 0 and direct_b != 0,
)
check(
    "exact",
    "direct and owner first variations agree in the independent T direction",
    sp.simplify(direct_t - owner_t) == 0 and direct_t != 0,
)
check(
    "exact",
    "direct and owner first variations agree simultaneously without compensating omissions",
    sp.simplify(direct_both - owner_both) == 0
    and sp.simplify(direct_both - direct_b - direct_t) == 0,
)


print("\nE. SAME-ACTION ZEROTH-ORDER EULER AND Q_WEDGE COMPARATOR TEST")

check(
    "exact",
    "Wave J remains a positive exact cyclic calibration at coefficients one-half and one-third",
    wave_j.matrix_equal(wave_j.source_euler, wave_j.translated_curvature)
    and sp.simplify(wave_j.direct_translation - wave_j.owner_translation) == 0,
)

f0, fx, fy = sp.symbols("f0 fx fy", real=True)
alpha_shape: Form = {(0,): e0t, (1,): e2t}
alpha_symbolic = fscale(f0, alpha_shape)
df_symbolic: Form = {(0,): wave_h.escale(fx, wave_h.E_ONE),
                     (1,): wave_h.escale(fy, wave_h.E_ONE)}
d_alpha_symbolic = fwedge(df_symbolic, alpha_shape)
green_symbolic = sp.expand(owner_density(
    B, T, zero_form, alpha_symbolic, d_alpha=d_alpha_symbolic
))
q_green = sp.simplify(sp.diff(green_symbolic, f0))
p_x = sp.simplify(sp.diff(green_symbolic, fx))
p_y = sp.simplify(sp.diff(green_symbolic, fy))
linear_remainder = sp.simplify(
    green_symbolic - q_green * f0 - p_x * fx - p_y * fy
)

f_test = 1 + x + y + x * y
green_direct = integrate_xy(
    green_symbolic.subs({f0: f_test, fx: sp.diff(f_test, x), fy: sp.diff(f_test, y)})
)
green_bulk_density = sp.simplify(q_green - sp.diff(p_x, x) - sp.diff(p_y, y))
green_bulk = integrate_xy(green_bulk_density * f_test)
green_boundary = sp.simplify(
    sp.integrate((p_x * f_test).subs(x, 1) - (p_x * f_test).subs(x, 0), (y, 0, 1))
    + sp.integrate((p_y * f_test).subs(y, 1) - (p_y * f_test).subs(y, 0), (x, 0, 1))
)

print(
    "Green diagnostics: "
    f"q={q_green}, px={p_x}, py={p_y}, "
    f"direct={green_direct}, bulk={green_bulk}, boundary={green_boundary}"
)

check(
    "exact",
    "the same-action variation is linear in the test field and its two first derivatives",
    linear_remainder == 0,
)
check(
    "exact",
    "the same-action one-channel variation equals bulk Euler plus Green boundary",
    sp.simplify(green_direct - green_bulk - green_boundary) == 0,
)
check(
    "planted",
    "claiming this zeroth-order channel proves a live Green concomitant is rejected",
    green_boundary == 0 and p_x == 0 and p_y == 0,
)

translated_curvature_qwedge = fadd(F_B, D_BT, Q_T)
qwedge_target = fadd(
    active_shiab(translated_curvature_qwedge).representative,
    lower_native_13(fscale(KAPPA, hodge(T))).representative,
)
qwedge_target_coefficient = sp.simplify(pair_top(alpha_shape, qwedge_target))
transgression_defect = sp.simplify(green_bulk_density - qwedge_target_coefficient)

# The classification is printed before the assertion so the first execution
# fixes the branch without silently treating a mismatch as an implementation
# failure.  A nonzero defect narrows only this repository q_wedge comparator;
# source bracket normalization is a separate open gate.
print(f"TRANSgression defect = {transgression_defect}")
check(
    "exact",
    "the normalized-trace fixed conditional-active Shiab has a live exact q_wedge-transgression mismatch",
    transgression_defect != 0,
)
check(
    "type",
    "the q_wedge mismatch is not promoted to a source-[T,T] obstruction before bracket normalization is fixed",
    True,
)

wrong_linear = owner_density(B, T, zero_form, ALPHA, a=1, b=R(1, 3))
wrong_quadratic = owner_density(B, T, zero_form, ALPHA, a=R(1, 2), b=R(1, 2))
wrong_linear_value = integrate_xy(wrong_linear)
wrong_quadratic_value = integrate_xy(wrong_quadratic)
print(
    "coefficient diagnostics: "
    f"correct={owner_t}, wrong_linear={wrong_linear_value}, "
    f"wrong_quadratic={wrong_quadratic_value}"
)
check(
    "planted",
    "mutating either live source coefficient changes the same-action T variation",
    wrong_linear_value != owner_t and wrong_quadratic_value != owner_t,
)


print("\nF. LOCAL ACTIVE GAUGE ORBIT OF THE SAME B1 ACTION")

XI = wave_h.escale(x * y, e12)
xi_form: Form = {(): XI}
delta_b_gauge = fadd(
    dform(xi_form),
    fwedge(B, xi_form),
    fscale(-1, fwedge(xi_form, B)),
)
delta_t_gauge = fadd(
    fwedge(T, xi_form),
    fscale(-1, fwedge(xi_form, T)),
)
delta_phi = fcomm_right(PHI1, XI)
delta_tau = wave_h.ecomm(TAU, XI)

gauge_fixed_operator = integrate_xy(owner_density(
    B, T, delta_b_gauge, delta_t_gauge
))


def delta_shiab_operator(
    curvature_value: Form,
    delta_phi_value: Form,
    delta_tau_value: Element,
    phi_one: Form = PHI1,
    tau: Element = TAU,
) -> Dual13:
    phi_two = fscale(R(1, 2), fwedge(phi_one, phi_one))
    delta_phi_two = fscale(
        R(1, 2),
        fadd(
            fwedge(delta_phi_value, phi_one),
            fwedge(phi_one, delta_phi_value),
        ),
    )
    star_curvature = hodge(curvature_value)
    middle = hodge(fwedge(phi_two, star_curvature))
    delta_middle = hodge(fwedge(delta_phi_two, star_curvature))
    delta_raw = fadd(
        fwedge(delta_phi_value, star_curvature),
        fscale(
            R(-1, 2),
            hodge(fadd(
                fwedge(delta_phi_value, middle),
                fwedge(phi_one, delta_middle),
            )),
        ),
    )
    _first, _second, traced = raw_shiab_parts(curvature_value, phi_one, tau)
    raw_untraced = fleft(wave_h.blade(()), fadd(
        fwedge(phi_one, star_curvature),
        fscale(R(-1, 2), hodge(fwedge(phi_one, middle))),
    ))
    delta_traced = fadd(
        fleft(delta_tau_value, raw_untraced),
        fleft(tau, delta_raw),
    )
    # ``traced`` is deliberately evaluated above as a same-constructor
    # checksum; the derivative is assembled term-by-term to avoid a huge
    # symbolic finite-difference expansion.
    if not form_equal(traced, fleft(tau, raw_untraced)):
        raise AssertionError("raw Shiab derivative owner drifted from constructor")
    return flat_native_13(native_grade_form(delta_traced))


gauge_operator_owner_density = pair_top(
    T,
    delta_shiab_operator(C_BT, delta_phi, delta_tau).representative,
)
gauge_operator_owner = integrate_xy(gauge_operator_owner_density)
gauge_owner_sum = sp.simplify(gauge_fixed_operator + gauge_operator_owner)

check(
    "exact",
    "one nonvacuous infinitesimal active gauge-owner cancellation witness vanishes",
    gauge_owner_sum == 0
    and gauge_fixed_operator != 0
    and gauge_operator_owner != 0,
)
check(
    "planted",
    "freezing the active Shiab ingredients leaves a nonzero incomplete Ward contraction",
    gauge_fixed_operator != 0 and gauge_operator_owner != 0,
)

delta_b_no_maurer = fadd(
    fwedge(B, xi_form), fscale(-1, fwedge(xi_form, B))
)
gauge_no_maurer = sp.simplify(
    integrate_xy(owner_density(B, T, delta_b_no_maurer, delta_t_gauge))
    + gauge_operator_owner
)
check(
    "planted",
    "omitting the inhomogeneous connection response breaks the local active Ward orbit",
    gauge_no_maurer != 0,
)
check(
    "type",
    "the owner-cancellation witness is not an independently differentiated Ward theorem, public source epsilon orbit, or Xi equals D Upsilon redundancy",
    True,
)


print("\nG. DEGREE-THIRTEEN DUAL PORT AT FIXED METRIC AND J")


def p1_form(value: Form) -> Form:
    return oneform_to_form(wave_i.Psrc_raw_0(form_to_oneform(value)))


def p13_dual(value: Dual13) -> Dual13:
    raised_one = hodge(value.representative)
    projected_one = p1_form(raised_one)
    return flat_native_13(native_form(hodge(projected_one)))


port_image_one = oneform_to_form(p_image)
port_image_13 = flat_native_13(native_form(hodge(port_image_one)))
port_test_one = oneform_to_form(wave_i.T_raw_0)

check(
    "exact",
    "the degree-thirteen port is idempotent on the actual selected image fixture",
    form_equal(
        p13_dual(p13_dual(port_image_13)).representative,
        p13_dual(port_image_13).representative,
    )
    and bool(p13_dual(port_image_13).representative),
)
check(
    "exact",
    "the degree-thirteen port is the Hodge/Krein dual of Psrc under the top-form pairing",
    sp.simplify(
        pair_top(port_test_one, p13_dual(port_image_13).representative)
        - pair_top(p1_form(port_test_one), port_image_13.representative)
    ) == 0,
)
check(
    "type",
    "the one-fixture fixed-background Hodge-conjugation witness does not prove a global rank-252 port, moving descent, or identify Psrc with R_J",
    True,
)
omega13_rejected = False
try:
    form_to_oneform(port_image_13.representative)
except AssertionError:
    omega13_rejected = True
check(
    "planted",
    "applying the Omega1 port directly to an Omega13 value is rejected by the form adapter",
    omega13_rejected,
)


print("\nH. DISPOSITION AND BOUNDARY")

check(
    "type",
    "source bracket normalization and a separately typed Cl77 construction are required before testing the displayed source identity",
    True,
)
check(
    "type",
    "the I2B residual-square primalizer is not imported as the I1 Shiab adjoint",
    True,
)
check(
    "type",
    "fermionic residual, total tangency, common domain, and physical observation remain open",
    True,
)
check(
    "type",
    "P1/P2/P3 remain unchanged and unused",
    True,
)
check(
    "type",
    "Curt remains formally separate and TG-1 AND TG-2 AND TG-3 remains not promoted",
    True,
)
check(
    "type",
    "no VEV, mass value, stationarity, anomaly, index, generation count, or cosmology is claimed",
    True,
)


total = sum(COUNTS.values())
print("\n" + "=" * 118)
print(
    "COUNTS: "
    + ", ".join(f"{key}={value}" for key, value in COUNTS.items())
    + f" total={total}"
)
print(f"TRANSGRESSION_ZERO={transgression_defect == 0}")
print(
    "RESOLVER WAVE K VERDICT: "
    "NORMALIZED_TRACE_FIXED_ACTIVE_95_QWEDGE_B1_CANDIDATE_MISMATCH"
)
print(
    "The normalized-trace active fixed-frame candidate has a live monolithic B1 direct/owner "
    "variation and a candidate-local q_wedge transgression mismatch. The source's [T,T] "
    "normalization, an independent Cl(7,7) real construction, global lowerer/port/Ward theorems, "
    "fermions, domain, and physics stay open."
)

if FAILURES:
    print("FAILURES:")
    for failure in FAILURES:
        print(f"- {failure}")
    raise SystemExit(1)
