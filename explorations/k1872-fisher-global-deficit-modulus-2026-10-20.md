---
title: "K1872: A full-line deficit modulus throughout the Fisher moment family"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: explicit conservative full-line gap and fixed-parameter accuracy; no sharp tunneling, entropy or GU claim
---

# Fixed-parameter Fisher accuracy does not require balance

Let 1<k<3, delta=k-1, and let p_k be the actual Fisher minimizer with raw
second moment1 and fourth moment k. For EVERY feasible density p with finite
Fisher information, including non-even densities with nonzero mean, put
D=I(p)-F(k). Then

```
gamma_full(k) > exp(-488/delta),
TV(p,p_k) <= min(1, exp(244/delta) sqrt(D)).                 (1)
```

This gives a bound that vanishes as D tends to zero at any fixed delta.
Its enormous coefficient is intentionally conservative. It is not a useful
moderate-precision spectrum estimate, a sharp tunneling law, or a positive
uniform gap as delta tends to zero. K1868's unbalanced near-minimizers are
compatible with (1). K1870's balanced endpoint estimate remains much stronger
in its joint endpoint regime.

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
result: all-parameter full-line gap, deficit accuracy and moment-error consumers
carrier: real densities on R with raw second moment1 and fourth moment k in (1,3) LAYER=toy CHIRALITY=N/A
pairing: L2(dx), Fisher energy4 integral |u'| squared, and actual ground-state weighted Dirichlet form ON=real_Sobolev_functions
real_structure: nonnegative real square roots; no physics real-form identification
grading: even and odd parity both included
action_owner: repository-construction -- constrained Fisher variational functional
target: actual moment-selected quartic oscillator and probability density MAP-TYPE=evaluation
```

## 1. Reused theorems and the new parameter range

[K1843](k1843-unrestricted-fisher-variational-gap-2026-10-20.md) supplies the
unique positive even optimizer, quartic duality and b>0. [K1849](k1849-fisher-effective-gap-2026-10-20.md)
supplies the elementary ODE and weighted Hardy proof. [K1853](k1853-fisher-practical-gap-2026-10-20.md)
already extends that argument to both parity sectors and gives the far better
k=2 bound gamma>1/47. We reuse that step, not claim to discover it here.
The new result is a single explicit bound on the entire1<k<3 interval,
including the previously untreated two-well endpoint. No earlier result is
withdrawn. This is GU-independent mathematics, with no novelty claim.

The weighted Hardy method is classical (B. Muckenhoupt, *Hardy's inequality
with weights*, Studia Mathematica44 (1972),31-38,
https://doi.org/10.4064/sm-44-1-31-38). The complete argument needed here is
in the two pinned local predecessors; no unavailable literature theorem is
assumed beyond that proof.

## 2. Bound the actual multipliers using feasible trials

Write psi=sqrt(p_k), H=-4d²/dx²+a x²+b x4 and H psi=E psi. Virial and
energy identities give

```
a=F-2bk, E=2F-bk,
4Q(x)=4psi''/psi=b(y²-2ky+k)+F(y-2), y=x².              (2)
```

The equal mixture with means +/-sqrt(1-v) and common variance
v=1-sqrt(1-delta/2) has the exact moments. Convexity of Fisher gives
F<=1/v=2(1+sqrt(1-delta/2))/delta<=4/delta. Cauchy-Schwarz applied to
integral x p'=-1 gives F>=1. This uses raw second moment, not mean zero
of competitors. The true optimizer is even by the inherited theorem.

The true dual support is F(t)>=F(k)-b(t-k). Take t=1+delta/2. The same
mixture construction at t gives F(t)<=8/delta, hence

```
0<b<16/delta²,  1<=F<=4/delta,  0<delta<2.              (3)
```

The strict b bound follows because F>0. No differentiability of F or fitted
Hamiltonian is used. Symmetrization does not increase Fisher and preserves
raw even moments; thus the same F is the all-density minimum. Alternatively,
the ground-state form inequality with exact moments proves I(p)>=F directly.

## 3. One compact and tail certificate for the entire family

Use R=3, L=4, kappa=40/delta. If y>=9, then

```
y²-2ky+k >= y²-6y+3 >=30,
4Q >= y-2 >=7 >4.                                      (4)
```

The first inequality uses k<3 and 1-2y<0. Both polynomials increase for
y>=9. On0<=x<=4, y<=16, the elementary bounds
|y²-2ky+k|<=355 and |y-2|<=14 imply

```
Q <=1420/delta²+14/delta <=1448/delta² < kappa².         (5)
```

These broad bounds deliberately avoid an unknown lower bound on b.
The positive decaying solution obeys psi(z)<=psi(x)exp(-(z-x)) for z>=x>=R
by the maximum principle. On[0,L], positivity and psi'(0)=0 give

```
psi(x)<=psi(0)cosh(kappa x),
psi(x)>=psi(0)sinh(kappa(L-x))/sinh(kappa L).
```

For rho=2psi² on the half-line, normalization and the tail estimate yield
the same Hardy product bound as K1849:

```
sup_x (integral_x^infinity rho)(integral_0^x 1/rho)
 <= B= (21/2)cosh²(3kappa)[sinh(4kappa)/sinh(kappa)]²+1/4.
