---
title: "K1554--K1559 spectral shell gap and gauge normal-form boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1554--K1559 spectral shell gap and gauge normal-form boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests a positive-
Hamiltonian prerequisite bordering SC-META-53 and a conditional PDE control.
The cutoff field, sign geometry, nonlinear Hamiltonian and temporal-gauge
normal form are repository controls, not released GU data.

```gu-typed-objects
result: cutoff-independent fixed-shell defect gap, sharp lamellar control, quartic cutoff ground-energy scale and first gauge-potential normal-form exchange
carrier: beta=1 Gaussian reduced Fock control plus classical Maxwell-matter graph tiers LAYER=toy BRIDGE=positive-state-and-flow-requirements CHIRALITY=N/A
pairing: normalized torus Fourier L2 pairing, Gaussian Q-space pairing and temporal-gauge spatial current pairing ON=repository_owned_control
real_structure: real cutoff trigonometric field for the spectral theorem; compatible complex matter carrier for the Maxwell-current identity
grading: Fourier radius, fixed-ratio shell, quartic defect, Wick-square energy, charge graph tier and spatial derivative order
action_owner: repository-construction -- no released source measure, Hamiltonian, counterterm, gauge choice, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary and K1413 conditional PDE control MAP-TYPE=restriction
```

## Preflight bookend

K1548--K1553 left the `N^(-4/3)` texture bound explicitly nonsharp. Its
coarea proof used phase balance and an `L4` gradient bound but did not use the
fact that the sign shell can be transferred back to the degree-`N` field.
That transfer forces order-`N^2` gradient energy. The new route asks whether a
small quartic defect can carry that energy either inside or outside the
transition set.

The strongest same-object contrary construction is a high-frequency lamella,
not K1550's localized bubble: it retains a fixed shell fraction and therefore
tests the new conclusion under the load-bearing hypothesis. Independently,
K1478 says any successful K1413 correction must depend on gauge/Maxwell fields,
derivatives, nonlocal spacetime structure or a higher hierarchy. The cheapest
gauge-dependent test is the exact product rule for `int A dot j_n` in temporal
gauge.

## K1554 — the fixed-shell defect has a positive gap

Work on normalized `T^3`. Let `f_N` be real with Fourier support
`|k|_2<=N`, set `s_N=sgn(f_N)`, and write

```text
delta_N=int_(T3)(f_N^2-1)^2,
H_(alpha,N)=||P_(alpha,N)s_N||_2^2,
P_(alpha,N)=1_{alpha N<=|k|_2<=N}.
```

Assume `H_(alpha,N)>=eta`. K1548 gives

```text
||f_N-s_N||_2^2<=delta_N.                            (1)
```

If `delta_N<=eta/4`, the projection triangle inequality yields

```text
||P_(alpha,N)f_N||_2
 >=||P_(alpha,N)s_N||_2-||f_N-s_N||_2
 >=sqrt(eta)/2.                                      (2)
```

Plancherel on the shell therefore forces

```text
||grad f_N||_2^2>=alpha^2 eta N^2/4.                 (3)
```

Now split this energy at `B_N={|f_N|<1/2}`. On `B_N`, the defect density is
at least `9/16`, so

```text
mu(B_N)<=16delta_N/9.                                (4)
```

The K1549 identity gives

```text
||f_N||_4^4<=(1+sqrt(delta_N))^2.                    (5)
```

For `delta_N<=1`, `L4` Bernstein and Holder imply

```text
int_(B_N)|grad f_N|^2
 <=mu(B_N)^(1/2)||grad f_N||_4^2
 <=C N^2 sqrt(delta_N).                              (6)
```

On the complement, differentiate the quantity that is small. Put
`g_N=f_N^2-1`, which has degree at most `2N`. Bernstein gives

```text
||grad g_N||_2<=2N||g_N||_2=2N sqrt(delta_N).        (7)
```

Since `|f_N|>=1/2` on `B_N^c`,

