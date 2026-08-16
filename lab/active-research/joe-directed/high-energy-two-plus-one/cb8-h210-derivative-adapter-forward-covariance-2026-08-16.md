---
artifact_type: exploration
status: exploration
doc_type: conditional_build_exact_forward_covariance_and_stage_classifier
created: 2026-08-16
work_item: CB-8A
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-8A: a supplied horizontal Clifford section gives a natural forward derivative adapter, but only a source-Y horn repairs equation 9.16 upstream"
grade: "L1 bundle-algebra theorem plus exact QQ and two-field Cl(7,7) certificate, conditional on H210 and on a supplied coherently transforming q_H section/cocycle. The theorem does not construct, select, or source-own q_H, an observer graph, an atlas, an action, a family row, or a physical quotient."
disposition: FORWARD_COVARIANCE_PASSES_CONDITIONALLY__SOURCE_Y_ONLY_UPSTREAM__PULLBACK_X_AND_GRAPH_HJ_OBSERVED_ONLY__NONNULL_FULL_RANK__NONZERO_NULL_HALF_RANK__ZERO_KILLS__GLOBAL_EXISTENCE_UNPROVED
canon_verdict_change: none
steering_effect: "Carry the forward square as conditionally solved once the base, horizontal covector bundle, Spin transition, Clifford-compatible connection, and q_H cocycle are supplied. Do not promote an X or H_J section into the source-Y equation. CB-8B subsequently proves that generic normal first jets contaminate isolated reverse-H210 custody; retain L_q|_Z=0 only as an externally triggered reopen condition and do not continue this branch by searching for its owner."
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb4-h210-finite-comoving-naturality-square-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb6-h210-full-correlated-lift-naturality-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb7-h210-minimal-odd-adapter-classifier-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb7-wave-h210-half-duality-reprioritization-2026-08-16.md
  - lab/process/hostile-reviews/2026-08-16-joe-directed-cb7-h210-half-duality-review.md
scripts:
  - tests/channel-swings/joe_directed_cb8_h210_derivative_adapter_forward_covariance_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — source-native conditional build.** This artifact
> concerns Weinstein's equation-(9.16) candidate grammar, section-11.2
> ambient-half labels, equation-(11.6) Z/internal-`144` partner sector,
> equation-(12.22) F/imposter referent, `2+1`, Pati--Salam recombination, and
> emergent chirality. Ordinary family indices, net-chirality arguments,
> scalar-Higgs/VEV models, conventional `SO(10)` mass mechanisms, and familiar
> low-energy particle models are irrelevant comparators without an explicit
> typed bridge. Read `lab/methods/source-native-comparator-routing.md`.
>
> Horn `H210` is assumed. The additional `H210-D0-QH` horn supplies a smooth,
> coherently transforming horizontal covector section and its cocycle. It is
> not constructed, selected, or attributed to the source. Constructing an
> action, selector, observer graph/background, family row, moving reduction,
> quotient, external datum, mass, scale, threshold, spectrum, or observable is
> outside this channel. Bars remain independent fields; stars are not promoted
> to adjoints or reality maps.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-8A — derivative-side horizontal adapter and forward covariance

## Verdict

The forward differential objection from CB-7 is discharged **conditionally**.
Once a base and compatible overlap data are declared, the operator

```text
D_q = gamma(q_H) o d0
```

is a natural first-order associated-bundle operator. Its overlap square moves
the spinor, derivative one-form, horizontal covector, Clifford frame, and
connection together. The inhomogeneous connection term is essential. This is
stronger than CB-7's pointwise parity certificate and is not another replay of
CB-4 or CB-6's H210 tensor naturality.

The stage classifier is equally decisive: only a `q_H` supplied on the source
base `Y`, in a source-horizontal covector subbundle on which equation (9.16)
is defined, can repair the upstream displayed cell. A covector supplied only
on `X` after pullback, or only in the graph plane `H_J`, defines an observed
adapter. It cannot be inserted into the source operator without a new typed
extension/bridge.

Thus forward covariance is no longer the primary gate. Global existence and
ownership of the horn remain deliberately unasked. The next mathematical gate
is the reverse operator, where reversing order forces a `nabla q_H` term.

## Reverse-conditional input

This result begins by assuming, never deriving:

```text
H210-D0-QH:
  a base B;
  a horizontal covector bundle H* -> B;
  a Spin bundle S=S+ direct-sum S- -> B;
  a Clifford map gamma:H* tensor S+- -> S-+;
  a compatible connection nabla;
  a smooth section q_H of H* with its declared overlap cocycle;
  either a coherent untwisted section/trivialization or the corresponding
  explicit line-valued target;
  g(q_H,q_H) != 0 wherever full rank is claimed.
```

For the equation-(9.16) full-cell candidate, inherited opposite-half density
duality is also retained and H210 is left untouched. Nothing here selects the
horn, a source action, the observer, a family, or a luminous half.

## Exact forward theorem

Let an overlap carry:

```text
S         = local Spin transition,
E         = exterior one-form transition,
C_H       = horizontal q-covector transition,
psi'      = S psi,
q_H'      = C_H q_H,
gamma'(C_H q_H) S = S gamma(q_H).
```

For a Clifford-compatible connection, including its affine term, the local
connection matrices obey the component version of

```text
nabla' psi' = (E tensor S) nabla psi.
```

Before the coframe component is applied, the familiar spin-frame law is

```text
omega' = S omega S^-1 - (dS)S^-1,
```

so that the `dS` generated by differentiating `psi'=S psi` cancels exactly.
Consequently,

```text
D_q' psi'
 = (id tensor gamma'(q_H')) nabla' psi'
 = (E tensor S)(id tensor gamma(q_H)) nabla psi
 = (E tensor S) D_q psi.
```

This is the required forward associated-bundle square. The probe verifies it
over `QQ` with a genuinely moving nonconstant spin transition and explicitly
checks the inhomogeneous connection law. Freezing the connection, using the
wrong affine sign, freezing `q_H`, freezing the Clifford frame, freezing the
spinor jet, or omitting the exterior coframe factor makes the square fail. The
exact fixture deliberately takes `E != C_H`, preventing accidental collapse
of the derivative one-form leg with the horizontal Clifford-covector leg.

The theorem assumes transition data satisfying the displayed cocycle laws. It
does not construct a global atlas, prove the existence of a horizontal
subbundle on `Y`, or show that the draft's displayed `rho(epsilon)` factors are
the active K77 cocycle.

## Symbol, order, and Leibniz rule

For a cotangent frequency `xi`,

```text
sigma_1(D_q)(xi) = xi tensor gamma(q_H).
```

Because Clifford multiplication is postcomposed with the derivative,

```text
D_q(f psi) = f D_q psi + df tensor gamma(q_H) psi.
```

There is no forward `nabla q_H` term. This does **not** say `q_H` is constant;
it says this operator does not differentiate its left coefficient. The
different grammar `d0 o gamma(q_H)` would add
`gamma(nabla q_H) psi` (with the precise contraction fixed by the connection),
and the reverse formal transpose has that order. CB-8A does not type or remove
that reverse term.

The symbol statement is source-faithful only as a declared modification of
the candidate grammar. The draft says fields may “begin with operators like”
equation (9.16); it does not print `gamma(q_H)d0`, select `q_H`, or prove a
unique fermionic operator.

## Base and stage classifier

| horn | supplied object | forward operator that types | repairs upstream equation (9.16)? | unresolved dependency |
|---|---|---|---|---|
| `QH-Y` | `q_Y in Gamma(H_Y*)` over source `Y`, with source Spin/coframe cocycle | `gamma_Y(q_Y)d0_Y` | **yes, conditionally** | source-wide horizontal subbundle, compatible connection, cocycle, and non-null section are all assumed |
| `QH-X` | `q_X` over observation base `X`, after a typed pullback/soldering into the Clifford bundle | `gamma_X(q_X)s* d0_Y` | **no**; observed operator only | pullback/soldering and connection compatibility |
| `QH-HJ` | `q_J in Gamma(H_J*)` on an admitted graph chart | `gamma_J(q_J) O_J d0_Y` | **no**; graph-observed operator only | graph atlas, induced Gram, Spin lift/cocycle, and chart compatibility |

`QH-Y` is the only horn at the right stage for the printed source operator,
but it is also the strongest additional assumption. `QH-X` and `QH-HJ` are
closer to the observation geometry already banked in CB-4/CB-6; their merit
does not erase the stage mismatch. An `X` section can be the pullback of a `Y`
section if a bridge is supplied, but pullback data alone do not define or
extend a source section.

