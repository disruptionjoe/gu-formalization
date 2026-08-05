---
artifact_type: construction_result
created: 2026-08-05
status: ACTION_HILBERT_STRESS_RADIAL_TRANSGRESSION_EXACT__KREIN_DIRAC_STRESS_SYMMETRIC_CONSERVED__OBSERVED_NULL_10_TO_6_TO_2_RETAINED__REPAIRED_GRAVITY_DOUBLE_POLE__QUADRATIC_VACUUM_ZERO_INDEFINITE_ONLY
lane: "1"
functional_channels: [BUILD, SOURCE, COMPOSE, VERIFY]
fork_assumed: "SIGNATURE-AMBIENT=(7,7); OBSERVATION-FIRST PRE-SHIAB REPAIRED ACTION HORN"
search_space_dim: "zero selector parameters; action radial path fixed; observed Sym2 rank ten; exact four-component Lorentzian Krein-Dirac control"
free_object_delta: 0
ledger_rows: [LT-GR2b, LT-GR2c, LT-GR2d, LT-GR5, LT-GR6]
source_return: SOURCE-CORRECTS
scripts:
  - tests/channel-swings/observed_upback_stress_normal_constraint_vacuum_probe.py
  - tests/channel-swings/observed_upback_stress_normal_constraint_vacuum_independent.sage
registry: lab/process/observed-upback-stress-normal-constraint-vacuum.json
---

# Action-owned stress, observed normal constraints and the variable-vacuum gate

## 1. Outcome

This wave builds the missing **physical stress tensor** without adding an
external datum or inventing a free map. It also exposes why that success does
not yet recover Einstein gravity.

For the already-owned common matter action, let

\[
 T_H(g,\psi)=E_g^{\rm matter}(g,\psi),
 \qquad
 V_{\rm raw}(g,\psi)=D_\psi T_H(g,\psi).
\]

Because `T_H(g,0)=0`, the nonlinear metric Euler covector is reconstructed
exactly by

\[
 \boxed{
 T_H(g,\psi)=\int_0^1
 V_{\rm raw}(g,t\psi)[\psi],dt .} \tag{1}
\]

This is the action-owned Hilbert stress. It is symmetric by metric/coframe
variation and conserved on the matter shell by the complete diffeomorphism
Ward identity. For a quadratic fermion action the integral is particularly
simple because `V_raw(g,t psi)[psi]=2t T_H(g,psi)`.

Equation (1) is **not** the literal diagonal composite `VU`. `V_raw` is the
matter derivative of stress; `VU` is a linear Hessian-response operator. The
two have different types. This corrects the repository's earlier diagrammatic
gloss of Weinstein's unfinished “up-and-back” phrase.

An exact four-dimensional massless Dirac control includes the Krein factor
`K=gamma^0`. Its on-shell stress is symmetric, conserved and trace free. The
same spinor remains on shell when a null momentum is rescaled, while its
stress rescales. Therefore a momentum-free algebraic current-to-stress map is
not universal. Any relation between the projected connection current and
physical stress must carry the derivative/soldering data explicitly.

The observation-first constraint result survives composition: on the flat
Lorentzian defect, the coupled characteristic kernel still filters

```text
10 characteristic directions
- 4 harmonic-constraint violations
= 6 constraint-compatible directions
- 4 residual diffeomorphisms
= 2 physical directions: plus and cross.
```

But the action placement fails the next physics test. In either transverse-
traceless polarization, the repaired pre-Shiab action has matrix

\[
 J_{TT}(z)=\begin{pmatrix}0&z\\z&\kappa_1\end{pmatrix},
 \qquad \det J_{TT}=-z^2,
 \qquad (J_{TT}^{-1})_{hh}=-\frac{\kappa_1}{z^2}. \tag{2}
\]

The metric response has a **double pole**, not the Einstein single pole.
Harmonic constraints preserve the two polarization labels but do not remove
the generalized propagation partner. This is the sharp next construction
target.

Finally, on the homogeneous observed quadratic distortion horn, the unshifted
vacuum equation has only `v=0`, and the trace-reversed Hessian has inertia
`(6,4)`, so the stationary point is indefinite. An independent trace source
moves `v` linearly and is not screened. This does **not** settle the full
nonlinear action: the existing `T`-cubic term and non-equilibrium vacua remain
uncomputed. Ledger `LT-GR2d` is scope-corrected accordingly rather than
overclaiming that the whole current action is unable to select a vacuum.

## 2. Why this is a material advance

The previous gate named two missing objects: normal-jet propagation and a
symmetric conserved up-and-back stress. Merely running the null quotient again
would not be progress. The new content is instead the composition that was
missing:

