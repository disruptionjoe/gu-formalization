"""
ROUTE S3 -- DOUBLE-DUTY: does the mirror-hiding source action select the count base?

THE DEEP QUESTION (the swing): are the COUNT (the twisted-Rarita-Schwinger base-topology
index) and the ALIGNMENT (the mirror-hiding condensate coupling tr(Q5 Phi^2), 2026-07-07
alignment swing) the SAME source-action object, or two INDEPENDENT external inputs?

If the mirror-hiding dynamics -- a native source action generating tr(Q5 Phi^2) with the
stabilizing sign -- ALSO forced a base topology carrying 3-torsion, then one built object
would do double duty (hide the mirrors AND supply the count), a route to PROMOTE the
order-3-class -> integer-3 conjecture. If instead the alignment coupling is base-agnostic, or
selects a 2-adic base, then count and alignment are two SEPARATE external inputs and the
count-import stays structural (KILL of the double-duty branch).

This script tests double-duty on the verified (9,5) carrier along four independent legs, each
exact machine-checked linear algebra or symbolic arithmetic:

  (S1) BASE-AGNOSTICISM of the alignment weight.  Q5 = e9..e13|_W (the internal spacelike
       5-volume, = -P_ghost = -K|_W by V8's identity) is the weight of the alignment coupling
       tr(Q5 Phi^2).  Its BASE tangent-frame charge is exactly zero:
         - [Q5, so(4)_base] = 0 over every base-frame generator (the twist / sigma / e_R live
           on the base X^4);
         - <Q5, Lambda^2_+> = 0 (zero overlap with the self-dual su(2)+ generators -- exactly
           the twist-generating direction that carries the order-3 e_R = 1/12 framing).
       CONTROL: Q5 is NOT vacuously trivial -- [Q5, internal boost] != 0.  Cross-check: the
       paper's chiralizer J_quat is frame-trivial too (Section 6 anchor reproduced), and on W
       Q5 = -P is the same Z2 as the ghost parity.  => the alignment coupling cannot see, hence
       cannot select, any base topology.

  (S2) 2-ADIC vs 3-TORSION content of the alignment SELECTOR.  Q5^2 = I (order 2); the
       selecting sign is flipped by chi-conjugation (chi Q5 chi = -Q5, A2/A3).  Since
       {P, chi} = 0 (P = -Q5), (P.chi)^2 = -I, so the multiplicative group <P, chi> contains -I
       and is a 2-GROUP of ORDER 8 (element orders in {1,2,4}) -- the group-theoretic shadow of
       the paper's selector arena Z/8.  By Lagrange an order-8 group has NO order-3 (or order-6)
       element.  A 2-group selector carries no mod-3 information: Hom(Z/2, Z/3) = 0, the
       Z2-analogue of this swing's Hom(Z/3, Z) = 0 discipline.  => the alignment selector lives
       entirely in the 2-primary selector arena Z/8; it is CRT-disjoint from the carrier arena
       Z/3 where the count would live.  A single object doing double duty would need a native
       Z/6 = Z/2 x Z/3 whose Z2 part is the alignment and Z3 part is the count -- and the native
       structure group is a 2-group with none.

  (S3) ORTHOGONALITY of the twist sector and the alignment sector.  The twist / count-carrier
       generator is the self-dual family su(2)+ (= Lambda^2_+, carrier of e_R = 1/12).  On W it
       is SPECTRALLY SCALAR: su(2)+ Casimir = 8.0 * I (measured), so the parity-sensitive
       alignment potential (built from Str(Phi^n) = tr(sign(K) Phi^n)) is su(2)+-blind, and
       [Q5, su(2)+] = 0.  The twist sector (base, 3-torsion home) and the alignment selector
       (internal, Z2) pass through each other without coupling.

  (S4) MULTIPLICITY vs INDEX, and the base arithmetic.  Alignment is a SPECTRAL operation: the
       aligned condensate M = phi* Pi_mirror gives the 96 mirrors a mass and leaves the 96
       generations massless -- it REMOVES modes, and by {K, chi} = 0 the physical sector stays
       achiral (Re tr(chi Pi_+) = 0), net chiral index 0.  The COUNT is a TOPOLOGICAL index:
       reusing the h2 canon / V7 arithmetic, ind_full == m^2 d' + sigma (mod 3), 3-divisibility
       <=> 3|m AND 3|sigma -- both external base data (twist degree m, signature sigma).  The
       alignment weight Q5 enters NONE of {k, m, d', sigma}; it is a mass weight, not a
       curvature that enters the index.  A spectral gapping cannot BE a topological index
       (the paper's Section 3 multiplicity-vs-index crux).

TARGET-IMPORT GUARD (maximum strictness): {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8}
never assumed, inserted, hardcoded as an answer, or divided by.  Every 3 printed carries its
provenance chain; the mod-3 reductions use 3 only as the modulus of the divisibility QUESTION
under test.  Every count statement is "mechanism/base M forces c", never "GU forces c".
Anchors reproduced first; residuals printed; random / scrambled controls throughout.

Hom(Z/3,Z)=0 DISCIPLINE: no torsion class is ever identified with an integer.  The only integer
that appears (the count) is the RELATIVE twisted-RS index of h2 canon, integer-by-construction;
the alignment weight is a Z2 class carrying mod-2 information only, never equated to a count.

HONEST OUTCOME: KILL of the double-duty branch -- the mirror-hiding source action is
base-agnostic (frame-trivial weight), its selector is an order-8 2-group (no 3-torsion), the
twist sector is scalar on the alignment channels, and alignment is spectral while the count is
topological.  Count and alignment are TWO SEPARATE external inputs; the count-import is
confirmed structural.  This STRENGTHENS the paper's CRT two-arena picture (selector in Z/8,
count in Z/3, disjoint) rather than bridging it.

Run from repo root:  python tests/big-swing/rs_s3_double_duty_base_selection.py   (exit 0)
Carrier machinery reused verbatim from tests/big-swing/vg_v7_cp2_equivariant_payoff.py /
as_a4_basin_stability.py / ghost_parity_krein.py.
"""
import sys
import numpy as np
import sympy as sp
from itertools import combinations

