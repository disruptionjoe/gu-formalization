---
title: "Wick-dominant non-Gaussian coefficient and flat-connection radius boundary"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__K1573_RAW_B_A_GLOBAL_NECESSITY
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Wick-dominant non-Gaussian coefficient and flat-connection radius boundary

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff scalar-field variational problem and a periodic gauge-PDE
> control. It is not a source-native GU action, physical state space,
> observed carrier, prediction, confirmation, or falsification of a
> registered source claim. Conventional comparator conclusions bind only the
> model stated here and do not transfer to Weinstein's source-native mechanism
> without an explicit typed bridge.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: finite_cutoff_translation_invariant_density_states_plus_periodic_charged_fields
  pairing_or_form: weighted_relative_fisher_form_and_flat_connection_covariant_energy
  real_structure: real_fourier_q_space_with_complex_u1_charged_pde_field
  grading: cube_cutoff_modes_and_charge_powers_Q_n
  action_owner: repository_control_not_source_owned
  target_object: wick_dominant_nongaussian_coefficient_and_K1573_raw_B_A_budget
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

The quantum arc keeps K1433's finite cube cutoff and K1572's normalized
three-torus, positive mass and positive coupling. It enlarges the stationary
diagonal Gaussian class to translation-invariant finite-Fisher densities with
nonnegative integrated Wick defect. The unrestricted theory remains outside
that sign condition.

The PDE arc keeps K1568--K1573's smooth periodic temporal-gauge convention.
It asks whether the displayed `B_A` budget is a necessary dynamical cost. A
static flat connection is the cheapest decisive control because it has
nonzero potential and zero curvature. If the raw budget spends radius there
while the exact covariant flow conserves energy, the global route must separate
harmonic holonomy from curvature-bearing modes.

The source claims SC-ACT-01/02/06 remain assertions and SC-META-53 remains
uncertain. The standing physics rows LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain
`NEEDS`; none supplies the action, measure, Hamiltonian, physical quotient or
observed map used below.

## K1576 — all-density reduction in the stationary Wick-dominant class

At cutoff `N`, let `T_N^+` consist of normalized wavefunctions

```text
psi=sqrt(rho) exp(i theta)
```

with finite weighted relative Fisher information and translation-invariant
law. Write the constant spatial mean as `h`, the translation-invariant
covariance as `S`, and at each point write the centered moments as
`v, mu_3, mu_4`. Require only

```text
int_[T^3] {4h mu_3(x)+mu_4(x)-3v(x)^2} dx >= 0.    (1)
```

This is a genuinely non-Gaussian class. It includes stationary laws whose
centered fluctuations are symmetric and have nonnegative fourth cumulant,
including finite-Fisher translation-invariant linear images of independent
symmetric positive-kurtosis coordinates and stationary Gaussian scale
mixtures.

K1533 gives, for the moment-matched Gaussian `gamma_(h,S)`,

```text
q_0[psi] >= q_0[gamma_(h,S)].                       (2)
```

The phase term is nonnegative. K1534 gives the exact interaction identity

```text
E_psi W_N=E_gamma W_N
 +int {4h mu_3+mu_4-3v^2}.                         (3)
```

Thus (1)--(3) imply

```text
q_0[psi]+gE_psi W_N
 >=q_0[gamma_(h,S)]+gE_gamma W_N.                  (4)
```

Translation invariance makes `S` Fourier diagonal, with the usual real-mode
conjugacy, and makes `h` a zero-mode constant. Therefore the Gaussian on the
right of (4) belongs exactly to K1572's stationary diagonal class. Conversely
every member of that Gaussian class has zero defect and lies in `T_N^+`.
The finite-cutoff infima are equal.

The defect sign is load-bearing. K1534's thin symmetric two-well states have
negative fourth cumulant and are excluded. No conclusion applies to arbitrary
negative-kurtosis or nonstationary likelihoods.

## K1577 — matching coefficient and rigidity

Let `E_N^(T+)` be the infimum over `T_N^+`. The exact finite-cutoff identity
and K1572 give

```text
E_N^(T+)/N^4 -> h_g^prof.                           (5)
```

