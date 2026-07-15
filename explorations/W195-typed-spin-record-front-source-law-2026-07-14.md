---
artifact_type: exploration
label: W195
status: "exploration (bounded World-B calibration implemented; execution intentionally not run in this wave; no claim, canon, verdict, or posture movement)"
created: 2026-07-14
title: "W195 - Signature-conditioned typed Spin(9,5) World-B record-front calibration"
verdict: "IMPLEMENTED / EXECUTION NOT RECORDED. The bounded verifier constructs a conditional 91-generator Spin(9,5) connection subsector, real representation-K calibration action, correctly typed variational current, a one-dimensional initial-value record front, state-dependent adjoint contraction, local joint gauge quotient, rival/completion controls, and an ordered World-B source trace. The fixture is preregistered to classify as dynamic selection inside a fixed whole-family-completable theory and to refuse World C/source issuance. W201/W202 reconciliation is explicit: this branch does not select (9,5) over (7,7), identify its representation K with the DeWitt reservoir sign or interacting C metric, or construct the independent generation-count datum. W203/W205 reconciliation further demotes this fixture from a source-law candidate to a typed calibration: it neither imports W203's branch-3 source action and record current nor resolves W205's independent physical branch bit. Execution remains pending, so no PASS count or computed scientific result is claimed. Full Sp(32,32;H), actual I1B/star_shiab identity, a physical shared-carrier overlap, retarded rho_J, interacting C metric, and physical poles remain absent."
depends_on:
  - explorations/W194-w192-reciprocal-packet-intake-gate-2026-07-14.md
  - explorations/W192-explicit-carrier-kernel-spectral-gate-2026-07-14.md
  - explorations/W201-count-external-datum-characterization-2026-07-14.md
  - explorations/W202-signature-crux-bach-branch-2026-07-14.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/W205-source-action-reverse-engineering-condorcet-2026-07-14.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
---

# W195 - Signature-conditioned typed Spin(9,5) World-B record-front calibration

## Branch choice

Build the 91-generator `spin(9,5)` connection subsector already represented by
the repository's 128 by 128 Clifford matrices. It lies inside the conditional
`(9,5)` reconstruction and its candidate native noncompact `Sp(32,32;H)`
structure, repairs W180's current type, and avoids treating a first test as an
8,256-generator full-Sp result. W202 leaves `(9,5)` versus `(7,7)`
underdetermined, so this fixture tests one declared branch and is not a
signature selector.

A success is a bounded Spin-subsector pipeline result. A failure kills only
this branch unless the reason is representation-independent.

## W201/W202/W203/W205 reconciliation

The post-draft GU sync added two constraints that narrow this fixture without
invalidating it:

1. W202 proves that the `(9,5)` versus `(7,7)` signature remains
   underdetermined. W195 is therefore a conditional `(9,5)` branch, not the
   native signature selected by the dynamics.
2. W202's signature-invariant reservoir sign lives on the DeWitt `(6,4)`
   fiber. W195's matrix `K` is the invariant form of the chosen Clifford
   representation. No map identifying those two forms, activating an
   interacting physical `C` metric, or carrying the fiber sign into the
   `(alpha,beta)` weights is built here.
3. W201 separates the order-two Krein selector from the independent order-three
   generation-count magnitude. W195 constructs neither the Y14 source-action
   pushforward nor that count datum, even if a future construction shows that
   the two arcs share an operator.

These are executable output guards in the verifier, not interpretive
afterthoughts.

The later W203/W205 source-action work adds a second, sharper boundary:

4. W203 builds an ultralocal branch-3 parent action with a Schur-forced
   indefinite kernel and a record current, conditional on the W154
   record-current identification and the interacting `C`-operator question.
   W195's polynomial order-parameter potential was chosen only to make a
   bounded front fixture. It is not that source action, and its 91-component
   adjoint current is not identified with W203's frame/connection-distortion
   current.
5. W205 reduces the remaining source-action ambiguity to one independent
   physical branch bit. Choosing a `K`-positive seed in W195 is a calibration
   restriction; it neither derives nor measures that bit.

Accordingly W195 is no longer described as Action-2 native source evidence. Its
remaining role is narrower and still useful: verify that a correctly typed,
state-conditioned Spin-subsector construction lands in E177 World B and is
absorbed by the fixed-family controls.

## Expected source classification

This proposal is preregistered as a typed **World B calibration**: dynamic
selection inside a fixed, whole-family-completable field theory. It is not a
presumptive source-extension result.

For the Temporal Issuance adapter, define the candidate event exactly as the
gauge-orbit class of the first regular formed front,

```text
e_n = [Psi_star]_gauge at the first slice with ds != 0 and ds.ds != 0.
```

