#!/usr/bin/env python3
"""K241: exact common-anchor atlas for K231's variable quartic coefficient."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
import json
from math import prod

from k225_order_six_diagonal_cancellation import K185, ROOT, terms
from k240_order_six_common_anchor_shell import K239, OUT as K240

OUT = ROOT / "lab/process/k241-order-six-quartic-coefficient-atlas.json"
PAIRS = tuple(combinations(range(2, 8), 2))
GRID = 8
HALF_WIDTH = Q(1, 4)
HEADROOM = Q(17933, 10**26)


def convolution(left: list[Q], right: list[Q]) -> list[Q]:
    return [sum((left[i] * right[k-i] for i in range(k+1)), Q())
            for k in range(5)]


def symbolic_groups(items: list[tuple[int, tuple[int, ...]]]):
    """Group identical pair-projected rational functions before bounding."""
    groups = defaultdict(int)
    for weight, masks in items:
        for pair in PAIRS:
            signature = tuple(sorted((
                int(bool(masks[0] & (1 << i))),
                int(bool(masks[1] & (1 << i))),
                256 + sum(bool(masks[j] & (1 << i)) for j in range(2, 8)),
                sum(bool(masks[j] & (1 << i)) for j in pair),
            ) for i in range(14)))
            groups[signature] += weight
    return tuple((signature, weight) for signature, weight in groups.items()
                 if weight)


def coefficient_jet(signature, u: Q, v: Q) -> tuple[Q, ...]:
    """Return [h^4] of f, f_u, f_v, f_uu, f_uv and f_vv exactly."""
    f = [Q(1)] + [Q()] * 4
    fu = [Q()] * 5
    fv = [Q()] * 5
    fuu = [Q()] * 5
    fuv = [Q()] * 5
    fvv = [Q()] * 5
    for nu, nv, constant, nh in signature:
        a = constant + nu*u + nv*v
        r = [Q((-nh)**k, a**(k+1)) for k in range(5)]
        ru = [-Q((k+1)*nu, a) * r[k] for k in range(5)]
        rv = [-Q((k+1)*nv, a) * r[k] for k in range(5)]
        ruu = [Q((k+1)*(k+2)*nu*nu, a*a) * r[k] for k in range(5)]
        ruv = [Q((k+1)*(k+2)*nu*nv, a*a) * r[k] for k in range(5)]
        rvv = [Q((k+1)*(k+2)*nv*nv, a*a) * r[k] for k in range(5)]
        new_f = convolution(f, r)
        new_fu = [x+y for x, y in zip(convolution(fu, r), convolution(f, ru))]
        new_fv = [x+y for x, y in zip(convolution(fv, r), convolution(f, rv))]
        new_fuu = [x+2*y+z for x, y, z in
                   zip(convolution(fuu, r), convolution(fu, ru), convolution(f, ruu))]
        new_fuv = [x+y+z+t for x, y, z, t in
                   zip(convolution(fuv, r), convolution(fu, rv),
                       convolution(fv, ru), convolution(f, ruv))]
        new_fvv = [x+2*y+z for x, y, z in
                   zip(convolution(fvv, r), convolution(fv, rv), convolution(f, rvv))]
        f, fu, fv, fuu, fuv, fvv = (
            new_f, new_fu, new_fv, new_fuu, new_fuv, new_fvv)
    return tuple(series[4] for series in (f, fu, fv, fuu, fuv, fvv))


def signed_jet(groups, u: Q, v: Q) -> tuple[Q, ...]:
    total = [Q()] * 6
    for signature, weight in groups:
        values = coefficient_jet(signature, u, v)
        for index, value in enumerate(values):
            total[index] += Q(weight, len(PAIRS)) * value
    return tuple(total)


def absolute_hessian(groups, u: Q, v: Q) -> tuple[Q, Q, Q]:
    total = [Q()] * 3
    for signature, weight in groups:
        values = coefficient_jet(signature, u, v)
        for index, value in enumerate(values[3:]):
            # Total h degree and total u/v derivative degree are both even,
            # so each per-function second derivative coefficient is positive.
            assert value >= 0
            total[index] += Q(abs(weight), len(PAIRS)) * value
    return tuple(total)


def atlas(groups):
    buu, buv, bvv = absolute_hessian(groups, Q(1), Q(1))
    remainder = (buu/2 + buv + bvv/2) * HALF_WIDTH**2
    cells = []
    for i in range(GRID):
        for j in range(GRID):
            center_u = Q(1) + HALF_WIDTH * (2*i + 1)
            center_v = Q(1) + HALF_WIDTH * (2*j + 1)
            value, du, dv, *_ = signed_jet(groups, center_u, center_v)
            radius = abs(du)*HALF_WIDTH + abs(dv)*HALF_WIDTH + remainder
            cells.append((value-radius, value+radius))
    lower = min(x[0] for x in cells)
    upper = max(x[1] for x in cells)
    assert lower > 0
    payload = "\n".join(f"{lo}|{hi}" for lo, hi in cells).encode()
    return lower, upper, remainder, sha256(payload).hexdigest(), cells


def raw_remainder_majorant(items) -> Q:
    """Uniform raw-term fifth-order remainder on the full q=5 cube."""
    total = Q()
    for weight, masks in items:
        loads = [256 + sum(bool(masks[j] & (1 << i)) for j in range(8))
                 for i in range(14)]
        base_value = Q(abs(weight), prod(loads))
        radial_load = sum((Q(4 * sum(bool(masks[j] & (1 << i))
                                     for j in range(2, 8)), loads[i])
                           for i in range(14)), Q())
        total += base_value * radial_load**5
    return total


def generate():
    items = list(terms(json.loads(K185.read_text())))
    assert len(items) == 1864 and len(PAIRS) == 15
    groups = symbolic_groups(items)
    assert len(groups) == 585
    lower, upper, remainder, atlas_sha, cells = atlas(groups)

    # For q=5, M0=sinh(log 5)=12/5 and M2=M0+M0^3/3. Since
    # D=M0*M2-M1^2 <= M0*M2, K5=15 D^2 M0^2 has this rational upper.
    m0 = Q(12, 5)
    m2 = m0 + m0**3/3
    k5_upper = 15 * (m0*m2)**2 * m0**2
    normalization_upper = Q(2**8 * 256**6, 120) * Q(10, 31)**8
    quartic_shell_upper = normalization_upper * upper * k5_upper * m0**2
    assert quartic_shell_upper < HEADROOM
    raw_r5_upper = normalization_upper * raw_remainder_majorant(items) * m0**8
    assert raw_r5_upper > HEADROOM
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {
            "k185": sha256(K185.read_bytes()).hexdigest(),
            "k239": sha256(K239.read_bytes()).hexdigest(),
            "k240": sha256(K240.read_bytes()).hexdigest(),
        },
        "object": "K231 quartic coefficient A_b(u,v) of the S6-projected signed K185/K218 rational-cosh core, at the common K240 anchor b=1",
        "domain": {"u": [1, 5], "v": [1, 5], "anchor_b": 1},
        "raw_signed_terms": len(items),
        "projected_pairs": len(PAIRS),
        "nonzero_symbolic_groups": len(groups),
        "atlas": {
            "grid": [GRID, GRID],
            "cell_half_width": str(HALF_WIDTH),
            "global_lower": str(lower),
            "global_upper": str(upper),
            "global_lower_decimal": f"{float(lower):.12e}",
            "global_upper_decimal": f"{float(upper):.12e}",
            "common_second_order_remainder": str(remainder),
            "cell_bounds_sha256": atlas_sha,
            "cells": len(cells),
        },
        "theorem": "For every u,v in [1,5], the common-anchor coefficient obeys the displayed exact positive interval. Each of the 1,864 signed terms is averaged over fifteen exceptional coordinate pairs and combined into 585 identical symbolic rational functions before differentiation. On each unit square, exact value and gradient at the center are enclosed by Taylor's theorem. For every grouped positive reciprocal product, the absolute uu, uv and vv derivatives of its h^4 coefficient are coordinatewise decreasing on the positive orthant; their signed-weight absolute sum at (1,1) therefore bounds every cell Hessian. The exact lower endpoint is positive. This is a covered coefficient theorem, not sampling.",
        "quartic_shell": {
            "pi_lower": "31/10",
            "k5_upper": str(k5_upper),
            "headroom": str(HEADROOM),
            "upper": str(quartic_shell_upper),
            "upper_decimal": f"{float(quartic_shell_upper):.12e}",
            "fraction_of_headroom": f"{float(quartic_shell_upper/HEADROOM):.12e}",
            "argument": "K240's positive quartic shell is at most C*Amax*K5*measure(U^2). Dropping the negative K4 low-cube subtraction only enlarges it. Here measure([0,log 5])=sinh(log 5)=12/5, K5=15*(M0*M2-M1^2)^2*M0^2 <=15*(M0*M2)^2*M0^2 with M2=M0+M0^3/3, and pi>31/10.",
        },
        "raw_remainder_discriminator": {
            "full_q5_cube_upper": str(raw_r5_upper),
            "full_q5_cube_upper_decimal": f"{float(raw_r5_upper):.12e}",
            "multiple_of_headroom": f"{float(raw_r5_upper/HEADROOM):.12e}",
            "result": "fails_budget",
            "argument": "For every raw reciprocal product, Taylor along the six-coordinate ray from b=1 has fifth remainder at most q(0)*(sum_i r_i)^5 because all loads increase. Use u=v=1 and all six deviations <=4 for a uniform worst case, sum absolute raw weights, and multiply by the full q=5 eight-coordinate measure. This is rigorous but discards the signed grouping needed for R_1.",
        },
        "required_next_certificate": "Certify the signed same-anchor R_1 integral directly on U^8 minus L^8 below the residual K224 allocation. Do not spend further work on the quartic coefficient unless a tighter remainder composition explicitly needs it.",
        "source_routing": "SC-ACT-01/02 ASSERTS; SC-META-53 UNCERTAIN; LT-GR6b/LT-SM8 NEEDS. This remains internal integration algebra.",
        "claim_ceiling": "Exact positive A_1 atlas and rigorous complete quartic-shell upper only. No sign or bound for the same-anchor R_1 integral, complete signed third-shell upper, K215 prefix, source action/state, ledger, canon or public-posture change.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K241 exact quartic-coefficient atlas", result["atlas"]["global_lower_decimal"], result["atlas"]["global_upper_decimal"])
    print("[PASS] K241 complete quartic shell upper", result["quartic_shell"]["upper_decimal"], result["quartic_shell"]["fraction_of_headroom"])
