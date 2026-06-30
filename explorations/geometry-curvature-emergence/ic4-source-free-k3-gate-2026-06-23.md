---
title: "IC4 Source-Free K3 Metric-Selection Gate"
date: 2026-06-23
problem_label: "ic4-source-free-k3-gate"
status: exploration
verdict: CONDITIONALLY_SUPPORTED
depends_on:
  - explorations/geometry-curvature-emergence/ic4-ricci-flat-k3-selection-2026-06-23.md
  - explorations/geometry-curvature-emergence/ic4-lagrangian-tmunu-derivation-2026-06-23.md
  - explorations/geometry-curvature-emergence/pc2-gauss-y14-curvature-2026-06-23.md
  - explorations/geometry-curvature-emergence/rfail-umbilic-sections-2026-06-23.md
  - explorations/geometry-curvature-emergence/ic3-nonlinear-conservation-2026-06-23.md
  - explorations/geometry-curvature-emergence/ic2-positivity-soldering-normal-2026-06-23.md
  - explorations/geometry-curvature-emergence/ic2-cas-clifford-trace-verification-2026-06-23.md
  - explorations/generation-sector/oq3a-willmore-k3-selection-2026-06-23.md
  - explorations/generation-sector/oq3a-k3-variational-selection-2026-06-23.md
  - explorations/generation-sector/oq3a-gu-variational-k3-selection-2026-06-23.md
  - explorations/generation-sector/oq3a-t4-vs-k3-disambiguation-2026-06-23.md
---

# IC4 Source-Free K3 Metric-Selection Gate

## Verdict

**CONDITIONALLY_SUPPORTED, not verified.**

The existing notes support the following narrow implication:

```
generation/topology gate selects Ahat(X^4) = 2
+ K3/simply-connected spin hypotheses
+ IC4/PC2 gives source-free Einstein on the selected section
+ Lambda_eff = 0 in the trace equation
+ fixed complex structure and Kahler class
= K3-Yau metric representative
```

The existing notes do **not** prove that source-free Ricci-flatness alone selects K3.
The untracked T4/K3 note is decisive here: flat `T^4` is source-free, Ricci-flat, and
Willmore-minimizing by the LC section, but `Ahat(T^4) = 0`, so the 2+1 index formula
gives `ind_H(D_GU) = 8`, not `24`. K3 is separated from T4 by the generation-count
discriminant `Ahat(K3) = 2`, not by the source-free metric gate.

## Inputs Inspected

- `explorations/geometry-curvature-emergence/ic4-ricci-flat-k3-selection-2026-06-23.md`
- `explorations/geometry-curvature-emergence/ic4-lagrangian-tmunu-derivation-2026-06-23.md`
- `explorations/geometry-curvature-emergence/pc2-gauss-y14-curvature-2026-06-23.md`
- `explorations/geometry-curvature-emergence/rfail-umbilic-sections-2026-06-23.md`
- `explorations/geometry-curvature-emergence/ic3-nonlinear-conservation-2026-06-23.md`
- `explorations/geometry-curvature-emergence/ic2-positivity-soldering-normal-2026-06-23.md`
- `explorations/geometry-curvature-emergence/ic2-cas-clifford-trace-verification-2026-06-23.md`
- `explorations/generation-sector/oq3a-gu-variational-k3-selection-2026-06-23.md`
- `explorations/generation-sector/oq3a-k3-variational-selection-2026-06-23.md`
- `explorations/generation-sector/oq3a-willmore-k3-selection-2026-06-23.md`
- `explorations/generation-sector/oq3a-t4-vs-k3-disambiguation-2026-06-23.md` (existing untracked note)

## Resolved Subgates

