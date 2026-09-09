---
title: "K176 last-contraction exchange-orbit tail wave"
document_role: active_research
doc_type: conditional_native_K139_K176_adjacent_contraction_cancellation_and_exchange_orbit_tail_result
created: 2026-09-09
date: 2026-09-09
claim_ceiling: exact repository-owned coefficient-specific all-order exchange seed-orbit convergence for the K139--K175 signed point control; finite-cutoff endpoint renormalization cancels the adjacent Wick contraction before the limit and every surviving older-letter exchange carries two resolvents, giving a sector-uniform order-n bound and an explicit post-adjoint tail below 1/250 after order 12, but the resolved exchange vectors through order 12, complete base action column, R_ref residual, complement or flux floor, scalar-center left floor, K152 interval, physical/source selection, Born derivation, prediction and confirmation remain open
manifest: lab/process/k176-last-contraction-exchange-orbit-tail-wave.json
solver: tests/channel-swings/k176_last_contraction_exchange_orbit_tail.py
probe: tests/channel-swings/k176_last_contraction_exchange_orbit_tail_probe.py
target_claim: INTERNAL_TARGET:K175_COMPLETE_ALL_ORDER_EXCHANGE_COEFFICIENT_AND_CAR_TAIL
target_claim_verdict: EXCHANGE_TAIL_CONVERGENT_AFTER_ADJACENT_CONTRACTION_CANCELLATION_RESOLVED_PREFIX_OPEN
canon_verdict_change: none
---

# K176 last-contraction exchange-orbit tail wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet stays on the repository-supplied K139--K175 equal-coupling
two-edge positive particle/hole point control at auxiliary chart `256`, and on
the exact normalized K162 zero-bath seed orbits. It proves a
coefficient-specific orbit estimate. It does not make the isolated point trace
continuous on a global graph domain and does not alter K174's obstruction.

```gu-typed-objects
result: finite-cutoff endpoint renormalization cancels the adjacent Wick contraction in C_N A_N^-1 C_N* G_N^n phi; the surviving annihilator has exactly n older creation letters to hit and each term carries two resolvents, so the complete 16-monomial exchange contribution has a summable sector-uniform seed-orbit tail
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space over L2(R;C4), in q=(0,0),(1,0),(0,1), with fixed K139 chart and normalized K162 zero-bath seed lines LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive physical Fock Hilbert pairing transported by S=(1-G_256)^-1 to M=S* S; CAR creation and annihilation maps are contractions after coefficient smearing ON=repository_signed_point_control
real_structure: CAR adjoint, momentum conjugation, Hermitian normal-ordered bath blocks and the K168 real flavor-symmetric reference shape
grading: conserved incidence charges, hard-core impurity degree, bath-particle number, free-energy weight, Neumann word order and K162 level
action_owner: repository-construction -- K156 owns finite-cutoff matched normal ordering, K161 owns the 16 exchange-monomial census, K172/K175 own D_256, and K153 owns the Hilbert contraction; no source/GU action selects an extension, state, domain or scalar center
target: serialize the exact all-order exchange coefficient on each seed word, prove a sector-uniform CAR sum bound, and close the K171 unresolved exchange tail without claiming the still-unevaluated resolved vector prefix MAP-TYPE=intertwiner
```

## Inline preflight bookend

K175 correctly refused to assign the diagonal `D_256` estimate to four
isolated exchange traces. Its proposed next premise was phrased as a possible
cross-term cancellation. The finite-cutoff normal form shows the sharper fact:
cross-polarity cancellation is not required and is not asserted. The actual
cancellation is the adjacent Wick contraction against the matched endpoint
counterterm, before removal of the cutoff.

The evidence chain is K156's exact finite normal ordering, K161's complete
exchange census, K172/K175's resolvent-difference bound, and K153's normalized
Hilbert contraction. No source or external evidence is introduced.

## 1. The adjacent contraction is the endpoint term

Write the finite-cutoff order-`n` seed word as

`G_N^n phi=(-A_N^-1 C_N*)^n phi`.

In `C_N A_N^-1 C_N* G_N^n phi`, commute the left annihilator through the
newly adjacent creation operator first. The resulting Wick contraction is
exactly the diagonal endpoint coefficient `c_N D G_N^n phi`. K156 subtracts
that same term in the finite expression. Thus

`G_N* A_N G_N-c_ND = X_N`

is formed before `N -> infinity`; the raw divergent contraction never enters
the limiting exchange coefficient.

After that cancellation the annihilator can contract only with a creation
letter already present in `G_N^n phi`. There are exactly `n` such older-letter
positions per exchange monomial. Fermionic signs change phases, not norms.
This is the complete all-order coefficient identity needed here. It is not a
cancellation between polarity blocks.

