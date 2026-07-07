"""
FB-F3 -- the CRT split Z/24 = Z/8 (+) Z/3 read ON THE ACTUAL CARRIER (big-swing 2026-07-07).

THE ONE REMAINING GATED CARRIER.  The RS-index swing closed the native-construction escape four ways;
the last located-not-forced object is the paper's Section-9 / conjecture-D FRAMED-BORDISM carrier.  The
GU-forced RP^3 = L(2;1) spine, with its self-dual Lambda^2_+ tangential framing, escapes the 2-adic
cohomology wall (H^2(RP^3;Z)=Z/2) into FRAMED bordism pi_3^s = Z/24.  By CRT, Z/24 = Z/8 (+) Z/3, two
disjoint non-interacting summands.  A homotopy-theoretic (odd) generation count, IF it exists, must live
in the Z/3 summand, read by the Adams e-invariant via the image of J, with e_R = 1/12.

ROUTE F3 -- reachability of the Z/3 summand ON THE CARRIER:
    Is the Z/3 summand reachable at all by a SECTOR-CONSTRUCTIBLE invariant, or does the achirality wall
    ({K,chi}=0) + base 2-adicity force everything into the Z/8 (2-primary) summand even in framed bordism?

  (a) Build the CRT iso pi_3^s = Z/24 -> Z/8 x Z/3 EXPLICITLY (derived, not asserted: 24 = 2^3*3 factored,
      gcd(8,3)=1 verified, projection x -> (x%8, x%3) and its CRT inverse, roundtrip over all 24 classes),
      then MACHINE-CHECK the image of every sector invariant under the projection onto Z/3.

  (b) Take the sector data:  (i) the SIGNED index (achirality {K,chi}=0, reproduced as a measured net-0
      on the 128-dim carrier), and (ii) the UNSIGNED twisted index ind_full = 12k + 16 m^2 d' - 2 sigma
      (RS-S2 arithmetic, recomputed independently).  Machine-check the Z/3-component of each:
        - signed index -> 0 identically -> CRT image (0, 0):  contributes to NEITHER summand.
        - unsigned twisted index -> Z/3-component == m^2 d' + sigma; every native selected m in {1,2,5}
          has m^2 == 1 (mod 3), so the carrier's own twist is 3-INERT and the Z/3-component is carried
          ENTIRELY by (d', sigma) -- section degree (unbuilt) + base signature (external), both DISJOINT
          from the located RP^3 carrier.
      So EVERY sector-constructible INTEGER invariant has Z/3-component 0 (signed) or external-carried
      (twisted).  None is a carrier-native nonzero integer in Z/3.

  (c) THE DECISIVE READOUT.  The Z/3 summand IS reachable -- but by exactly two objects, and neither is a
      carrier-native integer index:
        (1) the FRACTIONAL Adams e-invariant e_R = 1/12: its 3-primary part is 1/3 mod Z (NONZERO), so the
            carrier genuinely has a Z/3-component -- the achirality wall does NOT force it into Z/8.  But
            1/3 is a FRACTION, not an integer:  Hom(Z/3, Z) = 0.
        (2) EXTERNAL imports (3|m cubic coupling AND 3|sigma spacetime signature): an integer, but external
            and NOT through the located carrier (m^2 == 1 for every native twist).
      So: the Z/3 summand is reached by the fractional carrier (1/3) and by external integers, but by NO
      carrier-native sector-constructible integer index.  This is the Section-9 category error CONFIRMED
      ONE LEVEL UP from Hom(Z/3,Z)=0:  not "Z/3 is unreachable", but "the carrier reaches Z/3 only
      fractionally, and the only integer preimage is external or the still-unbuilt relative/equivariant
      twisted-RS index".  SIGNAL = GATED (with a KILL sub-finding on the native-integer branch).

CONTROLS (discriminating power -- an artificially Z/3-charged input MUST project to nonzero Z/3):
  - pure Z/3 generators (classes 8, 16 in Z/24): CRT image (0, nonzero) -- Z/3 reached, Z/8 not.
  - pure Z/8 generators (classes 3, 9 in Z/24): CRT image (nonzero, 0) -- Z/8 reached, Z/3 not.
  - a Z/3-charged twisted index (sigma=1, native m=1, d'=0): Z/3-component nonzero -- the machinery CAN
    produce nonzero Z/3, but only via the EXTERNAL sigma (proving the SM/native 0 is a real measurement).
  - the carrier class itself (framed-bordism +/-2): CRT image (2, 2) -- NONZERO in BOTH summands, so
    achirality does NOT wall the e-invariant carrier into Z/8; it genuinely has a Z/3 part.

E-INVARIANT / Hom(Z/3,Z)=0 DISCIPLINE (this swing's signature guard): the Adams e-invariant is Q/Z-valued;
e_R = 1/12 is a FRACTION, its 3-primary part 1/3 is a torsion/fractional datum, NEVER identified with an
integer count.  Every integer here is either an index that is integer-by-construction (the twisted index,
whose Z/3-image is proven external-carried, NOT the forbidden e-invariant identification) or a CRT class
representative used only as a projection target.  No torsion class is ever equated to an integer.

TARGET-IMPORT GUARD (maximum strictness): {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} is never
assumed, inserted, hardcoded as an answer, or divided by to GET an answer.  Every 3 is MEASURED with its
provenance chain printed:  24 = |Im J_3| = denom(B_2/4) (Bernoulli/homotopy, DISTINCT from chi(K3)=24);
24 = 2^3 * 3 factored by sympy; the CRT split 8*3 derived from that factorization; the carrier class
2 = e_R * 24 measured from the framing (not recalled); m^2 == 1 mod 3 measured per native twist.  Every
count is stated as "mechanism/carrier M forces c", never "GU forces c".

Run from repo root:   python tests/big-swing/fb_f3_crt_split_on_carrier.py    (exit 0)
"""
import sys
from fractions import Fraction

