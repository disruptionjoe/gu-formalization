---
artifact_type: exploration
status: exploration
doc_type: construction_result
created: 2026-08-17
work_item: RSC-1
channel: rs-corner
target_claim: "INTERNAL — ST-1 §6 item 3 (consumer row for the Majorana/126 successor arc), verbatim: 'The clean selective route is the 1-form corner channel `Λ^7_∓ → Λ²(ζ_±)`, multiplicity 1 — pointing the heavy Majorana-type partner at the Rarita-Schwinger-adjacent slot, which is a named partner sector. New join with the 128-partner-placement obligation; kinematic only.' Secondary internal target, same sentence one section earlier, ST-1 §4.5(3): 'a single middle-form VEV direction can give exactly one corner a Grassmann-live Majorana-type self-shape, and that corner is a 1-form corner — the Rarita-Schwinger-adjacent slot'."
target_claim_verdict: "THE JOIN FAILS AS AN IDENTIFICATION, AND THE FAILURE IS EXACT — ST-1's ARITHMETIC IS UNTOUCHED AND FULLY REPRODUCED; ONLY THE MODULE-GRANULARITY GLOSS OVER-REACHES BY EXACTLY ONE LEVEL. The one-form corner is REDUCIBLE: ζ_± = Ω^1(S_±) = V ⊗ S_± = S_∓ ⊕ R^(±), 896 = 64 + 832, and the 832/64 are the two dimension subscripts the draft PRINTS on p.51. The Rarita-Schwinger term of the source's own product rule (eq (11.1), L128) is the 832 — a PROPER submodule of the corner, of codimension 64. ST-1's multiplicity-1 invariant sits ENTIRELY in the cross block S_∓ ⊗ R^(±): mult(Λ^7_+, Λ²(R^(+))) = 0 and mult(Λ^7_-, Λ²(R^(+))) = 0, verified by two independent instruments (Klimyk + block subtraction; and a Racah/Brauer alternating sum over all 322,560 elements of W(D_7) reading the raw 345,696-weight multiset). So the unique chirality-selective Grassmann-live channel is a gamma-trace × gamma-traceless DIRAC-type pairing, not a self-pairing of the Rarita-Schwinger module. It is corner-diagonal and module-OFF-diagonal, and the 128 remainder lives strictly inside the traceless side. TWO further exactness clauses: (i) the RS module is not even chirality-SELECTIVE — Sym²(R^(±)) contains BOTH middle forms with multiplicity 1 each, so it behaves exactly like a 0-form corner (selective-blind and Grassmann-dead); (ii) a rank bound holds for every VEV direction — the only nonzero block is off-diagonal, so the induced form has rank ≤ 2·64 = 128 on the 896 and can reach at most 64 of the 128 remainder's directions, leaving ≥ 768 of R unpaired. PLACEMENT VERDICT: EXACT OBSTRUCTION at the ambient layer for the selective channel; TYPED-CONDITIONAL placement survives only on the chirality-BLIND directions (Λ^1: 1, Λ^5: 2 Grassmann-live shapes in Λ²(R)), which by ST-1 §4.5(2) cannot separate the two corners by irrep type. R5 is ADJACENT, and its kinematic pre-leg is executed here with a negative and SIMULTANEOUS result across both sectors."
title: "RSC-1: 'Rarita-Schwinger-adjacent' was exactly the right hedge and cannot be upgraded — the unique one-insertion chirality-selective Grassmann-live channel lives on the GAMMA TRACE, not on the Rarita-Schwinger module. Exact three-block resolution of ST-1's ζ_± row at D_7: ζ_± = S_∓(64) ⊕ R^(±)(832) — the source's own printed p.51 subscripts — with all ten ST-1 cells decomposed blockwise and the multiplicity-1 invariant located 100% in the cross block. Λ²(R^(±)) carries ZERO of both middle forms; Sym²(R^(±)) carries BOTH with multiplicity 1, so the RS module is chirality-BLIND as well as Grassmann-dead. NEW: the ambient gamma-traceless 832 is EXACTLY the source's Z ⊕ Q ⊕ F bracket and the gamma-trace 64 is EXACTLY its standalone F bracket (eq (11.6) reproduced from the branching, both graded 64/192/576 and ungraded 128/384/1152); the source's 'the logic of the known matters is reversed' for Q is FORCED by V_4 ⊗ 2_+ = 6 ⊕ 2_-; each middle form carries exactly one so(10) `120` as its 4d-Lorentz-scalar part; 16 ⊗ 144 contains no `120` and no singlet, while Sym²(144) contains the `120` with multiplicity 1 — so the obstruction is AMBIENT, not internal. The 128 remainder is dark spinorial matter inside Z, NOT Rarita-Schwinger matter: two different 'RS' tokens at two different layers (ambient γ-traceless 832 / internal γ-traceless 144 vs 4d spin-3/2 Q, 192)."
grade: "EXACT integer/Fraction arithmetic; no float anywhere. Doubled integer weight tuples; Klimyk/Racah-Speiser with every decomposition dimension-saturated; Weyl dimensions asserted integral as Fractions. 103/103 checks, exit 0 (~1.8 s). The decisive multiplicities are computed TWICE by genuinely independent instruments — Klimyk plus the Λ²(A⊕B) block identity, and a Racah/Brauer alternating sum over all 322,560 elements of W(D_7) applied to the raw 345,696-weight multiset of Λ²(R) — agreeing on all ten (insertion × symmetry) entries. NON-VACUITY four ways: 20 [R]-tagged banked reproductions before any extension (all ten ST-1 §4.5 ζ_+ cells, the ST-1 §4.1 spinor-square split, CS-1's duality, MJ-1's 16⊗16 = 10+120+126, canon's singlet-free 16⊗16, HE-1's Inv_Spin(10)(16⊗144) = 0, the draft's printed 832/64 and eq (11.6)'s 64/192/576 and 128/384/1152); a SAME-RANK planted-positive control where the same detector on the same module returns nonzero (Λ²(R^(+)) ⊃ Λ^1 mult 1, Λ^5 mult 2; Sym²(R^(+)) ⊃ Λ^3 mult 2); a DIFFERENT-RANK planted-positive control with the OPPOSITE attribution on the same code path (at D_5 the entire live selective middle-form channel of V_10⊗16b sits on the RS module: Λ²(144) ⊃ 126bar, mult 1); and two contrary controls where the placement provably CANNOT land (the 0-form corners, Λ²(ν_±) middle-form content (0,0); and the gamma-trace block itself, Λ²(S_∓) = Λ^1 ⊕ Λ^5). 15 planted false propositions each observed False. Failure path: `--selftest` verifies the CLEAN BASELINE exits 0 with zero [FAIL] lines BEFORE any mutation and refuses to proceed otherwise, then 12/12 injected machinery/reference mutations each drive exit 1 VIA A GENUINE [FAIL] LINE (0 crash-only, 0 missed), the selftest itself exiting 0; `--selftest --poison-baseline` exits 1 with the refusal printed, proving the baseline guard has power. STANDARD REPRESENTATION THEORY throughout: Weyl dimension formula, Klimyk/Racah-Speiser, Racah/Brauer alternating multiplicity sum, -w_0 as the D_n diagram automorphism for odd n, symmetric/exterior-square weight combinatorics, the D_7 ⊃ D_2 × D_5 coordinate branching. NOT: an action, a vacuum, a scale, a spectrum, a reality map, a Majorana claim about GU, a seesaw claim about GU, a mass for any GU field, a claim that the source's sector labels ARE these modules (that map is typed as a READING and fenced), a resolution of SIGNATURE-AMBIENT, or any claim-status movement."
disposition: THE_JOIN_FAILS_AS_AN_IDENTIFICATION_AND_THE_FAILURE_IS_FIRST_CLASS__ONE_FORM_CORNER_IS_REDUCIBLE_896_EQUALS_64_PLUS_832_AND_THE_SOURCE_PRINTS_BOTH_SUBSCRIPTS__UNIQUE_CHANNEL_SITS_100_PERCENT_IN_THE_GAMMA_TRACE_CROSS_BLOCK__ALT2_OF_THE_RS_MODULE_CARRIES_ZERO_OF_BOTH_MIDDLE_FORMS_TWO_INDEPENDENT_INSTRUMENTS__SYM2_CARRIES_BOTH_SO_THE_RS_MODULE_IS_CHIRALITY_BLIND_AND_GRASSMANN_DEAD_LIKE_A_ZERO_FORM_CORNER__128_PLACEMENT_IS_AN_EXACT_AMBIENT_OBSTRUCTION_PLUS_A_DIRECTION_INDEPENDENT_RANK_BOUND_OF_64_OUT_OF_128__TYPED_CONDITIONAL_PLACEMENT_SURVIVES_ONLY_ON_CHIRALITY_BLIND_DIRECTIONS__AMBIENT_832_IS_EXACTLY_THE_SOURCE_Z_Q_F_BRACKET_AND_THE_TRACE_64_IS_EXACTLY_THE_STANDALONE_F_BRACKET__128_REMAINDER_IS_DARK_SPINORIAL_INSIDE_Z_NOT_RARITA_SCHWINGER_MATTER__RS_IS_A_HOMONYM_ACROSS_TWO_LAYERS__R5_IS_ADJACENT_AND_ITS_KINEMATIC_PRE_LEG_IS_EXECUTED_NEGATIVE_AND_SIMULTANEOUS
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md
  - lab/active-research/joe-directed/lens-digs/ldb-bit2-direction-and-krein-parity-2026-08-17.md
  - lab/active-research/joe-directed/class-shift/cs1-first-order-shift-is-the-chirality-grading-2026-08-15.md
  - lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he2-real-form-does-not-pair-144-with-144bar-2026-08-15.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he3-four-corner-partner-placement-and-family-rank-2026-08-16.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj1-exact-126-majorana-block-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/sn1-observed-neutrino-mass-pencil-2026-08-16.md
  - lab/active-research/joe-directed/majorana-126-neutrino/src1-source-steelman-of-the-vev-2026-08-14.md
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
  - lab/sources/source-claim-register.yaml
  - lab/process/correction-registry.yaml
  - lab/process/canonical-currency-checks.yaml
  - lab/process/layer0-fork-registry.yaml
  - canon/escape-corners-campaign-RESULTS.md
  - lab/methods/source-native-comparator-routing.md
  - VERIFICATION.md
