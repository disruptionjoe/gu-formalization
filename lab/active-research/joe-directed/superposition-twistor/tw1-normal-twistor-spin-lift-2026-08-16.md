---
artifact_type: exact_conditional_normal_twistor_spin_lift_and_rolled_square_result
created: 2026-08-16
status: SELECTED_COMPONENT_NORMAL_TWISTOR_SPIN_LIFT_EXACT__SQUARE_IS_MINUS_J10__ROLLED_SQUARE_IS_MINUS_JHAT__OPPOSITE_COMPONENT_SIGN_FENCED__NO_SELECTION_OR_PHYSICAL_SUPERPOSITION
channel: joe_directed_superposition_twistor_conditional_build
work_item: TW-1
target_claim: NONE-NOT-A-KILL
claim_grade: EXACT_CURRENT_K77_FIBREWISE_AND_ASSOCIATED_BUNDLE_KINEMATICS__SOURCE_SILENT__CONDITIONAL_HORN
source_return: SOURCE_SILENT
probe: tests/channel-swings/joe_directed_tw1_normal_twistor_spin_lift_probe.py
canon_verdict_change: none
ledger_row_changes: none
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# TW-1 — normal-twistor Spin lift on the selected current-K77 component

## Result first

Under the declared horn that a normal orthogonal complex structure has been
supplied on the selected connected component,

```text
J_N in SO_0(6,4)/U(3,2),
J_N^2=-1,
J_N^T eta_N J_N=eta_N,
```

its current-K77 Spin lift constructs exactly. This closes the adapter that the
twistor/BV and reverse-`J` artifacts had correctly left type-missing.

Choose an adapted same-sign frame

```text
(e_1,J_N e_1),...,(e_5,J_N e_5),
epsilon=(+,+,+,-,-),
```

whose complex orientation agrees with the repository's fixed `NORMAL` order.
With `gamma_a^2=eta_aa`, the infinitesimal spin operator is

```text
j_tilde = -(1/2) sum_i epsilon_i gamma(e_i)gamma(J_N e_i),
[j_tilde,gamma(v)] = gamma(J_N v).
```

The exponential-path lift is

```text
S_J = exp((pi/2) j_tilde)
    = product_i (1-epsilon_i gamma(e_i)gamma(J_N e_i))/sqrt(2).
```

It projects to the vector quarter-turn `J_N`. In the fixed repository
orientation and Clifford convention,

```text
S_J^2 = -J10,
S_J^4 = -1,
S_J^8 = 1.
```

Thus the vector transformation has order four while either of its two Spin
preimages has order eight. The other preimage `-S_J` has the same square. The
sign in the square is an **orientation-component sign**, not a choice between
the two central-sign lifts: on the opposite normal-complex-orientation
component, the exponential lift is `S_J^{-1}` and squares to `+J10` relative
to the same fixed normal volume.

This is also the exact relation to the previously owned rolled endomorphism.
Embed the vector transformation as

```text
g_J = I_BASE direct-sum J_N,
g_J^2 = R_split,
```

and use simultaneous vector-spin transport on the one-form spinor:

```text
S_hat_J = (g_J tensor S_J) direct-sum S_J
           on Omega1(S) direct-sum Omega0(S).
```

Then `S_hat_J` preserves the gamma-trace carrier and

```text
S_hat_J^2 = -[(R_split tensor J10) direct-sum J10]
           = -Jhat.
```

The result relates four formerly separate objects; it does not identify them.
In particular, `S_J` is a group element, not the spinor complex structure
`J10`, and neither is a physical scalar multiplication or a derivation of
quantum superposition.

## Conditional-build horn and stop boundary

`TW1-NORMAL-J` assumes one compatible `J_N` field or fibre point. The source
and repository have not selected it by an action, vacuum, external datum,
boundary condition or physical state. This swing asks only what follows if
such a source-native normal reduction exists.

The build stops after fibrewise Spin lifting, associated-bundle naturality,
rolled-carrier typing and exact spectra. It does not construct or select:

- a GU action, connection, vacuum, coefficient or source datum;
- an observer domain, positive pairing, quotient or physical cohomology;
- a family row, imposter/partner alignment, scale or observed particle label;
- a Penrose pushforward, twistor interaction or decoherence functional; or
- an ordinary index, standard Higgs/VEV or `Cl(9,5)` substitute.

