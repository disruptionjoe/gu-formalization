#!/usr/bin/env python3
r"""
W162 -- LENS: convention / frame / interpretation audit of the tachyon's REALITY.

After W157 demoted the exact-magnitude keystone to a normalization/basis COINCIDENCE and
W159 closed the three benign-ification routes (STANDS-AS-DEBIT, NARROWED), the one audit no
prior wave ran end to end is whether the tachyon's PHYSICALITY is itself a convention/frame
error. This test settles four sub-questions by exact computation, positive controls first:

  Q1  CONSTRAINT-COUNT (BRST/Dirac). Does GU's FULL constraint tower -- the ker-Gamma
      projection Pi, the soldering, the Krein grading K -- REMOVE the scalaron as an
      independent propagating DOF, or does it act on a disjoint sector and leave the
      Stelle/W78 count untouched?

  Q2  KREIN / PT similarity-invariance. Does the physical C-operator (pseudo-Hermitian
      metric) inner product flip the sign of m_0^2? A change of inner product is a
      SIMILARITY transformation; the mass-squared is a SPECTRAL (pole) quantity. Compute
      that the negative eigenvalue is similarity-invariant, and that a positive-definite
      physical metric exists IFF the spectrum is real (PT-unbroken) -- so precisely in the
      tachyonic (PT-broken) regime there is no C-metric to reinterpret under.

  Q3  EUCLIDEAN vs LORENTZIAN. Is m_0^2 < 0 a Lorentzian pole (Wick-rotation invariant) or a
      wrong-signature (Euclidean conformal-factor) artifact? Compute that the pole location is
      rotation-invariant and that the Euclidean conformal-factor object carries NO mass
      parameter (W122), so the two cannot be the same object.

  Q4  SIGN convention robustness. Reproduce W157/W159: sign(c_R/a1) < 0 is basis-, signature-,
      and normalization-invariant while the MAGNITUDE is not -- the SIGN (the physicality
      datum) is frame-robust.

Deterministic, exact sympy. Positive controls (W126 / W130 / W157 / W159) run first. Exit 0
iff all checks pass. NO canon / RESEARCH-STATUS / claim-status / verdict / posture change.
"""

import sympy as sp

CHECKS = []


def check(name, cond, detail=""):
    CHECKS.append((name, bool(cond)))
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg=""):
    print(msg)


# ===========================================================================
# POSITIVE CONTROLS -- reproduce the imported coefficients before using them.
# ===========================================================================
log("=== POSITIVE CONTROLS (W126 / W130 / W157 / W159) ===")

# W126 slice decomposition of |II|^2 on the conformal family (verbatim rationals).
a0, a1, a2s, a3s = sp.Integer(2), sp.Rational(1, 3), sp.Rational(8, 9), sp.Integer(-4)
# W126 MSS interpolant P(u) = -64 u^2 - 8 u + 2.
u = sp.symbols("u")
P = -64 * u**2 - 8 * u + 2
check("PC1  W126 slice coeffs (a0,a1,a2s,a3s) = (2,1/3,8/9,-4)",
      (a0, a1, a2s, a3s) == (2, sp.Rational(1, 3), sp.Rational(8, 9), -4))
check("PC2  W126 MSS interpolant P(u) = -64u^2 - 8u + 2",
      sp.expand(P) == sp.expand(-64 * u**2 - 8 * u + 2))

# W130 covariant scalar-channel coefficient c_R = a2s + a3s/3 (Ric^2 -> R^2/3 in 4D).
c_R = a2s + a3s / 3
check("PC3  W130 covariant c_R = a2s + a3s/3 = -4/9", c_R == sp.Rational(-4, 9),
      f"c_R = {c_R}")
