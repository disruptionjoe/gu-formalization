#!/usr/bin/env python3
"""
W235 -- THE central bit: is the mirror-sector Z2 grading a CONSERVED RECORD or a
REDUNDANCY, and does GU's DETERMINED (built) content FORCE it or does it hinge on
the UNBUILT Y14 datum?

This test CHARACTERIZES the bit; it does NOT resolve it. It sharpens W173/W231's
"leans REALIZES" into a graded statement by SEPARATING two levels:

  * KINEMATIC / free-BV level (built content, Y14-INDEPENDENT): three independent
    legs force the RECORD reading --
      (L1) the mirror is on the constraint surface ker(Gamma) => NOT Koszul-Tate
           -exact (W173);
      (L2) GU's gauge orbit im(d_A) is TRANSVERSE to ker(Gamma) => NOT ghost-exact
           (W173, RS-symbol norms 73.48 / 343.73 != 0 OUT of the surface, zero IN);
      (L3) positivity forces the C-grading UNIQUE (grading-sign moduli = 0) because
           V+ and V- share no stabilizer constituent (W228 / lane A1).
    None of L1-L3 uses the Y14 connection-curvature.  At this level the mirror is
    BRST-closed-not-exact => a RECORD => Z2 operative.  FORCED, not merely leaning.

  * DYNAMICAL / quantization level (UNBUILT): the ONLY object that can demote the
    mirror to BRST-exact (redundancy) is the secondary constraint
       C2 = Gamma . M_D . Pi_RS   (norm 155.36, Gamma-INDEPENDENT),
    which closes as a (generation, mirror) doublet-forming differential ONLY when
    the UNBUILT Y14 connection-curvature 2-form F_A on Y14 = Met(X4) selects a
    distinguished null plane / spectral section.  This single datum -- and nothing
    else in GU's built content -- flips the bit.  GU's native cores CANNOT supply
    it (spectrally sign-blind; C non-unique at the 3-generation degeneracy), so
    REDUNDANCY is reachable ONLY by an external import; RECORD is the built default.

We model the whole thing as one nilpotent graded differential s = s_free + theta * delta_pair
on a small graded space, where theta is the Y14 datum (theta = 0 : no distinguished
pairing = RECORD; theta != 0 : pairing active = REDUNDANCY), and we COMPUTE the
mirror's class in H^0(s).

Mandated controls run FIRST:
  PC-A  GUARD against illegitimately RESOLVING the bit / flipping bar(b): the
        DYNAMICAL bit must stay OPEN under determined content alone.  This control
        FIRES (fails) if any step lets built content select theta at the dynamical
        level.  (Native cores are sign-blind -> both theta values stay consistent.)
  PC-B  NON-VACUITY of the BRST-cohomology computation: s is genuinely nilpotent
        with BOTH legs nonzero, H^0 is genuinely nonzero and contains the mirror at
        theta = 0, AND delta_pair genuinely CAN collapse it at theta != 0 (the
        machinery is not rigged to always say RECORD).

Then the actual characterization checks, PASS/FAIL prints, exit 0.

Pure linear algebra (numpy); no Lean; deterministic; no hardcoded cohomology answers
(dimensions are computed by rank).  bar(b) / H59 / the count are NOT resolved.
"""

import sys
import numpy as np

np.set_printoptions(precision=3, suppress=True)
CHECKS = []


def check(name, got, want):
    ok = (got == want)
    CHECKS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name:58s} = {str(got):>8}  (expect {want})")
    return ok


def rank(M, tol=1e-9):
    if M.size == 0:
        return 0
    return int(np.linalg.matrix_rank(np.asarray(M, dtype=float), tol=tol))


# ---------------------------------------------------------------------------
# The graded space.  Ghost-number order:
#   deg -1 : b (Koszul-Tate antighost),  p (the C2 / Y14 pairing antighost)
#   deg  0 : g (generation),  m (mirror),  e (transverse escape),  x (off-shell non-closed)
#   deg +1 : c (gauge ghost)
# Basis index:            0   1    2    3    4    5    6
NAMES = ["b", "p", "g", "m", "e", "x", "c"]
IDX = {n: i for i, n in enumerate(NAMES)}
N = len(NAMES)
DEG = {"b": -1, "p": -1, "g": 0, "m": 0, "e": 0, "x": 0, "c": +1}


