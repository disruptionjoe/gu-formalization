---
title: "K1829: an explicit Fisher face-instability interval"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: sufficient high-q instability intervals, direction ordering, boundary second variation and explicit finite descent; no true transition or minimizing displacement
---

# A certified parameter range where the Rademacher face loses

In K1825's symmetric unit-variance two-radius Gaussian-channel family,
the Rademacher face c=0 is not locally minimizing whenever

```
2(4095/4096)^2 <= q < 2.                                (1)
```

The lower endpoint is approximately 1.9990235567092896. It is a **sufficient
bound**, not the actual transition parameter. At z=3/4 the inward derivative
satisfies J_c(q,0,z)<=-7t/(72v^2), where t=sqrt(q/2), v=1-t.
Consequently K1825's attained minimum has c>0 throughout (1).

A released follow-through gives a whole set of improving directions. For
v<=1/16384, every z in [3/4,15/16] has a negative inward derivative;
the derivative at z=15/16 is strictly smaller than the one at z=3/4.
This orders infinitesimal directions, not finite steps or global shapes.
The actual second c derivative at z=3/4 also has an explicit positive,
exponentially growing lower bound throughout (1).
A separate uniform estimate below supplies an explicit finite improving c.
No minimizing displacement, exclusion of z=1,
all-q shape uniqueness, GU physical interpretation or canon promotion follows.

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
result: effective parameter interval for boundary instability and exact direction comparison
carrier: real symmetric unit-variance two-radius Gaussian mixtures LAYER=toy CHIRALITY=N/A
pairing: ordinary and Gaussian-relative Fisher integrals against Lebesgue measure ON=real_observation_line
real_structure: real scalar densities, parameters and Gaussian score
grading: moment order and first shape variation; no physical grading
action_owner: repository-construction -- moment-constrained scalar functional, not a source action
target: sufficient parameter bound and one-sided derivative ordering MAP-TYPE=evaluation
```

## 1. Reuse the actual chart and qualitative theorem

[K1827](k1827-endpoint-fisher-asymptotic-2026-10-20.md) proves qualitative
high-q instability and sharp leading growth. Its uncomputed overlap constant
prevented an explicit interval. Here the overlap is bounded quantitatively;
no old optimizer bank is rerun. Use

```
p=c/(c+z^2), a=1-z, b=1+c/z,
X in {+/-sqrt(a),+/-sqrt(b)} with weights p/2,(1-p)/2,
t(c)=sqrt(q/(2-c)), v(c)=1-t(c), Y=sqrt(t(c))X+sqrt(v(c))Z.
```

At c=0 set r=sqrt(1-z), m=sqrt(t), and write phi_v(y-mu) for a Gaussian
density. The positive-lobe density derivative (the full density is its
half-sum with its reflection) is

```
h=A[phi_v(y-mr)-phi_v(y-m)]
   +b0 m partial_m phi_v(y-m) - (t/4) partial_v phi_v(y-m),
A=(1-r^2)^-2,     b0=1/8+1/[2(1-r^2)].                  (2)
```

The derivative exists at each fixed q<2: noise remains positive locally,
the new inner mean lies between the outer means, and Gaussian polynomial
domination justifies the one-sided derivative as in K1827. The second
moment is exactly preserved, so J=I-1 and their shape derivatives coincide.
Equation (2) independently has zero second-moment derivative.

Let T_y=tanh(my/v). For the baseline score and Fisher variation,

```
s=(-y+m T_y)/v, G=-2s'-s^2,
Gplus=2/v-(y-m)^2/v^2,
G-Gplus=(T_y-1)[2my+m^2(T_y+1)]/v^2.                    (3)
```

G is even, so the two half-weights sum to integral G h. Exact Gaussian
moments, including the variance derivative, give

```
integral Gplus h = -kappa(r)t/v^2,
kappa(r)=1/(1+r)^2-1/4.                                (4)
```

The mean derivative contributes zero. For r=1/2, kappa=7/36; for r=1/4,
kappa=39/100. Equation (4) alone is not a whole-mixture sign certificate.

## 2. An explicit overlap estimate

Suppose 0<v<=1/2 and 1/4<=r<=1/2. Then m<=1, m^2>=1/2,
A<=16/9 and b0<=19/24. Split the line at y=mr/2.
On the upper part, 1-T_y<=2 exp(-2my/v), so (3) is bounded by

```
4(|y|+1)v^-2 exp(-m^2 r/v).
```

On the lower part use the global bound 4(|y|+1)v^-2. Each Gaussian mean
mu in {mr,m} is at least distance mr/2 from the split. If u=y-mu there,

```
phi_v(u)<=sqrt(2) exp(-m^2 r^2/(16v)) phi_(2v)(u).       (5)
```

This follows by allocating half of u^2/(2v) to the distance. The derivatives
in (2) obey |partial_mu phi_v|=|u|phi_v/v and
|partial_v phi_v|<=(u^2+v)phi_v/(2v^2).
For either original or doubled variance and |mu|<=1, v<=1/2,

```
E(|Y|+1)<=3,
E[(|Y|+1)|u|]<=3,
E[(|Y|+1)(u^2+v)]<=7.                                 (6)
```

Indeed E u^2<=1, E|u|<=1 and E|u|^3<=sqrt(3)<2, while
|Y|+1<=2+|u|. These inequalities also cover the unexpanded upper region.
Both exponentials above are at most exp(-r^2/(32v)). Adding the upper
and lower estimates and using 1+sqrt(2)<3 yields

```
|integral (G-Gplus)h|
 <= 12 v^-2 exp(-r^2/(32v))
       [6A +3b0/v +7/(8v^2)]
 <= 168 v^-4 exp(-r^2/(32v)).                           (7)
