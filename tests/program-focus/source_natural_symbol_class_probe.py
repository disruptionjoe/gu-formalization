#!/usr/bin/env python3
"""Exact Clifford controls for the 18-generator symbol module.

No dense spin matrices, spectral approximations or action coefficients.
Completeness is proved in result.md; this checks its concrete algebra and
dimension discriminators in both real signatures. Run local verification serially.
"""
from fractions import Fraction as Q
import argparse
import json


def add(*parts):
    out = {}
    for part in parts:
        for key, value in part.items():
            out[key] = out.get(key, Q(0)) + value
            if not out[key]:
                del out[key]
    return out


def scale(part, coefficient):
    return {key: value * coefficient for key, value in part.items() if value * coefficient}


def blade_mul(a, b, eta):
    sign = 1
    for i in range(len(eta)):
        if (a >> i) & 1:
            if (b & ((1 << i) - 1)).bit_count() % 2:
                sign = -sign
            if (b >> i) & 1:
                sign *= eta[i]
    return a ^ b, sign


def cmul(left, right, eta):
    out = {}
    for a, x in left.items():
        for b, y in right.items():
            mask, sign = blade_mul(a, b, eta)
            out = add(out, {mask: x * y * sign})
    return out


def rank(columns):
    pivots = {}
    for column in columns:
        work = dict(column)
        while work:
            pivot = min(work)
            if pivot not in pivots:
                pivots[pivot] = scale(work, Q(1) / work[pivot])
                break
            work = add(work, scale(pivots[pivot], -work[pivot]))
    return len(pivots)


I = {0: Q(1)}


def block_entry(out, row, col, cliff):
    for mask, value in cliff.items():
        key = row, col, mask
        out[key] = out.get(key, Q(0)) + value
        if not out[key]:
            del out[key]


def symbols(eta, xi):
    n = len(eta)
    # One-form coefficients are metric-raised coordinates, so Gamma=sum gamma_a z_a,
    # J_a=eta_a gamma_a, x_a=delta_ai, i_x z=eta_i z_i. Do not mix this with
    # covector-coordinate insertion eta_i delta_ai and unraised contraction.
    gamma = [{1 << j: Q(1)} for j in range(n)]
    J = [scale(gamma[j], eta[j]) for j in range(n)]
    cx = gamma[xi]
    out = [{} for _ in range(9)]
    for a in range(n):
        for b in range(n):
            if a == b:
                block_entry(out[0], a, b, cx)
            if a == xi:
                block_entry(out[1], a, b, gamma[b])
            if b == xi:
                block_entry(out[2], a, b, scale(J[a], eta[xi]))
            block_entry(out[3], a, b, cmul(cmul(J[a], cx, eta), gamma[b], eta))
        if a == xi:
            block_entry(out[4], a, n, I)
        block_entry(out[5], a, n, cmul(J[a], cx, eta))
    for b in range(n):
        if b == xi:
            block_entry(out[6], n, b, scale(I, eta[xi]))
        block_entry(out[7], n, b, cmul(cx, gamma[b], eta))
    block_entry(out[8], n, n, cx)
    omega = {(1 << n) - 1: Q(1)}
    partners = []
    for entry in out:
        partner = {}
        for (a, b, mask), value in entry.items():
            block_entry(partner, a, b, cmul({mask: value}, omega, eta))
        partners.append(partner)
    return out + partners


def full_vector(symbols_at_x):
    return {(x, *key): value for x, entry in enumerate(symbols_at_x) for key, value in entry.items()}


def gradient(entry, xi, eta):
    # Input is zeta=x^flat u, nu=0. Only NW output is checked.
    n = len(eta)
    return {(a, mask): value for (a, b, mask), value in entry.items() if b == xi and a < n}


def leakage(entry, n, h=4):
    # Hidden input: normal one-form; observed output: horizontal plus scalar.
    return {key: value for key, value in entry.items()
            if h <= key[1] < n and (key[0] < h or key[0] == n)}