The typed current and front contraction are witnesses and downstream outputs,
not interchangeable definitions of the event. A separate aspirant World C
track may open only if later evidence establishes algebra/admissibility growth
and defeats the complete fixed action/seed/boundary/solution/adapter family.

## Fields and action

On a source-first observer section `(X4,g)`, take a commuting effective record
order parameter

```text
Psi: X4 -> C^128,
A_mu = A_mu^{AB} Sigma_AB,
D_mu Psi = partial_mu Psi + A_mu^{AB} Sigma_AB Psi,
s[Psi] = Psi^dagger K Psi.
```

The commuting spinor is a classical or mean-field test object. Its later
quantization is not assumed.

Use the real gauge-invariant action

```text
S_rec = integral sqrt(|g|) [(D_mu Psi)^dagger K D^mu Psi - U(s)],
U(s) = lambda/(4 v^4) s^2 (s-v^2)^2.
```

For the structural build, `lambda=v=1` set units and are not predictions.

## Typed current and invariant form

Varying all 91 connection coefficients must give

```text
J^mu_AB = 2 Re[(D^mu Psi)^dagger K Sigma_AB Psi]
         in Omega^1(X4, spin(9,5)^*).
```

Raise the algebra index only through the computed nondegenerate trace form

```text
B_{AB,CD} = -Re Tr_S(Sigma_AB Sigma_CD),
Jhat^mu = B^{AB,CD} J^mu_AB Sigma_CD.
```

No positive-Hilbert replacement is allowed.

## State formation and record front

The primary implementation must be an initial-value evolution, not a two-sided
completed-history solve. Pre-register the background connection, finite slab,
an initial state near `s=0`, one incoming boundary condition, and a localized
target-blind seed with enough declared energy to test barrier crossing. Evolve
the hyperbolic Euler-Lagrange system forward and define, where `s>0`, `ds != 0`,
and `ds.ds != 0`,

```text
Psi_star = EvolveEL(S_rec; A0, initial_data, incoming_boundary),
psi = Psi_star / sqrt(Psi_star^dagger K Psi_star),
n_mu = partial_mu s / sqrt(|partial s . partial s|).
```

The action derives the phase profile and norm. Initial data and the seed select
the orbit direction. This is state selection, not a claim of unique actuality
or issuance. A two-sided `s=0 -> s=v^2` boundary-value solution may be retained
only as an analytic positive control and must be labeled completed-history
input, never source evidence.

## Bounded adjoint-valued adapter

The primary Action-2 adapter is

```text
(Phi_ad^[Psi_star] F)_mu^{AB} = n^nu[Psi_star] F_{nu mu}^{AB}.
```

For this test branch, declare the complete candidate composite to be interior
contraction by the record-front normal. It is typed, state-dependent, and gauge
covariant, with

```text
n^mu (Phi_ad F)_mu = 0.
```

It is not asserted to be GU's written `star_shiab` or the final I1B map.

One simple rival is the state-independent codifferential symbol

```text
(Phi_k F)_mu^{AB} = i k^nu F_{nu mu}^{AB}.
```

The actual fixed-source rival family must be broader: constant and variable
symbol contractions `i_q F`, including `q(x)=n[Psi](x)`; finite mode mixtures;
the codifferential on the nonplanar background; every predeclared parameter,
initial state, seed, boundary, and access schedule; and quotient-equivalent
local operators. The constant-`k` comparison is only a calibration control.

## Gauge quotient and Ward identity

For background `(A0,Psi_star)`, quotient linearized perturbations by

```text
G(epsilon) = (D_A0 epsilon, -epsilon Psi_star).
```

A finite implementation may use a declared positive auxiliary norm to choose a
representative,

```text
P_quot = I - G (G^sharp G)^+ G^sharp,
```

but all physical signs must use `K`, `B`, and `g`. Verify `P_quot^2=P_quot` and
`P_quot G=0`.

Gauge invariance must yield the off-shell identity

```text
D_mu J^mu_AB + 2 Re[E_Psi^dagger K Sigma_AB Psi] = boundary flux.
```

On shell with zero admitted flux, `D_mu J^mu_AB=0`.

## Holdouts and rival controls

Freeze the background, boundary data, state solution, front normal, quotient,
and one source-first carrier mode before response coefficients are evaluated.
Calibration may consume `v` and one overall source normalization. It may not
consume the response residues.

Hold out:

1. the exact front-transversality relation;
2. W191's response rank/minor relation for the derived shared-carrier rank;
3. a separate-carrier control that generically violates the rank-one case;
4. a positive prediction-codimension check over all admissible selectors;
5. comparison against the complete frozen rival family, not only constant `k`;
6. the ordered E177 record vector over initial records, provenance, and all six
   perturbation traces.

