---
title: "DG Precision Carve-Out: Canon §2.4 Paragraph Edit"
date: 2026-06-23
problem_label: "dg-canon-nogo-update"
status: reconstruction
verdict: RESOLVED
---

# DG Precision Carve-Out: Canon §2.4 Paragraph Edit

## 0. Purpose

This file contains the exact paragraph edit for `canon/no-go-class-relative-map.md` §2.4,
implementing the Distler-Garibaldi precision carve-out as specified in
`explorations/distler-garibaldi-precision-carveout-2026-06-23.md` §7. It records the
edit applied, the mathematical basis for each clause, and the failure conditions for the
resolution verdict.

## 1. Source Specification (§7 of the precision carveout file)

The source document specifies the new final paragraph of §2.4 as follows (quoted verbatim
from §7):

> **[Precision carve-out, 2026-06-23 — distler-garibaldi-precision-carveout]**
>
> **Formal verdict: EVASION BY SCOPE EXIT.** GU violates DG assumptions DG-A1 (gauge group
> is Sp(64), not E8), DG-A2 (Lorentz group does not embed inside the gauge group), DG-A6
> (chirality is ind_H(D_GU) from the Clifford module operator index, not V_{2,1} complexity),
> and DG-A7 (GU is geometric bundle data on the non-compact Y^{14} = Met(X^4)). GU is not
> an object of the category DG_E8 that the theorem addresses. The theorem is inapplicable,
> not contradicted or circumvented within its domain.
>
> The condition GU satisfies instead of DG-A6 is:
>
> > **GU-Chir:** ind_H(D_GU) = 24 via the Atiyah-Singer theorem on (Y^{14}, Sp(64), S=H^{64})
> > with K3-type X^4 (A-hat=2), decomposing as 16 H-lines (spin-1/2, two generations) +
> > 8 H-lines (RS sector, one generation). Generation count = ind_H(D_GU) / 8 = 3.
>
> GU-Chir replaces DG's Lie-algebraic chirality test with an operator-analytic index theorem.
> No functor from GU's construction to DG_E8 is known that preserves ind_H(D_GU), because
> DG_E8 forbids bundle/compactification data (DG-A7) and the generation invariant depends on
> X^4 topology and Clifford module structure, not E8 adjoint branching. The DG carve-out from
> the functor audit (see Functor-audit status entry above) is therefore promoted from a
> structural observation to a precision theorem: GU's class exit from DG is at the level of
> the category of objects, not a clever condition-by-condition evasion. Reopen only if a
> functor F_DG: GU_data -> DG_E8 is exhibited that lands in the correct category and preserves
> ind_H(D_GU).

The source document also specifies a replacement row for the §1 acceptance summary table.

## 2. Mathematical Basis for Each Clause

**DG-A1 violation (Sp(64) not E8).**
GU's gauge group is Sp(64) = U(64,H), arising from Cl(9,5) ~= M(64,H). Sp(64) has real rank
64, dim_R = 8256. E8 has real rank at most 8, dim = 248. No Lie group homomorphism Sp(64) ->
E8 can have nontrivial image at the same Lie type: any continuous homomorphism of a connected
compact group reduces the rank, and rank 64 cannot embed into rank 8. Established in §2 of
the precision carveout file.

**DG-A2 violation (Lorentz not inside gauge group).**
In GU, SL(2,C) ~= Spin(3,1) acts on the base X^4 via the structure group of TX^4; it is
external to Sp(64). The DG theorem requires i_L: SL(2,C) -> E with i_L injective and the
image centralizing the internal gauge group inside E. No such embedding exists in GU's
construction. The Lorentz group and Sp(64) act on different bundles (tangent vs. spinor).
Established in §2 of the precision carveout file.

**DG-A6 violation (chirality is ind_H(D_GU), not V_{2,1} complexity).**
DG defines chirality as V_{2,1} being a complex G-representation in the SL(2,C) x G
decomposition of Lie(E). GU defines chirality via the H-linear Fredholm index
ind_H(D_GU) = dim_H ker D_GU - dim_H coker D_GU in Z,
where D_GU is the Dirac-DeRham operator on the Clifford module bundle over Y^{14}.
These are incommensurable chirality tests: the DG test is Lie-algebraic and
finite-dimensional; the GU test is operator-analytic and depends on global topology.
The replacement condition GU-Chir is stated in §4 of the precision carveout file, with
comparison table.

