---
artifact_type: exploration
status: exploration
created: 2026-07-11
hypothesis: H59
branch: "Path-2 wave-2, Target 3 (GU-independent theorem swing): no local positive metric for 4th-order QFT"
title: "No local positive-definite metric operator exists for the interacting 4th-order (Stelle / Pais-Uhlenbeck) QFT. PROVEN at strength (a): in the positive-energy (Bender-Mannheim / keep-and-grade) quantization, every positive metric that makes the keep-and-grade theory unitary has a NON-ENTIRE momentum-space symbol -- no finite-order differential operator (polynomial symbol) qualifies. The full positive-intertwiner family is characterized (eta = J*C, C = alpha*lambda + beta*lambda^3 with alpha,beta strictly-signed positive combinations of 1/sqrt(k^2+m_i^2) for ALL commutant weights); the commutant freedom cannot restore locality; the only entire grading is even-in-energy and yields an INDEFINITE eta (refutation trap closes). Two independent derivations (commutant+sign / Paley-Wiener analyticity) agree, locating the obstruction at k=+-i*m_ghost. The non-locality is exponentially localized (kernel ~ e^{-m|x-y|}), NOT long-range. Interacting case: first-order (Q1) non-locality persists -- STRONG-ARGUMENT, not all-orders."
grade: "exploration / free-case theorem PROVEN at strength (a) (symbolic commutant characterization + analyticity, machine-checked in tests/W54_path2_target3_no_local_metric.py, 13/13). Strength (b) [no metric from ANY local operator] ARGUED not proven. Interacting persistence: first-order STRONG-ARGUMENT, not all-orders. No loop amplitude computed. No canon / RESEARCH-STATUS / CANON / claim-status / verdict / posture changed. H59 remains OPEN."
depends_on:
  - explorations/path2-branchB-pt-c-operator-2026-07-11.md
  - explorations/path2-branchE-nogo-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W54_path2_target3_no_local_metric.py
---

# Path-2 Wave-2 Target 3 -- no local positive metric for the 4th-order QFT

**Role.** A directed GU-independent theorem swing. Branch B showed the *natural* metric `eta = e^{-Q}`
has a non-entire generator (`1/sqrt(k^2+m^2)`, branch points at `k = +-i m`). Branch E gave the R1
equivalence (positive grading iff Krein-diagonalizable real-spectrum) and the metric family's
uniqueness-up-to-commutant structure. My mandate: turn "the natural `eta` is non-local" into "**NO**
local `eta` exists" -- i.e. rule out every positive local metric, not just the canonical one. This is
the crux the two prior branches flagged as the single computation that would upgrade Q-caus FAIL from a
structural argument to a theorem.

This makes rigorous, at the 4th-order-gravity point, the standard folk-claim that PT / indefinite-metric
QFT trades **locality** for **positivity**. It is a real GU-independent contribution and it changes no
GU claim status.

---

## 1. Construction forks stated (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

Three load-bearing forks, named so the theorem's strength is unambiguous.

| Object | Construction I use | Why |
|---|---|---|
| **Ghost clearance** | GU-native **keep-and-grade** (Krein / PT indefinite metric), NOT positive-Hilbert removal / SUSY / Lee-Wick / fakeon | This is the program's object and the whole class's rescue; the theorem is a cost-of-that-rescue statement. |
| **The metric** | the **positive intertwiner** `eta` on the field Fock space: `eta > 0`, `eta H = H^dag eta` (H self-adjoint on `<.,.>_eta`). I characterize the FULL family, not one representative. | Branch E's point: the positivity-defining object, not the kinematic Krein form. |
| **"Local"** | `eta` is a translation-invariant multiplication operator in momentum space with matrix symbol `eta(k)`; **LOCAL(a)** := `eta(k)` **entire of finite exponential type** (Paley-Wiener: compact-support kernel), in particular **polynomial symbol = finite-order differential operator**. | Locality of a symbol = entirety (analytic continuation to all complex `k`). The airtight theorem is for polynomial/entire symbols; stronger senses are graded separately. |

**Which "Hamiltonian".** As in Branch B: the PT-Hermitian `H` with **real, bounded-below** spectrum
(Bender-Mannheim boundary conditions), which is pseudo-Hermitian -- not Dirac-Hermitian -- in the local
canonical fields. This is the quantization for which a nontrivial `eta` is genuinely required (see the
non-vacuity note below).

---

## 2. Why the theorem is non-vacuous (the honest crux)

The 4th-order field admits two quantizations:

- **Ostrogradsky / naive:** `eta = 1` (perfectly local), but the energy is **unbounded below** -- the
  ghost carries negative energy. Unitary, local, but no ground state.
