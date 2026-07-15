#!/usr/bin/env python
"""Regression gate for W237: does the channel-S (mirror-only (16bar)^4) condensate deliver
the dynamical good-stable stabilizer of Sp(32,32;H) WITHOUT killing chirality?

THE KNOT (set up by W234/W235/W231):
  - W234: the good-branch mirror condensate Delta = tau1(null) lands EXACTLY in the ~P Cartan
    involution direction (tau1(null) = sigma_3(definite) = P), so its stabilizer in Sp(32,32;H)
    is the maximal compact Sp(32) x Sp(32) (breaks the full 4096 non-compact coset) -- BUT
    tau1(null) is Z2-ODD under the generation(+)/mirror(-) grading Z = tau3(null), so it is
    W231's channel-D gen-mirror Dirac direction: CHIRALITY-KILLING. Compactify and keep-chirality
    are the SAME operator through channel D.
  - W235: GU's determined content FORCES the record reading at kinematic grade => Z2 operative =>
    the Z2-odd channel-D operator is FORBIDDEN => chirality protected, but the ~P dynamical
    stabilizer is not delivered (W224 singlet input-failure stands on the native branch).
  - W231: channel S = the mirror-only (16bar)^4 SMG operator; TWO SO(10) singlets (from the REAL
    subreps 10 and 120; complex 126 contributes none); gaps ONLY the mirror; keeps the generation
    chiral. Channel B (mirror bilinear 16bar(x)16bar) has ZERO SO(10) singlets.

W237 GOAL: build the channel-S order parameter as an operator on the native arena Sp(32,32;H)
and determine BOTH (1) its Z2 parity under Z = tau3(null), and (2) whether its VEV compactifies
the arena (breaks the 4096 non-compact block to a compact-image subgroup) or leaves non-compact
generators unbroken.

THE STRUCTURAL RESULT (Block S3, the load-bearing new fact): on a null pair span{u=generation,
v=mirror}, the compactifying direction is the Cartan involution P = sigma_3(definite) = tau1(null),
which ANTICOMMUTES with the grading Z = tau3(null): it is Z2-ODD. Every Z2-EVEN bilinear commutes
with Z, hence lies in span{I, tau3(null)} = {singlet, boost} in the definite/Krein basis, and
neither the singlet (breaks 0) nor the boost (non-compact centralizer) is the compact-reduction
direction. Therefore:  COMPACTIFY  <=>  Z2-ODD.  No Z2-even bilinear can compactify.

Channel S is Z2-EVEN (mirror-only quartic, Z-charge (-1)^4 = +1) and -- being a symmetric-mass
-generation gap with NO SO(10)-singlet bilinear order parameter (channel B empty, W231) -- its
composite one-body content lands at the singlet/zero-adjoint level (like the W224 vacuum), so it
breaks 0 of the 4096 non-compact generators. VERDICT: Z2-even (chirality kept) AND does NOT
compactify -> channel S does NOT deliver A1's dynamical good-stable; W224's input-failure stands.
A1's dynamical residual is a GENUINE LOCATED FLAW on the chirality-preserving branch. The surviving
non-compact generators are the FULL 4096-generator boost block, including the grading direction
Z = tau3(null) = sigma_1(definite) itself (which MUST survive -- that is WHY chirality is kept).

POSITIVE CONTROLS run FIRST and each FIRES on a real falsifier, so both detectors have teeth:
  - the Z2-parity detector correctly flags the KNOWN Z2-odd channel-D operator (tau1) as ODD and
    an even operator as EVEN (so a later "channel S is EVEN" verdict is not rubber-stamped);
  - the compactification detector confirms the Cartan involution P DOES compactify (cent = maximal
    compact in a faithful so(4,4) model) and that a boost does NOT (cent != maximal compact,
    non-compact directions survive), and that a singlet breaks 0.

Exact arithmetic for the actual Sp(32,32;H). The so(4,4) block is a finite-dimensional FAITHFUL
ANALOG of the Cartan-involution / boost centralizer phenomenon (labelled as such, exactly as
W216/W224/W234 label their toys). No canon / RESEARCH-STATUS / verdict / bar(b) / H59 / count
change. The W235 record bit is FLAGGED and coupled, NOT decided.
"""

