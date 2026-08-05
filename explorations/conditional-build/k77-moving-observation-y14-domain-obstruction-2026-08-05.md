---
artifact_type: construction_result
created: 2026-08-05
status: FIRST_JET_SECTION_GERM_NO_LEAKAGE_EXACT__VALUE_ONLY_AND_FINITE_JET_GLOBAL_SHELL_ROUTES_KILLED__STANDARD_K77_CODIM1_GLOBALLY_HYPERBOLIC_DOMAIN_SHARPLY_OBSTRUCTED__CONDITIONAL_OBSERVED_CURVATURE_DISTORTION_EQUATION_TYPED__UP_AND_BACK_STRESS_CONSTRAINED_DOMAIN_AND_VACUUM_OPEN
lane: "1"
functional_channels: [BUILD, SOURCE, COMPOSE, VERIFY]
fork_assumed: "SIGNATURE-AMBIENT=(7,7); SOURCE-GUIDED-OBSERVATION-SECTION-HORN"
search_space_dim: "14 first-derivative coefficient directions; 3 normal-orbit types"
free_object_delta: 0
residue_touched:
  - "LT-GR2b: T3"
  - "LT-GR2c: T3"
  - "LT-GR5: T3"
  - "LT-GR6: T3_CURRENT/T4_STRESS_OPEN"
ledger_rows: [LT-GR1b, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR5, LT-GR6, LT-SM8]
source_return: SOURCE-CORRECTS
scripts:
  - tests/channel-swings/k77_moving_observation_y14_domain_obstruction_probe.py
  - tests/channel-swings/k77_moving_observation_y14_domain_obstruction_independent.sage
registry: lab/process/k77-moving-observation-y14-domain-obstruction.json
---

# K77 moving observation, ambient-domain obstruction and conditional observed equations

## 1. Outcome

The action can now reach the observation section without silently discarding
the normal first-jet data that it actually generates. The correct observation
object is not value pullback. It is the **complete first jet along the moving
section**, decomposed into tangential and vertical-normal pieces by the
already-built four-plus-ten observer map. Its inverse-transpose carries every
first-order Euler monopole and normal dipole, so no-leakage holds exactly on
the section germ.

Two stronger statements fail, and the failures are constructive rather than
orthodox dismissals.

1. The Bianchi-selected `comm/symi/symi` Shiab has live response in all 85
   mixed-normal exterior directions and rank 1,190 on its full grade-one
   mixed-normal bank. A value-only or tangential-only observation therefore
   cannot carry the selected action.
2. No finite jet along a codimension-ten section determines a global bulk
   Euler row. For every order `k`, the normal polynomial `y^(k+1)` has zero
   `k`-jet on the section and is nonzero away from it. Section-germ
   no-leakage is not global-shell equivalence.

The ambient analytic question also receives a sharp answer. A nondegenerate
`(7,7)` principal metric has no spacelike codimension-one hypersurface. A
non-null hypersurface has inertia `(6,7)` or `(7,6)`; a null one has
`(6,6,1)`. Therefore the ordinary Lorentzian globally-hyperbolic
advanced/retarded Green/BFV route is unavailable on `Y14`. This does **not**
exclude a constrained ultrahyperbolic boundary-value class, a source-derived
polarization/reduction, or an observation-first physical theory on Lorentzian
`X4`. Those are now the explicit revival horns.

Finally, the observed first-order gravitational equation is typed. With

\[
 C_s=G_4\!\left(\operatorname{res}_H P_R\bar F+Q(II_s)\right),
 \qquad v=\sigma_\epsilon(v_T),
\]

the gravitational projection of the complete connection-difference Euler row
has the conditional form

\[
 \boxed{C_s+\kappa_1v+\mathcal J_X^{\rm conn}
              +\mathcal E_X^{\rm defect/BV}=0.} \tag{1}
\]