scripts:
  - tests/channel-swings/joe_directed_rsc1_unique_channel_lives_on_the_gamma_trace.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: **`BRIDGE_OR_SEMANTIC_BOUNDARY`** — see §8, which separates
> the source-native leg (exact `D_7` Hom spaces on GU's own printed corners and
> declared bosonic slots; the `D_7 ⊃ D_2 × D_5` branching of the draft's own
> p.51 diagram and eq (11.6)) from the comparator leg (the words "Dirac-type",
> "Majorana-type", "self-mass", "seesaw", "mass matrix rank", used strictly as
> a TAXONOMY OF HOM SPACES, never as an assumed mechanism — the primary corpus
> says "Majorana" **zero** times, and the reality condition that any Majorana
> reading would need is SOURCE-SILENT).
>
> **REQUIRED INTEGRATION WRITE, not performed here.** This artifact was produced
> under a write scope limited to its own two paths, on a checkout shared with
> concurrent agents, so it edits no registry, sidecar, ledger or canon surface.
> One entry belongs to the canonical integrator. Measured at ship time, the
> routing gate's gap is **7 against baseline 5**: this artifact contributes
> **exactly one**, and one further unregistered artifact belongs to a
> concurrently-running sibling channel (`rwall/`) which this work scope may not
> touch. The gate was ALREADY red before this artifact for two unrelated
> reasons owned elsewhere (a registered artifact that does not repeat the
> notice, and a registered path the derived scope no longer finds) — neither is
> attributable here. The entry:
>
> ```json
> { "path": "lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md",
>   "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY" }
> ```
>
> `UNCLASSIFIED_BASELINE` must NOT be raised; the gate's own comment says it may
> only ratchet down. The three currency-check records of §1.2 are likewise
> **stated, not written**: the sidecar
> `lab/process/canonical-currency-checks.yaml` is the integrator's file.

## Typed objects

```gu-typed-objects
result:         the exact module identification of ST-1's unique one-insertion
                chirality-selective Grassmann-live diagonal channel, and the
                placement verdict for the 128 partner-placement obligation
carrier:        zeta_+- = Omega^1(S_+-) = V_14 (x) S_+- , dim 896, REDUCIBLE as
                S_-+ (+) R^(+-) with dims 64 + 832 (the gamma-trace and the
                gamma-traceless Rarita-Schwinger module of draft eq (11.1))
                LAYER=ambient CHIRALITY=S-HALF-SAME
                # SCOPE OF THIS TOKEN: it types THIS artifact's carrier -- one
                # one-form slot at a time, built from ONE half-spinor S_+- --
                # and says NOTHING about the source's two-slot declaration.
                # The CN-2 fork over how Omega^0 and Omega^1 pair is untouched
                # here and no reading of it is asserted.  Note the corner's
                # ambient Z/4 class is 1 for zeta_+ and 3 for zeta_- (CS-1's
                # grading) -- the class of the OPPOSITE half, which is exactly
                # why the trace summand is S_-+ and not S_+- .
pairing:        zero-derivative invariant bilinear ON=Lambda^2(zeta_+-) (the
                Grassmann-surviving square of a SINGLE anticommuting multiplet;
                the symmetric column Sym^2(zeta_+-) is carried alongside and is
                Grassmann-DEAD for one multiplet, never silently swapped in)
real_structure: SOURCE-SILENT. Everything computed is complexified D_7 and is
                therefore identical on both SIGNATURE-AMBIENT horns; the one
                horn-sensitive clause is inherited unchanged from ST-1 4.5(2)
                (independence of the two odd blocks of End(Delta)). No reality
                map is assumed, supplied or needed for any number here.
grading:        CS-1's Z/4 centre class, additive over (+) and (x):
                cls(S_+)=3, cls(S_-)=1, cls(V)=2; cls(zeta_+)=1, cls(zeta_-)=3;
                cls(R^(+))=1 = cls(S_-), so the two summands of a corner are
                class-DEGENERATE and the class rule cannot separate them --
                which is exactly why the block resolution below was needed.
action_owner:   repository-construction (the decomposition and both instruments);
                the insertion slots and the printed corner content are
                source-print (draft eq (9.16), (11.1), (11.6), p.51 diagram);
                whether any insertion is ON is source-action, owned by Lane 1
                via SG4 bit 2 and is NOT decided here
target:         the Rarita-Schwinger module R^(+-) (dim 832) and its sub-blocks
                Z (576) / Q (192) / F (64), and inside Z the 128 remainder
                MAP-TYPE=restriction
```

```gu-typed-objects
result:         the reduced-layer typing of an admissible middle-form VEV
                direction and of where the 128 remainder actually lives
carrier:        the branched corner under D_7 > D_2 x D_5 (Spin(1,3) x
                Spin(6,4) complexified): zeta_+ = Q(192) (+) 2F(2x64) (+) Z(576),
                with the internal spinor 16 and internal vector-spinor 144
                LAYER=observed CHIRALITY=S-HALF-SAME
pairing:        the so(10)-invariant channel of a Lorentz-scalar middle-form
                direction ON=16 (x) 144 (the trace-to-Z cross route) and
                ON=Sym^2(144) (the Z self route)
real_structure: N/A at this layer -- all statements are complex so(10)
                multiplicities; no reality map is used
grading:        4d Lorentz spin (1/2 for F and Z, 3/2 for Q) crossed with the
                internal so(10) label (16 for F and Q, 144 for Z)
action_owner:   source-print (eq (11.6) and the p.51 bracket supply the labels
                and the dimensions; this artifact derives them from the
                branching and does not invent them)
target:         the so(10) `120` = Lambda^3(V_10), the unique Lorentz-scalar
                content of each middle form Lambda^7_+-  MAP-TYPE=restriction
```

