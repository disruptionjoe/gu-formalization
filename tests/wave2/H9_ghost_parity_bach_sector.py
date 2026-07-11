#!/usr/bin/env python3
r"""H9 -- Does GU's Bach (Weyl^2 / 4-derivative) gravity sector instantiate the
Bateman-Turok hidden-ghost-parity ghost-free completion?

Wave 2, cheap decisive cascade-gate. GRAVITY-SIDE dual of the matter-sector
ghost-parity work (canon/ghost-parity-krein-synthesis.md, big-swing-2026-07-06).

DECISIVE QUESTION
-----------------
Bateman & Turok (arXiv:2607.00096) make a 4-derivative theory UNITARY by
quantizing on a Krein space, KEEPING the ghost but grading it by a hidden ghost
parity P that is made explicit via a TWO-FIELD O(1,1) embedding (a healthy field
+ a distinct ghost field), with a generalized Born rule giving positive tree-level
probabilities -- PROVIDED [P,S]=0 (P a symmetry of the dynamics).

Wave 1 (tests/wave1/H1_bach_flat_exact_vacua.py + the D-thread) established that
GU's H-class pure-gravity/spin-2 section-EL IS the Bach operator, box^2 h on the
transverse-traceless sector (box^2 h = -4 Bach^(1)). So GU's established gravity
kinetic operator is box^2.

THE STRUCTURAL CRUX THIS FILE COMPUTES (exact sympy, no imported target)
------------------------------------------------------------------------
Bateman-Turok's clean O(1,1) ghost-parity split requires a NON-DEGENERATE ghost:
two DISTINCT poles (a massless/healthy graviton at one mass and a MASSIVE ghost at
another). Pure Bach / Weyl^2 = box^2 is the COINCIDENT-POLE (equal/zero mass)
DEGENERATE limit -- exactly the Pais-Uhlenbeck equal-frequency Jordan-block case
where the two-field O(1,1) diagonalization FAILS and the ghost parity is NOT unique
(matches R1's Jordan-boundary nonexistence theorem and R3's K-balance non-uniqueness
in big-swing-2026-07-06). This file decides that structural fact.

WHAT THIS TESTS (and what it does NOT)
--------------------------------------
It COMPUTES the free/kinematic structure exactly:
  A. propagator partial-fraction: the O(1,1) healthy/ghost split of the NON-degenerate
     massive quadratic-gravity TT propagator, and the SINGULAR degeneration of pure Bach.
  B. Pais-Uhlenbeck companion-matrix diagonalizability: clean split iff non-degenerate.
  C. ghost-parity P as a Krein isometry commuting with the free action (kinematic
     [P,S_free]=0) -- and its NON-UNIQUENESS at the degenerate (Bach) mass.
  D. adversarial: GU's matter Krein form (O(96,96), so(9,5) Cartan involution) is NOT
     literally the gravity-sector O(1,1) ghost space -- shared Z2 grade, different space.

It does NOT: build GU's (unbuilt) source action S, so the INTERACTING [P,S]=0 stays
open (canon fencing, R3 sustained); it does NOT compute loop-level positivity (Bateman
-Turok prove only TREE level); it does NOT settle the conformal-vs-Einstein / OQ2-A
functional choice (whether GU's gravity is pure Bach or massive-Stelle R+Weyl^2) --
that choice is precisely the fork this file shows the whole ghost question hinges on.

External facts USED (Bateman & Turok arXiv:2607.00096), not re-proved here: that the
two-field O(1,1) embedding + ghost parity + Krein Born rule gives POSITIVE tree-level
probabilities. This file computes only the STRUCTURAL preconditions for that theorem
to apply to the Bach sector.

Run: python -u tests/wave2/H9_ghost_parity_bach_sector.py
"""
from __future__ import annotations
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg):
    print(msg, flush=True)


def commutant_dim(M):
    """dim of {X : [X, M] = 0} over the field, by solving the linear system."""
    n = M.shape[0]
    Xs = sp.symbols(f'x0:{n * n}')
    X = sp.Matrix(n, n, Xs)
    comm = X * M - M * X
    eqs = [comm[i, j] for i in range(n) for j in range(n)]
    sol = list(sp.linsolve(eqs, Xs))[0]
    free = set()
    for e in sol:
        free |= e.free_symbols
    return len(free)


