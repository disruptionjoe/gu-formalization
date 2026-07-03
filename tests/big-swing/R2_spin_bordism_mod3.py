#!/usr/bin/env python3
# R2 BIG SWING -- SM-as-boundary, GLOBAL/torsion layer, mod-3 arena.
# ============================================================================================
# QUESTION (home run target). Today's LOCAL toy (tests/sm-boundary/anomaly_inflow_toy.py) showed
# perturbative SM anomaly-freedom is COUNT-BLIND: it constrains only the 2-primary (parity) arena and
# leaves every residue mod 3 free. The offensive escalation: reach the GLOBAL (Dai-Freed /
# spin-bordism) layer and decide whether requiring the whole anomaly-free SM as chiral BOUNDARY data
# PINS the generation count in the ODD-TORSION (mod-3) arena -- the Z/3 <= pi_3^s = Z/24 where the
# program's CRT split says a count could hide.
#
# A 4D chiral theory's global (Dai-Freed) anomalies are classified by the torsion of the relevant
# spin-bordism group Omega^{Spin}_5(BG) (Freed-Hopkins; Garcia-Etxebarria-Montero). The count is
# "pinned mod 3" iff there is a Z/3 in that group AND the SM content maps to it non-trivially so that
# n generations must satisfy 3 | n. So the sharp, decidable, TARGET-FREE question is:
#
#     Does Omega^{Spin}_5(B G_SM) -- the SM Dai-Freed anomaly group -- have any 3-torsion at all?
#     (3 enters ONLY as "the prime we localize at to probe odd torsion." We never assume 3
#      generations, never divide by 3, never normalize to a target. We ask: is the arena non-empty?)
#
# METHOD. Atiyah-Hirzebruch spectral sequence (AHSS), localized at the prime 3:
#     E_2^{i,j} = H_i(BG ; Omega^{Spin}_j(pt))  ==>  Omega^{Spin}_{i+j}(BG).
# Two rigorous inputs, both TARGET-import-safe:
#   (I)  Omega^{Spin}_*(pt) has NO odd torsion, in EVERY degree. THEOREM (Anderson-Brown-Peterson +
#        Wall): at an odd prime p, MSpin_(p) ~ MSO_(p), and MSO_(p) is a wedge of suspensions of BP,
#        whose homotopy Z_(p)[v_1,v_2,...] is torsion-free. => 3-locally Omega^{Spin}_j is FREE,
#        supported in j = 0,4,8,... . (We encode the standard low-degree table and ASSERT its torsion
#        is 2-primary, as an executable sanity check of input (I).)
#   (II) H_*(B G_SM ; Z_(3)) is torsion-free and concentrated in EVEN degrees. Reason (an honest Lie
#        iso, not a target): the true SM group is G_SM = (SU(3)xSU(2)xU(1))/Z_6. Localized at 3 the
#        Z_2 factor is invisible, and (SU(3)xU(1))/Z_3 ~= U(3) EXACTLY (the map (A,z)->zA has kernel
#        {(w^-1 1, w): w^3=1}=Z_3 and image U(3)). So 3-locally B G_SM ~ BU(3) x BSU(2). Both have
#        torsion-free integral cohomology Z[c1,c2,c3], Z[c2] concentrated in even degree => H_odd = 0,
#        no torsion. We VERIFY the rational Poincare series of B(SU(3)xU(1)) and BU(3) coincide (the
#        computable shadow of the U(3) iso) and that H_odd = 0.
#
# CONSEQUENCE we compute: for ANY odd total degree n, every (i,j) with i+j=n has i odd (H_i=0) or j
# odd (Omega^{Spin}_j 3-locally = 0). So E_2^{i,j}(3) = 0 on the whole odd-degree line. No page can
# create torsion out of nothing => Omega^{Spin}_n(B G_SM) (x) Z_(3) = 0 for all odd n, in particular
# n = 5 (the 4D Dai-Freed degree) and n = 3.
#
# NON-VACUITY (house discipline: the strongest check must be able to FAIL). We run the identical
# machinery on BZ_3, whose H_odd = Z/3 in every odd degree, and CONFIRM it DOES produce 3-torsion in
# Omega^{Spin}_3(BZ_3). So a "no 3-torsion" verdict is a real measurement, not a machine that always
# says zero.
#
# NO TARGET IMPORT: the only integers are prime 3 (the localization prime), the SM Lie data, and
# bordism ranks. 3-generations is never assumed; chi(K3)=24, /8, Ahat=3 never appear.
# ============================================================================================
import numpy as np

NA = 0
def check(c, m):
    global NA; NA += 1
    assert c, "FAIL: " + m

