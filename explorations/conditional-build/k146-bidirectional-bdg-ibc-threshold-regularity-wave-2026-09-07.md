---
title: "K146 bidirectional BdG/IBC threshold and regularity wave"
status: active_research
doc_type: conditional_one_edge_bidirectional_bdg_ibc_implementability_charge_spectrum_pauli_threshold_and_physical_conjugate_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned theorem for the equal-coupling one-edge diagonal-W signed point control that its renormalized IBC operator is a relative BdG boundary problem with odd Schur function, one simple zero mode, Hilbert-Schmidt interacting/free polarization difference and implementable relative Bogoliubov transform; the two vacuum-adjacent fixed-charge blocks have one simple ground state each and essential spectrum from one dressed threshold, all other charge blocks have no point spectrum, every bound-residual first threshold has rank-one Pauli matrix with one odd kinematic channel, and the physical velocity conjugate gives C1,1 and strict Mourre estimates away from zero and threshold; no global hole-sea flip, unequal-coupling or rook-cycle theorem, many-body asymptotic completeness, NESS/current, physical selector, source/GU action, Born derivation, prediction or confirmation follows
manifest: lab/process/k146-bidirectional-bdg-ibc-threshold-regularity-wave.json
probe: tests/channel-swings/k146_bidirectional_bdg_ibc_threshold_regularity_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K146 bidirectional BdG/IBC threshold and regularity wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet fixes one active edge `e=(u,v)`, equal real particle and
hole couplings `g=1`, `m=kappa=|q|=1`, positive self-inclusive screening,
subtraction at zero and diagonal `W=0`. It uses K139's renormalized IBC domain
on the positive empty particle/hole Fock representation. It does not cover
unequal couplings or a second edge.

```gu-typed-objects
result: the equal-coupling one-edge bidirectional signed IBC control has an implementable relative Bogoliubov diagonalization, a simple zero BdG mode, complete charge-resolved point and essential spectra, rank-one Pauli first-threshold matrices and physical-velocity C1,1/Mourre control, while the global hole-sea flip and rook-cycle extension remain unproved or false as stated
carrier: C2 impurity-Klein parity reduction tensor Gamma_minus of L2(R)_plus direct-sum L2(R)_minus, equivalently the self-dual Nambu boundary carrier C direct-sum L2(R) direct-sum conjugate-L2(R) relative to the empty particle/hole Fock polarization LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive CAR Fock pairing and self-dual BdG pairing with the interacting negative spectral projection compared to the free gapped projection ON=repository_signed_point_control
real_structure: particle-hole conjugation exchanges the positive and negative Nambu branches; it is bookkeeping until the interacting/free polarization difference is proved Hilbert-Schmidt
grading: conserved integer edge charge q=n_d+N_plus-N_minus and combined Klein-CAR parity; the zero mode joins the q=0 and q=1 ground sectors
action_owner: repository-construction -- polarization, point operator, equal couplings, subtraction, W, screening, charge convention, domain and state are not selected by Weinstein's source or a GU action
target: relative BdG/IBC implementability, charge-resolved spectrum, Pauli threshold matrices and physical-conjugate regularity MAP-TYPE=intertwiner
```

## Inline preflight bookend

K145 proves that the exact bidirectional charge block is infinite, which rules
out finite residual enumeration but not quadratic diagonalization. With one
edge and the Klein parity fixed, the impurity transition is one fermionic mode
`d`; the particle term is hopping and the hole term is pairing. This makes the
right first object a self-dual BdG boundary operator, not a truncated Fock
matrix.

Mechanism retrieval found K139's IBC chart, K140's warning that a global sea
change can fail Shale--Stinespring, K144's scalar Weyl function and K145's
charge ladder. It found no relative polarization comparison or charge-resolved
many-body spectrum for this block. The primary route is the odd Schur function
and its finite-rank resolvent. A direct sector Jacobi/Feshbach construction was
held as fallback. The route-changing checks are the Hilbert--Schmidt norm of
the relative polarization and the second commutator of the resolvent-dressed
point vector.

