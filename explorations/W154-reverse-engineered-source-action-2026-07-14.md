---
artifact_type: exploration
status: exploration (TEAM REVERSE, W154; five personas inline, one worker, no sub-agents; deterministic test with positive controls)
created: 2026-07-14
wave: W154
label: W154
hypothesis: "Joe's corrected marble/wood framing: the cheap wood is the METRIC g_munu + the cosmological constant Lambda (both DERIVED); the KEPT content is T_munu = the record/matter content, with G the coupling. Records are fundamental in Y14; the metric is a derived X4 shadow. REVERSE-ENGINEER (assumption-first, not forward-build) a single source action S that coheres the full picture: take everything that MUST be true (A1-A4 + F1-F5) as boundary conditions on S and back out the action form that produces all of it simultaneously."
title: "W154 -- the reverse-engineered source action S. VERDICT: ONE coherent S is assembled (record field Psi fundamental on Y14, metric DERIVED as the shadow), and it is UNDER-DETERMINED, not over-determined: no F1-F4 conflict survives inspection (the sharpest candidate, F3 sign-forced-+ vs F1 sign-changing-Q, RESOLVES as field-sign vs rate-sign and is jointly satisfiable). The reverse-engineering makes genuine progress by E1's test on THREE counts at once: (i) it REDUCES the free-function count (the 10 metric functions g_munu are removed -- metric is derived, not an input; sign(Lambda) is fixed +; beta/alpha=2 becomes a CONSEQUENCE not a selection); (ii) it PARTIALLY DERIVES debit-2 (the amplitude O(1) q_B ~ H^2 and the sign-changing CHARACTER of Q are forced by the everpresent 1/sqrt(N) law + C-positivity + one-way accretion; the specific crossing epoch z=0.405 is NOT derived); and (iii) it EXPOSES a precise obstruction -- the everpresent MEAN Lambda=c/sqrt(N) with N monotone gives monotone WITHDRAWAL (Q<0 always, no rise), so F1's rise MUST be carried by the non-monotone fluctuation, whose single-crossing realization is the one remaining free object. The single remaining unbuilt object is sharpened: the promotion-gate BOUNDARY term whose variation yields Q, equivalently discharging C3 (theta = EL derivative of a gauge-invariant action on Y14) for the record field."
grade: "exploration / conditional register throughout. Every 'S does X' reads 'under the reverse-engineered conditional structure, X'; nothing asserts GU, that the DESI wiggle is real, or that any decomposition is physical. The reverse-engineering is explicitly ASSUMPTION-FIRST (bad science if taken as forward derivation; it is hypothesis generation, the rigorous kill comes after). COMPUTED (deterministic, tests/W154_reverse_engineered_source_action.py, 25/25 exit 0): the W136 bulk-flatness anchor (a0_fam=2alpha-beta, beta/alpha*=2, Einstein a1_fam=3 attractive, native a1=1/3, tachyon a2=-1/9); the W144 CPL crossing (a_x=0.71163, z_x=0.40523); the everpresent amplitude 1/sqrt(N_4)=(l_p/R_H)^2 ~ H^2 giving O(1) q_B; the (9,5)=(3,1)+(6,4) split and q=5 finality frontier; the debit-2 OBSTRUCTION (monotone N -> sign-definite Q_mean); the F1^F3 COMPATIBILITY (positive single-hump Lambda -> rho_V>0 while Q crosses zero once); the epoch-unpinned check (crossing tracks the free peak); the constraint-vs-free-object count. CITED (not re-derived): W125/W131 (source action / covariant Y14 operator, H41 unbuilt), W126/W130 (induced |II|^2 action: a1=1/3, split 3:2:1, tachyon), W132/W137 (C-operator positive subspace, signed |II|^2 ledger), W136 (bulk-flatness), W144 (DESI-fitted Q), W145/W146 (everpresent-Lambda, sign from C-positivity), W150 ((9,5) commitment split / q=5 firewall), W151 (Malament+BLMS+Jacobson emergence, route beta), W152 (marble/wood), W138 (kill battery), the source-action-requirements-spec (27 rows). No canon / RESEARCH-STATUS / claim-status / verdict / posture change; no spec FIT row moves; the count stays {1,3}; H41 unbuilt; H59 OPEN."
construction: "program-native where the objects are GU's (Y14, the record field Psi in carrier B/ker Gamma, the induced |II|^2 action, the C-operator, the gimmel null cone, the (9,5) split); standard-field where the machinery binds any construction (the interacting-vacuum decomposition -- PORTED Wands/De-Bruck; the everpresent-Lambda law -- PORTED Sorkin/ADGS; Malament/BLMS/Jacobson emergence -- PORTED; the contracted Bianchi identity). Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md; the RS cure fork (geometer's g=1 projector vs Porrati-Rahman vertex) is carried, not resolved."
depends_on:
  - explorations/source-action-requirements-spec-2026-07-13.md
  - explorations/W125-source-action-first-build-2026-07-13.md
  - explorations/W131-covariant-operator-y14-2026-07-14.md
  - explorations/W136-issuance-declaration-propagation-2026-07-14.md
  - explorations/W144-desi-fitted-issuance-function-2026-07-14.md
  - explorations/W146-substrate-sweep-theoretical-physics-2026-07-14.md
  - explorations/W150-substrate-sweep-consensus-crypto-2026-07-14.md
  - explorations/W151-gr-and-c-emergence-from-records-2026-07-14.md
  - explorations/W152-marble-and-wood-source-fix-2026-07-14.md
  - explorations/W138-issuance-kill-battery-2026-07-14.md
  - explorations/dark-energy-cosmology/dark-energy-divergence-free-proof-2026-06-22.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W154_reverse_engineered_source_action.py
