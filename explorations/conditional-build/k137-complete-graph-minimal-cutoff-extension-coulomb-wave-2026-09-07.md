---
title: "K137 complete-graph minimal cutoff, extension, and Coulomb wave"
status: active_research
doc_type: conditional_complete_positive_graph_minimal_point_fock_and_coulomb_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned positive-dispersion finite-circle theorem that the complete nine-state/eighteen-species ordered matrix-unit/Klein/CAR cutoff with a fixed sharp symmetric regulator and K134 diagonal endpoint subtraction has a norm-resolvent limit on full antisymmetric Fock space, that finite triangle/square/exchange remainders identify one scheme-dependent W_min in K135's dressed family, and that adding the raw finite-interval all-sector Coulomb/Gauss form preserves norm-resolvent convergence; no empty-vacuum signed-Dirac result, infinite-volume limit or NESS/current, scheme-independent or uniquely physical extension, smooth unreduced parent, Weinstein/source/GU owner, Born derivation, prediction or confirmation follows
manifest: lab/process/k137-complete-graph-minimal-cutoff-extension-coulomb-wave.json
probe: tests/channel-swings/k137_complete_graph_minimal_cutoff_extension_coulomb_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K137 complete-graph minimal cutoff, extension, and Coulomb wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) 126
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> lab/methods/source-native-comparator-routing.md and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet stays on K134--K136's repository-owned positive-dispersion
finite-circle control. It restores all nine impurity states, all eighteen
K115 graph edges, every Pauli sector and every overlapping triangular and
rectangular path. It proves the minimally countertermed cutoff converges for
that complete control and then adds the **raw** K128/K131 finite-interval
Coulomb form. It does not restore K127's empty-vacuum signed Dirac generator,
take spatial volume to infinity, or make the regulator-selected extension
physically preferred.

```gu-typed-objects
result: the complete positive-energy nine-state/eighteen-species physical matrix-unit point cutoff has a norm-resolvent limit with only K134's diagonal endpoint divergence; finite overlap words select a scheme-dependent W_min in the dressed extension family, and the raw finite-interval all-sector Coulomb/Gauss form can be added before the limit
carrier: C9 tensor C512 tensor Gamma_minus(direct_sum over eighteen positive-dispersion l2(Z) species) tensor l2(Z8), including arbitrary finite-particle spectators and every directed path of the three-by-three rook graph but excluding the empty-vacuum signed Dirac carrier LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive impurity, Klein and antisymmetric Fock Hilbert pairing; operator-graph pullback by the nilpotent boundary transform and positive closed-form pullback for Coulomb ON=repository_complete_positive_point_control
real_structure: CAR adjoint, complex conjugation in momentum and impurity bases, Hermitian diagonal endpoint subtraction and Hermitian finite regular remainder W_min
grading: matrix units are even, Klein and CAR fields are odd, defect monomials are even, and point creation strictly lowers the ordered impurity label; on the actual rook graph every fifth creation word vanishes
action_owner: repository-construction -- graph orientation, positive dispersion, sharp symmetric regulator, subtraction scale, finite impurity energy, couplings, polarization, Coulomb interval/domain and state are not selected by Weinstein's source or a GU action
target: complete positive-graph minimal point-Fock norm-resolvent limit, exact divergent-counterterm census, scheme-selected finite extension coordinate and raw all-sector Coulomb/Gauss limit MAP-TYPE=not-a-map
```

## Inline preflight bookend

K136 supplied the depth-two recursion base but deliberately excluded the full
graph. The new route-changing objects are the six row/column triangles and
nine rectangular four-cycles of the K115 product graph. They can either create
a new divergent off-diagonal/higher-order counterterm or only a finite regular
remainder. That discriminator precedes the complete Schur recursion and the
minimal Coulomb successor.

Mechanism retrieval found K127's physical matrix units, K134's diagonal
vacuum contraction and nilpotent IBC map, K135's operator-graph exchange
limit, and K136's uniform two-edge inverse/tail estimates. It found no prior
complete-graph minimal theorem or raw minimal Coulomb limit. No correction
entry supersedes those inputs.

The specialist census covered CAR pull-through and Pauli vacancy, finite
directed-graph filtrations, operator-valued Schur/Feshbach maps, IBC/boundary
triples, ultraviolet power counting, graph-relative convergence, finite
renormalization coordinates, particle-number graph norms, positive Coulomb
forms, signed-Dirac polarization, thermodynamic scattering, source ownership
and hostile claim audit. The primary route is not a brute-force cutoff matrix:
it is the exact finite impurity-label filtration, with computation used only
to enumerate its paths and test the analytic tail bounds.

## 1. The complete graph has a shorter exact filtration than K134 used

