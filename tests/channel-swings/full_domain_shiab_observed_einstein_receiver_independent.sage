#!/usr/bin/env -S sage -python
"""Independent QQ replay of the selected-Shiab kernel theorem.

This file intentionally does not import the SymPy certificate.
"""

from sage.all import QQ, PolynomialRing, binomial, diagonal_matrix, matrix, vector, zero_matrix


Q = QQ
gH = diagonal_matrix(Q, [1, -1, -1, -1] + [0] * 10)
gN = diagonal_matrix(Q, [0] * 4 + [1] * 6 + [-1] * 4)
g = gH + gN
ginv = g.inverse()
g4 = diagonal_matrix(Q, [1, -1, -1, -1])
g4inv = g4.inverse()


def KN(A, B, a, b, c, d):
    return (A[a,c]*B[b,d] + A[b,d]*B[a,c]
            - A[a,d]*B[b,c] - A[b,c]*B[a,d])


def ricci(F, dim, inv):
    return matrix(Q, dim, dim, lambda b, d:
                  sum(inv[a,c] * F(a,b,c,d)
                      for a in range(dim) for c in range(dim)))


def einstein(F, dim, metric, inv):
    Ric = ricci(F, dim, inv)
    scal = sum(inv[a,b] * Ric[a,b]
               for a in range(dim) for b in range(dim))
    return Ric - scal/2 * metric


def scalar_witness(a,b,c,d):
    return (KN(gH,gH,a,b,c,d)/2
            - 3*KN(gH,gN,a,b,c,d)/10
            + KN(gN,gN,a,b,c,d)/15)


assert ricci(scalar_witness, 14, ginv).is_zero()
assert einstein(scalar_witness, 14, g, ginv).is_zero()
assert einstein(scalar_witness, 4, g4, g4inv) == -3*g4


def tf_basis():
    out = []
    for i in range(4):
        for j in range(i+1,4):
            S = zero_matrix(Q,14)
            S[i,j] = S[j,i] = 1
            out.append(S)
    for j in range(1,4):
        S = zero_matrix(Q,14)
        S[0,0] = S[j,j] = 1
        out.append(S)
    return out


def family(S):
    return lambda a,b,c,d: KN(S,gH,a,b,c,d) - KN(S,gN,a,b,c,d)/5


def symvec(M):
    return vector(Q, [M[i,j] for i in range(4) for j in range(i,4)])


outs = [symvec(-3*g4)]
for S in tf_basis():
    F = family(S)
    assert ricci(F,14,ginv).is_zero()
    E4 = einstein(F,4,g4,g4inv)
    assert E4 == 2*S[:4,:4]
    outs.append(symvec(E4))

assert matrix(Q, outs).rank() == 10

# Independent nonzero Riemann-projector replay and exact carrier rank.
raw_values = {(0,1,0,2):Q(1), (2,0,3,1):Q(2),
              (4,7,5,9):Q(-3), (13,8,6,11):Q(5)}


def raw(a,b,c,d):
    return raw_values.get((a,b,c,d), Q(0))


def pa(F,a,b,c,d):
    return (F(a,b,c,d)-F(b,a,c,d)-F(a,b,d,c)+F(b,a,d,c))/4


def ps(F,a,b,c,d):
    return (pa(F,a,b,c,d)+pa(F,c,d,a,b))/2


def PR(F,a,b,c,d):
    s = ps(F,a,b,c,d)
    return s-(s+ps(F,a,c,d,b)+ps(F,a,d,b,c))/3


P = lambda a,b,c,d: PR(raw,a,b,c,d)
PP = lambda a,b,c,d: PR(P,a,b,c,d)
slots = [(0,1,0,2),(0,2,0,1),(2,0,3,1),(4,7,5,9),(13,8,6,11)]
assert any(P(*slot) != 0 for slot in slots)
assert all(PP(*slot) == P(*slot) for slot in slots)
pair_dim = binomial(14,2)
pair_sym_dim = pair_dim*(pair_dim+1)//2
four_dim = binomial(14,4)
assert pair_sym_dim == 4186
assert four_dim == 1001
assert pair_sym_dim-four_dim == 3185

# Independent Gauss derivative coefficient over QQ[t].
Rt = PolynomialRing(Q, "t")
t = Rt.gen()
B = [zero_matrix(Rt,4) for _ in range(10)]
dB = [zero_matrix(Rt,4) for _ in range(10)]
B[0][0,0], B[0][1,1] = 1, 2
B[1][0,1] = B[1][1,0] = 1
dB[0][0,1] = dB[0][1,0] = 3
dB[1][2,2] = -2
eps = [1]*6 + [-1]*4


def QG(Bs,a,b,c,d):
    return sum(eps[u]*(Bs[u][a,c]*Bs[u][b,d]
                       - Bs[u][a,d]*Bs[u][b,c]) for u in range(10))


def DQ(Bs,dBs,a,b,c,d):
    return sum(eps[u]*(dBs[u][a,c]*Bs[u][b,d]
                       + Bs[u][a,c]*dBs[u][b,d]
                       - dBs[u][a,d]*Bs[u][b,c]
                       - Bs[u][a,d]*dBs[u][b,c]) for u in range(10))


for slot in [(0,1,0,1),(0,2,1,2),(1,2,1,2),(0,3,2,3)]:
    assert QG([B[u]+t*dB[u] for u in range(10)],*slot)[1] == DQ(B,dB,*slot)

print("PASS: independent Sage QQ replay — ambient-kernel observed rank 10 and exact Gauss first variation")
