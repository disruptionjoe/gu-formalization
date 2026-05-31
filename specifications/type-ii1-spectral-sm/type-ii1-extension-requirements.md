# Type II_1 / Non-Embeddable Extension — Additional Structural Requirements

**Purpose.** The companion file `connes-finite-control-checklist.md` walks the ten items the finite Connes-Chamseddine spectral Standard Model already satisfies and names, item by item, what a Type II_1 extension must preserve. This file collects the **additional structural requirements** that the Type II_1 / non-embeddable regime introduces — items the finite case does not have to deal with at all — and the open questions specific to the non-embeddable subregime.

**Scope.** This is again a requirements checklist, not a construction. Each requirement is stated with the reason it appears (what feature of the Type II_1 / non-embeddable regime forces it), the natural mathematical candidate that addresses it, and the published-record status.

**Status conventions.**
- **[required]** = the Type II_1 extension cannot be coherent without addressing this.
- **[candidate]** = a natural mathematical candidate addressing the requirement.
- **[open]** = whether the candidate works is not closed in the published record.

## R1 — Tracial state and Murray-von Neumann dimension theory

**[required]** A Type II_1 factor `M` carries a unique faithful normal tracial state `τ`, normalized so that `τ(1) = 1`. The projections of `M` have continuous dimension `τ(p) ∈ [0, 1]` (Murray-von Neumann dimension), not integer dimension. Any quantity in the finite spectral SM that was a discrete dimension count (number of fermion modes, dimension of Hilbert subspaces) becomes a real-valued trace quantity in the Type II_1 extension.

**[candidate]** Use `τ` to define the analog of all dimension quantities. Specifically:

- The fermion count "16 per generation" becomes `τ(p_generation) = 16 · u` for some fundamental unit `u`.
- The Hilbert-space dimension of internal sectors becomes `τ`-dimension of bimodule projections.
- The spectral action `Tr(f(D/Λ))` becomes `τ(f(D/Λ))`.

**[open]** Whether the integer constraints of the finite case (fermion count, KO-dimension multiplicity, gauge-group rank) all factor through the tracial state cleanly is open. Some integers are likely topological (KO-dimension mod 8 is a topological invariant, not a dimension count), and so persist under tracialization unchanged. Other integers may dissolve into real-valued trace quantities, in which case the constraint they imposed is lost.

## R2 — Breuer-Fredholm index theory

**[required]** In the finite case, the Dirac operator's chirality content is captured by an integer-valued index: `index(D_+) = dim ker D_+ − dim ker D_−`. In the Type II_1 case, the operator `D` is τ-Fredholm rather than Fredholm, and its index is the **Breuer-Fredholm index** taking values in `R` (real numbers) rather than `Z`.

**[candidate]** Use Breuer-Fredholm index in place of ordinary index. This is the standard semifinite analog and is well-developed (Carey-Phillips-Rennie-Sukochev). The chirality content of the Type II_1 internal Dirac operator is captured by `τ-ind(D_+) = τ(P_{ker D_+}) − τ(P_{ker D_−})`.

**[open]** Two related questions.

1. Does the Breuer-Fredholm index of the Type II_1 internal Dirac operator land on integer values (recovering the finite case), on rational values (encoding fractional-mode structure), or on irrational values (signaling genuinely non-finite-approximable content)?
2. The non-embeddable subregime is precisely the regime where finite-dimensional approximation fails. If the Breuer-Fredholm index can be irrational only when the factor is non-embeddable, that would be a clean indicator of *what the non-embeddable regime contributes that the embeddable Type II_1 case does not*. No published paper has studied this.

## R3 — Semifinite spectral triple framework

**[required]** Spectral triples over a Type II_1 factor are **semifinite spectral triples** in the sense of Benameur-Fack and Carey-Phillips-Rennie-Sukochev: the algebra `A` is a τ-Fredholm-friendly subalgebra of a semifinite von Neumann algebra `(M, τ)`, the Hilbert space carries a faithful normal representation of `M`, and the Dirac operator `D` has τ-compact resolvent. The local index formula and Chern character are expressed via the resolvent cocycle.