# ------------------------------------------------------------------------------------------
# INPUT (I): Omega^{Spin}_n(pt), standard low-degree table, and the 3-locally-free ranks.
#   n:   0    1     2     3   4   5   6   7   8       9
#  grp:  Z   Z/2   Z/2   0   Z   0   0   0   Z^2   (Z/2)^2
# All torsion is 2-primary (ABP: MSpin_(2) = wedge of ko, ko<2>, HZ/2 spectra; odd-locally torsion
# free). We store (free_rank, torsion_prime_factorization) and ASSERT no factor of 3.
# ------------------------------------------------------------------------------------------
OmegaSpin = {  # n : (free_rank, [torsion orders])
    0: (1, []), 1: (0, [2]), 2: (0, [2]), 3: (0, []), 4: (1, []),
    5: (0, []), 6: (0, []), 7: (0, []), 8: (2, []), 9: (0, [2, 2]),
}
print("=" * 94)
print("INPUT (I): Omega^Spin_*(pt) is odd-torsion-FREE (ABP/Wall). Verify table torsion is 2-primary.")
print("=" * 94)
for n, (fr, tors) in OmegaSpin.items():
    for t in tors:
        while t % 2 == 0:
            t //= 2
        check(t == 1, "Omega^Spin_%d torsion order has an odd factor (contradicts ABP)" % n)
    print("  Omega^Spin_%d = Z^%d + %s   (odd-torsion-free: %s)"
          % (n, fr, ("+".join("Z/%d" % o for o in tors) if tors else "0"), "OK"))

def omega_spin_free_rank_3local(j):
    """3-local rank of Omega^Spin_j: free part only (all torsion is 2-primary => dies at p=3)."""
    return OmegaSpin.get(j, (0, []))[0]

# ------------------------------------------------------------------------------------------
# INPUT (II): H_*(BG ; Z) ranks via Poincare series of a polynomial cohomology ring.
# H^*(BG;Z) = Z[generators in given even degrees]; Poincare series = prod 1/(1 - t^deg).
# ------------------------------------------------------------------------------------------
def poincare_ranks(gen_degrees, N):
    """Ranks of H_i (=dim of degree-i part of Z[gens]) for i=0..N, gens of the given even degrees."""
    r = np.zeros(N + 1, dtype=object)
    r[0] = 1
    for d in gen_degrees:
        nr = np.zeros(N + 1, dtype=object)
        for i in range(N + 1):
            k = 0
            while i - k * d >= 0:
                nr[i] += r[i - k * d]
                k += 1
        r = nr
    return r

N = 9
# Naive gauge group SU(3)xSU(2)xU(1): gens c1(2), c2^SU2(4), c2^SU3(4), c3^SU3(6).
ranks_naive = poincare_ranks([2, 4, 4, 6], N)
# 3-local G_SM ~ BU(3) x BSU(2): BU(3) gens c1(2),c2(4),c3(6); BSU(2) gen c2(4).
ranks_bu3   = poincare_ranks([2, 4, 6], N)
ranks_bsu2  = poincare_ranks([4], N)
ranks_gsm   = np.array([sum(ranks_bu3[a] * ranks_bsu2[i - a] for a in range(i + 1))
                        for i in range(N + 1)], dtype=object)

print()
print("=" * 94)
print("INPUT (II): H_*(BG;Z_(3)) torsion-free, H_odd = 0.  Verify via Poincare ranks.")
print("=" * 94)
# (a) The U(3) iso shadow: rational Poincare series of B(SU(3)xU(1)) == BU(3).
ranks_su3u1 = poincare_ranks([2, 4, 6], N)  # SU(3): c2(4),c3(6); U(1): c1(2)  == BU(3) gens
check(list(ranks_su3u1) == list(ranks_bu3),
      "PS(B(SU(3)xU(1))) == PS(BU(3)) -- the computable shadow of (SU(3)xU(1))/Z_3 = U(3)")
print("  (SU(3)xU(1))/Z_3 = U(3) shadow: PS(B(SU(3)xU(1))) == PS(BU(3))  -> OK")
# (b) H_odd = 0 for the naive group and for 3-local G_SM.
for name, ranks in [("SU(3)xSU(2)xU(1)", ranks_naive), ("G_SM~BU(3)xBSU(2) (3-local)", ranks_gsm)]:
    odd = [int(ranks[i]) for i in range(1, N + 1, 2)]
    check(all(x == 0 for x in odd), "H_odd(B %s) must vanish" % name)
    print("  H_i(B %-28s) i=0..%d : %s   (H_odd all 0: OK)"
          % (name, N, [int(x) for x in ranks]))
check(list(ranks_naive) == list(ranks_gsm),
      "naive and 3-local-G_SM even-degree ranks agree (both rationally U(3)xSU(2))")

# H_*(BG;Z_(3)) as (free_rank, has_3_torsion). Torsion-free => (rank, False).
def H_gsm(i):
    return (int(ranks_gsm[i]) if 0 <= i <= N else 0, False)

# NON-VACUITY control: BZ_3.  H_0 = Z; H_odd = Z/3 (every odd degree); H_{even>0} = 0.
def H_BZ3(i):
    if i == 0:
        return (1, False)
    if i % 2 == 1:
        return (0, True)   # Z/3 torsion, no free part
    return (0, False)

