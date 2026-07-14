---
artifact_type: exploration
status: exploration
created: 2026-07-13
hypothesis: H59 / H61a (W78 follow-through -- the last finite-scale positivity-side open item)
branch: "W122 -- GAUGE-vs-PHYSICAL status of the spin-0 conformal-mode sign, settled by the EXACT auxiliary-field (Legendre) route + the spin-0 projection of Weyl^2, with the Euclidean conformal-factor problem cleanly DELINEATED from the Lorentzian scalaron mass sign. Third independent leg on top of W78 (constraint/Weyl-BRST) and W79 (norm-sign + vacuum)."
title: "VERDICT: PHYSICAL-UNGRADED-BUT-POSITIVE-NORM (not a gauge artifact; nothing for keep-and-grade to grade; a genuine spectral instability of the Krein-TT leg only). Exact results, no perturbative expansion anywhere: (1) Weyl^2 contributes ZERO spin-0 -- the Weyl tensor vanishes identically on conformal metrics e^{2phi}eta (exact, all orders) AND the linearized Weyl tensor vanishes on the entire spin-0 polarization sector {eta, k x k}; (2) pure EH's conformal reduction is KINETIC-ONLY (sqrt(-g)R[e^{2phi}eta] = 6 e^{2phi}(dphi)^2 + total derivative, EXACT; no mass term) -- THAT kinetic sign is the object of the Euclidean/GHP conformal-factor problem, and it contains no mass parameter, so the 'gauge artifact' escape is category-inapplicable to a MASS sign; (3) adding f_0^2 R^2 adds EXACTLY ONE scalar via the exact Legendre map f_0^2 R^2 == f_0^2(2 chi R - chi^2), canonical (+1/2, POSITIVE-NORM) in Einstein frame, with m_0^2 = gamma/(6 f_0^2) (canonical-V_E'' and f(R)-formula routes agree; the derivation contains NO gauge parameter -- m_0^2 is a potential-curvature invariant, so gauge-parameter dependence has nowhere to enter); (4) on the AF trajectory the W46 ratio quadratic has BOTH roots negative and f_2^2 > 0, so f_0^2 (the R^2 coefficient -- a SIGNED coupling despite the square notation) is the one that is negative => m_0^2 < 0 trajectory-wide, fork-independently (agravity AND fixed-scale ghost-mass branches). W119's flag 'plausibly a gauge artifact / W78 remains THE open item' was stale (W78+W79 had answered it); W122 closes the remaining escape."
grade: "exploration / DERIVED, exact within the 4th-order truncation: every claim is an exact sympy identity (conformal Weyl vanishing; spin-0-sector linearized Weyl vanishing; the kinetic-only conformal reduction of EH; the Legendre map; the Einstein-frame mass and its two-route agreement; the W46 ratio roots). LOAD-BEARING imports (cited, not re-derived): f_0^2 < 0 on the AF trajectory (W45-47 ported one-loop betas; W119 Vieta: no admissible regulator dressing flips the ratio sign), gamma > 0 (H25), the 4th-order landing (H49). Ghost-mass construction fork carried: sign(m_0^2) < 0 on BOTH branches. Gauge-independence is established at the pole/invariant level (the Legendre route is gauge-parameter-free and residue/pole facts are gauge-fixing-independent by the standard Nielsen-identity argument); a direct two-parameter (alpha, sigma) propagator sweep on the full 10-component flat-space quadratic action was built and its exact-diffeo-invariance validation PASSED, but the full symbolic inversion exceeded the session compute budget and is NOT shipped as a claim -- named as the one untested corroboration, not load-bearing. Deterministic test tests/W122_spin0_scalaron_auxfield.py, 27 checks, exit 0, with positive controls (Starobinsky healthy scalaron; nonzero Ricci on conformal metrics; nonzero linearized Riemann on TT polarizations; W46 root values reproduced). NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59/H61a remain OPEN."
depends_on:
  - explorations/conformal-factor-mode-gauge-status-2026-07-11.md
  - explorations/scalaron-normsign-and-vacuum-2026-07-11.md
  - explorations/h59-frg-minimal-truncation-krein-negative-ratio-2026-07-13.md
  - explorations/path2-wave2-target1-af-flow-vs-exceptional-locus-2026-07-11.md
  - tests/W46_H57_stage2_fixed_point.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W122_spin0_scalaron_auxfield.py
