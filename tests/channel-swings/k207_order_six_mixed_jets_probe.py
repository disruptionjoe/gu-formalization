#!/usr/bin/env python3
"""Independent K185 signed Leibniz replay of all K207 bivariate jets."""
from __future__ import annotations

from collections import defaultdict
import hashlib
import itertools
import json
import math
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
FILES = {key: P / name for key, name in (
    ("K184", "k184-order-six-certified-low-rank-wave.json"),
    ("K185", "k185-order-six-duffy-face-tail-wave.json"),
    ("K203", "k203-order-six-positive-moment-rule.json"),
    ("K205", "k205-order-six-radial-normal-form.json"),
    ("K206", "k206-order-six-angular-jets.json"),
)}
OUT = P / "k207-order-six-mixed-jets.json"
mp.mp.dps = 78
PAIRS = tuple(itertools.product(range(3), repeat=2))


def center(ball):
    return mp.mpf(ball.split(" +/- ")[0][1:])


def tmask(i):
    return sum(1 << j for j in range(i-1, 7))


def umask(i):
    return sum(1 << j for j in range(i+6, 14))


def terms():
    native = json.loads(FILES["K184"].read_text())["andreief_time_gram_certificate"]["gram_entries"]
    face = json.loads(FILES["K185"].read_text())
    records = face["complete_face_hypergraph"]["entries"]
    catalog = face["exact_allocation_certificate"]["allocation_catalog"]
    assert len(native) == len(records) == 234
    result = []
    for row, record in zip(native, records):
        assert (row["left"], row["right"], row["group_id"], row["coefficient_product"]) == (
            record["left"], record["right"], record["group_id"], record["coefficient_product"])
        saved = {term["species_permutations"]: term for term in record["terms"]}
        choices = [list(itertools.permutations(s["right_time_positions"]))
                   for s in row["species_kernels"]]
        for permutations in itertools.product(*choices):
            sign = row["coefficient_product"] * (1 if row["left"] == row["right"] else 2)
            masks = [tmask(row["left_old_position"]), umask(row["right_old_position"])]
            labels = []
            permutation_sign = 1
            for species, perm in zip(row["species_kernels"], permutations):
                masks.extend(tmask(i) | umask(j)
                             for i, j in zip(species["left_time_positions"], perm))
                indices = [species["right_time_positions"].index(j) for j in perm]
                permutation_sign *= (-1) ** sum(indices[i] > indices[j]
                                                for i in range(len(indices)) for j in range(i+1, len(indices)))
                labels.append(species["species"]+":"+",".join(map(str, perm)))
            record_term = saved.pop("|".join(labels))
            stored = tuple(int(x, 16) for x in catalog[record_term["allocation_id"]]
                           ["support_masks_hex"].split(","))
            assert tuple(masks) == stored and len(masks) == 8
            assert record_term["leibniz_sign"] == permutation_sign
            result.append((row["group_id"], sign*permutation_sign, stored))
        assert not saved
    assert len(result) == 1864
    return result


def multiply(a, b):
    return {(i, j): sum((a[k, l]*b[i-k, j-l]
                        for k in range(i+1) for l in range(j+1)), mp.mpf(0))
            for i, j in PAIRS}


def bessel_coefficients(x):
    """Taylor coefficients of K1 about x from its second-order ODE."""
    k1, k0 = mp.besselk(1, x), mp.besselk(0, x)
    c = [k1, -k0-k1/x]
    for n in range(3):
        back1 = c[n-1] if n >= 1 else mp.mpf(0)
        back2 = c[n-2] if n >= 2 else mp.mpf(0)
        c.append((2*x*back1+back2-(n*n-x*x-1)*c[n]
                  -x*(n+1)*(2*n+1)*c[n+1])/(x*x*(n+2)*(n+1)))
    return c


def factor_taylor(rho, s, t):
    # x=(rho+u)(s+t*a); truncate the rectangular coefficient ring (u^3,a^3).
    x0 = rho*s
    delta = {(i, j): mp.mpf(0) for i, j in PAIRS}
    delta[1, 0], delta[0, 1], delta[1, 1] = s, rho*t, t
    power = {(i, j): mp.mpf(int((i, j) == (0, 0))) for i, j in PAIRS}
    series = {(i, j): mp.mpf(0) for i, j in PAIRS}
    for coeff in bessel_coefficients(x0):
        for key in PAIRS:
            series[key] += coeff*power[key]
        power = multiply(power, delta)
    radius = {(i, j): mp.mpf(0) for i, j in PAIRS}
    radius[0, 0], radius[1, 0] = 2*rho, mp.mpf(2)
    return multiply(series, radius)


