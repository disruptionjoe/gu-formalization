---
title: "K1987: Parametric thermal regularity and exact feasibility"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1987_thermal_spacing_parametric_frontier.py
  - tests/channel-swings/k1987_thermal_spacing_parametric_frontier_probe.py
---

# K1987: Parametric thermal regularity and exact feasibility

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
result: lower semicontinuity, finite algebraic parameter structure and complete feasibility domain
carrier: fixed finite catalyst dimension, four-level bath and positive minimum spacing LAYER=toy CHIRALITY=N/A
pairing: worst-input catalyst marginal half trace distance ON=independent_initial_registers
real_structure: finite complex conserving unitaries and real nondegenerate energies
grading: physical energy shells, not source chirality
action_owner: repository-construction -- unchanged extreme four-state channel
target: spacing and upper-budget dependence of the actual physical optimum MAP-TYPE=intertwiner
```

## Parametric question and result

Keep [K1981](k1981-wide-spacing-thermal-frontier-2026-10-23.md)'s exact channel,
bath energies0,1,2,3 and weights t^b/Z(t),0<t<1. Let F_d(delta,E,t) be the
optimal worst-input catalyst marginal half trace distance with at most d
nondegenerate levels, ground0, minimum gap delta>0 and mean energy AT MOST E.
Use +infinity for infeasible parameters, solely as an optimization convention.

For each fixed finite d, F is jointly lower semicontinuous on delta>0,0<t<1.
It is nondecreasing in delta and nonincreasing in E. Therefore it is
LEFT-continuous in spacing and RIGHT-continuous in budget at feasible points.
It is not generally right-continuous in spacing. Its feasible graph and finite
value graph are semialgebraic. Each one-parameter slice has only finitely many
jumps and is piecewise algebraic, with the parameters fixed. At algebraic
parameters the optimum, when feasible, is algebraic. No rationality claim
is made for arbitrary spacing.

## Uniform compactness proves the direction of continuity

Reuse K1978's protocol-preserving component translation. On a neighborhood
with delta bounded above by D and actual dimension n<=d, its spectra can be
put into the common compact interval

    [0,(d-1)(D+3(d-1))+3(d-1)].                         (1)

This retains the original unitary/channel/return while lowering energy.
For delta bounded below away from0, ordered levels cannot collide in a limit.
Choose optimizers along any parameter sequence converging to a feasible or
infeasible target. A subsequence has fixed actual dimension and convergent
spectrum, density and unitary. Conservation, exact channel and upper-budget
conditions pass to the limit. New resonances cause no problem: the full
commutator is a closed equality. Gibbs weights are continuous for0<t<1.
Worst-input trace distance is continuous because its input-state set is compact.
The limit is feasible and has the limiting return, proving lower semicontinuity.

For delta_j increasing to delta, monotonicity gives F(delta_j)<=F(delta),
while lower semicontinuity gives the reverse inequality for the limit. For
E_j decreasing to E, monotonicity likewise gives F(E_j)<=F(E), and the same
argument proves right-continuity. The reverse directions do not follow.
K1981's physical delta1 witness proves a strict RIGHT jump for d>=5,E>=2.
Thus interpolation across a detected resonance threshold needs a one-sided
bound, not an assumed continuous curve. Nothing here is uniform as delta->0
or as d->infinity; those limits lose the compactness used above.

## Finite algebraic structure, including coherent protocols

This statement uses the actual finite-dimensional physical data, not a grid.
Fix an actual dimension n<=d and introduce real/imaginary entries of U and rho,
ordered energies e_i, and delta,E,t. Unitarity, trace-one positivity (principal
minors), ground/spacing, conservation and mean budget are polynomial equalities
and inequalities. Exact channel equality is imposed on a finite matrix-unit
basis. Clear the positive denominator Z(t)=1+t+t^2+t^3. The fixed target's
coefficients are algebraic.

The trace-norm return bound is also a formula over real polynomial inequalities:
for every input density sigma, require a decomposition of its Hermitian return
difference as A-B, A,B positive semidefinite, with tr(A+B)<=2r. Existence of
such a decomposition is equivalent to half trace norm<=r by the positive and
negative spectral parts. This is a universal input quantifier followed by
existential A,B; exchanging those quantifiers would change the problem.
Conjoin the protocol constraints and existentially quantify the protocol.
The finite union over n<=d defines an exact feasible-return relation S.

The finite value graph is

    S(delta,E,t,r) AND NOT exists s<r: S(delta,E,t,s).    (2)

Attainment from compactness justifies using an actual minimum in(2).
The [Tarski-Seidenberg projection theorem, Appendix A.4.4](https://www.mit.edu/~parrilo/sdocag/SIAMBookFinalvNov12-2012.pdf)
then gives semialgebraicity: finite Boolean operations and quantified polynomial
relations remain semialgebraic. This is a standard theorem applied to the
explicit physical encoding, not a claim of a practical quantifier-elimination
implementation. One-variable semialgebraic cell decomposition partitions the function graph
into finitely many points and continuous algebraic branches. Thus every
one-parameter slice, including temperature where monotonicity was not proved,
has only finitely many discontinuities. Isolated values at algebraic
parameters are algebraic.
No universal bound on the number of pieces or small-spacing rate is supplied.

## Executed consumers: complete feasibility and the three-level frontier

A lowest occupied energy e has a bath0 shell requiring a distinct lower
physical level e-b, b in{1,2,3}; hence e>=1. A highest occupied energy similarly
needs a higher physical level through bath3. At least three physical levels
are necessary. For delta<=1, the actual spectrum{0,1,2}, pure at1, meets all
four shell-rank constraints and has mean1. For delta>1 reuse K1981's forced
partners e-2,e+2, which require mean>=2 and delta<=2; {0,2,4}, pure at2,
attains those bounds. Consequently, for EVERY0<t<1 the exact feasible domain is

    d>=3 AND 0<delta<=2 AND E>= [1 if delta<=1, else2].  (3)

This closes all spacing/budget/dimension feasibility, without pretending to
solve all optimal returns. At E=1 and delta<=1 every feasible preparation is
supported at the sole level1, so the optimum return is1/2, for every d.

For actual dimension3, only the middle level can be occupied. Write the
spectrum{0,a,a+b}. The bath0 and bath3 shells force a,b in{1,2,3}.
The lower partner covers bath labels k<=3-a; the upper covers k>=b.
All four labels are covered precisely when a+b<=4. There are exactly SIX
spectra, all actual and nondegenerate. Every one has sharp return1/2.
Thus F_3=1/2 on the full feasible domain(3), at all temperatures. The largest
feasible spacing is1 when1<=E<2, and2 when E>=2, for every d>=3.

The producer executes all six spectra,252 parameter controls and30 exact
thermal returns. The separate probe enumerates bath labels independently,
checks rational-spectrum stress cases, and rejects spectrum, spacing, budget
and return faults after baseline. The real-spectrum completeness is the
partner argument, not the finite stress census. General regularity and
semialgebraicity are analytic results, not falsely labeled code proofs.

## Boundary and next use

Strongest overclaim is reversing the continuity direction; the known physical
jump is a contrary control. Compactness requires positive spacing and fixed
dimension; algebraicity does not imply a small algorithm or a rational optimum.
The next useful thermal work is a quantitative small-spacing lower bound or
an actual higher-dimensional parametric curve, with thresholds located before
interpolation. Existing five-level reciprocal-lattice results remain intact.
This is independent thermal mathematics; SC-META-53 remains UNCERTAIN and no
source, physics-ledger, canon or public physical verdict changes.
