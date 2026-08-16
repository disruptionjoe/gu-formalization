---
title: "Selected-K118 RSAP TT full-moving D3 owner sufficiency and action-layer gate"
status: active_research
doc_type: exact_owner_sufficiency_action_layer_and_observed_to_native_two_jet_gate
created: "2026-08-15"
registry: lab/process/selected-k118-rsap-tt-full-moving-d3-owner-sufficiency-and-action-layer-gate.json
probe: tests/channel-swings/selected_k118_rsap_tt_full_moving_d3_owner_sufficiency_and_action_layer_gate_probe.py
grade: "THE REQUESTED FULL MOVING D3 I_SELECTED IS NOT YET A SINGLE TYPED REPOSITORY OBJECT. THE OBSERVED SCALAR HORN, FIRST ACTION I1B, RESIDUAL-SQUARE I2B, AND OBSERVER NORM-II-SQUARED FUNCTIONAL HAVE DISTINCT OWNERS AND NO ESTABLISHED THIRD-DERIVATIVE IDENTIFICATION. EVEN GRANTING BOTH THE OWNED HH KINETIC RESPONSE AND THE CONDITIONAL INTRINSIC VV CUBIC RESPONSE LEAVES AT LEAST FOUR FIRST-ORDER PENCIL COEFFICIENTS FREE; EXACT DIRECT AND FIELD-REDEFINITION COMPLETIONS SHARE BOTH KNOWN PROJECTIONS BUT HAVE DIFFERENT SPECTRAL RESPONSE. THE NEXT OWNER IS A SINGLE ACTION-LAYER SELECTION PLUS A STATIONARY OBSERVED-TO-NATIVE TWO-JET MAP, NOT ANOTHER GUESSED PENCIL."
target_claim: K117_NEXT_GATE__THE_EXISTING_OWNER_PACKETS_CAN_BE_ASSEMBLED_DIRECTLY_INTO_ONE_FULL_MOVING_D3_I_SELECTED_AND_UNIQUE_TWO_FIELD_PENCIL
target_verdict: NO__ACTION_LAYER_AND_SCALAR_LIFT_ARE_UNSELECTED__KNOWN_DIAGONAL_PROJECTIONS_LEAVE_A_FOUR_PARAMETER_FIRST_ORDER_PENCIL_FAMILY
canon_verdict_change: none
---

# Selected-K118 RSAP TT full-moving D3 owner sufficiency and action-layer gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> action-layer, observation-lift, variational-jet and Krein-pencil question.
> Ordinary Higgs/VEV, family-index, net-chirality, anomaly, symmetry-breaking
> and familiar four-dimensional gauge-model constructions do not adjudicate
> it. Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K117 correctly moved the next gate to the full moving third derivative. K118
finds that the repository still names that target one layer too late.

There is no single object presently typed as `I_selected` whose third
derivative can simply be assembled. Four different functionals are in play:

1. the observed scalar horn `I_sc`, which owns the kinetic `theta-h-h`
   projection;
2. the first transgression action `I1B`, whose intrinsic augmented-torsion
   cubic owns a conditional radial-`v-v` projection;
3. the residual-square second action `I2B`; and
4. the observer extrinsic functional `I_II=||II||^2`.

The repository has already proved that these action layers cannot be merged
by verbal similarity. It has not selected an identification of the observed
scalar `theta` with the invariant radial `theta_rad`, nor a stationary
two-jet map carrying `(theta,h,v)` into one chosen primitive action.

This is not only a documentation gap. Even if we grant both diagonal pieces—
the owned kinetic `hh` response and the conditional intrinsic `vv` response—
the first-order symmetric pencil still has four undetermined coefficients.
Two exact completions share both granted projections. One moves the spectral
gap; the other is a field redefinition and is isospectral. Therefore no
unique full moving pencil, spectral connection or action-owner test follows.

The next swing must select one action layer and construct the stationary
observed-to-native two-jet map. Only then is a coefficientwise `D3` pullback
well typed.

