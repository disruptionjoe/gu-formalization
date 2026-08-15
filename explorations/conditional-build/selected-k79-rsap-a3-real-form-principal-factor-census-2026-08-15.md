---
title: "Selected-K79 RSAP A3 real-form principal-factor census"
status: active_research
doc_type: exact_real_form_symmetric_pair_coverage_and_rank_census
created: "2026-08-15"
registry: lab/process/selected-k79-rsap-a3-real-form-principal-factor-census.json
probe: tests/channel-swings/selected_k79_rsap_a3_real_form_principal_factor_census_probe.py
grade: "ALL FIVE REAL A3 PRINCIPAL FACTORS CONSTRUCTED AT FACTOR GRADE; REGULAR NONSEMISIMPLE AND FIRST SINGULAR GATES PASS; CROSS-FORM GLUING OPEN"
canon_verdict_change: none
---

# Selected-K79 RSAP `A3` real-form principal-factor census

## Result first

The principal-factor census now covers all five real forms of complex `A3`:

```text
SL(4,R)/SO(2,2),
SU(4)/SO(4),
SU(3,1)/SO(3,1),
SU(2,2)/SO(2,2),
SU*(4)/SO*(4).
```

Each isotropy has real dimension six, each moving space has dimension nine,
and each cotangent factor has dimension eighteen. The four new factors cover
their complete real-form canonical types at reconstruction grade. Every
available regular nonsemisimple type has factor-map rank `15`; the compact
form has no nonsemisimple elements because its adjoint matrices are normal.
The first singular centralizer jump has factor-map rank `14` in all four
forms. Composed with the common leaf and four zero directions, every factor
therefore has the same exact schedule

```text
target/map: 84/91 -> 82/90 -> 72/85
             regular  first singular  origin.
```

All three rows saturate the `98D` pointwise RSAP bound.

The quaternionic case forces one correction to the candidate list. The
Cartan quotient `SU*(4)/Sp(2)` has a five-dimensional base and only a `10D`
cotangent factor, so it cannot cover a `15D` regular target. The relevant
maximal-rank pair is `SU*(4)/SO*(4)`: its `6+9` symmetric decomposition is
verified exactly, its paired non-real size-two Jordan control is regular at
rank `15`, and its first singular control has the required `15 -> 14` loss.

This closes factor construction, not cross-real-form gluing. Pairwise common
refinements, complete nonsplit singular atlases, deeper ambient strata, zero
charge and global all-strata RSAP remain open.

## Layer 0

This packet concerns classical Lie-algebra symmetric pairs and their
cotangent moment maps. It is not a particle-family, Higgs, index, chirality or
quantization calculation. The ordinary particle comparators remain outside
this lane.

## The three unitary constructions

Fix a real diagonal or congruent symmetric form `S` of signature `(p,q)`.
Writing an element of `su(p,q)` as `A+iB` gives

```text
A^T S + S A = 0,
B^T S = S B,
tr A = tr B = 0.
```

Thus

```text
su(p,q) = so(p,q) direct-sum i Sym_0(S;R).
```

The summands have dimensions six and nine, and the invariant real trace
pairing makes the second the annihilator of the first. Consequently

```text
T*(SU(p,q)/SO(p,q)) -> su(p,q)*
```

is an `18D` Hamiltonian factor for `(p,q)=(4,0),(3,1),(2,2)`.

For `X in su(p,q)`, the matrix `Y=-iX` is pseudo-Hermitian. Its canonical form
has real characteristic polynomial. Real Jordan blocks use reverse-identity
Gram blocks; non-real conjugate pairs use neutral real blocks. Choosing block
signs gives exactly the canonical types compatible with the ambient signature,
and congruence moves their Gram form to `S`. A central unit scalar corrects a
pseudo-unitary conjugator to determinant one without changing conjugation.
This is the same canonical-form mechanism already tested in `A2`, now
exhausted in complex dimension four.

The nine dimension-four configurations distribute as follows:

| form | compatible configurations | regular nonsemisimple control |
|---|---:|---|
| `SU(4)` | `1` | none; compact normality makes every element semisimple |
| `SU(3,1)` | `4` | `J3(lambda)+J1(mu)`, `lambda != mu` |
| `SU(2,2)` | `9` | `J4(0)` |

For `SU(3,1)`, the four compatible rows are real `3+1`, real `2+1+1`, real
`1+1+1+1`, and one complex pair plus two real lines. Signature `(2,2)` admits
all nine rows from the split predecessor. The probe computes this signature
census rather than extrapolating from semisimple eigenlines.

## The quaternionic construction

Let

```text
J = [[0,I],[-I,0]].
```

The real form `su*(4)` consists of trace-free complex matrices satisfying
`XJ=J conjugate(X)`. In `2 x 2` blocks every element is

