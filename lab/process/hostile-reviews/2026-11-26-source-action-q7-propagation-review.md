# Q7 propagation: independent T1 reviews

Basis `4578af6d992be339395cf3d7e97eca8bd03689d6`. Two mathematical/source specialists and a separate hostile reviewer. These are internal agent reviews, not external peer review. The concrete probe author is separate. The lead integrated the held-metric connection ceiling, all-u quantifier, unknown-kernel independence and fixed-module/free-profile conditions.


## First mathematical specialist

# Independent review: Q flow, auxiliary ambiguity, and actual consistency

Date: 2026-11-26. Read-only review against clean GU revision
`4578af6d992be339395cf3d7e97eca8bd03689d6`.
No owner edits and no heavy replay. This review reads the existing native
algebra, exact energy intervals and written geometric results; it does not
certify a new inverse or a propagated physical mode.

## 1. Verdict

The proposed **degree-two flow closure obstruction is valid**, with the whole-Q
isotropy premise and the qualification that auxiliary elimination is available
only on the sources being used. It needs no full-N inverse, no new cross-entry
calculation and no new receiver solve.

At either certified root, for horizontal covector theta0, the highest-spin7
two-dimensional complex multiplicity space of Q maps injectively into R/Q
under the degree-two velocity, for every allowed auxiliary-kernel correction.
Consequently no nonzero SO3 submodule of Q can contain that velocity for all its
data. Any SO3-invariant range subsystem containing Q and closed under this
degree-two flow needs at least **four spin7 copies, hence at least 60 real
dimensions**. Extra types or further copies may also be needed.

This is a requirement on closure of a proposed range subsystem. Q is isotropic
for the time symplectic form and is not already a full phase space. The result
does not exclude initial data with range value in Q, prove their propagation,
exclude the candidate equations, identify physical particle spin, or select a
source-required restriction. It must not replace the actual Dirac consistency
question in Section 7 below.

## 2. Typed setup and sign convention

Work at a point with real native nondegenerate symmetric pairing b, complexified
as the Hermitian form h(u,v)=b(conj(u),v). Use the actual imaginary-U pairing;
changing to raw real-Clifford coordinates changes one overall sign below and
does not change the conclusion. Let

    A=K_dt, N=ker A, P:N projection, R=I-P,
    G=(A|R)^(-1) on R, zero on N,
    M=P J|N,  J=I+2 N(T,.),
    s_xi(v)=P K_xi v.

P and R are native selfadjoint. A and K_xi are native skew-adjoint; M is native
selfadjoint. These are adjoints for the native indefinite pairing, not a
positive auxiliary norm. Q is the two-copy real spin7 range module generated
by V5=A b5 and V12=A b12.

The previously certified complete N6/N7 inverses solve s_xi(v) when xi=theta0
and v is in Q. Denote the particular solution by y(v), so M y(v)=s_xi(v).
No inverse on the remaining native N is required. Every other solution is
y(v)+k, k in ker M.

After n=-y(derivative v)+lower terms is substituted in the R equation, the
formal real-derivative degree-two velocity symbol is

    S_xi(v)=+G R K_xi y(v).

For Fourier substitution derivative -> i xi it is -S_xi. The proposed minus
sign is therefore correct for the Fourier generator, while the formal
real-derivative symbol has plus sign. The closure result is sign-independent.

## 3. Whole-Q symplectic isotropy is established by parity

The native highest-spin7 basis construction in
`source_action_reduced_evolution_probe.py` gives

    b5:  zeros [2,3,4,6], degree 8,
    b12: zeros [2,3,6,7], degree 8.

These metadata were independently recomputed from the displayed enumeration,
without rebuilding the large native bases. Every Clifford word in either
vector has even degree. K_xi reverses Clifford parity: in the native Phi formula
the first summand has one degree-one factor, and the second has degree-one and
degree-two factors; Hodge operations act on exterior indices. Phi_adj reverses
parity as well, hence so does K_xi=(Phi wedge_xi-wedge_xi^* Phi_adj)/2.

Thus V5,V12 are odd, and A applied to either is even. The native pairing is
diagonal in Clifford blade labels, so opposite Clifford parities are orthogonal.
Geometric rotations preserve grade. Therefore the entire real SO3 orbit and
its complexification satisfy

    h(Q,AQ)=0.                                            (1)

This includes the cross-copy pairings. Merely knowing h(v,Av)=0 for individual
vectors would not suffice; it is automatic for every skew-adjoint A and gives
no such conclusion. Equation (1) is the necessary stronger fact.

## 4. The two source energy rows are a nondegenerate Hermitian matrix

For i,j in {5,12}, put

    F_ij=h(s_xi(V_i),y(V_j)).

Because M is selfadjoint and M y(V_i)=s_xi(V_i),

    F_ij=h(M y_i,y_j)=h(y_i,M y_j)=conj(F_ji).

This proof does not need a nondegenerate restriction of the pairing to the
receiver and does not need an ambient inverse. Also, for k in ker M,

    h(s_xi(V_i),k)=h(M y_i,k)=h(y_i,Mk)=0.                 (2)

Thus all the F rows are independent of the auxiliary solution choice.

