---
title: "Six-Axis Candidate: GU Section-Selection with BvN L1-L2 Coupling Rule (fr2-bvn-layer5)"
date: 2026-06-23
problem_label: "six-axis-l1l2-coupling-example"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Six-Axis Candidate: GU Section-Selection with BvN L1-L2 Coupling Rule

**Purpose.** This document fills one complete six-axis candidate specification row for the GU
section-selection protocol where the L1-L2 coupling rule

```
Gamma >= Gamma_min = ln(1/epsilon) / t_obs
```

is the load-bearing constraint. It discharges the final promotion gate for the
`fr2-bvn-layer5` coupling-rule candidacy: the promotion condition required one filled
six-axis example with this as the load-bearing L1-L2 constraint.

---

## Acceptance Summary (One-Line Table)

| candidate | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 coordination loop | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GU-section-BvN-coupling | Smooth principal bundle on Y^14 = Met(X^4), Cl(9,5) spinor module S = H^64, quantum metric fluctuations active | Snowball / metastable consensus observer — finite, subsampling, epsilon-bounded; decoherence rate Gamma; finalization latency t_obs | Metastable-consensus pairing — Gamma_min = ln(1/epsilon)/t_obs bounds lambda_max; BvN wall prevents classical-shadow extraction below Gamma_min | Total-order Lorentzian on X^4; quantum metric fluctuations on fibers of Y^14 not smoothly ordered below decoherence threshold | Specific-object substrate (Y^14 with gimmel metric, Tikhonov-selected section s*) | Stochastic gradient / RG flow — Tikhonov-Willmore energy E[s] + Lambda ||s - s_ref||^2 drives section selection; Lambda = 8 epsilon^2 / t_obs^2 couples decoherence tolerance to section energy | If the GU Tikhonov section selection can be formulated and evaluated without any classicality requirement on the metric (purely quantum metric input, no pointer-basis certification required), the coupling rule is not load-bearing and the candidate collapses; test by constructing a purely quantum-mechanical formulation of the Willmore minimization on a quantum superposition of metrics and checking whether the output remains well-defined. |

---

## Leg 1 — Substrate Class

**Class label:** (a) Smooth principal bundle on a smooth manifold — specifically Y^14 = Met(X^4)
with the gimmel metric of signature (9,5) — but with the non-standard modification that the
fiber coordinates (metric components g_{mu nu}(x)) are treated as quantum-fluctuating fields
subject to Lindblad/pointer-basis decoherence above the decoherence threshold Gamma_min.

**Specification (1-3 sentences):** The substrate is Y^14 = Met(X^4): the bundle of Lorentzian
metrics on the 4-manifold X^4, equipped with the gimmel metric (Frobenius + trace-reversal,
signature (9,5)) and the Clifford spinor module S = H^64 (from Cl(9,5) ~= M(64,H)). The
fiber GL(4,R)/O(3,1) ~= RP^3 carries quantum metric fluctuations: the section
s: X^4 -> Y^14 is not fixed but is selected by Tikhonov-Willmore minimization
s* = argmin_{s} [E[s] + Lambda ||s - s_ref||^2] with Lambda = 8 epsilon^2 / t_obs^2
(established in `explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md`). The substrate includes
the quantum coherence dynamics of the metric field: below the decoherence threshold Gamma_min,
the fiber coordinates are in a quantum superposition with no definite classical shadow.

**Literature anchor:** Weinstein GU construction (transcript 2025-04; primary source
`literature/weinstein-ucsd-2025-04-transcript.md`); gimmel metric derivation
(`explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md`); Tikhonov
section selection (`explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`); Lindblad/pointer-basis
decoherence model (`explorations/time-as-finality-crosswalk/observer-section-error-model-2026-06-23.md`).

**Class-assumption signature broken:** Witten 1981 and Distler-Garibaldi assume a fixed,
classical, smooth bundle. This candidate adds the non-smooth modification that the fiber
coordinates carry quantum fluctuations until the observer's decoherence rate is sufficiently
fast. The smooth bundle structure is the CLASSICAL SHADOW of the quantum metric substrate;
the shadow is well-defined only above Gamma_min. Below Gamma_min, the substrate does not
present a classical smooth section to the observer, and GU's field equations (D_A*theta = 0,
the Tikhonov-Willmore minimization) are ill-posed. The no-go theorems do not see this
level; they act on the classical shadow, which is the forgetful image of the substrate under
the L3 pairing when Gamma >= Gamma_min.

