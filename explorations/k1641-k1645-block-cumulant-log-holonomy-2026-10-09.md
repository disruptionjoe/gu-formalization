---
title: "Fourier-block cumulant rigidity and the logarithmic holonomy endpoint"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__BLOCK_CUMULANT_AND_LOG_HOLONOMY_BOUNDARY
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Fourier-block cumulant rigidity and the logarithmic holonomy endpoint

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
  carrier: stationary_finite_cutoff_fourier_block_laws_plus_compact_ac_bv_spectral_primitives
  pairing_or_form: weighted_relative_fisher_wick_form_plus_log_weighted_fourier_pairing
  real_structure: real_trigonometric_cutoff_coordinates_and_real_compact_spectral_values
  grading: ultraviolet_block_size_plus_logarithmic_endpoint_frequency_weight
  action_owner: repository_control_not_source_owned
  target_object: submacroscopic_block_coefficient_rigidity_and_critical_log_holonomy_endpoint
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1636--K1638 reduce the finite-cutoff variational problem to stationary
positive densities and prove that every leading descent needs a negative Wick
defect of order `N^4`.  The first arc asks whether modewise or locally blocked
non-Gaussianity can supply that defect.  It retains finite Fisher information,
finite fourth moments, central symmetry, a uniformly bounded stationary
covariance profile and uniformly bounded standardized block fourth cumulants.
Those hypotheses are load-bearing; the result is not an unrestricted
coercivity theorem.

K1639 proves that ordinary `H^(1/2)` is insufficient for holonomy `L1`.  The
second arc resolves the first logarithmic refinement.  It constructs a compact
AC/BV atom-free primitive with finite critical log-weighted half-derivative
energy and divergent Fourier `L1`, while every `log^(1+epsilon)` strengthening
is sufficient.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain.  The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
K1145/K1150 remain 0/7.  No source, ledger, canon, paper, prediction,
confirmation, or public-posture state moves.

## K1641 — exact independent-block cumulant decomposition

Use a real uniformly bounded trigonometric basis on the normalized torus and
write the centered cutoff field as

```text
Z_N(x)=sum_(B in P_N) <a_B(x),X_B>.                 (1)
```

The coordinate blocks `X_B` are independent, centered and centrally
symmetric, with identity covariance after standardization.  The coefficient
of coordinate `j` is

```text
a_j(x)=sqrt(lambda_j)e_j(x),
lambda_j=s_j/(2 omega_j).                           (2)
```

Central symmetry makes every third central moment vanish.  Independence makes
joint cumulants additive, so at every point

```text
mu_4(x)-3v(x)^2
 =sum_B kappa_4(<a_B(x),X_B>).                      (3)
```

Consequently K1637's complete integrated defect is exactly

```text
D_N=sum_B int_T3 kappa_4(<a_B(x),X_B>)dx.           (4)
```

This is an identity, not a sign claim.  It includes independent non-Gaussian
modes as singleton blocks and representation-compatible finite Fourier blocks.
Stationarity remains an explicit class premise; arbitrary independent real
sine and cosine coordinates need not define a stationary law.

## K1642 — submacroscopic dependence cannot carry a leading defect

Assume the standardized block laws obey the uniform directional cumulant bound

```text
|kappa_4(<u,X_B>)| <= K ||u||_2^4                 (5)
```

and every block has at most `b_N` real coordinates.  If
`||e_j||_infinity<=C_e`, then (4), Cauchy within each block, and the partition
property give

```text
|D_N|
 <= K C_e^4 sum_B (sum_(j in B) lambda_j)^2
 <= K C_e^4 b_N sum_j lambda_j^2.                  (6)
```

For a uniformly profile-bounded covariance, `0<s_j<=S`,

```text
sum_j lambda_j^2
 <=(S^2/4)sum_(|k|_infinity<=N) omega_k^(-2)
 =O_(m,S)(N)                                       (7)
```

in three dimensions.  Thus

```text
|D_N|=O_(m,S,K,C_e)(b_N N).                        (8)
```

Since the cutoff has `Theta(N^3)` real modes, every uniformly bounded-kurtosis
profile-bounded block family with `b_N=o(N^3)` has `D_N=o(N^4)`.  A leading
defect inside this model therefore requires macroscopic `Omega(N^3)` block
dependence.  The alternatives are to leave a load-bearing hypothesis through
growing standardized cumulants, an unbounded covariance profile, broken
central symmetry, or a different non-block correlation structure.  Equation
(8) does not exclude those routes.

## K1643 — coefficient rigidity for submacroscopic block laws

Let `C_N^block` be the normalized stationary positive-amplitude finite-Fisher,
finite-fourth-moment laws satisfying K1641--K1642 with fixed `m,S,K,C_e` and
`b_N=o(N^3)`.  K1637 gives, for each member,

