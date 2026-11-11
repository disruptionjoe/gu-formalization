---
title: Spectral crossings require a symmetry-compatible family repair
status: exploration
doc_type: structural-result
created: '2026-11-11'
program_target: P3xsymmetry
tier: T2
expected_delta: Classify global spectral sections and admissible repairs for a specified
  elliptic symmetry category.
actual_delta: 'Constrained: the clutched Fourier family has a representation-valued
  obstruction to a global spectral section. A G-equivariant finite-rank smoothing repair exists
  exactly when the two symmetry modules match; its Green-Lagrangian repair can still
  break a separately fixed grading. No GU end realization or physical count is supplied.'
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Spectral crossings require a symmetry-compatible family repair

Constrained: the clutched Fourier family has a representation-valued obstruction to a global spectral section. A G-equivariant finite-rank smoothing repair exists exactly when the two symmetry modules match; its Green-Lagrangian repair can still break a separately fixed grading. No GU end realization or physical count is supplied.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: P3xsymmetry
tier: T2
expected_delta: Classify global spectral sections and admissible repairs for a specified elliptic symmetry category.
actual_delta: Constrained: the clutched Fourier family has a representation-valued obstruction to a global spectral section. A G-equivariant finite-rank smoothing repair exists exactly when the two symmetry modules match; its Green-Lagrangian repair can still break a separately fixed grading. No GU end realization or physical count is supplied.

```gu-typed-objects
result: equivariant spectral-section obstruction and repair
carrier: L2 of the circle with fixed H1 domain, doubled and tensored with finite unitary symmetry modules LAYER=toy CHIRALITY=N/A
pairing: positive L2 Hermitian form; normal c defines skew Green form ON=declared_carrier
real_structure: complex conjugation reflects parameter and sign; not a fixed-parameter antiunitary symmetry
grading: Gamma=sigma3 on doubled channels, independent of native physical chirality
action_owner: repository-construction -- structural elliptic family and boundary algebra, no action constructed
target: norm-continuous clutched spectral section with specified symmetry MAP-TYPE=projection
```
## 1. Native demand, prior work and exact scope

The [July boundary proposal](../blockbuster-p4-generation-doors-2026-07-19.md)
already demanded compatible spectral sections, including ghost-sector data.
The recent [Green-domain classification](p3-green-form-symmetry-domain-2026-11-11.md)
and [interval family result](p3-auxiliary-domain-family-2026-11-11.md)
separated pointwise admissibility from global families. They did not compute
the varying-spectrum obstruction and smoothing repair below. The present
consumer is the same P3 symmetry/global-domain requirement, now tested on an
actual compact-resolvent elliptic family rather than a finite endpoint model.

This is a structurally defined analytic category, not a chosen GU boundary
connection or action. Class C's noncompact Y14 realization remains to be
supplied separately. SC-GEN-02/03/54 and SC-CHI-01/51 retain ASSERTS at their
source2+1/nonchiral-total scopes. Ordinary spectral flow is not their integer
physical-family observable. RA-F1 and AC-F1 remain NEEDS; neither ledger moves.

## 2. One clutched family has no spectral section

Let H=L2(S1), circle coordinate theta of period2pi, with positive Hermitian
pairing and fixed domain H1(S1). For t in[0,1] define
B_t=-i d/dtheta+t+1/2. The Fourier vectors e_n=e^{in theta} have eigenvalues
lambda_n(t)=n+t+1/2. Endpoints are identified by U=e^{-i theta}:
B_1=U B_0 U^{-1}. Multiplication by U preserves H1. This gives a smooth
family on a Hilbert bundle over the parameter circle, with fixed local
principal symbol and one upward zero crossing, at n=-1,t=1/2. The graph
norms are uniformly equivalent; the resolvents are compact.

A spectral section here means norm-continuous orthogonal projections P_t
with P_1=U P_0 U^{-1}, such that for one uniform R, P_t is identity on
eigenvectors with eigenvalue>R and zero for eigenvalue<-R. The uniform
cutoff is part of the definition; no finite-dimensional periodic truncation
replaces this Hilbert-space problem.

Let Q project onto modes n>=0. Then P_t-Q is supported in one common finite
Fourier window: high modes agree, and orthogonality forbids mixing those fixed
high modes with the middle. Its trace is continuous and integer-valued, hence
constant. But U^{-1} Q U=Q-|e_0><e_0|, so endpoint clutching gives
Tr(P_1-Q)=Tr(P_0-Q)+1, a contradiction. This proves the obstruction without
sampling eigenvalues or invoking a general theorem.

