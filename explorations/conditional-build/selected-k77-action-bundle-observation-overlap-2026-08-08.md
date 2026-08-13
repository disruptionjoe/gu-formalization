---
artifact_type: construction_result
created: 2026-08-08
status: FULL_ACTION_COVECTOR_ADJOINT_BUNDLE_OVERLAP_EXACT__COMPLETE_OBSERVATION_GERM_AND_NO_LEAKAGE_PROJECTOR_DESCEND__ARBITRARY_X_SECTION_INTEGRABILITY_BFV_DOMAIN_OPEN
source_return: SOURCE-CONFIRMS__GLOBAL_P_H_GAMMA_EPSILON_AND_SECTION_OBSERVATION_ROLE__SOURCE-SILENT__COMPLETE_EQUATION_DUAL_PREFERRED_SHIAB_BFV_DOMAIN__REPO-DERIVES__FULL_ACTION_COVECTOR_AND_OBSERVATION_PROJECTOR_THREE_PATCH_DESCENT
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_action_bundle_observation_overlap_probe.py
  - tests/channel-swings/selected_k77_action_bundle_observation_overlap_independent.sage
registry: lab/process/selected-k77-action-bundle-observation-overlap.json
---

# Selected K77 action-bundle and observation overlap

## Result first

The full pointwise selected-action covector from ledger v0.77 now satisfies an
exact noncommuting three-patch overlap test when composed with the already
owned global K77 chimeric-spin reduction.  On every patch the fields are
transformed first and the complete action bank is **recomputed**.  The direct
`0 -> 2` bank agrees with the sequential `0 -> 1 -> 2` bank and with the
coadjoint transition law.

The complete `4+10` observation equation-dual and its no-leakage projector
also descend, but only when they co-move with the frame.  Freezing either one
breaks covariance.  An explicit hidden covector remains invisible even while
`R L = 1`, so left-invertibility alone is not promoted to no leakage.

The same result passes on a second held-out background.  The complete
coefficient pairing and observed full-support Gram form descend exactly, and
opposite endpoint restriction preserves that form.

This closes the finite algebraic overlap/cocycle gate.  It does **not**
construct an integrable physical observation section on arbitrary `X`, prove
ordinary pullback is faithful, select the historical preferred Shiab, or
produce a global `tau_A0`/BFV phase space and common analytic domain.

## The composed objects

This swing did not build a second global bundle.  It uses the earlier theorem

\[
  C=\operatorname{Sym}^2(\pi^*T^*X)\oplus\pi^*T^*X,
  \qquad
  \gamma_\epsilon=\operatorname{Ad}(\epsilon^{-1})\gamma_0:
  C\longrightarrow\operatorname{ad}(P_H),
\]

and asks whether the v0.77 action covector is compatible with its transition
law.  It also reuses the complete observation-germ cotangent theorem rather
than treating ordinary section pullback as lossless.

Two positive signed quarter-turns inside the labelled four-plane are used:
`g01=(1,2)` and `g12=(2,3)`.  They preserve K77 and the `4+10` splitting but
do not commute.  Their product supplies the direct third overlap.  Every
exterior one-form index and every Clifford coefficient index is transformed.

If `K_i` is the recomputed action bank, `A_ij` the exterior transition and
`C_ij` the coefficient transition, the exact law is

\[
  K_j=A_{ij}K_iC_{ij}^{T},
  \qquad
  A_{02}=A_{12}A_{01},
  \qquad
  C_{02}=C_{12}C_{01}.
\]

Both the SymPy and independent Sage implementations reconstruct the actual
selected-action bank on all three patches.  Transported aliases are not used
as patch data.

## Observation and no leakage

Let `O_i` be the complete equation-dual receiver.  It moves as

\[
  O_j=A_{ij}O_iA_{ij}^{T},
\]

so its observed equation bank satisfies the same coadjoint law.  A fixed
`O_0` fails on patch one, which proves the check is not vacuous.

