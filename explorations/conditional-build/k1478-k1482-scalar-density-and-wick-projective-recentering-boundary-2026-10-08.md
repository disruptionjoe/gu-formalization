---
title: "K1478--K1482 scalar-density and Wick projective-recentering boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1478--K1482 scalar-density and Wick projective-recentering boundary

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests global-state
and positive-Hamiltonian requirements bordering SC-META-53. The Maxwell--matter
plane wave, Gaussian field, cutoff Hamiltonians and BRST tower are repository
controls, not released GU data.

```gu-typed-objects
result: ultralocal modified-energy boundary, vacuum--fourth-chaos variational gap, projective-recentering Mosco failure and BRST transfer
carrier: repository Maxwell--massive-matter Fourier control and beta=1 Gaussian reduced Fock space tensored with the Gaussian gauge-boson/ghost complex LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: positive Maxwell--matter energy, Gaussian Q-space pairing and tensor-product BRST Hilbert pairing ON=repository_owned_controls
real_structure: Fourier conjugation, Gaussian real field and coordinatewise complex conjugation
grading: compact charge, spatial frequency, Wiener chaos, particle number, cutoff filtration and ghost number
action_owner: repository-construction -- no released source current decomposition, measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 global-dynamics and interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1473--K1477 leave two exact questions. On the PDE side, the cheapest
structural discriminator asks whether another function of the charge-spectral
matter densities can cancel K1413's lifted-current work. On the quantum side,
the free-vacuum concentration leaves open the sharper prerequisite to a Mosco
construction: whether the exact projective scalar shift even follows the true
ground energy to bounded error.

The PDE route is tested on constrained data before any broad spacetime
calculation. The quantum route uses one normalized fourth-chaos direction,
rather than attempting premature recovery sequences for an incorrectly
centered family. The source-owned selector and full spacetime repair remain
independent, but their missing action/carrier or new-estimate dependencies are
not produced here.

## K1478 — ultralocal scalar densities cannot cancel current work

Choose a nonzero charge eigenvector `Qv=qv` and, on normalized `T3`, initial
data

```text
phi(x)=r exp(i k.x)v,  pi=D_t phi=0,  A=0,
E=E0 constant,         E0.k != 0.
```

The charge density is zero and `div E0=0`, so Gauss holds. Every ultralocal
charge-spectral scalar

```text
S_ab=Re<Q^a phi,Q^b phi>=q^(a+b)r^2
```

is spatially constant and has zero time derivative at the testing time. In
particular `partial_t||phi||^2=0`. But for every lifted tier,

```text
j_n=e Im<Q^(n+1)phi,D Q^n phi>
   = plus-or-minus e q^(2n+1) k r^2,
```

so `integral E0.j_n` is nonzero. Therefore the derivative of every correction
`integral F({S_ab}) dx` built from finitely many ultralocal charge-spectral
matter densities vanishes exactly where K1413's current work survives. This
class cannot be the missing modified energy. Gauge/Maxwell dependence,
covariant derivatives, a nonlocal spacetime normal form or a higher hierarchy
remain open.

## K1479 — vacuum mixing misses the projective energy origin

Write

```text
V_N=integral :phi_N^4: dx,
sigma_N^2=E(V_N^2)=Theta(N^5),
W_N=V_N+6C_N^2,
H_N=H0+gW_N.
```

For fixed `0<a<=1/128`, use the finite-cutoff form vector

```text
psi_N=1-a V_N/sigma_N,       ||psi_N||^2=1+a^2.
```

If `h_N=<V_N,H0V_N>` and `m3_N=E(V_N^3)`, direct expansion gives

```text
R_N-6gC_N^2
 = [a^2 h_N/sigma_N^2-2ga sigma_N
    +ga^2 m3_N/sigma_N^2]/(1+a^2).
```

Because `V_N` is pure fourth Wiener chaos supported below the cutoff,
`h_N<=4 omega_max(N)sigma_N^2` with `omega_max(N)=O(N)`. Gaussian
hypercontractivity gives `||V_N||_3<=4||V_N||_2`, hence
`|m3_N|<=64sigma_N^3`. The fixed choice of `a` makes the linear mixing term
dominate the third moment, while `sigma_N=Theta(N^(5/2))` dominates the free
frequency cost. Thus

```text
E_N-6gC_N^2 <= -c_(g,a) N^(5/2)
```

for all sufficiently large cutoffs. The exact projective shift does not track
the interacting ground energy up to bounded error. This is a one-sided gap,
not a sharp asymptotic for `E_N`.

## K1480 — exact martingality fails semibounded Mosco liminf

The projectively recentered family is exactly

```text
K_N^proj=H_N-6gC_N^2=H0+gV_N.
```

Its spectral bottom tends to minus infinity by K1479. More sharply, put
`chi_N=V_N/sigma_N`. For every fixed cylinder cutoff `M`, Wick martingality
gives

```text
P_(F_M)chi_N=V_M/sigma_N -> 0.
```

Cylinder functions are dense, so `chi_N` converges weakly to zero. The
normalized trials therefore converge weakly to the nonzero vacuum multiple
`1/sqrt(1+a^2)` while their projectively recentered quadratic values tend to
minus infinity. This contradicts Mosco's weak-liminf inequality for every
finite semibounded limiting form on the fixed Gaussian Hilbert space.

The result excludes the exact martingale shift as the semibounded Mosco route.
It does not exclude recentering by `E_N+O(1)`, arbitrary unbounded-below
strong-resolvent behavior, singular dressings, non-Gaussian measures or
changed representations.

## K1481 — the fixed BRST factor inherits the instability

For K1471's tensor construction,

```text
mathbb K_N^proj
 =(H_N-6gC_N^2) tensor 1+1 tensor Delta_BRST.
```

The BRST Laplacian has a zero-energy harmonic vacuum. Tensoring K1480's trial
with that vacuum preserves both the divergent negative form value and the
nonzero weak limit. The full projectively recentered forms, including their
degree-zero harmonic compression, fail the same Mosco-liminf test. Closed
nilpotence remains algebraically stable but cannot repair the matter energy
origin or construct a common interacting continuum domain.

## K1482 — admission replay

The bridge census is now 162 rows: 101 satisfied, ten conditional, 47 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest PDE overclaim would extend K1478 from ultralocal matter-density
corrections to corrections involving `A`, `E`, covariant derivatives or
spacetime nonlocality; those are exactly the surviving routes. The strongest
quantum overclaim would turn failure of the exact projective shift into failure
of true-ground-energy recentering or every beta-one representation. K1479
proves only a one-sided divergent gap, and K1480 uses the fixed Gaussian
Hilbert space essentially. The weakest analytic seam is hypercontractive
control of the third moment; the standard fourth-chaos constant gives the
uniform bound needed by the fixed small trial amplitude, without asserting a
sharp third-moment asymptotic.

Within those ceilings the results are decision-grade: one broad PDE correction
class is removed, and the canonical projective scalar shift is removed from
the semibounded continuum route before any recovery-sequence campaign spends
on the wrong energy origin.

## Exact next input

For the PDE, construct a genuinely gauge-field-dependent bilinear spacetime or
secondary-null estimate, or a derivative/nonlocal modified energy controlling
both K1413 leakages. For the quantum arc, determine the actual asymptotic of
`E_N`, choose `a_N=E_N+O(1)`, and test compactness plus Mosco liminf/recovery on
one common recentered domain. Only that matter limit can support a continuum
version of K1471's BRST-compatible Hamiltonian.
