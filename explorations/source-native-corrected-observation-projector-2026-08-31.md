---
artifact_type: exploration
status: exploration
doc_type: representation_bridge_candidate
created: 2026-08-31
title: "A canonical algebraic correction into the observed Clifford kernel"
target_claim: "INTERNAL — a split-surjective observed Clifford contraction canonically supplies a trace-subtraction projector and kernel-times-trace decomposition; verdict: CONSTRUCTED at exact algebraic grade, not source-owned or physical"
source_claims: [SC-FER-04, SC-FER-05, SC-FER-07, SC-GEN-51, SC-GEN-52]
canon_verdict_change: none
probe: tests/channel-swings/source_native_corrected_observation_probe.py
lean: Lean/GUFormalization/SourceNativeCorrectedObservation.lean
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact split-surjective projector and kernel-times-trace decomposition for a supplied observed Clifford contraction
carrier: abstract observed one-form-spinor module B LAYER=observed CHIRALITY=S-CHIRALITY-UNTYPED
pairing: NONE
real_structure: UNTYPED; no scalar-antilinear or Krein structure is used or inferred
grading: observed gamma kernel versus supplied trace complement; no physical chirality or family grading is assigned
action_owner: repository-construction -- source/action/dynamics ownership remains open
target: ker(Gamma_B) together with the explicit linear equivalence B ~= ker(Gamma_B) x S MAP-TYPE=isomorphism
```

# A canonical algebraic correction into the observed Clifford kernel

## Result in one sentence

Whenever the observed Clifford contraction `Gamma_B : B -> S` comes with a
right inverse `j_B : S -> B`, exact linear algebra canonically supplies the
projector

```text
P_B = 1_B - j_B Gamma_B
```

onto `ker Gamma_B`, an equivalence `B ~= ker(Gamma_B) x S`, and a corrected
observation `P_B P_s` that cancels the literal-pullback leakage proved on
2026-08-30.  This constructs a corrected **algebraic** kernel; it does not show
that Weinstein's source, an action, a constraint complex or physical dynamics
selects this projector.

## 1. Preflight, source scope and retrieval

The prior result fixed the exact obstruction.  Literal section pullback
`P_s` can send an ambient gamma-traceless one-form spinor to an observed
one-form spinor with nonzero observed gamma trace.  It named three possible
reopeners: a source-owned intertwiner, a corrected observed kernel with
representation meaning, or action/BV/boundary/domain cohomology.

Searches by object rather than wording covered gamma-trace projector,
Rarita--Schwinger projector, split exact sequence, kernel complement, trace
subtraction, section-pullback intertwiner and observation quotient.  The
repository already had:

- the general leakage theorem in
  `Lean/GUFormalization/SourceNativeSpin64Observation.lean`;
- the exact factorization criterion in
  `Lean/GUFormalization/SourceNativeObservationDescent.lean`; and
- projectors on other RS or Shiab carriers whose domains and purposes do not
  identify them with the observation map tested here.

It did not have the split projector on the observed carrier, its direct-sum
classification, or the exact relation between literal and corrected
observation.  The current correction registry supplies no later source change
that selects such a projector.

## 2. Route selection and claim ceiling

The split-linear route dominates a new dimension census: the dimensions and
the existence of a gamma-trace right inverse are already owned, while the open
question is what exact additional map repairs leakage.  It also dominates a
new index calculation, because an index cannot make a noncommuting carrier
square commute.

The work used three separated packets:

1. a Lean proof of the projector, fixed-point law, idempotence, direct-sum
   equivalence and corrected-observation laws;
2. an independent exact Clifford-matrix realization of the old leakage
   witness and new correction, including hostile wrong-map controls; and
3. source-scope integration and hostile review.

Cheapest switch condition: if `P_B` did not land in `ker Gamma_B`, failed to
fix that kernel, or did not split every `b` uniquely into kernel plus trace,
the route would stop as a false correction.  None fires.  The physical route
does not automatically open, because selection and representation meaning are
separate premises.

## 3. Exact construction

Assume only

```text
Gamma_B j_B = 1_S.
```

For every `b in B`, define

```text
k(b) = b - j_B Gamma_B(b).
```

Then

```text
Gamma_B k(b)
  = Gamma_B(b) - Gamma_B j_B Gamma_B(b)
  = 0.
