---
title: "Eric-lane native equation replacement contract"
status: active_research
doc_type: specification
created: 2026-07-31
branch: agent/weinstein-guided-source-action
run: archived private execution record
---

# Eric-native equation replacement contract

## 1. Replacement is an intertwining theorem

A familiar equation is not replaced by giving a native field the same name.
For each physical component `i`, the construction must supply:

```text
native field carrier F_Y
native Euler covector E_Y
stationary background phi_bar
observation lift L_i and extraction R_i
equation-dual map L_i^!
closed common domain D_i
symmetry/Noether map
observable comparison map O_i
parameter and datum debit
```

If the effective action is

\[
I_i^{\rm eff}[\phi_i]=I_Y[\mathcal L_i\phi_i],
\]

then its Euler covector is

\[
E_i^{\rm eff}
=(D\mathcal L_i)^!E_Y.
\]

A standard equation `E_i^std=0` is an earned low-energy shadow only if, on a
declared domain and modulo a declared field redefinition/irrelevant remainder,

\[
E_i^{\rm std}
=Z_i\,\mathcal P_i(D\mathcal L_i)^!E_Y
+\mathcal O(M_i^{-1}),
\]

with `Z_i`, `P_i`, and `M_i` determined before observational scoring. Equality
of carriers, representation dimensions, or principal symbols alone is not a
replacement.

## 2. Native parent currently available

The Eric lane's built bosonic parent is

\[
B=A_{\rm LC}(\epsilon_{\rm red},g_{\rm DW}),
\qquad T=A-B,
\]

\[
I_{G2}
=\int_YT\wedge\mathscr S_\epsilon
\left(F_B+\frac12D_BT+\frac13q(T,T)\right)
+\frac{\kappa_1}{2}\int_YT\wedge\flat_1T.
\]

Its exact connection/distortion equation is

\[
E_A=E_T,
\]

\[
E_T
=\mathscr S_\epsilon(F_B)
+\frac12(L+L^!)T
+M_\epsilon(T,T)
+\kappa_1\flat_1T.
\]

The familiar-looking compressed expression
`S(F_(B+T))+kappa T` is killed for the native map and may not be reintroduced.
The reduction and metric equations are the graph returns

\[
E_\epsilon
=(D_\epsilon B)^!(E_B^\circ-E_T)
+(D_\epsilon\mathscr S)^!E_{\mathscr S}
+(D_\epsilon\flat_1)^!E_\flat,
\]

and the analogous `E_g`. G3 also supplies the coupled Ward identity,
preboundary potential, presymplectic current, and ordinary-gauge minimal BV
completion through antifield number one.

## 3. Observation contract

Every four-dimensional equation row is gated by

\[
\mathcal R_s\mathcal L_s=1,
\qquad
\mathcal R_sD_Y\mathcal L_s=D_X,
\qquad
(1-\mathcal L_s\mathcal R_s)D_Y\mathcal L_s=0,
\]

plus `(D L_s)^!` on Euler covectors, a closed right-quaternionic Krein domain,
a positive majorant, and the quotient of the action-derived preboundary
kernel. Ordinary differential-form pullback is not the equation-dual map.

## 4. Status vocabulary

| status | meaning |
| --- | --- |
| `BUILT_NATIVE_PARENT` | field, action, and Euler/identity exist on `Y` |
| `BUILT_IDENTITY_ONLY` | kinematic/Bianchi/Noether identity exists, not dynamics |
| `CANDIDATE_SHADOW` | native carrier/equation exists but observation/reduction comparison is unproved |
| `CANDIDATE_PARENT` | possible native physical carrier exists without complete Euler dynamics |
| `NATIVE_CARRIER_ONLY` | representation/bundle exists, no native physical equation |
| `PARTIAL_BV` | classical symmetry resolution exists only for the stated subalgebra/order |
| `DOWNSTREAM_TEST` | consistency/readout requirement, not an equation to replace |

No row may terminate at “source action or external datum missing.” A missing
arrow becomes a bounded construction or kill. Finite external data are carried
as a family parameter through the equations and consumed only at their typed
domain/index/orientation map.

## 5. No-stall rules

1. Use `I_G2` and its G3 Euler packet as the bosonic backbone; do not restart
   from an empty action ledger.
2. Add a term only if it survives G3.5's target-blind naturality enumeration
   or is explicitly labeled a comparator.
3. Construct G4 observation/domain maps before naming four-dimensional modes.
4. Compute one stationary reduced Hessian before separately fitting photon,
   gravity, Higgs, or dark-energy sectors.
5. Derive matter currents from the same frozen action used for fermion
   propagation.
6. Carry P1/P2/P3 across every branch without using them to select an action,
   background, projector, or Standard Model representation.
7. If a conventional equation appears only when its dedicated comparator term
   is restored, record `SUPPLIED`, not `EMERGENT`, and continue with the
   conditional family rather than declaring the whole construction stalled.

## Boundary

This contract supplies comparison criteria and a build order. It does not
claim that Maxwell, Yang--Mills, Dirac, Einstein, Higgs/Yukawa, cosmology,
anomaly freedom, or three generations have been recovered.