| Subgate | Current status | What is genuinely settled |
|---|---:|---|
| Willmore-only selection | RESOLVED negative | `E[s_LC] = 0` for every LC section. Willmore energy alone does not select Ricci-flatness or K3. |
| T4 vs K3 discriminator | RESOLVED for the discriminator | T4 also has `E=0` and Ricci-flat metrics, but `Ahat(T4)=0`; K3 has `Ahat=2`. The metric gate must sit after the index/topology gate. |
| K3 Einstein implies Ricci-flat | PASS under compact K3 topology | Hitchin-Thorpe is saturated on K3, so any compact Einstein metric on K3 topology is Ricci-flat. A nonzero `Lambda_eff` obstructs the K3 vacuum instead of giving a non-Ricci-flat Einstein K3. |
| Yau-Calabi implication | PASS with fixed data | On a complex K3 surface, a fixed Kahler class has a unique Ricci-flat Kahler metric. This is theorem-grade once the complex structure and Kahler class are supplied. |
| IC2 trace-form positivity | CONDITIONALLY_RESOLVED | `B_fund(j_s n_i, j_s n_j) = 512 h_ij` and positivity on the 5 physical TT modes are structurally argued; explicit 64x64 quaternionic CAS and exact gauge-mode elimination remain proof gates. |
| IC3 nonlinear conservation | CONDITIONALLY_RESOLVED | The ambient Bianchi pullback gives the structural conservation identity through quadratic order. Torsion, `(6,4)` Weitzenboeck signs, and a shape-term coefficient remain gates. |
| IC4 Lagrangian match | CONDITIONALLY_RESOLVED | The GU stress tensor is matched to `Q^{TF}`, spinor stress, and ambient projection at reconstruction grade. `O(theta^3)` distortion and Shiab component checks remain. |
| `[G^Y_T]^{TF}` identification | CONDITIONALLY_RESOLVED | PC2 identifies `[G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF}` by Gauss/IC4 consistency. A moving-frame component CAS check is still needed. |
| `C_Gauss = 1` | CONDITIONALLY_RESOLVED | PC2 gives `C_Gauss=1` from pointwise Gauss/section-pullback normalization. A fiber-localization proof is still needed to exclude hidden noncompact-fiber factors. |

## Source-Free Section Hypotheses

The source-free K3 metric-selection gate is valid only under all of the following
hypotheses.

1. **Topology is already K3.** The index/topology chain must have selected the compact,
   smooth, simply-connected, spin `Ahat=2` class. This imports the OQ3 conditions:
   RS index `=8`, index additivity, and `ch_2(S(6,4))[K3]=0` or a computed correction
   compatible with `ind_H=24`.

2. **The selected section is tautological LC in the horizontal-normalized convention.**
   `theta = A - Gamma_LC = 0`, hence `B = II_s^H = 0` and `Q^{TF}(B)=0`.
   This also kills torsion-sourced hidden curvature pieces only if the GU connection
   being used is really the LC/torsion-free one on the selected section.

3. **No trace-free Yang-Mills or mixed flux survives.**
   The PC2 identification gives
   ```
   [G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF} + hidden/torsion corrections.
   ```
   Source-free K3 needs the right side to vanish, not merely be identified.

4. **No spinor anisotropic stress survives.**
   Either `Psi=0`, or the on-shell Dirac-DeRham, RS, and Shiab stresses have zero
   trace-free part on the selected section.

5. **Normal flux is trace-only and the trace equation gives `Lambda_eff=0`.**
   Normal curvature `F_ij` may contribute a pure metric term. On K3 this term must not
   force nonzero `Lambda_eff`; otherwise the K3 source-free Einstein gate fails.

6. **Torsion corrections cancel or vanish.**
   IC3 assumes torsion-free moving-frame Christoffels. If the GU connection has torsion
   with `T ~ B`, the torsion-Codazzi/Bianchi terms enter at `O(B^2)`. For the LC vacuum
   they should vanish, but that still needs an explicit torsion-free certificate for the
   selected section.

7. **Yau data are fixed.**
   Ricci-flat K3 gives a hyperkahler moduli family. A single K3-Yau representative
   requires GU to fix the complex structure, Kahler class, volume normalization, and
   any Euclidean-to-Lorentzian continuation convention.

## Remaining CAS / Proof Gates

1. **Moving-frame CAS for `[G^Y_T]^{TF}`.** Compute the independent components of
   `Riem^Y`, contract to `[G^Y_T]^{TF}`, and compare component-by-component with
   `T^{YM,TF} + T^{mix,TF}`. Include the `O(theta^2)` hidden curvature pieces
   `H^(1,2,3)` flagged in PC2.

2. **Fiber-localization proof for `C_Gauss=1`.** Show that the GU action localizes to
   `s(X^4)` by section pullback and does not require a regularized volume of
   `GL(4,R)/O(3,1)`.

