---
title: "K133 K132 matrix point-star IBC and spectator-uniformity boundary"
status: active_research
doc_type: conditional_matrix_point_star_ibc_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned nine-vertex/eighteen-channel vacuum-plus-one-excitation point-star Hamiltonian with positive weighted-Laplacian matrix counterterm, norm-resolvent limit, one dense common star-sector IBC domain and finite Hermitian subtraction-scale flow; fixed spectator blocks converge and finite Pauli occupation changes only finite remainders, but those remainders grow logarithmically with unbounded spectator/global-flux energy, so no complete antisymmetric multiparticle point-Fock Hamiltonian or common full-Fock/global-flux domain follows; no infinite-volume NESS/current, smooth unreduced parent, Weinstein/source/GU ownership, Born derivation, prediction or confirmation
manifest: lab/process/k133-k132-matrix-point-ibc-star-spectator-boundary-wave.json
probe: tests/channel-swings/k133_k132_matrix_point_ibc_star_spectator_boundary_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K133 K132 matrix point-star IBC and spectator-uniformity boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) 126
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> lab/methods/source-native-comparator-routing.md and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet extends K132 from one scalar point channel to one explicit
nine-vertex/eighteen-channel **incidence-coupled star model** on the finite
circle. The K123 graph is reused exactly, but the incidence coupling is a new
repository-supplied completion: K122's source-free CAR defect and no
Weinstein/GU action select it. The result is a vacuum-plus-one-excitation
Friedrichs carrier, not a proved invariant sector of the complete
antisymmetric CAR Fock interaction.

```gu-typed-objects
result: the complete K123 nine-vertex/eighteen-edge graph admits one stipulated incidence-coupled singular point-star Hamiltonian whose ultraviolet divergence is the positive weighted graph Laplacian; matrix Schur convergence gives a self-adjoint norm-resolvent limit and one dense common eighteen-channel momentum-tail IBC domain, while the renormalized finite remainder grows logarithmically with unbounded spectator/global-flux energy and therefore does not prove a common multiparticle Fock domain
carrier: C^9 direct sum over eighteen copies of l2(Z) for the vacuum-plus-one-excitation incidence star on a finite circle; this is not asserted to be an invariant sector of the full antisymmetric CAR Fock carrier LAYER=observed CHIRALITY=N/A
pairing: standard positive Hilbert pairing on C^9 and the eighteen l2(Z) channels, tensored only blockwise with K131 diffuse Gauss fibres and fixed l2(Z^8) global-flux eigenspaces ON=repository_incidence_point_star_control
real_structure: complex conjugation in the vertex and Fourier bases with a real Hermitian impurity matrix, real nonzero edge couplings and real oriented incidence columns
grading: degree-zero even Hamiltonian assembled from an impurity transition and the two odd CAR/Klein factors inherited from K132; no full BV-BFV or multiparticle Fock grading is constructed here
action_owner: repository-construction -- the incidence coupling, edge constants, impurity matrix, subtraction scale and domain are supplied controls, not selected by Weinstein's source or a GU action
target: matrix counterterm, norm-resolvent point-star limit, common star IBC and exact spectator-uniformity boundary MAP-TYPE=not-a-map
```

## Inline preflight bookend

K132 closes exactly one scalar Friedrichs/Lee block and explicitly leaves the
shared nine-level/eighteen-edge problem open. K123 supplies the exact connected
graph: nine vertices, eighteen undirected edges, incidence rank eight and cycle
rank ten. Retrieval found no existing matrix counterterm, common multi-edge IBC
domain or spectator-uniformity theorem. The cheapest route-changing question
is whether the edge overlap produces a convergent finite-dimensional matrix
Schur problem before any attempt at full Fock space.

The route census separated four constructions:

1. eighteen orthogonal K132 copies;
2. a vertex-incidence star;
3. a fixed-particle-number CAR sector with occupation-dependent contractions;
4. the complete Fock IBC Hamiltonian.

