---
artifact_type: exploration
status: exploration
doc_type: conditional_build_exact_four_dimensional_clifford_split_certificate
created: 2026-08-16
work_item: CB-5A
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-5A: the observed H210 port has a co-moving four-dimensional Clifford split, but its trace is observation-induced and is not source-F provenance"
grade: "EXACT two-field finite certificate over GF(1009) and GF(1013), conditional on H210. H210-ALIGN, H210-FCORR, and H210-PSRED remain separate declared horns. The result concerns the decorated post-contraction maps F_J^tr and Q_J^RS. It does not identify F_J^tr with Weinstein's equation-(12.22) F/imposter, derive any action or reduction, or construct a physical quotient."
disposition: CONDITIONAL_H210_FQ_SPLIT_EXACT_AND_COMOVING__UPSTREAM_AMBIENT_F_TRACE_ZERO__POSTCONTRACTION_4D_TRACE_OBSERVATION_INDUCED__SOURCE_F_PROVENANCE_NOT_ESTABLISHED
canon_verdict_change: none
probe: tests/channel-swings/joe_directed_cb5_h210_four_dimensional_clifford_split_probe.py
depends_on:
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb3-h210-source-observation-functor-crosswalk-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb4-wave-h210-naturality-reprioritization-2026-08-16.md
  - lab/process/hostile-reviews/2026-08-16-joe-directed-cb4-h210-naturality-review.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb5-h210-source-fq-bridge-2026-08-16.md
  - explorations/conditional-build/selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact borders
> Weinstein's source-native `2+1`, imposter, emergent-chirality, and
> Pati--Salam recombination proposal. Ordinary family indices, net-chirality
> arguments, scalar-Higgs/VEV models, conventional `SO(10)` mass mechanisms,
> and familiar low-energy particle models are controls only. They do not
> adjudicate this mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.
>
> Horn `H210` is assumed. `H210-ALIGN`, `H210-FCORR`, and `H210-PSRED` are
> independent, separate conditional horns. Deriving or varying an action, choosing an
> observer graph, background, vacuum, section, selector or family row,
> constructing a reduction, or importing an external datum is outside scope.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-5A — exact four-dimensional Clifford split of the observed H210 port

## Result first

The conditional H210 port has a nontrivial, exact four-dimensional Clifford
split after literal observation contraction. For

```text
A_J       = O_J T,
F_J^tr    = (1/4) j_4 Gamma_4 A_J,
Q_J^RS    = Pi_4 A_J,
Pi_4      = I-(1/4)j_4 Gamma_4,
```

the two-field certificate proves

```text
A_J = F_J^tr + Q_J^RS,
Gamma_4 Q_J^RS = 0,
Pi_4^2 = Pi_4,
ker(A_J) = ker(F_J^tr) intersection ker(Q_J^RS).
```

Both projected maps commute in separate finite co-moving squares when the
horizontal covector frame, output spin frame, horizontal Clifford
injection/trace, and full right-domain spin transport all move together. The
result holds on both conjugate ambient halves over `GF(1009)` and `GF(1013)`.

The most important interpretation is adverse to the naive source promotion:

`F_J^tr` is an F-shaped carrier component only; that phrase records a target
shape and does not assign source provenance.

```text
Gamma_14 T = 0,              Pi_14 T = T,
```

so the upstream H210 tensor belongs to the ambient gamma-traceless Z-shaped
sector and its canonical ambient trace/F projection is zero. A nonzero
`F_J^tr` appears only after the normal covector leg is contracted into the
four-dimensional observer graph. It is therefore an **observation-induced
Z-to-F-shaped adapter**, not a discovery that the upstream H210 port was the
source F summand.

Equation (12.22)'s source F is a correlated horizontal/normal trace pair
inside ambient `ker Gamma_14`. The decorated `F_J^tr` computed here is only
its horizontal four-dimensional Clifford-trace-shaped component. This result
does not identify that component with Weinstein's source-labelled F/imposter
provenance. The pointwise split-canonical carrier lift is

```text
kappa_J(tau_J)=((1/4)j_4 tau_J,-(1/10)j_10~ tau_J),
tau_J=Gamma_4 O_JT,
```

