#!/usr/bin/env python3
"""
Independent cross-check of pati_salam_chain_verification.py.

Builds explicit 32x32 gamma matrices for an SO(10) Clifford algebra, forms the
chirality operator, projects onto each 16, and reads the Cartan eigenvalues
(weights) directly from the matrices -- no reference to the paper's weight
diagram. It then recomputes B-L, T3L, T3R, Y = T3R + (B-L)/2, n = 6Y and confirms
one chirality reproduces the Standard Model one-generation table (= the paper's
n=1 table) while the other reproduces its CP conjugate (the anti-generation).

Chirality convention: which 16 is "S^+" is a pure sign convention in the
chirality operator. Both chiralities are one generation; they are CP conjugates
(n -> -n, rep -> conjugate rep).

Deps: numpy
"""
import numpy as np
from collections import defaultdict, Counter

sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

def kron(*mats):
    out = np.array([[1]], dtype=complex)
    for m in mats:
        out = np.kron(out, m)
    return out

k = 5  # SO(10): 10 gammas, 2^5 = 32 dim spinor
gammas = []
for a in range(1, k + 1):
    left = [sz] * (a - 1)
    right = [I2] * (k - a)
    gammas.append(kron(*left, sx, *right))
    gammas.append(kron(*left, sy, *right))

ok_clifford = all(
    np.allclose(gammas[p] @ gammas[q] + gammas[q] @ gammas[p],
                2 * (p == q) * np.eye(32))
    for p in range(10) for q in range(10))
print("[%s] explicit 32x32 gammas satisfy SO(10) Clifford algebra"
      % ("OK" if ok_clifford else "FAIL"))

G = gammas[0].copy()
for g in gammas[1:]:
    G = G @ g
Gchi = ((-1j) ** k) * G
ok_chi = np.allclose(Gchi @ Gchi, np.eye(32)) and np.allclose(Gchi, Gchi.conj().T)
print("[%s] chirality operator Hermitian and squares to identity"
      % ("OK" if ok_chi else "FAIL"))
chi_diag = np.diag(Gchi).real
dimplus = int(round(sum(chi_diag > 0)))
print("[%s] +chirality subspace (the 16) has dim %d"
      % ("OK" if dimplus == 16 else "FAIL", dimplus))

sigmas = [0.5j * gammas[2*a] @ gammas[2*a + 1] for a in range(k)]
weights = np.array([np.diag(s).real for s in sigmas]).T

def multiplets_for(weight_rows):
    recs = []
    for w in weight_rows:
        s1, s2, s3, s4, s5 = w
        t3l = (s4 + s5) / 2
        t3r = (s4 - s5) / 2
        bl = -(2/3) * (s1 + s2 + s3)
        n = int(round(6 * (t3r + bl/2)))
        nminus = sum(1 for c in (s1, s2, s3) if c < 0)
        su3 = "1" if nminus in (0, 3) else ("3" if bl > 0 else "3bar")
        recs.append((round(bl, 3), round(t3r, 3), round(t3l, 3), su3, n))
    grp = defaultdict(list)
    for bl, t3r, t3l, su3, n in recs:
        grp[(bl, t3r)].append((t3l, su3, n))
    out = Counter()
    for _, mem in grp.items():
        su2 = len({m[0] for m in mem})
        su3 = mem[0][1]
        n = mem[0][2]
        su3dim = len(mem) // su2
        out[(su3, su2, n, su3dim * su2)] += 1
    return out

plus16 = multiplets_for(weights[chi_diag > 0])
minus16 = multiplets_for(weights[chi_diag < 0])

sm_table = Counter({
    ("3",    2,  1, 6): 1,
    ("3bar", 1,  2, 3): 1,
    ("3bar", 1, -4, 3): 1,
    ("1",    2, -3, 2): 1,
    ("1",    1,  6, 1): 1,
    ("1",    1,  0, 1): 1,
})

def conj(counter):
    swap = {"3": "3bar", "3bar": "3", "1": "1"}
    return Counter({(swap[s], su2, -n, d): v for (s, su2, n, d), v in counter.items()})

print("")
print("+chirality multiplets (SU3, SU2_L, n=6Y, dim):")
for kk, v in sorted(plus16.items(), key=lambda kv: (-kv[0][3], kv[0][2])):
    print("   %s x%d" % (kk, v))
print("-chirality multiplets (SU3, SU2_L, n=6Y, dim):")
for kk, v in sorted(minus16.items(), key=lambda kv: (-kv[0][3], kv[0][2])):
    print("   %s x%d" % (kk, v))

plus_is_paper = (plus16 == sm_table)
minus_is_paper = (minus16 == sm_table)
one_matches = plus_is_paper or minus_is_paper
conj_consistent = (minus16 == conj(plus16))
tot_ok = (sum(d for (_, _, _, d) in plus16) == 16
          and sum(d for (_, _, _, d) in minus16) == 16)
print("")
print("[%s] one chirality == paper n=1 table (%s chirality matches)"
      % ("OK" if one_matches else "FAIL", "+" if plus_is_paper else "-"))
print("[%s] the other chirality is its exact CP conjugate"
      % ("OK" if conj_consistent else "FAIL"))
print("[%s] each chirality totals 16 states" % ("OK" if tot_ok else "FAIL"))
print("=" * 60)
allok = ok_clifford and ok_chi and one_matches and conj_consistent and tot_ok
print("CROSS-CHECK %s" % ("PASSED" if allok else "FAILED"))
