<!-- GENERATED from lab/process/path-dependencies.yaml by
     process_gates/path_dependency_audit.py --write.
     Edit the YAML, never this file. -->

# Path dependencies

Why a strange-looking check exists. Each chain ends in a **check**;
each **trap** is a mistake that actually happened, with its date.

```mermaid
graph TD
  PD_SIGNATURE_PARITY["PD-SIGNATURE-PARITY"]
  PD_SIGNATURE_PARITY_s0["EXACT: The DeWitt fibre form is (6,4), and this is INDEPENDENT of the base sign: G..."]
  PD_SIGNATURE_PARITY --> PD_SIGNATURE_PARITY_s0
  PD_SIGNATURE_PARITY_s1["EXACT: So the base sign alone moves the ambient: (3,1)->(9,5), (1,3)->(7,7)."]
  PD_SIGNATURE_PARITY_s0 --> PD_SIGNATURE_PARITY_s1
  PD_SIGNATURE_PARITY_s2["EXACT: Cl(9,5) = M(64,H) quaternionic; Cl(7,7) = M(128,R) real. Not real-isomorphic."]
  PD_SIGNATURE_PARITY_s1 --> PD_SIGNATURE_PARITY_s2
  PD_SIGNATURE_PARITY_s3["EXACT: Majorana-Weyl exists iff p-q = 0 mod 8. Of the reachable horns only (7,7) q..."]
  PD_SIGNATURE_PARITY_s2 --> PD_SIGNATURE_PARITY_s3
  PD_SIGNATURE_PARITY_s4["THEOREM: Quaternionic structure forces Kramers doubling, hence EVEN multiplicity."]
  PD_SIGNATURE_PARITY_s3 --> PD_SIGNATURE_PARITY_s4
  PD_SIGNATURE_PARITY_s5["CONDITIONAL: Three generations is ODD. So (9,5) structurally forbids the target; (7,7) p..."]
  PD_SIGNATURE_PARITY_s4 --> PD_SIGNATURE_PARITY_s5
  PD_SIGNATURE_PARITY_chk{"CHECK: State which horn the work stands on"}
  PD_SIGNATURE_PARITY_s5 --> PD_SIGNATURE_PARITY_chk
  PD_SIGNATURE_PARITY_t0("TRAP 2026-08-04")
  PD_SIGNATURE_PARITY_chk -.-> PD_SIGNATURE_PARITY_t0
  PD_SIGNATURE_PARITY_t1("TRAP 2026-08-08")
  PD_SIGNATURE_PARITY_chk -.-> PD_SIGNATURE_PARITY_t1
  PD_SIGNATURE_PARITY_t2("TRAP 2026-08-08")
  PD_SIGNATURE_PARITY_chk -.-> PD_SIGNATURE_PARITY_t2
  PD_SIGNATURE_PARITY_t3("TRAP 2026-08-08")
  PD_SIGNATURE_PARITY_chk -.-> PD_SIGNATURE_PARITY_t3
  PD_GHOST_PARITY["PD-GHOST-PARITY"]
  PD_GHOST_PARITY_s0["THEOREM: Bender-Mannheim's C and Turok-Bateman's ghost parity are the SAME operator ..."]
  PD_GHOST_PARITY --> PD_GHOST_PARITY_s0
  PD_GHOST_PARITY_s1["THEOREM: They come APART at spectral degeneracies, where C exists but is NOT unique."]
  PD_GHOST_PARITY_s0 --> PD_GHOST_PARITY_s1
  PD_GHOST_PARITY_s2["EXACT: At the degenerate point the KINEMATIC parity is exactly well-defined ([P_to..."]
  PD_GHOST_PARITY_s1 --> PD_GHOST_PARITY_s2
  PD_GHOST_PARITY_s3["EXACT: R3's balance is caused by CHI, not by quaternionic structure: {K,chi} = 0 e..."]
  PD_GHOST_PARITY_s2 --> PD_GHOST_PARITY_s3
  PD_GHOST_PARITY_s4["EXACT: Balance requires ANTIcommutation with K. Kramers alone gives only EVENNESS...."]
  PD_GHOST_PARITY_s3 --> PD_GHOST_PARITY_s4
  PD_GHOST_PARITY_s5["EXACT: chi is the Clifford volume element and exists in every even dimension, so t..."]
  PD_GHOST_PARITY_s4 --> PD_GHOST_PARITY_s5
  PD_GHOST_PARITY_chk{"CHECK: Before citing R3 as a blocker, ask: is the claim SPECTRAL or KINEMATIC? Spe..."}
  PD_GHOST_PARITY_s5 --> PD_GHOST_PARITY_chk
  PD_GHOST_PARITY_t0("TRAP 2026-08-08")
  PD_GHOST_PARITY_chk -.-> PD_GHOST_PARITY_t0
  PD_GHOST_PARITY_t1("TRAP 2026-08-08")
  PD_GHOST_PARITY_chk -.-> PD_GHOST_PARITY_t1
  PD_SOURCE_NOTATION["PD-SOURCE-NOTATION"]
  PD_SOURCE_NOTATION_s0["EXACT: Curt states raw (3,7), traceless (3,6), flipped (4,6). The repository compu..."]
  PD_SOURCE_NOTATION --> PD_SOURCE_NOTATION_s0
  PD_SOURCE_NOTATION_s1["EXACT: The mirror is FORCED, not inferred: all three forms are even in A = g^-1 B,..."]
  PD_SOURCE_NOTATION_s0 --> PD_SOURCE_NOTATION_s1
  PD_SOURCE_NOTATION_s2["EXACT: So Curt writes (negatives, positives). His blocks (4,6)+(1,3) = (5,9) == th..."]
  PD_SOURCE_NOTATION_s1 --> PD_SOURCE_NOTATION_s2
  PD_SOURCE_NOTATION_s3["AUTHOR-STATED: The 2021 draft eq (12.19) prints TY^{7,7} = TX^{1,3} + N^{6,4}: base, fibre..."]
  PD_SOURCE_NOTATION_s2 --> PD_SOURCE_NOTATION_s3
  PD_SOURCE_NOTATION_s4["AUTHOR-STATED: Weinstein independently fixes the base at (1,3) in his own voice and gives ..."]
  PD_SOURCE_NOTATION_s3 --> PD_SOURCE_NOTATION_s4
  PD_SOURCE_NOTATION_chk{"CHECK: Declare plus-first or negatives-first before adding any signature pair"}
  PD_SOURCE_NOTATION_s4 --> PD_SOURCE_NOTATION_chk
  PD_SOURCE_NOTATION_t0("TRAP 2026-08-04")
  PD_SOURCE_NOTATION_chk -.-> PD_SOURCE_NOTATION_t0
  PD_SOURCE_NOTATION_t1("TRAP 2026-08-08")
  PD_SOURCE_NOTATION_chk -.-> PD_SOURCE_NOTATION_t1
  PD_SOURCE_NOTATION_t2("TRAP 2026-08-08")
  PD_SOURCE_NOTATION_chk -.-> PD_SOURCE_NOTATION_t2
  PD_CONDITIONAL_VS_SETTLED["PD-CONDITIONAL-VS-SETTLED"]
  PD_CONDITIONAL_VS_SETTLED_s0["EXACT: The declared-base resolver: filed, then falsified the same afternoon by the..."]
  PD_CONDITIONAL_VS_SETTLED --> PD_CONDITIONAL_VS_SETTLED_s0
  PD_CONDITIONAL_VS_SETTLED_s1["EXACT: The non-equivariance retyping: rejected on hostile review; '-g is a differe..."]
  PD_CONDITIONAL_VS_SETTLED_s0 --> PD_CONDITIONAL_VS_SETTLED_s1
  PD_CONDITIONAL_VS_SETTLED_s2["EXACT: The REAL-CLIFFORD-FORM reopen: withdrawn. The row asks which algebra the so..."]
  PD_CONDITIONAL_VS_SETTLED_s1 --> PD_CONDITIONAL_VS_SETTLED_s2
  PD_CONDITIONAL_VS_SETTLED_s3["EXACT: The underlying fact -- the mixed-notation sum -- survived all three and was..."]
  PD_CONDITIONAL_VS_SETTLED_s2 --> PD_CONDITIONAL_VS_SETTLED_s3
  PD_CONDITIONAL_VS_SETTLED_chk{"CHECK: File the finding with its receipt"}
  PD_CONDITIONAL_VS_SETTLED_s3 --> PD_CONDITIONAL_VS_SETTLED_chk
  PD_CONDITIONAL_VS_SETTLED_t0("TRAP 2026-08-08")
  PD_CONDITIONAL_VS_SETTLED_chk -.-> PD_CONDITIONAL_VS_SETTLED_t0
  PD_SIGNATURE_PARITY === PD_SOURCE_NOTATION
  PD_SIGNATURE_PARITY === PD_GHOST_PARITY
  PD_GHOST_PARITY === PD_SIGNATURE_PARITY
  PD_GHOST_PARITY === PD_CONDITIONAL_VS_SETTLED
  PD_SOURCE_NOTATION === PD_SIGNATURE_PARITY
  PD_CONDITIONAL_VS_SETTLED === PD_SIGNATURE_PARITY
  PD_CONDITIONAL_VS_SETTLED === PD_GHOST_PARITY
  PD_CONDITIONAL_VS_SETTLED === PD_SOURCE_NOTATION
```