---

# W154 -- the reverse-engineered source action S

## 0. The move, and why it differs from every forward build

Every prior build attempt (W102, W125, W152) took the metric `g_munu` as an input field, wrote a
gravitational action on it, and repeatedly reduced to "one unbuilt object" (the covariant operator
on Y14 as a dynamical action deriving `Q`). This wave takes Joe's CORRECTED framing at face value
and inverts the procedure. The cheap wood is now `g_munu` AND `Lambda`; both are DERIVED. The kept
content is `T_munu` = the record content. So the reverse-engineering does not build `S` forward and
read off what it gives; it takes everything that MUST be true and backs out the action form.

The single structural decision that makes this different: **`g_munu` is not an integration variable
of `S`.** The fundamental field is the record field `Psi` on Y14 (carrier B / ker Gamma, A3/A4),
and the X4 metric is a DERIVED functional `g[Psi, C]` -- its causal cone is the gimmel null cone of
`Psi`'s covariant operator (Malament leg, A1) and its conformal factor is the C-positive record
count (BLMS leg, A1). This is exactly W151's route beta made into the definition of `S`'s field
content, rather than a comparison run after the fact.

Assumption-first by design; the rigorous kill comes after (Section 7). Five personas ran inline in
one worker; the deterministic test `tests/W154_reverse_engineered_source_action.py` (25/25, exit 0)
runs its four positive controls first.

## 1. Persona 1 -- constructive field theorist: S assembled backward, term by term

The record field `Psi` is a section over Y14 valued in `ker Gamma` = carrier B (dim 1664 of the RS
carrier 1792 = 14 x 128), graded by the Krein/C-operator inner product `K = eta_V (x) beta_S`. Every
term below is written to satisfy a specific boundary condition, and is cited to the artifact and
FORCED-row that forces it.

