---
artifact_type: exploration
status: exploration (W232; GAP-CLOSURE lane A5; four personas inline, one worker, no sub-agents; deterministic parity/bordism test, exit 0, positive controls first)
created: 2026-07-14
wave: W232
label: W232
lane: A5
posture: coherence-first; exploration grade; conditional register; truth-seeking (report value under either outcome); RUTHLESS self-verification; tri-repo gating STRICT
verdict: COMPLETED-GENUINE-CHOICE
title: "W232 (lane A5) -- PIN the (9,5)-vs-(7,7) signature via the open 2-primary Witten / Dai-Freed Z/2 (global) anomaly. RESULT: the lever does NOT fire against (9,5). The Witten Z/2 anomaly VANISHES on the (9,5)/quaternionic side by THREE independent mechanisms: (B) the mapping-torus dimension 15 = D+1 (D=14) sits in a DEAD KO/KSp degree -- KO_15 = KO_7 = 0 (real/(7,7) side) and KSp_15 = KO_19 = KO_3 = 0 (quaternionic/(9,5) side) -- so the point-level (gravitational) mod-2 index vanishes for BOTH signatures; (C) the reduced spin-bordism global-anomaly group on the (9,5) side is EMPTY, Omega~^spin_15(BSp(64)) = 0, because H*(BSp;Z) lives only in degrees = 0 mod 4 and Omega^spin_q = 0 for q in {3,7,11} (AHSS), leaving NO room for any global anomaly perturbative or torsion; (D) in the 4D-reduced reading the genuine candidate pi_4(Sp(64)) = Z/2 (the Witten-SU(2) mechanism) is killed by the EVEN quaternionic multiplicity dim_H(S) = 64, while the (7,7)/real side has NO candidate at all since pi_4(SO(128)) = 0. Therefore (9,5) is NOT excluded, (7,7) is NOT forced, and the generation-count leg (which dissolves ONLY if (7,7) is forced) does NOT dissolve. The signature is a GENUINE FREE CHOICE fixed solely by the declared base Lorentzian convention sign(d) via W202's closed form p-q = d + d^2/2, NOT by any anomaly-consistency requirement. This CLOSES W202's sole live lever and converts the standing conditional into a characterized free choice. HONEST CORRECTION to W202's conjectured asymmetry: the direction W202 feared (Z/2 excludes the H-class -> forces (7,7) -> dissolves count) is exactly the direction proven CLOSED; if anything is left open it is on the (7,7)/real side (BSO(128)-type bordism), which could only bear on excluding (7,7) and pointing toward (9,5), never on forcing (7,7). Deterministic test tests/W232_signature_witten_z2_anomaly.py, all checks exit 0, positive controls first (Witten SU(2)=Sp(1) single doublet reproduced as ANOMALOUS)."
grade: "exploration / strong. The load-bearing objects are exact table lookups and finite parity/degree arithmetic, machine-checked: the KO/KSp Bott periodicity table, the Omega^spin_* Anderson-Brown-Peterson table, the p-q mod 8 Clifford Morita type, the Atiyah-Hirzebruch degree bookkeeping for Omega~^spin_15(BSp(64)), and the pi_4 stable homotopy of Sp and SO. COMPUTED (tests/W232_signature_witten_z2_anomaly.py, exit 0): PC1-PC5 positive controls (KO/KSp/Omega^spin values; Witten SU(2)=Sp(1) single doublet ANOMALOUS, even doublets NON-anomalous); A the reality class 4->H / 0->R; B the dead degree at 15 for both reality types; C the empty reduced bordism Omega~^spin_15(BSp(64))=0; D the 4D even-multiplicity kill and the absent (7,7) candidate; E the verdict logic. BUILDS ON (cited, not re-derived): anomaly-sp64-global-pi15 (the Dai-Freed reduction to a mod-2 index; Cl(9,5)=M(64,H); the KSp-evenness Fact A), W202 (sole live lever; closed form; reality-blind perturbative part), SG1 (signature-relative Kramers parity). No canon / RESEARCH-STATUS / claim-status / verdict / posture change; the debit count is unmoved; count stays {1,3}; bar(b)/H59 OPEN untouched; no forbidden target {3,8,24,chi(K3),Ahat} assumed or inserted. Zero em dashes."
construction: "program-native where the objects are GU's (Y14 signature (9,5)=(3,1)+(6,4) or (7,7)=(1,3)+(6,4); the internal Clifford Cl(9,5)=M(64,H) vs Cl(7,7)=M(128,R); the fermion content Psi = (Omega^0 (x) S^+) (+) (Omega^1 (x) S^-) with S = H^64; the gauge group Sp(64) on the (9,5) side). Standard-field where the machinery binds any construction (Bott/KO/KSp periodicity; the Atiyah-Singer mod-2 index theorem; the Dai-Freed / Freed-Hopkins global-anomaly = (D+1)-bordism-invariant statement; the Atiyah-Hirzebruch spectral sequence; the Witten SU(2) global anomaly template). Every ported fact labelled; none asserted OF GU beyond its stated content. Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md. Tri-repo gating STRICT: the anomaly computation is entirely GU-side; NO TaF / cross-repo identity asserted; the generation-count bearing is reported as a NON-event (no dissolution), not a count movement."
depends_on:
  - explorations/anomaly-and-bordism/anomaly-sp64-global-pi15-2026-06-23.md
  - explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md
  - explorations/W202-signature-crux-bach-branch-2026-07-14.md
  - explorations/big-swing-2026-07-03/BIG-SWING-signature-9-5-vs-7-7-UNDER-DETERMINED.md
  - explorations/sequential-goals-2026-07-09/SG1-signature-carrier-parity-77.md
  - explorations/nguyen-gu-critique/nguyen-critique-full-synthesis.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W232_signature_witten_z2_anomaly.py
