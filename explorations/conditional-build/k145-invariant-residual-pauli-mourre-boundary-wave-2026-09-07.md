---
title: "K145 invariant residual, Pauli, and Mourre boundary wave"
status: active_research
doc_type: conditional_signed_incidence_sector_obstruction_one_edge_invariant_residual_threshold_and_propagation_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned theorem that the supplied diagonal-W signed point-Fock control conserves an affine Z9 incidence charge and combined Klein-CAR parity, that every charge sector containing one genuinely bidirectional active edge is infinite and K144's vacuum-plus-one projection leaks, while the smallest one-edge particle-only charge sector is genuinely invariant and has one simple zero bound state, absolutely continuous spectrum [5/4,infinity) of multiplicity two, full Pauli threshold rank, vacuous dark compression, exact spectral Mourre estimates away from threshold, sharp square-root weighted threshold loss and uniform high-energy control; every single-cut periodic unwrapping retains the K143 seam obstruction; no complete bidirectional signed residual spectrum, nonvacuous dark denominator, full-Fock Mourre/Moller/Ruelle or NESS theorem, physical selector, smooth unreduced parent, Weinstein/source/GU action, Born derivation, prediction or confirmation follows
manifest: lab/process/k145-invariant-residual-pauli-mourre-boundary-wave.json
probe: tests/channel-swings/k145_invariant_residual_pauli_mourre_boundary_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K145 invariant residual, Pauli, and Mourre boundary wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet starts on K139--K144's repository-supplied positive
particle/hole point control. It proves the exact reducing charge that the full
signed interaction actually owns and the obstruction to turning K144's
projection into a finite residual sector. It then solves one deliberately
specialized one-edge, particle-only face on a genuine invariant charge sector.
That positive control is not the complete bidirectional signed Hamiltonian.

```gu-typed-objects
result: the diagonal-W signed point-Fock control has exact affine incidence-charge and combined-parity reductions but every genuinely bidirectional active-edge charge sector is infinite; its smallest one-edge particle-only invariant sector has a complete residual spectrum, full Pauli threshold rank, vacuous dark compression and exact threshold/Mourre/high-energy bounds, while every single-cut periodic unwrapping retains the seam obstruction
carrier: C9 tensor C512 tensor Gamma_minus of L2(R;C36) for the signed charge theorem, and the reducing C direct-sum L2(R) one-edge particle-only charge sector with its explicit Klein partner for the solved residual control LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive impurity, Klein and antisymmetric particle/hole Fock Hilbert pairing; standard scalar Friedrichs and spatially weighted resolvent pairings on the invariant control ON=repository_signed_point_control
real_structure: K140's supplied positive particle/hole conjugation is retained on the full charge theorem; the solved one-polarity face does not claim charge-conjugation closure or physical selection
grading: the full interaction preserves combined Klein-CAR parity and an affine Z9 incidence charge; the solved cyclic sector fixes one charge, one Klein seed, zero hole number and every inactive occupation
action_owner: repository-construction -- diagonal W, polarization, masses, screening, charges, couplings, one-edge restriction, subtraction, domain and state are not selected by Weinstein's source or a GU action
target: exact signed invariant-sector obstruction, minimal invariant residual spectrum, Pauli Gamma threshold, compressed denominator, spectral Mourre/weighted/high-energy boundary and single-cut periodic seam classification MAP-TYPE=intertwiner
```

## Inline preflight bookend

K144 solved a projected Friedrichs model, not an invariant part of the signed
Fock Hamiltonian. The first task is therefore to compute the symmetry before
computing another spectrum. Incidence charge supplies the exact reduction,
but a particle-hole pair on any bidirectional edge has zero net incidence
charge. This makes the fixed-charge carrier infinite and blocks a finite
residual enumeration.

Object retrieval found K136's invariant ladder only after a positive-only
interaction restriction, K138's surviving bidirected five-step path, K139's
full signed IBC limit, K143's structural residual-threshold rule and K144's
projected spectral solution. It found no complete signed charge-sector census
or invariant line-sector Mourre result. No correction-registry entry
supersedes these inputs. The primary route is exact charge algebra followed by
the smallest honest invariant face; a finite-cutoff diagonalization is
rejected because it cannot decide the infinite signed sector. The independent
topology packet tests every single-cut unwrapping before leaving multichart or
other topology-changing comparisons open.

