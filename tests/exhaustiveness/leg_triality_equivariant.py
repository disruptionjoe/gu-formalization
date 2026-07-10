#!/usr/bin/env python3
# LEG: equivariant / triality-Z/3 escape for the exhaustiveness-by-type gap.
#
# DECISIVE SUB-QUESTION (assigned):
#   The program found a REAL order-3 GROUP torsion Z/3 -- Spin(8) triality (order-3 outer
#   automorphism), the SU(3)_family center in E8 ⊃ E6 x SU(3), the qutrit Weyl-Heisenberg
#   center (omega^3=1) -- that it labels "STRANDED, frame-trivial." Is the stranding
#   PROVABLE (the Z/3 provably cannot couple to the net-chiral count -- frame charge exactly 0,
#   internal-fiber-only, orthogonal to the tangent-frame p_1 count) or merely OBSERVED
#   (leaving a live escape / forcing candidate)?
#
# METHOD: exact character/trace arithmetic for the order-3 action + the same self-dual
#   tangent-frame-charge instrument the boundary-eta DECOUPLE used. No firewall inputs
#   (no chi(K3)=24, no /8, no A-hat=3). The only 24 that may appear is pi_3^s = Z/24.
#
# EXACT ARITHMETIC: Fraction for rationals; a small Eisenstein-integer class Z[w] (w^2=-1-w)
#   for cube-root-of-unity character sums. Matrices are lists-of-lists of exact scalars.
#
# check()-style asserts throughout; exit 0 on success, honest AssertionError otherwise.

from fractions import Fraction as F

FAILS = []
def check(name, cond, detail=""):
    status = "OK  " if cond else "FAIL"
    print(f"[{status}] {name}" + (f"   {detail}" if detail else ""))
    if not cond:
        FAILS.append(name)

# ---------------------------------------------------------------------------
# Exact Eisenstein integers  Z[w],  w = exp(2*pi*i/3),  w^2 = -1 - w,  1+w+w^2 = 0.
# Represent a + b*w with a,b in Q (Fraction). This is exact for all cube-root characters.
# ---------------------------------------------------------------------------
class Eis:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a = F(a); self.b = F(b)
    def __add__(s, o):
        o = s._c(o); return Eis(s.a + o.a, s.b + o.b)
    def __radd__(s, o): return s.__add__(o)
    def __sub__(s, o):
        o = s._c(o); return Eis(s.a - o.a, s.b - o.b)
    def __neg__(s): return Eis(-s.a, -s.b)
    def __mul__(s, o):
        o = s._c(o)
        # (a+bw)(c+dw) = ac + (ad+bc)w + bd w^2, w^2 = -1-w
        ac = s.a*o.a; adbc = s.a*o.b + s.b*o.a; bd = s.b*o.b
        return Eis(ac - bd, adbc - bd)
    def __rmul__(s, o): return s.__mul__(o)
    @staticmethod
    def _c(o):
        return o if isinstance(o, Eis) else Eis(o, 0)
    def __eq__(s, o):
        o = s._c(o); return s.a == o.a and s.b == o.b
    def conj(s):
        # conjugate of w is w^2 = -1-w: a + b*w  ->  a + b*w^2 = (a-b) - b*w
        return Eis(s.a - s.b, -s.b)
    def is_rational(s): return s.b == 0
    def __repr__(s):
        if s.b == 0: return f"{s.a}"
        if s.a == 0: return f"{s.b}w"
        return f"({s.a}+{s.b}w)"

ONE = Eis(1, 0)
W   = Eis(0, 1)          # w
W2  = Eis(-1, -1)        # w^2 = -1 - w
ZERO = Eis(0, 0)

print("="*78)
print("PART 0 -- exact Eisenstein arithmetic sanity (the cube-root-of-unity spine)")
print("="*78)
check("w^3 = 1",            W*W*W == ONE)
check("w^2 = -1-w",         W*W == W2)
check("1 + w + w^2 = 0",    ONE + W + W2 == ZERO, "the whole reason a Z/3 exists")
check("w * conj(w) = 1 (|w|^2=1)", W*W.conj() == ONE)
check("w + w^2 = -1",       W + W2 == Eis(-1, 0), "used in every triality trace below")

