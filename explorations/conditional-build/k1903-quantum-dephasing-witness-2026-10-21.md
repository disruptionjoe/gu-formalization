---
title: "K1903: A robust four-mode quantum dephasing witness"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied noise and finite-mode mathematics; no native GU realization or physical bath selection
scripts:
  - tests/channel-swings/k1903_quantum_dephasing_witness.py
  - tests/channel-swings/k1903_quantum_dephasing_witness_probe.py
---

# K1903: A robust four-mode quantum dephasing witness

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: explicit classical-phase witness, quantum dilation and lower-dimensional sufficiency
carrier: four-dimensional one-particle logical subspace of four fermion modes LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=conditional_target
real_structure: real phase profiles and complex conjugation
grading: finite mode labels and CAR parity
action_owner: repository-construction -- supplied classical laws or finite quantum dilation
target: bounded neutral coherence and specified control cost MAP-TYPE=intertwiner
```


## 1. Question and established background

Pairwise coherence factors need not come from ONE classical phase law.
A matrix C=C*>=0 with diagonal1 defines a completely positive trace-preserving
Schur channel on density matrices, rho -> C entrywise-times rho.
Classical phase noise requires the stronger condition C=E[z z*], |z_j|=1.
The dimension-three sufficiency and dimension-four failure are established
results, not a new discovery: see Li--Tam,
[A Note on Extreme Correlation Matrices](https://epubs.siam.org/doi/abs/10.1137/S0895479892240683)
and Buscemi--Chiribella--D'Ariano,
[Inverting Quantum Decoherence by Classical Feedback from the Environment](https://doi.org/10.1103/PhysRevLett.95.090501).
We give a self-contained finite control and a sharp explicit linear witness
for the selected example, then connect it to bounded neutral mode observables.

## 2. Three modes versus four

Write any rank-r correlation matrix as C=V*V with unit columns v_j spanning
C^r. If r^2>n, there is a nonzero Hermitian r-by-r Q with v_j* Q v_j=0 for
all j: n homogeneous real equations cannot span the r^2-dimensional real
Hermitian space. For small epsilon, V*(I+/-epsilon Q)V are distinct
correlation matrices with midpoint C. Thus extreme matrices satisfy r^2<=n.
The compact finite-dimensional correlation set is the convex hull of its
extreme points; for n<=3 those all have rank1 and are phase matrices.
Caratheodory gives a finite decomposition of at most n(n-1)+1 histories.
This is an existence upper bound, not the minimum history count or energy.

Now take unit vectors

    v1=(1,0), v2=(0,1), v3=(1,1)/sqrt2, v4=(1,i)/sqrt2,
    V=[v1 v2 v3 v4], C=V*V.                           (1)

The four projectors v_j v_j* span all Hermitian2: they recover I,sigma_z,
sigma_x,sigma_y. This is an extreme rank2 correlation matrix. More directly,
the explicit witness below excludes every phase mixture without an extremality
assumption. Merely testing positive eigenvalues or every three-mode principal
submatrix would miss the obstruction: all such submatrices ARE phase mixtures,
but those decompositions need not share a common four-mode law.

## 3. A sharp witness against arbitrary classical laws

Define the 2-by-4 matrix and positive witness

    B = [ -1 -1  sqrt2  0
          -1  i    0   sqrt2 ],     H=B*B.             (2)

One checks B V*=0, hence tr(H C)=0. But for every phase vector z,

    z*H z = |sqrt2 z3-z1-z2|^2
             +|sqrt2 z4-z1+i z2|^2 >= delta,
    delta=(2-sqrt2)^2=6-4sqrt2>0.                     (3)

Proof: set w=conjugate(z1)z2. The magnitudes of z1+z2 and z1-i z2
have squares 2+2Re w and 2+2Im w. For either a, |a|<=2 and

    ||a|^2-2| <= (2+sqrt2) |sqrt2 u-a|,  |u|=1.

Square and sum; (Re w)^2+(Im w)^2=1 gives
4 <= (2+sqrt2)^2 z*H z. This equals(3). Equality occurs at
z=(1,1,1,(1-i)/sqrt2). Thus delta is the exact minimum for this witness;
no finite grid or small-phase approximation is involved.
Averaging proves tr(H D)>=delta for EVERY classical phase correlation D,
including arbitrary continuous or correlated histories. Quantum C in(1)
violates it maximally for a positive H, with value zero.

The nonzero eigenvalues of H are 4+sqrt2 and 4-sqrt2. Therefore

    ||D-C||_1 >= delta/(4+sqrt2),                     (4)

where the norm is the matrix trace norm, not a normalized-state distance.
If C_p=(1-p)C+p I4 is mixed with complete dephasing, tr(H C_p)=8p;
it remains excluded for p<delta/8=(3-2sqrt2)/4.
This is a certified robustness range, NOT the exact classicality threshold.
If every off-diagonal entry is measured within complex absolute error e,
then the witness error is at most (10sqrt2)e, the sum of absolute
OFF-diagonal H entries. This gives a direct finite precision decision rule:
observed tr(H Cobs)+(10sqrt2)e<delta excludes the classical phase class,
assuming diagonal1. A general correlated-noise model is covered; an arbitrary
quantum bath or a non-dephasing model is not excluded.

## 4. Released quantum construction and bounded observable test

Let the environment be C^2 initially in |0>, and choose unitaries U_j with
U_j|0>=conjugate(v_j). The controlled unitary
sum_j |j><j| tensor U_j gives reduced channel rho_jk -> C_jk rho_jk,
because <conjugate(v_k),conjugate(v_j)>=<v_j,v_k>.
For example use U1=I, U2=sigma_x, U3=(1/sqrt2)[[1,-1],[1,1]],
U4=(1/sqrt2)[[1,-i],[-i,1]]. Each is unitary. Kraus operators are the
diagonal matrices formed from rows of conjugate(V). Their sum K* K is I4.
The minimal pure-environment dimension is2, since the Choi rank is rank C=2.
This is a finite quantum realization, not a microscopic local continuum bath.

On the one-particle sector of four normalized fermion modes,
|j>=a_j*|vac>, the even operators a_j* a_k act as matrix units |j><k|.
Prepare (|j>+|k>)/sqrt2 and measure the Hermitian real/imaginary combinations
of these bounded neutral bilinears to recover C_jk with a stated conjugation
convention. All six pairs suffice; the witness itself needs only the nonzero
H entries. The state |s>=(1,1,1,1)/2 produces C/4. Thus an observable H on
that output has expectation0 versus at least delta/4 for classical phase
noise. Its spectral norm is4+sqrt2, so it can be rescaled to a bounded test.
This gives a single-preparation multi-mode consumer rather than relying only
on pairwise PSD tests. The matrix witness may require coherent mixing of
modes; it is not automatically a local spacelike measurement.

Extending the controlled unitary by identity on other Fock sectors preserves
fermion parity and realizes the logical experiment, but is an imported global
finite-mode operation. It does not inherit the scalar pulse's spacetime cone,
a prescribed sea-energy budget or GU source ownership. K1900/K1902 classical
scalar pulses cannot reproduce(1) on these modes, regardless of support,
energy, number of histories or duration. The obstruction is channel structure,
not insufficient control resources. Supplying a quantum ancilla repairs the
finite channel realization while changing the model class; it is not a rescue
within classical phase noise.

## Scope and verification

These are supplied positive-Hilbert/CAR controls, not the GU physical quotient.
SC-OP-04 ASSERTS candidate four-field operator grammar; SC-MAS-01 and
SC-CHI-02 ASSERT a stylized curvature-mass toy; SC-META-53 remains UNCERTAIN.
The controls do not identify that source mechanism. LT-SM8, LT-GR6b and AC-F1,
the source register, physics ledger and canon verdicts remain unchanged.
Classical randomness, the observable algebra, sea and/or quantum ancilla are
imported. No microscopic bath, native full20/K-C adapter, GU prediction,
novelty, external specialist acceptance or formal proof is claimed.

The analytic argument carries the general scope. The producer checks exact
matrices/integrals; a separate probe rederives decisive controls and rejects
mathematical input faults after a clean baseline, separately from report and
provenance checks. These finite tests do not certify all continuum hypotheses.
Hostile review targets phase lifts, positivity versus classical realizability,
infima versus minima, source attribution and the exact physical carrier.