Here `J_X^conn` is the first-jet-observed, gravitationally projected
`J_D+J_F` connection current. It lands in a symmetric-tensor target, but it is
**not yet the physical stress-energy tensor**. Weinstein's source says that
stress energy should be an up-and-back zeroth-order invariant term and says
the required cancellations were unfinished. The Hilbert stress tensor from
an independently owned `X` matter action instead enters the metric/section
Euler equation. The missing equality between those objects is now the next
physics construction, not a naming convention.

The trace component of `v` gives a variable metric-proportional contribution
and therefore a concrete home for a VEV that moves with curvature. No
constant `Lambda g` is inserted. A nonzero vacuum, magnitude, screening and
`w(z)` remain open.

## 2. Why this moves the North-Star gate

The predecessor stopped just before physics because observation no-leakage and
the global domain were undetermined. This wave settles both questions at the
strongest grade the current objects permit:

- local first-order section observation is constructed exactly;
- promotion from section germ to global shell is killed exactly;
- the standard ambient Cauchy-domain horn is killed by signature;
- the observation-first and constrained-ultrahyperbolic horns remain live
  with explicit burdens; and
- the observed curvature/distortion equation is written far enough to locate
  the missing physical stress map and vacuum rule.

This is not a request for another unspecified source action or external datum.
The action, receiver and equation are present. The residue is a specific
domain/constraint-propagation choice and a specific up-and-back map.

## Pre-wave record

1. **Fork assumed.** This wave stays on the already-selected K77 `(7,7)`
   chimeric carrier and the source-guided observation-section horn. If the K95
   carrier or a source-derived Lorentzian reduction is ultimately selected,
   the first-jet section theorem transports but the ambient hypersurface
   obstruction must be recomputed; no signature result transfers silently.
2. **Search-space dimension and wholesale exclusion.** The complete
   first-derivative coefficient space splits as `4+10=14`; its observation
   map and equation dual are fixed by the graph jet and pairing, so there is
   no selector enumeration. The hypersurface problem has exactly three normal
   orbit types—positive, negative and null—and their inertias decide the
   entire codimension-one Cauchy class at once. The already-certified
   `85/85/1190` selected mixed-normal result is composed, not recomputed.
3. **Unowned-object check.** Successful first-jet observation introduces no
   field, projector, datum or parameter: `free_object_delta=0`. A future time
   polarization would be a new owned geometric reduction and is not smuggled
   in here. The source-directed up-and-back stress map and normal-jet
   constraint differential remain named next-gate constructions rather than
   implicit objects.

## 3. Inline divergent specialist preassessment

| lens | binding instruction |
| --- | --- |
| jet/differential geometry | use the canonical `ds(TX) plus V` splitting and distinguish the section germ from the global field |
| variational bicomplex | carry normal Legendre coefficients as derivative-of-delta Euler owners rather than dropping them |
| symplectic/BFV | treat the conormal coefficient as preboundary polarization until a tangent differential says otherwise |
| hyperbolic PDE | prove the hypersurface signature before discussing a Cauchy domain; preserve constrained ultrahyperbolic revivals |
| Krein operator theory | use nondegeneracy and signature honestly; do not manufacture positivity |
| representation theory | compose the selected channel's already-certified mixed-normal rank instead of rerunning the full Clifford bank |
| gauge geometry | use the complete first-jet equation dual and retain moving-section, epsilon, metric and density owners |
| mathematical physics | keep the connection current, Hilbert stress tensor and proposed up-and-back tensor distinct |
| exact-computation engineering | certify the jet inverse, equation pairing, finite-jet counterexample and all three hypersurface normal types over rationals |
| science council/proof systems | attack both summary overreach and any attempt to defend the superseded value-only or ordinary-Cauchy routes |

Pre-registered kills were value-only observation with a live conormal symbol,
first-jet observation promoted to global bulk faithfulness, an ambient
codimension-one Cauchy surface in `(7,7)`, removal of plus/cross, current
renamed stress tensor, and variable `v` renamed constant `Lambda`. All are
exercised in the certificate.

## 4. Layer 0