def sample(label):
    if label == "radial-minus|angular-0|direction-0-13":
        special, first, last = 0, 0, 13
    elif label == "radial-minus|angular-7|direction-6-7":
        special, first, last = 7, 6, 7
    else:
        raise AssertionError(label)
    rho = (7-mp.sqrt(7))/256
    theta = mp.sqrt(mp.mpf(3)/17)
    z = [(1-theta)/14+(theta if i == special else 0) for i in range(14)]
    v = [int(i == first)-int(i == last) for i in range(14)]
    return rho, z, v


def replay(forms, label):
    rho, z, v = sample(label)
    weight = {(i, j): mp.mpf(int((i, j) == (0, 0)))/(2*mp.pi)**8
              for i, j in PAIRS}
    for zi, vi in zip(z, v):
        angular = {(i, j): (zi**(mp.mpf(2)/3)
                            *mp.binomial(mp.mpf(2)/3, j)*(vi/zi)**j
                            if i == 0 else mp.mpf(0)) for i, j in PAIRS}
        weight = multiply(weight, angular)
    factors = {}
    for mask in {mask for _, _, masks in forms for mask in masks}:
        s = sum(z[i] for i in range(14) if mask & (1 << i))
        t = sum(v[i] for i in range(14) if mask & (1 << i))
        factors[mask] = factor_taylor(rho, s, t)
    groups = defaultdict(lambda: {key: mp.mpf(0) for key in PAIRS})
    for group, sign, masks in forms:
        product = weight
        for mask in masks:
            product = multiply(product, factors[mask])
        for i, j in PAIRS:
            groups[group][i, j] += sign*product[i, j]
    return {group: {(i, j): value[i, j]*math.factorial(i)*math.factorial(j)
                    for i, j in PAIRS} for group, value in groups.items()}


def inspect(manifest, forms, results):
    assert manifest["classification"] == "INTERNAL_STRUCTURAL_ONLY"
    assert "no global cellwise enclosure" in manifest["claim_ceiling"]
    assert manifest["counts"] == {"gram_entries": 234, "coherent_groups": 18,
                                  "mixed_partial_fields_per_group": 9,
                                  "independent_replay_factor_occurrences": 14912}
    for key, path in FILES.items():
        assert manifest["input_sha256"][key] == hashlib.sha256(path.read_bytes()).hexdigest()
    for label, groups in results.items():
        record = manifest["nodes"][label]
        assert set(groups) == set(record) and len(record) == 18
        for group, jets in groups.items():
            for i, j in PAIRS:
                assert abs(jets[i, j]-center(record[group][f"d{i}r_d{j}v_arb"])) < mp.mpf("1e-55"), (label, group, i, j)


def main():
    forms = terms()
    baseline = json.loads(OUT.read_text())
    results = {label: replay(forms, label) for label in baseline["nodes"]}
    inspect(baseline, forms, results)
    # Direct scalar differentiation checks the ODE seed and first recurrence.
    rho, z, v = sample(sorted(results)[0])
    mask = forms[0][2][0]
    x = rho*sum(z[i] for i in range(14) if mask & (1 << i))
    assert abs(mp.diff(lambda y: mp.besselk(1, y), x)
               -bessel_coefficients(x)[1]) < mp.mpf("1e-65")
    for field, replacement in (("classification", "PHYSICAL"),
                               ("claim_ceiling", "full rule certified")):
        changed = json.loads(json.dumps(baseline))
        changed[field] = replacement
        try:
            inspect(changed, forms, results)
        except AssertionError:
            pass
        else:
            raise AssertionError(f"hostile {field} mutation survived")
    for key in ("d1r_d1v_arb", "d2r_d2v_arb"):
        changed = json.loads(json.dumps(baseline))
        first = changed["nodes"][sorted(changed["nodes"])[0]]
        first[sorted(first)[0]][key] = "[0 +/- 0]"
        try:
            inspect(changed, forms, results)
        except AssertionError:
            pass
        else:
            raise AssertionError(f"hostile {key} mutation survived")
    print("[PASS] independent 1864 signed terms, 14912 support factors, 18 groups x 9 jets x 2 nodes")
    print("[PASS] four hostile mutations and direct Bessel-ODE seed differentiation")


if __name__ == "__main__":
    main()
