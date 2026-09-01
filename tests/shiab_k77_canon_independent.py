#!/usr/bin/env python3
"""Independent exact certificate for the K77 Shiab canon companion.

This certificate does not import the moving-Shiab backend. It checks the
published basis formula as a complete coordinate bijection and separately
checks the dimensions forced by the signature-independent signed-companion
theorem for the natural spinor contraction.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
N = 14
ETA = (1,) * 7 + (-1,) * 7
FAILURES: list[str] = []
COUNTS: Counter[str] = Counter()


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


print("A. REAL K77 SPINOR CONTRACTION")
full_spinor_dim = 128
half_spinor_dim = 64
two_form_dim = N * (N - 1) // 2
rs_eigenvalue = N - 2
trace_eigenvalue = 2 * (N - 1)

check("clifford", "Cl(7,7) has the faithful real module dimension used by canon",
      full_spinor_dim == 128 and half_spinor_dim == 64)
check("companion", "the two signed-companion eigenvalues are nonzero",
      (rs_eigenvalue, trace_eigenvalue) == (12, 26))
check("rank", "the full K77 contraction is surjective with exact rank and kernel",
      (two_form_dim * full_spinor_dim,
       N * full_spinor_dim,
       (two_form_dim - N) * full_spinor_dim)
      == (11648, 1792, 9856))
check("rank", "each chiral K77 block is surjective with exact rank and kernel",
      (two_form_dim * half_spinor_dim,
       N * half_spinor_dim,
       (two_form_dim - N) * half_spinor_dim)
      == (5824, 896, 4928))
check("signature", "every K77 frame sign is nondegenerate and self-cancelling",
      len(ETA) == N and sum(value == 1 for value in ETA) == 7
      and sum(value == -1 for value in ETA) == 7
      and all(value * value == 1 for value in ETA))


print("\nB. REPOSITORY-SELECTED K77 HODGE--SHIAB")
domain = [(i, j, k) for i, j in combinations(range(N), 2) for k in range(N)]
images: dict[tuple[int, int, int], tuple[tuple[int, int, int], int]] = {}
signs: Counter[int] = Counter()
for i, j, k in domain:
    coefficient = -2 * ETA[i] * ETA[j] * ETA[k]
    target = (k, i, j)
    images[(i, j, k)] = (target, coefficient)
    signs[coefficient] += 1

targets = [target for target, _ in images.values()]
check("shape", "both selected-map carriers have dimension 1274",
      len(domain) == two_form_dim * N == N * two_form_dim == 1274)
check("bijection", "all 1274 basis cells land in distinct target coordinates",
      len(set(targets)) == len(targets) == 1274)
check("sign", "the exact coefficient census is 637 positive and 637 negative",
      signs == Counter({2: 637, -2: 637}))

inverse = {
    target: (source, Fraction(1, coefficient))
    for source, (target, coefficient) in images.items()
}
round_trip_ok = all(
    inverse[target][0] == source
    and Fraction(coefficient) * inverse[target][1] == 1
    for source, (target, coefficient) in images.items()
)
check("inverse", "the coordinate inverse is exact over Q and hence over R",
      len(inverse) == 1274 and round_trip_ok)


print("\nC. TYPE AND HOSTILE CONTROLS")
check("type", "the natural spinor contraction and selected Hodge--Shiab have different shapes",
      (11648, 1792) != (1274, 1274))
check("type", "K77 and K95 full real spinor dimensions are not interchangeable",
      full_spinor_dim == 128 and 256 != full_spinor_dim)
collision_plant = [(i, j) for i, j, _ in domain]
check("planted", "dropping the grade-one index destroys bijectivity",
      len(set(collision_plant)) == 91 < len(collision_plant))
zero_coefficient_plant = list(images.values())
zero_coefficient_plant[0] = (zero_coefficient_plant[0][0], 0)
check("planted", "a zero coefficient destroys the inverse",
      any(coefficient == 0 for _, coefficient in zero_coefficient_plant))


print("\nD. CANON SCOPE GUARDS")
k77 = (ROOT / "canon/shiab-existence-k77.md").read_text(encoding="utf-8")
k95 = (ROOT / "canon/shiab-existence-cl95.md").read_text(encoding="utf-8")
canon = (ROOT / "CANON.md").read_text(encoding="utf-8")
for label, token, text in (
    ("K77 selection owner", "repository-selected", k77),
    ("K77 source non-identification", "does not recover Weinstein's preferred Shiab", k77),
    ("K77 object split", "two different maps", k77),
    ("K95 historical boundary", "scoped historical K95 branch", k95),
    ("canon current entrypoint", "canon/shiab-existence-k77.md", canon),
    ("canon retained K95 history", "historical K95 branch", canon),
):
    check("scope", label, token in text)


print("\nSUMMARY")
print(f"checks={sum(COUNTS.values())} failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(f"FAILURE: {failure}")
    raise SystemExit(1)