## 2. Every older-letter exchange has two resolvents

If the contracted older letter carries momentum `p`, one denominator comes
from that creation letter and a second comes from the outer exchange
resolvent. Nonnegative energies of all spectator letters only enlarge those
denominators. The absolute created-leg coefficient is therefore dominated by

`J_256(e)=D_256(e)/e`.

K172/K175 give `D_256(e)<=(1/3)e^(1/4)`. Hence

`J_256(e)<=(1/3)e^(-3/4)`.

At `e=omega(p)=sqrt(1+p^2)`,

`||J_256(omega)||_2^2 <= (1/9) int_R (1+p^2)^(-3/4) dp`.

Split the positive half-line at one. On `[0,1]` the integral is at most one;
on `[1,infinity)` it is at most `int_1^infinity p^(-3/2)dp=2`. Doubling gives
an integral at most six, so

`||J_256(omega)||_2^2 <= 2/3 < 25/36`

and therefore `||J_256(omega)||_2 < 5/6`. This deliberately rational rounding
keeps every later bound exact.

## 3. Complete CAR census and order bound

K161's native normal-order census has four ordered edge pairs and four
polarity blocks for each pair: `16` exchange monomials. Creation and
annihilation by a fixed `L2` coefficient have operator norm equal to the
coefficient norm on every fermionic sector. Applying the triangle inequality
over the complete census and the `n` older-letter slots therefore gives, for
every normalized K162 seed and every `n>=1`,

`||X_ex,n G^n phi|| <= 16*(5/6)*n*(3/8)^(n-1)`

`                         = (40/3)n(3/8)^(n-1)`.

This estimate is uniform in particle number and cutoff. The two-resolvent
majorant is integrable, so finite-cutoff coefficient convergence passes each
term to the native limit; the displayed summable majorant permits the
all-order limit. K174 remains intact because no isolated unsmeared trace has
been promoted to a bounded global operator.

## 4. K171 post-adjoint exchange tail

K171 adds the lowering words on the left. Their Hilbert Neumann sum is at most
`1/(1-q)` with `q=3/8`. Resolving exchange orders through `N` leaves

`T_ex(N) <= (40/3)/(1-q) * sum_(n=N+1)^infinity n q^(n-1)`

`        = (40/3) q^N ((N+1)-Nq)/(1-q)^3`.

The deliberately conservative order-one value is `T_ex(1)<=832/25`. After
order twelve,

`T_ex(12) <= 3011499/838860800 < 1/250`.

Thus the complete native exchange contribution has a certified all-order
tail on every named seed orbit. This closes the convergence gate left by K175.

## 5. What the result releases—and what it does not

K176 releases finite evaluation: compute the actual native exchange vectors
for orders `1` through `12`, in the same vector basis as the scalar and
diagonal pieces. The tail then contributes less than `1/250` to the complete
post-adjoint exchange column.

K176 does not evaluate that finite vector prefix. Consequently it does not
yet produce the coefficient-complete base action column, `M`-dual
`R_ref` residual, positive complete `M`-orthogonal complement or flux floor,
scalar-center left floor, or native K152 interval. The distinction matters:
convergence of an action column is not its numerical evaluation.

## Residual replay and outward boundary

The scalar `-256M` tail and the diagonal tail remain exactly as certified by
K175. The exchange tail is now closed by the all-order normal form above, not
by the invalid componentwise `4/pi` shortcut. The next complete residual must
combine the explicitly resolved exchange prefix with those pieces and the
K168 reference shape in one common `M`-dual calculation.

The result leaves `SC-META-53` `UNCERTAIN`, and `LT-SM8`, `RA-F1`, and `AC-F1`
`NEEDS`. It selects no physical extension, state, polarization, scalar center,
source action, observable, or threshold. It earns no Born, prediction,
confirmation, paper, canon, release, or public-posture credit.

## Postflight bookend

The K175 fork is decided. The all-order exchange seed-orbit tail converges,
but for a different reason than cross-polarity cancellation: finite-cutoff
endpoint matching removes the adjacent contraction, and the surviving
older-letter terms gain a second resolvent. The honest next gate is finite and
vector-valued: evaluate orders through twelve, then assemble the complete
base/reference action column and its residual before attempting any
complement/flux or K152 conclusion.

## Reproduction

Run:

```bash
python3 tests/channel-swings/k176_last_contraction_exchange_orbit_tail.py --demo
python3 tests/channel-swings/k176_last_contraction_exchange_orbit_tail_probe.py
python3 tests/channel-swings/k176_last_contraction_exchange_orbit_tail_probe.py --selftest
```

Expected: `40/40` exact controls and `27/27` hostile mutations caught.