external_refs:
  - "Gibbons, Hawking & Perry, NPB 138 (1978) 141 -- Euclidean conformal-factor contour rotation"
  - "Mazur & Mottola, NPB 341 (1990) 187 -- conformal-factor measure/quantization"
  - "Stelle, PRD 16 (1977) 953 -- fourth-order gravity spectrum 2+5+1"
  - "Salvio & Strumia, JHEP 06 (2014) 080 -- agravity: scalaron positive-norm, ghost spin-2 only"
  - "De Felice & Tsujikawa, Living Rev. Rel. 13 (2010) 3 -- f(R) scalaron mass/no-ghost conditions"
  - "Nielsen, NPB 101 (1975) 173 -- gauge-parameter independence of pole-level quantities"
---

# W122 -- The spin-0 conformal-mode sign: gauge escape closed by the exact route

**Role.** W119 confirmed the spin-2 Krein grading is RG-stable at FRG-truncation level and left one
line standing: *"the spin-0 conformal-mode sign (M_0^2 < 0 on the AF trajectory) ... W78's
physical-vs-gauge question remains THE open item,"* flagged "plausibly a gauge artifact." That flag was
**stale**: W78 had already proven NOT-gauge two ways (DOF/constraint count; Weyl-BRST + GHP-scope, with
the H49 fork-closure), and W79 had already derived the norm-sign (POSITIVE -- tachyon, not ghost) and the
background-independence of the tachyon (no vacuum lift). W122 closes the one channel a "gauge artifact"
reading could still hide in -- gauge-fixing/quantization-level dependence -- by a route where a gauge
parameter provably has nowhere to enter, and cleanly delineates the Euclidean conformal-factor problem
(which IS about a gauge/contour choice) from GU's Lorentzian scalaron mass sign (which is not).

Five personas inline, one context. Deterministic test: `tests/W122_spin0_scalaron_auxfield.py`
(27 checks, exact sympy, exit 0).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Why |
|---|---|---|
| **Gravity functional** | induced `\|II\|^2` -> 4th-order class `gamma R + f_0^2 R^2 + f_2^2 C^2` (H49/H57-stage1) | The standing physics-side representation of the induced action (W83/W88/W119). The induced-vs-free fork was carried by W79; it fixes `gamma > 0` (H25), which is what makes the scalaron positive-norm. |
| **Which coupling carries the sign** | READ OFF from W45-47/W46: the fixed ratio `r* = f_0^2/f_2^2 < 0` (both roots, reproduced exactly) with `f_2^2 > 0` on the AF branch (`1/f_2^2` grows linearly, W119) `=> f_0^2 < 0`. | The notation `f_0^2` suggests a positive square; in the repo's convention it is a SIGNED coupling, and it -- not `f_2^2` -- is the negative one. Stated explicitly so no reader mistakes the ratio sign for an `f_2` statement. |
| **Ghost/scalaron mass normalization** | BOTH branches: agravity (`m^2 ~ f_0^2 M_Pl^2`) and GU-native fixed-scale (`gamma/(6 f_0^2)` in `mu_DW` units) | Carried, not defaulted: `sign(m_0^2) < 0` on BOTH (tested). The fork moves magnitude/scale only. |
| **Positivity object** | Krein keep-and-grade `[P,S] = 0` | The question is whether the grading machinery can absorb the spin-0 mode. Answer (Section 4): nothing to grade -- the mode's kinetic term is canonically `+1/2`; grading acts on norms and cannot move a pole. |

## 1. Persona 1 -- QG theorist: which parts of the standard conformal-factor problem apply?

