---
artifact_type: exploration
label: W234
created: 2026-07-15
status: exploration
posture: adversarial; truth-seeking; native-object first; construction-fork explicit; no verdict movement; does NOT decide the W235 record bit
title: "W234 condensate VEV isotropy gate: the good-branch mirror condensate Delta lands EXACTLY in the ~P Cartan-involution direction, so its stabilizer in Sp(32,32;H) is Sp(32)xSp(32) -- closing A1's dynamical residual CONDITIONAL on the record bit; and that very direction IS W231's channel-D chirality-killer, so closing A1 dynamically and preserving chirality are the SAME operator gated oppositely by the one W235 bit"
grade: "EXACT for the operator identity tau1(null) = sigma_3(definite) = P and the centralizer arithmetic (hyperbolic-rotation transform machine-verified; centralizer of the Cartan involution = maximal compact confirmed numerically in a faithful so(4,4) model and reproduced by exact 4160/4096 arithmetic for Sp(32,32;H)); STRUCTURAL for the lift of the 2x2-per-null-pair BdG condensate to the full arena VEV (same toy status as W216/W224); CONDITIONAL on the W235 record bit for whether the ~P condensate is an ALLOWED vacuum, and on the W216/W211 Krein-sign branch for the condensate being real (good branch); OPEN for the interacting source action, the physical state space, and the observable algebra. Machine regression: tests/W234_condensate_vev_isotropy_gate.py (35/35, exit 0, positive controls first). No canon, RESEARCH-STATUS, verdict, bar(b), H59, or generation-count change; the record bit is FLAGGED not decided."
depends_on:
  - explorations/W224-native-good-stable-dynamical-vacuum-2026-07-15.md
  - explorations/W216-true-vacuum-spectral-condensate-2026-07-14.md
  - explorations/W219-native-good-stable-stabilizer-input-gate-2026-07-14.md
  - explorations/W228-close-a1-corrected-sign-gu-instance-2026-07-14.md
  - explorations/W231-close-a3-smg-realization-gu-mirror-2026-07-14.md
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W234_condensate_vev_isotropy_gate.py
---

# W234 condensate VEV isotropy gate

## Result in one paragraph

W224 closed the dynamical good-stable gate with a negative -- the only unconditionally-built
vacuum (the record-count scale mode `p`) is an internal SINGLET, so it breaks 0 of the 4096
non-compact generators -- and named the ONLY arc candidate that could break the block: the
mirror-sector BCS condensate `Delta` (W216), the off-diagonal `tau1` pairing of the 96
hyperbolic null pairs of `ker(Gamma)` (W173). W224 asserted only that IF an adjoint
condensate `<O> ~ P` existed its centralizer WOULD be `Sp(32) x Sp(32)`, and left open
whether the built condensate equals that direction. W234 supplies exactly that step, as an
EXACT operator identity. A hyperbolic null pair `{u, v}` and the definite (`beta`-eigen) pair
`{e_+, e_-}` are related by the fixed 45-degree hyperbolic rotation
`u = (e_+ + e_-)/sqrt2`, `v = (e_+ - e_-)/sqrt2`. Under it the good-branch condensate operator
`Delta . tau1(null)` maps to `Delta . sigma_3(definite) = Delta . P`, with `P = diag(I_32, -I_32)
= beta` the Cartan involution. So the good-branch gap lands EXACTLY in the `~P` adjoint
direction, and its stabilizer in `Sp(32,32;H)` is the maximal compact `Sp(32) x Sp(32)`
(centralizer of the Cartan involution), breaking precisely the full 4096-generator
non-compact block. Conditional on the condensate being an allowed vacuum, W219/W228 kinematic
uniqueness becomes the DYNAMICAL answer: A1's dynamical residual closes. But the crux is the
reconciliation with W231: the SAME operator `tau1(null)` is Z2-ODD under the
generation(+)/mirror(-) grading `Z = tau3(null)` (`{tau1, tau3} = 0`), and W231's channel-D
Dirac mass is exactly that Z2-odd gen-mirror pairing. So "lands in `~P` (compactifies)" and
"is the channel-D chirality-killing direction" are the SAME operator statement, not two
objects. The record bit (W235, Joe-gated) therefore gates BOTH, one way, with OPPOSITE
desirability: record CONSERVED forbids the `~P` condensate (A1 does not close dynamically --
it reverts to the W224 singlet failure) but protects chirality; record BROKEN allows it (A1
closes, stabilizer `Sp(32) x Sp(32)`) but the same condensate kills chirality. Closing A1
dynamically and keeping the chiral generation are mutually exclusive through this one
condensate. bar(b), H59, and the count remain OPEN / unchanged; the W235 bit is not decided.

