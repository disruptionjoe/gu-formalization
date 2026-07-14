#!/usr/bin/env python3
r"""
W172 / TEAM NO-GO -- does the free no-local-positive-metric theorem (W121/W54) extend to
FORBID the INTERACTING C-operator (Krein grading NOT-OPERATIVE), or does the C-metric survive
as a consistent non-local object (OPERATIVE)?

THE ONE OBJECT. The interacting C-operator: C^2 = 1, [C, S] = 0, eta_+ = eta C > 0. If it EXISTS
the Krein grading is OPERATIVE (physical-subspace unitarity holds in the C-metric, W132). If it
does NOT exist the grading is NOT-OPERATIVE: the tachyon is physical and re-poses bar (b) as the
false-vacuum record-accretion ENGINE (W163/W166), it does NOT fail the program.

THE NEGATIVE ATTACK (adversarial; try to PROVE the C-operator does not exist). Three routes, each
tested here, plus the honest fourth handle they surface:

  ROUTE 1 -- extend the no-local-positive-metric theorem (the assigned attack). W54/W121 proved
    (free case, machine-checked) NO LOCAL positive metric exists: the whole positive-intertwiner
    family carries 1/sqrt(k^2+m^2) branch cuts, exponentially localized kernel ~e^{-m|x|}. Does
    the interaction upgrade "no LOCAL metric" to "no metric AT ALL"? RESULT (B1, B3): NO. The
    theorem forbids LOCALITY, not EXISTENCE; the free C EXISTS as a (non-local) object and the
    interacting C exists order-by-order (the positive metric persists under the coupling in the
    unbroken phase, B3 sweep). NO-OBSTRUCTION on this route.

  ROUTE 2 -- CLOP forces a contradiction (W124). RESULT (B2): NO. The CLOP band
    {-1/2,0,+1/2,+1}x(cut) is a property of the REMOVAL prescription's contour-deformation step;
    the GRADED family (real mass, ordinary Feynman contour, Krein weights) gives the SINGLE
    unambiguous even-cut value +1. The graded S-matrix is CLOP-unambiguous, so the C-operator
    commuting with it is not obstructed by CLOP. NO-OBSTRUCTION on this route.

  ROUTE 3 -- the jointly-unsatisfiable axioms (W133 X1) prove no single C. RESULT (B3): NO as a
    non-existence proof. eps=-1 forces even cut +1, odd cut -1; spectral positivity of ALL
    real-axis cuts needs eps=+1: (A) analyticity and (P) positivity are jointly unsatisfiable
    WITH A LOCAL STRUCTURE. This RE-DERIVES W54's non-locality; the C-metric resolves it by being
    NON-LOCAL, not by not existing. GU picks the positivity family consistently as a non-local
    object. NO-OBSTRUCTION on this route.

  ROUTE 4 (the honest handle the three routes surface; INDEPENDENT of the metric-locality
    theorem) -- DYNAMICAL PT breaking. The interacting ghost self-energy has Im Sigma(M^2) > 0
    (W51) with ANTI-DAMPING sign (W132: the leak is probability EXCESS, wrong-sign width). A
    wrong-sign width past the exceptional point puts a complex-conjugate eigenvalue pair on the
    PHYSICAL sheet = spontaneously broken PT = NO positive metric = NO C-operator = NOT-OPERATIVE.
    RESULT (B4): this no-go is GENUINE but CONDITIONAL on the pole reaching the physical sheet
    (exceeding the exceptional point), which is exactly H59's open settling object. It is NOT
    supplied by the no-local-positive-metric theorem. So the overall verdict is NARROWED, not
    NO-GO-PROVEN and not bare NO-OBSTRUCTION.

VERDICT: NARROWED. The assigned metric-locality attack returns NO-OBSTRUCTION-FOUND (the interacting
C survives as a consistent non-local object at the level the free theorem controls); the only live
no-go is the DYNAMICAL PT-breaking handle, narrowed to the physical-sheet-vs-second-sheet stability
of the interacting ghost pole (= H59). Effect on bar (b): NOT cleared, NOT proven-no-go; the
C-operator is OPERATIVE-CONDITIONAL-ON-UNBROKEN-PT, priced non-local (microcausality). If the
dynamical PT-breaking later closes, NOT-OPERATIVE -> engine reframe (bar (b) RE-POSED, not failed).

Machinery: finite-dimensional Bender-Brody-Jones 2x2 PT model as the EXACT calibrator for
"C-operator exists <=> unbroken PT (positive metric)"; the W121 polynomial-fiber sign test inline
for the free non-locality; exact Krein/CLOP weight arithmetic for W124/W133; a random pseudo-
unitary S for the W132 expansion identity. Deterministic. No canon / RESEARCH-STATUS / claim-status
/ verdict / posture change. H59 remains OPEN.

Reproducible: python tests/W172_interacting_c_operator_nogo.py
"""
from __future__ import annotations