## 1. The infinite charge block is a renormalized BdG boundary problem

Write `d*|u>=|v>` after fixing the Klein-parity partner. With particle and hole
fields `a_+` and `a_-`, the cutoff interaction is

```text
V_N=d* a_+(r_N)+a_+*(r_N)d+d* a_-*(r_N)+a_-(r_N)d.    (1)
```

It commutes with

```text
q=n_d+N_+-N_-.                                        (2)
```

Nambu notation `Psi=(d,a_+,a_-*)` turns (1) into a number-preserving boundary
matrix with free entries `0,epsilon,-epsilon`, where

```text
epsilon(p)=sqrt(1+p^2)+1/4,  tau=5/4.                 (3)
```

This notation does **not** fill the hole continuum. The free negative spectral
projection is the reference complex structure of the original empty-hole Fock
representation; only differences from it can be implemented.

Let K be the self-adjoint boundary operator selected by K139's matched IBC
limit. In terms of K144's subtracted Weyl function `M`, its impurity Schur
function is

```text
F(z)=-z-[M(z)-M(-z)]
    =-z[1+2 integral_R dp/(2 pi)(epsilon(p)^2-z^2)^-1]. (4)
```

For `|z|<tau` the bracket is strictly positive. Hence K has one simple gap
eigenvalue, `z=0`, and no other gap eigenvalue. The positive/negative boundary
imaginary parts exclude embedded eigenvalues; the finite-rank boundary
resolvent formula excludes singular-continuous spectrum. Therefore

```text
sigma_p(K)={0} simple,
sigma_ac(K)=(-infinity,-tau] union [tau,infinity),
sigma_sc(K)=empty.                                     (5)
```

The normalized zero mode has impurity weight

```text
Z=[1+2 I_2]^-1,
I_2=integral_R dp/(2 pi) epsilon(p)^-2,                (6)
```

and continuum tails `-sqrt(Z)/epsilon` and
`+sqrt(Z)/epsilon` in the particle and conjugate-hole entries.

## 2. The relative Bogoliubov transform is implementable

Let `P_0` and `P` be the negative spectral projections of the free and
interacting gapped BdG operators, with the zero mode assigned separately.
The resolvent difference is finite rank and its vectors are
`(epsilon-z)^-1` and `(epsilon+z)^-1`. The gap permits a sign-contour formula;
the squared Hilbert--Schmidt integrand is bounded by a constant times
`epsilon^-2`, which is integrable in one dimension. Thus

```text
P-P_0 is Hilbert--Schmidt.                              (7)
```

Shale--Stinespring therefore implements the **relative** interacting
polarization on the original Fock space. This is not implementation of
`a_-(p) <-> a_-*(p)` on every mode: that global hole flip changes projections
by the identity on an infinite-dimensional continuum and is not
Hilbert--Schmidt.

After the relative implementer, the renormalized quadratic Hamiltonian is a
constant `E_B` plus positive quasiparticle energy `|K|`. The simple zero mode
may be empty or occupied. The two vectors are normalizable and lie in charges
`q=0` and `q=1`, respectively.

## 3. Complete fixed-charge point and essential spectra

No exterior sum containing an absolutely continuous K-mode is an eigenvector.
Consequently

```text
sigma_p(H_q)={E_B} simple for q=0,1;
sigma_p(H_q)=empty otherwise.                          (8)
```

For integer q define

```text
n(q)=max(1,dist(q,{0,1})).                             (9)
```

The lightest charge-preserving continuum configuration uses `n(q)` dressed
quasiparticles, and Minkowski sums of `[tau,infinity)` fill a half-line. Hence

```text
sigma_ess(H_q)=[E_B+n(q) tau,infinity),                (10)
```

with no singular-continuous spectrum. In particular the infinite `q=1` block
that K145 left open has one simple ground state and its continuum begins at
`E_B+5/4`, not at a finite collection of K144 projected levels.

## 4. Every bound-residual first threshold has rank one

