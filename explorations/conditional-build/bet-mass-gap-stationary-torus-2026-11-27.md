---
status: exploration
doc_type: structural-result
created: '2026-11-27'
title: Every stationary compact Pati-Salam torus background retains physical Hessian zero modes
program_target: BET-MASS-GAP
tier: T1
expected_delta: Close the nonflat stationary-background escape for the existing compact-positive MG1 full
  quadratic gap on the same flat three-torus.
actual_delta: All stationary endpoints in the declared compact PS flat-torus category retain physical
  Hessian zero modes; strictly positive full quadratic gap excluded.
class_covered: All smooth static source-free MG1 Yang-Mills connections, zero background electric field,
  on all principal compact PS product or diagonal-Z2 quotient bundles over fixed closed flat T3; positive
  invariant pairing and full periodic H2 Gauss/Coulomb quotient by vertical internal gauge.
premises:
- explorations/conditional-build/bet-mass-gap-pati-salam-holonomy-2026-11-25.md
- explorations/conditional-build/bet-mass-gap-stability-topology-2026-11-24.md
- explorations/conditional-build/signature-generic-cartan-ward-compose-2026-08-08.md
- lab/sources/source-claim-register.yaml#SC-GRP-03
- lab/sources/source-claim-register.yaml#SC-PRE-52
- https://arxiv.org/abs/0808.0667
source_bridge:
  status: conditional
  reason: The source supplies related compact group and representation data, not the positive MG1 action,
    flat torus, static magnetic sector, full physical state space or identification of this classical
    Hessian with a native or quantum mass observable.
kill_condition: Failure of global bundle admission, Jacobi/Coulomb identity, non-gauge positivity or the
  inherited flat-PS carrier theorem invalidates this closure. Success excludes only a strictly positive
  full quadratic Hessian in the named comparator category.
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
internal_target: INTERNAL-MG1-PS-STATIONARY-T3-FULL-POSITIVE-GAP
internal_target_verdict: internal scoped exclusion; no bet-wide kill or source verdict
---

# No stationary endpoint restores the full MG1 quadratic gap on this torus

```yaml
program_target: BET-MASS-GAP
tier: T1
expected_delta: Replace nonflat stationary-background construction by an all-stationary theorem.
actual_delta: Global translation-Jacobi class closure; finite exact and Lean checks below.
```

Basis: freshly fetched `630b7f50b7fce50efb614d36cb15958b1a4636ff`.
This is the carried LC discovery slot under unchanged `program_focus`. No new
action, background, coefficient, physical quotient or choice family is added.

> **GU-COMPARATOR-ROUTING — scope before inference.** Classification:
> `CONVENTIONAL_COMPARATOR`. The result binds compact-positive MG1 on the stated
> torus and physical quadratic domain. It is not a GU, source, class-C or quantum
> mass-gap verdict. Follow [source-native routing](../../lab/methods/source-native-comparator-routing.md).

```gu-typed-objects
result: all-stationary compact PS torus physical Hessian kernel
carrier: adjoint connection one-forms on every admitted compact PS bundle over fixed flat T3 LAYER=toy CHIRALITY=N/A
pairing: positive Ad-invariant compact Lie algebra pairing and spatial L2 ON=adjoint_one_forms
real_structure: compact real Lie algebra and real smooth bundle sections; not native K77/K95 Krein data
grading: Gauss/Coulomb quotient by vertical internal gauge; no family/chiral grading
action_owner: comparator -- existing MG1 positive Yang-Mills energy, no new action
target: complete smooth and H2 Coulomb physical Hessian at every stationary magnetic background MAP-TYPE=quotient
```

## 1. Result

Let G be the already-owned PS product SU(4) x SU(2)L x SU(2)R or its quotient
by the diagonal central element (-I4,-I2,-I2), on which the complete16 is honest.
Let P be any such principal bundle over a fixed closed flat three-torus.
At **every** smooth source-free stationary magnetic MG1 connection A, the full
Gauss/Coulomb quadratic operator has a nonzero kernel. In fact:

- If F_A is nonzero, curvature contractions with global parallel vector fields
  give **at least two independent physical Jacobi fields**.
- If F_A is zero, the owned full-PS holonomy classification supplies kernel
  dimension3 or9 in nonzero central-flux sectors, and at least15 in zero flux.

Therefore no m>0 satisfies K_A >= m^2 I on the **entire** physical quadratic
space in this category. Searching another smooth nonconstant stationary
background on the same flat torus cannot restore that full positive gap.

| State | Exact meaning |
|---|---|
| ESTABLISHED | All stationary endpoints in this fixed comparator category have physical Hessian zero modes; nonflat modes come from exact symmetry-generated stationary families. |
| RULED OUT | Strict positivity of the entire MG1 physical quadratic Hessian on the named torus/bundle/domain category. |
| NOT MODELED / UNDETERMINED | Native GU/Krein transfer, other geometry, electric/time-dependent states, matter-coupled dynamics, selected charged spectra, extra collective-coordinate quotients and an interacting quantum gap. |

