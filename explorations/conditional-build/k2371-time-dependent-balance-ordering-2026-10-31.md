---
title: "K2371 Integrated damping balance depends on control ordering"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics or numerical evidence; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2371_time_dependent_balance_ordering_probe.py
---

# K2371 Integrated damping balance depends on control ordering

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
result: K2371
carrier: eight physical dual rails with code, no-jump leakage and one-loss sectors LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product and complete Kraus Knill-Laflamme products ON=declared_carrier
real_structure: complex finite-dimensional matrices and positive time-dependent real rates
grading: logical qubit, rail bit, syndrome, loss time and control ordering
action_owner: repository-construction -- independent Markov amplitude damping and supplied physical transparent controls
target: time-resolved balance iff and finite noncommuting no-jump obstruction MAP-TYPE=evaluation
```

## Typed scope and result

Use K2356's positive-Hilbert eight-rail code V|b>=(|00bb>+|11,1-b,1-b>)/sqrt2, with each outer bit s represented by |s,1-s>. Damping is independent Markov amplitude damping, with bounded integrable strictly positive occupied-rail rates k_i(s,t)=mu_i(t)+(-1)^s delta_i(t). The time-dependent rates and K2362 controls are supplied apparatus data. No hardware, GU physical-state, native-action, empirical or novelty claim follows; SC-META-53 and LT-SM8/GR6b remain unchanged. This is a conventional comparator extending K2368, not a source-native inference.

For idle damping over [0,T], replace constant-rate aggregate balance by integrated balance:

    GammaBar=integral sum_i mu_i(t) dt,
    ABar=integral [delta1(t)+delta2(t)] dt,
    BBar=integral [delta3(t)+delta4(t)] dt.

The complete zero/one-pair-loss Kraus family is exactly correctable iff ABar=BBar=0. The same balance is sufficient for K2362 diagonal transparent Z and K2365 diagonal serial-Z. It is NOT sufficient for arbitrary noncommuting transparent controls: an exact finite-duration X_ET counterexample below fails even the no-jump Knill-Laflamme condition, despite every individual rail pair having matched integrated damping. Pointwise aggregate balance remains sufficient for the full K2362 transparent gate set.

## 1. Time-resolved proof, not a stationary-rate substitution

Put K_i(s)=integral_0^T k_i(s,t)dt and eta_i(s)=exp[-K_i(s)]. Independent time-dependent amplitude damping on a physical qubit has survival exp[-K] because its amplitude-damping generator is a scalar rate multiplying one fixed generator. Tensoring gives the same finite Kraus maps as K2368 with these eta values.

For exactly one loss at pair j and occupied bit s, at time tau, the time-resolved idle Kraus operator is

    E_js(tau) = c_js(tau) E_js^finite,
    c_js(tau)=sqrt[k_j(s,tau)] exp[-(1/2)integral_0^tau k_j(s,t)dt]
               /sqrt[1-eta_j(s)].

The coefficient is independent of the logical input, and integral_0^T |c_js(tau)|^2 dt=1. This follows directly by multiplying the lost rail's no-jump propagation before tau and its jump amplitude, while the surviving rails propagate over the entire interval. Thus the finite Kraus family and its full continuum of time refinements have identical correction conditions. Strict positivity can be weakened to positive integrated loss probability for each required branch; keep the stronger stated assumption to avoid degenerate exceptions.

The no-jump Gram is exp(-GammaBar) diag(cosh(ABar+BBar),cosh(ABar-BBar)), scalar iff ABar BBar=0. A loss in group {1,2} has a Gram scalar iff BBar=0; a loss in group {3,4} requires ABar=0. Erasure flags and surviving lost-bit syndromes are orthogonal. This proves the full iff and gives the same K2356 decoder under balance.

## 2. Why diagonal controls permit integrated balance

For diagonal Z_ET or a diagonal serial-Z schedule, every reached computational string keeps its occupations and bits until its jump. The damping exponent accumulated by a complete one-loss history is the full-interval exponent on the original code string, less the lost rail's tail integral from tau to T. Under integrated balance the first quantity is GammaBar; the removed tail depends only on j,s,tau. Every such complete trajectory is therefore a logical-independent positive scalar multiplying the corresponding purely Hamiltonian trajectory. Intermediate attenuation need NOT be scalar on the code. It may leave the code, but diagonal controls stay on the same four-string support and the whole-history argument still applies.

The resulting probabilities are exactly

    P0=exp(-GammaBar),
    P1=exp(-GammaBar)[sum_i exp(M_i) cosh(D_i)-4],
    M_i=integral mu_i, D_i=integral delta_i,
    Bbad=1-P0-P1.

K2362 diagonal Z gives E<=Bbad with ideal recovery. K2365's fixed-sign monotone serial-Z schedule gives E<=Bbad+P1 min(1,2theta/n), with its original finite-cap/slew duration charged in the integrals. No jump-time observation is supplied to the recovery. Rates and logical phases may be arbitrary within the stated diagonal support-preserving model. These statements do not apply to arbitrary non-diagonal compilations.

## 3. Finite transparent-X counterexample

Work in the four actual code-support strings |r,b> := |r,r,r xor b,r xor b>, ordered (0,0),(0,1),(1,0),(1,1). Here V=|+>_r tensor I_b. K2362's full physical operator

    X_ET=(5-N)(x1 x2+x3 x4)/2

restricts on this invariant four-string space to P_+^(r) tensor X_b: x1x2 maps (r,b) to (1-r,1-b), while x3x4 maps it to (r,1-b). This restriction must be derived from the physical operator; replacing it by I_r tensor X_b is wrong off the code.

Use three intervals, with time measured in a declared unit:

1. Duration1, mu_i=ln4 for all pairs, delta=(-ln2,-ln2,-ln3,-ln3).
2. Duration t_p=1+pi/2, matched positive rates k_i(s)=ln2/t_p; drive X_ET with a zero-endpoint scalar trapezoid: rise at slope1 for1, plateau at1 for pi/2-1, fall at slope-1 for1. Its area is pi/2, scalar cap/slew1. Full Hamiltonian norm/slew are <=3/2 by K2362's norm. No instantaneous pulse is used.
3. Duration1, same mu_i=ln4 and opposite delta.

All rates are strictly positive (the smallest exposure rate is ln(4/3)). Exposure changes are prescribed piecewise-constant noise coefficients; no physical apparatus realizing rate switching is claimed or priced. The Hamiltonian pulse itself has finite amplitude, slew and duration. Preparation/recovery/readout and omitted noise remain additional debts.

Let D=diag(6,2/3,1/6,3/2). No-jump propagation in the first and last intervals is D/16 and D^-1/16. During the pulse all rates match, so the no-jump attenuation is 1/4 on the ENTIRE occupied support, including leakage from the code. The physical pulse unitary is

    U=P_+ tensor(-i X)+P_- tensor I.

Hence E0=(1/1024)D^-1 U D V and

    E0^dagger E0 = (1/1048576) [
       860809/5184       i 12025/216
      -i 12025/216        110809/5184 ].

This is not scalar. Its diagonal difference is 15625/113246208>0, already proving exact-recovery failure independently of the off-diagonal entries. The integrated rate on each occupied rail is ln32, independent of its bit, so every pair has equal final survival eta_i(0)=eta_i(1)=1/32. An idle channel with those same integrated rates would have E0=V/1024 and scalar Gram I/1048576.

Mechanism: the first unequal no-jump interval leaves the code. Error transparency constrains the code and one-loss images, not this additional no-jump leakage sector. The actual physical X_ET treats the syndrome-minus sector differently, so the later reversed imbalance cannot undo the earlier attenuation. This is an ordering effect with a physical full-support operator, not a fitted device witness.

## 4. Controls and exact evidence

The companion standard-library probe reconstructs X_ET from physical dual-rail bit operations, checks invariant support and its P_+ tensor X restriction, constructs the exact pulse unitary and Gram matrix with rational complex arithmetic, verifies positive rational rail survivals, and tests ordering changes. Removing the pulse, replacing it by diagonal transparent Z, or moving it after the two damping exposures gives a scalar no-jump Gram. A deliberately incorrect I_r tensor X extension agrees with the physical gate on V but produces a scalar no-jump Gram after the mismatched intervals; it is a diagnostic for silently substituting a logical gate on an off-code state.

These finite exact checks certify the displayed counterexample. Universal time-dependent and serial statements rest on the preceding trajectory proofs. A generic noncommuting schedule without pointwise aggregate balance requires its actual non-Hermitian time-ordered propagation and corrected Kraus family; final integrated rates alone are insufficient.
