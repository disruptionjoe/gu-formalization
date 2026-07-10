#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HOSTILE REFEREE -- independent verification of LEG-A1 (corner (a), leg 1).

Different machinery on every load-bearing item:

  V1  Explicit 32x32 Clifford matrices for Cl(10) (Pauli tensor construction,
      exact Gaussian-integer arithmetic in pure Python): construct the
      conjugation intertwiner B and PROVE conj swaps the two Weyl 16s
      (B Gamma11 B^-1 = -Gamma11).  Control: Spin(8), where conj must
      PRESERVE each Weyl 8 (m even).  This is the load-bearing rep fact
      behind reading (i)'s "rep-theoretically exact".
      [Leg's machinery: weight-set combinatorics.  Mine: explicit matrices.]

  V2  SU(5)xU(1) content of the two 16s read off the SAME explicit matrices
      (diagonal Cartan H_k = -(i/2) G_{2k-1} G_{2k}), not from abstract
      weights: charge spectrum on S+ must be {5/2 x1, 1/2 x10, -3/2 x5} and
      exactly negated on S-.

  V3  Real-Clifford even-algebra types via Bott/tensor-product chains with
      exact integer dimension bookkeeping (NO mod-8 lookup table):
        Cl^0(5,5)  = Cl(5,4) = Cl(1,0) (x) M(2,R)^4 = M(16,R)+M(16,R)
        Cl^0(10,0) = Cl(0,9) = Cl(7,0) (x) H, chain down to M(16,C)
      using only: Cl(1,0)=R+R, Cl(0,1)=C, Cl(2,0)=M(2,R), Cl(0,2)=H,
      Cl(p+1,q+1)=Cl(p,q)(x)M(2,R), Cl(0,q+2)=Cl(q,0)(x)Cl(0,2),
      Cl(p+2,0)=Cl(0,p)(x)Cl(2,0), C(x)C=C+C, C(x)H=M(2,C), H(x)H=M(4,R).

  V4  Index arithmetic re-derived from characteristic classes (Fractions):
      Ahat(K3) = 1 - p1/24 integrated = -sigma/8 = 2 ;
      ind(D (x) T_C) = int (1 - p1/24)(4 + p1) = (5/6) * 3 sigma = -40 ;
      B = -40+2 = -38 = 19 sigma/8 ; A = -40-2 = -42 = 21 sigma/8 ;
      h^{1,1}(K3) = b2 - 2 h^{2,0} = 22 - 2 = 20 ; dim ker = 2 h11 - 2 = 38
      = 14+12+12 ; ind = -dim ker (ker+ = 0).

  V5  My own needle checks (own normalizer) on the primary transcript:
      the decisive quotes, ZERO occurrences of 'massless', and the TWO
      passages the leg OMITTED that bear on the corner-open case:
        O1 [00:36:13] 'you want a zero in a self adjoint operator'
        O2 [00:42:42+] 'The Higgs is an illusion' ... 'Minimal coupling and
           Yukawa coupling are the same thing'

  V6  GP-hypothesis audit: the fetched abstract contains NO chirality /
      unpairedness hypothesis -- flag the leg's Section-2 wording ('only
      whether an UNPAIRED massless chiral family is asserted') as too strong:
      a PAIRED massless coupled spin-3/2 engages GP equally.

FIREWALL: sigma = -16 only; Ahat from sigma; no chi(K3); no /8 manufacture;
58.72 never touched.  Exit 0 iff all checks pass.
"""

import re, sys
from fractions import Fraction as Fr
from pathlib import Path

REPO = Path(r"C:\Users\joe\JB\CapacityOS\repos\public\gu-formalization")
N = 0
def check(cond, label):
    global N
    N += 1
    if not cond:
        print(f"REFEREE FAIL [{N:02d}] {label}")
        sys.exit(1)
    print(f"REFEREE PASS [{N:02d}] {label}")

# ---------------------------------------------------------------------------
# V1 -- explicit Clifford matrices, exact Gaussian-integer arithmetic
# ---------------------------------------------------------------------------
print("=" * 78)
print("V1: explicit Cl(2m) matrices -- conjugation swaps Weyl reps iff m odd")
print("=" * 78)

# exact 2x2 blocks over Gaussian integers, represented as ((re, im)) int pairs
def gi(re, im=0): return (re, im)
def gadd(a, b): return (a[0] + b[0], a[1] + b[1])
def gmul(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def gneg(a): return (-a[0], -a[1])
def gconj(a): return (a[0], -a[1])
Z, ONE, I_ = gi(0), gi(1), gi(0, 1)

S1 = [[Z, ONE], [ONE, Z]]
S2 = [[Z, gneg(I_)], [I_, Z]]
S3 = [[ONE, Z], [Z, gneg(ONE)]]
ID2 = [[ONE, Z], [Z, ONE]]

def kron(A, B):
    na, nb = len(A), len(B)
    return [[gmul(A[i // nb][j // nb], B[i % nb][j % nb])
             for j in range(na * nb)] for i in range(na * nb)]

def matmul(A, B):
    n = len(A)
    return [[_dot(A[i], B, j, n) for j in range(n)] for i in range(n)]
def _dot(row, B, j, n):
    acc = Z
    for k in range(n):
        if row[k] != Z and B[k][j] != Z:
            acc = gadd(acc, gmul(row[k], B[k][j]))
    return acc

def mconj(A):  return [[gconj(x) for x in row] for row in A]
def mneg(A):   return [[gneg(x) for x in row] for row in A]
def msca(c, A):return [[gmul(c, x) for x in row] for row in A]
def meq(A, B): return A == B
def ident(n):  return [[ONE if i == j else Z for j in range(n)] for i in range(n)]

def build_gammas(m):
    """2m Euclidean gammas, dim 2^m, standard recursive Pauli construction.
       G_{2k-1} = s3^{(k-1)} (x) s1 (x) 1^(m-k);  G_{2k} = ... s2 ..."""
    gams = []
    for k in range(1, m + 1):
        for s in (S1, S2):
            M = None
            for pos in range(1, m + 1):
                blk = S3 if pos < k else (s if pos == k else ID2)
                M = blk if M is None else kron(M, blk)
            gams.append(M)
    return gams

def clifford_ok(gams, dim):
    for a in range(len(gams)):
        for b in range(a, len(gams)):
            AB = matmul(gams[a], gams[b])
            BA = matmul(gams[b], gams[a])
            anti = [[gadd(AB[i][j], BA[i][j]) for j in range(dim)] for i in range(dim)]
            want = msca(gi(2), ident(dim)) if a == b else [[Z]*dim for _ in range(dim)]
            if not meq(anti, want):
                return False
    return True

def chirality(gams, m, dim):
    """Gamma_{2m+1} = (-i)^m G1...G_{2m}; check it squares to 1, diagonal +-1."""
    P = ident(dim)
    for G in gams:
        P = matmul(P, G)
    phase = ONE
    for _ in range(m):
        phase = gmul(phase, gneg(I_))       # (-i)^m
    return msca(phase, P)

def run_case(m):
    dim = 2 ** m
    gams = build_gammas(m)
    check(clifford_ok(gams, dim), f"n={2*m}: Clifford relations exact on {dim}x{dim} matrices")
    G = chirality(gams, m, dim)
    check(meq(matmul(G, G), ident(dim)), f"n={2*m}: chirality^2 = 1")
    diag_ok = all(G[i][j] == (Z if i != j else G[i][i]) and
                  (i != j or G[i][i] in (ONE, gneg(ONE))) for i in range(dim) for j in range(dim))
    check(diag_ok, f"n={2*m}: chirality diagonal with entries +-1")
    trace = sum(G[i][i][0] for i in range(dim))
    check(trace == 0, f"n={2*m}: tr(chirality) = 0 (two Weyl reps of dim {dim//2})")
    # conjugation intertwiner: B = product of the imaginary gammas (even index)
    B = ident(dim)
    for k in range(1, len(gams), 2):        # gams[1], gams[3], ... are the s2-type
        B = matmul(B, gams[k])
    # verify uniform intertwining: Gamma_a^* = eps * B Gamma_a B^{-1}
    Binv = ident(dim)
    # B is a product of m anticommuting gammas: B^2 = (-1)^{m(m-1)/2} * 1
    B2 = matmul(B, B)
    sgn = (-1) ** (m * (m - 1) // 2)
    check(meq(B2, msca(gi(sgn), ident(dim))), f"n={2*m}: B^2 = {sgn} * 1 (so B^-1 = {sgn} * B)")
    Binv = msca(gi(sgn), B)
    eps_seen = set()
    for a, Ga in enumerate(gams):
        BGB = matmul(matmul(B, Ga), Binv)
        Gc = mconj(Ga)
        if meq(Gc, BGB):        eps_seen.add(+1)
        elif meq(Gc, mneg(BGB)): eps_seen.add(-1)
        else:                    eps_seen.add(0)
    check(eps_seen in ({+1}, {-1}),
          f"n={2*m}: uniform eps: Gamma_a^* = {eps_seen} * B Gamma_a B^-1 for ALL a "
          "(=> Sigma_ab^* = B Sigma_ab B^-1: B intertwines the conjugate spin rep)")
    # the verdict: does conjugation swap the Weyl spaces?
    BGB = matmul(matmul(B, G), Binv)
    Gc = mconj(G)
    if meq(Gc, mneg(BGB)):
        return "SWAP"
    if meq(Gc, BGB):
        return "FIX"
    return "??"

res10 = run_case(5)
check(res10 == "SWAP",
      "Spin(10) [m=5 ODD]: B Gamma11 B^-1 = -Gamma11^* -- complex conjugation "
      "SWAPS the two Weyl 16s: conj(16) = 16bar.  Reading (i)'s rep fact "
      "CONFIRMED by explicit matrices (independent of weight combinatorics)")
res8 = run_case(4)
check(res8 == "FIX",
      "Spin(8) control [m=4 EVEN]: conjugation FIXES each Weyl 8 -- the swap "
      "is NOT an artifact of the construction; the m-parity dependence is real")

# ---------------------------------------------------------------------------
# V2 -- SU(5)xU(1) content from the explicit Cartan (not abstract weights)
# ---------------------------------------------------------------------------
print("=" * 78)
print("V2: U(1) charge spectrum on the two 16s, read off the explicit matrices")
print("=" * 78)

m = 5; dim = 32
gams = build_gammas(m)
G11 = chirality(gams, m, dim)
# H_k = -(i/2) G_{2k-1} G_{2k}: verify diagonal with entries +-1/2 (use 2H_k, integer)
charges = [0] * dim
for k in range(m):
    P = matmul(gams[2*k], gams[2*k + 1])          # G_{2k-1} G_{2k}
    H2 = msca(gneg(I_), P)                        # 2 H_k = -i G G'
    ok = all(H2[i][j] == Z for i in range(dim) for j in range(dim) if i != j) and \
         all(H2[i][i] in (ONE, gneg(ONE)) for i in range(dim))
    check(ok, f"2*H_{k+1} diagonal, entries +-1")
    for i in range(dim):
        charges[i] += H2[i][i][0]                 # 2*charge accumulates
# split by chirality and count charge multiplicities (charges are 2*q, integers)
from collections import Counter
plus  = Counter(charges[i] for i in range(dim) if G11[i][i] == ONE)
minus = Counter(charges[i] for i in range(dim) if G11[i][i] == gneg(ONE))
check(sum(plus.values()) == 16 and sum(minus.values()) == 16, "16 + 16 chirality split")
want = Counter({5: 1, 1: 10, -3: 5})              # 2q in {5,1,-3}
wantn = Counter({-5: 1, -1: 10, 3: 5})
check(plus == want or plus == wantn,
      "S+ charge spectrum = {5/2 x1, 1/2 x10, -3/2 x5} (up to overall sign conv): "
      f"got {dict(plus)}")
check(minus == (wantn if plus == want else want),
      "S- spectrum is the EXACT negation -- 'conjugate of the internal symmetry "
      f"representation' verified on explicit matrices: got {dict(minus)}")

# ---------------------------------------------------------------------------
# V3 -- even-algebra types via Bott/tensor chains (no mod-8 lookup)
# ---------------------------------------------------------------------------
print("=" * 78)
print("V3: Cl^0(5,5) and Cl^0(10,0) by tensor-product chains, exact dims")
print("=" * 78)

# algebra of types: ('R'|'C'|'H'|'R2'|'C2'|'H2', k) meaning M(k,F) or M(k,F)^2
def tensor(t1, t2):
    (f1, k1), (f2, k2) = t1, t2
    # peel off double factors: (F^2 (x) G) = (F (x) G)^2
    dbl = f1.endswith('2') + f2.endswith('2')
    f1, f2 = f1.rstrip('2'), f2.rstrip('2')
    table = {('R','R'):('R',1), ('R','C'):('C',1), ('R','H'):('H',1),
             ('C','R'):('C',1), ('C','C'):('C2',1), ('C','H'):('C',2),
             ('H','R'):('H',1), ('H','C'):('C',2), ('H','H'):('R',4)}
    f, kf = table[(f1, f2)]
    k = k1 * k2 * kf
    if dbl == 1: f += '2' if not f.endswith('2') else ''
    assert dbl <= 1
    return (f, k)

def rdim(t):
    f, k = t
    base = {'R':1, 'C':2, 'H':4, 'R2':2, 'C2':4, 'H2':8}[f]
    return base * k * k

Cl10, Cl01, Cl20, Cl02, M2R = ('R2',1), ('C',1), ('R',2), ('H',1), ('R',2)
check(rdim(Cl10) == 2 and rdim(Cl01) == 2 and rdim(Cl20) == 4 and rdim(Cl02) == 4,
      "seed dims: Cl(1,0)=R+R, Cl(0,1)=C, Cl(2,0)=M(2,R), Cl(0,2)=H")

# Cl^0(5,5) = Cl(5,4) = Cl(1,0) (x) M(2,R)^{(x)4}   [Cl(p+1,q+1) = Cl(p,q) (x) M(2,R)]
t = Cl10
for _ in range(4):
    t = tensor(t, M2R)
check(t == ('R2', 16) and rdim(t) == 2 ** 9,
      "Cl^0(5,5) = Cl(5,4) = M(16,R)+M(16,R)  [Bott chain; two SELF-CONJUGATE "
      "real MW 16s -- the split-form control, independent of any lookup table]")

# Cl^0(10,0) = Cl(0,9) = Cl(7,0) (x) Cl(0,2);  Cl(7,0) = Cl(0,5) (x) Cl(2,0);
# Cl(0,5) = Cl(3,0) (x) Cl(0,2);  Cl(3,0) = Cl(0,1) (x) Cl(2,0)
Cl30 = tensor(Cl01, Cl20); check(Cl30 == ('C', 2) and rdim(Cl30) == 8,  "Cl(3,0) = M(2,C)")
Cl05 = tensor(Cl30, Cl02); check(Cl05 == ('C', 4) and rdim(Cl05) == 32, "Cl(0,5) = M(4,C)")
Cl70 = tensor(Cl05, Cl20); check(Cl70 == ('C', 8) and rdim(Cl70) == 128,"Cl(7,0) = M(8,C)")
Cl09 = tensor(Cl70, Cl02); check(Cl09 == ('C', 16) and rdim(Cl09) == 512,
      "Cl^0(10,0) = Cl(0,9) = M(16,C) -- complex type: the two Weyl 16s are a "
      "conjugate PAIR (matches V1's explicit-matrix SWAP)")

# ---------------------------------------------------------------------------
# V4 -- index arithmetic from characteristic classes (Fractions only)
# ---------------------------------------------------------------------------
print("=" * 78)
print("V4: -40 / -38 / -42 / 38 re-derived from characteristic classes")
print("=" * 78)

sigma = -16                              # signature of K3 (the ONLY topological input)
p1 = 3 * sigma                           # signature theorem: sigma = p1/3
check(p1 == -48, "int_K3 p1 = 3 sigma = -48 (signature theorem)")
ind_D = Fr(-p1, 24)                      # Ahat = 1 - p1/24 -> int Ahat = -p1/24
check(ind_D == 2 == Fr(-sigma, 8), "ind D = -p1/24 = -sigma/8 = 2 (firewall: sigma only)")
# ch(T_C) = rk + ch2, rk = 4, ch2(V (x) C) = p1(V):  ind(D (x) T_C) = int Ahat*ch
ind_DT = 4 * ind_D + Fr(0) + p1          # deg-4 terms: Ahat_0*ch_2 + Ahat_4*ch_0
# careful: int (1 - p1/24)(4 + p1) = int(p1) - 4*int(p1)/24 = p1 (1 - 1/6) = (5/6) p1
ind_DT = Fr(5, 6) * p1
check(ind_DT == -40, "ind(D (x) T_C) = (5/6) * 3 sigma = -40 (the bare control row)")
check(ind_DT + ind_D == -38 == Fr(19, 8) * sigma, "carrier B: -40 + 2 = -38 = 19 sigma/8")
check(ind_DT - ind_D == -42 == Fr(21, 8) * sigma, "carrier A: -40 - 2 = -42 = 21 sigma/8")
check((ind_DT + ind_D) - (ind_DT - ind_D) == 4 == 2 * ind_D,
      "fork = 4 = two spin-1/2 units")
b2, h20 = 22, 1
h11 = b2 - 2 * h20
check(h11 == 20, "h^{1,1}(K3) = b2 - 2 h^{2,0} = 20")
check(2 * h11 - 2 == 38 == 14 + 12 + 12, "dim ker Q = 2 h11 - 2 = 38 = 14+12+12")
check(-(2 * h11 - 2) == ind_DT + ind_D,
      "ind Q = -dim ker Q (ker+ = 0): the -38 counts one-chirality FIBER zero modes")

# ---------------------------------------------------------------------------
# V5 -- my own needle checks on the primary transcript (own normalizer)
# ---------------------------------------------------------------------------
print("=" * 78)
print("V5: transcript needles with an independent normalizer + omission audit")
print("=" * 78)

TXT = (REPO / "papers" / "drafts" / "Transcript into the impossible.md").read_text(
    encoding="utf-8", errors="replace")
low = re.sub(r"\s+", " ", TXT.lower())

def has(s): return re.sub(r"\s+", " ", s.lower()) in low

check(has("So in g u, there's one family of 16 flipped chiral spin three halves "
          "particles. That is, there is a sort of spin three halves family, which "
          "aside from being spin three halves is just the conjugate of the internal "
          "symmetry representation."),
      "P1 verbatim (the apposition) -- independently re-verified")
check(has("the fermionic extension gives you exactly three families of chiral "
          "fermions if you have a decreased VEV"),
      "P3 verbatim (decreased VEV / chiral families) -- independently re-verified")
check(has("because the mass is actually a variable"), "P3b 'mass is actually a variable'")
check("massless" not in low,
      "ZERO occurrences of 'massless' in the primary transcript -- BOTTOM LINE 1's "
      "textual basis independently confirmed")
# the two OMITTED corner-open-relevant passages (leg's Section 5 does not cite them):
check(has("you want a zero in a self adjoint operator"),
      "OMISSION O1 exists: [00:36:13] GU's rolled-up (RS-containing) mass operator "
      "is DESIGNED with a zero eigenvalue (seesaw) -- corner-open-relevant, not "
      "cited by the leg")
check(has("The Higgs is an illusion"),
      "OMISSION O2a exists: [00:42:42] no independent Higgs sector")
check(has("Minimal coupling and Yukawa coupling are the same thing"),
      "OMISSION O2b exists: [00:43:04] ONE mass mechanism (Yukawa = minimal "
      "coupling) -- affirmative support for the open case's single-dial conjunct, "
      "stronger than the leg's 'nothing in the transcript says otherwise'")
check(has("these would be the analogs of quarks"),
      "OMISSION O3 (minor) exists: [00:41:24] quark/antiquark analogs -- extra "
      "support for GP's couplings hypothesis (colored content)")

# ---------------------------------------------------------------------------
# V6 -- GP hypothesis audit: no unpairedness/chirality hypothesis in the abstract
# ---------------------------------------------------------------------------
print("=" * 78)
print("V6: GP abstract hypothesis audit")
print("=" * 78)

L1 = (REPO / "tests" / "carrier-bit-decision" / "leg1_applicability_matrix.md"
      ).read_text(encoding="utf-8", errors="replace")
L1 = re.sub(r"(?m)^\s*>\s?", " ", L1)      # strip blockquote markers (md wrap)
l1low = re.sub(r"\s+", " ", L1.lower())
gp = ("if massless fermions of spin 3/2 have non-vanishing low-energy couplings, "
      "the fermions must have massless partners of spin 2, and all particles to "
      "which the fermions couple must display supersymmetry.")
check(gp in l1low, "GP abstract verbatim in the repo cache -- re-verified")
check("unpaired" not in gp and "chiral" not in gp and "vectorlike" not in gp,
      "GP's fetched hypotheses are MASSLESS + COUPLINGS only -- no chirality / "
      "unpairedness hypothesis: a PAIRED (vectorlike) massless coupled spin-3/2 "
      "engages GP equally; the leg's 'only whether an UNPAIRED massless chiral "
      "family is asserted' is too strong AS WORDED (its Section 5 prong 1 "
      "already uses the correct criterion)")

print("=" * 78)
print(f"ALL {N} REFEREE CHECKS PASS.  Load-bearing items independently confirmed;")
print("omissions O1/O2 documented (corner-open case understated, LOW severity);")
print("wording flag on 'unpaired' documented.  Exit 0.")
print("=" * 78)