```gu-typed-objects
result:         the homonym separation: 'Rarita-Schwinger' names two different
                objects at two different layers, and the 128 is in neither of
                the ones a naive read would pick
carrier:        (i) R^(+-), the AMBIENT gamma-traceless V_14 (x) S_+-, dim 832;
                (ii) the INTERNAL gamma-traceless V_10 (x) 16, dim 144;
                (iii) Q_{3/2}, the 4d spin-3/2 sector, dim 192, whose internal
                factor is a 16 and NOT a 144
                LAYER=ambient+observed BRIDGE=the D_7 > D_2 x D_5 branching of
                section 4.4, which sends R^(+-) to Q (+) F (+) Z
                CHIRALITY=S-HALF-SAME
                # each of (i)-(iii) is built from ONE half-spinor and its
                # partner (V_14 (x) S_+- ambiently, V_10 (x) 16 internally,
                # V_4 (x) 2 in 4d); none is a full Dirac carrier.
pairing:        NONE
real_structure: N/A
grading:        (i) and (ii) are gamma-tracelessness at two different ranks;
                (iii) is 4d spin. The 128 remainder sits inside (ii), hence
                inside Z, hence inside (i) -- and NOT inside (iii).
action_owner:   source-print (the three tokens all originate in the draft:
                eq (11.1)'s R-slash, eq (11.6)'s Q_{3/2}, and SC-FER-03's
                'Rarita-Schwinger matter')
target:         the SC-FER-03 sector list (Looking-Glass / dark Spinorial /
                Rarita-Schwinger matter), typed as a READING and fenced as such
                MAP-TYPE=not-a-map
```

---

# RSC-1 — does ST-1's unique channel land where the source put the Rarita-Schwinger matter?

## 0. The gate, verbatim

ST-1 (2026-08-16, 94/94, exit 0) computed the per-irrep selectivity table and
closed §4.5 with a uniqueness result, then handed it to the successor arc in
§6 item 3:

> **§4.5(3).** *The unique one-insertion chirality-selective Grassmann-live
> diagonal channel lives at the ONE-FORM corners:* `Λ^7_- → Λ²(ζ_+)` *with
> multiplicity exactly 1 … In comparator vocabulary: a single middle-form VEV
> direction can give exactly one corner a Grassmann-live Majorana-type
> self-shape, and that corner is a 1-form corner — the Rarita-Schwinger-adjacent
> slot, which is one of the sectors the source itself names for partner
> placement.*

> **§6 item 3.** *The clean selective route is the 1-form corner channel*
> `Λ^7_∓ → Λ²(ζ_±)`*, multiplicity 1 — pointing the heavy Majorana-type partner
> at the Rarita-Schwinger-adjacent slot, which is a named partner sector. New
> join with the 128-partner-placement obligation; kinematic only.*

The word doing the work is **adjacent**. This file is the demand that it become
either an exact module identification or an exact distinction — and, per the
brief's hostile instruction, that if the identification fails the file says the
join **FAILS** rather than softening back into adjacency.

**Verdict in one line: the join FAILS, exactly, and the failure is worth more
than the join would have been.** The one-form corner is reducible; ST-1's
multiplicity-1 invariant sits entirely on the *gamma-trace* side of the very
split the source's own product rule (eq (11.1)) defines; and the 128 remainder
lives entirely on the other side. §5 states the split; §7 states what each
consumer inherits.

**ST-1 is not broken.** Every number in ST-1 §4.5 is reproduced here, all ten
ζ_+ cells, and its hedge word "adjacent" was exactly correct. What fails is the
one-granularity-too-coarse gloss in §6 item 3 — "pointing the heavy partner at
the RS slot" — and that is a versionless delta to a consumer row, not a kill.

---

## 1. Retrieval first — prior art, the honest ratio, and the currency checks

### 1.1 Prior-art sweep, by mechanism and by exact object

Searched before computing, by object and by mechanism: *gamma-trace,
gamma-traceless, vector-spinor, 832, 896, Rarita-Schwinger module, product rule,
eq (11.1), (11.6), F/Q/Z, 128 remainder, Looking-Glass, dark spinorial, middle
form, Λ^7, chirality-selective, Grassmann-live, partner placement, R5, one dial,
imposter.*

| Result | Owner | Status before RSC-1 |
|---|---|---|
| ST-1 §4.5 per-irrep table; the uniqueness of `Λ^7_∓ → Λ²(ζ_±)`, multiplicity 1; the "RS-adjacent" gloss | ST-1 §4.5(3), §6.3 | **exact — all ten ζ_+ cells reproduced, [R]-tagged in the probe** |
| `Sym²(S_+) = Λ^3 ⊕ Λ^7_+` (2080), `Λ²(S_+) = Λ^1 ⊕ Λ^5` (2016) | ST-1 §4.1 | **exact — reproduced** |
| `W_+^* = W_-`; `-w_0` as the D_7 diagram automorphism; the Z/4 class layer | CS-1, CR-B | **exact — reproduced** |
| The draft prints `832` and `64` as dimension subscripts inside each ζ slot on p.51, and eq (11.6) defines `F/Q/Z` with graded dims 64/192/576 | s11–s12 extraction §2.1–2.2 | **held as a PRINTED READING only — never identified with an ambient module.** This file supplies the identification |
| `16 ⊗ 144` has no `Spin(10)` invariant; the channel opens only at Pati-Salam (2) and SM (11); `144 − 16 = 128` exotics; the mirror family is the exact conjugate of the `16`'s six SM irreps | HE-1 §3.2–3.6 | **exact — the `Spin(10)` zero reproduced on this code path; the SM block decomposition is cited, not recomputed** |
| `16 ⊗ 16 = 10 ⊕ 120 ⊕ 126`, `Sym²(16) = 10 ⊕ 126`, `Λ²(16) = 120`; the luminous spin-3/2 has "**NO invariant mass channel**" | MJ-1; `canon/escape-corners-campaign-RESULTS.md` | **exact — reproduced as controls** |
| `IMPOSTER-LABEL-AB` settled to side **A** (the spin-1/2 `128`), 2026-08-03, confidence 0.90; HE-1 FENCE 1 excludes the RS `384`; R5 is real, stated once, and unexecuted | layer0 fork registry; LD-B card 9 | **standing — consumed unchanged** |
| `n_g → n_g − 1`, real-form stable, `n_g` remains an INPUT; the partition is FORCED, SUBTRACTIVE and UNLABELLED | HE-1, HE-2 | **standing — consumed unchanged** |

**Honest ratio: roughly 35% of this file is reproduction.** The whole banked
layer above was re-derived on this code path before anything new was computed
(20 `[R]`-tagged checks). Novelty greps returned zero hits for the exact new
objects: the three-block resolution of a ζ row, `Λ²(R^(±))` or `Sym²(R^(±))` as
computed objects at `D_7`, any identification of the draft's printed `832` with
`ker(γ·)`, and the Lorentz-scalar `120` content of the middle forms.

### 1.2 Canonical-currency check — recorded verdicts

This artifact's content sits squarely inside three register signatures. Verdicts
below; the integrator writes the sidecar.

| Correction | In signature? | Verdict | Basis |
|---|---|---|---|
| **`CC-05-SUBTRACTIVE-TWO-PLUS-ONE`** (canonical since 2026-08-14) | **YES** — all three token families fire (`n_g` / "three generations"; "imposter" / "third family" / "2+1"; "additive" / count production) | **CLEARED-CONSISTENT** | This file consumes only the CORRECTED reading. It states the partition as FORCED and SUBTRACTIVE (`n_g → n_g − 1`), keeps `n_g` an INPUT, keeps the removed family UNLABELLED, and nowhere treats three as an additive target a mechanism must produce. Its one count sentence — that the 128 is `144 − 16` — is HE-1's own arithmetic, quoted with its owner. |
| **`CC-08-DARK-PARTNER-OBLIGATION`** (canonical since 2026-08-15) | **YES** — family 1 fires on "128 remainder", "Looking-Glass", "dark spinorial"; family 2 on "remainder" and on the explicit "NOT an established defect" | **CLEARED-CONSISTENT, with the register's blindness caveat CONFIRMED BY EXAMPLE — flagged, not silently cleared** | The 128 is typed throughout as a partner-placement / decoupling **obligation** (IV-20260815's corrected typing), never as an established defect; and the corrected reading is *strengthened* here, since the file locates the obligation's target exactly. **The flag:** CC-08's signature deliberately EXCLUDES the `Rarita` token (measured at 295 pre-date files and rejected as non-discriminating). This artifact is the exact document class that exclusion was designed to survive — an RS-corner file — and it is visible to the signature **only because** it also writes the remainder vocabulary. Had it discussed "the Rarita-Schwinger corner" alone, it would have been invisible. That is the register's own documented escape surface, now instantiated; RSC-1 is a natural planted-positive for it, and the observation is offered to the register's owner, not acted on here. |
| **`CC-03-FOUR-CORNER-NONCHIRAL`** (canonical since 2026-08-15) | **YES** — family 1 on "four corners" / "total fermionic"; family 2 on "reality condition" / "non-chiral" / "Majorana" | **CLEARED-CONSISTENT** | The total is stated four-corner and NON-CHIRAL; the corners are subscripted everywhere; the reality condition is stated SOURCE-SILENT and is not supplied; the Weyl-pullback and package-to-three layers are kept distinct and neither is used. |
| `CC-06-CHIRALITY-VEV-CONDITIONAL` (canonical since 2026-08-16) | borderline — the file conditions on the insertion being ON | **CLEARED-CONSISTENT (noted, not a full record)** | The corrected posture is consumed verbatim: the selector is SG4 bit 2, owned by Lane 1, and nothing here decides whether any insertion is on. |

