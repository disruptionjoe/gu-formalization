---
title: "BvN Gate (ii): GU Section-Selection Well-Posedness Changes at Gamma = Gamma_min"
date: 2026-06-23
problem_label: "fr2-bvn-gate-ii"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# BvN Gate (ii): GU Section-Selection Well-Posedness Changes at Gamma = Gamma_min

## 1. Problem Statement

NEXT-STEPS.md (FR-series residual table) lists two promotion gates for the Gamma_min
L1--L2 coupling rule to earn active-research status in the six-axis protocol:

> **(i)** Prove the BvN wall to Layer-5 rigor (define the denied functor; prove without
> smuggling). -- CONDITIONALLY_RESOLVED 2026-06-23 in `fr2-bvn-layer5-promotion-gate-2026-06-23.md`.
>
> **(ii)** Exhibit a GU result (anomaly cancellation input OR signed-readout scope condition)
> whose truth value changes when Gamma < Gamma_min.

This file discharges gate (ii) at reconstruction grade.

**Why gate (ii) matters.** Gate (i) proves the BvN wall is structurally real. Gate (ii) proves
that the wall is *load-bearing for GU*: some claim that GU makes -- either about anomaly
cancellation or about the scope of its signed-readout theorem -- is only valid when the
observer's substrate satisfies Gamma >= Gamma_min. Without gate (ii), the BvN wall and the
Gamma_min coupling could be formally correct but physically irrelevant to GU (the wall
crosses, but none of the GU machinery cares).

The GU result exhibited here is:

> **The classical field equation D_A*theta = 0 (GU's dark energy / distortion condition at
> the Tikhonov-selected section) changes truth value from WELL-POSED to ILL-POSED when
> Gamma falls below Gamma_min = ln(1/epsilon)/t_obs.**
>
> More precisely: the section-selection step that picks a definite A on which D_A*theta = 0
> is evaluated -- the Tikhonov-regularized Willmore minimization s*: X^4 -> Y^14 -- requires
> the observer to certify a classical (pointer-basis definite) metric value. That certification
> is the classicality step gated by Gamma >= Gamma_min (from FR2/fr2-bvn-layer5). Below
> Gamma_min, no classical section is available, and D_A*theta = 0 (as a classical field
> equation) is ill-posed: A is not defined, theta = A - Gamma is not defined, and the
> distortion equation is a statement about a quantum superposition of competing metric
> configurations, not a definite classical field.

**Corollary (anomaly cancellation input):** The pseudoreality argument for Sp(64) anomaly
cancellation (J^2 = -1 on S = H^{64} at the selected section) is an input to the anomaly
proof that is evaluated at the selected connection A. When Gamma < Gamma_min, the section
and connection are quantum-indefinite; the anomaly cancellation input is not a statement
about a definite representation but about a quantum mixture. The classical anomaly
computation changes scope from "Sp(64) on a definite H^{64}" to "quantum mixture over
competing Sp(64) structures," which is a different (and unresolved) object.

---

## 2. Established Context

This computation builds on:

- **FR2 Gamma_min definition:** `Gamma_min(epsilon) = ln(1/epsilon)/t_obs` is the minimum
  decoherence rate for the observer to certify a classical shadow of the L1 substrate.
  `explorations/time-as-finality-crosswalk/fr2-bvn-rate-of-classicality-derivation-2026-06-22.md`

- **BvN Layer-5 gate (i):** The inclusion I: CAlg -> OMLat has no left adjoint natural
  w.r.t. unitary action on Q(H) for dim H >= 2. Below Gamma_min, the observer's accessible
  event algebra E_obs(t_obs) is genuinely non-distributive.
  `explorations/misc/fr2-bvn-layer5-promotion-gate-2026-06-23.md`

- **GU dark energy / distortion:** D_A*theta = 0 proved on-shell via Noether for the
  Yang-Mills action; theta = A - Gamma_gimmel; condition is evaluated at the gauge connection
  A on the section s(X^4) c Y^14.
  DERIVATION-PROGRESS.md Layer 2 log entry (2026-06-22).

- **GU Tikhonov section selection:** Lambda ~ epsilon^2/t_obs^2 from Tikhonov regularization
  of the section selection problem on compactified X^4; the selected section s* minimizes
  E[s] + Lambda * ||s - s_ref||^2; Lambda explicitly depends on both epsilon and t_obs.
  `explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md` and `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`

