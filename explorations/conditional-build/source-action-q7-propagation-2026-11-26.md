---
title: Canonical isotropy forces additional connection dynamics
status: active_research
doc_type: conditional-build-result
program_target: LB-CLASS
tier: T1
expected_delta: Decide actual principal dynamic isolation of all fixed SO3 submodules of the owned two-Q7
  sector using existing exact certificates
actual_delta: At both kappa1 roots, every nonzero fixed SO3 submodule of the tested two-copy Q7 fails
  autonomous connection-range principal evolution. Any SO3-invariant connection subsystem containing Q
  and closed under that flow needs at least four spin7 copies (60 real coefficient dimensions). No physical
  ghost, action or GU exclusion.
class_covered: Autonomous imaginary-connection block of the complete quadratic W2/K95 system at both certified real zero-matter kappa1 root boxes; fixed real SO3
  submodules of the two-copy Q7, arbitrary local horizontal profiles and constraint-compatible local principal
  response; quadratic decoupling reused from the owned full-system theorem
premises:
- 'source-action-coupled-ghost-2026-11-25.md section 1: complete quadratic imaginary-sector autonomy at real zero-matter roots'
- "source-normal-tensor-class-2026-11-26.md sections6.3\u20136.5: actual Q constraint lift, remaining\
  \ R equation explicitly open"
- 'source-action-reduced-evolution-2026-11-26.md section2: same theta0 and V5/V12 root-box signs'
- 'source-action-kappa1-constraints-2026-11-25.md: complete N6/N7 inverse certificates (machine evidence
  is authoritative)'
- 'source-adjoint-spinless-placement-2026-11-26.md: primary-minus versus plus-comparator distinction'
source_bridge:
  status: conditional
  reason: Actual equation test on the repository-built connection candidate. Neither W2 nor the diagnostic
    Q sector is source-required. Autonomous Q-only evolution would require this tangency; physical/source
    necessity is absent.
kill_condition: Whole-Q canonical isotropy plus an invertible two-row source form excludes the stated
  freely initialized fixed Q-only dynamic class. It never excludes Q initial data in larger coupled systems, W2 itself, class C or GU.
---

# Canonical isotropy forces additional connection dynamics

program_target: LB-CLASS
tier: T1
expected_delta: Decide fixed Q-submodule tangency to the actual connection time evolution
actual_delta: At both kappa1 roots, every nonzero fixed SO3 submodule of the tested two-copy Q7 fails autonomous connection-range principal evolution. Any SO3-invariant connection subsystem containing Q and closed under that flow needs at least four spin7 copies (60 real coefficient dimensions). No physical ghost, action or GU exclusion.

```gu-typed-objects
result: kernel-independent principal-flow obstruction for fixed Q-only connection dynamics
carrier: W2 K95 connection one-forms, N=ker K_dt, R=N-perp and real Q=V7 plus V7 LAYER=ambient BRIDGE=owned-quadratic-sector-autonomy CHIRALITY=N/A
pairing: native imaginary-U trace/form pairing and omega(u,v)=h(u,K_dt v) ON=declared_carrier
real_structure: native conjugation, full real SO3 modules; no new positive physical form
grading: Clifford parity and geometric rotation weight; neither is a physical chirality or family index
action_owner: repository-construction source-action W2 imaginary connection Hessian, autonomous at the held real zero-matter roots
target: principal time-flow map from Q into R modulo Q MAP-TYPE=homomorphism
```

## Result and scope

Basis: fetched clean `4578af6d992be339395cf3d7e97eca8bd03689d6`. The Q diagnostic consists of two real geometric spin7 modules, 30 coefficient dimensions. It already admits smooth auxiliary-constraint solutions. The new result tests the **remaining R equation**: no nonzero fixed rotation-invariant submodule can evolve autonomously with arbitrary local horizontal profiles while its range component stays in Q. A connection subsystem containing all Q requires at least two additional spin7 copies, for at least 60 real coefficient dimensions.

