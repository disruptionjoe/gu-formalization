---
title: "Normal SU(3,2) existence adds no absolute obstruction, including a fixed Spin lift"
status: exploration
doc_type: structural-result
created: "2026-11-25"
program_target: P2xglobal_index / X-P1-P2
tier: T2
expected_delta: "Decide the additional normal determinant and inherited-Spin burden in W09, retaining torsion and fixed-data distinctions."
actual_delta: "On the admitted dimension-at-most-seven homotopy bases, any negative complex reduction extends to a determinant-trivial normal reduction compatible with any prescribed total Spin structure. Thus absolute SU(3,2) existence is equivalent to the already-established U(3,2) criterion; fixed-J, phase, relative and selection problems remain distinct."
class_covered: "Oriented positive-rank6/negative-rank4 real bundles with fixed total Spin structure over paracompact bases of CW homotopy dimension at most7, with any fixed compatible negative U(2) reduction; applied to the native trace-reversed normal bundle over X, Y and its time-oriented cover."
premises:
  - "lab/sources/source-claim-register.yaml#SC-GRP-03: ASSERTS simultaneous reductions; SU is optional relative to U, not source-selected."
  - "explorations/conditional-build/global-normal-complex-reduction-2026-11-24.md: native normal splitting, component orientations, base criterion and RP3/S3 spines."
  - "canon/w2-y14-spin-structure.md: existing spin scope; this result separately fixes the total normal Spin lift."
  - "https://arxiv.org/html/2406.05518v2: rank6 almost-complex lifting stages, not a GU application theorem."
source_bridge:
  status: conditional
  reason: "The normal bundle and optional reduction are source-relevant, but no source-selected complex structure, determinant section, preserved connection or physical realization is supplied."
kill_condition: "No GU kill. An additional obstruction would bind only the optional special-unitary branch with its stated topology/fixed data. The absolute existence test instead closes positively."
classification: SOURCE_NATIVE_ROUTE
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

```yaml
program_target: P2xglobal_index / X-P1-P2
tier: T2
expected_delta: Decide additional normal determinant and fixed-Spin existence burden.
actual_delta: Absolute SU existence equals U existence in the declared bundle class; fixed and relative data are separate.
```

# The optional determinant question closes positively

```gu-typed-objects
result: Absolute normal special-unitary existence with prescribed total Spin lift
carrier: N=Nplus+Nminus=Sym2(pi*TX)*; native normal rank10 over X or metric bundle Y/cover, positive6 negative4 LAYER=ambient+observed BRIDGE=literal-section-pullback CHIRALITY=N/A
pairing: trace-reversed Frobenius lambda=1/2, signature6,4; compact splitting used only for topology ON=declared_carrier
real_structure: real normal bundle; chosen orthogonal complex structures, fixed total Spin double cover
grading: positive6/negative4 metric split, no fermion chirality grading
action_owner: N/A -- absolute bundle reduction, no source action, vacuum or physical connection
target: SU(3,2) reduction of the normal bundle compatible with Spin MAP-TYPE=not-a-map
```

Basis: `2858d21dfd7a1c67afa4b2195a7606de801f3173`.

**Result.** In the absolute problem, imposing determinant one does not add a
new existence obstruction to the previously established normal U(3,2)
criterion. This remains true with the total normal Spin structure prescribed.
One may keep the negative U(2) structure and change the positive U(3)
structure. The result does **not** say every fixed U(3,2) structure has trivial
determinant or fits every prescribed Spin structure.

This closes W09's stated discriminator. It supplies no GU falsification,
physical vacuum selection, preserved connection, global observed gauge quotient,
chirality count, or prediction. The source explicitly admits the U(3,2)
alternative; that is an independent reason this optional test cannot by itself
exclude GU. Physics rows and matrix statuses do not move.

## 1. Precise theorem and source scope

Let B have the homotopy type of a CW complex of dimension at most seven. Let
N=P⊕Q be an oriented real bundle with a metric of signature (6,4), chosen
component orientations, and a prescribed Spin(6,4) lift of its SO0 frame bundle.
Fix an orthogonal complex structure J_Q on the negative rank-four factor,
compatible with its chosen orientation.

**Theorem.** There exist an orientation-compatible orthogonal complex structure
J_P on P and a unit complex determinant trivialization of
(P,J_P)⊕(Q,J_Q) whose induced Spin lift is isomorphic, over the given SO frame
bundle, to the prescribed one. Equivalently there is a lifted SU(3,2) reduction
of that fixed Spin bundle extending J_Q.

All existence here is smooth when B is smooth. Bundles and sections can be
handled on the indicated CW model and transported back; no geometric
fourteen-dimensional obstruction calculation is substituted for the
seven-dimensional homotopy model. No equivariance, integrability, parallelism,
canonical choice, or boundary condition is asserted.