The World B control must enumerate its represented completion family across
allowed initial data, seeds, gauge orbits, solution branches, regular front
normals, and contraction adapters. It is expected to factor through the fixed
universal evaluation `(q,F) -> i_q F` and therefore to fail W1, W4, and W5.

For the TI interface, map all six `Adapter_P` fields, `tau_n`, `Preserve_n`,
family index, and provenance even though the expected source verdict is
negative. No claimed dynamic-formation or nonfactorization boolean is accepted
as input; the verifier derives it.

## Kill conditions

Kill or exit this branch if:

1. the action is not exactly real and gauge invariant;
2. finite variation does not reproduce the typed current;
3. the Ward residual survives beyond admitted boundary flux;
4. no finite-action regular front exists in the initial-value problem without
   target fitting;
5. every formed state is gauge-equivalent with no invariant front/current effect;
6. the adapter factors through or is quotient-equivalent to the frozen rival
   family, for any claim stronger than World B;
7. physical current/carrier overlap vanishes after quotient;
8. selector freedom gives full response rank and no holdout relation;
9. the commuting spinor cannot admit a consistent later total C metric;
10. the result requires calling this contraction GU's actual shiab without a
    source receipt.

## Immediate test matrix

The implementation should test representation and K-adjointness, trace-form
rank and invariance, action reality and gauge invariance, analytic versus
finite-difference current, off/on-shell Ward identities, fixed-seed front
formation, front normalization, adapter typing/covariance/rank, gauge quotient,
current/carrier overlap, rank-minor holdouts, and rival separation.

It must also emit the full World B source trace, run all E177 perturbations,
show the fixed-family zero-error absorber, and refuse World C when any H7/T2
certificate is missing.

No `|II|^2/R^2`, generation index, measured `mu_DW`, positive-Hilbert ghost
removal, spacetime SUSY, or RS field-strength vertex may enter this build.

The fixture also may not be used to select `(9,5)`, infer the W168/W202
reservoir sign from its representation-level `K`, activate the interacting
`C` metric, or supply W201's independent generation-count datum.

## Honest boundary

Implementable without fitted physics: the complete finite algebra/type/action
pipeline and a dimensionless initial-value World B front fixture.

This calibration action/potential is not GU's selected source law. New source
input remains required for why GU would select it,
physical section and boundary data, the status of a commuting spinor order
parameter, physical scales, relation to actual I1B `star_shiab`, full Sp,
interacting C metric, retarded response, and physical poles.

Implemented verifier: `tests/W195_typed_spin_record_front_source_law.py`.

## Implementation receipt

The verifier is now present but was deliberately not executed in this wave.
It implements the smallest deterministic calibration that does not require a
large solve or fitted physics:

1. reuse of the verified `Cl(9,5)` matrices and construction of all 91
   `Sigma_AB` generators;
2. `K`-anti generator/type checks and the trace-form identification from
   `spin(9,5)^*` to `spin(9,5)`;
3. action reality, finite bounded Spin covariance, all-index analytic current,
   and representative finite-difference variation;
4. algebraic off-shell and on-shell Ward identities;
5. a positive-signature one-dimensional velocity-Verlet initial-value front
   with no supplied final boundary;
6. the adjoint-valued contraction `i_n F`, its transversality, bounded rank,
   covariance, and constant-symbol rival;
7. a local joint gauge quotient using an explicitly auxiliary positive
   numerical norm;
8. W191 rank/minor positive and separate-carrier controls;
9. an ordered World-B trace with the six E177 perturbation classes, all six
   `Adapter_P` fields, `tau_n`, `Preserve_n`, represented family index, and
   provenance;
10. exact fixed-family completion by the universal evaluator `(q,F) -> i_q F`,
    forcing W1/W4/strict-W5 failure and refusing World C.

The one-dimensional calibration does not implement Lorentzian hyperbolic
record formation or a nonplanar physical
current/carrier survivor. Its front current is normal while `i_n F` is
tangential, so the verifier records their quotient overlap as zero and keeps
`physical_shared_carrier_established=false`. This is an honest limitation of
the bounded fixture, not a failed physical calculation and not evidence for a
larger no-go.

Deferred rather than simulated: a Lorentzian hyperbolic record-formation solve,
a full nonlinear 128-component spacetime solve, complete continuous rival
family, full native `Sp(32,32;H)`, actual
`I1B` identification, interacting Hamiltonian and `C` metric, retarded
spectral density, physical boundary, scale, and pole sheet.

Root command for a later authorized execution:

```text
python -u tests/W195_typed_spin_record_front_source_law.py
```
