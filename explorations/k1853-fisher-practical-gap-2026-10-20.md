---
title: "K1853: a practical full-line gap for the true Fisher optimizer"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: full-line gap and vanishing stability at raw second moment 1 and fourth moment 2; no endpoint or GU claim
---

# A useful vanishing error bound, without fitting the optimizer Hamiltonian

The actual moment-selected quartic oscillator has **full-line spectral gap
`gamma > 1/47`**. For every normalized density p with finite Fisher information,
raw second moment1 and fourth moment2, including nonsymmetric densities,

```
TV(p,p*) <= min(1,sqrt(47*(I(p)-F(2)))) < 7 sqrt(I(p)-F(2))
```

when the excess is positive. Equality at zero means p=p*. This is a practical
vanishing modulus: excess at most1/4700 guarantees TV<0.1. It improves
K1849's conservative even-sector exponential constant and removes its parity
restriction. It does not improve K1845's optimum-value interval. At the existing
primal/dual precision it gives TV<0.24 without a symmetry assumption; K1851's
TV<0.093 remains the better fixed-precision bound for even densities.

The key is a **lower bound on the true optimizer density**, obtained from its
small certified score residual relative to a known reference. The tail bound
uses the true quartic equation. The reference is never identified with p*.
No restricted-family quantitative gap, endpoint asymptotic, GU, novelty,
formal-proof or external-expert acceptance claim is made.

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
result: practical full-line spectral gap and vanishing true-optimizer stability
carrier: normalized real square roots in H1(R) with finite fourth moment LAYER=toy CHIRALITY=N/A
pairing: L2(dx), positive reference-weighted Dirichlet form and actual quartic form ON=real_Sobolev_functions
real_structure: real nonnegative densities, positive even optimizer
grading: reflection parity used to construct the bound, not required of the tested density
action_owner: repository-construction -- scalar Fisher energy with raw-even-moment constraints
target: actual constrained Fisher minimizer and its full-line quartic operator MAP-TYPE=evaluation
```

## 1. Reuse exactly the needed inputs

[K1843](k1843-unrestricted-fisher-variational-gap-2026-10-20.md) and
[K1851](k1851-fisher-parity-stability-2026-10-20.md) establish the unique
positive even optimizer p*=psi², also among all densities with these raw moments.
For its **actual** operator, K1849 gives

```
H=-4 d²/dx²+a x²+b x4, H psi=E psi,
a=F-4b, E=2F-2b, 3/4<b<13, 7/4<F<2.
```

[K1845](k1845-fisher-certified-moment-bounds-2026-10-20.md) supplies
`L=875729/500000<F<U=1752673/1000000`, so `delta=U-L=243/200000`.
Use its same odd rational score g=x N(x²)/D(x²), with

```
N(y)=-26379/25000+(12003/10000)y+(137193/500000)y²,
D(y)=1+(266879/500000)y+(43447/2000000)y².
V(x)=integral_0^x g(t)dt, pi=exp(-V)/Z.
```

The inherited whole-line square-completion certificate implies
`J_g(p*)=integral(2psi'+g psi)² < delta`. Its strictly positive residual,
weak-form integration and feasible upper trial are reused by dependency hash,
not proved by the finite calculations here. K1851 supplies g(x)>=x for x>=3/2.
Searches of the recent chain found gap existence, conservative effectiveness,
and fixed-reference TV control, but no such practical full-line certificate.

## 2. Exact compact reference bound

Let r=N/D. The coefficients of N'D-ND' are all positive; D is positive
on y>=0. Thus r is increasing. Set h=1/32 and, for0<=j<=128, form

```
L_j=(h/2) sum_(i=0)^(j-1) r(ih),
U_j=(h/2) sum_(i=1)^j r(ih).
```

Exact rational arithmetic verifies `min L_j>-1/5` and `max U_j<2`.
For any y between jh and(j+1)h, the partial integral of r/2 lies above
`L_j+min(0,h*r(jh)/2)` and below
`U_j+max(0,h*r((j+1)h)/2)`. These are minima/maxima of the corresponding
successive sums. Hence the bounds hold **between nodes**, proving

```
-1/5 < V(x) < 2 for 0<=x<=2.                              (1)
```

For rho=2pi restricted to the positive half-line, its normalizer is
`Zplus=integral_0^infinity exp(-V)`. The inherited tail g>=x gives
`integral_2^infinity exp(-V)<=exp(-V(2))/2`. Consequently

```
Zplus < (5/2) exp(1/5) <25/8,
rho(x)>exp(-2)/(25/8)>1/25,   0<=x<=2.                    (2)
```

Here exp(1/5)<5/4 follows by comparison with a geometric series.
For exp2<8, sum through order5 and majorize the tail starting at order6
by a geometric series of ratio2/7. These are rational certificates, not
floating-point exponential bounds. No reference moment is assumed.

## 3. Transfer to the actual optimizer

Put rho*=2psi² on the half-line and w=sqrt(rho*/rho). Smooth positivity
and the score identity imply

```
4 integral_0^infinity rho (w')² = J_g(p*) < delta.         (3)
```

The true second moment is1, so Markov gives
`integral_0^2 rho* >=3/4`. Since `integral_0^2 rho<=1`, there exists
y in[0,2] with `w(y)>=sqrt(3)/2>6/7`. For any x in[0,2], weighted
Cauchy--Schwarz, (2) and (3) give

```
|w(x)-w(y)|² <= (delta/4) integral_[x,y] 1/rho
             < (delta/4)*50 <1/64.
```

Thus w(x)>41/56 and

```
rho*(x)>m=1681/78400,  0<=x<=2.                          (4)
```

The lower bound is on the **true** optimizer, not merely its L1 distance
from a reference. Total variation alone could not have ruled out a narrow
bottleneck; the weighted derivative estimate is essential.

For x>=2 the actual ODE has psi''=Q psi, where
`4Q=b(x4-4x²+2)+F(x²-2)>5>4`. The positive decaying solution therefore
satisfies `psi(y)<=psi(x)exp(-(y-x))` for y>=x>=2, by the maximum-principle
argument in K1849. This uses the actual multipliers and full-line ground state.

## 4. Weighted Hardy bound and both parity sectors

Define Qtail(x)=integral_x^infinity rho* and H0(x)=integral_0^x1/rho*.
For0<x<=2, (4) and the true second moment give

```
Qtail(x)H0(x) <= min(1,1/x²)*x/m <=1/m.
```

For x>=2, exponential decay gives Qtail(x)<=rho*(x)/2 and
`integral_2^x1/rho*(s)ds<=1/(2rho*(x))`.
The compact contribution is at most H0(2)<=2/m, multiplied by
Qtail(x)<=1/4. Therefore

```
B=sup_x Qtail(x)H0(x) <= max(1/m,1/(2m)+1/4)
                     <=1/m+1/4 <47.                     (5)
```

The elementary weighted-Hardy proof in K1849 gives
`integral (f-f(0))²rho* <=4B integral(f')²rho*` on the half-line.
It is a standard weighted-Hardy inequality; see
[Muckenhoupt, Studia Mathematica44 (1972)](https://doi.org/10.4064/sm-44-1-31-38).
Here the proof and its domain closure are supplied by the pinned predecessor.

Apply it separately to f(x)-f(0) and f(-x)-f(0), then divide their sum by2.
The same f(0) is used on both sides. Minimizing over constants proves
`Var_p*(f)<=4B integral_R(f')²p*` for arbitrary full-line form-domain f.
This is the missing odd-sector step: no even-only gap is silently reused.
The ground-state transform has kinetic factor4, so min-max gives

```
gamma_full >=1/B >1/47.                                  (6)
```

Smooth compact functions are a form core; weighted traces at zero are valid
because the positive smooth density is bounded away from zero locally.
The confining quartic's compact resolvent and simple ground state are inherited.

## 5. Released consequences: useful vanishing stability and imperfect moments

For any normalized p=u² in the form domain with exact raw moments, set
Dtrue=I(p)-F. Its ground-state energy is Dtrue. Spectral decomposition gives
`1-<u,psi>²<=Dtrue/gamma_full`. Cauchy--Schwarz applied to
`(u-psi)(u+psi)` gives TV<=sqrt(1-<u,psi>²). Hence

```
TV(p,p*) <=sqrt(47 Dtrue),
||u-psi||² <=94 Dtrue.                                   (7)
```

The weak non-strict form includes Dtrue=0. For positive excess the certified
strict gap makes the first bound strict. This holds with no mean or evenness
assumption: second moment is raw, not variance unless centered.
Dtrue<=1/4700 gives TV<0.1. If only I<=U is known, Dtrue<delta gives
TV<sqrt(11421/200000)<6/25=0.24. K1851 remains sharper for its even class.
The computable bound with I-L has a certificate floor; the bound with true
excess I-F genuinely vanishes. These are different uses of (7).

For e2=E_p X²-1 and e4=E_p X4-2, the exact form energy is
`D=I(p)-F+a e2+b e4>=0`. Therefore (7) holds with D and with the larger

```
Dbar=I(p)-F+52|e2|+13|e4|.
```

For numerical certification F can be replaced by L. No hidden normalization
or moment error is inferred from TV; normalization remains an assumption.
Using K1849's pointwise quartic form bound, E+C<108 and b>3/4,

```
4||u'-psi'||²+(3/8)||x²(u-psi)||² <=10153 D.               (8)
```

This follows from the inherited inequality with right side
`D+(E+C)||u-psi||²` and (7); it also applies without symmetry.
Thus derivative and weighted-tail convergence now have practical explicit
constants for this fixed moment. No parameter-uniform endpoint conclusion
is drawn from a certificate at k=2.

## 6. Verification and remaining question

Run the two scripts `tests/channel-swings/k1853_fisher_practical_gap.py`
and `tests/channel-swings/k1853_fisher_practical_gap_probe.py` with python3.
The producer uses exact Fraction polynomial and Riemann bounds; the independent
probe implements rational evaluation and monotonicity separately, rechecks a
finer enclosure, the conservative transfer constants and mathematical input
faults. Dependency hashes preserve the earlier rigorous residual/tail premises.
Finite checks certify these premises and arithmetic, not the continuum theorem.
The written weighted derivative, actual ODE, two-half-line Hardy and form
arguments own the analytic transfer. Review is inline, not a separate agent
or proof assistant.

Hostile review specifically tests: a node-only V claim; reference-as-optimizer
substitution; arbitrary holes despite TV closeness; mistaken full-line/even
transfer; missing kinetic4; raw versus centered moments; and a false vanishing
claim after replacing F by L. Each is addressed above. The useful vanishing
fixed-k endpoint is closed. Sharper constants alone do not supply unrestricted
endpoint asymptotics, a restricted same-k quantitative gain, or GU physics.
