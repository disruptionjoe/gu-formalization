#!/usr/bin/env python3
"""K210 exact stick-breaking density and multivariate chain (no signed error)."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
SOURCES = {k: P / f"k{k}-order-six-{name}.json" for k, name in (
    (185, "duffy-face-tail-wave"), (203, "positive-moment-rule"),
    (208, "cubic-moment-rule"), (209, "cubic-core-geometry"))}
OUT = P / "k210-order-six-duffy-chain.json"
N = 14


def chart(u):
    remaining = F(1)
    z = []
    for x in u:
        z.append(remaining * x)
        remaining *= 1 - x
    return z + [remaining]


def chart_partial(u, indices):
    """Exact derivative of z in selected stick coordinates; repeated => zero."""
    if len(indices) != len(set(indices)):
        return [F(0)] * N
    chosen = set(indices)
    result = []
    for k in range(N):
        if any(i > k or (i == k and k == N-1) for i in chosen):
            result.append(F(0))
            continue
        value = F(1)
        for i in range(k):
            value *= -1 if i in chosen else 1-u[i]
        if k < N-1:
            value *= 1 if k in chosen else u[k]
        result.append(value)
    return result


def partitions(items):
    """Set partitions of derivative-slot positions, not stick-coordinate values."""
    if not items:
        yield ()
        return
    first, *rest = items
    for tail in partitions(rest):
        yield ((first,),) + tail
        for j in range(len(tail)):
            blocks = list(tail)
            blocks[j] = (first,) + blocks[j]
            yield tuple(blocks)


def tensor_monomial(z, factors, directions):
    """Symmetric derivative of a coordinate monomial by labelled product rule."""
    if len(directions) > len(factors):
        return F(0)
    total = F(0)
    for slots in itertools.permutations(range(len(factors)), len(directions)):
        chosen = dict(enumerate(slots))
        term = F(1)
        for a, coordinate in enumerate(factors):
            hits = [directions[b][coordinate] for b, slot in chosen.items() if slot == a]
            term *= hits[0] if hits else z[coordinate]
        total += term
    return total


def composed_partial(u, indices, polynomial):
    z = chart(u)
    value = F(0)
    for blocks in partitions(tuple(range(len(indices)))):
        vectors = [chart_partial(u, tuple(indices[j] for j in block))
                   for block in blocks]
        if any(not any(v) for v in vectors):
            continue
        value += sum((coefficient*tensor_monomial(z, factors, vectors)
                      for coefficient, factors in polynomial), F(0))
    return value


def density_exponents(beta):
    """Powers of u_j and 1-u_j after multiplying simplex density by Jacobian."""
    assert len(beta) == N and min(beta) >= F(1, 3)
    return [(beta[j]-1, sum(beta[j+1:], F(0))-1) for j in range(N-1)]


def generate():
    old = json.loads(SOURCES[185].read_text())
    catalog = old["exact_allocation_certificate"]["allocation_catalog"]
    assert len(catalog) == 1276
    for record in catalog.values():
        beta = [1-F(s) for s in record["loads"].split(",")]
        assert sum(beta) == 6
        density_exponents(beta)
    common = density_exponents([F(1, 3)]*N)
    # Disjoint derivative-slot patterns distinguish pure from mixed pullbacks.
    u = [F(i+2, 2*i+17) for i in range(N-1)]
    polynomial = [(F(1), (0, 0, 0, 0)), (F(-3), (2, 5)),
                  (F(2), (13, 13)), (F(1), (1, 3, 8))]
    patterns = ((0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 1),
                (0, 1, 2, 3), (2, 5, 8, 12))
    controls = {"-".join(map(str, p)): str(composed_partial(u, p, polynomial))
                for p in patterns}
    counts = Counter(len(p) for p in partitions(tuple(range(4))))
    assert [counts[k] for k in range(1, 5)] == [1, 7, 6, 1]
    for length in range(1, 5):
        for indices in itertools.combinations(range(13), length):
            vec = chart_partial(u, indices)
            assert sum(vec) == 0
            assert sum(map(abs, vec)) <= 2**length
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {str(k): hashlib.sha256(path.read_bytes()).hexdigest()
                         for k, path in SOURCES.items()},
        "chart": "z_j=u_j product_{i<j}(1-u_i), j=1..13; z_14=product_{i<=13}(1-u_i)",
        "jacobian": "product_{j=1}^{13}(1-u_j)^(13-j)",
        "term_specific_allocation_count": len(catalog),
        "common_beta_parameters": ["1/3"]*N,
        "common_stick_exponents_u_then_one_minus_u": [list(map(str, p)) for p in common],
        "chain": "D_{i1}...D_{im}(f o z)=sum_{partitions pi of labelled slots} D^|pi|f(z)[D_{i_B}z for B in pi]; any block repeating a stick index is zero",
        "fourth_set_partition_counts_by_outer_derivative_order": {str(k): counts[k] for k in range(1, 5)},
        "fourth_mixed_chart_bound": "16*(M1+7*M2+6*M3+M4), Mk=sup ||D^k f||_2 on chart image; conservative |D_B z|_2<=2^|B|",
        "fourth_pure_stick_bound": "4*M4 since z is affine in each u_i and ||D_i z||_2<=sqrt(2)",
        "rational_test_sticks": [str(x) for x in u],
        "rational_test_polynomial": [[str(c), list(f)] for c, f in polynomial],
        "rational_fourth_partial_controls": controls,
        "unchanged_full_domain_error_rational": json.loads(SOURCES[208].read_text())["all_group_absolute_error_ceiling_rational"],
        "remaining_gate": "Complete normalized/coalescent signed D1..D4 on outward core cells, including chart mixed lower-order terms, K185/K188 distinct termwise face/tail, and coherent-group allocation; common-reference moments alone are insufficient.",
        "claim_ceiling": "exact 13-stick Jacobian/Dirichlet factorization and fourth-order multivariate chain, tested on rational polynomial controls; not a signed K184 derivative enclosure, accurate prefix or physics/source result",
    }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2)+"\n")
    print("[PASS] 1276 term weights, 13-stick density and fourth-order chain")
