---
artifact_type: exploration
label: W240
created: 2026-07-15
status: exploration
posture: adversarial; truth-seeking; native-object first; construction-fork explicit; coherence-first then kill; no verdict movement; does NOT decide the W235 record bit
title: "W240 Z2-even compact-image no-go: generalizing W237's bilinear theorem to ALL VEVs (higher-rank tensors, fundamental orbits, and SETS of order parameters) in Sp(32,32;H). RESULT: a SCOPED STRUCTURAL NO-GO. The grading Z = tau3(null) = sigma1(definite) is a genuine NON-COMPACT (non-elliptic) boost generator, Z in p. (A) Any Z-NEUTRAL VEV of any rank or any set keeps Z in its isotropy => non-compact stabilizer. (B) Any ADJOINT/operator-type VEV is Z2-even iff it commutes with Z, which puts Z in its centralizer => non-compact (W237's bilinears = the rank-2 case, now extended to all adjoint ranks). (C) The deep theorem: NO Cartan involution of Sp(32,32;H) commutes with Z (Z is non-elliptic), so the good-stable maximal-compact reducing direction is INTRINSICALLY Z2-ODD -- chirality-preservation and the maximal-compact good-stable target are structurally incompatible. The located flaw thus UPGRADES to a structural no-go on everything GU builds. HONEST residual: one escape corridor survives -- Z2-EVEN but Z-CHARGED (charge != 0), non-adjoint higher-rank VEVs -- because for a charged vector the 'Z survives' argument does not apply and a charged vector CAN have a compact stabilizer (SO(2,1) timelike, stabilizer SO(2)). That corridor is GU-native-EMPTY: its only native candidate, channel S ((16bar)^4, charge -4), has no order parameter (W231/W237). So the no-go is a structural no-go for adjoint/neutral/max-compact-target VEVs, not an unconditional Lie-theory no-go."
grade: "EXACT for: the grading Z = tau3(null) = sigma1(definite) being a non-compact non-elliptic generator (ad(Z) real, nonzero: max|imag|=1e-16, max|real|=2.00 in the faithful so(4,4) model); the operator identities and the centralizer arithmetic (cent(P)=maximal compact so(4)+so(4)=12, cent(Z)!=12, cent(I)=full 28); the exact 8256/4160/4096 arithmetic for Sp(32,32;H); the anticommutator {P,Z}=0 (compactifier Z2-ODD); and the SO(2,1) charged-vector compact-stabilizer fact (stab dim 1). STRUCTURAL for the three no-go classes (A) Z-neutral any-rank/any-set, (B) adjoint/operator any-rank, (C) no Cartan involution commutes with Z -> good-stable direction intrinsically Z2-odd; these are proven in a faithful finite so(n,n) analog of the Cartan-involution / boost-centralizer phenomenon (same toy status as W216/W224/W234/W237) plus the rank/set-independent Lie-theory argument (exp(tZ) in the isotropy of any Z-neutral VEV; Z non-elliptic => not in any maximal compact). SCOPED / HONEST-OPEN for the residual corridor (Z2-even, Z-charged, non-adjoint higher-rank VEVs): shown non-empty in general Lie theory (the charged corridor is NOT closed by classes A-C) and shown GU-native-EMPTY (channel S, the only native tenant, has zero order parameter, W231/W237). CONDITIONAL on the W235 record bit for channel D's availability (the whole comparison lives on the favorable, record-conserved branch). OPEN for the interacting source action, the physical state space, and the observable algebra. Machine regression: tests/W240_z2even_compact_image_nogo.py (27/27, exit 0, positive controls first). No canon, RESEARCH-STATUS, verdict, bar(b), H59, or generation-count change; the W235 record bit is FLAGGED not decided."
depends_on:
  - explorations/W237-channel-s-condensate-isotropy-2026-07-15.md
  - explorations/W234-condensate-vev-isotropy-gate-2026-07-15.md
  - explorations/W235-central-bit-mirror-record-vs-redundancy-2026-07-15.md
  - explorations/W231-close-a3-smg-realization-gu-mirror-2026-07-14.md
  - explorations/W224-native-good-stable-dynamical-vacuum-2026-07-15.md
  - explorations/W219-native-good-stable-stabilizer-input-gate-2026-07-14.md
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W240_z2even_compact_image_nogo.py
---

# W240 Z2-even compact-image no-go

## Result in one paragraph

