---
title: "K2428 Exact nominal recovery-channel uniqueness"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no smooth solution, empirical or native GU verdict
scripts:
  - tests/channel-swings/k2428_exact_recovery_uniqueness_probe.py
---

# K2428 Exact nominal recovery-channel uniqueness

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2428
carrier: the original asymmetric two-law flagged qubit instruments LAYER=toy CHIRALITY=N/A
pairing: half-diamond distance and output-first unnormalized Choi trace ON=declared_carrier
real_structure: real planar Bloch data and full complex Hermitian Choi matrices
grading: classical good and two bad sign record blocks
action_owner: repository-construction -- inherited flagged-instrument model
target: exact physical-channel uniqueness and quantitative stability MAP-TYPE=evaluation
```

## Result

The original asymmetric instruments in [K2424](k2424-recovery-saddle-reduction-2026-10-31.md) have **one optimal physical good decoder and one optimal decoder for each bad sign**, with the negative sign aligned as in that construction. Their normalized projective dual coordinates are also unique. This settles the uniqueness question without isolating an algebraic optimizer or adding digits to the existing value bracket.

The rational candidate remains a certified near-optimum, not the exact optimum. Uniqueness concerns channels, not Kraus representations, environments or hardware. It applies to the nominal two-law family, not automatically to perturbed instruments. SC-META-53 remains UNCERTAIN and ledger0.263 is unchanged.

## 1. Localize every attained optimal dual

[K2422](k2422-joint-recovery-optimality-2026-10-31.md) proves compact minimax attainment. Choose an exact reduced optimum. [K2426](k2426-recovery-rigidity-2026-11-01.md) bounds its half-diamond distance from the certified candidate by

    db < 1.584e-12,   dg < 1.202e-13.

The probe recomputes those bounds and compares them with these outward radii.
For either physical law, its bad contribution is

    B_i = E[(t + A v n) n^T].

Each vn is an actual pointer input state, and ||n||=1. Channel distance bounds every output Bloch-vector change by2db. Hence ||Delta B_i||F<=2db. The map taking a real2x2 matrix C to ell=(tr C,C12-C21) has Frobenius-to-Euclidean norm sqrt2. The unitary good block gives

    ||Delta ell_i||2 <= 4(1-w_i)dg + 2sqrt2 w_i db < 1e-11.

Evaluate candidate ell_i exactly in Arb, then enlarge each coordinate by1e-11. Throughout these enclosures the cosine entries are positive and the slopes satisfy b1<0<b2, where b_i=ell_si/ell_ci.

At a saddle q_i=p_i ell_i/||ell_i||. The common-rotation balance is sum q_si=0. Opposite strict sine signs force both p_i>0. Normalizing the cosine resultant to one yields uniquely

    lambda = b2/(b2-b1),   tau = -b1*b2/(b2-b1).

Every attained optimal dual therefore lies in the recorded rectangle near

    lambda = 0.518217356 +/- 1.87e-10,
    tau    = 0.0575373309 +/- 4.23e-11.

These displayed balls enclose the implementation's tighter internal balls. They are not optimizer coordinates.

## 2. Uniform exposure throughout the rectangle

Replay K2424's original support construction on interval inputs, preserving every complex Hermitian Choi direction. The entire rectangle satisfies:

- det N>0 and a simple top eigenvalue;
- strict improving branch h>|det N|;
- nonzero translation;
- rank-two positive slack with a strictly positive nonzero eigenvalue bound;
- injective partial trace on the full supported Hermitian space;
- nonzero good support vector.

Representative lower certificates are mu^2>0.0522306 and gamma_raw>0.1658905. Exact physicality and complementary-slackness identities establish PSD and rank upper bounds; interval positivity establishes strict lower bounds. Containment of zero in DJ is only a consistency check and is not a rank proof.

Fix **one** attained exact dual in this rectangle. Its bad slack D has a two-dimensional kernel P. If J is any supported TP Choi matrix, the injective map Tr_out:Herm(P)->Herm(C2) forces J to be the unique physical support optimizer. The Y-Hermitian direction is included.

## 3. Recover uniqueness of the original channels

An optimality-preserving average or unitary replacement alone would not imply uniqueness before that operation. Use instead the unreplaced supporting inequality. With normalized dual data, let r=||sum(1-w_i)q_i|| and h=sum p_i(1-w_i), so h>=r>0. The original channels satisfy

    4 E_original >= ell_dual + Tr(Dg Jg)
                    + [Tr(Db Jplus)+Tr(Db Jminus_aligned)]/2.

All three slacks are nonnegative. The exact symmetries preserve their functionals; neither sign nor imaginary Choi directions are discarded. In the preferred unitary frame Dg has Bell spectrum(0,r+h,2r,r+h).

At an exact optimal dual ell_dual=4E*. Every optimal original controller thus has all three slacks zero. The full supported TP injectivity fixes each aligned bad channel separately. The one-dimensional good Bell kernel and TP fix the original good unitary. This proves primal uniqueness using one attained dual, without assuming dual uniqueness. The now-fixed endpoint slopes then prove uniqueness of(lambda,tau).

## 4. Useful consequence: stability around the true optimizer

The same uniform rectangle gives conservative coefficients

    original bad distance <= min(1,71 sqrt(e)),
    original good distance <= min(1,4 sqrt(e)+4e),

for every nominal controller with excess error e=E-E*>=0. These bounds refer to the unique exact optimizer and have **no additive1e-27 floor**. They follow from K2426's support-leakage argument at an exact dual, with the maximum constants over the whole rectangle:

    Cb=(1+sqrt2/mu) sqrt(16R/gamma_raw),
    Ag=sqrt(4R/r_raw),   Bg=R/r_raw.

For complete flagged-instrument families within Hausdorff half-diamond distance delta, an actual e_actual-optimal controller has nominal excess at most2delta+e_actual. Substitute that value above. The fixed rational controller still has the inherited objective regret bound1e-27+2delta+kappa when its implementation allowance is kappa. No measured delta is supplied; planar moments alone do not furnish it.

## 5. Executed successor: finite-shot decoder certification

A concrete implementation test can consume the support rigidity without estimating the tiny minimax gap. Prepare a trusted maximally entangled two-qubit state, apply the decoder to its input half and measure the complementary projector to the exact candidate Choi support P0 (not an interval-valued matrix). Retain every trial and the original bad sign labels. For the two aligned bad decoders let p_b be this failure probability. For the good decoder measure the complement of its candidate Bell target, with probability p_g. Then

    bad distance <= 2(1+sqrt2/mu) sqrt(p_b),
    good distance <= 2sqrt(p_g).

Here p_b=Tr[(I-P)J]/2. The first inequality is K2426's supported-TP proof with leakage2p_b; the second follows from the pure-state fidelity/trace-distance bound for J/2. These bounds concern the candidate channels actually measured, so they can provide the implementation allowance kappa in E_actual<=U+delta+kappa.

For fixed N independent stationary trials and zero observed failures, the exact one-sided binomial upper bound is1-alpha^(1/N), no larger than log(1/alpha)/N. Allocate alpha=1/60 to each of the three branches. The probe certifies a prospective simultaneous95% certificate with each channel distance below0.01 using9,000,000 trials per bad sign and170,000 good trials, total18,170,000. These are conservative sufficient budgets, not optimal sample complexity or observed counts. Nonzero failures do not pass this zero-failure criterion; optional stopping or discarded failures invalidates its stated coverage.

Preparation allowance epsilon_p in joint input/reference state trace distance (half trace norm, not just the input marginal) and readout-effect operator-norm allowance epsilon_m increase the true support-failure bound by epsilon_p+epsilon_m before taking square roots. Neither is supplied by channel rigidity. The test assumes complete trace-preserving outputs; postselecting successful detections would test a different object. For classical-flag-controlled postprocessing use kappa=max(d_g,d_b+,d_b-). It certifies decoder implementation, not the unknown flagged-instrument family delta. The full flags and that separate input calibration remain necessary.

## Verification and next condition

The [probe](../../tests/channel-swings/k2428_exact_recovery_uniqueness_probe.py) and [report](../../lab/process/k2428-exact-recovery-uniqueness.json) reconstruct the original certificate, enclose every optimal dual, and certify the entire rectangle. New evidence is counted separately from inherited checks. Concrete controls exhibit distinct PSD/TP channels with one singular supported TP map, an inactive balanced endpoint, multiple exact support optimizers on a branch boundary, and a repeated spectral eigenvalue.

Independent internal mathematical review checks the original-channel supporting inequality, not just the interval outputs. Standard qubit canonical form remains the [Ruskai–Szarek–Werner construction](https://arxiv.org/abs/quant-ph/0101003); no novelty, external-expert or proof-assistant certification is claimed.

Exact algebraic coordinates remain optional mathematical work with no demonstrated physical payoff. The remaining operational successor is an independently calibrated complete instrument with its flags, uncertainty and costs, or a native same-background source/readout construction. The robust theorem specifies what such data would consume; it does not supply them.