## 1. Construction fork (mandatory)

The load-bearing object is the CONDENSATE VEV as a Lie-algebra direction of the internal
arena, and it has the program's recurring Krein/native fork.

- **Standard-physics reading.** Treat the mirror gap as a BCS pairing amplitude in a Nambu
  doubling of a single mode and read its "direction" as a phase in a doubled particle-hole
  space; then the connection to an internal-symmetry adjoint VEV is obscured and one is
  tempted to import a maximal-compact breaking by fiat (the W224 physics-reading trap).
- **Program-native reading.** GU's condensate is NOT a Nambu doubling. It is the BCS pairing
  of a genuine hyperbolic NULL PAIR `{generation u, mirror v}` inside `ker(Gamma)` of
  `Cl(9,5) = M(64,H)` (W173: signature `(+96, -96, 0)`, the Krein form `K` the Cartan
  involution), acting on the actual quaternionic fiber `V` of the arena `Sp(32,32;H)`. The
  2x2-per-pair BdG block `H = xi tau3(null) + Delta tau1(null)` (W216, good branch) is a
  genuine operator on the 2-dim subspace `span{u, v} subset V`, so `Delta tau1(null)` is a
  bona fide adjoint direction of `Sp(32,32;H)`, and its isotropy is a well-posed centralizer.

**Which side, and why.** The answer lives on the native side and is decisive: because the
condensate acts on `V` itself (not a doubled space), the null-vs-definite basis relation is a
fixed rotation of `V`, and the "pairing direction" is literally a Cartan-involution direction
of the arena. Per the fork discipline the kill is checked in the other construction: in the
Nambu reading one would never see that `tau1(null) = P(definite)`, and would miss both the
closure of A1 AND its identity with channel D. The native reading exposes both at once.

## 2. The exact isotropy computation

### 2.1 The two bases of a null pair

On each of the 96 hyperbolic pairs, put the definite (`beta`-eigen) basis `{e_+, e_-}`
with `eta(e_+, e_+) = +1`, `eta(e_-, e_-) = -1`, and the null basis

```
u = (e_+ + e_-)/sqrt2,   v = (e_+ - e_-)/sqrt2,
```

so `eta(u,u) = eta(v,v) = 0`, `eta(u,v) = 1` -- the Krein Gram in `{u,v}` is the hyperbolic
`tau1` (machine check B2). The rotation `R` sending `{e_+, e_-} -> {u, v}` is orthogonal and
involutive (`R^2 = I`, B1).

### 2.2 The condensate direction (the new EXACT result)

W216's good-branch BdG block, in the null basis, is `H = xi tau3(null) + Delta tau1(null)`:
the kinetic `tau3(null) = diag(+1,-1)` distinguishes generation (`+xi`) from mirror (`-xi`),
and the pairing `tau1(null) = [[0,1],[1,0]]` is the off-diagonal generation<->mirror coupling.
Transform each null-basis operator to the definite basis by `M_def = R M_null R^{-1}`:

```
tau1(null)  ->  sigma_3(definite)  =  diag(+1, -1)  =  P          (condensate  -> DIAGONAL)
tau3(null)  ->  sigma_1(definite)  =  [[0,1],[1,0]]               (kinetic     -> off-diagonal)
tau2(null)  ->  off-diagonal (i.e. stays off-diagonal, ~ sigma_2)  (pathological direction)
```

(machine checks C1-C4.) The decisive line is the first: **the good-branch pairing
`Delta tau1(null)` equals `Delta P` in the definite basis** -- it is DIAGONAL, and it is
exactly the Cartan-involution `P = diag(I_32, -I_32) = beta` that W219/W228 identified as the
good-stable grading. Assembling the uniform-`Delta` condensate over the pairs that make up the
`(32, 32)` split reconstructs `P = diag(I_32, -I_32)` on the full fiber.

### 2.3 The stabilizer

The isotropy of the condensate VEV `<O> = Delta P` in `G = Sp(32,32;H)` is the centralizer

```
Stab_G(<O>) = Z_G(P) = { g in Sp(32,32;H) : g P g^{-1} = P } = Sp(32) x Sp(32),
```

because `P` is the Cartan involution whose fixed-point subgroup is the maximal compact. The
arithmetic is exact and matches W219/W224 to the generator:

```
dim_R Sp(32,32;H)        = 64(2*64+1) = 8256
dim_R [Sp(32) x Sp(32)]  = 2 * 32(2*32+1) = 4160
generators broken        = 8256 - 4160 = 4096 = 4 * 32 * 32   (the full non-compact block).
```

