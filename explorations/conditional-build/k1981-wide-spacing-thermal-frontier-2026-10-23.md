---
title: "K1981: The complete wide-spacing thermal frontier and its jump"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1981_wide_spacing_thermal_frontier.py
  - tests/channel-swings/k1981_wide_spacing_thermal_frontier_probe.py
---

# K1981: The complete wide-spacing thermal frontier and its jump

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
result: exact all-energy wide-spacing optimum and strict threshold discontinuity
carrier: finite nondegenerate catalyst and four-level Gibbs bath with 0<t<1 LAYER=toy CHIRALITY=N/A
pairing: positive trace and worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex conserving unitaries and real spectra with minimum gap delta
grading: occupied energy-shell rank, not density rank
action_owner: repository-construction -- fixed extreme four-state Schur channel
target: physical dimension/energy/spacing resource frontier MAP-TYPE=intertwiner
```

## 1. Complete answer for spacing greater than one

Keep [K1978](k1978-thermal-spectral-spacing-2026-10-23.md)'s changed resource
model, with the exact extreme four-state Schur channel and bath energies0,1,2,3.
The argument extends from t=1/2 to EVERY 0<t<1, with Gibbs weights proportional
to t^b. Allow coherent initial catalyst preparations, dimension at most d,
nondegenerate ground-zero energies, minimum adjacent gap delta, and mean
energy AT MOST E. Return is the worst-input catalyst MARGINAL half trace
distance, not joint/product return or approximate simulation.

For1<delta<=2 the COMPLETE frontier is

    F_(d,delta,t)(E)=1/2  if d>=3 and E>=2,
    infeasible otherwise.                                 (1)

For delta>2 it is infeasible for every finite d and E. Thus adding arbitrarily
many levels or energy budget cannot improve the return in the wide-spacing
regime. K1978 only proved the minimum-energy edge E=2; (1) settles ALL budgets.
The minimum is attained by the actual three-level protocol{0,2,4}, prepared
at 2. No compactness/limit argument is required to attain this value.

## 2. Forced partners forbid occupied-shell overlap

First pinch the preparation in the catalyst energy basis. The inherited
covariance/convexity reduction preserves the exact channel and mean energy,
and cannot increase return. A lower bound for diagonal preparations therefore
bounds arbitrary coherent preparations as well.

The exact shell-rank theorem is reused from
[K1968](k1968-joint-thermal-finite-dimension-program-2026-10-22.md): in every
occupied bath/catalyst shell, the number of physical environment directions
must be at least twice the number of occupied input directions. It is also
sufficient with the established full-channel shell unitaries. All four bath
probabilities are nonzero for 0<t<1.

For any occupied energy e, its bath-index 1 shell can have only one other
physical direction when delta>1: e-2. Its bath-index 2 shell similarly requires
e+2. Hence e-2,e,e+2 must be actual catalyst levels. In particular e>=2;
three levels are necessary, and delta>2 is impossible.

Two occupied energies cannot differ by 1 because of spacing. They cannot
differ by 3: the forced partner e+2 would lie distance1 from e+3.
They cannot differ by 2 either. The shared shell at e+2 would have two
occupied input directions (bath labels2 and 0), but its only permitted
physical positions are e and e+2; e-1 and e+1 violate spacing from an
occupied level. The rank requirement would read4<=2, a contradiction.
The same reasoning applies to negative differences by exchanging levels.

Therefore distinct occupied energies never differ by 1,2 or3. Noninteger
separations do not share a bath shell at all. Every occupied shell has just
ONE occupied input direction, regardless of additional unused levels.

## 3. The sharp return formula collapses to one half

For a diagonal preparation p_e and bath weights g_b, the inherited sharp
all-input return formula sums retention at each occupied e as

    retained_e=(1/2) sum_(b=0)^3 max_{f+c=e+b}(p_f g_c),
    R=sum_e (p_e-retained_e)_+.                            (2)

The maximization includes occupied input directions, not unoccupied physical
padding. When occupied shells never overlap, each maximum in(2) is just
p_e g_b, so retained_e=p_e/2 and R=1/2. Formula(2) is a lower bound on
all allowed unitaries and is attained by the full-shell construction.
This does not assert that every nonoptimal unitary has error exactly 1/2.

The pure occupied level 2 in spectrum{0,2,4} satisfies all four shell-rank
conditions. It has mean 2, spacing 2, dimension 3 and sharp return 1/2 at every
temperature parameter 0<t<1. It supplies the upper bound in(1) for every
E>=2,d>=3,delta<=2. The support argument supplies the matching lower bound.
Finite resources at exact energy different from2, degeneracies, another bath,
a different target channel and approximation remain different problems.

## 4. Executed threshold consumer: a strict discontinuity at delta=1

At delta=1, the actual five-level spectrum{0,1,2,3,4} can have occupied
levels 1 and 3 with populations1/2 each. Its mean energy is 2 and the shell-rank
inequalities hold. Summing the bath labels in(2) gives exactly

    R_boundary(t)=(1+3t^2)/(4(1+t^2)) <1/2,
    1/2-R_boundary(t)=(1-t^2)/(4(1+t^2))>0.                (3)

For every d>=5 and E>=2, this witness proves a strict right discontinuity of
the optimal return as delta rises through1. The jump is at least(3);
we do not claim this particular witness optimizes delta=1. At t=1/2 it has
R=7/20 and proves a jump of at least3/20. More unused levels and budget
cannot remove the jump on the delta>1 side. This is an exact-conservation
resonance effect, not a numerical instability or a claim about approximate
conservation. No uniform positive lower jump as t approaches1 is asserted.

## 5. Verification and scope

The producer checks all three local resonant occupied gaps,25 physical
families and five exact temperature-dependent boundary witnesses. A separate
bath-label implementation checks95 energy/return obligations and enumerates
32 feasible spectrum/support controls on a half-unit grid. It rejects four
actual spectrum/return-factor/energy/population perturbations after baseline.
The proof in sections2-3 covers ALL real spectra and all finite dimensions;
the finite census does not establish that universal quantifier.

Strongest overclaim: a lower bound on pinched states silently excluding
coherence; the covariance reduction explicitly supplies that bridge.
Strongest contrary construction: extra empty shell positions; spacing rules
exclude them in the only dangerous shared shell. Weakest scope boundary is
strict delta>1: the actual witness(3) shows why it cannot be weakened.
The remaining quantitative small-spacing gap and matching optimal family are
open, now restricted to0<delta<=1. Conditional independent mathematics only;
SC-META-53 remains UNCERTAIN, and all source/physics-ledger/canon verdicts stay
unchanged. No novelty, external expert or proof-assistant certification claimed.
