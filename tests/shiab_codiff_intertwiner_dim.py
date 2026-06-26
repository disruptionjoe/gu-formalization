#!/usr/bin/env python3
"""Selector multiplicity for the GU shiab: dim Hom_{so(14,C)}(Lambda^2 V (x) S, V (x) S).

GOAL
----
Compute the algebraic multiplicity of natural so(14,C)-equivariant maps

    Phi : Omega^2 (x) S  ->  Omega^1 (x) S

i.e.  dim Hom_{so(14,C)}( Lambda^2 V (x) S , V (x) S )

where
    V          = C^14            (vector rep of so(14,C) = D_7, h.w. omega_1)
    Lambda^2 V = adjoint, dim 91 (h.w. omega_2)
    S          = the so(14) Dirac spinor (dim 128) = S^+ (+) S^- ,
                 S^+ = h.w. omega_7 (dim 64), S^- = h.w. omega_6 (dim 64).

The GU shiab lives in this Hom space. canon/shiab-existence-cl95.md holds the
"uniqueness of the equivariant map / source-forced selector identity" OPEN. This
script settles the ALGEBRAIC multiplicity (an integer) decisively:

    dim = 0  -> no such map (the constructed Clifford contraction would be a
               ghost; "3 generations as proof" loses its carrier).
    dim = 1  -> the equivariant selector is UNIQUELY pinned (up to scale);
               closes the OPEN canon question (uniqueness holds).
    dim > 1  -> residual equivariant freedom (the selector is NOT pinned by
               equivariance alone; an extra choice / observer input is needed).

METHOD
------
We complexify (Spin(9,5) is a non-compact real form of Spin(14,C); the algebraic
Hom-multiplicity is a complexified invariant, identical for so(9,5) and so(14,C)).

Primary method: explicit irreducible decomposition of both tensor products via
the Racah-Speiser / Brauer-Klimyk algorithm (exact integer arithmetic on the
D_7 weight lattice), then

    dim Hom(A, B) = sum_W  m_W(A) * m_W(B)         (Schur's lemma)

Cross-check method (independent): the multiplicity of the trivial rep in
    M_xy = Lambda^2 V (x) (S_x)^* (x) V (x) S_y
computed by the Kostant/Klimyk alternating Weyl-group sum
    m_0(M) = sum_{w in W} (-1)^{l(w)} n_M( w.rho - rho )
with n_M the (Weyl-invariant) weight multiplicities of M obtained by direct
convolution of the four factor weight systems, and W = W(D_7), |W| = 322560.
By Schur, m_0(M_xy) = dim Hom( Lambda^2 V (x) S_x , V (x) S_y ).

NOTHING is tuned. Every number below is the actual computed output.

All weights are stored in DOUBLED integer coordinates (2 * weight) so that
spinor half-integers become exact integers. D_7 has rank 7.
"""

from __future__ import annotations
from itertools import combinations, product
from math import prod

# ----------------------------------------------------------------------------
# D_7 root datum, in orthonormal e-coordinates. Everything in integer arithmetic.
# We store weights in DOUBLED units: stored vector = 2 * (true weight).
# ----------------------------------------------------------------------------
N = 7

# rho = (n-1, n-2, ..., 1, 0); doubled:
RHO2 = tuple(2 * (N - 1 - i) for i in range(N))  # (12,10,8,6,4,2,0)

# Positive roots of D_n: e_i - e_j and e_i + e_j for i<j. (normal units)
POS_ROOTS = []
for i, j in combinations(range(N), 2):
    r_minus = [0] * N; r_minus[i] = 1; r_minus[j] = -1
    r_plus = [0] * N; r_plus[i] = 1; r_plus[j] = 1
    POS_ROOTS.append(tuple(r_minus))
    POS_ROOTS.append(tuple(r_plus))
assert len(POS_ROOTS) == N * (N - 1)  # 42

