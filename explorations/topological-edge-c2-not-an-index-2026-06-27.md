---
title: "The topological edge: ch2(S_X)[K3] = -5376 (not 24), eta = 0, and C2 is NOT an index — the 'convergence' is a forced analogy"
date: 2026-06-27
status: exploration
doc_type: exploration
verdict: speculation   # honest negative at the edge; CORRECTS the SOURCE-03 convergence over-claim. NO claim promoted.
method: "Design -> Build -> adversarial Kill over 3 approaches (ch2 from Codazzi, APS eta for the real operator, the C2<->index connection audit); all genuine=True, target-import clean, reproduced; load-bearing facts independently re-derived in the main loop"
builds_on:
  - explorations/c2-is-global-y14-end-data-2026-06-27.md  (SOURCE-03)
  - active-research/topological-generation-count-families-k3-chi-gate-2026-06-26.md
corrects: "SOURCE-03's inference that C2 = the boundary index = one global object (it is a FORCED ANALOGY)"
bears_on: "the generation count (OPEN; this route does not close it) + the precise edge of GU's reconstruction"
---

# The topological edge — and a correction to SOURCE-03

This gate ran the repo's own required computation (`S_XCharacteristicClassPacket_V0`) to test whether the
GLOBAL Y14 object supplies the ~94% of C2 the local curvature could not. **It does not, the topological route
does not close the generation count, and — the most important finding — the "grand convergence" SOURCE-03
inferred (that C2 and the boundary index are one global object) is a FORCED ANALOGY.** This is the discipline
catching a seductive convergence in the program's own (and this author's own) prior narration.

## 1. The computable global objects — honest numbers, not 24

Both genuinely-computable global objects were built from a-priori in-repo data (no target import, no blocked
shortcut; all `genuine=True`, reproduced on re-run):

- **ch2(S_X)[K3] = -5376.** The pulled-back spinor connection `s*A^0` on `S_X = s*S` is NON-flat on the
  source-free LC/K3 branch (K3 is Ricci-flat but not flat; holonomy SU(2)). Via Chern-Weil with two
  matrix-verified rep multipliers (`dim_S/8 = 16`, `p1(Sym^2 T*) = 6 p1(T)`):
  `ch2(S_X)[K3] = 16·(p1(TK3) + p1(Sym^2)) = 16·(-48 + 6·-48) = 16·7·(-48) = -5376`. Computed from only
  `sigma(K3) = -16 -> p1 = -48`; **chi(K3)=24 was never read.** Variants on the same data: normal-only
  S(6,4) = -1152; tangent-only Dirac = -24; H-line-normalized (rank 64) = -84. **Decisively not 24**, and not
  reducible to 3 by any rank normalization. The one apparent "24" (tangent-only `|p1/2|`) is a **disguised
  chi-import** — it equals 24 only because K3 satisfies `2chi + 3sigma = 0` — and was correctly rejected.
- **APS eta(actual operator) = 0.** On the genuine curved Y14 end (not the flat round-S^3), the boundary
  Dirac spectrum is exactly +/- symmetric (defect 2e-14): `eta = 0`, `h = 0`, spectral flow `= 0`. This is
  **structurally forced** by Clifford symmetry (`A_0 = c(p)` has spectrum `+/-|p|`, 64+64, so eta = 0). The
  S^1 lens-space control confirms a nonzero eta is LIVE in principle (`eta(1/3) = +1/3`) but only via the
  global cross-section holonomy, which is unsupplied. **Not 24.**

So the source-derived characteristic class is real and large but **not the generation number**, and the
boundary eta is zero. The topological route, computed honestly, does not produce 3.

## 2. The decisive fact: C2 is NOT an index