np.random.seed(20260707)

FAIL = []
nrm = np.linalg.norm
comm = lambda A, B: A @ B - B @ A
acomm = lambda A, B: A @ B + B @ A


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAIL.append(name)


# ============================================================================
print("=" * 96)
print("SECTION 0 -- CARRIER ANCHORS (verbatim recipe of ghost_parity_krein.py / VG-V2 / V7)")
print("=" * 96)
N, DIM = 14, 128
TIMELIKE = {4, 5, 6, 7, 8}
SPACELIKE = [a for a in range(N) if a not in TIMELIKE]
BASE = [0, 1, 2, 3]                       # base X^4 directions (all spacelike in the (9,5) build)
INT_SPACE = [9, 10, 11, 12, 13]           # internal spacelike (Q5 lives here)
INT_TIME = [4, 5, 6, 7, 8]                # internal timelike


def jw(n):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


base = jw(7)
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
e = [(1j * base[a] if a in TIMELIKE else base[a]) for a in range(N)]
etaV = np.diag([(-1.0 if a in TIMELIKE else 1.0) for a in range(N)]).astype(complex)


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


def gen(i, j):
    return np.kron(I14, sgen(i, j)) + np.kron(lvec(i, j), I128)


def mono_big(idxs):
    Mm = I128.copy()
    for a in idxs:
        Mm = Mm @ e[a]
    return np.kron(I14, Mm)


# beta_S = product of spacelike gammas (the Cartan-involution implementer on the spinor factor)
bS = I128.copy()
for s in SPACELIKE:
    bS = bS @ e[s]
if nrm(bS.conj().T + bS) < 1e-9:
    bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))
res_pah = max(nrm(bS @ sgen(i, j) + sgen(i, j).conj().T @ bS)
              for i in range(N) for j in range(i + 1, N))
print(f"  beta_S pseudo-anti-Hermiticity residual over all 91 so(9,5) generators: {res_pah:.1e}")
print(f"    (this residual = 0 is the Cartan involution theta X = -X^dag in module form -- V2)")
check("anchor: beta_S pseudo-anti-Hermitian (theta = Cartan involution, residual ~ 0)", res_pah < 1e-9)

Gam = np.hstack(e)
rankG = int(np.linalg.matrix_rank(Gam, tol=1e-9))
Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
w, Vv = np.linalg.eigh(Pi)
Wk = Vv[:, w > 0.5]
print(f"  rank(Gamma) = {rankG}   dim ker(Gamma) = {Wk.shape[1]}   (carrier dim {N * DIM})")
check("anchor: rank(Gamma) = 128, dim ker = 1664", rankG == 128 and Wk.shape[1] == 1664)