The published `lab/process/source-action-reduced-evolution.json`, under
`exact_probe.physical_derivative_energy`, uses exactly the same xi=theta0 and
the exact basis indices 5 and 12. The probe computes both complete spin6 and
lowered spin7 contributions. Its factor14 on the lowered spin7 Gram and its
physical/raw pairing sign are explicit. The strict interval signs are:

| Root | F55 interval, rounded outward for display | F12,12 interval, rounded outward for display |
|---|---:|---:|
| 0 | [1484669.16,1484681.24] | [-3943694.67,-3943662.60] |
| 1 | [-3347127.51,-3347075.24] | [7155644.70,7155756.43] |

The exact rational endpoints in that artifact, rather than these displayed
decimals, are the evidence. Consequently at every actual background covered
by each root certificate,

    det F=F55 F12,12-|F5,12|^2 < 0.                       (3)

No cross-entry estimate is needed. The result uses both diagonal signs at the
same covector, not signs from different axes or roots. It establishes
nondegeneracy, not positive or negative definiteness. In particular F does
have isotropic lines; that fact causes no gap because Section 5 tests against
all of Q, not just against the proposed output line.

## 5. Kernel-independent injection of the velocity modulo Q

For u in Q and any v in the highest multiplicity span,

    h(u,A S_xi(v))
      =h(u,K_xi y(v))
      =-h(P K_xi u,y(v))
      =-F_xi(u,v).                                       (4)

R drops out because u is in R and A G=R. Formula (2) proves that (4) is unchanged
if any k in ker M is added to y(v). The Fourier sign reverses both sides of the
velocity convention and has no effect on vanishing.

If S_xi(v), with any such correction, were in Q, (1) would make the left side
zero for BOTH test vectors V5,V12. For v=c5 V5+c12 V12, this gives F c=0.
By (3), c=0. More generally the map

    span_C(V5,V12) -> R_C/Q_C,
    v -> [S_xi(v)]

is injective for every linear selection of auxiliary corrections. Its
nonvanishing conclusion holds pointwise even if the correction is chosen
separately for each input. Thus every nonzero SO3-invariant submodule
U tensor V7 of Q fails to contain this degree-two velocity.

The stronger fact that the spin7 component itself is independent of arbitrary
kernel corrections also follows from the owned complete N6/N7 invertibility:
ker M has only spins at most5 at these roots; a horizontal spin1 K_xi cannot
send it to spin7, and G preserves SO3 type. The row argument already suffices
and does not require using this extra fact.

## 6. The four-copy lower bound

Let W be an SO3-invariant real subspace of R containing Q, and suppose the
degree-two velocity for every Q datum, with any valid choice of auxiliary
lift, lies in W. Since A commutes with rotations, a Hermitian pairing against
a highest-weight7 test vector detects only weight7 of spin7. The ambient
carrier has no spin above7, so weight7 is highest weight.

Let p_7,7 be the projection onto that highest multiplicity space. Applying
p_7,7 to the two outputs in (4) leaves their pairings unchanged. The linear
functionals w -> h(V_i,A w) vanish on Q_high by (1); their matrix on the two
output classes is the invertible matrix -F. Hence

    dim_C (W_high,7 / Q_high,7) >= 2,
    dim_C W_high,7 >= 4.

Real integer-spin7 irreducibles have dimension15; the owned reality structure
on Q has already been verified. Thus W contains at least four real spin7
copies and has real dimension at least60. This is a lower bound, not a claimed
closed 60-dimensional system. The other spin components and further iterations
of the flow may force more dimensions. It is not an observed-particle or
generation count. It is compatible with ordinary enlargement from a
configuration-like isotropic subspace to the needed phase variables.

## 7. Actual Dirac consistency: the needed matched equation

In a time-adapted local trivialization write the complete differential system
in block form, including every connection/projector/lower term,

    A v_t+B v+E n=0,
    D v+M n=0.                                           (5)

B,D,E are spatial differential operators. The closed-time theorem is exactly
what makes M multiplication, with no derivatives of n in the second equation.
No assertion that affine-invariant T is parallel is used. In a stationary
trivialization A,M,D have no explicit time dependence; in general retain it.
Differentiate the WHOLE second equation and substitute the first:

    M n_t = D G(B v+E n) - (partial_t D)v
                            - (partial_t M)n.            (6)

All compositions in (6) are differential-operator compositions: derivatives
act on coefficients, frames and preceding factors. Writing partial_t D means
the full time derivative in the chosen trivialization, with any necessary
connection commutators included. Equation (6), rather than an uncontracted
L_b Gamma_a source, is the next necessary auxiliary range equation.

If n=n0+k, k in ker M, every genuine native kernel vector z imposes

    h(z,D G(Bv+E(n0+k))-(partial_t D)v
                                  -(partial_t M)(n0+k))=0. (7)

In the variable PDE this is a differential condition on the kernel multiplier
section k. For a frozen constant-coefficient Fourier problem at fixed spatial
frequency, B,D,E become matrices, M_t=D_t=0, and (7) is a finite linear system

    L k=-c,
    (Lk)(z)=h(z,D G E k),
    c(z)=h(z,D G(Bv+E n0)),
    L:ker M -> (ker M)^*.

