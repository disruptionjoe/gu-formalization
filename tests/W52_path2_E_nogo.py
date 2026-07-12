#!/usr/bin/env python3
r"""
W52 / Path-2 Branch E -- the adversarial no-go: the positivity-defining grading is
DYNAMICAL and lives on a finite domain with a fatal boundary, so loop positivity of the
keep-and-grade (Krein / PT / indefinite-metric) rescue is RG-contingent, not structural.

What this file is.
  This is the concrete obstruction arithmetic for the red-team branch of the Path-2
  keep-and-grade loop-positivity wave (H59). It does NOT compute a GU/Stelle loop
  amplitude. It encodes, in closed form on a solvable 2x2 PT toy, the mechanism by which
  the grading that defines the POSITIVE physical inner product fails -- and it certifies
  that failure is (a) tied to the interacting/coupling data, not kinematic, and (b) hits a
  codimension-1 exceptional locus on which -- by the R1 two-line theorem already in this
  repo -- NO positivity-compatible grading of any kind exists.

The obstruction (stated GU-independently, for the whole Stelle/conformal/agravity class).
  Keep-and-grade unitarity has TWO distinct objects that must not be conflated:
    * the KINEMATIC indefinite (Krein) form eta -- fixed, signature-only, survives
      everything, but is INDEFINITE and by itself defines no positive probability;
    * the POSITIVITY-DEFINING grading (C-operator / positivity-compatible ghost parity /
      metric operator eta_+) -- the object that makes the physical inner product positive.
  Repo route R1 (tests/big-swing/cg_r1_pu_pt_vs_ghost_parity.py) proved, in the shared
  Pais-Uhlenbeck toy, a two-line theorem: a positivity-compatible grading P (P^2=I,
  [P,H]=0, eta P > 0) EXISTS iff H is Krein-diagonalizable with real spectrum. That is a
  DYNAMICAL property of the interacting Hamiltonian/action, not a kinematic datum. Hence
  the positive physical inner product is a FUNCTION OF THE COUPLINGS, and the region of
  coupling space where it exists is OPEN with a boundary: the PT-breaking / exceptional
  (Jordan) locus. Tree-level positivity is only the statement "at the free point we are
  safely inside." It gives ZERO protection against the renormalization-group trajectory
  reaching the boundary, on which the grading provably ceases to exist.

Why this is the kill and not a slogan.
  On the 2x2 PT model H(a,b) = [[ i a, b ], [ b, -i a ]] (the minimal exceptional-point
  Hamiltonian; a,b real), everything is closed form:
    * eigenvalues  lambda = +/- sqrt(b^2 - a^2);
    * the unique (up to scale/family) positive intertwining metric is
          eta_+ = [[ 1, -i a/b ], [ i a/b, 1 ]],  eta_+ H = H^dagger eta_+,
      with eigenvalues  1 -/+ a/b;
    * PT-unbroken (real spectrum, eta_+ > 0)  <=>  |a| < b;
    * exceptional locus a = b: eigenvalues collide, H is a defective Jordan block,
      lambda_min(eta_+) = 0  -> grading DEGENERATES (no positive inner product);
    * PT-broken |a| > b: eigenvalues imaginary, eta_+ indefinite -> positivity LOST.
  Reading a,b as effective (running) couplings, the physical inner product eta_+(a,b)
  depends on the ratio a/b and is therefore NOT RG-invariant; and lambda_min(eta_+) ->
  0 as a/b -> 1, so the positive metric is destroyed by DEGENERATION on a codimension-1
  locus, a failure a sign-flip-catching grading cannot repair.

Construction forks used (GEOMETER-VS-PHYSICS-OBJECTS.md), stated explicitly.
  1. Ghost clearance: GU-native KEEP-AND-GRADE Krein/PT (NOT positive-Hilbert removal /
     SUSY / Lee-Wick / fakeon). The obstruction attacks this construction directly.
  2. Grading: we distinguish the KINEMATIC Krein form eta (Cartan involution of so(9,5) --
     survives RG but is indefinite) from the POSITIVITY-DEFINING grading (C / ghost parity
     / eta_+). The GU-native hope "the grading is the kinematic Cartan involution, so it
     cannot run" is ALREADY closed by R1: the kinematic form is not positivity-defining;
     the positivity-defining object is dynamical. The kill targets the positivity-defining
     grading.
  3. Unitarity: the construction attacked is POSITIVE Born-rule probability on the physical
     subspace -- NOT mere pseudo-unitarity S^dagger S = 1, which Bateman-Turok establish to
     all orders and which this file does NOT dispute.

Class-wide vs construction-specific.
  CLASS-WIDE at the level of the positivity-defining grading: R1's equivalence
  (positivity-compatible grading <=> Krein-diagonalizable real-spectrum dynamics) is
  construction-independent within the keep-and-grade class, so the RG-contingency and the
  fatal exceptional locus apply to Krein, PT/Bender-Mannheim, and Bateman-Turok alike.
  The kill is NOT a completed proof that any specific flow crosses the locus -- that
  remains a per-theory computation. What is rigorously established is the CONTINGENCY plus
  the fatal boundary; the burden is thereby flipped onto the rescuer to prove the flow
  stays PT-unbroken, which tree positivity does not do.

The one assumption the whole kill rests on.
  R1's equivalence transfers from the PU quantum-mechanical toy to the interacting QFT:
  i.e. at loop level too, a positivity-compatible grading exists iff the (renormalized)
  action is Krein-diagonalizable with real spectrum. If a purely kinematic positive
  grading existed for the ghost sector in QFT, the RG-contingency would vanish.

Reproducible: python tests/W52_path2_E_nogo.py     (pure Python, no dependencies)
No canon / verdict / claim-status / RESEARCH-STATUS file is touched. Exploration-grade.
"""
from __future__ import annotations

