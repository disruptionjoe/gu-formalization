---
title: "K152 form-dual residual lower-enclosure wave"
status: active_research
doc_type: conditional_native_hard_core_transformed_form_pencil_dual_residual_ground_enclosure_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned form-level certificate theorem and rational kernel for the equal-coupling two-edge native hard-core signed point control: a positive-definite generalized conforming form pencil is isolated by exact inertia, and a proved coercive shift, shifted form-dual residual, and lower bound on the next distinct spectrum give an outward-certified native ground interval and ground-eigenspace projection error without any raw point-field Hilbert coupling norm; the certificate is basis covariant and charge transport requires the complete signed flavor-unitary form/residual/gap intertwiner; K139--K151 do not yet serialize the operator-specific q=(0,0) or q=(1,0) transformed-domain matrices, dual residual, or exterior gap, so no numerical native residual spectrum, complete threshold/Gram closure, full-Fock scattering, NESS/current, physical/source selection, Born derivation, prediction or confirmation follows
manifest: lab/process/k152-form-dual-residual-lower-enclosure-wave.json
probe: tests/channel-swings/k152_form_dual_residual_lower_enclosure_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K152 form-dual residual lower-enclosure wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet stays on K148--K151's equal-coupling two-edge native
hard-core corner, positive particle/hole polarization, diagonal `W=0`,
`m=kappa=|q|=1`, positive self energy `1/4` and threshold mass `tau=5/4`.
It replaces the raw-block Schur interface rejected by K151 with a quadratic-
form certificate that is compatible with K139's transformed common domain.
It does not claim that the required native form data have already been
serialized.

```gu-typed-objects
result: a symmetric-definite conforming form pencil plus a coercive shifted dual residual and next-distinct-spectrum gap gives an exact/outward-certified ground interval and ground-eigenspace projection error without a bounded raw point-field coupling block
carrier: each fixed q=(q1,q2) block of K139's transformed common boundary domain for the native C3 hard-core impurity tensor positive particle/hole Fock carrier; a finite positive-control pencil is separately typed and non-native LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: native Hilbert Gram M_ij=<psi_i,psi_j>, closed form matrix A_ij=a(psi_i,psi_j), and shifted form-dual norm induced by H+s; all three must refer to the same conforming trial vector ON=repository_signed_point_control
real_structure: exact rational real-symmetric control; signed flavor exchange may transport q=(1,0) to q=(0,1) only when it intertwines Hilbert pairing, form, trial space, residual functional and exterior gap
grading: exact conserved charges q_i=n_i+N_i+-N_i-, native constraint n1*n2=0, generalized Ritz index and ground-cluster/exterior spectral split
action_owner: repository-construction -- graph, extension, polarization, couplings, subtraction, form core, shift, state and exterior-gap proof are not selected by Weinstein's source or a GU action
target: form-level native ground enclosure and projection input suitable for K149 threshold/complete-Gram propagation MAP-TYPE=intertwiner
```

## Inline preflight bookend

K151 proves that the bare point tail is not Hilbert bounded uniformly in the
cutoff. That invalidates K150's `||B||^2<=beta^2` input for this singular IBC
operator, not the native operator or K149's form convergence. The next
question is whether K139's transformed form domain admits a lower certificate
whose residual is measured after one resolvent weight.

Object-level retrieval found K139's bounded inverse
`U_s^-1` and common domain `U_s^-1 Dom(H0)`, K149's monotone penalty--Ritz
squeeze, K150's exact inertia and outward arithmetic, and K151's finite charge
blocks and signed flavor unitary. It found no serialized native
`(A_q,M_q)`, no complete shifted dual residual, and no lower bound on the next
distinct native charge-sector spectral value. The later K151 custody Run
confirms that this absence is current rather than a stale status pointer.

The route census compared raw Schur blocks, Lehmann--Goerisch complement
matrices, generalized Rayleigh--Ritz, Kato--Temple residuals, shifted form-dual
norms, penalty-form bounds, basis congruence, spectral-measure estimates and
charge-orbit transport. The shifted dual-residual route is selected because
it uses exactly the one-resolvent regularity K139 owns and never reconstructs
the divergent bare tail.

