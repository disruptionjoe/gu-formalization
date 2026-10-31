---
title: "K2368 Exact recovery tolerates balanced unequal damping"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics or numerical evidence; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2368_unequal_rail_recovery_probe.py
---

# K2368 Exact recovery tolerates balanced unequal damping

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
result: K2368
carrier: one logical qubit in the eight-rail K2356 code and its loss sectors LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product and reference-aware half-diamond norm ON=declared_carrier
real_structure: complex quantum amplitudes and constant strictly positive real damping rates
grading: logical information, rail occupation, erasure position and lost-bit syndrome
action_owner: repository-construction -- independent Markov amplitude damping with the supplied neutral controls
target: complete good-history correctability and balanced-mismatch resource bound MAP-TYPE=evaluation
```

## Result and scope

Pairwise rail equality is sufficient but stronger than necessary for [K2356](k2356-protected-erasure-record-2026-10-31.md). For the same code V|b>=(|00bb>+|11,1-b,1-b>)/sqrt2, write the occupied-rail damping rates as k_i(s)=mu_i+(-1)^s delta_i>0. Assume constant independent damping for duration T>0. Put A=delta1+delta2, B=delta3+delta4 and Gamma=sum mu_i.

For idle damping, the complete zero/one-pair-loss subchannel is exactly correctable if and only if A=B=0. The full channel still includes two-or-more losses. This correctability theorem does not make arbitrary unequal damping harmless. It replaces matching each physical pair by matching the two aggregate repeated-code groups. It is supplied quantum apparatus mathematics, not GU physical positivity: SC-META-53 remains UNCERTAIN, LT-SM8/GR6b and ledger0.263 unchanged.

## 1. Complete Kraus discriminator

Let eta_i(s)=exp[-k_i(s)T]. A physical amplitude-damping branch on a one-excitation rail pair either survives with amplitude sqrt(eta_i(s)) or loses the occupied bit s with amplitude sqrt(1-eta_i(s)), leaving vacuum. Tensor these branches on all four pairs and compose with V. This is the actual finite physical channel on the reached subspace, including loss labels in the environment, not a state-independent erasure replacement.

The no-jump Gram matrix is

    V†K0†K0V=e^(-Gamma T) diag(cosh[T(A+B)],cosh[T(A-B)]).

It is scalar iff AB=0. This necessary condition is insufficient for all good branches. For loss in j=1 or2 with bit s, its squared logical amplitude on b is

    (1-eta_j(s))/2 * exp[-(Gamma-k_j(s))T]
      * exp[-(-1)^s T(A+(-1)^b B)].

Strictly positive k and T make the prefactor nonzero, so its Gram is scalar iff B=0. For j=3 or4 the same calculation requires A=0. Distinct lost positions have orthogonal vacuum flags; distinct lost bits at the same position have orthogonal surviving syndrome images. Under A=B=0 all cross-Kraus products are scalar, including the no-jump branch. These facts prove necessity and sufficiency by directly constructing a decoder below. No finite test substitutes for the displayed all-rate argument.

For idle damping, the time-resolved one-loss Kraus at time tau is sqrt(k_j(s)) exp[-k_j(s)tau/2]/sqrt(1-eta_j(s)) times its finite-channel Kraus. Thus the finite products also cover every unknown-time trajectory refinement; they are not only end-time samples.

## 2. Same decoder, different probabilities

Under balance, the total occupied rate is Gamma on every codeword component. On a one-loss image with erased j and lost bit s it is Gamma-k_j(s), independent of logical b. The no-loss branch is a scalar multiple of V. Every loss branch is a scalar multiple of the same erasure map <s|_j V used by K2356. Its existing syndrome/rail/outer decoder therefore recovers coherence with any reference; it need not know the rate values. Different scalars only alter branch probabilities.

The exact logical-state-independent good probabilities are

    P0=e^(-Gamma T),
    P1=e^(-Gamma T) [sum_i e^(mu_i T) cosh(delta_i T)-4],
    Bbad=1-P0-P1.

With arbitrary trace-preserving fallback for bad branches, the recovered channel is (P0+P1)Id+Bbad F, so half-diamond error is at most Bbad. This is an upper bound, not proof every two-loss sector is uncorrectable. Its total bad probability is state independent because the good subchannel is scalar and the physical channel is trace preserving; individual bad patterns need not be.

An exact nonmatched fixture uses survival rows (9/10,4/5),(4/5,9/10),(19/20,9/10),(9/10,19/20). Products match within each repeated group. It gives P0=1539/2500, P1=3231/10000 and Bbad=613/10000. All eight rates are strictly positive and some within-pair mismatches are nonzero. The companion checks all finite Kraus products and recovered logical matrix units, including off-diagonal coherence, with exact radicals/rationals. Matched pairs recover K2356's former formula.

## 3. Control-time follow-through

The rate operator is Gamma I on the code and (Gamma-k_j(s))I on each one-loss image. Thus [K2362](k2362-transparent-control-locality-2026-10-31.md)'s genuinely transparent controls preserve scalar no-jump evolution and their jump intertwining, giving the same good-event recovery result during those stipulated exact controls. A two-block gate requires the corresponding balance per block and separately accounts for losses in both blocks.

[K2365](k2365-serial-transparent-control-2026-10-31.md)'s diagonal serial-Z path stays in the same computational support before and after a jump, so the rates remain scalar on those reached supports. Its fixed-sign, no-overshoot phase argument therefore gives

    E_serial <= Bbad + P1 min(1,2theta/n).

This extends that specific serial implementation, not arbitrary non-diagonal compiled gates. Keep its finite cap/slew duration when evaluating T; subdivision still increases exposure and can worsen the bound. Initialization, recovery, readout, control imperfections, other subsystem noise and correlated loss remain the explicitly priced debts from K2356/K2365. These formulae are not a measured hardware budget.

## 4. Residual imbalance, not every mismatch

For nonbalanced rates, construct a balanced delta' while preserving each mu: within each group, reduce only entries having the sign of its nonzero sum toward zero until the sum vanishes. This is always possible and never increases an absolute delta, hence preserves strictly positive rates. It achieves

    sum_i |delta_i-delta'_i|=|A|+|B|,
    sum_(i,s)|k_i(s)-k'_i(s)|=2(|A|+|B|).

The same finite-carrier generator/Duhamel estimate as K2356 yields

    E_actual <= min(1,E_balanced+2T(|A|+|B|)).

Use the balanced schedule's complete error bound and the same controls and duration. Large exactly cancelling mismatches contribute zero perturbation debt. This is a sufficient robustness certificate, not a sharp optimal recovery lower bound or empirical noise estimate.

## Controls and remaining conditions

A one-group imbalance passes no-jump KL but fails a loss in the opposite group; imbalance in both fails no-jump KL. Equal rails recover the prior result. Two losses can erase logical distinctions. Off-diagonal recovery must pass, not only basis flags. Heating, correlated damping, time-dependent rates and controls leaving the reached supports change the premises. Exact correction under these larger models is unproved here. Real measured aggregate balance and complete instrument cost remain required before physical application; no novelty or external-expert certification is claimed.
