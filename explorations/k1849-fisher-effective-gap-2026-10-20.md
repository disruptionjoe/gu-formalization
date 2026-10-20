---
title: "K1849: an effective spectral gap for the actual Fisher optimizer"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conservative effective even-sector gap and stability; no sharp spectrum, restricted gap or GU physics
---

# True-optimizer stability is effective without fitting its Hamiltonian

For the unique even variance-one, fourth-moment-two Fisher minimizer, the
actual moment-selected quartic oscillator has even-sector spectral gap
`gamma_2 > exp(-36)`. Hence
`TV(p,p*) <= min(1,exp(18)*sqrt(I(p)-F(2)))` on that exact moment class.
The constant is very conservative and becomes nontrivial only at extremely
small excess energy. It is an effective theorem, not a useful-precision
spectrum estimate. A common bound `gamma_k>exp(-400)` also holds for every
`7/4<=k<=17/8`. Exact moment errors can be included explicitly.

The proof derives intervals for the **true** multipliers from dual support
and the virial identity, then bounds its ground state by elementary ODE
comparison and a weighted Hardy inequality. It does not identify K1845's
rational-score reference or fitted dual coefficients with the optimizer.
K1845's value bracket is unchanged. No restricted-family quantitative gap,
unrestricted endpoint expansion, GU physical claim or novelty is asserted.

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
result: effective true-quartic even spectral gap and TV/Hellinger/Sobolev stability with moment errors
carrier: even real normalized square roots u in H1(R) with finite fourth moment LAYER=toy CHIRALITY=N/A
pairing: L2(dx) and positive ground-state weighted Dirichlet form ON=real_Sobolev_functions
real_structure: real nonnegative square roots and positive even ground state
grading: even parity; no physical chirality
action_owner: repository-construction -- constrained scalar Fisher functional
target: actual moment-selected quartic optimizer, not the score-reference density MAP-TYPE=evaluation
```

## 1. Bound the unknown true coefficients before computing a spectrum

Reuse the existence/duality theorem in [K1843](k1843-unrestricted-fisher-variational-gap-2026-10-20.md)
and the exact certificate in [K1845](k1845-fisher-certified-moment-bounds-2026-10-20.md).
Write F=F(2), u*=sqrt(p*), and

```
H=-4 d²/dx²+a x²+b x4,       H u*=E u*, b>0,
a=F-4b,                    E=2F-2b.                        (1)
```

The equalities are the true virial and energy identities, not a fit.
K1845 gives `L=875729/500000<F<U=1752673/1000000`, so
`7/4<F<2`. The true dual support inequality is
`F(t)>=F(k)-b_k(t-k)`. At k=2 and t=3 use the variance-one Gaussian
with energy1, obtaining b>=F-1>3/4. At t=3/2 use the equally weighted
Gaussian mixture with means ±sqrt(1-v) and variance
`v=1-sqrt(3)/2`. It has second moment1, fourth moment3/2 and Fisher
at most `1/v=4+2sqrt(3)<8` by convexity of Fisher. Thus
`F(3/2)>=F+b/2`, whence b<2(8-F)<13. In summary,

```
3/4<b<13,  7/4<F<2,  |a|<52,  |E|<26.                    (2)
```

No differentiability of F is needed: the maximizing dual pair itself supplies
the supporting line. The same inequality applies to the endpoint Gaussian
because it is an admissible trial for the oscillator form. The Gaussian-mixture
bound is an upper bound, not its exact mixture Fisher information.

## 2. A general positive-ground-state estimate

For a normalized positive even ground state psi of `-4d²+V`, define
`Q(x)=(V(x)-E)/4`, so psi''=Q psi. Suppose exact constants R>0, L0>R,
kappa>0 satisfy

```
Q(x)>=1 for x>=R,       Q(x)<=kappa² for 0<=x<=L0.           (3)
```

The following estimates are sufficient; a lower bound on Q inside the
compact interval is unnecessary. Positivity, H1 and the ODE give psi(x)->0
at infinity. On [x,infinity), x>=R, compare with
`psi(x)exp(-(y-x))`: the difference has nonnegative `(d²-1)` applied to it,
is zero at x and tends to zero at infinity. The maximum principle implies

```
psi(y)<=psi(x)exp(-(y-x)), y>=x>=R.                         (4)
```

On [0,L0], variation of constants and psi'(0)=0 give
`psi(x)<=psi(0)cosh(kappa*x)`. For the lower bound compare to
`psi(0)sinh(kappa*(L0-x))/sinh(kappa*L0)`. Its value matches at0 and is0
at L0, while `(-d²+kappa²)psi>=0`; the Dirichlet maximum principle gives

```
psi(x)>=psi(0) sinh(kappa*(L0-x))/sinh(kappa*L0).            (5)
```

Use the half-line probability density rho=2psi². Normalization, the compact
upper bound and(4) imply
`1<=(R+1/2)rho(0)cosh²(kappa R)`. Therefore on[0,R],

```
rho(x)>= [sinh(kappa*(L0-R))/sinh(kappa*L0)]²
          /[(R+1/2)cosh²(kappa R)].
