---
title: "Selected-K121 RSAP scalar role, action-germ, and conditional-bridge gate"
status: active_research
doc_type: exact_scalar_action_germ_incompatibility_and_role_bridge_reassessment
created: "2026-08-15"
registry: lab/process/selected-k121-rsap-scalar-role-action-germ-and-conditional-bridge-gate.json
probe: tests/channel-swings/selected_k121_rsap_scalar_role_action_germ_and_conditional_bridge_gate_probe.py
grade: "THE SOURCE IDENTIFIES THE DARK-ENERGY CARRIER AS THE FULL PARAMETERIZED-TORSION/DISTORTION FIELD, NOT AS A SEPARATELY NORMALIZED SCALAR. THE REPOSITORY'S I_SC HORN IS A SCALAR-IRREP EFFECTIVE REDUCTION, WHILE THE EXACT I1B PHI1 RADIAL RESTRICTION HAS A NONZERO CUBIC ACTION GERM. AT THEIR STATIONARY POINTS NO NONZERO AFFINE SCALAR MAP, EVEN WITH AN OVERALL ACTION RESCALING, IDENTIFIES THESE TWO ACTION GERMS: I_SC HAS ZERO PURE-SCALAR D3 AND I1B HAS D3=8736. THEIR STATIONARY FAMILIES ALSO DO NOT SELECT A UNIVERSAL SLOPE. A NONLINEAR MAP CAN CANCEL THE CUBIC ONLY BY ADDING THE NEW UNOWNED SCALAR SECOND JET Q=208 LAMBDA^2/KAPPA_1. THEREFORE I_SC CANNOT DONATE ITS COEFFICIENTS TO I1B. LAMBDA REMAINS AN EXPLICIT VARIANCER TRANSLATION DATUM; NATIVE I1B WORK SHOULD USE T ITSELF AND COMPUTE ITS COMPLETE CUBIC WITHOUT CROSS-ACTION FUSION."
target_claim: K120_NEXT_GATE__ACTION_NORMALIZATION_STATIONARY_BACKGROUND_ORIENTATION_AND_OBSERVATION_SEMANTICS_SELECT_THETA_ISC_EQUALS_LAMBDA_TIMES_T_RADIAL
target_verdict: ROLE_LINK_ONLY__STRICT_AFFINE_ACTION_GERM_IDENTITY_REFUTED__LAMBDA_AND_ANY_NONLINEAR_SCALAR_JET_REMAIN_CONDITIONAL
canon_verdict_change: none
---

# Selected-K121 RSAP scalar role, action-germ, and conditional-bridge gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> parameterized-torsion, action-restriction, stationary-background and
> observation-map question. Ordinary Higgs/VEV, family-index, net-chirality,
> anomaly, symmetry-breaking and familiar four-dimensional gauge-model
> constructions do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K121 separates two statements that earlier work repeatedly allowed to slide
into one another.

The first statement is source-supported: Weinstein's proposed dark-energy
carrier is a movable, equivariant **parameterized torsion/distortion field**,
the difference of two connections. The repository's `I1B` variable `T` is
therefore the right native kind of object to investigate. The invariant line
`T=t Phi1` is a useful exact slice of that field, not the whole field and not
an observed scalar by declaration.

The second statement is false at the action-germ grade tested here: the scalar
coefficient in the local `I_sc` horn is not an affine normalization of the
exact `I1B` radial action. At fixed geometry the two scalar restrictions are

```text
W_sc(theta)=beta R theta+(kappa/2)theta^2-rho,
W_1B(t)=1456 t^3+7 kappa_1 t^2.                         (1)
```

At their nondegenerate stationary points, `D3 W_sc=0` while
`D3 W_1B=8736`. A nonzero affine change of scalar coordinate, even combined
with a nonzero overall rescaling of the action, cannot turn zero into nonzero.
The quadratic terms can be matched only by imposing a cross-action equation,
and the background values can be matched only pointwise; neither selects a
universal slope or orientation.

A nonlinear scalar map can hide the cubic locally, but it must introduce the
new second jet

```text
t=t_*+lambda x+(q/2)x^2+...,
q=208 lambda^2/kappa_1.                                (2)
```

No source, geometry, observation or boundary owner supplies (2). It is
exactly the kind of fitted map jet K119 prohibited.

So the strongest synthesis is neither “the fields are unrelated” nor “set
`lambda=1`.” They are related at the **physical-role/carrier** level, but the
written actions and scalar coordinates are not identified. `lambda` remains
an explicit Variancer conditional whenever translating the effective horn to
the native radial slice. Native construction should instead use `t` directly
and compute the complete `I1B` pullback on `(t,h,v)` without importing
`I_sc` coefficients.

## 1. Layer-0 packet