**[candidate]** The Benameur-Fack and Carey-Phillips-Rennie-Sukochev framework is the natural mathematical setting. The semifinite local index formula has been proven.

**[open]** Embedding the *Standard Model–shaped* product structure (`C∞(M) ⊗ A_F` replaced by `C∞(M) ⊗ A_M` with `A_M` a Type II_1 algebra) into the semifinite spectral-triple framework, with real structure and grading, and verifying that the resulting object satisfies all of Connes' spectral-triple axioms in their Type II_1 analogs, has not been done in the published record.

## R4 — Reality and KO-dimension in the semifinite setting

**[required]** The finite SM critically uses KO-dimension 6 (mod 8) for chirality and the reality structure `J`. A semifinite analog needs:

- A definition of KO-dimension for a semifinite spectral triple.
- Verification that the mod-8 periodicity carries over.
- Specification of `J` (antiunitary) and `γ` (grading) on the Type II_1 Hilbert module with the right commutation signs.

**[candidate]** Two paths.

- *Approximant path.* Define KO-dim via finite-dimensional approximants in the trace-preserving inclusion chain `A_F^(n) → A_F` (when `A_F` is approximately finite-dimensional). This works only if `M` is embeddable; it fails for non-embeddable factors by construction.
- *Cyclic-cohomology path.* Define KO-dim via the Hochschild / cyclic-cohomology characters of the spectral triple, which are intrinsic to the Type II_1 data and do not require approximation. This is the candidate that has a chance in the non-embeddable case.

**[open]** Both paths are open. The cyclic-cohomology path is the more interesting one for the non-embeddable subregime, but the corresponding signs and mod-8 structure have not been worked out in the published record.

## R5 — Subfactor inclusion and principal-graph data

**[required]** The lead candidate frame from the deep-research brief uses a **Jones-subfactor inclusion** `N ⊂ M` of finite Jones index `[M : N]`, with the **principal graph** of the inclusion conjectured to carry generation structure. The principal graph is a bipartite graph encoding the fusion data of `M`-`N`, `N`-`N`, `M`-`M`, and `N`-`M` bimodules generated by basic-construction iteration. For finite-depth inclusions, the principal graph is finite and the standard invariant is a finite **fusion category**.

**[candidate]** Specify a candidate inclusion. The lead conjecture from the WRK-375 example specification is that an appropriate inclusion (with index near the Jones-Wenzl values 4 cos²(π/n), or one of the exceptional Haagerup-Asaeda subfactors) has principal-graph data that carries 3-generation structure. Subfactor classification (Popa's classification, Evans-Kawahigashi's recent survey) provides candidate inclusions.

**[open]** Major open question. Evans-Kawahigashi (2023) survey makes clear that subfactor / planar-algebra technology produces fusion categories. **The Standard Model gauge group does not have its representation theory as a finite fusion category**, which suggests the natural reading "principal graph = generation structure" is not straightforward. Either (a) the principal graph encodes only the *generation count*, not the full gauge representation theory (gauge structure comes from a different part of the data); or (b) the candidate inclusion would have to be non-finite-depth, in which case the standard invariant is no longer a finite fusion category; or (c) the conjecture is wrong and there is no subfactor-based generation mechanism. The published record does not select among these.

## R6 — Non-embeddable separation: what the non-embeddable regime contributes

**[required]** A coherent Type II_1 extension that uses *only* the hyperfinite (= embeddable, approximately finite-dimensional) II_1 factor `R` would be a *strict* extension of the finite case but would not load on MIP* = RE. The non-embeddable subregime — factors `M` such that the standard ultrapower `M^ω` cannot embed into the ultrapower of `R` — is unavoidable only after MIP* = RE (Ji-Natarajan-Vidick-Wright-Yuen 2020) ruled out the Connes embedding conjecture.

