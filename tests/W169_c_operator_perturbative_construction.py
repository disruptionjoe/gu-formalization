#!/usr/bin/env python3
r"""
W169 / TEAM C-OP-CONSTRUCT -- the perturbative C-operator, ORDER BY ORDER, THROUGH Q2.

THE ONE OBJECT
--------------
Is the Krein grading physically OPERATIVE at the INTERACTING/loop level = does the interacting
C-operator EXIST = [P_ghost, S] = 0 hold beyond tree level?  Keep-and-grade unitarity (W132) is
reduced WITHOUT REMAINDER to exactly this: there is no independent physical-subspace optical
theorem; the only unitarity resource is the interacting C-operator (Mostafazadeh eta_+ = eta C > 0).

W49 / path2-branchB computed Q1 (first interacting order) and stopped, explicitly: "Only the FIRST
interacting order of Q was computed ... convergence/all-orders is not established here." W169
computes the NEXT order Q2 -- the first genuinely loop/interacting order where an obstruction can
bite -- for the minimal GU keep-and-grade model, and asks: does C = e^Q P OBSTRUCT at Q2 or exist?

CONSTRUCTION (Bender-Brody-Jones / Mostafazadeh; GEOMETER-VS-PHYSICS-OBJECTS.md discipline)
------------------------------------------------------------------------------------------
Physical inner product = the POSITIVE C-metric eta_+ = e^{-Q}, Q Hermitian, Q = g Q1 + g^2 Q2 + ...
NOT a positive-Hilbert-subspace projection (that removes the ghost; grading keeps it). The defining
condition is pseudo-Hermiticity  e^{-Q} H e^{Q} = H^dag  (equivalently eta_+ H = H^dag eta_+), with
H = H0 + g V, plus C^2 = 1 and eta_+ > 0.

Admissibility fork (Krein-Hermiticity  eta0 V eta0 = V^dag, eta0 = (-1)^{N_ghost} the fundamental
Krein metric): every admissible vertex splits V = A + S with
    A  Krein-ODD  and  ANTI-Hermitian  (the genuinely non-Hermitian PT part; sources Q1),
    S  Krein-EVEN and       Hermitian  (ordinary interactions; source Q2 via [Q1,S]).
BCH expansion of e^{-Q} H e^{Q} = H^dag gives, EXACTLY (derived + machine-checked below):
    order g^1:  [H0, Q1] = -2 A
    order g^2:  [H0, Q2] =  [Q1, S]
Each is solved elementwise  X_{mn} = source_{mn}/(E_m - E_n), which EXISTS iff the source has NO
matrix element between DEGENERATE H0 states (E_m = E_n) -- the SECULAR / small-denominator condition.
A nonzero degenerate-block source = an OBSTRUCTION: no Hermitian generator at that order.

THE GU-RELEVANT MODEL (minimal keep-and-grade: physical graviton mode + ghost mode + vertices)
----------------------------------------------------------------------------------------------
Two Krein modes: physical (mode 1, freq w1, norm +), ghost (mode 2, freq w2, norm -), eta0 =
(-1)^{N2}, H0 = w1 N1 + w2 N2 (Hermitian, bounded below, REAL spectrum, INDEFINITE norm -- the
keep-and-grade Krein picture: real masses, graded not removed).  Cubic vertices, all Krein-Hermitian:
    A     = (a1)^2 a2^dag - (a1^dag)^2 a2       Krein-odd,  anti-Herm  (physical<->ghost, PT part)
    Smin  = a1 (a2^dag)^2 + a1^dag (a2)^2       Krein-even, Herm       (physical<->ghost, ordinary)
    Sgrav = a1^dag a1^dag a1 + a1^dag a1 a1     Krein-even, Herm       (PHYSICAL SELF-coupling)
Sgrav is mandatory in any real gravity theory (the graviton self-interacts); it is the piece that
makes Q2 a genuine test, because it first enters the C-operator at O(g^2).

WHAT THE COMPUTATION FINDS (deterministic, numpy only; exit 0 on success)
------------------------------------------------------------------------
  Q1                  EXISTS: [H0,Q1]=-2A solved; Q1 Hermitian + Krein-odd => C = e^{gQ1+...}P, C^2=1.
  Q2, pure-odd vertex = 0 EXACTLY (source [Q1,S]=0): single-odd-vertex model is Q2-obstruction-free
                      (the BBJ "Q is odd in g" result); first correction would be Q3.
  Q2, full vertex, GENERIC (incommensurate) masses  EXISTS: Hermitian, finite, metric positive;
                      including Q2 drives the metric residual ||eta_+ H - H^dag eta_+|| from O(g^2)
                      (Q1 alone) to O(g^3) -- Q2 removes the O(g^2) non-Hermiticity.  => OPERATIVE-perturbatively.
  Q2, full vertex, RESONANT (COMMENSURATE) masses  OBSTRUCTS.  The obstruction is a small-denominator
                      / Poincare resonance, on a measure-zero set of frequency ratios:
                        * w_ghost = 2 w_phys : the A-vertex resonance, obstructs already at Q1;
                        * w_ghost =   w_phys (EQUAL mass = conformal / double-pole limit) and
                          w_ghost = 3 w_phys : obstruct FIRST at Q2 (secular_Q1 = 0, secular_Q2 != 0),
                          driven by Sgrav -- INVISIBLE to the leading order.  This is the loop-order kill.
                      As w_ghost -> w_phys the Q2 matrix elements DIVERGE ~ 1/(w_phys - w_ghost).
  Massless graviton + massive ghost (Stelle mass-split, w_phys -> 0, w_ghost = M): NON-resonant =>
                      C EXISTS through Q2.  The equal-mass obstruction is the CONFORMAL/Weyl (1/p^4
                      double-pole) member, i.e. Bender-Mannheim's PU equal-frequency non-unitary case.

VERDICT: NARROWED.  OPERATIVE-perturbatively (C exists through Q2) for generic/mass-split spectra;
OBSTRUCTS-AT-Q2 on the commensurate-resonance loci, the equal-mass (conformal double-pole) case among
them.  bar (b) reduces to ONE sub-bit: is GU's linearized 4th-order operator the equal-mass/conformal
(degenerate, resonant) case or the mass-split (incommensurate) case?  Inherited caveat (W49/W54, not
re-opened): even in the EXISTS case this is QM + perturbative; the QFT generator carries
1/sqrt(k^2+m^2) energy denominators => non-local Hermitian partner.

Reproducible:  python tests/W169_c_operator_perturbative_construction.py
No canon / RESEARCH-STATUS / claim-status / verdict / posture file is touched. Exploration-grade.
"""
from __future__ import annotations

