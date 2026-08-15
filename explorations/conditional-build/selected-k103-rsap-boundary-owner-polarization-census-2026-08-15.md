---
title: "Selected-K103 RSAP boundary-owner and polarization census"
status: active_research
doc_type: exact_conditional_presymplectic_boundary_route_census
created: "2026-08-15"
registry: lab/process/selected-k103-rsap-boundary-owner-polarization-census.json
probe: tests/channel-swings/selected_k103_rsap_boundary_owner_polarization_census_probe.py
grade: "THREE BOUNDARY ROUTES EXACTLY CLASSIFIED; ZERO-FLUX AND MULTIPLIER GIVE 98D BY REMOVING CHARGE; EDGE COMPLETION PRESERVES CHARGE AT 182D; PHYSICAL SELECTOR ABSENT"
target_claim: K102_NEXT_GATE__CURRENT_ACTION_OWNED_BOUNDARY_ROUTE_BOTH_ISOLATES_J_R_H_BAL_ZERO_AND_PRESERVES_LIVE_CHARGED_HORN
target_verdict: NO_AT_CURRENT_BOUNDARY_OWNERSHIP_GRADE__CONDITIONAL_ROUTE_TRILEMMA_EXACT
canon_verdict_change: none
---

# Selected-K103 RSAP boundary-owner and polarization census

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> boundary moment-map and reduction problem. Ordinary Higgs/VEV, family-index,
> net-chirality, anomaly, symmetry-breaking and familiar four-dimensional
> gauge-model conclusions do not substitute for Weinstein's objects. Read
> `lab/methods/source-native-comparator-routing.md` before importing them.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: SOURCE_NATIVE_ROUTE`

Scope: K102's conditional local `I1B` collar, the action-owned epsilon
preboundary parent, the externally supplied balanced seed `R_0`, and the
three explicit boundary completions below. This does not select a physical
time, global domain or boundary theory.

## Result first

The three remaining routes form an exact trilemma. None is a current
action-owned way to obtain the `98D` reverse RSAP while also retaining generic
right-`H_bal` endpoint charge in the same reduced phase space.

```text
route                         ambient/surface/rank/kernel/quotient
charged endpoint horn         182 / 182 / 182 /  0 / 182
zero h bulk flux -> lambda=0  182 / 140 /  98 / 42 /  98
minimal H_bal edge extension  224 / 224 / 182 / 42 / 182
edge plus extra lambda=0      224 / 182 /  98 / 84 /  98
K99 multiplier Dirac system   266 / 182 /  98 / 84 /  98
```

Rank and kernel are those of the pulled-back presymplectic form on the
displayed surface. For the multiplier route, the `84D` kernel contains the
`42` primary multiplier directions and the `42` right-`H_bal`
characteristics. On the original endpoint parent, the same route is the
`140D` zero level with `42D` characteristic distribution and `98D` quotient.

```text
zero-flux horn:       reaches 98D, but sets the h charge to zero;
edge horn:            preserves arbitrary h charge, but stays 182D;
explicit multiplier: reaches 98D, but is new action data and gauges the charge.
```

An edge extension reaches `98D` only after the additional restriction
`lambda_h=0`. That extra step is the zero-charge horn in new coordinates, not
a charge-preserving edge solution. The live charged horn remains a distinct
boundary theory, not a sector simultaneously contained in the `98D` quotient.

## Layer 0: objects that cannot be merged

| object | exact role | not the same as |
|---|---|---|
| source diagonal Gauss | `Div_varpi(Pi)_h-lambda_h=0` | endpoint zero level |
| zero-flux boundary condition | `Div_varpi(Pi)_h=0`, hence `lambda_h=0` on K102's constraint | source derivation of that condition |
| edge completion | makes diagonal boundary motion characteristic while storing charge in relative edge data | setting endpoint charge to zero |
| explicit multiplier | new `a_t in h_bal` whose Euler equation is `lambda_h=0` | an existing component of released `I1B` |

The balanced seed and right-gauge declaration remain conditional inputs. The
source physical `(1,3)|(6,4)` stabilizer has dimension `51`; it is not this
`42D` subgroup and would produce a different reduction.

## Route A: zero h bulk flux

K102 gives

```text
Div_varpi(Pi)_h-lambda_h=0.
```

Adding `Div_varpi(Pi)_h=0` implies `lambda_h=0`. On the `182D`
`T*Spin_0(7,7)` endpoint parent, the `42` independent moment constraints give
a `140D` coisotropic surface. Its pulled-back form has rank `98` and kernel
the `42D` right-`H_bal` orbit, so the characteristic quotient is `98D`.

This route is mathematically exact and physically unselected. The current
preboundary theorem instead says compactly supported transformations are
basic while unrestricted endpoint transformations carry a live moment map.
Neither the checked source nor the serialized action selects zero `h_bal`
bulk flux. Choosing it removes the generic charged endpoint states by design.

## Route B: minimal edge completion

Introduce one `H_bal` edge coordinate `u` and let endpoint and edge frames
transform diagonally. In local trivialization the `h` part of the extended
form is the direct 42-copy analogue of the already-built K77 edge cell:

```text
Omega_h,edge = delta lambda_h wedge delta(q_h-u).
```

Together with the `98D` complement block, the extended space has dimension
`182+42=224`, presymplectic rank `182`, and a `42D` diagonal characteristic
kernel. The quotient retains both `q_h-u` and `lambda_h`, so it is symplectic
`182D`. The edge field converts charged transformations into gauge by
relocating their charge into a gauge-invariant relative pair; it does not
erase the pair.

This proves why an edge completion preserves generic charge and why it cannot
be the standalone `98D` RSAP. Imposing `lambda_h=0` afterwards gives a `182D`
surface with rank `98`, kernel `84`, and quotient `98D`, but the added
condition reinstates the zero-charge horn. A scalar boundary counterterm
cannot change this because `delta^2 B=0` leaves the presymplectic form fixed.

## Route C: K99's explicit multiplier

K99's new term

```text
L_min=<lambda,g^-1 dot(g)-a_t>,  a_t in h_bal
```

imposes `lambda_h=0` and declares the right action gauge. On the endpoint
parent this is exactly the `182 -> 140 -> 98` reduction. In a full Dirac count,
add `42` coordinates `a_t` and `42` primary momenta `pi_a`:

```text
extended phase dimension:                    266
primary constraints pi_a=0:                   42
secondary constraints lambda_h=0:             42
joint constraint-surface dimension:           182
joint characteristic dimension:                84
physical quotient dimension:                   98
```

The construction is exact, regular and already has K98's irreducible BFV
completion. It is nevertheless new action data. K102 proved that the released
`I1B` owner is `varpi_n` for the distinct diagonal full-`G` constraint and
that `B(epsilon)_n` is an epsilon velocity, not this multiplier.

## Ownership verdict

There is no contradiction between the live horns:

- the charged horn keeps the `182D` endpoint cotangent phase space and treats
  unrestricted right-boundary motion as physical symmetry;
- the reverse RSAP horn adds a zero-flux condition or multiplier/gauge law and
  reduces to `98D`.

They are alternative boundary dispositions. A single phase space cannot both
retain freely varying `lambda_h` as physical charge and impose
`lambda_h=0`. Edge modes make the gauge alternative consistent, but do not
select the zero level or shrink it to `98D`.

```text
SOURCE-CONFIRMS:
  epsilon, varpi, T, I1B and the live unrestricted preboundary charge.