---

## Leg 2 — Observer Class

**Class label:** (d) Snowball / metastable consensus observer — finite, subsampling,
epsilon-bounded, with explicit decoherence rate Gamma and finalization latency t_obs.

**Specification:** The observer is a finite-resource measuring apparatus that extracts a
classical shadow of the metric substrate via a pointer-basis measurement. The observer's
classicality-certification rate is Gamma (the rate at which the Lindblad channel drives
metric density matrices to pointer-basis eigenstates). The observer's record-finalization
latency is t_obs (the time over which a single metric readout is completed). The
decoherence tolerance is epsilon (the maximum off-diagonal density matrix element allowed
at the time of record finalization). The observer can certify a classical metric shadow
only when Gamma >= Gamma_min = ln(1/epsilon)/t_obs; below this threshold, the observer's
accessible event algebra is non-distributive (BvN wall, formalized in
`explorations/misc/fr2-bvn-layer5-promotion-gate-2026-06-23.md`) and no definite classical
section is available.

**Literature anchor:** BvN gate (i) proof at `explorations/misc/fr2-bvn-layer5-promotion-gate-2026-06-23.md`;
Lindblad/pointer-basis model at `explorations/time-as-finality-crosswalk/observer-section-error-model-2026-06-23.md`;
FR2 Gamma_min derivation at `explorations/time-as-finality-crosswalk/fr2-bvn-rate-of-classicality-derivation-2026-06-22.md`;
Lindblad (1976) (open quantum systems, standard reference); Zurek (2003) (pointer basis,
einselection).

**Class-assumption signature broken:** The no-go theorems implicitly assume an unlimited-fidelity
observer (class (a), finite Turing with BPP/BQP access to a fixed, already-classical substrate).
This candidate drops the already-classical assumption: the observer must perform classicality
certification as an active step, and the certification rate bounds the record-finalization rate.
The BvN wall is the structural reason the certification is a non-trivial step.

---

## Leg 3 — Pairing

**Class label:** (f) Metastable-consensus pairing, parameters (k, alpha, beta, CAP-corner) with
the additional quantitative coupling rule Gamma_min = ln(1/epsilon)/t_obs that bounds
lambda_max <= Gamma_min.

**Specification:** The observer pairs with the substrate by extracting a classical shadow of
the metric fiber coordinates via a Lindblad decoherence channel with rate Gamma. The pairing
produces a definite classical section s: X^4 -> Y^14 only when Gamma >= Gamma_min. The coupling
rule Gamma_min = ln(1/epsilon)/t_obs is the load-bearing constraint: it is derived from the
requirement that the off-diagonal density matrix elements decay to below epsilon in the time
window t_obs. The BvN wall (denied functor I: CAlg -> OMLat has no left adjoint natural
w.r.t. unitary action for dim H >= 2) is the structural source of the coupling inequality;
the inequality is the rate-parameterized form of the wall crossing. Below Gamma_min, the
pairing channel outputs a quantum mixture over metric configurations, not a classical section,
and the GU section-selection Tikhonov minimization is ill-posed (its minimizer is not a
definite point in Gamma(pi) but a density over sections).

**Literature anchor:** BvN theorem (Birkhoff and von Neumann 1936); denied-functor formalization
at `explorations/misc/fr2-bvn-layer5-promotion-gate-2026-06-23.md`; fr2-gate-ii GU result at
`explorations/misc/fr2-bvn-gate-ii-gu-result-2026-06-23.md`; Lindblad decoherence model at
`explorations/time-as-finality-crosswalk/observer-section-error-model-2026-06-23.md`.

**Class-assumption signature broken:** Witten 1981, Freed-Hopkins, Distler-Garibaldi, and
Nielsen-Ninomiya all assume the pairing is cartesian/smooth (class (a)): substrate is classical,
observer reads off invariants without a classicality-certification step. This candidate inserts
the BvN-gated classicality certification into the pairing. The coupling rule Gamma >= Gamma_min
is the admission criterion for the classical smooth pairing to be valid; below Gamma_min, the
pairing is genuinely non-classical and the no-go theorems' calculations at the classical level
are inapplicable (they would need to be re-done over the quantum mixture, which is a different
calculation).