| Term | Schematic form | Forced by | What it supplies |
|---|---|---|---|
| **T1 record kinetic + mass** | `<Psi, Pi D_gimmel Pi Psi> + m2 <Psi, Pi Psi>` on ker Gamma | SA-C2 (g=1 cure, causal; leakage(g)=(1-g)C2, root g=1), SA-C4 (subprincipal passes, W125), SA-U4 (massive), A4 (ker Gamma = carrier B), A1 (the characteristic variety of `D_gimmel` IS the gimmel null cone, W131) | the record dynamics; and, via A1, the DERIVED conformal metric `[g]` (Malament: the causal order of the gimmel cone fixes `[g]` + topology + a maximal signal speed) |
| **T2 Krein/C grading** | the pseudo-unitary inner product `[P,S]=0`, `[K,Pi]=0` (W125), positive subspace `H_C+`, `eta_+ = eta C` | A4 (records = C-positive subspace, W132/W137), F3-sign (C-positivity), SA-U1 (H59 loop packet, tree leg `nabla K = 0`) | the admissibility of records AND the FORCED SIGN: `Lambda` is built from a trace over the POSITIVE subspace, so `Lambda >= 0` (F3) |
| **T3 count -> conformal factor + shadow-Lambda** | `Omega^2 ~ N(x)` (BLMS); `Lambda(x) = c / sqrt(N(x))`, `N(x)` = promoted C-positive count in the causal past | A1 (number -> conformal factor, BLMS), F3-magnitude (everpresent `Lambda ~ 1/sqrt(N)`, W146), A2 (N counts PROMOTED records only -> the 14->4 dimension collapse) | the DERIVED conformal factor `Omega` (completing `g` = `[g]` x `Omega`), and a POSITION-DEPENDENT `Lambda(x)` tracking record accretion |
| **T4 promotion-gate boundary term** | a boundary functional on the finality frontier; `delta S_gate` -> the promotion current `Q^nu` | A2 (measurement-gated projection; firewall = finality frontier = the (9,5) Krein q=5 indefiniteness image, W150), F1 (the interacting-vacuum exchange `nabla_mu(Lambda g) = Q`) | the exchange flux `Q`: a record promotes when `P_sigma D P_sigma` crosses the q=5 finality boundary, and the promotion flux across it is `Q` |
| **T0 induced gravity (NOT fundamental)** | the effective action obtained by integrating out `Psi`'s shadow = the W126 `|II|^2 + |H|^2` induced functional | F2 (bulk-flatness), F4 (a1=1/3 + split 3:2:1) | the derived metric's dynamics; because `g` is derived, `S_grav` is INDUCED, not postulated |
| **T5 matter/Yukawa sector** | `y_ij <psi_+, C phi_0 chi_->` on the k=0 form carrier | SA-Y1 (FORCED unique channel), SA-Y7a (FORCED doublet spurion type) | `T_munu` = the record/fermion content (A3); Hom-disjoint from T1-T4 (W125/W136) |

The decisive reverse-engineering consequence sits in **T0**: since the metric is DERIVED (A1), the
gravitational action is not an input but the INDUCED functional of the record shadow -- and the
induced functional is exactly W126's `|II|^2` reduction giving `a1 = 1/3` (F4) and the family whose
bulk constant is `a0_fam = 2 alpha - beta` (F2). So F2 and F4 are not separate postulates bolted on;
they are what the derived-metric sector MUST be. This is where forward builds spent an unbuilt
object and the reverse-engineering spends none.

## 2. Persona 2 -- rep theorist: the FORCED rows carried by one S, and the sign that signs Lambda

The 8 FORCED rows are carried by T1/T2/T5 exactly as W125's joint-carve certified NONEMPTY, and
nothing in the metric-is-derived move disturbs that certificate (the cure sector is Hom-disjoint
from the gravity and Yukawa clusters, W125/W136):

- **SA-C2 / SA-C4 / SA-U4** (cure `g=1`, subprincipal survival, massive RS): T1, unchanged from
  W125; `Pi` is the constant so(9,5)-equivariant ker-Gamma projector, `[K,Pi]=0` exact, leakage 0
  including the mass term. The shiab revision `t*=-1/6` (revising the written `(1,0,1,0)`) rides
  along.
- **SA-Y1 / SA-Y7a** (unique form-carrier Yukawa channel, doublet spurion type): T5, standing tests.
- **SA-G9** (matter-coupled linearization): in the reverse-engineered picture this is the statement
  that T0 (the induced gravity) is sourced by T5 (the record matter) -- the same-source closure that
  the 2026-06-24 map left `open`. NOT discharged here; named (Section 6).
- **SA-U1 / SA-U3** (H59 loop packet, Krein positivity bound): T2's grading; the tree leg holds
  (`nabla K = 0`), the loop arena stays OPEN (H59).

