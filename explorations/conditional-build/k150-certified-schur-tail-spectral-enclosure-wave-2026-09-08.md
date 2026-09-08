---
title: "K150 certified Schur-tail spectral enclosure wave"
status: active_research
doc_type: conditional_exact_rational_ritz_inertia_block_tail_projection_gram_and_threshold_certificate_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned rational certificate kernel and block-operator theorem only; exact inertia isolates finite conforming Ritz values, an independently proved complement floor and coupling norm produce rigorous full-operator Schur lower enclosures, and certified residual/gap inputs propagate to projection, complete Gram, first-threshold and rank decisions; the solver does not assemble the native K148 singular-IBC matrix or tail constants and emits no native numerical spectrum, full-Fock Mourre/scattering, physical/source, Born, prediction or confirmation claim
manifest: lab/process/k150-certified-schur-tail-spectral-enclosure-wave.json
solver: tests/channel-swings/k150_certified_schur_tail_solver.py
probe: tests/channel-swings/k150_certified_schur_tail_spectral_enclosure_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K150 certified Schur-tail spectral enclosure wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet implements the exact certificate kernel demanded by K149.
It accepts a finite conforming Ritz matrix together with independently proved
tail, residual and gap bounds. It does not assemble those inputs for K148's
native two-edge singular IBC operator. Its built-in finite matrix is a positive
control only and is not a truncated native Hamiltonian.

```gu-typed-objects
result: exact rational finite-Ritz inertia and bisection, complement-tail Schur lower enclosure, residual-to-projection and projection-to-complete-Gram error transport, and finite first-threshold/rank stopping decisions
carrier: an abstract orthogonal block decomposition P H direct-sum (1-P) H of one fixed native charge-sector operator, with finite conforming Ritz block A and separately certified complement data; the built-in 2 by 2 fixture is non-native LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert pairing for the self-adjoint block operator and exact rational Euclidean pairing for serialized finite matrices ON=repository_signed_point_control
real_structure: exact rational symmetric matrices are real controls; any K148 particle-hole or flavor symmetry may reduce work only after a unitary charge-intertwining identity is independently proved
grading: ordered eigenvalue index, native conserved charge, finite Ritz dimension, complement cut, residual cluster multiplicity and endpoint-channel label
action_owner: repository-construction -- the certificate algorithm, fixture and every eventual operator input remain unselected by Weinstein's source or a GU action
target: fail-closed exact certificate from finite conforming data plus proved singular-tail bounds to full-operator energy, projection, threshold and rank enclosures MAP-TYPE=intertwiner
```

## Inline preflight bookend

K149 proved convergence and finite stopping rules but left their trusted
computational core implicit. The immediate question is not whether a floating-
point truncation looks converged. It is which small exact certificate, supplied
with operator-specific tail facts, would make the lower endpoint and every
later threshold/rank decision logically valid.

Object retrieval found K139's singular boundary chart, K143's HVZ threshold
form, K148's native hard-core operator and K149's penalty--Ritz theorem. It
found no serialized finite charge-sector IBC basis, exact transformed matrix,
complement floor, off-diagonal tail norm, subspace residual or charge-symmetry
intertwiner. Those absences are input obligations, not values the solver may
guess.

The route census compared floating-point diagonalization, interval eigensolvers,
exact characteristic polynomials, Sturm/inertia methods, Temple bounds,
Lehmann--Goerisch bounds, Feshbach--Schur complements, verified residual bounds,
and symmetry reduction. Exact congruence inertia plus a scalar Schur tail bound
was selected: it has a short auditable core, supports multiplicity, and exposes
the missing native data. A form-level Lehmann--Goerisch method remains the
fallback if K139's chart yields certified quadratic-form data but no bounded
off-diagonal block.

## 1. Exact finite spectral isolation

Let `A=P H P` be the matrix of the native form on a finite-dimensional
conforming subspace of one fixed charge sector. All serialized entries are
rationals or outward rational intervals resolved to a rational symmetric
bound matrix before this kernel is called.

For rational `x`, Sylvester inertia of `A-xI` gives exactly

```text
n_-(A-xI)=#{j: a_j<x},    n_0(A-xI)=#{j: a_j=x}.       (1)
```

The implementation computes inertia by exact symmetric congruence, using
one-dimensional pivots when a diagonal entry is nonzero and a two-dimensional
`[[0,b],[b,0]]` pivot when every remaining diagonal vanishes. Congruence
preserves inertia. Rational bisection therefore returns `[a_k^-,a_k^+]`
containing the requested ordered Ritz value without a floating-point sign
decision. Repeated eigenvalues are retained through the exact zero count.

This is a certificate for `A`, not yet for `H`.

## 2. A full-operator lower enclosure from a proved tail

Write the full self-adjoint operator in the orthogonal decomposition as

```text
H = [ A  B* ],      D >= d,      ||B||^2 <= beta^2.    (2)
    [ B  D  ]
```

The inequalities in (2) are operator-specific proof inputs. For any
`epsilon>0`, the weighted Cauchy inequality gives

```text
H >= diag(A-epsilon, d-beta^2/epsilon).                (3)
```

Set `a=a_k^-` and choose the positive root satisfying

```text
d-beta^2/epsilon = a-epsilon,
epsilon = [sqrt((d-a)^2+4 beta^2)-(d-a)]/2.            (4)
```

Then the min--max principle applied to (3), together with
`a_k(A)>=a`, gives