# self-dual su(2)+ (the twist generator / Lambda^2_+ / e_R carrier) and its triplet sector
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
ASD = [(0, 1, 3, 2), (0, 2, 1, 3), (0, 3, 2, 1)]
J3 = [gen(a, b) + gen(c, d) for (a, b, c, d) in SD]         # su(2)+ = self-dual Lambda^2_+
J3m = [gen(a, b) + gen(c, d) for (a, b, c, d) in ASD]       # su(2)- anti-self-dual
Cas = -(J3[0] @ J3[0] + J3[1] @ J3[1] + J3[2] @ J3[2])
CasK = Wk.conj().T @ Cas @ Wk
CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
top = max(round(x.real, 3) for x in ev)
Wt = Wk @ U[:, np.abs(ev - top) < 1e-3]
tdim = Wt.shape[1]
Rc = lambda M: Wt.conj().T @ M @ Wt
I192 = np.eye(tdim, dtype=complex)

Kful = np.kron(etaV, bS)
Kt = Rc(Kful)
Kt = 0.5 * (Kt + Kt.conj().T)
sig = np.linalg.eigvalsh(Kt)
npl, nmi, nz = int(np.sum(sig > 1e-9)), int(np.sum(sig < -1e-9)), int(np.sum(np.abs(sig) < 1e-9))
print(f"  triplet sector: dim {tdim}, su(2)+ Casimir top eigenvalue {top}, "
      f"Krein signature (+{npl}, -{nmi}, 0:{nz})")
check("anchor: triplet dim 192, su(2)+ Casimir top = 8, Krein signature (+96, -96, 0)",
      tdim == 192 and top == 8.0 and (npl, nmi, nz) == (96, 96, 0))

# chirality and ghost parity on the triplet
om = I128.copy()
for a in range(N):
    om = om @ e[a]
chiS = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
chi_t = Rc(np.kron(I14, chiS))
chi_t = 0.5 * (chi_t + chi_t.conj().T)
kev, kU = np.linalg.eigh(Kt)
Pg = (kU * np.sign(kev)) @ kU.conj().T
Pg = 0.5 * (Pg + Pg.conj().T)
res_pchi = nrm(acomm(Pg, chi_t))
print(f"  ghost parity P = sign(K_t): ||P^2 - I|| = {nrm(Pg @ Pg - I192):.1e}, "
      f"||{{P, chi}}|| = {res_pchi:.1e}, tr chi = {np.trace(chi_t).real:.1e}")
check("anchor: P^2 = I, {P, chi} = 0 (the cross-chirality Krein form, V1)",
      nrm(Pg @ Pg - I192) < 1e-9 and res_pchi < 1e-9)

# THE ALIGNMENT WEIGHT: Q5 = internal spacelike 5-volume, restricted to W (= -P_ghost)
Q5 = Rc(mono_big(INT_SPACE))
Q5 = 0.5 * (Q5 + Q5.conj().T)
print(f"  V8 identity (the alignment weight): Q5 = e9..e13|_W = -P_ghost, ||Q5 + P|| = "
      f"{nrm(Q5 + Pg):.1e}, Q5^2 = I ({nrm(Q5 @ Q5 - I192):.1e})")
check("anchor: Q5 = -P_ghost = -K|_W, the tr(Q5 Phi^2) alignment weight, order 2 (Q5^2 = I)",
      nrm(Q5 + Pg) < 1e-8 and nrm(Q5 @ Q5 - I192) < 1e-9)

# ============================================================================
print()
print("=" * 96)
print("SECTION 1 -- (S1) BASE-AGNOSTICISM: the alignment weight has ZERO base tangent-frame charge")
print("=" * 96)
print("  The count lives on the base X^4 (twist O(m) from su(2)+ = Lambda^2_+; signature sigma;")
print("  gravitational framing e_R). The alignment weight Q5 = tr(Q5 Phi^2) coupling weight is")
print("  the INTERNAL spacelike 5-volume. Its base charge is the double-duty question.")
print()

# base-frame so(4): the six sigma_ab, a,b in {0,1,2,3}, restricted to W
base_frame = []
base_names = []
for a, b in combinations(BASE, 2):
    base_frame.append(Rc(gen(a, b)))
    base_names.append(f"gen({a},{b})")
