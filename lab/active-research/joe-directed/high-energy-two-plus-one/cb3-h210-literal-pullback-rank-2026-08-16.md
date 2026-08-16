---
artifact_type: exploration
status: exploration
doc_type: conditional_build_exact_observation_gate
created: 2026-08-16
work_item: CB-3A-H210
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-3A H210: literal graph pullback has exact signature-sensitive rank strata, but raw section-slope survival is not yet an intrinsic observation statement"
grade: "EXACT signed-permutation Cl(7,7) and rational/integer rank arithmetic for the declared H210 CB-1 tensor. Both ambient Weyl halves, flat/non-null/totally-isotropic/paired-null strata, basis-free family kernels, and planted controls are checked. The classification concerns literal differential-form contraction through a raw graph slope J only. It does not identify associated-bundle restriction, the canonical K77 Cartan/Spin lift, or a physical quotient, and it does not derive or vary an action, background, vacuum, selector, family row, mass, scale, threshold, or observable."
disposition: RAW_GRAPH_PULLBACK_EXACTLY_STRATIFIED__GENERIC_NON_NULL_INJECTIVE__TOTALLY_ISOTROPIC_KERNELS__J_ZERO_KILLS_PURE_NORMAL_REPRESENTATIVE__INTRINSIC_OBSERVATION_SURVIVAL_NOT_YET_ESTABLISHED
canon_verdict_change: none
steering_effect: "Carry this rank table and the exact banked receiver test point into the co-moving naturality square. Do not promote generic coordinate-J survival. Compose associated restriction, literal contraction, co-moving K77 Cartan/Spin naturality, and any physical quotient as successive stages. Keep fixed trace-Hq as an adverse TYPE_MISSING subhorn and keep action/external-datum work off limits."
scripts:
  - tests/channel-swings/joe_directed_cb3_h210_literal_pullback_probe.py
depends_on:
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb1-h210-k77-rs-intertwiner-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb2-h210-equation916-cross-half-composition-2026-08-16.md
  - lab/active-research/joe-directed/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md
  - tests/channel-swings/selected_k77_canonical_section_jet_cartan_spin_prolongation_probe.py
  - tests/channel-swings/selected_k77_finite_section_projector_atlas_descent_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — CONDITIONAL BUILD, H210.** The nonzero CB-1 `210`
> port is an assumed horn. Ordinary family indices, net-chirality arguments,
> scalar-Higgs VEVs, and conventional mass mechanisms do not adjudicate this
> source-native route. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.
>
> Deriving or varying the source action, choosing a vacuum/background, importing
> an external selector, or fitting a family covector is outside this lane. The
> source imposter is the F-shaped `128 = S(X) tensor S(N)`. The `144` is its
> predicted high-energy partner sector; it is never renamed “the imposter.”
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-3A — literal graph pullback of the H210 port

## Result first

Let the observation section have raw graph differential

```text
L_J = (I,J): H -> H + V,       J: H -> V,
```

and let the banked CB-1 tensor have only internal one-form components

```text
T_a = c_a Gamma_a phi_4,
c_a = -2/5 on A_6,       c_a = +3/5 on B_4,
signature(V) = (6,4).
```

Literal differential-form pullback contracts the internal one-form leg:

```text
(O_J T)_mu = sum_a J_(a mu) T_a
           = Gamma(w_mu) phi_4,
w_mu       = sum_a c_a J_(a mu) e_a.

O_J T : 16 -> T*X tensor s^*S.
```

Literal contraction consumes the free normal covector index. A nonzero rank
therefore does not mean that a free Z/internal-`144` representation remains as
the codomain after observation; it means the contracted spinor-valued 4D
one-form map is nonzero at this stage.

An irrelevant common factor has been suppressed. Write `W_J` for the span of
the four weighted vectors `w_mu` in the internal `(6,4)` space. Then, on either
internal complex Weyl `16`, the exact classification is:

| weighted row-space `W_J` | rank `O_J T` | kernel `O_J T` |
|---|---:|---:|
| `0` (`J=0`) | `0` | `16` |
| contains a non-null vector | `16` | `0` |
| totally isotropic, dimension `k=1` | `8` | `8` |
| totally isotropic, dimension `k=2` | `12` | `4` |
| totally isotropic, dimension `k=3` | `14` | `2` |
| totally isotropic, dimension `k=4` | `15` | `1` |

The real Witt index is four, so these exhaust the totally isotropic real
strata available to a rank-at-most-four graph. Two null generators with
nonzero mutual pairing are not a totally isotropic plane: their span contains
a non-null vector, and the map is again injective.

On either real ambient K77 Weyl half, multiply the displayed ranks and kernels
by four. The opposite ambient half has the identical fingerprint. Thus this
calculation preserves the fundamentally non-chiral parent carrier; it does not
select one half as physical.

For any declared nonzero family covector `r in M_3*`, `dim_C M_3=3`, the composed
row has

```text
0 -> ker(r) tensor S_16 -> ker(r tensor O_J T)
  -> (M_3/ker(r)) tensor ker(O_J T) -> 0,

ker(r tensor O_J T)
  = (ker r tensor S_16) + (M_3 tensor ker(O_J T)),

dim_C ker(r tensor O_J T) = 32 + dim_C ker(O_J T) = 48 - rank(O_J T).
```

Here `M_3` is the three-dimensional family-multiplicity space; `F` is reserved
for the source's distinct equation-(12.22) imposter summand. The exact sequence
is invariant and chooses no complement to `ker(r)`.

Consequently the family-kernel dimensions are `32` on the non-null stratum,
`40,36,34,33` on the isotropic `k=1,2,3,4` strata, and `48` at `J=0`. This is a
basis-free algebraic kernel. It names no family and is not a mass kernel.

The most important qualification is equally exact: **these are raw-coordinate
graph-pullback ranks, not yet intrinsic observation ranks.** At `J=0`, literal
contraction kills this pure-normal representative even though associated-bundle
restriction retains the nonzero tensor in the restricted fibre. Under a
co-moving K77 frame change, both the graph and the tensor/spin frame must move;
holding `T` pure-normal while changing only `J` is not that natural operation.
Nothing here supplies a physical quotient.

The already-banked canonical receiver **test point** lies in the injective raw
stratum. Substituting its exact ten-by-four jet gives weighted Gram matrix

```text
diag(614591/3553225,
     1171823/13608721,
     715/29241,
     1027/64009).
```

All four entries are nonzero. Thus this repository test point gives raw rank
`16`, kernel `0` per internal complex Weyl copy, raw rank `64` per real ambient
half, and family-input kernel `32`. It is not a nature-selected section or a
co-moving/physical observation theorem.

## Conditional-build contract

All five packet rules are active:

1. Horn `H210` is declared compatible and nonzero; `H54` is absent.
2. The task is downstream composition of the banked CB-1/CB-2 port only.
3. Source-action construction, background/vacuum selection, external-data
   search, and coefficient fitting are off limits.
4. Both ambient halves and the conjugate arrow are retained. No ordinary net
   chirality argument replaces Weinstein's emergent-chirality proposal.
5. No algebraic kernel is promoted to a named family, mass, scale, threshold,
   observable, or prediction.

The source typing is also fixed: HE-1 Fence 1 resolves *imposter* onto the
F-shaped `128`. The `144` is the distinct high-energy partner with which the
unlabelled family direction is proposed to recombine. This calculation tests
only whether the already-banked `16 <-> 144` partner port survives one literal
contraction model.

## Problem-specific preflight — six divergent lenses

### 1. Differential-geometric lens

