---
title: "K1999: Effective pulse-rank and approximation barriers"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1999_effective_rank_residual_bound.py
  - tests/channel-swings/k1999_effective_rank_residual_bound_probe.py
---

# K1999: Effective pulse-rank and approximation barriers

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
result: explicit rank-only marginal-residual and unrestricted low-rank approximation lower bounds
carrier: actual K1991 central rectangle with normalized Lebesgue measures LAYER=toy CHIRALITY=N/A
pairing: real L2 norm and row/column averages ON=central_rectangle
real_structure: real bounded measurable exact pulses; arbitrary real L2 low-rank approximants
grading: separation rank in the two characteristic coordinates, not source chirality
action_owner: repository-construction -- fixed optimal scalar phase and amplitude cap
target: effective representation complexity MAP-TYPE=intertwiner
```

## Result and scope

[K1997](k1997-finite-rank-pulse-obstruction-2026-10-23.md) proved a positive
but unquantified marginal-residual floor at every fixed rank. Here that floor
becomes explicit. Let q be any real kernel on the ACTUAL central rectangle,
with |q|<=1 and separation rank at most r. Use K1997's normalized measures
mu=dx/2, nu=dz/W, actual ramp marginal g, and combined squared residual

    J(q)=||int q dnu+x||²_L2(mu)+||int q dmu-g||²_L2(nu).

For every integer r>=0, set N=r+2. Then

    J(q) > L_r,
    L_r=1/[9437184 N^4 (768 N²)^(3(N-1))].             (1)

This is a universal explicit NONSHARP bound, independent of a chosen basis
or conditioning constant. It applies to approximate rows AND columns.
It does not claim an efficient optimizer, the optimal rank/error rate, or
an explicit wing/central minimum-norm pulse.

A released consequence is stronger in a different direction. If q_* is ANY
exact capped central pulse and w is ANY rank-at-most-r real L2 kernel,
even if w violates the cap or marginals, then

    ||q_*-w||² >= (169/256) alpha0 k a_N²,             (2)
    alpha0=1/3, k=1/(16N),
    a_N=(1/4)(768 N²)^(-(N-1)).

Thus every exact pulse has a quantitative obstruction to arbitrary low-rank
strong approximation. This is not only a bound for capped approximants.
Both the actual pulse and the errors use normalized central measures; they
are not global pulse-energy or phase-Dirichlet-energy errors.

## 1. Corner bands retain the actual continuum data

Use K1997's h=(1+q)/2. Set s=(1-x)/2. The row measure is ds on[0,1],
and the desired row mean is s. On the terminal positive ramp put
v=(1-g)/2 in[0,1/2]. Its column measure is alpha dv, where

    alpha=4t/(3+4t)>1/3=alpha0

because the ACTUAL algebraic root t is in(9/20,23/50). The desired h-column
mean is1-v. No endpoint value is imposed, and the other columns retain their
usual measure. Set rho=alpha0 k²=1/(768N²) and

    a_i=(1/4)rho^(i-1), b_i=k a_i, 1<=i<=N.

Take row bands I_i=[a_i,2a_i] and ramp-column bands T_i=[b_i,2b_i].
All are positive-measure, disjoint within their axis, and lie in the actual
rectangle/ramp. Let A_ij be the mean of h over I_i x T_j.

Write e_row and e_col for the L2 errors in the h marginals. Then
sqrt(e_row²+e_col²)=sqrt(J(q))/2. Nonnegativity and Cauchy-Schwarz give

    A_ij <= [3a_i/2+e_row/sqrt(a_i)]/(alpha b_j),      (3)
    1-A_ij <= [3b_j/2+e_col/sqrt(alpha b_j)]/a_i.      (4)

For(3), integrate h over the band and ALL columns, obtaining at most
3a_i²/2+sqrt(a_i)e_row, then divide by a_i alpha b_j.
For(4), integrate1-h over the column band and ALL rows, obtaining at most
3alpha b_j²/2+sqrt(alpha b_j)e_col. Both inequalities need0<=h<=1;
using only the marginal equations without the cap would be invalid.

## 2. An approximately triangular compression forces rank

Let U_ij=1 for j>=i and0 otherwise. When j>=i use(4); its structural
term is at most3k/2=3/(32N). When j<i use(3); the largest structural
term is at adjacent bands, where

    a_i/(alpha b_(i-1)) <=rho/(alpha0 k)=k.

Suppose J(q)<=L_r. Equivalently,

    sqrt(J(q))/2 <= alpha0 k a_N^(3/2)/(16N).

The error term in(3) is at most1/(16N), since
alpha b_j sqrt(a_i)>=alpha0 k a_N^(3/2).
The error term in(4) has the same bound: its denominator is at least
sqrt(alpha0 k)a_N^(3/2), which is larger than
alpha0 k a_N^(3/2). Therefore

    |A_ij-U_ij|<=5/(32N).                              (5)

U^-1 has diagonal1, superdiagonal-1 and zeros elsewhere, hence its row
and column norms are at most2. The row norm of A-U is at most5/32,
so ||U^-1(A-U)||_infinity<=5/16<1. A is invertible by the geometric-series
inverse. Equivalently its smallest singular value is at least
1/2-5/32=11/32, since both matrix row and column error norms are<=5/32.

But averaging a separated kernel cannot increase its rank, and
rank(h)<=rank(q)+1<=r+1=N-1. Its N-by-N compression A must be singular.
This contradiction proves the STRICT bound(1), including rank0.
No finite sampling of a continuum sign was used: every entry is an integral
over a positive-measure band, controlled by the entire marginal residual.

## 3. Released consumer: all low-rank approximants, without a cap

For exact q_*, both errors vanish, so the stronger bound
|A-U|<=3/(32N) gives sigma_min(A)>=13/32. Normalize the row and column
indicator functions to have L2 norm1. The resulting operator compression is

    C=diag(sqrt(a_i)) A diag(sqrt(alpha b_j)).

Consequently sigma_min(C)>=(13/32)a_N sqrt(alpha0 k).
For any rank-r approximant w, put h_w=(1+w)/2. Its corresponding compression
C_w has rank<=r+1<N, so some unit vector z satisfies C_w z=0. Thus

    ||C-C_w||_operator >= ||Cz|| >= sigma_min(C).

Compression by orthonormal indicators has operator norm at most the L2 norm
of its kernel (direct Cauchy-Schwarz). Since h_*-h_w=(q_*-w)/2,
(2) follows. This argument neither clips w nor assumes bounded factors.
It also supplies the usual singular-value lower certificate at index r+1
of the exact q_* operator, if expressed in singular-value language.

For a capped approximant one can also use J(q)<=2||q-q_*||², giving the
weaker L_r/2 bound. Equation(2) is the useful stronger strong-error consumer.
Multiplying the normalized squared error by2tWM² converts it to the
physical central v=Mq squared norm. No conclusion about the wings follows.

## 4. Complexity and exact controls

The logarithm of1/L_r is O(r log(r+2)). Thus driving the marginal residual
norm to epsilon requires rank at least order
log(1/epsilon)/log log(1/epsilon), as epsilon tends to zero.
This is a necessary, weak lower rate, not a matching asymptotic theorem.
K1997's even-rank midpoint construction remains the constructive upper
comparison: J(q_n)=(1+alpha)/(3n²), and its strong error to the elementary
central pulse is alpha/n+(1-alpha)/(3n²). The large gap between bounds is open.

The certificate serializes exact band sizes and rational bounds at ranks
0,1,2,4,8,16,32. The following conservative marginal-error consumers use(1):

- Residual norm <=1e-10 requires rank >=1.
- Residual norm <=1e-50 requires rank >=6.
- Residual norm <=1e-100 requires rank >=12.
- Residual norm <=1e-250 requires rank >=27.

These large-precision examples illustrate the weakness as well as the
computability of the bound; they do not recommend numerical working precision.
The producer checks4935 exact rational geometry/Cauchy inequalities. The
separate probe checks1738 integral, finite-matrix and midpoint-approximation
identities, and rejects five corrupted mathematical bounds after a green
baseline. Universal statements rely on sections1–3, not those finite totals.

Strongest contrary control: the uncapped rank2 kernel -x+g has exact marginals,
but exceeds1 on a positive-measure corner and fails the hypothesis of(1).
This does not contradict(2): it has nonzero strong distance to every exact
CAPPED pulse. Strongest overclaim: presenting the logarithmic lower bound as
sharp or finite-rank impossibility as pulse nonexistence. K1991's feasible
central pulse and K1997's approximants remain explicit countercontrols.
The weakest practical seam is the large lower/upper rate gap and absence of
an exact global minimum-norm formula. These are same-author internal checks,
not specialist acceptance, formal proof-assistant certification or novelty
claims. Source, physics-ledger and canon verdicts remain unchanged.
