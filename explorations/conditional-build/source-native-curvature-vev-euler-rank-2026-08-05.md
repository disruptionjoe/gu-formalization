---
artifact_type: construction_result
created: 2026-08-05
status: AMBIENT_ACTION_COUPLING_AND_RANK_EXACT__OBSERVED_RECEIVER_AND_NATIVE_BV_OPEN
ledger_rows: [LT-GR1b, LT-GR2b, LT-GR2c, LT-GR2d, LT-SM8]
fork_assumed: SIGNATURE_AMBIENT_K77__SELECTED_DISPLAYED_SHIAB_COMM_SYMI_SYMI
search_space_dim: "zero selector parameters; complete 1+104+3080 ambient Riemann decomposition and 196-dimensional Cl1 distortion receiver"
free_object_delta: 0
source_return: SOURCE-CONFIRMS
scripts:
  - tests/channel-swings/source_native_curvature_vev_euler_rank_probe.py
  - tests/channel-swings/source_native_curvature_vev_euler_rank_independent.sage
registry: lab/process/source-native-curvature-vev-euler-rank.json
---

# Source-native curvature/VEV Euler coupling and rank

## Result first

The smallest source-native coupling did not need to be invented. It is already
present in the K77 two-connection action once the source's movable dark-energy
field is typed as the connection difference `T=A-B` and the action is varied
rather than read from its printed endpoint.

At the homogeneous linearized value locus, the actual `T` equation couples
the selected ambient Einstein curvature to the distortion with exact
curvature-covariation rank **105**. Its complete tested `Cl^1` Euler block has
rank **196** because 91 further `T` directions have no ambient-Riemann
curvature partner and are constrained by the invertible Krein/Hodge gain term.

This is genuine construction progress, but it is not yet the physical
dark-energy map:

- the independent `B` variation adds no second algebraic value equation at
  `T=0`; it is a derivative/commutator equation away from that locus;
- the selected post-Shiab route erases a rank-10 observed Einstein sector;
- the actual odd BV tangent differential is still unbuilt, so the native
  quotient rank is **undefined**, not zero; and
- an independent vacuum shift is transferred into `T` but not screened, and
  the free gain leaves the common normalization unexplained.

The source's limited “two problems to one” claim therefore has an exact
ambient action realization. The stronger observed-curvature, magnitude and
radiative-stability claims remain open.

## Pre-wave disposition and ten inline lenses

The pre-wave answers were fixed in the governed Run Plan: K77 plus the selected
displayed Shiab, no coefficient search, and zero new free objects. Ten compact
specialist lenses then set the calculation order:

1. differential geometry required `theta` and `T` to be compared as
   connection differences before any tensor receiver;
2. the variational bicomplex required independent `B` and `T` variations;
3. representation theory selected the complete `1+104+3080` decomposition;
4. Krein geometry used only invertibility of the pseudo-musical, not
   positivity;
5. gauge/BV theory prohibited assigning a quotient rank without the odd
   differential;
6. homological algebra separated the even Ward identity from BV cohomology;
7. hyperbolic PDE fenced a homogeneous value rank from a principal-symbol or
   well-posedness theorem;
8. observer geometry separated ambient `G_14` from observed `G_4`;
9. cosmology required the independent vacuum-shift control; and
10. exact-computation engineering required a second Sage/QQ reconstruction
    and planted failures for every tempting promotion.

## Source collision and Layer 0

The April 2025 seminar states, at `00:23:02--00:27:00`, that the equivariant
connection distortion replaces `Lambda g`, that a curvature term and the
dark-energy term sit across an equality, and that the latter is not constant
but a field capable of acquiring a VEV and responding to curvature. The
Keating interview separately confirms the two-movable-fields/two-problems-to-
one magnitude argument. **Source return: `SOURCE-CONFIRMS`.**

The source does not publish the action, select the K77 displayed Shiab, define
the observed equation dual, or construct BV. Those are reconstruction results
and open burdens, not source attributions.