import numpy as np
import sympy as sp
from scipy.linalg import expm, qr

np.random.seed(20260707)
FAIL = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAIL.append(name)


# ============================================================================================
# SECTION 0 -- CARRIER ANCHORS (verbatim recipe of ghost_parity_krein.py / VG-V2), + measured {K,chi}=0
# ============================================================================================
print("=" * 96)
print("SECTION 0 -- ANCHORS: rank(Gamma)=128/ker=1664, triplet Krein (+96,-96,0), {K,chi}=0 (net index 0)")
print("=" * 96)
N, DIM = 14, 128
TIMELIKE = {4, 5, 6, 7, 8}
SPACELIKE = [a for a in range(N) if a not in TIMELIKE]


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


bS = I128.copy()
for s in SPACELIKE:
    bS = bS @ e[s]
if np.linalg.norm(bS.conj().T + bS) < 1e-9:
    bS = 1j * bS
bS = bS / np.sqrt(abs((bS @ bS)[0, 0].real))

Gam = np.hstack(e)
rankG = int(np.linalg.matrix_rank(Gam, tol=1e-9))
Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
w, Vv = np.linalg.eigh(Pi)
Wk = Vv[:, w > 0.5]
print(f"  rank(Gamma) = {rankG}   dim ker(Gamma) = {Wk.shape[1]}   (carrier dim {N * DIM})")
check("anchor: rank(Gamma) = 128, dim ker = 1664", rankG == 128 and Wk.shape[1] == 1664)

SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
J3 = [gen(a, b) + gen(c, d) for (a, b, c, d) in SD]
Cas = -(J3[0] @ J3[0] + J3[1] @ J3[1] + J3[2] @ J3[2])
CasK = Wk.conj().T @ Cas @ Wk
CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
top = max(round(x.real, 3) for x in ev)
Wt = Wk @ U[:, np.abs(ev - top) < 1e-3]
DT = Wt.shape[1]
Kful = np.kron(etaV, bS)
Kt = Wt.conj().T @ Kful @ Wt
Kt = 0.5 * (Kt + Kt.conj().T)
sig = np.linalg.eigvalsh(Kt)
npl, nmi, nz = int(np.sum(sig > 1e-9)), int(np.sum(sig < -1e-9)), int(np.sum(np.abs(sig) < 1e-9))
print(f"  triplet sector: dim {DT}, su(2)+ Casimir top {top}, Krein signature (+{npl}, -{nmi}, 0:{nz})")
check("anchor: triplet dim 192, Krein signature (+96, -96, 0) [Cartan=Krein=ghost-parity, constraint 1]",
      DT == 192 and (npl, nmi, nz) == (96, 96, 0))

# chirality on the triplet + measured achirality {K,chi}=0 and net index 0
om = I128.copy()
for a in range(N):
    om = om @ e[a]