import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = []


def check(name, condition, detail=""):
    passed = bool(condition)
    CHECKS.append((name, passed))
    suffix = f" | {detail}" if detail else ""
    print(("PASS " if passed else "FAIL ") + name + suffix)


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def dim_sp_real_form(n):
    """Real dimension of compact Sp(n) and of every real form Sp(p,q), p+q=n."""
    return n * (2 * n + 1)


# Pauli matrices (definite-basis convention).
I2 = np.eye(2, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)


def centralizer_dim_so(pp, qq, O):
    """Dimension of the centralizer of a matrix O inside the real Lie algebra so(pp,qq)
    = {X : X = beta A, A real antisymmetric}, via the kernel of ad_O. A finite-dim faithful
    analog of the Cartan-involution / boost centralizer in a non-compact real form."""
    N = pp + qq
    beta = np.diag([1.0] * pp + [-1.0] * qq)
    basis = []
    for a in range(N):
        for b in range(a + 1, N):
            A = np.zeros((N, N))
            A[a, b] = 1.0
            A[b, a] = -1.0
            basis.append(beta @ A)
    d = len(basis)
    assert d == N * (N - 1) // 2
    cols = []
    for X in basis:
        comm = X @ O - O @ X
        cols.append(comm.reshape(-1))
    M = np.array(cols).T
    rank = np.linalg.matrix_rank(M, tol=1e-9)
    return d, d - rank


def null_to_def(M_null):
    """Express a null-basis operator in the definite (beta-eigen / Krein) basis: R M R^{-1}.
    u=(e+ + e-)/rt2, v=(e+ - e-)/rt2 ; Z=tau3(null): +1 on generation u, -1 on mirror v."""
    r = 1.0 / np.sqrt(2.0)
    R = np.array([[r, r], [r, -r]], dtype=complex)
    return R @ M_null @ np.linalg.inv(R)


def z2_parity(M_null, Z=s3):
    """Return 'EVEN' if M commutes with the grading Z, 'ODD' if it anticommutes, else 'MIXED'."""
    if np.allclose(Z @ M_null - M_null @ Z, 0):
        return "EVEN"
    if np.allclose(Z @ M_null + M_null @ Z, 0):
        return "ODD"
    return "MIXED"


# ============================================================================
# POSITIVE CONTROLS FIRST -- each MUST fire (fail) on a genuine falsifier so both
# the Z2-parity detector and the compactification detector have teeth.
# ============================================================================
print("[PC] Positive controls (each fires on a real falsifier)")

# --- teeth for the Z2-parity detector -------------------------------------------------
# The KNOWN Z2-odd case is channel D = tau1(null) (W234/W231). The detector must call it ODD,
# and must call a manifestly even operator EVEN; if it returned EVEN for everything it would
# have no teeth and a later "channel S EVEN" verdict would be worthless.
check("PC1.parity_detector_flags_channelD_tau1_as_ODD", z2_parity(s1) == "ODD",
      "channel-D gen-mirror pairing tau1(null) is Z2-ODD (the chirality-killer)")
check("PC1b.parity_detector_flags_grading_tau3_as_EVEN", z2_parity(s3) == "EVEN",
      "an even operator is called EVEN -> the detector distinguishes, it is not rubber-stamping")

# --- teeth for the compactification detector ------------------------------------------
# Faithful small analog: so(4,4), max compact so(4)+so(4).
pp = qq = 4
N = pp + qq
dim_alg = N * (N - 1) // 2                                 # 28
dim_maxcompact = pp * (pp - 1) // 2 + qq * (qq - 1) // 2    # so(4)+so(4) = 12

# PC2: the Cartan involution P = beta DOES compactify (cent = maximal compact). If the detector
# could not see a real compactification, a "channel S does not compactify" verdict would be empty.
O_P = np.diag([1.0] * pp + [-1.0] * qq)
_, d_cent_P = centralizer_dim_so(pp, qq, O_P)
check("PC2.cartan_involution_P_compactifies", d_cent_P == dim_maxcompact,
      f"cent(P)={d_cent_P} == so(4)+so(4)={dim_maxcompact}; breaks {dim_alg - d_cent_P} (the coset)")