| phrase | object used here | not identified with |
| --- | --- | --- |
| source `theta_omega` | `pi-Ad(epsilon^-1)B`, an `Omega^1(Y,ad P)` connection difference | `Lambda g`, its VEV, its stress tensor, or a vertical SFF proxy |
| action `T` | `A-B(epsilon)` in the same tilted trivialization | Euler covector `E_T` |
| `barF` | path-average `F_B + 1/2 D_B T + 1/3 T^2` | `F_A` or observed curvature |
| selected curvature receiver | `S|Riem=-2G_14` | pre-Shiab Gauss receiver or `G_4` |
| action Euler | variation of the one action | the printed endpoint or its derivative |
| vacuum shift | an independent source `rho_vac` | a gauge transformation or fitted gain |

Thus `theta` and `T` are the same connection-difference object up to the
named tilted trivialization. The older curvature-locked vertical-SFF ansatz is
a downstream proxy on another carrier and is not used in this proof.

## The one action and both variations

The relevant bosonic shell is

\[
 I[B,T]=\langle T,S(\bar F)\rangle
       +\frac{\kappa_1}{2}\langle T,*T\rangle,
 \qquad
 \bar F=F_B+\frac12D_BT+\frac13T^2.
\]

The repository's exact first-variation result is

\[
 E_T=S(\bar F)+(D_T\bar F)^!S^!T+*\kappa_1T. \tag{1}
\]

Holding `T` fixed and varying `B` gives, up to the already-fenced adjoint and
left/right sign conventions,

\[
 E_B=D_B^!S^!T+\frac12\operatorname{ad}_T^!S^!T. \tag{2}
\]

Equation (2) matters globally and at nonzero jet order. But at the homogeneous
value locus `T=0`, its algebraic Jacobian is zero. It is not a second
independent value equation that fixes the common amplitude.

Linearizing (1) at the same locus leaves the value block

\[
 \delta E_T=C\,\delta R+\kappa_1K\,\delta T,
 \qquad C=S|_{\mathrm{Riem}}, \tag{3}
\]

where `K` is the nondegenerate Krein/Hodge flat map.

## Exact rank theorem

For ambient fourteen-dimensional algebraic Riemann curvature,

\[
 \mathrm{Riem}_{14}=\mathbf 1\oplus\mathrm{Ric}_0\oplus W,
 \qquad 3185=1+104+3080.
\]

The selected displayed Shiab obeys `C=-2G_14`, hence

\[
 \operatorname{rank}C=105.
\]

On the tested `Omega^13 tensor Cl^1` receiver, `dim T=196` and `K` is
invertible. For fixed nonzero `kappa_1`,

\[
 \operatorname{rank}[C\;\kappa_1K]=196.
\]

The interpretation is not “196 curvature modes.” It is:

| block | rank | meaning |
| --- | ---: | --- |
| ambient curvature covariation | 105 | scalar plus traceless-Ricci curvature tracks 105 `T` directions |
| `T`-only complement | 91 | direct gain constrains `T` with no Riemann curvature partner |
| total homogeneous `T` Euler | 196 | sum of the two blocks |

At `kappa_1=0`, total rank drops to 105. If `kappa_1` is itself free, it adds
one variable without adding an equation; the relation does not select its
normalization.

## What survives Bianchi, Ward, BV and observation

At this algebraic value grade, the ambient Einstein contraction discards the
3080-dimensional Weyl kernel and is exact on the 105-dimensional scalar/Ricci
quotient. The even Ward owner is derivative-valued, so its homogeneous
zero-jet row has rank zero. That does not mean the global Ward equation is
absent; it means it cannot be counted again as an independent field-value
constraint here.

No native odd BV tangent differential has been constructed on this action and
receiver. Therefore the requested **BV quotient rank is undefined**. The only
honest bound before construction is that an induced physical covariation rank
cannot exceed 105. The global ledger continues to report zero quotients
ranked.

Observation is a separate and sharper obstruction. The exact existing theorem
is

\[
 \operatorname{rank}\left(G_4\operatorname{res}_H\mid\ker G_{14}\right)=10.
\]

Every observed symmetric two-tensor direction occurs on ambient curvature
that `S=-2G_14` erases. No post-Shiab map can recover it. The source's
physical “flatness/curvature” field therefore cannot yet be identified with
the ambient action variable. The live repair is the parameter-free pre-Shiab
Gauss/`II` receiver already built locally; the next wave must prove that the
same source action owns its equation dual.