The load-bearing test (independently re-derived in the main loop): **C2 is degree-1 homogeneous.**
`C2(2·xi)/C2(xi) = 2.000000` exactly (and `C2(0.5 xi)/C2(xi) = 0.5`). A topological index is **scale-invariant**
(ratio 1); C2 scales linearly with the covector, so `C2 = K·|xi|` is a **symbol-norm**, not an index. It is
also non-integer (`155.36/24 = 6.47`, `/8 = 19.42`, `/16 = 9.71`). **C2 and any topological index are different
KINDS of object**: C2 is a scale-dependent operator-norm on the symbol; ch2/eta/chi are scale-invariant
integers. No computable handle maps one to the other.

## 3. CORRECTION to SOURCE-03

SOURCE-03 established — correctly, and it stands — that **C2 is global**: no local curvature/holonomy can
reduce it (~94% global residual; a holonomy carrier cannot pull a Gamma-independent C2 below bare). But
SOURCE-03 then **inferred** that "the source-action line and the boundary-index line are ONE global object"
and that C2 *is* the boundary spectral section Joe's record-issuance idea pointed at. **That inference is
RETRACTED.** This gate tested it three ways and found **FORCED_ANALOGY**:
- the `ch2` route: no handle maps -5376 / -1152 / -84 onto C2's ~146 residual;
- the `eta` route: inserting the spectral-section projector into the BV closure gives sandwich-C2 = 109.86,
  but that is *exactly* the generic rank-64 Frobenius projection floor (`sqrt(64/128)·155.36 = 109.86`),
  statistically indistinguishable from a random rank-64 projector — a meaningless artifact, not a connection;
- the direct audit: C2 is degree-1 homogeneous and non-integer (Section 2), so it cannot be an index.

"Both global" was **vocabulary convergence**, not machinery — exactly the trap the program is built to catch,
and which it has now caught in its own prior reasoning. C2 is global, AND it is a different kind of object
from the index. The honest status is two distinct open objects, not one.

## 4. The edge of GU's reconstruction, located precisely

The unsupplied objects that block both closing the generation count and connecting C2 to any index — all
confirmed against the repo's own k3-chi-gate map:
1. **The families pushforward** `pi_!: ch(S)/Y14 -> ch(S_X)/X4` is NOT_DEFINED — the metric fiber
   `GL(4,R)/O(3,1)` is non-convex (no valid K-orientation / compact-support / APS pushforward supplied). So
   ch2(S_X)[K3] = -5376 is a bulk characteristic number, NOT yet a licensed index.
2. **The global boundary holonomy / cross-section eta** of the non-compact Y14 end is unsupplied (only the
   trivial flat round-S^3 eta = 0 exists).
3. **A "BV-to-boundary-Dirac symbol map"** — an explicit identification of the BV Koszul-Tate differential
   `M_KT` with a geometric self-adjoint boundary Dirac operator whose APS spectral section connects to C2 —
   does not exist. Without it the C2<->index link is structurally impossible (Section 2).

## 5. The honest bottom line of the whole arc

Pushed to its computational limit, GU's reconstruction **does not close the generation count** and **does not
unify the source action with the topological index**. The appealing "everything is one global object" picture
is, on test, a forced analogy: C2 is a scale-dependent symbol-norm; the index is a scale-invariant integer;
ch2 = -5376; eta = 0; the only 24 is a disguised chi-import. What the reconstruction DOES supply — and this is
the genuine value of the arc — is a complete, machine-checked map of exactly where it ends: the RS BV
bicomplex (built), the C2 obstruction (isolated, proven global, proven not-an-index), and the three precise
unsupplied objects above. Closing GU from here is not a computation on the existing data; it requires new
physics (the written source action) that supplies the pushforward, the boundary holonomy, and the
BV-to-Dirac identification — and even then, per the k3-chi-gate conditional, only IF the source-derived class
evaluates to 24 H-lines without importing the target, which the actual ch2 (-5376) does not.

## What this does NOT establish
- It does not close (or refute) the generation count; the route is OPEN, this specific computation is a negative.
- ch2 = -5376 is a bulk number, not a licensed index (pushforward undefined).
- eta = 0 is for the available (flat-cross-section) operator; the global boundary holonomy is uncomputed.
- It establishes that THIS convergence is forced; it does not preclude some other, genuinely-machinery link
  that a future written source action might supply.