It may determine multipliers, impose a secondary restriction on v, or make a
specified initial datum inconsistent. Failure with k=0 alone is insufficient.
If L is singular, its own compatibility and the next differentiated conditions
must be considered. A degenerate native Gram on ker M is no obstacle to this
dual formulation; do not write an unjustified orthogonal projector onto ker M.

The top potential cubic source for n0 linear in first derivatives cancels in
the matched symbol because the owned identity gives

    P K_xi G K_xi P=0.

After that cancellation, coefficient derivatives and lower pieces remain.
One cannot infer that the entire consistency chain closes. In particular the
firstjet census separates individual connection channels; it does not compute
the fully contracted expression (6) or its multiplier freedom.

## 8. Decision link and existing propagation status

The published reduced-evolution report explicitly proves only an equation
one-jet at a point for the stated witnesses and says differentiated constraints
remain. Its Section 4 explicitly denies a convergent solution, propagation
proof or permission to apply Cauchy-Kowalevski to the singular time symbol.
The normal-tensor report solves P H(i_Q v+n)=0 for every smooth Q test section,
and explicitly leaves the R equation unsolved. The coupled-ghost report also
keeps propagated physical states undetermined. I found no owned proof that
propagates these negative constrained Q data.

A true full-native cokernel witness can exclude a specific proposed jet or a
specific multiplier-free lift. It cannot by itself exclude the action. Even
failure of the correctly multiplier-adjusted condition (7) excludes that data
category, not all solutions. A decision relevant to the negative-energy data
requires either a consistency-preserving solution construction carrying a
strict negative-energy datum, or proof that the COMPLETE consistency chain
removes all such data in a stated required category. Which category is
source-required remains a separate bridge.

A negative-energy polynomial eigenmode of a frozen native pencil would be
propagation evidence for that frozen descriptor only. It does not establish a
mode of the variable geometric PDE without an exact invariant reduction or
another PDE existence argument. Noncommuting adapted frame directions prevent
silently discarding normal derivatives to turn a frozen pencil into an exact
local spacetime mode.

## 9. Family-wide algebraic shortcuts and the uncovered-source question

On the all59 affine family, M(x)=I+sum x_j A_j, so M(0)=I. There is no nonzero
kernel shared by that entire affine family, and its determinant is not the
zero polynomial. Native reciprocity alone implies neither positivity nor
diagonalizability nor a root-specific kernel. A stationary root might be
singular because of additional equations, but that needs an exact identity
modulo those equations or another genuine root-bound proof. A numerical small
singular value or an interval containing zero is not such a proof.

For the already uncovered sources, an annihilator of E4/E5 is only a receiver
annihilator. It is a true range obstruction only if its representing vector
has exact full-native M z=0. The nondegenerate E5 signature (56,64,0), exact
invariance and reciprocity do give an invariant E5-perpendicular complement;
the uncovered spin5 sources, whose support is disjoint from E5, stay there
under all59 generators. That is a valid reduction for a grouped future solve,
not an obstruction or decision link. Do not extrapolate the E5 direct sum to
E4 without checking its Gram nondegeneracy.

## 10. Review disposition

Accept the Section 5 closure obstruction and Section 6 four-copy lower bound as
conditional internal structural consequences of the already owned exact
native premises and root intervals. No additional numerical evidence is
needed for the mathematical implication. If publishing it, add small literal
controls for the parity, same-row mapping and sign conventions; keep the
existing source/physical ceilings intact.

Do not report this as actual admission or rejection of negative initial data.
For that task, the next object is the fully matched consistency source (6),
with kernel multipliers and all variable-frame terms retained. No current
census or covariance result proves its solvability or failure.

## 11. Concrete new probe review and independent replay

Reviewed the full new
`/private/tmp/gu-q7-propagation-wt-20261126/tests/program-focus/source_action_q7_propagation_probe.py`
and root output `/private/tmp/gu-q7-propagation-native.json`.
I also independently ran its cheap native mode with bytecode writes disabled,
saving `/private/tmp/gu-q7-propagation-independent-native.json`. The replay
finished successfully in about 0.11 seconds. All output fields agree with the
root output after removing elapsed time.

The implementation correctly:

- Hash-binds all seven old data/code dependencies before reuse, rather than
  implicitly trusting whichever local file happens to have the same name.
- Replays the exact Gaussian-rational inverse candidates and the old
  Neumann/source error formulas, with both the official inverse hash and
  root-radius binding checked. All128 spin6 kernel indices are covered.
- Checks the particular two sources have the exact single spin6 coordinates
  37 and40 and zero lowered-spin7 source. Omitting the spin7 solve for these
  two columns is therefore valid; it is not an assumption that every Q
  derivative source has zero spin7 component.
- Requires exact agreement with all four old center/error/lower/upper fields.
- Uses the correct upper bound
  positive.lower times negative.upper for the negative diagonal product.
  The two determinant upper bounds are approximately -5.855034267964e12 and
  -2.3950481263017e13. Subtracting the cross-entry absolute square can only
  decrease the determinant.
- Reconstructs exactly the old V5/V12 vectors, binds them to the old native
  range hashes, checks their weight/highest conditions, and computes their
  canonical cross-Gram as zero. The actual reconstructed grades are V:7,
  A V:8, consistent with the general parity proof above.
