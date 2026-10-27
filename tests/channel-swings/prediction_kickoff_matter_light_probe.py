#!/usr/bin/env python3
"""Exact conditional source/readout controls; no GU physical recovery.

All computations use Fraction. The all-nonzero-q and operator claims rest on
the accompanying written proofs. A selftest runs a clean baseline before
altering mathematical inputs/operators, and counts explicit failed checks only.
"""

from __future__ import annotations

import sys
from fractions import Fraction as F


def zeros(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in tr(b)] for row in a]


def mv(a, x):
    return [sum(u * v for u, v in zip(row, x)) for row in a]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def neg(a):
    return [[-x for x in row] for row in a]


def subvec(a, b):
    return [x - y for x, y in zip(a, b)]


def hcat(a, b):
    return [ar + br for ar, br in zip(a, b)]


def block(a, b, c, d):
    return hcat(a, b) + hcat(c, d)


def rref(a):
    a = [[F(x) for x in row] for row in a]
    row = 0
    pivots = []
    for col in range(len(a[0])):
        p = next((i for i in range(row, len(a)) if a[i][col]), None)
        if p is None:
            continue
        a[row], a[p] = a[p], a[row]
        scale = a[row][col]
        a[row] = [x / scale for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def rank(a):
    return len(rref(a)[1])


def kernel(a):
    rr, pivots = rref(a)
    n = len(a[0])
    free = [j for j in range(n) if j not in pivots]
    columns = []
    for j in free:
        v = [F(0)] * n
        v[j] = F(1)
        for i, p in enumerate(pivots):
            v[p] = -rr[i][j]
        columns.append(v)
    return tr(columns) if columns else [[] for _ in range(n)]


def inv(a):
    n = len(a)
    rr, pivots = rref(hcat(a, eye(n)))
    if pivots[:n] != list(range(n)):
        raise ValueError("attempted singular inverse")
    return [row[n:] for row in rr]


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0))
            for i in range(n)]


def poly_scale(a, scale):
    return [F(scale) * x for x in a]


def poly_derivative(a):
    return [F(i) * a[i] for i in range(1, len(a))] or [F(0)]


def poly_integral_01(a):
    return sum(x / F(i + 1) for i, x in enumerate(a))


def poly_endpoint_difference(a):
    return sum(a) - a[0]


SYM = [(a, b) for a in range(4) for b in range(a, 4)]
ALT = [(a, b) for a in range(4) for b in range(a + 1, 4)]
ETA = [-1, 1, 1, 1]


def symmetric_basis():
    out = []
    for a, b in SYM:
        h = zeros(4, 4)
        h[a][b] = h[b][a] = F(1)
        out.append(h)
    return out


def symbols(q, fault):
    basis = symmetric_basis()
    lc = zeros(64, 10)
    spin = zeros(24, 10)
    adapter = zeros(24, 10)
    for col, h in enumerate(basis):
        for rho in range(4):
            for mu in range(4):
                for nu in range(4):
                    lc[(rho * 4 + mu) * 4 + nu][col] = F(ETA[rho], 2) * (
                        q[mu] * h[nu][rho] + q[nu] * h[mu][rho] - q[rho] * h[mu][nu]
                    )
        for mu in range(4):
            for ab, (a, b) in enumerate(ALT):
                row = mu * 6 + ab
                sign = 1 if fault == "spin-sign" else -1
                spin[row][col] = (q[b] * h[mu][a] + sign * q[a] * h[mu][b]) / 2
                adapter[row][col] = ETA[a] * lc[(a * 4 + mu) * 4 + b][col]
                if fault != "coframe-drop":
                    adapter[row][col] -= q[mu] * h[a][b] / 2
    r = [[q[a] * F(b == j) + q[b] * F(a == j) for j in range(4)] for a, b in SYM]
    gs = zeros(24, 6)
    qs = zeros(6, 4)
    gc = zeros(64, 16)
    qc = zeros(16, 4)
    for mu in range(4):
        for ab in range(6):
            gs[mu * 6 + ab][ab] = q[mu]
        for rho in range(4):
            for nu in range(4):
                gc[(rho * 4 + mu) * 4 + nu][rho * 4 + nu] = q[mu]
    for ab, (a, b) in enumerate(ALT):
        for j in range(4):
            qs[ab][j] = (q[b] * F(a == j) - q[a] * F(b == j)) / 2
    for rho in range(4):
        for nu in range(4):
            qc[rho * 4 + nu][rho] = q[nu] * ETA[rho]
    return lc, spin, adapter, r, gs, qs, gc, qc


