---
artifact_type: exploration
status: exploration
doc_type: conditional_build_typed_stage_composition
created: 2026-08-16
work_item: CB-6B
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-6B: the equation-9.16 H210 zero-order arrows admit a downstream observed correlated-F composition, but kappa is not an upstream cell coefficient and the full d0+varpi cells remain untyped"
grade: "EXACT GF(1009)/GF(1013) two-half intrinsic stage-composition, parity, rank/kernel, source-cell, and semantic-mutation certificate. CONDITIONAL on H210. The intrinsic horizontal/normal interface is the CB-6A graph-plane correlated lift; CB-5 fixed-frame ranks are retained only as a qualified legacy decoration. H210-FCORR, H210-ALIGN, and H210-PSRED remain independent. No action, selector, graph/background, family-row fit, reduction, physical quotient, external datum, mass, scale, threshold, or observable is constructed."
disposition: ZERO_ORDER_EQ916_TO_OBSERVED_FCORR_STAGE_CHAIN_TYPED__KAPPA_STRICTLY_DOWNSTREAM__BANKED_WRONG_ORDER_WITNESS_MAXIMAL__FINAL_PARITY_REMAINS_OFFDIAGONAL__FULL_D0_VARPI_CELL_RANK_AND_SPECTRUM_FORBIDDEN
canon_verdict_change: none
steering_effect: "Reuse the staged zero-order chain only after the full correlated-lift interface is admitted. Never insert kappa into varpi, replace upstream Z by F, or quote a rank/kernel/spectrum for the unresolved full d0+varpi cell."
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/sources/source-claim-register.yaml
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb1-h210-k77-rs-intertwiner-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb2-h210-equation916-cross-half-composition-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb5-h210-four-dimensional-clifford-split-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb5-h210-source-fq-bridge-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb5-wave-h210-fq-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb6-h210-full-correlated-lift-naturality-2026-08-16.md
  - lab/process/hostile-reviews/2026-08-16-joe-directed-cb5-h210-fq-split-review.md
scripts:
  - tests/channel-swings/joe_directed_cb6_h210_equation916_observed_composition_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — source-native conditional build.** This artifact
> concerns Weinstein's equation-(12.22) F/imposter, equation-(11.6) Q/Z,
> `2+1`, Pati--Salam recombination, and emergent-chirality claims. Ordinary
> family indices, net-chirality arguments, scalar-Higgs/VEV models,
> conventional `SO(10)` mass mechanisms, anomaly selectors, and familiar
> low-energy particle models are irrelevant comparators without an explicit
> typed bridge. Read `lab/methods/source-native-comparator-routing.md`.
>
> Horn `H210` is assumed. Constructing or deriving an action, selector,
> observer graph/background, family row, moving PS reduction, physical
> quotient, external datum, mass, scale, threshold, or observable is outside
> this channel.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-6B — equation-9.16 zero-order arrow through observed correlated F

## Outcome first

There is a correct typed composition, but it is a sequence of stages. It is
not a new entry in Weinstein's equation-(9.16) matrix.

On source-effective package A the forward sequence is

```text
E_A = M_3 tensor 16_+                         [nu_+]
  -- R_A = r tensor T_+ --> Z_A / 144bar_-    [zeta_-]
  -- O_J --> H_J* tensor S_-
  -- Gamma_H,J^intr --> S_+
  -- kappa_J --> F_corr,- .
```

`R_A` is the zero-order `varpi_-+` summand in displayed cell `(1,2)`. The
barred row there is `bar-zeta-plus`; under the explicitly inherited
opposite-half density-dual bridge it represents the unbarred output slot
`zeta-minus`. The conjugate package B is

```text
E_B = bar(M_3) tensor 16bar_-                 [nu_-]
  -- R_B = bar(r) tensor bar(T)_- --> Z_B / 144_+ [zeta_+]
  -- O_J --> H_J* tensor S_+
  -- Gamma_H,J^intr --> S_-
  -- kappa_J --> F_corr,+ ,
```