## 1. The full signed operator has an exact affine incidence charge

Orient every rook edge `e=(u,v)` by `u<v` and put

```text
b_e=e_v-e_u in Z^9.                                    (1)
```

For impurity basis state `|x>` and particle/hole number operators define

```text
Q=e_x+sum_e b_e N_(e,+)-sum_e b_e N_(e,-).            (2)
```

The signed annihilation half is

```text
C=sum_e[g_(e,+) B_e a_(e,+)+g_(e,-) B_e* a_(e,-)],
B_e=|v><u| tensor kappa_e.                             (3)
```

`B_e a_(e,+)` changes `(e_x,N_(e,+))` by `(b_e,-1)`;
`B_e* a_(e,-)` changes it by `(-b_e,-1)`, and the hole
coefficient in (2) supplies the opposite sign. Their adjoints reverse both
changes. Hence every component of `Q` commutes with every cutoff Hamiltonian.
Diagonal `W`, the free energy, the diagonal endpoint subtraction and the
screened density interaction also commute with `Q`. The convergent K139--K142
resolvent/form limit therefore reduces by the same joint spectral projections.

Every state has `sum_j Q_j=1`; only eight differences are independent. The
Klein factor and a CAR field both change parity, so

```text
Pi_total=Pi_Klein (-1)^(N_++N_-)                       (4)
```

is conserved as well. Equations (2)--(4) are operator reductions, not
physical charge or sector selections.

## 2. Bidirectionality makes the exact charge sectors infinite

Take one active edge `e=(u,v)` with both polarities nonzero. In the sector
`Q=e_v`, choose any `n` mutually orthogonal particle orbitals and `n` mutually
orthogonal hole orbitals of that edge. Then both families

```text
|v; n_+=n,n_-=n>,
|u; n_+=n+1,n_-=n>                                    (5)
```

have charge `e_v` for every `n>=0`. The appropriate Klein-parity partner
keeps (4) fixed. Thus the exact `Q=e_v` block is infinite even before rook
cycles or other edges are used. The same argument applies to any charge block
connected to a genuinely bidirectional edge.

This also identifies K144's leakage. Starting from `|u,Omega>`, the adjoint
hole term creates `|v;1_->`. From there an allowed distinct particle or hole
creation along an incident edge produces a two-excitation state with the same
`Q` and total parity. Therefore

```text
[H,P_<=1] != 0                                         (6)
```

for the complete signed rook control. K144's nine projected zero modes are
not residual eigenvectors of the full Hamiltonian and may not be imported into
its HVZ threshold list.

## 3. The smallest genuine invariant residual family is exactly solvable

Now specialize rather than conceal the obstruction. Retain only
`e_0=(0,1)`, set `g_(e_0,+)=1`, set `g_(e_0,-)=0`, and set all other couplings
to zero. Fix

```text
m=kappa=|q|=1, positive self-inclusive screening,
subtraction energy 0, diagonal W=0.                    (7)
```

Freeze `Q=e_1`, zero holes, every inactive occupation and one unit Klein seed
`xi`. The exact reducing carrier is

```text
H_inv = C |1,xi,Omega>
        direct-sum L2(R){|0,kappa_(e_0)xi;
                          a*_(e_0,+)(psi)Omega>}.       (8)
```

The reverse interaction returns the second summand to the first because
`kappa_(e_0)^2=1`. Charge excludes every other particle number, so (8) is
invariant under the specialized full Fock Hamiltonian and its IBC domain, not
merely under a compression.

There is at most one matter excitation, hence no screened pair term. The
positive self energy gives

```text
epsilon(p)=sqrt(1+p^2)+1/4,   tau=5/4.                 (9)
```

The subtracted scalar Weyl function and Schur denominator are

```text
M(z)=integral_R dp/(2 pi)
     [1/(epsilon(p)-z)-1/epsilon(p)],
f(z)=-z-M(z).                                          (10)
```

