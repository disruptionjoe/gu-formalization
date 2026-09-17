#!/usr/bin/env python3
"""Independent exact-monomial and K185 time-permutation controls for K208."""
from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUT = ROOT / "lab/process/k208-order-six-cubic-moment-rule.json"
spec = importlib.util.spec_from_file_location("k207probe", HERE / "k207_order_six_mixed_jets_probe.py")
k207 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k207)
mp.mp.dps = 78
N = 14


def exact_all_monomials():
    manifest = json.loads(OUT.read_text())
    w = Q(manifest["rule"]["center_weight"])
    each = Q(manifest["rule"]["each_pair_weight"])
    pairs = list(itertools.combinations(range(N), 2))
    assert len(pairs) == 91 and w + 91*each == 1
    seen = 0
    for degree in range(4):
        for indices in itertools.combinations_with_replacement(range(N), degree):
            actual = w*Q(1, N)**degree
            for pair in pairs:
                actual += each*math.prod(Q(19, 50) if i in pair else Q(1, 50)
                                         for i in indices)
            multiplicities = [indices.count(i) for i in range(N)]
            expected = math.prod(math.prod(Q(1, 3)+j for j in range(m))
                                 for m in multiplicities)
            expected /= math.prod(Q(14, 3)+j for j in range(degree))
            assert actual == expected, (indices, actual, expected)
            seen += 1
    assert seen == math.comb(N+3, 3) == 680
    # Independent radial Gamma moments from the old Gauss rule.
    root = mp.sqrt(7)
    radial = [((7-root)/256, (1+1/root)/2),
              ((7+root)/256, (1-1/root)/2)]
    for degree in range(4):
        expected = mp.mpf(math.prod(range(6, 6+degree)))/256**degree
        observed = sum(weight*rho**degree for rho, weight in radial)
        assert abs(observed-expected) < mp.mpf("1e-70")
    return manifest


def signed_point_control():
    """Use K185 permutations/masks, not K203's production determinants."""
    forms = k207.terms()
    for pair in ((0, 1), (6, 7)):
        z = [mp.mpf(19)/50 if i in pair else mp.mpf(1)/50 for i in range(N)]
        rho = (7-mp.sqrt(7))/256
        coefficient = rho**8*mp.fprod(zi**(mp.mpf(2)/3) for zi in z)/(2*mp.pi)**8
        cache = {}
        for _, _, masks in forms:
            for mask in masks:
                if mask not in cache:
                    s = sum(z[i] for i in range(N) if mask & (1 << i))
                    cache[mask] = 2*mp.besselk(1, rho*s)
        groups = {}
        for group, sign, masks in forms:
            groups[group] = groups.get(group, mp.mpf(0)) + sign*coefficient*mp.fprod(cache[m] for m in masks)
        # Compare a distinct complete Leibniz calculation against K203's
        # Gram determinant function only at control nodes, not the 184-node sum.
        spec = importlib.util.spec_from_file_location("k203", HERE / "k203_order_six_positive_moment_rule.py")
        k203 = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(k203)
        from flint import arb, ctx
        ctx.dps = 100
        entries = json.loads((ROOT/"lab/process/k184-order-six-certified-low-rank-wave.json").read_text())["andreief_time_gram_certificate"]["gram_entries"]
        actual = k203.signed_groups_at_node(entries, arb(str(rho)), [arb(str(x)) for x in z])
        assert set(groups) == set(actual) and len(groups) == 18
        for name, value in groups.items():
            center = mp.mpf(str(actual[name]).split(" +/- ")[0][1:])
            assert abs(value-center) < mp.mpf("1e-55"), (pair, name)
    return len(forms)


