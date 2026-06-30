---
title: "IC4 Ricci-Flat/K3 Metric-Selection Proof Gate"
status: exploration
doc_type: research_note
updated_at: "2026-06-23"
problem_label: "ic4-ricci-flat-k3-selection"
verdict: "CONDITIONALLY_SUPPORTED"
---

# IC4 Ricci-Flat/K3 Metric-Selection Proof Gate

## 1. Question

The latest OQ3a Willmore note changes the metric-selection problem. The Willmore
energy alone does not select Ricci-flat metrics:

```
E[s_LC] = integral |II_s^H|^2 = 0
```

for every tautological Levi-Civita section, regardless of whether the metric is
Ricci-flat. Thus the proof gate is:

> Does IC4 reduce the GU section field equation, within the K3 topological class,
> to the source-free Einstein equation, so that K3 topology forces Ricci-flatness
> and Yau-Calabi then supplies the preferred K3 metric?

This note does not reopen the topological factor-of-2 argument. It tests the
metric-selection step after the K3 class has already been selected by the
generation-count/Rokhlin chain.

## 2. Inputs Inspected

- `explorations/generation-sector/oq3a-willmore-k3-selection-2026-06-23.md`
- `explorations/generation-sector/oq3a-k3-variational-selection-2026-06-23.md`
- `explorations/generation-sector/oq3a-gu-variational-k3-selection-2026-06-23.md`
- `explorations/geometry-curvature-emergence/ic4-lagrangian-tmunu-derivation-2026-06-23.md`
- `explorations/geometry-curvature-emergence/pc2-gauss-y14-curvature-2026-06-23.md`
- `explorations/geometry-curvature-emergence/ic3-nonlinear-conservation-2026-06-23.md`
- `explorations/geometry-curvature-emergence/ic2-positivity-soldering-normal-2026-06-23.md`
- `explorations/geometry-curvature-emergence/codazzi-sp64-2026-06-23.md`
- `explorations/geometry-curvature-emergence/codazzi-general-non-umbilic-2026-06-23.md`
- `explorations/geometry-curvature-emergence/rfail-umbilic-sections-2026-06-23.md`
- `explorations/geometry-curvature-emergence/pc2-gauss-y14-curvature-2026-06-23.md`

## 3. Verdict

**K3-Yau metric selection is conditionally supported, not proved outright.**

The supported chain is narrower than older OQ3a wording:

```
ind_H = 24 + Rokhlin/split assumptions
  => Ahat(X^4) = 2
  => K3-type topology
  => IC4 source-free Einstein equation on the selected section
  => Einstein metric on K3
  => Ricci-flat by Hitchin-Thorpe equality for K3
  => Yau metric, once a complex structure and Kahler class are fixed
```

What fails is the stronger claim:

```
E[s] = 0  =>  Ricci-flat  =>  K3
```

That implication is false because every LC section has `E = 0`, including round
`S^4` and Fubini-Study `CP^2`, which are not Ricci-flat.

## 4. Gate Results

### Gate A: Willmore-alone metric selection

**Status: FAILS.**

The latest Willmore note is decisive: `E = 0` is flat across LC sections. It is
not a Ricci-flatness test and cannot distinguish K3-Yau from non-Ricci-flat
LC sections.

This means the proof must not use "minimum Willmore energy" as the metric selector
unless extra field-equation constraints are imposed.

### Gate B: K3 topology already fixed

**Status: CONDITIONAL PASS.**

K3 topology is supported only under the separate topological/index assumptions:

- `X^4` is compact, oriented, spin, and in the simply-connected/K3-type regime.
- The generation split is correct:
  ```
  ind_H(D_GU) = 8 * Ahat(X^4) + 8
  ```
- The RS block contributes `8`.
- The spin-1/2 and RS blocks are index-additive.
- The `ch_2(S(6,4))[K3]` correction is zero or cancels consistently.

Under those assumptions, `ind_H = 24` forces `Ahat = 2`; Rokhlin makes this
the first nonzero allowed spin value; this identifies the K3-type class. This
is topology, not Willmore dynamics.

### Gate C: IC4 reduces GU to the Einstein equation

**Status: CONDITIONAL PASS at reconstruction grade.**

IC4 derives the on-shell 4D stress tensor from the GU Lagrangian and matches it
to the Codazzi trace-free Einstein identification:

```
G^X_{mu nu} = 8 pi G T^GU_{mu nu}
```

with the trace equation fixing the effective cosmological term. PC2 further
closes the two IC4 sub-gates at reconstruction grade:

- `C_Gauss = 1`
- `[G^Y_T]^{TF} = T^{YM,TF} + T^{mix,TF}`

Residual gates remain:

- component-level CAS verification of `[G^Y_T]^{TF}`;
- fiber-localization proof for `C_Gauss = 1`;
- torsion corrections in IC3;
- Weitzenboeck sign in the `(6,4)` normal bundle;
- `O(theta^3)` distortion corrections in IC4;
- IC2 physical-mode positivity and gauge elimination of negative normal modes.

