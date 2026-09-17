#!/usr/bin/env python3
"""K207: complete signed bivariate radial/angular jets through degree (2,2)."""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import itertools
import json
import math
from pathlib import Path

from flint import arb, ctx

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
ctx.dps = 100
ctx.threads = 1
N = 3
PAIRS = tuple(itertools.product(range(N), repeat=2))


class Jet:
    """Raw partials d_r^i d_v^j, 0<=i,j<=2, not Taylor coefficients."""

    def __init__(self, cells=None):
        self.cells = cells or {(i, j): arb(0) for i, j in PAIRS}

    def __add__(self, other):
        return Jet({key: self.cells[key] + other.cells[key] for key in PAIRS})

    def __neg__(self):
        return Jet({key: -self.cells[key] for key in PAIRS})

    def __mul__(self, other):
        result = {}
        for i, j in PAIRS:
            result[i, j] = sum((math.comb(i, a) * math.comb(j, b)
                                * self.cells[a, b] * other.cells[i-a, j-b]
                                for a in range(i+1) for b in range(j+1)), arb(0))
        return Jet(result)


ZERO = Jet()
ONE = Jet({key: arb(int(key == (0, 0))) for key in PAIRS})


def determinant(matrix):
    result = ZERO
    for p in itertools.permutations(range(len(matrix))):
        term = ONE
        for i, j in enumerate(p):
            term = term * matrix[i][j]
        if sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2:
            term = -term
        result = result + term
    return result


def factor(rho, s, t):
    x = rho * s
    k0, k1 = x.bessel_k(0), x.bessel_k(1)
    return Jet({
        (0, 0): 2*rho*k1,
        (1, 0): -2*x*k0,
        (2, 0): 2*s*(x*k1-k0),
        (0, 1): -2*rho**2*t*(k0+k1/x),
        (0, 2): 2*rho**3*t**2*(k1+k0/x+2*k1/x**2),
        (1, 1): 2*rho*t*(x*k1-k0),
        (1, 2): 2*rho**2*t**2*(k1-x*k0),
        (2, 1): 2*t*(2*x*k1-(1+x**2)*k0),
        (2, 2): 2*rho*t**2*((1+x**2)*k1-4*x*k0),
    })


def samples():
    theta = (arb(3)/17).sqrt()
    rho = (7-arb(7).sqrt())/256
    for special, first, last in ((0, 0, 13), (7, 6, 7)):
        z = [(1-theta)/14 + (theta if i == special else 0) for i in range(14)]
        v = [arb(int(i == first)-int(i == last)) for i in range(14)]
        yield f"radial-minus|angular-{special}|direction-{first}-{last}", rho, z, v


def evaluate(entries, rho, z, v):
    tails = {}
    for side in range(2):
        for position in range(1, 8):
            start = 7*side+position-1
            tails[side, position] = (sum(z[start:7*(side+1)], arb(0)),
                                     sum(v[start:7*(side+1)], arb(0)))
    cache = {}

    def kernel(s, t):
        key = (str(s), str(t))
        if key not in cache:
            cache[key] = factor(rho, s, t)
        return cache[key]

    def cross(left, right):
        s0, t0 = tails[0, left]
        s1, t1 = tails[1, right]
        return kernel(s0+s1, t0+t1)

    p = math.prod((x**(arb(2)/3) for x in z), start=arb(1))/(2*arb.pi())**8
    a = arb(2)/3 * sum((d/x for d, x in zip(v, z)), arb(0))
    b = -arb(2)/3 * sum((d*d/x**2 for d, x in zip(v, z)), arb(0))
    weight = Jet({key: (p if key == (0, 0) else
                        p*a if key == (0, 1) else
                        p*(a*a+b) if key == (0, 2) else arb(0))
                  for key in PAIRS})
    groups = defaultdict(lambda: ZERO)
    for row in entries:
        result = weight * kernel(*tails[0, row["left_old_position"]])
        result = result * kernel(*tails[1, row["right_old_position"]])
        for species in row["species_kernels"]:
            matrix = [[cross(i, j) for j in species["right_time_positions"]]
                      for i in species["left_time_positions"]]
            result = result * determinant(matrix)
        sign = row["coefficient_product"] * (1 if row["left"] == row["right"] else 2)
        if sign < 0:
            result = -result
        if abs(sign) == 2:
            result = Jet({key: 2*value for key, value in result.cells.items()})
        groups[row["group_id"]] = groups[row["group_id"]] + result
    return groups


def generate():
    entries = json.loads(FILES["K184"].read_text())["andreief_time_gram_certificate"]["gram_entries"]
    baseline = json.loads(FILES["K206"].read_text())
    assert len(entries) == 234 and len(baseline["nodes"]) == 2
    nodes = {}
    for label, rho, z, v in samples():
        groups = evaluate(entries, rho, z, v)
        assert set(groups) == set(baseline["nodes"][label]) and len(groups) == 18
        for name, jet in groups.items():
            for key, field in (((0, 0), "value_arb"), ((0, 1), "first_arb"),
                               ((0, 2), "second_arb")):
                # Arb balls must overlap their K206 independently produced values.
                old = arb(baseline["nodes"][label][name][field].split(" +/- ")[0][1:])
                assert abs(jet.cells[key]-old) < arb("1e-70")
        nodes[label] = {name: {f"d{i}r_d{j}v_arb": str(jet.cells[i, j])
                               for i, j in PAIRS}
                        for name, jet in sorted(groups.items())}
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {key: hashlib.sha256(path.read_bytes()).hexdigest()
                         for key, path in FILES.items()},
        "counts": {"gram_entries": 234, "coherent_groups": 18,
                   "mixed_partial_fields_per_group": 9,
                   "independent_replay_factor_occurrences": 14912},
        "factor": "h(rho,S)=2 rho K1(rho S); S is a positive K184 tail-support sum, D_v S=t",
        "identities": {
            "radial": "h_r=-2xK0; h_rr=2S(xK1-K0)",
            "angular": "h_v=-2rho^2 t(K0+K1/x); h_vv=2rho^3 t^2(K1+K0/x+2K1/x^2)",
            "mixed": "h_rv=2rho t(xK1-K0); h_rvv=2rho^2 t^2(K1-xK0); h_rrv=2t(2xK1-(1+x^2)K0); h_rrvv=2rho t^2((1+x^2)K1-4xK0)",
            "rule": "raw bivariate Leibniz jets with binomial coefficients through (2,2), preserved through signed native determinants",
        },
        "nodes": nodes,
        "remaining_gate": "cellwise normalized/coalescent mixed suprema on a positive Duffy/Jacobi atlas; a degree-two angular rule needs a controlled third angular Taylor remainder (or a stronger reduction), while a degree-three radial rule needs fourth radial derivatives if using a direct Peano bound rather than K205's first-derivative coupling; exact chart chain, distinct K185/K188 termwise boundary and K204 common-reference moment defects; signed-group error allocation near the true order-six scale",
        "claim_ceiling": "exact interior bidegree-(2,2) signed derivative algebra and independent point replay only; no global cellwise enclosure, complete 28-node cubature error, accurate prefix or physical/source effect",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2)+"\n")
    print("[PASS] 234 signed Gram entries, 18 groups, nine mixed fields at two nodes")
