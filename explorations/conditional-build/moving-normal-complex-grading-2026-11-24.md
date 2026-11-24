---
title: Moving normal reductions supply additional genuine RS symbol gradings
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2-P3
tier: T2
expected_delta: Determine whether moving-reduction covariance supplies actual descending symbol grades
  beyond the four common-fixed-symmetry grades
actual_delta: Sixteen spectral-sign gradings of the canonical tangential RS symbol descend to the same
  chi_H under moving-J covariance. The rank10 extreme projector has normal stabilizer u(3,2); pure tangential
  Dirac oddness requires parallel J. Combined with the native shape block and an explicit raw-E observed-grade
  extension, every squared-weight sector couples:15 of16 sign choices fail the necessary off-block oddness
  test, leaving only hidden +chi_H for further testing. No full operator-grade or index acceptance follows.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Moving-reduction symbol grades and their shape-coupling test

program_target: X-P1-P2-P3
tier: T2
expected_delta: Determine whether moving-reduction covariance supplies actual descending symbol grades beyond the four common-fixed-symmetry grades
actual_delta: Sixteen spectral-sign gradings of the canonical tangential RS symbol descend to the same chi_H under moving-J covariance. The rank10 extreme projector has normal stabilizer u(3,2); pure tangential Dirac oddness requires parallel J. Combined with the native shape block and an explicit raw-E observed-grade extension, every squared-weight sector couples:15 of16 sign choices fail the necessary off-block oddness test, leaving only hidden +chi_H for further testing. No full operator-grade or index acceptance follows.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: Explicit moving-J spectral-sign grades and their connection compatibility condition
carrier: canonical R_Y=ker Gamma_Y, hidden S_H tensor R_N, observed four-spinor contraction; distinct from raw six-spinor observation LAYER=ambient+observed BRIDGE=canonical-RS-contraction CHIRALITY=S-FULL-DIRAC
pairing: supplied nondegenerate orthogonal metric-spin splitting, actual K95 cross-grade law retained; no physical positivity assumption ON=declared_carrier
real_structure: actual K95 quaternionic fixture and conditional general Spin-commuting real/quaternionic structure; no K77 transfer
grading: sixteen explicitly constructed symbol grades, not all possible grades, full-operator grades or Fredholm indices
action_owner: N/A -- representation and connection conditions; no source action or selected J built
target: moving-reduction alternative to common-fixed-symmetry classification MAP-TYPE=contraction
```

## Result first

The moving-reduction alternative is more than a logical loophole. For every
supplied normal orthogonal complex structure J on the actual (6,4) normal
bundle, there are sixteen explicit spectral-sign gradings of the canonical
tangential RS symbol which descend to the **same** observed chi_H. They obey
the compatible Krein and antilinear laws described below. Fourteen are beyond
the two uniform hidden signs surviving the prior quaternionic restriction.
This is an exhibited family, not an exhaustive classification of all
moving-selector grades, and it selects no J or source action.

Composing these hidden sign choices with the companion native shape block
gives a stronger answer in that explicit raw-carrier category:15 of16 fail
the necessary opposite-block oddness condition for every J. Only the uniform
hidden +chi_H choice passes that condition; no full operator grade is thereby
accepted. Section7 states the carrier/readout hypotheses and proof.

A particularly economical member flips a rank-ten normal subbundle (rank40
in the hidden ambient carrier), leaving the observed complement unchanged.
Its projector P(J) has normal Lie stabilizer exactly u(3,2). For a bare
compatible tangential Dirac connection on the hidden bundle, full operator
oddness of this member holds iff nabla P=0, equivalently nabla J=0. Thus the
surviving symbol construction comes with a precise differential test rather
than a presumption of physical viability.

No new integer index, zero-total witness, family count, source physical
projector or Fredholm realization is inferred. The native grading packet
remains blocked on its named physical/domain data.

## 1. Source audit and the category under test

The operative source facts remain SC-CHI-01/04/51 (nonchiral total and
effective observed separation), SC-GEN-01/03 (2+1 and imposter labels),
SC-GRP-03 (normal compact/complex reductions), SC-GRP-06 (not an independent
internal group), and SC-FER-07 (normal-spinor quantum numbers). None identifies
a physical Fredholm grade. The moving family is a repository-derived test of
an admitted structural alternative, not an attribution of this polynomial to
the source.

Use Category G from `source-weak-action-transport-2026-11-13.md`: normal
form and spin factors transform together. Spin-only transport would not
preserve gamma contraction. The source connection and current may move with
epsilon/reduction data; the fixed-versus-transported distinction and the
four independent fields in `source-joint-symmetry-current-2026-11-13.md`
remain in force.

The earlier exact trace-motion theorem applies to **one fixed grade**
commuting with full endogenous Lorentz and geometric weak symmetry. It does
not classify a covariant family G(J), for which differentiation has the
additional dG(X·J) term. This result constructs such a family while retaining
the actual symbol/descent equations, rather than merely presenting an
unrelated moving tensor.

The global-normal-complex theorem proves absolute U(3,2) existence on
noncompact spin four-bases, but it selects no J and imposes no end value.
It is a theorem about the real normal (6,4) bundle, not a consequence of the
K77 Spin lift and not a K95-to-K77 reality transfer. The construction below
is global only relative to a supplied J and compatible Spin bundle; it is
otherwise a universal fibrewise formula for every admissible J. It needs no
new globally chosen spinor, determinant square root or frame: those appearing
in the Fock calculation are a way to calculate the representation, not extra
chosen fields. The real polynomial is defined directly in the existing Spin
representation.

TW1 already computes the infinitesimal normal Spin action of J and its
spinor weights; TW3 already proves associated-bundle naturality. Those are
inputs, not new results here. The new objects are the gamma-traceless normal
weight projectors, the genuine descending grade family, and its stabilizer /
connection test. The existing 16/144 endogenous-Lorentz branching is not
repeated or recredited.

## 2. Carrier and exact normal weight calculation

Retain the Nov21 canonical tangential category (rank1664 R_Y, observed rank512): nondegenerate split H⊕N,
complex full Dirac spinors, R_Y=ker Gamma_Y, literal observation contraction
q, its canonical orthogonal right inverse r, and observed g=chi_H. The
orthogonal decomposition is

    R_Y = K ⊥ im(r),
    K = S_H tensor (R_N+ ⊕ R_N−),
    R_N± = ker[Gamma_N : N_C tensor S_N± -> S_N∓].       (1)

Each R_N half has complex rank144. The hidden canonical tangential symbol
is c_H(xi) tensor I; it preserves the two summands of (1). This does not
assert anything about all normal-covector symbols of a full Y operator.
This carrier is not the rank1920 raw one-form/scalar carrier used in the
companion two-sided test, whose observed receiver has rank768. They share
the rank1152 hidden kernel; compatibility of their completions is not inferred.

Write R(J) for the infinitesimal form-plus-spin action of J in a specified
normal representation. It is not the vector J, its finite Spin quarter-turn,
or the spinor volume. In an adapted frame, the commuting plane rotations
have eigenvalues i times half-integers. Fix the Fock convention

    S_N = Lambda* W tensor det(W)^(-1/2),
    weight on Lambda^r W = r-5/2,
    vector weights = +1 (five times), -1 (five times).

The determinant notation is local representation notation. Gamma contraction
is equivariant and surjective. Consequently subtract the opposite spin-half
character from N_C tensor S_N±. The exact result is

| Normal half | weights of R(J)/i, with complex multiplicities |
|---|---|
| R_N+ (even input spin degree) | -7/2:5, -3/2:50, +1/2:65, +5/2:24 |
| R_N− (odd input spin degree) | -5/2:24, -1/2:65, +3/2:50, +7/2:5 |

Reversing the J/chirality naming interchanges the signs/rows and does not
change the squared-weight result. Set

    Z = -4 R(J)^2.

On R_N+⊕R_N− its distinct eigenvalues are 1,9,25,49, with ranks
130,100,48,10. The operator is semisimple: J is conjugate to five same-sign
plane rotations, and the finite Spin representation is completely reducible
under its compact circle. The exact polynomial spectral projectors are

    P_a(J) = product_(b != a) (Z-b I)/(a-b),
    a,b in {1,9,25,49}.                                  (2)

In particular,

    P_49 = (Z-I)(Z-9I)(Z-25I)/46080.                     (3)

This rank-ten projector contains both extreme weights, five in each normal
chirality. It is nontrivial within each irreducible normal Spin half.

For an explicit kernel check, creation u_i and annihilation v_i have charges
+1 and -1. The five v_i tensor vacuum and five u_i tensor top-wedge vectors
are gamma-free: annihilation kills the vacuum, and creation kills the top.
These are exactly the extreme weights. No quotient rank is guessed from
multiplicity alone.

## 3. Genuine grades, descent, pairing and reality

For signs epsilon_a in {+1,-1}, put on the hidden factor

    B_epsilon(J) = sum_a epsilon_a P_a(J),
    A_epsilon(J) = -chi_H tensor B_epsilon(J),

and put G_epsilon=r chi_H r^-1 on im(r), with off-diagonal lift T=0.
All sixteen choices satisfy

    G_epsilon²=I,
    q G_epsilon = chi_H q,
    {G_epsilon, sigma_tan(xi)}=0.                         (4)

The proof uses the orthogonal idempotents (2), their sum I, and the fact
that the hidden symbol acts only on S_H. Normal form-plus-spin action preserves
Gamma_N and Gamma_Y, so the maps act on the actual kernels in (1).

For the extreme member, B=I-2P_49. The same P_49 polynomial may be taken
in the normal action on the full R_Y: im(r) carries the normal spin module,
whose squared weights are only 1,9,25, so the polynomial vanishes there.
Thus it changes no observed field and qP_49=0. Its ambient hidden rank is
4 times10=40; on each normal half it reverses five of144 hidden directions,
not the whole half. It is therefore outside all four constant-per-half
product-equivariant grades. This is a representation distinction, not a
physical observable. For this member, the normal B has eigen-ranks
278 and10 and trace268 (trace134 on each144 half), replacing the uniform
B=I trace288. Tensoring with chi_H keeps the hidden G eigen-ranks576/576;
including im(r) gives total finite fibre ranks832/832. These finite traces
are not Fredholm indices and do not establish the source zero-total premise.

Let sharp denote the **actual supplied** invariant Hermitian/Krein adjoint.
Normal Spin generators obey R(J)^sharp=-R(J); hence Z^sharp=Z and every
real polynomial P_a is self-adjoint. The hidden split is nondegenerate,
and P_a commutes with the base grade. Therefore a baseline law
G0^sharp=s G0 (s=+1 or -1 as appropriate to the declared pairing) is inherited
by the new grades. The original K95 cross-grade fixture has s=-1, not a
positive-Hilbert self-adjoint grading; that convention is retained. No
nonorthogonal shear is used, so T=0 remains pairing-compatible.

If C is an actual anti-linear real/quaternionic structure commuting with the
normal Spin action, then C R(J) C^-1=R(J). Since (2) is a polynomial in
R(J)^2 with real coefficients, C P_a C^-1=P_a. Thus the existing
C G0=-G0 C law is inherited. This is why the construction uses **squared
weights**, not sign(-iR): the latter changes sign under C and would generally
break the desired cross-grade law. In the K95 fixture, C exchanges both
normal chirality and the two opposite weights, and the equal signs on their
squares preserve that exchange. The abstract polynomial argument applies separately whenever the actual
K77 real or K95 quaternionic C has these stated properties. The companion
probe checks the existing K95 fixture explicitly; it does not transfer that
fixture to K77 or certify a K77 physical grade.

These are all grades **within this four-projector sign ansatz**. Other
stabilizer-equivariant maps, off-diagonal terms without an orthogonal pairing,
full-operator grades and physical quotients have not been classified.

## 4. Moving covariance and weak invariance

For an allowed normal Spin transformation k,

    P_a(k J k^-1)=rho(k) P_a(J) rho(k)^-1.

The same holds under endogenous Lorentz with its induced action on N and
its horizontal action on S_H. Consequently the construction defines a
covariant family on the whole admitted orbit without choosing an orbit point.
Every normal transformation preserving J commutes with its polynomial;
in particular a geometric weak factor in the supplied compatible compact /
U(3,2) intersection commutes with these grades. If a proposed weak embedding
does not preserve that same J, this statement does not apply to it.

The exact trace-motion theorem now gives a useful contrary control: since
P_49 is a nontrivial rank-five operator on each irreducible R_N half, it
cannot commute with all normal Spin. It commutes with a compatible weak
factor, so it cannot also commute with all fixed endogenous Lorentz actions.
Its Lorentz covariance genuinely uses motion of J; it does not satisfy the
hypothesis of the four-grade fixed-object theorem.

## 5. Exact stabilizer and the next operator test

The identity-component normal stabilizer of P_49 has Lie algebra u(3,2).
Here is the proof, rather than a dimension guess. Complexify the normal
algebra using W from the calculation:

    so(10,C) = gl(W) ⊕ Lambda²W ⊕ Lambda²W*.

The first summand preserves J and hence P. The two ten-dimensional cosets
are irreducible inequivalent gl(W) modules, with central charges +2 and -2.
For X in the lowering summand, choose its nonzero representative annihilating
modes1,2. On the extreme vector u_3 tensor top it acts nontrivially through
the spin factor, producing u_3 tensor (annihilate1 annihilate2 top), weight
+3/2, outside im(P). The vector factor action vanishes because 3 is distinct
from1,2. Spin equivariance keeps the result gamma-free. The raising analogue
acts nontrivially on v_3 tensor vacuum, giving weight -3/2. Thus neither
coset is in the stabilizer. Irreducibility and inequivalent central charges
exclude any nonzero kernel or cancellation between the cosets. The complex
kernel is exactly gl5, and its real intersection with so(6,4) is u(3,2).

Let nabla be a product Clifford-compatible connection on K, let
D_h=c_H^mu nabla_mu have no extra zeroth-order term, and use the extreme
grade A=-chi_H B(J). Then

    {D_h,A} = chi_H c_H^mu (nabla_mu B),                 (5)

up to the harmless overall sign chosen for D/chi. The four Clifford
coefficients c_H^mu are linearly independent, and nabla B acts on the normal
factor. Thus (5) vanishes iff every nabla_mu P vanishes. By the exact
stabilizer just proved, this is equivalent to nabla_mu J=0 for all horizontal
mu. Equivalently, the orbit map J->P(J) has injective differential: it may
identify the discrete pair J,-J, but has no additional infinitesimal kernel.

For D_h=c_H^mu nabla_mu+Phi the equation instead contains {Phi,A}; the full
source operator also has hidden/observed cross terms and independent dual
conditions. They may change or compensate the connection term. Derivatives
of J cannot be dropped merely because the symbol identities pass. Grade-stable
closed domains and end/boundary conditions are further requirements, not
consequences of the polynomial.

**Holonomy countercontrol.** If the normal connection were exactly the
Sym²-induced Levi-Civita connection and its horizontal Lorentz holonomy were
full, it could not preserve J: it preserves the negative metric trace t,
so parallel J would make Jt a parallel negative traceless symmetric tensor.
The traceless Lorentz nine-dimensional representation has no fixed vector.
The contradiction is the connection version of the already-owned absence of
a Lorentz-natural J. This is a control, not a new source exclusion. Source
SC-GEO-55 explicitly allows displacement from the gauge-rotated Levi-Civita
connection; its actual connection and lower couplings must be tested. Do not
silently replace them by the bare Levi-Civita control.

## 6. What is ready and what remains missing

Section7 completes the immediate opposite-block test on the existing
reconstruction. Its only surviving hidden sign choice still requires a
compatible observed six-spinor grade and all remaining principal/lower-order
oddness equations. Other operators or non-spectral grades retain their own
connection and dual tests. Constructing an action or selecting a J would be
a different task; no such missing object is fabricated here.

The result gives a concrete counterexample to treating the fixed-product
four-grade list as exhaustive for moving reductions. It does not give a
counterexample to that theorem, which explicitly excludes this category.
It also does not show that the source selects any member, that total index is
zero, or that an odd observed count follows. None of the new ranks are family
counts. P3 and X-P1-P2-P3 acquire additional conditional symbol witnesses and
an exact differential burden; the native physical grading packet is not
unblocked solely by them.

Reproducibility: the companion probe enumerates the exact Fock/gamma kernel
weights, polynomial projectors, all16 sign controls, extreme raising/lowering
witnesses, observed annihilation and actual K95 Clifford reality/adjoint
building blocks. The general stabilizer and naturality assertions rest on
the proofs above, not on a sampled matrix rank.

## 7. Immediate composition with the native opposite-block result

The companion two-sided-shape result now gives an exact additional constraint
without choosing J. Its same normal hidden kernel has an opposite block

    B_shape = a P_K A_II : H* tensor S -> K,
    rank_C B_shape = 512

on the actual symmetric-metric shape. Each coefficient of A_II is a single
horizontal Clifford vector, and P_K contains only even normal Clifford
products. Hence

    B_shape chi_H = -chi_H B_shape.                     (6)

For any of the sixteen hidden grades A_epsilon=-chi_H B_epsilon(J), assume
a proposed extension to the full raw E remains block-diagonal for K and its
canonical orthogonal complement and its observed grade G_o satisfies
pi_b G_o=chi_H pi_b, where pi_b extracts the horizontal one-form coordinate.
Mixing from b into the trace/scalar output is allowed; trace/scalar input
cannot feed b. These are explicit extension hypotheses; the sixteen RS
symbol constructions do not supply them. A
necessary off-diagonal condition for that extension to grade this triangular
operator is

    A_epsilon B_shape + B_shape chi_H = 0
    iff (B_epsilon(J)+I) B_shape = 0.                   (7)

Thus im(B_shape) must lie in the negative eigenspace of B_epsilon. This
condition is necessary even before checking the remaining observed rows,
lower terms, derivatives or domains; it is not a claim those checks pass.
The b-input with other observed coordinates zero is the canonical RS
observation lift, and the hidden K is the same. Nevertheless R_Y and the raw
E are different carriers and the repaired operator need not preserve R_Y.
Equation(7) is only a necessary condition on a raw-E grade with the same
hidden choice. The minimal observed condition permits b-to-trace/scalar
mixing, so such a grade need not preserve R_Y and need not extend the entire
R_Y symbol grade. No full raw-E grading is declared here.

If r_minus is the sum of the selected negative **normal** spectral ranks
from {130,100,48,10}, that negative hidden space has dimension4 r_minus.
The native rank certificate and elementary rank inequalities give

    rank[A_epsilon B_shape + B_shape chi_H]
        >= max(0, 512-4 r_minus).                       (8)

Exactly six of the sixteen sign choices have r_minus<128:

| Negative normal rank | Lower bound on the off-block grading defect |
|---:|---:|
| 0 |512|
|10|472|
|48|320|
|58|280|
|100|112|
|110|72|

Consequently those six cannot extend to an odd grading of this repaired
operator with the same observed chi_H. In particular the economical extreme
rank-ten moving grade has defect rank at least472 for **every** J. The
remaining ten pass this dimension screen only; no compatibility is asserted.
The all-negative choice is the already-known hidden-reversed grade and
passes (7) automatically, but its other operator/domain/physical conditions
are still separate.

This is a scoped composition of the two new results, not retraction of the
symbol witnesses. A symbol grade can fail the lower-order cross-block test.
The source never demanded this particular exact graded/index realization;
its physical weak projector, full current and possible other constructions
remain open. No physical-family count or index is read from (8).


### 7.1 Exact native shape incidence: only the all-negative sign can pass

The dimension screen is not the final answer. For the native shape and the
same factorized metric-spin pairing, **every** squared-weight sector meets
the shape coupling nontrivially:

    P_a(J) B_shape != 0  for all a=1,9,25,49 and every J.  (9)

To prove this, let W be the +i normal eigenspace of J, choose any nonzero
w in W, and choose a nonzero exterior spinor phi in Lambda^r W containing
w as a wedge factor. For r=2,3,4,5 this is always possible. Normal Clifford
multiplication by w is creation, so c_N(w)phi=0. Thus, for any horizontal
spinor s, the simple normal one-form spinor

    k = w^flat tensor (s tensor phi)

is in the normal gamma kernel. Its doubled J weight is 2r-3, hence its
squared weight is respectively1,9,25,49. It belongs to im(P_a), not merely
to the containing vector-spinor module.

Let tau=+1 or -1 be the uniform Clifford adjoint sign for the supplied spin
pairing. In orthonormal frames, the adjoint of (2) in the companion shape
article, applied to this k, is

    (A_II^sharp k)(e_j)
       = tau c_H(S_w e_j) s tensor phi.                 (10)

For completeness, A_II has coefficients
A_(r,j)=sum_mu eta_mu (S_(n_r))^j_mu c(e_mu).
The form adjoint contributes eta_j eta_r. Substituting
k_r=K(w,n_r)(s tensor phi)=eta_r w^r(s tensor phi) sums the shape operators
to S_w. The g-selfadjoint relation
eta_j(S_w)^j_mu=eta_mu(S_w)^mu_j then gives (10). This derivation uses
complex linearity in w and a nondegenerate invariant pairing; neither
positivity nor a nonzero norm of k is required. A nonzero scalar density
and the coefficient a only multiply the adjoint by invertible factors.

Native shape is injective as a map of normal vectors:
S_w=-(1/2)g^-1 w. Hence w!=0 gives some j with S_w e_j!=0. Clifford
multiplication by that complex horizontal vector is a nonzero matrix.
Choose s outside its kernel, which is possible even if the vector is null.
Equation(10) is then nonzero. Since P_K k=k and P_a^sharp=P_a,
P_a B_shape=0 would imply

    0=B_shape^sharp P_a k=conjugate(a) A_II^sharp k,

a contradiction. This proves (9) for arbitrary J without a sampled
placement or a chosen background.

Now apply P_a to (7). If epsilon_a=+1, it would require 2 P_a B_shape=0,
contradicting (9). The direct spectral summands cannot cancel one another.
Therefore exactly one of the sixteen sign choices can pass this necessary
cross-block test:

    epsilon_1=epsilon_9=epsilon_25=epsilon_49=-1,
    B_epsilon=-I,     A_epsilon=+chi_H on K.             (11)

It is the already-known hidden-reversed grade. It passes this cross-block
condition automatically; the remaining source rows, differential oddness,
realization and analytic domains are not thereby established. The other
fifteen still exist as canonical tangential **symbol** grades, but their hidden
sign choices cannot occur in the specified raw-E graded realization of this
repaired operator.
This is not a source physical-chirality verdict, a statement about every
moving grade, or a universal result over arbitrary normal extensions or
pairings. Equation(9) uses the exact native shape at the B_n=0 representative.
The companion theorem about all metric normal extensions proves nonvanishing
of their opposite block, not the same spectral-incidence or rank statement.

Root replay:324 exact controls, including actual K95 building blocks, and
two planted-error controls rejected. Internal specialist review is recorded
in the [review](../../lab/process/hostile-reviews/2026-11-24-source-dual-grading-review.md).
