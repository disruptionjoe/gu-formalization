---
title: "Selected-K112 RSAP spectral-connection variational owner port"
status: active_research
doc_type: exact_local_covariant_tt_quadratic_stationary_background_boundary_bfv_and_invariant_attachment_gate
created: "2026-08-15"
registry: lab/process/selected-k112-rsap-spectral-connection-variational-owner-port.json
probe: tests/channel-swings/selected_k112_rsap_spectral_connection_variational_owner_port_probe.py
grade: "THE K111 SPECTRAL CONNECTION HAS AN EXACT MINIMAL LOCAL QUADRATIC VARIATIONAL OWNER WITH NO FREE CONNECTION COEFFICIENT; THIS IS A RECONSTRUCTED ACTION EXTENSION, NOT A TERM OWNED BY THE CURRENT RELEASED ACTION. THE TT SECTOR DOES NOT SELECT THE MOVING BACKGROUND AT ZERO TT FIELD, ITS GREEN FLUX IS NOT THE BALANCED BFV LAW, AND NO NONZERO H_BAL-INVARIANT LINEAR 2D-TO-98D ATTACHMENT EXISTS. STATIONARY BACKGROUND, NONINVARIANT OR NONLINEAR BV-BFV MAP, POSITIVE CLOSED DOMAIN AND PHYSICAL COHOMOLOGY REMAIN OPEN"
target_claim: K111_NEXT_GATE__THE_SPECTRAL_CONNECTION_HAS_A_LOCAL_VARIATIONAL_OWNER_AND_CURRENT_ACTION_BACKGROUND_BFV_DATA_PROMOTE_IT_TO_THE_CONDITIONAL_98D_PHYSICAL_PACKET
target_verdict: MINIMAL_VARIATIONAL_OWNER_CONSTRUCTED_AT_RECONSTRUCTION_GRADE__CURRENT_SERIALIZED_SOURCE_OWNER_STATIONARY_BACKGROUND_PHYSICAL_BFV_DOMAIN_AND_TYPED_98D_ATTACHMENT_NO
canon_verdict_change: none
---

# Selected-K112 RSAP spectral-connection variational owner port

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> variational, Krein/Green and balanced BV-BFV carrier question. Ordinary
> Higgs/VEV, family-index, net-chirality, anomaly, symmetry-breaking and
> familiar four-dimensional gauge-model conclusions do not adjudicate it.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K111's connection is not merely an operator covariantization. It has an exact
minimal local quadratic variational owner.

On the gapped two-field TT bundle, put

```text
A_C=(1/2)C dC,              nabla_A=d+A_C,
L_TT,C(phi;u)
  =(1/2)<nabla_A phi,K nabla_A phi>
   -(1/2)<phi,M(u)phi>.
```

Because `A_C` is `K`-skew, the normalized Euler operator is exactly

```text
D_A=Box_A+K^-1 M(u).
```

Its first-order coefficient is `2A_C`; its connection zero-order coefficient
is `div A_C+A_C^2`. No coefficient is fitted. Thus the unique connection from
K111 also fixes a canonical minimal quadratic action at reconstruction grade.

That positive result does **not** close action ownership in the source-native
sense. The displayed selected cubic supplies the variable mass block but no TT
derivative Hessian. The released action census does not display the covariant
TT quadratic above. Adding it is new reconstructed action data, not discovery
of a previously owned term.

The other three required owners also remain absent:

- at `phi=0`, this TT quadratic contributes zero to the `u` Euler equation, so
  it does not select a nonconstant stationary moving background;
- its canonical Green flux is compatible with `C`, but is not the right-
  `H_bal` zero-level equation, gauge declaration, ghost domain or positive
  physical quotient; and
- an invariant linear map from this `2D` package into the conditional `98D`
  phase tangent must vanish. Its nonzero image would have dimension at most
  two, while K107 proves every nonzero proper invariant linear subquotient has
  dimension `49`.

The exact gain is therefore sharp: the missing connection has a variational
completion, and the remaining obstruction is no longer “perhaps no action can
own it.” It is that the current source/action does not own this term or the
background, BFV law, domain and non-invariant attachment needed around it.

## 1. Layer-0 object and owner typing

The local TT object is

```text
K=[[alpha,1],[1,0]],                 det K=-1,
M(u)=M_0+u vv^T,                    v=(1,1),
L(u)=K^-1 M(u),
C(u)=[2L-tr(L)I]/sqrt(Delta),
H(u)=K C(u)>0.
```

This is a real rank-two field bundle over the observed globally hyperbolic
defect, restricted to the simple-real-spectrum component. The distinct phase
object is the conditional balanced tangent

```text
M_bal=R^2 tensor U,                 dim U=49,
dim M_bal=98,
H_bal=Spin(3,4)xSpin(4,3).
```

K112 does not identify them. It asks separately whether the first admits a
variational completion and whether any current owner maps it into the second.

The ownership labels are:

```text
mathematical variational owner:     constructed below;
current released/source action:     does not display the new derivative term;
stationary moving u owner:          absent;
balanced boundary/gauge owner:      absent;
closed positive physical domain:    absent;
typed non-invariant 98D map:         absent.
```

## 2. Exact minimal variational completion

Work first in one coordinate; the spacetime formula is its metric contraction.
For

```text
q=nabla phi=phi'+A phi,
L_kin=(1/2) q^T K q,
```

the Euler expression `d/dx(partial L/partial phi')-partial L/partial phi`
is

```text
K phi'' + (K A-A^T K)phi'
 + (K A'-A^T K A)phi.
```

K111 gives

```text
A^T K+K A=0.
```

Therefore

