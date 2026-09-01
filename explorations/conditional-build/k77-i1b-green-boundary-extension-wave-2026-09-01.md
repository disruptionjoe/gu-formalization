---
title: "K77 I1B Green-boundary extension wave"
status: active_research
doc_type: reverse_scaffold_i1b_green_boundary_extension_result
date: 2026-09-01
claim_ceiling: exact minimal/maximal-domain, Green-form and self-adjoint-extension classification for one repository-owned positive two-component regular-singular radial control; no actual source-owned cross-null operator, native positive pairing, physical boundary law, coefficient selector, prediction, confirmation or GU verdict
manifest: lab/process/k77-i1b-green-boundary-extension-wave.json
probe: tests/channel-swings/k77_i1b_green_boundary_extension_probe.py
---

# K77 I1B Green-boundary extension wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: exact Green identity, singular trace plane, minimal/maximal boundary data and U(1)-equivalent Lagrangian self-adjoint extension family for a positive regular-singular control
carrier: complex two-component sections on 0<u<1 with frozen kappa=1/4 LAYER=conditional CHIRALITY=N/A
pairing: positive repository-owned Hilbert pairing integral f^*g du ON=two_component_radial_control; not the native alternating I1B Green form and not a physical state pairing
real_structure: componentwise conjugation, preserved because J, S, H, kappa and a are real
grading: two indicial modes u^(-kappa)e1 and u^(kappa)e2; no gauge, BRST, BV or physical grading
action_owner: repository owns the frozen control only; no filed source action owns this operator, positive pairing or endpoint law
target: whether the bounded tangential coefficient a changes the leading Green boundary form or the singular self-adjoint extension space MAP-TYPE=classification
```

## Freeze a genuinely positive symmetric control

Work in the positive Hilbert space

```text
H = L2((0,1),du;C^2),
<f,g> = integral_0^1 f(u)^* g(u) du,
```

with matrices

```text
J = [[0,-1],[1,0]],   S = [[0,1],[1,0]],   H = [[1,0],[0,-1]],
J^*=-J,               S^*=S,               H^*=H.
```

For real `a` and the frozen `kappa=1/4`, define the formal expression

```text
D_(kappa,a) f = J f' + (kappa/u) S f + a H f.                 (1)
```

This is formally symmetric for the displayed positive pairing. Multiplying
the zero-mode equation by `-uJ` gives

```text
u f' + (kappa H - a u S) f = 0.                              (2)
```

Thus `a` is a bounded, lower-indicial-order tangential coefficient: the
indicial family is `I(z)=zI+kappa H`, with modes

```text
u^(-kappa)e1,      u^(kappa)e2.                               (3)
```

At `kappa=1/4`, their squared densities are `u^(-1/2)` and
`u^(1/2)`, so both lie in `L2(du)` at zero. More generally this endpoint is
limit-circle exactly for `|kappa|<1/2`; at `|kappa|=1/2` one mode has the
logarithmically divergent density `u^(-1)`, and for `|kappa|>=1/2` the endpoint
is limit-point. This terminology applies to the symmetric control (1), not to
the earlier weighted mode count alone.

## Minimal and maximal domains

Define

```text
Dom(Dmax,a) = {f in H: f is AC_loc and D_(kappa,a)f is in H},
Dmin,a = closure of D_(kappa,a) on C_c^infinity(0,1;C^2).
```

Because `aH` is bounded and self-adjoint,

```text
Dom(Dmax,a)=Dom(Dmax,0),     Dom(Dmin,a)=Dom(Dmin,0)            (4)
```

as sets; the corresponding graph norms are equivalent. For every maximal-
domain section the singular traces exist:

```text
c_-(f)=lim_(u->0) u^kappa f_1(u),
c_+(f)=lim_(u->0) u^(-kappa) f_2(u).                           (5)
```

The trace map onto `(c_-,c_+) in C^2` is surjective. The full minimal domain
has

```text
c_-=c_+=0,       f(1)=0,                                      (6)
```

whereas the full maximal domain permits arbitrary singular trace in `C^2`
and arbitrary regular trace in `C^2` at `u=1`. Therefore the maximal/minimal
boundary quotient is the direct sum of the two endpoint trace planes. These
are operator-domain statements, not an `L2` count relabelled as a boundary
law.

## Green form and singular Lagrangians

Integration by parts gives the exact Green identity

```text
<Dmax,a f,g>-<f,Dmax,a g>
 = omega_0(gamma_0 f,gamma_0 g) - f(1)^*Jg(1),                 (7)

