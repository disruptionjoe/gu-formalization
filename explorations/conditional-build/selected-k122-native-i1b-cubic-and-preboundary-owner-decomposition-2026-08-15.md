---
title: "Selected-K122 native I1B cubic and preboundary owner decomposition"
status: active_research
doc_type: exact_native_stationary_chain_rule_and_preboundary_owner_decomposition
created: "2026-08-15"
registry: lab/process/selected-k122-native-i1b-cubic-and-preboundary-owner-decomposition.json
probe: tests/channel-swings/selected_k122_native_i1b_cubic_and_preboundary_owner_decomposition_probe.py
grade: "THE NATIVE I1B CUBIC ON (T,H,V) NOW HAS A COMPLETE STRUCTURAL OWNER DECOMPOSITION. WITH PBAR=(0,PHI1), HBAR=(H,DB_LC[H]), VBAR=(0,V), AND Q_HH=(0,D2B_LC[H,H]), THE THREE TT SLOTS ARE C_THH=D3I1B[PBAR,HBAR,HBAR]+D2I1B[PBAR,Q_HH], C_THV=D3I1B[PBAR,HBAR,VBAR], AND C_TVV=D3I1B[PBAR,VBAR,VBAR]. ONLY T-H-H RECEIVES A SECOND-LEVI-CIVITA-JET CORRECTION. EXACT NATIVE COORDINATE CANCELLATION RETYPES THE OLD 14/3 LC-LC VALUE AS A FIXED-VARPI PARTIAL REPRESENTATIVE, NOT A NATIVE T-H-H COEFFICIENT. AT FIXED G THE FULL I1B ACTION IS AT MOST CUBIC IN T AND ONLY ITS AUGMENTED-TORSION TERM IS CUBIC, SO C_TVV=-56/3 TIMES THE NATIVE TT NORM AND D3_TTT=8736 ARE FULL-I1B VALUES ON THIS SLICE. C_THH, C_THV, AND REDUCED PREBOUNDARY DESCENT REMAIN OPEN ON THREE SAME-I1B PRIMITIVE EVALUATIONS."
target_claim: K121_NEXT_GATE__COMPLETE_NATIVE_I1B_PULLBACK_CUBIC_AND_PREBOUNDARY_ON_T_H_V
target_verdict: STRUCTURAL_OWNER_DECOMPOSITION_COMPLETE__FIXED_METRIC_C_TVV_EXACT__C_THH_C_THV_AND_REDUCED_PREBOUNDARY_OPEN
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

Equations (3)--(4) are structurally complete. The fixed-metric slot is also
numerically complete:

```text
C_t_v_v = -(56/3)<V,*V>.                              (5)
```

At fixed `g`, the printed `I1B` action is linear in `T` through `F_B`,
quadratic through `D_B T` and the `kappa_1` term, and cubic only through
`T^2`. Consequently no omitted moving or derivative term can add to a third
derivative containing only `t,v,v`. The two `h`-containing coefficients are
**not numerically complete** because the repository has not serialized three
required same-`I1B` primitive tensor evaluations. K123 is now a bounded
coefficientwise task rather than another undifferentiated “full moving”
request.

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

Under (1), `u=t Phi1+v` exactly; its TT component is `v`. The probe plants a
nonzero radial-connection Hessian, a nonzero `D2B_LC`, and a nonzero
radial-distortion cubic. Every apparent `t-h-h` and `t-h-v` contribution
cancels after the exact pullback, while the native `t-v-v` and `t-t-t` values
survive unchanged.

This prevents a serious overcount. Source-basis direct, first-jet and
second-jet terms are owner pieces, not separate physical interactions. They
must be summed before interpretation.

### Correction to the earlier LC--LC representative

The August 6 gauge-rotated Levi-Civita artifact inserted `DB_LC[H]` twice as
though it were an independent distortion direction in the fixed-geometry
`D3 I_T` backend and obtained the exact raw value

```text
(14/3)(p.q)(h0:hm).                                   (9)
```

That evaluator is algebraically correct for the path where `varpi` is held
fixed while `g` moves, or for two independently supplied connection
directions. It is not the native `h` column of (1). On that column

```text
delta varpi=DB_LC[H],
delta T=delta varpi-DB_LC[H]=0,
delta2 T=D2B_LC[H,H]-D2B_LC[H,H]=0.                  (10)
```

Thus (9) is retyped as a noncomposable partial-coordinate representative,
not a native `C_t_h_h` owner. Genuine nonzero `h`-containing coefficients
must come from the `F_B`, `D_B T`, and moving metric/frame/Hodge/Shiab/
pairing/density terms of the same full action after all source-coordinate
pieces are summed.

## 4. Exact fixed-metric full-`I1B` slots

The printed selected first action is

```text
bar F = F_B + (1/2)D_B T + (1/3)T^2,
I1B    = <T,S(bar F)> + (kappa_1/2)<T,*T>.            (11)
```

