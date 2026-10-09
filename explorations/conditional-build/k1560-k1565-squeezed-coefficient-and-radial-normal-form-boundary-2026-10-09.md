---
title: "K1560--K1565 squeezed coefficient and radial normal-form boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-09"
updated_at: "2026-10-09"
---

# K1560--K1565 squeezed coefficient and radial normal-form boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification is `SOURCE_NATIVE_ROUTE` because this packet sharpens a
repository-owned positive-Hamiltonian control bordering SC-META-53 and a
conditional PDE estimate. The box cutoff, Gaussian trial family, nonlinear
Hamiltonian and temporal-gauge identities are not released GU data.

```gu-typed-objects
result: exact cube-cutoff Weyl coefficients, optimized uniform-squeeze limsup coefficient, radial same-tier exchange and residual-gauge boundary cocycle
carrier: beta=1 Gaussian reduced Fock control plus classical Maxwell-matter graph tiers LAYER=toy BRIDGE=positive-state-and-flow-requirements CHIRALITY=N/A
pairing: normalized torus Fourier L2 pairing, Gaussian Q-space pairing, charge pairing and temporal-gauge spatial current pairing ON=repository_owned_control
real_structure: real cutoff trigonometric field for the variational calculation; compatible complex matter carrier for the Maxwell-current identities
grading: box cutoff radius, covariance/frequency Weyl order, uniform squeeze, charge graph tier and spacetime boundary degree
action_owner: repository-construction -- no released source measure, Hamiltonian, counterterm, gauge choice, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary and K1413 conditional PDE control MAP-TYPE=restriction
```

## Preflight bookend

K1557 proves only `E_N=Theta_g(N^4)`: it neither identifies the coefficient
nor gives bounded-error recentering. K1524 supplies exact stationary
quasi-free formulas but does not optimize their leading coefficient. The
first load-bearing correction in this packet is geometric: K1433 uses the box
`K_N={k in Z^3: ||k||_infinity<=N}`, not a Euclidean ball. Consequently the
leading constants are cube integrals and are not `pi`.

On the PDE arc, K1558 exchanges the electric-current leakage but leaves both
the radial derivative and differentiated-current term. K1450 already controls
both leakages conditionally through a shrinking analytic hierarchy. The new
packet tests whether exact normal forms simplify that conditional boundary; it
does not replace K1450 or globalize the flow.

## K1560 — cube-cutoff Weyl coefficients

Let

```text
omega_k=sqrt(m^2+|k|^2),
C_N=sum_(k in K_N)(2omega_k)^(-1),
Omega_N=sum_(k in K_N)omega_k.
```

Choosing one representative from each nonzero `plus/minus k` pair gives one
zero coordinate and two real cosine/sine coordinates per pair, hence exactly
`|K_N|` real covariance coordinates. There is no extra factor two.

Put `L=log((1+sqrt(3))/sqrt(2))`. Lattice Riemann sums on the cube give

```text
C_N/N^2 -> c_C=12L-pi                         (1)
Omega_N/N^4 -> c_Omega=2sqrt(3)+8L-pi/3.      (2)
```

Numerically, `c_C=4.760154727959107...` and
`c_Omega=7.684735651640424...`. For (1), convergence away from the origin is
ordinary and the singular part is uniform because

```text
sum_(0<|k|<=delta N)|k|^(-1)=O(delta^2N^2).   (3)
```

Cube symmetry and elementary face integration evaluate the limiting
integrals. Fixed mass and the origin cell are lower order. These are leading
coefficients only, not a bounded-error lattice expansion.

## K1561 — exact uniform-squeeze energy

Fix `0<s<=1`, take covariance `S=sI`, and let `y=a^2>=0` be the square of a
constant physical mean. The zero `Q` coordinate contributes the exact free
cost `(m^2/2)y`. K1524 therefore gives

```text
R_N(s,y)=Omega_N/4 (s+s^(-1)-2)+(m^2/2)y
 +g[y^2-6C_N(1-s)y+C_N^2(3s^2-6s+9)].        (4)
```

The exact optimizer and optimized value are

```text
y_N^*=[3C_N(1-s)-m^2/(4g)]_+,                 (5)

R_N^*(s)=Omega_N/4 (s+s^(-1)-2)
 +gC_N^2(3s^2-6s+9)
 -[6gC_N(1-s)-m^2/2]_+^2/(4g).                (6)
```

On the active-mean branch, (6) is equivalently

```text
Omega_N/4 (s+s^(-1)-2)+6gC_N^2s(2-s)
 +(3m^2/2)C_N(1-s)-m^4/(16g).                 (7)
```

Thus the fixed-`s` leading coefficient is

```text
e_g(s)=c_Omega/4 (s+s^(-1)-2)+6g c_C^2 s(2-s). (8)
```

## K1562 — optimized family coefficient

