---
artifact_type: exploration
status: exploration
doc_type: conditional_build_exact_full_correlated_lift_naturality_certificate
created: 2026-08-16
work_item: CB-6A
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-6A: the intrinsic graph-plane correlated H210 lift is co-moving, while the CB-5 fixed-frame trace is a distinct chartwise decoration"
grade: "EXACT two-field finite certificate over GF(1009) and GF(1013), conditional on H210. The theorem is intrinsic to the nondegenerate graph plane and its metric-orthogonal complement. H210-FCORR, H210-ALIGN, and H210-PSRED remain separate declared horns. No action, observer graph/background, selector, family row, reduction, physical quotient, external datum, mass, scale, threshold, or observable is constructed."
disposition: INTRINSIC_GRAPH_PLANE_KAPPA_NATURALITY_PASSES__CB5_FIXED_TRACE_IS_CHARTWISE_NOT_INTRINSIC_OFF_FLAT__UPSTREAM_H210_FCORR_PROJECTION_ZERO__DOWNSTREAM_ADAPTER_OBSERVATION_INDUCED__SOURCE_REVEAL_REMAINS_H210_FCORR
canon_verdict_change: none
probe: tests/channel-swings/joe_directed_cb6_h210_full_correlated_lift_naturality_probe.py
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb4-h210-finite-comoving-naturality-square-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb5-h210-four-dimensional-clifford-split-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb5-h210-source-fq-bridge-2026-08-16.md
  - lab/process/hostile-reviews/2026-08-16-joe-directed-cb5-h210-fq-split-review.md
  - explorations/conditional-build/selected-k77-local-twistor-bach-detour-composition-gate-2026-08-14.md
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This is a source-native
> conditional build for Weinstein's equation-(12.22) F/imposter,
> equation-(11.6) Q/Z, `2+1`, Pati--Salam recombination, and emergent-chirality
> claims. Ordinary family indices, net-chirality arguments, scalar-Higgs/VEV
> models, conventional `SO(10)` mass mechanisms, and familiar low-energy
> particle models are controls only. They do not adjudicate this mechanism
> without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.
>
> Horn `H210` is assumed. `H210-FCORR`, `H210-ALIGN`, and `H210-PSRED` are
> independent conditional horns. Constructing or deriving an action, selector,
> observer graph/background, family row, moving PS reduction, physical
> quotient, external datum, mass, scale, threshold, observable, or
> phenomenology is outside scope.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-6A — full intrinsic horizontal/normal correlated-lift naturality

## Result first

On every admitted nondegenerate graph chart, and given compatible orthogonal
overlap and Spin-lift data, the complete correlated lift is an exact natural
associated-carrier morphism. Let

```text
L_J = [I;J],                         H_J = im(L_J),
K_J = [-eta_H^-1 J^T eta_V; I],     N_J = im(K_J)=H_J^perp,
G_H,J = L_J^T eta L_J,              G_N,J = K_J^T eta K_J.
```

Use the graph-frame Clifford maps and the inverse induced Grams to define

```text
Gamma_H,J : H_J^* tensor S -> S,
j_H,J     : S -> H_J^* tensor S,
Gamma_N,J~: N_J^* tensor S -> S,
j_N,J~    : S -> N_J^* tensor S.
```

The normal map is the graded normal Clifford action inside the ambient
`Cl(7,7)` representation. Exact Clifford algebra gives

```text
Gamma_H,J j_H,J = 4 I,
Gamma_N,J~ j_N,J~ = 10 I.
```

For the intrinsic observed trace

```text
tau_J = Gamma_H,J O_J T_H210,
```

the full lift

```text
kappa_J(tau_J)
  = ((1/4)j_H,J tau_J, -(1/10)j_N,J~ tau_J)
```

has zero ambient Clifford trace. Its normal component is constructed in the
normal trace image; it is not the consumed H210/internal-`144` leg.

