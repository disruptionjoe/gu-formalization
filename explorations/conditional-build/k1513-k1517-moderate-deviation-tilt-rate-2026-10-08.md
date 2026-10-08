---
title: "K1513--K1517 moderate-deviation tilt rate"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1513--K1517 moderate-deviation tilt rate

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests the positive
Hamiltonian prerequisite bordering SC-META-53. The Gaussian cutoff field,
moderate-deviation theorem, exponential tilts and nonlinear Hamiltonians are
repository controls, not released GU data.

```gu-typed-objects
result: fourth-chaos relative moderate deviations, truncated exponential tilt transfer, weighted Malliavin cost, nearly one-fourteenth-power Wick variational rate and strengthened scalar-recentering obstruction
carrier: beta=1 Gaussian reduced Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing ON=repository_owned_control
real_structure: Gaussian real field and coordinatewise complex conjugation
grading: spatial frequency, Wiener chaos, contraction modulus, moderate-deviation radius, Malliavin derivative, particle number and cutoff filtration
action_owner: repository-construction -- no released source measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1508--K1512 use the absolute total-variation error to transfer a compact bump.
That method necessarily stops when the Gaussian bump mass is comparable to the
error, producing the `sqrt(log N)` boundary. K1498 contains more structure than
total variation uses: a quantitative maximum contraction norm for a fixed
fourth chaos. Schulte and Thäle's cumulant theorem converts precisely that
modulus into a *relative* Gaussian tail estimate on a polynomial moderate-
deviation window.

The probability lens therefore replaces the compact rare bump by a truncated
Gaussian likelihood-ratio tilt. The Gaussian-analysis lens transfers its norm
and negative mean from relative tails without asserting density convergence.
The form lens pays for the resulting unbounded weight by a near-one Hölder
exponent and vector-valued third-chaos hypercontractivity. The asymptotic lens
stays strictly inside the theorem's endpoint. The hostile lens preserves the
one-sided ceiling: the theorem constructs better upper trials, not a lower
bound for every many-chaos state or an optimal ground-energy scale. K1413 and
the source-owned selector tuple remain independent routes with inputs not
produced here.

## K1513 — the contractions give a polynomial relative-tail window

Write as before

```text
X_N=I_4(g_N),                 E(X_N^2)=1.
```

Schulte and Thäle, *Cumulants on Wiener chaos: moderate deviations and the
fourth moment theorem*, JFA 270 (2016), Theorem 5(i),
[`doi:10.1016/j.jfa.2016.01.002`](https://doi.org/10.1016/j.jfa.2016.01.002),
normalize the kernel rather than the random variable. Put

```text
h_N=sqrt(4!) g_N,             ||h_N||=1,
F_N=I_4(h_N)=sqrt(4!)X_N,     Var(F_N)=4!.
```

Their contraction parameter is

```text
K_N=max_(1<=r<=3)||h_N tensor_r h_N||.
```

K1498 gives

```text
K_N=O(N^(-3/2)(1+log N)^4).
```

For even chaos order four, the theorem's graph exponent is

```text
alpha(4)=(4+2)/(3*4+2)=3/7.
```

Consequently its deviation parameter obeys

```text
Delta_N=(4^6 K_N^(3/7))^(-1)
       =Omega(N^(9/14)(1+log N)^(-12/7)).
```

After rescaling `F_N` back to unit variance, Theorem 5(i) gives constants
depending only on the chaos order such that

```text
|log(P(X_N<=-z)/Phi(-z))|
 <=C(1+z^3)/Delta_N^(1/3)
```

uniformly for `0<=z<=c Delta_N^(1/3)`. Therefore every radius satisfying

```text
R_N=o(Delta_N^(1/9))
```

has relative logarithmic error `o(1)` uniformly through `2R_N`. In particular,

```text
R_N=N^(1/14)/(1+log N)
```

is admissible because

```text
Delta_N^(1/9)
 =Omega(N^(1/14)(1+log N)^(-4/21)).
```

Every fixed power `N^beta`, `beta<1/14`, also lies inside the window. The
strict inequality and logarithmic retreat are load-bearing. This argument does
not prove a density ratio, a local limit theorem or endpoint optimality.

## K1514 — transfer a truncated exponential tilt

Fix a smooth cutoff `chi` with

```text
0<=chi<=1,       chi=1 on [-3/2,-1/2],
supp(chi) subset [-2,0].
```

Define

```text
u_N(x)=exp(-R_N x/2-R_N^2/4) chi(x/R_N).
```

Without the cutoff, `u_N(Z)^2` is the likelihood ratio of `N(-R_N,1)`
relative to `N(0,1)`. Its Gaussian norm is one, its tilted mean is `-R_N`,
and the plateau contains probability `1-o(1)` under the tilted law.

No density estimate is required for transfer. With `y=-x`, integration by
parts writes a truncated exponential moment on `0<=y<=2R_N` as endpoint terms
plus an integral of

```text
exp(R_N y) P(X_N<=-y).
```

K1513 controls the tail factor multiplicatively and uniformly on the whole
interval. The endpoint outside the plateau is exponentially negligible under
the tilted Gaussian law. The same estimate on the central bands
`|(y/R_N)-1|>=epsilon` shows concentration at `y/R_N=1`. Thus

```text
E[u_N(X_N)^2]=1+o(1),

E[X_N u_N(X_N)^2]/E[u_N(X_N)^2]
 =-(1+o(1))R_N.
