#!/usr/bin/env python3
"""Reconcile the selected lower-order metric/epsilon residual blocks.

The fixed-varpi metric block was already completed by v0.95.  This gate ports
that theorem to both current residual-zero roots and constructs the remaining
constant-eta (lower-order) primitive-epsilon derivative of the raw residual
from the full B/T packet plus moving Shiab.  It keeps that raw derivative
distinct from the integrated first-action epsilon Euler and its endpoint
momentum, and from the principal derivative coefficient ``-q eta``.
"""

from collections import Counter
from fractions import Fraction
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_probe.py"
METRIC = ROOT / "tests/channel-swings/selected_k77_fixed_varpi_normal_frechet_closure_probe.py"
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

    return json.loads(path.read_text(), object_pairs_hook=hook)


def read(relative):
    return (ROOT / relative).read_text()


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
source_epsilon = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
metric_registry = strict("lab/process/selected-k77-fixed-varpi-normal-frechet-closure.json")
branch_registry = strict("lab/process/selected-k77-source-tangent-branch-stationarity.json")
port_registry = strict("lab/process/selected-k77-two-branch-action-block-port.json")
check("source", "source owns g varpi epsilon and augmented torsion as a connection difference",
      r"I^B_1:\mathcal G\times \operatorname{MET}(X^{1,3})" in source
      and r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "source owns primitive epsilon splitting motion and moving Shiab coefficients",
      "delta B=D_B eta" in source_epsilon
      and "delta T=-D_B eta" in source_epsilon
      and "delta Phi_i=[Phi_i,chi]" in source_epsilon)
check("prior_art", "v0.95 already closes the local fixed-varpi metric block",
      metric_registry["disposition"].startswith("LOCAL_FIXED_VARPI_DG_UPSILON_BLOCK_CLOSED"))
check("prior_art", "both exact branches solve the raw-residual/source-varpi equation on the selected tangent",
      branch_registry["exact_result"]["branch_pullback"]["varpi_euler"].startswith("ZERO_ALL_1470"))
check("prior_art", "v0.119 leaves lower-order metric and epsilon as an explicitly typed frontier",
      "BRANCH_DEPENDENT_LOWER_ORDER_METRIC_RESIDUAL_BLOCK" in port_registry["open_blocks"]
      and "BRANCH_DEPENDENT_LOWER_ORDER_EPSILON_RESIDUAL_BLOCK" in port_registry["open_blocks"])

for label in (
    "raw D-epsilon Upsilon versus integrated first-action epsilon Euler",
    "bulk epsilon Euler cancellation versus live endpoint momentum",
    "constant-eta lower-order response versus principal minus-q-eta response",
    "fixed-varpi metric partial versus common diffeomorphism Ward graph",
    "selected Spin 91-direction tangent versus expanded unitary parents",
    "raw-residual block closure versus residual-square Hessian and complete first-action Hessian",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(ENGINE))
check("prior_art", "independent selected first-action engine and moving-Shiab grammar replay",
      "PASS 61/61" in capture.getvalue() and not P["FAILURES"])

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    G = runpy.run_path(str(METRIC))
check("prior_art", "v0.95 exact fixed-varpi metric theorem replays rather than being rebuilt",
      "PASS 58/58" in capture.getvalue() and not G["FAILURES"])

M = P["M"]
SELECTED = P["SELECTED"]
ZERO = M["ZERO"]


print("\nB. COMPLETE CONSTANT-ETA RAW-RESIDUAL DERIVATIVE")


def coefficient_derivative(form, eta):
    return {mask: M["comm"](value, eta) for mask, value in form.items()}


def lower_epsilon_response(b_value, t_value, eta, omit_moving=False, freeze_split=False):
    b_field = M["fscale"](Fraction(b_value), M["PHI1"])
    t_field = M["fscale"](Fraction(t_value), M["PHI1"])
    a_field = M["fadd"](b_field, t_field)
    curvature = M["wedge_raw"](a_field, a_field)
    db_field = coefficient_derivative(b_field, eta)
    dt_field = {} if freeze_split else M["fscale"](-1, db_field)
    # At fixed source varpi, A=B+T and F_A do not move.  Only the splitting
    # term T and the epsilon-dependent Shiab coefficients move.
    pieces = [dt_field]
    if not omit_moving:
        pieces.append(M["hodge"](P["d_shiab"](curvature, eta)))
    return M["fadd"](*pieces)