**The load-bearing new content of this persona: C-positivity SIGNS Lambda.** In a bare causal set
the everpresent fluctuation `Lambda ~ +/- 1/sqrt(N)` has a coin-flip sign (W146 Section 2.5). Here
`N(x) = Tr(P_sigma eta_+ P_sigma)` with `eta_+ = eta C` the C-positive metric (W132/W137), so `N`
is a trace over the POSITIVE subspace and is non-negative by construction; the everpresent
amplitude built from it is therefore `Lambda >= 0`, giving F3's forced positive sign. This is the
GU-specific pin the bare port lacks, and it is what makes F3 a CONSEQUENCE of T2 rather than an
extra postulate. (Honest boundary: that the C-metric BIAS actually delivers `Lambda > 0` at the
fluctuation level, not just the mean, is the W146 named-unbuilt "signed-positive-Lambda" prediction;
here it is the reason the sign is not free, carried at the conditional grade W146 set.)

## 3. Persona 3 -- interacting-DE / GR theorist: does S's variation give W144's Q(a)?

This is the debit-2 question, and the reverse-engineering answers it with a sharp PARTIAL that is
more informative than a yes.

**The bookkeeping (PORTED, W144/W152).** Keep `Lambda(x)` as a strict `w=-1` vacuum. The contracted
Bianchi identity `nabla_mu G^{mu nu} = 0` (the marble, kept because it is a geometric identity)
splits the total conservation into `nabla_mu(Lambda(x) g^{mu nu}) = -8 pi nabla_mu T^{mu nu}_matter =: Q^nu`.
So `Q` is the record-promotion flux (T4), and `Q(a) = rho_V'(a)` with `rho_V = Lambda/(8 pi)`.

**The obstruction the reverse-engineering EXPOSES (test RE1).** `Lambda(x)` is sourced by the
record count via `Lambda = c/sqrt(N)` (T3). Records only accrete and promotion is one-way (W146/W151:
the measured count is MONOTONE, giving time's arrow). So the MEAN `N(a)` is monotone increasing,
hence `Lambda_mean(a) = c/sqrt(N(a))` is monotone DECREASING, hence
`Q_mean = rho_V' < 0` for ALL `a`: **monotone withdrawal, no zero-crossing.** The everpresent mean
cannot produce F1's rise. This is a genuine finding: it localizes exactly why the naive "record
accretion sources dark energy" picture does NOT give the DESI rise-and-fall.

**Where the rise must come from, and what is DERIVED.** The rise (`Q>0` in the past) must be carried
by the NON-monotone piece: the everpresent FLUCTUATION `delta Lambda ~ +/- 1/sqrt(N)` with a
correlation length set by the 10 marginalized Y14 fiber directions (W146/W147). Test RE2 certifies
that a POSITIVE `Lambda(a)` = mean + a single-hump fluctuation keeps `rho_V > 0` throughout (F3)
while `Q = rho_V'` crosses zero exactly once (F1). So:

- **DERIVED (debit-2, the KIND and SCALE):** `Q` is a clock-coupled, sign-changing boundary flux
  (T4, forced), and its amplitude is O(1) in `q_B = 3 H0 rho_L` because the everpresent law forces
  `Lambda ~ 1/sqrt(N_4) ~ (l_p/R_H)^2 ~ H^2` (test PC3), which is exactly the O(1) Planck-ladder
  amplitude W144 fitted. The clock-coupling (the flux tracks the record-promotion rate) is what T4
  IS. These were the three things W144 said the source action "must carry"; here they are forced.
- **NOT DERIVED (debit-2, the EPOCH):** the specific single crossing at `z = 0.405` is a realization
  of the stochastic fluctuation. Test RE3 shows the crossing epoch tracks the free peak location:
  `S` does not pin it. So debit-2 moves from "fitted" to **PARTIAL**: amplitude + sign-changing
  character DERIVED, crossing epoch NOT.

**F2 under this S (beta/alpha=2).** Because the physical `Lambda` is boundary/record-supplied (T3/T4),
the BULK induced constant must vanish or it would double-count -- and the induced family
`alpha |II|^2 + beta |H|^2` vanishes its bulk constant `a0_fam = 2 alpha - beta` at exactly
`beta/alpha = 2` (test PC1, W136). So in the reverse-engineered picture beta/alpha=2 is not an
independent selection; it is FORCED by A1+F3 (the metric is a shadow and `Lambda` is record-supplied,
so the bulk must be flat). The Einstein channel stays attractive there (`a1_fam = 3 > 0`), and the
scalaron stays tachyonic (`a2 = -1/9`): S inherits GU's own R^2 problem (H59), exactly W152's
"marble augmented."

## 4. Persona 4 -- numerical engineer: positive controls and the over/under-determination count

`tests/W154_reverse_engineered_source_action.py`, 25/25, exit 0. Positive controls first:

- **PC1** reproduces the W136 bulk-flatness anchor: `a0_fam = 2 alpha - beta`, `beta/alpha* = 2`,
  Einstein `a1_fam = 3` attractive, native `a1 = 1/3` (F4), tachyon `a2 = -1/9`.
- **PC2** reproduces the W144 CPL crossing `a_x = 0.71163`, `z_x = 0.40523`.
- **PC3** reproduces the everpresent amplitude `1/sqrt(N_4) = (l_p/R_H)^2 ~ H^2`, O(1) `q_B`.
- **PC4** reproduces `(3,1) + (6,4) = (9,5)` and the `q=5` finality frontier (W150).

Then the reverse-engineering's own computations: RE1 (the obstruction: monotone `N` -> sign-definite
`Q_mean`), RE2 (F1 ^ F3 jointly satisfiable: positive single-hump `Lambda` -> `rho_V>0` while `Q`
crosses zero once -> NO over-determination conflict), RE3 (crossing epoch unpinned), and CC1-CC3
(the constraint-vs-free-object count).