1. the common action's existing mixed return block reconstructs the full
   nonlinear Hilbert stress with zero new freedom;
2. the exact Krein pairing is part of the physical bilinear;
3. conserved stress is compatible with the inherited harmonic constraints;
4. the resulting repaired gravity placement is tested at propagator, not just
   carrier/rank, grade; and
5. the double pole explains why “two polarizations survived” was not yet
   “Einstein physics recovered.”

This replaces a vague request for stress with a concrete remaining fork:
cancel or constrain the generalized partner, or change the action placement,
while retaining (1), plus and cross.

## 3. Pre-wave record and divergent specialist instructions

1. **Fork.** K77 `(7,7)` ambient geometry, complete first-jet observation and
   the already-declared restriction-first pre-Shiab repaired action horn.
2. **Search dimension.** No coefficient or map search. The radial path is
   forced by the vector-space matter fibre and zero-field boundary condition.
   Exact controls use a rank-ten observed `Sym^2` sector and one four-spinor
   Lorentzian Dirac shell.
3. **Unowned-object check.** `free_object_delta=0`. Equation (1) is derived
   from an existing scalar action and mixed Hessian, not supplied by P1/P2/P3.

| lens | binding instruction |
| --- | --- |
| variational bicomplex | reconstruct the nonlinear Euler term from its mixed derivative; do not equate a Hessian square with the original Euler map |
| Lorentzian spin geometry | include the Krein pairing in every fermion bilinear and vary the full density-pairing-operator product |
| mathematical relativity | require symmetry, on-shell conservation, harmonic compatibility and a single-pole response separately |
| hyperbolic PDE | inspect pole multiplicity and generalized solutions; a two-dimensional characteristic quotient alone is insufficient |
| symplectic/BFV | keep constraint restriction, gauge quotient and propagator multiplicity distinct |
| Krein operator theory | use the nondegenerate `(6,4)` primalizer honestly; do not infer a stable vacuum from invertibility |
| gauge geometry | keep connection current and Hilbert stress in their own Euler rows until a soldered Ward map relates them |
| source archaeology | read “up-and-back” as an unfinished path instruction unless the source publishes maps and cancellations |
| exact-computation engineering | use a second Sage/QQ route and planted single-pole, no-Krein and screening failures |
| science council/proof systems | attack both directions: summary overreach and rigorous defense of literal `VU` or the already-superseded rank-only test |

Pre-registered kills were a free hand-written stress map, literal `VU` equal
to nonlinear stress, a momentum-free current-to-stress identity, harmonic
constraints promoted to single-pole GR, and a nonzero/stable vacuum inferred
from an invertible indefinite quadratic form. Each kill fires at its scoped
object.

## 4. Layer 0

| phrase | object here | kept distinct |
| --- | --- | --- |
| connection current | variation with respect to a gauge connection | metric/coframe Hilbert stress |
| Hilbert stress | matter contribution to the metric Euler covector | raw mixed return block |
| `V_raw` | `D_psi T_H : F -> B!` | `T_H` itself |
| `VU` | primalized diagonal Hessian response | nonlinear quadratic stress |
| up-and-back | source path target with unreleased maps and cancellations | a proved literal composite |
| zeroth order | desired source operator order after path cancellation | momentum-free matter bilinear |
| normal constraint | harmonic-compatible observed `(h,v)` symbol condition | global `Y14` shell or ambient time polarization |
| two polarizations | quotient dimension and plus/cross representatives | pole multiplicity or number of initial-data branches |
| variable vacuum | stationary/non-equilibrium branch of the complete distortion action | response forced by curvature or an inserted trace source |

The decisive semantic correction is that **a count of characteristic
representatives is not a count of propagator poles**. The same plus/cross
carrier can support a single or double pole.

## 5. Source collision

The complete receipt is
[`observed-upback-stress-source-reinspection-2026-08-05.md`](../../lab/sources/observed-upback-stress-source-reinspection-2026-08-05.md).

Portal/Oxford `02:03:07--02:03:53` says stress energy *should* be the
up-and-back path, Dirac equations should come from competing crossed paths,
and cancellations were still needed for order, invariance, signs, indices and
handedness. It does not publish the mixed maps, primalizers or an equality
with `VU`.

The decisive return is **`SOURCE-CORRECTS`**:

- the source confirms the coupled-path target and unfinished burden;
- it corrects the earlier repo assertion that the phrase already types a
  literal diagonal `VU` composite;
- “zeroth order” belongs to the post-cancellation operator architecture, not
  automatically to a momentum-free physical stress bilinear; and
