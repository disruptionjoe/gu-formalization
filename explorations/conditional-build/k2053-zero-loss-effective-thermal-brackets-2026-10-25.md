---
title: "K2053: Zero-loss finite approximation and a low-energy thermal bracket"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: improved effective approximation and certified bracket at energy5/2 above half spacing; no exact low-energy frontier
scripts:
  - tests/channel-swings/k2053_zero_loss_effective_thermal_brackets.py
  - tests/channel-swings/k2053_zero_loss_effective_thermal_brackets_probe.py
---

# K2053: Zero-loss finite approximation and a low-energy thermal bracket

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: multiplicative finite-dimension bounds, sharper sufficient resources and a physical low-energy bracket
carrier: four-state bath and finite/countable pure-point catalyst LAYER=toy CHIRALITY=N/A
pairing: positive populations and worst-input marginal half trace distance ON=declared_bath_catalyst
real_structure: complex shell channels and nonnegative populations
grading: physical energy shells and resonance components
action_owner: repository-construction -- K2008 and K2020 exact thermal model
target: certified finite approximation to unrestricted return MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] K2020's zero-loss erasure improves the
older K2008 effective-dimension theorem. A finite optimum now gives a
multiplicative two-sided bracket on the unrestricted finite/countable optimum,
with a smaller sufficient dimension for any prescribed additive accuracy.
Separately, direct cellwise support certificates and a physical thirteen-level
channel give a rigorous nonzero-width bracket at E=5/2 for1/2<delta<=1.
The fictitious tail point is retained only as lower-bound machinery.

## 1. Updated all-temperature finite approximation

Keep K2008's nondegenerate, nonnegative pure-point catalyst with ground zero,
minimum physical gap delta>0, upper mean budget E, normal initial state,
independent registers and exact energy-shell channel. Bath energies are0,1,2,3
and weights t^b/(1+t+t^2+t^3),0<t<1. Let F be the unrestricted finite/countable
optimum and F_d the optimum with at most d physical levels. K2010 supplies
unrestricted attainment; K2008 supplies equality of finite/countable infima
and finite-dimensional approximation. These are reused, not new claims.

For any feasible E>1 and integer N>E, put D=2N+7 and

    Q_N=(E-1)/(N-1), alpha_N=1-Q_N=(N-E)/(N-1).

Then

    alpha_N F_D <= F <= F_D,
    0<=F_D-F<=Q_N F_D<=(E-1)/(2(N-1)).                  (1)

Unlike K2008's older bound (E-1)/(N-E), this uses zero-loss erasure and then
rearranges the multiplicative inequality before using F_D<=1/2.
For a tolerance epsilon>0 it suffices to choose

    N=max(floor(E)+1, ceil(1+(E-1)/(2epsilon))), D=2N+7. (2)

This remains a sufficient O(E/epsilon) bound, not a sharp dimension law or
a proof that finite dimension attains F. E=1 is handled by the inherited
pure three-level construction when feasible. No bound is asserted by
subtracting infinities at infeasible parameters.

### Proof with actual energy and physical completion