**THE VERDICT: a SCOPED STRUCTURAL NO-GO.** W237 proved, for null-pair BILINEAR condensates,
`COMPACTIFY <=> Z2-ODD`. W240 generalizes to ALL VEVs and the located flaw UPGRADES to a
structural no-go on **everything GU actually builds**, resting on one exact fact: the grading
`Z = tau3(null) = sigma1(definite)` is a genuine **NON-COMPACT, NON-ELLIPTIC boost generator**
of `Sp(32,32;H)` (`Z in p`, `ad(Z)` real and nonzero, `exp(tZ)` unbounded). From it, three
rank-independent no-go classes follow. **(A) Z-NEUTRAL VEVs** (charge 0 under `Z`), of any rank
and any SET of order parameters: `exp(tZ)` fixes each, so `Z` lies in the common isotropy
algebra; `Z` non-compact => the stabilizer is not compact-image => no compactification. **(B)
ADJOINT / operator-type VEVs** of any rank that reduce to a Lie-algebra direction: Z2-even
`<=> [O,Z]=0 <=> ` block-diagonal in the generation/mirror split, which puts `Z` in the
centralizer `cent(O)` => non-compact. W237's bilinears are exactly the rank-2 case; this covers
all adjoint ranks. **(C) The deep structural theorem:** NO Cartan involution of `Sp(32,32;H)`
commutes with `Z`, because an element commuting with a Cartan involution `P'` would sit in
`cent(P') = k'` (compact) and hence be elliptic, but `Z` is non-elliptic. Therefore the
good-stable maximal-compact reducing direction (the `~P` Cartan involution whose centralizer is
`Sp(32) x Sp(32)`) is **intrinsically Z2-ODD**: chirality-preservation (Z2-even) and the
good-stable maximal-compact target are structurally incompatible, for VEVs of any rank. **The
honest residual (why this is SCOPED, not unconditional):** the "Z survives" argument requires
`Z` to be IN the isotropy, which for a higher-rank vector `w` needs `Z`-NEUTRALITY
(`dR(Z)w = 0`), NOT merely Z2-even (charge even but possibly nonzero, e.g. channel S carries
`Z`-charge `-4`). For a `Z`-CHARGED even VEV the argument does not apply, and the abstract Lie
theory PERMITS charged vectors with compact stabilizers (an `SO(2,1)` timelike vector has
stabilizer `SO(2)`, compact, yet is boost-charged). So one escape corridor stays open: Z2-even,
`Z`-charged, non-adjoint higher-rank VEVs. That corridor is **GU-native-EMPTY** -- its only
native candidate, channel S (`(16bar)^4`, charge `-4`), has no order parameter at all
(W231/W237). So the located flaw upgrades to a structural no-go on the adjoint, neutral, and
maximal-compact-target classes -- everything GU builds -- while the residual escape is exotic
(charged, higher-rank, non-adjoint) and contains no GU-native object. `bar(b)`, `H59`, and the
count remain OPEN / unchanged; the W235 record bit is FLAGGED, not decided.

## 1. Construction fork (mandatory)

The load-bearing object is a general VEV / order-parameter read as an element of a representation
of the internal arena `Sp(32,32;H)`, and its isotropy (stabilizer) subgroup. This is the
program's recurring Krein/native fork, now at the level of arbitrary-rank order parameters.

