---
title: "K134 K133 Pauli spectator IBC core and exchange boundary"
status: active_research
doc_type: conditional_physical_point_fock_ibc_boundary_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned K127 matrix-unit/Klein/CAR coupling algebra on a diagonal-impurity positive-energy finite-circle control, with a positive diagonal endpoint counterterm distinct from K133's weighted-Laplacian incidence control, occupation-projection-valued self-energy for commuting free/global-flux spectators with infinitesimal logarithmic and Pauli energy bounds, and one dense Pauli-compatible full-Fock IBC boundary core from a norm-convergent nilpotent creation map; this is not the full signed-Dirac K127 operator, the normal-ordered exchange term retains an H1/2-discontinuous point-annihilation trace and the physical Coulomb form does not commute with momentum occupation, so no complete self-adjoint nine-state/eighteen-species point-Fock/Gauss Hamiltonian, infinite-volume NESS/current, smooth unreduced parent, Weinstein/source/GU ownership, Born derivation, prediction or confirmation follows
manifest: lab/process/k134-k133-pauli-spectator-ibc-exchange-boundary-wave.json
probe: tests/channel-swings/k134_k133_pauli_spectator_ibc_exchange_boundary_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K134 K133 Pauli/spectator IBC core and exchange boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) 126
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> lab/methods/source-native-comparator-routing.md and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet returns from K133's stipulated incidence star to K127's
actual repository-owned matrix-unit/Klein/CAR **coupling algebra**, placed on
K132's positive-dispersion finite-circle branch with a diagonal renormalized
impurity energy. It constructs the resulting matrix-unit vacuum contraction, the commuting occupation/spectator
self-energy and a dense Pauli-compatible IBC **boundary core** on the complete
antisymmetric positive-branch Fock carrier. This is not the full signed-Dirac
K127 operator. It then proves that the diagonal construction is
not the whole self-energy: normal ordering leaves an exchange trace outside
the critical free form topology. No complete self-adjoint point-Fock/Gauss
Hamiltonian is claimed.

```gu-typed-objects
result: the K127 matrix-unit/Klein/CAR coupling algebra on a diagonal-impurity positive-energy finite-circle control has a positive diagonal endpoint counterterm rather than K133's incidence Laplacian; its commuting vacuum-plus-Pauli spectator contraction and nilpotent boundary creation map admit infinitesimal energy bounds and one dense full-Fock IBC boundary core, but the remaining normal-ordered exchange trace is not continuous on the critical H1/2 form domain and the full signed-Dirac and noncommuting Coulomb lifts stay open
carrier: C9 tensor C512 tensor Gamma_minus(direct_sum over eighteen positive-dispersion l2(Z) species), optionally tensored with a commuting nonnegative global-flux spectator; this is not the full C2 signed-Dirac K127 operator and the K131 position/Coulomb carrier is not included in the commuting theorem LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive impurity, Clifford-Klein and antisymmetric Fock Hilbert pairing, with joint spectral calculus only for the free occupation and commuting global-flux operators ON=repository_physical_matrix_unit_point_control
real_structure: CAR adjoint, complex conjugation in the Fourier and impurity bases, Hermitian impurity energy and real nonzero edge couplings
grading: each matrix unit is even, each Clifford-Klein generator and CAR field is odd, and every defect monomial is even; the IBC creation map raises CAR number while strictly lowering the ordered impurity label
action_owner: repository-construction -- the orientation, couplings, subtraction scale, vacuum representation, IBC transform and spectator split are supplied controls, not selected by Weinstein's source or a GU action
target: physical ultraviolet counterterm, occupation/spectator self-energy, common Pauli IBC boundary core and exact exchange/Coulomb closure boundary MAP-TYPE=not-a-map
```

## Inline preflight bookend

K133 proved a matrix point limit for a deliberately supplied incidence
coupling. Its own boundary said that this star carrier was not proved invariant
under K127's full CAR defect. Retrieval of K127 resolves the first typing gate:

```text
B_e = |v><u| tensor kappa_e,
V_N = A_N + A_N*,
A_N = sum_e g_e B_e tensor a_e(1_{|k|<=N}).              (1)
```

This is not the incidence column `|v>-|u>`. The route census therefore
separated: (a) physical vacuum contraction; (b) diagonal Pauli/spectator
functional calculus; (c) the singular creation/IBC transform; (d) the
normal-ordered exchange term; (e) the noncommuting Coulomb/Gauss lift; and (f)
thermodynamic scattering. The first four are ready on the finite circle. The
Coulomb lift depends on their result. Infinite volume remains downstream.

