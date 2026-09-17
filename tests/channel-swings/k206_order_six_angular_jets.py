#!/usr/bin/env python3
"""K206 determinant-preserving tangent angular jets of the K184 signed Gram."""
from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
import hashlib
import itertools
import json
import math
from pathlib import Path

from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[2]
K184 = ROOT / "lab/process/k184-order-six-certified-low-rank-wave.json"
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K203 = ROOT / "lab/process/k203-order-six-positive-moment-rule.json"
K205 = ROOT / "lab/process/k205-order-six-radial-normal-form.json"
OUT = ROOT / "lab/process/k206-order-six-angular-jets.json"
ctx.dps = 100
ctx.threads = 1


@dataclass(frozen=True)
class Jet:
    value: arb
    first: arb
    second: arb

    def __mul__(self, other: "Jet") -> "Jet":
        return Jet(self.value * other.value,
                   self.first * other.value + self.value * other.first,
                   self.second * other.value + 2 * self.first * other.first
                   + self.value * other.second)

    def __add__(self, other: "Jet") -> "Jet":
        return Jet(self.value + other.value, self.first + other.first,
                   self.second + other.second)

    def __neg__(self) -> "Jet":
        return Jet(-self.value, -self.first, -self.second)


ONE = Jet(arb(1), arb(0), arb(0))
ZERO = Jet(arb(0), arb(0), arb(0))


def determinant(matrix: list[list[Jet]]) -> Jet:
    n = len(matrix)
    result = ZERO
    for p in itertools.permutations(range(n)):
        term = ONE
        for i, j in enumerate(p):
            term = term * matrix[i][j]
        if sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n)) % 2:
            term = -term
        result = result + term
    return result


def samples():
    theta = (arb(3) / 17).sqrt()
    root = arb(7).sqrt()
    rho = (7 - root) / 256
    for special, first, last in [(0, 0, 13), (7, 6, 7)]:
        z = [(1 - theta) / 14 + (theta if i == special else 0)
             for i in range(14)]
        v = [arb(int(i == first) - int(i == last)) for i in range(14)]
        yield f"radial-minus|angular-{special}|direction-{first}-{last}", rho, z, v


def evaluate(entries, rho, z, v) -> dict[str, Jet]:
    # T_i and U_j are original ordered-time tails.  The tangent direction
    # satisfies sum(v)=0, so all derivatives stay on the simplex hyperplane.
    tails = {}
    for side in range(2):
        for position in range(1, 8):
            start = 7 * side + position - 1
            end = 7 * (side + 1)
            tails[(side, position)] = (sum(z[start:end], arb(0)),
                                       sum(v[start:end], arb(0)))

    cache: dict[tuple[str, str], Jet] = {}

    def h(s, t):
        key = (str(s), str(t))
        if key not in cache:
            x = rho * s
            k0, k1 = x.bessel_k(0), x.bessel_k(1)
            cache[key] = Jet(2 * rho * k1,
                             -2 * rho**2 * t * (k0 + k1 / x),
                             2 * rho**3 * t**2 * (k1 + k0 / x + 2 * k1 / x**2))
        return cache[key]

    def factor(left, right):
        s = tails[(0, left)][0] + tails[(1, right)][0]
        t = tails[(0, left)][1] + tails[(1, right)][1]
        return h(s, t)

    def old(side, position):
        s, t = tails[(side, position)]
        return h(s, t)

    angular = math.prod((x ** (arb(2) / 3) for x in z), start=arb(1))
    log1 = arb(2) / 3 * sum((d / x for d, x in zip(v, z)), arb(0))
    log2 = -arb(2) / 3 * sum((d**2 / x**2 for d, x in zip(v, z)), arb(0))
    prefactor = angular / (2 * arb.pi()) ** 8
    weight = Jet(prefactor, prefactor * log1, prefactor * (log1**2 + log2))
    groups = defaultdict(lambda: ZERO)
    for row in entries:
        value = weight * old(0, row["left_old_position"])
        value = value * old(1, row["right_old_position"])
        for species in row["species_kernels"]:
            matrix = [[factor(i, j) for j in species["right_time_positions"]]
                      for i in species["left_time_positions"]]
            value = value * determinant(matrix)
        coefficient = row["coefficient_product"] * (1 if row["left"] == row["right"] else 2)
        if coefficient == -1:
            value = -value
        elif coefficient == -2:
            value = Jet(-2 * value.value, -2 * value.first, -2 * value.second)
        elif coefficient == 2:
            value = Jet(2 * value.value, 2 * value.first, 2 * value.second)
        groups[row["group_id"]] = groups[row["group_id"]] + value
    return groups


def generate():
    source = json.loads(K184.read_text())
    prior = json.loads(K203.read_text())
    radial = json.loads(K205.read_text())
    entries = source["andreief_time_gram_certificate"]["gram_entries"]
    assert len(entries) == 234 and radial["counts"]["factor_occurrences"] == 14912
    assert radial["counts"]["coherent_groups"] == len(prior["groups"]) == 18
    nodes = {}
    for label, rho, z, v in samples():
        result = evaluate(entries, rho, z, v)
        assert set(result) == set(prior["groups"])
        nodes[label] = {key: {"value_arb": str(jet.value),
                              "first_arb": str(jet.first),
                              "second_arb": str(jet.second)}
                        for key, jet in sorted(result.items())}
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest()
                         for name, path in (("K184", K184), ("K185", K185),
                                            ("K203", K203), ("K205", K205))},
        "counts": {"gram_entries": 234, "coherent_groups": 18,
                   "independent_replay_factor_occurrences": 14912},
        "normalized_factor": "h(rho,S)=2*rho*K1(rho*S); distribute rho^8 over two old kernels and six determinant rows before angular differentiation",
        "factor_jets": {
            "first": "D_v h=-2*rho^2*(D_v S)*(K0(x)+K1(x)/x), x=rho*S",
            "second": "D_v^2 h=2*rho^3*(D_v S)^2*(K1(x)+K0(x)/x+2*K1(x)/x^2)",
            "argument": "S is a K184 time-tail support sum; D_v S=sum_i(mask_i*v_i)",
            "prefactor": "P=prod_i z_i^(2/3)/(2*pi)^8; D_v log P=(2/3)sum_i v_i/z_i; D_v^2 log P=-(2/3)sum_i v_i^2/z_i^2",
            "jet_product": "(ab)''=a''b+2a'b'+ab''; determinants evaluated over this jet ring",
        },
        "nodes": nodes,
        "claim_ceiling": "exact interior first/second tangent-angular derivative algebra and independently controlled signed node jets; no global derivative supremum, face/tail composition, angular remainder, accurate order-six prefix or source/physics effect",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] 234 native Gram entries, 18 complete signed group jets at two K203 nodes")
