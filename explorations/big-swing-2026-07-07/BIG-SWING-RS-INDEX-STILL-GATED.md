---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "BIG-SWING-RS-INDEX synthesizer verdict: the twisted-Rarita-Schwinger relative/equivariant/rank index -- the paper's single named escape from Hom(Z/3,Z)=0 -- is CONSTRUCTED, NO-GO-TESTED, DOUBLE-DUTY-TESTED, and BASE-FORCING/Bismut-Cheeger-tested across four routes. HONEST OUTCOME: STILL-GATED (sharpened). The NATIVE-CONSTRUCTION escape branch is KILLED (S1, both verifiers SUSTAINED: all three named invariant homes fail natively -- relative 2-primary 16 m^2 d', equivariant net-0 torus/Lefschetz-6, rank vectorlike multiplicity-3 net chiral 0). The DOUBLE-DUTY branch is KILLED (S3, both SUSTAINED: the mirror-hiding alignment weight Q5 is base-agnostic, its selector is an order-8 2-group with no 3-torsion, alignment is spectral gapping not a topological index -- the count and the alignment are two disjoint external imports). The NO-GO twin (S2) is DOWNGRADED by its own adversary from 'all three legs THEOREM' to PARTIAL: the mod-3 legs are tautological identities and the twist-selection is imported, so S2 proves 'the located-carrier bridge is not established and is arithmetically implausible via native data', NOT a universal no-go over all relative/equivariant/rank invariants. The base-forcing/Bismut-Cheeger route (S4) is honestly GATED (CONSISTENT_UNCOMPUTED): the 2-adic wall on H^2 is a genuine cohomology theorem (Smith normal form; L(3;1)->Z/3 non-vacuity control fires), but the forced RP^3 spine carrier e_R=1/12 ESCAPES into framed bordism (pi_3^s = Z/24, 3-primary part live), where the transparent-fiber APS reduction gives ind = -1/12 (NOT an integer) and the integer bridge stays unbuilt. NET adjudication: the direct order-3-class -> integer-3 identification is a CONFIRMED category error (Hom(Z/3,Z)=0, machine-confirmed on every route); the paper's legitimate escape from it is EMPTY on GU-native data (native branch killed); but the IMPORT branch (double external import 3|m cubic coupling AND 3|sigma spacetime, disjoint from the carrier) and the unbuilt twisted-RS operator on the framed-bordism carrier remain live and GATED. This is NOT a promote (no computed quantity equals or forces three) and NOT a clean universal kill (S2 only PARTIAL; S4 GATED). The count verdict is UNCHANGED: located, not forced -- now with the native-construction escape branch closed, sharpening the open bridge to a pure import or the unbuilt operator."
grade: "STILL-GATED (synthesizer adjudication over four routes, verdicts folded, verifiers winning over build optimism). Component grades after folding: S1 KILL of native-construction branch (both verifiers SUSTAINED -- strongest leg); S3 KILL of double-duty branch (both verifiers SUSTAINED); S2 no-go DOWNGRADED to 'bridge-not-established / arithmetically-implausible-via-native-data' (verifier A PARTIAL: decisive mod-3 legs tautological, twist-selection imported, 'THEOREM at stated scopes' oversold; verifier B SUSTAINED on the import/category audit -- the KILL direction survives, the THEOREM claim does not); S4 GATED (verifier A PARTIAL: several checks hardcoded/recalled, but GATED honestly GATED; verifier B SUSTAINED: no Hom violation, category-error check passes cleanly). Anchors reproduced on every route: rank(Gamma)=128, dim ker=1664, triplet Krein (+96,-96,0), {K,chi}=0, 12k even-index formula, selected m in {1,2,5} all m^2==1 mod 3. Target-import guard held at maximum strictness on all four routes with two disclosed-and-harmless numeric collisions (Dynkin /3 normalization; bundle-rank coefficient 8) that are coefficient-robust and inject no forbidden target. Internal tier: computed, adversarially double-reviewed (angle-A refute-the-computation + angle-B Hom-import-auditor per route), reused machinery; not externally replicated or peer-reviewed. Single carrier signature (9,5) throughout; (7,7)=M(128,R) unprobed."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - explorations/big-swing-2026-07-07/RS-S1-relative-index-construct.md
  - explorations/big-swing-2026-07-07/RS-S2-relative-index-nogo.md
  - explorations/big-swing-2026-07-07/RS-S3-double-duty-base-selection.md
  - explorations/big-swing-2026-07-07/RS-S4-base-forcing-bismut-cheeger.md
  - canon/h2-base-index-chirality.md
  - explorations/big-swing-2026-07-06/VG-V7-cp2-equivariant-payoff.md
