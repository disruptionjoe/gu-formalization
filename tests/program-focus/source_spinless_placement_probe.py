"""Exact ordered full-ambient spinless insertion; scalar mu factored out.
No adjoint assumptions enter these 392 Clifford identities.
"""
n = 14
eta = [1] * 9 + [-1] * 5

def mul(A, B):
    out = {}
    for x, a in A.items():
        for y, b in B.items():
            parity = sum((y & ((1 << j) - 1)).bit_count()
                         for j in range(n) if x >> j & 1)
            z = x ^ y
            sign = (-1) ** parity
            for j in range(n):
                if x & y & (1 << j):
                    sign *= eta[j]
            out[z] = out.get(z, 0) + a * b * sign
    return {x: a for x, a in out.items() if a}

def add(*xs):
    out = {}
    for A in xs:
        for x, a in A.items():
            out[x] = out.get(x, 0) + a
    return {x: a for x, a in out.items() if a}

def scale(s, A):
    return {x: s * a for x, a in A.items() if s * a}

I = {0: 1}
gam = [{1 << j: 1} for j in range(n)]
C = {}
for u in range(n):
    for v in range(n):
        got = {}
        for b in range(n):
            F = add(gam[b] if u == v else {},
                    scale(-1, gam[u]) if b == v else {})
            got = add(got, scale(eta[b], mul(gam[b], F)))
        expected = add(scale(n - 2, I) if u == v else {},
                       scale(eta[v], mul(gam[u], gam[v])))
        assert got == expected, (u, v, got, expected)
        C[u, v] = got
for u in range(n):
    for v in range(n):
        gammaC = {}
        for b in range(n):
            gammaC = add(gammaC, scale(eta[b], mul(gam[b], C[b, v])))
        got = mul(gam[u], gammaC)
        expected = scale(2 * (n - 1) * eta[v], mul(gam[u], gam[v]))
        assert got == expected, (u, v, got, expected)
print('392 exact native Cl(9,5) coefficient identities pass; mu factored out.')
