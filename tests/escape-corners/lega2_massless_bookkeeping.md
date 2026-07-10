# LEG-A2 — CORNER (a), leg 2: the massless-limit bookkeeping, computed

**Leg of:** corners-swing (the two PARTIAL corners of the carrier-bit decision campaign,
`canon/carrier-bit-decision-campaign-RESULTS.md`). This leg addresses CORNER (a) — the
massless-chiral corner — from the mass-mechanism side: which states go light in the
decreased-VEV limit, what spin are they, and does the generation-count structure need light
chiral spin-3/2 at all?

**Runnable checklist:** `LEG-A2-massless-bookkeeping.py` — **81/81 checks, exit 0**
(run 2026-07-10, serial, single process; exact `Fraction`/sympy arithmetic only; every quoted
claim needle-verified against its source file at run time).

**Grade:** toy + substrate-proxy + rep-arithmetic + cached-verbatim theorem hypotheses.
**Not a verdict on the carrier bit** — SG4 (the unbuilt source action's field-space
declaration) stays the sole decider, per canon. This leg only decides what the MASS
BOOKKEEPING does and does not force.

**Story-shopping guard (inverted):** the exciting outcome here is corner-CLOSED. The
strongest corner-OPEN case is therefore computed and carried in §4(d) and §6, not
strawmanned.

**Firewall (DEAD-ENDS.md):** clean. Â(K3) = −σ/8 = 2 computed from σ = −16 only (asserted
≠ 3); no χ(K3), no /8 manufacture; the bare commutator 58.72 appears only as the
nonvanishing-couplings PREMISE (cited, never computed with, never reduced).

---

## 0. Inputs (all needle-verified verbatim at run time)

**Transcript** (`papers/drafts/Transcript into the impossible.md`):

- [00:40:27] "in g u, there's one family of 16 flipped chiral spin three halves particles.
  That is, there is a sort of spin three halves family, which aside from being spin three
  halves is just the conjugate of the internal symmetry representation."
- [00:39:18] (the three-reasons-unseen passage, immediately preceding) "It's too massive and
  you haven't gotten enough energy to see it yet."
- [00:46:02] "the fermionic extension gives you exactly three families of chiral fermions if
  you have a decreased VEV in the total space taking a Dirac equation into two vial [Weyl]
  equations because the mass is actually a variable."
- [00:39:18] "Rarita v tensor spinners on w, spinners on v, tensor Rarita Schwinger on w or
  tensor Rarita Schwinger on w plus spinners on v, tensor spinners on w. So that's where you
  get your third generation of matter from."
- [00:36:13] "which will yield you three families, really two plus one. The third family is
  an imposter for representation theoretic reasons, but at low energy, it'll look the same as
  the other two."
- [00:38:09] "these three representations are exactly what we now see in the standard model."
- [00:46:02] "We will never find space time Susie."

**Substrate/canon** (needled): capstone SW mass spectrum `{+64, 0:64, -64}` (the 2+1 split);
carrier vectorlike, "Krein signature exactly (+96, -96)"; "decouples to ZERO net chiral
generations, not three"; on-shell background nonzero `|mu| = 123.08`; SW seesaw refutation
"(slope 1.000), not seesaw t^2"; vectorlike Majorana block 391.027; carrier = "the pure
Spin(10) generation spinor (16/16bar), vectorlike (96/96)". Adjudication: "[B] - [A] =
2([S+]-[S-])" and the order-3 class lives "Entirely in the orientation of the rank-2
spin-1/2 slot".

**Theorem hypotheses** (cached fetches, needled): Grisaru–Pendleton PLB 67 (1977) 323,
abstract verbatim (cache: `carrier-bit-swing/LEG-1-applicability-matrix.py`, cross-needled
against repo `tests/carrier-bit-decision/leg1_applicability_matrix.md`):

> "If massless fermions of spin 3/2 have non-vanishing low-energy couplings, the fermions
> must have massless partners of spin 2, and all particles to which the fermions couple must
> display supersymmetry."