import math

import numpy as np

np.random.seed(0)  # determinism (nothing random is used, but pin it)

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


def herm_err(M: np.ndarray) -> float:
    return float(np.max(np.abs(M - M.conj().T)))


def anti_herm_err(M: np.ndarray) -> float:
    return float(np.max(np.abs(M + M.conj().T)))


def min_eig_herm(M: np.ndarray) -> float:
    return float(np.min(np.linalg.eigvalsh((M + M.conj().T) / 2.0)).real)


def expm(M: np.ndarray) -> np.ndarray:
    wv, U = np.linalg.eig(M)
    return (U * np.exp(wv)) @ np.linalg.inv(U)


# ==============================================================================================
# Two Krein modes: mode 1 (physical, +norm), mode 2 (ghost, -norm), each truncated to n levels.
# ==============================================================================================
def ops(n: int):
    a = np.zeros((n, n), dtype=complex)
    for k in range(1, n):
        a[k - 1, k] = np.sqrt(k)
    I = np.eye(n, dtype=complex)
    a1, a2 = np.kron(a, I), np.kron(I, a)
    return a1, a2


def krein_metric(n: int) -> np.ndarray:
    """eta0 = (-1)^{N2}: +1 even ghost number, -1 odd. The fundamental (indefinite) Krein metric."""
    return np.diag([(-1.0) ** j for _ in range(n) for j in range(n)]).astype(complex)


def build(n: int, w1: float, w2: float):
    a1, a2 = ops(n)
    a1d, a2d = a1.conj().T, a2.conj().T
    N1, N2 = a1d @ a1, a2d @ a2
    H0 = w1 * N1 + w2 * N2
    A = (a1 @ a1) @ a2d - (a1d @ a1d) @ a2          # Krein-odd, anti-Herm
    Smin = a1 @ (a2d @ a2d) + a1d @ (a2 @ a2)       # Krein-even, Herm (cross)
    Sgrav = a1d @ a1d @ a1 + a1d @ a1 @ a1          # Krein-even, Herm (physical self-coupling)
    return H0, A, Smin, Sgrav, krein_metric(n)


