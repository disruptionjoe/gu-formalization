---
title: "K1956: Finite energy stays above the thermal floor"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-channel conditional mathematics; no sharp constant, native GU, novelty or formal proof claim
scripts:
  - tests/channel-swings/k1956_finite_energy_thermal_gap.py
  - tests/channel-swings/k1956_finite_energy_thermal_gap_probe.py
---

# K1956: A uniform energy gap and logarithmic resource order

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
result: uniform finite-mean-energy separation from the positive thermal floor and logarithmic excess-error resource order
carrier: fixed four-state extreme Schur channel, four-level Gibbs bath t=1/2, finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex shell unitaries and energy-pinched rational probabilities
grading: additive energy shells; no source chirality
action_owner: repository-construction -- exactly energy-conserving channel implementation
target: unrestricted finite-spectrum mean-energy return infimum MAP-TYPE=intertwiner
```

## 1. Result and the question it settles

Use exactly [K1943](k1943-arbitrary-preparation-catalyst-energy-2026-10-22.md)'s
model: the four-state extreme Schur channel, bath energies 0,1,2,3 with
probabilities proportional to `(1/2)^b`, independent initial registers,
exact additive energy conservation and a finite nondegenerate nonnegative
catalyst spectrum with ground 0. Energy is in units of the bath spacing.
Return is the worst-system-input catalyst MARGINAL half trace distance.
Let `R_star(E)` be its infimum with initial mean energy at most E.

For every finite E>=1,

    R_star(E) >= 4/25 + (652/34375)(2/3)^(25E/16) > 4/25.       (1)

[K1935](k1935-arbitrary-support-thermal-return-2026-10-22.md) proved that
each finite catalyst lies above 4/25, and that increasing resources approach
it. Strictness for every individual finite object does not imply a uniform
gap at a fixed mean energy when dimensions and spectra vary. Equation (1)
closes that distinction without enumerating more energy-frontier facets.
[K1936](k1936-bounded-energy-catalyst-return-2026-10-22.md)'s entropy bound
separates return from zero under an additional spectral growth condition;
it does not give this gap above the positive four-level-bath floor.

The explicit constructions below show that the minimum mean energy needed
for return at most `4/25+delta` has order `log(1/delta)` as delta tends to
zero. The constants and exponential rate in (1) are not asserted optimal.
This is independent conditional mathematics, not a GU prediction.

## 2. Preserve the actual orientation and positive part

By K1933/K1943, a coherent feasible preparation has an energy-diagonal
feasible comparison with no larger energy or return. It suffices to bound
every diagonal preparation. Write its population p over all occupied sites.
In each resonance component, gaps d are 1,2,3 and successive gaps satisfy
`d_i+d_(i+1)>=4`. Set

    L_d=sum_(b=0)^(3-d) t^b/Z_bath, H_d=t^d L_d, t=1/2.

Choose each edge orientation using its ACTUAL population imbalance
`H_d p_low-L_d p_high`. Define I as the sum of the nonnegative incoming
excesses and `D p=p-I`. K1943 proves that the sharp return is
`R(p)=sum_i (Dp)_i,+ /2`. For this population-consistent orientation,

    u=(Dp)_+, 0<=u_i<=p_i, m=sum u_i=2R(p)<=1,
    sum e_i u_i <= sum e_i p_i <= E.                          (2)

The inequality u<=p is not claimed for an arbitrary orientation applied to
an unrelated population. This distinction matters in the energy estimate.
K1935's acyclic substochastic representation gives `D^-1>=0`. Thus, with
`w^T=1^T D^-1`,

    1=w^T Dp <= sum_i w_i u_i.                               (3)

Disconnected components use block diagonal D. Actual site energies are kept;
positive fractional offsets only strengthen the estimate below.

## 3. A root-energy deficit in every resolvent column

Reuse K1935's outward-orientation domination: the column reward w_i is no
larger than the fully outward rooted reward

    1 + sum_left_prefixes product q_d + sum_right_prefixes product p_d,
    (q1,q2,q3)=(7/11,2/3,1/2),
    (p1,p2,p3)=(7/29,1/9,1/23).

The factor here is 1, because D is twice K1935's M. Put
`q=2/3`, `W=1+2+1/8=25/8`, and `c=163/440`.
If the root has N left edges, the gap constraint implies their total length
is at least `2N-1` for N>=1. Every occupied energy is at least 1, so its
actual energy e satisfies e>=2N. Since every q_d<=q,

    left reward <= sum_(j=1)^N q^j = 2(1-q^N)
                <= 2(1-q^(e/2)).                            (4)

For a right arm beginning with gap 2 or 3, K1935's Bellman bounds give
right reward <=1/8. Missing right arms obey the same bound. Hence (4)
leaves at least `2q^(e/2)` below W.
If the right arm begins with gap 1, a present left arm must begin with gap
3. The separate Bellman bounds are `F3=3/2` and `G1=14/55`, giving

    W-[1+F3+G1]=17/8-3/2-14/55=163/440=c.

A missing left arm leaves more slack. Since q^(e/2)<=1 and c<2, all cases
give the uniform column bound

    0<w_i <= W-c q^(e_i/2).                                 (5)

This uses the analytic outward-domination and Bellman proof already owned
by K1935; finite orientation checks below are independent supporting controls,
not a replacement for that proof.

## 4. Jensen turns the column deficit into a mean-energy theorem

Equations (3) and (5) first imply `m>=1/W`. Exponential convexity and (2)
then imply

    sum u_i q^(e_i/2)
      >= m q^[(sum e_i u_i)/(2m)]
      >= m q^(E/(2m)).

For E>=0, the function `m exp[-E log(1/q)/(2m)]` is increasing on m>0:
its derivative is the positive exponential times `1+E log(1/q)/(2m)`.
Consequently

    1 <= Wm-c m q^(E/(2m)) <= Wm-(c/W)q^(WE/2).

Divide by 2W and use m=2R(p) to obtain (1), since
`c/(2W^2)=652/34375` and `W/2=25/16`. Every physical implementation has
return at least R(p); pinching extends the bound to coherent initial states.
Taking the infimum preserves this fixed-E positive gap. No dimension or
minimum spacing between DIFFERENT resonance components is assumed.

## 5. Physical upper family and the resource consequence

Use K1934's rooted gap-2 construction, with n edges on either side of the
root. On occupied energies `s_i=1+2i`, i=0,...,2n, give the root weight 1
before normalization, left weights `q^(n-i)`, and right weights `p^(i-n)`,
where p=1/9. Use the complete physical ladder 0,...,4n+4. Then

    Z_n=W-2q^n-(1/8)p^n,
    R_n=1/(2Z_n),
    0<R_n-4/25 <= (17/50)q^n,
    E_n <= 2n+1+2 sum_(k>=1) k p^k = 2n+41/32.               (6)

For the return inequality, use Z_n>=1 and p<=q. For the mean-energy bound,
subtract the nonnegative left-arm displacement from root energy 2n+1,
discard it, and use 1/Z_n<=1 on the right arm. These are conservative
inequalities, not asymptotic equalities. K1943's shell construction proves
full complex channel attainment for each preparation; it is not merely an
optimized population map. Zero-weight unused physical levels are included.

Let E_min(delta) be the infimum of feasible mean energies with return at
most `4/25+delta`. For 0<delta<652/34375, (1) gives

    E_min(delta) >= [16/(25 log(3/2))] log[(652/34375)/delta]. (7)

Choose `n=ceil(log[(17/50)/delta]/log(3/2))` in (6). This is an actual
finite nondegenerate protocol and gives

    E_min(delta) <= 2 ceil(log[(17/50)/delta]/log(3/2))+41/32. (8)

Thus `E_min(delta)=Theta(log(1/delta))`. The different constants in (7)
and (8) leave a genuine sharp-exponent problem. This prices initial catalyst
mean energy only, not preparation work, physical bandwidth, control complexity,
joint product return, or repeated reuse. Changing bath temperature, allowing
degenerate spectra, approximate channels or initial correlations changes the
problem. No infinite-dimensional unitary or exchange of physical limits is used.

The same family gives a more precise construction asymptotic. Put
`S_r(n)=sum_(k=1)^n k r^k`. Directly from its normalized probabilities,

    E_n=1+2n+2[S_p(n)-S_q(n)]/Z_n,
    E_n-2n -> -11/4,
    (R_n-4/25)/q^n -> 64/625.

Here `S_r(n)->r/(1-r)^2`; the constants follow from the displayed exact
formula, not a numerical fit. This describes the explicit sequence only.
It does not prove its exponent or constant optimal over arbitrary spectra.

## 6. Verification, scope and next test

The producer checks rational bath ratios, root rewards on every orientation
through five sites, population-consistent positive parts, sixteen exact
rooted families and full complex shell consumers for n=0,1,2,3. The separate
probe derives its recurrence from bath labels and audits longer paths.
Mathematical faults are checked after green baselines. Report identity and
input digests are separate consistency evidence. Universal statements are
the analytic proof above; internal review is not external expert acceptance
or proof-assistant certification.

Mean-energy limitations in thermal catalysis are established context:
[Ng et al., Limits to catalysis in quantum thermodynamics](https://arxiv.org/abs/1405.3039).
The primary abstract was rechecked; no literature-completeness or novelty
claim is made. The contribution here is the specified fixed-channel bound
above its already positive floor, and the matched logarithmic order.

Next compare a sharp energy-weighted Bellman dual against the explicit
rooted-family energy asymptotics. More finite-window secants cannot establish
the sharp global exponent. K1954's rejected secant remains rejected; all
previous proved low-energy segments survive. SC-META-53 remains UNCERTAIN;
LT-SM8, LT-GR6b and AC-F1 remain NEEDS. No source, ledger or canon verdict moves.
