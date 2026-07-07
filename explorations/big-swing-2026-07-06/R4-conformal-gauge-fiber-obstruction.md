---
artifact_type: exploration
status: exploration
created: 2026-07-06
title: "Big swing R4 (Mannheim intake): does conformal gauge CURE or INHERIT the fiber-metric obstruction and the C-07 quaternionic wall? HONEST OUTCOME: INHERITS BOTH -- BLOCKED (bounded negative), with theorem-grade sub-results. (1) Re-derived from scratch, exact over the rationals: the metric fiber tangent gl(4,R)/o(3,1) has invariant signature (+7,-3) [BIG-SWING-1's anchor reproduced, not copied]; the conformal quotient removes EXACTLY the pure-trace scale direction X=I, a PLUS direction (B(I,I)=4, exactly B-orthogonal to the traceless part), leaving sl(4,R)/so(3,1) with EXACT signature (+6,-3); on the conformal tangent the invariant form is UNIQUE up to scale (measured nullspace dim 1), so indefiniteness is unavoidable; the isotropy O(3,1) of the conformal class remains noncompact (boosts preserve [eta] exactly, norm unbounded) -- only the scale R+ is quotiented away, and R+ was never the source of either obstruction. Compact control returns DEFINITE ((+10,0), (+9,0)), so the machinery discriminates. (2) On the verified 1792-dim Cl(9,5) carrier (anchors reproduced: rank(Gamma)=128, ker=1664, triplet Krein signature (+96,-96,0)), a Weyl-squared-shaped block C_abcd Sigma^ab Sigma^cd with genuine 4D Weyl-symmetric real coefficients is J_quat-commuting (defect 1.5e-11) and its 192-dim triplet compression obeys Kramers pairing exactly (max pair gap 4.8e-15; multiplicities 64/64/64, all even; signature -64, even). LEMMA found en route: COMPLEX Weyl coefficients cannot escape -- the Weyl tensor's pair symmetry cancels the hermitized imaginary part identically. Escaping J-commutation inside the quadratic-in-generators class (pair-antisymmetric imaginary block) buys only the J-antilinear ZERO class (signature 0), and even the mixture stays even-paired -- the wall on curvature-squared-type blocks is STRONGER than Kramers alone. Controls confirm discriminating power (a rank-3 projector in the triplet: odd signature 3, pairing gap 3.66e+02). No forbidden target imported; no chiral physical sector produced."
grade: "exploration / BLOCKED, bounded-negative. The conformal-gravity-CLASS structure, transplanted to GU's fiber and carrier, inherits the fiber-metric obstruction ((+6,-3), unique-up-to-scale invariant form, noncompact isotropy) and the C-07 quaternionic-Kramers wall (even spectra for every curvature-squared-type GU-native block, including all complex-Weyl-coefficient ones). The exact signature computations and the pair-symmetry cancellation lemma are machine-checked and exact (theorem-grade sub-results); the route as a cure for the walls is closed. Generation-count verdict unchanged: OPEN. No 3/8/24/chi(K3)/Ahat/rank_H/ind_H assumed, inserted, or divided by -- 3 appears only as the MEASURED odd signature of the foreign control."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - explorations/generation-sector/mannheim-conformal-gravity-source-action-intake-2026-07-06.md
  - explorations/big-swing-2026-07-03/BIG-SWING-1-source-action-definite-vertical-dirac-BLOCKED.md
  - tests/generation-sector/ghost_parity_krein.py
  - tests/generation-sector/step10_parity_gate_quaternionic_wall.py
  - tests/generation-sector/step11_gu_native_parity_theorem.py
scripts:
  - tests/big-swing/cg_r4_conformal_fiber_obstruction.py
---

# R4: conformal gauge does not cure the fiber-metric obstruction or the C-07 wall — it inherits both

**The swing.** The Mannheim intake (2026-07-06) put conformal (Weyl) gravity on the table as the
maximally symmetric member of the higher-derivative class that the ghost-parity synthesis names as
the plausible home for GU's unbuilt source action. Conformal gravity's structural signature is that
it has **no metric scale**: its natural fiber is the conformal class, i.e. GU's metric fiber
`GL(4,R)/O(3,1)` gets its trace direction quotiented away, becoming `GL(4,R)/(O(3,1) x R+)`.
BIG-SWING-1's one solid target-free result was an obstruction on the *metric* fiber: the only
invariant trace form is indefinite `(+7,-3)` with noncompact isotropy, so no invariant Riemannian
fiber metric exists. The R4 question: **does passing to the conformal class change that obstruction
— and does a Weyl-squared-shaped object on the GU carrier dodge the C-07 quaternionic-Kramers wall?**

