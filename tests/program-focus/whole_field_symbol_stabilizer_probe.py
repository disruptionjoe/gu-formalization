#!/usr/bin/env python3
"""Exact small controls; analytic proof supplies n14 completeness."""
from fractions import Fraction as F
n, d = 2, 6
I = [[1, 0], [0, 1]]
gs = [[[0, 1], [1, 0]], [[0, -1], [1, 0]]]
eta = [1, -1]

def zero(k=d):
    return [[0] * k for _ in range(k)]

def eye(k=d):
    return [[int(i == j) for j in range(k)] for i in range(k)]

def mul(A, B):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*B)] for row in A]

def add(A, B, t=1):
    return [[a + t * b for a, b in zip(ar, br)] for ar, br in zip(A, B)]

def scale(A, t):
    return [[t * a for a in ar] for ar in A]

def block(a, b, m):
    A = zero()
    for i in range(2):
        for j in range(2):
            A[2*a+i][2*b+j] = m[i][j]
    return A

om = mul(gs[0], gs[1])
G = add(add(block(0, 0, om), block(1, 1, om)), block(2, 2, om), -1)

def arrows(x):
    P = block(x, n, I)
    Q = block(n, x, scale(I, eta[x]))
    W, D = zero(), zero()
    for a in range(n):
        W = add(W, block(a, a, gs[x]))
        D = add(D, block(a, a, gs[x]))
    for b in range(n):
        W = add(W, block(x, b, gs[b]), -1)
    T = block(n, n, gs[x])
    return P, Q, W, T, add(D, T)

def rank(rows):
    piv = {}
    for rr in rows:
        r = {k: F(v) for k, v in rr.items() if v}
        while r:
            j = min(r)
            if j not in piv:
                a = r[j]
                piv[j] = {k: v/a for k, v in r.items()}
                break
            a = r[j]
            for k, v in piv[j].items():
                r[k] = r.get(k, F(0)) - a*v
                if not r[k]:
                    del r[k]
    return len(piv)

def equations(mats):
    for A in mats:
        for i in range(d):
            for j in range(d):
                row = {}
                for k in range(d):
                    if A[k][j]:
                        row[i*d+k] = row.get(i*d+k, 0) + A[k][j]
                    if A[i][k]:
                        v = d*d+k*d+j
                        row[v] = row.get(v, 0) - A[i][k]
                yield row

As = [arrows(x) for x in range(n)]
cases = [('cross_only', [0, 1], 64),
         ('cross_plus_exterior', [0, 1, 2], 70),
         ('cross_plus_SE', [0, 1, 3], 70),
         ('fixed_Dirac', [4], 54),
         ('SE_only', [3], 22)]
for name, ids, expected in cases:
    rk = rank(equations([a[k] for a in As for k in ids]))
    assert rk == expected
    print(name, 'rank', rk, 'nullity', 72-rk)

J = zero()
for a in range(n):
    J = add(J, block(a, n, scale(gs[a], eta[a])))
M = add(eye(), J)
assert mul(J, J) == zero()
assert mul(M, add(eye(), J, -1)) == eye()
assert any(mul(A, M) != A for a in As for A in a[:4])
for a in As:
    for A in a[:4]:
        assert add(mul(G, A), mul(A, G)) == zero()
        N = add(scale(eye(), 3), scale(G, -2))
        M = add(scale(eye(), 3), scale(G, 2))
        assert mul(N, A) == mul(A, M)

jetcols = [sum(mul(As[mu][0], G if isb else eye()), [])
           for isb in [False, True] for mu in range(n)]
rk = rank({j: jetcols[j][i] for j in range(4) if jetcols[j][i]}
          for i in range(d*d))
assert rk == 4
print('first_jet_NE_rank', rk, 'of', 4)
print('PASS exact rational stabilizer, independent pairs, degeneracies, shear, jets')
