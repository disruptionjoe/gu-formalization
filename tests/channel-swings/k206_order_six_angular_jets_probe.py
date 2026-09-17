#!/usr/bin/env python3
"""Independent K206 Leibniz-jet replay, including signed permutation controls."""
from __future__ import annotations

from collections import defaultdict
import hashlib
import itertools
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
FILES = {k: P / f for k, f in (
    ("K184", "k184-order-six-certified-low-rank-wave.json"),
    ("K185", "k185-order-six-duffy-face-tail-wave.json"),
    ("K203", "k203-order-six-positive-moment-rule.json"),
    ("K205", "k205-order-six-radial-normal-form.json"))}
OUT = P / "k206-order-six-angular-jets.json"
mp.mp.dps = 75


def center(ball: str):
    return mp.mpf(ball.split(" +/- ")[0][1:])


def tmask(i):
    return sum(1 << j for j in range(i - 1, 7))


def umask(i):
    return sum(1 << j for j in range(i + 6, 14))


def terms():
    original = json.loads(FILES["K184"].read_text())[
        "andreief_time_gram_certificate"]["gram_entries"]
    allocation = json.loads(FILES["K185"].read_text())
    records = allocation["complete_face_hypergraph"]["entries"]
    catalog = allocation["exact_allocation_certificate"]["allocation_catalog"]
    assert len(original) == len(records) == 234
    result = []
    for row, record in zip(original, records):
        assert row["group_id"] == record["group_id"]
        assert row["coefficient_product"] == record["coefficient_product"]
        saved = {item["species_permutations"]: item for item in record["terms"]}
        choices = [list(itertools.permutations(s["right_time_positions"]))
                   for s in row["species_kernels"]]
        for permutations in itertools.product(*choices):
            sign = row["coefficient_product"] * (1 if row["left"] == row["right"] else 2)
            masks = [tmask(row["left_old_position"]), umask(row["right_old_position"])]
            parts = []
            for species, right in zip(row["species_kernels"], permutations):
                left = species["left_time_positions"]
                masks.extend(tmask(i) | umask(j) for i, j in zip(left, right))
                indices = [species["right_time_positions"].index(j) for j in right]
                sign *= (-1) ** sum(indices[i] > indices[j]
                                    for i in range(len(indices)) for j in range(i + 1, len(indices)))
                parts.append(species["species"] + ":" + ",".join(map(str, right)))
            saved_term = saved.pop("|".join(parts))
            assert len(masks) == 8
            assert saved_term["leibniz_sign"] == (1 if sign * row["coefficient_product"] > 0 else -1)
            stored = [int(s, 16) for s in catalog[saved_term["allocation_id"]][
                "support_masks_hex"].split(",")]
            assert stored == masks
            result.append((row["group_id"], sign, tuple(masks)))
        assert not saved
    assert len(result) == 1864
    return result


def sample_data(label):
    if label == "radial-minus|angular-0|direction-0-13":
        special, first, last = 0, 0, 13
    elif label == "radial-minus|angular-7|direction-6-7":
        special, first, last = 7, 6, 7
    else:
        raise AssertionError(label)
    rho = (7 - mp.sqrt(7)) / 256
    theta = mp.sqrt(mp.mpf(3) / 17)
    z = [(1 - theta) / 14 + (theta if i == special else 0) for i in range(14)]
    v = [int(i == first) - int(i == last) for i in range(14)]
    return rho, z, v


def replay(forms, label):
    rho, z, v = sample_data(label)
    common = mp.fprod(x ** (mp.mpf(2) / 3) for x in z) / (2 * mp.pi) ** 8
    A = mp.mpf(2) / 3 * sum(d / x for d, x in zip(v, z))
    B = -mp.mpf(2) / 3 * sum(d * d / (x * x) for d, x in zip(v, z))
    unique = sorted({mask for _, _, masks in forms for mask in masks})
    kernel = {}
    for mask in unique:
        s = sum(z[i] for i in range(14) if mask & (1 << i))
        d = sum(v[i] for i in range(14) if mask & (1 << i))
        x = rho * s
        k0, k1 = mp.besselk(0, x), mp.besselk(1, x)
        h = 2 * rho * k1
        h1 = -2 * rho**2 * d * (k0 + k1 / x)
        h2 = 2 * rho**3 * d**2 * (k1 + k0 / x + 2 * k1 / x**2)
        kernel[mask] = h, h1 / h, h2 / h
    groups = defaultdict(lambda: [mp.mpf(0), mp.mpf(0), mp.mpf(0)])
    for group, sign, masks in forms:
        values = [kernel[mask] for mask in masks]
        q = sign * common * mp.fprod(t[0] for t in values)
        R = sum(t[1] for t in values)
        C = sum(t[2] - t[1]**2 for t in values)
        subtotal = groups[group]
        subtotal[0] += q
        subtotal[1] += q * (A + R)
        subtotal[2] += q * ((A + R)**2 + B + C)
    return groups