For real `z<tau`,

```text
M(z)=z integral_R dp/(2 pi epsilon(p)(epsilon(p)-z)),  (11)
```

so `M` has the sign of `z`. Thus zero is the unique subthreshold root. Its
continuum tail is `-(2 pi)^(-1/2)/epsilon(p)`, which is square integrable.
For `E>tau`, put `w=E-1/4`; then

```text
Im M(E+i0)=w/sqrt(w^2-1)>0,                            (12)
```

excluding embedded roots. The explicit finite-rank boundary formula leaves
no singular-continuous support. Therefore

```text
sigma_p(H_inv)={0}, simple;
sigma_ac(H_inv)=[5/4,infinity), multiplicity 2;
sigma_sc(H_inv)=empty.                                 (13)
```

The two continuum branches are `p=+/-sqrt(w^2-1)`. Point coupling reaches the
even branch; the odd branch is exactly free. The resolvent difference from the
decoupled scalar comparison has rank at most two, so the invariant-sector wave
operators exist and are complete.

## 4. The first residual Pauli matrix is full rank

The compatible residual sector is `Q=e_0`, whose vacuum `|0,xi,Omega>` has
bound energy zero. The only admitted escape is one `e_0,+` fermion. Its
creation vacancy on the residual vacuum is

```text
1-N_(e_0,+)=1.                                         (14)
```

Consequently the threshold set and finite channel matrices are

```text
T={0+1+1/4}={5/4},
Gamma_tau=[1], D_tau=Gamma_tau Gamma_tau*=[1].          (15)
```

`ker D_tau=0`; the compressed dark denominator is `0 by 0` and its
invertibility test is vacuous. There is no threshold eigenvalue or
impurity-local dark resonance. Inactive channels are absent because (7)
specialized the Hamiltonian. They are not Pauli-blocked channels, a channel
kernel or a dark impurity space.

For a general residual Slater state with one-particle density projection
`gamma_res`, the exact creation availability of a normalized escape orbital
`h` is

```text
||a*(h)Phi_res||^2=<h,(1-gamma_res)h>.                 (16)
```

Equation (16) is the structural Pauli input to `Gamma_tau`; numerical signed
matrices still require the unknown full-sector residual eigenvectors. K145
does not manufacture them from K144.

## 5. Threshold, Mourre and high energy close on the invariant carrier

Set `a=1/4`, `w=z-a` and

```text
J(w)=integral_0^infinity dt/(cosh(t)-w).
M(z)=[w J(w)+a J(-a)]/pi.                              (17)
```

For `-1<w<1`,

```text
J(w)=2 atan(sqrt((1+w)/(1-w)))/sqrt(1-w^2),           (18)
```

while for `w>1` its upper boundary value is

```text
J(w+i0)=-arcosh(w)/sqrt(w^2-1)+i pi/sqrt(w^2-1).      (19)
```

Hence `M(tau-delta)~(2 delta)^(-1/2)` and
`|f(tau+delta+i0)^(-1)|~sqrt(2 delta)`. For

```text
J_s=diag(1,<x>^(-s)),  s>1/2,                         (20)
```

the explicit free kernel plus the rank-two resolvent formula gives

```text
sup_(z near tau) |z-tau|^(1/2)
 ||J_s P_c(H_inv-z)^(-1)P_c J_s|| < infinity.          (21)
```

The exponent is sharp because the odd branch stays free. Thus there is no
unweighted or threshold-uniform full-channel limiting-absorption estimate to
promote from the impurity cancellation.

In the explicit absolutely-continuous spectral representation, define

```text
A_sp=(b(E)i partial_E+i partial_E b(E))/2,
b(E)=(E-tau)/(1+E-tau).                                (22)
```

The vector field is complete on `(tau,infinity)` and

```text
[H_inv,i A_sp]=b(H_inv)                                (23)
```

on the continuous subspace. Every compact interval strictly above `tau` has
a positive strict Mourre constant and the standard `s>1/2` spectral-weighted
limiting-absorption estimate. This is an exact spectral Mourre statement for
(8), not an unproved `C^(1,1)` assertion for the full signed IBC domain.

