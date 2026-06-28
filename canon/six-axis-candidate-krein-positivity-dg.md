---
title: "Six-axis candidate: the Krein / ghost-parity positivity-axis evasion of Distler-Garibaldi"
status: candidate
doc_type: six_axis_candidate
created: 2026-06-28
depends_on:
  - work/drafts/wrk-376-gu-no-go-map/no-go-map.md
  - work/drafts/wrk-375-gu-six-axis/six-axis-template.md
  - canon/ghost-parity-krein-synthesis.md
external_ref: "Turok & Bateman, quadratic-gravity / Krein-space generalized Born rule (TOE interview, June 2026; UNPUBLISHED, not a citable paper)"
---

# Six-axis candidate: the Krein / ghost-parity positivity-axis evasion of Distler-Garibaldi

> **Standing honesty boundary (binds every line below, including the acceptance-row table; the one-line row must never be quoted without this banner attached).**
> All kinematics cited here is exact and machine-checked: the Krein signature `(+96, -96, 0)` on the 192-dim self-dual triplet; net chiral asymmetry exactly `0` in every `p+q=14` signature, real and quaternionic; pseudo-anti-Hermiticity residual `0.0e+00`. Everything dynamical is **OPEN**, because GU supplies no built source action / S-matrix: that GU's dynamics realizes the ghost parity as a symmetry (`[P_ghost, S] = 0`), that any chiral selection actually fires, that GU's action is quadratic-gravity-like. This is a **TYPED CANDIDATE with one open dynamical condition**, not a proof that Distler-Garibaldi is evaded. Distler-Garibaldi's theorem hypotheses and its representation-theoretic conclusion (the matter rep is vectorlike) are **untouched and agreed**: the self-dual triplet that carries the generation is genuinely vectorlike, and we **reproduce** the D-G mirror obstruction rather than contradict it. What is contested is one hidden interpretive premise sitting under D-G assumption (5), not the theorem.

---

> **CORRECTION (A0 audit, 2026-06-28).** This candidate's central claim -- that the Krein / positivity move
> is a "first inside-the-single-group-class" shadow of Distler-Garibaldi -- is RETRACTED. By the Weyl
> unitarian trick a finite-dimensional representation of a compact group always admits an invariant
> positive-definite form, so the indefinite Krein form exists ONLY because the internal gauge group is
> taken NON-COMPACT (SO(5,5), not SO(10)). Dropping Hilbert positivity (Leg 7) is therefore logically the
> same move as negating DG assumption DG-A3 (compact internal G); Leg 3's claim to "preserve G compact" and
> Leg 7's "drop positivity" are the same step read twice and cannot both hold. The Krein datum is a
> SCOPE-EXIT (it joins DG-A1/A2/A6/A7 in `canon/no-go-class-relative-map.md`), not an inside-class
> enrichment. The kinematics below is unaffected; the typed-candidate and "inside-class" framing is
> downgraded to: a scope-exit whose favored outcome was already the kill.

## Lead (the sharp statement, fully hedged)

Distler-Garibaldi proves that no single real form of `E8` carries three chiral generations as a **complex** `G`-representation: any embedding makes the matter representation real, hence vectorlike. Every published escape leaves the single-group class (`E8 x E8`, `SO(3,11)`, `K(E10)`); the no-go-map records this as the stress case and states that "there is no known richer-substrate datum that lives inside single-E8 representation theory and reproduces three SM generations."

This candidate does not leave the class. It keeps GU's single finite-dimensional reconstruction (`Cl(p,q)`, `p+q=14`, the verified Pati-Salam `Spin(2k)` chain) and reproduces the obstruction exactly: the self-dual `SU(2)+` triplet that carries the generation is vectorlike, net chiral asymmetry `0` in every signature. It then names one premise D-G never states because it is universal background: that the fermion state space is a positive-definite **Hilbert** space, so that "vectorlike `G`-rep" forces "non-chiral physics." This premise is **not** the literal content of D-G assumption (5). Assumption (5) ("`V_{2,1}` is complex as a `G`-representation") is a statement about the **reality type** of a representation and is **inner-product-independent**; D-G's reality-type computation is left exactly intact. The premise actually dropped is the **unlisted** background identification `vectorlike G-rep ==> non-chiral physics`, which silently presupposes Hilbert positivity.

