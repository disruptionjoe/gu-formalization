---
status: process
doc_type: internal-specialist-review
created: 2026-11-26
claim_effect: none
---

# Internal review of matched weak coefficients

Basis: 139873dd462fe8bc99774a82cdb7a6ecc0f09c00. These are internal agent reviews, not external peer review or Lean certification. Root executed the recorded exact calculations serially.



# Independent review — star-free exact engine and 120-dimensional trial closure

Reviewer: full-weak-formula specialist. Read-only review of `inverse_fast_exact.py`,
`inverse_stage3_basis.py` and `inverse_stage4_closure.py` against the owned
`source_action_deep_algebra.py` and actual K95 frame. No heavy jobs run. This
review concerns algebra and certificate structure; it does not assert that the
120-dimensional closure run passes.

## Verdict

**The native K95 formulas and exact elimination logic are sound.** Add explicit
Hodge-parity scope and bind resumable checkpoints to their exact inputs before
calling a completed closure result a durable certificate. The155 controls are
regression samples; the component derivation below is what establishes the
formula for arbitrary Clifford coefficients. A failed120-space closure is an
exact trial-space failure, not a failure of source GU or of the full spin5
operator.

## 1. Component derivation of the fast map

Let theta_i be the rational orthogonal coframe, metric entries d_i nonzero,
q the number of negative entries, and W_ij the coefficients of a two-form for
i<j. Extend W antisymmetrically when indices are reversed. The actual engine
uses phi1=sum_i theta_i gamma_i and phi2=sum_(i<j) theta_i theta_j gamma_ij.
All Clifford products below are ordinary commutators/anticommutators, as in the
owned `Engine.cliff_product` parity rule.

For the first Hodge term, the component contraction identity at degree2 is

    *^-1(theta_i wedge *W) = - i_(e_i/d_i) W.

Thus its contribution to output j is minus sum_i [gamma_i,W_ij]/d_i. Summing
only i<j gives precisely the code's opposite contributions to slots i and j.

For the second term, outer *^-1 * cancels exactly. The inner top-form Hodge
operation gives

    * (phi2 wedge_anti *W)
      = (-1)^q sum_(i<j) {gamma_ij,W_ij}/(d_i d_j).

Consequently, with Z the displayed sum,

    (Phi W)_j = -sum_i [gamma_i,W_ij]/d_i
                + ((-1)^q/2) {gamma_j,Z}.

The native K95 has q=5, so the coefficient is -1/2, exactly as implemented.
K77 also has odd q, but equality of this component sign is not an identification
of metrics, carriers or source operators. **Do not label the current hardcoded
formula valid for every14D signature:** for even q the second sign changes
under this same engine convention. Safest current guard is dimension14 and odd
negative index (or directly the native diagonal); alternatively carry
`(-1)**self.negative/2` explicitly in both Phi and Phi_adj and verify each
newly admitted signature. No such extension is needed for this wave.

## 2. Exact adjoints and cubic derivative

The pairing is the complex-bilinear extension of the native real trace/form
pairing, not a positive Hermitian pairing. Cyclic trace gives

    <[A,X],Y> = -<X,[A,Y]>,
    <{A,X},Y> = <X,{A,Y}>.

After the form weights are raised/lowered, the adjoint is

    (Phi* V)_ij = [gamma_i,V_j]-[gamma_j,V_i]
                  + ((-1)^q/2) {gamma_ij,A},
    A = sum_k {gamma_k,V_k}/d_k.

This is the implemented Phi_adj at q5. No Hermitian conjugation of the
Gaussian-rational coefficients should be inserted: that would change the
admitted action pairing.

For Q_U(V)=U wedge_comm V, cyclicity and the one/two-form weights give its
adjoint components as

    (Q_U* W)_j = -sum_i [U_i,W_ij]/d_i.

Again the i<j assembly in `wadj` is correct. Therefore

    N(U,V)=1/6 (Phi Q_U(V)+Q_U* Phi*V+Q_V* Phi*U)

matches the owned engine for arbitrary coefficients of the stated carrier.
The existing155 exact sample comparisons are valuable checks of sign, index
and implementation against the independent star implementation. They do not,
by themselves, exhaust every2-form/Clifford input. The derived identities make
that exhaustion unnecessary if preserved with the certificate. It would also
be cheap to include the bilinear adjoint identity on additional mixed inputs
and one deliberately wrong second-term sign as mutation controls; this is a
strengthening, not a new mathematical premise.

