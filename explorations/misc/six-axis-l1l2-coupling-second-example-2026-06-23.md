---
title: "Six-Axis Candidate: Sorkin Causal-Set Observer with FR2 Gamma_min Coupling Rule (Second Filled Row)"
date: 2026-06-23
problem_label: "six-axis-l1l2-coupling-second-filled-row"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Six-Axis Candidate: Sorkin Causal-Set Observer with FR2 Gamma_min Coupling Rule

**Purpose.** This document fills a second complete six-axis candidate specification row for
the FR2 Gamma_min coupling rule:

```
lambda_max <= Gamma / ln(1/epsilon)
```

equivalently: any observer that finalizes records of a substrate at rate `lambda_max` while
tolerating decoherence error `epsilon` requires substrate coherence lifetime at least
`1/lambda_max * ln(1/epsilon)`.

The L1 substrate is physically distinct from the first filled example
(`six-axis-l1l2-coupling-filled-example-2026-06-23.md`, which used the BvN/decoherence model
on Y^14 = Met(X^4)). Here the L1 substrate is the **Sorkin causal-set observer** from FR1
(`explorations/time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md`):
a locally finite partially ordered set (C, prec) whose elements carry quantum amplitudes
subject to coherence decay.

The promotion condition for the FR2 Gamma_min coupling rule to active-research status
requires a second filled six-axis example with the coupling rule as the load-bearing
L1-L2 constraint. This document supplies that second example.

---

## Acceptance Summary (One-Line Table)

| candidate | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 loop | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sorkin-CS-Gamma-coupling | Locally finite poset (C, prec) whose elements carry quantum amplitudes; each element x has coherence lifetime tau_coh(x) = 1/(decoherence rate Gamma_x); the substrate IS the causal order (Sorkin L1-L4 coupling) | Finite Turing observer O with accessible past P(O), finalization latency t_obs per record, and decoherence tolerance epsilon (max off-diagonal amplitude allowed at time of record finalization) | Causal-completeness-plus-classicality pairing: O finalizes record of x when (a) J^-(x) cap P(O) is order-complete AND (b) the quantum amplitude of x has decohered to within epsilon; the conjunction gates on Gamma >= lambda_max * ln(1/epsilon) = Gamma_min(lambda_max, epsilon) | Sorkin causal-set partial order: prec on (C, prec) is the causal order; L1 and L4 are coupled (the substrate IS the causal order) | Specific-object substrate: a particular (C, prec) with element-wise coherence rates Gamma_x | Completeness-gated cadence loop (class (g)): O's finalization rate lambda_max is bounded by Gamma / ln(1/epsilon) from above; the cadence Delta in the record-finalization protocol is set to max(t_obs, ln(1/epsilon)/Gamma) to avoid premature commitment | If a Sorkin causal-set observer can be constructed that finalizes records at lambda_max > Gamma / ln(1/epsilon) without triggering decoherence-error exceedance (off-diagonal elements above epsilon at finalization time), the coupling bound is falsified |

---

## Setup: The Causal-Set with Quantum Amplitudes

### Substrate Enrichment over the FR1 Example

The FR1 worked check (`fr1-sorkin-absorption-worked-check-2026-06-22.md`) used the
standard Sorkin causal-set (C, prec) with **classical** records: the invariants extracted
from each element x (chain abundances, interval counts) were classical combinatorial quantities.
The resulting lambda_max was absorbed by L4+L2 with no L1-L2 coupling rule because the
causal order is rate-blind and the observer's classicality of the extracted invariants was
automatic.

The present candidate adds a **quantum amplitude layer** to the causal-set elements:

**Definition (quantum causal set).** A quantum causal set (C, prec, psi) is a locally
finite poset (C, prec) together with an assignment psi: C -> H where H is a Hilbert space
(taken to be finite-dimensional per element for simplicity) and each element x carries a
density matrix rho_x (t) = psi_x(t) psi_x(t)^dagger evolving under Lindblad dynamics:

```
d rho_x / dt = -i [H_x, rho_x] + sum_k (L_k rho_x L_k^dagger - 1/2 {L_k^dagger L_k, rho_x})
```

The Lindblad operators L_k drive rho_x toward pointer-basis eigenstates at rate Gamma_x
(the decoherence rate of element x). In the simple scalar case, the off-diagonal element
satisfies:

```
|rho_x(t)_{off}| <= |rho_x(0)_{off}| * exp(-Gamma_x * t)
```

This is the same decoherence model used in the BvN L1-L2 coupling row
(`observer-section-error-model-2026-06-23.md`), instantiated here at the level of
individual causal-set elements rather than metric fiber coordinates on Y^14.

**Why this is a physically distinct L1 substrate.** The first filled row (BvN/decoherence)
has L1 = smooth principal bundle Y^14 = Met(X^4), with quantum metric fluctuations in the
fiber GL(4,R)/O(3,1). The present row has L1 = locally finite poset (C, prec, psi), with
quantum amplitudes on the combinatorial elements of the poset. These are genuinely different
mathematical objects: Y^14 is a smooth fiber bundle over a 4-manifold; (C, prec, psi) is a
directed graph with a Hilbert-space decoration. The decoherence model appears in both, but
acting on structurally distinct substrates.

---

## Leg 1 — Substrate Class

**Class label:** (k) Sorkin causal-set substrate, enriched: locally finite poset (C, prec)
with quantum amplitude assignment psi: C -> H and element-wise Lindblad decoherence at
rate Gamma (for uniform Gamma_x = Gamma; the general case uses min_x Gamma_x).

