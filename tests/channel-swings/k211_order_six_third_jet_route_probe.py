#!/usr/bin/env python3
"""Independent K185 permutation/Taylor replay of K211's third signed jets."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
FILES = {key: P / f"k{key}-order-six-{suffix}.json" for key, suffix in (
    (184, "certified-low-rank-wave"), (185, "duffy-face-tail-wave"),
    (203, "positive-moment-rule"), (204, "core-moment-defect"),
    (205, "radial-normal-form"),
    (206, "angular-jets"), (209, "cubic-core-geometry"),
)}
OUT = P / "k211-order-six-third-jet-route.json"
mp.mp.dps = 82


def center(ball):
    return mp.mpf(ball.split(" +/- ")[0][1:])


def tmask(i):
    return sum(1 << j for j in range(i-1, 7))


def umask(i):
    return sum(1 << j for j in range(i+6, 14))


def terms():
    native = json.loads(FILES[184].read_text())["andreief_time_gram_certificate"]["gram_entries"]
    face = json.loads(FILES[185].read_text())
    records = face["complete_face_hypergraph"]["entries"]
    catalog = face["exact_allocation_certificate"]["allocation_catalog"]
    assert len(native) == len(records) == 234
    forms = []
    for row, record in zip(native, records):
        assert row["group_id"] == record["group_id"]
        saved = {term["species_permutations"]: term for term in record["terms"]}
        choices = [list(itertools.permutations(s["right_time_positions"]))
                   for s in row["species_kernels"]]
        for permutations in itertools.product(*choices):
            masks = [tmask(row["left_old_position"]), umask(row["right_old_position"])]
            sign = row["coefficient_product"]*(1 if row["left"] == row["right"] else 2)
            parity = 1
            labels = []
            for species, perm in zip(row["species_kernels"], permutations):
                masks.extend(tmask(i)|umask(j) for i, j in zip(species["left_time_positions"], perm))
                indices = [species["right_time_positions"].index(j) for j in perm]
                parity *= (-1)**sum(indices[i] > indices[j] for i in range(len(indices))
                                    for j in range(i+1, len(indices)))
                labels.append(species["species"]+":"+",".join(map(str, perm)))
            item = saved.pop("|".join(labels))
            stored = tuple(int(s, 16) for s in catalog[item["allocation_id"]][
                "support_masks_hex"].split(","))
            assert tuple(masks) == stored and item["leibniz_sign"] == parity
            forms.append((row["group_id"], sign*parity, stored))
        assert not saved
    assert len(forms) == 1864
    return forms


def multiply(a, b):
    return [sum((a[i]*b[n-i] for i in range(n+1)), mp.mpf(0)) for n in range(4)]


def ode_coefficients(x):
    # x^2 K1''+x K1'-(x^2+1)K1=0, independently of producer's
    # explicit K0/K1 third derivative formula.
    c = [mp.besselk(1, x), -mp.besselk(0, x)-mp.besselk(1, x)/x]
    for n in range(2):
        previous = c[n-1] if n else mp.mpf(0)
        previous2 = c[n-2] if n >= 2 else mp.mpf(0)
        c.append((2*x*previous+previous2-(n*n-x*x-1)*c[n]
                  -x*(n+1)*(2*n+1)*c[n+1])/(x*x*(n+2)*(n+1)))
    return c


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
    pref = [1/(2*mp.pi)**8, mp.mpf(0), mp.mpf(0), mp.mpf(0)]
    for zi, vi in zip(z, v):
        factor = [zi**(mp.mpf(2)/3)*mp.binomial(mp.mpf(2)/3, n)
                  *(vi/zi)**n for n in range(4)]
        pref = multiply(pref, factor)
    kernels = {}
    for mask in {mask for _, _, masks in forms for mask in masks}:
        s = sum(z[i] for i in range(14) if mask & (1 << i))
        t = sum(v[i] for i in range(14) if mask & (1 << i))
        c = ode_coefficients(rho*s)
        kernels[mask] = [2*rho*c[n]*(rho*t)**n for n in range(4)]
    groups = defaultdict(lambda: mp.mpf(0))
    for group, sign, masks in forms:
        result = pref
        for mask in masks:
            result = multiply(result, kernels[mask])
        groups[group] += sign*6*result[3]
    return groups


def inspect(record, forms, results):
    assert record["classification"] == "INTERNAL_STRUCTURAL_ONLY"
    assert "no global cellwise enclosure" in record["claim_ceiling"]
    assert record["counts"] == {"gram_entries": 234, "coherent_groups": 18,
                                "signed_leibniz_terms": 1864, "factor_occurrences": 14912}
    for key, path in FILES.items():
        assert record["input_sha256"][str(key)] == hashlib.sha256(path.read_bytes()).hexdigest()
    geom = record["geometry"]
    r2 = F(39, 238)
    r4 = F(json.loads(FILES[209].read_text())["centered_euclidean_fourth_reference"])
    lost = F(json.loads(FILES[204].read_text())["lost_reference_probability_upper_rational"])
    a = F(geom["reference_third_moment_cauchy_upper"])
    b = F(geom["rule_third_moment_upper"])/r2
    assert a*a > r2*r4 and b*b > r2
    assert F(geom["conditional_third_taylor_coefficient_upper"]) == (a/(1-lost)+r2*b)/6
    assert F(geom["conditional_fourth_taylor_coefficient_upper_K209"]) == F(
        json.loads(FILES[209].read_text())["conditional_taylor_remainder_coefficient_upper"])
    radial = F(json.loads(FILES[205].read_text())["all_groups_radial_only_error_upper_rational"])
    assert F(record["separate_radial_only_error_upper_rational_K205"]) == radial < F(4633, 10**11)
    low, high = map(F, geom["cubic_z0_rule_minus_reference_open_interval"])
    theta_low, theta_high = map(F, geom["theta_open_interval"])
    assert theta_low**2 < F(3, 17) < theta_high**2 and 0 < low < high
    theta = mp.sqrt(mp.mpf(3)/17)
    actual = sum(((1-theta)/14+(theta if i == 0 else 0))**3 for i in range(14))/14-mp.mpf(1)/170
    assert mp.mpf(low.numerator)/low.denominator < actual < mp.mpf(high.numerator)/high.denominator
    for label, groups in results.items():
        assert set(record["nodes"][label]) == set(groups) and len(groups) == 18
        for group, value in groups.items():
            assert abs(value-center(record["nodes"][label][group]["d3v_arb"])) < mp.mpf("1e-55"), (label, group)


def main():
    forms = terms()
    baseline = json.loads(OUT.read_text())
    results = {label: replay(forms, label) for label in baseline["nodes"]}
    inspect(baseline, forms, results)
    rho, z, v = sample(sorted(results)[0])
    mask = forms[0][2][0]
    x = rho*sum(z[i] for i in range(14) if mask & (1 << i))
    assert abs(mp.diff(lambda y: mp.besselk(1, y), x, 3)-6*ode_coefficients(x)[3]) < mp.mpf("1e-65")
    for key, replacement in (("classification", "PHYSICAL"),
                             ("claim_ceiling", "full rule certified")):
        changed = json.loads(json.dumps(baseline))
        changed[key] = replacement
        try:
            inspect(changed, forms, results)
        except AssertionError:
            pass
        else:
            raise AssertionError(f"hostile {key} mutation survived")
    for field in ("d3v_arb",):
        changed = json.loads(json.dumps(baseline))
        label = sorted(changed["nodes"])[0]
        group = sorted(changed["nodes"][label])[0]
        changed["nodes"][label][group][field] = "[0 +/- 0]"
        try:
            inspect(changed, forms, results)
        except AssertionError:
            pass
        else:
            raise AssertionError("hostile signed third jet survived")
    changed = json.loads(json.dumps(baseline))
    changed["geometry"]["cubic_z0_rule_minus_reference_open_interval"] = ["-1", "1"]
    try:
        inspect(changed, forms, results)
    except AssertionError:
        pass
    else:
        raise AssertionError("hostile cubic witness survived")
    print("[PASS] 1864 independent K185 terms, 14912 masks, 18 groups x two third jets")
    print("[PASS] exact geometry/cubic witness, Bessel ODE, four hostile mutations")


if __name__ == "__main__":
    main()