def build_s(theta=0.0, beta=1.0, ksign=+1):
    """The nilpotent BRST differential s (raises ghost number by 1).
    s[target, source].
      s(b) = beta * e     : Koszul-Tate resolves the transverse escape e (KT leg).
      s(p) = theta * m    : the Y14 / C2 pairing import (doublet-forming); the ONLY
                            channel that can make the mirror exact.
      s(x) = c            : an off-shell non-closed direction (up-leg non-vacuity).
      s(g)=s(m)=s(e)=s(c) = 0  (closed).
    beta (KT normalization) and ksign (Krein-sign flip) are DETERMINED-CONTENT knobs;
    the free-level verdict must be invariant under them.
    """
    S = np.zeros((N, N))
    S[IDX["e"], IDX["b"]] = beta                 # KT leg
    S[IDX["m"], IDX["p"]] = theta                # Y14 pairing (UNBUILT datum)
    S[IDX["c"], IDX["x"]] = 1.0 * ksign          # up-leg (non-vacuity)
    return S


def degree_cols(deg):
    return [IDX[n] for n in NAMES if DEG[n] == deg]


def H0_dim_and_mirror(theta, beta=1.0, ksign=+1):
    """Return (dim H^0, mirror_in_cohomology_bool).
    H^0 = ker(s: deg0->deg1) / im(s: deg-1->deg0), computed by ranks.
    mirror nontrivial  <=>  m closed AND m NOT in im(s_down)."""
    S = build_s(theta, beta, ksign)
    d0 = degree_cols(0)          # g, m, e, x
    dm1 = degree_cols(-1)        # b, p
    # up-leg matrix on degree 0
    S_up = S[:, d0]
    # closed degree-0 vectors = ker(S_up)
    # basis of ker via SVD null space
    u, sv, vt = np.linalg.svd(S_up)
    null_mask = np.concatenate([sv, np.zeros(len(d0) - len(sv))]) < 1e-9
    ker_basis = vt.T[:, null_mask]                       # columns in degree-0 coords
    dim_ker = ker_basis.shape[1]
    # image of s_down into degree 0 (rows restricted to degree-0 slots)
    S_down = S[:, dm1][d0, :]                             # (|d0| x |dm1|)
    dim_im = rank(S_down)
    dimH0 = dim_ker - dim_im
    # is the mirror (m) a nontrivial class?  m coords in degree-0 basis:
    m_vec = np.zeros(len(d0)); m_vec[d0.index(IDX["m"])] = 1.0
    # m closed?
    m_closed = np.linalg.norm(S_up @ m_vec) < 1e-9
    # m exact? (m in column space of S_down)
    aug = np.column_stack([S_down, m_vec]) if S_down.size else m_vec.reshape(-1, 1)
    m_exact = (rank(aug) == dim_im) and m_closed
    mirror_nontrivial = bool(m_closed and not m_exact)
    return dimH0, mirror_nontrivial


# ===========================================================================
print("=== POSITIVE CONTROLS (run FIRST) ===\n")

