---
title: "K2017: The sharp unrestricted thermal transition is 4/15"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional independent mathematics; no GU identification, canon promotion, novelty or external certification
scripts:
  - tests/channel-swings/k2017_sharp_unrestricted_thermal_transition.py
  - tests/channel-swings/k2017_sharp_unrestricted_thermal_transition_probe.py
---

# K2017: The sharp unrestricted thermal transition is 4/15

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
result: sharp unrestricted spacing transition and energy stability
carrier: exact extreme four-state channel and nondegenerate finite or countable positive-spacing catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input catalyst marginal half trace distance with upper mean-energy budget ON=independent_initial_registers
real_structure: complex conserving shell unitaries and real diagonal populations
grading: bath resonance components, not source chirality
action_owner: repository-construction -- unchanged K2008 thermal class
target: explicit global spacing window and resource stability MAP-TYPE=intertwiner
```

## 1. Sharp result and fixed object

In the exact finite-or-countable positive-spacing thermal class of K2008,
with bath ratio t=1/2 and every interior budget 6/5<E<11/5, the unrestricted
optimum is

    F_infty(delta,E)=G(delta,E)
      = B(E)+(3/20)delta min((E-6/5)/(1+delta),(11/5-E)/(1-delta)),
    B(E)=63/100-3E/20,                   0<delta<=4/15.       (1)

The endpoint is included and is the SHARP UNIFORM endpoint. The actual
seven-level witness already supplied by K2015 improves G at E=113/91 for
every 4/15<delta<=1/2. Thus no larger interval starting at zero can satisfy
(1) at every interior budget. K2016 proved only delta<=1/15; this note
closes its [1/15,4/15] bracket without a larger finite census.

This is independent conditional mathematics, not a GU prediction. Retain
K1943's exact extreme four-state channel, faithful four-level bath,
independent input registers, nondegenerate nonnegative spectrum with ground
zero, exact energy conservation and worst-input catalyst MARGINAL half trace
distance. Coherent preparations are included by the established pinching
reduction; an arbitrary prescribed coherent state need not attain the sharp
diagonal formula. No continuous or degenerate catalyst spectrum, free flag,
product return, repeatability, arbitrary bath optimum or novelty is claimed.

## 2. Directed deletion before normalization

For any nonnegative diagonal populations p, normalized or not, write

    R(p)=1/2 sum_s (p_s-I_s(p))_+,
    I_s(p)=sum of incoming positive edge imbalances.

For an edge from s to s+d, d=1,2,3, its two weights are H_d p_s and
L_d p_(s+d), where

    L_d=(1+t+...+t^(3-d))/(1+t+t^2+t^3), H_d=t^d L_d.

Let p^- delete every population above a cutoff N; q=sum_(s>N)p_s.
The actual occupied graph is a disjoint union of increasing paths. Each
retained site has at most one edge crossing up through N, and each removed
site at most one edge crossing down. Only loss of incoming flow through a
crossing edge can increase a retained positive deficit. On such an edge,

    0 <= (L_d p_tail-H_d p_low)_+ <= L_d p_tail.

The function x_+ is 1-Lipschitz. Drop the nonnegative original deficits on
removed sites and sum the retained deficit increases. This proves

    R(p^-) <= R(p)+C_boundary,
    C_boundary=1/2 sum_crossing_edges L_d p_tail
              <= C_t q,
    C_t=(1+t+t^2)/(2(1+t+t^2+t^3)).                       (2)

At t=1/2, C_t=7/15. The coefficient is a proved bound, NOT asserted optimal.
The direction matters: a high-energy neighbor contributes L_d, not H_d.
This argument uses actual positive-part changes, not differentiability or
an assumed fixed sign cone. It remains valid for countably many components
by summing nonnegative inequalities; all sums converge by total mass.

Homogeneity gives R(p^-/(1-q))=R(p^-)/(1-q). If h=sum_(s>N)s p_s and
e=sum s p_s, its mean is (e-h)/(1-q). Keep ALL original physical completion
levels through N+3, including zero-population positions. Every retained input
shell keeps its original positions. Positive spacing makes this a finite
physical spectrum even for countable inputs. There is no arbitrary
population projection claimed to preserve an unchanged unitary: a sharp
shell implementation exists on the retained completed spectrum by K1943.

## 3. Compose the existing COMPLETE low-support certificate

Set N=9, a=6/5, b=11/5 and m=3/[20(1+delta)]. K2015 already certifies G
for every physical protocol with occupied energy at most nine throughout
0<delta<=4/15. Its 26 supports, 183 orientations and full compatible interval
program are reused; another large cutoff enumeration is unnecessary.

For retained budget x in [1,E], define

    f(x)=B(x) if x<=a;  f(x)=G(delta,x) if a<x<=E.

The first branch is the existing global supporting lower bound K1950, not
an extrapolation of a two-ladder optimizer into an infeasible energy range.
The two branches of G have slopes -m and -3/[20(1-delta)]; both join
continuously at their minimum's kink. Below a, B has slope -3/20 and joins
G at9/20. Therefore, throughout [1,E],

    f(x) >= G(delta,E)+m(E-x).                            (3)

In particular retained budgets BELOW6/5 are covered. The old preliminary
tail bound and high-budget branch split are no longer needed.

Take any protocol at mean e<=E and let q,h be its diagonal mass and energy
above9. Since occupied energies are at least1, q<=(E-1)/8<1, so its retained
state exists with x=(e-h)/(1-q)>=1 and x<=E. Combine its low-support lower
bound, (2) and (3):

    R_original >= R_diagonal
      >= (1-q)f(x)-(7/15)q
      >= G(delta,E)+m(E-e)+m(h-9q)+kappa(delta,E)q,
    kappa=m(9-E)-G(delta,E)-7/15.                         (4)

No assumption R<=G or approximate-optimality tolerance was used. Since
G(delta,E)<=9/20-m(E-a),

    kappa >= m(9-a)-9/20-7/15
          >= (9/76)(39/5)-11/12 = 2/285 >0.              (5)

Every term after G in (4) is nonnegative. Hence R>=G for EVERY finite or
countable competitor. The actual ten-level upper witness proves (1).
The previously retained seven-level counterexample proves sharpness above
4/15. This is a direct physical hard-budget argument, not strong Lagrange
duality, a dimension-limit interchange or a countable-attainment assumption.

## 4. Released population, ENERGY and budget stability

For ANY epsilon>=0 and any protocol with R_original<=G+epsilon, (4) gives

    m(E-e)+m(h-9q)+kappa q <= epsilon,
    q <= min(1,epsilon/kappa),
    E-e <= epsilon/m,
    h <= 9epsilon/kappa.                                (6)

For the last bound, m h <= epsilon+(9m-kappa)q and
9m-kappa=mE+G+7/15>0; substitute q<=epsilon/kappa.
Unlike a mass-only truncation estimate, this controls actual high-energy
expectation. There is no small-epsilon qualification. The universal uniform
versions are q<=285epsilon/2 and h<=2565epsilon/2, with trivial mass/mean
bounds also available. Constants are conservative and not claimed sharp.

Every exact optimizer has q=h=0 and e=E. Thus its diagonal occupied support
is finite and at most nine, even if its spectrum has infinitely many unused
levels. Positivity then excludes coherences joining that support to a
zero-diagonal tail. This does not classify coherences within the support or
trace distance to a chosen optimizer. It DOES show saturation of the allowed
mean-energy budget, a consequence not supplied by the prior mass bound.

For a faithful perturbed bath b', K2012 transports the reference gap
Gamma=G-B: F_b'-D_b'>=Gamma-2TV(b',b_ref). TV<Gamma/2, or the sufficient
Gibbs condition |t-1/2|<Gamma/12, retains strict positive duality gap on the
entire sharp reference strip. It does not keep G as the perturbed optimum.

## 5. Verification, contrary routes and successor

The producer checks183 actual completed physical tail deletions at three
bath ratios,24 actual globally optimal ten-level witnesses, and72 rational
secant/truncation controls including retained budgets below6/5. The separate
implementation recomputes bath-label maxima and shell capacities, all these
controls, and rejects four actual corruptions after a clean baseline:
normalization, completion, return and tail energy. Four input hashes are
provenance checks. The universal result rests on (2)--(5) and the inherited
complete low-support proof, not sampling. No independent specialist,
proof-assistant acceptance or external novelty review is claimed.

Strongest hidden seam: confusing normalized and unnormalized deletion would
lose the -(G q) term in (4). Strongest contrary route: changing a high-edge
coefficient to H, or keeping only occupied completion levels, is invalid.
A trial extension to delta=3/10 makes the uniform coefficient in (5) negative
and an actual seven-level competitor beats G; no extension is inferred.
All source, ledger and canon verdicts remain unchanged.

The released next question is equality in the existing finite certificate:
which optimal rays remain, and does the sharp endpoint change the smallest
physical catalyst? K2018 executes that successor. The full frontier ABOVE
4/15 still requires a new compatible finite certificate and its own tail
transfer; a feasible competitor alone is not that frontier.

Reproduce from the repository root:

```text
python tests/channel-swings/k2017_sharp_unrestricted_thermal_transition.py --write
python tests/channel-swings/k2017_sharp_unrestricted_thermal_transition.py
python tests/channel-swings/k2017_sharp_unrestricted_thermal_transition_probe.py
```
