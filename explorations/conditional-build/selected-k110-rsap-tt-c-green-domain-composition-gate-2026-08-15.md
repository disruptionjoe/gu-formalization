---
title: "Selected-K110 RSAP TT spectral-C and Green-domain composition gate"
status: active_research
doc_type: exact_fixed_background_positive_fibre_majorant_green_domain_composition_and_carrier_gate
created: "2026-08-15"
registry: lab/process/selected-k110-rsap-tt-c-green-domain-composition-gate.json
probe: tests/channel-swings/selected_k110_rsap_tt_c_green_domain_composition_gate_probe.py
grade: "THE FIXED-BACKGROUND TT SPECTRAL C AND OBSERVED TWO-FIELD GREEN SYSTEM COMPOSE EXACTLY ON THEIR SHARED 2D PENCIL, GIVING A POSITIVE FIBRE MAJORANT PRESERVED BY THE GREEN OPERATORS; THE RESULT IS NOT A CLOSED SELF-ADJOINT QUANTUM DOMAIN, FAILS FOR VARIABLE BACKGROUND WITHOUT DERIVATIVE COMPLETION, AND HAS NO INVARIANT MAP INTO THE 98D RSAP/BFV CARRIER"
target_claim: K109_CLOSEST_SEAM__THE_FIXED_BACKGROUND_TT_C_AND_OBSERVED_GREEN_SYSTEM_COMPOSE_INTO_THE_FULL_98D_RSAP_POSITIVITY_DOMAIN_PACKET
target_verdict: PARTIAL__YES_ON_THE_SHARED_CONSTANT_BACKGROUND_2D_OBSERVED_DEFECT_AT_GREEN_GRADE__NO_AT_CLOSED_QUANTUM_DOMAIN_STATIONARY_TOTAL_FIELD_OR_98D_BFV_GRADE
canon_verdict_change: none
---

# Selected-K110 RSAP TT spectral-C and Green-domain composition gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> Krein, observed-defect and RSAP/BFV carrier question. Ordinary Higgs/VEV,
> family-index, net-chirality, anomaly, symmetry-breaking and familiar
> four-dimensional gauge-model conclusions do not adjudicate it. Read
> `lab/methods/source-native-comparator-routing.md` before importing any such
> comparator.

Classification: `SOURCE_NATIVE_ROUTE`.

## Result in plain English

K109 separated the strongest positivity result from the strongest analytic
result too sharply. They are not unrelated objects. They are two structures
on the same selected two-field gravitational TT pencil.

At a fixed constant scalar background, the spectral `C(u)` and the observed
Green operator compose exactly:

- `H(u)=K C(u)` is a positive-definite fibre metric on the free-connected
  real-spectrum component;
- the normalized field operator is `D_u=Box I+L(u)` and is normally
  hyperbolic on the inherited globally hyperbolic observed defect;
- `C(u)` commutes with `D_u` and preserves compactly supported test sections
  and spacelike-compact Green images;
- `D_u` is formally symmetric for the positive fibre metric `H(u)`; and
- uniqueness of advanced/retarded Green operators gives
  `C G_u^+ = G_u^+ C` and `C G_u^- = G_u^- C`.

So one real seam closes: positivity and Green propagation can coexist on the
same conditional `2D` observed-defect carrier.

That is not yet the packet K109 required. The result is a positive **fibre
majorant on a Green test core**, not a proved positive conserved energy,
self-adjoint Hamiltonian domain, Fock space, loop-unitary theory or BFV
cohomology. The supplied constant background is not proved stationary for the
complete action. If `u=u(x)` varies, `C(u(x))` no longer commutes with `Box`;
new first- and zero-order derivative terms appear. And K107's invariant
subquotient classification contains only `49D` copies of the balanced module,
not a `2D` invariant subquotient. There is no current invariant attachment of
this TT package to the conditional `98D` RSAP/BFV carrier.

## 1. Shared carrier and action ownership

Both predecessors use

```text
K = [[alpha,1],[1,0]],        det K=-1,
M_0 = [[0,0],[0,b]].
```

The first selected cubic contributes, at supplied constant scalar background,

```text
M(u)=M_0+u vv^T,              v=(1,1),
u=2 c theta_bar,
L(u)=K^-1 M(u).
```