- the radial-transgression theorem is a repository action construction, not
  an attribution to Weinstein.

## 6. The action radial-transgression theorem

Let `B` be the bosonic metric/coframe field space, `F` the matter field space,
and `S_m:B x F -> R` a twice differentiable common action. Define

\[
 E_B^m(b,f)=D_bS_m(b,f),
 \qquad V_{\rm raw}(b,f)=D_fE_B^m(b,f).
\]

On a star-shaped matter fibre, if `E_B^m(b,0)=0`, the fundamental theorem of
calculus along `t -> tf` proves

\[
 E_B^m(b,f)-E_B^m(b,0)
 =\int_0^1D_fE_B^m(b,tf)[f]dt . \tag{3}
\]

Thus equation (1) is unique once the action and zero-field boundary are fixed.
No independent up-and-back coefficient is available.

Mixed second-variation symmetry gives

\[
 V_{\rm raw}=U_{\rm raw}^{\top}
\]

in the density-dual pairing already constructed by the predecessor. This is
the correct role of the earlier mixed-Hessian reciprocity theorem.

The diagonal composite needs primalizers:

\[
 VU:B\longrightarrow B.
\]

It is the derivative response of the coupled Euler system. It is not typed as
`E_B^m(b,f) in B!`, and even after using a primalizer it remains linear in a
bosonic perturbation rather than the nonlinear matter source. The planted
finite action catches exactly this category error.

## 7. Symmetry and conservation

For a diffeomorphism-invariant matter action, varying every metric, density,
pairing, connection and matter owner under a compactly supported vector field
gives the Ward identity schematically

\[
 -2\nabla_\mu E_g^{\mu\nu}
 +E_\psi\cdot\mathcal L^{\rm spin}_{(\cdot)}\psi
 +E_{\rm other}\cdot\rho_{(\cdot)}({\rm other})=0. \tag{4}
\]

On the complete matter/other-owner shell,

\[
 \nabla_\mu T_H^{\mu\nu}=0. \tag{5}
\]

This is an action theorem, conditional on including all moving owners. It does
not prove that the projected connection current is separately conserved or
equal to `T_H`.

The exact control uses signature `(+---)`, `K=gamma^0`, null momentum
`p=(1,0,0,1)` and spinor `psi=(1,0,1,0)^T`. It verifies

\[
 \slashed p\psi=0,
 \quad j^\mu=\bar\psi\gamma^\mu\psi=2p^\mu,
 \quad T^{\mu\nu}=p^{(\mu}j^{\nu)},
\]

with `T=T^T`, `p_mu T^{mu nu}=0` and zero trace. Omitting `K` changes the
current. Scaling `p -> a p` preserves the same shell spinor but scales `T`,
which kills a universal momentum-free algebraic `j -> T` map.

## 8. Constraint compatibility and the propagator test

On the minimal repaired observed horn,