```text
Q_N-lambda_N^statG
 =A_N+(1/4)R_(Omega,N)+gD_N
 >=-o(N^4),                                        (9)
```

for every fixed `g>0`.  The K1572 profiled Gaussian belongs to the class and
supplies the matching upper bound.  Hence

```text
inf_(C_N^block) Q_N/N^4 -> h_g^prof.               (10)
```

This crosses the independent-mode boundary and proves a class coefficient for
all submacroscopic dependence blocks under the declared uniform hypotheses.
It does not identify the unrestricted coefficient: one macroscopic correlated
block is exactly the unresolved scale, and K1587 already shows subleading
higher-chaos descent outside any claim of bounded-error Gaussian recentering.

## K1644 — the critical logarithmic holonomy boundary

For `n>=2`, set

```text
A_n=1/[n log(n+1)],
w_n=(A_n-A_(n+1))/A_2,
epsilon_n=e^(-n),
f=sum_(n>=2) w_n tau_(epsilon_n),                  (11)
```

where `tau_epsilon` is K1639's triangular probability density.  The positive
weights telescope to one.  Thus `mu=f dx` is a compact atom-free AC
probability measure and

```text
widehat mu(t)=sum_(n>=2) w_n sinc^2(epsilon_n t/2)>=0.             (12)
```

On `I_n=[e^n,e^(n+1)]`, the unresolved tail `k>=n+2` supplies the lower bound,
while `sinc^2 y<=min(1,y^(-2))` controls the earlier scales.  Therefore

```text
widehat mu(t) asymp A_n asymp 1/[n log n],  t in I_n.              (13)
```

With `F(x)=mu((-infinity,x])` and `G(x)=F(x)-F(x-1)`, the primitive is
nonnegative, compact, AC and BV, its derivative is atom-free and AC, and

```text
it widehat G(t)=(1-e^(-it))widehat mu(t).           (14)
```

The periodic multiplier has uniformly positive mean on every long annulus.
Consequently

```text
int_(|t|>=e^2) |t| log|t| |widehat G(t)|^2 dt
  asymp sum_(n>=2) 1/[n log^2 n] < infinity,        (15)

int_R |widehat G(t)|dt
  asymp sum_(n>=2) 1/[n log n] = infinity.          (16)
```

So even the critical logarithmic strengthening of `H^(1/2)` is insufficient.
Conversely, for every `epsilon>0`, Cauchy--Schwarz gives

```text
int_(|t|>=e) |widehat G(t)|dt
 <=[int |t|(log|t|)^(1+epsilon)|widehat G(t)|^2dt]^(1/2)
   [int dt/(|t|(log|t|)^(1+epsilon))]^(1/2),        (17)
```

and the second factor is finite.  Low frequencies follow from `L2` control.
Thus the `log^(1+epsilon)` condition is sufficient for Fourier/holonomy `L1`,
while the exponent one endpoint fails even for compact AC/BV primitives with
atom-free AC derivative.  This is a sharp logarithmic scale boundary, not a
necessary characterization of all `L1` primitives.

## K1645 — protected integration and hostile bookend

The bridge census is now 360 rows: 281 satisfied, ten conditional, 65
excluded, and four missing.  K1641--K1643 prove that profile-bounded stationary
centrally symmetric laws with uniformly bounded standardized fourth cumulants
and submacroscopic independent dependence blocks retain coefficient
`h_g^prof`.  They isolate macroscopic mode correlation or failure of one of
those uniform hypotheses as necessary inside the block model, not in every
stationary law.  K1644 proves that a single logarithmic half-derivative weight
still does not force holonomy `L1`, while every `log^(1+epsilon)` strengthening
does.

Hostile review rejects transferring block independence to arbitrary stationary
laws, dropping central symmetry or profile/cumulant bounds, calling
`b_N=Omega(N^3)` sufficient for descent, claiming an unrestricted coefficient,
or treating the logarithmic sufficient condition as necessary.  It also
rejects transfer to electric-field `L1`, nonlinear remainders, or a source-owned
flow.

The next quantum wake is an explicit normalized stationary macroscopic-block
family with `D_N=-Omega(N^4)` and controlled `A_N+R_(Omega,N)/4`, or a
coercivity theorem covering that correlated endpoint.  The next PDE wake
remains source-owned derivation of a supercritical logarithmic/Besov primitive
budget and integrable curvature/current/radial remainders.  The source-owned
action/measure/Hamiltonian tuple remains separate.

## Postflight bookend

The variational frontier is now genuinely collective: bounded local
non-Gaussianity across every submacroscopic Fourier block is too small by the
exact factor needed to change the `N^4` coefficient.  The harmonic frontier is
also sharp on the first logarithmic scale: exponent one fails, every exponent
strictly above one suffices.  Protected source, ledger, canon, paper,
prediction, confirmation, and public-posture states are unchanged.