**DG-A7 violation (GU is bundle data).**
Y^{14} = Met(X^4) is a non-compact fiber bundle with fiber GL(4,R)/O(3,1), which has
homotopy type RP^3 x R^+. The gimmel metric G is a canonical bundle metric on Y^{14}.
The spinor bundle S = H^{64} is a Clifford module bundle, not a representation of one
finite-dimensional Lie group. DG-A7 explicitly forbids "bundle / compactification / flux
data." Established in §2 and §5 of the precision carveout file.

**Functor audit confirmation.**
The functor audit (`explorations/distler-garibaldi-functor-audit-2026-06-23.md`) tested
five candidate source categories for a functor F_DG: C_rich -> DG_E8 and found none that:
(a) accepts GU objects as inputs;
(b) lands in DG_E8 (preserving Lorentz-embedding and compact-centralizer data);
(c) preserves ind_H(D_GU) as a shadow of single-E8 adjoint branching.
The structural obstacle is DG-A7: DG_E8 has no room for non-compact fibers, and
ind_H(D_GU) is topology-dependent in a way that has no counterpart in a single-E8 branch
table. The functor audit confirms the precision carveout at reconstruction grade.

**GU-Chir status.**
GU-Chir is stated at reconstruction grade. The count ind_H(D_GU) = 24 is
CONDITIONALLY_RESOLVED via the 2+1 split: ind_H(D_{1/2}) = 16 (from A-hat(K3) = 2 exact,
rank_H(S(6,4)) = 8 algebraic) and ind_H(D_RS) = 8 (CONDITIONALLY_RESOLVED via APS on K3,
physical DOF count, and SM generation count; primary remaining gate is OQ-RK1).
The generation count is CONDITIONALLY_RESOLVED (reconstruction). GU-Chir is stated as the
correct condition regardless of whether ind_H(D_GU) = 24 is itself at verified grade; the
condition definition does not require the numerical value to be proved to state which
condition GU satisfies.

## 3. The Exact Paragraph Edit Applied

The following paragraph is inserted in `canon/no-go-class-relative-map.md` §2.4,
immediately after the "Functor-audit status (2026-06-23)" block and before section 2.5.
It is appended as a new paragraph, not replacing any existing content.

```
**[Precision carve-out, 2026-06-23 — distler-garibaldi-precision-carveout]**

**Formal verdict: EVASION BY SCOPE EXIT.** GU violates DG assumptions DG-A1 (gauge group is
Sp(64), not E8), DG-A2 (Lorentz group does not embed inside the gauge group), DG-A6
(chirality is ind_H(D_GU) from the Clifford module operator index, not V_{2,1} complexity),
and DG-A7 (GU is geometric bundle data on the non-compact Y^{14} = Met(X^4)). GU is not an
object of the category DG_E8 that the theorem addresses. The theorem is inapplicable, not
contradicted or circumvented within its domain.

The condition GU satisfies instead of DG-A6 is:

> **GU-Chir:** ind_H(D_GU) = 24 via the Atiyah-Singer theorem on (Y^{14}, Sp(64), S=H^{64})
> with K3-type X^4 (A-hat=2), decomposing as 16 H-lines (spin-1/2, two generations) + 8
> H-lines (RS sector, one generation). Generation count = ind_H(D_GU) / 8 = 3.

GU-Chir replaces DG's Lie-algebraic chirality test with an operator-analytic index theorem.
No functor from GU's construction to DG_E8 is known that preserves ind_H(D_GU), because
DG_E8 forbids bundle/compactification data (DG-A7) and the generation invariant depends on
X^4 topology and Clifford module structure, not E8 adjoint branching. The DG carve-out from
the functor audit (see Functor-audit status entry above) is therefore promoted from a
structural observation to a precision theorem: GU's class exit from DG is at the level of
the category of objects, not a clever condition-by-condition evasion. Reopen only if a
functor F_DG: GU_data -> DG_E8 is exhibited that lands in the correct category and preserves
ind_H(D_GU).
```

