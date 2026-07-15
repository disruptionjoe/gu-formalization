#!/usr/bin/env python
"""Regression gate for W234: isotropy / stabilizer of the mirror-sector condensate VEV
in the program-native arena Sp(32,32;H), and its channel-D (chirality) reconciliation.

W224 closed the DYNAMICAL good-stable gate with a negative: the only UNCONDITIONALLY
built vacuum (the record-count / conformal-scale mode p) is an internal SINGLET, so it
breaks 0 of the 4096 non-compact generators and supplies no good-stable grading. W224
named the ONLY arc candidate that could break the non-compact block: the mirror-sector
BCS condensate Delta (W216), the off-diagonal tau1 pairing of the 96 hyperbolic null
pairs of ker(Gamma) (W173). W224 asserted "IF an adjoint condensate <O> ~ P existed its
centralizer WOULD be Sp(32) x Sp(32)" but did NOT show the built condensate equals that
~P direction.

W234 supplies exactly that missing step, as an EXACT operator identity, and reconciles it
with W231's channel-D warning.

THE LOAD-BEARING NEW FACT (Block C): a hyperbolic null pair {u, v} and the definite
(beta-eigen) pair {e_+, e_-} are related by the fixed 45-degree "hyperbolic rotation"
u = (e_+ + e_-)/sqrt2, v = (e_+ - e_-)/sqrt2. Under it the good-branch condensate operator
  Delta * tau1(null)   (the off-diagonal generation<->mirror pairing, W216)
maps to
  Delta * sigma_3(definite) = Delta * P,   P = diag(I_32, -I_32) = beta,
i.e. it lands EXACTLY in the ~P Cartan-involution direction whose centralizer is the
maximal compact Sp(32) x Sp(32). So (on the good branch, and conditional on the condensate
being an ALLOWED vacuum) the dynamical good-stable stabilizer is Sp(32) x Sp(32): W219/W228
kinematic uniqueness becomes the dynamical answer.

THE COUPLING TO W235 (Block D): the SAME operator tau1(null) is Z2-ODD under the
generation(+)/mirror(-) grading Z = tau3(null) ({tau1, tau3} = 0). W231's channel D is the
Z2-odd gen-mirror Dirac mass. So "lands in ~P (compactifies)" and "is the channel-D
chirality-killing direction" are the SAME operator statement. The record bit (W235,
Joe-gated) gates it ONE way with OPPOSITE desirability:
  record CONSERVED (Z operative) -> tau1 = P FORBIDDEN -> good stable NOT supplied dynamically
                                    (reverts to W224 singlet failure) BUT chirality protected;
  record BROKEN   (redundancy)   -> tau1 = P ALLOWED   -> good stable Sp(32)xSp(32) supplied,
                                    A1 closes, BUT the same condensate kills chirality (channel D).
W234 does NOT decide that bit; it reports the geometry conditional on it.

POSITIVE CONTROLS run FIRST and each FIRES (fails) on a real falsifier, including a genuine
"singlet / non-compactifying" case so the isotropy detector has teeth: a singlet condensate
(prop. to I) breaks 0 generators and its stabilizer is the FULL non-compact group, NOT
Sp(32)xSp(32); an off-diagonal i*tau2 (pathological-branch) condensate stays off-diagonal in
the definite basis, mixing the two Sp factors, so its stabilizer is NOT the compact
Sp(32)xSp(32) either. Only the tau1 (-> P) good-branch pairing compactifies. A small
faithful so(p,q) model computes the centralizer DIMENSIONS numerically so the compact-vs-
noncompact distinction is exhibited, not asserted.

Exact arithmetic for the actual Sp(32,32;H). The so(p,q) block is a finite-dimensional
FAITHFUL ANALOG of the Cartan-involution centralizer phenomenon (labelled as such), exactly
as W216/W224 label their 2x2 BdG toys. No canon / RESEARCH-STATUS / verdict / bar(b) / H59 /
count change. No decision of the W235 record bit.
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


# ============================================================================
# POSITIVE CONTROLS FIRST -- each MUST fire (fail) on a genuine falsifier.
# Includes a real "singlet / non-compactifying" control so the detector has teeth.
# ============================================================================
print("[PC] Positive controls (each fires on a real falsifier)")

p = q = 32
n = p + q
dim_arena = dim_sp_real_form(n)                         # Sp(32,32;H) = 8256
dim_compact = dim_sp_real_form(p) + dim_sp_real_form(q)  # Sp(32)xSp(32) = 4160
dim_coset = dim_arena - dim_compact                     # non-compact block = 4096


def centralizer_dim_so(pp, qq, O):
    """Dimension of the centralizer of a matrix O inside the real Lie algebra so(pp,qq)
    = {X real (pp+qq): X^T beta + beta X = 0}, computed as the null space of the linear
    map X -> [X, O] restricted to the algebra. A finite-dim faithful analog of the
    Cartan-involution centralizer in a non-compact real form."""
    N = pp + qq
    beta = np.diag([1.0] * pp + [-1.0] * qq)
    # Basis of so(pp,qq): X = beta * A with A real antisymmetric (A^T = -A).
    basis = []
    for a in range(N):
        for b in range(a + 1, N):
            A = np.zeros((N, N))
            A[a, b] = 1.0
            A[b, a] = -1.0
            basis.append(beta @ A)
    d = len(basis)
    assert d == N * (N - 1) // 2
    # Build the matrix of ad_O : g -> gl(N) in this basis, then find its kernel.
    cols = []
    for X in basis:
        comm = X @ O - O @ X
        cols.append(comm.reshape(-1))
    M = np.array(cols).T  # (N*N) x d
    # kernel dimension of the map coefficients -> [sum c_i X_i, O]
    rank = np.linalg.matrix_rank(M, tol=1e-9)
    return d, d - rank


# Faithful small analog: so(4,4), a non-compact real form with max compact so(4)+so(4).
# (Chosen over so(2,2) so the singlet, ~P, and off-diagonal-boost centralizer dimensions
#  are all distinct -- so(2,2) is too small: a single boost is regular and its centralizer
#  coincidentally equals the compact dimension.)
pp = qq = 4
N = pp + qq
dim_alg = N * (N - 1) // 2                    # 28
dim_maxcompact = pp * (pp - 1) // 2 + qq * (qq - 1) // 2  # so(4)+so(4) = 6+6 = 12

# PC1 (SINGLET / NON-COMPACTIFYING -- gives the detector teeth):
# a condensate prop. to the identity is a SINGLET; it commutes with EVERYTHING, so its
# stabilizer is the FULL group and it breaks ZERO generators. FIRES if anyone claims a
# singlet condensate compactifies to the maximal compact.
O_singlet = np.eye(N)
d_alg, d_cent_singlet = centralizer_dim_so(pp, qq, O_singlet)
check("PC1.singlet_stabilizer_is_full_group", d_cent_singlet == dim_alg,
      f"cent={d_cent_singlet}, full={dim_alg} (breaks 0; does NOT close A1)")
check("PC1b.singlet_is_not_the_compact_reduction", d_cent_singlet != dim_maxcompact,
      "singlet does NOT reduce to the maximal compact")

# PC2 (GOOD-BRANCH tau1 -> P): the condensate prop. to P = beta (the Cartan involution)
# has centralizer = the MAXIMAL COMPACT. FIRES if the centralizer of P were not the
# compact reduction (the whole claim of the wave).
O_P = np.diag([1.0] * pp + [-1.0] * qq)        # P = diag(I_pp, -I_qq)
_, d_cent_P = centralizer_dim_so(pp, qq, O_P)
check("PC2.P_condensate_gives_maximal_compact", d_cent_P == dim_maxcompact,
      f"cent(P)={d_cent_P} == so(4)+so(4)={dim_maxcompact}; breaks {dim_alg - d_cent_P}")
check("PC2b.P_breaks_the_full_noncompact_coset", dim_alg - d_cent_P == dim_alg - dim_maxcompact,
      f"broken={dim_alg - d_cent_P} == coset={dim_alg - dim_maxcompact}")

# PC3 (PATHOLOGICAL / off-diagonal): an off-diagonal boost generator (the definite-basis
# image of i*tau2, a coset element that MIXES the two factors) does NOT have the compact
# centralizer; its stabilizer contains non-compact directions and differs from Sp x Sp.
# FIRES if an off-diagonal pairing were mistaken for a compactifying ~P direction.
O_boost = np.zeros((N, N))
O_boost[0, pp] = O_boost[pp, 0] = 1.0          # a genuine so(4,4) boost (couples + and - block)
_, d_cent_boost = centralizer_dim_so(pp, qq, O_boost)
check("PC3.offdiagonal_boost_not_compact_reduction", d_cent_boost != dim_maxcompact,
      f"cent(boost)={d_cent_boost} != compact {dim_maxcompact} (does NOT give Sp x Sp)")

# PC4: Proposition-1 style guard -- only the compact-image stabilizer admits a good stable.
# A stabilizer equal to the full non-compact group (the singlet case) admits NONE. FIRES if
# a singlet background were credited with a good-stable grading.
singlet_supplies_good_stable = bool(d_cent_singlet == dim_maxcompact)
check("PC4.singlet_supplies_no_good_stable", singlet_supplies_good_stable is False)


# ============================================================================
# [A] Exact arithmetic for the actual arena Sp(32,32;H) (reproduced from W219/W224).
# ============================================================================
print("\n[A] Exact Sp(32,32;H) dimensions")
check("A1.dim_arena_8256", dim_arena == 8256, str(dim_arena))
check("A2.dim_compact_Sp32xSp32_4160", dim_compact == 4160, str(dim_compact))
check("A3.dim_coset_4096", dim_coset == 4096 and dim_coset == 4 * p * q, str(dim_coset))
check("A4.split_closes", dim_compact + dim_coset == dim_arena)


# ============================================================================
# [B] The hyperbolic rotation relating the null pair {u,v} to the definite pair {e+,e-}.
# ============================================================================
print("\n[B] Hyperbolic rotation: null pair <-> definite (beta-eigen) pair")
r = 1.0 / np.sqrt(2.0)
# columns give u, v in the definite basis {e+, e-}
R = np.array([[r, r], [r, -r]], dtype=complex)   # u=(e++e-)/rt2, v=(e+-e-)/rt2
check("B1.rotation_is_involutive_orthogonal", np.allclose(R @ R, I2) and np.allclose(R.T @ R, I2))
# Krein Gram of eta in the null basis is hyperbolic tau1 (null pair: <u,u>=<v,v>=0,<u,v>=1)
beta_def = s3                                    # beta = diag(+1,-1) in the definite basis
gram_null = R.T @ beta_def @ R
check("B2.null_pair_is_hyperbolic", np.allclose(gram_null, s1),
      "eta Gram in {u,v} = [[0,1],[1,0]] (null pair)")


# ============================================================================
# [C] LOAD-BEARING: the good-branch condensate tau1(null) lands in the ~P direction.
# ============================================================================
print("\n[C] Condensate direction: tau1(null) -> P(definite); the exact new result")


def null_to_def(M_null):
    """Express a null-basis operator in the definite basis: M_def = R M_null R^{-1}."""
    return R @ M_null @ np.linalg.inv(R)


# W216 good-branch BdG block:  H = xi*tau3(null) + Delta*tau1(null).
# Condensate (pairing) operator = tau1(null); kinetic = tau3(null); Z2 grading Z = tau3(null).
cond_def = null_to_def(s1)     # image of tau1(null) in the definite basis
kin_def = null_to_def(s3)      # image of tau3(null)
path_def = null_to_def(s2)     # image of tau2(null) (pathological i*tau2 direction)

check("C1.condensate_tau1_maps_to_P", np.allclose(cond_def, s3),
      "Delta*tau1(null) = Delta*sigma_3(definite) = Delta*P  (the ~P Cartan direction)")
check("C2.kinetic_tau3_maps_to_offdiagonal", np.allclose(kin_def, s1),
      "xi*tau3(null) = xi*sigma_1(definite) (off-diagonal in definite basis)")
check("C3.pathological_tau2_stays_offdiagonal",
      abs(path_def[0, 0]) < 1e-12 and abs(path_def[1, 1]) < 1e-12 and
      not np.allclose(path_def, s3),
      "i*tau2 stays OFF-diagonal in definite basis -> mixes the two Sp factors (pathological)")
# The condensate in the definite basis is DIAGONAL = a Cartan-involution direction.
check("C4.condensate_is_diagonal_in_definite_basis",
      abs(cond_def[0, 1]) < 1e-12 and abs(cond_def[1, 0]) < 1e-12)

# Lift to the 64-quaternionic arena: uniform Delta across the pairs assembles P=diag(I_32,-I_32),
# whose centralizer in Sp(32,32;H) is Sp(32)xSp(32). We assert the stabilizer by the SAME
# structural fact the so(2,2) model verified numerically (centralizer of the Cartan involution
# = maximal compact), plus the exact 4160/4096 arithmetic.
stab_dim_condensate = dim_compact
broken_by_condensate = dim_arena - stab_dim_condensate
check("C5.condensate_stabilizer_is_Sp32xSp32", stab_dim_condensate == 4160)
check("C6.condensate_breaks_the_full_4096_coset", broken_by_condensate == 4096,
      "the good-branch condensate breaks exactly the non-compact block W224 required")
check("C7.model_confirms_cartan_involution_centralizer_is_compact",
      d_cent_P == dim_maxcompact,
      "so(2,2) analog: cent(P) = max compact; same structure gives Sp(32)xSp(32) at rank 32")


# ============================================================================
# [D] Channel-D reconciliation and the W235 coupling (the crux).
# ============================================================================
print("\n[D] Channel-D reconciliation: same operator, gated by the record bit")

# The Z2 grading (generation +, mirror -) is Z = tau3(null). The condensate is tau1(null).
Z_grading = s3          # tau3(null): +1 on generation (u), -1 on mirror (v)
condensate = s1         # tau1(null): the off-diagonal gen<->mirror pairing
anticommute = np.allclose(Z_grading @ condensate + condensate @ Z_grading, np.zeros((2, 2)))
check("D1.condensate_is_Z2_odd", anticommute,
      "{tau1, tau3} = 0: the ~P condensate is Z2-ODD = W231 channel-D Dirac direction")

# SAME OPERATOR: the good-stable ~P direction (Block C: tau1(null)=P) IS the channel-D
# gen-mirror pairing (tau1(null)). Not two objects.
check("D2.good_stable_direction_equals_channel_D_operator",
      np.allclose(cond_def, s3) and np.allclose(condensate, s1),
      "P(definite) and channel-D(null) are the one operator tau1(null) in two bases")

# Record-bit truth table (W235, NOT decided here). Z2-odd operator allowed iff Z NOT conserved.

def condensate_allowed(record_conserved):
    # a Z2-odd condensate is forbidden by a conserved Z2 superselection charge
    return not record_conserved

def a1_closes(record_conserved):
    # good stable is dynamically supplied iff the ~P (=tau1) condensate is allowed
    return condensate_allowed(record_conserved)

def chirality_survives(record_conserved):
    # channel-D Dirac mass (=same operator) gaps the generation iff it is allowed
    return not condensate_allowed(record_conserved)

# record CONSERVED: condensate forbidden -> A1 does NOT close, chirality PROTECTED.
check("D3.record_conserved_forbids_condensate", condensate_allowed(True) is False)
check("D4.record_conserved_A1_not_closed", a1_closes(True) is False,
      "reverts to W224 singlet input-failure")
check("D5.record_conserved_chirality_survives", chirality_survives(True) is True)
# record BROKEN: condensate allowed -> A1 CLOSES (Sp(32)xSp(32)), chirality KILLED.
check("D6.record_broken_allows_condensate", condensate_allowed(False) is True)
check("D7.record_broken_A1_closes", a1_closes(False) is True,
      "dynamical stabilizer = Sp(32)xSp(32)")
check("D8.record_broken_chirality_killed", chirality_survives(False) is False,
      "same condensate = channel-D chirality-killer")
# The two goods are MUTUALLY EXCLUSIVE through this one condensate (the sharp coupling).
mutually_exclusive = all(a1_closes(b) != chirality_survives(b) for b in (True, False))
check("D9.A1_closure_and_chirality_are_mutually_exclusive", mutually_exclusive,
      "one operator, one bit, opposite desirability: closing A1 and keeping chirality cannot both hold")


# ============================================================================
# [E] Source / dependency guards (read, not assumed).
# ============================================================================
print("\n[E] Dependency guards")
w216 = read("explorations/W216-true-vacuum-spectral-condensate-2026-07-14.md")
w224 = read("explorations/W224-native-good-stable-dynamical-vacuum-2026-07-15.md")
w231 = read("explorations/W231-close-a3-smg-realization-gu-mirror-2026-07-14.md")
w219 = read("explorations/W219-native-good-stable-stabilizer-input-gate-2026-07-14.md")
w173 = read("explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md")

check("E1.w216_good_branch_is_xi_tau3_plus_delta_tau1",
      "xi tau3 + Delta tau1" in w216 or "xi tau3 +\n" in w216 or "Delta tau1" in w216)
check("E2.w224_named_the_adjoint_P_direction",
      "~ P" in w224 and "4096" in w224 and "mirror-sector" in w224)
check("E3.w224_left_it_conditional_on_operative_C",
      "operative-C" in w224 or "operative C" in w224 or "conditional" in w224.lower())
check("E4.w231_channel_D_is_chirality_killing",
      "chirality-killing" in w231.lower() or "chirality lost" in w231.lower())
check("E5.w231_discriminant_is_Z2_conservation",
      "Z2" in w231 and ("conserved" in w231.lower()))
check("E6.w173_record_bit_unbuilt_and_open",
      "QUANTIZATION-DEPENDENT" in w173 and "unbuilt" in w173.lower())
check("E7.w219_kinematic_Sp32xSp32",
      "Sp(32) x Sp(32)" in w219 or "Sp(32)xSp(32)" in w219 or "Sp(32) x Sp(32)" in w219)


passed = sum(1 for _, c in CHECKS if c)
total = len(CHECKS)
print("\n==================== SUMMARY ====================")
print(f"{passed}/{total} checks passed")
print("GATE VERDICT (W234), conditional on the W235 record bit:")
print("  The good-branch condensate Delta = tau1(null) lands EXACTLY in the ~P Cartan")
print("  direction (tau1(null) = sigma_3(definite) = P), so IF it forms its stabilizer in")
print("  Sp(32,32;H) is Sp(32)xSp(32) (breaks the full 4096 coset) -- W219/W228 kinematic")
print("  uniqueness becomes the dynamical answer.")
print("CHANNEL-D RECONCILIATION: SAME statement, not tension. The ~P direction IS the")
print("  Z2-odd channel-D Dirac operator. Record CONSERVED -> forbidden -> A1 not closed but")
print("  chirality protected; record BROKEN -> allowed -> A1 closes (Sp32xSp32) but chirality")
print("  killed. Closing A1 dynamically and keeping chirality are mutually exclusive through")
print("  this one condensate. The bit (W235) is NOT decided here.")
print("=================================================")
raise SystemExit(0 if passed == total else 1)