- **Standard-physics reading.** Treat symmetry breaking as "some Higgs field in some
  representation gets a VEV and the gauge group reduces to the stabilizer," and default to
  assuming a compact residual group is generically available (pick a representation, pick an
  orbit). Under this default one silently assumes the compactification whose obstruction is the
  whole question, and one conflates the DISCRETE grading Z2 with the CONTINUOUS boost it is built
  from (the trap that makes "chirality kept => the grading survives => nothing forbids
  compactifying" look automatic).
- **Program-native reading.** The arena is `Sp(32,32;H)`, the non-compact real form whose
  non-compactness IS the Krein/indefinite form (GEOMETER-VS-PHYSICS-OBJECTS, gauge-group row).
  The grading `Z = tau3(null)` is the generation(`+`)/mirror(`-`) Cartan-involution / ghost-parity
  label (W173/W234), and in the definite (`beta`-eigen) basis it is `sigma1(definite)` -- an
  OFF-diagonal, `beta`-Hermitian element, i.e. a genuine element of the non-compact part `p` of
  the Cartan decomposition `g = k + p`. It is a BOOST, not a compact charge: `ad(Z)` has real
  eigenvalues, `exp(tZ)` is unbounded.

**Which side, and why.** The answer lives on the native side and it is decisive in a way the
physics reading misses in BOTH directions. Natively, `Z` is a non-compact boost, so its role as
the grading is inseparable from its role as one of the 4096 non-compact generators that a
good-stable must break. That exposes the exact tension the physics reading hides: to compactify
you must break `Z` (a p-generator), but W237 read "keeping the grading" as "keeping `Z`," which
would forbid compactification. Per the fork discipline the kill is checked in the OTHER
construction, and this is where the native reading also EXPOSES the escape the physics reading
would over-claim away: the DISCRETE grading Z2 (chirality) and the CONTINUOUS boost `Z` come
apart. Chirality is protected by the discrete Z2 (no generation-mirror Dirac mass = Z2-even);
the continuous boost `Z` can be broken (a `Z`-charged VEV) WITHOUT pairing the generation away.
So a Z2-even but `Z`-charged VEV could in principle break `Z` (allowing a compact residual) while
keeping chirality. That corridor is real (Section 4), and only the native construction makes both
the no-go (Sections 2-3) and its precise limit (Section 4) visible at once.

## 2. The grading Z is a non-compact, non-elliptic boost (goal: verify, do not assert)

The entire generalization hinges on `Z` being genuinely non-compact, so this is checked, not
assumed. In the definite basis, `Z = sigma1(definite)` per null pair; on the full fiber
`Z = [[0, I_32],[I_32, 0]]` in the `(generation, mirror)` block split. It is `beta`-Hermitian and
lies in `g = sp(32,32;H)` (check: `Z\dagger beta + beta Z = 0`), and being Hermitian it is in the
NON-COMPACT part `p`. Consequences, all machine-verified in the faithful `so(4,4)` model
(checks PC1-PC4, B1):

```
ad(Z) eigenvalues : REAL (max|imag| = 1.1e-16), NONZERO (max|real| = 2.00)  -> NON-ELLIPTIC
exp(tZ)           : cosh/sinh, UNBOUNDED                                     -> NON-COMPACT
parity of Z under itself : EVEN ([Z,Z]=0)   ;   parity of the compactifier P : ODD ({P,Z}=0)
cent(P) = so(4)+so(4) = maximal compact (compactifies)  ;  cent(Z) != maximal compact (does not)
```

`Z` is simultaneously (i) the Z2-even grading and (ii) a non-compact boost. This reconciles with
W234 (`Z = tau3(null)`) and W235 (the Cartan-involution / ghost-parity grading): the SAME `Z`
whose discrete parity protects chirality is a CONTINUOUS non-compact generator of the arena. Note
`Z` is NOT the Cartan involution `P`: `P = tau1(null) = sigma3(definite)` is the compactifier
(centralizer the maximal compact) and it ANTICOMMUTES with `Z` (`{P,Z}=0`, check C1). This is the
seed of theorem (C).

## 3. The three no-go classes (the upgrade of W237 beyond bilinears)

### 3.1 (A) Z-neutral VEVs, any rank, any SET

Let `w` be any VEV in any finite-dimensional representation `R` with `dR(Z) w = 0` (charge 0
under the grading). Then `exp(tZ) w = w` for all `t`, so `exp(tZ)` is in the stabilizer
`Stab_G(w)`, i.e. `Z` is in the isotropy algebra. Since `exp(tZ)` is a non-compact one-parameter
subgroup (Section 2), `Stab_G(w)` is not compact-image. This is rank-independent and
SET-independent: for a set `{w_1, ..., w_k}` of Z-neutral order parameters, `Z` fixes each, so
`Z` is in the intersection `∩_i Stab_G(w_i)` -- the unbroken group of the whole set is still
non-compact (checks D1, D2). Every Z2-even ADJOINT is Z-neutral (Section 3.2), and the W224
singlet vacuum is the charge-0 special case (`Z` in `Stab = G`), so this class subsumes both.

### 3.2 (B) Adjoint / operator-type VEVs, any rank

For an order parameter that reduces to a Lie-algebra direction `O in g` (the adjoint/one-body
content of any condensate, at any rank), the grading Z2 is the block grading of the associative
matrix algebra by `Z`: `O` is Z2-EVEN iff it is block-diagonal in the generation/mirror split iff
`[O, Z] = 0`. But `[O, Z] = 0` says exactly `Z in cent(O) = Stab_G(O)`. So `Z` is in the
isotropy of EVERY Z2-even adjoint VEV, and by Section 2 the stabilizer is non-compact (checks B2,
B3, B4). W237's bilinear theorem is the rank-2 instance (there the only traceless even direction
is `Z` itself); W240 shows the conclusion is independent of rank for all adjoint-representable
VEVs. Equivalently: a Z2-even adjoint VEV can never be the compact-reduction direction `~P`.