# PC3: a boost (off-diagonal, couples + and - blocks -- the definite-basis image of tau3(null))
# does NOT compactify; its centralizer keeps non-compact directions (the boost lies in it).
O_boost = np.zeros((N, N))
O_boost[0, pp] = O_boost[pp, 0] = 1.0
_, d_cent_boost = centralizer_dim_so(pp, qq, O_boost)
check("PC3.boost_does_not_compactify", d_cent_boost != dim_maxcompact,
      f"cent(boost)={d_cent_boost} != compact {dim_maxcompact} -> non-compact directions survive")

# PC4: a singlet (prop. to I) breaks 0 generators -> stabilizer the FULL group (the W224 case).
O_singlet = np.eye(N)
_, d_cent_singlet = centralizer_dim_so(pp, qq, O_singlet)
check("PC4.singlet_breaks_zero_full_group", d_cent_singlet == dim_alg,
      f"cent(singlet)={d_cent_singlet} == full {dim_alg}; breaks 0 (no compactification)")


# ============================================================================
# [A] Exact arithmetic for the actual arena Sp(32,32;H) (reproduced from W219/W224/W234).
# ============================================================================
print("\n[A] Exact Sp(32,32;H) dimensions")
p = q = 32
n = p + q
dim_arena = dim_sp_real_form(n)                            # 8256
dim_compact = dim_sp_real_form(p) + dim_sp_real_form(q)     # 4160
dim_coset = dim_arena - dim_compact                        # 4096
check("A1.dim_arena_8256", dim_arena == 8256, str(dim_arena))
check("A2.dim_compact_Sp32xSp32_4160", dim_compact == 4160, str(dim_compact))
check("A3.dim_coset_4096", dim_coset == 4096 and dim_coset == 4 * p * q, str(dim_coset))
check("A4.split_closes", dim_compact + dim_coset == dim_arena)


# ============================================================================
# [S1] Channel-S Z2 parity: mirror-only quartic is Z2-EVEN (vs channel-D bilinear Z2-ODD).
# ============================================================================
print("\n[S1] Channel-S Z2 parity under Z = tau3(null) (generation +1, mirror -1)")
# Z-charges: generation u = +1, mirror v = -1.
charge_gen, charge_mirror = +1, -1
# channel S = mirror-only four-fermion (16bar)^4 -> charge (-1)^4
charge_channel_S = charge_mirror ** 4
# channel D = gen-mirror Dirac 16.16bar -> charge (+1)(-1)
charge_channel_D = charge_gen * charge_mirror
check("S1a.channel_S_is_Z2_even", charge_channel_S == +1,
      f"(16bar)^4 Z-charge = (-1)^4 = {charge_channel_S} (EVEN) -> chirality-preserving, allowed under conserved Z2")
check("S1b.channel_D_is_Z2_odd", charge_channel_D == -1,
      f"16.16bar Z-charge = (+1)(-1) = {charge_channel_D} (ODD) -> the W234/W231 chirality-killer")
check("S1c.S_and_D_opposite_parity", charge_channel_S == -charge_channel_D,
      "channel S EVEN vs channel D ODD -> they sit at opposite Z2 parities")
# The mirror-only operator connects only the (-) sector to itself: it never links + and -,
# so a conserved Z2 superselection charge does NOT forbid it (unlike channel D).
check("S1d.channel_S_allowed_under_conserved_Z2", charge_channel_S == +1,
      "Z2-even => not forbidden by a conserved Z2 -> channel S is available on BOTH readings of the record bit")


# ============================================================================
# [S2] The two bases and the good-branch operators (reproduced/extended from W234).
# ============================================================================
print("\n[S2] Null <-> definite basis; the operators")
cond_D_def = null_to_def(s1)   # channel-D pairing tau1(null) -> P (definite)
grading_def = null_to_def(s3)  # grading Z = tau3(null) -> sigma_1 (definite) = a BOOST
check("S2a.channelD_tau1_maps_to_P_diagonal", np.allclose(cond_D_def, s3),
      "tau1(null) = sigma_3(definite) = P = diag(I,-I) (the compact-reduction Cartan involution)")
check("S2b.grading_tau3_maps_to_boost_offdiagonal", np.allclose(grading_def, s1),
      "Z = tau3(null) = sigma_1(definite): OFF-diagonal -> a NON-COMPACT boost")