**Honest outcome: it inherits both, and the second wall comes out *stronger* than expected.**
Everything below is printed by `tests/big-swing/cg_r4_conformal_fiber_obstruction.py` (runs to
exit 0 from the repo root in ~2.5 min; sections A–D are exact sympy rationals, section E is the
verified 1792-dim carrier with residuals printed).

---

## Anchors — reproduced first, from scratch

| anchor | required | reproduced |
|---|---|---|
| metric-fiber invariant signature (BIG-SWING-1) | `(+7,-3)` | **`(+7, -3, 0:0)`** — re-derived exactly (rational Lagrange congruence), NOT copied |
| `rank(Gamma)` / `dim ker(Gamma)` | 128 / 1664 | **128 / 1664** |
| self-dual triplet dim / Krein signature in (9,5) | 192 / `(+96,-96,0)` | **192 / `(+96, -96, 0:0)`** |
| `beta_S` pseudo-anti-Hermiticity residual | ~0 | **`0.0e+00`** |

Carrier construction copied verbatim from `tests/generation-sector/ghost_parity_krein.py`
(Jordan-Wigner Cl(9,5), gamma-trace projector, SU(2)+ triplet extraction, `K = eta_V (x) beta_S`).

## (A)–(B) The conformal quotient removes exactly one direction — the scale, a PLUS direction

Exact, over the rationals (sympy; no floats in the load-bearing numbers):

- **Metric fiber tangent** `p = gl(4,R)/o(3,1)` = eta-self-adjoint 4x4 matrices, dim 10,
  `eta = diag(-1,1,1,1)`, invariant form `B(X,Y) = tr(XY)`:
  **EXACT signature `(+7, -3, 0:0)`** (float cross-check eigenvalues `{-2 x3, +1 x4, +2 x3}`).
- **Conformal fiber tangent** `p_0 = sl(4,R)/so(3,1)` = traceless eta-self-adjoint matrices, dim 9:
  **EXACT signature `(+6, -3, 0:0)`**.
- **The removed direction is identified exactly**: it is the pure-trace direction `X = I` (the
  metric scale `g -> lambda g`), with `B(I,I) = 4 > 0` (a **plus** direction) and `B(I, p_0) = 0`
  exactly (all nine basis pairings print 0). So the conformal quotient removes **one + direction
  and nothing else**: `(+7,-3) -> (+6,-3)`. All three minus directions — the mixed
  time–space deformations, the actual source of indefiniteness — survive untouched.
- **The indefiniteness cannot be dodged by choosing a different invariant form.** The space of
  isotropy-invariant symmetric forms is *measured* (numerical nullspace of the invariance
  equations, singular-value gaps printed ~`3e+00` vs ~`1e-15`): dim **2** on `p`
  (span of `tr(XY)` and `trX trY`) but dim **1** on `p_0`. On the conformal tangent every invariant
  form is `c*B`: signature `(+6,-3)` or `(+3,-6)`, indefinite for every `c != 0`. The conformal
  fiber is in this respect *worse* than the metric fiber — the scale direction that a compensator
  could have played against is gone, and the remaining form is rigid.

## (C) Isotropy: still noncompact

The stabilizer of the conformal class `[eta]` in `GL(4,R)` is
`{g : g^T eta g = lam*eta, lam > 0} = CO(3,1) = O(3,1) x R+`. The quotient removes only the `R+`
factor. Verified exactly: the boost `B_t` in the 0–1 plane satisfies `B_t^T eta B_t - eta = 0`
identically in `t` (sympy, exactly zero matrix), while its entries `cosh(t)` grow through
`1.543, 74.2, 11013.2` at `t = 1, 5, 10` — an unbounded family *inside* the isotropy. Noncompact
isotropy — the second leg of BIG-SWING-1's obstruction — survives the conformal quotient entirely,
because `R+` was never its source; `O(3,1)` was.

## (D) Compact control — the machinery discriminates

The identical machinery on `eta = I`: `gl(4)/o(4)` gives **EXACT `(+10, -0, 0:0)`** and
`sl(4)/so(4)` gives **EXACT `(+9, -0, 0:0)`** — definite, as they must be. The invariant-form
counts are the same (2 and 1), so the *dimension* bookkeeping is structural while the *signature*
is what distinguishes `p - q = 4` from the compact case. The obstruction readout is a measurement,
not an artifact of the method.

