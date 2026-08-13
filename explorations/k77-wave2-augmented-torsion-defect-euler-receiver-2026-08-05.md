---
title: "K77 Wave 2: augmented-torsion four-plus-ten defect Euler receiver"
date: 2026-08-05
status: PARTIAL_WITH_DECISIVE_ROUTE_SELECTION
named_gate: K77_ACTION_DERIVED_HORIZONTAL_EULER_IMAGE_OR_DEFECT_VARIATIONAL_RECEIVER
gate_before: K77_ACTION_DERIVED_HORIZONTAL_EULER_IMAGE_OR_DEFECT_VARIATIONAL_RECEIVER
gate_after: K77_FOUR_PLUS_TEN_DEFECT_EULER_RECEIVER_BUILT_LOCALLY__AUTOMATIC_HORIZONTALITY_KILLED_FOR_NONZERO_KAPPA_FULL_LOCAL_TRANSLATION_DOMAIN__FULL_MOVING_ACTION_WARD_BV_DESCENT_OPEN
route_disposition: PASS_WITH_DECISIVE_ROUTE_SELECTION_AND_SCOPE_FENCE
source_collision: SOURCE_CONFIRMS_CARRIERS_AND_PULLBACK_OBLIGATION__SOURCE_GUIDES_FOUR_PLUS_TEN_RETENTION__SOURCE_SILENT_ON_EXACT_RECEIVER
fork_assumed: SIGNATURE-AMBIENT
fork_horn: K77
search_space_dim: "0 selector parameters once the section and existing vertical coefficient restriction are fixed"
free_object_delta: 0
residue_touched:
  - "K77-W2-ACTUAL-Y14-RECEIVER: T3"
fork_stack_acknowledged: "The exact receiver is signature-independent after a section is supplied, while the local density/primalizer check uses the K77 trace-reversed metric. A K95 port would still require its carrier, pairing and transition report. No Eric/Curt source phrase is treated as an identity theorem."
probe: tests/channel-swings/k77_wave2_augmented_torsion_defect_euler_receiver_probe.py
registry: lab/process/k77-wave2-augmented-torsion-defect-euler-receiver.json
grade: "Exact fibrewise bundle and first-variation theorem along a supplied section, plus an exact local source-action counterexample to automatic horizontality for nonzero kappa on the displayed full translation domain. The complete nonlinear localized action, moving vertical density and section variation, tilted Ward/BV descent, common analytic domain and physics identification remain open."
---

# K77 Wave 2 augmented-torsion four-plus-ten defect Euler receiver

## Result in plain English

The source check resolves the preceding three-way fork enough to choose a
construction route. Eric's augmented torsion is a full fourteen-direction
connection one-form upstairs. Pulling it back to a four-dimensional observer
retains four connection components, but GU's existing vertical coefficient
map retains the other ten as scalar-like fields. Together those two maps are
an exact, parameter-free change of field coordinates along any supplied
section. Their inverse transpose then gives the unique equation receiver that
preserves the first variation: four connection equations and ten
vertical-field equations.

This also kills the simplest hoped-for shortcut. On the full local translation
domain displayed with the 2021 action, a nonzero quadratic augmented-torsion
coefficient can emit an entirely conormal Euler component. So the action image
is not automatically horizontal. The viable source-faithful path is now to
localize the **full action** on the observation defect while keeping both the
four pulled-back and ten vertical coefficients, then vary that moving system
and prove its Ward/BV descent. No new datum, projector or physical particle is
introduced.

## 1. Why this is movement rather than another restatement

The predecessor established three possible repairs for the rank-ten conormal
loss:

1. derive a horizontal source-action Euler image;
2. reduce/localize the full action on a codimension-ten observation defect and
   vary the reduced action; or
3. construct and type a ten-component normal receiver.

The source collision in
[`gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md`](../lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md)
shows that routes 2 and 3 are not independent inventions. N1 already defines
the two source-compatible defect fields

\[
A_X=s^*A,
\qquad
v_s=\operatorname{res}_s^V(A-A_0),
\]

and explicitly distinguishes vertical coefficient restriction from
differential-form pullback. The ten previously “untyped normal outputs” can
therefore be typed by an existing field map. What remains open is not their
carrier but their full action, symmetry, domain and physical role.

## 2. Pre-wave specialist assessment

Ten lightweight lenses were applied before constructing the map.

| lens | highest-information instruction |
| --- | --- |
| differential geometer | use the canonical splitting along a section before choosing a metric-normal complement |
| variational analyst | derive the equation receiver from the first-variation pairing, not from matching ranks |
| gauge engineer | keep the two-connection difference and test the tilted action on both output sectors |
| hyperbolic PDE specialist | do not discuss a Green domain until the complete equation carrier is fixed |
| symplectic/BV geometer | ask which tangent differential owns any quotient; normal does not mean gauge |
| representation theorist | preserve the vertical bundle as a bundle, not ten named Standard Model scalars |
| source archaeologist | collide “pullback” with the actual observerse and native/invasive grammar |
| exact-computation engineer | compute the complete map, inverse, pairing and adversarial conormal witness over rationals |
| systems engineer | retire the superseded generic receiver debt and propagate the replacement gate immediately |
| statistics/ML engineer | do not fit a selector: the relevant map space has zero selector parameters, so exact algebra dominates |

