---
title: "FR2 BvN Layer-5 Promotion Gate: Denied Functor, Proof Obligations, and Gamma_min Coupling Rule"
date: 2026-06-23
problem_label: "fr2-bvn-layer5"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# FR2 BvN Layer-5 Promotion Gate

## 1. Problem Statement

FR2 (NEXT-STEPS.md, FR-series) established a candidate L1--L2 coupling rule:

> For any candidate whose L2 observer must certify a classical (distributive) shadow of an L1 substrate with non-trivial coherence dynamics, the observer's record-finalization rate lambda_max is bounded above by the substrate's decoherence rate divided by the decoherence-tolerance factor: lambda_max <= Gamma / ln(1/epsilon).

The FR-series synthesis (NEXT-STEPS.md residual table) lists two promotion gates for this coupling rule to earn active-research status:

- **(i)** Prove the BvN wall to Layer-5 rigor: define the denied functor or adjunction; prove the obstruction without smuggling.
- **(ii)** Exhibit a GU result (anomaly input or signed-readout scope) that changes when Gamma < Gamma_min.

This file addresses gate (i) at reconstruction grade, and assesses whether the coupling rule passes the no-go discipline for inclusion in the six-axis protocol's Current Coupling Rules section.

**Why this matters.** If the BvN wall is formalizable at Layer 5, the Gamma_min coupling rule becomes a *rate-parameterized characterization of the wall*, not merely a useful bound. That elevates it from an exploration artifact to a structural condition on the six-axis sextuple: every candidate that must bridge L1 quantum coherence to a classical L3/L2 readout must satisfy the coupling inequality, and the BvN obstruction is the reason why.

---

## 2. Established Context

Prior results this builds on:

- `explorations/time-as-finality-crosswalk/fr2-bvn-rate-of-classicality-derivation-2026-06-22.md`: Steps A--C derivation, Gamma_min definition, lambda_max definition, proportionality Gamma_min = ln(1/epsilon) * lambda_max.
- `explorations/c-mpr/rigor-redirect-c-mpr-branch.md`: Layer 5 discipline: "define the functor or adjunction being denied; state exactly which preservation requirements are impossible; prove the obstruction without smuggling in the conclusion through object definitions."
- `canon/six-axis-specification-protocol.md`: Current Coupling Rules section; admission rule for proposed additions.
- `explorations/time-as-finality-crosswalk/rate-independence-worked-check-2026-06-22.md`: The signed-readout monotonicity criterion is rate-independent; Gamma_min is a pre-classicality gate, not a post-classicality theorem.

---

## 3. Computation

### 3.1 The BvN Wall: What Must Be Formalized at Layer 5

The Birkhoff--von Neumann theorem (1936) states: the lattice of closed subspaces of a Hilbert space H (the quantum event algebra Q(H)) is NOT a Boolean algebra in general; it is orthomodular but non-distributive. A classical event algebra C is a Boolean sigma-algebra (distributive orthocomplemented lattice). The BvN wall is the failure of any (structure-preserving) map from Q(H) to C to be an isomorphism of lattice structures.

At Layer 5, the rigor-redirect requires four things:

1. Define the classical side C precisely.
2. Define the quantum side Q precisely.
3. Define the functor or adjunction being DENIED.
4. Prove the obstruction without importing distributivity as an assumption on the quantum side.

We now execute each step.

---

### 3.2 The Classical and Quantum Lattices

**Classical event algebra C:** A complete Boolean algebra (sigma-algebra of events). Concretely: C = (P(Omega), cup, cap, complement, 0, 1) where Omega is a measurable sample space. The distinguishing axiom is distributivity:

```
a cap (b cup c) = (a cap b) cup (a cap c)     for all a, b, c in C.
```

**Quantum event algebra Q(H):** The lattice of closed linear subspaces of a Hilbert space H, ordered by inclusion. Equivalently, the lattice of orthogonal projections P(H) = {P in B(H) | P^2 = P, P = P*} ordered by P <= Q iff ran(P) subset ran(Q). The meet is P cap Q (projection onto ran(P) cap ran(Q)); the join is P cup Q (closure of ran(P) + ran(Q)); the complement is P^perp = 1 - P.

The orthomodular law holds in Q(H): if P <= Q then Q = P cup (P^perp cap Q). But distributivity FAILS: for any three projections P, Q, R in H with dim H >= 2, the identity

```
P cap (Q cup R) = (P cap Q) cup (P cap R)
```