```

The coefficient before rounding is
12[6(16/9)+3(19/24)+7/8]=167. No hidden constant, sampled quadrature,
fixed unproved separation limit or numerical floating sign is used.
For the single direction r=1/2 the exponent in (7) is 1/(128v).
Uniformly on the whole r interval it is at least 1/(512v).

## 3. Certify the whole interval by rational arithmetic

For alpha>0, v^-2 exp(-alpha/v) increases with v when v<alpha/2.
At (alpha,v0)=(1/128,1/4096) or (1/512,1/16384), alpha/v0=32.
The elementary exponential series gives the exact rational upper bound

```
exp(-32) < 32!/32^32.
168 v0^-2 (32!/32^32) < 7/144                           (8)
```

for both pairs. The larger left side is less than 0.008120, whereas
7/144 exceeds 0.04861. These decimals are illustrations; the checks compare
fractions exactly. Since kappa(r)>=7/36 and t>=1/2, (7)-(8) imply

```
J_c <= -kappa(r)t/(2v^2)<0.                            (9)
```

For r=1/2, v<=1/4096 is exactly (1), giving the first headline bound.
For all r in [1/4,1/2], v<=1/16384 gives (9) uniformly. At each fixed q,
a negative derivative supplies some feasible c in (0,2-q) with lower value.
This existence is not a certified common step size.

For direction ordering, kappa(1/4)-kappa(1/2)=44/225.
Twice the uniform scaled error in (8) is less than half that gap.
Since t>=1/2, subtraction of the two derivative estimates proves

```
J_c(q,0,15/16) < J_c(q,0,3/4)       when v<=1/16384.      (10)
```

The constants have deliberately conservative slack. Neither (1) nor the
uniform interval locates the actual onset of instability, and (10) does not
identify a globally best direction.

## 4. Controlled second variation at the boundary

The released next calculation is the actual second c derivative at z=3/4,
not a Hessian of an affine-mixture substitute. It satisfies, for 0<v<=1/4096,

```
J_cc(q,0,3/4) >= exp(1/(8v))/(1024 v^(3/2))-1706/v^6 > 0. (11)
```

This estimate itself is pointwise. Section 5 separately bounds the second
derivative on a positive c interval to construct a finite descent witness. It shows why an ordinary size step based only on the
negative first derivative can be misleading near the endpoint.

Write rho for the symmetric outer Gaussian mixture, tau for the inner one
at means +/-m/2, h=rho_c and k=rho_cc at c=0. Gaussian domination for each
fixed v justifies differentiating twice; products of the inner densities
divided by the baseline still have integrable Gaussian tails. Direct
variation of I=integral rho'^2/rho gives

```
I_cc=2 integral (h'-s h)^2/rho + integral G k.            (12)
h=A(tau-rho)+b0 m rho_m-(t/4)rho_v.
```

Here primes denote y derivatives, while m/v subscripts differentiate the
Gaussian-mixture parameters. Let x=A(tau'-s tau) and
w=[b0 m rho_m-(t/4)rho_v]'-s[b0 m rho_m-(t/4)rho_v].
The -A rho term cancels in h'-s h. Using
2(x+w)^2>=x^2-2w^2 and the exact baseline log-density derivatives,

```
|w/rho| <= 2(1+|y|)/v^3,
integral w^2/rho <=16/v^6.                              (13)
```

For clarity those derivatives are

```
partial_y partial_m log(rho)=T_y/v+my sech^2(my/v)/v^2,
partial_y partial_v log(rho)
 =y/v^2-m T_y/v^2-m^2 y sech^2(my/v)/v^3.
```

The norm uses E_rho Y^2=t+v=1.
On y=vu/m with 1<=u<=2,

```
|tau'/tau-s|=(m/v)[tanh(u)-(1/2)tanh(u/2)] >= m/(4v),
tau^2/rho=(2pi v)^(-1/2) exp(-y^2/(2v)+t/(4v))
           cosh^2(u/2)/cosh(u)
          >= (1/96) v^(-1/2) exp(t/(4v)).               (14)
```

The elementary bounds are tanh(1)>3/4, cosh(2)<4,
exp(-2)>1/8 and sqrt(2pi)<3. Since y^2/(2v)<=4v<=2
and dy=(v/m)du>=v du, (14) gives

```
integral (tau'-s tau)^2/rho >= v^(-3/2)exp(t/(4v))/3072.
```

A^2=(16/9)^2>3, so the quadratic term in (12) is at least
exp(t/(4v))/(1024 v^(3/2))-32/v^6.

It remains to control k from the **nonlinear chart**. At c=0,

```
p'=16/9, p''=-512/81, v'=-t/4, v''=-3t/16,
mu_outer'=19m/24, mu_outer''=-115m/576,
mu_inner'=m/16.
```

In particular |p''|<7, 2p'<4 and every displayed mean/noise derivative
has magnitude at most one. In
k=p''(tau-rho)+2p'(tau_c-rho_c)+rho_cc_parameters,
the last term includes the outer second mean/noise derivatives and all
three quadratic parameter-derivative terms. For any |mu|<=1, v<=1/2,
Gaussian absolute derivative norms weighted by (1+y^2) are bounded by

| density derivative | norm upper bound |
| --- | --- |
| phi | 5 |
| partial_mu phi | 7/v |
| partial_v phi | 7/v^2 |
| partial_mu_mu phi | 14/v^2 |
| partial_mu_v phi | 21/v^3 |
| partial_v_v phi | 27/v^4 |

These follow from 1+y^2<=3+2(y-mu)^2 and Gaussian even moments
E U^2<=1, E U^4<=3, E U^6<=15, with Cauchy--Schwarz for the odd
absolute moments. Thus integral (1+y^2)|k|<=279/v^4.
The actual G satisfies |G|<=6(1+y^2)/v^2, giving
|integral G k|<=1674/v^6. Combining this with (13)-(14) and t>=1/2
proves the lower estimate in (11).

Its strict positivity holds over the entire interval: exp(1/(8v)) is
at least (1/(8v))^32/32!, and at v=1/4096,

```
512^32/32! > 1706*1024*4096^5.
```

For smaller v the power advantage increases; v^-5>=v^(-9/2) for v<=1.
The last inequality is checked with integers. No decimal comparison supplies
the sign. This also gives an exponentially growing lower bound on the
boundary curvature, not a full asymptotic equivalent.

A positive boundary second derivative does not locate a stationary point:
it need not remain controlled over the step needed to cancel the first
derivative. A finite improving step requires additional estimates on an actual c
interval, supplied next. An interior minimum and its scale remain open.

## 5. A fully explicit finite descent step

The boundary curvature result does not by itself give a step. A separate
uniform estimate on a genuine interval now does. Fix q in (1), set v=1-sqrt(q/2),
and define

```
M(v)=2*10^12 v^-6 exp(32/v),    a(v)=7/(144v^2),
c_step=a(v)/M(v)=7v^4 exp(-32/v)/(288*10^12).             (15)
```

Then 0<c_step<=v/4<2-q, and at z=3/4,

```
J(q,c_step,3/4) <= J(q,0,3/4)-a(v)^2/[2M(v)] < J(q,0,3/4). (16)
```

This is a conservative constructive witness, not the scale of the minimizing
displacement. Its very small size reflects the coarse density-ratio estimate.
It is a mathematical bound; ordinary floating-point evaluation will underflow
near this endpoint and is not its reproduction method.

Here is the additional uniform proof. For 0<=c<=v/4, the actual noise
w=v(c) lies in [v/2,v], all four component means have absolute value at most
2, their first/second derivatives are bounded by 4 and 16, |w'|,|w''|<=1,
and the outer positive Gaussian has weight at least 1/4. To verify these:
c<=1/8, t(c)<1, t'<=1/3 gives w>=11v/12; differentiate
log(mu_outer)=log(t)/2+log(1+c/z)/2 and log(mu_inner)=log(t)/2+log(1-z)/2.
Also |weight'|<=1 and |weight''|<=4 follow directly from p=c/(c+z^2).

Let R=|y|+2 and S_phi be the sum of the four unweighted component densities.
Gaussian derivative formulas, with w>=v/2, give the pointwise bounds

```
|h| <=6(R+1)^2 v^-2 S_phi,
|h'|<=8(R+1)^3 v^-3 S_phi,
|h'-s h|<=20(R+1)^3 v^-3 S_phi,
|k|<=100(R+1)^4 v^-4 S_phi,
|G|<=72(1+y^2)v^-2.                                    (17)
```

For reproducibility, the polynomial before the bound on h' is
4R^3+16R^2+14R+16, bounded by 8(R+1)^3 for R>=2.
The polynomial before the k bound is
4R^4+32R^3+94R^2+144R+86, bounded coefficientwise by 100(R+1)^4.
These include weight, mean, variance and mixed parameter derivatives,
not merely an affine change of weights.

Choose phi_0 to be the outer positive component. rho>=phi_0/4 and
S_phi^2<=4 sum_i phi_i^2. For equal variance w,

```
phi_w(y-mu)^2/phi_w(y-mu0)
 =exp((mu-mu0)^2/w) phi_w(y-(2mu-mu0)).                  (18)
```

The exponential is at most exp(32/v), and the new mean has absolute value
at most 6. Gaussian even moments and (a+b)^6<=32(a^6+b^6) bound the sixth
weighted moment by 32(9^6+15)<2*10^7. Equations (12),(17),(18) therefore
bound its quadratic term by 1.024*10^12 v^-6 exp(32/v).
For integral Gk, the original component means have absolute value at most
2, so their corresponding sixth weighted moment is at most
32(5^6+15)<10^6. This term is at most 2.88*10^10 v^-6 in absolute value.
Their sum is below M(v). Hence |J_cc(q,c,3/4)|<=M(v) on the entire interval.
Gaussian domination also justifies the second differentiation there.

Since J_c(q,0,3/4)<=-a(v), Taylor's theorem with this upper bound gives
(16). The exact polynomial and moment inequalities are checked independently;
no minuscule floating-point number is substituted for the positive exponential.
This closes finite descent construction. It does not locate the stationary
point, the true transition, a near-optimal step, or a minimizing-shape limit.

## 6. Reproduction, contrary controls and remaining problem

```
python3 tests/channel-swings/k1829_effective_fisher_face_instability.py
python3 tests/channel-swings/k1829_effective_fisher_face_instability_probe.py
```

The producer pins K1825/K1827 and gives exact interval witnesses. The probe
independently computes Gaussian first variations, preserved moments and the
score subtraction, checks the tail exponent allocation and exact margins,
and separately rejects reporting mutations. These finite controls support
the analytic uniform proof; they do not independently integrate the
parameter family or rerun the inherited attainment theorem.

**Preflight.** Quantifying the overlap was the smallest missing input for an
explicit useful result, while minimizing displacement requires second
variation. Information, Gaussian-tail and moment lenses selected estimates
on the actual score rather than another unvalidated grid. The interval of
other directions and its ordering were admitted follow-through.

**Postflight.** The main overclaim is a true transition or a minimizing displacement. The family f_M(c)=-c+M c^2 has derivative -1 at zero, yet f_M(2/M)>0;
a negative first derivative alone cannot supply that step. The finite
step in (15) instead uses the separate uniform bound (17)-(18). The weakest seam
is the actual mixture overlap, explicitly bounded in (5)-(8), not the
single-lobe calculation. No source/ledger or canonical claim changes, and no
novelty or external acceptance is asserted. A separate-agent review was not
performed; the alternative exact controls and the direct proof obligations
are reported at their actual scope.

The next scalar problem is a sharp rescaled subleading shape functional
or a near-optimal displacement bound. The finite witness in (15) is
conservative and does not claim that exponential scale for the minimizer. It must handle
rare-inner-atom and merging-lobe scales; reducing the conservative threshold
again would not answer that problem. Effective local uniqueness near q0
retains its separate exterior-gap and uniform parameter-Hessian obligations.