**Specification (1-3 sentences):** The substrate is the triple (C, prec, psi) where
(C, prec) is the standard Sorkin causal-set (locally finite, acyclic, irreflexive partial
order) and psi is an assignment of density matrices rho_x (t) to each element x in C,
evolving under Lindblad dynamics with pointer-basis decoherence rate Gamma_x >= Gamma > 0.
The substrate IS the causal order (Sorkin L1-L4 coupling: L4 = d is forced). The
quantum amplitude layer means that the classical invariant of x (its contribution to
chain abundances, interval counts, or any record-readable quantity) is not available
until rho_x has decohered sufficiently: until the off-diagonal elements |rho_x|_{off}
have fallen below the observer's tolerance epsilon. Below the decoherence threshold,
element x presents a quantum superposition of pointer-basis states and the classical
record of x is undefined (the BvN wall fires at the element level: the observer's
event algebra for x is non-distributive until decoherence is complete).

**Literature anchor:** Sorkin causal-set program (Bombelli-Lee-Meyer-Sorkin 1987;
Sorkin "Causal sets: discrete gravity" 2003); FR1 worked check
(`explorations/time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md`);
Lindblad dynamics (Lindblad 1976, "On the generators of quantum dynamical semigroups");
Zurek pointer basis (Zurek 2003, "Decoherence, einselection, and the quantum origins of
the classical"); BvN at element level (`explorations/misc/fr2-bvn-layer5-promotion-gate-2026-06-23.md`,
Section 2 -- the denied functor fires at any individual Hilbert space dim H >= 2, not only
at the metric-fiber level).

**Class-assumption signature broken:** The FR1 worked check (and the standard Sorkin program)
uses a fully classical (C, prec): elements have definite causal-set invariants available
at any time, subject only to the completeness-gating condition (all causal predecessors
present). The present substrate breaks this by adding the quantum amplitude layer: even
when J^-(x) cap P(O) is order-complete, element x's classical record is not available
until Gamma * t_obs >= ln(1/epsilon). The no-go theorems (Witten 1981, Freed-Hopkins,
Distler-Garibaldi) assume classical data in the substrate; they do not model element-level
quantum amplitudes or Lindblad coherence lifetimes. The L1 class-assumption broken is:
"substrate elements present definite classical invariants once causally accessible."

---

## Leg 2 — Observer Class

**Class label:** (d) Snowball / metastable consensus observer — finite, subsampling,
epsilon-bounded, with decoherence rate Gamma and finalization latency t_obs,
instantiated in the causal-set context.

**Specification:** The observer O is a finite-resource agent that reads off classical
invariants from causal-set elements. O has:
- Finalization latency t_obs: the time window available to finalize the record of
  element x once x's causal past J^-(x) cap P(O) is order-complete.
- Decoherence tolerance epsilon: the maximum off-diagonal density-matrix element
  allowed at the time of record finalization (the observer certifies the record of x
  as classical only when |rho_x|_{off} <= epsilon).
- Finalization rate lambda_max: the number of elements finalized per unit time (the
  inverse of t_obs in the rate picture).

The observer's record-finalization protocol has two gates that must both be satisfied
before x's record enters the finalized evidence set X_O:
1. **Causal completeness gate (L4, from FR1):** all elements of J^-(x) are in P(O).
2. **Classicality gate (new, from FR2):** the decoherence of x has reduced
   |rho_x(t_obs)|_{off} to <= epsilon.

The second gate is the new element relative to the FR1 worked check. In FR1, gate 2
did not exist (substrate elements were classical). The addition of gate 2 is what
causes the L1-L2 coupling rule to fire.

**Literature anchor:** BvN classicality gate at observer level (`explorations/misc/fr2-bvn-layer5-promotion-gate-2026-06-23.md`);
Lindblad decoherence observer model (`explorations/time-as-finality-crosswalk/observer-section-error-model-2026-06-23.md`);
FR1 observer (finite Turing, `explorations/time-as-finality-crosswalk/fr1-sorkin-absorption-worked-check-2026-06-22.md`,
Section 2); finalization latency t_obs from TaF FR2 (`explorations/time-as-finality-crosswalk/fr2-bvn-rate-of-classicality-derivation-2026-06-22.md`).

**Class-assumption signature broken:** The FR1 observer is a finite Turing observer with
no classicality certification step (the substrate is already classical; gate 2 is
trivially satisfied). The no-go theorem observers similarly assume classical substrate access
(the invariants of a fixed smooth bundle are available on demand). The present observer
breaks this by requiring the decoherence check as an active step: the observer cannot
read off x's record until the decoherence condition is met. This is the same observation-
class as the BvN-coupling candidate (`six-axis-l1l2-coupling-filled-example-2026-06-23.md`,
Leg 2), here applied to a Sorkin causal-set element rather than a metric fiber.

---

## Leg 3 — Pairing

**Class label:** (f) Metastable-consensus pairing — conjunction of causal completeness
and classicality certification, with quantitative coupling rule Gamma_min = lambda_max * ln(1/epsilon).

**Specification:** The pairing channel has two stages:
1. **Order-completion check (causal):** O checks whether J^-(x) cap P(O) is order-complete
   (the FR1 completeness gate). This is rate-blind: it depends on which elements of C
   are in P(O), not on the finalization rate.
2. **Decoherence check (quantum):** O checks whether |rho_x(t_obs)|_{off} <= epsilon.
   This gate closes only when Gamma * t_obs >= ln(1/epsilon), i.e., when the decoherence
   has had time to drive off-diagonal elements below epsilon within the finalization window.

The coupling rule fires at stage 2. Given finalization latency t_obs = 1/lambda_max, the
classicality gate closes iff:

```
Gamma * (1/lambda_max) >= ln(1/epsilon)
=> lambda_max <= Gamma / ln(1/epsilon)
```

This is the FR2 coupling bound: the observer can finalize records at rate lambda_max
(with decoherence tolerance epsilon) only if the substrate decoherence rate satisfies
Gamma >= lambda_max * ln(1/epsilon) = Gamma_min.

**Structural source of the coupling.** The bound is derived from the Lindblad decay
equation |rho_x(t)|_{off} = |rho_x(0)|_{off} * exp(-Gamma * t). For the off-diagonal
element to fall from the initial value (bounded above by 1) to epsilon in time t_obs:

```
exp(-Gamma * t_obs) <= epsilon
=> Gamma * t_obs >= ln(1/epsilon)
=> Gamma >= ln(1/epsilon) / t_obs = ln(1/epsilon) * lambda_max
```

The BvN wall provides the structural reason the classicality gate is non-trivial: until
Gamma * t_obs >= ln(1/epsilon), the element's density matrix has off-diagonal elements
> epsilon, and the observer's event algebra for x is non-distributive (the BvN
obstruction: no classical shadow of x is available). The rate-parameterized form of
the BvN wall crossing is exactly the Gamma_min bound.

**Why this is distinct from FR1's pairing.** The FR1 pairing had only the order-completion
gate (stage 1 above). No classicality certification was required. In FR1, lambda_max was
absorbed by L4+L2 because the per-record cost w depended on the order structure (L4)
and the observer's compute budget B (L2), with no third input. Here, stage 2 adds a
third input: the substrate's decoherence rate Gamma (an L1 property of the quantum
causal set). The addition of Gamma is the L1-L2 coupling. Without quantum amplitudes
in (C, prec), this coupling is absent; with them, it is forced by Lindblad dynamics.

**Literature anchor:** Lindblad decay law (Lindblad 1976); BvN obstruction at element
level (`fr2-bvn-layer5-promotion-gate-2026-06-23.md`); FR2 Gamma_min derivation
(`fr2-bvn-rate-of-classicality-derivation-2026-06-22.md`); FR1 rate-blind completeness
gate (`fr1-sorkin-absorption-worked-check-2026-06-22.md`, Sections 3.1-3.2).

**Class-assumption signature broken:** The FR1 pairing (and all standard no-go theorem
pairings) is class (a) cartesian/smooth: the observer receives classical substrate data
via a well-defined extraction channel without any active classicality certification step.
This candidate's pairing is metastable-consensus class (f): the coupling inequality
Gamma >= Gamma_min is the admission criterion for the pairing to produce a classical
record. Below Gamma_min, the pairing produces a quantum-mixed record (indefinite pointer-
basis value) and the causal-set invariant is undefined.

---

## Leg 4 — Causal-Order Class

**Class label:** (d) Sorkin causal-set (substrate IS the causal order; L1 and L4 coupled).

**Specification:** The causal order on the substrate is the partial order prec on (C, prec, psi).
This is the same causal-set partial order as in the FR1 example and example-02 of the
six-axis specification protocol: locally finite, acyclic, irreflexive, with no global
Lorentzian metric (metric is emergent, per "Order + Number = Geometry"). The L1-L4
coupling rule for Sorkin causal sets applies: (C, prec) is simultaneously the substrate
object (L1) and the causal-order model (L4). There is no coherent sextuple with
(L1 = Sorkin causal-set, L4 not-d) or (L1 not-Sorkin, L4 = d).

