---
title: "A Literal-Observation Obstruction for Ambient Gamma Kernels"
author: "Joseph Hernandez"
status: draft
document_role: draft
operational_state: working
claim_verdict: exact
updated_at: "2026-09-02"
---

# A Literal-Observation Obstruction for Ambient Gamma Kernels

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

~~~gu-typed-objects
result: LITERAL-OBSERVATION-GAMMA-KERNEL-OBSTRUCTION
carrier: abstract ambient one-form-spinor module A=H times N with supplied horizontal and normal Clifford contractions into S, and observed horizontal carrier H LAYER=source-print+observed CHIRALITY=S-FULL-DIRAC
pairing: NONE; the theorem uses only module-linear Clifford contractions and a supplied right inverse for the normal contraction
real_structure: UNTYPED; the obstruction is scalar-linear and does not identify a physical real or Krein sector
grading: ambient gamma kernel versus observed horizontal gamma kernel; no family, chirality, mass or physical grading is assigned
action_owner: repository construction owns the kernel witness; source/action ownership of observation, correction, quotient and physical interpretation remains open
target: MAP-TYPE exact linear theorem proving that literal horizontal pullback need not map ker(Gamma_A) into ker(Gamma_H)
~~~

## Abstract

Split an ambient one-form-spinor carrier as `A = H × N`, with Clifford
contraction

    Gamma_A(h,n) = Gamma_H(h) + Gamma_N(n),

and let literal observation discard the normal component:

    P(h,n) = h.

If `Gamma_N` has a right inverse and some horizontal element has nonzero
Clifford trace, then that element has an explicit ambient gamma-traceless lift
whose literal observation retains the nonzero trace. Hence

    P(ker Gamma_A) is not contained in ker Gamma_H.

The obstruction is exact module-linear algebra and requires no dimension
count. A separately supplied observed right inverse gives the familiar
trace-subtraction projector and removes the leakage algebraically, but neither
that correction nor this obstruction classifies the physical leftover or
constructs a source/action-owned quotient.

## Frozen objects and premises

Let `R` be a ring and let `H`, `N`, and `S` be `R`-modules. Freeze:

1. **Ambient split.** The carrier is `A = H × N`, with horizontal and normal
   one-form-spinor summands kept distinct.
2. **Clifford contractions.** Linear maps `Gamma_H : H -> S` and
   `Gamma_N : N -> S` define
   `Gamma_A(h,n)=Gamma_H(h)+Gamma_N(n)`.
3. **Normal right inverse.** A linear map `j_N : S -> N` obeys
   `Gamma_N j_N = id_S`.
4. **Literal observation.** `P : A -> H` is the first projection
   `P(h,n)=h`; it does not include a compensating spinor intertwiner or
   trace subtraction.
5. **Nonzero horizontal trace.** There exists `h in H` with
   `Gamma_H(h) != 0`.
6. **Interpretive ceiling.** No source/action-owned corrected observation,
   constraint complex, representative-independent quotient, boundary/domain
   law or physical-sector classifier is supplied.

Premises 1--5 are the exact algebraic denominator. Premise 6 prevents a
failure of the literal map from being mistaken for a classification theorem.

## Theorem

**Literal-observation gamma-kernel obstruction.** Under premises 1--5, define

    t_h = (h, -j_N Gamma_H(h)).

Then

1. `Gamma_A(t_h)=0`, so `t_h` lies in the ambient gamma kernel;
2. `P(t_h)=h`; and
3. `Gamma_H(P(t_h))=Gamma_H(h) != 0`.

Consequently, literal observation does not map the ambient gamma kernel into
the observed horizontal gamma kernel. Under premise 6, the theorem does not
identify, count or physically classify the leaked observed trace component.

## Proof

By linearity, the definition of `Gamma_A`, and the right-inverse law,

    Gamma_A(t_h)
      = Gamma_H(h) + Gamma_N(-j_N Gamma_H(h))
      = Gamma_H(h) - (Gamma_N j_N)(Gamma_H(h))
      = 0.