For the complete lift `L_i` and exact left inverse `R_i`, define

\[
  P_i=L_iR_i.
\]

The projectors satisfy

\[
  P_j=A_{ij}P_iA_{ij}^{T}
\]

pairwise and directly.  A fixed projector fails.  Moreover, the probe builds
a nonzero `h=(1-P_0)v` with `L_0^T h=0`; thus observed equation equality and
`R_iL_i=1` do not erase hidden ambient equations.  The co-moving projector is
the separate no-leakage datum that must descend.

## Layer 0

| phrase | exact object here | not identified with |
| --- | --- | --- |
| global action bundle | source-owned associated K77 Clifford/adjoint bundle plus the natural action-covector transition law | existence of a preferred physical field section |
| overlap certificate | two noncommuting exact signed rotations and their direct cocycle | exhaustive computation over every smooth atlas |
| complete observation | value-plus-first-jet equation dual with dependent normal data | ordinary four-dimensional pullback |
| no leakage | co-moving complementary projector | the identity `R L=1` by itself |
| descended pairing | scalar Clifford coefficient form on the full live action image | positive energy or closed Krein domain |
| endpoint acceptance | opposite local restrictions preserve the descended form | global BFV phase space, polarization or charges |

## Source return

The source material owns the chimeric-spinor extension `P_H`, the moving
`epsilon`-rotated Clifford frame and the role of observation by a section.  It
does not print the complete equation-dual, its no-leakage projector, the
preferred Shiab, or a global BFV/common-domain theorem.  Those overlap laws
are repo derivations.

```text
SOURCE-CONFIRMS: global P_H/gamma_epsilon and observation-section role
SOURCE-SILENT:   complete equation dual, no-leakage projector, preferred Shiab, BFV/domain
REPO-DERIVES:    full action-covector and observation-projector three-patch descent
```

## Seven-axis disposition

- **Layer 0:** pointwise fibre, associated-bundle law, physical section,
  complete germ, ordinary pullback and BFV/domain are separated.
- **L1 syntactic:** both transition matrices, coefficient duals, direct
  cocycle, observation receiver, lifts and projectors are explicit.
- **L2 type:** exterior rows transform covariantly and action coefficient
  covectors contragrediently; every coefficient index is transported.
- **L3 algebraic:** two independent exact implementations and two field
  backgrounds pass pairwise and direct noncommuting overlaps.
- **L4 geometric:** the action covector, complete receiver, projector and
  coefficient pairing have compatible associated-bundle laws.  Arbitrary-X
  physical section integrability remains open.
- **L5 variational:** patch banks are independently recomputed from the same
  selected action; no fitted current, receiver coefficient or datum is added.
- **L6 analytic:** no common closed Green/Krein domain, hyperbolicity, BFV
  polarization or global charge algebra is claimed.
- **L7 physical:** no Einstein equation, vacuum, spectrum, positivity,
  unitarity or cosmological prediction is promoted.

## Constraint fence and progress

```text
new fitted K/current: 0
new external datum: 0
new coefficients or selectors: 0
new fields: 0
P1/P2/P3 consumed: 0

Ledger v0.78 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped

headline_delta: NONE
frontier_conditions_closed: 3
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Closed are the full action-covector overlap, complete equation-dual overlap,
and no-leakage-projector overlap gates.  Opened is the narrower physical
arbitrary-X observation-section integrability/faithfulness gate.  Verdicts,
residue, quotient count, P1/P2/P3, canon and public posture do not move.

Curt remains formally separate inside the Eric lane.  No third lane is
promoted.

## Next gate

Construct the actual observation-section jet and its integrability/physical
faithfulness conditions on `Y^14`, then place the descended action and
projector inside the global `tau_A0`/BFV moment-map and common Green/Krein
domain.  Keep the preferred-Shiab question, coupled nonzero-fermion residual,
and distinct `I2B <-> ||II||^2` map separate.