- States that extension from the highest vectors to all descendants is the
  structural parity theorem, not a sampled inference.
- Labels data-only mode partial and keeps physical admission, instability and
  action/source rejection out of its conclusions.

No blocking implementation or proof-scope issue found. The output's quotient
rank2 is a theorem consequence of the checked data and written argument; it
is not falsely presented as a newly computed full R matrix rank. The
four-spin7-copy lower bound remains the written representation-theory
consequence in Section 6. Any forthcoming Lean lemma may certify its stated
finite algebraic implication, but should not be described as formalization
of native geometry, the full PDE, or propagation.


## Second specialist and source relevance

# Second independent specialist and source review — Q7 propagation

## Reviewed artifacts and verdict

Reviewed the installed probe `/private/tmp/gu-q7-propagation-wt-20261126/tests/program-focus/source_action_q7_propagation_probe.py` and `/private/tmp/gu-q7-propagation-native.json` against the owned source-energy and constraint evidence. Probe SHA256: `de122fac6296819abd83b7f6d1050b5d460e59100da0005456625eb08a1a18d7`.

Independently replayed the full default probe with bytecode disabled, writing only `/private/tmp/gu-q7-propagation-second-review-replay.json`. Exit0; output is identical to the supplied native result except elapsed time. This is an independent cheap replay and mathematical review, not a fresh full N6 inversion, formal proof of native geometry, external review, or completion of the other T1 requirements.

**PASS at the declared candidate scope.** The actual parity checks, exact energy replay and written argument establish that no nonzero SO3 submodule contained in the two owned Q7 copies is preserved by the freely initialized horizontal degree-two principal time flow. Unknown auxiliary-kernel corrections do not restore the tested tangency. The stated lower bound of at least four spin7 copies /60 real coefficient dimensions for an SO3-invariant closed R subsystem containing Q is valid under the same closure/free-data premises.

## Concrete checks and weakest reproducibility seam

- Native reconstruction checks exactly the prior V5/V12 hashes, highest weight7 and raising annihilation. Both have Clifford grade7, while K_dt V has grade8. Their canonical highest Gram is exactly zero; native Q Gram is diag(3145728,-9437184), so this is canonical isotropy, not degeneracy of the native Q pairing.
- Phi's odd Clifford-factor parity and rotation generators' even parity support the all-descendant proof. The theorem does not extrapolate all Q isotropy from four sampled Gram entries: parity proves it on the full two SO3 modules.
- The source replay identifies the same theta0 derivative sources: b5 is the single N6 coordinate37 with coefficient3145728, and b12 coordinate40 with coefficient9437184. Their lowered-N7 source parts are empty. All four N6 blocks, the actual root radii, inverse hashes and existing Neumann certificates are bound and checked.
- Exact replay recovers strict diagonal signs (+,-) at root0 and (-,+) at root1. For a Hermitian matrix H=[[a,z],[conjugate(z),d]], det H=ad-|z|². The code's positive-lower times negative-upper bound is a valid strictly negative upper bound on ad and therefore on det H. No cross-entry value or floating rank is assumed.
- The probe deliberately reuses previously certified complete-N6 inverses through hashes and exact metadata/error replay. It does not rederive every old matrix coefficient. That is an honest reuse seam; dependency changes trigger failure rather than silent rebinding. The native written reciprocity theorem supplies Hermitian symmetry; a file hash alone is not its proof.
- `highest_Q_multiplicity_quotient_rank:2` is a consequence of the written theorem, not a separately computed full propagation matrix. The output explicitly says the conclusion requires the written theorem. Preserve that distinction.

## Mathematical implication, including all-kernel freedom

Let A=K_dt and omega(u,z)=b(conjugate(u),Az). The parity result gives omega(Q,Q)=0. For s_v=P K_theta0 v, choose the certified N6 preimage y_v with M y_v=s_v. Native reciprocity makes

`F(u,v)=b(conjugate(s_u),y_v)`

Hermitian. It is independent of every full-M kernel correction k because

`b(conjugate(s_u),k)=b(conjugate(M y_u),k)=b(conjugate(y_u),M k)=0`.

For the actual degree-two time symbol D2 v=G K_theta0 y_v (up to the single consistent Fourier sign),

`omega(u,D2 v)=-F(u,v)`.

The corresponding identity holds after any first-order auxiliary principal kernel addition. Tangency D2 v in Q therefore forces F(u,v)=0 for all u in Q. The two-by-two highest-multiplicity form is nonsingular by the opposite strict diagonal signs, so no nonzero highest v can satisfy that condition. Every nonzero SO3 submodule of Q has such a highest vector.

**Critical quantifier:** the argument uses all u in Q, not merely u=v or u in the proposed submodule. Indefinite F does have isotropic lines. Those lines do not give tangency because Q×Q canonical isotropy forces the entire dual row F(.,v) to vanish. This removes the strongest apparent counterexample.

Lower-order Z_Q, frame and density terms cannot cancel this principal second-derivative obstruction for freely initialized horizontal profiles in the first-order graph category. No full-M invertibility, arbitrary full-R lift, chosen positive norm or physical quotient is needed. This does not settle higher/nonlocal lift classes outside the stated principal-order contract, special constrained profiles, or spatially homogeneous solutions.

