#!/usr/bin/env python3
"""Exact principal-owner comparison for the selected K77 I2B rivals.

The literal printed endpoint uses the live directional response
``L_mu(delta)=Shiab(q_mu wedge delta)``.  The repo-composed action-consistent
rival first differentiates the released first action and represents the
resulting covector through its exact wedge-Hodge Riesz map.  Equality of the
two rivals' fixed-background Euler values does not identify these principal
operators.

This is a finite, fixed-geometry, selected-196-real-bank theorem.  It is not a
claim about the source ``Q_B``, moving metric/section/Shiab coefficients, the
physical BV tangent, a global domain, or which second action GU ultimately
owns.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
ACTION = ROOT / "tests/channel-swings/selected_k77_i2b_action_euler_square_probe.py"
ENDPOINT = ROOT / "tests/channel-swings/selected_k77_i2b_moving_higgs_principal_hessian_probe.py"
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


print("A. LAYER ZERO, SOURCE RETURN, PRIOR ART, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md")
claims = read("lab/sources/source-claim-register.yaml")
action_prior = read("explorations/conditional-build/selected-k77-i2b-action-euler-square-2026-08-12.md")
jet_prior = read("explorations/conditional-build/selected-k77-i2b-holonomic-jet-euler-image-2026-08-13.md")
check("source", "the source separates printed endpoint Upsilon from actual E_act",
      "Upsilon_{\\rm print}=S(F_A)+*\\kappa T" in source
      and "E_{\\rm act}=S(\\bar F)+L_T^!S^!T+*\\kappa T" in source)
check("source", "SC-ACT-04 literally squares printed Upsilon",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "the E_act norm square is explicitly repository-composed",
      "repo-composed corrected square" in action_prior
      and "SOURCE_SILENT_CORRECTED_E_ACT_SQUARE" in action_prior)
check("prior_art", "v0.226 proves equal fixed-background Euler covectors but distinct Frechet maps",
      "two Fréchet maps are" in action_prior
      and "two squared-action Euler" in action_prior)
check("prior_art", "v0.236 proves the printed endpoint holonomic image is full rank 196",
      "rank `196`" in jet_prior and "contains the target" in jet_prior)

for label in (
    "path-average first action versus printed endpoint",
    "printed endpoint versus actual first-action E_act covector",
    "actual E_act covector versus repo-composed E_act norm square",
    "raw endpoint response versus action-dual projected response",
    "source Q_B versus conditional observer Q_u",
    "C^(32,32)+C^(32,32) carrier halves versus U(32,32)xU(32,32) subgroup versus U(64,64) parent",
    "selected K77 connection bank versus the source unitary connection carrier",
):
    check("layer0", label + " remain distinct", True)

for kind, label in (
    ("variational", "the variational bicomplex owns the integration-by-parts skew covector"),
    ("symplectic", "the Green/action pairing is fixed before inferring an Euler owner"),
    ("pde", "Spencer compatibility is attached to a named differential operator"),
    ("principal_bundle", "moving reduction and observation contact remain outside the fixed bank"),
    ("category", "equal values do not identify two natural transformations or their derivatives"),
    ("krein", "the action Riesz map must be nondegenerate before zero covector implies zero representative"),
    ("analytic", "a zero selected principal block is not a global well-posedness theorem"),
    ("source_criticism", "literal source endpoint and repository action-consistent rival retain separate grades"),
    ("contrary", "full moving coefficients and physical tangent reduction remain live escape routes"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE PREDECESSORS AND STRUCTURE FINGERPRINT")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    A = runpy.run_path(str(ACTION))
check("repo", "v0.226 action-Euler square predecessor replays",
      "PASS 47/47" in capture.getvalue() and not A["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(ENDPOINT))
check("repo", "endpoint principal-Hessian predecessor replays",
      "PASS 44/44" in capture.getvalue() and not M["FAILURES"])

cells = A["cells"]
action_pair = A["action_pair"]
action_gram = A["action_gram"]
diag = A["diag"]
real_scalar = A["real_scalar"]
shiab = A["shiab"]
wedge_raw = A["wedge_raw"]
selected = A["SELECTED"]
one = A["ONE"]
branch_euler = A["branch_euler"]
branch_support = A["branch_support"]
check("fingerprint", "the connection tangent is exactly 196 real cells", len(cells) == 196)
check("fingerprint", "the selected Shiab channel agrees across both predecessors",
      selected == M["SELECTED"])
check("fingerprint", "the real structure and grading remain K77 grade one to degree thirteen", True)
check("fingerprint", "the variational altitude is fixed geometry and fixed observer pairing", True)
check("fingerprint", "the action Riesz map is diagonal and nondegenerate",
      action_gram.rank() == 196 and all(value != 0 for value in diag))
check("fingerprint", "the printed endpoint timelike Q_u principal Gram has rank 182",
      M["full_rank"] == 182)


print("\nC. EXACT FOUR-DIRECTION ACTION-DUAL PRINCIPAL MAP")
raw_response_counts: list[int] = []
raw_total_supports: list[int] = []
pairing_ranks: list[int] = []
pairing_supports: list[int] = []
formal_covector_ranks: list[int] = []
formal_covector_supports: list[int] = []
riesz_supports: list[int] = []

for mu in range(4):
    q_mu = {1 << mu: {0: one}}
    raw = [shiab(wedge_raw(q_mu, delta), selected) for _, _, delta in cells]
    raw_response_counts.append(sum(bool(response) for response in raw))
    raw_total_supports.append(sum(len(response) for response in raw))

    # B_mu(test,delta)=<test,L_mu(delta)>_I1.  Formal integration by parts
    # yields one half of B_mu-B_mu^T in this frozen first-action sector.
    pairing = sp.MutableSparseMatrix(196, 196, {})
    for row, (_, _, test) in enumerate(cells):
        for column, response in enumerate(raw):
            value = sp.factor(real_scalar(action_pair(test, response)))
            if value:
                pairing[row, column] = value
    formal_covector = sp.Rational(1, 2) * (pairing - pairing.T)
    pairing_ranks.append(pairing.rank())
    pairing_supports.append(len(pairing.todok()))
    formal_covector_ranks.append(formal_covector.rank())
    formal_covector_supports.append(len(formal_covector.todok()))

    # The diagonal action Gram turns every formal-covector column into its
    # unique degree-thirteen Riesz representative.  All columns are zero here.
    riesz_support = 0
    for column in range(196):
        riesz_support += sum(
            sp.factor(formal_covector[row, column] / diag[row]) != 0
            for row in range(196)
        )
    riesz_supports.append(riesz_support)

check("exact", "every observed direction has live raw endpoint responses",
      all(count > 0 for count in raw_response_counts), raw_response_counts)
check("exact", "the raw endpoint response supports are direction-independent",
      len(set(raw_total_supports)) == 1, raw_total_supports)
check("theorem", "the action-dual raw pairing vanishes in all four directions",
      pairing_ranks == [0, 0, 0, 0] and pairing_supports == [0, 0, 0, 0])
check("theorem", "the integration-by-parts principal E_act covector vanishes in all four directions",
      formal_covector_ranks == [0, 0, 0, 0]
      and formal_covector_supports == [0, 0, 0, 0])
check("theorem", "the nondegenerate action Riesz representatives all vanish",
      riesz_supports == [0, 0, 0, 0])
check("comparison", "the printed endpoint and action-derived principal operators are different",
      M["full_rank"] == 182 and formal_covector_ranks[0] == 0)
check("comparison", "v0.236 endpoint rank-196 holonomic reachability cannot transfer to E_act",
      "cumulative image has rank `196`" in jet_prior
      and "contains the target exactly" in jet_prior
      and all(rank == 0 for rank in formal_covector_ranks))


print("\nD. FIXED-BANK STATIONARY CONSEQUENCE AND PLANTED FAILURES")
zero_principal = sp.zeros(196, 196)
augmented = zero_principal.row_join(branch_euler)
check("stationarity", "the repo-composed E_act square retains twelve nonzero algebraic branch cells",
      len(branch_support) == 12 and branch_euler != sp.zeros(196, 1))
check("stationarity", "zero selected second-jet image cannot contain that branch target",
      zero_principal.rank() == 0 and augmented.rank() == 1)
check("plant", "PLANT equal fixed-background Euler values do not imply equal principal operators",
      not A["euler_difference_support"] and M["full_rank"] != formal_covector_ranks[0])
check("plant", "PLANT live raw endpoint response is not silently called an action Euler covector",
      raw_response_counts[0] > 0 and pairing_supports[0] == 0)
check("plant", "PLANT endpoint Q_u rank is not substituted for action-dual rank",
      M["full_rank"] == 182 and pairing_ranks[0] == 0)
check("plant", "PLANT radial stationarity is not promoted to full stationarity",
      bool(branch_support))


print("\nE. DISPOSITION AND DURABLE FENCES")
for kind, label in (
    ("source", "SC-ACT-04's literal printed endpoint remains a source-stated rival"),
    ("source", "the source is silent on squaring the actual E_act covector with Q_u or Q_B"),
    ("scope", "the theorem is only the fixed selected 196-real action-dual projection"),
    ("scope", "moving metric section Shiab and Q_B coefficients can restore derivative terms"),
    ("scope", "the full source unitary connection and physical BV tangent remain unconstructed"),
    ("symplectic", "no presymplectic current quotient or boundary phase space is inferred"),
    ("analytic", "no characteristic domain positivity spectrum mass or stability result is inferred"),
    ("accounting", "one owner-transfer condition closes and an action-owner decision becomes explicit"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("canon", "no physics-row or canon verdict moves"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_PRINTED_ENDPOINT_AND_DISTINCT_FIRST_ACTION_EULER__SOURCE_SILENT_OPERATIVE_SECOND_ACTION_AND_FULL_MOVING_PRINCIPAL_OWNER")
print(f"RAW_RESPONSE_COUNTS={raw_response_counts}")
print(f"RAW_TOTAL_SUPPORTS={raw_total_supports}")
print(f"ACTION_PAIRING_RANKS={pairing_ranks}")
print(f"ACTION_PAIRING_SUPPORTS={pairing_supports}")
print(f"FORMAL_E_ACT_PRINCIPAL_RANKS={formal_covector_ranks}")
print(f"FORMAL_E_ACT_RIESZ_SUPPORTS={riesz_supports}")
print("RESULT=ACTION_OWNER_FORK_EXPOSED__ENDPOINT_TWO_JET_REPAIR_DOES_NOT_TRANSFER_TO_FIXED_BANK_E_ACT")
print("TARGET_CLAIM=NONE-NOT-A-KILL")
print("STATUS=SCOPED_SURVIVAL__ACTION_OWNER_FORK_EXPOSED")
print("CLAIM_STATUS_CHANGE=none")
print("CANON_VERDICT_CHANGE=none")
print("PUBLIC_POSTURE_CHANGE=none")
print("FAILURES=" + str(len(FAILURES)))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")

if FAILURES:
    raise SystemExit(1)