**New feature relative to FR1.** The causal order in FR1 was purely classical: it
determined which elements needed to be present for order-completion, and that predicate
was rate-blind. In the quantum causal set (C, prec, psi), the causal order still performs
the same order-completion role (L4 is rate-blind per FR1's structural result). But the
quantum amplitude layer adds a new role for L1 (not L4): each element x carries a
coherence lifetime 1/Gamma_x determined by its Lindblad dynamics. L4 (the causal order
prec) remains rate-blind; L1 (the quantum amplitude assignment psi) supplies the
decoherence rate Gamma that enters the coupling bound.

**Separation of L1 and L4 roles in the coupling.** The coupling bound lambda_max <=
Gamma/ln(1/epsilon) has two axes contributing:
- **L4 contribution:** ln(1/epsilon) / lambda_max = t_obs, the per-record finalization
  latency, is bounded from below by the order-complexity of x's past (L4 sets the
  minimum t_obs per FR1's w = poly(max-past-size(prec, W))). For fixed observer budget B,
  lambda_max = B/w (L2/L4), and t_obs = 1/lambda_max = w/B.
- **L1 contribution:** Gamma is a property of the quantum amplitude assignment psi (L1),
  not of the causal order prec (L4). It represents the coherence dynamics of the substrate
  elements, which is a new physical input not present in the FR1 classical setting.

The coupling rule therefore couples L1 (decoherence rate Gamma from the quantum amplitudes)
and L2 (finalization rate lambda_max from the observer's compute budget and latency) with L4
playing a supporting role in setting the minimum t_obs.

**Literature anchor:** Sorkin causal-set causal-class (d) from six-axis protocol
(`canon/six-axis-specification-protocol.md`); FR1 rate-blindness of prec
(`fr1-sorkin-absorption-worked-check-2026-06-22.md`, Section 3.1 -- "L4 yields no finite
lambda_max"); Sorkin-causal-set L1-L4 coupling (`explorations/sorkin-causal-set/sorkin-causal-set-axis-note.md`, Section 4.1).

**Class-assumption signature broken:** Same as the standard Sorkin drop: Witten 1981,
Freed-Hopkins, Distler-Garibaldi all assume total-order Lorentzian causal structure.
The partial order is strictly more general. (Same break as FR1; no new break from the
quantum amplitude layer at L4.)

---

## Leg 5 — Emergence Class

**Class label:** (a) Specific-object substrate — a particular (C, prec, psi) with a
specific Lindblad decoherence rate Gamma and specific causal-set structure.

**Specification:** The candidate is not a universality class (L5 != b). It is a specific
quantum causal set (C, prec, psi) with a uniform Lindblad decoherence rate Gamma across
elements (the general case uses Gamma = min_x Gamma_x as the effective coupling-rule
input). The coupling rule lambda_max <= Gamma/ln(1/epsilon) is a specific numerical
constraint for each choice of Gamma and epsilon; it is not a statement about a
universality class. The emergence class is specific-object, the same as the first filled
row and as the standard FR1 Sorkin example.

**GU contact.** The GU Tikhonov section-selection candidate uses the quantum metric
fluctuations of Y^14 as its L1 substrate. The present candidate uses the quantum
amplitudes of a Sorkin causal set as its L1 substrate. These are two different specific
objects at which the same coupling rule fires (decoherence rate Gamma bounds record
finalization rate lambda_max). The specific-object class is preserved; the objects differ.

**Literature anchor:** Specific-object emergence class (a) from six-axis protocol; FR1
specific Sorkin example-02 (`specifications/six-axis/examples/example-02-sorkin-causal-set.md`).

**Class-assumption signature broken:** No standard no-go theorem assumption is broken
at L5. The standard no-go theorems also use specific-object substrates. The difference
is at L1 (quantum causal set vs. smooth bundle), L2 (classicality-certifying observer),
and L3 (metastable-consensus pairing with coupling bound). L5 is inherited from the
baseline.

---

## Leg 6 — Coordination-Loop Class

**Class label:** (g) Completeness-gated cadence loop — the observer's finalization rate
lambda_max is dynamically bounded by the substrate's decoherence rate Gamma; the
cadence Delta is set to t_obs = max(w/B, ln(1/epsilon)/Gamma) to avoid premature commitment.

**Specification:** The coordination loop governs the pace of record finalization. The
observer sets its finalization cadence Delta (time between successive finalizations) to:

```
Delta = max(w/B, ln(1/epsilon)/Gamma)
```

where:
- w/B is the L2/L4-determined per-record cost (from FR1: w = poly(max-past-size(prec, W)),
  B = observer compute budget, giving the classical FR1 bound lambda_max = B/w).
- ln(1/epsilon)/Gamma is the new L1-driven lower bound on Delta: the minimum time required
  for the substrate decoherence to drive off-diagonal elements below epsilon.

The cadence loop closes as follows: the observer finalizes element x when BOTH (a) the
order-completion gate (J^-(x) cap P(O) is order-complete) AND (b) the classicality gate
(Gamma * Delta >= ln(1/epsilon)) are satisfied. The loop feeds back from the substrate's
decoherence rate (an L1 quantity) to the observer's cadence (an L2/L6 quantity): the
observer must slow down (increase Delta) if Gamma is small (slow decoherence) relative
to the tolerance epsilon and the target rate lambda_max.

**Contrast with FR1's no-loop setting.** In FR1, the L6 setting was "No loop" (class (a)):
the record-graph was static, the observer accumulated records, and no feedback from
decoherence to cadence was present. Adding quantum amplitudes to the causal-set elements
turns L6 from class (a) into the cadence-gated class (g), because the observer's
finalization rate is now constrained by the substrate's coherence dynamics. This is a
genuine change in the coordination-loop class driven by the change in L1 (from classical
to quantum causal set).

**Relation to FR4's cadence field Delta.** FR4 (`fr4-l6-cadence-parameterization-2026-06-22.md`)
introduced the cadence field Delta as an L6 field for deadline-gated finalization,
establishing a distinct failure mode (premature commitment) from the FR1 order-completion
gate. The present cadence loop uses the same Delta field, but the trigger for adjusting
Delta is the substrate decoherence rate Gamma rather than an external deadline policy.
This is a third cadence variant (L1-driven, not deadline-driven), structurally distinct
from both the no-loop (class (a)) and the deadline-cadence loop of FR4.

**Literature anchor:** FR4 cadence field (`explorations/time-as-finality-crosswalk/fr4-l6-cadence-parameterization-2026-06-22.md`);
FR2 Gamma_min as finalization-latency bound (`fr2-bvn-rate-of-classicality-derivation-2026-06-22.md`,
Section 3); observer-section coupling in L6 for the first filled row
(`six-axis-l1l2-coupling-filled-example-2026-06-23.md`, Leg 6).

**Class-assumption signature broken:** The no-go theorem baseline has no coordination
loop (class (a)): substrate data is available on demand, no coherence-driven pacing is
required. This candidate requires L6 feedback from L1 (Gamma) to the observer's cadence:
the standard no-go theorem setup does not model this dynamic. The cadence loop is the
loop that makes the coupling rule observable as a constraint: without it, the observer
could attempt to finalize records faster than Gamma/ln(1/epsilon) and would trigger
the classicality gate failure mode (record finalized with residual off-diagonal elements
above epsilon, producing a mixed-state record whose classical invariant is undefined).

---

## Explicit Derivation: The Coupling Bound Fires in the Causal-Set Setting

We now show step by step that lambda_max <= Gamma/ln(1/epsilon) arises naturally from the
Sorkin causal-set structure enriched with quantum amplitudes, without requiring ad hoc
rate assumptions.

### Step 1. Lindblad Decay in the Causal-Set Element

Let x be any element of (C, prec, psi). The density matrix rho_x(t) satisfies:

```
|rho_x(t)|_{off} <= exp(-Gamma * t) * |rho_x(0)|_{off}
```

where |.|_{off} denotes the operator norm of the off-diagonal block (in the pointer basis).
This is the standard Lindblad decoherence estimate; it is exact for pure dephasing and an
upper bound for general Lindblad dynamics.

### Step 2. Classicality Gate Condition

The observer O finalizes the record of x at time t_fin(x), which is the time at which
BOTH gates are satisfied:
- Gate 1 (order-completion): t_OC(x) = time when J^-(x) cap P(O) becomes order-complete.
  This is a function of the causal order prec and the arrival sequence of elements into
  P(O). It is rate-blind (FR1 structural result).
- Gate 2 (classicality): |rho_x(t)|_{off} <= epsilon, satisfied for the first time at
  t_class(x) = ln(1/epsilon) / Gamma (from the Lindblad estimate at equality, taking
  |rho_x(0)|_{off} = 1 as the worst case).

The actual finalization time is:
```
t_fin(x) = max(t_OC(x), t_class(x))
```

### Step 3. The Finalization Rate Is Bounded

The observer's finalization rate lambda_max is the inverse of the average finalization
latency: lambda_max = 1 / E[t_fin(x)]. Since t_fin(x) >= t_class(x) = ln(1/epsilon)/Gamma:

```
E[t_fin(x)] >= ln(1/epsilon) / Gamma
=> lambda_max = 1 / E[t_fin(x)] <= Gamma / ln(1/epsilon)
```

This is the coupling bound. It follows from:
1. The Lindblad decay law (a property of the L1 substrate's quantum amplitude dynamics).
2. The observer's classicality gate (a property of the L2 observer's tolerance epsilon).
3. The finalization-latency definition (the rate-finalization-latency duality: lambda_max = 1/t_obs).

No ad hoc rate assumption is introduced. The bound arises from (i) the Lindblad decay
rate Gamma (an L1 quantity determined by the quantum amplitude structure of the causal-set
elements) and (ii) the observer's tolerance epsilon (an L2 quantity determined by the
observer's classicality requirements). The causal order prec (L4) contributes a separate
lower bound t_OC(x) >= w/B (from FR1), but does not generate the Gamma_min bound -- that
bound is entirely L1-driven.

### Step 4. The FR1 Rate-Blindness is Preserved

The FR1 result established that the Sorkin partial order prec is rate-blind: the
order-completion gate fires at a causal event (the last element of J^-(x) enters P(O)),
not at a rate threshold. This result is unaffected by the quantum amplitude layer, because:
- The order-completion gate (Gate 1) is computed purely on the causal order prec, not
  on the quantum amplitudes psi.
- The decoherence rate Gamma enters only Gate 2 (classicality), not Gate 1.
- The two gates are independent: the order-completion check is rate-blind; the
  classicality check is not rate-blind (it has an explicit time dependence t_class = ln(1/epsilon)/Gamma).

FR1's result that "prec is rate-blind; a patient completeness-gated observer is safe at
any rate below its L2 capacity ceiling" continues to hold for Gate 1. The coupling rule
lambda_max <= Gamma/ln(1/epsilon) comes entirely from Gate 2 (classicality), which FR1
did not have. The quantum amplitude layer adds the second gate without invalidating FR1.

### Step 5. The BvN Wall Fires at the Element Level

The BvN wall (`fr2-bvn-layer5-promotion-gate-2026-06-23.md`) states that for any Hilbert
space H with dim H >= 2, there is no natural transformation I: CAlg -> OMLat (from
commutative algebras to orthomodular lattices) that is functorial with respect to the
unitary action on Q(H) (quantum observables). Applied at the level of a single causal-set
element x with dim(H_x) >= 2:

Below Gate 2's threshold (Gamma * t < ln(1/epsilon)), rho_x(t) has off-diagonal elements
> epsilon. The observer's event algebra for x is the quantum lattice L(H_x) (orthomodular,
non-distributive). There is no classical shadow of x available at the C*-algebra level
that commutes with the unitary action on H_x. The BvN wall is the structural reason Gate 2
is non-trivial: it is not a matter of computational convenience but of the lattice structure
of quantum events versus classical events.

When Gamma * t >= ln(1/epsilon) (Gate 2 closes), rho_x has decohered to within epsilon
of a pointer-basis eigenstate. The off-diagonal elements are epsilon-small, and the
observer's event algebra for x is epsilon-close to a Boolean lattice (a classical shadow).
The BvN wall has been crossed: the quantum event structure of x has been driven to within
epsilon of a classical event structure by the Lindblad dynamics. At this point, the
classical record of x is available to the observer within error epsilon.

This confirms that the coupling bound lambda_max <= Gamma/ln(1/epsilon) is the rate-
parameterized form of the BvN wall crossing in the causal-set context. The decoherence
rate Gamma determines how fast the wall is crossed; the tolerance epsilon determines
how close to classical the observer needs the element to be; the finalization rate
lambda_max determines how often the observer needs the crossing to have occurred.

---

## Chirality Bridge Claim

In the Sorkin causal-set context, the chirality bridge operates at a different level than
in the GU-Y^14 candidate. The present candidate is not making a new claim about SM generation
count; it is a structural candidate that shows the coupling rule fires on a different L1 substrate.

The chirality content of the Sorkin causal-set substrate (if any) is the subject of the
scoping note (`explorations/sorkin-causal-set/sorkin-causal-set-axis-note.md`), which
identifies three candidate construction families for a substrate-native causal-set chirality
invariant (spinor-BdAlembertian, signed-abundance asymmetry, BD-kernel reflection-asymmetry)
and finds that none is currently established. The L1-L2 coupling rule does not depend on
the chirality content of the substrate: the coupling bound lambda_max <= Gamma/ln(1/epsilon)
fires regardless of whether the causal-set carries a chirality invariant.

**Role of the coupling rule in the chirality picture.** If a causal-set chirality invariant
IS eventually established (the scoping note's open problem), the coupling rule provides a
necessary condition for any observer to read it off: the observer must have Gamma >=
lambda_max * ln(1/epsilon) to finalize classical records of the quantum causal-set elements
that carry the chirality information. Below Gamma_min, the chirality invariant (like all
other element invariants) is not available to the observer as a classical quantity. This is
the same role Gamma >= Gamma_min plays in the GU-Y^14 candidate: it is a pre-classicality
precondition on the observer, not a condition on the chirality invariant itself.

**Forgetful operation.** The Cauchy-slice-linearization map phi_CSL: (C, prec) -> (M^4, g)
(established in the Sorkin scoping note, Section 5) operates on the classical shadow of
the quantum causal set: it takes the pointer-basis eigenvalues of rho_x (once decoherence
has occurred) as the classical causal-set elements and constructs the smooth approximant.
Below Gamma_min, the pointer-basis eigenvalues are not well-defined to precision epsilon,
and phi_CSL's input is not available. Above Gamma_min, phi_CSL operates on the classical
shadow and its output (the smooth manifold with the standard no-go theorem assumptions)
is the image in which Witten 1981, Freed-Hopkins, and Distler-Garibaldi compute.

---

## Coupling Rule Falsification Condition

**Stated falsification condition:** Exhibit a Sorkin causal-set observer instantiation
of (C, prec, psi) such that an observer O with decoherence tolerance epsilon and
finalization rate lambda_max > Gamma/ln(1/epsilon) finalizes records of elements of C
without any record having off-diagonal density-matrix elements above epsilon at finalization
time, and without any causal completeness gate failure.

**Concretely, this requires:** Either --

(A) **Fast decoherence without the rate bound:** Show that the Lindblad dynamics of some
quantum causal-set element x causes rho_x to decohere to within epsilon in time t < ln(1/epsilon)/Gamma
(faster than the exponential bound). For the pure dephasing model, this is impossible
(the bound |rho_x(t)|_{off} <= exp(-Gamma*t) is exact). For more general Lindblad
operators, the bound is an upper bound, and faster decoherence is in principle possible
for specific Lindblad structures. **Falsification requires a Lindblad operator L_k such
that the off-diagonal decay is super-exponential in Gamma, driving the classicality gate
faster than the exponential bound predicts.** In that case, the effective Gamma_min would
be smaller than ln(1/epsilon)/lambda_max, and the coupling bound would be loosened.

(B) **Classical shadow without decoherence:** Show that the causal-set element x has a
classical record available to O even when |rho_x(t)|_{off} > epsilon (i.e., the BvN wall
does not fire for the specific invariant being read off). This requires that the specific
invariant I(x) (chain count, interval count, chirality candidate) is determinate in the
non-classical state rho_x -- i.e., it is an observable that commutes with the Lindblad
pointer-basis operators L_k. In that case, I(x) is already a classical observable in the
quantum causal set, and the classicality gate for I(x) is trivially satisfied. The coupling
rule then does not apply to I(x) specifically (it applies only to observables that do not
commute with the L_k, i.e., genuinely quantum-coherent observables).

**This is the primary structural escape from the coupling rule:** if the causal-set invariant
of interest is a quantum-coherent observable (does not commute with the pointer-basis
operators), the coupling rule applies. If it is a classical observable (commutes with all
L_k), the coupling rule is vacuously satisfied at any rate. The falsification test is
operationally: identify whether the specific chirality candidate from the scoping note
(spinor-BdAlembertian extension, signed abundance asymmetry, BD-kernel reflection-asymmetry)
is a quantum-coherent or classical observable in the quantum causal set (C, prec, psi).

**Failure condition (the bound does not arise naturally from the Sorkin causal-set structure):**
The bound lambda_max <= Gamma/ln(1/epsilon) does NOT arise naturally from the Sorkin
causal-set structure if the causal-set substrate carries no quantum amplitudes -- i.e.,
if the canonical Sorkin (C, prec) program does not include Lindblad decoherence dynamics
as a native component. In the classical Sorkin program, elements of C have definite
classical invariants (once their pasts are order-complete), and no decoherence rate Gamma
appears. The coupling rule is NOT a statement about the classical Sorkin causal set; it is
a statement about the quantum-amplitude-enriched version (C, prec, psi).

**Therefore:** The coupling rule's natural appearance in the Sorkin setting requires the
quantum causal set enrichment (C, prec, psi) as an explicit additional input. Whether
this enrichment is physically motivated within the Sorkin program (as opposed to being
an external quantum-gravity input) is a separate question -- it is not assumed here.
The present candidate's claim is: IF the causal-set elements carry quantum amplitudes
subject to Lindblad dynamics at rate Gamma, THEN the coupling bound fires by the above
derivation. The conditional is established at reconstruction grade. The unconditional
claim (that standard Sorkin causal sets have Lindblad-decohering elements) requires
engagement with the Sorkin program's quantum dynamics literature (Dowker-Kent 1996 on
quantum causal sets; Henson 2006 review) and is not established here.

---

## One First Falsification Test

**Test.** Identify a chirality-relevant observable I(x) in the quantum causal set
(C, prec, psi) that commutes with all Lindblad pointer-basis operators L_k.

Concretely:
1. Take the quantum causal set (C, prec, psi) with Hilbert spaces H_x = C^2 (minimal
   quantum case, dim H_x = 2, BvN wall fires) and Lindblad operators L_k = {sigma_z}
   (dephasing in the z-basis, pointer basis = {|0>, |1>}).
2. Define a candidate chirality observable I(x) = <sigma_x>(rho_x) (expectation of the
   Pauli-x operator, which does NOT commute with sigma_z) as the signed-abundance
   asymmetry proxy.
3. Evaluate whether I(x) is determinate (equal to a definite value +1 or -1) before
   decoherence has occurred (when |rho_x|_{off} > epsilon).

**Pass condition (coupling rule confirmed):** I(x) = <sigma_x>(rho_x) is NOT determinate
before decoherence: its value depends on the off-diagonal components of rho_x, which are
undefined to precision epsilon when t < ln(1/epsilon)/Gamma. The classicality gate is
non-trivial for I(x), and the coupling bound applies. The causal-set chirality candidate
requires Gamma >= lambda_max * ln(1/epsilon) to be finalized as a classical record.

**Fail condition (coupling rule falsified for this observable):** I(x) commutes with sigma_z
(or is a function of the diagonal elements of rho_x only). Then I(x) is determinate
immediately (the sigma_z pointer basis gives a definite value of I(x) even before decoherence).
In that case, the classicality gate for I(x) is trivially satisfied and the coupling rule
does not constrain lambda_max for this particular observable.

**Physical interpretation.** If causal-set chirality invariants (like signed-abundance
asymmetries) are functions only of diagonal density-matrix elements (pointer-basis
occupation probabilities), they are classical observables and the coupling rule is
vacuous for them. If they require off-diagonal coherence (quantum superpositions of
different causal-set configurations contribute to the signed asymmetry), the coupling
rule is non-trivial. The test operationalizes this distinction for the simplest quantum
causal-set element.

**Tied to no-go theorem assumption.** The test is tied to the Witten 1981 assumption
that the substrate presents definite classical invariants for the Dirac index calculation.
If the causal-set chirality candidate requires off-diagonal quantum amplitudes (is not
a classical observable), the coupling rule confirms that Witten's classical calculation
is inapplicable below Gamma_min; if the candidate is a classical observable, Witten's
framework can be applied at any rate (the coupling rule does not obstruct it, but the
causal-set scoping note's chirality obstruction still applies independently).

---

## Explicit Failure Conditions (Falsification of This Row)

**F1 (Classical causal set, no Lindblad dynamics):** If the Sorkin causal-set program
does not include Lindblad decoherence dynamics as a native substrate feature -- i.e., if
(C, prec) is a purely classical combinatorial object with no Hilbert-space decoration --
then the quantum amplitude layer (C, prec, psi) is an external addition not part of the
Sorkin substrate. In that case, the coupling bound does not arise from the Sorkin
structure itself; it arises from the external quantum-gravity input. This is the primary
structural failure condition: the candidate depends on (C, prec, psi) being a natural
object in the Sorkin program, which requires engagement with the quantum causal set
literature.

**F2 (Super-exponential decoherence):** If a specific Lindblad structure exists such that
|rho_x(t)|_{off} decays faster than exp(-Gamma*t) (super-exponential, not possible for
pure dephasing but possible for multi-Lindblad interactions), the effective classicality
time t_class(x) < ln(1/epsilon)/Gamma, and the coupling bound lambda_max <= Gamma/ln(1/epsilon)
is a loose upper bound rather than a tight one. The coupling rule fires but with a weaker
conclusion than Gamma_min = ln(1/epsilon)/lambda_max. The tightness of the bound depends
on the Lindblad dynamics.

**F3 (Chirality observables are classical):** If every causal-set chirality invariant that
carries physically relevant information (for SM generation count or chiral asymmetry) is
a function only of pointer-basis occupation probabilities (commutes with all L_k), then
those invariants are classical observables and the coupling rule is vacuously satisfied
for them. The rule still applies to quantum-coherent observables, but those may carry no
chirality-relevant information.

**F4 (BvN wall does not fire at dim H_x >= 2 for element-level algebras):** If the BvN
obstruction (the denied functor proof, `fr2-bvn-layer5-promotion-gate-2026-06-23.md`)
does not apply to the element-level event algebra of individual causal-set elements --
for example, if the physically relevant algebra for a causal-set element is commutative
(classical), even when H_x is quantum -- then Gate 2 (classicality) is trivially satisfied
and the coupling rule does not fire. This would require the physical observables of a
single causal-set element to form a commutative algebra despite H_x being a non-trivial
Hilbert space.

**F5 (Coupling formula incorrect for this Lindblad model):** The coupling bound was
derived from the simple exponential decay |rho_x(t)|_{off} <= exp(-Gamma*t). If the
Lindblad model for the quantum causal set uses a non-Markovian dynamics (memory effects,
non-exponential decay), the formula t_class = ln(1/epsilon)/Gamma is not exact and the
coupling bound takes a different form. The correction could be looser (slower decoherence,
stricter bound) or tighter (faster effective decoherence, looser bound).

**F6 (FR1 rate-blindness fails with quantum amplitudes):** If adding quantum amplitudes
to the causal-set elements causes the order-completion gate (Gate 1) to become rate-
dependent -- for example, if the quantum state of element x depends on which predecessor
elements have arrived, making the completeness predicate dependent on the arrival rate --
then FR1's rate-blindness result no longer holds and the Gate 1 and Gate 2 contributions
to the coupling rule are entangled. The FR1 structural result relied on the classical
causal order being a predicate on the poset, not on the dynamics. Adding quantum amplitudes
should not affect Gate 1 (which checks the classical causal order structure), but a
quantum model where the causal order itself is dynamical (quantum causal orders per
Hardy 2007, Oreshkov-Costa-Brukner 2012) could violate this separation.

---

## Axis Comparison with the First Filled Row

| axis | GU-section-BvN-coupling (first row) | Sorkin-CS-Gamma-coupling (this file) |
| --- | --- | --- |
| L1 substrate | Smooth principal bundle Y^14 = Met(X^4), Cl(9,5), quantum metric fluctuations in fiber GL(4,R)/O(3,1) | Locally finite poset (C, prec, psi) with Lindblad-decohering quantum amplitudes on each element; no smooth manifold structure |
| L2 observer | Snowball/metastable consensus observer with decoherence rate Gamma and finalization latency t_obs | Same class: finite observer with decoherence tolerance epsilon and finalization latency t_obs; adds causal-completeness gate from FR1 |
| L3 pairing | BvN-gated metastable-consensus pairing (metric fiber decoherence gates section selection) | Conjunction pairing: causal-completeness gate (FR1) AND classicality gate (FR2); both gates must fire |
| L4 causal order | Conditional Lorentzian on X^4 (classical above Gamma_min; quantum-indefinite below) | Sorkin causal-set partial order (classical; L1-L4 coupled; rate-blind per FR1) |
| L5 emergence | Specific-object (Y^14 with gimmel metric, Tikhonov-selected section s*) | Specific-object (particular (C, prec, psi) with decoherence rate Gamma) |
| L6 loop | Tikhonov-Willmore gradient flow (Lambda = 8 epsilon^2/t_obs^2 couples observer to section energy) | Completeness-gated cadence loop (Delta = max(w/B, ln(1/epsilon)/Gamma) from L4/L2 and new L1/Gamma) |
| Coupling rule source | BvN obstruction at fiber level (smooth bundle); metric decoherence | BvN obstruction at element level (quantum causal set); Lindblad decay; FR1 order-completion |
| Chirality claim | ind_H(D_GU) = 24 = 3 SM generations (CONDITIONALLY_RESOLVED) | No new chirality claim; coupling rule fires independent of chirality content; chirality question delegated to Sorkin scoping note |
| First falsification test | Quantum Willmore well-posedness: is the Tikhonov-Willmore minimizer always pure? | Classical vs. quantum observable: does the causal-set chirality candidate commute with Lindblad L_k? |

The two candidates are distinct on L1, L3, L4, L6, and chirality claim. They share L5
(specific-object) and L2 class (both use a classicality-certifying finite observer with
epsilon and t_obs). The coupling rule fires in both via the same mechanism (Lindblad decay
+ BvN obstruction + tolerance epsilon + finalization latency t_obs), instantiated at
different L1 substrates.

---

## Coupling Rule Verified: Summary Table

| quantity | formula | source axis | derivation |
| --- | --- | --- | --- |
| Decoherence rate | Gamma | L1 (quantum amplitude dynamics of (C, prec, psi)) | Lindblad coefficient for element x |
| Classicality time | t_class = ln(1/epsilon)/Gamma | L1 + L2 | Lindblad decay equation (exact for pure dephasing) |
| Finalization latency | t_obs = 1/lambda_max | L2 (rate-latency duality) | Definition of finalization rate |
| Order-completion time | t_OC >= w/B (lower bound) | L4 + L2 | FR1 result: w = poly(max-past-size(prec,W)), B = L2 budget |
| Total finalization time | t_fin = max(t_OC, t_class) | L2, L4, L1 | Conjunction of two independent gates |
| Coupling bound | lambda_max <= Gamma/ln(1/epsilon) | L1, L2 | t_fin >= t_class => 1/lambda_max >= t_class = ln(1/epsilon)/Gamma |
| Gamma_min | ln(1/epsilon)/t_obs = ln(1/epsilon) * lambda_max | L1, L2 | The minimum Gamma for which the classicality gate closes within t_obs |

**Conclusion:** The coupling bound lambda_max <= Gamma/ln(1/epsilon) arises naturally
from the Sorkin causal-set structure enriched with quantum amplitudes, without ad hoc
rate assumptions. The derivation uses only:
1. The Lindblad decay equation (L1 property of the quantum causal set elements).
2. The observer's decoherence tolerance epsilon (L2 property).
3. The rate-latency duality lambda_max = 1/t_obs (L2 definition).
4. The FR1 order-completion gate (L4 property, rate-blind, contributes a separate lower
   bound on t_fin but not the coupling bound itself).

The coupling rule is established at reconstruction grade. The primary failure condition
is F1 (whether the quantum amplitude enrichment (C, prec, psi) is a natural object in
the Sorkin program or an external addition).

---

## Verdict and Grade

**Verdict: CONDITIONALLY_RESOLVED at reconstruction grade.**

All six axes are filled with class labels, specifications, literature anchors, and
class-assumption signatures. The coupling bound lambda_max <= Gamma/ln(1/epsilon) is
derived from first principles in the Sorkin causal-set setting (Steps 1-5 above).
The BvN wall fires at the element level. FR1's rate-blindness result is shown to be
preserved (Gate 1 is rate-blind; Gate 2 is rate-sensitive). The coupling rule is
shown to arise from L1-L2 coupling without ad hoc rate assumptions, subject to the
quantum causal set enrichment being a natural L1 substrate.

**Failure conditions (explicit):** F1 through F6 above. The primary failure condition
is F1 (classical causal set, no Lindblad dynamics): if the Sorkin substrate does not
natively include quantum amplitudes with Lindblad decoherence, the coupling rule is an
external imposition, not an internal derivation. Secondary failure conditions are F3
(classical observables) and F6 (entangled gate structure under quantum causal orders).

**Grade justification:** Reconstruction grade because:
- The Lindblad decay equation is a standard result, not requiring re-derivation.
- The BvN obstruction at element level is established in `fr2-bvn-layer5-promotion-gate-2026-06-23.md`.
- The FR1 rate-blindness of the causal order is established in `fr1-sorkin-absorption-worked-check-2026-06-22.md`.
- The quantum causal set enrichment (C, prec, psi) is a reasonable but not canonical
  extension of the Sorkin program; its physical motivation requires specialist engagement.
- The first falsification test (observable commutativity check) has not been run.

**What remains for upgrade to verified:**
- RC1: Determine whether the quantum causal set (C, prec, psi) is a canonical object
  in the Sorkin program (Dowker-Kent 1996, Henson 2006, or successor literature).
- RC2: Run the first falsification test (compute whether candidate chirality observables
  commute with Lindblad L_k operators for the simplest H_x = C^2 case).
- RC3: Identify whether any causal-set chirality candidate from the scoping note
  requires off-diagonal quantum amplitudes to be non-zero (quantum coherence is
  chirality-relevant), which would make the coupling rule non-vacuous for chirality.
- RC4: Verify that FR1's rate-blindness result holds when quantum amplitudes are added
  (Gate 1 and Gate 2 remain independent; quantum causal orders per Hardy/Oreshkov
  do not entangle the two gates).

**Discharge of the second-row promotion condition.** This document fills a second
six-axis specification row with the FR2 coupling rule Gamma >= lambda_max * ln(1/epsilon)
as the load-bearing L1-L2 constraint, using a physically distinct L1 substrate from the
first filled row (Sorkin causal-set with quantum amplitudes vs. smooth principal bundle
Y^14 with quantum metric fluctuations). The second-row promotion gate for the FR2
coupling rule is hereby discharged at reconstruction grade, subject to the failure
conditions F1-F6 and remaining conditions RC1-RC4.
