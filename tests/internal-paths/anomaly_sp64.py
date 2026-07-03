#!/usr/bin/env python3
r"""INTERNAL PATH #6 -- Sp(64) global anomaly, GLOBAL/torsion leg via AHSS at odd primes.

Reuses the R2 big-swing machinery (tests/big-swing/R2_spin_bordism_mod3.py:
Atiyah-Hirzebruch spectral sequence localized at a prime; ABP/Wall input that
Omega^Spin_*(pt) is odd-torsion-free) and applies it to the OPEN Sp(64) global
anomaly-cancellation question instead of the SM.

WHAT THIS DECIDES (target-free)
-------------------------------
GU is a 14-dimensional fermionic theory. Its GLOBAL (Dai-Freed) gauge anomaly for a
gauge group G is classified by the TORSION of the spin-bordism group Omega^Spin_{D+1}(BG)
with D=14, i.e. Omega^Spin_15(BG) (Freed-Hopkins; Garcia-Etxebarria-Montero). The CANON
"Not Yet Canon" entry warns the global leg is "not settled by pi_15(Sp) alone." We make
that precise and settle the ODD-primary part of the global leg:

    Does Omega^Spin_15(B Sp(n)) have any ODD torsion?
    (a prime p enters ONLY as the localization prime to probe odd torsion; we never
     assume any generation/anomaly target, never divide by 3/8/24/chi.)

METHOD (identical to R2). AHSS at an odd prime p:
    E_2^{i,j}(p) = H_i(BG ; Omega^Spin_j(pt))_(p)  ==>  Omega^Spin_{i+j}(BG)_(p).
Two rigorous, cited, target-safe inputs:
  (I)  Omega^Spin_*(pt) is ODD-TORSION-FREE in every degree (Anderson-Brown-Peterson +
       Wall): 3-locally MSpin ~ MSO, a wedge of BP with torsion-free homotopy. So at an
       odd prime Omega^Spin_j is FREE, supported in j = 0,4,8,12,... . (We encode the
       standard low-degree table and ASSERT its torsion is 2-primary.)
  (II) H_*(B Sp(n) ; Z) = Z[q_1,...,q_n], the symplectic Pontryagin classes in degrees
       4,8,...,4n. TORSION-FREE and concentrated in degrees divisible by 4 (=> even; in
       particular H_odd = 0). This is standard and holds for EVERY n, so it covers both
       the naive "Sp(64)" reading (n=32; the fundamental H^64 has rank-32 Cartan) and the
       genuine Clifford commutant Sp(1)=right-H reading (n=1) from MOVE-1 / shiab_selector.

CONSEQUENCE we compute. In ODD total degree n (in particular n=15, the 4D... err 14D
Dai-Freed degree D+1=15), every (i,j) with i+j=n has i not-divisible-by-4-and-odd =>
either i odd (H_i=0) or j odd (Omega^Spin_j(p)=0). The whole odd-degree E_2 line vanishes
p-locally for every odd p. No page creates torsion from nothing => Omega^Spin_15(B Sp(n))
has NO odd torsion, for ANY n. It is therefore a purely 2-PRIMARY finite group (and has no
free part in odd degree either). This is independent of the assumed fermion content: the
content picks which class in the group the theory realizes, but the group's odd part is
empty, so no content can produce an odd-primary global anomaly obstruction.

pi_15(Sp) (the datum CANON says is "not enough"): Bott periodicity pi_i(Sp)=pi_{i+4}(O)
gives pi_15(Sp) = Z -- FREE, no torsion. It sees the perturbative octic (the free/local
degree-16 datum) but is torsion-blind, hence cannot see the global torsion anomaly. Our
AHSS locates that global torsion (purely 2-primary) exactly where pi_15 cannot look.

NON-VACUITY (house discipline: the strongest check must be able to FAIL). We run the
identical machinery on BZ_3 (H_odd = Z/3 in every odd degree) and CONFIRM it DOES find
3-torsion in Omega^Spin_15(BZ_3). So "no odd torsion for Sp(n)" is a real measurement.

NO TARGET IMPORT: the only integers are the localization primes {3,5,7}, the Sp Lie data
(generator degrees 4,8,...,4n), and standard bordism ranks. No 3-generations, no chi(K3),
no /8, no /24, no Ahat=3 anywhere.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import comb, factorial

NA = 0
def check(c, m):
    global NA; NA += 1
    assert c, "FAIL: " + m

# ----------------------------------------------------------------------------------------
# INPUT (I): Omega^Spin_n(pt), standard table 0..15. Store (free_rank, [torsion orders]).
#   All torsion is 2-primary (ABP/Wall: 3-locally MSpin ~ MSO ~ wedge of BP, torsion-free).
# ----------------------------------------------------------------------------------------
OmegaSpin = {  # n : (free_rank, [torsion orders])
    0:(1,[]), 1:(0,[2]), 2:(0,[2]), 3:(0,[]), 4:(1,[]), 5:(0,[]), 6:(0,[]), 7:(0,[]),
    8:(2,[]), 9:(0,[2,2]), 10:(0,[2,2,2]), 11:(0,[]), 12:(3,[]), 13:(0,[]), 14:(0,[]),
    15:(0,[]),
}
print("="*94)
print("INPUT (I): Omega^Spin_*(pt) is odd-torsion-FREE (ABP/Wall). Verify table torsion 2-primary.")
print("="*94)
for n,(fr,tors) in OmegaSpin.items():
    for t in tors:
        while t % 2 == 0: t //= 2
        check(t == 1, "Omega^Spin_%d torsion has an odd factor (contradicts ABP)" % n)
    print("  Omega^Spin_%2d = Z^%d + %-10s (odd-torsion-free: OK)"
          % (n, fr, ("+".join("Z/%d"%o for o in tors) if tors else "0")))

def omega_free_rank_oddlocal(j):
    """At any ODD prime, Omega^Spin_j = free part only (all torsion 2-primary dies)."""
    return OmegaSpin.get(j,(0,[]))[0]

# ----------------------------------------------------------------------------------------
# INPUT (II): H_i(B Sp(n); Z) ranks via Poincare series of Z[q_1..q_n], deg q_k = 4k.
#   Torsion-free; supported in degrees divisible by 4 => H_odd = 0 for every n.
# ----------------------------------------------------------------------------------------
def poincare_ranks(gen_degrees, N):
    r = [0]*(N+1); r[0] = 1
    for d in gen_degrees:
        nr = [0]*(N+1)
        for i in range(N+1):
            k = 0
            while i - k*d >= 0:
                nr[i] += r[i-k*d]; k += 1
        r = nr
    return r

N = 15
def H_BSp(n):
    """Return a function i -> (free_rank, has_odd_torsion) for H_*(BSp(n);Z)."""
    ranks = poincare_ranks([4*k for k in range(1, n+1)], N)
    def H(i):
        return (ranks[i] if 0 <= i <= N else 0, False)
    return H, ranks

print()
print("="*94)
print("INPUT (II): H_*(B Sp(n);Z)=Z[q_1..q_n] (deg 4k) torsion-free, H_odd=0. Verify Poincare ranks.")
print("="*94)
# Sp(1)=right-H commutant (MOVE-1 genuine reading, n=1); Sp(64)=U(64,H) naive reading
#   -> rank-32 Cartan, so BSp(32) (fundamental H^64 has weights {+-x_1..+-x_32}).
readings = [("Sp(1)=right-H (commutant, MOVE-1)", 1),
            ("Sp(2)  (control)", 2),
            ("Sp(64)=U(64,H) naive (rank 32)", 32)]
Hfuns = {}
for label, n in readings:
    H, ranks = H_BSp(n); Hfuns[label] = H
    odd = [ranks[i] for i in range(1, N+1, 2)]
    check(all(x == 0 for x in odd), "H_odd(B %s) must vanish" % label)
    print("  H_i(B %-34s) i=0..%d: %s" % (label, N, ranks))
    check(all(ranks[i] == 0 for i in range(1, N+1) if i % 4 != 0),
          "H_*(BSp) supported only in degrees divisible by 4")
print("  (all readings: H_odd = 0, support in degrees 0,4,8,...  -> OK)")

# NON-VACUITY control: BZ_3. H_0=Z; H_odd=Z/3 (every odd degree); H_{even>0}=0.
def H_BZ3(i):
    if i == 0: return (1, False)
    if i % 2 == 1: return (0, True)   # Z/3 torsion, no free part
    return (0, False)

# ----------------------------------------------------------------------------------------
# AHSS at an odd prime p. E_2^{i,j} = H_i (x) Omega^Spin_j.  Detect any odd torsion in
# total degree n. free(x)free=free; oddtors(x)free(rank>0)=oddtors; Tor(free,anything)=0.
# ----------------------------------------------------------------------------------------
def ahss_line_odd_torsion(Hfun, n):
    """(free_rank_sum, any_odd_torsion, detail) of the E_2 line i+j=n at an odd prime."""
    free_rank = 0; odd_tors = False; detail = []
    for j in range(0, n+1):
        i = n - j
        hr, htor_odd = Hfun(i)
        sj = omega_free_rank_oddlocal(j)
        fr = hr * sj
        e_tor = htor_odd and (sj > 0)
        if fr != 0 or e_tor: detail.append((i, j, fr, e_tor))
        free_rank += fr
        if e_tor: odd_tors = True
    return free_rank, odd_tors, detail

print()
print("="*94)
print("AHSS at an ODD prime:  Omega^Spin_n(B Sp(n_group)) on the ODD-degree line (n=1,3,...,15).")
print("  (result is prime-uniform for every odd p: inputs supported only in degrees div by 4.)")
print("="*94)
DAIFREED_DEG = 14 + 1  # D=14 GU theory -> Dai-Freed degree D+1 = 15
verdict = {}
for label, n in readings:
    H = Hfuns[label]
    allzero = True; line15 = None
    for tot in range(1, N+1, 2):
        fr, t, det = ahss_line_odd_torsion(H, tot)
        if tot == DAIFREED_DEG: line15 = (fr, t, det)
        check(fr == 0 and not t,
              "Omega^Spin_%d(B %s) must have NO odd torsion / no odd free" % (tot, label))
        if fr != 0 or t: allzero = False
    verdict[label] = allzero
    fr, t, det = line15
    print("  %-34s  n=%d line: free rank %d, odd-torsion: %s  entries=%s"
          % (label, DAIFREED_DEG, fr, t, det if det else "ALL ZERO"))
    print("      -> entire odd line (n=1..15) vanishes odd-locally: %s" % allzero)

print()
print("="*94)
print("NON-VACUITY control: same machinery on BZ_3 (H_odd=Z/3) at n=15. MUST find 3-torsion.")
print("="*94)
fr3, t3, det3 = ahss_line_odd_torsion(H_BZ3, 15)
print("  BZ_3, n=15:  free rank %d, odd-torsion present: %s  entries=%s" % (fr3, t3, det3))
check(t3, "machinery MUST detect the Z/3 in Omega^Spin_15(BZ_3) -- else it is vacuous")
# and confirm Sp(n) has NO odd torsion in the SAME degree where BZ_3 HAS it
for label, n in readings:
    _, ts, _ = ahss_line_odd_torsion(Hfuns[label], 15)
    check(not ts, "same degree n=15: B %s has NO odd torsion where BZ_3 HAS it" % label)
print("  contrast confirmed: Sp(n) empty at n=15 where BZ_3 is nonempty -> real measurement.")

# ----------------------------------------------------------------------------------------
# pi_15(Sp) is FREE (=Z): the 'not enough' datum, made precise. Bott: pi_i(Sp)=pi_{i+4}(O).
# ----------------------------------------------------------------------------------------
piO = {0:"Z/2",1:"Z/2",2:"0",3:"Z",4:"0",5:"0",6:"0",7:"Z"}  # pi_i(O), period 8
def pi_Sp(i):
    return piO[(i+4) % 8]
print()
print("="*94)
print("pi_15(Sp): the CANON 'not settled by pi_15(Sp) alone' datum, made precise.")
print("="*94)
print("  Bott pi_i(Sp)=pi_{i+4}(O):  pi_15(Sp) = %s   (FREE, torsion-free)" % pi_Sp(15))
check(pi_Sp(15) == "Z", "pi_15(Sp) should be Z (free) by Bott")
print("  => pi_15(Sp) is torsion-BLIND: it carries the perturbative octic (free datum) but")
print("     cannot see any global/torsion anomaly. The global torsion lives in the 2-primary")
print("     part of Omega^Spin_15(B Sp(n)) -- exactly where pi_15 cannot look. This is why the")
print("     global leg is 'not settled by pi_15(Sp) alone'.")

# ----------------------------------------------------------------------------------------
# LOCAL LEG (free/perturbative part), CONDITIONAL on assumed content. Recomputed here so
# both legs sit in one certificate. The local anomaly is the degree-16 = D+2 piece: the
# I_16 index density / anomaly polynomial. From MOVE-1 (move1_octic_sp64_vs_sp1.py):
#   * gauge octic Str_S F^8 under the genuine Sp(1)=right-H commutant = 128*(y^2)^4 = pure
#     product of quadratic Casimirs -> Green-Schwarz REDUCIBLE (no independent order-8 inv).
#   * the reading-INDEPENDENT gravitational tr R^8 (p4 of [A-hat(TY14)]_16) is nonzero iff
#     the ASSUMED truncated content has net chirality n_+ - n_- != 0.
# We recompute the p4 coefficient and the net-chirality factor (NO target divides anything).
# ----------------------------------------------------------------------------------------
print()
print("="*94)
print("LOCAL LEG (degree-16 anomaly polynomial / I_16), CONDITIONAL on assumed content.")
print("="*94)
# [A-hat]_16 p4 coefficient (the pure tr R^8 irreducible), exact, over AGW denominator.
# AGW deg-16 numerators over D=464486400: p4 -> -192.  => p4 coeff = -192/464486400.
D = 464486400
p4_coeff = Fr(-192, D)
check(p4_coeff == Fr(-1, 2419200), "p4 (grav irreducible) coeff must equal -1/2419200 (AGW)")
print("  [A-hat(TY14)]_16 pure-gravity p4 (~tr R^8) coeff = %s  (Alvarez-Gaume-Witten)" % p4_coeff)
# ASSUMED truncated GU content (repo canon): Omega^0(x)S^+ (rank C(14,0)=1) + Omega^1(x)S^- (rank C(14,1)=14)
rank0, rank1 = comb(14, 0), comb(14, 1)
netchi = (+1)*rank0 + (-1)*rank1     # n_+ - n_-  (ASSUMED content) = -13
dimS = 64                             # dim S = H^64 as a complex/real vector space (reading-independent)
grav_irr = Fr(dimS*netchi) * p4_coeff
print("  ASSUMED content: Omega^0(x)S^+ (rank %d) + Omega^1(x)S^- (rank %d)  [truncated, canon]"
      % (rank0, rank1))
print("     net chirality n_+ - n_- = %d   (CONDITIONAL on this truncation)" % netchi)
print("  grav tr R^8 irreducible coeff = dim(S)*(n_+ - n_-)*p4 = %d*%d*(%s) = %s"
      % (dimS, netchi, p4_coeff, grav_irr))
gauge_octic_irreducible_Sp1 = False   # MOVE-1: 128*(y^2)^4 is a pure product -> reducible
print("  gauge octic (Sp(1)=right-H): Str_S F^8 = 128*(y^2)^4 = pure product of quadratics")
print("     -> Green-Schwarz REDUCIBLE, no independent order-8 Casimir: irreducible? %s"
      % gauge_octic_irreducible_Sp1)
local_factorizes = (grav_irr == 0) and (not gauge_octic_irreducible_Sp1)
print("  => LOCAL I_16 Green-Schwarz factorizable (this content)? %s" % local_factorizes)
print("     CONDITIONAL: net chirality != 0 for the ASSUMED truncation => grav channel blocks.")
print("     A chirally BALANCED content (n_+ = n_-) makes grav_irr = 0 -> local leg would")
print("     factorize; the truncation is the load-bearing assumption, NOT a derived fact.")

# ----------------------------------------------------------------------------------------
print()
print("#"*94)
print("# VERDICT (internal path #6, Sp(64) anomaly) -- GRADE: PARTIAL")
print("#"*94)
print("# GLOBAL LEG (advanced here, target-free, content-INDEPENDENT for the odd part):")
print("#   Omega^Spin_15(B Sp(n)) has NO ODD torsion, for EVERY n (Sp(1) commutant, Sp(64),")
print("#   general). Proof: AHSS at any odd prime -- H_*(BSp) sits in degrees div by 4 and")
print("#   Omega^Spin_*(pt) is odd-torsion-free (ABP/Wall), so the whole odd-degree E_2 line")
print("#   vanishes. Hence the GU 14D global (Dai-Freed) gauge-anomaly group is a purely")
print("#   2-PRIMARY finite group. pi_15(Sp)=Z is free/torsion-blind, so it genuinely could")
print("#   not have settled this -- CANON's warning is now precise.")
print("#   Non-vacuity: identical machinery DOES find Z/3 in Omega^Spin_15(BZ_3).")
print("# LOCAL LEG (recomputed, CONDITIONAL): gauge octic is GS-reducible under the genuine")
print("#   Sp(1) commutant; the pure-gravity tr R^8 is nonzero ONLY because the ASSUMED")
print("#   truncated content has net chirality -13. Chirally balanced -> vanishes.")
print("# WHAT THE GLOBAL LEG STILL NEEDS (the open 2-primary remainder):")
print("#   compute the 2-PRIMARY part of Omega^Spin_15(B Sp(n)) (ABP 2-local: MSpin_(2) =")
print("#   ko v ko<2> v ... v HZ/2's; ko-module differentials) AND the map the ASSUMED chiral")
print("#   content induces into it (whether the GU class is trivial there). Odd primes are")
print("#   now provably clean; the 2-primary channel -- home of Witten-type SU(2)=Sp(1) global")
print("#   anomalies -- is the decisive next step.")
print("# NO TARGET IMPORTED: primes {3,5,7}, Sp gen-degrees {4k}, bordism ranks only.")
print("# hard asserts passed: %d" % NA)
print("#"*94)