This concerns the **imaginary-connection block of the full coupled quadratic W2 system** at these real zero-matter backgrounds. The owned coefficient-conjugation theorem makes this block autonomous: metric, real-connection and matter perturbations cannot cancel its linear principal response. The 60 bound therefore applies to its imaginary-connection range components even within the coupled quadratic system. It is not a bound on every GU realization, nonlinear completion or physical quotient. Q was a diagnostic family, not an asserted physical sector. The result does not reject Q initial data in a larger system, special solutions, momentum-dependent polarizations, spatially restricted jets or source-admitted physical quotients.

The principal calculation is unchanged at the two previously certified stationary roots. It neither establishes a path from the small-h branch nor constructs a new action, norm, background or selection law. Source 2+1, imposter gamma-trace placement, independent fields, contraction observation, K77 versus derived K95, and total versus physical grading remain distinct. Geometric spin7 is not a particle-spin or generation claim.

## Why the proposed successor changed

The previous 22-channel source census is valid. Its 16 uncovered channels (rank 15) concern extension of an auxiliary inverse from Q to unrestricted R. Neither the sources nor W2 require that unrestricted inverse. A genuine cokernel there could impose a restriction on allowed R jets; it would not by itself falsify the equations. In particular the uncontracted first-jet sources do not contradict the already constructed smooth Q constraint lift.

The current test addresses actual dynamic tangency. It uses accepted coefficients and a structural identity instead of expanding another inverse. The optional full-R source quotient is retained as evidence and deferred until a necessary field/jet or physical-domain bridge makes its result decisive. This is factual research reranking under existing policy, not a new stopping rule.

## Proof

### 0. Reused full quadratic-sector autonomy