- **Observer-section bridge model:** Under the quantum metric measurement model, the section
  precision epsilon_sec is related to the decoherence tolerance epsilon_dec by
  epsilon_sec^2 ~ epsilon_dec; the Tikhonov parameter Lambda_GU = C_GU * epsilon_sec^2 / t_obs^2
  depends on both the observer's classicality tolerance and the GU geometry.
  `explorations/time-as-finality-crosswalk/observer-section-error-model-2026-06-23.md`

- **Sp(64) anomaly cancellation input:** The pseudoreal fundamental representation of Sp(64)
  (J^2 = -1 on S = H^{64}) gives n_L - n_R = 0 cancelling the perturbative chiral anomaly.
  This is a property of the spinor module at a fixed section; the section choice determines
  which Clifford module structure is active.
  `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md`

---

## 3. Computation

### 3.1 The GU Section-Selection Classicality Requirement

In GU, the physical 4D physics is extracted from the 14D theory by choosing a section:

```
s: X^4 -> Y^14 = Met(X^4),   s(x) = (x, g_s(x)).
```

The section selection problem is: which section does GU predict? The Tikhonov-regularized
Willmore functional (from the P62/steelman-pass identification and CPA-1 computation) is:

```
s* = argmin_s [ E[s] + Lambda * ||s - s_ref||^2 ],   Lambda ~ epsilon_sec^2 / t_obs^2.
```

The Tikhonov parameter Lambda was derived by requiring that the section selection problem be
well-posed (the Hessian spectrum gap from the Willmore energy equals Lambda; from
`explorations/ii-s-horizontal-convention-hessian-2026-06-23.md` and
`explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md`).

**The observer's role.** The tolerance epsilon_sec is the section precision: the RMS
deviation of the observer's metric measurement from the true section. From the bridge model
(`observer-section-error-model-2026-06-23.md`):

```
epsilon_sec^2 ~ epsilon_dec   (quantum metric measurement model),
```

where epsilon_dec is the observer's decoherence tolerance (1 minus the fidelity of the
decohered state at time t_obs).

**The classicality requirement.** For the selected section s* to be a *definite classical
metric configuration* (rather than a superposition), the observer must be able to certify a
pointer-basis value for g_s(x) at each point x. This is precisely the classicality
certification requirement from FR2: the source state (the metric configuration) must have
decohered to within tolerance epsilon_dec on the observer's timescale t_obs.

**Formal statement.** The observer can certify a definite section s* iff:

```
Gamma >= Gamma_min(epsilon_dec) = ln(1/epsilon_dec) / t_obs.
```

Below Gamma_min, the metric state at each x is still in coherent superposition over competing
metric configurations; no pointer-basis definite g_s(x) is available; and the section
s*: X^4 -> Y^14 cannot be specified as a classical geometric object.

---

### 3.2 Impact on D_A*theta = 0: The Core GU Structural Result

The distortion equation D_A*theta = 0 is evaluated at the connection A on the selected
section. Specifically:

```
theta = A - Gamma_LC,   D_A*theta = 0.
```

Here A is the Sp(64) gauge connection pulled back to s*(X^4) c Y^14, and Gamma_LC is the
Levi-Civita connection of the gimmel metric on Y^14. The equation D_A*theta = 0 asserts that
the distortion (difference between the gauge connection and the canonical geometric connection)
is co-closed with respect to the gauge-covariant codifferential.

**Well-posedness above Gamma_min.** When Gamma >= Gamma_min:
- The observer certifies a definite section s* (classicality certification passes).
- A is a definite classical connection on s*(X^4).
- theta = A - Gamma_LC is a definite classical 1-form valued in ad(P).
- D_A*theta = 0 is a well-posed classical partial differential equation (an elliptic equation
  on a definite Riemannian/Lorentzian manifold with a definite gauge connection).
- TRUTH VALUE: WELL-POSED (and, by Noether, satisfied on-shell for the GU Yang-Mills action).

**Ill-posedness below Gamma_min.** When Gamma < Gamma_min:
- The observer's metric state is still in coherent quantum superposition over distinct metric
  configurations {g_alpha}: rho = sum_{alpha, beta} rho^{alpha beta} |g_alpha><g_beta|.
- There is no pointer-basis definite g_s(x); the section is not a classical map but rather a
  quantum-coherent mixture of sections {s_alpha} with off-diagonal coherences rho^{alpha beta}.
