#!/usr/bin/env python3
"""K208: rational 92-point cubic Dirichlet rule, paired with K203 radial nodes."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path

from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
P = ROOT / "lab/process"
OUT = P / "k208-order-six-cubic-moment-rule.json"
INPUTS = {key: P / name for key, name in (
    ("K184", "k184-order-six-certified-low-rank-wave.json"),
    ("K185", "k185-order-six-duffy-face-tail-wave.json"),
    ("K202", "k202-order-six-common-weighted-core.json"),
    ("K203", "k203-order-six-positive-moment-rule.json"),
    ("K207", "k207-order-six-mixed-jets.json"),
)}
spec = importlib.util.spec_from_file_location("k203", HERE / "k203_order_six_positive_moment_rule.py")
k203 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k203)
ctx.dps = 100
ctx.threads = 1
N = 14
PAIR_WEIGHT = Q(8125, 11016)
CENTER_WEIGHT = 1 - PAIR_WEIGHT
PAIRS = tuple(itertools.combinations(range(N), 2))


def angular_nodes():
    yield tuple(Q(1, N) for _ in range(N)), CENTER_WEIGHT
    for pair in PAIRS:
        yield tuple(Q(19, 50) if i in pair else Q(1, 50) for i in range(N)), PAIR_WEIGHT / len(PAIRS)


def dirichlet_moment(indices):
    alpha, total = Q(1, 3), Q(14, 3)
    top = math.prod(math.prod(alpha + j for j in range(indices.count(i)))
                    for i in set(indices))
    bottom = math.prod(total + j for j in range(len(indices)))
    return Q(top, bottom)


def rule_moment(indices):
    return sum((weight * math.prod(z[i] for i in indices)
                for z, weight in angular_nodes()), Q(0))


def exact_certificate():
    nodes = list(angular_nodes())
    assert len(nodes) == 92 and sum((w for _, w in nodes), Q(0)) == 1
    assert all(w > 0 and min(z) > 0 and sum(z) == 1 for z, w in nodes)
    # Symmetric moment tensors are determined by the partitions of 1, 2, 3.
    representatives = ((), (0,), (0, 0), (0, 1), (0, 0, 0),
                       (0, 0, 1), (0, 1, 2))
    moments = {}
    for indices in representatives:
        actual, expected = rule_moment(indices), dirichlet_moment(indices)
        assert actual == expected, (indices, actual, expected)
        moments[",".join(map(str, indices)) or "unit"] = str(actual)
    theta = Q(18, 25)
    covariance_ratio = Q(6, 13)  # uniform two-subsets vs centered one-hot orbit
    cubic_to_covariance_ratio = theta * Q(5, 12)
    assert PAIR_WEIGHT * covariance_ratio * theta**2 == Q(3, 17)
    assert cubic_to_covariance_ratio == Q(3, 10)
    return moments


def radial_nodes():
    root = arb(7).sqrt()
    yield (7-root)/256, (1+1/root)/2
    yield (7+root)/256, (1-1/root)/2


def generate():
    moments = exact_certificate()
    entries = json.loads(INPUTS["K184"].read_text())["andreief_time_gram_certificate"]["gram_entries"]
    old = json.loads(INPUTS["K203"].read_text())
    assert len(entries) == 234 and old["counts"]["coherent_groups"] == 18
    normalizer = (arb(120)/256**6 * (arb(1)/3).gamma()**14
                  / (arb(14)/3).gamma())
    group_values = defaultdict(lambda: arb(0))
    total_weight = arb(0)
    count = 0
    for rho, radial_weight in radial_nodes():
        for rational_z, rational_weight in angular_nodes():
            assert min(rational_z) >= Q(1, 50) > Q(1, 2**180)
            assert rho < arb(1)/4
            z = [arb(x.numerator)/x.denominator for x in rational_z]
            weight = radial_weight * arb(rational_weight.numerator)/rational_weight.denominator
            total_weight += weight
            groups = k203.signed_groups_at_node(entries, rho, z)
            assert len(groups) == 18
            for key, value in groups.items():
                group_values[key] += weight*value
            count += 1
    assert count == 184 and abs(total_weight-1) < arb("1e-80")
    for key in group_values:
        assert key in old["groups"]
    complete_sum = normalizer*sum(group_values.values(), arb(0))
    old_sum = sum((arb(row["twenty_eight_node_value_arb"])
                   for row in old["groups"].values()), arb(0))
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {key: hashlib.sha256(path.read_bytes()).hexdigest()
                         for key, path in INPUTS.items()},
        "counts": {"gram_entries": 234, "coherent_groups": 18,
                   "angular_nodes": 92, "radial_nodes": 2, "product_nodes": count},
        "rule": {
            "angular_reference": "Dirichlet(1/3)^14",
            "center": "z_i=1/14", "center_weight": str(CENTER_WEIGHT),
            "pair_nodes": "z_i=19/50 for i in a chosen unordered pair, 1/50 otherwise",
            "pair_count": len(PAIRS), "each_pair_weight": str(PAIR_WEIGHT/len(PAIRS)),
            "radial_nodes": old["rule"]["radial_nodes"],
            "radial_probabilities": old["rule"]["radial_probabilities"],
            "normalizer_arb": old["rule"]["normalizer_arb"],
        },
        "exact_angular_moments": moments,
        "moment_construction": "two-hot covariance factor 6/13 and cubic/covariance ratio 5*theta/12; target Dirichlet ratios 3/17 and 3/10 force theta=18/25 and total pair weight 8125/11016, leaving center weight 2891/11016",
        "exactness": "all angular polynomials of total degree <=3 and radial degree <=3; products thereof",
        "compact_core_location": "all 184 nodes have rho<1/4 and z_i>=1/50>2^-180; this does not transfer K204's degree-two conditional moment accounting to degree three",
        "complete_signed_sum_arb": str(complete_sum),
        "difference_from_k203_28_node_sum_arb": str(complete_sum-old_sum),
        "groups": {key: {"ordered_support_terms": old["groups"][key]["ordered_support_terms"],
                         "one_hundred_eighty_four_node_value_arb": str(normalizer*value),
                         "absolute_error_ceiling_rational": old["groups"][key]["absolute_error_ceiling_rational"]}
                   for key, value in sorted(group_values.items())},
        "all_group_absolute_error_ceiling_rational": old["all_group_absolute_error_ceiling_rational"],
        "remaining_gate": "fourth angular derivative cellwise enclosure for cubic Taylor remainder, Duffy/Jacobi chain, distinct K185/K188 termwise face/tail and K204 common-reference moment accounting, realistic coherent signed-group allocation; compare 184-node cost against K203's 28-node degree-two rule",
        "claim_ceiling": "positive interior cubic-angular polynomial rule and complete signed node values only; no improved nonpolynomial full-rule error, accurate order-six prefix, physical quotient or source result",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2)+"\n")
    print("[PASS] rational 92-point angular degree-three rule x two radial nodes")
    print("[PASS] 18 complete signed groups; inherited broad error unchanged")
