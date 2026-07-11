# Narrowing the source action by the intersection of the legs that need it (not building it -- constraining it)

2026-07-11. Joe's move: rather than a FREE build of the source action (which p-hacks the residual),
identify what it MUST look like by requiring every leg that depends on it to work SIMULTANEOUSLY. The
central finding: the source action is NOT a product of independent freedoms -- several legs constrain the
SAME sector, so the joint requirement OVER-DETERMINES the shared sectors and narrows the build. This is not
p-hacking: the constraints come from independent physics legs, not from choosing the answer.

## The source action's four sectors

`S_GU` over the field space on `Y14` decomposes into:
- **(A) shape / gravity:** the section-shape functional `E[s] = int |II_s^H|^2` -- Willmore `W_s` plus the
  ambient-curvature term `alpha_W * R^Y.B` at `O(M^2/r^4)`.
- **(B) gauge / Yang-Mills:** `F_A` of the inhomogeneous gauge group `IG = G semidirect Omega^1(ad)`, the
  ambient group / its symmetry-breaking vacuum.
- **(C) theta / source-law:** the geometric distortion `theta` and the closure `D_A*F_A = theta`.
- **(D) RS / matter:** the Rarita-Schwinger sector and its field-space DECLARATION (the located-not-forced
  2-bit: invariance-selection x phase).

## The constraint matrix -- which leg touches which sector

| Leg (needs the action) | (A) shape | (B) gauge | (C) theta | (D) RS |
|---|---|---|---|---|
| **Gravity** (Branch-3 must give exact Schwarzschild) | **fixes `alpha_W` / `R^Y.B` sign+coeff** | `E_s^YM` enters | **needs `theta ~ M/rho^2` to cancel `W_s`** | -- |
| **Dark energy** (DESI-consistent, `f_0`) | -- | `F_A` sources it | **`theta` IS the DE field (Assumption 3, amplitude `f_0`)** | -- |
| **Forces** (max-compact = SM, no extra photon) | -- | **fixes the ambient `G` / sub-block** | -- | -- |
| **Standard Model** (`v_PSB -> G_SM`, anomaly) | -- | **fixes the breaking vacuum** | -- | matter content |
| **Generation count** (carrier A/B) | -- | RS-gauge coupling | -- | **the 2-bit declaration** |

## The over-determinations (where the joint requirement NARROWS the action)

The off-diagonal fills are the narrowing. Two sectors are constrained by MULTIPLE independent legs:

### theta-sector = gravity INTERSECT dark energy  (the sharpest, most decisive narrowing)
`theta` appears in BOTH the gravity source law (`D_A*F_A = theta`, Branch 3 needs a nonzero geometric
`theta ~ M/rho^2` in a `Psi=0` vacuum to carry the `M/rho^2` tail and cancel the trace-free Willmore
residual) AND the dark-energy sector (`theta` is the dynamical DE field; Assumption 3 `theta ~ D_A*F_A`
with amplitude `f_0`). **These are two independent physics constraints on the SAME object.** So the
`theta`-coupling is NOT free: it must simultaneously (i) give the DESI-consistent EOS and (ii) provide the
exact `O(M^2/r^4)` gravitational cancellation. **Decisive, computable, non-p-hacking test: does the
`theta`-coupling fixed by dark energy (Assumption 3 + `f_0`) also produce the Branch-3 Willmore
cancellation gravity needs?** If YES -> `theta` is jointly fixed, gravity and dark energy collapse to one
sector, and `f_0` is no longer a free fit (dark energy's weakest point closes). If NO -> a genuine tension
(possibly a disproof via the theta-sector). Either outcome narrows the build decisively.

### gauge-sector = forces INTERSECT SM INTERSECT dark energy INTERSECT count  (the most over-constrained)
`F_A` / `G` / the IG structure appears in ALL of forces (max-compact `= su(3)+su(2)+u(1)`), SM (a `v_PSB`
vacuum reaching exactly `G_SM`), dark energy (`F_A` sources `theta`), and the count (RS-gauge coupling).
So `G` and its vacuum are pinned by a FOURFOLD requirement: the ambient group must (a) have maximal compact
`= SM` (forces), (b) admit a rank-one breaking vacuum whose stabilizer is exactly `G_SM` (SM -- already
verified to EXIST for the Pati-Salam vector), (c) have `F_A` whose divergence is the DE `theta` (dark
energy + gravity), and (d) couple to the RS sector to deliver the matter. The surviving `G`/IG structures
are the intersection of (a)-(d); this is where "which sub-block" (the residual flagged in the paper) is
actually constrained -- the sub-block is not free once (a)-(d) must all hold.

### The two genuinely-remaining scalars
After the shared-sector over-determination, the residual freedom is small:
- `alpha_W` (the gravity `R^Y.B` coefficient) -- fixed by the gravity leg alone (one scalar), gated on the
  `theta`-sector above.
- the RS 2-bit declaration (the located-not-forced count) -- the last freedom, coupled to the (now
  over-determined) gauge sector.

## What the source action must look like (the narrowed form)

Given the intersection, `S_GU` is forced into the shape:
`S_GU = int [ alpha_W (W_s + R^Y.B-term)  +  ||F_A||^2  +  <Psi, D_A Psi>  +  |D_A*F_A - theta|^2 ]`
with the constraints: **`theta` is the single field shared by gravity and dark energy (its coupling fixed
by their intersection, not a free `f_0`)**; **`G`/IG is the intersection group whose max-compact is the SM,
whose rank-one vacuum is `G_SM`, and whose `F_A` sources `theta`**; the only free data left are `alpha_W`
(gravity) and the RS 2-bit (count) -- and both are gated on, not independent of, the `theta`- and
gauge-sector solutions.

## Why this is not p-hacking, and the decisive next computation

Every constraint above is an INDEPENDENT physics requirement (a DESI fit, a black-hole solution, the SM
gauge group, anomaly-freedom) -- none is "choose the answer". The intersection therefore FORCES rather than
fits. The single highest-leverage, decisive, non-p-hacking computation the map isolates:

> **Compute whether the `theta`-coupling that dark energy requires (Assumption 3, `f_0`) is the same
> `theta` that cancels the gravity Branch-3 Willmore residual at `O(M^2/r^4)`.** One shared field, two
> independent leg-constraints. Agreement collapses gravity + dark energy into one solved sector and
> removes `f_0` as a free fit; disagreement is a real tension. Either way it narrows the build far more
> than a free construction, and it does not p-hack the count.

## Grade

Structural / reconstruction-grade (the sector forms are reconstruction-grade from the draft + canon). The
CONSTRAINT-INTERSECTION logic (shared sectors over-determine the action; the theta = gravity ∩ dark-energy
coupling; the fourfold gauge over-determination) is the contribution -- it converts "build the source
action (p-hacks)" into "the legs jointly force it, and here is the one decisive compatibility computation."
No claim/canon movement. Feeds WI-068 and the North Star (the honest, non-p-hacking route to the action).