## (E) The C-07 tie-in: Weyl-squared-shaped GU-native blocks cannot dodge the quaternionic wall

On the verified carrier (anchors above), with the antiunitary quaternionic structure
`J_quat = (I_14 (x) U) o conj` built by the step10/step11 averaging construction (transplanted to
this timelike set; `||U U* + I|| = 3.6e-12`, `||U U^dag - I|| = 1.7e-14`):

1. **All so(9,5) carrier generators are J-commuting**: max H-linearity defect `2.2e-12` over all
   91 spin generators (128-level), `6.9e-12` over full 1792-dim samples `Sigma_ab`, and `2.2e-12`
   for the constraint projector `Pi`. Hence any **real** polynomial in them is J-commuting.
2. **A genuine Weyl-squared-shaped block** `W2 = sum C_abcd Sigma^ab Sigma^cd + h.c.` was built
   with a random coefficient tensor carrying the **full 4D Weyl symmetries** (antisymmetry
   residuals `0.0e+00`, pair `0.0e+00`, first Bianchi `0.0e+00`, trace `1.1e-16`; the measured
   dimension of the 4D Weyl space is **10**, the classical value, so the projection is non-vacuous;
   `||W2|| = 110.02`). Its J-commutation defect: **`1.5e-11`**.
3. **Kramers on the triplet**: the triplet sector is J-invariant (residual `1.3e-12`;
   `J_trip` unitarity `5.3e-14`, `||J_trip^2 + I|| = 3.5e-12`), the compressed block commutes with
   `J_trip` (defect `7.0e-13`), and its spectrum obeys the Kramers pairing **exactly**: max pair
   gap `4.8e-15`; the full multiplicity structure is `{-6.530794 x64, -0.659944 x64, +7.190738 x64}`
   — all even; **signature `-64`, even**. No odd count.
4. **LEMMA (found when a planned control failed *for a reason*)**: complexifying the Weyl
   coefficients does **not** break J-commutation. Hermitization turns the imaginary part into
   `(i/2) sum W_abcd [Sigma^ab, Sigma^cd]`, and the commutator is **antisymmetric under pair
   exchange while the Weyl tensor is symmetric** — the imaginary part cancels identically
   (measured J-defect of the hermitized complex-Weyl block: `1.5e-11`; pairing gap `6.99e-15`).
   So the wall covers the **entire complex-Weyl-coefficient class**, not just real couplings.
5. **Escaping J-commutation inside the quadratic class buys nothing odd.** The Hermitian block
   that genuinely leaves the J-commutant — pair-ANTIsymmetric imaginary coefficients, i.e.
   `i x (real element of so(9,5))` (Hermiticity residual `2.2e-15`, J-defect `100.64`) — lands in
   the step10 **J-antilinear zero class**: measured signature **0**. Measured surprise: its
   pairing gap is still `4.66e-15`, and even the mixture (J-commuting + J-anticommuting parts)
   stays even-paired (gap `1.24e-14`, signature 0). Within the quadratic-in-generators class,
   every tested member has even multiplicities — **the wall on curvature-squared-type blocks is
   stronger than Kramers alone**; the extra doubling is measured, not yet explained.
6. **The pairing check has discriminating power** (it is not a tautology of the triplet): a random
   rank-3 projector inside the 192-dim triplet has J-defect `1001.95` (foreign), **odd measured
   signature `3`**, and breaks the pairing with gap `3.66e+02`. The check returns the opposite
   verdict on foreign input.

## Defect-candidate audit (the failure modes that killed claims last swing)

- **Constants copied from canon?** No. The `(+7,-3)` anchor is *re-derived* by an independent
  exact method (rational Lagrange congruence) and only then compared; `(+96,-96,0)`, 128, 1664 are
  reproduced by running the copied construction, and every downstream number is computed fresh.
- **Tautological closure / zero discriminating power?** No. Three controls: the compact fiber
  returns DEFINITE (D); the rank-3 foreign carrier returns ODD signature and a broken pairing
  (E5-i); the invariant-form count is measured against printed singular-value gaps. Where a planned
  control *failed to discriminate* (complex Weyl coefficients), the failure was diagnosed to an
  exact cancellation mechanism and honestly re-reported as a lemma strengthening the wall — the
  discriminating role was reassigned to controls that actually discriminate.
- **Forbidden-target import?** None. `{3, 8, 24, chi(K3), Ahat, rank_H, ind_H}` never assumed,
  inserted, or divided by. The number 3 appears exactly twice, both as **measured outputs**: the
  `-3` block of the exact fiber signature, and the odd signature `3` of the foreign control.
