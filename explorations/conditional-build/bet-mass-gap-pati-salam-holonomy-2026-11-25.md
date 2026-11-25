---
title: Pati-Salam flat holonomy retains neutral quadratic modes
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: BET-MASS-GAP
tier: T2
expected_delta: Apply the full flat-torus Hessian criterion to the compact source-related PS representation and global quotients.
actual_delta: All declared flat PS bundles retain neutral modes; nonzero correlated central flux has common adjoint fixed dimension one or three, versus at least five for zero flux.
class_covered: All flat compact-positive MG1 connections on T3 for SU4 x SU2 x SU2 and its diagonal Z2 quotient, with honest 16 representation and ordinary spin background.
premises:
  - lab/sources/source-claim-register.yaml#SC-GRP-03
  - explorations/conditional-build/source-symmetry-matching-scope-2026-11-24.md
  - explorations/conditional-build/bet-mass-gap-stability-topology-2026-11-24.md
source_bridge:
  status: conditional
  reason: The source supplies related local group and representation data, not this compact-positive action, flat vacuum, torus domain or physical spectrum.
kill_condition: No bet-wide kill; the result determines the quadratic spectrum at zero for this flat compact subgroup/bundle category only.
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# The SO(3) gap does not extend to the whole compact Pati-Salam carrier

**Result.** In the existing speculative MG1 curvature-square comparator, every
flat connection on a three-torus for

`G = (SU(4) x SU(2)L x SU(2)R)/<(−I4,−I2,−I2)>`

has a nonzero common adjoint fixed space `h`. For nonzero central flux,
`dim_R h` is **1 or 3**. For zero central flux it is **at least 5**, sharply.
The reduced physical quadratic Hessian therefore has zero eigenvalue, with
linearized Coulomb-slice kernel dimension `3 dim_R h`. The simply connected covering product is the
zero-flux case. This tests the complete21-dimensional compact adjoint, not
only a gapped weak SU(2)/Z2 subblock.

This is a conditional classical spectrum result, not a quantum mass-gap
verdict, bet-wide kill, or a statement that a photon should be massive. A
massless unbroken gauge factor can be physically desirable. The source's
native indefinite operator, nonflat condensate and observed sector are not
identified with this comparator. No new guessed action is introduced.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```yaml
program_target: BET-MASS-GAP
tier: T2
expected_delta: Complete compactPS flat-holonomy gap discriminator.
actual_delta: All allowed fluxes retain physical quadratic zero modes; no bet-wide or native verdict.
```

## 1. Source and object custody

SC-GRP-03 ASSERTS the simultaneous maximal-compact/complex reduction role;
SC-PRE-52 ASSERTS Pati-Salam-level recombination. The recent
[source-symmetry audit](source-symmetry-matching-scope-2026-11-24.md) already
identifies the compact embedded quotient and the all-left-handed representation
`(4,2,1) + (bar4,1,2)`. Neither asserts unbroken compact PS dynamics on T3.
The total source parent remains U(64,64), and K77 assertion versus K95 geometric
derivation is unchanged. The 16 here is a representation control, not a
physical family count, a substitute for 2+1, or the imposter/RS identification.

Objects: real adjoint one-forms; positive invariant compact pairing; real
compact Lie algebra; ordinary Gauss/Coulomb grading only; repository MG1
variational owner; complete physical quadratic Hessian on a fixed torus.
Observation is not rebuilt or replaced by projection. A later native use owes
the actual contraction, group/bundle, state and action bridge.

## 2. Which central quotient admits the complete16?

A centre element has form `(i^a I4, (−1)^b I2, (−1)^c I2)`.
Its actions on the two summands are `i^a(−1)^b` and `i^(−a)(−1)^c`.
Both equal1 exactly for `(a,b,c)=(0,0,0)` or `(2,1,1)`.
Consequently any central quotient of this product on which the16 is an
**honest representation** is either the covering product or the diagonalZ2
quotient. This does not classify spin-charge-twisted structures, additional
compensating flavour groups, or other carriers. Those are explicit scope exits,
not permissions to import a PSU4 bundle into the stated category.

## 3. Exhaustive central-flux calculation

A flat quotient bundle is specified by a commuting holonomy triple inG.
Choose lifts `(U_i,V_i,W_i)` to the covering product. Their pair commutators
must all have the correlated form

`[U_i,U_j]=(-I4)^m_ij`, `[V_i,V_j]=[W_i,W_j]=(-I2)^m_ij`,

where `m` is an alternating3x3 matrix overF2. Changing lifts does not change
m. All eight fluxes are treated.

**Zero flux.** Each factor consists of commuting unitary matrices and hence
admits simultaneous diagonalization. The common centralizer contains a
maximal torus of ranks3,1,1, giving `dim h >=5`. A generic diagonal triple
attains5. This argument is specific to these unitary factors: it does not
assert that commuting triples in every simply connected compact group are toral.

