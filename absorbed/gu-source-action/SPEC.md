# SPEC — the object to construct

The single missing object in Geometric Unity, as pinned by the `gu-formalization` campaign
(see `../gu-formalization/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md`, Part B).

## Prominent Candidate Lens: Security-Budget Source Action

The current front-door steelman for how to search for `S_IG` is the cryptoeconomic security-budget lens:

```text
S_IG may be the variational rule that prices admissible source extensions against
worst-case mathematical forks.
```

See `CRYPTOECONOMIC-SOURCE-ACTION.md`.

This lens does **not** relax the target below. It only proposes a disciplined form for the missing global
selector:

```text
growth of admissible source structure
- validation/finality cost
- worst-case adversarial loss
```

If the lens cannot produce a GU-native carrier for those terms, it is vocabulary and must be killed.

## The target: the stabilized RS/IG source action `S_IG`

Everything downstream in GU (the shiab selector, the generation count, the dark-energy structure, anomaly
closure) is gated on this one object, which GU never writes. A valid `S_IG` must have ALL of:

1. **Master equation.** It is a BV action satisfying `(S, S) = 0` (its own internal consistency / BRST
   nilpotency `s^2 = 0`).

2. **Noether-forced constraint.** Its gauge invariance FORCES the physical (gamma-trace) constraint via a
   Noether identity `delta_2 . d_RS,-1 = 0` — rather than imposing the constraint by hand. (A hand-imposed
   projector is not action-canonical; it was killed in the parent.)

3. **Non-equivariant compensator.** It supplies a ghost `sigma_c` that lives OUTSIDE the Spin(9,5)
   equivariant family. PROVEN NECESSARY: every equivariant attempt cannot close the complex. The parent
   built a genuine non-equivariant, H-linear, anti-trap-passing ghost; the open part is making it close.

4. **Cohomological constraint (full BV bicomplex).** It realizes the constraint COHOMOLOGICALLY via the full
   BV bicomplex (both the ghost leg AND the Koszul-Tate / antighost leg), NOT as a clean decoupled subspace —
   because a clean decoupling reinstates Velo-Zwanziger acausality. The parent BUILT and verified the
   bicomplex (`s^2 = 0`, non-vacuous; the "escape" resolved). What remains is the obstruction below.

5. **The three GLOBAL objects** (this is where the existing data is exhausted):
   - (i) a valid **families pushforward** / index over the non-convex metric fiber `GL(4,R)/O(3,1)`;
   - (ii) the **global boundary holonomy / spectral section** of the non-compact Y14 end;
   - (iii) a **BV-to-boundary-Dirac map** tying the BV Koszul-Tate differential to an actual geometric
     boundary Dirac operator whose APS spectral section connects to the obstruction C2.

## The obstruction it must reconcile: C2

The final, isolated obstruction is `C2 = ||Gamma . M_D . Pi_RS||` = **155.3625** at the repo covector,
**fully Gamma-independent**. Established facts (do not re-discover):
- C2 is **global**: no local curvature/holonomy reduces it (~94% global residual; a holonomy carrier
  `B_W = Gamma.(id (x) G_W)` cannot pull a Gamma-independent C2 below bare).
- C2 is **NOT an index**: it is degree-1 homogeneous (`C2(2 xi)/C2(xi) = 2` exactly) and non-integer — a
  scale-DEPENDENT symbol-norm, a different KIND of object from a scale-invariant topological index.

So a valid `S_IG` must connect C2 to a genuine index via object 5(iii) — which is exactly the unsolved part.

## The hard bar (do not forget)

Even if 1-5 are achieved, the natural characteristic-class computation on the existing data gives
`ch2(S_X)[K3] = -5376`, **not 24**, and `APS eta = 0`. So `S_IG` must ALSO make the matter number come out
right **without importing it**. Existence of `S_IG` is necessary but NOT obviously sufficient for "three
generations." That is the real target, and it may not be reachable — which is a legitimate outcome to prove.
