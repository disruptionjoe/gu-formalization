---
artifact_type: exploration
created: 2026-08-03
title: "Generic-native q6 exists; the tilted moving source port is still a schema"
grade: "Exact sparse Cl(9,5) algebra on all 16384 blades and all 8256 native adjoint blades, independent Sage D7 multiplicities, exhaustive 252-image exterior projector, native 128x128 K/right-H mover control, exact rational chosen-A0=0 tilted-jet group-law fixture, and explicit variational/global fences. The combined local Psrc(T_omega), public U-type to native-Sp reduction, actual Theta_Z/Zorro nonconstant descent, global density/Krein Riesz, source variation domain, total Euler, domain, no-leakage, VEV, mass, index, and count remain open."
named_gate: RESOLVER-WAVE-G-Q6-NATIVE-SP-TILTED-SOURCE-PORT-AND-TRANSVERSE-EULER
gate_before: OPEN_REBASED_COMPONENT_PROJECTOR_BUILT
gate_after: PARTIAL_NATIVE_Q6_AND_LOCAL_TILTED_SCHEMA_CONSTRUCTED
route_disposition: CONTINUE
source_collision: SOURCE-CONFIRMS-TILTED-TENSORIALITY_SOURCE-SILENT-NATIVE-Q6
canon_verdict_change: none
third_lane_promoted: false
---

# Resolver Wave G: generic-native `q6` and the local tilted-source schema

## Result first

Wave G closes the algebraic gap that Wave F exposed. At a fixed native
`Cl(9,5)` reduction, the grade-six projection acts directly on a generic
native adjoint coefficient. It does not require the input to arrive already
written as an exterior six-form.

Let

\[
  \mathcal N(X)=\sum_{a=1}^{14}c(e_a)Xc(e^a).
\]

On Clifford grade `r`,

\[
  \mathcal N\big|_{\Lambda^r}=(-1)^r(14-2r).
\]

The native adjoint contains the seven grades

\[
  R_{\rm ad}=\{2,3,6,7,10,11,14\},
\]

whose `N`-eigenvalues are respectively

\[
  10,-8,2,0,-6,8,-14.
\]

They are distinct, so the exact native coefficient projector is

\[
 \Pi_6^{\rm ad}
 =\frac{(\mathcal N-10)(\mathcal N+8)\mathcal N
 (\mathcal N+6)(\mathcal N-8)(\mathcal N+14)}{122880}.
\]

Composing its Chevalley grade-six symbol with Wave F gives

\[
  P_{252}^0
  =j_5\frac19\pi_{\Lambda^5V^*}\delta\,q_6.
\]

This is an exact rank-252 projector from a **generic native** adjoint-valued
one-form at a fixed chimeric split. It is not yet a map from the public
complex source bundle, because the public-to-native real-form reduction and
global Zorro/coindex transport remain unbuilt.

The source group law also yields a real local construction advance. In a
chosen local `A0=0` specialization of the reconstructed semidirect
convention, with ordinary local first-jet derivative `d`, take

\[
  (\epsilon_1,\varpi_1)(\epsilon_2,\varpi_2)
  =\left(\epsilon_1\epsilon_2,
  \operatorname{Ad}(\epsilon_2^{-1})\varpi_1+\varpi_2\right),
\]

\[
  \tau(h)=(h,h^{-1}dh),\qquad
  T_\omega=\varpi-\epsilon^{-1}d\epsilon,
\]

exact rational first jets prove

\[
 T_{\tau(h)\omega}=T_\omega,
 \qquad
 T_{\omega\tau(h)}=\operatorname{Ad}(h^{-1})T_\omega.
\]

The executable verifies the semidirect-product associativity and the
homomorphism law for `tau` in this convention. The left tilted factor then
cancels and the right factor acts tensorially. An untilted left action and
the wrong Maurer--Cartan side both fail as planted controls. This is an exact
local `A0=0` convention fixture, not yet the bridge to the draft's general
`tau_(A0)` formula or the actual `Y14` double-coset bundle.

The strongest honest local moving **schema** is therefore

\[
 P_{\rm src}(\epsilon,\Theta)
 =(Z_\Theta^{-1}\otimes\iota^6_\epsilon)
 P_{\rm ext}^0
 (Z_\Theta\otimes q_{6,\epsilon}),
\]

