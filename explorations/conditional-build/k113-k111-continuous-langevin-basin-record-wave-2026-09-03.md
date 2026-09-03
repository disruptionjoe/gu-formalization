---
title: "K113 K111 continuous Langevin basin record and finite-energy boundary"
status: active_research
doc_type: conditional_continuous_diffusion_basin_record_and_domain_result
created: 2026-09-03
date: 2026-09-03
claim_ceiling: exact finite-dimensional reflected-diffusion, Gibbs/Dirichlet-form, equivariant basin-record and zero-noise concentration theorem on the repository-coordinate K111 simplex; the sharp record is measurable but not a finite-energy generator-domain observable and exact vacua have zero mass at finite temperature; no source/GU stochastic action, physical environment or detector, spacetime causal BV-BFV descent, Born derivation, prediction or confirmation follows
manifest: lab/process/k113-k111-continuous-langevin-basin-record-wave.json
probe: tests/channel-swings/k113_k111_continuous_langevin_basin_record_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K113 K111 continuous Langevin basin record and finite-energy boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

Scope: this packet constructs an exact finite-dimensional classical reflected
diffusion on K111's repository-coordinate simplex. It owns a potential, noise
covariance, invariant measure, reflecting boundary domain, variational
dissipation law and measurable branch coarse-graining. It does not authenticate
the construction as Weinstein's source action, assign it a physical bath or
clock, or produce a spacetime stochastic field theory.

```gu-typed-objects
result: one S_256-equivariant reflected overdamped Langevin law on the K111 simplex has Gibbs stationary measure and a uniform almost-sure argmax basin record, but the sharp record is outside the diffusion Dirichlet domain and exact K111 branches occur only in the singular zero-noise conditional limit
carrier: K111 closed normalized nonnegative weight simplex Delta_255 inside the K105 positive coefficient-blind seed space LAYER=observed CHIRALITY=N/A
pairing: relative 255-dimensional Lebesgue measure and Euclidean tangent metric for the Gibbs/Dirichlet construction, with the inherited K105 lowerer used only after basin-label transport ON=repository_continuous_boundary_control
real_structure: real simplex coordinates, real Brownian tangent noise, real quartic potential and real inherited K105/K91 branch interfaces
grading: degree-zero classical diffusion and measurable basin center, with inherited minimal K91 BRST grading only branchwise
action_owner: repository-construction -- K111's quartic as a finite-dimensional Langevin potential plus reflecting Skorokhod boundary term; not authenticated as Weinstein's source action or a physical GU environment
target: continuous stochastic variational ownership, basin-record regularity, zero-noise branch recovery and finite-energy observable/domain descent MAP-TYPE=evaluation
```

## Inline preflight bookend

K111 owns a symmetric quartic on the complete continuous simplex but has no
branch law. K112 owns a uniform finite Markov law and perfect classical record
only after restricting to K111's 256 vacua. The open reverse edge is therefore
not another finite transition matrix. It is whether the continuous carrier can
own the measure, noise, boundary and variational data needed for a stochastic
law, and whether its natural branch readout belongs to the same analytic
domain.

The route census compared unconstrained ambient noise, softmax coordinates,
absorbing wells, reflected diffusion and an unowned spacetime stochastic PDE.
Ambient noise exits the simplex. Softmax changes the metric and hides the
boundary at infinity. Absorption imports terminal-branch semantics and destroys
the equilibrium question. A spacetime PDE has no authenticated field action or
causal covariance to act on. Normal reflection is the minimal route that keeps
K111's exact carrier and potential while making covariance, invariant measure,
boundary domain and variational structure explicit. Its switch condition is a
failure of tangent covariance or zero-flux detailed balance; neither occurs.

## 1. Continuous reflected nonlinear dynamics

Let

```text
n=256,
Delta={w in R^n : w_i>=0 and sum_i w_i=1},
T={x in R^n : sum_i x_i=0},
Pi=I-(1/n)11^T,
V(w)=sum_i ((w_i-a)(w_i-b))^2,
a=2/257, b=1/257.
```

