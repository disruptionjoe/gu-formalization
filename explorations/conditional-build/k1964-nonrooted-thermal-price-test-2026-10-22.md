---
title: "K1964: Global thermal price law and near-optimal localization"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional quantum mathematics; no rooted completeness, sharp subleading constant, GU identification or novelty claim
scripts:
  - tests/channel-swings/k1964_nonrooted_thermal_price_test.py
  - tests/channel-swings/k1964_nonrooted_thermal_price_test_probe.py
---

# K1964: Global thermal price law and near-optimal localization

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
result: all-spectrum priced asymptotics with explicit global energy envelopes and near-optimal localization
carrier: fixed extreme four-state quantum channel, bath t=1/2, arbitrary finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input marginal half trace distance plus initial energy price ON=independent_initial_registers
real_structure: complex conserving shell unitaries and pinched real populations
grading: additive energy shells; no source chirality
action_owner: repository-construction -- fixed conditional channel
target: all-spectrum priced infimum and finite near-optimal protocols MAP-TYPE=intertwiner
```

## 1. The candidate search and the global question it leaves

[K1962](k1962-finite-tail-thermal-improvement-2026-10-22.md) optimizes the
rooted gap2 family exactly. It is an upper bound on the all-spectrum priced
infimum b(lambda)=inf_protocol [R+lambda E]. A single-thread floating scout
checked9468 orientation/price LPs over canonical paths with maximum occupied
energy13, including mixed gaps and multi-root orientations, at prices
1/10,1/25,1/50,1/100. It found no strict improvement over the rooted benchmarks.
This is search evidence ONLY: no rounded dual was accepted, no complete
finite exact census or all-spectrum optimality is claimed. At price1/100 the
rooted optimizer itself exceeds this window, a further reason not to infer
completeness. The scout did not justify more of the same finite enumeration.

The useful global successor is instead settled analytically below. Write
r0=4/25 and a=log(3/2)/2. For all sufficiently small lambda>0,

    b(lambda)=r0+(lambda/a)log(1/lambda)+O(lambda).       (1)

Every finite protocol within eta*lambda of b(lambda), for fixed eta>=0,
has

    E=(1/a)log(1/lambda)+O_eta(1),
    R-r0=Theta_eta(lambda).                            (2)

The quantifier includes arbitrary finite spectra, coherent preparations via
pinching, mixed gaps and disconnected components. It is not restricted to
rooted optimizers. The next unknown is the bounded coefficient of lambda,
not the leading lambda log law or whether low-energy near-minimizers suffice.

## 2. Explicit global exponential envelopes

Reuse [K1958](k1958-sharp-thermal-energy-rate-2026-10-22.md)'s rigorously
uniform signed-deficit and capped-energy proof, with W=25/8, c=163/440,
displacement constant D=36. It proves, for epsilon=2W delta and
B(epsilon)=W epsilon/c+epsilon^2<1,

    E >= (1/a)log(1/B(epsilon))
          -D(1+epsilon)/W -(2/a)epsilon log(1/epsilon). (3)

Take epsilon0=c/(4W)<1/2, B0=W/c+1/2. For epsilon<=epsilon0,
B(epsilon)<=B0 epsilon<1, 1+epsilon<=2 and
epsilon log(1/epsilon)<=1. Therefore

    delta >= exp(-aE)/[2WB0 exp(2aD/W+2)].

Use 2WB0<64, a<1/4, D/(2W)+2<8 and e<3. The denominator is
less than64*3^8=419904. For larger delta, delta>=epsilon0/(2W)
already exceeds1/419904. Thus the same bound holds for EVERY physical
protocol, and passes to the infimum at every finite budget E>=1:

    Cminus exp(-aE) <= R_star(E)-r0, Cminus=1/419904.    (4)

For the upper bound reuse actual finite n-left/n-right rooted shell protocols,
with E_n<=2n+41/32 and R_n-r0<=(17/50)(2/3)^n. For E>=41/32 choose
n=floor((E-41/32)/2). Since41/64<1, floor rounding gives a prefactor
at most(17/50)(3/2)^2=153/200<1. For1<=E<41/32 the single occupied
energy1 protocol has return1/2, and its excess17/50 is less than
exp(-aE). Consequently

    R_star(E)-r0 <= exp(-aE), E>=1.                    (5)

The upper uses finite physical protocols; no infinite catalyst or unproved
population-only realization enters. Constants are explicit and deliberately
loose. The sharp exponent was already K1958's result; (4)-(5) expose usable
constants for the priced and localization consumers.

## 3. Global priced bounds, with exact minimization of the envelopes

For C>0 the unconstrained minimum over real E of
C exp(-aE)+lambda E occurs at E_C=(1/a)log(aC/lambda) and is
(lambda/a)[1+log(aC/lambda)]. Restricting to E>=1 can only increase it.
For lambda<=a exp(-a), the upper-envelope minimizer E_1 is admissible.
Equations(4)-(5), and K1960's global price/energy relation, give

 r0+(lambda/a)[1+log(a Cminus/lambda)] <= b(lambda)
          <=r0+(lambda/a)[1+log(a/lambda)].             (6)

The lower bound remains valid even when E_Cminus<1; for small lambda both
minimizers lie in the domain. The width is exactly
(lambda/a)log(419904). This supplies a GLOBAL dual lower certificate,
contrasting with the rooted-family upper optimum. It is asymptotically sharp
at leading order, not a new exact finite-energy facet or sharp O(lambda) term.
The rejected third secant in K1954 remains rejected.

## 4. All near-minimizers have a localized resource scale

Let a finite physical protocol satisfy R+lambda E<=b(lambda)+eta lambda.
Set E=log(a/lambda)/a+x and y=ax. Its universal lower bound(4) and the
upper bound in(6) imply

    y+Cminus exp(-y)<=1+a eta.                         (7)

The left side is strictly convex, tends to infinity at both ends, and has
minimum1+log(Cminus)<1. Thus(7) confines y to a fixed compact interval
[y_minus(eta),y_plus(eta)], the two roots of equality. This proves the energy
statement in(2), uniformly over dimensions, spectra and internal motifs.
Moreover

    (Cminus/a)exp(-y_plus) lambda <=R-r0
       <=[(1-y_minus)/a+eta] lambda.                   (8)

These strictly positive finite constants prove the return statement.
At eta=0 this applies to any attained optimizer if one exists; the theorem
does not assert attainment. For every eta>0 finite near-minimizers exist by
the definition of the finite-protocol infimum. Increasing dimension or using
non-rooted configurations cannot evade this localization, though either may
improve the unresolved subleading coefficient. The resource is initial mean
energy, not preparation work, reset cost, bandwidth or repeated-use return.

## 5. Verification and scientific boundary

The producer checks128 rational constant/family inequalities and1167 full
complex physical shell controls for three finite protocols. The separate
probe reconstructs bath weights and actual incoming populations and checks
the exponential minimizer and localization identity symbolically:23 exact/
symbolic controls. Four actual mathematical faults alter the lower prefactor,
a population, the optimizing energy and the shifted price expression; all
are rejected after a green baseline. Upstream K1958's all-spectrum analytic
proof and K1960 dual bridge are reused by unchanged pins, not newly certified
by these finite checks. Scout floating LPs are not included in proof counts.

Hostile review: (6) is global but does not establish rooted completeness;
(7) constrains physical near-minimizers, not hypothetical minimizers of a
population relaxation. The lower bound uses capped-energy control, avoiding
an unjustified first moment of a small negative deficit. Upper bounds are
physical finite constructions. Internal analytic review found no remaining
issue in this scope; no external expert or formal certification is claimed.

[Ng et al.](https://arxiv.org/abs/1405.3039) supply general context on
mean-energy restrictions in thermal catalysis; the abstract was rechecked.
No novelty or GU claim is made. SC-META-53 remains UNCERTAIN and
LT-SM8/LT-GR6b/AC-F1 remain NEEDS. The next discriminating question is an
all-spectrum subleading priced lower bound or a physical non-rooted motif
that improves K1962, not further checks of the leading logarithmic law.
