---
title: "K1907: Four-mode dephasing distance and phase compatibility"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied finite quantum dynamics; no GU identification or optimal full-channel distance claim
scripts:
  - tests/channel-swings/k1907_four_mode_dephasing_distance.py
  - tests/channel-swings/k1907_four_mode_dephasing_distance_probe.py
---

# K1907: Four-mode dephasing distance and phase compatibility

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
result: negative-type distance bounds, phase cycles and integrated Lindblad realization
carrier: four-dimensional positive logical density matrices and Schur channels LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product and state expectation ON=conditional_target
real_structure: complex conjugation and CAR star; no native K/C identification
grading: finite occupation sectors and even fermion parity
action_owner: repository-construction -- supplied finite interactions or quantum channels
target: conditional coherence, causal implementation and memory demands MAP-TYPE=intertwiner
```

## Result and exact scope

For K1903's correlation matrix C, put a=1/sqrt(2). Among endpoints of
finite-integrated-rate, time-local diagonal GKSL evolution, the maximum
complex entry error satisfies

    e4 <= inf_D max_jk |D_jk-C_jk| <= 1/4,
    e4(a+e4)=(a-e4)^4,                 13/100<e4<14/100.       (1)

The upper bound is exactly 1/4. The earlier valid construction below gives
about 0.25117; the logarithmic-time construction improves it. The lower bound improves K1906's
three-mode bound. It is exactly sharp for the separate problem of matching
entry MODULI; it cannot be attained while also matching the required complex
phases at error e4. No exact optimum or numerical positive gap above e4 for
the complex-channel problem is claimed. The lower bound also holds in the
entrywise closure of regular endpoints. General singular continuous paths
are covered by K1906's exact endpoint obstruction, not by an unstated
extension of the quantitative generator assumptions here.

## Four-point inequality, with a constructive converse for moduli

Use the Schrödinger convention

    G_jk=<l_k,l_j>-(||l_j||²+||l_k||²)/2-i(h_j-h_k),
    D_jk=exp G_jk,
    Gamma_jk=-log|D_jk|=||l_j-l_k||²/2.                      (2)

Here l_j are vectors in the integrated Lindblad Hilbert space; time-dependent
coefficients are included by an L2 time coordinate. A diagonal Hamiltonian
only changes gauge phases. The parallelogram identity gives

    Gamma12+Gamma34 <= Gamma13+Gamma14+Gamma23+Gamma24.        (3)

Indeed the right minus left is ||l1+l2-l3-l4||²/2. If complex
entry error is at most e<a and a+e<1, then

    |D12|<=e, |D34|<=a+e, |D13|,|D14|,|D23|,|D24|>=a-e.

Exponentiating(3) proves e(a+e)>=(a-e)^4. The difference has
strictly positive derivative a+2e+4(a-e)^3 on [0,a], hence one root.
Exact substitution at13/100 and14/100 brackets it. Errors outside the
stated range already exceed the root.

For the modulus-only converse choose two real, orthogonal Lindblad
coordinates and four coefficient vectors

    l1=(-x,0), l2=(x,0), l3=(0,y), l4=(0,-y),
    x²=-log(e4)/2, y²=-log(a+e4)/2.

Their endpoint has D12=e4, D34=a+e4 and all four cross entries
(a-e4). Its modulus error is e4 exactly. This is an actual real diagonal
GKSL semigroup and a Gaussian phase-noise model; no independent pairwise
rate choices are made. For the three-mode restriction, K1906's smaller
root e3=(a-e3)^4 IS the exact complex optimum: choose l=(-x,x,0),
x²=-log(e3)/2, obtaining D12=e3 and D13=D23=a-e3.

## Why the full phase pattern cannot saturate the modulus optimum

At error e4, every inequality used in (3) must be an equality. Therefore
l1+l2=l3+l4. Translating their common midpoint to zero changes only a
Hamiltonian gauge, so write l1=-u,l2=u,l3=v,l4=-v. The forced moduli
fix ||u||²=-log(e4)/2 and ||v||²=-log(a+e4)/2. Equality in the complex
error triangle also fixes the phase of every nonzero target entry.
In particular D13 and D14 are positive, while arg D34=pi/4. The
Hamiltonian-invariant triangular phase of D13 D34 D41 is thus pi/4.
For this parallelogram its generator phase has absolute value at most

    2||u||||v||=sqrt(log(1/e4) log(1/(a+e4))) < pi/4.         (4)

To verify the strict comparison without a decimal solver, e4>13/100
and a>7/10 imply the two logarithms are less than21/10 and1/5;
their product is below 21/50<9/16 and pi>3. The logarithmic bounds follow
from exp(7/10)>2 and exp(1/5)>100/83 by their positive Taylor terms.
No phase branch helps: any real angle congruent to pi/4 modulo 2pi has
absolute value at least pi/4. The Cauchy-Schwarz bound holds also for
many noise coordinates and time-dependent coefficients. Thus saturation
fails for the complex channel, despite exact modulus attainability.
We do not replace this proof by an uncertified optimizer or claim a sharp
complex distance from nonattainment alone.

## Explicit phase-matching upper construction

Set s=sqrt(pi)/2, use one complex diagonal Lindblad operator with entries

    l=s(-1,1,0,-i),        h=(0,0,0,pi/4),        T=1.        (5)

Direct substitution into (2) gives

    D12=exp(-pi/2),
    D13=D23=exp(-pi/8),
    D14=exp(-pi/4), D24=i exp(-pi/4),
    D34=exp(i pi/4) exp(-pi/8).

The maximum entry error is a-exp(-pi/4), at14 and24. The other errors
are exp(-pi/2) and a-exp(-pi/8), both smaller. Positive elementary
bounds on pi and exp verify these comparisons; the probe also evaluates them
with directed-interval arithmetic. This is an admissible channel with one
Lindblad operator and an explicit Hamiltonian, not just a positive candidate
correlation matrix. It preserves all populations and reaches its endpoint
in finite time. K1908 separately tests whether such generators have
classical noise representations; that question is not CP divisibility.

## Same-day strengthening: exact quarter-error attainment

Retain the lower bound and its phase nonattainment. Use unscaled
l=(-1,1,0,-i), h=(0,0,0,1), and T=log2. The same generator yields

    D12=1/4, D13=D23=a, D14=1/2,
    D24=exp(2i log2)/2, D34=a exp(i log2).                   (6)

Every other entry error is strictly less than 1/4, so the maximum is exactly
1/4. Here is a non-numerical phase check. The positive artanh series gives
56/81<log2<25/36; with 3<pi<22/7, delta=pi/2-2log2 lies in(0,1/5).
Thus sin(2log2)=cos(delta)>49/50>11sqrt(2)/16, and

    |D24-i a|²=3/4-a sin(2log2)<1/16.

Also |D34-a exp(i pi/4)|<=a delta/2<a/10<1/4,
and |D14-a|=a-1/2<1/4. The series lower bound keeps its first two
terms; for the upper bound replace every denominator2n+1 for n>=1 by3,
then sum the geometric tail. This proves an exact admissible quarter-error
upper bound without solving the global complex-distance minimization.
The previous pi/4 construction remains valid historical evidence, not a
withdrawn result. The new construction releases no claim that 1/4 is optimal.

## Released operational consumer

For any two channels in this fixed basis, input (|j>+|k>)/sqrt(2) produces
an output difference with trace norm |D_jk-C_jk|. Thus their diamond-norm
distance is at least their maximum entry error, and(1) is also a lower
bound on diamond norm. With equal prior channel probabilities, the optimized
single-use success probability is at least1/2+e4/4. The best pair depends
on the alternative D; this is not one fixed measurement attaining the bound
uniformly. No upper bound on diamond norm follows by simply copying the
entrywise upper bound. All preparations/readouts here are supplied logical
operations; no native GU accessibility claim follows.

## Review and scientific ceiling

The strongest contrary control is the Gaussian modulus optimizer: it proves
that a magnitude-only argument cannot settle complex attainability. The
phase proof uses integrated complex coefficients and gauge-invariant cycles;
it does not assume real Lindblad data. The upper construction supplies its
actual generator; a PSD matrix alone would not establish divisibility.
Analytic identities carry the general claims. Exact matrix controls and a
separate interval/proof probe check coefficients, root signs, phases and
faults; finite samples never certify an optimum.

SC-OP-04 ASSERTS candidate four-field grammar; SC-MAS-01 and SC-CHI-02
ASSERT a stylized local scalar-curvature toy; SC-META-53 is UNCERTAIN.
These do not identify the imported positive Hilbert carrier, K/C forms or
accessible observations. LT-SM8, LT-GR6b, AC-F1, source/physics-ledger and
canon verdicts are unchanged. The native full20 injection remains a distinct
construction. This is conditional quantum mathematics, with no novelty,
external review, formal proof, GU prediction or GU falsification claim.