For inverse temperature `beta>0`, define the normally reflected overdamped
Langevin process on the compact convex simplex by the Skorokhod equation

```text
dW_t=-Pi grad V(W_t) dt+sqrt(2/beta) Pi dB_t+dK_t,          (1)
```

where `K_t` has bounded variation, grows only on the boundary and points in the
inward normal cone. The covariance on `T` is exactly `(2/beta)Pi`. Both `Pi`
and `V` commute with coordinate permutations, and the normal cone is
permuted into itself, so (1) is `S_256`-equivariant. The drift is cubic and the
process lives on K111's full nonlinear carrier rather than its finite vacuum
orbit.

On the Neumann core its generator is

```text
L_beta f=-<grad_T V,grad_T f>+(1/beta) Delta_T f,            (2)
partial_n f=0 on each boundary face.                         (3)
```

The reflected process is the standard diffusion associated with the closure of
this form on the connected compact simplex. This is an analytic boundary
domain for the finite-dimensional control. It is not a causal spacetime domain
or a BV-BFV boundary condition.

## 2. Gibbs measure, detailed balance and variational coupling

Write `lambda_Delta` for relative 255-dimensional Lebesgue measure. Then

```text
dmu_beta=Z_beta^-1 exp(-beta V) dlambda_Delta.               (4)
```

The probability current for (1) is

```text
J=-rho grad_T V-(1/beta)grad_T rho.
```

For `rho=Z_beta^-1 exp(-beta V)`, `J=0` pointwise, including zero normal
flux at every face. Integration by parts therefore gives

```text
-integral f L_beta g dmu_beta
  =(1/beta) integral <grad_T f,grad_T g> dmu_beta.            (5)
```

Thus `mu_beta` is reversible and stationary. Positivity of its density and
connectedness of the simplex give uniqueness of the stationary law. The
weighted Sobolev closure has Dirichlet form

```text
E_beta(f,g)=(1/beta) integral <grad_T f,grad_T g> dmu_beta.  (6)
```

If `rho_t` is a density relative to `mu_beta`, the Fokker-Planck evolution is
the gradient flow of relative entropy and obeys

```text
d/dt Ent_mu(rho_t)
  =-(1/beta) integral rho_t |grad_T log rho_t|^2 dmu_beta.   (7)
```

Equations (4)--(7) close the measure/noise/boundary/variational denominator
left open by K112 at repository-construction grade. They do not supply a
physical environment, an observed time variable, fluctuation-dissipation data
from GU, or a source-owned stochastic quantization.

## 3. The equivariant basin record

Away from ties, define

```text
R(w)=argmax_i w_i,
C_j={w in Delta : w_j>w_i for every i != j}.                 (8)
```

The tie set is contained in a finite union of codimension-one affine
hyperplanes. It has `lambda_Delta` and hence `mu_beta` measure zero. Equation
(8) is therefore an almost-sure measurable record. It is equivariant:
`R(sigma w)=sigma R(w)`. Since `mu_beta` is invariant and `S_256` acts
transitively on the cells,

```text
mu_beta(C_j)=1/256.                                          (9)
```

The record carries eight classical bits. On `C_j`, the diagonal weight
operator `diag(w)` has unique top eigenspace `R e_j`; its spectral projector is
`P_j=e_j e_j^T`. Consequently the basin label transports exactly to the K110
top-projector quotient and the existing K91 action/domain/Green retract.

This is a mathematical coarse-graining of the continuous state. No detector,
memory medium, readout dynamics or collapse rule has been derived. A sample
path can cross a tie wall, changing `R(W_t)` and hence changing which branch
retract is named.

## 4. Sharp records fail the diffusion's finite-energy domain

The bounded cell indicators `1_{C_j}` belong to `L^2(mu_beta)`, but not to the
weighted `H^1` Dirichlet domain. They jump across the codimension-one walls
`w_i=w_j` where the Gibbs density is smooth and strictly positive. The
distributional derivative therefore has a surface singularity rather than an
`L^2` gradient.

