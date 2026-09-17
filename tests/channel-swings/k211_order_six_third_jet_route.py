#!/usr/bin/env python3
"""K211: exact 28-node third-remainder geometry and full signed angular jets."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path

from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
FILES = {key: P / f"k{key}-order-six-{suffix}.json" for key, suffix in (
    (184, "certified-low-rank-wave"), (185, "duffy-face-tail-wave"),
    (203, "positive-moment-rule"), (204, "core-moment-defect"),
    (205, "radial-normal-form"),
    (206, "angular-jets"), (209, "cubic-core-geometry"),
)}
OUT = P / "k211-order-six-third-jet-route.json"
ctx.dps = 100
ctx.threads = 1


def rational_sqrt_upper(value: F, denominator: int = 10**12) -> F:
    """Smallest multiple of 1/denominator above sqrt(value), integer only."""
    n = math.isqrt(value.numerator * denominator**2 // value.denominator) + 1
    result = F(n, denominator)
    assert result**2 > value and (result-F(1, denominator))**2 <= value
    return result


def geometry():
    prior = json.loads(FILES[209].read_text())
    lost = F(prior["lost_mass_upper"])
    r2 = F(39, 238)  # E||z-c||^2, also every K203 angular node's radius squared.
    r4 = F(prior["centered_euclidean_fourth_reference"])
    a = rational_sqrt_upper(r2*r4)
    b = rational_sqrt_upper(r2)
    third_upper = (a/(1-lost) + r2*b)/6
    fourth_upper = F(prior["conditional_taylor_remainder_coefficient_upper"])
    # The cubic witness is z_0^3. K203's one-hot orbit has a radical third
    # centered moment; the Dirichlet reference has the exact rational 1/170.
    theta_lo = F(42008402520, 10**11)
    theta_hi = F(42008402521, 10**11)
    assert theta_lo**2 < F(3, 17) < theta_hi**2
    base = F(1, 14)**3 + 3*F(1, 14)*F(39, 238)/14
    cubic_lo = base + F(39, 686)*theta_lo**3 - F(1, 170)
    cubic_hi = base + F(39, 686)*theta_hi**3 - F(1, 170)
    assert 0 < cubic_lo < cubic_hi
    return {
        "centered_second_reference_and_rule": str(r2),
        "centered_fourth_reference": str(r4),
        "reference_third_moment_cauchy_upper": str(a),
        "rule_third_moment_upper": str(r2*b),
        "conditional_third_taylor_coefficient_upper": str(third_upper),
        "conditional_fourth_taylor_coefficient_upper_K209": str(fourth_upper),
        "fourth_over_third_coefficient": str(fourth_upper/third_upper),
        "cubic_z0_rule_minus_reference_open_interval": [str(cubic_lo), str(cubic_hi)],
        "theta_open_interval": [str(theta_lo), str(theta_hi)],
        "core_lost_mass_upper": str(lost),
    }


class Jet:
    def __init__(self, cells):
        self.d = tuple(cells)

    def __add__(self, other):
        return Jet([x+y for x, y in zip(self.d, other.d)])

    def __neg__(self):
        return Jet([-x for x in self.d])

    def __mul__(self, other):
        return Jet([sum((math.comb(n, i)*self.d[i]*other.d[n-i]
                         for i in range(n+1)), arb(0)) for n in range(4)])


ZERO = Jet([arb(0)]*4)
ONE = Jet([arb(1), arb(0), arb(0), arb(0)])


def determinant(matrix):
    result = ZERO
    for p in itertools.permutations(range(len(matrix))):
        term = ONE
        for i, j in enumerate(p):
            term = term*matrix[i][j]
        if sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2:
            term = -term
        result = result+term
    return result


def samples():
    theta = (arb(3)/17).sqrt()
    rho = (7-arb(7).sqrt())/256
    for special, first, last in ((0, 0, 13), (7, 6, 7)):
        z = [(1-theta)/14+(theta if i == special else 0) for i in range(14)]
        v = [arb(int(i == first)-int(i == last)) for i in range(14)]
        yield f"radial-minus|angular-{special}|direction-{first}-{last}", rho, z, v


def evaluate(entries, rho, z, v):
    tails = {}
    for side in range(2):
        for pos in range(1, 8):
            start = 7*side+pos-1
            tails[side, pos] = (sum(z[start:7*(side+1)], arb(0)),
                                 sum(v[start:7*(side+1)], arb(0)))
    cache = {}

    def h(s, t):
        key = (str(s), str(t))
        if key not in cache:
            x = rho*s
            k0, k1 = x.bessel_k(0), x.bessel_k(1)
            cache[key] = Jet((
                2*rho*k1,
                -2*rho**2*t*(k0+k1/x),
                2*rho**3*t**2*(k1+k0/x+2*k1/x**2),
                -2*rho**4*t**3*(k0*(1+3/x**2)+k1*(2/x+6/x**3)),
            ))
        return cache[key]

    def old(side, pos):
        return h(*tails[side, pos])

    def factor(left, right):
        s0, t0 = tails[0, left]
        s1, t1 = tails[1, right]
        return h(s0+s1, t0+t1)

    pref = math.prod((x**(arb(2)/3) for x in z), start=arb(1))/(2*arb.pi())**8
    l1 = arb(2)/3*sum((d/x for d, x in zip(v, z)), arb(0))
    l2 = -arb(2)/3*sum((d**2/x**2 for d, x in zip(v, z)), arb(0))
    l3 = arb(4)/3*sum((d**3/x**3 for d, x in zip(v, z)), arb(0))
    weight = Jet((pref, pref*l1, pref*(l1*l1+l2),
                  pref*(l1**3+3*l1*l2+l3)))
    groups = defaultdict(lambda: ZERO)
    for row in entries:
        value = weight*old(0, row["left_old_position"])*old(1, row["right_old_position"])
        for species in row["species_kernels"]:
            matrix = [[factor(i, j) for j in species["right_time_positions"]]
                      for i in species["left_time_positions"]]
            value = value*determinant(matrix)
        coefficient = row["coefficient_product"]*(1 if row["left"] == row["right"] else 2)
        groups[row["group_id"]] = groups[row["group_id"]]+Jet(
            [coefficient*x for x in value.d])
    return groups


def generate():
    native = json.loads(FILES[184].read_text())
    entries = native["andreief_time_gram_certificate"]["gram_entries"]
    assert len(entries) == 234
    prior = json.loads(FILES[206].read_text())
    radial = json.loads(FILES[205].read_text())
    radial_upper = F(radial["all_groups_radial_only_error_upper_rational"])
    assert radial_upper < F(4633, 10**11)  # 4.633e-8, not a lower error floor.
    nodes = {}
    for label, rho, z, v in samples():
        groups = evaluate(entries, rho, z, v)
        assert set(groups) == set(prior["nodes"][label]) and len(groups) == 18
        for key, jet in groups.items():
            for i, field in enumerate(("value_arb", "first_arb", "second_arb")):
                assert abs(jet.d[i]-arb(prior["nodes"][label][key][field].split(" +/- ")[0][1:])) < arb("1e-55")
        nodes[label] = {key: {"d3v_arb": str(jet.d[3])} for key, jet in sorted(groups.items())}
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {str(k): hashlib.sha256(path.read_bytes()).hexdigest()
                         for k, path in FILES.items()},
        "geometry": geometry(),
        "counts": {"gram_entries": 234, "coherent_groups": 18,
                   "signed_leibniz_terms": 1864, "factor_occurrences": 14912},
        "nodes": nodes,
        "factor_third": "D_v^3[2*rho*K1(rho*S)]=-2*rho^4*(D_v S)^3*[K0(x)*(1+3/x^2)+K1(x)*(2/x+6/x^3)]",
        "prefactor_log_third": "D_v^3 log P=(4/3)*sum_i v_i^3/z_i^3",
        "claim_ceiling": "exact conditional third-remainder geometry, nonzero cubic discrepancy and full signed third point jets; no global cellwise enclosure, accurate integral, source or physics effect",
        "separate_radial_only_error_upper_rational_K205": str(radial_upper),
        "unchanged_full_domain_error_rational": json.loads(FILES[209].read_text())["unchanged_full_domain_error_rational"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2)+"\n")
    print("[PASS] third geometry, cubic witness; 18 signed groups x two full third jets")
    print("third coefficient <", float(F(result["geometry"]["conditional_third_taylor_coefficient_upper"])))