The result is an explicit application of established spectral-section/index
ideas, not a novelty claim. Primary references include
[Ivanov, two proofs of Melrose–Piazza](https://arxiv.org/abs/2112.04673) and
[Prokhorova, Spectral Sections](https://arxiv.org/abs/2008.04672).
The self-contained argument above settles precisely this category.

## 3. Executed repair: smoothing, exact high modes and Green form

On H tensor C2 take A_t=B_t sigma3. Choose a real smooth compactly supported
chi on R that is strictly positive in a neighborhood of zero, and m>0. Define
K_t=m chi(B_t)sigma1 and D_t=A_t+K_t. This is a specified boundary-operator
repair, not a Lagrangian or stabilized RS action. K_t is finite-rank smoothing;
on the compact t interval its Fourier support is uniformly bounded. It
clutches by U tensor I. Direct computation gives

D_t²=(B_t²+m² chi(B_t)²)I.

The continuous function x²+m²chi(x)² has a positive global lower bound:
it has no zero, and tends to infinity as |x| grows. Thus D_t is uniformly
invertible on H1 and
P_t=(I+D_t(D_t²)^(-1/2))/2
is a smooth norm-continuous clutched orthogonal projection. Outside the
support of chi, it agrees exactly with the positive spectral projection of
A_t. This is an actual spectral section, not just a compact perturbation of
one. Constant mass would be gapped but would not have exact high-mode
agreement; localization is essential for this definition.

The normal c=i sigma2 satisfies c*=-c,c²=-I and anticommutes with A_t and
K_t. Therefore cP_t=(I-P_t)c. For L_t=ker P_t one has cL_t=L_t-perp, so
L_t is maximal isotropic for the Green form <c u,v>. This supplies genuine
Green-Lagrangian boundary subspaces in the specified product Dirac algebra.
The Fourier description preserves every Sobolev space and gives the ordinary
smooth spectral boundary projection. No GU bulk, complete boundary-value
problem on Y14, noncompact Fredholm estimate or physical quotient follows.

## 4. Complete compact-symmetry refinement and stabilization

Let W_+,W_- be finite-dimensional unitary representations of a compact group
G, acting trivially on t. Set
A_t=(B_t tensor I_W+) direct_sum (-B_t tensor I_W-),
with clutch U on both summands. A G-equivariant spectral section exists
**if and only if W_+ and W_- are isomorphic as G modules**.

Necessity. Decompose the finite representations into irreducibles rho with
multiplicities m_+(rho),m_-(rho). A commuting projection preserves each
isotypic summand and acts on its multiplicity space. The finite-window trace
argument from section2, with Q on positive channels and I-Q on negative
channels, yields endpoint defect m_+(rho)-m_-(rho) for each rho. Continuity
forces every defect to vanish. Taking only the total trace would lose this
information; multiplying by dim(rho) does not remove a nonzero defect.

Sufficiency. Choose a unitary intertwiner T:W_+→W_-. Use the localized mass
with off-diagonal blocks T* and T. Its square is m²chi(B_t)² and it
anticommutes with A_t. The section3 positive projection is equivariant,
clutched and exact on high modes. This proves both directions for all finite
multiplicities in the stated category, not only for the two-channel example.

The obstruction is the virtual representation [W_+]-[W_-]. Adding identical
modules Z to both sides leaves it unchanged. Adding unmatched inverse
channels can remove it: W_+ plus W_- becomes equivalent to W_- plus W_+.
That is a change of supplied field content, not a repair allowed automatically
inside class C. Additional uniformly gapped equivariant families contribute
zero defect and cannot change the criterion.

For G=Z/2, choose W_+ trivial and W_- sign, each dimension1. Total spectral
flow vanishes, but the two irreducible defects are +1,-1. There is no
G-equivariant section. This is an exact infinite-family countercontrol to
ungraded cancellation; it does not assert these are GU symmetry modules.

## 5. Which symmetry does the repair preserve?

For the two-channel family put Gamma=sigma3. Then [Gamma,A_t]=0, but
[Gamma,K_t] is nonzero near a crossing. At lambda=0 the repaired projection
is (I+sigma1)/2 and does not commute with Gamma. A Gamma-invariant section
would split into sections for B_t and -B_t separately, which section2 rules
out. Hence the repair preserves Green admissibility but necessarily breaks
this fixed grading.

There is no contradictory demand that Gamma commute with the normal c:
Gamma c=-c Gamma. Thus the formal product Dirac expression
c(partial_r+A_t) anticommutes with Gamma. The question is domain invariance
under that grading. Conversely, if one demands an ordinary compact symmetry
G commute with **both A and c**, then the displayed c already intertwines
W_+ and W_-, so their module equivalence must be checked at the outset. The
nonisomorphic-module example is a symmetry of the adapted operator, not an
example of a commuting symmetry of the full normal Dirac algebra.

Complex conjugation C obeys C B_t C=-B_{-t-1} with this half-offset.
It reverses the parameter modulo the gauge clutch, rather than giving a
fixed-parameter real structure at generic t. The zero-space parity tests of
the earlier note cannot be applied by silently freezing this base action.

## 6. Verification and consequences

[Exact controls](../../tests/program-focus/p3_equivariant_spectral_sections_probe.py)
and [saved report](../../lab/process/p3-equivariant-spectral-sections.json)
check the clutch sign, one-mode defect, smoothing-block algebra, actual
nontrivial multiplicity intertwiner, Green relation and rejected grading.
A cyclic finite truncation has an artificial opposite wraparound crossing and
zero total trace defect; the probe explicitly rejects it as certification.
Universal analytic proofs are in this note; finite tests are supporting
controls, not Lean, full-C or physical certification. Independent specialist and hostile review completed with substantive findings
resolved; equivariance and matrix/antilinear notation were checked explicitly.

For structural subfamilies requiring such a global equivariant spectral
section, P3xsymmetry and P3xglobal_index require the same symmetry-resolved family
obstruction and admissible repair, not merely zero scalar spectral flow.
X-P2-P3 cannot infer a global domain from its fixed local symbol. The complete
Fourier-category obstruction and its actual smoothing/Green repair are settled;
transfer needs the genuine target family, symmetry action and domain. Source,
physics ledger0.263, class C and canon remain unchanged.
