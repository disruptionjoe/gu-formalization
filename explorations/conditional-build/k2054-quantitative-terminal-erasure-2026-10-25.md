---
title: "K2054: Quantitative terminal erasure and attached thermal tails"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact terminal response, finite/countable tail controls and improved bracket; no exact optimum
scripts:
  - tests/channel-swings/k2054_quantitative_terminal_erasure.py
  - tests/channel-swings/k2054_quantitative_terminal_erasure_probe.py
---

# K2054: Quantitative terminal erasure and attached thermal tails

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
result: sharp terminal excess inequality, zero-loss characterization and attached-tail stability
carrier: four-state bath and finite/countable positive-spacing catalyst LAYER=toy CHIRALITY=N/A
pairing: nonnegative populations and sharp marginal half trace distance ON=declared_bath_catalyst
real_structure: complex shell channels with real diagonal populations
grading: increasing occupied resonance paths
action_owner: repository-construction -- unchanged K2020 thermal channel
target: quantitative upper-tail erasure MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] K2020's zero-loss erasure is strengthened
by a sharp single-terminal excess bound. It gives a boundary-dependent tail
certificate, classifies exactly when an entire upper tail is invisible to the
unnormalized return, and controls almost invisible tails. It strictly narrows
K2053's low-energy optimality gap using its attached-boundary correction,
while leaving a positive gap. These are independent thermal-model
results, with no source-physics or novelty claim.

## 1. Sharp terminal inequality at every faithful temperature

Keep K2020's actual model, path geometry and sharp diagonal return R. For a
terminal population u with predecessor population p and predecessor incoming
flow c0>=0, set, for gap d in{1,2,3} and 0<t<1,

    Z=1+t+t^2+t^3, L=(1+...+t^(3-d))/Z, H=t^d L,
    k=H/(1+L), c=(1+H-L)(1+L)/(2(1+H+L)).

Twice the affected return is the inherited expression

    T(u)=(p-c0-(Lu-Hp)_+)_+ +(u-(Hp-Lu)_+)_+.

Writing Delta=(T(u)-T(0))/2 gives the NEW sharp uniform inequality

    Delta >= c (u-kp)_+,                                  (1)
    Delta=0 iff u<=kp.                                    (2)

The coefficient c is sharp when incoming c0 is unconstrained except c0>=0:
choose c0=0, p>0 and u=(1+H)p/L. This is an actual two-input path, not merely
an algebraic fixture. An isolated terminal instead contributes u/2.

### Complete piecewise proof

Let a=Hp and A=(p-c0)_+ in[0,p]. For u<=a/L,

    2Delta=((1+L)u-a)_+.

For u>=a/L,

    2Delta=u-min(A,Lu-a).

Thus Delta is minimized over c0>=0 at A=p. The minimum is linear on the
three intervals with boundaries kp, a/L, (p+a)/L; it vanishes below kp,
has slope(1+L)/2, then(1-L)/2, then1/2. Since 0<L<1, (2) follows.
For p>0 the ratio Delta/(u-kp) decreases on the middle interval, increases
on the final interval, and is constant(1+L)/2 on the first. Its global
minimum at u=(p+a)/L is exactly c. For p=0 the response is u/2 and c<=1/2.
This proves (1) on the whole half-line, not by sampling breakpoints.

At t=1/2 the exact values are

| gap d | k | sharp c |
| --- | --- | --- |
| 1 | 7/29 | 29/135 |
| 2 | 1/9 | 9/50 |
| 3 | 1/23 | 23/90 |

## 2. Whole-tail attachment and near-erasure stability

Erase all occupied energies above any fixed absolute cutoff N. Let q be
their mass, b the sum of populations of retained immediate predecessors at
the cut, and Delta=R(p)-R(p_low)>=0 the actual UNNORMALIZED erasure loss.
Each retained predecessor is counted at most once because components are
increasing paths. For an erased vertex i with predecessor population p_parent
use its actual edge k_i; an erased component root has k_i p_parent=0.
Descending terminal erasure and (1) prove at t=1/2

    Delta >= (9/50) sum_erased (p_i-k_i p_parent)_+,       (3)
    q <= (7/22)b + (725/99)Delta.                         (4)

Indeed k_i<=K=7/29; the sum of erased predecessor populations is at most
q+b, so the excess sum is at least(1-K)q-Kb. Rearrangement gives (4).
It is also legitimate to use the positive part of this latter lower bound.
For a tail whose every edge has gap2, the stronger constants give

    q <= b/8 + (25/4)Delta.                              (5)

For an upper tail starting at positive spacing, bounded energy intervals
are finite. Apply the finite theorem to successive truncations. The inherited
l1 continuity of R passes Delta to the limit, while nonnegative excess sums
converge monotonically. This proves (3)--(5) for countable paths and countably
many components. No highest vertex of an infinite path is assumed. No
normalization or mean-energy rescaling is performed in these inequalities.

Consequently a protocol losing at most epsilon on erasure obeys the same
bounds with Delta replaced by epsilon. The general-path constants in (4)
are sufficient, not asserted sharp: adjacent gaps obey geometric restrictions
that prevent arbitrary repetition of gap1. The sharp c in (1) and sharp
zero-loss gap2 ratio below are distinct claims.

## 3. Exact invisible-tail classification and geometric controls

The finite telescoping sum consists of nonnegative terminal losses. Each
loss is zero exactly when p_i<=k_i p_parent. The same equivalence holds for
countable paths by the l1 limit and nonnegative series. Thus

    R(p)=R(p_low) iff every erased edge satisfies
    p_i<=k_i p_parent and every wholly erased root has zero mass. (6)

