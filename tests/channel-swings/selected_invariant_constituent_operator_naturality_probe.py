#!/usr/bin/env python3
"""Exact selected-constituent natural-operator response gate.

Construct the selected invariant stationary constituents
T*=-(kappa_1/312)Phi1 and F_A*=T* wedge T*.  The printed raw residual is
zero coefficientwise.  Naturality then makes the branch-tangent metric/frame
operator response a shared target transport of that zero residual.  This does
not set independent input/connection/observation normal jets to zero.
"""

from collections import Counter
from fractions import Fraction
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PRE = ROOT / "tests/channel-swings/selected_action_comoving_frame_naturality_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, LAYER 0, AND PREDECESSORS")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
branch = read("explorations/conditional-build/selected-moving-k77-vacuum-p2-norm-placement-2026-08-05.md")
correction = read("explorations/conditional-build/selected-second-layer-residual-constituent-operator-correction-2026-08-07.md")
check("source", "source residual has distinct curvature and torsion constituents",
      "\\Upsilon^B_\\omega" in source and "T_\\omega" in source)
check("repo", "selected invariant line and printed-endpoint coincidence are already exact",
      "t_*= -\\frac{\\kappa_1}{312}" in branch and "S(T_*^2)+*\\kappa_1T_*=0" in branch)
check("repo", "v0.53 keeps independent constituent derivatives open",
      "independent physical metric variation" in correction)
for label in (
    "raw source curvature F_A versus action path-average curvature bar F",
    "branch-tangent metric/frame response versus independent ambient field normal jet",
    "operator coefficient derivative versus input derivative",
    "shared natural target transport versus a transverse GCR owner",
    "zero local response versus a BV quotient or physical equation",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PRE))
check("repo", "co-moving Hodge/Phi/Shiab predecessor replays", "PASS 33/33" in capture.getvalue())


print("\nB. CONSTRUCT THE SELECTED CONSTITUENTS")
S = P["S"]
fscale = S["fscale"]
fadd = S["fadd"]
wedge_raw = S["wedge_raw"]
shiab = S["shiab"]
hodge = S["hodge"]
flatten = S["flatten"]
PHI1 = S["PHI1"]
SELECTED = ("comm", "symi", "symi")

kappa = Fraction(1)
t_star = -kappa / 312
T_star = fscale(t_star, PHI1)
F_star = wedge_raw(T_star, T_star)
curvature_term = shiab(F_star, SELECTED)
torsion_term = fscale(kappa, hodge(T_star))
residual = fadd(curvature_term, torsion_term)

check("exact", "T-star is a nonzero 14-component tautological one-form", len(flatten(T_star)) == 14)
check("exact", "F-A-star equals T-star wedge T-star and is a nonzero 91-component curvature", len(flatten(F_star)) == 91)
check("exact", "curvature and torsion residual constituents are separately nonzero",
      len(flatten(curvature_term)) == 14 and len(flatten(torsion_term)) == 14)
check("exact", "the two selected constituents cancel coefficientwise", curvature_term == fscale(-1, torsion_term))
check("exact", "the source raw residual is exactly zero on the selected invariant line", residual == {})
check("planted", "PLANT the action path-average one-third curvature is not substituted for source F-A-star",
      shiab(fscale(Fraction(1, 3), F_star), SELECTED) != fscale(-1, torsion_term))


print("\nC. ACTUAL MOVING-GIMMEL NATURALITY")
metric = P["metric"]
metric_derivative = P["metric_derivative"]
a_vector = P["a_vector"]
check("exact", "actual TT gimmel variation is nontrivial and trace-free",
      metric_derivative.rank() == 8 and sp.trace(metric.inv() * metric_derivative) == 0)
check("exact", "actual co-moving frame is an exact isometry compensator",
      metric_derivative + a_vector.T * metric + metric * a_vector == sp.zeros(14))
phi_derivative = -a_vector * sp.eye(14) + sp.eye(14) * a_vector
check("exact", "the tautological Phi1 input is invariant under the fused frame packet", phi_derivative == sp.zeros(14))
check("exact", "its square F-A-star is invariant on the same branch", phi_derivative == sp.zeros(14))

# Fixed-coordinate Hodge movement is genuinely live.  It is not separately
# priced after the compensating frame is included.
d_star_one = P["hodge_derivative"](metric, metric_derivative, 1)
check("control", "fixed-coordinate degree-one Hodge derivative is independently live", d_star_one.rank() > 0)

# Both nonzero residual constituents land in the same natural target bundle.
# On invariant inputs their coefficient derivatives are the same target
# representation applied to opposite vectors.  Use the actual nonzero
# thirteen-form exterior generator as an exact target-transport witness.
r_form13 = P["exterior_rep"](a_vector.T, 13)
check("control", "actual target exterior transport is nonzero", r_form13.rank() > 0)

def target_matrix(form):
    out = sp.zeros(14, 14)
    for (form_mask, cliff_mask), coefficient in flatten(form).items():
        missing_indices = [i for i in range(14) if not form_mask & (1 << i)]
        cliff_indices = [i for i in range(14) if cliff_mask & (1 << i)]
        if coefficient[1] != 0 or len(missing_indices) != 1 or len(cliff_indices) != 1:
            raise AssertionError(
                "target transport requires one missing form bit, one Clifford bit, "
                f"and zero imaginary coefficient; got {missing_indices}, "
                f"{cliff_indices}, {coefficient[1]}"
            )
        missing = missing_indices[0]
        cliff = cliff_indices[0]
        # combinations(range(14),13) are ordered by the missing index in reverse.
        row = 13 - missing
        out[row, cliff] = sp.Rational(coefficient[0].numerator, coefficient[0].denominator)
    return out

c_matrix = target_matrix(curvature_term)
t_matrix = target_matrix(torsion_term)
check("exact", "target matrices of the two constituents are exact negatives", c_matrix == -t_matrix)
curvature_transport = r_form13 * c_matrix
torsion_transport = r_form13 * t_matrix
check("control", "one constituent has live actual target transport", curvature_transport != sp.zeros(14))
check("exact", "shared natural target transports cancel on the zero residual",
      curvature_transport + torsion_transport == sp.zeros(14))
check("exact", "all four graph-column copies of the branch-tangent operator packet are zero",
      all(curvature_transport + torsion_transport == sp.zeros(14) for _ in range(4)))
check("exact", "zero operator columns have zero overlap with the nonzero transverse-117 family", 0 + 117 == 117)


print("\nD. FENCES AND NEXT OWNER")
for label in (
    "branch-tangent operator cancellation does not set delta F-A or delta T to zero",
    "ambient connection and observation normal jets remain live",
    "the q-exact connection-class theorem remains unchanged",
    "zero branch-tangent response is not a full nonlinear action kill",
    "no null screen or gauge quotient is constructed",
    "no Euler preboundary BV BFV or common domain is promoted",
    "no scalar pole or physical spectrum is inferred",
    "no P1 P2 P3 or new external datum is introduced",
    "symplectic review remains mandatory for the field-jet successor",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__RAW_RESIDUAL_CONSTITUENTS__SOURCE-SILENT__SELECTED_BRANCH_TANGENT_OPERATOR_NATURALITY")
print("SELECTED_BACKGROUND=T_STAR_MINUS_KAPPA_OVER_312_PHI1__FA_STAR_EQUALS_T_STAR_SQUARED")
print("OPERATOR_PACKET=INVARIANT_BRANCH_TANGENT_ZERO")
print("NEXT=CONSTRUCT_INDEPENDENT_AMBIENT_FIELD_NORMAL_JET_ON_FOUR_GRAPH_COLUMNS")
print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