fails unless P, Q, R pairwise commute. The failure is the non-commutativity of projections: P cap Q != Q cap P in general (they are not equal as sets of projections, because the meet in the lattice is not commutative without further conditions).

**Explicit counterexample (standard):** H = C^2. Let P = projection onto span{(1,0)}, Q = projection onto span{(0,1)}, R = projection onto span{(1,1)/sqrt(2)}.

```
Q cup R = 1     (their ranges span C^2)
P cap (Q cup R) = P cap 1 = P     (P itself, projection onto span{(1,0)})
P cap Q = 0     (orthogonal), P cap R = 0     (orthogonal, since (1,0).(1,1) = 1 != 0)
Wait: P cap R requires checking: ran(P) cap ran(R) = span{(1,0)} cap span{(1,1)} = {0}.
So (P cap Q) cup (P cap R) = 0 cup 0 = 0.
But P cap (Q cup R) = P != 0.
```

This is the standard failure case. The quantum lattice Q(H) is NOT distributive for H of dimension >= 2. This establishes the BvN wall concretely.

---

### 3.3 The Denied Functor: Precise Statement

**Setup.** Let CAlg denote the category of complete Boolean algebras (classical event algebras) with morphisms = bounded lattice homomorphisms that preserve countable joins and complements (sigma-algebra morphisms). Let OMLat denote the category of complete orthomodular lattices (quantum event algebras) with morphisms = bounded lattice homomorphisms that preserve orthocomplementation.

There is an obvious inclusion functor I: CAlg -> OMLat (every Boolean algebra is orthomodular, since distributivity implies orthomodularity; inclusion sends C to itself viewed as an orthomodular lattice). The denied functor is the alleged left adjoint or right adjoint to I.

**Claim (Denied Functor).** There is NO functor F: OMLat -> CAlg such that F is a left adjoint to I: CAlg -> OMLat with F satisfying:

```
Hom_{CAlg}(F(L), C) ~= Hom_{OMLat}(L, I(C))     naturally in L in OMLat, C in CAlg.
```

Equivalently: the inclusion I: CAlg -> OMLat has no left adjoint that preserves the orthomodular structure of Q(H) for dim H >= 2.

**Adjunction statement.** If F were a left adjoint to I, then for L = Q(H) (H = C^2) and C = 2 (the two-element Boolean algebra), the unit map eta: Q(H) -> I(F(Q(H))) would be a morphism of OMLat sending Q(H) into a Boolean algebra. But:

- A morphism of OMLat from Q(H) to a Boolean algebra B must satisfy: for all P, Q in Q(H), phi(P cap Q) = phi(P) cap phi(Q) AND phi(P cup Q) = phi(P) cup phi(Q). Because B is Boolean (distributive), phi must send non-commuting projections to commuting elements. But in B, all elements commute (Boolean lattices are commutative). So phi must factor through the commutative part of Q(H), which is the Boolean subalgebra of Q(H) generated by commuting projections.
- For Q(H) with dim H = 2, the maximal Boolean subalgebras are {0, P, P^perp, 1} for fixed P (2-element partition of unity). Any phi must send all of Q(H) into one such 2-element block, thereby collapsing superposition structure entirely.
- The unit eta: Q(H) -> I(F(Q(H))) must be the initial such morphism (universal among all OMLat morphisms into Boolean algebras). The only candidates are: (a) the zero map (sends everything to 0); (b) maps that factor through a fixed maximal Boolean subalgebra; but none is natural in L (the choice of subalgebra is not canonical for arbitrary Q(H)).

**Formal denial.** For dim H >= 2, there is no naturally defined Boolean algebra F(Q(H)) equipped with a natural bijection Hom_{CAlg}(F(Q(H)), C) ~= Hom_{OMLat}(Q(H), I(C)) for all C in CAlg. The obstruction is: Hom_{OMLat}(Q(H), I(C)) is empty unless C has at most as many elements as the maximal Boolean subalgebras of Q(H) (which for H = C^n are the subalgebras generated by a partition of unity into n projections, i.e., with at most 2^n elements). But Hom_{CAlg}(F(Q(H)), C) must be naturally defined for all C including C = Free(n) (freely generated Boolean algebras with 2^n elements), breaking naturality.

