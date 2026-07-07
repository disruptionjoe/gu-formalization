---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "RS-S4 (base-forcing + Bismut-Cheeger, the paper's other two named Section-9 bridges): is there ANY GU-forced base carrying 3-torsion, and can a Y14-fiber twisted-RS index reduce to the located e_R=1/12 carrier on the RP^3 spine? HONEST OUTCOME: GATED. Two sharp sub-results, both MEASURED: (a) the 2-adic wall is a THEOREM in COHOMOLOGY -- p-q=4 forces the metric-fiber spine RP^3 = O(4)/(O(3)xO(1)) = S^3/Z2, whose H^2 = Z/2 (Smith-normal-form measured, not recalled), the whole real-projective forcing tower RP^n is 2-adic, and the two target-fitted spaces DO NOT EVEN CARRY TORSION (CP^2's 3 and K3's 24 are chi/free-rank, measured via Betti sums, never a 3-torsion class); a non-vacuity control MEASURES H^2(L(3;1))=Z/3, proving the solver detects 3-torsion when present. So no GU-forced base has H^2 3-torsion; the 'choose X^4 with 3-torsion' escape is an unforced IMPORT of the same class as K3/CP^2. (a') BUT the forced RP^3 spine DOES reach order 3 -- in FRAMED BORDISM pi_3^s=Z/24 (|Im J|=denom(B_2/4)=24, homotopy provenance, DISTINCT from chi(K3)=24), via a reconstruction-grade tangential framing carrying e_R = p_1/48 = 2/24 = 1/12 (two normalizations agree, order 12 in Q/Z, 3-adic valuation 1). This is not a cohomology escape; the carrier was never a cohomology-torsion object, and by Hom(Z/3,Z)=0 it is mod-3 INFORMATION, not an integer. (b) The Bismut-Cheeger fiber-index reduction to an INTEGER preimage of e_R is UNAVAILABLE in the built machinery: the even S^6 metric fiber is index-transparent (A-hat[M^6]=0 structurally -- no degree-6 Pontryagin number -- so its BC eta-form contributes ZERO to the e_R channel); the RP^3=L(2;1) boundary's own gauge/Dai-Freed eta is 2-adic (APS/Donnelly trig sum measured -1/8,+1/8, denominators powers of 2, with a 3-adic L(3;1) control); and the decisive arithmetic -- with the transparent-fiber bulk = 0 the APS identity ind = bulk - e_R gives ind = -1/12, NOT an integer -- shows e_R is a BOUNDARY DATUM with no integer-index preimage in the available reduction. SIGNAL = GATED: a forced 3-base (RP^3 in framed bordism) and a candidate reduction both survive; the open condition is exactly the unbuilt RELATIVE/EQUIVARIANT twisted-RS index PLUS a proven BC reduction on the actual operator (Section 9's gate). KILL is NOT warranted."
grade: "CONSISTENT_UNCOMPUTED (route verdict GATED); sub-results at THEOREM grade at their stated scopes: (a) integer-cohomology torsion of RP^n / L(p;1) / CP^2 / K3 is MEASURED by Smith normal form with a passing non-vacuity control (L(3;1) -> Z/3) and a passing 2-adic tower (RP^2..RP^5 all Z/2), so the cohomology 2-adic wall is machine-certified; the retract identification GL(4,R)/O(3,1) ~ RP^3 is dimension-and-structure verified (dim 3, S^3/antipodal). (b) A-hat[S^6]=0 is a structural theorem (no degree-6 Pontryagin monomial, machine-listed empty); the RP^3 gauge eta 2-adicity and the L(3;1) 3-adic control are exact rationals from the APS/Donnelly trig sum; the transparent-fiber index fractionality (ind=-1/12) is exact rational arithmetic. FROM-MEMORY flags: the Kirby-Melvin p_1=4 framing normalization for e_R (cross-checked against the independent Adams class-2/24 route, agreeing at 1/12); eta(S^6)=0 for the round PSC metric; the general Bismut-Cheeger fibered-boundary theorem statement (its application to GU's operator is the unbuilt gate, not asserted here). Anchors reproduced first on the verified Cl(9,5)=M(64,H) carrier: rank(Gamma)=128, dim ker=1664, triplet Krein (+96,-96,0), 12k index. TARGET-IMPORT GUARD at maximum strictness: no element of {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} assumed, inserted, hardcoded as an answer, or divided by to GET an answer; the two 24s (chi(K3) via Betti sum vs |Im J| via Bernoulli denominator) are kept provenance-distinct; every 3 is MEASURED with its chain printed. Every count stated as 'mechanism/base M forces c', never 'GU forces c'. Internal tier: computed + self-adversarial, not externally replicated."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - canon/h2-base-index-chirality.md
  - explorations/big-swing-2026-07-06/VG-V7-cp2-equivariant-payoff.md
  - explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md
  - explorations/big-swing-2026-07-06/BIG-SWING-CONFORMAL-CLASS-BLOCKED.md
  - explorations/big-swing-2026-07-07/BIG-SWING-ALIGNMENT-PHASE-NOT-TUNING.md
