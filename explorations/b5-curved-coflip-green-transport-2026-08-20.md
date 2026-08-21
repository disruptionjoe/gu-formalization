---
title: "B5 curved coflip and Green transport: complete folded trace symbol and null radical"
status: active_research
doc_type: exact_curved_green_transport
created: "2026-08-20"
registry: lab/process/b5-curved-coflip-green-transport.json
probes:
  - tests/channel-swings/b5_curved_coflip_green_transport_probe.py
grade: "ON THE ACTUAL COMPLEXIFIED (9,5) STRICT B5 CARRIER, THE COMPLETE FOLDED BV GREEN TRACE SYMBOL IS EXACTLY [[0,A_N^VEE],[A_N,K_N]]. IT IS KREIN SELF-ADJOINT, NONDEGENERATE FOR BOTH NON-NULL CONORMAL ORBITS, COVARIANT UNDER THE RELATIVE GAMMA-NATURAL ANTILINEAR COFLIP, AND INDEPENDENT OF THE LOWER-ORDER EINSTEIN DEFORMATION. THE ABSOLUTE COFLIP PHASE CANCELS. THE KNOWN NONGAUGE NULL-SYMBOL CLASS REMAINS AN EXACT TRACE RADICAL. THIS IS A LOCAL FORMAL TRACE PACKET, NOT A GLOBAL CLOSED DOMAIN OR PHYSICAL QUOTIENT."
target_verdict: B5_CURVED_RELATIVE_COFLIP_AND_FORMAL_GREEN_TRACE_DESCEND
target_claim: internal target B5-COFLIP-GREEN-TRANSPORT-ON-CURVED-COMPLEX; verdict relative coflip covariance and complete formal Green trace constructed on the strict curved branch
canon_verdict_change: none
---

# B5 curved coflip and Green transport

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this result binds the repository-owned standard curved strict B5
Rarita--Schwinger BV complex on the actual complexified `(9,5)`
spinor/vector-spinor carrier. It transports the already-owned relative
Gamma-natural coflip and freezes the local formal Green trace of that action.
It is not Weinstein's unreleased cyclic two-connection complex, the current
graph-mixing Stage-B family, the K77 boundary campaign, a positive-Hilbert
realization, or a global physical state space.

```gu-typed-objects
result: the strict curved B5 BV Hessian has a complete relative-coflip-covariant formal Green trace whose off-null fold is nondegenerate and whose null trace retains the exact nongauge radical
carrier: U0=S rank128, U1=T*Y tensor S rank1792, U2=density dual rank1792, U3=S density dual rank128 LAYER=ambient CHIRALITY=S-FULL-DIRAC
pairing: program-native (9,5) invariant spinor Krein form, induced vector-spinor Krein form and canonical BV stage duality ON=independent-B5-curved-strict-carrier
real_structure: relative Gamma-natural antilinear coflip C_VS=(N eta) tensor C_perp; absolute phase is a nontrivial local-system trivialization and is not selected
grading: linear abelian BV ghost/field/antifield/Noether grading at local formal compact-core curved grade
action_owner: repository-construction quadratic curved Rarita--Schwinger action; historical source-preferred nonlinear action remains unowned
target: folded conormal Green trace, coflip covariance and characteristic radical MAP-TYPE=homomorphism
```

## Result first

For a conormal `n`, let

```text
(A_n epsilon)_mu = n_mu epsilon,
(K_n psi)^mu = gamma^{mu nu rho} n_nu psi_rho,
A_n^vee psi = n^mu psi_mu.
```

Order the folded input as `U0 plus U1` and its density dual as `U3 plus
U2`. The complete boundary coefficient of the strict BV Hessian is

```text
             [ 0    A_n^vee ]
B_n       =  [               ].
             [ A_n    K_n    ]
```

Under the invariant spinor Krein form, the induced vector-spinor form and
canonical BV stage duality,

```text
(A_n)^times = A_n^vee,
(K_n)^times = K_n,
B_n^times   = B_n.
```

The differential operator is formally anti-adjoint in the no-`i`
convention, so the compact-region Green identity is

```text
integral_Omega ( [D U,V] + [U,D V] )
  = integral_boundary [ B_n U,V ].
```

This supplies the program-native formal Green form of the assembled strict
curved branch rather than borrowing a boundary form from the distinct K77
operator.

## Non-null and null trace classes

At a positive unit conormal and at a negative unit conormal, the exact
Clifford certificate constructs a two-sided inverse for `B_n`. The
ghost/longitudinal pair is an invertible `2 by 2` stage block, while the
thirteen transverse vector-spinor directions use the exact inverse