- The connection A is not a classical field but the expectation value <A> = sum_alpha p_alpha A_alpha
  (where p_alpha = rho^{alpha alpha}), plus off-diagonal quantum interference terms
  sum_{alpha != beta} rho^{alpha beta} <A_alpha - A_beta>.
- The distortion theta = A - Gamma_LC is not defined as a classical field; it inherits the
  quantum indeterminacy of A.
- D_A*theta = 0, interpreted as a classical field equation, is ILL-POSED: the operator D_A is
  not defined on a classical field (A is quantum-indefinite), so the equation has no classical
  truth value.
- TRUTH VALUE: ILL-POSED (the equation is a statement about a quantum-indefinite object;
  it does not have a classical WELL-POSED/SATISFIED/VIOLATED status).

**The truth-value change.** At the threshold Gamma = Gamma_min:
- Above Gamma_min: D_A*theta = 0 is WELL-POSED and ON-SHELL SATISFIED.
- Below Gamma_min: D_A*theta = 0 is ILL-POSED (no classical A to plug in).

This is the GU structural result required by gate (ii): a definite claim that GU makes
(the dark energy / distortion condition D_A*theta = 0) is only meaningful as a classical
field equation when the observer's substrate satisfies Gamma >= Gamma_min.

---

### 3.3 Impact on Sp(64) Anomaly Cancellation Input

The Sp(64) anomaly cancellation argument (NEXT-STEPS.md N2, RESOLVED) asserts:

> The fundamental representation of Sp(64) on S = H^{64} is pseudoreal (J^2 = -1), giving
> n_L - n_R = 0 and cancelling the perturbative chiral anomaly in 14D.

This argument is a statement about the representation of Sp(64) on the spinor module S = H^{64}
at the selected section. Specifically: at each fiber point h in Y^14 (equivalently, at each
metric configuration g in Met(X^4)), the spinor module is S_h = H^{64}, and the anomaly
cancellation input (J^2 = -1) is a property of this module.

**Above Gamma_min.** The observer certifies a definite section s*, picking a definite fiber
point h* = s*(x) at each x in X^4. The anomaly cancellation input (J^2 = -1 on S_{h*}) is
a definite classical statement about a fixed H^{64}-module. The pseudoreality argument goes
through unambiguously: the representation is pseudoreal, n_L - n_R = 0 (exact).

**Below Gamma_min.** No definite h* exists. The observer's state is a quantum superposition
over fiber points {h_alpha}. The anomaly computation would need to be run on the quantum
mixture rho = sum_alpha p_alpha |h_alpha><h_alpha| + coherences. The relevant object is not
"Sp(64) on H^{64}" at a fixed fiber point but "Sp(64) acting on the quantum-mixed collection
{H^{64}_{h_alpha}}."

**Is this a change in the anomaly cancellation verdict?**

The answer is nuanced. The pseudoreality property (J^2 = -1) is a fiber-by-fiber algebraic
fact: at each fiber point h, J_h^2 = -1 on S_h = H^{64}_h. This is a property of Cl(9,5)
acting on H^{64} and does NOT depend on which fiber point is selected -- it is an algebraic
identity of the representation, not a geometric fact about the section.

**However**, the anomaly cancellation argument uses this algebraic fact to conclude that the
physical spectrum of the 14D Dirac operator D_GU satisfies n_L - n_R = 0. This conclusion
requires the Dirac operator to be a well-defined classical differential operator on a
definite classical gauge bundle over a definite classical section. Below Gamma_min:

- The Dirac operator D_GU is not a definite classical operator; it acts on sections of
  the spinor bundle over the quantum-mixture section.
- The index theorem (which gives n_L - n_R = 0 from ind_H(D_GU) = 0 for Sp(64)) requires
  an elliptic operator on a compact or controlled non-compact manifold with a definite metric.
- Below Gamma_min, the metric is quantum-indefinite and the index theorem inputs are ill-posed.

**TRUTH VALUE CHANGE (anomaly input):**
- Above Gamma_min: anomaly cancellation input (pseudoreality) is a valid input to the
  classical anomaly computation; the spectrum conclusion n_L - n_R = 0 follows.
- Below Gamma_min: anomaly cancellation input is still algebraically valid fiber-by-fiber,
  but the SCOPE of the conclusion changes: n_L - n_R = 0 is a statement about the
  quantum-mixed Dirac operator, not the classical Dirac operator. The classical anomaly
  cancellation conclusion requires Gamma >= Gamma_min to have its standard interpretation.

