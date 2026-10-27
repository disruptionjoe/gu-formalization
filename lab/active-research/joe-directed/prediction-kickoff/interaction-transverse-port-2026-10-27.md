---
artifact_type: exploration
doc_type: conditional_build_result
status: exploration
claim_verdict: internally_reviewed_conditional_mathematics
created: 2026-10-27
title: "The source mixed fermion port: all-null unrestricted-input exclusion and a fixed grade-six on-shell escape"
target_claim: NONE-NOT-A-KILL
source_claims: [SC-OP-04, SC-OP-05, SC-FER-07, SC-GEN-53]
canon_verdict_change: none
probe: tests/channel-swings/source_native_fermion_transverse_port_probe.py
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: exact local mixed-port annihilator and null-quotient condition, all-null exclusion for unrestricted spinor inputs, and a fixed grade-six on-shell-input escape under the supplied frozen constraints
carrier: a supplied frozen nondegenerate n-dimensional quadratic tangent space V, full Dirac module S, and V* tensor S; source-facing application n=14 on the declared K77 construction, with external constraints supplied locally LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: supplied nondegenerate Clifford-skew spinor pairing B and the metric-induced vector-spinor pairing ON=the full Dirac and one-form spinor spaces; this is an explicit local duality horn, not a source-selected global adjoint or a positive Hilbert form
real_structure: real full-Dirac K77 is the source-facing construction; K95 is only a separate complexified Clifford-sign control, never a transported real module or physical signature choice
grading: one-form degree and gamma-trace versus momentum-transverse constraints; ambient half labels, spacetime chirality and family labels remain separate
action_owner: repository-construction supplies the local pairing, frozen covector, external constraint space and optional radical quotient; source equation 9.16 supplies the mixed connection/derivative grammar only
target: classify when a mixed port a:S to V* tensor S gives a nonzero paired bilinear on a declared transverse gamma-kernel, and when that functional descends to its null radical quotient MAP-TYPE=intertwiner
```

# Result and use

For a nonzero covector `k`, put `T_k = ker Gamma intersect ker d_k`, where
`Gamma` is Clifford trace and `d_k` is contraction with `k`. A connection
insertion `a:S -> V* tensor S` has zero paired bilinear against **every**
external state in `T_k` exactly when

```text
a_i = k_i X + gamma_i Y                           (1)
```

for some spinor endomorphisms `X,Y`. Thus the derivative port `a_i=k_i I`
and every pure Clifford-trace port are invisible to this external sector.
Generic connection components survive; an explicit nonzero Spin-valued
control is given below. This is a local conditional amplitude criterion,
not a scattering amplitude or an observed particle statement.

The sharper result is on the null cone. When `q=g^-1(k,k)=0`, the pairing on
`T_k` has the full injective twistor image

```text
R_k = { k_i psi - (1/n) gamma_i slash(k) psi : psi in S }  (2)
```

as its radical. Its dimension is `dim S`, **not** `dim ker slash(k)`.
A mixed-port functional descends to the algebraic quotient `T_k/R_k` iff

```text
[ d_k - (1/n) slash(k) Gamma ] a = 0.               (3)
```

A generic connection fails (3), while nonzero Spin-valued connections can
pass at one fixed momentum. This is an exact additional equation that a proposed null-quotient
interaction must satisfy. Calling a gamma-traceless port nonzero is
insufficient. Neither the quotient nor these external constraints have been
identified with the GU physical state space.

The strongest exclusion holds when a single zero-order port `a` is held
independent of momentum and (3) holds as an operator on **all of `S` for
every** nonzero null covector in an indefinite metric. Then
`a_i=gamma_i Gamma(a)/n`. It is pure Clifford
trace and therefore invisible against every `T_k`. This excludes a nonzero
fixed zero-order mixing with **unrestricted inputs** on the whole family
of these frozen null quotients.
The pointwise surviving controls do not evade that theorem: they work only
on restricted momentum directions or require momentum-dependent coefficients.
But a separately constructed fixed grade-six port passes descent for
massless inputs `psi in ker slash(k)` at every null momentum. Its response
is `Z slash(k)/2` and vanishes on those inputs; its quotient functional
is nonzero at the exhibited K77 momentum. This distinction is essential: unrestricted-input
descent is stronger than on-shell amplitude descent. Neither construction
is a selected GU physical interaction.

## Source placement and prior-art boundary

The [rendered section-9 extraction](../../../sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md)
fixes equation (9.16), its independent barred/unbarred fields, reversed row
order, `d0+varpi` mixed cells and negative formal-adjoint-shaped lower cells.
It also fixes the source's candidate strength and admits a nonzero southeast
rival. The same extraction records the unresolved collision between ambient
half labels and the derivative parity of the simple `Phi d` construction.
This note uses the full-Dirac mixed **one-form port**; it does not repair that
collision or identify a barred field with a Hermitian adjoint.

The following results are reused, not claimed anew:

- HE-1/HE-3/HE-4 own the complex `16/144` ladders, cross-half bilinear versus
  within-half arrow distinction and independent family-row/`54`/`210` data.
- [CB-2](../high-energy-two-plus-one/cb2-h210-equation916-cross-half-composition-2026-08-16.md)
  owns the source cell placement and its density-dual caveat.
- CB-8 owns derivative-adapter covariance and its reverse first-jet term;
  no adapter or missing receipt is reconstructed here.
- [The August 10 principal discriminator](../../../../explorations/conditional-build/selected-k77-induced-fermion-principal-discriminator-2026-08-10.md)
  owns the complete nonnull/null symbol ranks and the mirror equality.
- [The moving-varpi stationary intersection](../../../../explorations/conditional-build/selected-k77-moving-varpi-stationary-intersection-2026-08-10.md)
  owns the tautological `varpi_i=s gamma_i` branch and its gamma-trace kernel.
  Its branch amplitudes are not selected or rerun here.
- The old VZ Schur calculations split gamma trace from gamma kernel. Their
  Schur result is not the additional `k`-transverse pairing radical computed
  here; no VZ causality conclusion is imported.
- [The August 30 observation obstruction](../../../../explorations/source-native-spin64-observation-sector-obstruction-2026-08-30.md)
  already proves that literal observation need not preserve ambient gamma
  kernels. A local zero here therefore cannot silently be pushed to the
  observed carrier.

The new result is the exact **mixed-port annihilator and null radical
descent condition**, composed with the source's actual one-form grammar.
The projector technique is standard Clifford linear algebra, with no claim
of mathematical novelty outside this application.

## General proof

Work over characteristic zero with `n >= 3`, a nondegenerate quadratic
space, and a full Clifford module `S` of dimension `d`. Supply a nondegenerate
bilinear pairing `B` for which Clifford multiplication is skew:
`B(gamma(v)x,y)=-B(x,gamma(v)y)`. A compatible sesquilinear version has the
same argument with conjugate adjoints. The real-matrix probe uses a bilinear
pairing, and makes no reality identification of the source bars.

In a pseudo-orthonormal coframe with signs `eta_i`, use lower gamma matrices
`gamma_i^2=eta_i`. Define

```text
(j psi)_i = gamma_i psi,       Gamma z = sum_i eta_i gamma_i z_i,
(u psi)_i = k_i psi,           d_k z   = sum_i eta_i k_i z_i,
s = slash(k) = sum_i eta_i k_i gamma_i,       q = sum_i eta_i k_i^2.
```

Then

```text
Gamma j=nI,   Gamma u=s,   d_k j=s,   d_k u=qI,   s^2=qI,
j^times=-Gamma,            u^times=d_k.              (4)
```

The vector-spinor pairing is `B_V(z,w)=sum eta_i B(z_i,w_i)`.

### Complete annihilator, including null k

The images `jS` and `uS` are disjoint for every nonzero `k`. Indeed, if
`u x+j y=0`, contraction with a nonnull vector perpendicular to `k` gives
`gamma(v)y=0`, hence `y=0` and then `x=0`. Such a vector exists for `n>=3`.
The adjoint of `C=(Gamma,d_k)` is therefore injective, so `C` is surjective.
Consequently

```text
dim T_k=(n-2)d,                 T_k^perp = uS + jS.  (5)
```

Apply (5) to each input column of `a`. This proves (1) in both directions.
It uses a nondegenerate pairing on the ambient space, not positivity of its
restriction. It therefore remains valid at null `k`.

### Nonnull projector

For `q!=0`, set

```text
j_perp = j-u s/q,       Gamma_perp=Gamma-s d_k/q,
Pi_k = I-u d_k/q-j_perp Gamma_perp/(n-1).             (6)
```

Equation (4) gives `Gamma_perp j_perp=(n-1)I`. The longitudinal and
perpendicular Clifford-trace projectors annihilate each other. Thus (6) is
an idempotent, pairing-self-adjoint projector onto `T_k`, with kernel
`uS+jS`. The surviving mixed vertex is exactly `Pi_k a`. Equation (6)
must **not** be evaluated at `q=0` or assigned a finite null limit.

### Null radical and quotient condition

For `q=0`, an element of `T_k intersect T_k^perp` has the unique expression
`u x+j y`. Applying (4) gives

```text
s x+n y=0,                  s y=0.
```

The second equation follows from the first because `s^2=0`. Hence
`y=-s x/n`, proving (2). The map `t=u-j s/n` is injective because `uS` and
`jS` are disjoint. Thus `dim R_k=d` and the radical quotient has dimension
`(n-3)d`.

For a fixed input `psi`, the functional `z -> B_V(z,a psi)` is independent
of the representative of `[z] in T_k/R_k` precisely when it vanishes on
`R_k`. Since

```text
t^times=d_k-s Gamma/n,
```

this is exactly (3). This is functional descent only. It does not assert
that `a` lands in `T_k`, that a full differential descends, or that the
radical is gauge. The source must separately supply those physical claims.

There is also a precise parameter count. At null `k`, `t^times` is
surjective. The space of maps `a:S -> V* tensor S` satisfying (3) has
dimension `(n-1)d^2`; quotienting the invisible maps (1), which have
dimension `2d^2`, leaves `(n-3)d^2` possible bilinear couplings. Off the
null cone the corresponding space has dimension `(n-2)d^2`. These are
dimensions of **unrestricted full-Dirac linear-map spaces**. Restricting to
a particular source Lie algebra or chirality block requires intersection,
and may change the count. None is a particle or family count.

### Principal source-shaped operator

For the already-owned simple contraction, the rolled upper-left symbol is

```text
R(k)=s I-u Gamma.
```

On `T_k` it reduces to `s I` and preserves both constraints. At null `k`,

```text
R(k)t = ((n-2)/n) t s.                              (7)
```

It therefore preserves the radical as well. This supplies a local
principal-symbol consistency check for the optional algebraic quotient;
zero-order terms, moving pairings, observation, boundary conditions and the
source half-label collision remain separate. The southeast-zero branch is
not invoked as a uniqueness theorem.

There is a concrete source-shaped reason to retain the **on-shell input**
escape rather than imposing unrestricted inputs by default. For this same
fixed simple-contraction, displayed-southeast-zero horn, write the complete
coupled principal symbol as

```text
D(k)(zeta,nu)=((sI-u Gamma)zeta+u nu, -d_k zeta).
```

At null k, its characteristic kernel projects onto **exactly `ker s` in
the nu slot**. Indeed the lower equation gives `d_k zeta=0`. Applying
s and Gamma to the upper equation gives, respectively,

```text
s(nu-Gamma zeta)=0,       s(nu-2 Gamma zeta)=0.
```

Here `Gamma(s zeta)=2d_k zeta-s Gamma zeta` fixes the factor two and
the signs. Subtraction yields `s Gamma zeta=0`, then `s nu=0`.
Conversely, any `nu in ker s` has the explicit lift

```text
zeta=j nu/(n-2),
```

because `R(k)j nu=(2-n)u nu` and `d_k j nu=s nu=0`.
Thus the unrestricted-input theorem below **does not exclude** mixing
on these actual characteristic nu inputs. The grade-six escape is
compatible with this necessary input condition. This conclusion is only
for the inherited fixed simple-Phi principal horn; the released source's
unresolved half-label placement, other contractions, lower terms and
physical quotient are not thereby settled.

## Exact contrary constructions

Take the real `Cl(2,2)` control with `eta=(+,+,-,-)` and null
`k=(1,0,1,0)`. Its four-dimensional spinor module is an independent small
fixture, not the GU carrier. Choose bivector-valued connection components

```text
a_1=gamma_0 gamma_1,       a_3=gamma_3 gamma_0,
a_0=a_2=0.                                           (8)
```

Direct Clifford multiplication gives

```text
Gamma a=0,         d_k a=0,         a^times a=2I.
```

Thus this Spin-valued port satisfies (3) and has a nonzero paired bilinear
on the quotient. It disproves a universal interaction zero under the stated
constraints. In contrast, setting only `a_0=gamma_1 gamma_3` gives
`t^times a != 0`: a genuine Spin-valued counterexample to automatic null
descent. The bare derivative port `a=u` is invisible exactly, and a pure
Clifford-trace connection is invisible without imposing transversality.

The null radical is larger than the tempting candidate `u ker(s)`.
In this fixture the latter has dimension two while `R_k` has dimension
four. Replacing (2) by that smaller space loses genuine conditions in (3).

## Immediate consumer: the existing decomposable source-shaped port

The nearest coefficient-complete consumer is the existing
[four-field zero-order port](../../../../explorations/conditional-build/selected-k77-four-field-zero-order-port-2026-08-10.md),
not a new action. It fixes

```text
a_i=v_i P,       v=(2,-1,0,1,0,...,0),
```

with invertible `P` in each of its grade-two moving-Spin, grade-six two-half
and grade-one full-parent controls. These are repository-owned explicit
source-shaped coefficient insertions; the released source does not select
this particular `v` or `P`. Equation (3) now gives an exact new consequence:

```text
t_k^times a = [ (k dot v)I - slash(k)slash(v)/n ] P.  (9)
```

For null nonzero `k` and invertible `P`, (9) is zero **iff `v` is proportional
to `k`**. To prove necessity, remove `P`, and separate Clifford scalar and
two-form grades:

```text
slash(k)slash(v)=(k dot v)I+gamma(k wedge v).
```

The scalar component gives `(n-1)(k dot v)=0`, and the two-form component
then gives `k wedge v=0`. Full-Dirac Clifford action is faithful on these
grades in the `n=14` application. Sufficiency follows from `slash(k)^2=0`.
But `v` proportional to `k` makes `a` longitudinal and completely invisible
by (1). Therefore:

> An invertible-parent decomposable port cannot give a nonzero descended
> mixed bilinear on this null radical quotient. A nondecomposable coefficient
> outside the invisible subspace is necessary **within the invertible-parent
> class**.

The banked `v` has squared norm `6` in its fixed K77 frame, so it is not
parallel to any nonzero null `k`. Its null functional fails (3) for **every**
nonzero null covector, across all three invertible parent controls. An
invertible spinor factor or a simultaneous Pin reflection preserves this
conclusion; choosing a different parent cannot remove the form-leg failure.
This neither reverses the predecessor's correct port-image inclusion result
nor tests its physical graph by implication: the newly imposed quotient is
additional construction data.

**Singular-parent escape, explicitly alive.** Invertibility is essential.
Set `P=slash(k)`, which is nonzero and singular at null `k`. Then

```text
t_k^times (v slash(k))=(1-2/n)(k dot v)slash(k).
```

For `v` perpendicular to `k` but not parallel, this is zero. In the
`Cl(2,2)` fixture take `v=e_1` and `k=e_0+e_2`. The resulting decomposable
port has a nonzero rank-two functional on the radical quotient. To see
nonvanishing without a norm argument, suppose `v slash(k)=u X+j Y`.
Contract with the nonnull `e_3`, orthogonal to both `k,v`; this forces
`Y=0`, after which the distinct form directions forbid equality with
`u X`. The probe computes the nonzero cross-pairing directly. Its
self-pairing is nevertheless zero because `slash(k)^2=0`; zero self-norm
is not zero bilinear coupling in an indefinite space. This is a supplied
momentum-dependent pointwise symbol, not an identified source zero-order
connection, an off-shell vertex, or a physical rescue.

The nearest stationary coefficient is the already-owned tautological
`a_i=s gamma_i` in the moving-varpi result. It passes (3) but is exactly
invisible. Its column-Pin completion leaves the forward port unchanged.
For its row-Pin completion, with `Q=gamma_7`, `Q^2=-I` and reflection `r`
that negates component seven, the actual forward components are
`r_i Q gamma_i Q=gamma_i`; they are also unchanged. Thus both existing
completions give the same zero against this external sector. This does not
reopen CB-8 or require a new derivative adapter.

These pointwise controls are consumed by the stronger **unrestricted-input**
all-null theorem below. They do not justify another search for a fixed
coefficient that survives every null direction on all input spinors with
the same constraints. Restricting the input to a stated equation of motion
is a separate admissible route, and the fixed grade-six construction below
closes that algebraic escape positively. Momentum-dependent interactions
or changed coupled constraints/observation remain separate routes.

The concrete next test is the existing source coefficient/cell/real-pairing
admissibility test for the grade-six on-shell construction, together with a
source-owned input equation and external quotient. Merely finding another
fixed matrix cannot settle those types. The whole action need not be
derived to run this local admissibility test.

## All-null theorem: a fixed zero-order port must become invisible

Freeze the metric, Clifford map, pairing and the external spaces
`T_k/R_k` above at one background point. Let `a:S -> V* tensor S` be
independent of `k`, and assume the real metric is indefinite with both
signs present. Require the displayed equality as a map on the **full input
space `S` for every k**, not merely on `ker slash(k)` or another moving
on-shell input space. Then the following are equivalent:

```text
t_k^times a=0 in Hom(S,S) for every nonzero null k;
a_i=gamma_i Y for one Y in End(S), namely Y=Gamma(a)/n.  (10)
```

**Proof.** Write `b_i=a_i-gamma_i Gamma(a)/n`. Equation (3) becomes

```text
t_k^times a=sum_i eta_i k_i b_i.                       (11)
```

This is linear in `k`. Real null covectors span every nondegenerate
indefinite quadratic space: if `e_0` is a positive unit covector and
`e_p` a negative one, a concrete null basis is

```text
e_0+e_p, e_0-e_p;
e_i+e_p  for all remaining positive i;
e_0+e_j  for all remaining negative j.                 (12)
```

The first two vectors span `e_0,e_p`; each remaining vector then adds
its distinct coordinate. Thus (11) vanishes on all null covectors iff
every `b_i=0`, proving necessity. Sufficiency follows from
`Gamma j=nI`. Equation (1) now shows that this port has zero paired
bilinear against **every** transverse gamma-kernel. QED.

For K77, (12) consists of fourteen explicit null covectors with
`p=7`. Its coefficient matrix has rank fourteen (determinant of absolute
value two before metric signs). The executable certificate checks every
null norm, the full rational rank, and the complete Clifford-coefficient
identity (11), not a sample of ports. It separately checks the same
linear-algebra certificate for the K95 sign control without transporting
real Clifford structures.

This proof does not require an invertible parent coefficient or a
decomposable form. It covers arbitrary fixed `a`, including singular and
nondecomposable coefficients. It applies pointwise to a spatially varying
zero-order `a(x)` if the demand is all null directions and all input
spinors at each point. It does **not** allow the input subspace to vary
with k before invoking null spanning.

**The pointwise controls fail the all-null test.** In the `Cl(2,2)`
control, retain (8) but change from `k=e_0+e_2` to the also-null
`k'=e_1+e_2`. Since `Gamma a=0`, its new response is simply
`t_k'^times a=a_1=gamma_0 gamma_1 != 0`. The singular port with its
original fixed coefficient `P=slash(e_0+e_2)` likewise fails at `k'`.
Changing `P` with `k` leaves the fixed zero-order class, and even the
earlier momentum-dependent singular control required `k dot v=0`.