# Fundamental highest weights we need (doubled units):
OMEGA1_2 = (2, 0, 0, 0, 0, 0, 0)            # vector V
OMEGA2_2 = (2, 2, 0, 0, 0, 0, 0)            # Lambda^2 V (adjoint)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


# ----------------------------------------------------------------------------
# Weight systems (DOUBLED coordinates), each as list of (weight_tuple, mult).
# ----------------------------------------------------------------------------
def spinor_weights(parity):
    """Doubled weights of a half-spinor. parity=0 -> even #minus (S^+, h.w. omega_7),
    parity=1 -> odd #minus (S^-, h.w. omega_6). Each weight has multiplicity 1."""
    out = []
    for signs in product((1, -1), repeat=N):
        nmin = sum(1 for s in signs if s == -1)
        if nmin % 2 == parity:
            out.append(tuple(signs))  # already doubled: 2*(+-1/2) = +-1
    return out


SPLUS = spinor_weights(0)   # 64 weights, even # of minus signs
SMINUS = spinor_weights(1)  # 64 weights, odd  # of minus signs
assert len(SPLUS) == 64 and len(SMINUS) == 64
assert (1, 1, 1, 1, 1, 1, 1) in SPLUS                    # omega_7 highest weight
assert (1, 1, 1, 1, 1, 1, -1) in SMINUS                  # omega_6 highest weight


# ----------------------------------------------------------------------------
# Reflect a (doubled) vector into the dominant chamber of D_7.
# Returns (mu2, sign) where mu2 = w(v2) dominant and sign = det(w) = (-1)^{l(w)},
# or (None, 0) if v2 is SINGULAR (lies on a wall: |v_i| == |v_j| for some i<j).
# Assumes no zero coordinate (true for our Racah-Speiser shifts; asserted).
# ----------------------------------------------------------------------------
def reflect_to_dominant(v2):
    absv = [abs(x) for x in v2]
    assert all(a != 0 for a in absv), f"unexpected zero coordinate: {v2}"
    # singular if two equal absolute values
    if len(set(absv)) != N:
        return None, 0
    # order positions by descending |value|
    order = sorted(range(N), key=lambda k: -absv[k])
    num_neg = sum(1 for x in v2 if x < 0)
    mu2 = [absv[order[k]] for k in range(N)]          # magnitudes, descending
    # D_n: even # of sign flips allowed; first n-1 positive, last sign by parity
    if num_neg % 2 == 1:
        mu2[N - 1] = -mu2[N - 1]
    # sign(w) = det of signed permutation taking v2 -> mu2.
    # Build permutation perm where source axis order[k] maps to row k, entry s_k.
    # det = sign(perm) * prod(s_k).
    perm = order[:]  # perm[k] = source index landing in slot k
    # permutation sign of the map k -> order[k]
    # compute parity of 'order' as a permutation of range(N)
    seen = [False] * N
    perm_sign = 1
    for start in range(N):
        if seen[start]:
            continue
        clen = 0
        x = start
        while not seen[x]:
            seen[x] = True
            x = order[x]
            clen += 1
        if clen % 2 == 0:
            perm_sign = -perm_sign
    sgn_prod = 1
    for k in range(N):
        src = order[k]
        # s_k satisfies mu2[k] = s_k * v2[src]; |mu2[k]| = |v2[src]| so s_k = +-1
        s_k = 1 if (mu2[k] > 0) == (v2[src] > 0) else -1
        sgn_prod *= s_k
    sign = perm_sign * sgn_prod
    return tuple(mu2), sign


