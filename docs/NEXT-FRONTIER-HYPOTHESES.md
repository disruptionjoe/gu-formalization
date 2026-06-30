# Next-frontier hypotheses (keeping this repo alive)

Status: live research directions, 2026-06-28. These supersede "draft the paper and close the repo" as the
near-term frontier. The persona sprint (`explorations/persona-and-dialectic/higher-order-story-persona-sprint-2026-06-28.md`)
established that the highest-leverage continuation is **repo-resident**: one unbuilt object gates dark
energy, the middle map, and the matter count at once, and the transcript names its mathematical template.

Each hypothesis is falsifiable and carries a concrete first computation. Grades:
`load-bearing-verifiable | structural-plausible | seductive-unverified`. Posture is unchanged: optimize for
truth, keep what survives (often GU-independent), attack don't defend.

---

## H1 (keystone) -- Build the Seiberg-Witten-shaped source action on the chimeric bundle

**Hypothesis.** The fermionic "source action" the program named as its universal blocker (author-disclaimed
draft eq 10.10, "Caveat Emptor") has a known mathematical template, stated in the transcript's first 90
seconds: the bottom equation "became sufficiently nonlinear in 1994 when Ed Witten and Nattie Seiberg did
it." That is the Seiberg-Witten / monopole nonlinearity: a coupling of self-dual curvature to a spinor
bilinear, plus a Dirac term, on objects GU already has (`Lambda^2_+`, the spinor bundle, the `d^2` middle
map).

**Why it is the keystone.** One written action plausibly discharges three open lanes at once:
- (a) identifies `theta` as the gauge-potential sector of the Euler-Lagrange derivative `E_A`, discharging
  dark-energy **Assumption 3** (`canon/dark-energy-theta-divergence-free.md`);
- (b) closes the **middle map** (the `d^2` non-closure the repo has measured qualitatively);
- (c) generates the **2+1 matter content** (H2 below), making the asserted `+8` Rarita-Schwinger term in
  `ind_H = 8*A-hat + 8` an actual computation rather than an assertion.

**First computation.** Write the monopole-type coupling explicitly on the chimeric bundle:
self-dual `Lambda^2_+` curvature set equal to the spinor bilinear `sigma(psi)`, plus the Dirac term. Check
the variational structure: do the Euler-Lagrange equations identify `theta` with the gauge-potential sector
of `E_A`? Is the resulting RS operator Fredholm? This is construction, not litigation.

**Honest risk.** Building it could equally reveal the count is observer-relative or not a clean integer
(GU's own materials oscillate between "two generations" and "2+1"), dissolving the headline rather than
confirming 3. That is an acceptable outcome under the truth-seeking posture.

**Grade:** load-bearing-verifiable (the gap and its named template are both textually anchored; the
construction is the open work). The single highest-leverage open item in the program.

**STATUS 2026-06-28 -- BUILT AND MEASURED (see `canon/source-action-seiberg-witten-RESULTS.md`).** The
doubled full-`Lambda^2` SW action was constructed on the `Cl(9,5)` substrate and verified numerically. The
moment map `mu` exists (Krein-real, equivariant, unique) and dark energy (A) discharges **conditionally**.
But running code **refuted all three jobs it was built for**: the SW shell makes the gamma-trace obstruction
1.44x WORSE (B1), does not collapse the selector (B2), produces only a VECTORLIKE `2+1` mass split with the
chiral `+8` not computed (C), and is provably orthogonal to the `-5376` index (sign). Deepest result: **a
Krein-isometric source action is structurally orthogonal to the chiral generation count** -- the count needs
a symmetry-breaking import or a re-reading as a vectorlike mass multiplicity. BV `(S,S)=0` and Velo-Zwanziger
stay open. Net: H1 is no longer "unbuilt" -- it is "built, exists, conditionally discharges dark energy,
performs none of the chiral/index jobs," which hardens the standing no-go rather than relieving it. The
keystone moved from open-construction to a sharpened, named open frontier (the 6 next computations in the
RESULTS doc).

---

## H2 -- Re-specify the count as "2 + 1 by two bundle origins," not "an index = 3"

**Hypothesis.** Weinstein's mechanism is 2 genuine families from pulling back Weyl spinors (the base
complex) plus 1 "imposter" from the Rarita-Schwinger product-rule term on the 10-dim normal bundle. Two
different bundle origins means **no single Atiyah-Singer index, Adams e-invariant, or bordism class can ever
yield "2+1-with-an-imposter."** The campaign's central NOT-ESTABLISHED verdict litigated a target the theory
never claimed.

