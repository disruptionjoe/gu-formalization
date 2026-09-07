---
title: "K135 K134 operator exchange IBC completion and polarization Coulomb boundary"
status: active_research
doc_type: conditional_operator_graph_point_fock_ibc_extension_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned positive-dispersion finite-circle theorem that point annihilation and the normal-ordered exchange term converge on the free operator graph and that one explicitly dressed K134 IBC completion is self-adjoint with cutoff norm-resolvent convergence; the completion contains finite self-adjoint extension data not selected by the ultraviolet tail and is not convergence of the minimally countertermed K127 cutoff, while the signed-Dirac result requires a supplied positive particle-hole polarization and the Coulomb/Gauss result closes only at fixed particle truncation, so no uniquely selected complete physical point-Fock/Gauss Hamiltonian, infinite-volume NESS/current, smooth unreduced parent, Weinstein/source/GU ownership, Born derivation, prediction or confirmation follows
manifest: lab/process/k135-k134-operator-exchange-ibc-extension-polarization-coulomb-boundary-wave.json
probe: tests/channel-swings/k135_k134_operator_exchange_ibc_extension_polarization_coulomb_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K135 K134 operator exchange IBC completion and polarization/Coulomb boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) 126
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> lab/methods/source-native-comparator-routing.md and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet remains on K134's repository-owned, positive-dispersion,
finite-circle matrix-unit/Klein/CAR control. It defines the normal-ordered
exchange operator on the free **operator** graph and constructs one explicit
boundedly dressed IBC extension. It does not prove that the minimally
countertermed K127 cutoff converges or that this extension is uniquely
physical. Its signed-Dirac and Coulomb conclusions are exact boundaries on
which extra representation or uniform-domain data are still missing.

```gu-typed-objects
result: point annihilation and the K134 normal-ordered exchange converge in the free-operator graph dual; the nilpotent K134 boundary transform gives one self-adjoint dressed IBC completion with norm-resolvent cutoff convergence, but finite extension data remain unselected and only a supplied positive Dirac polarization plus fixed-particle Coulomb truncations close
carrier: C9 tensor C512 tensor Gamma_minus(direct_sum over eighteen positive-dispersion l2(Z) species), with signed empty-vacuum and positive particle-hole doubled carriers compared but not identified; K128/K131 Coulomb is added only after finite particle truncation LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive impurity, Clifford-Klein and antisymmetric Fock Hilbert pairing; the dressed theorem uses a positive shifted regular operator and boundedly invertible nonunitary congruence ON=repository_operator_graph_point_control
real_structure: CAR adjoint, complex conjugation in momentum and impurity bases, Hermitian finite exchange extension and particle-hole adjoint after a supplied polarization
grading: matrix units are even, Clifford-Klein and CAR fields are odd, defect monomials are even, and the K134 boundary creation map strictly lowers the ordered impurity label
action_owner: repository-construction -- point coupling, subtraction, finite exchange extension, Dirac polarization, sea normal ordering, Coulomb truncation and state are supplied rather than selected by Weinstein's source or a GU action
target: operator-graph exchange closure, explicit dressed IBC self-adjoint extension, extension-selection discriminator, signed-polarization boundary and fixed-particle Coulomb/Gauss boundary MAP-TYPE=not-a-map
```

## Inline preflight bookend

K134's negative result is topological in the Sobolev scale, not an operator-
domain no-go. The point functional is outside the dual of the `H^(1/2)` form
domain because `sum omega_k^-1` diverges, but it belongs to the dual of the
free operator graph because `sum omega_k^-2` converges. The route census
therefore separated: (a) graph-dual completion of point annihilation; (b)
normal-ordered exchange convergence; (c) self-adjoint IBC closure; (d) finite
extension selection; (e) signed-Dirac representation choice; (f) Coulomb/Gauss
all-sector uniformity; and (g) thermodynamic scattering.

The problem-matched lenses were fermionic second quantization, weighted graph
duals, Kato--Rellich perturbation theory, bounded congruence extensions,
norm-resolvent convergence, self-adjoint extension nonuniqueness, Dirac-sea
polarization, finite-volume Coulomb forms, Gauss reduction, source ownership
and hostile claim audit. The cheapest closure was graph-norm convergence of
the point annihilator. The cheapest kill was uniqueness of the Hamiltonian
from K134's IBC tail. No correction-registry entry supersedes K127, K128,
K131, K132 or K134.

## 1. Point annihilation closes on the free operator graph

Let

