---
title: "X-P1-P2: multiplicity mixing and naturality rigidity"
status: exploration
doc_type: structural-result
created: "2026-11-11"
program_target: X-P1-P2
tier: T2
expected_delta: "Refine the constrained weld by including provenance mixing and its naturality conditions."
actual_delta: "Constrained: full-support symbol alone has a 17-dimensional commutant control; fixed extended gamma-trace/inclusion arrows force scalar commutant for every full-support coefficient choice in the declared H-symbol subclass. Existence remains separate."
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Mixing repeated representations changes the weld problem

**Result.** Regroup the existing twenty observer-subgroup H slots into twelve
isotypic types: four multiplicities three and eight multiplicities one. A
fully supported symbol can have complex H-equivariant multiplicity commutant dimension **17**, despite
all 136 scalar cells being nonzero and the support graph being connected.
If the extended gamma-trace and inclusion maps are also fixed, the commutant
is instead exactly the scalars for **every** full-support symbol in this
specified coefficient category. Thus compatible invertible coflips, if they
exist, are unique up to a scalar; prescribing the same square restricts that
scalar to unit modulus. This is a conditional structural-subclass result,
not proof that all actions in C obey the added hypotheses.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P1-P2
tier: T2
expected_delta: Replace scalar-slot uniqueness inference with the complete multiplicity condition.
actual_delta: Symbol-only freedom and its conditional naturality repair proved; no universal C verdict.

```gu-typed-objects
result: multiplicity-weld-and-naturality-rigidity
carrier: twelve H-isotypic multiplicity spaces regrouping twenty native slots LAYER=UNTYPED CHIRALITY=N/A
pairing: optional nondegenerate Hermitian multiplicity forms; positive identity Gram only in the control ON=declared_carrier
real_structure: complex-linear arrow maps and antilinear mirror coflips; square and isometry imposed separately
grading: native representation types and named provenance inclusions, not physical family count
action_owner: repository-construction -- H-symbol structural subclass, no action construction
target: all simultaneous coefficient and named-map intertwiners MAP-TYPE=intertwiner
```

## 1. Prior evidence and the exact question

The [earlier weld audit](x-p1-p2-class-c-lift-2026-11-11.md) proves weighted
scalar compatibility and separates existence from uniqueness. It explicitly
leaves repeated-copy mixing open. The July full20 polarization analysis already
owns invariant pairing freedom between S and imΓ; K2199/K2200 already use
commutants for principal pairings. Generic Schur uniqueness is reused here,
not claimed as a new mathematical theorem.

The coefficient category comes from
[`shiab_b5_observer_symbol_multiplicity_matrix.py`](../../tests/shiab_b5_observer_symbol_multiplicity_matrix.py).
Its `TYPES`, `SLOTS` and exact `symbol_multiplicity` give four multiplicity-three
types `Lp,Rm,Lm,Rp`, and eight multiplicity-one types
`X32p,X23m,X2Tp,X1Tm,X32m,X23p,X2Tm,X1Tp`.
There are 40 ordered type-arrows, each with one H-intertwiner; their matrix
coefficients supply 136 scalar cells. All multiplicity-space endomorphisms
together have 44 complex coordinates. Choosing these coefficients is an
algebraic control on the stated symbol category, not choosing a Lagrangian
or certifying membership in C.

## 2. General intertwiner and existence criterion

For each arrow e:s→t, let A_e:V_s→V_t and B_e:W_s→W_t be the original and
mirror coefficient maps after **specified** irrep intertwiners and any vector
argument transformation have been factored out. An antilinear candidate
`C_i(v)=U_i conjugate(v)` intertwines exactly when

`U_t conjugate(A_e)=B_e U_s` for every e.