- **Scripts persisted?** Yes: one script, `tests/big-swing/cg_r4_conformal_fiber_obstruction.py`,
  runs to exit 0 from the repo root and prints every number cited above.

## What this settles

- **The Mannheim-shaped escape from the fiber-metric obstruction is closed.** The attraction of
  conformal gravity for this program was the thought that removing the metric scale might remove
  what obstructed BIG-SWING-1's fiber Dirac construction. Computed: the scale is a *plus* direction,
  exactly orthogonal to everything else; removing it leaves `(+6,-3)` with a now *unique* invariant
  form and the same noncompact `O(3,1)` isotropy. Conformal gauge deletes the one direction that
  was never the problem.
- **The conformal-gravity-CLASS action inherits the C-07 wall unchanged — and hardened.** Any
  Weyl-squared-type block built from GU-native so(9,5) data is J-commuting for *all* complex Weyl
  coefficients (the pair-symmetry lemma), and its triplet spectra are even-multiplicity. A
  "curvature-squared source action on GU's carrier" cannot, at this kinematic level, produce an odd
  chiral count; the only inside-the-class escape (J-antilinear) is the signature-0 class.
- Statement form, per house rules: **"the conformal-class mechanism forces even/zero"** — a
  property of the mechanism on GU's fiber and carrier, never "GU forces c".

## What this does NOT settle (honest boundary)

- **Scope.** This tests the conformal CLASS structure *transplanted to GU's fiber and carrier*: the
  tangent-space geometry of the conformal quotient, and Weyl-squared-shaped algebra on the verified
  Cl(9,5) module. It does **not** build conformal gravity on `X4`, does not construct Bach-equation
  dynamics or an S-matrix, and does not test Mannheim's PT-quantization mechanism or his
  phenomenology (rotation curves, lensing disputes). The canon's open condition `[P_ghost, S] = 0`
  remains untestable for the same reason as before: there is no `S`.
- **Signature scope of the C-07 leg.** The quaternionic wall is a `Cl(9,5) = M(64,H)` fact; the
  `(7,7) = M(128,R)` alternative has no `J_quat` of this type and is not probed here (the exact
  fiber results in A–D, by contrast, are signature-generic in `p - q = 4`).
- **The extra doubling.** The measured even-pairing of the J-*anti*linear quadratic block (and the
  mixture) exceeds what Kramers guarantees; the responsible structure (plausibly the
  `2 (SU(2)-) x 16/16bar` factorization of the 192-dim triplet — note all multiplicities came out
  64 = 192/3) is observed, not proven. Worth a short follow-up; it can only strengthen the wall.
- **The Weyl coefficients were built with the Euclidean metric on the base `{0,1,2,3}`** (all
  spacelike in the (9,5) assignment used). The J-commutation conclusion is coefficient-independent
  for real tensors, so it covers eta-based Weyl projections too; the printed Weyl-space dim 10 is
  for the Euclidean case.
- **Nothing here derives or forbids three generations.** The count verdict stays OPEN. No chiral
  physical sector was produced — the opposite: another natural class of candidate source actions is
  shown unable to produce one from GU-native data alone.

## Next steps

1. **Explain the extra doubling** on the quadratic-in-so(9,5) class (candidate: the compressed
   quadratic algebra acts as `(3x3) (x) I_64` on the triplet isotypic decomposition — the 64s in
   the printed multiplicities). If proven, it upgrades the C-07 wall on curvature-squared blocks
   from Kramers-even to "spectra constant on 64-dim blocks", an even sharper no-go.
2. **The PT-vs-ghost-parity comparison** (intake follow-up #1) is still the live positive
   direction: this swing closed the "conformal gauge cures the walls" branch, not the
   "PT/ghost-parity dynamics realizes `[P_ghost, S] = 0`" branch — that one still has no
   computable object and remains the program's named frontier.
3. **If anyone re-attacks the fiber:** the measured uniqueness (dim-1 invariant-form space on the
   conformal tangent) means any future "definite conformal fiber metric" claim must break
   `SO(3,1)`-equivariance explicitly — the same compensator import that killed BIG-SWING-1's
   attempt 1. That defect is now provably unavoidable on the conformal fiber, not just unavoided.

**Governance.** Exploration-grade; no canon promotion proposed. The generation-count verdict
remains OPEN; this is a bounded negative about a candidate source-action class, which is exactly
the kind of result the research posture counts as a win.