worst_base = max(nrm(comm(Q5, G)) / nrm(Q5) for G in base_frame)
print(f"  [Q5, so(4)_base] over all 6 base-frame generators: max ||[Q5, gen_base]||/||Q5|| = "
      f"{worst_base:.1e}")
check("Q5 COMMUTES with the entire base tangent frame so(4)_base "
      "(e_a base anticommutes past 5 internal gammas: (-1)^5 per index, +1 for the pair)",
      worst_base < 1e-9)

# overlap with Lambda^2_+ (the self-dual twist generator that carries e_R = 1/12)
def frob(A, B):
    return np.trace(A.conj().T @ B)


J3W = [Rc(J) for J in J3]                     # su(2)+ generators restricted to W
overlaps = [abs(frob(Q5, iJ)) / (nrm(Q5) * nrm(iJ)) for iJ in J3W]
worst_sd = max(overlaps)
print(f"  <Q5, Lambda^2_+> normalized overlap over the 3 self-dual generators: max = {worst_sd:.1e}")
print(f"    (Q5 is Clifford grade 5 (odd), the su(2)+ generators are grade 2 -- grade-orthogonal)")
check("Q5 has ZERO overlap with the self-dual su(2)+ = Lambda^2_+ twist direction "
      "(the direction carrying the order-3 e_R = 1/12 framing)", worst_sd < 1e-9)

# CONTROL: Q5 is NOT vacuously trivial -- it is charged under internal boosts
int_boost = Rc(gen(INT_SPACE[0], INT_TIME[0]))       # sigma_9,4: internal spacelike-timelike boost
r_boost = nrm(comm(Q5, int_boost)) / nrm(Q5)
print(f"  CONTROL: [Q5, internal boost sigma_9,4] / ||Q5|| = {r_boost:.3f}  (Q5 is a GENUINE")
print(f"    internal-boost-charged operator -- base-triviality is a real property, not vacuous)")
check("CONTROL: Q5 is charged under internal boosts (not identically frame-trivial everywhere)",
      r_boost > 0.1)

# cross-check: the paper's chiralizer J_quat carries no self-dual (p_1 / Lambda^2_+) charge
# (paper Sec 6 anchor: |<J_quat, Lambda^2_+>| = 0 -- the chiralizer lives in the selector arena).
# NOTE: the raw imaginary-gamma product does NOT commute with the full base so(4) rotation
# (that would need the paper's specific internal U); the load-bearing, convention-independent
# anchor is the vanishing self-dual OVERLAP, reproduced here.
S_imag = [a for a in range(N) if nrm(e[a].conj() + e[a]) < 1e-12]
Cq = I128.copy()
for a in S_imag:
    Cq = Cq @ e[a]
Jq = Rc(np.kron(I14, Cq))                              # J_quat-type linear part on W
sd_jq = max(abs(frob(Jq, iJ)) / (nrm(Jq) * nrm(iJ)) for iJ in J3W)
print(f"  cross-check (paper Sec 6): <J_quat, Lambda^2_+> = {sd_jq:.1e} (the chiralizer carries no "
      f"self-dual p_1 charge -- selector-arena, like Q5)")
check("paper anchor reproduced: the antilinear chiralizer J_quat has zero self-dual overlap "
      "(|<J_quat, Lambda^2_+>| = 0, Section 6)", sd_jq < 1e-9)

print()
print("  (S1) VERDICT: the alignment coupling weight Q5 carries ZERO base tangent-frame charge")
print("  (commutes with so(4)_base, orthogonal to Lambda^2_+). The mirror-hiding dynamics is")
print("  BASE-AGNOSTIC at the frame level: it cannot see the base topology, hence cannot select")
print("  it. On W, Q5 = -P_ghost is the SAME Z2 as the ghost parity / Cartan seat -- a selector-")
print("  arena object (Section 2).")

# ============================================================================
print()
print("=" * 96)
print("SECTION 2 -- (S2) 2-ADIC vs 3-TORSION: the alignment selector is a Z2, no order-3 element")
print("=" * 96)

# the orientation flip is chi-conjugation: chi Q5 chi = -Q5 (A2/A3)
flip = chi_t @ Q5 @ chi_t
print(f"  orientation flip = chi-conjugation: ||chi Q5 chi + Q5|| = {nrm(flip + Q5):.1e} "
      f"(chi Q5 chi = -Q5)")