# ----------------------------------------------------------------------------
# Racah-Speiser: decompose  V_alpha (x) (rep with weight list beta_weights)
# into irreps. alpha2 = doubled highest weight of the (irreducible) first factor.
# Returns dict: highest_weight_doubled (tuple) -> integer multiplicity.
# ----------------------------------------------------------------------------
def racah_speiser(alpha2, beta_weights):
    res = {}
    for nu2 in beta_weights:
        xi2 = tuple(alpha2[i] + RHO2[i] + nu2[i] for i in range(N))
        mu2, sign = reflect_to_dominant(xi2)
        if mu2 is None:
            continue
        hw2 = tuple(mu2[i] - RHO2[i] for i in range(N))
        res[hw2] = res.get(hw2, 0) + sign
    return {k: v for k, v in res.items() if v != 0}


# ----------------------------------------------------------------------------
# Weyl dimension formula (exact integer), input doubled highest weight.
# dim = prod_{a>0} <lam+rho, a> / <rho, a>  with lam,rho in doubled units the
# factor of 2 cancels in numerator/denominator.
# ----------------------------------------------------------------------------
def weyl_dim(hw2):
    lr2 = tuple(hw2[i] + RHO2[i] for i in range(N))
    num = prod(dot(lr2, a) for a in POS_ROOTS)
    den = prod(dot(RHO2, a) for a in POS_ROOTS)
    assert num % den == 0
    return num // den


def total_dim(dec):
    return sum(m * weyl_dim(hw2) for hw2, m in dec.items())


# ----------------------------------------------------------------------------
# PRIMARY METHOD: decompositions
# ----------------------------------------------------------------------------
print("=" * 80)
print("Selector multiplicity  dim Hom_{so(14,C)}(Lambda^2 V (x) S, V (x) S)")
print("so(14,C) = D_7  (complexification of so(9,5)); exact weight-lattice arithmetic")
print("=" * 80)

dec = {
    ("V", "S+"): racah_speiser(OMEGA1_2, SPLUS),
    ("V", "S-"): racah_speiser(OMEGA1_2, SMINUS),
    ("L2", "S+"): racah_speiser(OMEGA2_2, SPLUS),
    ("L2", "S-"): racah_speiser(OMEGA2_2, SMINUS),
}

# sanity: each decomposition must have total dim = product of factor dims
factor_dim = {"V": 14, "L2": 91, "S+": 64, "S-": 64}
print("\n-- Irreducible decompositions (Racah-Speiser), with dimension check --")
for (A, B), d in dec.items():
    td = total_dim(d)
    expect = factor_dim[A] * factor_dim[B]
    status = "OK" if td == expect else "*** MISMATCH ***"
    print(f"\n{A} (x) {B}:  total dim {td} vs {factor_dim[A]}*{factor_dim[B]}={expect}  [{status}]")
    for hw2, m in sorted(d.items(), key=lambda kv: -weyl_dim(kv[0])):
        hw_str = "(" + ",".join(f"{x/2:g}" for x in hw2) + ")"
        print(f"     mult {m:+d}   dim {weyl_dim(hw2):5d}   h.w.={hw_str}")

# Textbook validation: V (x) S^+ = W(omega_1+omega_7) [dim 832] (+) S^- [dim 64]
vsplus = dec[("V", "S+")]
hw_RS = (3, 1, 1, 1, 1, 1, 1)       # omega_1 + omega_7, doubled
hw_Sm = (1, 1, 1, 1, 1, 1, -1)      # omega_6 = S^-, doubled
ok_textbook = (vsplus.get(hw_RS) == 1 and vsplus.get(hw_Sm) == 1 and len(vsplus) == 2
               and weyl_dim(hw_RS) == 832 and weyl_dim(hw_Sm) == 64)
print(f"\n[textbook check] V (x) S^+ == 832 (+) 64 with the right h.w.s : {ok_textbook}")


def hom_dim(dom, cod):
    """dim Hom(dom, cod) = sum_W m_W(dom) m_W(cod)."""
    s = 0
    for hw2, m in dom.items():
        s += m * cod.get(hw2, 0)
    return s