## At least four spin7 copies: proof and ceiling

A commutes with SO3. Pairing with a highest-weight Q7 vector only sees the weight7/spin7 component of the output: the carrier has no spin above7. If a linear combination of the two projected highest7 outputs belonged to Q, the same dual identity would make the corresponding two-component F column zero. Nonsingularity forces the combination to be zero. Thus there are two independent highest7 classes modulo the original Q highest plane.

Any SO3-invariant R subsystem that contains Q and the required principal-flow images contains these projected classes as well, since weight/Casimir projectors preserve an invariant subspace. Its spin7 multiplicity is therefore at least2+2=4. Integer spin7 is real type, of real dimension15; for the actual real field carrier this implies at least60 real coefficient dimensions. This is a lower bound, not an exhibited closed60-dimensional subsystem. Other spins, further copies and lower-term/differential closure may be required. It is not four physical particles, four families, a physical spin7 spectrum or a degree-of-freedom count after constraints/quotients.

## Source scope and novelty

This is stronger than the earlier auxiliary-Q construction: it now answers a necessary part of the actual remaining R equation. It does not repeat the old full-regular-R energy/Sobolev result, raw compact Lie-module obstruction, or fermionic A01 rotation-rigidity theorem. It reuses their appropriate algebraic certificates without inheriting their different premises.

SC-ACT-01/05 provide source action/variation grammar, not necessity of W2 or this Q family. SC-OP-04/05 retain independent-field candidate grammar and rivals. SC-ACT-06 concerns a Euclidean Upsilon deformation complex, not this Lorentzian candidate principal flow. Source2+1, literal contraction, K77/K95 and full-U/optional-C remain distinct. No source claim, physics-ledger row, class-C or GU verdict changes.

**Established:** Q cannot be promoted to an autonomous freely initialized Q-range-only graph; additional range components are required in this category. **Ruled out:** every nonzero SO3 submodule inside the owned Q as such a closed principal-flow family. **Undetermined:** the enlarged coupled flow, propagated states, stability, physical admission and GU consistency.

## Quick20 reassessment and continuation

1 Linear algebra: determinant certificate avoids new inverses. 2 Representation theory: two quotient highest classes force at least four copies. 3 Clifford algebra: grade7/8 parity proves canonical isotropy. 4 Differential geometry: actual graph/remaining-R distinction retained. 5 Constrained PDE: tangency is necessary for the actual equation. 6 Functional analysis: no propagation-domain theorem follows. 7 Symplectic geometry: all-Q isotropy supplies the annihilating rows. 8 Gauge theory: no BRST quotient is imported. 9 Category theory: constrained variations are not automatically dynamical states. 10 Number theory: exact Gaussian rationals/root bounds certify strict determinant negativity. 11 Algebraic geometry: two certified root neighborhoods, not all backgrounds. 12 Topology: no boundary implication. 13 Index theory:60 is a coefficient dimension, never a family index. 14 Anomaly theory: no new anomaly premise. 15 Variational calculus: full reciprocity removes every auxiliary-kernel ambiguity. 16 Perturbation theory: order-two leakage cannot be canceled by lower graph terms. 17 Harmonic analysis: free horizontal profiles are explicit. 18 Krein theory: zero self-energy lines do not annihilate the full dual form. 19 Observability: Q remains diagnostic rather than source-required physical content. 20 Decision theory: actual dynamical coupling is a better next question than certifying an optional universal lift.

The optional full-R-lift programme should now be deferred unless a concrete necessary bridge to the actual dynamical/observable question makes one of its remaining sources useful. This is result-dependent prioritization, not a new stop gate. A worthwhile successor is a bounded test of the **forced coupled range flow**—whether the actual generated additional directions satisfy the necessary closure/constraint conditions and change a stability or propagation decision—reusing existing receivers and minimizing new ones. The lower bound does not authorize choosing an arbitrary four-copy completion or launch an all-lower-block inversion programme. Nov26g counterfactual suites remain proposal-only.


## Separate hostile review

# Independent hostile review: Q7 principal propagation

Review target: admitted `RUN-20261126-gu-q7-propagation`, GU basis
`4578af6d992be339395cf3d7e97eca8bd03689d6`, worktree
`/private/tmp/gu-q7-propagation-wt-20261126`. This reviewer did not author the
probe, proof or Lean file, did not alter owner truth, and ran no heavy job.

## Disposition

**Accept the scoped mathematical obstruction**, subject to the final owner text
retaining the operator/domain limits below and the lead's successful Lean/native
validation. The argument is stronger than a failed inverse attempt: it uses the
actual connection-block principal equation and a full two-row nonsingularity
test. It is weaker than a physical ghost, propagated instability, exclusion of
Q initial data in a larger system, a W2 action inconsistency, or GU falsification.

The quantitative lower bound is valid for an **SO3-invariant R-valued connection
subsystem governed by the held-metric connection Hessian**, containing Q and
closed under the stated degree-two principal flow: at least four geometric
spin7 copies, hence at least60 real coefficient dimensions. Do not state this as
a bound on every fully coupled metric/fermion/GU state space without checking its
additional principal responses. The present proof does not analyze those added
response maps.

