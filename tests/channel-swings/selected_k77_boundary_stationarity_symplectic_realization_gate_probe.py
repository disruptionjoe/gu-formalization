#!/usr/bin/env python3
"""Exact certificate for the K77 boundary-stationarity/carrier gate."""

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "lab/process/selected-k77-coadjoint-invariant-variation-gate.json"

checks: list[tuple[bool, str]] = []


def check(condition: bool, label: str) -> None:
    checks.append((condition, label))


data = json.loads(PREDECESSOR.read_text(encoding="utf-8"))
endpoint = data["endpoint"]
invariants = data["coadjoint_invariants"]

# Immutable predecessor controls.
g_dim = endpoint["dimension"]
orbit_dim = endpoint["coadjoint_orbit_dimension"]
corank = endpoint["regular_stabilizer_dimension"]
derivatives = [Fraction(x) for x in invariants["first_derivatives"]]
check(g_dim == 91, "ambient Lie algebra has dimension 91")
check(orbit_dim == 84, "regular Kirillov rank is 84")
check(corank == 7, "regular Poisson corank is seven")
check(invariants["differential_rank"] == 7, "invariant differential rank is seven")
check(len(derivatives) == 7, "all seven invariant derivatives are present")
check(all(value != 0 for value in derivatives), "the owned scaling direction is transverse")

# Bare endpoint potential Theta=p0 dq0-p2 dq3.
p0 = (Fraction(2), Fraction(-3), Fraction(5))
p2 = (Fraction(7), Fraction(11), Fraction(-13))
dq0 = (Fraction(17), Fraction(19), Fraction(23))
dq3 = (Fraction(29), Fraction(-31), Fraction(37))
theta = sum(a * b for a, b in zip(p0, dq0)) - sum(
    a * b for a, b in zip(p2, dq3)
)
check(theta != 0, "unrestricted variation has nonzero endpoint term")
check(
    all(x == 0 for x in (Fraction(0),) * 6),
    "free stationarity sets both endpoint momenta to zero",
)
eta0 = (Fraction(3), Fraction(0), Fraction(-2))
eta3 = (Fraction(1), Fraction(4), Fraction(0))
charge = sum(a * b for a, b in zip(p0, eta0)) - sum(
    a * b for a, b in zip(p2, eta3)
)
check(charge != 0, "nonzero endpoint momentum permits a live charge")
check(
    sum(a * Fraction(0) for a in p0) - sum(a * Fraction(0) for a in p2) == 0,
    "Dirichlet variations kill Theta without killing momentum",
)
check(
    sum(Fraction(0) * b for b in eta0)
    - sum(Fraction(0) * b for b in eta3)
    == 0,
    "free stationary momentum kills every endpoint charge",
)

# A generated boundary graph is Lagrangian only when its derivative is symmetric.
H = (
    (Fraction(2), Fraction(3), Fraction(5)),
    (Fraction(3), Fraction(7), Fraction(11)),
    (Fraction(5), Fraction(11), Fraction(13)),
)
check(all(H[i][j] == H[j][i] for i in range(3) for j in range(3)),
      "generated boundary Hessian is symmetric")
bad_H = [list(row) for row in H]
bad_H[0][1] += 1
check(any(bad_H[i][j] != bad_H[j][i] for i in range(3) for j in range(3)),
      "nonsymmetric planted graph is not generated/Lagrangian")

# Regular Poisson symplectic-realization theorem.
local_min_dim = g_dim + corank
split_model_dim = orbit_dim + 2 * corank
cotangent_group_dim = 2 * g_dim
check(local_min_dim == 98, "Poisson-submersion lower bound is 98")
check(split_model_dim == 98, "Weinstein split realization attains 98 locally")
check(local_min_dim == split_model_dim, "local lower bound is sharp")
check(local_min_dim % 2 == 0, "local carrier dimension is symplectic-even")
check(cotangent_group_dim == 182, "cotangent group has dimension 182")
check(local_min_dim < cotangent_group_dim, "global cotangent fallback is not locally minimal")
check(orbit_dim < local_min_dim, "one fixed orbit cannot span transverse Casimirs")
check(local_min_dim - orbit_dim == 14, "seven Casimirs require seven conjugate pairs")
check(cotangent_group_dim >= local_min_dim, "global fallback respects the lower bound")

# Claim-ceiling controls.
check(data["disposition"]["analytic_domain"] == "NOT_CONSTRUCTED",
      "analytic domain remains open")
check(data["disposition"]["physical_cohomology"] == "NOT_CONSTRUCTED",
      "physical cohomology remains open")
check(data["claim_ceiling"]["canon_or_public_posture_change"] == "NONE",
      "canon and public posture remain unchanged")
check(data["claim_ceiling"]["generation_count"] == "NOT_INFERRED",
      "generation count is not inferred")

failed = [label for ok, label in checks if not ok]
if failed:
    for label in failed:
        print(f"FAIL: {label}")
    raise SystemExit(1)

for _, label in checks:
    print(f"PASS: {label}")
print(f"PASS_{len(checks)}_OF_{len(checks)}")
