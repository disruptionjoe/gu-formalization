---
title: "K2146: Fixed-support ultraviolet suppression and rare-record energy"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source selection, apparatus construction or GU recovery
scripts:
  - tests/channel-swings/k2146_fixed_support_parity_ultraviolet_probe.py
---

# K2146: Fixed-support ultraviolet suppression and rare-record energy

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
result: Fixed-support ultraviolet suppression and rare-record energy
carrier: massive scalar Fock space with real compact modulated Cauchy smears LAYER=toy CHIRALITY=N/A
pairing: global vacuum covariance and free-field energy ON=declared_carrier
real_structure: real coefficients and complex adjoint as stated
grading: regional oscillator parity; all vacuum branches globally even
action_owner: repository-construction -- explicit conditional object below
target: fixed-support high-frequency asymptotics of complete parity measurement MAP-TYPE=intertwiner
```

## 1. A distinct way to suppress the actual vacuum baseline

[K2143](k2143-local-canonical-parity-2026-10-27.md) widens spatial support.
Here fix a nonzero real g in C_c^infinity(R), m>0, and define

    f_K(x)=c_K g(x) cos(Kx), ||f_K||=1, K->+infinity,
    mu2=||g'||^2/||g||^2 >0, omega=sqrt(-partial_x^2+m^2).           (1)

Every f_K has the SAME support closure as g. Its parity V_K changes with K:
this is a family of different observables, not approximation of a fixed detector.
The construction remains a supplied positive-Hilbert scalar observable, not a
causal apparatus or GU grading. It disproves a positive vacuum-response floor
based on region size alone within this family, while exposing the cost in rare
outcomes and spatial frequency.

## 2. Controlled two-lobe Fourier asymptotics

Use unitary Fourier transform and a_j=<f_K,omega^j f_K>. The transform of g is
Schwartz; c_K^2=2/||g||^2+O(K^-N) for every N. Products of the two lobes centered
at ±K, even with weights omega^-1, omega, omega^2, integrate to O(K^-N) for every
chosen N. To see this, split momentum space into neighborhoods of the two centers
and their complement; at least one Schwartz factor is in its tail. The mass gap
bounds omega^-1 by1/m, while the other weights grow at most quadratically.
The same estimate controls normalization corrections.

Since g is real, w(q)=|g-hat(q)|^2/||g||^2 is even. Both diagonal lobes give
E_w[omega(K+q)^j]. Split |q|<=K/2 and the complement. On the central part expand
in q/K and m/K; the uniform Taylor remainder integrates against finite Schwartz
moments. All odd q terms integrate to zero on this symmetric part. The complementary
moments are superalgebraically small; near q=-K the bound1/m is essential.
For fixed m and fixed g this yields

    a_1=K+m^2/(2K)+O(K^-3),
    a_-1=K^-1+(mu2-m^2/2)K^-3+O(K^-5),
    a_2=K^2+mu2+m^2+O(K^-N).                                    (2)

The last remainder may be taken to any fixed order. Constants are not uniform
as m->0 or over arbitrary envelope families. A formal Taylor expansion across
the small-frequency lobe tail without this split would not justify (2).

## 3. Complete record and energy accounting

Reuse the exact K2143 identities with A=a_-1 a_1, s=A^-1/2:

    p_-=(1-s)/2, E_V=a_-1 a_2-a_1,
    E_unread=E_V/2, E_-=E_V/(4p_-), E_+=E_V/[2(1+s)],
    <N_global>_-=(1+s)/s^2.                                     (3)

These energies are vacuum-input field energies, with E_± conditional on the
record. The cross terms vanish because the global vacuum is annihilated by H_F
and N_global. Combining (2) with (3) gives

    A=1+mu2/K^2+O(K^-4),
    p_-=mu2/(4K^2)+O(K^-4),
    E_V=2mu2/K+O(K^-3), E_unread=mu2/K+O(K^-3),
    E_-=2K+O(K^-1), E_+=mu2/(2K)+O(K^-3),
    <N_global>_-=2+3mu2/(2K^2)+O(K^-4).                          (4)

Thus both baseline probability and mean deposited field energy vanish at fixed
support, while the rare odd-labeled branch has unbounded mean energy. It still
has EVEN global particle parity and approaches mean particle count2; the energy
per rare excitation grows. A local odd label never means a global odd-particle
outcome. These statements concern moments, not concentration onto a sharp energy
or a two-particle vector.

The spatial-resolution marker is

    ||f'_K||^2=K^2+mu2+O(K^-N).                                 (5)

This diverges even as unread deposited energy falls. It is a required mode-profile
frequency scale, not a proved minimum controller work. Field vacuum disturbance,
conditional energy, spatial bandwidth, preparation and total work are different
resources. Causality remains unconstructed; [K2145](k2145-parity-causal-duration-2026-10-27.md)
continues to impose the support-diameter necessity for exact implementation.
Its fixed-profile dilation law cannot be presented as a uniform lower bound here.

## 4. A directly consumed tradeoff and exact countercontrol

Eliminate K from (4). Along this one fixed-envelope family,

    E_- ~ sqrt(mu2/p_-), E_unread ~ 2 sqrt(mu2 p_-),
    p_- E_-^2 -> mu2, E_unread E_- ->2mu2.                        (6)

A bounded rare-outcome energy rules out this ultraviolet escape along this
family. It does not prove a universal energy-noise bound for every local instrument.
Keeping the detector fixed, controlling the full recorded channel on a named code,
and paying actual preparation/controller resources remain independent problems.

For a finite exact moment countercontrol put equal weight at positive frequencies
K±d, 0<d<K. Then A=K^2/(K^2-d^2), s=sqrt(1-d^2/K^2),
E_V=2Kd^2/(K^2-d^2), E_-=K(1+s)/s^2 and N_-=(1+s)/s^2.
At K=5,d=3 one gets p_-=1/10, E_V=45/8, E_unread=45/16,
E_-=225/16, E_+=25/16 and N_-=45/16. Setting d=0 gives zero vacuum
response, but the conditional odd branch is then undefined (zero probability),
not a state of zero energy. This finite spectral model is an exact control of
the moment identities and coefficients, not a compact-continuum proof.

## Acceptance and source boundary

The adjacent probe checks finite exact identities, certificate arithmetic and altered-input
controls. Universal statements use the written arguments and independent internal specialist
review; finite controls do not prove continuum claims. No external-expert certification,
proof-assistant verification, remote CI or novelty claim is made. SC-OP-04 ASSERTS candidate
operator grammar; SC-OP-05 and SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS an odd-action
prerequisite. LT-SM8/LT-GR6b, ledger0.263, source polarity and canon are unchanged.