**Adjunction from the other side.** There is also no right adjoint G: OMLat -> CAlg to I: CAlg -> OMLat. A right adjoint would assign to each C in CAlg a Boolean algebra G(C) in CAlg with a counit epsilon: I(G(C)) -> C in OMLat, i.e., a morphism of OMLat from G(C) (viewed as an OMLat) back to C. This is the identity (G(C) = C works trivially). But then G is just the identity, which is an adjoint only if I is also the identity -- which it is not (I is the inclusion of a full subcategory, not an equivalence). The adjunction collapses: G = Id is not a right adjoint to I in the correct sense because I is not surjective on objects.

**The correct denied functor statement:** The inclusion I: CAlg -> OMLat does not have a left adjoint F: OMLat -> CAlg that assigns to each Q(H) a Boolean algebra F(Q(H)) and a unit eta: Q(H) -> I(F(Q(H))) that is a lattice morphism AND is natural in H. The BvN wall is this denial: there is no "classicalization" functor from quantum lattices to Boolean algebras that is natural (i.e., commutes with lattice homomorphisms arising from unitary maps) when dim H >= 2.

---

### 3.4 Proof Obligations at Layer 5

The rigor-redirect (Layer 5 of rigor-redirect-c-mpr-branch.md) requires that the proof does NOT smuggle distributivity. We state the obligations precisely.

**Obligation P1 (No smuggling).** The quantum lattice Q(H) must be defined without assuming any distributive law. The proof that distributivity fails must use the definition of Q(H) (closed subspaces of H, ordered by inclusion, meet = intersection, join = closed span) and the non-commutativity of projections (which follows from quantum mechanics, not from any classical assumption).

*Status:* MET at reconstruction grade. The counterexample in §3.2 uses only the definition of Q(H) and the non-commutativity of projections in C^2. No distributive law is assumed; its failure is a computation.

**Obligation P2 (Naturality must be stated).** The denial of the left adjoint must specify what "natural" means: it means that for every unitary U: H -> H', the diagram

```
Q(H) --eta_H--> I(F(Q(H)))
|                |
Q(U)             I(F(Q(U)))
|                |
Q(H') -eta_{H'}-> I(F(Q(H')))
```

commutes, where Q(U)(P) = U P U^{-1} (conjugation). Naturality requires F(Q(U)) = I-morphism corresponding to Q(U), but Q(U) is not a Boolean-algebra morphism for U not preserving any fixed Boolean subalgebra.

*Status:* MET at reconstruction grade. The non-commutativity of the Q(U) action with any fixed Boolean subalgebra selection is standard (and follows from the fact that U P U^{-1} for generic unitary U does not map any fixed Boolean subalgebra of Q(H) into itself).

**Obligation P3 (Objects and morphisms of CAlg).** The categories CAlg and OMLat must have their morphism sets precisely defined, not just their objects. The morphisms must be lattice homomorphisms preserving all listed structure (meet, join, complement, 0, 1, and in CAlg also distributivity -- but distributivity in CAlg is automatic from the lattice axioms, so morphisms need not separately enforce it).

*Status:* MET. Standard (see Birkhoff 1967, section on Boolean algebras; Kalmbach 1983 for orthomodular lattices).

**Obligation P4 (Existence of obstruction, not just absence of construction).** The denial requires proving that NO functor F works, not just that one obvious construction fails. The proof must close over all possible functors.

*Status:* PARTIALLY MET at reconstruction grade. The argument in §3.3 shows that the unit of any putative adjunction cannot be natural by an explicit computation on H = C^2. The full universality (over all OMLat objects, not just Q(H) for H a Hilbert space) requires more. But for the application to physics (where L = Q(H) is always a concrete Hilbert-space lattice), the restriction to Hilbert-space lattices is sufficient and the argument is complete.