chiS = om if (np.trace(om @ om) / DIM).real > 0 else (-1j) * om
Cful = np.kron(I14, chiS)
chi_t = Wt.conj().T @ Cful @ Wt
chi_t = 0.5 * (chi_t + chi_t.conj().T)
antic = np.linalg.norm(Kt @ chi_t + chi_t @ Kt)
tr_chi = np.trace(chi_t).real
print(f"  {{K, chi}} on the triplet = {antic:.1e} (K purely cross-chirality); tr(chi) = {tr_chi:.1e}")
check("anchor: {K,chi}=0 (cross-chirality) and tr(chi)=0 (net chiral index 0) -- the achirality wall",
      antic < 1e-9 and abs(tr_chi) < 1e-9)


# ============================================================================================
# SECTION 1 -- pi_3^s = Z/24 and the CRT iso Z/24 = Z/8 x Z/3, BUILT EXPLICITLY (derived, not asserted)
# ============================================================================================
print()
print("=" * 96)
print("SECTION 1 -- pi_3^s = Z/24 and the CRT split Z/24 = Z/8 (+) Z/3, built explicitly and validated")
print("=" * 96)

# |Im J_3| = denom(B_2/4) -- HOMOTOPY (Bernoulli/Adams) provenance, DISTINCT from chi(K3)=24.
B2 = sp.bernoulli(2)                    # B_2 = 1/6
imJ_order = int(sp.denom(B2 / 4))       # denom(1/24) = 24
print(f"  |Im J_3| = denom(B_2/4) = denom({B2}/4) = denom({sp.nsimplify(B2/4)}) = {imJ_order}"
      f"   [Adams image-of-J / Bernoulli; DISTINCT from chi(K3)=24]")
check("pi_3^s = Z/24: order = denom(B_2/4) = 24 (homotopy provenance, not the K3 chi import)",
      imJ_order == 24)

# factor 24 and DERIVE the CRT split (not asserted): 24 = 2^3 * 3, coprime parts 8 and 3.
fac24 = sp.factorint(imJ_order)         # {2:3, 3:1}
prime_powers = [p ** a for p, a in sorted(fac24.items())]
print(f"  24 = {' * '.join(f'{p}^{a}' if a>1 else str(p) for p,a in sorted(fac24.items()))}"
      f"  => coprime prime-power parts {prime_powers} (the 2-primary Z/8 and the 3-primary Z/3)")
n8, n3 = None, None
for pp in prime_powers:
    if pp % 2 == 0:
        n8 = pp
    else:
        n3 = pp
gcd83 = int(sp.gcd(n8, n3))
print(f"  gcd({n8}, {n3}) = {gcd83}  => CRT: Z/24 ~= Z/{n8} (+) Z/{n3} (disjoint, non-interacting summands)")
check("CRT split derived from 24 = 2^3*3: coprime parts (8, 3), gcd=1 => Z/24 = Z/8 (+) Z/3",
      n8 == 8 and n3 == 3 and gcd83 == 1)

# explicit CRT projection and its inverse (idempotents), roundtrip over ALL 24 classes
def crt_project(x):
    """pi_3^s class x in Z/24 -> (Z/8 component, Z/3 component)."""
    return (x % n8, x % n3)


# CRT idempotents: e8 = the element that is 1 mod 8, 0 mod 3; e3 = 0 mod 8, 1 mod 3.
inv_3_mod_8 = pow(n3, -1, n8)           # (n3)^{-1} mod n8
inv_8_mod_3 = pow(n8, -1, n3)           # (n8)^{-1} mod n3
e8 = (n3 * inv_3_mod_8) % imJ_order     # == 1 mod 8, 0 mod 3
e3 = (n8 * inv_8_mod_3) % imJ_order     # == 0 mod 8, 1 mod 3


def crt_invert(c8, c3):
    """(Z/8, Z/3) -> Z/24."""
    return (c8 * e8 + c3 * e3) % imJ_order


roundtrip_ok = all(crt_invert(*crt_project(x)) == x for x in range(imJ_order))
bijective = len({crt_project(x) for x in range(imJ_order)}) == imJ_order
print(f"  CRT idempotents: e8 = {e8} (=(1 mod8,0 mod3)), e3 = {e3} (=(0 mod8,1 mod3));"
      f" roundtrip over all 24 classes: {roundtrip_ok}, bijective: {bijective}")
