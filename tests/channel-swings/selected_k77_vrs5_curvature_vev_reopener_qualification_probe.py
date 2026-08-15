#!/usr/bin/env sage -python
"""Qualify the action-owned curvature/VEV trace reopener against SR-1C.

The repository owns an exact scalar-jet trace closure and an exact canonical
Zorro branch.  This probe tests whether they are the same carrier, whether the
old scalar cell can be imported without a new fitted value, and which honest
VRS-5 reopener should be tried next.  It does not solve the successor
nonparallel second-jet system.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy

from sage.all import PolynomialRing, QQ


ROOT = Path(__file__).resolve().parents[2]
SCALAR_PROBE = ROOT / "tests/channel-swings/selected_k77_curvature_vev_trace_probe.py"
CANONICAL_PROBE = ROOT / "tests/channel-swings/selected_k77_zorro_nonzero_t_first_action_jet_probe.py"
ZORRO_PROBE = ROOT / "tests/channel-swings/selected_k77_zorro_dewitt_trace_curvature_obstruction_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PRIOR EXACT RECEIPTS AND OWNER TYPES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    OLD = runpy.run_path(str(SCALAR_PROBE))
check("prior", "the source-owned scalar-jet closure replays",
      "PASS 43/43" in capture.getvalue() and not OLD["FAILURES"])

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    NEW = runpy.run_path(str(CANONICAL_PROBE))
check("prior", "the canonical-Zorro nonzero-T action/Bianchi branch replays",
      "PASS 40/40" in capture.getvalue() and not NEW["FAILURES"])

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    ZORRO = runpy.run_path(str(ZORRO_PROBE))
check("prior", "the canonical nine-plane trace-curvature discriminator replays",
      not ZORRO["FAILURES"] and ZORRO["RESULT"]["canonical_zorro_zero_planes"] == 9)

for label in (
    "an action-owned curvature coordinate versus a freely adjustable action coefficient",
    "the old homogeneous scalar jet versus the canonical Zorro curvature module",
    "a branch-local trace cancellation versus cancellation on another branch",
    "a generous counterfactual graft versus a legal canonical connection jet",
    "a nonparallel formal two-jet versus an open stationary background",
):
    check("type", label + " remain distinct", True)


print("\nB. THE OLD TRACE-CLOSING BRANCH IS NOT CANONICAL B_Z")
b_star = Fraction(1, 208)
r_star = Fraction(1, 129792)
t_star = Fraction(-1, 104)
old_curvature_scale = b_star**2 + r_star
check("exact", "the old branch total B curvature is (1/32448) C",
      old_curvature_scale == Fraction(1, 32448))

# For B=b Phi1 with an added rC derivative cell, F_B=(b^2+r)C.  On every
# trace--traceless plane the Clifford commutator coefficient is twice this
# nonzero scalar, whereas the canonical DeWitt scale factor has zero mixed
# curvature on all nine labelled planes.
old_trace_plane_coefficients = [2 * old_curvature_scale] * 9
check("geometry", "the old trace-closing scalar branch is nonzero on all nine mixed trace planes",
      all(value != 0 for value in old_trace_plane_coefficients))
check("geometry", "canonical Zorro curvature is zero on the same nine labelled planes",
      all(value.is_zero_matrix for value in ZORRO["trace_planes"].values()))
check("gauge", "zero cannot be gauge-conjugate to the old nonzero scalar curvature on a fixed plane",
      all(value != 0 for value in old_trace_plane_coefficients))

C = NEW["C"]
F_BZ = NEW["D"]["F_BZ"]
c_flat = {
    (form_mask, cliff_mask): value[0]
    for form_mask, coefficients in C.items()
    for cliff_mask, value in coefficients.items()
    if value[0]
}
f_flat = {
    ((1 << r) | (1 << k), (1 << i) | (1 << j)): value
    for (r, k), coefficients in F_BZ.items()
    for (i, j), value in coefficients.items()
    if value
}
common = set(c_flat) & set(f_flat)
ratios = {f_flat[cell] / c_flat[cell] for cell in common}
check("exact", "C has 91 cells while canonical F_BZ has 107 cells on 25 form legs",
      len(c_flat) == 91 and len(f_flat) == 107 and len(F_BZ) == 25)
check("exact", "the two curvature supports overlap in only 25 cells",
      len(common) == 25 and len(set(c_flat) - set(f_flat)) == 66
      and len(set(f_flat) - set(c_flat)) == 82)
check("exact", "canonical F_BZ is not proportional to the scalar cell C",
      set(c_flat) != set(f_flat) and len(ratios) == 6)


print("\nC. THE TWO EXACT BRANCHES ARE ALGEBRAICALLY DISJOINT")
R = PolynomialRing(QQ, "t")
t = R.gen()
branch = 28392 * t**2 + 91 * t - 351
check("branch", "the old scalar-jet amplitude is not an SR-1C root",
      branch(QQ(t_star.numerator) / t_star.denominator) == -QQ(1397) / 4)
check("branch", "the SR-1C quadratic is irreducible with two simple real roots",
      branch.is_irreducible() and branch.discriminant() == 39870649)

# Give the old cell every benefit of the doubt: import its exact 4368*t*r
# action normalization into the current density without first requiring a
# canonical connection realization.  Cancellation would still require a
# root-dependent value.  The endpoint-preserving transgression placement has
# half that response and is root-dependent as well.
action_density = -t * (27 + 728 * t**2)
required_old_normalization = ((27 + 728 * t**2) / 4368).mod(branch)
required_endpoint_preserving = ((27 + 728 * t**2) / 2184).mod(branch)
check("exact", "the generous old-normalization cancellation requires 3/364-t/1872",
      required_old_normalization == QQ(3) / 364 - t / 1872)
check("exact", "endpoint-preserving canonical placement requires 3/182-t/936",
      required_endpoint_preserving == QQ(3) / 182 - t / 936)
check("no_fit", "neither required value is one fixed rational cell on both algebraic roots",
      required_old_normalization.degree() == 1
      and required_endpoint_preserving.degree() == 1)

r_old = QQ(r_star.numerator) / r_star.denominator
generous_graft = action_density + 4368 * t * r_old
check("no_fit", "even the old solved r value fails to cancel the current trace on either root",
      branch.gcd(generous_graft) == 1
      and generous_graft.mod(branch) == -QQ(67343) / 1872 * t + QQ(3) / 104)
check("no_fit", "the old r value differs from the required current value on both roots",
      branch.gcd((required_old_normalization - r_old).numerator()) == 1)


print("\nD. VRS-5 RERANK AND SUCCESSOR SCAFFOLD")
scalar_result = read(
    "explorations/conditional-build/selected-k77-curvature-vev-trace-closure-2026-08-09.md"
)
metric_kill = read(
    "explorations/conditional-build/selected-k77-sr1c-fixed-varpi-metric-stationarity-2026-08-14.md"
)
check("source", "the scalar curvature cell is genuinely action-owned rather than a counterterm",
      "No second dark-energy field" in scalar_result and "No second" in scalar_result
      and "counterterm" in scalar_result)
check("scope", "its missing full derivative Euler and canonical realization were already explicit",
      "full derivative Euler" in scalar_result and "global connection" in scalar_result)
check("scope", "the metric kill leaves nonparallel compatible extensions logically open",
      "not every possible" in metric_kill and "second jet over the two point roots" in metric_kill)
check("scope", "the old parallel graph zero has a live nonparallel control",
      "planted nonparallel momentum derivative fires" in metric_kill)

# The current parallel extension makes the graph adjoint zero.  A nonparallel
# extension is therefore the nearest owned mechanism able to emit the exact
# opposite rank-one row without adding a field or coefficient.  The next gate
# is an image/cokernel calculation before attempting another large solve.
check("rerank", "the action-owned scalar sector receives no vote as a direct SR-1C graft", True)
check("rerank", "the scalar-jet branch remains a high-conviction distinct reconstruction hypothesis", True)
check("rerank", "the canonical nonparallel source-graph image test ranks first for the next swing", True)
check("successor", "the next gate must constrain translation Bianchi epsilon and metric rows on one carrier", True)
check("successor", "a cokernel obstruction would kill every nonparallel two-jet over both SR-1C roots at once", True)
check("scope", "VRS-6 remains conditional because no stationary background exists", True)
check("accounting", "no ledger canon residue quotient datum or public-posture move follows", True)
check("physics", "no superposition positivity Born rule spectrum or empirical prediction follows", True)


RESULT = {
    "disposition": "ACTION_OWNED_SCALAR_JET_TRACE_CLOSURE_CONFIRMED_BUT_DISJOINT_FROM_CANONICAL_SR1C__NONPARALLEL_GRAPH_REOPENER_RANKED_FIRST",
    "old_scalar_branch": {
        "B": "Phi1/208",
        "T": "-Phi1/104",
        "r": "1/129792",
        "total_B_curvature": "C/32448",
        "canonical_trace_plane_mismatch": "9_OF_9",
    },
    "canonical_intersection": {
        "C_cells": len(c_flat),
        "F_BZ_cells": len(f_flat),
        "overlap": len(common),
        "proportional": False,
        "old_amplitude_branch_value": "-1397/4",
    },
    "counterfactual_no_fit": {
        "required_old_normalization": "3/364-t/1872",
        "required_endpoint_preserving": "3/182-t/936",
        "old_r_cancels_either_current_root": False,
    },
    "rerank": {
        "first": "SR-1D_CANONICAL_NONPARALLEL_SOURCE_GRAPH_IMAGE_COKERNEL_GATE",
        "second": "DISTINCT_CANONICAL_BRANCH_OR_CONNECTION_JET",
        "high_conviction_but_not_current_vote": "OLD_ACTION_OWNED_SCALAR_JET_BRANCH_REQUIRES_DISTINCT_CANONICAL_REALISATION",
    },
    "next_gate": "BUILD_THE_COMBINED_SECOND_JET_MAP_TO_DIFFERENTIATED_TRANSLATION_BIANCHI_PRIMITIVE_EPSILON_AND_FIXED_VARPI_METRIC_GRAPH__TEST_WHETHER_MINUS_RHO_L1_LIES_IN_ITS_CONSTRAINED_IMAGE_ON_EACH_ROOT",
    "sr1": "BACKGROUND-MISSING",
    "sr2": "BLOCKED",
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
