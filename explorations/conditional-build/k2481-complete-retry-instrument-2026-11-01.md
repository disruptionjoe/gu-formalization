---
title: "K2481 Complete retry instruments, memory and sharp calibration"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "exact supplied finite-dimensional retry effects and sharp full-instrument calibration; no original Q/T realization or native GU physical identification"
---

# K2481 Complete retry instruments, memory and sharp calibration

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2481
carrier: supplied finite-dimensional positive-Hilbert instruments including retained memory and classical terminal records LAYER=toy CHIRALITY=N/A
pairing: positive trace pairing and complete arbitrary-reference channel distinguishability ON=declared_carrier
real_structure: complex adjoint on operators and real outcome probabilities
grading: reached classical histories and terminal wrong-correct-no-output records
action_owner: repository-construction -- supplied conditional mathematical models
target: Exact complete-instrument retry risk and robust reset interface MAP-TYPE=evaluation
```

## Result and semantic boundary

K2478's classical risk design requires reached-history calibration that an
acceptance POVM alone cannot supply. Complete quantum instruments give exact
finite/adaptive retry effects and an infinite-horizon completion criterion.
Two instruments with identical effects have different retry error. Uniform
complete-instrument error delta and ideal completion floor p yield a sharp
conditional-risk degradation delta/p, including one shared calibration event.
This is a supplied positive-Hilbert interface, not an implementation of the
original 108-dimensional Q/T verifier or a GU physical-state construction.
SC-META-53 remains UNCERTAIN; ledger0.263, source polarities and canon remain unchanged.

Layer 0 distinguishes an acceptance effect from its state-update instrument,
and a mathematical wrong/correct performance audit from information available
to the controller. H includes every retained memory subsystem; accepted output
may have a different carrier K. Arbitrary-reference calibration covers input
entanglement. None of these positive trace/instrument premises follows from
the indefinite native pairing. A conditional risk theorem is not a derivation
of physical probabilities.

## 1. Exact complete-map retry effects

Let W,C,N be completely positive trace-nonincreasing maps on finite-dimensional input H, with output direct sum W,C,N trace preserving. W and C can be mathematical refinements of an accepted output A using a fixed binary performance audit F on K: E_W=A*(F), E_C=A*(I-F). The audit need not actually be measured; accepted output stops. N includes all retained memory and the declared retry/reset operation. Write E_W=W*(I), E_O=E_W+C*(I)=I-N*(I). The three flags have fixed performance meaning across attempts.

For m>=1 attempts stopping at first output, define

 A_m=sum_(k=0)^(m-1) (N*)^k E_W,
 B_m=I-(N*)^m I.

For every initial density matrix rho, wrong mass is tr(rho A_m), output mass is tr(rho B_m). Proof: compose the subnormalized no-output states N^k(rho), sum the disjoint terminal probabilities, and telescope E_O=I-N*I. No independent-attempt assumption occurs. In particular 0<=A_m<=B_m<=I.

If B_m is nonzero, the exact worst conditional error over all initial states producing output is

 lambda_max(B_m^(-1/2) A_m B_m^(-1/2))

on supp(B_m), using the support inverse. Equivalently it is the least eta such that A_m<=eta B_m. Kernel(B_m) is in kernel(A_m); pure states attain the generalized Rayleigh quotient. If B_m=0 the conditional quantity is undefined, not zero. Restricting the initial-state class can lower this value and requires its own constraint; an all-input criterion must not be declared necessary for one prepared state.

For a finite history-dependent tree with retry labels y and maps N_(h,y), use exact backward effects

 A_h=E_(W,h)+sum_y N_(h,y)*(A_hy),
 B_h=E_(O,h)+sum_y N_(h,y)*(B_hy),

with zero at cap leaves. This computes a supplied adaptive controller including memory and history-dependent instruments. It does not optimize an unspecified controller, or justify an entrywise maximum over incomparable positive operators. A known one-attempt nonnegative expected-cost effect X_h gives the identical recurrence for costs. Homogeneous C_m=sum_(k<m)(N*)^k X is exact; actual pathwise caps remain a separate premise.

## 2. Infinite horizon and its exact domain

The survival effects S_m=(N*)^m I decrease in positive order to S_infinity. Finite-dimensional continuity gives N*S_infinity=S_infinity. Completion for initial rho holds exactly when tr(rho S_infinity)=0. Completion for all initial states is equivalent to S_infinity=0.

In finite dimension, the latter is equivalent to existence of a block length n and p_n>0 with (N*)^n I<=(1-p_n)I. Indeed S_m->0 in matrix norm implies such an n; conversely the block contraction gives geometric survival. It follows that N* has spectral radius<1 (its positive-map operator norm on Hermitian inputs is bounded by ||(N*)^n I||). Thus

 A_infinity=(I-N*)^(-1)E_W,
 B_infinity=I,
 C_infinity=(I-N*)^(-1)X.

All-input eventual error is lambda_max(A_infinity), and expected cost is tr(rho C_infinity). A one-step completion floor p gives C_infinity<=K/p I when X<=KI. A missing one-step floor does not prevent a block floor; e.g. a two-state chain may first move a state and then terminate deterministically. The block floor also gives P(T>kn)<=(1-p_n)^k and E T<=n/p_n for every initial state. Conversely a nonzero dark no-output sector invalidates the full resolvent: S_infinity can be nonzero and I-N* singular. A_m still converges monotonically, but one must use B_infinity=I-S_infinity and the support ratio rather than pretending output is certain.

## 3. Identical POVMs, different retry risks

On H=C^2 take the same effects in both implementations:

 E_W=diag(0,1/2), E_C=diag(1/2,0), E_N=I/2.

Use identical wrong/correct terminal maps, and either

 N_good(rho)=tr(rho)|0><0|/2,
 N_bad(rho)=tr(rho)|1><1|/2.

These are complete measure-and-prepare instruments. For any positive effect
E and density matrix sigma, rho -> tr(E rho)*sigma is CP: diagonalizing
E=sum_i e_i|i><i| and sigma=sum_j s_j|j><j| gives Kraus operators
sqrt(e_i*s_j)|j><i|. Its Choi matrix is E^T tensor sigma, positive. Thus the
terminal maps and both replacement retry maps are genuinely CP with the
stated effects, rather than just formal outcome probabilities. Starting at |0>, the first attempt has error0 and output1/2 for both. At cap2, N_good gives error0 while N_bad gives wrong1/4, output3/4 and conditional error1/3. At infinite cap the respective conditional errors are0 and1/2. Every first-attempt acceptance/no-output effect agrees exactly. Complete state updates, reset and custody are therefore essential; calibrating all initial outcome probabilities alone cannot certify adaptive reuse. This is a concrete performance statement for these instruments, not a claim about an unconstructed Q/T retry map.

A coherent control is N(rho)=H rho H/2 with Hadamard H and the same E_W,E_C. Then

 A_2=[[1/8,-1/8],[-1/8,5/8]], B_2=3I/4,
 A_infinity=[[1/6,-1/6],[-1/6,5/6]].

The retry Kraus operator is H/sqrt(2); terminal replacement maps retain the same effects, so completeness holds. The cap2 and eventual all-input risks both equal (3+sqrt(5))/6. Diagonal population propagation alone misses the off-diagonal response.

## 4. Sharp uniform complete-instrument calibration consumer

Freeze a finite cap m, and an ideal possibly history-dependent complete protocol. On every reached history and every allowed memory/reference input, assume ideal no-output probability<=1-p, p>0. Suppose its ideal capped conditional error is<=eta for every initial state, eta in[0,1]. Each actual complete attempt differs from its corresponding ideal attempt by at most delta in half-diamond norm, uniformly on the same full input domain and histories; take 0<=delta<p. Fresh calibration is not inferred from a marginal distribution. Set

 b=1-(1-p)^m, epsilon=delta*b/p.

Replace attempts one by one, with the ideal prefix and actual suffix. The hybrid difference at attempt i is at most delta times the ideal reached probability, bounded by (1-p)^(i-1). Later adaptive maps are contractive. Hence the full terminal record/output channels differ in half-diamond norm by at most epsilon; after the fixed correctness audit, terminal-law TV is at most epsilon. This bound retains stopped reach weights instead of using m*delta. It applies to arbitrary initial entanglement because complete-instrument calibration includes it. The instruments must act on compatible carriers; hidden memory outside the calibrated carrier defeats the premise.

The sharp terminal-law perturbation lemma is:

 ideal output>=b, ideal wrong<=eta*ideal output, TV(actual,ideal)<=epsilon
 implies actual conditional error<=min(1,eta+epsilon/b),

whenever actual output exists. For the nontrivial case r=eta+epsilon/b<1, let h give rewards 1-r on wrong, -r on correct and0 on no output. Its range has width1, so TV changes its mean by at most epsilon. Ideal mean <=(eta-r)*b=-epsilon, implying actual wrong-r*output<=0. Also epsilon<(1-eta)b<=b, so actual output is positive. When r>=1 the bound is only the trivial bound; the stated delta<p still supplies an actual one-step floor p-delta and hence positive completion.

Therefore the whole calibrated retry protocol has error<=eta_delta=min(1,eta+delta/p), UNIFORMLY in finite cap m. This is stronger than independently worsening numerator and denominator to (eta*p+delta)/(p-delta). It is sharp in this complete-instrument class: ideal constant effects (eta*p,(1-eta)*p,1-p)I, actual ((eta*p+delta),((1-eta)*p-delta),1-p)I attain equality whenever delta<=(1-eta)p; if delta is larger, move all correct mass to wrong using distance(1-eta)p<=delta. Replacement outputs implement these scalar laws on any supplied positive Hilbert carrier, not necessarily the original constrained Q/T family.

A single common calibration event G with P(G^c)<=zeta<1 can be included. The preceding assumptions must hold under the conditional-on-G model itself, with the complete CP instruments valid there. A future postselected calibration event need not preserve that description. Allow arbitrary bad-event outcomes. Then the sharp abstract class bound is

 F=[zeta+(1-zeta)*b*eta_delta]/[zeta+(1-zeta)*b].

For eta_delta<1, use h with r=F: good ideal mean<=(eta-F)b and the perturbation costs epsilon, while a bad event contributes at most1-F. Mixing gives zero exactly. F>=eta ensures the lower output floor is used in the correct direction. A smaller bad mass cannot increase the bound because its maximum reward1-F dominates the good signed expectation; alternatively pad the bad event with arbitrary already-valid cases. Scalar good extremizers above plus immediately wrong bad outcomes attain F. This is sharpness in a supplied full-instrument uncertainty class, not original Q/T attainability or joint cost sharpness.

For m->infinity, the actual floor p-delta gives almost-sure completion, b->1, and F->zeta+(1-zeta)*eta_delta. Uniform error control alone is not proof of reset or fresh resource supply.

## 5. Reset-tolerance and complete costs

A sufficient interface for importing scalar per-attempt calibration is an ideal reset R(rho)=tr(rho)*sigma on the ENTIRE memory input that is meant to be renewed, followed by an ideal accepted-output verifier. Suppose its one-attempt wrong mass is alpha=eta*p and output mass p on sigma. If the actual reset is half-diamond epsilon_R close to R and the actual complete verifier is epsilon_V close to ideal, composition gives delta<=epsilon_R+epsilon_V (cap at1). With delta<p the preceding result applies. Correlations with untouched reference systems are retained; renewal must not silently discard an external system that is used again. This is an explicit sufficient demand on a proposed implementation, not a measured estimate or preparation of the required sigma from GU.

For p=1/2, eta=1/20, delta=1/100, m=3, zeta=1/1000:

 b=7/8, eta_delta=7/100,
 F=49751/700100 (approximately0.0710627).

The zero-calibration-error good value1/20 becomes7/100; the entire shared-failure event is charged once. Taking epsilon_R=epsilon_V=1/200 is one possible error-budget split, not an implemented reset. A complete-attempt cap K and setup S give pathwise cost<=S+mK. Under G actual mean count<=sum_(k<m)(1-p+delta)^k, so unconditional expected cost is bounded by

 S+(1-zeta)*K*[1-(1-p+delta)^m]/(p-delta)+zeta*m*K,

provided K also holds on bad histories. Cost extremizers may shift correct mass to no output and need not attain the sharp risk bound. Resource acquisition, reset, calibration, abort and retained-memory management must all be in K or separately and correctly priced.

## 6. Verification and remaining question

Exact Fraction controls check recurrence, coherent/noncommuting effects,
singular output support, dark and block-completion sectors, finite adaptive
cost recurrence, terminal-law perturbations, scalar calibration extrema,
shared-event arithmetic and reset budgets. These controls support the written
universal proofs; they do not themselves quantify over all channels. Contrary
controls distinguish equal POVMs from equal instruments, conditional error
from wrong mass, unweighted calibration, diagonalized memory, singular output
and omitted reset/bad-history costs.

If a proposed apparatus supplies complete retry/reset maps, compute its A_m,
B_m and its true reachable input class before importing scalar designs. If
only effects are known, the equal-POVM pair proves nonidentifiability in the
stated class; the successor is a state-update calibration or explicitly priced
renewal mechanism. A complete original Q/T attempt still needs resource
preparation/custody, wrong-event meaning, completion and reset maps. The
original local tests may destroy test states; they do not turn a failed
specimen into a fresh use resource. Abstract scalar sharpness proves no
attainability in the original constrained Q/T family.

The source-to-physics challenger remains a positive physical quotient and
common matter/light source/readout on the source-owned operator. This
operational result does not settle that route. Internal specialist review is
not external-expert, proof-assistant, novelty or measured-device certification.

Standard CP-map/instrument and complete channel distinguishability definitions
are treated in [Watrous, The Theory of Quantum Information, chapters 2--3](https://cs.uwaterloo.ca/~watrous/TQI/).
The finite sums and perturbation argument above are proved here within their
stated scope; no novelty claim is made.

[Probe](../../tests/channel-swings/k2481_complete_retry_instrument_probe.py)
and [report](../../lab/process/k2481-complete-retry-instrument.json).