---

## Leg 4 — Causal-Order Class

**Class label:** (a) Total-order Lorentzian (smooth manifold, Cauchy slicing) on the base X^4;
non-classical fiber ordering below Gamma_min on the fibers of Y^14.

**Specification:** The causal order on the base X^4 is the standard smooth Lorentzian order
(class (a)). The GU construction inherits this from X^4: the section s: X^4 -> Y^14 is
evaluated in Lorentzian time, and D_A*theta = 0 is a classical field equation on X^4. The
modification is on the fiber side: the fiber GL(4,R)/O(3,1) ~= RP^3 carries a quantum metric
fluctuation that is temporally ordered in the Lindblad sense (decoherence is a time-directed
process with rate Gamma), but the fiber configuration does not carry a smooth Lorentzian
causal order below Gamma_min (no definite section means no definite metric means no definite
light cone on X^4 from the observer's perspective). Above Gamma_min, the fiber configuration
decoheres to a definite metric and the Lorentzian causal order on X^4 is well-defined; this
is the classical shadow in which GU's equations hold.

**Literature anchor:** Standard smooth Lorentzian geometry; Lindblad time direction (Lindblad
1976); GU section s*(theta) = II_s at reconstruction grade
(`explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`).

**Class-assumption signature broken:** Preserves L4 Lorentzian assumption on the base X^4.
Adds a non-standard qualifier at the fiber level: below Gamma_min, the light cone structure
of X^4 (determined by the section-selected metric g_s) is quantum-indefinite. This is a
weaker modification than a causal-set or partial-order L4 drop; it is a conditionally-classical
Lorentzian order.

---

## Leg 5 — Emergence Class

**Class label:** (a) Specific-object substrate (Y^14 with the specific gimmel metric, the
Tikhonov-Willmore selected section s*, and the explicit coupling constant Lambda = 8 epsilon^2 / t_obs^2).

**Specification:** The substrate is a specific geometric object: Y^14 = Met(X^4) equipped
with the gimmel metric (Frobenius + trace-reversal, signature (9,5)), the Clifford spinor
module S = H^64, and the Sp(64) gauge bundle. The section is selected by the specific
variational principle E[s] + Lambda ||s - s_ref||^2 with Lambda = 8 epsilon^2 / t_obs^2
(explicit coefficient C_GU = 8 derived from the lowest TT eigenvalue of the Lichnerowicz
operator on S^4 at l=2, n=4; verified in `explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md`
and `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`). The emergence class is specific-object
(not a universality class); the candidate's heterodoxy is entirely in L3 (the pairing carries
the BvN coupling rule) and L6 (the Tikhonov-Willmore minimization drives section selection).

**Literature anchor:** GU Tikhonov regularization (Weinstein UCSD 2025-04 transcript);
Tikhonov (1943) (regularization theory); explicit Lambda coefficient derivation
(`explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md`); CPA-1 cross-program contact
(`explorations/geometry-curvature-emergence/cpa1-omega-tuning-2026-06-23.md`).

**Class-assumption signature broken:** Preserves the specific-object emergence assumption.
The no-go theorems' application to this specific object is what the BvN L1-L2 coupling
rule limits: Witten 1981 and others apply to the classical shadow of the specific object,
which is well-defined only above Gamma_min.

---

## Leg 6 — Coordination-Loop Class

**Class label:** (g) Stochastic gradient / RG flow as coordination dynamics — specifically
the Tikhonov-Willmore energy gradient flow that drives the section s toward the regularized
minimum s*, with Lambda = 8 epsilon^2 / t_obs^2 depending on the observer's classicality
parameters.

**Specification:** The coordination loop is the section-selection dynamics: starting from
a reference section s_ref, the observer runs Tikhonov-Willmore gradient descent

```
ds/dt = -nabla_s [E[s] + Lambda ||s - s_ref||^2]
       = -nabla_s E[s] - 2 Lambda (s - s_ref)
```

