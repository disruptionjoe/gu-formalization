---
title: "K1433--K1438 Wick-chaos and PDE normal-form boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1433--K1438 Wick-chaos and PDE normal-form boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE` only because the packet tests the
positive-state and global-dynamics requirements bordering SC-META-53. The
Fourier covariance, Wick interaction, compact charge sequence and Maxwell--
matter control are repository constructions, not released GU data.

```gu-typed-objects
result: exact equal-time Wick-chaos obstruction and same-tier PDE normal-form exclusion
carrier: real Gaussian scalar Fourier fields on normalized tori and the repository Maxwell--matter multi-charge phase space LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive Gaussian L2 pairing plus classical covariant energy pairing ON=repository_owned_controls
real_structure: Fourier conjugation for the scalar field and compatible-real charge sectors for the PDE
grading: Wiener chaos degree, charge powers, spatial Sobolev tier and Fourier cutoff
action_owner: repository-construction -- no released source measure, renormalization prescription or action-stationary selector
target: SC-META-53 interacting-positive-state and global-dynamics boundary MAP-TYPE=restriction
```

## K1433 — exact three-dimensional fourth-chaos obstruction

On normalized `T^d`, use nested box cutoffs and equal-time covariance

```text
q_k=(2 sqrt(m^2+|k|^2))^-1,
C_N(x-y)=sum_(k in K_N) q_k exp(ik.(x-y)).
```

For `V_N=integral :phi_N^4: dx`, Gaussian chaos gives

```text
E(V_M|F_N)=V_N,
Var(V_N)=24 integral C_N(z)^4 dz
        =24 sum_(k1+...+k4=0) product_i q_ki.
```

If `8|N`, choose `k1,k2,k3` componentwise in `[N/8,N/4]` and set
`k4=-(k1+k2+k3)`. All four momenta lie in `K_N`, giving

```text
Var(V_N) >= (3/2)(N/8+1)^(3d)/(m^2+dN^2)^2.
```

In three spatial dimensions this grows like `N^5`, so the martingale is not
`L2` bounded or Cauchy. For deterministic quadratic and vacuum counterterms,

```text
U_N-EU_N=V_N+(6C_N+a_N) integral :phi_N^2: dx.
```

Orthogonality of the fourth, second and zeroth Wiener chaoses gives
`Var(U_N)>=Var(V_N)`. Wick ordering is the variance-minimizing pure-fourth-
chaos choice, but mass and vacuum counterterms cannot produce an `L2`
multiplication-potential limit in `d=3`. This is not an operator no-go:
free-Hamiltonian smoothing, closed quadratic forms, coupling or field-strength
renormalization, and resolvent limits remain outside the theorem.

## K1434 — dimensional positive control

For the same covariance in `d=1`, `q` lies in `ell^(4/3)`. Hausdorff--Young
gives `C_N -> C` in `L4`, so the Wick martingale converges in `L2`. For every
integer `d>=2`, K1433's cone lower bound grows as `N^(3d-4)`. The obstruction
is dimensional, not a failure of Hermite martingale algebra. A Euclidean
covariance `(m^2+|k|^2)^-1` has different power counting and is not silently
substituted.

## K1435 — harmonic electric resonance

Retain K1397's harmonic electric mode and take
`phi_q=a cos(omega_q(k)t) exp(ik.x)v_q` with `E_h.k!=0`. The linear Gauss
constraint holds, while K1413's lifted-current work has nonzero period average

```text
(e Vol/2) q^(2n+1) a^2 (E_h.k).
```

The derivative of a bounded autonomous cubic normal form has zero period
average, so it cannot cancel this leakage. Adding one multiple of Maxwell
energy requires coefficient `q^(2n)`; realized charges `4` and `8` demand
incompatible coefficients. A strict zero-harmonic sector removes this witness
and remains open.

## K1436 — radial curl and derivative loss

For unequal absolute charges, set `M0=x+y` and
`Mn=q^(2n)x+r^(2n)y`. A derivative-free quartic correction would require
`M0 dMn` to be exact, but

```text
d(M0 dMn)=(r^(2n)-q^(2n)) dx wedge dy != 0.
```

The free homological divisor also obeys

```text
(omega_q(K)+omega_r(K))/(omega_q(K)-omega_r(K))
  ~ 4K^2/(mu(q^2-r^2)),
```

so a time-local cross-charge correction loses two spatial derivatives and is
not bounded on the same tier.

## K1437--K1438 — joint boundary and admission

Together the results exclude bounded autonomous time-local polynomial normal
forms and coercively equivalent same-tier energies as a common repair for both
K1413 defects. They leave strict zero-harmonic nonzero-mode analysis, gauge-
covariant spacetime/null-form estimates, deliberately higher-tier corrections,
and summable hierarchies open.

The bridge census now has 106 rows: 72 satisfied, eight conditional, 22
excluded and four missing. The source selector/action, interacting continuum
positive physical cohomology with global PDE evolution, and observed-state
export remain missing. K1145/K1150 stay `0/7`; protected statuses do not move.

## Exact next input

For the quantum arc, construct a renormalized closed form or self-adjoint
resolvent limit that genuinely uses the free Hamiltonian and states every
additional counterterm. For the PDE arc, test the strict zero-harmonic
nonzero-mode null structure or a higher-tier/summable hierarchy with an
explicit finite-tier Cauchy consequence. Source admission still requires an
action-stationary observed-carrier selector fixing `Q` and its normalization.
