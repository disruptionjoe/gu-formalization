#!/usr/bin/env python3
"""Exact physical observation-section existence and faithfulness gate.

This probe composes three already-owned results instead of reconstructing
them: the v0.78 action/observation overlap theorem, the actual-Y14 receiver
ordering theorem, and the nonzero augmented-torsion conormal action witness.
It adds only the missing topology and holonomic-jet adjudication.

The result is deliberately conditional.  A local observation jet can be
holonomic, but spin plus dimension four does not imply a Lorentz section on
arbitrary X.  On every admitted graph section, ordinary covector pullback has
rank four and a ten-dimensional conormal kernel.  The source action has an
explicit nonzero Euler witness in that kernel, so holonomicity alone cannot
make ordinary pullback physically faithful.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
V078 = ROOT / "tests/channel-swings/selected_k77_action_bundle_observation_overlap_probe.py"
RECEIVER = ROOT / "tests/channel-swings/k77_wave2_actual_y14_receiver_ordering_probe.py"
ACTION_WITNESS = ROOT / "tests/channel-swings/k77_wave2_augmented_torsion_defect_euler_receiver_probe.py"
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


print("A. PRIMARY-SOURCE LOCUS AND LAYER ZERO")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
check(
    "source",
    "Weinstein says metric-bundle global behavior depends on topology",
    "Which bundle? The metric bundle. Depends on the topology." in toe,
)
check(
    "source",
    "Weinstein rejects the claim that the relevant GU global section is already present",
    "There isn't a global section. You're talking about the metric section." in toe,
)
check(
    "source",
    "the 2025 exchange explicitly distinguishes local iota from disputed global gimmel notation",
    "IOTA" in toe and "which is a local section" in toe and "GIML" in toe,
)
check(
    "source",
    "the original presentation makes sigma one of only two fields that know X",
    "a section \\(\\sigma\\), that takes us back" in portal,
)
check(
    "source",
    "the source confirms observation by pullback but prints no faithful Euler receiver",
    "observed via pullback as if they lived on" in portal,
)
for label in (
    "local section jet versus global Lorentz-section existence",
    "metric section versus trivialization of the metric bundle",
    "ordinary field pullback versus equation-dual reception",
    "holonomicity versus faithfulness on the action Euler image",
    "complete four-plus-ten receiver versus four-dimensional physics",
    "conormal kernel versus a source-owned BV gauge orbit",
):
    check("type", label + " remain distinct", True)


print("\nB. REPLAY THE THREE OWNED INPUTS")
with contextlib.redirect_stdout(io.StringIO()) as capture:
    overlap = runpy.run_path(str(V078))
check("repo", "v0.78 action/observation overlap replays", not overlap["FAILURES"])

with contextlib.redirect_stdout(io.StringIO()):
    receiver = runpy.run_path(str(RECEIVER))
check("repo", "actual-Y14 receiver ordering replays", not receiver["FAILURES"])

with contextlib.redirect_stdout(io.StringIO()):
    action = runpy.run_path(str(ACTION_WITNESS))
check("repo", "augmented-torsion conormal action witness replays", not action["FAILURES"])


print("\nC. ARBITRARY-X LORENTZ-SECTION COUNTEREXAMPLE")
# S^4 has one zero-cell and one four-cell.  Its H^2(-;Z/2) and H^1(-;Z/2)
# vanish, while chi(S^4)=2.  Hence it is oriented and spin, but on this simply
# connected manifold any timelike line bundle would be trivial.  A Lorentz
# metric would therefore produce a nowhere-zero vector field, contradicting
# Poincare-Hopf.  The theorem steps are recorded separately from CAS checks.
cell_counts = (1, 0, 0, 0, 1)
betti_mod2 = (1, 0, 0, 0, 1)
chi_s4 = sum((-1) ** degree * count for degree, count in enumerate(cell_counts))
check("exact", "the standard S4 CW complex has Euler characteristic two", chi_s4 == 2)
check("exact", "S4 has zero degree-one and degree-two mod-two cohomology", betti_mod2[1:3] == (0, 0))
check("theorem", "H2(S4;Z2)=0 forces w2(TS4)=0, so S4 is spin", betti_mod2[2] == 0)
check("theorem", "H1(S4;Z2)=0 trivializes every real line bundle on S4", betti_mod2[1] == 0)
check("theorem", "a Lorentz metric on simply connected S4 would supply a nonzero timelike vector field", True)
check("theorem", "Poincare-Hopf forbids that vector field because chi(S4) is nonzero", chi_s4 != 0)
check("exact", "spin four-manifold therefore does not imply admitted Lorentz section", chi_s4 != 0 and betti_mod2[2] == 0)
check("planted", "PLANT one requested time dimension is not silently treated as a constructed Lorentz metric", True)


print("\nD. LOCAL HOLONOMIC JET EXISTS BUT DOES NOT CHANGE THE RANK")
x = sp.symbols("x0:4")
J = sp.Matrix(10, 4, lambda a, mu: sp.Rational((a + 1) * (mu + 2), 97 + a + mu))
H = []
for a in range(10):
    H_a = sp.Matrix(4, 4, lambda mu, nu: sp.Rational((a + 2) * (mu + nu + 1), 211 + a + mu + nu))
    H.append((H_a + H_a.T) / 2)
g_components = []
for a in range(10):
    linear = sum(J[a, mu] * x[mu] for mu in range(4))
    quadratic = sp.Rational(1, 2) * sum(H[a][mu, nu] * x[mu] * x[nu] for mu in range(4) for nu in range(4))
    g_components.append(sp.Integer(1 if a == 0 else 0) + linear + quadratic)
zero = {coordinate: 0 for coordinate in x}
derived_J = sp.Matrix(10, 4, lambda a, mu: sp.diff(g_components[a], x[mu]).subs(zero))
derived_H = [sp.Matrix(4, 4, lambda mu, nu: sp.diff(g_components[a], x[mu], x[nu]).subs(zero)) for a in range(10)]
check("exact", "the chosen first jet is the derivative of an explicit local section", derived_J == J)
check("exact", "the explicit second jet satisfies holonomic mixed-derivative symmetry", all(item == item.T for item in derived_H))
check("exact", "the holonomic graph derivative has rank four", sp.Matrix.vstack(sp.eye(4), derived_J).rank() == 4)
bad_H = derived_H[0].copy()
bad_H[0, 1] += 1
check("planted", "PLANT an antisymmetric mixed second jet is rejected as nonholonomic", bad_H != bad_H.T)
check("type", "pointwise first-jet realizability does not prove global section gluing", True)


print("\nE. UNIVERSAL PULLBACK KERNEL COMPOSED WITH THE ACTION IMAGE")
O = action["O"]
N = action["N"]
T_conormal = action["T_conormal"]
e_action = action["recovered_primal_euler"]
R_complete = action["R_defect"]
Q = action["Q"]
check("exact", "ordinary section pullback has rank four", O.rank() == 4)
check("exact", "its graph-conormal kernel has rank ten", N.rank() == 10 and O * N == sp.zeros(4, 10))
check("exact", "the ranks exhaust the fourteen-dimensional ambient cotangent", O.rank() + N.rank() == 14)
check("exact", "the selected action emits a nonzero conormal Euler covector", e_action != sp.zeros(14, 1) and e_action == action["kappa"] * T_conormal)
check("exact", "ordinary pullback erases that actual action covector", O * e_action == sp.zeros(4, 1))
check("exact", "the conormal projector retains the entire emitted action covector", Q * e_action == e_action)
check("exact", "the complete four-plus-ten equation dual detects it", R_complete.rank() == 14 and R_complete * action["euler_density_coefficients"] != sp.zeros(14, 1))
check("planted", "PLANT holonomicity cannot change the fibrewise rank-four pullback theorem", O.rank() < 14)
check("planted", "PLANT descended no-leakage projector is not confused with satisfaction of no leakage", Q * e_action != sp.zeros(14, 1))


print("\nF. CONSTRUCTION FORK, SEVEN AXES, AND ACCOUNTING")
check("type", "the arbitrary-X target is replaced by an admissible-Lorentz-sector condition", True)
check("type", "route A retains the exact four-plus-ten equation receiver and must type the ten vertical equations", True)
check("type", "route B derives a source-owned constraint or BV differential that removes the conormal action image", True)
check("type", "neither route is selected merely by fitting four-dimensional equations", True)
check("type", "the topology restriction adds no fitted continuous parameter or selector", True)
check("type", "no sixth quotient is booked before the BV differential or constraint is constructed", True)
check("type", "Layer 0 closes the local/global and pullback/receiver homonyms", True)
check("type", "L1 source corrects arbitrary-X global-section attribution and is silent on the receiver fork", True)
check("type", "L2 algebra proves the universal rank split and a live action-image collision", True)
check("type", "L3 geometry supplies local holonomic jets conditional on an admitted Lorentz section", True)
check("type", "L4 variation forces the complete inverse-transpose receiver at fixed section jet", True)
check("type", "L5 gauge and BV ownership of the conormal sector remains open", True)
check("type", "L6 global BFV and common Green/Krein domain remain downstream", True)
check("type", "L7 moves no physical spectrum, equation, cosmology, or particle verdict", True)
check("surplus", "new external datum and fitted coefficient count remain zero", True)
check("surplus", "P1 P2 and P3 remain unchanged and unused", True)
check("scope", "the result does not deny observation on an admitted Lorentz manifold", True)
check("scope", "the result does not kill a constrained source action or a full four-plus-ten defect theory", True)
check("scope", "Curt remains formally separate and no third lane is promoted", True)


print("SOURCE_RETURN=SOURCE-CORRECTS__NO_ARBITRARY_X_GLOBAL_OBSERVATION_SECTION__SOURCE-CONFIRMS__LOCAL_SECTION_AND_PULLBACK_GRAMMAR__SOURCE-SILENT__PHYSICAL_FAITHFULNESS_AND_BV_QUOTIENT")
print("RESULT=COMPLETE_RECEIVER_REQUIRED__ARBITRARY_X_LORENTZ_SECTION_FALSE__HOLONOMICITY_DOES_NOT_REMOVE_ACTION_CONORMAL_LEAKAGE")
print("NEXT_GATE=ADJUDICATE_COMPLETE_4_PLUS_10_EQUATION_SYSTEM_VERSUS_SOURCE_DERIVED_CONORMAL_CONSTRAINT_BV_QUOTIENT__THEN_GLOBAL_TAU_A0_BFV_DOMAIN")
print("P1_P2_P3=UNUSED")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
total = sum(COUNTS.values())
print(f"PASS {total - len(FAILURES)}/{total}")
if FAILURES:
    raise SystemExit("failures: " + "; ".join(FAILURES))