- **Bender-Mannheim / keep-and-grade:** choose the contour so the spectrum is **real and bounded
  below** (positive energies). Then `H` is pseudo-Hermitian and a nontrivial positive `eta != 1` is
  forced.

**The theorem is that the second trade cannot also keep a local metric.** Precisely:

> **You may have (energy bounded below, positive norm) OR (local positive metric), but not both.**

If `eta = 1` were allowed to be the positive metric in the bounded-below quantization, there would be no
ghost problem at all; the content is that positivity + bounded-below-energy forces `eta` non-local. That
is the GU-independent, sharp form of the PT-QFT folk-claim.

---

## 3. The setup (free case), one mode at a time

The free 4th-order / PU field is quadratic, so `eta = Gamma(eta_1)` is the second quantization of a
one-particle metric `eta_1`, and everything reduces to the one-particle space per spatial momentum
`k`. Two mass shells: `m1` (healthy), `m2` (ghost), with dispersions `om_i(k) = sqrt(k^2 + m_i^2)`.

**The local data (fixed, entire).**
- The 4th-order dispersion polynomial `(E^2 - om1^2)(E^2 - om2^2) = E^4 - (om1^2 + om2^2) E^2 + om1^2
  om2^2`. Its coefficients `om1^2 + om2^2 = 2k^2 + m1^2 + m2^2` and `om1^2 om2^2 = (k^2+m1^2)(k^2+m2^2)`
  are **polynomials in k** -- the companion generator `A(k)` (eigenvalues `+-om1, +-om2`) is a
  polynomial (entire) matrix. This is the locality of the action.
- The **Krein one-particle signature** on the four states `(om1+, om1-, om2+, om2-)`:
  ```
  eps = (+1, -1, -1, +1).
  ```
  *Derivation:* the 4th-order propagator `1/[(k^2+m1^2)(k^2+m2^2)]` partial-fractions into two poles
  with **opposite residues** -- the two masses carry opposite Klein-Gordon norm sign (this IS the
  ghost). Within each mass, positive- and negative-frequency modes carry opposite KG sign. Hence
  `(+,-,-,+)`. **This is the load-bearing physical input** (Section 8).

**The requirement.** A positive metric `eta` must give every physical state positive norm; equivalently
the grading `C := eta^{-1} J` (with `J` the Krein form) must have eigenvalue `eps_i` on state `i`. So
`C` is an operator commuting with `H` whose eigenvalues realize the sign pattern `(+,-,-,+)` at energies
`lambda = (om1, -om1, om2, -om2)`.

---

## 4. Free-case theorem and proof -- Derivation D1 (commutant + sign)

### 4.1 The full positive-intertwiner family (the commutant characterization)

