---
title: "K2454 Two setting families for fully local coherent verification"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "conditional four-register verifier with an exact gap; no native GU identification or measured operation cost"
---

# K2454 Two setting families for fully local coherent verification

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
result: K2454
carrier: the original ten-string purified flagged qubit programs on F tensor R tensor B tensor E LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product and operator norm ON=declared_carrier
real_structure: complex Fourier phases with the original real positive amplitudes
grading: coherent three-dimensional flag, two qubits and nine-dimensional environment
action_owner: repository-construction -- supplied conditional mathematical model
target: fully local verifier construction and spectral certificate MAP-TYPE=evaluation
```

## Result

The original coherent programs admit two setting families using only local
measurements on F, R, B and E, with classical feedforward. The certified gap is
exactly

    nu=(1-sqrt((1-w)/(2-w)))/2.

It is greater than `(1-1/sqrt(2))/2` for every `0<w<1`, regardless of how small
any of the eight positive bad-string weights becomes. This removes the tree
bottleneck in K2451 and reduces its ten setting families to two. It changes
which local operations are required: the final E measurement now projects onto
an explicitly known vector with up to nine components, rather than onto an
edge's two-symbol subspace. No claim of lower physical gate cost follows.

Two-setting bipartite verification is established [Li et al.](https://arxiv.org/abs/2112.13638); that result alone does not prove locality inside four registers. The explicit construction below proves the property for these programs, with no novelty claim.

This is conditional pure-state verification, specialized to the original
programs. It uses the same positive Hilbert carrier as K2447/K2451, not a
source-derived GU physical state space. SC-META-53 remains UNCERTAIN; source,
physics ledger and canon receive no new verdict. Internal specialist review
is neither external-expert nor proof-assistant certification.

## 1. Two local setting families on the original object

Use the actual native-axis rotation of R and B from K2451. The target is
`Psi=sum_i sqrt(mu_i)|x_i>`, in site order `(F,R,B,E)`:

|i|x_i|
|---|---|
|0|(0,0,0,0)|
|1|(0,1,1,0)|
|2|(1,0,0,1)|
|3|(1,0,1,2)|
|4|(1,1,1,3)|
|5|(1,1,0,4)|
|6|(2,1,0,5)|
|7|(2,1,1,6)|
|8|(2,0,1,7)|
|9|(2,0,0,8)|

Here `mu0=mu1=g=(1-w)/2`; the other weights are the eight original K2447
values, are strictly positive and sum to `w`. This exact original-object
identification is a required probe check.

The first test measures all four registers computationally and accepts exactly
these ten strings. Its effect is the support projection `Q`. This destroys
coherence on test rounds; it is not applied on use rounds.

The second test first measures F in its three-dimensional Fourier basis and R
and B in their X bases. Write the outcome as `a=(k,s,t)`, where `k=0,1,2` and
`s,t=+/-1`, and

    |a> = (sum_f omega^(k f)|f>)/sqrt(3)
          tensor (|0>+s|1>)/sqrt(2)
          tensor (|0>+t|1>)/sqrt(2),  omega=exp(2 pi i/3).

For `h=s*t`, the unnormalized conditional E vector is

    c_a=(sqrt(g)*(1+h)|0>
         +sum_(i=2)^9 sqrt(mu_i)*omega^(-k F_i)*s^R_i*t^B_i|E_i>)/sqrt(12).

Its squared norm is `p_a=(2-w)/12` if `h=+1`, and `p_a=w/12` if `h=-1`.
Both are nonzero. Communicate `a` to the E controller and accept iff E passes
`|e_a><e_a|`, where `e_a=c_a/sqrt(p_a)`. Each operation acts on a single
register. The ordering is essential: the E basis is chosen after the F/R/B
outcomes; reading E computationally first destroys the resource being tested.
No joint FRB projection occurs.

The effect of this second setting is

    T=sum_a |a,e_a><a,e_a|.

The twelve `|a>` are orthonormal and every `e_a` is normalized, so T is a
projection of rank12 on the full108-dimensional carrier. The expansion
`Psi=sum_a sqrt(p_a)|a,e_a>` proves `T Psi=Psi`. Choose Q and T with probability
one half: `Omega=(Q+T)/2`.

## 2. Exact spectral proof, including outside support

Let `u=(|x0>+|x1>)/sqrt(2)` and
`v=sum_(i=2)^9 sqrt(mu_i/w)|x_i>`. These are orthonormal, and
`Psi=sqrt(1-w)u+sqrt(w)v`.

Restricting each `|a,e_a>` to the ten-string support cancels the Fourier and
X phases. Its support vector is

    a_plus/sqrt(12*(2-w)), if h=+1,
    a_minus/sqrt(12*w),    if h=-1,

where `a_plus=2 sqrt(1-w)u+sqrt(w)v` and `a_minus=sqrt(w)v`.
There are six outcomes of each parity. Consequently

    Q T Q = a_plus a_plus*/[2(2-w)] + a_minus a_minus*/[2w].

It vanishes on the eight-dimensional support complement of `span{u,v}`.
On `(u,v)` its matrix is

    [ 2(1-w)/(2-w), sqrt(w(1-w))/(2-w) ]
    [ sqrt(w(1-w))/(2-w), 1/(2-w)     ].

The eigenvectors are Psi with eigenvalue1 and
`z=sqrt(w)u-sqrt(1-w)v` with eigenvalue `r=(1-w)/(2-w)`. Thus Q and T intersect
only at Psi; the one nontrivial principal-angle cosine is `sqrt(r)`.

For completeness, this principal-angle calculation does control states
outside Q. Define `y=(Tz-r z)/sqrt(r(1-r))`. Then `Qy=0`, and on the
orthonormal pair `(z,y)`, Q is `diag(1,0)` while T is
`[[r,sqrt(r(1-r))],[sqrt(r(1-r)),1-r]]`. Omega has eigenvalues
`(1+sqrt(r))/2` and `(1-sqrt(r))/2` there. On all other sectors the two
projections either agree at Psi, vanish, or act on orthogonal ranges, giving
only eigenvalues1, 0 or1/2. Hence the exact full-carrier gap is
`nu=(1-sqrt(r))/2`, with no numerical spectral fit.

Within mixtures of these two fixed tests, equal randomization is optimal.
For `Omega_p=pQ+(1-p)T`, the nontrivial block's largest eigenvalue is
`[1+sqrt(1-4p(1-p)(1-r))]/2`; the other non-target sectors have eigenvalues at
most `max(p,1-p)`, which this block dominates. Maximizing `p(1-p)` therefore
maximizes the gap at `p=1/2`. This is not an optimality claim over all local
verification protocols or all available effects.

For the original two laws, `r=27/127` and `r=15/67`, respectively. No assumption
about independent actual inputs enters this operator inequality. The verified
positive gap may therefore replace nu in K2447/K2450 for arbitrary conditional
resource states, including resources correlated with inaccessible memory.

## 3. Contrary controls and operation boundary

Neither setting alone suffices: Q accepts ten independent vectors and T
accepts twelve. Omitting feedforward, using the wrong conjugate Fourier phase,
or reading E before the conditional coherent test can break completeness.
The probe checks explicit wrong-phase and prior-E-readout controls on both
original targets, not only an abstract two-dimensional surrogate.

A complete flag dephasing or environment dephasing preserves the correct
reduced program but lowers the new acceptance. These are controls on coherent
custody, not evidence that the reduced instrument is wrong. In particular, for
`T` the exact acceptances are

    flag dephasing: [2(1-w)^2+w/2]/(2-w),
    E dephasing:    2(1-w)^2/(2-w)+sum_(i=2)^9 mu_i^2/[w(2-w)].

The full randomized verifier accepts each with `(1+that_value)/2`, strictly
less than one. K2447's no-free-upgrade result still applies. The new protocol
requires coherent F and E custody, trusted X/Fourier measurements, all twelve
conditional E projection settings, and conditional calibration of the complete
effect. A statement of two randomized setting families does not mean two
fixed elementary hardware settings or cheap nine-level control.

## 4. Same consumer and prospective cost

On use, discard E, dephase the program flag, and apply the original declared
consumer; never disclose test outcomes or E data to that consumer. K2450's
conditional leakage/calibration assumptions and K2444's completed-operation
allowance remain unchanged. For a single original qubit slot, `q=1/4`, `C=2`,
and a one-percent output target, the sufficient zero-failure actual-use count
is

    N_U >= ceil(log(1/alpha)/
      [c_delta*(nu*((.01-kappa/q)/C)^2-delta-beta)]),

provided the denominator is positive. The exact probe reports outward-rounded
Arb bounds for both new gaps, the prior K2451 tree bounds and the internally
entangled gap-one-half verifier under the same prospective allowances:
`pi=1/2`, `alpha=.05`, `delta=beta=10^-8`, `kappa=10^-6`. The exact sufficient counts are 644,001 and 658,808 actual uses, compared
with 22,647,684 and 24,184,903 for the respective tree protocols and 346,586
for the internally entangled gap-one-half effect. These are hypothetical
sampling costs, not measurements or a claim that calibrating the new operation
is equally easy. Storage, routing, actual calibration and use records remain
separate inputs.

[Exact probe](../../tests/channel-swings/k2454_two_setting_local_verifier_probe.py),
[report](../../lab/process/k2454-two-setting-local-verifier.json). The written
universal spectral proof, original-object exact checks, and prospective
sample budgets are separate kinds of evidence.