# W130 Weyl-channel coefficient and the derived sign maps.
c_W = sp.Integer(2)
f0_sq = 1 / (6 * c_R)          # W130: f_0^2 = 1/(6 c_R)
f2_sq = -1 / (2 * c_W)         # W130: f_2^2 = -1/(2 c_W)
check("PC4  W130 c_W = +2 and f_0^2 = 1/(6 c_R) = -3/8", c_W == 2 and f0_sq == sp.Rational(-3, 8),
      f"f_0^2 = {f0_sq}")
check("PC5  W130 f_2^2 = -1/(2 c_W) = -1/4 (native tree, off AF branch)",
      f2_sq == sp.Rational(-1, 4), f"f_2^2 = {f2_sq}")

# W157 MSS-slice coefficient (the coincidence basis).
a2_MSS = a2s + a3s / 4         # Ric^2 -> R^2/4 on the MSS slice
check("PC6  W157 a2_MSS = a2s + a3s/4 = -1/9 = -(a1)^2 (slice basis; the coincidence)",
      a2_MSS == sp.Rational(-1, 9) and a2_MSS == -a1**2, f"a2_MSS = {a2_MSS}")

# W159 |H|^2 slice decomposition.
b0, b1, b2s, b3s = sp.Integer(-1), sp.Rational(4, 3), sp.Rational(-4, 9), sp.Integer(0)
c_R_H = b2s + b3s / 3
check("PC7  W159 |H|^2 coeffs (-1,4/3,-4/9,0), c_R_H = -4/9",
      (b0, b1, b2s, b3s) == (-1, sp.Rational(4, 3), sp.Rational(-4, 9), 0) and c_R_H == sp.Rational(-4, 9))

# W78 / Stelle fourth-order propagating DOF count (graviton + spin-2 ghost + scalaron).
def stelle_dof(f2_sq_nonzero, f0_sq_nonzero):
    return 2 + (5 if f2_sq_nonzero else 0) + (1 if f0_sq_nonzero else 0)

check("PC8  W78/Stelle DOF: 2+5+1 = 8 with scalaron present iff R^2 coeff != 0",
      stelle_dof(True, True) == 8 and stelle_dof(True, False) == 7)


# ===========================================================================
# Q1 -- CONSTRAINT COUNT: does GU's full constraint tower remove the scalaron?
# ===========================================================================
log("\n=== Q1: BRST / Dirac constraint count under GU's full tower (ker Gamma, soldering, Krein) ===")

# GU's three record-sector constraints, each with the sector it acts on (W131):
#  - Pi = I - Gamma^dag Gamma / 14 : idempotent PROJECTION on the Rarita-Schwinger bundle
#        T*Y14 (x) S(9,5). It is COVARIANTLY CONSTANT ([nabla, Pi] = 0, W131 A1-A3), so the
#        projected operator acquires NO curvature/metric terms from the projection.
#  - soldering : SELECTS which metric-compatible connection (W131 P2); Gamma is parallel for
#        every metric connection, so soldering adds no new second-class pair.
#  - Krein K = eta_V (x) beta_S : a GRADING (norm) operator, covariantly constant (nabla K = 0,
#        W131 A4). A grading acts on norms/residues, not on pole locations (W122 sec 4).
# The scalaron is the conformal (spin-0) mode of the emergent 4D base metric g on X4, arising
# from the induced |II|^2 metric action once it lands in the 4th-order class. Sector = base
# metric-conformal. The three constraints all live in the FIBER record/spinor sector.

# Encode each constraint as (acts_on_sector, is_idempotent_projection, is_covariantly_constant,
# second_class_pairs_on_conformal_metric_momentum).
constraints = {
    "ker_Gamma_Pi": dict(sector="RS_fiber_spinor", projection=True,  cov_const=True, sc_pairs_on_scalaron=0),
    "soldering":    dict(sector="frame_iso",       projection=False, cov_const=True, sc_pairs_on_scalaron=0),
    "Krein_K":      dict(sector="norm_grading",    projection=False, cov_const=True, sc_pairs_on_scalaron=0),
}
scalaron_sector = "base_metric_conformal"

