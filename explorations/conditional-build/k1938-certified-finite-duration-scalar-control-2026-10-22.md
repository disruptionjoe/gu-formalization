---
title: "K1938: Certified finite-duration scalar pulse budgets"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: independent conditional mathematics; no native GU, novelty, external acceptance or formal proof
scripts:
  - tests/channel-swings/k1938_certified_finite_duration_scalar_control.py
  - tests/channel-swings/k1938_certified_finite_duration_scalar_control_probe.py
---

# K1938: Certified finite-duration scalar pulse budgets

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
result: continuum lower and upper pulse bounds from finite rational certificates and exact endpoint correction
carrier: supplied one-dimensional massless two-characteristic system LAYER=toy CHIRALITY=N/A
pairing: real Lebesgue marginal duality ON=finite_moving_tube
real_structure: real phase lift and real signed bounded pulse
grading: propagation directions only; no source chirality
action_owner: repository-construction -- common scalar spacetime potential
target: exact right phase phi with identically zero left phase MAP-TYPE=intertwiner
```

## 1. Finite duration now has rigorous decisions

[K1914](k1914-scalar-control-transport-cuts-2026-10-21.md) proves the exact
all-set criterion; [K1915](k1915-scalar-pulse-duration-limits-2026-10-21.md)
proves sharp limiting constants. Here finite rational matrices give actual
CONTINUUM upper and lower bounds, with a proof of convergence. Floating-point
linear programming only discovers candidate certificates; exact arithmetic
verifies both marginals, capacity, geometry, duality and endpoint correction.

For c=1,L=3, fix the odd continuous profile

    phi(u)=-min(u,1,3-u), 0<=u<=3,   phi(-u)=-phi(u).         (1)

Its plateau magnitude is1 on[1,2], contrast2, half-area2 and gradient
energy integral|phi'|^2=4. This is a fixed H1 profile, not smooth. For
T=9/2 the certified conclusion is

    1519/6579 <= M_star <= 3571033/14452992 < 1/4.            (2)

Thus budget23/100 is impossible, while budget1/4 admits an explicit
bounded measurable pulse with EXACT endpoints(phi,0). Both elementary
K1915 lower bounds give only2/9 here and would permit23/100. The previous
constructive upper bracket was greater than0.64. Equation(2) does not claim
an exact finite-T optimum or smooth realization of the nonsmooth profile.

## 2. Finite certificates with correct continuum meaning

Use characteristic coordinates u=x-ct,z=x+ct, d=2cT,
E={(u,z):u in[-L,L],0<=z-u<=d}, and w=V/(2c).
Partition I and J=[-L,L+d] into intervals I_i,J_j of length h. Write
b_i=integral_(I_i) phi and a_ij=area(E intersect(I_i x J_j)).

The OUTER linear program minimizes m subject to

    sum_j x_ij=b_i, sum_i x_ij=0, |x_ij|<=m a_ij.            (3)

Every continuum pulse gives a feasible matrix by integration, so its
optimum is a lower bound for M_star/(2c). For ANY rational potentials
f_i,g_j with positive denominator,

    m >= [sum_i f_i b_i]/[sum_ij a_ij |f_i+g_j|].            (4)

This is directly the continuum dual tested on cellwise constant potentials;
it does not assume cellwise constant continuum marginals. Rationalizing
potentials preserves validity even when they cease to be LP-optimal.

The INNER program keeps only rectangles wholly contained in E, with
capacity h^2. A feasible rational matrix becomes the actual pulse
w=x_ij/h^2 on each kept rectangle, zero elsewhere. It satisfies zero column
marginal pointwise and row marginal bar_phi=b_i/h pointwise in each cell.
That is not yet the requested phi. Section3 supplies the exact missing
correction. Merely integrating a partial outer cell would not give this
pointwise row or column statement; outer solutions are never used as primal
pulses.

The program discovers primal flows with SciPy HiGHS, rationalizes them and
repairs any rounding residual on a spanning forest of the inner bipartite
graph. Leaf elimination transfers the exact remaining vertex imbalance to
its parent; root compatibility is checked. It then recalculates the actual
maximum|x_ij|/h^2. No floating residual tolerance enters acceptance.
The JSON contains every flow and every dual potential, enabling replay
without trusting the optimizer. A solver failure supplies no certificate.

## 3. Exact residual pulse and numerical consumer

Let r=phi-bar_phi and F_r(u)=integral_(-L)^u r. It has zero integral on
EVERY cell. Put f=-F_r/(2c), and take the triangular time density g with
integral1 on[0,T], height2/T and slopes+/-4/T^2. The correction is

    V_r(t,x)=g'(t) f(x-ct)+g(t) r(x-ct).                     (5)

Along right characteristics it integrates to r. Along left characteristics
it is the time derivative of g(t)f(z-2ct), so its integral is exactly0.
The identity holds almost everywhere for this Lipschitz primitive and
piecewise smooth g; isolated corners do not affect the phases.
Thus the inner matrix plus(5) gives exact(phi,0), with

    M_star <= 2c m_inner + 2||F_r||/(c T^2)+2||r||/T.         (6)

For(1), take h=1/n so cells align with all breakpoints. On a ramp,
r has slope+/-1 and zero mean; hence ||r||=h/2 and
||F_r||=h^2/8. On a plateau both vanish. The correction is exactly bounded
by h^2/(4cT^2)+h/T. At T=9/2,h=1/16, the rational certificate gives the
upper fraction in(2); its two marginals and amplitude are independently
checked by polygon clipping and direct summation.

The supplied certificate bank also gives the following bounds. Where the
older analytic construction is tighter, it is retained rather than replaced:

| T | certified lower | valid upper | upper evidence |
|---|---:|---:|---|
| 1/2 | 16 | 20 | K1915 analytic pulse |
| 1 | 4 | 8423/1792 | h=1/8 matrix plus correction |
| 3/2 | 16/9 | 12827/6336 | h=1/8 matrix plus correction |
| 3 | 4/9 | 26807/52992 | h=1/8 matrix plus correction |
| 9/2 | 1519/6579 | 3571033/14452992 | shifted cut; h=1/16 pulse |

These are fixed-profile peak-amplitude costs, not optimized phase-energy,
2pi-lift, noise-law, temporal bandwidth, total-work or source-native costs.
A smooth pulse has smooth marginal, so exact smooth attainment of(1) is
impossible. Mollification after interior contraction yields smooth nearby
profiles and nearby budgets, not exact preservation of this nonsmooth target.

## 4. A new cut that the elementary duration tests miss

For d>=2L and A=[-L,s] with -L<=s<=0, set a=L+s. Direct integration
of the smaller crossing length gives C(A)=a(d-a): the growing and shrinking
edge triangles plus the common rectangle have precisely this area.
For(1), when -1<=s<=0, integral_A phi=2-s^2/2. Hence at d=9,

    M_star >= (4-s^2)/[(3+s)(6-s)].                         (7)

Choose s=-9/20 to obtain1519/6579>23/100>2/9, proving the rejected budget
in section1. Differentiating this one-parameter lower bound gives the
maximizing half-line s=(-14+4sqrt10)/3. This is not proof that half-lines
exhaust ALL measurable cuts; even an exactly optimized cut family remains
only a lower bound until a matching primal pulse or full dual theorem is
provided. The explicit rational s already settles the stated budget.

## 5. Why refinement converges, not just why one mesh is safe

Assume a fixed Lipschitz phi on I, zero at its endpoints and with integral0.
Use nested interval partitions whose maximum cell width tends to0; allow
partial boundary cells, use their actual widths and retain exact cell
integrals. The implementation specializes to commensurate uniform grids. The outer optimum is nondecreasing on nested refinements,
since fine matrices aggregate into feasible coarse matrices. It is bounded
above by the continuum optimum. For any sequence of outer solutions with
bounded m, realize w_h=x_ij/a_ij on the actual cut cells. These functions
have uniformly bounded amplitude and exactly the required integrated cell
marginals. Weak-star compactness supplies a subsequential limit on finite E.
For continuous test functions of u or z, replacing the test by cellwise
constants has error tending to0 by uniform continuity. Thus the limit has
EXACT marginals(phi,0). The outer optimal values therefore converge to the
continuum optimum. No assertion is made that each outer realization has
pointwise correct marginals.

For the inner upper convergence, begin with a bounded continuum minimizer.
Contract about the tube center using u'=alpha u,
z'=alpha z+(1-alpha)d/2 as in K1914. This creates positive diagonal-boundary
clearance, preserves amplitude and zero column marginal, and produces
phi_alpha(u)=alpha phi(u/alpha), extended by0. Since the zero extension
of phi is Lipschitz, ||phi-phi_alpha||_infinity tends to0 as alpha tends to1.
Correct this residual with a fixed smooth temporal density compact in(0,T)
using(5). Its amplitude tends to0 and it also has positive diagonal
clearance. The u-boundaries need no interior margin: the grid partitions I
exactly. For sufficiently fine grids, every rectangle meeting this pulse's
support is wholly inside E. Averaging that pulse on full rectangles gives
exact cell demands b_i and zero column sums, without increasing amplitude.
Thus limsup m_inner is no greater than the true optimum in w units.

Finally the remaining r=phi-bar_phi obeys ||r||<=Lip(phi) h/2, while
its cellwise primitive is bounded by h||r||; (6)'s correction tends to0.
The lower and corrected upper certificates therefore converge to M_star.
This proves eventual decision for any budget strictly above or below the
threshold. No finite grid is promised to decide equality and no uniform
convergence rate is claimed. For smooth compact phi, K1914 also identifies
the same threshold with smooth exact-endpoint infimum, with strict amplitude
slack; that theorem does not convert(1) into a smooth marginal.

## 6. Hostile review and reproducibility

Strongest hidden assumption rejected: aggregated outer cell marginals do
NOT identify continuum marginals on that mesh. The primal uses only full
rectangles and adds an explicit correction. Strongest contrary case: the
shifted cut rejects a budget that passes both elementary duration tests.
Weakest seams are geometry, Jacobian2c, zero-column exactness, and the
residual primitive. Independent rational polygon clipping checks the area
formula; every primal row/column is reconstructed and the correction is
integrated analytically. Planted flow, Jacobian, residual and capacity faults
fail actual mathematical checks after a green baseline. Report/pin controls
are separate consistency evidence.

Run both scripts with Python3, SciPy1.18.0 and NumPy as installed; producer
--write regenerates JSON. Rational certificate verification determines
acceptance; floating optimization is discovery only. Universal convergence
rests on section5, not sampled meshes. Internal hostile reasoning and
independently written code are not external expert review or formal proof.

Capacity-constrained transport and duality are established background:
[Korman/McCann/Seis](https://arxiv.org/abs/1307.7774) and
[their elementary duality proof](https://arxiv.org/abs/1309.3022).
The signed pulse specialization is not claimed novel. SC-OP-04 ASSERTS
candidate grammar, SC-MAS-01/SC-CHI-02 ASSERT a stylized toy, and
SC-META-53 remains UNCERTAIN. None selects this scalar drive or positive
physical interface. LT-SM8/LT-GR6b/AC-F1, source, ledger and canon remain
unchanged; full20/K-C/domain/accessibility remains an independent construction.
