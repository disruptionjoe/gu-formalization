---
title: "K2260 Charged donors and coherent detector replenishment"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied model theorem only; no source physicalization or canonical verdict
scripts:
  - tests/channel-swings/k2260_coherent_replenishment_bound_probe.py
---

# K2260 Charged donors and coherent detector replenishment

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2260 Charged donors and coherent detector replenishment
carrier: finite-band phase-bearing device, arbitrary invariant charged donors and K retained two-mode field plus record outputs LAYER=toy CHIRALITY=N/A
pairing: positive tensor-product Hilbert structure and quantum trace norm ON=declared_carrier
real_structure: complex conjugation and Hilbert adjoint
grading: nonnegative occupation-number labels, not observed physical chirality
action_owner: repository-construction -- supplied conserving finite apparatus
target: complete detector error lower bound from phase-orbit distinguishability MAP-TYPE=intertwiner
```


## 1. Charge supply does not measure asymmetry supply

[K2257](k2257-finite-battery-service-capacity-2026-10-29.md) gives charge-support and mean-budget necessities. Here charged donors may have arbitrarily large number, so that obstruction alone need not apply. We ask whether they can support the full [K2253 instrument](k2253-full-instrument-reference-reuse-2026-10-29.md) when the phase-bearing device remains finite.

The initial ENTIRE asymmetric device state sigma has total-number support0,...,H (H>=1). All fresh donors jointly commute with their total number and are initially independent of sigma and the vacuum inputs. They may have degeneracy, correlations among themselves, and unlimited charge; individual diagonal marginals alone do not imply joint invariance. Every control/feedforward map is U(1)-covariant, neutral records carry no phase resource, and no asymmetric controller is omitted from sigma. Conserving dilations with invariant ancillary stock imply this covariance. Old outputs are isolated and retained. This is a declared apparatus class, not all physical detectors.

For R_theta=exp(-i theta N), covariance and trace-distance contraction give for actual output xi_K

    D(xi_K,R_theta xi_K R_theta*)
      <=D(sigma,R_theta sigma R_theta*)
      <=sin(H|theta|/2), if H|theta|<=pi.             (1)

For the last step purify sigma without rotating its purifying reference. Its overlap is sum_n p_n exp(-in theta), a convex combination on an arc of angular width H|theta|. The modulus is at least cos(H|theta|/2); pure-state trace distance is at most the displayed sine, and partial trace contracts. Unlimited invariant donors do not increase the initial orbit distance. This is a direct application of symmetric-processing information monotonicity; see [Marvian and Spekkens, modes of asymmetry](https://arxiv.org/abs/1312.0680). No novelty of that general principle is claimed.

## 2. Exact vacuum consumer for the actual full instrument

Use b=(5/3)a1+(4/3)a2*, E=1_(b*b=0) its mode-vacuum spectral projector, and v0=E|00>, v1=(I-E)|00>. Let tau=|0><0|record tensor |v0><v0|+|1><1|record tensor |v1><v1|. The vectors are unnormalized: ||v0||²=p=9/25, ||v1||²=1-p, and v0's |j,j> coefficient has magnitude p(4/5)^j. Set r=16/25, z=exp(-2i theta). The root fidelity with its phase rotation is exactly

    f(theta)=|p²/(1-rz)|+|1-2p+p²/(1-rz)|.           (2)

The two terms are overlaps of the two unnormalized rank-one record blocks. Fidelity multiplies for K independent ideal vacuum calls. The fidelity-distance inequality therefore gives

    D(tau^tensor K,R_theta tau^tensor K R_theta*)
      >=1-f(theta)^K.

If actual joint field-plus-record error is epsilon_K, triangle inequality and (1) imply

    epsilon_K >= [1-f(theta)^K-sin(H|theta|/2)]_+/2.  (3)

This is a complete-service lower bound since the fixed vacuum-input tester is allowed. A record-only channel discards the resource-bearing field and is NOT the target. No conditional rare-record normalization is used. The exact geometric sums include the whole infinite output tail.

## 3. Quantitative lifetime despite unlimited diagonal charge

The second block overlap is at most1-p, while the first equals p/sqrt(1+(1600/81)sin²theta). Thus

    f(theta)<=1-p[1-(1+(1600/81)sin²theta)^(-1/2)].

Take theta=1/(2H). Since sin theta>=theta/2 and
1-(1+x)^(-1/2)>=x/[2(1+x)] for x>=0, monotonicity yields

    f(theta)<=1-18/(181H²),
    epsilon_K>=max(0,3/8-(1/2)exp(-18K/(181H²))).     (4)

Here sin(Htheta/2)=sin(1/4)<=1/4. For K>=20H², exp(360/181)>4, so epsilon_K>1/4. The exponential inequality follows already from 1+x+x²/2>4 at x=360/181 and is checked rationally. This is a conservative sufficient lifetime obstruction, not an optimum. More generally, for fixed finite H choose theta=K^(-1/4): the initial orbit distance tends to zero while K(1-f(theta)) tends to infinity, giving liminf epsilon_K>=1/2.

Unlike K2257, the bound survives unlimited invariant charged replenishment. It requires a finite bandwidth for the TOTAL initial asymmetric resource. A large phase-bearing memory or coherent donor changes H or the initial orbit-distance bound. The theta-dependent equation(3), generalizes by replacing the sine term with the actual initial orbit distance.

## 4. Recharge countercontrol and irreversible coherence loss

Do NOT conclude that diagonal donors can never restore a reference. Suppose a packet sum_(n=d)^H c_n|n> was coherently translated to sum c_n|n-d>. A donor in number eigenstate |d> permits the conserving map

    |n-d>_B|d>_D -> |n>_B|0>_D,

extended to a unitary independently in each total-number sector. This restores the packet exactly: charge was spent, its coherence was not destroyed. The map is an existence construction with explicit finite support, not a local control synthesis theorem.

For actual lost asymmetry, define the number-d mode beta^(d)=sum_n P_(n+d) beta P_n and C_d(beta)=||beta^(d)||1. Covariance preserves modes and CPTP maps contract their trace norm (by the unital adjoint operator-norm bound), so invariant independent donor addition and covariant processing cannot increase C_d. Extraction of a mode is a Fourier average of conjugations, hence trace-norm contractive. Therefore

    D(beta_out,r_target)>=[C_d(r_target)-C_d(beta_in)]_+/2. (5)

Include ALL accessible device memories in beta_in and compare their total-number mode; correlations may retain recoverable coherence. This generic mode bound need not be sharp. A sharp simple control is a fully dephased (|0>+|2>)/sqrt2 reference: invariant processing leaves an invariant state with zero 0--2 matrix element. The norm-one observable |0><2|+|2><0| gives distance at least1/2 from the desired pure packet, attained by its dephased state. Arbitrarily high diagonal donor charge cannot reduce it. This distinguishes reversible charge translation from loss of global phase information and identifies coherent fresh stock or a larger preserved asymmetric memory as the concrete replenishment requirement.


## Reproduction and scientific ceiling

Run `python tests/channel-swings/k2260_coherent_replenishment_bound_probe.py`; `--write` refreshes the report. Exact finite controls and genuine changed-input faults supplement the written proofs; sampling does not prove the universal assertions. Independent internal specialists reviewed the actual arguments and probes, including cross-review of the separate results. No Lean, external-expert, novelty or remote-CI certification is claimed.

SC-OP-04 ASSERTS candidate four-field grammar; SC-OP-05 remains UNCERTAIN on the southeast rival; SC-META-53 remains UNCERTAIN on physical positivity. These supplied models do not resolve those source claims. LT-SM8/LT-GR6b/AC-F1 and ledger0.263 remain unchanged because action ownership, physical quotient and observed-domain bridges remain absent. Preserve full16cells/full20/K-C, native2+1/nonchiral, mirrors/fullII/normaljets, scalar/thermal and cosmology ceilings.