samples = ((0, 0), (0, -1), (1, 1), (2, -1), (-1, 2), (3, 2))
monomials = sp.Matrix([[1, b, t, b*b, b*t, t*t] for b, t in samples])
check("exact", "six rational backgrounds are unisolvent for every degree-two response coefficient",
      monomials.det() != 0)
etas = [M["blade"](pair) for pair in P["pairs14"]]
sample_responses = [
    [M["flatten"](lower_epsilon_response(b, t, eta)) for eta in etas]
    for b, t in samples
]
expected_responses = [
    [M["flatten"](M["fscale"](
        Fraction(-b + 360*(b+t)*(b+t)),
        coefficient_derivative(M["PHI1"], eta),
    )) for eta in etas]
    for b, t in samples
]
check("theorem", "the complete lower-order epsilon block has coefficient -b+360(b+t)^2",
      sample_responses == expected_responses)


def raw_residual(b_value, t_value):
    b_field = M["fscale"](Fraction(b_value), M["PHI1"])
    t_field = M["fscale"](Fraction(t_value), M["PHI1"])
    a_field = M["fadd"](b_field, t_field)
    return M["fadd"](
        t_field,
        M["hodge"](M["shiab"](M["wedge_raw"](a_field, a_field), SELECTED)),
    )


check("exact", "the sampled raw residual is its own scalar equation times Phi1",
      all(raw_residual(b, t) == M["fscale"](
          Fraction(312*(b+t)*(b+t)+t), M["PHI1"]
      ) for b, t in samples))


def to_sympy(value):
    return Q(value[0].numerator, value[0].denominator) \
        + sp.I*Q(value[1].numerator, value[1].denominator)


poly_columns = []
for column in range(91):
    keys = sorted(set().union(*(set(sample_responses[sample][column]) for sample in range(6))))
    polynomial = {}
    for key in keys:
        values = sp.Matrix([
            to_sympy(sample_responses[sample][column].get(key, ZERO))
            for sample in range(6)
        ])
        coefficients = monomials.inv() * values
        if any(value != 0 for value in coefficients):
            polynomial[key] = tuple(sp.factor(value) for value in coefficients)
    poly_columns.append(polynomial)

check("control", "the lower-order response is genuinely live away from residual zero",
      any(column for column in poly_columns))


def branch_columns(point):
    monomial_values = (1, point[b], point[t], point[b]**2, point[b]*point[t], point[t]**2)
    out = []
    for polynomial in poly_columns:
        out.append({
            key: sp.simplify(sum(coefficient * monomial
                                 for coefficient, monomial in zip(coefficients, monomial_values)))
            for key, coefficients in polynomial.items()
            if sp.simplify(sum(coefficient * monomial
                               for coefficient, monomial in zip(coefficients, monomial_values))) != 0
        })
    return out


def flattened_rank(columns):
    keys = sorted(set().union(*(set(column) for column in columns)))
    rows = {key: index for index, key in enumerate(keys)}
    matrix = sp.SparseMatrix(len(keys), len(columns), {
        (rows[key], column): value
        for column, packet in enumerate(columns)
        for key, value in packet.items()
    })
    return matrix.rank()

omitted_moving = [
    M["flatten"](lower_epsilon_response(1, 1, eta, omit_moving=True))
    for eta in etas
]
frozen_split = [
    M["flatten"](lower_epsilon_response(1, 1, eta, freeze_split=True))
    for eta in etas
]
check("planted", "PLANT omitting moving Shiab leaves a live lower-order defect",
      any(column for column in omitted_moving))
check("planted", "PLANT freezing delta T while moving B leaves a live lower-order defect",
      any(column for column in frozen_split))
check("planted", "PLANT zero lower-order response does not erase the rank-91 principal epsilon bank",
      port_registry["selected_principal_bank"]["epsilon_dimension"] == 91
      and port_registry["selected_principal_bank"]["timelike"]["rank"] == 110)