---

## 2. Preflight — six problem-matched lenses, run before computing

**Lens 1 — Rarita-Schwinger representation theory / the spinor exponential
property.** *Route:* the source's own product rule is `W ⊗ S̸_W = S̸_W ⊕ R̸_W`
(eq (11.1), the `L128` term), whose second summand is the pure spin-3/2 piece
"corresponding to the sum of the highest weights of the factors". At `D_7` that
is `λ = ω_1 + ω_7`, dimension `14·64 − 64 = 832`. *Prediction:* ST-1's corner
`ζ_± = Ω^1(S_±)` is the FULL tensor product, dimension 896, hence NOT the RS
module but a reducible extension of it by the 64-dimensional gamma-trace.
*Stake:* if 896 were irreducible, "adjacent" would be an artefact of vocabulary
and the join would be automatic. It is not irreducible, so the question is
decidable and the answer is a location.

**Lens 2 — centre-class arithmetic under CS-1's derived rule.** *Route:* the
Z/4 class is additive over `⊕` and `⊗`, so `cls(ζ_+) = cls(V) + cls(S_+) =
2 + 3 = 1`. But `cls(S_-) = 1` too, and `cls(R^(+)) = 1`: **the two summands of
a corner are class-degenerate.** *Consequence, recorded before computing:* the
class instrument — the sharpest tool CS-1 and ST-1 had — is provably blind to
this question. Any answer must come from an actual Hom computation, and a
"class-allowed" verdict cannot substitute. *Binding condition:* no clause below
may argue from class alone.

**Lens 3 — layer discipline.** *Route:* four layers (declared total / pullback /
± package / observed-VEV-conditional), plus, here, a fifth distinction that has
bitten this repository before: **ambient module vs reduced sector.** The 832 is
an ambient `Spin(14)` module; the `128` remainder is defined only after breaking
to the Standard Model inside an *internal* `so(10)` module. *Binding condition:*
every clause names its layer, and no ambient multiplicity is quoted as an
internal one or vice versa. §4.6 makes the two disagree on purpose, and says so.

**Lens 4 — source philology.** *Route:* three separate tokens in the draft wear
the letters "RS": eq (11.1)'s `R̸_W`; the internal vector-spinor `144` inside
`Z`; and eq (11.6)'s `Q^±_{3/2}`, the only genuinely spin-3/2 *sector*. And
`SC-FER-03`'s list ("Looking-Glass matter, dark Spinorial Matter,
Rarita-Schwinger matter and more") is fenced by the s9 extraction as
**assignments, not derivations**. *Binding condition:* the map from that list to
computed modules is written as a READING with its evidence, never as a
derivation, and the homonym is separated explicitly (§5.3).

**Lens 5 — adversarial reading of my own framing.** *Route:* the brief's own
hostile instruction is the danger and the discipline at once. The seductive
failure is to find `Λ²(R) = 0` and inflate it into "GU cannot decouple the dark
sector" — a claim about an action, from a kinematic multiplicity, at the wrong
layer. The mirror failure is to find it and soften it back to "well, adjacent".
*Binding condition:* the obstruction is stated at exactly the layer it holds
(§5.2, ambient, one insertion, one channel), the surviving routes are computed
and reported in the same table (§4.3), and §9 attacks the result.

**Lens 6 — statistics / parity bookkeeping.** *Route:* for a SINGLE
anticommuting multiplet the quadratic term keeps `Λ²` only; the symmetric column
is Grassmann-dead. But a corner is reducible, and `Λ²(A ⊕ B) = Λ²A ⊕ (A ⊗ B) ⊕
Λ²B`: the **cross term is unconstrained by statistics** and appears identically
in both columns. *Prediction, recorded before computing:* if a "Grassmann-live
self-shape" is really a cross term, it is a self-pairing of the FIELD and a
Dirac-type pairing of the MODULES, and only the module reading is relevant to
placing a specific sub-block. This is the lens that decided the file.

**Cheapest kill-or-switch, recorded before computing.** If
`mult(Λ^7_+, Λ²(R^(+))) = 1` and the cross term were 0, the join would be an
exact identification, the file would lead with it, and the 128 placement would
become a live typed-conditional at the ambient layer. **Outcome: the reverse —
`Λ²(R^(+))` carries 0 and the cross block carries the whole multiplicity 1.**

**One credible contrary route, recorded before computing.** The instrument might
simply be unable to see anything in `Λ²(R)` — a 345,696-weight object reached by
subtraction. Two independent defeats of that route were pre-committed: (i) the
same detector must return NONZERO for other insertions on the same module; (ii)
the same code path must return the OPPOSITE attribution at another rank.
Computed: (i) `Λ^1 → 1`, `Λ^5 → 2`, `Sym² Λ^3 → 2`; (ii) at `D_5` the entire
live selective middle-form channel sits ON the RS module. The route is closed.

---

## 3. Conventions

Corners, after CR-B/CS-1: `ν_± ∈ Ω^0(S_±)` (class 3, 1), `ζ_± ∈ Ω^1(S_±)`
(class 1, 3); protected half `W_+ = ν_+ ⊕ ζ_-`; `W_+^* = W_-` [R]. Declared
bosonic slots `ε ∈ Ω^0(ad P)`, `ϖ ∈ Ω^1(ad P)`, `ad P = End(Δ) = Σ_k Λ^k V`.
Everything is complexified `D_7`, hence identical on both SIGNATURE-AMBIENT
horns; the single horn-sensitive clause is inherited from ST-1 §4.5(2) and
nothing new is computed about it.

New notation, fixed here and used throughout:

```
    zeta_+ = Omega^1(S_+) = V (x) S_+ = S_-  (+)  R^(+)      896 = 64 + 832
    zeta_- = Omega^1(S_-) = V (x) S_- = S_+  (+)  R^(-)      896 = 64 + 832
```

`R^(±)` is the **gamma-traceless vector-spinor**: the second summand of the
source's product rule at eq (11.1), highest weight `ω_1 + ω_7` (resp. `ω_1 +
ω_6`), the "pure Rarita-Schwinger spin 3/2 representation corresponding to the
sum of the highest weights of the factors". `S_∓` is the **gamma-trace**: the
image of Clifford multiplication, the piece eq (11.1) calls "the action of gamma
matrices as spinor endomorphisms".

Multiplicities are reported in two conventions and the conversion is stated
once: ST-1's table entry is `Inv(Sym²/Λ²(X) ⊗ Λ^k)`, which equals
`mult((Λ^k)^*, X)`; and `(Λ^7_±)^* = Λ^7_∓` because `−w_0` on `D_n` with `n` odd
is the diagram automorphism. Tables below labelled "mult of `Λ^k`" are in the
second convention; the `[R]` reproductions are stated in ST-1's.

---

## 4. The swing — exact results

Probe: `tests/channel-swings/joe_directed_rsc1_unique_channel_lives_on_the_gamma_trace.py`,
**103/103 exact checks, exit 0** (~1.8 s). Failure path: `--selftest` verifies
the clean baseline exits 0 with zero `[FAIL]` lines FIRST, then **12/12 injected
machinery/reference mutations each drive exit 1 via a genuine `[FAIL]` line**
(0 crash-only, 0 missed), the selftest exiting 0; `--selftest --poison-baseline`
exits 1 with the refusal printed. 15 planted false propositions observed False.

### 4.1 The corner is reducible, and the source prints both pieces

```
    V (x) S_+  decomposes into exactly TWO irreps:  S_-(64)  (+)  R^(+)(832)
    dim R^(+) = dim R^(-) = 832        (Weyl dimension formula, hw = omega_1 + omega_7)
    64 + 832 = 896 = dim Omega^1(S_+)
