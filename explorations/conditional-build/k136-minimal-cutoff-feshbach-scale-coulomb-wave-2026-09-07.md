---
title: "K136 minimal-cutoff Feshbach, scale selection, and all-sector Coulomb wave"
status: active_research
doc_type: conditional_minimal_cutoff_recursive_feshbach_and_all_sector_coulomb_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned positive-dispersion finite-circle results proving norm-resolvent convergence of a two-edge restriction of the minimally countertermed K127 physical matrix-unit coupling algebra on one nontrivial depth-two CAR ladder, identifying subtraction-scale flow and a finite Schur boundary value as the renormalization condition selecting the corresponding extension datum, and using finite-species Pauli filling to lift K135's dressed Coulomb/Gauss completion to all Fock sectors; the complete nine-state/eighteen-species minimal cutoff, minimally countertermed Coulomb cutoff, unique physical W, signed-Dirac polarization, infinite-volume NESS/current, smooth unreduced parent, Weinstein/source/GU ownership, Born derivation, prediction and confirmation remain open
manifest: lab/process/k136-minimal-cutoff-feshbach-scale-coulomb-wave.json
probe: tests/channel-swings/k136_minimal_cutoff_feshbach_scale_coulomb_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K136 minimal-cutoff Feshbach, scale selection, and all-sector Coulomb wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) 126
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> lab/methods/source-native-comparator-routing.md and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet stays on K134--K135's repository-owned positive-dispersion
finite-circle matrix-unit/Klein/CAR control. It proves the first genuinely
recursive minimally countertermed limit on one invariant ladder of the
declared two-edge restriction,
and closes the particle-number growth estimate required for the **dressed**
all-sector Coulomb form. It does not extend the ladder proof to every
overlapping path in the complete nine-state graph, identify a physical finite
extension, or treat the empty-vacuum signed Dirac operator.

```gu-typed-objects
result: the two-edge restriction of the minimally countertermed physical matrix-unit coupling algebra converges in norm resolvent on a nontrivial depth-two CAR ladder; subtraction scale and a finite Schur boundary value parameterize rather than physically select the finite extension; finite-species Pauli filling lifts the positive-energy dressed Coulomb/Gauss completion to all Fock sectors
carrier: the invariant ladder C|2,vac> direct-sum l2(Z)|1;b_k> direct-sum l2(Z2)|0;a_l b_k> for the minimal-cutoff theorem, and C9 tensor C512 tensor Gamma_minus(direct_sum over eighteen positive-dispersion l2(Z) species) tensor l2(Z8) for the dressed Coulomb theorem LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive impurity, Klein and antisymmetric Fock Hilbert pairing; nested Schur complements at one common lower resolvent point and positive closed-form addition for Coulomb ON=repository_positive_energy_point_control
real_structure: CAR adjoint, complex conjugation in momentum and impurity bases, Hermitian diagonal endpoint counterterm and finite Hermitian Schur boundary datum
grading: matrix units are even, Klein and CAR fields are odd, defect monomials are even, and boundary creation strictly lowers the ordered impurity label while increasing particle number
action_owner: repository-construction -- point couplings, subtraction scale, finite Schur boundary value, positive dispersion, Dirac polarization, charge normalization, Coulomb domain and state are not selected by Weinstein's source or a GU action
target: depth-two minimal-cutoff resolvent limit, finite renormalization selection condition, Pauli number-energy coercivity and all-sector dressed Coulomb/Gauss completion MAP-TYPE=not-a-map
```

## Inline preflight bookend

K135 produced a family of self-adjoint dressed completions but left two
different questions open: whether the **minimal** cutoff converges, and whether
the fixed-particle Coulomb estimate can be made uniform over Fock space. The
first question is recursive rather than one-channel; the second is a Pauli
filling problem rather than a momentum/Coulomb commutator problem.

Mechanism retrieval found K132's scalar one-edge Schur theorem, K134's physical
diagonal endpoint counterterm and K135's graph-domain exchange/dressed family.
It found no depth-two nested minimal-cutoff theorem and no finite-species
particle-number coercivity application to the Coulomb form. No correction
entry supersedes K127, K128, K131, K132, K134 or K135.

The route census covered nested Feshbach maps, Herglotz resolvents,
self-adjoint extensions, subtraction-scale flow, finite-volume fermionic
spectral counting, positive form sums, reduced-gauge Coulomb energy,
signed-Dirac polarization, thermodynamic limits, source ownership and hostile
claim audit. The smallest route-changing minimal-cutoff discriminator is a
two-edge ordered ladder: unlike K132, it has a genuine inner Schur denominator
whose spectator momentum is integrated by an outer point coupling. The
Coulomb route uses occupation-basis spectral counting; it never assumes the
false commutation rejected by K134.

## 1. A nontrivial depth-two physical ladder