The Type II_1 spectral SM pathway is interesting *as a substrate-level proposal* (in the gu-formalization six-axis frame) precisely because the non-embeddable regime is where genuinely new operator-algebraic content lives. The extension must therefore specify **what the non-embeddable regime contributes that an embeddable Type II_1 extension would not**.

**[candidate]** Two candidate contributions, both speculative.

- *Index spectrum.* Non-embeddable factors may carry Breuer-Fredholm indices at values not realized by any embeddable factor. If the Standard Model fermion content requires such an index value, only the non-embeddable regime delivers it.
- *Standard invariants beyond fusion categories.* The standard invariant of a subfactor in a non-embeddable factor is not constrained to be a fusion category in the same way as in the hyperfinite case. New algebraic data structures could appear that have no finite-dimensional analog.

**[open]** Both candidates are speculative and have no published instance. Goldbring (2021) studies non-embeddable II_1 factors structurally but does not connect them to noncommutative-geometry model building. Cabello-Quintino-Kleinmann (2023) discusses physical implications of MIP* = RE but does not touch spectral triples or the Standard Model.

This requirement is what makes the **non-embeddable** subregime distinct from the embeddable Type II_1 subregime. If no specific contribution of the non-embeddable regime can be identified, the pathway should be re-scoped to use hyperfinite II_1 only, and the MIP* = RE motivation is decorative rather than load-bearing.

## R7 — Recovery of finite-case results in the appropriate limit

**[required]** Any Type II_1 extension must recover the finite Connes-Chamseddine results in an appropriate limit (typically: take the inclusion chain `A_F^(n) → A_F → M` and verify that the spectral action, fermion content, gauge-group recovery on `A_F^(n)` reproduce the finite-case results, with the full Type II_1 structure as the `n → ∞` limit). Without this recovery, the extension is decoupled from observable physics and is not a generalization of the finite case but a different theory.

**[candidate]** Standard inductive-limit construction. For the embeddable subregime, the inductive limit makes sense in the AFD framework. For the non-embeddable subregime, the inductive limit construction fails by definition; an alternative limit (free-product, ultrapower, or non-standard limit) must be specified.

**[open]** What recovery in the limit looks like for non-embeddable factors is the structural obstacle to the non-embeddable subregime. If recovery requires embeddability, the non-embeddable case is incompatible with this requirement and the pathway has to be either restricted to hyperfinite II_1 or to provide an alternative recovery mechanism.

## R8 — Spectral-action convergence and renormalization

**[required]** The spectral action `τ(f(D/Λ))` on the Type II_1 product spectral triple must converge in the heat-kernel expansion and yield a finite, renormalizable bosonic Lagrangian. Convergence is non-trivial because τ-compact resolvents in Type II_1 settings have different spectral asymptotics than compact resolvents in finite-dimensional settings.

**[candidate]** Use the Chattopadhyay-Pradhan-Skripka (2023) framework for τ-compact-resolvent spectral actions. Their result extends perturbation theory of the spectral action to semifinite von Neumann algebras with τ-compact resolvent.

**[open]** Chattopadhyay-Pradhan-Skripka (2023) does not address the almost-commutative product structure or the recovery of the SM Lagrangian. Whether their framework, combined with the Type II_1 internal data of R5, gives a convergent and renormalizable bosonic SM Lagrangian is open and is the natural target of the first technical paper a specialist would write in this direction.

## R9 — Twisted spectral triples (Connes-Moscovici) as a fallback

**[required, conditional]** Connes-Moscovici (2006) introduced **twisted σ-spectral triples** to handle cases where ordinary commutators `[D, a]` are not bounded after non-central perturbations. The Type II_1 setting may force a twisted-spectral-triple framework if the ordinary commutator condition cannot be preserved.

