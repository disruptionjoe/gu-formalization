---
title: "K139 signed boundary inverse and profile universality wave"
status: active_research
doc_type: conditional_signed_point_fock_neumann_chart_and_bounded_profile_universality_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned finite-circle theorem on a supplied positive particle/hole polarization that an auxiliary resolvent shift gives a cutoff-uniform convergent Neumann inverse for the natural bidirectional boundary map at every fixed finite coupling, that the doubled endpoint counterterm and four polarity exchange blocks close the minimally countertermed signed point-Fock and finite-interval Coulomb/Gauss limits, and that the result is universal for matched uniformly bounded pointwise-convergent diagonal regulator profiles; no volume-uniform limit, uniquely physical extension or polarization, infinite-volume scattering/NESS/current, smooth unreduced parent, Weinstein/source/GU owner, Born derivation, prediction or confirmation follows
manifest: lab/process/k139-signed-boundary-inverse-profile-universality-wave.json
probe: tests/channel-swings/k139_signed_boundary_inverse_profile_universality_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K139 signed boundary inverse and profile universality wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) 126
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> lab/methods/source-native-comparator-routing.md and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet stays on K138's declared positive particle/hole
polarization of the repository-owned finite-circle point control. It proves a
uniform inverse and a minimally countertermed signed limit on that carrier.
The auxiliary shift below is a coordinate in the boundary-domain
factorization, not a physical mass, coupling restriction or selected
renormalization condition. The sea, polarization, finite extension, interval
and state remain supplied rather than source-owned.

```gu-typed-objects
result: the natural bidirectional signed boundary transform has a cutoff-uniform convergent Neumann inverse after an arbitrarily large auxiliary resolvent shift; its two endpoint counterterms, four polarity exchange blocks and geometrically summed higher words close the finite-circle minimal signed point-Fock/Coulomb limit, uniformly across matched bounded pointwise-convergent diagonal regulator profiles
carrier: C9 tensor C512 tensor Gamma_minus of the direct sum of eighteen particle and eighteen hole l2(Z) species tensor l2(Z8), with arbitrary finite-particle spectators on a supplied positive spectral polarization LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive impurity, Klein and antisymmetric particle/hole Fock Hilbert pairing; free-operator graph and particle-number graph pullbacks by a boundedly invertible nonunitary boundary transform ON=repository_signed_point_control
real_structure: CAR adjoint and momentum conjugation; particle and hole charges are opposite, endpoint subtraction is Hermitian, and all mixed-polarity exchange blocks occur with their adjoints
grading: matrix units are even, Klein/CAR fields are odd and defect monomials are even; signed creation raises or lowers the impurity label, so convergence uses a geometric boundary-word majorant rather than a finite label filtration
action_owner: repository-construction -- positive polarization, sea-charge convention, defect split, regulator class, couplings, finite extension, Coulomb interval/domain and state are not selected by Weinstein's source or a GU action
target: cutoff-uniform signed boundary inverse, doubled endpoint/exchange census, minimally countertermed signed point-Fock/Gauss limit and bounded matched-profile universality MAP-TYPE=not-a-map
```

## Inline preflight bookend

K138 gives an exact obstruction to reusing K137: the signed creation map runs
in both impurity directions and has nonzero words of length five. That kills a
particular finite inverse polynomial, not invertibility. The higher-altitude
question is whether the resolvent parameter already present in the boundary
chart can make every bidirected word summable without weakening the physical
coupling.

Mechanism retrieval found K135's free-operator-graph point annihilator,
K137's endpoint contraction and minimal pullback, and K138's bidirected path.
It found no signed Neumann chart, lower-endpoint counterterm, four-polarity
exchange census or bounded-profile theorem. No correction-registry entry
supersedes these inputs.

The route census covered resolvent-dressed CAR creation, boundary triples,
Neumann and Fredholm alternatives, Feshbach pullback, graph-relative exchange,
geometric word majorants, charge/polarity orientation, finite-volume Coulomb
number graphs, dominated regulator convergence, physical renormalization
selection and hostile scope audit. A Fredholm-only route would prove
invertibility away from a discrete set but would not give the uniform cutoff
or word-summation bounds. The resolvent-shift Neumann route gives both. Exact
computation checks the rook endpoints, contraction margin and four sample
profiles; it is not the analytic proof.

## 1. A uniform inverse without nilpotence or weak physical coupling

For each rook edge `e=(u,v)`, `u<v`, set `B_e=|v><u| tensor kappa_e` and use
independent particle/hole CAR species. The annihilation half of the natural
signed point field is

