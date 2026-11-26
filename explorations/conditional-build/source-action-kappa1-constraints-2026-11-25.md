---
title: Actual finite-coupling constraints without adding a completion
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: LB-CLASS
tier: T1
expected_delta: Evaluate actual kappa1 constraint blocks and distinguish them from physical energy and quotient claims.
actual_delta: Closed-time geometric cancellation, complete spin6/7 constraint inverses and nonzero derivative-induced connection readout at both roots, plus a regular-path obstruction between them; full constrained energy and physical ghost status remain undetermined.
class_covered: Held W2 K95 full-U candidate and its two certified kappa1 real zero-matter backgrounds; closed non-null physical-time covector, native compatible reference connection, actual imaginary connection sector. Structural cancellation also holds for the stated constant-rank parallel symbol class.
premises:
- lab/sources/source-claim-register.yaml#SC-ACT-01
- lab/sources/source-claim-register.yaml#SC-ACT-05
- lab/sources/source-claim-register.yaml#SC-GEO-51
- lab/sources/source-claim-register.yaml#SC-META-53
- explorations/conditional-build/source-action-coupled-ghost-2026-11-25.md
- explorations/conditional-build/source-action-dynamics-and-continuation-2026-11-25.md
source_bridge:
  status: conditional
  reason: Source motivates the action grammar and full U, but does not select this reconstructed action, physical quotient or state domain. No source-necessary exclusion follows.
kill_condition: Opposite certified signs of a persistent scalar constraint eigenvalue exclude an everywhere-invertible path inside the fixed-geometry59 family. Separately only actual constrained negative-energy states in a stated admitted category exclude its energy positivity; a matrix entry or failed search is not a physical ghost verdict.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target: INTERNAL-REGULAR-CONSTRAINT-PATH-59
internal_target_verdict: No everywhere-regular constraint path connects the two roots within the stated fixed-geometry family.
canon_verdict_change: none
---

# Actual finite-coupling constraints without adding a completion

```yaml
program_target: LB-CLASS
tier: T1
expected_delta: Evaluate actual coupling-one constraints without new completion choices.
actual_delta: Complete spin6/7 inverses, nonzero derivative-source readout and a regular-path obstruction; physical energy remains undetermined.
```

## Decision and advance outcomes

Continue the diagnostic on the existing candidate, without installing a new action,
state law, pairing, cutoff or other completion choice. The preceding coupled
test already established a large-positive-coupling constrained-energy
obstruction. Repeating that result does not answer the two coupling-one roots.

Before root evaluation, the outcomes were fixed as follows:

| Certified outcome | Permitted conclusion |
|---|---|
| Negative constrained quadratic directions at both roots | Both stated candidate data categories have an energy obstruction; physical status still needs quotient and propagation checks. |
| Such directions at one root only, with a complete contrary classification at the other | A source-independent stability discriminator; no automatic proof of nonlinear stability or decrement of a choice-family count. |
| Positive/semidefinite constrained quadratic form at both roots | The proved large-coupling obstruction does not extend to these categories. |
| Incomplete inverse, incomplete constraint chain, or no witness found | UNDETERMINED, not positive and not a failed theory. |

The physical-quotient and propagation conditions are separate from these local
algebraic tests. The choice inventory remains10 grouped families /4 grouped
compatibility bundles /bookkeeping net6. The stationary-branch entry is pending,
not one of those ten installed families.

```gu-typed-objects
result: actual finite-coupling algebraic constraints and physical-inference audit
carrier: TstarY tensor u64_64; imaginary-Clifford connection sector LAYER=ambient BRIDGE=physical_observation_unproved CHIRALITY=N/A
pairing: native -Re_trace_div128 with K95 one-form contraction ON=connection_forms
real_structure: real full U64_64; complex highest-weight computations require their real-form return
grading: coefficient conjugation and geometric rotation weights; not a physical family/chirality grading
action_owner: repository-construction fixed W2 I1B-style action with independent bars
target: actual algebraic constraint endomorphism and scoped evidence MAP-TYPE=not-a-map
```

> **GU-COMPARATOR-ROUTING — scope before inference.** This is
> `INTERNAL_STRUCTURAL_ONLY`; read [source-native routing](../../lab/methods/source-native-comparator-routing.md).
> K95 is not K77, full U is not Sp, I1B is not I2B, and a geometric
> rotation weight is not an observed particle spin. Krein data alone do not
> supply a BRST quotient. Source2+1 and literal contraction are retained.