Only residual charges `0` and `1` have bound states. One-particle first
thresholds therefore occur for total charges `-1,0,1,2`: a dressed hole leaves
residual charge `0` or `1`, and a dressed particle leaves residual charge `0`
or `1`. Orthogonality to the zero mode gives unit Pauli vacancy in the open
continuum. In normalized even-channel coordinates every one of the four
matrices is

```text
Gamma_tau=[sqrt(Z)],  D_tau=[Z],  rank=1.              (11)
```

In the two momentum-branch coordinates this is
`Gamma_tau=[sqrt(Z/2),sqrt(Z/2)]`; the orthogonal odd branch is a one-
dimensional kinematic channel kernel. There is no dark impurity direction and
the compressed dark denominator is `0 by 0`. Charges outside
`{-1,0,1,2}` first reach continuum through two or more escapes and have no
bound-residual one-particle `Gamma_tau` to invent.

## 5. A physical velocity conjugate is C1,1 on the IBC domain

Let `v(p)=p/sqrt(1+p^2)` and

```text
a=(v i partial_p+i partial_p v)/2,
A_N=0 direct-sum a direct-sum (-a).                    (12)
```

The opposite sign on the conjugate-hole branch makes the free commutator
positive on both continua:

```text
[K_0,iA_N]=0 direct-sum p^2/(1+p^2)
                direct-sum p^2/(1+p^2).               (13)
```

Although the raw point vector is not in `L2`, its first commutator is
`(i/2)v'`, and the first two commutators of every resolvent-dressed boundary
vector are in `L2`; `v'` and `v''` have integrable square. The K139 boundary
inverse and its adjoint therefore preserve the corresponding graph estimates.
Thus `K` and the implemented quadratic Hamiltonian are `C^(1,1)` with respect
to the second-quantized physical conjugate.

On compact energy intervals separated from `0` and `+/-tau`, the boundary
terms are compact and (13) has a positive lower bound after spectral
localization. The simple zero mode is projected out, giving strict Mourre and
the standard `s>1/2` limiting-absorption estimate. The constant collapses at
threshold; no threshold-uniform or rook-cycle-uniform estimate is claimed.

## Inline postflight bookend

- **Strongest advance:** the first genuinely bidirectional infinite charge
  block is diagonalized relative to the original positive Fock representation.
- **Strongest distinction:** the relative interacting polarization is
  implementable, while the global hole-sea flip is not.
- **Strongest spectral result:** only charges `0` and `1` have point spectrum,
  each a simple ground; every charge block has the exact half-line threshold
  (10).
- **Strongest threshold result:** all four bound-residual first thresholds have
  rank-one matrix `D_tau=Z`, one odd kinematic kernel and no dark impurity.
- **Strongest regularity result:** the physical velocity conjugate is
  `C^(1,1)` on the one-edge IBC domain and yields strict Mourre away from zero
  and the two mass thresholds.
- **Strongest overclaim:** extending this scalar result uniformly across rook
  cycles. Refused: shared impurity modes create matrix thresholds and
  overlapping charge channels.
- **Weakest reproducibility seam:** the theorem uses equal real couplings and
  diagonal `W=0`; breaking particle-hole symmetry removes the odd Schur
  factorization and must be reanalyzed.

The companion probe checks the odd Schur identity, unique zero, polarization
Hilbert--Schmidt bound, charge thresholds, Pauli matrices, commutator weights
and all scope fences under baseline-first hostile mutations.

## Next condition

Extend the relative-polarization and `C^(1,1)` estimates to the first two-edge
rook corner sharing an impurity vertex. Compute the resulting matrix-valued
zero modes and all Pauli-restricted threshold ranks before any cycle-uniform
Mourre or many-body scattering claim. Physical/source selection and open-system
NESS/current remain separate dependencies.

## Reproduction

```bash
python3 tests/channel-swings/k146_bidirectional_bdg_ibc_threshold_regularity_probe.py
python3 tests/channel-swings/k146_bidirectional_bdg_ibc_threshold_regularity_probe.py --selftest
```