The "conformal-factor problem" bundle has three members. The test separates them **computationally**:

1. **The GHP/Euclidean object (does NOT apply).** The exact conformal reduction of Einstein gravity is
   *kinetic-only*: `sqrt(-g) R [e^{2 phi} eta] = 6 e^{2 phi} (d phi)^2 + total derivative` -- an exact
   identity (test 1c; the coefficient solved for, not inserted; convention fixes only its sign). The
   Euclidean conformal-factor problem (GHP contour rotation; Mazur-Mottola measure) is entirely a
   statement about the SIGN OF THIS KINETIC TERM for a mode that the second-order constraint analysis
   removes (W78). **It contains no mass parameter at all** -- the reduction has provably no potential
   term -- so a contour/measure/gauge choice in that problem cannot say anything about a scalaron MASS
   sign. The two problems share no parameter.
2. **The Lorentzian fourth-order spectrum (DOES apply -- Stelle).** With `f_0^2 != 0` the theory has
   2+5+1 propagating DOF and the +1 is the scalaron. GU's Krein keep-and-grade targets the spin-2
   member; the spin-0 member is positive-norm and needs no grading -- what it needs, and lacks on the AF
   trajectory, is a positive mass-squared.
3. **The Lorentzian-vs-Euclidean distinction, sharpened.** GU's Krein setup is Lorentzian; there is no
   Euclidean contour to rotate, and the pathology is a *pole location* (`m_0^2 < 0`), not a Euclidean
   kinetic sign. This is the same category distinction W78 drew; here it is backed by the exact
   kinetic-only identity rather than by literature scope.

## 2. Persona 2 -- BRST/gauge-fixing specialist: the DOF count, exact route

The count is assembled from three exact facts (no perturbative expansion anywhere):

- **Weyl^2 contributes NO spin-0.** Two exact computations: (i) the Weyl tensor of an arbitrary
  conformal metric `e^{2 phi(t,z)} eta` vanishes identically -- all 256 components, exact in `phi`
  (positive control: the Ricci scalar of the same metric is nonzero); (ii) the **linearized** Weyl
  tensor vanishes on the ENTIRE spin-0 polarization sector `eps = phi0 eta + B k (x) k` (the two
  covariant scalars spanning `P^0_s`, `P^0_w`), with a negative control (nonzero linearized Riemann on a
  TT polarization). So the `C^2` quadratic form has zero spin-0 part: **Einstein + Weyl^2 propagates no
  scalar** -- the brief's positive control, verified.
