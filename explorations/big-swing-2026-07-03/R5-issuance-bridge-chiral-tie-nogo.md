---
title: "R5 big swing: the signed-readout / chiral-block-tie selector, BUILT and KILLED (with a stated reason)"
date: 2026-07-03
status: exploration
doc_type: crosswalk
verdict: kill-of-one-leg   # decisive KILL of the chiral-tie sub-lead; NO claim promotion; NO target import
lane: OBJ-TAF / LANE-ISSUANCE-BRIDGE (NEXT-STEPS)
re_open_candidate: "deflation-false-negative-audit-2026-07-03.md, item 1 (the GU-native shiab-selector residual)"
scripts:
  - tests/big-swing/R5_chiral_tie_nogo.py        # DECISIVE: invariant-Hom dims, no S+<->S- swap
  - tests/big-swing/R5_theta_signed_readout.py   # probe: the obvious GU antilinear maps preserve chirality
  - tests/big-swing/R5_crosscheck_bilinear.py    # INDEPENDENT re-derivation via invariant bilinears (matches MOVE-4)
imports: NONE (Spin(9,5)=Cl(9,5)=M(64,H) objects only; no TaF/TI repo internals; no target 3/8/24)
---

# R5 -- Firewall / issuance bridge: the decisive test, taken and settled

## The swing named

The OBJ-TAF deflation false-negative audit (2026-07-03, item 1) flagged exactly one live sub-lead
possibly buried by the lane-wide OBJ-TAF KILL: the **GU-native shiab-selector residual** -- the 3 free
coordinates (channel-mix / chiral-block-tie / scale) of GU's own 4-real-dim natural family
`Hom(Lambda^2 V (x) S, V (x) S)`, canon coords `(1,0,1,0)`. Of the crosswalk-proposed selectors
catalogued in `observer-selector-leftover-space-2026-06-26.md`, all but one were already run and dead
for canon (gamma-trace excludes canon; seesaw forces the Clifford-even `d_A*`; complex-closure empties
the family; PO1/forgetful kernel leg failed). The **one** candidate that touches an actual residual
coordinate but was left **UNBUILT** is the **"signed-readout -> chiral-sign tie"**: the proposal that
some structure forces `c_(-+) = eps * c_(+-)` between the two chiral blocks `S+->S-` and `S-->S+`.
The note's exact words: *"the crosswalk computes NO sign."*

This swing BUILDS that selector, GU-native, and settles it.

## What a "signed-readout tie" needs, made precise

GU canon ties the two blocks -- coords `(1, _, 1, _)` -- only because its shiab is literally **one**
Clifford-odd operator `c(iota_{e_a} alpha)` restricted to each chirality (`c` odd => it maps `S+->S-`
and `S-->S+` by the same formula). A general family element need not: the family basis treats the two
blocks as independent coordinates. So a selector fixes the tie **iff** it supplies a Spin(9,5)-INVARIANT
structure that carries one chiral block onto the other, i.e. a map that **swaps `S+ <-> S-`**. The sign
`eps` such a swap carries is the number the crosswalk never produced.

## Step 1 -- the obvious GU-native operator FAILS (probe)

`R5_theta_signed_readout.py`. The natural antilinear structures on the `Cl(9,5)=M(64,H)` spinor are the
quaternionic `J = U.conj` (forced by the signature) and its chirality twist `omega.J`. Computed:

| map | Spin-invariant antilinear? | `Theta^2` | chirality |
|---|---|---|---|
| `J = U.conj` | YES (defect 0.0e+00) | `-I` | **PRESERVES** (swap-err 1.0) |
| `omega.J` | YES (defect 0.0e+00) | `-I` | **PRESERVES** (swap-err 1.0) |

Both are Spin(9,5)-invariant antilinear reality structures, but both are **block-diagonal** (they act
inside `S+` and inside `S-` separately, because both `omega` and `J` commute with the whole Clifford
algebra). So the obvious "signed readout" operator cannot tie the blocks. My initial guess that `omega.J`
swaps chirality was FALSIFIED by the computation (`omega` is not purely imaginary under Jordan-Wigner);
reported honestly rather than patched.

## Step 2 -- the DECISIVE test: no invariant swap exists at all

