---
title: "K1851: parity makes the Fisher optimizer shape bound useful"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: explicit total-variation bounds from the existing dual gap; no new spectral gap or GU physics
---

# The true optimizer is within total variation 0.093 at the existing precision

Every even probability density with second moment1, fourth moment2 and
Fisher information at most `U=1.752673` is within total variation
`sqrt(27/3125)<0.093` of the actual unique optimizer. The same class lies
within `sqrt(27/12500)<0.047` of K1845's explicit rational-score reference.
The reference need not have the prescribed moments. Folding even densities
onto the half-line improves the Stein bound enough to reach the named
`TV<0.1` target without estimating the unknown optimizer's spectrum.

This is a fixed certificate-precision guarantee. It is **not** a new lower
bound on the true spectral gap, and it does not vanish as `I(p)->F(2)` with
the existing dual certificate held fixed. K1849's separate vanishing-modulus
theorem remains valid, with its stated conservative constant. Explicit moment
error tolerances and a measured-asymmetry extension are given below. The
optimizer is also proved unique in the unrestricted raw-even-moment class.
No restricted-family gap, endpoint asymptotics, GU physics or novelty is claimed.

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
result: useful true-optimizer total variation certificate, moment-error tolerance and asymmetry extension
carrier: real probability densities p=u² with u in H1(R) and finite fourth moment LAYER=toy CHIRALITY=N/A
pairing: L2(dx) square-root energy and half-line probability Stein identity ON=real_Sobolev_functions
real_structure: real nonnegative densities and positive reference density
grading: reflection parity only; no physical chirality
action_owner: repository-construction -- scalar Fisher functional and fixed raw-even-moment constraints
target: total variation to the actual unrestricted moment optimizer MAP-TYPE=evaluation
```

## 1. Reuse the certificate and change the consuming argument

[K1843](k1843-unrestricted-fisher-variational-gap-2026-10-20.md) supplies
the positive even optimizer `p*` and its actual quartic ground-state
characterization. [K1845](k1845-fisher-certified-moment-bounds-2026-10-20.md)
supplies, with exact rational coefficients,

```
N(y)=-26379/25000+(12003/10000)y+(137193/500000)y²,
D(y)=1+(266879/500000)y+(43447/2000000)y²,
g(x)=x N(x²)/D(x²), V(x)=integral_0^x g(t)dt,
pi(x)=exp(-V(x))/Z,
(A,B,C)=(-84469/40000,9487187/1000000,-1406001/500000),
L=A+B+2C=875729/500000, U=1752673/1000000,
delta=U-L=243/200000.
```

For any normalized finite-Fisher density with finite fourth moment,

```
I(p)=J_g(p)+A+B E_p X²+C E_p X4+E_p R(X),
J_g(p)=integral_R (2u'+g u)², p=u², R(x)>0.                 (1)
```

The full-line positivity of the rational remainder `R=P(x²)/D(x²)²`,
the exactly feasible upper trial and the weak square-completion identity
are reused by dependency hashes. They are not recertified by a finite grid.
[K1847](k1847-fisher-density-stability-2026-10-20.md) establishes that pi
is a well-defined positive even density and proves the full-line Stein method.
Its bound `91/24` discarded useful parity. The present target class is even,
so its folding has a genuine boundary at zero and a cheaper lower-tail bound.

Object searches found the K1847 full-line argument but no prior half-line
Stein certificate in this chain. The method is a direct specialization of
that standard density-Stein argument, not a claimed new general inequality.

## 2. Three exact polynomial inequalities

Since D has positive coefficients, it is positive for y>=0. On0<=y<=1,

```
N-D/2=-38879/25000+(933421/1000000)y+(1054097/4000000)y².
```

The nonconstant coefficients are positive and the value at1 is
`-1432859/4000000<0`. Therefore `g(x)<=x/2` for0<=x<=1.
Also N is increasing on y>=0 and `N(1)=209763/500000>0`, so
`g(x)>=0` for x>=1. Finally, translating `N-D` by y=z+9/4 gives

```
N(z+9/4)-D(z+9/4)=23157229/32000000
             +(7214093/4000000)z+(20213/80000)z².
```

All coefficients are positive: `g(x)>=x` for x>=R0=3/2. This last
fact also replays K1847's tail input with exact arithmetic.

## 3. A half-line Stein factor below 4/3

Let rho=2pi on[0,infinity), with CDF F_rho. For the indicator h of any
measurable subset of that half-line, define

```
f_h(x)=rho(x)^-1 integral_0^x (h-E_rho h)rho,
f_h'-g f_h=h-E_rho h, f_h(0)=0.                            (2)
```

The same conditional-probability subtraction as in K1847 gives

```
|f_h(x)|<=F_rho(x)(1-F_rho(x))/rho(x)
        <=min(F_rho(x),1-F_rho(x))/rho(x).                  (3)
```

This holds for arbitrary measurable events, not just CDF intervals.
For0<=x<=1 use the lower-tail ratio and the first polynomial inequality:

```
F_rho(x)/rho(x)=integral_0^x exp(V(x)-V(y))dy
 <=x exp(x²/4)<=exp(1/4)<4/3.                              (4)
```

Indeed `V(x)-V(y)<=integral_y^x t/2 dt=(x²-y²)/4`.
The exponential bound follows from
`sum_n (1/4)^n/n! < sum_n (1/4)^n=4/3`; the strict inequality already
occurs at n=2. For1<=x<=R0, V is nondecreasing and

```
(1-F_rho(x))/rho(x)
 <= R0-x + exp(V(x)-V(R0))/R0 <= 1/2+2/3=7/6.             (5)
```

For x>=R0, the quadratic-tail comparison gives the ratio at most
`1/x<=2/3`. In deriving(5), the tail at R0 is bounded by1/R0 using
`V(y)-V(R0)>=(y²-R0²)/2>=R0(y-R0)`. Equations(3)--(5)
give a uniform bound `||f_h||_infinity<4/3`.

For an even p=u², its folded density is q=2p on[0,infinity).
Integration of(2) against q yields

```
E_q h-E_rho h=-integral_0^infinity f_h(2v'+g v)v,
v=sqrt(q)=sqrt(2)u.
```

The zero endpoint contributes nothing because f_h(0)=0. At infinity use
compact cutoffs: bounded f_h, `q'=2vv' in L1`, and finite second moment
justify the limit exactly as in K1847. This avoids dividing by p at zeros.
The half-line integral of `(2v'+g v)²` equals J_g(p), since u is even and
g is odd. Cauchy--Schwarz and integral q=1 then prove

```
TV(p,pi)=TV(q,rho)<= (4/3)sqrt(J_g(p)).                    (6)
```

The equality of total variations follows directly by splitting the L1
integral at zero for two even densities. It does not hold for an arbitrary
nonsymmetric density and its folding; that case is treated in section5.

## 4. Reach the declared shape target and tolerate moment errors

For exact moments, (1) and strictly positive R give
`J_g(p)<I(p)-L`. Thus I(p)<=U implies

```
TV(p,pi)<(4/3)sqrt(delta)=sqrt(27/12500)<0.047,
TV(p,p*)<(8/3)sqrt(delta)=sqrt(27/3125)<0.093<0.1.          (7)
```

The second inequality uses the triangle inequality and the same bound
for p*, whose existence and I(p*)<U come from the pinned predecessors.
One may display the rational bounds `TV(p,pi)<7/150` and
`TV(p,p*)<7/75`, since `delta<(7/200)²`.
The factor4/3 applies to the actual half-line reference, not to an assumed
optimizer Hamiltonian. In particular(7) does not prove a spectral gap above
0.1215; that was one sufficient method for the TV consumer, not a necessary
condition for any proof of it.

More generally, for even p put e2=E_p X²-1 and e4=E_p X4-2. Define

```
r(p)=I(p)-L-B e2-C e4=J_g(p)+E_p R>0.
TV(p,p*)<=(4/3)(sqrt(r(p))+sqrt(delta)).                   (8)
```

If I(p)<=U+eta, eta>=0, a directly checkable sufficient condition for
TV(p,p*)<0.1 is

```
eta+(9487187/1000000)|e2|+(1406001/500000)|e4|
 <=77/200000.                                             (9)
```

Indeed r(p)<=delta+77/200000=1/625 and
`(4/3)(1/25+7/200)=1/10`, with strictness from
sqrt(delta)<7/200. Normalization is assumed exactly; an unnormalized input
must first be normalized, including recomputation of its moments and Fisher
information. No normalization error is hidden inside(9).

For fixed L,U, the bound in(8) has a nonzero floor as I(p)->F(2): it is
not the vanishing-modulus bound from K1849. Neither pi's exact moments nor
pi=p* are asserted. For bounded observables h the expectation discrepancy
is at most `2||h||_infinity TV`; unbounded observables require their own
tail bounds. The error tolerances in(9) are assumptions, not consequences
of small total variation.

## 5. Released successor: nonsymmetric laws and unrestricted uniqueness

For any normalized p=u² with finite Fisher and fourth moment, define
`p_s(x)=(p(x)+p(-x))/2` and the measurable asymmetry defect

```
alpha(p)=TV(p,p_s)=(1/4)integral_R |p(x)-p(-x)|dx.
```

Fisher convexity gives I(p_s)<=I(p), reflection preserves Fisher, and
p_s preserves both raw even moments. Therefore

```
TV(p,p*) <= alpha(p)+(4/3)(sqrt(r(p))+sqrt(delta)).         (10)
```

Here r(p) uses the original p's Fisher and raw moments, so it upper-bounds
the symmetrized residual. In the exact-moment I<=U class,
`TV(p,p*)<alpha(p)+sqrt(27/3125)`. The easy rational condition
`alpha(p)<=1/150` suffices for TV<0.1 because
`1/150+7/75=1/10`. An empirical or numerical estimate of alpha needs its
own error certificate before this conclusion is used. No odd-sector gap
or unproved asymmetry decay is imported.

For nonsymmetric p, E X² is a **raw** second moment, not necessarily its
variance. The theorem applies without a mean constraint to the raw-moment
class; a centered variance-one subclass is included. Changing the constraint
to variance alone without fixing the mean would define another problem.

The same ground-state certificate also closes the unrestricted uniqueness
question. Symmetrization shows that allowing nonsymmetric densities with
the same two raw moments cannot lower F(2). K1843's positive even u* is the
ground state of the full-line confining quartic
`H=-4d²+a x²+b x4`, b>0, with simple bottom eigenvalue E0.
For any feasible u=sqrt(p), even or not, its moments give

```
I(p)-F(2)=<u,(H-E0)u> >=0.
```

If equality holds, the nonnegative closed form has zero value, so u lies
in the ground eigenspace. Simplicity and nonnegative normalization force
u=u*, hence p=p*. This uses positivity/simplicity of the actual full-line
ground state, already established in K1843; it does not use K1849's even
gap as a bound for an odd excitation. The argument works for every fixed
raw fourth moment1<k<3 by the same K1843 operator.

## 6. Reproduction and specialist review

```
sage -python tests/channel-swings/k1851_fisher_parity_stability.py
python3 tests/channel-swings/k1851_fisher_parity_stability_probe.py
```

The producer checks exact polynomial inequalities, the exponential majorant,
threshold and moment-error arithmetic, square-completion signs, symmetrization
identities and dependency hashes. The independent standard-library probe
rederives the inequalities with Fraction arithmetic, tests conditional-event
covariance and Fisher-convexity controls, and corrupts mathematical inputs
only after a clean baseline. Reporting flags are checked separately.
Finite controls do not prove the half-line integration theorem or full-line
spectral simplicity; the written proof and pinned predecessor own those steps.

Preflight functional-analysis and numerical lenses ranked the actual TV
consumer ahead of a spectrum calculation. The parity specialist identified
the unused boundary at zero; the skeptical lens demanded all-measurable-set
control rather than a CDF estimate. Postflight review checks the endpoint
term, square-root factors, raw-versus-centered moments, asymmetry defect,
strict residual, moment-error signs and the fixed-gap limitation. A separate
mathematical author supplied the initial proof to the integrating reviewer;
no proof-assistant or external verification is claimed. Further improvement
in this constant alone is not the next scientific endpoint. A vanishing
modulus with a practically useful rate, a quantified restricted-family gain,
or unrestricted endpoint behavior remains a different question.
