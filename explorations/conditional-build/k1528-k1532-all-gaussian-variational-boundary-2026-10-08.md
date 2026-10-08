---
title: "K1528--K1532 all-Gaussian variational boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1528--K1532 all-Gaussian variational boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests the positive
Hamiltonian prerequisite bordering SC-META-53. The Gaussian cutoff field,
arbitrary Gaussian Q-space trial family, nonlinear Hamiltonian and BRST complex
are repository controls, not released GU data.

```gu-typed-objects
result: exact arbitrary-Gaussian Q-space free form, local Wick-square coercivity, matrix ultraviolet-shell cost and an all-Gaussian N^4 variational boundary
carrier: beta=1 Gaussian reduced Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing ON=repository_owned_control
real_structure: real Fourier covariance basis with arbitrary positive covariance matrix and optional real linear-quadratic phase
grading: spatial frequency, ultraviolet shell, local variance, integrated covariance mass, free energy, Wick-square energy and cutoff filtration
action_owner: repository-construction -- no released source measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1523--K1527 exclude coherent and stationary translation-invariant diagonal
quasi-free trials from matching K1519's unrestricted `Omega(N^2)` lower scale.
Their exact next wake is whether nonstationary or off-diagonal Gaussian
covariance can evade the shell dichotomy. It cannot.

The key is to separate two questions that stationarity previously collapsed.
An arbitrary covariance has a spatially varying point variance `v(x)`, but the
one-point field law remains Gaussian. Its optimized Wick-square expectation is
therefore pointwise coercive in `C_N v(x)`, even when `v` forms sharp spikes.
The spatial average is the matrix trace `Tr(Lambda S)`. If that trace is small,
the outer-shell deficit is large; a noncommutative Frobenius factorization then
prices it with the exact covariance part of the free form. No simultaneous
diagonalization with the frequency operator is needed.

This closes the entire finite-cutoff Gaussian-wavefunction route, including
linear-quadratic phases. It does not touch genuinely non-Gaussian likelihoods,
singular representation changes, the true ground-energy asymptotic, or the
source-owned GU state-space problem.

## K1528 — exact arbitrary-Gaussian Q-space formula

Let the real cutoff coordinate vector be `xi`, distributed under the standard
Gaussian measure `mu`. For an arbitrary mean vector `m` and a real symmetric
positive-definite covariance `S`, define the probability density

```text
rho_(m,S)(xi)
 =det(S)^(-1/2)
  exp[-(1/2){(xi-m)^T S^(-1)(xi-m)-xi^T xi}]
```

relative to `mu`. The normalized positive Gaussian amplitude is
`psi=rho^(1/2)`. Its logarithmic gradient is

```text
grad log psi
 =(1/2)[(I-S^(-1))xi+S^(-1)m].
```

Under `rho mu=N(m,S)`, write `xi=m+z`. The bracket becomes
`m+(I-S^(-1))z`, with the centered cross term zero. If
`Omega=diag(omega_j)`, the exact free form is

```text
q_0[psi]
 =(1/4){m^T Omega m
         +Tr[Omega(S+S^(-1)-2I)]}.
```

Indeed,

```text
(I-S^(-1))S(I-S^(-1))
 =S+S^(-1)-2I
 =(I-S)S^(-1)(I-S)>=0.
```

This identity does not require `[S,Omega]=0`. When `S=diag(s_j)`, it reduces
exactly to K1524's `sum omega_j(s_j-1)^2/s_j`.

A general pure Gaussian wavefunction may also carry a real linear-quadratic
phase `exp(i theta(xi))`. Since

```text
|grad(psi exp(i theta))|_Omega^2
 =|grad psi|_Omega^2+psi^2|grad theta|_Omega^2,
```

the phase adds a nonnegative cost and cannot improve the variational lower
bound. The argument therefore covers arbitrary finite-cutoff Gaussian
wavefunctions, not just positive amplitudes.

## K1529 — local mean/variance coercivity

Let

```text
b_N(x)_j=sqrt(lambda_j)e_j(x),
h(x)=b_N(x)^T m,
v(x)=b_N(x)^T S b_N(x),
C_N=|b_N(x)|^2.
```

The vacuum variance `C_N` is spatially constant, but `v(x)` need not be. At
each point, the scalar field is a one-dimensional Gaussian with mean `h` and
variance `v`. Its exact square-completed Wick expectation is

```text
F_C(h,v)
 =h^4+6h^2v+3v^2-6C(h^2+v)+9C^2.
```

Minimize over `y=h^2>=0`. The two branches are

```text
0<=v<=C:
  y=3(C-v),
  f_C(v)=6v(2C-v);

v>=C:
  y=0,
  f_C(v)=3(v-C)^2+6C^2.
```

These branches admit a uniform linear lower bound. For `0<=v<=C`,
`f_C(v)/(Cv)=6(2-v/C)>=6`. For `t=v/C>=1`,

```text
f_C(v)/(Cv)=3(t-2+3/t),
```

whose minimum occurs at `t=sqrt(3)`. Thus, with the sharp constant

```text
c_*=6(sqrt(3)-1),
```

one has

```text
F_C(h,v)>=f_C(v)>=c_* C v
```

for every mean and every local variance. In particular, a covariance cannot
hide its total mass in thin high-variance spatial spikes: the lower bound is
pointwise and linear in `v`.

Orthonormality of the real Fourier basis gives

```text
V_N=int v(x)dx=Tr(Lambda S),
```

so the interaction expectation is at least `g c_* C_N V_N`.

## K1530 — matrix ultraviolet-shell cost

Let `P=P_N` be the real-mode projector onto the fixed-ratio outer shell from
K1525. The diagonal matrices `P`, `Lambda` and `Omega` commute, and

```text
C_(S,N)=Tr(P Lambda)>=kappa C_N.
```

Because both `Lambda` and `S` are positive,

```text
V_N=Tr(Lambda S)>=Tr(P Lambda S)>=0.
```

If `V_N>(kappa/2)C_N`, K1529 already gives

```text
g int E[W_N]dx
 >=g c_* C_N V_N
 >=c_g C_N^2
 =Omega_g(N^4).