Relative to the vacuum endpoint,

```text
e_g(s)-e_g(1)=(1-s)^2[c_Omega/(4s)-6g c_C^2]. (9)
```

Hence the family threshold is

```text
g_c=c_Omega/(24c_C^2)=0.0141310864013... .     (10)
```

For `0<g<=g_c`, the uniform-squeeze family is minimized at `s=1` with value
`6g c_C^2`. For `g>g_c`, its unique minimizer satisfies

```text
48g c_C^2 s_g^2=c_Omega(1+s_g),                (11)

s_g=[c_Omega+sqrt(c_Omega^2+192g c_C^2 c_Omega)]
    /(96g c_C^2),                               (12)
```

and has coefficient

```text
h_g=c_Omega(s_g^2-3s_g+4)/(8s_g)<6g c_C^2.     (13)
```

Therefore

```text
limsup_(N->infinity) E_N/N^4 <= min_(0<s<=1)e_g(s). (14)
```

For `g>g_c`, this is a strict unrestricted upper bound below the vacuum
coefficient, obtained from one explicit family. It is not convergence of the
ratio, a matching lower coefficient, a full-theory phase transition,
bounded-error recentering, compactness or Mosco recovery.

## K1563 — radial normal-form exchange

Write `psi_n=Q^n phi` and let `F_n^PDE` be K1413's positive graph energy,
including `(lambda/2)int |phi|^2|psi_n|^2`. Define

```text
R_n=-(lambda/2)int |phi|^2|psi_n|^2,
H_n=F_n^PDE+R_n.                                  (15)
```

Then `H_n` is the positive quadratic covariant graph energy and

```text
H_n'=int E dot j_n
 -lambda Re int |phi|^2<psi_n,D_t psi_n>.         (16)
```

For `m>0`, its second term obeys the same-charge-tier conditional estimate

```text
|radial work| <= (|lambda|/m)||phi||_infinity^2 H_n. (17)
```

Adding K1558's `M_n=int A dot j_n` in temporal gauge gives

```text
(H_n+M_n)'=-lambda Re int |phi|^2<psi_n,D_t psi_n>
            +int A dot partial_t j_n.             (18)
```

This removes `partial_t|phi|^2` without a charge-tier shift, but the
coefficient `||phi||_infinity^2` is not controlled by base energy. Moreover
`M_n` is indefinite and adjacent-tier; coercivity and differentiated-current
control remain open.

## K1564 — continuity and the residual-gauge cocycle

For `psi_n=Q^n phi`, define

```text
rho_n=e Im<Q psi_n,D_t psi_n>,
j_n^a=e Im<Q psi_n,D^a psi_n>.                     (19)
```

The real scalar potential and its commutation with charge imply

```text
partial_t rho_n+div j_n=0.                         (20)
```

Under a smooth periodic, time-independent residual temporal-gauge
transformation `A -> A+grad chi` and the matching charge phase for `psi_n`,
the density and current are invariant, while

```text
delta M_n=int grad chi dot j_n
         =d/dt int chi rho_n.                      (21)
```

Thus `M_n` is not instantaneously gauge invariant: it carries an exact time-
boundary cocycle. A coercive construction must fix the residual gauge or add
a compatible charge-boundary convention. Equation (21) covers the smooth
periodic core, not large non-single-valued gauges, spatial boundaries,
completed domains or the differentiated-current remainder.

## K1565 — protected admission replay

The bridge census is now 280 rows: 201 satisfied, ten conditional, 65
excluded and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53
remains `UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS
/ 2 OVER-DETERMINED, and K1145/K1150 stay `0/7`. No source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile bookend

The highest-value hostile finding was a genuine blocking correction: replacing
K1433's cube by a ball would give the tempting but wrong pair
`c_C=c_Omega=pi` and threshold `1/(24pi)`. A second correction was the
zero-mode coherent cost, which changes the exact finite-cutoff optimizer from
`3C_N(1-s)` to the positive-part formula (5). The producers and probes pin
both corrections and the exact formula (6).

The variational result remains one-sided and family-scoped. Nonuniform,
off-diagonal, nonstationary and non-Gaussian states may lower the coefficient;
a matching unrestricted lower coefficient and `O(1)` recentering remain open.
On the PDE side, (17) is conditional on an uncontrolled `L-infinity`
coefficient, while (18) contains an adjacent-tier, gauge-cocyclic correction
and differentiated current. K1450 remains the available conditional hierarchy;
K1563--K1564 classify a simplification boundary, not a replacement theorem.

The exact next wakes are: prove a matching unrestricted lower coefficient or
bounded-error recentering for the cutoff Hamiltonian; control the
differentiated current inside a coercive gauge-fixed or spacetime-completed
hierarchy; and obtain a source-owned action/measure/Hamiltonian tuple before
any GU-native physical admission.
