---
artifact_type: exact_local_twistor_projector_yang_mills_detour_and_gu_operator_composition_result
created: 2026-08-14
status: LOCAL_TWISTOR_CONNECTION_CONSTRUCTED_FROM_OBSERVED_CONFORMAL_SPIN_GEOMETRY__UNTWISTED_CURVED_COMPLEX_CLOSES_ON_BACH_FLAT_LOCUS__FULL_GU_TWIST_AND_ROLLED_OPERATOR_ADAPTER_OPEN
source_return: STANDARD_GEOMETRY_SUPPLIES_LOCAL_TWISTOR_CONNECTION_AND_BACH_FLAT_DETOUR_THEOREM__GU_SOURCE_OWNS_NEITHER_FULL_BACH_EQUATION_NOR_DETOUR_OPERATOR_IDENTIFICATION
ledger_rows: [LT-SM8]
ledger_hypothesis: HYP-TW-COHERENCE-01
registry: lab/process/selected-k77-local-twistor-bach-detour-composition-gate.json
probe: tests/channel-swings/selected_k77_local_twistor_bach_detour_composition_gate_probe.py
canon_verdict_change: none
---

# Selected K77 local-twistor/Bach-detour composition gate

## Result first

The recommended general-Lorentzian H3 branch has a better answer than either
“the twistor connection must be flat” or “generic curvature kills the route.”

The observed four-dimensional conformal spin geometry canonically constructs
the local-twistor, or spin-tractor, connection. Its curvature contains the
Weyl and Cotton tensors, so its raw covariant square is generically nonzero.
Demanding

```text
(D_local-twistor)^2 = 0
```

would simply return the conformal-flatness wall already found by the strict
holomorphic route. That is too strong for a curved cohomological construction.

The correct curved successor is the Yang--Mills detour sequence. In four
dimensions the spin-tractor connection is Yang--Mills exactly when the
conformal structure is Bach-flat, and on that locus the twistor-spinor
sequence

```text
S[1/2] --T--> Tw --N--> Tw* --T*--> S[-1/2]
            order 1   3       1
```

is a differential complex. This admits non-conformally-flat curved positive
controls: every Einstein four-metric is Bach-flat, including Ricci-flat
Schwarzschild and Kerr, while generally retaining nonzero Weyl curvature.

This changes the strongest hypothesis:

> The natural curved coherence locus is not presently `II=0`. It is the locus
> on which the action-selected total twistor-plus-normal connection satisfies
> its Yang--Mills equation. On the untwisted observed base, that condition is
> Bach-flatness. Only on this locus does the twistor-spinor detour sequence
> supply a curved complex whose cohomology could later be tested as a state
> carrier.

Two hard GU-specific gates remain. First, the repository owns a Bach operator
only as a spin-two/TT shadow of candidate Willmore or curvature-squared
dynamics; the released fundamental law is curvature-linear and does not yet
derive the full Bach equation. Second, tensoring the base spin-tractor
connection with the normal/mixed K77 connection changes the condition from
base Bach-flatness to the Yang--Mills equation for the **total** twisted
connection. A nonzero normal or mixed Yang--Mills current obstructs the
complex even when the base is Bach-flat.

The current GU rolled Dirac--Rarita--Schwinger operator is also not the detour
middle operator. Their orders and typed domains differ. No physical
superposition, positive pairing or decoherence law follows yet.

## 1. The local-twistor connection now constructs

Choose a representative metric in the observed conformal class. A chiral
local twistor splits as

```text
Z = (omega^A, pi_A'),
```

which has complex rank `2+2=4` and is the curved bundle version of the prior
local/developable carrier

```text
T_GU = S_L direct-sum S_R*.
```

Up to conventional factors of `i` and index placement, the local-twistor
connection is

```text
D_AA' (omega^B,pi_B')
 = (nabla_AA' omega^B + delta_A^B pi_A',
    nabla_AA' pi_B' + P_ABA'B' omega^B),
```

where `P` is the Schouten tensor. Changing conformal scale changes the split,
not the underlying connection. Thus the previous global-marking debt is
replaced on a curved base by an associated rank-four bundle with a canonical
normal conformal connection.

Its curvature is triangular by representation type:

```text
Omega_local-twistor = [ Weyl+       0   ]
                       [ Cotton    Weyl- ].
```

The exact probe carries three firing controls:

```text
conformally flat:      rank(Omega)=0;
Einstein, Weyl!=0:     rank(Omega)>0, Cotton=0;
generic curved:        Weyl and Cotton blocks both live.
```

A parallel local twistor is therefore a special holonomy solution. A section
of the local-twistor bundle exists without being parallel, and the bundle plus
connection exist without conformal flatness. These three statements must not
be collapsed.

## 2. Why the detour condition is the right curved square

For any connection `D` on a bundle `V`, the Yang--Mills detour construction is

```text
Omega0(V) --d_D--> Omega1(V) --M_D--> Omega1(V) --delta_D--> Omega0(V),
```

