---
artifact_type: construction_result
created: 2026-08-05
status: CURRENT_I1B_OWNER_KILLED_AT_T0__CONDITIONAL_PRE_SHIAB_DEFECT_ACTION_AND_NONNULL_EVEN_BV_SYMBOL_EXACT__GLOBAL_SOLDERING_WELD_AND_NONLINEAR_BV_OPEN
ledger_rows: [LT-GR1b, LT-GR2b, LT-GR2c, LT-GR2d, LT-SM8]
fork_assumed: SIGNATURE_AMBIENT_K77__RESTRICTION_FIRST_GAUSS_REPLACEMENT_HORN
search_space_dim: "five Lorentz-covariant second-order coefficients reduced to one Einstein line by rank-four Ward/Bianchi constraints; overall cross coefficient inherited as unit on the replacement horn; one discrete action horn and one global soldering owner remain"
free_object_delta: "zero new fields; one existing-but-unbuilt epsilon_IG gravitational soldering map remains"
source_return: SOURCE-SILENT
scripts:
  - tests/channel-swings/pre_shiab_gauss_defect_action_bv_symbol_probe.py
  - tests/channel-swings/pre_shiab_gauss_defect_action_bv_symbol_independent.sage
registry: lab/process/pre-shiab-gauss-defect-action-bv-symbol.json
---

# Pre-Shiab Gauss defect action and even-BV symbol

## Result first

The existing K77 `I1B` action cannot own the faithful restriction-first
Einstein receiver at the homogeneous `T=0` value locus. Its only curvature
row there is the selected Shiab output. Every section, density and moving-Shiab
derivative of the bilinear curvature term still carries an explicit factor of
`T`. Consequently the already-proved rank-ten Riemann-kernel witness gives

```text
current I1B Euler curvature rows = 0
restriction-first observed Einstein tensor != 0.
```

This is the noncircular answer to the previous question. The old receiver is
not allowed to kill the fluctuating geometry, but the old **action term** also
cannot be credited with geometry it does not contain.

A smallest local repair can nevertheless be written as an honest action horn:

\[
 I_{\rm pre}
 =\int_X
 \left[
 \left\langle\sigma_\epsilon(v_T),
 G_4\!\left(\operatorname{res}_H P_R\bar F+Q(II_s)\right)
 \right\rangle_{DW}
 +\frac{\kappa_1}{2}
 \left\langle\sigma_\epsilon(v_T),\sigma_\epsilon(v_T)\right\rangle_{DW}
 \right]\mu_s . \tag{1}
\]

Here the Gauss receiver is applied before the killed ambient contraction and
the trace-reversed Frobenius pairing is retained. The term is not another
copy of `I1B`; it is a declared replacement for the localized gravitational
vertical transgression on one rival action horn.

At a fixed gravitational slot, flat observation background and non-null
covector, (1) has an exact linearized diffeomorphism-BV symbol complex

\[
 \mathbb R^4\xrightarrow{d_0}
 \operatorname{Sym}^2\oplus\operatorname{Sym}^2
 \xrightarrow{J_{\rm pre}}
 (\operatorname{Sym}^2\oplus\operatorname{Sym}^2)^*
 \xrightarrow{d_0^*}(\mathbb R^4)^*, \tag{2}
\]

with dimensions `4 -> 20 -> 20 -> 4`, Hessian rank `16`,
`ker J_pre=im d0`, and `im J_pre=ker d0*`. Thus the local quotient dimension
and descended Hessian rank are both **16**. This is an actual tangent
differential and exact complex, not a subtraction by four.

The repair remains conditional. Raw
`v_T in V* tensor ad(P)` is not an ordinary symmetric tensor. Equation (1)
requires a gravitational soldering map `sigma_epsilon`. The repository owns a
moving `epsilon_IG` field and fixed-frame gravitational slots, but not the
global ten-dimensional equivariant map needed here. The one-dimensional
tautological trace `q` cannot substitute for the full ten-dimensional map.
Accordingly the local symbol quotient is ranked, but the nonlinear/global
action, soldering descent, bulk/defect weld and physical quotient remain open.

## Layer 0