**What this changes.** Promote `canon/two-primary-lemma.md` to the airtight GU-independent core: it proves
every obstruction in the no-go is 2-primary, hence structurally blind to an odd count -- the homotopy-side
shadow of the 2+1 two-origin structure. Mark every "count = 3" claim as **asserted-pending-source-action**
(it rests on the unbuilt `+8` term from H1), not computed.

**First action.** Edit the count-bearing canon to state the 2+1 two-origin structure, label the `+8` RS term
conditional on H1, and demote the Adams e-invariant boundary computation to "what you would compute IF the
complex closed."

**Grade:** load-bearing-verifiable.

---

## H3 -- IG equivariance forces divergence-free dark energy (the GU-independent headline theorem)

**Hypothesis.** The inhomogeneous gauge group `IG = G semidirect Omega^1(ad P)` is the stated deliverable
("the unified field sought by Einstein," "wildly understudied"). Its load-bearing mechanism is purely
classical-structural: `d_A(g)g^-1` is connection-independent, so a difference of two connections is
adjoint-tensorial, and equivariance forces the divergence-free property -- from which a dynamical `theta`
(replacing `Lambda*g`) flows and the cosmological-constant fine-tuning dissolves, with no 120-orders
problem because it is a field, not a constant.

**First computation.** Write the variational principle that identifies `theta` as the gauge-potential sector
of `E_A` and prove the remaining structural step `equivariance => D_A* theta = 0`. This is the SAME write as
H1 (the source action lives on the same IG), so one action discharges both lanes.

**Why it matters.** This is a citable, reconstruction-independent theorem the program currently lacks. It
survives a referee who rejects GU outright. Pair with H1.

**Grade:** load-bearing-verifiable (mechanism is anchored and largely GU-independent; the theorem step is
unwritten).

---

## H4 -- Indefinite signature is the real setting; GUT deflates to a normal bundle

**Hypothesis (two layers).**
- (a) The physically correct setting has an **indefinite Killing form**; the compact Standard Model is the
  maximal compact subgroup of an indefinite real form (`SU(3)xSU(2)xU(1) = max compact of SU(3,2)`;
  Pati-Salam `= max compact of Spin(6,4)`). GU's trace-reversed `(6,4)+(3,1) = (9,5)/(7,7)` signature **IS**
  our machine-checked `Cl(9,5) = M(64,H)` Krein build. Our ghost-parity / Krein canon already self-corrected
  (A0 audit) to exactly this reading: dropping Hilbert positivity = negating Distler-Garibaldi's
  compact-internal-G assumption (DG-A3), a scope-exit.
- (b) **The deflation of grand unification.** `14 = 4 + 10`, so SO(10)'s "10" is literally the dimension of
  the normal bundle of `X^4` in `Met(X)`: "there is no grand unification, it's just a normal bundle." The
  spinor-in-ambient = spinor-on-X tensor spinor-on-normal-bundle exponential rule supplies the 16.

**First checks.** Verify `SU(3)xSU(2)xU(1) = max compact of SU(3,2)` directly (only the Spin(6,4) chain is
in-repo). State the normal-bundle deflation as a standalone checkable claim. Attach a **unitarity ledger**:
indefinite signature is necessary-not-sufficient (net chirality 0 survives into (9,5)/(7,7), so flipping
signature injects no kinematic 3), and the Velo-Zwanziger cost (tachyons / unitarity loss for gauge-coupled
spin-3/2) applies.

**Action.** Promote `canon/ghost-parity-krein-synthesis.md` from "generation-evasion axis 7" to a standalone
headline result, cite the transcript as the primary anchor, and add the normal-bundle deflation.

**Grade:** load-bearing-verifiable (cross-validated against an independent in-repo computation), with the
"the 3 hides in the non-compact directions" overhang held at seductive-unverified until computed.

