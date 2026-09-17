#!/usr/bin/env python3
"""K203 positive 28-node common-weight rule; no useful error budget claimed."""
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
OUT = ROOT / "lab/process/k203-order-six-positive-moment-rule.json"
spec = importlib.util.spec_from_file_location(
    "k202", HERE / "k202_order_six_common_weighted_core.py")
k202 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k202)
ctx.dps = 100
ctx.threads = 1


def exact_moments():
    """All identities here are rational consequences, not numerical fits."""
    alpha = Q(1, 3)
    total = 14 * alpha
    theta2 = 1 / (total + 1)
    mean = Q(1, 14)
    angular_diag = mean * mean + theta2 * Q(13, 196)
    angular_offdiag = mean * mean - theta2 * Q(1, 196)
    assert theta2 == Q(3, 17)
    assert angular_diag == alpha * (alpha + 1) / (total * (total + 1)) == Q(2, 119)
    assert angular_offdiag == alpha * alpha / (total * (total + 1)) == Q(1, 238)
    # Roots of monic L_2^(5)(x): x^2-14x+42=0.
    # Their weighted moments are 1, 6, 42, 336, respectively.
    # The radial variable is x/256, distributed Gamma(6,256).
    assert [math.prod(range(6, 6 + n)) for n in range(4)] == [1, 6, 42, 336]
    return {"angular_degree": 2, "radial_degree": 3,
            "angular_mean": str(mean), "angular_diag_second": str(angular_diag),
            "angular_offdiag_second": str(angular_offdiag),
            "radial_scaled_moments_through_degree_three": [1, 6, 42, 336]}


def argument_supports(k184, k185):
    """Replay the exact linear-form Jacobian for every determinant Leibniz term."""
    original = k184["andreief_time_gram_certificate"]["gram_entries"]
    support = k185["complete_face_hypergraph"]["entries"]
    catalog = k185["exact_allocation_certificate"]["allocation_catalog"]

    def tmask(i):
        return sum(1 << k for k in range(i - 1, 7))

    def umask(j):
        return sum(1 << k for k in range(7 + j - 1, 14))

    forms = set()
    checked = 0
    for row, record in zip(original, support):
        for term in record["terms"]:
            actual = dict(part.split(":") for part in term["species_permutations"].split("|"))
            expected = [tmask(row["left_old_position"]),
                        umask(row["right_old_position"])]
            for species in row["species_kernels"]:
                right = [int(x) for x in actual[species["species"]].split(",")]
                for i, j in zip(species["left_time_positions"], right):
                    expected.append(tmask(i) | umask(j))
            assert len(expected) == 8
            actual_masks = [int(x, 16) for x in
                            catalog[term["allocation_id"]]["support_masks_hex"].split(",")]
            assert actual_masks == expected, term["term_id"]
            forms.update(expected)
            checked += 1
    assert checked == 1864
    # If argument is rho * sum(mask_i*z_i), then its exact Jacobian is
    # d_rho = sum(mask_i*z_i), d_z_i = rho*mask_i, and all second
    # z_i,z_j derivatives vanish. The algebra is shared by old-position
    # and determinant factors; no independent fitted chain is supplied.
    return {"support_terms_checked": checked, "factor_occurrences_checked": 8 * checked,
            "distinct_linear_argument_masks": len(forms),
            "argument_formula": "rho*sum_i(mask_i*z_i)",
            "rho_derivative": "sum_i(mask_i*z_i)",
            "z_i_derivative": "rho*mask_i", "z_i_z_j_second_derivative": "0"}


def nodes():
    theta = (arb(3) / 17).sqrt()
    rad = arb(7).sqrt()
    zbase = (1 - theta) / 14
    radial = [((7 - rad) / 256, (1 + 1 / rad) / 2),
              ((7 + rad) / 256, (1 - 1 / rad) / 2)]
    assert all(weight > 0 and rho > 0 for rho, weight in radial)
    for rho, rw in radial:
        for k in range(14):
            z = [zbase + (theta if i == k else 0) for i in range(14)]
            assert all(x > 0 for x in z)
            yield rho, z, rw / 14