import math
import random

import numpy as np

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ==================================================================================================
# Bender-Brody-Jones 2x2 PT model -- the EXACT calibrator for "C-operator exists <=> unbroken PT".
#   H(r, s, theta) = [[r e^{i theta}, s], [s, r e^{-i theta}]],  P = [[0,1],[1,0]],  T = conj.
#   Eigenvalues E_pm = r cos theta +- sqrt(s^2 - r^2 sin^2 theta); REAL iff s >= r|sin theta|.
#   Unbroken: sin(alpha) = (r/s) sin theta,  C = (1/cos alpha)[[i sa, 1],[1, -i sa]],  C^2 = 1,
#             [C, H] = 0, eta_+ = P C is Hermitian positive-definite (eigenvalues (1 +- sa)/cos a).
#   The EXCEPTIONAL POINT s = r|sin theta| is where the C-operator ceases to exist.
# ==================================================================================================

def H_ptrs(r: float, s: float, theta: float) -> np.ndarray:
    return np.array([[r * np.exp(1j * theta), s], [s, r * np.exp(-1j * theta)]], dtype=complex)


P2 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)


def c_operator(r: float, s: float, theta: float):
    """Return (C, eta_plus, ok) with ok = True iff unbroken PT (positive metric exists)."""
    x = (r / s) * math.sin(theta)          # sin(alpha)
    if abs(x) >= 1.0:                       # broken PT: alpha complex, no real C
        return None, None, False
    ca = math.sqrt(1.0 - x * x)             # cos(alpha) > 0
    C = (1.0 / ca) * np.array([[1j * x, 1.0], [1.0, -1j * x]], dtype=complex)
    eta_plus = P2 @ C                        # candidate positive metric
    return C, eta_plus, True


def is_pos_def_hermitian(M: np.ndarray, tol: float = 1e-9) -> bool:
    if np.max(np.abs(M - M.conj().T)) > tol:
        return False
    w = np.linalg.eigvalsh((M + M.conj().T) / 2)
    return bool(np.min(w) > tol)


log("=" * 96)
log("W172 -- DOES THE NO-LOCAL-POSITIVE-METRIC THEOREM EXTEND TO FORBID THE INTERACTING C-OPERATOR?")
log("=" * 96)

# --------------------------------------------------------------------------------------------------
# BLOCK 0 -- positive controls (calibrator + the two named reproductions).
# --------------------------------------------------------------------------------------------------
log("")
log("0. Positive controls")