```text
[a+d-sqrt((d-a)^2+4 beta^2)]/2
    <= lambda_k(H) <= a_k^+.                           (5)
```

The upper side is ordinary conforming Rayleigh--Ritz. The lower side is a
statement about the complete block operator. The code encloses the square
root outward by integer arithmetic on a dyadic rational grid, so its reported
lower endpoint rounds down rigorously. It fails closed unless `a_k^+<d`.

Equation (5) is useful for K149's finite-penalty operator only after a native
assembly proves (2) in its actual transformed charge sector. A truncated
finite-`U` eigenvalue alone is not a lower bound and is never accepted as one.

## 3. Cluster projection and complete Gram propagation

Suppose exact inertia and neighboring enclosures certify the cluster count,
and let `delta>0` be a proved separation from the approximate cluster to the
rest of the full spectrum. If the conforming approximate spectral subspace has
operator residual at most `r<delta`, the standard sin-theta residual estimate
gives, after equal-rank polar alignment,

```text
||P_approx-P_cluster|| <= eta_P := r/delta.            (6)
```

The solver rejects `r>=delta`. For `m` compatible endpoint channels with
`||C_alpha||<=c`, K149's complete residual Gram operator then obeys

```text
||G_approx-G|| <= eta_G := 2 m c^2 eta_P.              (7)
```

All degenerate off-diagonal blocks must be present in `G_approx`. A one-state
diagonal block cannot certify a degenerate cluster.

For candidate residual intervals `[l_a,u_a]`, the common escape mass cancels
from ordering. Candidate `a` is uniquely first exactly when the supplied
intervals establish

```text
u_a < min_(b!=a) l_b.                                  (8)
```

Exact inertia of `G_approx-eta_G I` decides how many approximate Gram
eigenvalues clear the perturbation margin. Full rank requires all of them to
clear it. Exact deficient rank `d-z` additionally requires a proved structural
kernel of dimension `z`; the engine checks that exactly `z` approximate
eigenvalues lie below the error margin and rejects numerical smallness as a
kernel proof.

## 4. Native input contract and symmetry boundary

A K148 charge-sector certificate must serialize all of the following before
this engine can emit a native interval:

1. an exact conforming charge-sector Ritz matrix;
2. a proved complement floor `D>=d` below the relevant K143 HVZ edge;
3. a proved bound `||B||^2<=beta^2` for the actual transformed off-diagonal
   block;
4. exact cluster counts, neighboring enclosures, a true exterior gap and a
   certified subspace residual;
5. the complete residual Gram matrix, including degenerate off-diagonal
   entries; and
6. a structural kernel identity for any deficient exact rank.

Flavor exchange or particle--hole symmetry may reduce the ground-carrying
charge census only after an explicit unitary is proved to intertwine the
native charge restrictions, forms, conforming spaces and endpoint operators.
The phrase “symmetry-related” is not a certificate and the engine performs no
implicit orbit quotient.

The executable positive control uses

```text
A=[-1  1/4],   d=3,   beta^2=1/16.                    (9)
  [1/4 1/2]
```

It isolates the first Ritz value, produces a strict Schur-corrected lower
endpoint, propagates `eta_P=1/50` to `eta_G=4/25`, certifies one disjoint first
threshold interval and certifies rank four for a diagonal positive Gram
fixture. These numbers test the engine only; none is a K148 energy or form
factor.

## Inline postflight bookend

- **Strongest advance:** K149's lower-bound requirement is now executable as
  a fail-closed exact rational certificate, including zero-diagonal inertia
  pivots and outward irrational rounding.
- **Strongest propagation advance:** the same kernel carries certified
  residual/gap data through projection error to the complete Gram, threshold
  order and exact-rank decision.
- **Strongest contrary route:** a form-level Lehmann--Goerisch method may fit
  K139's singular chart better if no bounded `B` exists after transformation;
  that is the named switch condition.
- **Strongest overclaim:** presenting the positive-control output as the native
  residual spectrum. Refused: the native assembly fields are deliberately
  absent and `native_ibc_inputs_assembled_by_solver=false` is emitted.
- **Weakest reproducibility seam:** the complement floor and coupling norm are
  as strong as their operator-specific proof. An underestimated `beta` or an
  unproved `d` invalidates the lower endpoint even though all arithmetic passes.

The four admitted arcs share the same exact matrix/tail contract and public
state surfaces, so they were executed inline. Hostile controls mutate symmetry,
matrix exactness, separation, tail sign, gap closure, threshold order, Gram
margin, structural kernel and every scientific fence.

## Next condition

Assemble K139's transformed equal-coupling two-edge operator in the two native
ground-charge orbit representatives. Serialize an exact finite conforming
basis and matrix, prove a complement floor and off-diagonal coupling bound,
and certify the unitary charge symmetries. Feed those inputs to this solver;
then refine until the residual threshold intervals and complete Gram margins
close. If the transformed off-diagonal block is not bounded, switch to a
form-level Lehmann--Goerisch certificate rather than weakening (2). Only after
native margins close may strict full-Fock Mourre constants be tested.

## Reproduction

```bash
python3 tests/channel-swings/k150_certified_schur_tail_solver.py --demo
python3 tests/channel-swings/k150_certified_schur_tail_spectral_enclosure_probe.py
python3 tests/channel-swings/k150_certified_schur_tail_spectral_enclosure_probe.py --selftest
```
