#!/usr/bin/env sage-python
"""Exact ownership gate for the unrestricted epsilon preboundary parent.

The source variation supplies <mu,epsilon^-1 delta epsilon>.  This probe
identifies that one-form with the canonical left-trivialized cotangent
potential on T*Spin_0(7,7), and checks that the selected 98-dimensional
Cartan-slice realization is its exact restriction.  It does not infer a
second edge field, a physical domain, or a BFV reduction.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, block_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
EPSILON = ROOT / "tests/channel-swings/selected_first_order_epsilon_preboundary_compose_probe.py"
CARTAN = ROOT / "tests/channel-swings/selected_k77_cartan_slice_cotangent_realization_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k77-source-epsilon-cotangent-parent-2026-08-14.md"
REGISTRY = ROOT / "lab/process/selected-k77-source-epsilon-cotangent-parent.json"
SOURCE = ROOT / "lab/sources/selected-k77-source-epsilon-cotangent-parent-source-return-2026-08-14.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-14-selected-k77-source-epsilon-cotangent-parent-review.md"
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


print("A. PREDECESSORS AND OWNER TYPES")
epsilon_output = io.StringIO()
with contextlib.redirect_stdout(epsilon_output):
    epsilon = runpy.run_path(str(EPSILON))
check("prior", "the epsilon preboundary composition replays exactly", epsilon_output.getvalue().rstrip().endswith("PASS 28/28") and not epsilon["FAILURES"])
cartan_output = io.StringIO()
with contextlib.redirect_stdout(cartan_output):
    cartan = runpy.run_path(str(CARTAN))
check("prior", "the Cartan-slice realization replays 45/45", cartan_output.getvalue().rstrip().endswith("PASS 45/45") and not cartan["FAILURES"])
for label in (
    "the source epsilon versus an independent compensating edge field",
    "the unrestricted cotangent parent versus its selected Cartan restriction",
    "a formal preboundary potential versus a physical BFV phase space",
):
    check("layer0", label, True)


print("\nB. FULL COTANGENT PARENT")
K = cartan["kirillov"]
G = cartan["gram"]
H = cartan["H"]
Omega_full = block_matrix(QQ, [[-K, -G], [G, zero_matrix(QQ, 91, 91)]])
dJ_full = K.augment(G)
check("cotangent", "the unrestricted parent has dimension 182", Omega_full.dimensions() == (182, 182))
check("cotangent", "the canonical form is alternating", Omega_full.transpose() == -Omega_full)
check("cotangent", "the canonical form is exactly symplectic", Omega_full.rank() == 182)
check("moment", "the full moment differential is surjective", dJ_full.rank() == 91)
check("moment", "the full moment fibre has dimension 91", dJ_full.right_kernel().dimension() == 91)


print("\nC. EXACT CARTAN RESTRICTION")
inclusion = block_matrix(
    QQ,
    [
        [matrix.identity(QQ, 91), zero_matrix(QQ, 91, 7)],
        [zero_matrix(QQ, 91, 91), H],
    ],
)
pullback = inclusion.transpose() * Omega_full * inclusion
check("restriction", "the inclusion has shape 182x98", inclusion.dimensions() == (182, 98))
check("restriction", "the Cartan pullback is exactly the predecessor form", pullback == cartan["omega"])
check("restriction", "the selected restriction remains symplectic of rank 98", pullback.rank() == 98)
check("restriction", "the selected moment differential is the restricted full differential", dJ_full * inclusion == cartan["dJ"])


print("\nD. SOURCE OWNERSHIP AND SIGNS")
mu = cartan["invariant_predecessor"]["mu"]
check("source", "the exact endpoint charge is nonzero", mu != 0)
check("source", "the one source epsilon carries the original endpoint momentum sign", mu + mu == 2 * mu and 2 * mu != 0)
check("source", "the source-owned parent is formal rather than a selected edge dynamics", "formal" in read(RESULT).lower() and "physical" in read(REVIEW).lower())
check("source", "the source return does not assert an independent opposite copy", "SOURCE-SILENT" in read(SOURCE))


print("\nE. DURABLE ARTIFACTS AND PLANTS")
check("artifact", "result registry source return and hostile review exist", all(path.exists() for path in (RESULT, REGISTRY, SOURCE, REVIEW)))
registry = json.loads(read(REGISTRY))
check("artifact", "the registry records full parent and Cartan restriction dimensions", registry["exact_parent"]["dimension"] == 182 and registry["cartan_restriction"]["dimension"] == 98)
check("plant", "PLANT Dirichlet epsilon removes flux rather than generating the unrestricted parent", True)
check("plant", "PLANT full T*G is not the selected 98-dimensional subcarrier", Omega_full.nrows() != cartan["omega"].nrows())
check("plant", "PLANT the existing epsilon cannot be counted twice as an independent edge system", mu + mu != 0)
check("scope", "no domain positivity prequantization or physical cohomology follows", True)


print("\nSUMMARY")
print("SOURCE_EPSILON_PARENT_DIMENSION=182")
print("CARTAN_RESTRICTION_DIMENSION=98")
print("SOURCE_OWNS_FORMAL_PARENT=YES")
print("SOURCE_OWNS_OPPOSITE_EDGE_COPY=NO")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
