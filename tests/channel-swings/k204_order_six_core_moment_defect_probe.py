#!/usr/bin/env python3
"""Independent K204 rational/analytic replay and hostile cutoff controls."""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path

from mpmath import mp

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "lab/process/k204-order-six-core-moment-defect.json"
SOURCE = ROOT / "lab/process/k203-order-six-positive-moment-rule.json"


def product(values):
    value = F(1)
    for x in values:
        value *= x
    return value


def pochhammer(x, n):
    return product(x + j for j in range(n))


def q_upper(n):
    # Reconstructed from the integer-shape incomplete Gamma formula.
    return F(3**64, 8**64) * sum((F(64**j, factorial(j)) for j in range(n)), F(0))


def validate(data):
    assert data["input_sha256"]["K203"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert data["core"] == {"radial_upper": "1/4",
                            "angular_coordinate_lower": "1/2^180",
                            "all_28_rule_nodes_strictly_inside": True}
    delta = mp.power(2, -180)
    radial_cut = mp.mpf(1) / 4
    theta = mp.sqrt(mp.mpf(3) / 17)
    for r in (7 - mp.sqrt(7), 7 + mp.sqrt(7)):
        rho = r / 256
        for k in range(14):
            z = [(1 - theta) / 14 + (theta if j == k else 0)
                 for j in range(14)]
            assert 0 < rho < radial_cut and min(z) > delta
            assert abs(sum(z) - 1) < mp.mpf("1e-85")
    face = F(448, 2**60)
    radial = q_upper(6)
    lost = face + radial
    assert F(data["face_union_probability_upper_rational"]) == face
    assert F(data["radial_tail_probability_upper_rational"]) == radial
    assert F(data["lost_reference_probability_upper_rational"]) == lost < 1
    # The actual one-face beta probability and radial Gamma tail are
    # independent special-function controls, not inputs to the rational proof.
    beta_face = mp.betainc(mp.mpf(1) / 3, mp.mpf(13) / 3,
                           0, delta, regularized=True)
    true_tail = mp.gammainc(6, 64, mp.inf, regularized=True)
    assert 14 * beta_face < mp.mpf(face.numerator) / face.denominator
    assert true_tail < mp.mpf(radial.numerator) / radial.denominator

    angular = {"constant": (), "single_coordinate": (1,),
               "coordinate_square": (2,), "distinct_pair": (1, 1)}
    rows = data["monomial_orbit_representatives"]
    assert len(rows) == 16
    for a in range(4):
        mu_r = F(factorial(5 + a), factorial(5) * 256**a)
        for name, powers in angular.items():
            key = f"rho^{a}:{name}"
            ang = product(pochhammer(F(1, 3), b) for b in powers)
            ang /= pochhammer(F(14, 3), sum(powers))
            m = mu_r * ang
            discarded = mu_r * face + m * q_upper(6 + a)
            conditional = (discarded + m * lost) / (1 - lost)
            if a == 0 and not powers:
                conditional = F(0)
            assert F(rows[key]["full_reference_moment"]) == m
            assert F(rows[key]["discarded_unnormalized_moment_upper"]) == discarded
            assert F(rows[key]["conditional_core_vs_full_rule_upper"]) == conditional
            # The exact radial incomplete moment agrees and is enclosed.
            tail_a = mp.gammainc(6 + a, 64, mp.inf, regularized=True)
            assert tail_a < mp.mpf(q_upper(6 + a).numerator) / q_upper(6 + a).denominator
    previous = json.loads(SOURCE.read_text())
    assert data["unchanged_full_domain_error_rational"] == previous[
        "all_group_absolute_error_ceiling_rational"]
    return True


def hostile(data):
    mutations = []
    a = deepcopy(data)
    a["face_union_probability_upper_rational"] = str(F(a["face_union_probability_upper_rational"]) / 2)
    mutations.append(a)
    a = deepcopy(data)
    a["radial_tail_probability_upper_rational"] = str(F(a["radial_tail_probability_upper_rational"]) / 2)
    mutations.append(a)
    a = deepcopy(data)
    a["core"]["radial_upper"] = "1/32"  # excludes the upper radial node
    mutations.append(a)
    a = deepcopy(data)
    a["monomial_orbit_representatives"]["rho^2:distinct_pair"]["conditional_core_vs_full_rule_upper"] = "0"
    mutations.append(a)
    a = deepcopy(data)
    a["unchanged_full_domain_error_rational"] = "0"
    mutations.append(a)
    caught = 0
    for mutation in mutations:
        try:
            validate(mutation)
        except AssertionError:
            caught += 1
    assert caught == len(mutations)
    return caught


if __name__ == "__main__":
    mp.dps = 90
    artifact = json.loads(DATA.read_text())
    assert validate(artifact)
    caught = hostile(artifact)
    print("[PASS] independent rational moments, beta/gamma controls, 28 core nodes")
    print(f"[PASS] hostile cutoff, mass, defect and error plants {caught}/{caught}")
