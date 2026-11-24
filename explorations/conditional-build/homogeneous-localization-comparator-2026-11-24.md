---
title: 'Homogeneous localization comparator: no L2 point spectrum, native transfer open'
status: exploration
doc_type: result
created: '2026-11-24'
program_target: X-P1-P2-P3
tier: T2
expected_delta: Settle homogeneous Riemannian Dirac/RS/Pi localization with exact domain and transfer
  hypotheses
actual_delta: RC1 formal-degree/count and W175 native gap/Fredholm imports are unsupported for the stated
  metric pair. A separate theorem excludes all L2 eigenmodes for finite-rank positive homogeneous selfadjoint
  first-order elliptic operators on SL4R/SO4, and for first-order translation-invariant elliptic operators
  on its full-line product. Intrinsic Dirac and RS are covered; positive ambient Pi14 is conditional on
  the stated Hilbert realization. No native Krein transfer, numerical spectral gap or P3 emptiness follows.
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Homogeneous localization: a comparator theorem, with the native transfer exposed

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

program_target: X-P1-P2-P3
tier: T2
expected_delta: Settle the positive homogeneous localization comparator without importing W175's threshold
actual_delta: Empty L2 point spectrum proved in the stated Riemannian class; native transfer and physical mode necessity remain open

Base: `d89b56eac67c1df293ec2782171b3cbb8c14bbbe`. Directed steps 0 and 1R only. This is an internally reviewed
T2 theorem at comparator scope, not a Tier1 matrix decision or external review.
The [reconciliation](localization-source-reconciliation-2026-11-24.md) was
recorded before this theorem investigation. No numerical spectral gap is assumed.

```gu-typed-objects
result: Homogeneous positive Riemannian no-L2-eigenmode theorem and its exact transfer boundary
carrier: finite-rank homogeneous Hermitian bundles over M9=SL4R/SO4 and M9 times full R; intrinsic RS9/RS10 and conditional positive ambient Pi14 distinguished LAYER=ambient BRIDGE=native-Krein-and-observation-transfer-unproved CHIRALITY=S-FULL-DIRAC
pairing: positive homogeneous Hilbert L2 and invariant product measure; native K77/K95 not identified ON=declared_carrier
real_structure: finite spin cover allowed; no physical quaternionic family count inferred
grading: no chiral index or observed family count asserted; ungraded eigenmode statement
action_owner: N/A -- structural operator class, no specific action constructed
target: prerequisite for the localization route to P3 MAP-TYPE=not-a-map
```

## 1. The theorem and the operator class

Let `M=SL(4,R)/SO(4)` have its complete invariant **positive** Riemannian
metric. Replace the group and compact isotropy by compatible finite spin
covers where necessary. Let `E=G×K V` for a finite-dimensional unitary
K-module. If A is a homogeneous selfadjoint first-order elliptic differential operator
on the ordinary Hilbert space L2(M,E), then

```
Spec_point(A) = empty, hence ker_L2(A) = 0.
```