GU's matter module is not Hilbert. It is a **Krein** space: the `so(p,q)`-invariant form `K = eta_V (x) beta_S` is indefinite and pseudo-anti-Hermitian (`beta_S sigma + sigma^dagger beta_S = 0`, residual `0.0e+00`), and on the 192-dim triplet its signature is exactly `(+96, -96)`. Each generation is null-paired with its mirror in a hyperbolic pair. A `Z2` **ghost parity** (the generation-mirror swap) would split each pair into one positive-norm physical state and one negative-norm ghost; on a Krein space chirality **could** be a property of the physical (positive-norm, ghost-parity-even) subspace rather than of the whole `G`-rep, and the three mirrors **would** then be negative-norm ghosts rather than physical mirror fermions. Every clause of that last sentence is modal on purpose: whether the physical subspace is in fact chiral is the open dynamical condition, and (see the representation-theory crux below) index conservation makes the negative outcome the **favored** one absent extra symmetry-breaking data that only the unbuilt dynamics (or a base-manifold Dirac index) can supply.

The forgetful operation that makes D-G's null image reappear is therefore a **metric forgetting**, not a category collapse:

```
phi_Hilbert : (Krein module V(x)S, indefinite form K induced by the spacelike-gamma adjoint, ghost parity Z2)
              |-->  (underlying real Spin(10) G-rep, positive-definite metric imposed)
```

On the image of `phi_Hilbert` the triplet is `16 + 16bar`, net asymmetry `0`, `V_{2,1}` real: D-G's exact null answer. The datum `phi_Hilbert` deletes is the metric signature and the ghost parity. This is a genuine inside-the-single-group-class shadow, which is new relative to the no-go-map's category-change-only exits. It is **not** a refutation of the no-go-map's stronger claim: the map said no inside-class datum **reproduces three chiral generations**, and this candidate does **not** yet reproduce them. It converts that stress case from "no inside-class datum exists" to "here is one inside-class datum; whether it reproduces three chiral generations is the open dynamical question."

---

## 1. Acceptance summary (one-line row)

The template's standard contract row is L1-L6 plus the first falsification test. This candidate deliberately holds L1-L6 inside the Distler-Garibaldi class (most cells preserve all four no-goes); the entire evasive load is carried by a proposed seventh axis L7, appended. The row below is bound by the standing honesty boundary above and may not be read without it.

| candidate | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 coordination loop | L7 positivity (PROVISIONAL; see Sec. 3) | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Krein / ghost-parity inside-class candidate (D-G) | (l, menu ext.) finite-dim real Clifford/spinor module of a **single** real Lie group; **NOT** a spectral triple / bundle / product group [preserves D-G 1,4,6] | (a) finite quantum / BQP observer [preserves; the projector Born rule is booked at L7, not here] | (a) `so(p,q)`-invariant-form channel [preserves D-G 3] | (a) total-order Lorentzian [preserves D-G 2] | (a) specific-object substrate [preserves D-G 6,7] | (a) no loop, kinematic candidate [preserves; dynamical completion OPEN; targets (e) broken-`Z2`, (g) RG / quadratic-gravity flow] | Krein (indefinite-metric) state space + ghost-parity `Z2` superselection [**candidate** break of the positivity premise hidden under D-G 5, **contingent on the open `[P_ghost,S]=0` condition**] | Build a gauge-equivariant (`[P_ghost,G]=0`) ghost-parity-preserving (`[P_ghost,S]=0`) Krein-unitary (`S^dagger K S = K`) toy evolution on the 192-dim triplet; check the projector Born rule `p_i = Tr(P_{phys,i} S P_phys S^dagger)/Z` gives nonnegative `p_i` summing to 1, and whether the physical `+1`-eigenspace can carry **nonzero** net chirality. Index conservation makes the **kill** (net chirality forced back to 0) the favored outcome; a pass would only show finite-sector existence, not GU realization. |

No L1-L6 cell drops a class. That is what "inside-the-class" means: the candidate stays inside Distler-Garibaldi's single-finite-dimensional-group class and proposes a seventh assumption the six-axis menu did not name.

---

## 2. L1-L6 fillings

### Leg 1 — Substrate class