**[candidate]** If the Type II_1 Dirac operator does not satisfy bounded-commutator conditions with the algebra, fall back to twisted-spectral-triple data `(A, H, D, σ)` with σ a regular automorphism such that the twisted commutator `[D, a]_σ := D a − σ(a) D` is bounded.

**[open]** Whether the Type II_1 SM construction forces a twisted framework, or can stay within ordinary spectral-triple language, is open. Connes-Moscovici demonstrated the twisted framework arises naturally in Type III settings; it is not currently known whether Type II_1 / non-embeddable internal algebras force it as well.

## R10 — Mathematical compatibility with the six-axis frame

**[required]** This pathway is `pathway A` in the WRK-375 six-axis frame and is the **single-axis-heterodox** sextuple (L1 = Type II_1 spectral triple; L2-L6 inherit defaults: finite Turing observer, Cartesian smooth pairing, total-order Lorentzian, specific-object emergence, no coordination loop). The Type II_1 extension must be coherent under this sextuple, in particular:

- *L2 / observer.* The observer is a finite Turing (BPP/BQP) computational agent. It sees only finite-dimensional approximants of `M`. In the non-embeddable subregime, finite-dimensional approximants do not converge to `M` (that is what non-embeddability means). The observer therefore literally cannot see the structure that distinguishes a non-embeddable factor from a hyperfinite one. This is internally consistent with the substrate-level invariant claim — the substrate carries content the observer cannot extract — but it means the extension must specify what the observer *does* extract (presumably: the hyperfinite-truncation image, which recovers a finite or hyperfinite spectral SM).
- *L3 / pairing.* Cartesian-smooth Connes-channel coupling is preserved. This is the spectral-action pairing.
- *L4-L6 / causal order, emergence, coordination loop.* Inherit defaults; no requirement beyond the standard product spectral triple over a smooth Lorentzian 4-manifold.

**[candidate]** State all six axes explicitly in the public artifact and note that the candidate is single-axis-heterodox by design. This keeps the surface for specialist disagreement small.

**[open]** Whether the single-axis-heterodox sextuple is the optimal one for the Type II_1 pathway, or whether a multi-axis variant (e.g., L1 = Type II_1 + L5 = universality-class emergence) is more natural, is a downstream question.

---

## Summary table

| # | Requirement | Source of requirement | Candidate addressing it | Open status |
|---|---|---|---|---|
| R1 | Tracial state and Murray-von Neumann dimension | Type II_1 factors carry continuous trace, not integer dimension | Reframe all dimension counts as `τ`-values | Integer constraints may dissolve |
| R2 | Breuer-Fredholm index | Type II_1 Dirac operators are τ-Fredholm, not Fredholm | Carey-Phillips-Rennie-Sukochev framework | Real- vs integer-valued indices unsettled; non-embeddable separation unknown |
| R3 | Semifinite spectral triple framework | Spectral-triple axioms must extend to Type II_1 | Benameur-Fack + Carey-Phillips-Rennie-Sukochev | SM-shaped instance not constructed |
| R4 | Reality and KO-dimension semifinite analog | Chirality requires `J`, `γ`, KO-dim 6 (mod 8) | Cyclic-cohomology character path | Mod-8 periodicity for Type II_1 not worked out |
| R5 | Subfactor inclusion and principal graph | Lead candidate frame for generation structure | Jones subfactor + Popa classification + Evans-Kawahigashi | SM gauge group is not a finite fusion category; mechanism unsettled |
| R6 | Non-embeddable separation contribution | MIP*=RE motivation requires non-embeddable to do work | Index-spectrum or beyond-fusion-category candidates | Both speculative; no published instance |
| R7 | Recovery of finite case in limit | Theory must reduce to known SM | Inductive-limit construction (embeddable) or alternative limit | Non-embeddable case has no natural recovery limit |
| R8 | Spectral-action convergence | τ-compact resolvent vs compact resolvent asymptotics | Chattopadhyay-Pradhan-Skripka 2023 | SM-Lagrangian recovery not done |
| R9 | Twisted spectral triple fallback | Bounded-commutator condition may fail | Connes-Moscovici σ-spectral triples | Whether Type II_1 forces twisted framework unknown |
| R10 | Six-axis compatibility | Pathway is single-axis-heterodox in WRK-375 frame | State the sextuple explicitly | Sextuple choice may not be optimal |

