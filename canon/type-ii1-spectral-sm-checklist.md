---
title: "Type II_1 Spectral Standard Model Checklist"
status: canon
doc_type: canon
updated_at: "2026-06-23"
---

# Type II_1 Spectral Standard Model Checklist

This synthesis points to the Type II_1 / non-embeddable spectral Standard Model checklist now housed in [`../specifications/type-ii1-spectral-sm/`](../specifications/type-ii1-spectral-sm/).

The Type II_1 path remains the strongest mathematically adjacent substrate-class candidate identified by the ranking work. The public claim is deliberately modest:

> A Type II_1 or non-embeddable internal algebra extension is not constructed here. The repository now has an item-by-item control checklist describing what such a construction would have to preserve or replace from the finite Connes-Chamseddine spectral Standard Model.

## Public Artifacts

- [`../specifications/type-ii1-spectral-sm/connes-finite-control-checklist.md`](../specifications/type-ii1-spectral-sm/connes-finite-control-checklist.md)
- [`../specifications/type-ii1-spectral-sm/type-ii1-extension-requirements.md`](../specifications/type-ii1-spectral-sm/type-ii1-extension-requirements.md)

## Load-Bearing Questions

The first checklist pass isolates three high-value controls:

1. **KO-dimension 6 mod 8 in a Type II_1 / semifinite setting.** If no coherent analog exists, the path closes cleanly.
2. **Subfactor principal-graph data and generation count.** If principal graphs can explain three generations without smuggling in Standard Model representation content by hand, this would be a substantial positive signal.
3. **Freed-Hopkins compatibility after Connes-channel pairing.** The smooth observer-facing shadow must still land inside the ordinary anomaly-cancellation constraints.

## Current Verdict

The path is open, specialist-dependent, and high-upside, but the 2026-06-23 specialist pass narrows the target:

- KO-dimension 6 mod 8 is **not** a clean immediate no-go at the formal real-even sign-package level. It remains open as a Type II_1 finite-control selector.
- Subfactor principal graphs **fail** as a full SM representation source. They remain conditionally viable only as a generation-count selector.
- Freed-Hopkins compatibility remains downstream: it conditionally passes if the Connes-channel shadow is exactly ordinary anomaly-free SM content, and fails if extra Type II_1 modes survive in the smooth shadow with uncanceled anomaly.

See `../explorations/type-ii1-finite-control-specialist-pass-2026-06-23.md`.

## GU Contact Update (2026-06-23)

Two targeted GU-contact checks now make the current Type II_1 bridge more negative:

- **OQ1 real-structure pullback:** `s*(J_GU)^2` remains `-1`. Ordinary section pullback does not convert the GU quaternionic sign into the finite Connes KO-6 `J^2=+1` sign. A positive bridge would need an added twisted or newly defined real structure.
- **OQ2 inner fluctuations:** GU connection fluctuations preserve an already input `Sp(64)` connection orbit. They do not derive the finite Connes one-form bimodule or select `SU(3) x SU(2) x U(1)`.

These results do not close the abstract Type II_1 spectral-SM pathway, but they close the naive "GU section pullback supplies the CC finite-control data" route. See `../explorations/type-ii1-oq1-j2-section-pullback-2026-06-23.md` and `../explorations/type-ii1-oq2-dgu-inner-fluctuations-2026-06-23.md`.