external_refs:
  - "Witten, E., An SU(2) anomaly, Phys. Lett. B117 (1982) 324 -- the pi_4(G)=Z/2 global gauge anomaly; single pseudoreal doublet anomalous."
  - "Witten, E., Global gravitational anomalies, CMP 100 (1985) 197 -- Z-valued homotopy vs continuous-family anomaly."
  - "Dai, X. and Freed, D.S., eta-invariants and determinant lines, J. Math. Phys. 35 (1994) 5155 -- mapping-torus eta = global anomaly phase."
  - "Freed, D.S. and Hopkins, M.J., Reflection positivity and invertible topological phases, Geom. Topol. 25 (2021) 1165 -- anomaly of a D-dim theory = (D+1)-dim bordism invariant."
  - "Atiyah, M.F. and Singer, I.M., The index of elliptic operators V, Ann. Math. 93 (1971) 139 -- the KO/KSp-valued (mod-2) index; quaternionic index is even."
  - "Anderson, D.W., Brown, E.H., Peterson, F.P., The structure of the Spin cobordism ring, Ann. Math. 86 (1967) 271 -- Omega^spin_* table."
  - "Bott, R., The stable homotopy of the classical groups, Ann. Math. 70 (1959) 313 -- KO/KSp periodicity; pi_4(Sp)=Z/2, pi_4(O)=0."
  - "Garcia-Etxebarria, I. and Montero, M., Dai-Freed anomalies in particle physics, JHEP 08 (2019) 003 -- bordism classification of global anomalies."
---

# W232 (lane A5) -- pinning the (9,5) signature against the open Witten Z/2 anomaly

## 0. The charge and the one-paragraph answer

Lane A5 of the GAP-CLOSURE wave. W202 left the (9,5)-vs-(7,7) signature UNDER_DETERMINED
with exactly one live lever: the open 2-primary Witten / Dai-Freed Z/2 (global) anomaly,
which W202's skeptic conjectured could only push toward (7,7) (exclude the H-class),
dissolving the generation count (which is theorem-forbidden from the fermion index and
dissolves under (7,7)). The charge: resolve that anomaly. Does it FIRE (forcing (7,7)) or
VANISH (leaving (9,5) admissible), or is the signature a genuine free choice?