Title (needled): "Soft Spin 3/2 Fermions Require Gravity and Supersymmetry" — a SOFT-limit
(S-matrix) theorem; leg-1's regime row "S-matrix soft limit" needled. Homma–Semmelmann
(cache `symbol-swing/hs_paper.txt`): "ind Q = dim kerQ+ − dim kerQ−" (the definitional
line); eq (11) "(ch(TM C) + 1)[M] = ind DT M + ind D"; Prop 3.1(i) "ind Q = − 19 ˆA(M)";
Rem 3.6 "discarding zero modes that ca[n] be gauged away". PTZ PRD 106 (2022) 025022
(cache `carrier-bit-swing/ptz-rsa.txt`): "−19 = −21 + 2. (5.1)".

---

## 1. Exact rep bookkeeping: GU's stated fermion content has exactly 3 spin-1/2 family slots and exactly 1 spin-3/2 family slot

GU's linearized fermion content is spinor-valued zero- and one-forms ([00:49:16]:
"zero forms and one forms valued either in add or in the spinners"). Under the 14 = 4 + 10
split (all complex dims of Weyl pieces, computed exactly):

- 4d: V4 ⊗ S4L = (1,1/2) ⊕ (0,1/2), i.e. 8 = 6 + 2, with the gamma-trace (spin-1/2) part
  **flipping 4d chirality** — computed from SU(2)×SU(2) tensor arithmetic, matching the
  published Bär–Mazzeo chirality reversal the adjudication rides.
- internal: 10 × 16 = 160 = 144 + 16 (the trace part is the conjugate 16bar — standard
  SO(10) branching, Slansky Phys. Rep. 79 (1981); dimension identity checked exactly).
- S14 Weyl: 64 = 2·16 + 2·16 (S14+ = S4L⊗16 ⊕ S4R⊗16bar).
- Ω¹(S14+) closes exactly: 14·64 = 896 = 192 (RS4⊗S10-type) + 64 (4d-trace) + 64
  (internal-trace) + 576 (S4⊗144 dark).
- **The transcript's RS product rule [00:39:18], made exact:** dim RS(V⊕W) = 896 − 64 = 832
  = 192 [RS(V)⊗S(W)] + 576 [S(V)⊗RS(W)] + 64 [the ADDED S(V)⊗S(W) term] — the "slightly
  more complicated rule that looks vaguely like a product rule," with the third-generation
  slot being exactly the ADDED 64 (= 4d-trace 64 + internal-trace 64 − the one diagonal 14d
  gamma-trace 64).

**Family census per Weyl half** (a "16-family" = one Weyl-fermion unit in internal 16/16bar):

| slot | 4d spin | internal | 16-unit chirality |
|---|---|---|---|
| Ω⁰ | **1/2** | 16 | +1 |
| 4d-trace | **1/2** | 16bar | −1 |
| internal-trace (the ADDED term = the imposter) | **1/2** | 16bar | −1 |
| RS4⊗S10 | **3/2** | 16-type | (multiplicity 1) |
| S4⊗144 | 1/2 | 144 (dark) | — |

Machine-asserted consequences:

1. **Exactly 3 spin-1/2 16-families; exactly 1 spin-3/2 16-family** ("one family of 16",
   [00:40:27]). All three family slots are spacetime **spin-1/2**; the spin-3/2 slot is NOT
   one of the three. 3·16 = 48 = one-generation SM content ×3 (with RH neutrino).
2. **The spin-3/2 slot cannot carry the family count:** its multiplicity is 1 ≠ 3.
3. **The internal-chirality split of the three is 2 + 1** — the exact-arithmetic shadow of
   [00:36:13] "really two plus one."
4. **Net 16-chirality per Weyl half = −1, and 0 over the full S14** — multiplicity-3 is not
   net-3; the full content is vectorlike. This is an independent rep-arithmetic match to the
   capstone's *measured* (+96, −96) net-0 — two different routes, same vectorlike verdict.

## 2. The toy seesaw / VEV-split spectrum, exact

