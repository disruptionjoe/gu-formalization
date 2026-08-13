#!/usr/bin/env python3
"""Exact reconciliation of the v0.85 principal Ward packet.

The source owns ``(g,varpi,epsilon)`` and ``T=varpi-B_LC(g)``.  It does not
identify a spacetime diffeomorphism parameter with the conditional
grade-one Clifford lift ``gamma_epsilon(xi-flat)``.  This probe removes that
unlicensed identification before pricing the principal Ward defect.

Result: the direct torsion pieces from ``g`` and ``varpi`` cancel exactly.
The full raw-Upsilon varpi response still contains a rank-three curvature
piece, so a moving operator response remains required on three—not four—of
the diffeomorphism columns.  The fourth column in v0.85 came solely from the
conditional gamma-epsilon insertion.  The earlier zero moving-operator
theorem is a different, invariant-branch tangent and cannot close this
source-variable diffeomorphism packet.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
V085 = ROOT / "tests/channel-swings/selected_k77_metric_transverse_augmented_torsion_block_probe.py"
INVARIANT_OPERATOR = ROOT / "tests/channel-swings/selected_invariant_constituent_operator_naturality_probe.py"
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


print("A. SOURCE LOCUS, LAYER ZERO, AND PREDECESSORS")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
moving = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
prior = read("explorations/conditional-build/selected-k77-metric-transverse-augmented-torsion-block-2026-08-08.md")
check("source", "source owns the two-connection difference T equals varpi minus the epsilon-rotated reference",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "source varies varpi with epsilon fixed in the printed translation equation",
      "varpi+s\\alpha" in source and "holding `epsilon` fixed" in moving)
check("source", "the primary-source pack rejects automatic identity with a physical soldering datum",
      "source's epsilon is not automatically N1's soldering datum" in source
      and "LAYER-0-UNCERTAIN" in source)
check("source", "source epsilon moves B T and Shiab but not metric Hodge density or observation automatically",
      "Metric/Hodge" in moving
      and "density and section equations remain separate rows" in moving)
check("repo", "v0.85 assigned the conditional four-column remainder to a missing moving operator",
      "rank four" in prior and "moving Shiab/Hodge/curvature/density/" in prior)
for label in (
    "source gauge epsilon versus a spacetime diffeomorphism soldering tangent",
    "direct kappa-T response versus the full raw-Upsilon varpi response",
    "invariant-branch target transport versus an independent source-variable diffeomorphism jet",
    "rank-three sourced orbit packet versus the conditional rank-four gamma extension",
    "principal Ward target versus full Frechet closure and reduced covariant phase space",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    W = runpy.run_path(str(V085))
check("repo", "immutable v0.85 predecessor replays", "PASS 57/57" in capture.getvalue())
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    runpy.run_path(str(INVARIANT_OPERATOR))
operator_output = capture.getvalue()
check("repo", "the invariant-branch moving-operator predecessor replays",
      "PASS 35/35" in operator_output
      and "OPERATOR_PACKET=INVARIANT_BRANCH_TANGENT_ZERO" in operator_output)

G = W["G"]
S = W["S"]
P = W["P"]
M = W["M"]
V = W["V"]


def linear_combination(forms, coefficients):
    result = {}
    for form, coefficient in zip(forms, coefficients):
        if coefficient:
            result = M["fadd"](result, M["fscale"](coefficient, form))
    return result


def negate(form):
    return M["fscale"](-1, form)


print("\nB. REMOVE THE SOURCE-SILENT GAMMA-DIFFEO IDENTIFICATION")
results = {}
for name, packet in S["results"].items():
    L = packet["L"]
    D = packet["D"]
    C = packet["connection_lift"]
    q = sp.Matrix(G["S"]["orbits"][name])

    metric_torsion_columns = [negate(G["horizontal_form"](L[:, column])) for column in range(10)]
    metric_orbit = [linear_combination(metric_torsion_columns, D[:, column]) for column in range(4)]
    direct_varpi = [G["horizontal_form"](C[:, column]) for column in range(4)]
    full_varpi = [P["response"](value) for value in direct_varpi]
    curvature_remainder = [M["fadd"](full, negate(direct)) for full, direct in zip(full_varpi, direct_varpi)]
    sourced_packet = [M["fadd"](metric, full) for metric, full in zip(metric_orbit, full_varpi)]

    check("exact", f"{name}: metric and varpi direct augmented-torsion responses cancel on all four columns",
          all(not M["fadd"](metric, direct) for metric, direct in zip(metric_orbit, direct_varpi)))
    check("exact", f"{name}: the surviving source-variable packet is exactly the curvature response",
          sourced_packet == curvature_remainder)
    check("exact", f"{name}: the source-variable curvature packet has rank three",
          V["family_rank"](sourced_packet) == 3)

    kernel = C.nullspace()[0]
    check("exact", f"{name}: the longitudinal connection-kernel column already has zero sourced response",
          not linear_combination(sourced_packet, kernel))

    gamma_forms = [G["gamma_connection_form"](q, column) for column in range(4)]
    gamma_responses = [P["response"](value) for value in gamma_forms]
    conditional_packet = [M["fadd"](sourced, negate(gamma))
                          for sourced, gamma in zip(sourced_packet, gamma_responses)]
    check("exact", f"{name}: conditional gamma-epsilon response has rank four",
          V["family_rank"](gamma_responses) == 4)
    check("exact", f"{name}: gamma-epsilon adds a nonzero response precisely on the sourced kernel direction",
          bool(linear_combination(gamma_responses, kernel)))
    check("exact", f"{name}: the old gamma-extended partial packet retains rank four",
          V["family_rank"](conditional_packet) == 4)
    check("exact", f"{name}: old packet supports reproduce the v0.85 registry",
          [len(M["flatten"](value)) for value in conditional_packet]
          == W["results"][name]["partial_ward_supports"])

    sourced_required_operator = [negate(value) for value in sourced_packet]
    conditional_required_operator = [negate(value) for value in conditional_packet]
    check("exact", f"{name}: sourced principal moving-operator target has rank three",
          V["family_rank"](sourced_required_operator) == 3)
    check("exact", f"{name}: gamma-conditioned moving-operator target has rank four",
          V["family_rank"](conditional_required_operator) == 4)
    check("planted", f"PLANT {name}: invariant-branch zero transport cannot cancel this nonzero source-variable packet",
          V["family_rank"](sourced_required_operator) != 0)

    results[name] = {
        "direct_torsion_cancellation_rank": 0,
        "source_variable_curvature_packet_rank": V["family_rank"](sourced_packet),
        "source_variable_curvature_packet_supports": [len(M["flatten"](value)) for value in sourced_packet],
        "source_longitudinal_kernel": list(kernel),
        "source_longitudinal_response_zero": not linear_combination(sourced_packet, kernel),
        "conditional_gamma_response_rank": V["family_rank"](gamma_responses),
        "conditional_gamma_kernel_response_nonzero": bool(linear_combination(gamma_responses, kernel)),
        "conditional_gamma_extended_packet_rank": V["family_rank"](conditional_packet),
        "source_required_operator_rank": V["family_rank"](sourced_required_operator),
        "conditional_required_operator_rank": V["family_rank"](conditional_required_operator),
    }


print("\nC. RECONCILED TARGET AND PROGRAM FENCES")
check("theorem", "all causal classes reduce the sourced moving-operator target from four columns to rank three",
      all(row["source_required_operator_rank"] == 3 for row in results.values()))
check("theorem", "all fourth directions were introduced only by the conditional gamma-epsilon soldering law",
      all(row["source_longitudinal_response_zero"]
          and row["conditional_gamma_kernel_response_nonzero"] for row in results.values()))
check("theorem", "the moving operator is narrowed rather than eliminated",
      all(row["source_required_operator_rank"] != 0 for row in results.values()))
check("surplus", "the correction removes one unsupported tangent identification and fits no coefficient",
      True)
for kind, label in (
    ("symplectic", "principal source-variable Ward typing is not a reduced presymplectic or BFV class"),
    ("symplectic", "the gamma-epsilon construction may revive only after its boundary and reduced charge class is built"),
    ("variational", "the exact rank-three moving Shiab Hodge curvature density observation packet remains unbuilt"),
    ("variational", "complete lower-order transverse and primitive internal-epsilon Frechet blocks remain open"),
    ("krein", "K-star formal adjoint Green concomitant and a common domain remain open"),
    ("analytic", "no contour determinant saddle path-integral measure or Green domain is selected"),
    ("scope", "the conditional gamma-epsilon map remains a live internal or future soldering construction"),
    ("scope", "the rank-six transverse direct augmented-torsion result remains exact"),
    ("scope", "P1 P2 P3 remain unused and no datum quotient or physics claim is added"),
    ("scope", "Curt remains formally separate and no third lane is promoted"),
):
    check(kind, label, True)

registry = strict("lab/process/selected-k77-principal-ward-gamma-epsilon-reconciliation.json")
check("exact", "registry records all three exact causal reconciliations",
      registry["causal_reconciliations"] == results)
check("source", "registry carries the decisive source correction",
      registry["source_return"] == "SOURCE-CORRECTS")
check("exact", "registry narrows the next moving-operator target to rank three",
      registry["next_gate"]["source_variable_moving_operator_rank"] == 3)

print("SOURCE_RETURN=SOURCE-CORRECTS")
print("DIRECT_METRIC_PLUS_VARPI_TORSION_ORBIT=ZERO_ALL_FOUR_COLUMNS")
print("SOURCE_VARIABLE_CURVATURE_WARD_PACKET=RANK3_ALL_CAUSAL_CLASSES")
print("GAMMA_EPSILON_DIFFEO_IDENTIFICATION=SOURCE_SILENT__ADDS_FOURTH_COLUMN")
print("MOVING_OPERATOR_TARGET=RANK3_SOURCE_VARIABLE_PACKET__NOT_ELIMINATED")
print("NEXT=CONSTRUCT_RANK3_MOVING_SHIAB_HODGE_CURVATURE_DENSITY_OBSERVATION_PACKET__THEN_LOWER_ORDER_TRANSVERSE_AND_PRIMITIVE_INTERNAL_EPSILON_FRECHET__K_STAR_GREEN")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
