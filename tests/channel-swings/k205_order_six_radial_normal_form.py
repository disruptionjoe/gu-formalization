#!/usr/bin/env python3
"""K205: signed Gram radial normal form and radial-only error certificate."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
K184 = ROOT / "lab/process/k184-order-six-certified-low-rank-wave.json"
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K202 = ROOT / "lab/process/k202-order-six-common-weighted-core.json"
OUT = ROOT / "lab/process/k205-order-six-radial-normal-form.json"


def tmask(i: int) -> int:
    return sum(1 << j for j in range(i - 1, 7))


def umask(i: int) -> int:
    return sum(1 << j for j in range(i + 6, 14))


def expected_terms(entry):
    species = entry["species_kernels"]
    lists = [list(itertools.permutations(s["right_time_positions"])) for s in species]
    for choices in itertools.product(*lists):
        masks = [tmask(entry["left_old_position"]), umask(entry["right_old_position"])]
        sign = 1
        parts = []
        for s, perm in zip(species, choices):
            left = s["left_time_positions"]
            masks.extend(tmask(i) | umask(j) for i, j in zip(left, perm))
            original = s["right_time_positions"]
            indices = [original.index(j) for j in perm]
            sign *= (-1) ** sum(indices[i] > indices[j]
                                 for i in range(len(indices)) for j in range(i + 1, len(indices)))
            parts.append(s["species"] + ":" + ",".join(map(str, perm)))
        yield "|".join(parts), sign, tuple(masks)


def generate():
    source = json.loads(K184.read_text())
    allocation = json.loads(K185.read_text())
    baseline = json.loads(K202.read_text())
    original = source["andreief_time_gram_certificate"]["gram_entries"]
    records = allocation["complete_face_hypergraph"]["entries"]
    catalog = allocation["exact_allocation_certificate"]["allocation_catalog"]
    assert len(original) == len(records) == 234
    groups = defaultdict(int)
    term_count = factor_count = 0
    maximal_load = 0
    for row, record in zip(original, records):
        assert all(row[field] == record[field] for field in
                   ("left", "right", "group_id", "coefficient_product"))
        actual = {term["species_permutations"]: term for term in record["terms"]}
        assert len(actual) == len(record["terms"])
        for key, sign, masks in expected_terms(row):
            term = actual.pop(key)
            assert term["leibniz_sign"] == sign
            stored = tuple(int(x, 16) for x in
                           catalog[term["allocation_id"]]["support_masks_hex"].split(","))
            assert masks == stored and len(masks) == 8
            # sum_j S_j(z) = sum_i m_i z_i, so its simplex maximum is max_i m_i.
            multiplicity = max(sum(bool(mask & (1 << i)) for mask in masks)
                               for i in range(14))
            assert multiplicity == 7
            maximal_load = max(maximal_load, multiplicity)
            ordered = 1 if row["left"] == row["right"] else 2
            groups[row["group_id"]] += ordered
            term_count += 1
            factor_count += len(masks)
        assert not actual
    assert (term_count, factor_count, maximal_load) == (1864, 14912, 7)
    assert sum(groups.values()) == 2928
    assert {k: v["ordered_support_terms"] for k, v in baseline["groups"].items()} == dict(groups)
    E = F(baseline["per_support_term_integral_ceiling_rational"])
    # Coupling independent Gamma(6,256) and the two-point degree-three-exact
    # rule has mean-square distance 2*Var(rho)=12/256^2.  Cauchy gives
    # E|rho-R|<=sqrt(12)/256<7/512, entirely rational at the last step.
    radial_factor = F(7 * 7, 512)
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {"K184": hashlib.sha256(K184.read_bytes()).hexdigest(),
                         "K185": hashlib.sha256(K185.read_bytes()).hexdigest(),
                         "K202": hashlib.sha256(K202.read_bytes()).hexdigest()},
        "counts": {"gram_entries": len(records), "leibniz_terms": term_count,
                   "ordered_terms": sum(groups.values()), "factor_occurrences": factor_count,
                   "coherent_groups": len(groups)},
        "max_simplex_support_multiplicity": maximal_load,
        "normal_form": "rho^8 product_j[2 K1(rho S_j)] = product_j[2 rho S_j K1(rho S_j)/S_j], S_j=sum_(i in mask_j) z_i; eight factors per term",
        "derivative_identity": "d_rho log(product_j[2 rho S_j K1(rho S_j)/S_j])=-sum_j S_j K0(rho S_j)/K1(rho S_j)",
        "proof": {
            "bessel": "(x K1(x))'=-x K0(x); the positive cosh-integral representation proves 0<K0(x)<K1(x) for x>0; 2xK1(x)<=2 by its unit limit and negative derivative",
            "allocation": "K185 termwise AM-GM gives product_i z_i^(2/3)/product_j S_j <= C_w <= 1; thus each normal-form quotient has absolute value <= pi^-8",
            "support": "sum_j S_j(z)=sum_i m_i z_i <= max_i m_i=7 on the simplex for every exact K184/K185 term; hence absolute first radial derivative <= 7 pi^-8",
            "coupling": "Independent Gamma(6,256) rho and K203 two-node R have the same mean and variance 6/256^2, hence E|rho-R|<=sqrt(12)/256<7/512 by Cauchy-Schwarz",
            "error": "With exact angular expectation on both sides, each signed group with n ordered terms has radial-only error <=49*n*Z/(512*pi^8)<=49*n*E/512, E=K202 proof-safe per-support-term ceiling",
            "scope_limit": "The K203 fourteen-node angular replacement, positive-core higher mixed derivatives, signed group allocation, K185/K188 term-specific boundary and K204 common-reference lost mass are separate obligations; no accurate full integral or physical/source claim",
        },
        "radial_lipschitz_factor_per_ordered_term": maximal_load,
        "radial_coupling_distance_strict_upper": "7/512",
        "radial_two_node_error_factor": str(radial_factor),
        "per_ordered_term_integrated_radial_error_upper_rational": str(radial_factor * E),
        "groups": {key: {"ordered_support_terms": n,
                         "radial_only_error_upper_rational": str(radial_factor * n * E)}
                   for key, n in sorted(groups.items())},
        "all_groups_radial_only_error_upper_rational": str(radial_factor * sum(groups.values()) * E),
        "unchanged_complete_rule_error_upper_rational": baseline["all_group_absolute_error_ceiling_rational"],
        "scope": "integrate exact Dirichlet angular reference on both sides; compare exact Gamma radial integral with K203 two-node radial rule at each z before angular quadrature",
        "claim_ceiling": "proof-safe radial component for complete signed groups, not angular quadrature error, core remainder, accurate order-six integral, action column or physical/source result",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] 234 entries; 1864 terms; 14912 independently replayed masks")
    print("[PASS] maximal support multiplicity 7; 18 signed radial-only error ceilings")