The complete finite square commutes over both exact fields, three mixed
transitions, flat/isotropic/banked graph strata, and both ambient chirality
halves. This closes CB-5's moving-normal functorial debt at intrinsic
graph-plane carrier grade. It does not establish that this adapter is
Weinstein's intended reveal; that interpretation remains `H210-FCORR`.

## Exact graph and normal cocycles

Write an ambient K77 transition in blocks as

```text
g = ((a,b),(c,d)),
A = a+bJ,
J' = (c+dJ)A^-1.
```

The horizontal frame obeys `gL_J=L_J'A`. Orthogonality determines the normal
frame and its separate cocycle:

```text
D = d-c eta_H^-1 J^T eta_V,
gK_J=K_J'D.
```

Consequently

```text
G_H,J' = A^-T G_H,J A^-1,
G_N,J' = D^-T G_N,J D^-1.
```

The two coframes therefore move by `A^-T` and `D^-T`; using one for the other
is ill typed. For a Spin lift `S(g)` and the complete right-domain transport,
the exact square is

```text
kappa_J'(S(g) tau_J S(g)^-1)
 = ((A^-T tensor S(g)) direct-sum (D^-T tensor S(g)))
     kappa_J(tau_J) S(g)^-1.
```

This theorem is formally forced once the nondegenerate graph split and its
Spin overlap are admitted, but it is not an empty component identity. The
normal complement, `D` cocycle, both induced Grams, graded normal sign, and
right-domain factor are independently load bearing; the exact mutations in
the probe break when any is frozen or removed.

## Successor correction to CB-5

CB-5 used a fixed `(eta_H,gamma_H)` at each source `J` and then transported
that four-dimensional Clifford datum across overlaps. Denote its trace by

```text
Gamma_4^chart O_JT.
```

The intrinsic graph-plane trace certified here is instead

```text
Gamma_H,J^intr O_JT,
```

where the Clifford generators are `c(L_Je_mu)` and contraction uses
`G_H,J^-1`. The exact comparison shows that the two traces agree at the flat
chart and differ on both the admitted isotropic and banked nonflat charts in
both fields. Therefore CB-5's projector algebra and its own transported
naturality square remain exact for the declared chartwise Clifford
decoration, but that decoration must not be called the canonical Clifford
trace of the graph plane. Intrinsic graph-plane F/Q ranks and the correlated
lift must use the induced-Gram construction of CB-6A.

This is a successor qualification, not a deletion of CB-5: the identity
`Gamma j=4I`, complementary split, kernel intersection, and finite covariance
remain correct for the datum CB-5 actually defined. What changes is the
geometric ownership claim on nonflat graph strata.

The exact rank comparison on either ambient half is:

| graph stratum | CB-5 chartwise trace rank | intrinsic `tau_J` / correlated-pair rank | intrinsic kernel | internal-complex rank | family-input kernel for nonzero `r in M_3*` |
|---|---:|---:|---:|---:|---:|
| flat | `0` | `0` | `64` | `0` | `48` |
| isotropic two-plane | `32` | `48` | `16` | `12` | `36` |
| banked receiver | `64` | `64` | `0` | `16` | `32` |

The banked chart has equal ranks but unequal trace maps. Rank equality does
not repair the ownership distinction. The family-input column uses the
already declared, unfitted nonzero row and the basis-free exact sequence

```text
0 -> ker(r) tensor S -> ker(r tensor kappa_J tau_J)
  -> ker(kappa_J tau_J) -> 0.
```

It does not name or select a family.

## Source functor order and chirality

The source sequence remains

```text
ambient RS -- F/Q/Z branching --> Z-shaped H210 input
           -- literal graph contraction --> O_JT
           -- intrinsic graph Clifford trace --> tau_J
           -- kappa_J --> correlated F-shaped carrier.
```

At the upstream orthogonal split, the H210 tensor is pure normal and
normal-gamma-traceless, so