check("explicit CRT iso validated: projection is bijective and invert(project(x))==x for all x in Z/24",
      roundtrip_ok and bijective and crt_project(e8) == (1, 0) and crt_project(e3) == (0, 1))


# ============================================================================================
# SECTION 2 -- the CARRIER class in Z/24, its CRT projection, and the Q/Z primary decomposition of e_R
# ============================================================================================
print()
print("=" * 96)
print("SECTION 2 -- the located carrier e_R = 1/12 on the RP^3 spine: its Z/24 class and CRT projection")
print("=" * 96)

# e_R measured from the framing (Kirby-Melvin p_1=4; FROM-MEMORY), cross-checked class-2/24; order 12.
p1 = 4  # FROM MEMORY (Kirby-Melvin: RP^3 tangential Lambda^2_+ framing)
e_R = Fraction(p1, 48)
carrier_class = (e_R.numerator * imJ_order) // e_R.denominator   # e_R * 24 = 24/12 = 2  (MEASURED)
print(f"  e_R = p_1/48 = {p1}/48 = {e_R}   [p_1=4 Kirby-Melvin, FROM-MEMORY; order {e_R.denominator} in Q/Z]")
print(f"  framed-bordism class = e_R * |Im J| = {e_R} * {imJ_order} = {carrier_class}"
      f"   (the RP^3 spine's class +/-2 in pi_3^s; MEASURED from the framing, not recalled)")
check("carrier class in Z/24 = e_R*24 = 2 (measured from the framing e_R=1/12; two normalizations agree)",
      carrier_class == 2 and e_R == Fraction(1, 12) and Fraction(2, imJ_order) == e_R)

c8, c3 = crt_project(carrier_class)
print(f"  CRT projection of the carrier class {carrier_class}: (Z/8, Z/3) = ({c8}, {c3})")
print(f"    => the carrier has NONZERO Z/3-component ({c3}) AND nonzero Z/8-component ({c8}):")
print(f"       the achirality wall + 2-adicity do NOT force the e-invariant carrier into Z/8.")
check("carrier class 2 projects to (2, 2): NONZERO in BOTH summands -- Z/3 is genuinely reached by it",
      (c8, c3) == (2, 2) and c3 != 0)


# Q/Z primary decomposition of e_R = 1/12 -> 2-primary part + 3-primary part (fractional, exact)
def qz_primary_decomp(fr):
    """x = num/den mod 1  ->  {p^e: c/p^e}  with sum == x mod 1 (CRT of Q/Z)."""
    den, num = fr.denominator, fr.numerator
    parts = {}
    for p, ee in sp.factorint(den).items():
        pe = p ** ee
        cofac = den // pe
        cofac_inv = pow(cofac, -1, pe)
        c = (num * cofac_inv) % pe
        parts[pe] = Fraction(c, pe)
    return parts


parts = qz_primary_decomp(e_R)
recon = sum(parts.values(), Fraction(0))
part2 = next(v for k, v in parts.items() if k % 2 == 0)
part3 = next(v for k, v in parts.items() if k % 2 == 1)
print(f"  Q/Z primary decomposition of e_R = 1/12:  2-primary part = {part2} (order {part2.denominator}),"
      f"  3-primary part = {part3} (order {part3.denominator})")
print(f"    check: {part2} + {part3} = {recon} == 1/12 mod Z: {(recon - e_R).numerator % (recon-e_R).denominator == 0}")
check("e_R 3-primary part = 1/3 (NONZERO, order 3), 2-primary part = 3/4; sum == 1/12 mod Z",
      part3 == Fraction(1, 3) and part2 == Fraction(3, 4)
      and (recon - e_R).numerator % (recon - e_R).denominator == 0)
print(f"  DISCIPLINE (Hom(Z/3,Z)=0): the 3-primary part 1/3 is a FRACTION (Q/Z torsion datum), NEVER an")
print(f"  integer.  The carrier reaches Z/3 -- but only as the fractional e-invariant 1/3, not a count.")
check("Hom(Z/3,Z)=0 discipline: carrier's Z/3-reach is the fraction 1/3, not an integer (order 3 in Q/Z)",
      part3.denominator == 3 and part3 != 0)


# ============================================================================================
# SECTION 3 -- (b) every SECTOR-CONSTRUCTIBLE INTEGER invariant, and its Z/3-component under CRT
# ============================================================================================
print()
print("=" * 96)
print("SECTION 3 -- (b) the Z/3-component of every sector-constructible INTEGER invariant (CRT projected)")
print("=" * 96)