| phrase | object used here | kept distinct |
| --- | --- | --- |
| pullback | field-value restriction to `s(X)` | complete first-jet observation and equation dual |
| four-plus-ten map | zero-jet coefficient isomorphism for an ambient one-form | its first-jet prolongation |
| no-leakage | Euler current is in the image of the section-germ equation dual | observation implies the global bulk shell |
| normal jet | derivative data of an already-owned ambient field along the section | a new external field or datum |
| moving observation | derivative of field, section jet, density and shape owners together | fixed-section restriction |
| defect Green complex | harmonic-gauge Lorentzian propagation on `X4` | global split-signature propagation on `Y14` |
| ambient domain | constrained boundary/Green/BFV data for the coupled bulk system | ordinary one-time Hamiltonian Cauchy data |
| connection current | action derivative `J_D+J_F` after the typed receiver | Hilbert stress energy or source-proposed up-and-back term |
| cosmological contribution | trace component of the variable distortion `v` | fixed `Lambda g`, selected VEV or observed `w(z)` |

## 5. Source collision

The complete receipt is
[`k77-moving-observation-y14-domain-source-reinspection-2026-08-05.md`](../../lab/sources/k77-moving-observation-y14-domain-source-reinspection-2026-08-05.md).

The decisive return is **`SOURCE-CORRECTS`**.

- Weinstein confirms the observerse/section/pullback architecture, most fields
  and actions upstairs, a variable VEV-bearing dark-energy term, and
  gauge-rotated connection data as augmented torsion.
- He explicitly distinguishes ordinary one-time Hamiltonian dynamics from the
  multiple-time ultrahyperbolic problem and calls the latter technical debt.
  The source therefore corrects any assumption that a standard ambient Cauchy
  domain has already been supplied.
- He says stress energy should arise from an up-and-back term but also says the
  zeroth-order, invariance, index and sign cancellations were unfinished. This
  corrects any promotion of `J_D+J_F` or a later raw cyclic block to the
  physical stress tensor.
- The source is silent on the first-jet equation dual, constrained ambient
  boundary class, completed up-and-back map and vacuum selection.

## 6. Complete first-jet observation

Let `E` denote any of the already-owned ambient field bundles. Along a section
`s:X->Y`, the metric-bundle geometry has the canonical splitting

\[
 T_Y|_{s(X)}=ds(TX)\oplus V,
 \qquad
 T_Y^*|_{s(X)}=T^*X\oplus V^* . \tag{2}
\]

For scalar coefficients this gives the complete first-jet restriction

\[
 r_s^1(j_Y^1u)
 =\left(u|_s,D_{ds(TX)}u|_s,D_Vu|_s\right). \tag{3}
\]

For associated-bundle fields the ordinary derivatives are replaced by the
already-owned covariant derivatives. The zero-jet connection coefficient is
first passed through the exact four-plus-ten map
`F_s=(s^*,res_s^V)`. Equation (3) is then applied componentwise. No new
projector or datum is introduced.

In local graph coordinates `y=s(x)` with section jet `J`, the derivative
block is

\[
 M_1(J)=
 \begin{pmatrix}I_4&J^T\\0&I_{10}\end{pmatrix},
 \qquad
 M_1(J)^{-1}=
 \begin{pmatrix}I_4&-J^T\\0&I_{10}\end{pmatrix}. \tag{4}
\]

It has determinant one. The executable certificate uses a nontrivial rational
`2+3` model, where the same block theorem is exact, and the independent Sage
route reproduces it over `QQ`.

The value/tangential-only row

\[
 (I,J^T)
\]

has graph-conormal kernel `(-J^T,I)^T`. That is precisely the information the
selected action is known to use: the selected `comm/symi/symi` channel has
rank 85 on the mixed-normal witness slice and rank 1,190 on the complete
grade-one bank. Thus the first-jet enlargement is demanded by the action; it
is not fitted to a Standard Model target.

## 7. Equation dual and local no-leakage

At fixed section jet, write `q=M_1a`. Equality of first variations for every
observed jet variation forces

\[
 e_q=M_1^{-T}e_a. \tag{5}
\]

Equivalently, the equation lift is `L_E=M_1^T` and observation is
`O_E=M_1^{-T}`. Therefore

\[
 O_EL_E=1,
 \qquad
 L_EO_E=1 \tag{6}
\]