conditional on an actual native coindex map and local adapted Clifford lift.
Wave G does not instantiate this composite or feed `T_omega` through it.
It uses the intrinsic chimeric split

\[
  \mathcal C=V_{10}\oplus\pi^*T^*X_4
\]

rather than asking the coarse Clifford plane or `epsilon_src` to invent the
`4+10` split. `Theta_Z` transports the coindex geometry; source `epsilon`
moves the Clifford image by conjugation.

The exact non-Spin mover is decisive. For

\[
 X=(e_0+e_3)e_4e_5,\qquad X^2=0,\qquad
 g=1+\tfrac12X,
\]

the native 128-by-128 matrix is K-anti/right-H at the infinitesimal level and
`g` is K-unitary. On

\[
 A=e_0e_1e_2e_3e_4e_5,
\]

exact Clifford algebra gives

\[
 \operatorname{Ad}_gA=A-e_1e_2e_3-e_0e_1e_2.
\]

Consequently

\[
 q_6^0\operatorname{Ad}_gA\ne
 \operatorname{Ad}_gq_6^0A.
\]

A fixed grade-six projector is not full-`Sp` equivariant. The moved family

\[
 q_6^g=\operatorname{Ad}_gq_6^0\operatorname{Ad}_{g^{-1}}
\]

restores covariance and remains idempotent. This is not a failure of the
construction; it tells us precisely what the source/moving reduction must
own.

The gate moves

```text
OPEN_REBASED_COMPONENT_PROJECTOR_BUILT
  -> PARTIAL_NATIVE_Q6_AND_LOCAL_TILTED_SCHEMA_CONSTRUCTED
```

with route decision `CONTINUE`. The next gate begins by instantiating the
combined local `Psrc(T_omega)`, then attempts global native reduction,
adapted `Theta_Z` descent, and the total active/transverse Euler port—not
another isolated projector.

## Layer 0: the objects that must remain separate

| Object | Type | Wave G status |
|---|---|---|
| public source field | `T_omega in Omega1(Y,ad P_H)` | source-confirmed |
| native local source coefficient | `C* tensor sp(32,32;H)` | conditional on unbuilt public/native reduction |
| Clifford symbol | exterior expansion inside `Cl(9,5)=M(64,H)` | fixed native reduction only |
| `q6(T)` | `C* tensor Lambda6 C*` | constructed locally |
| effective active component | rank-252 image of `Pext q6` | constructed locally at fixed split |
| contracted five-form kernel | real `Lambda5 V*`, K-self | not a connection coefficient |
| source `epsilon` | gauge-group field in tilted source geometry | identity with `epsilon_IG` source-silent; kept Layer-0 distinct until a map exists |
| `Theta_Z` | coindex/Zorro transport owner | no actual global overlap data yet |
| diagnostic Euler split | `Pi*E` and `(1-Pi)*E` | formula only |
| restricted-action Euler | includes `(D Pi[delta rho]T)^*E` | not assembled |

In particular, a local native `q6` is not the public source port, a real 252
is not either complex 126 half alone, and a projected Euler equation is not a
consistent truncation.

## What exact computation established

### 1. Exhaustive Clifford-number certificate

The sparse rational implementation checks all `2^14=16384` Clifford blades.
The number-operator eigenvalue formula holds without exception. The native
coefficient dimensions are

| grade | 2 | 3 | 6 | 7 | 10 | 11 | 14 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| dimension | 91 | 364 | 3003 | 3432 | 1001 | 364 | 1 |

Their sum is `8256`. The projector fixes all 3,003 grade-six blades and kills
all 5,253 other native blades. An inverse-blade trace comparator independently
recovers every retained coefficient.

For one-form values:

\[
 \dim\operatorname{dom}=14\cdot8256=115584,
\]

\[
 \operatorname{rank}q_6=14\binom{14}{6}=42042,
 \qquad \dim\ker q_6=73542.
\]

After `Pext`, the rank is 252 and the composite kernel has dimension 115,332.

The fixed coefficient projector is self-adjoint for the invariant diagonal
Clifford coefficient pairing and commutes with grade involution, reversion,
and Clifford conjugation. This is a local coefficient-pairing result. It does
not replace the unbuilt global density/Hodge/Krein Riesz map.

### 2. Spin equivariance does not select the map