using the zero-order `varpi_+-` summand in cell `(0,3)`. The bars in the
source remain four independent fields. The density-dual arrow reading does
not impose a field reality condition or prove a common formal adjoint.

Writing

```text
A_J    = O_J R,
tau_J  = Gamma_H,J^intr A_J,
F_J^intr = (1/4) j_H,J tau_J,
K_J   = kappa_J tau_J,

kappa_J(tau)=((1/4)j_H,J tau,-(1/10)j_N,J~ tau),
```

the final map is `K_J`, not `R`. In particular, `kappa_J` is defined only
after literal observation and horizontal Clifford trace. It must not be
inserted into `varpi`, used to retype the upstream cell codomain as F, or
identified with the upstream F projection.

At the banked receiver the distinction is maximal on each internal complex
half:

```text
rank(K_J)=16,              rank(P_Fcorr R)=0.
```

The first map is the intrinsic CB-6A observation-induced `Z -> F_corr`
associated-carrier adapter. The second is
the direct-sum F projection of the upstream H210 Z port. They do not commute
or become equal. Calling `K_J` Weinstein's intended reveal still requires
`H210-FCORR`; assigning its selected family quotient F provenance requires
the independent `H210-ALIGN`; moving PS descent requires `H210-PSRED`.

## 1. Source cell and corner typing

The source fixes the orders

```text
rows:    (bar-zeta-minus, bar-zeta-plus, bar-nu-minus, bar-nu-plus)
columns: (zeta-plus, zeta-minus, nu-plus, nu-minus).
```

The complete zero-order ledger relevant here is:

| role | cell | displayed entry | conditional unbarred arrow |
|---|---:|---|---|
| A forward | `(1,2)` | `d0 + varpi_-+` | `nu+ : 3x16 -> zeta- : 144bar` |
| B forward | `(0,3)` | `d0 + varpi_+-` | `nu- : 3x16bar -> zeta+ : 144` |
| A reverse-shaped partner | `(2,1)` | `-d0* - bar(varpi_+-)*` | `zeta- -> nu+` |
| B reverse-shaped partner | `(3,0)` | `-d0* - bar(varpi_-+)*` | `zeta+ -> nu-` |

Only the forward pair has the family domain used in this artifact. The
reverse-shaped cells are an optional declared four-cell completion. Source
stars and bars do not prove that completion is an adjoint on a common domain,
so its ranks are not silently added to the forward-family ledger.

The bare pp/mm cells `(0,2)` and `(1,3)` remain exact negative controls. They
would use `16 x 144bar` and `16bar x 144`, whose Pati--Salam invariant
multiplicities are zero. Their superficial cross-effective-package placement
does not make them H210 channels.

## 2. Functor order and parity

The upstream H210 tensor is normal gamma-traceless and belongs to Z. Literal
observation consumes its normal covector leg. Horizontal trace is then taken
in the observed four-dimensional vector-spinor. Only after those operations
does `kappa_J` synthesize the correlated normal trace-image partner.

The exact Clifford certificate also locks the parity class. `T` is odd in
ambient spin chirality, while `O_J` preserves spin parity. `Gamma_H,J^intr`
and each component of `kappa_J` are individually odd, so
`kappa_J Gamma_H,J^intr` is even on the observed vector-spinor. Therefore
`K_J` has the same odd parity as `T`:

```text
nu+ -> F_corr,-,              nu- -> F_corr,+.
```

The downstream decoration does not move either arrow into a pp/mm cell. It
also does not select an effective luminous half; both conjugate packages are
retained.

## 3. Exact intrinsic rank and family-kernel ledger

Every entry below is in the internal-complex convention on one half. The
conjugate half has the identical fingerprint. `R=r tensor T` always has rank
`16` and kernel dimension `32` before observation. `A_J` is the literal raw
contraction. `F_J^intr` and `K_J` use the induced graph Gram, graph-plane
Clifford frame, orthogonal normal frame, and distinct normal Gram from CB-6A.

