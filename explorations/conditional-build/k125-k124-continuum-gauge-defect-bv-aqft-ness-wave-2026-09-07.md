---
title: "K125 K124 continuum gauge defect BV AQFT NESS boundary wave"
status: active_research
doc_type: reverse_scaffold_continuum_gauge_defect_boundary_result
created: 2026-09-07
date: 2026-09-07
target_claim: INTERNAL_TARGET:K124_CONTINUUM_GAUGE_UNSMEARED_DEFECT_BV_AQFT_NESS_COMPLETION
claim_ceiling: exact repository-owned constant-holonomy fixed-mode squared-symbol and classical weak-Gauss consistency, conditional vectorlike anomaly cancellation, parity and local-gauge obstructions to inheriting a fixed-smearing BV/BFV or even-local-net owner, plus a theorem that K123's linear uniformly bounded CAR mollifier route cannot retain nonzero delta strength; no universal point-defect no-go, continuum operator/domain theorem, interacting net or NESS, source/GU ownership, Born derivation, prediction, confirmation or holdout credit follows
manifest: lab/process/k125-k124-continuum-gauge-defect-bv-aqft-ness-wave.json
probe: tests/channel-swings/k125_k124_continuum_gauge_defect_bv_aqft_ness_probe.py
---

# K125 K124 continuum gauge/defect/BV/AQFT/NESS boundary wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: staged continuum descent of the K124 gauge regulator and exact obstruction to a nonzero uniformly bounded CAR delta defect
carrier: nine-state impurity tensor CAR Fock space of 18 full left-right Dirac species tensor U(1)^8 connection-electric sector on the spatial circle LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: Hilbert adjoint and CAR L2 pairing plus electric L2 pairing; no defect BV field-antifield pairing is owned ON=repository_owned_fixed_mode_control
real_structure: real u(1)^8 gauge fields, Hermitian adjoint, complex Dirac conjugation and integer charge lattice
grading: fermion parity plus BRST ghost number and BV antifield degree
action_owner: repository-construction
target: constant-holonomy fixed-mode gauge and classical weak-Gauss consistency, fixed-smearing parity/local-gauge owner obstruction, bounded point-unsmearing discriminator and interacting-NESS release gate MAP-TYPE=not-a-map
```

Scope: this packet binds one repository-selected continuum-circle completion of
K124's gauge sector and one exact limit test for K123's bounded CAR defect. It
does not bind Weinstein's action, a GU-native gauge group, a renormalized point
interaction, nature's state/effect rule, or an empirical observable.

## Inline preflight bookend

The maximum-depth frontier rebuild admitted five arcs. The ultraviolet
point-defect scaling test is the route-changing discriminator. The smooth
gauge/Gauss prefix and the tests for a fixed-smearing classical BV owner and
fixed-width causal-defect construction are independent. A point-coupled common domain is
released only if the ultraviolet test supplies a nontrivial limit; an
interacting NESS is released only if the fixed-width theory supplies the
required reservoir correlation or scattering theorem. A source/GU action
owner remains outside this construction because the current action-causal
registry contains no complete candidate.

Mechanism retrieval separated this packet from K77's Maxwell and closed-range
controls, K89's cylindrical BFV model, K104's action/BV/Green construction,
K118's free continuum BV-BFV host, K120's Fock rigging, K122's free CAR net,
K123's compactly smeared bounded defect and K124's finite gauge regulator. It
also distinguishes this result from the unrelated August I1B packet already
named K125. No canonical correction changes the K124 charge, cycle, affinity,
or source-owner typing used here.

The route-changing lens census included Fourier and numerical analysis,
lattice gauge theory, constrained Hamiltonian systems, vector gauge anomalies,
CAR operator theory, self-adjoint extension theory, BRST/BFV and BV-BFV,
defect AQFT, constructive QFT, open-system scattering, NESS theory, graph
cohomology, stochastic thermodynamics, source fidelity, representation typing
and hostile philosophy of science. It chose a staged structural descent over
a monolithic point-theory assertion. Computation certifies the finite algebra
and quantitative bounds below; it does not replace the analytic theorem.

## 1. Smooth gauge sector: fixed-mode quadratic-form consistency

Put the spatial circle at length one, take `N` sites and lattice spacing
`a=1/N`. For one of the eight Abelian factors, gauge-fix a smooth flat
connection to constant holonomy angle `theta` and put

```text
U_j = exp(-i theta/N).
```

On the sampled Fourier mode `psi_k(j)=exp(2 pi i k j/N)`, the covariant
forward difference has symbol

```text
d_N(k,theta) = N (exp(i(2 pi k-theta)/N)-1).
```

Writing `p_k=2 pi k-theta`, its squared modulus satisfies, throughout the
certified low-mode range,

```text
0 <= p_k^2 - |d_N(k,theta)|^2
   = p_k^2 - 4 N^2 sin^2(p_k/(2N))
  <= p_k^4/(12 N^2).