REPOSITORY-COMPOSES:
  the conditional balanced projection and exact three-route
  presymplectic/Dirac dimension census.

SOURCE-SILENT:
  zero h bulk flux, balanced edge completion, explicit balanced multiplier,
  gauge-versus-charge boundary disposition and physical polarization.
```

No ledger, datum, quotient booking, canon claim, public posture, W/mirror
choice, chirality or generation count changes.

## Hostile boundary

- `224-42=182`, not `98`: quotienting the minimal edge extension only removes
  the coordinates it added.
- `98D` after an edge extension requires another `42` constraints and their
  characteristics; here those are precisely the forbidden generic charges.
- Zero flux is not action-owned merely because it is compatible with the bulk
  equation; the multiplier is not current-source-owned merely because it is
  the unique minimal mathematical completion.
- None of these finite ranks constructs a global ultrahyperbolic Hamiltonian
  domain, analytic BFV complex, positive state space or physical spectrum.

## Next gate

The algebraic boundary census is closed. Do not repeat the three routes or
look for a fourth relabeling of existing variables. Reopen the `98D` physical
selection only on one of two genuinely new inputs:

1. a source/action-derived boundary variational principle or polarization
   whose Euler/Noether data selects zero `h_bal` flux and right gauge; or
2. an explicit source-owned balanced edge/multiplier term whose own boundary
   equations choose the zero-charge branch rather than merely making generic
   charge gauge-compatible.

Until then, retain the `182D` charged horn and the `98D` reverse RSAP as
distinct conditional boundary theories. Reproduce the exact ranks with:

```bash
python3 tests/channel-swings/selected_k103_rsap_boundary_owner_polarization_census_probe.py
```