## Ten-lens preflight and assessment

| lens | exact question and disposition |
|---|---|
| source fidelity | `SOURCE-SILENT`: the source owns the broader complex/split language, not this lift, its square or a physical interpretation. |
| `2+1` / imposter / partner | The lift acts uniformly on normal spinors. It identifies no `F`, `M_3` row or internal `144`, and supplies no family selector. |
| emergent chirality / both halves | `S_J` is even and commutes with ambient chirality. Both K77 halves and all four observation blocks remain present. |
| vector-versus-spinor Layer 0 | `J_N`, `j_tilde`, `S_J`, `J10` and `Jhat` have different carriers and roles; the square relations are adapters, not identities. |
| Spin covering topology | The exponential path selects one lift on the declared component; `-S_J` is the other. Central sign does not alter the square, whereas reversing complex orientation does. |
| exact Clifford real form | The certificate uses the current real `Cl(7,7)` module with normal signature `(6,4)`. No K95 result is transferred. |
| stabilizer / equivariance | The vector and Spin centralizers have kernel dimension `25`, exactly `u(3,2)`, with orbit dimension `20`. |
| associated-bundle naturality | `J -> gJg^-1` carries `j_tilde -> gj_tilde g^-1` and `S_J -> gS_Jg^-1`; central overlap signs cancel in conjugation. |
| prior art / novelty | Prior work constructed the orbit, moving BRST and `J10/Jhat` separately and explicitly listed this adapter as missing. No prior exact `S_J^2` or order/spectrum theorem was found. |
| conditional boundary / falsifier | A failed Clifford adjoint, wrong square, smaller centralizer, half mixing or failed co-moving square would kill this lift horn. None occurs. |

## Exact construction and rational certificate

Use the repository axis split

```text
BASE   = (0,7,8,9),
NORMAL = (1,2,3,4,5,6,10,11,12,13)
```

and the selected adapted pairs

```text
(1,2),(3,4),(5,6)     positive,
(10,11),(12,13)       negative.
```

Each signed bivector `B_i=gamma_ai gamma_bi` squares to `-1`, and the five
disjoint bivectors commute. The exact probe avoids algebraic-number matrix
arithmetic by setting

```text
T = sqrt(32) S_J = product_i (1-epsilon_i B_i).
```

It proves over the rationals that

```text
T^-1 = product_i (1+epsilon_i B_i)/2,
T gamma(v) T^-1 = gamma(g_J v),
T^2 = -32 J10,
T^4 = -1024,
T^8 = 1048576.
```

The normalization then gives the asserted order and square without numerical
matrix exponentiation. A direct adverse control rejects `T^2=+32 J10`, and
`J10` itself is shown to project to `R_split`, not to the quarter-turn `g_J`.

## Orientation-component sign

The sign is fixed only after orienting the normal twistor component relative
to the ambient normal volume. In complex dimension five, replacing `J_N` by
`-J_N` reverses the induced complex orientation. The exponential lift becomes
`S_J^{-1}`, and the rational certificate gives

```text
(S_J^-1)^2 = +J10
```

relative to the unchanged repository `J10`. Therefore the unqualified formula
`S_J^2=-J10` belongs to the selected orientation-aligned `SO_0` component.
The larger notation `O(6,4)/U(3,2)` must retain this component tag whenever a
fixed-volume sign is reported. Changing `S_J` to `-S_J` does **not** change
the sign and cannot be used to cross this fence.

## Stabilizer, covariance and associated bundles

The complete `45`-generator normal calculation gives

```text
rank(A -> [A,J_N]) = 20,
dim ker(A -> [A,J_N]) = 25.
```

The independent Spin calculation gives the same coefficient kernel for

```text
A_tilde -> [A_tilde,S_J].
```

Thus the infinitesimal centralizer is exactly `u(3,2)`, and its lifted action
commutes with `j_tilde`, `S_J` and `J10`. Consequently

```text
J_N'       = g J_N g^-1,
j_tilde'   = g j_tilde g^-1,
S_J'       = g S_J g^-1
```