## 3. Trial basis and reduction

The raw2176 coordinate support was numerically discovered. Stage3 then imposes
K_dt=0, J01=5i and the raising-annihilation condition by exact Gaussian-rational
elimination. Its120-dimensional result is an exact finite trial space in that
support. Both actual source seeds are checked to lie in it, independent of the
numerical solution coefficients.

The second reduction normalizes each successive basis vector at a new pivot,
with zeros at every earlier pivot. The stored pivot order is insertion order,
not necessarily sorted order; stage4 retains the same order. Forward reduction
is therefore valid even though earlier basis vectors may have later-pivot
entries. The produced cs satisfies w=sum_i cs_i b_i+remainder. A nonzero
remainder proves that w is outside this trial space. It need not be a coordinate
outside the original2176 support to be a genuine nonmembership witness.

Recommended cheap structural checks before resume:

- len(pivots)=len(basis)=120, distinct pivots;
- each basis has pivot1 and zeros at all previous pivots;
- exact reproduction of both source-seed coordinates;
- optional exact reconstruction of every stored closure column from its basis
  coordinates when replaying a completed certificate.

## 4. What the closure loop proves

Each column computes the *full native* P(2N(T_j,b_i)) before reduction, not a
projection into the guessed space. Thus zero remainder for all120 basis
vectors and all59 independent affine background coefficients proves invariance
under every M(x)=I+sum_j x_j A_j in the admitted homogeneous59 family. Identity
preserves the space automatically. This is stronger than root-center closure.
The exact actual P is the existing nondegenerate-kernel projection, built by
full28-coordinate XOR blocks and their pairing Gram; no positive metric is
substituted.

A completed family-closure certificate means that a120x120 affine matrix can
solve this source-generated subproblem exactly. It is not a classification of
all1048 highest5 multiplicities or all49154 auxiliary directions. If the block
is invertible, its solution is a full-carrier particular solution for these
sources. To identify it with a unique full reduction still needs either full-M
regularity or source/goal kernel-compatibility; a kernel outside this block may
make an unrestricted scalar goal ambiguous.

## 5. Checkpoint integrity correction

The current resume path checks only `dimension`. That is insufficient for a
reproducible exact certificate: a stale checkpoint with the same120 dimension
could come from another basis, background order, source revision or helper.
Before resuming, bind and verify hashes of:

1. ordered basis and ordered pivots;
2. ordered59 background coefficients and their basis revision;
3. exact source seeds (or the basis-stage evidence);
4. the native source/operator/projection code and fast-engine code.

Also require completed=len(columns), 0<=completed<=120, every stored basis entry
has59 maps and every column has120 exact coefficient pairs, and no persisted
failure record. Appending a new basis column only after all59 pass is correct.
Atomic checkpoint replacement is preferable; it protects an expensive exact
calculation against a partial write. None of these checks changes scientific
scope or creates governance.

## 6. Root-ball inverse certificate

Once all closure columns pass, form the exact affine coordinate matrix at each
root center. A rational approximate inverse R0 supplies a standard enclosure:

    eta = ||I-R0 M_center||_infinity
          + radius * sum_j ||R0 A_j||_infinity < 1.

Then for exact source-coordinate vector s, y0=R0 s,

    ||y-y0||_infinity <= eta/(1-eta) ||y0||_infinity.

Use the actual stored root certificate's coordinate-box norm/radius. This is a
coordinate norm for the declared basis, not a physical norm. Root centers,
matrices and candidate R0 must be exact rational/Gaussian-rational values at
acceptance. Numerical residuals alone do not bound inverse error.

The current full weak kernel also depends on T directly and on already-solved
6/7 responses. A final current certificate must propagate *all* those errors,
including products of T-error with inverse-response error and the inherited
cross-Gram range. The full matched sum must be certified; separated nonzero
axis terms are insufficient.


# Independent review of the matched weak coefficient reduction

Reviewer: domain/support specialist, read-only. Basis GU `139873dd462fe8bc99774a82cdb7a6ecc0f09c00`. Reviewed `full-weak.md`, `full_weak_helpers.py`, native paired-response and receiver-strategy derivations, and the closed-time reduction. No heavy computation or native edits.

## Disposition