```

It remains to treat `V_N<=(kappa/2)C_N`. Then the shell deficit

```text
delta_N
 =Tr[P Lambda(I-S)]
 =Tr(P Lambda)-Tr(P Lambda S)
 >=(kappa/2)C_N
 =Theta(N^2).
```

Define

```text
A=Omega^(1/2)(I-S)S^(-1/2),
B=S^(1/2)P Lambda Omega^(-1/2).
```

Trace cyclicity gives `Tr(AB)=delta_N`. Frobenius Cauchy therefore yields

```text
delta_N^2
 <=Tr[Omega(S+S^(-1)-2I)]
   Tr[P Lambda^2 Omega^(-1)P S].
```

On the outer shell, `lambda_j/omega_j=O(N^(-2))`, hence

```text
P Lambda^2 Omega^(-1)P
 <=cN^(-2)P Lambda
```

in Loewner order. Consequently,

```text
Tr[P Lambda^2 Omega^(-1)P S]
 <=cN^(-2)Tr(P Lambda S)
 <=cN^(-2)V_N
 =O(1).
```

The covariance part of K1528's free form is one quarter of the first Cauchy
factor. Since `delta_N^2=Theta(N^4)`, the low-variance branch has
`q_0>=cN^4`.

This proof retains every off-diagonal shell/complement correlation in positive
matrix traces. It never assumes that `S` commutes with `P`, `Lambda` or
`Omega`, and it never assumes stationarity of the local variance profile.

## K1531 — the all-Gaussian bottom is `Theta(N^4)`

Let `E_N^Gauss` be the infimum over normalized finite-cutoff Gaussian Q-space
wavefunctions with arbitrary mean, positive covariance and real
linear-quadratic phase. K1529--K1530 give

```text
E_N^Gauss>=c_gN^4.
```

The vacuum is in the class and has energy `6gC_N^2=O(N^4)`. Therefore

```text
E_N^Gauss=Theta_g(N^4).
```

The predecessor's nonstationary/off-diagonal Gaussian escape is closed. An
order-`N^2` upper trial, if one exists in the fixed representation, must be
genuinely non-Gaussian. A singular change of representation or domain changes
the admitted question and is not silently included.

Every subquartic scalar shift leaves all Gaussian Rayleigh quotients divergent
to `+infinity`. This remains a restricted trial-class statement, not a
spectral or resolvent theorem for the full Hamiltonian. Tensoring a classified
Gaussian matter vector with a harmonic BRST vector preserves the same Rayleigh
quotient, so only this restricted boundary transfers. No continuum interacting
charge, physical cohomology or GU Hilbert space follows.

K1519 still supplies only the unrestricted `E_N>=c_gN^2` lower bound, while
K1516 supplies the nonmatching upper descent from `6gC_N^2`. The actual
ground-energy asymptotic, localization, compactness and Mosco recovery remain
open.

## K1532 — admission replay

The bridge census is now 240 rows: 161 satisfied, ten conditional, 65 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would promote the Gaussian `Theta(N^4)` result to the
true ground-energy asymptotic. That is invalid. The theorem classifies
finite-dimensional Gaussian wavefunctions—now with arbitrary covariance and
phase—but does not constrain general non-Gaussian vectors in the nonlinear
form domain.

The most delicate algebraic seam is matrix order. Positivity of
`S+S^(-1)-2I` does not come from commuting `S` with `Omega`; it comes from the
factor `(I-S)S^(-1)(I-S)`. The shell estimate pairs two Frobenius factors and
uses cyclicity only after their product is formed. The dual Loewner comparison
is between diagonal shell weights before tracing against positive `S`.

The strongest contrary construction is a non-Gaussian amplitude that suppresses
the low-Wick-square event without paying the Gaussian covariance Fisher cost.
The theorem neither constructs nor excludes it. A mixed non-Gaussian state,
singular dressing or inequivalent reference measure is also outside the
classified class.

The source boundary is unchanged. The cutoff field and Hamiltonian are
repository controls bordering SC-META-53, not an action-owned GU quantization.
No result here selects a source measure, interacting BRST charge, physical
carrier or observed map.

## Exact next input

Construct or exclude a genuinely non-Gaussian normalized trial with energy
comparable to `N^2`. A useful next discriminator should identify a concrete
nonlinear likelihood or geometric localization family and compute both its
Dirichlet cost and Wick-square expectation without reducing it back to a
Gaussian covariance change. Only after identifying `E_N` to bounded error
should compactness and Mosco liminf/recovery be tested on one common nonlinear
domain. Independently, K1413 still requires a genuinely gauge/Maxwell-dependent
spacetime, secondary-null or derivative/nonlocal estimate, and source admission
still requires one action-owned primitive circle, kinetic normalization,
physical carrier and faithful observed intertwiner.