Every U_i must be invertible. All named extra maps and their mirror relations
must be included among these equations. Rectangular and rank-deficient A_e
are allowed: no inverse of them is used. This is simply an isomorphism of
the conjugate quiver representations (the standard definition in
[Crawley-Boevey, Lecture 1 §1.1](https://www.math.uni-bielefeld.de/~wcrawley/dmvlecs.pdf)).
Solve the linear equations for the U_i first. The product of their determinant
polynomials is nonzero somewhere exactly when it is not identically zero on
that solution space over C. The zero solution alone proves nothing. Prescribed
coflip square and pairing isometry impose additional, non-linear real equations;
invertible intertwining alone does not establish them.

If C0 and C1 are compatible invertible antilinear maps to the same mirror
object, `T=C0^-1 C1` is a linear automorphism commuting with every A arrow.
Conversely each such T produces C0T. Thus the solution set, when nonempty,
is a torsor for the full automorphism group, not automatically one phase.
For an endomorphism coflip with `C0²=epsilon I`, the condition that C0T has
the same square is `tau(T)T=I`, where `tau(T)=C0 T C0^-1`.

An equal-rank tree of invertible arrows allows further root reduction:
if A_i,B_i are tree-path transports, then
`U_i=B_i U_root conjugate(A_i)^-1`. Every remaining arrow gives
`U_root conjugate(A_t^-1 A_e A_s)=(B_t^-1 B_e B_s) U_root`.
This shortcut is inapplicable to the native rectangular/rank-deficient arrows
without an actual invertible spanning tree. The general equations remain valid.

## 3. Native full-support control: commutant dimension 17

Choose every coefficient matrix A_e to be the all-ones matrix of its required
size. Every one of the 136 scalar cells is nonzero. In each multiplicity-three
space split `C³=span(1,1,1)⊕{x:sum(x)=0}`. All incoming maps land in the first
line; all outgoing maps annihilate the two-dimensional second space. A
commuting endomorphism preserves this split. On the connected twelve-type
bright graph it has one shared scalar; on each of the four dark two-spaces
it is arbitrary. Consequently

`End_H(A) = C ⊕ Mat_2(C)^4`, with complex dimension `1+4·4=17`.

This also follows independently by exact elimination: the 136 equations on
44 variables have rank 27. Connectivity of scalar support does not remove
linear combinations that the symbol annihilates.

At the normalized multiplicity level, pair mirror types by coordinate
conjugation. Real all-ones coefficients obey the mirror equations. Swap the
first two provenance coordinates in all four C³ spaces and act identically on
singlets. This T preserves each all-ones map, is real orthogonal, has T²=I,
and is mirror-compatible. It supplies a non-scalar coflip with the same square
and positive multiplicity Gram as the original. Irrep-level canonical transport
is held separately; this is not a claim about the native Krein form or all C.

## 4. Actual follow-through: fixed gamma-trace and inclusion restore rigidity

Order the three provenance coordinates as S, imΓ, and the low R summand.
Freeze their named inclusions/projections and the normalized nonzero Γ/j maps.
Extended to the total multiplicity space, these are the matrix units
`E01` and `E10`. Requiring the coflip to respect them means that the ratio T
of any two coflips commutes with both. In each C³ block this forces

`T_i=diag(a_i,a_i,b_i)`.

The single-copy blocks are scalars. For a general full-support symbol, each
nonzero scalar coefficient in `T_t A_e=A_e T_s` then equates the corresponding
source and target diagonal values. The existing twenty-slot support graph is
connected, so all values coincide. Therefore

`End_H(A, extended Γ, extended j)=C I`

for **every** full-support coefficient choice in this category. This proof is
uniform; it does not infer universality from finite coefficient samples. The
all-ones control's augmented matrix has exact rank 43 on 44 variables, agreeing
with the analytic result. Its previous coordinate swap fails the E01 equation.

If C1=cC0 and both squares equal the same epsilon I, then
`C1²=|c|² C0²`, so `|c|=1`. Existence is still separate: the earlier weighted
incompatible coefficient controls are not repaired merely by this uniqueness
theorem. Nor does the mere abstract existence of Γ and j force their extended
matrices to be preserved by every action completion; the fixed field summands
and naturality equations are essential hypotheses. The sparse extension below removes the full-support restriction.

## 4b. Released successor: all sparse coefficient strata

After the extended Γ/j equations, merge the S and imΓ diagonal variables
within each triple. There are sixteen remaining scalar variables: two per
triple plus eight singlets. Build an undirected graph on them, adding an edge
for each **actually nonzero** scalar coefficient A_e[b,a] between the
corresponding source and target variables. Let c be its component count,
including isolated vertices. Then, uniformly over every zero/nonzero pattern,

`End_H(A, extended Γ, extended j) = C^c`, and `Aut_H = (C*)^c`.

Proof: the named-map equations already force diagonal matrices. Each arrow
entry is precisely `(lambda_target-lambda_source) A_e[b,a]=0`; over C it
identifies variables exactly when that entry is nonzero. These are all the
remaining equations, so a freely chosen scalar on each component is necessary
and sufficient. No coefficient magnitudes or cycle products enter this
**commutant** classification; existence of a coflip still has its distinct
weighted equations. This covers rectangular and rank-deficient arrows.

If an existing coflip C0 preserves the whole arrow system up to its specified
mirror involution and has square epsilon I, conjugation by C0 permutes the
primitive component projectors by an involution pi. For C=C0 T with component
scalars lambda, the same-square condition is

`conjugate(lambda_pi(i)) lambda_i = 1`.

A fixed component contributes U(1); an exchanged pair contributes one C*,
with the partner fixed as `1/conjugate(lambda)`. It is incorrect to call every
component an independent phase without checking this permutation and any
additional pairing condition. The probe constructs the non-unit-modulus
exchanged-pair example and a violated-square control. It does not claim such
component exchange is realized by a C action.

Independent exact checks build a spanning tree using actual allowed native
cells: fifteen selected nonzero coefficients give c=1 and rank43. Removing
one tree edge gives c=2 and rank42. Setting all symbol coefficients to zero
leaves c=16 and rank28 from the named maps alone. These controls test the
classification; the entrywise proof establishes it for all patterns.

## 5. Pairing consequence and differential limit

Let P and K be nondegenerate Hermitian forms on the same total carrier, and
assume explicitly that `X=K^-1 P` is H-equivariant (for example, both forms
are invariant under the same specified real H action). This is essential: the
computed commutant is vertexwise in H types, not the unrestricted endomorphism
algebra of the full carrier. If they
give the **same adjoint** to every selected symbol and named-map generator,
then `X=K^-1 P` commutes with all those generators. To see this, equality of
`P^-1 A†P` and `K^-1 A†K` says X commutes with the K-adjoint of A; taking
K-adjoints and using `X^sharp=X` gives commutation with A. Under the scalar
commutant hypothesis, `P=cK` with nonzero real c. Mere H-invariance is weaker
and does not give this conclusion.

This is pointwise algebra. A varying multiplier c(x) can change the formal
adjoint of a differential operator through derivatives. Density-dual transport,
zero-order terms, connection descent and boundary forms must still agree.
The [boundary transfer result](p3-boundary-symmetry-transfer-2026-11-11.md)
then adds full-operator and closed-domain preservation before any kernel or
index inference. That is the released consumer of this rigidity calculation.

## Program effect and verification

`X-P1-P2` remains constrained, now with an explicit, sufficient naturality
subclass that handles provenance mixing and an exact symbol-only countercontrol.
Every sparse stratum is classified by its sixteen-variable support graph;
coflip component exchange controls the residual square condition. The
geometric/reconstructed weld stays intact. No complete natural/gauge tensor
basis, action existence, full C decision, two-datum floor, P3 realization or
source-family statement follows. SC-CHI-01/51 and SC-GEN-02/03/54 retain their
ASSERTS polarity; RA-F1 and AC-F1 remain NEEDS.

[Exact probe](../../tests/program-focus/x_p1_p2_multiplicity_weld_probe.py)
imports the held representation census, independently builds the full linear
systems and checks ranks, mirror compatibility, square, pairing and contrary
controls. [Evidence](../../lab/process/x-p1-p2-multiplicity-weld.json) records
these separately from the universal proof in §4. Independent specialist and
hostile review govern acceptance; no Lean proof or external certification is claimed.