This is not a test that secretly reinstates a fixed cosmological constant.
`Lambda g` spans only the one-dimensional metric-proportional direction, while
the kernel theorem concerns all ten components of an observed symmetric
two-tensor. The loss is caused by **contraction before restriction**, not by
the value or constancy of `Lambda`. But it would be circular to demand that
the new fluctuating geometry pass through that contraction-first receiver and
then treat failure as a failure of the fluctuating mechanism. Moving `T`, the
section, and the Gauss/`II` terms are precisely the additional geometry not
seen by the killed factorization. The theorem therefore redirects the build
to the complete pre-Shiab moving-observation Euler equation; it is not
negative evidence against that complete equation.

## Vacuum-shift control

On one paired active mode, add an independent vacuum source:

\[
 c+\kappa_1t+\rho_{\rm vac}=0. \tag{4}
\]

Its Jacobian has rank one. It reduces three values to two and gives

\[
 t=-\frac{c+\rho_{\rm vac}}{\kappa_1}.
\]

So `T` can respond to the shift, which is the dynamical/tracking content of
Weinstein's proposal. But `c` remains free. Keeping observed curvature fixed
requires a second independent curvature/vacuum-selection equation; the
homogeneous `B` variation has rank zero and does not supply it. The present
action therefore tracks the shift but does not screen it or derive the
observed scale.

## Constraint and residue accounting

| quantity | result |
| --- | ---: |
| selector parameters searched | 0 |
| new free objects | 0 |
| ambient paired field values | `105+105` |
| independent paired equations at fixed nonzero gain | 105 |
| extra `T` constraints | 91 |
| free gain | 1 existing continuous parameter |
| native BV quotients ranked | 0 |
| global residue movement | none |

The ambient paired block realizes “two values to one” before physical
observation and BV. Because those two interfaces remain open, no global
parameter or function-valued residue is retired.

## Seven-axis audit

| layer | disposition |
| --- | --- |
| Layer 0 | source `theta`/action `T` same object up to tilted trivialization; ambient/observed receivers distinct |
| L1 source | `SOURCE-CONFIRMS` the two terms, equality, dynamism and VEV; action formula remains reconstruction |
| L2 algebra | complete `1+104+3080` decomposition; exact ranks 105 and 196 |
| L3 geometry | ambient selected-Shiab map exact; pre-Shiab observed Gauss owner open |
| L4 variation | both `B` and `T` rows written; homogeneous independence counted honestly |
| L5 covariance | Bianchi and even Ward typed; odd BV differential open |
| L6 analytic | homogeneous finite rank only; no closed Green/domain theorem |
| L7 physics | no magnitude, radiative solution, `w(z)` or observed dark-energy claim |

## Hostile review outcome and next gate

The two-sided review is recorded in
`lab/process/hostile-reviews/2026-08-05-source-native-curvature-vev-euler-rank-review.md`.
It rejected both promotion of ambient rank to solved cosmology and defense of
the superseded claim that the post-Shiab route kill means no curvature
coupling exists.

Next gate:

```text
CONSTRUCT_ACTION_OWNED_PRE_SHIAB_GAUSS_CURVATURE_TO_T_EULER_RECEIVER_AND_NATIVE_BV_QUOTIENT
```

It must derive the moving observation-jet equation dual of the pre-Shiab
Gauss/`II` receiver from the one K77 action, construct the actual BV tangent
differential, and recompute the induced observed curvature/`T` rank. Only then
may a nonzero vacuum branch and repeated shift test move `LT-GR2c/d` further.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/source_native_curvature_vev_euler_rank_probe.py

DOT_SAGE=/private/tmp/gu-source-native-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/source_native_curvature_vev_euler_rank_independent.sage
```

Main receipt: `3 source + 3 repo + 19 exact + 4 type + 9 planted = 38/38`.
Independent Sage/QQ reconstruction passes.

No P1/P2/P3, canon, public posture, Lane count or phenomenological claim
moves.
