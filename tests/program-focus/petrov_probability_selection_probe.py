#!/usr/bin/env python3
"""Exact Gaussian-integer Laurent-polynomial controls, not a topology proof.

Coordinates: x,y,t,alpha,beta. Negative t/alpha powers are formal Laurent
monomials, valid for nonzero parameters. No floating point or tolerance.
"""
import json
from fractions import Fraction


def gc_add(a, b):
    return a[0] + b[0], a[1] + b[1]


def gc_mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def add(*ps):
    d = {}
    for p in ps:
        for m, c in p.items():
            d[m] = gc_add(d.get(m, (0, 0)), c)
    return {m: c for m, c in d.items() if c != (0, 0)}


def mul(p, q):
    d = {}
    for m, c in p.items():
        for n, e in q.items():
            k = tuple(a+b for a, b in zip(m, n))
            d[k] = gc_add(d.get(k, (0, 0)), gc_mul(c, e))
    return {m: c for m, c in d.items() if c != (0, 0)}


ONE = {(0, 0, 0, 0, 0): (1, 0)}
ZERO = {}


def scale(p, c):
    return {m: v for m, z in p.items() if (v := gc_mul(z, c)) != (0, 0)}


def power(p, n):
    q = ONE
    for _ in range(n):
        q = mul(q, p)
    return q


def monomial(k, c=(1, 0)):
    return {k: c}


x = monomial((1, 0, 0, 0, 0))
y = monomial((0, 1, 0, 0, 0))
t = monomial((0, 0, 1, 0, 0))
ti = monomial((0, 0, -1, 0, 0))
alpha = monomial((0, 0, 0, 1, 0))
ai = monomial((0, 0, 0, -1, 0))
beta = monomial((0, 0, 0, 0, 1))


def quartic(a, b, c, X=x, Y=y):
    return add(mul(a, mul(power(X, 2), power(Y, 2))),
               mul(b, mul(X, power(Y, 3))), mul(c, mul(power(X, 3), Y)))


def mm(A, B):
    return [[add(*(mul(A[i][k], B[k][j]) for k in range(2)))
             for j in range(2)] for i in range(2)]


def det(A):
    return add(mul(A[0][0], A[1][1]), scale(mul(A[0][1], A[1][0]), (-1, 0)))


def sm(A, c):
    return [[scale(v, c) for v in row] for row in A]


def subst(f, A):
    X = add(mul(A[0][0], x), mul(A[0][1], y))
    Y = add(mul(A[1][0], x), mul(A[1][1], y))
    return f(X, Y)


def main():
    checks = []

    def check(label, value):
        assert value, label
        checks.append(label)

    I2 = [[ONE, ZERO], [ZERO, ONE]]
    J = [[ZERO, scale(t, (0, 1))], [scale(ti, (0, 1)), ZERO]]
    A0 = [[scale(ONE, (0, 1)), scale(t, (-1, 0))],
          [ti, scale(ONE, (0, -1))]]
    B0 = [[scale(ONE, (0, 1)), t],
          [scale(ti, (-1, 0)), scale(ONE, (0, -1))]]
    f3 = lambda X, Y: quartic(ZERO, ONE, power(ti, 2), X, Y)
    f23 = lambda X, Y: quartic(alpha, beta, mul(beta, power(ti, 2)), X, Y)
    check('J determinant', det(J) == ONE)
    check('J square', mm(J, J) == sm(I2, (-1, 0)))
    check('J exact II/III invariance', subst(f23, sm(J, (-1, 0))) == f23(x, y))
    for name, M in [('A', A0), ('B', B0)]:
        check(name+' unnormalized determinant', det(M) == scale(ONE, (2, 0)))
        check(name+' unnormalized square', mm(M, M) == sm(I2, (-2, 0)))
        check(name+' quartic normalization', subst(f3, sm(M, (-1, 0))) == scale(f3(x, y), (4, 0)))
    check('A0 B0 = 2J', mm(A0, B0) == sm(J, (2, 0)))
    check('B0 A0 = -2J', mm(B0, A0) == sm(J, (-2, 0)))
    M = [[scale(ONE, (0, -1)), scale(mul(beta, ai), (0, -1))],
         [ZERO, scale(ONE, (0, 1))]]
    f2 = lambda X, Y: quartic(alpha, beta, ZERO, X, Y)
    check('general II exact exchange', subst(f2, sm(M, (-1, 0))) == f2(x, y))
    check('general II exchange square', mm(M, M) == sm(I2, (-1, 0)))
    check('general II exchange determinant', det(M) == ONE)
    # The sharp-II sequence is even, so the fixed compact involution preserves it.
    R = [[scale(ONE, (0, 1)), ZERO], [ZERO, scale(ONE, (0, -1))]]
    fe = lambda X, Y: add(mul(alpha, power(X, 4)), mul(power(X, 2), power(Y, 2)), power(Y, 4))
    check('even sharp-II sequence fixed', subst(fe, R) == fe(x, y))
    wrong = [[ZERO, scale(t, (0, 1))], [scale(ti, (0, -1)), ZERO]]
    check('mutation: wrong off-diagonal sign rejected', subst(f23, wrong) != f23(x, y))
    wrong_ratio = [[scale(ONE, (0, -1)), scale(mul(beta, ai), (0, 1))],
                   [ZERO, scale(ONE, (0, 1))]]
    check('mutation: wrong II exchange rejected', subst(f2, wrong_ratio) != f2(x, y))
    # Four-point regular Klein action: exact saturation of overlap budgets.
    for subset in [{0}, {0, 1}]:
        translates = [{h ^ a for a in subset} for h in range(4)]
        overlap = [sum(a in s for s in translates) for a in range(4)]
        mass = Fraction(len(subset), 4)
        check('weighted overlap saturation '+str(len(subset)),
              all(k == len(subset) for k in overlap) and 4*mass == len(subset))
    print(json.dumps({'status': 'PASS', 'checks': len(checks), 'labels': checks,
                      'arithmetic': 'Gaussian integers / formal Laurent polynomials / rational weights',
                      'scope': 'finite identities only; not properness, tightness, source relevance or worldwide priority'}, indent=2))


if __name__ == '__main__':
    main()