- **Class label:** **(l) — menu extension.** A finite-dimensional **real Clifford / spinor module of a single real Lie group**: GU's Rarita-Schwinger module realized as `Cl(p,q)`, `p+q=14`, on a `2^7 = 128`-dim real spinor module carrying the verified Pati-Salam `Spin(2k)` chain. This is explicitly **not** a Connes spectral triple, not a bundle, not a product group, and not a Kac-Moody object.
- **Justification for extending the menu:** Menu (a) ("smooth principal bundle on a smooth manifold") is the geometric Witten-class object; Distler-Garibaldi's actual class sits **below** L1 (a specific finite-dimensional real form, a specific representation type). A candidate intending to stay inside the D-G class must name that sub-L1 object explicitly rather than borrow the bundle slot, or it cannot record that it preserves D-G assumptions 1 and 6. We deliberately do **not** label the substrate a spectral triple: recasting it as a Connes spectral triple is the "change the unit" move the no-go-map flags (Sec. 2.4) as a category change that leaves the single-group class, and it would forfeit the inside-class claim that is this candidate's entire reason to exist. The machine-checked object is a real Clifford module with an indefinite invariant form; it is **not** an established spectral triple (no built Dirac / source action satisfying the spectral-triple axioms is demonstrated).
- **Specification:** `ker(Gamma) = 1664 = 2^7 * 13`, decomposing under the GU-forced self-dual `SU(2)+` (rank-3 `Lambda^2_+` of any 4-base) as `640` singlets `+ 416` doublets `+ 64` triplets; the 192-dim triplet sector carries the pure `Spin(10)` generation spinor (`16/16bar`, Casimir `-11.25` exact). No product group, bundle, or Kac-Moody extension is added; only an invariant metric (booked at L7) is placed on the same rep content D-G takes as input.
- **Literature anchor:** Atiyah, Bott & Shapiro, "Clifford modules," *Topology* 3 (Suppl. 1, 1964); Lawson & Michelsohn, *Spin Geometry* (Princeton, 1989) for the real Clifford-module classification; Distler & Garibaldi, "There is no 'Theory of Everything' inside E8," *Comm. Math. Phys.* 298 (2010) 419, arXiv:0905.2658, for the class preserved. Reconstruction basis: `draft-papers/multiplicity-theorem-note-2026-06-28.md`.
- **Class-assumption signature:** **Preserves** Distler-Garibaldi assumptions 1 (single real form), 4 (low-spin matter, `m+n <= 4`: the generation lives in the low-spin self-dual triplet), and 6 (finite-dimensional representation theory of one group). The candidate does **not** leave the single-group class here.

### Leg 2 — Observer class

- **Class label:** (a) Finite Turing / quantum (BQP) observer, the implicit baseline. Kept at pure baseline.
- **Specification:** The observer that reads invariants off the module is the standard finite quantum observer; no hypercomputation, oracle, or QRF enrichment is invoked. The generalized (projector) Born rule that recovers probabilities from the indefinite metric is **not** an observer-class change and is **not** booked here; it is a probability rule attached to the Krein metric and is booked entirely under L7. Booking it here would double-count the single load-bearing novelty across two axes and smear the one dropped assumption, breaking the discipline that defines "inside-class."
- **Literature anchor:** Nielsen & Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), as the baseline finite-quantum-observer class. No candidate-specific literature.
- **Class-assumption signature:** **Preserves all four.** Distler-Garibaldi is observer-independent; this candidate keeps it so and does not cheat with an oracle.

### Leg 3 — Pairing

