---
title: "K2465 Sharp original leakage compensation and binary stopping limits"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional sharp half-routing compensator and exact-cost confidence scale; no inferred budget or physical experiment"
---

# K2465 Sharp original leakage compensation and binary stopping limits

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2465
carrier: original predictable binary test/use laws and success-weighted conditional output model LAYER=toy CHIRALITY=N/A
pairing: conditional expectation and supplied positive-Hilbert output pairing ON=declared_carrier
real_structure: real probabilities and real nonnegative adapted processes
grading: classical histories and test/use branches
action_owner: repository-construction -- supplied conditional mathematical models
target: Sharp original leakage compensation and binary stopping limits MAP-TYPE=evaluation
```

## Result and unchanged event

For the original half-test/half-use, eta=1/2, zero-failure certificate,
the smallest uniform linear compensation is explicit. This improves the
coarse K2459 coefficient and its original-budget transfer. A separate exact
per-step normalization makes K2462's inverse-confidence coefficient sharp
within actual binary experiments. The budget still must be independently
justified. Neither passing tests nor this theorem estimates leakage.
SC-META-53 remains UNCERTAIN; LT-SM8, ledger0.263 and canon are unchanged.

## 1. Exact predictable compensation

Given history-predictable a,b in[0,1], fresh routing pi in(0,1), k>0,
r=1-exp(-k),u=1-pi and c=log(1+pi*r/u), the original one-step multiplier
has conditional expectation

    G=pi(1-r a)+u exp(c b).

Thus h=log max(1,G) is the smallest nonnegative predictable logarithmic
compensator for that multiplier. For Z=sum U c b-sum T k X and H=sum h,
M=exp(Z-H) is a nonnegative supermartingale. At k=infinity a test failure
makes M zero forever; no restart is permitted. The positive part makes H
nonnegative and increasing, which the expected-budget argument needs.

Under the initial law E H_infinity<=K_H, stop at the first crossing of
Z>=L or a finite horizon. If crossing has probability p, conditional
Jensen and optional stopping give

    1>=p exp(L-K_H/p).

Hence L=log(1/epsilon)+K_H/epsilon controls every finite prefix and every
stopping time. This reuses K2462's proof with the exact smaller H. It does
not condition on the rare initial mode or the final passing transcript.
A fixed-horizon expectation bound only licenses that horizon. Under a
pathwise cap H<=B_H, Ville instead gives log(1/epsilon)+B_H.

## 2. Sharp coefficient for the original half/half budget

Fix pi=eta=1/2,k=infinity. Let d=(b-a)_+,q=a+d/2 and
v=d^2/[4q(1-q)], with coincident endpoints set to zero. Put

    c=log2, J=(1-c)/2, L=c-1/2,
    Cstar=(1+L)^2/(4L), gammastar=2Cstar.                (1)

For every original a,b, G=(1-a)/2+2^(b-1)<=1+Cstar*v.
Cstar is the smallest possible constant. Moreover

    log max(1,G)<=gammastar log(1+v/2),                (2)

and gammastar is the smallest uniform transfer constant.
These sharp statements are for the specified parameters, not arbitrary pi,
eta or finite k. K2459's general parameter theorem remains available.

For a>=b, v=0 and convexity gives G<=1. Otherwise d>0, b>0 and q in(0,1).
Write B=b(1-b), Delta=(1+b-2^b)/2=B h0(b), where the continuous endpoint
values are h0(0)=J,h0(1)=L. The second divided difference of exp(ct) gives

    h0(b)=(c^2/2) integral_{x,y>=0,x+y<=1} exp(c(x+b y)) dx dy.

This identity follows from two applications of the fundamental theorem of
calculus (the divided-difference simplex formula). The exact series
c=2 sum_(n>=0)1/[(2n+1)3^(2n+1)] yields56/81<c<25/36;
in particular2/3<c<7/10 and c>11/16. Simplex moments integral y=1/6,
integral y^2=1/12, and1<=exp(c(x+b y))<=2 give

    3/20<h0<1/5, 3/125<h0'<3/50, 0<h0''<21/1000.

The first bound also uses monotonicity and endpoints. With
w=1/2+(2b-1)h0/2, these imply w>=2/5,w'>=3/25,w''>=3/80.
Also9/5<Cstar<361/192<2. For F=w^2-Cstar h0,

    F''>=2(3/25)^2+2(2/5)(3/80)-2(21/1000)=21/1250>0.

F(1)=0 and w(0)^2/J<=289/240<9/5<=Cstar, hence F(0)<0.
Convexity implies F<=0 on the interval. Finally

    B=d^2/(4v)-(2b-1)d/2+d^2/4,
    G-1=d/2-B h0<=w d-h0 d^2/(4v)<=w^2 v/h0<=Cstar v.

The last inequality is completion of a real square, not a sampled bound.
For sharpness set b=1-z,d=t z,a=1-(1+t)z with t=4L/(1-L).
As z decreases to zero these remain admissible and

    (G-1)/v -> (t/2-L)(4+2t)/t^2=Cstar.

Since v tends to zero, log G/log(1+v/2) tends to2Cstar. The upper transfer
(2) follows from log(1+Cstar v)<=2Cstar log(1+v/2), whose derivative
inequality holds since2Cstar>1. This proves both optimal constants.

## 3. Actual binary sharpness of expected exact cost

For general fixed pi and k=infinity, choose a rare initial mode with
probability p>epsilon. In that mode set a=0,b=delta>0 until the m-th
actual use, then set a=b=0. Safe mode has a=b=0 throughout. This is a
predictable rule with fresh routing; every test passes. The waiting time
has mean m/u, and all rare paths reach the endpoint almost surely. Thus

    Z_tau=c delta m,
    E H_infinity=(p m/u) log(pi+u exp(c delta)),
    rho_delta=u c delta/log(pi+u exp(c delta)) ->1.     (3)

For any proposed coefficient lambda<1, choose p>epsilon and small delta
with lambda p/epsilon<rho_delta, then m large enough that
Z_tau>log(1/epsilon)+lambda E H_infinity/epsilon. Crossing occurs with
probability p>epsilon. Thus coefficient1 is sharp in this actual binary
class for the EXACT H, not merely an abstract supermartingale class.
It is not a sharpness theorem for the old coarse H or for original budget B.

For B=sum log(1+pi v), the same law gives necessary leading coefficient
u c/[pi(1-eta)]. At half/half it is2log2, below gammastar. The minimax
expected-B confidence coefficient therefore remains between these bounds;
sharp pointwise transfer does not prove sharp stopped expected-B transfer.

## 4. Original output consumer and contrary evidence

For fixed half/half, use K2459's success-weighted original output theorem,
trusted complete-effect gap nu, average calibration beta, privately
initialized controller independent of current resource test/E data, history-
selected ideal controller, operation error kappa, ideal heralding qherald>0,
and separately positive actual mean success. Let

    e=(tau-kappa/qherald)/Cout>0, D=nu e^2-beta>0.

An independently justified pathwise original B cap gives

    Nuse >= ceil([log(1/epsilon)+gammastar B]/[log2 D]).

For an expected original cap K replace gammastar B by gammastar K/epsilon.
For expected exact H cap K_H use K_H/epsilon instead. These are distinct
premises; one cannot relabel the same numerical cap across them. The probe
computes rigorous prospective counts for nu2/5 and9/20, epsilon.05,
B or K=10^-6,beta10^-8,kappa10^-6,qherald1/4,Cout2,tau.01. These are
not measured device capabilities. Systematic floors persist.

The actual pair a49/50,b99/100 has v1/591 and G1/100+2^(-1/100),
which violates coefficient9/5. Pair a1/2,b1 rejects unit original-budget
transfer. A=b=1/2 has G<1, showing that signed log G permits refunds;
H must retain its increasing positive-part form for the stated expectation
proof. The probe includes an explicit rare-mode law that violates a
half-strength expected-H penalty while satisfying the claimed budget.
Written universal proofs, exact counterlaws and interval calculations are
separate. Internal independent review is not experimental, external-expert,
proof-assistant or novelty certification.

[Probe](../../tests/channel-swings/k2465_sharp_leakage_compensator_probe.py) and [report](../../lab/process/k2465-sharp-leakage-compensator.json).