The pre-registered kill condition was: if `(s*,res_s^V)` is not faithful, or
if its equation dual does not preserve the whole first variation, do not
promote it. Both conditions pass exactly.

## 3. Layer 0 and source boundary

| object | type | not identified with |
| --- | --- | --- |
| augmented torsion `T_omega` | `Omega1(Y,ad P)`; difference of two connections | ordinary torsion or a four-dimensional tensor supplied in advance |
| `s* T_omega` | `Omega1(X,s*ad P)` | the complete restriction of all upstairs coefficients |
| `res_s^V T_omega` | `Gamma(s*V*Y tensor ad P)` | differential-form pullback or a physical Higgs multiplet |
| ambient Euler residual | density-dual 13-form / its primal one-form | augmented torsion itself |
| defect Euler receiver | dual of the complete defect field map | a gauge projector or BV quotient |
| vertical density/current | localization data for reducing the action | literal pullback of a 14-form |

The source confirms the carriers and the obligation to observe on `X`. It
guides retaining both horizontal and vertical connection components. It is
silent on the exact inverse-transpose receiver constructed below.

## 4. The canonical field map along a section

For the metric bundle `pi:Y->X` and any section `s`, there is a canonical
direct sum **along the image of the section**:

\[
T_{s(x)}Y=ds(T_xX)\oplus V_{s(x)}Y.
\]

The sum is direct because `d pi ds=1`, and every tangent vector `w` decomposes
as

\[
w=ds(d\pi w)+\bigl(w-ds(d\pi w)\bigr).
\]

Consequently a covector along `s` is completely determined by its value on
`ds(TX)` and on `V`. For adjoint-valued one-forms this gives the fibrewise
bundle isomorphism

\[
F_s=(s^*,\operatorname{res}_s^V):
s^*T^*Y\otimes s^*\operatorname{ad}P
\overset{\sim}{\longrightarrow}
T^*X\otimes s^*\operatorname{ad}P
\oplus
s^*V^*Y\otimes s^*\operatorname{ad}P. \tag{1}
\]

In local graph coordinates `ds=[I;J]`, the coefficient matrix is

\[
M=
\begin{bmatrix}
I_4&J^T\\
0&I_{10}
\end{bmatrix},
\qquad
M^{-1}=
\begin{bmatrix}
I_4&-J^T\\
0&I_{10}
\end{bmatrix}. \tag{2}
\]

The exact probe verifies `rank M=14` and `det M=1` for a nontrivial rational
section jet. Ordinary pullback alone kills the graph-conormal basis
`N=[-J^T;I]`; vertical coefficient restriction sends that same basis to
`I_10`. The combined map therefore retains exactly the information that
pullback alone erases.

This result needs no trace-reversed metric. The metric matters later for the
density/primalizer and K77 signature, not for the field isomorphism.

## 5. The Euler receiver is forced by variation

Write the defect variables as `q=M A`. At fixed section jet,
`delta A=M^{-1}delta q`. If `e_A` is the ambient Euler covector, equality of
the first-variation pairing for every `delta q` requires

\[
\langle\delta A,e_A\rangle
=\langle\delta q,e_q\rangle,
\qquad
e_q=M^{-T}e_A. \tag{3}
\]

Thus

\[
e_q=
\begin{bmatrix}
I_4&0\\
-J&I_{10}
\end{bmatrix}
\begin{bmatrix}e_H\\e_V\end{bmatrix}
=
\begin{bmatrix}
e_H\\e_V-Je_H
\end{bmatrix}. \tag{4}
\]

The four rows are the connection equation. The ten rows are the
vertical-scalar equation with the section-jet correction forced by the moving
field coordinates. The probe verifies rank fourteen, exact recovery
`M^T M^{-T}=I`, and equality of the complete variation pairing. Using `M^T`
instead of `M^{-T}`, omitting the `-J e_H` term, or dropping the ten rows all
fail planted tests.

This is a fibrewise equation-dual theorem, not yet the variation of the full
moving defect action. When `s`, the vertical density, Hodge star, Shiab and
connections vary, their derivatives must also be included.

## 6. The degree-correct four-plus-ten split

The ambient connection Euler density lies in degree thirteen. On the
four-plus-ten splitting there are exactly two possible bidegrees:

\[
\Lambda^{13}(H\oplus V)^*
\cong
\left(\Lambda^3H^*\otimes\Lambda^{10}V^*\right)
\oplus
\left(\Lambda^4H^*\otimes\Lambda^9V^*\right). \tag{5}
\]