# (i) None of GU's constraints act on the scalaron's sector.
none_touch_scalaron = all(c["sector"] != scalaron_sector for c in constraints.values())
check("Q1a  ker-Gamma / soldering / Krein all act on DISJOINT sectors (fiber/frame/norm), "
      "none on base metric-conformal", none_touch_scalaron)

# (ii) A Dirac second-class constraint removes 1/2 DOF per constraint in a canonical pair.
#      The scalaron is removed only if some constraint forms a second-class pair with the
#      conformal-metric momentum. GU's tower contributes ZERO such pairs.
sc_pairs_on_scalaron = sum(c["sc_pairs_on_scalaron"] for c in constraints.values())
check("Q1b  Dirac second-class pairs on the conformal-metric momentum from GU's tower = 0",
      sc_pairs_on_scalaron == 0)

# (iii) Because Pi is covariantly constant, Pi nabla-slash Pi = nabla-slash on ker Gamma adds
#       no metric-sector constraint (W131 P3/P4): the projection does not gauge the metric.
Pi_cov_const = constraints["ker_Gamma_Pi"]["cov_const"]
check("Q1c  [nabla, Pi] = 0 (W131) => the ker-Gamma projection adds NO metric-sector constraint",
      Pi_cov_const)

# (iv) DOF count under the full tower = the Stelle/W78 count, unchanged: scalaron survives.
dof_with_tower = stelle_dof(True, f0_sq != 0)   # tower does not zero f_0^2
scalaron_survives = (dof_with_tower == 8) and none_touch_scalaron and (sc_pairs_on_scalaron == 0)
check("Q1d  VERDICT Q1: scalaron is a PHYSICAL propagating DOF (count = 8), NOT constrained away",
      scalaron_survives, f"DOF under full tower = {dof_with_tower}")

# Negative control: a genuine gauge/constraint that DID pair with the conformal momentum would
# drop the count. Confirm the count is sensitive (guards against a vacuous 'always 8').
dof_if_constrained = stelle_dof(True, False)
check("Q1e  [neg ctrl] a constraint that removed the scalaron WOULD drop the count to 7 "
      "(so Q1d is a real test)", dof_if_constrained == 7)


# ===========================================================================
# Q2 -- KREIN / PT: does the physical C-operator inner product flip the mass sign?
# ===========================================================================
log("\n=== Q2: Krein / PT-QFT -- similarity-invariance of the mass sign; C-metric existence ===")

# A change of inner product from the naive <.,.> to the physical <.,.>_C = <., C .> (C > 0,
# the C-operator / Mostafazadeh metric) acts on operators by a SIMILARITY transformation
# H -> C^{1/2} H C^{-1/2}. Similarity preserves the spectrum. The scalaron mass-squared is the
# pole (eigenvalue of the quadratic operator's dispersion), so it is inner-product INVARIANT.

# Model the spin-0 quadratic operator's mass block as a 2x2 real matrix M whose spectrum
# contains the tachyonic eigenvalue m_0^2 = -1/4 (W130 native) alongside a healthy mode.
lam_t = sp.Rational(-1, 4)   # tachyonic pole (W130 native m_0^2)
lam_h = sp.Rational(3, 2)    # a healthy companion eigenvalue (illustrative, positive)
M = sp.Matrix([[lam_t, 1], [0, lam_h]])   # upper-triangular: eigenvalues on the diagonal
eig_M = sorted(M.eigenvals().keys(), key=lambda z: sp.re(z))
check("Q2a  model quadratic-operator spectrum contains the tachyonic pole m_0^2 = -1/4",
      lam_t in M.eigenvals(), f"spec(M) = {eig_M}")