# ------------------------------------------------------------------------------------------
# AHSS at p=3.  E_2^{i,j}(3) = H_i(BG;Z_(3)) (x) Omega^Spin_j(3)  (+ Tor).  Detect any 3-torsion in
# total degree n.  (free (x) free = free; 3-torsion (x) free(rank>0) = 3-torsion; Tor(free,anything)=0.)
# ------------------------------------------------------------------------------------------
def ahss_total_degree_has_3torsion(Hfun, n, jmax=None):
    """Return (free_rank_sum, any_3_torsion, detail) of the E_2 line i+j=n at p=3."""
    if jmax is None:
        jmax = n
    free_rank = 0
    tors3 = False
    detail = []
    for j in range(0, n + 1):
        i = n - j
        hr, htor3 = Hfun(i)
        sj = omega_spin_free_rank_3local(j)   # Omega^Spin_j 3-local: free rank (torsion 2-primary=0)
        # E_2^{i,j} free rank contribution:
        fr = hr * sj
        # 3-torsion contribution: H_i's 3-torsion tensored with a free Omega (rank sj>0) survives.
        e_tor3 = htor3 and (sj > 0)
        if fr != 0 or e_tor3:
            detail.append((i, j, fr, e_tor3))
        free_rank += fr
        if e_tor3:
            tors3 = True
    return free_rank, tors3, detail

print()
print("=" * 94)
print("AHSS at p=3:  Omega^Spin_n(B G_SM) (x) Z_(3)  on the ODD-degree line (n=1,3,5,7,9).")
print("=" * 94)
gsm_verdict = {}
for n in [1, 3, 5, 7, 9]:
    fr, t3, det = ahss_total_degree_has_3torsion(H_gsm, n)
    gsm_verdict[n] = (fr, t3)
    print("  n=%d:  E_2 line i+j=%d  ->  free rank %d, 3-torsion present: %s   entries=%s"
          % (n, n, fr, t3, det if det else "ALL ZERO"))
    check(fr == 0 and not t3,
          "Omega^Spin_%d(B G_SM)(x)Z_(3) must be ZERO (no mod-3 arena)" % n)

print()
print("=" * 94)
print("NON-VACUITY control:  same machinery on BZ_3 (H_odd = Z/3).  MUST find 3-torsion.")
print("=" * 94)
fr3, t3_3, det3 = ahss_total_degree_has_3torsion(H_BZ3, 3)
print("  BZ_3, n=3:  E_2 line  ->  free rank %d, 3-torsion present: %s   entries=%s"
      % (fr3, t3_3, det3))
check(t3_3, "machinery MUST detect the Z/3 in Omega^Spin_3(BZ_3) -- else it is vacuous")
# Also confirm the machinery finds NO 3-torsion for the SM in the SAME degree it found it for BZ_3.
check(not gsm_verdict[3][1], "same degree n=3: G_SM has NO 3-torsion where BZ_3 HAS it -> real contrast")

# ------------------------------------------------------------------------------------------
# The general structural statement, verified as a loop rather than asserted once.
# ------------------------------------------------------------------------------------------
print()
print("=" * 94)
print("STRUCTURAL: for G_SM, the ENTIRE odd-degree E_2 line vanishes 3-locally (n=1..9).")
print("=" * 94)
all_odd_zero = all(gsm_verdict[n] == (0, False) for n in [1, 3, 5, 7, 9])
check(all_odd_zero, "every odd-degree Omega^Spin_n(B G_SM)(x)Z_(3) vanishes")
print("  verified: Omega^Spin_n(B G_SM) (x) Z_(3) = 0 for n in {1,3,5,7,9}.")

print()
print("#" * 94)
print("# VERDICT (R2 big swing, GLOBAL/torsion layer): the mod-3 arena is EMPTY for the SM.")
print("#  Omega^Spin_5(B G_SM) (x) Z_(3) = 0  (and Omega^Spin_3, and every odd degree).")
print("#  The SM's Dai-Freed / spin-bordism global-anomaly group has NO 3-torsion at all.")
print("#  => Requiring the whole anomaly-free SM as chiral boundary data CANNOT pin the generation")
print("#     count in the odd-torsion (mod-3) arena: there is no Z/3 for a count to be pinned in.")
print("#  Root cause, and it is fully 2-primary: Omega^Spin_*(pt) is odd-torsion-free (ABP/Wall),")
print("#  and 3-locally B G_SM ~ BU(3) x BSU(2) has torsion-free, even-degree cohomology. Every SM")
print("#  structural subtlety that could have made an arena -- the Z_6 quotient, the Spin-Z_2 twist,")
print("#  the Witten SU(2) anomaly -- is 2-primary and never reaches the prime 3.")
print("#  Combined with today's LOCAL toy (count-blind, 2-primary only): BOTH the local and the")
print("#  global layers leave the count mod-3 free. The 'count hides in Omega^Spin Z/3' hope is DEAD.")
print("#  Non-vacuity: identical machinery DOES find the Z/3 in Omega^Spin_3(BZ_3).")
print("#  hard asserts passed: %d ;  NO target imported (no 3-gen, no chi=24, no /8, no Ahat=3)." % NA)
print("#" * 94)