| name | typed object | disposition |
| --- | --- | --- |
| source `Theta` | full adjoint-valued one-form/difference of two connections | source-named movable dark-energy candidate |
| native `T` | augmented torsion in `I1B` | correct source-native carrier class |
| `t` or `theta_rad` | coefficient on the invariant slice `T=t Phi1` | exact native coordinate on one line, not the full field |
| `I_sc` scalar | scalar-irrep local curvature/VEV horn | effective/reduced comparator, not the complete radial `I1B` action |
| `lambda` | tangent conversion between the observed/reduced scalar and `t` | explicit conditional datum |
| `q` | possible scalar second jet in a nonlinear bridge | new unowned datum, not admitted into the native assembly |

The typed relation is therefore:

```text
full parameterized torsion <-> dark-energy carrier role: SOURCE-CONFIRMS
Phi1 radial line <-> useful invariant native slice:       EXACT
I_sc scalar action germ = affine pullback of I1B radial:  REFUTED
observed/reduced scalar -> native radial perturbation:     CONDITIONAL(lambda)
```

## 2. Exact action-germ obstruction

For fixed `R`, the scalar-horn stationarity equation and Taylor data are

```text
theta_*=-beta R/kappa,
W_sc''(theta_*)=kappa,
W_sc'''(theta_*)=0.                                     (3)
```

The selected nonzero native radial branch is

```text
t_*=-kappa_1/312,
W_1B''(t_*)=-14 kappa_1,
W_1B'''(t_*)=8736.                                     (4)
```

Suppose strict identity held up to a nonzero action scale `mu` and a nonzero
affine slope `lambda`:

```text
W_sc(theta_*+x)=mu W_1B(t_*+lambda x)+constant.         (5)
```

Third differentiation of (5) would require

```text
0=mu 8736 lambda^3,                                    (6)
```

which is impossible for a genuine action and invertible scalar coordinate.
This is stronger than a coefficient mismatch: vanishing versus nonvanishing
pure-scalar third derivative is invariant under every nonzero affine change.

Quadratic matching alone would impose

```text
kappa=mu (-14 kappa_1) lambda^2.                        (7)
```

It remains a cross-action condition, is sign-blind in `lambda`, and cannot
repair (6). With `mu=1` and both gains positive, it has no real solution at
the nonzero native branch; no selected theorem currently equates those gains
or their sign conventions.

## 3. Stationary families do not choose the slope

The constant-field `I_sc` horn gives

```text
R_*=2 rho/(a),
theta_*=-2 beta rho/(a kappa).                          (8)
```

The native algebraic branch gives `t_*=-kappa_1/312`, independent of `rho`.
An origin-preserving point match `t_*=lambda theta_*` therefore requires

```text
lambda_bg=a kappa kappa_1/(624 beta rho).               (9)
```

That is source-amplitude dependent, so it is not a fixed field normalization.
A background-centred affine map

```text
t=t_*+lambda(theta-theta_*)                             (10)
```

matches the points for every nonzero `lambda`, proving again that stationarity
does not select the tangent bridge. Moreover, the native branch is only a
fixed-metric algebraic stationary branch; it is not yet the coupled
curvature/VEV stationary family assumed by `I_sc`.

## 4. Why a nonlinear rescue is conditional, not selected

Let

```text
t=t_*+lambda x+(q/2)x^2+....                            (11)
```

At native stationarity the composite third derivative is

```text
D3(W_1B o t)=8736 lambda^3+3(-14 kappa_1)lambda q.      (12)
```

It vanishes exactly for (2). Thus a local nonlinear equivalence is not
mathematically impossible. But it changes the scalar `D2F` that K120 left
zero and that K119 proved can manufacture desired cubic coefficients. No
source-coordinate identity analogous to `T=varpi-B_LC(g)` owns this scalar
second jet. It is therefore a new Variancer conditional, not a closure.

## 5. Observation, orientation, and boundary checks

- The source's `Theta` is the full equivariant connection difference. It does
  not name the coefficient of `Phi1` as the observed field or provide its
  units.
- The observation germ receives an already chosen native field. It does not
  manufacture an inverse scalar coordinate or select `lambda`.
- The native cubic or the `I_sc` `theta-h-h` vertex could fix an oriented
  slope only after their action terms were proved equal. Equation (6) refutes
  that strict affine equality, so such a fit is not ownership.
- The native preboundary radial column remains proportional to `lambda`; the
  unrestricted boundary moment map is still live and supplies no normalization.
- Gauge/BV descent acts on the full connection-valued field. It does not
  collapse that carrier to the `Phi1` line or normalize its scalar coefficient.

## 6. Twenty-lens reassessment and vote

The four hypotheses were:

```text
H_A  strict affine equality of the I_sc and I1B radial action variables
H_B  role-linked effective reduction; native I1B owns the carrier, lambda conditional
H_C  keep the action layers strictly separate in all coefficient assembly
H_D  a nonlinear scalar bridge may exist but requires a new owned scalar D2 jet
```

