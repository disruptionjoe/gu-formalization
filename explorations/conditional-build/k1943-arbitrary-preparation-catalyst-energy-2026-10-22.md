---
title: "K1943: Arbitrary populations and mean-energy catalyst optimization"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: independent conditional mathematics; no native GU, novelty, external acceptance or formal proof
scripts:
  - tests/channel-swings/k1943_arbitrary_preparation_catalyst_energy.py
  - tests/channel-swings/k1943_arbitrary_preparation_catalyst_energy_probe.py
---

# K1943: Arbitrary populations and mean-energy catalyst optimization

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
result: sharp arbitrary energy-diagonal preparation marginal return, finite energy programs and a convergent global infimum hierarchy
carrier: four-state system, faithful four-level Gibbs bath, finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert trace and worst-input marginal half trace norm ON=independent_initial_registers
real_structure: complex adjoint with covariant initial energy pinching
grading: additive energy resonance components; no source chirality
action_owner: repository-construction -- full energy-conserving shell unitary
target: energy-constrained exact full-channel simulation MAP-TYPE=intertwiner
```

## 1. Question and fixed model

Retain precisely [K1939](k1939-physical-catalyst-resource-frontier-2026-10-22.md)'s
extreme four-state Schur channel, bath energies0,1,2,3 in units Delta,
Gibbs weights t^b/Z with0<t<1, and diagonal system Hamiltonian. All input
registers are independent; the target channel is exact on every matrix unit.
The catalyst is finite, nondegenerate, nonnegative with ground0. The resource
is its initial mean energy; return is the worst-system-input CATALYST
MARGINAL half trace distance. Product return, repeatability, locality,
approximate channels, degenerate spectra and GU physical identification are
separate questions.

K1939 solved at most two occupied energies; K1941 solved unconstrained return
at finite physical dimension. Neither solves an energy constraint with more
occupied populations. Here the unitary search is removed for ANY prescribed
admissible support and energy-diagonal preparation, and energy optimization becomes a finite
union of linear programs. Fractionally shifted disconnected components then
supply a convexified hierarchy converging to the unrestricted energy infimum.
The hierarchy has an explicit cutoff error; no finite global optimum or
optimal catalyst is asserted from one cutoff.

## 2. Sharp return for every admissible energy-diagonal preparation

Let the prescribed initial catalyst be sigma=sum_s p_s |s><s|, and let S
be its occupied energies. Physical shell completion
must satisfy k_e>=2n_e (K1935/K1941). In each congruence class modulo1,
occupied resonance components are paths: successive gaps d are1,2,3 with
adjacent gap sums at least4. Gaps at least4 disconnect. For an edge from
s to s+d put

    L_d=(1+t+...+t^(3-d))/Z, H_d=t^d L_d,
    x=H_d p_s, y=L_d p_(s+d).

Add (y-x)_+ to I_s and (x-y)_+ to I_(s+d), starting with I_s=0.
Then the sharp all-input return for this preparation, over physical shell
completions and conserving implementations, is

    R(p)=1/2 sum_s (p_s-I_s)_+.                         (1)

It is also attained on ANY supplied physical spectrum that completes these
shells. Different congruence components are separate; do not omit an edge
merely because a fractionally offset energy lies between its endpoints.

**Lower bound.** Use the system input rho12=(|1><1|+|2><2|)/2.
Extreme-Gram polarization gives orthogonal two-dimensional output spaces for
every occupied bath/catalyst input in each shell. Its environment output
spectrum is each initial shell input weight divided by2, twice. A singleton
occupied shell can return at most its input weight/2 to its occupied catalyst
position. A shared shell has two occupied output positions; each can receive
at most half the larger input weight. Summing bath labels bounds the returned
population at s by (p_s+I_s)/2. Measuring the catalyst in the energy basis
bounds trace distance below by the sum of positive population deficits,(1).
This applies to arbitrary implementing unitaries, not only controlled ones.

**Simultaneous attainment.** Reuse the actual full shell construction of
K1939: singleton input uses its own output position and one empty position;
in a shared shell the heavier input uses both occupied positions (own first),
and the lighter input uses both empty positions. Send the two-vector Wv_j
into each pair and complete orthogonal unused columns. W is the Hadamard
matrix and v_j are(1,0),(0,1),(1,1)/sqrt2,(1,i)/sqrt2. This is an energy-
conserving full unitary without a hidden pure ancilla, including incomplete
edge shells. Every occupied input realizes the same full complex Gram matrix.

At first-coordinate probability c=1/2 it saturates ALL population bounds,
so the return is(1). At c=1 the return is

    B=sum_edges min(x,y).

The physical system basis inputs have c=1/2,1/2,1,1/2; all system states
therefore give a convex combination in[1/2,1]. Off-diagonal system entries
vanish when forming the catalyst marginal. Moreover shared bath-label ranges
are disjoint at each occupied site, because adjacent gaps sum to at least4.
Consequently Q=sum_edges(x+y)<=sum_s p_s=1. Thus

    B=(Q-sum_edges|x-y|)/2
      <=(1-sum_edges|x-y|)/2
      <=1/2 sum_s(p_s-I_s)_+=R(p).

Trace-distance convexity proves all-input attainment. An external reference
on the system does not change its catalyst marginal. This inequality is the
new transfer needed beyond the earlier rooted-optimum special case.

For a prescribed coherent preparation with the same diagonal populations,
(1) is a lower bound by K1933 pinching, but equality is not established.
Pinching changes that state. The unrestricted mean-energy infimum in section5
does include coherent preparations: every coherent feasible protocol has a
diagonal feasible replacement with no greater return or energy, and the
diagonal constructions are themselves allowed. This is an optimization
reduction, not a fixed-state attainment theorem.

## 3. Fixed-support energy optimization is finite and exact

For each edge choose a sign specifying x>=y or y>=x. On that closed cell I
is linear. Introduce nonnegative z_s with z_s>=p_s-I_s, impose sum p=1 and
sum s p_s<=E, and minimize sum z_s/2. The orientation inequalities are part
of the program. Enumerate every orientation, including ties; an infeasible
cell needs a Farkas certificate, not an omitted floating failure. This finite
union gives the EXACT optimum on the chosen physical support (zero p are
allowed, so at-most support is intended).

For rational t,S,E, the producer stores rational primal and dual certificates
or rational Farkas witnesses for every cell. Floating HiGHS only discovers
these numbers; acceptance checks every inequality and exact primal-dual
equality. This is not a sampled optimization or an all-spectrum conclusion.

Examples at t=1/2 on S={1,3,5}:

| E | sharp return on this support | attaining weights |
|---|---|---|
|3/2|89/200|(41/50,11/100,7/100)|
|2|7/20|(1/2,1/2,0)|
|3|9/32|(3/8,9/16,1/16)|

At E=3/2,89/200<9/20, the best result with at most two occupied energies.
At E=3,9/32<3/10. Full complex shell matrices on actual finite ladders
verify these attainments. A FOUR-support example at E=4 gives9/40 with
weights(1/5,3/10,9/20,1/20) on1,3,5,7. These fixed-support answers are
not the unrestricted mean-energy frontier.

## 4. Disconnected fractional components matter at fixed energy

The unconstrained optimum can select one component (K1941); this shortcut
is invalid with an energy budget. Mixtures of low-energy/high-return and
higher-energy/lower-return components can beat either connected preparation
at the same mean energy. The components may be fractionally offset in a
nondegenerate spectrum, so they share no energy shells.

For an explicit example at t=1/2,E=3/2, take epsilon=1/100. Use a singleton
at energy1 with mass71/121 and a two-site component at1+epsilon,3+epsilon
with mass50/121 and internal weights2/5,3/5. The physical spectrum is
{0,1,2} union {epsilon,1+epsilon,2+epsilon,3+epsilon,4+epsilon}.
Its mean is exactly3/2, its return101/242<89/200, and each shell is a
full unitary. This is a genuine finite nondegenerate implementation, not
an extra classical flag outside the catalyst. It is a useful counterexample
to optimizing only a single connected support under mean energy.

## 5. Complete global hierarchy with a quantitative cutoff

A connected gap word has smallest possible occupied offset
 a=max(1,3-d_first), with a=1 for a singleton. Its lowest input needs a
lower empty energy by at least1; its first shared shell needs all four bath
positions. A full ladder from0 through its largest occupied energy+3 proves
sufficiency. Any component of any supplied spectrum can be translated down
to this canonical offset, decreasing its preparation energy without changing
return. Translation of a fixed supplied experiment is not a free operation;
this comparison is for optimization over spectra.

For integer K>=1 enumerate all canonical connected words whose largest
occupied energy is at most K and all their orientation cells. This is finite.
Take their convex hull in the (mean energy,return) plane. Equivalently use
one unnormalized p,z block per word/orientation, impose a SINGLE total
normalization and total energy budget, and minimize sum z/2. Denote this
rational LP value by F_K(E). The report stores exact primal-dual certificates
for selected small cutoffs. Each active block is a physically realizable
connected protocol. Zero blocks are harmless; no big-M or integer relaxation
is used.

Let R_star(E) be the infimum over all finite nondegenerate catalysts in this
model. For E>1,

    max(t^2/(1+t^2)^2, F_K(E)-2E/K) <= R_star(E) <= F_K(E),  (2)
    F_K(E) decreases to R_star(E) as K tends to infinity.

At E<1 implementation is impossible; at E=1 the only occupied energy is1,
so R_star(1)=1/2. The value at E>1 is an infimum, not promised attained.

**Upper bound and physical mixture limit.** Any finite LP mixture can be
implemented by translating its finitely many components by distinct positive
fractional offsets tending to0, adding an empty physical ground0. This
preserves each component's channel/return and prevents accidental shell
collisions. If the mixture uses all budget E, first mix an arbitrarily small
amount of the pure energy1 protocol to create strict energy slack; this is
possible for E>1. Choose offsets smaller than that slack. Actual admissible
protocols approach the LP return from above. This proves the infimum upper
bound without claiming that coincident degenerate copies are allowed.

**Lower bound.** Pinch a candidate preparation by K1933; energy and channel
exactness survive and return cannot increase. Discard occupied energies
strictly greater than K and normalize the rest. Their total mass delta is
at most E/K; for K>E the kept mass is positive and its normalized mean is
no greater than E. The SAME conserving unitary still implements the exact
extreme channel on the kept support. For every system input, contractivity
and the triangle inequality change its return by at most2delta (input
preparation and returned marginal each change by at most delta). Decompose
the retained support into resonance components and translate each to its
minimal canonical offset. Their energies are at most K and their sharp
returns cannot exceed the same-unitary return. They are feasible blocks of
the convexified cutoff program. Hence F_K(E)<=r+2E/K for every candidate r.
Taking the infimum proves(2); monotonicity and the upper bound give convergence.
For K<=E the lower estimate remains valid trivially whenever its right side
is nonpositive; otherwise use K>E for the stated truncation proof. The global
fixed-bath floor is reused from K1935.

Exact cutoff examples at t=1/2 are F_5(3/2)=81/200, F_5(2)=33/100,
F_5(3)=9/35 and F_7(3)=159/625. These are the finite convexified values,
not assertions of global equality. Physicalizing the first and last mixtures
with offsets1/1000 and2/1000, and mixing a small energy1 component to restore
the budget, gives actual finite returns4067/10034 at E=3/2 and191089/750578
at E=3. The latter is below0.255. Their5 and9 occupied energies live in21
and25 physical levels respectively; complete complex shells are verified.
The report retains the component weights, spectra, energy and all-input return.

This settles computability of the mean-energy infimum through certified finite
programs, not efficient complexity, finite attainment, a closed all-E formula,
or a practically sharp small-cutoff error. Rational t,E have fully rational
finite programs; other t are covered by the analytic characterization.

## 6. Energy-frontier consequences

The same argument sharpens the cutoff error without a new optimization.
Every occupied energy is at least1, so for K>E and K>1 the discarded mass
obeys delta<=(E-1)/(K-1). Consequently

    max(t^2/(1+t^2)^2, F_K(E)-2(E-1)/(K-1)) <= R_star(E) <= F_K(E).

For rational E,t and desired enclosure width epsilon, any integer
K>E with K>=1+2(E-1)/epsilon suffices. This is a computable accuracy
guarantee, not a claim that enumerating its programs is practical.

There is also a cutoff-free bound near the minimum energy:

    R_star(E) >= max(t^2/(1+t^2)^2, 3/2-E), E>=1.        (3)

To prove it, let delta be the total population at energies at least2.
The remaining occupied energies lie in[1,2), so none share a bath shell
with each other. Each high-energy site has at most one neighbor in that
interval, because a resonance gap is an integer. Its contribution to the
incoming excess at that low site is at most L_d p_high<=p_high.
The total incoming excess on all low sites is therefore at most delta.
Equation(1), restricted to those sites, gives R>=((1-delta)-delta)/2.
Since E>=1+delta, (3) follows. Pinching extends the bound to coherent
preparations. This is a necessary bound, not an optimal small-energy formula.
In particular a return budget r<1/2 requires E>=3/2-r.

The global value R_star is nonincreasing and convex in E. For convexity,
combine near-minimizers at two budgets as disconnected fractionally shifted
components; the strict-slack construction of section5 removes the arbitrarily
small offset cost whenever the combined budget exceeds1. The endpoint E=1
is handled by its exact singleton protocol. Taking the infimum proves the
convex inequality. It is finite on[1,infinity), continuous in the interior,
and (3) proves right continuity at1 with value1/2. Its limit as E tends to
infinity is the K1935 floor: that floor is a lower bound, and K1934's finite
protocols approach it with finite but growing mean energy. These conclusions
do not assert strict decrease, differentiability or finite attainment.

## 7. Verification and claim ceiling

The producer passes5182 exact controls; the separate probe passes530 exact
bath-label/planar-vertex/cutoff controls. The independent probe reconstructs shell output populations from bath labels
and tests arbitrary weights separately from the LP implementation. Exact
primal/dual/Farkas checks cover every enumerated orientation. Mathematical
faults affect normalization, preparation/energy, or dual coefficients and
must fail a genuine assertion after a green baseline; report/pin checks are
separate consistency controls. Universal claims depend on the proofs above,
not finite control counts. No independent expert or formal proof is claimed.

Strongest contrary route: disconnected fractional spectra really improve the
energy problem; section4 tests it rather than importing K1941's one-component
conclusion. Weakest seams are all-input attainment, minimal energy offsets,
nondegenerate physical mixing, and cutoff normalization; each has an explicit
argument and finite controls where applicable. Exact-channel extremality is
essential. Coherent catalysts are included only by the proved pinching
comparison; no physical dephasing resource is silently supplied.

[Ng et al.](https://arxiv.org/abs/1405.3039) already study dimension and
mean-energy restrictions in thermal catalysis using convex relaxations.
This target-specific characterization is not claimed novel. SC-META-53
remains UNCERTAIN; LT-SM8, LT-GR6b and AC-F1 remain NEEDS. No source,
physics-ledger, canon, physical repeatability or native GU result follows.
Reproduce the two frontmatter scripts; producer --write rediscovers and
stores the exact certificates.