```

The draft's p.51 "rolled up Fermionic complex" prints, inside each `ζ` slot, a
bracket subscripted **832** and a standalone bracket subscripted **64** — the
extraction records both as printed by the draft, not inferred. Those are exactly
these two dimensions. §4.4 promotes the coincidence to an identity.

### 4.2 The three-block resolution of ST-1's ζ row (new)

`Λ²(A ⊕ B) = Λ²A ⊕ (A ⊗ B) ⊕ Λ²B` and the same with `Sym²`, so every cell of
ST-1's row splits into a **trace** contribution, a **cross** contribution and an
**RS** contribution. Entries are `(Λ², Sym²)` multiplicities of `Λ^k`:

```
    zeta_+ = S_-(64) (+) R^(+)(832)

    insertion |  trace block   |  cross block  |   RS block    ||  total (= ST-1)
              |  Lam2 , Sym2   |  (both cols)  |  Lam2 , Sym2  ||  Lam2 , Sym2
    ----------+----------------+---------------+---------------++---------------
      Lam^1   |   1   ,   0    |       1       |   1   ,   0   ||   3   ,   1
      Lam^3   |   0   ,   1    |       1       |   0   ,   2   ||   1   ,   4
      Lam^5   |   1   ,   0    |       1       |   2   ,   0   ||   4   ,   1
      Lam^7_+ |   0   ,   0    |       1       |   0   ,   1   ||   1   ,   2
      Lam^7_- |   0   ,   1    |       0       |   0   ,   1   ||   0   ,   2
```

**Reading the table.** Rows are labelled by the irrep whose MULTIPLICITY is
counted; ST-1's columns are labelled by the INSERTION. The two agree for
`Λ^1, Λ^3, Λ^5` (self-dual) and swap for the middle forms, since
`Inv(X ⊗ Λ^7_±) = mult(Λ^7_∓, X)`. With that conversion the **total** column
reproduces ST-1 §4.5's `ζ_+` row exactly, in ST-1's own `(sym, antisym)`
convention: `Λ^1 (1,3)`, `Λ^3 (4,1)`, `Λ^5 (1,4)`, `Λ^7_+ (2,0)`, `Λ^7_- (2,1)`
— all ten cells, `[R]`-tagged. The mirror corner `ζ_-` is computed and behaves
as the mirror requires (`Λ²(ζ_-)` middle-form content `(0,1)`, the 1 carried by
its cross block).

### 4.3 The decisive arithmetic

```
    mult( Lam^7_+ , Lambda^2(R^(+)) )  =  0        <-- the join fails here
    mult( Lam^7_- , Lambda^2(R^(+)) )  =  0
    mult( Lam^7_+ , Lambda^2(S_-)   )  =  0        (= Lam^1 (+) Lam^5, no middle form)
    mult( Lam^7_+ , S_- (x) R^(+)   )  =  1        <-- the entire unique channel
    mult( Lam^7_- , S_- (x) R^(+)   )  =  0        (the channel IS selective ...)

    mult( Lam^7_+ , Sym^2(R^(+))    )  =  1        ... but the RS module is not:
    mult( Lam^7_- , Sym^2(R^(+))    )  =  1        BOTH middle forms, equally.
```

Four readings, each machine-checked and each load-bearing:

1. **The unique channel is carried 100% by the cross block.** ST-1's
   multiplicity-1 invariant is the pairing of the gamma-TRACE with the
   gamma-TRACELESS module. It is *corner*-diagonal and *module*-OFF-diagonal.
   In comparator taxonomy it is a **Dirac-type** shape linking two distinct
   modules, not a Majorana-type self-shape of either.
2. **The RS module has no Grassmann-live middle-form self-shape at all** —
   multiplicity 0 for `Λ^7_+` *and* `Λ^7_-`. Nothing inside `R^(±)` — not `Z`,
   not `Q`, not the 128 remainder — can receive a chirality-selective
   Grassmann-live self-mass from a middle-form direction.
3. **The RS module is not even chirality-SELECTIVE.** `Sym²(R^(±))` contains
   both middle forms with multiplicity 1 each, so no choice between `Λ^7_+` and
   `Λ^7_-` distinguishes `R^(+)` from `R^(-)`. The RS module therefore behaves
   *exactly like a 0-form corner* — selective-blind and Grassmann-dead — and the
   one-form corner's celebrated selectivity is a property of the piece the
   source's product rule explicitly splits OFF.
4. **A direction-independent rank bound.** With only the off-diagonal block
   nonzero, the induced bilinear form on the 896 has the shape `[[0, M], [−Mᵀ,
   0]]` with `M : R^(±) → S_∓^*`, so for EVERY choice of VEV direction
   `rank ≤ 2·64 = 128`, at least `832 − 64 = 768` directions of `R` stay
   unpaired, and **at most 64 of the 128 remainder's directions can be reached
   — less than half, with no direction able to do better.**

**Two independent instruments.** Every entry above is computed twice: once by
Klimyk/Racah-Speiser plus the `Λ²(A⊕B)` block identity, and once by a
Racah/Brauer alternating multiplicity sum over all **322,560** elements of
`W(D_7)` applied directly to the raw **345,696**-weight multiset of `Λ²(R^(+))`
— an instrument that uses no Klimyk, no block identity and no subtraction. They
agree on all ten (insertion × symmetry) entries.

**The detector is demonstrably alive on the same module** (planted-positive
control, same rank): `Λ²(R^(+)) ⊃ Λ^1` with multiplicity 1 and `Λ^5` with
multiplicity 2; `Sym²(R^(+)) ⊃ Λ^3` with multiplicity 2. The zeros are a fact
about the middle forms, not about the instrument.

### 4.4 The branching — eq (11.6) is the RS module's own decomposition (new)

Branching `D_7 ⊃ D_2 × D_5` (complexified `Spin(1,3) × Spin(6,4)`), computed as
an exact weight-multiset identity:

```
    zeta_+  =  Q(192)  (+)  F(64)  (+)  F(64)  (+)  Z(576)          = 896   [verified as multisets]
    R^(+)   =  Q(192)  (+)  F(64)  (+)  Z(576)                      = 832   [verified as multisets]
    S_-     =  F(64)                                                        [verified as multisets]

    with  F = 2 (x) 16 -type,  Q = 6 (x) 16 -type,  Z = 2 (x) 144 -type
    graded dims (F, Q, Z) = (64, 192, 576)   ungraded = (128, 384, 1152)   [R eq (11.6)]
```

**Three consequences, all new as identifications:**

1. **The draft's printed `832` bracket IS the ambient gamma-traceless
   Rarita-Schwinger module**, and its printed standalone `64` bracket IS the
   gamma-trace. The p.51 diagram's `(Z ⊕ Q −−⊕−− F)_{832} ⊕ (F)_{64}` structure
   is not a stylistic grouping: it is `ker(γ·) ⊕ im(γ·)` for eq (11.1), read off
   the branching. The repository held the two brackets as printed subscripts;
   they are now typed.
2. **The 128 remainder's address is exact.** `128 ⊂ 144 ⊂ Z ⊂ R^(±) ⊂ ζ_±` —
   inside the internal vector-spinor `144` (HE-1: the `144` contains exactly one
   generation-shaped block, the exact conjugate of the `16`'s six SM irreps,
   leaving `144 − 16 = 128`), inside the 4d **spin-1/2** sector `Z`, inside the
   ambient gamma-traceless module. Consistent with `IMPOSTER-LABEL-AB` side A,
   and sharper: the 128 is on the traceless side of exactly the split that
   decides §4.3.
3. **The source's "the logic of the known matters is reversed" is FORCED, not
   asserted.** The draft says of `Q^+_{3/2}`: *"a new cousin spin-3/2
   'generation' … in which the logic of the known matters is reversed in the
   sense that it is right handed matter and left handed anti-matter that feel
   the effects of Weak-Isospin."* The branching derives it: `V_4 ⊗ 2_+ = 6 ⊕
   2_-`, so the internal `16` travels with the 4d Weyl half `2_-` in `F` and
   with the spin-3/2 rep built on the OPPOSITE half `2_+` in `Q`. The reversal
   is the 4d leg of the same product rule. (This is a reproduction of a source
   statement from source-declared structure — not a new claim about GU.)

### 4.5 The reduced layer — what an admissible middle-form VEV actually is (new)

A VEV in the declared 0-form slot `ε ∈ Ω^0(ad P)` that preserves 4d Lorentz
invariance must be a `Spin(4)`-singlet in `ad P = ⊕_k Λ^k V_14`. For the middle
forms:

```
    Spin(4)-singlet part of Lambda^7(V_14)  =  Lambda^0(V_4) (x) Lambda^7(V_10)
                                          (+)  Lambda^4(V_4) (x) Lambda^3(V_10)
                                           =  120  (+)  120   (dim 240)
    so each middle form Lambda^7_+-  carries EXACTLY ONE so(10) `120` = Lambda^3(V_10).