## 1. Geometric transport cancels, rather than being discarded

Use the [actual Hessian and complete principal classification](source-action-coupled-ghost-2026-11-25.md):

    H = kappa I + K + 2 N(T0,.),
    K = (Phi D_B + D_B^dagger Phi^dagger)/2.

Here N is the polarized cubic-gradient map, not the time-kernel bundle. Write
that bundle as V_N below. Phi is parallel for the compatible reference spin-LC
connection because it uses parallel metric, Clifford, orientation and Hodge
operations. With the torsion-free form connection and actual native volume,

    K = sum_a K^a nabla_a.

This covariant expression includes the lower coefficients that a homogeneous
frame calculation reports separately. It does not declare them zero.

Let tau=dt remain non-null, A=K_tau, P the native-pairing orthogonal projector
onto V_N=ker A, and G the inverse of A on V_R=V_N-perp, extended by zero.
The previous classification proves constant rank in a non-null neighborhood,
nondegenerate kernel pairing and P K_alpha P=0 for every covector alpha.
Differentiating the projector in the tau direction beta gives

    (d_beta P)P = -G K_beta P,
    P(d_beta P) = -P K_beta G.

Differentiating P K_alpha P=0 and restricting to V_N therefore yields

    P K_beta G K_alpha P + P K_alpha G K_beta P = 0.       (1)

The same identity is the mixed quadratic term of the zero NN Schur complement
of the constant-rank pencil A+s K_alpha+t K_beta. No norm-positive metric or
self-adjoint Hilbert completion enters this algebra.

For a section n of V_N, differentiating K_tau n=0 gives

    (I-P) nabla_a n = -G K_(nabla_a tau) n.

Thus

    P K n = -sum_ab (nabla_a tau_b) P K^a G K^b n = 0,    (2)

because the Hessian of t is symmetric and(1) is antisymmetric. This uses the
closed physical covector dt; a rotating arbitrary timelike one-form with
nonzero exterior derivative need not satisfy the argument. Normalizing dt
changes no projector and contributes only terms annihilating V_N.

**The exact constraint endomorphism is consequently**

    M_N = kappa I_N + 2 P N(T0,.)|V_N.                    (3)

This is a structural theorem for a compatible parallel constant-rank symbol
pencil with the stated kernel identity and an exact non-null time covector.
It applies to the held candidate; it is not a theorem for every GU action.

### An exact control against freezing the moving projector

At the observation section take the raw coefficient vector n=theta3 Id,
representing physical i n. Its homogeneous P K(n) has three coefficients
+1/4 at(exterior8,Clifford1033),(8,4106),(8,8204). The physical-dt transport
contribution has exactly -1/4 at the same entries. Their sum is zero.
Omitting the transport would give a demonstrably wrong constraint column.
The implementation checks symbol covariance and additional kernel vectors;
the written proof, not sampling, supplies the class-wide cancellation.

## 2. Actual background dependence and invariant blocks

The cubic part in(3) is not zero. Exact all59-coefficient functionals evaluated
on both certified root balls prove nonzero couplings out of the central-time
kernel line. In raw real-coefficient pairing conventions the two tested
functionals are

    64 (x3+x5),                 -(1328/9) x4.

They evaluate respectively to approximately
(0.04182558708,0.40604617004) and(-1.8761970933,-4.8120996344)
at(root1,root2), with rigorous errors below3.2e-14. The physical i-sector
pairing reverses both raw signs; nonvanishing is unchanged. These are matrix
entries, not eigenvalues or reduced energies. The central line is not an
invariant scalar block, and replacing M_N by kappa I would be false.

For a coefficient with exterior mask e and Clifford mask c, use label e XOR c.
Phi preserves this label; cubic coupling adds a background label. The label
span of the held59 background family has binary rank10. Adding the time bit
raises it to11. Projection P preserves paired time labels. Therefore the
imaginary constraint matrix splits into eight invariant cosets, with dimensions

    6146, 6144, 6144, 6144, 6144, 6144, 6144, 6144.

These total49154. This is a complete support decomposition for the held
background family, not a numerical sparsity guess or a physical multiplicity.
The exact entry rule in a kernel basis {z_a}, with Gram matrix B, is

    (B M_N)ab = kappa B_ab + sum_j x_j C_jab,
    C_jab = 2 b(z_a,N(T_j,z_b)) = 2 b(T_j,N(z_a,z_b)).     (4)

