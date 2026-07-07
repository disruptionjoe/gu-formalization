---
artifact_type: exploration
status: exploration
created: 2026-07-06
title: "Conformal-class synthesis (Mannheim/Bender-Mannheim PT swing): can the Bender-Mannheim PT/C-operator mechanism supply what GU's ghost-parity frontier is missing -- a dynamics-derived definiteness and a chiral physical sector -- and does the conformal-gravity-class action evade the known walls? HONEST OUTCOME: BLOCKED, bounded-negative, with theorem-grade sub-results. R1 (toy, adversarially verified PARTIAL): Bender-Mannheim's C and Turok-Bateman's ghost parity are ONE mechanism in two dresses -- the identical operator on the PT-unbroken, diagonalizable, SIMPLE-spectrum domain of the Pais-Uhlenbeck oscillator (0/28 sign mismatches, ||C - P_ghost|| -> 3e-8 at fixed window), failing together at the Jordan boundary where a two-line theorem excludes every positivity-compatible parity; but at resonant degeneracies (verifier's find) C EXISTS yet is NON-UNIQUE -- and spectral degeneracy is exactly GU's three-generation target regime, so derivedness does NOT transfer. R3 (SUSTAINED x2): on GU's verified 192-dim triplet carrier the Mannheim move is measurably UNAVAILABLE -- all GU-native cores are PT-UNBROKEN (nontrivially; random controls are PT-broken) but EVERY eigenspace is exactly K-balanced (+m/2,-m/2), so C exists and is never determined by the dynamics; plus a one-line THEOREM: {K,chi}=0 forces Re tr(chi Pi_+)=0 for EVERY admissible C -- no PT/Krein quantization of this arena yields a net-chiral physical sector in the chi-trace sense. R4 (SUSTAINED/PARTIAL): conformal gauge inherits both walls -- the quotient removes exactly the pure-trace PLUS direction ((+7,-3) -> (+6,-3), exact over the rationals, invariant form unique up to scale on the conformal tangent, isotropy still noncompact), and Weyl-squared-shaped blocks on the carrier are J_quat-commuting with Kramers-even triplet spectra (signature -64). No chiral physical sector found on any route; no forbidden target imported; the generation-count verdict stays OPEN."
grade: "exploration / BLOCKED (bounded negative) for the swing question, containing theorem-grade sub-results: (i) the R1 two-line nonexistence theorem at the Jordan boundary and the BM=TB operator identity at generic frequencies (toy scope, truncation-converged, adversarially reproduced with STRONGER numbers than claimed); (ii) the R3 achirality identity Re tr(chi Pi_+)=0 for every admissible C, from {K,chi}=0, re-derived by hand and on independent synthetic arenas by two verifiers; (iii) the R4 exact fiber signatures over the rationals and the pair-symmetry cancellation lemma (scope-qualified to the all-spacelike base per verifier). Verifier verdicts folded in and controlling: R1 PARTIAL x2 (resonance hole in the identity domain; existence-vs-uniqueness split in the sharpened canon condition; three wording downgrades), R3 SUSTAINED x2 (docstring-level defects only; PT-unbrokenness flagged as canon-xi-specific), R4 SUSTAINED + PARTIAL (complex-Weyl lemma scope-limited to the spacelike base; two audit-sentence corrections; wall conclusion untouched). All anchors reproduced on the verified Cl(9,5)=M(64,H) carrier (rank Gamma = 128, ker = 1664, bare 58.7215, C2 = 155.3625, triplet Krein signature (+96,-96,0), beta_S residual 0.0e+00). No forbidden target {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} assumed, inserted, hardcoded, or divided by in any load-bearing computation (two route audit sentences overclaiming '3 never appears' are corrected herein). chiral_physical_sector_found = false on all three routes; the generation-count verdict stays OPEN."
depends_on:
  - explorations/big-swing-2026-07-06/R1-pu-pt-vs-ghost-parity.md
  - explorations/big-swing-2026-07-06/R3-pt-phase-classification-gu-cores.md
  - explorations/big-swing-2026-07-06/R4-conformal-gauge-fiber-obstruction.md
  - canon/ghost-parity-krein-synthesis.md
  - explorations/generation-sector/mannheim-conformal-gravity-source-action-intake-2026-07-06.md
