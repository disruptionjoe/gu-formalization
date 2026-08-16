---
title: "Selected-K119 RSAP TT stationary two-jet selection obstruction"
status: active_research
doc_type: exact_stationary_pullback_identifiability_and_geometric_jet_custody_gate
created: "2026-08-15"
registry: lab/process/selected-k119-rsap-tt-stationary-twojet-selection-obstruction.json
probe: tests/channel-swings/selected_k119_rsap_tt_stationary_twojet_selection_obstruction_probe.py
grade: "EXACT FINITE-DIMENSIONAL PULLBACK THEOREM AND CURRENT OWNER CENSUS. AT A STATIONARY BASE POINT, STATIONARITY CONSTRAINS NEITHER DF NOR D2F. FOR A NONDEGENERATE PRIMITIVE HESSIAN ON THE THREE-FIELD CARRIER, THE SECOND-MAP-JET CONTRIBUTION SURJECTS ONTO ALL TEN SYMMETRIC CUBIC COEFFICIENTS AND HAS AN EIGHT-DIMENSIONAL KERNEL. EVEN THE AFFINE DIAGONAL LIFT RETAINS A ONE-DIMENSIONAL SCALAR/TT RESCALING ORBIT AFTER BOTH KNOWN DIAGONAL PROJECTIONS ARE MATCHED. CUBIC AGREEMENT THEREFORE CANNOT SELECT I_SC, I1B, I2B OR I_II UNLESS THE GEOMETRIC TWO-JET IS OWNED INDEPENDENTLY."
target_claim: K118_NEXT_GATE__STATIONARITY_OR_CUBIC_MATCHING_CAN_SELECT_ONE_ACTION_LAYER_AND_SCALAR_LIFT_WITHOUT_AN_INDEPENDENTLY_DERIVED_OBSERVED_TO_NATIVE_TWO_JET
target_verdict: NO__STATIONARITY_IS_JET_BLIND_AND_A_FREE_SECOND_MAP_JET_CAN_MANUFACTURE_AN_ARBITRARY_CUBIC_MATCH_ON_THE_NONDEGENERATE_BRANCH
canon_verdict_change: none
---

# Selected-K119 RSAP TT stationary two-jet selection obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K118 correctly required a stationary observed-to-native two-jet before
assembling a moving cubic. K119 shows that the word *stationary* does not
select that jet, and that fitting the jet to the desired cubic would be
mathematically empty.

At a stationary native background `x_*`, every map `F` with `F(0)=x_*` makes
the pullback stationary:

```text
D(I o F)(0)=DI(x_*) DF(0)=0.
```

So stationarity places no condition on either `DF` or `D2F`. More strongly,
when the primitive Hessian is nondegenerate, the `D2F` term in the pullback
cubic can reproduce *any* symmetric cubic on the three observed fields. A
full cubic match then has no action-selection force unless the map jet was
derived independently from the actual observation/soldering geometry.

Even under the much stronger restriction `D2F=0` and a diagonal linear lift,
the two known `theta-h-h` and conditional `theta-v-v` projections leave a
continuous rescaling orbit. Thus neither stationarity, the diagonal data, nor
an unconstrained complete cubic match selects `I_sc`, `I1B`, `I2B`, or
`I_II`.

This is a scoped selection obstruction, not a nonexistence theorem. The
repository already owns locations for genuine first and second soldering and
observation jets. K120 must derive and compose those geometric jets for one
named action layer *without using the desired cubic as fitting data*.

## 1. Layer-0 packet

```text
observed carrier: E=span(theta,h,v), dim E=3
primitive carrier: V=fields(I) at a named native base point x_*
linear lift: L=DF_0:E->V
quadratic lift: Q=D2F_0:Sym^2(E)->V
primitive data: H=D2I_x*, C=D3I_x*
observed cubic: C_obs=D3(I o F)_0
selection owner: (I,x_*,L,Q,target pairing,preboundary representative)
claim ceiling: local identifiability and present serialized custody only
```

`I_sc`, `I1B`, `I2B`, and `I_II` remain distinct. The conditional `2D` TT
pencil and `98D` RSAP/BFV carrier remain different objects.

## 2. Stationarity is blind to the map jet

For `F(0)=x_*`, the first three pullback derivatives are

```text
D(I o F)       = DI[L-],
D2(I o F)      = D2I[L-,L-] + DI[Q(-,-)],
D3(I o F)      = C[L-,L-,L-]
                  + H[Q(-,-),L-] + cyclic
                  + DI[D3F(-,-,-)].                    (1)
```

At `DI(x_*)=0`, the last terms in all three lines vanish. This proves two
facts often conflated in the inherited gate:

1. the pullback is stationary for every `L,Q`; and
2. the cubic still depends on `Q` through the Hessian.

Stationarity removes `D3F`; it does not determine `DF` or `D2F`.

## 3. Complete second-jet image theorem

