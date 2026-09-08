---
title: "K148 hard-core infinite-U Feshbach, ground, and threshold wave"
status: active_research
doc_type: conditional_native_shared_corner_infinite_u_form_ground_energy_hvz_threshold_and_residual_rank_result
created: 2026-09-08
date: 2026-09-08
claim_ceiling: exact repository-owned theorem for the equal-coupling two-edge shared-vertex signed point control that its native three-state operator is the monotone infinite-U form limit of the two-flavor K146 quadratic parent, that the native vacuum/leaf Feshbach map is an operator-valued bath-Fock problem rather than K147's finite Schur matrix, that its global ground energy lies strictly above the unconstrained two-flavor value and at or below the one-flavor value and is an isolated native eigenvalue, and that every charge-resolved first HVZ threshold and one-residual signed endpoint rank is determined by actual residual bound energies and the residual impurity density; no complete charge-sector point spectrum, closed-form native ground energy, uniform full-Fock Mourre/scattering, NESS/current, physical selector, source/GU action, Born derivation, prediction or confirmation follows
manifest: lab/process/k148-hard-core-infinite-u-feshbach-ground-threshold-wave.json
probe: tests/channel-swings/k148_hard_core_infinite_u_feshbach_ground_threshold_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K148 hard-core infinite-U Feshbach, ground, and threshold wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet fixes K147's native shared corner with vertices `0,1,2`,
edges `(0,1),(0,2)`, equal real particle/hole couplings, diagonal `W=0`, and
K146's `m=kappa=|q|=1`, positive self energy `1/4` and zero subtraction. The
two-flavor exterior impurity is introduced only as an auxiliary quadratic
parent. The physical control remains its no-double-impurity-occupancy form
limit on the native three-state carrier.

```gu-typed-objects
result: the native shared corner is the infinite-U form restriction of the two-flavor K146 quadratic parent, with a strict ground-energy lift, an isolated native ground, an operator-valued charge-sector Feshbach problem, exact residual-energy first thresholds and a residual-density endpoint-rank theorem
carrier: native span{|0>,|1>,|2>} tensor positive particle/hole Fock, embedded as the no-double-occupancy subspace of the auxiliary two-impurity-mode exterior carrier C4 tensor Fock LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive impurity and antisymmetric Fock Hilbert pairing; closed semibounded quadratic forms and their monotone infinite-U restriction ON=repository_signed_point_control
real_structure: K146 particle-hole conjugation acts flavorwise on the auxiliary quadratic parent, but the no-double-occupancy projection is not a reducing quasifree polarization and no global sea flip is used
grading: two conserved incidence-charge coordinates q_i=n_i+N_(i,+)-N_(i,-), combined Klein-CAR parity, and auxiliary impurity occupation with native constraint n_1 n_2=0
action_owner: repository-construction -- graph, positive polarization, point operator, couplings, subtraction, W, screening, domain, charge sector and state are not selected by Weinstein's source or a GU action
target: native infinite-U form construction, vacuum-leaf Feshbach type, global ground bracket/existence, charge-resolved first thresholds and residual-density signed endpoint ranks MAP-TYPE=intertwiner
```

## Inline preflight bookend

K147 proves that the two native Hubbard transitions are not two CAR modes.
The nearest honest parent nevertheless exists: add the missing doubly occupied
impurity state, obtain two genuine K146 modes, and penalize precisely that one
state. The key question is what survives as the penalty tends to infinity,
not whether the projected one-excitation Schur matrix can be enlarged.

Mechanism retrieval found K139's signed IBC operator, K143's many-body HVZ
formula, K145's affine incidence charge, K146's one-flavor quasifree ground
doublet and K147's shared-vertex algebra. It found no infinite-`U` form limit,
native ground bracket, specialized first-threshold list or state-dependent
native endpoint rank theorem. No correction-registry entry supersedes these
inputs.

The route census covered Hubbard operators, infinite-`U` Anderson models,
monotone form convergence, compression versus reduction, Schur--Feshbach
maps, min--max and ground-space angle estimates, quasifree covariance,
massive HVZ localization, residual density matrices, Pauli availability,
flavor symmetry, Mourre prerequisites and source ownership. The selected
route uses the quadratic parent for construction and comparison only. A
finite matrix is a control witness, not the infinite-volume proof.

## 1. The native corner is an infinite-U form limit

Let `d_1,d_2` be genuine impurity CAR modes on
`Lambda(C2)=span{|0>,|1>,|2>,|12>}` and set

