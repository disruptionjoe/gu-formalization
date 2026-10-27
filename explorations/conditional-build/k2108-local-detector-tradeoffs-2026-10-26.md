---
title: "K2108: Fixed-region detector error and global vacuum disturbance"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional imported positive-Hilbert detector mathematics; no GU recovery or apparatus certification
scripts:
  - tests/channel-swings/k2108_local_detector_tradeoffs_probe.py
---

# K2108: Fixed-region detector error and global vacuum disturbance

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: conditional detector bounds and constructions with explicit locality and approximation assumptions
carrier: von Neumann algebra M on H with unit separating vacuum Omega LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_positive_Hilbert_space
real_structure: complex adjoint; no source-selected real form
grading: ordinary observable algebra; no source grading identified
action_owner: repository-construction -- supplied local observable algebra and bounded Kraus instruments
target: fixed-region detector error, preparation norm and global vacuum preservation MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and inference boundary

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 and SC-META-53 are
UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd-action prerequisite. The
positive Hilbert spaces, local algebras, vacuum and dynamics here are imported,
not selected by equation9.16. K2021 local R0/R1 already exists; source-selected
observation and physical domain remain open. LT-SM8/LT-GR6b, source register,
ledger0.263 and canon are unchanged. Native2+1, total/observed chirality,
full20 and K/C accessibility are separate obligations. No GU derivation,
novelty, external-expert or proof-assistant certification is claimed.

## 1. The exact specification is too strong

Let M be a von Neumann algebra on a positive Hilbert space H, and Omega a
unit vector separating for M: A Omega=0, A in M implies A=0. Every effect
E in M, 0<=E<=I, obeys

    p0=<Omega,E Omega>=0  implies  E=0.                (1)

