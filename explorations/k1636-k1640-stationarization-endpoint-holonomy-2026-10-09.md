---
title: "Finite-cutoff stationarization and the endpoint holonomy boundary"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__STATIONARY_FISHER_DEFECT_AND_ENDPOINT_HOLONOMY_BOUNDARY
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Finite-cutoff stationarization and the endpoint holonomy boundary

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff quartic Hamiltonian and a conditional harmonic spectral model.
> It is not a source-native GU action, physical state space, observed carrier,
> prediction, confirmation, or falsification of a registered source claim.
> Conventional comparator conclusions bind only the models stated here.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: finite_cutoff_torus_field_laws_plus_compact_bv_spectral_primitives
  pairing_or_form: weighted_relative_fisher_wick_form_plus_fourier_pairing
  real_structure: real_cutoff_q_space_and_real_compact_spectral_values
  grading: ultraviolet_cutoff_growth_plus_endpoint_frequency_weight
  action_owner: repository_control_not_source_owned
  target_object: stationary_fisher_defect_gap_and_atomfree_holonomy_endpoint
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1632 closes its particular Gaussian shell channel but leaves genuinely
non-Gaussian and nonstationary laws open.  The first arc below removes
nonstationarity and phase as independent finite-cutoff escape mechanisms, then
uses K1533 and K1534 to state the exact price a successful stationary
finite-full-energy law must pay.  It does not construct such a law.

K1633 proves Fourier `L1` from `H^s`, `s>1/2`, while correctly leaving the
endpoint open.  The second arc constructs an explicit compact absolutely
continuous BV primitive in `H^(1/2)` whose derivative is atom-free and
absolutely continuous but whose Fourier transform is not in `L1`.  A dyadic
`l1` square-function condition gives a sufficient endpoint replacement.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain.  The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
K1145/K1150 remain 0/7.  No source, ledger, canon, paper, prediction,
confirmation, or public-posture state moves.

## K1636 — exact translation-Haar Fisher reduction

Fix a finite Fourier cutoff on a normalized spatial torus.  Let `Q_N` be the
real cutoff configuration space, `mu_N=N(0,I)` its reference Gaussian,
`Omega_N>0` the free multiplier, and `U_a` the orthogonal representation of
translation by `a`.  Both `mu_N` and `Omega_N` are translation invariant.
For a normalized finite-Fisher wavefunction of finite full energy

```text
psi=sqrt(rho) exp(i theta),
q_0[psi]=(1/4) I_Omega(rho|mu_N)
          +int |grad theta|_Omega^2 rho dmu_N.       (1)
```

Removing the phase cannot increase the energy.  For
`rho_a(q)=rho(U_a^(-1)q)` define the normalized Haar average

```text
bar rho(q)=int_T^3 rho_a(q) da.                     (2)
```

The perspective map `(p,v) -> v^T Omega_N v/p` is convex.  Applying Jensen to
`p=rho_a` and `v=grad rho_a`, using commutation of `U_a` and `Omega_N`, gives

```text
I_Omega(bar rho|mu_N)
 <= int_T^3 I_Omega(rho_a|mu_N) da
 = I_Omega(rho|mu_N).                               (3)
```

The finite-cutoff Wick-square potential `W_N(q)` is translation invariant, so

```text
int W_N bar rho dmu_N=int W_N rho dmu_N.            (4)
```

Consequently every finite-full-energy finite-Fisher state has a stationary
positive-amplitude density with no larger full energy.  The unrestricted
finite-cutoff infimum therefore equals the infimum over stationary
positive-amplitude densities.  This is an exact finite-cutoff reduction, not
a continuum existence theorem.

## K1637 — exact stationary Fisher/Wick defect gap

Let `bar rho mu_N` be a stationary finite-Fisher law of finite full energy,
in particular with finite fourth moment/Wick expectation, mean `m` and
positive covariance `S`, and let `gamma=N(m,S)`.  Stationarity forces `m` to
lie in the translation-fixed constant sector and `S` to commute with
translations, so `gamma` is a stationary Gaussian competitor.  With
`u=grad log(bar rho)` and `u_gamma` the matching Gaussian score, K1533's score
regression is the exact weighted Pythagoras identity

```text
R_(Omega,N)=E_bar rho[(u-u_gamma)^T Omega_N(u-u_gamma)] >=0,
I_Omega(bar rho)=I_Omega(gamma)+R_(Omega,N).         (5)
```

At each spatial point write `phi_N=h+Z`, with variance `v` and central moments
`mu_3,mu_4`.  K1534 gives the exact integrated non-Gaussian Wick defect

```text
D_N=int_T^3 [4h mu_3+mu_4-3v^2] dx.                (6)
```

If `lambda_N^statG` is the infimum over stationary Gaussians and
`A_N=Q_N(gamma)-lambda_N^statG>=0`, the complete full-energy identity is

```text
Q_N[sqrt(bar rho)]-lambda_N^statG
 = A_N+(1/4)R_(Omega,N)+g D_N.                      (7)
```

