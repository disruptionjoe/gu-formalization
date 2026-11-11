---
title: "X-P1-P2: coefficient compatibility and pairing precede a class-wide weld"
status: active_research
doc_type: exploration
created: "2026-11-11"
program_target: X-P1-P2
tier: T1
expected_delta: "decided_for_C only if universal coefficient/pairing premises hold; otherwise refine constrained requirements"
actual_delta: "constrained: exact weighted-coefficient existence condition and action-pairing identity remain separate premises"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: "No full class-C counterexample, universal weld, datum floor or source verdict"
scripts:
  - tests/program-focus/x_p1_p2_weld_scope_probe.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`. This tests Part A of the
[two-datum packet](../../lab/process/work-packets/two-datum-theorem-2026-11-10.md).
The original geometric coflip and reconstructed-symbol weld are retained.

```gu-typed-objects
result: X-P1-P2-weld-scope
carrier: twenty labeled observer branching slots, one-dimensional equivariant symbol cells, and pairing controls LAYER=UNTYPED (algebraic inference, not a physical carrier identification) CHIRALITY=N/A
pairing: explicit action pairing P versus fixed Krein K ON=declared_carrier
real_structure: complex symbol scalars and antilinear coflip; real rational first-order pairing control
grading: geometric return, symbol compatibility, scalar phase uniqueness and class-C action membership are distinct
action_owner: N/A -- structural implication test; no candidate field action selected
target: conditional coefficient and pairing requirements MAP-TYPE=intertwiner
```

## Result and native bookends

- program_target: X-P1-P2
- tier: T1 attempted; constrained final scope
- expected_delta: decide for C only after proving both universal premises
- actual_delta: constrained requirement refined; no class-wide decision

The proposed lift from one reconstructed differential to every action in C is
not established. There are two independent issues:

1. Connected nonzero support proves uniqueness of a compatible scalar-phase
   extension, not existence of one. Mirror coefficient equations carry weights.
2. Helmholtz symmetry refers to the action's density-dual pairing. It does not
   identify that pairing with the fixed Krein form used by the weld.

The exact controls below refute these inference steps in their declared algebraic
categories. They are not asserted to satisfy every naturality, gauge, action,
BV or boundary condition of C; consequently they are not counterexamples to an
actual universal class-C weld. The matrix remains constrained.

## 1. What the old calculation actually uses

The [July probe](../../tests/channel-swings/full20_dewitt_loop_transport_probe.py)
computes its uniform returned coflip mismatch -I in section E, before introducing
the nine differential primitives in section F. Section G then checks actual
coefficient intertwiners for those formulas, before reducing slot phases to one
global class. Its last connectivity step is conditional on those earlier checks.

The exact multiplicity matrix reconstructs twenty labeled slots and 136 directed
nonzero cells. Its undirected support has 68 edges, one component, no bridge, and
cycle rank 49. Each cell is one-dimensional. Repeated isotypic copies retain their
provenance labels. Multiplicity one within a cell does not remove multiplicity
mixing between those copies.

The fixed geometric result is independent of scalar coefficient reweighting
because the differential has not entered that calculation. It is also unchanged
by constant scalar modifications of the coflip on each transported slot: if
C_1=-C_0, then (p C_0)^(-1)(p C_1)=-I. Thus that endpoint alone cannot eliminate
independent slot phases or establish covariance of an arbitrary differential.
We reuse this earlier geometric result at its stated grade; we do not rerun its
large operator computation or upgrade it to a class-C theorem.

## 2. Exact weighted compatibility and an all-nonzero control

In the coefficient formulas in this section, C_i denotes the complex matrix
part of the antilinear map z |-> C_i conjugate(z). Fix the canonical nonzero
basis intertwiners B_e of the July reconstruction, with
C_t conjugate(B_e)=B_m(e) C_s (including its fixed vector transformation).
For an observer-equivariant symbol A_e=c_e B_e and scalar-slot coflip C'_i=p_i C_i,
compatibility requires

    p_t conjugate(c_e) = p_s c_m(e),   e:s -> t.             (1)

This is a necessary and sufficient coefficient equation within this fixed-basis,
scalar-slot ansatz. It is not a classification of general provenance-mixing
coflips. Schur multiplicity one says c_e is a scalar; it does not say the two
scalars in (1) are equal.

Take all 136 coefficients equal to 1 except

    S:E+:L16+ -> S:E-:R16+, and its transpose,

which have coefficient 2. Their distinct mirror pair retains coefficient 1.
Every cell remains nonzero; the full support remains connected. The two directed
equations give

    2p_t=p_s, 2p_s=p_t, hence 3p_s=3p_t=0.

No nonzero scalar phases solve them over C. This is stronger than failing a
unit-modulus phase condition. Scaling a transpose pair together preserves any
already-established homogeneous transpose-adjoint relation for that pair, but
that observation neither establishes all action relations nor certifies class-C
membership. It is an exact H-equivariant symbol-space discriminator.

Therefore disconnected support is not the only obstruction in that symbol space.
Randomizing only mirror-matched coefficients would assume precisely the missing
premise. The original fixed geometric return remains -I for this control, while
differential compatibility fails in the scalar ansatz.

## 3. Correct conditional graph theorem and its consumer

For nonzero cells put lambda_e=c_m(e)/conjugate(c_e). For unit scalar phases,
(1) becomes p_t=lambda_e p_s. Add the mirror-identification relations p_m(i)=p_i
required by the coflip involution. Treat every directed equation as an oriented
edge with its stated weight; traversing it backwards uses the inverse weight.
If both cell directions exist, both equations are retained, so their two-edge
cycle is a real consistency condition.

A solution exists exactly when all edge weights have modulus one and every
closed walk in this augmented weighted graph has product one. Necessity follows
by taking phase ratios. For sufficiency choose one root phase per connected
component and transport it along a path; the closed-walk condition gives path
independence. Every solution is obtained this way. Thus connectedness yields one
global phase **after compatibility has been proved**. A spanning forest and the
remaining edge equations suffice to test the closed-walk condition.

For canonical real mirror-matched coefficients every lambda is 1. The old
phase propagation is this special case. A disconnected balanced example permits
one relative phase per component of the graph **including mirror edges**; raw
support components alone need not count the freedom correctly. The probe supplies
both a balanced positive family and a planted cut with two augmented components.

This is a structural condition on coefficient space, not a fitted action. For
any class-C subfamily whose actual symbols satisfy this condition in the fixed
scalar ansatz, the phase-uniqueness step follows. Whether C forces that subfamily,
or admits more general coflips, remains open.

## 4. Independent Helmholtz/pairing control

For compactly supported real fields, the second variation is symmetric as an
operator into the density dual. In a constant frame the first-order operator
J partial_x is formally symmetric when J^T=-J: integration by parts supplies the
extra minus sign. Raising the dual with an action pairing P produces
A=P^(-1)J and formal P-symmetry A^T P+P A=0. It does not select another form K.
This is the pertinent Helmholtz boundary; see the
[primary variational reference](https://www.dml.cz/handle/10338.dmlcz/137524).

The exact rational control is

    P=diag(1,-2), K=diag(1,-1), J=[[0,1],[-1,0]], A=P^(-1)J.
    A^T P+P A=0,
    A^T K+K A=[[0,1/2],[1/2,0]] != 0.

It can be read as the finite first-order variational control S=1/2 integral
phi^T J partial_x phi on a test-function line. This is a control of the logical
implication only, not a guessed GU action or a field-theory candidate. Replacing
P by K supplies the positive control. The action coefficients are not being
searched or fitted.

The [curved B5 result](../b5-curved-coflip-green-transport-2026-08-20.md) fixes K
for its named strict quadratic branch; it does not authenticate P=K for every
member of C. A universal lift must prove pairing identification or derive the
correct transport of the adjoint/coflip data from the actual pairing. Reality
alone leaves this inference unproved.

## 5. Consequence, acceptance and remaining question

X-P1-P2 remains constrained with explicit weighted compatibility and pairing
premises. The July finite-associated-bundle result is not withdrawn. Neither
control certifies an action in C, so no class-C counterexample, source verdict,
or extra physical sign datum is asserted. In particular it would be premature
to replace the ledger with either “exactly two data” or “two data plus a sign”.
Part B separately showed why blanket additive forgetting cannot establish its
floor. The conjunction of two unproved extensions does not repair either one.

The useful next structural questions are whether full natural/gauge covariance
forces the weighted coefficient relations, whether the permitted variational
pairing is uniquely identified with K, and what changes when provenance-mixing
coflips are allowed. These require their actual representation/naturality or
pairing premises; building a missing source action is not the authorized route.
They are alternatives to other matrix intersections and the class-width witness,
not a compulsory chain of numerical reweightings.

The exact probe rebuilds native support/multiplicities and tests weighted cycles,
positive and cut controls, fixed-return separation and the rational pairing
countercontrol. The [Lean file](../../Lean/GUFormalization/WeldCoefficientScope.lean)
proves equality propagation along reachable edges and the inconsistent two-cycle.
It does not certify representation theory, geometry, field-action membership,
the full weighted graph theorem, or the Helmholtz theorem. These remain explicit
written arguments, cited provenance and exact algebraic controls. Internal
specialist/adversarial review is not external-expert certification.

[Probe](../../tests/program-focus/x_p1_p2_weld_scope_probe.py) ·
[Report](../../lab/process/x-p1-p2-weld-scope.json) ·
[Matrix](../../lab/process/action-constraint-matrix.json).
