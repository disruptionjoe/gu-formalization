---
artifact_type: exploration
status: exploration
created: 2026-07-11
wave: 36
title: "H55 -- Positivity shape-collapse of the gravity beta/alpha band. Apply EFT positivity bounds (AADNR 2006) + the m2_eff window + the H49 survival constraint to the Wave-35 1-parameter shape family (r=beta/alpha, |II|^2 full-norm r=0 to conformal |II_0|^2 edge r=-1/4), and ask whether the band collapses to a point. VERDICT: NO-CONSTRAINT. The strong AADNR forward-positivity bound is BLIND here: GU's massive spin-2 is a KREIN ghost ([P,S]=0) and the source-action group Sp(32,32;H) is NON-COMPACT, so the dispersive spectral density is a SIGNED measure (eta_n=+-1) rather than positive, and c2 is sign-indefinite -- the massive-pole residue sign that would discriminate r enters with a compensating Krein sign. Physical-subspace positivity constrains only the massless-graviton mass (r>-1/4, the H49 survival edge), NOT the forward c2. Surviving band = (-1/4, 0], half-open, UNCHANGED from Wave 35: NOT collapsed to a point, NOT narrowed by positivity. No collapse manufactured."
grade: "COMPUTED (exact sympy + exact rational arithmetic): the Stelle two-pole TT symbol alpha*box*(box+m^2(r)) with m^2(r)=mstar2*(1+4r); the residues +-1/(alpha m^2(r)); the r=0 reproduction of the H45/H49 residues (+1/m2^2, -1/m2^2); the r->-1/4 Pais-Uhlenbeck Jordan degeneration (m^2->0, split coefficient diverges); the sign-indefiniteness of the Krein-signed two-pole dispersive sum (both signs achievable over non-negative spectral weights); the survival condition m^2(r)>0 <=> r>-1/4; the surviving-band arithmetic (-1/4,0], width 1/4>0 -> interval not point; the dim sp(64;H)=8256 rep anchor. ARGUED (structural / physics-reading tier): that the AADNR positive-density input is the ordinary-unitarity optical theorem and that Krein quantization replaces it with a signed measure (standard pseudo-unitary / indefinite-metric QFT, cited not re-derived); that physical-subspace positivity [P,S]=0 does not reach the forward-amplitude ghost channel; that non-compact Sp(32,32;H) admits no finite positive-definite invariant form; the map m^2(r) prop (1+4r) from the conformal decomposition |II_0|^2=|II|^2-(1/4)|H|^2; the theta=II_s structural upper edge r<=0 (H21/H45 P1). Reconstruction-tier, internal. No canon promotion; the shape residual stays OPEN as a FAMILY; SG4 unchanged; GU is neither killed nor forced by this bound."
depends_on:
  - tests/wave36/H55_positivity_shape_collapse.py
  - tests/wave35/source_action_carve.py
  - explorations/wave35/source-action-carve-2026-07-11.md
  - explorations/wave34/source-action-landscape-scan-2026-07-11.md
  - tests/wave24/H45_H2_vs_II2_binary.py
  - tests/wave28/H49_bach_weyl_sector.py
  - tests/wave6/H24_RY_normalization.py
  - tests/wave7/H25_II_first_variation_CRY.py
scripts:
  - tests/wave36/H55_positivity_shape_collapse.py
---

# Wave 36 -- H55: does EFT positivity collapse the gravity beta/alpha band?

Test: `tests/wave36/H55_positivity_shape_collapse.py` (deterministic, exact, exit 0, all PASS).

Wave 35 mapped GU's source action to a FAMILY whose only continuous shape freedom is the gravity ratio
`r = beta/alpha` of the two O(4)-invariant 4-derivative densities: `|II|^2` (full second-fundamental-form
norm, rank-10 on `Sym^2(R^4)`) and `|H|^2` (trace-square, rank-1). The family interpolates the conformal
edge `r = -1/4` (`|II_0|^2 = |II|^2 - (1/4)|H|^2`, H48, pure Bach, Einstein term absent) and the full-`|II|^2`
lean `r = 0` (H45, Stelle Einstein + Weyl). H49 showed this ratio is the survives-vs-forceable life-or-death
fork: `|II|^2` (Einstein term present) survives the rotation-curve + tree-ghost refutations; the pure
conformal `|II_0|^2` edge inherits Horne / Hobson-Lasenby as a kill and sits on the Pais-Uhlenbeck Jordan
boundary.