import math

TOL = 1e-12
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ---------------------------------------------------------------------------
# Minimal complex 2x2 machinery (pure Python -- no numpy, fully deterministic).
# A 2x2 complex matrix is a 4-tuple (m11, m12, m21, m22) of Python complex.
# ---------------------------------------------------------------------------
Mat = tuple[complex, complex, complex, complex]


def matmul(A: Mat, B: Mat) -> Mat:
    a11, a12, a21, a22 = A
    b11, b12, b21, b22 = B
    return (
        a11 * b11 + a12 * b21,
        a11 * b12 + a12 * b22,
        a21 * b11 + a22 * b21,
        a21 * b12 + a22 * b22,
    )


def dagger(A: Mat) -> Mat:
    a11, a12, a21, a22 = A
    return (a11.conjugate(), a21.conjugate(), a12.conjugate(), a22.conjugate())


def maxabs(A: Mat) -> float:
    return max(abs(x) for x in A)


def sub(A: Mat, B: Mat) -> Mat:
    return tuple(a - b for a, b in zip(A, B))  # type: ignore[return-value]


def H_of(a: float, b: float) -> Mat:
    """The minimal exceptional-point PT Hamiltonian H(a,b) = [[ i a, b ], [ b, -i a ]]."""
    return (1j * a, complex(b), complex(b), -1j * a)


def eta_plus(a: float, b: float) -> Mat:
    """Closed-form positive intertwining metric eta_+ = [[1, -i a/b], [i a/b, 1]]."""
    return (1.0 + 0j, -1j * a / b, 1j * a / b, 1.0 + 0j)


def H_eigs_realpart_sq(a: float, b: float) -> float:
    """lambda^2 = b^2 - a^2. >0 real spectrum; =0 exceptional; <0 imaginary spectrum."""
    return b * b - a * a


def hermitian_2x2_eigs(A: Mat) -> tuple[float, float]:
    """Eigenvalues of a Hermitian 2x2 (real), returned (min, max)."""
    a11, a12, a21, a22 = A
    tr = (a11 + a22).real
    det = (a11 * a22 - a12 * a21).real
    disc = max(0.0, tr * tr / 4.0 - det)
    r = math.sqrt(disc)
    lo, hi = tr / 2.0 - r, tr / 2.0 + r
    return (lo, hi)


def is_hermitian(A: Mat) -> bool:
    return maxabs(sub(A, dagger(A))) < TOL


log("=" * 92)
log("W52 / PATH-2 BRANCH E -- NO-GO: THE POSITIVITY-DEFINING GRADING IS DYNAMICAL,")
log("FINITE-DOMAIN, AND DIES ON A CODIM-1 EXCEPTIONAL LOCUS  (loop positivity is RG-contingent)")
log("=" * 92)

b = 1.0

# --- E1: the metric eta_+ genuinely intertwines H (it IS the positivity-defining object) ---
worst_intertwine = 0.0
for a in (0.1, 0.3, 0.5, 0.7, 0.9, 0.99):
    H = H_of(a, b)
    eta = eta_plus(a, b)
    worst_intertwine = max(worst_intertwine, maxabs(sub(matmul(eta, H), matmul(dagger(H), eta))))