scripts:
  - tests/big-swing/rs_s4_base_forcing_bismut_cheeger.py
---

# RS-S4: base-forcing + the Bismut-Cheeger bridge

**The swing.** The frozen `located-not-forced` paper (Section 9) states the only open bridge in sharp
form: the generation count *cannot BE* the absolute order-3 torsion class, because `Hom(Z/3, Z) = 0`
kills any class-to-integer map. An integer count can only arise from a **relative, equivariant, or rank**
invariant -- integer-by-construction, geometry-dependent -- which is exactly the unbuilt twisted
Rarita-Schwinger index. Section 9 names three things that must be built together, on GU's actual
14-manifold: a proven fibered-boundary reduction, the explicit twisted-RS operator, and an integer
extraction with the tangential-vs-gauge fork resolved. This route attacks the **other two named bridges**
(base-forcing and Bismut-Cheeger), not the operator itself:

- **(a) Base-forcing.** Is there ANY GU-forced base carrying 3-torsion, or is the 2-adic wall structural?
- **(b) Bismut-Cheeger.** Does the `Y14`-fiber twisted-RS index reduce to the boundary `e`-invariant
  `e_R = 1/12` on the `RP^3` spine via a proven reduction, or is `e_R` a boundary datum with no
  integer-index preimage?

**Honest outcome: GATED.** The 2-adic wall is a **theorem in cohomology** and the two target-fitted
spaces don't even carry torsion -- but the forced `RP^3` spine still reaches order 3, in **framed
bordism**, not cohomology, exactly where the located carrier lives; and the fiber-index reduction to an
integer preimage of `e_R` is **unavailable** in the built machinery, leaving the same Section-9 gate.
Neither half licenses a KILL.

All numbers below are printed by `tests/big-swing/rs_s4_base_forcing_bismut_cheeger.py` (run from repo
root, exit 0). Anchors reproduced first on the verified `Cl(9,5) = M(64,H)` carrier: `rank(Gamma) = 128`,
`dim ker(Gamma) = 1664`, triplet Krein signature `(+96, -96, 0)` (the Cartan = Krein = ghost-parity seat,
constraint 1), and the `h2` canon full-bundle index `2(0) + 4(k) + 2(4k) = 12k`.

---

## (a) Base-forcing: the 2-adic wall is a cohomology theorem

**The forced spine, by provenance.** The metric signature `p - q = 4` forces the metric fiber
`F = GL(4,R)/O(3,1)` (`dim = 16 - 6 = 10`). Its maximal-compact deformation retract -- its spine -- is
`O(4)/(O(3) x O(1))` (`dim = 6 - 3 - 0 = 3`): `O(4)/O(3) = S^3`, and the residual `O(1) = Z/2` acts
antipodally, so **the spine is `RP^3 = S^3/Z_2`** (measured by dimension and structure, not recalled).

**Torsion measured, not recalled.** Integer (co)homology via Smith normal form of the cellular boundary
matrices:

| base | provenance | `H^2` torsion | reading |
| --- | --- | --- | --- |
| `RP^3` (the spine) | `p-q=4` forced | `Z/2` | **2-adic** |
| `RP^2, RP^4, RP^5` | forcing tower | `Z/2` (all degrees) | 2-adic tower (`O(1)=Z/2` decks only) |
| `CP^2` | unforced target-fit | **NONE** | `chi = 3` is `b_0+b_2+b_4` (free rank), not torsion |
| `K3` | unforced target-fit | **NONE** | `chi = 24`, `sigma = -16` (free ranks), not torsion |

**Non-vacuity control (the solver can see a 3):** the identical machinery MEASURES
`H^2(L(3;1)) = H^2(S^3/Z_3) = Z/3` (and `L(5;1) -> Z/5`), while `RP^3 = L(2;1) -> Z/2`. The Z/2 verdict
is a measurement, not a machine that always says "2".

**The provenance point that matters most.** The two spaces whose "3" and "24" the program has repeatedly
had to fend off (`CP^2`'s `c_1 = 3h`; `K3`'s `chi = 24`) **carry no torsion at all**. Their `3` and `24`
are Euler-characteristic / free-rank data, measured here as Betti sums -- *not* order-3 or order-24
torsion classes. This sharpens the target-import guard: the forbidden `chi(K3) = 24` is not merely
un-imported, it is a *different kind of object* from the located order-3 carrier (a rank, not a torsion
class), so identifying the generation count with it was always a type error independent of `Hom(Z/3,Z)`.

