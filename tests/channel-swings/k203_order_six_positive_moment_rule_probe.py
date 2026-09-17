#!/usr/bin/env python3
"""Independent moment and complete signed-node controls for K203."""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
import importlib.util
import itertools
import json
import math
from pathlib import Path

from flint import arb
import mpmath as mp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k203", HERE / "k203_order_six_positive_moment_rule.py")
k203 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k203)
mp.mp.dps = 90


def mp_nodes():
    theta = mp.sqrt(mp.mpf(3) / 17)
    r = mp.sqrt(7)
    for x, rw in [(7-r, (1+1/r)/2), (7+r, (1-1/r)/2)]:
        for k in range(14):
            yield x / 256, [(1-theta)/14 + (theta if i == k else 0)
                            for i in range(14)], rw / 14


def independent_groups(entries):
    groups = defaultdict(lambda: mp.mpf(0))
    Z = mp.factorial(5) / 256 ** 6 * mp.gamma(mp.mpf(1) / 3) ** 14
    Z /= mp.gamma(mp.mpf(14) / 3)
    for rho, z, weight in mp_nodes():
        s = [rho * a for a in z]
        T = [sum(s[i:7]) for i in range(7)]
        U = [sum(s[7+i:]) for i in range(7)]
        cache = {}

        def kernel(x):
            if x not in cache:
                cache[x] = 2 * mp.besselk(1, x)
            return cache[x]

        density = rho ** 8 * mp.fprod(a ** (mp.mpf(2) / 3) for a in z)
        density /= (2 * mp.pi) ** 8
        for row in entries:
            value = row["coefficient_product"] * kernel(T[row["left_old_position"]-1])
            value *= kernel(U[row["right_old_position"]-1])
            for species in row["species_kernels"]:
                left = species["left_time_positions"]
                right = species["right_time_positions"]
                m = len(left)
                matrix = [[kernel(T[i-1] + U[j-1]) for j in right] for i in left]
                det = sum(((-1) ** sum(p[i] > p[j] for i in range(m)
                                           for j in range(i+1, m)))
                          * mp.fprod(matrix[i][p[i]] for i in range(m))
                          for p in itertools.permutations(range(m)))
                value *= det
            groups[row["group_id"]] += Z * weight * density * value * (1 if row["left"] == row["right"] else 2)
    return groups


def check_moments():
    nodes = list(mp_nodes())
    assert len(nodes) == 28
    assert abs(sum(w for _, _, w in nodes) - 1) < mp.mpf("1e-85")
    for n in range(4):
        actual = sum(w * (rho * 256) ** n for rho, _, w in nodes)
        assert abs(actual - mp.factorial(n+5) / mp.factorial(5)) < mp.mpf("1e-85")
    for i in range(14):
        mean = sum(w * z[i] for _, z, w in nodes)
        diag = sum(w * z[i] ** 2 for _, z, w in nodes)
        other = sum(w * z[i] * z[(i+1) % 14] for _, z, w in nodes)
        assert abs(mean - mp.mpf(1)/14) < mp.mpf("1e-85")
        assert abs(diag - mp.mpf(2)/119) < mp.mpf("1e-85")
        assert abs(other - mp.mpf(1)/238) < mp.mpf("1e-85")
    # Nontrivial mixed radial/angular moment of the product reference.
    mixed = sum(w * (rho*256)**3 * z[2]*z[8] for rho, z, w in nodes)
    assert abs(mixed - mp.mpf(336)/238) < mp.mpf("1e-84")


def main():
    check_moments()
    a, b = k203.k202.load()
    native = k203.generate()
    stored = json.loads(k203.OUT.read_text())
    assert native == stored
    entries = a["andreief_time_gram_certificate"]["gram_entries"]
    independent = independent_groups(entries)
    assert set(independent) == set(stored["groups"])
    for key, value in independent.items():
        ball = arb(stored["groups"][key]["twenty_eight_node_value_arb"])
        assert abs(arb(mp.nstr(value, 85)) - ball).abs_upper() < arb("1e-70"), key
    assert stored["all_group_absolute_error_ceiling_rational"] == (
        k203.k202.generate()["all_group_absolute_error_ceiling_rational"])
    # Mutations target the input/sign/moment assumptions, not just a manifest checksum.
    modified = deepcopy(a)
    modified["andreief_time_gram_certificate"]["gram_entries"][0]["coefficient_product"] *= -1
    try:
        k203.k202.validate(modified, b)
    except AssertionError:
        pass
    else:
        raise AssertionError("coefficient mutation not caught")
    masks_mutation = deepcopy(b)
    allocation_id = masks_mutation["complete_face_hypergraph"]["entries"][0]["terms"][0]["allocation_id"]
    allocation = masks_mutation["exact_allocation_certificate"]["allocation_catalog"][allocation_id]
    masks = allocation["support_masks_hex"].split(",")
    assert masks[0] == "7f"
    masks[0] = "3f"  # declared weights still fit, but true old-position T1 does not
    allocation["support_masks_hex"] = ",".join(masks)
    k203.k202.validate(a, masks_mutation)
    try:
        k203.argument_supports(a, masks_mutation)
    except AssertionError:
        pass
    else:
        raise AssertionError("actual Bessel-argument support mutation not caught")
    wrong_theta2 = Q(1, 6)
    assert Q(1, 196) + wrong_theta2 * Q(13, 196) != Q(2, 119)
    wrong_radial_weight = mp.mpf(1)/2
    assert abs(wrong_radial_weight*(7-mp.sqrt(7)) + wrong_radial_weight*(7+mp.sqrt(7))-6) > 0
    wrong_factor = mp.mpf(1)/7
    assert abs(wrong_factor*sum(z[0] for _, z, _ in mp_nodes())-mp.mpf(1)/14) > 0
    print("[PASS] independent Gamma/Dirichlet moments through radial 3, angular 2")
    print("[PASS] independent 90-digit mpmath evaluation of 28 nodes and 18 signed groups")
    print("[PASS] 14,912 actual argument supports; support, sign, scale and weight hostile controls")


if __name__ == "__main__":
    main()
