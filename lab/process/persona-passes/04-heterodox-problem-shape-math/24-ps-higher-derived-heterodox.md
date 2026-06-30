---
title: "Problem Shape — Higher / Derived / Homotopy-Coherent Geometer (Heterodox)"
status: process
doc_type: persona_pass
updated_at: "2026-05-31"
---

# Problem Shape — Higher / Derived / Homotopy-Coherent Geometer (Heterodox)

**Date:** 2026-05-28
**Baseline accepted:** Computation is substrate. Geometry is observer-frame artifact. The bundle is emergent. No-go theorems constrain observer-frames, not substrate. (00c)
**Persona:** Higher / derived / homotopy-coherent geometer, strong heterodox lean (motivic, condensed, TMF, prismatic, factorization-homological).

## (a) Thesis (mainstream-in-domain)

Textbook derived algebraic geometry on a substrate of "computation primary, bundle emergent" reduces to derived stacks over smooth manifolds, cotangent complexes, BV-BRST in cdga form, factorization algebras a la Costello-Gwilliam over a smooth $X$. The substrate's role is to refine $\pi_*$ to $R\pi_*$ and supply derived corrections in $H^{<0}$. The fiber is still classical Sym², the structure group still $GL(4)$, and chirality is still adjudicated by an index theorem on the smooth quotient. Witten 1981 is the 1-categorical shadow of an unsharpened $(\infty,1)$-categorical fact, and Freed-Hopkins is the K-theoretic shadow of the same fact in invertible field theory. Persona 14 already named this and found the derived shadow most likely BV-ghost rather than propagating fermion.

## (b) Heterodox antithesis

The heterodox literature refuses smooth schemes / smooth stacks as the carrier. Six moves:

1. **Condensed mathematics (Clausen-Scholze).** [speculation] Replace topological spaces (and smooth manifolds in their light-condensed analytic form) with condensed sets / liquid vector spaces. Functional analysis becomes homological algebra in an abelian category. The "observerse" reads as a **condensed metric bundle** whose RHom / Ext groups are the natural home for anomalies. Smooth-section reflection positivity is replaced by liquidity, which is a derived-categorical condition, not a smooth one.

2. **Motivic homotopy theory (Voevodsky-Morel).** [speculation] Chirality is a **motivic class** in $H^{p,q}_{mot}$, not a class in singular $H^*$. The motivic bigrading sees parity that Betti cohomology averages away; the slice filtration separates parity-graded pieces of the substrate-emergent bundle.

3. **TMF / topological modular forms (Hopkins-Miller, Ando-Hopkins-Rezk).** [speculation] Spin and String anomaly classes live in $\pi_*$ of TMF, not in ordinary cohomology. The SM chirality class is conjecturally a $tmf$-class of the substrate, with the smooth bundle picking up its image in $H\mathbb{Z}$ (which is lossy). Witten 1981 is the $H\mathbb{Z}$-shadow; the real obstruction lives in $tmf$.

4. **Factorization homology (Lurie, Ayala-Francis).** [speculation] 14D bulk-to-4D reduction is $\int_X \mathcal{A}$ where $\mathcal{A}$ is an $E_n$-algebra of substrate-local operators. Chirality is the **non-triviality of the $E_n$-structure**, not a section property. Higher $E_n$ braiding is invisible to 1-categorical KK.

5. **Prismatic cohomology (Bhatt-Scholze).** [speculation] If the substrate has number-theoretic structure (multiway hypergraph rewriting has rational combinatorial weights; chiral PEPS has $\mathbb{Q}_p$ stabilizer codes), the natural cohomology is **prismatic**, unifying crystalline / etale / de Rham. A "prismatic GU" relocates chirality to a Frobenius-equivariant $\delta$-ring datum on the substrate; Witten and Freed-Hopkins are the de Rham and $K$-theoretic specializations.

6. **Calabi-Yau $d$-categories and noncommutative motives (Kontsevich).** [speculation] The substrate's natural invariant is a **CY $d$-structure on a smooth proper dg-category**, with chirality the **shifted symplectic** structure's sign. Noncommutative motives provide a homotopy-theoretic substrate for "spaces" in which the bundle is a 1-shadow.

## (c) Aufhebung as a problem-shape question

Thesis says the derived enhancement lives over a smooth $X$ and produces $H^{<0}$ corrections. Antithesis says the substrate is condensed / motivic / prismatic / $E_n$-algebraic and the smooth $X$ is a $\pi_0$ / Betti / de Rham / $H\mathbb{Z}$-shadow that **loses** the chirality class.

Aufhebung within the domain: **the observerse is a condensed-motivic-prismatic object $\mathfrak{O}$ whose 1-categorical smooth shadow is the metric bundle $\mathrm{Met}(X) \to X$, and SM chirality is a class in a finer cohomology (motivic, $tmf$, prismatic, or $E_n$-factorization-homological) of $\mathfrak{O}$ whose image in $H\mathbb{Z}$ of the smooth shadow is null.** Witten 1981 computes the null image; the live class is upstairs.

> **What is the smallest enrichment class (condensed, motivic, $tmf$, prismatic, factorization-$E_n$, CY-$d$, or noncommutative-motivic) such that $\mathfrak{O}$ carries a chirality class whose smooth $H\mathbb{Z}$-image vanishes and whose Freed-Hopkins / Reinforced-cobordism image is non-trivial in a way the 1-shadow cannot detect?**

## (d) What WRK-326 should ask next from this lens

Stop testing derived pushforward $R\pi_*$ on smooth stacks. Start asking: **which enrichment class is the substrate honestly in.** Concretely: (i) for chiral PEPS, the substrate is naturally $E_n$ / factorization-algebraic over $\mathbb{R}^4$; compute $\int_{\mathbb{R}^4}$ of its $E_4$-substrate and check whether the resulting 0-dim factorization-homology class is $tmf$-detectable. (ii) For Connes II$_1$ spectral triple, the substrate is naturally noncommutative-motivic; ask whether its CY-$d$ structure has the chirality sign. (iii) For multiway hypergraph rewriting, the substrate is naturally condensed (causal-graph topology is profinite); ask whether the liquid-cohomology of the rewrite category carries a parity-graded class.

## (e) Falsifiable mathematical sub-question

> **Does the 4D factorization homology $\int_{\mathbb{R}^4} \mathcal{A}_{sub}$ of any substrate $E_4$-algebra named in 00c (chiral PEPS local operators, multiway-rewrite local Hopf algebra, or II$_1$ on-site algebra) carry a class in $\pi_*\mathrm{tmf}$ that maps to a non-trivial Freed-Hopkins anomaly in the SM signature, while mapping to zero in ordinary $H^*(\mathbb{R}^4; \mathbb{Z})$?**

A negative answer (no such $tmf$-class survives the smooth shadow non-trivially for any substrate $E_4$-algebra) closes the higher-derived-heterodox route: the chirality class is either visible to the 1-shadow (and Witten kills it) or invisible to Freed-Hopkins (and is not the SM chirality). A positive answer hands WRK-326 a concrete enrichment class and a $tmf$-level invariant to compute, replacing family-frontier exhaustion with a single sharp homotopy-theoretic computation.