The second equality uses the symmetric third variation of the cubic action
and avoids repeatedly multiplying by a large background. Certified root-ball
bounds propagate to every such affine entry. Inverting a selected compression
is not inverting all eight blocks.

## 3. Finite-coupling invariant sector

### Complete highest-rotation-weight block

The physical-time little group is the geometric SO(3) acting on the three
base-spatial axes. Its tangent14 representation is three spin0 copies, two
spin1 copies and one spin2 copy. In the imaginary Clifford phase the largest
Clifford weight is5; coupling the exterior one-form gives maximum weight7.
Exact character counting gives36 highest-weight multiplicities. These weights
are geometric rotation labels, not observed particle assignments.

A complete highest-weight basis is reconstructed from exterior theta5+i theta8
and the Clifford product

    (gamma0+i gamma1)(gamma10+i gamma12)
    (gamma9+i gamma11)(gamma5+i gamma8),

followed by every subset of the six zero-weight directions{2,3,4,6,7,13}
whose total Clifford degree is0 or3 mod4. There are36. Direct exact checks
verify weight7, raising annihilation, basis independence and full K_dt replay.
The Hermitian form b(conjugate(u),v) implements the pairing on multiplicity
coordinates; the actual i-sector real form reverses the raw common sign,
which does not change invertibility.

K_dt has rank20 on this multiplicity space. Its kernel dimension is16 and
its kernel pairing is nondegenerate. The background family is SO(3)-invariant,
so(3) preserves this complete highest-spin isotypic block; no untested small
ansatz is being called autonomous. This is pointwise algebraic autonomy, not
closure under all spacetime/normal differential terms.

The exact16 by16 constraint matrix uses all59 background coefficients via(4).
At each rational root center, an exact rational-complex inverse has zero
matrix residual. For the certified root ball of radius r, the probe bounds

    ||R [H(x)-H(x_center)]||_infinity <= eta < 1,

using the sum of absolute real and imaginary rational coefficients after R
is applied to every affine coefficient matrix. The certified eta values are
approximately3.7841e-10 and5.1428e-10. Therefore this entire constraint block
is invertible at BOTH actual roots, not only at their numerical centers.
Its16 multiplicity directions represent240 real algebraic constraint
components after the15-dimensional rotation representation is restored.
They are not240 physical states. At this stage alone, the remaining48914 imaginary constraints
are not thereby inverted; the spin6 calculation below extends the coverage.

### A regular-constraint path cannot join these roots

Across the entire held59 background family the16-dimensional constraint
block splits into fixed sizes1,4,6,4,1. Two scalar factors remain isolated.
After division by their nonzero kernel Gram factors, their values are:

| Scalar factor | Root1 | Root2 |
|---|---:|---:|
| mu0 | +3.77401801686 | -1.69762822877 |
| mu8 | +4.75452757052 | -2.61597476139 |

Each sign is certified over its full root ball; the largest stated error is
below1.1e-11. The exact affine functionals and Gram factors are reproduced in
the machine evidence. These are eigenvalues of the auxiliary constraint
endomorphism, NOT energy eigenvalues or mode frequencies.

For any continuous path(κ(s),T(s)) within this fixed-geometry59 family,
with the same physical-time kernel, each mu is a continuous real function.
A path from root1 to root2 must cross mu=0 by the intermediate value theorem.
Because the scalar lines are invariant, that makes the FULL M_N singular.
Thus **no everywhere-invertible-constraint path in this family joins the roots**.
This holds whether or not the path is stationary. It does not prove that a
stationary path exists, forbid paths through a constraint transition, or
exclude paths leaving the family.

The existing small-h stationary branch lies in the symmetry-selected59 family;
there mu=κ+O(1/κ)>0 at sufficiently large positiveκ. Its regular continuation
to root2 would meet the same obstruction. A regular continuation to root1
remains unproved. In particular, the earlier large-coupling energy result
cannot simply be transported to root2 by assuming an unchanged constraint
structure. A singular intermediate constraint matrix is not itself an
inconsistent theory or an unstable vacuum.

### Direct observation is zero; confinement is not established

At the held constant-base stationary section, every highest-spin7 connection
one-form is vertical, so literal section pullback vanishes on this whole
isotypic block with the metric held. A general moving section can contract
vertical components through its derivative; that different readout is not covered. Equivalently, the pulled-back
connection has maximal geometric rotation weight6. This does not mean the
block is dynamically confined: exact tests find a transverse axis with
nonzero q K_axis v for EACH of the36 highest-weight basis vectors. This
rejects a naive differential-closure inference from qv=0. An equation-symbol
image qK_axis v is not a propagated physical leakage rate.