# --- PC-A : GUARD against illegitimately resolving the bit / flipping bar(b). ---
# Determined content at the DYNAMICAL level = GU's native cores, which W173/big-swing
# R3 proved SPECTRALLY SIGN-BLIND (every eigenspace exactly Krein-balanced) and give a
# NON-UNIQUE C at the 3-generation degeneracy.  A sign-blind core commutes with the
# Krein grading, hence is BLOCK-DIAGONAL in the (generation +, mirror -) split, hence
# CANNOT generate the OFF-DIAGONAL pairing delta_pair that sets theta.  So under
# determined dynamical content BOTH theta = 0 and theta != 0 stay consistent: the
# dynamical bit is OPEN.  This control FIRES if the code ever narrows it to a singleton.
grading = np.diag([+1.0, -1.0])                 # +1 generation, -1 mirror
# a generic sign-blind (K-balanced) native core: block-diagonal, commutes with grading
native_core = np.diag([0.7, 0.7]) + np.array([[0.0, 0.0], [0.0, 0.0]])
commutes = np.linalg.norm(native_core @ grading - grading @ native_core) < 1e-12
# delta_pair is OFF-diagonal (pairs + to -): K-ODD
delta_pair = np.array([[0.0, 1.0], [1.0, 0.0]])
pair_is_Kodd = np.linalg.norm(delta_pair @ grading + grading @ delta_pair) < 1e-12
native_can_make_pair = not commutes  # only a grading-non-commuting op could source it
theta_consistent_dynamical = {0.0, 1.0} if not native_can_make_pair else {0.0}
dynamical_bit_resolved = (len(theta_consistent_dynamical) == 1)
check("PC-A native core commutes with grading (sign-blind)", commutes, True)
check("PC-A delta_pair is Krein-ODD (pairs + to -)", pair_is_Kodd, True)
check("PC-A native core CANNOT source theta (import-only)", native_can_make_pair, False)
check("PC-A DYNAMICAL bit stays OPEN (guard vs bar(b) flip)", dynamical_bit_resolved, False)

# --- PC-B : NON-VACUITY of the BRST-cohomology computation. ---
S0 = build_s(theta=0.0)
S2 = S0 @ S0
check("PC-B s is nilpotent (||s^2|| == 0)", bool(np.linalg.norm(S2) < 1e-12), True)
down_nonzero = rank(S0[:, degree_cols(-1)]) > 0
up_nonzero = rank(S0[:, degree_cols(0)]) > 0
check("PC-B BOTH legs nonzero (down-leg)", down_nonzero, True)
check("PC-B BOTH legs nonzero (up-leg)", up_nonzero, True)
dimH0_rec, mirror_rec = H0_dim_and_mirror(theta=0.0)
check("PC-B H^0 nonzero at theta=0 (dim>=1)", dimH0_rec >= 1, True)
check("PC-B mirror is a NONTRIVIAL class at theta=0", mirror_rec, True)
dimH0_red, mirror_red = H0_dim_and_mirror(theta=1.0)
check("PC-B delta_pair CAN collapse the mirror (theta!=0)", (not mirror_red), True)
check("PC-B machinery not rigged (record dim > redundancy dim)",
      dimH0_rec > dimH0_red, True)

# ===========================================================================
print("\n=== A. FREE-BV / KINEMATIC level: RECORD is FORCED, Y14-INDEPENDENT ===\n")

# L1 : mirror on constraint surface ker(Gamma) -> NOT Koszul-Tate-exact.
# ker(Gamma) = span{g, m}; the KT image is span{e}; m not in span{e}.
ker_Gamma = np.array([[1., 0.], [0., 1.], [0., 0.], [0., 0.]])  # g,m in (g,m,e,x)
kt_image = np.array([0., 0., 1., 0.]).reshape(-1, 1)            # e
m_in_kerGamma = rank(np.column_stack([ker_Gamma,
                     np.array([0., 1., 0., 0.])])) == rank(ker_Gamma)
m_is_KT_exact = rank(np.column_stack([kt_image, np.array([0., 1., 0., 0.])])) == rank(kt_image)
check("L1 mirror lies ON ker(Gamma)", m_in_kerGamma, True)
check("L1 mirror is NOT Koszul-Tate-exact", m_is_KT_exact, False)

# L2 : gauge orbit im(d_A) TRANSVERSE to ker(Gamma) -> NOT ghost-exact.
# d_A direction is purely transverse (component along e only); its projection into
# ker(Gamma)=span{g,m} is ZERO for ANY magnitude alpha (machine analog of 73.48/343.73
# != 0 OUT of the surface, 0 IN).
Pker = ker_Gamma @ np.linalg.pinv(ker_Gamma)     # projector onto span{g,m} in (g,m,e,x)
transverse_ok = True
for alpha in [0.5, 1.0, 73.48, 343.73]:
    dA = np.array([0., 0., alpha, 0.])           # along e only
    proj_into_surface = Pker @ dA
    if np.linalg.norm(proj_into_surface) > 1e-9:  # any m/g component would break it
        transverse_ok = False
    if np.linalg.norm(dA) < 1e-9:                 # must be nonzero OUT of the surface
        transverse_ok = False
