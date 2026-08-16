---
artifact_type: exploration
status: exploration
doc_type: conditional-contour-classification-gate
created: 2026-08-16
work_item: MC-2
channel: metric_cone_boundedness
title: "MC-2: a Gibbons-Hawking-Perry-style uniform phase does not repair SRC-3's full indefinite quartic"
grade: "EXACT root-of-unity and sign algebra on the banked SRC-3 rays K=-4 and K=+4, with a formal Euclidean-cycle horn only. No source action, Euclideanization, integration cycle, real structure, vacuum, measure, datum, analytic domain or physics is selected. A non-straight complex thimble is not excluded."
disposition: NO_SOURCE_REALITY_PRESERVING_UNIFORM_PHASE_REPAIR__NO_FULL_PRE_REDUCTION_UNIFORM_COERCIVITY__ISOLATED_NEGATIVE_RAY_HAS_COMPLEX_DECAY_WEDGES__POST_REDUCTION_REAL_CONTROL_SURVIVES__COMPLEX_THIMBLES_UNSELECTED_AND_OPEN
canon_verdict_change: none
steering_effect: unchanged
depends_on:
  - lab/active-research/joe-directed/majorana-126-neutrino/src3-potential-unbounded-below-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/src4-eddy-completion-cannot-rescue-the-potential-2026-08-15.md
  - lab/active-research/joe-directed/coset-versus-gauge/cg1-p-is-a-declared-coset-not-a-gauge-sector-2026-08-14.md
  - lab/active-research/joe-directed/metric-cone-boundedness/mc1-the-cone-does-not-bound-and-the-negative-direction-is-the-cone-itself-2026-08-14.md
  - explorations/conformal-factor-mode-gauge-status-2026-07-11.md
  - explorations/W122-spin0-gauge-vs-physical-auxfield-2026-07-13.md
scripts:
  - tests/channel-swings/joe_directed_mc2_ghp_quartic_contour_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result. Classification: `SOURCE_NATIVE_ROUTE`.

# MC-2 - exact contour classification

## Result first

The familiar substitution `z -> i z` can reverse a wrong-sign **quadratic**,
because `i^2=-1`. It cannot reverse SRC-3's negative quartic, because
`i^4=+1`. On the published ray,

```text
K=-4  ->  i^4 K=-4.
```

The smallest phase that does reverse a quartic is `z=e^(i pi/4)x`. It gives

```text
z^4=-x^4,
z^2= i x^2.
```

It therefore flips the quartic only by making the quadratic and every
bilinear kinetic term imaginary. More decisively, SRC-3 owns **both** a
negative ray `K_-=-4` and a positive ray `K_+=+4`. Under one uniform phase,
their real leading coefficients are

```text
-4 cos(4 theta),
+4 cos(4 theta).
```

Absolute Euclidean damping would require the first to be positive and the
second to be positive, hence simultaneously

```text
cos(4 theta)<0,
cos(4 theta)>0.
```

That is impossible. A scalar Gibbons-Hawking-Perry-style rotation repairs one
sign only by spoiling the other.

### Upstream custody

The `-4/+4` pair is not inserted as an unlabelled MC-2 premise. The MC-2 probe
runs and parses both upstream executable receipts:

```text
joe_directed_potential_boundedness_probe.py:
  SRC-3 pre-reduction ray = -4, timelike-leg control = +4

joe_directed_coset_versus_gauge_probe.py:
  pre-reduction = (-4,+4), post-reduction = (+4,+4)
```

Both predecessors must exit zero, expose the expected typed fields, and agree
on the pre-reduction pair before MC-2 evaluates any phase. The post-reduction
`(+4,+4)` pair is separately consumed as the CG-1 positive-pairing control.

This establishes

```text
NO_SOURCE_REALITY_PRESERVING_UNIFORM_PHASE_REPAIR
NO_FULL_PRE_REDUCTION_UNIFORM_COERCIVITY
```

It **DOES_NOT_PROVE_THAT_NO_COMPLEX_THIMBLE_EXISTS**. A non-straight
Picard--Lefschetz cycle can approach different decay sectors at its two ends.
Such cycles are not excluded here. They are additional global integration
data that neither the checked source nor the current repository construction
selects.

## Declared horn and Layer 0

This gate declares only the conditional formal object

```text
FORMAL-EUCLIDEAN-CYCLE:
  Z_Gamma = integral_Gamma exp(-V(z)) dz.
```

It does not say that GU uses a Euclidean functional integral. The following
objects remain distinct:

| Object | Meaning here | Not supplied here |
| --- | --- | --- |
| real classical boundedness | `V(x)` bounded below on the source real carrier | convergence on a complex cycle |
| pointwise phase | algebraic substitution `z=e^(i theta)x` | an integration cycle with endpoints and orientation |
| straight rotated slice | `e^(i theta)V_R` in the complexification | a Lefschetz thimble |
| original reality | the source/Krein antilinear involution and its real slice | a phase-modified reality |
| Euclidean damping | `Re V -> +infinity` on the ends of `Gamma` | Lorentzian pole or vacuum stability |
| pre-reduction pairing | SRC-3's Killing/DeWitt horn | CG-1's post-reduction positive pairing |
| first-order action | SRC-4's degree-one/two/three grammar | the eddy-squared second-order functional |

The missing owners are explicit:

```text
TYPE_MISSING[EUCLIDEANIZATION]
TYPE_MISSING[INTEGRATION_CYCLE]
TYPE_MISSING[CONTOUR_REALITY_STRUCTURE]
TYPE_MISSING[PATH_INTEGRAL_MEASURE]
TYPE_MISSING[PHYSICAL_DOMAIN]
```

## Multi-lens preflight and archaeology

1. **Complex-contour lens.** Test the real part of the highest-degree form on
   every asymptotic direction before discussing a saddle or vacuum.
2. **Degree-parity lens.** A GHP `i`-rotation is degree-sensitive: it flips
   degrees `2 mod 4`, not degree four.
3. **Convergence-sector lens.** One negative quartic ray can have complex decay
   sectors even when the full multidimensional form admits no uniform phase.
4. **Reality/Krein lens.** A convergent complex slice is not automatically the
   fixed set of the source antilinear involution.
5. **Source-custody lens.** The source confirms the eddy/quartic route, but not
   a Euclidean contour, measure or physical domain.
6. **Pairing-horn lens.** SRC-3's obstruction is pre-reduction; CG-1 supplies a
   distinct declared post-reduction horn where the quartic is nonnegative.
7. **GHP-scope lens.** W78 and W122 are scope prior art for a second-order
   Euclidean quadratic kinetic sign. They do not compute this quartic phase.
8. **Hostile-control lens.** Require a negative-quadratic positive control, a
   post-reduction positive-quartic control, a degree-six control, and live
   `K=-4/+4` rays.
9. **No-global-no-thimble lens.** A no-uniform-phase theorem must not be
   laundered into a theorem excluding nonlinear thimbles.
10. **Functional-level lens.** The first-order cubic and second-order quartic
    readings require separate convergence classifications.

The archaeology changes the target. W78/W122 already explain why GHP cannot
move a Lorentzian physical scalaron's tachyonic pole. MC-2 is not another pole
argument. Its new content is the exact degree-four phase obstruction on the
source-native SRC-3/SRC-4 potential.

## Exact quartic theorem

Let the formal Euclidean integrand be `exp(-V)` and restrict first to one ray,

```text
V(z)=-kappa z^4 + Q z^2,
kappa>0.
```

For `z=r e^(i phi)`, the quartic damps exactly when

```text
Re(-kappa z^4)>0
iff cos(4 phi)<0.
```

There are four decay wedges centered at

```text
phi=pi/4, 3pi/4, 5pi/4, 7pi/4,
```

with boundaries at odd multiples of `pi/8`. Thus the isolated negative ray
does admit formal complex decay directions.

The full pre-reduction potential is different. Because it has rays of both
quartic signs, one uniform phase must make both `K_- cos(4theta)` and
`K_+ cos(4theta)` positive. Their requirements contradict. This result uses
only SRC-3's exact `-4/+4` controls and no fitted coefficient.

### Pointwise sign is not a contour

The identity `V(e^(i pi/4)x)` has a favorable quartic sign on one ray. That is
only pointwise algebra. A legitimate contour additionally needs:

- a middle-dimensional cycle in the full complexified field space;
- endpoints in decay sectors for every asymptotic direction;
- an orientation and measure;
- compatibility with gauge orbits and the chosen reality condition;
- a prescription across Stokes walls; and
- a physical domain on which the resulting integral is meant to act.

None is owned. This gate therefore records the decay sectors and stops.

## Source reality and kinetic grammar

For the original conjugation `C`, the straight line `e^(i theta)V_R` is
preserved only if `e^(-2i theta)` is real. Hence `theta=0` or `pi/2` modulo
`pi`; both give `e^(4i theta)=1` and cannot flip the quartic.

The `pi/4` line can be made real only for a modified antilinear map such as

```text
C_theta=e^(2i theta) C.
```