The coefficient `1/4` belongs only to the Fisher convention in (1); the Wick
defect has coefficient `g`.  Equation (7) is not a coercivity estimate and
does not assume `D_N` has either sign.

## K1638 — the necessary leading defect scale

Fix the repository's coupling `g>0`, independent of `N`.  If a sequence of
normalized finite-Fisher states satisfies, along a cutoff subsequence,

```text
Q_N[psi_N] <= lambda_N^statG-epsilon N^4             (8)
```

for fixed `epsilon>0`, first apply K1636 and then (7).  Rearrangement yields

```text
-gD_N >= epsilon N^4+A_N+(1/4)R_(Omega,N).          (9)
```

Thus, for fixed `g>0`, every leading-order descent requires
`D_N=-Omega(N^4)`, large enough to pay both the stationary-Gaussian
displacement and the non-Gaussian score residual.  Nonstationarity and phase
cannot hide that requirement.  Negative defect by itself is not sufficient:
constructing a normalized stationary law that realizes the required defect
while controlling both positive terms is the remaining variational problem.

## K1639 — a compact `H^(1/2)` atom-free endpoint counterexample

Set `epsilon_n=e^(-n)`, `w_n=1/[n(n+1)]`, and

```text
tau_epsilon(x)=epsilon^(-1)(1-|x|/epsilon)_+,
f=sum_(n>=1) w_n tau_(epsilon_n),
mu=f dx.                                             (10)
```

Because `sum w_n=1`, `mu` is a compactly supported atom-free absolutely
continuous probability measure.  Its Fourier transform is nonnegative:

```text
widehat mu(t)=sum_(n>=1) w_n sinc^2(epsilon_n t/2). (11)
```

Let `F(x)=mu((-infinity,x])` and
`G(x)=F(x)-F(x-1)=mu((x-1,x])`.  Then `G` is nonnegative, compactly supported,
absolutely continuous and BV, and

```text
DG=[f(x)-f(x-1)]dx,
it widehat G(t)=(1-e^(-it))widehat mu(t).            (12)
```

On `I_n=[e^n,e^(n+1)]`, the tail `k>=n+2` in (11) and the elementary sinc
upper bound give constants `0<c<C` such that

```text
c/(n+2) <= widehat mu(t) <= C/(n+1),  t in I_n.     (13)
```

Since `|1-e^(-it)|` has a uniform positive logarithmic mean on these long
annuli, (12)--(13) imply

```text
sum_n int_(I_n) t|widehat G(t)|^2 dt < infinity,
sum_n int_(I_n) |widehat G(t)| dt = infinity.       (14)
```

The bounded low-frequency part is harmless.  Hence `G in H^(1/2)(R)` but
`widehat G notin L1(R)`.  Moreover `f notin L2`, so this does not contradict
K1628.  The strict inequality in K1633 cannot be replaced by `s>=1/2`, even
for compact AC/BV primitives with atom-free AC derivatives.

There is a useful sufficient endpoint replacement.  For dyadic annuli
`A_j={2^j<=|t|<2^(j+1)}`, low-frequency `L2` control plus

```text
sum_(j>=0) [int_(A_j)|t||widehat G(t)|^2 dt]^(1/2)
 < infinity                                             (15)
```

implies `widehat G in L1` by shellwise Cauchy--Schwarz, since
`int_(A_j)dt/|t|` is constant.  This is a `B^(1/2)_(2,1)`-type sufficient
condition, not a claimed necessary characterization.

## K1640 — protected integration and hostile bookend

The bridge census is now 355 rows: 276 satisfied, ten conditional, 65
excluded, and four missing.  K1636 closes nonstationarity and phase as
independent escapes for normalized finite-full-energy finite-Fisher cutoff
states.  On the finite fourth-moment/Wick domain and at fixed `g>0`,
K1637--K1638 replace that open direction with the exact necessary target
`D_N=-Omega(N^4)` plus its positive Fisher and Gaussian-displacement prices.
K1639 proves endpoint failure in a strong compact atom-free AC/BV class and
records an annular `l1` sufficient replacement.

Hostile review rejects treating the necessary defect scale as sufficient,
claiming an unrestricted coefficient value, passing to an infinite-cutoff
minimizer, identifying (15) as necessary, or transferring the spectral result
to electric-field `L1`, nonlinear remainders, or a source-owned flow.

The next quantum wake is an explicit normalized stationary non-Gaussian family
with `D_N=-Omega(N^4)` and controlled `A_N+R_(Omega,N)/4`, or a coercivity
theorem excluding it.  The next PDE wake remains source-owned derivation of
the needed primitive and remainder regularity.  The source-owned
action/measure/Hamiltonian tuple remains separate.

## Postflight bookend

The variational frontier is now narrower: any leading descent is stationary
after exact reduction and must be carried by a leading negative Wick moment
defect that dominates two explicit positive costs.  The harmonic frontier is
also exact at the Sobolev endpoint: `H^(1/2)` plus compactness, BV, and an
atom-free AC derivative still does not force Fourier `L1`; annular `l1`
summability does.  Protected source, ledger, canon, paper, prediction,
confirmation, and public-posture states are unchanged.
