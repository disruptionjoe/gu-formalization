---
title: "K1882: Effective transport of all three Fisher well profiles"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: all-density finite rescaled Wasserstein bounds with actual cell weights; no sharp rate, sextic spectral gap, entropy of hard cells or GU identification
---

# K1882: Effective transport of all three Fisher well profiles

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
result: explicit rescaled conditional well transport and second-moment tail control
carrier: real densities with raw moments2=1,4=k>3,6<=k²+delta LAYER=toy CHIRALITY=N/A
pairing: Fisher energy and quadratic transport ON=real_H1_square_roots
real_structure: nonnegative real densities
grading: nearest-root labels and small-slack scale
action_owner: repository-construction -- constrained Fisher functional
target: effective Gaussian conditional-profile transport MAP-TYPE=evaluation
```

## 1. Result and the missing tail argument

Use K1880's exact hypotheses, notation, cutoff functions and constants:
raw moments E X²=1, E X4=k>3, E X6<=k²+delta; finite Fisher I;
a proved bound delta I<=U; A=k+1, roots r=0,+sqrt(k),-sqrt(k),
a=(k,2k,2k), b_j=a_j A. Write C_j for the nearest-root cells and
p_j=P(C_j). Our W2 convention is the square root of the minimum expected
squared distance, with no factor1/2.

Reuse [K1880](k1880-effective-fisher-well-localization-2026-10-21.md)'s
```
e=4sqrt(delta)/(3k), epsilon=13h/(4sqrt(k)), tau=4e²/h²,
0<h<=sqrt(k)/4,
E=U-A²+A²[(1-epsilon)^(-2)-1]
  +2A e(1+sqrt(k))+4A k tau+40delta/h².
```
Define the additional quantities
```
Kcap=U+40delta/h²,
Splus=max(0,A-e(1+sqrt(k))-2k tau),
D=1-(1-epsilon)² Splus²/Kcap,
B=E/(kA)²+16D/(9k²)+tau/(kA).                         (1)
```
For every feasible density with a valid U, E,D,B are nonnegative. Then
```
sum_(j:p_j>0) p_j W2(law((X-r_j)/sqrt(delta) | C_j),
                         N(0,1/b_j))² <= B.             (2)
```
In particular every positive-mass cell has W2<=sqrt(B/p_j).
The mass denominator cannot be discarded. Actual cell weights are retained;
there is no balance or mean-zero assumption.

At k=4,delta=10^-12,U=25.002,h=10^-4 the exact rational bound is
B<0.0112². For an even density the central conditional W2 is<0.013 and
each outer conditional W2 is<0.032. These are errors in the rescaled
coordinate, not physical units. K1876's trial proves this U for the exact
even optimizer. A supplied competitor must itself meet the energy bound.

K1878 proves qualitative W2 convergence; K1880 proves finite TV and
unscaled W2. Neither already establishes (2). Small TV alone cannot control
rescaled second moments: (1-eps)N(0,1)+eps N(eps^-1/2,1) approaches the
standard Gaussian in TV while its second moment tends to2. The new step
below bounds the discarded *second moment*, not merely discarded mass.

## 2. Energy allocation leaves only D of the potential budget in the tail

Set u=sqrt(p), u_j=chi_j u, m_j=integral u_j², and
```
M=sum_j a_j² integral (x-r_j)² u_j² / delta,
Kloc=4delta sum_j integral |u_j'|²,
S=sum_j a_j m_j.
```
Compact support of each u_j and integration by parts give
`S=-2sum a_j integral (x-r_j)u_j u_j'`. Thus Cauchy-Schwarz gives
S²<=Kloc M. K1880's IMS estimate gives Kloc<=Kcap and its mass
estimate gives S>=Splus, so M>=Splus²/Kcap.

Let g=x³-kx and d=distance(x,{r_j}). K1880 proves globally
`g²>=9k² d²/16` and locally `g²>=(1-epsilon)² a_j²(x-r_j)²`.
The sixth-moment cap is exactly integral g²p<=delta. Since the cutoffs
have disjoint supports, the nonnegative leftover r=p-sum u_j² satisfies
```
integral g² r /delta <=1-(1-epsilon)²M <=D,
integral d² r /delta <=16D/(9k²).                        (3)
```
This also proves D>=0 for any valid U. No guessed U may be made valid by
clipping a negative budget. The lower energy allocation is the missing
uniform-integrability estimate. The first inequality uses the full cap,
not equality or optimizer-specific Euler equations.

## 3. Gaussian transport of localized densities

For m_j>0, let nu_j be u_j²/m_j in the rescaled variable y=(x-r_j)/sqrt(delta),
and gamma_j=N(0,1/b_j). The exact oscillator deficit is
```
E_j=4delta||u_j'||²+(b_j²/delta)||(x-r_j)u_j||²-2b_j m_j.
```
Integration by parts identifies its relative Fisher information as
`I(nu_j|gamma_j)=E_j/m_j`. This is valid for the smooth/Lipschitz
cutoff square root, not for a hard cell truncation extended by zero.
K1880 supplies E_j>=0 and sum E_j<=E.