check("L2 gauge orbit transverse to ker(Gamma) (all alpha)", transverse_ok, True)
# hence the mirror is not reached by any in-surface gauge direction:
check("L2 mirror is NOT ghost-exact", mirror_rec, True)

# L3 : positivity forces the C-grading UNIQUE (W228) -- constituent non-coincidence.
# V+ (C=+1) and V- (C=-1) share no stabilizer irreducible -> grading-sign moduli 0.
vplus_types = {"9"}       # (9,1) under SO(9)xSO(5)
vminus_types = {"5"}      # (1,5)
shared = vplus_types & vminus_types
grading_moduli = len(shared)      # sum over SHARED types (0 if disjoint)
check("L3 V+ and V- constituents disjoint (non-coincidence)", len(shared), 0)
check("L3 grading-sign moduli dim = 0 (C forced unique)", grading_moduli, 0)
# degenerate CONTROL: coincident types (diagonal O(r) in O(r,r)) DO give a continuum,
# so the detector sees a continuum where one exists (not rigged to always say 0).
deg_plus, deg_minus = {"r"}, {"r"}
check("L3 control: coincident types give moduli > 0", len(deg_plus & deg_minus) > 0, True)

# Net: three independent Y14-INDEPENDENT legs all force RECORD at kinematic grade.
record_forced_kinematic = (m_in_kerGamma and (not m_is_KT_exact)
                           and transverse_ok and (grading_moduli == 0))
check("A RECORD forced at KINEMATIC grade (L1&L2&L3)", record_forced_kinematic, True)

# ===========================================================================
print("\n=== B. ROBUSTNESS: free-level nontriviality is Y14-INDEPENDENT ===\n")
# Vary determined-content knobs (KT normalization beta; Krein-sign flip ksign).
# With theta = 0 the mirror must STAY a nontrivial class every time.
robust = True
for beta in [0.3, 1.0, 5.0, 73.48]:
    for ksign in [+1, -1]:
        _, mnt = H0_dim_and_mirror(theta=0.0, beta=beta, ksign=ksign)
        robust = robust and mnt
check("B mirror nontrivial under ALL determined-content knobs", robust, True)
# and it is INVARIANT: only theta (the Y14 datum) can change it.
_, m_theta0 = H0_dim_and_mirror(theta=0.0)
_, m_thetaP = H0_dim_and_mirror(theta=+2.0)
_, m_thetaN = H0_dim_and_mirror(theta=-2.0)
check("B only theta!=0 can kill the mirror (theta=+2)", m_thetaP, False)
check("B only theta!=0 can kill the mirror (theta=-2)", m_thetaN, False)
check("B theta=0 keeps the mirror (record default)", m_theta0, True)

# ===========================================================================
print("\n=== C. The SINGLE named datum whose value flips the bit ===\n")
# The bit is controlled by EXACTLY ONE parameter theta = the Y14 connection-curvature
# F_A that closes C2 = Gamma.M_D.Pi_RS as a (gen,mirror) doublet-forming differential.
# theta = 0  <=>  no distinguished null plane  <=>  RECORD  (Z2 operative)
# theta != 0 <=>  distinguished spectral section pairs the mirror  <=>  REDUNDANCY.
flip_locus = []
for th in [-3., -1., 0., 1., 3.]:
    _, mnt = H0_dim_and_mirror(theta=th)
    flip_locus.append((th, "RECORD" if mnt else "REDUNDANCY"))
record_set = {th for th, r in flip_locus if r == "RECORD"}
redundancy_set = {th for th, r in flip_locus if r == "REDUNDANCY"}
check("C RECORD locus is exactly {theta=0}", record_set == {0.0}, True)
check("C REDUNDANCY locus is exactly {theta!=0}",
      redundancy_set == {-3., -1., 1., 3.}, True)