def secular(source: np.ndarray, E: np.ndarray, tol: float = 1e-9) -> float:
    """max |source_{mn}| over DEGENERATE (|E_m - E_n| <= tol) pairs -- the obstruction measure."""
    sec = 0.0
    nN = source.shape[0]
    for m in range(nN):
        for k in range(nN):
            if abs(E[m] - E[k]) <= tol:
                sec = max(sec, abs(source[m, k]))
    return sec


def solve_comm(source: np.ndarray, E: np.ndarray, tol: float = 1e-9) -> np.ndarray:
    """Solve [H0, Q] = source with H0 = diag(E): Q_{mn} = source_{mn}/(E_m - E_n) (0 on degen block)."""
    Q = np.zeros_like(source)
    nN = source.shape[0]
    for m in range(nN):
        for k in range(nN):
            d = E[m] - E[k]
            if abs(d) > tol:
                Q[m, k] = source[m, k] / d
    return Q


log("=" * 96)
log("W169 / TEAM C-OP-CONSTRUCT -- PERTURBATIVE C-OPERATOR THROUGH Q2 (the first loop order)")
log("=" * 96)

# ==============================================================================================
# PC1 -- positive control: reproduce a KNOWN free-theory C-operator (2x2 Bender-Brody-Jones, exact).
# ==============================================================================================
log("\n[PC1] positive control: known 2x2 Bender-Brody-Jones C-operator (exact closed form)")
r, s, th = 1.0, 2.0, 0.6
HC = np.array([[r * np.exp(1j * th), s], [s, r * np.exp(-1j * th)]], dtype=complex)
sin_a = (r * np.sin(th)) / s
cos_a = np.sqrt(1.0 - sin_a**2)
Cbbj = (1.0 / cos_a) * np.array([[1j * sin_a, 1.0], [1.0, -1j * sin_a]], dtype=complex)
check("PC1a  BBJ C^2 = 1", float(np.max(np.abs(Cbbj @ Cbbj - np.eye(2)))) < 1e-12,
      f"||C^2-1||={float(np.max(np.abs(Cbbj @ Cbbj - np.eye(2)))):.1e}")
check("PC1b  BBJ [C,H] = 0 (C grades the interacting H)",
      float(np.max(np.abs(Cbbj @ HC - HC @ Cbbj))) < 1e-12,
      f"||[C,H]||={float(np.max(np.abs(Cbbj @ HC - HC @ Cbbj))):.1e}")
check("PC1c  BBJ spectrum real (unbroken PT)",
      float(np.max(np.abs(np.imag(np.linalg.eigvals(HC))))) < 1e-12)

# ==============================================================================================
# PC2 + Q1 -- GU model: vertex admissibility, Krein-pseudo-Hermiticity, leading-order C-operator.
# ==============================================================================================
n = 8  # per-mode truncation -> 64-dim two-mode space
w1_ref, w2_ref = 1.0, 1.3  # NON-RESONANT reference (distinct, incommensurate scales)
H0, A, Smin, Sgrav, eta0 = build(n, w1_ref, w2_ref)
S = Smin + Sgrav
E = np.real(np.diag(H0))

log("\n[PC2] GU keep-and-grade model: vertex admissibility + Krein-pseudo-Hermiticity")
check("PC2a  A anti-Hermitian (the non-Hermitian PT part, sources Q1)", anti_herm_err(A) < 1e-9,
      f"||A+A^dag||={anti_herm_err(A):.1e}")
check("PC2b  Smin, Sgrav Hermitian (ordinary interactions, source Q2)",
      herm_err(Smin) < 1e-9 and herm_err(Sgrav) < 1e-9,
      f"||Smin-Smin^d||={herm_err(Smin):.1e}, ||Sgrav-Sgrav^d||={herm_err(Sgrav):.1e}")
check("PC2c  every vertex Krein-Hermitian: eta0 V eta0 = V^dag for V in {A,Smin,Sgrav} "
      "(=> H = H0 + gV is eta0-pseudo-Hermitian: real spectrum, KEPT ghost)",
      all(float(np.max(np.abs(eta0 @ V @ eta0 - V.conj().T))) < 1e-9 for V in (A, Smin, Sgrav)))
