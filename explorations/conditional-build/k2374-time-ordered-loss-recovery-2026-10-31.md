---
title: "K2374 Sharp time-ordered loss-recovery criterion for transparent X/Z"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional finite-Hilbert mathematics; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2374_time_ordered_loss_recovery_probe.py
---

# K2374 Sharp time-ordered loss-recovery criterion for transparent X/Z

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
result: K2374
carrier: K2356 eight dual rails, its four intact support strings and eight fixed one-loss syndrome sectors LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and the complete continuum Kraus Knill-Laflamme kernel ON=declared_carrier
real_structure: complex finite-dimensional matrices with real positive piecewise continuous rates
grading: intact syndrome r, logical b, erased pair j, lost bit s and unobserved loss time
action_owner: repository-construction -- independent Markov damping and actual supplied K2362 X_ET/Z_ET controls
target: necessary-and-sufficient schedule criterion and cross-time correction discriminator MAP-TYPE=evaluation
```

## Result and scope

K2371 proves that total integrated balance can fail under the actual noncommuting transparent X control. Here the complete unknown-time Kraus family gives a sharp criterion for a finite-block class of X/Z schedules. It is stronger than testing either the no-jump Gram or each individual jump Gram: two individually reversible jump-time maps can demand incompatible recoveries.

Let H(t)=h(t)X_ET+g(t)Z_ET with the actual physical K2362 operators. Let k_i(s,t)=mu_i(t)+(-1)^s delta_i(t)>0 be independent occupied-rail damping rates, piecewise continuous on a finite interval; assume a positive lower bound and finite upper bound. Controls are piecewise continuous and bounded. Assume the schedule has finitely many X-active intervals, on whose interiors h(t) is continuous and nowhere zero, separated by maximal X-idle blocks on which h=0. Adjacent zero-X subintervals are merged even when rates or g change; merely splitting an idle block for calculation does not impose separate balance on its pieces. The scalar g(t) can be nonzero on either type. Isolated endpoints and rate discontinuities are interpreted by one-sided limits and do not affect the channel.

Put A=delta1+delta2, B=delta3+delta4 and Gamma=sum_i mu_i. Then the complete zero/one-pair-loss subchannel has an exact trace-preserving end recovery, with loss time unobserved, **if and only if**:

1. A(t)=B(t)=0 almost everywhere on every X-active interval; and
2. integral A=integral B=0 separately on every X-idle interval, including the initial and final idle intervals when present.

Precisely, this means a completely positive trace-preserving decoder R with R composed with E_good equal to p_good U_L(·)U_L†, where p_good=P0+P1 is input-independent. The decoder does not restore omitted bad-history probability. Composing with U_L† gives recovery of the input instead; existence of correction is unchanged by this known unitary. In the necessity argument, no target value of the no-jump logical gate is assumed: scalar full Kraus products alone force the stated schedule conditions. The specified U_L is obtained in the constructive sufficiency argument.

If there are no X-active intervals, condition2 is K2371's idle/diagonal integrated-balance result for the whole interval. Zero-duration idle intervals have no condition. This theorem does not cover an arbitrary infinite zero set of h, more general transparent controls, ancillas, monitored jump times or approximate recovery. It is conditional positive-Hilbert apparatus mathematics; no source claim, native GU physical-state result, measured hardware or novelty certification follows.

## 1. Actual time-ordered carrier reduction

Use the actual intact strings |r,b>=|r,r,r xor b,r xor b>, ordered r then b. V|b>=|+>_r|b>. From physical pair exchanges, x1x2 sends (r,b) to (1-r,1-b), while x3x4 sends it to (r,1-b). With N=4,

    H0(t)=h(t) Pplus_r tensor X_b + g(t) I_r tensor Z_b,
    R0(t)=Gamma(t)I + Z_r tensor [A(t)I+B(t)Z_b].

Here Pplus=(I+X_r)/2. The no-jump 4-by-2 matrix C(t) obeys C'=(-iH0-R0/2)C and C(0)=V. This is a time-ordered non-Hermitian evolution, not a substitution of integrated rates into a stationary channel. Write its two 2-by-2 row blocks C_0,C_1.

After loss of pair j in L={1,2} with bit s, the remaining pair in L fixes r=s, and the two b states span a fixed two-dimensional output syndrome sector. The actual physical X_ET restricts to X_b there: its coefficient becomes1 at N=3 and only x3x4 survives. Z_ET restricts to Z_b. Thus

    G_js(t)=-ih X-ig Z-[Gamma I+(-1)^s(A I+B Z)-k_j(s,t)I]/2.

Let P_js(T,t) be its invertible two-dimensional no-jump propagator. The exact one-loss trajectory map, in this physical output basis, is

    J_js(t)=sqrt(k_j(s,t)) P_js(T,t) C_s(t).

For j in R={3,4}, the lost bit satisfies r xor b=s, giving the analogous two-row selection and corresponding physical generator. Different j and s output sectors are orthogonal and remain so under these controls. The full correction discriminator is C(T)†C(T) scalar and J_js(t)†J_js(u) scalar for every same-sector pair of times (almost everywhere). Cross-sector products vanish physically. In particular, checking only t=u discards a required condition.

## 2. Necessity on every X-active interval

A fixed (j,s) output sector has dimension2, exactly the logical dimension. Complete cross-time Knill-Laflamme therefore forces all nonzero maps in that sector to be scalar multiples of one fixed unitary W_js: choose one nonzero J with scalar positive Gram, invert it, and apply its scalar cross products to every other J. Dividing by sqrt(k)>0 preserves this conclusion.

Where C_s is nonzero, it is consequently invertible and P_js(T,t)C_s(t)=f_s(t)W_js. Differentiate, using dP_js(T,t)/dt=-P_js(T,t)G_js(t). The physical generators from section1 give

    C'_s-G_js C_s = (ih/2)X(C_s-C_(1-s))-(k_j(s,t)/2)C_s.

Hence, where h is nonzero,

    X(C_s-C_(1-s))=alpha_s C_s,
    C_(1-s)=(I-alpha_s X)C_s.

Applying this for both s gives (I-alpha_1 X)(I-alpha_0 X)=I. Independence of I and X yields alpha_0+alpha_1=0 and alpha_0 alpha_1=0, so both vanish. Thus C_0=C_1.

There is no missing zero-amplitude escape. Exact correction makes each C_s either invertible or zero. The stacked C has rank2 because its full no-jump propagator is invertible. If C_s were zero at an interior point with h nonzero, C_(1-s) would be invertible and the ODE would give C'_s=-(ih/2)X C_(1-s), invertible. Both row blocks would then be invertible in a punctured neighborhood, where the preceding argument forces equality; continuity contradicts C_s=0 and C_(1-s) invertible. Apply this on each continuity subinterval and pass through its finite boundaries by continuity.

Finally subtract the two no-jump row equations while C_0=C_1=C_*:

    0=C'_0-C'_1=-(A I+B Z)C_*.

Invertibility forces A=B=0 almost everywhere on the X-active interval. The no-jump state is therefore on the code there, with scalar damping and the intended logical X/Z propagation. This is a complete same-sector time-kernel obstruction, not a finite-difference or selected-time argument.

## 3. Necessity and sufficiency of separate idle balances

On an X-idle block [a,b], the no-jump rate and Z controls are diagonal on the four actual strings. Starting with C(a)=V times an invertible logical matrix, its r blocks differ by the positive diagonal factor exp[-integral_a^b(A I+B Z)]. They coincide at the next active interval exactly when both block integrals vanish. This proves necessity for the initial and every interior idle block.

For a final idle block, take the limit of one-loss trajectories at T. In a loss sector j in L, scalar J_js(T)†J_js(T) requires integral B=0. For j in R it requires integral A=0; the preceding logical matrix is scalar times unitary because the previous active and balanced-idle blocks have already been proved. Strict positivity keeps all these terminal-limit branches nonzero. Continuity makes the endpoint-limit conditions necessary for the almost-everywhere kernel. This also proves the all-idle case with initial V.

Conversely, pointwise balance on each active block makes the rate scalar on V and on every A_js, so physical transparency propagates the same intended logical gate on each. On each complete balanced idle block, the full-history diagonal cancellation of K2371 applies, including a jump partway through the block: the removed lost-rail tail depends only on j,s and the jump time, never logical input. Each other idle block is scalar on the appropriate intact or one-loss image. Composing blocks therefore makes every good trajectory a scalar times V U_L(T), or A_js U_L(T), where U_L is the actual time-ordered logical hX+gZ propagator. K2356's syndrome decoder followed, if desired, by U_L(T)† recovers every logical state with every reference. No jump-time measurement is used.

Under these conditions, the same exact good probabilities survive:

    GammaBar=integral Gamma, M_i=integral mu_i, D_i=integral delta_i,
    P0=exp(-GammaBar),
    P1=exp(-GammaBar)[sum_i exp(M_i)cosh(D_i)-4],
    Bbad=1-P0-P1.

Indeed the squared scalar density for branch (j,s,t) is exp(-GammaBar) k_j(s,t)exp[integral_t^T k_j(s,u)du]/2; its time integral proves the expression. With a trace-preserving fallback on two-or-more losses, reference-aware half-diamond error is at most Bbad. Preparation, recovery, readout, rate switching and omitted noise remain unpriced apparatus debts.

## 4. Exact no-jump-pass, cross-time-fail discriminator

Use K2371's three finite intervals and finite trapezoid X pulse, changing only the first exposure to mu_i=ln4 and delta=(-ln2,-ln2,0,0); the final exposure has opposite delta. The pulse has duration1+pi/2, matched rates ln2/(1+pi/2), cap/slew1 and area pi/2. All physical rail rates are positive, final occupied-rail survival is1/32 for both bits of every pair, and every integrated aggregate balance vanishes. The pulse is finite, not instantaneous; noise switching is supplied piecewise-constant data.

Let D=diag(2,2,1/2,1/2). First and final no-jump exposures are D/16 and D^-1/16. During the pulse intact attenuation is1/4 and

    U=Pminus tensor I - i Pplus tensor X,
    E0=(1/1024)D^-1 U D V,
    E0†E0=(289/67108864)I.

Thus even the actual no-jump KL test PASSES. In the physical pair1, lost-bit0 syndrome, consider the one-sided limits of losses at the start and end of the matched pulse. Strip only their nonzero scalar attenuation and jump-rate factors, and the common normalization1/sqrt2. The actual remaining matrices are

    J_start=-2iX,
    J_end=(3/4)I-(5/4)iX.

Both individual Grams are scalar:4I and17I/8. Their cross product is

    J_start†J_end=(5/2)I+(3/2)iX,

which is not scalar. Restoring their nonzero scalar prefactors cannot fix it. The two limit times themselves have zero measure, but the finite pulse and time propagators are continuous, so a nonzero nonscalar cross entry persists in product neighborhoods of positive measure inside the pulse. Exact recovery of the complete good subchannel is impossible. This is not a claim that *every* individual branch Gram elsewhere in this channel is scalar.

Removing the drive restores the original integrated-balance recovery theorem; taking D=I removes the cross-time defect; an arbitrary I_r tensor X replacement changes the actual off-code physical operator and is not an admissible proof of correction for X_ET. The companion probe checks the actual physical restrictions, the exact rational-complex witness, balanced and zero-pulse controls, and the loss-sector restrictions. Written time-ordered proofs carry the universal classification; finite matrix checks certify only their named fixtures.

## 5. Constructive noncommuting schedule with genuinely unequal rails

The criterion permits finite unequal-rate exposures and noncommuting logical gates. Take two unit-duration X-idle intervals whose single occupied-rail no-jump amplitude rows are respectively

    lambda_first=((1/2,1/8),(1/2,1/8),(1/3,1/12),(1/3,1/12)),
    lambda_second=the bit-swapped rows of lambda_first.

The positive rates are k_i(s)=-2 log(lambda_i(s)); pairwise integrated equality over this complete idle block implies both aggregate balances. During the first exposure implement a finite diagonal Z_ET pulse of area pi/2 (arbitrary finite cap/slew may be chosen consistently with the unit duration; no cap1 is asserted here). Then apply the finite matched-rate X_ET pulse above. Logical X and Z do not commute, each idle half has nonzero imbalance in both groups, but the entire idle block balances before X becomes active. This satisfies the theorem and is exactly correctable on all good histories. It illustrates why a global pointwise-balance requirement would be too strong.

The exact probe evaluates losses in all eight (j,s) sectors at the exposure boundaries and at an interior point of the X pulse with accumulated cos(theta)=3/5, sin(theta)=4/5. It builds each pre-jump four-string propagator, actual erasure row selection and post-jump two-string propagator. All pairs of sampled times satisfy same-sector KL, and every branch is a nonzero scalar times the common ordered logical X/Z gate. Only scalar matched-rate attenuation and jump-rate prefactors are stripped; the full unequal diagonal attenuation is retained before and after loss. These are finite exact reproducibility controls for the general written trajectory proof, not claims of sampling every loss time.