```text
C_N=sum_e[g_(e,+) B_e a_(e,+)(r_N delta)
         +g_(e,-) B_e* a_(e,-)(r_N delta)],             (1)
```

so its adjoint creates a particle while lowering the impurity label and a
hole while raising it. Let `H_0^pol>=0` be the positive particle/hole free
energy and introduce the **auxiliary** boundary-chart parameter `lambda>0`:

```text
G_(N,lambda)=-(H_0^pol+lambda)^-1 C_N*,
U_(N,lambda)=1-G_(N,lambda).                            (2)
```

For a regulator bounded by `M`, CAR creation and pull-through give

```text
||G_(N,lambda)||
 <= M sum_(e,s)|g_(e,s)| h(lambda)=q(lambda),
h(lambda)^2=sum_(k in Z)(omega_k+lambda)^-2.            (3)
```

The series is finite and `h(lambda)->0` as `lambda->infinity`. Therefore,
for **every fixed finite** coupling family, choose `lambda` so that
`q(lambda)<1`. This is not a small-coupling hypothesis: no `g_(e,s)` is
changed, and `lambda` is free to increase. The cutoff maps converge in norm
because the omitted coefficient tail converges in `l2`. Consequently

```text
U_(N,lambda)^-1=sum_(j>=0)G_(N,lambda)^j,
sup_N ||U_(N,lambda)^-1|| <= (1-q)^-1,
U_(N,lambda)^-1 -> U_lambda^-1                         (4)
```

in operator norm. No graph nilpotence is used.

The physical cutoff operator does not acquire `lambda`. Adding and
subtracting `lambda` in the exact pullback identity merely moves a bounded
diagonal term between the free resolvent used in (2) and the regular operator.
Equivalently, changing `lambda` changes the domain chart `U_lambda` while the
expanded minimally countertermed operator is held fixed. Thus the condition
`q(lambda)<1` selects a convenient coordinate patch, not a physical
weak-coupling phase.

## 2. The signed field doubles endpoints, not logarithmic matrix structure

Normal ordering `C_N(H_0^pol+lambda)^-1C_N*` produces exactly two diagonal
vacuum contractions:

```text
c_N(lambda) D_g^pol,
D_g^pol=sum_e[|g_(e,+)|^2 B_e B_e*
             +|g_(e,-)|^2 B_e* B_e].                  (5)
```

The first is supported at the upper endpoint `v`; the second at the lower
endpoint `u`. Particle and hole species are independent, so mixed-polarity
vacuum contractions vanish. For equal particle and hole couplings, upper and
lower incidences partition the four edges at each rook vertex, so (5) is
`4g^2 I`. No off-diagonal
logarithmic counterterm appears.

After (5) is removed, normal ordering leaves four polarity blocks:

```text
T^(++), T^(+-), T^(-+), T^(--).                        (6)
```

The diagonal blocks preserve polarity; the mixed blocks convert one
quasiparticle polarity into the other. Each block contains one point
annihilation trace and one resolvent-dressed creation coefficient. K135's
estimate applies verbatim to every finite edge/polarity pair:

```text
||(T_N^(st)-T^(st)) psi||
 <= epsilon_N ||H_0^pol psi||+c_N'||psi||,
epsilon_N ->0,             s,t in {+,-}.               (7)
```

Every additional bidirected boundary word carries a factor of `G`. Instead
of terminating after four factors, the complete word family is dominated by
`sum_j q^j`. Equations (3), (4), (7), the subtracted `O(k^-2)` contraction
tail and finite edge count therefore make the pulled-back regular operators
Cauchy in `H_0^pol`-graph relative norm.

## 3. Minimal signed point-Fock and finite-interval Gauss limits

Define the signed minimally countertermed cutoffs, with `E_R(lambda)` shifted
by the finite difference between subtraction coordinates so the expanded bare
family is independent of the auxiliary chart,

```text
H_N^pol=H_0^pol+C_N+C_N*+E_R(lambda)+c_N(lambda)D_g^pol. (8)
```

The exact conjugation by (4) cancels the naked singular linear terms. After
(5), the remaining regular operator consists of the diagonal Pauli/spectator
term, the four blocks (6), and the absolutely geometrically summed higher
words. A common finite lower shift makes these operators self-adjoint on
`Dom(H_0^pol)`, uniformly semibounded, and graph-relatively convergent. The
inverse factorization then gives

```text
H_N^pol -> H_min^pol                                   (9)
```

