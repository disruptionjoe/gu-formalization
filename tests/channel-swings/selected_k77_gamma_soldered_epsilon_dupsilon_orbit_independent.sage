#!/usr/bin/env sage
"""Independent QQ certificate for the K77 gamma-soldered epsilon orbit."""

def packet(q):
    q = vector(QQ, q)
    pairs = [(a,b) for a in range(4) for b in range(a+1,4)]
    B = matrix(QQ, 24, 6)
    for mu in range(4):
        for j in range(6):
            B[6*mu+j,j] = q[mu]
    E = matrix(QQ, 6, 4)
    for j,(a,b) in enumerate(pairs):
        for nu in range(4):
            E[j,nu] = (q[a]*(1 if b==nu else 0)-q[b]*(1 if a==nu else 0))/2
    C = -B*E
    G = matrix(QQ, 16, 4)
    for mu in range(4):
        for nu in range(4):
            G[4*mu+nu,nu] = q[mu]
    D = matrix(QQ, 10, 4, lambda i,j: 1 if i==j else 0)
    return B,E,C,G,D

for q in ((1,0,0,0),(0,1,0,0),(1,0,0,1)):
    B,E,C,G,D = packet(q)
    assert B.rank() == 6
    assert E.rank() == 3
    assert C.rank() == 3
    assert (B*E + C).is_zero()
    assert E.right_kernel() == C.right_kernel()
    assert G.rank() == 4
    combined = block_matrix(QQ, 2, 1, [C,-G])
    assert combined.rank() == 4
    L = (D.transpose()*D).inverse()*D.transpose()
    Jg = -combined*L
    assert (Jg*D + combined).is_zero()
    assert Jg.rank() == 4
    assert (identity_matrix(QQ,10)-D*L).rank() == 6

print("PASS 30/30")
