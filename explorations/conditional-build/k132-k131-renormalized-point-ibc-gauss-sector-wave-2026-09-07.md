---
title: "K132 K131 renormalized point/IBC Gauss-sector wave"
status: active_research
doc_type: reverse_scaffold_renormalized_point_ibc_gauss_sector_result
created: 2026-09-07
date: 2026-09-07
target_claim: INTERNAL_TARGET:K131_SINGULAR_NUMBER_CHANGING_POINT_INTERACTION_SUCCESSOR
claim_ceiling: exact repository-owned norm-resolvent construction of one singular number-changing impurity/one-CAR-channel point Hamiltonian on a finite circle after logarithmic bare-energy subtraction, with an equivalent momentum-tail IBC domain, exact subtraction-scale reparameterization, and a neutral Wilson/electric-string lift through one K131 diffuse Gauss/global-flux block; the shared-level eighteen-edge many-particle Hamiltonian, infinite-volume scattering, interacting NESS/current, source/GU ownership, Born derivation, prediction, confirmation and holdout credit remain unconstructed
manifest: lab/process/k132-k131-renormalized-point-ibc-gauss-sector-wave.json
probe: tests/channel-swings/k132_k131_renormalized_point_ibc_gauss_sector_probe.py
---

# K132 K131 renormalized point/IBC Gauss-sector wave

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
result: logarithmically renormalized singular impurity/one-CAR-channel point Hamiltonian, its norm-resolvent limit and momentum-tail interior-boundary condition, lifted through one neutral diffuse Gauss/global-flux block
carrier: one impurity amplitude plus one selected positive Dirac spectral branch l2(Z), tensored blockwise with the K131 spectator and l2(Z8) global-flux carriers LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive C plus l2(Z) Hilbert pairing, with the K131 positive diffuse configuration/global-flux pairing on spectator blocks ON=repository_owned_single_channel_point_control
real_structure: CAR adjoint, complex conjugation of Fourier amplitudes, Hermitian impurity transition and Clifford-Klein generator, and fibrewise Hilbert adjoint
grading: total fermion parity and total Z8 charge; the impurity matrix is even while the point CAR field and Clifford-Klein factor are odd, so their product is even
action_owner: repository-construction
target: one singular point-sector Hamiltonian and its exact Gauss/global-flux compatibility, with full-graph, thermodynamic and source boundaries MAP-TYPE=intertwiner
```

Scope: this packet constructs one exactly solvable neutral transition sector on
a finite circle. It proves a nontrivial singular point interaction that the
uniform KLMN route in K131 could not supply. It does not sum the eighteen K115
edges on the full antisymmetric Fock space and does not construct an
infinite-volume reservoir theory.

## Inline preflight bookend

The rebuilt frontier contained seven substantial arcs: a logarithmic
counterterm, the finite-cutoff self-adjoint family, Schur-complement
norm-resolvent convergence, an IBC domain, subtraction-scale flow, a diffuse
Gauss/global-flux lift, the full eighteen-edge many-particle extension,
infinite-lead NESS and source ownership. The counterterm/resolvent,
IBC/scale-flow and Gauss arcs were independently ready. The full graph was
admitted as a closure-or-obstruction discriminator; NESS lacked infinite-
volume dynamics and source credit lacked an authenticated action owner.

Mechanism retrieval finds the exact opening left by K125 and K131. K131 proves
that the point functional is not uniformly bounded on the `H^(1/2)` energy
form domain. This route never asserts that bound: it lets the bare impurity
energy run so the divergent scalar self-energy cancels in the resolvent.
K125 explicitly excluded neither a counterterm nor an IBC/resolvent limit. No
canonical correction supersedes the spectral, charge, parity or domain inputs.

The route-changing lens census covered singular Friedrichs/Lee models,
rank-one resolvent formulae, self-adjoint extension theory, Sobolev trace
thresholds, renormalization-scale covariance, fermionic number change,
impurity graphs, Abelian Gauss reduction, Wilson/electric strings, direct
integrals, global flux, scattering/NESS and source fidelity. A scalar
subtraction in one invariant block dominates another form-bound attempt
because the subtracted self-energy has an absolutely summable ultraviolet
tail.

## 1. Finite cutoffs and the logarithmic counterterm

Choose one positive one-particle Dirac spectral branch on the circle,

```text
omega_k = sqrt(mass^2 + (2 pi k/L)^2),  k in Z,  mass>0,             (1)
```

and write `chi_N(k)=1` for `|k|<=N` and zero otherwise. On
`C direct-sum l2(Z)`, define

```text
H_N = [ epsilon_N       g <chi_N,.> ]
      [ g chi_N              omega  ],                              (2)