on the complete first-order **section germ**. This is the actual no-leakage
theorem earned here.

For a localized first-order action, the preceding variational theorem writes
the ambient Euler current as

\[
 \mathcal E_{\rm loc}=\delta_sE_0-\partial_a(\delta_sE_a),
 \qquad
 E_a=\mu_s(P^a-s_i^aP^i). \tag{7}
\]

The dual (5) records both `E_0` and all `E_a`. The selected action generically
has nonzero `E_a`, so a value-only map fails and (5) succeeds.

When the section moves,

\[
 \delta(r_s^1u)=r_s^1(\delta u)+(D_sr_s^1)[\delta s]u. \tag{8}
\]

The second term is owned by the already-derived shape/density equation. The
exact control makes it nonzero; freezing it fails.

The analytic grade remains bounded. This theorem gives a fibrewise/jet-bundle
isomorphism and exact first-variation dual. It does not construct a global
bounded right-extension operator on the noncompact Sobolev domain.

## 8. Why local no-leakage does not imply the global bulk shell

For every finite order `k`, choose a local normal coordinate `y` and the bulk
row

\[
 f_k(y)=y^{k+1}. \tag{9}
\]

Every derivative of order at most `k` vanishes at `y=0`, while `f_k` is not
the zero function. Therefore the kernel of finite-jet restriction is nonzero
at every order. No finite observation jet can prove

\[
 E_Y=0\quad\Longleftrightarrow\quad O_s^kE_Y=0
\]

for unrestricted global bulk rows.

This corrects the meaning of the nonduplicating action

\[
 S=S_Y+\lambda_{\rm def}S_X^{\rm independent}.
\]

Its field equation is stratified/distributional,

\[
 E_Y+\lambda_{\rm def}R_s^!E_X=0, \tag{10}
\]

and observation captures the section-supported term without loss. It does not
replace the bulk equation by a second localized copy. A global solution still
needs an ambient domain or a theorem reducing the bulk to section data.

## 9. Sharp obstruction to the standard ambient domain

The global K77 construction has principal chimeric form of signature `(7,7)`.
Let `H=n^perp` be a thirteen-dimensional hypersurface tangent space.

- If `n` is positive, `H` has inertia `(6,7)`.
- If `n` is negative, `H` has inertia `(7,6)`.
- If `n` is null, the restriction is degenerate with inertia `(6,6,1)`.

Equivalently, the maximum dimension of a definite subspace is seven, less
than thirteen. Hence no codimension-one hypersurface is spacelike. The
ordinary Lorentzian definition of global hyperbolicity, with a spacelike
Cauchy hypersurface and causal advanced/retarded Green propagation, does not
apply to the full `Y14` principal geometry.

This is the promised sharp obstruction. It kills:

```text
K77 Y14 + ordinary codimension-one spacelike Cauchy surface
          + standard one-time globally-hyperbolic Green/BFV construction.
```

It does not kill:

1. a source-derived polarization/reduction selecting a Lorentzian physical
   subsystem and proving the other directions are constraints;
2. a constrained ultrahyperbolic boundary-value domain, possibly with
   nonlocal compatibility conditions; or
3. an observation-first theory whose physical evolution is the existing
   Lorentzian `X4` defect Green complex and whose normal jets satisfy a closed
   propagation/compatibility system.

No existing external datum supplies horn 1. P1 is an orientation line, P2 is
still an under-typed `X`-sector datum, and P3 is count/KO data. A choice of a
time polarization would be a much larger geometric reduction, not a hidden
bit. This wave therefore inserts no datum and leaves the three revival horns
honest.

The older repo sentence that the base-time direction automatically makes the
full fibre system symmetric hyperbolic is not used. It requires exactly the
constraint propagation or fibre estimate still missing and cannot override
the hypersurface theorem.

## 10. Conditional observed equations

Let `iota_epsilon` be the already-built adjoint right inverse of the
rank-ten gravitational receiver and let `O_{E,s}^1` be the first-jet equation
observation above. Define the projected connection current