Choose two K134 physical edges `a=(0,1)` and `b=(1,2)` with nonzero real
couplings `g_a,g_b`, and restrict the interaction to those two edges. The
resulting Hamiltonian leaves invariant

```text
H_lad = C |2,vac>
        direct-sum l2(Z) {|1;b_k>}
        direct-sum l2(Z^2) {|0;a_l b_k>},                (1)
```

The other sixteen K127 couplings are not asserted to vanish physically; this
is an exact two-edge control, and (1) is not proved invariant under the full
defect. All cutoffs act on the same `H_lad`: modes outside `|k|<=N` retain
their free action and only the two point couplings are cut off. Let
`omega_k=sqrt(m^2+k^2)`, `m>0`, and

```text
c_N(mu)=sum_(|j|<=N) 1/(omega_j+mu),  mu>0.              (2)
```

The only counterterm is K134's physical diagonal endpoint term: the middle
block receives `g_a^2 c_N`, the top block receives `g_b^2 c_N`, and the bottom
block receives none. After one harmless common positive shift, `z=-1` lies in
every cutoff resolvent set.

Eliminating the bottom block gives one diagonal inner Schur denominator for
every spectator momentum `k`:

```text
d_(k,N) = E_1+omega_k-z
          +g_a^2 sum_(|l|<=N) [1/(omega_l+mu)
             -1/(E_0+omega_l+omega_k-z)].                (3)
```

For fixed `k`, the summand is `O((1+omega_k) omega_l^-2)` and the sum
converges absolutely. Absolute convergence is not uniform for the raw
denominators when `k` also tends to infinity; the resolvent factor is the
correct object. Positivity gives `d_(k,N)>=c(1+omega_k)`. Splitting the tail at
`|l|=omega_k` yields

```text
sup_k |d_(k,N)^-1-d_k^-1| -> 0.                          (4)
```

The lower resolvent-dressed coupling is a direct sum over `k`, with tail norm
bounded by

```text
sup_k [sum_(|l|>N)(E_0+omega_l+omega_k-z)^-2]^(1/2)
 <= C N^-1/2.                                            (5)
```

The outer Schur complement is

```text
s_N(z)=E_2-z+g_b^2 sum_(|k|<=N)
       [1/(omega_k+mu)-1/d_(k,N)].                       (6)
```

Equations (3)--(4) give
`d_(k,N)=omega_k+O(log(2+omega_k))` on the diagonal
`|k|<=N`, hence the summand in (6) is
`O(log(2+|k|)/k^2)`. It is absolutely summable. The outer resolvent-dressed
vector has coefficients `d_(k,N)^-1`, dominated by `C/(1+omega_k)` in
`l2(Z)`. The block inverse formula, (4)--(6), and convergence of the free
bottom resolvent therefore make **every block** of the ladder resolvent
Cauchy in operator norm. Thus

```text
H_(lad,N) -> H_lad  in norm resolvent.                   (7)
```

This is the first recursive minimally countertermed result beyond K132's
one-edge star within a restriction of the physical coupling algebra: one
point-created particle is a genuine spectator inside a second renormalized
point denominator. It is not the complete K127 theorem. The
complete graph has several incoming and outgoing edges at each impurity level,
overlapping CAR paths and operator-valued Schur blocks. Equation (7) supplies
the recursion base and tail mechanism, not uniform control of that full
operator-valued recursion.

## 2. What actually selects the finite extension

For two subtraction scales `mu,nu>0`,

```text
Delta_(mu,nu)=sum_k [1/(omega_k+mu)-1/(omega_k+nu)]       (8)
```

converges absolutely. The same bare cutoff family is represented at the new
scale by

```text
E_R(nu)=E_R(mu)+Delta_(mu,nu) D_g.                        (9)
```

The sign in (9) is fixed by keeping `E_R+c_N D_g` unchanged as the subtraction
coordinate changes. Thus the subtraction scale labels coordinates on the
finite extension family; it is not a physical selector.

At a fixed common resolvent point `z_0`, the finite matrix Schur function has
the form

```text
S_W(z_0)=S_0(z_0)+W.                                    (10)
```

Prescribing the Hermitian boundary value `S_phys(z_0)` selects exactly
`W=S_phys(z_0)-S_0(z_0)` on the declared finite boundary subspace. Equivalent
conditions may fix bound-state poles, scattering length or another complete
finite set of extension observables. K135's ultraviolet tail supplies none of
those values. No source-owned action or physical measurement in the repository
currently supplies `S_phys`; (10) identifies the missing datum without
pretending to derive it.

## 3. Pauli filling controls particle number squared

Let `r=18` be the finite number of positive-dispersion species. Arrange all
one-particle energies on the circle, including species multiplicity, as
`lambda_1<=lambda_2<=...`. Since there are at most `r(2K+1)` modes with
`|k|<=K`,

```text
lambda_j >= c j/r-C,
sum_(j=1)^n lambda_j >= c n^2/r-Cn.                      (11)
```