The graph-plane horn is intrinsically chartable on admitted nondegenerate
graph overlaps. Its local vector can move by the graph coframe cocycle and its
Clifford action can use the induced graph metric. That gives the same formal
theorem downstream. It does not make `H_J` a horizontal distribution over all
of `Y`.

## Zero, null, and non-null strata

Clifford algebra gives

```text
gamma(q_H)^2 = g(q_H,q_H) I.
```

Therefore:

| stratum | ambient-half map `S+ -> S-` | consequence for `sigma_1(D_q)(xi)` when `xi != 0` |
|---|---|---|
| `g(q,q) != 0` | invertible, rank `64` in the current real K77 fixture | full spin-half rank |
| `q != 0`, `g(q,q)=0` | nilpotent, rank `32` on each ambient half | half-rank adverse stratum |
| `q=0` | rank `0` | symbol killed |
| any `q`, `xi=0` | not applicable | first-order symbol killed |

The exact probe checks these ranks on both conjugate ambient halves over
`GF(1009)` and `GF(1013)`. “Nowhere nonzero” is insufficient in Lorentzian
signature; retained rank requires “nowhere null.” A null section can still be
smooth and nonvanishing while the adapter loses half its pointwise rank.

These are ranks of the horizontal Clifford factor (and of the scalar `d0`
principal symbol for nonzero `xi`). They do not establish the analytic rank,
kernel, domain, or spectrum of a global differential realization.

## Multiple-lens assessment

1. **Source fidelity.** Equation (9.16) remains a displayed candidate, not a
   uniquely selected operator. `gamma(q_H)d0` is a conditional modification.
2. **Stage/base.** `Y`, `X`, and `H_J` are different bases or subbundles. Only
   `QH-Y` reaches upstream.
3. **Associated bundles.** Covariance needs simultaneous transport of every
   bundle leg; component equality in a fixed frame is not the theorem.
4. **Clifford connection.** The affine `-(dS)S^-1` term is load bearing.
5. **First-order symbol.** The exact symbol is `xi tensor gamma(q_H)`.
6. **Leibniz/order.** Postcomposition has no forward `nabla q_H`; reversing
   order does.
7. **Null strata.** Non-null, null nonzero, and zero are three distinct ranks.
8. **Both halves.** Horizontal Clifford multiplication exchanges both ambient
   halves symmetrically; neither is removed or called physical.
9. **Adverse transitions.** Six exact frozen/wrong-law mutants fail.
10. **Prior-art novelty.** CB-4/CB-6 established moving H210/graph functors;
    CB-8A adds a genuine first-order connection square and stage theorem.
11. **Scope.** Formal naturality is conditional on the cocycle. It does not
    create its global owner or physical interpretation.

## Exact certificate

Run from the repository root:

```bash
sage -python tests/channel-swings/joe_directed_cb8_h210_derivative_adapter_forward_covariance_probe.py
```

All `66/66` checks pass. The certificate includes packet/source/routing
guards, eleven preflight lenses, a nonconstant exact spin transition over
`QQ`, the inhomogeneous connection law, moving spinor/form/q/Clifford factors,
six firing transition mutants, symbol and Leibniz identities, the
precomposition adverse control, exact zero/null/non-null K77 ranks over two
finite fields, both ambient halves, the three-stage classifier, and semantic
mutants against upstream promotion, adjoint/reality collapse, atlas inflation,
and downstream-kappa repair.

## What moved and what did not

The forward covariance cell marked `TYPE_MISSING` by CB-7 now passes at
conditional bundle-algebra grade for each stage where the assumed data type.
It is not blocked by a hidden forward `nabla q_H` term. The null-stratum fence
is exact, and only the source-Y version addresses the upstream source cell.

No source/action owner for `q_H` has been found or sought. No global source
horizontal subbundle, section, graph, atlas, Spin cocycle, line
trivialization, density dual, reverse operator, adjoint, reality condition,
boundary/domain, quotient, family alignment, mass, scale, spectrum,
observable, phenomenology, or physical chirality has been constructed.
The isolated H210 zero-order CB-2--CB-6 chain remains unchanged. F/imposter,
`M_3`, and Z/internal-`144` remain distinct, and both conjugate halves remain
present.