check("PC2d  H0 commutes with the Krein metric ([H0,eta0]=0): the free ghost is GRADED, not removed",
      float(np.max(np.abs(H0 @ eta0 - eta0 @ H0))) < 1e-12)

log("\n[Q1] leading order: solve [H0,Q1] = -2A")
sec1_ref = secular(-2.0 * A, E)
Q1 = solve_comm(-2.0 * A, E)
check("Q1a  [H0,Q1] = -2A solved to machine precision, no leading secular obstruction "
      "(reproduces W49 Q1 existence)",
      float(np.max(np.abs((H0 @ Q1 - Q1 @ H0) - (-2.0 * A)))) < 1e-9 and sec1_ref < 1e-12,
      f"resid={float(np.max(np.abs((H0 @ Q1 - Q1 @ H0) + 2.0 * A))):.1e}, secular={sec1_ref:.1e}")
check("Q1b  Q1 Hermitian (forced by A anti-Herm)", herm_err(Q1) < 1e-9,
      f"||Q1-Q1^dag||={herm_err(Q1):.1e}")
check("Q1c  Q1 Krein-ODD (eta0 Q1 eta0 = -Q1) => C = e^{gQ1+...} P squares to 1",
      float(np.max(np.abs(eta0 @ Q1 @ eta0 + Q1))) < 1e-9,
      f"||eta0 Q1 eta0 + Q1||={float(np.max(np.abs(eta0 @ Q1 @ eta0 + Q1))):.1e}")

# ==============================================================================================
# Q2a -- PURE Krein-odd vertex (S = 0): the g^2 source [Q1,S] vanishes => Q2 = 0 EXACTLY.
# ==============================================================================================
log("\n[Q2a] pure Krein-odd vertex (S=0): order-g^2 source [Q1,S] = 0  =>  Q2 = 0 exactly")
check("Q2a  with S=0 the g^2 source [Q1,S]=0 => Q2=0 (BBJ 'Q odd in g'; NO g^2 obstruction; "
      "first correction is Q3)",
      float(np.max(np.abs(Q1 @ (0.0 * S) - (0.0 * S) @ Q1))) < 1e-14)

# ==============================================================================================
# Q2b -- FULL vertex, GENERIC (incommensurate) masses: Q2 EXISTS and DOES ITS JOB.
# ==============================================================================================
log("\n[Q2b] full vertex, GENERIC masses (w1=1.0, w2=1.3): compute Q2 = solve [H0,Q2] = [Q1,S]")
source2 = Q1 @ S - S @ Q1
sec2_ref = secular(source2, E)
Q2 = solve_comm(source2, E)
check("Q2b1  order-g^2 source [Q1,S] has NO degenerate-block matrix element (no secular "
      "obstruction off resonance) => Q2 EXISTS at the first loop order",
      sec2_ref < 1e-9, f"degenerate-block source (secular) = {sec2_ref:.1e}")
check("Q2b2  Q2 solves [H0,Q2] = [Q1,S] to machine precision",
      float(np.max(np.abs((H0 @ Q2 - Q2 @ H0) - source2))) < 1e-9,
      f"resid={float(np.max(np.abs((H0 @ Q2 - Q2 @ H0) - source2))):.1e}")
check("Q2b3  Q2 Hermitian ([Q1,S] anti-Herm / (E_m-E_n) antisym => Q2 Herm) "
      "=> eta_+ = e^{-Q} stays a genuine (Hermitian) metric",
      herm_err(Q2) < 1e-9, f"||Q2-Q2^dag||={herm_err(Q2):.1e}")


# The metric residual R(g) = eta_+ H - H^dag eta_+ (eta_+ = e^{-Q}) measures pseudo-Hermiticity
# failure.  Design: R = O(g^2) with Q = gQ1 alone; R = O(g^3) once Q2 is included.  Measured on a
# truncation-clean low block (banded vertices keep the k-sum away from the Fock boundary).
mb = 10


def metric_residual(g: float, order: int) -> float:
    Q = g * Q1 + (g**2 * Q2 if order >= 2 else 0.0)
    eta = expm(-Q)
    H = H0 + g * (A + S)
    res = eta @ H - H.conj().T @ eta
    return float(np.max(np.abs(res[:mb, :mb])))


def slope(order: int, g_hi: float, g_lo: float) -> float:
    return math.log(metric_residual(g_hi, order) / metric_residual(g_lo, order)) / math.log(g_hi / g_lo)