## PD-SIGNATURE-PARITY

**The ambient horn is not cosmetic: (9,5) forbids an odd generation count and (7,7) permits it. A computation on the wrong horn cannot reach three.**

- **Trigger:** Any work touching the generation count, chirality, spinor reality, Kramers/quaternionic structure, or that builds on a Cl(9,5) carrier.
- **Naive reading:** "(9,5) vs (7,7) is a sign convention, so results transfer." They do not. The two are not real-isomorphic and the reality type is observable.

| # | evidence | fact | receipt |
|---|---|---|---|
| 1 | `EXACT` | The DeWitt fibre form is (6,4), and this is INDEPENDENT of the base sign: G(-g) = G(g) exactly. | `tests/signature_fork_equivariance_defect.py` |
| 2 | `EXACT` | So the base sign alone moves the ambient: (3,1)->(9,5), (1,3)->(7,7). | `tests/signature_fork_equivariance_defect.py` |
| 3 | `EXACT` | Cl(9,5) = M(64,H) quaternionic; Cl(7,7) = M(128,R) real. Not real-isomorphic. | `tests/majorana_weyl_forces_the_seven_seven_horn.py` |
| 4 | `EXACT` | Majorana-Weyl exists iff p-q = 0 mod 8. Of the reachable horns only (7,7) qualifies. | `tests/majorana_weyl_forces_the_seven_seven_horn.py` |
| 5 | `THEOREM` | Quaternionic structure forces Kramers doubling, hence EVEN multiplicity. | `canon/no-go-quaternionic-parity-generation-sector.md` |
| 6 | `CONDITIONAL` | Three generations is ODD. So (9,5) structurally forbids the target; (7,7) permits it. | `explorations/twentyfive-lens-council-on-the-signature-decision-2026-08-08.md` |