The H55 question: apply the standard EFT positivity bound (Adams-Arkani-Hamed-Dubovsky-Nicolis-Rattazzi
2006) plus the `m2_eff` window `[5/6, 5/4]` plus the H49 survival constraint, and ask whether the
1-parameter band collapses to a point. The Wave-34 caveat is load-bearing: GU's ghost is Krein-cleared
(`[P,S]=0`) and the group `Sp(32,32;H)` is non-compact, so the correct object is the **Krein-modified /
physical-subspace positivity**, not the naive bound.

## The four verdicts

### Q1 -- The propagator residues [COMPUTED, exact sympy]

The family density `alpha|II|^2 + beta|H|^2 = alpha(|II|^2 + r|H|^2)` gives, on the TT graviton, the Stelle
two-pole symbol

    P(s; r) = alpha * box * (box + m^2(r)),   m^2(r) = mstar2 * (1 + 4r),

where the Einstein (`box`, `s^1`) coefficient is proportional to `(1 + 4r)` because the conformally invariant
combination is the traceless `|II_0|^2 = |II|^2 - (1/4)|H|^2`: the Einstein term is present at the full norm
(`r = 0`) and vanishes at the conformal edge (`r = -1/4`). The Weyl/Bach (`box^2`, `s^2`) term is present for
all `r`. The propagator `1/P` has:

- **massless graviton** at `s = 0`, residue `+1/(alpha m^2(r))` (healthy);
- **massive spin-2** at `s = -m^2(r)`, residue `-1/(alpha m^2(r))` (the Krein ghost, opposite sign).

At `r = 0`, `alpha = 1` this reproduces the H45/H49 residues `(+1/m2^2, -1/m2^2)` exactly, with the scale
`mstar2 = m2_eff * mu_DW^2` and `m2_eff in [5/6, 5/4]` (H24/H25). As `r -> -1/4`, `m^2(-1/4) = 0`: the two
poles collide and the split coefficient `1/(alpha m^2)` diverges -- the Pais-Uhlenbeck Jordan degeneration
(H45 Q4), pure Bach `box^2`. **The sign of the massive-spin-2 residue is exactly the object a positivity
bound would probe to discriminate `r`.**

### Q2 -- AADNR positivity and its Krein modification [COMPUTED core + ARGUED applicability]

**The naive bound.** AADNR: for the low-energy `2->2` forward amplitude, analyticity + Froissart + ordinary
unitarity give `c2 = (1/2) d^2A/ds^2|_0 = (2/pi) int Im A(s')/s'^3 ds' >= 0`, because the optical theorem
makes `Im A(s') = s' sigma_tot(s') >= 0` -- a **positive** spectral density (a sum over intermediate states
with non-negative weights). A massive spin-2 exchange contributes with the sign of its propagator residue.
For the Stelle `|II|^2` branch the massive spin-2 is a **ghost** (residue `< 0`), so the naive bound would
be violated and would **exclude the whole `|II|^2` branch** -- which contradicts H49 (GU survives). That
contradiction is the tell that the naive bound is the wrong object for a Krein theory.

**The modification (stated explicitly).** GU clears the ghost by a **Krein quantization**: the physical inner
product is indefinite, with metric operator `P` (Cartan involution of `so(9,5)`), `[P,S] = 0` (Bateman-Turok
hidden-ghost parity; H23/H26; ledger item 4). The completeness relation becomes

    1 = sum_n eta_n |n><n|,   eta_n = <n|P|n> = +-1   (Krein signature),

so the amplitude discontinuity is a **signed** measure `Im A = sum_n eta_n rho_n`, `rho_n >= 0`. The massless
graviton carries `eta = +1`; the massive spin-2 -- the pole whose residue sign is the `r`-discriminant --
carries `eta = -1`. The dispersive integral `c2` is therefore **not** a sum of non-negative terms: it is
**sign-indefinite** (the test exhibits both signs over non-negative spectral weights). No sign-definite
condition on the residues, hence no sign-definite interval on `r`, follows from the strong bound.

