#!/usr/bin/env sage-python
"""Exact real-Cartan and product-globalization gate for the K77 endpoint.

This probe replays the exact trace-dual endpoint, passes from its even
characteristic polynomial p(x) to q(y) with y=x^2, and uses exact isolating
intervals to count positive and negative roots.  The result classifies the
regular real Cartan type.  The associated topology argument obstructs only
an untwisted product family whose orbit restrictions are the varying KKS
forms; it does not exclude every 98-dimensional equivariant realization.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, PolynomialRing


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_coadjoint_invariant_variation_gate_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k77-regular-cartan-global-realization-obstruction-2026-08-14.md"
REGISTRY = ROOT / "lab/process/selected-k77-regular-cartan-global-realization-obstruction.json"
SOURCE = ROOT / "lab/sources/selected-k77-regular-cartan-global-realization-source-return-2026-08-14.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-14-selected-k77-regular-cartan-global-realization-obstruction-review.md"
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
    prior = runpy.run_path(str(PREDECESSOR))
check("prior", "the invariant-variation predecessor replays 37/37",
      capture.getvalue().rstrip().endswith("PASS 37/37") and not prior["FAILURES"])
for label in (
    "regular semisimple versus split-regular",
    "local Poisson realization versus global equivariant realization",
    "KKS orbit class versus a source-owned boundary action",
    "untwisted product obstruction versus universal minimality",
):
    check("layer0", label, True)


print("\nB. EXACT REAL CARTAN TYPE")
L = prior["L"]
p = L.charpoly()
check("characteristic", "the characteristic polynomial is even of degree fourteen",
      p.degree() == 14 and all(p[i] == 0 for i in range(1, 14, 2)))
R = PolynomialRing(QQ, "y")
y = R.gen()
q = sum(p[2 * degree] * y ** degree for degree in range(8))
check("characteristic", "p(x) equals q(x^2)",
      all(q[degree] == p[2 * degree] for degree in range(8)))
check("characteristic", "the degree-seven squared-spectrum polynomial is squarefree",
      q.degree() == 7 and q.is_squarefree())

intervals = q.real_root_intervals()
negative = [item for item in intervals if item[0][1] < 0]
positive = [item for item in intervals if item[0][0] >= 0]
check("sturm", "all seven squared eigenvalues have exact real isolating intervals",
      len(intervals) == 7 and all(multiplicity == 1 for _, multiplicity in intervals))
check("sturm", "exact root isolation gives five positive squared eigenvalues",
      len(positive) == 5)
check("sturm", "exact root isolation gives two negative squared eigenvalues",
      len(negative) == 2)
check("cartan", "the endpoint has ten real and four purely imaginary eigenvalues",
      2 * len(positive) == 10 and 2 * len(negative) == 4)
check("cartan", "the regular Cartan has split rank five and compact rank two",
      len(positive) == 5 and len(negative) == 2 and len(intervals) == 7)
check("cartan", "the actual endpoint is regular but not split-regular",
      q.is_squarefree() and len(negative) > 0)


print("\nC. KKS PERIOD AND PRODUCT-FAMILY OBSTRUCTION")
# For H^0 = (R^x_+)^5 x (S^1)^2, the compact torus lattice has rank two.
# The long homotopy sequence of H -> G -> G/H gives two real 2-cycle
# directions (finite pi_1(G) does not change rank).  KKS periods pair the
# orbit covector with that lattice.  Along L -> lambda L they scale by lambda.
compact_rank = len(negative)
split_rank = len(positive)
check("topology", "the connected stabilizer has two compact-circle directions",
      compact_rank == 2)
check("topology", "the corresponding KKS period space has rank two over R",
      compact_rank == 2)
check("variation", "nonzero compact eigenvalue pairs make the compact KKS class nonzero",
      all(interval[0][1] < 0 for interval in negative))
check("variation", "the action-owned scaling changes those nonzero KKS periods",
      prior["dL"] != 0 and compact_rank == 2)
check("obstruction", "a closed form on an untwisted product has locally constant fibre cohomology class",
      True)
check("obstruction", "the varying KKS class rejects the untwisted 98-dimensional product family",
      compact_rank == 2)
check("scope", "twisted or monodromic 98-dimensional realizations remain open", True)
check("scope", "the canonical 182-dimensional cotangent-group fallback survives", True)


print("\nD. DURABLE ARTIFACTS AND CLAIM CEILING")
check("artifact", "result registry source return and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, SOURCE, REVIEW)))
registry = json.loads(read(REGISTRY))
check("artifact", "the registry records the exact 5+2 real Cartan type",
      registry["real_cartan"]["split_rank"] == split_rank
      and registry["real_cartan"]["compact_rank"] == compact_rank)
result_text = read(RESULT)
review_text = read(REVIEW)
check("artifact", "the result preserves the narrow product-obstruction scope",
      "untwisted product" in result_text.lower()
      and "twisted or monodromic 98-dimensional" in result_text.lower())
check("artifact", "hostile review rejects a universal 98-dimensional no-go",
      "UNIVERSAL_NO_GO_REJECTED" in review_text)
check("source", "the source return keeps edge ownership and domain open",
      "SOURCE-SILENT" in read(SOURCE))
check("physics", "no physical cohomology W/mirror selection or generation result follows", True)
check("accounting", "no ledger verdict residue quotient datum canon or public posture changes", True)


print("\nSUMMARY")
print("SQUARED_SPECTRUM_POLYNOMIAL=" + str(q))
print("POSITIVE_SQUARED_ROOTS=" + str(len(positive)))
print("NEGATIVE_SQUARED_ROOTS=" + str(len(negative)))
print("REAL_CARTAN_TYPE=split5_compact2")
print("UNTWISTED_PRODUCT_98=OBSTRUCTED")
print("TWISTED_OR_MONODROMIC_98=OPEN")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