Indeed E^(1/2) belongs to M and has zero norm on Omega. This is the standard
separating-vacuum consequence, not a new theorem or a derivation of separation
for a proposed GU algebra. Reeh–Schlieder is one way conventional relativistic
nets obtain the premise; see [Fewster–Rejzner](https://arxiv.org/abs/1904.04051).
Neither positivity of H alone nor finite-dimensional empty Fock vacuum supplies it.

A stronger measurement consequence requires explicitly local bounded Kraus
operators K_i in M, finite or countable, sum_i K_i* K_i=I strongly. If the
nonselective channel preserves the GLOBAL pure vacuum,

    sum_i |K_i Omega><K_i Omega|=|Omega><Omega|,         (2)

then for each xi perpendicular to Omega, the sum of nonnegative numbers
sum_i |<xi,K_i Omega>|² vanishes. Every K_i Omega=c_i Omega. Separation
implies K_i=c_i I and sum_i |c_i|²=1. Thus the channel is identity, and every
outcome has state-independent probability |c_i|². Grouping Kraus outcomes
does not restore information. This excludes a nontrivial instrument satisfying
this exact specification; it says nothing against an approximate instrument.

Preserving only the vacuum restriction to M is weaker. For
Omega=sqrt(1/3)|00>+sqrt(2/3)|11> and M=M2 tensor I, local Z dephasing leaves
the reduced density matrix diag(1/3,2/3) fixed while removing global
coherence. Its global vacuum fidelity is5/9, not1. The probe checks this
countercontrol. Nonlocal channels and algebras with a nonseparating vacuum
also fall outside the theorem.

## 2. A known inequality with an explicit consuming error budget

For normalized psi choose B' in M', ||B'||<=C, with
||psi-B'Omega||<=delta. Commutation and contraction give

    sqrt(p_psi)=||sqrt(E)psi||
      <=||B' sqrt(E)Omega||+delta<=C sqrt(p0)+delta.    (3)

This inequality and proof are prior art: [Falcone–Conti,
Eq.(8)](https://arxiv.org/html/2509.11599v1#S0.E8). Their
[2026 follow-up](https://arxiv.org/abs/2601.10354) develops coherent-state
applications. Here reuse(3) to specify an error budget for the existing
capture problem; no new inequality is claimed.

Let C>=0 and0<=epsilon<=1. If dark probability p0<=epsilon and miss probability1-p_psi<=epsilon,
then sqrt(1-epsilon)<=C sqrt(epsilon)+delta. For0<=delta<1 its exact
algebraic consequence is

    epsilon >= [(sqrt(1+C²-delta²)-C delta)/(1+C²)]².  (4)

Set x=sqrt(epsilon); the increasing Cx+delta crosses decreasing sqrt(1-x²)
once on[0,1]. Squaring at the crossing gives the positive root in(4).
At delta=0 this is1/(1+C²). For delta>=1 there is no positive bound.
This solves the scalar necessary inequality; it does not prove the bound
is optimal over physical detectors with the given C,delta.

For C>=1 and0<=delta<1, abstract sharpness is achievable in a diagonal two-dimensional
algebra. Set epsilon to(4), Omega=(sqrt(epsilon),sqrt(1-epsilon)),
psi=(sqrt(1-epsilon),sqrt(epsilon)), E=diag(1,0), and
B'=diag(C,sqrt(epsilon/(1-epsilon))). Then epsilon<=1/2,
||B'||=C, ||psi-B'Omega||=delta and both errors are epsilon.
Omega is separating since both coordinates are nonzero. This is abstract
sharpness, not a detector in a relativistic net.

For a desired signal0<eta<=1 and0<=delta<sqrt(eta), equation(3) gives

    p0 >= (sqrt(eta)-delta)²/C².                      (5)

C>0 follows whenever this approximation and eta are possible. Equivalently,
a putative detector with p0<=epsilon and signal>=eta forces
C >= (sqrt(eta)-delta)/sqrt(epsilon) for epsilon>0.
This is a commutant approximation norm cost, not an energy, distance or time
cost. Separation implies cyclicity for M', so approximants exist, but supplies
no uniform norm bound or fixed remote localization. A contraction B'/C would
prepare the unnormalized B'Omega/C with success probability
||B'Omega||²/C²; this is an algebraic postselection statement, not an apparatus.

## 3. Quantifiers determine the practical conclusion

Fix M,Omega and psi. For any0<eta<=1, cyclicity supplies one approximant with
delta<sqrt(eta). Equation(5) then supplies a positive lower bound on p0
for all effects in this fixed M that maintain signal>=eta. Consequently,
p0(E_n)->0 forces p_psi(E_n)->0 for any sequence of effects in fixed M.
The bound depends on the fixed target and algebra through the approximant.

There is no target-uniform positive floor. In H=ell2 tensor ell2 let
Omega=sum_n sqrt(lambda_n)|nn>, every lambda_n>0, sum lambda_n=1,
lambda_n->0. For M=B(ell2) tensor I, Omega is separating. Take
E_n=|n><n| tensor I and psi_n=|nn>. Then p0=lambda_n->0, p_psi_n=1,
and B'_n=I tensor |n><n|/sqrt(lambda_n) exactly prepares psi_n with
C_n=lambda_n^(-1/2). Exact bounded preparations may exist; C need not
diverge as delta->0 for an individual fixed psi.

[K2080](k2080-local-car-detector-2026-10-26.md) already achieves arbitrarily
small errors by growing the local support around its chosen electron packet.
That changes M and is compatible with the fixed-M statement. It must not be
replaced by a universal detector floor. [K2110](k2110-almost-local-instruments-2026-10-26.md)
constructs a different controlled growing-region repair; [K2109](k2109-finite-switching-response-2026-10-26.md)
tests finite switching on a declared scalar field.

## 4. Acceptance and remaining physical seam

The actual detector must justify membership of its bounded Kraus operators
in the declared M, vacuum separation, and a quantitative preparation class.
Neither a finite matrix control nor a formal Hamiltonian density proves these.
Our exact probe checks a faithful Schmidt control, local/global distinction,
nonseparating countercontrol, the algebraic root and changing-state norm cost.
The universal conclusions follow from the proofs above. No local massive
capture Hamiltonian or source-to-observable bridge has been supplied.