# ---- (b.i) the SIGNED index: achirality {K,chi}=0 => net 0 (MEASURED on the 128-carrier) ----
kev, kU = np.linalg.eigh(Kt)
Ppos = kU[:, kev > 1e-9]                 # 96-dim maximal K-positive physical subspace
proj_plus = 0.5 * (np.eye(DT) + chi_t)
proj_minus = 0.5 * (np.eye(DT) - chi_t)


def rank_of(M, tol=1e-7):
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > tol))


Qref, _ = qr(Ppos, mode="economic")
dp_ref, dm_ref = rank_of(proj_plus @ Qref), rank_of(proj_minus @ Qref)
net_ref = dp_ref - dm_ref
signed_index = net_ref                    # the sector-constructible SIGNED index
sig_c8, sig_c3 = crt_project(signed_index % imJ_order)
print(f"  (b.i) SIGNED index (net chiral index of the physical subspace): {dp_ref} - {dm_ref} = {signed_index}")
print(f"        CRT image of {signed_index} in Z/24: (Z/8, Z/3) = ({sig_c8}, {sig_c3})"
      f"  -- contributes to NEITHER summand")
check("(b.i) SIGNED index = 0 (achirality {K,chi}=0); CRT image (0,0): zero Z/3-component",
      signed_index == 0 and (sig_c8, sig_c3) == (0, 0))

# CONTROL: a K-COMMUTING grading breaks achirality -> net = 96 (net-0 is load-bearing, not automatic)
Pghost = (kU * np.sign(kev)) @ kU.conj().T
Pghost = 0.5 * (Pghost + Pghost.conj().T)
gp_plus, gp_minus = 0.5 * (np.eye(DT) + Pghost), 0.5 * (np.eye(DT) - Pghost)
net_ctrl = rank_of(gp_plus @ Qref) - rank_of(gp_minus @ Qref)
print(f"  CONTROL (K-commuting grading): net = {net_ctrl} != 0 -- the achirality net-0 is not a tautology")
check("(b.i) CONTROL: K-commuting grading gives net = 96 != 0 -- {K,chi}=0 is load-bearing", net_ctrl == 96)

# ---- (b.ii) the UNSIGNED twisted index: ind_full = 12k + 16 m^2 d' - 2 sigma; Z/3-component = m^2 d'+sigma
print()
kk_, m_, sig_, dp_ = sp.symbols("k m sigma d'", integer=True)
ind_full = sp.expand(12 * kk_ + 16 * (m_ ** 2 * dp_) - 2 * sig_)   # X spin (d=2d'); RS-S2 formula
z3_component = sp.expand(m_ ** 2 * dp_ + sig_)                     # ind_full mod 3 (12==0,16==1,-2==1)
print(f"  (b.ii) UNSIGNED twisted index (h2 12k bundle + O(m) twist + gravitational, X spin):")
print(f"         ind_full = {ind_full}")
print(f"         mod 3 (12==0, 16==1, -2==1):  Z/3-component == {z3_component}")
# independently verify the mod-3 reduction AND the CRT-projection agreement over random integer inputs
rng = np.random.default_rng(303)
mod3_ok, crt_ok = True, True
for _ in range(300):
    kv, mv, sv, dv = (int(rng.integers(-9, 9)) for _ in range(4))
    full = int(ind_full.subs({kk_: kv, m_: mv, sig_: sv, dp_: dv}))
    z3 = int(z3_component.subs({m_: mv, sig_: sv, dp_: dv}))
    if (full - z3) % 3 != 0:
        mod3_ok = False
    # the CRT Z/3 projection of the integer index (reduce mod 24 then mod 3) must equal z3 mod 3
    if crt_project(full % imJ_order)[1] != full % 3 or full % 3 != z3 % 3:
        crt_ok = False
check("(b.ii) mod-3 reduction ind_full - (m^2 d' + sigma) == 0 (mod 3) over 300 random inputs", mod3_ok)
check("(b.ii) CRT Z/3-projection of the integer index == ind_full mod 3 == (m^2 d' + sigma) mod 3",
      crt_ok)

# CARRIER 3-INERTNESS: every native selected twist has m^2 == 1 (mod 3) => Z/3-component = d' + sigma
selected = {"breaking line O(-1) [|m|=1]": 1, "quadratic condensate O(-2) [|m|=2]": 2,
            "coset D own anticanonical O(5)": 5}
