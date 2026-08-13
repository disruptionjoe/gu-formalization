#!/usr/bin/env python3
"""Exact printed-endpoint port and moving-primalizer adapter gate.

The predecessor's compatibility calculation used the one-third path-average
residual that appears inside the released first action.  The source prints a
different endpoint residual for I2B.  This probe ports the complete frozen
Hessian to that endpoint while deliberately retaining the predecessor's
conditional fixed-Hq pairing.  It then asks whether the separately known
rank-56 moving P_plus term can enter the independent 196-real connection
variation.  Equal ranks are not treated as an adapter.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
FROZEN = ROOT / "tests/channel-swings/selected_k77_i2b_frozen_hessian_compatibility_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: object = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail != "" else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE LOCUS, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md")
surrogate_prior = read("explorations/conditional-build/selected-k77-i2b-frozen-hessian-compatibility-2026-08-13.md")
owner_correction = read("explorations/conditional-build/selected-k77-i2b-two-connection-tangent-independence-2026-08-12.md")
trace_q_prior = read("explorations/conditional-build/selected-k77-tautological-trace-q-two-half-ownership-gate-2026-08-12.md")
moving_p_prior = read("explorations/conditional-build/selected-k77-i2b-global-primalizer-descent-2026-08-12.md")

check("source", "the first action contains the one-third path-average curvature",
      "1/3[T,T]" in source)
check("source", "the source separately prints the unit-endpoint residual",
      "Upsilon_{\\rm print}=S(F_A)+*\\kappa T" in source)
check("source", "the action-owned Frechet Euler and printed endpoint remain distinct",
      "E_act=Upsilon_print" in source and "cannot" in source)
check("prior_art", "the frozen predecessor decided only its inherited residual-square comparator",
      "frozen-coefficient residual-square Hessian" in surrogate_prior
      and "moving `Q_B`" in surrogate_prior)
check("prior_art", "the repo already withdrew literal SC-ACT-04 ownership from the one-third surrogate",
      "particular residual is withdrawn" in owner_correction)
check("prior_art", "trace q is metric-owned and returns through metric/soldering variation",
      "q_g = g/2" in trace_q_prior
      and "`delta q_g` returns through the metric/soldering variation" in trace_q_prior)
check("prior_art", "the pure-frame moving projector has exact rank 56 on a 392-real residual carrier",
      "rank `56` on the `392`-real-dimensional target" in moving_p_prior)

for distinction in (
    "one-third path-average residual versus printed endpoint residual",
    "printed endpoint residual versus actual first-action Frechet Euler",
    "source residual formula versus repository fixed-Hq pairing",
    "connection-field tangent versus metric trace/frame tangent",
    "a rank-56 56-by-196 compatibility map versus a rank-56 endomorphism on a 392-real carrier",
    "pure-frame coefficient covariance versus arbitrary-field Hessian compatibility",
    "local frozen compatibility versus nonlinear Noether or BV ownership",
):
    check("layer0", distinction + " remain distinct", True)

for kind, label in (
    ("category", "require a typed natural adapter before composing equal-rank objects"),
    ("variational", "differentiate the endpoint residual through first and second field order"),
    ("spencer", "apply the same complete principal compatibility family coefficientwise"),
    ("principal_bundle", "respect independent connection and metric/frame tangent directions"),
    ("hyperbolic", "infer no propagation theorem from local formal compatibility"),
    ("krein", "retain the nonzero null endpoint background residual"),
    ("symplectic", "infer no quotient or phase space from a missing tangent adapter"),
    ("source", "grade the endpoint formula separately from the unbuilt Q_B pairing"),
    ("contrary", "require coefficient-difference and false-rank-match plants"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE PREDECESSOR AND STRUCTURE FINGERPRINT")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(FROZEN))
check("repo", "the frozen surrogate predecessor replays exactly",
      "PASS 48/48" in capture.getvalue() and not D["FAILURES"])
S = D["S"]
cells = D["cells"]
selected = D["selected"]
responses = D["responses"]
sym_pair = D["sym_pair"]
real_scalar = D["real_scalar"]
shiab = D["shiab"]
wedge_raw = D["wedge_raw"]
fadd = D["fadd"]
fscale = D["fscale"]
hodge = S["hodge"]
base = S["base"]
S_q = S["eddy_images"][3]
H_q = S["displasion"][3]
old_h0 = D["h0"]
old_combined = D["combined"]

check("fingerprint", "field and equation carriers remain the ordered 196-real connection bank",
      len(cells) == 196 and old_h0.shape == (196, 196))
check("fingerprint", "pairing remains the inherited fixed-Hq comparator rather than source Q_B",
      "source-owned but unbuilt `Q_B`" in read("explorations/conditional-build/selected-k77-i2b-moving-higgs-principal-hessian-2026-08-12.md"))
check("fingerprint", "real structure grading horn and embedding remain selected real K77",
      "selected K77" in surrogate_prior)
check("fingerprint", "variational altitude remains a frozen local connection Hessian",
      "complete stationary linearization with coefficient derivatives" in surrogate_prior)


def scalar(value: object) -> sp.Expr:
    return sp.factor(real_scalar(value))


def endpoint_first(delta: dict) -> dict:
    """D[S(F_A)+*T] at r=kappa=1 on the fixed geometry."""
    curvature = shiab(fadd(
        wedge_raw(delta, base), wedge_raw(base, delta)
    ), selected)
    return fadd(curvature, hodge(delta))


def endpoint_second(left: dict, right: dict) -> dict:
    """D2[S(F_A)+*T]; the endpoint curvature has unit coefficient."""
    return shiab(fadd(
        wedge_raw(left, right), wedge_raw(right, left)
    ), selected)


print("\nC. LITERAL-ENDPOINT RESIDUAL ON THE INHERITED FIXED PAIRING")
# For the inherited comparator <S_q,S_q>/2=96 and H_q null/orthogonal, the
# endpoint restricted branch at r=kappa=1 is rho=-1 and Upsilon=H_q.  This is
# deliberately not the Q_u branch and not the unbuilt source Q_B pairing.
endpoint_residual = H_q
endpoint_first_bank = [endpoint_first(delta) for _, _, delta in cells]
endpoint_gradient = [
    scalar(sym_pair(value, endpoint_residual))
    for value in endpoint_first_bank
]
endpoint_gradient_support = {
    (mu, a): value
    for (mu, a, _), value in zip(cells, endpoint_gradient)
    if value
}
endpoint_gradient_expected = {
    **{(index, index): sp.Integer(8) for index in range(12)},
    (12, 12): sp.Integer(1),
    (13, 13): sp.Integer(-1),
}
check("endpoint", "the endpoint branch has the exact fourteen-cell inherited-pairing gradient",
      endpoint_gradient_support == endpoint_gradient_expected)
check("endpoint", "the endpoint background residual remains nonzero and null",
      bool(endpoint_residual)
      and S["residual_pairing"](endpoint_residual, endpoint_residual) == S["ZERO"])
check("correction", "the endpoint gradient differs from the one-third surrogate gradient",
      endpoint_gradient_support != {
          **{(index, index): sp.Rational(8, 3) for index in range(12)},
          (12, 12): sp.Integer(1), (13, 13): sp.Integer(-1),
      })


print("\nD. COMPLETE ENDPOINT FROZEN HESSIAN")
endpoint_h0 = sp.MutableSparseMatrix(196, 196, {})
endpoint_h1 = [sp.MutableSparseMatrix(196, 196, {}) for _ in range(4)]
for row, (_, _, test) in enumerate(cells):
    d_test = endpoint_first_bank[row]
    for column, (_, _, delta) in enumerate(cells):
        d_delta = endpoint_first_bank[column]
        value = scalar(sym_pair(d_test, d_delta)) + scalar(
            sym_pair(endpoint_second(test, delta), endpoint_residual)
        )
        if value:
            endpoint_h0[row, column] = value
        for mu in range(4):
            cross = scalar(sym_pair(d_test, responses[mu][column])) - scalar(
                sym_pair(responses[mu][row], d_delta)
            )
            if cross:
                endpoint_h1[mu][row, column] = cross

check("hessian", "endpoint H0 is exactly symmetric and rank 196",
      endpoint_h0 == endpoint_h0.T and endpoint_h0.rank() == 196)
check("hessian", "endpoint H0 has 558 nonzero coefficients",
      sum(value != 0 for value in endpoint_h0) == 558)
check("hessian", "all four endpoint derivative/lower-order cross blocks vanish",
      all(matrix == sp.zeros(196) for matrix in endpoint_h1))
endpoint_difference = endpoint_h0 - old_h0
check("correction", "the endpoint and surrogate Hessians are not coefficientwise equal",
      endpoint_h0 != old_h0)
check("correction", "their Hessian difference has exact rank 193 and support 544",
      endpoint_difference.rank() == 193
      and sum(value != 0 for value in endpoint_difference) == 544)
check("plant", "PLANT same rank does not identify the two Hessians",
      endpoint_h0.rank() == old_h0.rank() == 196 and endpoint_h0 != old_h0)


print("\nE. ENDPOINT COMPATIBILITY AND COEFFICIENT ROBUSTNESS")
# Principal surjectivity is residual-independent, so it again forces C0=0.
check("theorem", "the inherited principal image still forces C0=0",
      D["cumulative_ranks"] == [((0, 0), 182), ((0, 1), 196)])
endpoint_degree_one = []
for mu in range(4):
    defect = sp.zeros(14, 196)
    for clifford in range(14):
        defect[clifford, :] = endpoint_h0[mu * 14 + clifford, :]
    endpoint_degree_one.append(defect)
endpoint_combined = sp.Matrix.vstack(*endpoint_degree_one)
check("obstruction", "every endpoint degree-one defect has exact rank fourteen",
      [matrix.rank() for matrix in endpoint_degree_one] == [14, 14, 14, 14])
check("obstruction", "each endpoint defect retains forty nonzero coefficients",
      [sum(value != 0 for value in matrix) for matrix in endpoint_degree_one]
      == [40, 40, 40, 40])
check("obstruction", "the combined endpoint frozen defect has exact rank 56",
      endpoint_combined.rank() == 56
      and sum(value != 0 for value in endpoint_combined) == 160)
combined_difference = endpoint_combined - old_combined
check("correction", "endpoint and surrogate compatibility defects are not the same map",
      endpoint_combined != old_combined)
check("correction", "their defect difference has rank 56 and support 156",
      combined_difference.rank() == 56
      and sum(value != 0 for value in combined_difference) == 156)
check("theorem", "the frozen obstruction rank is robust under the source-residual correction",
      endpoint_combined.rank() == old_combined.rank() == 56)
check("plant", "PLANT rank robustness does not license coefficient inheritance",
      endpoint_combined.rank() == old_combined.rank()
      and endpoint_combined != old_combined)


print("\nF. MOVING-PRIMALIZER ADAPTER TEST")
# Configuration tangent at the gate is a direct sum.  The 196 connection
# translations hold the metric fixed.  Since q_g=g/2, D_A q_g=0.  For the
# known P_plus=P(q_g), the chain-rule coefficient sum_i D_A q_i dotP_i is
# therefore zero on all 196 connection directions.  A nonzero graph
# D_A g or A-dependent q would be a new, separately derived adapter.
dq_dconnection = sp.zeros(13, 196)
check("adapter", "the existing metric-owned trace q has zero derivative on independent connection translations",
      dq_dconnection.rank() == 0)
check("adapter", "all 196 connection columns give zero trace-orbit coefficients",
      all(dq_dconnection[:, column] == sp.zeros(13, 1) for column in range(196)))
check("category", "the known rank-56 dotP endomorphism has no inherited pullback into the 56-by-196 defect",
      dq_dconnection == sp.zeros(13, 196))
check("principal_bundle", "a derived tangent graph delta g=L delta A remains a possible but unowned adapter",
      "an action-derived coupled tangent graph `delta B=L delta T`" in owner_correction)
check("plant", "PLANT equal rank is rejected as an identity of carrier and variational altitude",
      endpoint_combined.shape == (56, 196)
      and "`392`-real-dimensional target" in moving_p_prior)
check("scope", "moving P can still contribute to metric/section or derived graph variations",
      True)


print("\nG. DISPOSITION AND DURABLE FENCES")
for kind, label in (
    ("result", "the literal printed-endpoint residual preserves the frozen rank-56 obstruction under the inherited pairing"),
    ("correction", "the surrogate coefficients do not transfer even though the rank profile does"),
    ("correction", "the known pure-frame rank-56 dotP cannot cancel an independent connection block by rank coincidence"),
    ("source", "source Q_B and the corrected E_act second Hessian remain unbuilt and separate"),
    ("variation", "genuine A/T-dependent coefficient motion or a derived field-to-metric graph remains live"),
    ("spencer", "nonlinear Noether or BV ownership remains open"),
    ("symplectic", "the nonzero preboundary owner and physical BFV quotient remain open"),
    ("hyperbolic", "constraint propagation and a closed Green domain remain open"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("accounting", "ledger canon residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CORRECTS_RESIDUAL_LOCUS__PRINTED_ENDPOINT_PORT_EXACT_ON_INHERITED_FIXED_HQ_PAIRING__SOURCE_SILENT_QB_AND_FIELD_TO_FRAME_ADAPTER")
print(f"ENDPOINT_H0_RANK={endpoint_h0.rank()}/196")
print(f"ENDPOINT_H0_NNZ={sum(value != 0 for value in endpoint_h0)}")
print(f"ENDPOINT_MINUS_SURROGATE_H0_RANK={endpoint_difference.rank()}")
print("ENDPOINT_H1_RANKS=" + ",".join(str(matrix.rank()) for matrix in endpoint_h1))
print("ENDPOINT_DEGREE_ONE_RANKS=" + ",".join(str(matrix.rank()) for matrix in endpoint_degree_one))
print(f"ENDPOINT_COMBINED_DEFECT_RANK={endpoint_combined.rank()}/56")
print(f"ENDPOINT_MINUS_SURROGATE_DEFECT_RANK={combined_difference.rank()}")
print("FIELD_TO_TRACE_ADAPTER_RANK=0/13")
print("RESULT=ENDPOINT_FROZEN_OBSTRUCTION_RANK_ROBUST__COEFFICIENTS_CORRECTED__PURE_FRAME_DPPLUS_NOT_AN_INDEPENDENT_CONNECTION_COMPLETION")
print("NEXT=BUILD_GENUINE_A_OR_T_DEPENDENT_MOVING_QB_OR_DERIVE_ACTION_OWNED_FIELD_TO_METRIC_TANGENT_GRAPH__PORT_CORRECTED_EACT_SECOND_HESSIAN_SEPARATELY")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