## 1. Exact generalized Ritz isolation on a conforming form core

Fix one native charge sector and a finite family

```text
psi_1,...,psi_N in Dom(a_q)=U_s^-1 Dom(H0,q).          (1)
```

Define

```text
A_ij=a_q(psi_i,psi_j),       M_ij=<psi_i,psi_j>.       (2)
```

The basis is conforming because (1) is an operator-domain statement, not because a bare cutoff has finitely many modes.
`M` must be positive definite.
For rational `x`, the symmetric-definite pencil obeys

```text
n_-(A-xM)=#{j: rho_j<x},    n_0(A-xM)=#{j: rho_j=x}.  (3)
```

Exact congruence inertia and rational bisection therefore isolate every
generalized Ritz value without floating-point eigensigns. Under an invertible
basis change `psi'=psi T`,

```text
(A,M) -> (T* A T,T* M T),                             (4)
```

so (3), the Rayleigh quotient and every certificate below are basis
covariant. The first generalized Ritz value is an upper bound on the native
ground energy. It is not a lower bound.

## 2. A shifted form-dual ground lower enclosure

Let `H=H_q` be the self-adjoint operator associated with the closed native
form. Supply an operator-specific shift and coercivity proof

```text
H+s >= c>0.                                            (5)
```

For a normalized conforming trial vector `u`, set

```text
rho=a_q[u],
epsilon^2=||(H+s)^(-1/2)(H-rho)u||^2.                 (6)
```

Equation (6) is a form-dual residual. The distributional expression
`(H-rho)u` is interpreted as a continuous functional on the shifted form
domain; it need not be a Hilbert vector. This is the exact point at which the
K151 raw-tail obstruction is avoided.

Assume the spectrum outside the ground eigenspace lies in `[b,infinity)` with
`b>rho`. Put

```text
g=b-rho,        E=(rho+s)epsilon^2,
Delta=[E+sqrt(E^2+4g^2 E)]/(2g).                      (7)
```

Then

```text
rho-Delta <= lambda_0(H) <= rho.                      (8)
```

Proof: let `mu` be the spectral measure of `u`, let `p` be its mass on the
ground eigenspace, and put `delta=rho-lambda_0`. The zero first moment gives

```text
p delta = integral_[b,infinity) (x-rho) dmu(x)
        >= g(1-p),
p >= g/(g+delta).                                      (9)
```

The ground part of the dual residual and
`lambda_0+s<=rho+s` give

```text
epsilon^2 >= p delta^2/(lambda_0+s)
          >= g delta^2/[(rho+s)(g+delta)].             (10)
```

Thus `g delta^2-E delta-Eg<=0`; its positive root is (7). The implementation
rounds the square root upward on a dyadic grid, so the reported lower endpoint
rounds downward. No raw point-field Hilbert norm occurs in (5)--(10).

## 3. Ground-eigenspace projection transport

For `x>=b`, the function

```text
(x-rho)^2/(x+s)                                        (11)
```

is increasing because both `x+s` and `rho+s` are positive. The exterior
part of (6) therefore gives

```text
1-p <= epsilon^2 (b+s)/(b-rho)^2.                     (12)
```

Consequently the normalized trial line has distance at most

```text
eta_P=sqrt(epsilon^2 (b+s)/(b-rho)^2)                  (13)
```

from the exact ground eigenspace. The executable uses an outward upper square
root and fails closed when `eta_P>=1`. Equation (13) can feed K149's bounded
endpoint-form estimates for a simple ground state. If the ground eigenspace is
degenerate, one vector does not recover the complete cluster projector or its
off-diagonal Gram blocks; an equal-rank conforming cluster basis and its full
residual matrix are still required.

## 4. Exact charge-orbit transport is a five-part certificate

