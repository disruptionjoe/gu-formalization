# Example 02 — Sorkin Causal-Set Substrate (L4 Axis-Drop)

| candidate | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 coordination loop | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sorkin causal-set | Sorkin causal-set | Finite Turing (BPP/BQP) | Cartesian / smooth (Cauchy-slice channel) | Sorkin causal-set | Specific-object | No loop | Define a causal-set chirality invariant whose Cauchy-slice-linearization image is exactly the Witten-1981 null result; if no such invariant exists, the L4 drop does not open the substrate door. |

## Leg 1 — Substrate class

- **Class label:** (k) Sorkin causal-set substrate.
- **Specification:** The substrate is a locally finite partially ordered set `(C, ≺)`. Spacetime is not a smooth manifold; the smooth Lorentzian manifold is the coarse-grained / sprinkling-faithful approximation of `C`. No prior bundle structure; all geometric content (metric, dimension, curvature) is emergent from order plus number.
- **Literature anchor:** Bombelli-Lee-Meyer-Sorkin (1987); Sorkin, "Causal sets: discrete gravity" (2003); Dowker, "Causal sets and the deep structure of spacetime" (2013).
- **Class-assumption signature broken:** Witten 1981 assumes smooth manifold and Levi-Civita connection; causal-set substrate has neither. Distler-Garibaldi assumes smooth Lie-group embedding; causal sets do not natively carry Lie-group structure (it would be emergent).

## Leg 2 — Observer class

- **Class label:** (a) Finite Turing observer (BPP / BQP).
- **Specification:** Standard finite-resource computational observer. Can compute combinatorial invariants of finite chunks of `C` (chains, antichains, interval structure, abundance counts).
- **Literature anchor:** Standard complexity classes; Rideout-Sorkin classical sequential growth model uses similar observer assumptions.
- **Class-assumption signature broken:** Preserves observer-class assumption (00d default).

## Leg 3 — Pairing

- **Class label:** (a) Cartesian / smooth (Cauchy-slice channel).
- **Specification:** The observer pairs with the substrate via Cauchy-slice-linearization: a smooth Lorentzian approximant `(M^4, g)` is reconstructed by sprinkling fidelity (Hawking-King-McCarthy / Malament reconstruction), and the observer reads bundle/connection data off the approximant. The pairing is the standard smooth channel applied to the reconstructed smooth shadow.
- **Literature anchor:** Hawking-King-McCarthy reconstruction (1976); Malament (1977); the Sorkin reconstruction theorem.
- **Class-assumption signature broken:** Preserves pairing-class assumption.

## Leg 4 — Causal-order class

- **Class label:** (d) Sorkin causal-set (substrate IS a locally finite partially ordered set; Lorentzian metric is emergent).
- **Specification:** Causal order is the partial order `≺` on `C`. No total order, no global time slicing in the substrate. Lorentzian total-order is the image of `≺` under sprinkling-fidelity reconstruction; it is observer-frame data, not substrate data.
- **Literature anchor:** Same as Leg 1.
- **Class-assumption signature broken:** Witten 1981 (smooth Lorentzian Cauchy slicing); Freed-Hopkins (cobordism categories assume smooth manifolds with boundary, not partially ordered substrates). Nielsen-Ninomiya's locality and translation-invariance assumptions are also unstated in causal-set substrate.

## Leg 5 — Emergence class

- **Class label:** (a) Specific-object substrate.
- **Specification:** `C` is a specific causal set (or a specific growth-model trajectory in the Rideout-Sorkin class) chosen for compatibility with SM-class observables. Not a universality-class candidate; that would require combining L4 + L5 (see notes).
- **Literature anchor:** Rideout-Sorkin (2000).
- **Class-assumption signature broken:** Preserves emergence-class assumption.

## Leg 6 — Coordination-loop class

- **Class label:** (a) No loop.
- **Specification:** Substrate is fixed; observer reads off invariants. No backreaction.
- **Literature anchor:** Standard.
- **Class-assumption signature broken:** Preserves coordination-loop assumption.

## Chirality bridge claim

The substrate-level invariant carrying chirality is a **causal-set-native chirality invariant** — a count or signature defined on the partial-order structure of `C` that distinguishes left-handed from right-handed configurations without reference to a smooth tangent bundle. (Candidate constructions: causal-set spinor lifts a la Sorkin's discrete d'Alembertian extensions, or asymmetry indices on the abundance distribution of small intervals.) The forgetful operation is the Cauchy-slice-linearization that produces the smooth Lorentzian approximant `(M^4, g)`; under this operation the causal-set chirality invariant is mapped to a smooth-bundle chirality candidate. Witten 1981 acts on the smooth approximant and computes the null result; the substrate-level invariant survives the forgetting only if causal-set chirality is not exhausted by its smooth shadow. The substrate-level claim is that the partial-order content carries strictly more information than the Cauchy-slice-linearization preserves.

## One first falsification test

**Test:** Attempt to define a causal-set chirality invariant that satisfies all of:

1. Defined purely on `(C, ≺)` — no smooth tangent structure required.
2. Invariant under causal-set isomorphism.
3. Sprinkling-fidelity well-defined: under sprinkling of a smooth Lorentzian into a causal set, the invariant must give a well-defined limit that agrees with smooth chirality on smooth backgrounds.
4. Distinguishes left from right on at least one causal set whose smooth shadow is null (i.e., an explicit substrate-level chirality witness whose Cauchy-slice-linearization image is zero).

**Failure modes that kill the candidate:**

- No isomorphism-invariant chirality construction exists on partial orders (likely because partial orders do not natively carry orientation data).
- All proposed constructions collapse under sprinkling fidelity to the smooth chirality, leaving the no-go theorems' image intact.
- Construction exists but requires extra structure (orientation, sign rule) that is itself not substrate-native and so smuggles smoothness back in.

**Runner:** Causal-sets specialist (Sorkin school) or a careful agent pass familiar with Bombelli-Lee-Meyer-Sorkin. Agent pass can produce the candidate constructions and check failure modes 2 and 3; the orientation-data question (failure mode 1) likely requires specialist judgment.

**Why this test is load-bearing:** The Sorkin L4 drop is only interesting if causal-set order carries more chirality-relevant information than its smooth shadow. If every candidate invariant either fails to be substrate-native or collapses to its smooth image, the L4 drop preserves the Witten-1981 null result and the candidate is dead.

## Notes

- This is a single-axis drop on L4. L1 still names a "substrate" — the causal set — but in the Sorkin frame the substrate IS the causal order, so L1 and L4 are coupled.
- A natural extension is L4 + L5 combined: causal-set growth as a universality-class / RG-fixed-point process (Rideout-Sorkin classical sequential growth class), which would address the "specific causal set vs. class of causal sets" question explicitly. See sibling candidate `WRK-374` (Sorkin axis note) for that direction if separately admitted.
- This candidate is sibling to `example-03-rg-universality-class.md` (single-axis drop on L5) and `example-01-type-ii1-spectral-sm.md` (single-axis modification of L1).