## What I inspected independently

- The author derivation `gu-q-propagation-parity-20261126.md`.
- Installed `source_action_q7_propagation_probe.py` and the actual native output
  `/private/tmp/gu-q7-propagation-native.json`.
- The native `Engine.shiab`, `Phi`, actual reversed-factor `Phi_adj`, diagonal
  trace/form pairing, and `symbols` definition in the authenticated dependencies.
- The prior actual derivative-source/energy code: it uses the same `tau=theta3`,
  `xi=theta0`, and range amplitudes `K_dt b5`, `K_dt b12`; it solves complete
  spin6/lowered-spin7 sources, with the latter zero for these two amplitudes.
- The algebraic statements in `Lean/GUFormalization/Q7Propagation.lean`.
  This is inspection of their mathematical scope, not a separate compiler run.
- Applicable AGENTS and GEOMETER-VS-PHYSICS T02/T09/T10/T11/T12/T13/T15/T17
  distinctions, plus source-native/comparator routing.

A light independent check recomputed all seven frozen dependency byte hashes,
validated the positive/negative interval separation, and recomputed the exact
rational determinant upper bound at each root. Rounded displays are
`-5.855034267964793e12` and `-2.395048126301717e13`; only rational values are
acceptance inputs. This does not claim to rebuild the inherited N6 matrices or
root certificates. Their explicit authenticated reuse is appropriate.

## Hostile challenges and resolutions

### 1. Indefinite does not imply anisotropic

Opposite diagonal signs alone do NOT imply that every nonzero vector has
nonzero quadratic energy. The2x2 form has null quadratic lines. The argument
works because tangency into **Q as a whole** forces pairing against BOTH Q test
rows to vanish, including rows outside a proposed smaller submodule U. The whole
Q satisfies `h(Q,AQ)=0`, so `H(Q,v)=0`, not merely `H(v,v)=0`. With
`det H=ad-|z|^2<0`, this yields `v=0`. Keep this explicit in the owner proof.

### 2. Whole-Q canonical isotropy is proved, not sampled

Native Phi contains an odd total Clifford-factor count in each term: phi1,
or phi1 with phi2. Star acts on exterior masks only; multiplication uses XOR.
The actual adjoint reverses the same factors with diagonal weights, so it has
the same odd Clifford parity. Wedge by a scalar covector preserves that parity.
Thus every `K_xi` reverses Clifford parity. Both seed vectors b5,b12 have degree8;
the authenticated V vectors have degree7 and their A-images degree8. Rotations
act on the form leg and by even bivector commutators, preserving parity.
Consequently all descendants and all cross-copy combinations obey `h(Q,AQ)=0`.
The probe's four zero pairings corroborate this structural statement; they are
not the entire proof.

### 3. The principal equation uses the right operator

For the held-metric connection block, `H=A partial_t + K^a nabla_a + J` and
`N=ker A`, with native nondegenerate orthogonal splitting R/N. The source
constraint supplies `M y_v=P K_xi v`. Inserting `n=-y(derivative v)+...` gives,
up to the common formal/Fourier sign, the degree-two R-velocity
`D2 v=G K_xi y_v`. `P K_xi P=0` puts the right side in R before G. Coefficient,
connection and lower-source derivatives contribute lower differential orders,
so they cannot cancel this coefficient for freely prescribed local amplitudes.
This argument does not require existence of a full reduced PDE on every R field.
It is a necessary principal tangency condition for the claimed subsystem.

### 4. Unknown auxiliary kernel cannot repair the tested rows

For any `M z=0`, skew-adjoint K, orthogonal P and reciprocal M give
`h(u,K_xi z)=-h(PK_xi u,z)=-h(M y_u,z)=-h(y_u,Mz)=0`.
Both row sources have owned preimages. No unexamined full-M inverse is assumed;
no assertion that the full kernel is zero is required. The cross-entry of H is
Hermitian by the same reciprocity, so it need not be numerically evaluated.

### 5. Fixed submodule and realification limits

Every nonzero real SO3-submodule of the owned real Q has a nonzero highest vector
in its complexification, in the span of V5,V12. A fixed range subbundle closed
under the local equation for arbitrary scalar amplitudes must pass the theta0
principal test for that vector. The row nonsingularity contradicts it. This
excludes fixed SO3 local-module truncations. It does not exclude momentum-dependent
polarizations, spatially homogeneous or specially constrained jets, nonlocal
physical state selections, quotient closure, or solutions whose range data
leave Q. Those alternatives are not established by this theorem either.

### 6. Why the additional two-copy bound follows

The Q rows see only output weight7/spin7: the native form and A are SO3-equivariant,
and the ambient carrier has maximum spin7. If a linear combination of the two
projected highest7 velocity outputs lies in Q, the same two-row argument forces
its two input coefficients to vanish. Hence there are two independent highest7
classes modulo Q. Any SO3-invariant R subsystem containing Q and these outputs
has highest7 multiplicity at least4. Integer-spin7 real irreducibles have
real dimension15, giving at least60 real coefficient dimensions. This is a
geometric representation/closure count, never a physical particle spin or
family count, and it is only a lower bound: other components may be required.