**Conditional mathematical PASS.** The formula is a valid reduction of the complete pointwise diagonal weak coefficient provided the stated smooth local SO3-equivariant auxiliary solution family exists and solves the full residual without relevant ambiguity. Pointwise finite spin5 invertibility alone does not establish that premise. Do not present the resulting coefficient as an integrated constrained response or physical observable before support/domain obligations are met.

## 1. Summed moving correction

The safe decomposition is

    j_eff(V) = j_seed(V-Y0V+W(V)) + sum_a (partial_a j_raw)(Y^aV),

where the derivative in the second term holds the native frame coefficients of its test connection fixed. **W must contain every current-independent coefficient/lift correction** from the product rule: moving Y and P, the coordinate-time covector's variation in the moving frame, density/frame divergence, induced R-connection, and any identification/vertex derivative not already retained in the fixed-frame current derivative. Individual terms need not vanish or preserve a single type.

Closed coordinate dt is invariant under spatial SO3. The homogeneous background, its actual displacement, metric, native pairing, symbols, projectors and canonical Nomizu identification are SO3-natural. The spatial-plus-normal divergence omits physical time in an SO3-invariant way. A smooth equivariant auxiliary solution family therefore makes the *contracted sum* W a linear SO3 intertwiner on the range test V. It sends a highest-spin7 vector to the full highest-spin7 connection space.

The native complete36-vector highest7 carrier is normal-only and gamma-traceless; the existing current control proves the section map q(At)^-1 VERTEX(w)I vanishes on it, including both range and kernel sectors. This is stronger than merely knowing blindness on the tested highest7 kernel. Multiplication on the left by any existing cross-Gram inverse preserves zero. Thus j_seed(W(V)) and the equivariantly solved highest7 lower response vanish.

The old A01 state space is not covariant, but that does not invalidate this specific step: W is constructed from **bosonic constraint geometry**, not the matter seed. At the section the derivative-free q/At/I current map is SO3-equivariant. The seed's symmetry breaking remains precisely in its normal derivatives, which the formula retains.

## 2. Current derivatives and surviving axes

In the owned normal frame, the vertical Nomizu coefficients vanish at the origin. A fixed-frame normal connection test is B-parallel there; its vertex derivative is zero in this identification. Tangential-to-A01 seed column derivatives vanish, while the row derivative is

    Q_a = -Q (At)_a (At)^-1.

The actual `(At)_a` is determined by the normal matrix row3. Hence axes5,6,9,11 are zero;4/7 reduce to the already blind highest7 current. Axis13 has SO3 weight0, so its source on a weight7 vector has weight7; with no spin8 carrier it is highest7 and blind. Axes10/12 can have weight6 and remain. Axis8 is the CK solving direction and requires the full owned row/column jet, not an additional tangent correction.

The checks in `source_controls` are appropriate: explicitly verify source weights, Casimir types, `src12=i src10`, and the spin5 relation `src8=i src5`. Do not infer these signs from naming conventions. Static inspection of the native frame matrices supports the proposed signs.