epsilon_N = epsilon_R + g^2 sum_(|k|<=N) 1/(omega_k+mu),            (3)
```

where `mu>0`, `epsilon_R` and real `g!=0` are fixed. Each `H_N` is self-adjoint
on `C direct-sum Dom(omega)`: its off-diagonal is finite rank and bounded.
The bare level (3) diverges logarithmically. That divergence is not hidden; it
is the one running datum needed to retain a finite physical denominator.

The upper component is an impurity state and the lower component a one-fermion
state. The off-diagonal changes particle number by one. In the physical block
below, the even impurity matrix multiplies the odd CAR field and the same odd
Clifford-Klein factor as K126, so the complete term is fermion even.

## 2. Norm-resolvent convergence

For nonreal `z`, put `R_z=(omega-z)^(-1)` and

```text
b_N(z)=R_z chi_N,
D_N(z)=epsilon_R-z
       -g^2 sum_(|k|<=N)[1/(omega_k-z)-1/(omega_k+mu)].              (4)
```

The difference inside the sum is `(z+mu)/((omega_k-z)(omega_k+mu))`
and is `O(k^-2)`. Hence `D_N(z)` converges absolutely to `D(z)`. Also
`b_N(z)` converges in `l2` because its squared tail is `O(sum k^-2)`.
At `z=i`,

```text
Im D_N(i) = -1-g^2 sum_(|k|<=N) 1/(omega_k^2+1) < 0,                (5)
```

so every denominator, and its limit, is nonzero.

The Schur formula writes `(H_N-z)^(-1)` as the fixed free resolvent plus a
finite sum of rank-one terms whose only moving data are `b_N(z)` and
`D_N(z)^(-1)`. Their norm convergence proves

```text
(H_N-i)^(-1) -> R_ren(i) in operator norm.                           (6)
```

The norm-resolvent limit theorem therefore gives a unique self-adjoint
`H_ren`. This is a genuine nonzero singular point Hamiltonian: `g` stays
fixed, `chi_N` converges distributionally to evaluation at the impurity, and
the limiting off-diagonal is not a bounded operator on the free Hilbert
space. K131's no-uniform-form result remains true; (6) succeeds by changing
the operator domain and bare level, not by contradicting the trace theorem.

The family is also uniformly semibounded. If
`r>max(mu,-epsilon_R)`, the Schur complement of `H_N+r` is

```text
epsilon_R+r+g^2 sum_(|k|<=N)
 [1/(omega_k+mu)-1/(omega_k+r)] > 0.                                (6a)
```

Since `omega+r` is positive, (6a) gives `H_N>=-r` for every cutoff; the
norm-resolvent limit obeys the same lower bound. This permits a strongly
commuting positive spectator or global-flux energy to be added without
changing the point-domain construction.

## 3. The limiting IBC-style domain

Let `a_mu(k)=1/(omega_k+mu)`. Although `a_mu` lies in `l2`, it does not lie in
`Dom(omega)`. Every vector in the limiting domain has the unique form

```text
(c, psi),  psi = phi - g c a_mu,  phi in Dom(omega).                (7)
```

On this domain,

```text
H_ren(c,psi) =
 (epsilon_R c + g sum_k phi_k,
  omega phi + g c mu a_mu).                                        (8)
```

The sum in (8) is absolutely convergent by Cauchy--Schwarz because
`omega^-1` is in `l2`. The ultraviolet tail obeys

```text
(omega_k+mu) psi_k -> -g c  as |k|->infinity,                       (9)
```

since `omega_k phi_k -> 0`. Equation (9) is the interior-boundary condition:
the singular one-particle tail is fixed by the lower-sector impurity
amplitude. It is a momentum-tail/domain statement. It is not a continuous
coordinate point trace on `H^(1/2)`.

Changing the subtraction point from `mu` to `mu'>0` changes the coordinate
description but not the operator when

```text
epsilon_R(mu') = epsilon_R(mu)
 + g^2 sum_k [1/(omega_k+mu)-1/(omega_k+mu')].                       (10)
```

The sum is absolutely convergent and (10) makes `D(z)` identical. Thus `mu`
is a renormalization convention paired with `epsilon_R`, not a new physical
prediction or source-selected parameter.

## 4. One neutral diffuse Gauss/global-flux block

Choose one K115 edge `e:u->v` with integral charge vector `c_e` and impose

```text
q_u = q_v + c_e.                                                     (11)
```