### A fixed on-shell-input escape, including a pure grade-six port

For even n let `Z` be a fixed homogeneous Clifford element of middle grade
`r=n/2`, and take `a_i=Z gamma_i`. The standard sandwich identity gives

```text
Gamma(a)=sum_i eta_i gamma_i Z gamma_i=(-1)^r(n-2r)Z=0,
t_k^times a=Z slash(k).                               (13)
```

This vanishes on `ker slash(k)` for **every** null k while `a` is generally
nonzero and not pure Clifford trace. It is a fixed momentum-independent
port; the assumption it changes is the input domain, not the coefficient.
The independent `Cl(2,2)` control chooses `Z=gamma_0 gamma_1`. The probe
finds a rank-two nonzero quotient functional after restricting the input
to the two-dimensional `ker slash(e_0+e_2)`, and checks the response formula
at a second null covector. Thus the escape is constructive, not deferred.

For the actual n=14 Clifford algebra, choose fixed grade-seven Z and
project to

```text
a_i=(Z gamma_i+gamma_i Z)/2,
Gamma(a)=7Z,          t_k^times a=Z slash(k)/2.         (14)
```

Because grade seven is odd, the anticommutator in (14) contains only
grade six. Relative to the supplied Clifford-skew pairing, a pure
grade-six word has adjoint sign `(-1)^(6*7/2)=-1`; each coefficient is
therefore skew. Equation (14) passes the null-functional condition for
every massless input without being a pure-trace fixed port.