```text
Q_12=n_1 n_2=|12><12|,       P=1-Q_12.                (1)
```

On the range of `P`, the compressed creators are exactly the native Hubbard
transitions (including the already fixed Klein signs):

```text
P d_i* P=|i><0| tensor kappa_i=B_i,
P d_i P=B_i*.                                          (2)
```

Let `H_qf=H^(1)+H^(2)` be the two-flavor sum of K146's renormalized quadratic
IBC control on the same positive particle/hole representation. If `h_qf` is
its closed semibounded form, define

```text
h_U[psi]=h_qf[psi]+U ||Q_12 psi||^2,       U>=0.       (3)
```

The forms increase with `U`. Monotone form convergence therefore gives a
self-adjoint strong-resolvent limit whose form is

```text
Dom(h_hc)=Dom(h_qf) intersect Ran(P),
h_hc=h_qf restricted to Ran(P).                        (4)
```

By (2), (4) is precisely the native three-state shared-corner Hamiltonian
selected by K139--K147. This constructs it without inventing a two-mode
Bogoliubov lift. The auxiliary `C4` carrier and every finite `U` are comparison
objects; only the `U=infinity` restriction is native.

## 2. The honest Feshbach map is operator-valued

Inside `Ran(P)`, split the impurity into the vacuum and leaf subspaces,

```text
P_0=|0><0|,       P_L=|1><1|+|2><2|.                  (5)
```

The native operator has the block form

```text
H_hc=[ H_0   T* ; T   H_L ],                           (6)
```

where `T` contains the four particle/hole boundary fields multiplying the two
Hubbard transitions. For `z` in the resolvent set of `H_L`, the exact vacuum
Feshbach map is

```text
F_0(z)=H_0-z-T*(H_L-z)^-1 T.                           (7)
```

The last term acts on the full bath Fock space. Its diagonal pieces contain
occupation-dependent Pauli contractions; its off-diagonal `i!=j` pieces
exchange the two edge flavors through
`B_i B_j*=|i><j| tensor kappa_i kappa_j`. It neither commutes with all bath
occupations nor collapses to a scalar Weyl function or a `3 by 3` impurity
matrix. Equation (7), restricted by `(q_1,q_2)` below, is the actual nonlinear
spectral problem left by K147. The projected matrix Schur function omitted
these higher Fock sectors and cannot supply its roots.

## 3. The hard-core constraint strictly lifts the quadratic ground

Write `E_B<0` for K146's one-flavor many-body ground energy and `Z` for its
zero-mode impurity weight,

```text
Z=(1+2 I_2)^-1,       0<Z<1,
p_-=(1-Z)/2,          p_+=(1+Z)/2.                    (8)
```

For one flavor, the two ground vectors in charges `0,1` have compressed local
impurity occupations `p_-,p_+`. Hence the four-dimensional ground space of
`H_qf` has energy `2E_B`, and the compression of `Q_12` to that space has
eigenvalues

```text
p_-^2, p_- p_+, p_+ p_-, p_+^2.                       (9)
```

All are positive. No unconstrained two-flavor ground vector satisfies the
native hard-core constraint. Since the next quadratic excitation costs at
least `tau=5/4`, the angle estimate

```text
||Pi_ground psi||^2 <= 1/(1+p_-^2),       Q_12 psi=0  (10)
```

and the spectral gap give the explicit lower comparison

```text
2E_B + tau p_-^2/(1+p_-^2) <= E_hc.                   (11)
```

For the upper comparison, take either normalized one-flavor K146 ground and
tensor it with the other flavor's bare vacuum. It lies in `Ran(P)`; the unused
flavor interaction has zero expectation. Therefore

```text
2E_B < 2E_B+tau p_-^2/(1+p_-^2)
        <= E_hc <= E_B < 0.                            (12)
```

Thus K147's missing impurity state has a strict, not merely formal, spectral
effect. The native energy is not the sum of two quasifree ground energies.

K143's localization hypotheses survive the bounded local projection: the
point defect remains fixed, its dressed boundary vectors are `L2`, screened
cross-cluster terms vanish and every escaping fermion costs at least `tau`.
The massive HVZ lower bound places the global essential spectrum at least
`tau` above `E_hc`; compactness below that edge makes `E_hc` an isolated
finite-multiplicity native eigenvalue. This proves nonempty native point
spectrum, not its complete charge decomposition or a closed formula for
`E_hc`.

## 4. The true first thresholds use residual hard-core energies

The exact conserved coordinates for the two-edge corner are