```

So "the chirality-selective middle-form direction", read at the layer where the
128 lives, is a `120` of the internal `so(10)`. Its internal channels:

```
    16 (x) 144   contains the `120` with multiplicity  0      and no Spin(10) singlet  [R HE-1]
    Sym^2(144)   contains the `120` with multiplicity  1
    Lambda^2(144) contains the `120` with multiplicity 3
    16 (x) 16 = 10 (+) 120 (+) 126 ;  Sym^2(16) = 10 (+) 126 ;  Lambda^2(16) = 120   [R MJ-1]
```

**The layered reading, stated exactly.** At the *internal* layer alone a `120`
direction is NOT obstructed from giving the `144` a Grassmann-live Majorana-type
mass (`Sym²(144) ⊃ 120`, multiplicity 1, which pairs with the 4d `ε_{αβ}`). At
the *ambient* layer the same channel is **zero** (§4.3). The two are consistent
because ambient invariance is strictly stronger, and the difference is the
finding: **the obstruction is AMBIENT, not internal.** Any route that places the
128 through a middle-form direction must already have broken `Spin(14)` by
something else — a named condition, owned by the action lane, and not a repair
available at the carrier layer.

And the trace-to-`Z` escape is separately closed at the internal layer too:
`16 ⊗ 144` contains no `120`, so even the cross block — the one block that
carries the channel — has no `Lorentz`-scalar middle-form route from the
gamma-trace's internal `16`s into `Z`'s `144`. Both routes to the 128 are shut,
by different arithmetic, at two different layers.

### 4.6 Controls

- **Contrary control 1 — the 0-form corners.** `Λ²(ν_±)` contains neither
  middle form: `(0,0)`. The placement provably cannot land there, and this is
  ST-1 §4.5(1)'s own result reproduced. The machinery discriminates: on the very
  same code path `Sym²(ν_+) ⊃ Λ^7_+` with multiplicity 1.
- **Contrary control 2 — the gamma-trace block.** `Λ²(S_∓) = Λ^1 ⊕ Λ^5` has
  zero middle-form content, so the trace's own self-square cannot host the
  channel either. The channel exists ONLY as the cross term — it is not a
  self-pairing of anything.
- **Planted-positive, same rank.** `Λ²(R^(+))`: `Λ^1 → 1`, `Λ^5 → 2`;
  `Sym²(R^(+))`: `Λ^3 → 2`. A dead detector cannot produce these.
- **Planted-positive, different rank, OPPOSITE attribution.** At `D_5` the
  analogous corner `V_10 ⊗ 16b = 16 ⊕ 144` has its entire live selective
  middle-form channel carried by the **RS module**: `Λ²(144) ⊃ 126bar`,
  multiplicity 1, while `Λ²(16)` carries none. The same code path therefore
  attributes the channel to the RS side when that is where it is. The `D_7`
  attribution to the trace is a computed fact about `D_7`, not a default.
- **15 planted false propositions** each observed False; `--selftest`
  baseline-first, 12/12 mutations caught via genuine `[FAIL]` lines.

---

## 5. The verdicts

### 5.1 The corner identification — an exact DISTINCTION, not an identity

| Question | Answer | Layer |
|---|---|---|
| Which module is ST-1's target corner? | `ζ_± = Ω^1(S_±) = V ⊗ S_±`, **dim 896, REDUCIBLE** `= S_∓(64) ⊕ R^(±)(832)` | declared total / ambient `D_7` |
| Which chirality class? | `cls(ζ_+) = 1`, `cls(ζ_-) = 3`; **both summands share the corner's class**, so class cannot separate them | ambient, both horns |
| Is it the SAME object as the corner the RS product-rule term (L128, eq (11.1)) generates? | **NO — exact distinction.** The product-rule term is `R̸_W = R^(±)`, dim **832**, a proper submodule of codimension **64**. `ζ ⊋ R̸` | ambient |
| Is it the same object as any sector `SC-FER-03` assigns? | **NO — the corner is a union.** `ζ_+ = Q(192) ⊕ 2·F(64) ⊕ Z(576)`; no single named sector is the corner | ambient → reduced, via §4.4's branching |
| Where does the multiplicity-1 invariant actually sit? | **Entirely in the cross block `S_∓ ⊗ R^(±)`**: trace 0, RS 0, cross 1 | ambient |

**So "Rarita-Schwinger-adjacent" was exactly the right hedge — and sharpening it
moves it further away, not closer.** The channel does not merely fail to *be* the
RS module's self-mass; it is *disjoint* from `Λ²(R)`, whose middle-form content
is zero. The honest one-line upgrade of ST-1's phrase is: **the channel is
RS-DISJOINT in the Grassmann-live column and lives on the gamma trace.**

### 5.2 The placement verdict — EXACT OBSTRUCTION, plus a surviving conditional

| # | Clause | Layer | Status |
|---|---|---|---|
| **O1** | `mult(Λ^7_±, Λ²(R^(±))) = 0`. No Grassmann-live chirality-selective self-shape exists anywhere inside the RS module — hence none for `Z`, none for the `144`, none for the 128 | declared total / ambient, both horns | **EXACT OBSTRUCTION.** Two independent instruments |
| **O2** | The whole multiplicity-1 channel is the trace × traceless cross block, so its bilinear form is off-diagonal, `rank ≤ 128` on the 896, reaching **at most 64 of the 128** for EVERY direction | ambient, direction-independent | **EXACT OBSTRUCTION (rank).** Independent of O1 — it would bite even if O1 failed |
| **O3** | `Sym²(R^(±))` contains BOTH middle forms with multiplicity 1: the RS module is chirality-BLIND, and its one middle-form self-shape is Grassmann-DEAD | ambient | **EXACT.** The RS module is a 0-form corner in disguise |
| **O4** | At the reduced layer, `16 ⊗ 144` contains no `120`: the cross-block route from the gamma-trace's internal `16`s into `Z`'s `144` is empty for a Lorentz-scalar middle-form VEV | observed / reduced `so(10)` | **EXACT OBSTRUCTION**, by different arithmetic at a different layer |
| **C1** | `Sym²(144) ⊃ 120` with multiplicity 1 — the internal group alone does NOT forbid the placement | observed / reduced `so(10)` | **TYPED-CONDITIONAL.** Locates the obstruction as AMBIENT; a route exists only after `Spin(14)` is broken by something else, which is an action-lane condition, unnamed here |
| **C2** | `Λ²(R^(±))` carries `Λ^1` (1) and `Λ^5` (2) — three Grassmann-live self-shapes on the RS module from **chirality-BLIND** directions | ambient | **TYPED-CONDITIONAL.** Placement survives, but only in a form that by ST-1 §4.5(2) cannot separate the two corners by irrep type; block-selection needs the SOURCE-SILENT reality condition |
| **C3** | Whether any insertion is ON at all | observed, VEV-conditional | **UNCHANGED** — SG4 bit 2, Lane 1. Not decided here, by design |

**Answer to the RSC-1 binary: EXACT OBSTRUCTION for the named channel, with a
named surviving conditional.** The 128's partner placement **cannot** be typed to
ST-1's unique chirality-selective Grassmann-live channel — not by dimension
(it fits: `128 ⊂ 832`), not by class (they agree: both class 1 at `ζ_+`), but by
**multiplicity**, which is zero, and independently by **rank**, which is 64 < 128.
Placement onto the RS module is not dead in general; it is dead *selectively*.

### 5.3 The homonym, separated

Three objects wear "Rarita-Schwinger" in this corpus. They are not the same
object and two of them are not even at the same layer:

```
  RS-1  ambient gamma-traceless  V_14 (x) S_+-  = R^(+-)   dim 832   [eq (11.1), p.51 subscript]
  RS-2  internal gamma-traceless V_10 (x) 16    = 144      dim 144   [inside Z, eq (11.6)]
  RS-3  4d spin-3/2 SECTOR       Q^+-_{3/2}                dim 192   [eq (11.6); internal factor is a 16]
