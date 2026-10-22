---
title: "K1918: Collective thermal preparation has an entropy threshold"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied conditional models only; no native GU, novelty, work protocol or formal proof
scripts:
  - tests/channel-swings/k1918_collective_thermal_preparation_threshold.py
  - tests/channel-swings/k1918_collective_thermal_preparation_threshold_probe.py
---

# K1918: Collective thermal preparation has an entropy threshold

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
result: exact finite spectral compression, entropy threshold and qutrit exponential regimes
carrier: N-copy finite product Gibbs bath for an extreme rank-k correlation channel LAYER=toy CHIRALITY=N/A
pairing: positive trace pairing and Gibbs relative entropy ON=finite_tensor_product_bath
real_structure: ordinary complex adjoint and positive density operators; no native K/C identification
grading: bath energy shells, not particle chirality
action_owner: repository-construction -- unrestricted collective preparation and endpoint controlled unitary
target: support mass, preparation cost and constructive channel approximation MAP-TYPE=intertwiner
```

## 1. Exact finite problem and the entropy threshold

[K1916](k1916-bath-preparation-resource-limits-2026-10-21.md) proves the exact
N-copy preparation cost is D_N=-log p_N, where p_N is the sum of the largest
s_N=floor((d/k)^N) eigenvalues of tau^(tensor N). Here C is an extreme
correlation matrix of rank k, tau is a faithful d-dimensional Gibbs state,
and d>k>=2. Tensor extremality and arbitrary joint-unitary support realization
are inherited proved hypotheses, not new assumptions about local physics.
Write p=(p1,...,pd), S=-sum p_i log p_i, R=log(d/k). Then

    S<R: p_N ->1, D_N ->0,
    S>R: p_N ->0 exponentially, D_N grows at least linearly,
    S=R: p_N ->1/2, D_N ->log2.                         (1)

The critical assertion assumes nonzero information variance. This holds in
the stated class at S=R: zero variance with faithful p implies uniform p,
whose entropy log d is strictly above R. Logarithms are natural. At finite N,
p_N<1 and exact preparation changes the bath rank. Vanishing TOTAL cost in
the low-entropy regime does not mean zero finite-N cost or a finite-rate
rank-reduction protocol. The minimum free-energy difference is D_N/beta for
beta>0; trace-distance preparation cost is1-p_N. It is not total work.

## 2. Proof by spectral information, before any enumeration

Let X1,...,XN be independent with distribution p, Z_N=sum -log p_X.
The eigenvalues are exp(-Z_N). For any real a_N>0,

    Pr[Z_N<=log s_N-a_N] <= p_N
       <= Pr[Z_N<=log s_N+a_N]+exp(-a_N).               (2)

For the lower bound the threshold set has at most s_N exp(-a_N)<=s_N
words: each word has weight at least exp(a_N)/s_N and total mass is at most1.
For the upper bound, any selected s_N words above the second threshold carry
at most exp(-a_N) total mass. This proves(2) without a coding heuristic.
The law of large numbers proves the off-critical threshold. Because
-log p_X is bounded, a Chernoff bound with a small nonzero exponential tilt
gives exponential tail decay on either side of its mean; choosing a_N linear
but smaller than the entropy gap proves the claimed exponential statements.
At S=R choose a_N=N^(1/4). Since log s_N=NR+o(1), the central limit theorem
with positive variance sends both probabilities in(2) to1/2. Thus(1) includes
the critical constant, not just a rate per copy. No claim is made for d=k:
there s_N=1 and p_N=p_max^N, exactly. Nonfaithful initial states require their
own support accounting rather than silent use of the faithful theorem.

This is spectral fixed-length source compression applied to K1916's bath
resource formula, not a novel coding theorem. Closest context is Masahito
Hayashi, [Exponents of quantum fixed-length pure state source coding](https://arxiv.org/abs/quant-ph/0202002),
Physical Review A66,032321(2002). Its abstract concerns coding exponents;
our elementary spectral inequalities above and shell proof below are given
explicitly, and no theorem from an unread proof is used as a black box.

## 3. Complete qutrit shell formula, including partial degeneracy

Take d=3,k=2,H=diag(0,Delta,Delta), beta Delta=x>=0, and

    q=2exp(-x)/(1+2exp(-x)), R=log(3/2),
    s=floor(3^N/2^N), n_j=binom(N,j)2^j,
    D_m=sum_(j=0)^m n_j.

Let m be the smallest integer with D_m>=s and r=s-D_(m-1), using D_-1=0.
The exact optimal mass is

    p_N=sum_(j<m) binom(N,j) q^j(1-q)^(N-j)
            +r (q/2)^m(1-q)^(N-m).                    (3)

All states in a shell have equal weight; only r of them are retained at the
last shell. Omitting that partial shell changes the exact optimum. For x>0
these shells are in decreasing probability order. At x=0 all weights are
equal and the same formula gives p_N=s/3^N, independent of shell ordering.
The producer uses only integer and Fraction arithmetic for rational q.

Let f(r)=-r log r-(1-r)log(1-r)+r log2. On(0,2/3), f is strictly increasing.
There is one r_* in this interval with f(r_*)=log(3/2). In fact

    1/10<r_*<11/100,
    log(178/11)<x_*:=log[2(1-r_*)/r_*]<log18.           (4)

The rational bounds are certified by exponentiating the endpoint entropy
inequalities into exact integer comparisons, not floating logarithms.
The entropy of tau is f(q), so x>x_* is exactly the vanishing-cost regime.

## 4. Sharp exponential regimes and the critical cost

Elementary type bounds for binomial coefficients give
m=Nr_*+O(log N): on any compact subinterval of(0,2/3), D_m has logarithm
N f(m/N)+O(log N), and D_(m-1)<s<=D_m brackets log s=NR+o(1).
The nonzero derivative f'(r_*) converts the logarithmic error to O(log N).
For J distributed Bin(N,q), (3) implies

    Pr[J<=m-1] <= p_N <= Pr[J<=m].                       (5)

For 0<q<2/3 define binary relative entropy
I(r||q)=r log(r/q)+(1-r)log[(1-r)/(1-q)]. Then

    q<r_*: lim -log(1-p_N)/N=I(r_*||q),
    q>r_*: lim -log(p_N)/N=I(r_*||q),
    q=r_*: p_N->1/2 and D_N->log2.                     (6)

Proof of the exponential rates: a binomial point of empirical frequency r
has probability between exp[-N I(r||q)]/(N+1) and exp[-N I(r||q)].
On a tail beyond q the largest exponential term is at the boundary, and
at most N+1 terms change only the polynomial factor. Apply this to(5) and
its complement, with adjacent boundaries converging to r_*. At the critical
point their separation from the mean is O(log N)=o(sqrt N), so the binomial
CLT gives1/2. At q=2/3 the exact flat formula gives rate log2, agreeing with
I(r_*||2/3)=log3-f(r_*)=log2. The pure limit q=0 gives p_N=1 separately.
For q<r_* also D_N~1-p_N, hence its decay exponent is the same I.
No large-N estimate is used to certify any finite-N numerical claim.

## 5. Released operational consequences and a finite certificate

Use K1916's exact realizing unitaries for the optimally truncated state,
but feed the ORIGINAL product Gibbs bath. Linearity gives a channel

    p_N Phi_(C tensor N)+(1-p_N) Phi_tail,
    half-diamond error <=1-p_N.                         (7)

Therefore unrestricted collective interactions on unchanged faithful baths
approximate the entire N-copy target with exponentially vanishing error
when S<R. This is an upper bound, not the sharp fixed-spectrum channel
optimum. At every finite N exact realization remains impossible by K1912's
faithfulness result. K1913's lower bounds decay with joint minimum eigenvalue;
there is no contradiction with(7). The protocol need not use a separate pure
flag; the endpoint unitary is defined directly on the joint bath support and
extended to the complement. Locality, sequential implementation, uniform
control strength and reset are unpriced and not asserted.

For q=1/21 (exp(beta Delta)=40), use the exact N=300 shell computation in
the report. It certifies 1-p_N<1/10000 by a rational comparison, hence both
full-block half-diamond error<1/10000 and D_N<1/9999 (using
-log(1-e)<=e/(1-e)). Separately preparing300 cells requires
300log(21/20)>300/21, by log(1+t)>=t/(1+t). Thus the collective TOTAL
relative-entropy cost is below1/9999 while the independent cost exceeds14.
These are mathematical resource costs, not a claim of an experimentally
available300-cell machine. The exact bound is checked before acceptance.

## 6. Released finite-copy guarantees and a spectral converse

The threshold has a nonasymptotic consumer for any nonuniform faithful
Gibbs spectrum. Let B=log(p_max/p_min)>0, choose0<delta<R-S, and take

    N >= log2/(R-S-delta).

Since floor(exp(NR))>=exp(NR)/2, every word with
Z_N<=N(S+delta) fits within s_N. Bounded independent information variables
give

    1-p_N <= exp(-2N delta^2/B^2).                       (8)

For completeness, the centered single-variable log moment-generating
function has second derivative equal to a tilted variance, at most B^2/4.
Its value and first derivative at zero vanish, so it is at most t^2 B^2/8.
Multiplication for N variables, Markov's inequality and minimization over
t=4delta/B^2 prove(8). This checks the bounded-variable hypotheses directly.
For a requested0<eta<1 it suffices also to require
N>=B^2 log(1/eta)/(2delta^2). Then whole-block half-diamond error<=eta
and D_N<=eta/(1-eta). This is a conservative finite-copy guarantee;
the qutrit exact certificate is much sharper.

Conversely, for every alpha>1, Holder's inequality on the selected s_N
weights gives the exact finite-N lower bound

    D_N >= (alpha-1)/alpha * [N H_alpha(p)-log s_N],
    H_alpha(p)=log(sum p_i^alpha)/(1-alpha).             (9)

A negative right side can be replaced by zero. This prices a hot spectrum
without a limiting argument. At a flat spectrum, alpha->infinity gives
D_N>=Nlog d-log s_N, with equality in the known flat solution. At alpha=2,
(9) is simply p_N^2<=s_N (sum p_i^2)^N, independently checked on the
same exact rational spectra. These are standard concentration and spectral
norm arguments applied to the resource problem, not new coding theorems.

## 7. Hostile review and reproducibility

The producer evaluates(3) with exact shell counts and probability weights.
A separate probe enumerates and sorts all3^N words for small N, and uses a
separate count recurrence for large N. It checks partial shells, N=1/2,
flat and cold limits, monotonic support, normalization, and the exact finite
certificate. Faults remove degeneracy or shift the final-shell weight; they
must fail real algebraic comparisons after a clean baseline. Provenance/report
checks are separately labeled. Analytic proofs, not these examples, carry(1),(6).

Strongest overclaim: automatic cheap local cooling, a sharp diamond-distance
optimum, or exact faithful finite-bath realization. None is claimed.
Strongest contrary regimes: uniform bath has extensive cost Nlog2+o(1);
d=k has no support compression; q above r_* loses almost all allowed mass.
Weakest seam: shell degeneracy and order of finiteN versus asymptotic limits.
Equation(3) and the finite rational certificate preserve them explicitly.

## Source and acceptance boundary

SC-OP-04 ASSERTS candidate four-field grammar, SC-OP-05 is UNCERTAIN about
its rival, SC-MAS-01/SC-CHI-02 ASSERT a stylized curvature-mass toy, and
SC-META-53 remains UNCERTAIN about indefinite spectra. None supplies the
positive Hilbert model, control, physical units or bath used here. LT-SM8,
LT-GR6b and AC-F1, the source register and canon verdicts stay unchanged.
Native full20 injection, separate K/C, accessible algebra and physical
interaction/domain are separate construction debts. Analytic arguments carry
universal claims. Exact finite probes check identities, constructive examples
and countercontrols, not all continuum hypotheses. No expert acceptance,
formal verification, empirical prediction or novelty is claimed.
