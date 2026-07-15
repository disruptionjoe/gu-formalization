---
artifact_type: exploration
status: exploration
created: 2026-07-14
title: "W222 FALSIFICATION probe (NON-NAIVE) of the Standard-Model-emergence leg of GU: does the 4D shadow, GRANTING the reduction, give the actual SM hypercharges and an anomaly-free chiral gauge content? VERDICT: SURVIVES. (i) The Pati-Salam SU(4)xSU(2)xSU(2) -> SU(3)xSU(2)xU(1) branching of the SO(10) 16 reproduces the SM generation's electric-charge multiset EXACTLY (Y-values {1/6,-2/3,1/3,-1/2,1,0}; every Q=T3+Y comes out {2/3,-1/3,-2/3,1/3,0,-1,1,0} with correct color/weak multiplicities). (ii) The four perturbative gauge-anomaly coefficients of the chiral 16 all vanish -- U(1)^3=0, grav^2-U(1)=0, SU(2)^2-U(1)=0, SU(3)^3=0 -- by a REAL rep-theory mechanism (Spin(10) has no symmetric cubic Casimir), NOT by analogy; the Witten SU(2) global anomaly is absent (4 SU(2)_L doublets, even); the spin-cobordism Omega^Spin_5(BG_SM) shadow carries no obstruction (consistent with prior repo result R2). (iii) No exotic chiral states are forced in the surviving half. HONEST CAVEAT logged: the carrier delivers a VECTORLIKE 16+16bar, so chirality is produced ONLY by the unbuilt/dynamics-gated mirror-gapping condensate; council H3's 'only-by-analogy' risk is thereby DISPLACED off the anomaly-cancellation (genuine rep theory) and ONTO chirality PRODUCTION, which is a GAP this probe GRANTS per method, not a falsification. So the pre-declared failure condition is NOT triggered."
grade: "exploration / strong-negative (a failed falsification, honestly reported). The hypercharge match and the four perturbative anomaly zeros are exact rational computations with positive controls that have power (a single chiral triplet reads nonzero; two deliberately-wrong embeddings are correctly rejected; removing e_c breaks the cancellation). The SO(10)-16 anomaly-freedom and the Pati-Salam Y-embedding are standard GUT physics, flagged FROM-MEMORY where standard. The global/cobordism leg is asserted at the level of its two computable shadows (tr Y = 0, even doublet count) plus a citation to R2 (Omega^Spin_5(BG_SM) has no 3-torsion; SM saturates the 5th-bordism constraints); a full Dai-Freed/cobordism recomputation is NOT redone here and is the one place a determined adversary could still push. No canon/verdict flip; exploration-tier."
depends_on:
  - explorations/big-swing-2026-07-07/MP-M2-dark-vs-visible.md
  - explorations/big-swing-2026-07-07/MP-M3-count-and-anomaly.md
  - explorations/big-swing-2026-07-03/R2-sm-boundary-mod3-arena-empty.md
  - canon/no-go-class-relative-map.md
scripts:
  - tests/W222_falsify_sm_emergence.py
---

# W222 -- Falsification probe: does GU's 4D shadow give the actual Standard Model?

## The leg and the method

This probe attacks ONE leg of Geometric Unity: **Standard-Model emergence** -- specifically
whether the 4D shadow (a) carries the actual SM **hypercharge** assignments and (b) is **gauge
anomaly-free** as a chiral theory. Method is strict NON-NAIVE falsification: **assume GU is
correct and grant every unbuilt piece resolving as GU hopes.** In particular the 14D->4D
reduction is unbuilt; per the method it is GRANTED, together with the GU carrier's measured
result (MP-M2 / MP-M3) that the internal matter factor is one **SO(10) 16** per generation and
that the mirror-gapping condensate removes the conjugate half. "The reduction is unbuilt" is a
GAP, not a falsification. Only a WRONG definite output or a forced inconsistency counts.

### Pre-declared FAILURE CONDITION

GU is **FALSIFIED on this leg** iff any of:

- **(i)** the `SU(4) x SU(2)_L x SU(2)_R -> SU(3) x SU(2)_L x U(1)_Y` branching gives
  hypercharges that **do not match** the SM (wrong `Q = T3 + Y` on any state), OR