---

## H5 -- The Higgs is the norm-square of the unified curvature

**Hypothesis.** "There's no Higgs. The Higgs is an illusion." The Higgs potential is `||F||^2` of the
unified connection: the `a-wedge-a` term gives the quartic, the unperturbed-curvature cross term gives the
quadratic, and a negative curvature produces the Mexican hat; "minimal coupling and Yukawa coupling are the
same thing, the only thing different is the spin."

**First computation.** Expand `||F||^2` for the GU connection on the chimeric bundle and test whether the
`a-wedge-a` quartic plus the cross-term quadratic with negative curvature reproduce `V(phi)`. Promote
`explorations/geometry-curvature-emergence/pc5-higgs-emergence-spec-2026-06-23.md` to a verified canon check, or kill it.

**Why it matters.** It reframes the "field content" the campaign kept auditing as derived geometry, not
postulated scalars. Independent of H1; runs in parallel.

**Grade:** load-bearing-verifiable (directly checkable Lagrangian claim).

---

## H6 -- "Square and square root" = Dirac^2 = Lichnerowicz, NOT BCJ double copy

**Hypothesis.** GU's "first-order theory squares to a second-order theory ... think double copy" is the
operator factorization `Dirac^2 = Lichnerowicz` (Weitzenbock/Bochner, the SUSY square-root of a Hamiltonian),
already partially verified in-repo (`M_KT = N * D_Sigma^2`). It is **not** the BCJ double copy (gravity =
gauge squared via color-kinematics), which GU cannot be: it has no amplitudes, asymptotic states, or
color-kinematics duality.

**First action.** Finish the `M_KT = N*D_Sigma^2` verification; state precisely in any paper that the
"square" is the operator square, to pre-empt a referee mistaking the slogan for BCJ. Optionally probe the one
real bridge: the self-dual `Lambda^2_+` sector is the only locus where a GU "double copy" could be an exact
theorem (self-dual YM double-copies to self-dual gravity).

**Grade:** load-bearing-verifiable (the operator-square reading), with the amplitudes bridge at
seductive-unverified.

---

## Canon hygiene (do alongside, not as frontiers)

- **The 343.73 "d^2 gate" was already killed in-repo.** Ensure canon reads "qualitative non-closure plus a
  provably non-unique (>= 8-real-dim) selector," NOT "the measured 343.73 obstruction." The live gate is the
  selector freedom.
- **DESI w(z).** Verify the self-documented hardcoded-3 in `tests/theta_flrw_desi_sign.py`, and correct
  `canon/theta-field-flrw-dark-energy-eos.md` from "sign-inconsistent with DESI" to "method-dependent / not
  robust (range-fit agrees in sign; magnitude ~3x off; f_0 is a fit)." Do NOT elevate w(z) to a frontier --
  chasing the one DESI-legible scalar is the streetlight bias one level down.

## What stays parked (seductive-unverified)

Coadjoint-orbit / Wigner-dual of IG; Takesaki conditional-expectation selector; the numerologies
(Mexican-standoff = 2-primary tower, square-root = Born rule, "axis of evil" CMB axis, "the 3 hides in the
non-compact directions"). Each is a one-sentence aside with no existence-and-magnitude computation. Keep the
observer-relative open-bridge reframe (the count may be section-dependent by construction) as a flagged
falsifiable hypothesis, not a result.

---

## Sequence

1. **H1 + H3 together** (one source action, two discharges) -- the keystone build.
2. **H5 and H6** in parallel (independent, cheap, GU-checkable).
3. **H4** promotion + the two direct verifications (max-compact-of-SU(3,2); normal-bundle deflation).
4. **H2** re-specification + canon hygiene (low effort, high honesty value).

Pointers: the campaign verdict is `canon/final-verdict-generation-count-and-the-open-bridge.md`; the sprint
synthesis is `explorations/persona-and-dialectic/higher-order-story-persona-sprint-2026-06-28.md`; the public-review/publishing
decisions live in CapacityOS `WRK-542`; the spinout (separate-repo) directions live in CapacityOS
`WORK-000-reputation-gu-spinout-research-directions`.
