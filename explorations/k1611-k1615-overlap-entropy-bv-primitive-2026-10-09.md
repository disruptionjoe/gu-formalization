---
title: "Overlap-free Gaussian-mixture rigidity and BV spectral primitives"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__OVERLAP_ENTROPY_RIGIDITY_AND_BV_PRIMITIVE_BUDGET
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Overlap-free Gaussian-mixture rigidity and BV spectral primitives

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
  carrier: translated_stationary_diagonal_gaussian_mixtures_plus_bv_harmonic_spectral_primitive
  pairing_or_form: weighted_relative_fisher_form_quartic_schrodinger_form_and_background_adapted_charge_energy
  real_structure: real_finite_q_space_with_real_flat_harmonic_connection
  grading: gaussian_component_label_and_charge_power_Q_n
  action_owner: repository_control_not_source_owned
  target_object: affinity_weighted_score_mismatch_and_integrable_bv_holonomy_remainder
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1607 used positive-density covariance separation to make Gaussian affinity
exponentially small. That hypothesis is unnecessary. In a fixed relative
band around the K1572 profile, the same covariance and translation differences
that enlarge the score mismatch also enlarge the exact Bhattacharyya exponent.
Their product is uniformly `O_g(N)` for every pair, including pairs with
macroscopic overlap. K1606 then controls a fixed mixture by `O_g(N)` and a
growing mixture by its Renyi-half effective component count.

The independent PDE route replaces K1608's absolutely continuous second
derivative by a finite distributional second-derivative measure. Piecewise
`W^{2,1}` primitive densities with derivative jumps are therefore admitted.
The spectral representation and nonlinear remainder remain assumptions.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain. The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
No source, ledger, canon, paper, prediction, confirmation, or public-posture
state moves.

## K1611 — uniform affinity-score control without separation

Let `S_i=diag(s_(i,k))`, `S_j=diag(s_(j,k))`, and suppose

```text
c_- S_N^* <= S_i,S_j <= c_+ S_N^*.                            (1)
```

The means `m_i,m_j` are arbitrary. Put `Delta_k=m_(i,k)-m_(j,k)` and
`r_k=log(s_(i,k)/s_(j,k))`. The exact Gaussian affinity is

```text
BC_ij=exp(-X_ij),
X_ij=sum_k {psi(r_k)+zeta_k},
psi(r)=(1/2)log cosh(r/2),
zeta_k=Delta_k^2/[4(s_(i,k)+s_(j,k))].                         (2)
```

K1606's score polynomial splits exactly as

```text
P_ij=P_ij^cov+P_ij^mean,
P_ij^cov=sum_k 2 omega_k(s_(i,k)-s_(j,k))^2
                   /[s_(i,k)s_(j,k)(s_(i,k)+s_(j,k))],
P_ij^mean=sum_k 4 omega_k Delta_k^2/(s_(i,k)+s_(j,k))^2.       (3)
```

The second identity follows from
`B_ij h_ij+b_ij=2(S_i+S_j)^(-1)(m_i-m_j)` in the common diagonal basis.
On the compact relative band, `psi(r)` is uniformly comparable to `r^2`,
and the rational covariance factor in (3) is bounded by `C psi(r)`.
Also the mean term is bounded by `C(omega_k/s_(N,k)^*)zeta_k`. Hence

```text
P_ij<=C_(c_-,c_+) Lambda_N X_ij,
Lambda_N=max_k omega_k/s_(N,k)^*=O_g(N).                       (4)
```

Consequently

```text
BC_ij P_ij<=C Lambda_N X_ij exp(-X_ij)<=C Lambda_N/e=O_g(N).   (5)
```

No separation, centeredness, mean bound, or lower bound on `X_ij` is used.
When components approach one another, the score mismatch vanishes; when they
separate, affinity suppresses it.

## K1612 — growing mixtures and Renyi-half rigidity

For `nu_N=sum_i p_(N,i) N(m_(N,i),S_(N,i))`, define

```text
R_(1/2)(p_N)=(sum_i sqrt(p_(N,i)))^2.                           (6)
```

Combining K1606 with (5),

```text
0<=sum_i p_i Q_N(nu_i)-Q_N(nu_N)
 <=C_g Lambda_N sum_(i<j)sqrt(p_i p_j)
 =C_g Lambda_N [R_(1/2)(p_N)-1]/2.                             (7)
```

K1572/K1602 bound every translated stationary diagonal Gaussian component
in the fixed relative band below by `lambda_N^prof`. Therefore

