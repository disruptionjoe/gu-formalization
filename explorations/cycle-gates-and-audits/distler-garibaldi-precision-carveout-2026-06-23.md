---
title: "Distler-Garibaldi Precision Carve-Out"
date: 2026-06-23
problem_label: "distler-garibaldi-precision-carveout"
status: exploration
doc_type: research_note
verdict: RESOLVED
verdict_detail: "DG is an evasion by scope exit: GU violates assumptions (1) and (6) structurally, placing its chirality mechanism outside DG's target category DG_E8. No residual DG obligation remains."
---

# Distler-Garibaldi Precision Carve-Out

## 0. Purpose

Formalize the Distler-Garibaldi (DG) carve-out as a precision statement. Establish exactly
which assumptions GU violates, whether the relationship is evasion or residual, write the
exact condition GU satisfies instead, and propose an updated canon/no-go-class-relative-map.md
entry. This file is the deliverable output; the canon update is proposed here as a diff block
and must be applied in a separate editing pass.

## 1. The Distler-Garibaldi Theorem: Assumptions in Precision Form

Distler-Garibaldi 2009 (arXiv:0905.2483) states: There is no real Lie group E and subgroups
SL(2,C) and G such that (ToE1) G is connected, compact, and centralizes SL(2,C) inside E;
(ToE2) in the SL(2,C) x G decomposition of Lie(E), V_{m,n} = 0 for m+n > 4; (ToE3) V_{2,1}
is a complex G-representation; inside complex E8 or any real form of E8.

The precise assumption list needed for the carve-out is:

| # | Assumption | Precise statement |
|---|---|---|
| DG-A1 | Single finite-dimensional simple Lie group | E is a real form of one copy of E8 (or complex E8) |
| DG-A2 | Lorentz embedding inside E | SL(2,C) embeds as a subgroup i_L: SL(2,C) -> E with i_L injective |
| DG-A3 | Internal gauge group centralizes Lorentz | G connected, compact, and [G, i_L(SL(2,C))] = 0 inside E |
| DG-A4 | Matter content from V_{m,n} branching | All matter = subspaces V_{m,n} in the SL(2,C) x G decomposition of Lie(E) |
| DG-A5 | Low-spin condition | V_{m,n} = 0 for m+n > 4 |
| DG-A6 | Chirality = complex G-representation of V_{2,1} | Chirality is detected by V_{2,1} being complex as a G-rep |
| DG-A7 | Finite-dimensional representation theory only | No bundle data, no compactification, no flux, no infinite-dimensional extension |

The theorem says: within the category of objects satisfying DG-A1 through DG-A7
simultaneously, no object satisfies ToE1+ToE2+ToE3.

## 2. Which Assumptions Does GU Violate?

GU uses the following structures, established in the canon as of 2026-06-23:

- **Gauge group:** Sp(64) = U(64,H), arising from Cl(9,5) ~= M(64,H) acting on S = H^{64}.
- **Base geometry:** Y^{14} = Met(X^4), a 14-dimensional non-compact bundle over X^4 with
  non-compact fibers GL(4,R)/O(3,1) (homotopy type RP^3 x R^+).
- **Chirality source:** the Clifford module structure of D_GU, specifically the operator index
  ind_H(D_GU) (generation count = ind_H(D_GU) / 8) via an index theorem on X^4 combined
  with the RS sector. The *value* is OPEN pending OQ-RK1: ind_H(D_GU) in {24, 32} (3 or 4
  generations), Candidate A and Candidate B equistatus (see
  `explorations/generation-sector/generation-count-rank3-resolution-2026-06-23.md`, verdict OPEN). The carve-out
  below depends only on *which invariant* carries chirality, not on its numerical value.
- **Internal symmetry:** Sp(64), which is not E8 or a subgroup of E8 in any natural embedding.

**DG-A1 is violated.** GU's symmetry group is Sp(64), not E8 or a real form of E8. Sp(64)
has real rank 64 and dim_R = 8256. No copy of E8 (real rank 8, dim 248) appears structurally
in GU's setup. Sp(64) is not a subgroup of any real form of E8, since E8 has real rank at
most 8 and Sp(64) has real rank 64. There is no group homomorphism Sp(64) -> E8 with
non-trivial image of the same Lie type.

**DG-A2 is violated.** GU's Lorentz group does not embed inside its gauge group Sp(64) as
the DG embedding requires. Instead, the Lorentz group SL(2,C) ~= Spin(3,1) acts on the
fiber of Y^{14} via the structure group of the tangent bundle of X^4. The 4D Lorentz
transformation is external to the gauge group Sp(64); it acts on the base X^4, not inside
the Lie algebra of the gauge group. This is structurally different from i_L: SL(2,C) -> E.

