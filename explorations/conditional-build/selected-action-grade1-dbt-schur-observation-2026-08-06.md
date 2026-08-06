---
artifact_type: exploration_result
created: 2026-08-06
status: EXACT_FINITE_SOURCE_SYMBOL__GENERIC_GRAPH_EINSTEIN_MATCH_RETRACTED__DISCRETE_TWO_MODE_CAUSAL_CANDIDATE_OPEN
ledger: lab/process/conditional-physics-ledger-v0.36.json
registry: lab/process/selected-action-grade1-dbt-schur-observation.json
---

# Selected grade-one completion, source Schur symbol and observation

## Outcome

The first source-required adjacent Clifford bank changes the gravitational
answer.  The earlier constant-torsion graph theorem remains correct on its
declared subspace, but it is not the principal symbol of the completed source
action.

The complete grade-one bank has dimension 196 and an exact nondegenerate
algebraic Hessian.  Eliminating it produces a live second-order Schur
correction on the native source variables `(g,varpi)`.  At the normalized
choice `kappa_1^2=1`, the corrected timelike, spacelike and null symbols all
have rank 30 with only the rank-four diffeomorphism radical.  In particular,
the two graph-only null tensor modes are lifted.

This is not an ultimate kill.  The quotient determinant has three positive
null exceptional values.  Exactly one is a two-extra-mode locus:

```text
N2(z) = z^2 + (1352/615) z - 1178198372/69047075
z = kappa_1^2
positive root = 3.17537838044882...
```

`N2` is coprime to every timelike and spacelike characteristic factor, so its
positive root is a genuine finite causal candidate rather than an everywhere-
characteristic collision.  But the two source modes' metric projections are
not the original graph TT plane modulo gauge.  Null little-group type, Green
form, positivity and global domain remain open.  Ledger row `LT-GR1` therefore
moves from `SAME/DERIVED_CONDITIONAL` to `NEEDS/MISSING_CONSTRUCTION`; no
coefficient or residue reduction is booked.

## Layer 0

Five objects must not be collapsed:

1. the raw curvature coupling from `<T,S(F_B)>`;
2. the formal-adjoint cross from `<T,S(d_B T/2)>`;
3. the grade-one algebraic Hessian;
4. the source-variable pullback `T=varpi-B_LC(g)`;
5. the observation pair `(s* T,res_s^V T)`.

The previous wave computed item 2.  Using it alone would produce a partial
Schur correction and the wrong source symbol.  Item 1 contributes a separate
metric-to-grade-one term and is load-bearing.

## Source return

`SOURCE-CONFIRMS_AND_SOURCE-SILENT`.

The source and its repo reinspection confirm that `T` is the full
adjoint-valued connection difference and that the source-compatible observed
field retains both ordinary pullback and vertical coefficient restriction.
The source does not publish the grade-one Hessian, the cross ranks, the
coefficient factors, the physical mode identification or a common domain.

## 1. Exact grade-one Hessian

On `V* tensor V`, define the metric transpose

```text
tau(A)_(mu a) = eta_mu eta_a A_(a mu).
```

The complete invariant decomposition is

```text
V* tensor V = 1 + Sym^2_0 + Lambda^2
dimensions      1      104        91.
```

Relative to the native pairing, the selected stationary-branch Hessian has
eigenvalues

```text
-kappa_1,  (15/13) kappa_1,  (41/39) kappa_1.
```

Its invariant inverse is therefore

```text
H_1^{-1} = [-P_1 + (13/15)P_sym0 + (39/41)P_anti] G^{-1}.
```

For positive `kappa_1`, its inertia is `(97,99)`; changing the sign swaps the
two counts.  Nondegeneracy is exact, but positivity is false.  The hostile
rerun checked all `196^2` entries of the selected Hessian against this
projector formula.

## 2. Correct source-variable cross

Let `F(k)` be the raw grade-one/connection coupling from the curvature term
and let

```text
E(k) = (F(k)-R(k))/2
```