An independent Sage 10.9 `D7` character calculation finds

\[
 \dim\operatorname{Hom}_{\Spin(14)}
 (\Lambda^6,\Lambda^6)=1,
\]

but for one-form intertwiners it finds five routes into
`C* tensor Lambda6 C*`:

| input coefficient grade | 2 | 3 | 6 | 7 | 10 | 11 | 14 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| Hom multiplicity | 0 | 0 | 4 | 0 | 1 | 0 | 0 |

The four grade-six amplitudes arise from the four irreducible summands of
`C* tensor Lambda6 C*`. Grade ten supplies a fifth, Hodge--wedge near-miss
landing in the `Lambda5` summand. Therefore equivariance alone is
insufficient. The coefficientwise conditions

1. identity on every grade-six simple tensor, and
2. annihilation of every other native coefficient grade

are load-bearing. The executable plants grade ten as a mandatory zero.

### 3. Fixed-pairing adjoint of the rank-252 projector

Wave G upgrades Wave F's adjoint status. For the fixed trace-reversed split,
`j5` and `delta` are exact signed adjoints, `pi_(Lambda5 V*)` is orthogonal,
and

\[
 P_{\rm ext}^0=j_5\frac19\pi_{\Lambda^5V^*}\delta
\]

is self-adjoint and idempotent for that fixed tensor pairing. All 252
internal five-blade images are checked. The normalization remains `1/9`, not
the internal-only `1/5` comparator.

The useful shortcut

\[
 \delta q_6(T)
 =\sigma_5\pi_5\left(\sum_\mu c(e^\mu)T_\mu\right)
\]

passes on a mixed native input because the native adjoint has grade six but
not grade four. A planted non-adjoint grade-four coefficient contaminates the
shortcut, proving that the native-domain qualification matters.

### 4. Chosen-convention tilted law and frame-surrogate schema

The executable uses an arbitrary `GL(2)` frame surrogate `s_ref` and defines

\[
 F=\epsilon^{-1}s_{\rm ref}.
\]

Under a left tilted representative change, transform both fields:

\[
 \epsilon' = h\epsilon,\qquad s'_{\rm ref}=hs_{\rm ref}.
\]

Then `F'=F` and `T'=T`. Under a right tilted change,

\[
 \epsilon'=\epsilon h,\qquad s'_{\rm ref}=s_{\rm ref},
\]

so

\[
 F'=h^{-1}F,\qquad T'=\operatorname{Ad}(h^{-1})T.
\]

These identities are a `GL(2)` transformation-law fixture only. The
surrogate does not satisfy Clifford relations, does not act in `q6/Pext`,
and is not `Theta_Z`. If an actual adapted Clifford lift exists with the same
transformation law, the candidate local family would be

\[
 q_6^F(T)=\operatorname{Ad}_F
 q_6^0(\operatorname{Ad}_{F^{-1}}T)
\]

The combined covariance of this candidate with `Pext` and `T_omega` is
**not tested**. The executable proves only the separate moving-`q6`, tilted
`T_omega`, and `GL(2)` surrogate identities. The rational matrices are not
the actual `Y14` transition functions.

## First-variation consequence

For a genuinely restricted field

\[
 Q=\Pi_\rho T,
\]

the variation is

\[
 \delta Q=\Pi_\rho\delta T+
 (D_\rho\Pi_\rho[\delta\rho])T.
\]

The first term gives the pulled active covector; the second is a moving-frame
moment term. Fixed `q6` and fixed `Pext` are zero-order and add no independent
Green current. The source root

\[
 \delta T=\alpha-D_B\xi
\]

does add one derivative in `epsilon` and therefore owns a formal-adjoint
boundary term. If `Theta_Z` is derived from a metric/connection jet, its
moving projector may add further derivative and Riesz terms.

Merely decomposing an already computed Euler covector is different:

\[
 E_{\rm active}=\Pi_\rho^*E_T,
 \qquad
 E_\perp=(1-\Pi_\rho)^*E_T.
\]

That diagnostic split adds no chain term. Consistent truncation requires both
the active and transverse equations. Observation additionally still requires

\[
  R E_Y L=E_X,
  \qquad
  (1-LR)E_YL=0.
\]

`RL=1`, local descent, or projected Euler success alone proves neither.

## What is still missing