Substrate anchor: the SW mass operator on the 192-dim j=1 carrier is `M·Jz` per 64-fold
spin-1 triplet (spectrum `{+64, 0:64, -64}`, M = |F0|, on-shell |mu| = 123.08 ≠ 0), plus the
VEV-controlled gen↔mirror Dirac leg of scale v ("the mass is actually a variable").

**T1 (weight-diagonal Dirac leg):** H₁ = [[M·Jz, v·I₃],[v·I₃, M·Jz]]. Exact spectrum
{M±v, ±v, −M±v}.

- The **light states are exactly the zero-weight (w=0) slot** — the '0:64' third of
  {+64, 0:64, −64} (light fraction 2/6 = 64/192 = 1/3, exact); eigenvectors have exactly
  zero overlap with the w=±1 slots.
- Their mass is **±v: LINEAR in the VEV (slope 1, exact)** — the light pair is a Dirac pair
  splitting into **two Weyl of opposite chirality** as v→0 (net chirality 0). This is the
  transcript's [00:46:02] mechanism ("a Dirac equation into two [Weyl] equations")
  reproduced in exact arithmetic, and it reproduces the SW campaign's slope-1.000
  seesaw-refutation exactly (control: [[0,v],[v,M]] light eigenvalue = −v²/M + O(v⁴),
  slope 2).
- The **heavy two-thirds stay at M as v→0** — the heavy scale is VEV-independent.

**T2 (su(2)-algebra background leg):** blocks M·Jz ± v·Jx have exact spectrum
{0, ±√(M²+v²)} — the spin-1 weight diagram always has a zero weight, so the light state is
**exactly massless for ALL v** (a modulus), limiting to the w=0 slot as v→0
(overlap fraction M²/(M²+v²) → 1, exact) and still net-chirality 0.

**The three decreased-VEV branches (exact):** (1) v→0, M fixed: light = w=0 slot only, 2/3
heavy at M; (2) M→0, v fixed: all six masses = |v|, nothing exactly massless, net 0;
(3) both→0: all masses vanish **only at the exact origin (M,v) = (0,0)**. The light mass
|±v| = 0 **iff v = 0 exactly** — the massless point is measure-zero in the mass modulus.
These are canon's two capstone poles (massless flat modulus / massive decoupled), reproduced
exactly, with net chirality 0 at every point of every branch.

## 3. Spin content of the light states — the decisive question, answered

