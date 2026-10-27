#!/usr/bin/env python3
"""Exact controls for the conditional source mixed-port discriminator.

Standard library only. Universal claims are proved in the companion note;
these checks cover the actual n=14 Clifford algebra and an independent small
real-matrix null fixture. No physical quotient, signature choice, half-label
repair, family count, or GU prediction is certified.
"""

from fractions import Fraction as F
import argparse


class CheckFailure(Exception):
    pass


class Checks:
    def __init__(self, quiet=False):
        self.count = 0
        self.quiet = quiet

    def __call__(self, label, condition):
        self.count += 1
        if not condition:
            raise CheckFailure(label)
        if not self.quiet:
            print("[PASS] " + label)


# Sparse exact Clifford polynomials. Distinct basis blades are independent.
def clean(a):
    return {m: F(v) for m, v in a.items() if v}


def add(*args):
    out = {}
    for a in args:
        for m, v in a.items():
            out[m] = out.get(m, F(0)) + v
    return clean(out)


def scale(a, c):
    return clean({m: F(c) * v for m, v in a.items()})


def mul(a, b, eta):
    out = {}
    for x, u in a.items():
        for y, v in b.items():
            sign = 1
            for i in range(len(eta)):
                if (x >> i) & 1:
                    if (y & ((1 << i) - 1)).bit_count() % 2:
                        sign = -sign
                    if (y >> i) & 1:
                        sign *= eta[i]
            mask = x ^ y
            out[mask] = out.get(mask, F(0)) + sign * u * v
    return clean(out)


ONE = {0: F(1)}


