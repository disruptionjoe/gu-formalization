---
title: "K1533--K1537 Wick-dominant non-Gaussian variational boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1533--K1537 Wick-dominant non-Gaussian variational boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests the positive
Hamiltonian prerequisite bordering SC-META-53. The cutoff field, nonlinear
Hamiltonian, non-Gaussian likelihoods and BRST complex are repository controls,
not released GU data.

```gu-typed-objects
result: sharp all-density Fisher/covariance extremality, exact non-Gaussian Wick moment defect, ultraviolet-shell Fisher coercivity, scoped non-Gaussian N^4 variational boundary and endpoint-capacity wake
carrier: beta=1 Gaussian reduced Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing ON=repository_owned_control
real_structure: real Fourier covariance basis with arbitrary absolutely continuous likelihood and optional complex phase
grading: spatial frequency, ultraviolet shell, mean, covariance, relative Fisher information, local central moments, Wick-square energy and cutoff filtration
action_owner: repository-construction -- no released source measure, counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1528--K1532 prove that every finite-cutoff Gaussian wavefunction costs
`Theta_g(N^4)`. The exact wake is genuinely non-Gaussian. Two facts prevent a
careless extension. First, Gaussian amplitudes are only one likelihood family;
their exact free-form expression must be replaced by a lower bound valid for
all densities. Second, the Gaussian fourth-moment identity is false outside
that family: a symmetric two-well law can make the Wick square arbitrarily
small at variance `3C`.

The structural split is therefore Fisher cost versus moment defect. Gaussian
integration by parts proves that K1528's matrix expression is the sharp minimum
of relative Fisher information at fixed mean and covariance. The one-point
Wick expectation differs from K1529's polynomial by one exact skewness/fourth-
cumulant remainder. When the integrated remainder cannot cancel more than a
fixed fraction of Gaussian coercivity, K1530's shell proof survives unchanged.
The counterexample is retained as the boundary of the theorem, not discarded.

## K1533 — Gaussian extremality at fixed moments

Let `mu=N(0,I_d)` be the real cutoff Gaussian measure and let
`nu=rho mu` have mean `m`, positive covariance `S` and weak score

```text
u=grad log rho.
```

For finite weighted relative Fisher information,

```text
I_Omega(nu|mu)=E_nu[u^T Omega u].
```

Gaussian integration by parts gives the exact score identities

```text
E_nu u=m,
E_nu[(X-m)(u-m)^T]=S-I.
```

Regress `u-m` on `X-m`. Positivity of the residual covariance gives

```text
Cov_nu(u)>=(S-I)S^(-1)(S-I).
```

Tracing against positive `Omega` yields

```text
I_Omega(nu|mu)
 >=m^T Omega m+Tr[Omega(S+S^(-1)-2I)].
```

Equality forces

```text
u-m=(I-S^(-1))(X-m),
```

whose normalized solution is exactly `N(m,S)`. Thus the K1528 expression is
not merely a Gaussian computation: it is the sharp all-density lower bound at
fixed first and second moments.

For a normalized complex wavefunction `psi=sqrt(rho) exp(i theta)`,

```text
q0[psi]
 =(1/4)I_Omega(nu|mu)
  +int |grad theta|_Omega^2 dnu.
```

No phase can lower the positive-amplitude cost. Smooth positive densities prove
the identities directly; Gaussian convolution and lower semicontinuity give
the finite-Fisher closure.

## K1534 — the exact non-Gaussian moment defect

At each point write

```text
phi_N(x)=h(x)+Z_x,
E Z_x=0,
E Z_x^2=v(x),
E Z_x^3=mu3(x),
E Z_x^4=mu4(x).
```

Direct expansion gives

```text
E[(phi_N^2-3C_N)^2]
 =F_C(h,v)+R_N(x),

R_N(x)=4h(x)mu3(x)+mu4(x)-3v(x)^2.
```

The first term is exactly K1529's Gaussian polynomial and obeys

```text
F_C(h,v)>=c_* C_N v,
c_*=6(sqrt(3)-1).
```

For fixed `0<=beta<c_*`, define `M_beta` by the integrated defect budget

```text
int R_N(x)dx >= -beta C_N V_N,
V_N=int v(x)dx=Tr(Lambda S).
```

Every law in this class has

```text
E W_N >=(c_*-beta)C_N V_N.
```

This class is genuinely non-Gaussian. `M_0` contains arbitrary linear mixes of
independent centered symmetric standardized coordinates with nonnegative fourth
cumulants. Every projection then has

```text
kappa4(sum a_j Z_j)=sum a_j^4 kappa4(Z_j)>=0.
```

It includes Laplace-type laws, finite-fourth-moment Student-type examples and
elliptical Gaussian scale mixtures. Arbitrary phases remain allowed because
K1533 prices them separately.

The defect condition is load-bearing. Let

```text
Y=aR+epsilon Z,
```

where `R` is uniform on `{minus one,plus one}` and `Z` is standard Gaussian.
Then

```text
Var(Y)=a^2+epsilon^2,
kappa4(Y)=-2a^4.
```

Choosing `Var(Y)=3C` gives

```text
E[(Y^2-3C)^2]
 =4a^2 epsilon^2+2epsilon^4 ->0.
```

No theorem depending only on mean and variance can extend K1529 to every
non-Gaussian law.

There is also an exact cutoff realization. Take the equal mixture of Gaussian
densities with means

```text
m_plus/minus=plus/minus a/sqrt(lambda_0)e_0
```

and common covariance `epsilon I`, with

```text
a^2=3(1-epsilon)C_N.
```

Its pointwise law is the smooth mixture

```text
(1/2)N(a,epsilon C_N)+(1/2)N(-a,epsilon C_N),
```

and exactly

```text
E W_N=6epsilon(2-epsilon)C_N^2.
```

The negative fourth cumulant cancels the Gaussian coercivity. But the common
squeeze in every nonzero mode gives, by K1533,

```text
q0 >=(1/4)sum_(j not zero)
      omega_j(epsilon+epsilon^(-1)-2)
    =Theta(N^4/epsilon)