## Final acceptance conditions

1. Identify the held W2/K95 connection-block operator and both stationary root
   boxes; keep source necessity of W2/Q and physical admission unproved.
2. Retain the whole-Q pairing argument and two-row condition. Do not replace it
   by a claim that the indefinite quadratic form has no null vectors.
3. State fixed SO3 subbundle, free local amplitudes and principal closure;
   distinguish actual initial data from an autonomous truncation.
4. Scope the60-dimensional bound to the specified R-valued connection subsystem;
   include extra coupled-field principal terms only after a typed check.
5. Bind the installed probe and output bytes. Record the inherited-certificate
   reuse honestly and the lead's actual Lean/gate results.
6. Lean verifies the small determinant/kernel algebra. Native parity, actual
   source mapping, analytic root-box custody, SO3 realification and the PDE
   identification remain separately validated mathematics; do not call the
   complete physical theorem Lean-verified.

Within these conditions: **ESTABLISHED** is the native two-row obstruction and
minimum enlarged connection closure; **RULED OUT** is freely initialized,
nonzero fixed SO3-submodule Q-only range dynamics for this connection block;
**NOT MODELED / UNDETERMINED** includes the physical quotient, actual admissible
propagation, instability, fully coupled escape/closure, source necessity and GU.

## Final owner-draft pass

I inspected `explorations/conditional-build/source-action-q7-propagation-2026-11-26.md`
after the lead integrated the held-metric connection scope, fixed-submodule/free
profile hypotheses, extra-field and momentum-dependent exclusions, six-lemma
Lean scope and the matched descriptor-consistency distinction. These satisfy the
substantive hostile conditions above. The descriptor differentiation has the
correct sign and retains derivative-of-coefficient and auxiliary-kernel terms.
The reported existing sandwich cancellation is a leading-order simplification,
not a claim that the consistency chain already closes.

One required wording precision in proof section1: define H and the pure-N6
preimages on the tested highest span `Q_high=span_C{V5,V12}`, rather than claiming
all fixed-theta0 sources from arbitrary Q descendants are pureN6. General Q
responses can use the complete N6/N7 ownership already available. The proof only
needs the two authenticated highest rows; this correction changes no result.

Subject to that exact wording correction and the lead's final recorded native
checks, **the scoped T1 result is accepted by this hostile reviewer**. The Lean
source contains no `sorry`; its six statements express the determinant/kernel
core, including an explicit null-quadratic-vector countercontrol. Compiler
success was reported by the lead; this reviewer does not claim an independent
second compilation or full-PDE formalization.



## Later scope reconciliation: owned complete quadratic autonomy

The initial held-metric caveat is resolved at these exact real zero-matter roots by the already-owned imaginary-sector autonomy theorem. No new coupled-Hessian assembly is claimed. The later reviews below supersede metric/matter perturbations as a linear repair escape, while preserving all nonlinear, physical and GU ceilings.

# Review addendum: metric variations do not repair the linear Q obstruction

**Confirmed from the existing owned theorem; no proof reopening is needed.**

`explorations/conditional-build/source-action-coupled-ghost-2026-11-25.md`, §1 “The actual action and a coupled sector,” explicitly proves autonomy of the imaginary-Clifford connection sector in the **complete coupled quadratic W2 system**, including metric and real-connection variations. Its stated premises are the real stationary T0, real Clifford coefficients of geometry/B/Phi, the real trace action, and zero background matter. Mixed real/imaginary products have imaginary trace, so their real quadratic cross terms vanish; moving metric/Clifford/reference terms remain real. Zero-background matter also decouples linearly.

The same source expressly applies this theorem to the two certified kappa1 roots. `source-action-kappa1-constraints-2026-11-25.md` frontmatter fixes those roots as real zero-matter backgrounds; its “Propagation and energy exchange” subsection reiterates quadratic matter/boson decoupling and says the first mixed cubic bosonic vertex has two imaginary fields and one real field. The new Q vectors are in that same actual imaginary-Clifford real sector, with complex highest-weight notation returned to its real SO3 module.

Therefore the Q principal-flow obstruction is not an artifact that can be canceled by turning on a linear metric, real-connection or zero-background-matter perturbation. Their equations cannot supply a term in this autonomous imaginary block. The new T1 result may be stated as an obstruction **inside an autonomous block of the complete coupled linearized W2 equations**. The computation holds the certified background fixed, as every linearization does; it does not need an additional assumption freezing allowed metric perturbations.

The extra required range components are additional imaginary-connection R components. Allowing linear perturbations in the other coupled fields does not remove the at-least-four spin7-copy /60-real-coefficient-dimensional lower bound under the same SO3/free-Q-flow premises. This remains a coefficient-subsystem lower bound, not a count of physical degrees of freedom or particle families.

Preserve the prior limits: nonlinear imaginary fields can backreact at quadratic order; no invariant nonlinear truncation is claimed. A different nonzero-matter or non-real background, source action choice, physical quotient/domain and full GU remain outside the theorem. The result does not prove instability, a propagated ghost, or nonexistence of restricted Q-supported solutions.