\[
 \mathcal J_X^{\rm conn}
 =\iota_\epsilon^!O_{E,s}^1(\widehat J_D+\widehat J_F+\cdots). \tag{11}
\]

The ellipsis retains the explicitly owned connection, defect, background and
BV contributions rather than pretending the matter current is the whole
Euler row. On the pre-Shiab gravitational replacement horn, variation of the
distortion slot gives equation (1).

This is an action-owned curvature/distortion covariation equation at
section-germ grade. It realizes the source's “movable field next to curvature”
shape. But three equations/objects remain distinct:

1. **Curvature/distortion equation:** equation (1), obtained by varying `v`.
2. **Metric/section equation:** schematically

   \[
   (D_{g,s}C_s)^!W_{DW}v
   +\frac{\kappa_1}{2}D_{g,s}\langle v,v\rangle_{DW}
   +\lambda_{\rm def}\,\delta_{g,s}S_X^{\rm matter}
   +E_{\rm shape/density}=0. \tag{12}
   \]

   The Hilbert stress tensor is defined by the matter variation in (12).
3. **Source-proposed up-and-back stress equation:** an unfinished zeroth-order
   invariant map that would have to identify the appropriate matter/fermion
   content with the gravitational equation while clearing the source's
   cancellation burdens.

Landing in `Sym^2T*X` makes (11) a symmetric-target current. It does not prove
that it equals the Hilbert tensor, is separately conserved, or is the source's
up-and-back term. The full diffeomorphism Ward identity may relate the three
only after every moving owner is included.

There is also a consequential action fork. In one mode,

\[
 L(v,C,J)=v(C+J)+\frac{\kappa_1}{2}v^2
\]

gives `C+J+kappa_1 v=0`; eliminating `v` yields

\[
 L_{\rm eff}=-\frac1{2\kappa_1}(C+J)^2. \tag{13}
\]

That is curvature/current squared, not automatically Einstein--Hilbert.
Therefore equation (1) must remain as a first-order auxiliary system, or an
additional source-owned constraint/cancellation must show how its low-energy
branch reduces to Einstein plus physical stress energy. Calling (13) GR would
repeat the mapping error the ledger is designed to prevent.

For the cosmological component, decompose

\[
 v=\lambda_v(x)g+v_0,
 \qquad \operatorname{tr}_g v_0=0. \tag{14}
\]

The trace of (1) makes `lambda_v(x)` covary with the trace of curvature and
the projected current. It is a field and can in principle acquire a VEV; it
is not a constant `Lambda`. Equation (14) locates the mechanism but does not
select a nonzero branch, fix the common amplitude, screen an independent
vacuum shift or derive an observable equation of state.

## 11. Preservation of the physical null quotient

The first-jet map is invertible on the section germ, so it cannot erase the
predecessor's exact two-dimensional constrained characteristic quotient. The
plus and cross representatives remain the physical null modes of the
Lorentzian defect Green complex.

The ambient signature obstruction does not turn those modes into defects.
Conversely, the two defect modes do not prove a global ambient domain. The two
statements concern different objects and both remain true.

## 12. Constraint and residue accounting

| item | result |
| --- | --- |
| fitted parameters | 0 |
| new fields/projectors/data | 0 |
| selected mixed-normal block | composed, not recomputed; 85 live directions, rank 1,190 |
| section-germ equation loss | 0 at complete first-jet grade |
| global bulk kernel of finite-jet observation | nonzero for every finite order |
| standard ambient Cauchy-domain horn | killed by `(7,7)` hypersurface inertia |
| ambient revival horns | 3: polarization/reduction, constrained ultrahyperbolic BVP, observation-first constrained system |
| defect physical quotient | dimension 2, plus/cross retained |
| up-and-back stress map | open |
| nonzero cosmological vacuum/magnitude | open |
| global continuous residue | unchanged at 84 reals before quotient |
| P1/P2/P3 | unchanged and unused |

The observation map does not add a parameter: it is forced by the metric-bundle
splitting and action jet order. The global residue does not fall because no
ambient constraint domain, stress identity, vacuum selector or normalization
quotient was constructed.