# Chiral 2x2 block structure of the selector space.
# Clifford contraction Phi(alpha (x) s) = sum_a e^a (x) c(iota_{e_a} alpha) s uses
# ONE Clifford multiplication by a covector -> flips chirality: S^+ -> S^-.
blocks = {}
for sx in ("S+", "S-"):
    for sy in ("S+", "S-"):
        blocks[(sx, sy)] = hom_dim(dec[("L2", sx)], dec[("V", sy)])

print("\n-- Chiral block multiplicities  dim Hom(Lambda^2 V (x) S_x , V (x) S_y) --")
print("        cod S+   cod S-")
for sx in ("S+", "S-"):
    print(f"dom {sx}    {blocks[(sx,'S+')]:6d}   {blocks[(sx,'S-')]:6d}")

# Full Dirac S = S^+ (+) S^-:
cod_full = {}
for d in (dec[("V", "S+")], dec[("V", "S-")]):
    for k, v in d.items():
        cod_full[k] = cod_full.get(k, 0) + v
dom_full = {}
for d in (dec[("L2", "S+")], dec[("L2", "S-")]):
    for k, v in d.items():
        dom_full[k] = dom_full.get(k, 0) + v
dim_full = hom_dim(dom_full, cod_full)

dim_chirality_flipping = blocks[("S+", "S-")] + blocks[("S-", "S+")]
dim_chirality_preserving = blocks[("S+", "S+")] + blocks[("S-", "S-")]

print("\n-- Headline selector multiplicities --")
print(f"  dim Hom(Lambda^2 V (x) S^+ , V (x) S^-)   [the natural chirality-flipping shiab] = {blocks[('S+','S-')]}")
print(f"  dim Hom(Lambda^2 V (x) S^- , V (x) S^+)                                          = {blocks[('S-','S+')]}")
print(f"  dim Hom(Lambda^2 V (x) S^+ , V (x) S^+)   [chirality-preserving]                 = {blocks[('S+','S+')]}")
print(f"  dim Hom(Lambda^2 V (x) S^- , V (x) S^-)                                          = {blocks[('S-','S-')]}")
print(f"  chirality-flipping total                                                         = {dim_chirality_flipping}")
print(f"  chirality-preserving total                                                       = {dim_chirality_preserving}")
print(f"  dim Hom(Lambda^2 V (x) S , V (x) S)  with full Dirac S = S^+(+)S^-               = {dim_full}")


# ----------------------------------------------------------------------------
# CROSS-CHECK METHOD: trivial-rep multiplicity via Kostant/Klimyk Weyl sum.
# dim Hom(L2 (x) S_x, V (x) S_y) = m_0( L2 (x) (S_x)^* (x) V (x) S_y ).
# (S^+)^* = S^- and (S^-)^* = S^+ for D_7 (n odd); as weight SETS, the dual is
# the negated set, which equals the opposite-parity spinor set.
# ----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("CROSS-CHECK: Kostant/Klimyk alternating Weyl-group sum, |W(D_7)| = 322560")
print("=" * 80)

# Weight system of Lambda^2 V (doubled): the 84 roots (mult 1) + zero weight (mult 7=rank).
L2_weights = {}
for i, j in combinations(range(N), 2):
    for si in (1, -1):
        for sj in (1, -1):
            w = [0] * N
            w[i] = 2 * si
            w[j] = 2 * sj
            L2_weights[tuple(w)] = L2_weights.get(tuple(w), 0) + 1
L2_weights[tuple([0] * N)] = L2_weights.get(tuple([0] * N), 0) + N  # zero weight mult = rank
assert sum(L2_weights.values()) == 91

# Vector V weights (doubled): +-2 e_i
V_weights = {}
for i in range(N):
    for s in (2, -2):
        w = [0] * N
        w[i] = s
        V_weights[tuple(w)] = 1
assert sum(V_weights.values()) == 14


def convolve(wa, wb):
    out = {}
    for ka, va in wa.items():
        for kb, vb in wb.items():
            k = tuple(ka[i] + kb[i] for i in range(N))
            out[k] = out.get(k, 0) + va * vb
    return out


