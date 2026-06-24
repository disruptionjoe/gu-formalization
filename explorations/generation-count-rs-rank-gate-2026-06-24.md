---
title: "Generation Count RS Rank Gate: OQ-RK1/OQ-RK2 Audit"
date: 2026-06-24
status: exploration
verdict: "OPEN: the generation count is not settled; the existing OQ-RK1/OQ-RK2 material does not contain a non-circular computation of rank_H(S_RS^+) or ind_H(D_RS)."
---

# Generation Count RS Rank Gate

## Verdict

The honest status remains OPEN. The spin-1/2 leg and the K3 topological input are the strong
parts of the current story: rank_H(S(6,4)) = 8 and A-hat(K3) = 2 give the compact-model
spin-1/2 contribution 16. The RS/spin-3/2 leg is still not computed.

Candidate A is:

```
rank_H(S_RS^+) = 4
ind_H(D_RS) = 2 * 4 = 8
ind_H(D_GU) = 16 + 8 = 24 = 3 generations
```

Candidate B is:

```
rank_H(S_RS^+) = 8
ind_H(D_RS) = 2 * 8 = 16
ind_H(D_GU) = 16 + 16 = 32 = 4 generations
```

Neither candidate has been eliminated by a derivation. Selecting Candidate A is still verdict
inflation unless OQ-RK1 or a direct RS index computation closes.

## Surfaces Read

I read the requested status surfaces and nearby gates: `RESEARCH-STATUS.md`,
`NEXT-STEPS.md`, `DERIVATION-PROGRESS.md` correction entries, and the 2026-06-23 exploration
files for generation-count rank-3 resolution, OQ-RK1 first-principles rank, OQ-RK1 CAS rank,
OQ-RK2 APS boundary, OQ-RK2 FC3/FC4 closure, and OQ-RK2 FC4 holonomy rank.

Local code audit: `rg --files` found no executable Sage/Mathematica/Python CAS implementation
for the RS rank gate. The only Python test surfaced was `tests/h3-cech-sheaf-fixture.py`,
which is unrelated to this computation. I therefore did not run a relevant CAS test.

## What Must Be Computed

The exact non-circular computation is not a bare rank of a prose-named projector. It is one
of the following two precise computations:

1. Direct index route: construct the constrained, gauge-fixed RS operator on K3, including its
   gamma-trace projector and any gauge/ghost subtraction needed for ellipticity, compute its
   principal symbol class in K-theory, and apply Atiyah-Singer/APS to get `ind_H(D_RS)` without
   using `ind_H(D_RS) = 8` as an input.

2. Effective-rank route: construct the actual effective coefficient object `E_RS^eff` whose
   Chern character enters
   `ind_H(D_RS) = integral_K3 A-hat(TK3) ch_H(E_RS^eff)`, then compute
   `rank_H(E_RS^eff)` and the degree-4 Chern correction from first principles.

A raw finite-dimensional Clifford rank will not by itself settle 4 vs 8. Existing files already
show several honest raw ranks:

```
rank_H(ker Gamma^{14D}|_{S^+}) = 448 - 32 = 416
rank_H(ker Gamma^{4D}|_{section, pre-gauge}) = 4 * 32 - 32 = 96
rank_H(S_RS^+(x)) via Spin(4) irreducible refinement = 24
post-gauge physical fiber counts in the notes give still other ranks
```

None of these is 4 or 8. The number 4 is an effective APS/index density, not the obvious
fiber rank of the vector-spinor constraint space. Therefore an executable gate must say how
the raw gamma-trace/gauge data becomes the symbol class or effective Chern character.

## Audit of Existing OQ-RK1/OQ-RK2 Material

OQ-RK1 first-principles rank is OPEN. Its surviving algebraic result is useful and exact:
`rank_H(ker Gamma^{14D}|_{S^+}) = 416`. Its attempted last step to
`rank_H(S_RS^+) = 4` is the retracted identity `8 / A-hat(K3) = 8 / 2 = 4`, so it assumes
the RS index value it is meant to derive.

OQ-RK1 CAS matrix rank is not an executed CAS result. It gives useful sanity checks
(`omega_9,5^2 = +1`, `rank_H(S^pm) = 32`, gamma-trace surjectivity), but its advertised
rank 4 comes from the APS identification `ind_H(D_RS)/A-hat(K3) = 8/2`. That is circular
for the present purpose. The file is best treated as a failed/speculative contract, not as
evidence for Candidate A.

OQ-RK2 APS boundary material contains executable-looking boundary structure: a projected
boundary operator `A_RS`, a Calderon projector, and a spectral-symmetry route to
`eta(A_RS)=0`. This is useful, especially the FC3 claim that the RS projector is compatible
with the chirality/orientation symmetry. But it does not determine the RS integer, because
the topological term still imports `rank_H(E_RS^eff)=4` from OQ-RK1/physical counting.