Honest gap first: the toy's weight labels are NOT 4d spin labels; the 14d→4d effective
identification is UNBUILT (leg-1's carried PARTIAL corner). What is exact and stated:

- The generation-count structure is carried by the **three spacetime spin-1/2 slots** (§1),
  which the transcript itself identifies with observed SM content ([00:38:09]) — spin-1/2.
- The spin-3/2 slot is **one family**, which the transcript places in the un-seen /
  "too massive" bin ([00:39:18]–[00:40:27]).
- Exhaustive placement of the spin-3/2 slot in the toy: **case H** (w=±1): heavy at M for
  all v — massless only if M→0 too (the exact origin); **case L** (w=0): mass ±v — massless
  only at v = 0 exactly. **In both cases a massless interacting spin-3/2 requires an exact
  point of the mass moduli, never a generic point.**

**Answer to the decisive question: the generation-count structure needs only light chiral
spin-1/2; the spin-3/2 sector staying heavy is fully consistent with every stated GU number
(3 families × 16; one spin-3/2 family of 16; 2+1 imposter split), and nothing in the stated
mechanism or the built proxy forces the spin-3/2 light.** Reading (ii) of the corner (light
chiral = spin-1/2 SM fermions, spin-3/2 stays heavy) is realized by the computed bookkeeping;
reading (iii) (a required massless chiral spin-3/2 sector) is FORCED BY NOTHING at this grade.

## 4. The corner-open steelman, computed precisely

**(a) The index table (exact, firewall-clean):** σ(K3) = −16, p1 = 3σ = −48, Â = −σ/8 = 2.
ind_A = 21σ/8 = −42; ind_B = 19σ/8 = −38; bare = 5p1/6 = −40; double-subtraction = 11p1/12
= −44; reversed-D = −2. Additivity −40 − (−2) = −38 (HS eq (11), needled). Fork
−38 − (−42) = 4 = 2·ind(D). Order-3 residues (0,1,2,1) — matching the adjudication exactly.

**(b) What the index counts when the physical spectrum is massive:** the needled HS
definitional line — ind Q = dim ker Q⁺ − dim ker Q⁻ — is kernel chirality of the FIBER
operator: **UV field-content (K-class) data, mass-blind**. Finite-dimensional exact model:
for T(m): ℚ³ → ℚ², ind = dim ker − dim coker = dim V⁺ − dim V⁻ = 1 at m = 0, 1, 5 (pure
field content, mass-independent), while the massless-mode count changes (3 at m = 0; 1 at
m ≠ 0). **The index is not an IR massless-state count.** When the spectrum is massive, the
−38/−42 survive as anomaly coefficients (PTZ "−19 = −21 + 2", needled — an anomaly statement
about field content) and as deformation-invariant K-class/eta data — exactly the registers
the adjudication computed. The index's mass-insensitivity therefore cuts AGAINST the
corner-open reading: it means the −38/−42 arithmetic and the order-3 classes survive the
spin-3/2 being heavy; they never needed massless spin-3/2.

**(c) Which 4d spin the fiber indices attach to (any fibered/KK reading):** a 4d field's
spacetime spin comes from the 4d factor, its multiplicity from the fiber operator on its
internal content. The 4d spin-3/2 slot (RS4⊗S_F) carries internal content S_F → fiber Dirac
operator, |ind| = 2. The generation arena (S4⊗RS_F) carries internal RS content → the
−38/−42/−40 fork. **The entire carrier fork is two spin-1/2 units ([B]−[A] = 2([S⁺]−[S⁻]),
needled) and its order-3 content rides the spin-1/2 slot (adjudication LEG-D, needled):
in every reading the generation arena is a 4d SPIN-1/2 slot.** The 4d spin-3/2 slot's index
has magnitude 2: ≠ 3 (not the family count) and its masslessness is not implied by any
index in the table.

**(d) The strongest surviving corner-open strand (carried, not hidden):** IF the unbuilt
fibered geometry implements standard KK chirality pairing on the spin-3/2 slot, the nonzero
fiber Dirac index (|2|) would force net-2 exactly-massless, chirality-PROTECTED, interacting
4d spin-3/2 states ("lots of them won't be [electrically neutral]", [00:40:27]) — and GP
re-engages with full force. Machine-asserted tension: pairing requires net 2 in that slot;
the built substrate MEASURES net 0 (vectorlike, needled). The strand survives only by
overturning the measured proxy via the unbuilt 14d→4d identification — SG4-adjacent, named,
open.

**(e) GP applicability logic (the IR point):** GP is a soft-limit S-matrix theorem (title
"Soft Spin 3/2 Fermions Require Gravity and Supersymmetry"; hypothesis predicate = "massless
fermions of spin 3/2 [with] non-vanishing low-energy couplings" — a predicate on the IR
asymptotic spectrum). Machine-asserted: GP does **not** engage on a massive spin-3/2
spectrum regardless of the UV index value (−42, −38, or −40); GP **does** engage at an exact
massless-spin-3/2 point with couplings on (the firewall keeps couplings nonzero — the escape
is only via mass, never decoupling). Caveat carried honestly: the GP full text is unfetched
(paywalled); the IR classification rides the verbatim abstract + title + leg-1's regime row,
i.e. abstract-tier.

## 5. Verdict (this leg)

**CORNER (a) CLOSES at this leg's grade.** The decreased-VEV mechanism lights the zero-weight
third of the carrier as Dirac pairs → two Weyl (slope 1 exact; or an exact zero-weight
modulus under su(2)-algebra backgrounds), always with net chirality 0; the generation-count
structure is carried by exactly three spacetime spin-1/2 slots (the spin-3/2 slot has
multiplicity 1 and fiber-index magnitude 2 — neither is 3); the −38/−42 index arena attaches
to a 4d spin-1/2 slot in any fibered reading and, being mass-blind UV data, survives a heavy
spin-3/2 sector without needing massless states; and GP's hypothesis reads the IR spectrum,
which GU-as-stated populates with massive spin-3/2 ("too massive"; mass a modulus; on-shell
proxy background nonzero). **Nothing computed or stated forces an exactly-massless
interacting spin-3/2** — readings (i)/(ii) suffice for everything GU says; reading (iii) is
an unforced import.

## 6. The strongest surviving corner-OPEN case (the inverted guard's deliverable)

1. **The KK-pairing strand (§4d):** the fiber Dirac index |2| ≠ 0 plus a chirality-pairing
   fibered geometry would force net-2 protected massless interacting 4d spin-3/2 → GP
   re-engages → tilt flips toward carrier A or the GU-inconsistent fourth outcome. Blocked
   by: the unbuilt 14d→4d identification, and in measured tension with the vectorlike
   substrate (net 0). Not excluded by any built object.
2. **The exact-origin strand (§2–3):** no stated GU mechanism excludes the exact point
   (M,v) = (0,0) where the whole carrier — including the spin-3/2 slot — is massless while
   still coupled (58.72 premise). GP engages there. Weighed against: the author's own
   placement of the physical point ("too massive... haven't gotten enough energy"), the
   modulus reading ("the mass is actually a variable"), and the on-shell proxy's nonzero
   condensate — but "disfavored by author statements" is not "excluded by a built object."

Both strands ride SG4-adjacent unbuilt objects; neither is a computed fact about
GU-as-stated. That is exactly why this leg closes the corner at ITS grade and no higher.

## 7. Named missing inputs (BLOCKED items)

1. The 14d→4d effective identification (which weight/slot carries the 4d spin-3/2; whether
   any KK chirality pairing exists) — unbuilt, SG4-adjacent.
2. GP full text (paywalled; abstract + title tier for the IR/S-matrix classification).
3. Any stated GU mechanism placing or excluding the exact massless origin of the mass moduli
   — none exists in the transcript; only the author's "too massive" placement.
4. The fibered geometry required by the families criterion (adjudication's own caveat) —
   the fiberwise −38 is not a families-criterion pass, and nothing here changes that.

## 8. Sources

- `papers/drafts/Transcript into the impossible.md` — timestamps [00:36:13], [00:38:09],
  [00:39:18], [00:40:27], [00:46:02], [00:49:16]; all needled this run.
- `canon/carrier-dirac-mass-capstone-RESULTS.md` — {+64, 0:64, −64}; (+96,−96); decouples to
  zero; |mu| = 123.08; needled.
- `canon/source-action-seiberg-witten-RESULTS.md` — slope 1.000 not seesaw t²; 391.027;
  generation spinor 16/16bar vectorlike; needled.
- `canon/gamma-traceless-38-adjudication-RESULTS.md` — [B]−[A] = 2([S⁺]−[S⁻]); order-3 class
  in the spin-1/2 slot; index table; needled.
- Grisaru & Pendleton, PLB 67 (1977) 323 — abstract verbatim via cached InspireHEP fetch
  (`carrier-bit-swing/LEG-1-applicability-matrix.py`), cross-needled in
  `tests/carrier-bit-decision/leg1_applicability_matrix.md`.
- Homma & Semmelmann, arXiv:1804.10602 — cached `symbol-swing/hs_paper.txt`; index
  definition, eq (11), Prop 3.1(i), Rem 3.6; needled.
- Prokhorov, Teryaev & Zakharov, PRD 106 (2022) 025022 — cached
  `carrier-bit-swing/ptz-rsa.txt`; eq (5.1) "−19 = −21 + 2"; needled.
- Slansky, Phys. Rep. 79 (1981) — SO(10) branching 10×16 = 16bar ⊕ 144 (conjugation of the
  trace part; dimension identity computed exactly in-script; conjugation cited, unfetched).
- `absorbed/gu-source-action/DEAD-ENDS.md` — firewall, complied with.