### The first directly readable block is also fully evaluated

The highest-spin6 sector has264 imaginary multiplicities. Its time-symbol
rank is136 and its kernel dimension128, with nondegenerate native kernel
pairing. Literal connection readout has rank36 on the full multiplicity
space and rank16 on its time kernel. These ranks do not count particles.

The actual128 by128 algebraic constraint matrix is evaluated using all59
background coefficients. An exact label-support screen reduces8256 possible
symmetric trilinear pairs to2112. The resulting symbolic coefficient graph
splits into four32 by32 blocks. ALL FOUR are certified invertible at BOTH
root balls. Worst exact Neumann upper bounds are approximately1.0754e-4
and2.8694e-4, respectively, comfortably below1.

For these larger blocks a numerical calculation supplied candidate inverse
entries; each decimal was then frozen as an exact rational. Acceptance uses
only the recomputed rational residual plus the entire root-ball perturbation
bound. The committed witness matrices and standard-library verifier make
numerical inversion unnecessary for reproduction. No eigenvalue sign is
accepted from floating arithmetic.

Together, the complete spin6 and spin7 blocks cover1904 of49154 real imaginary
connection constraints. The other47250 remain unevaluated. Neither a16-row
readout compression nor these two isotypic inverses substitutes for the full
constraint system. They do make a specific hidden-to-readout constraint
transfer computable, instead of automatically queueing every lower rotation
sector.

### Hidden variation forces a readable algebraic response

A fixed range vector v=K_dt b7 in the highest-spin7 block has zero direct
literal connection pullback. Apply the actual horizontal symbol K_theta0,
project its equation onto the complete spin6 time kernel, solve that block's
constraints and read the resulting connection:

    q_N6 M_N6^(-1) P_N6 K_theta0 v.

The sign convention for the solved response includes a minus sign from the
constraint equation. Its source covector has only three nonzero multiplicity
entries: b18=-3145728, b27=9437184 and b117=6291456. For the same raw real
readout coefficient(exterior1,Clifford1597), the exact certificates give:

| | Rational-center response (approximate) | Certified absolute error bound |
|---|---:|---:|
| Root1 | +1.3098877408e-5 | 1.2839272426e-5 |
| Root2 | -1.2366927788e-4 | 6.0482178270e-5 |

Both intervals strictly exclude zero. If R is a rational inverse candidate,
c0=-Rb and ||I-RH||<=eta<1 over the root ball, the solution-error bound is
eta/(1-eta) times ||c0||. Multiplying each block error by the readout row's
absolute norm gives the displayed bound. The verifier recomputes eta before
using it. The physical imaginary-sector convention flips both H and b,
leaving this solved response unchanged.

A smooth range section can have v_R7(p)=0 and prescribed first derivative
nabla v_R7(p)=theta0 tensor K_dt b7. At its zero value, lower/frame and
projector-derivative terms multiplying that value vanish. This is a possible
section jet, not a proved full solution jet. Solving both spin6 and spin7
auxiliary blocks completes the pointwise constraints; other types can be
assigned zero without presuming their invertibility. Because the operator
and held readout are real, a nonzero complex highest-weight response yields
at least one nonzero realified witness in the imaginary-Clifford real form.

A horizontal spatial covector has spin1. Acting on spin7 can therefore
reach only spin6,7,8; spin8 is absent and literal q_N7=0. No uncomputed lower
rotation sector can cancel this particular derivative-induced contribution.
Other independently supplied data can compensate it; this is a nonzero
linear transfer coefficient, not a statement that every state is visible.

**ESTABLISHED:** a specified horizontal derivative source in the directly
invisible sector induces a nonzero algebraic constraint readout at both roots,
with other independent sources fixed. This is stronger than the uneliminated
qK symbol test. **UNDETERMINED:** whether this source is realized by an admitted
propagated state, whether the physical quotient removes it, and whether any
associated exchange is unstable. No general confinement claim is settled.

### What the finite-coupling test has not decided

Both roots pass the complete spin6 and spin7 algebraic-constraint inverse checks.
Their full constrained canonical energy still has status UNDETERMINED.
None of the both/one/neither-negative outcomes in the opening table has been established.
Even a negative reduced pointwise form in this block would require checking
transverse constraint forcing and admissible data before a compact-data or
physical ghost conclusion. No background has been selected by stability.

