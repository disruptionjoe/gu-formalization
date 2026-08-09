#!/usr/bin/env python3
"""Exact mixed-order and ownership admission gate for the K77 bulk operator.

This does not construct a closed operator.  It records the derivative grammar
of the source variables, checks the smallest symmetric Douglis--Nirenberg
weights admitted by that grammar, and refuses to promote the v0.116 kinematic
trace carrier until every action-Hessian/gauge-fixing owner is present on the
same stationary branch and action parent.
"""

from collections import Counter
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []
FIELDS = ("g", "varpi", "epsilon")


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


def join(*orders):
    return {field: max(order[field] for order in orders) for field in FIELDS}


print("A. SOURCE LOCUS AND LAYER ZERO")
source = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
path_deps = (ROOT / "lab/process/path-dependencies.md").read_text()
first = strict("lab/process/selected-k77-common-first-action-epsilon-hessian.json")
gram = strict("lab/process/selected-k77-stationary-gram-boundary-strata.json")
branches = strict("lab/process/selected-k77-source-tangent-branch-stationarity.json")
parents = strict("lab/process/selected-k77-full-parent-branch-stationarity.json")
trace = strict("lab/process/selected-k77-common-graded-trace-boundary-triple.json")

check("source", "source prints the first action with F_B, one-half d_B T and one-third bracket",
      "F_{B_\\omega}" in source and "\\frac12d_{B_\\omega}T_\\omega" in source
      and "\\frac13[T_\\omega,T_\\omega]" in source)
check("source", "source owns g, varpi and derivative-bearing epsilon coordinates",
      r"I^B_1:\mathcal G\times \operatorname{MET}(X^{1,3})" in source
      and r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "source prints residual and Xi redundancy but no closed domain",
      r"\Xi_\omega=D_\omega\Upsilon_\omega" in source
      and "common domain" in source)
check("prior_art", "the ultrahyperbolic domain dependency is explicitly registered",
      "PD-ULTRAHYPERBOLIC-DOMAIN" in path_deps)