## 1. Layer-0 owner packet

```text
observed carrier: E_obs=span(theta,h,v) on one TT polarization
native candidates: fields of I_sc, I1B, I2B, and I_II
known projection: D3 I_sc[theta,h,h] = d z
conditional projection: D3 I1B[theta_rad,v,v] = s
unselected identification: theta <-> theta_rad
missing map: stationary two-jet j2 F:E_obs -> fields(I_chosen)
target: D3(I_chosen o F), including its Green/preboundary representative
controls: direct completion, congruence/field-redefinition completion,
          nonstationary pullback, residual-square cubic
claim ceiling: exact owner insufficiency and minimum-interface theorem
```

The observed `2D` TT pencil and conditional `98D` RSAP/BFV carrier remain
different objects.

## 2. Four action layers, not one cubic

The existing action-layer retype gives the exact custody table:

| layer | owned object | relevant exact result | missing identification |
| --- | --- | --- | --- |
| `I_sc` | observed scalar/metric horn | `delta J_hh(z)=d z E_hh` | full native `h-v` completion |
| `I1B` | first transgression action in connection distortion | intrinsic `D3[theta_rad,q0,qm]=0`, `D3[theta_rad,qm,qm]` nonzero | `theta=theta_rad`, moving geometry and observation pullback |
| `I2B` | `1/2 <Upsilon_B,Q_B Upsilon_B>` | at residual zero, Hessian `DUpsilon^! Q_B DUpsilon` | chosen `Q_B`, full residual two-jet and observed pullback |
| `I_II` | observer `||II||^2` | separate Gauss/Weyl/Bach functional | map from `I2B` or `I1B`, Euler and preboundary equivalence |

The source confirms the two-layer architecture and observation arena but is
silent on an equality among these functionals or their cubic tensors. The
repository's exact two-layer theorem already supplies counterexamples to a
generic `D3 I1B = D3 I2B` identification.

Thus “assemble all owners” would add terms from distinct actions unless the
map among them is constructed first.

## 3. Minimum pullback data

Choose one primitive action `I` and a field map `F` from observed variables to
its native fields. At a stationary native background,

```text
D3(I o F)[u,v,w]
 = D3I[DFu,DFv,DFw]
 + D2I[D2F(u,v),DFw] + cyclic.                       (1)
```

No `DI[D3F]` term survives at stationarity. Hence the minimum geometric input
is the first and second jet of `F`, not an unspecified third observation jet.
Off shell, `DI[D3F]` returns and the two-jet packet is insufficient.

For the residual-square layer

```text
I2=(1/2)<Upsilon,Q Upsilon>,   Upsilon(x_*)=0,          (2)
```

the cubic depends on `DUpsilon`, `D2Upsilon` and `DQ`:

```text
D3I2 = <D2Upsilon, Q DUpsilon> + cyclic
      + <DUpsilon, (DQ) DUpsilon> + cyclic.             (3)
```

So residual zero eliminates tadpole terms but does not reduce `D3 I2` to the
known Hessian. A selected target pairing and residual two-jet remain required.

The repository owns general first/second soldering and observation jet
locations, plus pointwise action banks and local Noether/preboundary packets.
It does not yet own one stationary `j2F` on the three requested external legs
inside one selected action layer.

## 4. Exact non-identifiability after both diagonal projections

Write the free pencil as

```text
J0(z)=z K0+M0,
K0=[[alpha,1],[1,0]],   M0=[[0,0],[0,b]].               (4)
```

A general symmetric first-order deformation is

```text
delta J(z)=z [[d,c],[c,e]] + [[m,q],[q,s]].              (5)
```

It has six coefficients. The observed scalar horn fixes only `d`. Even if we
conditionally identify `theta` with `theta_rad` and use the intrinsic
augmented-torsion result to fix `s`, four coefficients remain:

```text
(c,e,m,q).                                               (6)
```