The divergence is already exact on a transverse coordinate `x`. Replace the
step by a linear transition from zero to one across `[-epsilon,epsilon]`. Its
slope is `1/(2 epsilon)`, so with wall density `q(0)>0`,

```text
E_beta(record_epsilon,record_epsilon)
  ~ (q(0)/beta) * 1/(2 epsilon) -> infinity.                 (10)
```

Thus the sharp branch record is measurable but not a finite-energy observable
for the same diffusion generator. The reflected Langevin law does not preserve
one fixed K91 branch domain across wall crossings. A physical record would need
an enlarged hybrid state space, detector hysteresis, absorbing/superselection
structure, degenerate noise at the walls, or another owned mechanism. Each is
a new premise rather than a consequence of (1).

This is the exact domain obstruction that a finite branch Markov model cannot
see: K112's diagonal record can be adjoined algebraically, while the natural
sharp record of the continuous diffusion lies outside its energy domain.

## 5. Zero-noise recovery is singular

K111 proved that `V` has exactly 256 strict interior global minima `w^(j)`, all
related by `S_256`, and that the restricted Hessian at every minimum is

```text
H_j=(2/257^2) I_T.                                          (11)
```

The finite-dimensional Laplace principle applied to (4) therefore gives

```text
mu_beta => (1/256) sum_j delta_{w^(j)}        as beta->infinity,  (12)
mu_beta(. | C_j) => delta_{w^(j)}.                            (13)
```

Equal weights follow both from transitivity and from the equal Hessian
determinants. Equations (12)--(13) recover K112's uniform branch law and exact
conditioned branch only in the singular zero-noise limit.

At every finite `beta`, `mu_beta` is absolutely continuous. Every individual
vacuum therefore has probability zero. The continuous law gives a uniform
basin record and a branchwise top eigenspace, but not an exact sampled K111
vacuum. No preferred coordinate is selected in either the finite-temperature
law or its limit.

## 6. Ownership and exact boundary

K113 supplies a complete continuous finite-dimensional stochastic denominator:
carrier, nonlinear drift, covariance, reflecting boundary, Gibbs measure,
detailed balance, variational dissipation and an equivariant record map. It
also proves why that denominator is not yet a physical branch mechanism. The
sharp record is outside the generator's finite-energy domain, exact vacua have
zero finite-temperature mass, and the perfect finite K112 branch is recovered
only after a singular limit.

No authenticated source/GU action or environment owns (1). No spacetime causal
noise, microlocal domain, nonlinear BV-BFV complex, physical detector, Born
pairing, held-out score, prediction, confirmation, canon or public posture is
constructed or changed.

## Inline postflight bookend

- **Strongest overclaim:** “continuous stochastic dynamics now derives the
  physical K105 branch.” Refused. It derives a symmetric Gibbs diffusion and
  measurable basin label; exact vacua occur only in a singular limit, and the
  label is not a finite-energy generator-domain observable.
- **Strongest contrary route:** degenerate wall noise, absorbing boundaries or
  an enlarged detector variable could make a durable sharp record. Those
  remain valid conditional routes but are new owners and may break detailed
  balance or permutation symmetry.
- **Strongest mistyping risk:** calling Neumann reflection a BV-BFV boundary
  condition or Gibbs weight a Born law. Refused. Both are classical
  finite-dimensional analytic structures.
- **Weakest reproducibility seam:** a simulation would almost surely never land
  exactly on a tie wall or vacuum and could hide both measure-zero facts. The
  certificate instead checks tangent projection, exact vacuum/Hessian data,
  transitive basin labeling and the inverse-epsilon wall-energy divergence.

The standard-library certificate runs a clean baseline before every hostile
mutation. No source/GU stochastic action, physical branch environment,
measurement, collapse, spacetime BV-BFV quotient, Born derivation, held-out
score, prediction, confirmation, canon, paper or public posture moves.

## Reproduction

```bash
python3 tests/channel-swings/k113_k111_continuous_langevin_basin_record_probe.py
python3 tests/channel-swings/k113_k111_continuous_langevin_basin_record_probe.py --selftest
```
