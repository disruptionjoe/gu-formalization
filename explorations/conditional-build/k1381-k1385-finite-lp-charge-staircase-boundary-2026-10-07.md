---
title: "K1381--K1385 finite-Lp charge-staircase boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-07"
updated_at: "2026-10-07"
---

# K1381--K1385 finite-`Lp` charge-staircase boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only because this packet tests the
maximal-compact analytic route left uncertain by SC-META-53. The compact
circle, charge operator, scalar-electrodynamics action and every mixed
charge--Sobolev topology below are repository constructions. They do not
identify a source-selected reduction, observed charge assignment or source
observation map.

Scope: the sharp bare-Hölder cost of replacing K1378's electric
`L-infinity_x` coefficient by finite `L^p_x`, an exact diagonal-mode
obstruction, the conditional mixed-staircase repair, and a finite-rectangle
nonclosure theorem for that proof method. No null-form exclusion, global
coupled evolution, nonlinear KT resolution, proper BV-BFV quotient,
quantization or GU physical cohomology is constructed.

```gu-typed-objects
result: sharp finite-Lp charge-spatial trade, diagonal mixed-norm obstruction, conditional staircase estimate and finite rectangular hierarchy nonclosure
carrier: scalar-electrodynamics phase data on T3 with unbounded self-adjoint integer Q and charge-lift variables psi_n=Q^n phi LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive nth charge-lift graph energy plus mixed Sobolev norms ON=repository_owned_control
real_structure: complex Hilbert charge representation with self-adjoint Q and real Abelian gauge field
grading: spatial Fourier momentum, integer compact charge, charge-lift order and BRST ghost degree
action_owner: repository-construction -- the mixed staircase is an analytic estimate, not a source action term
target: SC-META-53 conditional nonlinear propagation boundary MAP-TYPE=restriction
```

## Preflight bookend

K1378 closes the first charge lift if the electric field and radial
coefficient derivative are time-integrable in `L-infinity_x`; K1379 proves
that the base energy does not provide those endpoint norms. The cheapest
candidate weakening is finite spatial `L^p`, before attempting a full
Strichartz or null-form theorem. The key question is whether Hölder closes on
the same lifted energy or silently spends a higher mixed charge--spatial norm.

The source/action-owned selector remains the strongest independent challenger,
but no released source datum fixes the compact generator, normalization or
observed carrier. The finite-`p` calculation is exact, reusable and directly
tests the most immediate dispersive escape left by K1380.

## K1381 — finite `p` has a sharp mixed charge--spatial price

For the `n`th charge lift `psi_n=Q^n phi`, the electric exchange is

```text
j_n=e Im<Q psi_n,D psi_n>
   =e Im<Q^(n+1)phi,D Q^n phi>.
```

For `3<=p<=infinity`, set

```text
r_p=2p/(p-2),              sigma_p=3/p,
```

with `r_infinity=2` and `sigma_infinity=0`. Hölder and the sharp three-
dimensional Sobolev line give

```text
|integral E.j_n|
 <= |e| ||E||_p ||Q^(n+1)phi||_(r_p) ||D Q^n phi||_2
 <= C_p |e| ||E||_p ||Q^(n+1)phi||_(H^(sigma_p))
                    ||D Q^n phi||_2.
```

At `p=infinity`, the demanded matter factor is exactly the
`||Q^(n+1)phi||_2` term already supplied by the positive `mu Q^2`
regularizer in the `n`th lifted energy. Every finite `p` has
`sigma_p>0` and therefore demands spatial regularity of the next charge level.
The radial term is cheaper:

```text
|integral partial_t f |psi_n|^2|
 <= ||partial_t f||_p ||psi_n||_(2p/(p-1))^2,
```

and `H^1` control of `psi_n` already supplies that exponent for `p>=3`.
Thus the finite-`p` loss is specific to the charged electric current in this
bare Hölder argument.

## K1382 — the existing lifted energy cannot pay that price

Let `e_(4N)` be an actual K1358 charge eigenvector with
`Qe_(4N)=4N e_(4N)`, choose spatial frequency `k_N=(4N,0,0)`, set
`q_N=4N`, and define

```text
phi_N=a_N exp(i k_N.x)e_(q_N),
a_N=q_N^(-n)(N^2+q_N^2)^(-1/2).
```

