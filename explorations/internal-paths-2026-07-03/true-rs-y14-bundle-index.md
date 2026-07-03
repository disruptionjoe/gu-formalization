---
artifact_type: exploration
status: exploration
created: 2026-07-03
title: "Internal path #4 -- the true-RS-Y14-bundle family/APS index. Push the residual-closure machinery from faithful stand-ins (and R1's algebraic Cl(9,5) carrier) onto the ACTUAL fiber-bundle geometry Y14 = Met(X4) -> X4 (fiber GL(4,R)/O(3,1), dim 10, homotopy core RP^3 = L(2;1)). Grade each term of ind(D_RS/Y14) = pi_!(Ahat . ch) separately. RESULT (PARTIAL / BLOCKED-ON-SOURCE-ACTION): four pieces CLOSE on Y14 with no source action -- the spin precondition w2(Y14)=pi*w2(X4) recomputed on the actual Sym^2 vertical bundle, the bulk char-number I_{3/2}=21 sigma/8 (2-primary, sigma kept FREE), the fiber-core APS eta on L(2;1) (grav 0/24 + gauge (1/8)Z, 2-primary), and the cross-chirality family Chern c1(E_-)=0; the ONE decisive piece -- the DEFINITE vertical fiber Dirac L^2 index over the noncompact GL(4,R)/O(3,1) -- is genuinely gated on the unbuilt GU source action, for TWO independent reasons (it leaves the cross-chirality class, and the topological pushforward over a noncompact fiber is undefined without the fiber L^2/APS metric). No target imported."
grade: "exploration / strong-honest. All four closable pieces are RUN (exit 0, 11 hard asserts) on the actual bundle data: w2 via the true Sym^2(rank-4) splitting-principle over GF(2); I_{3/2} via Ahat x RS-character with sigma(X4) a FREE symbol (never substituted -> denominator 8 = 2^3, numerator 21 = 3*7); the lens eta channel (2q^2-4q+1)/8 in exact rationals over q in [-3,6] (all denominators | 8); the cross-chirality symmetric-spectrum / net-holonomy-zero mechanism numerically (<= 1.4e-14). The gated piece [D] is characterized, not fabricated: a certified flux control (the repo's own flux_index_2d builder, |index|=flux, odd for odd flux) shows only a DEFINITE background is odd-capable, and a degree count (fiber dim 10 > homotopy-core degree 3) shows the noncompact pushforward is analytic (L^2/APS), not topological. This is the SAME wall named by R1 and by rs-boundary-eta; internal path #4 pins exactly which sub-terms are on which side of it, on the actual Y14 geometry. Internal tier."
depends_on:
  - canon/function-space-index-conservation-residual-closure-RESULTS.md
  - explorations/big-swing-2026-07-03/R1-rs-operator-residual-and-odd-count-nogo.md
  - canon/rs-boundary-eta-2primary-RESULTS.md
  - canon/w2-y14-spin-structure.md
scripts:
  - tests/internal-paths/y14_bundle_index.py
---

# Internal path #4 -- the true-RS-Y14-bundle index: what closes on Y14, what is gated

## The one open analytic residual

After R1 (big swing) the standing state is: the residual-closure items 2 (APS/end eta) and 3 (family
Chern) are discharged not only on 2x2/1D stand-ins but on the **actual 1792-dim Cl(9,5) Rarita-Schwinger
carrier** over a source-parameter loop. The single wall both R1 and `rs-boundary-eta-2primary` name is
the **definite vertical fiber Dirac operator**, whose family pushforward is the unbuilt GU source action.

R1 worked with the RS carrier as an **algebra at a point**. Internal path #4 pushes onto the object R1
did not touch: the **actual fiber-bundle geometry** `Y14 = Met(X4) -> X4`, fiber
`F = GL(4,R)/O(3,1)` (dim 10, noncompact; homotopy core `RP^3 = L(2;1)`). The Atiyah-Singer family-index
theorem writes the sector index as a fiber pushforward,

```
ind(D_RS / Y14) = pi_!( Ahat(T_vert) . ch(twist) )     (integrate a form over the 10-dim fiber F)
```

and the **fiber's own topology splits this into four gradeable pieces plus the spin precondition**.
Each is graded independently in `tests/internal-paths/y14_bundle_index.py` (exit 0, 11 asserts).

## Precondition -- spin structure, recomputed on the actual vertical bundle

`w2(Y14) = pi* w2(X4)` (canon W2-01) is re-derived here computationally on the **actual** vertical
bundle `TV = Sym^2(T*X4)`: the splitting-principle roots `{a_i + a_j}` of `Sym^2` of a rank-4 bundle
give `w2(Sym^2 E) = w1(E)^2` over GF(2) (residual 0, checked symbolically), so for oriented X4
(`w1=0`) the vertical `w2(TV)=0` and there is nothing to cancel `pi* w2(X4)`. **Y14 is spin iff X4 is
spin** -- the Dirac operator on Y14 is well-posed with no section choice exactly when X4 is spin.
COMPUTABLE on Y14, no source action.

## The four pieces

### [A] Bulk base char-number `I_{3/2} = 21 sigma(X4)/8` -- COMPUTABLE, 2-primary

Computed via `Ahat(X4) . (ch(TX_C) - 1)` (vector-spinor with one Dirac ghost removed), with
`Ahat_4 = -p1/24`, `ch_2(TX_C) = p1`, and `int p1 = 3 sigma`. Keeping **`sigma(X4)` a free symbol**
(no target manifold substituted) yields `I_{3/2} = (21/8) sigma`. **Denominator `8 = 2^3`
(2-primary)**; numerator `21 = 3*7` (so the bulk is itself divisible by 3 and cannot *be* a `1 mod 3`).
This holds for **every** X4. No source action.

