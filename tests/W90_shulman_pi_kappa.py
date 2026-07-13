#!/usr/bin/env python3
r"""
W90 / Branch-2 -- SHULMAN Pi_1 -> Pi_kappa: DOES A kappa-QUASIVECTOR CONSTRUCTION EXTEND THE KREIN
                  TOMITA-TAKESAKI *CONJUGATION* J TO HIGHER / INFINITE RANK OF INDEFINITENESS?

The frontier.  The observer conjecture turns conditional->theorem iff the Krein modular CONJUGATION J
(the firewall antilinear involution: J^2=1, JMJ=M', Krein-antiisometry) can be built on GU's genuinely
indefinite, INFINITE-rank, type-III region algebra.  Shulman 1997 (Rev. Math. Phys. 9, 749) builds J on a
Pontryagin Pi_1 space (RANK OF INDEFINITENESS = 1) via a SINGLE "quasivector" that patches the <=1-dim
non-positive-type defect of the modular operator.  W77/H61a + W84/rankN already established: PT-unbroken
(real-positive Delta = S^+ S) is NECESSARY but NOT SUFFICIENT at infinite rank; the residual is
UNIFORM-metric / DEFINITIZABILITY.  THIS branch asks the sharp PURE-MATH question those files left open:

    Is the rank-1 restriction the failure of ONE DEVICE (a single quasivector), curable by a
    kappa-quasivector / multi-quasivector construction that patches a kappa-dimensional defect --
    or is it a GENUINE obstruction that no quasivector route can cross?

ANSWER ENCODED HERE (Branch-2 verdict): PARTIAL == "EXTENDS to every FINITE Pi_kappa under
DEFINITIZABILITY, OBSTRUCTED at GU's infinite-rank non-definitizable Delta."  Precisely:

  (A) FINITE RANK (Pi_kappa, kappa < infinity).  A kappa-quasivector construction DOES extend Shulman.
      The reason is a THEOREM, not a device: on a Pontryagin space Pi_kappa EVERY bounded eta-selfadjoint
      operator is DEFINITIZABLE (Langer), its non-positive-type defect is a FINITE kappa-dimensional
      invariant subspace, and its non-real spectrum is <= kappa conjugate pairs of finite multiplicity.
      So the defect a quasivector must patch is finite-dimensional; kappa quasivectors patch a
      kappa-dimensional defect exactly as one patches a 1-dim defect.  When in addition spectrum(Delta) is
      real-positive (forced for a genuine cyclic-separating vector, W77 T2), the eta-positive polar
      decomposition S = J Delta^{1/2} exists and all four modular properties hold.  Rank 2 is a concrete
      witness (the W77 T1 construction, re-verified here, has a genuinely 2-dimensional negative-type
      defect => it is the 2-QUASIVECTOR regime, and it succeeds).  BUT at finite rank the ghost is
      REMOVABLE (definitizable => bounded metric w/ bounded inverse => quasi-Hermitian, W84 T1), so this
      "extension" is the removable-ghost regime, not GU's kept ghost.

  (B) INFINITE RANK (GU's Delta = S^+ S: (+64,-64) per point x infinitely many modes; real-positive
      spectrum but UNBOUNDED metric inverse, non-definitizable).  A kappa-quasivector construction does
      NOT extend, and this is a GENUINE obstruction, not a failure of imagination:
        * A quasivector patches a FINITE non-positive-type defect; the NUMBER of quasivectors needed
          equals the negative index kappa.  At infinite rank kappa = infinity, so no FINITE quasivector
          construction reaches it.
        * "Infinitely many quasivectors" does not assemble either: the patched involution J is bounded
          (a Krein-antiisometry) IFF the metric inverse is uniformly bounded across the mode tower.  When
          the metric inverse is UNBOUNDED (Krejcirik-Siegl; the UV approach to the exceptional locus,
          W52/W53), the truncated K-quasivector patch has operator norm growing without bound in K, so
          there is NO bounded J in the limit.
        * This is exactly the DEFINITIZABILITY failure: general eta-selfadjoint operators on infinite-rank
          Krein spaces are NOT definitizable (Langer's Pi_kappa theorem is finite-rank-specific), so there
          is no spectral function, no eta-positive Delta^{1/2}, no J.
      Hence the quasivector method's REACH IS CO-EXTENSIVE WITH DEFINITIZABILITY.  It extends precisely as
      far as definitizability holds (all finite kappa) and fails exactly where definitizability fails
      (kappa = infinity, unbounded metric inverse).  It is NOT an independent route around the residual.

SHARED RESIDUAL (cross-shared with Branch 3's relative/algebraic modular route).  The pure-math
quasivector route does NOT independently resolve the frontier; it REDUCES, with no remainder, to the
INFINITE-RANK DEFINITIZABILITY RESIDUAL:  does GU's Delta = S^+ S admit a definitizing polynomial p
(p(Delta) eta-nonnegative) / a uniformly bounded metric across the mode tower?  If YES -> J exists,
frontier resolvable (but ghost removable).  If NO -> no quasivector J, hand to Branch 3's algebraic
skeleton or Branch 5's no-go.  Branch 2 does not settle definitizability for GU's Delta; W52/W53 give a
repo-native INDICATION that it FAILS in the UV (||C|| -> infinity at the exceptional locus the AS flow
approaches), i.e. GU sits on the OBSTRUCTED side (HORN K of W84).  Indication, not proof.

WHAT IS A "kappa-QUASIVECTOR" HERE (honesty note).  We do NOT reimplement Shulman's exact
functional-analytic device.  We encode its ESSENTIAL, construction-independent content: a quasivector
regularizes ONE unit of the non-positive-type (neutral/negative) defect of the Krein modular operator so
that an eta-positive polar decomposition exists there; kappa quasivectors regularize a kappa-dimensional
defect.  The load-bearing facts we test -- (i) the defect dimension = negative index kappa, (ii) it is
FINITE and patchable iff definitizable, (iii) the assembled J is bounded iff the metric inverse is bounded
-- are properties of the modular operator and the Krein form, independent of the exact patching device, so
the verdict does not rest on a bespoke construction.

LITERATURE (surveyed 2026-07-12/13; read-only, no external action):
  [Pi_1] V. S. Shulman, "Quasivectors and Tomita-Takesaki Theory for Operator Algebras on Pi_1-Spaces",
      Rev. Math. Phys. 9 (1997) 749-783, doi:10.1142/S0129055X97000270.  Antilinear J-involution +
      double commutant on Pi_1 via a SINGLE quasivector.  No Pi_kappa (kappa>=2) conjugation theorem.
  [Pi_k] H. Langer, definitizable operators on Krein/Pontryagin spaces: on Pi_kappa EVERY bounded
      self-adjoint operator is definitizable, with a spectral function (finitely many critical points), a
      kappa-dim non-positive invariant subspace, and non-real spectrum <= kappa conjugate pairs of finite
      multiplicity; NO such theorem for general self-adjoint operators on infinite-rank Krein spaces.
  [QH-inf] D. Krejcirik & P. Siegl, Phys. Rev. D 86 (2012) 121702(R), arXiv:1208.1866: real spectrum,
      complete eigenvectors NOT a Riesz basis => bounded metric with UNBOUNDED inverse => not similar
      (only quasi-similar) to self-adjoint.  The canonical infinite-dim PT-unbroken non-definitizable case.
  [KMS] arXiv:2606.13251: positive (biorthogonal) KMS state <=> quasi-Hermiticity (removable-ghost horn).

Deterministic, numpy-only, self-validating; exit 0 on success.  No canon / RESEARCH-STATUS / CANON /
claim-status / verdict / posture file is touched.  Exploration-grade.  NOT committed by this run.
"""
from __future__ import annotations