is a well-defined equivariant construction on each declared component. If a
full ambient co-moving frame changes the normal subspace, `J10` moves too and
the differentiated identity remains

```text
delta(S_J^2) = -delta(J10).
```

This supplies associated-bundle naturality, not a global section, a preferred
reduction or an action-selected field. It also does not revive a physical
`+/-Jhat` bit: the prior reverse-`J` census already places those signs in one
conditional larger moving source-frame redundancy orbit.

## Exact spectrum and the four K77 observation blocks

Let `zeta_8=exp(i pi/4)`. In the repository compact-normal chirality naming,

```text
S10+ : J10=+i,
S10- : J10=-i.
```

The exact five-weight enumeration gives

| normal half | `S_J` eigenvalues and multiplicities | `j_tilde` weights |
|---|---|---|
| `S10+` | `zeta_8^7` x `10`, `zeta_8^3` x `6` | `(-1)` x `10`, `(+3)` x `5`, `(-5)` x `1`, each times `i/2` |
| `S10-` | `zeta_8^1` x `10`, `zeta_8^5` x `6` | `(+1)` x `10`, `(-3)` x `5`, `(+5)` x `1`, each times `i/2` |

Because the base Weyl factor has complex rank two, the four blocks are

| block | ambient half | exact finite-lift spectrum |
|---|---|---|
| `++` | `S14+` | `zeta_8^7` x `20`, `zeta_8^3` x `12` |
| `--` | `S14+` | `zeta_8^1` x `20`, `zeta_8^5` x `12` |
| `+-` | `S14-` | `zeta_8^1` x `20`, `zeta_8^5` x `12` |
| `-+` | `S14-` | `zeta_8^7` x `20`, `zeta_8^3` x `12` |

Each block remains complex rank `32`; each ambient half remains complex rank
`64`; and the two ambient spectra agree. The lift preserves rather than
selects these blocks. It therefore supplies no ordinary net-chirality index
and no substitute for Weinstein's observation-and-decoupling proposal.

## What changed and what did not

The exact gap between the normal vector twistor and the spinor/rolled volume
operators is now closed at conditional kinematic grade:

```text
normal vector J_N      --Spin exponential--> S_J,
S_J^2                  = -J10               selected component,
rolled S_hat_J^2       = -Jhat.
```

This strengthens the moving-normal-twistor route because its principal
objects now live in one explicit current-K77 associated construction. It also
sharpens the limitation: the Spin lift is an eighth-order group action, not
the square-minus-one physical complex structure itself. No action-owned total
complex, physical cohomology, closed domain, positive pairing or superposition
interpretation follows.

## Falsifiers and adverse controls

The declared lift would fail if any of these occurred:

- `[j_tilde,gamma(v)] != gamma(J_N v)` on one normal axis;
- the rational adjoint failed to project to `g_J`;
- `T^2` differed from the orientation-tagged volume relation;
- the Spin centralizer kernel differed from the vector `u(3,2)` kernel;
- `S_J` mixed either ambient K77 half or deleted one `2 x 16` block;
- simultaneous vector-spin transport failed to preserve gamma trace; or
- a co-moving ambient frame broke the differentiated square relation.

The probe also rejects eight hostile mutants: the wrong selected sign, direct
`S_J=J10` identification, volume-as-quarter-turn, central-sign/component
confusion, opposite-component sign erasure, `so(6)+so(4)` stabilizer
substitution, half deletion and physical-family selection.

## Reproduction and claim ceiling

```text
sage -python tests/channel-swings/joe_directed_tw1_normal_twistor_spin_lift_probe.py
sage -python tests/channel-swings/joe_directed_tw1_normal_twistor_spin_lift_probe.py --self-test
```

The strongest licensed statement is:

> On the declared orientation-aligned normal-twistor horn, the selected
> current-K77 vector complex structure has an explicit equivariant order-eight
> Spin lift whose square is `-J10`; its simultaneous rolled lift squares to
> `-Jhat`, preserves both ambient halves, and has the stated exact four-block
> spectrum.

It is not licensed to say that the source selected `J_N`, that `S_J` is the
physical imaginary unit, that the lift proves emergent chirality, or that GU
has derived quantum superposition.