[Coupled-ghost section 1](source-action-coupled-ghost-2026-11-25.md#1-the-actual-action-and-a-coupled-sector) establishes the relevant symmetry. Coefficient conjugation fixes the real geometry, reference connection, Phi and real stationary T0, while it negates imaginary connection variations. Mixed real/imaginary quadratic terms have imaginary trace and vanish in the real action. Moving metric, Clifford and reference-connection variations are real. Zero-background matter has no mixed linear boson response. Thus the full quadratic Hessian is block diagonal between the imaginary connection block and these other fields at both held roots.

This is authenticated reuse of the existing theorem, not a new coupled-Hessian assembly or an additional frozen-metric assumption. Nonlinear imaginary fields can backreact at quadratic order in their amplitude. Changed backgrounds, physical quotients and nonlinear completion remain outside the present theorem.

### 1. Native operators and the dual test

At the point let `A=K_dt`, `N=ker A`, `P` its native orthogonal projector,
`R=1-P`, and `G=(A|R)^(-1)` with zero extension on N. The real physical imaginary
sector has symmetric form `b_phys=-b_raw`; write its complexification as
`h(u,v)=b_phys(conj(u),v)`. Native identities are

```
K_xi^* = -K_xi,   P^*=P,   M^*=M,
M=P(I+2N(T,.))|N,   P K_xi P=0.
```

For `u,v in the tested highest span Q_high=span_C{V5,V12}` define `s_v=P K_0 v` and choose an owned response
`y_v in N` with `M y_v=s_v`. The complete N6 certificate supplies this response on the tested highest span. General Q sources may also use the already certified N7 block. This supplies the required two-row response
at both roots (the actual two sources have no lowered-N7 component). Define

```
H(u,v)=h(s_u,y_v),
S2(v)=G K_0 y_v.
```

`K_0 y_v` lies in R by `P K_0 P=0`. Thus no full-M inverse is needed to form
this partial symbol. M self-adjointness makes H Hermitian:

```
H(u,v)=h(M y_u,y_v)=h(y_u,M y_v)=conj(H(v,u)).
```

Since `A S2(v)=K_0 y_v`, native skew-adjointness gives

```
h(u,A S2(v)) = -h(P K_0 u,y_v) = -H(u,v).       (1)
```

With `n=-Y_Q^a partial_a v` at principal order, the formal real-derivative velocity has the displayed plus sign. Fourier substitution changes its overall sign; the kernel/invariance test is unchanged. This is the degree-two term of this autonomous imaginary-connection R equation
obtained from the original first-order constrained equation with the already
owned Q lift. Lower-order terms cannot cancel this coefficient for arbitrary
smooth local amplitudes.

#### Independence from every unspecified auxiliary kernel correction

If another allowed response is `y_v+z`, `M z=0`, then

```
h(u,K_0 z) = -h(s_u,z) = -h(M y_u,z) = -h(y_u,M z)=0.   (2)
```

Hence the dual test (1) is unchanged by **any** full-native auxiliary kernel
correction. This is stronger and simpler than assuming a complete inverse on
all R sources. Equivalently, SO3 completeness says the unknown kernel has no
N6/N7 component, while K_0 is a vector symbol; but equation (2) already proves
exact independence without an extra decomposition computation.

### 2. Why Q is canonical-isotropic

The two owned highest vectors are exactly

```
V5=K_dt b5,      V12=K_dt b12.
```

The native 36-highest7 construction gives

```
b5:  zero axes [2,3,4,6],  Clifford degree8,
b12: zero axes [2,3,6,7],  Clifford degree8.
```

Let `chi` be Clifford grade parity, acting on every one-form coefficient by
`(-1)^grade`. In `Engine` the factor `phi1` has Clifford degree1 and `phi2`
degree2. Both terms of Phi contain an odd total number of Clifford gamma
factors (one, or one plus two). Hodge stars change exterior indices only;
Clifford multiplication changes masks by XOR. Therefore Phi reverses chi.
The native diagonal pairing commutes with chi, so Phi's actual adjoint also
reverses chi. Wedge by a scalar covector and its adjoint preserve chi. Consequently

```
chi K_xi = -K_xi chi
```

for every covector, without a numerical or special-root assumption.

Thus `V5,V12`, and all their SO3 descendants, have odd Clifford parity.
Rotations preserve this parity: their one-form action changes no Clifford mask,
and their spin action is a commutator with a Clifford bivector. Therefore
`Q` is odd and `A Q` is even. The native trace/form pairing is diagonal in
Clifford masks, giving

```
h(Q,A Q)=0.                                            (3)
```

The direct check in the probe also verifies the highest 2-by-2 canonical Gram
is zero and the ordinary native Hermitian Q Gram is
`diag(3145728,-9437184)`. Zero in (3) is independent of the overall physical
imaginary-sector minus sign. The whole-orbit assertion follows from the parity
proof, not from extrapolating four sampled pairings.

### 3. Exact reused roots and signs

In `source_action_reduced_evolution_probe.py`, the covectors are explicitly
`tau[3]=1`, `xi[0]=1`; its source loop uses indices `(5,7,12)`. The two rows
used here are exactly the same V5,V12 as above:

| index | range vector SHA256 | complete N6 paired source | lowered N7 source |
|---|---|---|---|
| 5 | `7236fdb46516a6658219f14c461837e7424b64d68ed9d584bd583a36cb86e57b` | index37: `3145728` | zero |
| 12 | `3678e4fb50fe53aada59a3f6e8329a7e4c7df7f208f476ee21a6475ebddf9d1d` | index40: `9437184` | zero |

Both active indices lie in the same existing 32-by-32 N6 constraint block.
The published rational preconditioners and their exact root-ball Neumann bounds
give the following strictly separated diagonal intervals for H (rounded here
only for readability; the executable uses the full rational strings):

| root | H(V5,V5) center | exact error bounded above by | H(V12,V12) center | exact error bounded above by |
|---|---:|---:|---:|---:|
| 0 | +1,484,675.20 | 6.04 | -3,943,678.64 | 16.04 |
| 1 | -3,347,101.37 | 26.13 | +7,155,700.56 | 55.86 |

They are `lab/process/source-action-reduced-evolution.json`
`exact_probe.physical_derivative_energy[0 or 1].witnesses`, selected by
`basis_index=5 or 12`. The physical convention there is exactly
`b_raw^* c`, where `c=-H_raw^{-1}b_raw`; it equals
`h(s,M^{-1}s)`, not its negative. The source bindings are at
`exact_probe.source_receivers`.

For a Hermitian 2-by-2 matrix `[[a,z],[conj(z),d]]` with opposite strict
diagonal signs,

```
det H=ad-|z|^2 <0.
```

No cross-entry evaluation is needed. If `p_lower>0` and `n_upper<0` are the
certified positive lower and negative upper bounds, then
`det H <= p_lower*n_upper <0` is an exact uniform root-ball bound.

### 4. Consequence for propagation and all multiplicity combinations

Suppose `v=c5 V5+c12 V12` and `S2(v)` belongs to Q. Equation (3) makes the
left side of (1) zero for both `u=V5,V12`; thus the 2-by-2 H matrix kills
`(c5,c12)`. Its determinant is strictly negative, so `c5=c12=0`.

Therefore the highest-multiplicity map

```
span_C{V5,V12} -> R_C / Q_C,
v |-> [S2_0(v)]
```

is injective at both roots, even after all kernel corrections in (2). The dual
rows use spin7 test vectors, so they detect an actual spin7 component outside
the particular two-copy Q, not merely an SO3-lowering artifact.

Every nonzero real SO3 submodule of the real two-copy Q has a nonzero highest
vector in its complexification. If its arbitrary scalar local sections were
preserved by the actual reduced time equation, its degree-two symbol would
preserve that submodule for theta0. The preceding injectivity contradicts this.
This excludes **every nonzero SO3 multiplicity combination of the two copies**
as such an unrestricted dynamic truncation. It does not say every individual
Q initial datum is excluded from every larger or constrained solution class.


### 5. Minimum additional connection content

Pairing with a highest-weight7 Q vector sees only weight7 and geometric spin7 in the output: A commutes with SO3 and the ambient carrier has no spin above 7. The two-row nondegeneracy therefore proves that the highest7 parts of the two output classes are linearly independent in R7/Q. Any SO3-invariant connection subspace containing Q and closed under this principal flow must contain those two extra highest vectors and their complete SO3 modules. It has at least four real spin7 copies, hence at least 4*(2*7+1)=60 real coefficient dimensions. This is only a lower bound; no particular four-copy completion is selected or constructed.

It is a bound on imaginary-connection range components, supported by the owned quadratic autonomy. Linear metric, real-connection and zero-background matter fields cannot repair it at these roots. Momentum-dependent state restrictions, a specified physical quotient, nonlinear or changed-background constructions require their own equations and transfer arguments. No physical particle or family count follows. The canonical-isotropy argument is a standard linear-algebra mechanism applied here to the actual candidate, not a claim of a new general mathematical theorem.

### 6. Actual constraint propagation remains a different question

Write the stationary descriptor system as

    A partial_t v + B v + E n = 0,
    D v + M n = 0,

where B,E,D are the complete spatial/lower differential operators, not isolated source columns. With G=A^{-1} on R, consistency of the second equation requires

    M partial_t n = D G(Bv+En) - (partial_t D)v - (partial_t M)n.

All allowed auxiliary-kernel multipliers in n=n0+k remain in this equation. The previous unrestricted-inverse source census is not this matched consistency source. The owned identity P K_xi G K_xi P=0 cancels the candidate cubic principal term after substitution; lower orders and all actual connection/projector terms remain to be assessed. The present theorem does not prove that this chain closes or that negative-energy initial data propagate.

## Verification and reproduction

The [probe](../../tests/program-focus/source_action_q7_propagation_probe.py) freezes seven predecessor hashes and replays the accepted complete-N6 inverse bounds and the four same-source diagonal intervals. It reconstructs the 36 highest7 seed recipe, exactly reproduces both range hashes, checks V has degree7 and A V degree8, verifies highest weight, and checks both native Grams. Whole-Q isotropy follows from the structural parity proof, not four sampled zero pairings. No new inverse, large receiver, floating rank or full-M assumption is used.

```sh
python3 tests/program-focus/source_action_q7_propagation_probe.py --repo . --output _local/q7-propagation.json
```

Full native replay passed in about 0.17 s. `--data-only` is explicitly partial and cannot stand in for the native parity checks. The [certificate](../../lab/process/source-action-q7-propagation-certificates.json) stores exact rational bounds; decimal summaries are explanatory only. Dependency, installed-probe and output hashes are recorded in the [evidence](../../lab/process/source-action-q7-propagation.json).

[Q7Propagation.lean](../../Lean/GUFormalization/Q7Propagation.lean) checks six algebraic implications without `sorry`: negative Hermitian determinant, two-row injectivity, source-row independence from kernel corrections, complex determinant nonvanishing, the resulting Hermitian kernel test, and a null-vector countercontrol. Targeted compilation passed, and the certificate is registered in the default import and owner inventories. An aggregate import check could not complete because the isolated cache lacks compiled artifacts for 26 unchanged predecessor modules; no full `lake build` is claimed. It does not formalize the full PDE, native parity implementation, CG classification or root-box computation; those are supplied by the reviewed proof and authenticated native certificates. Verified algebra is kept separate from validated statement alignment.

Two independent specialist reviews and a separate hostile review passed. The hostile review required the explicit connection-sector ceiling, pure-N6 scope on the two highest vectors, and the exclusions for momentum-dependent polarizations and restricted jets; these are incorporated above. All three reviewers subsequently confirmed the owned full-quadratic autonomy bridge, removing metric/matter perturbations as linear repair escapes at these roots. [Review record](../../lab/process/hostile-reviews/2026-11-26-source-action-q7-propagation-review.md). Seven native gates and protected-surface checks are recorded in the evidence.

## Three-state conclusion and continuation

- **ESTABLISHED:** canonical isotropy of whole Q, exact same-source sign reuse, kernel-independent rank 2 principal flow modulo Q, and the imaginary-connection 60-dimensional lower bound at both roots.
- **RULED OUT:** every nonzero fixed SO3 submodule of this Q as a freely initialized, arbitrary-profile autonomous local connection-range subsystem at those roots.
- **NOT MODELED / UNDETERMINED:** a closed enlarged subsystem, full Dirac consistency, propagated negative modes, stability/runaway exchange, physical cohomology, nonlinear or changed-background repair, global domain and source necessity. These are not asserted absent.

The next actual-equation discriminator is the matched constraint-consistency source above on the required coupled range data, retaining all kernel multipliers. It must decide whether negative constrained data can be preserved, require additional constraints, or remain unresolved; raw inverse nonmembership is insufficient. A supplied source-required physical domain/readout remains the stronger physical bridge. No arbitrary four-copy completion or automatic inverse backlog is selected.

Two specialists, a separate hostile reviewer and the 20-description reassessment (including category theory and number theory) are recorded in the evidence. These are simulated internal research roles, not independent external scientists. Candidate choices remain 10 grouped families / 4 obligation bundles / net 6 / zero source-selected predictions; the diagnostic Q was not a new physical choice. Scientific matrix cells, intersections, shrinkage, source/physics/canon/class-C verdicts and papers remain unchanged. Directed count 71 → 72 / LB-CLASS 30 → 31 records this result. The Nov26(g) counterfactual suites remain proposal-only; governance and schedules are unchanged.