Then the two load-bearing pieces of the `n`th lifted energy obey

```text
||grad Q^n phi_N||_2^2+||Q^(n+1)phi_N||_2^2=1
```

up to the fixed Fourier normalization, while

```text
||Q^(n+1)phi_N||_(H^(sigma_p))
 = q_N (1+|k_N|^2)^(sigma_p/2)/(|k_N|^2+q_N^2)^(1/2)
 = (1+(4N)^2)^(sigma_p/2)/sqrt(2)
 ~ (4N)^(sigma_p)/sqrt(2).
```

This diverges for every finite `p`. Consequently there is no constant
bounding K1381's demanded mixed norm by the same `n`th lifted energy. The
obstruction couples high charge and high spatial frequency; a fixed-charge or
fixed-frequency test misses it.

## K1383 — the exact conditional mixed staircase

If the missing norm is supplied independently, the electric exchange closes
at that step:

```text
|integral E.j_n|
 <= C_p |e| ||E||_p M_(n,p) E_n^(1/2),
M_(n,p)=||Q^(n+1)phi||_(H^(3/p)).
```

Together with the cheaper radial term,

```text
dE_n/dt
 <= C_p |e| ||E||_p M_(n,p) E_n^(1/2)
    +C_p ||partial_t f||_p E_n.
```

Equivalently, wherever `E_n>0`,

```text
d sqrt(E_n)/dt
 <= C_p |e| ||E||_p M_(n,p)
    +C_p ||partial_t f||_p sqrt(E_n).
```

Hence `E_n` propagates on every interval on which
`||E||_p M_(n,p)` and `||partial_t f||_p` are time-integrable. This is an
exact conditional repair. It does not derive `M_(n,p)`, conserve an augmented
hierarchy or prove global existence.

## K1384 — finite rectangular hierarchies do not close bare Hölder

Suppose one controls only finitely many rectangular norms
`H^s_x D(Q^m)` with `s<=S` and `m<=N`. Applying the finite-`p` estimate at
the top charge/spatial corner asks for

```text
H^(S+3/p)_x D(Q^(N+1)),
```

which lies outside the rectangle for every finite `p`. The K1382 diagonal
modes make this failure quantitative. Increasing either finite ceiling merely
moves the exposed corner; it does not close the bare-Hölder induction.

This theorem is deliberately method-relative. A null-form cancellation,
covariant spacetime estimate, diagonal anisotropic weight with a proved
closed energy identity, or summable infinite analytic/Gevrey hierarchy could
avoid the rectangular staircase. None is constructed or excluded here.

## K1385 — admission replay

The bridge census now has 57 rows: 36 satisfied, six conditional, eleven
excluded and four missing. The sharp finite-`p` trade and diagonal obstruction
are satisfied results; propagation with an independently controlled mixed
staircase norm is conditional; and closure of the same lifted energy or any
finite rectangular hierarchy by bare finite-`p` Hölder is excluded.

The same four source/physical rows remain missing: source-owned selection and
normalization; identification with one source action; a closed fully coupled
global nonlinear BV-BFV quotient with positive physical Hilbert cohomology;
and a source-owned observed-state/export map. K1145/K1150 remain `0/7`.

## Postflight hostile review

The strongest overclaim is that finite-`p` dispersive closure is impossible.
Only closure by the displayed bare Hölder/Sobolev route on the same or any
finite rectangular hierarchy is excluded. The strongest contrary control is
the endpoint `p=infinity`, where `sigma_p=0` and the positive charge
regularizer supplies the exact next-charge `L2` factor. The weakest seam is a
possible null form, covariant Strichartz estimate or summable anisotropic
hierarchy that couples charge and spatial regularity without exposing a top
corner.

The staircase is not attributed to the source and selects neither `Q`, its
sign, primitive normalization nor observed semantics. No source, ledger,
canon, paper, prediction, confirmation or public posture moves.

## Exact next input

Construct a genuinely closed alternative to the finite rectangular bare-
Hölder hierarchy: an action-compatible null-form/covariant spacetime estimate,
a conserved or controlled diagonal charge--spatial weight, or a summable
infinite hierarchy with a global bound. Only then attempt closed nonlinear KT
properness and the positive BV-BFV quotient. Independently, a source/action-
owned observed-carrier selector must fix the generator and normalization and
preserve the same domain.