That is a new reality horn, not the source reality. The same rotation sends a
bilinear kinetic or quadratic term to `i` times itself. It also complexifies
the real connection `A=B+T`. The rotated vector line is not a real Lie
subalgebra:

```text
[e^(i theta)X,e^(i theta)Y]
  =e^(2i theta)[X,Y],
```

which belongs to `e^(i theta)g_R` by a real scalar only when the phase itself
is real. A complex contour may still evaluate the holomorphic continuation of
the action, but it is not the original real source grammar silently repaired.

## Cubic first-order branch

SRC-4 keeps two functional levels separate. For its first-order branch, the
leading term on a ray is cubic. On a straight line through the origin, a real
nonzero cubic has opposite real signs at the two ends, so it cannot provide
strict damping at both.

The phase `theta=pi/6` makes a real cubic purely imaginary. The probe derives,
rather than inserts, the quadratic factor from the same exact root of unity:
`Re[(e^(i pi/6))^2]=cos(pi/3)=1/2`. A positive quadratic could then provide
damping. This is a genuine conditional control, not a solution: `flat_1` is
explicitly not a positive Riesz map, and the full quadratic composite, cycle
and domain are undeclared. A non-straight Airy-like contour is likewise not
excluded. A dedicated hostile mutation changes the derived `1/2` to `-1/2`
and must fail both the exact-factor and conditional-damping checks.

The first-order action also need not be minimized; SRC-4 already records that
its stationary-point content can be meaningful while it is unbounded. MC-2
does not turn boundedness into a health criterion for a first-order theory.

## Pairing-horn classifier

| Horn | Exact contour reading | Ceiling |
| --- | --- | --- |
| `PRE-E2-INDEF` | `K=-4/+4`; no uniform phase makes the full quartic damp | nonlinear thimbles open but unselected |
| `POST-E2-POS` | the CG-1 quartic is nonnegative on the real slice; no phase repair is needed | quartic-flat directions still require `kappa_1 flat_1 >= 0` |
| `POST-E2-FLAT-INDEF` | if the quadratic on quartic-flat rays has both signs, one uniform phase again faces incompatible `cos(2theta)` requirements | actual coercive domain remains missing |
| `E1-CUBIC` | no strict cubic damping at both ends of one straight line | an oscillatory cubic plus coercive quadratic, or a non-straight Airy contour, remains conditional |

The source currently selects none of these integration-cycle horns. The
pairing fork precedes the contour fork: under `POST-E2-POS`, the real quartic
already has the favorable sign; under `PRE-E2-INDEF`, a global scalar rotation
cannot repair it.

## Hostile review and controls

**Strongest overclaim, rejected.** "No convergent complex contour exists."
MC-2 does not establish this. Polynomial integrals can be defined on sums of
Lefschetz thimbles approaching different decay wedges. The exact result is
only that no original-reality-preserving **uniform straight phase** repairs the
full indefinite quartic.

**Strongest contrary construction, preserved.** A conjugate pair of nonlinear
thimbles may yield a real total integral even though neither thimble is the
source real slice. That possibility is not excluded. It requires precisely
the cycle, reality, measure and Stokes data listed as `TYPE_MISSING`.

**Controls.** The probe requires all of the following:

- `-x^2` is repaired by `x -> ix`, the genuine GHP-style degree-two control;
- `-x^4` is not repaired by `x -> ix`;
- `-x^4` is flipped by `x -> e^(i pi/4)x` on an isolated ray;
- `+x^4` converges on the real line and is spoiled by the same `pi/4` phase;
- degree six flips under `x -> ix`, proving the test follows degree modulo four;
- the cubic endpoint signs oppose on a straight line; and
- seven planted mutations attack the load-bearing degree, sign, reality,
  cubic, derived `pi/6` quadratic factor and post-reduction conclusions.

## Claim ceiling and reprioritization

MC-2 banks a narrow exact conclusion:

> The usual `z -> iz` GHP move cannot change a quartic sign. A general uniform
> phase can make SRC-3's isolated negative ray damp only by changing the
> quadratic/kinetic phase and the source reality, and no uniform phase can make
> the full pre-reduction `K=-4/+4` quartic damp in all directions.

It does not construct or select a source action, contour, Euclidean theory,
reality, vacuum, coefficient, measure, datum, physical quotient or domain. It
does not change SRC-3's conditional pairing scope, SRC-4's functional-level
fork, CG-1's post-reduction repair, W78/W122's physical-scalar result, canon or
public posture.

Within this path, contour work should now be deprioritized. Reopen it only when
an independently owned Euclideanization and integration cycle arrive. The
nearer source-native decision remains which functional level and which pairing
the physical construction uses.