**Physical-subspace positivity does not rescue it.** `[P,S] = 0` gives positivity on the `P`-positive
(physical) subspace, but the forward amplitude exchanges the `eta = -1` ghost in the intermediate channel;
the ghost pole is not in the physical subspace, so forward-`c2` positivity is not the physical-subspace inner
product. Physical-subspace positivity constrains only the **massless-pole residue** (`> 0`, a condition on
`m^2(r)`), not the forward `c2`.

**Non-compactness closes the escape.** Naive positivity's teeth come from a positive-definite invariant inner
product (a compact-group unitary rep). `Sp(32,32;H)` is non-compact (ledger item 3): it has no finite
positive-definite invariant form (only the indefinite Krein form is invariant), so there is no route to
restore the naive positive-density input. The strong bound is genuinely toothless here.

### Q3 -- The surviving band [COMPUTED]

- **The `m2_eff` window is a scale, not a ratio bound.** `m^2(r) = mstar2 (1 + 4r)` with
  `mstar2 = m2_eff mu_DW^2`, `m2_eff in [5/6, 5/4]` the H24/H25 method uncertainty at the physical config
  `r = 0`. It bounds the overall magnitude, not where `r` sits. It cannot collapse the band.
- **The H49 survival constraint** = keep the Einstein term = massless-graviton residue `> 0` = `m^2(r) > 0`
  `=> r > -1/4` (open conformal edge). This is the **weak** physical-subspace positivity (the massless pole
  healthy) / Stelle `m^2 != 0`, **not** the AADNR forward bound. At `r = -1/4` the theory dies (Jordan ghost
  + Horne / Hobson-Lasenby, H49).
- **The upper edge `r = 0`** (full `|II|^2`) is the `theta = II_s` structural lean (H21/H45 P1: the action
  norms the full `|theta|^2 = |II|^2`; `r > 0` would add a trace-square not sourced by `theta`). Structural,
  not positivity.

**Surviving band = `(-1/4, 0]`, half-open, width `1/4 > 0` -- an interval, not a point.** The strong AADNR
positivity neither narrowed nor collapsed it.

### Q4 -- Verdict: NO-CONSTRAINT [COMPUTED]

The strong AADNR positivity bound is **blind** here (Q2). On the question "does positivity collapse the shape
band", the honest answer is **NO-CONSTRAINT**. The band remains the Wave-35 half-open FAMILY `(-1/4, 0]`:
positivity did not move it. Life-or-death is decided by the **survival** constraint (exclude the conformal
edge), not by positivity.

## COMPUTED vs ARGUED ledger

- **COMPUTED (exact):** the Stelle two-pole symbol `alpha box(box+m^2(r))`, `m^2(r) = mstar2(1+4r)`; the
  residues `+-1/(alpha m^2(r))`; the `r = 0` reproduction of the H45/H49 residues `(+1/m2^2, -1/m2^2)`; the
  `r -> -1/4` Jordan degeneration (`m^2 -> 0`, split coefficient diverges); the sign-indefiniteness of the
  Krein-signed two-pole dispersive sum (both signs over non-negative weights); the survival condition
  `m^2(r) > 0 <=> r > -1/4`; the surviving-band arithmetic `(-1/4, 0]`, width `1/4 > 0`; the
  `dim sp(64;H) = 8256` rep anchor.
- **ARGUED (structural / physics-reading):** that the AADNR positive-density input is the ordinary-unitarity
  optical theorem and that Krein quantization replaces it with a signed measure (standard indefinite-metric
  QFT, cited); that physical-subspace positivity `[P,S] = 0` does not reach the forward-amplitude ghost
  channel; that non-compact `Sp(32,32;H)` admits no finite positive-definite invariant form; the map
  `m^2(r) prop (1 + 4r)` from the conformal decomposition `|II_0|^2 = |II|^2 - (1/4)|H|^2`; the `theta = II_s`
  structural upper edge `r <= 0`.

## Honest limits (what this bound does NOT do)