in norm resolvent on the full positive particle/hole Fock carrier. Its common
recursive boundary domain is `U_lambda^-1 Dom(H_0^pol)`. Equation (9) is the
signed analogue of K137 for the supplied polarization; it is not an
empty-vacuum indefinite Dirac theorem and it does not physically select the
sea or finite extension.

For the particle-number graph, creation costs at most the standard factor two
under conjugation by `N+1`. Increase the auxiliary `lambda`, without changing
(8), until `2q(lambda)<1`. Then (4) also converges on that graph. K136--K137's
finite-interval estimate

```text
0 <= Coul_L <= C_L(F_root^2+(N_p+N_h+1)^2)             (10)
```

pulls back in form norm and preserves (9) after adding the raw all-sector
Coulomb/Gauss form. The constant `C_L` depends on the interval. Nothing here
is uniform as `L->infinity`.

## 4. A stated matched-regulator universality class

K138's sharp/Abel argument extends without a special summation formula. Let
`r_N:Z->C` be diagonal momentum profiles satisfying

```text
sup_(N,k)|r_N(k)| <= M < infinity,
r_N(k) -> 1 for each fixed k,
sum_k |r_N(k)|^2/(omega_k+lambda) < infinity for each N. (11)
```

and pair each coupling with its own squared-profile endpoint counterterm

```text
c_N^r(lambda)=sum_k |r_N(k)|^2/(omega_k+lambda).       (12)
```

The subtracted contraction is bounded uniformly by `M^2 C_X(1+k^2)^-1`,
while `r_N/(omega+lambda)` converges in `l2` by dominated convergence. Thus
the elementary boundary maps, all four exchange blocks and every subtracted
contraction converge to profile-independent limits. The geometric bound in
(4) is common after choosing `lambda` with
`M sum|g| h(lambda)<1`, so dominated convergence also passes through the
infinite boundary-word sum. Hence every matched family satisfying (11)--(12)
has the same `H_min^pol` at a fixed renormalized boundary coordinate.

The last condition only requires each regulated raw endpoint sum to exist; it
is not a common summable dominator as `N` grows. Sharp, Abel, Gaussian and
Fejer profiles are examples. Their raw counterterms
may differ by finite or divergent coordinate terms; equality of raw sums is
neither assumed nor physical. Unbounded, nonlocal, matrix-mixing or
non-pointwise-convergent regulators lie outside this theorem.

## Inline postflight bookend

- **Strongest advance:** the signed bidirectional boundary map is uniformly
  invertible for arbitrary fixed finite couplings after choosing an auxiliary
  resolvent chart, and the minimal signed point-Fock/Gauss cutoff closes on the
  supplied positive polarization.
- **Strongest structural classification:** the ultraviolet divergence is the
  sum of upper particle and lower hole endpoint matrices. Mixed polarity adds
  finite exchange blocks, not new logarithmic off-diagonal counterterms.
- **Strongest universality result:** one common domination theorem covers all
  uniformly bounded diagonal profiles converging pointwise to one when their
  endpoint subtractions are matched.
- **Strongest overclaim:** “the physical signed GU Hamiltonian is selected.”
  Refused. The polarization, sea charge, finite extension, couplings, volume
  and state remain repository inputs.
- **Strongest contrary route:** an indefinite Krein-space or empty-vacuum
  extension may exist and need not be equivalent to this positive
  particle/hole carrier. This theorem does not exclude it.
- **Weakest propagation seam:** the freely enlarged `lambda` can be mistaken
  for a physical mass/coupling bound, and finite-interval Coulomb control can
  be mistaken for a thermodynamic estimate. Both readings are explicitly
  false.

The companion probe checks 41 exact structural/numerical controls and uses a
baseline-first hostile harness with 35 planted mutations. No volume-uniform
limit, physical extension/polarization selection, infinite-volume
Moller/Ruelle theory, interacting NESS/current, smooth unreduced gauge parent,
Weinstein/source/GU action, Born rule, held-out score, prediction,
confirmation, canon, paper, release or public-posture move follows.

## Next condition

Seek owner-native complete Schur boundary data or an action principle that
selects the finite extension, polarization, sea charge and couplings. In
parallel, prove or refute volume-uniform bounds for the signed point-Fock/Gauss
operator under an explicit thermodynamic scaling; only then construct
Moller/Ruelle wave operators or return-to-NESS dynamics and compare a genuine
field current with K115's reduced cycle affinity. A smooth unreduced
connection/BRST parent and source/GU ownership remain separate requirements.

## Reproduction

```bash
python3 tests/channel-swings/k139_signed_boundary_inverse_profile_universality_probe.py
python3 tests/channel-swings/k139_signed_boundary_inverse_profile_universality_probe.py --selftest
```