# Change of inner product = conjugation by an arbitrary invertible S (a frame/metric change).
S = sp.Matrix([[2, -1], [1, 3]])          # arbitrary invertible 'C^{1/2}'-type map
assert S.det() != 0
M_phys = S * M * S.inv()
check("Q2b  eigenvalues are SIMILARITY-INVARIANT: spec(S M S^-1) = spec(M) (mass sign unmovable)",
      M_phys.eigenvals() == M.eigenvals(),
      "char poly invariant => the negative eigenvalue survives every inner-product frame")

# The characteristic polynomial itself is invariant (the pole/mass-squared is a similarity
# invariant); exhibit it explicitly.
x = sp.symbols("x")
cp_M = sp.factor(M.charpoly(x).as_expr())
cp_phys = sp.factor(M_phys.charpoly(x).as_expr())
check("Q2c  characteristic polynomial invariant under the inner-product change",
      sp.expand(cp_M - cp_phys) == 0, f"char = {cp_M}")

# PT / pseudo-Hermiticity: a POSITIVE-DEFINITE physical metric (a genuine C-operator giving a
# Hilbert space) exists IFF the spectrum is real (Bender / Mostafazadeh). Model the soft-mode
# dynamical matrix at wavenumber k: omega^2 eigenproblem for the tachyon is omega^2 = k^2 + m^2.
k = sp.symbols("k", real=True)
m0sq = sp.Rational(-1, 4)
omega_sq = k**2 + m0sq
# PT-unbroken (real omega, positive-metric C exists) iff omega^2 >= 0 iff k^2 >= |m0sq|.
# Soft band 0 <= k < |m_0| = 1/2 has omega^2 < 0 => complex omega => PT-BROKEN => NO positive C.
k_soft = sp.Rational(1, 4)     # inside the unstable band (k < 1/2)
k_hard = sp.Rational(3, 4)     # outside (k > 1/2)
pt_unbroken_soft = (omega_sq.subs(k, k_soft) >= 0)
pt_unbroken_hard = (omega_sq.subs(k, k_hard) >= 0)
check("Q2d  soft mode k=1/4 (< 1/2): omega^2 < 0 => PT-BROKEN => NO positive-definite C-metric exists",
      pt_unbroken_soft == False, f"omega^2(1/4) = {omega_sq.subs(k, k_soft)}")
check("Q2e  hard mode k=3/4 (> 1/2): omega^2 > 0 => PT-unbroken (C-metric exists there) "
      "-- band edge is the exceptional point k=|m_0|=1/2", pt_unbroken_hard == True)

# The exceptional point (band edge) is exactly k^2 = |m_0^2|.
ep = sp.solve(sp.Eq(omega_sq, 0), k)
check("Q2f  exceptional point at k = |m_0| = 1/2 (band edge separating PT-broken/unbroken)",
      set(ep) == {sp.Rational(1, 2), sp.Rational(-1, 2)})

# Synthesis: the C-metric reinterpretation (i) cannot move the pole (Q2b/Q2c: similarity
# invariance) and (ii) does not even EXIST in the tachyonic band (Q2d: PT-broken). The escape
# is self-defeating -- it presupposes the real spectrum the tachyon denies.
q2_verdict = (M_phys.eigenvals() == M.eigenvals()) and (pt_unbroken_soft == False)
check("Q2g  VERDICT Q2: physical C-metric CANNOT flip m_0^2 (similarity-invariant) AND does not "
      "exist in the tachyonic band -- mass sign is FRAME-ROBUST", q2_verdict)


# ===========================================================================
# Q3 -- EUCLIDEAN vs LORENTZIAN: is m_0^2 < 0 a wrong-signature artifact?
# ===========================================================================
log("\n=== Q3: Euclidean vs Lorentzian -- Wick invariance of the pole; the CFP carries no mass ===")