`R5_chiral_tie_nogo.py`. Instead of guessing operators, compute the dimensions of the invariant
Hom-spaces directly from the verified representation (matrix-free Hermitian defect operator, smallest
eigenvalues by Lanczos; the 13 adjacent `Sigma_{i,i+1}` generate `so(14,C)`, re-verified on 8
non-adjacent insurance generators). Result (clean spectral gap: invariant directions `~1e-15`, next
eigenvalue `3.0`--`4.0`):

```
Hom_lin (S+, S+)  = 1     Hom_lin (S+, S-)  = 0   <-- linear swap
Hom_lin (S-, S-)  = 1
Hom_alin(S+, S+)  = 1     Hom_alin(S+, S-)  = 0   <-- antilinear swap
Hom_alin(S-, S-)  = 1
```

The **controls validate the method**: `Hom_lin(S+,S+)=1` is the Schur scalar; `Hom_alin(S+,S+)=1` is
exactly the quaternionic `J`. Both chirality-swap Homs -- linear AND antilinear -- are **0**.

**There is no Spin(9,5)-invariant (anti)linear map swapping `S+ <-> S-`.** The two chiral blocks live in
inequivalent, non-conjugate irreps (`conj(S+) ~= S+` via `J`, so `conj(S+) !~= S-`). Every invariant
single-spinor structure acts block-diagonally. Therefore **no GU-native invariant selector of
signed-readout type can impose `c_(-+) = eps * c_(+-)`**: the chiral-block-tie coordinate is invariantly
UNCONSTRAINABLE. Canon's tie is a WRITTEN choice, not something any spinor reality structure forces.

## Step 3 -- independent re-derivation (different object, matches the repo's own MOVE-4)

`R5_crosscheck_bilinear.py`. Re-derive the same conclusion from invariant BILINEAR forms `S (x) S -> C`
(a different invariant object, different constraint `Sigma^T C + C Sigma = 0`):

```
bilinear S+ x S+ = 0   (same-chirality / Majorana scalar)
bilinear S+ x S- = 1   (cross-chirality / charge conjugation)
bilinear S- x S- = 0
```

This reproduces canon MOVE-4 exactly ("the scalar bilinear exists only OFF-diagonally, on `S+<->S-`") --
a genuinely independent anchor. It shows `S+ ~= (S-)^*` (the two blocks are mutually **DUAL**, not
isomorphic), consistent with `Hom_lin(S+,S-)=0`. The one invariant relating the blocks is the dual
pairing; **using it on the shiab pairs the codomain `V`-slot too, i.e. introduces the metric
codifferential = the form-degree-shifting seesaw route already dead-for-canon (SHIAB-04).** So even the
sole block-relating invariant lands on a killed direction. No within-channel invariant tie exists.

## Honest outcome

**A decisive KILL of the signed-readout / chiral-tie leg, with a stated, computed, independently
cross-checked reason -- the KILL branch of the home-run.** Not a positive transport: no crosswalk object
imposes a real constraint on the chiral tie, because the required invariant swap provably does not exist.
This is *stronger* than the prior note (which said only "unbuilt / computes no sign"): it is now proven
that the sign is not merely uncomputed but **invariantly undefinable** by any single-spinor selector.

For the deflation audit's bookkeeping: on the chiral-tie leg the lane-wide OBJ-TAF KILL was **NOT a
false negative** -- the sub-lead is genuinely dead, now for a representation-theoretic reason rather than
by aggregation.

### Scope / what this does NOT do
- It closes **one** of the three residual coordinates (the chiral-block tie). The **channel-mix**
  (contract vs wedge) and **scale** coordinates are untouched here; prior work already showed channel-mix
  selectors either exclude canon (gamma-trace -> `wedge - 6*contract`) or are GU-native re-readings
  (metric-covariance), and scale is physically inert. The full 3-dim residual is not entirely closed by
  this note alone.
- No generation count. No target imported (never divided by / normalized to 3, 8, 24, chi(K3)).
- No canon/status edits; nothing promoted; cross-repo identity claims remain GATED (no TaF/TI internals
  were used -- only GU's own `omega`, `J`, and `Sigma_ab`).

### Executable certificates (all RUN, exit 0)
- `tests/big-swing/R5_chiral_tie_nogo.py` -- invariant-Hom dims; swap = 0 (lin & alin); controls pass.
- `tests/big-swing/R5_theta_signed_readout.py` -- `J`, `omega.J` Spin-invariant antilinear, chirality-preserving.
- `tests/big-swing/R5_crosscheck_bilinear.py` -- bilinears `0 / 1 / 0`; matches MOVE-4; `S+ ~= (S-)^*`.