### [B] Fiber-core APS boundary eta on `RP^3 = L(2;1)` -- COMPUTABLE, 2-primary

The compact core of the fiber is `RP^3 = L(2;1)`, so the odd-fiber part of the pushforward is exactly
the APS eta already studied in `rs-boundary-eta-2primary`. Two channels, both denominator-decided:
- **gravitational `-p1/24`** (the only route to an order-3): fed only by a **net self-dual frame
  charge**, which is `0` for a chirality-odd (cross-chirality) operator because `{D,Gamma}=0` forces a
  `+/-`-symmetric spectrum (re-checked here to `1.4e-14`). So `grav eta-bar = 0/24`.
- **gauge/spectral**: charge-`q` reduced eta-bar `= (2q^2 - 4q + 1)/8`, evaluated in exact rationals
  over `q in [-3,6]` -- **every denominator divides 8**.

`eta = [grav: 0] + [gauge: (1/8)Z] => 2-PRIMARY, never a 3`. No source action.

### [C] Cross-chirality family Chern `c1(E_-) = 0` -- COMPUTABLE (structural)

In the cross-chirality Krein class, `Gamma` conjugates `E_- <-> E_+`, so `c1(E_-) = c1(E_+)` while
`c1(E_-) + c1(E_+) = c1(total, trivial) = 0`. Reconfirmed here by the net-holonomy-zero identity on a
loop of cross-chirality blocks (`|Berry(E_-) + Berry(E_+)| = 1.3e-16`). R1 already proved this on the
**actual** Cl(9,5) carrier. No source action.

### [D] Definite vertical fiber Dirac `L^2` index -- GATED on the source action

This is the decisive piece, and it is genuinely gated -- for **two independent reasons**, both
exhibited in the script:

- **(d1) It leaves the cross-chirality class.** The vertical fiber Dirac operator over `GL(4,R)/O(3,1)`
  is **same-chirality / definite (Riemannian)**, so `{D,Gamma} != 0`, its spectrum is *not*
  `+/-`-symmetric, and **none** of the vanishing mechanisms [A]/[B]/[C] apply. It is the **only**
  odd-capable term. Control (the repo's own certified `flux_index_2d` builder): a definite magnetic
  background carries net chiral index `= flux`, **odd for odd flux** (`|index| = 1,2,3`), while a
  cross-chirality operator's index is forced to 0.
- **(d2) The pushforward over a noncompact fiber is not topological.** `F = GL(4,R)/O(3,1)` is
  **noncompact** (the Lorentzian condition is open in `Sym^2`), dim 10, but its rational cohomology
  stops at the homotopy-core degree 3 (`RP^3`). The family pushforward `pi_!` must integrate a
  degree-10 form over `F`; over a **noncompact** fiber that is **not** a topological pushforward but an
  **`L^2` / APS analytic index** requiring the fiber Riemannian metric, completion, and end condition
  -- exactly the datum the **unbuilt GU source action** supplies. The compact-core (`RP^3`, odd) part
  is the eta term [B] (computable); the full noncompact 10-dim definite fiber index is not.

## Outcome grade

**PARTIAL -- BLOCKED-ON-SOURCE-ACTION for the decisive term.**

| piece | on Y14 | grade |
|---|---|---|
| precond `w2(Y14)=pi*w2(X4)` | actual `Sym^2` vertical bundle | **CLOSED** |
| [A] bulk `I_{3/2}=21 sigma/8` | base, `sigma` free | **CLOSED** (2-primary, every X4) |
| [B] fiber-core APS eta on `L(2;1)` | grav `0/24` + gauge `(1/8)Z` | **CLOSED** (2-primary) |
| [C] cross-chirality family `c1(E_-)` | structural + R1 actual carrier | **CLOSED** (0) |
| [D] definite vertical fiber Dirac `L^2` index | noncompact `GL(4,R)/O(3,1)` | **GATED on source action** |

What internal path #4 adds beyond R1: it moves from the algebraic RS carrier at a point to the
**actual `Y14 -> X4` fiber-bundle geometry**, and pins *exactly which* sub-terms sit on which side of
the wall. Every 2-primary / vanishing sub-term (the entire route by which an **odd** generation count
could enter through the interior, boundary, family, or base) closes on the real bundle without the
source action. The lone remaining channel is the definite vertical fiber index -- and it is gated for a
**structural** reason (noncompact non-topological pushforward), not a bookkeeping one.

## The next decisive step

Build the definite vertical fiber Dirac operator on `GL(4,R)/O(3,1)` with its GU-supplied fiber metric
and APS/`L^2` end condition, and compute its family pushforward over X4. That single object -- the GU
source action -- stands between "every odd-capable interior/boundary/family/base term closes 2-primary
on Y14" and an actual generation count. It is the same wall named across the program; #4 shows it is
now the *only* one, localized to one analytic object on the actual bundle.

## Hard-rule compliance

No target imported: `sigma(X4)`, `chi`, the `/8`, and `Ahat=3` are never substituted; the only integers
are RS-bundle character coefficients (`21=3*7`), chiralities, lens charges, and flux quanta. Nothing
here derives three or forbids three. Exploration-grade; staged under `explorations/internal-paths-2026-07-03/`
and `tests/internal-paths/`. No canon/paper/status edits; no promotion; no commit.

## Reproduce

```
python tests/internal-paths/y14_bundle_index.py
```

Exit 0, 11 hard asserts.