### 3.3 (C) No Cartan involution commutes with Z -> the good-stable direction is intrinsically Z2-odd

This is the deepest and most general statement, and it targets the good-stable TARGET directly.
The good stable (W219/W224) requires reducing `G = Sp(32,32;H)` to a maximal-compact-image
subgroup: break all 4096 non-compact generators, leave the compact 4160 `= Sp(32) x Sp(32)`. Such
a residual is the centralizer of a Cartan involution `P'` (a `G`-conjugate of `P = beta`).

Claim: no Cartan involution `P'` commutes with `Z`. Proof: if `[Z, P'] = 0` then `Z in cent(P')`.
But `cent(P') = k'` is the maximal compact algebra fixed by the Cartan involution `theta'`, whose
elements are all elliptic (`ad` purely imaginary). `Z` is non-elliptic (`ad(Z)` real nonzero,
Section 2). Contradiction. Hence `[Z, P'] != 0` for every Cartan involution `P'` (checks C1, C2:
no conjugate `gPg^{-1}` is both a maximal-compact compactifier and Z2-even). Consequently the
maximal-compact reducing direction cannot be Z2-even -- it is intrinsically Z2-ODD. Restated in
physics terms: **the good-stable good stabilizer is intrinsically the chirality-KILLING direction
(channel D), for any order parameter that achieves the maximal-compact target, not only for
bilinears.** This is the structural upgrade of W234's "same operator, opposite desirability"
coupling from one bilinear to the whole target class.

## 4. Adversarial escape-hatch hunt (the part that makes it rigorous)

Each hatch from the brief, worked and dispositioned.

**Hatch 1 -- does good-stable require breaking `Z`, or only compact-image on a relevant
subspace/quotient (so `Z` could survive on an irrelevant factor)?** This is the crux and it is
where the SCOPE lives. The maximal-compact good-stable target (W219/W224: break the full 4096)
DOES require breaking `Z` (`Z` is one of the 4096 non-compact generators). But "chirality
preserved" (the physical requirement) needs only the DISCRETE grading Z2 to be unbroken -- no
generation-mirror Dirac mass, which is the Z2-ODD channel D. The CONTINUOUS boost `exp(tZ)` need
NOT survive for chirality to hold: a Z2-even but `Z`-CHARGED VEV keeps the discrete parity (no
Dirac mass) while breaking the continuous boost. W237's identification "the survival of the
grading boost `Z` IS the preservation of chirality" (its S5b) conflates the discrete Z2 with the
continuous boost; the honest statement is that chirality = discrete Z2, and the boost may be
broken. Disposition: PARTIALLY CLOSES the no-go and OPENS the residual corridor. The no-go is
airtight for VEVs whose Z2-even-ness forces `Z` into the isotropy -- namely `Z`-NEUTRAL VEVs
(class A) and ADJOINT VEVs (class B, which are neutral), and for the maximal-compact TARGET (class
C). It does NOT cover Z2-even but `Z`-charged non-adjoint VEVs.