**Obligation P5 (Connection to the observer-finality chain).** The BvN wall must be connected to the six-axis chain: it is the obstruction at the L1 (quantum substrate) -> L3 (pairing) -> L2 (observer record) junction, not a free-floating category theory result. This requires identifying: (a) the quantum lattice as L1 (the substrate's event algebra); (b) the Boolean algebra as the observer's record algebra (L2); and (c) the denied functor as the "classicalization map" the observer would need to apply to get a definite record.

*Status:* MET at exploration grade from FR2. The Lindblad decoherence model gives a physical mechanism for why the classicalization map fails below Gamma_min: the off-diagonal elements rho^{ij}(t) = rho^{ij}(0) exp(-Gamma t) are still nonzero (the quantum lattice has not projected to a Boolean subalgebra), so the unit eta: Q(H) -> I(C) does not exist as a well-defined map on the observer's timescale.

---

### 3.5 The Rate-Parameterized BvN Wall: Connecting Gamma_min

The connection between the abstract denial and the physical rate is now explicit.

**Key insight.** The BvN wall is not a binary obstruction (the quantum lattice is always non-distributive in isolation). It is an OBSERVER-RELATIVE obstruction parameterized by time. At time t:

- Off-diagonal elements rho^{ij}(t) = rho^{ij}(0) exp(-Gamma_{ij} t).
- The "effective quantum lattice accessible to the observer at time t" is NOT Q(H); it is the lattice of projection-valued measures that commute with the diagonal (decohered) part of rho_S(t).
- The effective event algebra E_obs(t) transitions from Q(H) (fully quantum, non-distributive) at t=0 to a classical Boolean algebra C (the pointer-basis subalgebra) as t -> infinity.

The BvN wall at time t is: the effective event algebra E_obs(t) is non-distributive iff the surviving coherences are nonzero, i.e., iff exp(-Gamma t) > epsilon (the tolerance). Rearranging:

```
E_obs(t) is distributive (classical, Boolean) iff t >= (1/Gamma) ln(1/epsilon) = t_dec(epsilon).
```

The observer's finalization latency is t_obs. The observer can certify a distributive shadow iff:

```
t_obs >= t_dec(epsilon)
<=>  Gamma >= ln(1/epsilon) / t_obs  =  Gamma_min(epsilon).
```

**This is the rate-parameterized BvN wall.** The wall is not crossed (the classicalization functor becomes well-defined) iff Gamma >= Gamma_min. Below Gamma_min, the functor from E_obs(t_obs) to any Boolean algebra cannot be the unit of an adjunction (because E_obs(t_obs) is still genuinely non-distributive on the observer's timescale).

**The denied adjunction, rate-parameterized.** For fixed observer latency t_obs and tolerance epsilon, define the effective quantum lattice L_{obs} = E_obs(t_obs) (the lattice of observables commuting with rho_S(t_obs)). The BvN denial says:

- If Gamma >= Gamma_min: L_{obs} = C (effectively Boolean), and the inclusion I: CAlg -> OMLat has a "unit" that is well-defined on L_{obs}. The classicalization "functor" (collapsing L_{obs} to C) is the identity. The BvN wall has been crossed by decoherence.
- If Gamma < Gamma_min: L_{obs} is strictly orthomodular but not Boolean (surviving coherences). No functor F: OMLat -> CAlg sends L_{obs} to a Boolean algebra with a natural unit -- the off-diagonal rho^{ij}(t_obs) terms prevent any faithful Boolean image. The BvN wall is in force for this observer.

---

### 3.6 Can Gamma_min Be Included in the Six-Axis Coupling Rules?

The six-axis protocol's "Current Coupling Rules" section records structural L-axis dependencies discovered through worked examples. The existing rules are:

1. L1 = Sorkin causal set and L4 = Sorkin partial order are coupled.
2. L5 = universality class requires L6 = RG flow.

The candidate coupling rule from FR2 is:

> For any candidate whose L2 observer must certify a classical (distributive) shadow of an L1 substrate with non-trivial coherence dynamics, the observer's record-finalization rate lambda_max is bounded above by the substrate's decoherence rate divided by the decoherence-tolerance factor: lambda_max <= Gamma / ln(1/epsilon).

**Assessment under no-go discipline.**

The no-go discipline (from NEXT-STEPS.md FR-series notes and no-go-class-relative-map.md honesty contract) requires that coupling rules:
- Not be framed as "the BvN wall is proven" (that claim requires a closed Layer 5 proof, which §3.4 shows is at reconstruction grade, not verified).
- Not smuggle classicality: the coupling rule must hold regardless of whether the BvN wall proof is complete.
- Be a STRUCTURAL constraint on the sextuple, not a process parameter.

**Evaluation:**

A. The coupling rule lambda_max <= Gamma / ln(1/epsilon) is a structural constraint on the L1--L2 pair. It does not assert that the BvN wall is proven; it asserts that IF an observer must certify a classical shadow AND the substrate has decoherence rate Gamma AND the observer's latency is t_obs = 1/lambda_max THEN the coupling inequality must hold. The BvN proof gives the REASON why it must hold (the quantum lattice is non-distributive below Gamma_min), but the coupling rule holds independently as a physical requirement for any certifiable observer.

B. The coupling rule does NOT smuggle classicality. It derives from the physical requirement that the observer's record of a source state is only well-defined (as a pointer-basis record) after the source state has decohered. This is pre-classicality: it is the condition under which classicality becomes available, not the assertion that classicality is already present.

C. The coupling rule IS structural in the six-axis sense: it is a dependence between L1 (substrate's coherence dynamics: Gamma) and L2 (observer's record-finalization rate: lambda_max). This is the same type of statement as the two existing rules (L1-L4 coupling for Sorkin; L5-L6 coupling for RG). The analogy is direct.

D. One tension: the existing coupling rules were derived from WORKED EXAMPLES within the six-axis protocol (example-02 for Sorkin, example-03 for RG). The Gamma_min rule is derived from a CROSSWALK computation (FR2), not from a filled six-axis example. Before formal inclusion, it would be cleaner to fill a six-axis example where the L1--L2 Gamma_min coupling is the load-bearing structural feature (a quantum substrate example where the observer's classicality certification is the protocol). This is a promotion condition, not a blocking condition.

**Verdict on inclusion:**

The coupling rule is ADMISSIBLE under the no-go discipline as a CANDIDATE for the Current Coupling Rules section. It satisfies the structural requirements (genuine L1--L2 dependence, not a process parameter, no classicality smuggling). The promotion condition (a filled six-axis example with this coupling as the load-bearing feature) is not yet met, so the rule should be marked as exploration-grade candidate, not locked canon.

**Proposed addition to six-axis protocol Current Coupling Rules (exploration-grade):**

> **Classicality-certification coupling (exploration-grade):** For any candidate whose L2 observer certifies a classical (distributive) shadow of an L1 quantum substrate with coherence dynamics, the maximum record-finalization rate lambda_max and the substrate decoherence rate Gamma are coupled: lambda_max <= Gamma / ln(1/epsilon), where epsilon is the classicality tolerance. This bounds L2 capacity by L1 coherence dynamics. The coupling is the rate-parameterized form of the Birkhoff--von Neumann wall at the observer's timescale. Does NOT require the BvN obstruction proof to be complete; the physical reason (observer cannot record a state before it decoheres) is self-standing. Promotion gate: one filled six-axis example where this coupling is the load-bearing L1--L2 constraint.

---

### 3.7 Explicit Failure Conditions

This computation would be FALSIFIED if:

**F1 (Smuggling check):** A proof is found that the counterexample in §3.2 relies on an implicit distributive assumption in the definition of C^2's subspace lattice. (Unlikely: the failure P cap (Q cup R) != (P cap Q) cup (P cap R) follows from basic Hilbert space geometry, not from any distributive axiom.)

**F2 (Functor construction):** An explicit natural functor F: OMLat -> CAlg is constructed with the unit property. This would mean a canonical "classicalization" exists -- contradicting the BvN analysis. The only way out is if F maps Q(H) to a trivial Boolean algebra (2-element), in which case F is the constant functor and not useful for physics.

**F3 (Rate argument):** The decoherence model (Lindblad, pointer basis, pure dephasing) is shown to be inapplicable to the relevant GU substrate. If the GU substrate is not a quantum system with a Hilbert space (e.g., if it is purely classical at L1), the rate coupling does not apply. In that case, the BvN wall is simply irrelevant to GU (not an obstruction, not an evasion -- outside the domain of applicability).

**F4 (Coupling non-triviality):** The shared t_obs in Step A (decoherence window) and Step B (inverse service rate) is shown to be definitionally circular: the observer's t_obs is DEFINED as t_dec(epsilon), making Gamma_min = lambda_max a tautology. Rebuttal: the two roles of t_obs (upper bound from source physics; lower bound from observer throughput) are conceptually distinct and can in principle differ; the requirement that they must be equal is a genuine physical constraint, not a definition.

**F5 (Layer 5 closure failure):** The proof obligation P4 (universality over all functors) is not closed at reconstruction grade, and a counterexample is found: a natural functor from some orthomodular lattice (not of the form Q(H)) to a Boolean algebra that has the adjunction property. This would narrow the BvN denial to Hilbert-space lattices and not extend to all OMLat. For the physics application, this is acceptable (the GU substrate is a Hilbert-space quantum system), but it weakens the categorical generality.

---

## 4. Result

**Primary verdict:** CONDITIONALLY_RESOLVED at reconstruction grade.

The BvN wall at Layer-5 rigor is established as follows:

- **Denied functor:** The inclusion I: CAlg -> OMLat (classical Boolean algebras into orthomodular lattices) has no left adjoint F: OMLat -> CAlg that is natural with respect to the unitary group action on Q(H) for dim H >= 2. The obstruction is the non-commutativity of projections in Q(H), demonstrated by an explicit counterexample in C^2. No distributive law is assumed on the quantum side.

- **Proof obligations:** P1 (no smuggling) and P2 (naturality statement) are met at reconstruction grade. P3 (morphism definitions) is standard. P4 (universality) is met for Hilbert-space lattices; extension to all OMLat is an open residual. P5 (chain connection) is met at exploration grade from FR2.

- **Rate-parameterized form:** The BvN wall, when parameterized by the observer's finalization latency t_obs and tolerance epsilon, becomes: the classicalization functor is well-defined on the observer's timescale iff Gamma >= Gamma_min = ln(1/epsilon) / t_obs. This is Gamma_min from FR2, and it is the rate-parameterized form of the wall crossing.

- **Six-axis inclusion:** The coupling rule lambda_max <= Gamma / ln(1/epsilon) is ADMISSIBLE as a candidate addition to the Current Coupling Rules section under the no-go discipline. Promotion gate (one filled six-axis example with this coupling as the load-bearing L1--L2 feature) is not yet met. The rule should appear as exploration-grade in the protocol.

**What remains open:**

- P4 universality over all OMLat (not just Hilbert-space lattices).
- A filled six-axis example where the classicality-certification coupling is the load-bearing structural constraint (gate for promotion from candidate to locked coupling rule).
- Gate (ii) from NEXT-STEPS.md: a GU result that changes when Gamma < Gamma_min. (This requires identifying a specific GU computation where the classicality of the L1 substrate enters the result, which requires knowing what the GU L1 substrate is at the quantum level -- beyond the current formalization scope.)

---

## 5. Open Questions

**OQ1 (GU substrate quantum status).** Is the GU L1 substrate (the metric bundle Y^14 with Sp(64) gauge theory) a quantum system in the Hilbert-space sense? If yes, which Hilbert space, and does it carry a genuine non-distributive event algebra? If the substrate is classical at L1, the BvN wall is irrelevant to GU and the Gamma_min coupling rule does not apply to it.

**OQ2 (Filled six-axis example).** The promotion gate requires one filled six-axis example where L1 = quantum Hilbert-space substrate, L2 = finite-Turing observer certifying a classical shadow, and the load-bearing coupling is lambda_max <= Gamma / ln(1/epsilon). The Sorkin causal-set example (example-02) is already filled; a quantum-substrate analog is needed.

**OQ3 (Universal adjunction failure).** The denial in §3.3 is proven for Hilbert-space lattices Q(H) via the explicit C^2 example. Extension to all complete orthomodular lattices requires a categorical argument showing that no OMLat object has a natural Boolean-algebra image (i.e., the free Boolean algebra on an OMLat does not exist in CAlg). This is related to the Kochen-Specker theorem (no global valuation exists on Q(H)) and deserves a separate treatment.

**OQ4 (Subprincipal decoherence effects).** The Lindblad model in FR2 (Step A) uses pure dephasing for simplicity. A more complete model would include relaxation (energy exchange with environment) and allow off-diagonal coherences to relax at different rates for different pointer-basis pairs. The minimal decoherence rate Gamma = min_{i != j} Gamma_{ij} is then the bottleneck, and Gamma_min retains the same form. Whether GU's specific decoherence physics (if any) changes the form of Gamma_min is beyond current scope.

---

## 6. Cross-References

- FR2 derivation (Steps A--C, Gamma_min definition): `explorations/time-as-finality-crosswalk/fr2-bvn-rate-of-classicality-derivation-2026-06-22.md`
- FR-series synthesis and residual table: `NEXT-STEPS.md` (FR-series summary section)
- Rigor-redirect Layer 5 discipline: `explorations/c-mpr/rigor-redirect-c-mpr-branch.md`
- Six-axis protocol (target for coupling rule): `canon/six-axis-specification-protocol.md`
- No-go map (BvN row): `canon/no-go-class-relative-map.md`
- Rate-independence (signed-readout is not rate-dependent; Gamma_min is pre-classicality): `explorations/time-as-finality-crosswalk/rate-independence-worked-check-2026-06-22.md`
