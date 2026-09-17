#!/usr/bin/env python3
"""Independent rational K209 replay; deliberately does not import the producer."""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction as F
import hashlib
import itertools
import json
from math import comb, factorial, prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
DATA = P / "k209-order-six-cubic-core-geometry.json"
K204 = P / "k204-order-six-core-moment-defect.json"
K208 = P / "k208-order-six-cubic-moment-rule.json"
PAIRS = tuple(itertools.combinations(range(14), 2))
NAMES = {(): "constant", (1,): "single", (2,): "square",
         (1, 1): "distinct_pair", (3,): "cube",
         (2, 1): "square_times_distinct", (1, 1, 1): "three_distinct"}
FOUR = {(4,): "four", (3, 1): "three_one", (2, 2): "two_two",
        (2, 1, 1): "two_one_one", (1, 1, 1, 1): "four_distinct"}


def source(indices):
    degrees = [indices.count(i) for i in range(14)]
    top = prod((prod((F(1, 3)+j for j in range(p)), start=F(1))
                for p in degrees), start=F(1))
    bottom = prod((F(14, 3)+j for j in range(len(indices))), start=F(1))
    return top/bottom


def finite(indices):
    # Sum pair intersections by support exponents, without constructing nodes.
    power = len(indices)
    pair_sum = sum(19**sum(indices.count(i) for i in pair) for pair in PAIRS)
    return F(2891, 11016)*F(1, 14)**power + F(625, 77112)*F(pair_sum, 50**power)


def q_tail(shape):
    return F(3, 8)**64 * sum((F(64**j, factorial(j)) for j in range(shape)), F(0))


def check(data):
    assert data["input_sha256"] == {
        "K204": hashlib.sha256(K204.read_bytes()).hexdigest(),
        "K208": hashlib.sha256(K208.read_bytes()).hexdigest()}
    old = json.loads(K204.read_text())
    cubic = json.loads(K208.read_text())
    face = F(old["face_union_probability_upper_rational"])
    lost = face + q_tail(6)
    assert F(data["lost_mass_upper"]) == lost < 1
    assert data["all_184_nodes_inside"] is True
    assert F(1, 50) > F(1, 2**180)
    assert (7+3) < 64  # sqrt(7)<3, so the upper radial node < 1/4.
    assert len(data["cubic_orbit_representatives"]) == 28
    for a in range(4):
        radial = F(factorial(5+a), factorial(5)*256**a)
        for pattern, name in NAMES.items():
            indices = tuple(i for i, p in enumerate(pattern) for _ in range(p))
            m = radial*source(indices)
            assert finite(indices) == source(indices)
            bound = radial*face + m*q_tail(6+a)
            conditional = (bound+m*lost)/(1-lost)
            if (a, pattern) == (0, ()):
                conditional = F(0)
            row = data["cubic_orbit_representatives"][f"rho^{a}:{name}"]
            assert tuple(F(row[k]) for k in (
                "full_reference_and_rule_moment", "discarded_unnormalized_upper",
                "conditional_core_vs_rule_upper")) == (m, bound, conditional), (a, name)
    # All 680 distinct multiindices, not only the seven orbit representatives.
    total = 0
    for degree in range(4):
        for indices in itertools.combinations_with_replacement(range(14), degree):
            assert finite(indices) == source(indices)
            total += 1
    assert total == comb(17, 3) == 680
    assert len(data["quartic_angular_representatives"]) == 5
    for pattern, name in FOUR.items():
        indices = tuple(i for i, p in enumerate(pattern) for _ in range(p))
        row = data["quartic_angular_representatives"][name]
        assert (F(row["reference"]), F(row["rule"]),
                F(row["rule_minus_reference"])) == (
                    source(indices), finite(indices), finite(indices)-source(indices))
    def norm4(moment):
        return (14*moment((0, 0, 0, 0))
                + 14*13*moment((0, 0, 1, 1))
                - 2*moment((0, 0)) + F(1, 14**2))
    expected, actual = norm4(source), norm4(finite)
    assert F(data["centered_euclidean_fourth_reference"]) == expected > 0
    assert F(data["centered_euclidean_fourth_rule"]) == actual > 0
    assert F(data["centered_fourth_rule_minus_reference"]) == actual-expected
    assert F(data["conditional_core_fourth_upper"]) == expected/(1-lost)
    assert F(data["conditional_taylor_remainder_coefficient_upper"]) == (
        expected/(1-lost)+actual)/24
    assert data["unchanged_full_domain_error_rational"] == cubic[
        "all_group_absolute_error_ceiling_rational"]


def hostile(original):
    mutations = []
    for path, bad in (("lost_mass_upper", "0"),
                      ("centered_euclidean_fourth_rule", "0"),
                      ("conditional_taylor_remainder_coefficient_upper", "0"),
                      ("unchanged_full_domain_error_rational", "0")):
        changed = deepcopy(original)
        changed[path] = bad
        mutations.append(changed)
    changed = deepcopy(original)
    changed["cubic_orbit_representatives"]["rho^2:cube"]["conditional_core_vs_rule_upper"] = "0"
    mutations.append(changed)
    changed = deepcopy(original)
    changed["quartic_angular_representatives"]["two_two"]["rule_minus_reference"] = "0"
    mutations.append(changed)
    for changed in mutations:
        try:
            check(changed)
        except AssertionError:
            continue
        raise AssertionError("hostile mutation escaped")
    return len(mutations)


if __name__ == "__main__":
    data = json.loads(DATA.read_text())
    check(data)
    print("[PASS] independent 680-monomial enumeration and 28 core rows")
    print("[PASS] independent quartic geometry; hostile mutations", hostile(data))