- **Pure EH propagates no spin-0.** The conformal reduction is kinetic-only for a constrained mode
  (Section 1; the constraint count is W78's, unchanged).
- **`f_0^2 R^2` adds EXACTLY ONE scalar.** The auxiliary-field map is exact:
  `f_0^2 R^2 == f_0^2 (2 chi R - chi^2)` with `chi = R` the unique auxiliary solution (Legendre, test
  2a). One auxiliary scalar in, one propagating scalar out; the Einstein-frame reduction gives it a
  canonical `+1/2` kinetic term (POSITIVE NORM, valid iff `f'(R) > 0`, i.e. `gamma > 0` near flat --
  H25), and mass

  `m_0^2 = gamma / (6 f_0^2)`

  by TWO independent routes that agree exactly: the canonical Einstein-frame `V_E''` at the unique
  extremum `Phi* = gamma` (the flat point), and the `f(R)` formula `(1/3)(f'/f'' - R)`. (The two differ
  by the positive frame factor `1/gamma`, so the SIGN is route-independent -- checked.)

**DOF count: 2 (graviton) + 5 (Weyl^2 massive spin-2, the Krein-graded ghost) + 1 (scalaron) = 8, with
the +1 present iff `f_0^2 != 0`.** This reproduces Stelle and W78's canonical count by a third,
independent formalism.

**Mass-squared sign as a function of the couplings:** `sign(m_0^2) = sign(gamma / f_0^2)`. Starobinsky
control: `f_0^2 = +1 => m_0^2 = +1/6 > 0` (healthy inflaton). GU: `gamma > 0` (H25), `f_0^2 < 0`
(W45-47) `=> m_0^2 < 0`: tachyon, positive-norm.

## 3. Persona 3 -- FRG practitioner: is `m_0^2 < 0` trajectory-wide, and can a gauge parameter move it?

- **Trajectory-wide.** The W46 ratio quadratic `(5/6) r^2 + (5 + b_2) r + 5/3 = 0` with
  `b_2 = 133/10 + 17/12` has both roots real and negative (`r* = -0.0848, -23.575`, reproduced exactly);
  `f_2^2 > 0` all along the AF branch, so `f_0^2 = r* f_2^2 < 0` on BOTH roots at every finite scale.
  W119's Vieta argument (imported) closes the regulator channel: no admissible dressing flips the ratio
  sign. So `m_0^2 < 0` is not a point statement -- it holds along the whole trajectory, at every
  admissible regulator.
- **Gauge-parameter channel, closed at the invariant level.** The Legendre/Einstein-frame derivation
  never introduces gauge fixing: `chi` is a diffeomorphism scalar, and `m_0^2` is the curvature of a
  scalar potential at its extremum -- checked in the test by the blunt criterion that the derived
  `m_0^2`'s free symbols are a subset of the couplings `{gamma, f_0^2}`. A gauge parameter has nowhere
  to enter. This is the concrete face of the standard Nielsen-identity statement: pole locations and
  residue signs of gauge-invariant correlators are gauge-parameter independent; only contact/off-shell
  pieces move.
- **Honest disclosure of the not-landed corroboration.** A direct two-parameter `(alpha, sigma)`
  propagator sweep on the full 10-component flat-space quadratic action (exact second-order metric
  expansion, no ported Fierz-Pauli) was built this session; its validation gate -- exact linearized
  diffeomorphism invariance of the derived quadratic action -- PASSED, but the full symbolic saturated-
  amplitude inversion exceeded the session's compute budget and its claims are NOT asserted here. It is
  corroboration-in-waiting, not load-bearing: the shipped gauge-independence argument stands on the
  gauge-parameter-free route above.

**Sweep-question outcome: `m_0^2 < 0` is trajectory-wide and CANNOT be gauge-parameter dependent,
because the quantity is derived in a formulation in which no gauge parameter exists.** Evidence for
"artifact": none, in the last channel it had left.

## 4. Persona 4 -- Krein specialist: does keep-and-grade extend to the scalaron?

Two computed facts decide it:

1. **There is nothing to grade.** The scalaron's Einstein-frame kinetic term is canonically `+1/2`
   (positive norm) whenever `gamma > 0` -- and `gamma > 0` is forced by the induced construction (H25),
   not chosen. The keep-and-grade parity structure assigns it grade `+1`: it sits *inside* the graded
   algebra, in the trivial sector. No exotic parity sector is needed, and none would help.
2. **Grading cannot move a pole.** The grading operator acts on norms/residues; the pole location
   `m_0^2 = gamma/(6 f_0^2)` carries no grading label. A tachyonic pole means imaginary frequencies for
   soft modes (`omega^2 = |k|^2 + m_0^2 < 0` for `|k|^2 < |m_0^2|`) under ANY norm assignment: the
   modular/`Delta` spectrum in the spin-0 sector is non-real (PT-broken), a SPECTRAL statement outside
   the reach of a norm-side machine.

So: **vacuously yes (grade +1), effectively no** -- the construction was built to cure indefinite norms
and does cure the spin-2 sector; the scalaron's pathology is of a different type. This is exactly W79's
split, restated structurally: loop-POSITIVITY (norm) is untouched; Krein-TT (real spectrum) is
obstructed.

## 5. Persona 5 -- adversarial skeptic: the honest negative at full strength

**Steelman of "physical and uncaught."** The strongest honest reading stands: GU's AF trajectory
carries a genuine propagating positive-norm scalar with `m_0^2 < 0` that is (i) not gauge -- three
independent legs (constraint count W78; Weyl-BRST + H49 fork-closure W78; the gauge-parameter-free
invariant derivation here), (ii) not background-liftable (W79: `m_0^2` is exactly `R`-independent),
(iii) not regulator-liftable (W119 Vieta), (iv) not Krein-liftable (Section 4). Within the 4th-order
truncation on the ported betas this is a real instability of every background, and the Krein
construction does not catch it. **The observer-conjecture Krein-TT leg's first genuine no-go (W79)
stands, strengthened.**

**Where the skeptic must stop.** Verdict (c) as posed ("physical and UNGRADED -- a genuine instability
the Krein construction does not catch") is correct ONLY with the norm qualifier: the mode is
positive-norm, so the casualty is the stability/real-spectrum leg, NOT loop-positivity. Calling it an
uncaught *ghost* would be wrong on the computation; calling it an uncaught *instability* is exactly
right.

**Surviving escape routes (named, not defeated):**
1. `f_0^2 < 0` is PORTED (W45-47 one-loop betas). If GU's *native* induced `R^2` running has the
   opposite sign, the tachyon evaporates. Still the single number the no-go rests on.
2. The 4th-order truncation (H49 landing): beyond-4th-order `|II|^2` invariants giving non-constant
   `f''(R)` would break W79's background-independence and re-open vacuum lifting.
3. Non-perturbative condensation of the tachyonic mode (the mean-field/vacuum-shift version is closed by
   W79; a qualitatively non-perturbative mechanism is not, and none is currently on the table).

## 6. Verdict

**PHYSICAL-UNGRADED-BUT-POSITIVE-NORM** (the brief's option (c), with the norm qualifier that keeps it
honest):

- **NOT (a) GAUGE-ARTIFACT.** Closed three independent ways; the Euclidean conformal-factor problem --
  the only setting where "gauge/contour artifact" is the right verdict -- is computationally delineated:
  its object is a massless, kinetic-only, constrained mode, sharing no parameter with the scalaron mass.
- **NOT (b) PHYSICAL-GRADED.** The keep-and-grade machinery grades it trivially (+1); it is not a
  second graded-ghost sector and the grading contributes nothing to its fate.
- **(c), refined: a genuine, propagating, positive-norm tachyon** -- gauge-independent,
  background-independent, regulator-robust, fork-independent (`m_0^2 < 0` on both ghost-mass branches)
  -- that the Krein construction cannot catch because its pathology is spectral, not norm. Casualty:
  the observer-conjecture Krein-TT leg (W79's first genuine no-go, confirmed). Untouched: the UV
  loop-positivity leg.

**Stale-flag repair (bookkeeping; no retro-edit of W119's file):** W119's "W78's physical-vs-gauge
question remains THE open item" should be read as pointing at what is now W79's residual: the sign of
GU's NATIVE `R^2` running.

## 7. What would settle the remainder

1. **The native `f_0^2` sign** (unchanged, now the unique load-bearing number): derive the `R^2` beta
   function from the induced `|II|^2` geometry directly, instead of the ported one-loop system.
2. **Beyond-4th-order `f''(R)`**: any non-constant `f''` from higher `|II|^2` invariants re-opens
   vacuum lifting.
3. Optionally, land the direct `(alpha, sigma)` propagator sweep as corroboration (built, validated at
   the Ward-identity gate, not yet run to completion; a compute-budget item, not a conceptual one).
4. Nothing further on the gauge side: constraint, BRST, and invariant-derivation legs all agree; the
   channel is exhausted.

## What this does NOT do

No loop amplitude (W48 gate). No canon / RESEARCH-STATUS / claim-status / verdict / posture change; no
edit to W119's file. H59/H61a remain **OPEN**. The no-go remains conditional on `f_0^2 < 0` (ported)
and the 4th-order truncation (H49), exactly as in W79.