**CHECK.** State which horn the work stands on. If Cl(9,5), say so and say whether the result is horn-robust. Do NOT let a (9,5) result silently stand in for the source-aligned reconstruction.

**Traps that actually happened:**

- **2026-08-04** — Wave K settled REAL-CLIFFORD-FORM on a MIXED-NOTATION sum: it took the vertical block in repository notation ((7,3)->(6,4)) and the horizontal in the source's ((1,3)), then added them. Read consistently in either notation the sum is (9,5), never (7,7).
  - *Cost:* Four days as the program's primary reconstruction burden on a retracted derivation.
  - *Receipt:* `lab/process/hostile-reviews/2026-08-08-real-clifford-form-settlement-review.md`
- **2026-08-08** — An agent wrote "Cl(3,1) = M(2,H) and Cl(1,3) = M(4,R)". SWAPPED. Correct: three '+' generators = M(4,R) real; one '+' = M(2,H) quaternionic. A sibling artifact hours earlier had it right.
  - *Cost:* Self-contradiction inside one day; caught by re-derivation, not by review.
  - *Receipt:* `tests/signature_fork_equivariance_defect.py`
- **2026-08-08** — M-H9 was named as the fork's resolver while being built on a COMPLEXIFIED Racah-Speiser module. Cl(p,q) (x) C depends only on p+q, so both horns give M(128,C) -- the module was PROVABLY incapable of discriminating, and returned bit-identical output on both horns.
  - *Cost:* A named resolver that could never have worked; falsified at Tier 1.
  - *Receipt:* `explorations/mh9-tier1-mechanism-falsified-2026-08-08.md`
- **2026-08-08** — The Majorana-Weyl candidate called the (6,4) fibre "pinned" because G(-g)=G(g), but the certificate fixes lambda=1/2 and a trace sign. Base-sign invariance at that input does not derive the coefficient or trace-sign choice; the TT criterion used to prefer the sign is an imported physical input.
  - *Cost:* Nearly promoted a sound conditional implication into a resolver for the highest-fan-out fork by moving the convention one level upstream.
  - *Receipt:* `lab/process/hostile-reviews/2026-08-08-majorana-weyl-conditional-resolver-review.md`

