#!/usr/bin/env python3
"""Independent high-precision point control and hostile manifest mutations."""
from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
import importlib.util
import itertools
import math
from pathlib import Path

from flint import arb, ctx
import mpmath as mp


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("k202", HERE / "k202_order_six_common_weighted_core.py")
k202 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k202)
ctx.dps = 100
ctx.threads = 1
mp.mp.dps = 90


def mp_det(matrix):
    size = len(matrix)
    return sum(((-1) ** sum(p[i] > p[j] for i in range(size)
                              for j in range(i + 1, size))
                * math.prod(matrix[i][p[i]] for i in range(size))
                for p in itertools.permutations(range(size))), mp.mpf(0))


def independent_values(k184):
    rho = Q(3, 128)
    primitive = rho / 14
    tails = {i: (8 - i) * primitive for i in range(1, 8)}
    cache = {}

    def k1(arg):
        if arg not in cache:
            cache[arg] = 2 * mp.besselk(1, mp.mpf(arg.numerator) / arg.denominator)
        return cache[arg]

    node_factor = (mp.mpf(3) / 128) ** 8 / (2 * mp.pi) ** 8
    node_factor *= (mp.mpf(1) / 14) ** (mp.mpf(28) / 3)
    Z = mp.gamma(mp.mpf(1) / 3) ** 14 / mp.gamma(mp.mpf(14) / 3)
    Z *= mp.mpf(120) / 256 ** 6
    groups = defaultdict(lambda: mp.mpf(0))
    for entry in k184["andreief_time_gram_certificate"]["gram_entries"]:
        value = entry["coefficient_product"] * k1(tails[entry["left_old_position"]])
        value *= k1(tails[entry["right_old_position"]])
        for species in entry["species_kernels"]:
            matrix = [[k1(tails[i] + tails[j])
                       for j in species["right_time_positions"]]
                      for i in species["left_time_positions"]]
            value *= mp_det(matrix)
        groups[entry["group_id"]] += (1 if entry["left"] == entry["right"] else 2) * value
    return {key: Z * node_factor * value for key, value in groups.items()}


def rejects(k184, k185, mutation):
    a, b = deepcopy(k184), deepcopy(k185)
    mutation(a, b)
    try:
        k202.validate(a, b)
    except (AssertionError, KeyError, ValueError):
        return True
    return False


def main():
    a, b = k202.load()
    generated = k202.generate()
    independent = independent_values(a)
    assert set(independent) == set(generated["groups"])
    for key, value in independent.items():
        direct = arb(mp.nstr(value, 85))
        accepted = arb(generated["groups"][key]["one_node_value_arb"])
        assert (direct - accepted).abs_upper() < arb("1e-70"), key
    E = k202.proof_safe_per_support_term()
    Z = arb(generated["rule"]["normalizer_arb"])
    assert Z / arb.pi() ** 8 < arb(str(E.numerator)) / E.denominator

    mutations = [
        lambda x, y: y["complete_face_hypergraph"]["entries"].pop(),
        lambda x, y: y["complete_face_hypergraph"]["entries"][0]["terms"][0].__setitem__("leibniz_sign", -1),
        lambda x, y: y["complete_face_hypergraph"]["entries"][0].__setitem__("coefficient_product", -1),
        lambda x, y: next(iter(y["exact_allocation_certificate"]["allocation_catalog"].values()), {}).__setitem__("loads", "1/2," * 13 + "1/2"),
        lambda x, y: x["andreief_time_gram_certificate"]["gram_entries"][0]["species_kernels"].pop(),
    ]
    assert all(rejects(a, b, change) for change in mutations)
    print("[PASS] 18 independently evaluated mpmath signed-group controls")
    print("[PASS] exact outward ceiling contains the common-rule normalizer")
    print("[PASS] 5/5 planted mapping/sign/allocation mutations rejected")


if __name__ == "__main__":
    main()