Use the actual graph `L_J=(I,J)`. Its one-form pullback is `L_J^T`, so a
pure-normal one-form is sent to `J^T` times its coefficient. This is the VZ-4
correction: pullback is a contraction, not deletion of the normal summand and
not a KK projection. Prediction: the CB-1 tensor vanishes at `J=0` but need not
vanish for nonzero slope.

### 2. Exact Clifford/rank lens

Factor the common invertible `phi_4` and classify the stacked Clifford maps
`Gamma(w_mu)`. If any `w_mu` is non-null, `Gamma(w_mu)^2=q(w_mu)I` makes one
component invertible. If their span is totally isotropic, use the chiral-spinor
annihilator filtration. Prediction: the kernel sequence is `8,4,2,1`, not an
all-or-nothing rank.

### 3. Representation/family lens

Run both K77 Weyl halves and state the family result as `ker(r)`, never as a
chosen basis vector. Prediction: the two halves have equal ranks and a nonzero
row leaves the same two-family plane only on the injective stratum.

### 4. Naturality/gauge lens

Separate four operations that earlier artifacts placed near one another:

```text
raw coordinate graph shear
canonical reciprocal-block K77 Cartan/Spin completion
associated-bundle restriction
physical observation/quotient.
```

Prediction: a rank table for the first operation cannot by itself establish
the fourth. In particular, changing a splitting while freezing a tensor that
was declared pure-normal is not a co-moving bundle transformation.

### 5. Emergent-chirality lens

Every `T_a` is K77-chirality odd. Check both domain halves rather than retaining
only the half that resembles a luminous package. Prediction: identical rank
fingerprints, with the conjugate arrow intact.

### 6. Falsifier/control lens

Use `J=0`, a rank-one non-null jet, totally isotropic jets of every possible
real dimension, and two null rows with nonzero mutual pairing. Plant three
wrong rules: “nonzero `J` implies injective,” “rank `J` alone decides,” and
“normal projection is pullback.” Prediction: all three plants fire.

## Exact derivation

### Weighted Clifford reduction

The CB-1 coefficients are nonzero on all ten internal axes, so diagonal
weighting by `c_a` is invertible as a vector-space map. It does not preserve
the `(6,4)` quadratic form, however. The relevant signature test must therefore
be performed on the **weighted** vectors `w_mu`, not directly on the unweighted
columns of `J`. This is why `rank(J)` alone cannot decide the spinor-map rank.

After suppressing a common factor `1/5`, the exact probe uses weights `-2` on
the six positive axes and `+3` on the four negative axes. The stacked map is

```text
S_+ -> H* tensor S_-,       psi |-> (Gamma(w_mu) phi_4 psi)_mu,
```

and similarly with plus and minus exchanged. Since `phi_4` is invertible, its
kernel is the common annihilator of all `Gamma(w)` for `w in W_J`.

### Non-null stratum

If `q(w) != 0` for one `w in W_J`, then

```text
Gamma(w)^2 = q(w) I,
```

so that component is invertible from one Weyl half to the other. The stacked
map is therefore injective. More generally, if the restricted bilinear form
on `W_J` is not identically zero, `W_J` contains a non-null linear combination;
this includes a plane generated by two null vectors with nonzero pairing.

### Totally isotropic strata

For a totally isotropic `k`-plane, choose a Witt basis. The `k` Clifford
operators become independent creation/annihilation operators. Their common
annihilator on a complex chiral spinor has dimension

```text
2^(4-k),       1 <= k <= 4.
```

The probe verifies canonical rational representatives exactly in the current
signed-permutation `Cl(7,7)` implementation on both ambient Weyl halves:

```text
w_i = 6(e_i + f_i),       q(e_i)=+1, q(f_i)=-1, i=1,...,k.
```

It obtains ambient ranks `32,48,56,60`, hence internal-complex ranks
`8,12,14,15`. Orthogonal/Spin transport preserves rank, so these canonical
representatives classify each real totally isotropic orbit at the local
linear-algebra level.

## What the four nearby “observation” operations do

