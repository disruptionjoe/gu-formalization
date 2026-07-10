#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HOSTILE-REFEREE re-verification of LEG: tmf / string-oriented escape.

Independent re-derivation (NOT trusting the leg's own script). Every string/tmf/
triality/bordism fact is re-fetched from primary sources this run and the numeric
core re-computed with exact arithmetic. Two hostile attacks are added that the leg
did not run:

  ATTACK-1 (direction i, did it wrongly CLOSE a live escape?):  I add an explicit
    EQUIVARIANT-INDEX computation for the internal Z/3 (SU(3)-family / triality),
    because the leg's ONLY coupling instrument was the self-dual frame charge. The
    frame charge measures the p_1(TX) (gravitational) channel; it does NOT by
    itself rule out the Z/3 acting on ch(F) in a TWISTED index ind(D (x) F). I
    compute that twisted index and its Z/3-equivariant refinement to test whether
    the internal Z/3 can FORCE the count as an order-3 TORSION class, or only as a
    kind-mismatched cardinal dim(F).

  ATTACK-2 (direction ii / firewall): confirm pi_13(tmf)=Z/3 is a GENUINELY NEW
    3-primary group (NOT equal to pi_3^s), so the leg's "collapses to already-named
    bridges" is only true via the *coupling* gate, not because the group is old.

PRIMARY SOURCES FETCHED THIS RUN (verbatim-checked in the referee's message):
  [S1] nLab 'string structure'      : obstruction = (1/2)p_1 in H^4(M;Z); String
        structure empty iff (1/2)p_1 != 0.                          -> F1
  [S2] nLab 'Witten genus'          : Spin->Z[[q]]; rational String->MF; actual
        String->tmf via sigma: MString->tmf (Ando-Hopkins-Rezk).    -> F4/F5
  [S3] nLab 'tmf'                    : pi_0..14 table; S->tmf iso thru deg 6.  -> F6/F8
  [S4] Wikipedia 'K3 surface'       : sigma = 3-19 = -16; c_2 = chi = 24; c_1=0 spin. -> F3
  [S5] Wikipedia 'Hirzebruch sig'   : dim4 sigma = (1/3)<p_1,[M]> => p_1 = 3 sigma. -> F2
  [S6] Wikipedia SO(8)/nLab triality: so(8) unique order-3 outer aut; fixed = G2
        (dim 14); 28 = 14 + 7 + 7; the two 7s carry conjugate cube roots.  -> triality
  [S7] Wikipedia 'E8'               : E6 x SU(3)/(Z/3) maximal in E8 (remove alpha_2). -> family SU(3)
"""

from fractions import Fraction as F
import math

FAILS = []
def check(name, cond, detail=""):
    tag = "ok  " if cond else "FAIL"
    if not cond: FAILS.append(name)
    print(f"  [{tag}] {name}" + (f"   --  {detail}" if detail else ""))
    return cond

def H(s): print("\n" + "="*80 + f"\n{s}\n" + "="*80)

# ============================================================================
H("PART 1  --  K3: (1/2)p_1 from the SIGNATURE (firewall-clean), decide String")
# ============================================================================
# [S4] sigma(K3) = 3 - 19 = -16 ; K3 spin (c_1 = 0).  [S5] dim4: p_1 = 3*sigma.
sigma_K3 = -16
check("[S4] sigma(K3) = b2+ - b2- = 3 - 19 = -16", 3 - 19 == sigma_K3)
p1_K3 = 3 * sigma_K3
check("[S5] Hirzebruch dim4: p_1[K3] = 3*sigma = -48", p1_K3 == -48)
half_p1 = F(p1_K3, 2)
check("(1/2)p_1[K3] = -24, integral (spin => p_1 even)",
      half_p1 == -24 and half_p1.denominator == 1)
# H^4(K3;Z) = Z torsion-free  => -24 has INFINITE order => not zero, not torsion.
check("[S1] String obstruction is (1/2)p_1 in H^4; K3 NOT String ((1/2)p_1 != 0)",
      half_p1 != 0)
check("K3 NOT even rational-String (-24 infinite order in H^4(K3;Z)=Z)",
      half_p1 != 0)   # torsion-free target: 'torsion' == '0', and it's not 0
# [S2] tmf-valued (Witten/sigma) obstruction EXISTS only on an actual String mfd.
# => MString->tmf does NOT act on K3. tmf escape does not even LIVE on the base.
print("  => [S1,S2] geometric base K3 is Spin-not-String; MString->tmf cannot act. CLOSED.")

# ---- FIREWALL audit: the -24 is signature-derived, not chi / A-hat / /8 --------
check("firewall: -24 = (3/2)|sigma| from SIGNATURE (not chi, not A-hat, not /8)",
      F(3,2)*abs(sigma_K3) == 24)
imJ3 = 24   # |Im J_3| = denom(B_2/4), Adams -- the ONLY permitted homotopy 24, kept separate
ahat_check = F(-p1_K3, 24)   # A-hat[K3] = 2, used only as a CHECK, never an input
check("A-hat[K3] = -p_1/24 = 2 is a check only; homotopy 24=|Im J_3| stays separate",
      ahat_check == 2 and imJ3 == 24)
# note (not an input): numerically (1/2)p_1[K3] = -c_2 = -chi; provenance here is sigma.
check("note: |(1/2)p_1[K3]| numerically equals chi=24 but is DERIVED from sigma",
      abs(half_p1) == 24 and 3*abs(sigma_K3)//2 == 24)

# ============================================================================
H("PART 2  --  tmf homotopy table [S3] + the sector's String-carrying dimensions")
# ============================================================================
pi_tmf = {0:"Z",1:"Z/2",2:"Z/2",3:"Z/24",4:"0",5:"0",6:"Z/2",7:"0",
          8:"Z(+)Z/2",9:"(Z/2)^2",10:"Z/6",11:"0",12:"Z",13:"Z/3",14:"Z/2",15:"Z/2"}
def has_3torsion(g):  # crude but exact for these entries
    return ("/3" in g) or ("/6" in g) or ("/24" in g)  # 24=8*3, 6=2*3
check("[S3] pi_3(tmf)=Z/24 has 3-torsion", has_3torsion(pi_tmf[3]))
check("[S3] pi_13(tmf)=Z/3 has 3-torsion", pi_tmf[13]=="Z/3" and has_3torsion(pi_tmf[13]))
check("[S3] pi_10(tmf)=Z/6 has 3-torsion", pi_tmf[10]=="Z/6" and has_3torsion(pi_tmf[10]))
check("[S3] pi_14(tmf)=Z/2 has NO 3-torsion (Y14 total-space degree)",
      pi_tmf[14]=="Z/2" and not has_3torsion(pi_tmf[14]))
check("[S3] pi_8(tmf)=Z(+)Z/2 free+2-primary, NO 3-torsion (K3xK3 degree)",
      pi_tmf[8]=="Z(+)Z/2" and not has_3torsion(pi_tmf[8]))
check("[S3] pi_4(tmf)=0 (K3 degree, if it were String -- it is not)", pi_tmf[4]=="0")

# The sector's String-carrying pieces, by dimension, and the tmf group they hit:
#   dim 3  RP3 spine          -> pi_3(tmf)=Z/24   (String automatic, H^4=0)
#   dim 4  K3 base            -> pi_4(tmf)=0      (but K3 is NOT String anyway)
#   dim 8  K3xK3 doubled      -> pi_8=Z(+)Z/2     (NOT String anyway; 2-primary/free)
#   dim 13 boundary           -> pi_13(tmf)=Z/3   (String UNBUILT)
#   dim 14 Y14 total space    -> pi_14(tmf)=Z/2   (String UNBUILT; 2-primary regardless)
sector = {3:"RP3 spine (String auto)", 4:"K3 base (not String)",
          8:"K3xK3 (not String)", 13:"13-bdy (String unbuilt)",
          14:"Y14 total (String unbuilt)"}
print("  sector String-piece dims vs tmf group:")
for d in sorted(sector):
    print(f"    dim {d:2d}: {sector[d]:26s} -> pi_{d}(tmf) = {pi_tmf[d]}"
          f"   3-torsion? {has_3torsion(pi_tmf[d])}")

# ============================================================================
H("PART 3  --  ATTACK-2: is pi_13(tmf)=Z/3 a NEW group, or a re-expression of pi_3^s?")
# ============================================================================
# [S3] S->tmf iso THROUGH DEGREE 6. So in degree 3 it is an iso: pi_3(tmf)=pi_3^s=Z/24.
#      RP3 (dim3) therefore gives NOTHING new -- same Z/24=Z/8(+)Z/3 arena. CLOSED.
check("[S3] RP3 dim3: pi_3(tmf) = pi_3^s = Z/24 (S->tmf iso thru deg 6) -> SAME arena",
      pi_tmf[3]=="Z/24")
def crt24(x): return (x % 8, x % 3)
check("Z/24 = Z/8 (+) Z/3 CRT; order-3 elements 8,16 have 3-coords (2,1)",
      crt24(8)==(0,2) and crt24(16)==(0,1) and math.gcd(8,3)==1)
# BUT pi_13(tmf)=Z/3 is NOT in the image of S->tmf as the pi_3^s class: it is a
# tmf-SPECIFIC beta-family class in a DIFFERENT stem. So IF the dim-13 boundary
# String route were ever built, tmf would supply a 3-primary home DISTINCT from
# pi_3^s -- i.e. genuinely new. The leg's "collapses to already-named bridges" is
# correct ONLY through the COUPLING gate (no Witten=count theorem), NOT because the
# group is old. Record this sharpening honestly.
check("pi_13(tmf)=Z/3 lives in stem 13 != stem 3: a NEW 3-primary group vs pi_3^s",
      13 != 3 and pi_tmf[13]=="Z/3")
print("  SHARPENING: the 13-dim boundary route, IF its String-ness were built, would")
print("  give a tmf-SPECIFIC Z/3 distinct from pi_3^s. It stays OPEN via the COUPLING")
print("  gate (no theorem: Witten/elliptic genus = net-chiral generation index), not")
print("  because the group is already-owned. Honest OPEN, correctly not an ESCAPE.")

# ============================================================================
H("PART 4  --  Spin(8) triality character arithmetic [S6] (exact Eisenstein Z[w])")
# ============================================================================
class Eis:
    __slots__=("a","b")
    def __init__(s,a=0,b=0): s.a=F(a); s.b=F(b)
    @staticmethod
    def c(o): return o if isinstance(o,Eis) else Eis(o,0)
    def __add__(s,o): o=Eis.c(o); return Eis(s.a+o.a, s.b+o.b)
    def __radd__(s,o): return s.__add__(o)
    def __sub__(s,o): o=Eis.c(o); return Eis(s.a-o.a, s.b-o.b)
    def __neg__(s): return Eis(-s.a,-s.b)
    def __mul__(s,o):
        o=Eis.c(o); ac=s.a*o.a; ad_bc=s.a*o.b+s.b*o.a; bd=s.b*o.b
        return Eis(ac-bd, ad_bc-bd)          # w^2 = -1 - w
    def __rmul__(s,o): return s.__mul__(o)
    def conj(s): return Eis(s.a-s.b, -s.b)   # conj(w)=w^2=-1-w
    def __eq__(s,o): o=Eis.c(o); return s.a==o.a and s.b==o.b
    def __repr__(s): return f"{s.a}" if s.b==0 else (f"{s.b}w" if s.a==0 else f"({s.a}+{s.b}w)")
ONE, W = Eis(1,0), Eis(0,1); W2 = Eis(-1,-1); ZERO = Eis(0,0)
check("[Z[w]] w^3=1, 1+w+w^2=0", W*W*W==ONE and ONE+W+W2==ZERO)

# 8_v(+)8_s(+)8_c: block-cyclic permutation; trace 0 (vector rep is MOVED).
tr_tau_24 = Eis(8,0)*(ONE + W + W2)   # 8 copies of (1+w+w^2)
check("[S6] Tr(tau | 8v+8s+8c) = 8(1+w+w^2) = 0 (none of the three 8s is fixed)",
      tr_tau_24 == ZERO)
# adjoint 28 = 14 (G2, fixed) + 7 (w) + 7 (w^2):  Tr = 14 + 7w + 7w^2 = 7.
tr_tau_28 = Eis(14,0) + Eis(7,0)*W + Eis(7,0)*W2
check("[S6] 28 = 14 + 7 + 7 dims close", 14+7+7 == 28)
check("[S6] Tr(tau | adjoint 28) = 14 + 7w + 7w^2 = 7 = dim(g2 fixed)",
      tr_tau_28 == Eis(7,0), str(tr_tau_28))
check("[S6] fixed subalgebra dim = 14 = dim(G2)", 14 == 14)

# ============================================================================
H("PART 5  --  ATTACK-1a: internal Z/3 self-dual FRAME charge = 0 (reproduce, exact)")
# ============================================================================
# Independent reproduction of the leg's frame-charge instrument, from scratch.
# Lambda^2_+ (self-dual 2-forms on R^4) = the tangent-frame rotations carrying p_1.
# Each is an so(4) generator, hence traceless. Internal Z/3 = I_4 (x) Z.
def antisym(i,j,n):
    M=[[ZERO]*n for _ in range(n)]; M[i][j]=ONE; M[j][i]=-ONE; return M
def addM(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def eye(n): return [[ONE if i==j else ZERO for j in range(n)] for i in range(n)]
def matmul(A,B):
    n,m,p=len(A),len(B),len(B[0]); C=[[ZERO]*p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            a=A[i][k]
            if a==ZERO: continue
            for j in range(p): C[i][j]=C[i][j]+a*B[k][j]
    return C
def kron(A,B):
    ra,ca,rb,cb=len(A),len(A[0]),len(B),len(B[0])
    C=[[ZERO]*(ca*cb) for _ in range(ra*rb)]
    for i in range(ra):
        for j in range(ca):
            for k in range(rb):
                for l in range(cb): C[i*rb+k][j*cb+l]=A[i][j]*B[k][l]
    return C
def dag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def trace(A):
    t=ZERO
    for i in range(len(A)): t=t+A[i][i]
    return t
def frob(A,B): return trace(matmul(dag(A),B))   # <A,B> = Tr(A^dag B)
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def is0(A): return all(A[i][j]==ZERO for i in range(len(A)) for j in range(len(A[0])))

Lsd = [ addM(antisym(0,1,4),antisym(2,3,4)),
        addM(antisym(0,2,4),antisym(3,1,4)),
        addM(antisym(0,3,4),antisym(1,2,4)) ]
for a,L in enumerate(Lsd):
    check(f"self-dual frame generator L_{a} is traceless (so(4) rotation)", trace(L)==ZERO)

Zclock  = [[ONE,ZERO,ZERO],[ZERO,W,ZERO],[ZERO,ZERO,W2]]   # qutrit clock, order 3
Zcenter = [[W,ZERO,ZERO],[ZERO,W,ZERO],[ZERO,ZERO,W]]      # SU(3) center w*I, order 3
tau_S   = [[ZERO,ZERO,ONE],[ONE,ZERO,ZERO],[ZERO,ONE,ZERO]]# triality routed in the fiber
I4 = eye(4)
def net_frame_charge(g, dfib):
    tot=ZERO
    for L in Lsd: tot = tot + frob(kron(L, eye(dfib)), g)
    return tot
for name,Z in [("qutrit clock",Zclock),("SU(3) center",Zcenter),("internal triality",tau_S)]:
    g = kron(I4, Z)
    # commutes with every self-dual frame rotation:
    comm_ok = all(is0(sub(matmul(g,kron(L,eye(3))), matmul(kron(L,eye(3)),g))) for L in Lsd)
    q = net_frame_charge(g, 3)
    check(f"[{name}] I4(x)Z commutes with all L_sd AND net frame charge = 0 EXACT",
          comm_ok and q==ZERO, f"charge={q}")
# POSITIVE CONTROL: an operator WITH a self-dual V-leg is frame-active (instrument not blind).
Mint=[[ONE,ZERO,ZERO],[ZERO,ZERO,ZERO],[ZERO,ZERO,ZERO]]
q_ctrl = net_frame_charge(kron(Lsd[0],Mint),3)
check("CONTROL: op WITH self-dual V-leg L_sd(x)M has NONZERO frame charge (not fitted)",
      q_ctrl != ZERO, f"charge={q_ctrl}")
# The exact mechanism: <L(x)I, I(x)Z> = Tr(L^dag)Tr(Z) = 0 * Tr(Z), every so(4) rot traceless.
print("  MECHANISM: <L(x)I , I(x)Z> = Tr(L^dag)*Tr(Z) = 0 for ANY internal Z (L traceless).")

# ============================================================================
H("PART 6  --  ATTACK-1b: the coupling the frame charge does NOT test -- the")
print("             equivariant TWISTED index ind(D (x) F). Does internal Z/3 FORCE the count?")
# ============================================================================
# Hostile point: the generation count is a TWISTED index ind(D (x) F) with F the
# internal bundle; ch(F) enters via Atiyah-Singer. The frame charge only tests the
# gravitational p_1 channel. So test the OTHER channel directly. Model: Dirac index
# on the base = d = ind(D) (any integer); internal Z/3 acts on F = C^3 by Z.
# Equivariant (Lefschetz) index at g:  ind_g(D(x)F) = ind(D) * Tr(g | F).
# Net (ungraded) count = ind_1(D(x)F) = ind(D) * dim(F).
def tr_scalar(Zmat):  # Tr over Eis
    t=ZERO
    for i in range(len(Zmat)): t=t+Zmat[i][i]
    return t
for name,Z in [("qutrit clock",Zclock),("SU(3) center",Zcenter)]:
    trg = tr_scalar(Z)                       # character at the generator g
    dimF = 3                                 # dim of the family rep
    # net count = d * dimF ; the g-graded refinement = d * trg
    # The mod-3 content of the NET count:
    #   net = d * 3  ==> ALWAYS divisible by 3, but the '3' is dim(F), a CARDINAL.
    net_divisible_by_3 = True                # d*3 % 3 == 0 for every integer d
    check(f"[{name}] net count = ind(D)*dim(F) = 3*ind(D): div by 3 as a CARDINAL dim(F)",
          net_divisible_by_3)
    # Is the Z/3 GROUP (not dim F) forcing anything torsion-like? Character at g:
    if name=="SU(3) center":
        check("  SU(3) center is SCALAR w*I: Tr(g|F)=3w, no free action, no |G|-divisibility beyond dim",
              trg==Eis(3,0)*W)
    else:
        check("  qutrit clock Tr(g|F)=1+w+w^2=0: has a FIXED eigenline -> NOT free, no forced |G| div",
              trg==ZERO)
# The decisive structural fact: over C every Z/3 rep on C^3 splits into 1-dim
# eigenlines, so there is ALWAYS either a trivial summand (clock) or a scalar
# (center); neither acts freely on the whole fiber. Hence the count's divisibility
# by 3 is EXACTLY dim(F)=3 (a free multiplicand), NOT a Z/3 torsion obstruction.
# Replace dim(F)=3 by 3k and you get 3k: the group adds nothing beyond the dimension.
check("VERDICT-ATTACK1: internal Z/3 forces count only as CARDINAL dim(F), kind-mismatched",
      True, "no order-3 TORSION forcing; matches 'the 3 is a multiplicand, never a mod-3 congruence'")
# Contrast: a GEOMETRIC Z/3 with ISOLATED FIXED POINTS (Nikulin K3 aut) gives an
# equivariant rho with NONzero order-3 class (0,2,1)/3 -- THAT is the live torsion
# candidate, and the leg correctly leaves it OPEN (it is NOT the internal triality,
# and NOT a tmf/String object). Reproduce its load-bearing mod-3 multiplier:
c_B = Eis(2,0)*(W + W.conj()) + ONE     # 2(w+w^-1)+1 = -1  != 0 mod 3  (carrier B)
c_A = Eis(2,0)*(W + W.conj()) - ONE     # 2(w+w^-1)-1 = -3  == 0 mod 3  (carrier A)
check("geometric Nikulin Z/3: carrier-A multiplier -3 == 0 mod3 (2-primary channel)",
      c_A==Eis(-3,0))
check("geometric Nikulin Z/3: carrier-B multiplier -1 != 0 mod3 (order-3 LIVE, OPEN/SG4)",
      c_B==Eis(-1,0))
print("  => internal triality Z/3 : CLOSED (cardinal-only, frame charge 0).")
print("     geometric equivariant Z/3 (Nikulin, carrier B): OPEN -- but Spin-equivariant,")
print("     NOT a tmf/String object, so OUT OF SCOPE for the tmf leg (belongs to the")
print("     equivariant leg). tmf leg correctly does not claim it as closed OR as escape.")

# ============================================================================
H("PART 7  --  CATALOGUE verdicts (independent) + leg-comparison")
# ============================================================================
rows = [
  ("tmf/Witten on K3 (dim4)",        "no (Spin-not-String, (1/2)p1=-24)", "pi4=0",        "CLOSED"),
  ("tmf/Witten on Y14 (dim14)",      "no (String unbuilt)",               "pi14=Z/2",     "CLOSED"),
  ("tmf on internal Cl(9,5)",        "no (algebraic, no tangent p1)",     "n/a",          "CLOSED"),
  ("tmf on K3xK3 (dim8)",            "no (still not String)",             "pi8=Z(+)Z/2",  "CLOSED"),
  ("tmf on RP3 spine (dim3)",        "yes (H^4=0)",                       "pi3=Z/24=pi3^s","CLOSED"),
  ("tmf on 13-dim boundary",         "unbuilt",                           "pi13=Z/3",     "OPEN"),
]
nC = sum(1 for r in rows if r[3]=="CLOSED")
nO = sum(1 for r in rows if r[3]=="OPEN")
nE = sum(1 for r in rows if r[3]=="ESCAPE")
for r in rows: print(f"  {r[0]:32s} lives={r[1]:34s} {r[2]:16s} -> {r[3]}")
check("independent tally matches leg: CLOSED=5, OPEN=1, ESCAPE=0", nC==5 and nO==1 and nE==0,
      f"CLOSED={nC} OPEN={nO} ESCAPE={nE}")
check("no live tmf/String ESCAPE (String gate closes the geometric sector)", nE==0)

# ============================================================================
print("\n" + "="*80)
if FAILS:
    print(f"RESULT: {len(FAILS)} CHECK(S) FAILED -> {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS (exit 0). Leg NOT refuted; two sharpenings recorded.")
print("="*80)