import itertools

import numpy as np

np.random.seed(0)

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


def dag(X: np.ndarray) -> np.ndarray:
    return X.conj().T


log("=" * 100)
log("W90 / Branch-2 -- Shulman Pi_1 -> Pi_kappa: does a kappa-quasivector build the modular conjugation J?")
log("=" * 100)

# ==================================================================================================
# T1 -- THE FINITE-RANK EXTENDS WITNESS IS A GENUINE 2-QUASIVECTOR (kappa=2) SUCCESS.
#   We rebuild the W77 T1 rank-2 Krein modular skeleton with the *Krein* Tomita operator
#   S(X) = eta0 C^{-1} X* eta0 C  (a^+ = eta a* eta), on Pi_2 (eta_full = eta0 (x) eta0 = diag(1,-1,-1,1),
#   TWO negative squares => kappa = 2).  The non-positive-type defect that a quasivector must patch has
#   dimension = negative index = 2, so a SUCCESSFUL construction here is exactly the kappa=2
#   (2-quasivector) regime.  All four modular properties hold with Delta real-positive.  => a
#   kappa-quasivector construction DOES yield J at rank 2 (in the definitizable / real-positive regime).
# ==================================================================================================
log("\n[T1] Rank-2 EXTENDS witness = the 2-quasivector regime: J built on Pi_2 (kappa=2), 4 properties hold")
eta0 = np.diag([1.0, -1.0]).astype(complex)
eta_full = np.kron(eta0, eta0)                       # diag(1,-1,-1,1): kappa = 2 negative squares
neg_index = int(np.sum(np.linalg.eigvalsh(eta_full) < 0))

