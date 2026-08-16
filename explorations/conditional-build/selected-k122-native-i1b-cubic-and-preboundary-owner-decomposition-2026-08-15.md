---
title: "Selected-K122 native I1B cubic and preboundary owner decomposition"
status: active_research
doc_type: exact_native_stationary_chain_rule_and_preboundary_owner_decomposition
created: "2026-08-15"
registry: lab/process/selected-k122-native-i1b-cubic-and-preboundary-owner-decomposition.json
probe: tests/channel-swings/selected_k122_native_i1b_cubic_and_preboundary_owner_decomposition_probe.py
grade: "THE NATIVE I1B CUBIC ON (T,H,V) NOW HAS A COMPLETE STRUCTURAL OWNER DECOMPOSITION. WITH PBAR=(0,PHI1), HBAR=(H,DB_LC[H]), VBAR=(0,V), AND Q_HH=(0,D2B_LC[H,H]), THE THREE TT SLOTS ARE C_THH=D3I1B[PBAR,HBAR,HBAR]+D2I1B[PBAR,Q_HH], C_THV=D3I1B[PBAR,HBAR,VBAR], AND C_TVV=D3I1B[PBAR,VBAR,VBAR]. ONLY T-H-H RECEIVES A SECOND-LEVI-CIVITA-JET CORRECTION. THE PREBOUNDARY COLUMNS PULL BACK AS P_T=P_VARPI[PHI1], P_H=P_G[H]+P_VARPI[DB_LC[H]], AND P_V=P_VARPI[V]. THIS PACKET IS STRUCTURALLY COMPLETE BUT NOT NUMERICALLY COMPLETE: CURRENT ARTIFACTS DO NOT SERIALIZE FOUR REQUIRED FULL-I1B PRIMITIVE TENSOR EVALUATIONS. THE INTRINSIC 8736 AND -56/3 VALUES REMAIN EXACT SUB-SUMMANDS, NOT THE FULL CUBIC."
target_claim: K121_NEXT_GATE__COMPLETE_NATIVE_I1B_PULLBACK_CUBIC_AND_PREBOUNDARY_ON_T_H_V
target_verdict: STRUCTURAL_OWNER_DECOMPOSITION_COMPLETE__NUMERICAL_PRIMITIVE_TENSOR_EVALUATION_REMAINS_OPEN
canon_verdict_change: none
---

# Selected-K122 native I1B cubic and preboundary owner decomposition

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> parameterized-torsion, source-coordinate, variational-chain-rule and
> preboundary question. Ordinary Higgs/VEV, family-index, net-chirality,
> anomaly, symmetry-breaking and familiar four-dimensional gauge-model
> constructions do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K122 completes the *shape* of the native `I1B` answer without pretending that
an owner location is already a coefficient value.

Use the native fields `(t,h,v)`, where `T=t Phi1+v`, and the exact source
coordinate change

```text
(t,h,v) -> (g=h, varpi=B_LC(h)+t Phi1+v).               (1)
```

At a stationary background, the complete cubic with one radial leg and two TT
legs has exactly three slots. If

```text
Pbar=(0,Phi1),  Hbar=(H,DB_LC[H]),
Vbar=(0,V),     Q_hh=(0,D2B_LC[H,H]),                  (2)
```

then

```text
C_t_h_h = D3 I1B[Pbar,Hbar,Hbar] + D2 I1B[Pbar,Q_hh],
C_t_h_v = D3 I1B[Pbar,Hbar,Vbar],
C_t_v_v = D3 I1B[Pbar,Vbar,Vbar].                      (3)
```

Only `t-h-h` receives a Hessian paired with the nonlinear Levi-Civita second
jet. The other two slots are pure primitive third derivatives. This is the
exact support theorem that the earlier broad owner lists did not provide.

The matching unreduced preboundary one-form pulls back as

```text
p_t = p_varpi[Phi1],
p_h = p_g[H] + p_varpi[DB_LC[H]],
p_v = p_varpi[V].                                      (4)
```

No observed-scalar slope appears in (1)--(4). `lambda` enters only if a later
interface reports the native answer in an observed/reduced scalar convention.

Equations (3)--(4) are structurally complete. They are **not numerically
complete** because the repository has not yet serialized four full-`I1B`
primitive tensor evaluations. K123 is now a bounded coefficientwise task
rather than another undifferentiated “full moving” request.

## 1. Layer-0 packet

| name | typed object | disposition |
| --- | --- | --- |
| `t` | native coefficient of the invariant `Phi1` line inside full parameterized torsion | exact native coordinate; not an observed scalar |
| `h` | TT metric variation | enters both source metric and dependent Levi-Civita connection |
| `v` | independent TT distortion variation | enters the independent connection directly |
| `I1B` | selected first transgression action on source variables `(g,varpi)` | sole primitive action owner for this packet |
| `D2B_LC` | geometric second metric jet of the spin Levi-Civita connection | contributes only to `C_t_h_h` |
| `p` | unreduced Cartan/preboundary one-form | not yet a BFV charge or physical observable |

The geometer/physics fork is settled here in favor of the source-native
two-connection construction because the source action itself uses
`T=varpi-B_LC(g)`. That does not privilege a native answer elsewhere.

## 2. Exact stationary chain rule

For a stationary primitive action `I` and a map `F`,

