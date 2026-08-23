---
title: "LT-GR8 D4: observed Hilbert-stress composition through the section"
status: active_research
doc_type: exact_typing_and_missing_owner_result
created: "2026-08-23"
registry: lab/process/selected-k77-ltgr8-observed-stress-composition-typing.json
probe: tests/channel-swings/selected_k77_ltgr8_observed_stress_composition_typing_probe.py
grade: "EXACT CODOMAIN CHECK PLUS FINITE HYPOTHETICAL TENSOR-PULLBACK TYPING; NO AMBIENT HILBERT INPUT, CAUSAL FLUX, HORIZON, ENTROPY, TEMPERATURE, STATE OR GU VERDICT CONSTRUCTED"
target_claim: "LT-GR8 demand D4 at typing grade; LT-GR8 remains NEEDS / MISSING_CONSTRUCTION"
canon_verdict_change: none
---

# LT-GR8 D4: observed Hilbert-stress composition through the section

> **GU-COMPARATOR-ROUTING — scope before inference.** The LT-GR8 target is a
> scoped external semiclassical-horizon benchmark. Jacobson's mechanism is not
> imported. Reverse-track compatibility is not GU confirmation, and no tensor
> contraction below is evidence for a physical horizon, entropy law or
> Einstein equation.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: the existing reconstruction-grade Hilbert stress is already an observed metric Euler covector, so composing it through s^* is ill-typed; only a hypothetical ambient undensitized symmetric two-tensor admits D^T T_Y D
carrier: s:X4->Y14 with ds_x:T_xX->T_s(x)Y and J_x=d(g_ab)_x; D=[I4;J] has rank four LAYER=ambient+observed BRIDGE=section-contraction CHIRALITY=N/A
pairing: the existing observed density-dual action pairing is owned; D^T T_Y D is separately tested only for a hypothetical undensitized ambient tensor ON=finite-section-jet witnesses
real_structure: real
grading: degree-zero tensor typing; the fourteen-density and four-density are different line bundles
action_owner: repository-construction -- the common action owns T_H in the observed metric/coframe Euler dual; no ambient Hilbert tensor is owned as an input to s^*
target: LT-GR8 D4 existing stress composition ill-typed; hypothetical ambient tensor contraction typed and causal flux missing MAP-TYPE=contraction
```

## Result first

The phrase “compose the native Hilbert stress through `s^*`” first fails a
codomain check. The stress constructed on 2026-08-05 is

\[
T_H(g,\psi)=E_g^{\rm matter}(g,\psi)\in B_X^!,
\]

the density-dual of the **observed** rank-ten metric/coframe variation. Its
density/Krein primalizers and matter-shell Ward conservation are already owned
at that artifact's reconstruction ceiling. It is not an ambient tensor in
`Sym^2(T^*Y)` and cannot be fed to `s^*:\Omega^1(Y)\to\Omega^1(X)` (or its
covariant-tensor extension) a second time. No inverse observation or canonical
lift exists. D4 therefore resolves as an exact type correction:

1. **Existing native/common-action `T_H` — ALREADY OBSERVED.** Its codomain is
   the observed metric Euler dual `B_X^!`. “Pull back `T_H` through `s^*`” is
   ill-typed and would double-apply observation. This preserves, rather than
   erases, the 2026-08-05 result: symmetric action-owned stress and its
   matter-shell Ward conservation remain exact at their recorded observed
   flat-control/reconstruction scope.

2. **Hypothetical ambient algebraic tensor contraction — TYPED BUT UNOWNED.**
   If a future action supplies an undensitized ambient symmetric covariant
   two-tensor `T_Y`, then

   \[
   C_s(T_Y)=s^*T_Y=(ds)^T T_Y(ds),\qquad
   (C_sT)_{\mu\nu}=T_{AB}(s(x))D^A{}_\mu D^B{}_\nu . \tag{D4.1}
   \]

   is a symmetric covariant two-tensor on `X`. With the MD-1 section jet
   `D=[I_4;J]`, it is a contraction, not horizontal projection. The map
   `Sym^2(T^*Y)->Sym^2(T^*X)` is surjective, has rank `10`, and has kernel
   dimension `105-10=95` at every section jet because `D` has rank four. But
   the LT-GR8 packet owns no such ambient Hilbert input; this conditional map
   does not replace or further compose the already-observed `T_H`.

3. **Ambient-to-observed stress density — MISSING FOR THE HYPOTHETICAL ROUTE.**
   `D^T T_Y D` contracts tensor legs but does
   not turn a fourteen-dimensional density line into a four-dimensional one.
   A rectangular `14 x 4` derivative has no determinant supplying this
   conversion. Equivalently, the pullback of a fourteen-form to `X^4` is zero;
   a nonzero reduction needs a transverse density, fibre integration, delta
   current, or an independently declared observed action. None is currently
   owned for an ambient LT-GR8 stress route. This is not a defect in the
   already-observed common-action `T_H`, whose observed density dual is owned.

4. **Variation of a future ambient action after observation — MISSING CHAIN.**
   The observation
   section is the metric, `s_g(x)=(x,g_{ab}(x))`. Varying `g` therefore varies
   both the ambient fields and the map used to observe them. A physical
   observed Euler covector derived from a future ambient action would need a
   defined reduction and
   and contains the section-chain term

   \[
   D_g(S_Y\circ s_g)[h]
   =D_bS_Y[\delta b(h)]+D_sS_Y[D_gs_g(h)]
   +D_{\rho_X}S_X[\delta\rho_X(h)]. \tag{D4.2}
   \]

   The bare tensor contraction (D4.1) supplies none of the last two terms.
   The exact scalar control `A(g,s)=gs`, `s(g)=g` gives direct derivative `1`
   but total derivative `2` at `g=1`, so silently dropping the section chain
   is detectably wrong.

5. **Conservation of a hypothetical pullback — NOT INHERITED.** Even if a
   future ambient stress is
   symmetric and ambient-divergence-free on its complete shell, a pullback
   need not be divergence-free on the induced geometry. For the curve
   `s(x)=(x,x^2)` in flat `R^2` and constant ambient
   `T=diag(0,1)`, ambient divergence is zero but
   `s^*T=4x^2 dx^2`. At `x=1`, with induced metric `g=1+4x^2`,
   `nabla_x(s^*T)_{xx}=8/5`, hence the raised divergence is `8/25`, not zero.
   The missing terms are precisely the normal/extrinsic response and the
   complete observed action Ward identity. This counterexample does not undo
   the independent observed matter-shell Ward theorem already proved for
   `T_H`; it blocks reusing ambient conservation as a substitute.

6. **Rindler energy flux — MISSING PHYSICAL DATA.** The frozen reverse packet
   defines the target flux as `delta Q = integral_H T_ab chi^a dSigma^b`.
   Forming it additionally requires an instantiated observed causal boundary,
   its post-observation orientation, a boost vector `chi`, boundary measure,
   complete shell and integrability/domain data. The T-4 certificate proves
   that causal orientation has no metric-only ambient default. No such data is
   constructed here.

Thus D4 is **executed and closed at typing grade**, but its scientific
disposition is a codomain correction, not a new stress construction:

```text
existing reconstruction-grade T_H in observed B_X^!
  -> compose again through s^*: ILL-TYPED / NO INVERSE OBSERVATION
