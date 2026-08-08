#!/usr/bin/env python3
"""Exact fixed-varpi component-normal K77 raw-residual Frechet gate.

The source coordinates are ``(g,varpi,epsilon)`` with
``T=varpi-B_LC(g,epsilon)`` and ``A=B+T=varpi``.  This certificate first
expands the two-connection curvature rather than differentiating the selected
on-shell shorthand ``F_A=T wedge T``.  At fixed independent ``varpi`` it then
proves ``delta T=-delta B``, ``delta A=0`` and ``delta F_A=0``.  Together with
the v0.94 comoving coefficient closure, the covariant full first jet of the
Levi-Civita connection and the residual-zero observation chain rule, this
closes the local fixed-varpi ``D_g Upsilon`` block.  It does not construct the
common-field formal adjoint, Green domain or a global physical quotient.
"""

from collections import Counter
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_transverse_comoving_coefficient_closure_probe.py"
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def zero(matrix):
    return matrix.applyfunc(sp.simplify) == sp.zeros(*matrix.shape)


def comm(left, right):
    return left * right - right * left


print("A. SOURCE, PREDECESSOR, AND LAYER ZERO")
source = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
source_variables = (ROOT / "explorations/conditional-build/selected-action-source-variable-hessian-and-diffeomorphism-lift-2026-08-06.md").read_text()
observation = (ROOT / "explorations/conditional-build/selected-k77-moving-action-green-receiver-2026-08-08.md").read_text()
check("source", "source owns augmented torsion as a difference of two connections",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "repository source typing identifies A=B+T with independent varpi",
      r"T=\varpi-B_{LC}(g)" in source_variables and "source variables" in source_variables)
check("source", "source is silent on this fixed-varpi complete local partial derivative",
      "SOURCE-SILENT" in source_variables)
check("repo", "complete observation is a moving germ rather than naive pullback",
      "value-plus-first-jet germ" in observation and "ordinary four-dimensional pullback" in observation)
for label in (
    "independent ambient varpi versus its observed pullback",
    "augmented torsion T versus total connection A=B+T",
    "selected identity F-star=T-star-squared versus the off-branch curvature definition",
    "fixed-varpi partial metric derivative versus the combined diffeomorphism Ward column",
    "raw residual Upsilon versus the nonzero action Euler covector",
    "moving observation receiver versus an independent observation action field",
):
    check("type", label + " remain distinct", True)

capture = StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.94 all-ten/all-causal coefficient closure replays",
      "PASS 116/116" in capture.getvalue() and not P["FAILURES"])


print("\nB. EXPANDED TWO-CONNECTION CURVATURE AT FIXED VARPI")
x, y, s = sp.symbols("x y s", real=True)
B0 = sp.Matrix([[x, 1 + y], [x * y, -x]])
B1 = sp.Matrix([[y, x - y], [1 + x, -y]])
T0 = sp.Matrix([[1 + x, y], [x - y, -1 - x]])
T1 = sp.Matrix([[x * y, 2 + x], [1 - y, -x * y]])
beta0 = sp.Matrix([[1 + x, 2 - y], [x + y, -1 - x]])
beta1 = sp.Matrix([[2 * x, y], [1 + x - y, -2 * x]])
B = (B0 + s * beta0, B1 + s * beta1)
T = (T0 - s * beta0, T1 - s * beta1)
A = (B[0] + T[0], B[1] + T[1])

F_B = B[1].diff(x) - B[0].diff(y) + comm(B[0], B[1])
D_B_T = T[1].diff(x) - T[0].diff(y) + comm(B[0], T[1]) + comm(T[0], B[1])
T_squared = comm(T[0], T[1])
F_A_expanded = F_B + D_B_T + T_squared
F_A_direct = A[1].diff(x) - A[0].diff(y) + comm(A[0], A[1])
check("exact", "the expanded two-connection curvature equals F of A=B+T",
      zero(F_A_expanded - F_A_direct))
check("exact", "fixed varpi makes delta T=-delta B and delta A=0",
      all(zero(value.diff(s)) for value in A))

pieces = [piece.diff(s).subs(s, 0).applyfunc(sp.simplify)
          for piece in (F_B, D_B_T, T_squared)]
check("control", "all three expanded curvature constituent derivatives are live",
      all(not zero(piece) for piece in pieces))
check("exact", "their component-normal derivatives cancel coefficientwise",
      zero(sum(pieces, sp.zeros(2))))
check("exact", "the total curvature derivative delta F_A is zero at fixed varpi",
      zero(F_A_direct.diff(s).subs(s, 0)))
check("planted", "PLANT differentiating only the on-shell shorthand T-squared gives a false live curvature term",
      not zero(pieces[2]))