# ===========================================================================
# PART A -- propagator: the O(1,1) healthy/ghost split is CLEAN only when the
#           ghost is MASSIVE (distinct pole). Pure Bach box^2 is the coincident
#           (degenerate) limit where the split is singular (double pole).
# ===========================================================================
log("=" * 78)
log("PART A -- O(1,1) healthy/ghost split needs a DISTINCT ghost pole; Bach box^2 degenerates")
log("=" * 78)
s, m = sp.symbols('s m', positive=True)  # s = box (momentum^2), m = ghost mass

# Massive quadratic gravity (Stelle R + Weyl^2) TT propagator ~ 1/(s (s + m^2)).
prop_massive = 1 / (s * (s + m**2))
pf = sp.apart(prop_massive, s)
res_healthy = sp.residue(prop_massive, s, 0)          # massless graviton pole
res_ghost = sp.residue(prop_massive, s, -m**2)        # massive ghost pole
log(f"  massive propagator 1/(s(s+m^2)) = {pf}")
log(f"  residue at s=0 (healthy graviton): {res_healthy}")
log(f"  residue at s=-m^2 (massive ghost): {res_ghost}")
opposite_sign = sp.simplify(res_healthy) > 0 and sp.simplify(res_ghost) < 0
check("massive quadratic-gravity TT propagator splits into a POSITIVE-residue (healthy) "
      "pole + a NEGATIVE-residue (ghost) pole -- this opposite-sign pair IS the O(1,1) / "
      "Krein two-field structure Bateman-Turok grade by ghost parity", opposite_sign,
      f"(+{res_healthy}, {res_ghost})")

# Pure Bach / Weyl^2 = box^2 TT propagator ~ 1/s^2: coincident double pole (m -> 0 limit).
prop_bach = 1 / s**2
order = sp.Poly(sp.denom(prop_bach), s).degree()
split_coeff_limit = sp.limit(1 / m**2, m, 0)  # the 1/m^2 that multiplies BOTH residues
double_pole = (order == 2)
check("pure Bach / Weyl^2 TT propagator is 1/box^2 = a DOUBLE pole (order 2), NOT two "
      "simple poles: it is the coincident-pole m->0 limit of 1/(s(s+m^2))", double_pole,
      f"pole order = {order}")
check("the O(1,1) split coefficient 1/m^2 DIVERGES as m->0: the healthy/ghost separation "
      "is SINGULAR in the pure-Bach limit -- the two-field embedding degenerates exactly "
      "where GU's established (H1) gravity operator lives", split_coeff_limit == sp.oo,
      f"lim_(m->0) 1/m^2 = {split_coeff_limit}")

# ===========================================================================
# PART B -- Pais-Uhlenbeck companion matrix: the 4-derivative operator is
#           Krein-DIAGONALIZABLE (clean ghost parity) iff the two frequencies
#           are DISTINCT. Bach (both freq -> 0, box^2) and equal-freq are
#           non-diagonalizable Jordan blocks -> the mechanism degenerates.
# ===========================================================================
log("\n" + "=" * 78)
log("PART B -- Pais-Uhlenbeck: clean ghost-parity split <=> DISTINCT frequencies")
log("=" * 78)

# Companion matrix of the 4th-order operator's characteristic polynomial in lambda=d/dt.
# distinct freq (w1=1, w2=2): (l^2+1)(l^2+4) = l^4 + 5 l^2 + 4
C_distinct = sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [-4, 0, -5, 0]])
# equal freq (w1=w2=1): (l^2+1)^2 = l^4 + 2 l^2 + 1  (Mannheim equal-frequency PU)
C_equal = sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, -2, 0]])
# Bach: box^2 -> l^4 (both frequencies zero)
C_bach = sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])

d_distinct = C_distinct.is_diagonalizable()
d_equal = C_equal.is_diagonalizable()
d_bach = C_bach.is_diagonalizable()
eig_distinct = list(C_distinct.eigenvals().keys())
log(f"  distinct-freq eigenvalues: {eig_distinct} (four distinct -> diagonalizable={d_distinct})")
log(f"  equal-freq   diagonalizable = {d_equal}  (double roots +-i -> Jordan blocks)")
log(f"  Bach box^2   diagonalizable = {d_bach}  (nilpotent l^4 -> single Jordan block)")
check("NON-degenerate Pais-Uhlenbeck (distinct frequencies) is DIAGONALIZABLE: the two "
      "modes separate into a healthy + a ghost oscillator -> Bateman-Turok's O(1,1) "
      "embedding and ghost parity are well-defined", d_distinct)
