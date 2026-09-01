---
title: "K77 source-transgression affine-bridge obstruction wave"
status: active_research
doc_type: reverse_scaffold_source_to_observed_affine_bridge_obstruction
date: 2026-09-01
claim_ceiling: exact obstruction to identifying the source-native cubic I1B augmented-torsion transgression with the repository-owned even quartic rank-1920 quotient action through any field-independent affine one-mode bridge; no obstruction to nonlinear, nonlocal, background-dependent, orbit-averaged or later-action bridges and no GU verdict
manifest: lab/process/k77-source-transgression-affine-bridge-obstruction-wave.json
probe: tests/channel-swings/k77_source_transgression_affine_bridge_obstruction_probe.py
---

# K77 source-transgression affine-bridge obstruction wave

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
result: affine-bridge degree and parity obstruction between the source-native I1B transgression ray and the repository-owned interacting rank-1920 quotient ray
carrier: one real augmented-torsion ray and one real one-mode ray inside the rank-960 observed quotient W LAYER=conditional CHIRALITY=N/A
pairing: source Shiab/Hodge action pairing on the first ray and transported positive H pairing on the second ON=typed_action_germ_comparison
real_structure: real affine bridge parameter and real polynomial action germs
grading: polynomial field degree only; not a BRST, BV-BFV or physical particle grading
action_owner: source owns the I1B transgression grammar and coefficients; GU repository owns the rank-1920 quotient family; no source-to-observed bridge is attributed
target: equality of action germs under a field-independent affine one-mode bridge MAP-TYPE=obstruction
```

## The first source coefficient packet reaches the observed family

The source-native first I1B action has the displayed augmented-torsion form

```text
I1B = <T,S(F_B+(1/2)D_B T+(1/3)[T,T])>
      +(kappa_1/2)<T,*T>.                              (1)
```

Earlier source custody and exact cyclic controls already establish the role
of `1/2` and `1/3`: on a fixed typed ray `T=t tau`, variation produces unit
weights because `d(t^2/2)/dt=t` and `d(t^3/3)/dt=t^2`. This packet does not
reclaim that result as new. It asks whether (1) can be the missing selector for
the complete repository-owned observed family

```text
S_(m2,lambda)(q)=m2 q^2/2+lambda q^4/4,
m2>0, lambda>=0,                                    (2)
```

through the cheapest source-to-observed identification: a field-independent
affine one-mode bridge `T=T0+s q`, `s!=0`.

## Exact affine-bridge obstruction

Restrict (1) to any affine ray. It is a polynomial of degree at most three in
`q`, because its highest source term is cubic in `T`. Equation (2) has degree
four whenever `lambda>0`. Therefore

```text
I1B(T0+s q) = S_(m2,lambda)(q) for every q
implies lambda=0.                                    (3)
```

At the origin-preserving bridge `T=s q tau`, write the source ray data as

```text
f=<tau,S(F_B)>,
c=<tau,S(D_B tau)>+kappa_1<tau,*tau>,
e=<tau,S([tau,tau])>.
```

After absorbing the nonzero bridge scale into `(f,c,e)`, the source and
observed Euler polynomials are

```text
E_src(q)=f+c q+e q^2,
E_obs(q)=m2 q+lambda q^3.                             (4)
```

Coefficient equality in (4) is possible only when

```text
f=0, e=0, lambda=0, c=m2.                            (5)
```

Thus every genuinely interacting member `lambda>0` is excluded from being a
literal affine reduction of the cubic source transgression, and a nonzero
quadratic eddy response `e` is independently incompatible with the even
observed Euler parity. This is a bridge-class obstruction. It does not exclude
either action on its own.

The conclusion is invariant under every nonzero rescaling of the affine
bridge. Scaling changes coefficients but cannot turn a cubic polynomial into
a quartic one or an even-power Euler term into an odd-power one.

## What survives

The source term has decision power: it kills the tempting literal or affine
identification of the two complete packets. It does **not** choose a point
inside `(m2,lambda)`. A viable source-to-observed route must add at least one
typed structure that is absent from the affine comparison:

- a nonlinear bridge whose substitution can generate degree four;
- a later source-owned square-of-eddy or curvature-square action term;
- background/orbit data whose integration changes the effective polynomial;
- a nonlocal reduction; or
- a cancellation/quotient identity derived on the full carrier.

Merely copying `1/3` into `lambda` is invalid. The coefficients belong to
different typed monomials, pairings and action owners. The exact probe passes
its structural checks and its hostile selftest rejects coefficient mutation,
degree laundering, source promotion and widening beyond the affine class.

## Next condition

The observed selector gate is now a typed bridge problem rather than a request
for any source coefficient. Reopen the source-action route only with a
source/action-owned nonlinear map or later action term from augmented torsion
to the rank-1920 quotient whose pulled-back quartic, cubic, kinetic and pairing
coefficients can all be compared. Until then the interacting family remains a
repository-owned reverse-scaffold family, not a source reduction.