## What separates the embeddable from the non-embeddable subregime

This is the load-bearing distinction for whether the pathway loads on MIP* = RE or not.

- **Embeddable subregime** (hyperfinite II_1 factor `R` or factors embeddable into `R^ω`). Most of R1-R5 and R7-R10 are addressable by existing machinery extended naturally. The KO-dimension question (R4) is the hardest item. The pathway in this subregime is a **strict generalization of the finite Connes-Chamseddine SM** with continuous-trace dimension data, which may or may not have SM-relevant content but does not rely on MIP* = RE for its motivation.
- **Non-embeddable subregime** (factors not embeddable into `R^ω`, witnessed by MIP* = RE). Items R6 and R7 become load-bearing obstacles. The pathway is interesting in this subregime only if non-embeddable factors carry SM-relevant content that embeddable factors do not. No published instance demonstrates this. The MIP* = RE motivation is genuinely physical (Cabello-Quintino-Kleinmann 2023), but the bridge from physical motivation to a spectral-SM construction is currently a leap of faith.

A specialist contributor should expect to do the embeddable case first (where the machinery is more complete) and only attack the non-embeddable case after the embeddable case is closed, since the embeddable case is a strict prerequisite for any non-embeddable construction.

---

## Contributor questions for operator-algebra / NCG specialists

These are the short questions the artifact should leave the public repo with, for outreach to specialists who could either close the pathway or open the next sub-problem.

1. **KO-dimension for semifinite spectral triples.** Is there a published or conjectural definition of KO-dimension for a semifinite spectral triple `(A, H, D)` over a Type II_1 factor `M`, such that the mod-8 periodicity and the chirality-bearing role of KO-dim 6 in the finite case carry over? If not, what is the natural obstruction?

2. **Real structure on Type II_1 spectral triples.** What is the natural antiunitary `J` and grading `γ` on a Type II_1 Hilbert module compatible with the tracial state, and do the KO-dim-6 commutation signs `(J² = 1, JD = DJ, Jγ = −γJ)` survive in a meaningful form?

3. **Subfactor principal graphs and generation structure.** Is there a specific Jones-subfactor inclusion `N ⊂ M` of finite index whose principal-graph data could plausibly encode 3-generation structure for SM fermions, given that the SM gauge group is not a finite fusion category? If subfactor principal graphs cannot do this, what is the structural obstruction?

4. **Inner fluctuations on Type II_1.** Is the inner-fluctuation calculus of Connes-Chamseddine well-defined for Type II_1 Dirac operators, and does it select a compact SM-shaped gauge group out of the much larger unitary group of `M`?

5. **Breuer-Fredholm chirality indices.** Can the Breuer-Fredholm index of a Type II_1 internal Dirac operator be irrational in a way that distinguishes non-embeddable from embeddable factors, or does the chirality content always land on rational (or integer) values regardless of embeddability?

6. **Semifinite spectral action on almost-commutative products.** Combining Chattopadhyay-Pradhan-Skripka (2023) with an almost-commutative product `C∞(M) ⊗ A_M`, does the spectral action converge and recover a bosonic SM-like Lagrangian, or are there analytic obstacles in the τ-compact-resolvent setting?

7. **Non-embeddable contribution.** Is there any structural feature of non-embeddable II_1 factors (post-MIP*=RE) that bears on SM-shaped spectral triples, or is the connection between MIP* = RE and spectral SM construction currently decorative rather than load-bearing?

These seven questions are the leave-behind for the repo. They are stated as open problems suitable for a specialist contributor to take on independently, with the corresponding context fixed by `connes-finite-control-checklist.md` and the present file.
