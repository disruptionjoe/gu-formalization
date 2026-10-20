---
title: "K1852: charged walls do not make affine vacuum compensation locally invisible"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional membrane charge, junction and topology constraints; no GU or nucleation theorem
---

# Vacuum-jump matching leaves a gravitating wall

Adding a charged membrane to K1850's affine top-form model permits a jump of
its cosmological multiplier. The bulk vacuum jump cancels exactly only when
`q=alpha*[rho]` in the declared orientation. A nonzero wall tension still
requires a jump of extrinsic curvature. Thus equality of the two bulk
cosmological terms does not mean the entire metric is unchanged.

Fixed charges preserve the old **uniform** constant-shift covariance but do
not compensate arbitrary independent shifts in adjacent regions. On a
connected region-adjacency graph only the common shift survives. A
quantized charge lattice adds a precise matching condition; a global current
must also be exact. An opposite-normal equal-curvature wall is retained as a
counterexample to an overbroad claim that no such wall can exist.

This is a classical conditional Einstein/multiplier/three-form/membrane model.
It is not GU's ad-valued connection or its observed metric equation.
SC-COS-50/51/54 and SC-ACT-01/02 remain ASSERTS; SC-META-53 UNCERTAIN.
LT-GR2c/2d, the source register, physics ledger and canon do not change.
No nucleation rate, probabilistic vacuum selection, causal relaxation,
quantum stability, numerical vacuum prediction or novelty is claimed.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: charge-matched bulk compensation, nonzero wall stress, connected-region shift restriction and global-current obstruction
carrier: real Lorentzian four-metric, piecewise constant vacuum sectors, scalar multiplier, three-form and timelike membrane LAYER=toy CHIRALITY=N/A
pairing: metric bulk and induced wall volumes plus oriented differential-form integration ON=real_classical_fields
real_structure: real fields and charges; unit spacelike wall normal
grading: differential-form degree and region labels, not GU grading
action_owner: repository-construction -- affine constrained Einstein action with explicitly added charged membrane
target: fixed-charge vacuum response and distributional metric junction data MAP-TYPE=evaluation
```

## 1. Scope, prior result and action

[K1850](k1850-metric-screening-ensembles-2026-10-20.md) already proves
that a smooth sourceless multiplier is constant; substituting C(x) for a
constant vacuum shift fails d(lambda)=0. This note tests one concrete repair:
an explicit charged timelike membrane, not another formal trace subtraction.
Charged-membrane unimodular models are established constructions; see
[Kaloper (2023), section4](https://arxiv.org/html/2305.02349#S4).
The calculation here fixes its own normalization and tests matching, not that
paper's semiclassical or statistical conclusions.

Let a timelike oriented wall Sigma separate regions minus and plus; n points
from minus to plus. Set [f]=f_plus-f_minus. Its distributional one-form
current delta_Sigma is defined by
`integral_M a3 wedge delta_Sigma=integral_Sigma a3`.
Choose the compatible transverse coordinate so
`d lambda=[lambda] delta_Sigma`. Use the fixed outer-A/flux ensemble of
K1850, standard Einstein boundary/junction terms, and

```
S= (K/2) integral R vol - sum_regions integral rho_i vol
   -integral lambda vol +integral (alpha lambda+beta)dA
   +q integral_Sigma A -T integral_Sigma vol_h,
K>0, alpha!=0, T>=0.                                     (1)
```

The vacuum constants label two phases; when the embedding is varied their
region volumes vary as well. A microscopic phase-field wall is not derived.
Use the thin-wall distributional limit with continuous induced metric h and
finite one-sided extrinsic curvatures. There are no other surface stresses,
curvature couplings or field-dependent tensions. All conclusions are within
this action/domain class. Global F may require patches as in K1850; local
variation formulas apply on a neighborhood of the wall.

## 2. The jump follows from varying A

The bulk variation at fixed outer tangential A is
`alpha integral delta A wedge d lambda`; the wall adds
`q integral delta A wedge delta_Sigma`. Thus

```
alpha d lambda +q delta_Sigma=0,
[lambda]=-q/alpha.                                       (2)
```

Variation of lambda still gives `vol=alpha F`. Away from the wall,

```
K G_munu=-(rho_i+lambda_i)g_munu,
R_i=4(rho_i+lambda_i)/K.                                 (3)
```

Consequently

```
[R]=(4/K)([rho]-q/alpha).                                (4)
```

Equal bulk curvature is equivalent to charge matching `q=alpha*[rho]`.
This is a relation among inputs, not a mechanism selecting q from arbitrary
rho. Reversing orientation reverses every bracket and q together and leaves
the condition invariant. The sign in (2) is pinned to the current definition;
copying another paper's sign without its orientation is invalid.

## 3. Equal bulk curvature does not erase the shell

The topological membrane coupling has no direct Hilbert stress. Its tension
term gives surface stress `S_ab=-T h_ab`. With the same normal convention on
both sides, distributional Einstein variation gives the Israel condition

```
[K_ab]-[Ktrace]h_ab=-(1/K)S_ab=(T/K)h_ab.
```

The wall has dimension3. Taking its trace and substituting back gives

```
[Ktrace]=-3T/(2K),       [K_ab]=-T h_ab/(2K).              (5)
```

Thus an unchanged smooth metric across a newly inserted wall, for which
[K_ab]=0, is impossible when T>0 under these assumptions. If comparing two
already-walled configurations with the same geometry, their **total** wall
stress must agree; a change of charge alone is not a proof it does. No
statement excludes equal-curvature but nonsmooth glued spacetimes.

The normal embedding equation is consistent with the distributional
conservation law. In particular when the total bulk vacuum jump vanishes,
a nonzero-tension wall must have zero mean trace extrinsic curvature
`bar Ktrace=(Ktrace_plus+Ktrace_minus)/2=0` (no other normal force).
This condition is also the normal Einstein constraint difference. It must be
checked in an existence example; bulk (4) alone is insufficient.

### A nontrivial equal-curvature countercontrol

For two zero-mass de Sitter regions with equal curvature parameter H²>=0,
let `f(R)=1-H²R²` and write a timelike spherical trajectory R(tau).
The angular Israel equation, in compatible sign convention, is

```
epsilon_minus sqrt(Rdot²+f_minus)
 -epsilon_plus sqrt(Rdot²+f_plus)=T R/(2K).                (6)