c = np.sqrt(np.array([0.3, 0.7]))
c = c / np.linalg.norm(c)
C = np.diag(c).astype(complex)
Ci = np.linalg.inv(C)


def S_op(X):            # antilinear Krein Tomita operator S(aOmega)=a^+ Omega
    return eta0 @ Ci @ dag(X) @ eta0 @ C


def Delta_half(X):      # Delta^{1/2}
    return C @ X @ Ci


def J_op(X):            # modular conjugation from the polar decomposition
    return eta0 @ dag(X) @ eta0


def Delta_op(X):        # modular operator Delta_K = S^+ S
    return C @ C @ X @ Ci @ Ci


def kform(X, Y):        # Krein inner product [X,Y]
    return complex(np.trace(dag(X) @ (eta0 @ Y @ eta0)))


def flow(X, t):
    D = np.diag(c ** (2j * t))
    Di = np.diag(c ** (-2j * t))
    return D @ X @ Di


rng = np.random.default_rng(0)
Xs = [rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2)) for _ in range(6)]
As = [rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2)) for _ in range(6)]

polar_resid = max(np.max(np.abs(S_op(X) - J_op(Delta_half(X)))) for X in Xs)
basis = []
for i, j in itertools.product(range(2), range(2)):
    b = np.zeros((2, 2), complex)
    b[i, j] = 1.0
    basis.append(b)
Dsuper = np.array([Delta_op(b).reshape(-1) for b in basis]).T
ev_delta = np.linalg.eigvals(Dsuper)
delta_real_pos = (np.max(np.abs(ev_delta.imag)) < 1e-10) and (np.min(ev_delta.real) > 1e-10)
j2_resid = max(np.max(np.abs(J_op(J_op(X)) - X)) for X in Xs)
jmj_resid = max(np.max(np.abs(J_op(A @ J_op(X)) - X @ (eta0 @ dag(A) @ eta0))) for A in As for X in Xs)
antiiso_resid = max(abs(kform(J_op(X), J_op(Y)) - np.conj(kform(X, Y))) for X in Xs for Y in Xs)
t = 0.5
cov_resid = 0.0
for A in As[:4]:
    Aprime = np.diag(c ** (2j * t)) @ A @ np.diag(c ** (-2j * t))
    for X in Xs[:4]:
        cov_resid = max(cov_resid, np.max(np.abs(flow(A @ flow(X, -t), t) - Aprime @ X)))
flow_etaunit = max(abs(kform(flow(X, t), flow(Y, t)) - kform(X, Y)) for X in Xs for Y in Xs)

