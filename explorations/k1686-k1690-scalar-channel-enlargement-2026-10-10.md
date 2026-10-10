---
title: "K1686--K1690 scalar-channel enlargement"
status: active_research
document_role: exploration
claim_verdict: proved_for_weak_scalar_channels_and_fixed_cardinal_product_blocks
target_claim: INTERNAL_TARGET__K1684_FIXED_RADEMACHER_SCALAR_ENVELOPE
updated_at: "2026-10-10"
---

# K1686--K1690: enlarging the scalar channel inside the cardinal trial

## Result and boundary

K1684's Rademacher channel is not locally optimal among bounded symmetric
unit-variance scalar seeds at fixed small negative fourth defect. A unique
three-point seed that cancels its sixth cumulant has smaller relative Fisher
information at the same defect coordinate through the first distinguishing
order. On every fixed exchangeable cardinal block, allowing a different
independent scalar channel on each cardinal coordinate gives no further
advantage beyond choosing the best one scalar channel and repeating it.

This widens the explicit trial class. It does not prove that the three-point
seed is globally optimal at finite channel strength, lower the globally
optimized K1684 envelope strictly, control correlated cumulant tensors or
moving packet shapes, account exactly for Fisher reduction under continuous
translation-Haar averaging, or identify the unrestricted coefficient.

Scope: the result binds bounded symmetric scalar Ornstein--Uhlenbeck channels
inserted independently in K1683's fixed rectangular real-cardinal block, before
the one-way translation-Haar Fisher convexity step. It is repository-derived
conditional mathematics, not a source-owned GU Hamiltonian or physical state.

## K1686: an exact scalar Fisher/MMSE identity

Let `X` be centered with unit variance, let `Z` be standard Gaussian and put

```text
Y_t=sqrt(t)X+sqrt(1-t)Z,             0<t<1.
```

Writing `m_t(y)=E[X|Y_t=y]`, differentiation of the Gaussian mixture gives
the exact relative score

```text
u_t(y)=d/dy log(p_t(y)/phi(y))
      =sqrt(t)/(1-t) [m_t(y)-sqrt(t)y].
```

If `mmse_X(gamma)` is the posterior mean-square error in
`sqrt(gamma)X+Z`, then with `gamma=t/(1-t)`,

```text
j_X(t)=E[u_t(Y_t)^2]
      =t/(1-t)^2 [1-t-mmse_X(gamma)]
      =gamma [1-(1+gamma)mmse_X(gamma)].
```

Indeed `E[m_t(Y_t)^2]=1-mmse`,
`E[Y_tm_t(Y_t)]=E[Y_tX]=sqrt(t)`, and `E[Y_t^2]=1`. The formula is exact;
nonnegativity is the Gaussian-channel inequality
`mmse_X(gamma)<=1/(1+gamma)`. Independently,

```text
kappa_4(Y_t)=t^2kappa_4(X).
```

## K1687: the first distinguishing symmetric coefficient

Assume now that `X` is bounded and symmetric. Put

```text
kappa_4=E[X^4]-3,
kappa_6=E[X^6]-15E[X^4]+30.
```

Mehler's expansion and `H_n'=nH_(n-1)` give

```text
p_t/phi
 =1+(kappa_4/24)t^2H_4+(kappa_6/720)t^3H_6+O_X(t^4),