The centralizer-of-the-Cartan-involution-is-maximal-compact fact is confirmed numerically in a
faithful `so(4,4)` model (checks PC2, C7: `cent(P) = so(4)+so(4) = 12`, breaks the full coset
16), and the model is given teeth by two matched controls: a SINGLET condensate `~ I` has
centralizer the FULL group (breaks 0 -- the W224 case; PC1), and an off-diagonal boost (the
`i tau2` / pathological direction, which stays off-diagonal in the definite basis and mixes the
two factors) does NOT have the compact centralizer (PC3, `cent = 16 != 12`). Only the
`tau1 -> P` good-branch pairing compactifies.

### 2.4 Good branch vs pathological branch, geometrically

The good/pathological split of W216 maps cleanly onto compact/non-compact stabilizer. Good
branch: `Delta tau1(null) -> Delta P` DIAGONAL in the definite basis -> centralizer the
compact `Sp(32) x Sp(32)`. Pathological branch: `H = xi tau3 + i Delta tau2`, and
`i tau2(null)` stays OFF-diagonal in the definite basis (C3) -- it mixes the two `Sp(32)`
factors and does not reduce the arena to a compact-image subgroup. So the same reason the
pathological spectrum is complex (opposite-type Krein collision) is the reason the pathological
condensate does not compactify. This is the geometry, unconditional on the record bit.

## 3. Channel-D reconciliation (the crux, the coupling to W235)

W231 (lane A3) found that GU's own built condensate -- the BCS pairing of the null partners
`generation-xi <-> mirror--xi` -- structurally sits in "channel D", the gen-mirror Dirac
pairing `<16 . 16bar>`, which contains the `SO(10)` singlet and gives a SO(10)-symmetric
vectorlike Dirac mass that gaps the generation TOGETHER with the mirror: CHIRALITY-KILLING,
unless the Cartan-involution / ghost-parity `Z2` (generation `+`, mirror `-`) is a CONSERVED
record, which FORBIDS the Z2-odd Dirac mass.

The reconciliation is exact and it is an IDENTITY, not a tension:

- **Same operator.** The condensate is `Delta tau1(null)`. Its good-stable reading (Section 2)
  is `Delta P` (compactifies to `Sp(32) x Sp(32)`); its channel-D reading (W231) is the
  gen-mirror Dirac mass. These are the ONE operator `tau1(null)` in two bases/roles, not two
  objects (checks D1, D2). The very pairing that gives the good stabilizer IS the pairing that
  gaps the generation.

- **Z2-odd.** With the grading `Z = tau3(null)` (generation `+1`, mirror `-1`), `tau1(null)`
  anticommutes with `Z` (`{tau1, tau3} = 0`, D1), so the `~P` condensate is Z2-ODD: it connects
  the `+` and `-` sectors. This is exactly W231's statement that channel D carries one
  generation and one mirror.

- **One bit, opposite desirability.** The record bit (W235, = W173's operative-C /
  Y14-spectral-section datum, Joe-gated) decides whether `Z` is a conserved superselection
  charge. A conserved `Z` forbids every Z2-odd operator -- including `tau1 = P`. Hence:

  | record bit (W235) | `~P = tau1` condensate | A1 dynamical good stable | chirality |
  |---|---|---|---|
  | CONSERVED (record) | FORBIDDEN (Z2-odd) | NOT supplied -> reverts to W224 singlet failure | PROTECTED |
  | BROKEN (redundancy) | ALLOWED | CLOSES: stabilizer `Sp(32) x Sp(32)` | KILLED (channel D) |

  (checks D3-D8.) The two desirable outcomes -- closing A1 dynamically, and keeping the chiral
  generation -- are MUTUALLY EXCLUSIVE through this one condensate (D9): the same bit that lets
  the good stabilizer form is the bit that kills chirality, and the same bit that protects
  chirality forbids the good-stable VEV.

