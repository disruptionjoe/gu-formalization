---
title: "K2114: Binary Lueders causality and a sharp approximation threshold"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional imported mathematics; no source selection, continuum readout implementation, GU verdict or novelty
scripts:
  - tests/channel-swings/k2114_binary_lueders_causality_probe.py
---

# K2114: Binary Lueders causality and a sharp approximation threshold

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
result: conditional operational and analytic mathematics
carrier: supplied complex Hilbert CAR, finite code and ordinary external tensor reference LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert metric ON=declared_complex_completion
real_structure: CAR adjoint; no source-selected reality or barred-field identification
grading: fermion parity; energy sign, charge and source grades remain separate
action_owner: repository-construction -- supplied CAR and free massive Dirac dynamics
target: finite-factor instruments or specified free-Dirac scattering MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and prior-result boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite.
The imported positive CAR/Dirac construction is not source operator9.16.
K2021 local R0/R1 maps do not select its state, algebra or dynamics.
LT-SM8/LT-GR6b retain their action/observation/quotient/positivity debts.
Source register, ledger0.263 and canon verdicts remain unchanged. These results
answer reverse-scaffold coherence and causal-transfer demands; no GU recovery,
new substrate pathway, novelty or external certification is claimed.

## 1. The binary classification, with prior art

Let H_A,H_B be finite-dimensional complex Hilbert spaces. E is an orthogonal
projection, R=I-2E a Hermitian unitary, and the UNREAD binary Lueders channel is

    Phi_E(rho)=E rho E+(I-E)rho(I-E)=(rho+R rho R)/2.       (1)

Here A-to-B non-signalling means that Bob's output marginal depends only on his
input marginal, for all joint inputs. In Heisenberg form this is invariance of
I tensor B(H_B). Then

    Phi_E is A-to-B non-signalling
    iff R=R_A tensor R_B with local Hermitian involutions
    iff Phi_E is non-signalling in BOTH directions.       (2)

Proof. Equation(1) implies Ad_R(B)=2 Phi_E*(B)-B lies in Bob's algebra.
Conjugation is its own inverse, so this inclusion is equality. Every finite
matrix-algebra automorphism is inner; remove its implementing Bob unitary.
The remaining unitary commutes with Bob's full algebra and therefore lies in
Alice's factor. Thus R=U_A tensor U_B. Since R^2=I, U_A^2=z I and
U_B^2=z^-1 I for a unit scalar z. Opposite scalar rephasings make both squares
I; a unitary with square I is Hermitian. Conversely (1) is the equally weighted
mixture of two product unitaries, implemented with shared classical randomness.

This is an elementary specialization of known unitary semicausality rigidity,
not a novelty claim: [Beckman, Gottesman, Nielsen and Preskill (2001), Theorem7](https://preskill.caltech.edu/pubs/preskill-2001-causal.pdf).
[K1894](k1894-semicausal-quantum-dynamics-2026-10-21.md) studies GKLS generators;
[K2081](k2081-causal-instrument-realization-2026-10-26.md) gives particular
mode-measurement causal witnesses. Neither is being rediscovered as a new
continuum apparatus. Equation(2) classifies this binary channel class only;
multi-outcome measurements and general noisy channels need not obey it.

## 2. Exact distance for the existing rank-one-versus-three coarse readout

[K2090](k2090-coherent-coarse-readout-2026-10-26.md) uses
E=1-(1-n_f)n_g. Up to local basis relabeling and outcome exchange its unread
channel is Phi=(Id+Ad_CZ)/2 on two logical qubits, where
CZ=diag(1,1,1,-1). The two-outcome rank split is1+3, not a measurement of each
occupation separately. Define half-diamond error as one half the diamond norm,
including arbitrary finite external references. Then

    inf_(Lambda non-signalling) ||Phi-Lambda||_diamond/2
      = inf_(Lambda localizable) ||Phi-Lambda||_diamond/2 = 1/4.   (3)

Lower bound: Alice prepares0 or1 while Bob prepares |+>. The two target Bob
outputs are |+><+| and I/2, trace distance1/2. A non-signalling Lambda gives the
same Bob state for these inputs. If its uniform error is e, contraction and
the triangle inequality give1/2<=2e.

Attainment is constructive. Put S=diag(1,i), V=Z tensor Z times CZ, and

    Psi = (1/2)Id+(1/4)Ad_(S tensor S)+(1/4)Ad_(S* tensor S*).

This channel requires only shared randomness and local phase gates. Entrywise
on ALL matrix units,

    Psi=(1/2)Id+(1/4)Ad_CZ+(1/4)Ad_V,
    Phi-Psi=(1/4)(Ad_CZ-Ad_V).                           (4)

The difference of unitary channels has diamond norm at most2. Equality here
is witnessed by (|00>+|01>)/sqrt2: CZ and V produce orthogonal vectors.
Thus (4) gives exactly1/4. This proves optimality, not just a lower bound or
an unreferenced numerical optimization. A local X conjugation moves the
rank-one distinguished basis vector to K2090's |01>; the error is unchanged.

## 3. Legitimate local CAR tests and causal scope

A single-mode even algebra is abelian. Do not apply the full-factor theorem
by silently using forbidden odd single-mode operations. Instead choose two
orthogonal compact modes in each region. The fixed one-particle dual-rail
corner has basis |10>,|01>; its logical X is the even hopping bilinear and
its logical Z is an occupation difference. The above input preparations and
swaps are physical even operations on this supplied CAR encoding. The coarse
projection restricts to the stated logical projection on the four-mode corner.
Arbitrary spectator inputs do not remove a uniform lower bound already witnessed
on one reducing corner. This does not classify centered even algebras globally.

Assume an apparatus obeys finite propagation speed v and includes no superluminal
communication resource. Shared pre-existing apparatus correlations independent of the unknown system input
are permitted. Input-dependent apparatus preparation is outside this channel model. If
input/output labels are fixed in two spatial regions at distance L, its
unread channel before T<L/v is non-signalling between them. Consequently it
cannot approximate this encoded target uniformly with error less than1/4.
A free-evolved endpoint changes the supports of the tests; use K2081's
transported-cone accounting rather than inserting the initial gap unchanged.
K2112's positive-energy modes have tails and are NOT these compact local
factor encodings. Transferring this numerical threshold to those modes requires
its own quantified localization bridge. This is a conditional apparatus
constraint, not a universal impossibility of measuring E after communication.

## 4. Surviving class and released next construction

For R=R_A tensor R_B, shared randomness realizes the unread channel immediately.
It does not provide the correlated measurement record. The full coarse instrument
must retain within-sector coherences. [K2116](k2116-distributed-coherent-readout-2026-10-26.md)
constructs it using supplied entangled ancillas, local controlled reflections,
and later classical collection. It also computes the exact cost of an imperfect
pure resource. Those operations are imported finite-factor resources, not a
local massive continuum coupling. This classification explains which part of
K2113's arbitrary-E interface can use that repair without contradicting causality.

The probe checks all16 diagonal two-qubit reflections against the actual Heisenberg
non-signalling condition, every matrix unit in(4), the sharp witness, and even
dual-rail controls. The universal factor classification, diamond norm upper
bound and causal interpretation are written arguments, not finite enumeration.