```

The weighted Hölder input also transfers. For

```text
p_N=1+R_N^(-2),
```

the full Gaussian exponential calculation gives

```text
(E|u_N(Z)|^(2p_N))^(1/p_N)
 <=exp((p_N-1)R_N^2/2)=sqrt(e),
```

up to the harmless cutoff. K1513 transfers the same `O(1)` bound. This remains
a truncated statement; no full Laplace transform of the fourth chaos is being
identified with the Gaussian one.

## K1515 — the weighted Malliavin cost remains polynomial

The chain rule gives

```text
D u_N(X_N)=u_N'(X_N)D X_N,
u_N'=-(R_N/2)u_N
     +R_N^(-1)exp(-R_N x/2-R_N^2/4)chi'(x/R_N).
```

The cutoff derivative is supported where the tilted coordinate is at least
`R_N/2` from its center. K1513's same relative-tail estimate makes its
normalized weighted contribution exponentially negligible; no false
pointwise comparison `|chi'|<=C chi` is used. Let

```text
q_N=p_N/(p_N-1)=R_N^2+1,
Y_N=||D X_N||^2.
```

The Malliavin derivative is Hilbert-valued third chaos and
`E||D X_N||^2=4`. Vector-valued hypercontractivity therefore gives

```text
||Y_N||_(q_N)
 <=4(2q_N-1)^3
 =O(R_N^6).
```

Hölder together with K1514's near-one moment bound yields

```text
E[u_N(X_N)^2 Y_N]/E[u_N(X_N)^2]
 =O(R_N^6).
```

Hence

```text
E||D u_N(X_N)||^2/E[u_N(X_N)^2]
 =O(R_N^8).
```

For `H_0=dGamma(omega)` and `omega_max(N)=O(N)`, the normalized free cost is

```text
q_0[u_N(X_N)]/E[u_N(X_N)^2]
 =O(N R_N^8).
```

Since `sigma_N=Theta(N^(5/2))`, at the selected radius

```text
N R_N^8/(sigma_N R_N)
 =O(N^(-1)(1+log N)^(-7))
 ->0.
```

The `R_N^8` cost is deliberately nonsharp. Its role is to prove that the
weight remains affordable throughout the present relative-tail window.

## K1516 — polynomial variational descent and recentering

The normalized trial in the finite-cutoff form domain gives, for every fixed
`g>0`,

```text
E_N
 <=6gC_N^2
   -(1-o(1))g sigma_N R_N,

R_N=N^(1/14)/(1+log N).
```

This strictly supersedes K1510's square-root-logarithmic rate. Equivalently,
for every fixed `beta<1/14` and every `A>0`,

```text
E_N<=6gC_N^2-A g sigma_N N^beta
```

eventually. This is still only a variational upper bound.

If `H_N-a_N` is uniformly bounded below, then `a_N<=E_N+O(1)`, so necessarily

```text
liminf_N (6gC_N^2-a_N)/(g sigma_N R_N)>=1.
```

Every scalar family whose corresponding limsup is strictly below one has
spectral bottoms tending to minus infinity. The normalized tilt trials lie in
the fixed Gaussian unit ball and therefore have weakly convergent subsequences;
their weak limit may be zero. Mosco weak liminf nevertheless forbids their
form values from tending to minus infinity for a finite semibounded candidate
form. The entire stated window is excluded.

Tensoring the trials with K1471's normalized degree-zero harmonic BRST vacuum
preserves their form values and weak convergence. The same exclusion holds for
the full matter--BRST forms and harmonic compression. No true-ground-energy
recentered limit, recovery sequence, compactness theorem, interacting
continuum BRST charge or changed-representation conclusion follows.

## K1517 — admission replay

The bridge census is now 221 rows: 142 satisfied, ten conditional, 65 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would call `1/14` the true exponent or the displayed
upper bound a ground-energy asymptotic. The exponent is only the interior
radius delivered by the general fixed-chaos cumulant theorem after K1498's
current contraction estimate. A model-specific cumulant argument, a different
trial, or the true many-chaos ground state can change it.

The strongest contrary route remains a coercive many-chaos or small-ball lower
bound. Nothing here prevents `E_N` from lying much farther below the vacuum
level. The weakest transfer seam is the relative-tail-to-weighted-integral
step; it is protected by truncation, uniformity through `2R_N`, positive-tail
integration and a strict retreat from the endpoint. No pointwise density ratio
is used. The weighted Malliavin estimate is also intentionally crude and is
not a localization theorem.

The fixed Gaussian representation remains load-bearing. A singular dressing
or changed measure can alter the compactness and recentering problem. Within
those ceilings the result is decision-grade: it removes the logarithmic rate
as the present boundary and forces any uniformly semibounded scalar recentering
below a nearly `N^(1/14)` polynomial correction.

## Exact next input

For the quantum arc, prove a matching many-chaos kinetic-localization or
small-ball lower boundary for the actual Hamiltonian, or obtain a model-specific
relative-tail/cumulant theorem that safely enlarges the current tilt window.
Only after bracketing `E_N` test ground-energy recentering, compactness and Mosco
recovery on one common nonlinear domain. Independently, advance K1413 through a
genuinely gauge/Maxwell-dependent spacetime, secondary-null or
derivative/nonlocal estimate controlling both leakages. Source admission still
requires one action-owned primitive circle, kinetic normalization, physical
carrier and faithful observed intertwiner.