The problem-matched lenses were CAR algebra and antisymmetric Fock space,
singular operator extensions, graph/matrix-unit typing, spectral functional
calculus, relative-bound analysis, reduced gauge/Coulomb domains, open-system
thermodynamic representations, source fidelity and hostile claim audit. The
cheapest kill was equality of the physical counterterm with K133's Laplacian;
the cheapest closure was a jointly diagonal Pauli/spectator self-energy plus a
common boundary transform. No correction-registry entry supersedes K127,
K128, K131 or K133.

## 1. The physical counterterm is diagonal, not the K133 Laplacian

Let every undirected K115 edge be oriented `u<v`, as in the control, and take
`B_e=|v><u| tensor kappa_e`, with `kappa_e^2=1`. Let

```text
H_0 = E_R + dGamma(omega) + S,
omega_k = sqrt(m^2+k^2),  m>0,  S>=0,                     (2)
```

where `E_R` is diagonal in the ordered vertex basis and this section assumes
that `S` strongly commutes with the CAR occupation projections. The diagonal
assumption is load bearing: it makes the resolvent preserve the vertex label.
Put `R_mu=(H_0+mu)^-1`, `mu>0`. Completing the square
at cutoff `N` isolates `A_N R_mu A_N*`. Its vacuum contraction has divergent
coefficient

```text
D_g c_N,
D_g = sum_e g_e^2 B_e B_e* = sum_e g_e^2 |v(e)><v(e)|,
c_N = sum_{|k|<=N} 1/(omega_k+mu).                        (3)
```

Thus `D_g` is positive and diagonal in the impurity endpoint basis. With the
chosen increasing orientation it has rank eight: vertex zero has no incoming
edge and every other vertex has at least one. This rank statement is a control
property of the chosen orientation, not a source law.

K133 instead used

```text
L_g = sum_e g_e^2 (|v>-|u>)(<v|-<u|),                    (4)
```

which has nonzero off-diagonal entries and the constant-vector kernel. Equations
(3) and (4) are different operators because they arise from different
couplings. The K133 star remains a valid matrix existence model, but its
Laplacian counterterm cannot be transferred to (1).

## 2. Exact occupation-projection spectator self-energy

On a joint occupation/spectator eigenvector, let `X>=0` denote the free energy
of the particles already present plus the commuting spectator energy, and let
`N_{e,k}` be the CAR occupation projection. The diagonal contraction after the
vacuum subtraction is

```text
Q_e(X) = sum_k [
  (1-N_{e,k})/(X+omega_k+mu) - 1/(omega_k+mu)
].                                                        (5)
```

This is the exact Pauli content of the contraction term. It decomposes as

```text
Q_e(X) = q(X) - sum_k N_{e,k}/(X+omega_k+mu),
q(X) = sum_k [1/(X+omega_k+mu)-1/(omega_k+mu)].           (6)
```

The summand in `q(X)` is `O(X |k|^-2)` at fixed `X`, so the series converges.
Integral comparison gives

```text
q(X) = -2 log(1+X) + O(1).                               (7)
```

For every `epsilon>0`, `log(1+X)<=C_epsilon+epsilon X`.
Hence the unbounded logarithm is infinitesimally form bounded by `X`; K133's
failure of uniform operator boundedness is not a form obstruction.

The Pauli term has the same relative grade. Split occupied modes at `|k|=K`.
The low block contains at most `18(2K+1)` projections and is bounded. On the
high block,

```text
sum_{e,|k|>K} N_{e,k}/omega_k
 <= K^-2 sum_{e,|k|>K} omega_k N_{e,k}.                   (8)
```

As `K` grows, the relative coefficient tends to zero. Equations (5)--(8)
therefore define an occupation-projection-valued self-energy, infinitesimally
form bounded by free plus commuting spectator energy. Finite Pauli occupation
changes a finite, mode-dependent remainder exactly as K133 anticipated.

The eight global-flux energies may be included in `S` because they act on a
separate tensor factor and strongly commute with every `N_{e,k}`. This is not
yet the K128/K131 Coulomb lift.

## 3. One dense Pauli-compatible full-Fock IBC boundary core

The point creation map is singular, but its resolvent dressing is bounded:

```text
G_N = -R_mu A_N*,
sum_k (omega_k+mu)^-2 < infinity.                         (9)
```

The cutoff maps are Cauchy in norm, giving `G=lim_N G_N` on the complete
antisymmetric Fock carrier. CAR creation itself inserts the vacancy factor, so
creation into an occupied `(e,k)` mode vanishes without an added rule.

There is a second finite-graph advantage. `A_N*` contains `B_e*`, which maps
`|v>` to `|u>` with `u<v`. Resolvents and occupation factors preserve the
impurity label. Every nonzero product of boundary creations therefore strictly
lowers that label at each step, and

```text
G^9=0,
(1-G)^-1 = 1+G+...+G^8.                                  (10)
```

No small-coupling assumption is needed for this inverse. If `C_fin` is the
usual finite-particle, finite-momentum-support core of `H_0`, then