The interaction and Hessian are selected-action owned. The value
`theta_bar`, its constancy and complete-action stationarity are supplied
conditions, not derived owners. The Green theorem uses the already declared
observed globally hyperbolic defect horn; it is not an ambient `Y14`
ultrahyperbolic theorem.

## 2. Exact positive Green-grade composition

The characteristic discriminant is

```text
Delta(u)=(b+u)[alpha^2 b+(alpha-2)^2 u].
```

On the component containing `u=0`, both factors are positive and

```text
C(u)=[2L(u)-tr(L(u))I]/sqrt(Delta(u)),
H(u)=K C(u)>0.
```

The predecessor identities are

```text
C^2=I,      [C,L]=0,      C^T K=K C,      det H=1.
```

They imply the new composition identity

```text
H L=L^T H.
```

Indeed, `H L=K C L=K L C=L^T K C=L^T H`. Thus

```text
D_u=Box I+L(u)
```

is formally symmetric for `H(u)`. Because `u` and therefore `C` are constant,

```text
[C,D_u]=[C,L(u)]=0.
```

Constant finite-fibre multiplication preserves `C_c^infinity` and
spacelike-compact support. Normal hyperbolicity is unchanged by `L(u)`, which
is lower order. If `G_u^+` and `G_u^-` are the unique advanced and retarded
Green operators, both `C G_u^+` and `G_u^+ C` solve the same supported inverse
problem, and likewise for `G_u^-`; uniqueness yields exact commutation.

This constructs a compatible positive fibre majorant and Green propagation
package without a new fitted coefficient.

## 3. Three exact ceilings

### Constant background is load-bearing

For `u=u(x)`, multiplication by `C(u(x))` gives

```text
[Box,C] psi=(Box C)psi+2(grad C).(grad psi).
```

The exact derivative `dC/du` is nonzero generically. The fixed-background
commuting square therefore does not globalize by pointwise substitution. A
moving completion would have to derive and cancel the derivative terms from
the complete action/connection; no such completion is currently owned.

### Green grade is not a closed quantum domain

The existing theorem supplies the common core `C_c^infinity` and
spacelike-compact Green images. Finite-fibre `C` preserves them and extends
boundedly on ordinary Sobolev completions. This does not select a time
evolution generator, boundary condition or self-adjoint realization on a
positive Hilbert space. It also does not erase the previously computed
opposite residues of the original metric response. Amplitude, energy and
physical-state positivity remain separate tests.

### The `2D` package is not the `98D` RSAP

At the balanced zero section the phase tangent is

```text
M=R^2 tensor U,               dim U=49,
```

and every nonzero proper `H_bal`-invariant linear subquotient has dimension
`49`, with signature `24|25` up to sign. Hence this `2D` TT package is not an
invariant linear subquotient of the balanced phase tangent. A future
attachment must be non-invariant and owned by an actual stationary background,
boundary law or total BV/BFV map. Dimension matching by itself cannot provide
that map.

## 4. Correction to K109 and reverse-scaffold disposition

K109's zero-of-nine eligibility verdict survives, but one explanatory sentence
is superseded. The TT `C` and observed Green domain do share a carrier and now
have an exact typed composition at Green grade. The balanced BFV carrier
remains a different object.

The current inventory is therefore better summarized as:

```text
positive fibre metric + Green propagation on conditional 2D TT defect: YES
closed positive quantum domain on that defect:                           NO
stationary complete-action background:                                  NO
typed attachment to conditional 98D RSAP/BFV:                            NO
```

Keep Variancer's reverse scaffold through the exact classical `98D` RSAP/BFV
layer. The next worthwhile bridge is no longer “can positivity and propagation
coexist at all?” It is an action-owned stationary total-field or boundary map
that embeds or descends the observed package into the actual BFV complex and
controls the moving-background derivative terms.

## Claim ceiling

This is an exact fixed-constant-background, two-field, observed globally
hyperbolic defect result. It is not an ambient `Y14` domain, nonlinear
symmetry, stationary-vacuum theorem, positive conserved-energy theorem,
self-adjoint quantum realization, Fock construction, loop/UV result, physical
BFV cohomology or `98D` positivity theorem. It neither proves `H-Q*` nor `H0`.

No ledger, datum, quotient booking, canon, public posture, particle,
phenomenology or GU truth-status claim changes. Reproduce:

```bash
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/selected_k110_rsap_tt_c_green_domain_composition_gate_probe.py
```