As `E` tends to infinity, (19) gives

```text
Im M(E+i0)=1+O(E^-2),  Re M(E+i0)=O(log E),
f(E+i0)^(-1)=O(E^-1).                                 (24)
```

The impurity spectral density is `O(E^-2)`, and the spatially weighted full
resolvent in (20) is uniformly bounded for sufficiently large energy. The
full signed Hamiltonian still lacks residual eigenvectors, all `Gamma_tau`,
IBC commutator regularity and a sector-uniform high-energy estimate.

## 6. Recentring cannot remove the periodic seam

Let any single-cut unwrapping identify the length-`L` circle with one interval
of the line, with arbitrary cut position `c_L`. Place two fixed-width packets
on opposite sides of that cut at circular separation `r>0`. Their periodic
cross interaction tends to `Y_kappa(r)>0`; their line images are separated by
`L-r`, so the line interaction tends to zero. The packets retain bounded free
form norm. Therefore every single-cut identification obeys

```text
sup_(bounded form vectors)
 |E_(kappa,L)^periodic-E_kappa^line| not->0.            (25)
```

Changing or translating the cut only translates the witness. K143's
relative-form/norm-resolvent route cannot be repaired by recentering a single
fundamental cell. A genuinely multichart, enlarged-carrier or other
topology-changing comparison is a different open construction and is not
excluded by (25).

## Inline postflight bookend

- **Strongest advance:** the full diagonal-`W` signed operator now has an
  exact affine incidence-charge and combined-parity reduction, and every
  charge sector containing a bidirectional active edge is proved infinite.
- **Strongest correction:** K144's projected zero modes leak to higher Fock
  sectors and cannot be imported as full residual bound states.
- **Strongest positive control:** the one-edge particle-only `Q=e_1` carrier
  is genuinely invariant and has a complete simple-bound plus multiplicity-two
  continuous spectrum, full Pauli threshold rank and vacuous dark compression.
- **Strongest propagation result:** exact spectral Mourre theory closes away
  from `5/4`; the spatially weighted threshold loss is sharply square-root
  and high-energy impurity response decays as stated.
- **Strongest topology result:** every single-cut periodic unwrapping retains
  the seam witness; only genuinely topology-changing comparisons remain open.
- **Strongest overclaim:** “the complete signed Fock residual spectrum or
  Moller/Ruelle theory is solved.” Refused. The exact signed sectors are
  infinite and their residual spectral/IBC commutator data are absent.
- **Strongest contrary route:** a renormalized quasifree/Bogoliubov treatment
  of one bidirectional edge may diagonalize an infinite charge block, but its
  point-limit implementability and relation to the K139 domain are unproved.
- **Weakest reproducibility seam:** the full-signed charge theorem uses
  diagonal `W`; an off-diagonal extension must first be tested for charge
  covariance rather than silently inherited.

The companion probe checks the rook incidence charges term by term, the
infinite bidirectional ladders, projection leakage, exact invariant carrier,
Weyl signs and boundary asymptotics, Pauli threshold rank, Mourre velocity,
high-energy response, single-cut seam witness and every claim boundary under
baseline-first hostile mutations.

## Next condition

Construct the one-edge **bidirectional** infinite fixed-charge block as a
renormalized quasifree/Bogoliubov problem on K139's actual IBC domain. Prove or
refute implementability of its diagonalization, compute its residual point
spectrum and exact threshold matrices, and establish `C^(1,1)` regularity for
a physical conjugate operator. Only then enlarge across rook cycles and seek
sector-uniform Mourre/Moller/Ruelle estimates. A separate open-system theorem
is still required for return to NESS and current. Physical and source/GU
selection of the free operator, polarization, charges, couplings, `W`,
`kappa`, domain and state remains independent.

## Reproduction

```bash
python3 tests/channel-swings/k145_invariant_residual_pauli_mourre_boundary_probe.py
python3 tests/channel-swings/k145_invariant_residual_pauli_mourre_boundary_probe.py --selftest
```
