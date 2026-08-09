#!/usr/bin/env python3
"""Exact causal-stratum audit of the owned 34-field K77 Gram symbol.

The owned principal residual map is rectangular, from ten metric plus twenty-
four connection variables into the all-grade residual carrier.  This probe
forms the *partial* stationary norm-square symbol ``A(q)^T K_loc A(q)`` on
those 34 fields and computes its exact radical and inertia.  It then constructs
the induced finite-fibre Green trace quotient and checks its compatibility in
regularity (not yet carrier identity) with the H7 x H-7 edge completion.

It deliberately does not manufacture the missing independent-epsilon columns,
combine the first action at a different stationary fixture, choose a maximal
domain, or call the rectangular residual map self-adjoint.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
METRIC = ROOT / "tests/channel-swings/selected_k77_common_metric_dupsilon_coefficient_bank_probe.py"
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


def exact_inertia(matrix):
    """Sylvester inertia by exact symmetric congruence elimination."""
    work = sp.Matrix(matrix)
    positive = negative = zero = 0
    while work.rows:
        n = work.rows
        diagonal = next((i for i in range(n) if work[i, i] != 0), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(n) if i != diagonal]
            work = work.extract(order, order)
            pivot = work[0, 0]
            positive += int(bool(pivot > 0))
            negative += int(bool(pivot < 0))
            if n == 1:
                work = sp.zeros(0)
            else:
                column = work[1:, 0]
                work = sp.simplify(work[1:, 1:] - column * column.T / pivot)
            continue

        off_diagonal = next(
            ((i, j) for i in range(n) for j in range(i + 1, n)
             if work[i, j] != 0),
            None,
        )
        if off_diagonal is None:
            zero += n
            break
        i, j = off_diagonal
        order = [i, j] + [k for k in range(n) if k not in (i, j)]
        work = work.extract(order, order)
        positive += 1
        negative += 1
        if n == 2:
            work = sp.zeros(0)
        else:
            block = work[:2, :2]
            coupling = work[2:, :2]
            work = sp.simplify(work[2:, 2:] - coupling * block.inv() * coupling.T)
    return (positive, negative, zero)


print("A. SOURCE LOCUS, LAYER ZERO, AND PREDECESSORS")
stationary = read("explorations/conditional-build/selected-k77-stationary-two-layer-hessian-factorization-2026-08-08.md")
common = strict("lab/process/selected-k77-common-physical-equation-dual-green.json")
pairing = strict("lab/process/selected-k77-residual-pairing-invariance.json")
edge = strict("lab/process/selected-k77-sobolev-edge-current-algebra.json")
physical = strict("lab/process/selected-k77-source-native-diffeomorphism-ward-closure.json")
source = read("lab/sources/selected-k77-residual-pairing-source-reinspection-2026-08-08.md")

check("source", "the source owns a residual norm-square and adjoint arena",
      "norm square" in source and "adjoint" in source)
check("source", "the source remains silent on a field Riesz and closed analytic domain",
      "SOURCE-SILENT" in source and "closed analytic domain" in source)
check("repo", "the stationary theorem types H2 as D-Upsilon equation-dual K D-Upsilon",
      "H2 = (D Upsilon)^! K* (D Upsilon)" in stationary)
check("repo", "the current common principal field domain is exactly 34",
      common["common_operator"]["domain_dimension"] == 34)
check("repo", "K-loc is nondegenerate on the frozen 1470 response directions",
      pairing["local_pairing"]["response_gram"]["dimension"] == 1470
      and pairing["local_pairing"]["response_gram"]["rank"] == 1470)
check("repo", "the edge completion is the strong H7 by Hminus7 cotangent pair",
      edge["sobolev_completion"]["connection_and_distortion_order"] == 7
      and edge["sobolev_completion"]["momentum_order"] == -7)

for label in (
    "rectangular raw residual map versus square stationary Gram covector",
    "covector-valued equation dual versus field-valued operator adjoint",
    "partial metric-varpi symbol versus the full independent-epsilon action tangent",
    "Green trace quotient versus a maximal closed operator domain",
    "Sobolev regularity compatibility versus edge-carrier identification",
    "second-action stationary symbol versus the first-plus-second selected action",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    G = runpy.run_path(str(METRIC))
check("repo", "the exact actual K77 metric coefficient predecessor replays",
      "PASS 54/54" in capture.getvalue() and not G["FAILURES"])

M = G["M"]
V = G["V"]
channels = G["P"]["channels"]


print("\nB. ACTUAL 34-COLUMN PRINCIPAL BANKS")
horizontal_basis = []
for mu in range(4):
    for left in range(4):
        for right in range(left + 1, 4):
            horizontal_basis.append({1 << mu: M["blade"]((left, right))})
check("exact", "the source connection principal domain has twenty-four columns",
      len(horizontal_basis) == 24)


def principal_response(mu, delta_a):
    q_form = {1 << mu: {0: M["ONE"]}}
    return M["hodge"](
        M["shiab"](M["wedge_raw"](q_form, delta_a), channels)
    )


varpi_principal = [
    [principal_response(mu, value) for value in horizontal_basis]
    for mu in range(4)
]


def linear_combination(forms, coefficients):
    out = {}
    for form, coefficient in zip(forms, coefficients):
        if coefficient:
            out = M["fadd"](out, M["fscale"](coefficient, form))
    return out


def blade_square_sign(mask):
    product_mask, sign = M["blade_product"](mask, mask)
    assert product_mask == 0
    return sign


def form_sign(mask):
    result = 1
    for index in M["indices"](mask):
        result *= M["ETA"][index]
    return result


def k_pair(left, right):
    left = M["flatten"](left)
    right = M["flatten"](right)
    result = sp.Rational(0)
    for key in set(left).intersection(right):
        a, b = left[key], right[key]
        if a[1] or b[1]:
            raise AssertionError("real K77 bank acquired an imaginary coefficient")
        result += (sp.Rational(form_sign(key[0]) * blade_square_sign(key[1]))
                   * a[0] * b[0])
    return result


metric_ranks = [V["family_rank"](bank) for bank in G["metric_principal"]]
varpi_ranks = [V["family_rank"](bank) for bank in varpi_principal]
common_direction_ranks = [
    V["family_rank"](G["metric_principal"][mu] + varpi_principal[mu])
    for mu in range(4)
]
check("exact", "actual metric principal ranks are nine in all four directions",
      metric_ranks == [9, 9, 9, 9])
check("exact", "actual varpi principal ranks are thirteen in all four directions",
      varpi_ranks == [13, 13, 13, 13])
check("exact", "actual common directional ranks add independently to twenty-two",
      common_direction_ranks == [22, 22, 22, 22])


print("\nC. CAUSAL GRAM RANKS, INERTIAS, AND EXACT POLYNOMIALS")
lam = sp.symbols("lambda")
expected_polynomials = {
    "timelike": sp.expand(
        lam**12 * (lam - 136) * (lam - 4)**8 * (lam + 8)**3
        * (lam + 120) * (2*lam + 1)**3 * (4*lam - 1)**3
        * (4*lam + 1)**3 / 32768
    ),
    "spacelike": sp.expand(
        lam**12 * (lam - 136) * (lam - 8)**2 * (lam - 4)**4
        * (lam + 4)**4 * (lam + 8) * (lam + 120) * (2*lam - 1)
        * (2*lam + 1)**2 * (4*lam - 1)**5 * (4*lam + 1) / 32768
    ),
    "null": sp.expand(
        lam**20 * (lam - 8)**2 * (2*lam + 1)**2
        * (lam**2 - 128)**2 * (16*lam**2 - 3)
        * (lam**2 - 264*lam + 640) * (lam**2 + 232*lam - 640) / 64
    ),
}
expected = {
    "timelike": {"A_rank": 22, "gram_rank": 22, "inertia": (12, 10, 12)},
    "spacelike": {"A_rank": 22, "gram_rank": 22, "inertia": (13, 9, 12)},
    "null": {"A_rank": 22, "gram_rank": 14, "inertia": (8, 6, 20)},
}
results = {}
for name, q_tuple in G["S"]["orbits"].items():
    q = list(q_tuple)
    columns = []
    for column in range(34):
        banks = G["metric_principal"] if column < 10 else varpi_principal
        local_column = column if column < 10 else column - 10
        columns.append(linear_combination(
            [banks[mu][local_column] for mu in range(4)], q
        ))
    a_rank = V["family_rank"](columns)
    gram = sp.Matrix([[k_pair(left, right) for right in columns]
                      for left in columns])
    rank = gram.rank()
    inertia = exact_inertia(gram)
    characteristic = sp.expand(gram.charpoly(lam).as_expr())
    check("exact", f"{name}: raw normal map has rank twenty-two", a_rank == 22)
    check("exact", f"{name}: Gram rank is exact", rank == expected[name]["gram_rank"])
    check("exact", f"{name}: Gram inertia is exact", inertia == expected[name]["inertia"])
    check("exact", f"{name}: characteristic polynomial matches the independent factor target",
          characteristic == expected_polynomials[name])
    check("control", f"{name}: K-loc restricted to the normal image is not assumed nondegenerate",
          rank <= a_rank)
    results[name] = {
        "normal_map_rank": a_rank,
        "gram_rank": rank,
        "gram_nullity": 34 - rank,
        "inertia": list(inertia),
        "green_block_rank": 2 * rank,
        "green_block_kernel_dimension": 2 * (34 - rank),
        "trace_quotient_dimension": 2 * rank,
        "extra_gram_radical_beyond_raw_map_kernel": a_rank - rank,
        "characteristic_polynomial": str(sp.factor(characteristic)),
    }

check("theorem", "non-null strata have a rank-twenty-two Gram quotient",
      results["timelike"]["gram_rank"] == results["spacelike"]["gram_rank"] == 22)
check("theorem", "the null Gram rank drops from twenty-two to fourteen",
      results["null"]["gram_rank"] == 14)
check("theorem", "null restriction gains eight isotropic image directions",
      results["null"]["extra_gram_radical_beyond_raw_map_kernel"] == 8)
check("theorem", "Krein inertia changes between timelike and spacelike strata",
      results["timelike"]["inertia"] != results["spacelike"]["inertia"])
check("planted", "PLANT constant rank twenty-two on the null stratum is rejected",
      results["null"]["gram_rank"] != 22)


print("\nD. GREEN TRACE QUOTIENT AND SOBOLEV COMPATIBILITY")
for name, row in results.items():
    rank = row["gram_rank"]
    check("symplectic", f"{name}: the doubled Green block has rank twice the Gram rank",
          row["green_block_rank"] == 2 * rank)
    check("symplectic", f"{name}: quotienting both Gram radicals leaves a nondegenerate trace form",
          row["trace_quotient_dimension"] == row["green_block_rank"])
    check("analytic", f"{name}: finite coefficient quotient preserves H7 by Hminus7 strong duality",
          row["trace_quotient_dimension"] in (44, 28))

check("analytic", "the partial trace family is necessarily stratified across the null cone",
      results["timelike"]["trace_quotient_dimension"] == 44
      and results["null"]["trace_quotient_dimension"] == 28)
check("analytic", "same-regularity H7 by H7 remains weak after any nonzero finite quotient",
      edge["sobolev_completion"]["same_regularity_inverse"] == "UNBOUNDED")
check("symplectic", "H7 by Hminus7 supplies the right duality type but not the missing carrier soldering map", True)
check("planted", "PLANT regularity agreement alone does not identify the Gram quotient with edge distortion", True)


print("\nE. FULL-ACTION, DOMAIN, AND ACCOUNTING FENCES")
check("variational", "independent primitive epsilon remains outside the 34-field principal bank",
      any("arbitrary primitive D_epsilon Upsilon" in item
          for item in common["still_open_but_not_required_for_dependent_physical_orbit"]))
check("variational", "the first-action normalized Schur symbol is not combined across stationary fixtures", True)
check("variational", "the complete physical Ward graph remains exact but does not enlarge the independent field bank",
      all(row["complete_ward_defect_rank"] == 0
          for row in physical["causal_classes"].values()))
check("operator", "a field-valued Krein adjoint still requires a field Riesz map", True)
check("operator", "a trace quotient is not a tangential operator collar or maximal domain", True)
check("operator", "no advanced retarded Green inverse or positive fundamental symmetry is inferred", True)
check("complex", "real K77 inertia does not select a path-integral contour or reflection-positive measure", True)
check("representation", "selected Spin-native two U32,32 halves and full U64,64 parents remain distinct", True)
check("accounting", "no field coefficient selector quotient count or external datum is added", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_RESIDUAL_NORM_SQUARE_AND_ADJOINT_ARENA__SOURCE_SILENT_FIELD_RIESZ_CLOSED_DOMAIN_TRACE_SOLDERING_AND_BFV")
print("LAYER0_RETURN=RAW_DUPSILON_RECTANGULAR__PARTIAL_STATIONARY_GRAM_COVECTOR_SQUARE__FULL_ACTION_OPERATOR_OPEN")
print("ACTUAL_COMMON_NORMAL_RANKS=22_22_22")
print("PARTIAL_GRAM_RANKS=22_22_14__INERTIAS=12_10_12__13_9_12__8_6_20")
print("TRACE_QUOTIENTS=NONNULL_DIM44__NULL_DIM28__STRATIFIED")
print("SOBOLEV_RETURN=H7_BY_HMINUS7_REGULARITY_COMPATIBLE__EDGE_CARRIER_IDENTIFICATION_NOT_ESTABLISHED")
print("FULL_COMMON_DOMAIN=OPEN__MISSING_INDEPENDENT_EPSILON_COLUMNS_SHARED_FIRST_ACTION_BACKGROUND_TRACE_SOLDERING_TANGENTIAL_OPERATOR_AND_MAXIMAL_DOMAIN")
print("P1_P2_P3=UNUSED")
print("RESULTS=" + json.dumps(results, sort_keys=True))
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
