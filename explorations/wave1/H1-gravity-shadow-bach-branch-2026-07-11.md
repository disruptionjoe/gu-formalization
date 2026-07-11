# H1 -- Gravity shadow test in the conformal/Bach branch (ELProjectedGRShadowTheorem)

Wave-1 swing (Condorcet #1). `tests/wave1/H1_bach_flat_exact_vacua.py` (exit 0). Question: does the H-class
(conformal / Bach) gravity section-EL residual VANISH on an imported exact vacuum -- exact Schwarzschild, then
Kerr -- at all orders? The Willmore-ONLY branch was BLOCKED at strong field
(`explorations/geometry-curvature-emergence/exact-schwarzschild-kerr-el-gate-2026-06-24.md`).

## What was computed (exact sympy, from scratch: Christoffel -> Riemann -> Weyl -> nabla nabla C -> Bach)

- **PART 1:** for any Einstein metric (`Ric = Lambda g`) the algebraic Bach term `(1/2)R^{cd}C_{acbd}` vanishes
  because the Weyl tensor is trace-free (`g^{cd}C_{acbd}=0`). Verified on a generic metric.
- **PART 2 (DECISIVE):** on EXACT Schwarzschild (all orders in M) the divergence of the Weyl tensor
  `nabla^d C_{acbd}` is **identically zero** (0 of 64 components nonzero, robust zero-test), while the Weyl
  tensor itself is **nonzero** (genuine strong-field curvature). Since `Ric = 0`, the full nonlinear Bach
  tensor `B_ab = nabla^c(div-Weyl) + (1/2)R^{cd}C = 0` **exactly, at all orders**. This is a real strong-field
  cancellation, not triviality.
- **PART 3:** exact Kerr (Boyer-Lindquist, general `a`) is **Ricci-flat** -- verified as an exact
  rational-function identity in `(r, M, a)` at four independent exact `theta` slices (`pi/3, pi/4, pi/6,
  pi/5`); Ricci is assembled with no intermediate simplification and differentiation precedes the `theta`
  substitution, so this is an all-orders check in `(r, M, a)` (full trig-symbolic simplification of Kerr is
  intractable, hence the exact-slice route). Ricci-flat => Einstein => Bach-flat by the same
  `Schouten P = 0 => Cotton = 0 => div-Weyl = 0 => Bach = 0` mechanism Part 2 exhibits and verifies on the
  Ricci-flat Schwarzschild member.
- **PART 4 (adversarial, the honest reduction):** the H-class section-EL equals the Bach operator only on the
  spin-2 sector (D-thread `box^2 h = -4 Bach^(1)`). On the TRACE/conformal sector -- where Schwarzschild's
  linearized graph section `h_ab = (2M/r) eta_ab` lives -- Bach and the naive `|H|^2`-Willmore operator
  DIFFER. On the harmonic Schwarzschild mode both vanish (`box(M/r)=0`), but on a non-harmonic pure-trace
  mode the naive `box^2` is nonzero (`box^2(x^4)=24`) while Bach = 0 (conformally-flat -> Weyl = 0). So
  Bach-flatness clears the exact vacua for BACH gravity, and for GU-proper ONLY IF its OQ2-A functional is
  the conformally-invariant Willmore combination (= Bach on all sectors), not the naive `|H|^2`.

## Verdict -- REDUCTION, not a full clear (honest)

- **Bach/conformal gravity passes the exact-vacuum gate decisively:** the Bach tensor of exact Schwarzschild
  is identically zero at all orders (nonzero Weyl -> a genuine cancellation), and Kerr is Ricci-flat hence
  Bach-flat. The strong-field wall that BLOCKED the Willmore-only branch is CLEARED in the Bach branch.
- **The H-class GU pure-gravity/spin-2 residual vanishes on the exact vacua** (it IS the Bach operator on
  spin-2).
- **But it is a REDUCTION:** the standing `O(M^2/r^4)` obstruction (RFAIL-03) lives in the trace/conformal
  sector, where Bach and the naive `|H|^2` disagree. **Gravity CLEARS iff GU's OQ2-A functional is the
  conformally-invariant Willmore (Bach) combination.** That is exactly the single `c_W` / OQ2-A datum the
  source-action narrowing already isolated -- the gravity leg now depends on it, not on an unbuilt source
  action.

**Net:** the gravity wall moves from BLOCKED/unknown to **REDUCED to one named datum** -- is GU's H-class
functional the conformally-invariant Willmore combination? This is decidable by the higher-codimension Willmore
first variation (H4) and bears directly on "is GU just Bach gravity?" (H8).

## Re-ranking consequences (feeds M4)

- **H1 is resolved** into a reduction: gravity clears in the Bach branch, conditional on the conformal-
  invariance of the OQ2-A functional. Its follow-up merges into H4 and H8.
- **H4 (full Willmore first variation) rises** -- it now directly gates the gravity clear (does the functional
  annihilate the trace mode / equal Bach on all sectors?).
- **H8 (is GU just Bach?) rises** -- H1 showed Bach gravity passes; "is GU = Bach" is now live and could moot
  the source-action buildbench.
- Consistent with H3's independent finding (the corrected `M^2/r^6` residual comes from harmonic H, the
  H-class branch where gravity self-closes with no theta-source) -- two Wave-1 swings both point at the
  H-class / conformal reading.

## Grade
Computation-grade for the Bach-flatness of the exact vacua (exact sympy Schwarzschild all-orders in `M`;
Kerr Ricci-flat as an exact rational identity in `(r,M,a)` at four `theta` slices). Structural for the
GU-proper connection (linearized D-thread identity + the honest trace-sector reduction). The clear is
CONDITIONAL on the OQ2-A conformal-invariance datum -- stated, not assumed. No claim/canon movement; feeds
WI-068 and the re-rank.

### Adversarial self-checks recorded in the test
- Weyl confirmed **nonzero** on Schwarzschild, so the Bach vanishing is a real cancellation, not triviality.
- div-Weyl computed **from scratch** (one covariant derivative), not asserted from the Einstein-implies-Bach
  theorem; the theorem is what the numbers must reproduce.
- A `sympy.simplify` false-nonzero on two div-Weyl components (the trig identity
  `sin(2t)tan(t)+cos(2t)-1 == 0`) was caught by a stronger `expand_trig`/`factor` zero-test plus independent
  numeric evaluation -- the PASS uses the robust test, so "0 of 64 nonzero" is trustworthy.
- The sharpest objection -- *is Bach even the right residual for GU-proper?* -- is answered honestly by PART 4:
  no, not off spin-2. A naive "Bach=0 therefore GU clears Schwarzschild" would silently assume GU's functional
  is the conformal one; the REDUCE verdict exists precisely because that assumption is the remaining gate.

### On H2 (the signature crux) -- not displaced, promoted
H1 reduces the gravity leg without touching the `(9,5)` vs `(7,7)` signature question. By removing gravity
as the bottleneck it leaves rep-canonicity as the single highest-leverage open item (it decides both whether
the conformal reading is GU-native on the `(6,4)` DeWitt form and forced-vs-located generation count). And
inheriting Bach's exact vacua also inherits Bach's fourth-order **Ostrogradsky-ghost / unitarity** obligation
(`canon/ghost-parity-krein-synthesis.md`) -- a real cost of the identification, not a free win.