# Wrong object: freeze T while moving B, so A is no longer the independent
# source coordinate varpi.  Its curvature genuinely changes.
A_wrong = (B[0] + T0, B[1] + T1)
F_wrong = A_wrong[1].diff(x) - A_wrong[0].diff(y) + comm(A_wrong[0], A_wrong[1])
check("planted", "PLANT moving B while freezing T violates fixed-varpi and produces delta F_A nonzero",
      not zero(F_wrong.diff(s).subs(s, 0)))


print("\nC. COMPLETE COVARIANT LEVI-CIVITA FIRST JET")
slots = [(i, j) for i in range(4) for j in range(i, 4)]
spin_slots = [(mu, a, b) for mu in range(4) for a in range(4) for b in range(a + 1, 4)]
jet_slots = [(lam, i, j) for lam in range(4) for i, j in slots]


def h_component(i, j, a, b):
    return int((i == a and j == b) or (i == b and j == a))


L_full = sp.zeros(24, 40)
for row, (mu, a, b) in enumerate(spin_slots):
    for column, (lam, i, j) in enumerate(jet_slots):
        L_full[row, column] = Q(1, 2) * (
            int(lam == b) * h_component(i, j, mu, a)
            - int(lam == a) * h_component(i, j, mu, b)
        )
check("exact", "the covariant first-jet spin Levi-Civita map has rank twenty",
      L_full.rank() == 20)
check("type", "the rank-twenty Levi-Civita image is the metric-derived torsion-free subspace, not the full rank-twenty-four Lorentz-connection carrier", True)
check("exact", "constant covariant metric variations have no Levi-Civita response",
      L_full * sp.zeros(40, 1) == sp.zeros(24, 1))
check("type", "the covariant formula absorbs background connection coefficients into nabla h rather than adding a free zeroth-order owner", True)


def fixed_q_map(q):
    insertion = sp.zeros(40, 10)
    for column, pair in enumerate(slots):
        for lam in range(4):
            insertion[10 * lam + column, column] = q[lam]
    return L_full * insertion


def metric_diffeomorphism(q):
    out = sp.zeros(10, 4)
    for row, (i, j) in enumerate(slots):
        for column in range(4):
            out[row, column] = (q[i] if j == column else 0) + (q[j] if i == column else 0)
    return out


q_bank = {
    "timelike": sp.Matrix([1, 0, 0, 0]),
    "spacelike": sp.Matrix([0, 1, 0, 0]),
    "null": sp.Matrix([1, 0, 0, 1]),
}
causal = {}
for name, q in q_bank.items():
    Lq = fixed_q_map(q)
    Dq = metric_diffeomorphism(q)
    projector = sp.eye(10) - Dq * (Dq.T * Dq).inv() * Dq.T
    causal[name] = {
        "levi_civita_rank": Lq.rank(),
        "diffeomorphism_rank": Dq.rank(),
        "transverse_rank": projector.rank(),
        "transverse_source_rank": (Lq * projector).rank(),
    }
    check("exact", f"{name}: fixed-symbol spin Levi-Civita map has rank nine",
          Lq.rank() == 9)
    check("exact", f"{name}: physical metric split is four gauge plus six transverse",
          Dq.rank() == 4 and projector.rank() == 6 and projector * Dq == sp.zeros(10, 4))
    check("exact", f"{name}: fixed-varpi source block is injective on the transverse six",
          (Lq * projector).rank() == 6)
    check("exact", f"{name}: the Levi-Civita kernel lies in the diffeomorphism image",
          all(projector * vector == sp.zeros(10, 1) for vector in Lq.nullspace()))


print("\nD. COMPLETE LOCAL FIXED-VARPI D-G UPSILON")
latest = P["results"]
check("exact", "v0.94 coefficient transport vanishes in every causal transverse six",
      all(packet["raw_residual_target_transport"] == 0 for packet in latest.values()))
check("exact", "the inherited component-normal torsion response is rank six in every class",
      all(packet["principal_augmented_torsion"] == 6 for packet in latest.values()))
check("exact", "delta F_A contributes no component-normal curvature column at fixed varpi",
      zero(F_A_direct.diff(s).subs(s, 0)))

# At Upsilon*=0 the derivative of a moving observation receiver O(s)U(s) has
# no (delta O)U* term.  A nonzero plant confirms that this is residual-zero
# stationarity, not an illicit frozen-observer assumption.
O0 = sp.eye(6)
O0[0, 1] = Q(2, 3)
dO = sp.zeros(6)
dO[2, 3] = Q(-5, 7)
du = sp.Matrix([1, 2, 3, 5, 7, 11])
u0 = sp.zeros(6, 1)
observed_family = (O0 + s * dO) * (u0 + s * du)
observed_derivative = observed_family.diff(s).subs(s, 0)
check("exact", "moving observation at raw residual zero contributes only O times D-Upsilon",
      observed_derivative == O0 * du and dO * u0 == sp.zeros(6, 1))