Write the nine impurity states as `(x,r) in {0,1,2}^2`, in lexicographic order.
Two vertices are connected exactly when one coordinate agrees. This is the
three-by-three rook graph: it has eighteen undirected edges, six `K3`
triangles and nine rectangular four-cycles. Orient each edge `e=(u,v)` by
`u<v`, and retain K127's

```text
B_e = |v><u| tensor kappa_e,
A_N = sum_e g_e B_e tensor a_e(delta_N),
G_N = -R_mu A_N*.                                      (1)
```

Creation in `G_N` maps `|v>` to `|u>` and strictly lowers the impurity label.
For the actual rook graph the directed path counts at lengths one through
four are `18,24,18,6`, and there is no length-five path. Hence

```text
G_N^5=G^5=0,
U_N^-1=(1-G_N)^-1=sum_(j=0)^4 G_N^j.                   (2)
```

This sharpens K134's graph-independent safe bound `G^9=0`. More importantly,
(2) includes rather than deletes all triangle, square and multiply convergent
paths. The complete graph is not replaced by a direct sum of K136 ladders.

## 2. Only the diagonal endpoint contraction diverges

Let `omega_k=sqrt(m^2+k^2)`, `m>0`, and let the cutoff be the fixed sharp
symmetric set `|k|<=N` in every species. CAR orthogonality gives

```text
<vac|a_e(k) a_f(l)*|vac>
  = delta_(e,f) delta_(k,l).                            (3)
```

Therefore the only one-loop vacuum divergence is

```text
c_N(mu) D_g,
c_N(mu)=sum_(|k|<=N) (omega_k+mu)^-1,
D_g=sum_(e=(u,v)) g_e^2 |v><v|.                        (4)
```

Its diagonal multiplicities for equal couplings are
`(0,1,2,1,2,3,2,3,4)`. No off-diagonal contraction survives (3), so neither
triangles nor rectangles can create a second logarithmic matrix counterterm.

Normal ordering every remaining word leaves two kinds of tails. A diagonal
subtracted contraction is bounded by

```text
sum_k |(omega_k+mu)^-1-(omega_k+X+mu)^-1|,              (5)
```

with K134's logarithmic-in-`X` relative bound. A normal-ordered exchange word
has one point-annihilation leg, controlled from `Dom(H_0)` by
`sum omega_k^-2<infinity` as in K135. Every further unconstrained momentum
comes from a `G_N` factor and therefore carries a resolvent coefficient in
`l2(Z)`. Since (2) leaves only finitely many words, products of these tails
form a finite operator ideal that is Cauchy in the `H_0` graph-relative norm.

The cycle terms do not vanish. Triangles, rectangles and exchange paths leave
finite Hermitian off-diagonal and occupation-dependent remainders. What
vanishes is only their divergent part. Thus the discriminator returns:

```text
additional divergent counterterm beyond c_N D_g: NONE;
finite overlap remainder: NONZERO.                     (6)
```

## 3. Complete minimal-cutoff norm-resolvent convergence

Let

```text
H_N^min = H_0 + A_N + A_N* + E_R + c_N(mu)D_g          (7)
```

on the complete positive-energy Fock carrier. Add one common finite scalar
shift, independent of `N`. On the finite-support core, pull (7) through (2):

```text
K_N^min = (U_N*)^-1 H_N^min U_N^-1.                    (8)
```

The choice of `G_N` cancels the two naked singular linear terms. Equation (4)
cancels the only vacuum divergence. The finite expansion of (8) is then
`H_0` plus K134's diagonal Pauli/spectator remainder, K135's adjoint-paired
graph exchange, and the finitely many triangle/rectangle words from (2).
Equations (3)--(6), the low/high spectator split of K134 and K136's uniform
inverse estimate give

```text
||(K_N^min-K_M^min)(H_0+1)^-1| -> 0,                   (9)
```

with an arbitrarily small relative bound after a uniform finite shift. Hence
the `K_N^min` are self-adjoint on the common `Dom(H_0)`, uniformly bounded
below, and converge in norm resolvent to a regular `K_min`.

Meanwhile `G_N->G` in norm, and the finite polynomial (2) makes
`U_N^-1->U^-1` in norm. Inverse factorization at the common positive shift,

```text
(H_N^min)^-1
 = U_N^-1 (K_N^min)^-1 (U_N*)^-1,
```

therefore converges in operator norm to

```text
(H_min)^-1=U^-1 K_min^-1 (U*)^-1.                      (10)
```

This is norm-resolvent convergence of the **complete** nine-state/eighteen-
species minimally countertermed positive-energy cutoff on full antisymmetric
Fock space, including arbitrary finite-particle spectators and every
overlapping Pauli path. It closes the exact problem K136 fenced. It does not
apply to the empty-vacuum signed Dirac generator, whose cutoff lower bound
still diverges downward.