def replay_complete_rule(manifest):
    """Full weighted K185 Leibniz sum, independent of K203 determinants."""
    forms = k207.terms()
    root = mp.sqrt(7)
    radial = [((7-root)/256, (1+1/root)/2),
              ((7+root)/256, (1-1/root)/2)]
    center_weight = Q(manifest["rule"]["center_weight"])
    pair_weight = Q(manifest["rule"]["each_pair_weight"])
    angular = [([mp.mpf(1)/14]*N, center_weight)]
    angular.extend(([mp.mpf(19)/50 if i in pair else mp.mpf(1)/50
                     for i in range(N)], pair_weight)
                   for pair in itertools.combinations(range(N), 2))
    sums = {name: mp.mpf(0) for name in manifest["groups"]}
    for rho, rw in radial:
        for z, aw in angular:
            coefficient = rho**8*mp.fprod(zi**(mp.mpf(2)/3) for zi in z)/(2*mp.pi)**8
            cache = {}
            for _, _, masks in forms:
                for mask in masks:
                    if mask not in cache:
                        s = sum(z[i] for i in range(N) if mask & (1 << i))
                        cache[mask] = 2*mp.besselk(1, rho*s)
            for group, sign, masks in forms:
                sums[group] += mp.mpf(rw)*mp.mpf(aw.numerator)/aw.denominator * sign*coefficient*mp.fprod(cache[m] for m in masks)
    normalizer = mp.factorial(5)/256**6 * mp.gamma(mp.mpf(1)/3)**14/mp.gamma(mp.mpf(14)/3)
    for name, value in sums.items():
        saved = mp.mpf(manifest["groups"][name]["one_hundred_eighty_four_node_value_arb"].split(" +/- ")[0][1:])
        assert abs(normalizer*value-saved) < mp.mpf("1e-55"), name
    return sums


def main():
    manifest = exact_all_monomials()
    assert manifest["classification"] == "INTERNAL_STRUCTURAL_ONLY"
    assert "no improved nonpolynomial" in manifest["claim_ceiling"]
    assert manifest["counts"] == {"gram_entries": 234, "coherent_groups": 18,
                                  "angular_nodes": 92, "radial_nodes": 2, "product_nodes": 184}
    for key, path in (("K184", "k184-order-six-certified-low-rank-wave.json"),
                      ("K185", "k185-order-six-duffy-face-tail-wave.json"),
                      ("K202", "k202-order-six-common-weighted-core.json"),
                      ("K203", "k203-order-six-positive-moment-rule.json"),
                      ("K207", "k207-order-six-mixed-jets.json")):
        assert manifest["input_sha256"][key] == hashlib.sha256((ROOT/"lab/process"/path).read_bytes()).hexdigest()
    old = json.loads((ROOT/"lab/process/k203-order-six-positive-moment-rule.json").read_text())
    assert manifest["all_group_absolute_error_ceiling_rational"] == old["all_group_absolute_error_ceiling_rational"]
    assert signed_point_control() == 1864
    results = replay_complete_rule(manifest)
    assert len(results) == 18
    normalizer = mp.factorial(5)/256**6 * mp.gamma(mp.mpf(1)/3)**14/mp.gamma(mp.mpf(14)/3)
    saved_sum = mp.mpf(manifest["complete_signed_sum_arb"].split(" +/- ")[0][1:])
    assert abs(normalizer*sum(results.values())-saved_sum) < mp.mpf("1e-55")
    for field, replacement in (("center_weight", "0"), ("each_pair_weight", "0")):
        changed = json.loads(json.dumps(manifest))
        changed["rule"][field] = replacement
        w = Q(changed["rule"]["center_weight"])
        each = Q(changed["rule"]["each_pair_weight"])
        assert w + 91*each != 1
    # Mass-preserving corruption must still fail a nontrivial cubic moment.
    altered_center = Q(manifest["rule"]["center_weight"]) + Q(1, 1000)
    altered_pair = Q(manifest["rule"]["each_pair_weight"]) - Q(1, 91000)
    assert altered_center + 91*altered_pair == 1
    altered_cubic = altered_center*Q(1, 14)**3
    altered_cubic += sum(altered_pair*Q(19, 50)**3 for pair in itertools.combinations(range(N), 2) if 0 in pair)
    altered_cubic += sum(altered_pair*Q(1, 50)**3 for pair in itertools.combinations(range(N), 2) if 0 not in pair)
    assert altered_cubic != Q(1, 170)
    print("[PASS] all 680 angular monomials, radial degree three, positivity and mass")
    print("[PASS] independent K185 signed 1864-term replay at two pair nodes and all 184 weighted nodes")
    print("[PASS] three hostile weight mutations, including mass-preserving cubic corruption")


if __name__ == "__main__":
    main()