1. **Public-to-native reduction.** The source is publicly typed in a complex
   U-type group, while this construction begins only after a native
   `Sp(32,32;H)` reduction. The bundle morphism and total Euler tangency to
   its fixed locus are open.
2. **Actual `Theta_Z` port.** The intrinsic chimeric split is the right owner,
   but the actual coindex direction, adapted Spin/native lift, nonconstant
   transition maps, triple-overlap cocycle, and global obstruction class have
   not been constructed.
3. **Density/Krein adjoint.** Fixed coefficient pairings are complete; the
   global Hodge/Krein lowerer and its variation are not.
4. **Source field space.** The repo's primary-source locator still grades the
   admissible `(epsilon,varpi)` variation domain `UNDECLARED`.
5. **Total action.** The actual moving Shiab term, complete fermion residual,
   barred/unbarred variations, `P0/rho/Y_K/Y_C/C` placement, active and
   transverse Euler equations, Ward identity, Green form, quotient, domain,
   and observation no-leakage remain open.

These are construction requirements generated by the object just built.
They are not reasons to discard the route, and they may not be filled by
declaring an external datum.

## Source collision

The silence ledger is scoped to three enumerated local source surfaces: the
2021-draft reconstruction in `gu-paper-reference-surfaces.md` and
`paper-formalization-candidates.md`, the Portal/Oxford transcript at
`01:12:17--01:13:55`, `01:34:00--01:34:34`, and
`02:26:23--02:29:23`, and the primary-source pack's WGS-06/WGS-07 audit.
None contains `q6`, `Pext`, or a native-`Sp` reduction. This is a bounded
source-silence statement, not a claim about every possible Weinstein source.
Portal `01:12:17--01:13:55` directly owns the intrinsic chimeric `10+4`
split and connection-dependent identification with `TY`; it does not supply
the Wave-G `GL(2)` surrogate as an actual lift.

| Claim | Primary/source status | Wave G use |
|---|---|---|
| `T_omega=varpi-epsilon^-1 d0 epsilon` | `SOURCE-CONFIRMS` | exact `A0=0` specialization fixture; general `tau_(A0)` bridge open |
| tilted subgroup/double-coset role | `SOURCE-CONFIRMS` | left-basic/right-adjoint schema |
| source epsilon equals `epsilon_IG` | `SOURCE-SILENT-ON-IDENTITY / LAYER-0-UNCERTAIN` | kept distinct until a map exists |
| intrinsic chimeric `V plus pi*T*X` split | `SOURCE-CONFIRMS` | split owner; not invented by epsilon |
| native `Sp` reduction | `SOURCE-SILENT` | remains open |
| coefficientwise `q6` | `SOURCE-SILENT` | reconstruction result |
| exact `Pext` and `1/9` | `SOURCE-SILENT` | reconstruction result |
| full source variation domain | `SOURCE-SILENT/UNDECLARED` | blocks total Euler promotion |

No source silence is used as a no-go.

## External datum ledger

P1/P2/P3 remain unchanged and unused. The local projector and the separate
tilted-law fixture are constructed without them. An external datum may
eventually select among
globally admissible reductions or domains. It cannot create the missing
public/native bundle map, global lift, BV differential, Euler closure, or
analytic domain.

## Next gate

**`RESOLVER-WAVE-H-PUBLIC-NATIVE-REDUCTION-THETA-Z-DESCENT-AND-TOTAL-EULER`**:

1. instantiate and test the combined local `Psrc(T_omega)` under a genuine
   non-Spin moving Clifford frame and both tilted actions;
2. construct or obstruct the public U-type to native right-H `Sp` bundle
   reduction and prove total Euler tangency;
3. instantiate the actual `Theta_Z` coindex map, adapted transitions, and
   nonconstant three-overlap descent for the moving `Psrc`;
4. construct the density/Krein adjoints and differentiate the whole port;
5. join it to the displayed first source action without importing the rival
   residual-square or N1 bridge as if source-owned;
6. derive active plus transverse Euler, Ward/Green data, and the observation
   no-leakage condition.

If the bundle reduction Hom-space is zero or global lift is obstructed, Wave
H returns a scoped obstruction. Otherwise it must produce the first global
source-to-active port before any further local representation refinement.

No stationarity, mass, VEV, anomaly solution, index, generation count,
cosmological prediction, domain, or public-posture change is claimed.