**DG-A6 is violated.** GU does not detect chirality through V_{2,1} being a complex
G-representation in E's Lie algebra. GU's chirality arises from the index theorem applied to
the Dirac-DeRham operator D_GU on the Clifford module bundle E = (Omega^0 tensor S+) oplus
(Omega^1 tensor S-) over Y^{14}. The chirality invariant is ind_H(D_GU) in KSp^0(X),
not the representation-theoretic complexity of a specific V_{m,n} space. The operator-analytic
mechanism is entirely outside DG's Lie-theoretic framework.

**DG-A7 is violated.** GU is explicitly geometric bundle data: Y^{14} = Met(X^4) is a
non-compact fiber bundle, the gimmel metric is a canonical bundle metric on this space, and
the spinor bundle S = H^{64} is a Clifford module bundle, not a single representation of one
finite-dimensional Lie group.

**Summary:** DG-A1, DG-A2, DG-A6, and DG-A7 are all violated structurally. GU is not an
object of the category DG_E8 that the theorem addresses. Assumptions DG-A3, DG-A4, DG-A5
are moot because the prerequisite DG-A1 and DG-A2 are already absent.

## 3. Evasion or Genuine Residual?

**This is an evasion by scope exit, not a genuine residual.**

A genuine residual would require GU to be (or contain) an object of DG_E8 that is then
subject to the theorem's conclusion. GU contains no such object:

- There is no single finite-dimensional E8 in GU's construction.
- There is no Lorentz embedding i_L: SL(2,C) -> E for any E8 in the setup.
- The chirality mechanism (Clifford module index) has no shadow in single-E8 branching.

The category DG_E8 requires all seven assumptions simultaneously. GU fails four of them. The
theorem cannot be applied to GU because GU is not in the domain of the theorem.

The appropriate formal statement is:

> GU lies outside the domain category DG_E8 of the Distler-Garibaldi theorem, making the
> theorem inapplicable rather than violated or satisfied.

This is qualitatively different from a loophole: GU does not find a way around the theorem
inside its domain; GU operates in a different mathematical setting that the theorem does not
cover.

**What distinguishes evasion from loophole inside the class.** Lisi's SU(5) assignment
(refuted by DG 2009) was a failed attempt to work inside DG_E8 that did not satisfy ToE3.
GU makes no claim to work inside DG_E8 at all. The evasion is at the level of not being an
object of the category, not at the level of satisfying a different condition within the
category.

## 4. The Exact Condition GU Satisfies Instead of DG's Condition

DG-A6 asks: V_{2,1} is a complex G-representation inside Lie(E) under SL(2,C) x G
decomposition, for some E8 and subgroup G.

GU satisfies the following structurally different chirality condition:

**GU-Chir:** The Dirac-DeRham operator D_GU: Gamma(E) -> Gamma(E) on the Clifford module
bundle E = (Omega^0(Y^{14}) tensor S+) oplus (Omega^1(Y^{14}) tensor S-) over Y^{14} =
Met(X^4) is H-linear (Sp(64)-equivariant via the Cl(9,5) ~= M(64,H) bimodule structure) and
Fredholm on the zero-mode sector. The chirality invariant is

    ind_H(D_GU) = dim_H ker D_GU - dim_H coker D_GU in Z

computed as a quaternionic line count. The generation count is ind_H(D_GU) / 8, where 8 is
the H-dimension of one SM generation from the S(6,4) = C^{16} fiber (one Pati-Salam
generation = 16 Weyl fermions = 8 H-lines under Sp(64)).

This condition replaces DG-A6 with a purely analytic-topological statement:

| | DG chirality condition (DG-A6) | GU chirality condition (GU-Chir) |
|---|---|---|
| Object | Real form of E8 | Clifford module bundle over Y^{14} = Met(X^4) |
| Chirality carrier | V_{2,1} in Lie(E) under SL(2,C) x G | ker D_GU (H-linear, Fredholm) |
| Chirality invariant | Complex G-representation type of V_{2,1} | ind_H(D_GU) in Z (quaternionic index) |
| Generation count | |V_{2,1}| as complex G-rep class | ind_H(D_GU) / 8 |
| Mechanism | Lie-algebra representation theory | Atiyah-Singer index theorem on Y^{14} with K3-type X^4 |
| Group assumption | single finite-dim E8 | Sp(64) on non-compact Y^{14}, no E8 |

The two conditions are not related by any known functor. GU-Chir is not a refinement or
generalization of DG-A6; it is a different mathematical framework for the same physical goal
(counting chiral SM generations).

## 5. Why This Cannot Be A Forgetful-Image Realization of DG