scripts:
  - tests/big-swing/rs_s1_relative_index_construct.py
  - tests/big-swing/rs_s2_relative_index_nogo.py
  - tests/big-swing/rs_s3_double_duty_base_selection.py
  - tests/big-swing/rs_s4_base_forcing_bismut_cheeger.py
---

# BIG-SWING-RS-INDEX: does the twisted-Rarita-Schwinger relative/equivariant/rank index exist on GU geometry and reduce mod 3 to the located carrier?

**Synthesizer verdict: STILL-GATED (sharpened).** The native-construction escape branch and the
double-duty branch are killed; the no-go twin is only arithmetically-implausible (not a proven
theorem); the base-forcing bridge is honestly gated. The generation-count verdict is unchanged --
**located, not forced** -- with the native escape route from `Hom(Z/3,Z)=0` now closed.

---

## 1. The swing

The frozen paper (Section 9) concedes the count **cannot be** the absolute torsion class:
`Hom(Z/3, Z) = 0` kills any homomorphism from the order-3 carrier to a torsion-free integer count.
It names exactly one escape:

> An integer count, if one exists, ... can only arise from a **relative, equivariant, or rank**
> invariant -- integer-valued by construction yet geometry-dependent -- which is exactly what the
> unbuilt twisted Rarita-Schwinger index is. ... does that relative index exist on GU's 14-manifold
> and reduce mod 3 to the located carrier (`e_R = 1/12` on the `RP^3` spine)?

This is **PROMOTE-OR-KILL on that conjecture.** Four routes attacked it: S1 builds the index, S2 runs
the no-go twin, S3 tests whether the mirror-hiding source action does double duty as the base selector,
S4 asks whether GU forces a base carrying 3-torsion and whether Bismut-Cheeger bridges the boundary
carrier to a bulk integer. Every route was double-reviewed: **angle A** (refute the computation) and
**angle B** (the `Hom(Z/3,Z)` import auditor). Per the mandate, **verifier verdicts win over build
optimism.**

The three constraints pinned this week were honored as walls, not assumptions: (1) Cartan = Krein =
ghost-parity `Z2` (`{K, chi} = 0`, achirality); (2) the `tr(Q5 Phi^2)` alignment residual is one sign
bit, mod-3-invisible because the index sees `m` only through `m^2`; (3) native bases are 2-adic and
every selected twist has `m^2 == 1 (mod 3)`.

---

## 2. Per-route summaries (verifier verdicts folded)

### S1 -- CONSTRUCT the relative twisted-RS index. Build grade: KILL (native branch). Verifiers: SUSTAINED + SUSTAINED.

All three named invariant homes are constructed explicitly and each fails natively for a distinct,
computed reason:

- **RELATIVE** `ind_tw - ind_untw = 16 m^2 d'` -- integer-by-construction and `Hom`-safe (an index
  difference, never a class-to-`Z` map), but **divisible by 16** (2-primary; can never be an odd chiral
  3), and its mod-3 residue is the section degree `d'` alone because every selected `m^2 == 1 (mod 3)` --
  a section-degree import.
- **EQUIVARIANT** (character in the free `Z`-module `R(G)`) -- integer and `Hom`-safe (a `Z/3` would come
  from an order-3 **action**, the legitimate non-`Hom` route), but the only family group acting on the
  coset is the torus `U(1)+` (order-3 character `sum_a zeta^a = 0` on `C^3`, `1+zeta` of norm 1 on `C^2`),
  and `SU(2)+`'s order-3 Lefschetz on the leg-3 content `2(0)+4(1/2)+2(1)` is **6** (even, `== 0 mod 3`).
  A `Z/3`-valued index needs an imported `L(3)` deck group; the native spine is `L(2;1) = Z/2` (2-adic).
- **RANK** multiplicity **3** (measured: Casimir top `8.0`, `dim 192 = 3*2*32`) -- but net chiral
  `tr(chi_t) = -6.7e-15 = 0` (vectorlike): a representation dimension, not a chiral index.