```text
|grad g_N|^2=4f_N^2|grad f_N|^2>=|grad f_N|^2,

int_(B_N^c)|grad f_N|^2<=4N^2delta_N.                (8)
```

Combining (3), (6), and (8), then canceling `N^2`, gives

```text
alpha^2 eta/4<=4delta_N+C sqrt(delta_N).             (9)
```

Thus

```text
delta_N>=c_(alpha,eta)>0                             (10)
```

uniformly in `N`. The cases excluded while deriving (2), (5), or (9) already
have a fixed positive defect and are absorbed by decreasing the constant.
This replaces K1549's `N^(-4/3)` lower bound by the sharp cutoff exponent zero.

The mechanism is spectral, not merely geometric: fixed sign-shell mass forces
high-frequency energy in `f_N`, and a small square defect cannot hide that
energy either at or away from the zero set.

## K1555 — a fixed-shell lamella is exponent-sharp

Fix `0<alpha<1`. For large `N`, choose an integer `M_N` with
`alpha N<=M_N<=N` and set

```text
f_N(x)=sin(M_N x_1).                                 (11)
```

This field is degree `N`. Its sign is the square wave
`sgn(sin(M_N x_1))`; the fundamental Fourier pair `plus/minus M_N e_1`
alone carries mass

```text
2(2/pi)^2=8/pi^2.                                    (12)
```

Hence the fixed shell mass is uniformly positive and the two sign phases each
have volume one half. Meanwhile

```text
delta_N=int(sin^2(M_Nx_1)-1)^2
       =int cos^4(M_Nx_1)
       =3/8.                                         (13)
```

Therefore the `N^0` exponent in (10) is optimal under the declared normalized
hypotheses. This does not determine the best dependence on `alpha,eta`, and it
does not construct a low-Fisher likelihood or a ground-state profile.

## K1556 — arbitrary mixtures retain quartic Wick cost

Let `nu_N` be any law on real degree-`N` fields with

```text
E_nu H_(alpha,N)>=eta.
```

Since `0<=H<=1`,

```text
nu_N{H>=eta/2}>=eta/(2-eta)>=eta/2.                  (14)
```

K1554 applies on this event, so

```text
E_nu delta_N>=c'_(alpha,eta)>0.                      (15)
```

After amplitude scaling `h_N=sqrt(3C_N)f_N`,

```text
E_nu W_N=9C_N^2 E_nu delta_N=Omega(N^4),             (16)
```

because `C_N=Theta(N^2)`. K1550 remains an honest boundary: its localized
Fejer bubble has both shell mass and defect of order `N^-3`, not a fixed shell
expectation.

## K1557 — the cutoff ground-energy exponent closes at four

The earlier ground-energy proof used only asymptotically subquartic free cost.
For the endpoint exponent, use K1539 quantitatively. Suppose

```text
q_0[psi]+gE_nu W_N<=epsilon N^4.                     (17)
```

K1539's explicit low-shell Fisher bound supplies `c_0>0` such that choosing
`epsilon<c_0` forces

```text
T_N>C_(sh,N)/2>=kappa C_N/2.                         (18)
```

Let `A_N=sqrt(3C_N)` and
`r_N=E_nu|||phi_N|-A_N||_2^2`. K1538 gives

```text
r_N<=E_nu W_N/(3C_N),
r_N/C_N<=epsilon/(3g c_C^2)                          (19)
```

when `C_N>=c_C N^2`. K1541's projection factorization is quantitative:

```text
E_nu H_N
 >=T_N/(6C_N)-r_N/(3C_N)
 >=kappa/12-epsilon/(9g c_C^2).                     (20)
```

For smaller fixed `epsilon`, (20) is at least `kappa/24`. K1556 then forces
`E_nu W_N>=c_1N^4`, contradicting (17) after one final reduction of
`epsilon`. Approximate minimizers therefore give

```text
E_N>=c_gN^4.                                         (21)
```

The vacuum has `q_0=0` and `E W_N=6C_N^2=O(N^4)`, so

```text
E_N=Theta_g(N^4).                                    (22)
```