scripts:
  - tests/big-swing/cg_r1_pu_pt_vs_ghost_parity.py
  - tests/big-swing/cg_r3_pt_phase_gu_cores.py
  - tests/big-swing/cg_r4_conformal_fiber_obstruction.py
---

# Conformal-class synthesis: does the Bender-Mannheim mechanism supply what GU's ghost-parity frontier is missing?

**The swing.** `canon/ghost-parity-krein-synthesis.md` ends at one named open condition: GU's unbuilt
source action must realize the ghost parity as a symmetry of the dynamics, `[P_ghost, S] = 0`, and the
canon speculates this is "plausibly met if GU's source action is quadratic-gravity-like." The Mannheim
intake (2026-07-06) put the strongest known member of that class on the table: conformal (Weyl)
gravity, quantized by the Bender-Mannheim PT/C-operator mechanism -- the one construction in the
literature that *derives* the physical inner product from the dynamics' own spectral data rather than
importing it (BIG-SWING-1's fatal move). Three routes attacked the offer from three sides:

- **R1** -- mechanism identity: is Bender-Mannheim's dynamics-derived `C` the SAME `Z2` as the
  Turok-Bateman ghost parity the canon is built on, tested in the shared home arena (the
  Pais-Uhlenbeck fourth-order oscillator)?
- **R3** -- availability: is the Mannheim move (definiteness derived from spectra) actually available
  on GU's own verified carrier, for GU-native cores on the 192-dim self-dual triplet sector?
- **R4** -- the walls: does passing to the conformal class cure the fiber-metric obstruction
  ((+7,-3), noncompact isotropy) or the C-07 quaternionic-Kramers wall, or inherit them?

**Honest outcome: BLOCKED, bounded negative.** The mechanism is real and is the *same* mechanism the
canon already depends on (R1, theorem-grade in the toy) -- so the Mannheim intake adds no independent
second resolution; it adds a *derivation* of the object the canon consumes. But that derivation
measurably fails on GU's carrier (R3): every GU-native core is PT-unbroken yet spectrally sign-blind,
so `C` exists and is never determined by the dynamics -- the same missing datum, relocated. A one-line
theorem closes the chirality door for every admissible `C` under the chi-trace readout. And the
conformal-gravity-class action inherits both known walls unchanged (R4). No route produced a chiral
physical sector. The count stays OPEN.

Each route was adversarially verified by two independent agents (fresh runs from repo root, all exit 0,
every cited number reproduced from stdout; several claims independently re-derived by hand and by
disjoint methods). **Verifier verdicts control this synthesis: every claim a verifier damaged is stated
here in its downgraded form.**

---

## Anchors -- reproduced on the verified carrier before any claim

All three routes reproduced the standing anchors fresh (R1's arena is the PU toy; R3/R4 are on the true
1792-dim `Cl(9,5) = M(64,H)` carrier), and both verifiers per route re-ran them:

| anchor | reproduced (R3 / R4) | target |
|---|---|---|
| `rank(Gamma)` | **128** | 128 |
| `dim ker(Gamma)` | **1664** | 1664 |
| bare `||[Pi_RS, M_D]||` | **58.7215** | 58.7215 |
| `C2 = ||Gamma M_D Pi_RS||` | **155.3625** | 155.3625 |
| `beta_S` pseudo-anti-Hermiticity residual | **0.0e+00** | ~0 |
| triplet dim / Krein signature | **192 / (+96, -96, 0)** | 192 / (+96,-96,0) |
| `{K, chi}` (K purely cross-chiral) | **0.00e+00** | 0 |
| metric-fiber signature (BIG-SWING-1, re-derived not copied) | **(+7, -3, 0)** exact | (+7,-3) |
| R1 toy anchor: PU spectrum `E(n1,n2) = w1(n1+1/2)+w2(n2+1/2)` | `E0 = 1.5000000000`; window error `7.3e-6` at N=20 | exact |

---

## R1 -- Bender-Mannheim C vs Turok-Bateman ghost parity: one mechanism in two dresses

**Build grade: THEOREM (toy scope). Verifier verdicts: PARTIAL, PARTIAL.** The computation itself is
near-sustained -- both verifiers reproduced every printed number to the digit, confirmed the controls
genuinely discriminate (wrong parity mismatches 12/28; random pseudo-Hermitian input is refused with
30/40 complex eigenvalues), re-derived the two-line nonexistence theorem by hand, and one verifier's
fixed-window attack came out *stronger* than the doc's numbers (`||C - P_ghost|| = 3.0e-8` at N=20,
window held fixed; the doc's convergence report was conservative). Seed variation holds
(`max |p_TB - p_BM| ~ 2e-10`).

**What stands (with verifier-mandated qualifiers):**

- **CONDITIONALLY_SAME, with a sharpened domain.** On the PT-unbroken, diagonalizable,
  **simple-spectrum** domain (or degeneracies that do not mix ghost parity), BM's `C` -- built from
  eigenvector Krein-norm signs -- IS TB's `(-1)^{N_g}` -- built from the measured ladder algebra
  (`lambda_g = -0.2716 < 0`): 0/28 sign mismatches, operator identity converging with truncation,
  probability assignments identical to `5.8e-9`. The identity is structurally forced by the ladder
  algebra (a short theorem confirmed end to end, honestly disclosed as such).
- **The Jordan boundary kills both together.** At `w1 = w2` both mechanisms degenerate in lockstep
  (`min|nu| ~ eps^2.00`, `||C|| ~ eps^-2.00`, `|lambda_g| ~ eps^0.94`; Jordan splitting exponent 0.496
  vs 1.000 control), and the two-line theorem -- verified by hand by both verifiers -- excludes EVERY
  positivity-compatible ghost parity there: `P^2 = I`, `[P,H] = 0`, `eta P > 0` forces `H`
  diagonalizable with real spectrum, contradicting the measured Jordan block.

**Verifier downgrades (applied; these WIN over the build doc):**

1. **RESONANCE HOLE in the claimed identity domain.** At exact odd-rational frequency ratios
   (verifier's probe: `w1:w2 = 3:1`, spectrum real and diagonalizable, `w1 != w2`), degenerate levels
   mix opposite ghost parity and BM's spectral recipe becomes **basis-dependent and non-unique** (a
   hyperbolic family of valid `C`'s per mixed eigenspace) while TB's ladder parity stays canonical.
   The doc's "identical operator EXACTLY on the PT-unbroken / diagonalizable domain (w1 != w2)" is
   FALSE as stated; the correct domain is *simple spectrum or parity-non-mixing degeneracies*.
2. **Existence vs uniqueness split in the sharpened canon condition.** The correct statement:
   Krein-diagonalizability with real spectrum gives **EXISTENCE** of a positivity-compatible parity
   (converse demonstrated numerically in the toy, not proved as a theorem -- the theorem covers only
   the forward direction); **UNIQUENESS / derivedness additionally requires no parity-mixing
   degeneracy**. This qualifier is load-bearing for GU: the transfer target (three degenerate
   generations in the 192-dim triplet) is *precisely* the degenerate-spectrum regime, so the build
   doc's "the split of the 96 hyperbolic pairs into 3 physical + 3 ghost is canonical" is
   **unsupported as stated** and is withdrawn here. Canonicity would require GU's degeneracies not to
   mix ghost parity -- a condition never stated or tested.
3. **Priority claim partially inverts at resonant points** (there TB's ladder parity is the canonical
   object and BM's `C` needs an extra choice); "disjoint raw data" is an overstatement (only the
   sign-extraction data is disjoint); the grade string's "the number 3 does not appear" is literally
   false (innocuous `3`s exist; correct claim: 3 never enters as input, answer constant, or divisor);
   measured convergence is ~1.5 decades per +4 in N, not ~2.

**Net for the program:** the Mannheim intake's mechanism is the canon's mechanism -- one `Z2`, derived
where derivable. Neither gives GU a dynamics-free shortcut, and even *with* dynamics, derivedness fails
exactly in GU's degenerate target regime. GU transfer stays CONSISTENT_UNCOMPUTED.

---

## R3 -- the Mannheim move on GU's own carrier: measurably unavailable

**Build grade: BLOCKED (bounded negative) + one THEOREM-grade sub-result. Verifier verdicts:
SUSTAINED, SUSTAINED.** Both verifiers re-ran the full script (exit 0), reproduced every key number,
confirmed the classifier is not a tautology (three verdicts on three input classes: GU cores
UNBROKEN/NON-CANONICAL, random controls PT-BROKEN with 90-95 complex pairs at O(1) imaginary parts, the
non-GU definitizable control UNBROKEN with a DERIVED unique `C`, `min eig(KC) = 0.209`), and --
critically -- **independently re-derived the achirality theorem** by hand and on independent synthetic
arenas with their own code, including a converse control the route lacked (a K-*commuting* involution
gives `Re ~ O(1)`, proving the identity hinges exactly on `{K, chi} = 0`). That closes the build doc's
own stated gap ("not independently re-derived").

**What stands:**

- **All GU-native cores on the triplet are PT-UNBROKEN** -- real spectra, no Jordan blocks,
  K-nondegenerate eigenspaces -- and this is a measured specialness, not generic (random K-self-adjoint
  controls, even J-commuting ones, are PT-broken).
- **But the C operator is NEVER derived.** Every eigenspace of every GU-native core has exactly
  balanced Krein signature `(+m/2, -m/2)`: `comp(M_D)` gives `+/-0.3606` x 96 each `(+48,-48)`;
  the SU(2)+ Casimir is exactly scalar (maximally undetermined); the Weyl^2-shaped core gives three
  64-dim eigenspaces each `(+32,-32)`; mixed cores six 32-dim eigenspaces each `(+16,-16)`. The
  hyperbolic (generation, mirror) pairs survive inside every eigenspace. `C` exists (built and
  verified per core) but the choice of positive subspace per hyperbolic eigenspace is free --
  demonstrated concretely by a second, equally valid `C'` from a hyperbolic rotation. **The Mannheim
  move fails not at spectral reality but at spectral separation**; it relocates BIG-SWING-1's missing
  datum, it does not supply it.
- **THEOREM (achirality of every admissible C):** `{K, chi} = 0` (canon cross-chirality, exact) forces
  `Re tr(chi Pi_+) = 0` for EVERY `C` with `KC` Hermitian -- GU-native, imported, or otherwise. No
  PT/Krein quantization of this arena outputs a net-chiral physical sector in the Cl(14)-volume-trace
  sense, no matter what source action GU eventually builds. This is the C-07 wall speaking PT language,
  as a theorem rather than a scan. Both verifiers re-proved it independently; it is the strongest
  single result of the swing.
- Cross-check: PT-unbrokenness of `comp(M_D)` holds on the full 1664-dim gamma-traceless slice too
  (signature `(+832, -832, 0)`).

**Verifier notes folded in (none change the grade):**

- The chirality column of the readout table has **zero discriminating power** -- it is forced to zero
  for ANY input by the theorem (the doc says so; the script's docstring falsely promises otherwise and
  is stale -- cleanup item). The "0 of 6 with chiral sector" count is an arena identity, not a per-core
  finding.
- "Six cores" overstates independent evidence: core 2 = core 1 exactly, core 3 is scalar, and the
  mixed cores' structure follows from cores 1 and 4 commuting -- effectively **two independent reality
  measurements** plus forced combinations. The doc prints all the reduction facts itself. Also "both
  Casimirs" is a slight overcount (the so(9,5) Casimir was shown scalar, not run through the
  classifier).
- **PT-unbrokenness is canon-xi-specific** (PLAUSIBLE, verifier probe unfinished at deadline):
  `comp(M_D)^2 = 0.130000 I` matches `Q(xi) - 30` at the canon `xi`; if exact, spacelike `xi` with
  `Q(xi) < 30` would make `comp(M_D)^2` negative-scalar, i.e. PT-BROKEN -- which would *strengthen*
  the BLOCKED verdict (no `C` at all) -- and would relocate the Jordan locus away from the null cone
  (build doc's next-step 3 looks mislocated). Flagged for the xi scan.

---

## R4 -- conformal gauge inherits both walls; it cures neither

**Build grade: BLOCKED (bounded negative) + exact theorem-grade sub-results. Verifier verdicts:
SUSTAINED, PARTIAL.** Full reruns reproduce every number; one verifier re-derived all four fiber
signatures by a disjoint method plus closed form, and ran a scrambled-J control (random antisymmetric
unitary with `J^2 = -I` gives generator defect 8.04 vs 2e-12) proving the J-commutation measurement is
genuine; the other verified the pair-symmetry cancellation algebraically and on a different small
carrier.

**What stands:**

- **The fiber leg, exact over the rationals.** `gl(4,R)/o(3,1)` has invariant signature `(+7,-3)`
  (BIG-SWING-1's anchor re-derived, not copied); the conformal quotient removes EXACTLY the pure-trace
  scale direction `X = I` -- a **plus** direction, `B(I,I) = 4`, exactly orthogonal to the traceless
  part -- leaving `sl(4,R)/so(3,1)` at `(+6,-3)` with an invariant form **unique up to scale** on the
  conformal tangent (measured dim-1 nullspace, rep-theory-confirmed) and **still-noncompact O(3,1)
  isotropy** (exact boost family). Conformal gauge deletes the one direction that was never the
  problem. Compact control returns definite `(+10,0)/(+9,0)`: the machinery discriminates. Any future
  "definite conformal fiber metric" claim must break SO(3,1)-equivariance explicitly -- BIG-SWING-1's
  killed move, now provably unavoidable on the conformal fiber.
- **The C-07 leg.** On the verified carrier, a genuine Weyl-squared-shaped block (full 4D Weyl
  symmetries, measured Weyl-space dim 10) is `J_quat`-commuting (defect 1.5e-11); its triplet
  compression obeys Kramers pairing exactly -- multiplicities {64, 64, 64}, all even, **signature
  -64**. The only inside-the-quadratic-class escape from J-commutation (pair-antisymmetric imaginary
  coefficients) lands in the J-antilinear **signature-0** class; even the mixture stays even-paired.
  The foreign control (rank-3 projector) returns odd signature 3 with broken pairing -- the check is
  input-sensitive. A curvature-squared source action on GU's carrier cannot, at this kinematic level,
  produce an odd chiral count. Statement form: **"the conformal-class mechanism forces even/zero"**,
  never "GU forces c".

**Verifier downgrades (applied):**

1. **The complex-Weyl lemma is scope-limited.** The "complex Weyl coefficients cannot escape"
   cancellation is proven only for the **all-spacelike 4-base {0,1,2,3}** used (uniform
   anti-Hermiticity of the `Sigma`'s). On a Lorentzian 4-base the imaginary pair-symmetric part
   genuinely escapes J-commutation -- but it escapes **into the J-antilinear signature-0 class the
   script itself measures**, so the WALL conclusion (no odd count from curvature-squared blocks)
   survives; the lemma's universality framing does not, and is withdrawn here.
2. **Audit-sentence corrections.** "The number 3 appears exactly twice, both as measured outputs" is
   false in letter: the rank-3 of the foreign control is an inserted input (its odd signature is a
   consequence of that choice -- fine as a control, not a measurement), and the script divides by 24.0
   (the forced 4! antisymmetrizer normalization, not chi(K3)). Benign, but the route's forbidden-target
   audit sentence needed this correction.
3. **"The only invariant trace form is (+7,-3)"** is loose: the invariant-form space on `p` is
   2-dimensional and member signatures vary (none Riemannian -- the obstruction stands); uniqueness
   holds exactly where it is load-bearing, on `p_0`.
4. Minor: the E4 Kramers pairing is forced once E1/E2 hold (internal consistency, not independent
   content -- the doc says so); the E5(ii) lemma numbers are re-measurements of W2 itself, not a
   second confirmation; two carrier-arithmetic anchors (rank 128 / ker 1664) are near-tautological.

---

## The key scientific question, answered honestly

**Can the Bender-Mannheim PT/C mechanism supply what GU's ghost-parity frontier is missing?** No -- on
three independent legs, each bounded and machine-checked:

1. **It is not a second mechanism.** BM's `C` and TB's ghost parity are the same `Z2` wherever both
   exist (R1, theorem-grade in the toy at generic frequencies). The intake's implicit hope of an
   independent resolution collapses into the canon's existing open condition.
2. **Its distinguishing virtue -- derivedness -- fails exactly where GU needs it.** In the toy,
   derivedness fails at parity-mixing degeneracies (R1 verifier's resonance hole), and GU's target is a
   degenerate triplet. On GU's actual carrier the failure is total and sharper (R3): the spectra of all
   tested GU-native cores are real but perfectly sign-blind -- every eigenspace exactly K-balanced --
   so `C` is never derived, and definiteness would still have to be imported, which is BIG-SWING-1's
   refuted move.
3. **Even granting any admissible `C`, the physical sector is achiral** in the chi-trace readout
   (R3 theorem, from `{K, chi} = 0`), and the conformal-class action inherits the fiber obstruction and
   the C-07 even-count wall unchanged (R4).

What the swing *bought*: the canon's open condition is now sharpened into a precise, testable
dichotomy (below); the C-07 wall now has a PT-language theorem form; the conformal escape route is
closed with exact computations; and a new named failure mode (Jordan loci / parity-mixing degeneracies)
constrains every future source-action candidate.

---

## What this settles, and what it does not

**Settles (this swing).**

- The Bender-Mannheim and Turok-Bateman mechanisms are ONE mechanism; the Mannheim intake adds a
  derivation route, not an independent resolution (R1, with the resonance qualifier).
- The canon's open condition `[P_ghost, S] = 0` sharpens to a two-part property of `S` on the matter
  module: **(existence)** `S` Krein-diagonalizable with real spectrum (PT-unbroken, no Jordan blocks)
  -- forward direction a theorem, converse demonstrated in the toy; **(derivedness/uniqueness)**
  additionally, no degeneracy of `S` may mix ghost parity. GU's three-generation target sits in the
  degenerate regime, so the second part is not free.
- The Mannheim move (derive definiteness from spectra) is measurably unavailable on all tested
  GU-native cores: PT-unbroken but never K-separating (R3, sustained twice).
- THEOREM: no admissible `C` (any `C` with `KC` Hermitian) yields a net-chiral physical sector under
  the Cl(14)-volume-trace readout, because `{K, chi} = 0` (R3, independently re-derived twice).
- Conformal gauge inherits the fiber-metric obstruction ((+6,-3), rigid form, noncompact isotropy;
  exact) and the C-07 quaternionic-Kramers wall (even/zero signatures for the tested
  curvature-squared class) (R4, with the lemma scope qualifier).

**Does NOT settle.**

- **The generation-count verdict stays OPEN.** No route derived three, forbade three, or computed a
  chiral physical sector from GU-native data (`chiral_physical_sector_found = false` on all three).
  No forbidden target was imported in any load-bearing computation.
- R1 is quantum mechanics, not field theory: BM's full conformal-gravity claim, TB's quadratic-gravity
  Born rule at interacting-QFT level, and the PT-QFT critiques remain unadjudicated against primary
  sources (intake stress-test item still open).
- R3's balance finding is measured on a finite core list (effectively two independent reality
  measurements plus forced combinations); the chi-odd/mixed balance lemma is open; the chirality
  readout is the chi-trace only -- the `Spin(10)` `16/16bar` refinement inside the triplet is untested
  and is the canon hope's remaining trace-level readout. PT-unbrokenness is established at the canon
  `xi` only and may be xi-contingent (a flip would strengthen the negative).
- R4 tests the conformal-class *structure* on GU's fiber and carrier -- no conformal gravity on X4, no
  Bach dynamics, no S-matrix; the C-07 leg is `Cl(9,5) = M(64,H)`-specific (the `(7,7) = M(128,R)`
  alternative is unprobed); the Lorentzian-base version of the complex-Weyl lemma is open (escape lands
  in the signature-0 class either way).
- These are symbol/kinematic-level classifications; a genuine built source action could in principle
  supply a K-separating, parity-non-mixing perturbation. Nothing tested does.

---

## Where the wall now is

1. **Spectral separation, not spectral reality, is the missing datum.** GU's cores pass the
   PT-unbroken gate for free and then fail the only gate that matters: nothing GU-native splits a
   hyperbolic (generation, mirror) pair. The open lemma -- every K-self-adjoint element of GU's
   J-commuting native algebra, compressed to the triplet, has K-balanced eigenspaces (proved for
   chi-even cores, measured for the rest) -- would, if proved, upgrade R3 to a structural no-go:
   *the Mannheim move is unavailable on GU's carrier, period.*
2. **The achirality theorem fences every admissible C** at the chi-trace level. The only untested
   readout is the `16/16bar` refinement: if the refined grading also anticommutes with `K`, the
   theorem extends and the canon's "three physical chiral generations" reading loses its last
   trace-level readout; if not, that is the first crack worth attacking.
3. **Degeneracy is now a named enemy.** R1's Jordan/resonance loci mean any future source-action
   candidate must be checked for (a) no Jordan pairing of a generation with its mirror
   (positivity-unrescuable), and (b) no parity-mixing spectral degeneracy (derivedness-destroying) --
   and GU's triplet degeneracy makes (b) the default expectation, not the exception.
4. **The conformal escape is closed exactly.** The scale direction was a plus direction orthogonal to
   everything; the conformal tangent's invariant form is rigid; the isotropy stays noncompact; and the
   curvature-squared class stays inside the even/zero wall (with an observed-not-explained extra
   64-block doubling that can only strengthen it).

## Next steps

1. **Prove or refute the balanced-eigenspace lemma** for chi-odd/mixed K-self-adjoint elements of the
   J-commuting native algebra on the triplet (R3 next-step 1). This is the highest-leverage single
   item: it converts BLOCKED into a theorem-grade no-go for the whole derived-definiteness route.
2. **Build the `Spin(10)` `16/16bar`-graded readout** on the triplet and re-run the trace identity
   (R3 next-step 2). This is the one live positive direction the achirality theorem leaves open.
3. **Run the xi scan** for `comp(M_D)^2 = Q(xi) - sum_base(xi_a^2)` (verifier's conjecture): map the
   PT phase diagram in `xi`, locate the true Jordan locus, and determine whether PT-unbrokenness at the
   canon `xi` is generic or tuned.
4. **State and test the parity-non-mixing condition** for GU's forced degeneracies (R1's load-bearing
   qualifier): does the SU(2)+ triplet's equal-Casimir degeneracy mix ghost parity under any
   dynamics-shaped perturbation? A forced mixing would close the derivedness door from GU's own
   structure.
5. **Primary-source pass** on Bender-Mannheim 2008/2008b (incl. the equal-frequency Jordan-block
   unitarity claim, PRD 78, 025022, deliberately unadjudicated here) and the PT-QFT critiques, per the
   intake's promotion rule.
6. **Hygiene (non-blocking, from verifiers):** fix R3/R4 stale script docstrings (chirality-column
   claims, "trace moves" promise), print `||C' - C||` in the R3 non-uniqueness demo, correct the two
   "the number 3 does not appear" audit sentences, downgrade R1's convergence-rate wording to ~1.5
   decades per +4, add the simple-spectrum qualifier to R1's identity-domain sentences, and add the
   spacelike-base scope to R4's complex-Weyl lemma.

## Governance

Exploration-grade; **no canon promotion proposed from this synthesis.** Two candidate canon edits are
motivated but deferred to separate passes that pause for Joe: (a) rewriting the open condition
`[P_ghost, S] = 0` as the sharpened existence/derivedness dichotomy (with the parity-mixing
degeneracy caveat -- the R1 verifiers' qualifier is load-bearing and must travel with any promotion);
(b) recording the achirality theorem `Re tr(chi Pi_+) = 0` once the chi-odd balance lemma is settled.
The generation-count verdict is unchanged: **OPEN**. Any verdict/status flip pauses for Joe.
Verification tier: internal adversarial (two independent verifier agents per route, fresh re-runs,
partial independent re-derivations); not externally replicated or peer-reviewed.

---

## Verifier's note (main-loop review, 2026-07-06)

Synthesis of an 11-agent workflow (`wf_0db445cb-38b`; ~1.25M tokens, ~68 min). Main-loop review:

- **Independently re-run (holds):** `cg_r3_pt_phase_gu_cores.py` and `cg_r4_conformal_fiber_obstruction.py`
  were re-executed from disk in the main loop after the workflow closed — both exit 0 and reproduce their
  decisive tables to the digit (R3: six GU-native cores PT-UNBROKEN / C NON-CANONICAL / tr(chi Pi_+) =
  ±0.000, controls discriminate — the definitizable non-GU control returns DERIVED, randoms return
  PT-BROKEN; R4: (+7,-3) -> (+6,-3) exact, Weyl^2-shaped block J-commuting with Kramers-even signature
  -64, the foreign rank-3 projector control breaks pairing with odd signature 3). R1's numbers were not
  re-run in the main loop; both its verifiers re-ran it fresh and reproduced them with stronger
  convergence than claimed.
- **R2 (ghost-parity chirality wall on the true carrier) DID NOT RUN.** Its build agent died on a
  64k output-token cap (API error, no science produced); the pipeline dropped it, and this synthesis was
  written without it — no text above cites R2. The loss is materially covered: R2's central target (the
  trace obstruction for chirality under any admissible parity) is subsumed by existing canon
  (`canon/swing-ghost-parity-no-chiral-selection.md`) plus R3's STRONGER achirality theorem
  ({K,chi}=0 => Re tr(chi Pi_+)=0 for every admissible C). R2's unique unclaimed residue — the dimension
  of the J-commuting ghost-parity family and the commutant-size measurement of [P,S]=0 — remains open
  and can be re-run from the resumable workflow if wanted.
- **Federation gate-folding** (the 2026-07-06 tri-theory federation pre-registered R1/R3/R4 as gates;
  applying its own rules):
  1. **R1 CONDITIONALLY_SAME** resolves the federation's mirror-ontology fork in the merge direction:
     in the PT-unbroken regime Mannheim's and Bateman-Turok's rescues are ONE mechanism in two dresses —
     the federation's quantization seat has "two members plus a marketing layer" (its own pre-stated
     wording), and persona-pass-1's kill condition 3 (witness arithmetic merges toward one) FIRES. The
     R1 verifiers' resonance hole is load-bearing for GU: at spectral degeneracies C exists but is
     NON-UNIQUE, and the three-generation target is exactly a degenerate regime — so even where the
     mechanisms agree, derivedness does not transfer to GU's target.
  2. **R3 BLOCKED** fires the first half of federation kill condition 8 in a sharpened form: derived
     definiteness closes NOT because GU cores are PT-broken but because they are spectrally sign-blind
     (every eigenspace exactly K-balanced) — C always exists, is never canonical. BIG-SWING-1's
     imported-definiteness kill is now permanent at this altitude.
  3. **R4 BLOCKED** fires the second half: per the federation's pre-registered gate, the conformal leg
     demotes to rejection-level alignment (shared anti-Einstein diagnosis, no mechanism transfer);
     T1'/T10'/T4' are to be read as kinematic classification only, not as GU-native conformal attachment.
  4. **What survives of the tri-theory conjecture after the gates:** T2' (breaking-coset topology) and
     T3' (condensate ghost-parity compatibility) remain live at kinematic grade — but T3' now survives
     ONLY in the Bateman-Turok (kinematic-parity) reading, since the derived-C reading died in R3. The
     viability gauntlet (running at review time: V1-V6 + sources) executes both and must be read under
     these gates.
- **Canon edits proposed above (weakening the "plausibly met if quadratic-gravity-like" sentence;
  fencing the "three physical chiral generations" reading behind the new achirality theorem) PAUSE FOR
  JOE**, per governance; nothing has been edited in canon/.

**Bottom line (main-loop concurrence):** BLOCKED is the right grade and the sub-results are the real
harvest: the BM=TB identity theorem (toy scope, with the degeneracy hole), the achirality identity for
every admissible C, and the exact conformal-quotient signatures. The Mannheim offer — definiteness
derived from dynamics — is measurably unavailable on GU's carrier; the conformal action class inherits
every wall it was hoped to evade; and the count stays OPEN, now with one fewer escape route.