| operation | object returned | what happens at raw `J=0` | status here |
|---|---|---|---|
| literal differential-form pullback `L_J^T` | four one-form components | pure-normal `T` contracts to zero | computed exactly |
| associated-bundle restriction `s^*E` | same fibre type over the section | the internal `T` fibre remains nonzero | typing control only |
| canonical K77 Cartan/Spin completion of `J` | reciprocal-block orthogonal frame motion plus spin lift | graph and Clifford frame co-move | owned prior art; not identified with `L_J^T` |
| physical observation/quotient | would require a declared reduction/cohomology/domain | not determined | missing, no claim |

This table prevents two opposite errors. Literal pullback is not a normal
projection, so nonzero normal components can survive for nonzero raw slope.
But associated restriction and co-moving Cartan transport also prevent the
coordinate calculation from being promoted directly to a gauge-invariant
physical field count.

## Fixed trace-`H_q` adverse subhorn

CB-1 already proves that the owner blade is admitted by fixed trace `H_q`, but
that no common phase makes all ten components simultaneously PS equivariant,
gamma traceless, and `H_q`-unitary. Componentwise phase completion destroys the
gamma trace. CB-3A does not repair or re-run that missing port: its rank table
is conditional on the real current-K77 tensor before the fixed-`H_q`
connection constraint. The fixed-`H_q` realization remains `TYPE_MISSING`, an
adverse repository-constructed subhorn rather than a source-level no-go.

## Controls and plants

The exact probe includes:

- `J=0`: rank `0`, proving the contraction is genuinely slope-sensitive;
- rank-one positive vector: rank `16`, a non-null positive control;
- rank-one null vector: rank `8`, killing “nonzero `J` means injective”;
- isotropic `k=2,3,4`: ranks `12,14,15`, checking the annihilator ladder;
- two null generators with nonzero pairing: rank `16`, proving individual
  nullness is not the criterion;
- the banked rank-four receiver jet: exact positive diagonal weighted Gram,
  raw rank `16`, and family-input kernel `32`;
- two rank-one jets with different signature and different spinor ranks,
  killing “rank `J` alone decides”;
- a nonflat normal component whose literal contraction is nonzero, killing the
  replacement of pullback by normal projection;
- associated restriction at `J=0`, which retains the nonzero fibre tensor and
  therefore cannot be silently identified with literal contraction.

## Reprioritization inside CB-3

| next item | priority | reason |
|---|---:|---|
| staged observation composition | 1 | compose associated restriction, literal contraction, co-moving naturality, then any physical quotient without substituting one stage for another |
| intrinsic/co-moving survival of the family-to-144-partner port | 2 | raw generic `J` and the exact banked test point are insufficient without the Cartan/Spin naturality square |
| quotient/domain survival | 3 | still downstream, but premature before the observation map is intrinsic |
| fixed trace-`H_q` | adverse control | remains `TYPE_MISSING`; do not invent a phase or new Hermitian datum |
| derive action/background/selector | off limits | violates the conditional-build contract |

The exact raw rank table is fertile because it supplies a sharp falsifier for
any proposed observation functor: the functor must explain why it lands in a
particular stratum, or show that co-moving covariance makes that stratification
coordinate-only. It does **not** authorize choosing a convenient non-null `J`.

## Claim ceiling

This artifact establishes only a finite-dimensional, local, exact rank
classification for literal raw graph pullback of the assumed H210 port. It
does not identify the source's full observation operation, construct a source
action or external datum, select a section, choose a family, delete a chiral
half, prove quotient or domain survival, or infer a particle spectrum, mass,
scale, threshold, observable, or phenomenology. It makes no canon or public
posture change.

## Reproduction

```bash
_local/cas-venv/bin/python tests/channel-swings/joe_directed_cb3_h210_literal_pullback_probe.py
```

The probe uses exact signed-permutation Clifford matrices and exact
integer/rational elimination only; no floating-point arithmetic appears.