check("the alignment-selecting sign is flipped by chi-conjugation (A2/A3): chi Q5 chi = -Q5 "
      "-- the selector is a Z2", nrm(flip + Q5) < 1e-8)

# the alignment selector P (= -Q5) anticommutes with the orientation-flip chi: {P, chi} = 0,
# so (P.chi)^2 = P chi P chi = -P^2 chi^2 = -I. The multiplicative group <P, chi> therefore
# contains -I and is a 2-group of order 8 (P^2 = chi^2 = I, (Pchi)^2 = -I) -- the group-theoretic
# shadow of the paper's selector arena Z/8. Generate it explicitly and read element orders.
def elt_order(M, maxr=12):
    P_ = M.copy()
    for r in range(1, maxr + 1):
        if nrm(P_ - I192) < 1e-8:
            return r
        P_ = P_ @ M
    return None


def close_group(gens, maxsize=64):
    grp = [I192.copy()]
    frontier = [I192.copy()]
    while frontier:
        new = []
        for A in frontier:
            for g in gens:
                for prod in (A @ g, A @ g.conj().T):
                    if all(nrm(prod - G) > 1e-7 for G in grp):
                        grp.append(prod)
                        new.append(prod)
                        if len(grp) > maxsize:
                            return grp
        frontier = new
    return grp


Grp = close_group([Pg, chi_t])
grp_orders = sorted({elt_order(G) for G in Grp})
print(f"  multiplicative group <P, chi>: |G| = {len(Grp)}, element orders present = {grp_orders}")
print(f"    (P^2 = chi^2 = I, {{P,chi}} = 0 => (P.chi)^2 = -I => -I in G => 2-group of order 8)")
is_2group = (len(Grp) & (len(Grp) - 1)) == 0                # power of 2
no_3 = all(o is not None and o % 3 != 0 for o in grp_orders)
check("the alignment structure group <P, chi> is a 2-GROUP (|G| = 8, a power of 2) -- the shadow "
      "of the selector arena Z/8", is_2group and len(Grp) == 8)
check("NO element of <P, chi> has order divisible by 3 (orders all in {1,2,4}); by Lagrange no Z3 "
      "or Z6 subgroup can exist in an order-8 group -- the alignment selector carries no 3-torsion",
      no_3 and 3 % len(Grp) != 0)
print("  Hom(Z/2, Z/3) = 0: a 2-group selector carries NO mod-3 information -- the Z2-analogue of")
print("  this swing's Hom(Z/3, Z) = 0 discipline. The alignment selector lives ENTIRELY in the")
print("  2-primary selector arena Z/8 (paper Sec 5), whose group shadow it literally is; the count")
print("  would live in the CRT-disjoint carrier arena Z/3. Double-duty would need a NATIVE")
print("  Z/6 = Z/2 x Z/3 whose Z2 part is the alignment and Z3 part is the count -- and the native")
print("  structure group <P, chi> is an order-8 2-group with none.")

# ============================================================================
print()
print("=" * 96)
print("SECTION 3 -- (S3) ORTHOGONALITY: the twist / e_R generator su(2)+ is SCALAR on W")
print("=" * 96)
print("  The twist O(m) and the order-3 e_R = 1/12 both ride the self-dual family su(2)+ =")
print("  Lambda^2_+. If su(2)+ acted nontrivially on the alignment channels, the mirror dynamics")
print("  could couple to the twist. It does not:")

# su(2)+ Casimir is scalar on W (measured), so the parity-sensitive potential is su(2)+-blind
CasW = Rc(Cas)
CasW = 0.5 * (CasW + CasW.conj().T)
cas_scalar = nrm(CasW - top * I192) / nrm(CasW)
print(f"  su(2)+ Casimir on W = {top} * I: ||Cas_W - 8 I||/||Cas_W|| = {cas_scalar:.1e}")
check("su(2)+ Casimir is EXACTLY scalar on W (measured top = 8) -- the parity-sensitive "
      "alignment potential Str(Phi^n) is su(2)+-blind (Casimir -> plain trace, not supertrace)",
      cas_scalar < 1e-9)