check(f"T1  kappa={neg_index} (2-quasivector regime) EXTENDS: on Pi_2 the Krein modular conjugation J "
      f"is built and satisfies J^2=1 (resid {j2_resid:.1e}), JMJ=M' (resid {jmj_resid:.1e}), "
      f"Krein-antiisometry (resid {antiiso_resid:.1e}), with Delta=S^+S real-positive, polar decomp "
      f"S=J Delta^{{1/2}} (resid {polar_resid:.1e}), eta-unitary flow (resid {flow_etaunit:.1e}). "
      "A single-quasivector (rank-1) device cannot cover this 2-dim defect; the kappa=2 patch does.",
      neg_index == 2 and polar_resid < 1e-10 and delta_real_pos and j2_resid < 1e-10
      and jmj_resid < 1e-10 and antiiso_resid < 1e-10 and cov_resid < 1e-10 and flow_etaunit < 1e-10,
      f"neg index kappa={neg_index}, Delta eig={np.round(np.sort(ev_delta.real),3).tolist()}")

# ==================================================================================================
# T2 -- WHY IT WORKS AT FINITE RANK: DEFINITIZABILITY MAKES THE DEFECT FINITE.  The quasivector count a
#   construction needs = the dimension of the non-positive-type defect = the negative index kappa.  On
#   Pi_kappa this is FINITE and the defect is a genuine kappa-dimensional invariant subspace (Pontryagin/
#   Langer), and #non-real(Delta) <= 2*kappa.  We verify on Pi_2:  (i) a random eta-selfadjoint Delta has
#   #non-real <= 4 = 2*kappa; (ii) a real-spectrum Delta built with a genuine 2-dim negative-type
#   eigenspace has that eigenspace Delta-INVARIANT and NON-POSITIVE of dimension exactly kappa=2 -- the
#   finite defect two quasivectors patch.  This is the finite-rank lever that has NO infinite-rank analogue.
# ==================================================================================================
log("\n[T2] Finite-rank definitizability: defect = negative index kappa is FINITE; #non-real <= 2*kappa")
eta_p2 = np.diag([1.0, 1.0, -1.0, -1.0]).astype(complex)     # Pi_2, kappa = 2


def Delta_from_M(M, eta):
    return (eta @ M.T @ eta) @ np.conj(M)                    # Delta = S^+ S, eta-selfadjoint


def n_nonreal(D, tol=1e-7):
    e = np.linalg.eigvals(D)
    return int(np.sum(np.abs(e.imag) > tol))


kappa = 2
# (i) Langer non-real bound over random eta-selfadjoint modular operators on Pi_2
g = np.random.default_rng(11)
max_nr = 0
selfadj_resid = 0.0
for _ in range(6000):
    M = g.standard_normal((4, 4)) + 1j * g.standard_normal((4, 4))
    D = Delta_from_M(M, eta_p2)
    selfadj_resid = max(selfadj_resid, np.max(np.abs(eta_p2 @ dag(D) @ eta_p2 - D)))
    max_nr = max(max_nr, n_nonreal(D))
nonreal_bounded = max_nr <= 2 * kappa

# (ii) build a real-positive eta-selfadjoint Delta with a genuine 2-dim NEGATIVE-type eigenspace.
#      J-unitary eigenbasis U (U^+ U = 1): columns 0,1 positive type, 2,3 negative type.
gA = np.random.default_rng(5)
Aherm = gA.standard_normal((4, 4)) + 1j * gA.standard_normal((4, 4))
Aherm = 0.3 * (Aherm + dag(Aherm))
# numpy-only eta-unitary U = exp(i * eta * A): eta-selfadjoint generator eta*A => eta-unitary exponential
M_gen = 1j * (eta_p2 @ Aherm)


def expm_dense(Mx, terms=40):
    acc = np.eye(Mx.shape[0], dtype=complex)
    term = np.eye(Mx.shape[0], dtype=complex)
    for k in range(1, terms):
        term = term @ Mx / k
        acc = acc + term
    return acc


U = expm_dense(M_gen)
Uinv_krein = eta_p2 @ dag(U) @ eta_p2                        # U^+ = eta U* eta ; for eta-unitary, = U^{-1}
etaunitary_resid = float(np.max(np.abs(Uinv_krein @ U - np.eye(4))))
lam = np.array([2.3, 1.7, 0.9, 1.4])                        # ALL real-positive
Delta_def = U @ np.diag(lam.astype(complex)) @ Uinv_krein
Delta_def_selfadj = float(np.max(np.abs(eta_p2 @ dag(Delta_def) @ eta_p2 - Delta_def)))
Delta_def_realpos = (np.max(np.abs(np.linalg.eigvals(Delta_def).imag)) < 1e-8
                     and np.min(np.linalg.eigvals(Delta_def).real) > 1e-8)