With `g` fixed, `B`, `S`, `*`, the pairing and density are fixed. The four
summands in (11) have degrees one, two, three and two in `T`. Therefore the
existing augmented-torsion computation gives the complete full-`I1B` third
derivative for any three fixed-metric `T` directions:

```text
D3 I1B[t,t,t] = 8736,
D3 I1B[t,v,v] / <v,*v> = -56/3                        (12)
```

on the named radial/TT slice. The native `t-h-h` and `t-h-v` values of the
`T`-only term vanish after the coordinate cancellation in Section 3.
Equation (12) does not settle the `h`-containing slots, because moving `g`
activates the other terms and the metric-dependent tensors in (11).
Euler/Green and preboundary data govern descent; they are not extra bulk
terms that can alter (12).

## 5. Exact remaining evaluation packet

The action formula itself sharpens the owner support:

| same-`I1B` summand | fixed-`g` degree in `T` | native cubic support still requiring evaluation |
| --- | ---: | --- |
| `<T,S(F_B)>` | 1 | `t-h-h` through two metric/curvature or moving-tensor variations |
| `(1/2)<T,S(D_B T)>` | 2 | `t-h-v`, and `t-h-h` on the nonzero radial background through moving coefficients/connection |
| `(1/3)<T,S(T^2)>` | 3 | exact fixed-metric `t-v-v`; its moving tensors may also enter the two `h` slots |
| `(kappa_1/2)<T,*T>` | 2 | only `h`-containing slots through moving Hodge/pairing/density |

This is why the old LC insertion cannot simply be subtracted and the job
declared done: cancellation removes a mistyped `T`-only path, while the
printed action still contains genuine metric-dependent same-action owners.

Current artifacts own the map jet and the nonlinear Euler/preboundary
*locations*, but explicitly leave the direct selected-action coefficient
expansion and full derivative/curvature/density/observation tensors open.
Numerical completion of the two open bulk slots therefore requires exactly
these three evaluations:

1. `D3I1B[Pbar,Hbar,Hbar]`;
2. `D2I1B[Pbar,Q_hh]`;
3. `D3I1B[Pbar,Hbar,Vbar]`.

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
| exact computation | use symbolic generic tensors, degree support and planted cancellations | certificate role |
| brute-force matrix search | enumerate full coefficients without a tensor contract | rejected as premature |
| cross-action matching | import `I_sc` or `I_II` coefficients | rejected by custody and K121 |
| field redefinition | choose a fitted scalar or quadratic map | rejected by K119/K121 |
| wild-frontier | infer a spectral mode directly from `-56/3` | rejected: a cubic coefficient is not a free pencil or reduced observable |

The selected route has the highest decision power because it converts the
open request into three falsifiable primitive evaluations while preserving all
exact cancellations. The fallback is coefficientwise evaluation of any
proper subset with explicit residual slots; a guessed pencil is never the
fallback.

## 7. Reverse scaffold and next gates

```text
S0 complete: native source-coordinate two-jet
S1 complete: exact three-slot cubic support theorem
S2 complete: exact three-column preboundary pullback
S3 complete: fixed-metric full-I1B values 8736 and -56/3
S4 corrected: old 14/3 LC-LC representative is not a native h coefficient
S5 complete at K123: primitive slots are chart-split; evidence deficit rank 2
S6 open at K124: build O_K123 and evaluate the native sums in one basis
S7 then: determine whether all six first-order pencil coefficients are fixed
S8 then: test spectral ownership and common Green/domain data
S9 later: BFV reduction and non-invariant/nonlinear/boundary/cohomological
          2D-to-98D attachment
```

K123 subsequently proves that the three primitive source-coordinate slots
redistribute under admissible chart changes and that the pre-K124 serialized
bank leaves the two native sums underdetermined with rank two. K124 then
constructs the homogeneous-radial/back-to-back full-carrier TT slice,
obtaining `C_t_h_h^prin=-12q^2<DW>` and `C_t_h_v^prin=0` there. K126 later
completes the common-transverse three-momentum polynomial and shows that its
isolated live radial-momentum `d(D2B_LC)` cell cancels under full natural
transport. K127 constructs the local Ricci-flat curved response and exposes
off-TT leakage; source-global representative/domain selection now routes to
K128. Only a completed native evaluator may
reopen the pencil, spectral-owner, and common-domain gates.

No ledger, datum, quotient, canon, public posture, particle interpretation,
phenomenology or GU truth-status claim changes. Joe input is not required.

Exact probe: `39/39`.

## K123 successor closure — 2026-08-15

K123 proves that the three primitive source-coordinate evaluations cannot be
recovered numerically from the current serialized bank. More sharply, linear
and nonlinear connection-coordinate changes redistribute those primitive
pieces while preserving the two native sums. A planted missing moving germ
shifts `C_t_h_h,C_t_h_v` with rank two while preserving every K122 control.
The next target is therefore `O_K123`, one common full-14D native-`I1B`
evaluator returning the two native coefficients first and the three frozen-
chart pieces only as checksums.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k122_native_i1b_cubic_and_preboundary_owner_decomposition_probe.py
```