| # | lens | strongest hypothesis | reason |
| --- | --- | --- | --- |
| 1 | source criticism | `H_B` | source names full parameterized torsion, not a normalized scalar coefficient |
| 2 | Layer-0 typing | `H_B` | full `Theta`, radial `t`, and reduced horn scalar have different types |
| 3 | variational calculus | `H_B` | the reduced horn and complete radial restriction have different Taylor tensors |
| 4 | action-germ theory | `H_D` | affine equality fails; a nonlinear Morse-type map remains possible |
| 5 | stationary backgrounds | `H_B` | point matching leaves the slope free and family matching makes it `rho` dependent |
| 6 | differential geometry | `H_B` | `T=varpi-B_LC(g)` owns TT jets but no scalar injection |
| 7 | representation theory | `H_B` | `Phi1` is one invariant line inside the full adjoint-valued carrier |
| 8 | observation semantics | `H_B` | a receiver transports a chosen field; it does not define the native field |
| 9 | quadratic normalization | `H_B` | Hessian matching is conditional and sign blind |
| 10 | field-redefinition theory | `H_D` | cancellation requires the explicit new `q` in (2) |
| 11 | action custody | `H_C` | coefficients from distinct written functionals cannot be summed without an owner map |
| 12 | orientation | `H_B` | oriented matching would still be a cross-action fit |
| 13 | preboundary geometry | `H_B` | the scalar column records rather than removes `lambda` |
| 14 | gauge/BV | `H_B` | descent preserves the full connection-valued carrier distinction |
| 15 | PDE/Green analysis | `H_B` | the native branch is not yet a coupled stationary solution/domain |
| 16 | cosmology | `H_B` | `I_sc` tracks `rho`; the native algebraic branch does not |
| 17 | exact computation | `H_D` | the cubic obstruction and unique cancelling `q` are exact |
| 18 | model selection | `H_B` | `H_B` adds no fitted coefficient beyond declared translation data |
| 19 | hostile falsification | `H_C` | strict separation is the safe coefficientwise consequence of (6) |
| 20 | program strategy | `H_B` | native `I1B` can advance without pretending the observed bridge closed |

Vote:

```text
H_A  0
H_B 15
H_C  2
H_D  3
```

The highest-conviction conclusions are not merely the plurality result:

1. **Exact variational conviction:** `H_A` is refuted for every nonzero affine
   bridge by (6).
2. **Source-semantic conviction:** the full parameterized-torsion carrier is
   the intended dark-energy candidate; the source does not select `Phi1` or
   normalize its coefficient.
3. **Custody conviction:** `I_sc` coefficients cannot be imported into `I1B`
   cubic assembly.
4. **Constructive conviction:** `H_D` remains a real mathematical reopening,
   but only when a source/action/observation theorem independently owns its
   scalar second jet.

## 7. Reverse scaffold for the next series of swings

Retaining Variancer's reverse conditional from the superposition hypothesis:

```text
S0 superposition hypothesis:
   the observable interaction is carried by one native parameterized-torsion
   theory whose radial and TT projections must be derived from I1B.

S1 reverse condition:
   if an observed scalar translation is requested, keep
   delta T=lambda delta theta_obs Phi1 with lambda explicit.

S2 native assembly:
   set no cross-action coefficient equalities; compute
   D3(I1B o F_native)[t,h,v] using the owned DB_LC and D2B_LC jets.

S3 coefficient custody:
   separate intrinsic T cubic, induced Levi-Civita geometry, moving pairing/
   density/Shiab, direct curvature terms, observation, and preboundary class.

S4 cancellation test:
   determine the complete native t-h-h, t-h-v, and t-v-v coefficients and
   whether any vanish or cancel before quotient.

S5 translation family:
   only after S4, report observed coefficients as lambda times native ones;
   do not choose lambda by fitting I_sc.

S6 reopening condition:
   replace conditional lambda or add nonlinear q only with an independently
   derived observation/action map and compatible stationary family.

S7 later:
   unique pencil, spectral connection, common Green domain, BFV reduction and
   2D-to-98D attachment remain downstream.
```

## 8. Next gates

1. **K122:** complete the native `I1B` pullback cubic and preboundary owner
   decomposition on `(t,h,v)`, with `t` the native `Phi1` coefficient. Report
   any observed translation only as the family parametrized by `lambda`.
2. **K123:** if K122 fixes a native pencil, test its spectral owner and common
   domain without importing the `I_sc` horn.
3. **Reopen the scalar bridge** only if a source/action observation theorem
   supplies a normalized linear map, or a nonlinear scalar second jet and a
   compatible coupled stationary background.

No ledger, datum, quotient, canon, public posture, particle interpretation,
phenomenology or GU truth-status claim changes.

Exact probe: `38/38`.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k121_rsap_scalar_role_action_germ_and_conditional_bridge_gate_probe.py
```