Consequently the unshifted resolvent norm is `O_g(N^-4)`, and every scalar
recenter `a_N=o(N^4)` remains coercively divergent. Equation (22) identifies
the exponent only. It does not identify `E_N` to bounded error, produce a
common limiting nonlinear domain, or prove compactness, Mosco recovery,
interacting BRST closure, or source ownership.

## K1558 — the first gauge-potential normal-form exchange

K1413 gives, for the lifted graph-tier energy,

```text
(F_n^PDE)'
 =int E dot j_n
  +(lambda/2)int partial_t||phi||^2||Q^nphi||^2.     (23)
```

Fix temporal gauge with `E=-partial_t A` and define

```text
M_n=int A dot j_n.                                   (24)
```

The product rule is exact:

```text
M_n'=-int E dot j_n+int A dot partial_t j_n.         (25)
```

Thus `G_n=F_n^PDE+M_n` satisfies

```text
G_n'
 =(lambda/2)int partial_t||phi||^2||Q^nphi||^2
  +int A dot partial_t j_n.                          (26)
```

This genuinely escapes K1478's ultralocal matter-density no-go. On its
Gauss-compatible witness, `A=0` at the testing time, so `M_n=0` while
`M_n'=-int E dot j_n`, exactly canceling the live leakage.

The work has been exchanged, not eliminated. Differentiating

```text
j_n^a=e Im<Q^(n+1)phi,D^aQ^nphi>
```

produces the two differentiated-matter terms

```text
e Im<Q^(n+1)pi,D^aQ^nphi>,
e Im<Q^(n+1)phi,D^aQ^npi>,
```

plus the gauge term

```text
e Im<Q^(n+1)phi,(partial_tD^a)Q^nphi>.               (27)
```

No same-tier coercive bound for (24), estimate for the last term of (26),
control of the radial leakage, summation over graph tiers, or global Cauchy
consequence is proved. The next PDE gate is now exact: either control
`int A dot partial_t j_n` in a coercive gauge-covariant hierarchy, or add a
second normal-form correction that does not recreate K1463's near-parallel
two-derivative loss.

## K1559 — protected admission replay

The bridge census is now 274 rows: 195 satisfied, ten conditional, 65 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, and K1145/K1150 stay `0/7`. No source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim is that every nonconstant sign field has a positive
defect gap. K1550 remains a direct counterexample. The theorem requires a
nonvanishing fixed-ratio shell component, and K1555 shows the right cutoff
exponent inside that class.

The most delicate analytic step is (8). It uses `g_N=f_N^2-1`, not `f_N`, so
the small quantity is differentiated directly; the factor `|f_N|>=1/2` is
used only on the complement of the transition set. The transition part uses
the independent `L4` estimate. Neither half alone proves the gap.

The ground-energy transfer is quantitative rather than asymptotic. K1539's
low-shell branch already has a fixed `cN^4` free floor. Once that branch is
excluded by a sufficiently small candidate constant, K1541 releases a fixed
sign-shell expectation with the explicit amplitude-error subtraction in
(20). This proves the exponent but not the coefficient.

The K1413 correction is intentionally narrow. The gauge convention is frozen,
and (25) is a product rule. Gauge invariance, coercivity and remainder control
are not inferred. The radial leakage in (23) survives unchanged.

The source boundary is unchanged. These are repository-owned cutoff and PDE
controls bordering SC-META-53, not a source-admitted measure, Hamiltonian,
gauge, physical quotient, prediction or confirmation.

## Exact next inputs

For the quantum arc, identify `E_N` beyond exponent-only `Theta(N^4)`: obtain a
matching coefficient or bounded-error recenter, then test compactness and
Mosco liminf/recovery on one common nonlinear domain. For the PDE arc, control
the differentiated-current remainder in (26) together with the pointwise
radial term, or prove that this local gauge-potential correction necessarily
loses a tier and switch to a spacetime/nonlocal hierarchy. The action-owned
primitive circle, kinetic normalization, physical carrier and faithful
observed intertwiner remain a separate source admission wake.