until convergence to s*. This is not a no-loop candidate (class (a)): the section s back-
reacts on the observer's classicality certification through the coupling
Lambda = 8 epsilon^2 / t_obs^2. Specifically: the Tikhonov regularization strength is set
by the observer's decoherence tolerance epsilon and finalization latency t_obs, which are
properties of the L2 observer. The observer-section coupling creates a feedback loop where
the observer's decoherence precision determines the energy scale Lambda that regularizes
the metric section, and the section's second fundamental form II_s determines (through the
Willmore energy gradient) the preferred metric and hence the light-cone structure on X^4.
The loop closes when the observer certifies s* as classical (Gamma >= Gamma_min), at which
point D_A*theta = 0 is well-posed at the selected section and GU's dark energy / distortion
condition holds on-shell.

**Literature anchor:** Tikhonov regularization (Tikhonov 1943); Willmore energy (Willmore 1965);
GU Tikhonov derivation at `explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md`; explicit Lambda
formula at `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`; observer-section coupling at
`explorations/time-as-finality-crosswalk/observer-section-error-model-2026-06-23.md`; L6 cadence confirmation at
`explorations/time-as-finality-crosswalk/fr4-l6-cadence-parameterization-2026-06-22.md`.

**Class-assumption signature broken:** Breaks the "no loop" (class (a)) assumption of the
standard no-go theorems. The Tikhonov-Willmore energy couples the observer's decoherence
parameters (epsilon, t_obs) to the section-selection energy scale Lambda, creating an
observer-substrate coordination loop that the no-go theorems do not model. The chirality /
anomaly content of the selected section s* depends on which section is selected, which
depends on Lambda, which depends on the observer's decoherence precision. Below Gamma_min,
the loop fails to converge (no definite section is selected) and the no-go theorems'
assumptions are not met.

---

## Chirality Bridge Claim

The substrate-level invariant carrying chirality is the **Sp(64) gauge bundle over Y^14
with the selected section s*: X^4 -> Y^14**, whose Clifford spinor module S = H^64
(from Cl(9,5) ~= M(64,H)) decomposes under SO(3,1) x Spin(6,4) as
S(9,5) = S(3,1) x S(6,4), with S(6,4) = C^16 carrying one SM generation under the
Pati-Salam decomposition (4,2,1) + (4bar,1,2) -- one SM generation per RS fiber spinor
contribution (verified at reconstruction grade in
`explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md`).

The forgetful operation is the Tikhonov-selected section pullback s*: the substrate Y^14
(with quantum metric fluctuations in the fiber) is mapped to its classical shadow -- the
selected metric g_{s*} on X^4 -- via the gradient flow convergence at Gamma >= Gamma_min.
At this shadow level, the Clifford spinor S(9,5) branches to S(3,1) x S(6,4), and the
SM chirality / 3-generation structure appears as the discrete-series Plancherel multiplicity
m_H(S(6,4)) = 24 (reconstruction-grade, from `explorations/representation-theory-noncompact/n5-discrete-series-gl4r-2026-06-23.md`).

The smooth-bundle shadow yields the null Witten / Nielsen-Ninomiya / Freed-Hopkins /
Distler-Garibaldi image because those theorems act on the classical section after the
forgetful operation; they do not see the BvN-gated coupling rule Gamma >= Gamma_min that
conditions the validity of the forgetful operation, nor the Tikhonov-Willmore coordination
loop (L6) that selects s*. The substrate-level invariant (the discrete-series multiplicity
m_H(S(6,4)) = 24) is preserved by the forgetful operation above Gamma_min; the no-go
theorems compute on the shadow and find no chirality obstruction because the specific
GU construction evades their assumptions at L1 (Y^14 fiber quantum fluctuations), L2
(decoherence-rate observer), L3 (BvN-gated pairing), and L6 (Tikhonov-Willmore loop).

---

## One First Falsification Test

**Test.** Attempt to formulate the GU Tikhonov-Willmore section selection

```
s* = argmin_{s in Gamma(pi)} [E[s] + Lambda ||s - s_ref||^2],    Lambda = 8 epsilon^2 / t_obs^2
```

