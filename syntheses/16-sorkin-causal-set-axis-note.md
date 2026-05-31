# Sorkin Causal-Set Axis-Drop — Scoping Note

**Status.** Public draft artifact. Generated 2026-05-30 as the single-pass output of WRK-384.
**Eventual repo home (if accepted).** `syntheses/16-sorkin-causal-set-axis-note.md`.
**Six-axis cross-ref.** This note is the standalone scoping artifact for the **L4 = (d) Sorkin causal-set** axis-drop in the six-axis specification protocol (WRK-375, `specifications/six-axis/six-axis-template.md`). The six-axis worked example `example-02-sorkin-causal-set.md` already fills the sextuple; this note **expands** on that example with the chirality bridge, smooth-shadow analysis, obstruction map, falsification ladder, and L1/L4 coupling treatment that the example's body intentionally left to a downstream scoping pass. It does **not** re-derive the sextuple.

---

## 0. Honesty contract

This note is **not** a claim that the Sorkin causal-set program yields the Standard Model, evades Witten 1981, or hosts a chirality invariant. It is a scoping note that asks one sharply-typed question:

> Does the Sorkin causal-set substrate carry chirality-relevant information that the smooth-Lorentzian shadow (Hawking-King-McCarthy / Malament / sprinkling-fidelity reconstruction) forgets — or does every causal-set chirality candidate either fail to be substrate-native or collapse under the smooth-shadow map to exactly the null Witten-1981 image?

If the answer is "no candidate survives," the L4 = (d) axis-drop is **closed as a chirality route** (it remains a legitimate quantum-gravity / GR-emergence program in its own right, but does not touch the no-go families). If a candidate survives at least the operational checks below, the axis-drop is **promoted to an open problem in the public repo** with a named contributor task.

The note follows the established convention of `wrk-376-gu-no-go-map` (analogy-strength + open-stress columns), `wrk-377-gu-type-ii1-checklist` ([control] / [bridge] / [open] status tags), and `wrk-378-gu-nielsen-protocol` (a single load-bearing predictive bridge plus a single named falsification handle).

---

## 1. Acceptance summary

| field | value |
| --- | --- |
| six-axis sextuple | (L1=k Sorkin causal-set, L2=a finite Turing, L3=a Cartesian/smooth via Cauchy-slice channel, L4=d Sorkin causal-set, L5=a specific-object, L6=a no loop) — see `example-02-sorkin-causal-set.md`. |
| invariant candidate | **Causal-set chirality witness** — an isomorphism-invariant signature on the abundance distribution of small order-intervals of `(C, ≺)` that distinguishes orientation classes of poset embeddings of small chiral patterns without reference to a smooth tangent bundle. Candidate constructions: Sorkin discrete d'Alembertian (BdAlembertian) extensions to spinor-valued fields; signed-interval-abundance asymmetry indices; reflection-asymmetry on the Benincasa-Dowker action's contribution to small-interval kernels. **None published**; the construction is the falsification handle. |
| smooth shadow | The Cauchy-slice-linearization map `ϕ_CSL : (C, ≺) ↦ (M^4, g)` of the sprinkling-fidelity / Malament / Hawking-King-McCarthy reconstruction. The smooth shadow loses: (i) **fine-grained order-interval combinatorics** beyond the manifold-faithfulness regime, (ii) **non-manifold-like causal sets** that have no smooth approximant at all, and (iii) any **substrate-native orientation data** carried at the poset level that does not lift to a tangent-bundle orientation. The Witten-1981 null result is the image of any candidate invariant under `ϕ_CSL` restricted to manifold-faithful causal sets with trivial gauge background. |
| chirality obstruction | **Partial orders do not natively carry orientation data.** Causal-set isomorphism is "directed-graph isomorphism of the Hasse diagram"; isomorphism-invariance plus the lack of a tangent bundle means any chirality witness must extract orientation from order-interval combinatorics or signed-abundance asymmetries. Both routes confront the same structural fact: a partial order `(C, ≺)` is invariant under reversal only up to a global time-direction choice (a single bit), not a tangent-bundle orientation (`O(d)/SO(d)` coset). The obstruction is whether substrate-native combinatorial orientation can be richer than that single bit. |
| L1/L4 coupling treatment | L1 = k and L4 = d are **the same axis-drop in two vocabularies**. L1 names the substrate object class (locally finite poset); L4 names the causal-order class (partial-order substrate-native). Per the WRK-375 example-02 note: "in the Sorkin frame the substrate IS the causal order, so L1 and L4 are coupled." This note treats the coupling as **load-bearing**: a sextuple that lists Sorkin causal-set on L1 but a different (non-d) class on L4 is incoherent, and vice versa. Section 4 makes this constraint explicit and lists which other sextuples in the six-axis space are blocked by this coupling. |
| first falsification test | **Construct a causal-set chirality witness that satisfies all four criteria in `example-02` Section "One first falsification test."** If no isomorphism-invariant, sprinkling-fidelity-well-defined witness can be defined on `(C, ≺)` alone that distinguishes left from right on at least one causal set whose smooth shadow is null, the axis-drop is closed. Specialist judgment required for failure-mode 1 (orientation data); agent pass can produce candidate constructions and check failure-modes 2-3. |
| public-push verdict | **Public open problem.** The L4 = (d) drop is a mature axis with real literature behind it (Bombelli-Lee-Meyer-Sorkin 1987 onward, ≈40 years of program), and the falsification test is operationally crisp. This earns it a public contributor prompt. The note distinguishes "established causal-set physics" (the Sorkin program) from "GU-specific speculation" (the chirality bridge claim) — see Section 6. |