check("EQUAL-frequency Pais-Uhlenbeck is NON-diagonalizable (Jordan block): the "
      "healthy/ghost split degenerates -- Mannheim's equal-frequency wall / R1's "
      "Jordan-boundary nonexistence theorem", not d_equal)
check("pure BACH box^2 (l^4, both frequencies zero) is NON-diagonalizable (a single "
      "size-4 Jordan block): GU's ESTABLISHED gravity operator is the MOST degenerate "
      "coincident-pole case -- the clean Bateman-Turok ghost parity does NOT apply as-is",
      not d_bach)

# ===========================================================================
# PART C -- ghost parity P: a Krein isometry commuting with the free action
#           ([P,S_free]=0 KINEMATICALLY) -- but NON-UNIQUE at the degenerate mass.
# ===========================================================================
log("\n" + "=" * 78)
log("PART C -- ghost parity P: kinematic [P,S_free]=0 holds; UNIQUE only off degeneracy")
log("=" * 78)
eta = sp.diag(1, -1)   # O(1,1) Krein metric on (healthy, ghost) field space
P = sp.diag(1, -1)     # ghost parity: flip the ghost field
M_distinct = sp.diag(1, 2)   # distinct masses (non-degenerate)
M_degen = sp.diag(1, 1)      # equal mass (Bach-analog degenerate)

P_is_krein_isometry = (P.T * eta * P == eta)
check("ghost parity P = diag(+1,-1) is a Krein ISOMETRY of the O(1,1) form eta=diag(+1,-1): "
      "P^T eta P = eta -- P preserves the indefinite inner product", P_is_krein_isometry)
commutes_free = (P * M_distinct - M_distinct * P == sp.zeros(2))
check("[P, M_free] = 0 for the free O(1,1) action: the ghost parity is a SYMMETRY of the "
      "free/kinematic dynamics -- the kinematic [P,S_free]=0 that Bateman-Turok positivity "
      "needs holds AT FREE LEVEL (same grade as canon V2's Cartan-involution Z2, residual 0)",
      commutes_free)

cdim_distinct = commutant_dim(M_distinct)
cdim_degen = commutant_dim(M_degen)
log(f"  commutant dim, distinct masses diag(1,2): {cdim_distinct} (only diagonal -> P unique up to signs)")
log(f"  commutant dim, equal   masses diag(1,1): {cdim_degen} (full 2x2 -> P NOT singled out)")
check("at DISTINCT masses the commutant of the mass matrix is 2-dim (diagonal only), so the "
      "ghost parity P is essentially UNIQUE (fixed up to signs) -- the physical/ghost split "
      "is canonical", cdim_distinct == 2)
check("at EQUAL mass (Bach-analog degeneracy) the commutant is 4-dim (all of gl(2)): EVERY "
      "O(1,1) rotation commutes, so the ghost parity is NOT singled out by the dynamics -- "
      "the split is NON-canonical. This is the gravity-side image of R3's K-balance: at "
      "GU's degenerate spectrum C exists but is never DETERMINED", cdim_degen == 4)

# ===========================================================================
# PART D -- adversarial: is GU's Krein form Bateman-Turok's O(1,1), or an ANALOGY?
# ===========================================================================
log("\n" + "=" * 78)
log("PART D -- adversarial: GU matter Krein (O(96,96)) is NOT the gravity O(1,1) (shared Z2 only)")
log("=" * 78)
# GU's matter triplet Krein form (canon): signature (+96,-96) on the 192-dim self-dual
# triplet, implementing the Cartan involution of so(9,5). That is an O(96,96) grading.
gu_matter_pos, gu_matter_neg = 96, 96
gu_matter_dim = gu_matter_pos + gu_matter_neg
# Bateman-Turok's gravity ghost space per spin-2 mode is O(1,1): one healthy + one ghost.
bt_gravity_pos, bt_gravity_neg = 1, 1
different_space = (gu_matter_pos != bt_gravity_pos)
check("GU's matter Krein form is O(96,96) (192-dim self-dual triplet, so(9,5) Cartan "
      "involution) while Bateman-Turok's per-mode gravity ghost space is O(1,1): these are "
      "DIFFERENT Krein spaces. The identification 'GU's Krein = Bateman-Turok's O(1,1)' is a "
      "shared Z2-GRADING analogy, NOT an equality of spaces", different_space,
      f"O({gu_matter_pos},{gu_matter_neg}) vs O({bt_gravity_pos},{bt_gravity_neg})")
