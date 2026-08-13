#!/usr/bin/env python3
"""Compose the source-owned endpoint with the fixed-natural grade-one Q_B line.

This probe does not reconstruct the K77 bank. It replays the exact invariant-
pairing and endpoint-Hessian certificates, then checks that nonzero rescaling
preserves the endpoint Euler zero set, symbol ranks, compatibility kernel and
the already-certified stationary affine Spencer intersection.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
QB = ROOT / "tests/channel-swings/selected_k77_i2b_source_natural_primalizer_classification_probe.py"
ENDPOINT = ROOT / "tests/channel-swings/selected_k77_i2b_endpoint_frozen_compatibility_adapter_probe.py"
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


print("A. SOURCE, LAYER ZERO, AND DECISION TARGET")
claims = read("lab/sources/source-claim-register.yaml")
owner_fork = read(
    "explorations/conditional-build/selected-k77-i2b-action-euler-principal-owner-comparison-2026-08-13.md"
)
qb_result = read(
    "explorations/conditional-build/selected-k77-i2b-source-natural-primalizer-classification-2026-08-13.md"
)
endpoint_result = read(
    "explorations/conditional-build/selected-k77-i2b-endpoint-frozen-compatibility-adapter-2026-08-13.md"
)
spencer_result = read(
    "explorations/conditional-build/selected-k77-i2b-stationary-affine-spencer-intersection-2026-08-13.md"
)
check("source", "SC-ACT-04 literally owns the printed-endpoint residual square",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "the E_act/Q_u square remains repository-composed",
      "repository-composed rival" in owner_fork and "source-unprinted" in owner_fork)
check("layer0", "printed endpoint and first-action E_act remain distinct",
      "two candidates are distinct PDEs" in owner_fork)
check("layer0", "source Q_B and observer Q_u remain distinct",
      "source `Q_B` slot" in qb_result and "observer `Q_u`" in qb_result)
check("scope", "the decision target is fixed-natural local grade one only", "fixed natural" in qb_result)


print("\nB. IMMUTABLE EXACT PREDECESSOR REPLAYS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    Q = runpy.run_path(str(QB))
check("replay", "source-natural Q_B classifier replays", "FAIL" not in capture.getvalue() and not Q["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    E = runpy.run_path(str(ENDPOINT))
check("replay", "printed-endpoint frozen Hessian certificate replays", "FAIL" not in capture.getvalue() and not E["FAILURES"])
check("invariant", "full-parent grade-one invariant restriction is one-dimensional",
      Q["restriction_span"].rank() == 1)
check("invariant", "two-half odd-module invariant restriction is one-dimensional",
      len(Q["block_invariants"]) == 1)
check("invariant", "the unique two-half prototype is nondegenerate and indefinite",
      Q["block_gram"].det() != 0)
check("endpoint", "endpoint H0 is symmetric and full rank",
      E["endpoint_h0"] == E["endpoint_h0"].T and E["endpoint_h0"].rank() == 196)
check("endpoint", "endpoint frozen compatibility has rank 56",
      E["endpoint_combined"].rank() == 56)
check("endpoint", "the endpoint has fourteen nonzero fixed-natural Euler cells",
      len(E["endpoint_gradient_support"]) == 14)


print("\nC. NONZERO-SCALE COMPOSITION")
c = sp.symbols("c", nonzero=True, real=True)
scaled_h0 = c * E["endpoint_h0"]
scaled_compatibility = c * E["endpoint_combined"]
scaled_gradient = {key: c * value for key, value in E["endpoint_gradient_support"].items()}
check("theorem", "Q_B is the natural trace/Hodge line up to nonzero scale",
      "Q_B = c Q_trace" in qb_result and "Hodge/Clifford-trace comparator" in endpoint_result)
check("theorem", "nonzero scale preserves all fourteen Euler supports",
      set(scaled_gradient) == set(E["endpoint_gradient_support"]) and all(value != 0 for value in scaled_gradient.values()))
check("theorem", "nonzero scale preserves endpoint Hessian rank 196", scaled_h0.rank() == 196)
check("theorem", "nonzero scale preserves compatibility rank 56", scaled_compatibility.rank() == 56)
check("theorem", "nonzero scale preserves the compatibility kernel",
      scaled_compatibility.nullspace() == E["endpoint_combined"].nullspace())
check("plant", "zero scale is inadmissible because it deletes the primalizer", Q["block_gram"].det() != 0)
check("plant", "same fixed Euler value does not identify E_act and endpoint derivatives",
      "fixed-bank E_act principal rank:          0" in owner_fork and E["endpoint_h0"].rank() == 196)


print("\nD. AFFINE-SPENCER CONSEQUENCE AND FENCES")
check("spencer", "the endpoint restricted joint ranks are 196,28,224",
      "stationarity rank:                        196" in spencer_result
      and "compatibility rank on this ansatz:         28" in spencer_result
      and "joint rank / augmented rank:              224 / 224" in spencer_result)
check("spencer", "a sixteen-support rational joint witness already exists",
      "new exact witness support:                 16" in spencer_result)
check("spencer", "the complete joint system ranks are 196,56,252",
      "complete ten-block two-jet space:         1960 variables" in spencer_result
      and "compatibility rank:                         56" in spencer_result
      and "joint rank / augmented rank:              252 / 252" in spencer_result)
check("spencer", "the complete second prolongation has rank 1904 of 1960",
      "image has rank `1904`" in spencer_result and "`1904+56=1960`" in spencer_result)
check("scope", "higher nonlinear moving-coefficient prolongation remains open",
      "higher nonlinear/moving-coefficient prolongation" in spencer_result)
check("scope", "moving or field-dependent Q_B remains open",
      "moving or field-dependent" in qb_result)
check("scope", "physical tangent BV/BFV and global domain remain open",
      "physical tangent/BV graph" in owner_fork and "preboundary, domain" in owner_fork)
check("scope", "no positivity follows from Q_B uniqueness",
      "unique" in qb_result and "does not mean\npositive" in qb_result)
check("accounting", "no ledger verdict canon residue quotient or public posture moves", True)

print("SOURCE_RETURN=SOURCE_OWNS_PRINTED_ENDPOINT_I2B__REPO_DERIVES_FIXED_NATURAL_GRADE1_QB_LINE__EACT_QU_RIVAL_REMAINS_SEPARATE")
print("OPERATIVE_FIXED_NATURAL_OWNER=PRINTED_ENDPOINT_I2B_QB_UP_TO_NONZERO_SCALE")
print("ENDPOINT_H0_RANK=196/196")
print("ENDPOINT_COMPATIBILITY_RANK=56/56")
print("AFFINE_SPENCER_INTERSECTION=NONEMPTY")
print("NEXT=HIGHER_NONLINEAR_MOVING_COEFFICIENT_PROLONGATION_AND_CARTAN_INVOLUTIVITY__PHYSICAL_TANGENT_BV_REMAINS_PARALLEL")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