def pmul(a, b, eta):
    return [[add(*(mul(a[i][k], b[k][j], eta)
                   for k in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]


def pzero(a):
    return all(not v for row in a for v in row)


def symbolic_fixture(eta, k, fault=None):
    n = len(eta)
    gam = [{1 << i: F(1)} for i in range(n)]
    slash = add(*(scale(gam[i], eta[i] * k[i]) for i in range(n)))
    q = sum(eta[i] * k[i] ** 2 for i in range(n))
    j = [[g] for g in gam]
    gamma = [[scale(gam[i], eta[i]) for i in range(n)]]
    u = [[scale(ONE, k[i])] for i in range(n)]
    d = [[scale(ONE, eta[i] * k[i]) for i in range(n)]]
    identity = [[ONE if i == j else {} for j in range(n)] for i in range(n)]
    data = dict(n=n, eta=eta, k=k, gam=gam, slash=slash, q=q,
                j=j, gamma=gamma, u=u, d=d, identity=identity)
    if q:
        jp = [[add(gam[i], scale(slash, -F(k[i], q)))] for i in range(n)]
        gp = [[add(gamma[0][i], scale(slash, -F(eta[i] * k[i], q)))
               for i in range(n)]]
        denom = n if fault == "projector-denominator" else n - 1
        long = pmul(u, d, eta)
        trace = pmul(jp, gp, eta)
        p = [[add(identity[i][j], scale(long[i][j], -F(1, q)),
                  scale(trace[i][j], -F(1, denom)))
              for j in range(n)] for i in range(n)]
        data.update(jp=jp, gp=gp, p=p)
    else:
        denom = n - 1 if fault == "null-denominator" else n
        t = [[add(u[i][0], scale(mul(
            slash if fault == "reversed-clifford-order" else gam[i],
            gam[i] if fault == "reversed-clifford-order" else slash,
            eta), -F(1, denom)))] for i in range(n)]
        tx = [[add(d[0][i], scale(mul(slash, gamma[0][i], eta),
                                  -F(1, n))) for i in range(n)]]
        data.update(t=t, tx=tx)
    return data


# Independent explicit real Cl(2,2) exterior-algebra representation.
def zeros(r, c):
    return [[F(0) for _ in range(c)] for _ in range(r)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(x) for x in zip(*a)]


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def ma(a, b, c=1):
    return [[x + F(c) * y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def ms(a, c):
    return [[F(c) * x for x in row] for row in a]


def vstack(blocks):
    return [row[:] for b in blocks for row in b]


def hstack(blocks):
    return [sum((b[i] for b in blocks), []) for i in range(len(blocks[0]))]


def rref(a):
    a = [row[:] for row in a]
    pivots = []
    row = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(row, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        divisor = a[row][col]
        a[row] = [x / divisor for x in a[row]]
        for j in range(len(a)):
            if j != row and a[j][col]:
                c = a[j][col]
                a[j] = [x - c * y for x, y in zip(a[j], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def rank(a):
    return len(rref(a)[1])


def kernel(a):
    reduced, pivots = rref(a)
    free = [i for i in range(len(a[0])) if i not in pivots]
    cols = []
    for j in free:
        col = [F(0)] * len(a[0])
        col[j] = F(1)
        for i, p in enumerate(pivots):
            col[p] = -reduced[i][j]
        cols.append(col)
    return transpose(cols) if cols else zeros(len(a[0]), 0)


def real_cl22():
    positive, negative = [], []
    for i in range(2):
        create, annihilate = zeros(4, 4), zeros(4, 4)
        for mask in range(4):
            sign = F((-1) ** ((mask & ((1 << i) - 1)).bit_count()))
            if mask & (1 << i):
                annihilate[mask ^ (1 << i)][mask] = sign
            else:
                create[mask | (1 << i)][mask] = sign
        positive.append(ma(create, annihilate))
        negative.append(ma(create, annihilate, -1))
    return positive + negative


def run_checks(fault=None, quiet=False):
    check = Checks(quiet)
    for signature in ((7, 7), (9, 5)):
        p, qneg = signature
        eta = [1] * p + [-1] * qneg
        # K95 is a complexified/algebraic sign control, not real K77 transport.
        for axis in (0, p):
            k = [0] * 14
            k[axis] = 1
            f = symbolic_fixture(eta, k, fault)
            check(f"Cl{signature} slash-square axis{axis}",
                  mul(f["slash"], f["slash"], eta) == scale(ONE, f["q"]))
            check(f"Cl{signature} perpendicular Clifford normalization axis{axis}",
                  pmul(f["gp"], f["jp"], eta) == [[scale(ONE, 13)]])
            check(f"Cl{signature} projector idempotent axis{axis}",
                  pmul(f["p"], f["p"], eta) == f["p"])
            check(f"Cl{signature} projector gamma-traceless axis{axis}",
                  pzero(pmul(f["gamma"], f["p"], eta)))
            check(f"Cl{signature} projector transverse axis{axis}",
                  pzero(pmul(f["d"], f["p"], eta)))
            check(f"Cl{signature} annihilates longitudinal and Clifford trace axis{axis}",
                  pzero(pmul(f["p"], f["u"], eta))
                  and pzero(pmul(f["p"], f["j"], eta)))
        k = [0] * 14
        k[0] = k[p] = 1
        f = symbolic_fixture(eta, k, fault)
        check(f"Cl{signature} null slash nilpotent", not mul(f["slash"], f["slash"], eta))
        check(f"Cl{signature} null radical gamma constraint",
              pzero(pmul(f["gamma"], f["t"], eta)))
        check(f"Cl{signature} null radical transverse constraint",
              pzero(pmul(f["d"], f["t"], eta)))
        check(f"Cl{signature} null quotient functional kills invisible ports",
              pzero(pmul(f["tx"], f["u"], eta))
              and pzero(pmul(f["tx"], f["j"], eta)))
        # Actual coefficient-complete predecessor form v=(2,-1,0,1,...).
        # The all-null exclusion is analytic; these exact inputs check its
        # source-matched formula and all three invertible parent grades.
        v = [2, -1, 0, 1] + [0] * 10
        slash_v = add(*(scale(f["gam"][i], eta[i] * v[i]) for i in range(14)))
        kv = sum(eta[i] * k[i] * v[i] for i in range(14))
        bracket = add(scale(ONE, kv), scale(mul(f["slash"], slash_v, eta), -F(1, 14)))
        check(f"Cl{signature} inherited decomposable form is nonnull", sum(eta[i] * v[i] ** 2 for i in range(14)) == 6)
        for grade in (1, 2, 6):
            parent = {(1 << grade) - 1: F(1)}
            square = mul(parent, parent, eta)
            a = [[scale(parent, v[i])] for i in range(14)]
            response = pmul(f["tx"], a, eta)
            check(f"Cl{signature} parent grade{grade} is invertible", square in (ONE, scale(ONE, -1)))
            check(f"Cl{signature} inherited grade{grade} null response formula", response == [[mul(bracket, parent, eta)]])
            check(f"Cl{signature} inherited grade{grade} port fails null descent", not pzero(response))
            parallel = [[scale(parent, k[i])] for i in range(14)]
            check(f"Cl{signature} parallel grade{grade} port passes but is longitudinal", pzero(pmul(f["tx"], parallel, eta)))
        if signature == (7, 7):
            qpin = f["gam"][7]
            transported = [[scale(mul(mul(qpin, g, eta), qpin, eta), -1 if i == 7 else 1)]
                           for i, g in enumerate(f["gam"])]
            check("K77 stationary row-Pin forward port remains pure Clifford trace", transported == f["j"])
        # R_k = slash(k) I - u_k Gamma is the inherited simple Phi d symbol.
        ug = pmul(f["u"], f["gamma"], eta)
        r = [[add(f["slash"] if i == j else {}, scale(ug[i][j], -1))
              for j in range(14)] for i in range(14)]
        rt = pmul(r, f["t"], eta)
        expected = [[scale(mul(x[0], f["slash"], eta), F(12, 14))] for x in f["t"]]
        check(f"Cl{signature} principal symbol preserves null radical", rt == expected)
        gamma_r = pmul(f["gamma"], r, eta)
        gamma_r_expected = [[add(scale(f["d"][0][i], 2),
                                 scale(mul(f["slash"], f["gamma"][0][i], eta), -2))
                             for i in range(14)]]
        check(f"Cl{signature} coupled principal Gamma equation has the required factor two",
              gamma_r == gamma_r_expected)
        rj = pmul(r, f["j"], eta)
        lift_residual = [[add(scale(rj[i][0], F(1, 12)), f["u"][i][0])]
                         for i in range(14)]
        check(f"Cl{signature} every massless nu has the explicit coupled principal lift",
              all(not mul(row[0], f["slash"], eta) for row in lift_residual)
              and not mul(pmul(f["d"], f["j"], eta)[0][0], f["slash"], eta))

        # Complete finite certificate for the ALL-null fixed-port theorem.
        # Any fixed port a has b=(I-j Gamma/n)a, and each null response is
        # the metric contraction of k with b. Null covectors span V*.
        null_basis = []
        for sign in (1, -1):
            covector = [0] * 14
            covector[0], covector[p] = 1, sign
            null_basis.append(covector)
        for i in range(1, p):
            covector = [0] * 14
            covector[i] = covector[p] = 1
            null_basis.append(covector)
        for i in range(p + 1, 14):
            covector = [0] * 14
            covector[0] = covector[i] = 1
            null_basis.append(covector)
        if fault == "null-basis-duplicate":
            null_basis[-1] = null_basis[0][:]
        check(f"Cl{signature} all fourteen spanning covectors are null",
              len(null_basis) == 14 and all(sum(eta[i] * v[i] ** 2 for i in range(14)) == 0
                                          for v in null_basis))
        contracted_basis = [[F(eta[i] * v[i]) for i in range(14)] for v in null_basis]
        check(f"Cl{signature} null contraction matrix has full exact rank",
              rank(contracted_basis) == 14)
        jgamma = pmul(f["j"], f["gamma"], eta)
        tracefree = [[add(f["identity"][i][j], scale(jgamma[i][j], -F(1, 14)))
                      for j in range(14)] for i in range(14)]
        all_linear = True
        all_trace_zero = True
        for v in null_basis:
            null_f = symbolic_fixture(eta, v)
            contraction = [[scale(ONE, eta[i] * v[i]) for i in range(14)]]
            all_linear = all_linear and pmul(contraction, tracefree, eta) == null_f["tx"]
            all_trace_zero = all_trace_zero and pzero(pmul(null_f["tx"], f["j"], eta))
        check(f"Cl{signature} full-coefficient null response equals contraction of gamma-tracefree port",
              all_linear)
        check(f"Cl{signature} fixed pure-trace port descends on complete null basis", all_trace_zero)
        # Full-input null spanning does not apply after restricting inputs to
        # ker slash(k). A fixed middle-grade word supplies an exact escape.
        middle = {(1 << 7) - 1: F(1)}
        raw_middle = [[mul(middle, g, eta)] for g in f["gam"]]
        check(f"Cl{signature} middle-grade raw port has zero Clifford trace",
              pzero(pmul(f["gamma"], raw_middle, eta)))
        relative_sign = -1 if fault == "middle-grade-port-sign" else 1
        pure_six = [[scale(add(mul(middle, g, eta),
                               scale(mul(g, middle, eta), relative_sign)), F(1, 2))]
                    for g in f["gam"]]
        check(f"Cl{signature} anticommutator port is purely Clifford grade six",
              any(row[0] for row in pure_six)
              and all(mask.bit_count() == 6 for row in pure_six for mask in row[0]))
        check(f"Cl{signature} grade-six port pairing adjoint is skew",
              all((-1) ** (mask.bit_count() * (mask.bit_count() + 1) // 2) == -1
                  for row in pure_six for mask in row[0]))
        check(f"Cl{signature} grade-six port Clifford trace is 7Z",
              pmul(f["gamma"], pure_six, eta) == [[scale(middle, 7)]])
        all_raw_responses = True
        all_six_responses = True
        all_onshell = True
        for v in null_basis:
            null_f = symbolic_fixture(eta, v)
            raw_response = pmul(null_f["tx"], raw_middle, eta)[0][0]
            six_response = pmul(null_f["tx"], pure_six, eta)[0][0]
            expected_response = mul(middle, null_f["slash"], eta)
            all_raw_responses = all_raw_responses and raw_response == expected_response
            all_six_responses = all_six_responses and six_response == scale(expected_response, F(1, 2))
            all_onshell = all_onshell and not mul(six_response, null_f["slash"], eta)
        check(f"Cl{signature} fixed middle-grade raw response is Z slash(k)", all_raw_responses)
        check(f"Cl{signature} fixed grade-six response is Z slash(k)/2", all_six_responses)
        check(f"Cl{signature} fixed grade-six response kills im slash(k)=ker slash(k)", all_onshell)
        check(f"Cl{signature} grade-six nonzero quotient witness has zero component eight",
              not pure_six[8][0])
        check(f"Cl{signature} grade-six nonzero quotient witness has invertible component one",
              mul(pure_six[1][0], pure_six[1][0], eta) in (ONE, scale(ONE, -1)))

    eta = [1, 1, -1, -1]
    gam = real_cl22()
    identity, zero = eye(4), zeros(4, 4)
    check("independent real Clifford relations", all(
        ma(mm(gam[i], gam[j]), mm(gam[j], gam[i]))
        == ms(identity, 2 * eta[i]) if i == j else
        ma(mm(gam[i], gam[j]), mm(gam[j], gam[i])) == zero
        for i in range(4) for j in range(4)))
    b = mm(gam[0], gam[1])
    check("independent real nondegenerate Clifford-skew pairing",
          rank(b) == 4 and all(ma(mm(transpose(g), b), mm(b, g)) == zero for g in gam))
    form = zeros(16, 16)
    for i in range(4):
        for r in range(4):
            for c in range(4):
                form[4 * i + r][4 * i + c] = eta[i] * b[r][c]
    gamma = hstack([ms(gam[i], eta[i]) for i in range(4)])
    j = vstack(gam)
    for k, null in (([1, 0, 0, 0], False), ([1, 0, 1, 0], True)):
        u = vstack([ms(identity, x) for x in k])
        d = hstack([ms(identity, eta[i] * k[i]) for i in range(4)])
        constraint = vstack([gamma, d])
        basis = kernel(constraint)
        gram = mm(transpose(basis), mm(form, basis))
        check(f"matrix constraint surjective null={null}", rank(constraint) == 8)
        check(f"matrix transverse gamma kernel dimension null={null}", len(basis[0]) == 8)
        check(f"matrix restricted pairing rank null={null}", rank(gram) == (4 if null else 8))
        invisible = hstack([u, j])
        check(f"matrix complete annihilator null={null}",
              rank(invisible) == 8 and mm(transpose(basis), mm(form, invisible)) == zeros(8, 8))
        if not null:
            continue
        slash = ma(gam[0], gam[2], -1)
        t = ma(u, mm(j, slash), -F(1, 4))
        check("matrix null radical is full injective twistor image",
              rank(t) == 4 and mm(constraint, t) == zeros(8, 4)
              and mm(transpose(basis), mm(form, t)) == zeros(8, 4))
        check("k ker(slash) is only a proper radical subspace",
              rank(mm(u, kernel(slash))) == 2 < rank(t))
        tx = ma(d, mm(slash, gamma), -F(1, 4))
        check("matrix null descent condition has four independent equations", rank(tx) == 4)
        check("matrix null quotient coupling dimensions", 16 - rank(tx) - rank(invisible) == 4)
        # Bivector-valued connection components, rather than arbitrary End(S).
        a = vstack([zero, mm(gam[0], gam[1]), zero, mm(gam[3], gam[0])])
        if fault == "surviving-port-sign":
            a = vstack([zero, mm(gam[0], gam[1]), zero, ms(mm(gam[3], gam[0]), -1)])
        check("nonzero Spin-valued port obeys both external constraints",
              mm(constraint, a) == zeros(8, 4))
        check("nonzero Spin-valued port descends", mm(tx, a) == zero)
        check("nonzero descended amplitude exact pairing 2B", mm(transpose(a), mm(form, a)) == ms(b, 2))
        bad = vstack([mm(gam[1], gam[3]), zero, zero, zero])
        check("generic Spin-valued port fails null descent", mm(tx, bad) != zero)
        check("bare derivative port is invisible", mm(transpose(basis), mm(form, u)) == zeros(8, 4))
        singular_port = vstack([zero, slash, zero, zero])
        check("singular-parent escape has rank-two null Clifford coefficient", rank(slash) == 2)
        check("decomposable singular-parent escape descends", mm(tx, singular_port) == zero)
        check("decomposable singular-parent escape has nonzero rank-two quotient functional",
              rank(mm(transpose(basis), mm(form, singular_port))) == 2)
        check("singular-parent escape self-pairing is zero despite nonzero cross-amplitude",
              mm(transpose(singular_port), mm(form, singular_port)) == zero)
        next_k = [0, 1, 1, 0]
        next_slash = ma(gam[1], gam[2], -1)
        next_d = hstack([ms(identity, eta[i] * next_k[i]) for i in range(4)])
        next_tx = ma(next_d, mm(next_slash, gamma), -F(1, 4))
        check("second tested momentum is null", mm(next_slash, next_slash) == zero)
        check("fixed nondecomposable port fails at second null momentum",
              mm(next_tx, a) == mm(gam[0], gam[1]) != zero)
        check("fixed singular-parent port fails at second null momentum",
              mm(next_tx, singular_port) != zero)
        fixed_z = mm(gam[0], gam[1])
        fixed_onshell_port = vstack([mm(fixed_z, g) for g in gam])
        null_inputs = kernel(slash)
        check("fixed middle-grade real port has zero Clifford trace",
              mm(gamma, fixed_onshell_port) == zero)
        check("fixed middle-grade real response equals Z slash(k)",
              mm(tx, fixed_onshell_port) == mm(fixed_z, slash))
        check("fixed middle-grade real port descends on massless inputs",
              mm(tx, mm(fixed_onshell_port, null_inputs)) == zeros(4, 2))
        check("fixed middle-grade real port has rank-two nonzero quotient cross-amplitude on massless inputs",
              rank(mm(transpose(basis), mm(form, mm(fixed_onshell_port, null_inputs)))) == 2)
        check("fixed middle-grade real response equals Z slash(k) also at second null momentum",
              mm(next_tx, fixed_onshell_port) == mm(fixed_z, next_slash))
        check("fixed middle-grade real port descends on second massless input subspace",
              mm(next_tx, mm(fixed_onshell_port, kernel(next_slash))) == zeros(4, 2))
        slash_diagonal = zeros(16, 16)
        for i in range(4):
            for r in range(4):
                for c in range(4):
                    slash_diagonal[4 * i + r][4 * i + c] = slash[r][c]
        r_block = ma(slash_diagonal, mm(u, gamma), -1)
        coupled = vstack([hstack([r_block, u]), hstack([ms(d, -1), zero])])
        coupled_kernel = kernel(coupled)
        nu_projection = coupled_kernel[16:]
        check("actual simple-contraction coupled null kernel has exactly massless nu image",
              rank(nu_projection) == 2 and mm(slash, nu_projection) == zeros(4, len(nu_projection[0])))
        lifted = vstack([ms(mm(j, null_inputs), F(1, 2)), null_inputs])
        check("explicit nu lift solves both coupled principal equations", mm(coupled, lifted) == zeros(20, 2))
    return check.count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    try:
        count = run_checks(quiet=args.selftest)
    except CheckFailure as exc:
        print("[FAIL] clean baseline: " + str(exc))
        return 1
    print(f"BASELINE_PASS: {count} exact finite checks")
    if args.selftest:
        faults = ("projector-denominator", "null-denominator",
                  "reversed-clifford-order", "surviving-port-sign",
                  "null-basis-duplicate", "middle-grade-port-sign")
        for fault in faults:
            try:
                run_checks(fault, quiet=True)
            except CheckFailure as exc:
                print(f"[FAIL] mutation {fault}: {exc}")
                print(f"[CAUGHT] {fault}")
            else:
                print(f"[FAIL] mutation escaped: {fault}")
                return 1
        print(f"SELFTEST_PASS: {len(faults)} mathematical construction mutations caught")
    print("CEILING: local conditional Clifford/paired-bilinear controls; no physical quotient or GU prediction")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
