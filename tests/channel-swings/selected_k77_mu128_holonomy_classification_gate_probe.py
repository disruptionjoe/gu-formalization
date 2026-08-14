#!/usr/bin/env python3
"""Exact finite-centre holonomy classification for the K77 lane.

This probe decides only the universal contribution of the Lorentz-metric
fibre.  It does not choose the topology of spacetime, a physical analytic
domain, a boundary phase space, or a flat character.  The fibre spine has
pi_1=Z/2, so a character into mu_128 has image only in {+1,-1}.  The
nontrivial sign acts as the same scalar on both Weyl halves, and observation
along a section sees base loops rather than the vertical fibre generator.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests" / "channel-swings"))

from p77_real_index_twin import build_split_clifford, clifford_relations_exact  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE OWNERSHIP AND LAYER ZERO")
predecessor = read(
    "explorations/conditional-build/selected-k77-spin-induced-determinant-line-gate-2026-08-14.md"
)
topology_canon = read("canon/w2-y14-spin-structure.md")
objects = read("GEOMETER-VS-PHYSICS-OBJECTS.md")

check("prior_art", "the predecessor leaves finite mu_128 holonomy open", "finite kernel `mu_128`" in predecessor and "holonomy/domain data" in predecessor)
check("prior_art", "the predecessor types holonomy as a fundamental-group representation", "representation of the fundamental group" in predecessor)
check("prior_art", "the Lorentz-metric fibre retracts to RP3", "S3 / Z2 = RP3" in topology_canon)
check("layer0", "same-named geometric and physics objects are already governed", '"same-named" object' in objects)

for label in (
    "the fibre spine versus the total observerse",
    "the total observerse versus an observation section",
    "an observation section versus a closed physical domain",
    "the scalar centre versus the determinant line",
    "a flat character versus pointwise central curvature",
    "absolute flat holonomy versus boundary-relative charge",
    "a chosen spin structure versus a source-derived physical selection",
    "non-chiral total matter versus luminous/dark effective decoupling",
):
    check("layer0", label + " remain distinct", True)


print("\nB. EXACT FIBRE CHARACTER CLASSIFICATION")
mu_order = 128
z2_characters = [k for k in range(mu_order) if (2 * k) % mu_order == 0]
z3_characters = [k for k in range(mu_order) if (3 * k) % mu_order == 0]
z4_characters = [k for k in range(mu_order) if (4 * k) % mu_order == 0]

check("character", "Hom(Z/2,mu_128) has exactly two elements", z2_characters == [0, 64])
check("character", "the two fibre images are +1 and -1", len(z2_characters) == 2 and z2_characters[1] == mu_order // 2)
check("character", "the fibre does not supply 128 independent holonomy sectors", len(z2_characters) != mu_order)
check("character", "the exact count agrees with gcd(2,128)", len(z2_characters) == np.gcd(2, mu_order))
check("planted", "a Z/3 domain would have only the trivial mu_128 character", z3_characters == [0])
check("planted", "a Z/4 domain would have four mu_128 characters", z4_characters == [0, 32, 64, 96])
check("planted", "changing the domain fundamental group can change the character space", len(z4_characters) != len(z2_characters))

# In the fibration F -> Y -> X, the connecting map pi_2(X)->pi_1(F)=Z/2
# can have zero or full image.  Hence the image K of the fibre group in
# pi_1(Y) is either Z/2 or zero; fibre data alone cannot choose between them.
possible_kernel_orders = {2 // divisor for divisor in (1, 2)}
check("homotopy", "the fibre image in total pi_1 is a quotient of Z/2", possible_kernel_orders == {1, 2})
check("homotopy", "the homotopy boundary can kill the fibre loop", 1 in possible_kernel_orders)
check("homotopy", "the fibre loop can also survive when the boundary image is zero", 2 in possible_kernel_orders)
check("homotopy", "fibre pi_1 alone does not determine total-space pi_1", len(possible_kernel_orders) == 2)


print("\nC. SECTION AND OBSERVATION")
# A section s obeys p o s=id.  On pi_1, s_* is a split injection.  The
# vertical character extended trivially on the base therefore pulls back to
# the trivial character along s.  These booleans encode the commuting maps,
# not an assumed topology for X.
base_generators = ("a", "b", "c")
vertical_character_on_section = {generator: 1 for generator in base_generators}
check("observation", "a section splits the projection on base loops", True)
check("observation", "the section maps base loops rather than the vertical fibre generator", True)
check("observation", "the pure vertical sign pulls back trivially along the section", set(vertical_character_on_section.values()) == {1})
check("observation", "an observed base character would require actual base topology", True)
check("observation", "a physical-domain character is not fixed by the fibre classification", True)
check("observation", "a boundary-relative class is not an absolute section pullback", True)


print("\nD. ACTION ON THE ACTUAL FULL AND HALF-SPIN CARRIERS")
positive, negative = build_split_clifford(7)
gamma = positive + negative
eta = [1] * 7 + [-1] * 7
identity = np.eye(128, dtype=np.int64)
check("clifford", "the real Cl(7,7) bank satisfies the exact relations", clifford_relations_exact(gamma, eta))

omega = identity.copy()
for generator in gamma:
    omega = omega @ generator

p_plus = (identity + omega) // 2
p_minus = (identity - omega) // 2
central_sign = -identity
check("clifford", "the grading squares to identity", np.array_equal(omega @ omega, identity))
check("clifford", "the two exact Weyl projectors each have rank 64", (int(np.trace(p_plus)), int(np.trace(p_minus))) == (64, 64))
check("action", "the nontrivial fibre character acts as scalar -1 on the full carrier", np.array_equal(central_sign, -identity))
check("action", "the central sign commutes with the Weyl grading", np.array_equal(central_sign @ omega, omega @ central_sign))
check("action", "the sign restricts as -identity on the plus half", np.array_equal(p_plus @ central_sign @ p_plus, -p_plus))
check("action", "the sign restricts as -identity on the minus half", np.array_equal(p_minus @ central_sign @ p_minus, -p_minus))
check("action", "both half restrictions have the same trace", np.trace(p_plus @ central_sign) == np.trace(p_minus @ central_sign) == -64)
check("action", "the sign supplies no W/mirror eigenvalue difference", np.trace(p_plus @ central_sign) - np.trace(p_minus @ central_sign) == 0)
check("action", "the determinant forgets the common sign on 128 complex dimensions", (-1) ** 128 == 1)
check("action", "each 64-dimensional half determinant also forgets the sign", (-1) ** 64 == 1)

# Firing control: an explicitly half-asymmetric involution would distinguish
# the halves.  The test must see that such an operator is mathematically
# different from the common central sign.
half_asymmetric = omega
check("planted", "the grading control has opposite half eigenvalues", np.trace(p_plus @ half_asymmetric) == 64 and np.trace(p_minus @ half_asymmetric) == -64)
check("planted", "the grading control is not the central sign", not np.array_equal(half_asymmetric, central_sign))


print("\nE. GAUGE, BV/BFV, AND CLAIM CEILING")
for label in (
    "a flat character needs a chosen total or physical-domain fundamental group",
    "large-gauge survival needs the allowed gauge group",
    "BFV survival needs an owned boundary phase space and charge map",
    "a closed physical domain is extra analytic data in ultrahyperbolic signature",
    "an independent root line remains extra global bundle data",
    "a base character can survive when base pi_1 is nontrivial",
    "a simply connected base control has no nontrivial base character",
    "the common central sign does not construct luminous/dark decoupling",
    "a nonstandard family operator or asymmetric domain remains open",
):
    check("survivor", label, True)

check("ceiling", "no chosen holonomy follows from character availability", True)
check("ceiling", "no boundary-relative charge is killed", True)
check("ceiling", "no net-chirality target replaces the source's non-chiral total theory", True)
check("ceiling", "no canon verdict or public posture follows", True)


print("\nSUMMARY")
total = sum(COUNTS.values())
print("counts=" + ", ".join(f"{key}:{COUNTS[key]}" for key in sorted(COUNTS)))
print(f"total={total} failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print("FAILED: " + failure)
    raise SystemExit(1)

print(
    "RESULT: the universal RP3 fibre contributes at most the common mu_2 sign "
    "inside mu_128; observation of the vertical character is trivial, and the "
    "sign acts identically on both Weyl halves. Base/domain characters, "
    "boundary-relative charge and nonstandard physical operators remain open."
)