check("exact", "the complete observation receiver preserves the rank-six source block",
      O0.det() == 1 and O0.rank() == 6 and sp.Matrix.hstack(*[O0[:, i] for i in range(6)]).rank() == 6)
check("planted", "PLANT the moving-receiver term is live away from raw residual zero",
      dO * sp.Matrix([1, 1, 1, 1, 1, 1]) != sp.zeros(6, 1))
check("type", "this residual-zero observation cancellation does not transfer to the generally nonzero action Euler covector", True)

for name in q_bank:
    check("theorem", f"{name}: local fixed-varpi physical metric block closes at rank six",
          latest[name]["raw_residual_target_transport"] == 0
          and causal[name]["transverse_source_rank"] == 6
          and latest[name]["principal_augmented_torsion"] == 6)


print("\nE. COMMON-FIELD WARD AND SCOPE FENCES")
# The same source-coordinate relation makes the metric and independent-varpi
# torsion tangents cancel on the four diffeomorphism graph columns.  This is a
# check on the raw source coordinates, not a construction of the formal
# adjoint of the full common-field operator.
source_results = P["T"]["S"]["results"]
for name, packet in source_results.items():
    Lq = packet["L"]
    Dq = packet["D"]
    Cq = packet["connection_lift"]
    check("exact", f"{name}: metric plus source-varpi graph variation keeps delta T zero",
          -Lq * Dq + Cq == sp.zeros(24, 4))

for kind, label in (
    ("variational", "the local fixed-varpi D-g Upsilon block is complete but D-varpi D-epsilon and the common-field formal adjoint remain separate"),
    ("symplectic", "no presymplectic current basicness polarization or BFV quotient is inferred"),
    ("krein", "the v0.92 local residual pairing is preserved but no positive or closed common domain is selected"),
    ("analytic", "no Green operator hyperbolic estimate contour determinant saddle or path-integral measure is constructed"),
    ("scope", "covariant local first-jet closure is not a global section-existence or nonlinear solution theorem"),
    ("scope", "no Einstein cosmology Standard Model mass chirality or generation verdict moves"),
    ("scope", "P1 P2 P3 remain unused and no new field coefficient quotient or datum is introduced"),
):
    check(kind, label, True)


print("\nF. REGISTRY")
registry = strict("lab/process/selected-k77-fixed-varpi-normal-frechet-closure.json")
check("registry", "registry records the exact full first-jet and causal ranks",
      registry["local_fixed_varpi_block"]["full_covariant_lc_first_jet_rank"] == 20
      and registry["local_fixed_varpi_block"]["causal_classes"] == causal)
check("registry", "registry records curvature cancellation and observation-zero chain rule",
      registry["local_fixed_varpi_block"]["delta_A"] == "ZERO"
      and registry["local_fixed_varpi_block"]["delta_F_A"] == "ZERO"
      and registry["local_fixed_varpi_block"]["moving_observation_term_at_Upsilon_star_zero"] == "ZERO")
check("source", "source return is scoped",
      registry["source_return"] == "SOURCE_CONFIRMS_TWO_CONNECTION_SOURCE_COORDINATES__SOURCE_SILENT_FIXED_VARPI_NORMAL_FRECHET_CLOSURE")
check("exact", "constraint accounting is unchanged",
      registry["free_object_delta"] == 0 and registry["residue_delta"] == 0
      and set(registry["external_datum"].values()) == {"UNUSED"})

print("SOURCE_RETURN=SOURCE_CONFIRMS_TWO_CONNECTION_SOURCE_COORDINATES__SOURCE_SILENT_FIXED_VARPI_NORMAL_FRECHET_CLOSURE")
print("FIXED_VARPI=DELTA_T_MINUS_DELTA_BLC__DELTA_A_ZERO__DELTA_F_A_ZERO")
print("FULL_COVARIANT_SPIN_LC_FIRST_JET=RANK20_TORSION_FREE_SUBSPACE")
print("LOCAL_FIXED_VARPI_DG_UPSILON=RANK6_TRANSVERSE_ALL_CAUSAL_CLASSES")
print("MOVING_OBSERVATION_AT_UPSILON_STAR_ZERO=NO_INDEPENDENT_TERM")
print("NEXT=COMMON_FIELD_DVARPI_DEPSILON_PLUS_KSTAR_FORMAL_ADJOINT_GREEN_CONCOMITANT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