This is a SCOPE CONDITION change: the anomaly cancellation result holds classically only
when the observer can certify a classical section. Below Gamma_min, it is a quantum statement
with different content.

---

### 3.4 The Signed-Readout Scope Condition

**Prior result (confirmed, closed).** The signed-readout monotonicity criterion is
RATE-INDEPENDENT: the structural truth of the monotonicity theorem does not depend on
lambda or Gamma (from `explorations/time-as-finality-crosswalk/rate-independence-worked-check-2026-06-22.md`).
This finding is NOT overturned by the present computation.

**Clarification of why signed-readout is not affected.** The signed-readout theorem operates
*post-classicality*: it assumes a classical shadow exists and asks whether the monotonicity
condition is satisfied. The theorem is pre-certified as classical: it reasons about definite
classical records, not about quantum-indefinite states. The Gamma_min condition is
*pre-classicality*: it gates whether a classical shadow exists at all.

**What changes at Gamma_min for the signed-readout.** Below Gamma_min:
- There is no classical shadow to apply the signed-readout theorem to.
- The SCOPE of the signed-readout theorem changes: from "applies to the GU 4D reduction
  shadow" to "not applicable because no classical shadow is available."

This is a SCOPE CONDITION change, not a TRUTH VALUE change of the monotonicity criterion
itself. The distinction is important: the signed-readout rate-independence finding (that
lambda does not appear in the monotonicity criterion) remains valid; what changes below
Gamma_min is the APPLICABILITY of the theorem, not its truth.

The signed-readout scope condition is:

```
[GU 4D signed readout is applicable] iff Gamma >= Gamma_min(epsilon_sec).
```

This is a new positive scope condition derived from the Gamma_min coupling and the
section-selection classicality requirement. It is weaker than a truth-value change of the
monotonicity criterion but is a genuine structural condition on GU's observer-facing claims.

---

### 3.5 The Gate (ii) Result in Minimal Form

To be precise about what changes and what the failure condition is:

**Result statement (gate ii, reconstruction grade):**

The GU field equation D_A*theta = 0 is a classical field equation that requires a definite
classical section s*: X^4 -> Y^14 for its formulation. The section-selection step uses the
Tikhonov-regularized Willmore energy with parameter Lambda = C_GU * epsilon_sec^2 / t_obs^2.
Under the observer-section bridge model (epsilon_sec^2 ~ epsilon_dec), this parameter depends
on the observer's decoherence tolerance epsilon_dec and finalization latency t_obs. The
classicality of the selected section requires Gamma >= Gamma_min = ln(1/epsilon_dec)/t_obs
(from FR2). Therefore:

```
THEOREM (reconstruction): D_A*theta = 0 is well-posed as a classical GU field equation
if and only if the substrate decoherence rate satisfies:
    Gamma >= Gamma_min(epsilon_dec) = ln(1/epsilon_dec) / t_obs.

Below Gamma_min, the equation D_A*theta = 0 is ill-posed: A is quantum-indefinite, theta
is quantum-indefinite, and D_A*theta = 0 is a statement about a quantum mixture, not a
classical field equation.
```

**Corollary (anomaly input scope):**

```
COROLLARY (reconstruction): The classical anomaly cancellation conclusion -- n_L - n_R = 0
for the classical Dirac operator D_GU on the selected 14D background -- holds in its
standard classical form if and only if Gamma >= Gamma_min. Below Gamma_min, the conclusion
holds only as a statement about the quantum-mixed Dirac operator (a different, unresolved
object).
```

**Corollary (signed-readout scope):**

```
COROLLARY (reconstruction): The signed-readout theorem of GU's 4D shadow is applicable to
a definite observer record if and only if Gamma >= Gamma_min. Below Gamma_min, no classical
shadow is certified; the signed-readout theorem is out of scope.
```

---

### 3.6 Why This Is Non-Trivial

One might object: "D_A*theta = 0 is a theorem of GU's Yang-Mills action, not an empirical
claim; its truth is not observer-dependent."

**Rebuttal.** The equation D_A*theta = 0 requires the following classical inputs:
1. A definite section s: X^4 -> Y^14 (so that the equation can be restricted to s(X^4)).
2. A definite gauge connection A on the Sp(64) bundle over s(X^4).
3. A definite Levi-Civita connection Gamma_LC of the gimmel metric g_Y.
4. The distortion theta = A - Gamma_LC as a definite classical field.

