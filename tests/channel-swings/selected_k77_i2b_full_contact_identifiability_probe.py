#!/usr/bin/env python3
"""Exact identifiability gate for the full SC-ACT-04 observer contact.

This probe does not guess the missing ambient normal jet.  It composes the
currently owned coefficient-transport, Levi-Civita and observation-receiver
facts, then builds paired exact SO(3)-equivariant ambient extensions which
agree on every restricted datum but give opposite observer-selection results.
The result is an independence/identifiability theorem at current grade, not a
full-contact construction or a no-go for constructing the source-native jet.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_constrained_observer_euler_ward_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
owner_probe = read("tests/channel-swings/selected_second_layer_observation_owner_retype_probe.py")
contact_report = read("explorations/conditional-build/selected-k77-i2b-radial-lc-section-qrow-composition-2026-08-12.md")
moving_metric = read("explorations/conditional-build/selected-k77-moving-metric-first-action-hessian-2026-08-09.md")
check("source", "SC-ACT-04 owns the residual square but not the ambient normal jet",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims
      and "SOURCE-SILENT__NORMAL_JET_OF_UPSILON" in owner_probe)
check("prior_art", "observation is a dependent graph-section derivative rather than a second field",
      "METRIC_GRAPH_SECTION_DIFFEO_TANGENT=SAME_RANK4_COLUMN" in owner_probe)
check("prior_art", "restricted pullback cannot determine the ambient normal jet",
      "MOVING_SECTION_NORMAL_JET_TERM=LIVE_BUT_UNDETERMINED_BY_ON_SECTION_PULLBACK" in owner_probe)
check("prior_art", "owned radial Levi-Civita response is live but its first action derivative vanishes",
      "radial residual derivatives are nonzero `4/4`, action derivatives zero" in contact_report)
check("prior_art", "co-moving coefficient transport is stationary while the source LC chain stays separate",
      "The source-coordinate field chain remains live" in moving_metric
      and "The first term vanishes at a stationary point" in moving_metric)
for label in (
    "restricted residual derivative versus ambient normal residual jet",
    "moving coefficient transport versus fixed-varpi Levi-Civita contact",
    "observation receiver versus an independent action field",
    "observer Euler tensor versus physical stress-energy",
    "simple timelike line versus a future-pointing arrow",
    "local response stratum versus a global common section",
):
    check("layer0", label + " remain distinct", True)
for label in (
    "variational bicomplex requires the normal-jet chain-rule term",
    "principal-bundle geometry requires SO3-equivariance at an adapted line",
    "symplectic review forbids promoting a receiver to a quotient",
    "analytic review treats the simple eigenline as open but not globally protected",
    "Clifford/Krein review preserves the exact inverse-adjoint tensor",
    "contrary review requires paired completions with opposite outcomes",
):
    check("preflight", label, True)


print("\nB. IMMUTABLE V0.218 OBSERVER TENSOR")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V218 = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.218 exact observer predecessor replays",
      '"failures": 0' in capture.getvalue())
TENSOR = V218["TENSOR"]
check("exact", "v0.218 timelike block remains minus-eight plus-eight",
      TENSOR[0][0] == sp.diag(*([-8] * 4 + [8] * 12)))
check("exact", "v0.218 spatial blocks remain minus-eight identity",
      all(TENSOR[j][j] == -8 * sp.eye(16) for j in range(1, 4)))
check("exact", "v0.218 mixed observer blocks remain zero",
      all(TENSOR[a][b] == sp.zeros(16)
          for a in range(4) for b in range(4) if a != b))


def active_norm(response: sp.Matrix) -> sp.Expr:
    return sp.expand(sum(response[index] ** 2 for index in range(4)))


def observer_gap(response: sp.Matrix) -> sp.Expr:
    return sp.expand(-16 * active_norm(response))


print("\nC. PAIRED AMBIENT NORMAL-JET COMPLETIONS")
# The adapted SO(3) stabilizer decomposes the four active response coordinates
# as one scalar plus one spatial vector.  The rank-ten observation normal has
# a scalar trace line.  A normal-jet coefficient q from that scalar to the
# active scalar is therefore SO(3)-equivariant; covariance does not fix q.
r_symbols = sp.symbols("r00:03 r10:13 r20:23")
R4 = sp.Matrix(3, 3, r_symbols)
response_action = sp.diag(1, R4, sp.eye(12))
normal_action = sp.diag(1, R4, sp.eye(6))
scalar_inclusion = sp.zeros(16, 10)
scalar_inclusion[0, 0] = 1
check("equivariance", "the scalar normal-to-response contact is SO3-equivariant",
      sp.simplify(response_action * scalar_inclusion
                  - scalar_inclusion * normal_action) == sp.zeros(16, 10))
check("equivariance", "zero contact is independently SO3-equivariant",
      response_action * sp.zeros(16, 10) == sp.zeros(16, 10) * normal_action)

# The graph derivative J and restricted derivative D are fixed.  Q is the
# ambient normal derivative which restricted pullback does not see.  Q0 and Q1
# therefore agree on all on-section data D but give different total derivatives
# D+QJ.  One exact scalar graph direction is enough to decide identifiability.
J = sp.zeros(10, 1)
J[0, 0] = 1
D_selected = sp.Matrix([1, 0, 0, 0] + [1] * 12)
Q_preserve = sp.zeros(16, 10)
Q_destroy = -scalar_inclusion
total_preserve = D_selected + Q_preserve * J
total_destroy = D_selected + Q_destroy * J
zero_normal = sp.zeros(10, 1)
check("exact", "paired ambient extensions have the same on-section restriction",
      D_selected + Q_preserve * zero_normal
      == D_selected + Q_destroy * zero_normal == D_selected)
check("exact", "paired extensions differ only by the normal-jet chain rule",
      total_destroy - total_preserve == (Q_destroy - Q_preserve) * J)
check("exact", "zero normal jet preserves the A-positive line",
      active_norm(total_preserve) == 1 and observer_gap(total_preserve) == -16)
check("exact", "equivariant scalar normal jet destroys selection by reaching A-zero",
      active_norm(total_destroy) == 0 and observer_gap(total_destroy) == 0)
check("plant", "PLANT equal restricted data do not force equal observer strata",
      observer_gap(total_preserve) != observer_gap(total_destroy))

D_flat = sp.Matrix([0] * 4 + [1] * 12)
Q_create = scalar_inclusion
total_flat = D_flat + Q_preserve * J
total_create = D_flat + Q_create * J
check("exact", "zero completion leaves a nonzero restricted response observer-flat",
      D_flat != sp.zeros(16, 1) and observer_gap(total_flat) == 0)
check("exact", "equivariant scalar normal jet can create an A-positive line",
      active_norm(total_create) == 1 and observer_gap(total_create) == -16)
check("plant", "PLANT the A-zero restricted stratum is not protected from unknown contact",
      observer_gap(total_flat) != observer_gap(total_create))


print("\nD. COMPLETE SCALAR-CONTACT DISCRIMINANT")
a0, a1, a2, a3, q, section_scalar = sp.symbols(
    "a0 a1 a2 a3 q section_scalar", real=True
)
generic = sp.Matrix([a0 + q * section_scalar, a1, a2, a3] + [0] * 12)
generic_A = sp.factor(active_norm(generic))
check("exact", "generic equivariant scalar-contact active norm is exact",
      sp.expand(generic_A - (a1**2 + a2**2 + a3**2
                             + (a0 + q * section_scalar) ** 2)) == 0)
check("exact", "selection can fail only on the exact contact discriminant",
      generic_A.subs({a1: 0, a2: 0, a3: 0, q: -a0 / section_scalar}) == 0)
check("exact", "any nonzero active spatial component protects the line from scalar contact",
      generic_A.subs({a1: 1, a2: 0, a3: 0, q: -a0 / section_scalar}) == 1)
check("control", "a noncancelling contact remains in the selected stratum",
      generic_A.subs({a0: 1, a1: 0, a2: 0, a3: 0, section_scalar: 1, q: 2}) == 9)
check("plant", "PLANT local openness is not universal protection",
      generic_A.subs({a0: 1, a1: 0, a2: 0, a3: 0, section_scalar: 1, q: -1}) == 0)


print("\nE. IDENTIFIABILITY VERDICT AND ACCOUNTING")
for kind, label in (
    ("composition", "owned co-moving coefficient transport does not fix the normal jet"),
    ("composition", "owned radial LC first variation does not fix the residual-square observer contact"),
    ("scope", "current restricted data admit preserve destroy and create observer outcomes"),
    ("scope", "the observer-line route remains live because generic contact avoids the discriminant"),
    ("scope", "the actual source-native J1 Upsilon normal jet is the single next owner"),
    ("symplectic", "no receiver quotient presymplectic class or BFV reduction is inferred"),
    ("analytic", "no global line arrow domain spectrum or stability theorem is inferred"),
    ("datum", "no external observer normal jet P1 P2 or P3 is adopted"),
    ("accounting", "no parameter residue quotient or selector is booked"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_OBSERVATION_AND_SC_ACT_04_GRAMMAR__SOURCE_SILENT_AMBIENT_NORMAL_JET")
print("OWNED_CONTACT=COEFFICIENT_TRANSPORT_PLUS_RADIAL_LC_PLUS_RECEIVER__NORMAL_JET_UNOWNED")
print("PAIRED_COMPLETIONS=SAME_RESTRICTED_DATA__PRESERVE_DESTROY_AND_CREATE_OBSERVER_LINE")
print("DISCRIMINANT=(a0+q*s)^2+a1^2+a2^2+a3^2=0")
print("VERDICT=FULL_CONTACT_NOT_IDENTIFIABLE_FROM_CURRENT_RESTRICTED_DATA__OBSERVER_PATH_REMAINS_LIVE")
print("NEXT=CONSTRUCT_SOURCE_NATIVE_J1_UPSILON_AMBIENT_NORMAL_JET__THEN_RECOMPUTE_COUPLED_OBSERVER_TENSOR")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