**So the swing W234 (close A1's dynamical residual) and the central-bit swing W235 are coupled
on a single operator.** W234 does not decide the bit; it shows precisely what the bit buys and
costs. If W235 reads "record conserved" (the W173/W231 lean), the ~P condensate is forbidden
and A1's dynamical good stable is NOT supplied by this object -- the W224 singlet input-failure
stands, and the good stabilizer remains kinematic-only (W219/W228). If W235 reads "record
broken", A1 closes dynamically with stabilizer `Sp(32) x Sp(32)`, at the price of the chiral
generation.

## 4. Verdict

```
CONDENSATE-VEV-ISOTROPY (good-branch mirror condensate Delta = tau1(null) of the 96 null pairs):
  condensate direction (definite basis) : Delta * P,  P = diag(I_32, -I_32) = beta  (EXACT)
  stabilizer in Sp(32,32;H)             : Z_G(P) = Sp(32) x Sp(32)   (dim 4160)
  generators broken                     : 4096  (the FULL non-compact block W224 required)
  => Delta LANDS IN THE ~P ADJOINT DIRECTION. A1's kinematic uniqueness (W219/W228) becomes the
     DYNAMICAL answer -- CONDITIONAL on the condensate being an allowed vacuum (the W235 bit).

CHANNEL-D RECONCILIATION (W231):
  "lands in ~P (compactifies)" and "is the channel-D chirality-killer" are the SAME operator
  (tau1(null) = P; Z2-odd). One record bit (W235) gates both, oppositely:
    record CONSERVED -> ~P forbidden -> A1 not closed (W224 singlet failure) BUT chirality protected;
    record BROKEN    -> ~P allowed   -> A1 closes (Sp(32)xSp(32))            BUT chirality killed.
  Closing A1 dynamically and preserving chirality are MUTUALLY EXCLUSIVE through this condensate.
  The W235 bit is NOT decided here (Joe-gated).
```

This does not claim GU has a dynamical good stable, nor that it kills chirality. It is the
narrower, computed result that the ONLY compactification-capable condensate GU builds lands
exactly in the good-stable `~P` direction, that its stabilizer is therefore `Sp(32) x Sp(32)`,
and that this is the very same operator W231 flagged as the chirality-killer -- so the
dynamical closure of A1 and the survival of chirality are one coupled question decided by the
single unbuilt record bit. bar(b), H59, and the generation count remain OPEN / unchanged.

## 5. Joe-gated items borne on but NOT moved

- **The W235 record / redundancy bit** (is the Cartan-involution `Z2` a conserved
  superselection charge?): this result COUPLES to it precisely and states the truth table, but
  does NOT decide it. FLAGGED, not moved. The verdict-level decision is Joe-gated / W235's.
- **The W216/W211 Krein-sign branch** (good vs pathological): taken as the good branch for the
  geometry (real `Delta`); not fixed here. It is logically distinct from the record bit, and I
  keep them separate per the guardrail.
- **H59 / bar(b)**: unchanged. This SHARPENS what H59 must build (a source action whose
  allowed condensate is the mirror-only channel S, not the gen-mirror `~P` channel D), exactly
  matching W231's stated `X`. No debit added or cleared.
- **Generation count / RESEARCH-STATUS / verdicts**: untouched.

## 6. Follow-up this unlocks

The result reduces the dynamical good-stable question and the chirality question to ONE object
with sharp content: the source action must, if it is to give BOTH a compact good-stable
stabilizer AND a chiral generation, condense the mirror-only `(16bar)^4` `SO(10)`-singlet
(channel S, W231) rather than the gen-mirror `~P` singlet (channel D, this note) -- and channel
S is a four-fermion operator that does NOT reduce to a single adjoint `~P` VEV, so its internal
isotropy is a genuinely different (and unbuilt) computation. The next bounded sub-goal is the
internal isotropy of a channel-S condensate: does a mirror-only quartic condensate reduce
`Sp(32,32;H)` to a compact-image subgroup WITHOUT being Z2-odd? If yes, GU could in principle
have both; if no, the mutual exclusion is structural. This is the Lean-portable core
(the operator identity `tau1(null) = P` and the centralizer are finite-dimensional and exact);
a Lean port is noted as follow-up only (no Lean/Lake run here).

## 7. Machine receipt

```
python -u tests/W234_condensate_vev_isotropy_gate.py
```

35/35 checks passed, exit 0. Positive controls run FIRST and each fires on a real falsifier,
including a genuine singlet / non-compactifying control (breaks 0, stabilizer the full group --
the detector cannot mistake a singlet for a compactification) and an off-diagonal boost control
(does not give the compact reduction). The actual checks then verify the hyperbolic-rotation
operator identity `tau1(null) = sigma_3(definite) = P`, the `Sp(32) x Sp(32)` stabilizer and
the 4096-generator break, the Z2-odd property, and the full channel-D / record-bit truth table.

## Governance

Exploration grade only. No canon, RESEARCH-STATUS, verdict, bar(b), H59, or generation-count
change. The W235 record bit is flagged and coupled, not decided. No cross-repository identity
asserted; the reservoir Krein sign and the Y14 spectral-section / record datum stay gated
temporal-issuance / time-as-finality objects. bar(b) and H59 remain OPEN. Zero em dashes.