Route 1 is mistyped because shared vertices create off-diagonal self-energy.
Route 3 already requires Pauli/spectator operators. Route 4 depends on the
common-domain estimates this packet is meant to test. Route 2 is selected as
the minimal genuine matrix problem. It supplies an existence/control model,
not the unique or source-owned physical coupling.

## 1. Exact graph and the matrix divergence

Let V={0,...,8} be K123's 3 by 3 product vertices and let E be its eighteen
row-or-column edges. Choose an orientation for every edge and write

~~~
b_e = delta_v(e) - delta_u(e) in C^9,
0 < g_e < infinity.                                      (1)
~~~

The finite-circle one-excitation carrier is

~~~
H_star = C^9 direct-sum (direct-sum over e in E of l2(Z)). (2)
~~~

For cutoff N, the off-diagonal map sends a vertex amplitude c to
g_e <b_e,c> 1_{|k|<=N} in edge channel e. Its ultraviolet coefficient is

~~~
L_g = sum_e g_e^2 |b_e><b_e|.                            (3)
~~~

This is the weighted graph Laplacian. For every c,

~~~
<c,L_g c> = sum_e g_e^2 |c_v-c_u|^2 >= 0.               (4)
~~~

Connectedness gives rank(L_g)=8 and ker(L_g)=C(1,...,1). Adjacent vertices
give nonzero off-diagonal entries, so the divergence cannot be absorbed by
eighteen unrelated scalar levels or by one scalar multiple of the identity.
The required bare impurity matrix is

~~~
E_N = E_R + L_g sum_{|k|<=N} 1/(omega_k+mu),             (5)
~~~

where E_R=E_R*, mu>0, and omega_k=sqrt(m^2+k^2). The counterterm is a positive
logarithmically divergent matrix and vanishes only on the constant vertex
direction. This direction is a property of the supplied incidence completion,
not a physical dark state derived from K115.

## 2. Matrix Schur limit and self-adjoint point-star Hamiltonian

At nonreal z, the renormalized Schur matrix is

~~~
D_N(z) = E_R-z
         - L_g sum_{|k|<=N}
             [1/(omega_k-z)-1/(omega_k+mu)].             (6)
~~~

The bracket is O(|k|^-2), hence the scalar series converges absolutely and
D_N(z) converges in the norm of M_9(C). The resolvent coupling map has
Hilbert--Schmidt tail

~~~
sum_e g_e^2 ||b_e||^2 sum_{|k|>N}|omega_k-z|^-2 -> 0.    (7)
~~~

For z=i,

~~~
Im <c,D_N(i)c>
 = -||c||^2
   - sum_e g_e^2 |<b_e,c>|^2
       sum_{|k|<=N} 1/(omega_k^2+1) < 0.                 (8)
~~~

Thus every D_N(i) and its limit are invertible. The finite-rank block
resolvent formula, (6), and (7) give operator-norm convergence of
(H_N-i)^-1. The limit is the resolvent of a unique self-adjoint fixed-coupling
point-star Hamiltonian.

Choose r>mu with E_R+r>0. The Schur complement of H_N+r is

~~~
E_R+r + L_g sum_{|k|<=N}
  [1/(omega_k+mu)-1/(omega_k+r)] > 0.                    (9)
~~~

Therefore the cutoff family has one N-independent lower bound, and the
norm-resolvent limit inherits semiboundedness.

## 3. One dense common eighteen-channel IBC domain

Let c be in C^9. The limiting domain is

~~~
psi_e = phi_e - g_e <b_e,c>/(omega+mu),   e in E,
phi_e in Dom(omega).                                      (10)
~~~

All eighteen singular tails are controlled by the same vertex amplitude c.
Equation (10) is linear and dense: Dom(omega)^18 is dense in the channel
Hilbert space, and each fixed singular tail belongs to l2(Z), so arbitrary
channel data plus that tail can be approximated by regular remainders. It is
not in Dom(omega) unless its coefficient vanishes. Equivalently,

~~~
(omega_k+mu) psi_e(k) -> -g_e <b_e,c>                    (11)
~~~

along the ultraviolet tail after the regular remainder is removed. This is a
momentum-domain IBC. It is not a continuous coordinate point trace on the
critical H^(1/2) form domain.