# [Q5, su(2)+] = 0 : the alignment weight commutes with the twist generator
worst_q5_su2 = max(nrm(comm(Q5, Rc(J))) / nrm(Q5) for J in J3)
print(f"  [Q5, su(2)+] over the 3 self-dual generators: max = {worst_q5_su2:.1e}")
check("[Q5, su(2)+] = 0: the alignment weight and the twist generator commute -- the twist "
      "sector (base, 3-torsion home) and the alignment selector (internal, Z2) are orthogonal",
      worst_q5_su2 < 1e-9)

# and su(2)- (the anti-self-dual doublet route of h2 canon) is also scalar / commuting on W
Casm = -(J3m[0] @ J3m[0] + J3m[1] @ J3m[1] + J3m[2] @ J3m[2])
CasmW = Rc(Casm)
CasmW = 0.5 * (CasmW + CasmW.conj().T)
evm = np.linalg.eigvalsh(CasmW)
topm = round(evm.max(), 3)
print(f"  su(2)- Casimir on W: top eigenvalue {topm} (the anti-self-dual doublet route of h2 canon)")
check("su(2)- Casimir top = 3.0 on W (measured; the doublet route also acts by a fixed Casimir, "
      "not through the alignment channels)", topm == 3.0)

print()
print("  (S3) VERDICT: the self-dual su(2)+ that builds the twist O(m) and carries e_R is")
print("  SPECTRALLY SCALAR on the alignment channels and commutes with Q5. The mirror dynamics")
print("  and the twist sector pass through each other without coupling: alignment cannot select m.")

# ============================================================================
print()
print("=" * 96)
print("SECTION 4 -- (S4) MULTIPLICITY vs INDEX: alignment is spectral, the count is topological")
print("=" * 96)

# 4a. Alignment is a spectral gapping with net chiral index 0 (achirality, {K,chi}=0)
print(" 4a. ALIGNMENT is a SPECTRAL operation (gap the mirrors), net chiral index 0:")
PIm = 0.5 * (I192 + Q5)                    # mirror projector = (I - P)/2
PIg = 0.5 * (I192 - Q5)                    # generation projector = (I + P)/2
phi = 1.0
Maligned = phi * PIm                       # the aligned condensate (gaps mirrors, keeps gens massless)
gen_masses = np.sort(np.abs(np.linalg.eigvalsh(0.5 * (Maligned + Maligned.conj().T))))
n_massless = int(np.sum(gen_masses < 1e-9))
n_massive = int(np.sum(gen_masses > 1e-9))
print(f"  aligned condensate phi* Pi_mirror: {n_massless} massless (generations), "
      f"{n_massive} gapped (mirrors)")
check("alignment GAPS 96 mirrors and keeps 96 generations massless -- a SPECTRAL split, not an "
      "index", n_massless == 96 and n_massive == 96)

# physical projector (max K-positive) and the achirality readout Re tr(chi Pi_+) = 0
Ep = kU[:, kev > 0]                         # generation (K-positive) frame
PiPlus = Ep @ Ep.conj().T                   # a physical (K-positive) subspace projector
re_chi = np.real(np.trace(chi_t @ PiPlus))
print(f"  achirality (paper theorem, {{K,chi}} = 0): Re tr(chi Pi_+) = {re_chi:.1e}")
check("physical sector is ACHIRAL: Re tr(chi Pi_+) = 0 (forced by {K, chi} = 0, cross-chirality "
      "Krein form) -- the condensate produces no net chiral count", abs(re_chi) < 1e-8)
# CONTROL: a K-COMMUTING involution gives Re != 0 (the identity hinges on {K,chi}=0)
Rctrl = np.diag([1.0 if i % 2 == 0 else -1.0 for i in range(tdim)]).astype(complex)
re_ctrl = np.real(np.trace(Rctrl @ PiPlus))
check("CONTROL: a generic K-commuting grading gives Re tr(R Pi_+) != 0 -- achirality hinges "
      "exactly on chi being K-cross (anti-commuting)", abs(re_ctrl) > 0.1)

# 4b. The COUNT is a topological base index -- reuse the h2 canon / V7 arithmetic (exact sympy)
print()
print(" 4b. The COUNT is a TOPOLOGICAL index on the base (h2 canon / V7 arithmetic, exact sympy):")
kk_, d_, m_, sig_, dp_ = sp.symbols("k d m sigma d'", integer=True)
jr = sp.Rational
T_dynk = lambda jj: sp.nsimplify(jj) * (sp.nsimplify(jj) + 1) * (2 * sp.nsimplify(jj) + 1) / 3
assert T_dynk(jr(1, 2)) == jr(1, 2) and T_dynk(1) == 2
# full 16-dim multiplicity bundle [leg-3 content 2(0) + 4(1/2) + 2(1)] + CP-twist rk*c1^2/2 + grav
ind_full = sp.expand(2 * 0 + 4 * (2 * T_dynk(jr(1, 2)) * kk_) + 2 * (2 * T_dynk(1) * kk_)
                     + 16 * (m_ ** 2 * d_ / 2) + 16 * (-sig_ / 8))