Thus IC4 supports the Einstein-equation reduction only conditionally.

### Gate D: Source-free/vacuum section

**Status: CONDITIONAL PASS.**

To use IC4 for metric selection, the selected K3 section must be source-free in
the trace-free equation:

```
T^{GU,TF}_{mu nu} = 0.
```

Sufficient conditions are:

- LC/tautological section in the horizontal-normalized convention, so `B = II_s^H = 0`;
- no spinor stress: `E^{Psi,TF} = 0`;
- no YM or mixed-flux anisotropic stress: `T^{YM,TF} = T^{mix,TF} = 0`;
- no surviving hidden-curvature trace-free correction.

If these fail, IC4 gives Einstein-with-matter, not Ricci-flat selection.

### Gate E: Einstein on K3 implies Ricci-flat

**Status: PASS, assuming compact smooth K3 topology.**

For K3:

```
chi(K3) = 24,   sigma(K3) = -16,
2 chi = 48 = 3 |sigma|.
```

The Hitchin-Thorpe inequality for compact Einstein 4-manifolds is saturated.
Equality forces the scalar curvature term to vanish, so any Einstein metric on
K3 topology is Ricci-flat. Therefore, if IC4 really reduces the selected K3
section to a source-free Einstein equation, the metric is Ricci-flat. A nonzero
effective cosmological constant would not give a non-Ricci-flat K3 solution; it
would instead obstruct the K3 vacuum gate.

### Gate F: Ricci-flat K3 gives Yau metric

**Status: CONDITIONAL PASS.**

Yau-Calabi gives a unique Ricci-flat Kahler metric in each fixed Kahler class on
a complex K3 surface. Therefore IC4 plus K3 plus Kahler data supports the
K3-Yau metric.

This is not a single globally unique metric unless GU separately fixes:

- the complex structure;
- the Kahler class;
- the normalization/volume;
- the Lorentzian continuation or Euclidean compactification convention.

Without those, the selection is a Ricci-flat hyperkahler moduli family, not a
single point.

## 5. Minimal Valid Selection Statement

The strongest statement supported by the current notes is:

> Assuming the topological/index chain has already fixed the K3-type class, and
> assuming IC4's on-shell Einstein-equation reduction holds with no trace-free
> GU source on the selected LC section, the selected metric on compact K3 must
> be Ricci-flat. If GU also fixes a complex structure and Kahler class, Yau-Calabi
> identifies the corresponding Ricci-flat Kahler metric as the preferred K3-Yau
> representative.

This is a conditional metric-selection result, not a standalone Willmore theorem.

## 6. Failure Conditions

**F1: Willmore-only selector.** If the argument needs `E = 0` alone to imply
Ricci-flatness, the selection fails. Round `S^4` and Fubini-Study `CP^2` already
give counterexamples via LC sections.

**F2: IC4 does not reduce to Einstein.** If the IC4 Lagrangian stress tensor does
not match the Codazzi equation after component verification, the field-equation
selector is lost.

**F3: Nonzero trace-free GU source.** If YM, mixed-flux, spinor, hidden-curvature,
or non-LC distortion terms survive, IC4 selects an Einstein-with-matter solution,
not a Ricci-flat K3 metric.

**F4: Effective Lambda obstruction.** On K3, a source-free Einstein solution must
be Ricci-flat. If the GU trace equation forces nonzero `Lambda_eff`, the K3 vacuum
section fails rather than becoming non-Ricci-flat.

**F5: K3 topology not actually forced.** If the index split, RS `+8`, additivity,
Rokhlin assumptions, or `ch_2` flat-bundle gate fail, the argument does not reach
the K3 class.

**F6: Yau data not fixed.** If GU does not fix complex structure and Kahler class,
the output is a Ricci-flat K3 moduli family, not a unique metric.

**F7: Lorentzian continuation.** The Yau-Calabi theorem is Euclidean/Kahler. A
Lorentzian K3-fibered or Euclidean-continuation model needs the APS/Lorentzian
continuation gate to transfer the selection to the physical spacetime setting.

## 7. Final Answer

**Selection status: CONDITIONAL.**

K3-Yau selection is supported only after replacing the Willmore-only claim with
the IC4 field-equation claim. The latest Willmore note correctly blocks the
standalone argument. The viable proof gate is:

```
topology/index fixes K3
+ IC4 gives source-free Einstein on the selected LC section
+ Hitchin-Thorpe on K3
+ Yau-Calabi with fixed Kahler data
= conditional K3-Yau metric selection
```

The next proof-critical upgrade is not another Willmore inequality. It is a
component-level IC4/PC2 verification plus the vacuum/trace gate showing that the
selected K3 section has no trace-free GU source and no nonzero effective
cosmological obstruction.