**The verdict is UNDER-DETERMINED, not over-determined.** Sixteen constraints (A1-A4, F1-F4, the 8
FORCED rows) are imposed simultaneously with no surviving conflict -- the sharpest candidate for a
conflict, F3 (sign forced +) against F1 (sign-changing Q), dissolves under inspection: F3 is about
the sign of the FIELD `Lambda` (positive), F1 is about the sign of its RATE `Q = Lambda'` (changes
once); a positive `Lambda` with an interior maximum satisfies both (test RE2). The residue is a named
set of free objects (Section 6). The reverse-engineering also REDUCES freedom relative to the forward
builds: the 10 metric functions `g_munu` are removed (metric derived), `sign(Lambda)` is fixed +,
and the SA-G5 shape-dim-1 freedom collapses to `beta/alpha = 2`.

## 5. Persona 5 -- honesty auditor / E1: is S a coherent object or a wish-list?

Per E1, a reverse-engineered S that merely re-lists the constraints is NOT progress; it must either
DERIVE a fit, EXPOSE a conflict, or REDUCE the free-function count. This S does the first and third
and a variant of the second, so it clears the bar:

- **DERIVES a fit (partially):** debit-2's amplitude and sign-changing character are forced (Section
  3). Not the epoch. PARTIAL, stated as such.
- **REDUCES the free-function count:** the metric stops being 10 free functions and becomes a
  functional of `Psi` and `C`; `sign(Lambda)` stops being a free bit; `beta/alpha` stops being a
  shape-dim-1 band and becomes forced to 2. This is a real reduction, the honest content of "coherent
  object, not wish-list."
- **EXPOSES structure at the conflict frontier:** the F3-vs-F1 apparent conflict is resolved (field-
  sign vs rate-sign) rather than papered over, and the debit-2 obstruction (monotone accretion ->
  monotone withdrawal) is a precise, previously-unstated localization of why the mean cannot do the
  job.

**What keeps it honest / where the wish-list charge partially lands.** Three of the load-bearing
identifications are conditional, not closed: T3's `Lambda = c/sqrt(N)` normalization uses the free
`phi = 1/(3 Omega_L)^2` (W146: a fit, its derivation from the (9,5) fiber measure unbuilt); T0's
`a1 = 1/3` magnitude rides the unbuilt eta-from-gimmel-area bridge (W151: only the SIGN is forced);
and the whole `Lambda`-term divergence-freedom routes through C3 of the 2026-06-22 proof (`theta` =
EL derivative of a gauge-invariant action on Y14), undischarged. So `S` is a coherent SHAPE with a
named unbuilt core, not a closed action. The E1 verdict: PROGRESS (a partial derivation + a genuine
reduction + a precise obstruction), explicitly short of a built S.

