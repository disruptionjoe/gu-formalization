---
title: "Gimmel/DeWitt normalization ledger"
status: active_research
doc_type: exploration
ledger_kind: normalization
created: 2026-07-20
directed_by: "orchestrated normalization audit, 2026-07-20"
sources:
  - explorations/W131-covariant-operator-y14-2026-07-14.md
  - explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md
  - canon/w2-y14-spin-structure.md
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Gimmel/DeWitt normalization ledger

At `(x,g)`, write the vertical fiber as `W = Sym^2(T*_x X)` and

`G_lambda(S,T) = tr(g^{-1} S g^{-1} T) - lambda tr_g(S) tr_g(T)`.

The source-native GU trace reversal is

`R(S) = S - (1/2) tr_g(S) g`, hence `G_GU = G_{1/2}`.

The conventional DeWitt-style comparison used in some imported calculations is `G_DW = G_1` in
this same parameterization. It is a comparison convention, not a silent replacement for the native
GU normalization.

For the pure-trace direction `S=T=g` in dimension four,

- `G_GU(g,g) = 4 - 16(1/2) = -4`;
- `G_DW(g,g) = 4 - 16(1) = -12`.

The traceless block is independent of `lambda`. The pure-trace eigenvalue changes sign at
`lambda=1/4`; consequently every `lambda>1/4`, including `1/2` and `1`, has the same fiber
signature `(6,4)` on the Lorentzian locus.

## Typing and transfer rule

`lambda_GU=1/2` belongs to the third-person vertical metric on `T_gY_x`. Pullback along a
first-person observer section does not change it. Later `eta`, `K_S`, `C`, or `eta_+` metrics are
representation/readout structures; they may consume the vertical sign split but do not redefine
the source normalization.

| datum | transfer between `lambda=1/2` and `lambda=1` |
|---|---|
| sign split, negative count, `(6,4)` signature, associated fundamental-symmetry split | yes, for `lambda>1/4` |
| pure-trace norm, inverse trace factor, determinant/volume density, coordinate null cone | no silent transfer |
| connection, curvature, action coefficient, or measure derived from the metric | no silent transfer; recompute with `lambda_GU=1/2` for native GU claims |

This ledger repairs only explicit native fixtures in W168, W176, W202, and W209 from `lambda=1`,
`-12` to `lambda=1/2`, `-4`. Their signature-only conclusions and recorded verdicts are unchanged.