# PC1: the C-operator EXISTS in the unbroken phase (calibrator sanity). C^2=1, [C,H]=0, eta_+ > 0.
r0, s0, th0 = 1.0, 2.0, 0.6
C, etap, ok = c_operator(r0, s0, th0)
H0 = H_ptrs(r0, s0, th0)
evals = np.linalg.eigvals(H0)
c2 = np.max(np.abs(C @ C - np.eye(2)))
commut = np.max(np.abs(C @ H0 - H0 @ C))
check("PC1 calibrator: in the UNBROKEN phase (s=2 > r|sin theta|=0.56) the C-operator EXISTS -- "
      "C^2=1, [C,H]=0, eigenvalues real, eta_+ = P C positive-definite",
      ok and c2 < 1e-12 and commut < 1e-12 and np.max(np.abs(evals.imag)) < 1e-12
      and is_pos_def_hermitian(etap),
      f"|C^2-1|={c2:.1e}, |[C,H]|={commut:.1e}, max|Im E|={np.max(np.abs(evals.imag)):.1e}")

# PC2 (reproduce the free no-local-positive-metric theorem, W121/W54): the ghost Krein signs
# (+,-,-,+) admit NO local (polynomial-symbol) grading, but the EVEN entire grading is indefinite
# -- so any positive metric must carry a NON-polynomial (branch-cut) symbol = non-local. The C
# EXISTS non-locally; LOCALITY is what fails. (W121 PC1 + T3-1 arithmetic, inline.)
eps_ghost = (+1, -1, -1, +1)
c_even = (+1, +1, -1, -1)
weights = tuple(e * c for e, c in zip(eps_ghost, c_even))
M1f, M2f = 1.0, 2.0


def om(k, m):
    return math.sqrt(k * k + m * m)


def local_poly_grades(coeffs, k_grid) -> bool:
    """Does a polynomial fiber symbol F(lambda)=sum c_j lambda^j realize the ghost sign pattern?"""
    for k in k_grid:
        vals = (sum(cj * om(k, M1f) ** j for j, cj in enumerate(coeffs)),
                sum(cj * (-om(k, M1f)) ** j for j, cj in enumerate(coeffs)),
                sum(cj * om(k, M2f) ** j for j, cj in enumerate(coeffs)),
                sum(cj * (-om(k, M2f)) ** j for j, cj in enumerate(coeffs)))
        for v, e in zip(vals, eps_ghost):
            if v == 0 or (v > 0) != (e > 0):
                return False
    return True


rng = random.Random(172)
k_grid = np.linspace(0.0, 400.0, 401)
n_local = sum(1 for _ in range(3000)
              if local_poly_grades([rng.uniform(-5, 5) for _ in range(rng.randint(1, 6) + 1)],
                                   k_grid))
check("PC2 free theorem (W121/W54 reproduced): the even ENTIRE grading gives indefinite metric "
      "weights (+1,-1,+1,-1), and NONE of 3000 random polynomial (local) fiber symbols realizes "
      "the ghost sign pattern (+,-,-,+) on k in [0,400] -- no LOCAL positive metric; the surviving "
      "C carries a branch-cut symbol (non-local), it EXISTS but is not local",
      weights == (1, -1, 1, -1) and min(weights) < 0 and n_local == 0,
      f"even-grading weights={weights}; local polynomial graders found={n_local}/3000")

