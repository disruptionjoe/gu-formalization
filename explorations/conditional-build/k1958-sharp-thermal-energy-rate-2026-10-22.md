---
title: "K1958: Sharp logarithmic mean-energy cost for the fixed thermal channel"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional fixed quantum model; no GU derivation, sharp additive constant or novelty claim
scripts:
  - tests/channel-swings/k1958_sharp_thermal_energy_rate.py
  - tests/channel-swings/k1958_sharp_thermal_energy_rate_probe.py
---

# K1958: The sharp logarithmic energy coefficient

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
result: sharp leading mean-energy cost and two-sided exponential return rate
carrier: fixed four-state extreme Schur channel, bath t=1/2, arbitrary finite nondegenerate nonnegative catalyst spectrum LAYER=toy CHIRALITY=N/A
pairing: Hilbert trace and worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex physical shell unitaries, rational energy-pinched populations
grading: additive energy shells, no source chirality
action_owner: repository-construction -- exact conserving channel implementation
target: uniform initial mean-energy resource law MAP-TYPE=intertwiner
```

## 1. Result

In exactly [K1956](k1956-finite-energy-thermal-gap-2026-10-22.md)'s model, write
`r0=4/25`, and let `E_min(delta)` be the infimum of initial mean energies of
finite protocols with worst-input marginal return at most `r0+delta`. Then

    E_min(delta) = [2/log(3/2)] log(1/delta) + O(1), delta -> 0+.

Equivalently, `R_star(E)-r0 = Theta((2/3)^(E/2))` as E tends to infinity.
This closes K1956's gap between leading lower/upper constants. It determines
neither the additive O(1) term nor the exact all-energy frontier. The existing
finite-energy facets and K1954's counterexample to a proposed secant survive.
No limit protocol, infinite-dimensional unitary, GU identification or external
acceptance is asserted.

## 2. A uniform displacement moment

Use K1956's population-consistent acyclic matrix D and put `A=D^-1`.
Set `q=2/3`, `W=25/8`, `c=163/440`, `C=36`, `a=log(3/2)/2`.
For a root j and a reachable vertex i at path distance n, the direct recurrence
for the inverse column has root value at most1 and each step ratio at most q.
Indeed a left step has ratio at most `L_d/(1+H_d)` and a right step at most
`H_d/(1+L_d)`; an additional incoming edge only increases its diagonal.
Acyclicity leaves one directed path, or none. Thus

    0 <= A_ij <= q^|i-j|.

At most two vertices have path distance n, each energy displacement at most3n.
Different resonance components contribute zero. Consequently, uniformly over
all dimensions, spectra, fractional offsets and orientations,

    sum_i |e_i-e_j| A_ij <= 6 sum_(n>=1) n q^n = 36 = C.       (1)

Let `w_j=sum_i A_ij`. K1956 already proves `0<w_j<=W-c exp(-a e_j)`.
For every L>0 the function `f_L(e)=min(e,L)` is1-Lipschitz, so (1) gives

    sum_i f_L(e_i) A_ij >= f_L(e_j) w_j-C.                    (2)

The cap is essential: the negative deficit can occur at arbitrarily large
energy, and its small total mass does not bound its untruncated first moment.

## 3. Keep the negative deficit instead of dropping it

For a normalized diagonal population p, set `Dp=u-v` with disjoint positive
parts u,v. Then `p=A(u-v)`, `m=sum u=2R(p)`, and

    h=Wm-1,
    d=sum_j (W-w_j)u_j,
    b=sum_j w_j v_j,
    h=d+b >= 0.                                             (3)

These are exact identities, not approximations near the floor. Since
`f_L^T A v<=L b`, (2) and `0<=f_L<=L` yield

    E >= f_L^T p
      >= sum_j f_L(e_j)w_j u_j-Cm-Lb
      >= W sum_j f_L(e_j)u_j-Cm-L(d+b).

Thus `sum f_L(e_j)u_j <= (E+Cm+Lh)/W`. Also

    exp(-a e) >= exp(-a min(e,L))-exp(-aL).

Jensen's inequality for the probability weights u/m now gives

    h >= d >= c sum_j u_j exp(-a e_j)
      >= cm {exp[-a(E+Cm+Lh)/(Wm)]-exp(-aL)}.                (4)

Unlike K1956's earlier bound through `u<=p`, this uses almost all normalized
resolvent mass and therefore preserves the sharp leading energy coefficient.
The exact finite controls also check (1)--(3) for orientations unrelated to p;
physical use selects the actual orientation so m/2 is the sharp population
return lower bound.

## 4. An explicit lower bound and its inverse

Suppose the actual physical return is at most `r0+delta`. Pinching as in
K1933/K1943 supplies a feasible diagonal comparison of unchanged mean energy
and no larger return. Its population lower bound therefore satisfies
`0<=h<=epsilon=2W delta`, with `1/W<=m<=(1+epsilon)/W`.
For `0<epsilon<1`, choose `L=(2/a)log(1/epsilon)` and write
`B(epsilon)=W epsilon/c+epsilon^2`. Whenever B(epsilon)<1, (4) implies

    E >= (1/a)log[1/B(epsilon)]
         - C(1+epsilon)/W
         - (2/a)epsilon log(1/epsilon).                    (5)

To check the inequality direction: (4) bounds the positive exponential above
by `h/(cm)+epsilon^2 <= B(epsilon)`. Taking logs first gives
`E >= (Wm/a)log(1/B)-Cm-Lh`; then use `Wm>=1` and `log(1/B)>0`.
Thus (5) holds for EVERY finite physical protocol, coherent included, and
survives the infimum over dimensions and spectra. Since epsilon=2W delta,
it is `(1/a)log(1/delta)-O(1)`. In particular the negative-deficit correction
`epsilon log(1/epsilon)` tends to zero; it does not change the leading rate.

## 5. Matching physical upper bound and useful consumers

Reuse K1956's actual finite, padded, nondegenerate shell protocols, with n
left and right gap2 edges: `R_n-r0 <=(17/50)q^n` and
`E_n<=2n+41/32`. The complete complex target channel and all-input marginal
return are verified by that construction, not inferred from a population
linear program. Taking

    n=ceil(log[(17/50)/delta]/log(3/2))

gives `E_min(delta)<=(1/a)log(1/delta)+O(1)`, matching (5). Each n is a finite
protocol; this argument never exchanges an infinite unitary with a limit.
Conversely choose n=floor((E-41/32)/2) for large E to obtain
`R_star(E)-r0<=constant*exp(-aE)`. The uniform lower bound (5) gives the
opposite inequality with another positive constant: after restricting to any
fixed sufficiently small delta range, its bounded remainder gives
`delta>=constant*exp(-aE)`. Protocols outside that range already satisfy the
same weaker asymptotic bound. Infima need not be attained for this argument.

This prices initial catalyst mean energy only. Preparation work, bandwidth,
number of levels, control complexity, joint product return and repeated-use
cost remain distinct. Degenerate spectra, another bath, approximate channels
or initial correlations are different problems. Source SC-META-53 remains
UNCERTAIN and LT-SM8/LT-GR6b/AC-F1 remain NEEDS; no ledger verdict changes.

## 6. Verification and remaining question

The producer checks exact rational inverse columns, geometric envelopes,
displacement moments, signed-deficit balance, capped-energy inequalities and
seven physical-family energy/return formulas. The separate probe reconstructs
bath coefficients and inverse columns by a directed recurrence, without
importing the producer. Mathematical input faults follow a green baseline;
identity and input-pin faults are separate reporting checks. Universal
quantifiers, Jensen and asymptotic inversion are the analytic proof above,
not conclusions drawn from finite sampling. Internal review is not independent
external expert acceptance or proof-assistant certification.

Known energy limitations for thermal catalysis remain context, rather than a
novelty claim; see [Ng et al.](https://arxiv.org/abs/1405.3039), already cited by
K1956. The next distinct question is the sharp bounded remainder or limiting
amplitude/possible log-periodic modulation, not another test of the logarithmic
order or leading exponent. A full finite-energy formula still needs a global
certificate and must preserve the rejected-secant counterexample.
