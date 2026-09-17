#!/usr/bin/env python3
"""Independent K205 source replay, signed 28-node control and hostile mutations."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
S = P / "k184-order-six-certified-low-rank-wave.json"
A = P / "k185-order-six-duffy-face-tail-wave.json"
B = P / "k202-order-six-common-weighted-core.json"
R = P / "k203-order-six-positive-moment-rule.json"
M = P / "k205-order-six-radial-normal-form.json"
mp.mp.dps = 65


def center(ball):
    return mp.mpf(ball.split(" +/- ")[0][1:])


def inspect(manifest):
    source = json.loads(S.read_text())
    allocations = json.loads(A.read_text())
    baseline = json.loads(B.read_text())
    prior = json.loads(R.read_text())
    for label, path in (("K184", S), ("K185", A), ("K202", B)):
        assert manifest["input_sha256"][label] == hashlib.sha256(path.read_bytes()).hexdigest()
    entries = source["andreief_time_gram_certificate"]["gram_entries"]
    rows = allocations["complete_face_hypergraph"]["entries"]
    catalog = allocations["exact_allocation_certificate"]["allocation_catalog"]
    assert len(entries) == len(rows) == 234
    forms = []
    multiplicities = []
    counts = defaultdict(int)
    for row, record in zip(entries, rows):
        assert row["group_id"] == record["group_id"]
        assert row["coefficient_product"] == record["coefficient_product"]
        ordered = 1 if row["left"] == row["right"] else 2
        for term in record["terms"]:
            pieces = dict(x.split(":") for x in term["species_permutations"].split("|"))
            left = [sum(1 << k for k in range(row["left_old_position"] - 1, 7))]
            right = [sum(1 << k for k in range(7 + row["right_old_position"] - 1, 14))]
            masks = left + right
            for species in row["species_kernels"]:
                assignments = [int(x) for x in pieces[species["species"]].split(",")]
                assert sorted(assignments) == sorted(species["right_time_positions"])
                for i, j in zip(species["left_time_positions"], assignments):
                    masks.append(sum(1 << k for k in range(i - 1, 7)) |
                                 sum(1 << k for k in range(7 + j - 1, 14)))
            stored = [int(x, 16) for x in catalog[term["allocation_id"]]["support_masks_hex"].split(",")]
            assert masks == stored and len(masks) == 8
            multiplicities.append(max(sum(bool(mask & (1 << i)) for mask in masks)
                                      for i in range(14)))
            forms.append((row["group_id"], ordered * row["coefficient_product"] *
                          term["leibniz_sign"], tuple(masks)))
            counts[row["group_id"]] += ordered
    assert len(forms) == 1864 and set(multiplicities) == {7}
    assert sum(counts.values()) == 2928 and len(counts) == 18
    assert manifest["max_simplex_support_multiplicity"] == 7
    assert manifest["counts"]["factor_occurrences"] == 8 * len(forms)
    assert manifest["radial_lipschitz_factor_per_ordered_term"] == 7
    assert F(manifest["radial_coupling_distance_strict_upper"]) == F(7, 512)
    assert F(manifest["radial_two_node_error_factor"]) == F(49, 512)
    E = F(baseline["per_support_term_integral_ceiling_rational"])
    assert F(manifest["all_groups_radial_only_error_upper_rational"]) == 2928 * F(49, 512) * E
    for group, n in counts.items():
        assert manifest["groups"][group]["ordered_support_terms"] == n
        assert F(manifest["groups"][group]["radial_only_error_upper_rational"]) == n * F(49, 512) * E
    assert manifest["unchanged_complete_rule_error_upper_rational"] == baseline["all_group_absolute_error_ceiling_rational"]

    # Independent Leibniz expansion of the pole-cancelled normal form at all
    # 28 K203 nodes, including exact path-pair and determinant permutation signs.
    norm = center(prior["rule"]["normalizer_arb"])
    radial = [(7 - mp.sqrt(7), (1 + 1 / mp.sqrt(7)) / 2),
              (7 + mp.sqrt(7), (1 - 1 / mp.sqrt(7)) / 2)]
    theta = mp.sqrt(mp.mpf(3) / 17)
    totals = defaultdict(lambda: mp.mpf(0))
    unique_masks = sorted({mask for _, _, masks in forms for mask in masks})
    for value, radial_weight in radial:
        rho = value / 256
        for special in range(14):
            z = [(1 - theta) / 14 + (theta if i == special else 0) for i in range(14)]
            factor = norm * radial_weight / 14 * mp.fprod(x ** (mp.mpf(2) / 3) for x in z) / (2 * mp.pi) ** 8
            bessel = {}
            for mask in unique_masks:
                support = sum(z[i] for i in range(14) if mask & (1 << i))
                bessel[mask] = 2 * rho * mp.besselk(1, rho * support)
            node = defaultdict(lambda: mp.mpf(0))
            for group, sign, masks in forms:
                node[group] += sign * mp.fprod(bessel[mask] for mask in masks)
            for group, value in node.items():
                totals[group] += factor * value
    for group, expected in prior["groups"].items():
        assert abs(totals[group] - center(expected["twenty_eight_node_value_arb"])) < mp.mpf("1e-55")
    # Independent numerical derivative control on a real eight-factor term;
    # the proof itself is the Bessel recurrence and strict K0<K1 inequality.
    rho = (7 - mp.sqrt(7)) / 256
    z = [(1 - theta) / 14 + (theta if i == 0 else 0) for i in range(14)]
    supports = [sum(z[i] for i in range(14) if mask & (1 << i))
                for mask in forms[0][2]]
    product = lambda r: mp.fprod(2 * r * mp.besselk(1, r * s) for s in supports)
    predicted = -product(rho) * sum(s * mp.besselk(0, rho * s) /
                                    mp.besselk(1, rho * s) for s in supports)
    assert abs(mp.diff(product, rho) - predicted) < mp.mpf("1e-50")
    return len(totals)


def main():
    baseline = json.loads(M.read_text())
    count = inspect(baseline)
    # Cheap adversaries run only structural checks, not repeated Bessel replay.
    for field, replacement in (("max_simplex_support_multiplicity", 8),
                               ("radial_lipschitz_factor_per_ordered_term", 6),
                               ("radial_two_node_error_factor", "1/20"),
                               ("unchanged_complete_rule_error_upper_rational", "0")):
        changed = json.loads(json.dumps(baseline))
        changed[field] = replacement
        try:
            inspect_structure(changed)
        except AssertionError:
            continue
        raise AssertionError("hostile mutation escaped: " + field)
    print(f"[PASS] independent signed normal form at 28 nodes for {count} groups")
    print("[PASS] exact rational radial-only bound and four hostile controls")


def inspect_structure(m):
    b = json.loads(B.read_text())
    assert m["max_simplex_support_multiplicity"] == 7
    assert m["radial_lipschitz_factor_per_ordered_term"] == 7
    assert F(m["radial_two_node_error_factor"]) == F(49, 512)
    assert m["unchanged_complete_rule_error_upper_rational"] == b["all_group_absolute_error_ceiling_rational"]


if __name__ == "__main__":
    main()