The §1 acceptance summary table row for Distler-Garibaldi is updated from:

| Distler-Garibaldi | ... | **outlier — stress case** ... | smooth-bundle-shadow framing has the weakest analogical purchase here; this is where the unified frame is most original and most vulnerable |

to:

| Distler-Garibaldi | Sp(64) Clifford module over Y^{14} with chirality ind_H(D_GU): not a richer-datum-in-the-same-class but a different mathematical framework | "single-E8-adjoint" functor phi_singleE8 does not exist from GU's construction (GU is not in DG_E8) | **outlier — stress case RESOLVED as scope exit: GU violates DG-A1/A2/A6/A7, no residual obligation** | no residual; reopen only if F_DG: GU_data -> DG_E8 is constructed |

## 4. Failure Conditions for the RESOLVED Verdict

The RESOLVED verdict on the DG carve-out is falsified by any one of the following:

**FC-1 (Functor construction).** A functor F_DG: GU_data -> DG_E8 is constructed that:
  (a) accepts GU's actual mathematical objects (Sp(64) bundle on Y^{14} = Met(X^4), Clifford
      module S = H^{64}, operator D_GU);
  (b) maps them to an object of DG_E8 (a tuple with E = real form of E8, Lorentz embedding
      i_L: SL(2,C) -> E, compact centralizer G);
  (c) preserves the chirality invariant as a shadow of single-E8 adjoint branching.
FC-1 is considered impossible given DG-A7 (which forbids all bundle data from DG_E8), but
an explicit construction would override this assessment.

**FC-2 (E8 embedding).** A continuous Lie group homomorphism Sp(64) -> E8 is exhibited with
nontrivial image of the same Lie type, disproving the rank-64-vs-rank-8 argument.

**FC-3 (DG-A1 restoration).** GU is rewritten to use a single real form of E8 as its
symmetry group with Lorentz embedded inside it. This would require abandoning Sp(64) and
the Clifford module construction, making it a different theory rather than falsifying the
carveout.

**FC-4 (GU-Chir false).** ind_H(D_GU) is shown to be undefined or zero for GU's actual
construction, meaning GU's chirality mechanism has no analytic realization. This would
replace the RESOLVED-by-scope-exit verdict with an OPEN chirality question.

None of FC-1 through FC-4 is currently supported by any evidence in the canon.

## 5. What Changes After This Edit

**Before:** §2.4 described the DG carve-out in structural terms (category-change, weak
analogy, open stress) without specifying which assumptions are violated or whether GU has
a genuine residual obligation. The acceptance summary table showed "stress case... most
original and most vulnerable."

**After:**
- The violated assumptions are named precisely: DG-A1, DG-A2, DG-A6, DG-A7.
- The evasion type is specified: scope exit (not domain-straddling, not condition-satisfying).
- The condition GU satisfies instead is written: GU-Chir with ind_H(D_GU) = 24.
- The verdict is upgraded from "stress case with open stress" to RESOLVED: no residual DG
  obligation for GU.
- The acceptance summary table row reflects "no residual; reopen only if F_DG constructed."
- The falsification surface is explicit (FC-1 through FC-4 above).

**What does not change:**
- The underlying GU-Chir count ind_H(D_GU) = 24 remains CONDITIONALLY_RESOLVED (it is a
  GU-internal open question, not a DG residual).
- The open questions OQ3b (RS analytic index = 8) and OQ-RK1/RK2 remain; they are not DG
  residuals and are not resolved by this edit.
- The VZ, Witten, Nielsen-Ninomiya, and Freed-Hopkins entries are not affected.

## 6. Cross-References

- Source specification: `explorations/distler-garibaldi-precision-carveout-2026-06-23.md` §7
- Functor audit (evidence base): `explorations/distler-garibaldi-functor-audit-2026-06-23.md`
- Canon file edited: `canon/no-go-class-relative-map.md` §2.4
- GU-Chir status: `explorations/n5-generation-count-synthesis-2026-06-23.md`
- DG-A1/A2 evidence: `explorations/distler-garibaldi-precision-carveout-2026-06-23.md` §2
- DG-A6 replacement: `explorations/distler-garibaldi-precision-carveout-2026-06-23.md` §4