```text
h = direct_sum_(e=1)^18 l2(Z),
omega_k = sqrt(m^2+k^2),  m>0,
H_f = dGamma(omega),
delta_(e,N)(k)=1_(|k|<=N),
b_(e,N)=a_e(delta_(e,N)).                              (1)
```

For `psi in Dom(H_f)` and `N>K`, CAR Cauchy--Schwarz on every particle
sector gives

```text
||(b_(e,N)-b_(e,K)) psi||
 <= c_K ||H_f psi||,
c_K^2 = sum_(|k|>K) omega_k^-2 -> 0.                   (2)
```

For a fixed low block, `||a_e(delta_(e,K))||<=sqrt(2K+1)`. Splitting at `K`
therefore gives, for every `epsilon>0`,

```text
||b_e psi|| <= epsilon ||H_f psi|| + C_epsilon||psi||. (3)
```

Thus `b_(e,N)` converges in the operator norm from `Dom(H_f)` equipped with
its graph norm to Fock space. This is the exact strengthening left open by
K134. It does not repair the form route: the corresponding form-dual series
is `sum omega_k^-1`, which still diverges.

K134's normal ordering places a resolvent-dressed creation operator on the
other leg. Its one-particle coefficient is dominated by
`r_k=(omega_k+mu)^-1`, and `r in l2(Z)`, so fermionic creation by `r` is
bounded. Equations (2)--(3), the finite eighteen-edge matrix sum and the
pull-through resolvent bound therefore imply

```text
T_N -> T in B(Dom(H_0)_graph, Fock),
||T psi|| <= epsilon ||H_0 psi|| + C_epsilon||psi||,    (4)
```

for the complete adjoint-paired normal-ordered exchange operator. `T` is
symmetric on `Dom(H_0)`. K134 established the weaker form estimate for its
diagonal occupation/spectator term `Q`; its explicit diagonal formula also
upgrades to the operator graph here. For the vacuum tail,
`|q(X)-q_N(X)|/(1+X)` is bounded by
`sum_(|k|>N)(omega_k+mu)^-2`; for the occupied tail K134's low/high split
gives the same graph-relative convergence after division by `1+H_f`.
Consequently `Q` is infinitesimally `H_0`-operator-bounded and `Q_N` converges
in the relative graph norm. Together with (4), Kato--Rellich gives a
self-adjoint regular
operator

```text
K_W = H_0 + Q + T + W + c                           (5)
```

on `Dom(H_0)`, bounded below by one after a finite shift `c`. Here `W` is any
bounded self-adjoint finite boundary/exchange term allowed by the declared
impurity and parity symmetries.

## 2. One explicit self-adjoint dressed IBC completion

K134 supplies norm-convergent boundary maps `G_N -> G`. The increasing
orientation makes every `G_N` and `G` strictly lower the nine-state impurity
label, hence

```text
G_N^9=G^9=0,
U_N=1-G_N,
U=1-G,
U_N^-1=sum_(j=0)^8 G_N^j -> U^-1.                       (6)
```

Let `Q_N,T_N` be their cutoffs and choose the same `W,c` in
`K_(W,N)=H_0+Q_N+T_N+W+c`. The graph-relative tail estimates imply
`K_(W,N)^-1 -> K_W^-1` in norm. Define

```text
L_(W,N)=U_N* K_(W,N) U_N,
Dom(L_(W,N))=U_N^-1 Dom(H_0),
L_W=U* K_W U,
Dom(L_W)=U^-1 Dom(H_0).                                 (7)
```

Because `K_W>=1` and `U` is boundedly invertible,

```text
L_W^-1 = U^-1 K_W^-1 (U*)^-1                           (8)
```

is bounded, positive and self-adjoint. Its inverse is therefore the positive
self-adjoint operator in (7). The same holds at every cutoff. Equations
(6)--(8) give

```text
||L_(W,N)^-1-L_W^-1|| -> 0,                             (9)
```

which is norm-resolvent convergence at the common real resolvent point zero.
The domain condition `U psi in Dom(H_0)` is one recursive operator-domain IBC:
the singular K134 tails of `psi` are exactly removed by `1-G` before the
regular graph operator acts.

This is a genuine complete self-adjoint singular point-Fock operator for the
declared **dressed renormalization scheme**. Expanding (7) produces finite
dressing corrections in addition to the minimally countertermed
`H_0+A_N+A_N*+c_N D_g`. No equality with that minimal K127 cutoff family is
proved. Calling (7) “the physical K127 point Hamiltonian” would erase the
remaining extension choice.