**Invalidates if:** The generation count is shown NOT to be the index whose parity Kramers constrains; or a mechanism supplies the odd '+1' outside the Kramers- constrained sector.

## PD-GHOST-PARITY

**"Ghost parity is blocked" is a SPECTRAL result. Turok-Bateman's parity is KINEMATIC and is not touched by it.**

- **Trigger:** Any work citing R3's sign-blindness, the C-operator, Bender-Mannheim, or concluding that the Turok-Bateman mechanism is unavailable to GU.
- **Naive reading:** "R3 showed the ghost-parity mechanism fails on GU's carrier, so TB is dead here." R3 tested whether the SPECTRAL C is dynamics-derived. TB's parity comes from a two-field O(1,1) EMBEDDING and is defined where the spectral C is not.

| # | evidence | fact | receipt |
|---|---|---|---|
| 1 | `THEOREM` | Bender-Mannheim's C and Turok-Bateman's ghost parity are the SAME operator on the simple-spectrum domain (||C - P_ghost|| -> 3e-8). | `explorations/big-swing-2026-07-06/BIG-SWING-CONFORMAL-CLASS-BLOCKED.md` |
| 2 | `THEOREM` | They come APART at spectral degeneracies, where C exists but is NOT unique. | `explorations/big-swing-2026-07-06/VG-V4-quantize-break-commuting-square.md` |
| 3 | `EXACT` | At the degenerate point the KINEMATIC parity is exactly well-defined ([P_tot, H(0)] = 0.0e+00) while the spectral C dies. | `explorations/big-swing-2026-07-06/VG-V4-quantize-break-commuting-square.md` |
| 4 | `EXACT` | R3's balance is caused by CHI, not by quaternionic structure: {K,chi} = 0 exactly, and the whole native algebra lies in the chirality commutant. | `tests/krein_parity_dichotomy_jk_anticommutation.py` |
| 5 | `EXACT` | Balance requires ANTIcommutation with K. Kramers alone gives only EVENNESS. GU's J_quat COMMUTES with the Krein Gram ([beta_S, J_quat] = 0.0e+00). | `tests/krein_parity_dichotomy_jk_anticommutation.py` |
| 6 | `EXACT` | chi is the Clifford volume element and exists in every even dimension, so the chi wall is NOT horn-specific. | `tests/krein_parity_dichotomy_jk_anticommutation.py` |

**CHECK.** Before citing R3 as a blocker, ask: is the claim SPECTRAL or KINEMATIC? Spectral no-goes do not constrain an embedding-defined parity. Also state whether the arena is FIXED -- every GU test so far searched a fixed arena's commutant, and TB's mechanism works by enlarging it.

**Traps that actually happened:**

- **2026-08-08** — An agent conjectured R3's sign-blindness was a Kramers artifact of the (9,5) horn, and put that in a handoff prompt as a task to test. WRONG: Kramers gives evenness, not balance; the source is chi; and both inputs were already computed and filed months earlier.
  - *Cost:* A wrong task issued to another agent; retracted the same day.
  - *Receipt:* `tests/krein_parity_dichotomy_jk_anticommutation.py`
- **2026-08-08** — The {J,K} dichotomy was stated more broadly than it holds. It is a SPECTRAL statement and says nothing about a kinematic parity.
  - *Cost:* Scope overreach, caught by a specialist panel the same day.
  - *Receipt:* `explorations/specialist-panel-on-the-degenerate-point-2026-08-08.md`

**Invalidates if:** The kinematic parity is shown to require a spectral C after all; or GU's chirality operator is shown not to anticommute with K in the relevant arena.

## PD-SOURCE-NOTATION

**Curt Jaimungal is the EXPOSITOR; Weinstein is the AUTHOR. They use OPPOSITE signature notations. Never add pairs across the two.**

- **Trigger:** Any work quoting a signature pair from a transcript, or citing "the source" for a numeric signature claim.
- **Naive reading:** "'Curt/Eric' is one source." They are two, they disagree in notation, and only one is authorial.