| name | object used | not identified with |
| --- | --- | --- |
| ambient Shiab | selected `Omega2(Y,ad P)->Omega13(Y,ad P)` contraction in current `I1B` | restriction-first Gauss curvature |
| observed Gauss curvature | `G4(res_H P_R barF+Q(II_s))` | ambient `G14`, fixed `Lambda g`, or a direct pullback of a 13-form |
| `T` | full connection difference | its vertical coefficient, Euler covector or VEV |
| `v_T` | section-restricted element of `V* tensor ad(P)` | a bare `Sym2` multiplier |
| `sigma_epsilon` | gravitational soldering/projection to the selected `Sym2` slot | identity on the adjoint carrier or the trace line `q` |
| even BV symbol | diffeomorphism tangent of the repaired observed action | odd super-IG, global CME, BFV boundary theory or positive state space |
| quotient rank 16 | non-null symbol quotient of the 20-field Hessian | ten Einstein components, six graviton polarizations or a global residue reduction |

The current-action no-go and repaired-action construction therefore concern
different action horns, not two descriptions of the same term.

## Why current `I1B` cannot do it at this locus

At homogeneous `T=0`, the existing action has the schematic value term

\[
 I_{1B}^{(0)}(T,R,s)=\langle T,S_s(R)\rangle
 +\frac{\kappa_1}{2}\langle T,*T\rangle .
\]

Its curvature-dependent value derivatives are

\[
 E_T=S_s(R),\qquad
 E_s^{\rm curv}=\langle T,(D_sS_s)R\rangle
 +D_s(\mu_s,*)\,[T,S_s(R)],
\]

and the independent connection row begins with derivatives/commutators of
`T`. At `T=0`, every row other than `E_T` vanishes and `E_T` factors through
`S_s`. The rank-ten witness lies in `ker S_s` but has nonzero
restriction-first `G4`. No moving-section chain rule can remove the explicit
factor of `T` at that point.

The scope is exact: this does not exclude a nonzero-`T` branch, a different
Shiab, a nonregular parent action, or the repaired defect horn (1).

## Why the observed receiver is not fitted freely

Before examining the BV ranks, use the complete Lorentz-covariant second-order
five-coefficient ansatz on symmetric tensors:

\[
 a k^2h_{\mu\nu}
 +b(k_\mu k^\rho h_{\rho\nu}+k_\nu k^\rho h_{\rho\mu})
 +c k_\mu k_\nu h
 +d g_{\mu\nu}k^\rho k^\sigma h_{\rho\sigma}
 +e g_{\mu\nu}k^2h.
\]

Exact gauge-tangent annihilation and Bianchi transversality have joint
constraint rank four and leave the single line

```text
(a,b,c,d,e) proportional to (-1,1,-1,-1,1).
```

The Gauss linearization is the half-normalized member of that line. The
replacement therefore does not fit five coefficients to a desired rank.
The remaining overall unit is inherited from the unit transgression on the
declared replacement horn, not derived from the source; choosing that horn is
one discrete construction choice inside the already-open `LT-GR1b/LT-GR2c`
action-architecture fork, not a new independent factor in the residue product.

The trace-reversed Lorentz Frobenius Gram is nondegenerate with inertia
`(6,4)`. Replacing it by a Euclidean dot product changes the construction and
is rejected by the certificate.

## Exact BV symbol theorem

Let `h` be the observed metric variation and `v=sigma_epsilon(v_T)` the
selected gravitational distortion coefficient. At a flat background,

\[
 I_{\rm pre}^{(2)}(h,v)
 =\langle v,G^{(1)}(h)\rangle_{DW}
 +\frac{\kappa_1}{2}\langle v,v\rangle_{DW}.
\]

With `W_DW` the `(6,4)` Gram, the Hessian is

\[
 J_{\rm pre}(k)=
 \begin{pmatrix}
 0&G(k)^TW_{DW}\\
 W_{DW}G(k)&\kappa_1W_{DW}
 \end{pmatrix}. \tag{3}
\]

The actual linearized even BRST tangent at `v=0` is

\[
 d_0(k)\xi=(k_{(\mu}\xi_{\nu)},0).
\]

For both a timelike and a spacelike rational covector and fixed nonzero
`kappa_1`:

| object | exact rank |
| --- | ---: |
| Einstein symbol `G(k)` | 6 |
| diffeomorphism tangent `d0(k)` | 4 |
| repaired Hessian `J_pre(k)` | 16 |
| Hessian kernel | 4 = `im d0` |
| Noether kernel | 16 = `im J_pre` |
| field quotient | `20-4=16` |