## 13. Seven axes plus Layer 0

| layer | result |
| --- | --- |
| Layer 0 | value/jet observation, germ/global shell, defect/ambient domain, current/stress and variable/fixed cosmological terms separated |
| L1 source | `SOURCE-CORRECTS` ordinary ambient-Cauchy and completed-stress assumptions; confirms observation and dynamic-field direction |
| L2 algebra | exact first-jet inverse/dual, finite-jet counterexamples and all three hypersurface inertias certified |
| L3 geometry | canonical moving section-germ carrier built from `ds(TX) plus V`; global bounded extension/open ambient reduction not claimed |
| L4 variation | complete first-order defect monopole/dipole no-leakage and conditional curvature/distortion equation typed |
| L5 covariance/BV | previous formal even owner retained; physical up-and-back map and ambient BFV boundary class open |
| L6 analytic | standard codimension-one globally-hyperbolic `Y14` horn killed; defect Green complex survives; constrained ambient horns open |
| L7 physics | two graviton polarizations preserved; dynamic trace field located; physical stress, vacuum, magnitude and cosmology open |

## 14. Two-sided hostile review boundary

The durable hostile review is
[`2026-08-05-k77-moving-observation-y14-domain-review.md`](../../lab/process/hostile-reviews/2026-08-05-k77-moving-observation-y14-domain-review.md).

The summary-outruns-artifact charge rejects all of the following:

- “no-leakage solves the bulk equations”;
- “the global `Y14` domain is impossible in every sense”;
- “the observed current is the stress tensor”;
- “the trace field solves the cosmological-constant problem”; and
- “the two polarizations prove positivity or quantum consistency.”

The superseded-object charge rejects further work on a value-only observation
or an ordinary ambient Cauchy hypersurface. Their failures are now exact. The
live objects are normal-jet constraint propagation/constrained boundary data
and the up-and-back stress map.

## 15. Ledger movement and next gate

Ledger v0.9 preserves `82/82` targets, verdict counts and global residue.

- `LT-GR2b` moves closer: the action-owned variable distortion now has a
  faithful section-germ equation placement; nonzero vacuum selection remains.
- `LT-GR2c` moves closer: moving first-jet no-leakage is exact and the standard
  ambient-domain horn has a sharp obstruction; the constrained domain and
  physical stress identity remain.
- `LT-GR5` moves closer: the observed augmented-torsion jet equation is typed,
  while extra-mode propagation remains open.
- `LT-GR6` moves closer: the observed receiver/current is built, but the
  physical up-and-back stress identification is explicitly not supplied.
- `LT-GR1b`, `LT-GR2d` and `LT-SM8` do not change.

The next named gate is

```text
CONSTRUCT_OBSERVATION_FIRST_NORMAL_JET_CONSTRAINT_PROPAGATION_AND_SOURCE_DIRECTED_UP_AND_BACK_SYMMETRIC_CONSERVED_STRESS_MAP__OR_BUILD_A_CONSTRAINED_ULTRAHYPERBOLIC_DOMAIN__THEN_SELECT_AND_SHIFT_TEST_A_NONZERO_VARIABLE_COSMOLOGICAL_VACUUM
```

The efficient primary horn is observation-first: prove that the normal-jet
equations close and propagate on the Lorentzian defect domain while building
the up-and-back map from the already-owned matter/fermion complexes. A genuine
constrained ultrahyperbolic domain remains an independent rival, not a
prerequisite silently assumed solved. Only after one domain horn and the
stress map close should the nonzero vacuum, repeated vacuum-shift and FLRW
tests run.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/k77_moving_observation_y14_domain_obstruction_probe.py

DOT_SAGE=/private/tmp/gu-k77-observation-y14-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/k77_moving_observation_y14_domain_obstruction_independent.sage
```

Primary receipt: `23 exact + 10 planted + 7 repo + 1 source + 11 type = 52/52`.
Independent Sage/QQ jet and hypersurface reconstruction passes. No P1/P2/P3,
canon, public posture, Lane count or phenomenological prediction moves.