---

## 2. The axis-drop, stated precisely

### 2.1 What is being dropped

The smooth Lorentzian causal structure is dropped to a partial-order causal class. Concretely:

| feature | smooth (00d default) | Sorkin (this axis-drop) |
| --- | --- | --- |
| substrate object | smooth Lorentzian manifold `(M^4, g)` | locally finite partially ordered set `(C, ≺)` |
| causal order | total at each Cauchy slice; light-cone-given | partial; `x ≺ y` iff there is a directed chain from `x` to `y` |
| metric | Levi-Civita on a smooth tangent bundle | emergent from order + number (Sorkin: "Order + Number = Geometry") |
| dimension | fixed by the manifold | emergent (Myrheim-Meyer dimension estimator from chain abundances) |
| chirality home | smooth tangent-bundle orientation + Dirac spinor representation | **the object of this note** — what (if anything) plays this role |
| evolution | Cauchy-slice flow on `Met(X)` | classical sequential growth (Rideout-Sorkin) or quantum analog |

Recovery direction: the smooth Lorentzian manifold appears as the **Cauchy-slice-linearization** of `(C, ≺)` under the sprinkling-fidelity / Malament reconstruction. This map is well-defined only on the "manifold-faithful" subclass of causal sets; generic locally finite posets do not have a smooth approximant.

### 2.2 What is being added

Nothing — no extra structure is imported. The axis-drop is a substrate **simplification** (poset is structurally simpler than smooth manifold + bundle), not a substrate enrichment. This distinguishes the Sorkin path from substrate-enrichment paths like L1 = c (Type II_1 spectral triple, WRK-377) or L1 = f (higher / motivic / tmf / prismatic). The **bet** is that chirality content can survive — and even be enriched — under substrate simplification, because the partial-order data is finer than the Cauchy-slice-linearization preserves.

This is the same bet as the partial-order DAG lens (`passes/05-heterodox-problem-shape-distributed-systems/32-ps-dag-partial-order-heterodox.md`) but on the spacetime substrate rather than on the protocol substrate. Sorkin causal-sets and the distributed-systems partial-order axis are sibling axis-drops on the **same axis** (L4), populating different classes (L4 = d vs. L4 = b CALM-monotonic).

### 2.3 What survives by hypothesis

By hypothesis (to be tested): substrate-level chirality content lives in **combinatorial signatures of the partial-order structure** that the smooth Lorentzian approximant forgets. The candidate constructions are surveyed in Section 3. **None is established**; the survey is what makes the falsification test concrete.

---

## 3. Invariant candidate — substrate-native chirality witness

### 3.1 Three candidate construction families

The note proposes three construction families, all `[open]`. Each must satisfy the four `example-02` falsification criteria: substrate-native, isomorphism-invariant, sprinkling-fidelity well-defined, distinguishes left from right on at least one causal set whose smooth shadow is null.

#### Family A — Spinor lift of the Sorkin discrete d'Alembertian `[open]`

**Construction sketch.** The Sorkin BdAlembertian (Benincasa-Dowker 2010) is a partial-order operator on causal sets whose continuum limit recovers `□`. Extension to a **spinor-valued** BdAlembertian — an operator on a `Cl(d)`-valued sheaf over `C` whose continuum limit recovers `∂̸` (Dirac) — would carry chirality-relevant information at the substrate level via the action of `γ^5` (or its discrete analog) on the spinor structure.