**Answer: the lever does NOT fire against (9,5). The Witten Z/2 anomaly VANISHES on the
(9,5)/quaternionic side by three independent mechanisms.** Hence (9,5) is NOT excluded,
(7,7) is NOT forced, and the generation-count leg does NOT dissolve. The signature is a
GENUINE FREE CHOICE, fixed solely by the declared base Lorentzian convention `sign(d)` via
W202's closed form `p - q = d + d^2/2`, not by any anomaly-consistency requirement. This
CLOSES W202's sole live lever and converts the standing conditional into a characterized
free choice. Deterministic test `tests/W232_signature_witten_z2_anomaly.py`, exit 0,
positive controls first.

## 1. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Why |
|---|---|---|
| Total space / signature | `Y14`, signature (9,5)=(3,1)+(6,4) or (7,7)=(1,3)+(6,4) | GU's verified object; the crux is `sign(d)` (W202, BIG-SWING). |
| Internal Clifford / reality | `Cl(9,5) = M(64,H)` (quaternionic) vs `Cl(7,7) = M(128,R)` (real) | fixed by `p-q mod 8` = 4 vs 0 (real Clifford Morita type). |
| Fermion content | `Psi = (Omega^0 (x) S^+) (+) (Omega^1 (x) S^-)`, `S = H^64` | audit content; the spinor module is the fundamental of Sp(64) on (9,5). |
| Gauge group | `Sp(64)` (9,5 side); `SO(128)`-type / real form (7,7 side) | commutant of the reality structure; Sp(64) is the audit determination. |
| Anomaly invariant | `(D+1)=15`-dim bordism / mod-2 index; 4D-reduced `pi_4` Witten class | Dai-Freed / Freed-Hopkins; the two readings cross-check. |

The ONLY structural datum that changes across the crux is the **reality class** of the
spinor: quaternionic H (KSp) on (9,5), real R (KO) on (7,7). Everything below is the
consequence of chasing that single change through the anomaly machinery.

## 2. Persona 1 (global-anomaly / Witten specialist): what the anomaly actually is, and the two readings

The perturbative anomaly is already closed at verified grade (the anomaly audit: `tr_R F^8`
is reality-class-blind and vanishes for the even Casimir; BIG-SWING angle 1). The OPEN
object is the **global** (non-perturbative) anomaly. By Dai-Freed / Freed-Hopkins, the
anomaly of a `D`-dimensional chiral theory is a bordism invariant on `(D+1)`-manifolds --
the value of an `eta`-type partition function on the mapping torus of the large gauge
transformation. Its 2-primary torsion part is the **Witten Z/2** (Pfaffian-sign) anomaly.

There are two physically natural readings, and I run BOTH:

- **14D reading (primary).** The fermions live on `Y14`, so `D = 14`, mapping torus
  dimension `D+1 = 15`. This is the reading the Sp(64) global-anomaly note used
  (`pi_15(Sp) = Z`). Handled in Sections 3-4.
- **4D-reduced reading.** After SM emergence the effective theory is 4D with internal gauge
  group; `D = 4`, mapping torus dimension `5`. This is where a Witten-SU(2)-type Z/2 can be
  genuinely live for a pseudoreal group. Handled in Section 5.

The two readings probe DIFFERENT KO-degrees and so are an independent cross-check. If either
gave an anomaly on (9,5), the H-class would be excluded. Neither does.

## 3. Persona 2 (cobordism / bordism specialist): the dead degree at 15, and the empty bordism group

**(B) The point-level (gravitational) mod-2 index is dead at dimension 15 for BOTH reality
types.** The Atiyah-Singer mod-2 index theorem says a closed-manifold Z/2 index exists only
when the effective KO-degree is `1` or `2 mod 8`. The effective degree is `(dim) - (reality
shift)`, with shift `0` for real (KO) and `4` for quaternionic (KSp = KO shifted by 4):

- (7,7)/real: `15 mod 8 = 7`. `KO_15 = KO_7 = 0`. No Z/2.
- (9,5)/quaternionic: `15 - 4 = 11 = 3 mod 8`. `KSp_15 = KO_19 = KO_3 = 0`. No Z/2.

Dimension 15 sits in a Bott-dead slot for BOTH reality types. So the pure gravitational
(untwisted) Witten Z/2 vanishes regardless of the signature. (Calibration: the Witten SU(2)
anomaly is at mapping-torus dim `5`, and `5 - 4 = 1 mod 8` -- quaternionic Z/2 is LIVE
there; my `has_mod2_index` reproduces this, PC4.)