All four inputs require a definite classical metric configuration -- which in turn requires
the observer to have certified a definite pointer-basis metric value. GU's claim is not
merely the algebraic identity "for any section, D_{s*(A)}*theta = 0"; it is the physical
claim "the selected physical section satisfies D_A*theta = 0." The selection step is where
the classicality requirement enters.

The theorem D_A*theta = 0 (Noether's theorem applied to the Yang-Mills action) holds for
*any* definite classical configuration. The question is which definite classical configuration
GU predicts. That question requires the section-selection problem to be solved, which
requires Gamma >= Gamma_min. Below Gamma_min, there is no definite classical configuration
to which the theorem applies.

**Analogy.** This is structurally identical to saying: "the equations of GR are
G_{mu nu} = 8 pi G T_{mu nu}; they are metric-dependent; below some coherence threshold,
the metric is quantum-indefinite and GR as a classical field theory is inapplicable." The
BvN gate (ii) finding says the same thing about GU's distortion equation, grounded in the
specific GU section-selection mechanism and the Gamma_min coupling rule from FR2.

---

## 4. Result

**Verdict: CONDITIONALLY_RESOLVED at reconstruction grade.**

Gate (ii) is discharged at reconstruction grade:

- **Primary result:** D_A*theta = 0 (GU dark energy / distortion condition) changes truth
  value from WELL-POSED (above Gamma_min) to ILL-POSED (below Gamma_min). This is the GU
  structural result exhibiting sensitivity to the decoherence threshold.

- **Anomaly input corollary:** The classical anomaly cancellation conclusion (n_L - n_R = 0
  for the classical Dirac operator) changes scope from "classical" to "quantum-mixed" below
  Gamma_min. The algebraic pseudoreality input is unchanged fiber-by-fiber; the scope of
  the classical conclusion changes.

- **Signed-readout corollary:** The signed-readout theorem's applicability gates on
  Gamma >= Gamma_min. This is a scope condition, not a truth-value change of the monotonicity
  criterion (the rate-independence finding stands).

**Remaining gaps for upgrade to VERIFIED:**

1. **G1 (section-selection physical model):** The observer-section bridge model
   (epsilon_sec^2 ~ epsilon_dec) requires a GU-first-principles derivation, not just a
   quantum-measurement-model assumption. Currently at reconstruction grade from
   `observer-section-error-model-2026-06-23.md`.

2. **G2 (quantum-mixed Dirac operator):** What does D_A*theta = 0 mean for a
   quantum-mixed section? If the mixed Dirac operator can be defined (e.g., as an expectation
   value), the "ill-posed" characterization should be replaced with a precise statement about
   which form the equation takes in the quantum-mixed regime. This is an open mathematical
   problem beyond current scope.

3. **G3 (Tikhonov from first principles):** The Tikhonov-regularized section selection
   (Lambda ~ epsilon_sec^2/t_obs^2) is a phenomenological model for section selection; its
   derivation from GU's first principles (the Willmore functional alone, without P62
   observer-identification) is not completed. If the section selection is purely classical
   (no observer required), the Gamma_min sensitivity disappears. This is the key
   falsification condition.

---

## 5. Explicit Failure Conditions

**F1 (No quantum-classical bridge in GU).** If the section s: X^4 -> Y^14 is selected by
a purely classical variational principle (no observer required), the Tikhonov parameter
Lambda has no epsilon_dec dependence and the Gamma_min sensitivity disappears. The distortion
equation D_A*theta = 0 is then a theorem for any classical section, not conditioned on
Gamma. FALSIFICATION STATUS: This is the main structural risk. If GU's section selection
is purely classical, gate (ii) is not discharged by this route.

**F2 (Fiber-by-fiber pseudoreality breaks the argument).** The Sp(64) pseudoreality J^2 = -1
is a fiber-by-fiber algebraic fact of the Clifford module (Cl(9,5) ~= M(64,H)), independent
of the section choice. If one argues the anomaly cancellation is purely algebraic and
section-independent, the scope condition from gate (ii) does not affect the core anomaly
cancellation verdict. FALSIFICATION STATUS: Partially falsified; the algebraic pseudoreality
input is section-independent, but the classical anomaly computation's spectral conclusion
(n_L - n_R = 0 as an index theorem) requires a definite classical section.

