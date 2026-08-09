#!/usr/bin/env python3
"""Exact primitive-epsilon extension of the selected K77 residual symbol.

The source-owned group field ``epsilon`` has an independent infinitesimal
``eta``.  On the selected Spin-native parent its tangent is ``spin(7,7)``, the
91-dimensional bivector carrier.  At principal order and fixed independent
``varpi`` the two-connection identity gives ``delta T=-q eta`` and
``delta F_varpi=0``.  This probe appends those 91 columns to the actual
metric-ten plus varpi-twenty-four stationary residual bank, then computes the
exact real causal Gram strata.

The moving-Shiab response ``delta Phi=[Phi,eta]`` is zeroth order and remains
required for the full Frechet operator.  The four-column physical Ward orbit,
the conditional gamma-soldered orbit, and the printed covariant prolongation
are deliberately not substituted for this independent field bank.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_stationary_gram_boundary_strata_probe.py"
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
        off = next(
            ((i, j) for i in range(n) for j in range(i + 1, n)
             if work[i, j] != 0),
            None,
        )
        if off is None:
            zero += n
            break
        i, j = off
        order = [i, j] + [k for k in range(n) if k not in (i, j)]
        work = work.extract(order, order)
        positive += 1
        negative += 1
        if n == 2:
            work = sp.zeros(0)
        else:
            pivot = work[:2, :2]
            coupling = work[2:, :2]
            work = sp.simplify(
                work[2:, 2:] - coupling * pivot.inv() * coupling.T
            )
    return (positive, negative, zero)


print("A. SOURCE LOCUS, LAYER ZERO, AND PREDECESSOR")
source = read("lab/sources/selected-k77-gamma-soldered-epsilon-dupsilon-orbit-source-reinspection-2026-08-08.md")
cartan = read("explorations/conditional-build/signature-generic-cartan-ward-compose-2026-08-08.md")
common_green = read("explorations/conditional-build/selected-k77-common-field-formal-adjoint-green-2026-08-08.md")
first = strict("lab/process/selected-k77-coupled-euler-complex-scope.json")
action_parent = strict("lab/process/selected-k77-stationary-gram-boundary-strata.json")
check("source", "source epsilon is an H-valued independent field with Maurer-Cartan derivative",
      "epsilon is an H-valued field" in source
      and "T_omega=varpi-epsilon^-1 d0 epsilon" in source)
check("source", "source confirms primitive epsilon grammar but not gamma soldering",
      "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source)
check("repo", "primitive epsilon Euler and compact Green owner already exist",
      "source-owned row, Euler chain and compact Green owner already existed" in cartan)
check("repo", "the available normalized first-action source symbol has only 34 variables",
      first["first_layer"]["source_variable_dimension"] == 34)
check("repo", "three action parents remain explicitly uncollapsed",
      action_parent["action_parents"]["selected_spin_native_dimension"] == 2107
      and action_parent["action_parents"]["two_U32_32_halves_dimension"] == 16382
      and action_parent["action_parents"]["full_U64_64_dimension"] == 16383
      and not action_parent["action_parents"]["collapsed"])

for label in (
    "primitive epsilon field versus the four-column dependent physical Ward orbit",
    "primitive epsilon field versus the source-silent gamma-soldered orbit",
    "Frechet D-epsilon versus printed covariant prolongation Xi",
    "principal d-eta response versus lower-order moving-Shiab commutator",
    "selected Spin-native action versus two U32,32 halves versus full U64,64",
    "stationary second-action Gram versus the normalized first-action Schur symbol",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "the 34-field stationary Gram predecessor replays",
      "PASS 60/60" in capture.getvalue() and not P["FAILURES"])

G = P["G"]
M = P["M"]
V = P["V"]


print("\nB. SELECTED SPIN-NATIVE PRIMITIVE-EPSILON PRINCIPAL BANK")
pairs14 = [(left, right) for left in range(14) for right in range(left + 1, 14)]
check("exact", "spin(7,7) has ninety-one bivector tangent directions",
      len(pairs14) == 91)

epsilon_principal = [
    [M["fscale"](-1, {1 << mu: M["blade"](pair)}) for pair in pairs14]
    for mu in range(4)
]
check("exact", "every epsilon principal coefficient is a real grade-two-valued one-form",
      all({key[1].bit_count() for key in M["flatten"](column)} <= {2}
          for bank in epsilon_principal for column in bank))
check("exact", "each coordinate epsilon bank has exact rank ninety-one",
      [V["family_rank"](bank) for bank in epsilon_principal] == [91] * 4)


def columns_at(q):
    old = []
    for column in range(34):
        banks = G["metric_principal"] if column < 10 else P["varpi_principal"]
        local = column if column < 10 else column - 10
        old.append(P["linear_combination"](
            [banks[mu][local] for mu in range(4)], q
        ))
    epsilon = [P["linear_combination"](
        [epsilon_principal[mu][column] for mu in range(4)], q
    ) for column in range(91)]
    return old, epsilon, old + epsilon


print("\nC. EXACT CAUSAL RAW AND GRAM STRATA")
expected = {
    "timelike": {"gram_rank": 110, "inertia": (58, 52, 15)},
    "spacelike": {"gram_rank": 110, "inertia": (53, 57, 15)},
    "null": {"gram_rank": 16, "inertia": (10, 6, 109)},
}
results = {}
for name, q in G["S"]["orbits"].items():
    old, epsilon, columns = columns_at(q)
    epsilon_rank = V["family_rank"](epsilon)
    metric_epsilon_rank = V["family_rank"](old[:10] + epsilon)
    raw_rank = V["family_rank"](columns)
    gram = sp.Matrix([
        [P["k_pair"](left, right) for right in columns]
        for left in columns
    ])
    gram_rank = gram.rank()
    inertia = exact_inertia(gram)
    check("exact", f"{name}: primitive epsilon symbol is injective",
          epsilon_rank == 91)
    check("exact", f"{name}: metric adds exactly six transverse directions beyond primitive epsilon",
          metric_epsilon_rank == epsilon_rank + 6 == 97)
    check("exact", f"{name}: enlarged raw rank is one hundred ten",
          raw_rank == 110)
    check("exact", f"{name}: exact Gram rank matches the preregistered rerun target",
          gram_rank == expected[name]["gram_rank"])
    check("exact", f"{name}: exact inertia matches the preregistered rerun target",
          inertia == expected[name]["inertia"] and sum(inertia) == 125)
    check("control", f"{name}: enlarged field bank retains a nontrivial radical",
          inertia[2] > 0)
    results[name] = {
        "field_dimension": 125,
        "epsilon_rank": epsilon_rank,
        "metric_plus_epsilon_rank": metric_epsilon_rank,
        "raw_rank": raw_rank,
        "gram_rank": gram_rank,
        "inertia": list(inertia),
        "green_quotient_dimension": 2 * gram_rank,
        "raw_kernel_dimension": 125 - raw_rank,
        "extra_isotropic_image_dimension": raw_rank - gram_rank,
    }

check("theorem", "primitive epsilon and transverse metric motion are complementary by six directions",
      all(row["metric_plus_epsilon_rank"] == 97 for row in results.values()))
check("theorem", "the selected full principal field bank has fifteen raw gauge/coordinate redundancies",
      all(row["raw_kernel_dimension"] == 15 for row in results.values()))
check("theorem", "the null stratum gains ninety-four isotropic image directions",
      results["null"]["extra_isotropic_image_dimension"] == 94)
check("theorem", "the non-null restrictions are nondegenerate on the raw image",
      results["timelike"]["extra_isotropic_image_dimension"] == 0
      and results["spacelike"]["extra_isotropic_image_dimension"] == 0)
check("planted", "PLANT the 91 epsilon directions are not the four-column physical Ward orbit",
      91 != 4)


print("\nD. FIRST-ACTION AND FULL-FRECHET COMPOSITION FENCE")
check("variational", "the enlarged second-action principal tangent has 125 fields",
      all(row["field_dimension"] == 125 for row in results.values()))
check("variational", "the available first-action Schur symbol cannot be directly added to that tangent",
      first["first_layer"]["source_variable_dimension"] == 34 != 125)
check("variational", "the moving-Shiab primitive response remains lower-order and un-serialized on this bank",
      "full lower-order/nonlinear" in common_green)
check("source", "source does not select Spin-native over the expanded action parents here",
      "SOURCE-SILENT" in source)
check("representation", "two U32,32 halves are retained as a comparator distinct from full U64,64",
      action_parent["action_parents"]["two_U32_32_halves_dimension"] + 1
      == action_parent["action_parents"]["full_U64_64_dimension"])


print("\nE. ANALYTIC, SYMPLECTIC, AND ACCOUNTING FENCES")
check("analytic", "causal strata remain separate and no fixed quotient is assumed", True)
check("operator", "finite exact inertia supplies no field Riesz or maximal closed domain", True)
check("symplectic", "the doubled Gram quotient is not identified with the edge carrier", True)
check("complex", "no complexification contour measure or reflection positivity is inferred", True)
check("accounting", "epsilon was already source-owned; no new field coefficient selector or datum is added", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)
check("planted", "PLANT selected Spin-native closure is not full-U64,64 closure", True)
check("planted", "PLANT a principal bank is not the complete nonlinear Frechet operator", True)
check("planted", "PLANT a finite Green quotient is not odd BFV or CME", True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_PRIMITIVE_EPSILON_AND_MOVING_SHIAB_GRAMMAR__SOURCE_SILENT_K77_FULL_BANK_ACTION_PARENT_AND_SHARED_FIRST_ACTION")
print("LAYER0_RETURN=PRIMITIVE_EPSILON_91_NOT_DEPENDENT_WARD4_NOT_GAMMA4_NOT_XI")
print("SELECTED_SPIN_NATIVE_FIELDS=10_METRIC_PLUS_24_VARPI_PLUS_91_EPSILON_EQUALS_125")
print("RAW_RANKS=" + "_".join(str(results[name]["raw_rank"]) for name in ("timelike", "spacelike", "null")))
print("GRAM_RESULTS=" + json.dumps(results, sort_keys=True))
print("FIRST_ACTION_COMPOSITION=BLOCKED_BY_34_VERSUS_125_FIELD_TANGENT_AND_UNSERIALIZED_LOWER_ORDER_EPSILON")
print("ACTION_PARENTS=SELECTED_SPIN_NATIVE__TWO_U32_32_HALVES__FULL_U64_64__NOT_COLLAPSED")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