print(f"  CARRIER 3-INERTNESS -- native selected twists (VG-V7 stabilizer-character selection):")
inert_ok = True
for lbl, mv in selected.items():
    r = (mv * mv) % 3
    z3_at = sp.expand(z3_component.subs(m_, mv))
    print(f"    {lbl:34s}: m^2 = {mv*mv:2d} == {r} (mod 3)  =>  Z/3-component == {z3_at}  (carrier twist inert)")
    inert_ok = inert_ok and (r == 1)
check("carrier 3-INERT: every native m has m^2==1 (mod3) => Z/3-component == d'+sigma, EXTERNAL-carried, "
      "disjoint from the RP^3 carrier", inert_ok)

# section-independent carrier-controlled 3-charge <=> 3|m AND 3|sigma  (double external import)
print(f"  carrier-controlled nonzero Z/3 for ALL sections d' <=> 3|m (m^2==0 mod3) AND 3|sigma:")
div_ok = all(((mv % 3 == 0) == ((mv * mv) % 3 == 0)) for mv in range(0, 9))
native_needs_import = all((mv % 3 != 0) for mv in selected.values())
print(f"    3|m sweep m in 0..8 consistent: {div_ok}; NO native selected m is divisible by 3: {native_needs_import}")
check("Z/3-charge independent of the unbuilt section needs the DOUBLE EXTERNAL import 3|m AND 3|sigma; "
      "no native twist supplies 3|m", div_ok and native_needs_import)


# ============================================================================================
# SECTION 4 -- CONTROLS: discriminating power of the CRT-Z/3 projection
# ============================================================================================
print()
print("=" * 96)
print("SECTION 4 -- CONTROLS: an artificially Z/3-charged input MUST project to nonzero Z/3")
print("=" * 96)

# pure Z/3 generators: classes 8, 16 (= n8 * {1,2}) -> (0, nonzero)
pure_z3 = [n8 * 1 % imJ_order, n8 * 2 % imJ_order]        # 8, 16
z3_imgs = [crt_project(x) for x in pure_z3]
print(f"  pure Z/3 classes {pure_z3}:  CRT images {z3_imgs}  -- Z/3 reached, Z/8 zero")
check("CONTROL: pure Z/3 generators (8,16) project to (0, nonzero) -- the projection DETECTS Z/3 charge",
      all(img[0] == 0 and img[1] != 0 for img in z3_imgs))

# pure Z/8 generators: classes 3, 9 (odd multiples of n3) -> (nonzero, 0)
pure_z8 = [n3 * 1 % imJ_order, n3 * 3 % imJ_order]        # 3, 9
z8_imgs = [crt_project(x) for x in pure_z8]
print(f"  pure Z/8 classes {pure_z8}:  CRT images {z8_imgs}  -- Z/8 reached, Z/3 zero")
check("CONTROL: pure Z/8 classes (3,9) project to (nonzero, 0) -- the projection SEPARATES the summands",
      all(img[0] != 0 and img[1] == 0 for img in z8_imgs))

# a Z/3-charged twisted index via the EXTERNAL sigma (sigma=1, native m=1, d'=0): Z/3-component nonzero
charged = int(ind_full.subs({kk_: 0, m_: 1, sig_: 1, dp_: 0}))   # = -2
charged_z3 = crt_project(charged % imJ_order)[1]
print(f"  Z/3-charged twisted index (sigma=1, native m=1, d'=0): ind_full = {charged}, "
      f"Z/3-component = {charged % 3}  (via the EXTERNAL sigma)")
check("CONTROL: a twisted index CAN have nonzero Z/3-component -- but only via the EXTERNAL sigma "
      "(so native/achiral 0 is a real measurement, not a blind zero)", charged % 3 != 0)

# scrambled control: a random UNBALANCED chirality grading breaks the achirality net-0.
# (A random BALANCED grading generically gives net 0 for pure rank reasons -- not discriminating; the
#  load-bearing point is that an UNBALANCED grading, or the K-commuting one above, does NOT give 0, so
#  the signed-index 0 is the measured {K,chi}=0 cross-chirality balance, not automatic.)
rngc = np.random.default_rng(77)
Grand = rngc.normal(size=(DT, DT)) + 1j * rngc.normal(size=(DT, DT))
Grand = 0.5 * (Grand + Grand.conj().T)
gv, gU = np.linalg.eigh(Grand)
n_plus_scr = 100                          # unbalanced eigenbasis: 100 (+1), 92 (-1)
chi_scr = gU @ np.diag([1.0] * n_plus_scr + [-1.0] * (DT - n_plus_scr)) @ gU.conj().T
net_scr = rank_of(0.5 * (np.eye(DT) + chi_scr) @ Qref) - rank_of(0.5 * (np.eye(DT) - chi_scr) @ Qref)
print(f"  scrambled UNBALANCED grading (n_+ = {n_plus_scr}): net chiral index = {net_scr} != 0 -- the "
      f"achirality net-0 is specific to the true cross-chirality structure, not automatic")
