---
title: "K2158 Local squeezing strictly improves detector field-energy budgets"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: independent fixed-mode mathematics; no total apparatus cost or GU recovery
scripts:
  - tests/channel-swings/k2158_local_squeezing_detector_energy_probe.py
---

# K2158 Local squeezing strictly improves detector field-energy budgets

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2158 exact field-energy frontier for diagonal instruments followed by one common real squeeze
carrier: positive scalar-field Fock space, fixed real normalized compact smear f and fixed photon-added signal a_h dagger Omega LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert inner product ON=declared_carrier
real_structure: real smear and real canonical squeeze Q maps to xQ, P maps to P/x, x positive
grading: occupation number n_b; no ambient GU spinor grading
action_owner: repository-construction -- supplied free positive scalar Hamiltonian and local quantum operations
target: fixed-effect instrument enlargement and exact scalar energy reparametrization MAP-TYPE=intertwiner
```

## Result and changed operation class

[K2156](k2156-energy-budget-detector-frontier-2026-10-27.md) settles the energy-versus-detection
frontier for diagonal nondemolition instruments on one fixed oscillator. Append one
common real squeezing unitary to every outcome, preserving the entire POVM and its
fixed-signal ROC. This strictly lowers the energy of every nonzero-energy optimal
diagonal detector. The enlarged frontier is an **exact scalar reparametrization** of
K2156, not a new high-dimensional search. Its saturation budget is strictly smaller.

This is independent detector mathematics on a supplied positive free field. It derives
no GU physical state or source mechanism. It optimizes precisely diagonal instruments
followed by one common deterministic real squeeze. Outcome-dependent squeezing,
randomized squeeze schedules and arbitrary local channels are different larger classes.
No global optimum over all local instruments, autonomous controller or thermodynamic
cycle cost is asserted. The fixed physical signal, mode and field Hamiltonian do not change.

## 1. Freeze the model and the full record

Reuse [K2151](k2151-optimal-local-mode-discrimination-2026-10-27.md): omega>0,
H=dGamma(omega)>=0, vacuum Omega, real normalized smooth f with finite moments
m_j=<f,omega^j f>, canonical Q=phi(f), P=pi(f), [Q,P]=i,
nu=sqrt(m_1/m_-1), b=(sqrt(nu)Q+iP/sqrt(nu))/sqrt2,
N=(sqrt(m_1 m_-1)-1)/2>0, z=N/(N+1). The signal is the same a_h†Omega.
Write L=m_-1 m_2>0 and E_sum=E_h+E_j as in K2151/K2153.

Let K_(r,a)=f_(r,a)(n_b) be any countable complete diagonal instrument. Keep its
reported outcome r and all effects E_r=sum_a K_(r,a)† K_(r,a). For x>0 let U_x
be the oscillator squeezing unitary with

    U_x† Q U_x=x Q,       U_x† P U_x=P/x.

The new Kraus operators are L_(r,a)=U_x K_(r,a). Then L†L=K†K exactly.
All outcome probabilities are unchanged for every input, including inputs entangled
with a reference. The postmeasurement state changes; this is not an identity of
recorded channels. U_x is a bounded unitary in the same oscillator von Neumann
algebra even though its self-adjoint quadratic generator is unbounded.

## 2. Exact global field energy from local covariances

Let E be the unread vacuum output energy of K. The diagonal channel leaves the
local thermal reduced state unchanged, so

    <Q²>=m_-1/2,       <P²>=m_1/2.

It also leaves every complement observable unchanged, since it is trace preserving
and local. Decompose the equal-time quadratic Hamiltonian into the f oscillator
and its orthogonal canonical complement:

    H = P²/2 + m_2 Q²/2 + Q phi((omega²-m_2)f) + H_perp + constant.

Only the cross expectation changes under the diagonal channel. Vacuum stationarity
and the two-point function give

    <Q phi((omega²-m_2)f)> = E + (m_1-L)/2.                 (1)

The combination is finite under the fixed smooth-mode assumptions; the finite two-mode form-domain argument below justifies the quadratic calculation. No assumption
that span(h,j) is invariant under omega is needed. Squeezing scales the cross term by x,
Q² by x² and P² by x^-2, leaving the complement fixed. Therefore the new energy is

    E_x = x E + A(x),
    A(x)=m_1/4 (x^-2+2x-3) + L/4 (x-1)².                  (2)

A(x) is precisely the energy of U_x Omega. It is nonnegative: A(1)=A'(1)=0 and
A''(x)=3m_1/(2x^4)+L/2>0. The infinite sums in the diagonal channel have finite
energy by K2153's bound E<=4 E_sum z/(1-z)². The unchanged local second moments,
finite cross form and fixed finite x show the squeezed outputs also have finite
energy. More directly, K and U_x act inside Fock(span{h,j}). Both b,c
occupations start at finite N and finite squeezing preserves finite total second
moments; the inverse Bogoliubov map gives finite h,j occupations. The restriction
of the omega quadratic form to span{h,j} is a bounded2x2 positive matrix, hence
the full states have finite H form norm even when that span is not omega-invariant.
This avoids subtracting uncontrolled infinite complement energies. The proof applies
to complex diagonal Kraus, not just positive roots.

For an independent covariance check use the Schmidt oscillator c, s=sqrt(N(N+1)),
t=Re<bc>=s-E/(2 E_sum s), and the Bogoliubov inverse of K2151. The transformed
h,j occupations and cross expectation reproduce(2); this second derivation is
checked symbolically and on the inherited exact three-mode fixture.

## 3. Optimize the squeeze, then the detector

For a given E>=0 define

    g(E)=min_(x>0) [xE+A(x)].                              (3)

Strict convexity and divergence at x=0 and x=infinity give a unique minimizer x_E.
It equals1 when E=0; for E>0 it lies strictly between0 and1 and satisfies

    2E+m_1(1-x_E^-3)+L(x_E-1)=0.                           (4)

Multiplying by x_E³ gives a quartic with a unique positive root. In particular,
g(0)=0, 0<g(E)<E for E>0, and g'(E)=x_E>0 by differentiating the minimizing
formula. Thus g has a continuous increasing inverse on its range. It is concave
as an infimum of affine functions; this does NOT imply concavity of the new
contrast frontier. At large E, x_E is of order E^-1/3 and g(E) diverges of order
E^2/3, so its inverse is defined for every nonnegative budget.

For each fixed set of effects, K2153's positive-square-root Kraus minimize E.
Since x>0, they minimize(2) at every squeeze, and since g is increasing they also
minimize after optimizing x. Therefore if V(b) denotes K2156's maximum contrast
at normalized diagonal budget b, the exact enlarged-class frontier is

    V_sq(B) = V(g^-1(B)/E_sum).                            (5)

V is already capped by the all-POVM total variation. Equation(5) also proves
attainment using the existing attained diagonal optimum and the unique squeeze.
For any positive diagonal energy target the required budget strictly decreases.
This is not a claim of strict contrast improvement after saturation.

Let b_sat be K2156's normalized saturation threshold (including its likelihood-tie
case). The new threshold is exactly g(E_sum b_sat), strictly below E_sum b_sat.
No new optimized effect sequence or high-precision finite conic replay is required:
K2156's certified tail bounds transport through this monotone scalar map.

## 4. Exact unchanged-ROC improvement and scalar certificate

Use the inherited finite-mode control omega=diag(1,9,4), f=(1,1,0)/sqrt2.
Then m_1=5, m_-1=5/9, m_2=41, L=205/9, N=1/3, z=1/4, E_sum=10.
The equal-prior optimal threshold n_b>=1 has alpha=1/4, eta=1, error=1/8,
and old saturation energy E=5. Choose x=4/5. Direct rational evaluation yields

    E_x = 12761/2880 < 5.                                  (6)

Its positive difference from the old budget is1639/2880. This is an exactly feasible
instrument with the SAME effects and ROC. It leaves total physical energy nonnegative;
it extracts part of measurement-induced excitation, not energy from the vacuum below0.
The unique optimum is specified by

    205 x^4 -70 x^3 -45=0,       0<x<1.                     (7)

The probe brackets its root with rational bisection, evaluates a feasible rational
upper energy, and uses a global convex tangent to bound the minimum below. These
are exact rational bounds, not a numerical-optimizer success assertion. The report
stores the bracket and can be replayed without an optimizer. In particular it certifies
4.4289859434858 < g(5) < 4.4289859434859.

Near zero, implicit differentiation of(4) gives

    g(E)=E-E²/(3m_1+L)+O(E³).

Thus the strict energy improvement starts at second order. K2156's leading
small-budget law remains V_sq(B)~sqrt(B/(z E_sum)). Its diagonal lower bound
E>=z E_sum Delta² transports to B>=g(z E_sum Delta²) in this declared class.
This is an actual consequence of the proved transformation, not transfer of the old
untransformed energy inequality.

## 5. Useful continuation and resource limits

Equation(2) shows why this improvement was absent from the diagonal class: the reduced
oscillator stays thermal but global cross correlations change. One common squeeze
uses those correlations while preserving the detector's evidence. The next larger
question is outcome-dependent Gaussian feedback or other non-diagonal operations at
fixed effects; it must account for conditional covariances and prove its own optimum.
Randomizing instruments is another distinct enlargement; no concave-envelope theorem
for that class is asserted here.

The energy here is final unread FIELD excitation above the original vacuum. Squeeze
preparation, switching, record storage/reset and signal preparation are uncharged.
K2154's G-commuting switched-control estimates do not apply: squeezing changes G.
A stable autonomous implementation with full accounting remains an independent task.
No causal continuum velocity, free apparatus or GU recovery follows.

Closest general context is restricted Gaussian work extraction/passivity, studied by
[Brown, Friis and Huber](https://arxiv.org/abs/1608.04977), and subsystem-constrained
operations in [Frey, Funo and Hotta](https://arxiv.org/abs/1404.5081). These references
motivate the operation-class distinction, not the present exact frontier formula;
no novelty claim is made. This is not remote quantum-energy teleportation.

The probe distinguishes symbolic covariance identities, exact rational controls and
certified one-variable bounds from the written domain/attainment argument. Real
coefficient, squeeze, signal-effect and covariance faults must fail after a clean
baseline. Independent internal review checks the mathematical transfer, not merely
report consistency. No external certification or proof-assistant verification is claimed.