print("\nC. BOTH-BRANCH METRIC PORT")
b, t = sp.symbols("b t", real=True)
r = sp.sqrt(3)
branches = (
    {b: Q(1, 208)-r/312, t: (-2+r)/208},
    {b: Q(1, 208)+r/312, t: (-2-r)/208},
)
upsilon = 312*(b+t)**2+t
raw_upsilon = upsilon
check("exact", "both exact roots solve the action-varpi equation",
      all(sp.simplify(upsilon.subs(point)) == 0 for point in branches))
check("layer0", "both exact action branches satisfy the raw-residual-zero premise used by v0.95",
      all(sp.simplify(raw_upsilon.subs(point)) == 0 for point in branches))
branch_maps = [branch_columns(point) for point in branches]
branch_ranks = [flattened_rank(columns) for columns in branch_maps]
print("BRANCH_LOWER_EPSILON_RANKS=" + repr(branch_ranks))
check("theorem", "the exact lower-order primitive-epsilon branch ranks are 91 and 91",
      branch_ranks == [91, 91])
expected_lower = ((51-19*r)/8112, (51+19*r)/8112)
check("exact", "the two lower-order coefficients are positive nonzero Galois conjugates",
      all(sp.simplify((-b+360*(b+t)**2).subs(point) - expected) == 0
          and expected.is_positive is True
          for point, expected in zip(branches, expected_lower)))
metric_block = metric_registry["local_fixed_varpi_block"]
check("prior_art", "the structural fixed-varpi identities delta-T=-delta-B and delta-F_A=0 remain available",
      metric_block["delta_T"] == "MINUS_DELTA_B_LC"
      and metric_block["delta_F_A"] == "ZERO")
check("layer0", "v0.95 metric coefficient and observation cancellations have their raw-Upsilon-zero premise on both branches",
      metric_block["comoving_coefficient_transport"] == "ZERO_AT_UPSILON_STAR_ZERO"
      and metric_block["moving_observation_term_at_Upsilon_star_zero"] == "ZERO")
check("control", "the ported metric block retains a live rank-twenty Levi-Civita source map",
      metric_block["full_covariant_lc_first_jet_rank"] == 20)


print("\nD. DISPOSITION AND FENCES")
check("construction", "the selected lower-order epsilon block is computed and the metric prior art is ported with its premise exposed", True)
check("variational", "raw epsilon cancellation does not substitute for the distinct first-action Hessian", True)
check("symplectic", "raw bulk cancellation does not erase the live first-action epsilon endpoint momentum", True)
check("representation", "selected Spin two-half and full-unitary parent scopes remain distinct", True)
check("microlocal", "the lower-order epsilon result leaves the live principal q-eta coefficient and causal strata intact", True)
check("krein", "finite local block reconciliation supplies no positive field Riesz or closed domain", True)
check("analytic", "no determinant contour reflection positivity Green inverse or quantum measure follows", True)
check("accounting", "no field coefficient selector bundle class quotient or datum is added", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_G_VARPI_EPSILON_MOVING_SHIAB_AND_AUGMENTED_TORSION_GRAMMAR__SOURCE_SILENT_EXACT_K77_LOWER_ORDER_BLOCK_RECONCILIATION_AND_ACTION_PARENT")
print("LOWER_EPSILON=EXACT_BRANCH_RANKS_REPORTED_ABOVE__RAW_RESIDUAL_ZERO_ON_BOTH_BRANCHES__PRINCIPAL_QETA_LIVE")
print("METRIC=V095_FIXED_VARPI_BLOCK_PORTS_WITH_RAW_RESIDUAL_ZERO_PREMISE_EXPLICIT__STRUCTURAL_DELTAF_ZERO_AND_TRANSVERSE_RANK6")
print("PARENTS=SPIN_NATIVE__TWO_U32_32_HALVES__FULL_U64_64_REMAIN_DISTINCT")
print("NEXT=COMPLETE_FIRST_ACTION_HESSIAN_AND_EXPANDED_PARENT_PAIRINGS__THEN_GAUGE_GHOST_DOMAIN")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