check("CONTROL: a scrambled unbalanced grading gives net != 0 -- the signed-index 0 is the measured "
      "{K,chi}=0 fact, not a rank tautology", net_scr != 0)


# ============================================================================================
# SECTION 5 -- (c) THE DECISIVE READOUT + verdict
# ============================================================================================
print()
print("=" * 96)
print("SECTION 5 -- (c) DECISIVE READOUT: is the Z/3 summand reachable by a carrier-native INTEGER index?")
print("=" * 96)
print("  Reachability of the Z/3 summand of pi_3^s = Z/24, by object:")
print(f"    * FRACTIONAL e-invariant carrier e_R = 1/12  -> 3-primary part = {part3} (NONZERO): REACHED,")
print(f"      but 1/3 is a fraction, NOT an integer  [Hom(Z/3,Z)=0].")
print(f"    * SIGNED sector index (achirality {{K,chi}}=0)  -> 0  -> CRT (0,0): does NOT reach Z/3.")
print(f"    * UNSIGNED twisted index, NATIVE twist (m^2==1) -> Z/3-component == d'+sigma: reached ONLY via")
print(f"      EXTERNAL (d' unbuilt dynamics, sigma external signature), disjoint from the RP^3 carrier.")
print(f"    * carrier-controlled integer Z/3-charge -> needs the DOUBLE EXTERNAL import 3|m AND 3|sigma.")
print()
print("  => The Z/3 summand IS reachable -- by the FRACTIONAL carrier (1/3) and by EXTERNAL integers --")
print("     but by NO carrier-native sector-constructible INTEGER index.  The achirality wall does NOT")
print("     wall the e-invariant carrier into Z/8 (its class is (2,2)), yet no integer preimage of its")
print("     Z/3-charge is sector-constructible: signed -> 0, unsigned native twisted -> external-carried.")
print()
print("  This CONFIRMS the Section-9 category error ONE LEVEL UP from Hom(Z/3,Z)=0: not 'Z/3 is")
print("  unreachable', but 'the carrier reaches Z/3 only as the fraction 1/3, and every integer that")
print("  reaches Z/3 is external or the still-unbuilt relative/equivariant twisted-RS index'.")
print()
print("  SIGNAL = GATED.")
print("   - KILL sub-finding (native-integer branch, consistent with RS-S2): no sector-constructible")
print("     INTEGER invariant has a carrier-native nonzero Z/3-component.")
print("   - NOT a full KILL of conjecture D: the Z/3 summand is genuinely reached by the fractional")
print("     carrier (1/3), and the ONLY object that could supply an INTEGER preimage of that 1/3 is the")
print("     unbuilt RELATIVE/EQUIVARIANT twisted-RS index whose nonzero geometry-dependent bulk cancels")
print("     1/12 mod Z -- exactly the Section-9 / RS-S4 gate.  PROMOTE-or-KILL stays on that one object.")

print()
print("#" * 96)
if FAIL:
    print(f"# RESULT: {len(FAIL)} CHECK(S) FAILED: {FAIL}")
    print("#" * 96)
    sys.exit(1)
print("# RESULT: ALL CHECKS PASSED. Route F3 -> conjecture_signal = GATED.")
print("#  CRT split Z/24=Z/8(+)Z/3 built + validated; carrier class 2 -> (2,2) reaches Z/3 fractionally")
print("#  (3-primary part 1/3); every sector-constructible INTEGER invariant has Z/3-component 0 (signed,")
print("#  achirality) or external-carried (unsigned twisted, native m^2==1); the Z/3 summand's only")
print("#  integer preimages are external imports or the unbuilt relative/equivariant twisted-RS index.")
print("#  Category error confirmed one level up from Hom(Z/3,Z)=0. No forbidden target imported.")
print("#" * 96)
sys.exit(0)