Changing the subtraction scale from mu to mu' preserves the operator when

~~~
E_R(mu') = E_R(mu)
  + L_g sum_k [1/(omega_k+mu)-1/(omega_k+mu')].           (12)
~~~

The series in (12) converges absolutely. The renormalized datum therefore
flows by a finite Hermitian matrix, not by eighteen independent numbers.

## 4. Fixed spectators converge; unbounded spectators are not uniform

For a fixed nonnegative spectator energy s, the scalar coefficient becomes

~~~
q_s(z) = sum_k [1/(omega_k+s-z)-1/(omega_k+mu)].          (13)
~~~

It converges because its summand is O((1+s+|z|)|k|^-2). The estimate is
uniform for s in every bounded interval [0,S], so every fixed Coulomb or
global-flux eigenblock admits the same matrix construction.

It is not uniform over s>=0. Integral comparison gives

~~~
Re q_s(i) = -2 log(1+s) + O(1) as s -> infinity.         (14)
~~~

The exact constant depends on m and mu, but the logarithmic growth does not.
Thus the renormalized finite remainder is unbounded across the full spectator
or l2(Z^8) global-flux direct sum. It is sublinear, and log(1+s) is
infinitesimally form-bounded relative to s, so (14) is not a no-go. It names
the next theorem: an operator-valued self-energy defined by spectator
functional calculus plus relative form estimates.

Finite Pauli occupation removes finitely many virtual-mode summands. That
changes only a finite remainder at each finite-particle vector, but the
remainder depends on which modes are occupied. Therefore the full self-energy
contains occupation projections; it is not the fixed 9 by 9 matrix (6).

## 5. Exact boundary to the full CAR Fock problem

K133 constructs a genuine shared-level matrix point interaction, but only on
the stipulated star carrier (2). It does not construct:

- the antisymmetric multiparticle CAR carrier with creation/annihilation
  contractions on all sectors;
- the occupation-projection-valued self-energy and its common domain;
- uniform Coulomb and global-flux form estimates;
- a proof that the star carrier is invariant under the complete defect;
- an infinite-volume point dynamics, wave operator, interacting NESS or
  microscopic current.

The full route is not killed. Equation (14) makes the missing estimate
specific: dominate the logarithmic spectator functional by the free,
Coulomb, and global-flux form and prove that every Pauli correction shares one
dense IBC core. Only then can the complete nine-level/eighteen-edge point-Fock
Hamiltonian be claimed.

## Inline postflight bookend

- **Strongest overclaim:** “K133 constructs the complete K115 point-Fock
  defect.” Refused. It constructs an incidence-coupled
  vacuum-plus-one-excitation Friedrichs star whose coupling is supplied.
- **Strongest contrary construction:** the physical edge operators may couple
  oriented impurity/particle states through matrix units rather than incidence
  columns. That can change the counterterm matrix. K133 proves one explicit
  graph-compatible completion, not uniqueness.
- **Strongest mistyping risk:** treating pointwise convergence for each
  spectator energy as uniform convergence on Fock/global-flux space. Equation
  (14) proves that promotion false for this fixed subtraction.
- **Weakest reproducibility seam:** a finite spectator cutoff can hide the
  logarithmic growth. The probe checks increasing energies and separately
  verifies bounded-interval tail convergence, Pauli-pattern dependence,
  matrix rank, Schur inverse convergence and the IBC scale flow.

The baseline-first hostile selftest catches 30/30 mutations after the exact
control passes 46/46. No source/GU action, full multiparticle point-Fock
Hamiltonian, uniform global-flux domain, infinite-volume NESS/current, smooth
unreduced parent, Born rule, held-out score, prediction, confirmation, canon,
paper, release or public posture moves.

## Reproduction

~~~bash
python3 tests/channel-swings/k133_k132_matrix_point_ibc_star_spectator_boundary_probe.py
python3 tests/channel-swings/k133_k132_matrix_point_ibc_star_spectator_boundary_probe.py --selftest
~~~