check("ind_full = 12k + 8 m^2 d - 2 sigma (h2 canon / V7 formula, Dynkin T(1/2)=1/2, T(1)=2)",
      sp.expand(ind_full - (12 * kk_ + 8 * m_ ** 2 * d_ - 2 * sig_)) == 0)
ind_spin = sp.expand(ind_full.subs(d_, 2 * dp_))         # spin X => d = 2 d'
resid3 = sp.expand(ind_spin - (m_ ** 2 * dp_ + sig_))
all_div3 = all(int(c) % 3 == 0 for c in sp.Poly(resid3, kk_, dp_, sig_, m_).coeffs())
print(f"  ind_full(spin) = {ind_spin};   mod 3:  ind_full == m^2 d' + sigma  (mod 3)")
check("exact: ind_full - (m^2 d' + sigma) divisible by 3 (12==0, 16==1, -2==1 mod 3)", all_div3)
print("  section-independent 3-divisibility  <=>  3 | m  AND  3 | sigma  (both EXTERNAL base data;")
print("  with Rokhlin 16|sigma: sigma == 0 mod 48). The alignment weight Q5 enters NONE of")
print("  {k, m, d', sigma}: it is a mass weight on the spectrum, not a curvature in the index.")
# every natively-selected twist m (V7) has m^2 == 1 mod 3
selected_m = [(1, "breaking line O(-1)"), (2, "quadratic condensate O(-2)"), (5, "coset D anticanon O(5)")]
allm1 = all((mm ** 2) % 3 == 1 for mm, _ in selected_m)
for mm, srcm in selected_m:
    print(f"    m = {mm} ({srcm}): m^2 == {(mm**2) % 3} (mod 3)")
check("every V7-natively-selected twist m in {1,2,5} has m^2 == 1 (mod 3): the base contributes "
      "nothing mod 3 that alignment could touch", allm1)

print()
print("  (S4) VERDICT: alignment is a SPECTRAL gapping (removes mirror modes, net chiral index 0")
print("  by {K,chi}=0); the count is a TOPOLOGICAL base index (needs 3|m AND 3|sigma, external).")
print("  A representation-dimension gapping is not an operator index (paper Section 3): the")
print("  mirror-hiding source action cannot BE the count.")

# ============================================================================
print()
print("=" * 96)
print("SECTION 5 -- (S5) THE CARTAN=KREIN=GHOST-PARITY CONSTRAINT (V2): does it force a 3-base?")
print("=" * 96)
print("  V2: the Krein form K IMPLEMENTS the Cartan involution theta of so(9,5); on W its module")
print("  image is P = -Q5 -- so the alignment weight IS the Cartan seat (one Z2). The double-duty")
print("  question at this grade: does the Cartan constraint the alignment respects force a base")
print("  carrying 3-torsion?")

# reproduce the V2 identity on W: theta commutes with the family su(2)+ (twist generator)
theta_seat = Pg                                          # = -Q5, the Cartan-seat operator on W
worst_theta_su2 = max(nrm(comm(theta_seat, Rc(J))) / nrm(theta_seat) for J in J3)
print(f"  V2 reproduced on W: [theta_seat (= -Q5), su(2)+] max = {worst_theta_su2:.1e} "
      f"(Cartan seat commutes with the twist generator)")
check("V2: the Cartan seat commutes with the family su(2)+ twist generator (it does not select "
      "the base twist)", worst_theta_su2 < 1e-9)
# and the Cartan seat is base-frame-trivial (same as Q5, since theta_seat = -Q5)
worst_theta_base = max(nrm(comm(theta_seat, G)) / nrm(theta_seat) for G in base_frame)
check("the Cartan seat is base tangent-frame-trivial ([theta_seat, so(4)_base] = 0): its V2 "
      "payoff is the maximal-COMPACT gauge chain (so(5)+so(5), su(4)+su(2)+su(2), su(3)+su(2)+u(1)"
      "), all 2-adic gauge groups -- internal, NOT the base frame where sigma/m live",
      worst_theta_base < 1e-9)