## 3. The ultraviolet tail does not select the finite extension

The same `G`, IBC recursion, divergent diagonal counterterm and graph-domain
exchange estimate work for every bounded self-adjoint `W`. If `W_1-W_2` is
nonzero on a state reached by `U`, the resolvent identity gives

```text
L_(W1)^-1-L_(W2)^-1
 = U^-1 [K_(W1)^-1-K_(W2)^-1] (U*)^-1 != 0.             (10)
```

Thus there are distinct self-adjoint norm-resolvent completions with the same
K134 ultraviolet tail and Pauli boundary recursion. This is not a defect in
the existence theorem; it is the exact ownership boundary. A physical action,
renormalization condition, symmetry, scattering datum or source-owned rule
must select `W`. None is presently supplied by Weinstein's source or a GU
action.

## 4. Signed Dirac requires a polarization choice

On the empty-vacuum Fock representation of the full signed circle Dirac
operator, filling all negative one-particle modes through cutoff `N` gives

```text
inf spectrum dGamma(D_N) <= -18 sum_(|k|<=N) omega_k,
```

so the lower bound tends to minus infinity. The positive-shift argument used
in (5)--(9) is therefore not uniform on that representation. This does not
prove that every indefinite operator-domain extension fails.

A chosen Dirac-sea particle/hole polarization replaces the free generator by
the positive doubled operator `dGamma(omega)_particles +
dGamma(omega)_holes`. Its point-resolvent coefficients have squared norm
`2 sum(omega_k+mu)^-2<infinity`, and the positive theorem above applies after
declaring how each defect monomial creates particles or holes. But the
polarization, sea charge, normal-ordering constant and defect split are new
representation data. The result is a conditional positive-polarization lift,
not the unsupplied full signed-Dirac K127 lift.

## 5. Coulomb/Gauss closes at every fixed particle truncation, not uniformly

K128/K131 Coulomb energy is multiplication by the squared cumulative charge
field in position configuration space. It does not commute with momentum
occupation, so K134's joint spectral formula cannot be reused. On a finite
interval and sectors with at most `P` particles, however, bounded charges and
finite string length give

```text
0 <= C_P <= C (P+1)^2.                                  (11)
```

It is then a bounded perturbation of every fixed-`P` regular operator. After
compressing point creation at the top sector, adding `C_P` to (5) leaves the
graph domain unchanged, and (6)--(9) construct a self-adjoint dressed
Coulomb/Gauss point completion for each fixed particle truncation.

The bound in (11) grows with `P`. The present proof contains no uniform
commutator-resolvent estimate, no all-sector position-space IBC trace theorem
and no proof that the fixed-`P` resolvents converge as `P->infinity`.
Fermionic kinetic energy may control the quadratic particle growth, so this
is not a no-go. It is the exact remaining all-Fock gate.

## Inline postflight bookend

- **Strongest advance:** K134's exchange obstruction is closed on the free
  operator graph, and one explicitly dressed full-Fock IBC Hamiltonian is
  self-adjoint with norm-resolvent cutoff convergence.
- **Strongest overclaim:** “The physical K127 point Hamiltonian is now
  uniquely constructed.” Refused. The minimal cutoff family is not proved to
  converge, and finite self-adjoint `W` data change the resolvent without
  changing the ultraviolet tail.
- **Strongest contrary route:** a direct boundary-triple/Feshbach theorem may
  select or derive the minimal extension and could also handle an indefinite
  signed vacuum. This packet does not exclude it.
- **Strongest representation boundary:** a positive particle/hole Dirac
  polarization restores semiboundedness but imports the sea and normal-ordering
  convention; it is not the empty-vacuum signed K127 representation.
- **Weakest propagation seam:** fixed-particle Coulomb boundedness can be
  mistaken for an all-Fock theorem. The probe forces the quadratic cutoff
  growth and momentum/position noncommutation to remain explicit.

The exact control and baseline-first hostile selftest are recorded by the
companion probe. No uniquely selected complete physical point-Fock/Gauss
Hamiltonian, infinite-volume scattering, interacting NESS/current, smooth
unreduced parent, source/GU action, Born rule, held-out score, prediction,
confirmation, canon, paper, release or public-posture move follows.

## Reproduction

```bash
python3 tests/channel-swings/k135_k134_operator_exchange_ibc_extension_polarization_coulomb_probe.py
python3 tests/channel-swings/k135_k134_operator_exchange_ibc_extension_polarization_coulomb_probe.py --selftest
```