```text
K A-A^T K=2K A,
K A'-A^T K A=K(A'+A^2),
```

and normalizing by `K^-1` yields

```text
phi''+2A phi'+(A'+A^2)phi=nabla_A^2 phi.
```

Adding the mass quadratic gives `nabla_A^2+K^-1M(u)` up to the declared
overall action-sign convention. The multidimensional formula is
`Box_A+L(u)`. This reproduces every first- and zero-order connection
coefficient in K111.

There is no new connection coefficient: `A=A_C` is already uniquely fixed by
simultaneous `K` compatibility and `C` parallelism. A different compatible
connection has zero difference on the simple rank-one eigenspaces, as K111
proved.

This action is minimal, not a uniqueness theorem for the complete nonlinear
theory. Terms vanishing to quadratic TT order, total divergences, other field
sectors and nonlinear completions remain unclassified.

## 3. Source/action and stationary-background ceiling

The selected cubic is

```text
V_3=c theta(q_0+q_m)^2.
```

Its TT Hessian produces `u(x)vv^T`, a zeroth-order block. It has no TT
derivative Hessian and cannot print the `2A_C partial` or
`div(A_C)+A_C^2` terms. The checked released action census likewise does not
display the covariant TT kinetic quadratic constructed here. Consequently:

```text
minimal local variational completion exists:        YES;
current selected cubic owns it:                      NO;
released source action displays it coefficientwise: NO;
full action could contain or induce it:              OPEN.
```

The completion also fails to choose its own moving background. Every term in
`L_TT,C` is quadratic in `phi` and its derivative. Its variation with respect
to `u` therefore vanishes at the zero-TT background `phi=0`, including the
dependence through `A_C(u,du)`. A nonconstant stationary `u(x)` must be selected
by another field sector or a nonzero coupled saddle.

K105's current owner census has five serialized stationary-carrier classes and
zero full local stationarity survivors. K112 neither repeats that census nor
counts unconstructed future backgrounds as failures. It proves only that the
new TT quadratic does not repair the empty input by itself.

## 4. Boundary and BFV port

The variational completion has the canonical covariant Green flux

```text
j_n(phi,psi)
 =phi^T K nabla_n psi-(nabla_n phi)^T K psi.
```

Because `nabla C=0` and `C^T K=K C`,

```text
j_n(C phi,psi)=j_n(phi,C psi).
```

Thus the two spectral sectors are respected by the Green boundary pairing.
This is real progress over a pointwise fibre metric: the moving completion is
variationally and boundary compatible on the same TT system.

It is still the wrong type to select the reverse RSAP. K98's BFV charge lives
on the `182D` cotangent parent with 42 right-`H_bal` constraints. K103 and K104
show that the `98D` quotient additionally needs a zero-level boundary equation
and right-gauge declaration, neither supplied by the released source. The TT
Green flux above is a bilinear concomitant for the two-field wave operator; it
is not the `h_bal^*`-valued moment map and does not manufacture either owner.

The finite classical master equation therefore remains exact, while analytic
BFV domain, positive quotient pairing and physical cohomology remain open.

## 5. Invariant linear attachment obstruction

K107 classifies the conditional balanced zero-section tangent as

```text
M_bal=R^2 tensor U,
```

and proves that every nonzero proper `H_bal`-invariant linear subquotient has
dimension `49`. Suppose a nonzero invariant linear map from the TT carrier
`T`, `dim T=2`, into `M_bal` existed. Its image would be an invariant subobject
with

```text
1 <= dim image <= 2,
```

contradicting the exact `49D` minimum. Hence the invariant linear map is zero.

This does not prohibit the route the program actually needs. A stationary
background may break `H_bal`, a nonlinear map can have a different tangent
story, and boundary or cohomological attachment need not be a fibrewise linear
intertwiner. Those are not present, but they are not killed by this argument.

## 6. Reverse-scaffold disposition

Retain the conditional classical stack:

```text
balanced seed and right-gauge law: explicit reverse conditionals;
98D symplectic realization:        exact;
minimal classical BFV charge:      exact;
TT spectral connection:            exact kinematic construction;
minimal TT variational owner:       exact reconstruction-grade candidate.
```

Do not append a physical layer. The next admissible owner packet must contain
all of:

1. a source- or action-owned smooth gapped stationary moving background;
2. a coefficientwise occurrence of `A_C`, or an exact equivalent, in the
   complete linearization;
3. a non-invariant, nonlinear, boundary or cohomological map into the actual
   balanced BV-BFV complex;
4. the selected zero-level and right-gauge law;
5. a common closed positive physical domain and pairing.

Another fixed-background spectral calculation, invariant dimension match, or
finite classical BFV replay cannot satisfy this packet.

> **Successor closure (K113).** The K112 connection reduces exactly to
> `A_C=G dphi` with closed-form transport `exp[-(phi(u)-phi(u0))G]`. It vanishes on
> the gapped but unselected `alpha_II=1` locus. Boundary-only/BFV-only data
> cannot generate its interior first-order coefficient, although boundary
> domain selection and non-invariant/boundary/cohomological attachment remain
> open. The next owner test is therefore the action normalization of
> `alpha_II` or an action-derived moving-TT Jacobian match to this transport.

## Claim ceiling and reproduction

This is an exact local quadratic variational reconstruction and current-owner
classification. It is not a source-confirmed action term, complete nonlinear
action, stationary solution, positive conserved-energy theorem, self-adjoint
quantum realization, `98D` physical embedding, quantum BFV cohomology, Fock
construction, particle model, phenomenology result or GU truth-status change.

Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k112_rsap_spectral_connection_variational_owner_port_probe.py
```