\[
 S^{(2)}[h,v,\psi]
 =\langle v,G^{(1)}h\rangle_{DW}
 +\frac{\kappa_1}{2}\langle v,v\rangle_{DW}
 +S_m^{(2)}[h,\psi]. \tag{6}

The linear equations are

\[
 G^{(1)}h+\kappa_1v=0,
 \qquad
 (G^{(1)})^!v+T_H=0, \tag{7}
\]

up to the separately retained connection-current, section, density and BV
rows of the full action. Conservation (5) and the Bianchi identity make the
matter source compatible with the four harmonic constraints. The prior exact
`10 -> 6 -> 2` quotient therefore survives.

However, eliminating `v` gives

\[
 -\frac1{\kappa_1}(G^{(1)})^!G^{(1)}h+T_H=0. \tag{8}
\]

On transverse-traceless modes this is equation (2): a squared wave operator.
The composition is Green-hyperbolic on the prior flat globally hyperbolic
defect domain, but it has a double pole and correspondingly enlarged initial-
data/generalized-solution content. The current result is therefore:

```text
constraint compatibility: PASS at flat observed symbol grade
plus/cross carrier: PASS
single-pole Einstein propagation: FAIL for the repaired quadratic placement
full moving/curved 85-direction normal system: OPEN
```

This is not an orthodox rejection of the repaired action. It is an exact
construction demand generated by writing it: find the cancellation or domain
condition that removes the generalized partner, or change the action term
while retaining every overdetermining constraint already passed.

## 9. Variable-vacuum test

On the homogeneous observed quadratic horn with zero curvature and zero
matter source,

\[
 E_v=\kappa_1W_{DW}v=0. \tag{9}
\]

For nonzero `kappa_1`, `W_DW` is rank ten with inertia `(6,4)`. Thus the only
stationary point is `v=0`, and it is indefinite rather than a minimum. Adding
an independent trace source `rho` gives

\[
 v=-(\kappa_1W_{DW})^{-1}\rho. \tag{10}
\]

The response is linear; it tracks rather than screens the shift.

The scope fence is essential. The full source action contains nonlinear
`T`-dependence through `bar F`, including a `T`-cubic contribution, and may
admit non-equilibrium branches. Equation (9) does not evaluate those. It kills
only the claim that the **quadratic observed horn by itself** selects a stable
nonzero VEV. The next vacuum wave must compute the already-present nonlinear
term before adding any new potential or datum.

## 10. Constraint and surplus accounting

| item | result |
| --- | --- |
| free stress maps added | 0 |
| stress selector parameters | 0 |
| stress constraint surplus | positive in the operational sense: one action-derived object clears reciprocity, zero-field, symmetry, Ward conservation and exact Dirac controls without fitting |
| observed null quotient | inherited exact dimension 2; not booked again |
| propagator pole order | 2 on each TT metric response of repaired horn |
| unshifted quadratic vacuum | zero only; Hessian inertia `(6,4)` |
| shift response | linear tracking, no screening |
| global residue | unchanged: 84 reals + at least 19 function-valued + 10 forks |
| P1/P2/P3 | unchanged and unused |

An external datum cannot repair the type error `VU=T_H` or turn a double pole
into a single pole merely by being declared. It could only help if supplied as
a **typed action/domain rule** whose variation causes the required
cancellation; that would be a new construction with its own surplus count.

## 11. Seven axes plus Layer 0

| layer | disposition |
| --- | --- |
| Layer 0 | current/stress, stress derivative/diagonal square, path/operator order, quotient/pole count and quadratic/full vacuum separated |
| L1 source | `SOURCE-CORRECTS` literal `VU` and momentum-free readings; confirms unfinished path architecture |
| L2 algebra | exact radial theorem, mixed reciprocity, Krein-Dirac tensor, `(6,4)` Gram, `10 -> 6 -> 2`, double pole and vacuum response |
| L3 geometry | observed metric/coframe Euler target and density/Krein primalizers owned; source totalization and current soldering open |
| L4 variation | nonlinear matter metric Euler reconstructed; repaired coupled equations varied exactly at quadratic grade |
| L5 covariance/BV | matter-shell Ward conservation and harmonic compatibility; full moving diffeomorphism/odd BV totalization open |
| L6 analytic | prior flat defect Green composition survives; single-pole GR fails; curved/full-85 and ambient constrained domains open |
| L7 physics | symmetric conserved stress and plus/cross pass; Einstein response, stable VEV, screening and cosmology do not |

## 12. Ledger movement and next gate

Ledger v0.10 remains `82/82`, with verdict counts `32/19/25/6` and unchanged
global residue. Five distances migrate:

- `LT-GR2b`: the observed quadratic horn has only a zero indefinite vacuum;
  nonlinear/non-equilibrium selection remains.
- `LT-GR2c`: action stress and flat constraint compatibility close, but the
  repaired action has a double rather than Einstein single pole.
- `LT-GR2d`: scope-corrected from a whole-action inability claim to a missing
  full nonlinear `T`-cubic/non-equilibrium calculation.
- `LT-GR5`: plus/cross survive but a generalized distortion partner remains.
- `LT-GR6`: Hilbert stress is constructed; literal `VU` is killed; source
  totalization, connection-current relation and single-pole placement remain.

The highest-information next gate is

```text
CONSTRUCT_SOURCE_OWNED_UP_BACK_CANCELLATION_OR_ALTERNATIVE_ACTION_PLACEMENT_THAT_YIELDS_ONE_EINSTEIN_POLE_WITH_ACTION_HILBERT_STRESS_AND_PLUS_CROSS__THEN_COMPUTE_THE_EXISTING_FULL_NONLINEAR_T_CUBIC_VACUUM_BEFORE_ADDING_ANY_SELECTOR
```

The constrained-ultrahyperbolic domain remains a rival horn. It does not
replace the single-pole observed-physics burden.

## 13. Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/observed_upback_stress_normal_constraint_vacuum_probe.py

DOT_SAGE=/private/tmp/gu-observed-upback-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/observed_upback_stress_normal_constraint_vacuum_independent.sage
```

Main exact receipt: `48 exact + 8 planted + 4 repo + 1 source + 11 type =
72/72 PASS`. Independent Sage/QQ reconstruction: PASS.

No canon, public posture, Lane count, P1/P2/P3, physical magnitude, `w(z)`,
generation or chirality claim moves.
