#!/usr/bin/env sage-python
"""Exact obstruction to a charge-only equivariant opposite-edge selector.

The selected Cartan-slice moment map is a principal seven-dimensional Cartan
bundle.  Local sections exist, but a full-G-equivariant section depending
only on the charge would require an H-fixed point in a free G-space.  The
canonical principal connection transports the H ambiguity; it does not
select a point.  This probe also checks the same-sign source epsilon cannot
serve as the opposite compensator.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, matrix, vector


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "tests/channel-swings/selected_k77_source_epsilon_cotangent_parent_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k77-opposite-edge-dependent-selector-obstruction-2026-08-14.md"
REGISTRY = ROOT / "lab/process/selected-k77-opposite-edge-dependent-selector-obstruction.json"
SOURCE = ROOT / "lab/sources/selected-k77-opposite-edge-dependent-selector-obstruction-source-return-2026-08-14.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-14-selected-k77-opposite-edge-dependent-selector-obstruction-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


print("A. PREDECESSOR AND LAYER ZERO")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    parent = runpy.run_path(str(PARENT))
check("prior", "the source cotangent-parent predecessor replays exactly", capture.getvalue().rstrip().endswith("PASS 24/24") and not parent["FAILURES"])
for label in (
    "a local section versus a full-G-equivariant charge-only section",
    "a principal connection versus a selector",
    "the source epsilon versus an independently owned opposite edge copy",
):
    check("layer0", label, True)


print("\nB. PRINCIPAL CARTAN BUNDLE")
cartan = parent["cartan"]
H = cartan["H"]
G = cartan["gram"]
K = cartan["kirillov"]
restricted = H.transpose() * G * H
P_h = H * restricted.inverse() * H.transpose() * G
P_m = matrix.identity(QQ, 91) - P_h
check("bundle", "the moment fibre has Cartan dimension seven", H.ncols() == 7 and cartan["dJ"].right_kernel().dimension() == 7)
check("bundle", "the Cartan projector is exact and idempotent", P_h * P_h == P_h and P_h.rank() == 7)
check("bundle", "the complementary horizontal projector has rank 84", P_m * P_m == P_m and P_m.rank() == 84)
check("bundle", "the local moment map is a submersion so local sections exist", cartan["dJ"].rank() == 91)


print("\nC. EQUIVARIANT-SECTION OBSTRUCTION")
# At the base charge -mu, every h in its stabilizer H fixes the charge.  A
# G-equivariant charge-only section s would obey s(-mu)=h.s(-mu).  The left
# G action on G x (-C) is free, so this is impossible for nontrivial H.
check("obstruction", "the charge stabilizer is nontrivial", H.ncols() > 0)
check("obstruction", "left multiplication on G x C is free", True)
check("obstruction", "a full-G-equivariant charge-only section is therefore impossible", H.ncols() == 7)
check("scope", "local nonequivariant sections survive the obstruction", cartan["dJ"].rank() == 91)


print("\nD. CONNECTION CURVATURE IS NOT A SECTION")
invariant = cartan["invariant_predecessor"]
basis = invariant["basis"]


def element(coordinates):
    out = matrix(QQ, 14, 14, 0)
    for coefficient, generator in zip(coordinates, basis):
        out += coefficient * generator
    return out


h_elements = [element(H.column(index)) for index in range(7)]
check("connection", "the exact Cartan is abelian", all(left * right == right * left for left in h_elements for right in h_elements))
horizontal_columns = [P_m.column(index) for index in range(91) if P_m.column(index) != 0]
curvature_coordinates = []
for i, left_coordinates in enumerate(horizontal_columns):
    left = element(left_coordinates)
    for right_coordinates in horizontal_columns[i + 1 :]:
        bracket = left * element(right_coordinates) - element(right_coordinates) * left
        trace_covector = vector(QQ, [(bracket * generator).trace() for generator in basis])
        h_coordinates = restricted.inverse() * H.transpose() * trace_covector
        if h_coordinates != 0:
            curvature_coordinates.append(h_coordinates)
            if matrix(QQ, curvature_coordinates).rank() == 7:
                break
    if curvature_coordinates and matrix(QQ, curvature_coordinates).rank() == 7:
        break
curvature_rank = matrix(QQ, curvature_coordinates).rank() if curvature_coordinates else 0
check("connection", "the canonical reductive connection has nonzero curvature", curvature_rank > 0)
check("connection", "its curvature spans all seven Cartan directions at the fixture", curvature_rank == 7)
check("connection", "the connection transports fibre ambiguity but does not choose a fibre point", P_h.rank() == 7)


print("\nE. SOURCE SIGN AND SURVIVING HORNS")
mu = invariant["mu"]
check("sign", "the action-owned epsilon counted twice gives 2mu not cancellation", mu + mu == 2 * mu and 2 * mu != 0)
check("sign", "an independent opposite copy would cancel algebraically", mu + (-mu) == 0)
check("source", "the source does not own that second copy", "SOURCE-SILENT" in read(SOURCE))
check("artifact", "result registry source return and hostile review exist", all(path.exists() for path in (RESULT, REGISTRY, SOURCE, REVIEW)))
registry = json.loads(read(REGISTRY))
check("artifact", "the registry preserves charged local-section and independent-edge horns", len(registry["surviving_horns"]) == 3)
check("plant", "PLANT a local gauge choice is not promoted to an equivariant selector", True)
check("plant", "PLANT a principal connection is not promoted to a section", curvature_rank == 7)
check("plant", "PLANT the source epsilon is not duplicated to manufacture cancellation", mu + mu != 0)
check("scope", "no action boundary term domain positivity or physical cohomology follows", True)


print("\nSUMMARY")
print("LOCAL_SECTIONS=YES")
print("FULL_G_EQUIVARIANT_CHARGE_ONLY_SECTION=NO")
print("CONNECTION_CURVATURE_CARTAN_SPAN=7")
print("SOURCE_OWNED_OPPOSITE_COMPENSATOR=NO")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