Every occupied energy is at least1. Delete occupied mass q at actual energies
strictly greater than N. Its energy moment gives q<=(E-1)/(N-1)<1.
K2020's terminal-erasure theorem applies at this absolute cutoff, component
by component, including fractional offsets and countable tails. It gives

    R(p_low)<=R(p), R(p')<=R(p)/(1-q), p'=p_low/(1-q).    (3)

The removed energies exceed the original mean, so the normalized retained
mean does not exceed that mean. Keep all physical completion levels through
N+3 before deleting unused components. K2008's two-component reduction
preserves spacing and counts at most2N+7 physical levels, including ground
and unoccupied shell partners. Thus F_D<=R(p)/(1-Q_N). Pass to the infimum,
then rearrange; F_D<=1/2 gives (1). No limit of infinite unitaries is required.
K2008/K2010 already justify the diagonal, countable and full-channel transfer.

The normalization coefficient in (3) cannot be improved uniformly: at t=1/2,
p=(9/10,1/10) on occupied energies(1,3), physical completion0,...,4, has
return9/20. Erasure of the upper input leaves the SAME unnormalized return,
while the normalized return is1/2. Thus R(p')-R(p)=q R(p') exactly.
This proves sharpness of that erasure/normalization step, not sharpness of D
or of the final worst-case energy bound.

## 2. Effective stopping certificates and useful consequences

If a rigorous finite solver certifies l_D<=F_D<=u_D, then

    alpha_N l_D <= F <= u_D,
    u_D-alpha_N l_D = (u_D-l_D)+Q_N l_D.                (4)

A feasible channel alone supplies only u_D; substituting it for l_D would
reverse the lower-bound logic. This yields a genuine, explicit stopping
certificate once both finite optimization sides are available. It does not
make their enumeration computationally cheap. F_d is nonincreasing in d.
Applying (1) along D=2N+7 proves uniform approximation on bounded feasible
energy sets, uniformly in temperature and positive spacing wherever the
model is feasible. No new continuity across spacing thresholds follows.

For E=5/2 and epsilon=1/100, (2) gives N=76,D=159; the bound is1/100.
The earlier K2008 sufficient choice N=153,D=313 is larger. These are proven
sufficient resources, not necessary numbers, and no159-level optimum was
computed here.

## 3. A physical bracket at E=5/2 above half spacing

Set t=1/2 and1/2<delta<=1. Reuse K2049's ground-pair packing lemma:
at most one occupied component has original offset below1, while all others
pay at least1 on every unit of population. Reuse K2045's complete cutoff11
bank (671 cells,20975 vertices,626412 enumerated bases) by its pinned digest.
The new producer assigns an affine support g_c(e)=a_c+s_c e to EACH possible
low cell, with s_c<0, and verifies

    R(v)>=g_c(e(v)) on that low cell,
    R(v)>=g_c(e(v)+1) on every high cell,
    g_c(12)<=0, g_c(13)<=0,
    g_c(5/2)>=124659/450796.                            (5)

K2049's unnormalized component/tail argument therefore proves the lower
bound for all finite/countable spectra, not only the finite bank. In (5),
the zero tail contact is permitted as a relaxed supporting point. It is
never interpreted as a physical zero-error catalyst.

An actual upper witness has occupied energies1,3,5,7,9,11 with populations

    (5052,7578,842,109,62,93)/13736.                     (6)

Its physical completion is0,...,12. Direct bath-label shell capacities and
sharp return give mean5/2 and return7671/27472. All physical gaps are1, so
it is feasible for the entire stated spacing interval. Consequently

    124659/450796 <= F_delta(5/2) <= 7671/27472,
    bracket width = 8356017/3096066928.                 (7)

The producer searches the existing cell hulls for a useful witness; the
separate checker reconstructs every bank vertex's return from bath labels
and checks all affine inequalities and the physical witness directly.
Neither the optimizer's claimed value nor a solver status is an acceptance
input. The thirteen physical levels are a sufficient realization, not a
minimal-resource claim. The gap is nonzero, so the exact optimum and the
full lower-energy frontier remain open. This is a quantitative result in
the previously unresolved region, not a continuation of K2049's exact
high-energy formula below its proven scope.

### Released whole-energy bracket

The same assignments prove an interval result, not merely a sampled point.
For EVERY1/2<delta<=1 and

    2843/1165 <= E <= 1951423/716722,

one has

    39366/112699 - (6561/225398) E
      <= F_delta(E) <= 3933/13736 + (-39/13736) E.                (8)

The upper construction interpolates the populations
(432,648,72,8,2,3)/1165 and(96,144,16,4,6,9)/275 on the same six odd
inputs and physical spectrum0,...,12. Their energies are2843/1165 and789/275,
respectively. Direct shared bath maximizers and common clipping signs prove
that the return is affine throughout this entire population segment.
The claimed upper-energy endpoint lies inside that segment. Every assigned
lower support exceeds the displayed lower line at BOTH interval endpoints;
affinity proves the whole interval. The limiting upper endpoint is a
certificate-domain boundary, not a claimed physical phase transition.

## 4. Verification, scope and next step

Exact checks cover normalization, budget, dimension/tolerance arithmetic,
zero-loss sharpness, all new support lines, the physical witness and the
rational bracket. Planted mathematical faults are rejected only after a
clean baseline. Existing bank completeness and infinite-tail erasure proofs
are reused by hash; no new626412-basis enumeration is claimed. Same-author
internal checks and written proofs are not external or proof-assistant
certification. Source register, physics ledger and canon are unchanged.

The next genuinely stronger result is a new tail lower estimate or an
actual physical construction narrowing (7), or a rigorously solved finite
program supplying both sides of (4). Merely enlarging the finite bank or
reporting the fictitious tail endpoint would not prove an exact frontier.