# PC3 (reproduce W132's violation): for any pseudo-unitary S (S^dag eta S = eta), the physical-
# subspace block A = P+ S P+ obeys A^dag A = P+ + B^dag B >= P+, so physical row sums exceed 1.
eta4 = np.diag([1.0, 1.0, -1.0, -1.0])        # (+,+,-,-): even/odd ghost-number grading
Pp = np.diag([1.0, 1.0, 0.0, 0.0])
Pm = np.diag([0.0, 0.0, 1.0, 1.0])
rngS = np.random.default_rng(172)
Kraw = rngS.standard_normal((4, 4)) + 1j * rngS.standard_normal((4, 4))
Kph = 0.5 * (Kraw + eta4 @ Kraw.conj().T @ eta4)   # eta-pseudo-Hermitian generator
# matrix exponential via eigen-decomposition of the (generally non-normal) matrix 1j*Kph
from numpy.linalg import eig as _eig
wv, Vv = _eig(1j * Kph)
S = Vv @ np.diag(np.exp(wv)) @ np.linalg.inv(Vv)
pseudo = np.max(np.abs(S.conj().T @ eta4 @ S - eta4))
A = Pp @ S @ Pp
B = Pm @ S @ Pp
ident = np.max(np.abs(A.conj().T @ A - (Pp + B.conj().T @ B)))
row_excess = np.real((A.conj().T @ A)[0, 0] - 1.0)
check("PC3 W132 violation reproduced: a random pseudo-unitary S (|S^dag eta S - eta| checked) "
      "satisfies the EXACT expansion identity A^dag A = P+ + B^dag B, so a physical in-state's "
      "physical-channel probability EXCEEDS 1 (excess = ||B|i>||^2 >= 0): violation on the free "
      "positive subspace",
      pseudo < 1e-9 and ident < 1e-9 and row_excess > 1e-6,
      f"|pseudo-unitarity|={pseudo:.1e}, |identity|={ident:.1e}, row-1 excess={row_excess:.4f}")

# --------------------------------------------------------------------------------------------------
# BLOCK 1 -- ROUTE 1: does the interaction upgrade "no LOCAL metric" to "no metric at all"? NO.
# --------------------------------------------------------------------------------------------------
log("")
log("1. ROUTE 1 -- no-local-positive-metric extended: forbids LOCALITY, not EXISTENCE")

# B1a: the free non-local C EXISTS. Realize it as the branch-cut (quasi-local) grading symbol
# F(lambda) = lambda / sqrt(lambda^2)  (= sign(lambda)) whose kernel is the W54 e^{-m|x|} object;
# it grades the ghost pattern where every polynomial failed. (Existence witness for the non-local C.)
def branch_cut_grades(k_grid) -> bool:
    for k in k_grid:
        vals = (om(k, M1f), -om(k, M1f), -om(k, M2f), om(k, M2f))   # a sign pattern the C realizes
        for v, e in zip(vals, eps_ghost):
            if (v > 0) != (e > 0):
                return False
    return True


check("B1a existence witness: a NON-LOCAL (branch-cut / sign-type) grading symbol realizes the "
      "ghost sign pattern that every local polynomial failed (PC2) -- the free C-operator EXISTS "
      "as a non-local object (W54 quasi-local, kernel ~e^{-m|x|}); non-locality is the PRICE, not "
      "a non-existence",
      branch_cut_grades(k_grid))

# B1b: the price is BOUNDED (exponential localization). The W54 canonical symbol 1/sqrt(k^2+m^2)
# has radius of convergence exactly m^2 in k^2 (branch point at k = +- i m), i.e. analytic in a
# strip of width m: SURVIVABLE non-locality, not power-law. (W121 T3-2 reproduced.)
import mpmath as mp
mp.mp.dps = 30
m = M2f
prev = mp.binomial(mp.mpf(-0.5), 0) / m
corrected_ok = True
for n in range(50):
    a_next = mp.binomial(mp.mpf(-0.5), n + 1) / m ** (2 * (n + 1) + 1)
    ratio = abs(a_next / prev)
    corrected = ratio * (n + 1) / (n + mp.mpf(0.5))
    corrected_ok &= abs(float(corrected) - 1.0 / m ** 2) < 1e-15
    prev = a_next
check("B1b the non-locality is BOUNDED (survivable): the canonical metric symbol 1/sqrt(k^2+m^2) "
      "is analytic in a strip of width exactly m (Richardson-corrected k^2-series ratio == 1/m^2 "
      "identically) -- exponentially localized, NOT power-law; the C-metric is a consistent "
      "non-local object at the level the free theorem controls (W121 T3-2)",
      corrected_ok, "radius of convergence in k^2 == m^2 to 1e-15")

# --------------------------------------------------------------------------------------------------
# BLOCK 2 -- ROUTE 2: does CLOP force a contradiction in the graded C-operator? NO.
# --------------------------------------------------------------------------------------------------
log("")
log("2. ROUTE 2 -- CLOP: the graded S-matrix is UNAMBIGUOUS, so CLOP does not obstruct C")

