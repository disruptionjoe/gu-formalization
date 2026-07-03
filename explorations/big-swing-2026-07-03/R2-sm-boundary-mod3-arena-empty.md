---
artifact_type: exploration
status: exploration
created: 2026-07-03
title: "R2 big swing (SM-as-boundary, GLOBAL/torsion layer): does requiring the whole anomaly-free SM as chiral boundary data PIN the generation count in the odd-torsion (mod-3) arena via spin-bordism / Dai-Freed eta? HONEST OUTCOME: a KILL. The mod-3 arena is provably EMPTY for the SM -- Omega^Spin_5(B G_SM) (x) Z_(3) = 0 -- so there is no Z/3 for a count to be pinned in. Two independent, RUN certificates: (A) an AHSS-at-p=3 computation showing Omega^Spin_n(B G_SM) has no 3-torsion for all odd n (root cause: Omega^Spin_*(pt) is odd-torsion-free by ABP/Wall, and 3-locally B G_SM ~ BU(3) x BSU(2) is torsion-free/even); (B) a concrete Dai-Freed eta / APS rho-invariant on L(3;1,1) with the whole SM generation coupled to the flat Z_3 <= U(1)_Y, giving mod-3 phase Theta = 0 via COLOR TRIALITY (charged-class Weyl multiplicities 6,6 == 0 mod 3), for any normalization. NO target imported."
grade: "exploration / strong. Certificate (A) is rigorous given two cited theorems (ABP/Wall: Omega^Spin_* odd-torsion-free; (SU(3)xU(1))/Z_3 = U(3)) -- the executable part verifies the AHSS consequence and is non-vacuous (same machinery finds the Z/3 in Omega^Spin_3(BZ_3)). Certificate (B)'s eta formula is externally validated (L(2;1,1)=RP^3 gives the known Dirac eta 1/8) and its verdict rests on an exact integer divisibility (color triality), normalization-independent. Honest limitation: (B) is 3-dimensional (a 2D-theory Dai-Freed test); the 4D statement is carried by (A). The generation-count verdict stays OPEN; nothing here derives three -- it KILLS a specific route by which three could have been forced."
depends_on:
  - explorations/anomaly-and-bordism/sm-as-boundary-cobordism-frontier-2026-07-03.md
  - tests/sm-boundary/anomaly_inflow_toy.py
  - canon/external-topological-index-flux-RESULTS.md
  - canon/source-action-family-index-interface-SPEC.md
scripts:
  - tests/big-swing/R2_spin_bordism_mod3.py
  - tests/big-swing/R2_lens_dai_freed_eta.py
---

# R2 big swing: is the generation count pinned in the mod-3 arena by SM boundary data?

**The swing.** Today's local toy (`tests/sm-boundary/anomaly_inflow_toy.py`) established that *perturbative*
SM anomaly-freedom is **count-blind**: it constrains only the 2-primary (parity) arena and leaves every
residue mod 3 free. The stated home-run target was to escalate to the **global (Dai-Freed / spin-bordism)**
layer and decide whether requiring the *whole anomaly-free SM as chiral boundary data* **PINS** the count in
the odd-torsion (mod-3) arena -- the `Z/3 <= pi_3^s = Z/24` where the program's CRT split says a count could
hide -- **without importing the number 3**.

**Honest outcome: a KILL (the "provably is NOT pinned" home run).** The mod-3 arena is **empty** for the
Standard Model. The generation count *cannot* be pinned mod 3 by requiring SM-shaped anomaly-free boundary
data, because the object that would have to contain the pinning constraint -- the SM's Dai-Freed /
spin-bordism global-anomaly group `Omega^Spin_5(B G_SM)` -- **has no 3-torsion at all**. There is no `Z/3`
for a count to live in. Two independent certificates, both RUN (exit 0), reach this verdict.

---

## Certificate A -- structural: `Omega^Spin_5(B G_SM) (x) Z_(3) = 0` (`R2_spin_bordism_mod3.py`)

A 4D chiral theory's global (Dai-Freed) anomalies are classified by the torsion of `Omega^Spin_5(BG)`
(Freed-Hopkins; Garcia-Etxebarria-Montero). The count is "pinned mod 3" iff that group has a `Z/3` **and**
the SM content maps to it non-trivially. So the sharp, decidable, target-free question is: *does the SM
anomaly group have any 3-torsion?* We answer it with the Atiyah-Hirzebruch spectral sequence localized at
the prime 3, `E_2^{i,j} = H_i(BG; Omega^Spin_j(pt)) ==> Omega^Spin_{i+j}(BG)`, on two rigorous, cited,
target-safe inputs:

- **(I) `Omega^Spin_*(pt)` is odd-torsion-free, in every degree.** THEOREM (Anderson-Brown-Peterson +
  Wall): at an odd prime `p`, `MSpin_(p) ~ MSO_(p)`, a wedge of suspensions of `BP` whose homotopy
  `Z_(p)[v_1,v_2,...]` is torsion-free. So 3-locally `Omega^Spin_j` is **free**, supported in
  `j = 0,4,8,...`. (The script encodes the standard `n=0..9` table and asserts its torsion is 2-primary.)
- **(II) `H_*(B G_SM; Z_(3))` is torsion-free and even.** The true SM group is
  `G_SM = (SU(3) x SU(2) x U(1))/Z_6`. Localized at 3 the `Z_2` is invisible, and
  **`(SU(3) x U(1))/Z_3 = U(3)` exactly** (the map `(A,z) -> zA` has kernel `{(w^-1 1, w): w^3=1} = Z_3`,
  image `U(3)`). So 3-locally `B G_SM ~ BU(3) x BSU(2)`; both have torsion-free integral cohomology
  `Z[c1,c2,c3]`, `Z[c2]` in even degree -> `H_odd = 0`, no torsion. (The script verifies the computable
  shadow -- `PS(B(SU(3)xU(1))) == PS(BU(3))` -- and `H_odd = 0`.)

**Consequence (computed).** For any **odd** total degree `n`, every `(i,j)` with `i+j = n` has `i` odd
(`H_i = 0`) or `j` odd (`Omega^Spin_j (x) Z_(3) = 0`). The whole odd-degree `E_2` line vanishes 3-locally;
no differential can create torsion from nothing. The script verifies

> `Omega^Spin_n(B G_SM) (x) Z_(3) = 0` for `n = 1,3,5,7,9` -- in particular `n = 5` (the 4D Dai-Freed
> degree) and `n = 3`.

**Non-vacuity (the check can fail).** The identical machinery on `BZ_3` (which has `H_odd = Z/3`) **does**
find `Z/3` in `Omega^Spin_3(BZ_3)` (entry `E_2^{3,0}`). So "no 3-torsion for the SM" is a real
measurement, not a machine that always says zero.

**Why the arena is empty, in one line.** *Every* SM structural subtlety that could have opened a mod-3
arena -- the `Z_6` quotient, the `Spin-Z_2` twist that makes the fermions well-defined, the Witten `SU(2)`
global anomaly -- is a **2-group / 2-primary** phenomenon and never reaches the prime 3. The count-carrying
`Z/3` the program hoped for simply has no home in the SM's bordism.

---

## Certificate B -- concrete: SM eta on `L(3;1,1)` gives mod-3 phase 0 (`R2_lens_dai_freed_eta.py`)

Independent confirmation from an actual eta-invariant on a manifold that *does* carry a `Z_3`. We take the
lens space `L(3;1,1) = S^3/Z_3`, couple the whole SM generation to the flat `Z_3 <= U(1)_Y` Wilson line, and
read the mod-3 Dai-Freed phase.

- **Object.** Reduced eta of the twisted Dirac operator (APS/Donnelly),
  `xi_a = (1/p) sum_{j=1..p-1} zeta^{aj} / (2i sin(pi j/p))^2`. Computed, real, rational; validated
  internally by `sum_a xi_a = 0` for `p = 2,3,5,7`. **Externally validated:** at `p = 2`,
  `L(2;1,1) = RP^3` gives `xi = +-1/8` -- the known Dirac eta of `RP^3`, the same 2-primary `Z/8` datum the
  program's own canon references (`rs-boundary-eta-2primary-RESULTS.md`).
- **Gravity subtraction (honest).** `xi_0` is the pure-gravity piece; since `Omega^Spin_3(pt) = 0`,
  `L(3;1,1)` bounds, so `xi_0` is a removable local counterterm. The genuine gauge invariant is
  `rho_a = xi_a - xi_0 in (1/3)Z`: here `rho_0 = 0`, `rho_1 = rho_2 = 1/3`.