```

**The 128 remainder lies inside RS-2, hence inside RS-1 — and NOT inside RS-3.**
So `SC-FER-03`'s "Rarita-Schwinger matter", if it names the genuinely spin-3/2
sector (which is the only sector the draft itself glosses in spin terms — "a new
cousin spin-3/2 'generation' `Q⁺_{3/2}`"), does **not** contain the 128 at all.
The best-supported reading of the sector list, offered as a READING and fenced:

| `SC-FER-03` token | Best-supported referent | Evidence | Status |
|---|---|---|---|
| "three generations of observed Fermions" | `F` (4d spin-1/2, internal `16`) | eq (11.6); the p.52 gloss "the one above the dashed line corresponds to matter in our world" | source-supported |
| "Rarita-Schwinger matter" | `Q^±_{3/2}` (4d spin-3/2, internal `16`) | the draft's own spin-3/2 gloss on `Q` | **READING**, well-supported |
| "dark Spinorial Matter" | `Z^±_{1/2}` (4d spin-1/2, internal `144`) | "the other sectors not labeled by F … are currently dark to us"; `Z` is spinorial in 4d | **READING**, well-supported |
| "Looking-Glass matter" | the mirror-family block inside the `144` | HE-1: the `144`'s family-shaped block is the exact conjugate of the `16`'s six SM irreps | **READING**, plausible; the draft never equates them |
| "and more" | the 128 exotic remainder | `144 − 16 = 128`; HE-1's 23-irrep SM branching | **READING** |

`SC-FER-03` is fenced by the s9 extraction as **assignments, not derivations**,
and its register adherence is already `PARTIAL` with the note that
"Looking-Glass/dark-spinorial labels appear on no treatment surface". This table
does not change that; it supplies candidate referents with their evidence so a
future kill cannot mis-target. Nothing in §4 or §5.2 depends on this table.

---

## 6. R5 — disposition

**R5, as LD-B card 9 states it:** *"the wave must exhibit the dial's action on
all sectors simultaneously"* — stated once, in a non-binding packet, never
executed; the upstream tension (the spin-3/2 has "NO invariant mass channel" and
rides the same modulus whose decrease is the generation mechanism) closed at
author-assertion tier only.

**Disposition: ADJACENT, with its kinematic pre-leg EXECUTED here and returning
a negative, genuinely simultaneous result.** Precisely:

- **What R5 demands and this file does NOT supply:** the *dial's action* is a
  dynamical statement — masses, as functions of one modulus, in two sectors at
  once. That needs an action, a vacuum and a scale. All three are Lane 1's, and
  none is touched here. R5's dynamical leg remains **unexecuted**.
- **What this file DOES supply, and it is exactly a pre-leg of R5:** a
  *simultaneous* kinematic statement about both sectors under one declared
  direction. The middle-form direction of the declared 0-form slot acts on `Q`
  (spin-3/2) and `Z` (spin-1/2) **identically — namely, not at all**, because
  both sit inside `R^(±)` and `mult(Λ^7_±, Λ²(R^(±))) = 0` covers the whole 832
  in one certificate. That is the first computed answer of the form R5 asks for:
  one dial, two sectors, one verdict, no hierarchy assumed.
- **A second, differential pre-leg at the reduced layer.** The same direction's
  Lorentz-scalar content is a `120`, and internally `16 ⊗ 16 ⊃ 120` (so `F` and
  `Q`, both internal-`16` sectors, DO have a `120` channel) while `16 ⊗ 144` has
  none. So at the internal layer the one dial types the `16`-internal sectors
  and the `144`-internal sector **oppositely**. That is precisely the "opposing
  demands on one dial" shape the canon row flagged, now with a computed
  asymmetry instead of an assertion — and it is a *constraint on* any future
  hierarchy story, not a hierarchy story.
- **Re-scope proposed (PROPOSAL ONLY, not written to any register):** split R5
  into **R5-K** (kinematic: exhibit the declared-slot directions' action across
  all sectors of the branched corner simultaneously) — *partially executed here,
  for the middle-form direction, negative and simultaneous* — and **R5-D**
  (dynamical: the modulus's action on masses in all sectors at once) —
  *unexecuted, Lane 1 jointly with the decoupling packet, unchanged*.
- **The targeting hazard LD-B named is confirmed and extended.** A kill aimed at
  "the spin-3/2 third family" misses on the settled label fork (side A, the
  spin-1/2 128) *and* now also on module grounds: the 128 is not in the spin-3/2
  sector `Q` at all (§5.3). The live obligation remains the shared dial.

---

## 7. What each consumer inherits, per layer — versionless deltas

Each row below adds a typed condition to an existing row. No claim status moves;
no version is bumped; nothing is retracted except one gloss sentence, named.

**7.1 ST-1 (the owner of the channel).**

| ST-1 locus | Was | Delta |
|---|---|---|
| §4.5(3) arithmetic and uniqueness | multiplicity exactly 1, chirality-selective, Grassmann-live, at a one-form corner | **UNCHANGED — fully reproduced, all ten cells** |
| §4.5(3) gloss "…that corner is a 1-form corner — the Rarita-Schwinger-adjacent slot" | corner-level statement | **UNCHANGED and correct at corner granularity**; now refined: the corner is `S_∓ ⊕ R^(±)` and the shape is off-diagonal in that split |
| §6 item 3 "pointing the heavy Majorana-type partner at the Rarita-Schwinger-adjacent slot … New join with the 128-partner-placement obligation" | offered as the clean selective route to a named partner sector | **CORRECTED (versionless delta).** The route is a gamma-trace × gamma-traceless **Dirac-type** pairing; it points at no partner sector, because `Λ²(R^(±))` carries zero middle-form content. The join is closed as FAILED, not left open |
| §6 item 3's "kinematic only" fence | present | **UNCHANGED and vindicated** — it is exactly the fence that keeps this correction a delta rather than a kill |

**7.2 The HE-1/HE-2 line (the 144-mirror, the subtractive 2+1).**

- *Ambient row gained (new):* the `144` sits inside `Z ⊂ R^(±)`, and the ambient
  chirality-selective middle-form direction gives the block containing it **no**
  Grassmann-live self-pairing. HE-2's "the real form does not pair `144` with
  `144bar`" now has a companion ambient row: neither does the selective channel
  pair the `144`-carrying block **with itself**.
- *Unchanged and explicitly reaffirmed:* `n_g` remains an INPUT; the partition
  is FORCED, SUBTRACTIVE (`n_g → n_g − 1`) and UNLABELLED; the removed family is
  not identified with anything here. **Nothing in this file supplies a count.**
- *Condition gained on the partner-placement gate (HE-3):* four-corner partner
  placement now has one channel typed CLOSED at the ambient layer and one
  surviving family typed OPEN-BUT-BLIND (`Λ^1`, `Λ^5`), so the gate's remaining
  work is the reality condition and block-selection, not the selective route.

**7.3 The Majorana/126 successor arc (SRC-1..4, SN-1..3, MJ-1..5).**

- *Delta:* the arc inherited from ST-1 §6.3 a "clean selective route" pointing
  at the RS slot. **That inheritance is withdrawn.** What remains is C2: three
  Grassmann-live self-shapes on the RS module from chirality-BLIND directions,
  which cannot select a corner by irrep type — so the arc's selectivity problem
  is back where ST-1 §6.3 item 3 said it would be *without* the one-form
  rescue: block-selection, gated on the SOURCE-SILENT reality condition.
- *Unchanged:* SN-1's `UNDEFINED_WITHOUT_REALITY_MAP` on every "Majorana"
  reading. Nothing here weakens or discharges it, and "Majorana" occurs **zero**
  times in the primary corpus.
- *New and usable:* the arc's own insertion slot (`a ∈ Ω^1(ad)` of SRC-1) is not
  touched by O1, which binds one insertion from the 0-form slot in the
  middle-form direction only. The `Ω^1` column of ST-1's table is unaffected by
  this file, and remains the arc's live route.
- *New reduced-layer datum:* `Sym²(144) ⊃ 120` (multiplicity 1) versus
  `Sym²(16) = 10 ⊕ 126` (no `120`). The comparator's `126` route and a `120`
  route are internally available on *different* modules — a comparator-side
  observation, routed and non-binding.

**7.4 The imposter typing.**

- *Confirmed, independently:* side **A** of `IMPOSTER-LABEL-AB`. The 128 is
  4d **spin-1/2** (it sits in `Z = 2 ⊗ 144`), reached here by branching rather
  than by the label argument that settled the fork.
- *Added:* the 128 is **not** in the spin-3/2 sector `Q` — so the fork's losing
  horn is now excluded by module arithmetic as well as by hostile review.
- *Added:* the sector that IS spin-3/2, `Q`, has internal factor `16` (a
  generation shape), not `144`; and the source's "logic reversed" gloss for it is
  forced by the 4d leg of the product rule (§4.4.3).
- *Unchanged:* the imposter partition is unlabelled; nothing here says which
  family is removed, and nothing here converts `SC-GEN-53`.

---

## 8. Comparator routing — which route does this bind?

**Source-native half — this BINDS.** The corner splitting, the three-block
table, the two independent multiplicity computations, the rank bound, the
`D_7 ⊃ D_2 × D_5` branching and its identification of the draft's own printed
`832`/`64` brackets, and the Lorentz-scalar `120` content of the middle forms
are representation theory of `D_7` evaluated on GU's own printed corners and
declared bosonic slots, common to both horns of SIGNATURE-AMBIENT. They are
structural, not evaluative, and no claim status moves.

**Comparator half — this does NOT bind.** "Dirac-type", "Majorana-type",
"self-mass", "seesaw", "mass matrix rank", the `126` and `120` route language,
and the `Sym²(144)` observation are fork-1/fork-4 comparator vocabulary used
here as a taxonomy of Hom spaces. The step from any multiplicity here to a
statement about masses in GU requires the reality map (source-silent), an action
term (Lane 1) and a scale (open) — three untyped bridge legs. Under the
boundary's symmetric rule, **none of the counts here advances or retards any GU
row**, including the negative ones: `Λ²(R) = 0` is a statement about invariant
Hom spaces at one insertion order in one direction, not a statement that GU
cannot decouple anything.

---

## 9. Hostile review — the strongest attacks, answered

**Attack 1 (the brief's own): "you are softening a failure into a
distinction."** Answered by leading with the word FAILS and by O2. If the reader
rejects the module-granularity argument entirely and insists that a quadratic
term in the single field `ζ_+` is a self-mass full stop, the rank bound still
bites: that form has rank ≤ 128 on 896 and reaches at most 64 of the 128
remainder, for every direction. The placement fails on two independent grounds.

**Attack 2: "the zero is a subtraction artefact."** `Λ²(R)` was reached by
subtraction in the first instrument. It was reached by *no* subtraction in the
second — a Racah/Brauer alternating sum over all 322,560 elements of `W(D_7)`
reading the raw 345,696-weight multiset of `Λ²(R)` directly. They agree on all
ten entries. And the detector returns nonzero on the same object for `Λ^1`,
`Λ^5` and (symmetric) `Λ^3`.

**Attack 3: "this kills ST-1."** It does not, and saying so would be the
misaimed-critique failure the repository's own memory warns about. ST-1's
theorem, its ten-pair table, its odd-count rule and its uniqueness result are all
reproduced. The correction is to one consumer sentence, at one granularity level,
and ST-1's own hedge word "adjacent" was correct.

**Attack 4: "the sector map is invented."** Conceded as a risk and handled by
construction: §5.3's map is labelled READING, its evidence is quoted, the source
is noted to fence `SC-FER-03` as assignments not derivations, and **no result in
§4 or §5.2 depends on the map**. The obstruction is a statement about modules,
provable with the sector names deleted.

**Attack 5: "the ambient/internal disagreement means the ambient computation is
the wrong question."** Half conceded, and that is why C1 exists as a first-class
row. The ambient statement is the right question *for an ambient invariant*, and
that is exactly what a one-insertion `Spin(14)`-invariant channel is. The moment
`Spin(14)` is broken by other structure, O1 stops binding and C1's internal
channel is live. Naming that condition is the file's positive contribution to the
placement problem; supplying it is not this file's business.

**Attack 6: "you have quietly given GU a mass mechanism / a count / a
generation."** No mass, no scale, no vacuum, no action, no reality map, no count.
The total remains four-corner and non-chiral; the 2+1 remains subtractive and
unlabelled; every "Majorana" word in this file is a Hom-space taxonomy label and
the source says "Majorana" zero times.

## 9.1 Postflight — five lenses re-run against the finished file

1. **RS representation theory.** Re-checked that `R^(±)` is the eq (11.1)
   summand and not the whole product: highest weight `ω_1 + ω_7`, dim 832,
   Weyl-formula verified, and independently recovered as `ζ ⊖ S_∓` as a weight
   multiset. Both routes agree. ✅
2. **Centre-class arithmetic.** Re-checked that no clause argues from class:
   the two summands are class-degenerate, this is stated in Lens 2 and in the
   typed-carrier block, and every verdict cites a Hom multiplicity. ✅
3. **Layer discipline.** Every clause in §5.2 carries a layer; the one place
   the layers disagree (O1 vs C1) is called out as the finding rather than
   smoothed. The `128` is never quoted as an ambient irrep — it is a
   sub-block defined only after SM breaking, and the file says so twice. ✅
4. **Source philology.** Three "RS" tokens separated (§5.3); `SC-FER-03` fenced
   as assignment; the p.51 diagram's printed numbers cited as printed and then
   identified with an argument; the "logic reversed" sentence derived rather
   than paraphrased; the draft's `±` superscript convention explicitly NOT
   reconstructed (the extraction records it is not independently decodable, and
   nothing here needs it — the identifications are by shape and dimension). ✅
5. **Adversarial self-reading.** The file's most quotable sentence — "the join
   fails" — is the one most likely to be over-carried. Guarded three ways: the
   scope is one insertion, one direction, one channel (O1's row says so); the
   surviving routes are in the same table (C1, C2); and §8 states that even the
   negative result advances no GU row. ✅
6. **Harness discipline (VERIFICATION.md).** Baseline-first selftest, 12/12
   caught via genuine `[FAIL]` lines with 0 crash-only, planted positives for
   both absence claims, a poison-baseline mode proving the guard has power, and
   the one falsifiability limit found while building (the coordinate embedding
   of the branching is not separately falsifiable, because the multisets are
   permutation-symmetric) written into the probe rather than left implicit. ✅

---

## 10. What this file is NOT

Not an action, a vacuum, a scale, a spectrum, a mass, or a reality map. Not a
Majorana claim about GU, not a seesaw claim about GU, not a claim that GU's dark
sectors cannot decouple, not a resolution of SIGNATURE-AMBIENT, not a count, not
a claim-status movement, and not a registry, sidecar, ledger or canon edit. It is
one exact question — where does a specific multiplicity-1 invariant live — asked
at module granularity, answered twice, and typed.

## 11. Reproduce

```
_local/cas-venv/bin/python tests/channel-swings/joe_directed_rsc1_unique_channel_lives_on_the_gamma_trace.py
_local/cas-venv/bin/python tests/channel-swings/joe_directed_rsc1_unique_channel_lives_on_the_gamma_trace.py --selftest
_local/cas-venv/bin/python tests/channel-swings/joe_directed_rsc1_unique_channel_lives_on_the_gamma_trace.py --selftest --poison-baseline
```

Expected: `103/103 checks pass … exit 0`; `12/12 mutations caught via a genuine
[FAIL]; 0 crash-only; 0 missed`, selftest exit 0; poison-baseline exit 1 with
the refusal printed.
