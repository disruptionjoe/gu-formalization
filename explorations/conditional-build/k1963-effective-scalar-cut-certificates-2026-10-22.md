---
title: "K1963: Effective finite certificates for all scalar cuts"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional scalar mathematics; no exact optimum, GU identification or novelty claim
scripts:
  - tests/channel-swings/k1963_effective_scalar_cut_certificates.py
  - tests/channel-swings/k1963_effective_scalar_cut_certificates_probe.py
---

# K1963: Effective finite certificates for all scalar cuts

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
result: finite-grid to all-measurable-cut transfer, explicit repair and energy convergence
carrier: supplied massless two-characteristic scalar control on a finite tube LAYER=toy CHIRALITY=N/A
pairing: Lebesgue marginals and Dirichlet energy ON=three_free_intervals
real_structure: real signed controls and real phase lifts
grading: characteristic direction only; no source chirality
action_owner: repository-construction -- prescribed scalar control
target: continuum amplitude and optimal phase-energy certificates MAP-TYPE=intertwiner
```

## 1. The finite certificate now has a quantitative continuum meaning

Keep exactly [K1942](k1942-complete-scalar-energy-duality-2026-10-22.md)'s
I=[-3,3], J=[-3,12], characteristic width9, physical c=1,
fixed +1/-1 plateaux, zero boundary trace, zero area and opposite phase0.
K1914's capacity is C(A)=integral min(a_A,ell-a_A), with
 a_A(z)=|A intersect[z-9,z]|. A physical amplitude M requires
|integral_A phi|<=M C(A)/2 for EVERY measurable A.

Let a finite partition of I have maximum cell length h. If an H1 phase phi
passes that inequality for every union of WHOLE cells at budget M and has
energy J_phi=integral|phi'|^2, it passes every measurable cut at budget

    M + epsilon(phi,h),
    epsilon(phi,h)=(2/3)[sqrt(h J_phi)+M h].              (1)

Thus finite cuts still do not certify the original amplitude. They certify
an explicit slightly larger amplitude. Unlike K1942's countable convergence,
(1) makes the transfer effective. The finite family must contain ALL unions,
not only half-lines or whatever cuts a solver happened to return.

## 2. Proof: averaging, transport, concavity

For arbitrary A let a(u) be its cellwise averaged indicator, and
s=min(|A|,6-|A|). In each cell couple the original A mass to the uniform
mass of density a inside the SAME cell. Every coupled point moves at most h.
The translated window indicators differ in z-integral by at most twice their
displacement. Integrate the coupling and use the triangle inequality:

    || integral_[z-9,z] (1_A-a)(u) du ||_(L1 dz) <=2h|A|.

Repeat with the complement to replace |A| by s. Since min(v,ell-v) is
1-Lipschitz in v, its fractional-density capacity satisfies

    |C(a)-C(A)|<=2hs.                                  (2)

No symmetric-difference approximation of arbitrary measurable sets is
assumed. That false shortcut fails for arbitrarily fine checkerboards.
Coupling controls window integrals instead.

Within a cell, H1 Cauchy-Schwarz gives oscillation at most
sqrt(h) ||phi'||_2. Coupling and then the complement give

    |integral_A phi-integral a phi|<=s sqrt(h J_phi).    (3)

For t in[0,1], A_t={a>t} is a union of whole cells. Layer cake and the finite
cut assumptions imply

    |integral a phi| <=(M/2) integral_0^1 C(A_t)dt
                       <=(M/2) C(a).                  (4)

The last inequality has this direction because min(v,ell-v) is concave.
It would be wrong to reverse it or identify the two capacities. Finally the
full rectangle I x[3,6] is in the tube, so C(A)>=3s. Combining(2)-(4) proves
(1), including null/full cuts by zero area. K1914 supplies a bounded measurable
pulse with these exact phase marginals. This is analytic existence, not a
serialized pulse or smooth attainment claim.

## 3. Repair at the original budget and effective energy optimization

Reuse K1944's exact strict witness, with

    M0=22451259/97656250 < M=23/100,
    U0=78227902689379/19531250000000,
    Delta=M-M0=19357/195312500.

Let phi_h minimize energy subject to every whole-cell cut and the fixed
plateaux/trace/area. The strict witness makes this finite relaxation nonempty.
By the finite representer/KKT argument in K1942 its minimum J_h is achieved,
4<=J_h<=J_star<=U0. Rational endpoints give rational capacities and projected
Gram coefficients, hence a finite exact active-set algorithm. This claims
finite decidability, NOT practical complexity: there can be 2^N unions.

Use epsilon_h=(2/3)[sqrt(h U0)+Mh] or a certified rational upper bound,
and theta_h=epsilon_h/(Delta+epsilon_h). Mix a pulse for phi_h at budget
M+epsilon_h with K1944's strict pulse in proportions 1-theta_h, theta_h.
The resulting chi_h preserves every required marginal and satisfies

    amplitude <=(1-theta_h)(M+epsilon_h)+theta_h M0=M,
    J_star <= energy(chi_h)
           <= U_h=(1-theta_h)J_h+theta_h U0.           (5)

Convexity of squared gradient norm proves the energy inequality. In particular

    0<=J_star-J_h<=theta_h(U0-J_h)<=theta_h(U0-4),
    U_h-J_h=O(sqrt(h)).                               (6)

Nested meshes give monotone lower bounds. This is an explicit convergence
modulus once a strict witness is known, not the unexplained limit of a mesh
search. Extra already-certified cuts can be added without changing the proof.
The feasible repaired phases and the relaxed projections both obey the
K1942 projection bounds; their squared derivative distance to the unique
optimal phase is at most U_h-J_h, and their squared uniform distance is at
most (U_h-J_h)/2. For the relaxed phase this uses projection onto its finite
convex set containing phi_star, not a false claim of pulse feasibility at M.
K1944 gives equality of smooth and measurable infima, not a smooth realization
of the generally nonsmooth chi_h.

## 4. Complete finite replay and a concrete upper improvement

At h=1/2 there are12 cells and4096 unions. The exact finite optimum is

    phi_h=phi0-(2/35)(g_(-1/2)+g_(1/2)), J_h=5601/1400,

where g denotes the zero-area Dirichlet representer from K1942. The producer
checks EVERY union and both inequality signs. The two active halfcuts have
nonnegative multipliers and exact contact; their KKT certificate proves
finite optimality, while all-union replay proves finite feasibility.
This lower bound is weaker than K1942's finest non-grid lower bound and does
not replace it.

Since sqrt(J_h/2)<=283/200, epsilon=51/50 is a rational allowance in(1).
The conservative but genuine repaired upper bound from(5) is

    J_star <=27930071724033303/6973333745000000 < U0.

The improvement is exactly
12052879476915121/27239584941406250000000 (about4.42e-7).
It is small; the substantial result is the universal transfer/modulus, not a
claim that this coarse computation solves the remaining optimality gap.
The upper is an existence certificate through K1914, not explicit new pulse
bytes. Together with K1942's stronger lower bound it tightens the existing
energy and phase-error enclosure. Arbitrarily small slack above this upper
admits smooth pulses by the unchanged strict-feasibility theorem.

## 5. Verification, hostile review and next use

The producer has4147 exact controls:4096 union inequalities, five exact graph certificates and fractional
capacity/layer-cake/central-rectangle controls. The separate probe reconstructs
the phase by solving the Dirichlet ODE piece by piece, integrates energy and
contact, computes same-cell transport moments and independently verifies64 quadrature identities:127 controls. Five actual
mathematical faults alter the multiplier, omit phase-averaging error, omit
transport error, underweight strict-pulse mixing and coarsen the capacity quadrature; all are rejected after a
green baseline. Input hashes are reporting checks separately. K1944's unchanged
large pulse certificate is reused, not counted as new verification.

Hostile review: finite halfcut-only tests are insufficient; all-grid unions
are essential. Capacity concavity, physical factor2 and complement bounds
are explicit. No unsupported convergence rate or exact optimizer is inferred
from samples. The universal result is the proof above, internally reviewed
without external specialist acceptance or formal certification.

[Korman, McCann and Seis](https://arxiv.org/abs/1307.7774) provide established
capacity-transport duality context; their abstract was rechecked. No novelty
claim. SC-OP-04 ASSERTS candidate operator grammar and SC-MAS-01 ASSERTS a
stylized local mass toy; neither supplies this drive. SC-META-53 remains
UNCERTAIN. LT-SM8/LT-GR6b/AC-F1 and source/physics/canon verdicts are unchanged.
The released exact grid-separation construction below removes exponential cut enumeration.
The remaining question is a matching continuum certificate or sharper transfer
modulus; neither follows from finite separation alone.

## 6. Released structural consumer: one exact graph replaces every grid union

The apparent exponential bottleneck in section3 can be removed for the fixed
long tube. Choose h=1/m, so all plateau, tube and endpoint knots align.
For z in[-3,3], only the right window endpoint moves inside I;
for z in[6,12], only the left endpoint moves. On each h-cell,
a_A and ell have integer multiples of h at endpoints, and 2a_A-ell has
slope +1 or -1. Thus its zeros lie at grid endpoints. On[3,6] both functions
are constant. Consequently min(a_A,ell-a_A) is affine between consecutive
z-grid points for EVERY union A of u-cells. Composite trapezoidal integration
on that grid is exact simultaneously for all unions.

Make one row vertex for each u-cell and one auxiliary vertex for each z-grid
point. Let l_ij be the overlap length of cell i with[z_j-9,z_j], w_j its
trapezoidal weight (h internally and h/2 at the endpoints), and b_i the exact
phase integral over row i. Connect row i and auxiliary j in both directions
with capacity (M/2)w_j l_ij. Add source-to-row capacity b_i when b_i>0,
and row-to-sink capacity -b_i when b_i<0. All capacities are nonnegative.
For a fixed source-side row set A, optimizing each auxiliary side gives

    cut_capacity - sum_i max(b_i,0)
       = (M/2) C(A) - integral_A phi.

Therefore one minimum cut separates ALL grid-union constraints. The empty
and full cuts have zero adjusted cost; a negative minimum exhibits an actual
violated cut. Complement symmetry and zero area supply the other sign.
The graph has O(N) vertices and O(N^2) arcs for N=6m, replacing2^N subsets.
This is an exact finite-grid separation algorithm, not a continuum mincut or
an implemented general QP optimizer. Rational capacities scale to integers;
a feasible integer flow and equal-capacity cut certify the global minimum.

The code uses exact integer Dinic augmentation and checks every capacity,
vertex conservation and flow/cut equality. It certifies candidates on grids
h=1,1/2,1/4,1/16. At h=1/16 the exact two-contact phase with s=7/16
has J=1850592923/462545000 and passes all2^96 unions using339 vertices
and27744 directed arcs. The h=1/2 graph agrees with exhaustive4096-union
verification; the unperturbed phi0 instead returns the actual violated cut
[-3,-1/2] with adjusted capacity -1/160.

Independent quadrature tests initially showed that removing midpoints was
NEUTRAL. That was not counted as a detected fault: in this long-tube geometry
original grid points already contain every kink. The final graph uses this
stronger reduction; actual coarsening that skips required grid points is
rejected. For a shorter tube where both window endpoints move inside I, the
slope argument changes and this grid rule must be re-proved. No such transfer
is claimed. The next numerical method can use exact graph separation and the
proved continuum error bound together, rather than rely on halfcuts alone.