Thus `t_h` belongs to `ker Gamma_A`. Literal observation is the first
projection, so `P(t_h)=h`. Applying the observed horizontal contraction gives
`Gamma_H(P(t_h))=Gamma_H(h)`, which is nonzero by premise 5. This is an explicit
witness against the proposed kernel inclusion. The calculation names no
quotient or physical interpretation, so premise 6 leaves the observed
leftover unclassified. ∎

## Corollaries and exact boundaries

The witness is stronger than a dimension mismatch: it gives an element and
uses no finite-dimensional assumption. It is weaker than a universal
observation no-go: a different map carrying extra structure can preserve or
replace the relevant kernel.

In particular, if `Gamma_H` itself has a supplied right inverse `j_H`, then

    Q_H = 1_H - j_H Gamma_H

obeys `Gamma_H Q_H=0`, and `Q_H P` sends every ambient input into the observed
gamma kernel. The repository already owns this corrected-projector theorem.
It is an exact escape from the literal-map obstruction, not a refutation of
it. Different supplied right inverses can select different complements, and
the algebra does not prove that the source, an action, a constraint complex or
physical dynamics chooses `Q_H`.

The theorem also does not say that every ambient kernel element leaks. It says
that one leaks whenever the frozen right inverse and nonzero horizontal trace
exist. Nor does it infer a family count from the dimensions `144`, `832` or
`1664`; those remain representation controls only.

## Preflight, prior art, and route choice

Object-level retrieval preceded construction. The 2026-08-30 source-native
Spin(6,4) exploration already supplied the general proof and exact finite
Clifford witness. `SourceNativeSpin64Observation.lean` already kernel-checks
the module-linear theorem. The 2026-08-31 corrected-observation exploration
and Lean module already own the algebraic trace-subtraction escape. This
package contributes the self-contained theorem, premise/reopener ledger,
independent baseline-first certificate and reproduction boundary; it does not
claim a new Clifford calculation.

The split-module route dominates a new branching or dimension census because
the decision question is functorial kernel preservation. It also dominates an
action or quotient construction: no owner for either is present, and the
current gate expressly forbids classifying the physical leftover without one.

## Hostile review

**Strongest overclaim.** “The observed Rarita--Schwinger sector is
inconsistent or physically absent.” Refused. Only literal pullback fails the
stated kernel inclusion. A corrected observation, quotient or dynamical
sector can still exist.

**Strongest contrary construction.** A source-owned intertwiner could make the
Clifford square commute, or an action-owned cohomology could define physical
classes after quotient. The existing split projector is an explicit algebraic
positive control. Any owned construction must be tested independently against
this witness.

**Strongest mistyping risk.** `P` acts on the one-form slot by discarding the
normal component. It is not a projector from the ambient spinor module onto a
physical observed spinor sector, and `ker Gamma_H` is not called a physical
state space.

**Weakest reproducibility seam.** The independent finite certificate uses one
real `Cl(1,1)` realization, so it demonstrates nonvacuity rather than proving
the general theorem. The Lean certificate checks the general theorem from the
explicit right-inverse premise.

## What this settles—and what it does not

The package settles an exact map-level statement: a normal right inverse lets
every nonzero horizontal trace be canceled by a normal component before
observation, and literal observation deletes that cancellation. Ambient
gamma-tracelessness therefore does not automatically descend.

It does not construct the source observation factor, choose a Clifford right
inverse or corrected projector, define a physical quotient, classify the
leaked component, derive observed `2+1` sectors, assign chirality or families,
produce a mass or interaction, predict an observable, confirm or falsify
Geometric Unity, or promote a publication candidate.

## Reproduction

Run:

~~~sh
python3 papers/drafts/literal-observation-gamma-kernel-obstruction/reproduce_all.py
~~~

The integrated certificate runs its clean baseline before hostile premise
mutations, then the capsule reruns the upstream exact Clifford controls and
both relevant Lean kernels.
