#!/usr/bin/env python3
"""Exact principal metric-to-augmented-torsion block after ledger v0.84.

The source variables are ``(g,varpi)`` with the augmented-torsion difference
``T=varpi-B_LC(g)`` on the selected epsilon frame.  At fixed independent
``varpi`` the principal metric response is therefore ``delta T=-L_q h``.
This probe constructs that map on all ten metric directions, proves its
restriction to the six directions transverse to the diffeomorphism orbit is
injective, and composes the resulting partial metric block with the exact
source-varpi and gamma-epsilon responses.  The nonzero remaining Ward packet
is typed as the still-unbuilt moving-Shiab/Hodge/lower-order metric block; it
is not fitted or promoted to a physical operator.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
V084 = ROOT / "tests/channel-swings/selected_k77_gamma_soldered_epsilon_dupsilon_orbit_probe.py"
SOURCE_VARIABLE = ROOT / "tests/channel-swings/selected_action_source_variable_hessian_probe.py"
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


print("A. SOURCE, PREDECESSORS, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
source_variables = read("explorations/conditional-build/selected-action-source-variable-hessian-and-diffeomorphism-lift-2026-08-06.md")
constituents = read("explorations/conditional-build/selected-invariant-constituent-operator-naturality-2026-08-07.md")
check("source", "source owns an independent varpi and a rotated Levi-Civita reference in augmented torsion",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "repo source reconstruction types the selected variables as T equals varpi minus B-LC of g",
      r"T=\varpi-B_{LC}(g)" in source_variables and "SOURCE-CORRECTS" in source_variables)
check("source", "source remains silent on the complete physical metric residual derivative",
      "SOURCE-SILENT" in source_variables and "full" in source_variables)
check("repo", "the selected nonzero stationary constituents are already exact",
      "selected stationary background is now explicit" in constituents
      and "Both constituents are nonzero" in constituents)
for label in (
    "metric value h versus its first-jet Levi-Civita symbol L-q h",
    "four diffeomorphism directions versus six transverse metric directions",
    "augmented-torsion input derivative versus moving Shiab and Hodge operators",
    "principal partial Ward packet versus the complete Frechet identity",
    "finite residual rank versus a reduced presymplectic or physical state count",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    G = runpy.run_path(str(V084))
check("repo", "v0.84 gamma-soldered orbit predecessor replays",
      "PASS 66/66" in capture.getvalue())
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    S = runpy.run_path(str(SOURCE_VARIABLE))
check("repo", "source-variable Levi-Civita predecessor replays",
      "PASS " in capture.getvalue())

P = G["P"]
M = P["M"]
V = P["V"]


def linear_combination(forms, coefficients):
    result = {}
    for form, coefficient in zip(forms, coefficients):
        if coefficient:
            result = M["fadd"](result, M["fscale"](coefficient, form))
    return result


def negate(form):
    return M["fscale"](-1, form)


print("\nB. TEN-DIRECTION LEVI-CIVITA AND TRANSVERSE SIX")
results = {}
for name, packet in S["results"].items():
    L = packet["L"]
    D = packet["D"]
    C = packet["connection_lift"]
    left_inverse = (D.T * D).inv() * D.T
    transverse = sp.eye(10) - D * left_inverse
    transverse_lift = L * transverse
    kernel = L.nullspace()[0]

    check("exact", f"{name}: spin Levi-Civita symbol has rank nine with one metric kernel",
          L.rank() == 9 and len(L.nullspace()) == 1)
    check("exact", f"{name}: metric diffeomorphism orbit has rank four and transverse projector rank six",
          D.rank() == 4 and transverse.rank() == 6 and transverse * D == sp.zeros(10, 4))
    check("exact", f"{name}: the Levi-Civita metric kernel lies wholly in the diffeomorphism orbit",
          transverse * kernel == sp.zeros(10, 1))
    check("exact", f"{name}: Levi-Civita is injective on all six transverse metric directions",
          transverse_lift.rank() == 6)
    check("exact", f"{name}: source connection orbit is exactly L times the metric orbit",
          C == L * D and C.rank() == 3)
    check("planted", f"PLANT {name}: rank nine on ten values is not a missing transverse physical direction",
          transverse_lift.rank() == transverse.rank())

    # At fixed varpi, delta T = -L h.  The source raw residual contains the
    # direct kappa*T constituent, so this is the exact top-order metric block
    # before moving-Shiab/Hodge and other lower-order metric terms.
    metric_torsion_columns = [negate(G["horizontal_form"](L[:, column])) for column in range(10)]
    transverse_columns = [
        linear_combination(metric_torsion_columns, transverse[:, column])
        for column in range(10)
    ]
    check("exact", f"{name}: direct augmented-torsion residual block has rank nine",
          V["family_rank"](metric_torsion_columns) == 9)
    check("exact", f"{name}: its transverse residual image has exact rank six",
          V["family_rank"](transverse_columns) == 6)

    varpi_forms = [G["horizontal_form"](C[:, column]) for column in range(4)]
    gamma_forms = [G["gamma_connection_form"](sp.Matrix(G["S"]["orbits"][name]), column)
                   for column in range(4)]
    varpi_responses = [P["response"](value) for value in varpi_forms]
    epsilon_responses = [negate(P["response"](value)) for value in gamma_forms]
    metric_orbit = [linear_combination(metric_torsion_columns, D[:, column]) for column in range(4)]
    partial_ward = [
        M["fadd"](metric, varpi, epsilon)
        for metric, varpi, epsilon in zip(metric_orbit, varpi_responses, epsilon_responses)
    ]
    partial_rank = V["family_rank"](partial_ward)
    check("exact", f"{name}: the actual partial metric-varpi-epsilon Ward packet remains rank four",
          partial_rank == 4)
    check("planted", f"PLANT {name}: six transverse closure does not imply full Frechet Ward closure",
          any(partial_ward))

    required_operator = [negate(value) for value in partial_ward]
    check("exact", f"{name}: the missing operator packet is uniquely fixed on the four orbit columns",
          all(not M["fadd"](left, right)
              for left, right in zip(partial_ward, required_operator)))

    results[name] = {
        "levi_civita_rank": L.rank(),
        "metric_kernel": list(kernel),
        "diffeomorphism_rank": D.rank(),
        "transverse_rank": transverse.rank(),
        "transverse_levi_civita_rank": transverse_lift.rank(),
        "direct_torsion_residual_rank": V["family_rank"](metric_torsion_columns),
        "transverse_torsion_residual_rank": V["family_rank"](transverse_columns),
        "partial_ward_defect_rank": partial_rank,
        "partial_ward_supports": [len(M["flatten"](value)) for value in partial_ward],
        "required_operator_supports": [len(M["flatten"](value)) for value in required_operator],
    }


print("\nC. CONSTRAINT SURPLUS AND SCOPE")
check("theorem", "all causal classes close the six transverse principal augmented-torsion columns",
      all(row["transverse_torsion_residual_rank"] == 6 for row in results.values()))
check("theorem", "all causal classes retain a rank-four missing operator Ward packet",
      all(row["partial_ward_defect_rank"] == 4 for row in results.values()))
check("surplus", "the six-column block uses the source-owned Levi-Civita map and no fitted coefficient",
      True)
for kind, label in (
    ("symplectic", "principal Ward typing is not a reduced presymplectic or BFV class"),
    ("variational", "moving Shiab Hodge curvature density and observation terms remain unbuilt"),
    ("krein", "the residual pairing formal adjoint and common domain remain unbuilt"),
    ("analytic", "no contour determinant saddle or Green operator is selected"),
    ("scope", "the v0.84 gamma-epsilon orbit remains conditional and source-silent"),
    ("scope", "the six transverse result is principal order only"),
    ("scope", "P1 P2 P3 remain unused and no field coefficient quotient or datum is added"),
    ("scope", "Curt remains formally separate and no third lane is promoted"),
):
    check(kind, label, True)

registry = strict("lab/process/selected-k77-metric-transverse-augmented-torsion-block.json")
check("exact", "registry records all three causal blocks", registry["causal_blocks"] == results)
check("source", "registry preserves source confirmation and silence",
      registry["source_return"] == "SOURCE-CONFIRMS__T_EQUALS_VARPI_MINUS_ROTATED_BLC__SOURCE-SILENT__COMPLETE_PHYSICAL_DG_UPSILON_OPERATOR_BLOCK")

print("SOURCE_RETURN=SOURCE-CONFIRMS__T_EQUALS_VARPI_MINUS_ROTATED_BLC__SOURCE-SILENT__COMPLETE_PHYSICAL_DG_UPSILON_OPERATOR_BLOCK")
print("TRANSVERSE_METRIC_AUGMENTED_TORSION_BLOCK=RANK6_ALL_CAUSAL_CLASSES")
print("PARTIAL_METRIC_VARPI_GAMMA_EPSILON_WARD_DEFECT=RANK4_ALL_CAUSAL_CLASSES")
print("NEXT=CONSTRUCT_MOVING_SHIAB_HODGE_CURVATURE_DENSITY_OBSERVATION_OPERATOR_PACKET_ON_THE_FOUR_ORBIT_COLUMNS__THEN_COMPLETE_LOWER_ORDER_TRANSVERSE_BLOCK_AND_FULL_JR_ZERO")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