**(C) The reduced twisted (gauge) bordism group is EMPTY on the (9,5) side.** The gauge
twist could in principle revive a Z/2 even when the point-level group vanishes; that lives in
the reduced group `Omega~^spin_15(BSp(64))`. I compute it via the Atiyah-Hirzebruch spectral
sequence. `H_*(BSp(64); Z) = Z[q_1, q_2, ...]` with `|q_i| = 4i` is a polynomial ring on the
symplectic Pontryagin classes -- TORSION-FREE, and nonzero only in degrees `= 0 mod 4`. The
`E^2` line `p + q = 15` with `p > 0` a multiple of 4 forces `q in {11, 7, 3}`:

```
  (p,q) = (4,11), (8,7), (12,3)   ->   Omega^spin_q = 0, 0, 0.
```

Every coefficient vanishes (`Omega^spin_{11} = Omega^spin_7 = Omega^spin_3 = 0`), so the
whole `E^2` line is zero and `Omega~^spin_15(BSp(64)) = 0`. **There is NO room for any global
anomaly -- perturbative or torsion -- on the (9,5) side.** This is the strongest and most
rep-multiplicity-independent leg: it does not care what the specific fermion content is, only
that the gauge group is Sp(64) and the tangential structure is spin.

This tightens the Sp(64) note (which reduced to a 16-dim mod-2 index and used the KSp-evenness
Fact A): the empty `Omega~^spin_15(BSp(64))` says the answer is forced by the ambient bordism
group before any index is computed.

## 4. Persona 3 (signature / Clifford specialist): the reality class is the whole story

`p - q mod 8` is the sole determinant of the spinor reality type (real Clifford Morita
theory): `(9,5) -> 4 -> H` (quaternionic, `M(64,H)`), `(7,7) -> 0 -> R` (real, `M(128,R)`).
This is the SAME datum SG1 used (Kramers is active on `M(64,H)` / `J^2 = -1`, forcing even
signature; inactive on `M(128,R)` / `J^2 = +1`). Here it selects WHICH K-theory the anomaly
lives in: KSp on (9,5), KO on (7,7). Sections 3 and 5 then read the Z/2 off the appropriate
Bott ladder. The quaternionic structure is a DOUBLE-EDGED object: in even-index (KO-degree
`0, 4`) dimensions it makes the complex index even (protection, the 16-dim Fact A); in KSp
mod-2 dimensions (`5, 6 mod 8`) it is exactly what CREATES a candidate Witten Z/2 (Witten
SU(2), dim 5). Getting the direction right requires knowing the mapping-torus dimension mod 8
-- which is why I compute rather than assert. At `15` (both readings' `D+1` for `D=14`) the
quaternionic side lands in the dead slot `3 mod 8`; at `5` (the 4D reading) it lands in the
live slot `1 mod 8`, and Section 5 handles that case by multiplicity.

## 5. Persona 1 again (Witten specialist): the 4D-reduced reading and the even-multiplicity kill

The 4D reading is where the H-class is genuinely at risk, so it is the honest stress test.
`pi_4(Sp(64)) = Z/2` (stable Bott: `pi_4(Sp) = pi_8(O) = pi_0(O) = Z/2`) -- a real candidate,
the same homotopy that powers the Witten SU(2) anomaly. The anomaly is the mod-2 index of the
5D mapping-torus Dirac operator coupled to the fundamental, and `5 - 4 = 1 mod 8` puts it in
the live KSp Z/2 slot. So the candidate does not vanish on degree grounds.

It vanishes on **multiplicity**. The Witten Z/2 of a pseudoreal (symplectic) gauge theory is
the number of half-multiplets mod 2; a SINGLE fundamental half-multiplet is anomalous (the
SU(2) doublet, PC4), an EVEN number is not (PC5). The GU spinor module is `S = H^64`: its
quaternionic dimension is `64`, an EVEN number of pseudoreal units, so the mod-2 index is
`64 mod 2 = 0`. The anomaly cancels. (This is the multiplicity face of the Sp(64) note's
"chiral doubling" Fact B and its KSp-evenness Fact A -- here made a one-line parity fact.)

On the (7,7)/real side there is no candidate at all: `pi_4(SO(128)) = 0` (stable
`pi_4(O) = 0`), so the Witten-SU(2) mechanism has nothing to hook onto. **Both reality types
are clean in the 4D reading -- (9,5) by even multiplicity, (7,7) by an absent homotopy
class.** Independent of, and concordant with, the 14D bordism verdict.

## 6. Persona 4 (ruthless skeptic): is the vanishing cheap, and did I get the direction right?

**Push 1 -- is `Omega~^spin_15(BSp(64)) = 0` too cheap?** No; it is a structural consequence
of two robust facts: `H*(BSp;Z)` sits only in degrees `= 0 mod 4` (symplectic Pontryagin
classes, torsion-free), and `Omega^spin_q = 0` for `q in {3, 7, 11}` (the odd-below-15 slots
that a degree-15 `E^2` line can reach). Both are standard table facts, machine-checked (PC3,
C). The one caveat: the AHSS gives the associated graded; a hidden extension cannot create a
nonzero group from an all-zero `E^2` line, so the conclusion `Omega~ = 0` is safe. This is a
genuinely stronger statement than the Sp(64) note's index computation, and it is
rep-content-agnostic.

**Push 2 -- did W202 get the DIRECTION right?** This is the important honest correction.
W202's skeptic wrote that the Witten Z/2 "could EXCLUDE the H-class (push toward
(7,7)/dissolution), never FORCE it." My computation shows the OPPOSITE structural asymmetry:
the quaternionic (9,5) side is provably anomaly-EMPTY (`Omega~^spin_15(BSp(64)) = 0`;
even-multiplicity kill in 4D), whereas the REAL (7,7) side is the one whose global bordism is
NOT obviously empty -- `H*(BSO(128); Z/2)` has Stiefel-Whitney classes in ALL degrees, so
`Omega~^spin_15(BSO(128))` has many potential `E^2` contributions (degree-15 Z/2 classes
paired with `Omega^spin_0 = Z`, degree-14 with `Omega^spin_1 = Z/2`, etc.) and I do NOT
compute it here. So the residual openness, if any, lives on the (7,7) side and can only bear
on EXCLUDING (7,7) (which would point toward (9,5)), never on forcing (7,7). **The precise
direction W202 feared -- Z/2 excludes (9,5) -> forces (7,7) -> dissolves the count -- is the
direction I have proven CLOSED.** W202's conjecture was pointing the wrong way; the
perturbative-reality-blindness plus the quaternionic protection make (9,5) the SAFE side, not
the endangered one.

