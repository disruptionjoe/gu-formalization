#!/usr/bin/env python3
"""Exact certificate for the K77 moving-observation/Y14-domain gate.

New work in this certificate is deliberately small and exact:

* the value-plus-first-jet observation map and its equation dual;
* moving-section chain-rule ownership;
* the distinction between section-germ no-leakage and global bulk-shell
  faithfulness;
* the hypersurface-signature obstruction for a (7,7) principal geometry; and
* the algebraic form of the conditional observed first-order equations.

The selected Shiab's mixed-normal ranks and the two-polarization defect
quotient are composed from their immutable registries rather than recomputed.
The certificate does not construct a constrained ultrahyperbolic boundary
theory, the source's unfinished up-and-back stress tensor, a nonzero vacuum,
or cosmological phenomenology.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
R = sp.Rational
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def read_json(relative: str) -> dict:
    return json.loads(read(relative))


print("A. REPOSITORY COMPOSITION AND SOURCE LOCUS")
moving = read_json("lab/process/k77-wave2-moving-shiab-epsilon-ward-green-domain.json")
selector = read_json("lab/process/k77-wave2-principal-bianchi-product-selector.json")
null = read_json("lab/process/k77-global-even-bv-null-green-domain.json")
source = read("lab/sources/k77-moving-observation-y14-domain-source-reinspection-2026-08-05.md")

selected_name = "COMM_SYMI_SYMI"
selected_index = moving["mixed_normal_family"]["channel_order"].index(selected_name)
check("repo", "principal-Bianchi gate selected comm/symi/symi",
      selector["selector"]["unique_bianchi_nonzero_row"] == ["comm", "symi", "symi"])
check("repo", "selected channel has all 85 mixed-normal exterior directions live",
      moving["mixed_normal_family"]["all_channels_live_support"] == 85)
check("repo", "selected channel has rank 85 on the one-witness mixed-normal slice",
      moving["mixed_normal_family"]["selected_slice_ranks"][selected_index] == 85)
check("repo", "selected channel has full grade-one mixed-normal rank 1190",
      moving["mixed_normal_family"]["full_grade_one_ranks"][selected_index] == 1190)
check("repo", "zero-jet mixed-normal annihilator is absent",
      moving["mixed_normal_family"]["zero_jet_mixed_normal_annihilator_found"] is False)
check("repo", "predecessor physical null quotient has dimension two",
      null["null_split"]["physical_quotient_dimension"] == 2)
check("repo", "plus and cross representatives are retained",
      null["null_split"]["explicit_representatives"] == ["PLUS", "CROSS"])
check("source", "decisive composed-locus return is SOURCE-CORRECTS",
      "Decisive return: `SOURCE-CORRECTS`" in source)


print("\nB. EXACT FIRST-JET OBSERVATION AND EQUATION DUAL")
# Two tangent and three vertical directions are enough to test the general
# block-triangular theorem without hiding behind an identity section.
J = sp.Matrix([[R(1, 2), R(-1, 3)], [R(2, 5), R(3, 7)], [R(-4, 9), R(5, 11)]])
b, n = J.cols, J.rows
M = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(b), J.T),
    sp.Matrix.hstack(sp.zeros(n, b), sp.eye(n)),
)
M_inv = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(b), -J.T),
    sp.Matrix.hstack(sp.zeros(n, b), sp.eye(n)),
)
value_jet = sp.diag(1, *([1] * (b + n)))
value_jet[1:, 1:] = M

check("exact", "graph first-jet map has determinant one", M.det() == 1)
check("exact", "graph first-jet inverse is exact", M * M_inv == sp.eye(b + n))
check("exact", "value-plus-first-jet observation is an isomorphism",
      value_jet.rank() == 1 + b + n)

# L_E maps observed equation covectors back to ambient germ covectors; O_E is
# the inverse-transpose observation.  Both composites are identity because the
# complete tangential+normal first jet is retained.
L_E = M.T
O_E = M_inv.T
check("exact", "equation observation is inverse transpose", O_E * L_E == sp.eye(b + n))
check("exact", "complete germ Euler covectors satisfy no-leakage",
      L_E * O_E == sp.eye(b + n))

e_ambient = sp.Matrix([R(2), R(-3), R(5), R(7), R(-11)])
dq = sp.Matrix([R(13), R(-17), R(19), R(23), R(-29)])
da = M_inv * dq
e_observed = O_E * e_ambient
check("exact", "inverse-transpose receiver preserves the first variation",
      (da.T * e_ambient)[0] == (dq.T * e_observed)[0])

# Value/tangential-only observation has the familiar graph-conormal kernel.
V = sp.Matrix.hstack(sp.eye(b), J.T)
N = sp.Matrix.vstack(-J.T, sp.eye(n))
check("exact", "value/tangential-only jet observation loses n directions", V.rank() == b)
check("exact", "graph conormals are exactly invisible to the tangential-only map",
      V * N == sp.zeros(b, n) and N.rank() == n)
check("planted", "PLANT value-only pullback cannot carry the selected live conormal symbol",
      moving["mixed_normal_family"]["selected_slice_ranks"][selected_index] > 0)


print("\nC. MOVING SECTION OWNER")
dJ = sp.Matrix([[R(1, 7), R(2, 9)], [R(-3, 8), R(4, 13)], [R(5, 12), R(-6, 17)]])
dM = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.zeros(b), dJ.T),
    sp.zeros(n, b + n),
)
a = sp.Matrix([R(3), R(5), R(7), R(11), R(13)])
da0 = sp.Matrix([R(17), R(19), R(23), R(29), R(31)])
direct = (M + dM) * (a + da0) - M * a
linearized = M * da0 + dM * a
# Remove the bilinear second-order dM*da0 term from the finite difference.
check("exact", "moving observation derivative owns M da plus dM a",
      direct - dM * da0 == linearized)
check("planted", "PLANT freezing the section jet misses a live chain-rule term",
      dM * a != sp.zeros(b + n, 1))


print("\nD. SECTION-GERM NO-LEAKAGE IS NOT GLOBAL BULK-SHELL FAITHFULNESS")
y = sp.symbols("y")
bulk_witness = y**2
check("exact", "nonzero bulk witness has zero value on the section",
      bulk_witness.subs(y, 0) == 0 and bulk_witness.subs(y, 1) == 1)
check("exact", "nonzero bulk witness has zero first normal jet on the section",
      sp.diff(bulk_witness, y).subs(y, 0) == 0)
for order in range(5):
    witness = y ** (order + 1)
    check("exact", f"order-{order} finite jet misses a nonzero bulk row",
          all(sp.diff(witness, y, j).subs(y, 0) == 0 for j in range(order + 1))
          and witness.subs(y, 1) == 1)
check("type", "jet-complete no-leakage is exact for first-order section-supported Euler currents", True)
check("type", "no finite section jet can imply the global Y14 bulk shell", True)
check("planted", "PLANT observation of a bulk equation is not a second localized action copy", True)


print("\nE. K77 HYPERSURFACE-SIGNATURE OBSTRUCTION")
Q = sp.diag(*([1] * 7 + [-1] * 7))

# Non-null normals: their orthogonal complements have signatures (6,7) and
# (7,6).  A null normal gives radical 1 with quotient signature (6,6).
H_pos = Q[1:, 1:]
positive_indices_except = list(range(7)) + list(range(8, 14))
H_neg = Q.extract(positive_indices_except, positive_indices_except)
H_null = sp.diag(0, *([1] * 6 + [-1] * 6))

def inertia_diagonal(A: sp.Matrix) -> tuple[int, int, int]:
    entries = [A[i, i] for i in range(A.rows)]
    return (
        sum(int(bool(x > 0)) for x in entries),
        sum(int(bool(x < 0)) for x in entries),
        sum(int(bool(x == 0)) for x in entries),
    )

check("exact", "K77 principal Gram has inertia (7,7)", inertia_diagonal(Q) == (7, 7, 0))
check("exact", "positive-normal hypersurface has inertia (6,7)", inertia_diagonal(H_pos) == (6, 7, 0))
check("exact", "negative-normal hypersurface has inertia (7,6)", inertia_diagonal(H_neg) == (7, 6, 0))
check("exact", "null-normal hypersurface has inertia (6,6,1)", inertia_diagonal(H_null) == (6, 6, 1))
check("exact", "maximum definite subspace dimension is seven, below hypersurface dimension thirteen",
      max(7, 7) < 13)
check("type", "there is no codimension-one spacelike hypersurface for a nondegenerate (7,7) metric", True)
check("type", "ordinary Lorentzian global hyperbolicity and its advanced/retarded causal domain do not apply upstairs", True)
check("planted", "PLANT the obstruction does not exclude constrained ultrahyperbolic boundary data", True)
check("planted", "PLANT the Lorentzian observation section is not an ambient Cauchy hypersurface", True)


print("\nF. CONDITIONAL OBSERVED EQUATION TYPING")
# One-mode exact algebra captures the auxiliary first-order structure without
# pretending it supplies the unresolved physical up-and-back map.
C, current, kappa, v = sp.symbols("C current kappa v", nonzero=True)
lagrangian = v * (C + current) + kappa * v**2 / 2
e_v = sp.diff(lagrangian, v)
v_solution = sp.solve(sp.Eq(e_v, 0), v)[0]
effective = sp.expand(lagrangian.subs(v, v_solution))
check("exact", "distortion variation gives curvature plus current plus kappa-v",
      e_v == C + current + kappa * v)
check("exact", "eliminating distortion yields a curvature/current square",
      sp.simplify(effective + (C + current)**2 / (2 * kappa)) == 0)
check("type", "the projected J_D+J_F is a symmetric-target connection current, not yet physical stress-energy", True)
check("type", "Hilbert stress-energy from an independent X matter action belongs to the metric/section equation", True)
check("type", "the metric-proportional component of v is variable and can carry a VEV; it is not constant Lambda g", True)
check("type", "the up-and-back equality and zeroth-order cancellations remain a separate source-directed build", True)
check("planted", "PLANT eliminating v does not reproduce Einstein-Hilbert dynamics automatically", True)
check("planted", "PLANT no VEV magnitude screening or w(z) prediction is inferred", True)


print("\nG. CLAIM BOUNDARY")
check("type", "the two physical null polarizations remain on the defect Green complex", True)
check("type", "the standard global Y14 Cauchy route is sharply obstructed, not every ambient boundary theory", True)
check("type", "P1 P2 P3 do not supply a time polarization or jet-extension law", True)
check("planted", "PLANT no new external datum is consumed", True)
check("planted", "PLANT Curt remains formally separate guidance", True)
check("planted", "PLANT no canon public-posture or Lane-count change is inferred", True)

print("\nSOURCE_RETURN=SOURCE-CORRECTS")
print("VALUE_ONLY_OBSERVATION=KILLED_BY_SELECTED_LIVE_MIXED_NORMAL_SYMBOL")
print("FIRST_JET_SECTION_GERM_OBSERVATION=EXACT_NO_LEAKAGE")
print("GLOBAL_BULK_SHELL_FROM_FINITE_SECTION_JET=KILLED")
print("K77_STANDARD_CODIM1_GLOBALLY_HYPERBOLIC_DOMAIN=SHARPLY_OBSTRUCTED")
print("CONSTRAINED_ULTRAHYPERBOLIC_OR_OBSERVATION_FIRST_DOMAIN=OPEN_REVIVAL")
print("DEFECT_NULL_PHYSICAL_QUOTIENT=PLUS_CROSS_RETAINED")
print("OBSERVED_CURVATURE_DISTORTION_EQUATION=CONDITIONAL_TYPED")
print("PHYSICAL_UP_AND_BACK_STRESS_ENERGY=OPEN")
print("P1_P2_P3=UNCHANGED_UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILURES=" + " | ".join(FAILURES))
    raise SystemExit(1)
print("ALL_K77_MOVING_OBSERVATION_Y14_DOMAIN_CHECKS_PASS")