Successive inequalities yield geometric control along an invisible path:
p_(j+n)<=p_j product_(r=1..n) k_(j+r). In particular no positive isolated
high component is invisible. This exposes the physical dependency that a
fictitious mass at(12,0) omits: invisible mass must be attached to a retained
population and respect every local threshold.

For an all-gap2 path at t=1/2, p_j=b/9^j on energies 1+2j is invisible
beyond the first input. Its infinite tail mass is exactly b/8, so the zero-loss
boundary ratio1/8 in (5) is sharp. Normalizing gives b=8/9, mean5/4 and
return4/9. The physical spectrum of nonnegative integers supplies shell
completion and any spacing<=1; countable finite mean is allowed. This is a
sharp control of the new tail statement, not a new optimum at energy5/4.
Finite truncations have tail b(1-9^(-n))/8 and approach the bound. After
normalizing an erased state, return generally changes, as K2020 already showed.

## 4. A usable boundary correction for finite certificates

If a finite low-population certificate proves R(p_low)>=A*m_low-s*e_low
on its declared cell, then (3) gives

    R(p)>=A*m_low-s*e_low
            +(9/50)((22/29)q-(7/29)b)_+.                (7)

One may keep individual gap-dependent excess variables for a tighter exact
piecewise-linear certificate. Boundary population b is part of the finite
state, not an independently free optimizer. Formula(7) constrains an attached
tail in K2053's lower-bound program, but its energy, cell and budget must still
be combined consistently before claiming an improved optimum. No improved
numeric bracket or globally sharp frontier is asserted here.

## 5. Released improved low-energy certificate

The boundary term is consumed, not left as a future suggestion. At t=1/2,
1/2<delta<=1 and E=5/2, the new finite/countable lower bound is

    439997389/1588579400 <= F_delta(5/2) <= 7671/27472.   (8)

The lower improvement over K2053 is exactly
79585886761/179031309800600>0. The remaining gap is
12298038349/5455181659600>0. The upper physical thirteen-level witness is
unchanged and is reused, not counted as a new construction.

For each of the 671 retained cutoff-eleven orientation cells choose one
triple(a,s,theta), with s<0 and 0<=theta<=9/50. At every vertex let b be
the final population if the final canonical energy is at least9, and zero
otherwise. Verify exactly

    R(v)-theta*(7/29)*b(v) >= a+s*e(v) on the chosen low cell,
    R(v)-theta*(7/29)*b(v) >= a+s*(e(v)+1) on ALL high cells,
    a+12s <= theta*(22/29), a+13s <= theta*(22/29).       (9)

The retained parent of an erased tail must have canonical energy9,10 or11
because the next gap is at most3. There is only one such parent per component.
The vertex b can overestimate a nonexistent attachment and is therefore safe.
Choose the cell of the actual nonzero retained support. During its vertex
checks retain that cell's fixed support coordinates, even when its last vertex
population is zero; do not recompress a zero face before evaluating b or e.
This preserves the linear functional used in interpolation. For a genuinely
smaller actual support choose its own complete-bank cell.

The return is convex piecewise-linear within an orientation cone, not affine
on its whole cone. The inherited complete arrangement vertex bank subdivides
also at every deficit hyperplane. On each such subcell R and b are linear,
so (9) at all its vertices proves the inequality throughout the cone.

For a component with original offset d, total mass m, erased mass q and
canonical tail energy h>=12q, let ell=0 for the at-most-one component with
d<1 and ell=1 for all others. K2049 supplies that packing classification.
The new erasure bound and (9) yield

    R_component >= a*m+s*e_actual
       + q[theta*(22/29)-a-s*(12+ell)]
       + (-s)(h-12q)+(-s)(d-ell)*m.                    (10)

All correction terms are nonnegative. Entirely erased components have b=0
and satisfy the same excess inequality, including their erased root; their
return need NOT be q/2 unless they consist of one isolated input. No such
stronger false inequality is used. Choose one theta for the actual low cell
and use its same triple for every high component. Summing and using s<0 and
the upper mean budget gives the claimed lower bound. With no low component,
any assignment suffices. Positive spacing and inherited l1 continuity give
the countable limit. This is an attached-tail proof, not truncation at zero
cost or a claimed attained zero-return tail.

The same assignment bank supplies a whole interval. Throughout

    2843/1165 <= E <= 6986144548/2571017525,

    133748941/397144850 - (759987/31771588) E
       <= F_delta(E) <= (3933-39E)/13736.              (11)

Every assigned line dominates this lower line at both endpoints; the upper
family is K2053's proved common-return-chamber interpolation. Its domain
contains this interval. No physical phase transition is inferred at the
certificate endpoint. The producer searches only seven rational theta values;
optimality of that search is unnecessary because the checker verifies the
resulting inequalities directly. The 626412-basis completeness proof is reused
by exact bank hash, not rerun. The new bound is not an exact optimum.

## 6. Verification and limits

The written piecewise proof establishes all-temperature and countable claims.
The producer checks exact threshold and sharp coefficients for twelve
bath/gap choices and controls zero populations and arbitrary incoming flow.
A separate checker starts from actual bath-label maxima, verifies physical
terminal equality, path tail deletions, geometric chains, isolated components
and coefficient faults after a clean baseline. The boundary checker also reconstructs all20975 bank vertex returns from bath
labels, checks every new support line, and checks whole-interval inequalities.
Existing shell geometry and
l1 continuity are reused from K2020 by hash; the large vertex bank is not
rerun. Review challenges general-gap sharpness, countable telescoping and
normalization. Source register, physics ledger and canon remain unchanged.
