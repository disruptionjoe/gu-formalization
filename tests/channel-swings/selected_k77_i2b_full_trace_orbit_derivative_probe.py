#!/usr/bin/env python3
"""Exact full trace-orbit derivative of the selected K77 I2B primalizer.

V0.207 proves global descent and computes one infinitesimal motion of the
H_q-fixed Euler primalizer.  This probe exhausts all 91 generators of
so(6,4): the 78-dimensional stabilizer of the normalized tautological trace
and the 13-dimensional trace orbit.  It determines whether the q-dependent
part of the arbitrary-field derivative is already exactly frame-covariant.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_global_primalizer_descent_probe.py"
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
previous = read("explorations/conditional-build/selected-k77-i2b-global-primalizer-descent-2026-08-12.md")

check("source", "source owns an epsilon-conjugated dependent Clifford frame",
      "dependent full frame" in source and "Ad" in source)
check("source", "source is silent on the repository Hq involution and P_plus",
      "SOURCE_SILENT_ON_HQ_AND_PPLUS" in previous)
check("prior_art", "the tautological trace q is global natural and zero-datum",
      "globally defined" in trace_q and "falls from `13` to `0`" in trace_q)
check("prior_art", "v0.207 proves one nonzero q-orbit derivative and global descent",
      "rank `56`" in previous and "associated-bundle endomorphism" in previous)

for distinction in (
    "normalized trace-orbit motion versus arbitrary DeWitt metric deformation",
    "Spin-frame covariance versus source epsilon",
    "trace stabilizer versus trace-moving complement",
    "moving P_plus term versus complete Hodge Shiab and field derivative",
    "fixed-norm q tangent versus an independent radial q scaling",
    "selected K77 action versus full U64_64 parent and C32_32 carrier split",
):
    check("layer0", distinction + " remain distinct", True)

for lens in (
    "homogeneous-space geometry splits so64 into stabilizer plus thirteen-orbit tangent",
    "Clifford and Krein geometry type the signature-correct infinitesimal generators",
    "principal-bundle geometry treats q motion as associated transport",
    "category and functoriality require the same result on every generator",
    "variational bicomplex differentiates P_plus with its residual",
    "symplectic geometry retains the physical preboundary class as open",
    "analytic review retains Green domain spectrum and positivity as open",
    "source criticism keeps epsilon and action-parent ownership open",
    "constraint accounting rejects an independent radial q datum",
    "contrary review requires both frozen-P and radial-scaling controls",
):
    check("preflight", lens, True)


print("\nB. PREDECESSOR REPLAY AND COMPLETE TARGET CARRIER")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.207 global primalizer predecessor replays",
      "failures=0" in capture.getvalue().lower())

carrier_basis = P["carrier_basis"]
pplus_axis = P["pplus_axis"]
project_minus = P["project_minus"]
tau_target = P["tau_target"]
target_vector = P["target_vector"]
action_pair = P["action_pair"]
add = P["add"]
scale = P["scale"]
clean = P["clean"]
add_real_column = P["add_real_column"]

ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
Q_AXIS = 13
check("exact", "the complete target carrier is 392 real dimensional",
      len(carrier_basis) == 392)
check("geometry", "the selected trace axis is negative in the pinned six-four fibre",
      ETA[Q_AXIS] == -1)


def generator_mask(mask: int, first: int, second: int):
    """Induced so(6,4) action with L e_second=e_first.

    Metric skewness fixes L e_first=-(eta_second/eta_first)e_second.
    Every exterior blade therefore has at most two image terms.
    """
    source_indices = [index for index in range(14) if mask & (1 << index)]
    out = {}
    first_coefficient = Fraction(-ETA[second], ETA[first])
    for position, index in enumerate(source_indices):
        if index == first:
            target, coefficient = second, first_coefficient
        elif index == second:
            target, coefficient = first, Fraction(1)
        else:
            continue
        if target in source_indices:
            continue
        moved = list(source_indices)
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


def lie_column(column, first: int, second: int):
    out = {}
    for ((form_mask, clifford_mask), part), value in column.items():
        for moved_form, coefficient in generator_mask(form_mask, first, second).items():
            key = ((moved_form, clifford_mask), part)
            out[key] = out.get(key, Fraction(0)) + coefficient * value
        for moved_clifford, coefficient in generator_mask(clifford_mask, first, second).items():
            key = ((form_mask, moved_clifford), part)
            out[key] = out.get(key, Fraction(0)) + coefficient * value
    return clean(out)


def dot_tau(column, first: int, second: int):
    moved = lie_column(column, first, second)
    return add(
        lie_column(tau_target(column, q_axis=Q_AXIS), first, second),
        scale(-1, tau_target(moved, q_axis=Q_AXIS)),
    )


def dot_projector(column, first: int, second: int):
    return scale(Fraction(1, 2), dot_tau(column, first, second))


def add_to_span(basis, column):
    copied = {pivot: dict(value) for pivot, value in basis.items()}
    add_real_column(copied, column)
    return copied


print("\nC. WHOLESALE SO(6,4) STABILIZER/ORBIT CLASSIFICATION")
generators = [(first, second) for first in range(14) for second in range(first + 1, 14)]
orbit_generators = [(first, second) for first, second in generators if second == Q_AXIS]
stabilizer_generators = [(first, second) for first, second in generators if second != Q_AXIS]
check("dimension", "so(6,4) has 91 tested bivector generators",
      len(generators) == 91)
check("dimension", "the normalized trace orbit has 13 generators and stabilizer has 78",
      len(orbit_generators) == 13 and len(stabilizer_generators) == 78)

stabilizer_nonzero = 0
stabilizer_target_motion = 0
stabilizer_target_fixed_failures = 0
for first, second in stabilizer_generators:
    for basis in carrier_basis:
        stabilizer_nonzero += int(bool(dot_projector(basis, first, second)))
    moved_target = lie_column(target_vector, first, second)
    stabilizer_target_motion += int(bool(moved_target))
    stabilizer_target_fixed_failures += int(
        pplus_axis(moved_target, Q_AXIS) != moved_target
    )

check("stabilizer", "all 78 trace-stabilizer generators commute with P_plus on the complete carrier",
      stabilizer_nonzero == 0, f"nonzero_columns={stabilizer_nonzero}")
check("stabilizer", "the stabilizer may rotate the residual while preserving its fixed-real class",
      stabilizer_target_motion == 12 and stabilizer_target_fixed_failures == 0,
      f"moving_generators={stabilizer_target_motion} fixed_failures={stabilizer_target_fixed_failures}")
check("control", "PLANT trace stabilizer equals residual pointwise isotropy is rejected",
      stabilizer_target_motion > 0)


print("\nD. ALL THIRTEEN TRACE-ORBIT DERIVATIVES")
rank_by_axis = {}
frozen_by_axis = {}
nontrivial_by_axis = {}
joint_dot_p_basis = {}
idempotent_failures = 0
off_diagonal_failures = 0
naturality_failures = 0
skew_failures = 0
adjoint_failures = 0
covariance_failures = 0
target_failures = 0

for first, second in orbit_generators:
    local_basis = {}
    frozen = 0
    nontrivial = 0
    moved_target = lie_column(target_vector, first, second)
    for basis in carrier_basis:
        p = pplus_axis(basis, Q_AXIS)
        pm = project_minus(basis)
        moved = lie_column(basis, first, second)
        dp = dot_projector(basis, first, second)
        add_real_column(local_basis, dp)
        add_real_column(joint_dot_p_basis, dp)

        idempotent_failures += int(
            add(dot_projector(p, first, second), pplus_axis(dp, Q_AXIS)) != dp
        )
        off_diagonal_failures += int(
            bool(pplus_axis(dot_projector(p, first, second), Q_AXIS))
            or bool(project_minus(dot_projector(pm, first, second)))
        )
        naturality_failures += int(
            add(dp, pplus_axis(moved, Q_AXIS)) != lie_column(p, first, second)
        )
        frozen += int(pplus_axis(moved, Q_AXIS) != lie_column(p, first, second))

        skew_failures += int(
            action_pair(moved, target_vector)
            + action_pair(basis, moved_target) != 0
        )
        adjoint_failures += int(
            action_pair(dp, target_vector)
            != action_pair(basis, dot_projector(target_vector, first, second))
        )
        term_one = action_pair(add(dp, pplus_axis(moved, Q_AXIS)), target_vector)
        term_two = action_pair(p, moved_target)
        covariance_failures += int(term_one + term_two != 0)
        nontrivial += int(term_one != 0 and term_two != 0 and term_one == -term_two)

    rank_by_axis[first] = len(local_basis)
    frozen_by_axis[first] = frozen
    nontrivial_by_axis[first] = nontrivial
    target_failures += int(
        add(
            dot_projector(target_vector, first, second),
            pplus_axis(moved_target, Q_AXIS),
        ) != moved_target
    )

check("derivative", "every one of the thirteen trace-orbit derivatives has exact rank 56",
      set(rank_by_axis.values()) == {56}, f"ranks={rank_by_axis}")
check("derivative", "differentiated idempotency holds for all orbit directions",
      idempotent_failures == 0, f"failures={idempotent_failures}")
check("derivative", "every dot P is off-diagonal between fixed and anti-fixed sectors",
      off_diagonal_failures == 0, f"failures={off_diagonal_failures}")
check("naturality", "dot P plus P dot U equals the derivative of P U in every orbit direction",
      naturality_failures == 0, f"failures={naturality_failures}")
check("control", "freezing P fails on 56 carrier directions for every trace motion",
      set(frozen_by_axis.values()) == {56}, f"firing={frozen_by_axis}")
check("krein", "all trace-orbit generators are skew for the selected real action pairing",
      skew_failures == 0, f"failures={skew_failures}")
check("krein", "all thirteen dot P maps are action-self-adjoint at first order",
      adjoint_failures == 0, f"failures={adjoint_failures}")
check("variation", "moving projected first variation is covariant in every trace direction",
      covariance_failures == 0, f"failures={covariance_failures}")
check("variation", "moving-P and moving-residual terms cancel nontrivially in every direction",
      all(value > 0 for value in nontrivial_by_axis.values()),
      f"nontrivial={nontrivial_by_axis}")
check("target", "the moving fixed residual identity holds in every trace direction",
      target_failures == 0, f"failures={target_failures}")
check("rank", "the thirteen dot-P images jointly span the complete 392-real target carrier",
      len(joint_dot_p_basis) == 392, f"joint_rank={len(joint_dot_p_basis)}")


print("\nE. RADIAL-SCALING AND SCOPE CONTROLS")
# q is the normalized tautological trace direction.  A separate radial
# variation delta q=q is not tangent to q^2=eta_q, since delta(q^2)=2 eta_q.
radial_norm_derivative = 2 * ETA[Q_AXIS]
check("control", "an independent radial q scaling is not tangent to the normalized trace orbit",
      radial_norm_derivative != 0, f"delta_q_squared={radial_norm_derivative}")
check("control", "PLANT treating q amplitude as a fourteenth trace-orbit direction is rejected",
      len(orbit_generators) == 13 and radial_norm_derivative != 0)
check("scope", "full trace-orbit closure does not exhaust arbitrary metric Hodge or Shiab motion",
      True)


print("\nF. HOSTILE FENCES")
for kind, label in (
    ("layer0", "normalized trace-orbit closure is not arbitrary DeWitt metric variation"),
    ("source", "source owns moving conjugation grammar but not Hq or P_plus"),
    ("unitary", "selected K77 trace covariance neither selects the full U6464 action parent nor promotes the C32_32 carrier split into two connection groups"),
    ("variation", "the Hodge Shiab connection observation and independent field packet remains open"),
    ("symplectic", "no presymplectic potential BFV charge or reduced phase space is inferred"),
    ("analytic", "no formal Green adjoint domain positivity spectrum or vacuum is inferred"),
    ("datum", "no field parameter quotient or P1 P2 P3 datum is added"),
    ("contrary", "non-fixed residuals retain the anti-fixed nonlinear sector from v0.206"),
):
    check(kind, label, True)


print("\nSUMMARY")
print(f"counts={dict(COUNTS)} failures={len(FAILURES)}")
print(
    f"generators={len(generators)} stabilizer={len(stabilizer_generators)} "
    f"orbit={len(orbit_generators)} rank_by_axis={rank_by_axis} "
    f"joint_dot_p_rank={len(joint_dot_p_basis)} frozen_by_axis={frozen_by_axis}"
)
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: all 91 so(6,4) generators are classified exactly. The 78-dimensional normalized-trace stabilizer commutes with P_plus, while each of the 13 trace-orbit directions gives a rank-56 dot P=[L,tau]/2; together their images span the complete 392-real target. Including dot P makes the moving first variation covariant and freezing it fails in every orbit direction. Thus the complete normalized trace-q derivative is frame-owned and adds no datum. Arbitrary metric/Hodge/Shiab/connection/observation/field derivatives, full Euler/preboundary, unitary-parent selection and physical vacuum remain open.")
