---
title: "K1993: Optimal pulse has an unavoidable Sobolev corner"
status: active_research
doc_type: exploration
created: "2026-10-23"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no source identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k1993_pulse_sobolev_corner_obstruction.py
  - tests/channel-swings/k1993_pulse_sobolev_corner_obstruction_probe.py
---

# K1993: Optimal pulse has an unavoidable Sobolev corner

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
result: no locally H1 optimal pulse and an explicit finite-gradient phase-energy gap
carrier: actual optimal scalar phase on the width9 characteristic strip LAYER=toy CHIRALITY=N/A
pairing: Lebesgue marginal constraints and Euclidean pulse-gradient energy ON=characteristic_strip
real_structure: real bounded measurable or H1 pulses, as expressly stated
grading: forced angular sectors, not source chirality
action_owner: repository-construction -- fixed scalar transport problem
target: attainable regularity and quantitative approximation resources MAP-TYPE=intertwiner
```

## Result and scope

Every capped pulse realizing the ACTUAL optimal phase of
[K1974](k1974-scalar-excursion-separation-2026-10-23.md) fails H1 locally near
an interior tight-cut corner. Thus no pulse with square-integrable first
weak derivatives attains that optimum. This strengthens
[K1977](k1977-scalar-smooth-attainment-2026-10-23.md)'s C1 exclusion: the phase
itself is H1, so its derivative jump alone would not prove this result.

For a capped H1 pulse with exact zero column marginals and feasible phase,
let H be its gradient energy in the disk below and epsilon=J(phi)-J_star.
There is an explicit strictly positive necessary bound

    epsilon >= [pi^2 M^2 R^4/(32 Lmax^2)]
                 exp(-2-16H/(pi M^2)),
    M=23/100, R=1/4, Lmax=51/20.                         (1)

This is a resource-dependent gap, not a sharp optimum. It does not prove a
positive gap when H is unrestricted, nor construct smooth feasible approximants.
The explicit whole-wing transport and minimum pulse norm remain open.

## 1. The actual interior corner

Reuse K1969's exact algebraic t in(9/20,23/50), A=3-2t, and
[K1991](k1991-tight-cut-pulse-factorization-2026-10-23.md)'s forced regions.
Take the disk of radius R=1/4 centered at (u,z)=(-t,A), with local coordinates
X=u+t, Y=z-A. The disk is strictly inside D={-3<u<3,u<z<u+9}, and its rows
stay in the left or central bands. Saturation of the single cut u<-t forces

    v=+M on X<0,Y>0;    v=-M on X>0,Y<0.                (2)

These are opposite quadrants, each of angular width pi/2. The other two
quadrants are free for this local test. This uses the actual phase's tight
cut, not a test marginal or an assumed formula for the missing wing.

## 2. Exact logarithmic gradient divergence

Suppose v were H1 on the disk. On almost every circle of radius r its angular
slice is H1(S1), hence has an absolutely continuous representative. It is
constant on the two forced quadrants. On EACH remaining arc of length pi/2
it must change by2M. Cauchy--Schwarz therefore gives

    integral_circle |partial_theta v|^2 dtheta >=16M^2/pi.

The polar-coordinate energy on any annulus satisfies

    integral_{a<r<R} |grad v|^2 >= (16M^2/pi) log(R/a).   (3)

Let a decrease to0. The right side diverges, contradicting local H1. The
argument uses a.e. circle slicing on each annulus; it never assumes a value
or pointwise continuity at the center.

The coefficient in(3) is sharp for THIS LOCAL ANGULAR CONSTRAINT: choose the
constant values in(2) and interpolate linearly in angle on the other arcs,
independently of radius. Its angular gradient is4M/pi on total angle pi,
and its radial derivative is zero. Its W1p derivative integral is

    pi*(4M/pi)^p * R^(2-p)/(2-p),       1<=p<2.

This is a local representative satisfying forced geometry only, NOT a pulse
with the required full marginals. It proves the p=2 obstruction is intrinsic
to the corner test and that this test alone does not exclude W1p for p<2.
No global optimal-pulse regularity in those spaces is claimed.

## 3. A robust defect bound for approximate saturation

For any H1 pulse |v|<=M on this disk, define

    D = integral_Q+ (M-v) + integral_Q- (M+v),
    H = integral_disk |grad v|^2,
    D0 = pi M R^2/4.

All integrands in D are nonnegative. At radius r let d(r) be their angular
integral and let a(r),b(r) be the means over Q+,Q-. Then

    D=integral_0^R r d(r)dr,  a(r)-b(r)=2M-2d(r)/pi.

Call a radius good when d(r)<=pi M/2. At a good radius the two means differ
by at least M. Circle Poincare (constant1 for a 2pi-periodic circle) plus
Jensen on the two quarter-arcs gives

    integral |partial_theta v|^2 >= integral |v-mean(v)|^2
                                 >= pi M^2/4 = C.      (4)

For clarity, the second inequality follows by minimizing
(pi/2)[(a-c)^2+(b-c)^2] over c; its minimum is(pi/4)(a-b)^2.
The first follows directly from the Fourier expansion of a periodic H1
function: each nonconstant mode has squared frequency at least1.

For any inner radius rho, the logarithmic measure of bad radii in[rho,R]
is at most2D/(pi M rho^2). If0<D<D0, choose rho^2=4D/(pi M). Integrating(4)
on good radii yields

    H >= C [log(R/rho)-1/2],
    D >= D0 exp(-1-8H/(pi M^2)).                       (5)

If D>=D0 the second inequality is automatic. D=0 is excluded by section2.
Thus(5) holds for every capped H1 pulse on the disk, without imposing any
marginal equations. It is conservative, not sharp: the exact saturated
coefficient(3) is stronger than the coarse good-radius estimate(4).

### A matching logarithmic local construction

Multiply section2's angular minimizer psi(theta) by min(r/a,1), with0<a<R.
This is a capped Lipschitz function for each fixed a. Direct integration gives

    D=pi M a^2/6,
    H=(16M^2/pi) log(R/a) + (2pi/3+8/pi) M^2.

Indeed integral psi^2=4pi M^2/3, and the core radial and angular energies are
half that angular norm and half the angular derivative norm respectively.
Eliminating a gives H=(8M^2/pi)log(pi M R^2/(6D)) plus the displayed constant.
Thus the logarithmic order of the geometry-only resource obstruction is
achievable. Constants in(5) are not sharp. This local regularization need not
preserve either global marginal, so it is NOT an admissible near-optimal pulse
or proof that the unrestricted smooth infimum equals J_star.

## 4. Consume the defect in the actual phase problem

Now impose the original exact zero column marginals. The nonnegative slack
in the cut u<-t equals

    S = M C_cut - 2 integral_{-3}^{-t} phi
      = 2 integral_{-3}^{-t}(phi_star-phi).

For columns where the cut is the minority this slack is the integral of
M-v on that side; where it is the majority, zero column integral makes it
the integral of M+v on the complement. Hence the two quadrants used in D
are a subset of this slack and D<=S. This inequality requires exact zero
column marginals; an arbitrary approximate column residual needs another term.

For an admissible phase the established projection inequality gives
||phi-phi_star||_infinity<=sqrt(epsilon/2). With L=3-t<Lmax,

    D<=S<=sqrt(2)*Lmax*sqrt(epsilon).

Squaring(5) and dividing by2Lmax^2 proves(1). In particular a fixed finite
pulse-gradient budget H<=H0 gives a positive lower bound above J_star.
Approaching J_star with such pulses, if possible, requires unbounded gradient
energy. This is a necessary resource law, not existence or a convergence rate.

In physical coordinates tau=(z-u)/2,x=(z+u)/2, the Jacobian is2 and
|grad_{u,z}v|^2=(|V_tau|^2+|V_x|^2)/2. Thus H equals the physical
space-time gradient energy on the image ellipse. A global physical energy
bound can replace H in(1), giving a weaker but valid necessary bound.
Pulse-gradient energy is distinct from both the L2 pulse norm and phase
Dirichlet energy J; none is silently identified.

## 5. Verification and limitations

The producer checks324 rational geometry/constant controls. The separate
probe reconstructs angular energy, arc variance, inverted exponential bound,
phase-gap transfer and coordinate Jacobian symbolically, and checks the actual
corner geometry using both rational root endpoints. Its21 counted obligations
pass; four changed mathematical coefficients fail after a green baseline.
The continuum conclusions follow the proof, not the finite control count.

Strongest overclaim: treating a fixed-resource gap as an unrestricted smooth
infimum gap. Strongest contrary case: the explicit W1p angular example for
p<2, which has the forced signs but not the full marginals. Weakest remaining
seam: constructive constrained approximation at the fixed amplitude. No new
external theorem is borrowed beyond the elementary circle argument given here.
These are internal same-author checks, not external specialist acceptance or
proof-assistant certification. No novelty claim. SC-META-53 stays UNCERTAIN;
source, physics-ledger and canon remain unchanged.