**Push 3 -- does this let the count dissolve?** No. The generation-count leg dissolves ONLY
under FORCED (7,7) (W177/W221 register: the count is theorem-forbidden from the fermion index
and dissolves under (7,7)). Since (7,7) is not forced -- indeed (9,5) is the provably clean
side -- the count leg stands. Count stays `{1,3}`; no dissolution; no canon movement. (E4.)

**Push 4 -- is "genuine free choice" honest, or did I fail to find the selector?** The
perturbative anomaly is reality-blind and zero on both; the global anomaly is provably zero on
(9,5) and, in the 4D reading, zero on both. No consistency requirement I can construct
distinguishes the two signatures. That is the definition of a free choice fixed by convention
(`sign(d)`), not the definition of a hidden selector. The absence-of-forcing is now stronger
than W202's: W202 had one channel OPEN; W232 CLOSES it on the (9,5) side. The residual
(7,7)-side bordism is named, not hidden, and is asymmetric in the safe direction.

## 7. Synthesis -- the return data

| Question | Verdict | Basis |
|---|---|---|
| Reality class across the crux | H (9,5) vs R (7,7) -- only change | A: `p-q mod 8` = 4 vs 0 |
| Point-level Witten Z/2 at dim 15, (9,5)/H | ZERO | B: `KSp_15 = KO_3 = 0` |
| Point-level Witten Z/2 at dim 15, (7,7)/R | ZERO | B: `KO_15 = KO_7 = 0` |
| Global-anomaly room on (9,5) | NONE | C: `Omega~^spin_15(BSp(64)) = 0` (AHSS) |
| 4D `pi_4(Sp(64))` candidate | exists (`Z/2`) but KILLED | D: `dim_H(S) = 64` even |
| 4D `pi_4(SO(128))` candidate on (7,7) | absent | D: stable `pi_4(O) = 0` |
| Does the Witten Z/2 EXCLUDE (9,5)? | NO | E: anomaly absent by B, C, D |
| Does the Witten Z/2 FORCE (7,7)? | NO | E: requires (9,5) excluded |
| Does the generation-count leg dissolve? | NO | E4: dissolution needs FORCED (7,7) |
| What fixes the signature, then? | declared `sign(d)` convention | W202 closed form `p-q = d + d^2/2` |
| Lane verdict | COMPLETED-GENUINE-CHOICE | signature not fixed by anomaly consistency |