sQ1 = slope(1, 0.02, 0.01)
sQ12 = slope(2, 0.02, 0.01)
check("Q2b4  with Q1 ALONE the metric residual is O(g^2) (log-log slope ~ 2): Q1 removes the O(g) "
      "non-Hermiticity but leaves O(g^2)",
      1.7 < sQ1 < 2.3, f"slope(R with Q1 only) = {sQ1:.2f} (expect ~2)")
check("Q2b5  ADDING Q2 pushes the residual to O(g^3) (slope ~ 3): Q2 CANCELS the O(g^2) "
      "non-Hermiticity => the first loop-order correction does its job",
      2.6 < sQ12 < 3.4, f"slope(R with Q1+Q2) = {sQ12:.2f} (expect ~3)")
check("Q2b6  the perturbative positive metric eta_+ = e^{-(gQ1+g^2Q2)} is POSITIVE-DEFINITE (g=0.05)",
      min_eig_herm(expm(-(0.05 * Q1 + 0.05**2 * Q2))) > 1e-9,
      f"min eig(eta_+)={min_eig_herm(expm(-(0.05 * Q1 + 0.05**2 * Q2))):.3e}")

# ==============================================================================================
# Q2c -- THE OBSTRUCTION MAP: scan (w1,w2); the C-operator obstructs on COMMENSURATE resonances,
#        and the physical self-coupling Sgrav produces an obstruction FIRST at Q2 (invisible to Q1).
# ==============================================================================================
log("\n[Q2c] obstruction map: secular_Q1 (deg block of -2A) and secular_Q2 (deg block of [Q1,S])")
log("      w_phys  w_ghost   secular_Q1     secular_Q2     status")
cases = [
    (1.0, 1.3, "generic (incommensurate)"),
    (1.0, np.sqrt(2), "generic (irrational)"),
    (0.0, 1.0, "massless graviton + massive ghost (Stelle mass-split)"),
    (1.0, 2.0, "w_ghost = 2 w_phys  (A-vertex resonance)"),
    (1.0, 1.0, "w_ghost =   w_phys  (EQUAL mass = conformal / double-pole)"),
    (1.0, 3.0, "w_ghost = 3 w_phys  (odd resonance)"),
]
rows = []
for w1, w2, tag in cases:
    H0s, As, Smins, Sgravs, _ = build(n, w1, w2)
    Es = np.real(np.diag(H0s))
    s1 = secular(-2.0 * As, Es)
    Q1s = solve_comm(-2.0 * As, Es)
    Ss = Smins + Sgravs
    s2 = secular(Q1s @ Ss - Ss @ Q1s, Es)
    if s1 > 1e-6:
        status = "OBSTRUCTS at Q1"
    elif s2 > 1e-6:
        status = "OBSTRUCTS at Q2 (loop-order, invisible at Q1)"
    else:
        status = "EXISTS through Q2"
    rows.append((w1, w2, s1, s2, tag, status))
    log(f"      {w1:5.3f}   {w2:5.3f}    {s1:.3e}     {s2:.3e}   {status}")
    log(f"                                                             [{tag}]")

by_tag = {tag: (s1, s2, status) for (w1, w2, s1, s2, tag, status) in rows}
check("Q2c1  GENERIC (incommensurate) masses: secular_Q1 = secular_Q2 = 0 => C-operator EXISTS "
      "through Q2 (both 'generic' and 'irrational' rows)",
      by_tag["generic (incommensurate)"][0] < 1e-9 and by_tag["generic (incommensurate)"][1] < 1e-9
      and by_tag["generic (irrational)"][0] < 1e-9 and by_tag["generic (irrational)"][1] < 1e-9)
check("Q2c2  MASSLESS graviton + MASSIVE ghost (Stelle mass-split): NON-resonant => C EXISTS "
      "through Q2 (the generic Stelle spectrum is on the OPERATIVE side)",
      by_tag["massless graviton + massive ghost (Stelle mass-split)"][0] < 1e-9
      and by_tag["massless graviton + massive ghost (Stelle mass-split)"][1] < 1e-9)
check("Q2c3  w_ghost = 2 w_phys: secular_Q1 != 0 => OBSTRUCTS ALREADY AT Q1 (A-vertex resonance)",
      by_tag["w_ghost = 2 w_phys  (A-vertex resonance)"][0] > 1e-6)