# spinor weight systems as mult-1 dicts
SPLUS_d = {w: 1 for w in SPLUS}
SMINUS_d = {w: 1 for w in SMINUS}

base = convolve(L2_weights, V_weights)  # L2 (x) V

# For Hom(L2 (x) S_x, V (x) S_y): factor (S_x)^* (x) S_y.
# (S_x)^* weights = negated S_x = opposite-parity set; combine with S_y.
def spinor_pair(sx, sy):
    sx_dual = SMINUS_d if sx == "S+" else SPLUS_d   # (S^+)^*=S^-, (S^-)^*=S^+
    sy_d = SPLUS_d if sy == "S+" else SMINUS_d
    return convolve(sx_dual, sy_d)


nM = {}
for sx in ("S+", "S-"):
    for sy in ("S+", "S-"):
        nM[(sx, sy)] = convolve(base, spinor_pair(sx, sy))

# Enumerate W(D_7): permutations of N coords x even-sign-flip patterns.
# w: e_i -> eps_i e_{sigma(i)}; det(w) = sign(sigma) * prod(eps) = sign(sigma) (prod=+1).
# (w.rho)_{sigma(i)} = eps_i rho_i  =>  build vector then subtract rho.
def perm_sign(sigma):
    seen = [False] * N
    sgn = 1
    for s in range(N):
        if seen[s]:
            continue
        clen = 0
        x = s
        while not seen[x]:
            seen[x] = True
            x = sigma[x]
            clen += 1
        if clen % 2 == 0:
            sgn = -sgn
    return sgn


from itertools import permutations as _perms

# Precompute even sign patterns (product = +1): 2^(N-1) = 64 of them.
even_signs = [s for s in product((1, -1), repeat=N) if prod(s) == 1]
assert len(even_signs) == 2 ** (N - 1)

klimyk = {key: 0 for key in nM}
RHO2_list = list(RHO2)
W_count = 0
for sigma in _perms(range(N)):
    psign = perm_sign(list(sigma))
    for eps in even_signs:
        W_count += 1
        # w.rho doubled: place eps_i * RHO2[i] into slot sigma[i]
        wrho = [0] * N
        for i in range(N):
            wrho[sigma[i]] = eps[i] * RHO2_list[i]
        target = tuple(wrho[k] - RHO2_list[k] for k in range(N))
        for key, d in nM.items():
            mult = d.get(target)
            if mult:
                klimyk[key] += psign * mult
assert W_count == 322560

print(f"\nEnumerated |W(D_7)| = {W_count} Weyl elements.")
print("\n-- Klimyk trivial-multiplicity m_0(L2 (x) S_x^* (x) V (x) S_y) per block --")
print("        cod S+   cod S-")
for sx in ("S+", "S-"):
    print(f"dom {sx}    {klimyk[(sx,'S+')]:6d}   {klimyk[(sx,'S-')]:6d}")

# Agreement check between the two independent methods.
agree = all(klimyk[(sx, sy)] == blocks[(sx, sy)] for sx in ("S+", "S-") for sy in ("S+", "S-"))
print(f"\n[cross-check] Racah-Speiser blocks == Klimyk Weyl-sum blocks : {agree}")

klimyk_full = sum(klimyk.values())
print(f"[cross-check] full-Dirac total: RS={dim_full}  Klimyk={klimyk_full}  equal={dim_full==klimyk_full}")

print("\n" + "=" * 80)
print("RESULT SUMMARY")
print("=" * 80)
print(f"  natural shiab block  dim Hom(L2 V (x) S^+, V (x) S^-) = {blocks[('S+','S-')]}")
print(f"  full Dirac           dim Hom(L2 V (x) S,   V (x) S)   = {dim_full}")
print("  (both methods agree)" if agree and dim_full == klimyk_full else "  *** METHOD DISAGREEMENT ***")