```

Thus the squared symbol converges at fixed mode to the continuum constant-
connection quadratic form. The certificate checks modes `-2,...,2` at
`N=16,32,64,128`, the bound, monotone convergence and exact lattice gauge
covariance up to floating representation error. No isometric lattice-to-
continuum embedding, direct first-order symbol bound, graph-norm core theorem,
or interacting norm-resolvent theorem is supplied.

For a lattice gauge transformation `psi_j -> g_j psi_j` and
`U_j -> g_j U_j g_(j+1)^-1`, the difference transforms as
`d_U psi -> g d_U psi`. The periodic product is exactly

```text
product_j U_j = exp(-i theta),
```

so the eight Wilson holonomies survive refinement. Continuum passage does not
select their sector.

## 2. Classical weak Gauss identity, neutrality and anomaly check

For periodic link electric fields, lattice summation by parts is exact:

```text
sum_j phi_j (E_j-E_(j-1))
  = -sum_j E_j (phi_(j+1)-phi_j).
```

After restoring the factors of `a`, the formal smooth-limit identity is

```text
<phi, partial_x E-rho> = -<partial_x phi,E>-<phi,rho>.
```

The constant test function retains K124's global-neutrality condition. This is
a classical weak-identity consistency check only: no continuum gauge Hilbert
space, dense invariant operator core, or common self-adjoint Gauss domain is
constructed, either freely or after point coupling.

Conditional on K124's declaration that each of the 18 reservoirs is a full
left/right Dirac species with identical left/right charge vector `q_e`, every
entry of the Abelian anomaly matrix cancels:

```text
sum_e (q_e,L,a q_e,L,b - q_e,R,a q_e,R,b) = 0.
```

The certificate evaluates the full `8 x 8` matrix. This removes one anomaly
obstruction under the stated vectorlike-charge hypothesis; it does not derive
that hypothesis or identify the graph-derived `U(1)^8` with a source-native
GU gauge group.

## 3. Fixed-smearing BV-BFV owner is obstructed

For `epsilon>0`, a charged smeared field transforms with `g(x)` across the
support of `f_epsilon`, while K123's impurity transition transforms only with
`g(0)`. Charge cancellation at a point therefore does not make the finite-
width monomial locally gauge invariant. It needs a Wilson line from the
impurity to `x` (and a declared path convention).

There is a second independent obstruction. K123's impurity transitions are
ordinary matrices on `C^9`; multiplying one by a single CAR creation or
annihilation operator is Grassmann odd. It cannot be a term in a bosonic
classical action without an additional typed odd impurity/Klein carrier. Nor
can every transition of the K115 rook graph be declared odd: the graph has
triangles, so a consistent vertex `Z_2` grading is impossible.

Consequently K125 owns no defect action, antifield functional, classical
master equation, or boundary BFV charge. Nilpotence of the free Abelian BRST
differential and global charge neutrality are necessary controls, not a BV
construction. A successor must add Wilson-line dressing and a parity-complete
carrier, then write and verify `S`, `S_BV`, its boundary variation, and the
master identity explicitly.

## 4. Fixed-width even-local-net owner is obstructed

K123 does supply a bounded self-adjoint global perturbation and hence a norm-
continuous global `C*` dynamics at fixed width. It does not supply an even
perturbation: every displayed transition term contains one CAR operator and
an ungraded impurity matrix. Therefore the perturbation need not preserve the
even observable subnet. A Dyson automorphism preserves abstract inclusions
and commutators, but that fact does not establish the claimed local interacting
net when the observable subnet itself is not invariant.

Thus no fixed-width even-local-net, causal-hull locality, or defect-time
covariance theorem is owned here. A parity/Klein-factor completion might
reopen it, but must be typed and shown compatible with the nine-state
transition reduction. A Wilson-dressed, parity-completed construction may
also evade the local-gauge obstruction above.

## 5. The bounded point-unsmearing route fails nontrivially

The exact discriminator is already visible on one transition. On the circle,
take the delta-normalized box mollifier

```text
f_epsilon(x) = epsilon^-1 1_[0,epsilon](x).
```

It has `||f_epsilon||_1=1` and
`||f_epsilon||_2=epsilon^-1/2`. In a CAR representation,
`||a(f)||=||f||_2`. On the two-dimensional impurity/one-particle subspace, the
self-adjoint transition block

```text
V_epsilon = g_epsilon (X tensor a*(f_epsilon)
                        + X* tensor a(f_epsilon))