**Verdict (a).** No GU-forced base has `H^2` 3-torsion. The escape "choose the unforced `X^4` to carry
`H^2` 3-torsion" is an **import** of exactly the same unforced class as `K3` / `CP^2` (GU fixes no `X^4`
topology). The 2-adic wall **is** structural in cohomology.

---

## (a') But the order-3 was never a cohomology object -- it is on the forced spine, in framed bordism

The wall above is real, and it is also attacking the wrong invariant. The located carrier does not live
in `H^*(RP^3)`; it lives in the **framed bordism** of the same forced spine, `pi_3^s = Z/24`:

- `|Im J_3| = denom(B_2 / 4) = denom(1/24) = 24` -- a homotopy-group order (Adams image-of-`J` /
  Bernoulli), **provenance-distinct from `chi(K3) = 24`** (the guard's two `24`s are different numbers
  with different provenance chains, both printed).
- `e_R = p_1/48 = 4/48 = 1/12` (gravitational framing; `p_1 = 4` Kirby-Melvin, **from-memory**),
  cross-checked against the Adams `e`-invariant of class 2 in `Z/24`: `2/24 = 1/12`. The two
  normalizations agree.
- `e_R = 1/12` has order **12** in `Q/Z`, 3-adic valuation of the order **= 1**: the order-3 part is
  genuinely present.