A positive spectral threshold **above** a removed zero-mode sector is a different
question. A zero mode can be a collective coordinate rather than a local
particle. This theorem does not equate those concepts.

## 2. Existing action, domain and source custody

Use exactly the [owned MG1 normalization](bet-mass-gap-stability-topology-2026-11-24.md#1-source-boundary-and-common-conventions):

    E(A) = (1/2) integral sum_(i<j) |F_ij|^2,
    F_ij = partial_i A_j - partial_j A_i + [A_i,A_j],
    q_A(a) = ||d_A a||^2 + 2 <F_A, a wedge a>.

The time formulation is R_t x T3, temporal gauge, static background and zero
background electric field. Write

    E_i = sum_j D_j F_ji.

Stationarity is E_i=0. On Coulomb fields D_A^*a=0, the owned Hessian is

    (K_A a)_i = -sum_j D_j D_j a_i - 2 sum_j [F_ij,a_j].

The base metric and volume are fixed and flat. All adjoint bundle sections are
periodic in the bundle sense, not necessarily globally periodic matrix-valued
functions in a chosen trivialization. The form domain is the full H1 Coulomb
space; the corresponding smooth elliptic Hessian has H2 domain. Smooth global
sections on this compact manifold lie in both domains. At a stationary A,
gauge invariance makes the Hessian descend to the Gauss quotient.

SC-GRP-03 (2021 draft p29, equation4.6) and SC-PRE-52 (TOE2025,
02:52:38, transcript720–726) motivate the related compact group/representation
comparison. SC-GEO-55 (TOE2025,02:18:44) and SC-GEO-58 (UCSD2025,00:42:42)
do not specify positive compact Yang-Mills on T3 or
this full Hessian as the physical mass observable. The native total group,
K77/K95, independent bars, contraction observation and source2+1 remain distinct.
The proof uses no observation projection and extracts no generation count.

## 3. Exact off-shell identities

Choose a global parallel orthonormal frame e_k on the flat torus and put

    a_i^(k) = F_ki.

Antisymmetry immediately gives D_A^*a^(k)=E_k. Thus these fields are Coulomb
on every stationary background, without solving an extra gauge-fixing equation.

Linearizing the complete stationary equation gives

    delta E_i[a] = sum_j {D_j(D_j a_i-D_i a_j) + [a_j,F_ji]}.

Bianchi gives D_j F_ki - D_i F_kj = D_k F_ji. Consequently

    delta E_i[a^(k)]
      = sum_j {D_j D_k F_ji + [F_kj,F_ji]}
      = D_k E_i + sum_j {[F_jk,F_ji] + [F_kj,F_ji]}
      = D_k E_i.

This identity is **off shell**. It is not zero unless stationarity (or a
separately justified weaker condition) supplies that conclusion. On a
stationary Coulomb field, K_A=-delta E, so K_A a^(k)=0. Dropping the variation
of the connection in D_j would miss the bracket term and spoil the identity.

## 4. Global bundle and exact-family proof

There is also a geometric proof, useful because a global matrix gauge need
not exist. Horizontally lift a parallel vector field X to P using A. The lift
is equivariant, and its flow is complete: P is compact because both base and
structure group are compact. The flow covers a torus translation, hence an
isometry of the fixed base. Its pullback sends A to connections on the **same**
bundle, preserving the source-free Yang-Mills equation.

Cartan's formula for the principal connection form gives the tangent
L_(X^H) A = i_(X^H) F_A, since A(X^H)=0. Thus a_X=i_X F_A is the tangent to
an exact family of stationary connections. Differentiating the equation yields
the Jacobi identity above. No lift of the torus group action with special
periodicity is assumed: the one-parameter bundle flow suffices, and its return
may differ by a vertical gauge transformation.

Translations here are global symmetries of a fixed-metric Yang-Mills problem.
They are not vertical internal gauge transformations. Declaring translations
or collective coordinates gauge would change the tested quotient. This
argument does not prove that the entire stationary moduli space is smooth.

## 5. Nonzero, independent and not pure gauge

With the two-form norm summing over i<j,

    sum_k ||a^(k)||^2 = 2 ||F_A||^2.

For nonflat A this is positive. More strongly, choose a point p and indices
i!=j with F_ij(p)!=0. If r a^(i)+s a^(j)=0 for real constants r,s, evaluating
component i at p gives -s F_ij(p)=0, hence s=0; component j then gives
r F_ij(p)=0, hence r=0. So at least two global Jacobi fields are independent.
A nonzero real linear functional on that Lie-algebra component reduces this
to the finite scalar coefficient argument checked in Lean.

For any Coulomb a in the above domain and any admissible gauge parameter epsilon,

    <a,D_A epsilon> = <D_A^*a,epsilon> = 0.

If a=D_A epsilon, positivity implies ||a||^2=0 and a=0. The same orthogonality
holds for the L2 closure of gauge derivatives. Hence every nonzero contraction,
and every nonzero constant linear combination of the independent pair, remains
nonzero in the physical linearized quotient.

A residual vertical gauge stabilizer of A fixes F_A itself, and therefore fixes
its contractions. It does not remove these vectors. Large gauge identifications
likewise do not turn a nonzero tangent orthogonal to the gauge image into a
zero vector. No smooth full-moduli dimension is inferred.

## 6. Flat case, positive control and an independent sign check

For F=0 the contraction proof supplies no witness. The
[complete owned flat-PS theorem](bet-mass-gap-pati-salam-holonomy-2026-11-25.md)
is essential: in the product/diagonalZ2 category the common parallel adjoint
algebra h has dimension1 or3 for nonzero central flux, and at least5 for zero
flux. Its full physical kernel is h tensor H1(T3;R), of dimension3 dim(h).
The projective representation classification is reused with its exact carrier
and dependency bindings, not rerun or generalized to every compact group.

The flat twisted SO(3) comparator with no adjoint fixed vector still has a
positive quadratic gap. It evades the nonflat branch because F=0 and the flat
PS branch because its group/bundle category differs. This is a necessary
positive control against a false universal compact-group claim.

An independent three-dimensional check is [Stern, section4, equations4.2–4.3](https://arxiv.org/pdf/0808.0667).
For a stationary connection on flat T3, b=*F is Coulomb by Bianchi and d_A b=0
by Yang-Mills. The Bochner identity in the owned normalization gives
q_A(b)=-||nabla_A F||^2. Thus nonparallel curvature also has a negative physical
direction. This uses the displayed identity, not an extension of Stern's
minimizer theorem to arbitrary stationary points. Parallel curvature need not
be stable; the primary translation argument already supplies zero modes.

Translation variations and these classical identities are established methods.
The new repository delta is closing the previously open **all-stationary MG1
PS torus category**, not a claim of a new theorem unknown to the literature.

## 7. What the result changes

The bet's previous continuation requested a nonconstant stationary endpoint
and its full physical Hessian. On this same flat torus and full compact MG1
category, that endpoint search is now unnecessary: the theorem covers every
such endpoint. The flat PS result is strengthened in scope, not regraded.

This does not close BET-MASS-GAP itself. Nonflat or curved **base geometry**,
electric/time-dependent backgrounds, a different source-admitted action,
a physically specified charged sector, a different global/spin-charge bundle
category, or an interacting quantum mechanism are distinct. A nonflat
**connection on the same flat base**, by itself, is no longer that escape.
None of these alternatives is constructed or promoted to a default here.

No LC output enters matrix cells, the assumption view, a ledger or canon.
The candidate choice inventory10/4/net6/0 is unchanged. The due discovery
slot is consumed once; the next B alternative remains the native K95
Riemann-response transfer. The unrelated cosmology endpoint instruction is
marked consumed against its already-published evidence, with no extra bet
credit. The W2-displacement normalization idea remains an unexecuted opportunity.

## 8. Verification and preflight decision record

Root exact replay passed172 checks in0.088655 seconds; deterministic certificate
21,224bytes. Targeted single-thread Lean compilation passed all four finite
lemmas, with no warnings or placeholders. These checks do not replace the
written global theorem or its independent review.

[Exact probe](../../tests/program-focus/bet_mass_gap_stationary_torus_probe.py),
[certificate](../../lab/process/bet-mass-gap-stationary-torus-certificates.json),
[finite Lean core](../../Lean/GUFormalization/StationaryTorus.lean),
[evidence and review](../../lab/process/bet-mass-gap-stationary-torus.json).

Selection used the new reuse index and targeted owner searches because the
initial index omitted these bet reports. Flat Wilson-line deformations,
quartic obstructions and density-only tests were already covered. The new
question changes the next action: a valid global Jacobi field eliminates
another background-construction loop; a failed domain/type condition names
the specific surviving escape. Expected cost: one small analytic/exact/review
wave, no dense inverse or endpoint search. Measured checks and final hash-bound
reviews are recorded in evidence. The strongest alternative, K95 transfer,
remains B-class work rather than being relabeled as discovery credit.

The exact probe checks finite algebra and declared fixtures; Lean checks only
its stated finite core. Global bundle flow, elliptic domain, integration by
parts, source scope and inherited flat-PS completeness receive written
independent review. No full PDE or quantum theory is claimed Lean-formalized.