The primary input is Goette–Semmelmann Theorem1.3: the eigenspaces of such
an operator are sums of discrete-series representations. Their §1 allows
the spin covers and explains the equal-Cartan-rank condition. Here
rank(sl4C)=3 and rank(so4C)=2, so the needed representations are absent.
This uses their general homogeneous elliptic theorem, not merely their
untwisted Dirac classification. [Primary theorem, §1, Theorem1.3 and
Remark1.4](https://arxiv.org/pdf/math/9903177).

These are complex Cartan ranks. Do not substitute the real split rank of
SO(4), or the separate rank3-versus1 relative symmetric-space test.
Finite spin covers change neither Lie algebra rank.

The conclusion excludes **every L2 eigenvalue**, and therefore the discrete
spectrum in the isolated finite-multiplicity sense. It does not locate the
continuous spectrum. In particular, empty point spectrum does not prove a
gap about zero, Fredholmness, or existence of a bounded Krein C operator.
Group discrete series, operator point spectrum and operator discrete spectrum
are three different notions; the proof states their exact implication here.

## 2. Why the intrinsic RS compression is covered

Use a positive n-dimensional Clifford space with c(v)^2=-|v|^2. For a
vector-spinor u define

```
Gamma(u)=sum_a c(e_a)u_a,
i(s)_a=-(1/n)c(e_a)s,
P=1-i Gamma,        R=ker Gamma,
Q=P D_T|R.
```

This is the intrinsic gamma-traceless RS operator, with orthogonal P.
Homma–Semmelmann §2 gives this definition and formal selfadjointness; its
compact-manifold kernel classifications are not being transferred to this
noncompact space. [Definition and adjoint conventions](https://arxiv.org/pdf/1804.10602).

Here is the required separate symbol proof. At |xi|=1 write C=c(xi) and
q=P C|R. If q u=0, then C u_a=c(e_a)theta for some spinor theta. Thus
u_a=-C c(e_a)theta. The Clifford relation gives

```
sum_a c(e_a) C c(e_a)=(n-2)C,
0=Gamma(u)=-(n-2)C theta.
```

For n>2, C is invertible, so theta=u=0. The square symbol on a finite
bundle is therefore invertible. This proves ellipticity of Q; it is not an
inference from the kernel of the uncompressed twisted Dirac operator.

A sharper check sets j_xi(s)=P(xi tensor s) and
T_xi={u: Gamma u=0, u(xi)=0}. Orthogonally R=j_xi(S) plus T_xi, and

```
q j_xi(s)=((n-2)/n) j_xi(C s),       q|T_xi=C,
q^2 u=-u+(4/n)j_xi(u(xi)).
```

Thus the Hermitian symbol i q has singular values |xi| and
((n-2)/n)|xi|. At n=2 the j subspace is a genuine symbol kernel, a useful
failure control. The exact Clifford-word probe checks these identities on
spanning sections P(e_b tensor s), with an arbitrary right-hand spinor s.

| Positive carrier | Spin rank | RS rank | Reduced symbol factor |
|---|---:|---:|---:|
| Intrinsic shape, n=9 | 16 | 128 | 7/9 |
| Intrinsic product, n=10 | 32 | 288 | 4/5 |
| Separately supplied positive ambient n=14 | 128 | 1664 | 6/7 |

Q is formally symmetric, and ||[Q,chi]|| <= |d chi|. On the complete
homogeneous manifold, cutoffs chi_R with gradients tending uniformly to
zero show essential selfadjointness on compactly supported smooth sections:
apply the deficiency equation Q* u=±i u against chi_R^2 u and take imaginary
parts. Local elliptic regularity justifies the calculation; the commutator
bound forces u=0 as R tends to infinity. This fixes the unique closure and
rules out a hidden choice of boundary realization. The same argument covers
homogeneous first-order symmetric elliptic operators with bounded symbol
speed; finite rank and homogeneity provide that bound.

Consequently intrinsic Q9 satisfies §1 and has no L2 eigenmodes. Homogeneous
Hermitian twists with equivariant unitary connection and bounded homogeneous
selfadjoint zero-order terms are covered as well.

## 3. Full scale line: a direct-integral proof

Declare the comparison space F+=M×R with **positive unwarped product metric**,
invariant volume times Lebesgue measure, and a finite homogeneous Hermitian
bundle. Let L be first-order, symmetric, elliptic and G×R invariant. Use
its full-space closure from C_c^infinity, not a weighted, half-line, APS,
compact-quotient or imposed boundary realization.

Partial Fourier transformation in r gives L(k)=A+kV. A is homogeneous and
symmetric on M; its shape symbol is the full symbol at (xi,0), hence
elliptic. V is a bounded homogeneous Hermitian endomorphism. The cutoff
argument above gives selfadjoint A and L. Each fixed k gives the selfadjoint
operator A+kV on Dom(A), by bounded perturbation. Each satisfies §1, so
ker(A+kV-lambda)=0 for every real k and lambda. The Fourier transform of
an L2 eigenvector of L lies in those kernels almost everywhere and therefore
vanishes. Hence Spec_point(L) is empty.

This argument covers intrinsic Q10 as well as the product Dirac and its
finite homogeneous Hermitian twists. It does not apply the semisimple-group
theorem directly to the reductive group SL4R×R and does not assume a Dirac
square formula for RS. A constant scalar mass shifts the spectrum without
creating eigenvalues; more general homogeneous symmetric zero-order terms
also retain the theorem's hypotheses.

The flat line does not necessarily remove a continuous spectral gap. A
constant-in-r mode is not L2 on the full line. Neither observation computes
an actual native gap or a physical mass.

## 4. Pi14 and the native transfer: precise limits

W175's ambient Pi14 is not intrinsic P9 or P10. A **separately supplied
positive ambient comparison** is covered if it has a rank-14 Euclidean vector bundle with its Clifford module, orthogonal homogeneous gamma-trace projector, symmetric
compression on im Pi, elliptic shape symbol and the complete homogeneous
domain. The n14 symbol computation verifies that local ellipticity for
the stated positive Clifford compression. It supplies none of the missing
native Hilbert identification by itself.

Pi D Pi on the entire original bundle has an artificial ker Pi zero
sector. Its domain and codomain must be im Pi. Also an arbitrary orthogonal
projector need not preserve ellipticity: compressing the invertible Pauli
matrix sigma_x to its first coordinate gives zero. Merely knowing D is
elliptic cannot replace the gamma-trace symbol proof.

The actual metric fibre has noncompact isotropy SO0(3,1), a nonunitary finite
spin coefficient and indefinite normal form. Its trace-reversed DeWitt form
obeys K_g(g,g)=4-8=-4 on the scale direction. Thus the positive R product
here is a deliberate comparison, not W175's asserted spacelike native end.
K95 has normal signature(6,4); K77 remains a separate conditional branch.
Even a Euclidean base gives trace-reversed signature(9,1), not a positive
fibre. [Trace compatibility](source-chimeric-trace-compatibility-2026-11-13.md).

The required [GEOMETER routes](../../GEOMETER-VS-PHYSICS-OBJECTS.md) are:

- **T11:** name the actual operator, common closed domain and end conditions.
  A local compressed symbol is not a global Fredholm or causal theorem.
- **T13:** compact-K unitarization is a comparison; it does not turn the
  noncompact-H induced coefficient or its operator into the same Hilbert problem.
- **T15:** a Krein adjoint is not the positive Hilbert adjoint used above.
  Neither a native ghost exclusion nor an inconsistency follows merely from
  indefinite signature. K77 and K95 cannot be interchanged.

Source normal-spinor labels and contraction/readout do not establish that
physical fermions must be a conventional normal-L2 KK tower. SC-GEO-52
disavows a conventional KK interpretation; it does not rule out every
separately justified normal-L2 realization. SC-CHI-51/52 name VEV and curvature
mass structure, not an asymptotic Callias map. The [source register](../../lab/sources/source-claim-register.yaml)
and [action class](../../lab/process/action-class.json) retain nonhomogeneous
connection/end possibilities without selecting arbitrary potentials or indices.

The [observation graph result](observation-graph-domain-2026-11-24.md)
constrains literal section restriction on its tested L2/graph cores. It does
not exclude stronger or constrained domains, prove that every section
readout is non-propagating, or supply a dichotomy for all class C.
Index zero also permits paired zero modes. No protected index alone is not
P3 emptiness. No native VEV mechanism has been adjudicated adversely here;
source polarity, adherence and hedge-watch verdicts remain unchanged.

## 5. Result, reproducibility and continuation

**Step0 done:** the rank-one formal degree/count was unsupported, and W175
reused its invalid spectral premise. The owner artifacts now carry active
metadata corrections with historical prose retained.

**Step1R done at the stated scope:** the positive homogeneous Dirac/RS
comparison has no L2 point spectrum, including the full-line extension.
Positive ambient Pi14 is conditional on the explicit realization in §4.
There is no W175 threshold to inherit, and the comparison does not kill GU
or decide a native matrix cell. Packet failure is not triggered.

**Step1K ready:** test the exact native pairing/operator/domain transfer and
normal-L2 necessity for source observation. Do not construct the missing
source operator. Later asymptotic classification waits for this premise.

Reproduce finite algebra with
`python tests/program-focus/homogeneous_localization_comparator_probe.py`.
The [machine receipt](../../lab/process/homogeneous-localization-comparator.json)
records the exact controls; the noncompact spectral theorem is a cited
analytic proof, not a numerical simulation or Lean result. See the
[independent reviews](../../lab/process/hostile-reviews/2026-11-24-localization-comparator-review.md).