def inspect(manifest, forms):
    assert manifest["classification"] == "INTERNAL_STRUCTURAL_ONLY"
    for label, path in FILES.items():
        assert manifest["input_sha256"][label] == hashlib.sha256(path.read_bytes()).hexdigest()
    assert manifest["counts"] == {"gram_entries": 234, "coherent_groups": 18,
                                  "independent_replay_factor_occurrences": 14912}
    assert "no global derivative supremum" in manifest["claim_ceiling"]
    for label, record in manifest["nodes"].items():
        direct = replay(forms, label)
        assert len(direct) == len(record) == 18
        for group, jets in record.items():
            for index, field in enumerate(("value_arb", "first_arb", "second_arb")):
                assert abs(direct[group][index] - center(jets[field])) < mp.mpf("1e-55"), (label, group, field)


def main():
    forms = terms()
    baseline = json.loads(OUT.read_text())
    inspect(baseline, forms)
    # A direct differential control is distinct from both jet-ring propagation
    # and the logarithmic Leibniz formula used for the full replay.
    rho, z, v = sample_data(sorted(baseline["nodes"])[0])
    _, _, masks = forms[0]
    def one(t):
        shifted = [x + t * d for x, d in zip(z, v)]
        factor = mp.fprod(x ** (mp.mpf(2) / 3) for x in shifted) / (2 * mp.pi) ** 8
        return factor * mp.fprod(2 * rho * mp.besselk(1, rho * sum(
            shifted[i] for i in range(14) if mask & (1 << i))) for mask in masks)
    direction_ratio = []
    curvature_ratio = []
    for mask in masks:
        s = sum(z[i] for i in range(14) if mask & (1 << i))
        d = sum(v[i] for i in range(14) if mask & (1 << i))
        x = rho * s
        k0, k1 = mp.besselk(0, x), mp.besselk(1, x)
        ratio = -rho * d * (k0 / k1 + 1 / x)
        direction_ratio.append(ratio)
        curvature_ratio.append(rho**2 * d**2 * (1 + k0 / (x * k1) + 2 / x**2) - ratio**2)
    A = mp.mpf(2) / 3 * sum(d / x for d, x in zip(v, z))
    B = -mp.mpf(2) / 3 * sum(d * d / (x * x) for d, x in zip(v, z))
    predicted = one(0) * ((A + sum(direction_ratio))**2 + B + sum(curvature_ratio))
    assert abs(mp.diff(one, 0, 2) - predicted) < mp.mpf("1e-55")
    for field, replacement in (("classification", "PHYSICAL"),
                               ("claim_ceiling", "full rule certified")):
        changed = json.loads(json.dumps(baseline))
        changed[field] = replacement
        try:
            inspect(changed, forms)
        except AssertionError:
            pass
        else:
            raise AssertionError(f"hostile {field} mutation survived")
    changed = json.loads(json.dumps(baseline))
    first = changed["nodes"][sorted(changed["nodes"])[0]]
    first[sorted(first)[0]]["second_arb"] = "[0 +/- 0]"
    try:
        inspect(changed, forms)
    except AssertionError:
        pass
    else:
        raise AssertionError("hostile second-jet mutation survived")
    changed = json.loads(json.dumps(baseline))
    first = changed["nodes"][sorted(changed["nodes"])[0]]
    entry = first[sorted(first)[0]]
    entry["value_arb"] = f"[{-center(entry['value_arb'])} +/- 0]"
    try:
        inspect(changed, forms)
    except AssertionError:
        pass
    else:
        raise AssertionError("hostile coherent-sign mutation survived")
    print("[PASS] 14912 independently reconstructed support occurrences and signed jets")
    print("[PASS] 18 groups x 2 nodes x 3 jets; four hostile mutations caught")


if __name__ == "__main__":
    main()