def run_signature(p, q, mutation=None):
    n, h = p + q, 4
    # First four entries have the required Lorentz (3,1) horizontal signature.
    eta = [1, 1, 1, -1] + [1] * (p - 3) + [-1] * (q - 1)
    omega = {(1 << n) - 1: Q(1)}
    gammas = [{1 << j: Q(1)} for j in range(n)]
    controls = 0
    def check(predicate, label):
        nonlocal controls
        assert predicate, (p, q, label)
        controls += 1

    check(cmul(omega, omega, eta) == I, "Omega squared")
    for a in range(n):
        for b in range(n):
            anticommutator = add(cmul(gammas[a], gammas[b], eta), cmul(gammas[b], gammas[a], eta))
            check(anticommutator == scale(I, 2 * eta[a]) if a == b else not anticommutator,
                  "Clifford anticommutator")
        check(not add(cmul(omega, gammas[a], eta), cmul(gammas[a], omega, eta)), "Omega parity")
    normal_right_inverse = {}
    for a in range(h, n):
        normal_right_inverse = add(normal_right_inverse, scale(cmul(gammas[a], gammas[a], eta), Q(eta[a], n - h)))
    check(normal_right_inverse == I, "Gamma_N J_N / m = I")

    all_x = [symbols(eta, x) for x in range(n)]
    columns = [full_vector([sx[k] for sx in all_x]) for k in range(18)]
    if mutation == "drop_omega":
        columns = columns[:9]
    if mutation == "drop_extra_cross":
        columns = [c for k, c in enumerate(columns) if k not in (5, 7, 14, 16)]
    check(rank(columns) == 18, "complete eighteen independent arrows")

    # Every full generator has the auxiliary odd total grade, not a claimed
    # physical chirality: G=diag(Omega on one-forms, -Omega on scalar).
    for x in (0, 3, 4):
        for entry in all_x[x]:
            defect = {}
            for (a, b, mask), value in entry.items():
                left = scale(cmul(omega, {mask: value}, eta), -1 if a == n else 1)
                right = scale(cmul({mask: value}, omega, eta), -1 if b == n else 1)
                block_entry(defect, a, b, add(left, right))
            check(not defect, "auxiliary odd grade")

    # Kernel of the NW gradient map: (a+b)=0, (c+d)=0 per input half.
    nw = [0, 1, 2, 3, 9, 10, 11, 12]
    gradient_columns = [full_vector([gradient(sx[k], x, eta) for x, sx in enumerate(all_x)]) for k in nw]
    check(rank(gradient_columns) == 4, "four independent gradient constraints")
    for x, sx in enumerate(all_x):
        for a, b in ((0, 1), (2, 3), (9, 10), (11, 12)):
            check(not gradient(add(sx[a], scale(sx[b], -1)), x, eta), "exterior NW generator")

    # Ordinary literal descent has exactly six independent conditions:
    # b=d=k=0, separately in each half. This corroborates Nov11 and certifies
    # the independent Omega partners; it is not claimed as a new fixture.
    leak_columns = [full_vector([leakage(all_x[x][k], n) for x in range(h)]) for k in range(18)]
    check(rank(leak_columns) == 6, "six independent literal-leak constraints")
    active = {k for k, col in enumerate(leak_columns) if col}
    check(active == {1, 3, 7, 10, 12, 16}, "exact literal-leak support")

    exterior = [add(columns_[a], scale(columns_[b], -1))
                for columns_ in [[full_vector([sx[k] for sx in all_x]) for k in range(18)]]
                for a, b in ((0, 1), (2, 3), (9, 10), (11, 12))]
    exterior += [full_vector([sx[k] for sx in all_x]) for k in (4, 5, 6, 7, 8, 13, 14, 15, 16, 17)]
    check(rank(exterior) == 14, "complete exterior submodule dimension")

    # Exact principal kernel witness: if a=0 on one half, every normal
    # gamma-traceless input is killed at tangent x. Use the universal normal
    # projector P_N=I-J_N Gamma_N/m, no random spinor or action coefficient.
    for x in (0, 3):
        sx = all_x[x]
        for source_slot in range(h, n):
            projected = {}
            for a in range(h, n):
                projected[a] = add(I if a == source_slot else {},
                    scale(cmul(gammas[a], gammas[source_slot], eta), Q(-eta[a], n-h)))
            for k in range(1, 9):
                # All arrows except c_x Id annihilate K_R; includes both
                # omitted cross-arrow types and arbitrary southeast.
                output = {}
                for (a, b, mask), value in sx[k].items():
                    if b in projected:
                        for outmask, outvalue in cmul({mask: value}, projected[b], eta).items():
                            key = a, outmask
                            output[key] = output.get(key, Q(0)) + outvalue
                            if not output[key]:
                                del output[key]
                check(not output, "only NW Dirac coefficient acts on normal gamma-kernel")

    # Dimension core is a consequence of the proved kernel containment, not
    # a substitute for it. Independent Clifford right inverse above supplies
    # the normal contraction's surjectivity.
    s = 1 << (n // 2)
    check((n + 1) * s - (n - h - 1) * s == (h + 2) * s == 768, "rank-nullity consequence")
    return {"signature": [p, q], "controls": controls,
            "full_module_rank": 18, "exterior_rank": 14,
            "literal_leak_rank": 6, "minimum_output_rank": 768}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=["drop_omega", "drop_extra_cross"])
    args = parser.parse_args()
    reports = [run_signature(7, 7, args.mutation), run_signature(9, 5, args.mutation)]
    print(json.dumps({"status": "passed", "signatures": reports}, indent=2))