| graph stratum | `rank A_J` | `rank F_J^intr` | `rank K_J` | `dim ker A_J` on `M_3 tensor 16` | `dim ker K_J` |
|---|---:|---:|---:|---:|---:|
| flat | `0` | `0` | `0` | `48` | `48` |
| rank-one null | `8` | `8` | `8` | `40` | `40` |
| isotropic two-plane | `12` | `12` | `12` | `36` | `36` |
| rank-one non-null | `16` | `16` | `16` | `32` | `32` |
| paired null, nonzero pairing | `16` | `12` | `12` | `32` | `36` |
| banked receiver | `16` | `16` | `16` | `32` | `32` |

`kappa_J` and `j_H` are injective, so

```text
rank(K_J)=rank(tau_J)=rank(F_J^intr),
ker(K_J)=ker(F_J^intr).
```

For any stage map `B:16 -> W`, the nonzero rank-one family row gives the
basis-free exact sequence

```text
0 -> ker(r) tensor 16
  -> ker(r tensor B)
  -> (M_3/ker(r)) tensor ker(B)
  -> 0,

dim_C ker(r tensor B)=32+dim_C ker(B)=48-rank(B).
```

No complement to `ker(r)` is chosen. The kernel is neither a named family
nor a mass or physical kernel.

For the direct sum of the two forward conjugate arrows, the domain has
complex dimension `96` and the ledger doubles:

| stratum | `rank(A_A direct-sum A_B)` / kernel | `rank(K_A direct-sum K_B)` / kernel |
|---|---:|---:|
| flat | `0 / 96` | `0 / 96` |
| rank-one null | `16 / 80` | `16 / 80` |
| isotropic two-plane | `24 / 72` | `24 / 72` |
| rank-one non-null | `32 / 64` | `32 / 64` |
| paired null, nonzero pairing | `32 / 64` | `24 / 72` |
| banked receiver | `32 / 64` | `32 / 64` |

Flat and degenerate strata are adverse local observations, not global kills.
A source-compatible intrinsic observation rule would have to say which
strata are admitted; constructing such a rule is off limits here.

### CB-5 fixed-frame successor qualification

CB-5's fixed `(eta_H,gamma_H)` trace is a transported chartwise decoration,
not the intrinsic graph-plane trace off the flat chart. Its legacy
internal-complex F/kappa ranks on the same six fixtures are

```text
flat/null/isotropic/non-null/paired/banked = 0/8/8/16/16/16.
```

The intrinsic sequence is `0/8/12/16/12/16`. In particular, the isotropic
and paired fixtures change rank. At the banked receiver the fixed and
intrinsic maps are unequal even though both have rank `16`. No CB-5
fixed-frame rank is promoted to intrinsic ownership here.

## 4. What the full `d0+varpi` collision blocks

Section 11.2 types the source labels as

```text
nu+ in Omega0(S+),    nu- in Omega0(S-),
zeta+ in Omega1(S+),  zeta- in Omega1(S-).
```

The selected real-K77 exterior derivative preserves ambient spin chirality:

```text
d0 : Omega0(S+) -> Omega1(S+),
d0 : Omega0(S-) -> Omega1(S-).
```

The H210 zero-order maps are odd:

```text
varpi_-+ : Omega0(S+) -> Omega1(S-),
varpi_+- : Omega0(S-) -> Omega1(S+).
```

Thus the two displayed summands in `(1,2)=d0+varpi_-+` do not presently land
in the same source-labelled/K77 bundle; the same mismatch occurs in `(0,3)`
and in the two reverse `d0*` cells. The product grading
`(-1)^form J` reproduces the support only after a one-form relabeling that
conflicts with the identity-grade section-11.2 labels. No such repair is
silently adopted.

This blocks all of the following:

1. treating the full cell as one homogeneous K77 operator;
2. assigning a rank, kernel, cancellation, spectrum, or mass statement to
   `d0+varpi`;
3. promoting the zero-order `32`-dimensional family kernel through the full
   cell;
4. declaring the reverse cells adjoints on a common domain; and
5. postcomposing the whole displayed cell with `kappa_J`.