It also has a nonzero quotient bilinear in the K77 construction. Set
`Z=gamma_0...gamma_6` and `k=e_0+e_7`. Coefficients with indices outside
`0,...,6` vanish, while `a_1` is an invertible product of six Clifford
generators. If `a psi=u x+j y`, component eight forces `y=0` because
`k_8=a_8=0` and `gamma_8` is invertible. Component one then forces
`a_1 psi=0`, hence `psi=0`. Thus the paired functional is nonzero for
every nonzero input in `ker slash(k)` and has rank 64 on that real K77
input space. The rank `dim S/2` uses the standard nonzero-null Clifford
identity `im slash(k)=ker slash(k)`, obtained by anticommuting with a
covector having nonzero pairing with k. It is a conditional amplitude-map
rank, never a family or physical-state count.

The probe checks the complete n=14 coefficient identities, pure grade-six
support and pairing sign, plus the invertible `a_1` and vanishing `a_8`
used in this proof. It does not build an unowned full interaction or run
a large carrier computation. Z is supplied; source cell placement, real
unitary/Krein compatibility beyond this local skew test, input equation,
observation and physical quotient still require their existing admissibility
tests. The coupled principal calculation above already supplies the
massless-input necessity and lift within its fixed simple-Phi horn; it
does not supply those remaining bridges. The source half-label collision
is not resolved by Clifford degree.

