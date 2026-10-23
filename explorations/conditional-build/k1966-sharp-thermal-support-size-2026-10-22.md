---
title: "K1966: Exact thermal support and physical dimension frontier"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional independent mathematics; no GU identification, novelty or external certification
scripts:
  - tests/channel-swings/k1966_sharp_thermal_support_size.py
  - tests/channel-swings/k1966_sharp_thermal_support_size_probe.py
---

# K1966: Exact thermal support and physical dimension frontier

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
result: exact finite occupied-support and physical-dimension return frontier with sharp logarithmic resource coefficient
carrier: fixed extreme four-state quantum channel and four-level bath t=1/2, finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex conserving shell unitaries and pinched real energy populations
grading: additive energy shells; no source chirality
action_owner: repository-construction -- fixed conditional channel
target: minimum marginal return at finite spectral support and physical dimension MAP-TYPE=intertwiner
```

## 1. Exact finite resource frontier

Keep [K1935](k1935-arbitrary-support-thermal-return-2026-10-22.md)'s fixed
extreme four-state Schur channel, four-level bath energies0,1,2,3 at t=1/2,
independent input registers, exact additive conservation and arbitrary finite
nondegenerate nonnegative catalyst spectra. Return is worst-input catalyst
MARGINAL half trace distance. Let N count positive ENERGY populations after
pinching. This is occupied spectral support, not density-matrix rank: a pure
coherent state can occupy many energies.

Set q=2/3, p=1/9, W=25/8. For every integer N>=1, the sharp return among
protocols with at most N occupied energies is

    Z_N=max_(n+m=N-1) [W-2q^n-p^m/8],
    R_N=1/(2 Z_N).                                      (1)

It is attained by an actual finite conserving quantum protocol. Moreover,
physical catalyst dimension d permits any protocol only if d>=3, and its
sharp return is

    R_dimension(d)=R_floor((d-1)/2), d>=3.                (2)

Unlike a price or mean-energy bound, this is a COMPLETE finite resource
frontier in the stated model. It does not establish rooted completeness for
mean-energy optimization. Bath temperature, degeneracy, approximate target
channels, correlated inputs and product return are different problems.

## 2. Global reward reduction before any enumeration

K1933's pinching preserves the occupied energy set and gives an exact feasible
comparison with no larger return. K1935/K1943 reduce its support to disjoint
paths with gaps in{1,2,3}, successive gaps summing to at least4. Write Dp=u-v,
u,v>=0 disjoint, and A=D^-1>=0. For its population-consistent orientation,
R(p)=sum u/2. If every column reward w_j=sum_i A_ij is at most Z_N, then

    1=sum_j w_j(u_j-v_j)<=Z_N sum_j u_j,
    R_actual>=R(p)>=1/(2Z_N).                           (3)

The inherited outward-orientation domination bounds each column by the
reward of a root with outward left/right arms. At t=1/2 its step ratios are

    left:  q1=7/11, q2=2/3, q3=1/2,
    right: p1=7/29, p2=1/9, p3=1/23.

Every left ratio is at most q, so any n-edge left reward is at most
sum_(k=1)^n q^k. A right arm starting2 has maximum sum_(k=1)^m p^k:
after2 the next gap is2 or3, and a tail starting3 has total reward at most
G3=3/55<p. Even a single available gap2 contributes p, so replace a3 tail
by the same number of2 gaps to increase the reward. Iterating proves the
finite-length assertion, including the terminal case. A right arm beginning3
is dominated the same way. Replacement is root-compatible with an all2 left
arm. Missing right arms have zero reward.

Only a right arm beginning1 remains. If the left arm exists its first gap
must be3. The inherited Bellman bounds give left reward at most3/2 and right
reward at most14/55. Thus its entire reward is at most

    B=1+3/2+14/55=303/110=W-163/440.

With no left arm it is still smaller. The all2 allocation(n,m)=(5,1), N=7,
has reward692/243>B. Z_N increases with N, hence this special class cannot
win for ANY N>=7. Every root in every component with at most N vertices is
therefore bounded by Z_N. Disconnected components do not combine rewards;
(3) already treats all their positive and negative deficits together.

For N<=6 the finite first-gap recurrence is exact:

    L_k(d)=q_d[1+max_(e+d>=4) L_(k-1)(e)],
    H_k(d)=p_d[1+max_(e+d>=4) H_(k-1)(e)],

with continuation0 at k=1. Maximize1+L_n(a)+H_m(b) over n+m=N-1,
a+b>=4, including absent arms. Complete rational evaluation gives

|N|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|Maximum reward|1|5/3|19/9|65/27|211/81|665/243|
|n,m|0,0|1,0|2,0|3,0|4,0|5,0|

These equal (1). The independent probe enumerates every admissible gap word
and root through N=9 without importing this dynamic program. Thus the finite
base cases and analytic N>=7 proof together cover every N, not just a cutoff.

## 3. Physical attainment and minimal padding

For a maximizing n,m with N=n+m+1, choose occupied energies1,3,...,2N-1,
root index n, and unnormalized populations q^(n-i) for i<=n, p^(i-n) for i>n.
Their sum is Z_N. Incoming actual imbalances orient away from the root:
each nonroot equation Dp=0, and the root value is1/Z_N. K1943's complete
shell construction attains R=1/(2Z_N) for ALL system inputs while implementing
the entire complex target channel.

Only physical levels0,1,...,2N are needed, dimension2N+1. At the shared
shells, two occupied inputs have all four physical bath/catalyst positions
available; terminal singly occupied shells have at least two. The full shell
unitary constructor, including unused inputs and edge shells, verifies this
minimal padding for N=1,2,6,7,9,12. The construction applies to every N.

Conversely let a physical catalyst have d nondegenerate levels and N occupied
energies. On every total environment-energy shell, extremality requires
2r_E<=k_E, where r_E counts occupied inputs and k_E counts physical inputs.
Sum over all shells: sum r_E=4N and sum k_E=4d. At the unique lowest shell,
k_E=1; its occupied count must be0, so at least one inequality is STRICT.
Hence4d>8N and integrality gives

    d>=2N+1.                                            (4)

This argument allows arbitrary noncommensurate spectra, disconnected
components and coherent preparations through pinching. It does not assume
an equally spaced physical catalyst for the lower bound. Combining (1),(4)
and the actual padding construction proves (2). For even d, append one unused
level sufficiently far above the constructed ladder; its disjoint unoccupied
shells receive identity unitaries and do not affect the protocol. For d<3,
even N=1 violates (4). The physical dimension consequence is sharper than the
initial at-most-support question and needs no guessed rank-to-dimension map.

## 4. Exact optimizer and sharp resource scaling

The deficit at allocation n is

    D_N(n)=W-Z(n,N-1-n)=2 exp(-alpha n)
              +(1/8)exp[-beta(N-1-n)],
    alpha=log(3/2), beta=log9.

Its forward differences are strictly increasing. Thus the exact rational
optimizer can be found by a monotone sign search (with no ties),
without orientation or population enumeration. Equivalently, compare the
clipped floor and ceiling of

    n_c=[beta(N-1)+log(16 alpha/beta)]/(alpha+beta).

The forward difference is exactly p^m-q^(n+1). Equality would require
3^(-2m)=2^(n+1)3^(-n-1), impossible by prime factorization for n>=0.
Thus the integer optimizer is unique, including the boundary case. This
removes a tie case rather than selecting one numerically.

This real formula describes the minimizer; exact rational differences are
the certification method and avoid transcendental rounding. The optimum
satisfies n=beta N/(alpha+beta)+O(1), m=alpha N/(alpha+beta)+O(1).
Writing kappa=alpha beta/(alpha+beta), balancing the two positive
exponentials and rounding by at most1 proves

    R_N-4/25=Theta(exp(-kappa N)),
    N_min(delta)=(1/log(3/2)+1/log9)log(1/delta)+O(1),
    d_min(delta)=2N_min(delta)+1.

In particular the sharp physical-dimension logarithmic coefficient is
2/log(3/2)+2/log9. The last equality is exact whenever delta is feasible,
with N_min the smallest integer satisfying (1). Mean energy, physical
bandwidth, preparation work and repeated-use error remain different resources.
The unique integer allocation can modulate the bounded prefactor; no limiting
constant is asserted. The next joint question is the energy-return frontier
at this support/dimension constraint, not whether another support motif can
beat (1) at the same N and fixed bath.

## 5. Released joint-resource endpoint: energy at exact minimal return

For N>=7, equality in (1) also fixes the pinched occupied populations and
minimum initial mean energy. Let n,m be the unique optimizer. Then any
protocol with at most N occupied energies and return R_N has mean energy
at least

    E_N=1+2n+(2/Z_N)[sum_(k=1)^m k p^k-sum_(k=1)^n k q^k].  (5)

The minimal-padding construction attains this bound. This is a sharp
joint-resource ENDPOINT, not the whole intermediate energy-return curve.

To see necessity, equality in (3) requires v=0 and puts all positive u on
columns with reward Z_N. Strict increase of Z_N rules out disconnected
smaller components. Every occupied vertex must be reachable from that root;
an orientation missing a branch has fewer reachable vertices and hence
strictly smaller reward. A fully reachable path is outward. In section2 all
non2 left steps are strictly worse; a right3 tail is strictly worse; a
right1 root is strictly below Z_N for N>=7. Thus the support has all gaps2.
The unique maximizing root is n, so u is concentrated there and p=A u has
exactly the normalized geometric tails. Coherent inputs may retain coherence,
but their pinched populations and mean energy still obey this conclusion.

The lowest occupied energy is at least1: if it were in[0,1), its bath-ground
input would lie in a shell with only one possible physical input, contradicting
2r_E<=k_E. A translation of the canonical occupied progression therefore adds
a nonnegative energy offset to (5). Conversely the progression starting1 is
physically realizable and gives exactly (5). For physical dimension d with
N=floor((d-1)/2)>=7, the fixed-dimension minimum return is feasible under a
mean-energy budget E if and only if E>=E_N. Appending a remote unoccupied
level handles even d as before. A budget below E_N requires greater return;
its precise frontier is still open. This equality classification concerns
occupied populations and resonance geometry, not uniqueness of the whole
unitary, unoccupied spectrum or coherent state.

## 6. Verification and scope review

The producer checks340 exact obligations: finite Bellman maxima through N=40,
all integer allocation certificates through N=80, and the analytic special-gap
constants. The actual finite shell constructions pass2846 complex physical
controls across six minimal-padding examples. The separate probe checks11936
word/root, incoming-population and shell-rank obligations and rejects six
mathematical faults: wrong bath input, forbidden consecutive gaps, wrong
support allocation, missing half-trace factor, removed physical padding and altered mean energy.
Input-pin checks are separate. The universal proofs above carry the infinite
quantifiers; samples alone do not. No external expert or formal certification.

The strongest attempted overclaims were checked explicitly: support is not
state rank; padding is physical dimension; outward domination supplies a
lower bound only until a physical construction attains it; exact support
completeness does not solve the energy-constrained problem. K1935's finite
support transition at t=3/4 remains valid and lies outside t=1/2 here.
K1954's rejected energy secant is untouched.

[Ng et al.](https://arxiv.org/abs/1405.3039) give general dimension and
mean-energy constraints for thermal catalysis; the abstract was rechecked.
No novelty claim. SC-META-53 remains UNCERTAIN, and LT-SM8/LT-GR6b/AC-F1
remain NEEDS. These results use an imported finite quantum model and change
no GU source, physics-ledger or canon verdict.
