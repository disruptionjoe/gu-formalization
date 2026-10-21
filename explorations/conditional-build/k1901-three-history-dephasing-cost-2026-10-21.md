---
title: "K1901: Exact cost of three-history complete dephasing"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied noise and finite-mode mathematics; no native GU realization or physical bath selection
scripts:
  - tests/channel-swings/k1901_three_history_dephasing_cost.py
  - tests/channel-swings/k1901_three_history_dephasing_cost_probe.py
---

# K1901: Exact cost of three-history complete dephasing

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
result: exact finite-history energy penalty for three neutral modes
carrier: three plateau modes of the rank-four massless R1 target LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product ON=conditional_target
real_structure: real phase profiles and complex conjugation
grading: finite mode labels and CAR parity
action_owner: repository-construction -- supplied classical laws or finite quantum dilation
target: bounded neutral coherence and specified control cost MAP-TYPE=intertwiner
```


## 1. The remaining question

[K1900](k1900-sharp-phase-noise-cost-2026-10-21.md) gives four histories
attaining the unrestricted phase-law optimum for complete three-mode dephasing.
Its three-history example costs 32/27 as much, but that was only a control.
Here it is the exact optimum among laws with at most three histories.
The restriction is to the number of deterministic phase histories, not the
number of samples of a continuous process or a quantum environment dimension.

Fix ordered compact plateau packets with gaps g1,g2>0 in one massless
transport direction. Each history has real plateau phases phi_hj. Write
z_hj=exp(i phi_hj) and C_jk=sum_h p_h conjugate(z_hj) z_hk.
Require C=I3 exactly. Use the K1898/K1900 energy

    Ebar = c/(2pi) sum_r E ||Phi_r'||_2^2,  c=1/24.

Spatial support and amplitude are unrestricted here; fixed resources are
handled separately by [K1902](k1902-fixed-support-scalar-noise-2026-10-21.md).

## 2. Complete classification at three histories

Let A_hj=sqrt(p_h) z_hj. C=A* A=I3 forces at least three nonzero histories.
With exactly three, A is square unitary. Its row norms give 3p_h=1 for every h.
For any two distinct columns, their relative phases are three unit complex
numbers summing to zero. Such a triple is equilateral: after dividing by its
first entry, |1+u|=1 implies Re u=-1/2, so the other two are the primitive
third roots, in either order. Thus each pair has relative phases

    {exp(i alpha), exp(i(alpha+2pi/3)), exp(i(alpha-2pi/3))}.

This elementary proof supplies the needed order-three Hadamard classification;
no numerical search over probabilities or unitary matrices remains.
The Fourier classification itself is established prior art, see the
[research catalogue](https://chaos.if.uj.edu.pl/~karol/hadamard/catalogue/0301.html).

For any unwrapped relative phases with those exponentials, reducing each to
[-pi,pi] can only decrease its square. Rotate alpha into [-pi/3,pi/3] using
periodicity of the SET, not a physical gauge change in a fixed realization.
On this cell the sum of principal squares is

    alpha^2+(alpha+2pi/3)^2+(alpha-2pi/3)^2
      =3alpha^2+8pi^2/9.

Consequently every pair's mean square is at least 8pi^2/27. This also proves
that arbitrary unequal probabilities or large phase windings cannot evade it.
The comparison over alpha minimizes over admissible laws; it does not declare
that a deterministic relative phase has no gradient cost.

## 3. Sharp energy and released implementation

Cauchy--Schwarz on the two gaps now gives

    inf Ebar_(at most 3 histories)
      = (4 c pi/27) (1/g1+1/g2).

The unrestricted four-history infimum from K1900 is
(c pi/8)(1/g1+1/g2). Their ratio is exactly 32/27, for arbitrary positive gaps.
This is a strict 5/27 relative penalty, not merely non-attainment of equality.

Simultaneous equality for the phase law is achieved by equally weighted
plateau phase triples

    (0,0,0), (0,2pi/3,4pi/3), (0,-2pi/3,-4pi/3).

Both adjacent increments have the minimal triple, and all nonadjacent
coherences vanish. Linear ramps, long exterior return tails and smoothing
preserving the plateaux approach the energy. Apply K1900 section4.1 separately
to each of these THREE profiles: an exterior zero-area correction preserves
all plateau values and costs arbitrarily little; the compact antiderivative
then gives a smooth common scalar spacetime potential at fixed positive T.
No extra history is introduced. Thus the exact infimum survives the scalar
control restriction with unrestricted support/amplitude. Generally it is not
attained by a smooth compact profile, for the same ramp/tail reason as K1900.

There is no need for a separate compactness argument for a three-history
sequence: every exactly dephasing member already obeys this strict bound.
Approximate dephasing with a nonzero error tolerance is a different problem.
The distinction is operational: three classical histories suffice to erase
three-mode coherence, but four histories can do so at less sea-energy cost.
It does not compare thermodynamic entropy or the energy of a physical bath.

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