Both `J_pre d0=0` and `d0^*J_pre=0` hold coefficientwise. At zero gain the
Hessian rank drops to 12 and its eight-dimensional kernel is larger than the
four-dimensional gauge image. Thus the existing nonzero gain is doing real
constraint work rather than merely normalizing the action.

For a null covector, `rank G=4` and `rank J_pre=10`. After removing the four
gauge directions, six non-gauge characteristic kernel directions remain.
This is the expected place for propagation/Green-domain analysis; it prevents
promotion of noncharacteristic exactness to a hyperbolicity theorem.

## What the local soldering condition costs

The exact matrix calculation works after a ten-dimensional gravitational
slot is fixed. Globally, the source carrier is adjoint-valued. A map

\[
 \sigma_\epsilon:
 s^*V^*Y\otimes s^*\operatorname{ad}P
 \longrightarrow \operatorname{Sym}^2T^*X
\]

must be constructed from the moving reduction/soldering field or the symmetry
must honestly be restricted to its stabilizer. There is no invariant scalar
functional on a semisimple adjoint representation that makes this map
automatic. The canonical trace vector `q` supplies one line only; using it
for all ten components would repeat the trace-versus-full-sector error.

This is now the narrowest missing object. It is a possible home for the
previously under-typed X-sector datum, but the wave does not identify it with
P2 or consume P1/P2/P3.

## Source, constraint and residue accounting

**Source return: `SOURCE-SILENT`.** Weinstein supplies the two-connection
field, trace reversal, section-observation grammar and existing gain, but does
not print (1), `sigma_epsilon`, or (2).

| quantity | result |
| --- | ---: |
| new fields | 0 |
| new continuous coefficients | 0 on the unit replacement horn |
| new discrete architecture choice | 1 replacement horn refining the existing open action-architecture fork; not a new independent residue factor |
| five-coefficient receiver freedom after Ward/Bianchi | 1 scale line |
| local non-null BV quotients ranked | 1 |
| global nonlinear/BFV quotients ranked | 0 |
| P1/P2/P3 | unchanged and unused |

The finite ansatz is determined up to scale before held-out Hessian exactness,
zero-gain failure and null-characteristic behavior are read. A full numerical
constraint-surplus claim is withheld until the soldering-map parameter space
is itself ranked.

## Seven-axis audit

| layer | disposition |
| --- | --- |
| Layer 0 | ambient/observed curvature, raw/soldered `v_T`, action horns and BV grades separated |
| L1 source | `SOURCE-SILENT` on repaired term and BV; ingredients confirmed only in predecessor receipts |
| L2 algebra | unique Einstein line, `(6,4)` trace reversal and exact ranks independently rebuilt over `QQ` |
| L3 geometry | Gauss/`II` receiver written; global `sigma_epsilon` and moving normal-to-vertical descent open |
| L4 variation | current-action scoped kill and repaired variational Hessian exact |
| L5 covariance | local even diffeomorphism symbol complex exact off the null cone; nonlinear tilted BV open |
| L6 analytic | null characteristic residual exposed; no Green/domain theorem |
| L7 physics | no vacuum selection, screening, FLRW, positivity or particle claim |

## Hostile disposition and next gate

The paired review rejected two overstatements: calling the local `v` slot the
raw adjoint-valued `v_T`, and calling rank 16 a positive physical quotient.
The repaired result is accepted only at fixed-slot, non-null, linearized even
BV grade.

Next gate:

```text
CONSTRUCT_EPSILON_IG_GRAVITATIONAL_SOLDERING_MAP_AND_NONLINEAR_PRE_SHIAB_DEFECT_WELD
```

It must construct `sigma_epsilon` on the actual bundle (or state the honest
stabilizer restriction), insert (1) into one nonduplicating bulk/defect action,
derive the complete nonlinear even Ward/BV owner ledger, and then recompute
the quotient including the null characteristic/domain problem. Only after
that may a nonzero vacuum branch test `LT-GR2b/d/e`.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/pre_shiab_gauss_defect_action_bv_symbol_probe.py
DOT_SAGE=/private/tmp/gu-pre-shiab-bv-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/pre_shiab_gauss_defect_action_bv_symbol_independent.sage
```

Main receipt: `1 source + 3 repo + 36 exact + 7 type + 11 planted = 58/58`.
Independent Sage/QQ reconstruction passes. No canon, public posture, Lane
count, P1/P2/P3, magnitude or phenomenology claim moves.