```

as `epsilon` tends to zero. Making the interaction `O(N^2)` by
`epsilon=Theta(N^-2)` costs `Theta(N^6)`. This exact cat/squeeze family does
not supply the missing trial.

## K1535 — low Wick expectation forces shell Fisher cost

Use K1530's shell constants

```text
Tr(P_N Lambda)>=kappa C_N,
P_N Lambda^2 Omega^(-1)P_N<=a_N P_N Lambda,
a_N<=L N^(-2).
```

For `nu` in `M_beta`, if

```text
E_nu W_N <=(c_*-beta)eta C_N^2,
0<eta<kappa,
```

then K1534 implies `V_N<=eta C_N`. Hence

```text
delta_N=Tr[P_N Lambda(I-S)]
       >=(kappa-eta)C_N.
```

K1530's noncommutative Frobenius factorization gives

```text
delta_N^2
 <=Tr[Omega(S+S^(-1)-2I)]
   Tr[P_N Lambda^2 Omega^(-1)P_N S].
```

The second factor is at most `a_N eta C_N`. K1533 therefore yields

```text
I_Omega(nu|mu)
 >=((kappa-eta)^2/(a_N eta))C_N.
```

At `eta=kappa/2`,

```text
q0[psi]>=kappa C_N/(8a_N)=Omega(N^4).
```

No stationarity, mode independence, covariance diagonality or Gaussian density
is used in this step. Only the explicit integrated moment-defect budget remains.

## K1536 — scoped scale and the endpoint-capacity wake

Split at `V_N=(kappa/2)C_N`. The low-variance branch pays K1535's free cost;
the high-variance branch pays K1534's interaction cost. Therefore

```text
q0[psi]+gE W_N
 >=min{
      kappa C_N/(8a_N),
      g(c_*-beta)kappa C_N^2/2
    }
 =Omega_g(N^4)
```

for every fixed `0<=beta<c_*` and every density in `M_beta`. The vacuum lies in
`M_0` and gives `6gC_N^2`, so this materially non-Gaussian variational bottom is

```text
Theta_g(N^4).
```

The unrestricted escape is now sharply typed. If a normalized trial has
Rayleigh quotient at most `K N^2`, Markov puts at least half its probability on

```text
B_N={W_N<=2KN^2/g}.
```

Binary entropy contraction and cutoff-uniform Gross log-Sobolev then require

```text
-log mu(B_N)=O(N^2).
```

K1518 gives the opposite-order lower bound `-log mu(B_N)>=cN^2`; it does not
give a matching upper bound. Thus an order-`N^2` trial requires a sharp
quadratic endpoint small-ball exponent.

For a concrete sufficient route choose `chi` supported in `[0,2]`, equal to one
on `[0,1]`, and set

```text
psi_(N,L)=chi(W_N/L)/||chi(W_N/L)||.
```

Then

```text
E_psi W_N<=2L,

q0[psi]
 =L^(-2)
  E[chi'(W_N/L)^2 Gamma_Omega(W_N)]
  /E[chi(W_N/L)^2],

Gamma_Omega(W_N)
 =8||Pi_N[(phi_N^2-3C_N)phi_N]||_2^2.
```

Here `Pi_N` is the full cutoff projector, distinct from the fixed-ratio
ultraviolet-shell projector `P_N` used in K1530 and K1535.

At `L=Theta(N^2)`, an `O(N^2)` bound on this weighted boundary-capacity quotient
constructs the desired trial. Current bandlimit estimates leave an `O(N^3)`
prefactor times an uncontrolled transition-mass ratio, so the construction is
not yet certified. Any superquadratic endpoint small-ball exponent would rule
it out instead.

Harmonic BRST tensoring transfers only the scoped Rayleigh statement. It does
not construct a continuum charge, physical cohomology or GU Hilbert space.

## K1537 — admission replay

The bridge census is now 248 rows: 169 satisfied, ten conditional, 65 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would call the `M_beta` theorem an all-state result.
The smooth two-well law explicitly disproves the required variance-only
coercivity. Negative fourth cumulant and skewness are real escape directions,
not technical leftovers.

The strongest contrary construction is the endpoint bump above. Its potential
cost is already `O(N^2)`; the missing fact is exactly its weighted boundary
capacity. A crude bandlimit estimate does not certify that quotient, and the
explicit cat/squeeze family becomes more expensive when its potential narrows.

The most delicate proof seam is the Fisher regression identity. It uses the
relative score with respect to the standard Gaussian measure, not the ordinary
Lebesgue score. The cross covariance is `S-I`, which produces exactly
`S+S^(-1)-2I` and recovers K1528 without a factor error.

The source boundary is unchanged. These are repository-owned controls bordering
SC-META-53, not an action-owned GU quantization.

## Exact next input

Determine the endpoint capacity of `{W_N<=Theta(N^2)}`. Either prove a matching
`Theta(N^2)` small-ball exponent and an `O(N^2)` weighted transition quotient
for an explicit smooth bump, or prove a superquadratic exponent/capacity lower
bound that excludes the route. In parallel, K1413 still requires a genuinely
gauge/Maxwell-dependent spacetime, secondary-null or derivative/nonlocal
estimate, and source admission still requires one action-owned primitive
circle, kinetic normalization, physical carrier and faithful observed
intertwiner.