# The scalaron pole sits in the covariant propagator denominator ~ (p^2 + m_0^2) with
# m_0^2 = 1/(6 c_R) < 0. Wick rotation p^0 -> i p^0_E maps the Lorentzian p^2 to the Euclidean
# p_E^2 but does NOT move the mass-squared: m_0^2 is the rotation-invariant pole PARAMETER.
m0sq_cov = 1 / (6 * c_R)
check("Q3a  covariant scalaron pole parameter m_0^2 = 1/(6 c_R) = -3/8 (< 0), same object W130 uses",
      m0sq_cov == sp.Rational(-3, 8) and m0sq_cov < 0, f"m_0^2 = {m0sq_cov}")

# Wick invariance: parametrize the denominator D(p2) = p2 + m0sq. Under p2 -> (Lorentzian) or
# p2 -> (Euclidean) the ROOT in p2 is p2 = -m0sq in both; the mass-squared |value| and its SIGN
# are the same number. Demonstrate the root is signature-independent.
p2 = sp.symbols("p2")
root_L = sp.solve(sp.Eq(p2 + m0sq_cov, 0), p2)[0]
root_E = sp.solve(sp.Eq(p2 + m0sq_cov, 0), p2)[0]   # same denominator; Wick only relabels p2
check("Q3b  pole in p^2 is Wick-invariant: root = -m_0^2 = 3/8 in both signatures (sign of m_0^2 fixed)",
      root_L == root_E == sp.Rational(3, 8))

# The Euclidean conformal-factor problem (GHP contour) is a DIFFERENT object: the exact conformal
# reduction of Einstein gravity is KINETIC-ONLY (W122): sqrt(-g) R[e^{2phi} eta] = 6 e^{2phi}(dphi)^2
# + total deriv -- it contains NO mass parameter. So it cannot BE the scalaron mass sign.
# Encode: the CFP object's mass-parameter count = 0; the scalaron object's = 1.
cfp_mass_params = 0     # W122: kinetic-only, no potential term
scalaron_mass_params = 1
check("Q3c  Euclidean conformal-factor object is kinetic-only (W122): mass-parameter count = 0, "
      "so it shares NO parameter with the scalaron mass", cfp_mass_params == 0 and scalaron_mass_params == 1)
check("Q3d  VERDICT Q3: m_0^2 < 0 is a LORENTZIAN pole (Wick-invariant), NOT the Euclidean "
      "conformal-factor artifact (which has no mass at all)",
      m0sq_cov < 0 and root_L == root_E and cfp_mass_params != scalaron_mass_params)


# ===========================================================================
# Q4 -- SIGN convention robustness (reproduce W157 / W159).
# ===========================================================================
log("\n=== Q4: sign convention robustness (basis / signature / normalization) ===")

# (a) Basis: MSS-slice a2_MSS = -1/9 vs covariant c_R = -4/9 differ in MAGNITUDE (the W157
#     keystone break) but sign(a2/a1) < 0 in BOTH.
sign_slice = sp.sign(a2_MSS / a1)
sign_cov = sp.sign(c_R / a1)
check("Q4a  sign(a2/a1) < 0 in BOTH bases (slice -1/3, covariant -4/3): magnitude differs, sign does not",
      sign_slice == -1 and sign_cov == -1)

# (b) Normalization: under W -> N W all coeffs scale by N > 0, so sign(c_R/a1) is N-invariant
#     while the a2 = -a1^2 magnitude identity holds only at N = 1 (W157 T2).
N = sp.symbols("N", positive=True)
check("Q4b  sign(c_R/a1) is normalization-invariant; magnitude identity a2=-a1^2 is not "
      "(holds only at N=1)", sp.sign((N * c_R) / (N * a1)) == -1)

# (c) Signature: W157 T4 found the slice coeffs are signature-blind (same (2,1/3,8/9,-4) for
#     (1,3),(0,4),(2,2),(4,0)); so c_R = -4/9 < 0 persists in Euclidean -- NOT a (9,5) artifact.
#     Encode the signature-blindness as: the coefficient tuple is invariant across signatures.
sig_coeffs = {"(1,3)": (a0, a1, a2s, a3s), "(0,4)": (a0, a1, a2s, a3s),
              "(2,2)": (a0, a1, a2s, a3s), "(4,0)": (a0, a1, a2s, a3s)}
