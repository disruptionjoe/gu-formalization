---
artifact_type: exploration
status: exploration
created: 2026-07-03
title: "Internal path #6 (Sp(64) anomaly cancellation): advance the OPEN global leg by reusing R2's AHSS-at-a-prime spin-bordism machinery. HONEST OUTCOME: PARTIAL. The GLOBAL (Dai-Freed) gauge-anomaly group of the GU 14D theory, Omega^Spin_15(B Sp(n)), has NO ODD torsion for EVERY n (Sp(1)=right-H commutant, Sp(64), general) -- so the whole odd-primary global-anomaly arena is EMPTY, content-independently. Proof: AHSS at any odd prime, H_*(BSp)=Z[q_k] sits in degrees div by 4, Omega^Spin_*(pt) is odd-torsion-free (ABP/Wall), so the odd E_2 line vanishes. The global anomaly is therefore a purely 2-PRIMARY finite group. This makes CANON's 'not settled by pi_15(Sp) alone' precise: pi_15(Sp)=Z is free/torsion-blind. The local I_16 leg is recomputed (CONDITIONAL on the assumed truncated content: gauge octic GS-reducible under Sp(1); grav tr R^8 nonzero only via net chirality -13). NO target imported."
grade: "exploration / PARTIAL. The odd-prime global result is rigorous given two cited theorems (ABP/Wall: Omega^Spin_* odd-torsion-free; H_*(BSp(n);Z)=Z[q_1..q_n] in degrees 4k) -- the executable part verifies the AHSS consequence and is non-vacuous (same machinery finds the Z/3 in Omega^Spin_15(BZ_3)). It does NOT close anomaly cancellation: the 2-primary part of Omega^Spin_15(B Sp(n)) and the map the assumed chiral content induces into it stay OPEN. The local leg is CONDITIONAL on the assumed truncated content (chirally balanced -> vanishes). Nothing here derives cancellation; it removes the odd-primary channel and pins the decisive remainder to the 2-primary/local legs."
depends_on:
  - CANON.md  # "Anomaly cancellation for Sp(64)" Not-Yet-Canon entry + CORRECTION MOVE1-01
  - tests/chase/MOVE-1/move1_octic_sp64_vs_sp1.py
  - tests/chase/MOVE-1/verify/indep_ahat16.py
  - tests/big-swing/R2_spin_bordism_mod3.py
  - tests/big-swing/R2_lens_dai_freed_eta.py
  - explorations/big-swing-2026-07-03/R2-sm-boundary-mod3-arena-empty.md
scripts:
  - tests/internal-paths/anomaly_sp64.py
---

# Internal path #6: advancing the OPEN Sp(64) anomaly-cancellation question