The functor audit (`explorations/cycle-gates-and-audits/distler-garibaldi-functor-audit-2026-06-23.md`) tested five
candidate source categories and found no functor F_DG: C_rich -> DG_E8 that:

(a) accepts GU objects as inputs;
(b) lands in DG_E8 (preserving Lorentz-embedding and compact-centralizer data);
(c) preserves the generation count as a shadow of the single-E8 adjoint branching.

The structural reason is that the generation invariant ind_H(D_GU) depends on global
analytic data (Fredholmness of D_GU, KK zero-mode spectrum, Atiyah-Singer input from X^4
topology) that is entirely absent from Lie(E8) branching data. No coarse branch-table shadow
of Y^{14} Clifford data lands in DG_E8 because:

- DG_E8 has no room for non-compact fibers (DG-A7 forbids bundle data).
- DG_E8's chirality invariant is discrete and representation-theoretic; ind_H(D_GU) is
  continuous in the operator-theoretic sense and topology-dependent.
- The Schur complement computation for the RS sector (vz-schur, EVADED) further entangles
  spin-1/2 and spin-3/2 data in a way that has no counterpart in single-group adjoint
  decomposition.

## 6. The Precision Carve-Out Statement

The precision statement, suitable for inclusion in the no-go map, is:

**Distler-Garibaldi Carve-Out (2026-06-23):**

The Distler-Garibaldi theorem is a correct theorem about the category DG_E8 whose objects
are tuples (E, i_L: SL(2,C) -> E, G compact centralizing i_L(SL(2,C))) with E a real form
of E8, all matter from the SL(2,C) x G branching of Lie(E), and chirality detected by
V_{2,1} being a complex G-representation. GU evades DG by scope exit: GU's gauge group is
Sp(64), not E8 (violating DG-A1); GU's Lorentz group does not embed inside the gauge group
(violating DG-A2); GU's chirality mechanism is the Clifford module index ind_H(D_GU) on the
Dirac-DeRham operator over Y^{14} = Met(X^4), not the representation complexity of V_{2,1}
(violating DG-A6); and GU's construction is geometric bundle data on a non-compact fiber
bundle (violating DG-A7). GU is not an object of DG_E8. The theorem is inapplicable, not
contradicted.

The condition GU satisfies instead is GU-Chir: chirality is carried by the quaternionic
index ind_H(D_GU) of the H-linear Dirac-DeRham operator on Y^{14} (generation count =
ind_H(D_GU) / 8). This is an operator-analytic condition with no Lie-theoretic DG shadow.
The numerical value of the index is OPEN pending OQ-RK1 (ind_H(D_GU) in {24, 32}, 3 or 4
generations, Candidates A and B equistatus); the scope-exit evasion does NOT depend on it.

The evasion is structural (scope exit), not a trick within DG's domain, and is
index-value-independent: GU exits DG's class via DG-A1/A2/A6/A7 regardless of what
ind_H(D_GU) ultimately evaluates to.

DG cannot be applied to GU by analogy either: there is no canonical functor from GU's
construction to DG_E8 that preserves the generation invariant, because ind_H(D_GU) does not
factor through any single-E8 adjoint branch table.

The only circumstances under which DG would be applicable to GU are:
(a) GU were rewritten to use a single E8 as its symmetry group with Lorentz embedded inside
    it — which would require abandoning Sp(64) and the Clifford module structure;
(b) A functor F_DG: GU_data -> DG_E8 were constructed and shown to preserve ind_H(D_GU) —
    which is impossible given the DG-A7 prohibition on bundle data.

Neither (a) nor (b) is present in GU's construction.

**Status:** RESOLVED. DG is an evasion (scope exit). No residual DG obligation for GU.

## 7. Proposed Canon Update: no-go-class-relative-map.md Section 2.4

The following text is proposed as the new final paragraph of section 2.4, appending to the
existing "Functor-audit status" entry. It does not replace the existing content.

---

**[Precision carve-out, 2026-06-23 — distler-garibaldi-precision-carveout]**

**Formal verdict: EVASION BY SCOPE EXIT.** GU violates DG assumptions DG-A1 (gauge group is
Sp(64), not E8), DG-A2 (Lorentz group does not embed inside the gauge group), DG-A6
(chirality is ind_H(D_GU) from the Clifford module operator index, not V_{2,1} complexity),
and DG-A7 (GU is geometric bundle data on the non-compact Y^{14} = Met(X^4)). GU is not an
object of the category DG_E8 that the theorem addresses. The theorem is inapplicable, not
contradicted or circumvented within its domain.

The condition GU satisfies instead of DG-A6 is:

> **GU-Chir (chirality *test*, not a settled count):** chirality is carried by the
> quaternionic Clifford-module index ind_H(D_GU) of the Dirac-DeRham operator on
> (Y^{14}, Sp(64), S=H^{64}), with generation count = ind_H(D_GU) / 8. The *value* of this
> index is **OPEN pending OQ-RK1**: ind_H(D_GU) in {24, 32} (3 or 4 generations). The two
> candidates are equistatus per `explorations/generation-sector/generation-count-rank3-resolution-2026-06-23.md`
> (verdict OPEN): **Candidate A** (rank_H(S_RS^+) = 4 -> ind_H(D_RS) = 8 -> ind_H(D_GU) = 24
> -> 3 generations) and **Candidate B** (rank_H(S_RS^+) = 8 -> ind_H(D_RS) = 16 ->
> ind_H(D_GU) = 32 -> 4 generations) are neither derived nor eliminated; OQ-RK1 (the M(64,H)
> CAS computation of the RS gamma-trace projector rank) is the blocking gate. The
> Candidate-A-conditional decomposition is 16 H-lines (spin-1/2, two generations) + 8 H-lines
> (RS sector, one generation); under Candidate B the RS leg is 16 H-lines. **Do not cite a
> single settled value or "3 generations" as established** — the count is the open target of
> an unfinished index computation.

GU-Chir replaces DG's Lie-algebraic chirality test with an operator-analytic index theorem.
No functor from GU's construction to DG_E8 is known that preserves ind_H(D_GU), because
DG_E8 forbids bundle/compactification data (DG-A7) and the generation invariant depends on
X^4 topology and Clifford module structure, not E8 adjoint branching. The DG carve-out from
the functor audit (see Functor-audit status entry above) is therefore promoted from a
structural observation to a precision theorem: GU's class exit from DG is at the level of
the category of objects, not a clever condition-by-condition evasion. Reopen only if a
functor F_DG: GU_data -> DG_E8 is exhibited that lands in the correct category and preserves
ind_H(D_GU).

---

The proposed update to the summary table row for Distler-Garibaldi is:

| theorem | candidate richer datum | candidate forgetful operation | analogy strength | open stress |
| --- | --- | --- | --- | --- |
| Distler-Garibaldi | Sp(64) Clifford module over Y^{14} with chirality ind_H(D_GU): not a richer-datum-in-the-same-class but a different mathematical framework | "single-E8-adjoint" functor ϕ_singleE8 does not exist from GU's construction (GU is not in DG_E8) | outlier — stress case RESOLVED as scope exit: GU violates DG-A1/A2/A6/A7, no residual obligation | no residual; reopen only if F_DG: GU_data -> DG_E8 is constructed |

## 8. What This Changes

Before this note: the no-go map entry for DG described the carve-out in structural terms
(category-change, weak analogy) but did not specify which assumptions were violated or
whether GU had a genuine residual obligation.

After this note:
- The violated assumptions are named precisely: DG-A1, DG-A2, DG-A6, DG-A7.
- The evasion type is specified: scope exit (not domain-straddling or condition-satisfying).
- The condition GU satisfies instead is written: GU-Chir (chirality carried by ind_H(D_GU);
  numerical value OPEN pending OQ-RK1, ind_H(D_GU) in {24, 32}, Candidates A/B equistatus).
- The verdict is upgraded from "stress case with open stress" to RESOLVED: no residual
  DG obligation for GU. This scope-exit verdict is index-value-independent and survives
  regardless of how the generation-count gate OQ-RK1 resolves.
- The failure condition for this resolution is explicit: construct F_DG: GU_data -> DG_E8.

## 9. Remaining Open Questions (Not DG-Related)

The following items are open but are NOT DG residuals:

1. **The numerical value of ind_H(D_GU) (OPEN).** The count is OPEN between Candidate A
   (ind_H(D_GU) = 24, 3 generations) and Candidate B (ind_H(D_GU) = 32, 4 generations),
   equistatus per `explorations/generation-sector/generation-count-rank3-resolution-2026-06-23.md`. The
   blocking gate is OQ-RK1 (M(64,H) CAS computation of the RS gamma-trace projector rank
   rank_H(S_RS^+); rank 4 -> 24, rank 8 -> 32), with OQ-RK2 (APS boundary conditions on K3)
   also open. These are genuine open items in analytic index theory, not DG residuals.

2. **The GU-Chir condition itself.** GU-Chir is stated at reconstruction grade. Upgrading it
   to verified requires the RS analytic route or the APS boundary-condition verification on
   K3-type X^4. This is a GU-internal task, not a consequence of DG.

3. **OC1 Fredholmness of D_GU on non-compact Y^{14}.** The full operator-Fredholm question
   is open (CONDITIONALLY_RESOLVED via APS route). Not a DG issue.

None of these opens is created by DG. DG is definitively not applicable.