as a well-defined quantum mechanical variational problem (i.e., without any classicality
requirement on the metric fiber), and check whether the minimizer is well-defined.

Concretely:

1. Replace the classical section s: X^4 -> Y^14 with a density operator rho_s on the
   fiber RP^3 ~= GL(4,R)/O(3,1) at each point x in X^4.
2. Define the Willmore energy E[rho_s] = integral_X Tr_{rho_s}[|II_s|^2] using the
   expectation value of the second fundamental form operator.
3. Define the Tikhonov regularization term Lambda ||rho_s - rho_{s_ref}||^2 using the
   Frobenius norm on the density operator.
4. Ask: does the minimizer rho_s* of E[rho_s] + Lambda ||rho_s - rho_{s_ref}||^2
   converge to a pure state (classical section) for all Lambda > 0, or does it remain
   genuinely mixed (quantum superposition of sections)?

**Falsification outcomes:**

- **The coupling rule is falsified (candidate collapses)** if: the quantum variational
  problem is well-posed and its minimizer rho_s* is always a pure state regardless of
  Gamma / Gamma_min. This would mean classicality of the section is automatic from the
  variational principle alone, not from the observer's decoherence rate -- making the
  BvN coupling rule redundant for the GU section selection.

- **The coupling rule is confirmed** if: for any Gamma < Gamma_min, rho_s* remains
  genuinely mixed (positive entropy), so D_A*theta = 0 evaluated at rho_s* is
  ill-posed as a classical field equation (theta = A - Gamma is not defined for a
  mixed-state metric). The BvN wall then enforces the coupling: only above Gamma_min
  does rho_s* collapse to a pure state and the GU field equations become well-posed.

- **Intermediate outcome (new obstruction):** the quantum Willmore minimizer is pure
  but the classical-shadow field equations D_A*theta = 0 still require a separate
  classicality certification -- which gates on a different coupling rule. This outcome
  would refine the Gamma_min condition rather than kill it.

**Runner.** Agent pass (quantum variational / Lindblad specialist) can compute the
eigenspectrum of the quantum Willmore Hessian and determine whether lowest eigenstates
are pure or mixed. The calculation uses the Lichnerowicz operator spectrum on S^4
(already computed in `explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md`; lowest TT
eigenvalue lambda_2 = 8/R^2) and the Lindblad decoherence superoperator.

**Why this test is load-bearing.** The entire candidate depends on the BvN coupling rule
being non-trivial for GU section selection: if the Tikhonov-Willmore minimum is always
classical regardless of the observer's decoherence rate, the L3 pairing degenerates to
class (a) (cartesian / smooth) and the candidate's heterodoxy collapses. The test directly
probes whether the section selection inherits the BvN non-classicality from the substrate
or suppresses it by the variational structure.

**Tied to no-go theorem assumption.** The test is tied to the Witten 1981 assumption that
the substrate presents a fixed classical smooth section for the no-go computation. If the
quantum Willmore minimizer is genuinely mixed below Gamma_min, Witten's computation
cannot be applied to this substrate below that threshold, and the evasion is genuine.

---

## Explicit Failure Conditions

Six conditions that would falsify the result:

1. **F1 (variational purity):** The quantum Willmore minimizer rho_s* is always pure for
   Lambda > 0, regardless of Gamma. If confirmed (by computing the lowest Hessian
   eigenvalue and showing it forces a pure state), the BvN coupling is redundant.

2. **F2 (Tikhonov independence):** The explicit formula Lambda = 8 epsilon^2 / t_obs^2
   is wrong -- the correct Tikhonov coefficient has a different form that does not
   couple to the observer's decoherence parameters epsilon and t_obs. If the coefficient
   depends only on the geometry (not on the observer), the L2-L3 coupling rule is not
   part of the GU construction.

3. **F3 (section-selection GU-first-principles failure):** The GU Lagrangian does not
   select a unique section via the Willmore / Tikhonov mechanism; the section is fixed
   by a gauge condition or boundary condition, not by a dynamical variational principle.
   If section selection is kinematic rather than dynamic, L6 degenerates to class (a)
   and the coordination loop is absent.