So the **forced** `RP^3` spine reaches order 3 -- via a tangential framing (the `Lambda^2_+` framing; the
GU identification is reconstruction-grade, per the paper's Section 7). This is not a cohomology escape
and does not dent the wall of (a): the carrier is a homotopy-framing datum, and by `Hom(Z/3, Z) = 0` it
is **mod-3 information, not an integer**. It cannot be the base's cohomology torsion (that is `Z/2`), and
it cannot be an integer count.

This is the crux that forbids a KILL on (a): a **GU-forced 3-base does survive** -- the `RP^3` spine in
framed bordism -- just not in the cohomology arena where the wall lives.

---

## (b) Bismut-Cheeger: does a fiber index reach `e_R`, or is `e_R` preimage-free?

Three measured facts, converging on "no built reduction reaches it":

1. **Even-fiber transparency (structural).** Pontryagin classes have degree `4i`; there is **no**
   degree-6 Pontryagin monomial (the machine-listed set is empty), so `A-hat[M^6] = 0` for *every* closed
   spin 6-manifold, a fortiori the `S^6` metric fiber; and `eta(S^6) = 0` for the round PSC metric
   (from-memory). The Bismut-Cheeger `eta`-form of an index-transparent even fiber therefore contributes
   **zero** to the `e_R` channel. The fiber-index route transmits nothing to the gravitational-framing
   carrier. (This is the computed even-fiber transparency the paper flags at Section 8 caveat (ii),
   `A-hat[S^6] = eta(S^6) = 0`, now with the *reason* -- no degree-6 characteristic number -- printed.)

2. **The boundary's own gauge eta is 2-adic.** The `RP^3 = L(2;1)` reduced Dai-Freed / gauge `eta`
   (APS/Donnelly trig sum, measured) is `xi = (-1/8, +1/8)`: denominators are powers of 2. A 3-adic
   control on `L(3;1)` gives `(-2/9, 1/9, 1/9)` (denominator 3), so the trig sum *can* be 3-adic -- it
   simply is not on `RP^3`. So `e_R = 1/12` does **not** arise from the `RP^3` boundary gauge channel; it
   lives only in the gravitational framing `p_1/48`, a different channel the fiber index does not feed.
   (This reproduces the paper's Section 7 negative control -- `RP^3`'s deck group is `Z/2`, the charge-`q`
   `eta = (2q^2-4q+1)/8` is 2-primary -- from the trig-sum side.)

3. **The decisive arithmetic.** In the APS / Bismut-Cheeger index identity
   `ind = (bulk A-hat ch) - (boundary defect)`, the transparent-fiber bulk integral is `A-hat[S^6] ch = 0`,
   so a boundary defect `e_R = 1/12` forces `ind = 0 - 1/12 = -1/12`, which is **not an integer**. There
   is therefore **no integer index whose boundary defect is `e_R`** via the available (transparent-fiber)
   reduction. The homotopy-fixedness of `e_R` (identical for any bulk) is exactly what blocks it from
   being the geometry-dependent boundary term of a genuine varying family index.

**Readout (b).** `e_R = 1/12` is a **boundary datum with no integer-index preimage** in the built
machinery. An integer-by-construction preimage requires a **relative / equivariant** twisted-RS index
whose *nonzero, geometry-dependent* bulk cancels the `1/12` mod `Z` -- precisely the unbuilt source action
of Section 9. This is the `Hom(Z/3, Z) = 0` discipline made quantitative: the only integer home for an
order-3 boundary class is a relative index, and that index is exactly the gated object.

**Constraint touchpoints (consistency, not forcing).** The reduction obstruction enters through `m^2`
(the twist appears as `rk * c_1(L)^2/2`), and every VG-V7-selected twist `m in {1, 2, 5}` has
`m^2 == 1 (mod 3)` -- so the obstruction is **sign-blind**, consistent with the 2026-07-07 alignment
result that the residual `tr(Q5 Phi^2)` alignment datum is a single sign bit living elsewhere (A4). The
Cartan = Krein = ghost-parity `Z2` seat (constraint 1) is reproduced as the `(+96, -96, 0)` anchor.

---

## Verdict and conjecture signal

**SIGNAL = GATED.**

- **(a)** The 2-adic wall is a **cohomology THEOREM**: no GU-forced base has `H^2` 3-torsion, and the
  unforced target-fits carry no torsion at all.
- **(a')** The forced `RP^3` spine nonetheless carries the order-3 carrier in **framed bordism**
  (`e_R = 1/12`), via a reconstruction-grade tangential framing. A forced 3-base survives -- in the right
  arena (homotopy), consistent with `Hom(Z/3, Z) = 0` (mod-3 info, not an integer).
- **(b)** The fiber-index reduction to an integer preimage of `e_R` is **unavailable**: transparent even
  fiber (`A-hat = 0`), 2-adic boundary gauge eta, and a fractional (`-1/12`) naive index.

**Surviving candidate + open condition (name and gate).** The GU-forced `RP^3` spine carrying the order-3
carrier in framed bordism survives, gated on **both** of:

  (i) the **relative / equivariant twisted-RS index** (integer-by-construction, geometry-dependent bulk)
  whose fractional-part cancellation gives `e_R` an integer preimage mod 3; **and**

  (ii) a **proven Bismut-Cheeger fibered-boundary reduction** for the *actual* non-product
  `S^6`-bundle-over-`RP^3` twisted-RS boundary operator (the general machinery is a theorem; its
  application to GU's operator is unbuilt), plus the reconstruction-grade identification of GU's
  `Lambda^2_+` twist with the tangential framing.

**KILL is not warranted.** The wall is a cohomology theorem, but the carrier was never a cohomology
object; a forced 3-base (in framed bordism) and a candidate reduction (the unbuilt relative twisted-RS
index) both survive. This route neither promotes nor kills Section 9's conjecture; it **sharpens the
gate**: the two non-operator bridges are now pinned -- base-forcing yields a forced homotopy 3-carrier but
never a cohomology-torsion or integer one, and Bismut-Cheeger cannot reach an integer preimage through the
transparent fiber -- so the entire open bridge collapses onto the single unbuilt object the paper already
names: the relative/equivariant twisted-RS index.

---

## Honest gaps carried

1. **From-memory analytic inputs (flagged in-script):** the Kirby-Melvin `p_1 = 4` framing normalization
   for `e_R` (mitigated by the agreeing independent Adams class-2/24 route), `eta(S^6) = 0` for the round
   PSC metric, and the *statement* of the general Bismut-Cheeger fibered-boundary theorem. The theorem's
   application to GU's actual twisted-RS operator is the unbuilt gate, asserted nowhere here.
2. **The `S^6`-bundle-over-`RP^3` model** is the paper's own schematic for the non-compact metric fiber's
   boundary geometry; the transparency argument uses only that the fiber is an even sphere
   (index-transparent), which holds for any `S^{2k}`. The precise fiber dimension and non-product
   structure are not re-derived from `GL(4,R)/O(3,1)` here.
3. **The framing identification** (GU's `Lambda^2_+` twist = the tangential `RP^3` framing carrying
   `e_R`) is reconstruction-grade, inherited from the paper's Section 7, not established here.
4. **Cohomology vs framed bordism** is the load-bearing distinction: the 2-adic wall is proved for `H^2`
   (and the `RP^n` tower); the escape into `pi_3^s = Z/24` is where the order-3 lives, and this route
   locates it there but does not build the integer bridge out of it.
5. **Internal tier only:** computed and self-adversarial (measured torsion, non-vacuity controls, exact
   rational eta arithmetic), not externally replicated or peer-reviewed.

## Governance

Exploration-grade; **no paper edit made** (the frozen `located-not-forced` paper is not touched). A
promote/kill outcome would be a proposal for Section 9; this route returns **GATED**, so the proposal is:
record, under Section 9, that the two non-operator bridges are pinned (base-forcing gives a forced
*framed-bordism* 3-carrier on `RP^3` but no cohomology-torsion or integer one; Bismut-Cheeger cannot reach
an integer `e_R`-preimage through the transparent even fiber), collapsing the open bridge onto the single
unbuilt relative/equivariant twisted-RS index. This pauses for the maintainer. The generation-count
verdict is unchanged: **OPEN**.