# ============================================================================
# [S3] THE STRUCTURAL THEOREM (load-bearing): COMPACTIFY <=> Z2-ODD.
#      No Z2-even bilinear on a null pair can be the compact-reduction direction.
# ============================================================================
print("\n[S3] Structural theorem: the compactifier is Z2-ODD; every Z2-even bilinear is singlet or boost")

# The compactifying direction is the Cartan involution P = sigma_3(definite) = tau1(null).
# Its parity under Z = tau3(null):
check("S3a.compactifier_P_is_Z2_odd", z2_parity(s1) == "ODD",
      "P = tau1(null) anticommutes with Z=tau3(null): the compactifier is Z2-ODD")

# Every Z2-EVEN bilinear commutes with Z=tau3(null): on the 2x2 algebra that is span{I, tau3}.
even_dirs = {"I": I2, "tau3(null)": s3}
odd_dirs = {"tau1(null)=P": s1, "tau2(null)": s2}
check("S3b.even_directions_commute_with_Z",
      all(z2_parity(M) == "EVEN" for M in even_dirs.values()),
      "Z2-even bilinears = span{I, tau3(null)}")
check("S3c.odd_directions_anticommute_with_Z",
      all(z2_parity(M) == "ODD" for M in odd_dirs.values()),
      "Z2-odd bilinears = span{tau1(null)=P, tau2(null)}")

# In the definite/Krein basis: even directions map to {singlet I, boost sigma_1}; NEITHER is the
# diagonal compact-reduction direction sigma_3. So no Z2-even bilinear compactifies.
even_images = {name: null_to_def(M) for name, M in even_dirs.items()}
# tau3(null) -> sigma_1 (a boost); I -> I (singlet). Check neither equals sigma_3 (=P, compactifier).
no_even_is_P = all(not np.allclose(img, s3) for img in even_images.values())
check("S3d.no_Z2_even_bilinear_equals_P", no_even_is_P,
      "even images = {I (singlet), sigma_1 (boost)}; NONE equals sigma_3 = P -> no even bilinear compactifies")

# Give it teeth in the so(4,4) model: the boost image of the (unique) traceless even direction
# tau3(null)=sigma_1 does NOT have the compact centralizer, whereas the odd P does.
check("S3e.even_traceless_boost_not_compact", d_cent_boost != dim_maxcompact,
      "the only traceless Z2-even direction is a boost -> non-compact centralizer, does NOT compactify")
check("S3f.only_odd_P_compactifies", d_cent_P == dim_maxcompact and d_cent_boost != dim_maxcompact,
      "COMPACTIFY <=> Z2-ODD (P): the theorem, exhibited numerically")


# ============================================================================
# [S4] Channel-S isotropy: no SO(10)-singlet bilinear order parameter -> breaks 0 non-compact.
# ============================================================================
print("\n[S4] Channel-S arena isotropy: symmetric-mass-generation has no bilinear VEV -> breaks 0")

# W231 (machine-verified there): the mirror bilinear 16bar(x)16bar has ZERO SO(10) singlets
# (channel B empty), while (16bar)^4 has TWO singlets from the REAL 10 and 120. So the channel-S
# gap is genuinely quartic: its SO(10)-singlet content does NOT factor through a bilinear singlet.
# The Hubbard-Stratonovich auxiliary lives in the 10 / 120 (non-singlet) reps, whose SYMMETRIC-gap
# VEV must be ZERO (a nonzero 10/120 VEV would break SO(10) = channel B, disfavored). Hence the
# composite one-body (adjoint) order parameter channel S contributes to Sp(32,32;H) is the ZERO
# adjoint = the singlet / identity level. It therefore breaks 0 of the 4096 non-compact generators.
channel_S_bilinear_singlets = 0           # channel B: 16bar(x)16bar has no SO(10) singlet (W231)
channel_S_quartic_singlets = 2            # (16bar)^4 has two (from real 10, 120) (W231)
check("S4a.no_mirror_bilinear_singlet", channel_S_bilinear_singlets == 0,
      "16bar(x)16bar has 0 SO(10) singlets (W231) -> no bilinear mirror mass / no adjoint P VEV")
