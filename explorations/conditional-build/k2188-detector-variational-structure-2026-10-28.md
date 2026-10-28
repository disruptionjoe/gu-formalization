---
title: "K2188 All-contrast interiority and the detector multiplier criterion"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive free-field binary diagonal instrument, arbitrary feasible signed contrast and threshold, vacuum output field energy only
scripts:
  - tests/channel-swings/k2188_detector_variational_structure_probe.py
---

# K2188 All-contrast interiority and the detector multiplier criterion

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2188 all-contrast optimizer structure and common first-order noise slope
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

For every nonzero exact signed contrast |d|<3/4, every fixed positive
squeeze pair has a unique minimizing infinite effect, and each coordinate
is strictly between its caps. At any jointly minimizing profile, all
neutral-replacement noise biases have the SAME first-order energy derivative
-eta d. Adaptive bias does not give an independent first-order escape at
minimizers. The sign of eta remains a substantive unresolved condition.

This extends the half-contrast fixed-squeeze result of K2176 to all nonzero
interior contrasts. It does not prove joint-squeeze uniqueness, global
frontier monotonicity or threshold saturation. A new exact Dirichlet
reformulation and a formal zero-multiplier tail show why bounded squeezes
and leading tail stationarity alone do not supply the missing sign.

The object remains the supplied positive scalar Fock model, binary diagonal
square-root Kraus instrument, and one real squeeze per reported outcome.
The cost is vacuum output FIELD energy, excluding apparatus, clock,
preparation, switching, reset and total work. SC-META-53 remains UNCERTAIN;
LT-SM8/LT-GR6b, source, ledger0.263, canon and physical quotient do not change.
No new half-contrast numerical bound, optimum or novelty claim is made.

## 1. All nonzero interior contrast slices

Use p_n=(3/4)4^-n, q_n=3n-1, 0<=x_n<=p_n, y=p-x and

    R(x)=sum(n+1/2)x_n, T(x)=sum(n+1)sqrt(x_n x_(n+1)),
    A(s)=41s^2/6+3/(2s^2), C=40/3,
    E(x;s1,s0)=R(x)A(s1)+R(y)A(s0)
               -C[s1T(x)+s0T(y)]+35/18,
    H(x)=min_(s1,s0) E(x;s1,s0), d(x)=sum q_n x_n.

Let r+ have x0=0 and xn=pn for n>=1; r-=p-r+.
Their contrasts are +3/4 and -3/4. For 0<|d|<3/4 put

    t=4|d|/3, v=(1-t)p/2+t r_(sign d).            (1)

This reference has exact contrast d and a uniform cap margin (1-t)/2.
At fixed s1,s0>0, compactness and geometric domination give a minimizer.
Each branch has positive mass since d!=0. If a coordinate is zero, some
adjacent zero/positive edge exists. Mixing toward v creates a positive
square-root-order coherence gain at that edge. Concavity bounds the loss
on all other edges by their finite summed O(epsilon) change; linear moments
also change by O(epsilon). The gain dominates. Applying this argument to
both branches excludes every zero or saturated coordinate. This does not
assert a uniform margin for the minimizing effect.

Equality at the midpoint of two fixed-squeeze minimizers forces equality
in each geometric-mean term. Connectedness gives x'=a x and y'=b y.
Then (a-b)e_n=1-b. Unless a=b=1 the effect is constant and d=0, a
contradiction. Thus the minimizer is unique. This proof does not imply
uniqueness after optimizing squeezes, and its nonzero-contrast hypothesis
is essential to the uniqueness argument.

Joint minimizers exist by the existing compact squeeze bound
S=[2/3,113/100] and product compactness. Each is a fixed-squeeze minimizer
at its own squeezes, so the conclusions above apply to every joint
minimizer on these slices.

## 2. Multiplier and rigorous infinite noise derivatives

At an interior minimizer define branch gradients g1_n=partial T(x)/partial x_n
and g0_n=partial T(y)/partial y_n, and

    h_n=(n+1/2)[A(s1)-A(s0)]-C(s1 g1_n-s0 g0_n).

Finite variations delta x_j=1, delta x0=q_j preserve contrast for j>=1.
They are feasible with either sign for sufficiently small amplitude. Thus

    h_n=eta q_n, eta=-h0
       =(C/4)[s1 sqrt(e1/e0)-s0 sqrt((1-e1)/(1-e0))]
         -[A(s1)-A(s0)]/2.                       (2)

This is a finite-variation proof, not an assumed infinite multiplier theorem.
[K2176](k2176-detector-certified-convergence-2026-10-27.md), section2,
provides the needed summability argument, which does not depend on d=1/2:
at each n at least one branch coordinate is >=pn/2, so its gradient is
bounded by [n sqrt(8)+(n+1)/sqrt(2)]/2. Equation(2) bounds the other positive
branch gradient by another constant times n+1. Hence both p-weighted
gradient sums converge absolutely.

For beta in[0,1] consider x_t=(1-t)x+t beta p. Its contrast is (1-t)d.
For each branch, write z_t=(1-t)[z+(t/(1-t))gamma p], gamma>=0.
The positive-direction derivative of each concave geometric-mean term
is bounded by its derivative at z, whose sum against p is finite by the
preceding bound. Dominated convergence gives the whole infinite derivative;
homogeneity supplies the -(z) direction. Strict convexity of A and positive
branch R give unique continuous optimizing squeezes, permitting the envelope
derivative. Therefore, including beta=0 and1,

    d/dt H(x_t)|_(0+) = sum h_n(beta pn-x_n)
                     = -eta d.                  (3)