**Exact scope.** The exclusion in (10) is a necessary-condition result for
a fixed mixed port on unrestricted spinor inputs, descending to this entire
*supplied* family of radical quotients. It does not prove these radicals are gauge, impose them on the
internal144, or rule out source interactions. A full interacting theory
can restrict inputs by their equations of motion, as (13)--(14) demonstrate,
or change the characteristic surface, constraints, physical quotient or
derivative vertex. Such a construction must be stated before applying (10).
No positivity, causality or physical-state theorem is inferred.

## What this changes for the family question

The source's total theory remains nonchiral and its claimed mechanism is
`2+1`; no conventional net-index target is substituted. Imposter128,
internal partner144 and separately labeled RS384 remain different objects.
In particular, `Gamma z=0` for an internal144 is **not** a statement that
`d_k z=0` for a spacetime momentum, or that observation intertwines either
constraint. This note does not impose a transverse RS condition on the
partner144 and then use it to exclude the native mechanism.

The forward `d0` port and pure Clifford-trace ports cannot provide a nonzero
interaction against the declared transverse sector. A proposed surviving
null-quotient port must additionally pass (3), and (8) shows that this
requirement permits nonzero interaction at one momentum. Requiring one
fixed zero-order port to pass at all null momenta on **unrestricted input
spinors** leaves only invisible Clifford trace by (10). Restricting to
massless inputs permits the fixed nonzero grade-six construction (14).
These are distinct zero/survival tests for future source/observation placement.

