---
title: "Selected-K106 RSAP balanced-quotient positivity and ellipticity obstruction"
status: active_research
doc_type: exact_conditional_invariant_form_hamiltonian_and_principal_symbol_classification
created: "2026-08-15"
registry: lab/process/selected-k106-rsap-balanced-quotient-positivity-ellipticity.json
probe: tests/channel-swings/selected_k106_rsap_balanced_quotient_positivity_ellipticity_probe.py
grade: "THE CONDITIONAL 98D BALANCED QUOTIENT RETAINS ITS CLASSICAL SYMPLECTIC AND BFV CONSTRUCTION, BUT ITS UNIQUE INVARIANT ISOTROPY FORM HAS SIGNATURE 24|25 UP TO SIGN, SO NO CANONICAL INVARIANT POSITIVE KINETIC FORM, ELLIPTIC SCALAR PRINCIPAL SYMBOL OR SEMIBOUNDED QUANTIZATION FOLLOWS"
target_claim: CONDITIONAL_BALANCED_RSAP_HAS_CANONICAL_INVARIANT_POSITIVE_ELLIPTIC_KINETIC_QUANTIZATION
target_verdict: NO_AT_CANONICAL_G_INVARIANT_LOCAL_QUADRATIC_AND_SCALAR_SECOND_ORDER_GRADE
canon_verdict_change: none
---

# Selected-K106 RSAP balanced-quotient positivity and ellipticity obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: SOURCE_NATIVE_ROUTE`

Scope: the conditional reverse scaffold obtained after supplying the balanced
real-orbit seed `R_0`, the zero-level boundary equation and the declaration
that right `H_bal` is gauge. Those inputs remain unowned by the current source
action. The result classifies the canonical invariant local quadratic kinetic
form and scalar second-order principal symbol on the resulting `98D`
cotangent phase space. It does not classify every non-invariant, Krein,
constrained, contour, Wick-rotated, boundary-defined, interacting or nonlocal
quantization.

## Result first

The conditional `98D` balanced reverse RSAP remains a valid exact classical
symplectic realization, and its finite classical BFV master charge remains
closed. But it does not carry a canonical invariant positive kinetic theory.

The base is

```text
G/H_bal = Spin_0(7,7)/(Spin(3,4) x Spin(4,3)),
dim(G/H_bal)=49.
```

At the balanced point its isotropy module is

```text
p_bal = V_(3,4) tensor W_(4,3).
```

Each seven-dimensional standard factor has scalar commutant. The probe gives
exact commutator-system rank `48` in `49` unknowns for both `so(3,4)` and
`so(4,3)` over the prime `1,000,003`; identity supplies the rational kernel
line. A block argument then forces the product commutant on `p_bal` to be
scalar. Hence every `H_bal`-invariant symmetric bilinear form is proportional
to the tensor metric.

Its signature is exact:

```text
positive = 3*4 + 4*3 = 24,
negative = 3*3 + 4*4 = 25.
```

An overall sign only exchanges the two counts. Therefore no nonzero
`G`-invariant positive-definite quadratic form exists on the base tangent or
cotangent carrier.

The consequences are immediate and exact:

- the invariant fibre Hamiltonian has positive and negative quadratic rays
  and is unbounded above and below;
- the corresponding scalar second-order principal symbol has signature
  `24|25` and a nonempty null cone, so it is not elliptic; and
- local plane-wave symbols take arbitrarily large values of both signs, so
  the standard invariant scalar operator is not semibounded and has no
  canonical positive Friedrichs route.

This is not a failure of classical BFV. It is a failure of the inference

```text
classical symplectic quotient + nilpotent classical BFV charge
=> positive Hilbert space + elliptic domain + physical cohomology.
```

The left side remains exact and conditional. The right side does not follow.

## Layer 0 and owner fence

| object | status | not promoted to |
|---|---|---|
| `R_0` | explicit reverse-scaffold balanced seed | source/action-derived order parameter |
| `lambda_h=0` plus right gauge | conditional K99/K104 boundary law | released physical boundary principle |
| `T*(G/H_bal)` | exact `98D` classical symplectic realization | positive quantum phase space |
| minimal 42-ghost BFV charge | exact finite classical master equation | quantum physical cohomology |
| invariant tensor metric on `p_bal` | unique up to scale, signature `24|25` | positive kinetic metric |
| scalar principal operator | ultrahyperbolic/nonelliptic local symbol | canonical self-adjoint semibounded Hamiltonian |

The source-aligned real form is `(7,7)` and the balanced orbit type is
`(3,4)|(4,3)`. The physical source split `(1,3)|(6,4)` is a distinct
`51D` stabilizer and does not replace this calculation.

## Packet A: uniqueness of the invariant form

Let `V=R^(3,4)` and `W=R^(4,3)`. The isotropy representation is the outer
tensor product of the standard representations. To avoid a large opaque
`2401`-unknown solve, the exact certificate uses the block theorem directly.

If `X in End(V tensor W)` commutes with `so(V) tensor 1`, then every matrix
block indexed by an input/output pair in `W` commutes with `so(V)`. The
standard-factor commutant is scalar, so

