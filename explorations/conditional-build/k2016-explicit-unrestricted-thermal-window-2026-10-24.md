---
title: "K2016: A uniform explicit unrestricted ten-level window"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional internal mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2016_explicit_unrestricted_thermal_window.py
  - tests/channel-swings/k2016_explicit_unrestricted_thermal_window_probe.py
---

# K2016: A uniform explicit unrestricted ten-level window

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
result: explicit all-dimension spacing regime, ten-level necessity and quantitative tail/bath consumers
carrier: exact extreme four-state channel and nondegenerate finite or countable positive-spacing catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input catalyst marginal half trace distance with upper mean-energy budget ON=independent_initial_registers
real_structure: complex conserving shell unitaries and real diagonal populations
grading: bath resonance components, not source chirality
action_owner: repository-construction -- unchanged K2008 thermal class
target: explicit global spacing window and resource stability MAP-TYPE=intertwiner
```

## 1. Evaluated theorem

Keep the finite-or-countable positive-spacing thermal class of K2008, at
t=1/2. Write r=E-6/5, B(E)=63/100-3E/20. For EVERY

    0 < delta <= 1/15,        6/5 < E < 11/5,

including the spacing endpoint and arbitrarily near either energy endpoint,

    F_infty(delta,E)
      = G(delta,E)
      = B(E)+(3/20)delta min(r/(1+delta),(1-r)/(1-delta)). (1)

An actual ten-level catalyst attains (1). For the strict spacing interval
0<delta<3/380, fewer than ten physical levels cannot attain it. No
minimal-dimension claim is made here for 3/380<=delta<=1/15.
Every optimizer throughout the closed spacing interval has zero diagonal
population above energy nine. The theorem also covers coherent initial
preparations via the inherited pinching reduction, not by identifying all
coherent minimizers.

K2014 proved this curve only on an unevaluated, budget-dependent neighborhood
of zero. Here one explicit neighborhood works uniformly on the ENTIRE open
energy interval. The bound 1/15 is sufficient, NOT claimed to be the largest
valid spacing. No complete 25-level spectrum enumeration, full-spacing
frontier, arbitrary bath optimum or GU physical realization is asserted.

## 2. Quantitative low-support theorem

First consider any finite physical protocol whose occupied energies are at
most nine, with arbitrary dimension and nonnegative component offsets.
[K2015](k2015-finite-thermal-ray-separation-2026-10-24.md) supplies complete
return-cone rays and two directional certificates. Fix the protocol's
physical spectrum, its orientation/deficit cones, and optimize the lifted
ray weights. An optimum uses at most two rays and has no larger return or
energy. It remains in the same physical spectrum and sign cones.

If the chosen pair omits B, its return is at least
B(E)+c_A r, with c_A=81/12940. If it omits A, it is at least
B(E)+c_B(1-r), with c_B=9/7540. This includes every pair except A/B.
But the two feasible ten-level orientations give

    G-B <= (3/20)delta r/(1+delta),
    G-B <= (3/20)delta(1-r)/(1-delta).

The corresponding coefficient inequalities hold whenever

    delta <= c_A/(3/20-c_A) = 27/620,
    delta <= c_B/(3/20+c_B) = 3/380.                    (2)

Thus every non-A/B pair has return at least G throughout delta<=3/380.
These are exact affine numerator certificates on a whole interval, not
sampled comparisons. For strict delta<3/380 both relevant inequalities are
strict at every interior E, excluding all non-A/B optimal vertices.

For an A/B pair, K2015 proves it cannot be in one component cone. Let its
actual canonical offsets be x_A,x_B>=0. Their difference is at least delta,
because the two occupied levels 1+x_A and 1+x_B are distinct physical levels.
Moving the lower offset to zero and the higher to delta weakly lowers both
energies. Replacing completion by the two five-level ladders at those offsets
is physically feasible for delta<=1/2 and leaves return unchanged.
Optimizing the B weight gives precisely G. Consequently the original
low-support protocol also has return at least G.

K2015 section 4 then retains actual same-cone compatibility and paid component
offsets. Its complete affine interval certificate extends this low-support
theorem to delta<=4/15. The unrestricted proof below consumes only delta<=1/15.
The stronger low-support certificate does not assert that every optimal
vertex outside the original strict interval must be A/B.

The upper witness uses spectrum {0,...,4} union {delta,...,4+delta}. If B is
shifted, w_B=r/(1+delta); if A is shifted, w_B=(r-delta)/(1-delta).
Choose B-shift when r<=(1+delta)/2 and A-shift otherwise. The winning A-shift
weight is always nonnegative: its selection implies r>delta. Therefore no
extra assumption delta<r is necessary near the lower budget endpoint.
Both winning weights are strictly between zero and one for interior E.

## 3. Removing the high-energy tail without an unknown threshold

Now take ANY finite or countable protocol with R<=G at budget E. Pinch and
use the inherited sharp shell implementation. Let q be its diagonal
population above nine. K2013 gives

    R-B(E) >= (11/50)q,
    E' = (E-9q)/(1-q),
    R_low <= R+q/(1-q),      mean_low<=E'.              (3)

Retain all physical completion levels through twelve, not only occupied
levels through nine. This is a genuine finite protocol at the same spacing,
since a positive-spacing spectrum has finitely many levels below twelve.
No two-component reweighting or 25-level reduction is needed before applying
section 2. Canonicalization only lowers occupied energies.

Using the B-shift upper bound even when the other orientation wins gives

    q <= (15/22)delta r/(1+delta).

The retained budget remains strictly above 6/5 for ALL r in (0,1). Indeed,
E'>6/5 is equivalent to q<5r/39, and the preceding bound implies this whenever

    delta < 22/95.

This cancels the apparently dangerous small-r factor and removes the compact-
budget restriction of the earlier proof. Also E'<=E<11/5. The explicit
section-2 theorem thus applies at E', with no unknown onset function.

The minimum of G's two affine branches has secant slope magnitude at least
m_B=3/[20(1+delta)]. To retain a uniformly positive truncation coefficient on
the larger interval, use its steeper A branch when E>=15/8:

- If E<15/8, set m=m_B. For delta<=1/15,
  m(9-E)-1 >= 1/512 >0.
- If E>=15/8, the A-branch upper bound gives q<=39/2464, hence
  E'>=4269/2425>26/15>=17/10+delta/2. Both E' and E are on the A branch.
  Set m=m_A=3/[20(1-delta)]. Then m(9-E)-1>1/50.

These rational endpoint inequalities cover the entire budget/spacing range;
no untested branch identification is used. In both cases (3) and the
appropriate secant inequality give

    R >= G(delta,E')-q/(1-q)
      >= G(delta,E)+kappa(delta,E)q/(1-q),
    kappa = m(9-E)-1 >= 1/512.                          (4)

Any R<=G is at least G; all R>G are irrelevant competitors. The actual
ten-level upper witness proves (1). Equality in (4) forces q=0. There is
no interchange of dimension limits, appeal to convex hard-budget duality,
or assumption that the original countable infimum already had an optimizer.
The branch-sensitive proof replaces the earlier coarse restriction
kappa_B>0 for every budget, which would unnecessarily limit spacing to 1/50.

## 4. Explicit minimum dimension inside the window

For delta<3/380, every optimum has q=0 and hence lies in the low-support
class. Fix its physical spectrum and sign cones. At least one optimal
lifted vertex exists, and the strict inequalities in section 2 force that
vertex to be A/B. Both weights are positive for interior E.

Equality with G forces their offsets to be exactly zero and delta (either
orientation at the branch tie). To see this, lowering either positive-weight
offset strictly frees energy; at an interior budget the A/B return strictly
decreases as the B weight increases, so a strictly larger weighted offset
cost cannot attain the optimal formula. The two fractional offset classes
are distinct because 0<delta<1. Each preparation on {1,3} requires at least
five physical completion levels by the inherited shell-rank constraints.
They cannot share levels across these distinct fractional classes. Thus the
ORIGINAL physical spectrum contains at least ten levels. The exhibited
spectrum achieves ten, proving necessity and sufficiency on this explicit
strip, rather than on a further unevaluated neighborhood of zero.

This does not classify all optional unused levels, unitaries or coherent
minimizers. It proves a physical resource lower bound, not that every optimal
protocol is literally the displayed ten-level implementation.

## 5. Released quantitative near-optimal and bath guarantees

Let Gamma=G-B, c=11/50 and r=E-6/5. Define the explicit positive tolerance

    epsilon_0 = min(11r/780-Gamma, 1/10000) > 0.

For any 0<=epsilon<=epsilon_0 and any protocol with R<=G+epsilon,
its high-energy population obeys

    population(s>9) <= epsilon/[kappa(delta,E)+epsilon]. (5)

Proof: the preliminary tail bound q<=(Gamma+epsilon)/c ensures
q<=r/[2(9-6/5)], hence E'>6/5. For E>=15/8 the additional epsilon<=1/10000 gives
q<=1003/61600 and E'>=35491/20199>26/15, preserving the A-branch secant.
Section 3 applies unchanged, and solving
R-G>=kappa q/(1-q) proves (5). Positivity of epsilon_0 follows directly from
Gamma<= (3/20)delta r/(1+delta) on delta<=1/15. This controls population,
not tail energy, trace distance to a distinguished catalyst, or uniqueness.

The inherited faithful-bath stability theorem K2012 now has a fully
numerical reference regime. Its primal-dual gap is Gamma, so

    F_b-D_b >= Gamma-2 TV(b,b_ref).

Faithful baths within TV<Gamma/2 retain a strict gap. The sufficient Gibbs
condition is |t-1/2|<Gamma/12. At E=17/10 and delta=1/200, Gamma=1/2680;
thus TV<1/5360 or |t-1/2|<1/32160 is an actually certified radius.
These are robustness of the gap, not an assertion that G remains the exact
optimum for the perturbed bath or that missing-support baths are covered.

## 6. Actual upper limit on a uniform unrestricted onset

The seven-level K2015 witness has occupied energies {1,3,5}, probabilities
(81,9,1)/91, E=113/91 and R=81/182, with physical spectrum {0,...,6}.
For 0<delta<=1/2 its comparison to the proposed formula is exactly

    G(delta,113/91)-81/182 = 3(15delta-4)/[9100(1+delta)].

It ties at 4/15 and strictly improves G above that point. Therefore a largest
uniform unrestricted interval of the form (0,delta_*] lies between the
proved lower endpoint 1/15 and upper endpoint 4/15. We have NOT determined
delta_* inside that bracket. K2015 determines 4/15 exactly only for the
occupied-energy-at-most-nine class. Three actual witness comparisons,
including strict delta=3/10 and1/2 cases, are independently replayed.

## 7. Verification, rejected sharpness route and frontier

The producer consumes the complete K2015 interval certificate through 4/15
and replays 6,232 directional ray inequalities, 63 actual physical
optimal witnesses (including budgets one millionth from both endpoints),
189 quantitative near-optimizer consumers and 756 exact tail-equivalence
controls. The separate implementation reconstructs bath-label maxima and
all physical shell capacities, checks interval numerator endpoints, the exact
uniform kappa bound, tail and bath formulas, and exhausts 16 candidate small
completions of the canonical two-site support. Five fault controls reject an
unpaid offset, missing physical completion, wrong return factor, an extension
of the directional certificate to delta=1/100, and an inflated uniform tail
coefficient. Four provenance hashes are separate. The finite computations
support the explicit proof; samples alone do not prove its universal scope.

The provisional idea that 3/380 is sharp fails: the ray minimizing the c_B
ratio and B have incompatible return cones. Their actual half mixture has
strictly greater return than the chord. A physical separated mixture must
also pay its offset cost. This executed contrary case prevents turning a
sufficient bound into an exact transition. It does not refute the bound.

The substantive remaining thermal question is the unrestricted transition
inside [1/15,4/15], or the complete competing physical frontier beyond it. A useful
next method must retain actual cone compatibility AND physical offset costs;
a chord of incompatible rays is insufficient. Another existential onset,
small-spacing coefficient or repetition of this window is not that result.
Exact capped-pulse primal repair and a source-compatible common bar remain
separate contenders with their existing missing inputs. Preserve full20,
K/C/accessibility, mirror/full-II, normal jets, source2+1 and observed-chirality
debts. SC-META-53 remains UNCERTAIN, LT-SM8/LT-GR6b NEEDS; no source, ledger,
canon, novelty, independent-specialist or proof-assistant claim changes.

Reproduce from the repository root after K2015:

```text
python tests/channel-swings/k2016_explicit_unrestricted_thermal_window.py --write
python tests/channel-swings/k2016_explicit_unrestricted_thermal_window.py
python tests/channel-swings/k2016_explicit_unrestricted_thermal_window_probe.py
```