```text
X = [[A,B],[-conjugate(B),conjugate(A)]],
Re tr(A)=0.
```

Ordinary transpose gives a real symmetric-pair decomposition:

- `X^T=-X`: `A` complex skew and `B` Hermitian, dimension six; this is
  `so*(4)`;
- `X^T=X`: `A` complex symmetric and `B` skew-Hermitian, with the trace
  condition, dimension nine.

The exact probe builds bases for both spaces, checks all dimensions and
transpose types, and verifies that their union has real rank fifteen.

Quaternionic similarity gives six canonical spectral/Jordan families in
`2 x 2` quaternionic dimension, including degenerations:

```text
two distinct non-real conjugate pairs;
one paired non-real size-two Jordan block;
one repeated non-real semisimple pair;
one non-real pair plus one real double eigenvalue;
two real double eigenvalues;
one paired real size-two Jordan block.
```

Each admits a complex-symmetric representative. The probe instantiates all
six and checks their full and moving centralizers. The only nontrivial block
needed beyond diagonal representatives is

```text
N = [[1,i],[i,-1]],     N^2=0.
```

Putting `iI+N` in the `A` block and its conjugate in the paired block gives a
regular nonsemisimple `su*(4)` control in the moving space. Exact centralizer
calculation gives

```text
dim Z_su*(4)=3,  dim Z_m=3,  factor rank=15.
```

A diagonal `A=diag(1+i,-1)` gives one non-real conjugate pair plus a real
double eigenvalue. It is the first singular control:

```text
dim Z_su*(4)=5,  dim Z_m=4,  factor rank=14.
```

This is the control the smaller Cartan quotient cannot realize at the required
rank.

## Rank calculation

For any of the four new pairs, at a moving covector `xi`,

```text
dJ(X,delta xi) = [X,xi] + delta xi,
X,delta xi in m.
```

Because `[m,m]` lies in the isotropy and the two symmetric summands are
disjoint,

```text
rank dJ = 9 + rank(ad_xi|m)
         = 18 - dim(Z(xi) intersect m).
```

The tested schedules are therefore:

| stratum | `dim Z_g` | `dim Z_m` | factor rank | target rank | full rank |
|---|---:|---:|---:|---:|---:|
| regular | `3` | `3` | `15` | `84` | `91` |
| first singular | `5` | `4` | `14` | `82` | `90` |
| origin | `15` | `9` | `9` | `72` | `85` |

The compact control is diagonal with one repeated eigenvalue. The `SU(3,1)`
controls use `R3+(1)`; the `SU(2,2)` regular nilpotent uses `R4`, while its
singular `J3+J1` control uses `R3+(-1)`. Varying the symmetrizer within its
fixed signature is a base-coordinate change in the same homogeneous factor,
not a new model.

## Claim ceiling and next gate

- All five real forms of complex `A3` now have a constructed `18D` principal
  cotangent factor at exact algebra/rank and canonical-form reconstruction
  grade.
- Regular nonsemisimple controls are explicitly tested wherever they exist.
- One first singular centralizer jump is explicitly tested in every new form.
- The wrong quaternionic Cartan quotient is excluded only as the principal
  RSAP factor; this is not an obstruction to `SU*(4)/SO*(4)`.
- Pairwise common refinements between distinct real forms have not yet been
  constructed. No cross-form primitive or moment cocycle is claimed.
- Complete nonsplit singular transition atlases, deeper `so(7,7)` strata,
  zero charge and global RSAP remain open.
- The same-sign `SL2/SO2` sheet remains partial and non-RSAP; the all-charge
  fallback remains `182D`.
- No canon, ledger, residue, quotient datum, physical interpretation or public
  posture changes.

Next classify the ambient `so(7,7)` embeddings and actual incidence relation
for the split and `SU(2,2)` `A3` factors. Their shared complexification and
signature-`(2,2)` Jordan census do not by themselves prove that their real
target strata overlap. Only if an ambient common domain exists should the
successor construct its refinement, compare the full moment map and
tautological primitive, and attempt a first noncommuting triple.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k79_rsap_a3_real_form_principal_factor_census_probe.py
```

The probe uses exact integer, rational and Gaussian-rational arithmetic only.

## References

- O. Taussky and H. Zassenhaus, “On the similarity transformation between a
  matrix and its transpose,” *Pacific Journal of Mathematics* 9 (1959).
- I. Gohberg, P. Lancaster and L. Rodman, *Indefinite Linear Algebra and
  Applications*, Birkhäuser, 2005.
- B. Kostant and S. Rallis, “Orbits and representations associated with
  symmetric spaces,” *American Journal of Mathematics* 93 (1971).