Freeze a three-dimensional native slice containing the image of an invertible
`L`, and assume the restriction of `H` to that slice is nondegenerate. Absorb
them into coordinates, so `L=1` and `H` is the identity pairing. The part of
(1) controlled by the quadratic map jet is

```text
T(Q)(u,v,w)=<Q(u,v),w>+<Q(u,w),v>+<Q(v,w),u>.          (2)
```

For every symmetric cubic `S`, choose

```text
<Q_S(u,v),w> = (1/3) S(u,v,w).                         (3)
```

Then `T(Q_S)=S`. Therefore

```text
T: Hom(Sym^2 E,E) -> Sym^3 E*  is surjective.
```

For `dim E=3`, the domain has dimension `18` and the target dimension `10`.
The exact coefficient matrix has rank `10` and kernel dimension `8`.
Consequences:

- any difference between a primitive cubic and a desired observed cubic can
  be manufactured by a fitted `D2F`;
- even after the full observed cubic is fixed, eight quadratic-jet directions
  remain invisible to it; and
- cubic agreement tests an action layer only after `Q` is independently
  owned.

If the relevant Hessian is degenerate, the image can have a nonzero
cokernel. That cokernel may carry map-independent cubic information. K119
does not assume the unselected full moving Hessian or its selected
three-dimensional image is nondegenerate. It gives the exact branch rule:
compute the selected `H,L` first, then either use its cokernel or accept the
surjective obstruction.

## 4. Affine diagonal scalar-lift obstruction

Set `Q=0` and take the strongest simple lift

```text
theta_native=lambda theta,   h_native=a h,   v_native=b v.
```

The two granted diagonal projections depend on

```text
p_h=lambda a^2 c_h,          p_v=lambda b^2 c_v.       (4)
```

At a nonzero control point, the Jacobian of `(lambda a^2,lambda b^2)` has
rank two in the three variables `(lambda,a,b)`. Its tangent kernel is the
rescaling direction

```text
(delta lambda,delta a,delta b)=(-2,1,1).                (5)
```

Thus both known projections still leave one continuous lift orbit before any
mixed linear entries or quadratic jets are restored. Calling `theta` and
`theta_rad` the same symbol would choose a representative of this orbit; it
would not derive one.

## 5. Current owner census

The required selection tuple is

```text
(primitive action, stationary base point, independently derived DF,
 independently derived D2F, target pairing/preboundary owner).
```

| candidate | owned part | first missing selection datum |
| --- | --- | --- |
| `I_sc` | observed `theta-h-h` kinetic response | native `h-v` action completion and map |
| `I1B` | primitive transgression and intrinsic radial cubic summand | observed scalar identification and composed geometric `j2F` |
| `I2B` | residual-square grammar and scoped stationary native witnesses | selected residual target/pairing plus observed `j2F` and cubic |
| `I_II` | observer extrinsic functional and Gauss/Weyl/Bach route | typed equality or pullback from either source action layer |

No row currently owns the complete tuple. The existing local stationary
`I2B` connection two-jet solves a native Euler equation at one base point; it
is not the map jet from `(theta,h,v)` into the native fields. The exact first
and second soldering/observation artifacts locate candidate geometric owners,
but their selected-action coefficient composition remains open.

## 6. Reverse scaffold and next gates

```text
R0 known: observed theta-h-h response and conditional intrinsic theta_rad-v-v summand
R1 exact: stationarity selects neither DF nor D2F
R2 exact: free D2F has full cubic image on a nondegenerate three-field branch
R3 exact: affine diagonal matching retains a one-dimensional rescaling orbit
R4 missing: select I and x_* from action truth
R5 missing: derive DF,D2F from observation/soldering geometry independently
R6 then: compute D3(I o F), its preboundary representative and any cokernel invariant
R7 later: unique pencil, spectral owner, domain and 2D-to-98D attachment
```

K120 is therefore a geometric jet-custody gate, not a cubic-fitting gate. It
must compose the already located spin-Levi-Civita, soldering, section and
observation jets into one selected action and state the base point, carrier,
pairing and boundary representative. K121 may assemble the full cubic only
after that. K122 spectral ownership and K123 stationarity/domain/attachment
remain conditional.

No ledger, datum, quotient, canon, public posture, particle interpretation,
phenomenology or GU truth-status claim changes.

## K120 successor closure — 2026-08-15

K120 independently derives the `I1B` TT map jet from the source-coordinate
identity `T=varpi-B_LC(g)`: both TT columns and the nonlinear
spin-Levi-Civita second jet are owned without cubic fitting. The complete
three-field map still fails selection for one precise reason. The observed
`I_sc` scalar may enter the invariant `Phi1` radial line with any nonzero
slope `lambda`; the owned TT jet is unchanged, while the native scalar cubic
and preboundary column scale with `lambda`. K121 must compare the two action
normalizations, backgrounds and observation semantics before assembly.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k119_rsap_tt_stationary_twojet_selection_obstruction_probe.py
```
