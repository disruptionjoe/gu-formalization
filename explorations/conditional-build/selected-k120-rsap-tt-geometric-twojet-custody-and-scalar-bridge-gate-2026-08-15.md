---
title: "Selected-K120 RSAP TT geometric two-jet custody and scalar-bridge gate"
status: active_research
doc_type: exact_source_coordinate_twojet_and_observed_scalar_normalization_obstruction
created: "2026-08-15"
registry: lab/process/selected-k120-rsap-tt-geometric-twojet-custody-and-scalar-bridge-gate.json
probe: tests/channel-swings/selected_k120_rsap_tt_geometric_twojet_custody_and_scalar_bridge_gate_probe.py
grade: "THE SOURCE-NATIVE COORDINATE CHANGE T=VARPI-B_LC(G) AND THE EXACT FIRST/SECOND SPIN-LEVI-CIVITA JETS INDEPENDENTLY FIX THE METRIC/DISTORTION PART OF AN I1B OBSERVED-TO-NATIVE TWO-JET. THEY DO NOT IDENTIFY THE OBSERVED I_SC SCALAR THETA WITH THE INVARIANT RADIAL COEFFICIENT OF T. THE RESULTING FAMILY F_LAMBDA HAS IDENTICAL TT LINEAR COLUMNS AND IDENTICAL NONLINEAR LEVI-CIVITA SECOND JET FOR EVERY NONZERO LAMBDA, WHILE ITS SCALAR COLUMN, RADIAL CUBIC AND PULLED PREBOUNDARY COLUMN SCALE WITH LAMBDA. NO CURRENT ACTION, PAIRING, STATIONARY BASE-POINT OR BOUNDARY OWNER SELECTS LAMBDA OR EQUATES THE TWO SCALAR ACTION LAYERS."
target_claim: K119_NEXT_GATE__THE_EXISTING_SOLDERING_OBSERVATION_PAIRING_AND_PREBOUNDARY_OWNERS_SELECT_A_COMPLETE_OBSERVED_TO_NATIVE_TWOJET_FOR_ONE_ACTION_LAYER
target_verdict: PARTIAL__I1B_TT_GEOMETRIC_JET_CUSTODY_CLOSES__OBSERVED_THETA_TO_NATIVE_RADIAL_SCALAR_BRIDGE_AND_NORMALIZATION_REMAIN_UNOWNED
canon_verdict_change: none
---

# Selected-K120 RSAP TT geometric two-jet custody and scalar-bridge gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> action-coordinate, soldering, observation, variational-pairing and
> preboundary question. Ordinary Higgs/VEV, family-index, net-chirality,
> anomaly, symmetry-breaking and familiar four-dimensional gauge-model
> constructions do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K119 required the missing field map to come from geometry rather than from a
fit to the desired cubic. K120 finds that the geometry really does supply most
of that map for the first action `I1B`.

The source variables are the metric `g` and an independent connection
`varpi`, while augmented torsion is

```text
T=varpi-B_LC(g).
```

Therefore the inverse coordinate change

```text
(g,T) -> (g,varpi=B_LC(g)+T)
```

has an action-owned first jet and a nonzero, symmetric second jet fixed by the
spin Levi-Civita connection. On the TT metric/distortion legs this is exactly
the independently derived map K119 requested. It is not a fitted completion.

But the observed scalar in `I_sc` and the invariant radial coordinate in
`I1B` are still different objects. Writing

```text
delta T=lambda theta Phi1+v V
```

exposes the remaining bridge coefficient `lambda`. Every nonzero `lambda`
gives the same metric/distortion columns and the same nonlinear
Levi-Civita second jet. Only the scalar column changes. The native action's
radial cubic and preboundary column consequently scale with `lambda`.

Neither stationarity, the observation receiver, the native pairing nor the
currently open boundary class equates this coefficient with the normalization
of the separately written scalar horn. Matching coefficients across those two
actions would be the cubic-fitting move K119 excluded.

Thus K120 is a partial closure: the TT geometric two-jet is owned for `I1B`,
but the three-field map is still conditional on one scalar bridge. K121 must
test that bridge directly from the two action normalizations, background map
and observation semantics before any cubic assembly.

## 1. Layer-0 packet

```text
observed carrier: E_obs=span(theta,h,v)
I1B source variables: (g,varpi)
geometric coordinates: (g,T), with T=varpi-B_LC(g)
metric TT representative: H
independent distortion TT representative: V
native invariant radial representative: Phi1
conditional scalar bridge: theta -> lambda theta Phi1
owned map data: DB_LC and D2B_LC, section/field observation cross jet
unowned equality: theta_Isc = normalized radial coordinate t_I1B
claim ceiling: local geometric two-jet custody plus one-dimensional bridge obstruction
```

The observed `2D` TT pencil and conditional `98D` RSAP/BFV carrier remain
different objects.

## 2. The independently owned `I1B` map family

At one named native base point `(g_*,T_*)`, define the local family

```text
g(theta,h,v)=g_*+h H,
T(theta,h,v)=T_*+lambda theta Phi1+v V,
varpi(theta,h,v)=B_LC(g_*+h H)+T(theta,h,v).           (1)
```

This is not an arbitrary ansatz for the TT legs. The source fixes
`T=varpi-B_LC(g)`, while the repository has independently constructed the
first and second symmetric-frame spin-Levi-Civita jets. Differentiating (1)
gives