In our normalization Gaussian log-Sobolev and quadratic transport state
```
H(nu|gamma_b)<=I(nu|gamma_b)/(2b),
W2(nu,gamma_b)²<=2H(nu|gamma_b)/b,
```
so `m_j W2(nu_j,gamma_j)²<=E_j/b_j²`. These standard inequalities
are reviewed by Chafai and Lehec, [Logarithmic Sobolev Inequalities Essentials](https://djalil.chafai.net/docs/M2/chafai-lehec-m2-lsie-lecture-notes.pdf),
sections1.3 and3.2; normalizations of transportation cost differ, so the
constants here are also checked by translated Gaussians. Approximation
extends the form-domain statement to cutoffs with zeros. The same argument
bounds the **localized** weighted relative entropy by sum m_j H<=E/(2kA).
It does not assert a relative-entropy bound for hard conditional cells.

## 4. Reattach the real tails, rather than replacing the target distribution

In cell j the actual subprobability is u_j²+r_j, of mass p_j,
where r_j is the restriction of r. Couple u_j² optimally to m_j gamma_j.
Couple the residual r_j independently to (p_j-m_j)gamma_j. Because gamma_j
has zero mean, the second cost is exactly
```
integral_Cj (x-r_j)² r(x)/delta dx +(p_j-m_j)/b_j.
```
Here r_j in the integrand denotes the root; r(x) denotes residual density.
Adding the two couplings and dividing by p_j yields a coupling of the
actual hard conditional cell with gamma_j. Summing, using (3),
sum(p_j-m_j)<=tau and b_j>=kA proves (1)-(2). Cells with m_j=0
use only the residual coupling; cells with p_j=0 are omitted.
No differentiability or Fisher information of hard conditioning is assumed.

For fixed k, h=delta^(1/3), U<=A²+eta and sufficiently small delta give
`B=O_k(eta+delta^(1/3))` whenever eta tends to0. Hence each cell whose
mass is bounded below has W2=O_k(sqrt(eta+delta^(1/3))). K1876's
optimizer trial has eta=O_k(delta), so this proves a delta^(1/6) upper
rate. It is not asserted sharp. A large tau can make (1) conservative but
does not invalidate it.

## 5. Executed consumers and boundaries

**Means and widths.** Put q_j=sqrt(B/p_j). For Y_j the actual rescaled
conditional variable, coupling and the L2 triangle inequality imply
```
|E Y_j|<=q_j,
|sqrt(E Y_j²)-1/sqrt(b_j)|<=q_j.
```
The same q_j bounds the difference of standard deviations: centering is
an orthogonal projection in the coupling L2 space. Any 1-Lipschitz observable
has expectation error at most q_j, including unbounded ones with the stated
finite moments. Physical means multiply the error by sqrt(delta).

**An explicit tail modulus.** For a coupling with cost q_j², splitting at
|G|=L/2 gives
`E[Y_j² 1_(|Y_j|>L)]<=4q_j²+2E[G²1_(|G|>L/2)]`.
Gaussian fourth moment3/b_j² and Markov then give the weighted bound
```
sum p_j E[Y_j² 1_(|Y_j|>L)] <=4B+24/[(kA)² L²].        (4)
```
Thus the actual rescaled second moments are uniformly integrable along
B->0. This quantifies the qualitative K1878 tail step.

**Products and comparison.** For independent conditional samples the product
squared W2 bounds add. Independence is a premise, not an inferred physical
property. Two same-cell distributions with respective bounds q and q_star
are within q+q_star by the common Gaussian. For two even k4 example densities
(including the optimizer) this gives central<0.026 and outer<0.064.
This compares shapes at the same delta; it is not a spectral deficit modulus
that vanishes as I-I_star tends to0 with delta fixed.

**Scope.** No source register or physics-ledger row changes. No new GU,
sharpness, sextic multiplier/gap, global multiwell log-Sobolev constant,
physical observable or novelty claim. The useful endpoint is finite transport
accuracy for all feasible densities, with explicit tail and rare-cell costs.

## 6. Reproduction and hostile review

Run the K1882 producer and separate probe in tests/channel-swings. Exact
budget arithmetic, Gaussian equality controls, moment allocation, residual
coupling and planted inequality faults supplement the analytic proof above.
Finite controls are not a proof for all densities. Hostile checks target
hard-conditioning boundaries, false TV-to-W2 transfer, cap inequality direction,
missing cutoff energy, rare cells, actual U, transport normalization and mass
balance. No independent agent, external expert or proof assistant is claimed.