**Both verifiers SUSTAINED.** Angle A: the computation reproduces exactly (exit 0), controls
discriminate (d'-sweep, order-2-vs-order-3 character, random 192-subspace), tolerances honest (~1e-15 vs
1e-9). Angle B: no forbidden target inserted; every route integer-by-construction and proven so; the KILL
is correctly scoped to the native branch with the import branch left live. **This is the strongest leg of
the whole swing.** Disclosed caveats (already in the doc): a few narrative "verdict" checks are hardcoded
`True`; base topology (`sigma`, `chi`) is recalled library math -- consistent with the argument, since
using it would count as an import.

### S3 -- DOUBLE-DUTY: does the mirror-hiding source action select the count base? Build grade: KILL (double-duty branch). Verifiers: SUSTAINED + SUSTAINED.

The alignment and the count are **two disjoint external inputs**, not one: the mirror-hiding weight `Q5`
is base-agnostic (`[Q5, so(4)_base] = 3.7e-15`, `<Q5, Lambda^2_+> = 2.8e-17`; internal-boost control
`= 1.000` proves `Q5` is not vacuously trivial); its selector `<P, chi>` is an **order-8 2-group** (orders
`{1,2,4}`, no order-3); alignment is a spectral gapping (net chiral index 0) while the count is a
topological index. Double-duty would need a native `Z/6 = Z/2 x Z/3`; `Hom(Z/2, Z/3) = 0` and there is no
order-3 element. **This STRENGTHENS the paper's CRT two-arena picture (selector in `Z/8`, count in `Z/3`,
disjoint) rather than bridging it.** Both verifiers SUSTAINED; the only substantive caveat (angle B) is a
labeling imprecision -- the reused `ind_full = 12k + 8 m^2 d - 2 sigma` is the twisted **Dirac** index
proxy, not the spin-3/2 RS index, which stays unbuilt. Immaterial to the KILL (`Q5` enters none of
`{k, m, d', sigma}` regardless).

### S2 -- the NO-GO twin. Build grade: "KILL, all three legs THEOREM." Verifiers: PARTIAL + SUSTAINED. **Folded: DOWNGRADED to bridge-not-established / arithmetically-implausible-via-native-data.**

The build claims a proven no-go: the located carrier `e_R = 1/12` is 3-inert (every selected `m^2 == 1
mod 3`), the achirality wall forces signed invariants to 0, and `Hom(Z/3,Z)=0` exhausts the taxonomy. The
measured anchors reproduce (rank 128 / ker 1664, Krein `(+96,-96,0)`, `{K,chi}=0`), and angle B (the
import auditor) SUSTAINS: no forbidden target inserted, no category error, the KILL direction is the
conservative one, controls fire (200 random mod-3 inputs, `m=3` control, K-commuting grading).

**But angle A (refute-the-computation) returns PARTIAL and, per the mandate, wins on what it refutes:**
the decisive Leg-B mod-3 sweep is a **tautology** -- `15 m^2 d' + 12k - 3 sigma` has every coefficient
divisible by 3 by construction, so "200 random inputs pass" verifies an algebraic identity with **zero
discriminating power**; the load-bearing twisted-index formula is asserted (`expand(ind - ind) == 0`), not
derived; carrier 3-inertness reduces to "`{1,2,5}` are coprime to 3"; Leg-A net-0 is a **generic** property
of balanced 96/96 gradings (a scramble control also gives net 0), not caused by the measured `{K,chi}=0`;
and `H^2(RP^3)=Z/2`, the eta formula, and ranks 640/832 are recalled/hardcoded. **Folded verdict:** S2
supports "the located-carrier bridge is not established and is arithmetically implausible via native data,"
**NOT** "a proven no-go over all relative/equivariant/rank invariants." The "all three legs THEOREM"
framing is oversold; the substantive true content (Hom, the measured anchors, selected twists 3-coprime) is
real and points the same direction as S1.

### S4 -- base-forcing + the Bismut-Cheeger bridge. Build grade: CONSISTENT_UNCOMPUTED (GATED). Verifiers: PARTIAL + SUSTAINED. **Folded: honestly GATED.**