- **Class label:** (a) `so(p,q)`-invariant-form channel (tensor-product / contraction pairing).
- **Specification:** The observer pairs with the substrate through the `so(p,q)`-invariant form `K = eta_V (x) beta_S`, where `beta_S` is the spinor adjoint induced by the product of the spacelike gammas (`beta_S^2 = I`, `beta_S sigma + sigma^dagger beta_S = 0`). The **channel** (how the observer contracts against the module) is the standard invariant-form pairing and is unchanged. The **signature** of the induced form is deliberately factored out into L7; see Sec. 3 for the explicit argument that this factoring is the contested move (and for the conservative reading under which L7 is simply this Leg with its signature made explicit).
- **Literature anchor:** Lawson & Michelsohn, *Spin Geometry* (1989), Ch. I, for invariant bilinear forms on real spinor representations. (The Krein-form realization itself is anchored at L7, not here, to avoid re-typing the substrate.)
- **Class-assumption signature:** **Preserves** Distler-Garibaldi assumption 3 (internal `G` compact, centralizing the Lorentz factor; the standard invariant pairing through which D-G's branching is computed).

### Leg 4 — Causal-order class

- **Class label:** (a) Total-order Lorentzian (smooth manifold, Cauchy slicing).
- **Specification:** The candidate is a statement about the matter Krein module's kinematics over GU's standard 4-base; it makes no causal-order claim. The base is an ordinary smooth (pseudo-)Riemannian 4-manifold whose bundle of self-dual 2-forms `Lambda^2_+` (rank 3) supplies the `SU(2)+` family symmetry; `p - q = 4` retains a Lorentzian base and the `SL(2,C)` spin structure. Total order and Cauchy slicing are untouched.
- **Literature anchor:** Atiyah, Hitchin & Singer, "Self-duality in four-dimensional Riemannian geometry," *Proc. R. Soc. Lond. A* 362 (1978) 425, for the rank-3 `Lambda^2_+` self-dual structure that forces the `SU(2)+` triplet.
- **Class-assumption signature:** **Preserves** Distler-Garibaldi assumption 2 (`SL(2,C) ⊂ E` Lorentz embedding). No causal-order drop, and no causal-set / branching-DAG escape is smuggled in.

### Leg 5 — Emergence class

- **Class label:** (a) Specific-object substrate (00d default).
- **Specification:** The substrate is the specific `Cl(p,q)` reconstruction with its fixed `Lambda^2_+` triplet, not an RG universality class, attractor, or topological-phase representative. The generation count 3 is latent in the specific self-dual geometry (the `SU(2)+` triplet multiplicity), not emergent from a coarse-graining attractor. Which half of each hyperbolic pair becomes physical is set by the ghost parity plus dynamics, not by a fixed-point selection; that selection is the open condition, not an emergence-class phenomenon. (There is a tempting but non-load-bearing analogy to SPT edge-mode selection, menu (e); it is flagged and not used, to avoid overclaiming.)
- **Literature anchor:** None candidate-specific; Distler & Garibaldi 2009 (arXiv:0905.2658) is itself the specific-object reference.
- **Class-assumption signature:** **Preserves** Distler-Garibaldi assumptions 6 (one specific finite-dimensional object) and 7 (no compactification/flux/bundle data added). No emergence drop; the candidate does not buy chirality from emergence.

### Leg 6 — Coordination-loop class

- **Class label:** (a) No loop (00d implicit baseline) **for the kinematic candidate**, with explicitly named completion targets (e) Ising / spin-glass broken-`Z2` selection, and (g) RG / quadratic-gravity (higher-derivative) flow.
- **Specification:** As a typed kinematic object the candidate has no substrate-observer feedback loop: the Krein structure, the hyperbolic (generation, mirror) pairing, and the ghost-parity `Z2` all exist as fixed linear-algebraic data the observer reads off. The chiral **selection** of the physical half of each hyperbolic pair is **not** fixed by kinematics; making it canonical requires a ghost-parity-preserving dynamics whose flow selects the physical half. If such a dynamics materializes, its natural homes are broken-`Z2` selection (menu (e)) or higher-derivative / quadratic-gravity RG flow (menu (g)). This is the candidate's single open condition and is named here so the gap stays visible rather than hidden inside another axis.
- **Literature anchor:** Stelle, "Renormalization of higher-derivative quantum gravity," *Phys. Rev. D* 16 (1977) 953, for the higher-derivative dynamics in which a ghost parity is native; Lee & Wick, "Negative metric and the unitarity of the S-matrix," *Nucl. Phys. B* 9 (1969) 209, for indefinite-metric S-matrix dynamics. Open dynamical completion basis: Turok & Bateman (2026), Krein-space generalized Born rule for quadratic gravity (**unpublished TOE interview, June 2026; not a citable paper**; `canon/ghost-parity-krein-synthesis.md` external_ref).
- **Class-assumption signature:** **Preserves** Distler-Garibaldi (no-loop, no added dynamics) **at the kinematic level**. The dynamical completion is the candidate's open condition and is **not** asserted.

---

## 3. Leg 7 (PROVISIONAL) — state-space positivity / metric axis

- **Class label:** Krein (indefinite-metric) state space with ghost-parity `Z2` superselection. The state space is not a Hilbert space but a Krein space `(V(x)S, K)` with `K` indefinite; a discrete ghost parity `Z2` would resolve each hyperbolic null pair into a positive-norm (physical) and a negative-norm (ghost) eigenspace, and a projector / generalized Born rule would recover positive probabilities summing to 1 **provided the parity commutes with the dynamics**.
- **Specification:** Restricted to the 192-dim triplet sector, `K` has signature exactly `(+96, -96, 0)` in `(9,5)`, `(7,7)`, and `(14,0)`. Each chirality half is totally null; the form is purely the cross-pairing between a generation and its mirror, so the 96 states organize as 96 hyperbolic pairs `{u,v}` with `<u,v> != 0` and norms `+/- 2<u,v>` on `u +/- v`. The ghost parity swaps `u <-> v` (generation `<->` mirror); its even / odd eigenspaces would label physical vs ghost. **Important convention note:** `beta_S` here is the adjoint induced by the product of the **spacelike** gammas; this is a **choice**. The timelike-gamma adjoint yields a different invariant form, and the synthesis itself concedes the physical/ghost split is basis-dependent. So `(+96, -96)` and the physical/ghost assignment are **convention/basis-dependent**, not canonical; the ghost parity is exactly the extra datum that would fix the split, and it is canonical only if the dynamics realizes it as a symmetry.
- **Literature anchor:** Bognár, *Indefinite Inner Product Spaces* (Springer Ergebnisse 78, 1974); van den Dungen, "Krein spectral triples and the fermionic action," *Math. Phys. Anal. Geom.* 19 (2016) 4, arXiv:1505.01939 (cited here as the anchor for the **indefinite invariant form on spinors**, not as a re-typing of the substrate into the spectral-triple category); Pauli, "On Dirac's New Method of Field Quantization," *Rev. Mod. Phys.* 15 (1943) 175, and Nakanishi, *Prog. Theor. Phys. Suppl.* 51 (1972), for indefinite-metric QFT; Lee & Wick, *Nucl. Phys. B* 9 (1969) 209; Stelle, *Phys. Rev. D* 16 (1977) 953; Turok & Bateman (2026) generalized Born rule (**unpublished interview source**). Note: indefinite-metric / Lee-Wick unitarity is delicate (causality and contour subtleties at the ghost scale); even the conditional positivity statement is presented as cleaner than the literature settles.
- **Class-assumption signature:** **Candidate break of the positivity premise hidden under Distler-Garibaldi assumption 5, contingent on the open `[P_ghost, S] = 0` condition.** D-G 5 ("`V_{2,1}` is complex as a `G`-representation") is a reality-type statement and is **inner-product-independent**; we leave it and D-G's computation exactly intact. The premise dropped is the **unlisted** background identification `vectorlike G-rep ==> non-chiral physics`, which presupposes a positive-definite Hilbert state space so that chirality must be a property of the entire `G`-rep. On a Krein state space chirality **could** be a property of the physical (positive-norm, ghost-parity-even) subspace; this is a candidate break, fired only if the open dynamical condition holds. It breaks **no** assumption of Witten, Nielsen-Ninomiya, or Freed-Hopkins: those theorems are simply not the target here (we do **not** claim they also assume Hilbert positivity).

### Is this a genuine new axis, or a sharpening of Leg 3? — explicit resolution

**The case for a genuinely new axis.** Leg 3 as menued names the **channel/coupling** (Cartesian, superdeterministic, IIT-partition, protocol-class, and so on); none of its entries carries the **signature** of the resulting inner product or the discrete datum that resolves an indefinite one. Two candidates can share an identical Leg-3 channel (the same contraction `eta_V (x) beta_S`) yet differ on whether the induced form is positive-definite or indefinite, and on whether a ghost-parity superselection is needed to recover probabilities. A Euclidean signature gives a definite metric and no ghosts; `q > 0` gives the indefinite `(+96, -96)`; the ghost parity `Z2` is extra data not determined by the channel at all. That difference is exactly what decides whether the hidden positivity premise holds, and it is invisible in the Leg-3 menu. On this reading L7 is a separate degree of freedom, and giving positivity its own axis is what isolates the single dropped assumption instead of burying it inside a pairing tuple.

**The conservative reading (and the primary bookkeeping we adopt).** The inner product **is** the output of the pairing; its signature is arguably a **parameter of** Leg 3, exactly as `(k, alpha, beta)` parameterize the metastable-consensus pairing (3f). On this view L7 is not an independent seventh axis but a **signature-refinement of Leg 3**: "Leg 3 with its inner-product signature and any superselection structure made explicit."

**Resolution.** We **present** the positivity content under an L7 heading, for the epistemic-hygiene reason that isolating positivity is what converts the evasion from prose into a single, checkable assumption-drop. But we adopt the **conservative reading as the primary bookkeeping**: until a discriminating second candidate exists, L7 is recorded as **provisional**, and its canonical home is "Leg 3, signature-refined," **not** an asserted-independent seventh axis. **Justification:** parsimony. The independence claim is only certified by producing a second candidate that varies the state-space signature while holding the Leg-3 channel fixed (or vice versa); no such candidate yet exists, so we cannot certify independence and we do not assert it. The discriminating test is named here as the condition under which L7 would be promoted from "Leg-3 signature-refinement" to "independent seventh axis."

---

## 4. Chirality-bridge claim

The substrate invariant that **would** carry chirality is the ghost-parity-even, positive-norm subspace of the self-dual `SU(2)+` triplet: the `+1`-eigenspace of the generation-mirror swap `Z2` inside the `(+96, -96)` Krein triplet. The forgetful operation is `phi_Hilbert : (Krein module, indefinite form K, ghost parity Z2) |--> (underlying real Spin(10) G-rep, positive-definite metric imposed)`; it discards the metric signature and the ghost parity, retaining only the bare real `Spin(10)` rep content. On the image of `phi_Hilbert` the triplet is `16 + 16bar`, net chiral asymmetry exactly `0` in every `p+q=14` signature, `V_{2,1}` real, which **is** the Distler-Garibaldi mirror obstruction; so D-G computes correctly, on a shadow that has already thrown away the positivity datum that would distinguish a physical generation from a negative-norm ghost. Unlike the no-go-map's category-changing `phi_singleE8` (bundle / Kac-Moody / product-group exits that leave the class), `phi_Hilbert` is a genuine metric-forgetting shadow that stays inside the single-group class. Two caveats bind this paragraph. First, every chirality clause is modal: the physical subspace **would** be chiral only if a ghost-parity-preserving (or base-topology / Dirac-index) selection fires, which is the open condition, and the representation-theory crux below makes the non-chiral outcome the favored one. Second, the bridge does **not** yet reproduce three chiral generations; kinematically the physical half is a mirror-symmetric `3 x 2 x 16` sector with net chiral asymmetry `0`, and labeling it "three generations" would presuppose exactly the selection that is open.

### Representation-theory crux (the index-conservation expectation)

For the physical subspace to be a `G`-representation at all, the ghost parity must commute with the gauge group: `[P_ghost, G] = 0`. But a `G`-equivariant identification swapping the generation `16` with its mirror `16bar` is precisely (a real form of) the **reality structure** on `V_{2,1}`, and the existence of exactly such a structure is what Distler-Garibaldi **use** to certify that the rep is vectorlike. So the same `Z2` invoked to select a chiral half is, when `G`-equivariant, the very object certifying non-chirality: its `+1`-eigenspace fixes the `16` only up to `16 <-> 16bar` conjugation, and therefore carries net chiral asymmetry `0` under any `G`-equivariant map. This is an index-conservation argument: a Krein-unitary `S` on a fixed finite-dimensional space cannot move an index, and the chirality of the physical sector is fixed by the **choice** of `P_ghost` (its `+1`-eigenspace), not by `S`. Consequently the physical subspace is chiral **only if** an extra symmetry-breaking datum breaks the `G`-equivariant generation-mirror identification, and that datum can come only from the open dynamics or from a base-manifold Dirac index. Net: the candidate's own kill condition (net chirality forced back to `0`) is the **expected** outcome, not a coin flip, and "physical subspace is chiral" is a conditional whose antecedent is the open dynamical leg, never an established fact.

---

## 5. First falsification test

**Class-assumption tested.** Whether the L7 candidate-break of D-G's hidden positivity premise can survive a gauge-equivariant dynamics, or whether it is killed kinematically by index conservation.

**Construction (runnable now by an agent linear-algebra pass; numpy/sympy; no GU source action required, which is the point). Extends `tests/generation-sector/ghost_parity_krein.py`; reuse its guards (anchors `||[Pi_RS, M_D]|| = 58.7215`, `C2 = 155.3625`, pseudo-anti-Hermiticity residual `0.0e+00`).**

1. Build the 192-dim triplet sector and the restricted Krein form `K` with verified signature `(+96, -96, 0)`.
2. Construct `P_ghost`, the projector onto the ghost-parity-even (positive-norm) subspace, as the `+1`-eigenspace of the generation-mirror swap, and verify the **gauge-equivariance** requirement `[P_ghost, G] = 0` for the gauge group `G` acting on the triplet. (This step is the load-bearing kinematic check and is decidable **now**.)
3. **Kinematic half (decidable now).** With `[P_ghost, G] = 0` imposed, ask whether **any** physical (`+1`-eigenspace) subspace can carry **nonzero** net chirality at all. The representation-theory crux predicts **no**: a `G`-equivariant generation-mirror swap is a reality structure, so its eigenspaces carry net index `0`. If this prediction holds, the candidate is killed before the dynamical question is even reached.
4. **Dynamical half (open, blocked on GU's unbuilt source action).** Among the Krein-unitary evolutions `S` (those satisfying `S^dagger K S = K`, the only evolutions a Krein space admits), extract the subset with `[P_ghost, S] = 0`. For a basis of one-parameter subgroups `S = exp(tX)` in that subset, evaluate the projector Born rule `p_i = Tr(P_{phys,i} S P_phys S^dagger) / Z` and check the `p_i` are real, nonnegative, and sum to 1 over exactly 3 physical generations (not 6).

**Verdict logic.** Chirality is a property of the chosen `P_ghost`'s `+1`-eigenspace, not something `S` can change, so the live question is **existence**: does there exist a gauge-equivariant ghost parity whose physical eigenspace is net-chiral **and** admits a commuting Krein-unitary dynamics? Index conservation makes the **kill** (every `G`-equivariant, ghost-parity-preserving configuration re-symmetrizes generation and mirror and forces net chirality back to `0`) the **favored** outcome; the pass-branch may be structurally **empty**, in which case the test is a guaranteed kill, independent of GU's unbuilt S-matrix. A **pass** would demonstrate only finite-sector existence of a gauge-equivariant, ghost-parity-preserving, chirality-retaining Krein evolution; it would **not** show that GU's actual (unbuilt, plausibly quadratic-gravity-like) source action realizes such an `S` with `[P_ghost, S] = 0`, and it would **not** supply the base-manifold-topology / Dirac-index route the synthesis names as the other (arguably primary) chiral-selection mechanism. **Runner:** agent computational pass (the kinematic half and the toy-existence half); GU-dynamics specialist (the confirmation half, blocked on the unbuilt source action).

---

## 6. Honest status (mirrors the no-go-map honesty contract)

This is a **typed candidate, kinematically exact and dynamically open**. It does not assert that Distler-Garibaldi is evaded, and it does not claim GU is vindicated. Distler-Garibaldi's hypotheses and its representation-theoretic conclusion (the rep is vectorlike) are agreed and untouched; we reproduce the mirror obstruction rather than contradict it. What the candidate contributes is precise:

- the **precise new (provisional) axis**: state-space positivity (Hilbert vs Krein), recorded conservatively as a signature-refinement of Leg 3 until a discriminating second candidate certifies independence;
- the **precise forgotten datum**: `phi_Hilbert`, which deletes the (convention-dependent) Krein metric and the ghost parity;
- the **precise dropped premise**: not the literal content of D-G assumption 5, but the unlisted background identification `vectorlike G-rep ==> non-chiral physics`, which presupposes Hilbert positivity;
- the **precise open condition**: a gauge-equivariant, ghost-parity-preserving dynamics `[P_ghost, G] = 0`, `[P_ghost, S] = 0`, plausibly quadratic-gravity-like, realized by GU's unbuilt source action, against which index conservation makes the kill condition the favored outcome.

It converts the no-go-map's hardest stress case from "no inside-the-class datum exists" to "here is one inside-the-class metric-forgetting shadow; whether its dynamical realization reproduces three chiral generations is the open question." It does **not** refute the no-go-map's stronger claim that no inside-class datum reproduces three SM generations: that remains open and unrefuted. Per the no-go-map's own posture, this candidate is shipped with its stress visible, not papered over.