Every fermionic occupation configuration therefore satisfies, after adjusting
one finite constant,

```text
(N_f+1)^2 <= C_r (dGamma(omega)+1)                       (12)
```

as an exact diagonal quadratic-form inequality. This is the missing use of
Pauli exclusion: the linear `H_f>=m N_f` bound would not control K135's
quadratic fixed-particle constant.

On a finite interval, the K128/K131 cumulative charge field obeys

```text
Coul <= C_L (F_root^2 + q_max^2 (N_f+1)^2).              (13)
```

Combining (12)--(13) makes the positive Coulomb form bounded on the form
domain of free positive kinetic plus global-flux energy over **all** Fock
sectors. No momentum-position commutator is used or needed. This bound depends
on finite volume and finite species multiplicity. It does not extend uniformly
to the thermodynamic limit, and it is false as a coercive statement for the
empty-vacuum signed Dirac generator whose negative sea energy is unbounded
below.

## 4. The all-sector dressed Coulomb/Gauss completion

Let `K_(W,N)` be K135's positive shifted regular cutoff operator. Its symmetric
exchange/occupation terms converge in relative graph norm and therefore in
the corresponding sandwiched form norm. The closed positive Coulomb form from
(13) is bounded on the common free/global-flux form space. Hence

```text
k_(W,N)^C = k_(W,N) + Coul                               (14)
```

is closed and uniformly semibounded on one all-sector form domain, and the
associated regular operators `K_(W,N)^C` converge in norm resolvent to
`K_W^C`. Adding the same positive form to every cutoff does not require it to
commute with the momentum occupations.

K134's `U_N=1-G_N` converge in norm to boundedly invertible `U=1-G`. Define

```text
L_(W,N)^C = U_N* K_(W,N)^C U_N,
L_W^C     = U* K_W^C U.                                 (15)
```

After the common positive shift, inverse factorization gives

```text
(L_(W,N)^C)^-1
 = U_N^-1 (K_(W,N)^C)^-1 (U_N*)^-1
 -> U^-1 (K_W^C)^-1 (U*)^-1                            (16)
```

in operator norm. This constructs self-adjoint dressed Coulomb/Gauss point
completions on all positive-energy Fock sectors. It strictly upgrades K135's
fixed-particle result.

The qualifier **dressed** remains load bearing. Equation (16) does not prove
that the minimally countertermed Coulomb cutoff converges, and every finite
Hermitian `W` remains available. The all-sector estimate closes a domain and
growth gate; it does not select a physical Hamiltonian.

## Inline postflight bookend

- **Strongest advance:** the physical minimal cutoff now converges on a
  nontrivial recursive two-edge ladder, and Pauli filling closes the all-sector
  positive-energy dressed Coulomb/Gauss domain.
- **Strongest overclaim:** “K127's complete minimally countertermed point
  Hamiltonian is constructed.” Refused. Overlapping-path operator-valued
  Schur recursion is not controlled by the ladder theorem.
- **Strongest selection boundary:** scale covariance gives the finite running
  (9), while a finite Schur boundary value (10) selects `W`. Neither supplies
  the physical value of that condition.
- **Strongest contrary route:** a boundary-triple or block-Jacobi theorem may
  close the full nine-level recursion without iterating ladder estimates. It
  remains open and is not excluded.
- **Weakest propagation seam:** all-sector **dressed** Coulomb closure can be
  mistaken for minimal-cutoff convergence or for an infinite-volume bound.
  The manifest and hostile probe require all three boundaries to remain
  explicit.

The companion control passes 33/33 and its baseline-first hostile selftest
catches 33/33 mutations. No uniquely selected complete physical point-
Fock/Gauss Hamiltonian, signed-Dirac polarization, infinite-volume scattering,
interacting NESS/current, smooth unreduced parent, source/GU action, Born rule,
held-out score, prediction, confirmation, canon, paper, release or public-
posture move follows.

## Next condition

Extend the nested Feshbach argument from the two-edge ladder to the complete
nine-level/eighteen-species ordered matrix-unit graph: prove uniform inverse
bounds and norm convergence for its operator-valued Schur recursion across
overlapping Pauli paths, or exhibit the first additional counterterm. Then
compare that minimal limit with the dressed `W` family and impose a physically
owned finite Schur/scattering condition. Separately determine whether the
all-sector dressed Coulomb form admits the same minimal-cutoff limit. A full
signed-Dirac result still requires a selected sea/polarization, normal ordering,
charge and defect split. Infinite-volume Moller/Ruelle or return-to-NESS work
remains downstream of one uniquely specified physical point-Fock/Gauss
operator; source/GU credit still requires an actual action selecting every
imported datum.

## Reproduction

```bash
python3 tests/channel-swings/k136_minimal_cutoff_feshbach_scale_coulomb_probe.py
python3 tests/channel-swings/k136_minimal_cutoff_feshbach_scale_coulomb_probe.py --selftest
```