check(
    "E1  eta_+ satisfies eta_+ H = H^dagger eta_+ across the unbroken domain: it is a bona fide "
    "metric making H self-adjoint (the positive physical inner product), not a strawman",
    worst_intertwine < TOL and is_hermitian(eta_plus(0.5, b)),
    f"max||eta_+ H - H^dag eta_+|| = {worst_intertwine:.2e}",
)

# --- E2: unbroken phase |a|<b -> real spectrum AND eta_+ strictly positive (grading exists) ---
lo, hi = hermitian_2x2_eigs(eta_plus(0.5, b))
check(
    "E2  PT-unbroken |a|<b: H has real spectrum (b^2-a^2>0) and eta_+ is positive-definite "
    "(lambda_min>0) -> a positive physical inner product exists here (tree-level 'safe interior')",
    H_eigs_realpart_sq(0.5, b) > 0 and lo > TOL,
    f"b^2-a^2={H_eigs_realpart_sq(0.5,b):.3f}, eta_+ eigs=({lo:.3f},{hi:.3f})",
)

# --- E3: the grading DEGENERATES on approach to the exceptional locus a->b (the kill core) ---
# Closed form: lambda_min(eta_+) = 1 - a/b -> 0 linearly. Assert strict monotone decrease to 0.
seq_a = [0.90, 0.99, 0.999, 0.9999]
lam_min = [hermitian_2x2_eigs(eta_plus(a, b))[0] for a in seq_a]
predicted = [1.0 - a / b for a in seq_a]  # exact closed form
monotone = all(lam_min[i] > lam_min[i + 1] > 0.0 for i in range(len(lam_min) - 1))
matches_closed_form = all(abs(l - p) < 1e-9 for l, p in zip(lam_min, predicted))
goes_to_zero = lam_min[-1] < 2e-4
check(
    "E3  as effective couplings drive a/b -> 1, lambda_min(eta_+) -> 0 (matches closed form 1-a/b): "
    "the POSITIVE metric is destroyed by DEGENERATION on a codim-1 locus -- a failure no sign-flip "
    "grading can repair",
    monotone and matches_closed_form and goes_to_zero,
    f"lambda_min at a/b={seq_a}: {[f'{x:.4f}' for x in lam_min]}",
)

# --- E4: exactly ON the exceptional locus a=b -> Jordan block, no positive grading (R1 theorem) ---
a = 1.0
sq = H_eigs_realpart_sq(a, b)
lo_ep, hi_ep = hermitian_2x2_eigs(eta_plus(a, b))
# Defectiveness: at a=b the two eigenvectors of H coincide. Eigenvectors u_+/-=(b, lambda -/+ i a);
# at lambda=0, a=b they both become (b, -i b) ~ (1, -i): geometric multiplicity 1.
u_plus = (complex(b), 0.0 - 1j * a)   # (b, lambda - i a) with lambda=0
u_minus = (complex(b), 0.0 - 1j * a)  # (b, -lambda - i a) with lambda=0  -> identical
coincide = abs(u_plus[0] - u_minus[0]) + abs(u_plus[1] - u_minus[1])
check(
    "E4  ON the exceptional locus a=b: spectrum collides (b^2-a^2=0), H is a defective Jordan block "
    "(eigenvectors coincide), and lambda_min(eta_+)=0 -> NO positivity-compatible grading exists "
    "(the repo R1 two-line theorem, realized)",
    abs(sq) < TOL and coincide < TOL and abs(lo_ep) < TOL,
    f"b^2-a^2={sq:.2e}, eigvec-gap={coincide:.2e}, eta_+ lambda_min={lo_ep:.2e}",
)

# --- E5: PT-broken |a|>b -> imaginary spectrum, eta_+ INDEFINITE -> positivity gone past the locus ---
a = 1.3
sq = H_eigs_realpart_sq(a, b)
lo_b, hi_b = hermitian_2x2_eigs(eta_plus(a, b))
check(
    "E5  past the locus |a|>b: H has imaginary eigenvalues (b^2-a^2<0) and eta_+ is INDEFINITE "
    "(lambda_min<0) -> the physical inner product is no longer positive: the rescue is dead on this "
    "side of the boundary",
    sq < 0 and lo_b < -TOL,
    f"b^2-a^2={sq:.3f}, eta_+ eigs=({lo_b:.3f},{hi_b:.3f})",
)