print("  The Cartan involution's payoff (V2) is a GAUGE-sector structure -- the 2-adic maximal-")
print("  compact chain. It lives in the internal/gauge sector, disjoint from the base tangent")
print("  frame that carries the count's 3-torsion (sigma, m). The Cartan constraint the alignment")
print("  respects cannot force base 3-torsion; it forces 2-adic gauge groups.")

# ============================================================================
print()
print("=" * 96)
print("SECTION 6 -- FORBIDDEN-SET AUDIT AND ROUTE VERDICT")
print("=" * 96)
print("""Forbidden set {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8}: never assumed, inserted,
hardcoded as an answer, or divided by. Provenance of every 3 printed above:
  * su(2)+ Casimir top = 8: MEASURED eigenvalue on W (the triplet-sector marker), used only to
    show su(2)+ is scalar; not the forbidden 8 (= ind_H) and entered no count formula;
  * su(2)- Casimir top = 3.0: MEASURED eigenvalue (the doublet-route Casimir of h2 canon), used
    only to show su(2)- acts by a fixed Casimir; entered no count;
  * m in {1,2,5}: the V7-selected twist degrees (stabilizer-character outputs), reused; m^2 mod 3
    is the divisibility QUESTION, 3 used only as modulus;
  * ind_full = 12k + 8 m^2 d - 2 sigma: h2 canon formula; Dynkin /3 is library math anchored by
    T(1/2)=1/2; the 8 here is 2*T(adj)*... a MEASURED Dynkin product, not ind_H;
  * Hom(Z/2,Z/3) = 0 and Hom(Z/3,Z) = 0: the arithmetic discipline, no target inserted.
Every count statement is 'mechanism/base M forces c'; no torsion class is equated to an integer.""")
print()
if FAIL:
    print(f"RESULT: {len(FAIL)} CHECK(S) FAILED: {FAIL}")
    sys.exit(1)
print("RESULT: all checks passed.")
print()
print("ROUTE S3 VERDICT (printed for the doc):")
print("  DOUBLE-DUTY conjecture -- 'the mirror-hiding source action selects the count base' --")
print("  is KILLED on four independent legs (kinematic/potential + symbolic scope):")
print("   (S1) BASE-AGNOSTIC: the alignment weight Q5 has zero base tangent-frame charge")
print("        ([Q5, so(4)_base] = 0, <Q5, Lambda^2_+> = 0) -- it cannot see, hence cannot")
print("        select, any base topology. (Control: Q5 is internal-boost-charged, not vacuous.)")
print("   (S2) 2-ADIC SELECTOR: the alignment selector group <P, chi> is an order-8 2-group")
print("        (Q5^2=I, chi Q5 chi=-Q5, (P.chi)^2=-I) -- the shadow of the selector arena Z/8,")
print("        with NO order-3 element. A 2-group carries no mod-3 info (Hom(Z/2,Z/3)=0).")
print("        Double-duty would need a native Z/6; the native structure group is a 2-group.")
print("   (S3) ORTHOGONAL SECTORS: the twist/e_R generator su(2)+ is scalar on W (Casimir 8 I)")
print("        and commutes with Q5 -- the twist sector and the alignment selector do not couple.")
print("   (S4) SPECTRAL vs TOPOLOGICAL: alignment gaps mirrors (net chiral index 0 by {K,chi}=0);")
print("        the count is a base index needing 3|m AND 3|sigma (external). A gapping is not an")
print("        index (paper Section 3). Alignment enters none of {k, m, d', sigma}.")
print("   (S5) The Cartan=Krein=ghost-parity constraint (V2) ties alignment to the 2-adic maximal-")
print("        compact GAUGE chain, internal, not the base frame -- it cannot force base 3-torsion.")
print("  CONCLUSION: count and alignment are TWO SEPARATE external inputs. The count-import is")
print("  confirmed STRUCTURAL. This STRENGTHENS the paper's CRT two-arena picture (selector in")
print("  Z/8, count in Z/3, disjoint) -- it does not bridge it. conjecture_signal = KILL")
print("  (double-duty branch); the broader order-3 conjecture stays OPEN via an INDEPENDENT")
print("  built source action that could carry its own 3|m or 3|sigma import.")
sys.exit(0)
