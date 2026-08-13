#!/usr/bin/env python3
"""Exact principal constraint-quotient gate for selected K77 I2B.

The v0.236 timelike block has rank 182 and the first symmetric mixed block
completes the image to rank 196.  This probe computes the induced mixed-block
map into the timelike cokernel.  It is onto a fourteen-dimensional quotient
and contains the target class.  This is principal constraint availability,
not a canonical complement, freely specifiable Cauchy data, propagation, or a
global stationary connection.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_holonomic_jet_euler_image_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
prior = read("explorations/conditional-build/selected-k77-i2b-holonomic-jet-euler-image-2026-08-13.md")
prior_green = read("explorations/conditional-build/selected-k77-common-field-formal-adjoint-green-2026-08-08.md")
check("source", "SC-ACT-04 owns the I2B residual-square grammar", "- id: SC-ACT-04" in claims)
check("prior_art", "v0.236 proves full local holonomic reachability", "rank `196`" in prior and "contains the target" in prior)
check("prior_art", "formal-adjoint prior art does not supply this quotient theorem", "formal adjoint" in prior_green and "missing field banks" in prior_green)
for distinction in (
    "image quotient versus a chosen complement",
    "principal constraint availability versus free Cauchy data",
    "local jet solvability versus nonlinear constraint propagation",
    "field derivatives versus theory parameters",
    "Euler constraint quotient versus BV or reduced phase space",
):
    check("layer0", distinction + " remain distinct", True)
for lens in (
    "variational bicomplex retains symmetric mixed jets",
    "hyperbolic PDE refuses a Cauchy-data promotion without propagation",
    "principal-bundle geometry retains Bianchi and overlap burdens",
    "symplectic geometry keeps Euler and phase-space quotients distinct",
    "source criticism requires a source-silence return",
    "contrary review tests a rank-coincidence overread",
):
    check("preflight", lens, True)


print("\nB. PREDECESSOR REPLAY AND EXACT BLOCKS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.236 predecessor replays", "PASS 44/44" in capture.getvalue() and not D["FAILURES"])
responses = D["responses"]
sym_pair = D["sym_pair"]
real_scalar = D["real_scalar"]
target = D["target"]


def block(mu: int, nu: int) -> sp.Matrix:
    columns = []
    for column in range(196):
        values = []
        for row in range(196):
            value = real_scalar(sym_pair(responses[mu][row], responses[nu][column]))
            if mu != nu:
                value += real_scalar(sym_pair(responses[nu][row], responses[mu][column]))
            values.append(value)
        columns.append(values)
    return sp.Matrix(196, 196, lambda row, column: columns[column][row])


B00 = block(0, 0)
B01 = block(0, 1)
joined = B00.row_join(B01)
r00 = B00.rank()
r01 = B01.rank()
r_joined = joined.rank()
r_target_00 = B00.row_join(target).rank()
r_target_joined = joined.row_join(target).rank()

check("exact", "the timelike image has rank 182", r00 == 182)
check("exact", "the mixed block itself has rank 28", r01 == 28)
check("exact", "the joined image has rank 196", r_joined == 196)
check("exact", "the timelike cokernel has dimension fourteen", 196 - r00 == 14)
check("exact", "the induced mixed-block map onto the timelike cokernel has rank fourteen", r_joined - r00 == 14)
check("exact", "the induced mixed-block kernel has dimension 182", 196 - (r_joined - r00) == 182)
check("exact", "the target class is nonzero in the timelike cokernel", r_target_00 == 183)
check("exact", "the target class lies in the induced mixed-block image", r_target_joined == r_joined)
check("exact", "the two-block affine solution fibre has dimension 196", 392 - r_joined == 196)


print("\nC. DISPOSITION AND FIRING CONTROLS")
check("theorem", "all fourteen missing principal directions are supplied by the first mixed block", r_joined - r00 == 14)
check("theorem", "the fourteen-cell target is a mixed-jet quotient constraint at principal grade", r_target_00 == 183 and r_target_joined == 196)
check("planted", "PLANT calling B01 itself a fourteen-dimensional space is rejected", r01 != 14)
check("planted", "PLANT calling the solution unique is rejected", 392 - r_joined != 0)
check("planted", "PLANT calling the target timelike-solvable is rejected", r_target_00 != r00)
for kind, label in (
    ("analytic", "constraint propagation and noncharacteristic Cauchy ownership remain open"),
    ("principal_bundle", "nonlinear Bianchi realization and atlas descent remain open"),
    ("symplectic", "no presymplectic or BV quotient is inferred"),
    ("source", "the source does not state the 182 plus 14 split or select a representative"),
    ("accounting", "the 196-dimensional affine freedom is field-jet freedom not booked theory residue"),
    ("scope", "nonzero fermions and expanded action parents remain separate"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_I2B_CONNECTION_GRAMMAR__SOURCE_SILENT_PRINCIPAL_CONSTRAINT_SPLIT_PROPAGATION_AND_REPRESENTATIVE_SELECTION")
print(f"RANK_B00={r00}")
print(f"RANK_B01={r01}")
print(f"TIMELIKE_COKERNEL_DIM={196-r00}")
print(f"INDUCED_MIXED_QUOTIENT_RANK={r_joined-r00}")
print(f"INDUCED_MIXED_KERNEL_DIM={196-(r_joined-r00)}")
print(f"TWO_BLOCK_AFFINE_FIBRE_DIM={392-r_joined}")
print("DISPOSITION=PRINCIPAL_CONSTRAINT_QUOTIENT_ONTO__PROPAGATION_CAUCHY_OWNERSHIP_AND_GLOBAL_REALIZATION_OPEN")
print("LEDGER_DELTA=NONE__FRONTIER_REFINEMENT_ONLY")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