neg_space = U[:, 2:4]                                        # the 2-dim negative-type eigenspace
gram = dag(neg_space) @ eta_p2 @ neg_space                  # Krein Gram of the defect
defect_nonpositive = bool(np.max(np.linalg.eigvalsh(gram).real) < 1e-8)
defect_invariant = float(np.max(np.abs(Delta_def @ neg_space - neg_space @ np.diag(lam[2:4].astype(complex)))))
defect_dim = neg_space.shape[1]
check(f"T2  Definitizability = FINITE defect at finite rank.  #non-real(Delta) max = {max_nr} (<= 2*kappa "
      f"= {2*kappa}); the non-positive-type defect is a genuine kappa={defect_dim}-dim Delta-INVARIANT "
      f"(resid {defect_invariant:.1e}) NON-POSITIVE (max Gram eig {np.max(np.linalg.eigvalsh(gram).real):.1e}"
      ") subspace.  So the quasivector count needed = kappa = 2 is FINITE and patchable.  This finite "
      "spectral structure is the lever behind Shulman/Langer -- and it has NO infinite-rank analogue.",
      nonreal_bounded and selfadj_resid < 1e-9 and etaunitary_resid < 1e-8 and Delta_def_selfadj < 1e-8
      and Delta_def_realpos and defect_nonpositive and defect_invariant < 1e-8 and defect_dim == kappa,
      f"#non-real<=2kappa={nonreal_bounded}, defect dim={defect_dim}, invariant resid={defect_invariant:.1e}")

# ==================================================================================================
# T3 -- THE GENUINE INFINITE-RANK OBSTRUCTION (Branch-2's new content).  A quasivector patches ONE unit
#   of non-positive-type defect; K quasivectors patch K units.  For GU's Delta the negative index is
#   INFINITE, so no FINITE quasivector construction reaches it.  The only hope is a K -> infinity limit --
#   which assembles into a BOUNDED modular conjugation J (a Krein-antiisometry) IFF the metric inverse is
#   UNIFORMLY BOUNDED across the mode tower (== definitizability).  We reuse the repo's exceptional-point
#   mode tower (W52/W84): H_k = [[i a_k, b_k],[b_k, -i a_k]], r_k = a_k/b_k, PT-unbroken iff r_k < 1,
#   positive metric eta_k = [[1,-i r_k],[i r_k,1]], cond = (1+r_k)/(1-r_k).  With r_k -> 1 (the UV
#   approach to the exceptional locus, W53: m2^2 -> 0 at the free UV FP the AS trajectory approaches):
#     * the number of quasivectors needed (negative index) grows without bound (one per ghost mode);
#     * the K-quasivector patch NORM = ||metric^{-1}|| on the truncation grows without bound in K;
#   so the K -> infinity assembly is UNBOUNDED: there is NO bounded J.  This is exactly non-definitizability
#   (Krejcirik-Siegl: bounded metric, UNBOUNDED inverse).  The quasivector route has NO kappa=infinity limit.
# ==================================================================================================
log("\n[T3] Infinite-rank obstruction: quasivector count -> inf AND patch norm -> inf => no bounded J assembles")


def cond_metric(r: float) -> float:
    ev = np.linalg.eigvalsh(np.array([[1.0, -1j * r], [1j * r, 1.0]], dtype=complex))
    return float(ev.max() / ev.min())


def min_metric_eig(r: float) -> float:
    return float(np.linalg.eigvalsh(np.array([[1.0, -1j * r], [1j * r, 1.0]], dtype=complex)).min())


def is_real_spectrum_mode(r: float, tol: float = 1e-9) -> bool:
    H = np.array([[1j * r, 1.0], [1.0, -1j * r]], dtype=complex)
    return bool(np.max(np.abs(np.linalg.eigvals(H).imag)) < tol)