**Status.** Spinor lifts of the Benincasa-Dowker operator have been discussed in the causal-set literature (Aslanbeigi-Buck-Sorkin 2014 on causal-set d'Alembertians; Glaser 2014 on retarded Green functions) but a clean construction that (i) gives a left/right asymmetry on (ii) an isomorphism-invariant footing without (iii) smuggling in a smooth tangent frame is **not established**. The chirality content would have to enter via the orientation of small order-intervals as elementary spinor-frame data.

**Failure mode it most likely hits.** Failure-mode 1 (`example-02`): orientation data is not natively poset structure. A spinor lift must specify what frame the spinor is referred to; if the frame is local in `C`, it requires a substrate-native local orientation, which is exactly the obstruction. **Specialist judgment needed** (Sorkin school) — likely outcome is that any clean construction either (a) reduces to its smooth-shadow chirality via sprinkling fidelity (failure-mode 2) or (b) requires an extra global orientation bit that the smooth shadow also carries (in which case the chirality content is identical, not richer).

#### Family B — Signed-abundance asymmetry index `[open]`

**Construction sketch.** For each small finite poset `P` of cardinality `≤ n`, count the number of order-preserving injections `P ↪ C` (its "abundance" in `C`); this is the standard Myrheim-Meyer / Reid abundance. Define a **signed** version: pair each poset `P` with its **reverse** `P^op`; if there is a canonical orientation distinguishing `P` from `P^op` (e.g., when `P` carries a labeled chirality), the signed difference `n(P) − n(P^op)` is a candidate orientation invariant. The chirality witness is a specific linear combination of such signed differences indexed by chirally-labeled small posets.

**Status.** The unsigned abundance distribution is well-established as a causal-set observable; signed / chirally-labeled versions are not standard. The candidate is operationally checkable: agent pass can compute signed abundances for small `n` (`n ≤ 6` is tractable) on small causal sets and test whether any signed combination is non-zero on sprinklings whose smooth shadow has null Dirac index.

**Failure mode it most likely hits.** Failure-mode 1 again: a "chirally-labeled" small poset has to come from somewhere. If the labeling is just `P` vs `P^op`, the signed difference is exactly the global time-direction bit (which the smooth shadow already carries). If the labeling requires an embedding into an oriented `R^d`, the construction smuggles smoothness in. The interesting case is a **purely combinatorial** chirality on small posets — for instance, a small poset whose Hasse diagram has a non-trivial automorphism orbit whose orbit-data distinguishes left and right. Whether such posets exist is a finite combinatorial question.

#### Family C — Benincasa-Dowker kernel reflection-asymmetry `[open]`

**Construction sketch.** The Benincasa-Dowker action `S_BD(C)` is built from small-interval kernels `K_n` weighted by alternating coefficients; the kernel `K_n` counts `n`-element intervals in `C`. Define a **reflection-asymmetry partner**: for each small interval `I` of cardinality `n`, define a reflection class `I^r` (via a substrate-native involution if one exists), and form the asymmetry `K_n^chirality(C) = (count of I) − (count of I^r)`. If `K_n^chirality` is non-zero for at least one `n` on a causal set whose smooth shadow is null, the candidate survives.

**Status.** Not standard. The construction depends on whether a substrate-native involution on intervals exists; this is the central question. The candidate is closely related to Family B (signed abundance) but uses interval structure rather than general small-poset abundance, which is more naturally tied to the Benincasa-Dowker action.

**Failure mode it most likely hits.** Same as Family B at root: where does the involution come from? If the involution is `≺ ↦ ≻` (reversal), `K_n^chirality` is zero on time-reversal-symmetric causal sets, which is exactly the case where the smooth shadow also has null chirality (so no separation from the no-go image). If the involution requires extra orientation data, smoothness is smuggled in.

### 3.2 Common structure of the three families

All three families confront the **same obstruction**: a partial order does not natively distinguish "left" from "right." It distinguishes "earlier" from "later" (the order itself, up to a single global time-reversal bit). Any chirality witness on `(C, ≺)` alone must extract a richer orientation from order-interval combinatorics. **Whether this is possible is the central open question of the axis-drop.** The literature has not produced a witness; this note's contribution is to name the question precisely enough that a specialist can either produce a candidate or argue impossibility.

The structural parallel to `wrk-376-gu-no-go-map`'s "non-geometric exits have no published Witten-evasion" finding is exact: this note's Section 1 acceptance row and `wrk-376-gu-no-go-map` Section 2.1's six-axis cross-ref ("L4 paths have no Witten-evasion literature yet, consistent with I12") are the same statement in two vocabularies.

---

## 4. L1/L4 coupling — load-bearing treatment

### 4.1 Statement of the coupling

In the Sorkin frame, **the substrate IS the causal order**. The locally finite poset `(C, ≺)` is simultaneously:

- The **L1 substrate** — the mathematical object the chirality-bearing invariant lives on, before any reduction to a smooth-bundle shadow.
- The **L4 causal-order class** — the order structure that determines what "happens-before" means at the substrate level.

These are not two independent specifications of the candidate; they are the **same specification under two axis-headings**. The six-axis template (WRK-375) lists L1 and L4 as separable axes — and for substrate classes (a) through (j) they are — but for class (k) the two collapse.

### 4.2 What this means for the six-axis space

The six-axis space has nominal cardinality `11 × 6 × 7 × 5 × 5 × 7 = 16,170` sextuples (extending the template menus). For the L1 = k / L4 = d row, the coupling **identifies** the L1 and L4 entries: there is no sextuple with `(L1 = k, L4 ≠ d)` or `(L1 ≠ k, L4 = d)` that is coherent. Concretely:

| sextuple shape | coherence |
| --- | --- |
| `(L1 = k, L4 = d, ...)` | coherent — this note's candidate |
| `(L1 = k, L4 = a)` (Sorkin substrate, total-order Lorentzian causal class) | **incoherent** — the substrate has no total order to extract |
| `(L1 = k, L4 = b)` (Sorkin substrate, CALM-monotonic partial-order) | **incoherent** — the partial order IS the Sorkin order, not a CALM data-flow order on top of it |
| `(L1 = a, L4 = d)` (smooth principal bundle substrate, Sorkin causal-set causal class) | **incoherent** — a smooth manifold has a total-order Lorentzian causal class; calling its causal class "Sorkin" is a category error |
| `(L1 = e, L4 = d)` (Wolfram multiway hypergraph, Sorkin causal-set) | **incoherent in this direction** — though see §4.3 |

**Implication for repo navigation.** The six-axis README should note this coupling explicitly when L1 = k or L4 = d appears, to prevent a contributor from filling a row with an incoherent combination. This is a propagation finding for the coordination pass.

### 4.3 What is NOT collapsed

Some adjacent couplings might look similar but are not the same:

- `(L1 = e, L4 = e)` — Wolfram multiway substrate with branching multiway DAG causal class. These are coupled in the same way (the substrate IS the branching DAG), so the same coupling treatment applies. The Wolfram and Sorkin programs are sibling axis-drops on different L4 classes (d vs e), both with L1/L4 collapse.
- `(L1 = k, L5 = b)` — Sorkin substrate with universality-class emergence (Rideout-Sorkin classical sequential growth class as an L4+L5 combined drop). This is a **legitimate L4+L5 combined candidate**, not blocked by the L1/L4 collapse. The `example-02` Section "Notes" already flags this as a natural extension. The current scoping note covers L4-only; the L4+L5 combined candidate is a separate sextuple worth filling under sibling card #34 (RG-universality) or its successor.
- L2, L3, L6 are independent. The Sorkin axis-drop does not constrain observer class, pairing, or coordination-loop. This matters because it means the standard L2 = a / L3 = a / L6 = a defaults are legitimate and were not forced by the L1/L4 coupling.

### 4.4 Why the coupling is load-bearing for chirality

The coupling means the chirality bridge claim has **two routes that must be the same**:

- Reading on L1: substrate-level chirality is a property of the partial-order poset object.
- Reading on L4: substrate-level chirality is a property of the partial-order causal class.

If the two readings produce **different candidate witnesses**, the coupling is wrong (and the six-axis template needs revision). If they produce the **same candidate witness** (which all three families in Section 3 satisfy — they are witnesses on `(C, ≺)` qua poset), the coupling is consistent and the chirality content is genuinely substrate/causal-order content rather than one or the other.

This is the reason the chirality obstruction is so sharp: a partial order, viewed as either a substrate object or a causal-class structure, does not carry orientation data. The L1/L4 collapse is what makes the no-orientation-data obstruction unavoidable in this axis-drop.

---

## 5. Smooth shadow — the Cauchy-slice-linearization map

### 5.1 The map

The smooth shadow of a Sorkin causal set is the smooth Lorentzian manifold reconstructed by the sprinkling-fidelity / Malament / Hawking-King-McCarthy program:

```
ϕ_CSL : (C, ≺) ↦ (M^4, g)
```

where `(M^4, g)` is the smooth Lorentzian manifold whose causal structure is sprinkled-faithful to `(C, ≺)` in the manifold-like regime. The map is well-defined on the **manifold-faithful subclass** of causal sets — those whose order-interval abundance distributions match Poisson sprinklings of a smooth Lorentzian manifold within tolerance. Generic locally finite posets are not manifold-faithful and have no smooth shadow at all.

### 5.2 What `ϕ_CSL` forgets

Three categories of information are lost under `ϕ_CSL`:

1. **Fine-grained order-interval combinatorics beyond manifold-faithfulness.** Two causal sets with the same `K_2, K_3, ..., K_N` abundances (for some `N` tied to the manifold-fitting tolerance) project to the same smooth shadow. Differences in `K_{N+1}, K_{N+2}, ...` and in correlations across abundances are forgotten.
2. **Non-manifold-like causal sets entirely.** A causal set whose abundance distribution does not match any smooth-Lorentzian sprinkling has no smooth shadow — `ϕ_CSL` is undefined. These causal sets are by definition outside the no-go theorems' image (the theorems compute on smooth manifolds), and are the natural home for substrate-level chirality witnesses that have no smooth analog at all.
3. **Substrate-native orientation data carried at the poset level that does not lift to a tangent-bundle orientation.** This is the speculative category and is exactly the home of the candidate chirality witnesses in Section 3.

### 5.3 Where Witten 1981 sits in this picture

Witten 1981 computes the 4d Dirac index on the image of `ϕ_CSL` restricted to manifold-faithful causal sets with trivial gauge background and smooth Levi-Civita reduction. The result is null. The Sorkin axis-drop's question is whether the **non-image** of `ϕ_CSL` (categories 2 and 3 above) contains an SM-compatible chirality structure.

The candidate chirality witnesses in Section 3 attempt to populate **category 3** — substrate-native data that lives on manifold-faithful causal sets but is not preserved by `ϕ_CSL`. Whether this category is non-empty is the falsification question.

**Category 2** (non-manifold-like causal sets) is a separate route: if SM physics arises on non-manifold-like causal sets, the smooth-bundle shadow is not just lossy but undefined, and the no-go theorems literally do not apply. This route is harder to argue for (why would SM physics, which empirically has a smooth Lorentzian shadow, live on a non-manifold-like causal set?) and is not pursued in this scoping note. It is flagged as a future direction.

### 5.4 Cross-ref to the no-go map's framework

`wrk-376-gu-no-go-map` Section 2.1 defines the smoothing functor

```
ϕ_smooth : (X̃, S, B) ↦ (X', trivial-bg)
```

for the standard geometric (orbifold / boundary / brane / flux) class exits from Witten 1981. The Sorkin axis-drop's `ϕ_CSL` is a **different functor on a different source category**: not "smooth-with-singularities ↦ smooth," but "poset ↦ smooth." The composition picture for the unified frame is:

```
(Sorkin C, ≺) --ϕ_CSL--> (smooth M^4, g)  --ϕ_smooth--> (Witten image)
```

Where `ϕ_smooth` is the identity on smooth-without-singularity inputs. The unified framing is that **all axis-drops feeding into the smooth-bundle shadow factor through some smoothing-class functor**, and Witten 1981 is the constraint on the final image. Sorkin contributes a new factor at the top of the diagram; the rest of the picture is shared with the orbifold / brane / flux class exits and with the L1 = c / L1 = f substrate-enrichment paths.

---

## 6. Established literature vs GU-specific speculation

Following the DoD-4 convention of `wrk-377-gu-type-ii1-checklist` (status tags `[control]` / `[bridge]` / `[open]`):

| claim | status |
| --- | --- |
| Locally finite poset substrate `(C, ≺)` is the Sorkin causal-set program's central object. | `[control]` Bombelli-Lee-Meyer-Sorkin 1987. |
| Smooth Lorentzian manifolds are reconstructible from causal-set data under sprinkling fidelity. | `[control]` Hawking-King-McCarthy 1976; Malament 1977. |
| Sorkin discrete d'Alembertian `B` has a continuum limit recovering `□`. | `[control]` Benincasa-Dowker 2010 (4d); Aslanbeigi-Buck-Sorkin 2014 (higher d). |
| Causal-set classical sequential growth (CSG) defines a stochastic dynamics on the space of past-finite posets. | `[control]` Rideout-Sorkin 2000. |
| Order + Number = Geometry — geometric information is recoverable from order plus chain abundances. | `[control]` Sorkin 1991, Bombelli-Henson-Sorkin 2009 (Myrheim-Meyer dimension). |
| A spinor-valued extension of `B` whose continuum limit is `∂̸` exists in a form that carries substrate-native chirality. | `[open]` No published construction satisfies all four falsification criteria from `example-02`. |
| The smooth Lorentzian causal-class assumption of Witten 1981, Freed-Hopkins, Distler-Garibaldi is broken by L4 = d. | `[bridge]` — the assumption-class break is uncontroversial (causal sets are not smooth Lorentzian manifolds); whether this break carries chirality content is the open question. |
| A substrate-native causal-set chirality invariant exists. | `[open]` Conjectural; the three candidate families in Section 3 are the operational handles. |
| Causal-set substrate + L5 = b (RG / universality) is a natural combined L4+L5 drop. | `[bridge]` — flagged by `example-02` Notes; not constructed; cross-refs to sibling #34. |
| If no substrate-native chirality invariant exists, the L4 = d drop is closed as a chirality route but remains live as a GR / quantum-gravity / spacetime-emergence program. | `[bridge]` — the GR/QG program is unaffected by chirality failure; this note's verdict only constrains the chirality bridge. |

This is the line between the established Sorkin program and what would be GU-specific addition. The contributor task (Section 8) is scoped to the `[open]` items only.

---

## 7. Chirality obstruction — what mechanism would block or admit it

### 7.1 Block mechanism (most likely)

**Mechanism.** Partial orders do not natively carry orientation. The Hasse diagram of `(C, ≺)` is invariant under directed-graph isomorphism, which is a much smaller automorphism group than the tangent-bundle orientation group. Specifically:

- Smooth Lorentzian manifold orientation lives in `O(d, 1)/SO^+(d, 1)`, which carries time-orientation (a single bit) AND space-orientation (`O(d)/SO(d)`, another bit), AND the structure to distinguish them coherently across the manifold.
- Causal-set order-isomorphism preserves `≺` only. Reversal `≺ ↦ ≻` gives a single global time-direction bit. Beyond that bit, there is no native left/right distinction in the data.

**Consequence.** Any chirality witness on `(C, ≺)` alone must extract orientation from combinatorial structure of order intervals. Section 3 surveys three families; all confront this obstruction. The specialist judgment (Sorkin school) is needed to decide whether the combinatorial-orientation extraction is possible in principle.

**Sibling parallel.** This is the Sorkin analog of `wrk-378-gu-nielsen-protocol` Section 5.1's "load-bearing claim is on-site exact axial symmetry ↔ CALM-monotonicity." Here the load-bearing claim is "tangent-bundle orientation ↔ poset combinatorial orientation" — and the chirality verdict turns on whether the right-hand side carries strictly more than a single bit.

### 7.2 Admit mechanism (the conjectural route)

**Mechanism.** A combinatorial chirality structure on small posets exists if there are finite posets whose Hasse diagrams admit non-trivial automorphism orbits in a way that distinguishes orientation classes of embeddings into `R^d`. Concretely: a finite poset `P` such that its embeddings into a sprinkled-faithful causal set come in two classes that are isomorphic as abstract posets but project to distinct chirality data in the smooth shadow.

**What would have to be true.** The poset's "embedding class" data — which chirality of `R^d`-embedding the poset comes from — would have to be recoverable from the poset's order structure plus its abundance distribution in the host causal set, **without** referring to the embedding map itself. The candidate witnesses in Section 3 are operational handles on this question.

**Why this is hard.** The combinatorial-orientation question is similar to a known hard problem in discrete geometry: order types of point sets in `R^d` distinguish chirality (a point set and its reflection have distinct order types in dimension `d ≥ 2`), but the order-type data depends on the embedding, not just the abstract poset. The Sorkin question is whether a coarser, embedding-independent invariant can still distinguish chirality. **This is genuinely open and likely needs specialist input.**

### 7.3 Failure modes that close the drop

From `example-02`:

1. **No isomorphism-invariant chirality construction exists on partial orders** (the Section 7.1 obstruction wins).
2. **All proposed constructions collapse under sprinkling fidelity to the smooth chirality**, leaving the no-go image intact.
3. **Construction exists but requires extra structure** (orientation, sign rule) that is not substrate-native and smuggles smoothness back in.

If any one of these three failure modes is shown to be universal (across all candidate witness families), the L4 = d axis-drop is closed as a chirality route. The GR/QG program is unaffected.

---

## 8. First falsification test (and contributor task)

### 8.1 The test (verbatim from `example-02`, restated for this note's scope)

**Test.** Attempt to construct a causal-set chirality invariant satisfying all four criteria:

1. Defined purely on `(C, ≺)` — no smooth tangent structure required.
2. Invariant under causal-set isomorphism.
3. Sprinkling-fidelity well-defined: under sprinkling of a smooth Lorentzian manifold into a causal set, the invariant must give a well-defined limit that agrees with smooth chirality on smooth backgrounds.
4. Distinguishes left from right on at least one causal set whose smooth shadow is null.

If no such invariant can be constructed across the three candidate families in Section 3 (Family A spinor lift, Family B signed-abundance asymmetry, Family C BD-kernel reflection-asymmetry), the drop is closed as a chirality route.

### 8.2 Runnability

- **Failure-modes 2 and 3 (sprinkling collapse, smuggled smoothness):** runnable by an agent pass + small-poset enumeration. Tractable for `n ≤ 6` small posets, `N ≤ 10^4` causal-set elements.
- **Failure-mode 1 (no isomorphism-invariant chirality on partial orders):** requires specialist judgment. Likely needs Sorkin-school engagement (Sorkin, Dowker, Henson, Surya, Benincasa school) or a careful agent pass familiar with causal-set program literature. This is the central question.

### 8.3 Contributor task (issue-template-ready)

Following the issue-template convention of `wrk-380-gu-insight-mining`:

**Task title.** Construct or rule out a substrate-native causal-set chirality invariant.

**Issue type.** `open-problem`.

**Description.** The Sorkin causal-set axis-drop (six-axis L4 = d) is a mature heterodox substrate path with ≈40 years of literature. Whether it can carry chirality content — and so connect to the Witten 1981 / Freed-Hopkins / Distler-Garibaldi no-go families — turns on a single open question: does a substrate-native causal-set chirality invariant exist? This task asks specialists to attempt one of three candidate construction families (or propose a fourth) and check it against four explicit criteria.

**Acceptance.** Either:

(a) A construction satisfying all four criteria from Section 8.1, with worked examples on at least three small causal sets demonstrating the invariant is non-zero where the smooth shadow is null. The path is promoted to a full GU pathway with downstream questions about three-generation structure, gauge group emergence, and connection to the spectral-triple / Distler-Garibaldi families.

(b) An impossibility argument — a proof or strong heuristic that one of the three failure modes in Section 7.3 is universal across all candidate construction families. The path is closed as a chirality route and remains alive as a GR / quantum-gravity / spacetime-emergence program.

**Specialist runner.** Causal-sets specialist (Sorkin school) is preferred. A careful agent pass familiar with Bombelli-Lee-Meyer-Sorkin (1987), Sorkin's "Causal sets: discrete gravity" (2003), Dowker's "Causal sets and the deep structure of spacetime" (2013), and Benincasa-Dowker (2010) can produce candidate constructions and check failure modes 2 and 3.

**Related cards (cross-refs).**

- WRK-375 six-axis protocol (this is the L4 = d worked example).
- WRK-376 no-go-forgetful map (this Sorkin axis is the non-geometric Witten exit the map's Section 2.1 flags as "no published bridge").
- WRK-374 (if separately admitted) Sorkin axis as L4+L5 combined drop.

---

## 9. Cross-references to siblings in the GU research pipeline

### 9.1 Sibling #24 — WRK-375 six-axis specification protocol

**Relation.** This note is the scoping artifact for the L4 = d axis-drop, building on the L4 = d worked example (`example-02-sorkin-causal-set.md`). The example produces the sextuple and one-line falsification test; this note expands on the chirality bridge, smooth shadow, obstruction map, L1/L4 coupling, and contributor task.

**Findings to propagate.** (i) **L1/L4 coupling for class (k)/(d) is load-bearing** — the six-axis README should explicitly note that L1 = k and L4 = d are the same axis-drop in two vocabularies, and that sextuples mixing one but not the other are incoherent (Section 4). (ii) The Sorkin axis-drop's smoothing-class functor `ϕ_CSL` is **different from the standard `ϕ_smooth`** (orbifold / boundary / brane / flux) — it acts on poset → smooth, not smooth-with-singularities → smooth. The unified framing in `wrk-376` Section 2.1 should note this as a second functor type (Section 5.4).

### 9.2 Sibling #25 — WRK-376 no-go-forgetful image map

**Relation.** The no-go map's Section 2.1 Witten row notes "non-geometric exits (stochastic/observer/causal-set) are not in established literature." This note is the operationally-scoped follow-up for the causal-set non-geometric exit specifically. The chirality bridge claim here is the bridge the map's Section 2.1 marks as "open derivation problem; the formal opening exists but the substantive derivation does not."

**Findings to propagate.** (i) The Sorkin axis-drop's failure modes (Section 7.3) are the **same failure modes** the no-go map's Distler-Garibaldi row marks as "every successful evasion leaves the class entirely" — but at the L4 = d axis rather than the L1 = a single-E8 axis. In both cases, the unified frame's claim is weakest exactly where the substrate-shadow analogy is most original. (ii) The map's Section 4 ranked test 5 — "Witten non-geometric evasion search per I12, no Witten evasion using observer/stochastic/causal-set language is published; either find one and document it, or formalize that absence as a structural feature" — is **partially resolved** by this note for the causal-set direction: the absence is now scoped operationally (three candidate families, four criteria) rather than left as a generic gap. The coordination pass may want to update the map's test 5 to flag this note as the causal-set-direction follow-up.

### 9.3 Sibling #25 follow-on — Sorkin-flavored Witten / Freed-Hopkins / Distler-Garibaldi evasions

**Relation.** This note's Section 5.4 places the Sorkin axis-drop in the no-go map's smoothing-class functor framework as an additional layer above `ϕ_smooth`. The Sorkin route is specifically a **Witten 1981** evasion candidate (the Cauchy-slice-linearization map factors through the smooth-without-singularity input class of `ϕ_smooth`). It is **not natively a Distler-Garibaldi evasion** — Distler-Garibaldi is a representation-theoretic statement about single-E8 subgroups, which has no obvious causal-set analog without first emergent Lie-group structure (and Lie groups are emergent in causal sets, which means the Distler-Garibaldi obstruction would have to be checked on the emergent gauge data, not on the causal-set substrate directly). The Freed-Hopkins evasion question is intermediate: causal sets do not natively form bordism categories, so the Freed-Hopkins framework would need to be reformulated in poset-bordism terms, which is its own substantial program.

**Finding to propagate.** The Sorkin axis-drop's primary chirality target is Witten 1981. The Nielsen-Ninomiya and Freed-Hopkins targets are accessible only via additional emergence-class machinery (chirality on the emergent smooth shadow's bundle structure, or poset-bordism reformulation). Distler-Garibaldi is essentially inaccessible without a separate emergent-Lie-group story. The no-go map's per-theorem rows should reflect this: Sorkin (L4 = d) is a Witten-targeted axis-drop, not a full-spectrum no-go evasion.

### 9.4 Sibling #34 — WRK-385 (TBD) RG / universality axis note

**Relation.** Sibling #34 covers L5 = (b) universality-class / RG-fixed-point emergence as a separate axis-drop (`example-03-rg-universality-class.md`). The combined L4 = (d) + L5 = (b) drop — Sorkin causal-set substrate with universality-class emergence via classical sequential growth (Rideout-Sorkin) or quantum-gravity universality-class analogs — is a natural extension flagged by `example-02` Notes. **Not built here.**

**Finding to propagate.** The combined L4+L5 Sorkin-emergence drop is a third candidate worth filling, distinct from both this note (L4 alone) and #34 (L5 alone with default L4). The emergence-class concern that #34 will treat (chirality as RG-relevant operator at fixed point) and the substrate-shadow concern this note treats (chirality as substrate-native combinatorial invariant) are **complementary**, not competing. A worked sextuple `(L1=k, L2=a, L3=a, L4=d, L5=b, L6=a)` would address both at once. Flag for coordination pass; not built as part of this note.

### 9.5 Sibling — non-pipeline cross-ref: `passes/05-heterodox-problem-shape-distributed-systems/32-ps-dag-partial-order-heterodox.md`

**Relation.** The DAG / partial-order lens in `passes/05` introduces L4 = b (CALM-monotonic partial-order) as the distributed-systems sibling of L4 = d (Sorkin causal-set). The two are **different classes on the same axis**, populating L4 differently:

- L4 = b: CALM-monotonic partial-order. The substrate has a partial order from coordination-free data-flow constraints (CRDT safety, CALM monotonicity); the substrate object itself (Leg 1) is whatever it would be otherwise (a smooth bundle, Type II_1 algebra, etc.).
- L4 = d: Sorkin causal-set. The substrate object IS the partial order. L1 and L4 collapse (Section 4).

**Finding to propagate.** The two L4 classes are structurally distinct in a way the `passes/05` synthesis already names: "Sorkin's causal-set program already proposes discrete posets as the spacetime substrate, with continuum Lorentzian geometry as coarse-graining." The CALM/CRDT direction is a different axis-drop that may bear on the chirality question via a different mechanism (a CRDT-merge linearization rather than a Cauchy-slice linearization). Both are L4 = partial-order drops; the substrate-object axis (L1) distinguishes them. The coordination pass may want to make this CALM vs Sorkin distinction explicit in the six-axis README.

---

## 10. Public-push verdict

**Recommendation.** Treat this as a public open problem. Public repo location: `syntheses/16-sorkin-causal-set-axis-note.md`.

**Reasoning.** (i) The L4 = (d) drop has ≈40 years of established literature behind it (Sorkin program). (ii) The chirality bridge claim is operationally crisp (three candidate construction families, four explicit criteria, agent-runnable failure modes 2-3 + specialist-runnable failure mode 1). (iii) The contributor task is issue-template-ready (Section 8.3). (iv) The note distinguishes established causal-set physics from GU-specific speculation cleanly (Section 6 status tags). (v) The L1/L4 coupling treatment (Section 4) closes a real ambiguity in the six-axis specification that would otherwise propagate as quiet incoherence.

**Publication review notes.** The coordination-pass cross-refs (Section 9) should be reviewed and possibly updated for the six-axis README. The note may also want a one-paragraph public-facing introduction explaining the relation to Sorkin's program ("this note does not propose new causal-set physics; it asks one question of the existing program about chirality content") to manage reception in the causal-set community.

**What remains tentative for now.** The candidate construction families (Section 3) are scoping hypotheses until specialist input either advances Family A spinor lift to a constructive proposal or rules out the family. The note's public-facing claim is the **question**, not the answer.

---

## 11. One-paragraph public summary (for repo navigation)

This note scopes the Sorkin causal-set substrate as a single-axis-drop (L4 = d in the six-axis specification protocol) on the smooth Lorentzian causal-class assumption of Witten 1981, Freed-Hopkins, and Distler-Garibaldi. The substrate is a locally finite partially ordered set `(C, ≺)`; the smooth Lorentzian manifold is the image of `(C, ≺)` under the Cauchy-slice-linearization map of the sprinkling-fidelity / Malament reconstruction. In the Sorkin frame the substrate IS the causal order, so L1 = k and L4 = d are coupled. The candidate substrate-level chirality invariant — none currently constructed — is a combinatorial signature on the partial-order structure that distinguishes orientation classes without reference to a smooth tangent bundle. Three candidate construction families are surveyed (Sorkin spinor-BdAlembertian, signed-abundance asymmetry, BD-kernel reflection-asymmetry). The core obstruction is that partial orders do not natively carry orientation; whether substrate-native combinatorial orientation can be richer than a single global time-reversal bit is the central open question. If no candidate satisfies the four falsification criteria (substrate-native, isomorphism-invariant, sprinkling-fidelity well-defined, non-zero on causal sets with null smooth shadow), the L4 = d drop is closed as a chirality route and remains alive as a GR / quantum-gravity / spacetime-emergence program. Contributor task issued at Section 8.3.

---

## 12. Provenance

- Originating bounded pass: WRK-384.
- Generated: 2026-05-30 as the single-pass output of WRK-384.
- Persona dialectic applied per the card's Divergent Persona Dialectic Seed (causal-set theorist, general relativist, QFT-on-causal-sets lens, chirality skeptic, distributed-systems partial-order lens, heterodox synthesizer).
- Source-basis files in this repo:
  - `passes/05-heterodox-problem-shape-distributed-systems/32-ps-dag-partial-order-heterodox.md` (the DAG / partial-order lens that introduced the L4 axis-drop framing).
  - `syntheses/00d-problem-shape-meta-synthesis.md` and `syntheses/00e-problem-shape-distributed-systems-meta-synthesis.md` (the three- and four-leg substrate-observer-pairing specifications this candidate extends).
  - `syntheses/08-supplementary-15-persona-pathway-ranking.md` (per the card's "The Work" section).
  - `deep-research/03-assumption-decomposition-no-go-evasion-literature.md` (Witten 1981 published evasions; explicit confirmation that no published evasion uses causal-set language).
- Related public artifacts:
  - WRK-375 six-axis specification (`specifications/six-axis/`), especially `examples/example-02-sorkin-causal-set.md` (the L4 = d worked sextuple this note expands on) and `examples/example-03-rg-universality-class.md` (the L5 sibling).
  - WRK-376 no-go-forgetful map (`syntheses/10-no-go-forgetful-image-map.md`).
  - WRK-378 Nielsen protocol analogy (`syntheses/12-nielsen-protocol-analogy-pilot.md`) — sibling axis-drop pattern (L3 = g) followed structurally here.
  - WRK-377 Type II_1 spectral SM checklist (`specifications/type-ii1-spectral-sm/`) — status-tag convention adopted here.
- Pipeline coordination row: #33.
