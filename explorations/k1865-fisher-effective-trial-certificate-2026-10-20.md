---
title: "K1865: Effective Fisher density and value certificates from a trial oscillator"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite full-line trial and second density approximation, fifth Fisher value with explicit sixth-order error; no sixth coefficient, generic polynomial-moment transfer or GU physics
---

# An effective density approximation without fitting the optimizer

For the unrestricted Fisher minimum F(3-q), with raw second moment1 and fourth
moment3-q, the following bounds hold for every 0<q<=1/200. Let phi be the
standard Gaussian and Hn the probabilists' Hermite polynomials. Then

```
||p_q - phi[1-q H4/24+q²(7H6/432+H8/1152)]||_1 < 22q³,    (1)
|F(3-q)-1-[q²/6+q³/4+11q4/108+139q5/432]| < 80q6.         (2)
```

An explicitly normalized, dilated squared-polynomial density t_s, whose
moment parameter q(s) is strictly increasing, satisfies

```
TV(t_s,p_(q(s))) < 8s³,       0<s<=1/200.                  (3)
```

At the exact rational parameter s=1/1000, q(s) is approximately
0.001000001286058052 and the sharper rational certificate gives TV below
1/100000000. The decimal is explanatory; the certified q and bound are exact
rational expressions. These are independent scalar mathematics, not GU
physics, novelty or a formal proof-assistant result.

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
result: effective feasible-density approximation, second-response L1 remainder and fifth value with explicit error
carrier: real probability densities on R with raw second moment1 and fourth moment3-q LAYER=toy CHIRALITY=N/A
pairing: Fisher integral 4 integral |(sqrt p)'| squared ON=real_Sobolev_functions
real_structure: real nonnegative densities; signed quasimodes used only in spectral bounds
grading: polynomial Hermite degree only
action_owner: repository-construction -- scalar moment-constrained Fisher functional
target: actual minimizer density and minimum energy MAP-TYPE=evaluation
```

## 1. The finite question and the cheaper structural route

[K1859](k1859-fisher-optimizer-tail-response-2026-10-20.md) supplies a feasible
Hermite trial and its fourth-order value. [K1862](k1862-fisher-second-density-response-2026-10-20.md)
proves the second optimizer profile and a uniform actual spectral gap, but
leaves its asymptotic error ineffective. The initial finite route composed
K1855's global lower bound with that gap. It gives a valid O(s^(3/2)) TV
bound, but discards the trial's near-stationarity.

The stronger route below supplies its own confining oscillator and uses the
trial residual to bound that oscillator's lowest eigenvalue. The variational
dual then bounds the actual constrained minimum. No identification of the
trial Hamiltonian with the unknown optimizer Hamiltonian is made. This
removes the need to estimate unknown multiplier remainders before obtaining
an effective density certificate. The same bound releases (2), including its
fifth coefficient; a formal trial series alone would not justify it.

Use the full-line minimizer and uniqueness from K1843/K1851, plus K1862's
actual full-line gap greater than6/5 on 0<q<=1/100. No generic competitor
higher-moment hypothesis is inserted. Source register, physics ledger and
canon are unchanged. Searches found the trial, second profile and abstract
energy-to-TV conversion already held; the new objects are the effective
whole-interval dual error and its density/value consumers.

## 2. Exact feasible family and monotone moment coordinate

Set

```
u=-H4/48,
v=-1/192-H2/48-H4/64+H6/216+H8/4608,
h_s=1+s u+s²v,
N=E_phi h_s²=1+s³/64+7991s4/331776,
B=E_phi x²h_s²=1+13s³/576+93863s4/331776,
C=E_phi x4h_s²=3-s-173s³/144+604679s4/110592,
D=E_phi (h_s')²=s²/24+s³/16+919s4/6912.
```

Let sigma²=B/N and define

```
r_s(x)=phi(x)h_s(x)²/N,
t_s(y)=sigma r_s(sigma y),
q(s)=3-CN/B²,
J(s)=I(t_s)-1=(B/N)(2-B/N+4D/N)-1.                       (4)
```

The density has total mass1, raw variance1 and raw fourth moment3-q(s).
Zeros or signs of h_s do not invalidate it: |h_s|sqrt(phi) is H1 and its
weak derivative has the same squared energy as the signed square root.
Gaussian integration by parts gives the raw Fisher energy
`I(r_s)=2-B/N+4D/N`, so (4) is exact.

On 0<s<=1/200, exact coefficient certificates prove

```
s<q(s)<2s,   0<q'(s),   0<q(s)-s<2s³,
1/200<q(1/200)<1/100.                                    (5)
```

Thus each 0<q<=1/200 has a unique s(q) in this interval, with s(q)<q.
Monotonic rational bisection can enclose it. The assertions are not sample
estimates: after clearing positive denominators and the explicit vanishing
powers of s, each polynomial P is certified by
`P(0)-sum_(j>=1)|P_j|(1/200)^j>0`. The scripts reconstruct and check these
rational lower bounds. They also prove positivity of N,B,C throughout.

## 3. A supplied oscillator gives a rigorous variational dual

Define the auxiliary full-line self-adjoint oscillator by its closed form,

```
H_s=-4d²/dx²+a_s x²+b_s x4,
a_s=1-2s-11s²/3,  b_s=s/3+3s²/4,
e_s=2-s-19s²/12.
```

Its form domain is H1 intersect L2(x4 dx); a_s>25/36 and b_s>0 on the
interval. Compact resolvent and the min-max comparison with the harmonic
oscillator give its second eigenvalue lambda1>5: the harmonic eigenvalues
are 2sqrt(a_s)(2n+1), and shrinking the form domain cannot lower them.
This oscillator is an explicitly chosen dual certificate, not a fit to p_q.

Use the normalized signed trial z_s=phi^(1/2)h_s/sqrt(N). Put

```
P1=x4/3-2x²+1,   P2=3x4/4-11x²/3+19/12,
r3=P1 v+P2 u,    r4=P2 v,
(H_s-e_s)(phi^(1/2)h_s)=phi^(1/2)[s³r3+s4r4].             (6)
```

Exact Gaussian moments give

```
R2=E_phi(s³r3+s4r4)²
 =18165763s6/124416+167987027s7/248832+202282679s8/147456,
H=E_phi[h_s(s³r3+s4r4)]
 =-s³/2+11s4/108+139s5/432+6174095s6/1990656,
mu=<z_s,H_s z_s>=e_s+H/N<3.                              (7)
```

The squared residual variance at mu is `R2/N-(H/N)²<=R2/N`.
For completeness, the spectral inequality behind the lower bound follows
from `(lambda-lambda0)(lambda-lambda1)>=0` on every spectral value. Taking
expectation in z_s yields
`variance >= (mu-lambda0)(lambda1-mu)`. Since mu<3<5<lambda1,

```
lambda0 >= mu - R2/(2N).                                 (8)
```

The trial lies in the operator domain (polynomial times Gaussian), and mu
below lambda1 proves nonzero ground overlap. No assumed positivity of h_s,
unknown spectral gap, numerical eigenvalue or continuum sampling is used.

Dilating to y with variance1 multiplies the eigenvalues by sigma² and the
potential coefficients by sigma4 and sigma6. For any feasible density p,
its square root has expectation at least this dilated lambda0. The exact
moments remove the potential terms. For t_s the expectation equals
sigma²mu. Consequently

```
0<=I(t_s)-F(3-q(s)) <= E_s := B R2/(2N²).                 (9)
```

This is a genuine lower bound on the constrained optimum from a separately
supplied operator. Equality between its ground state and p_q is unnecessary.
It is also valid when the signed trial has nodes because its kinetic energy
matches that of the nonnegative square root.

## 4. Explicit error, density, CDF and energy-budget consumers

Whole-interval rational bounds give

```
R2<150s6,   B/(2N²)<64/125,
E_s<(384/5)s6.
```

The actual optimizer's K1862 gap exceeds6/5. Its ground-state decomposition
for an exactly feasible density gives
`TV(p,p_q)² <= (5/6)[I(p)-F(3-q)]`. Applying this to (9) proves (3).
At s=1/1000 the exact E_s is approximately7.334236428335693e-17, giving
TV below7.81784093614071e-9 and hence below1e-8. The exact comparison is
`(5/6)E_s < (1/100000000)²`; decimal rounding is not its proof.

For every event, including half-line CDF events, probability error is at
most8s³. For every measurable |f|<=1, expectation error is at most16s³.
For m independent samples the product-law TV is at most min(1,8m s³), by
successive product coupling or the TV telescoping inequality. These are
bounded-observable statements, not high-moment claims.

If another exactly feasible density p has a certified
`I(p)<=I(t_s)+eta`, eta>=0, then (9) yields

```
TV(p,p_q)<=min(1,sqrt((5/6)(E_s+eta))),
TV(p,t_s)<=min(1,sqrt((5/6)(E_s+eta))+sqrt(5E_s/6)).        (10)
```

Thus a target epsilon is certified whenever E_s+eta<=(6/5)epsilon².
This is a usable finite energy budget, not an assertion that a competitor's
unbounded moments are controlled. K1862's rare-tail counterexample survives.

## 5. Executed second-density remainder

Let D2=2v+u²=7H6/432+H8/1152 and P_q=phi(1+2q u+q²D2).
P_q is used as an integrable approximation; no positivity assumption about
this truncated expression is required. On the interval the same rational
controls give

```
0<N-1<s³/50,    0<B/N-1<s³/50,    I(r_s)<2,
E_phi u²<1/16,  E_phi v²<1/16,    E_phi D2²<1.
```

Expanding h_s² and applying Cauchy-Schwarz shows

```
||r_s-P_s||_1 <= |N-1|+2s³ E|uv|+s4 E v² < s³.           (11)
```

For the normalized density r_s, its dilation group's L1 generator satisfies

```
||r_s+x r_s'||_1 <=1+sqrt[(B/N) I(r_s)]<3.
```

This follows from Cauchy-Schwarz using finite Fisher and its raw second
moment, including zeros by weak derivatives. The generator norm is unchanged
under dilation. Integrating along log(sigma), with
`0<log(sigma)<s³/100`, gives `||t_s-r_s||_1<3s³/100`.
Also (5) and the Gaussian L2 bounds imply

```
||P_q(s)-P_s||_1
 <=2|q(s)-s|E|u|+|q(s)²-s²|E|D2| <4s³+6s4.              (12)
```

Finally `||p_q(s)-t_s||_1<16s³`. Sum these four bounds: the coefficient
is at most16+1+3/100+4+6/200<22. Since s(q)<q, this proves (1).
It provides an effective L1 second-response estimate and uniform bounded
observable/CDF errors. It does not provide a polynomial-weight remainder for
generic near minimizers or a coefficient at the next density order.

## 6. Released value successor, with a lower bound rather than just a series

Let `P5(q)=q²/6+q³/4+11q4/108+139q5/432`. Exact substitution in (4),
clearing denominators, proves cancellation of all coefficients below s6 in
`J(s)-P5(q(s))`. The remaining rational expression satisfies

```
|J(s)-P5(q(s))|<3s6,     0<s<=1/200.                     (13)
```

For (13) the scripts bound the absolute coefficient sum of its numerator
at1/200 and divide by a strictly positive coefficient lower bound on the
denominator. The resulting bound is below3 (approximately2.321), over the
whole interval. No numerical grid or formal little-o is used.
Combining (9) and (13),

```
|F(3-q(s))-1-P5(q(s))| < (384/5+3)s6 <80s6 <=80q(s)6.
```

This proves (2), including the fifth coefficient139/432. The fourth-order
value and second profile are reused, not relabeled as new. The sixth value
coefficient is not determined: the current dual defect is of precisely that
order. Resolving it requires a stronger quasimode/dual argument.

## 7. Reproduction and hostile review

```
sage -python tests/channel-swings/k1865_fisher_effective_trial_certificate.py
python3 tests/channel-swings/k1865_fisher_effective_trial_certificate_probe.py
```

The symbolic producer uses Gaussian moments and rational polynomial
elimination. The independent standard-library probe reconstructs Hermites,
moments, residuals and interval numerators with dense Fraction polynomials;
it imports no producer implementation. The producer has54 arithmetic checks and3 dependency checks; the probe
has53 arithmetic,3 dependency and1 reporting check. The probe detects21 mathematical input faults and4 reporting faults, each after
a clean baseline and by a failed assertion. These counts do not prove the
spectral/min-max or dilation arguments; the written proof above owns them.

Inline hostile review checked the auxiliary/actual operator distinction,
second eigenvalue rather than an assumed fitted gap, signed trial nodes,
normalization and dilation factors, spectral-domain inclusion, raw moment
constraints, all-interval rather than sampled signs, the q-to-s inverse,
and nontransfer to unbounded observables. A probe's first extended baseline
used its last sample parameter in the example check; this fixture error was
corrected before any mutation evidence was counted. No independent person,
external expert or proof assistant is claimed.

The useful finite density and value questions are settled at this scope.
The next mathematical extension needs a higher residual, a different moment
window, or a specified weighted-error consumer. The stronger source-facing
comparison remains actual native I1B/observation data, not another freely
chosen scalar comparator. No source claim, physics ledger row or canon moves.