def verify(fault=None):
    failures = []
    count = 0

    def check(ok, label):
        nonlocal count
        count += 1
        if not ok:
            failures.append(label)

    for name, q0 in [("timelike", [1, 0, 0, 0]), ("spacelike", [0, 1, 0, 0]),
                     ("null", [1, 0, 0, 1])]:
        q = [F(x) for x in q0]
        lc, ls, adapter, r, gs, qs, gc, qc = symbols(q, fault)
        check(ls == adapter, name + ": moving-coframe adapter")
        check(rank(lc) == 10, name + ": inherited coordinate LC rank ten")
        check(rank(ls) == 9, name + ": inherited spin LC rank nine")
        qq = [q[a] * q[b] for a, b in SYM]
        check(mv(ls, qq) == [0] * 24, name + ": longitudinal spin kernel")
        check(rank(r) == 4, name + ": metric gauge rank four")
        check(rank(gs) == 6 and rank(qs) == 3, name + ": spin gauge and compensator ranks")
        check(mm(ls, r) == mm(gs, qs), name + ": spin gauge commuting square")
        check(mm(lc, r) == mm(gc, qc), name + ": coordinate gauge commuting square")
        check(rank(hcat(ls, gs)) == 12, name + ": spin joint image rank twelve")
        check(rank(gc) == 16 and rank(hcat(lc, gc)) == 22,
              name + ": coordinate joint image ranks")
        currents = kernel(tr(gs))
        if fault == "ward-drop":
            currents[0][0] += 1
        check(len(currents[0]) == 18, name + ": Ward-current space dimension eighteen")
        check(mm(tr(gs), currents) == zeros(6, 18), name + ": current Ward law")
        returned = mm(tr(ls), currents)
        check(rank(returned) == 6, name + ": dual current receiver rank six")
        check(mm(tr(r), returned) == zeros(4, 18), name + ": returned current annihilates metric gauge")
        check(len(currents[0]) - rank(returned) == 12, name + ": current-return kernel twelve")
        cc = kernel(tr(gc))
        check(rank(mm(tr(lc), cc)) == 6, name + ": coordinate dual receiver rank six")
        j = [F((i % 5) - 2) for i in range(24)]
        h = [F((i % 3) - 1) for i in range(10)]
        check(dot(j, mv(ls, h)) == dot(mv(tr(ls), j), h), name + ": exact dual pairing")

    # The complete density-pairing-operator product, differentiated exactly.
    mu = [F(1), F(0 if fault == "density-drop" else 1)]
    pairing = [F(1), F(0 if fault == "pairing-drop" else 2)]
    direct = F(0 if fault == "direct-drop" else 3)
    solder = F(0 if fault == "solder-drop" else 4)
    action = poly_mul(poly_mul(mu, pairing), [F(1), direct + solder])
    check(action[1] == 10, "complete metric source product derivative")
    # S(F(y)): S(x)=x+3x^2/2, F(y)=y+y^2.
    fy = [F(0), F(1), F(1)]
    square = poly_mul(fy, fy)
    second = 2 * (fy[2] + F(3, 2) * square[2])
    chain = F(3) + (0 if fault == "off-shell-chain-drop" else 2)
    check(second == chain == 5, "nonstationary Hessian second-chain term")

    # Actual tensor identity (4), all coefficients depending on x^1 in [0,1].
    # Independent construction: L_s differentiates h; E differentiates J.
    # Antisymmetric (a,b) is summed in full with 1/2, while symmetric h
    # is also summed in full, so off-diagonal metric entries occur twice.
    hp = [[[F(0)] for _ in range(4)] for _ in range(4)]
    jp = [[[[F(0)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    hp[0][2] = hp[2][0] = [F(1), F(0), F(1)]
    jp[0][2][1] = [F(2), F(1)]
    jp[0][1][2] = poly_scale(jp[0][2][1], -1)
    lhs = F(0)
    bulk = F(0)
    boundary = F(0)
    adjoint_factor = F(1, 4) if fault == "adjoint-sign" else F(-1, 4)
    if fault == "spin-adjoint-normalization":
        adjoint_factor = F(-1, 2)
    for mu_i in range(4):
        for ia in range(4):
            for ib in range(4):
                spin_variation = poly_scale(poly_add(
                    poly_derivative(hp[mu_i][ia]) if ib == 1 else [F(0)],
                    poly_scale(poly_derivative(hp[mu_i][ib]), -1) if ia == 1 else [F(0)]
                ), F(1, 2))
                lhs += F(1, 2) * poly_integral_01(poly_mul(jp[mu_i][ia][ib], spin_variation))
            euler = poly_scale(poly_derivative(poly_add(jp[mu_i][ia][1], jp[ia][mu_i][1])),
                               adjoint_factor)
            bulk += poly_integral_01(poly_mul(euler, hp[mu_i][ia]))
            boundary += F(1, 2) * poly_endpoint_difference(poly_mul(jp[mu_i][ia][1], hp[mu_i][ia]))
    if fault == "boundary-drop":
        boundary = F(0)
    check(lhs == bulk + boundary, "formal-adjoint Green identity including boundary")
    check(lhs != 0 and bulk != 0, "tensor Green control has nonzero bulk and current coupling")
    check(boundary != 0, "unrestricted boundary witness")
    check(hp[0][2] == hp[2][0] and poly_derivative(hp[0][2]) != [0],
          "tensor Green control includes moving off-diagonal metric")

    l = [[F(1), F(2)], [F(0), F(1)]]
    g = [[F(1)], [F(2)]]
    x = [[F(2), F(-1)]]
    current, d = [F(3), F(4)], [F(5), F(6)]
    lp = add(l, mm(g, x))
    delta = mv(tr(x), mv(tr(g), current))
    dp = d if fault == "compensator-drop" else subvec(d, delta)
    before = [a + b for a, b in zip(d, mv(tr(l), current))]
    after = [a + b for a, b in zip(dp, mv(tr(lp), current))]
    check(before == after, "total-source compensator invariance")
    check(mv(tr(l), current) != mv(tr(lp), current), "isolated current is representative-dependent")
    check(mv(tr(g), current) != [0], "compensator witness does not assume separate Ward closure")

    # Full versus reduced response; nonzero direct distortion source/readout.
    b = [[F(3), F(1)], [F(1), F(4)]]
    a = [[F(1), F(2)], [F(0), F(1)]]
    c = [[F(2), F(1)], [F(1), F(3)]]
    jh, jt = [F(1), F(-1)], [F(2), F(1)]
    rh, rt = [F(1), F(2)], [F(-1), F(3)]
    hfull = block(b, tr(a), a, c)
    k = inv(c)
    heff = add(b, neg(mm(mm(tr(a), k), a)))
    jeff = jh if fault == "source-drop" else subvec(jh, mv(mm(tr(a), k), jt))
    reff = rh if fault == "detector-drop" else subvec(rh, mv(mm(tr(a), k), rt))
    contact = F(0) if fault == "contact-drop" else dot(rt, mv(k, jt))
    reduced = dot(reff, mv(inv(heff), jeff)) + contact
    full = dot(rh + rt, mv(inv(hfull), jh + jt))
    check(full == F(-11, 2), "independent full-response rational witness")
    check(reduced == full, "complete source-detector-contact Schur response")
    check(dot(jh + jt, mv(inv(hfull), rh + rt)) == full, "symmetric-domain exchange reciprocity")
    check(dot(rt, mv(k, jt)) != 0, "contact contribution is nonzero")

    # Non-selfadjoint inverse control for the one-sided left/right identity.
    # This matrix is an algebraic domain/transpose control, not a finite Hessian.
    cone = [[F(2), F(1)], [F(0), F(3)]]
    kone = inv(cone)
    hone = block(b, tr(a), a, cone)
    effone = add(b, neg(mm(mm(tr(a), kone), a)))
    jeffone = subvec(jh, mv(mm(tr(a), kone), jt))
    detector_inverse = kone if fault == "one-sided-detector" else tr(kone)
    reffone = subvec(rh, mv(mm(tr(a), detector_inverse), rt))
    reducedone = dot(reffone, mv(inv(effone), jeffone)) + dot(rt, mv(kone, jt))
    check(reducedone == dot(rh + rt, mv(inv(hone), jh + jt)),
          "one-sided Schur detector uses adjoint inverse")
    left, right = [F(1), F(0)], [F(0), F(1)]
    advanced = kone if fault == "retarded-swap" else tr(kone)
    check(dot(left, mv(kone, right)) == dot(right, mv(advanced, left)),
          "retarded-advanced transpose exchange")
    check(dot(left, mv(kone, right)) != dot(right, mv(kone, left)),
          "same-retarded exchange countercontrol")

    source = [F(1), F(0), F(0), F(0)]
    motion = source[:]
    light = [F(1), F(0 if fault == "light-collapse" else 1), F(0), F(0)]
    for av in [F(0), F(1, 2), F(1), F(2)]:
        gm = [[F(2 if fault == "motion-drift" else 1), av], [av, F(1)]]
        bh = eye(2) if fault == "pure-hh-addition" and av == 0 else zeros(2, 2)
        ha = block(bh, eye(2), eye(2), neg(gm))
        proposed_inverse = block(gm, eye(2), eye(2), zeros(2, 2))
        label = "a=" + str(av)
        check(ha == tr(ha) and bh == zeros(2, 2), label + ": native-shaped coupled block")
        check(mm(ha, proposed_inverse) == eye(4), label + ": full coupled inverse")
        check(rank(ha) == 4, label + ": coupled invertibility")
        sol = mv(inv(ha), source)
        check(dot(motion, sol) == 1, label + ": fixed motion response")
        check(dot(light, sol) == 1 + av, label + ": fixed light readout response")
        check(dot(light, sol) == dot(source, mv(inv(ha), light)), label + ": paired reciprocity")
        hgauge = [row + [F(0)] for row in ha] + [[F(0)] * 5]
        kgauge = kernel(hgauge)
        check(rank(hgauge) == 4 and kgauge == [[F(0)], [F(0)], [F(0)], [F(0)], [F(1)]],
              label + ": exact declared metric-gauge radical")
        if av in [F(0), F(1, 2)]:
            check(gm[0][0] > 0 and gm[0][0] * gm[1][1] - gm[0][1] * gm[1][0] > 0,
                  label + ": positive finite metric response")

    endpoint_a = F(1, 2) if fault == "no-slip-omitted" else F(1)
    endg = [[F(1), endpoint_a], [endpoint_a, F(1)]]
    endh = block(zeros(2, 2), eye(2), eye(2), neg(endg))
    endsol = mv(inv(endh), source)
    if fault == "singular-pseudoinverse":
        endsol = [F(1), F(1), F(1, 2), F(1, 2)]
    check(rank(endg) == 1 and rank(endh) == 4, "singular distortion with invertible coupled endpoint")
    check(mv(endh, endsol) == source, "endpoint satisfies every coupled equation")
    check(endsol[1] - endsol[0] == 0, "one-row no-slip selection")
    check(dot(light, endsol) == 2 * dot(motion, endsol), "conditional light-motion ratio two")
    pseudo = [F(1), F(1), F(1, 2), F(1, 2)]
    check(mv(endh, pseudo) != source, "pseudoinverse reconstruction loses a full equation")

    # Supplied timelike/null metric contraction bridge on one static mode.
    q = [F(0), F(1), F(0), F(0)]
    r = symbols(q, None)[3]
    u, n = [F(1), F(0), F(0), F(0)], [F(1), F(0), F(0), F(1)]
    mc = [-dot(u, mv(h, u)) / 2 for h in symmetric_basis()]
    lc = [-dot(n, mv(h, n)) / 2 for h in symmetric_basis()]
    check(mv(tr(r), mc) == [0] * 4 and mv(tr(r), lc) == [0] * 4,
          "supplied motion/light contractions annihilate static metric gauge")
    check(sum(ETA[i] * n[i] * n[i] for i in range(4)) == 0,
          "supplied light carrier is null")
    hp, hs = zeros(4, 4), zeros(4, 4)
    hp[0][0] = F(-2)
    for i in range(1, 4):
        hs[i][i] = F(-2)
    check([-dot(u, mv(h, u)) / 2 for h in [hp, hs]] == [1, 0], "normalized motion reads Phi")
    check([-dot(n, mv(h, n)) / 2 for h in [hp, hs]] == [1, 1], "normalized light reads Phi plus Psi")
    return count, failures


FAULTS = {
    "coframe-drop": "timelike: moving-coframe adapter",
    "spin-sign": "timelike: moving-coframe adapter",
    "ward-drop": "timelike: current Ward law",
    "density-drop": "complete metric source product derivative",
    "pairing-drop": "complete metric source product derivative",
    "direct-drop": "complete metric source product derivative",
    "solder-drop": "complete metric source product derivative",
    "off-shell-chain-drop": "nonstationary Hessian second-chain term",
    "adjoint-sign": "formal-adjoint Green identity including boundary",
    "spin-adjoint-normalization": "formal-adjoint Green identity including boundary",
    "boundary-drop": "formal-adjoint Green identity including boundary",
    "compensator-drop": "total-source compensator invariance",
    "source-drop": "complete source-detector-contact Schur response",
    "detector-drop": "complete source-detector-contact Schur response",
    "contact-drop": "complete source-detector-contact Schur response",
    "one-sided-detector": "one-sided Schur detector uses adjoint inverse",
    "retarded-swap": "retarded-advanced transpose exchange",
    "motion-drift": "a=0: fixed motion response",
    "light-collapse": "a=1/2: fixed light readout response",
    "pure-hh-addition": "a=0: native-shaped coupled block",
    "no-slip-omitted": "one-row no-slip selection",
    "singular-pseudoinverse": "endpoint satisfies every coupled equation",
}


def main():
    count, failures = verify()
    for failure in failures:
        print("[FAIL] baseline: " + failure)
    if failures:
        return 1
    print(f"BASELINE PASS {count}/{count} exact finite algebra checks")
    if "--selftest" not in sys.argv:
        return 0
    caught = 0
    for fault, expected in FAULTS.items():
        try:
            _, failed = verify(fault)
        except Exception as exc:
            print(f"[FAIL] CRASH-NOT-DETECTION {fault}: {type(exc).__name__}: {exc}")
            return 1
        if expected not in failed:
            print(f"[FAIL] mutation {fault}: expected {expected!r}, observed {failed!r}")
            return 1
        caught += 1
        print(f"MUTATION CAUGHT {fault}: [FAIL] {expected}")
    print(f"SELFTEST PASS {caught}/{len(FAULTS)} genuine altered-input/operator faults")
    return 0


if __name__ == "__main__":
    sys.exit(main())