```

Thus `P_B(b)=k(b)` lands in the observed gamma kernel.  If `b` is already in
that kernel, `P_B(b)=b`; conversely, if `P_B(b)=b`, applying `Gamma_B` proves
`Gamma_B(b)=0`.  Therefore the fixed points of `P_B` are exactly
`ker Gamma_B`, and `P_B^2=P_B`.

The complete carrier decomposition is explicit:

```text
Phi : B -> ker(Gamma_B) x S,
Phi(b) = (P_B(b), Gamma_B(b)),

Phi^{-1}(k,s) = k + j_B(s).
```

The two formulas are mutual linear inverses.  No dimension, basis, field,
inner product or positivity assumption enters.

For any literal observation map `P_s : A -> B`, define

```text
P_s^corr = P_B P_s.
```

It obeys

```text
Gamma_B P_s^corr = 0,
P_s = P_s^corr + j_B Gamma_B P_s,
P_s^corr(a) = P_s(a)  iff  Gamma_B P_s(a)=0.
```

Hence the correction removes exactly the trace leakage and nothing from an
already gamma-traceless output.  If literal observation already preserves an
ambient gamma kernel, corrected and literal observation agree on that kernel.

## 4. Exact independent reproduction

The finite probe uses rational arithmetic and real `Cl(1,1)` generators.  Its
observed carrier has two covector-spinor slots and contraction

```text
Gamma_B(b_0,b_1) = X b_0 + J b_1,
j_B(s) = (X s,0),
```

with `X^2=1`, so `Gamma_B j_B=1`.  It independently checks:

- the right-inverse law on a basis;
- zero output trace, idempotence, reconstruction and exact trace coordinates
  on three carrier samples;
- the held ambient-kernel/literal-observed-trace leakage witness;
- cancellation of that witness by `P_B`;
- preservation of an independent hand-built kernel element; and
- hostile identity and wrong-sign corrections, both of which retain nonzero
  trace.

All `23/23` checks pass.  The general claim rests on the Lean proof, not on the
finite model; the model is an independent non-vacuity and mutation control.

## 5. What moved and what did not

Moved:

- the corrected observed gamma kernel is now an exact algebraic construction,
  not merely a requested object;
- the full observed carrier is exactly classified as gamma kernel plus trace
  carrier under the supplied split; and
- the prior leakage witness now has a minimal coefficient-complete algebraic
  repair candidate and an exact acceptance law.

Did not move:

- source ownership of `j_B`, `P_B` or `P_s^corr`;
- an action, Euler equation, constraint/BV complex, boundary condition or
  common physical domain selecting the correction;
- representation meaning of the corrected kernel or its quotient;
- observed `2+1`, physical chirality, family count, mass, coefficient, scale,
  threshold, prediction, GU verdict, canon, paper, release or public posture.

The old obstruction is not retracted.  Literal pullback still fails.  The new
map is extra structure, and calling it “the observation map” without an owner
would repeat the exact source-attribution error the routing discipline forbids.

## 6. Hostile review

**Strongest overclaim.**  A canonical projector relative to supplied
`Gamma_B,j_B` is not canonical from the source alone.  Different right
inverses give different complements even though they have the same kernel.
The construction is canonical only after the split is supplied.

**Strongest contrary construction.**  Physical cohomology may quotient by a
constraint complex whose representatives are not the image of `P_B`; a
boundary condition may select a different complement; or the source-owned
observation map may carry a nontrivial spinor intertwiner.  Any of those can
replace this algebraic candidate without contradicting the theorem.

**Weakest seam.**  The right inverse is representation-grade Clifford trace
insertion.  The source/action has not fixed its normalization, real/Krein
adjoint, domain or compatibility with observation dynamics.  The theorem is
valid for every supplied split and therefore cannot select among them.

**Reproducibility seam.**  Lean uses only `propext`/quotient-free ordinary
linear algebra expected from Mathlib; the exact axiom receipt records the
actual dependencies.  The finite probe has real failure paths: identity and
wrong-sign mutations fail the defining trace condition.

## 7. Exact next condition

Reopen this arc only when one of the following supplies representation or
physical meaning:

1. a source/action-owned choice of `Gamma_B` and `j_B` together with the
   one-form/spinor observation intertwiner;
2. a constraint, BV/BFV, boundary or domain complex proving that `P_B` induces
   the physical cohomology/quotient and is independent of representative; or
3. a contrary source-owned complement or intertwiner that replaces `P_B` and
   can be tested against the same kernel/trace acceptance laws.

Until then the honest state is: corrected kernel **constructed algebraically**,
observed sector **uninterpreted physically**.