```text
X = 1_V tensor A.
```

Commuting also with `1 tensor so(W)` forces `A` into the scalar commutant of
the second factor. Thus `X` is scalar. The modular factor ranks are each
`48`; the visible identity kernel makes the conclusion exact over `Q`.

The tensor metric `q_V tensor q_W` is one nondegenerate invariant symmetric
form. Any other invariant form differs from it by an invariant endomorphism,
hence by one scalar. Its inertia is therefore fixed up to overall sign.

## Packet B: Hamiltonian and PDE consequences

Choose a tensor basis diagonalizing both factor metrics. Tensor signs are
products. There are `24` positive and `25` negative basis directions.

For the invariant quadratic fibre Hamiltonian, one unit positive covector has
energy `+1` and one unit negative covector has energy `-1` up to normalization.
Scaling either by `17` gives `+289` and `-289`. No additive constant or
overall nonzero scaling makes the form semibounded.

For the scalar second-order operator, the same inverse form is the principal
symbol. Adding one positive and one negative unit covector gives a nonzero
null covector. Hence the symbol vanishes away from the zero section and is
not elliptic. Local plane waves along the two rays give both signs with
unbounded magnitude. This blocks the canonical invariant positive elliptic
and semibounded route before lower-order terms.

Lower-order potentials cannot repair principal ellipticity. A potential can
also not bound an unconstrained negative quadratic momentum ray at fixed base
point. Repair requires changing the kinetic carrier, imposing constraints or
a domain, choosing a different real/complex contour, or abandoning full
invariance—not merely tuning a lower-order coefficient.

## Packet C: what classical BFV does and does not provide

K98 proves the `42` moment constraints are regular and irreducible and that
the minimal classical BFV charge closes. Those statements depend on the
symplectic moment-map algebra and Jacobi identity, not a positive kinetic
metric. K106 therefore preserves them.

What remains missing is a physical analytic package:

1. a positive sector, Krein-to-positive constraint, contour/Wick rotation, or
   boundary domain;
2. compatibility of that choice with the moving balanced field and its full
   Euler/Noether variation;
3. a closed or self-adjoint quantum operator on the chosen domain;
4. a proof that BRST/BFV cohomology inherits a positive physical pairing; and
5. only then a particle, spectral or phenomenological interpretation.

None is selected by the bare conditional quotient. Any such choice is a new
owner/domain datum until derived from the action.

## What closes and what remains

Closed:

- classification of invariant symmetric forms on the balanced isotropy
  module: one-dimensional, signature `24|25` up to sign;
- canonical invariant positive-definite kinetic form: absent;
- invariant quadratic Hamiltonian semiboundedness: absent;
- canonical invariant scalar ellipticity: absent; and
- inference from classical BFV closure to positive quantum cohomology:
  invalid.

Retained:

- the conditional `98D` classical symplectic realization;
- the conditional regular irreducible finite classical BFV system;
- non-invariant positive-sector constructions;
- Krein or constrained quantization with a proved positive physical quotient;
- action-owned contour/Wick rotations; and
- boundary-defined domains compatible with the moving-`R` Noether law.

No ledger, datum, quotient booking, canon, public posture, particle,
phenomenology or GU truth-status claim moves.

## Broad council and hostile bookends

Opening perspectives:

- representation theory selected invariant-form classification;
- pseudo-Riemannian symmetric-space geometry supplied the tensor signature;
- Hamiltonian mechanics tested energy semiboundedness;
- microlocal/PDE analysis tested the principal symbol before domains;
- BFV/symplectic geometry protected classical closure from an analytic
  overreach;
- functional analysis identified the missing semibounded/self-adjoint burden;
- source/owner criticism kept the complete construction conditional; and
- heterodox/Krein and contour routes were retained as real alternatives.

Exact structure dominates spectral numerics: no finite truncation is needed
to decide the invariant metric or principal-symbol sign.

Closing hostile charges:

1. **Overall-sign repair:** only swaps `24` and `25`; indefiniteness remains.
2. **Throw away negative directions:** changes the `49D` isotropy carrier and
   breaks the claimed invariant quotient unless a new constraint owns it.
3. **Add a potential:** cannot change the nonelliptic principal symbol or the
   fixed-base negative momentum rays.
4. **BFV nilpotence means positivity:** false; it is an algebraic master-
   equation statement.
5. **Universal quantization no-go:** rejected. Non-invariant, Krein,
   constrained, contour, Wick and boundary-domain routes remain open under
   their own exact burdens.

Reproduce with
`python3 tests/channel-swings/selected_k106_rsap_balanced_quotient_positivity_ellipticity_probe.py`.

> **Successor closure (K107).** Cotangent doubling does produce invariant
> compatible complex structures and preserves the canonical invariant
> vertical real polarization, so absence of complex or polarized geometry is
> not the obstruction. At the zero section every compatible invariant metric
> has signature `48|50` or `50|48`, and invariant Krein or linear-subquotient
> repairs retain the `24|25` factor. Reopen only with a concrete action-owned
> non-invariant selector or analytic domain, not another invariant linear
> construction.