```

in the Gaussian weighted spaces needed for the score. Expanding
`int phi (r_t')^2/r_t`, Hermite orthogonality kills the order-five term. The
only order-six contributions are the squared `H_5` score and the denominator
correction `H_4H_3^2`. Since

```text
int H_5^2 phi=120,
int H_4H_3^2 phi=216,
```

one obtains

```text
j_X(t)
 = (kappa_4^2/6)t^4
   + (kappa_6^2/120-kappa_4^3/4)t^6
   + O_X(t^7).
```

Thus K1681's `O_X(t^5)` remainder can be sharpened: the fifth-order
coefficient vanishes for every seed in its symmetric class.

For `kappa_4=-u<0`, compare channels at the same negative-defect coordinate

```text
q=u t^2=-kappa_4(Y_t).
```

Then

```text
j_X(q)
 = q^2/6
   + [1/4+kappa_6^2/(120u^3)]q^3
   + O_X(q^(7/2)).
```

The leading `q^2/6` term is universal; the squared sixth cumulant is the first
seed-dependent penalty.

## K1688: a three-point seed beats Rademacher locally

Let

```text
p_*=(15+sqrt(105))/60,
P(X_*=0)=1-p_*,
P(X_*=+p_*^(-1/2))=P(X_*=-p_*^(-1/2))=p_*/2.
```

This centered bounded symmetric seed has unit variance and

```text
1/p_*=(15-sqrt(105))/2,
kappa_4(X_*)=(9-sqrt(105))/2=-u_*<0,
kappa_6(X_*)=1/p_*^2-15/p_*+30=0.
```

Consequently its matched-defect expansion is

```text
j_*(q)=q^2/6+(1/4)q^3+O(q^(7/2)).
```

For symmetric Rademacher, `u_R=2` and `kappa_6=16`, so

```text
j_R(q)=q^2/6+(31/60)q^3+O(q^(7/2)).
```

Therefore

```text
j_R(q)-j_*(q)=(4/15)q^3+O(q^(7/2))>0
```

for every sufficiently small positive `q`. The two channels have the same
covariance and the same fourth cumulant `-q`; the three-point seed pays strictly
less Fisher information locally. This refutes finite-channel scalar optimality
of Rademacher near the Gaussian endpoint while preserving K1682's distinct
statement that Rademacher uniquely reaches the most negative seed cumulant at
fixed interpolation strength.

The deterministic quadrature control evaluates the exact score and the K1686
MMSE formula for both seeds. At `q=10^-3,3*10^-3,10^-2`, it reproduces the
identity and finds the predicted strict ordering. Those values are controls;
the sign theorem comes from the asymptotic coefficient and remainder.

## K1689: coordinate heterogeneity collapses to one scalar choice

Fix one K1683 rectangular block with `d_N` real cardinal translates
`psi_(j,N)`. Because the K1572 Fourier multiplier commutes with translation,
all packet fourth masses and all diagonal whitened score weights are equal:

```text
int |psi_(j,N)|^4=L_N/d_N,
[U_N^*S_N^(-1/2)Omega_NS_N^(-1/2)U_N]_(jj)=T_N/d_N.
```

Put an independent centered unit-variance scalar channel `(X_j,t_j)` on each
cardinal coordinate and standard Gaussians outside the block. Score
independence kills off-diagonal score covariances and cumulant tensorization
gives the exact pre-Haar gap

```text
Q_N-lambda_N^statG
 = (T_N/(4d_N)) sum_j j_(X_j)(t_j)
   + (gL_N/d_N) sum_j kappa_4(X_j)t_j^2.
```

This is the arithmetic mean of one scalar objective. Hence arbitrary
coordinate-to-coordinate heterogeneity cannot beat its infimum; repeating one
near-minimizing scalar channel on every coordinate attains the same infimum.
The heterogeneous class therefore collapses exactly to the enlarged scalar
envelope

```text
h_g^scalar-card-up
 = h_g^prof + inf_(C,X,t)
   [(tau_g(C)/4)j_X(t)+g ell_g(C)kappa_4(X)t^2],
```

over fixed K1683 blocks and bounded centered symmetric unit-variance seeds.
Rademacher is admissible, so

```text
h_g^scalar-card-up <= h_g^card-up < h_g^prof.
```

The local K1688 comparison is pointwise at fixed `C,q`; it does not by itself
prove strict inequality between the two fully optimized envelopes. Continuous
translation-Haar averaging can only lower Fisher and remains a separate
one-way step.

## K1690: protected integration and next frontier

The bridge census becomes 405 rows: 326 satisfied, ten conditional, 65
excluded and four missing. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53
remains `UNCERTAIN`; the standing ledger remains 33 SAME / 22 DIFFERS / 31
NEEDS / 2 OVER-DETERMINED; and K1145/K1150 remain 0/7. No source, ledger,
canon, paper, prediction, confirmation or public verdict moves.

The strongest coefficient questions are now: determine the exact finite-`t`
scalar infimum in `h_g^scalar-card-up`; test one genuinely non-product
fourth-cumulant tensor or moving packet shape; quantify the additional Fisher
reduction under translation-Haar averaging; or prove an unrestricted lower
bound against the widened envelope. Compactness, Mosco convergence and an
`E_N+O(1)` recentering still wait for the true coefficient and shift. The
source-owned action/domain/state/observation tuple remains separate.
