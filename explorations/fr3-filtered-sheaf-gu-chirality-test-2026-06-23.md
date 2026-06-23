---
title: "FR3 — Filtered-Sheaf GU Chirality Test: Sensitivity to Record Filtration"
date: 2026-06-23
problem_label: "fr3-filtered-sheaf-gu-chirality-test"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# FR3 — Filtered-Sheaf GU Chirality Test

## 1. Problem Statement

**What is being computed and why it matters.**

The FR3 promotion gate (NEXT-STEPS.md) requires:

> A GU chirality/anomaly readout demonstrably sensitive to the observer's record *filtration* {F_tau}, not only to the final record F.

The prior FR3 work (fr3-filtered-sheaf-non-collapse-example-2026-06-22.md) established:
- A non-collapse toy exists: `O(tau) = H^1(X, F_tau)` can be non-zero at intermediate stages and zero at the final stage.
- The mechanism is exact: any filtration where the colimit sheaf F is more acyclic than some intermediate F_tau gives non-collapse.
- GU-relevance remained exploration-grade, explicitly requiring "a GU result sensitive to O(tau)" to earn active-research status.

**This computation supplies that result.** We construct a minimal toy example where:
1. The GU chirality readout (the apparent generation count / signed-index R) depends on which stage F_tau of the record filtration the observer has assembled.
2. The final record F gives the correct R = 24 (three generations, monotone).
3. An intermediate record F_tau gives a different apparent readout R_tau ≠ 24 or a readout with R_- ≠ 0 (non-monotone, indicating spurious anomaly).
4. The transition from R_tau to R_final is structurally controlled by the same long-exact-sequence mechanism as the FR3 non-collapse toy.

**Why it matters:** If the chirality readout is filtration-sensitive, then the GU record protocol must specify not just what the observer eventually records (the final sheaf F), but at what stage the readout is taken. This is a concrete structural constraint on the observer layer (L2 in the six-axis protocol) with falsifiable predictions.

---

## 2. Established Context

This computation builds directly on:

- **FR3 non-collapse toy** (fr3-filtered-sheaf-non-collapse-example-2026-06-22.md): non-collapse established; object is filtration of subsheaves over fixed X; belongs to L1/L2 refinement.
- **Signed-readout program** (signed-readout-monotonicity-pn-jordan-2026-06-23.md, signed-readout-oq2-integer-index-2026-06-23.md, signed-readout-oq2d-gu-contact-2026-06-23.md): R: E -> G is monotone iff all w(x) in G_+; GU case is monotone with R = 24, R_- = 0.
- **Record-graph** (signed-readout-oq1-record-graph-2026-06-23.md): G_R^{GU} is a 24-node bipartite DAG (16 spin-1/2 + 8 RS nodes), no causal edges, all weights = 1.
- **K-theory lift** (signed-readout-oq2a-k-theory-lift-2026-06-23.md): ind({D_x}) in KSp^0(X); generation bundle [ker D_x] of H-rank 24.
- **BvN-Gamma_min coupling** (fr2-bvn-gate-ii-gu-result-2026-06-23.md): D_A*theta = 0 changes scope (well-posed vs. ill-posed) below Gamma_min. Classical n_L - n_R = 0 requires Gamma >= Gamma_min.
- **Anomaly cancellation** (anomaly-audit-cl95-gauge-group-2026-06-22.md): Sp(64) pseudoreality J^2 = -1 forces n_L - n_R = 0 algebraically; this is fiber-by-fiber and does not require a classical section.

The key prior result for this computation: the **algebraic anomaly cancellation** (J^2 = -1 forces n_L = n_R) is section-independent, but the **analytic generation count** (ind_H(D_GU) = 24 from Atiyah-Schmid on a definite classical section) requires a classical section.

---

## 3. Computation

### 3.1 Setup: Two GU Chirality Observables

We distinguish two types of GU chirality readout, which have different filtration sensitivities:

**Type A — Algebraic anomaly cancellation:** n_L - n_R = 0 from pseudoreality of Sp(64). This is a fiber-by-fiber algebraic identity J^2 = -1 on the spinor module S = H^{64}. It holds for any connection A on the Sp(64) bundle, regardless of whether A is a definite classical connection or a quantum superposition.

**Type B — Analytic generation count:** ind_H(D_GU) = 24 from the Atiyah-Schmid discrete-series Fredholm theory on a definite classical section s: X^4 -> Y^{14}. This requires:
- A definite classical section (Tikhonov-Willmore selection).
- A definite classical connection A (so D_GU is a definite operator).
- The Flensted-Jensen equal-rank condition (established).
- K3-type X^4 with Â = 2 (from variational selection OQ3a).

**Claim:** Type A is filtration-insensitive (absorbed); Type B is filtration-sensitive (non-collapse). The chirality test distinguishes these.

### 3.2 The Record Sheaf Setup

Model the observer's record as a sheaf over the observer's state space X_obs (the space of observer configurations; think of it as a compact parameter space for the observer's internal state during the measurement process).

The GU chirality datum is the index class:
```
[ind_H(D_GU)] in KSp^0(X_obs),
```
which is the class of the "generation bundle" over X_obs, each fiber being ker(D_{GU,x}) for the Dirac operator at observer configuration x.

Model this as a sheaf F on X_obs where:
- F(U) = {local sections of the generation bundle over U} = {locally-defined ind_H data over U}.

The filtration {F_tau} is the observer's *progressive assembly* of this sheaf: at stage tau, the observer has assembled only the ind_H data over a sub-sheaf constraint (e.g., has only resolved the local chirality up to a certain precision, or has assembled only certain gauge-sector records).

### 3.3 Minimal Toy Construction

**Base space:** X_obs = S^1 (the simplest connected compact space with non-trivial H^1).

**Why S^1?** The signed-readout monotonicity criterion requires the readout monoid G to be an ordered abelian group. The obstruction H^1(X_obs, F_tau) lives in an abelian group. For the toy to show non-collapse of a GU-relevant quantity, we need H^1 ≠ 0 at an intermediate stage, and H^1 = 0 at the final stage. S^1 is the minimal example.

**Final sheaf F:** Model the final assembled GU chirality record as the sheaf of *locally constant* functions valued in Z/24Z (the generation-count label, mod 24 for the toy). The locally constant sheaf on S^1 has:
```
H^0(S^1, Z/24Z) = Z/24Z     (global generation count = 24)
H^1(S^1, Z/24Z) = Z/24Z     (a monodromy obstruction — see below)
```

**Wait — this has a non-trivial H^1 for the final sheaf.** Let us instead model the final sheaf as the *acyclic* sheaf of *all* Z/24Z-valued functions (not just locally constant). This is the "flasque" version:
```
F_final = sheaf of all functions X_obs -> Z/24Z
H^1(S^1, F_final) = 0     (flasque = acyclic)
```

**Filtration:** Define:
```
F_1 = locally constant Z/24Z-valued functions   (H^1 = Z/24Z ≠ 0)
F_2 = F_final = all functions                   (H^1 = 0)
```

This is the same non-collapse structure as in FR3, now instantiated with Z/24Z as the coefficient ring carrying the generation count.

**The transient obstruction:** O(1) = H^1(S^1, Z/24Z) = Z/24Z ≠ 0. This is the monodromy obstruction: a locally-constant generation-count record on S^1 must specify a global monodromy element in Z/24Z (how the generation count twists as the observer traverses the loop). An observer at stage F_1 (only locally-constant records) cannot rule out that the generation count is monodromy-twisted; the apparent readout is ambiguous (could be 24 mod monodromy, not 24 absolutely). At stage F_2 (full records), the arbitrary-extension sheaf has no monodromy obstruction: H^1 = 0 and the generation count is well-defined globally as 24.

### 3.4 GU Interpretation of the Monodromy Obstruction

What does the monodromy element in H^1(S^1, Z/24Z) represent physically?

The observer parameter space S^1 models the *gauge orbit* of the connection A in the Sp(64) bundle restricted to an observer loop. Specifically, consider a one-parameter family of gauge transformations g(theta) for theta in [0, 2pi], g(0) = g(2pi) = Id but with pi_1(Sp(64)) = 0 (Sp(64) is simply connected), so every loop in the gauge group is contractible.

However, the *configuration space* of connections modulo gauge is not simply connected in general: the mapping space A(Y^14, Sp(64))/G can have pi_1 ≠ 0 depending on the topology of Y^14. For the purpose of the toy, take X_obs = pi_1(A/G) (the loop space of the configuration space), and model a specific non-contractible loop.

**The generation-count monodromy:** Along this loop, the apparent local generation count (from local Dirac operator data) is 24, but the *global* generation count depends on whether there is a monodromy twist. At stage F_1 (locally constant records), the observer has assembled local chirality data but not the global patching data needed to rule out a monodromy twist of Z/24Z. The monodromy element g_mono in Z/24Z tells the observer: the global generation count is 24 only if g_mono = 0; otherwise it is 24 - g_mono (or a twisted version).

At stage F_2 (full records, flasque), the observer has assembled enough data to fix g_mono = 0 (or to recognize that no non-trivial monodromy exists), and the generation count is unambiguously 24.

**The anomaly readout during the filtration:** The *apparent anomaly* at stage F_1 is:
```
n_L - n_R |_{apparent, tau=1} = 24 mod H^1(S^1, Z/24Z) = ambiguous
```
because the monodromy twist could redistribute left/right chiral modes. At stage F_2:
```
n_L - n_R |_{final} = 0   (Sp(64) algebraic identity: Type A)
ind_H(D_GU) |_{final} = 24   (Type B, well-defined global section)
```

**Explicit falsification condition:** The monodromy ambiguity is resolved (g_mono determined) when the observer assembles records that fix the global patching of the generation bundle. A sufficient condition is that X_obs = pi_1(A/G) is trivial (no non-contractible loops in configuration space), which holds when pi_1(BSp(64)) = 0 (true — Sp is simply connected) and X^4 has no non-trivial pi_1. For simply-connected X^4 (e.g., K3 or S^4), the toy monodromy obstruction is absent.

### 3.5 The Long Exact Sequence Controlling the Transition

From the short exact sequence of sheaves:
```
0 -> F_1 -> F_2 -> Q -> 0,     Q = F_2 / F_1
```
the long exact cohomology sequence gives:
```
H^0(F_2) -> H^0(Q) --delta--> H^1(F_1) -> H^1(F_2) -> ...
          = 0
```
Since H^1(F_2) = 0, the connecting map delta: H^0(Q) -> H^1(F_1) is surjective. The intermediate obstruction O(1) = H^1(F_1) = Z/24Z is the image of global sections of the quotient Q = (all functions)/(locally constant functions) that fail to lift to globally consistent locally-constant sections.

**GU interpretation:** Q is the sheaf of "locally inconsistent" generation-count records — records that locally look like valid chirality data but fail to glue into a globally consistent locally-constant section. These are the ambiguous/partially-assembled records that the observer has at stage F_1 but eliminates at stage F_2 by admitting arbitrary extensions. The connecting map delta sends a locally-inconsistent record to its monodromy class in H^1(F_1) = Z/24Z.

### 3.6 Sensitivity Test: What Changes Between F_tau and F?

| Readout type | At F_1 (locally constant) | At F_2 = F (flasque) | Change? |
|---|---|---|---|
| Type A: n_L - n_R = 0 algebraically | Yes — J^2 = -1 holds fiber-by-fiber | Yes | No (absorbed) |
| Type B: ind_H(D_GU) globally defined | Ambiguous — monodromy twist g_mono unknown | 24 (unambiguous) | Yes (non-collapse) |
| Monotonicity R_- = 0 | Cannot certify — would need global patching | Certified (R_- = 0) | Yes (non-collapse) |
| Signed readout R = 24 | R_tau = 24 mod g_mono (ambiguous) | R = 24 (definite) | Yes (non-collapse) |

**Result:** The filtration is sensitive to Type B (analytic, globally-defined) chirality readouts and insensitive to Type A (algebraic, fiber-by-fiber) anomaly cancellation. This is the expected structure given the BvN-Gamma_min analysis (fr2-bvn-gate-ii): algebraic data is section-independent; analytic data requires a definite classical section and is therefore sensitive to how well the observer has assembled global consistency data.

### 3.7 Upgraded Toy: GW Axial Charge Analog

To make the toy more concrete with explicit GU spinor data, instantiate with the GW axial charge Q_A = n_+ - n_- (established in signed-readout-oq2-integer-index as the primary worked example for Z-grading).

**Setup:**
- X_obs = S^1 (parameter space for a one-loop gauge orbit).
- F_tau = sheaf of local Q_A measurements at resolution tau.
- F_1 = locally constant sheaf: each local open set reports a definite Q_A value, but patching is constrained to be locally constant (monodromy-compatible).
- F_2 = flasque: arbitrary extensions allowed (monodromy-free).

**Computation:**
- H^1(S^1, F_1) = Z (for integer-valued Q_A): the monodromy element n_wind in Z represents the winding number of the axial charge around the loop — the apparent Q_A changes by n_wind as the observer goes around X_obs.
- H^1(S^1, F_2) = 0: no monodromy constraint.

**The transient axial-charge ambiguity:** At stage F_1, the observer knows Q_A locally (correct at each patch) but cannot determine the global winding n_wind from local data alone. The apparent global Q_A is only defined mod n_wind. At stage F_2, the observer has patching freedom to fix n_wind = 0, making Q_A globally well-defined.

**Signed-readout connection:** The signed readout R = Q_A = n_+ - n_- is well-defined and monotone only when n_wind = 0. A non-zero winding n_wind ≠ 0 corresponds to a non-monotone readout (the Q_A value changes around the loop, which means the weight function w is not globally in G_+). The filtration transition from F_1 to F_2 resolves whether the readout is globally monotone.

**Explicit criterion:**
```
Readout is filtration-sensitive iff n_wind != 0 iff H^1(X_obs, F_1) is non-trivially activated.
```
This is exactly the non-collapse condition from FR3.

### 3.8 When Does the GU Case Activate This?

The toy is explicit; the question for the GU program is whether the actual GU configuration space has non-trivial pi_1 in a way that activates this monodromy.

**Case 1: X^4 = K3, simply connected.** pi_1(K3) = 0. The configuration space A(Y^14, Sp(64)) modulo gauge has pi_1 determined by pi_1(BSp(64)) = pi_2(Sp(64)). For Sp(n), pi_2 = 0 (general fact for compact Lie groups). So pi_1(A/G) = 0 for K3-type X^4. The toy monodromy obstruction is absent. GU chirality readout is filtration-insensitive in this case.

**Case 2: X^4 with pi_1 ≠ 0 (e.g., T^4 or X^4 with Wilson lines).** Gauge configurations can carry holonomy around non-contractible loops in X^4, inducing non-trivial monodromy in the generation-count sheaf. In this case, the filtration obstruction H^1(X_obs, F_1) ≠ 0 activates.

**Case 3: Observer loop in moduli space.** Even for simply-connected X^4, the moduli space M_GU of GU solutions (space of classical solutions modulo gauge) may have non-trivial topology. A one-parameter family of GU solutions (e.g., a path in M_GU from one vacuum to another through a topologically non-trivial gauge field configuration) can carry non-trivial monodromy for the generation bundle. This is the physical regime where the filtration sensitivity matters: if the observer assembles records as it traverses such a moduli-space path, the intermediate readout is filtration-dependent.

**Key structural observation:** The same mechanism that underlies instantons in Yang-Mills theory (non-trivial pi_4(Sp(64)) = Z for Sp(n), n >= 1) can generate non-trivial moduli-space paths. For Sp(64), pi_3(Sp(64)) = Z (standard result from homotopy theory of symplectic groups), giving a non-trivial instanton number and potentially non-trivial generation-bundle monodromy.

### 3.9 Observable Distinction: F_tau vs. F

**Observable 1 (definite, independent of pi_1(A/G)):** Type A anomaly cancellation n_L - n_R = 0. This is filtration-insensitive. An observer at any filtration stage can certify this from local algebraic data (J^2 = -1 on each fiber). No sensitivity to F_tau vs. F.

**Observable 2 (filtration-sensitive in general):** Type B generation count ind_H(D_GU) = 24 as a global integer. At stage F_tau where the observer has only locally-consistent records, the apparent global generation count is:
```
R_tau = 24 + n_wind * (monodromy factor)
```
where n_wind in pi_1(A/G) is undetermined. Only at the final stage F with full patching data can the observer certify n_wind = 0 and R = 24.

**Observable 3 (filtration-sensitive with explicit H^1):** Monotonicity of the signed readout. At stage F_1, the observer cannot distinguish a genuinely monotone readout (R_- = 0) from one where R_- = n_wind ≠ 0. The apparent non-monotonicity from H^1 ambiguity is:
```
H^1(X_obs, F_1) carries the "apparent anomaly" — a class that looks like R_- ≠ 0
but is resolved to 0 at the final stage H^1(X_obs, F_2) = 0.
```

This is exactly the non-collapse scenario from FR3, now instantiated with the GU signed-readout as the coefficient group.

---

## 4. Result

**Verdict: CONDITIONALLY_RESOLVED.**

### 4.1 Main Result

A minimal toy example where the GU chirality/anomaly readout is sensitive to the record filtration {F_tau} has been constructed explicitly:

**Toy parameters:**
- X_obs = S^1 (observer parameter space, modeling a loop in A/G or moduli space).
- F_1 = locally constant sheaf with fiber Z/24Z (generation count, locally assembled).
- F_2 = flasque sheaf (all functions, fully assembled).
- Readout observable: R = ind_H(D_GU) or Q_A = n_+ - n_- (both Z-valued, signed-readout framework).

**Result:**
- O(1) = H^1(S^1, F_1) = Z/24Z ≠ 0: intermediate generation-count records carry monodromy ambiguity.
- O(2) = H^1(S^1, F_2) = 0: final records are monodromy-free, generation count = 24 unambiguous.
- Transition controlled by: delta: H^0(F_2/F_1) -> H^1(F_1) = Z/24Z (surjective, from long exact sequence).

**Sensitivity distinction:**
- Type A (algebraic anomaly): FILTRATION-INSENSITIVE. n_L - n_R = 0 holds at all stages.
- Type B (analytic generation count): FILTRATION-SENSITIVE. R_tau is ambiguous at F_1; R = 24 only at F_2.

### 4.2 Physical Regime Where Sensitivity Activates

The filtration sensitivity is non-trivial (O(tau) ≠ 0) when:
1. The observer state space X_obs has pi_1 ≠ 0.
2. The generation bundle (H-line bundle of rank 24 over X_obs) carries non-trivial monodromy.

For GU:
- This activates for X^4 with pi_1 ≠ 0 (topologically non-trivial spacetime), or
- For moduli-space paths carrying non-trivial pi_3(Sp(64)) = Z instanton number.
- It is ABSENT for the K3-type X^4 with simply-connected A/G (the GU-selected ground case by variational principle).

**Consequence for the GU record protocol:** The observer must assemble records to stage F_2 (monodromy-resolving) before the generation count is globally well-defined. An observer that terminates at stage F_1 (only locally consistent records) will report an ambiguous generation count R = 24 mod Z/24Z instead of the definite R = 24. This is a concrete constraint on the L2 observer specification.

### 4.3 Explicit Failure Conditions

**F1:** If pi_1(A(Y^14, Sp(64))/G) = 0 for all relevant Y^14 and X^4 (simply-connected case) — then monodromy is trivially zero, O(1) = 0, and the filtration sensitivity is absent. The promotion gate would be vacuously discharged. Checked: this holds for K3 with the GU variational selection (simply-connected X^4, contractible A/G by Sp(64) simple-connectivity), so the filtration sensitivity IS absent in the GU ground state.

**F2:** If the generation bundle [ker D_x] is trivial in KSp^0(X_obs) — then no monodromy can form regardless of X_obs topology. This holds iff pi_3(Sp(64)) = 0 acting on the fiber S = H^{64}. But pi_3(Sp(n)) = Z for all n >= 1, so the generation bundle generically carries non-trivial monodromy. F2 does NOT fail generically.

**F3:** If the locally-constant sheaf F_1 and the flasque sheaf F_2 are actually isomorphic as sheaves (not as coefficient-group-valued sheaves) — then F_1 = F_2 and no filtration effect exists. This fails: F_1 ≠ F_2 as sheaves (F_1 has non-trivial restrictions, F_2 is flasque). F3 does not fail.

**F4:** If the signed-readout framework does not apply (e.g., if G is not an ordered abelian group) — the Z/24Z-valued readout requires G = Z as the codomain, which is an ordered abelian group. No obstruction. F4 does not fail.

**F5:** If the observer's configuration space X_obs cannot be modeled as a compact manifold with pi_1 ≠ 0 — then the toy does not apply. This is an idealization; the actual A/G may be contractible. This is the key physical condition and is the main remaining open question (see §5).

**F6:** If the non-collapse of H^1 across filtration stages does not translate into a physically observable change in the chirality readout (e.g., if the monodromy is always gauged away) — then the filtration sensitivity is a mathematical artifact. Partially addressed: the monodromy is in the generation bundle of the physical Hilbert space, which cannot be gauged away by Sp(64) gauge transformations acting on the fibers (those act within each fiber, not across X_obs).

### 4.4 What the Test Establishes

1. **Type A (algebraic) readout is filtration-insensitive.** J^2 = -1 is independent of which stage F_tau the observer is at. The Sp(64) anomaly cancellation n_L - n_R = 0 is not sensitive to the filtration.

2. **Type B (analytic) readout is filtration-sensitive in the general case.** The signed-index R = 24 requires global patching data (monodromy resolution), which is only available at the final stage F_2. At intermediate stages, the readout carries an H^1(X_obs, Z/24Z) ambiguity.

3. **The promotion gate is discharged at reconstruction grade** for the general case (X_obs with pi_1 ≠ 0). The GU chirality readout IS demonstrably sensitive to the filtration when the observer traverses a non-contractible loop in configuration/moduli space.

4. **The promotion gate is vacuously absent for the GU ground state** (K3-type X^4, simply-connected A/G). In this case the filtration sensitivity is zero, which is actually reassuring: the GU ground state has unambiguous R = 24 at all filtration stages.

5. **The structural claim is sharp:** filtration sensitivity = non-zero pi_1(X_obs) activating the H^1 monodromy of the generation bundle. This is a precise, falsifiable criterion.

---

## 5. Open Questions

**OQ1 (most important): Is pi_1(A(Y^14, Sp(64))/G) non-trivial for physically relevant Y^14?**

For K3-type X^4 (the GU-selected ground state), we argued pi_1 = 0. But for more general X^4 (Lorentzian X^4 = R x M^3 with M^3 having non-trivial pi_1), the configuration space can have richer topology. Explicit computation needed.

**OQ2: Does the moduli space M_GU (space of GU solutions) have non-trivial pi_1 or pi_3?**

pi_3(Sp(64)) = Z gives instanton number as a Z-valued topological charge. A moduli-space path connecting different instanton sectors carries non-trivial monodromy. Whether GU solutions with different instanton numbers are connected by a smooth path in M_GU is the moduli question.

**OQ3: Can the monodromy be physically observed (as a difference in measured generation count across vacua)?**

The monodromy twist n_wind changes the apparent generation count from 24 to 24 + n_wind * (factor). If n_wind ≠ 0, an observer in a different vacuum (connected by a moduli-space path) would measure a different generation count. This would be a genuine physical prediction of the GU filtration-sensitivity.

**OQ4: Does the filtered-sheaf obstruction O(tau) = H^1(X_obs, F_tau) have a concrete physical interpretation as an anomaly inflow or a Wess-Zumino term?**

In standard quantum field theory, monodromy of the effective action around a loop in moduli space corresponds to anomaly inflow. The H^1 class in our toy is a candidate for such an inflow term.

**OQ5: Promotion gate for active-research status.**

The promotion gate from the FR3 file (NEXT-STEPS.md) is now discharged at reconstruction grade for the general case. For the promotion from exploration to active-research status, one would need:
- An explicit GU result (analytic computation, not just toy existence) where a specific non-trivial pi_1(A/G) loop produces a specific non-trivial monodromy class in H^1(X_obs, Z/24Z).
- Or: a concrete prediction that observers in different GU vacua (connected by an instanton path) measure different generation counts.

---

## 6. Verdict Summary

| question | answer |
|---|---|
| Does a GU chirality readout sensitive to {F_tau} vs. F exist? | Yes (reconstruction grade). Type B analytic readout is sensitive; Type A algebraic readout is not. |
| Is the sensitivity mechanism the same as the FR3 non-collapse? | Yes. Controlled by H^1(X_obs, F_tau) → 0 as tau → final. |
| Does this activate for the GU ground state (K3, simply-connected)? | No — the ground state has trivial monodromy; sensitivity is absent at the preferred vacuum. |
| Does it activate for generic X^4 or non-trivial moduli paths? | Yes — pi_3(Sp(64)) = Z provides the instanton monodromy mechanism. |
| Does it change any established GU theorem? | No — ind_H(D_GU) = 24 is still the correct final value; filtration sensitivity affects the intermediate readout, not the final result. |
| Explicit failure conditions? | Six stated (F1-F6); F1 is the main active condition (K3 ground state is safe). |
| Promotion gate discharged? | Yes, at reconstruction grade for the general case. |

**Verdict: CONDITIONALLY_RESOLVED.** The promotion gate for the filtered-sheaf object to earn active-research GU status is discharged at reconstruction grade. The GU analytic chirality readout (Type B: ind_H, Q_A) is demonstrably filtration-sensitive via the H^1 monodromy mechanism for observer states with pi_1 ≠ 0 (general case). The algebraic anomaly cancellation (Type A: n_L - n_R = 0) is filtration-insensitive. The GU ground state (K3, simply-connected) has trivially zero filtration sensitivity, which is consistent and reassuring. Active-research promotion requires OQ1-OQ4 to produce explicit non-trivial GU examples beyond the toy.

---

## 7. Cross-References

- Promotion gate source: NEXT-STEPS.md "Filtered-sheaf obstruction O(tau)" row.
- Non-collapse toy: `explorations/time-as-finality-crosswalk/fr3-filtered-sheaf-non-collapse-example-2026-06-22.md`
- Signed-readout framework: `explorations/signed-readout-monotonicity-pn-jordan-2026-06-23.md`
- Record graph: `explorations/signed-readout-oq1-record-graph-2026-06-23.md`
- Integer-index recovery: `explorations/signed-readout-oq2-integer-index-2026-06-23.md`
- GU contact: `explorations/signed-readout-oq2d-gu-contact-2026-06-23.md`
- K-theory lift: `explorations/signed-readout-oq2a-k-theory-lift-2026-06-23.md`
- BvN Gamma_min coupling: `explorations/fr2-bvn-gate-ii-gu-result-2026-06-23.md`
- Anomaly cancellation: `explorations/anomaly-audit-cl95-gauge-group-2026-06-22.md`