- **(ii)** the 4D chiral shadow carries a gauge anomaly -- perturbative cubic, or the Witten
  `SU(2)` global mod-2 anomaly, or the spin-cobordism `Omega^Spin_5(B G_SM)` global anomaly --
  that **no admissible REAL mechanism cancels**. If the ONLY route to cancellation is a
  lattice/cobordism **analogy** rather than a genuine rep-theory cancellation of GU's own
  chiral content, that is logged as **SURVIVES-ONLY-BY-ANALOGY** (an open falsification RISK,
  per council flag H3, NOT a pass), OR
- **(iii)** forced **exotic chiral states** survive in the physical (surviving) half.

If hypercharges match AND the chiral shadow is anomaly-free by a REAL mechanism AND no exotic
chiral states are forced: **GU SURVIVES** this leg.

Machine-checkable test: `tests/W222_falsify_sm_emergence.py` (exit 0; positive controls first;
every number below is printed by it).

---

## (i) Hypercharge -- the Pati-Salam branching reproduces the SM EXACTLY

`SO(10) 16 = (4, 2, 1) + (4bar, 1, 2)` under `SU(4) x SU(2)_L x SU(2)_R`. Branch
`SU(4) -> SU(3) x U(1)_{B-L}` with `4 = 3_{+1/3} + 1_{-1}` (quark `B-L = +1/3`, lepton `-1`),
and take the Pati-Salam hypercharge `Y = T3R + (B-L)/2`. Building every state and reading
`Q = T3L + Y` as an OUTPUT:

| state | SU(3) | T3L | Y | Q = T3L + Y | SM identity |
|---|---|---|---|---|---|
| `qL_up` (x3 color) | 3 | +1/2 | +1/6 | **+2/3** | up quark |
| `qL_dn` (x3 color) | 3 | -1/2 | +1/6 | **-1/3** | down quark |
| `lL_up` | 1 | +1/2 | -1/2 | **0** | neutrino |
| `lL_dn` | 1 | -1/2 | -1/2 | **-1** | electron |
| `qR_up` (x3 color) | 3bar | 0 | -2/3 | **-2/3** | u^c |
| `qR_dn` (x3 color) | 3bar | 0 | +1/3 | **+1/3** | d^c |
| `lR_up` | 1 | 0 | +1 | **+1** | e^c (positron) |
| `lR_dn` | 1 | 0 | 0 | **0** | nu^c |

The Y-value set is exactly `{1/6, -2/3, 1/3, -1/2, 1, 0}` and the full 16-state electric-charge
multiset (with color and weak multiplicities) is exactly the SM generation's. **Failure
condition (i) is NOT triggered.** Controls with power: a wrong SU(4) branching (`qbl = 1`
instead of `1/3`) and a wrong `SU(2)_R` coefficient (`y_T3R = 2`) are both correctly REJECTED
by the same comparison, so the match is a measurement, not a tautology.

Note (standard, from-memory): there is a discrete GUT-embedding choice (standard vs "flipped"
SU(5)) that permutes which states are `u^c/d^c` and `e^c/nu^c`; BOTH give a consistent
anomaly-free SM generation with correct electric charges, so neither choice falsifies the leg.
GU's carrier construction (MP-M2) fixes the standard embedding by the electron-control `Q = -1`.

---

## (ii) 4D-shadow gauge anomaly -- cancels by a REAL mechanism, not by analogy

**Perturbative cubic anomalies of the chiral 16** (all must vanish for a consistent chiral
gauge theory):

```
U(1)^3        = sum_16 Y^3  = 0
grav^2-U(1)   = sum_16 Y    = 0
SU(2)^2-U(1)  = sum_{L-doublets} Y = 0
SU(3)^3       = (triality sum) = 0
```

All four vanish -- verified as exact rationals. This is a **REAL rep-theory mechanism**, not an
analogy: `Spin(10)` has **no symmetric cubic Casimir**, so the full `so(10)` cubic anomaly tensor
`A^{abc} = tr_16(T^a {T^b, T^c})` is identically zero on the 16, and every `SU(3)xSU(2)xU(1)`
sub-anomaly is a projection of that identically-zero tensor. Positive control (the zero is
NONTRIVIAL, not a blind spot): **removing `e_c` breaks the cancellation** (`U(1)^3 = -1`,
`grav = -1`), and a single chiral color triplet reads `SU(3)^3 = 1`, its conjugate `-1`.