## 6. The consistency verdict, the free objects, and the single unbuilt object

**Consistency verdict: UNDER-DETERMINED (free functions remain), NOT over-determined.** One `S`
satisfies A1-A4 + F1-F4 + the 8 FORCED rows with no surviving conflict; the residue is:

1. `phi` = the measured-record 4-density normalization (W146; a fit; the (9,5) DeWitt-fiber-measure
   derivation is the strongest open novelty target).
2. the fluctuation correlation length / phase -> the specific crossing epoch `z_x` (the F1 debit-2
   residue; `S` derives the KIND and SCALE of `Q`, not the epoch).
3. the eta-from-gimmel-area bridge (W151): links route-beta's Einstein magnitude to route-alpha's
   `a1 = 1/3`; only the sign is forced.
4. `mu_DW` = the one free dimensionful scale (SA-G2; H36 stays refused).
5. the Yukawa FIT rows (vev, couplings, spurion values; Hom-disjoint, untouched).
6. C1/C2/C3 of the 2026-06-22 divergence-free proof (`theta` = EL derivative of a gauge-invariant
   action on Y14) -- undischarged.

**The single remaining unbuilt object, sharpened.** Across the forward waves it was "the covariant
operator on Y14 as a dynamical action deriving `Q`." The reverse-engineering sharpens it to: **the
promotion-gate boundary term T4 whose variation yields `Q`** -- concretely, the derivation that the
C-positive promotion flux across the (9,5) `q=5` finality frontier has a fluctuation two-point
function producing a single O(1) sign-change in the observable window. Equivalently: discharging C3
for the record field. Closing that one object would simultaneously supply `Q` genuinely (debit-2
epoch), give the equivariance/Noether route a concrete action, and open the same-source `T_munu`
bridge (SA-G9). It is the load-bearing unbuilt object, now named on the boundary, not in the bulk.

## 7. What this does NOT do (the kill comes after)

- Everything is conditional / exploration grade; assumption-first hypothesis generation. Nothing
  asserts GU, that the DESI wiggle is real (W144 fits it as HYPOTHESIS; the DR3 bet is live, opposite
  to W141 S1), or that any decomposition is physical.
- The interacting-vacuum decomposition, the everpresent-Lambda law, and the Malament/BLMS/Jacobson
  emergence are PORTED and labelled; the rise-and-fall SHAPE and the everpresent MAGNITUDE are
  generic (G5 bites on the magnitude, W146/W138). The GU-specific content is the sign pin (T2), the
  `beta/alpha=2` selection (T0/F2), and the structural localization of the promotion gate on the
  (9,5) q=5 frontier (T4/W150).
- `S` is not a built functional on sections of the Y14 bundle; the three failing legs (phi, the eta
  bridge, C3) trace to the same unbuilt boundary term (Section 6). H41 stays unbuilt; the count stays
  {1,3}; H59 stays OPEN.
- No canon / RESEARCH-STATUS / claim-status / verdict / posture change; no spec FIT row moves.
  Tri-repo gating honored: "record / substrate / issuance / promotion / finality" are local postulate
  labels (W136 sense); the issuance concept is owned by temporal-issuance, MEASURE by time-as-finality;
  GU owns the field-equation / emergent-metric math only; no cross-repo identity claim. Zero em dashes
  in paper-facing text. W138 battery honored (G1-G6); B2 rate-identity FALSE and unused; H36 refused.

*Filed 2026-07-14 by Team REVERSE (W154). Five personas inline in one worker (constructive field
theorist, rep theorist, interacting-DE/GR theorist, numerical engineer, honesty auditor/E1); no
sub-agents. Reproducible: `python -u tests/W154_reverse_engineered_source_action.py` (25/25, exit 0;
four positive controls first). Exploration grade; conditional register; no canon movement; H41
unbuilt; H59 OPEN.*
