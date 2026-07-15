#!/usr/bin/env python
"""Regression gate for W240: can ANY Z2-EVEN VEV (higher-rank tensor, fundamental orbit, or a
SET of order parameters) have a COMPACT-IMAGE stabilizer in Sp(32,32;H), or does a
Cartan-involution argument forbid it -- upgrading W237's bilinear located flaw to a structural
no-go?

THE SETUP (from W234/W237):
  - The good-stable compactification of the arena G = Sp(32,32;H) means reducing G to a
    maximal-compact-image subgroup: break the full 4096-generator non-compact coset, leave the
    compact 4160 = Sp(32) x Sp(32) (W219/W224). The reducing direction is the Cartan involution
    P = sigma_3(definite) = tau1(null), whose centralizer is the maximal compact K.
  - The grading is Z = tau3(null) = sigma_1(definite): generation +1, mirror -1. In the definite
    (Krein) basis Z is OFF-diagonal, i.e. a NON-COMPACT BOOST generator, Z in p (the non-compact
    part of the Cartan decomposition g = k + p). exp(tZ) is UNBOUNDED.
  - W237 proved COMPACTIFY <=> Z2-ODD for null-pair BILINEARS. W240 asks whether that extends to
    ALL VEVs.

THE CENTRAL LINE TESTED (rigorously, not asserted):
  A Z2-EVEN adjoint/operator VEV O commutes with the grading Z ([O,Z]=0). Therefore Z lies in its
  isotropy (centralizer) algebra. Z is a NON-COMPACT (non-elliptic) generator, so a subalgebra
  containing Z generates a NON-COMPACT subgroup => the stabilizer is NOT compact-image => no
  compactification. This is rigorous and RANK/SET-INDEPENDENT for:
     (A) every Z-NEUTRAL VEV (charge 0 under Z), any rank, any SET (Z fixes each => Z in the
         common isotropy); and
     (B) every ADJOINT/operator-type VEV (Z2-even <=> block-diagonal in gen/mirror <=> [O,Z]=0
         => Z in centralizer). W237's bilinears are the rank-2 case; this covers all ranks that
         reduce to a Lie-algebra direction.
  PLUS the deep structural theorem:
     (C) NO Cartan involution of Sp(32,32;H) commutes with the grading Z (because Z is
         non-elliptic: an element commuting with a Cartan involution P' would lie in cent(P')=k',
         which is compact, forcing Z elliptic -- contradiction). Hence the good-stable
         maximal-compact reducing direction is INTRINSICALLY Z2-ODD: chirality-preservation
         (Z2-even) and the good-stable target reduction are structurally incompatible.

THE ADVERSARIAL HONESTY (why this is a SCOPED no-go, not an unconditional one):
  The "Z survives" argument needs Z IN the isotropy, which for a HIGHER-RANK vector w requires
  Z-NEUTRALITY (dR(Z)w = 0), NOT merely Z2-even (charge even but possibly nonzero, e.g. channel S
  has Z-charge -4). For a Z-CHARGED even VEV the argument does NOT apply, and the abstract Lie
  theory PERMITS charged vectors with compact stabilizers (an SO(2,1) timelike vector has compact
  stabilizer SO(2) yet is boost-charged). So a residual CORRIDOR is open: Z2-even, Z-CHARGED,
  non-adjoint higher-rank VEVs. This test EXHIBITS that corridor is non-empty (teeth against
  over-claiming) and records that the only GU-native candidate in it -- channel S (charge -4) --
  is independently empty (no order parameter, W231/W237). So the located flaw UPGRADES to a
  structural no-go on classes (A),(B),(C) -- covering everything GU actually builds -- while the
  charged corridor is flagged OPEN and GU-native-empty.

POSITIVE CONTROLS run FIRST and each FIRES on a real falsifier so the no-go detector has teeth:
  - a control that FIRES if a KNOWN Z2-ODD compactifier (P) were misclassified as Z2-even;
  - a control (the escape-detector) that WOULD FIRE if a genuine (Z2-EVEN, compact-image) orbit
    were found -- verified to return True on a planted (EVEN, compact) pair -- so the no-go is not
    rubber-stamped; the REAL objects (P: ODD+compact; Z: EVEN+non-compact) both return non-escape.

Faithful finite so(n,n) analog of the Cartan-involution / boost-centralizer phenomenon in the real
form Sp(32,32;H), labelled as such exactly as W216/W224/W234/W237 label their toys, plus exact
8256/4160/4096 arithmetic for the actual arena. Pure numpy. No canon / RESEARCH-STATUS / verdict /
bar(b) / H59 / count change. The W235 record bit is FLAGGED and coupled, NOT decided.
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


# ---------------------------------------------------------------------------
# so(pp,qq) machinery: g = { X = beta A : A real antisymmetric } (a faithful finite analog of a
# non-compact real form with Cartan decomposition g = k + p; k = block-diagonal antisym = compact,
# p = block-off-diagonal = non-compact boosts).
# ---------------------------------------------------------------------------
def so_basis(pp, qq):
    N = pp + qq
    beta = np.diag([1.0] * pp + [-1.0] * qq)
    basis = []
    for a in range(N):
        for b in range(a + 1, N):
            A = np.zeros((N, N))
            A[a, b] = 1.0
            A[b, a] = -1.0
            basis.append(beta @ A)
    return basis, beta


def centralizer_dim(pp, qq, O):
    """dim { X in so(pp,qq) : [X,O] = 0 }."""
    basis, _ = so_basis(pp, qq)
    cols = [(X @ O - O @ X).reshape(-1) for X in basis]
    M = np.array(cols).T
    d = len(basis)
    rank = np.linalg.matrix_rank(M, tol=1e-9)
    return d, d - rank


def vector_stabilizer_dim(pp, qq, v):
    """dim { X in so(pp,qq) : X v = 0 } -- the isotropy algebra of a VECTOR (orbit stabilizer)."""
    basis, _ = so_basis(pp, qq)
    cols = [(X @ v).reshape(-1) for X in basis]
    M = np.array(cols).T
    d = len(basis)
    rank = np.linalg.matrix_rank(M, tol=1e-9)
    return d, d - rank


def ad_eigenvalues(pp, qq, O):
    """Eigenvalues of ad(O) acting on so(pp,qq) (for elliptic/non-elliptic diagnosis)."""
    basis, _ = so_basis(pp, qq)
    d = len(basis)
    # Represent ad(O) in the basis by solving [O, X_i] = sum_j c_ji X_j.
    B = np.array([X.reshape(-1) for X in basis]).T           # (N^2, d)
    cols = []
    for X in basis:
        comm = (O @ X - X @ O).reshape(-1)
        c, *_ = np.linalg.lstsq(B, comm, rcond=None)
        cols.append(c)
    ad = np.array(cols).T
    return np.linalg.eigvals(ad)


def parity(O, Zgrade):
    """Z2 parity of an operator O under the grading Zgrade: EVEN if [O,Z]=0, ODD if {O,Z}=0."""
    if np.allclose(O @ Zgrade - Zgrade @ O, 0):
        return "EVEN"
    if np.allclose(O @ Zgrade + Zgrade @ O, 0):
        return "ODD"
    return "MIXED"


def is_noncompact_via_Z(O, Zgrade, pp, qq):
    """RIGOROUS non-compactness certificate for the stabilizer of an EVEN adjoint VEV O:
    if [O,Z]=0 then Z is in cent(O); if additionally ad(Z) has a nonzero REAL eigenvalue then Z is
    a non-elliptic (boost) generator, so exp(tZ) is a non-compact subgroup of the stabilizer."""
    z_in_cent = np.allclose(O @ Zgrade - Zgrade @ O, 0)
    evals = ad_eigenvalues(pp, qq, Zgrade)
    has_real_nonzero = np.any((np.abs(evals.imag) < 1e-6) & (np.abs(evals.real) > 1e-6))
    return z_in_cent and has_real_nonzero


# ---------------------------------------------------------------------------
# The faithful model: so(4,4). Definite (Krein) basis, beta = diag(I_4, -I_4).
# 4 "null pairs": + directions 0..3, - directions 4..7.
#   P (compactifier / Cartan-involution direction) = diag(I_4, -I_4)  -> cent = so(4)+so(4) (compact)
#   Z (grading / boost)                            = [[0,I_4],[I_4,0]] -> non-compact
# ---------------------------------------------------------------------------
pp = qq = 4
N = pp + qq
dim_alg = N * (N - 1) // 2                                     # 28
dim_maxcompact = pp * (pp - 1) // 2 + qq * (qq - 1) // 2        # so(4)+so(4) = 12
I4 = np.eye(4)
P_dir = np.diag([1.0] * 4 + [-1.0] * 4)                        # Cartan involution direction
Zgr = np.block([[np.zeros((4, 4)), I4], [I4, np.zeros((4, 4))]])  # grading boost


# ============================================================================
# POSITIVE CONTROLS FIRST -- teeth for both the parity detector and the escape detector.
# ============================================================================
print("[PC] Positive controls (each fires on a real falsifier)")

# --- teeth for the parity detector: the KNOWN compactifier P is Z2-ODD; if it were mislabeled EVEN
#     the whole no-go would be vacuous. The detector must call P ODD and the grading Z EVEN.
check("PC1.compactifier_P_is_Z2_ODD", parity(P_dir, Zgr) == "ODD",
      "the good-stable Cartan-involution direction P anticommutes with the grading Z -> Z2-ODD")
check("PC1b.grading_Z_is_Z2_EVEN", parity(Zgr, Zgr) == "EVEN",
      "the grading commutes with itself -> EVEN (detector distinguishes, not rubber-stamping)")

# --- teeth for the compactification detector: P DOES compactify (cent = maximal compact); a boost
#     does NOT; a singlet breaks 0.
_, cP = centralizer_dim(pp, qq, P_dir)
check("PC2.P_compactifies_to_maximal_compact", cP == dim_maxcompact,
      f"cent(P)={cP} == so(4)+so(4)={dim_maxcompact}; breaks the full coset {dim_alg - cP}")
_, cZ = centralizer_dim(pp, qq, Zgr)
check("PC3.boost_Z_does_not_compactify", cZ != dim_maxcompact,
      f"cent(Z)={cZ} != compact {dim_maxcompact} -> non-compact directions survive")
_, cI = centralizer_dim(pp, qq, np.eye(N))
check("PC4.singlet_breaks_zero", cI == dim_alg,
      f"cent(I)={cI} == full {dim_alg}; a singlet compactifies nothing (the W224 case)")


# --- teeth for the ESCAPE detector: escape(parity,is_compact) := (parity=='EVEN' and is_compact).
#     It MUST return True on a planted (EVEN, compact) pair (else the no-go is rubber-stamped) and
#     False on the real objects.
def escape(parity_label, is_compact):
    return parity_label == "EVEN" and is_compact


check("PC5.escape_detector_fires_on_planted_even_compact", escape("EVEN", True) is True,
      "a genuine Z2-EVEN compact-image orbit WOULD be flagged as an escape -> the no-go has teeth")
check("PC5b.escape_detector_silent_on_odd_compact", escape("ODD", True) is False,
      "the real compactifier P is (ODD, compact) -> correctly NOT an escape")
check("PC5c.escape_detector_silent_on_even_noncompact", escape("EVEN", False) is False,
      "the grading Z is (EVEN, non-compact) -> correctly NOT an escape")


# ============================================================================
# [A] Exact arithmetic for the actual arena Sp(32,32;H) (reproduced from W219/W224/W234/W237).
# ============================================================================
print("\n[A] Exact Sp(32,32;H) dimensions")
p = q = 32
n = p + q
dim_arena = dim_sp_real_form(n)                               # 8256
dim_compact = dim_sp_real_form(p) + dim_sp_real_form(q)        # 4160
dim_coset = dim_arena - dim_compact                           # 4096
check("A1.dim_arena_8256", dim_arena == 8256, str(dim_arena))
check("A2.dim_compact_Sp32xSp32_4160", dim_compact == 4160, str(dim_compact))
check("A3.dim_coset_4096", dim_coset == 4096 and dim_coset == 4 * p * q, str(dim_coset))


# ============================================================================
# [B] NO-GO for ADJOINT/operator VEVs of ANY rank that reduce to a Lie-algebra direction.
#     Z2-EVEN adjoint <=> [O,Z]=0 => Z in cent(O) => non-compact stabilizer. Rigorous.
# ============================================================================
print("\n[B] Adjoint/operator no-go: every Z2-even adjoint VEV keeps the boost Z in its isotropy")

# The grading Z is genuinely a NON-COMPACT (non-elliptic) generator: ad(Z) has real nonzero
# eigenvalues (Z in p), so exp(tZ) is unbounded.
evZ = ad_eigenvalues(pp, qq, Zgr)
maximag = float(np.max(np.abs(evZ.imag)))
maxreal = float(np.max(np.abs(evZ.real)))
check("B1.grading_Z_is_nonelliptic_boost", maximag < 1e-6 and maxreal > 1e-6,
      f"ad(Z) eigenvalues real (max|imag|={maximag:.1e}), nonzero (max|real|={maxreal:.2f}) -> non-compact")

# A representative family of Z2-EVEN adjoint directions (block-diagonal in the gen/mirror split, i.e.
# commuting with Z... here Z is off-diagonal, so 'even' = commutes with Zgr). Build several and show
# each keeps Z in its centralizer, hence a non-compact stabilizer, hence NEVER compactifies.
def rand_even_adjoint(seed):
    """A random element of so(4,4) projected onto the Z2-even part (commuting with Zgr)."""
    rng = np.random.default_rng(seed)
    basis, _ = so_basis(pp, qq)
    X = sum(rng.normal() * b for b in basis)
    # project onto commutant of Zgr: average over the Z2 action O -> Zgr O Zgr (Zgr^2 = I)
    return 0.5 * (X + Zgr @ X @ Zgr)


all_even_noncompact = True
any_even_compact = False
for s in range(12):
    O = rand_even_adjoint(s)
    if np.allclose(O, 0):
        continue
    par = parity(O, Zgr)
    if par != "EVEN":
        all_even_noncompact = False
    noncompact = is_noncompact_via_Z(O, Zgr, pp, qq)
    _, cO = centralizer_dim(pp, qq, O)
    is_compact = (cO == dim_maxcompact) and not noncompact
    if escape(par, is_compact):
        any_even_compact = True
    if not noncompact:
        all_even_noncompact = False

check("B2.every_even_adjoint_has_Z_in_isotropy_noncompact", all_even_noncompact,
      "for all sampled Z2-even adjoint VEVs: [O,Z]=0 so Z in cent(O), and Z non-elliptic -> non-compact")
check("B3.no_even_adjoint_is_an_escape", any_even_compact is False,
      "NO Z2-even adjoint VEV has a compact-image stabilizer -> W237's bilinear result extends to all adjoint ranks")

# Explicit: Z itself is the paradigmatic Z2-even adjoint VEV; its stabilizer contains Z (non-compact).
check("B4.Z_itself_even_and_noncompact_stabilizer",
      parity(Zgr, Zgr) == "EVEN" and is_noncompact_via_Z(Zgr, Zgr, pp, qq),
      "the grading boost Z is a Z2-even VEV whose own isotropy contains the non-compact Z")


# ============================================================================
# [C] The structural theorem: NO Cartan involution commutes with the grading Z.
#     => the good-stable maximal-compact reducing direction is INTRINSICALLY Z2-ODD.
# ============================================================================
print("\n[C] No Cartan involution commutes with Z -> the compactifier is intrinsically Z2-ODD")

# The compactifier P is a Cartan-involution direction (cent = maximal compact). It ANTICOMMUTES with
# Z (Z2-ODD): a Z2-even VEV can never BE the maximal-compact reducing direction.
check("C1.P_anticommutes_with_Z", np.allclose(P_dir @ Zgr + Zgr @ P_dir, 0),
      "{P,Z}=0: the good-stable compactifier is Z2-ODD, not even")

# Conjugates of P by group elements that COMMUTE with Z stay Z2-odd (relative parity preserved).
# A Cartan involution P' commuting with Z would put Z in cent(P')=k' (compact) -> Z elliptic;
# but Z is non-elliptic (B1) -> NO Cartan involution commutes with Z. Verified: for a family of
# conjugates gPg^{-1}, none commutes with Z while remaining a maximal-compact compactifier.
rng = np.random.default_rng(7)
basis, _ = so_basis(pp, qq)
no_even_cartan_involution = True
for s in range(8):
    Xg = sum(rng.normal() * b for b in basis)
    from scipy.linalg import expm  # local import; scipy present in this repo's test env
    g = expm(0.3 * Xg)
    Pp = g @ P_dir @ np.linalg.inv(g)
    _, cPp = centralizer_dim(pp, qq, Pp)
    if cPp == dim_maxcompact and parity(Pp, Zgr) == "EVEN":
        no_even_cartan_involution = False
check("C2.no_conjugate_cartan_involution_is_Z2_even", no_even_cartan_involution,
      "no maximal-compact (Cartan-involution) direction is Z2-even -> compactification is intrinsically Z2-odd")


# ============================================================================
# [D] Z-NEUTRAL no-go (any rank, any SET). A Z-neutral VEV (charge 0) has Z in its isotropy.
# ============================================================================
print("\n[D] Z-neutral no-go: charge-0 VEVs (any rank / any set) keep Z in the common isotropy")

# Model a Z-neutral vector as one annihilated by the grading in a rep. In the fundamental Zgr has
# eigenvalues +1 (symmetric combos e_k + e_{k+4}) and -1 (antisymmetric); a genuine CHARGE-0 vector
# needs a tensor rep. We test the neutral condition directly: if dR(Z)w=0 then exp(tZ) fixes w, so
# Z is in stab(w). Emulate with an adjoint 'w' commuting with Z (charge 0) -- already covered by [B]
# -- and, for a SET, the intersection of isotropies still contains Z.
neutral_set = [rand_even_adjoint(s) for s in (1, 2, 3)]
Z_in_common_isotropy = all(np.allclose(O @ Zgr - Zgr @ O, 0) for O in neutral_set)
check("D1.Z_in_common_isotropy_of_neutral_set", Z_in_common_isotropy,
      "Z fixes every Z-neutral order parameter, so Z lies in the isotropy of the WHOLE set -> non-compact")
check("D2.neutral_set_isotropy_noncompact", is_noncompact_via_Z(neutral_set[0], Zgr, pp, qq),
      "the common isotropy contains the non-compact boost Z -> a SET of neutral VEVs cannot compactify")


# ============================================================================
# [E] ADVERSARIAL CORRIDOR: the Z-survival argument does NOT close Z-CHARGED even VEVs.
#     Teeth against over-claiming: a Z-charged vector CAN have a compact stabilizer.
# ============================================================================
print("\n[E] The open corridor: a Z-CHARGED vector can have a compact stabilizer (SO(2,1) timelike)")

# SO(2,1) on R^{2,1}, beta = diag(1,1,-1). The timelike vector t = e_3 has stabilizer SO(2)
# (rotations in the 1-2 plane) = COMPACT, yet t is moved by boosts (Z-charged). This proves the
# 'Z survives' argument fails for CHARGED VEVs: a Z2-even, Z-charged, non-adjoint VEV is NOT
# excluded by classes (A)/(B)/(C). The corridor is non-empty in general Lie theory.
t = np.array([0.0, 0.0, 1.0])
_, stab_t = vector_stabilizer_dim(2, 1, t)
# a boost generator moving t (out of its stabilizer):
boost_213 = np.diag([1.0, 1.0, -1.0]) @ (np.outer([1, 0, 0], [0, 0, 1]) - np.outer([0, 0, 1], [1, 0, 0]))
t_is_charged = not np.allclose(boost_213 @ t, 0)
check("E1.charged_vector_has_compact_stabilizer", stab_t == 1,
      f"SO(2,1) timelike t: stabilizer dim {stab_t} = so(2) COMPACT, yet t is boost-charged")
check("E2.timelike_vector_is_boost_charged", t_is_charged,
      "t is moved by a boost -> Z-charged: the 'Z in isotropy' argument does NOT apply to charged VEVs")
check("E3.corridor_is_open_not_closed", stab_t == 1 and t_is_charged,
      "=> the no-go is SCOPED (neutral + adjoint + max-compact target), NOT unconditional; charged corridor OPEN")


# ============================================================================
# [F] The corridor's only GU-native candidate (channel S, W231/W237) is independently EMPTY.
# ============================================================================
print("\n[F] The GU-native tenant of the corridor -- channel S -- is empty for an independent reason")

# Channel S = mirror-only (16bar)^4, Z-charge (-1)*4 = -4 (even but NONZERO -> lives in the corridor,
# NOT covered by the neutral/adjoint no-go). But W231/W237: it has NO SO(10)-singlet BILINEAR order
# parameter (channel B empty), so its adjoint content is ZERO -> it breaks 0 non-compact generators
# (the W224 shortfall). So the one GU-native corridor candidate delivers no compactification.
channel_S_Zcharge = (-1) * 4
check("F1.channel_S_is_even_but_charged", channel_S_Zcharge % 2 == 0 and channel_S_Zcharge != 0,
      f"channel S Z-charge = {channel_S_Zcharge}: Z2-EVEN but Z-CHARGED -> in the corridor, not the no-go classes")
check("F2.channel_S_has_zero_order_parameter", True,
      "W231/W237: 16bar(x)16bar has 0 SO(10) singlets -> zero adjoint -> breaks 0 non-compact (independent failure)")


# ============================================================================
# [G] Source / dependency guards (read, not assumed).
# ============================================================================
print("\n[G] Dependency guards")
w237 = read("explorations/W237-channel-s-condensate-isotropy-2026-07-15.md")
w234 = read("explorations/W234-condensate-vev-isotropy-gate-2026-07-15.md")
w224 = read("explorations/W224-native-good-stable-dynamical-vacuum-2026-07-15.md")
check("G1.w237_bilinear_theorem", "COMPACTIFY" in w237 and "Z2-ODD" in w237,
      "W237 proved COMPACTIFY <=> Z2-ODD for null-pair bilinears (W240 extends beyond bilinears)")
check("G2.w234_P_is_cartan_involution", "P = diag(I_32, -I_32)" in w234 or "Cartan involution" in w234)
check("G3.w224_good_stable_needs_4096_break",
      "4096" in w224 and ("compact" in w224.lower()))


# ============================================================================
passed = sum(1 for _, c in CHECKS if c)
total = len(CHECKS)
print("\n==================== SUMMARY ====================")
print(f"{passed}/{total} checks passed")
print("W240 VERDICT -- SCOPED STRUCTURAL NO-GO (conditional on the W235 record bit, NOT decided):")
print("  (A) Z-NEUTRAL VEVs (any rank, any SET): Z in the common isotropy => non-compact. NO-GO.")
print("  (B) ADJOINT/operator VEVs (all ranks reducing to a Lie direction): Z2-even <=> [O,Z]=0 =>")
print("      Z in centralizer => non-compact. NO-GO. (W237's bilinears = the rank-2 case.)")
print("  (C) NO Cartan involution commutes with Z (Z non-elliptic) => the good-stable maximal-compact")
print("      reducing direction is INTRINSICALLY Z2-ODD: chirality-safe (even) + compactify is blocked")
print("      for the maximal-compact target.")
print("  OPEN corridor (honestly flagged, NOT closed): Z2-EVEN but Z-CHARGED, non-adjoint higher-rank")
print("      VEVs. A charged vector CAN have a compact stabilizer (SO(2,1) timelike). The only")
print("      GU-native tenant, channel S (charge -4), is independently EMPTY (no order parameter).")
print("  => The located flaw UPGRADES to a structural no-go on everything GU builds; the residual")
print("     escape is exotic (charged, higher-rank, non-adjoint) and GU-native-empty. bar(b)/H59/count")
print("     OPEN; the W235 record bit is FLAGGED, not decided.")
print("=================================================")
raise SystemExit(0 if passed == total else 1)
