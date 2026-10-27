---
title: "K2121: The exact adaptive Gaussian error floor for recorded parity"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source selection, physical quotient, GU verdict, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2121_adaptive_gaussian_parity_probe.py
---

# K2121: The exact adaptive Gaussian error floor for recorded parity

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
result: sharp half-diamond distance one half from adaptive Gaussian parity readout
carrier: two system and two reference CAR modes with Gaussian ancillary modes LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: supplied positive Fock Hilbert product ON=finite_CAR_and_classical_record
real_structure: ordinary Hilbert conjugation and Majorana real coordinates
grading: total fermion parity; even witness and even operations
action_owner: repository-construction -- quadratic fermionic controls and single-mode occupation instruments
target: complete recorded two-mode Lueders parity instrument MAP-TYPE=intertwiner
```

## 1. Question, class and answer

[K2093](k2093-gaussian-readout-resource-2026-10-26.md) excludes a Gaussian
unitary dilation of its distinct 3+1 coarse-readout channel in its stated class. Its explicit
exclusions include measurements, classical mixing and adaptive feedback.
Here those operations ARE allowed. Let G be protocols with initially independent Gaussian ancillary
states, fermionic quadratic unitaries, single-mode occupation measurements,
partial traces, classical randomization, adaptive selection of further such
operations, and classical coarse graining of records. Finite protocols and their
channel-norm limits are included. Conditional Gaussian outputs and convex
mixtures must be distinguished: the unread parity channel itself is a mixture
of two Gaussian unitaries.

For the COMPLETE instrument

    I(rho)=sum_q |q><q| tensor P_q rho P_q,
    P_+ = |00><00|+|11><11|, P_- = I-P_+,

the exact distance is

    inf_(G in class) (1/2)||I-G||diamond = 1/2.        (1)

The reference witness can be chosen even under total fermion parity. This is
an imported positive-Hilbert resource theorem, not a GU exclusion or a claim
that bilinear dynamics cannot transfer a code.

## 2. Gaussian closure and the four-mode inequality

The Gaussian-map closure under occupation projections is known; see
[Bravyi, Lagrangian representation for fermionic linear optics](https://arxiv.org/abs/quant-ph/0404180).
We use it explicitly at each refined adaptive branch. Gaussian mixed states
are mixtures of pure Gaussian quasiparticle occupation states; partial trace
preserves Gaussianity. Classical mixing/coarse graining produces convex
Gaussian states. No claim that every such mixture is one Gaussian state is made.

For four modes in order(s1,r1,s2,r2), write an arbitrary normalized pure EVEN
Gaussian state as

    psi = a|0> + sum_(i<j) b_ij |ij> + c|1234>.

On the nonzero-vacuum BCS chart, expanding the quadratic exponential gives
ac=Pf(b)=b12 b34-b13 b24+b14 b23. The identity extends to its closure; the
nonzero-vacuum chart is dense in the even pure Gaussian manifold (or follows
by a small Bogoliubov rotation). Hence

    2|ac| <= sum_(i<j)|b_ij|²,
    |<chi_+,psi>|² = |a+c|²/2 <=1/2,
    chi_+=(|0000>+|1111>)/sqrt2.                       (2)

Odd pure Gaussian states overlap zero. Convexity extends the same bound to
all convex Gaussian mixed states. An even Gaussian particle-hole transformation
on modes1,2, followed by a number phase if needed, sends chi_+ to
chi_-=(|1100>+|0011>)/sqrt2, so(2) holds for chi_- too. These two special
states are nonGaussian; their bound is derived here, not inferred from a label.

## 3. Reference-complete lower bound

Prepare the normalized Gaussian EVEN input

    Phi=(1+a1^dagger a2^dagger)(1+a3^dagger a4^dagger)Omega/2.

Only modes1,3 are the system;2,4 are a retained reference. The ideal parity
instrument outputs chi_+ or chi_-, each with probability1/2. Every refined
branch of an allowed Gaussian protocol, acting on the system and Gaussian
ancillas, leaves the joint system/reference state Gaussian or a convex
Gaussian mixture after discarded modes. Thus for the bounded test effect

    E=sum_q |q><q| tensor |chi_q><chi_q|,

the ideal expectation is1 and any allowed output has expectation<=1/2,
including protocols with wrong label frequencies. The variational definition
of trace distance gives D>=1/2 on this one legitimate input, proving the
half-diamond lower bound. Norm limits preserve the inequality. Allowing more
Gaussian ancillas or adaptive rounds cannot remove this witness.

## 4. Matching protocol and consequences

Measure each system occupation separately and report only their parity.
This is an allowed Gaussian protocol, but discards coherence inside the parity
sectors. Its complete channel is

    G=(Id_record tensor D1) I,
    D1=(Id+Ad_Z1)/2, Z1=(-1)^n1.

Therefore I-G=(I-Ad_Z1 I)/2 and its half-diamond norm is at most1/2, since
both terms are channels. Together with the lower bound this proves(1).
In particular random Gaussian parity phase kicks exactly realize the UNREAD
channel, but cannot furnish its coherent Lüders record within this class.
Classical parity labels alone are also insufficient to distinguish the target:
the upper protocol has correct labels on every input and still loses coherence.

For any larger system parity instrument, fixing all but two system modes to
empty Gaussian states reduces it to this test. Thus the same lower bound
applies to that larger target/class, though the two-mode upper construction is
not a universal equality proof for all larger systems. A fixed finite local
bilinear probe-field implementation that induces only these Gaussian operations
on the selected finite code is subject to the bound. An arbitrary detector
measurement, nonGaussian resource, quartic interaction or nonGaussian state
preparation escapes an assumption and needs its own analysis. Bosonic resources
are not silently included. K2122 constructs one explicit bounded regional
escape and tests its remaining locality/domain debts.

## 5. Evidence and ceilings

Exact probes use Jordan-Wigner CAR matrices, an actual quadratic BCS
preparation, all system matrix units for the sharpness channel, the Pfaffian
identity and genuinely altered phase/circuit/reference inputs. The universal
Gaussian closure is attributed; the adaptive and reference proof is written.
Independent review is internal, not external certification. No novelty claim.
Source polarities SC-OP-04 ASSERTS, SC-OP-05/SC-META-53 UNCERTAIN and SC-META-56
DISAVOWS are unchanged; no source-native action/observation adapter is supplied,
and LT-SM8/LT-GR6b, ledger and canon remain unchanged.