K151's signed flavor map sends `q=(1,0)` to `q=(0,1)`. To transport a K152
native certificate, the unitary `S` must prove all of

```text
<Spsi,Sphi>_(0,1)=<psi,phi>_(1,0),
a_(0,1)(Spsi,Sphi)=a_(1,0)(psi,phi),
S V_(1,0)=V_(0,1),
r_(0,1)(Spsi)=r_(1,0)(psi),
b_(0,1)=b_(1,0).                                      (14)
```

The first two equalities are checked exactly on serialized pencils. The last
three are operator-specific proof inputs. A verbal equal-coupling claim is not
a certificate, and K151 already rules out using particle--hole complement on
the native C3 carrier.

## 5. Executable positive control and native input audit

The exact fixture uses

```text
A=diag(-1,2), M=I, v=(1,1/4), s=2, c=1, b=2.          (15)
```

It has

```text
rho=-14/17,
epsilon^2=720/4913,
lambda_0=-1.                                           (16)
```

The kernel isolates the exact generalized Ritz ground `-1`, returns an
outward interval containing `-1`, and bounds the trial-line distance to the
ground eigenspace. A nonorthogonal rational congruence produces the same
values exactly. This is a certificate-engine positive control, not K139 data.

The native audit is fail-closed. K139 proves existence of the transformed
common domain and the norm-resolvent limit; K151 proves exact bare finite-
regulator charge blocks and a signed flavor intertwiner. Neither artifact
serializes the complete continuum Gram/form tails of
`U_s^-1 V_N`, a full-form dual residual bound, or a lower bound on the next
distinct spectrum for `q=(0,0)` and `q=(1,0)`. Therefore K152 emits no native numerical interval.
Supplying `claim_native=true` without explicit references
for every one of those proofs is rejected.

## Inline postflight bookend

- **Strongest advance:** K151's required route switch is now an executable
  exact form certificate; the lower endpoint consumes a shifted dual residual
  instead of a bounded raw off-diagonal block.
- **Strongest spectral advance:** the same inputs give a rigorous distance
  from a conforming trial line to the native ground eigenspace, which is the
  first K149 projection interface available at form level.
- **Strongest covariance advance:** nonorthogonal form cores are handled by a
  symmetric-definite pencil, and charge transport is admitted only through the
  complete five-part signed unitary certificate (14).
- **Strongest contrary route:** a block Lehmann--Goerisch method may give
  sharper multi-eigenvalue enclosures once a full residual matrix is
  serialized. It is not needed for the one-vector ground theorem and is not
  claimed here.
- **Strongest overclaim:** presenting (15) or K151's bare finite matrices as
  native residual energies. Refused: neither carries the K139 transformed
  domain, continuum form tails, dual residual or exterior gap.
- **Weakest reproducibility seam:** the next-distinct-spectrum floor `b` is an
  operator-specific proof input. An essential-edge bound alone is insufficient
  if an unaccounted excited eigenvalue lies below it.

The five admitted arcs share the exact form-pair schema, spectral-measure
inequality and charge-transport contract, so they executed inline. No
independent source or specialist tool context justified a second writer.

## Next condition

Construct explicit conforming vectors `psi_i=U_s^-1 phi_i` in K139's native
`q=(0,0)` and `q=(1,0)` transformed domains. Serialize outward-certified
`A_q` and `M_q`, including every infinite resolvent-dressed tail; prove (5), a
next-distinct-spectrum floor `b_q`, and the complete form-dual residual (6).
Feed those inputs to K152 and transport `q=(0,1)` only through (14). Then build
an equal-rank cluster residual matrix before using K149's complete Gram and
threshold machinery. Do not seek another raw cutoff-uniform coupling norm.

## Reproduction

```bash
python3 tests/channel-swings/k152_form_dual_residual_enclosure_solver.py --demo
python3 tests/channel-swings/k152_form_dual_residual_lower_enclosure_probe.py
python3 tests/channel-swings/k152_form_dual_residual_lower_enclosure_probe.py --selftest
```