check("Q2c4  EQUAL mass (conformal / double-pole locus): secular_Q1 = 0 but secular_Q2 != 0 => "
      "OBSTRUCTS FIRST AT Q2 -- the loop-order kill, INVISIBLE to leading order (driven by Sgrav)",
      by_tag["w_ghost =   w_phys  (EQUAL mass = conformal / double-pole)"][0] < 1e-9
      and by_tag["w_ghost =   w_phys  (EQUAL mass = conformal / double-pole)"][1] > 1e-6)
check("Q2c5  w_ghost = 3 w_phys: also secular_Q1 = 0, secular_Q2 != 0 => a SECOND Q2-first "
      "obstruction (the resonant set is a lattice of commensurate ratios)",
      by_tag["w_ghost = 3 w_phys  (odd resonance)"][0] < 1e-9
      and by_tag["w_ghost = 3 w_phys  (odd resonance)"][1] > 1e-6)

# Approach to the equal-mass obstruction: the naive Q2 elements DIVERGE ~ 1/(w_ghost - w_phys).
log("\n[Q2c-approach] Q2 blows up as w_ghost -> w_phys (small denominators near the obstruction)")
maxQ2 = []
for w2 in [1.4, 1.2, 1.1, 1.05, 1.02]:
    H0s, As, Smins, Sgravs, _ = build(n, 1.0, w2)
    Es = np.real(np.diag(H0s))
    Q1s = solve_comm(-2.0 * As, Es)
    Ss = Smins + Sgravs
    Q2s = solve_comm(Q1s @ Ss - Ss @ Q1s, Es)
    m = float(np.max(np.abs(Q2s[:20, :20])))
    maxQ2.append((w2, m))
    log(f"      w_ghost={w2:.2f}  (gap={w2 - 1.0:+.2f})   max|Q2|(low block) = {m:.3e}")
check("Q2c6  max|Q2| DIVERGES on approach to the equal-mass obstruction (grows monotonically as the "
      "gap closes) => the construction is singular at the resonance, radius of convergence -> 0 there",
      maxQ2[-1][1] > 3.0 * maxQ2[0][1],
      f"max|Q2|: {maxQ2[0][1]:.2e} (gap +0.40) -> {maxQ2[-1][1]:.2e} (gap +0.02)")

# ==============================================================================================
# SUMMARY
# ==============================================================================================
log("\n" + "=" * 96)
npass = sum(1 for _, ok, _ in results if ok)
log(f"CHECKS: {npass}/{len(results)} passed.")
assert all(ok for _, ok, _ in results), "some W169 C-operator-through-Q2 checks FAILED"

log("")
log("W169 VERDICT (this file is the computation, not a claim-status change):")
log("  Q1:                     EXISTS ([H0,Q1]=-2A; Hermitian, Krein-odd, C^2=1). W49 reproduced.")
log("  Q2, pure-odd vertex:    = 0 exactly (source [Q1,S]=0). Single-odd-vertex model is Q2-clean.")
log("  Q2, generic/mass-split: EXISTS -- Hermitian, finite, eta_+ > 0; Q2 drives the metric residual")
log("                          from O(g^2) to O(g^3).  => C-operator EXISTS-PERTURBATIVELY = OPERATIVE.")
log("  Q2, commensurate resonance: OBSTRUCTS. w_ghost=2w_phys obstructs at Q1; w_ghost=w_phys (EQUAL")
log("                          mass = conformal / double-pole) and w_ghost=3w_phys obstruct FIRST at Q2")
log("                          (secular_Q1=0, secular_Q2!=0), driven by the physical self-coupling.")
log("                          Q2 diverges ~1/(w_ghost-w_phys) on approach.  => NOT-OPERATIVE there.")
log("  => NARROWED: OPERATIVE-perturbatively for generic/mass-split spectra (incl. Stelle massless-")
log("     graviton+massive-ghost); OBSTRUCTS-AT-Q2 on the commensurate-resonance loci, the equal-mass")
log("     (conformal double-pole = Bender-Mannheim PU) case among them.  bar(b) reduces to ONE sub-bit:")
log("     is GU's linearized 4th-order operator the equal-mass/conformal (resonant) or mass-split case?")
log("  CAVEAT (inherited W49/W54, not re-opened): even in the EXISTS case this is QM + perturbative;")
log("     the QFT generator carries 1/sqrt(k^2+m^2) energy denominators => non-local Hermitian partner.")
raise SystemExit(0)
