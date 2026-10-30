---
title: "K2290 Local positive pump with an explicit signed-core compiler"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied models only; no native GU, empirical or hardware acceptance
scripts:
  - tests/channel-swings/k2290_local_positive_pump_probe.py
---

# K2290 Local positive pump with an explicit signed-core compiler

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2290 Local positive pump with an explicit signed-core compiler
carrier: complex bosonic pair and retained pump on full Fock space LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert pairing ON=declared_carrier
real_structure: complex Hilbert adjoint
grading: no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: semibounded local pump and all-charge instrument MAP-TYPE=evaluation
```

## Result and scope

The global centered Q² pump primitive used in [K2282](k2282-centered-positive-control-2026-10-29.md) can be replaced by an explicitly supplied LOCAL polynomial sum-square interaction and positive diagonal correction pulses. Unlike the failed bounded modular stabilizer in [K2287](k2287-finite-register-compensator-2026-10-30.md), every instantaneous generator here is positive on the full Fock space. A noncommuting product bound, with the actual unbounded input tails retained, gives the same complete recorded instrument within9.3e-12 for the coherent and displaced-thermal consumers below. Field energy error<.008 and pump depletion12.8±.004 survive.

The cost is extreme: 10^46 slices per original pump pulse, 6*10^47 new pulses in total, with 10^-122 absolute correction-area tolerance. The local positive nonlinear interaction, controlled diagonal coefficients, phase-controlled preparation and pulse scheduling are supplied assumptions. This is not a microscopic hardware synthesis, efficient experiment, autonomous finite clock or native GU positivity. SC-META-53 remains UNCERTAIN and LT-SM8/LT-GR6b and ledger0.263 do not move.

## 1. Whole-space positivity without a global charge square

Let A=ab for the two addressed bosonic field modes, c the pump, K=c†c and Q=N_all+2K. For mu>=1 and |z|<=2, the signed core is

    H_z=i(z A†c-conj(z) A c†)/sqrt(mu).

Set D=N_a N_b/mu+4K. Exactly,

    B_z=D+H_z
       =(A/sqrt(mu)+i z c)†(A/sqrt(mu)+i z c)
          +(4-|z|²)K >=0.

This is a quartic field-pair term plus pump number and the same trilinear cross term. It addresses only that pair and pump, not all stored outputs. The coefficient4 must dominate |z|²; dropping the quartic term generally loses positivity. The noncommuting cross terms have the displayed sign.

All these operators preserve Q. With finitely many field modes, each Q=q eigenspace is finite dimensional. Define the self-adjoint operators as direct sums of their finite Hermitian shell matrices, with domain sum_q ||B_q psi_q||² finite. The sum-square form is nonnegative on finite-particle vectors and its closed direct-sum realization is positive. Piecewise continuous bounded z(t) defines unitary evolution on each shell and hence on the full Hilbert direct sum. No unproved uniform bounded-generator assertion or physical Fock truncation is used.

## 2. The shift is not central: cancel dynamically with a proved error

D does not commute with H_z. In an upward transition (n_a,n_b,k)->(n_a+1,n_b+1,k-1),

    Delta D=(n_a+n_b+1)/mu-4.

Thus a single final diagonal inverse does not reproduce the core. Instead divide each original pump interval into r slices. For a slice of duration delta apply U_B(delta), followed by exp(+i delta D). The latter factors into exp(+i delta N_aN_b/mu) and exp(+4i delta K). Integer spectra permit both to be implemented with positive generators N_aN_b,K and nonnegative areas modulo2pi. Representatives in[2pi,4pi) keep actual areas positive under the stated small errors. This adds real control time; the target core must be paused during correction pulses. No free drift or parallel scheduling is silently granted.

On the invariant proof subspace Q<=T=4mu (integer mu), any allowed transition has |Delta D|<=4. Each row/column of H has at most two entries. Using n_a+n_b<=T and k<=T/2 gives the safe bound

    ||H_z|| <=4(T+2)^(3/2)/sqrt(mu),
    ||[D,H_z]|| <=C_T=16(T+2)^(3/2)/sqrt(mu) <=240mu.

These are deliberately loose analytic bounds. In the D interaction picture, the rotated H differs from H by at most t C_T. Duhamel then bounds one corrected slice by delta² C_T/2, even with bounded time-dependent z(t); no derivative of z is needed. For twenty original intervals each of duration tau=log3 and r equal slices, telescoping gives

    E_split <=10 tau² C_T/r <3120mu/r.

The actual z(t), including the allowed predecessor calibration, is compared with the same signed z(t) core and must satisfy |z|<=2. Ideal and actual calibrated controls are not conflated.

## 3. Infinite-input tail and correction errors

No physical cutoff is applied. Since every control conserves Q, the comparison splits into Q<=4mu and its complement. For any input purification, the latter contributes at most2 sqrt Pr(Q>4mu). The two explicit consumers start all twenty field modes in vacuum:

- Coherent pump mean mu: Q=2K, Var Q=4mu, giving E_tail<=2/sqrt(mu).
- Displaced thermal pump with n=1: E Q=2mu+2, Var Q=12mu+8, giving E_tail<=2 sqrt(12mu+8)/(2mu-2), mu>1.

These bounds are for the original pump retained along with all records and external reference. A norm bound on a purification bounds half trace distance after any allowed workspace disposal.

Suppose each positive correction pulse has absolute area error at most e while retaining its exact N_aN_b or K generator. These actual diagonal pulses still commute all field numbers and Q. Since N_aN_b<=Q²/4 and K<=Q, a pulse contributes at most e sqrt(EQ^4)/4 or e sqrt(EQ²). Hybrid telescoping over20r of each kind gives

    E_area <=20r e [sqrt(EQ^4)/4+sqrt(EQ²)].

For mu>=1 the coherent preparation obeys the sufficient bounds4mu² and4mu. The displaced thermal n=1 preparation obeys22mu² and6mu: its raw pump moments have E K^4=mu^4+22mu³+133mu²+233mu+75<=464mu^4, and E K²=mu²+5mu+3<=9mu². The weaker constants22 and6 are retained deliberately. No tail or amplitude estimate substitutes for these moments. Also price the positive pump's diagonal errors. On each B interval, let its actual generator be H_z+a(t)N_aN_b+b(t)K, with a(t)>=3/(4mu), b(t)>=3 and the inherited calibrated |z|<=1+3*10^-17<3/2. Then a(t)b(t)>=9/(4mu)>|z|²/mu, so square completion still proves positivity. Require integral |a-1/mu|dt<=e and integral |b-4|dt<=e per slice. Duhamel bounds that extra error by the same moment expression per interval; integrated absolute error, not merely signed area, is essential because H does not commute D. Thus the full diagonal allowance is twice E_area. Duration jitter must be included in these bounds or controlled explicitly. Arbitrary idle/free drift over the enormous correction time is not covered.

## 4. Complete consumers and energy followthrough

Use r=10^46, e=10^-122, coherent mu=10^28 or thermal mu=4*10^28, and the SAME predecessor signed-core bound

    E_core=600(1+10^-17)/10^14+440/(2^50+1)
                          +(3600+22000+260100)10^-17 <9.25e-12.

For thermal input, E_split<=1.248e-14, E_tail<1.734e-14 and 2E_area<1.41e-16. Coherent bounds are smaller in sum. Total error is below9.3e-12, still with the original pump retained. There is no final global compensator in this construction: each local diagonal shift is removed by the interleaved compiler. Counts are20r positive B intervals and40r positive number-product/number corrections. Precise modular phase computation belongs inside e; it is not free floating-point arithmetic. The initial huge pump stock and elapsed correction time are not removed from the resource account.

The [K2279](k2279-uniform-pump-energy-2026-10-29.md)/[K2285](k2285-thermal-centered-composition-2026-10-30.md) moment proof survives for their fixed fresh-register consumers: D and every correction commute each addressed field number, so only H contributes to the weighted-number commutator growth. Total H exposure and its bound are unchanged; other output registers remain isolated. This preserves the upper second-moment bound6,300,000, NOT equality of number trajectories. K2273's sharp inequality then gives field-number error<=sqrt(6,300,000*9.3e-12)<.008. Exact Q conservation and ideal field mean25.6 give pump depletion12.8±.004. Energy is not returned catalytically; total engineering work is unpriced.

## 5. Countercontrols and next construction

Finite-shell matrices check actual square completion, negative eigenvalues when stabilization is removed, nonzero [D,H], and corrected-product convergence against exp(-itH). The infinite-dimensional result rests on positivity by direct sums, the entrywise commutator proof, Duhamel and moment/tail inequalities. Dropping interleaving, using the wrong cross-term sign, omitting pump weight2 in Q or using only a bounded modular stabilizer are not harmless compiler choices.

This construction removes the global centered nonlinear primitive by changing the supplied local alphabet. It does not derive that alphabet from conventional low-order laboratory couplings. The hardest next useful question is physical synthesis and calibration of the positive local square interaction while retaining the same error and moment guarantees. More decimals or finite-shell controllability cannot supply it. Nor does mere tensor locality establish spatial adjacency, controllable isolation or timing. No novelty, external-expert, Lean or hardware certification is claimed.