## 4. A time constraint is not a derivative-free field

The common kernel of all principal symbols is exactly zero:

    intersection_alpha ker K_alpha = {0}.

For each of the fourteen complete time-symbol representatives, stacking its
transverse symbol maps has full column rank on the time kernel. For a fixed
transverse axis, distinct time-label blocks map to distinct blocks, so inputs
from different blocks cannot cancel. The established orthogonal covariance
covers all equal-degree representatives; complex zero kernel implies zero on
the actual real U carrier and its imaginary sector.

This rules out a proposed computational shortcut—removing a whole subbundle
that is algebraic in every direction. It does not remove time constraints,
exclude derivative-dependent gauge transformations, count physical modes or
prove propagation.

## 5. Physical quotient, propagation and interactions

### BRST/physical quotient

**ESTABLISHED:** native frame covariance and independent dressing redundancy
are defined; the latter leaves Ahat unchanged. The active fixed-reference
central U1 shift is not a symmetry of this action: its change includes
kappa/2 times the native integral of |dphi|². The existing local matter gauge
identity test also excludes arbitrary-function additive local matter gauge
freedom in its stated zero-background category.

**UNDETERMINED / NOT SUPPLIED:** an actual nilpotent BRST charge Q, its domain,
physical cohomology, inherited pairing and observed descent for this candidate.
No tested negative direction can currently be classified Q-exact, nonclosed,
or a nonzero physical cohomology class. LT-SM8 remains NEEDS. SC-META-53 is
UNCERTAIN about bounded spectra and maximal-compact shielding; it does not
supply Q or an admissible positive projector. This is not a proof that no
such quotient can exist. Earlier K77/free-Yang–Mills/BV comparators cannot
be imported into this W2 action.

### Propagation and energy exchange

**ESTABLISHED:** where the complete relevant algebraic constraint system is
invertible, substitution gives an equation first order in physical time and at
most second order in the other coordinates. The spin7 pointwise inverse alone
does not close the PDE or eliminate cross-sector differential forcing. Even
the complete reduced equation form would not by itself prove well-posedness. At zero matter,
the selected positive linear matter sector and the bosonic sector decouple
quadratically. Coefficient conjugation makes the bosonic action even in the
imaginary connection perturbation: its first mixed cubic vertex contains two
imaginary fields and one real field.

The action also contains connection–matter vertices. For central a=i c Id,
the actual matter variation is deltaD[a]=i sigma_rep(c), nonzero for nonzero
c and invertible when c is non-null in the repaired principal representation.
Thus algebraic decoupling of the center from all matter is false. No new
interaction has been installed to reach that conclusion.

**UNDETERMINED:** whether the negative constrained data propagate in an
admitted domain, survive the physical quotient, overlap positive physical
modes and produce runaway exchange. A nonzero vertex does not prove those
mode overlaps. Indefinite energy does not by itself prove instability:
opposite-sign harmonic oscillators can both be stable; even nonzero weak
coupling at separated frequencies can preserve that stability. Neither
confinement nor runaway is established for the candidate.

## 6. Proposed constraint-sheet finding, not a release

> **Held-candidate accounting, not a GU necessity theorem.** The W2/K95
> candidate and its selected local linear-matter completion currently use10
> declared choice families(5 core,5 diagnostic), satisfy4 grouped mathematical
> compatibility obligations and select0 source-owned observable predictions.
> An entire observed dispersion function remains unselected. The bookkeeping
> difference6 is not six independent parameters or a lower bound on extra data
> required by GU. Candidate equations permit arbitrary local analytic observed
> fermion histories in the unrestricted independent-bar category. Recent tests
> also exclude positive canonical quadratic energy on unrestricted compact
> constrained instantaneous data of the sufficiently-large-positive-kappa
> branch. Coupling-one energy, physical ghosts, nonlinear viability and GU
> generally remain undetermined.

This updates the draft in [variable completion §12](source-action-variable-completion-2026-11-25.md).
It does not promote a general-elephant sheet, change a ledger verdict or release
a paper. “Best construction” is not an established optimization result.

### The two selection questions

