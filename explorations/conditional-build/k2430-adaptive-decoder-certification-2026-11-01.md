---
title: "K2430 Anytime certification of drifting decoder trials"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no all-order, smooth, empirical or native GU result
scripts:
  - tests/channel-swings/k2430_adaptive_decoder_certification_probe.py
---

# K2430 Anytime certification of drifting decoder trials

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
result: K2430
carrier: full complex qubit CPTP channels conditional on trial history LAYER=toy CHIRALITY=N/A
pairing: half-diamond distance and binary Choi-support failure probability ON=declared_carrier
real_structure: positive complex Hilbert Choi matrices and real conditional probabilities
grading: original good and two bad-sign branches, chronological trial index
action_owner: repository-construction -- inherited conditional model
target: tested predictable average channels and average trial distance MAP-TYPE=evaluation
```

## Result and target

[K2428](k2428-exact-recovery-uniqueness-2026-11-01.md)'s complete-channel support test extends to history-adaptive, nonstationary trials and optional stopping. With no failures, its same conservative sample budgets remain sufficient for the **average of the tested conditional channels**, and for their average distance from the candidate. They do not certify the next channel, every trial, a future device or a multi-round memory process.

The new contribution is this full complex-channel consumer and its inference boundary. General anytime calibration already appears in K2400/K2403; supermartingale confidence sequences are standard [Howard–Ramdas–McAuliffe–Sekhon](https://arxiv.org/abs/1808.03204) methodology. No novelty, measured counts or physical/GU recovery is claimed. SC-META-53 remains UNCERTAIN and ledger 0.263 is unchanged.

## 1. Conditional experiment

For each original branch retain every output, including detection failures. Before trial t, history F_(t-1) includes previous outcomes and all control decisions. Branch selection is predictable. A conditional CPTP channel C_t acts on a fresh trusted joint Bell input/reference state independent of device memory given that history. Memory and history adaptation of C_t are allowed; that input independence is a separate physical premise, not implied by calibration of an input marginal.

Use the exact fixed candidate support projector P0, never an interval-valued approximate projector treated as exact. Let

    X_t in {0,1}, p_t=E[X_t|F_(t-1)],
    A_n=sum p_t, S_n=sum X_t.

For ideal preparation/readout, p_t=Tr[(I-P0)J_t]/2. The sums here are within one predictably selected branch. Pauses leave the process unchanged.

## 2. Exact zero-failure confidence at all times

Define

    M_n = 1{S_n=0} / product_(t<=n)(1-p_t).

It is a nonnegative martingale until a certain failure. When p_t=1, define the process as killed on that step; it is a supermartingale everywhere. Conditional expectation follows from multiplying the next zero-outcome probability 1-p_t by its inverse. No independence or stationarity is used.

On a zero-failure path, arithmetic-geometric mean gives

    M_n >= (1-A_n/n)^(-n).

Ville's maximal inequality then implies, with probability at least 1-alpha, simultaneously at every n with S_n=0,

    A_n/n <= 1-alpha^(1/n) <= log(1/alpha)/n.             (2)

This includes arbitrary data-dependent stopping and predictable branch allocation. Counts never reset. Once a branch fails, this zero-failure-only protocol provides no later passing certificate for it.

## 3. A separate nonzero-failure protocol

For a fixed c in (0,1), set lambda=-log(1-c). Then

    M_n(c)=exp(c A_n-lambda S_n)

is a supermartingale, since its conditional factor is exp(c p_t)(1-c p_t)<=1. The inequality follows from log(1-z)<=-z. Hence simultaneously in n,

    A_n/n <= min(1, [lambda S_n+log(1/alpha)]/(c n)).    (3)

To choose among a prespecified grid c_j, assign positive weights w_j summing to one and replace alpha by alpha w_j before taking the minimum. The union bound licenses the choice. Unpenalized post hoc optimization does not inherit the guarantee.

Protocols (2) and (3) are alternatives with their own declared error allocation. To use both adaptively and report whichever passes, split alpha between them in advance, or prove a common test; do not spend the full alpha twice. The same applies across branches and repeated testing campaigns.

## 4. Complete-channel conclusion and systematic errors

For one branch, the realized predictable average Cbar_n=(1/n)sum C_t is CPTP. Its support leakage equals A_n/n. K2428's full complex supported-TP conditioning supplies

    bad d(Cbar_n,C0) <= min(1,Cb sqrt(A_n/n)),
    good d(Cbar_n,C0) <= min(1,2 sqrt(A_n/n)),
    Cb=2(1+sqrt2/mu),   mu^2 > 0.0522306.

Here d is half-diamond distance. The same upper bounds hold for (1/n)sum d(C_t,C0), by the per-trial bound and concavity of square root. K2428's supported TP proof includes imaginary Hermitian Choi directions; real-only tomographic data cannot replace it.

If the conditional joint preparation trace-distance allowance is epsilon_p,t and effect operator-norm allowance is epsilon_m,t, add their average to the observed failure-probability bound **before** the square root. These are bounds against a fresh decoupled ideal experiment. Joint preparation–device decoupling remains required separately. More trials cannot eliminate a fixed systematic floor. If supplied systematic or transport bounds themselves hold only on an external event with failure probability beta, the joint guarantee is at least 1-alpha-beta by a union bound, without requiring independence. Deterministic/pathwise bounds incur no extra probability charge.

For the zero-failure protocol, allocate alpha=1/60 to each of three branches. The already certified budgets of 9,000,000 trials per bad sign and 170,000 good trials, total 18,170,000, still give simultaneous 95% tested-average distances below 0.01 in the ideal experiment. These are sufficient prospective budgets, not observed counts or optimal sample complexity.

For a classical-flag-controlled mixture of the three certified average channels, kappa=max(kappa_g,kappa_+,kappa_-) bounds the decoder error. Applying it to actual deployment requires evidence that deployment realizes those average channels, or a separate transfer bound. The instrument uncertainty delta remains distinct from decoder kappa.

## 5. Executed follow-through: what can be transported

Let b_n bound the mean ideal support failure after adding systematic allowances, and C be the relevant branch constant. On that same simultaneous confidence event:

- The fraction of tested channels with distance at least epsilon>0 is at most min(1,C^2 b_n/epsilon^2). This follows from d_t^2<=C^2 p_t and is often more informative than a mean distance alone.
- Any nonnegative weights summing to one with w_t<=rho/n give both weighted-channel distance and weighted average distance at most min(1,C sqrt(rho b_n)). This is a pathwise consequence, so even outcome-selected weights satisfy it if the density cap really holds. Unrestricted postselection does not.
- For a future channel C_new, an independently justified bound gamma>=(1/n)sum d(C_new,C_t) gives d(C_new,C0)<=min(1,C sqrt(b_n)+gamma). For example a genuinely known channel-drift bound d(C_s,C_t)<=L|s-t| allows taking gamma=L times the mean age of the tested trials. Test data alone do not supply L or gamma.

The first two statements consume existing evidence without claiming a new physical assumption. The third states the exact additional transfer premise needed for deployment. The probe includes original X-mixture examples, an uncapped-selection failure and a nonvacuous exceptional-trial fraction control. None converts a single-use channel statement into a multi-use memory-process guarantee.

## 6. Contrary constructions and verification

- A device uses the target on every test, then switches to X on deployment. Every support test passes; the future channel is unconstrained.
- One tested channel out of 100 is X and the rest are identity. Average support failure is 1/100, although one trial has distance one.
- A rational coherent phase with sin(theta)=3/5 has failure 9/25 and distance 3/5. Square-root scaling cannot generally be replaced by linear failure scaling.
- Bell and product maximally mixed joint inputs share the same input marginal and have different support statistics.
- Distinct PSD/TP Choi matrices I4/2 +/- (Y tensor I)/4 are invisible to every real symmetric observable. Full complex conditioning is essential.
- With failure probability 3/4, an all-zero three-trial block has probability 1/64. Restarting nine times yields 1-(63/64)^9>1/8, violating a purported alpha=1/8 zero-failure certificate.
- A fair common X-error label reused across two uses has the same single-use average channel as independent labels but a different two-use process. Average-channel inference is not a process-tensor certificate.

The [probe](../../tests/channel-swings/k2430_adaptive_decoder_certification_probe.py) exactly enumerates a rational adaptive experiment including p=0 and p=1, verifies conditional hazard recursion, Jensen and maximal crossing controls, and constructs full complex CPTP counterexamples. Arb checks the sample budgets and finite exponential factors. The universal result rests on the written supermartingale and channel-transfer proof; these finite controls are not counted as independent universal proofs. The [report](../../lab/process/k2430-adaptive-decoder-certification.json) identifies each evidence kind.

Reproduce with Python, SymPy and python-flint:

```sh
python tests/channel-swings/k2430_adaptive_decoder_certification_probe.py
```

No actual trusted input/reference preparation, support readout, complete flagged-instrument calibration or physical cost data is supplied by this result.