The lower sector consists of impurity state `v` plus one species-`e` fermion
created at the impurity point. Equation (11) makes both sectors carry the
same total `Z^8` charge. The odd point CAR factor, even impurity transition and
odd Clifford-Klein factor therefore define an even neutral operator. In K131's
compact physical fibre, its zero-length endpoint Wilson character supplies
the same Gauss intertwiner as the limit of the fixed-width dressed terms; no
uncancelled local-gauge phase remains.

The transition does not change the root flux `m in Z^8`; hence the construction
acts diagonally on `l2(Z^8)`. Tensoring (2)--(8) with a fixed spectator block
preserves the norm-resolvent estimate. The positive global-flux energy strongly
commutes with the point block, so uniform semiboundedness and the spectral
sum theorem define their self-adjoint sum and preserve the global-flux form
domain. The point tail is therefore compatible with K131's diffuse physical
pairing, Gauss reduction and global-flux domain for this one transition
sector. A direct sum over general interacting spectator sectors still requires
the uniform estimates named in the next section.

This is reduced physical compatibility, not a smooth unreduced connection or
BRST parent. Because the particle is created exactly at the impurity, the
electric string has zero length in this block; the result does not prove a
nonzero-length point-splitting limit of connection holonomies.

## 5. The full eighteen-edge theory does not follow by summation

The K115 graph has nine impurity levels and eighteen shared edges. Its full
Fock Hamiltonian contains sectors with spectators, multiple admissible edge
transitions and Pauli occupancy. Those blocks are not an orthogonal direct sum
of eighteen copies of (2): different edges share impurity levels and their
creation/annihilation maps meet in common many-particle sectors. Coulomb and
global-flux energies can also make the diagonal denominator sector-dependent.

Consequently the one scalar counterterm (3) does not by itself prove that all
overlapping self-energies cancel, that the multi-edge domain intersections are
dense, or that the sum is self-adjoint and semibounded. The admitted
full-graph discriminator therefore returns `NOT-YET-CONSTRUCTED`, not a
no-go. A successor must formulate the operator-valued self-energy matrix on
the nine impurity levels, prove uniform spectator/global-flux estimates and
close the common IBC domain before claiming K115's complete point defect.

## 6. Thermodynamic and source boundaries

The construction is on a compact circle and has no incoming/outgoing
reservoir morphisms, return-to-NESS estimate or interacting field current.
K115's ratio `6561/256` remains a reduced finite-state target. The mass,
spectral branch, edge, charge, coupling, subtraction scale, renormalized
level, boundary condition, global sector and state are repository-selected.
No Weinstein/source/GU action owns them.

## Inline postflight bookend

The counterterm, finite-cutoff family, norm-resolvent limit, IBC domain,
subtraction-scale covariance and one-block Gauss/global-flux arcs completed.
The full eighteen-edge arc exposed an exact missing object: an operator-valued
nine-level self-energy/common-domain construction with uniform spectator and
global-flux control. Infinite-volume dynamics and source ownership remain
outside the licensed result.

- **Strongest construction:** a fixed-coupling singular point Hamiltonian in
  one neutral number-changing impurity/CAR channel, obtained as a norm-
  resolvent limit after one explicit logarithmic bare-energy subtraction.
- **Strongest overclaim caught:** a one-channel rank-one counterterm is not the
  complete eighteen-edge K115 Fock Hamiltonian, and an ultraviolet tail
  condition is not a continuous coordinate trace on `H^(1/2)`.
- **Strongest contrary route:** a matrix-valued renormalized resolvent or a
  simultaneous multi-channel IBC may close the shared impurity graph; the
  present block result supplies its diagonal control but neither proves nor
  excludes that extension.
- **Weakest reproducibility seam:** the positive spectral branch and scalar
  dispersion are selected controls. A full Dirac spinor, negative-energy
  polarization or infinite-volume limit can change multiplicities and
  renormalization bookkeeping.

No source action, physical preparation, detector effect, Born rule, held-out
score, prediction, confirmation, canon, paper, release or public-posture
status changes.

## Next condition

Construct the matrix-valued self-energy and common IBC domain for all nine
impurity levels and eighteen K115 transitions on the antisymmetric Fock/
diffuse-Gauss carrier, with uniform spectator and global-flux estimates.
Then take a controlled infinite-volume limit and prove wave operators or
return to an interacting NESS before identifying a microscopic current.
Independently build a genuinely unreduced smooth connection/BRST parent. An
actual source/GU action must still select every imported datum.

## Reproduction

```bash
python3 tests/channel-swings/k132_k131_renormalized_point_ibc_gauss_sector_probe.py
python3 tests/channel-swings/k132_k131_renormalized_point_ibc_gauss_sector_probe.py --selftest
```
