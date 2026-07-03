#!/usr/bin/env python3
"""INDEPENDENT check of dim Hom(L2 V (x) S+, V (x) S-) = 2, a DIFFERENT route
than the target script.

Target computes trivial-rep mult of a 4-factor product (L2 (x) Sx* (x) V (x) Sy).
Here instead:
  V (x) S- = W(omega_1+omega_6)[dim832] (+) W(omega_7)=S+[dim64]  (textbook, mirror).
So dim Hom(L2 (x) S+, V (x) S-)
   = mult_{L2 (x) S+}(omega_1+omega_6) + mult_{L2 (x) S+}(omega_7),
each multiplicity computed by the Kostant/Weyl-Klimyk irrep-multiplicity formula
   mult_M(lambda) = sum_{w in W} (-1)^{l(w)} m_M( w(lambda+rho) - rho )
applied DIRECTLY to the 2-factor rep M = L2 (x) S+ (weight-mult by convolution).
Doubled coords. |W(D_7)| = 322560.
"""
from itertools import combinations, product, permutations
from math import prod

N = 7
RHO2 = tuple(2*(N-1-i) for i in range(N))

def l2_weights():
    d = {}
    for i, j in combinations(range(N), 2):
        for si in (2, -2):
            for sj in (2, -2):
                w = [0]*N; w[i] = si; w[j] = sj
                d[tuple(w)] = d.get(tuple(w), 0)+1
    z = tuple([0]*N); d[z] = d.get(z, 0)+N
    return d

def spinor_weights(parity):
    return {tuple(s): 1 for s in product((1,-1), repeat=N)
            if sum(1 for x in s if x < 0) % 2 == parity}

def convolve(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(ka[i]+kb[i] for i in range(N))
            out[k] = out.get(k, 0)+va*vb
    return out

L2 = l2_weights()
Sp = spinor_weights(0)
M = convolve(L2, Sp)               # L2 (x) S+ , total dim must be 91*64=5824
assert sum(M.values()) == 91*64

even_signs = [s for s in product((1,-1), repeat=N) if prod(s) == 1]

def mult_of(lam2):
    lr = tuple(lam2[i]+RHO2[i] for i in range(N))   # doubled lambda+rho
    total = 0
    for sigma in permutations(range(N)):
        # perm sign
        seen = [False]*N; psign = 1
        for s in range(N):
            if seen[s]: continue
            c = 0; x = s
            while not seen[x]:
                seen[x] = True; x = sigma[x]; c += 1
            if c % 2 == 0: psign = -psign
        for eps in even_signs:
            # w(lambda+rho): place eps_i*lr[i] into slot sigma[i]
            wv = [0]*N
            for i in range(N):
                wv[sigma[i]] = eps[i]*lr[i]
            target = tuple(wv[k]-RHO2[k] for k in range(N))
            m = M.get(target)
            if m:
                total += psign*m
    return total

# highest weights (doubled) of the two constituents of V (x) S-:
hw_832 = (3,1,1,1,1,1,-1)   # omega_1 + omega_6
hw_64  = (1,1,1,1,1,1,1)    # omega_7  (= S+)
m832 = mult_of(hw_832)
m64 = mult_of(hw_64)
print("mult_{L2(x)S+}(omega_1+omega_6) [dim832] =", m832)
print("mult_{L2(x)S+}(omega_7=S+)      [dim64 ] =", m64)
print("dim Hom(L2(x)S+, V(x)S-) = m832 + m64 =", m832+m64)
