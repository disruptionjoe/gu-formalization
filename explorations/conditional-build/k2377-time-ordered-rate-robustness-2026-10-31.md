---
title: "K2377 Survival-weighted robustness of time-ordered physical loss channels"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional complete-channel continuity; no measured hardware certificate
scripts:
  - tests/channel-swings/k2377_time_ordered_rate_robustness_probe.py
---

# K2377 Survival-weighted robustness of physical loss channels

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
result: K2377
carrier: four ternary dual-rail pairs, code qubit and arbitrary reference LAYER=toy CHIRALITY=N/A
pairing: ordinary positive Hilbert form and trace distance ON=declared_carrier
real_structure: complex finite Hilbert space with real nonnegative loss rates
grading: occupation sectors and classical emitted-loss histories
action_owner: repository-construction -- supplied physical transparent X/Z Hamiltonian and independent Markov losses
target: complete-channel continuity and fixed decoder error MAP-TYPE=evaluation
```

## 1. Precisely typed comparison

Use the at-most-one-excitation-per-pair invariant carrier of four dual rails:
each pair has vacuum and two occupied-bit states. The input is the K2356 code
V|b>=(|00bb>+|11,1-b,1-b>)/sqrt(2). The pairing is the ordinary positive Hilbert
form. Put n_is=|s><s| on pair i and N_i=n_i0+n_i1. The physical jump operator is
a_is=|vac><s| and L_is(t)=sqrt(k_i(s,t)) a_is. Rates are positive, bounded,
piecewise continuous, with positive lower bound. The comparison k' satisfies
the same conditions. Both complete channels have the SAME supplied bounded
Hamiltonian h(t) X_ET + g(t) Z_ET, with the ACTUAL K2362 full-support operators.
The actual transparent operators conserve every N_i. They do not create a
second excitation or repopulate an empty pair.

This result compares complete trace-preserving physical channels, including
every multiple-loss history. It does not normalize the good subchannel, assume
the actual good probability is state independent, or assert that approximate
same-time Kraus Grams certify unknown-time recovery.

Define

    d_is(t) = (sqrt(k_i(s,t)) - sqrt(k'_i(s,t)))^2,
    m_i(t) = max_s d_is(t),
    alpha_i(t) = min_s k_i(s,t),
    alpha'_i(t) = min_s k'_i(s,t),
    Q = sum_i integral_0^T m_i(t)
          exp[-1/2 integral_0^t (alpha_i(u)+alpha'_i(u))du] dt.

Then for the encoded input, with arbitrary reference,

    (1/2)||E_k V - E_k' V||_diamond <= min(1,sqrt(Q)).

A slightly sharper optional expression is sqrt(Q-Q^2/4) for 0<=Q<=2,
and 1 for Q>=2. Use the simple expression unless the extra detail helps.

## 2. Complete common-history overlap proof

Use a common trajectory environment recording every emitted loss label and
continuous jump time, and retain the physical output system. Let Psi(t) and
Psi'(t) be the resulting normalized joint pure states for the same arbitrary
purified encoded input. All histories are present, so both norms are one.
The different trajectories are not conditioned or individually normalized.
Finite Hilbert dimension, bounded coefficients and finite duration ensure the
usual convergent time-ordered trajectory expansion; in this carrier there can
be at most four loss events. Thus the formulas can be derived directly by
differentiating the finite sum of ordered trajectory integrals. No stochastic
calculus theorem or quantum error-correction continuity theorem is required.

For a current common history, the pair of no-jump generators are
G=-iH-(1/2)sum L†L and G'=-iH-(1/2)sum L'†L'. Differentiation contributes
G'†+G, and the moving upper integration boundary for a new common jump
contributes sum L'†L. Their sum is exactly

    G'†+G+sum L'†L = -D(t)/2,
    D(t)=sum_is d_is(t) n_is.

The same Hamiltonian cancels, and L'†L=sqrt(kk') n_is is real and parallel.
Let z(t)=<Psi'(t),Psi(t)>. The identity is

    z'(t)=-1/2 <Psi'(t),(D(t) tensor I_history,reference)Psi(t)>.

Equivalently the bracket is the sum/integral over current common histories.
This is a cross-history overlap derivative, not a master equation for the
physical density matrix. Retaining only zero/one losses breaks the norm-one
step below and is not an admissible shortcut.

The operator D_i=sum_s d_is n_is is supported on N_i and has norm m_i.
Consequently

    |<Psi',D_i Psi>| <= m_i ||N_i Psi'|| ||N_i Psi||
                     = m_i sqrt(p'_i p_i).

Since [H,N_i]=0, the physical master equation gives

    p_i'(t) = -sum_s k_i(s,t) <n_is> <= -alpha_i(t) p_i(t).

Every code input starts with p_i(0)=1, including entangled logical inputs.
Hence p_i(t)<=exp(-integral_0^t alpha_i), and likewise for the comparison.
Integrating z(0)=1 yields Re z(T)>=1-Q/2, uniformly over purified inputs.
Therefore ||Psi-Psi'||^2=2-2 Re z<=Q. Partial trace contracts trace distance;
pure-state trace distance is sqrt(1-|z|^2)<=min(1,sqrt(Q)). Taking the supremum
over the reference gives the stated half-diamond bound. For Q<=2 one can use
|z|>=Re z>=1-Q/2 to obtain the optional sharper expression.

Without the occupancy argument one still gets Q0=integral sum_i m_i,
because ||D||=sum_i m_i on the full ternary carrier. Q<=Q0. The generic
comparison needs neither exact K2374 balance nor a recovery assumption.

## 3. Recovery consequence and honest comparison

If k' satisfies K2374's sharp schedule criterion, its fixed syndrome decoder
R and a trace-preserving fallback give the specified intended logical gate U
with half-diamond error at most Bbad'. Contractivity and the triangle inequality
give

    E_actual(R,U) <= min(1, Bbad' + min(sqrt(Q), D1)),
    D1 = integral_0^T sum_is |k_i(s,t)-k'_i(s,t)| dt.

D1 is the existing safe generator/Duhamel comparison with the same reference.
Neither comparison uniformly dominates. The new term is a full physical
trajectory continuity certificate, not a sharp optimal recovery error or lower
bound. Large background damping often makes Bbad' large; in that regime an
improved perturbation estimate alone need not improve a useful total budget.
One must evaluate both terms and the baseline failure probability.

The same decoder R is physically specified in advance; it does not use jump
times or recalibrate itself to the actual rates. The common environment exists
only in the proof. Identical actual and reference rates give Q=0. Different exactly correctable schedules can have Q>0; exact correctability alone does not make this comparison vanish. There is no claim that comparing to an arbitrary chosen
reference optimizes the certificate.

## 4. Nonvacuous exact survival fixture

Use an idle duration of one declared unit. The reference is pairwise matched:

    k'_1(0)=k'_1(1)=100 ln 2,
    k'_i(0)=k'_i(1)=ln(1000/999), i=2,3,4.

The actual rates differ only in k_1(0)=121 ln 2. Put

    a=2^-100, c=2^-121, b=999/1000.

All finite survival probabilities are rational. All rates are strictly positive.
Both schedules have alpha_1=alpha'_1=100 ln2, while m_1=ln2 and other m_i=0.
Thus

    Q=(1-a)/100 < 1/100,
    Bbad'=1-b^3-3 a b^2(1-b) < 1-b^3 < 3/1000.

The survival-weighted total certificate is therefore <103/1000. The L1 debt
for the very same reference is 21 ln2>1, hence vacuous. This is not merely an
improvement after the whole experiment has already failed: only the first
pair is almost certain to be lost, while the other three remain highly likely
to survive, and this code corrects one loss. The new bound is still loose.

For an independent endpoint certificate, use the two-Kraus damping dilation for each single rail (the vacuum/0/1 pair has three Kraus operators). This endpoint dilation is distinct from the continuum jump-time dilation used in the theorem. Unaffected channels cancel from this endpoint overlap. On the altered occupied rail its overlap
is f=sqrt(a c)+sqrt((1-a)(1-c)); it is one on the unaltered bit and vacuum.
Since V†n_10 V=I/2, the exact code-compressed overlap is (1+f)I/2. Therefore
the squared difference of these endpoint dilations is 1-f, and elementary rational
inequalities give 1-f<=a+c<Q. The accompanying probe proves the latter via
(1-a)(1-c)>=(1-a-c)^2 and a+c<Q, never by floating-point comparison. Thus the
direct finite fixture is substantially tighter than the general theorem.

The shared continuous-time environment also has an explicit independent check. For one occupied rail at constant rates k,kprime, summing the no-jump overlap and integrating the one-jump overlap gives

    f_time=exp(-(k+kprime)T/2)
           +2sqrt(k kprime)/(k+kprime)*(1-exp(-(k+kprime)T/2)).

For this fixture f_time=220/221+sqrt(ac)/221, so code overlap is (1+f_time)/2 and the time-resolved squared dilation distance is (1-sqrt(ac))/221 < 1/221 < Q. This verifies the continuum consumer directly. The endpoint f above uses a different environment representation and is much tighter here; neither dilation supplies an optimal recovery theorem.

One may append an identical finite matched-rate transparent X or X/Z segment
to both channels. Complete-channel distinguishability cannot increase, and the
new Q integrand is zero in that segment. Baseline Bbad' must be recalculated
using the added exposure. A finite cap/slew pulse must keep its actual duration;
do not call this continuation free or silently substitute I_r tensor X for
the actual Pplus_r tensor X action on intact leakage.

## 5. Cheap positive and assumption-breaking controls

The standard-library probe checks exactly: physical X_ET transition
edges preserve each pair's occupancy on all 81 ternary states; Z_ET is diagonal;
the code compression V†n_10 V=I/2; the closed rational survival fixture; its
finite Stinespring-overlap certificate; matched-rate Q=0; and a small-exposure
case where the old L1 bound is provably stronger.

Missing-occupancy control: on one physical qubit, damp occupied probability to
1/4 and then apply the vacuum/occupied flip. Occupancy becomes 3/4, exceeding
the purported no-pump survival envelope 1/4. The flip fails [H,N]=0. This is
an exact algebraic assumption test, not an admitted physical control schedule
or an instantaneous-pulse hardware claim. The unweighted Q0 bound remains
available for same-H rate comparisons even when the survival sharpening fails.

Preparation, recovery, readout, unmodelled Hamiltonian mismatch, heating,
correlated noise, and measured calibration data remain unpriced. The result
does not relax the exact K2374 criterion or turn an unequal-rate channel into
an exactly correctable one. Its scope is a rigorously sufficient approximate
full-channel certificate for the stipulated independent-loss model.

## Scientific boundary and provenance

[K2374](k2374-time-ordered-loss-recovery-2026-10-31.md) supplies exact baseline recovery; [K2368](k2368-unequal-rail-recovery-2026-10-31.md) supplies the retained L1 comparison. No native GU positive physical quotient is constructed, and SC-META-53 remains UNCERTAIN at its recorded scope. The comparison is internal conditional apparatus mathematics, not empirical noise estimation or source validation. Exact finite checks validate the displayed fixtures and full-carrier occupancy invariant; the continuum bound rests on the written proof. Internal agent review is not external expert or proof-assistant certification.