This is a matching leading coefficient over a materially non-Gaussian density
class, not merely a Gaussian trial upper bound. It inherits K1571's coupling
classification:

```text
g log(1/kappa_g) -> 1/(12pi),
(6gc_C^2-h_g^prof)/kappa_g^2 -> pi/16,
h_g^prof=4sqrt(24c_Cg)-4/c_C-c_Omega/2+o(1).       (6)
```

Equality is rigid. K1533 forces the density to be the moment-matched Gaussian
and the phase to be constant; (1) must also be saturated. K1572 then fixes the
unique larger finite-cutoff minimizing profile for large `N`. Non-Gaussian
members can approach equality only by closing both nonnegative gaps.

Equation (5) is not the unrestricted ground-energy coefficient. Negative
integrated defect, nonstationarity, an `O(1)` recentering, compactness and
Mosco recovery remain open.

## K1578 — the raw `B_A` budget is not globally necessary

On a periodic three-torus in temporal gauge take

```text
A(t,x)=a != 0,    E=-partial_t A=0,    div A=0.     (7)
```

K1573's coefficient becomes

```text
B_A=|e||a|,
int_0^T B_A dt=|e||a|T.                             (8)
```

The integral diverges as `T` tends to infinity, so the transparent radius law
`rho'=-(C_m/4)B_A` exhausts every finite initial radius. Yet (7) is flat: its
Maxwell curvature energy is zero.

This is not generally removable by a periodic gauge. For torus periods `L_j`,
the phase that removes `a` is periodic exactly when

```text
e a_j L_j in 2pi Z,    every j.                     (9)
```

Generic constant `a` is a genuine flat holonomy. Hence uniform energy or
Sobolev bounds cannot imply `B_A in L1_t`, and the raw K1573 budget is a
sufficient estimate rather than a necessary dynamical condition.

## K1579 — covariant energy cancels the flat mode exactly

For the fixed background (7), define

```text
D_a=grad-i e a,
H_a[phi]=(1/2)int(|partial_t phi|^2+|D_a phi|^2
                  +m^2|phi|^2).                    (10)
```

The Fourier mode `k` has frequency

```text
omega_k(a)=sqrt(|k-ea|^2+m^2).                      (11)
```

Each coefficient is an uncoupled oscillator, so (10) is exactly conserved.
The global charge generator `Q` commutes with the fixed covariant operator;
therefore the same identity holds for every `Q^n phi`, and every positive
charge-analytic sum of these adapted energies is constant on its interval of
finiteness. The static flat mode consumes zero analytic radius even when its
holonomy prevents periodic gauge removal.

The `|e|||A||_infinity` term in raw `B_A` is therefore an absolute-value
artifact on this sector. A global nonlinear route must separate harmonic flat
connection from curvature-bearing and time-dependent modes, control evolving
holonomy, and prove integrability or cancellation only for the remainder.
This does not yet control a time-dependent harmonic electric mode, nonlinear
current feedback, the radial term or the completed full flow.

## K1580 — protected integration and postflight hostile bookend

The bridge census is now 295 rows: 216 satisfied, ten conditional, 65
excluded and four missing. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53
remains `UNCERTAIN`; the physics ledger remains 33 SAME / 22 DIFFERS / 31
NEEDS / 2 OVER-DETERMINED; K1145/K1150 remain `0/7`. No source, ledger,
canon, paper, prediction, confirmation or public-posture state moves.

The hostile quantum pass rejects the unrestricted wording: the exact matching
coefficient requires translation invariance and the nonnegative integrated
defect (1). The hostile PDE pass rejects two opposite mistakes. A generic
constant connection is not a periodic pure gauge, but its raw radius cost is
also not physical growth: the covariant Fourier energy remains conserved.

The next quantum debt is the negative-defect sector, especially whether its
interaction cancellation necessarily incurs enough Fisher cost to preserve
the same coefficient or a bounded-error recentering. The next PDE debt is a
nonlinear harmonic/oscillatory split with a positive limiting radius, or a
genuine spacetime cancellation for the remainder. The source-owned
action/measure/Hamiltonian tuple remains a separate admission gate.