## 4. What the minimal scheme selects

Comparison of (8) with K135's regular family writes

```text
K_min = K_0 + W_min(mu, sharp symmetric cutoff, E_R, g). (11)
```

The nonzero finite triangle, square and exchange remainders determine one
Hermitian `W_min` for those fixed choices. Thus the minimal cutoff is one
member of K135's dressed extension family; K135's abstract `W` was not
spurious.

Changing `mu` changes `E_R` and the coordinate of `W_min` by K136's absolutely
convergent finite `D_g` flow while leaving the same bare family unchanged.
Changing regulator or finite subtraction convention can likewise change the
finite remainder. K137 proves neither regulator independence nor a physical
principle preferring this member. “The minimal prescription selects
`W_min`” is a mathematical scheme statement, not source/GU ownership or
physical uniqueness.

## 5. The raw all-sector Coulomb form also survives the limit

K136 proved on the finite interval

```text
0 <= Coul <= C_L(F_root^2+(N_f+1)^2),
(N_f+1)^2 <= C_r(H_f+1).                               (12)
```

For fermionic creation, `[N_f,G_N]=G_N`. The `l2` resolvent coefficient and
finite graph sum imply that `G_N->G` not only in Hilbert norm but also as
bounded maps on the particle-number graph. Equation (2) gives the same for
`U_N^-1`. Consequently the **raw** form `Coul[psi]`, which is defined on
`Dom(N_f)`, is defined on the singular minimal IBC form domain, and

```text
Coul[U_N^-1 phi] -> Coul[U^-1 phi]                     (13)
```

in form norm relative to the regular free/global-flux form. This argument
uses particle-number control, not false commutation between momentum
occupation and position-space Coulomb multiplication.

Adding (13) to the regular forms of (8) gives one common uniformly
semibounded form domain and norm-resolvent convergence. Pulling back yields

```text
H_N^(min,C)=H_N^min+Coul -> H_min^C                    (14)
```

in norm resolvent. Unlike K136's dressed Coulomb family, (14) adds the raw
finite-interval K128/K131 cumulative-charge form to the original minimal
cutoffs. The result remains finite-volume and positive-energy. No constant in
(12) is claimed uniform as the interval grows.

## Inline postflight bookend

- **Strongest advance:** the diagonal endpoint subtraction suffices for the
  complete positive-energy rook graph, and both the bare minimal point cutoff
  and its raw all-sector finite-interval Coulomb/Gauss addition converge in
  norm resolvent.
- **Strongest structural correction:** K134's `G^9=0` is valid but nonsharp;
  the actual rook graph has `G^5=0`. Its six triangles and nine rectangles are
  retained as finite `W_min` data rather than erased as disjoint ladders.
- **Strongest overclaim:** “the physical K127 Hamiltonian is now unique.”
  Refused. The theorem fixes one positive-energy finite-circle regulator and
  subtraction scheme; it neither selects the signed sea nor proves regulator-
  independent physical extension data.
- **Strongest contrary route:** another regulator or finite subtraction can
  land at a different member of the K135 family. K137 identifies this as the
  remaining finite renormalization comparison; it does not assume universality.
- **Weakest propagation seam:** the raw Coulomb theorem can be misread as
  infinite-volume or smooth unreduced gauge control. Its proof uses the
  finite-interval number bound and K131's reduced physical carrier only.

The companion control passes 36/36 and its baseline-first hostile selftest
catches 37/37 mutations. No empty-vacuum signed-Dirac polarization,
regulator-independent physical `W`, infinite-volume limit, Moller/Ruelle wave
operator, interacting NESS/current, smooth unreduced gauge parent,
Weinstein/source/GU action, Born rule, held-out score, prediction,
confirmation, canon, paper, release or public-posture move follows.

## Next condition

Compare at least two admissible regulators or finite subtraction conventions
and compute the finite `W_min` difference on the complete graph. A physical
point Hamiltonian requires an owner-native action, symmetry or scattering
condition that selects one equivalence class rather than merely one scheme.
Independently choose and validate a signed-Dirac sea/polarization, sea charge,
normal ordering and defect particle/hole split, then redo the lower-bound and
Coulomb estimates. Only after one physical infinite-volume point-Fock/Gauss
operator has a thermodynamic limit should Moller/Ruelle or return-to-NESS
work compare its current with K115. A genuinely unreduced smooth connection/
BRST parent and source/GU ownership remain separate requirements.

## Reproduction

```bash
python3 tests/channel-swings/k137_complete_graph_minimal_cutoff_extension_coulomb_probe.py
python3 tests/channel-swings/k137_complete_graph_minimal_cutoff_extension_coulomb_probe.py --selftest
```