The helper's tangent matrix implements the minus sign in `-Q At'_a At^-1 U I`. Since A03 and A13 have row3 entries `-e0` and `-e1`, the final displayed correction has plus signs. The full imaginary-variation and independent-row phases must be applied only after summing all terms and then taking the relevant Hermitian/polarized current.

## 3. Inverse helper scope

The known6/7 solve correctly records positive `u=M^-1source`, opposite the older energy convention `c=-M^-1source`. Weight5 lowering factors12 for spin6 and14*26=364 for spin7 match the usual invariant-pairing ladder norms; root must retain exact existing basis/inverse hash checks. The spin5 contribution remains unsolved by this helper. Residual certification must cover the full native source, not only projected coordinates.

The scalar-adjoint theorem can avoid full global M invertibility, but does not automatically yield the smooth equivariant family needed for derivatives of Y. Either establish that family on the reached module or state the pointwise result conditionally. Compact-group averaging can preserve equivariance of an already existing smooth right-inverse family, but it does not prove the missing range/constant-rank/domain facts.

## 4. Separation from the E2 witness

The invisible E2 trace-seed witness does not lie in the old A01 completion. This matched calculation belongs to the old diagnostic pair and cannot transport E2 into its positive graph or support conditions. A nonzero coefficient would be new candidate-level information; physical admission, admissible constrained test support and the full propagated response remain separate.

No mathematical blocker was found beyond the explicit family/domain premises. Numerical or exact checks are root-owned and were not rerun by this reviewer.


# Independent T2 review: exact selected matched-response coefficient

Review target: LB-CLASS / 5q.1, held W2/K95 SE=-1/2 candidate.
Tier: T2. Expected delta: independently assess the selected-coefficient
certificate and its claim ceiling. Kill condition for this certificate: an
omitted matched-current term, an underestimated input/product error, an
incorrect Clifford adjoint, or a claimed physical/domain consequence beyond
the established inputs. Actual delta: no blocking defect found in the reviewed
selected-coefficient algorithm; saved root-0 arithmetic is consistent. This
review does not complete or rerun the parent's exact root evaluation.

## Reviewed snapshot and method

Native basis: `139873dd462fe8bc99774a82cdb7a6ecc0f09c00` in
`/private/tmp/gu-weak-response-wt-20261126`.
Reviewed weak-response probe SHA256:
`f70e6e41d9486d301b0ea00a609cc0c20caa868fb35106cff27d524f4b985b5c`.
Owned paired-response probe SHA256:
`72f131477d041c19293a7e191fd099fbe637597e685ac1d84dfe76db8beb8655`.

Read local instructions, program-focus/semantic routing, the K95/K77
distinction, domain path-dependency, and the current native paired-response
and domain constructions. Inspected `MatchedCoefficients`, `MatchedInterval`,
`mode_exact`, source/inverse assembly, Ball operations, the owned Czero,
Clifford product and matter-symbol implementations. Read the scratch written
proofs `full-weak.md`, `inverse-contracted-jet.md`, `domain.md`, and
`starfree-closure-review.md`. No native writes, engine execution, heavy jobs,
or parallel verification were performed. The only arithmetic execution parsed
saved results and checked their exact rational margin identities.

## 1. Target-product enumeration and error propagation

For the ordered Clifford basis, `gamma_a gamma_b = s(a,b) gamma_(a xor b)`.
At target c, b is uniquely a xor c. Iterating the smaller support and looking
up the other support enumerates every contributing ordered pair once. The
branch iterating B still calls `cmul(a,b)`, preserving order and signs. No
full convolution or omitted target contributors are needed.

Ball(c,e) encloses complex perturbations in the coefficient l1 norm
`|Re(delta)|+|Im(delta)| <= e`. Its multiplication radius is

    ||c1||_1 e2 + ||c2||_1 e1 + e1 e2.

Submultiplicativity and the triangle inequality prove this bound. Rational
Clifford factors are exact and multiply the radius by their absolute value.
Addition, negation and division by a nonzero exact real rational preserve
the enclosure. Correlations between repeated inputs are discarded safely;
they can make the bound wider, not narrower.

The potentially dangerous zero-center case is handled correctly.
`MatchedInterval.balls` takes the union of center and error keys. Ball truth
tests return true when either the center or radius is nonzero. Therefore the
lookup tests in `target_ball_product`, and the native sparse clean/scale/add
operations, retain error-only entries. Neither a cancellation at the center
nor a zero center coefficient silently removes its uncertainty.

The 120-space reconstruction sums epsilon times each basis coefficient's
complex l1 norm. Known spin6/7 reconstruction uses the inherited exact
Neumann bounds and lowering factors. Real and imaginary extraction each use
the full complex error envelope, a conservative valid bound. Multiplication
by i to assemble the axis-8 source does not change this norm. T errors include
the radius contribution from every background coefficient, including keys
that cancel at the center. The interval calculation includes the products
between T uncertainty and auxiliary-response uncertainty automatically.

## 2. Factored matrix coefficient and Hermitian convention

`C_row(i)` and `U_row(i)` evaluate the corresponding 15-slot operator rows
on scalar Clifford basis columns. Multiplying these row coefficients by the
15 coefficients of `ZU_col(j)` or `ZC_col(j)` in the stated order gives exactly
the selected coefficient of Q C Z U J minus Q U Z C J. This is the same
operator composition as the native full-jet formula.

The Hermitian adjoint reverses Clifford order and conjugates scalar
coefficients. Since gamma_a dagger equals sign(d_a) gamma_a in the held
representation, the sign is

    (-1)^(r(r-1)/2) product_(a in c) sign(d_a).

The owned `adj_sign(c)` implements this sign. Both engines swap matrix
indices, conjugate the opposite coefficient, and divide the sum by two.
Conjugation preserves the Ball radius. This checks both the off-diagonal
entry and its partner, rather than incorrectly Hermitianizing one entry
alone. Physical i-variation and the independent row's i phase would produce
the previously stated overall minus; that does not change nonvanishing of
the reported unnormalized Hermitian matrix coefficient.

For center v and radius e, `max(|Re v|,|Im v|)-e > 0` is a sufficient strict
nonzero certificate. The weighted margin uses a lower square-root bound for
the center and an upper square-root bound for the error. This remains a
single-coefficient certificate. It does not imply the old all-Gram inequality.

## 3. Native lower, seed and tangent terms

`MatchedCoefficients.C` calls the owned `p.Czero(T, field)`, which includes
spin plus displacement, the covector-slot Nomizu bracket correction and the
scalar-divergence correction. No scalar-slot Dirac replacement is used.

`linear_col` includes all non-solving normal row-seed derivatives of
q(At)^(-1) appearing in the owned `full_jet`. It then subtracts the independent
axis10/12 fixed-u tangent-current terms with their actual At-prime symbols.
The solving-axis8 current derivative is not added twice. The sources use the
positive M-inverse sign, the exact phase relations are checked at source
level, and spin6/spin7 lowering uses 12 and 14*26=364 where appropriate.

The selected calculation is at diagonal zero base frequency. Neither a
claim for arbitrary frequency nor an all-Gram result follows from it.

## 4. Formal contracted-jet and domain ceiling

The contracted-jet argument is sound as the stated algebraic implication:
given the authenticated pointwise responses and their equivariant extension
on the tested source representation, the full contracted right-hand side
of differentiated MY=L is highest7. The complete N7 inverse assigns its
highest7 formal correction, and the inherited complete highest7 current
blindness kills this contracted contribution. Keeping the induced range,
normal-index and density connections is essential. The argument concerns
the whole sum, not separately vanishing derivatives.

This does not solve every uncontracted first-jet equation or construct a
smooth family. Nor does the invertible 120-space exclude a full highest5
kernel outside that space. The derivative-of-current covector could see
such a kernel. The proposed full-residual adjoint goal directly addresses
that remaining uniqueness question; projecting a residual into the trial
space would not suffice.

The report and JSON correctly retain these limits: a formal pointwise
coefficient for selected particular auxiliary responses; no smooth-family,
complement-kernel-independence, all-Gram, integrated-support, physical-ghost
or source-GU conclusion. The exact E2-to-A01 nonmembership independently
prevents transferring this certificate to the invisible-history witness.
K95 and the source's asserted K77 remain distinct, and the held W2 action is
not promoted to a source-selected necessity or all-class-C test.

## 5. Saved evidence inspected and small reporting correction

At review time the saved exact file contained root0, both realifications.
I independently checked the rational identities for its margins and boolean
flags, without rerunning the native engine:

| Root/part | Target (i,j,c) | Weighted interval margin | Coarse global-HS test |
| --- | --- | ---: | --- |
| 0 real | (3,4,1910) | 849.6192237287592 | inconclusive |
| 0 imag | (3,4,3446) | 849.6192259580309 | inconclusive |

The saved rearrangement-control count is 322; execution of those controls
belongs to the parent record. No completed root1 result was present when
this review was saved. Report all four cases only after the parent's job
finishes and those records are inspected.

Nonblocking reporting fix: the console line currently prints `PASS` from
`lower>0`, which is the coarse global-HS criterion, while JSON's
`certified_nonzero` correctly uses the selected interval margin. Label both
criteria explicitly so a successful selected-coefficient certificate is not
displayed as an unexplained failed test.

## Review disposition

Accept the reviewed implementation and written reduction at their stated
formal-particular-response scope, subject to the parent's completed native
execution and required gates. There is no independent proof-assistant,
external-expert, full-domain or source-necessity certification in this review.

## Completion addendum: all four saved exact cases

The parent subsequently completed the exact coefficient job. I inspected the
complete saved `matched-exact-coefficient.json`, SHA256
`364abc91ab7765ec10e11d8ed5efc29458e346be597aaad090c0cb09e7babff4`.
It contains both root records and both realifications in each record:

| Root/part | Target (i,j,c) | Weighted interval margin | Selected nonzero | Coarse global-HS test |
| --- | --- | ---: | --- | --- |
| 0 real | (3,4,1910) | 849.6192237287592 | true | inconclusive |
| 0 imag | (3,4,3446) | 849.6192259580309 | true | inconclusive |
| 1 real | (3,4,4981) | 1578.3592748435815 | true | inconclusive |
| 1 imag | (3,4,1909) | 1578.3595264112942 | true | inconclusive |

All four stored exact rational selected margins are positive, and each saved
`certified_nonzero` flag is true. All four `global_norm_certified_nonzero`
flags are false. The completed saved record therefore supports the four-case
selected-coefficient statement under the implementation review above; it does
not support the coarser global-HS certificate or an all-Gram conclusion.

This addendum supersedes only the earlier note that root1 was pending.
It is saved-result inspection, not an independent engine rerun or a new
calculation. All formal-particular-response, kernel, smooth-family, support,
integration, physical and source limits remain unchanged. The parent will
correct the console labels and owns the remaining native gates.

## Separate exploratory-test review: scalar-goal representer membership

Reviewed prepared scratch `scalar_goal_membership.py`, SHA256
`a0ad9d00d796fe185329e5572d4240dfe7506a67bc75210615aa45f38f48ac6f`,
and `scalar-goal-membership-plan.md`. This is static review only: no helper,
control, functional extraction, projection or membership test was run by
this reviewer. The target is the specified highest5 ambiguity of the real
Hermitian coefficient (3,4,1910), not a Tier-1 or physical/source result.

### Transposed coefficient functional

For fixed T, write Z=(A8)^(-1), Q=q(At)^(-1), and D for the owned row-seed
tangent correction. The u8-dependent part is

    Q(C+D) Z U(u8) J - Q U(u8) Z C J.

The first/Q rows prepared from the 15 scalar carrier columns are the correct
left Clifford coefficient matrices of the right-Clifford-linear fixed maps.
For an identity-valued injected slot, U(u8)J is a left polynomial times each
unknown connection component, so the first term can place that unknown to
the right of its computed left coefficient. The second term's five explicit
vertex contributions reproduce the native formula with the correct outer
minus sign: minus slash-U times z, plus the covector contraction, minus U nu,
minus U z/d in the scalar slot, and plus slash-U nu/2 there.

For a sandwich L gamma_d R, d=l xor r xor target is the only possible input
blade for each pair of fixed blades. `target_sandwich` evaluates `cmul(l,d)`
and then `cmul(l xor d,r)` in order, retaining both metric and sign factors.
There is no illicit commutation of the unknown Clifford coefficient. The
grade0/3 restriction matches the stated native imaginary-variation sector.
`T` must be the displacement only: Czero already adds the spin form.

For real T and real input coefficients, the raw covector coefficients are
real. Thus the real Hermitian-coefficient functional is one half of raw_ij
plus adj_sign times raw_ji. Its complex-linear extension has the same real
coefficients. This deliberate extension is correct; conjugating the unknown
complex argument would define a different map. The u10/u12 terms are fixed
affine offsets with respect to this highest5 ambiguity and are appropriately
absent from the derivative functional.

### Native dual, weight sign and Casimir projection

The native pairing is diagonal and complex bilinear. Dividing each covector
coefficient by `E.weight(e,c)` therefore produces its native representer.
The actual P is the self-adjoint kernel projector built from the native
pairing Gram, so applying P preserves evaluation on ker(K_dt).

J01 is skew for that pairing; a representer paired with highest weight +5
must have weight -5. On the authenticated integer-weight interval [-7,7],
the product of `(J^2+m^2)/(m^2-25)` over m=0,1,2,3,4,6,7 selects the ±5
sum. Then `(I+iJ/5)/2` selects eigenvalue -5i, as implemented. Only after
this step are all spins below5 absent. The polynomial
`(Cas-42)(Cas-56)/312` is consequently a valid spin5 projector under the
stated maximum spin7 premise. Reversing these two projections without a
different complete Casimir projector would be invalid. The final lowest
weight, Casimir, time-kernel and P assertions are appropriate controls.

Conjugate(E) is the correct candidate space for this lowest-weight
representer. If membership holds and native M reciprocity plus the existing
E inverse apply, solving within conjugate(E) gives the required adjoint
support and annihilates the full relevant kernel. That implication does not
require a separate nondegeneracy theorem for the restricted E Gram.

### Two small verification seams to tighten

1. `reduce_conjugate_E` checks own pivots equal1 and checks reconstruction,
   but its nonmembership conclusion additionally uses the inherited echelon
   property. Validate equal basis/pivot lengths, distinct pivots, and zero
   coefficients at all earlier pivots. Reconstruction alone holds even for
   a poorly ordered arbitrary basis and would not then justify declaring a
   surviving remainder to be outside the span. The previously authenticated
   basis is expected to satisfy these checks; they make this new boundary
   explicit.
2. `finite_controls` describes a nonvacuous fixture but does not assert a
   nonzero covector/evaluation. Include a unit input at an explicitly
   nonzero ell key and compare its exact evaluator output with ell[key].
   A nonzero target in at least one fixture prevents all-zero agreement
   from being mistaken for a transposed-functional check. Retain the
   separate complex-linearity control.

These are validation-hardening requests, not a discovered sign/projection
error. Root owns execution and any scratch edits.

### Result ceiling

Nonzero full-carrier remainder proves only nonmembership in this
conjugate(E) representer ansatz at the supplied T. It proves neither a
kernel nor scalar ambiguity. A T={} control or exact rational-root-center
result is not a result at the certified actual root. Since the goal and
projection/reduction are affine in T, all relevant affine remainders zero
would establish family membership; alternatively a rigorously enclosed
nonzero remainder coefficient could establish root-ball nonmembership.
No whole-space inverse, smooth family, integrated response, physical ghost,
GU verdict or change in the existing coefficient certificate follows from
this exploratory test alone.

## Conditional addendum: affine membership and native reciprocity

The parent is testing the reference T=0 and all59 background basis values
for each of the four selected Hermitian coefficient targets. This addendum
reviews the implication **conditional on all60 cases passing for all four
targets**. It does not claim completion of that run. I inspected
`run_goal_affine.py`; it now includes the requested echelon and nonzero
single-key controls and checks representer evaluation on all120 E basis
vectors. No computation was run by this reviewer.

### Exact reciprocity derivation

Let B1 and B2 denote the actual complex-bilinear trace/form pairings on
one-forms and two-forms. For one-forms,

    Q(a,b) = a wedge_comm b = Q(b,a).

The exterior swap and ordinary Clifford-commutator swap each contribute a
minus sign. Define H(a,b,c)=B2(Q(a,b),Phi* c), symmetric in its first two
arguments. Using the actual adjoints in the native definition of N gives

    B1(N(a,b),c)
      = [H(a,b,c) + H(a,c,b) + H(b,c,a)]/6.

This expression is invariant under every permutation of a,b,c. In
particular, N(T,.) is B1-self-adjoint for any fixed T. This is algebraic
reciprocity for the stated native pairing, not a positive Hilbert-space
claim and not a coefficient transpose substituting for a differential
adjoint.

The projector P is the B1-self-adjoint projection onto the nondegenerate
native time kernel N. For u,v in N, Pu=u and Pv=v, so

    B1(M_N u,v) = B1(u,M_N v),
    M_N = I + 2 P N(T,.).

The insertion of P is therefore legitimate; it does not spoil reciprocity
on N. This derivation uses the actual `Phi_adj` and `left_wedge_adj` contracts
inspected in the native engine and the reviewed star-free specialization.

### Why the finite representer suffices

E is the exact highest5 source envelope, invariant under all59 real affine
background operators. All native coefficients are real when T is real;
therefore conjugate(E) is also invariant, and M on conjugate(E) is the
conjugate of M on E. Wherever the already-certified E block is invertible,
including both certified real root balls, the conjugate block is invertible.

Suppose the restricted lowest5 representer g_T of a selected scalar
functional lies in conjugate(E). There is then z in conjugate(E) with
M_N z=g_T as a **full-carrier equality**, because E closure was established
before trial-space reduction. For any highest5 k in the full N-kernel,

    ell_T(k) = B1(g_T,k) = B1(M_N z,k)
             = B1(z,M_N k) = 0.

This proves the selected functional is independent of highest5 kernel
additions, even if the full highest5 operator has an unknown kernel. It
does not require the restriction of B1 to E or E plus conjugate(E) to be
nondegenerate; the full native pairing, closure and block inverse are the
relevant inputs. Since ell_T has real coefficients before complex-linear
extension, its annihilation of a complex k also annihilates the real and
imaginary realifications relevant to the selected coefficient.

### Affine proof and certificate interpretation

The goal covector is affine in displacement T: Czero is affine and appears
once in each goal term, while the row-seed correction is T-independent.
The native dual conversion, P, weight/Casimir projections and reduction
against fixed conjugate(E) are linear. Consequently

    g(sum_j x_j T_j) = g(0) + sum_j x_j [g(T_j)-g(0)].

Thus membership at T=0 and each of the59 T_j values proves membership for
the entire real59-parameter family. These are affine **values**, so the
reference must be subtracted in each direction; simply summing x_j g(T_j)
would be wrong. Completed evidence must contain all60 cases, all four
declared targets, no failure, and matching basis/background/helper inputs.
This family identity removes the rational-center-to-actual-root gap for
membership. Invertibility is still used only where it is certified.

### Scope challenge and accepted conclusion

If the run passes, the justified strengthening is: **the four selected
formal pointwise Hermitian coefficient functionals are independent of the
full highest5 kernel choices within the specified SO(3)-equivariant source
family**, at both certified real roots. The complete spin6/7 inverse inputs
handle the other relevant components of that same family, and the whole
contracted moving correction remains highest7 and current-blind.

Do not broaden this to every matrix coefficient, every scalar observable,
or arbitrary nonequivariant auxiliary choices. Equivariance is what limits
the relevant source-family ambiguities to the stated representation sectors.
The result does not construct an auxiliary solution family, solve individual
uncontracted differentiated equations, supply a new Gram-normalization
certificate, establish an integrated supported response, or identify a
physical/source-required observable. In particular the prior nonzero
coefficient evidence and this kernel-independence theorem remain distinct
from an actual smooth weak reduction and from GU falsification.

Conditional review disposition: the reciprocity and finite-adjoint-support
argument is sound with the exact premises above. Await the parent's complete
affine certificate to change the pending computational status.


## Final integration

All120x59 closure images, two root-ball inverses, four selected intervals and all60x4 affine goal memberships passed. Earlier review requests were addressed: native Hodge sign guard; input-bound checkpoints; exact echelon/earlier-pivot checks; nonzero transposed-coefficient control; selected interval and inconclusive global-HS console labels separated. The formal, equivariant scalar scope and unproved smooth-family, Gram, support and source/physical bridges are retained. No full-kernel matrix or physical verdict is claimed.


## Final affine computational status and integrated-report scope review


The complete `scalar-goal-affine.json` is now available. I inspected its
saved records and bindings without rerunning extraction or membership:

- SHA256: `cdd03c4fbeb9805dcdd0b65d2995c8611ee8237a6162d3e9f0ad430a3996ffc5`.
- `completed=60`, with exactly60 case records: reference -1 followed by
  background indices0 through58, without omissions or duplicate indices.
- Every case contains the four declared targets in order:
  (3,4,1910), (3,4,3446), (3,4,4981), (3,4,1909).
- All240 records have `member=true` and120 coordinate coefficients.
  There is no failure record.
- Basis, background and helper SHA256 bindings match the inspected input
  files. Both explicit echelon and nonzero-transpose control flags are true.

This completes the computational premise of the conditional reciprocity
addendum. Combining the saved affine-family membership with the reviewed
algebra proves independence of the four selected formal coefficient goals
from highest5 kernel additions within the specified SO(3)-equivariant source
family. Together with the root-ball coefficient certificates, their nonzero
values cannot be canceled by choosing a different highest5 auxiliary solution
within that category. The conclusion remains limited to these four goals.

I also read the generated native report
`explorations/conditional-build/source-action-weak-response-2026-11-26.md`.
Its section3a uses the correct affine value formula and reciprocity identity,
limits the conclusion to the four selected goals and the stated equivariant
category, and explicitly excludes arbitrary matrix entries and nonequivariant
choices. Its continuation retains individual differentiated equations,
smooth local realization, Gram normalization, supported integration and
physical/source admission as separate unresolved burdens. I found no blocking
scope overclaim in that generated report. The numerical all-Gram margin and
failed coarse global-HS test remain correctly distinguished from the exact
selected-coefficient certificates.

This final status supersedes only the pending computational language in the
conditional addendum. It does not certify new native gates, a whole weak
matrix, arbitrary auxiliary families, a full PDE realization or a physical
GU conclusion.