relative to the declared orthogonal split. Its complete co-moving
horizontal/normal naturality is not certified here. Identifying this
observation-induced adapter with Weinstein's intended equation-(12.22) F
reveal requires the separately declared `H210-FCORR` horn.
Identifying the selected multiplicity quotient with imposter provenance still
requires the independent `H210-ALIGN` horn; neither supplies `H210-PSRED`.

## Conditional-build preflight

The execution used exact-Clifford, projector-algebra, graph-stratum,
finite-naturality, both-half/chirality, family-kernel, `Pi_4`-versus-`Pi_14`,
adverse-mutation, and claim-ceiling lenses.

The source and ledger archaeology fixed the route before calculation:

1. equation (12.22) attaches the imposter label to F, not to the internal
   `144` or the Z-shaped H210 port;
2. associated-bundle F/Q/Z branching and differential-form pullback are
   distinct functors;
3. CB-3 shows that literal pullback consumes the normal covector leg;
4. CB-4 proves finite co-moving rank descent but leaves `H210-ALIGN` and
   `H210-PSRED` separate; CB-5C further separates `H210-FCORR`; and
5. twistor prior art owns the four-dimensional projector and positive
   adapter, while explicitly proving that `Pi_4` is not `Pi_14`.

No missing action, background, graph, selector, reduction, or external datum
was turned into a task.

## Exact Clifford and projector algebra

The certificate uses the current real-K77 Clifford packet, reordered as

```text
H_4 signature = (1,3),
V_10 signature = (6,4).
```

For covariant four-dimensional vector-spinors it constructs

```text
j_4(psi)_mu = gamma_mu psi,
Gamma_4(A)  = sum_mu eta_mu gamma_mu A_mu,
Gamma_4 j_4 = 4 I.
```

Thus the complementary projectors are

```text
P_4^tr = (1/4)j_4 Gamma_4,
Pi_4   = I-P_4^tr.
```

The split and gamma-trace identities are operator identities, not numerical
rank guesses. Since `P_4^tr+Pi_4=I`, the map into the direct sum of the two
images has exactly the same kernel as `A_J`. Consequently

```text
ker(A_J)=ker(F_J^tr) intersection ker(Q_J^RS).
```

This is the correct shared-domain relation. The ranks of `F_J^tr` and
`Q_J^RS` must never be added as counts of independent families or sectors.

## `Pi_4` is not `Pi_14`

The ambient projector is constructed separately:

```text
Pi_14 = I-(1/14)j_14 Gamma_14.
```

It is exactly idempotent and lands in `ker Gamma_14`. Its base block on a
base-supported vector-spinor is

```text
Pi_14,base = I-(1/14)j_4 Gamma_4,
```

which is neither `Pi_4` nor an idempotent projector on the base-supported
subspace. The certificate preserves the positive adapter

```text
Pi_14,base Pi_4 = Pi_4 Pi_14,base = Pi_4.
```

This says that a four-dimensionally gamma-traceless vector-spinor embeds in
ambient `ker Gamma_14`. It does not equate the projectors, the source-to-
carrier maps, or the local-twistor detour operator with the GU rolled operator.

For the actual upstream H210 tensor, exact ambient gamma-tracelessness gives

```text
Pi_14 T=T.
```

Substituting `Pi_14,base` for `Pi_4` after contraction leaves residual
four-dimensional trace and is caught by the adverse plant.

## Exact rank and kernel ledger

The certificate replays flat, rank-one null, totally isotropic two-plane,
rank-one non-null, paired-null with nonzero pairing, and the banked receiver
strata. Every displayed rank is the rank on one real ambient Weyl half; the
conjugate half has the identical fingerprint. Divide by four only for the
previously banked internal-complex rank convention.

| graph stratum | `rank A` | `rank F^tr` | `rank Q^RS` | `dim ker A` | `dim ker F` | `dim ker Q` | `dim(ker F intersect ker Q)` |
|---|---:|---:|---:|---:|---:|---:|---:|
| flat | `0` | `0` | `0` | `64` | `64` | `64` | `64` |
| rank-one null | `32` | `32` | `32` | `32` | `32` | `32` | `32` |
| isotropic two-plane | `48` | `32` | `48` | `16` | `32` | `16` | `16` |
| rank-one non-null | `64` | `64` | `64` | `0` | `0` | `0` | `0` |
| paired null, nonzero pairing | `64` | `64` | `64` | `0` | `0` | `0` | `0` |
| banked receiver | `64` | `64` | `64` | `0` | `0` | `0` | `0` |