This addendum strengthens only the already-owned coupled-linear scope; the native probe, exact replay and principal isotropy/source-form proof in `gu-q7-propagation-second-specialist-review-20261126.md` remain unchanged.


## 12. Prior full-quadratic decoupling bridge

The pre-existing
`source-action-coupled-ghost-2026-11-25.md`, Section 1, explicitly establishes
autonomy of the imaginary connection sector in the complete coupled quadratic
system at real Clifford T0 and zero background matter, including metric and
real connection variations. The later
`source-action-kappa1-constraints-2026-11-25.md`, Section 5, repeats the
coefficient-conjugation evenness and the first mixed cubic interaction with
two imaginary fields and one real field. Both held roots lie in the real59
coefficient family, so this premise applies here.

The symmetry argument is sufficient and does not require a new full matrix
assembly. If C is the coefficient-conjugation involution, the real bosonic
action satisfies S(C fields)=S(fields); the held background is C-fixed.
Metric and real connection variations are C-even, including their real
moving-frame and reference-connection contributions. Imaginary connection
variations are C-odd. Thus for any even variation e and odd variation o,

    Hess S(e,o)=Hess S(Ce,Co)=-Hess S(e,o)=0.

Equivalently mixed products have imaginary trace and disappear from the real
action. Both occurrences of i in the native Shiab recipe are retained, leaving
its real coefficient formula; none is silently removed to obtain this
symmetry. The matter action is at least quadratic in the independent matter
row/column fields, and both background matter fields are zero. Hence its
boson-matter mixed Hessian also vanishes there. The matter quadratic block can
remain nonzero without creating linear forcing of the imaginary connection.

Consequently adding metric, real-connection, or matter perturbations cannot
cancel the imaginary R equation's principal Q leakage at these backgrounds.
The Section 6 bound persists as a necessary condition on the **imaginary
connection R projection** of any full quadratic subsystem that contains the
unrestricted Q local module and closes its flow. At least four spin7 copies
are required in that projection; this does not count all coupled-system
variables or prove that those four copies suffice.

This reuses the owned quadratic decoupling, rather than claiming a new complete
coupled-Hessian calculation. It does not prove nonlinear autonomy: cubic terms
with two imaginary fields can source real fields at quadratic order in the
equations. It also does not convert a failure of unrestricted Q module closure
into failure of specially restricted Q solutions, a propagated ghost, an
action inconsistency, or a source/GU conclusion.


## Coupled-sector addendum: prior autonomy bridge checked

This addendum supersedes the hypothetical linear extra-field repair escape in
conditions4 and the earlier three-state paragraph; it does not change the
connection-count interpretation or claim a physical ghost obstruction.

I read the owned `source-action-coupled-ghost-2026-11-25.md` §1 (lines107–123),
`source-action-reduced-evolution-2026-11-26.md` §1 (lines84–102), and the prior
coupled-ghost hostile review load-bearing check3. The bridge is explicit, not
inferred from the new held-metric calculation:

- The held geometry, reference connection B, Phi and stationary T0 have real
  Clifford coefficients. Coefficient conjugation splits the real U(64,64)
  connection space into real grades1,2 mod4 and i times grades0,3 mod4.
- The action uses the real trace pairing. Real/imaginary mixed terms have
  imaginary trace and hence vanish in the real quadratic action. Metric and
  moving Clifford/reference variations are real, so their mixed Hessian terms
  with the imaginary connection sector also vanish.
- At zero-background matter, boson/matter mixed Hessian terms vanish. Thus the
  imaginary connection block is autonomous inside the complete quadratic W2
  system at both real certified kappa1 roots. The predecessor states this
  extension to both roots explicitly, independently of its large-kappa result.
- V5 and V12 and their SO3 descendants are represented by i times Clifford
  degree7, hence lie precisely in this imaginary-U block. The new leakage
  calculation is on that actual block, not a different complexification.

Consequently real metric, real connection, and zero-background matter
perturbations cannot repair the Q-only principal closure failure at this linear
order. It is valid to state the Q7 obstruction inside the full quadratic W2
system and to remove those fields from the list of linear repair escapes. The
at-least60 count remains a count of imaginary connection R coefficients: in any
full invariant linear system containing Q, its projection to this autonomous
imaginary connection sector must have the required enlarged closure. This does
not count metric degrees of freedom or physical particles.

**ESTABLISHED:** the existing coupled Hessian is block diagonal by conjugation
at the stated real zero-matter backgrounds; the extra linear fields listed
above cannot cancel the imaginary-block leakage.
**RULED OUT:** freely initialized nonzero fixed-SO3 Q-only imaginary-connection
range dynamics, even when the other linearized real metric/connection and
zero-background matter fields are present.
**NOT MODELED / UNDETERMINED:** physical quotient/admission, actual propagated
instability, nonlinear backreaction, different or non-real/nonzero-matter
backgrounds, momentum-dependent or constrained-jet completions, and source/GU
necessity. Nonlinear imaginary fields can backreact at quadratic order; no
nonlinear truncation is proved.

Hostile disposition: **accept this limited strengthening**. It reuses an
already-owned exact symmetry argument, needs no new coupled assembly, and does
not promote the candidate result to a GU or physical-ghost exclusion.