A profile-dependent choice of beta has the same first-order derivative.
This says nothing about second order or arbitrary profile-changing paths.

For Ep(s)=(5/6)A(s)-(2C/3)s+35/18 and
D(z)=DT(z)[p], define

    Q_z=Ep(s_z)-C s_z[D(z)-2/3].

The exact K2186 noise identity and(3) imply

    Q_x=Q_y=H-eta d.                              (4)

Failure of Q_x=Q_y is therefore an explicit necessary-condition rejection
for an interior exact-contrast local minimizer with its optimized squeezes.
It is not a sufficient optimality test. Since
D(z)=1/2 sum(n+1)pn[r_n+1/(4r_n)]>=2/3, (4) gives the sufficient test

    H>min(Ep(s1),Ep(s0))  =>  eta d>0.            (5)

No claim that(5) holds at every optimizer is made. In particular the K2186
softened-tail counterexample violates(4), as checked with full-tail rational
intervals here; its failed noise descent cannot be transferred to minimizers.

## 3. Consequences for the true frontier

Let F(d)=min H(x) at exact contrast d and V(d)=min H(x) at contrast >=d,
for 0<d<=3/4. Outcome exchange gives the same absolute-threshold problem.
K2180 supplies local Lipschitz continuity in the interior. At a point where
F is differentiable, take any optimizer and change only coordinate zero by
-epsilon. Interiority permits both signs, contrast changes by epsilon and
optimized energy changes by eta epsilon+o(|epsilon|). The two one-sided
upper comparisons with F(d+epsilon) prove

    F'(d)=eta                                    (6)

for every optimizer at that differentiability point.
Consequently nonnegative eta for optimizing profiles would prove
monotonicity on compact interior intervals by absolute continuity, and then
on the closed feasible interval by the existing continuity at endpoints.
It would give F=V. Strict eta>0 additionally rules out any interior slack
threshold minimizer: a slack minimum is locally unconstrained in contrast,
so (2) with a contrast-changing variation would force eta=0. A slack
maximal-contrast endpoint is separately excluded by the existing K2182 cusp
and its lower-energy nearby profiles. None of these implications establishes
the missing multiplier sign.

Threshold KKT nonnegativity by itself cannot prove strict saturation: it
allows a zero multiplier at a slack minimum. Fixed-squeeze uniqueness also
cannot supply uniqueness of the jointly optimized instrument.

## 4. Released Dirichlet form and the zero-multiplier tail

For w=sum x_n and e_n=x_n/p_n, direct summation gives

    T(x)=(5/4)R(x)-(3/8)w-(1/4)D_e,
    D_e=sum(n+1)pn(sqrt(e_(n+1))-sqrt(e_n))^2.      (7)

All sums converge; expansion uses pn+1=pn/4, so the two square sums are
M+w and4M. The full fixed-squeeze energy is therefore a constant plus

    sum{[Delta A-(5C/4)Delta s](n+1/2)
            +(3C/8)Delta s}x_n
       +(C/4)[s1 D_e+s0 D_(1-e)],                (8)

with constant (5/6)A(s0)-(2C/3)s0+35/18.
This exposes a linear occupation preference and two nonnegative Dirichlet
terms; it does not make H jointly convex after eliminating squeezes.

For any true branch optimum 0<=A'(s)<C. Thus if s1>s0,
Delta A<C Delta s and the n coefficient in(8) is negative.
A formal polarized tail with e_n->1 and
(1-e_(n+1))/(1-e_n)->r in(0,1) is compatible with eta=0 at leading order if

    s0(r^(-1/2)+r^(1/2)/4)=(5/4)s1-Delta A/C.     (9)

The right side divided by s0 is strictly greater than5/4. The left function
of r decreases continuously from infinity to5/4 on(0,1], so there is a
unique formal ratio r. Equation(9) is not a constructed stationary profile,
not a zero-multiplier optimizer and not a counterexample to monotonicity.
It demonstrates that this tail-only sign argument does not yield the
needed contradiction; the complete recurrence and global minimizing
property remain essential. The probe tests an exact algebraic ratio for
a rational squeeze pair within the necessary A' bounds.

## Verification and next question

Finite rational and symbolic controls check the reference contrasts/caps,
full-tail Dirichlet identity and energy, multiplier coefficient, tail
characteristic equation and necessary-condition rejection of a genuinely
nonoptimal profile. They are separate from the universal interiority,
summability and frontier proofs above. Planted faults change the geometric
tail, contrast weight, Dirichlet coefficient, multiplier or tail equation.
A green baseline is required before fault detection. Independent internal
review checks the analytic transfer; no proof-assistant/external-expert,
new optimum, physical apparatus or GU certification is asserted.

Next prove the multiplier sign using global minimizing structure, or find
and certify a true slack threshold optimizer. Another adaptive constant-bias
choice cannot change the first derivative. The complete nonconvex solver
and shared field-clock/preparation/reset model remain separate alternatives.
K2182 endpoint behavior, weak-contrast353/170 and K2176 half-contrast
bracket remain unchanged.