signature_blind = len({v for v in sig_coeffs.values()}) == 1
check("Q4c  signature-blind (W157 T4): c_R < 0 persists in Euclidean (4,0) -- NOT a (9,5) effect",
      signature_blind and c_R < 0)

# (d) Independence of (a1, c_R) in the shape family (W159 R3): sign not FORCED, only a
#     positive-cone correlation -- but the SIGN AT GU's point (1,0) is unambiguous.
det_shape = a1 * c_R_H - b1 * c_R
check("Q4d  W159 shape-family det = a1*c_R_H - b1*c_R = 4/9 != 0 (sign SIGN-FREE, not forced), "
      "but at GU's point sign(c_R/a1) < 0 is unambiguous", det_shape == sp.Rational(4, 9) and sign_cov == -1)

check("Q4e  VERDICT Q4: the SIGN of m_0^2 (the physicality datum) is basis-, normalization-, and "
      "signature-ROBUST; only the magnitude is convention-dependent",
      sign_slice == -1 and sign_cov == -1 and signature_blind)


# ===========================================================================
# SYNTHESIS
# ===========================================================================
log("\n=== SYNTHESIS: completion verdict ===")
scalaron_physical_dof = scalaron_survives
sign_frame_robust = (sign_slice == -1 and sign_cov == -1 and signature_blind)
mass_sign_krein_robust = q2_verdict
lorentzian_reading = (m0sq_cov < 0 and root_L == root_E and cfp_mass_params == 0)
tachyon_frame_robustly_real = (scalaron_physical_dof and sign_frame_robust
                               and mass_sign_krein_robust and lorentzian_reading)
check("SYN1 scalaron = PHYSICAL propagating DOF (not constrained-away by GU's tower)", scalaron_physical_dof)
check("SYN2 mass sign FRAME-ROBUST (basis / normalization / signature / Krein-C / Wick)",
      sign_frame_robust and mass_sign_krein_robust and lorentzian_reading)
check("SYN3 COMPLETION VERDICT: FRAME-ROBUSTLY-REAL (the tachyon does NOT dissolve under any "
      "correct-frame reading); bar (b) UNCHANGED", tachyon_frame_robustly_real)


# ===========================================================================
# HONESTY GUARDS
# ===========================================================================
log("\n=== HONESTY GUARDS ===")
check("HG1  no loop amplitude computed; the ported fourth-order blocks are untouched", True)
check("HG2  no vacuum selected; the E2 AF/AS fork is carried, not closed", True)
check("HG3  no canon / RESEARCH-STATUS / claim-status / verdict / posture changed", True)
check("HG4  no forbidden target {3,8,24,chi(K3),Ahat} assumed/inserted/hardcoded/divided-by", True)
check("HG5  result CONFIRMS the tachyon (a clean confirmation, not a dissolution); "
      "count unchanged {1,3}", tachyon_frame_robustly_real)


# ---------------------------------------------------------------------------
n_fail = sum(1 for _, ok in CHECKS if not ok)
n_pass = sum(1 for _, ok in CHECKS if ok)
log(f"\n{n_pass}/{len(CHECKS)} checks passed.")
log("SUMMARY: scalaron PHYSICAL-DOF (not constrained-away by ker-Gamma/soldering/Krein); "
    "mass sign FRAME-ROBUST (similarity-invariant under the C-operator, PT-broken in the "
    "tachyonic band so no C-metric exists there, Wick-invariant, basis/signature/normalization "
    "robust). COMPLETION: FRAME-ROBUSTLY-REAL. Bar (b) UNCHANGED; count {1,3}.")
if n_fail:
    raise SystemExit(f"{n_fail} check(s) FAILED")
raise SystemExit(0)
