---
title: "K1942: Complete cut duality for scalar phase energy"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: independent conditional mathematics; no native GU, novelty, external acceptance or formal proof
scripts:
  - tests/channel-swings/k1942_complete_scalar_energy_duality.py
  - tests/channel-swings/k1942_complete_scalar_energy_duality_probe.py
---

# K1942: Complete cut duality for scalar phase energy

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
result: no-gap countable finite-cut energy dual, convergent relaxed phases and certified phase-error consumers
carrier: supplied massless two-characteristic scalar control on a finite tube LAYER=toy CHIRALITY=N/A
pairing: real Lebesgue marginal duality and projected Dirichlet inner product ON=three_free_intervals
real_structure: real phase lifts and signed bounded measurable pulses
grading: propagation direction only; no source chirality
action_owner: repository-construction -- common scalar spacetime potential
target: fixed plateau contrast with zero opposite phase and optimal gradient energy MAP-TYPE=intertwiner
```

## 1. A complete characterization, with an explicit numerical ceiling

Use exactly [K1940](k1940-joint-scalar-amplitude-energy-cuts-2026-10-22.md)'s
c=1,T=9/2,I=[-3,3], phase+1 on[-2,-1], phase-1 on[1,2], zero boundary
trace and zero area. The opposite characteristic phase is0 and |V|<=M.
The baseline phase phi0 has gradient energy4. Write phi=phi0+delta, where H
is H1_0 on the three free intervals(-3,-2),(-1,1),(2,3), restricted to total
integral0, with norm squared integral|delta'|^2.

The full measurable-pulse optimum satisfies the exact no-gap formula

    J_star(M)=4+sup_{finite rational-union signed cuts, lambda>=0}
                   [2 lambda.D(M)-lambda^T K lambda].         (1)

Here D_i=int_(A_i) phi0-(M/2)C(A_i), with signs absorbed into the functional
and deficit, and K is the Gram matrix of its ZERO-AREA projected Dirichlet
representers. The supremum includes the empty family. It may be infinite.
There is no claim of a finite maximizing family or smooth-pulse attainment.
This closes the completeness question left open by individual cut bounds,
not the evaluation of the numerical joint optimum.

A new exact consumer at M=23/100 gives

    1730979348830867/432645592385000 <= J_star <= 30/7.        (2)

The lower is approximately4.0009175623 (the rational is authoritative).
The existing K1940 exact continuum pulse supplies the upper. The gap remains
positive. In particular, neither a finite-cut minimizer nor(2) is a matching
global primal/dual solution.

## 2. Rational interval unions exhaust all measurable cuts

K1914's exact measurable-pulse theorem says that feasibility is equivalent
to every cut inequality |int_A phi|<=(M/2)C(A), where

    C(A)=int_J min(a_A(z),ell(z)-a_A(z)) dz,
    a_A(z)=|A intersect[z-9,z]|, ell(z)=|I intersect[z-9,z]|.

Finite unions of intervals with rational endpoints are dense in measurable
subsets of I in symmetric-difference measure. Moreover

    |C(A)-C(B)| <= 9 |A symmetric_difference B|.

Indeed min(a,ell-a) is1-Lipschitz in a, and Fubini bounds int|a_A-a_B|
by9 times the symmetric difference. Each H1 phase is bounded, so int_A phi
is continuous under the same approximation. Hence ALL measurable cuts are
equivalent to the countable family of rational finite unions, including both
signs. Half-lines alone are not claimed sufficient.

For a rational union, a_A and ell are piecewise affine with rational knots.
Insert their crossing points2a_A=ell and integrate the smaller affine piece.
This computes C(A) exactly. Its Dirichlet representer is piecewise quadratic;
subtract its mean using h=G1, int h=5/6. All coefficients and Gram integrals
are rational. Arbitrary unions can be assembled by linearity from halfcut
representers, while capacities must be computed for the actual union.
The producer implements the rational capacity computation and tests central
halfcut, plateau and complement cases.

## 3. Finite-cut strong duality without a Slater assumption

Enumerate the signed rational-union inequalities and retain the first n.
Let P_n={delta in H: <g_i,delta><=-D_i, i<=n}. If nonempty, its minimum-norm
point delta_n lies in span{g_1,...,g_n}: an orthogonal component changes no
constraint and strictly increases norm. This is a finite-dimensional
polyhedron, even if the Gram matrix is singular or its interior is empty.

The projection's normal-cone/Farkas characterization gives nonnegative
multipliers with

    delta_n=-sum lambda_i g_i,
    K lambda >= D, lambda_i((K lambda)_i-D_i)=0.             (3)

Thus J_n=4+||delta_n||^2 equals the maximum in(1) for that finite family.
This uses the finite polyhedral normal cone, not an unverified infinite
constraint qualification. A singular Gram matrix need not be inverted:
a conic basis of active normals suffices. If P_n is empty, finite Farkas
supplies lambda>=0 with sum lambda_i g_i=0 and lambda.D>0; scaling it makes
the dual unbounded. A zero representer with positive deficit is the simplest
case. For the plateau A=[-2,-1], g_A=0, C(A)=9, int_A phi0=1. Hence M<2/9
is already certified infeasible by ONE exact cut.

## 4. Full duality, strong convergence and infeasibility

The sets P_n decrease. If the full problem is feasible, their projections
have bounded norms, since any fully feasible delta is a competitor. Take a
weakly convergent subsequence. Every fixed inequality holds eventually and
passes to the limit; section2 and K1914 then give a feasible pulse for the
limit phase. Weak lower semicontinuity bounds its energy by lim J_n.
The reverse inequality J_n<=J_star is automatic, so

    J_n increases to J_star.

Strict convexity gives the unique optimal phase delta_star. Every weak
cluster point is that optimizer, and convergence of norms upgrades weak to
STRONG convergence in H. This proves(1) as a supremum over finite supported
multipliers, without asserting that an infinite multiplier measure exists
or that finite support attains the supremum.

If the full problem is infeasible and every P_n remains nonempty, their
minimum norms must tend to infinity: otherwise the same weak-compactness
argument would produce a fully feasible limit. Thus(1) covers both a finite
Farkas witness and infeasibility visible only as diverging finite-cut energy.
This is a completeness theorem, not a finite detection bound, convergence
rate, or promise that a practical halfcut-only search will find every cut.

## 5. Exact finite certificates and a missed-cut counterexample

Start with the K1940 cut s=-9/20. Include its reflected partner+9/20 using
C([-3,s])=(3-|s|)(6+|s|) for |s|<=1. The exact nonnegative multipliers are
13992/222557 for both cuts, giving

    J_two=4452159667/1112785000.

The two-cut minimizer is nevertheless NOT globally feasible. At the rational
halfcut s=-227/500 its remaining positive deficit is exactly

    34994061/6954906250000.

That is a violated physical cut, not rounding noise. Adding this cut and its
reflection releases the stronger lower endpoint in(2); its active multipliers
are5456505000/86529118477 on the two new cuts, with zero on the old pair.
Adding the coarser cuts at+/-2/5 and+/-1/2 alone did not improve J_two.
This explicitly tests and rejects the shortcut “more cuts means full
feasibility.” No further finite-cut saturation is asserted.

For each certificate the code checks actual projected Gram matrices,
nonnegative multipliers, all retained primal inequalities, complementary
slackness and matching finite primal/dual energy. The independent probe solves
-v''=1_A separately on every free interval, imposes both endpoint conditions
and derivative continuity, removes the mean, and integrates its derivative
products. It does not simply replay a stored scalar formula.

## 6. Released quantitative consumers

Let a genuine feasible pulse have phase phi_p and energy U, and let L be any
certified dual lower bound. The projection inequality at the full optimizer
implies

    ||(phi_p-phi_star)'||_2^2 <= U-J_star <= U-L.

The analogous inequality for the relaxed projection gives
||(phi_n-phi_star)'||^2<=J_star-J_n<=U-J_n. Since differences vanish at the
endpoints of every free interval, the Dirichlet evaluation kernel gives

    ||phi_p-phi_star||_infinity^2 <= (U-L)/2.               (4)

The factor1/2 is max interval_length/4; the middle interval has length2.
Thus an actual pulse plus a dual certificate bounds the distance to the UNIQUE
optimal phase, even though the pulse optimizer need not be unique. This
bound never certifies that the RELAXED phi_n itself has a pulse.

Using the unchanged rational K1940 pulse gives U=30/7 and its certified
amplitude472/2071<23/100. The report stores exact squared derivative and
uniform error bounds from(2), rechecking its continuum marginals and physical
2c Jacobian. These are rigorous but not claimed sharp.

Each fixed dual multiplier also gives a global affine lower bound in M with
slope -sum lambda_i C(A_i). This converts the certificate into an energy-budget
impossibility test at other amplitudes without reoptimizing or extrapolating
a sampled curve. The probe evaluates this identity at four exact budgets.

## 7. Verification, prior context and ceilings

The producer passes7118 exact checks, most from reusing the already stored
K1940 continuum primal certificate; this is explicitly not new pulse discovery.
The separate probe passes116 differential reconstruction, exact KKT,
dual-line and capacity-complement controls. Three mathematical faults (mean projection, negative
multiplier, actual pulse flow) and separate report/pin faults must fail AFTER
a green baseline. Universal convergence and no-gap scope rest on sections2--4,
not finite check counts. Internal review is not external expert or formal proof.

[Korman, McCann and Seis](https://arxiv.org/abs/1307.7774) give established
capacity-transport duality background. The argument here specializes the
already proved signed-cut criterion to the Dirichlet projection problem; no
novelty claim. No rate, finite full optimizer, smooth exact equality,
derivative-bandwidth control, phase-lift optimum or total-work optimum follows.

SC-OP-04 ASSERTS candidate grammar; SC-MAS-01/SC-CHI-02 ASSERT a stylized toy;
SC-META-53 remains UNCERTAIN. These do not supply this drive or its positive
pairing. LT-SM8, LT-GR6b, AC-F1, source register, physics ledger and canon stay
unchanged. Native full20 pairing/domain/accessibility remains construction
work. Both frontmatter scripts reproduce the exact consumer with Python3 and
SymPy; the inherited pulse verifier also imports NumPy/SciPy but runs no solver.