**Nonzero flux.** Every nonzero alternating form onF2^3 has rank2. An integral
change of torus generators can put it into `m12=1,m13=m23=0` (lift an invertible
F2 basis change through GL3(Z)). The relabeling need not preserve the rectangular
metric, but it preserves the common fixed space and the zero-mode conclusion.
Thus U1,U2 anticommute and U3 commutes with both; likewise forV,W.

The commuting normal operators U1²,U2²,U3 are central in the algebra generated
by the triple. On each simultaneous eigenspace, rescale U1,U2 by their scalar
square roots. Two involutions anticommuting generate M2(C). All irreducible
unitary blocks consequently have complex dimension2. The third holonomy is
scalar on an irreducible block. This proves completeness; it is not a census
of selected clock/shift examples.

ForSU2 there is exactly one such block. Its U2 centralizer is scalar, so its
su2 centralizer is zero. ForSU4 there are two possibilities:

| Projective joint representation on C4 | Full unitary commutant | Traceless compact commutant |
|---|---|---|
| two inequivalent2-dimensional blocks | U1 x U1 | u1, dimension1 |
| one2-dimensional block with multiplicity2 | U2 on multiplicity | su2, dimension3 |

The trace restriction is `2 tr(K)=0` in multiplicity space. In particular it
removes the common scalar, **not the whole multiplicity commutant**. Therefore
`h = h_SU4` has dimension1 or3. Correlated twisting clears the two weak factors
but leaves a neutral SU4 direction.

Sharp controls use Pauli X,Z and
`U1=(iX) tensor I2`, `U2=(iZ) tensor I2`.
For `U3=I4`, the fixed algebra is su2. For
`U3=I2 tensor iZ`, it is u1. Both are SU4 triples with the required flux.
Take `V1=W1=iX`, `V2=W2=iZ`, `V3=W3=I2`.
On both16 summands the central minus signs cancel, so the actual matter
holonomies commute. The explicit surviving generator is `I2 tensor iZ`.

This is elementary projective-representation analysis in the setting of
[Borel–Friedman–Morgan's almost-commuting tuples](https://arxiv.org/abs/math/9907007).
The proof above, rather than a silent general-compact-group theorem, supplies
the exact bound needed here.

## 4. Physical domain and zero modes

Reuse the [full flat-torus result](bet-mass-gap-stability-topology-2026-11-24.md#5-stable-positive-control-twisted-flat-so3-on-t3):
MG1 has F=0, and on twisted adjoint one-forms the physical Hessian is the
covariant Hodge Laplacian restricted to Coulomb fields, with twistedH2 domain.
It is nonnegative with compact resolvent. The real parallel adjoint sections
are precisely h. Twisted Fourier characters with nontrivial phase have no
zero mode; the trivial characters have three constant spatial one-forms.
Hence `ker K_physical = h tensor H1(T3;R)` and its real dimension is `3 dim h`.

For a parallel nonzeroH, `a=H dx^j` is smooth, periodic in the associated flat
bundle, Coulomb, and has zero Hessian. It is orthogonal to every infinitesimal
gauge derivative by integration by parts on compactT3. It cannot be removed
as a pure gauge vector. For one fixedH, the deformation `A+t H dx^j` stays
flat: these are actual Wilson-line deformations, not only formal zero modes.
The dimension3dim(h) is on the linearized Coulomb slice modulo infinitesimal
gauge derivatives. When h=su2, the residual constant stabilizer is continuous
and the full reduced moduli space is singular; arbitrary triples in h need not
commute, so some quadratic zero directions can be lifted quartically. No smooth
physical moduli-space dimension3dim(h) is asserted. The one-H commuting
deformation above still gives genuine zero directions after residual gauge
identifications. No boundary/end-condition choice or unproved normalizability is used.

## 5. What follows and what remains

The old twistedSO3 gap remains a valid positive control. Its extension to this
complete compactPS comparator has exact neutral modes in **every allowed central
flux sector**. More flat backgrounds in this same category cannot supply a
strictly positive full quadratic gap. A chosen charged subspace can still have
a positive gap; that is a different observable and must be named explicitly.

Native source condensation, nonflat backgrounds, noncompact real form,
spin-charge/global categories beyond honest16, and an interacting quantum
mechanism remain outside the result. Do not construct a source action to fill
these gaps. The next useful mass-gap input is an actually supplied nonconstant
stationary background and full physical Hessian, or a physically specified
sector whose gap is the desired observable—not another flatPS holonomy.

## Verification

The analytic proof exhausts all eight fluxes and all projective multiplicity
patterns. The exact probe checks centre descent, allF2 flux reductions, sharp
1/3/5-dimensional controls and honest16 commuting holonomies. It passes98
controls and rejects three planted mistakes. The initial control needed symbolic
expansion of a rational-complex determinant; this was a comparison-normalization
error, corrected before acceptance. These controls do not certify source physics.
Independent review and acceptance are recorded in the linked review artifact.
