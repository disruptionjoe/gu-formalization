---
title: "K2059: Energy-aware attached tails and a two-peak thermal witness"
status: active_research
doc_type: exploration
created: "2026-10-25"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional finite and countable thermal bounds; no exact optimum or GU physics verdict
scripts:
  - tests/channel-swings/k2059_energy_aware_thermal_tail.py
  - tests/channel-swings/k2059_energy_aware_thermal_tail_probe.py
---

# K2059: Energy-aware attached tails and a two-peak thermal witness

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
result: stronger whole-energy lower certificate and physical finite/countable upper construction
carrier: four-state thermal channel with nondegenerate positive-spacing catalyst supports LAYER=toy CHIRALITY=N/A
pairing: diagonal classical marginal return ON=declared_thermal_population_model
real_structure: nonnegative real populations and rational arithmetic
grading: occupied support energies and gaps, not field parity
action_owner: repository-construction -- K1935 thermal model and K2054 terminal response
target: conditional return envelope with actual attached tails MAP-TYPE=intertwiner
```

[Verified conditional mathematics.] For the existing four-state thermal
population model at bath weights(8,4,2,1)/15, spacing1/2<delta<=1 and upper
mean energy E=5/2, the improved bracket is

    19063992615557/68547998140000 <= F_delta(5/2)
                               <= 11561805/41518097,
    0.2781115879798762          <= F_delta(5/2)
                               <= 0.2784762750566338.

A finite21-level physical spectrum gives upper286767/1029752, approximately
0.2784816150. The smaller upper uses an invisible geometric countable tail;
finite truncations approach it. These are bounds, not the exact optimum or
minimal resource theorem. Compared with K2057's final bracket, the width
shrinks by about82.2 percent. Both constructions and lower proof vary with E.

## 1. Inherited inputs and precise advance

[K2057](k2057-gap-aware-thermal-erasure-2026-10-25.md) supplies gap-aware
mass erasure q<=B+25Delta/4. Its optimized scalar-price relaxation is already
saturated. [K2029](k2029-multicomponent-thermal-placement-2026-10-24.md)
section3 supplies the compulsory physical ladder argument; this is NOT a new
packing lemma. We consume a safe offset consequence of that argument across
the existing cutoff-eleven bank and then price actual tail energy and incoming
gap, instead of pricing all erased mass at cutoff12. Finally we improve the
feasible upper construction by allowing two separated population peaks.

The complete inherited bank has671 subcells and20975 vertices. Its626412-basis
completeness is pinned reuse, not a new enumeration. The bank includes all
bath-max and deficit hyperplanes, so the actual return is affine on each
subcell. Vertex inequalities therefore extend to arbitrary populations.

[K2054](k2054-quantitative-terminal-erasure-2026-10-25.md) supplies the
incoming-aware terminal deletion loss. Occupied connected support gaps are
in{1,2,3}, and consecutive gaps d,e satisfy d+e>=4. Write

    k=(7/29,1/9,1/23), c=(29/135,9/50,23/90).

Deleting the last population p with predecessor b loses at least
c_d(p-k_d b)_+ in UNNORMALIZED return. A wholly erased root loses half its
population. This includes the incoming flow at the predecessor.

## 2. Packing consequence and the fixed-support rule

[K2049](k2049-wide-spacing-packing-2026-10-25.md) permits at most one
component with canonical offset D<1; all others have D>=1. Canonical roots
are1 or2. For a low component of fixed support s with at least two vertices,
put Z=s_penultimate+3. Its two-input shells force the physical catalyst ladder
D+[0,Z]. Indeed a shared shell has four occupied channel inputs and therefore
all four bath-compatible output energies; each edge forces the integer
interval from s_next-3 through s_previous+3. These intervals overlap or touch.
For root1 the lower singleton shell and D<1 force positions0,1; root2's first
shared shell already does so. This extends the same compulsory-ladder logic
used in K2029; we deliberately use a weaker safe bound than its sharper cases.

Any other component's first occupied energy y is at least2>D. If y lies
inside this ladder, a different fractional residue is within1/2 of a physical
ladder point, violating spacing. The same residue would share a bath shell
with an occupied low input and belong to that component. Hence y>D+Z. Its
canonical root r<=2 gives offset D_other=y-r>Z-2+D. We may safely use

    ell(s)=max(1,s_penultimate+1),

or ell=1 for a singleton. If there is no low component, choose the singleton
assignment and treat every component as high. The low component's actual
support determines ell, including if it extends beyond cutoff11: its retained
prefix supplies a weaker valid ladder. A component wholly above cutoff11
cannot be low, since a canonical root is1 or2.

The bank's fixed cell support is kept on its zero-population faces. One must
not recompress each vertex separately before computing ell or the boundary
coefficient: that would change the linear functional under interpolation.
For an actual population choose its genuine positive support first and then
use the closure of that cell for the certificate.

## 3. Energy-aware Bellman majorants

Seek a lower line a-tE, t>0. For n>=12 and incoming gap d, define

    G(n,d)=max(0, a-t*n + max_{e:d+e>=4} k_e G(n+e,e)).    (1)

Use cutoff L=64, G=0 beyond L, and a<=t(L+1). Farther rewards are nonpositive;
zero is consequently a valid majorant there. For the low cell, require
G(n,d)<=c_d only for states reachable from an allowed first erased edge of
that cell. Requiring the unreachable state(12,2) for cell188 would needlessly
weaken this bound. The released constraint there is reachable(13,2).
For high components define G_high by replacing a with a-t*ell. Require its
cost caps for every state and its whole-root reward at most1/2.

If s ends at z with incoming gap r, let allowed outgoing d satisfy z+d>=12
and r+d>=4; a singleton has no incoming restriction. Define

    B_low(s)=max_allowed k_d G(z+d,d),
    B_high(s)=max_allowed k_d G_high(z+d,d).

Empty maxima are zero. For each possible low cell choose ONE line and prove
on its vertices and on EVERY high cell's vertices, respectively,

    R(v)>=a-t*e(v)+B_low(s)*p_last,
    R(v)>=a-t*(e(v)+ell)+B_high(s)*p_last.               (2)

To see the tail transfer directly, put x_j=(p_j-k_d p_(j-1))_+ and
w_j=a-t*n_j. Then p_j<=k_d p_(j-1)+x_j, G>=0 and (1) give

    sum_tail w_j p_j <= B_low p_last + sum_tail G(n_j,d_j)x_j
                     <= B_low p_last + Delta.

One can derive the first inequality by writing w_j<=G_j-k_next G_next
and telescoping. It does not multiply a signed reward by an inequality.
The high formula uses w_j=a-t(n_j+ell). A wholly erased component starts
with a root whose maximum future reward is at most1/2, paid by its root loss.
Offset D>=ell only decreases the target line since t>0. Combining(2) with
these actual attached-tail inequalities gives R_total>=a-t*E_actual, and
therefore >=a-t*E_budget. There is no free, fictitious zero-return tail.

The remaining666 low assignments use K2057's scalar-price version with
0<=eta<=4/25 and the improved ell. Explicitly replace B by eta times its
invisible-tail reward, require a-12t<=eta and a-(12+ell)t<=eta, and check(2).
Its proof follows q<=B+25Delta/4 with Delta>=0. Five near-bottleneck cells
use(1). Every one of the671 low alternatives has an exact rational assignment.

For countable finite-mean states, positive spacing gives finite support below
any fixed cutoff. Prove the inequalities on finite truncations, then use the
inherited l1-continuity of return and convergence of mass and energy. The
majorant itself has finite energy range. No highest infinite vertex is assumed.

## 4. Released exact certificate and interval

Packing alone gives lower156644/563495. Energy-aware propagation improves it
to the displayed result; cell188 is the certificate bottleneck. Its line is

    L(E)=10473428044791/34273999070000
           -(75314538961/6854799814000)*E.

All671 assignments dominate this line on

    91135/37292 <= E <= 1902504111222032340789/758668264726977861095.

The producer finds candidate affine Bellman policies, solves exact two-contact
systems and verifies all inequalities. Rational seed choices and the finite
eta set are search choices, not claims of global dual optimality. A distinct
same-author probe recomputes raw bath-label maxima at all20975 vertices,
checks all low and high inequalities, Bellman transitions/caps, interval
crossings, packing, attached and wholly erased tails, and deliberate faults.

## 5. Two-peak physical upper construction

Use occupied energies1,3,...,19 and physical finite spectrum0,1,...,20.
For consecutive occupied inputs let orientation1 mean the left thermal
contribution is heavier and0 the right is heavier. Choose

    (0,1,1,1,0,0,0,0,1).

In the actual maximal-retention marginal matrix T, singleton boundaries
contribute T_00=2/5 and T_99=1/10. Every edge contributes half its weight to
each adjacent output row at the winning column, with weight1/5 for left and
4/5 for right. Set all deficits (I-T)p to zero except indices1 and8. Solve
these equations together with total mass1 and mean energy E. The certificate
stores exact affine populations, checked positive with consistent orientations
and nonnegative deficits on249/100<=E<=251/100.

The countable version appends population p_19/9^j at energy19+2j, j>=1.
Its added mass is p_19/8 and energy85p_19/32. These replace the two constraints
in the same linear system. At E=5/2 its ten retained populations are

    (15341724,23012586,2556954,284106,41569,
     32896,49344,74016,111024,12336)/41518097.

The added tail is invisible to return. Its exact upper line is stored in the
certificate; together with L(E), it supplies a two-sided interval certificate
on the intersection of the two displayed energy intervals.

Physical attainment uses the inherited all-input shell construction from
[K1934](k1934-nonuniform-four-level-catalyst-optimization-2026-10-22.md).
In each shared shell choose the thermally heavier occupied input. Map its
orthonormal two-dimensional input plane to the two occupied output positions,
with its own position first; map the lighter plane to the two empty positions.
For a singleton, map to its own position and an available empty position.
Every shell has the required dimension. Complete the remaining columns
orthogonally. For each declared channel input v_j this sends Wv_j to the same
ordered output pair, so the whole complex Gram matrix, not just probabilities,
is preserved. Its own-first probability is1/2 for j=1,2,4 and1 for j=3.
At1/2 the return equals the raw deficit formula; at1 it is no greater. Thus
the worst declared input achieves precisely the claimed bound. The probe
reconstructs every physical bath shell for both probabilities and checks
normalization and output total variation. Orthogonal completion supplies the
all-input unitary, not a separate state-dependent map for each v_j.

The infinite direct sum of the same finite shell unitaries is unitary on the
countable physical Hilbert space. Finite truncation, normalization and l1
continuity recover the countable return as a limit. The constructed population
has finite mean and the integer physical spectrum permits every delta<=1.
No finite truncation is asserted to have exactly the infinite bound.

## 6. Review, reproduction and remaining gap

Run the two named scripts from the repository root. Producer --write rebuilds
the JSON; ordinary invocation checks exact equality with it. The probe has21
physical witness controls,670 nontrivial packing cells and140 actual tail
controls in addition to the complete bank inequalities. Written proofs carry
the universal and countable assertions; fixtures alone do not. This is
same-author verification, not independent specialist or proof-assistant review.

The lower and upper remain separated. A stronger joint terminal response
could exclude excess patterns that this Bellman relaxation prices too cheaply;
a different feasible population might further lower the upper. No exhaustive
search of all support orientations, dimensions, dual policies or populations
is claimed. Re-running the inherited basis enumeration has no current benefit.
Source records, physics ledger and canon are unchanged; this toy construction
does not select a GU field grammar or validate a physical theory.