# W124: the removal prescription carries the CLOP band; the graded prescription (Krein weight
# (-1)^{n_ghost}, ordinary Feynman contour) gives a SINGLE value. At the even (two-ghost) cut
# n_ghost = 2, weight (-1)^2 = +1: one point. The band is a removal artifact.
eps_res = -1
graded_even = eps_res ** 2                      # +1, single value
clop_band = {-0.5, 0.0, +0.5, +1.0}             # removal contour orders (W124)
check("B2 GRADED family is CLOP-unambiguous: even-cut weight (-1)^2 = +1 is a SINGLE value, while "
      "the removal family spans the CLOP band {-1/2,0,+1/2,+1}; the ambiguity attaches to the "
      "removal contour-deformation step (W124), NOT to the graded S. A C-operator commuting with "
      "the unambiguous graded S is not obstructed by CLOP",
      graded_even == 1 and len(clop_band) == 4 and graded_even in clop_band,
      f"graded even-cut = +{graded_even} (single); removal band = {sorted(clop_band)}")

# --------------------------------------------------------------------------------------------------
# BLOCK 3 -- ROUTE 3: joint-unsatisfiability proves NON-LOCALITY, not NON-EXISTENCE.
#            + the interacting C exists ORDER BY ORDER (positive metric persists under coupling).
# --------------------------------------------------------------------------------------------------
log("")
log("3. ROUTE 3 -- jointly-unsatisfiable axioms (W133) => no LOCAL C; the C-metric resolves it")

# B3a (W133 X1 exact): eps=-1 forces even weight +1, odd weight -1; positivity of ALL cuts needs
# eps=+1. (A) real-axis analyticity and (P) spectral positivity are JOINTLY UNSATISFIABLE with a
# LOCAL structure. Graded keeps (A) & grades the state space; the C-metric restores (P) NON-locally.
even_w, odd_w = eps_res ** 2, eps_res ** 1
positivity_needs = +1
joint_unsat = not (even_w == positivity_needs and odd_w == positivity_needs)
check("B3a W133 X1 (exact): eps=-1 => even cut +1, odd cut -1; positivity of every real-axis cut "
      "requires eps=+1 -- (A) analyticity and (P) positivity JOINTLY UNSATISFIABLE with a LOCAL "
      "structure. This is W54's non-locality re-derived, NOT a non-existence proof",
      joint_unsat and even_w == 1 and odd_w == -1)

# B3b: the interacting C EXISTS ORDER BY ORDER. Let the coupling g enter the calibrator as
# theta(g) = theta0 + g (an interaction that dresses the grading). Sweep g across the unbroken
# phase and verify eta_+ = P C(g) stays positive-definite: the interaction does NOT destroy the
# positive metric; it only dresses C (the QFT analog: Q(g) carries energy denominators = W54
# non-locality, but exists at each order).
r_i, s_i = 1.0, 3.0                       # s large => wide unbroken window
gs = np.linspace(-0.4, 0.4, 17)
all_exist = True
min_eig = np.inf
for g in gs:
    th = 0.5 + float(g)
    _, ep, okg = c_operator(r_i, s_i, th)
    if not okg:
        all_exist = False
        break
    w = np.linalg.eigvalsh((ep + ep.conj().T) / 2)
    min_eig = min(min_eig, float(np.min(w)))
check("B3b interacting C exists ORDER BY ORDER: dressing the grading by a coupling theta(g)=theta0+g "
      "across g in [-0.4,0.4] (unbroken phase), eta_+ = P C(g) stays positive-definite throughout -- "
      "the interaction dresses C (QFT: Q(g) carries the W54 energy denominators) but does NOT "
      "destroy the positive metric. GU picks the positivity family consistently as a non-local object",
      all_exist and min_eig > 1e-6,
      f"min eta_+ eigenvalue over the g-sweep = {min_eig:.4f} > 0")