3. **Torsion-Codazzi closure.** Verify that torsion-Bianchi terms either vanish on the
   source-free LC K3 section or cancel in the nonlinear conservation identity.

4. **Normal `(6,4)` Weitzenboeck sign.** Confirm that the indefinite normal-bundle
   signature does not flip the IC3 cancellation.

5. **IC4 higher-order distortion.** Compute the full `delta B / delta g` correction
   beyond the leading `O(theta^2)` stress, especially the `O(theta^3)` terms.

6. **Vacuum/source-free certificate.** Prove, rather than assume, that the selected K3
   section has `B=0`, `F_mu nu^{TF}=0`, `F_i mu^{TF}=0`, `Psi^{TF}=0`, no hidden
   trace-free curvature, and `Lambda_eff=0`.

7. **Index-side corrections.** Compute `ch_2(S(6,4))[K3]` and keep the OQ3b/OQ3c
   assumptions explicit. The T4/K3 discriminator is exact at the `Ahat` level, but
   the full `ind_H=24` chain still inherits those gates.

8. **Kahler/Yau selection data.** Specify the GU mechanism that fixes complex structure,
   Kahler class, and volume. Without it, the output is a Ricci-flat K3 moduli family.

## Failure Conditions

**F1: Willmore-only argument.** If the proof needs `E=0 => Ricci-flat => K3`, it fails.
Tautological LC sections give `E=0` on S4, T4, CP2, and K3.

**F2: Source-free Ricci-flatness used as a topology selector.** T4 is the counterexample:
it is Ricci-flat and Willmore-minimizing but has `Ahat=0`, hence wrong generation count.

**F3: Nonzero trace-free GU source.** Surviving YM, mixed-flux, spinor, Shiab, torsion,
or hidden-curvature trace-free terms yield Einstein-with-matter, not Ricci-flat K3.

**F4: Nonzero trace obstruction.** If the trace equation forces `Lambda_eff != 0`, the
compact K3 source-free Einstein gate fails.

**F5: PC2 component mismatch.** Extra terms in `[G^Y_T]^{TF}` beyond YM plus mixed flux
would add new anisotropic source terms.

**F6: `C_Gauss != 1`.** A nontrivial fiber-volume or localization factor changes the
Newton normalization and weakens the IC4 matching.

**F7: Torsion signs fail.** Non-cancelling torsion-Codazzi terms or a bad `(6,4)`
Weitzenboeck sign break IC3 conservation at the order needed for IC4 consistency.

**F8: Yau data not selected.** Ricci-flat K3 is not a unique metric until complex
structure and Kahler class are fixed.

**F9: Lorentzian transfer fails.** Yau-Calabi and Hitchin-Thorpe are Euclidean compact
statements. Any Lorentzian use must pass the APS/continuation gate separately.

## Concrete Next Action

Build one source-free K3 verification fixture with the following inputs:

```
X^4 = compact Euclidean K3 representative
A = Gamma_LC
theta = 0
B = II_s^H = 0
Psi = 0
F_mu nu^{TF} = 0
F_i mu^{TF} = 0
F_ij = trace-only, if present
fixed complex structure J and Kahler class [omega]
```

The fixture should certify, in this order:

```
Q^{TF}(B) = 0
torsion T = 0 and H^(1,2,3) = 0
[G^Y_T]^{TF} = 0
[E^Psi]^{TF} = 0
C_Gauss = 1
Lambda_eff = 0
```

If all six outputs pass, the IC4 source-free K3 gate upgrades from conditional support
to a proof-grade local certificate. If any output fails, the selection result remains
Einstein-with-source or trace-obstructed rather than K3-Yau.

## Minimal Supported Statement

The strongest supported statement today is:

> After the generation/topology chain has selected K3 rather than T4, and assuming the
> selected LC section is genuinely source-free in both trace-free and trace equations,
> IC4 plus PC2 reduce the GU field equation to source-free Einstein on compact K3 at
> reconstruction grade. Then Hitchin-Thorpe forces Ricci-flatness, and Yau-Calabi gives
> the Ricci-flat Kahler metric once complex structure and Kahler class are fixed.

This is a conditional metric-selection result, not a standalone Willmore theorem and
not a proof that source-free Ricci-flatness by itself selects K3.