The equations act on form/spinor factors and do not select a family covector.
They cannot turn HE-3's independent family rows into a selected rank-one
row. A family label, physical quotient, scale, sign, threshold and observable
remain unconstructed; the result is not a new prediction packet.

## Evidence and reproduction

General results (1)--(7) follow from the written finite-dimensional proof.
The probe independently constructs explicit real `Cl(2,2)` matrices and
computes the constraint kernels, restricted pairing ranks, radical,
nonzero surviving port and failing port with rational arithmetic. It also
checks the projector and radical identities in the actual `n=14` sparse
Clifford algebra for both K77 and K95 signs. K95 is only an algebraic
complexified control; no real `128`-dimensional K95 module is asserted.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/source_native_fermion_transverse_port_probe.py
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/source_native_fermion_transverse_port_probe.py --selftest
```

The selftest first checks the clean baseline, then changes six actual
constructions: the projector normalization, null-trace normalization,
Clifford multiplication order, one surviving-port sign and a null-basis
vector (replaced by a duplicate, destroying span), and the relative sign
in the middle-grade port projection. Each must cause
a mathematical check to fail; crashes do not count as detection.

The serialized probe passes 125 exact finite checks and rejects all six
actual construction mutations without counting crashes as detection. Independent
internal review accepted the derivations, including the restricted-input escape
and simple coupled principal projection. Finite controls are distinct from
the general proof. Internal review does not constitute
external-expert review, proof-assistant certification or physical validation.

## Hostile reading and exact ceiling

**Strongest overclaim:** “The source's family144 coupling vanishes” or “the
radical is the physical gauge sector.” Neither follows. Both require the
missing carrier/observation/action/physical-state bridge.

**Strongest contrary construction:** an observed physical sector may have
different constraints, a different paired dual, a degree-dependent map or
a momentum-dependent/nonminimal vertex, or restrict the input by its own
equation of motion. The theorem then applies only after
those data are typed. Within the present assumptions, (8) defeats a
single-momentum no-interaction claim but fails the all-null requirement;
(14) is the stronger fixed-coefficient escape when the input is massless.
Both distinctions are certified rather than treated as proposed repairs.

**Weakest reproducibility seam:** the full `n=14` test uses symbolic
Clifford coefficients rather than a huge explicit carrier matrix. Its
coefficient identities are exact; kernel/radical dimensions additionally
use the written surjectivity argument and independent small real matrices.

**Ceiling:** exact local conditional Clifford/paired-bilinear mathematics;
source mixed-port grammar is cited, while the pairing, external constraints
and radical quotient are supplied construction data. No source-selection,
half-label repair, physical amplitude, family rank, particle count, mass,
energy scale, positivity, empirical prediction or canon movement follows.