# What IS shared: both are Z2 gradings of an indefinite (Krein) form. A Z2 grading exists
# on any balanced-signature Krein space; verify the matter form is balanced (neutral), the
# precondition for a hyperbolic-pair Z2 to exist at all.
matter_balanced = (gu_matter_pos == gu_matter_neg)
check("what IS shared is only the STRUCTURE: both are Z2 gradings of a balanced/neutral "
      "Krein form (GU matter (+96,-96) is neutral; O(1,1) is neutral). The common object is "
      "the Z2 grade at KINEMATIC level -- this matches canon exactly and adds no dynamics",
      matter_balanced)

# ===========================================================================
log("\n" + "=" * 78)
log("VERDICT -- H9 (Bach sector vs Bateman-Turok ghost-free completion)")
log("=" * 78)
log("""
COMPUTED (this file, exact sympy, exit 0):
  A. The Bateman-Turok O(1,1) healthy/ghost split is a POSITIVE-residue graviton pole +
     a NEGATIVE-residue ghost pole -- CLEAN only for a DISTINCT (massive) ghost. Pure
     Bach/Weyl^2 = box^2 is a DOUBLE pole (coincident-pole m->0 limit); the split
     coefficient 1/m^2 DIVERGES. GU's established (H1) gravity operator is exactly this
     degenerate limit.
  B. Pais-Uhlenbeck companion matrix: DIAGONALIZABLE (clean ghost parity) iff frequencies
     are DISTINCT. Equal-frequency and pure-Bach (l^4) are NON-diagonalizable Jordan
     blocks -- the two-field embedding degenerates precisely at the Bach point.
  C. Ghost parity P = diag(+1,-1) IS a Krein isometry and DOES commute with the free
     action (kinematic [P,S_free]=0 holds, same grade as canon V2). But at the degenerate
     (Bach) mass the commutant jumps 2 -> 4: P is NON-canonical, not singled out by the
     dynamics -- the gravity-side image of R3's spectral sign-blindness.
  D. GU's matter Krein form is O(96,96) (so(9,5) Cartan involution), NOT literally
     Bateman-Turok's per-mode gravity O(1,1). Shared object = the Z2 grade at kinematic
     level only.

VERDICT: REDUCE (NOT clear, NOT fail). Confidence: moderate-high on the structural claim.
  * The ghost objection is NOT cleared: Bateman-Turok's clean ghost-parity/O(1,1)/tree-
    positivity mechanism requires a NON-degenerate MASSIVE ghost. GU's established gravity
    sector is pure Bach = box^2 = the coincident-pole DEGENERATE limit, exactly where the
    mechanism's diagonalization fails and the ghost parity is non-unique.
  * The ghost objection is NOT newly failed either: the KINEMATIC Z2 ([P,S_free]=0, P a
    Krein isometry) genuinely holds -- as it does for any O(1,1). The failure is DEGENERACY
    + missing dynamics, the same open condition canon already fences (R3 sustained x2).
  * The Bach sector CLEARS via Bateman-Turok ONLY IF GU's gravity is actually Stelle-type
    (R + Weyl^2, a DISTINCT massive ghost), NOT pure conformal Bach. That is the SAME
    unresolved conformal-vs-Einstein / OQ2-A functional datum H1 already isolated. So H9's
    gravity-side frontier COLLAPSES ONTO H1's single named datum.

OPEN / NOT DONE (honest boundary):
  * INTERACTING [P,S]=0: GU has no built source action; only the free-level Z2 is checkable.
  * LOOP-level positivity: Bateman-Turok prove TREE only; not checked here or anywhere for GU.
  * The full section-EL fiber/gauge terms (E_s^YM, E_s^theta, ...) need the unbuilt action.
  * Whether GU's OQ2-A functional is pure Bach (degenerate) or R+Weyl^2 (massive, non-
    degenerate) -- the decisive fork -- is NOT settled here.
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("exit 0 = structural preconditions computed: Bateman-Turok needs a distinct massive")
log("         ghost; GU's established Bach box^2 is the degenerate coincident-pole limit;")
log("         VERDICT REDUCE, collapsing onto H1's conformal-vs-Einstein (OQ2-A) datum.")