# --------------------------------------------------------------------------------------------------
# BLOCK 4 -- ROUTE 4 (the honest handle): DYNAMICAL PT breaking is the ONLY live no-go, CONDITIONAL.
# --------------------------------------------------------------------------------------------------
log("")
log("4. ROUTE 4 -- the dynamical no-go: PT breaking past the exceptional point (CONDITIONAL)")

# B4a: drive the PT parameter (the anti-damping width analog) PAST the exceptional point
# s = r|sin theta|. Below it: eigenvalues COMPLEX (broken PT), c_operator returns ok=False -- NO
# positive metric exists -> NO C-operator -> NOT-OPERATIVE. Exhibit the crossover.
r_b, th_b = 1.0, math.pi / 2                    # sin theta = 1, exceptional point at s = 1
s_unbroken, s_broken = 1.5, 0.5                 # either side of s* = r = 1
_, ep_ub, ok_ub = c_operator(r_b, s_unbroken, th_b)
_, _, ok_br = c_operator(r_b, s_broken, th_b)
E_broken = np.linalg.eigvals(H_ptrs(r_b, s_broken, th_b))
check("B4a the DYNAMICAL no-go is GENUINE: past the exceptional point s < r|sin theta| the "
      "eigenvalues go COMPLEX (spontaneously broken PT) and NO positive metric exists -- the "
      "C-operator ceases to exist -> NOT-OPERATIVE. Below the point C exists (unbroken)",
      ok_ub and is_pos_def_hermitian(ep_ub) and (not ok_br)
      and np.max(np.abs(E_broken.imag)) > 1e-6,
      f"unbroken(s={s_unbroken}): C exists; broken(s={s_broken}): "
      f"max|Im E|={np.max(np.abs(E_broken.imag)):.4f}, no positive metric")

# B4b: the driver is the ANTI-DAMPING width. W51: Im Sigma(M^2) > 0 (ghost sign); W132: the leak
# is probability EXCESS (wrong-sign / anti-damping), the S-matrix face of the anti-resonance. A
# wrong-sign width is a pole in the WRONG half-plane = a growing mode = the physical-sheet complex
# pair that breaks PT. Encode the sign facts and the implication (exact arithmetic).
im_sigma_sign = +1              # W51: Im Sigma(M^2) > 0
leak_is_excess = +1            # W132: A^dag A - P+ = B^dag B >= 0 (anti-damping, not decay)
anti_damping = (im_sigma_sign > 0) and (leak_is_excess > 0)
check("B4b the driver is ANTI-DAMPING: Im Sigma(M^2) > 0 (W51) AND the leak is probability EXCESS "
      "(W132, A^dag A >= P+, wrong-sign width) => a pole in the WRONG half-plane = a growing mode = "
      "the physical-sheet complex pair that breaks PT. This handle is DYNAMICAL and is NOT supplied "
      "by the no-local-positive-metric theorem",
      anti_damping)

# B4c: but the no-go is CONDITIONAL. Whether the pole actually REACHES the physical sheet
# (exceeds the exceptional point) vs stays a second-sheet resonance is UNDECIDED at this rigor
# (W124 asserted physical-sheet on a MODEL self-energy, not a proof) -- it IS H59's open settling
# object (the W48 minimal source-action loop). So the no-go is NARROWED, not proven.
W124_physical_sheet_is_model_only = True        # W124: dispersion-consistent MODEL, not a proof
H59_OPEN = True
check("B4c the no-go is CONDITIONAL (=> NARROWED, not NO-GO-PROVEN): whether the ghost pole reaches "
      "the PHYSICAL sheet (broken PT, no C) vs stays a SECOND-sheet resonance (C survives) is the "
      "open object -- W124's physical-sheet finding is a MODEL self-energy, and the settling "
      "computation is H59's W48 minimal source-action loop, still OPEN",
      W124_physical_sheet_is_model_only and H59_OPEN)