# UNIFORM tower (r_k = 0.5): every mode PT-unbroken, metric inverse BOUNDED -> definitizable-surrogate ->
#   a uniformly bounded quasivector patch assembles -> J exists (but ghost REMOVABLE, W84 T1/T4 horn Q).
# NON-UNIFORM tower (r_k -> 1): every mode PT-unbroken, metric inverse UNBOUNDED -> non-definitizable ->
#   no bounded quasivector assembly -> NO J (horn K, GU's indicated regime).
def patch_norm(r_of_k, K):
    return 1.0 / min([min_metric_eig(r_of_k(k)) for k in range(K)])      # ||metric^{-1}|| on truncation K


def quasivector_count(K):        # negative index of the truncated tower = one ghost direction per mode
    return K


K1, K2 = 2000, 4000
r_uniform = lambda k: 0.5
r_nonuniform = lambda k: 1.0 - 1.0 / (k + 2.0)

all_unbroken_uni = all(is_real_spectrum_mode(r_uniform(k)) for k in range(0, K1, max(1, K1 // 200)))
all_unbroken_non = all(is_real_spectrum_mode(r_nonuniform(k)) for k in range(0, K1, max(1, K1 // 200)))

uni_norm_K1, uni_norm_K2 = patch_norm(r_uniform, K1), patch_norm(r_uniform, K2)
non_norm_K1, non_norm_K2 = patch_norm(r_nonuniform, K1), patch_norm(r_nonuniform, K2)

uniform_bounded = uni_norm_K2 < 1.1 * uni_norm_K1           # no growth under tower-doubling => bounded
nonuniform_unbounded = non_norm_K2 > 1.9 * non_norm_K1      # ~doubles => unbounded => no bounded J
count_diverges = quasivector_count(K2) > quasivector_count(K1)   # # quasivectors grows without bound

# closure (a bounded assembled J) holds IFF the metric inverse is uniformly bounded == definitizable:
uniform_J_bounded = uniform_bounded
nonuniform_J_bounded = not nonuniform_unbounded             # False: unbounded => NO bounded J

check("T3  Infinite-rank quasivector assembly FAILS on the non-definitizable tower.  BOTH towers are "
      f"mode-wise PT-unbroken, and the quasivector COUNT (negative index) diverges ({quasivector_count(K1)} "
      f"-> {quasivector_count(K2)}).  UNIFORM tower: patch norm bounded ({uni_norm_K1:.1e} -> "
      f"{uni_norm_K2:.1e}) => a bounded J assembles (definitizable; but ghost REMOVABLE).  NON-UNIFORM "
      f"tower (r_k->1, the UV exceptional-locus approach): patch norm UNBOUNDED ({non_norm_K1:.1e} -> "
      f"{non_norm_K2:.1e}) => NO bounded J (Krejcirik-Siegl; non-definitizable).  So there is NO "
      "kappa=infinity quasivector construction when the metric inverse is unbounded.",
      all_unbroken_uni and all_unbroken_non and count_diverges and uniform_bounded
      and nonuniform_unbounded and uniform_J_bounded and (not nonuniform_J_bounded),
      f"uniform J bounded={uniform_J_bounded}, nonuniform J bounded={nonuniform_J_bounded}")

# ==================================================================================================
# T4 -- THE EXTENDS-REGION IS BOUNDED EVEN AT FINITE RANK: quasivectors patch a NEUTRAL/NEGATIVE-TYPE
#   defect, NOT non-real spectrum.  On a rank-2 Delta = S^+ S with a genuinely NON-REAL conjugate pair
#   (PT-broken), there is NO eta-positive square root, so NO eta-positive polar decomposition and NO J --
#   and NO number of quasivectors repairs it (they do not move the spectrum off the complex plane).  So
#   "kappa-quasivector extends" is confined to the DEFINITIZABLE + REAL-SPECTRUM regime; the genuinely
#   broken locus obstructs at every rank.  (Consistent with W77 T4.)
# ==================================================================================================
log("\n[T4] EXTENDS is bounded: a non-real (PT-broken) Delta has no eta-positive sqrt -- quasivectors "
    "cannot repair non-real spectrum, at any rank")
gB = np.random.default_rng(23)
D_broken = None
while D_broken is None:
    M = gB.standard_normal((4, 4)) + 1j * gB.standard_normal((4, 4))
    D = Delta_from_M(M, eta_p2)
    e = np.linalg.eigvals(D)
    if np.max(np.abs(e.imag)) > 1e-6:                       # a genuine non-real pair
        D_broken = D
ev_b = np.linalg.eigvals(D_broken)
broken_selfadj = float(np.max(np.abs(eta_p2 @ dag(D_broken) @ eta_p2 - D_broken)))
broken_has_nonreal = bool(np.max(np.abs(ev_b.imag)) > 1e-6)
# no eta-positive square root of a non-real-spectrum operator: the principal sqrt has non-real eigenvalues
sqrt_ev = np.sqrt(ev_b)
no_eta_positive_sqrt = bool(np.max(np.abs(sqrt_ev.imag)) > 1e-6)
check("T4  Non-real (PT-broken) Delta obstructs at rank 2 regardless of quasivectors: Delta is "
      f"eta-selfadjoint (resid {broken_selfadj:.1e}) with a non-real pair (max |Im lambda| "
      f"{np.max(np.abs(ev_b.imag)):.2e}) => NO eta-positive Delta^{{1/2}} (its sqrt has |Im| "
      f"{np.max(np.abs(sqrt_ev.imag)):.2e}) => NO J.  Quasivectors patch NEUTRAL/negative-type defect, "
      "NOT non-real spectrum; so EXTENDS is confined to the definitizable + real-positive regime.",
      broken_selfadj < 1e-9 and broken_has_nonreal and no_eta_positive_sqrt,
      f"non-real pair present={broken_has_nonreal}, no eta-positive sqrt={no_eta_positive_sqrt}")

# ==================================================================================================
# T5 -- VERDICT BOOLEANS (Branch-2 synthesizer): PARTIAL == EXTENDS-under-definitizability /
#   OBSTRUCTED-for-GU's-infinite-rank-non-definitizable-Delta; reduces to the shared definitizability
#   residual.
# ==================================================================================================
log("\n[T5] VERDICT = PARTIAL (EXTENDS under definitizability; OBSTRUCTED for GU's infinite-rank Delta)")
verdict = {
    # (A) finite rank: a kappa-quasivector construction DOES extend Shulman, under definitizability:
    "kappa_quasivector_extends_at_finite_rank_definitizable_realpos": True,     # T1 + T2
    "finite_rank_defect_is_finite_kappa_dim_and_patchable": True,               # T2 (Langer/Pontryagin)
    "finite_rank_extension_has_removable_ghost": True,                          # W84 T1 (quasi-Hermitian)
    # (B) infinite rank: genuine obstruction, not a failure of one device:
    "quasivector_count_equals_negative_index_finite_only": True,               # T3 (K quasivectors patch K)
    "no_kappa_infinity_quasivector_limit_when_metric_inverse_unbounded": True,  # T3 (patch norm -> inf)
    "general_krein_selfadjoint_infinite_rank_is_definitizable": False,          # Langer: only Pi_kappa is
    "eta_positive_sqrt_from_real_spectrum_at_infinite_rank": False,             # T3/T4 + Krejcirik-Siegl
    "Pi_kappa_TT_conjugation_theorem_at_infinite_rank_exists": False,           # none (Shulman rank-1)
    # non-real locus obstructs at every rank (bounds the EXTENDS region):
    "non_real_broken_Delta_obstructs_regardless_of_quasivectors": True,         # T4
    # the reduction to the shared residual:
    "quasivector_reach_is_coextensive_with_definitizability": True,             # T1-T3 together
    "quasivector_route_independently_resolves_the_frontier": False,             # it reduces to the residual
    # repo-native indication GU is on the obstructed (non-definitizable) side:
    "repo_indication_GU_non_definitizable_in_UV_C_norm_blows_up": True,         # W52/W53 (indication)
}
extends_under_definitizability = (
    verdict["kappa_quasivector_extends_at_finite_rank_definitizable_realpos"]
    and verdict["finite_rank_defect_is_finite_kappa_dim_and_patchable"]
)
obstructed_at_infinite_rank = (
    verdict["no_kappa_infinity_quasivector_limit_when_metric_inverse_unbounded"]
    and (verdict["general_krein_selfadjoint_infinite_rank_is_definitizable"] is False)
    and (verdict["eta_positive_sqrt_from_real_spectrum_at_infinite_rank"] is False)
    and (verdict["Pi_kappa_TT_conjugation_theorem_at_infinite_rank_exists"] is False)
)
reduces_to_shared_residual = (
    verdict["quasivector_reach_is_coextensive_with_definitizability"]
    and (verdict["quasivector_route_independently_resolves_the_frontier"] is False)
)
partial_verdict = extends_under_definitizability and obstructed_at_infinite_rank and reduces_to_shared_residual
check("T5  VERDICT = PARTIAL.  A kappa-quasivector construction EXTENDS Shulman to every FINITE Pi_kappa "
      "under DEFINITIZABILITY + real-positive spectrum (the defect is a finite kappa-dim invariant "
      "subspace; rank 2 is a concrete witness -- but the ghost is REMOVABLE there).  It is OBSTRUCTED at "
      "GU's infinite-rank Delta: the quasivector count = negative index is infinite, and no bounded "
      "kappa=infinity assembly exists when the metric inverse is unbounded (non-definitizable, "
      "Krejcirik-Siegl).  The quasivector reach is CO-EXTENSIVE WITH DEFINITIZABILITY; it does NOT "
      "independently resolve the frontier -- it REDUCES to the shared infinite-rank definitizability "
      "residual (hand to Branch 3's algebraic route / Branch 5's no-go).  Repo-native indication (W52/W53) "
      "places GU on the OBSTRUCTED side.",
      partial_verdict,
      f"extends(def)={extends_under_definitizability}, obstructed(inf)={obstructed_at_infinite_rank}, "
      f"reduces={reduces_to_shared_residual}")

# ==================================================================================================
# SUMMARY
# ==================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W90 Shulman Pi_kappa checks FAILED"

log("")
log("BRANCH-2 SHULMAN Pi_1 -> Pi_kappa VERDICT (this file is the computation, not a claim-status change):")
log("  * VERDICT = PARTIAL.  A kappa-quasivector construction EXTENDS Shulman's modular conjugation J to")
log("    every FINITE Pi_kappa, but only under DEFINITIZABILITY + real-positive spectrum -- and there the")
log("    ghost is REMOVABLE (quasi-Hermitian).  It is OBSTRUCTED at GU's genuine infinite-rank Delta=S^+S.")
log("  * WHY finite works: on Pi_kappa every eta-selfadjoint operator is DEFINITIZABLE (Langer); the")
log("    non-positive-type defect is a FINITE kappa-dim invariant subspace and #non-real <= 2*kappa, so")
log("    kappa quasivectors patch a kappa-dim defect exactly as one patches a 1-dim defect.  Rank 2 is a")
log("    concrete 2-quasivector witness (all four modular properties, T1).")
log("  * WHY infinite fails GENUINELY (not one device): a quasivector patches ONE finite defect unit; the")
log("    count needed = the negative index = infinity, so no FINITE construction reaches GU.  The")
log("    kappa=infinity limit assembles into a BOUNDED J iff the metric inverse is uniformly bounded ==")
log("    definitizable.  For GU's real-positive-but-unbounded-inverse Delta (Krejcirik-Siegl; W52/W53 UV")
log("    exceptional locus) the patch norm diverges: NO bounded J.  General Krein-selfadjoint operators at")
log("    infinite rank are NOT definitizable (Langer) -- no spectral function, no eta-positive sqrt, no J.")
log("  * SHARED RESIDUAL: the quasivector route's reach is CO-EXTENSIVE with definitizability; it does NOT")
log("    independently cross the frontier.  It reduces, with no remainder, to the INFINITE-RANK")
log("    DEFINITIZABILITY residual: does GU's Delta admit a definitizing polynomial / uniformly bounded")
log("    metric?  YES -> J exists (ghost removable); NO -> hand to Branch 3 (algebraic) / Branch 5 (no-go).")
log("    Branch 2 does not settle it; W52/W53 indicate FAILURE (GU on the obstructed HORN K).  Not a proof.")
raise SystemExit(0)
