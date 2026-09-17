#!/usr/bin/env python3
"""K209: exact K208 compact-reference defects and fourth-order geometry."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
K204 = P / "k204-order-six-core-moment-defect.json"
K208 = P / "k208-order-six-cubic-moment-rule.json"
OUT = P / "k209-order-six-cubic-core-geometry.json"
N = 14
PAIRS = tuple(itertools.combinations(range(N), 2))
W_PAIR = F(8125, 11016) / len(PAIRS)
W_CENTER = F(2891, 11016)
PATTERNS = {
    "constant": (), "single": (1,), "square": (2,), "distinct_pair": (1, 1),
    "cube": (3,), "square_times_distinct": (2, 1),
    "three_distinct": (1, 1, 1),
}
QUARTIC = {"four": (4,), "three_one": (3, 1), "two_two": (2, 2),
           "two_one_one": (2, 1, 1), "four_distinct": (1, 1, 1, 1)}


def rising(x: F, n: int) -> F:
    return math.prod((x + k for k in range(n)), start=F(1))


def reference(pattern: tuple[int, ...]) -> F:
    return math.prod((rising(F(1, 3), p) for p in pattern), start=F(1)) / rising(
        F(14, 3), sum(pattern))


def angular_nodes():
    yield (F(1, N),) * N, W_CENTER
    for pair in PAIRS:
        yield tuple(F(19, 50) if i in pair else F(1, 50) for i in range(N)), W_PAIR


def rule(pattern: tuple[int, ...]) -> F:
    return sum((w * math.prod((z[i]**p for i, p in enumerate(pattern)), start=F(1))
                for z, w in angular_nodes()), start=F(0))


def generate() -> dict:
    old = json.loads(K204.read_text())
    cubic = json.loads(K208.read_text())
    assert cubic["counts"]["angular_nodes"] == 92
    assert sum((w for _, w in angular_nodes()), F(0)) == 1
    assert all(min(z) >= F(1, 50) > F(1, 2**180) for z, _ in angular_nodes())
    face = F(old["face_union_probability_upper_rational"])
    lost = F(old["lost_reference_probability_upper_rational"])
    rows = {}
    for a in range(4):
        radial = rising(F(6), a) / 256**a
        tail = F(3, 8)**64 * sum((F(64**k, math.factorial(k))
                                  for k in range(6+a)), start=F(0))
        for name, pattern in PATTERNS.items():
            assert rule(pattern) == reference(pattern)
            full = radial * reference(pattern)
            deletion = radial * face + full * tail
            conditional = (deletion + full * lost) / (1-lost)
            if a == 0 and not pattern:
                conditional = F(0)
            rows[f"rho^{a}:{name}"] = {
                "full_reference_and_rule_moment": str(full),
                "discarded_unnormalized_upper": str(deletion),
                "conditional_core_vs_rule_upper": str(conditional),
            }
            if sum(pattern) <= 2:
                name204 = {"constant": "constant", "single": "single_coordinate",
                           "square": "coordinate_square", "distinct_pair": "distinct_pair"}[name]
                assert old["monomial_orbit_representatives"][f"rho^{a}:{name204}"][
                    "conditional_core_vs_full_rule_upper"] == str(conditional)
    quartic = {name: {"reference": str(reference(pattern)),
                      "rule": str(rule(pattern)),
                      "rule_minus_reference": str(rule(pattern)-reference(pattern))}
               for name, pattern in QUARTIC.items()}
    # S2 = ||z-c||_2^2 = sum z_i^2 - 1/14; permutation symmetry makes
    # S2^2 depend only on the square and two-two orbit representatives.
    def fourth(moment):
        return (N*moment((4,)) + N*(N-1)*moment((2, 2))
                - F(2, N)*N*moment((2,)) + F(1, N**2))
    full_fourth, rule_fourth = fourth(reference), fourth(rule)
    assert full_fourth > 0 and rule_fourth > 0
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {"K204": hashlib.sha256(K204.read_bytes()).hexdigest(),
                         "K208": hashlib.sha256(K208.read_bytes()).hexdigest()},
        "reference": "Gamma(6,256) x Dirichlet(1/3)^14",
        "core": old["core"], "all_184_nodes_inside": True,
        "lost_mass_upper": str(lost),
        "cubic_orbit_representatives": rows,
        "orbit_coverage": "7 angular partitions through degree three x 4 radial powers; 680 angular monomials x 4 = 2720 product monomials",
        "quartic_angular_representatives": quartic,
        "centered_euclidean_fourth_reference": str(full_fourth),
        "centered_euclidean_fourth_rule": str(rule_fourth),
        "centered_fourth_rule_minus_reference": str(rule_fourth-full_fourth),
        "conditional_core_fourth_upper": str(full_fourth/(1-lost)),
        "conditional_taylor_remainder_coefficient_upper": str(
            (full_fourth/(1-lost)+rule_fourth)/24),
        "taylor_scope": "For an angular f with Euclidean operator norm of D^4 f <= M on the convex core, the difference of the two cubic Taylor remainders about c=(1/14)^14 is <= M times conditional_taylor_remainder_coefficient_upper. Separately retain the conditional-core versus full-rule polynomial moment defects above, including all radial cross moments. This is not a bound on D^4 f or on the signed K184 quotient.",
        "unchanged_full_domain_error_rational": cubic["all_group_absolute_error_ceiling_rational"],
        "remaining_gate": "Enclose complete signed K184 normalized/coalescent fourth angular and mixed derivatives on core cells; compose Duffy/Jacobi chain, separate K185/K188 termwise quotient boundaries, and allocate coherent-group error before an accurate prefix.",
        "claim_ceiling": "exact rational common-reference cubic core defects and conditional fourth-order geometry only; no complete signed quotient error, accurate order-six prefix or physical/source result",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] 28 cubic core orbit rows; 2720 product monomials covered")
    print("[PASS] five quartic orbits and conditional fourth-order geometry")