**The question (from CANON's "Not Yet Canon" entry).** Nguyen's `U(128)` anomaly pincer is defused by
the `Sp(64)` replacement, but full GU anomaly cancellation is **OPEN**. CANON names the two required
pieces: **(i)** an explicit **local `I_16` / index-density** computation for the actual chiral field
content (Green-Schwarz factorization), and **(ii)** a **global spin-bordism / Dai-Freed / eta** check,
"**not** settled by `pi_15(Sp)` alone." This pass advances the **global leg** with a rigorous,
target-free result, and recomputes the local leg alongside it (conditional on the assumed content).

**The object.** GU is a `D = 14`-dimensional fermionic theory. Its **global (Dai-Freed) gauge anomaly**
for gauge group `G` is classified by the torsion of the spin-bordism group `Omega^Spin_{D+1}(BG) =
Omega^Spin_15(BG)` (Freed-Hopkins; Garcia-Etxebarria-Montero). The **local** anomaly is the free /
perturbative datum, the degree-`D+2 = 16` anomaly polynomial `I_16` -- exactly the object MOVE-1 already
computed. So the two CANON legs are literally the **torsion** (`Omega^Spin_15`) and **free** (degree-16
`A-hat`) parts of the same bordism spectrum, which is a clean way to organize the problem.

---

## Global leg (advanced): the odd-primary anomaly arena is EMPTY for every Sp(n)

**Method (reused verbatim from R2, `R2_spin_bordism_mod3.py`).** Atiyah-Hirzebruch spectral sequence
localized at a prime `p`:  `E_2^{i,j}(p) = H_i(BG; Omega^Spin_j(pt))_(p) ==> Omega^Spin_{i+j}(BG)_(p)`,
on two rigorous, cited, **target-safe** inputs:

- **(I) `Omega^Spin_*(pt)` is odd-torsion-free** in every degree (Anderson-Brown-Peterson + Wall:
  3-locally `MSpin ~ MSO`, a wedge of `BP` with torsion-free homotopy). So at an **odd** prime,
  `Omega^Spin_j` is **free**, supported in `j = 0,4,8,12,...`. (The script encodes the `n=0..15` table
  and asserts its torsion is 2-primary.)
- **(II) `H_*(B Sp(n); Z) = Z[q_1,...,q_n]`**, symplectic Pontryagin classes in degrees `4,8,...,4n`.
  Torsion-free, supported in degrees divisible by 4 (so `H_odd = 0`). Holds for **every** `n`, covering
  both the naive `Sp(64) = U(64,H)` reading (rank-32 Cartan, so `BSp(32)`) and the **genuine Clifford
  commutant `Sp(1) = right-H`** reading (`n = 1`) that MOVE-1 / `shiab_selector_sp64.py` established as
  the correct gauge group.

**Consequence (computed, script exit 0, 43 asserts).** In any **odd** total degree `n` -- in particular
`n = 15`, the GU Dai-Freed degree -- every `(i,j)` with `i+j = n` has `i` odd (`H_i = 0`) or `j` odd
(`Omega^Spin_j(p) = 0`). The whole odd-degree `E_2` line vanishes `p`-locally for **every** odd prime;
no differential creates torsion from nothing. Therefore

> `Omega^Spin_15(B Sp(n))` has **NO odd torsion**, for **every** `n` -- Sp(1) commutant, Sp(64),
> general. The GU 14D global (Dai-Freed) gauge-anomaly group is a **purely 2-primary** finite group.

This is **content-independent for the odd part**: the fermion content picks *which class in the group*
the theory realizes, but the group's odd part is empty, so **no** chiral content can produce an
odd-primary global-anomaly obstruction.

**`pi_15(Sp)` made precise (the "not enough" datum).** Bott periodicity `pi_i(Sp) = pi_{i+4}(O)` gives
`pi_15(Sp) = Z` -- **free, torsion-blind**. It carries the perturbative octic (a free/local datum) but
by construction cannot see a global *torsion* anomaly. Our AHSS locates that global torsion in the
2-primary part of `Omega^Spin_15`, exactly where `pi_15` cannot look. That is *why* CANON's warning
"not settled by `pi_15(Sp)` alone" is correct -- now with the reason spelled out.

**Non-vacuity (house discipline).** The identical machinery on `BZ_3` (which has `H_odd = Z/3`) **does**
find `Z/3` in `Omega^Spin_15(BZ_3)` (entries at `(i,j) = (15,0),(11,4),(7,8),(3,12)`). So "no odd
torsion for `Sp(n)`" is a real measurement in the same degree, not a machine that always says zero.

---

## Local leg (recomputed, CONDITIONAL on assumed content)

Reproduced from MOVE-1 inside the same certificate so both legs sit together:

- The `[A-hat(TY14)]_16` pure-gravity `p4` (`~ tr R^8`) coefficient is `-1/2419200` (Alvarez-Gaume-Witten;
  the deg-16 numerator `-192` over `464486400`).
- Under the genuine `Sp(1) = right-H` commutant, the gauge octic `Str_S F^8 = 128 (y^2)^4` is a **pure
  product of quadratic Casimirs** -> Green-Schwarz **reducible**, no independent order-8 invariant.
- **ASSUMED truncated content** (repo canon): `Omega^0(x)S^+` (rank `C(14,0)=1`) `+ Omega^1(x)S^-`
  (rank `C(14,1)=14`), net chirality `n_+ - n_- = -13`. The reading-independent gravitational `tr R^8`
  coefficient `= dim(S) (n_+ - n_-) p4 = 64 * (-13) * (-1/2419200) = 13/37800 != 0`.
- Verdict: with this truncation the local `I_16` does **not** GS-factorize -- via the gravitational
  channel, **not** the gauge group. **This is explicitly CONDITIONAL:** a chirally balanced content
  (`n_+ = n_-`) makes the grav irreducible vanish. The truncation is the load-bearing assumption, not a
  derived fact. (No promotion to an anomaly-cancellation claim, per CORRECTION MOVE1-01.)

---

## Honest outcome, and what the global leg still needs

**Grade: PARTIAL.** Advanced the **global leg**: the odd-primary Dai-Freed arena is provably **empty**
for every `Sp(n)`, so the entire global gauge anomaly is 2-primary, and `pi_15(Sp) = Z` demonstrably
could not have settled it. This is rigorous (two cited theorems + verified AHSS consequence + non-vacuity
control) and content-independent. The **local leg** stays conditional on the assumed truncation.

**Does NOT close anomaly cancellation.** No cancellation is derived. The decisive remainder is now
sharply located:

1. **The 2-primary part of `Omega^Spin_15(B Sp(n))`.** Odd primes are clean; the anomaly lives entirely
   at `p = 2`. This needs the 2-local ABP structure (`MSpin_(2) = ko v ko<2> v ... v HZ/2` summands) and
   ko-module differentials -- genuinely harder than R2's mod-3 kill, which could stop at a torsion-free
   input. This is the home of Witten-type `SU(2) = Sp(1)` global anomalies.
2. **The map the assumed chiral content induces** into that 2-primary group -- whether the GU class is
   trivial there. This re-imports the same "assumed truncated content" caveat as the local leg.

**The decisive next step.** Run a 2-LOCAL AHSS / ko-module computation of `Omega^Spin_15(B Sp(1))`
(the genuine commutant is the cheapest: `H^*(BSp(1);Z) = Z[q_1]`, `q_1` in degree 4, so the `E_2` chart
is a single column tensored with `Omega^Spin_*` and the whole problem is a low, explicit ko-module
extension), then evaluate the eta / Dai-Freed invariant of the assumed GU content on a generating
4k-connected `Sp(1)`-bundle over a 15-manifold. That -- plus deciding whether the truncated content is
the physical content -- is what remains to move from PARTIAL toward a verdict.

**Not promoted.** Exploration-grade, staged under `explorations/internal-paths-2026-07-03/` and
`tests/internal-paths/`. No canon / CANON.md / RESEARCH-STATUS edits; no verdict flip. The Sp(64)
anomaly-cancellation question remains **OPEN**.