```text
DF_lambda(theta)=(0,lambda Phi1),
DF_lambda(h)=(H,DB_LC[H]),
DF_lambda(v)=(0,V),                                    (2)

D2F_lambda(h,h)=(0,D2B_LC[H,H]),                       (3)
```

with the corresponding bilinear version for two distinct metric legs. The
pure observation-section second Frechet jet is zero because the complete germ
map is affine; its section--field cross jet is independently nonzero. Those
receiver terms compose after the native field is chosen and do not create the
missing scalar injection.

Equations (2)--(3) close the K120 geometric-custody demand on both TT legs.
They also show the precise limitation: every TT entry is independent of
`lambda`.

## 3. Exact finite-dimensional certificate

The exact local control keeps one coordinate for each typed direction. Let

```text
B(h)=b1 h+(b2/2)h^2,
F_lambda(theta,h,v)=(h,lambda theta,v+B(h)).            (4)
```

The Jacobian determinant is `-lambda`, so each nonzero `lambda` is a valid
local coordinate lift. Its `h` and `v` columns are independent of `lambda`,
and its only nonzero second derivative is

```text
D2F_lambda(h,h)=(0,0,b2),                              (5)
```

also independent of `lambda`. Two different nonzero values therefore agree
on every geometric TT datum in K120 while disagreeing on the scalar column.

For a native radial cubic written in the independent distortion coordinate
`u=w-B(g)`, 

```text
I_native=(c_h/2) r g^2+(c_v/2) r u^2,
```

the pullback coefficients are

```text
D3(I_native o F_lambda)[theta,h,h]=lambda c_h
D3(I_native o F_lambda)[theta,v,v]=lambda c_v.          (6)
```

The ratio is map-independent, but the common normalization is not. Fitting
`lambda` to either observed coefficient is not geometric ownership; it uses
the desired cubic as input.

## 4. Pairing and base-point tests do not close the bridge

The native radial quadratic form and observed scalar horn have schematic
coefficients

```text
I1B_rad=(k_rad/2)t^2+...,
I_sc=(kappa/2)theta^2+beta theta R+....                 (7)
```

Pullback gives `k_rad lambda^2 theta^2/2`. Equating it to the `I_sc` term
would impose

```text
lambda^2=kappa/k_rad.                                  (8)
```

Equation (8) is a conditional cross-action matching rule, not a consequence
of the Levi-Civita, soldering or observation maps. It also leaves a sign until
an oriented interaction owner is supplied. The source/repository has not
proved that the two quadratic terms are the same action term or observable.

The same issue survives at the background. An affine map can carry an
observed stationary value `theta_*` to the native radial stationary value
`t_*` for every nonzero slope `lambda`. Stationarity fixes the image point,
not the tangent normalization, exactly as K119 predicted.

## 5. Preboundary custody is likewise partial

For a native local potential

```text
Theta_native=p_g delta g+p_r delta t+p_w delta varpi_TT,
```

the pullback through (1) has coefficients

```text
theta: lambda p_r,
h:     p_g+(DB_LC[H]) p_w,
v:     p_w.                                            (9)
```

The TT soldered potential in (9) is owned by the existing Green/Cartan
construction. The scalar column still scales with `lambda`. Moreover the
selected action has a live unrestricted boundary moment map and no selected
physical boundary class. Boundary data therefore do not currently choose the
scalar bridge.

This does not prove that a future boundary variational principle cannot do
so. It proves that the presently owned preboundary packet does not.

## 6. Candidate action disposition

| candidate | K120 geometric custody | first missing datum |
| --- | --- | --- |
| `I_sc` | identity map on its observed `theta,g` fields | no native independent distortion `v` completion |
| `I1B` | source-coordinate TT `DF,D2F` exact through (1)--(3) | `theta_Isc` to normalized `Phi1` radial coefficient and common action/background identification |
| `I2B` | may reuse native source coordinates after its residual target is chosen | selected target pairing, scalar bridge and source-to-observer action equality |
| `I_II` | observer functional already lives after geometric restriction | typed pullback/equality to a source action and independent distortion leg |

No row owns the full three-field tuple. `I1B` is now strictly strongest: it
owns the TT geometry and misses one scalar bridge rather than an unspecified
map.

## 7. Reverse scaffold and next swings

```text
R0 known: observed theta-h-h and conditional native theta_rad-v-v projections
R1 exact: cubic fitting cannot select DF,D2F
R2 exact: I1B source-coordinate map owns both TT columns and D2B_LC
R3 exact: the owned TT jet is invariant under lambda!=0 scalar rescaling
R4 missing: identify theta_Isc with the normalized I1B radial coordinate
R5 then: pull back the selected pairing, cubic and preboundary coefficientwise
R6 later: unique pencil, spectral owner, domain and 2D-to-98D attachment
```

Next:

1. **K121:** scalar-bridge normalization and background-compatibility gate.
   Compare the action-owned quadratic forms, oriented cubic, stationary values
   and observation meaning of `theta` and the `Phi1` radial coefficient. End
   with a typed equality, an incompatibility, or an explicit conditional
   datum `lambda`.
2. **K122:** only after K121 selects the bridge, assemble the complete `I1B`
   pullback cubic and preboundary representative.
3. **K123:** only if one pencil results, test spectral ownership and the
   separately open domain/attachment gates.

No ledger, datum, quotient, canon, public posture, particle interpretation,
phenomenology or GU truth-status claim changes.

Exact probe: `35/35`.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k120_rsap_tt_geometric_twojet_custody_and_scalar_bridge_gate_probe.py
```