```

Since kappa>20, the sinh ratio is less than2exp(3kappa), so

```
B<42exp(12kappa)+1/4<43exp(480/delta)<exp(488/delta).     (6)
```

The last comparison uses exp(8/delta)>exp4>43, established by the first
seven positive Taylor terms. No floating-point exponential enters the proof.

## 4. Both parity sectors and the deficit conversion

The pinned weighted-Hardy argument gives
integral_0^infinity(f-f(0))²rho<=4B integral_0^infinity f'²rho.
Apply it also to f(-x), using the SAME trace f(0), and divide the sum by2.
Minimization over constants gives Var_p_k(f)<=4B integral f'²p_k on the
full line. Local traces and approximation are justified by positivity and
smoothness on compact intervals. The ground-state transform has kinetic
factor4, so the full spectral gap is at least1/B. Compact resolvent and the
simple ground state come from b>0; no boundary condition is added.

For normalized u=sqrt(p)>=0 and c=<u,psi>, the exact-moment form excess is
D=<u,(H-E)u>. The gap gives1-c²<=BD. Cauchy-Schwarz applied to
(u-psi)(u+psi) gives TV<=sqrt(1-c²). Thus (1) follows, and

```
||sqrt(p)-sqrt(p_k)||² <=2exp(488/delta)D.               (7)
```

This is a genuine fixed-delta modulus, but says nothing about practical
precision near delta=0. In particular it supplies no polynomial-size even-
sector gap or stronger constrained-coercivity asymptotics.

## 5. Executed consumers: imperfect moments and certified tolerances

For any normalized p with finite fourth moment, set e2=E_p X²-1 and
e4=E_p X4-k. Its form excess is I(p)-F+a e2+b e4>=0. From (3),

```
|a|<=104/delta², b<=16/delta²,
Dbar=I(p)-F+(104|e2|+16|e4|)/delta².
```

Use Dbar instead of D in (1),(7). It is nonnegative by the form identity.
If only a certified lower value L_F<=F is known, replace F by L_F to obtain
a computable larger quantity. The resulting value uncertainty must itself
satisfy the stated precision budget; a positive numerical slack is not erased.
Normalization errors require a separate correction.

For epsilon in(0,1), the sufficient condition
Dbar<=epsilon² exp(-488/delta) guarantees TV<=epsilon. For n independent
copies, Dbar<=epsilon² exp(-488/delta)/n² guarantees joint TV<=epsilon
by the product coupling bound. CDF/event errors are at most epsilon and
bounded |g|<=M expectation errors at most2M epsilon. At delta=1/8,
a one-percent single-copy guarantee follows from Dbar<=10^-4 exp(-3904).
This is an exact symbolic tolerance, NOT a claim that a certificate with
that precision has been computed or that ordinary machine precision suffices.
Use K1853 at k=2 and K1867 near k=3 whenever they give stronger bounds.

There is weighted square-root Sobolev control as well. Set w=u-psi,
a_-=max(-a,0), C=a_-²/(2b)<=2bk²<288/delta². Since E<=8/delta,
E+C<=304/delta², completing the square in the potential gives

```
4||w'||²+(b/2)||x²w||²
 <=[1+(608/delta²)exp(488/delta)]Dbar.                  (8)
```

This controls the actual coefficient-weighted fourth-moment norm. It does
not assert a uniform positive lower bound on b or high-moment control.
Finally the reversible ground-state diffusion generator
L=4d²+8(psi'/psi)d has L2(p_k) spectral relaxation: its semigroup contracts
mean-zero functions by exp(-t/B). For an initial probability law with finite
chi-square distance, chi²_t<=exp(-2t/B)chi²_0 and TV_t<=sqrt(chi²_t)/2.
This is the ordinary ground-state semigroup consequence on its closed
Dirichlet-form domain, not a GU dynamical law or an entropy estimate.

## 6. Boundary tests, verification and remaining question

K1868 constructs imbalanced competitors and an exponentially SMALL upper
bound for the gap as delta->0. Our lower bound also collapses exponentially;
there is no contradiction. Fixed delta with D->0 and joint delta->0 with
D merely small are different limits. No reverse entropy, log-Sobolev constant,
sharp exponent, native physics or external acceptance follows.

The producer checks17 symbolic/algebraic conditions and4 dependency pins.
The separate Fraction probe checks82 mathematical controls,4pins and7scope
conditions, with10 mathematical-input and7reporting faults rejected by
assertions after a clean baseline. Finite controls certify the displayed
algebra; the ODE, Hardy, domain, spectral and measure proofs above own the
continuum conclusion. No proof assistant or external reviewer is claimed.

Hostile review checked dual-support sign, b versus F inequalities, tail
positivity without a lower b bound, the shared trace at0, raw moments, all
parities, the kinetic factor4, squared Hellinger normalization, form errors,
value-certificate slack and the difference between effective and practical.
Next: a polynomial-scale even/mean-constrained bound or a specified practical
error target requires new localization/coercivity information. Merely asking
again whether any fixed-delta modulus exists is now answered.
