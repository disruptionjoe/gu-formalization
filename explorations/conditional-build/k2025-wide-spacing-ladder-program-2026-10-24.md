---
title: "K2025: Wide-spacing ladder program, larger witnesses and a finite tail minimum"
status: active_research
doc_type: exploration
created: "2026-10-24"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact restricted thermal program and explicit feasible families; no unrestricted optimum, source physics, or novelty claim
scripts:
  - tests/channel-swings/k2025_wide_spacing_ladder_program.py
  - tests/channel-swings/k2025_wide_spacing_ladder_program_probe.py
---

# K2025: Wide-spacing ladder program, larger witnesses and a finite tail minimum

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: exact finite thermal family program and larger physical counterexamples
carrier: four-state bath times catalyst with declared full spectrum LAYER=toy CHIRALITY=N/A
pairing: positive normalized bath and catalyst density operators ON=declared_bath_catalyst
real_structure: rational energy and population witnesses with complex state space
grading: bath labels and physical catalyst energy levels, not Clifford grades
action_owner: repository-construction -- exact extreme channel and energy-conserving shell unitaries
target: catalyst return under exact channel and energy budget MAP-TYPE=intertwiner
```

## 1. Outcome and scope

[K2023](k2023-thermal-optimal-dimension-2026-10-24.md) settled sharp dimensions
on earlier contacts. Beyond spacing1/2, the current result supplies an exact
optimization program for a specified finite family, and then shows why that
family cannot be promoted to the unrestricted frontier. Larger13- and15-level
physical catalysts beat it across a full energy interval. Structural
follow-through gives a geometric-tail family with an exact **17-level minimum**:
adding further levels worsens this family's value. Its countable limit is
strictly worse than its17-level member.

This is not a general17-level optimum or a proof that an unrestricted optimum
needs finite or infinite dimension. The complete physical-spectrum problem
still lacks a matching lower bound here.

Freeze the inherited four-state bath with energies0,1,2,3, Boltzmann factor
1/2 and probabilities(8,4,2,1)/15; use the same exact extreme channel,
nonnegative catalyst spectrum with ground0, positive minimum spacing delta,
mean catalyst energy at most E, and inherited coherent-to-diagonal reduction.
Every displayed witness counts unoccupied completion levels in its dimension.
The exact shell-unitary construction applies after the reported capacity test;
it is not a diagonal-only relaxation substituted for channel feasibility.

## 2. The finite family and exact program

Use the complete [K2015](k2015-finite-thermal-ray-separation-2026-10-24.md)
canonical connected occupied-support census through energy9:26 supports,
183 orientation cells,3137 recorded vertices. For each support S choose the
consecutive physical completion0,...,Smax+1, extended to Smax+2 when the final
occupied gap is1. This explicit restriction excludes general holed completions.
Permit one such ladder, or two separated such ladders. For1/2<delta<1,
[K2006](k2006-uniform-two-component-spacing-2026-10-24.md) gives their least
relative offset Nlow-1+delta, where Nlow counts every physical level below.

Deduplicate vertex triples(energy,return,physical dimension), retaining1008
rays. Within each orientation cell, keep chords whose endpoint deficit signs
are compatible:4429 distinct relevant chords. On each sign-refined cell the
objective and energy are linear. A fixed-energy section attains its minimum
at a vertex or a chord joining two vertices of that cell. Across disconnected
ladders the return is additive and the cone is a direct product: a normalized
energy section needs at most two rays. The program therefore evaluates:

1. Every feasible single ray.
2. Every feasible same-cone chord.
3. Every ordered pair of separated rays, with its actual completion offset.

This is exact for this declared family. It is not a proof that every physical
catalyst has this form. The40 replayed rational parameter pairs have actual
normalized, spacing-valid, mean-valid full-spectrum witnesses. In particular,
E=13/10 selects a separated pair with20 physical levels; at delta=3/5 its
return is14587047/32891360. The numerical reference identifies the same
census cells used to reconstruct its populations and offset43/5.

## 3. A whole rectangle, beyond sampled parameter values

For every1/2<delta<1 and7/5<=E<=8/5, this finite family's exact value is

    L(E)=(3675-219E)/7640.                                (1)

It is attained by the same-cone chord on support(1,3,5,7,9) between

    p=(648,72,8,2,3)/733,   (e,R)=(945/733,651/1466),
    p=(144,16,4,6,9)/179,  (e,R)=(335/179,153/358).

The full physical spectrum is0,...,10. The lower certificate checks every
single ray at its smallest feasible budget, every same-cone chord at the
endpoints of its interval intersected with[7/5,8/5], and every separated
pair at four rectangle corners. After multiplying by its positive energy
span, a pair's difference from(1) is bilinear in E and delta. Its upper ray
always lies beyond8/5, so the feasible lower E endpoint is max(7/5,e).
Corner nonnegativity proves the whole rectangle, including the limiting
spacing endpoints for the algebra. This is a finite exact inequality
certificate, not interpolation of the40 successful examples.

## 4. Actual larger catalysts defeat the cutoff family

The report stores eight exact physical witnesses, with13 or15 levels, at
E=13/10,7/5,3/2,8/5. All eight improve their four sampled spacing comparisons.
A floating-point linear program proposed populations; rational active-equation
reconstruction and direct shell replay establish every accepted witness.
No optimizer tolerance is an acceptance criterion or replay dependency.

Moreover, endpoint populations share all shell maximizers and deficit signs,
so interpolation realizes the following affine curves throughout[7/5,8/5]:

    R13(E)=(12015-747E)/24892,
    R15(E)=(12145-757E)/25156.                           (2)

Both are strictly below(1), for every allowed delta, since their integer
full spectra have minimum spacing1. Minimum improvements over the interval
are25953/118859300 and27839/120119900 respectively. These counterexamples
refute unrestricted promotion of(1); they do not themselves prove an optimum.

## 5. Structural tail family and its exact finite minimum

The larger witnesses reveal a family that can be summed, avoiding an endless
sequence of finite-cutoff experiments. For integer m>=0, use full physical
spectrum0,...,2m+10 (dimension2m+11), occupied energies1,3,...,2m+9, and

    p0=9u, p1=u, p2=(u+4v)/10, p3=v,
    p_(4+k)=(3v/2)9^-k, k=0,...,m.                     (3)

Put q=9^(-m-1), a=101/10, c=25/2,

    b=247/80-27q/16,
    d=1575/64-27(8m+45)q/64,
    Delta=ad-bc,
    u=(d-bE)/Delta, v=(aE-c)/Delta.                     (4)

The finite geometric identities
sum9^-k=9(1-q)/8 and sum k9^-k=9[1-(8m+9)q]/64 prove normalization and
mean E. Delta is positive:640Delta=134375-27q(808m+4045), whose subtracted
term decreases with m. Also v>0. The ratio u/v increases with m because
each new tail term contributes a positive multiple of9+2k-E; it decreases
with E since its derivative has numerator bc-ad<0. Its uniform bounds are

    8/3 < 893/183 <= u/v < 32459/2624 < 36.             (5)

These inequalities fix the shell order: the first two occupied edges point
one way, the next two the other way, and the remaining tail edges the first
way. Direct bath-label deficit calculation gives positive deficits only at
p0 and p4, each half its population; all other deficits are zero. Thus

    R_m(E)=[64875-4044E+1215q(4E-8m-45)]
           /[134375-27q(808m+4045)].                    (6)

There is no hidden completion cost: alternate occupied levels of the full
consecutive spectrum pass every bath-shell capacity inequality, including
both ends. Equations(3)--(6) apply to every E in[7/5,8/5] and every positive
delta<=1. m=0 gives(1), m=1,2 give(2).

The family is NOT monotone in dimension. To classify every m, put

    A=64875-4044E, B=1215(4E-45), C=-9720,
    D=134375, c0=21816, d0=109215,
    alpha=A c0+D C, beta=A d0+D B, h=c0 B-C d0.

After multiplication by positive denominators, R_(m+1)-R_m has the sign of

    -8 beta+alpha(1-8m)+q h.                            (7)

Exact endpoint tests suffice because these expressions are affine in E.
For m=0,1,2 expression(7) is negative. For all m>=3 it is positive:
alpha<0, h>0, and -8beta-23alpha>0 across the entire interval. Therefore
**m=3, dimension17, is the unique minimum within family(3)**. Its line and
exact populations are in the report. At E=7/5 it gives2247813/5101040;
at E=8/5 it gives4434219/10202080.

The countable limit of(3) is a normal finite-mean catalyst on the integer
completion spectrum and has

    R_infty(E)=(64875-4044E)/134375.                     (8)

The inherited countable shell construction applies; finite family members
converge at O((m+1)9^-m), uniformly on this energy interval. But(8) lies
strictly ABOVE the finite17-level value. Hence an intuition that an infinite
tail must be best is refuted for this family. This does not settle the
unrestricted finite/countable frontier; K2008 already establishes its general
finite approximation relation, which is not counted as new here.

## 6. Verification and remaining question

The producer computes the finite program, physical witnesses, rectangle,
affine extensions and family sign certificate. The separate checker obtains
return deficits directly from bath-label shell maxima, reconstructs all3137
vertices and4429 chords, checks every candidate inequality for all40 rows,
checks the whole rectangle, and verifies the larger and tail witnesses.
The universal result uses(5),(7) and geometric summation, not a finite-m scan;
18 explicit tail endpoint witnesses and32 successive-difference identity
checks per energy endpoint are finite controls. Deliberate completion,
normalization, spacing and return faults must fail. Provenance hashes are
counted separately. These are same-author separate implementations, not
external review or proof-assistant certification.

Strongest hostile objection: one or two consecutive completions omit relevant
spectra and tails. Section4 proves the objection concretely rather than
masking it. Strongest residual risk: confusing the family minimum with a
physical optimum. The report and this note keep those claims distinct.
Next useful problem: obtain a global certificate or a better feasible
construction against the17-level line, allowing holed completions, larger
connected supports and multiple components. The generic lower bound
63/100-3E/20 remains separated here; no matching bound is asserted.
Source register, GU physics ledger, canon and inherited claim statuses remain
unchanged. This thermal toy calculation does not select a GU physical state.