| # | evidence | fact | receipt |
|---|---|---|---|
| 1 | `EXACT` | Curt states raw (3,7), traceless (3,6), flipped (4,6). The repository computes (7,3), (6,3), (6,4). Exact mirrors, three for three. | `tests/source_signature_notation_is_mirrored.py` |
| 2 | `EXACT` | The mirror is FORCED, not inferred: all three forms are even in A = g^-1 B, so they are bit-identical at every base sign. Curt's pairs are unreachable by any base choice. | `tests/source_signature_notation_is_mirrored.py` |
| 3 | `EXACT` | So Curt writes (negatives, positives). His blocks (4,6)+(1,3) = (5,9) == the repository's (9,5). His ASSERTED (7,7) does not follow from them. | `explorations/source-signature-notation-is-mirrored-2026-08-08.md` |
| 4 | `AUTHOR-STATED` | The 2021 draft eq (12.19) prints TY^{7,7} = TX^{1,3} + N^{6,4}: base, fibre and total in ONE equation, one notation, summing correctly. | `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md` |
| 5 | `AUTHOR-STATED` | Weinstein independently fixes the base at (1,3) in his own voice and gives a criterion for the trace sign (Pati-Salam Spin(6)xSpin(4)). | `lab/sources/curt-iceberg-77-primary-transcript-fetch-2026-08-08.md` |

**CHECK.** Declare plus-first or negatives-first before adding any signature pair. Attribute to EXPOSITOR or AUTHOR, never to "the source". Treat an expositor's guess about the author's beliefs as what it is.

**Traps that actually happened:**

- **2026-08-04** — REAL-CLIFFORD-FORM's settled_how cites 'Curt/Eric's exact source-typed arithmetic' as ONE object.
  - *Cost:* The conflation is what allowed the mixed-notation sum to survive review.
  - *Receipt:* `lab/process/layer0-fork-registry.yaml`
- **2026-08-08** — An agent read Curt's "I believe Eric isn't sure which of these is the sector of our universe" as the AUTHOR declining to choose. It is the expositor's belief about the author's state of mind. Weinstein does choose, in his own voice, and gives a reason.
  - *Cost:* Weighed as authorial evidence in a fork assessment.
  - *Receipt:* `lab/sources/curt-iceberg-77-primary-transcript-fetch-2026-08-08.md`
- **2026-08-08** — Having found the mirror in Curt's transcript, an agent generalised to "there is NO source/repository convention divergence". Correct about Curt, WRONG about the author: both authorial surfaces say base (1,3) while the repository computes on (3,1).
  - *Cost:* A resolver filed and falsified within hours.
  - *Receipt:* `lab/process/layer0-fork-registry.yaml`

**Invalidates if:** The 2021 draft is shown to use negatives-first after all, which would make its (12.19) inconsistent rather than the transcript's arithmetic.

## PD-CONDITIONAL-VS-SETTLED

**A correct FACT does not license a disposition. Keep findings and dispositions in separate artifacts.**

- **Trigger:** Any move to change a ledger row, canon verdict, fork status, or to declare something settled or reopened.
- **Naive reading:** "The computation is right, so the conclusion follows." On 2026-08-08 three dispositions were proposed off ONE correct fact and all three were wrong.

| # | evidence | fact | receipt |
|---|---|---|---|
| 1 | `EXACT` | The declared-base resolver: filed, then falsified the same afternoon by the notation mirror. | `lab/process/layer0-fork-registry.yaml` |
| 2 | `EXACT` | The non-equivariance retyping: rejected on hostile review; '-g is a different point in a different orbit', not a relabeling. | `lab/process/hostile-reviews/2026-08-08-signature-fork-equivariance-review.md` |
| 3 | `EXACT` | The REAL-CLIFFORD-FORM reopen: withdrawn. The row asks which algebra the source USES, which author assertion answers even when the author's arithmetic does not. | `lab/process/hostile-reviews/2026-08-08-real-clifford-form-settlement-review.md` |
| 4 | `EXACT` | The underlying fact -- the mixed-notation sum -- survived all three and was correct every time. | `tests/source_signature_notation_is_mirrored.py` |

**CHECK.** File the finding with its receipt. File the disposition separately and put it through the three charges. If a proposal would change a row, it is a PROPOSAL until reviewed -- see improvement register M-S1..M-S4 for the shape.

**Traps that actually happened:**

- **2026-08-08** — Three dispositions in one day off one correct fact; all three wrong, each caught by a different mechanism (review, review, concurrent work arriving first).
  - *Cost:* Two registry writes and one near-miss on the program's highest-fan-out row.
  - *Receipt:* `lab/process/hostile-reviews/2026-08-08-real-clifford-form-settlement-review.md`

**Invalidates if:** Never. This is a process invariant.