**Hatch 2 -- is `Z` genuinely non-compact, and genuinely THE chirality grading (reconcile with
W234's `Z = tau3(null)` and W235's grading)?** YES on both (Section 2). `Z = tau3(null) =
sigma1(definite)` is `beta`-Hermitian in `p`, `ad(Z)` real nonzero (non-elliptic), `exp(tZ)`
unbounded. Its discrete parity is the generation/mirror ghost-parity Z2 whose conservation
(W235's record reading) forbids channel D. Disposition: CLOSED -- `Z` is both the chirality
grading and a genuine boost; the two roles are the source of the tension, not a confusion.

**Hatch 3 -- higher-rank VEV whose ORBIT stabilizer differs from the element centralizer: can it
evade "Z survives"?** YES, this is precisely the corridor. For an adjoint `O`, the isotropy is the
centralizer and Z2-even forces `Z in cent(O)`. For a higher-rank vector `w`, the isotropy is
`{X : dR(X)w = 0}`, and `Z in` isotropy requires `dR(Z)w = 0` (`Z`-NEUTRAL), which is STRICTLY
stronger than Z2-even (charge even). A `Z`-charged even `w` (e.g. `dR(Z)w = -4 w`) is moved by
`exp(tZ)`, so `Z` is NOT in its isotropy, and the class-A/B argument does not apply. Disposition:
this is the OPEN corridor; it is why the no-go is scoped. It is closed for GU only by the separate
fact that GU's one native tenant of the corridor is empty (Section 5).

**Hatch 4 -- can a Z2-even element be elliptic (conjugate into `K = Sp(32) x Sp(32)`) despite
commuting with the boost `Z`?** Checked in the real-form Lie theory (Section 3.3). An element can
commute with `Z` and still be elliptic -- that is not the obstruction. The obstruction is the
converse and it is what theorem (C) proves: the element that DEFINES the maximal-compact reduction
is a Cartan involution `P'`, and NO Cartan involution commutes with `Z` (`Z` non-elliptic would
otherwise be forced into the compact `cent(P') = k'`). So the compact-reduction direction is
never Z2-even. And a genuine `Z`-charged vector CAN have a compact stabilizer -- exhibited
concretely: the `SO(2,1)` timelike vector `t = e_3` has stabilizer `SO(2)` (compact, dim 1) yet
is boost-charged (checks E1-E3). Disposition: CLOSED for the maximal-compact target (no even
Cartan involution) and HONESTLY OPEN for the charged corridor (charged vectors can have compact
stabilizers), consistent with hatch 3.

## 5. The corridor is GU-native-empty

The residual escape -- a Z2-even, `Z`-charged, non-adjoint higher-rank order parameter with a
compact-image stabilizer -- is non-empty in general Lie theory (hatch 4's `SO(2,1)` example). The
question that matters for GU is whether GU BUILDS such an object. The only native candidate is
channel S, the mirror-only `(16bar)^4` symmetric-mass-generation operator (W231/W237): it is
Z2-even and carries `Z`-charge `(-1) * 4 = -4` (even but NONZERO), so it sits exactly in the
corridor, NOT in the neutral/adjoint no-go classes (check F1). But channel S has NO `SO(10)`-
singlet bilinear order parameter (channel B empty, W231): its adjoint content is ZERO, so it
breaks 0 of the 4096 non-compact generators -- the W224 shortfall (check F2). So the one GU-native
tenant of the corridor delivers no compactification, for a reason INDEPENDENT of the `Z`-survival
argument (it has no order parameter at all). The corridor is therefore mathematically open but
GU-native-empty: on the favorable (record-conserved, W235) branch, no native VEV -- of any rank,
adjoint or not, single or a set -- delivers A1's dynamical good-stable while preserving chirality.

## 6. Verdict

```
Z2-EVEN COMPACT-IMAGE VEV in Sp(32,32;H) -- generalized beyond bilinears:

  grading Z = tau3(null) = sigma1(definite): NON-COMPACT, NON-ELLIPTIC boost (Z in p), exp(tZ) unbounded.

  (A) Z-NEUTRAL VEVs (any rank, any SET)     : Z in the common isotropy => NON-compact  -> NO-GO
  (B) ADJOINT/operator VEVs (any rank)       : Z2-even <=> [O,Z]=0 => Z in cent(O) => NON-compact -> NO-GO
                                               (W237's bilinears = the rank-2 case)
  (C) MAXIMAL-COMPACT good-stable target     : reducing direction = a Cartan involution P'; NO Cartan
                                               involution commutes with Z (Z non-elliptic) => that
                                               direction is INTRINSICALLY Z2-ODD  -> NO-GO

  => The located flaw UPGRADES to a STRUCTURAL NO-GO on everything GU builds (adjoint/neutral/target).
     Chirality-preservation (Z2-even) and the maximal-compact good-stable are structurally incompatible.

  RESIDUAL CORRIDOR (honestly OPEN, not closed): Z2-EVEN but Z-CHARGED (charge != 0), non-adjoint
     higher-rank VEVs. The 'Z survives' argument fails for charged VEVs; a charged vector CAN have a
     compact stabilizer (SO(2,1) timelike: stab = SO(2)). So this is NOT an unconditional Lie-theory
     no-go. The corridor is GU-native-EMPTY: channel S ((16bar)^4, charge -4) has no order parameter
     (W231/W237), so no native object fills it.

CONDITIONAL on the W235 record bit (NOT decided here): on the record-CONSERVED branch (chirality
protected), channel D is forbidden and no Z2-even native VEV compactifies -> W224's singlet
input-failure STANDS; A1's dynamical good-stable residual is a GENUINE LOCATED FLAW, now hardened
from "bilinear-only" (W237) to "all adjoint/neutral VEVs and the maximal-compact target."
```

This does not claim GU has no good stable, nor that GU is falsified (unbuilt `!=` false). It is
the narrower, computed result that the chirality-preserving compactification GU would need is
structurally blocked for every order parameter GU builds, and that the only mathematical escape
(a charged, higher-rank, non-adjoint VEV) is not realized by any native GU object. `bar(b)`,
`H59`, and the generation count remain OPEN / unchanged; the W235 record bit is not decided.

## 7. Joe-gated items borne on but NOT moved

- **The W235 record / redundancy bit**: this result is stated CONDITIONAL on it and does NOT
  decide it. FLAGGED, not moved. W240 shows the located flaw survives on the FAVORABLE
  (record-conserved) reading and now for all adjoint/neutral VEVs, not just bilinears.
- **H59 / bar(b)**: unchanged. This SHARPENS what H59 must build: not merely "a compactifying
  condensate that is also Z2-even" (W237's sharpening), but -- since that is now blocked for all
  adjoint/neutral VEVs and the maximal-compact target -- a Z2-even, `Z`-CHARGED, non-adjoint,
  higher-rank order parameter with a compact-image stabilizer, an object GU currently does not
  build (channel S, the only native corridor candidate, is empty). No debit added or cleared; a
  located input-failure hardened across ranks is a sharpened gap, not a new falsification.
  FLAGGED, not moved. This bears on `bar(b)`; it is CHARACTERIZATION only, verdict-relevant,
  Joe-gated.
- **Generation count / RESEARCH-STATUS / verdicts / canon**: untouched. No verdict flip.

## 8. Follow-up this unlocks

The single remaining crack is the charged corridor (Section 4-5). The highest-value next
computation is to determine whether GU can build ANY `Z`-charged, Z2-even order parameter with a
compact-image stabilizer -- or whether a second structural argument (e.g. that a `Z`-charged
extremal-weight vector always retains a non-compact parabolic in its stabilizer) closes the
corridor entirely, turning the scoped no-go into an unconditional one. If the corridor closes,
chirality-safe dynamical compactification is impossible in `Sp(32,32;H)` full stop; if a native
charged compactifier is exhibited, it is the exact object H59 needs. The other open route is the
W241 front door (the DYNAMICAL vacuum isotropy reducing to a smaller, coincidence-admitting group
in which the grading is no longer a boost). Both are finite-dimensional and Lean-portable: the
operator identities (`Z = sigma1(definite) in p`, `{P,Z}=0`), the non-ellipticity of `Z`
(`ad(Z)` real nonzero), and the "no Cartan involution commutes with a non-elliptic element"
theorem are exact. A Lean port of theorem (C) is noted as follow-up ONLY (no Lean/Lake run here,
per the machine-wide serialized-build rule; a sibling worker is concurrent).

## 9. Machine receipt

```
python -u tests/W240_z2even_compact_image_nogo.py
```

27/27 checks passed, exit 0. Positive controls run FIRST and each fires on a real falsifier: the
parity detector correctly flags the KNOWN compactifier `P` as Z2-ODD and the grading `Z` as EVEN
(so the no-go is not built on a mislabeled compactifier); the compactification detector sees `P`
reduce to the maximal compact and correctly rejects a boost and a singlet; and the ESCAPE detector
`escape(parity, is_compact)` is shown to FIRE on a planted `(EVEN, compact)` pair -- so a genuine
Z2-even compact-image orbit WOULD be caught -- while the real objects (`P`: ODD+compact; `Z`:
EVEN+non-compact) both return non-escape. The actual checks then verify the non-compact
non-elliptic character of `Z`, the class-(A) neutral/set no-go, the class-(B) adjoint no-go across
sampled even directions, the class-(C) theorem (no conjugate Cartan involution is Z2-even), the
open corridor (`SO(2,1)` charged vector with compact stabilizer), and that channel S is the
corridor's only GU-native candidate and is empty.

## Governance

Exploration grade only. No canon, RESEARCH-STATUS, verdict, `bar(b)`, `H59`, or generation-count
change. The W235 record bit is flagged and coupled, not decided. No cross-repository identity
asserted; the reservoir Krein sign and the Y14 spectral-section / record datum stay gated
temporal-issuance / time-as-finality objects. `bar(b)` and `H59` remain OPEN. This is
characterization, verdict-relevant and Joe-gated; no verdict is moved. Zero em dashes.