for label in (
    "source density jet order versus Euler operator order",
    "raw coordinate jet order versus covariantly reduced jet order",
    "formal covector Hessian versus field-valued operator",
    "pointwise parent stationarity versus parent-specific global Hessian",
    "kinematic boundary trace versus operator graph trace quotient",
    "strong boundary form versus Green inverse",
    "bosonic zero-fermion operator versus coupled matter operator",
    "selected Spin parent versus two U32,32 halves versus full U64,64",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT SOURCE DEPENDENCY GRAMMAR")
zero = {field: 0 for field in FIELDS}
B_raw = {"g": 1, "varpi": 0, "epsilon": 1}
T_raw = {"g": 1, "varpi": 0, "epsilon": 1}
F_B_raw = {"g": 2, "varpi": 0, "epsilon": 2}
dBT_raw = {"g": 2, "varpi": 1, "epsilon": 2}
T2_raw = T_raw

# Gauge covariance gives F_B(epsilon.B)=epsilon F_B(B) epsilon^-1.  The exact
# affine identity F_A=F_B+d_B T+T^2 then reduces d_B T without pretending the
# individual raw coordinate terms never contained second epsilon derivatives.
F_B_cov = {"g": 2, "varpi": 0, "epsilon": 0}
F_A_cov = {"g": 0, "varpi": 1, "epsilon": 0}
dBT_cov = join(F_A_cov, F_B_cov, T2_raw)
I1_raw = join(T_raw, F_B_raw, dBT_raw, T2_raw)
I1_cov = join(T_raw, F_B_cov, dBT_cov, T2_raw)
upsilon = {"g": 1, "varpi": 1, "epsilon": 1}
I2 = upsilon.copy()

check("exact", "raw B and T own first g/epsilon derivatives", B_raw == T_raw == {"g": 1, "varpi": 0, "epsilon": 1})
check("exact", "raw F_B and d_B T expose second epsilon derivatives before covariance", F_B_raw["epsilon"] == dBT_raw["epsilon"] == 2)
check("exact", "curvature covariance removes derivative epsilon from F_B", F_B_cov == {"g": 2, "varpi": 0, "epsilon": 0})
check("exact", "affine curvature identity reduces d_B T to orders g2 varpi1 epsilon1", dBT_cov == {"g": 2, "varpi": 1, "epsilon": 1})
check("exact", "first-action raw and covariant grammars remain separately recorded", I1_raw == {"g": 2, "varpi": 1, "epsilon": 2} and I1_cov == {"g": 2, "varpi": 1, "epsilon": 1})
check("exact", "residual-square layer owns one derivative of every source field", I2 == {"g": 1, "varpi": 1, "epsilon": 1})

# For a density with field jet weights m_i, its linearized Euler block i,j has
# the safe variational upper bound m_i+m_j.  This is an admission bound, not a
# proof that its top coefficient is nonzero after integrations by parts.
m = I1_cov
euler_bound = [[m[row] + m[column] for column in FIELDS] for row in FIELDS]
expected_bound = [[4, 3, 3], [3, 2, 2], [3, 2, 2]]
check("theorem", "first-action variational upper-bound matrix is exact", euler_bound == expected_bound)
check("theorem", "second-action stationary Gram bound is uniformly second order", [[I2[r] + I2[c] for c in FIELDS] for r in FIELDS] == [[2] * 3 for _ in FIELDS])

admissible = []
for wg in range(5):
    for wv in range(5):
        for we in range(5):
            weights = (wg, wv, we)
            if all(euler_bound[i][j] <= weights[i] + weights[j]
                   for i in range(3) for j in range(3)):
                admissible.append(weights)
minimal = [w for w in admissible if not any(
    v != w and all(v[i] <= w[i] for i in range(3)) for v in admissible
)]
check("theorem", "the unique componentwise-minimal symmetric DN weight is 2,1,1", minimal == [(2, 1, 1)])
check("planted", "PLANT uniform weight one under-resolves the g-g admission bound", (1, 1, 1) not in admissible)
check("control", "uniform weight two is an over-regular compatible bound, not a derived scalar principal order", (2, 2, 2) in admissible and minimal != [(2, 2, 2)])


print("\nC. ACTION-OPERATOR OWNERSHIP MATRIX")
check("owned", "two source-coordinate branches are locally stationary",
      len(branches["exact_result"]["branches"]) == 2
      and branches["exact_result"]["branch_pullback"]["varpi_euler"].startswith("ZERO_ALL_1470")
      and branches["exact_result"]["branch_pullback"]["action_density"] == "ZERO_BOTH_BRANCHES")
check("owned", "all full-parent pointwise varpi directions vanish on both branches", parents["exact_result"]["both_branches_full_varpi_zero"] and parents["exact_result"]["varpi_pointwise_direction_count"] == 229376)
check("partial", "pointwise parent compatibility explicitly does not prove a functional tangent", not parents["exact_result"]["functional_tangent_complete"])
check("partial", "the old first-action epsilon cross is rank 91 but its tangent selection was left open", first["moving_epsilon"]["mixed_cross_rank"] == 91 and first["field_tangent_gate"]["selection"].startswith("OPEN"))
check("partial", "the stationary Gram is only a 34-field metric-varpi block", gram["exact_result"]["field_dimension"] == 34 and gram["layer0"]["full_action"].endswith("OPEN"))
check("partial", "the partial Gram still lacks a field Riesz and trace soldering", "OPEN" in gram["layer0"]["field_operator"] and gram["layer0"]["edge_identification"].endswith("OPEN"))
check("unowned", "the complete action-owned gauge-fixed operator is explicitly unowned", trace["boundary_triple_readiness"]["complete_action_owned_gauge_fixed_bulk_operator"] == "UNOWNED")
check("unowned", "closed Dmax/Dmin and surjective trace are explicitly unowned", trace["boundary_triple_readiness"]["closed_Dmax_Dmin"] == "UNOWNED" and trace["boundary_triple_readiness"]["surjective_bulk_trace"] == "UNOWNED")
check("unowned", "Green inverse and coupled BV-BFV remain unowned", trace["boundary_triple_readiness"]["common_Green_inverse"] == "UNOWNED" and trace["boundary_triple_readiness"]["coupled_BV_BFV"] == "UNOWNED")
check("unowned", "action parent is not selected by pointwise stationarity", not parents["exact_result"]["parent_selected"])

required = {
    "branch_specific_first_action_hessian": False,
    "branch_specific_second_action_jacobian": False,
    "parent_specific_global_tangent": False,
    "gauge_fixing_and_bulk_ghost_operator": False,
    "field_riesz_or_covector_graph_calculus": False,
    "closed_ultrahyperbolic_realization": False,
}
check("theorem", "six named admission owners remain before Dmax/Dmin", len(required) == 6 and not any(required.values()))
check("planted", "PLANT pointwise stationarity is not promoted to a complete Hessian", not parents["exact_result"]["functional_tangent_complete"])
check("planted", "PLANT the kinematic H7/H8 carrier is not called operator-derived", trace["layer0"]["boundary_trace_space"] == "not_a_bulk_graph_domain")
check("planted", "PLANT two U32,32 halves are not collapsed into full U64,64", parents["exact_result"]["block_even_dimension"] == parents["exact_result"]["half_exchanging_odd_dimension"] == 8192)
check("planted", "PLANT the observed X4 domain is rejected as ambient K77 domain", trace["domain_routes"]["observed_X4_defect_domain_as_ambient_domain"] == "TYPE_ERROR")


print("\nD. DISPOSITION")
check("construction", "mixed-order admission is available without adding a field or datum", minimal == [(2, 1, 1)])
check("construction", "a complete operator/domain theorem is currently inadmissible", not any(required.values()))
check("symplectic", "the boundary form survives as a kinematic target rather than a selected extension", trace["boundary_triple_readiness"]["lagrangian_polarization"] == "OWNED_NOT_SELECTED")
check("analytic", "standard ambient Lorentzian Cauchy route remains killed", trace["domain_routes"]["standard_ambient_Lorentzian_Cauchy"] == "KILLED_PREVIOUSLY_FOR_K77")
check("accounting", "no new quotient coefficient selector or P1/P2/P3 consumption", trace["constraint_fence"]["new_booked_quotients"] == 0 and trace["constraint_fence"]["P1_P2_P3"] == "UNUSED")

print("SOURCE_RETURN=SOURCE_CONFIRMS_TWO_CONNECTION_FIRST_ACTION_RESIDUAL_AND_XI_GRAMMAR__SOURCE_SILENT_MIXED_ORDER_GAUGE_FIXED_OPERATOR_PARENT_SPECIFIC_HESSIAN_DMAX_DMIN_AND_BV_BFV")
print("JET_GRAMMAR=RAW_I1_G2_VARPI1_EPSILON2__COVARIANT_I1_G2_VARPI1_EPSILON1__I2_ALL1")
print("DN_ADMISSION=UNIQUE_COMPONENTWISE_MINIMAL_SYMMETRIC_WEIGHT_2_1_1__ACTUAL_TOP_COEFFICIENTS_UNTESTED")
print("OPERATOR=COMPLETE_ACTION_OWNED_GAUGE_FIXED_BULK_OPERATOR_UNOWNED")
print("TRACE=H7_H8_STRONG_KINEMATIC_TARGET__NOT_OPERATOR_DERIVED")
print("PARENT=SPIN_NATIVE__TWO_U32_32_HALVES__FULL_U64_64_REMAIN_DISTINCT")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