```

has norm `|g_epsilon| ||f_epsilon||_2`. Therefore:

1. if `g_epsilon -> g != 0`, the defect norm diverges like
   `epsilon^-1/2`;
2. if the family is uniformly bounded, then
   `g_epsilon=O(sqrt(epsilon))`; and
3. for every smooth test function `h`,
   `g_epsilon integral(f_epsilon h) -> 0`.

So K123's bounded-perturbation proof cannot simultaneously keep uniform norm
control and nonzero delta strength. The result is deliberately narrower than
a point-interaction no-go: a boundary condition, interior-boundary condition,
counterterm, quadratic-form limit or norm/strong-resolvent renormalization may
still succeed, but it must supply a new common Gauss domain and cannot inherit
K123's boundedness argument unchanged.

## 6. The interacting NESS gate does not release

The fixed-width bounded dynamics does not by itself supply the decay, Moller
morphism, asymptotic completeness, convergence, uniqueness or reservoir
normality needed to characterize a Ruelle NESS or identify a Cesaro cluster
state's physical current. Weak-* compactness can supply averaging subnet
limits in the abstract state space; it does not identify their physical
sector or yield a nonzero current. K115's
reduced stationary law and exact cycle ratio `6561/256` remain inherited, but
they are not promoted to an interacting field-current theorem.

The NESS successor therefore remains exact: first construct a renormalized
gauge-covariant point defect (or retain a declared finite width), then prove
reservoir correlation/scattering control and the stationary state's current.

## Inline postflight bookend

All five admitted arcs were attempted. Constant-holonomy fixed-mode squared-
symbol consistency, classical weak Gauss identity, and the conditional
vectorlike anomaly matrix completed. The fixed-smearing BV-BFV and even-local-
net arcs instead exposed missing local Wilson dressing and a missing parity
owner. The ultraviolet discriminator returned negative for the inherited
linear bounded route and switched the point-coupled domain successor to a
renormalized extension problem. The NESS arc reached but did not pass its
declared scattering/correlation release condition, so no interacting state or
current was minted.

- **Strongest overclaim caught:** global charge neutrality was insufficient
  for local gauge invariance, and K123's odd perturbation could not support an
  even-local-net conclusion.
- **Strongest contrary route:** Wilson dressing plus a parity/Klein completion,
  or singular extension/resolvent methods, may evade the recorded failures.
- **Weakest reproducibility seam repaired:** the certificate now computes the
  full anomaly matrix and tests explicit obstruction facts; it no longer
  encodes BV, locality, or common-domain assertions as hard-coded booleans.

The eight gauge charges, eight spatial holonomies, ten transition cycles and
real modular affinity remain distinct. No source action, physical state,
detector effect, Born rule, held-out result, prediction, confirmation, canon,
paper, release or public-posture status changes.

## Next condition

First supply a Wilson-dressed, parity-complete defect action and explicit BV-
BFV functional, or a gauge-covariant boundary-condition, interior-boundary-
condition, counterterm or norm/strong-resolvent renormalized point defect on a
common self-adjoint Gauss domain. Then prove its interacting causal net, reservoir
correlation/scattering limit and nonequilibrium stationary state. Separately
require an actual source/GU action to select the charge embedding,
coefficients and boundary sector.

## Reproduction

```bash
python3 tests/channel-swings/k125_k124_continuum_gauge_defect_bv_aqft_ness_probe.py
python3 tests/channel-swings/k125_k124_continuum_gauge_defect_bv_aqft_ness_probe.py --selftest
```