It does **not** block isolating and composing the admitted zero-order H210
summand. The source displays the candidate matrix; this artifact neither
repairs nor rejects it as a complete operator.

## 5. Multi-lens audit and novelty

1. **Operator grammar:** only the zero-order part of the two off-diagonal
   forward cells enters the chain.
2. **Barred/unbarred duality:** row reversal uses a declared density-dual
   bridge, not a reality condition.
3. **Functor order:** Z projection, literal observation, intrinsic horizontal
   trace, and correlated lift remain different stages.
4. **Exact rank/kernel:** every family kernel follows from one exact sequence;
   no projected ranks are added.
5. **K77 parity/chirality:** the final composition remains odd and both halves
   are kept.
6. **Source custody:** F/imposter, Z/internal-144 partner, and `M_3` are never
   renamed as one another.
7. **Representation/corner typing:** pp/mm are zero-channel controls; forward
   and reverse completions are distinct.
8. **Observation:** graph-stratum ranks are local pointwise data, not a
   physical quotient.
9. **Adverse control:** flat, null, pp/mm, wrong-order, and full-cell mutations
   remain visible.
10. **Efficiency/novelty:** CB-2 already proves the cell placement and
    upstream rank; CB-5 already proves the pointwise split and family formula;
    CB-6A corrects geometric ownership to the intrinsic graph-plane lift.
    CB-6B adds the explicit typed stage ledger, intrinsic family-rank
    propagation, and maximal wrong-order witness. It is not a new branching
    theorem.
11. **Claim ceiling:** no horn, family, reduction, regime, or physics is
    selected.

## 6. Dependency and strongest falsifier

This artifact consumes the CB-6A intrinsic `kappa_J` interface: the moving
graph plane and orthogonal normal complement have separate cocycles, induced
Grams, graded Clifford frames, and complete right-domain Spin transport. The
stage chain is therefore an associated-carrier morphism on the admitted
nondegenerate overlaps. This does not choose an observer graph or supply
`H210-FCORR`, `H210-ALIGN`, or `H210-PSRED`.

The strongest finite wrong-order witness already passes:

```text
banked rank(kappa_J Gamma_H,J^intr O_J R)=16,
banked rank(P_Fcorr R)=0
```

per internal half. CB-6A now passes the prior strongest conditional
falsifier: the complete co-moving `kappa` square on both halves. Within the
present finite chain, an admitted banked replay with intrinsic rank below
`16`, unequal conjugate-half fingerprints, loss of odd off-diagonal parity,
or a nonzero pp/mm PS multiplicity would kill the stated composition. A flat
or degenerate raw graph alone does not. The unresolved derivative-half
collision prevents the next stronger full-cell falsifier from being
formulated honestly.

## Reproduction

```bash
sage -python tests/channel-swings/joe_directed_cb6_h210_equation916_observed_composition_probe.py
sage -python tests/channel-swings/joe_directed_cb6_h210_equation916_observed_composition_probe.py --selftest
```

The exact probe checks the source matrix ledger, row reversal, parity typing,
both finite fields, both ambient halves, the intrinsic graph/normal Grams and
correlated trace on all displayed rank/kernel strata, the qualified CB-5
chartwise controls, the family exact sequence, pp/mm zero controls, the
banked wrong-order witness, and semantic mutations.

## Strict claim ceiling

CB-6B certifies an intrinsic associated-carrier typed composition of the
conditional H210 zero-order arrow through literal observation and the
correlated-F adapter on the admitted nondegenerate graph overlaps. It
does not place `kappa` in equation (9.16), make the upstream H210 port F,
resolve the full derivative cell, or prove a common adjoint/domain. It does
not derive `H210-FCORR`, `H210-ALIGN`, or `H210-PSRED`, select a family or
observer, construct a reduction/action/quotient/external datum, or infer a
mass, scale, threshold, spectrum, observable, phenomenology, or public
prediction. The parent theory remains non-chiral and both conjugate halves
remain present.