```text
C_IBC = (1-G)^-1 C_fin                                   (11)
```

is dense, Pauli compatible and still has finite particle support because the
inverse in (10) is a finite polynomial. Its sector recursion is

```text
(omega_k+X+mu) psi_{n+1}(...,e,k)
 -> -g_e B_e* psi_n(...)                                 (12)
```

with the ordinary CAR insertion sign and zero right side for an already
occupied mode. Equation (12) holds for every finite-particle sector on one
common boundary core. This constructs the missing IBC **boundary geometry**;
it does not by itself prove that the full renormalized Hamiltonian is closed
or self-adjoint on (11).

## 4. Normal ordering leaves an exchange trace outside the form topology

Using `a_e(k)a_f(l)*=delta_ef delta_kl-a_f(l)*a_e(k)` splits
`A_N R_mu A_N*` into the diagonal contraction (5) and normal-ordered exchange
terms. For `e,f,k,l`, the latter contain

```text
B_e B_f* a_f(l)* a_e(k)
```

with a resolvent denominator on the created leg. The sum over the annihilated
existing momentum still contains the point functional

```text
tau(phi)=sum_k phi(k).                                    (13)
```

It is not continuous on the critical `H^(1/2)` free form domain. Indeed, with

```text
s_N=sum_{|k|<=N} omega_k^-1,
phi_N(k)=1_{|k|<=N}/(omega_k sqrt(s_N)),                  (14)
```

one has `sum omega_k |phi_N(k)|^2=1` while
`tau(phi_N)=sqrt(s_N)` diverges logarithmically. Adding one fixed regular mode
keeps the resolvent-weighted created-leg functional nonzero, so the exchange
bilinear itself diverges on a bounded form-norm sequence. The probe checks
this hostile mixed sequence directly.

The point trace is continuous on the stronger free **operator** graph domain,
because

```text
|tau(phi)|^2 <= (sum_k omega_k^-2)(sum_k omega_k^2|phi(k)|^2). (15)
```

Therefore the result is not a no-go for a point-Fock Hamiltonian. It is an
exact route boundary: equations (5)--(12) do not license a naive KLMN form
closure. A recursive operator-domain IBC definition, an exchange extension
theorem, or a different Feshbach/resolvent construction is still needed.

## 5. Global flux lifts; the physical Coulomb form does not follow

Global flux is a separate diagonal tensor factor, so (5)--(8) lift by joint
functional calculus. K128/K131 Coulomb energy is different: it is multiplication
by cumulative charge in position/configuration space, whereas `N_{e,k}` is a
momentum-occupation projection. These operators do not strongly commute. A
two-mode Fourier control already has a nonzero commutator between momentum
occupation and a nonconstant position multiplier.

Consequently, replacing `X` in (5) by the Coulomb Hamiltonian is not an exact
derivation. The physical Gauss/Coulomb point lift requires commutator-resolvent
estimates or a position-space IBC analysis that also closes the exchange term.
The smooth unreduced connection/BRST parent remains separately absent.

## Inline postflight bookend

- **Strongest overclaim:** “K134 constructs the complete point-Fock
  Hamiltonian.” Refused. It constructs the exact physical contraction, its
  commuting Pauli/spectator functional calculus and a common IBC boundary
  core; exchange closure and the Coulomb lift remain open.
- **Strongest typing correction:** K133's incidence coupling and K127's
  matrix-unit coupling are different. Their weighted-Laplacian and diagonal
  endpoint counterterms must not be merged.
- **Strongest contrary route:** a direct operator-domain IBC or Feshbach
  construction may control the exchange term because (15) holds. The present
  form obstruction does not kill that route.
- **Strongest representation boundary:** K122's thermodynamic quasifree leads
  are not automatically the vacuum Fock representation used for the point
  counterterm. A thermodynamic GNS point limit requires separate work.
- **Weakest reproducibility seam:** finite cutoffs can hide both the logarithmic
  spectator growth and the critical exchange trace. The probe tests increasing
  cutoffs, planted trace regularization, Pauli erasure, counterterm mistyping,
  nilpotence, global-flux commutation and Coulomb noncommutation separately.

The exact control passes 45/45 and the baseline-first hostile selftest catches
35/35 mutations. No complete self-adjoint physical point-Fock/Gauss
Hamiltonian, infinite-volume scattering, interacting NESS/current, smooth
unreduced parent, source/GU action, Born rule, held-out score, prediction,
confirmation, canon, paper, release or public-posture move follows.

## Reproduction

```bash
python3 tests/channel-swings/k134_k133_pauli_spectator_ibc_exchange_boundary_probe.py
python3 tests/channel-swings/k134_k133_pauli_spectator_ibc_exchange_boundary_probe.py --selftest
```