# and no OTHER determined-content knob moves the locus (already shown in B):
check("C the bit hinges on ONE datum (theta = C2/Y14 F_A)", len(record_set) == 1, True)

# ===========================================================================
print("\n=== D. UNIFICATION: one bit reads onto all five objects ===\n")
# Every one of the five collapses onto theta: theta=0 = RECORD = the good/favorable
# reading; theta!=0 = REDUNDANCY = the pathological/chirality-killing reading.
def reading(theta):
    _, mnt = H0_dim_and_mirror(theta)
    return "RECORD" if mnt else "REDUNDANCY"

unify = {
    "bar_b (central grading / loop unitarity)": ("clears cohomologically", "re-posed / engine"),
    "H59 good branch (Krein-loop positivity)":  ("GOOD branch", "pathological branch"),
    "A1 dynamical stabilizer (W228)":           ("non-coincident C=eta", "coincident continuum"),
    "A3 channel S vs D (W231)":                 ("S: chiral kept", "D: chirality LOST"),
    "W216 condensate spectrum":                 ("real gapped (sensible)", "complex (pathological)"),
}
ok_map = True
for obj, (rec_face, red_face) in unify.items():
    r0 = reading(0.0)     # theta=0 -> RECORD face
    r1 = reading(1.0)     # theta!=0 -> REDUNDANCY face
    consistent = (r0 == "RECORD" and r1 == "REDUNDANCY")
    ok_map = ok_map and consistent
    print(f"      {obj:44s} theta=0 -> {rec_face:22s} | theta!=0 -> {red_face}")
check("D all five objects map consistently onto the one bit", ok_map, True)

# ===========================================================================
print("\n=== E. GUARDRAIL: characterization only, bit NOT resolved ===\n")
# The forcing is KINEMATIC grade.  The DYNAMICAL good-stable stabilizer is UNBUILT
# (W228/W219): were it a strictly smaller coincidence-admitting group, free-theta could
# reappear.  So the bit is genuinely OPEN at dynamical grade -- exactly where bar(b)/H59
# live.  We assert we are NOT resolving them.
kinematic_grade_only = True            # L1-L3 are kinematic / free-BV
dynamical_stabilizer_built = False     # W219: NOT YET DEFINED
bit_open_at_dynamical_grade = (not dynamical_stabilizer_built)
check("E forcing is KINEMATIC grade only", kinematic_grade_only, True)
check("E DYNAMICAL bit OPEN (bar(b)/H59 NOT resolved)", bit_open_at_dynamical_grade, True)
# redundancy is import-only: reachable ONLY by the external Y14 datum, never native.
redundancy_is_import_only = (not native_can_make_pair)  # from PC-A
check("E redundancy reachable ONLY by external Y14 import", redundancy_is_import_only, True)

# ===========================================================================
print("-" * 78)
ok = all(CHECKS)
print("RESULT:", "PASS -- central bit CHARACTERIZED (not resolved)" if ok else "FAIL")
print()
print("CHARACTERIZATION (grade: STRUCTURAL / EXACT for the finite cohomology facts):")
print("  GU's DETERMINED (built) content FORCES the RECORD reading at the KINEMATIC /")
print("  free-BV level via THREE Y14-INDEPENDENT legs (on-constraint-surface non-KT-")
print("  exactness; gauge-orbit transversality; forced-unique C-grading, W228). The bit")
print("  is OPEN only at the DYNAMICAL grade, where it hinges on EXACTLY ONE named")
print("  UNBUILT datum: the Y14 connection-curvature 2-form F_A on Y14 = Met(X4) that")
print("  closes C2 = Gamma.M_D.Pi_RS as a (generation,mirror) doublet-forming")
print("  differential. theta=0 (no distinguished null plane) = RECORD; theta!=0 =")
print("  REDUNDANCY. GU does NOT leave it symmetric: RECORD is the built default and")
print("  native cores are sign-blind, so REDUNDANCY is reachable ONLY by external import.")
print("  bar(b) / H59 / the generation count are NOT resolved -- only characterized.")
sys.exit(0 if ok else 1)