OQ-RK2 FC4 holonomy did not close the rank gate. Its correction note is decisive: the formulas
that hit 8 or 4 were chosen after other index attempts failed, and the file itself records that
the successful-looking formulas were not derived from SU(2) holonomy or an index theorem.

Bottom line: OQ-RK2 may be part of the final proof once the RS symbol/effective rank is known.
It does not currently distinguish Candidate A from Candidate B.

## CAS/Matrix Contract for a Future Worker

The next executable contract should be a small, explicit repository artifact, not another prose
rank reconstruction. It should have the following inputs.

Inputs:

- K3 invariants: `Ahat = 2`, `chi = 24`, `sigma = -16`, `p1[K3] = 3*sigma = -48`.
- Internal module: `F = S(6,4)` as a flat right-H bundle of rank 8, or else an explicit
  variable/integer for `ch_2(F)[K3]`. If this is not flat, the output must retain the
  `ch_2` dependence.
- Clifford data: explicit matrices for `Cl(4,0)` for the K3 computation, plus a consistent
  right-H structure or a complex model with a stated conversion rule from complex rank/index
  to H-rank/index. A full `Cl(9,5)` model can be included for consistency checks, but the K3
  RS index must be computed in the pulled-back 4D operator.
- Projectors: gamma-trace maps
  `G_+ : T*K3 tensor S_4^+ tensor F -> S_4^- tensor F` and
  `G_- : T*K3 tensor S_4^- tensor F -> S_4^+ tensor F`, with orthogonal projectors
  `P_+` and `P_-` onto their kernels.
- Gauge data: an explicit statement whether the computed object is the raw gamma-trace-free
  vector-spinor operator or the gauge-fixed physical RS complex. If gauge fixing is used,
  include the ghost/subtraction complex in the symbol class.

Required checks and outputs:

1. Verify Clifford relations exactly and print `sigma_4^2`, `omega_9,5^2`, and the H-ranks
   of `S^pm` as sanity checks.
2. Verify `P_+^2 = P_+`, `P_-^2 = P_-`, `G_+ P_+ = 0`, `G_- P_- = 0`, and report raw ranks.
   Expected sanity values may include 416, 96, or 24 depending on whether the model is full
   14D, 4D reducible, or Spin(4)-irreducible. Reporting 4 or 8 at this stage is a failure
   unless an additional effective-index map has been constructed.
3. Build the RS principal symbol
   `sigma_RS(xi) = P_- (c(xi) tensor 1_F) P_+`
   together with the stated gauge-fixing/ghost blocks. Check ellipticity: for symbolic
   `xi != 0`, or by an exact polynomial determinant/rank certificate, the gauge-fixed symbol
   is invertible in the appropriate quotient. If ellipticity fails, APS/Atiyah-Singer cannot
   be used as currently stated.
4. Compute the K-theory symbol class of the constrained/gauge-fixed operator and evaluate the
   topological index on K3:

```
index_C = AS_index(sigma_RS, K3, F)
index_H = index_C / 2        # only if the quaternionic structure is verified
rank_eff = index_H / Ahat    # only if the degree-4 Chern correction is zero or included
```

5. Decision rule:

```
index_H = 8   -> Candidate A survives: rank_eff = 4, 3-generation compact-model count.
index_H = 16  -> Candidate B survives: rank_eff = 8, 4-generation compact-model count.
other value   -> both A and B fail; update the generation count accordingly.
ch_2-dependent output -> rank gate remains OPEN until the actual Sp(64) background is fixed.
non-elliptic symbol -> APS route fails as stated.
```

Failure conditions for the contract:

- It uses `ind_H(D_RS)=8`, `rank_eff=4`, or the target generation count as an input rather
  than only as a comparison.
- It computes only a raw gamma-trace kernel rank and labels it the APS effective rank.
- It omits the gauge/ghost part while claiming to compute the physical constrained RS index.
- It assumes `ch_2(F)=0` without either proving flatness/triviality of the relevant bundle or
  carrying a correction term.
- It returns a value by choosing a normalization after seeing the target.

## Current Gate

The key next gate is therefore:

```
Compute the K3 RS constrained/gauge-fixed symbol class and its Atiyah-Singer index,
with all rank and Chern-character conventions printed.
```

This is stronger and cleaner than another `rank_H(Pi_RS * E_+)` note. If the repo still wants
the shorter OQ-RK1 name, the contract should redefine OQ-RK1 as this symbol-index computation,
or else explicitly define the effective projection whose rank is supposed to be 4 or 8.
