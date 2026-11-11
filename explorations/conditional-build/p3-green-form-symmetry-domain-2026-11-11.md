---
title: "P3: Green-form admissibility and real symmetry of spectral domains"
status: exploration
doc_type: structural-result
created: "2026-11-11"
program_target: P3xsymmetry
tier: T2
expected_delta: "Refine the constrained cell by classifying simultaneous Green-Lagrangian and antiunitary invariance."
actual_delta: "Constrained: a quaternionic symmetry commuting with normal Clifford multiplication admits an invariant split selfadjoint domain exactly when its zero-mode half-dimension is even. Other sign cases are classified below."
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Symmetric spectral choices must also satisfy the Green form

**Result.** In the explicitly specified positive-Hilbert Dirac boundary
subclass below, classify every zero-mode boundary space that is both
Green-Lagrangian and invariant under an antiunitary J. If J commutes with
normal Clifford multiplication c and J squared is minus identity, such a
space exists exactly when half the complex zero-mode dimension is even.
The obstruction disappears in the other sign cases subject to the necessary
dimension balance. This refines `P3xsymmetry`; it does not decide class C,
construct a GU action or give a physical family count.

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
expected_delta: Classify selfadjoint spectral zero-space choices compatible with J.
actual_delta: Exact four-sign classification and even-dimensional repair; no class-C verdict.

```gu-typed-objects
result: green-form-symmetry-domain
carrier: zero eigenspace of a selfadjoint elliptic adapted boundary operator LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and skew-Hermitian Green form defined by c ON=declared_carrier
real_structure: antiunitary J with J_squared=epsilon and Jc=sigma_cJ
grading: c eigenvalues plus-i and minus-i; not a physical chirality grading
action_owner: repository-construction -- conditional analytic subclass, no field action
target: selfadjoint spectral boundary subspace MAP-TYPE=inclusion
```

## 1. Analytic contract and prior evidence

The [previous transfer result](p3-boundary-symmetry-transfer-2026-11-11.md)
proves that J must preserve the full operator and the actual trace domain;
it leaves Green-form admissibility separate. Its arbitrary trace-line
half-line example is not asserted to be a selfadjoint Dirac boundary condition.
This result supplies that missing test rather than repeating generic
quaternionic parity or holonomy calculations.

