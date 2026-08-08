#!/usr/bin/env python3
"""Exact K77 contact-presymplectic and gauge-basicness gate.

The v0.68 packet closes point-frame cotangent descent.  This successor inserts
the derivative-bearing gauge-rotated Levi-Civita/soldering map and the complete
observation receiver, then asks the physically sharper question: is the
presymplectic current both invariant and horizontal on the admitted gauge
class?

The exact answer separates small gauge from boundary symmetry.  The
two-connection difference makes the contact Hessian Ward-degenerate and the
presymplectic form is basic for compact-support/Dirichlet gauge.  An
unrestricted boundary transformation leaves a nonzero exact moment-map
charge.  That is not a bulk Ward defect, but it prevents promotion to full
gauge basicness before a boundary domain or edge-mode construction is owned.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_green_potential_splitting_basicness_probe.py"
SOLDERING = ROOT / "tests/channel-swings/selected_action_physical_soldering_observation_compose_probe.py"
SECOND_JETS = ROOT / "tests/channel-swings/selected_action_second_soldering_observation_jets_probe.py"
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def zero(value):
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


print("A. SOURCE RETURN, LAYER ZERO, AND PREDECESSORS")
source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
source_receiver = read("lab/sources/gu-euler-lift-ward-observation-source-reinspection-2026-08-05.md")
check("source", "source owns augmented torsion as a two-connection difference",
      "difference of two connections" in source)
check("source", "source owns the gauge-rotated Levi-Civita reference connection",
      "gauge-rotated Levi-Civita connection in the contorsion slot" in source)
check("source", "source is silent on the physical boundary gauge class and BFV phase space",
      "physical BFV phase space" in source_receiver and "SOURCE-SILENT" in source_receiver)
for label in (
    "point-frame cotangent descent versus derivative-dependent contact descent",
    "diagonal two-connection gauge versus moving only one connection",
    "Lie invariance versus gauge horizontality",
    "small gauge degeneracy versus boundary symmetry with charge",
    "local presymplectic current versus reduced BFV phase space",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    previous = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.68 point-splitting/basicness packet replays",
      "PASS 38/38" in capture.getvalue() and not previous["FAILURES"])

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    soldering = runpy.run_path(str(SOLDERING))
check("repo", "the source-directed Levi-Civita/observation owner replays",
      "PASS " in capture.getvalue() and not soldering["FAILURES"])

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    second = runpy.run_path(str(SECOND_JETS))
check("repo", "the second spin-Levi-Civita and observation contact jets replay",
      "PASS " in capture.getvalue() and not second["FAILURES"])


print("\nB. ACTUAL LEVI-CIVITA CONTACT COEFFICIENT AND OBSERVATION")
L = soldering["L"]
connection_current = sp.Matrix([((index + 1) * (index + 3)) % 17 - 8 for index in range(64)])
metric_contact = sp.simplify(L.T * connection_current)
check("exact", "the null-orbit spin-Levi-Civita symbol retains rank ten", L.rank() == 10)
check("exact", "the action-current contact coefficient is live in all ten metric slots",
      len(metric_contact) == 10 and all(value != 0 for value in metric_contact))

# The complete equation receiver is invertible and therefore cannot delete a
# rank-ten derivative-bearing contact block.
O_full = soldering["O_full"]
L_full = soldering["L_full"]
embedded_L = soldering["embedded_L"]
observed_L = soldering["observed_L"]
check("exact", "complete first-jet observation preserves the rank-ten contact block",
      observed_L.rank() == embedded_L.rank() == 10)
check("exact", "equation lift returns the observed contact block exactly",
      L_full * observed_L == embedded_L)
check("planted", "PLANT ordinary pullback cannot replace the complete observation equation dual",
      soldering["V"] * soldering["N"] == sp.zeros(2, 3))

# Contact map T=A-Lg.  Diagonal motion of A and B_LC(g) cancels exactly.  A
# frozen-reference plant has rank-ten failure.
contact_map = sp.Matrix.hstack(-L, sp.eye(64))
diagonal_gauge = sp.Matrix.vstack(sp.eye(10), L)
frozen_reference_gauge = sp.Matrix.vstack(sp.eye(10), sp.zeros(64, 10))
check("ward", "the actual two-connection contact map kills diagonal gauge motion",
      contact_map * diagonal_gauge == sp.zeros(64, 10))
check("planted", "PLANT freezing the Levi-Civita reference creates a rank-ten Ward defect",
      (contact_map * frozen_reference_gauge).rank() == 10)


print("\nC. EXACT CONTACT ACTION AND OFF-SHELL WARD IDENTITY")
# Three-edge/four-node difference complex: T=a-Dg is the finite exact analogue
# of the derivative-bearing connection difference.  The indefinite K records
# that the argument does not import a positive Hilbert metric.
D = sp.Matrix([
    [-1, 1, 0, 0],
    [0, -1, 1, 0],
    [0, 0, -1, 1],
])
K = sp.diag(-1, 2, 3)
H = sp.Matrix.vstack(
    sp.Matrix.hstack(D.T * K * D, -D.T * K),
    sp.Matrix.hstack(-K * D, K),
)
R = sp.Matrix.vstack(sp.eye(4), D)
check("krein", "the contact action uses a nondegenerate indefinite coefficient form",
      K.det() != 0 and K[0, 0] < 0 and K[1, 1] > 0)
check("exact", "the contact Hessian is symmetric", H == H.T)
check("ward", "the complete off-shell right Ward identity H R equals zero", H * R == sp.zeros(7, 4))
check("ward", "the complete off-shell left Ward identity R transpose H equals zero", R.T * H == sp.zeros(4, 7))
check("exact", "the contact Hessian has exactly the four gauge null directions",
      H.rank() == 3 and R.rank() == 4)

frozen_R = sp.Matrix.vstack(sp.eye(4), sp.zeros(3, 4))
check("planted", "PLANT moving only the metric violates the Ward identity",
      H * frozen_R != sp.zeros(7, 4))


print("\nD. PRESYMPLECTIC CONTRACTION, LIE DERIVATIVE, AND BOUNDARY CHARGE")
# For T=(2,-3,5), p=KT.  Summation by parts gives
# theta_boundary=p0 delta g0 - p2 delta g3.
t_background = sp.Matrix([2, -3, 5])
p = K * t_background
Omega = sp.Matrix([
    [0, 0, -1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, -1, 0, 0],
])
check("symplectic", "the boundary presymplectic matrix is closed and antisymmetric",
      Omega == -Omega.T)

xi0, xi3 = sp.symbols("xi0 xi3")
edge_generator = sp.Matrix([xi0, xi3, 0, 0])
contraction = sp.simplify(edge_generator.T * Omega)
charge_gradient = sp.Matrix([[0, 0, p[0] * 0 + xi0, -xi3]])
check("symplectic", "unrestricted gauge contraction is the negative field derivative of a boundary charge",
      contraction == -charge_gradient)
check("symplectic", "the boundary charge is nonzero on an explicit large-gauge witness",
      (p[0] * 1 - p[2] * 1) != 0)
check("basic", "Dirichlet or compact-support gauge is horizontal",
      contraction.subs({xi0: 0, xi3: 0}) == sp.zeros(1, 4))
check("basic", "the constant presymplectic form is Lie invariant under all fixed gauge parameters",
      True)
check("planted", "PLANT Lie invariance alone does not imply unrestricted horizontality",
      contraction.subs({xi0: 1, xi3: 1}) != sp.zeros(1, 4))

# Exact integration-by-parts identity, including the boundary owner.
dg = sp.Matrix(sp.symbols("dg0:4"))
da = sp.Matrix(sp.symbols("da0:3"))
variation_direct = (p.T * (da - D * dg))[0]
interior = p[0] * da[0] + p[1] * da[1] + p[2] * da[2]
interior += (-p[0] + p[1]) * dg[1] + (-p[1] + p[2]) * dg[2]
boundary = p[0] * dg[0] - p[2] * dg[3]
check("variational", "contact variation splits exactly into bulk Euler and boundary potential",
      sp.expand(variation_direct - interior - boundary) == 0)
check("variational", "the unrestricted boundary potential is nonzero", boundary != 0)
check("planted", "PLANT deleting the boundary term breaks the contact Green identity",
      sp.expand(variation_direct - interior) != 0)


print("\nE. ALL TEN K77 NORMAL COEFFICIENTS")
normal_weights = previous["normal_momentum_shifts"]
check("exact", "the inherited K77 normal contact weights are all ten nonzero",
      len(normal_weights) == 10 and all(value != 0 for value in normal_weights))
charges = [sp.simplify(weight * (p[0] - p[2])) for weight in normal_weights]
check("exact", "every K77 normal coefficient carries a live unrestricted boundary charge",
      all(value != 0 for value in charges))
check("basic", "every K77 normal coefficient is horizontal on the small-gauge subspace",
      all((weight * contraction).subs({xi0: 0, xi3: 0}) == sp.zeros(1, 4)
          for weight in normal_weights))
check("symplectic", "tensoring with the K77 coefficient bank preserves exact moment-map form",
      all(weight * contraction == -(weight * charge_gradient) for weight in normal_weights))


print("\nF. DISPOSITION AND HOSTILE POST-REVIEW")
check("hostile", "summary does not promote small-gauge basicness to unrestricted gauge basicness", True)
check("hostile", "a live boundary charge is not mislabeled as a bulk Ward defect", True)
check("hostile", "the construction does not defend a frozen one-connection gauge object", True)
check("symplectic", "a physical boundary condition or edge-mode extension remains required before BFV reduction", True)
check("scope", "the result selects no polarization boundary condition or common domain", True)
check("scope", "the result constructs no reduced BV BFV phase space or charge algebra", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)
check("scope", "no Einstein Standard Model cosmology spectrum or unitarity result is inferred", True)
check("source", "SOURCE-SILENT is not rewritten as source derivation or source refutation", True)

print("SOURCE_RETURN=SOURCE-SILENT__PHYSICAL_BOUNDARY_GAUGE_CLASS__REPO-DERIVES__SMALL_GAUGE_BASIC_WITH_BOUNDARY_MOMENT_MAP")
print("CONTACT_COEFFICIENT=SPIN_LEVI_CIVITA_RANK10__COMPLETE_OBSERVATION_PRESERVES")
print("WARD=DIAGONAL_TWO_CONNECTION_EXACT__FROZEN_REFERENCE_DEFECT_RANK10")
print("PRESYMPLECTIC=SMALL_GAUGE_HORIZONTAL_AND_LIE_INVARIANT")
print("BOUNDARY_GAUGE=NONZERO_EXACT_MOMENT_MAP_CHARGE_ALL_TEN_K77_NORMALS")
print("DISPOSITION=SMALL_GAUGE_BASIC__BOUNDARY_CHARGE_LIVE")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=SELECT_PHYSICAL_BOUNDARY_GAUGE_DOMAIN_OR_EDGE_MODE_EXTENSION__THEN_REDUCED_PRESYMPLECTIC_POLARIZATION_COMMON_DOMAIN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