4. **F4 (BvN irrelevance for classical metrics):** The metric fiber GL(4,R)/O(3,1)
   carries only classical degrees of freedom in GU (no quantum metric fluctuations);
   the Lindblad decoherence model is a separate physical input not part of GU, and
   the BvN wall does not apply to the GU substrate. If GU is purely classical at
   the fiber level, L1 reduces to class (a) and the coupling rule is not load-bearing.

5. **F5 (coefficient mismatch):** The cross-program contact Lambda_GU = lambda_max^2
   (from CPA-1, `explorations/geometry-curvature-emergence/cpa1-omega-tuning-2026-06-23.md`) is not an algebraic
   identity but a coincidence. If the null-ray shot-noise model is not the correct
   observer-section error model for GU, the epsilon_sec = 1/(2 sqrt(2)) identification
   fails and the cross-program contact is lost, weakening the motivation for the
   coupling rule.

6. **F6 (P4 universality failure):** The denied functor proof at gate (i) fails at
   the P4 (universality / naturality) step -- no natural transformation between CAlg
   and OMLat exists that is functorial in the unitary group action. If P4 is refuted
   (e.g., by constructing a natural adjunction between the categories), the BvN wall
   is not a genuine obstruction and Gamma_min is not structurally required.

---

## Computation Grade and Residual Open Conditions

**Grade: reconstruction.** The six-axis specification is filled at reconstruction grade.
All six legs have class labels, specifications, literature anchors, and
class-assumption signatures. The chirality bridge claim and first falsification test are
stated. The load-bearing constraint Gamma >= Gamma_min = ln(1/epsilon)/t_obs is filled
explicitly with the derivation traceable to `fr2-bvn-layer5-promotion-gate-2026-06-23.md`
and `fr2-bvn-gate-ii-gu-result-2026-06-23.md`.

**Remaining open conditions before upgrade to verified:**

- RC1 (quantum Willmore well-posedness): The quantum variational formulation of the
  Tikhonov-Willmore minimization (Section "One First Falsification Test") has not been
  constructed; the test has not been run. This is the primary remaining check.

- RC2 (Lambda coefficient GU-first-principles): The coefficient C_GU = 8 in
  Lambda = 8 epsilon^2 / t_obs^2 has been derived at reconstruction grade via the
  Lichnerowicz operator on S^4 (null-ray shot-noise model), but the GU-first-principles
  derivation of the null-ray observer model has not been established from the GU
  Lagrangian or boundary conditions.

- RC3 (P4 BvN universality): The denied functor proof at gate (i) assessed P4 as
  reconstruction-grade residual; a verified proof of naturality failure in the
  BvN obstruction is needed.

- RC4 (discrete-series generation count): The chirality bridge claim rests on
  m_H(S(6,4)) = 24 (reconstruction grade); OQ3a-c from the discrete-series file
  gate this to CONDITIONALLY_RESOLVED, not VERIFIED.

**Promotion condition (from NEXT-STEPS.md fr2 residual table, now discharged):** One
filled six-axis example with the L1-L2 coupling rule as the load-bearing constraint.
This document satisfies that condition at reconstruction grade. The coupling rule
Gamma >= Gamma_min = ln(1/epsilon)/t_obs is admitted as an exploration-grade candidate
for the six-axis protocol's Current Coupling Rules section.

---

## Relation to Prior Six-Axis Examples

| prior example | axis differences | coupling rule difference |
| --- | --- | --- |
| example-02-sorkin-causal-set | L4 different (partial order vs. Lorentzian); L1 different (causal set vs. smooth bundle) | No L1-L2 coupling rule; L2 = standard finite Turing; no decoherence rate |
| example-03-rg-universality | L5 different (universality class vs. specific object); L6 different (RG flow as observer-independent dynamics) | No observer-rate coupling; RG flow is substrate-internal, not observer-coupled |
| this candidate | L2, L3, L6 different from 00d default | **L1-L2 coupling rule Gamma_min = ln(1/epsilon)/t_obs is the load-bearing new axis** |

The candidate is the first six-axis specification in this repo where L3 (pairing) carries
a quantitative coupling inequality between L1 (substrate coherence dynamics) and L2
(observer decoherence rate). This is also the first candidate where L6 (coordination loop)
is directly parameterized by L2 observer parameters (epsilon, t_obs enter Lambda).