```

Let Qtail(x)=integral_x^infinity rho and H0(x)=integral_0^x 1/rho.
Put

```
B0=R(R+1/2)cosh²(kappa R)
       *[sinh(kappa L0)/sinh(kappa*(L0-R))]²,
B=B0+1/4.                                                 (6)
```

For x<=R, Qtail<=1 and H0<=B0. For x>=R, the part of H0 from[0,R]
contributes at most B0. From(4), `Qtail(x)<=rho(x)/2` and
`integral_R^x 1/rho(s) ds<=1/[2rho(x)]`; their product is at most1/4.
Thus `sup_x Qtail(x)H0(x)<=B`. This proof keeps both compact and tail
parts: decay of psi alone would not control its reciprocal in the bottleneck.

## 3. Weighted inequality and the true even spectral gap

For completeness the required weighted Hardy estimate is proved here.
For a smooth f with f(0)=0, weighted Cauchy-Schwarz yields

```
f(x)² <= 2 sqrt(H0(x)) integral_0^x f'(s)² rho(s)sqrt(H0(s)) ds.
```

Integration by parts using Qtail*H0<=B bounds
`integral_s^infinity rho(x)sqrt(H0(x)) dx <=2B/sqrt(H0(s))`.
Indeed its boundary term is at most B/sqrt(H0(s)), and its remaining
integral is at most `(B/2)integral_s^infinity H0'/H0^(3/2)
=B/sqrt(H0(s))`. The far boundary vanishes since H0->infinity.
Fubini then gives `integral f²rho<=4B integral f'²rho`.
Approximation extends it to the weighted form domain. Applying this to
f-f(0) and minimizing over constants gives the same bound for Var_rho(f).
This is the classical [weighted Hardy inequality of Muckenhoupt](https://doi.org/10.4064/sm-44-1-31-38),
not a new inequality; the new input here is the explicit certificate(3).

The ground-state transform on even functions is
`<psi f,(H-E)psi f>=4 integral_R psi² f'²`.
Even parity is Neumann at0 on the half-line. The variance inequality and
min-max principle therefore imply

```
gamma_even>=1/B.                                           (7)
```

This is the even-sector gap, not automatically a bound for the smaller
full-line odd excitation. Boundary terms are justified first for compact
smooth functions and then by form closure. K1843's confining quartic has the
required positive ground state and compact resolvent; no boundary extension
or approximate reference Hamiltonian has been introduced.

## 4. Execute the k=2 certificate

By(1), setting y=x² gives

```
4Q=b(y²-4y+2)+F(y-2).
```

For x>=R=2, both polynomials are positive and increasing in y>=4;
`4Q> (3/4)*2+(7/4)*2=5`, proving the tail condition(3).
On[0,L0] with L0=17/8, y<=289/64. The quadratic y²-4y+2 has minimum-2
and maximum17729/4096 there; `|y-2|<=161/64`. Hence

```
Q <= [13*(17729/4096)+2*(161/64)]/4
   =251085/16384 <16=kappa²,   kappa=4.
```

Equation(6) now reads

```
B=5 cosh²(8)[sinh(17/2)/sinh(1/2)]²+1/4 < exp(36).          (8)
```

For the simple exponential bound, cosh8<exp8 and
`sinh(17/2)/sinh(1/2)<exp8/(1-exp(-1))<2exp8`, since exp1>2.
Thus B<20exp32+1/4<21exp32<exp36; the last inequality follows from
`exp4>1+4+8+64/6>21`. Combining(7),(8) proves

```
gamma_2>exp(-36).                                          (9)
```

No floating quadrature, eigenvalue discretization, unknown multiplier value
or Gaussian tail ansatz for psi is part of this certificate. The stronger
hyperbolic-function value1/B is also valid. Neither is claimed close to the
actual gap. A useful numerical constant still merits rigorous spectral work
when a concrete consuming tolerance needs it.

## 5. Executed successors: stability and approximate constraints

For even normalized p=u², u>=0 in H1 and finite fourth moment, put
`e2=E_p X²-1`, `e4=E_p X4-2`. The exact form excess is

```
D=<u,(H-E)u>=I(p)-F+a e2+b e4>=0.                          (10)
```

The spectral/TV argument already proved in K1847 now gives

```
TV(p,p*) <= min(1, exp18 sqrt(D)),
||u-u*||² <=2 exp36 D.
```

By(2) one may replace D on the right with the explicit safe upper quantity
`Dbar=I(p)-F+52|e2|+13|e4|`. This remains nonnegative by(10).
If only a certified value bound is available, replace F by L to get a larger
computable upper quantity; that introduces the existing value-certificate gap.
For exact moments, D=I-F and the bound genuinely vanishes with excess energy.
Errors in normalization or evenness require their own correction; they are
not covered by(10). In particular odd perturbations cannot use this even gap.

There is also effective strong square-root Sobolev control. Since
`a_-=max(-a,0)<=4b`, `C=a_-²/(2b)<=8b<104`, and E<4, the pointwise form
bound used in K1847 gives, with w=u-u*,

```
4||w'||²+(3/8)||x²w||² <= (1+216 exp36) D.                 (11)
```

Use Dbar if necessary. This follows from
`4||w'||²+(b/2)||x²w||²<=D+(E+C)||w||²`, b>3/4 and E+C<108.
It is an effective result for the actual optimizer, without asserting a
numerical profile for it. At the current ~0.0012 value uncertainty, the TV
bound from(9) is vacuous; K1847's explicit reference-distance bound remains
much more useful at that precision. Effectiveness and practical sharpness
are separate properties.

## 6. A uniform compact interval, not endpoint asymptotics

The same proof settles a parameter-uniform successor. Let
`7/4<=k<=17/8`. K1845's whole-line affine dual certificate gives

```
F(k)>=-84469/40000+9487187/1000000-(1406001/500000)k
     >=5599831/4000000 >21/16.
```

The trial at3/2 and monotonicity give F(k)<8. Dual support at3 and3/2
then gives `1/4<b_k<28`. The virial relations are now
`a=F-2bk`, `E=2F-bk`, so
`4Q=b(y²-2ky+k)+F(y-2)`.
For x>=R=3, y>=9, the first polynomial is at least
`y²-(17/4)y>=171/4`, increasing there, and the second is positive.
Thus 4Q>171/16>4. On[0,L0] for L0=25/8, y<10,
`|y²-2ky+k|<145` and `|y-2|<8`; hence
`Q<(28*145+8*8)/4=1031<33²`. Choose kappa=33.
Equation(6), exp(2*kappa*(L0-R))=exp(33/4)>2, and
`exp4>sum_(j=0)^6 4^j/j!>43` yield

```
B<42 exp396+1/4<exp400,
gamma_k>exp(-400) uniformly for 7/4<=k<=17/8.               (12)
```

Thus the TV coefficient exp200 is common on this compact interval. It does
not address k->1 or k->3 and is too large for ordinary numerical error bars.
Its payoff is a fully effective uniform theorem without differentiating the
optimizer or solving a parameter family of spectral problems. More endpoint
coefficients do not follow from it.

## 7. Reproduction and hostile review

Run `sage -python tests/channel-swings/k1849_fisher_effective_gap.py`
and `python3 tests/channel-swings/k1849_fisher_effective_gap_probe.py`.
The producer checks rational polynomial certificates, dual/virial identities,
compact/tail bounds, exponential comparison and stability factors. Independent
Fraction controls replay extrema via polynomial translation and vertex tests,
check coefficient sign/factor faults, and use an exactly solvable Gaussian
for the ground-state energy normalization. They do not computationally prove
the continuum ODE/Hardy theorem. The written proof owns that transfer.

Review checked wrong-sign dual slopes, presumed differentiability, bounds on
the wrong Hamiltonian, tail-to-reciprocal transfer, the half-line boundary,
the kinetic factor4, approximate moment terms and impractical constants.
The full-line odd gap remains outside the certificate. No separate-agent,
formal proof-assistant or external verification is claimed. Useful next work
is a much sharper certified actual spectrum for a named error target, a
quantitative restricted k2 improvement, or uniform endpoint analysis. Gap
existence and mere effectiveness are now reusable evidence, not open gates.