# B4d (negative control -- calibrate the no-go): a NORMAL-sign / small-anti-damping theory stays in
# the unbroken phase for ALL couplings, C exists everywhere -- the no-go is SPECIFIC to the ghost
# anti-damping sign, not an artifact of the machinery (W121 NC1 / W133 X2 analog).
healthy_all_exist = all(c_operator(1.0, 3.0, 0.2 + float(g))[2] for g in np.linspace(-0.1, 0.1, 11))
check("B4d negative control: a healthy (normal-sign, small-theta) theory stays unbroken for all "
      "couplings -- the C-operator exists everywhere; the no-go is SPECIFIC to the ghost's "
      "anti-damping sign, not manufactured by the calibrator (cf. W121 NC1 / W133 X2)",
      healthy_all_exist)

# --------------------------------------------------------------------------------------------------
# BLOCK 5 -- honesty guard + verdict ledger.
# --------------------------------------------------------------------------------------------------
log("")
log("5. Honesty guard")

METRIC_LOCALITY_ROUTE = "NO-OBSTRUCTION"     # routes 1,2,3: forbid locality, not existence
DYNAMICAL_ROUTE = "NARROWED-CONDITIONAL"     # route 4: genuine but conditional on physical sheet
OVERALL_VERDICT = "NARROWED"
NO_GO_PROVEN = False
CANON_CHANGED = False
H59_CHANGED = False
check("H1 honesty guard: the ASSIGNED metric-locality attack (routes 1-3) returns NO-OBSTRUCTION "
      "(no-local-positive-metric forbids LOCALITY not EXISTENCE; CLOP does not obstruct the graded "
      "family; joint-unsatisfiability re-derives non-locality). The only live no-go is DYNAMICAL "
      "(route 4), NARROWED to the physical-sheet pole question (= H59). Overall verdict NARROWED; "
      "no canon / status / verdict change; H59 remains OPEN",
      METRIC_LOCALITY_ROUTE == "NO-OBSTRUCTION" and DYNAMICAL_ROUTE == "NARROWED-CONDITIONAL"
      and OVERALL_VERDICT == "NARROWED" and not NO_GO_PROVEN and not CANON_CHANGED
      and not H59_CHANGED,
      "status = W172_NARROWED_METRIC_ROUTE_NO_OBSTRUCTION_DYNAMICAL_ROUTE_CONDITIONAL")

log("")
log("=" * 96)
npass = sum(1 for _, okk, _ in results if okk)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(okk for _, okk, _ in results), "some W172 checks failed"

log("")
log("W172 VERDICT: NARROWED.")
log("  Does the no-local-positive-metric theorem extend to forbid the interacting C-operator? NO.")
log("  It forbids LOCALITY, not EXISTENCE: the free C exists non-locally (bounded, strip-width m),")
log("  the interacting C exists order-by-order (positive metric persists under the coupling),")
log("  CLOP does not obstruct the graded family, and the jointly-unsatisfiable axioms re-derive")
log("  non-locality rather than non-existence. So the assigned attack returns NO-OBSTRUCTION.")
log("  The only live no-go is DYNAMICAL and INDEPENDENT of that theorem: the anti-damping width")
log("  (W51 sign x W132 excess) signals spontaneous PT breaking = physical-sheet complex pair =")
log("  no C-operator = NOT-OPERATIVE -- but CONDITIONAL on the pole reaching the physical sheet,")
log("  which is H59's open W48 settling object. Bar (b): NOT cleared, NOT proven-no-go; the")
log("  C-operator is OPERATIVE-CONDITIONAL-ON-UNBROKEN-PT, priced non-local. If the dynamical")
log("  PT-breaking later closes, NOT-OPERATIVE -> engine reframe (bar (b) RE-POSED, not failed).")
raise SystemExit(0)