```

If the functions f and the signs epsilon are the same on both sides, the
left side is zero and T must vanish. But opposite signs
`epsilon_minus=+1, epsilon_plus=-1` yield

```
Rdot²=omega² R²-1,
omega²=H²+(T/(4K))²,
R(tau)=cosh(omega*tau)/omega.                             (7)
```

For T>0 this satisfies the unsquared equation: both radicals are
`T R/(4K)>0`. Its acceleration equation is Rddot=omega²R;
`(Rddot+f'/2)/sqrt(Rdot²+f)=T/(4K)` supplies the temporal Israel component.
The two one-sided extrinsic curvatures are opposite, with the required jump;
their mean trace is zero, so the matched-vacuum normal condition holds.
This is a different gluing/domain, with a distributional gravitating wall.
It is not the original smooth geometry and is not a construction of bubble
nucleation from specified initial data. It prevents a false universal
nonexistence inference from the same-sign branch.

## 4. Released successor: which shifts survive at fixed charges?

At a fixed metric and fixed wall geometry, change the phase potentials by
C_i. Bulk compensation requires lambda_i ->lambda_i-C_i. Equation(2) on
an edge e from i to j then requires

```
q_e_new=q_e+alpha*(C_j-C_i).                              (8)
```

If charges are fixed, C_j=C_i on every edge. On a connected finite adjacency
graph, the incidence matrix has kernel exactly the span of the constant
vector: walking along any path proves this without a rank guess. Therefore
only a common shift survives; different connected components can have
independent constants at the local-equation level, with their own global
boundary data still to be checked. Cycle sums of prescribed charge jumps
must vanish for consistent single-valued region multipliers.

A uniform C on the connected spacetime remains an exact covariance of (1),
even with membranes. Taking lambda->lambda-C changes the action only by
`-alpha C Phi` at fixed total flux; membrane charges and tension are unchanged.
This is not the same experiment as changing one phase independently. No
blanket loss of the earlier constant-shift result is claimed.

If allowed charges form q0 Z, the exact cancellation set for a single jump
is `[rho] in(q0/alpha)Z`. If the nearest integer charge can be chosen, the
smallest residual magnitude is
`dist(alpha*[rho],q0 Z)/abs(alpha)` and the scalar-curvature jump is4/K times
that quantity. With fixed q there is no minimization permission. Several
incommensurate charge generators may form a dense countable group, so a
universal positive spacing cannot be inferred; a countable group still does
not exactly match every real shift. Rates or reachability are separate.

## 5. Global current consistency and what remains open

With several walls, (2) gives
`alpha d lambda=-J`, where `J=sum q_e delta_Sigma_e`.
A globally single-valued real lambda implies J is exact as a distributional
one-form; in particular dJ=0 and all periods vanish. A single nonseparating
charged wall on a compact manifold with a loop crossing it once violates
this condition: integrating (2) around that loop yields0=-q.
On a transverse periodic circle a set of walls requires sum q_e=0, and then
a piecewise constant periodic lambda can be built by successive jumps.
This is a current/cohomology restriction, additional to each local matching
and metric junction; it is not a statement about every GU topology.

A zero-tension, charge-matched ideal interface evades the wall-stress
obstruction at the distributional level. A positive-tension opposite-normal
gluing evades the false claim that equal bulk curvature is impossible, while
retaining the shell. A microscopic matter realization, admissible tunnelling
process, charge spectrum, global flux sector and physical observation map
remain independent construction inputs. None is selected by (4).

## 6. Validation and inference boundary

Run `python3 tests/channel-swings/k1852_membrane_screening_junction.py`
and the corresponding `_probe.py`. Exact rational checks cover signs,
charge-matched and mismatched stationary traces, dimension3 junction solving,
graph/cycle consistency, lattice residuals and unsquared opposite-gluing
controls. Hyperbolic trajectory identities are checked through their defining
algebraic relation cosh²-sinh²=1; no floating time sampling certifies a solution.
Independent controls reimplement the formulas and inject wrong charge signs,
wall dimensions and normalization factors after a passing baseline. Reporting
fields are checked separately from those mathematical faults.

The written variational/distributional proof, thin-wall assumptions and full
junction/normal conditions own the continuum claim. Inline hostile review
checks source typing, fixed-charge versus charge-retuned experiments,
unsquared sign branches, wall stress, current topology and the distinction
between existence and dynamics. No separate-agent or formal verification is
claimed. The result narrows this proposed local repair; it does not change any
source assertion or identify a source-native metric adapter.