**F3 (Quantum section theory exists).** If a mathematically well-posed quantum section theory
is developed (quantizing the section s as a quantum field, integrating over sections in a
path integral), the "ill-posed" characterization below Gamma_min would be replaced by a
well-posed quantum statement. In that case, the gate (ii) result would need to be
reformulated: the relevant change would be from "classical section theory" to "quantum
section theory," not from "well-posed" to "ill-posed." FALSIFICATION STATUS: Not a
falsification but a reframing; gate (ii) would still be discharged (a GU result changes --
from classical to quantum formulation -- at Gamma_min).

**F4 (Observer-section identification is wrong).** If the P62 observer-section identification
(identifying the observer's measurement with the section choice) is physically unjustified,
the bridge epsilon_sec^2 ~ epsilon_dec does not hold and the Tikhonov parameter is not a
function of the observer's decoherence tolerance. FALSIFICATION STATUS: This is an
exploration-grade identification; it requires promotion from P62 steelman status to canon
before gate (ii) can be upgraded to VERIFIED.

**F5 (Signed-readout rate-independence extends to scope).** If a more careful analysis shows
the signed-readout theorem is applicable even below Gamma_min (e.g., because it is a purely
mathematical statement about any function, not about a physical certified record), the scope
condition corollary does not represent a genuine change. FALSIFICATION STATUS: This would
narrow the result to the primary D_A*theta = 0 change; the core gate (ii) discharge via the
dark energy condition would survive.

---

## 6. Open Questions

**OQ1 (Classical section selection).** Does GU's variational principle (Willmore energy
E[s] = integral |II_s|^2) select a unique classical section without any observer input? If
yes, can the Tikhonov parameter Lambda be derived from the GU equations alone, without the
observer-section identification? This is the key open question for upgrading from
reconstruction to verified.

**OQ2 (Quantum-mixed operator formulation).** For a quantum mixture of sections
rho = sum_alpha p_alpha |s_alpha><s_alpha| + coherences, what is the appropriate form of
the distortion equation? Is D_{<A>}*<theta> = 0 (classical equation for expectation values)
a valid quantum-classical correspondence, or does the correct quantum distortion equation
require a different formulation? This is beyond current scope but is the right next question
if gate (ii) is accepted at reconstruction grade.

**OQ3 (Physical Gamma_min for GU substrate).** If GU's L1 substrate has a specific Hilbert
space and decoherence dynamics, what is its actual Gamma? Is it above or below Gamma_min
for physically reasonable epsilon and t_obs values? The gate (ii) result is an existence
statement ("a GU result changes at Gamma_min"); making it a concrete prediction requires
specifying the GU substrate's actual decoherence rate. This depends on the quantum gravity
model, which is beyond the current reconstruction-grade formalization.

**OQ4 (Six-axis example with Gamma_min as load-bearing constraint).** Gate (ii) together
with gate (i) (fr2-bvn-layer5) together constitute the package required to admit the
Gamma_min coupling rule as a Current Coupling Rule in the six-axis protocol. The remaining
promotion condition from fr2-bvn-layer5 (a filled six-axis example where the L1--L2 coupling
is the load-bearing structural constraint) is still unmet. OQ4 is: fill that example using
the GU section-selection context (L1 = metric bundle Y^14 with decoherence dynamics, L2 =
observer certifying section s*, load-bearing coupling = lambda_max <= Gamma/ln(1/epsilon)).

---

## 7. Cross-References

- FR2 Gamma_min definition and coupling: `explorations/time-as-finality-crosswalk/fr2-bvn-rate-of-classicality-derivation-2026-06-22.md`
- BvN gate (i) (Layer-5 formal denial): `explorations/misc/fr2-bvn-layer5-promotion-gate-2026-06-23.md`
- Observer-section bridge model: `explorations/time-as-finality-crosswalk/observer-section-error-model-2026-06-23.md`
- Tikhonov coefficient (C_GU = 8, Lambda derivation): `explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md`
- II_s moving frames (Tikhonov/Willmore computation): `explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md`
- Anomaly cancellation input (Sp(64) pseudoreality): `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md`
- Dark energy Noether proof: DERIVATION-PROGRESS.md Layer 2 log (2026-06-22)
- Signed-readout rate-independence (closed negative finding): `explorations/time-as-finality-crosswalk/rate-independence-worked-check-2026-06-22.md`
- FR-series synthesis: `explorations/time-as-finality-crosswalk/fr-series-synthesis-2026-06-22.md`
- NEXT-STEPS.md FR2 residual table (promotion gates listed)