By the standard pseudo-Hermitian result (and Branch E's uniqueness-up-to-commutant), every Hermitian
intertwiner is `eta = sum_i d_i w_i w_i^dag` over the left-eigenvectors `w_i` of `H`, with `d_i` real;
positivity `<=>` `d_i > 0`. Equivalently `eta = J C` where the grading `C` commutes with `H` and, by
positivity, has eigenvalue-signs equal to the Krein signs: `sign C(om_i) = eps_i`. The commutant of `H`
(distinct real eigenvalues) is the diagonal algebra, so the free parameters are exactly the positive
weights `d1, d2 > 0` (particle/antiparticle equal by CPT/reality). **This is the entire family.**

### 4.2 Every member is non-entire

The sign data `(d1, -d1, -d2, d2)` at nodes `(om1, -om1, om2, -om2)` is **odd** under `lambda ->
-lambda`, so the unique degree`<=3` interpolant is purely odd:
```
C(lambda) = alpha * lambda + beta * lambda^3,
  alpha = [ d1 * om2^2 / om1 + d2 * om1^2 / om2 ] / (m2^2 - m1^2),
  beta  = -[ d1 / om1 + d2 / om2 ] / (m2^2 - m1^2).
```
(Both closed forms are verified symbolically -- test check **D1a**.) Now the crux:

> **`alpha` and `beta` are strictly-signed positive combinations of `1/om1` and `1/om2` for ALL
> `d1, d2 > 0`.** They can never vanish, and they always carry the branch cuts of `1/sqrt(k^2+m_i^2)`
> (branch points at `k = +-i m_i`). Therefore **no choice of positive commutant weights makes `C` -- and
> hence `eta = J C` -- entire.** (Test checks **D1b**, **D1c**: the symbol's series has finite radius of
> convergence `= m^2` in `k^2`.)

This is the commutant-freedom argument at full strength: it is not that the *natural* `eta` is non-local;
it is that **positivity forces the odd (sign-resolving) part `1/om_i`, and no positive weight cancels a
positive combination of `1/om1, 1/om2`.**

### 4.3 The refutation trap closes

The adversary's best attempt: the **even** entire grading `C_even(lambda) = g0 + g2 lambda^2` with
`g2 = -2/(m2^2-m1^2)` (const), `g0` polynomial in `k^2`. It IS entire and hits the shell values `+1` on
`om1`, `-1` on `om2` (test **D1'a**). But `C_even` is even in `lambda`: eigenvalues `(+1,+1,-1,-1)` on
`(om1+,om1-,om2+,om2-)`. Against `eps = (+,-,-,+)` the metric weights are `d_i = eps_i C_i =
(+1,-1,+1,-1)` -- **negative entries -> `eta = J C_even` is INDEFINITE, not a positive metric** (test
**D1'b**). The only entire grading cannot separate particle from antiparticle, which is exactly what
positivity of the Fock vacuum requires. **Entire => indefinite; positive => non-entire.** The trap
closes.

### 4.4 Global corollary (the physical mechanism)

The ghost demands the grading take **opposite signs on the two mass shells**. A polynomial symbol grows
co-monotonically on both shells at high `k` (they share leading asymptotics), so the sum dominates the
difference and the two signs must coincide at large `k`:
`|F1 + F2| / |F1 - F2| -> oo`. Opposite shell signs are therefore impossible for any polynomial symbol
-- **the sign flip is intrinsically carried by the non-entire `sqrt`.** (Test **D1''**: 4000 random
polynomial symbols, none holds opposite signs on `[0,400]`; **D1''b**: symbolic divergence of the ratio.)

---

## 5. Derivation D2 (analyticity / Paley-Wiener) -- independent second route

A local operator (finite-order differential, or compact-support kernel) has an **entire** symbol of
finite exponential type (Paley-Wiener). The metric symbol carries `sign(lambda) = lambda/om =
lambda/sqrt(k^2+m^2)`, whose branch point at `k = +-i m` gives a **finite radius of convergence `m`** --
not entire, hence not local (test **D2a**, reproducing Branch B Model D independently of any positivity
argument).

**Two-derivation agreement (program discipline).** D1 (positivity/sign route) and D2 (analyticity route)
are logically independent -- one uses the Krein sign pattern and the commutant, the other uses only the
symbol's analytic structure -- and they **land on the same obstruction at `k = +-i m_i`** (test
**AGREE**). This is the required cross-derivation; they agree.

**Strength (c) -- how bad is the non-locality?** The nearest branch point is at `k = +-i m` (off the
real axis), so the metric kernel decays like `e^{-m|x-y|}` (the 1D inverse transform is `K0(m|x-y|)`;
test **D2b** fits log-tail slope `-> -m`). The metric is **NON-LOCAL but EXPONENTIALLY LOCALIZED**
(analytic in a strip of width `m`), **NOT long-range / power-law.** Honest refinement: this is a
quasi-local, not a genuinely long-range, obstruction -- but it is provably not a finite-order
differential operator.

---

## 6. Interacting case (STRONG-ARGUMENT, first order)

Branch B: the first interacting correction solves `[H0, Q1] = -2 H1`, giving
`Q1(k) ~ H1(k) / (om + om' + ...)` -- **energy denominators** `1/(om(k1)+om(k2))`. Two facts:

1. These denominators have their **own** branch points at `k_i = +-i m_i` (test **INT1**); they add
   cuts, they do not cancel the free `1/om` cut (different analytic object -- higher-point convolution
   kernel vs one-particle symbol).
2. The free obstruction (opposite shell signs, Section 4.4) is an **`O(eps^0)`** fact. A first-order
   metric correction `eta = eta0 (1 + eps * ...)` cannot flip the leading-order sign structure of
   `eta0` (test **INT2**).

Therefore the non-locality **persists** at first interacting order. **Grade: STRONG-ARGUMENT
(perturbative, first order).** This is not an all-orders proof -- higher-order cancellations are not
excluded here (the honest open edge, Section 9).

---

## 7. The theorem, at its true strength

- **(a) PROVEN.** For the free 4th-order / PU field in the positive-energy (Bender-Mannheim /
  keep-and-grade) quantization, **there is no positive metric with a polynomial / entire (finite-order
  differential-operator) symbol.** The full positive-intertwiner family is `eta = J C`,
  `C = alpha lambda + beta lambda^3` with `alpha, beta` strictly-signed positive combinations of
  `1/om1, 1/om2` for all commutant weights `d1, d2 > 0`; every member is non-entire; the sole entire
  grading is even-in-energy and gives an indefinite `eta`.
- **(c) PROVEN (characterization).** The non-locality is a `k = +-i m_ghost` branch point: the kernel is
  **exponentially localized** (`~ e^{-m|x-y|}`, analytic in a strip), **not long-range.**
- **(b) STRONG-ARGUMENT, not proven.** "No positive metric generated by ANY local field operator"
  (beyond entire-symbol multiplication operators -- e.g. a genuinely `x`-dependent or non-translation-
  invariant local construction). Translation/Poincare invariance reduces `eta` to a symbol, which (a)
  handles; dropping that invariance is the gap.
- **INTERACTING: STRONG-ARGUMENT, first order.** Non-locality persists at `O(eps)`; all-orders open.

**Headline:** *any positive metric that makes the keep-and-grade 4th-order theory unitary is necessarily
non-local* -- proven for entire/polynomial symbols, i.e. for all finite-order differential operators.
This upgrades Branch B's Q-caus FAIL from a symbol-level structural argument to a **free-case theorem**.

---

## 8. The load-bearing assumption

Named per program discipline:

> **The ghost's Krein one-particle signature `eps = (+,-,-,+)` is fixed by the local action** (opposite
> propagator residues for the two masses + per-mode positive/negative-frequency sign) **and is not
> re-definable by any local field redefinition.**

If a purely kinematic *local* choice made the ghost's norm positive (i.e. re-signed `eps` locally), the
whole obstruction would dissolve. It does not, in the keep-and-grade construction: the opposite-residue
sign is a property of the 4th-order propagator itself. Everything else (the commutant characterization,
the odd-interpolant non-entirety, the analyticity route) is rigorous given this input. Secondary
assumption: "local" = entire / finite-exponential-type symbol (Paley-Wiener) -- the standard operational
definition; the theorem is exactly as strong as this definition (Section 1).

---

## 9. Self-critical pass (specialist / adversary / referee, inline)

**Specialist.** The theorem is a clean linear-algebra-plus-analyticity statement per mode, lifted to the
field by the quadratic (Gaussian) structure. The commutant characterization is complete; the
non-entirety holds for the whole family; two independent derivations agree.

**Adversary.**
1. *"Does the commutant contain a local positive element you missed?"* -- No. The commutant (distinct
   eigenvalues) is exactly `{d1, d2}`, and Section 4.2 shows `alpha, beta` carry `1/om_i` for every
   `d1, d2 > 0`. The only *entire* grading is the even one, which Section 4.3 shows is indefinite.
2. *"Is 'local' defined so the theorem is trivial or vacuous?"* -- No. Section 2 shows a local `eta = 1`
   DOES exist in the *unbounded-below* quantization; the theorem is the genuine incompatibility of
   locality with bounded-below-positive-norm. And "local = entire symbol" is the standard Paley-Wiener
   notion, not a strawman.
3. *"Could a non-translation-invariant local metric evade it?"* -- This is exactly the ungraded gap (b).
   Poincare invariance excludes it; without that symmetry I have not proven non-existence. Stated
   honestly.
4. *"Weierstrass: any continuous function is polynomial-approximable on a compact set."* -- Not the
   criterion used. The obstruction is (i) non-entirety (finite radius of convergence, a global analytic
   fact) and (ii) the large-`k` sign domination on the whole line -- neither is defeated by compact-set
   approximation (Branch B Model D discipline, inherited).

**Referee grades.**
- Free-case theorem strength (a): **PROVEN** (symbolic + analyticity, machine-checked, 13/13).
- Strength (c) characterization: **PROVEN.**
- Strength (b): **ARGUED** (reduction via Poincare invariance; non-invariant case open).
- Interacting persistence: **STRONG-ARGUMENT** (first order; all-orders open).
- Load-bearing assumption: the fixed ghost Krein sign `(+,-,-,+)`; falsifying it (a local re-signing)
  would overturn the theorem.

---

## 10. What this does NOT do

No GU/Stelle **loop** amplitude is computed. No all-orders interacting proof. No claim about
non-translation-invariant metrics. No `CANON.md` / `RESEARCH-STATUS.md` / claim-status / verdict /
posture change. H59 remains **OPEN**. The contribution is a free-case theorem plus a graded interacting
argument: *the keep-and-grade 4th-order theory buys unitarity at the necessary price of locality* --
rigorous for all finite-order differential-operator (polynomial/entire-symbol) metrics.

**Artifacts:** this file + `tests/W54_path2_target3_no_local_metric.py` (13/13 checks, exit 0). Not
committed. Exploration-grade.