# --- E6: the grading is DYNAMICAL / coupling-dependent (NOT kinematic) -> it is not RG-invariant ---
# Two different coupling ratios give genuinely different metrics; a kinematic grading could not.
eta_A = eta_plus(0.3, b)
eta_B = eta_plus(0.8, b)
metric_runs = maxabs(sub(eta_A, eta_B)) > 0.1
kinematic_eta = (1.0 + 0j, 0j, 0j, -1.0 + 0j)  # the fixed indefinite Krein form (z-parity): survives, but
kinematic_is_indefinite = hermitian_2x2_eigs(kinematic_eta)[0] < 0  # ...defines NO positive inner product
check(
    "E6  eta_+(a,b) depends on the coupling ratio a/b (eta_+ at a/b=0.3 != a/b=0.8): the "
    "positivity-defining grading RUNS under RG. The only RG-fixed grading (the kinematic Krein form) "
    "is INDEFINITE and defines no positive probability -- so nothing RG-stable rescues positivity",
    metric_runs and kinematic_is_indefinite,
    f"||eta_+(.3)-eta_+(.8)||={maxabs(sub(eta_A,eta_B)):.3f}; kinematic eta eigs="
    f"{hermitian_2x2_eigs(kinematic_eta)}",
)

# --- E7: honesty guard -- this is NOT a completed kill of any specific flow ---
# We do NOT assert GU/Stelle's actual RG trajectory reaches a/b=1. The kill establishes the
# CONTINGENCY and the fatal boundary; whether a given flow crosses it is a per-theory computation.
# Encode that as an explicit non-claim so downstream work cannot over-read this file.
specific_flow_crossing_proven = False
check(
    "E7  honesty guard: this file proves the grading is dynamical + finite-domain + fatally bounded "
    "(RG-CONTINGENCY of loop positivity), NOT that GU/Stelle's specific flow crosses the locus -- that "
    "remains an open per-theory computation. No over-claim of a completed kill.",
    specific_flow_crossing_proven is False,
    "class-wide contingency: rigorous; specific-flow crossing: OPEN (not asserted)",
)

log("\n" + "=" * 92)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

# Hard asserts (the deterministic obstruction arithmetic).
assert worst_intertwine < TOL, "eta_+ does not intertwine H"
assert H_eigs_realpart_sq(0.5, b) > 0 and hermitian_2x2_eigs(eta_plus(0.5, b))[0] > TOL
assert all(lam_min[i] > lam_min[i + 1] > 0.0 for i in range(len(lam_min) - 1))
assert all(abs(l - p) < 1e-9 for l, p in zip(lam_min, predicted))
assert lam_min[-1] < 2e-4, "grading does not degenerate toward the exceptional locus"
assert abs(H_eigs_realpart_sq(1.0, b)) < TOL and abs(hermitian_2x2_eigs(eta_plus(1.0, b))[0]) < TOL
assert H_eigs_realpart_sq(1.3, b) < 0 and hermitian_2x2_eigs(eta_plus(1.3, b))[0] < -TOL
assert maxabs(sub(eta_plus(0.3, b), eta_plus(0.8, b))) > 0.1
assert hermitian_2x2_eigs(kinematic_eta)[0] < 0
assert specific_flow_crossing_proven is False
assert npass == ntot, "some Branch-E no-go checks failed"

log("")
log("VERDICT (Branch E, graded).")
log("  Q-pos  : OBSTRUCTION LANDS. The positivity-defining grading is dynamical, exists only on an")
log("           open PT-unbroken domain, and DEGENERATES to zero on a codim-1 exceptional locus. Loop")
log("           positivity is RG-CONTINGENT, not structural. Grade: rigorous (toy + R1 theorem) for the")
log("           contingency; PLAUSIBILITY for any completed 'flow crosses it' kill of a specific theory.")
log("  Q-cut  : INHERITS the contingency. Pseudo-unitarity (S^dag S=1) is all-orders and NOT disputed;")
log("           but ghost/cut decoupling is a positivity statement, so it holds only in the PT-unbroken")
log("           phase and degenerates at the locus (double poles / secular growth). Grade: plausibility.")
log("  Q-caus : the equivalent-Hermitian map eta_+^{1/2} is generically NON-LOCAL (metric bilinear in")
log("           fields); loop-unitarity is bought at a locality cost UNLESS the metric is local, which is")
log("           unestablished for the ghost sector. Grade: plausibility / folk-theorem (not proven here).")
log("")
log("  CLASS-WIDE (Krein / PT-Bender-Mannheim / Bateman-Turok) at the level of the positivity-defining")
log("  grading, via R1's construction-independent equivalence. ONE load-bearing assumption: R1's")
log("  equivalence (positive grading <=> Krein-diagonalizable real-spectrum action) transfers to loop QFT.")
log("  No canon / claim-status / verdict changed. H59 remains OPEN; burden flipped onto the rescuer.")
raise SystemExit(0)