| Question | ESTABLISHED / RULED OUT under stated premises | UNDETERMINED |
|---|---|---|
| Can section/metric dynamics alone select observed history? | Exact barred-zero coupled witnesses allow arbitrary local analytic observed fermion histories at both roots. Sole selection by those equations is ruled out in that unrestricted category. | Whether source-selected physical restrictions remove those witnesses; nonzero paired matter backreacts. |
| Must every probabilistic completion add an arbitrary reference? | Smooth positive full-fibre densities natural in(g,y) alone have infinite mass. Singular conformal-ray probability controls survive; the stated extra-tensor class allows smooth finite laws precisely under compact effective stabilizer conditions. Finite normalization alone does not select the tested signed response average. | Which physical probability category or extra data the source selects. A history probability need not be a fibre probability. Natural in enlarged data does not mean inherently non-natural. |

Interpretive server/client, observer-mind or information-processing ontology is
NOT MODELED, not excluded by these results.

### Exclusions with surviving mechanisms

- Finite-order spatial lifts of freely initialized, finite-rank,
  fibre-independent analytic base laws are excluded across the stated open
  varying-cone patch. Restricted data, boundary/global, nonlocal/infinite-order,
  different symbols and singular supports remain outside that theorem.
- Pointwise invertible antilinear bar graphs preserving all freely initialized
  actual local matter solutions fail at both roots. Source-independent bars,
  restricted-state, differential and nonlocal pairings remain.
- The stated faithful same-phase classical pseudodifferential lift class is
  excluded; phase-changing, nonclassical and restricted-data classes remain.
- Positive quadratic energy on the large-kappa unrestricted constrained-data
  category is excluded. A preserved physical domain may exclude witnesses,
  but must be supplied and tested rather than silently assumed.
- Finite smooth positive full-fibre(g,y)-natural normalization is excluded.
  Singular and extra-data alternatives survive without being installed here.

## 7. Choice accounting and next comparison

No new choice family, physical quotient, state restriction or source prediction
was added. Exact projection, representation decomposition and field elimination
are derived operations. The inventory remains10/4/net6; a whole dispersion
function still fits within one family. The net subtracts unlike grouped units
and is a monitoring convention, not a necessity theorem or predictive score.
A root preference would narrow a pending branch entry, not automatically
remove one of the ten active families.

For this directed wave, unsupported completion-building is not the next move.
A proposed future completion needs an actual source constraint or an independent,
source-relevant consequence with fixed inputs, a named failure test and no
retrospective refitting. Merely fitting a newly chosen dispersion is insufficient.
This bounded posture does not create a standing program_focus amendment or
an agent-wide stopping rule.

The next comparison, using the existing selection explanation, is:

| Rank | Investigation | Scope and source relevance | Input, cost and strongest alternative |
|---|---|---|---|
| 1 | Actual reduced observed evolution using the completed spin6/7 constraints | Held candidate; can test whether an existing state restriction removes the measured readout response while preserving evolution. Source necessity remains unproved. | Complete the required receiver closure only, with named failures. Medium cost; avoids blind inversion of all lower spins. Strongest alternative is the physical-quotient audit below. |
| 2 | Source-typed physical admission of the energy/readout witnesses | Can separate algebraic negative directions from a physical claim under LT-SM8; no BRST quotient is supplied. | Exact Q/domain/pairing is the missing input. Audit source constraints without inventing Q. Broad class potential, low current decisiveness. |
| 3 | Coupled preservation of the existing positive matter completion | Existing fixed domain/completion, with no refit; may reject an installed choice instead of adding one. | Actual coupled receiver and interactions needed. Medium cost. Generic finite-band product leakage is already known and is not a new result. |

Mandatory basis is Joe's directed diagnostic, not ordinary cadence. These are
continuation comparisons, not a governance amendment or global waiting rule.
A verified failure removes a specified category; a survivor must retain its
unselected inputs. No new completion is adopted by this ranking.

## Verification

The integrated standard-library probe reconstructs the actual native symbol,
bases, all59 affine coefficients and root-ball inverse bounds, then certifies
the fixed transfer. It passes without floating acceptance arithmetic. Three
finite-core Lean lemmas compile under the pinned project environment without
proof placeholders. Two mathematical specialists and a separate source/hostile
review accept the stated internal T1/T2 scope; see the
[review](../../lab/process/hostile-reviews/2026-11-25-source-action-kappa1-constraints-review.md).

All eight native audits and final diff/semantic-preservation checks pass.
Program-focus and carrier audits first identified two metadata-format issues;
these were corrected using existing artifact conventions and the failed gates
were rerun. No gate was changed. No full-project Lean build or fully formalized
PDE/physical-spectrum claim is made.