For a declared nonzero `r in M_3*`, each family-input kernel is computed as

```text
0 -> ker(r) tensor W -> ker(r tensor B) -> ker(B) -> 0,

dim_C ker(r tensor B)
  = 32 + dim_C ker(B),          B in {A,F^tr,Q^RS}.
```

In the internal-complex convention this gives:

| graph stratum | family kernel of `A` | family kernel of `F^tr` | family kernel of `Q^RS` | projected-kernel intersection |
|---|---:|---:|---:|---:|
| flat | `48` | `48` | `48` | `48` |
| rank-one null | `40` | `40` | `40` | `40` |
| isotropic two-plane | `36` | `40` | `36` | `36` |
| rank-one non-null | `32` | `32` | `32` | `32` |
| paired null, nonzero pairing | `32` | `32` | `32` | `32` |
| banked receiver | `32` | `32` | `32` | `32` |

The intersection of the two projected family kernels is the `A` family
kernel. No family is named, no row is fitted, and no projected rank is an
additional generation count.

## Separate finite co-moving squares

For the CB-4 finite graph transition, write

```text
g=((a,b),(c,d)),
A_h=a+bJ,
J'=(c+dJ)A_h^-1.
```

The observed map transports by

```text
C_J = A_h^-T tensor S(g),
A_J' = C_J A_J S(g)^-1.
```

The right factor is the complete domain-spinor transport and is retained in
every map-level check. The horizontal Clifford maps move as

```text
j_4'     = C_J j_4 S(g)^-1,
Gamma_4' = S(g) Gamma_4 C_J^-1,
Pi_4'    = C_J Pi_4 C_J^-1.
```

Therefore the certificate separately verifies

```text
F_J'^tr = C_J F_J^tr S(g)^-1,
Q_J'^RS = C_J Q_J^RS S(g)^-1
```

across three mixed Cayley transitions and all replayed strata in both exact
fields. Freezing the horizontal gamma frame breaks these squares and fires a
plant. The surviving invariant data are the associated-bundle morphisms and
their pointwise ranks/kernels on admitted overlaps, not a preferred component
matrix, observer graph, O/Spin lift, or global topology theorem.

## Adverse mutations

The self-test rejects all six required mutations:

1. promote `F_J^tr` to source F/imposter provenance without `H210-FCORR`;
2. substitute `Pi_14` or its base block for `Pi_4`;
3. freeze the horizontal gamma frame during finite transport;
4. delete the conjugate ambient half;
5. promote `H210-ALIGN` from a separate conditional horn; and
6. add projected ranks as family counts.

The algebraic mutations fail over both `GF(1009)` and `GF(1013)`. The semantic
mutations fail against the explicit source-provenance and conditional-horn
fences in this artifact.

## Claim ceiling

This artifact proves a formal, exact, conditional carrier decomposition and
finite associated-bundle naturality result. It strengthens the statement that
the H210 port can generate both four-dimensional trace-shaped and
gamma-traceless observed components on nonzero graph strata.

It does **not** prove full co-moving naturality of the complete correlated
horizontal/normal lift, or that the source or action selects H210, an observer
graph, `H210-ALIGN`, `H210-FCORR`, `H210-PSRED`, a Pati--Salam reduction, or a physical
quotient. It does not prove that `F_J^tr` is Weinstein's F/imposter, restore a
free observed `144`, select a luminous half, name a family, or derive a mass,
scale, threshold, domain, positive state, observable, or phenomenology. The
fixed trace-`H_q` adverse horn and the full `d0+varpi` collision remain open.

## Reproduction

```bash
sage -python tests/channel-swings/joe_directed_cb5_h210_four_dimensional_clifford_split_probe.py
sage -python tests/channel-swings/joe_directed_cb5_h210_four_dimensional_clifford_split_probe.py --selftest
```

The first command runs the exact two-field certificate. The second additionally
fires the six hostile plants.
