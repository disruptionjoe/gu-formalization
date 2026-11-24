#!/usr/bin/env python3
"""Exact finite controls for the global normal-complex reduction theorem.

Checks rational native form/splitting, F2 characteristic identities, and two
closed-base arithmetic controls. The topological theorem is NOT certified by
these finite calculations. Run with --output PATH to write the evidence JSON.
"""
from fractions import Fraction as F
from itertools import combinations
import argparse
import json
from pathlib import Path


def zeros():
    return [[F(0) for _ in range(4)] for _ in range(4)]


def diag(*xs):
    a = zeros()
    for i, x in enumerate(xs):
        a[i][i] = F(x)
    return a


def mixed(i, j):
    a = zeros()
    a[i][j] = a[j][i] = F(1)
    return a


def form(a, b, lam=F(1, 2)):
    signs = [-1, 1, 1, 1]
    frob = sum(signs[i] * signs[j] * a[i][j] * b[j][i]
               for i in range(4) for j in range(4))
    ta = sum(signs[i] * a[i][i] for i in range(4))
    tb = sum(signs[i] * b[i][i] for i in range(4))
    return frob - lam * ta * tb


def add(*polys):
    out = set()
    for p in polys:
        out.symmetric_difference_update(p)
    return out


def mul(p, q):
    out = set()
    for a in p:
        for b in q:
            monomial = tuple(sorted(a + b))
            if monomial in out:
                out.remove(monomial)
            else:
                out.add(monomial)
    return out


def w2(roots):
    return add(*(mul(a, b) for a, b in combinations(roots, 2)))


def polynomial_str(p):
    return " + ".join("*".join(m) for m in sorted(p)) or "0"


def checks(mutation=None):
    count = 0
    def check(cond, label):
        nonlocal count
        if not cond:
            raise AssertionError(label)
        count += 1

    lam = F(1) if mutation == "lambda" else F(1, 2)
    # Negative trace, three negative mixed directions, then six positive ones.
    basis = [diag(-1, 1, 1, 1)]
    basis += [mixed(0, i) for i in range(1, 4)]
    basis += [diag(3, 1, 1, 1), diag(0, 1, -1, 0), diag(0, 1, 1, -2)]
    basis += [mixed(i, j) for i, j in combinations(range(1, 4), 2)]
    expected = [-4, -2, -2, -2, 12, 2, 6, 2, 2, 2]
    for i, a in enumerate(basis):
        for j, b in enumerate(basis):
            check(form(a, b, lam) == (expected[i] if i == j else 0),
                  f"native Gram diagonal {i},{j}")
    check(sum(x > 0 for x in expected) == 6, "six positive directions")
    check(sum(x < 0 for x in expected) == 4, "four negative directions")
    # Scalar (a,s) form 1/2 a² + a s - 1/6 s².
    check(F(1, 2) * F(-1, 6) - F(1, 2)**2 == F(-1, 3),
          "scalar pair has opposite signs")

    a, b, c, l = ({(x,)} for x in "abcl")
    s1 = add(a, b, c)
    s2 = w2([a, b, c])
    sym2_roots = [set(), set(), set(), add(a, b), add(a, c), add(b, c)]
    check(add(*sym2_roots) == set(), "Sym2 rank3 is oriented")
    rhs = add(mul(s1, s1), s2)
    if mutation == "w2":
        rhs = s2
    check(w2(sym2_roots) == rhs, "w2(Sym2 E)=w1(E)^2+w2(E)")
    # Substitute l=s1, expressing w1(V)=l+w1(E)=0.
    neg_roots = [set(), add(s1, a), add(s1, b), add(s1, c)]
    v_roots = [s1, a, b, c]
    check(add(*neg_roots) == set(), "negative rank4 oriented")
    check(w2(neg_roots) == w2(v_roots), "w2(N-)=w2(V)")
    check(w2(sym2_roots) == w2(v_roots), "w2(N+)=w2(V)")
    # General tensor line rank4: w2(L tensor V)=w2(V)+l*w1(V).
    r = [{(x,)} for x in "abcd"]
    check(w2([add(l, x) for x in r]) == add(w2(r), mul(l, add(*r))),
          "real line twist rank4 identity")

    # K3 # 12(S1xS3): (chi,sigma)=(0,-16), hyperbolic square a²=2xy.
    chi = 24 - 2 * 12
    sigma = -16
    a_square = 2 * 1 * (-6)
    c_square = 4 * a_square
    if mutation == "closed_square":
        c_square += 4
    check(chi == 0, "compact spin Lorentz control chi")
    check(c_square == 2 * chi + 3 * sigma, "compact nonzero-signature square")
    check(c_square != 0, "do not force zero c1 square")
    # 2 CP2 # 2(S1xS3): diagonal odd lattice, characteristic coordinates odd.
    chi_nonspin = 3 + 3 - 2 - 2 * 2
    sigma_nonspin = 2
    check(chi_nonspin == 0, "nonspin Lorentz control chi")
    residues = {(x*x + y*y) % 8 for x in (1, 3, 5, 7) for y in (1, 3, 5, 7)}
    check(residues == {2}, "all characteristic square residues")
    check((2 * chi_nonspin + 3 * sigma_nonspin) % 8 not in residues,
          "nonspin obstruction is exact modulo eight")
    return {
        "artifact": "GLOBAL_NORMAL_COMPLEX_REDUCTION_FINITE_CONTROLS",
        "checks_passed": count,
        "arithmetic": "fractions_and_F2_polynomials_only",
        "native_gram_diagonal": expected,
        "positive_negative_rank": [6, 4],
        "w2_positive_and_negative": polynomial_str(w2(v_roots)),
        "compact_spin_control": {"base": "K3 connected sum 12(S1 x S3)",
                                 "chi": chi, "signature": sigma,
                                 "a_square": a_square, "c_square": c_square},
        "outside_spin_negative_control": {"base": "2 CP2 connected sum 2(S1 x S3)",
                                          "chi": chi_nonspin, "signature": sigma_nonspin,
                                          "characteristic_square_mod8": [2], "required_mod8": 6},
        "claim_ceiling": "Finite controls; topology is proved in the companion argument using the cited primary obstruction theorem. No source selection, domain or GU verdict."
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    result = checks()
    if args.selftest:
        detected = []
        for mutation in ("lambda", "w2", "closed_square"):
            try:
                checks(mutation)
            except AssertionError:
                detected.append(mutation)
        assert len(detected) == 3, detected
        result["mutations_detected"] = detected
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