Assume a formally selfadjoint complete Riemannian Dirac-type realization with positive Hermitian
bundle metric, compact boundary, a valid graph trace and Green identity.
Take a selfadjoint adapted elliptic boundary operator B and normal symbol c
with `c*=-c`, `c²=-I`, and `cB=-Bc`. Assume the usual regularity and maximal
domain statements for this realization. The standard spectral construction
`W=E_<0^(1/2)(B) ⊕ L`, `L⊂H0=ker B`, using the H^(1/2) spectral
trace subspace, is selfadjoint precisely when
`H0=L⊕cL` orthogonally. This is the split case of
[Bär and Ballmann, Theorem 3.12 and Remarks 3.13, printed p.11](https://archive.mpim-bonn.mpg.de/id/eprint/1180/1/preprint_2013_44.pdf).
Their theorem supplies the analytic boundary framework; the finite J
classification below is proved directly. Fredholmness on a noncompact
manifold additionally needs the appropriate estimate at infinity.

Require J antiunitary, preserving Dom(B), with `JB=BJ`, `J²=epsilon I`
and `Jc=sigma cJ`, where epsilon and sigma are independently declared signs.
Then J preserves H0 and the negative spectral space. Thus W is J-invariant
exactly when L is. Any extension of J to the bulk must separately satisfy
the appropriate full-operator relation. In a product expression
`D=c(partial_r+B)` with r-independent J commuting with partial_r and B,
`JD=sigma DJ`. In particular the minus sign is an anticommuting bulk
symmetry, not a commuting one. Both preserve a kernel, but their graded
index interpretation still needs a separately specified complex.

The positive elliptic hypotheses are not supplied by Lorentzian Y14, an
indefinite Krein form, or the words APS-type in the C declaration.

## 2. All Green-Lagrangians are unitary graphs

Set `V+=ker(c-iI)` and `V-=ker(c+iI)` inside H0. These are orthogonal and
`H0=V+⊕V-`. Use the convention that the Hilbert form is conjugate-linear
in its first argument; `omega(u,v)=<cu,v>`. For u=(x,y) and v=(x',y'),

`omega(u,v)=-i<x,x'>+i<y,y'>`.

If L is isotropic, both coordinate projections are injective on L: a
nonzero vector in either V alone has nonzero self-pairing. The equality
`L=L^{omega-perp}` requires half dimension, hence
`dim_C V+=dim_C V-=n`. Every such L is then the graph
`L_U={(x,Ux):x∈V+}` of a unique unitary U:V+→V-. Conversely this graph
is isotropic of dimension n, and `H0=L_U⊕cL_U` orthogonally.
Thus unequal dimensions exclude a selfadjoint split spectral choice even
before imposing J. This is a finite boundary-space statement, not an
assertion that arbitrary finite data are realized by an interior operator.

## 3. Complete antiunitary classification

Because J is antilinear, `Jc=+cJ` **exchanges** V+ and V-, whereas
`Jc=-cJ` **preserves** them. Forgetting that conjugation reverses i
interchanges the two cases and gives a false test.

### Commuting normal symbol: sigma=+1

Choose an orthonormal basis in V+ and its J-image in V-. Then

`J(x,y)=(epsilon conjugate(y), conjugate(x))`.

The graph is invariant iff `epsilon U conjugate(U)=I`. Since U is unitary,
this is equivalent to `U^T=epsilon U`.

For epsilon=+1, the symmetric unitary U=I works in every n. For epsilon=-1,
U must be skew-symmetric and invertible, so
`det U=det(-U^T)=(-1)^n det U` forces n even. For even n, the direct sum
of real blocks `[[0,-1],[1,0]]` is unitary and skew-symmetric, proving
sufficiency. These equations describe **all** allowed graphs, not just
the displayed witnesses. In particular H0 of complex dimension two has
a quaternionic J but no invariant Green-Lagrangian; dimension four permits
one. The obstruction concerns simultaneous requirements, not quaternionic
structure alone.

### Anticommuting normal symbol: sigma=-1

Now J restricts to antiunitaries J+ and J- on V+ and V-, each with square
epsilon. The graph is invariant iff

`U J+ = J- U`.

For epsilon=+1, choose orthonormal real bases on both spaces. An intertwining
unitary exists iff their complex dimensions agree, and all choices are real
orthogonal in those bases. For epsilon=-1, each space already has even
complex dimension; choose orthonormal quaternionic paired bases. An
intertwining unitary exists iff dimensions agree; all choices form the
quaternionic unitary group relative to one chosen identification. No further
parity obstruction is introduced by L. The basis construction follows by
choosing a unit vector v, pairing it with Jv (orthogonal when J²=-I), and
inducting on the invariant orthogonal complement.

| sigma | epsilon | Existence of invariant Green-Lagrangian |
| --- | --- | --- |
| +1 | +1 | always; dimensions balanced by J |
| +1 | -1 | n even, where dim H0=2n |
| -1 | +1 | dim V+=dim V- |
| -1 | -1 | dim V+=dim V-; both are already even |

All statements include the zero-dimensional case. They concern one frozen
boundary object. A smooth family requires compatible choices over parameter
space; pointwise existence is not a global spectral-section theorem.

## 4. Released composition: changes between admissible domains

Fix B, c and an admissible positive-Hilbert realization. Two split
selfadjoint choices L0,L1 both have dimension n. Their commensurable domains
have finite quotient spaces modeled on `Li/(L0∩L1)` by the surjective trace.
The signed relative complex dimension is zero. Therefore the existing
[relative-domain formula](p3-symmetry-relative-domain-2026-11-11.md) gives
zero **ordinary relative index** when its Fredholm hypotheses hold. If a
compact linear symmetry also preserves the data, is unitary and commutes
with c, each invariant L is its graph over the same representation V+;
the two L representations are isomorphic and the representation-valued
relative index also vanishes. This strengthens equal-dimension bookkeeping
to an actual representation statement in that subclass.

This is not a constraint on a supplied chiral index: the full ungraded
selfadjoint Fredholm operator already has ordinary index zero. A graded
domain that realizes D+ and its adjoint may have nonzero chiral index, but
its compatibility with this graph classification must be proved. It also
does not cover changing B, its Fredholm component, or infinite-dimensional
noncommensurable boundary changes. Those were distinct in the earlier notes.

The [moving-gauge result](x-p1-p2-moving-gauge-naturality-2026-11-11.md)
adds one more condition: a transported J and transported L at another
background are not a fixed-background symmetry/domain pair. Only after
that identification can the four-sign test constrain the same realization.

## 5. Released family test: every point passes, but no periodic choice exists

The pointwise classification does not solve the family problem. An explicit
finite boundary-data family on the circle proves the distinction. On the
trivial H0=C2 bundle take `c=diag(i,-i)`, `B=0`, and

`J_t(x,y)=(conjugate(x), exp(it) conjugate(y))`, `t mod 2pi`.

J is a smooth periodic antiunitary with J squared=I, commutes with B and
anticommutes with c. Every point therefore passes the balanced real case
in the table. Every Green-Lagrangian is the graph of a scalar u in U(1).
Its invariance condition is `u=exp(it) conjugate(u)`, equivalently
`u²=exp(it)`. There is no continuous periodic solution: on the interval
[0,2pi] a continuous phase lift u=exp(i theta) gives
`2theta(t)-t=2pi k` with constant integer k. Thus
`theta(2pi)-theta(0)=pi`, so the endpoints have opposite u. The local
choice exp(it/2) succeeds and returns its negative, an actual obstruction
to a global domain choice. This is not a claim about an interior GU action.

More generally in the preserving case sigma=-1, for a constant-rank smooth
family, invariant unitary graphs are exactly unitary isomorphisms of the
real bundles fixed by J+ and J- when epsilon=+1, or of their quaternionic
bundles when epsilon=-1. Equal rank is only a pointwise condition. A real
or quaternionic bundle isomorphism can be made isometric by fibrewise polar
normalization with the supplied metrics; its positive square root respects
the real/quaternionic structure. This gives necessity and sufficiency at
the bundle level without constructing the bundles for C. In the circle
control the two real line bundles differ: a local negative-space fixed
basis exp(it/2) changes sign around the circle, whereas the positive-space
fixed basis is constant. This is the same obstruction proved above.

The circle control has constant B and constant zero-eigenspace dimension, so the failure is not
an eigenvalue-crossing artifact. Varying kernels, spectral sections and
an actual analytic family require additional hypotheses. The result
eliminates the inference that checking the four-sign table pointwise
suffices for global domain selection.

## 6. Evidence and scope

The [exact probe](../../tests/program-focus/p3_green_form_symmetry_domain_probe.py)
checks actual c/J relations, graph isotropy, invariant/noninvariant controls,
the n=2 repair, unequal dimensions, and finite relative representations.
The [evidence record](../../lab/process/p3-green-form-symmetry-domain.json)
separates those finite checks from the universal proofs above. The analytic
framework is cited, not re-proved by a small matrix. Independent internal
specialist and hostile review are required before acceptance.

`P3xsymmetry` stays constrained. SC-CHI-01/51 retain ASSERTS for non-chiral
total/effective chiral physics; SC-GEN-02/03 retain ASSERTS for native 2+1
labels. An ordinary Dirac boundary index is not that observation mechanism.
RA-F1, AC-F1 and LT-SM8 remain NEEDS. No source, ledger, class-C, canon,
physical count, Lean certification or external-expert verdict changes.