```text
P_Fcorr(T_H210)=0.
```

On the nonflat admitted strata, `tau_J` and `kappa_J(tau_J)` are nonzero.
Thus the downstream map is observation induced; it is not a source-F
component that survived pullback and it does not recover a free observed
`144`.

Both ambient Weyl halves are retained. The H210 map and each correlated
one-form component have the matching opposite-half allocation, while the even
Spin transitions preserve the two source halves. Ambient chirality, 4D Weyl
chirality, internal duality, and effective luminous/dark labels remain
different types. No ordinary net-chirality index is relevant here.

## What is natural on admitted overlaps

| object | exact status |
|---|---|
| nondegenerate graph plane `H_J` and orthogonal complement `N_J` | intrinsic subspaces, and conditional subbundles given an admitted graph atlas |
| full `kappa_J Gamma_H,J O_JT` | natural associated `F_corr`-carrier-valued morphism on admitted O/Spin overlaps |
| pointwise rank and kernel dimension on each half | overlap invariant; may vary by graph stratum |
| `L_J`, `K_J`, `A`, `D`, and component matrices | local-frame representatives |
| local Spin lift | stabilizer and double-cover-sign dependent |
| CB-5 fixed-frame trace | a distinct chartwise Clifford decoration off the flat chart |
| source-reveal provenance | conditional on `H210-FCORR` |
| family provenance | conditional on independent `H210-ALIGN` |
| moving Pati--Salam descent | conditional on independent `H210-PSRED` |

The complement is canonical from a nondegenerate graph plane and `eta`; a
preferred complement **frame** or global O/Spin representative is not. The
theorem does not construct an observer atlas, graph section, global Spin lift,
or triple-overlap sign cocycle. It proves the transition formula on every
admitted overlap and assumes no section is physically selected. The finite
transition sample is exact regression evidence for that universal formula,
not an existence proof for the required global atlas.

## Exact certificate and falsifiers

Run:

```bash
sage -python tests/channel-swings/joe_directed_cb6_h210_full_correlated_lift_naturality_probe.py
sage -python tests/channel-swings/joe_directed_cb6_h210_full_correlated_lift_naturality_probe.py --selftest
```

The certificate checks, over `GF(1009)` and `GF(1013)`, the K77 Clifford
relations, graph/normal orthogonality and nondegeneracy, `gL=L'A`, `gK=K'D`,
both Gram cocycles, horizontal and graded-normal `Gamma-j` identities,
correlated ambient cancellation, the complete right-domain square, ranks and
kernels on both halves, upstream-zero/downstream-nonzero functor order, and
the CB-5/intrinsic comparison.

The hostile mutations freeze `K` or omit `D`, hold the Gram matrices fixed,
reverse the normal cancellation sign, omit the right-domain Spin factor,
delete the conjugate half, promote upstream H210 to source F, claim the
constructed normal trace partner was recovered, or collapse the three horn
roles. Every mutation must fire.

The route is killed at intrinsic carrier grade if an admitted overlap breaks
the graph/normal cocycle or full kappa square. A local nonzero chartwise trace
alone would then survive, but `H210-FCORR` would lose its natural carrier
candidate. Success, as obtained here, earns only associated-carrier typing.

## Strict claim ceiling

CB-6A proves the full intrinsic graph-plane horizontal/normal correlated lift
is a finite co-moving natural morphism on admitted nondegenerate O/Spin
overlaps. It does not construct the observer atlas or its global Spin cocycle,
and it proves neither that Weinstein's source or an action selects H210 nor
that the constructed adapter is his intended reveal. It does not select an
observer graph/background, a family row, a named family, a moving PS
reduction, a physical quotient, a luminous half, a free observed internal
`144`, a mass, scale, threshold, domain, positive state, observable, or
phenomenology. `H210-FCORR`, `H210-ALIGN`, and `H210-PSRED` remain separate
conditional horns. Canon and public posture do not move.