- **Assembly.** Each left-handed Weyl of hypercharge `Y6 = 6Y` contributes `rho_{Y6 mod 3}`. The SM
  generation's Weyl multiplicities by hypercharge class mod 3 are

  | class `a` | fields | multiplicity |
  |---|---|---|
  | 0 | `L (2)`, `e^c (1)` [`, nu^c (1)`] | 3 (or 4) |
  | 1 | `Q (3 color x 2 weak)` | **6** |
  | 2 | `u^c (3)`, `d^c (3)` | **6** |

  `Theta = sum_a mult_a rho_a = 6*(1/3) + 6*(1/3) = 4 in Z`. The mod-3 phase is **0**, for both 15- and
  16-Weyl content. `n` generations give `n*0 = 0`: **not pinned**.

**Robust backbone (normalization-independent).** `rho_a in (1/3)Z`, so `Theta` is an integer *as soon as*
each charged-class multiplicity is divisible by 3. The SM's are `6, 6 == 0 mod 3` -- this is **color
triality**: every colored multiplet arrives in 3 colors, so its Weyl count is a multiple of 3. The mod-3
phase vanishes for *any* spin structure / normalization convention, killed by an integer divisibility, not
by a fitted number. This is the *same* fact Certificate A saw as "3-locally `B G_SM ~ BU(3)`, the `Z_3` is
color triality." **Non-vacuity:** a bare charge-1 Weyl gives `Theta = 1/3 != 0`, and two of them give
`2/3 != 0` -- the toy can detect a mod-3 pin when the multiplicities are not `0 mod 3`.

**Honest limitation.** `L(3;1,1)` is 3-dimensional (directly a *2D*-theory Dai-Freed test); the 4D SM lives
on 5-manifolds. The dimension-faithful statement is Certificate A. Certificate B is a concrete realization
of the *mechanism* (triality/divisibility), which is dimension-independent.

---

## What this settles, and what it does not

**Settles (this swing).** The offensive question "does requiring the whole anomaly-free SM as boundary data
pin the count in the mod-3 arena?" gets a clean **NO**, from two independent directions that tell the same
story (color triality = `Z_3` is the `SU(3)` center = `BU(3)` torsion-free). The `Z/3 <= Z/24` arena the
program's CRT split flagged as *the* place a count could hide is, for the SM, **not present**:
`Omega^Spin_5(B G_SM)` has no 3-torsion. Together with today's local toy (perturbative anomaly-freedom is
count-blind, 2-primary only), **both the local and the global anomaly layers now provably leave the count
mod-3 free.** The "count hides in `Omega^Spin` `Z/3`" hope is **dead**.

**Does NOT settle (and no target imported).** This does not derive three and does not claim three is
forbidden -- it removes one specific *mechanism* by which three could have been *forced* (a mod-3 global
anomaly). The number 3 was never assumed, inserted, or divided by: it entered only as the prime we localize
at to probe odd torsion, and the SM's answer there is "empty." No `chi(K3)=24`, no `/8`, no `Ahat=3`. The
generation-count verdict stays **OPEN**.

**Where the wall now is (what would be needed to reopen a mod-3 route).** A mod-3 pinning would require
*new* 3-torsion in the relevant bordism -- i.e. a structure the SM does **not** have: (i) a nonabelian
finite or higher-form symmetry group `G'` with `3 | |H_*(BG')|` in an odd degree (the SM's discrete
structure is `Z_6`, whose 3-part is `Z_3 =` color center, already absorbed into `U(3)`); or (ii) an
enlarged tangential structure whose bordism `Omega^{H}_5` carries odd torsion (all SM-relevant twists --
`Spin`, `Spin-Z_2`, `Spin^c` -- are odd-torsion-free). Absent such a structure, the odd arena is provably
closed. This is the concrete residual, and it points *away* from anomaly cancellation as a source of three:
consistent with the program's standing conclusion that the count is **external, located but not forced**.

**Not promoted in this pass.** Exploration-grade; staged under `explorations/big-swing-2026-07-03/` and
`tests/big-swing/`. Canon promotion is agent-owned as of 2026-07-03 (see the RESEARCH-STATUS Promotion Rule);
a verdict/status flip is separate and still pauses for Joe. The generation-count verdict remains OPEN.