```text
(1 - Gamma_sharp Gamma/(d-2)) gamma(n)^sharp.
```

Thus the folded trace is nondegenerate on both non-null conormal orbits. In
the middle block alone, `ker K_n=im A_n` off the null cone: its rank-128
radical is precisely the gauge conormal image, and the folded ghost term
pairs that radical nondegenerately.

For `n=e0+e9`, the prior transverse class

```text
psi_1 = gamma_2 c(n),
psi_2 = gamma_1 c(n)
```

is killed by both `K_n` and `A_n^vee` and is not in `im A_n`. It is therefore
an exact nongauge radical of the complete folded trace. Coflip/Green transport
does not repair null exactness or license a characteristic boundary domain.

## Relative coflip transport

Let `N=+1` on the four base directions and `N=-1` on the ten genuine
`Sym^2 T*X` fibre directions. The already-owned Gamma-natural coflip acts on
vector-spinors by

```text
C_VS = (N eta) tensor C_perp.
```

Writing `t=N eta`, exact Clifford-word reduction gives

```text
C_fold overline(B_n) C_fold^-1 = B_(t n).
```

The same identity holds arrow by arrow for `A_n`, `K_n` and `A_n^vee`.
Here `overline` is entrywise coefficient conjugation from the antilinear
coflip, not the Krein adjoint `times` used above.
Changing the local absolute trivialization `C_fold -> -C_fold` multiplies both
sides of every sesquilinear trace pairing twice and cancels. Therefore the
Green packet needs only the globally meaningful relative covariance and the
nontrivial local-system class; it does not select or store a globally
nonexistent ordered absolute coflip phase.

Two hostile plants are discriminating. The pairing-only vector extension
`eta tensor C_perp` fails the curved trace covariance, reproducing the known
provenance mixing. Flipping one relative vector phase also fails. The
Gamma-natural `N eta` factor is required.

For a boundary hypersurface, this is covariance from the trace at `n` to the
trace at `t n`. It becomes invariance only when the boundary/end data are
themselves preserved. No boundary geometry or domain is silently selected.

## Einstein deformation and real branches

The curved completion uses

```text
A_alpha = nabla + alpha gamma,
K_m     = gamma(3) nabla + m gamma(2),
m       = -(d-2)alpha,
alpha^2 = -kappa/4.
```

The `alpha` and `m` terms are order zero. They contribute no conormal symbol,
so the Ricci-flat massless branch and every minimally deformed Einstein
branch share exactly the same `B_n`. Curvature also enters only the bulk
Noether defect and not the boundary coefficient.

Because the coflip is antilinear, it sends `(alpha,m)` to their complex
conjugates. A real deformation branch is individually fixed. An imaginary
pair is exchanged and only the unordered pair descends without an additional
real-structure choice. The massless `alpha=m=0` branch is fixed.

## Preflight, route choice and controls

Mechanism-level retrieval covered the native principal lift, the Einstein
completion, the formal Green packet, the full-20 DeWitt-loop transport, the
five-field packet and the section-domain moduli. None had assembled the
folded curved conormal trace, proved its two non-null inverses, or transported
the relative coflip through the completed curved action.

The route council compared Clifford conormal identities, full 1792-matrix
construction, boundary-triple selection, maximal-isotropic fitting, global
ultrahyperbolic PDE analysis and source-action custody. The structural
conormal route dominates because it determines the complete formal trace and
its characteristic radical before any analytically open domain choice.

The exact probe passes `29/29`. It checks the three arrow adjoints, both
Noether compositions, the complete folded adjoint, exact positive- and
negative-normal inverses, the null nongauge radical, relative coflip
covariance, absolute-phase cancellation, lower-order independence, real and
imaginary deformation branches, and four adverse mutations.

## Boundaries and continuation

Strict field (ii) now transports through the curved action at relative formal
trace grade, and strict field (iv) is the explicit `B_n` above. Strict field
(iii) remains `ANTI-PRINCIPAL-SYMBOL / ACTION-CLOSED-EINSTEIN`. The separate
graph-mixing full-nine family remains `EXTERNAL-VIA-GRAM`, and the five-field
packet remains fail-closed.

No common ambient closed domain follows. The current result supplies the
algebraic trace input, but the noncompact ultrahyperbolic ambient operator
still lacks a source/action-owned boundary or end model, trace topology,
closed realization and coflip-preserved maximal-isotropic subspace. The exact
next owner is `B5-COMMON-AMBIENT-DOMAIN-ON-NAMED-END-MODEL`: freeze one
geometrically owned non-null boundary/end model, then construct a common
closed coflip-compatible domain or return the exact analytic obstruction.