1. **The Krein modification is a genuine loss of teeth, not a disguised collapse.** The result is honestly
   NO-CONSTRAINT: the strong bound cannot carve `r` because the discriminating pole enters the dispersive
   integral with a compensating Krein sign. This is exactly the outcome Wave 34 flagged as possible ("the
   Krein modification may genuinely have no teeth for a non-compact group"); it was not manufactured either
   way.
2. **The `m^2(r) prop (1 + 4r)` map is the conformal-decomposition reading, not re-derived on the full
   bundle.** The endpoints (`r = 0` full `|II|^2`; `r = -1/4` conformal `|II_0|^2`, `m^2 = 0`) match H45/H48
   and the Wave-35 carve; the linear interpolation is the traceless-SFF decomposition, argued not recomputed
   here. Note this differs from H45's naive TT reduction (which assigned `|H|^2` no Einstein term); the
   conformal-edge endpoint is the physically load-bearing fact and it is convention-robust.
3. **The two-pole dispersive model is sign-faithful, not a full amplitude.** Q2b uses a narrow-pole
   Krein-signed spectral sum to establish sign-indefiniteness; it is not the full GU `2->2` forward
   amplitude (which is unbuilt). The conclusion "signed measure -> no sign-definite `c2`" is structural and
   does not depend on the amplitude's detailed form.
4. **The weak teeth are the SURVIVAL constraint, already held.** The open lower edge `r > -1/4` is the
   massless-graviton positivity = H49 survival = Stelle `m^2 != 0`; it is not new and it is not the AADNR
   forward bound. Positivity contributes no NEW teeth.
5. **No canon movement, no forcing, no kill.** The shape residual stays OPEN as a FAMILY `(-1/4, 0]`. SG4
   unchanged; the generation count untouched; GU is neither collapsed to a point nor killed by this bound.

## RE-RANK signal

**The Krein-modified EFT positivity bound is NO-CONSTRAINT on the gravity `beta/alpha` shape ratio. The band
is UNCHANGED from Wave 35: `(-1/4, 0]`, half-open, width `1/4` -- NOT collapsed to a point, NOT narrowed by
positivity.**

- **Does positivity collapse the shape residual?** No. The strong AADNR forward bound is blind for GU's
  non-compact `Sp(32,32;H)` Krein theory: the massive-spin-2 residue sign that would discriminate `r` enters
  the dispersive integral with a compensating Krein sign `eta = -1`, leaving `c2` sign-indefinite.
  **COLLAPSED-TO-POINT is falsified; NARROWED (by positivity) is falsified.**
- **Positivity-carving DROPS as a top lever for the shape ratio.** Wave 34 ranked "positivity /
  consistency-carving (Krein-modified)" as method #1 for the source action, with the caveat that the
  modification might remove the teeth. H55 computes that, for the `beta/alpha` shape direction, **the teeth
  are removed.** Positivity remains potentially useful elsewhere (e.g. bounding the cure-coupling coefficient
  in a built action), but it does not settle the gravity shape ratio.
- **Which physics decides the ratio?** The **survival** constraint (H49): the massless-graviton positivity /
  Stelle `m^2 != 0` excludes the conformal edge (`r > -1/4`, open), and the `theta = II_s` structure sets the
  upper edge (`r <= 0`). The `m2_eff` window is a scale, orthogonal to `r`. So the band is fixed by survival
  + structure, not by the analyticity/unitarity bound.
- **The single next object is unchanged:** build the source action (fix `mu_DW` / the scale). H55 removes one
  candidate shortcut (positivity does not close the shape residual) and confirms the residual is the same
  `|II|^2`-vs-`|II_0|^2` band Wave 35 mapped, gated on the same unbuilt object.
- **No canon promotion, no generation-count movement.** The shape residual stays OPEN as a FAMILY, honestly
  un-collapsed; the one-residual framing is unchanged, sharpened in one phrase: **EFT positivity is defanged
  by GU's Krein/non-compact structure on the gravity shape direction.**

---

*Filed 2026-07-11. Wave 36, H55 positivity shape-collapse. Reproducible:
`python -u tests/wave36/H55_positivity_shape_collapse.py` (exit 0, all PASS). Exploration-grade; not
promoted to canon. Adversarially graded: COLLAPSED-TO-POINT was tested for and falsified (the strong bound
is sign-indefinite under Krein), NARROWED-by-positivity was tested for and falsified (the only teeth are the
already-held survival constraint), and no collapse was manufactured. The honest outcome: NO-CONSTRAINT --
the Krein-modified positivity has no teeth for the non-compact `Sp(32,32;H)` theory, and the `beta/alpha`
band stays the Wave-35 half-open FAMILY `(-1/4, 0]`.*