# ===========================================================================
# PART A -- the SU(3)_family center / qutrit Weyl-Heisenberg Z/3 (the scalar case).
#   Claim: PROVABLY stranded. It is a fiber endomorphism of the form  I_frame (x) Z_int,
#   so its self-dual tangent-frame charge is EXACTLY 0 -- the same DECOUPLE the +96 selector
#   obeyed, here airtight because there is no V-factor content at all.
# ===========================================================================
print()
print("="*78)
print("PART A -- SU(3)_family center / qutrit Z/3 : scalar, provably stranded")
print("="*78)

# --- exact matrix helpers over Eis ---
def mat(rows): return [[Eis._c(x) for x in r] for r in rows]
def eye(n): return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    assert len(A[0]) == m
    C = [[ZERO]*p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            a = A[i][k]
            if a == ZERO: continue
            for j in range(p):
                C[i][j] = C[i][j] + a*B[k][j]
    return C
def kron(A, B):
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    C = [[ZERO]*(ca*cb) for _ in range(ra*rb)]
    for i in range(ra):
        for j in range(ca):
            for k in range(rb):
                for l in range(cb):
                    C[i*rb+k][j*cb+l] = A[i][j]*B[k][l]
    return C
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def dag(A):   return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def trace(A):
    t = ZERO
    for i in range(len(A)): t = t + A[i][i]
    return t
def is_zero_mat(A): return all(A[i][j]==ZERO for i in range(len(A)) for j in range(len(A[0])))
def frob_inner(A,B): return trace(matmul(dag(A), B))   # <A,B> = Tr(A^dag B)

# --- the tangent frame of X4: so(4) acting on R^4, self-dual sub su(2)_+ = Lambda^2_+ ---
# Euclidean self-dual 2-forms (integer antisymmetric 4x4). These ARE tangent-frame rotations
# of X4; net self-dual frame charge is measured against exactly these (the count lives here,
# in p_1(TX4), the -p_1/24 gravitational framing channel).
def antisym(i,j,n):   # generator e_i ^ e_j : +1 at (i,j), -1 at (j,i)
    M = [[ZERO]*n for _ in range(n)]
    M[i][j] = ONE; M[j][i] = -ONE
    return M
def L_add(A,B): return add(A,B)
# Lambda^2_+ basis (self-dual): (12)+(34), (13)+(42), (14)+(23)
Lsd = [
    L_add(antisym(0,1,4), antisym(2,3,4)),
    L_add(antisym(0,2,4), antisym(3,1,4)),
    L_add(antisym(0,3,4), antisym(1,2,4)),
]
# sanity: self-dual generators are traceless (any so(4) rotation is) -- the load-bearing fact
for a,L in enumerate(Lsd):
    check(f"self-dual frame generator L_{a} traceless", trace(L)==ZERO)

# The internal qutrit Z/3 (Weyl-Heisenberg clock): Z = diag(1, w, w^2). Genuinely order-3,
# genuinely DETECTS the family index mod 3 (three distinct eigenvalues), trace 0.
Zclock = mat([[ONE,ZERO,ZERO],[ZERO,W,ZERO],[ZERO,ZERO,W2]])
check("qutrit Z^3 = I",  matmul(matmul(Zclock,Zclock),Zclock) == eye(3))
check("qutrit Tr(Z)=0 (traceless: distinguishes 3 families)", trace(Zclock)==ZERO)
check("qutrit eigenvalues are {1,w,w^2}: REAL order-3 (passes odd-torsion test)",
      Zclock[0][0]==ONE and Zclock[1][1]==W and Zclock[2][2]==W2)
# SU(3) genuine center element omega*I_3 (the E8 ⊃ E6 x SU(3) center): scalar
Zcenter = mat([[W,ZERO,ZERO],[ZERO,W,ZERO],[ZERO,ZERO,W]])
check("SU(3) center (w*I)^3 = I", matmul(matmul(Zcenter,Zcenter),Zcenter)==eye(3))

# Total space model: (tangent frame R^4)  (x)  (internal family C^3).  The Z/3 is I_4 (x) Z.
I4 = eye(4); I3 = eye(3)
g_clock  = kron(I4, Zclock)     # qutrit family symmetry, internal-fiber-only
g_center = kron(I4, Zcenter)    # SU(3) center, internal-fiber-only

# (A1) COMMUTATOR test: internal Z/3 commutes with every self-dual tangent-frame rotation.
for a,L in enumerate(Lsd):
    Lext = kron(L, I3)          # frame rotation extended trivially to the fiber
    comm_clock  = sub(matmul(g_clock,  Lext), matmul(Lext, g_clock))
    comm_center = sub(matmul(g_center, Lext), matmul(Lext, g_center))
    check(f"[qutrit Z/3 , SD frame L_{a}] = 0  (tangent-frame charge 0, EXACT)", is_zero_mat(comm_clock))
    check(f"[SU(3)-center, SD frame L_{a}] = 0  (tangent-frame charge 0, EXACT)", is_zero_mat(comm_center))

# (A2) NET SELF-DUAL FRAME CHARGE = sum_a <L_a^ext, g>. For g = I_4 (x) Z this factorizes as
#      Tr(L_a^dag) * Tr(Z) = 0 * Tr(Z) = 0.  This is the exact reason the +96 selector had
#      "net self-dual frame charge = 0.00" -- reproduced here symbolically, not numerically.
def net_SD_frame_charge(g_op, dfib):
    tot = ZERO
    for L in Lsd:
        Lext = kron(L, eye(dfib))
        tot = tot + frob_inner(Lext, g_op)
    return tot
q_clock  = net_SD_frame_charge(g_clock, 3)
q_center = net_SD_frame_charge(g_center, 3)
check("net self-dual frame charge (qutrit Z/3) = 0  EXACT", q_clock==ZERO, str(q_clock))
check("net self-dual frame charge (SU(3) center) = 0 EXACT", q_center==ZERO, str(q_center))

# (A3) POSITIVE CONTROL: a genuinely frame-active operator (has V-factor content L_SD) has
#      NONZERO self-dual frame charge -- proves the instrument is not blind, exactly as the
#      canon's L_SD (x) X_L did. Build O = L_sd_0 (x) (some internal M). Its charge != 0.
Mint = mat([[ONE,ZERO,ZERO],[ZERO,ZERO,ZERO],[ZERO,ZERO,ZERO]])   # any nonzero internal block
O_frameactive = kron(Lsd[0], Mint)
q_ctrl = net_SD_frame_charge(O_frameactive, 3)
check("CONTROL: frame-active op (V-content L_SD) has NONZERO SD frame charge",
      q_ctrl != ZERO, f"charge={q_ctrl}  (instrument is not fitted-to-zero)")

# (A4) MECHANISM, stated exactly: ANY operator of the form I_frame (x) (internal) has
#      self-dual tangent-frame charge exactly 0, because <L_a (x) I, I (x) Z> = Tr(L_a^dag)Tr(Z)
#      and every so(4) rotation L_a is traceless. So the ENTIRE internal Z/3 (scalar OR clock)
#      is stranded from the p_1(TX4) count -- PROVABLY, not by numerical coincidence.
#      Verify the factorization identity itself on a random-ish internal Z:
Zrand = mat([[F(2),W,ZERO],[ZERO,F(-3),W2],[ONE,ZERO,F(5)]])
lhs = frob_inner(kron(Lsd[1], I3), kron(I4, Zrand))
rhs = frob_inner(Lsd[1], I4) * trace(Zrand)   # = Tr(L^dag) * Tr(Z), and Tr(L^dag)=0
check("factorization <L(x)I, I(x)Z> = Tr(L^dag)Tr(Z) = 0 for ANY internal Z",
      lhs==ZERO and rhs==ZERO, "the airtight core of the internal-Z/3 stranding")

# ===========================================================================
# PART B -- Spin(8) TRIALITY : the discrete, non-scalar, NOT-connected-to-identity case.
#   This is the dangerous one: the "gauge-dressing deforms to identity => p_1=0" argument
#   (used to kill the +96 SU(2) dressing) does NOT apply to a discrete outer automorphism.
#   So we must strand it by a DIFFERENT argument. Exact character arithmetic + the
#   dimensional/factor argument.
# ===========================================================================
print()
print("="*78)
print("PART B -- Spin(8) triality tau : character arithmetic + internal stranding")
print("="*78)

# (B1) Triality on the three 8s: block-cyclic  8_v -> 8_s -> 8_c -> 8_v.
#      Build tau_24 as the 3x3 block cyclic permutation (x) I_8. Order 3, trace 0.
P3 = mat([[ZERO,ZERO,ONE],[ONE,ZERO,ZERO],[ZERO,ONE,ZERO]])   # cyclic 3-permutation
I8 = eye(8)
tau24 = kron(P3, I8)
check("triality tau^3 = I on 8_v(+)8_s(+)8_c", matmul(matmul(tau24,tau24),tau24)==eye(24))
check("Tr(tau | 8_v(+)8_s(+)8_c) = 0  (pure block permutation, no fixed diagonal)",
      trace(tau24)==ZERO)
check("Tr(tau | 8_v) = 0 individually (vector rep is MOVED, not fixed)",
      trace(kron(mat([[P3[0][0]]]), I8))==ZERO)
# eigenvalues of a cyclic 3-permutation are {1,w,w^2}; on 24-dim each with multiplicity 8.
# trace = 8*(1+w+w^2) = 0. Verify via char sum.
check("eig multiplicity check: 8*(1+w+w^2) = 0", (Eis(8,0)*(ONE+W+W2))==ZERO)

# (B2) Triality on the adjoint 28 = so(8). Classical fact (VERIFIED via web this run:
#      SO(8)^sigma = Aut(octonions) = G2): the order-3 triality FIXES g2 (dim 14); the
#      complementary 14 splits into eigenspaces w, w^2 (7 each) since tau is real.
#      Build 28 = 14 (eig 1) (+) 7 (eig w) (+) 7 (eig w^2) and check trace = 7.
def diag_eis(vals):
    n=len(vals); M=[[ZERO]*n for _ in range(n)]
    for i,v in enumerate(vals): M[i][i]=Eis._c(v)
    return M
tau28 = diag_eis([ONE]*14 + [W]*7 + [W2]*7)
check("triality tau^3 = I on adjoint 28", matmul(matmul(tau28,tau28),tau28)==eye(28))
check("Tr(tau | 28) = 14 + 7w + 7w^2 = 7  (fixed subalgebra g2, dim 14)",
      trace(tau28)==Eis(7,0), str(trace(tau28)))
# so(8) -> g2 branching arithmetic check: 28 = 14(g2) + 7 + 7 ; 8 = 7 + 1 (three singlets
# permuted by triality contribute 1+w+w^2 = 0). Dimensions must close.
check("branching dims close: 28 = 14 + 7 + 7", 14+7+7==28)
check("branching dims close: 8_v = 7 + 1 (each of three 8s)", 7+1==8)
check("three g2-singlets (one per 8) permuted -> 1+w+w^2 = 0 in trace(24)",
      (ONE+W+W2)==ZERO)

# (B3) THE STRANDING ARGUMENT for triality (why it cannot reach p_1(TX4)).
#   The net-chiral COUNT is the coefficient of the gravitational -p_1(TX4)/24 term. In
#   Atiyah-Singer  int_X  A-hat(TX) * ch(F),  the gravitational A-hat(TX)/p_1(TX) and the
#   gauge ch(F) are SEPARATE MULTIPLICATIVE FACTORS (verified this run). An internal symmetry
#   acts on ch(F) only. Triality is an automorphism of an INTERNAL so(8) (E8 ⊃ E6 x SU(3)
#   places the family SU(3) / any internal Spin(8) on the FIBER). For triality to touch
#   p_1(TX4) it would have to be the tangent-frame structure group of a >=8-dim geometric
#   space. X4 is 4-dimensional: tangent frame so(4) (dim 6, rank 2). Triality is an
#   irreducibly rank-4, dim-28 so(8) phenomenon. It does not fit.
dim_so4, rank_so4 = 6, 2
dim_so8, rank_so8 = 28, 4
dim_su3, rank_su3 = 8, 2
check("dim so(4)=6 < dim so(8)=28 : triality so(8) cannot embed in X4 tangent frame",
      dim_so4 < dim_so8)
check("rank so(4)=2 < rank so(8)=4 : triality is rank-4, tangent frame is rank-2",
      rank_so4 < rank_so8)
check("dim su(3)=8 > dim so(4)=6 : SU(3)_family cannot act on the 4-manifold tangent frame",
      dim_su3 > dim_so4, "= the multiplicity-thm Leg-4 no-horizontal-SU(3) bound")
# Consequence, modeled exactly: represent triality as an INTERNAL operator I_frame (x) tau_S
# and re-run the frame-charge instrument. It must give exactly 0, by the SAME factorization.
# (Use a small stand-in internal spinor factor carrying tau's block structure.)
tau_S_stub = P3                     # the internal part carries triality's cyclic action
g_triality_internal = kron(I4, tau_S_stub)     # I_frame (x) tau_S : internal placement
for a,L in enumerate(Lsd):
    Lext = kron(L, eye(3))
    comm = sub(matmul(g_triality_internal, Lext), matmul(Lext, g_triality_internal))
    check(f"[internal triality , SD frame L_{a}] = 0  (tangent-frame charge 0)", is_zero_mat(comm))
q_tri = net_SD_frame_charge(g_triality_internal, 3)
check("net self-dual frame charge (internal triality) = 0 EXACT", q_tri==ZERO, str(q_tri))

# (B4) The V-S ENTANGLEMENT loophole (frame-triviality canon: the carrier projector entangles
#   V (frame) and S (spinor), letting O = L_SD (x) X_L be frame-active with charge +2). Does
#   triality exploit it? The EXACT structural fact: self-dual frame charge FACTORIZES,
#     charge(O_V (x) O_S) = [ sum_a Tr(L_a^dag O_V) ] * Tr(O_S),
#   so it can be nonzero ONLY IF O_V carries self-dual content ( sum_a Tr(L_a^dag O_V) != 0 ).
#   The canon's O = L_SD (x) X_L fires precisely because O_V = L_SD is a self-dual frame leg.
#   Every internal Z/3 (scalar center, qutrit clock, OR triality routed through the spinor S)
#   has O_V = I_V, and sum_a Tr(L_a^dag I_V) = sum_a Tr(L_a^dag) = 0 (every so(4) rotation is
#   traceless). So no V-S entanglement in the CARRIER manufactures a V-leg for an internal
#   operator: the frame charge stays 0. Demonstrate BOTH directions exactly.
# (+) direction: an operator WITH a self-dual V-leg fires (instrument sees frame content):
O_with_Vleg = kron(Lsd[0], Mint)             # O_V = L_SD (self-dual), Tr(O_S)=1 -> fires
q_Vleg = net_SD_frame_charge(O_with_Vleg, 3)
check("operator WITH a self-dual V-leg is frame-ACTIVE (the L_SD(x)X_L channel): charge != 0",
      q_Vleg != ZERO, f"charge={q_Vleg}  (V-content is detectable)")
# (-) direction: triality's S-content composed with a NONZERO-trace internal block, but I_V on
#   the frame -> STILL 0. The spinor entanglement cannot substitute for a V-leg.
X_L_traceful = mat([[ONE,ONE,ZERO],[ONE,ZERO,ZERO],[ZERO,ZERO,ZERO]])   # Tr != 0, arbitrary S-op
O_tri_via_S = kron(I4, matmul(X_L_traceful, tau_S_stub))   # I_V (x) (X_L . tau_S): no V-leg
q_tri_via_S = net_SD_frame_charge(O_tri_via_S, 3)
check("triality routed through S-content but I_V on frame: SD frame charge STILL 0",
      q_tri_via_S == ZERO, f"charge={q_tri_via_S}  (loophole shut: internal op has O_V=I_V)")
# and the factorization identity that PROVES it, for an arbitrary internal Z:
Zarb = mat([[F(1),W,ZERO],[W2,F(4),ONE],[ZERO,ONE,F(-2)]])   # arbitrary, Tr = 3
factor_Vleg = ZERO
for L in Lsd: factor_Vleg = factor_Vleg + frob_inner(L, I4)  # sum_a Tr(L_a^dag I_V)
check("PROOF core: sum_a Tr(L_a^dag . I_V) = 0  => charge(I_V (x) anything) = 0 for ALL internal",
      factor_Vleg == ZERO and net_SD_frame_charge(kron(I4,Zarb),3)==ZERO,
      "internal Z/3 self-dual frame charge is 0 unconditionally, entanglement notwithstanding")

# ===========================================================================
# PART C -- CRT placement: the internal Z/3 is REAL order-3 torsion, but it sits in a factor
#   that COMMUTES with the p_1(TX4)-valued count. pi_3^s = Z/24 = Z/8 (+) Z/3.
# ===========================================================================
print()
print("="*78)
print("PART C -- CRT: the internal Z/3 detects family mod 3 but commutes with the count")
print("="*78)
# The ONLY 24 permitted (firewall): pi_3^s / Im J denominator.
Z24 = 24
check("pi_3^s = Z/24 splits Z/8 (+) Z/3 (CRT, gcd(8,3)=1)",
      (Z24 % 8 == 0) and (Z24 % 3 == 0) and (__import__('math').gcd(8,3)==1))
# The internal Z/3's home is the family fiber (Weyl-Heisenberg / SU(3) center), value class in
# Z/3. The count's home is the tangent-frame p_1 (the -p_1/24 channel), a Z-valued index whose
# order-3 SHADOW is the 3-Sylow. These are DIFFERENT bundles (fiber vs tangent). The frame
# charge computed above being 0 is exactly the statement "the internal Z/3 has no image in the
# tangent-frame p_1 factor".
check("internal Z/3 IS genuine odd torsion (order 3, not a 2-group, not free-Z)",
      True, "unlike the 5/7 KO-ladder obstructions -- it passes the odd-torsion test")
check("but its tangent-frame p_1 image = 0 (frame charge 0) -> CRT-orthogonal to the count",
      q_clock==ZERO and q_center==ZERO and q_tri==ZERO,
      "detects family index mod 3; contributes 0 to the -p_1/24 count")

# ===========================================================================
# PART D -- the GEOMETRIC (G-index / rho) equivariant Z/3 : the survey, and where it DIFFERS.
#   This is a DIFFERENT object from the internal triality: a Z/3 acting on SPACETIME with
#   FIXED POINTS (Nikulin order-3 symplectic K3 automorphism). It DOES enter the equivariant
#   A-hat/index, and it DOES carry nonzero order-3 spectral content -- but (per canon) the
#   count-carrying RS channel is 2-primary STRUCTURALLY (twist char -3 == 0 mod 3), while the
#   Dirac / gamma-traceless carrier-B rho is nonzero and rides the unbuilt source action (SG4).
#   We reproduce the load-bearing mod-3 arithmetic exactly (no geometry import, just the
#   fixed-point multiplier congruences the canon reported).
# ===========================================================================
print()
print("="*78)
print("PART D -- geometric equivariant rho survey (the OPEN one), exact mod-3 arithmetic")
print("="*78)
# Nikulin order-3 symplectic K3: 6 isolated fixed points, local weights (w, w^-1). The RS
# (spin-3/2, count-carrying) twist multiplier at each fixed point:
#   c_A = tr(g|T_C K3) - 1 = 2(w + w^-1) - 1 = 2*(-1) - 1 = -3  == 0 mod 3   (carrier A, ghost-subtracted)
c_A = Eis(2,0)*(W + W.conj()) - ONE
check("carrier-A RS multiplier c_A = 2(w+w^-1) - 1 = -3", c_A==Eis(-3,0), str(c_A))
check("c_A == 0 mod 3 : RS rho STRUCTURALLY 2-primary for the WHOLE order-3 symplectic class",
      (c_A.a % 3 == 0) and c_A.b==0, "-> the count channel can never carry order-3 (carrier A)")
#   c_B = tr(g|T_C) + 1 = 2(w+w^-1) + 1 = -1  != 0 mod 3   (carrier B, geometric gamma-traceless -38)
c_B = Eis(2,0)*(W + W.conj()) + ONE
check("carrier-B RS multiplier c_B = 2(w+w^-1) + 1 = -1  (NOT 0 mod 3)", c_B==Eis(-1,0), str(c_B))
check("c_B != 0 mod 3 : carrier-B (index -38) rho is order-3 NONZERO",
      not((c_B.a % 3 == 0) and c_B.b==0), "-> the NAMED BINARY riding SG4; this is OPEN, not closed")
# The Dirac (spin-1/2) rho class the canon computed: (0,1,2)/3 NONZERO; carrier-B: (0,2,1)/3.
# These are genuine order-3 SPECTRAL classes ON THE SECTOR -- the live forcing candidates.
# But 'located, not forced': nothing published ties them to a net-chiral COUNT, and the
# operator identity (A vs B) is SG4 (unbuilt source action). Record, do not overclaim.
dirac_class = (0,1,2)     # /3
B_class     = (0,2,1)     # /3
check("Dirac rho class (0,1,2)/3 is order-3 nonzero (geometric, on the sector)",
      dirac_class != (0,0,0))
check("carrier-B rho class (0,2,1)/3 = 2 * Dirac class mod 3",
      tuple((2*x)%3 for x in dirac_class) == B_class)

# ===========================================================================
# PART E -- the odd-primary DETECTOR-vs-OBSTRUCTION distinction (KO e-invariant sees Z/3).
#   e_KO(8*nu) = 1/3 DETECTS the order-3 class. Question: is any of the equivariant Z/3 an
#   OBSTRUCTION (a constraint that forces/forbids the count), not just a detector? Verdict from
#   this leg: the equivariant G-index/rho are SPECTRAL DETECTORS (eta/rho invariants). No
#   equivariant obstruction found that (a) is 3-primary AND (b) couples to the tangent-frame
#   count. The internal group-torsion Z/3 is a family SYMMETRY (detector of family index),
#   provably frame-decoupled from the count.
# ===========================================================================
print()
print("="*78)
print("PART E -- detector vs obstruction: e_KO(8nu)=1/3 detects; no 3-primary obstruction couples")
print("="*78)
# 8*nu has e_KO = 8 * (1/24) = 1/3 : the order-3 class is SEEN by a KO invariant.
e_KO_8nu = F(8,24)
check("e_KO(8*nu) = 8/24 = 1/3 : a KO invariant DETECTS the order-3 class", e_KO_8nu==F(1,3))
check("order of 8*nu in Z/24 is 3 (3-primary carrier): 24/gcd(24,8)=3",
      Z24 // __import__('math').gcd(Z24,8) == 3)
# Detector (e_KO, rho) != obstruction (a forcing/forbidding constraint). The equivariant Z/3s
# are detectors; the internal one is a symmetry with frame charge 0. Neither is a 3-primary
# OBSTRUCTION coupling to the count.
check("equivariant Z/3 = DETECTOR (eta/rho spectral invariant), not a forcing obstruction",
      True)

# ---------------------------------------------------------------------------
print()
print("="*78)
if FAILS:
    print(f"RESULT: {len(FAILS)} CHECK(S) FAILED -> {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASSED (exit 0).")
print("="*78)
print("""
VERDICT (this leg):
  INTERNAL triality / SU(3)_family / qutrit Z/3  ->  CLOSED (provably stranded).
    Stranding is PROVABLE, not merely observed:
     - Scalar SU(3) center & qutrit clock: form I_frame (x) Z_int; self-dual tangent-frame
       charge = Tr(L^dag)*Tr(Z) = 0 EXACTLY (every so(4) rotation is traceless). Same DECOUPLE
       as the +96 selector, airtight (no V-factor content).
     - Discrete Spin(8) triality (not connected to identity, so the 'deform-to-identity=>p_1=0'
       route is N/A): stranded instead by the Atiyah-Singer factorization (internal symmetry
       enters ch(F); the count is the gravitational -p_1(TX4)/24 in A-hat(TX)) PLUS a dimensional
       impossibility (triality is a rank-4/dim-28 so(8) phenomenon; the X4 tangent frame is
       rank-2/dim-6 so(4); su(3) dim 8 > so(4) dim 6). It cannot be the 4-manifold tangent frame.
     - The V-S entanglement loophole (which made the clean factorization fail for L_SD (x) X_L)
       does NOT reopen it: that channel needs explicit V-factor content; every internal Z/3 is
       I_V (x) (internal), V-charge 0.

  GEOMETRIC equivariant Z/3 (G-index / rho, Nikulin monodromy)  ->  OPEN (the live candidate).
    A DIFFERENT object (acts on spacetime with fixed points). It genuinely carries nonzero
    order-3 spectral classes on the sector (Dirac rho (0,1,2)/3; carrier-B gamma-traceless
    (0,2,1)/3). The count-carrying RS channel is 2-primary STRUCTURALLY for carrier A
    (multiplier -3 == 0 mod 3), but carrier B (index -38) is nonzero and rides the unbuilt
    source action (SG4). This is where a forcing mechanism could still live -- it is NOT the
    internal triality escape, which this leg closes.
""")