with the curvature correction in `M_D` chosen so that

```text
M_D d_D = epsilon(delta_D F_D),
delta_D M_D = -iota(delta_D F_D).
```

Consequently this is a complex exactly when the connection satisfies its
Yang--Mills equation

```text
delta_D F_D = 0.
```

The probe verifies the composition identity over exact rationals on a
nonabelian connection with nonzero current, and a commuting flat control. The
generic control fires `M_D d_D != 0`; the flat control closes.

For the normal conformal tractor connection in four dimensions, the
Yang--Mills current is the Bach tensor. Prolonging and projecting the detour
construction yields the conformally invariant twistor-spinor detour sequence
above. Its middle operator `N` is third order. The sequence is a complex iff
the four-dimensional conformal structure is Bach-flat.

This is strictly weaker than conformal flatness:

```text
conformally flat  => tractor flat => Bach-flat,
Bach-flat         does not imply tractor flat.
```

The repo's existing exact controls already record the key nontrivial example:
Einstein metrics are Bach-flat, while Schwarzschild has nonzero Weyl curvature.

## 3. The four-dimensional/ambient projector adapter

Let `Gamma_4` be four-dimensional Clifford trace and `j_4` Clifford
injection. Then

```text
Gamma_4 j_4 = 4 I,
Pi_4 = I - (1/4) j_4 Gamma_4.
```

The exact rational Clifford control proves

```text
Pi_4^2=Pi_4,
Gamma_4 Pi_4=0,
rank_C(Tw_Dirac)=12,
rank_C(Tw_chiral)=6.
```

This is not the base block of the ambient projector

```text
Pi_14 = I - (1/14) j_14 Gamma_14.
```

If a base-supported vector-spinor is fed to `Pi_14`, its base block has

```text
Gamma_4 Pi_14,base = (5/7) Gamma_4.
```

The missing cancellation occurs through the ten normal one-form components
created by the ambient Clifford injection. Therefore the ambient projector
does not preserve the base-supported subspace and cannot be substituted for
`Pi_4` in the twistor-gradient.

There is nevertheless an exact positive adapter:

```text
Pi_14,base Pi_4 = Pi_4 Pi_14,base = Pi_4.
```

An already four-dimensionally gamma-traceless vector-spinor embeds in ambient
`ker Gamma_14` with zero normal one-form component. So the target carrier is
compatible; the source-to-target projectors and differentials are not equal.

## 4. Direct operator identification fails

The Bach-flat detour sequence has types

```text
spinor --order 1--> 4D gamma-traceless vector-spinor
        --order 3--> dual gamma-traceless vector-spinor
        --order 1--> dual spinor.
```

The currently owned GU operator is a first-order rolled operator on

```text
Omega1(S_14) direct-sum Omega0(S_14),
```

with a fourteen-dimensional gamma-trace/graph structure and an ambient
principal symbol. It is not the third-order detour middle map. The dimensions,
orders and source/target bundles differ before any lower-order comparison is
attempted.

This does not prove that the two constructions are unrelated. A valid bridge
could factor the detour operator through the rolled first-order connection,
its formal adjoint and curvature corrections. But that factorization must be
constructed and compared with the owned Shiab/Dirac/RS matrix; it cannot be
asserted from the shared word “twistor” or from gamma-tracelessness alone.

The exact disposition is:

```text
4D Tw carrier -> embeds in ambient ker Gamma14: PASS,
Pi4 = Pi14 or T = rolled GU operator: FAIL,
curved factorization through owned GU operator: OPEN.
```

## 5. The normal/mixed twist raises the real GU condition

The physical observation summands include normal spinors, so the likely
connection has tensor-product form

```text
D_total = D_spin-tractor tensor 1 + 1 tensor D_normal/mixed.
```

Its curvature and Yang--Mills current schematically split as

```text
F_total = F_tractor tensor 1 + 1 tensor F_normal/mixed,
delta F_total = Bach tensor 1 + 1 tensor J_normal/mixed + cross terms.
```

The exact probe tensors a zero-current base control with a nonzero-current
normal control. The total current remains nonzero. Hence

```text
base Bach-flatness is necessary for the untwisted base detour,
base Bach-flatness is not sufficient for the full GU-twisted complex.
```

An action-owned cancellation among base, normal and mixed currents is logically
possible, but would be a derived coupling equation, not an automatic property
of tensor products. This is where the previously computed mixed `4 x 10`
connection belongs. It is not itself the Bach tensor and not yet the
normalized Willmore second fundamental form.

## 6. What this does to the coherence hypothesis

The prior strongest wording placed coherence at `II=0`, or equivalently a
totally geodesic split. The detour result exposes that as unnecessarily
restrictive for the existence of a curved complex.

The better hierarchy is:

```text
Level A: tractor flatness / conformal flatness
         -> parallel local-twistor frame and ordinary flat BGG complex;

Level B: tractor Yang--Mills / Bach-flatness
         -> curved twistor-spinor detour complex, even with Weyl!=0;

Level C: total twisted Yang--Mills
         -> candidate GU complex after the normal/mixed connection is included;

Level D: positive BV/BFV cohomology
         -> possible physical superposition carrier;

Level E: open-system observable law
         -> possible decoherence statement.
```

GU currently reaches the canonical construction at Level A's bundle/connection
but not its flatness, and it has a standard-field Level-B theorem plus an
in-repo Bach shadow. It has not shown that the selected action places the
observed metric at Level B, that the total connection reaches Level C, or that
Levels D--E exist.

The strongest live hypothesis is therefore:

> GU's action may be selecting a Yang--Mills connection on a total
> twistor/normal bundle. The base component of that equation is Bach-flatness;
> its normal and mixed components are additional field equations. If the
> resulting detour complex survives BV/BFV reduction and positivity, its
> cohomology is a more credible home for superposition than a pointwise complex
> structure or a globally flat twistor connection.

## 7. Inefficiency audit

This gate removes three major costs from the previous formulation:

1. **Tool-hypothesis mismatch:** requiring `D^2=0` confused a flat connection
   with a differential complex. The detour curvature correction needs only the
   Yang--Mills equation.
2. **Signature/causal overhead:** the local-twistor connection and Lorentzian
   detour sequence live directly on the observed conformal spin base; no
   Euclidean continuation is required for H3.
3. **Redundant encoding:** the exact `Pi_4 -> ker Gamma_14` embedding identifies
   the shared carrier content while retaining the unequal projectors, rather
   than rebuilding two unrelated RS bundles or declaring them identical.

It also exposes two remaining inefficiencies:

- **Layer multiplication:** a third-order detour operator and a first-order GU
  rolled operator are parallel encodings until a factorization proves why both
  are needed.
- **Assumption-to-power ratio:** Bach-flatness, total twisted Yang--Mills,
  endpoint admission, a closed domain and positivity are still five distinct
  conditions before any quantum claim.

## 8. Seven-axis disposition

| layer | result |
|---|---|
| Layer 0 | rank-four spin tractor, rank-four base Dirac spinor, `Tw_4`, ambient `ker Gamma_14`, tractor flatness, Bach-flatness and physical cohomology separately typed |
| L1 algebra | `Pi_4` exact, rank 12 Dirac/rank 6 chiral; exact embedding in ambient gamma-trace kernel |
| L2 representation | chiral local twistor has rank four; Dirac spin tractor is the sum of two chiral rank-four halves |
| L3 geometry | local-twistor connection canonical; curvature is Weyl/Cotton; untwisted detour complex iff Bach-flat in 4D |
| L4 dynamics | full action ownership of Bach-flatness and total twisted Yang--Mills equation open |
| L5 observation | Lorentzian H3 survives on non-conformally-flat Einstein backgrounds without Wick rotation |
| L6 physics | direct GU rolled-operator equality fails; factorization, endpoint admission and BV/BFV cohomology open |
| L7 positivity | no positive reduced pairing, Hilbert completion or decoherence functional |

## 9. Decisive next sequence

1. Build the normal conformal spin-tractor connection from the observed GU
   metric and verify its Weyl/Cotton curvature formula in repo conventions.
2. Compute the full source-action metric equation and ask whether it implies
   Bach-flatness, only Einstein-plus-Bach balance, or neither.
3. Tensor with the normal/mixed K77 connection and compute the complete
   Yang--Mills current, including Codazzi/Ricci and normalized-`II` terms.
4. Attempt the exact factorization of the third-order detour middle map through
   the owned first-order rolled operator and its adjoint. Kill direct identity;
   retain only a proved factorization/intertwiner.
5. Admit the actual off-zero endpoint, then construct the Lorentzian closed
   domain and positive reduced pairing.
6. Only after nontrivial physical cohomology exists, test whether its linear
   structure represents superposition and whether interactions produce an
   observable coherence functional.

## Reproduction

```text
python3 tests/channel-swings/selected_k77_local_twistor_bach_detour_composition_gate_probe.py
```

passes `50/50` exact ownership, Layer-0, Clifford, projector, adapter,
spin-tractor curvature, Yang--Mills detour, twisting, Bach and operator-typing
controls.

## References

- A. R. Gover, P. Somberg and V. Soucek, [Yang--Mills detour complexes and
  conformal geometry](https://arxiv.org/abs/math/0606401), *Commun. Math.
  Phys.* 278 (2008), 307--327. The four-dimensional twistor-spinor detour
  sequence is a complex exactly on Bach-flat conformal spin backgrounds.
- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 2, Cambridge
  University Press, 1986, for local twistors and curvature integrability.
- `explorations/W202-signature-crux-bach-branch-2026-07-14.md`.
- `explorations/conditional-build/selected-k77-twistor-carrier-weyl-integrability-gate-2026-08-14.md`.
- `explorations/conditional-build/selected-k77-j10-bv-green-descent-gate-2026-08-13.md`.