SC-GRP-03 (ASSERTS, extracted draft2021 p29 eq4.6) supports simultaneous compact
and complex reductions and retains an extra U(1) when SU is not privileged.
The [source-chain audit](../../lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md)
constructed fibrewise Lie-algebra embeddings and named the missing global
reduction data. This result answers absolute existence, and proves the global
Spin lift rather than inferring it from Lie-algebra dimension. The earlier
[spinor determinant result](selected-k77-spin-induced-determinant-line-gate-2026-08-14.md)
is about a different bundle and is not used as the normal determinant proof.
The ambient K77 assertion versus K95 derivation remains separate: both labels
must not be substituted for this explicit normal (6,4) metric calculation.

## 2. Prescribed first Chern class, including torsion

For an oriented real rank-six bundle P over B, every integral class c with
rho2(c)=w2(P) is realizable as c1 of an orientation-compatible orthogonal complex
structure. More precisely, every specified Spin^c structure on P is realized
by such a U(3) reduction over this dimensional range.

One proof uses the natural U(3)→Spin^c(6) lift of realification. Its homogeneous
fibre is S7. Fix the canonical lift whose Spin^c determinant character restricts
to det_C on U(3), with the corresponding half-spin convention. Spin(6)=SU(4) acts transitively on unit positive spinors with SU(3)
stabilizer; in Spin^c(6) the stabilizer becomes U(3). The first possible
obstruction to a section lies in degree eight, above the dimension of B.
An integral lift c supplies a Spin^c structure of determinant c. Its choice,
not just c, is retained when two-torsion is present. This is the rank-six
specialization of the first lifting stage and next obstruction in
[Albanese–Milivojević, §§3.2–3.3](https://arxiv.org/html/2406.05518v2).

Write d=c1(Q,J_Q). Total Spin and the component orientations give

    w2(P)=w2(Q)=rho2(d)=rho2(-d).

Choose the positive complex structure with c1(P,J_P)=-d. Then

    c1(det_C(P,J_P) tensor det_C(Q,J_Q))=0 in H2(B;Z).

Complex line bundles are classified by integral H2, including its torsion.
Thus the determinant line really is trivial, not only flat or trivial in
real cohomology. This proves underlying special-unitary existence. On its own
it has not matched a prescribed Spin lift; the next proof supplies that part.
It is not necessary to force either summand's c1 separately to vanish.

## 3. The fixed-Spin proof: the remaining fibre is S7

Let G=Spin(6,4), the connected Clifford double cover of SO0(6,4). Over the
chosen compact split its maximal compact is

    (Spin(6) × Spin(4)) / <(-1,-1)>.

The covering character on pi1(SO(6)×SO(4))=Z2×Z2 is (a,b)↦a+b. Put
H0=S(U(3)×U(2)) inside SO(6)×SO(4). It is connected, and its fundamental-group
generator has determinant windings (1,-1); its image in Z2×Z2 is (1,1).
The character is therefore zero. H0 lifts injectively to a subgroup H of G.
The noncompact SU(3,2) lift follows by maximal-compact deformation retraction.
**SU(3,2) is not simply connected**; the parity argument, not that false claim,
proves the lift. The full inverse image of H0 also contains -H; use the
identity lift H throughout.

Let K be the inverse image of SO(6)×U(2) in G. The fixed J_Q reduces the fixed
Spin bundle to a principal K bundle. There are surjections

    K → U(2),       kernel Spin(6),
    H → U(2),       kernel SU(3).

Surjectivity of the second map is explicit: for any B∈U(2), choose A∈U(3)
with det A=(det B)^-1. It follows that Spin(6) acts transitively on K/H, with
stabilizer SU(3). Consequently

    K/H ≅ Spin(6)/SU(3) ≅ SU(4)/SU(3) ≅ S7.

The associated S7 bundle has a global section over B: pi_i(S7)=0 for i≤6,
so the first obstruction is in H8 and there are no cells that high. That
section reduces the **specified** Spin bundle to H, and hence to the lifted
SU(3,2). Its complex structure and unit volume have exactly the required
Spin compatibility. This directly handles all H1/Z2 and H2 torsion issues;
no surjectivity of integral-to-mod2 H1 is assumed.

The unit-spinor/SU(3) correspondence also appears in
[Agricola–Chiossi–Friedrich–Höll](https://arxiv.org/abs/1411.5663).
The extension to the present indefinite split is the group calculation above,
not an assumed transfer of an elliptic, positive or analytic theorem.

## 4. Apply it on X, Y and the time-oriented cover

The [Nov24 normal theorem](global-normal-complex-reduction-2026-11-24.md) owns

    Nplus = 1 ⊕ Sym2_0 E*,     Nminus = 1 ⊕ (L* tensor E*) ≅ L* tensor V*,
    w2(Nplus)=w2(Nminus)=pi*w2(TX),

with V=pi*TX=L⊕E. Its scalar trace line is globally trivial even without a
time orientation. Y=Met_(3,1)(X) retracts onto P(TX), with fibre RP3; its
time-oriented cover retracts onto S(TX), with fibre S3. Both have CW models
of dimension at most seven. The theorem therefore applies on all three bases,
not only on the four-dimensional observation section.

For the admitted oriented spin Lorentz four-bases, an almost-complex structure
on TX supplies J_Q over Y by pullback and tensoring with L. Whenever the
corresponding metric section is admitted, restriction gives the converse.
Hence, with the same orientation/section qualifications as the prior result,

    some normal SU(3,2) reduction compatible with fixed Spin
      ⇔ some normal U(3,2) reduction
      ⇔ TX admits the matching almost-complex structure.

On a connected noncompact base or compact base with nonempty boundary this
absolute existence follows in the existing spin scope. For closed X retain
exactly the earlier integral condition

    rho2(c)=w2(TX),  c²=p1(TX)+2e(TX);
    for spin Lorentz X: c=2a, 4a²[X]=3 signature(X).

No new claim that the closed square condition is universally soluble is made.
In particular, special-unitary normal existence does **not** require c1(TX)=0,
zero signature, or zero c1 on each factor. The already-owned positive example
K3#12(S1×S3), with c²=-48, remains valid by cancellation on the positive factor.

## 5. Fixed-data and torsion controls

| Data held fixed | Exact condition or conclusion |
|---|---|
| J_Q and total Spin; J_P and volume free | Existence automatic over dim≤7 by S7 lifting. |
| Both J_P and J_Q fixed; no specified Spin | SU exists iff c1(P,J_P)+c1(Q,J_Q)=0 **integrally**. |
| Both J fixed; determinant trivial; Spin s fixed | Fix a volume v0 with induced s0. A phase change realizes s iff s−s0 lies in im(H1(B;Z)→H1(B;Z2)). |
| J and volume fixed | They induce one Spin structure; compare it with s, not just w2. |
| Connection prescribed | Need parallel J and preserved volume; topological existence says nothing about this. |
| Boundary/end reduction prescribed | Relative extension problem; the source supplies no such datum here. |

The phase criterion follows from the double cover of U(3,2): a loop lifts
precisely when its **total** determinant winding is even. Changing volume by
u:B→U(1) changes its induced Spin class by rho2([u]). By the coefficient exact
sequence the obstruction is the Bockstein of s−s0 in H2(B;Z). Thus determinant
triviality alone cannot match every Spin structure with J fixed.

Two controls can be realized on admitted parallelizable Lorentz four-bases:

- **Torsion determinant.** X=R×L(4,1) retracts to a three-dimensional lens
  space. H2(X;Z)=Z4, generated by a. Let L be the complex line with c1=a.
  The positive complex rank-three bundle L⊕L⊕1 has c1=2a≠0 but w2=0;
  its underlying oriented real rank-six bundle is trivial. Here oriented
  real bundles of rank≥3 over a three-complex are classified by w2.
  Transport it to the trivial native positive bundle and choose the negative
  constant complex structure. This fixed normal J has nontrivial determinant
  despite zero real/de Rham c1. Changing J_P removes the obstruction.
- **Spin phase.** X=R×RP3 is also parallelizable. H1(X;Z)=0 while
  H1(X;Z2)=Z2. For the trivial normal bundle, choose a determinant-trivial J
  and its volume-induced s0, and prescribe the other Spin lift s. No volume
  phase repairs it with that J fixed. This is a control for a prescribed
  total Spin, not a claim that the source's inherited Spin is the other one.
  The theorem permits changing J_P and works for either prescribed lift.

Neither control defeats the existential theorem. They reject the stronger
fixed-data statements and prevent rational-cohomology or phase-only shortcuts.
The rank-six prescribed-c1 statement also does not extend without new work
above homotopy dimension seven. Conversely a source-owned low-dimensional
relative pair might be handled by the S7 argument after compatible lower-stage
data is fixed; no blanket relative obstruction or automatic extension of
arbitrary imposed data is asserted here.

## 6. Verification and consequence

The proof covers the whole declared bundle category. The finite probe checks
Lie stabilizer/orbit dimensions, winding parity and integral torsion/phase
controls; it does not certify obstruction theory by computation. Independent
specialist review checks the group-cover and fixed-Spin argument. This is T2
conditional research, not Lean or independent-human certification.

[Probe](../../tests/program-focus/normal_special_unitary_probe.py),
[evidence](../../lab/process/normal-special-unitary-existence-2026-11-25.json),
[review](../../lab/process/hostile-reviews/2026-11-25-normal-special-unitary-review.md).

**Actual delta:** W09's additional absolute determinant/Spin uncertainty is
resolved positively. There is no new topological falsifier here and no need
for repeated determinant-existence calculations in the same category. Selection,
connection preservation and specified relative data remain different questions;
they become scientific continuations only with their relevant inputs. The
ordinary program selection and discovery cadence remain in force.