Their dimensions are `4+10=14`. After pairing with a vertical density, the
first sector supplies a degree-three connection equation on `X`; the second
retains one vertical label and supplies a `V`-valued degree-four equation.
The exact top-form signs and the inverse-transpose field map preserve the
ambient variation pairing coefficient by coefficient.

Using densities rather than an oriented vertical volume consumes no P1. The
trace-reversed Frobenius metric supplies a local nondegenerate vertical
density, but its variation is part of the next gate.

## 7. Automatic horizontality is killed on the displayed local stratum

The 2021 bosonic source action contains

\[
\frac{\kappa_1}{2}\langle T_\omega,*T_\omega\rangle,
\qquad
\Upsilon^B_\omega
=\odot_\omega F_{A_\omega}+*\kappa_1T_\omega. \tag{6}
\]

Choose a constant augmented-torsion coefficient in one fixed Lie-algebra
generator and in the graph-conormal subspace:

\[
T_\omega=Nb,
\qquad N=[-J^T;I_{10}],
\qquad b\ne0.
\]

Locally `dT=0`; on a single commuting generator `[T,T]=0`; choose the
connection fixture so the curvature contribution vanishes. For
`kappa_1 != 0`, the action still emits `*kappa_1 T`. After the source-owned
primalizer, the Euler one-form is `kappa_1 T`: nonzero, conormal, invisible to
ordinary pullback, and visible to the vertical receiver.

Therefore

\[
Q R_Y\Upsilon_T=0
\]

is **not automatic** on the displayed full local translation domain when
`kappa_1` is nonzero.

The scope fence is essential:

- this does not prove that no source-derived constrained variation domain can
  exclude the fixture;
- `kappa_1=0` removes this witness but does not prove horizontality;
- the fixture is local and abelianized, so it does not establish global
  tilted descent or a physical solution; and
- it kills only automatic horizontality, not the augmented-torsion action.

## 8. The selected construction route

The most efficient next construction is now a weld of the existing pieces:

1. start with the complete source action `I1B`, not merely its advertised
   Euler endpoint;
2. use the existing defect fields `(T_X,v_T)` supplied by (1);
3. define a genuine codimension-ten current or induced vertical density, never
   literal pullback of the ambient 14-form;
4. include the moving support derivative already derived in N3;
5. vary the section jet, vertical density, Hodge/Krein map, Shiab, connection
   and both defect field sectors;
6. prove the tilted Ward/BV identity and patch descent for the entire reduced
   functional; and
7. only then impose a common closed Krein/Green domain and compare the emitted
   four-dimensional equations with physics.

The constructed receiver tells that action exactly where all fourteen Euler
components must go. It does not yet tell whether the ten vertical equations
are auxiliary, constrained, Higgs-like, massive, or propagating.

## 9. Seven-axis disposition

| layer | result |
| --- | --- |
| Layer 0 | pullback, vertical coefficient restriction, augmented torsion, Euler dual and localization are distinct |
| L1 | sources fix the full upstairs carrier and guide retaining both output sectors |
| L2 | exact algebra kills automatic full-domain horizontality for nonzero `kappa_1` on the displayed local stratum |
| L3 | `(s*,res_s^V)` and its four-plus-ten bundle carrier are exact and faithful along a supplied section |
| L4 | the inverse-transpose receiver preserves the full fibrewise variation pairing; full moving action variation is open |
| L5 | no normal direction is called gauge; tilted Ward/BV ownership remains open |
| L6 | no common closed Krein/Green domain or constraint propagation is claimed |
| L7 | no Standard Model, GR, dark-sector, particle, mass, generation or chirality row moves |

## 10. Accounting and boundary

| item | result |
| --- | --- |
| `search_space_dim` | `0 selector parameters once section and existing vertical restriction are fixed` |
| `free_object_delta` | `0` |
| new projector/datum | none |
| P1/P2/P3 | unchanged and unused |
| Curt | formally separate guidance inside Eric lane |
| Wave 3 | closed |
| claim/canon/public posture | unchanged |

The exact probe passes

`11 source + 28 type + 43 exact + 9 planted = 91/91`.

The hostile review verdict is

`PASS_WITH_MATERIAL_SCOPE_REPAIR__FULL_LOCAL_TRANSLATION_DOMAIN_AND_NONZERO_KAPPA_CONDITIONALIZED__DEFECT_LOCALIZATION_NOT_CLAIMED`.

## 11. Next named gate

`K77_FULL_SOURCE_ACTION_DEFECT_LOCALIZATION_MOVING_SECTION_WARD_BV_DESCENT`

Exit condition: one explicit, globally typed reduction of the complete source
action to the moving observation defect, using the four-plus-ten field map,
whose complete first variation reproduces the receiver above and whose tilted
Ward/BV identity and patch descent close. A failure must name the smallest
incompatible action term, density/current operation, symmetry identity or
domain—not demote augmented torsion or K77 wholesale.