**Witten `SU(2)` global (mod-2) anomaly.** The 16 contains `4` `SU(2)_L` doublets
(`Q_L` x 3 colors + `L_L`) = **even**, so the mod-2 anomaly is absent. Control: an odd count
would flag.

**Spin-cobordism global anomaly `Omega^Spin_5(B G_SM)`.** The two computable shadows -- `tr Y = 0`
(the only 5d-relevant mixed term at this order) and the even doublet count -- are consistent with
no obstruction, and this is corroborated by the prior repo result **R2**
(`R2-sm-boundary-mod3-arena-empty.md`): `Omega^Spin_5(B G_SM)` has no 3-torsion and the SM
content saturates the 5th-bordism constraints, so one SM generation carries no global anomaly.
**Failure condition (ii) is NOT triggered, and the cancellation is REAL, not merely analogical.**

**Where the H3 "only-by-analogy" concern actually lives (and why it does not trigger a kill).**
The concern is legitimate but MIS-LOCATED if aimed at the anomaly-cancellation itself: the
cancellation is genuine `Spin(10)` rep theory, independent of any lattice/cobordism analogy. The
real residual risk is one level UP, in **chirality production** -- see (iii).

---

## (iii) Exotic chiral states -- none forced; but the chirality is manufactured

The GU carrier (MP-M2 / MP-M3) delivers `16` (physical Krein half) `+ 16bar` (mirror half): a
**VECTORLIKE 32**. A vectorlike spectrum is anomaly-free **trivially** (this is the 14D
`Sp(64)`-pseudoreal / Nguyen statement: no perturbative gauge anomaly in the 14D theory) and is
**not chiral**. The nontrivial, SM-defining chiral anomaly-cancellation of (ii) is a SEPARATE
fact and applies only to the surviving CHIRAL 16. Granting the mirror-gapping condensate
(`phi * Pi_mirror`, `[M, P_ghost] = 0`), the physical half is exactly one SO(10) 16: **no exotic
chiral states beyond one SM generation.** Failure condition (iii) is NOT triggered.

The honest caveat, logged: **the step that turns the vectorlike `16 + 16bar` into a CHIRAL 16 is
the mirror-gapping condensate, which is UNBUILT and dynamics-gated** (the scale `mu = phi` is
never predicted; the orientation/which-half-is-physical bit is a free sign). This is exactly the
GU "effective chirality" mechanism placed on the emergence axis L5 by
`canon/no-go-class-relative-map.md` (2.2), where it is flagged as "the sharpest formalization
challenge for GU's chirality program." **H3's "only-by-analogy" risk is therefore real but
DISPLACED**: it is off the anomaly-cancellation (genuine rep theory) and onto chirality
PRODUCTION -- i.e. whether GU's globally-vectorlike Dirac operator can yield an on-shell chiral,
anomaly-consistent 4D gauge theory rather than a Nielsen-Ninomiya-style doubled (vectorlike)
spectrum that cannot be chirally gauged. Under the strict method this unbuilt mechanism is
GRANTED, so it is a GAP, not a falsification.

---

## VERDICT

**SURVIVES.** Granting the reduction and the carrier's `16`-per-generation content:

- **(i)** hypercharges MATCH the SM exactly -- `Y in {1/6, -2/3, 1/3, -1/2, 1, 0}`, correct `Q`
  on all 16 states;
- **(ii)** the chiral shadow is anomaly-free by a **REAL** mechanism -- `U(1)^3 = grav^2-U(1) =
  SU(2)^2-U(1) = SU(3)^3 = 0` (no `Spin(10)` cubic Casimir), Witten `SU(2)` absent (4 doublets),
  no spin-cobordism obstruction -- **NOT** merely by analogy;
- **(iii)** no exotic chiral states are forced.

The pre-declared FAILURE CONDITION is **NOT triggered**. This is an honest FAILED falsification:
the SM-emergence anomaly/hypercharge leg does not fall.

**Load-bearing caveat (not a kill, per method).** The result is CONDITIONAL on the 4D shadow
being the CHIRAL 16. The GU carrier as built is VECTORLIKE (`16 + 16bar`); chirality is produced
only by the unbuilt, dynamics-gated mirror-gapping condensate. The genuine open falsification
RISK for this leg is not the anomaly arithmetic (which is settled and real) but whether GU's
mechanism actually DELIVERS a chiral (not vectorlike) 16 -- a GAP granted here, and the correct
target for any future non-naive attack on SM emergence.