```text
q_i=n_i+N_(i,+)-N_(i,-),       i=1,2.                 (13)
```

Let `E_j(q)` denote an actual discrete eigenvalue of the native residual
Hamiltonian in charge `q=(q_1,q_2)`. An escaping particle of flavor `i`
carries `+e_i`; an escaping hole carries `-e_i`. The complete one-escape
threshold set in total charge `q` is therefore

```text
T_q^(1)={E_j(q-e_i)+tau, E_j(q+e_i)+tau:
         i=1,2 and the named residual eigenvalue exists}.               (14)
```

Its infimum is the first one-particle HVZ edge. Higher escape clusters add
Minkowski sums of `[tau,infinity)` exactly as in K143. Equation (14) is
numerically decidable only after (7) supplies the residual energies. In
particular, K147's three projected zeros are not entries of (14).

## 5. Native threshold rank is a residual-density invariant

Fix one normalized residual bound state `phi`. Across the four adjacent
total-charge channels obtained by attaching one of the two particles or two
holes to that residual, the leading signed endpoint form-factor Gram matrix is
block diagonal because the polarities and resulting charge sectors are
independent:

```text
D_phi=L_phi direct-sum p_0 I_2,                        (15)
(L_phi)_(ij)=<phi,B_i B_j* phi>,
p_0=<phi,P_0 phi>.                                    (16)
```

`L_phi` is the Gram matrix of `B_1*phi,B_2*phi`, hence is positive,
`rank(L_phi)<=2`, and

```text
tr L_phi=1-p_0,
rank D_phi=rank L_phi+2 1_(p_0>0),
dim ker D_phi=4-rank D_phi.                            (17)
```

This is the complete single-residual native form-factor classification. It is
a building block for (14), not one universal fixed-total-charge threshold
matrix: at specified total charge and energy, retain only compatible residual
states and assemble all form factors across a degenerate residual eigenspace.
If
`0<p_0<1`, the rank is three or four depending on whether the leaf/Klein
coherence has rank one or two. If a nondegenerate residual state is invariant
under the equal-coupling leaf-flavor `SU(2)`, then
`L_phi=(1-p_0)I_2/2`; for `0<p_0<1`, all four signed channels are bright. A
rank-three form-factor block has one genuine native dark combination, unlike K147's
Pauli-removed projected direction. Degenerate residual eigenspaces require the
corresponding matrix of form factors between all residual vectors; (15)--(17)
apply to each one-state diagonal block and do not manufacture a universal
rank.

## Inline postflight bookend

- **Strongest construction:** the native shared corner is the monotone
  infinite-`U` restriction of the two-flavor K146 parent, not an informal
  compression or an enlarged native carrier.
- **Strongest spectral result:** its global ground is a genuine isolated
  eigenvalue in the strict bracket (12); hard-core exclusion raises it above
  the unconstrained value `2E_B`.
- **Strongest threshold result:** every first edge is an actual residual
  hard-core energy shifted by `tau`, and every one-residual signed rank is
  fixed by (15)--(17).
- **Strongest contrary route:** the auxiliary finite-`U` Anderson family is a
  valid approximation and may support numerical/Bethe-ansatz work, but no
  finite `U` or quadratic ground is the native result.
- **Strongest overclaim:** calling (12) a complete point-spectrum solution.
  Refused: charge-sector excited eigenvalues and the exact value of `E_hc`
  still require the operator-valued equation (7).
- **Weakest reproducibility seam:** the HVZ ground-existence step uses the
  same massive-local compactness hypotheses already proved for the supplied
  K139--K143 point/screened control; a different extension, massless field or
  unscreened thermodynamic model must recheck it.

The companion probe checks the exact exterior-to-Hubbard compression,
monotone finite-`U` control, ground-space occupations and angle bound,
charge shifts, residual-density rank cases, `SU(2)` full-rank consequence and
scope fences under baseline-first hostile mutations.

## Next condition

Solve the charge-restricted operator equation (7), analytically or through a
convergent finite-volume/finite-`U` enclosure, for the residual energies that
enter (14). Start with the ground-carrying charge sectors and compute their
full residual form-factor matrices. Only then test strict Mourre constants
through the surviving native threshold set and attempt many-body scattering.
Multichart finite-volume comparison, physical/source selection and
open-system NESS/current remain independent routes.

## Reproduction

```bash
python3 tests/channel-swings/k148_hard_core_infinite_u_feshbach_ground_threshold_probe.py
python3 tests/channel-swings/k148_hard_core_infinite_u_feshbach_ground_threshold_probe.py --selftest
```