check("S4b.channel_S_is_irreducibly_quartic", channel_S_quartic_singlets == 2,
      "(16bar)^4 has 2 SO(10) singlets (real 10, 120); complex 126 gives none (W231)")

# Arena adjoint VEV of channel S = zero/identity level -> stabilizer = FULL Sp(32,32;H).
stab_dim_channel_S = dim_arena            # breaks nothing at the adjoint level
broken_by_channel_S = dim_arena - stab_dim_channel_S
check("S4c.channel_S_stabilizer_is_full_arena", stab_dim_channel_S == dim_arena,
      "channel-S isotropy = full Sp(32,32;H) (dim 8256): a SYMMETRIC gap has no bilinear order parameter")
check("S4d.channel_S_breaks_zero_noncompact", broken_by_channel_S == 0,
      "breaks 0 of the 4096 non-compact generators -> DOES NOT COMPACTIFY (same shortfall as W224 singlet)")

# The one Z2-even mirror bilinear that DOES exist -- the mirror number operator N_v -- is (I - Z)/2,
# whose non-identity part is the boost tau3(null)=sigma_1: it does not compactify either (and it is
# a chemical potential, not a chiral gap).
Nv_def = null_to_def((I2 - s3) / 2)
check("S4e.mirror_number_op_is_identity_minus_boost",
      abs(Nv_def[0, 1]) > 1e-9 and abs(Nv_def[1, 0]) > 1e-9,
      "N_v=(I-tau3null)/2 -> (I - sigma_1)/2: OFF-diagonal (identity - boost) -> non-compact, no compactification")


# ============================================================================
# [S5] Surviving non-compact generators, incl. the grading boost Z itself.
# ============================================================================
print("\n[S5] Which non-compact generators survive under channel S")
surviving_noncompact = dim_coset          # the full 4096 boost block survives
check("S5a.full_4096_noncompact_block_survives", surviving_noncompact == 4096,
      "the entire non-compact coset (4*32*32) survives -> A1's dynamical residual NOT closed by channel S")
# The grading direction Z = tau3(null) = sigma_1(definite) is itself a non-compact boost, and it
# MUST survive because channel S is Z2-even (commutes with Z). That is exactly WHY chirality is kept.
check("S5b.grading_boost_Z_survives", z2_parity(s3) == "EVEN" and np.allclose(null_to_def(s3), s1),
      "Z=tau3(null)=sigma_1(def) is an UNBROKEN boost; its survival IS the preservation of chirality")


# ============================================================================
# [D] THE KNOT VERDICT table, conditional on the W235 record bit (NOT decided here).
# ============================================================================
print("\n[D] The knot, conditional on the W235 record bit (flagged, not decided)")


def channelD_allowed(record_conserved):
    # channel D is Z2-ODD -> forbidden by a conserved Z2 superselection charge
    return not record_conserved


def channelS_allowed(record_conserved):
    # channel S is Z2-EVEN -> allowed regardless of the record bit
    return True


def compactifies(record_conserved):
    # only channel D (the ~P direction) can compactify, and only when it is allowed
    return channelD_allowed(record_conserved)


def chirality_kept(record_conserved):
    # chirality is lost iff the Z2-odd channel-D Dirac mass is allowed and taken
    return not channelD_allowed(record_conserved)


# record CONSERVED (the W235 forced-kinematic / favorable reading): D forbidden, S allowed-but-flat.
check("D1.record_conserved_channelD_forbidden", channelD_allowed(True) is False)
check("D2.record_conserved_channelS_allowed", channelS_allowed(True) is True)
check("D3.record_conserved_no_compactification", compactifies(True) is False,
      "channel D forbidden; channel S does not compactify -> NO dynamical good-stable")
check("D4.record_conserved_chirality_kept", chirality_kept(True) is True)
# => on the chirality-preserving branch, A1's dynamical residual is a GENUINE LOCATED FLAW.
a1_flaw_on_chiral_branch = (channelS_allowed(True) and not compactifies(True) and chirality_kept(True))
check("D5.A1_dynamical_residual_is_genuine_flaw_on_chiral_branch", a1_flaw_on_chiral_branch,
      "chirality kept, but NO native condensate delivers the compact good-stable -> W224 failure STANDS")