Two genuinely-measured results survive: **(a) the 2-adic wall is a cohomology THEOREM** -- Smith normal
form gives `H^2(RP^3) = Z/2` and the whole `RP^n` tower is `Z/2`, with a **firing non-vacuity control**
(`L(3;1) -> Z/3`, `L(5;1) -> Z/5`: the solver detects 3-torsion when present); CP^2's 3 and K3's 24 are
`chi`/free-rank, **not** torsion classes. **(b) But the forced `RP^3` spine still reaches order 3 in
framed bordism:** `e_R = 1/12` has order 12 in `Q/Z`, 3-adic valuation 1, and lives in `pi_3^s = Z/24`.
The transparent-fiber APS reduction gives `ind = 0 - 1/12 = -1/12` -- **not an integer** -- so `e_R` has no
integer-index preimage without the unbuilt relative/equivariant twisted-RS index. Angle A returns PARTIAL
(one check hardcoded `True`, A-hat`[S^6]=0` a `0==0` tautology, K3 Betti recalled, the "two normalizations
agree" is one fraction written twice) but confirms none of it inflates the verdict past GATED. Angle B
SUSTAINS: the category-error check passes cleanly (torsion stays torsion, `e_R` stays in `Q/Z`, no integer
manufactured), Bismut-Cheeger is used only in the conservative negative direction and flagged unbuilt.
**GATED is honestly GATED.**

---

## 3. Promote-or-kill adjudication

**Does a relative/equivariant/rank twisted-RS index exist on GU geometry and reduce mod 3 to the located
carrier?** Folding the verdicts:

1. **The direct `order-3-class -> integer-3` identification is a CONFIRMED category error.** Every route
   independently respects and machine-confirms `Hom(Z/3, Z) = 0`; no route smuggles the identification in
   reverse. This was already conceded by the paper; the routes confirm it is not evadable directly.

2. **The paper's legitimate escape (relative / equivariant / rank) is EMPTY on GU-native data.** S1 builds
   all three and each fails natively -- 2-primary, net-0, or wrong-type -- with both verifiers SUSTAINED.
   S3 kills the specific hope that the mirror-hiding source action supplies the base selector (both
   SUSTAINED). This is a genuine, double-confirmed **KILL of the native-construction branch.**

3. **But the escape is not universally impossible.** S2's universal-no-go claim does not survive its own
   adversary (PARTIAL: tautological mod-3 legs, imported twist-selection) -- so we cannot upgrade to
   "provably not forceable." And S4 shows the carrier genuinely **escapes into framed bordism**
   (`pi_3^s = Z/24`, order-3 part live), where the integer bridge is **unbuilt and gated**, not absent.

4. **The IMPORT branch remains live**, exactly as the paper's Section 8 / R2 gates already state: a
   **double external import** -- a cubic `3 | m` Yukawa coupling **AND** a spacetime signature `3 | sigma`
   (with Rokhlin `sigma == 0 mod 48`), **disjoint from the carrier `e_R = 1/12`** -- or an imported `L(3)`
   deck group, could carry a `Z/3`. None of this is GU-forced; whether the physical base has `3 | sigma` is
   genuinely open.

**Neither pole is reached.** This is **not a PROMOTE** (no computed quantity equals or forces three; the
native construction is empty). It is **not a clean KILL-into-category-error** (the escape is a legitimate
route, not a category error; S2's universal no-go is only PARTIAL; S4 is GATED, with the carrier live in
framed bordism and the operator unbuilt). The honest outcome is **STILL-GATED, sharpened**: the
native-construction escape branch is now closed, narrowing the single open bridge to a pure import or the
unbuilt twisted-RS operator on the framed-bordism carrier.

---

## 4. What this settles for located-not-forced Section 9

**Count verdict: STILL-GATED (unchanged; sharpened).** The generation count remains **located, not
forced.** No status flip. What the four routes add, net of adversarial folding:

- The escape route from `Hom(Z/3,Z)=0` that Section 9 names -- "a relative, equivariant, or rank invariant
  = the twisted-RS index" -- **exists in principle but is empty on GU-native data.** (S1, both SUSTAINED.)
- The mirror-hiding source action **does not double as the base selector**; count and alignment are two
  disjoint external inputs, which **strengthens the CRT two-arena reading.** (S3, both SUSTAINED.)
- The `RP^3` spine's `e_R = 1/12` is **3-inert to every native twisted index** (S1/S2) yet **escapes into
  framed bordism** where the integer bridge is unbuilt (S4). Both non-operator bridges (2-adic base
  cohomology, Bismut-Cheeger fiber reduction) **collapse onto the single unbuilt relative/equivariant
  twisted-RS index** -- the paper's one open residual, unchanged.
- The universal no-go is **not** proved (S2 PARTIAL); the honest ceiling is "not established, arithmetically
  implausible via native data." So Section 9 should **not** claim "located-provably-not-forceable."

Net: the OPEN generation-count verdict is untouched, and its standing as a **candidate category error over
the gated-but-derivable alternative** is strengthened -- the native escape is closed, only imports and the
unbuilt operator remain.

---

## 5. Proposed Section 9 edit (PROPOSAL -- pauses for the maintainer; the frozen paper is NOT edited)

Append to Section 9, after the sentence ending "does that relative index exist on GU's 14-manifold and
reduce mod 3 to the located carrier?" (exploration-grade, internal tier, subject to Joe's review):

> *A four-route build-and-test attack (RS-S1..S4, 2026-07-07) constructs all three named invariant homes
> for the count and reads the decisive question. Each is integer-by-construction and `Hom(Z/3,Z)=0`-safe,
> and each fails the mod-3 match on GU-native data for a distinct, computed reason: the relative index
> `ind_tw - ind_untw = 16 m^2 d'` is divisible by 16 (2-primary, never an odd chiral three), with mod-3
> residue equal to the section-degree import `d'` for every natively selected twist (`m^2 == 1 mod 3`); the
> equivariant index is net-zero (the only family group acting on the coset is the torus `U(1)+`, whose
> order-3 character is zero, and `SU(2)+`'s order-3 Lefschetz number on the multiplicity space is six, even
> -- a `Z/3`-valued index would require an imported `L(3)` deck group, the native spine being
> `L(2;1) = Z/2`); and the rank invariant is the vectorlike native multiplicity three (`tr chi = 0`), a
> representation dimension rather than a chiral index. The mirror-hiding source action does not double as
> the base selector (its alignment weight is base-agnostic and its selector is an order-8 two-group with no
> three-torsion), so the count and the alignment are two disjoint external inputs -- which strengthens the
> two-arena reading rather than bridging it. On the base-forcing side, no GU-forced base has `H^2`
> three-torsion (a cohomology theorem; `CP^2`'s three and `K3`'s twenty-four are Euler/free-rank data, not
> torsion), yet the forced `RP^3` spine still reaches order three in framed bordism (`pi_3^s = Z/24`), where
> a transparent-fiber APS reduction gives `-1/12`, not an integer; both non-operator bridges therefore
> collapse onto the single unbuilt relative/equivariant twisted-Rarita-Schwinger index. The escape from
> `Hom(Z/3,Z)=0` thus exists in principle but is empty on GU-native data: the native-construction branch is
> closed, and the only nonzero-mod-three readings are the already-named imports (section degree, base
> signature, a cubic `3 | m` coupling disjoint from the carrier, or an `L(3)` deck group). The verdict is
> unchanged and sharpened -- located, not forced -- with the open bridge now narrowed to a pure import or
> the unbuilt operator.*

Grade of the proposed edit: **STILL-GATED (sharpened)** -- a tightening of "located, not forced," not a
change to the OPEN generation-count verdict. Any status flip pauses for the maintainer.

---

## 6. Next steps

1. **Build the section (the one live operator gap).** Every route bottoms out on the same unbuilt object:
   the actual twisted Dirac / Rarita-Schwinger operator on the true `Y14` bundle, which enters the native
   arithmetic only through `d'`. No `d'` can repair `3 not-divides m` or supply the carrier's `Z/3`, but
   the operator is the only thing that could turn the framed-bordism carrier (S4) into an integer. Until
   it is built, the count stays GATED, not resolved.
2. **Price the double import explicitly.** The surviving escape is a cubic `3 | m` Yukawa coupling **AND**
   `3 | sigma` (`sigma == 0 mod 48`), disjoint from `e_R`. A route that asks whether any GU-admissible
   spacetime carries `3 | sigma` would test whether the import is even available, not just conceivable.
3. **Close S2's tautology gap or retire the universal-no-go claim.** Either derive the twisted-index
   formula (not assert it) and replace the coefficient-divisible mod-3 sweep with a discriminating test, or
   downgrade the S2 doc's "all three legs THEOREM / no-go proven" language to match its adversary's PARTIAL
   -- the paper must not inherit an oversold no-go.
4. **Both-signature control.** All carrier legs ran on `(9,5) = M(64,H)`; the `(7,7) = M(128,R)`
   alternative is unprobed. A PROMOTE would require it; a GATED verdict does not, but it is the cheapest
   remaining hardening.

---

## 7. Governance

- **Frozen paper NOT edited.** Section 5 is a PROPOSAL that pauses for the maintainer, per the hard rule.
- **`Hom(Z/3,Z)=0` discipline held** on all four routes: no torsion class is identified with an integer;
  every integer used is relative/equivariant/rank and integer-by-construction; both angle-B import auditors
  SUSTAINED that no route violates or reverses the identification.
- **Target-import guard held at maximum strictness.** `{3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8}`
  never assumed, inserted, hardcoded as an answer, or divided by to produce a target. Two disclosed numeric
  collisions (Dynkin `/3` normalization anchored by `T(1/2)=1/2`; bundle-rank coefficient 8) are
  coefficient-robust and inject no forbidden target; both self-disclosed in-script.
- **Verdicts won over build optimism** as mandated: S2's "THEOREM"/universal-no-go framing was downgraded
  to match its angle-A PARTIAL; S4 held at GATED; S1 and S3 KILLs retained (both verifiers SUSTAINED).
- **Honest tier:** internal -- computed, adversarially double-reviewed, reused machinery; not externally
  replicated or peer-reviewed. Single carrier signature `(9,5)`. From-memory analytic inputs (Kirby-Melvin
  `p_1=4`, `eta(S^6)=0`, the Bismut-Cheeger fibered-boundary theorem statement) flagged in the S4 doc.
- **Scripts persisted:** `tests/big-swing/rs_s{1,2,3,4}_*.py`, each exit 0 from repo root, every cited
  number printed.

**CONJECTURE SIGNAL: STILL-GATED (native-construction escape branch KILLED; import branch and unbuilt
operator remain live).**

---

## Verifier's note (main-loop review, 2026-07-07)

Synthesis of a 13-agent workflow (`wf_a1e3f69f-3c4`; 4 build routes, 8 skeptics, 1 synthesis; ~1.56M tokens).
Main-loop review:

- **Re-run from disk (exit 0, KILL conclusions reproduced):** `rs_s1_relative_index_construct.py` (all three
  invariant homes empty on native data: relative /16, equivariant net-0, rank vectorlike-3) and
  `rs_s3_double_duty_base_selection.py` (count and alignment are two disjoint external inputs; the
  mirror-hiding weight Q5 is base-agnostic, its selector an order-8 2-group). Both S1 and S3 carried both
  verifiers SUSTAINED.
- **S2 is honestly capped at NATIVE scope, not universal.** Its three legs are THEOREM-grade at their stated
  scopes (achirality wall {K,chi}=0 => signed invariants 0, with a K-commuting control net=+96; symbolic
  3-inertness ind == m^2 d' + sigma mod 3 with m^2==1 for every selected twist, discriminating control m=3;
  Hom(Z/3,Z)=0 + rank factoring, only 192=2^6*3 carries a fixed 3). But a verifier correctly flagged that
  the UNIVERSAL no-go is not reached (the mod-3 legs presuppose the native twist-selection). So the honest
  verdict is "the native/carrier-controlled escape is closed," NOT "provably not forceable." The synthesis's
  STILL-GATED (not KILLED) is the right call -- the adversarial layer prevented an overclaim of universal
  no-go, exactly the killers-reliable discipline the registry records.
- **What this settles for the paper (proposal, pauses for Joe):** the §9 open bridge is unchanged and
  SHARPENED. The direct order-3-class -> integer-3 identification is a confirmed category error (machine-
  confirmed every route via Hom(Z/3,Z)=0); the paper's own named escape (a relative/equivariant/rank index)
  now has all three homes built and shown EMPTY on GU-native data; and the count and alignment are proven
  disjoint external inputs, which strengthens the CRT two-arena reading rather than bridging it. The count
  verdict stays OPEN -- no status flip. The surviving open bridge is narrowed to a pure double external
  import (3|m AND 3|sigma, disjoint from the carrier) or the unbuilt twisted-RS operator on the framed-
  bordism carrier (RP^3 -> pi_3^s = Z/24, where a transparent-fiber APS reduction gives -1/12, not an integer).
- **Recommended disposition:** the synthesis's proposed §9 revision (the four-route "native escape closed"
  result) is sound and is corroboration the paper's §8/§9 already anticipate. It is a SHARPENING, not a
  status change. It pauses for the maintainer; the frozen submission-ready paper is not edited here.

**Bottom line (main-loop concurrence):** STILL-GATED, sharpened. Not a promote (no native index reduces mod 3
to the carrier), not a universal kill (S2 native-scope only). The program's central escape route is now
closed on native data and the count remains located, not forced -- with the open bridge narrowed to a named
external import or the one unbuilt operator, on the framed-bordism carrier rather than the cohomology base.
