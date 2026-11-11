---
title: "P3: locality and arbitrary-parameter gauge identities"
status: active_research
doc_type: exploration
created: "2026-11-11"
program_target: P3xvariational
tier: T2
expected_delta: "derive a structural constraint without a full-C decision"
actual_delta: "constrained: isolated generically invertible kinetics require trivial local linear gauge action; coupled completion needs symbol degeneracy"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: "No source verdict, class-C exclusion, realized physical count or action witness"
scripts:
  - tests/program-focus/p3_rs_local_gauge_necessity_probe.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`. No conventional-index conclusion is
transported to the native two-true-plus-effective-imposter observation construction.
SC-GEN-02/03/54 ASSERTS the native generation/supercharge claims; SC-CHI-01/51 ASSERTS
the nonchiral-total/effectively-chiral split with the source's stated qualifications.
This note does not adjudicate those claims. RA-F1, AC-F1 and LT-SM8 remain NEEDS.

```gu-typed-objects
result: p3-rs-local-gauge-necessity
carrier: smooth finite-rank bundles and finite-order differential operators; projected geometric RS as a conditional instance LAYER=UNTYPED (structural mathematics, not identified physical states) CHIRALITY=N/A
pairing: explicit topological pushforward or symbol composition ON=declared_carrier
real_structure: real metric geometry with complex K or Clifford modules; no physical reality transport
grading: K parity and symbol source/target grading are explicit; no multiplicity-to-count inference
action_owner: N/A -- structural subfamily requirement, no action constructed
target: P3xvariational MAP-TYPE=homomorphism
```

## Native bookends

program_target: P3xvariational
tier: T2
expected_delta: derive a structural constraint without a full-C decision
actual_delta: constrained: isolated generically invertible kinetics require trivial local linear gauge action; coupled completion needs symbol degeneracy

## 1. Exact theorem at the local differential level

Let Q:C∞(E)->C∞(E') be a smooth finite-order square linear differential operator.
At every point x assume its highest-order symbol q(x,xi) is invertible on a
nonempty open subset of the real cotangent fibre. Let R:C∞(G)->C∞(E) be any
finite-order local linear differential operator satisfying QR=0 on arbitrary smooth
parameter sections. Then R=0.

Proof: if R has order m, its top composition symbol is q r_m=0. At each x,
r_m vanishes on the open invertibility set. Every entry of r_m is a polynomial
in xi, so it vanishes identically on that fibre. Hence the top coefficients of
R vanish everywhere; lower its order and repeat. At order0 the same argument
annihilates the multiplication map. Smooth rather than analytic coefficients
suffice because polynomiality is in covectors, separately at each base point.
The argument also gives no nonzero left local differential identity LQ=0.

For a variational system, at a stationary background an arbitrary-parameter
linearized gauge transformation obeys H R=0 for the full Hessian H. Thus an
isolated H satisfying these hypotheses has zero linearized local gauge action.
This neither excludes nonlinear symmetries whose linearization vanishes there
nor says gauge-fixed H must retain the ungauge-fixed redundancy.

## 2. Application and exact new delta

The [carrier-bit leg2](../../tests/carrier-bit-decision/leg2_obstruction_hardening.md)
already proves the projected geometric RS symbol is invertible at non-null
covectors, generically, and already computes the failed projected-gradient
composition. Those are reused results, not new progress here. At each point,
a nondegenerate Clifford metric has a non-null open set; the same algebraic
symbol type supplies the theorem's hypothesis for n>2. Smooth zero-order
perturbations do not affect it.

That record also exhibits a nonzero null-cone kernel and leaves
characteristic-supported gauging open at its pointwise scope. The new locality
conclusion is precise: such cone-only values cannot be the symbol of a nonzero
finite-order local R satisfying QR=0 on unrestricted parameters. A polynomial
cannot be nonzero only on the null cone. On-shell characteristic modes and
parameters satisfying their own wave equation are different objects; their
existence survives. General distributional multipliers are also outside this
finite-order differential theorem. No claim about all nonlocal transformations
is made.

This is the same highest-symbol method as the separate scalar statement in
[K2525](k2525-metric-bundle-section-action-2026-11-02.md), now applied with the
actual RS invertibility input to an explicit unresolved locality question.
No stabilized action is constructed. No conclusion about the full source
field system follows from an isolated diagonal block.

## 3. Executed coupled-field repair and its required condition

For a coupled principal symbol with compatible common order (or a declared
weighted principal-symbol convention), write

    H = [ Q  B ; C  D ],  H (r,s)^t = 0.

On the open set where Q is invertible,

    r = -Q^-1 B s,   (D-C Q^-1 B)s = 0.

Thus nonzero coupled redundancy with s nonzero needs a singular Schur complement
where its leading parameter component s is nonzero. In the common-order convention,
if the full H is invertible on a nonempty open covector set at every base point,
the preceding polynomial theorem again forces every finite-order gauge generator
to vanish. Invertibility on only a nonempty open region of base points does not establish a global conclusion. If B=0, the isolated
RS component r vanishes but a companion gauge transformation may remain.
A singular Schur complement is necessary, not sufficient for a polynomial lift,
a full differential identity, global bundle descent or a nonlinear BV structure.

An exact first-order SYMBOL control demonstrates the repair: with a covector
coordinate p, take H=p[[1,1],[1,1]] and R=(1,-1)^t. Its Q=p block is invertible
when p is nonzero, yet HR=0 identically because the Schur complement vanishes.
This is a block-symbol countercontrol, not a guessed action in lane B or a
native RS realization. It proves the isolated-block argument cannot be extended
to a coupled system. The actual full vector-spinor RS symbol/ghost complex in
leg2 is another retained repair with a different off-shell carrier.

## 4. Matrix consequence and limits

P3xvariational becomes constrained with the original stabilized-action gate
retained as an unrealized analytic input. A structurally defined C subfamily
whose complete ungauge-fixed stationary kinetic operator is isolated geometric
Q cannot insert a nontrivial local linear gauge differential for that block.
A coupled candidate must demonstrate symbol degeneracy and the actual local
identity before subtracting ghost indices. This does not prescribe or construct
such a candidate. Raw Q, full vector-spinor, ghost complex and gauge-fixed Q are
separate. No class-C existence or emptiness, interacting positivity, physical
cohomology, source verdict or ghost count is established.

## Reproduction and acceptance

[Exact supporting probe](../../tests/program-focus/p3_rs_local_gauge_necessity_probe.py)
and [replay report](../../lab/process/p3-rs-local-gauge-necessity.json) accompany the written proof.
Finite checks test algebra and contrary controls; they do not certify topology,
all differential operators, physical applicability or an analytic APS family.
Independent internal specialist review and an integrated adversarial review
completed with all substantive findings resolved; saved exact reports replay. No Lean certification is claimed for this T2 result.