```text
D3(I o F)[a,b,c]
 = D3I[DFa,DFb,DFc]
 + D2I[D2F(a,b),DFc] + cyclic.                         (5)
```

The native/source map (1) has only one nonzero second derivative among the
selected fields:

```text
D2F(h,h)=Q_hh,
D2F(t,h)=D2F(t,v)=D2F(h,v)=D2F(v,v)=0.                 (6)
```

Substituting (6) into (5) gives (3). In a scalar control with source-basis
first Levi-Civita coefficient `b1`, second coefficient `b2`, radial-connection
Hessian `H_rw`, and primitive cubic slots `C_rgg,C_rgw,C_rww`, the formulas are

```text
C_t_h_h = C_rgg + 2 b1 C_rgw + b1^2 C_rww + b2 H_rw,
C_t_h_v = C_rgw + b1 C_rww,
C_t_v_v = C_rww.                                      (7)
```

The triangular first-jet part is invertible, but recovering `C_rgg` requires
the independently owned `b2 H_rw` correction. This is why a fitted observed
two-jet was invalid in K119 and why K120's independently derived `D2B_LC`
matters.

## 3. Coordinate-invariance cancellation control

A torsion-only term written in source coordinates depends on

```text
u=varpi-B_LC(g).                                       (8)
```

Under (1), `u=v` exactly. The probe plants a nonzero radial-connection Hessian,
a nonzero `D2B_LC`, and a nonzero radial-distortion cubic. Every apparent
`t-h-h` and `t-h-v` contribution cancels after the exact pullback, while the
native `t-v-v` and `t-t-t` values survive unchanged.

This prevents a serious overcount. Source-basis direct, first-jet and
second-jet terms are owner pieces, not separate physical interactions. They
must be summed before interpretation.

## 4. Certified intrinsic sub-summands

The existing augmented-torsion zero-jet packet contributes

```text
D3 I_T[t,t,t] = 8736,
D3 I_T[t,v,v] / <v,*v> = -56/3                         (9)
```

on the named radial/TT slice. Its native `t-h-h` and `t-h-v` values vanish
after the coordinate cancellation in Section 3.

These are exact sub-summands, not the full `I1B` coefficients. The complete
first transgression action also contains derivative/curvature, moving
pairing/Hodge/Shiab/density, observation, Euler/Green and preboundary owners.
Nothing in K122 licenses silently replacing the full right sides of (3) by
(9).

## 5. Exact remaining evaluation packet

Current artifacts own the map jet and the nonlinear Euler/preboundary
*locations*, but explicitly leave the direct selected-action coefficient
expansion and full derivative/curvature/density/observation tensors open.
Numerical completion therefore requires exactly these four evaluations:

1. `D3I1B[Pbar,Hbar,Hbar]`;
2. `D2I1B[Pbar,Q_hh]`;
3. `D3I1B[Pbar,Hbar,Vbar]`; and
4. the full `D3I1B[Pbar,Vbar,Vbar]`, retaining (9) only as its certified
   torsion-only sub-summand.

The pointwise preboundary columns are already completely typed by (4), but
their explicit values must be evaluated from the same full action and then
carried through a selected Green domain and boundary reduction.

## 6. Broad route census and decision

| lens | route proposed | disposition |
| --- | --- | --- |
| source criticism | use only `I1B` and its actual source variables | selected |
| differential geometry | compose the exact first/second spin-LC jets | selected |
| variational calculus | apply the stationary third-order chain rule | selected |
| multilinear algebra | triangularize the three TT slots | selected |
| representation theory | retain `Phi1`, TT metric and TT distortion types | selected |
| Cartan/Green | pull back the preboundary one-form before reduction | selected |
| symplectic/BFV | withhold charge and cohomology claims until descent | selected |
| exact computation | use symbolic generic tensors and planted cancellations | certificate role |
| brute-force matrix search | enumerate full coefficients without a tensor contract | rejected as premature |
| cross-action matching | import `I_sc` or `I_II` coefficients | rejected by custody and K121 |
| field redefinition | choose a fitted scalar or quadratic map | rejected by K119/K121 |
| wild-frontier | infer a spectral mode directly from `-56/3` | rejected as sub-summand overreach |

The selected route has the highest decision power because it converts the
open request into four falsifiable primitive evaluations while preserving all
exact cancellations. The fallback is coefficientwise evaluation of any
proper subset with explicit residual slots; a guessed pencil is never the
fallback.

## 7. Reverse scaffold and next gates

```text
S0 complete: native source-coordinate two-jet
S1 complete: exact three-slot cubic support theorem
S2 complete: exact three-column preboundary pullback
S3 retained: intrinsic 8736 and -56/3 sub-summands
S4 open: evaluate four full-I1B primitive tensor slots
S5 then: determine whether all six first-order pencil coefficients are fixed
S6 then: test spectral ownership and common Green/domain data
S7 later: BFV reduction and non-invariant/nonlinear/boundary/cohomological
          2D-to-98D attachment
```

K123 must evaluate the four-slot packet coefficientwise, with planted
coordinate-cancellation and Ward/Cartan controls. Only if those values fix one
pencil may K124 test its spectral owner and common domain.

No ledger, datum, quotient, canon, public posture, particle interpretation,
phenomenology or GU truth-status claim changes. Joe input is not required.

Exact probe: `32/32`.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k122_native_i1b_cubic_and_preboundary_owner_decomposition_probe.py
```