omega_0(c,d) = -conj(c_-)d_+ + conj(c_+)d_- .                 (8)
```

The zero-order term cancels from (7) because `aH` is Hermitian. The singular
trace plane is nondegenerate and skew-Hermitian. Its complex Lagrangian lines
are exactly

```text
L_theta = {(c_-,c_+): cos(theta)c_-+sin(theta)c_+=0},
theta in R/pi Z,                                                (9)
```

equivalently `c_+=lambda c_-` with `lambda in R union {infinity}`.
Via a Cayley transform this circle is the usual `U(1)` self-adjoint-extension
parameter. An arbitrary complex slope is not isotropic; for example the line
spanned by `(1,i)` has `omega_0(v,v)=-2i`.

To isolate the singular endpoint, fix the regular Lagrangian condition
`f_2(1)=0`. Start from the closed symmetric domain with this regular condition
and `c_-=c_+=0`. Its deficiency indices are `(1,1)`. Every endpoint-separated
self-adjoint realization, and no other endpoint-separated one with that fixed
regular condition, has

```text
Dom(D_(a,theta)) = {f in Dom(Dmax,a): f_2(1)=0,
                    gamma_0(f) in L_theta}.                   (10)
```

Thus the weighted `L2` fact that both modes survive only identifies the
limit-circle regime. Self-adjointness comes from maximal isotropy of (8) and
the adjoint-domain calculation.

## The bounded coefficient changes neither boundary form nor extension space

For every finite real `a`, `aH` is a bounded self-adjoint multiplication
operator. Equation (4) fixes the minimal and maximal domain sets, while its
cancellation in (7) fixes the Green form. Consequently the singular boundary
trace plane, its Lagrangian Grassmannian and every domain (10) are identical
for all finite `a`, including `a=log(2)` and `a=log(3)`:

```text
D_(a,theta) = D_(0,theta) + aH                               (11)
```

on the same domain, and bounded self-adjoint perturbation preserves
self-adjointness. This is stronger than leading-order indicial blindness for
the frozen model: `a` does not alter the exact Green boundary form or the
extension-domain family. It may alter spectra, resolvents and zero modes
inside a chosen extension, so spectral equality is not claimed.

## Ownership, limitation and next condition

The algebraic/manifest probe checks the matrix, threshold, declared trace,
Green and Lagrangian data and carries a hostile mutation selftest. The analytic
trace-surjectivity, adjoint-domain, deficiency-index and extension-completeness
claims rest on the derivation above; they are not independently mechanized by
that probe. The result belongs only to the repository-owned operator (1). In
particular, (1) is **not established as
the actual source cross-null I1B operator**; `du`, the positive fibre metric,
the residue `(kappa/u)S`, the bounded term `aH`, the regular boundary condition
and the endpoint law are frozen controls. The native I1B packet instead owns
rank-changing presymplectic data, and no typed bridge identifies its Green
quotient with this positive Hilbert control.

The `H` in this packet is a bounded coefficient matrix inside a positive
complex Hilbert pairing. It is not the indefinite real carrier form called
`H` in the separate null-first-jet packet. The two packets cannot be unioned
to claim a null bridge with this endpoint family.

Boundedness is load-bearing. Replacing `aH` by `(a/u)H` changes the indicial
matrix to `kappa H-aS`, whose eigenvalues are
`+/-sqrt(kappa^2+a^2)`. That contrary construction can move the
limit-circle/limit-point threshold and shows why this theorem does not cover
an actual operator in which the coefficient enters the singular residue.

Therefore no source/action-owned boundary law, physical self-adjoint
realization, selector of `log(2)` versus `log(3)`, prediction, confirmation or
GU verdict follows. A genuine reopener must derive the actual cross-null
operator, measure and positive/indefinite pairing from the source action. If
that operator gives `a` an unbounded `1/u` contribution, makes the principal
normal matrix depend on `a`, changes the measure, or couples matching data
across the rank jump, this control theorem does not transfer.