hypothetical ambient undensitized T_Y
  -> symmetric-tensor contraction D^T T_Y D: EXACT CONDITIONAL MAP
  -> ambient-to-observed 4-density: MISSING REDUCTION OWNER
  -> total observed variation: MISSING SECTION CHAIN FOR THIS ROUTE
  -> conservation: NOT INHERITED FROM AMBIENT DIVERGENCE
  -> Rindler flux: MISSING D5 ORIENTATION/BOUNDARY/FLOW DATA
```

LT-GR8 remains `NEEDS / MISSING_CONSTRUCTION`. The prior packet's
`stress_energy_flux` component refines from “observed composition untyped” to
“existing stress already observed; re-pullback ill-typed; hypothetical ambient
tensor contraction typed; causal flux missing.”

## Layer 0

| phrase | exact object here | kept distinct from |
|---|---|---|
| native/common-action Hilbert stress | observed density-valued metric/coframe Euler covector `T_H in B_X^!` | ambient `Y14` tensor |
| tensor pullback | `D^T T_Y D` on a hypothetical ambient tensor's two covariant legs | the already-observed `T_H`, density reduction or action variation |
| observation contraction | `D=[I;J]`, including vertical legs through `J` | horizontal projection |
| observed Hilbert Euler map | the existing common-action `T_H`, reconstructed by radial transgression | a second pullback operation |
| conservation | existing matter-shell Ward identity for `T_H` | conservation of a hypothetical ambient pullback |
| stress-energy flux | boundary integral using `chi` and `dSigma` | a local symmetric two-tensor |

The first row preserves the 2026-08-05 radial-transgression theorem. Its
observed density and matter-shell Ward identity remain owned at the recorded
scope. What remains absent is an ambient Hilbert input to `s^*` and the causal
boundary/orientation/flow data needed to turn `T_H` into LT-GR8's Rindler flux.

## Exact finite certificate

At a point, write the section derivative as the full-column-rank matrix

\[
D=\begin{bmatrix}I_4\\J_{10\times4}\end{bmatrix}.
\]

The probe uses a nonzero rational `J`, constructs a general symmetric
`14 x 14` tensor, and verifies:

- `D^T T D` is symmetric;
- vertical and mixed tensor blocks contribute whenever `J` is nonzero;
- horizontal projection disagrees with contraction on an explicit witness;
- the pullback map is onto `Sym^2(R^4)^*` by the horizontal embedding;
- its exact matrix rank is `10`, hence kernel dimension `95`;
- a planted tensor in the kernel is nonzero but pulls back to zero;
- for the hypothetical ambient route, the density dimensions are `14` and
  `4`, and the rectangular `D` has no determinant;
- the section-chain scalar control gives direct `1` versus total `2`;
- the curved-section conservation counterexample gives exactly `8/25`.

The negative controls fire if a future summary feeds the already-observed
`T_H` into `s^*`, promotes contraction to projection or injectivity, invents
an ambient density pullback, imports conservation, or claims horizon, flux or
confirmation credit.

## Source-to-proof delta and lens census

No new source claim is introduced. The source/repository inputs are:

- WG-B06 / MD-1: observation is contraction along a section, not projection;
- the 2026-08-05 action construction: the radial-transgression Hilbert Euler
  map is action-owned at reconstruction grade and distinct from literal `VU`;
- the 2026-08-22 T-4 certificate: causal orientation is post-observation-only;
- the 2026-08-23 reverse descent: D4 is the next typed demand and the target
  Rindler flux is frozen without claiming a realization.

The new proof content is the observed-codomain correction, plus the exact
conditional `10/95` rank/kernel certificate, density-dimension obstruction,
section-chain control and conservation counterexample for any future ambient
route. Inline lenses covered bundle geometry,
variational calculus, tensor densities, submanifold geometry, Ward identities,
causal-boundary physics, exact linear algebra, source fidelity, comparator
routing and hostile claim-ceiling review.

The hostile pass tested the strongest contrary reading: “Hilbert stress is a
tensor, so pull it back and the job is done.” It first fails because the
repository's `T_H` is already observed. Replacing it with a hypothetical
ambient undensitized tensor makes `D^T T_Y D` legal, but then density, total
variation and conservation still remain separate before causal flux is asked
for.

## Disposition and next gate

- D4: `TYPING_COMPLETE__EXISTING_T_H_ALREADY_OBSERVED__REPULLBACK_ILL_TYPED__HYPOTHETICAL_AMBIENT_CONTRACTION_EXACT__CAUSAL_FLUX_MISSING`.
- Ledger verdict, source ownership, mechanism commitment, confirmation credit,
  canon and public posture: unchanged.
- D5: not executable from current metric-only data; it requires genuinely new
  source/action-owned post-observation orientation and boundary-flow data.
- Next compatible reverse-track work: freeze D6's held-out consequence at
  packet grade before any future target-facing comparison, while D1--D3 and D5
  retain their named missing-owner predicates.

A deferred conditional-evidence delta records the row-distance refinement so
that no new ledger version is minted solely to restate an unchanged verdict.