```text
lambda_N^prof-C_g N R_(1/2)(p_N)
 <=Q_N(nu_N),
R_(1/2)(p_N)=o(N^3)  ==>  Q_N(nu_N)/N^4>=h_g^prof-o(1).         (8)
```

The class contains the profiled Gaussian, so its infimum coefficient is
`h_g^prof`. A fixed mixture has `O_g(N)` gain. An equally weighted mixture
with `M_N=o(N^3)` is also coefficient-rigid. Highly nonuniform mixtures may
have many more nominal components when their Renyi-half effective count is
`o(N^3)`. The theorem does not cover `R_(1/2)` of order `N^3` or larger,
non-Gaussian components, phases, textures, or nonstationarity.

## K1613 — bounded-variation primitive decay

Retain K1608's atom-free spectral representation and support away from zero.
For each divided density `G_+` and `G_-`, extend it by zero to the real line.
Assume the extension is in `W^{1,1}(R)` and its distributional second
derivative is a finite signed measure. Equivalently, on finitely many compact
support intervals the density has zero endpoint trace, an `L1` first
derivative, and a first derivative of bounded variation; derivative jumps are
allowed. Put

```text
B_0=||G_+||_1+||G_-||_1,
B_BV=|D^2 G_+|(R)+|D^2 G_-|(R).                                (9)
```

The Fourier-transform identity in distributions gives

```text
|tilde a(t)|<=min(B_0,t^(-2)B_BV).                             (10)
```

Thus

```text
int_0^infinity |tilde a|dt<=B_0+B_BV,
int_0^infinity |tilde a|^2dt<=B_0(B_0+B_BV).                   (11)
```

This strictly contains K1608's zero-extended `W^{2,1}` class and permits
piecewise-smooth spectral primitives with derivative jumps. It still does not
prove `E_h in L1` or derive the spectral measure from nonlinear dynamics.

## K1614 — BV primitive radius composition

K1609 applies verbatim with

```text
B_a=B_0+B_BV,             B_a2=B_0 B_a.                        (12)
```

For arbitrary static asymptotic flat holonomy `a_infinity`, the shifted
reference energy obeys

```text
E_infinity(t)<=E_infinity(0)
 exp[2|e|B_a+(e^2/m)B_a2].                                     (13)
```

If the adapted hierarchy satisfies

```text
B_A(t)<=|e||tilde a(t)|+R(t),  B_R=int_0^infinity R<infinity,  (14)
```

then

```text
rho_infinity>=rho_0-(C_m/4)(|e|B_a+B_R).                       (15)
```

The strict right-hand budget below `rho_0` preserves a positive radius. The
adapted hierarchy, integrable remainder, coercivity, physical domain, and
source-owned action remain unproved inputs.

## K1615 — protected integration and hostile bookend

The bridge census is now 330 rows: 251 satisfied, ten conditional, 65
excluded, and four missing. K1611 removes K1607's separation and centeredness
requirements inside the fixed relative stationary diagonal Gaussian band.
K1612 controls growing mixtures only under the explicit Renyi-half condition.
K1613 weakens primitive regularity but does not derive the representation or
electric-field `L1`. K1614 remains a conditional background-adapted theorem.

The hostile quantum check removes the fixed relative band, replaces
`R_(1/2)=o(N^3)` by a nominal component count with no weight control, or calls
the class unrestricted. The hostile PDE check allows endpoint jumps in `G`,
confuses derivative jumps with density jumps, asserts `E_h in L1`, or promotes
the conditional budget to a source-owned nonlinear flow. None is licensed.

The next quantum wake is the genuinely non-Gaussian/nonstationary
Fisher-defect sector or the critical/supercritical Renyi-half regime. The next
PDE wake is a source-owned nonlinear derivation of the primitive spectral
measure and integrable curvature/current/radial remainder. The source-owned
action/measure/Hamiltonian tuple remains a separate admission gate.

## Postflight bookend

The quantum route closes the entire fixed-finite translated stationary
diagonal Gaussian mixture class in a fixed order-one relative band, whether
components overlap or separate, and quantifies a growing-mixture extension.
The key structural fact is `x exp(-x)`, not a separation census. The PDE route
admits the natural finite-measure second derivative class without changing the
downstream conditional budget.

Strongest overclaim: treating `R_(1/2)=o(N^3)` as unnecessary or transferring
the theorem outside the stationary diagonal Gaussian band. Strongest contrary
construction: a mixture with effective count comparable to `N^3` is not
controlled at coefficient scale by (7). Weakest propagation seam: the BV
primitive remains assumed rather than derived from a source-owned nonlinear
action and physical domain.