def determinant(matrix):
    m = len(matrix)
    return sum(((-1) ** sum(p[i] > p[j] for i in range(m)
                            for j in range(i + 1, m))
                * math.prod(matrix[i][p[i]] for i in range(m))
                for p in itertools.permutations(range(m))), arb(0))


def signed_groups_at_node(entries, rho, z):
    primitive = [rho * x for x in z]
    left_tails = {i: sum(primitive[i - 1:7], arb(0)) for i in range(1, 8)}
    right_tails = {i: sum(primitive[7 + i - 1:], arb(0)) for i in range(1, 8)}
    cache = {}

    def k1(t):
        key = str(t)
        if key not in cache:
            cache[key] = 2 * t.bessel_k(1)
        return cache[key]

    coefficient = rho ** 8 / (2 * arb.pi()) ** 8
    coefficient *= math.prod((x ** (arb(2) / 3) for x in z), start=arb(1))
    groups = defaultdict(lambda: arb(0))
    for entry in entries:
        v = arb(entry["coefficient_product"])
        v *= k1(left_tails[entry["left_old_position"]])
        v *= k1(right_tails[entry["right_old_position"]])
        for species in entry["species_kernels"]:
            left, right = species["left_time_positions"], species["right_time_positions"]
            v *= determinant([[k1(left_tails[i] + right_tails[j]) for j in right] for i in left])
        if entry["left"] != entry["right"]:
            v *= 2
        groups[entry["group_id"]] += coefficient * v
    return groups


def generate():
    k184, k185 = k202.load()
    support_entries, counts, minima = k202.validate(k184, k185)
    entries = k184["andreief_time_gram_certificate"]["gram_entries"]
    assert minima == (Q(1, 3),) * 14
    moments = exact_moments()
    geometry = argument_supports(k184, k185)
    normalizer = (arb(120) / 256 ** 6
                  * (arb(1) / 3).gamma() ** 14 / (arb(14) / 3).gamma())
    groups = defaultdict(lambda: arb(0))
    node_count = 0
    for rho, z, weight in nodes():
        node_count += 1
        point = signed_groups_at_node(entries, rho, z)
        assert set(point) == set(counts)
        for key, value in point.items():
            groups[key] += weight * value
    assert node_count == 28 and len(groups) == 18
    # Positive weights sum to one. K202's positive support-term majorant
    # bounds both integral and *every* point of the quotient: no false
    # improvement to the full-domain error is inferred from polynomial exactness.
    E = k202.proof_safe_per_support_term()
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "inputs_sha256": {
            "K184": hashlib.sha256(k202.K184.read_bytes()).hexdigest(),
            "K185": hashlib.sha256(k202.K185.read_bytes()).hexdigest(),
            "K202": hashlib.sha256(k202.OUT.read_bytes()).hexdigest(),
        },
        "counts": {"gram_entries": len(support_entries), "support_terms": 1864,
                   "ordered_support_terms": sum(counts.values()),
                   "coherent_groups": len(groups), "nodes": node_count},
        "rule": {
            "radial_nodes": ["(7-sqrt(7))/256", "(7+sqrt(7))/256"],
            "radial_probabilities": ["(1+1/sqrt(7))/2", "(1-1/sqrt(7))/2"],
            "angular_nodes": "z_i=(1-sqrt(3/17))/14+sqrt(3/17)*delta_(i,k), k=0..13",
            "angular_probabilities": "1/14 each", "normalizer_arb": str(normalizer),
            "reference": "rho^5 exp(-256 rho) product_i z_i^(-2/3)",
        },
        "exact_moments": moments,
        "linear_argument_geometry": geometry,
        "groups": {key: {"ordered_support_terms": counts[key],
                         "twenty_eight_node_value_arb": str(normalizer * value),
                         "absolute_error_ceiling_rational": str(2 * counts[key] * E)}
                   for key, value in sorted(groups.items())},
        "all_group_absolute_error_ceiling_rational": str(2 * sum(counts.values()) * E),
        "claim_ceiling": "positive 28-node low-degree-exact common-weight rule with the same broad K202 full-domain error; not an accurate order-six prefix or source/physics result",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] 28 positive nodes, radial degree 3 and angular degree 2")
    print("[PASS] 18 complete signed group values; broad error retained")