Those four slots are exactly where moving Levi-Civita/soldering, Shiab,
pairing, observation and action-layer choices can enter. They are not fitted
parameters licensed by the current theory.

The insufficiency changes the spectrum. For the direct completion

```text
delta K_dir=[[d,0],[0,0]],  delta M_dir=[[0,0],[0,s]],   (7)
```

the first derivative of the normalized discriminant is

```text
delta Delta_dir = 2 alpha b (alpha s+b d).               (8)
```

Now take any infinitesimal field redefinition `x -> (1+tR)x`. Its congruence
completion is

```text
delta K_fr=R^T K0+K0 R,
delta M_fr=R^T M0+M0 R.                                  (9)
```

Choosing

```text
R21=d/2-alpha R11,    R22=s/(2b)                          (10)
```

makes (9) share exactly the same `delta K_hh=d` and
`delta M_vv=s` as (7), while leaving two free completion coordinates. But its
normalized dynamics changes by similarity, so

```text
delta Delta_fr=0.                                        (11)
```

For generic exact controls (8) is nonzero. Equations (7)--(11) are two full-
pencil completions agreeing on every presently granted diagonal projection
and disagreeing on the spectral response. Therefore even the strongest
conditional fusion of the existing cubic data does not select a pencil.

## 5. Disposition of the previously named owner packages

| package | K118 disposition |
| --- | --- |
| intrinsic augmented-torsion `D3` | exact summand, but its scalar lift is conditional |
| moving gimmel/Hodge/coframe | one fused naturality packet, not independent coefficients |
| first/second soldering and observation jets | exact owner locations; no selected three-leg coefficient assembly |
| pointwise full action bank | exact field-direction covector, not the requested observed three-leg pullback |
| local Noether/preboundary | small-gauge basicness exact; unrestricted boundary moment map live |
| `I2B` Hessian at residual zero | exact real symmetric pullback; insufficient for its cubic |
| `I_II` | separate observer functional; no action-layer equivalence |

Nothing here says that the missing map cannot exist. It says the map is the
input that would make the requested derivative a mathematical object.

## 6. Reverse-scaffold correction

```text
R0 known: observed fixed-symbol dJ_hh=d z E_hh
R1 conditional: intrinsic radial-vv D3 summand
R2 missing: choose I_sc, I1B, I2B or I_II as the primitive layer
R3 missing: stationary observed-to-native j2F on (theta,h,v)
R4 then: compute D3(I o F) and its unrestricted preboundary representative
R5 then: build the unique pencil only if R4 fixes all six coefficients
R6 later: spectral owner match, stationarity/domain, and BFV attachment
```

Next swings:

1. **K119:** action-layer and scalar-lift selection gate. Construct or rule out
   a typed stationary `j2F` identifying the observed scalar/TT horn with one
   primitive native action layer.
2. **K120:** if K119 succeeds, evaluate the complete pullback cubic and
   preboundary representative coefficientwise.
3. **K121:** only if K120 fixes one pencil, perform the spectral connection
   and literal Euler owner match.
4. **K122/K123:** stationarity/domain and `2D`-to-`98D` attachment remain last.

Exact probe: `42/42`. The result changes no canon, ledger verdict or public posture. It strengthens
the repository's custody rule: an action name without a selected action layer
and field map is not an owner.

## K119 selection correction — 2026-08-15

K119 proves that neither stationarity nor cubic agreement can select the map
requested above. At `DI=0`, every `DF,D2F` preserves stationarity, while the
Hessian-times-`D2F` terms remain in the cubic. On a nondegenerate three-field
branch, the exact 18-dimensional quadratic-jet space surjects onto all ten
symmetric cubic coefficients with an eight-dimensional kernel. Even the
affine diagonal lift retains one rescaling dimension after both known
projections match. K120 must therefore derive the geometric map jet
independently from one selected action's soldering/observation owners; cubic
assembly moves to K121.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k118_rsap_tt_full_moving_d3_owner_sufficiency_and_action_layer_gate_probe.py
```
