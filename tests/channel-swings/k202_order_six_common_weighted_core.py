#!/usr/bin/env python3
"""K202: one honest common-weight rule for the complete K184 order-six Grams.

The one-node error is intentionally broad; this is not an accurate prefix.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
import itertools
import json
import math
from pathlib import Path

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K184 = ROOT / "lab/process/k184-order-six-certified-low-rank-wave.json"
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
OUT = ROOT / "lab/process/k202-order-six-common-weighted-core.json"
ctx.dps = 100
ctx.threads = 1


def load():
    return json.loads(K184.read_text()), json.loads(K185.read_text())


def parsed_weights(record):
    factors = []
    for factor in record["weights"].split(";"):
        factors.append({int(i): Q(weight) for i, weight in
                        (cell.split(":") for cell in factor.split(","))})
    return factors


def validate(k184, k185):
    """Independent rational replay of every allocation and K184 occurrence."""
    entries = k185["complete_face_hypergraph"]["entries"]
    catalog = k185["exact_allocation_certificate"]["allocation_catalog"]
    original = k184["andreief_time_gram_certificate"]["gram_entries"]
    assert len(original) == len(entries) == 234
    assert len(catalog) == 1276
    seen = set()
    betas = []
    signed_counts = defaultdict(int)
    for a, b in zip(original, entries):
        for field in ("left", "right", "group_id", "coefficient_product"):
            assert a[field] == b[field], (field, a.get(field), b.get(field))
        expected = math.prod(math.factorial(len(s["left_time_positions"]))
                             for s in a["species_kernels"])
        assert b["leibniz_term_count"] == len(b["terms"]) == expected
        assert b["coefficient_product"] in (-1, 1)
        ordered = 1 if b["left"] == b["right"] else 2
        signed_counts[b["group_id"]] += ordered * expected
        permutations_seen = set()
        for term in b["terms"]:
            assert term["term_id"] not in seen
            seen.add(term["term_id"])
            assert term["leibniz_sign"] in (-1, 1)
            assert term["allocation_id"] in catalog
            parts = dict(cell.split(":") for cell in term["species_permutations"].split("|"))
            assert set(parts) == {s["species"] for s in a["species_kernels"]}
            sign = 1
            signature = []
            for species in a["species_kernels"]:
                canonical = species["right_time_positions"]
                actual = [int(x) for x in parts[species["species"]].split(",")]
                assert sorted(actual) == sorted(canonical)
                indices = [canonical.index(x) for x in actual]
                sign *= (-1) ** sum(indices[i] > indices[j] for i in range(len(indices))
                                    for j in range(i + 1, len(indices)))
                signature.append(tuple(actual))
            assert sign == term["leibniz_sign"]
            assert tuple(signature) not in permutations_seen
            permutations_seen.add(tuple(signature))
        assert len(permutations_seen) == expected
    assert len(seen) == 1864 and len(signed_counts) == 18
    for allocation in catalog.values():
        factors = parsed_weights(allocation)
        masks = [int(s, 16) for s in allocation["support_masks_hex"].split(",")]
        assert len(factors) == len(masks) == 8
        loads = [Q(0)] * 14
        for factor, mask in zip(factors, masks):
            assert sum(factor.values()) == 1
            assert set(factor) <= {i for i in range(14) if mask & (1 << i)}
            for i, weight in factor.items():
                assert weight > 0
                loads[i] += weight
        assert loads == [Q(x) for x in allocation["loads"].split(",")]
        assert max(loads) == Q(allocation["maximum_load"])
        betas.append(tuple(1 - x for x in loads))
    minima = tuple(min(row[i] for row in betas) for i in range(14))
    assert minima == (Q(1, 3),) * 14
    assert sum(signed_counts.values()) == 2928
    return entries, dict(signed_counts), minima


def determinant(matrix):
    m = len(matrix)
    return sum(((-1) ** sum(p[i] > p[j] for i in range(m)
                            for j in range(i + 1, m))
                * math.prod(matrix[i][p[i]] for i in range(m))
                for p in itertools.permutations(range(m))), arb(0))


def node_values(k184):
    # Gamma(6,256) radial mean and Dirichlet(1/3,...,1/3) angular mean.
    rho = arb(3) / 128
    primitive = rho / 14
    tails = {i: (8 - i) * primitive for i in range(1, 8)}
    cache = {}

    def k1(argument):
        key = str(argument)
        if key not in cache:
            cache[key] = 2 * argument.bessel_k(1)
        return cache[key]

    coefficient = rho ** 8 / (2 * arb.pi()) ** 8
    # Divide the original transformed integrand by prod(z_i^-2/3).
    coefficient *= (-(arb(28) / 3) * arb(14).log()).exp()
    groups = defaultdict(lambda: arb(0))
    for row in k184["andreief_time_gram_certificate"]["gram_entries"]:
        value = arb(row["coefficient_product"])
        value *= k1(tails[row["left_old_position"]])
        value *= k1(tails[row["right_old_position"]])
        for species in row["species_kernels"]:
            l = species["left_time_positions"]
            r = species["right_time_positions"]
            value *= determinant([[k1(tails[i] + tails[j]) for j in r] for i in l])
        if row["left"] != row["right"]:
            value *= 2
        groups[row["group_id"]] += coefficient * value
    return groups


def proof_safe_per_support_term():
    # Gamma(1/3)<27/8; Gamma(2/3)>9/10 by e^-t>=1-t on [0,1].
    # Gamma(14/3)=(11*8*5*2/3^4) Gamma(2/3)>792/81.
    # pi>3, C_w=prod w^w<=1, int rho^5 exp(-256rho)=120/256^6.
    return Q(27, 8) ** 14 * Q(81, 792) * Q(120, 256 ** 6) / 3 ** 8


def generate():
    k184, k185 = load()
    entries, counts, minima = validate(k184, k185)
    groups = node_values(k184)
    assert set(groups) == set(counts)
    Z = arb(1) / 3
    Z = Z.gamma() ** 14 / (arb(14) / 3).gamma()
    Z *= arb(120) / 256 ** 6
    E = proof_safe_per_support_term()
    result = {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {"K184": __import__("hashlib").sha256(K184.read_bytes()).hexdigest(),
                         "K185": __import__("hashlib").sha256(K185.read_bytes()).hexdigest()},
        "counts": {"gram_entries": len(entries), "support_terms": 1864,
                   "ordered_support_terms": sum(counts.values()),
                   "coherent_groups": len(groups), "distinct_allocations": 1276},
        "common_angular_exponents": [str(x - 1) for x in minima],
        "rule": {"rho_node": "3/128", "angular_nodes": ["1/14"] * 14,
                 "radial_weight": "rho^5 exp(-256 rho)",
                 "angular_weight": "product_i z_i^(-2/3)",
                 "normalizer": "120/256^6 * Gamma(1/3)^14 / Gamma(14/3)",
                 "normalizer_arb": str(Z)},
        "per_support_term_integral_ceiling_rational": str(E),
        "groups": {},
        "claim_ceiling": "rigorous but broad one-node error for complete signed K184 order-six time-Gram family; no accurate prefix or physical/source effect",
    }
    for group_id in sorted(groups):
        n = counts[group_id]
        result["groups"][group_id] = {
            "ordered_support_terms": n,
            "one_node_value_arb": str((Z * groups[group_id])),
            "absolute_error_ceiling_rational": str(2 * n * E),
        }
    result["all_group_absolute_error_ceiling_rational"] = str(2 * sum(counts.values()) * E)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K202 234 entries, 1864 terms, 1276 allocations, 18 signed groups")
    print("[PASS] common angular weight and one-node rational error", result["all_group_absolute_error_ceiling_rational"])
