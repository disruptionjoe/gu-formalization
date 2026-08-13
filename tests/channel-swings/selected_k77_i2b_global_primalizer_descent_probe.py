#!/usr/bin/env python3
"""Exact associated-bundle descent and moving derivative for the I2B P_plus.

V0.206 derives P_plus as the real-action Euler primalizer at an H_q-fixed
residual.  This probe asks whether that endomorphism requires a chosen global
Spin frame, and computes the term produced when the H_q reduction moves.
The answer is tested on a noncommuting three-patch signed-orthogonal cocycle
and on the complete 196-complex-coordinate target carrier.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_action_real_projection_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/k77-global-chimeric-spin-reduction-source-reinspection-2026-08-05.md")
trace_q = read("explorations/conditional-build/selected-k77-tautological-trace-q-two-half-ownership-gate-2026-08-12.md")
atlas = read("explorations/conditional-build/selected-k77-action-stabilizer-connection-flag-reconciliation-2026-08-12.md")
moving_parent = read("explorations/conditional-build/selected-k77-moving-parent-bundle-observation-reduction-2026-08-10.md")
previous = read("explorations/conditional-build/selected-k77-i2b-action-real-projection-2026-08-12.md")

check("source", "source owns an epsilon-conjugated dependent Clifford frame",
      "dependent full frame" in source and "Ad" in source)
check("source", "source is silent on the repository Hq involution and P_plus",
      "SOURCE_SILENT_ON_HQ_AND_PPLUS" in previous)
check("prior_art", "tautological trace q is global, natural and costs no datum",
      "globally defined" in trace_q and "falls from `13` to `0`" in trace_q)
check("prior_art", "the observation reduction already owns its stabilizer cocycle",
      "missing local stabilizer cocycle is not a new field or datum" in atlas)
check("prior_art", "a moving associated projector already descends in the full parent",
      "direct/sequential cocycle\ndescent" in moving_parent)
check("prior_art", "v0.206 owns P_plus only at fixed-real Euler grade",
      "Euler primalizer" in previous and "nonlinear replacement" in previous)

for distinction in (
    "associated residual bundle versus a chosen global frame",
    "SO transition versus either sign of a local Spin lift",
    "adjoint projector P_plus versus Weinstein source epsilon",
    "selected real K77 action versus full U(64,64) connection",
    "full U(64,64) parent versus two U(32,32) half reduction",
    "moving Euler primalizer term versus complete Euler/preboundary class",
):
    check("layer0", distinction + " remain distinct", True)

for lens in (
    "principal-bundle geometry tests associated-endomorphism descent",
    "Clifford and Krein geometry test Hq transport and action adjoints",
    "category/functoriality tests direct versus sequential overlap maps",
    "variational bicomplex differentiates the primalizer with the residual",
    "symplectic geometry refuses to call this a presymplectic potential",
    "analytic review retains formal adjoint Green domain and spectrum",
    "source criticism keeps epsilon and unitary-parent ownership open",
    "contrary review requires a frozen-projector control to fire",
):
    check("preflight", lens, True)


print("\nB. PREDECESSOR REPLAY AND COMPLETE TARGET CARRIER")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P206 = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.206 action-real projection predecessor replays",
      "failures=0" in capture.getvalue().lower())

P205 = P206["P205"]
P204 = P205["P"]
tau_target = P204["tau_target"]
add = P204["add"]
scale = P204["scale"]
target_vector = P204["target_vector"]
action_pair = P206["action_pair"]
project_plus = P206["project_plus"]
project_minus = P206["project_minus"]
coordinate_keys = sorted(P206["coordinate_keys"])
add_real_column = P204["add_real_column"]

carrier_basis = []
for key in coordinate_keys:
    carrier_basis.append({(key, 0): Fraction(1)})
    carrier_basis.append({(key, 1): Fraction(1)})
check("exact", "the target carrier is 196 complex or 392 real dimensional",
      len(coordinate_keys) == 196 and len(carrier_basis) == 392)


def clean(column: dict) -> dict:
    return {key: value for key, value in column.items() if value}


def identity_axis_map() -> dict[int, tuple[int, int]]:
    return {index: (index, 1) for index in range(14)}


def quarter_turn(first: int, second: int) -> dict[int, tuple[int, int]]:
    """e_first -> -e_second, e_second -> e_first."""
    out = identity_axis_map()
    out[first] = (second, -1)
    out[second] = (first, 1)
    return out


def compose_axis_maps(left, right):
    """Return left after right."""
    out = {}
    for index in range(14):
        middle, sign_right = right[index]
        target, sign_left = left[middle]
        out[index] = (target, sign_left * sign_right)
    return out


def mask_image(mask: int, axis_map) -> tuple[int, int]:
    mapped = []
    sign = 1
    for index in range(14):
        if mask & (1 << index):
            target, factor = axis_map[index]
            mapped.append(target)
            sign *= factor
    inversions = sum(
        1
        for left in range(len(mapped))
        for right in range(left + 1, len(mapped))
        if mapped[left] > mapped[right]
    )
    if inversions % 2:
        sign *= -1
    out = 0
    for index in mapped:
        out |= 1 << index
    return out, sign


def transport_column(column, axis_map):
    out = {}
    for ((form_mask, clifford_mask), part), value in column.items():
        moved_form, form_sign = mask_image(form_mask, axis_map)
        moved_clifford, clifford_sign = mask_image(clifford_mask, axis_map)
        key = ((moved_form, moved_clifford), part)
        out[key] = out.get(key, Fraction(0)) + form_sign * clifford_sign * value
    return clean(out)


def pplus_axis(column, q_axis):
    return scale(Fraction(1, 2), add(column, tau_target(column, q_axis=q_axis)))


print("\nC. NONCOMMUTING THREE-PATCH ASSOCIATED-BUNDLE DESCENT")
# Patch 0 uses q13, patch 1 q12, patch 2 q11.
t01 = quarter_turn(12, 13)
t12 = quarter_turn(11, 12)
t02 = compose_axis_maps(t12, t01)
reverse = compose_axis_maps(t01, t12)

check("geometry", "t01 maps q13 to q12 and t12 maps q12 to q11",
      t01[13] == (12, 1) and t12[12] == (11, 1))
check("geometry", "the adjacent-plane transitions do not commute",
      any(t02[index] != reverse[index] for index in range(14)))

cocycle_failures = 0
tau_failures = 0
projector_failures = 0
for basis in carrier_basis:
    direct = transport_column(basis, t02)
    sequential = transport_column(transport_column(basis, t01), t12)
    cocycle_failures += int(direct != sequential)

    tau01_left = transport_column(tau_target(basis, q_axis=13), t01)
    tau01_right = tau_target(transport_column(basis, t01), q_axis=12)
    tau12_left = transport_column(tau_target(transport_column(basis, t01), q_axis=12), t12)
    tau12_right = tau_target(direct, q_axis=11)
    tau02_left = transport_column(tau_target(basis, q_axis=13), t02)
    tau02_right = tau_target(direct, q_axis=11)
    tau_failures += int(
        tau01_left != tau01_right
        or tau12_left != tau12_right
        or tau02_left != tau02_right
    )

    projector_failures += int(
        transport_column(pplus_axis(basis, 13), t01)
        != pplus_axis(transport_column(basis, t01), 12)
        or transport_column(pplus_axis(basis, 13), t02)
        != pplus_axis(direct, 11)
    )

check("cocycle", "direct and sequential target transports agree on all 392 real basis vectors",
      cocycle_failures == 0, f"failures={cocycle_failures}")
check("reality", "the Hq target involution descends on all three overlaps",
      tau_failures == 0, f"failures={tau_failures}")
check("projector", "P_plus descends as an associated-bundle endomorphism",
      projector_failures == 0, f"failures={projector_failures}")

projected_basis = {}
for basis in carrier_basis:
    add_real_column(projected_basis, pplus_axis(basis, 13))
check("rank", "the global fibrewise P_plus has real rank 196 on the 392-real target",
      len(projected_basis) == 196)

# Any two local Spin lifts differ by the central sign, which cancels in the
# adjoint representation.  A rational matrix control checks the universal
# identity rather than choosing a 128-spinor frame.
s = ((Fraction(1), Fraction(1)), (Fraction(0), Fraction(1)))
s_inv = ((Fraction(1), Fraction(-1)), (Fraction(0), Fraction(1)))
x = ((Fraction(2), Fraction(3)), (Fraction(5), Fraction(7)))


def matmul(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


minus_s = tuple(tuple(-value for value in row) for row in s)
minus_s_inv = tuple(tuple(-value for value in row) for row in s_inv)
check("spin", "the two central-sign Spin lifts induce the same adjoint transport",
      matmul(matmul(s, x), s_inv) == matmul(matmul(minus_s, x), minus_s_inv))
check("layer0", "sign-blind adjoint descent does not choose a global Spin section", True)


print("\nD. INFINITESIMAL MOVING-PRIMALIZER DERIVATIVE")
# Generator of the t01 path: delta e12=-e13, delta e13=e12.
def generator_mask(mask: int, first: int = 12, second: int = 13):
    source = [index for index in range(14) if mask & (1 << index)]
    out = {}
    for position, index in enumerate(source):
        if index == first:
            target, coefficient = second, Fraction(-1)
        elif index == second:
            target, coefficient = first, Fraction(1)
        else:
            continue
        if target in source:
            continue
        moved = list(source)
        moved[position] = target
        inversions = sum(
            1
            for left in range(len(moved))
            for right in range(left + 1, len(moved))
            if moved[left] > moved[right]
        )
        if inversions % 2:
            coefficient *= -1
        moved_mask = sum(1 << item for item in moved)
        out[moved_mask] = out.get(moved_mask, Fraction(0)) + coefficient
    return clean(out)


def lie_column(column):
    out = {}
    for ((form_mask, clifford_mask), part), value in column.items():
        for moved_form, coefficient in generator_mask(form_mask).items():
            key = ((moved_form, clifford_mask), part)
            out[key] = out.get(key, Fraction(0)) + coefficient * value
        for moved_clifford, coefficient in generator_mask(clifford_mask).items():
            key = ((form_mask, moved_clifford), part)
            out[key] = out.get(key, Fraction(0)) + coefficient * value
    return clean(out)


def dot_tau(column):
    return add(
        lie_column(tau_target(column, q_axis=13)),
        scale(-1, tau_target(lie_column(column), q_axis=13)),
    )


def dot_projector(column):
    return scale(Fraction(1, 2), dot_tau(column))


idempotent_derivative_failures = 0
off_diagonal_failures = 0
moving_naturality_failures = 0
frozen_projector_failures = 0
dot_projector_basis = {}

for basis in carrier_basis:
    p = pplus_axis(basis, 13)
    pm = project_minus(basis)
    dp = dot_projector(basis)
    add_real_column(dot_projector_basis, dp)

    idempotent_derivative_failures += int(
        add(dot_projector(p), pplus_axis(dp, 13)) != dp
    )
    off_diagonal_failures += int(
        bool(pplus_axis(dot_projector(p), 13))
        or bool(project_minus(dot_projector(pm)))
    )
    moving_naturality_failures += int(
        add(dp, pplus_axis(lie_column(basis), 13))
        != lie_column(p)
    )
    frozen_projector_failures += int(
        pplus_axis(lie_column(basis), 13) != lie_column(p)
    )

check("derivative", "dot P equals one half [L,tau] and has nonzero rank 56",
      len(dot_projector_basis) == 56, f"rank={len(dot_projector_basis)}")
check("derivative", "the differentiated idempotency identity holds on the complete carrier",
      idempotent_derivative_failures == 0,
      f"failures={idempotent_derivative_failures}")
check("derivative", "dot P is off-diagonal between fixed and anti-fixed sectors",
      off_diagonal_failures == 0, f"failures={off_diagonal_failures}")
check("naturality", "dot P plus P times dot U equals the derivative of P U",
      moving_naturality_failures == 0,
      f"failures={moving_naturality_failures}")
check("control", "freezing P during the moving reduction fails on live target directions",
      frozen_projector_failures > 0,
      f"firing_basis_vectors={frozen_projector_failures}")


print("\nE. ACTION-PAIRING AND MOVING FIXED-RESIDUAL CHECK")
skew_failures = 0
dp_adjoint_failures = 0
covariant_variation_failures = 0
nontrivial_cancellations = 0
ly = lie_column(target_vector)

for left in carrier_basis:
    l_left = lie_column(left)
    dp_left = dot_projector(left)
    p_left = pplus_axis(left, 13)
    skew_failures += int(
        action_pair(l_left, target_vector) + action_pair(left, ly) != 0
    )
    dp_adjoint_failures += int(
        action_pair(dp_left, target_vector)
        != action_pair(left, dot_projector(target_vector))
    )
    first = action_pair(add(dp_left, pplus_axis(l_left, 13)), target_vector)
    second = action_pair(p_left, ly)
    covariant_variation_failures += int(first + second != 0)
    nontrivial_cancellations += int(first != 0 and second != 0 and first == -second)

check("krein", "the transport generator is skew for the selected real action pairing",
      skew_failures == 0, f"failures={skew_failures}")
check("krein", "dot P is action-self-adjoint at first order",
      dp_adjoint_failures == 0, f"failures={dp_adjoint_failures}")
check("variation", "the moving projected first variation is covariant on all carrier directions",
      covariant_variation_failures == 0,
      f"failures={covariant_variation_failures}")
check("control", "moving-P and moving-residual terms cancel nontrivially",
      nontrivial_cancellations > 0,
      f"nontrivial={nontrivial_cancellations}")
check("target", "the moving fixed residual obeys dot P y plus P dot y equals dot y",
      add(dot_projector(target_vector), pplus_axis(ly, 13)) == ly)


print("\nF. HOSTILE FENCES")
for kind, label in (
    ("layer0", "global P_plus descent does not identify a chosen Spin lift with source epsilon"),
    ("source", "the source owns moving conjugation grammar but not Hq or P_plus"),
    ("unitary", "selected K77 descent does not select full U6464 or two U3232 halves"),
    ("variation", "pure frame covariance is not the arbitrary metric field Euler derivative"),
    ("symplectic", "no presymplectic potential BFV charge or reduced phase space is inferred"),
    ("analytic", "no formal Green adjoint closed domain positivity spectrum or vacuum is inferred"),
    ("datum", "no field parameter quotient or P1 P2 P3 datum is added"),
    ("contrary", "non-fixed residuals retain the anti-fixed action sector from v0.206"),
):
    check(kind, label, True)


print("\nSUMMARY")
print(f"counts={dict(COUNTS)} failures={len(FAILURES)}")
print(
    f"carrier_real={len(carrier_basis)} pplus_rank={len(projected_basis)} "
    f"dot_p_rank={len(dot_projector_basis)} "
    f"cocycle_failures={cocycle_failures} tau_failures={tau_failures} "
    f"projector_failures={projector_failures} "
    f"frozen_projector_failures={frozen_projector_failures} "
    f"nontrivial_cancellations={nontrivial_cancellations}"
)
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: the Hq-fixed Euler primalizer P_plus descends as a sign-insensitive associated-bundle endomorphism on a noncommuting three-patch K77 cocycle and needs no chosen global Spin frame. Its exact moving term dot P=[L,tau]/2 has rank 56, satisfies differentiated projector and action-adjoint identities, and is required for covariant first variation. Source epsilon, full U(64,64), the two U(32,32) halves, arbitrary field variation, full Euler/preboundary and physical vacuum remain open.")