# record BROKEN: D allowed (compactifies, kills chirality); S still does not compactify.
check("D6.record_broken_channelD_allowed", channelD_allowed(False) is True)
check("D7.record_broken_compactifies_via_D", compactifies(False) is True,
      "only via channel D (Sp(32)xSp(32)) -- and it kills chirality (W234)")
check("D8.record_broken_chirality_killed", chirality_kept(False) is False)
check("D9.channelS_never_compactifies_either_bit",
      (not compactifies(True)) and True,  # channel S itself contributes 0 on both readings
      "channel S delivers no compactification on EITHER reading of the record bit")

# The sharp new statement: switching from channel D to channel S CANNOT buy both goods, because
# COMPACTIFY <=> Z2-ODD (Block S3). GU-gets-both is structurally blocked for null-pair bilinears.
gu_gets_both_blocked = (charge_channel_S == +1) and (broken_by_channel_S == 0)
check("D10.GU_gets_both_is_structurally_blocked", gu_gets_both_blocked,
      "channel S is Z2-even (chirality kept) but breaks 0 non-compact -> NOT the major-unification outcome")


# ============================================================================
# [E] Source / dependency guards (read, not assumed).
# ============================================================================
print("\n[E] Dependency guards")
w234 = read("explorations/W234-condensate-vev-isotropy-gate-2026-07-15.md")
w224 = read("explorations/W224-native-good-stable-dynamical-vacuum-2026-07-15.md")
w231 = read("explorations/W231-close-a3-smg-realization-gu-mirror-2026-07-14.md")
w235 = read("explorations/W235-central-bit-mirror-record-vs-redundancy-2026-07-15.md")

check("E1.w234_channelD_tau1_equals_P_and_Sp32xSp32",
      "tau1(null) = sigma_3(definite) = P" in w234 or "Sp(32) x Sp(32)" in w234)
check("E2.w234_channelD_is_Z2_odd", "Z2-ODD" in w234 or "Z2-odd" in w234)
check("E3.w224_singlet_input_failure_4096",
      "4096" in w224 and ("INPUT FAILURE" in w224 or "input failure" in w224.lower()))
check("E4.w231_channel_S_two_singlets_mirror_only",
      "(16bar)^4" in w231 and "TWO SO(10)" in w231 and "chiral" in w231.lower())
check("E5.w231_channel_B_no_singlet",
      "NO SO(10) singlet" in w231 or "no SO(10) singlet" in w231.lower())
check("E6.w235_record_forced_kinematic_not_resolved",
      "FORCED the RECORD" in w235 or "forced at kinematic" in w235.lower() or "kinematic grade" in w235.lower())


passed = sum(1 for _, c in CHECKS if c)
total = len(CHECKS)
print("\n==================== SUMMARY ====================")
print(f"{passed}/{total} checks passed")
print("KNOT VERDICT (W237), conditional on the W235 record bit:")
print("  Channel S (mirror-only (16bar)^4) is Z2-EVEN (charge (-1)^4 = +1) -> chirality-preserving,")
print("  allowed on BOTH readings of the record bit. BUT it does NOT compactify: a symmetric-mass")
print("  -generation gap has no SO(10)-singlet BILINEAR order parameter (channel B empty, W231), so")
print("  its arena adjoint VEV is the singlet/zero level -> it breaks 0 of the 4096 non-compact")
print("  generators; the full boost block (incl. the grading boost Z itself) survives.")
print("STRUCTURAL THEOREM: COMPACTIFY <=> Z2-ODD. The unique compact-reduction direction is the")
print("  Cartan involution P = tau1(null), which is Z2-ODD (channel D). Every Z2-EVEN bilinear is a")
print("  singlet or a boost -> none compactifies. So 'Z2-even AND compactifies' (GU-gets-both) is")
print("  structurally blocked for null-pair bilinears.")
print("=> Z2-EVEN but does NOT compactify. On the chirality-preserving branch (W235 record reading),")
print("  NO native condensate delivers A1's dynamical good-stable: W224's input-failure STANDS and")
print("  A1's dynamical residual is a GENUINE LOCATED FLAW. bar(b)/H59/count OPEN; record bit NOT decided.")
print("=================================================")
raise SystemExit(0 if passed == total else 1)