be the formal `d_B T/2` Euler cross, where `R` is the reverse pairing.  With
`b=L(k)g` and `delta T_Cl2=delta varpi_Cl2-b`, the grade-one equation couples
to source variables through

```text
W_g = [F-E] L = (F+R)L/2,
W_varpi = E,
W = [W_g | W_varpi].
```

This is the source-chain correction that a `d_B T`-only Schur calculation
misses.  It passes the exact principal Ward identity:

```text
F L D = 0,
W [D ; L D] = 0.
```

The causal ranks are:

| covector | `rank E` | `rank W_g` | `rank W` | `rank W^T H_1^-1 W` |
|---|---:|---:|---:|---:|
| timelike | 12 | 4 | 13 | 13 |
| spacelike | 12 | 6 | 15 | 15 |
| null | 11 | 7 | 15 | 14 |

The null drop from `rank W=15` to Schur rank 14 is an exact isotropic-image
effect.  Raw rank is not substituted for the reduced quadratic-form rank.

## 3. Observation does not erase the block

The horizontal pullback rows alone retain ranks `12/14/14` of `W`; the
vertical coefficient rows have rank one and raise the complete paired ranks
to `13/15/15`.  Thus the source-compatible pair preserves the cross.  The
observed construction must carry the grade-one equations/field; it cannot
salvage the old 34-variable truncation by ordinary pullback.

This proves finite algebraic preservation only.  It does not prove global
descent, faithfulness or a physical normal equation.

## 4. Schur pencil and coefficient locus

For nonzero `kappa_1`, the algebraic Hessian and graph principal symbol scale
as `kappa_1`, while `W` is coefficient-independent.  Multiplying the Schur
operator by `kappa_1` leaves the kernel unchanged and gives the rational
quotient pencil

```text
M(z,k) = z P_0(k) - Q(k),
z = kappa_1^2,
Q = W^T H_1^-1 W.
```

Sage independently factors the exact 30-dimensional quotient determinants.
For a null covector the nonzero part is

```text
z^22 N1(z) N2(z)^2,
N1(z)=z^2-(3016/3)z+4183088/369,
N2(z)=z^2+(1352/615)z-1178198372/69047075.
```

`N1` has two positive roots, approximately `11.4055` and `993.9278`, and
each adds one nongauge source mode.  `N2` has one positive root,
approximately `3.175378`, and adds two.  Both null factors have gcd one with
every nonnull factor.  This makes the positive `N2` root the unique two-mode
causal candidate in this finite bank.

The result does not yet fix `kappa_1`: the two modes have not been typed as the
physical spin-two representation, their Green form is unknown and other
source banks/common-domain effects can still alter the characteristic set.

## Specialist preassessment and hostile disposition

- Representation theory supplied the `1+104+91` invariant inverse.
- Differential geometry forced the extra `F_B` metric cross.
- Variational PDE fixed the source chain and Schur sign.
- Symplectic geometry forbids treating auxiliary elimination as a quotient
  and retains the Green/preboundary obligation.
- Observation geometry forced the paired receiver rather than horizontal
  pullback alone.
- Exact computation used rational SymPy plus an independent Sage
  factorization and number-field kernel check.
- Operator theory keeps the common right-H/Krein domain open.
- Source criticism returns confirmation plus silence, not attribution.
- Constraint accounting adds no field, datum, quotient or parameter.
- Epistemic review retracts the graph-only full-action reading rather than
  defending a superseded 34-variable carrier.

## Boundaries and next gate

No BV/symplectic quotient, Green hyperbolicity, positive energy, unitarity,
Einstein equation, cosmology or particle result is claimed.  P1/P2/P3 remain
unused.  Curt remains formally separate and no third lane is promoted.

The next highest-information gate is:

```text
TYPE_THE_POSITIVE_N2_TWO_MODE_KERNEL_UNDER_THE_NULL_LITTLE_GROUP
AND_ITS_GREEN_FORM__THEN_TEST_THE_COMMON_RIGHT_H_KREIN_DOMAIN_AND
ODD_BV_BFV_TOTALIZATION
```
