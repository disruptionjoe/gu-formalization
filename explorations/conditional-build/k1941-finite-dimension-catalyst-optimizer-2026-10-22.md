---
title: "K1941: Sharp finite physical-dimension catalytic return"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: independent conditional mathematics; no native GU, novelty, external acceptance or formal proof
scripts:
  - tests/channel-swings/k1941_finite_dimension_catalyst_optimizer.py
  - tests/channel-swings/k1941_finite_dimension_catalyst_optimizer_probe.py
---

# K1941: Sharp finite physical-dimension catalytic return

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
result: minimum physical shell completion and exact arbitrary finite dimension return optimizer
carrier: four-state system, faithful four-level Gibbs bath and finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace and worst-input marginal half trace distance ON=independent_initial_registers
real_structure: complex adjoint and initial energy pinching comparison
grading: additive energy resonance shells; no particle chirality
action_owner: repository-construction -- exact conserving joint unitary
target: physical dimension constrained full-channel simulation MAP-TYPE=intertwiner
```

## 1. The remaining dimension problem is finite and exact

Fix precisely [K1935](k1935-arbitrary-support-thermal-return-2026-10-22.md)'s
extreme four-state Schur channel, bath energies0,1,2,3 in units Delta and
weights t^b/Z, 0<t<1. The catalyst spectrum is finite and nondegenerate,
with ground0; its preparation and conserving unitary are unrestricted.
Registers start independently. Return means the worst-input CATALYST MARGINAL
half trace distance, not joint product return or repeatability.

[K1939](k1939-physical-catalyst-resource-frontier-2026-10-22.md) distinguished
occupied support N from full physical dimension D and settled D<=6. Here a
minimum empty-state completion algorithm and the fixed-support theorem close
the arbitrary finite-D question as an EXACT FINITE OPTIMIZATION. No real-energy
search, unitary search or floating relaxation remains. This is not a closed
formula uniform in D or an efficient large-D algorithm.

For every admissible gap word g=(d1,...,d_(N-1)), d_i in{1,2,3},
d_i+d_(i+1)>=4, let S_g={0,d1,d1+d2,...} and let c(g) be the minimum
physical dimension returned in section2. With the L_d,H_d,q_d,p_d of K1937,
let S(g,r) be its rooted prefix reward. Then

    r_D(t) = min_{N<=floor((D-1)/2), g, r : c(g)<=D} 1/[2 S(g,r)].  (1)

D<3 is infeasible. Every candidate in(1) has an actual full energy-conserving
unitary, including the incomplete edge shells. Extra EMPTY far-separated
levels pad a witness to exactly D. Initial coherent preparations cannot beat
this optimum: the K1933 covariant pinching comparison preserves dimension and
channel exactness while contracting the return error. This is a comparison
of preparations, not a free physical dephasing operation.

## 2. Minimum completion by a chronological greedy cover

Given an occupied set S in a single energy-lattice component, define n_e as
the number of s in S with e-s in{0,1,2,3}. Empty catalyst levels a contribute
to the four consecutive shells a,a+1,a+2,a+3. Exact implementation is possible
if and only if

    k_e >= 2 n_e  for every occupied-input shell e.            (2)

Necessity is K1935 extreme-Gram rank doubling. Sufficiency follows by putting
an orthogonal copy of the two-vector v_j into the shell for each occupied
input and completing the remaining columns to a full unitary. The target is
implemented on every matrix unit, including its complex phase. Thus one must
add at least n_e EMPTY positions from {e-3,e-2,e-1,e}, in addition to S.
No empty energy outside the finite set (S+{0,1,2,3})-{0,1,2,3} helps.

Algorithm: visit occupied-input shells e in increasing order. Count the
already chosen empty levels in[e-3,e]. If the count is below n_e, add the
largest still-available empty levels in that interval until the deficit is
filled. If there are too few, the support cannot be completed. Count S plus
the chosen empty levels; translate the whole construction so its minimum is0.
Translation changes neither shell multiplicity nor return. It DOES change
absolute preparation energy, so this is not a mean-energy optimizer.

**Exchange proof.** Maintain a minimum completion containing all greedy
choices so far. At the next deficit an optimal extension contains enough
unselected candidates covering e. Replace smaller such candidates by the
larger greedy candidates. Earlier shell requirements are already met by the
fixed greedy prefix, so they cannot be damaged. For any future e'>=e,
if a replaced level a covered e', its larger replacement b<=e also covers e':
b<=e<=e' and e'<=a+3<=b+3. Cardinality is unchanged. Repeat each required
replacement. This inductively constructs a minimum completion containing the
entire greedy set. A shortage cannot be cured by a level outside[e-3,e].

This argument includes unused positions inside a support span; it does not
silently fill an entire ladder. With arbitrary real spectra, treat each
congruence class modulo Delta separately. For a prescribed absolute spectrum
with forbidden negative levels, remove those candidates before the greedy
step; the same proof applies, but translating the given spectrum would then
be a different physical problem.

## 3. Why the finite optimizer is global

K1935 proves that occupied resonance components are paths with the stated
allowed gaps: gaps>=4 disconnect, while three occupied levels in one shell
are impossible. For any fixed component, K1937's orientation/visit lower
certificate bounds return by its best rooted reward; the global lower bound
uses the largest component reward, not a sum across disconnected components.

Any component present in a physical D-level implementation is completable
with at most those D levels. Even a level occupied in a different component
can be treated as empty when constructing the comparison realization. Hence
that component's c(g)<=D, and its best rooted rate is among(1). No collection
of disconnected or nonintegrally offset components evades the lower bound.
K1939's shell-slack count gives N< D/2 for each feasible component, which makes
the search finite. It is legitimate to optimize one connected component;
this is not an assumption that every supplied spectrum was connected.

For attainment use the K1937 rooted weights on the greedy completion.
In a shared shell there are two occupied positions, so(2) forces all four
positions: send the heavier input's Wv_j to the two occupied positions and
the lighter input's Wv_j to the two empty positions. In a singleton shell
there is at least one empty position; use its own position and that empty
position. Complete unused columns. Here W is the real Hadamard matrix and
v1=(1,0),v2=(0,1),v3=(1,1)/sqrt2,v4=(1,i)/sqrt2.

K1937's ALL-input argument uses only these two types of shell, not padded
positions elsewhere. With c in[1/2,1], its return remains
(1-c)s_root+(2c-1)B, with B<=s_root/2 by the disjoint bath-label inequality.
Thus the worst return is s_root/2=1/(2S), reached at c=1/2. Incomplete
edge-shell completion leaves this calculation intact. This is the crucial
transfer from a fixed-support lower bound to a physically attainable D-budget.

## 4. Exact resource decisions and limitations

The report enumerates the finite optimum at t=1/2,3/4,9/10 for D3 through11,
including the actual spectra, roots and preparations. Examples:

| t | D | minimum return | occupied levels |
|---|---|---|---|
| 1/2 | 7 or8 | 9/38 | 1,3,5 |
| 1/2 | 9 | 27/130 | 1,3,5,7 |
| 3/4 | 7 or8 | 289/978 | 1,3,5 |
| 3/4 | 9 | 11849/45300 | 1,3,5,7 |

For t=1/2,D7 the preparation is(4,6,9)/19 on the seven-level ladder0..6.
The D9 preparation is(8,12,18,27)/65. At warm t=3/4,D6 the inherited
adjacent-support improvement143/434 remains; the new algorithm reproduces
it without assuming that all optimal words are consecutive-odd. The displayed
odd words at D7--9 are finite exact conclusions, not a theorem about all D,t.
The finite word enumeration is exponential in D; only the completion of a
specified word is greedy. Rational t gives rational arithmetic throughout.

The new algorithm enables exact inversion of any attainable return budget by
increasing D. K1935's strict global infimum t^2/(1+t^2)^2 remains unchanged;
a budget at or below it has no finite solution. Above it, the K1937 odd-path
construction guarantees eventual termination. This dimension inversion does
not determine optimal mean energy, degenerate spectra, approximate-channel
resources, locality, product return or reusable operation.

## 5. Verification and source boundary

The producer performs4269 exact controls, including full complex shell
unitaries on minimal physical spectra and all-input returns. The separate
probe performs97 controls using exhaustive subset covers and every edge
orientation's inverse matrix; it independently checks small-D global optima.
Finite controls challenge the proof; they do not replace its universal scope.
Three actual mathematical-input faults (wrong greedy endpoint, complex phase,
return normalization) and separate report/pin faults fail after green baselines.

Strongest overclaim rejected: a mean-energy optimum or a polynomial-time
arbitrary-D algorithm. Strongest contrary route—disconnected fractional
spectra—is included in the lower-bound argument. Weakest seam is extending
padded-shell attainment to a minimum completion; it is proved above and
reconstructed on the actual full matrices. Internal verification is not an
independent expert review or Lean proof.

[Ng et al.](https://arxiv.org/abs/1405.3039) establish catalyst resource
restrictions as prior context; no novelty claim is made. SC-META-53 remains
UNCERTAIN. LT-SM8, LT-GR6b and AC-F1 remain NEEDS: this supplied positive
finite Hilbert model supplies no native GU state, pairing, domain or observable.
Source register, physics ledger and canon are unchanged. Reproduce with both
frontmatter scripts (Python/SymPy); producer --write regenerates the report.