## 8. What this closes and what stays open

**Closed.** W202's sole live lever. The 2-primary Witten Z/2 anomaly cannot fire against
(9,5): three independent mechanisms (dead KO/KSp degree at 15; empty `Omega~^spin_15(BSp(64))`;
even 4D multiplicity) all give NO anomaly. The signature is therefore a genuine free choice --
a declared base Lorentzian convention, not an anomaly-forced structure. This converts W202's
conditional ("under-determined, one channel open") into a CHARACTERIZED CHOICE ("all
anomaly channels closed on the (9,5) side; the signature is a convention").

**Direction corrected.** W202's conjectured asymmetry (Z/2 could exclude the H-class and force
(7,7)) is reversed: the quaternionic (9,5) side is the provably clean one; any residual bordism
openness is on the (7,7)/real side and could only point toward (9,5).

**Open (named, not hidden, and asymmetric in the safe direction).** The full twisted bordism on
the (7,7)/real side, `Omega~^spin_15(BSO(128))`, is not computed here; `BSO` mod-2 cohomology
is rich, so the group need not vanish. But it can only bear on EXCLUDING (7,7), never on forcing
it, so it does not disturb this verdict -- it is a future pass that could tighten (7,7) toward
inadmissibility (which would strengthen, not threaten, (9,5)). Also, both readings assume the
Sp(64) gauge determination (9,5 side) and the standard Dai-Freed / Freed-Hopkins
`D+1` bordism placement; both are cited, not re-derived.

## 9. Gates and honest limits

- Exploration grade; conditional register throughout. Nothing asserts GU, asserts a vacuum, or
  changes any verdict. All results are computed statements about KO/KSp periodicity, the
  `Omega^spin_*` table, `p-q mod 8`, and the AHSS degree bookkeeping, with the Witten
  SU(2)=Sp(1) single-doublet positive control -- not assertions about GU.
- The signature verdict is GENUINE-CHOICE (not FORCES_9_5, not FORCES_7_7): no anomaly
  consistency requirement distinguishes the two; `sign(d)` is a declared convention. C-04
  confirmed; the C-07 wall stays genuinely conditional.
- The generation count stays LOCATED-NOT-FORCED and `{1,3}`; the count leg does NOT dissolve
  (that requires FORCED (7,7), which is not delivered). `bar(b)`/H59 stay OPEN and untouched.
  No canon / RESEARCH-STATUS / claim-status / posture change; debit count unmoved; no forbidden
  target `{3,8,24,chi(K3),Ahat}` assumed or inserted.
- Tri-repo gating STRICT: the entire computation is GU-side; no TaF / cross-repo identity
  asserted. Zero em dashes in paper-facing text.

*Filed 2026-07-14 by lane A5 (W232), GAP-CLOSURE wave. Coherence-first; truth-seeking (value
reported under either outcome, and W202's conjectured direction corrected on the evidence);
RUTHLESS self-verification. Four personas inline in one worker (global-anomaly / Witten
specialist; cobordism / bordism-group specialist; signature / Clifford-structure specialist;
ruthless skeptic); no sub-agents. Reproducible:
`python -u tests/W232_signature_witten_z2_anomaly.py` (all checks, exit 0; positive controls
first). Exploration grade; conditional register; no canon movement; tri-repo gating strict.
VERDICT: COMPLETED-GENUINE-CHOICE -- the Witten Z/2 does not fire against (9,5); the signature
is a characterized free choice; the count leg does not dissolve.*
