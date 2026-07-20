---
artifact_type: exploration
doc_type: adversarial_verification
status: "hostile verification of explorations/conditional-forcing-minimal-input-2026-07-20.md + tests/channel-swings/conditional_forcing_probe.py (commit f513fcf); independent probe exit 0 (14 [E] + 2 [F] + 4 [T], 286.2 s full breadth; reduced-breadth ladder 247.7 s); verdict NOT-DRY (zero computational refutations; one material attribution fork, one material X1.5 reframe, one closed exhaustion gap)"
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (hostile verify: conditional forcing)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
target: explorations/conditional-forcing-minimal-input-2026-07-20.md
target_probe: tests/channel-swings/conditional_forcing_probe.py
probe: tests/channel-swings/verify_conditional_forcing_probe.py
related:
  - explorations/conditional-forcing-minimal-input-2026-07-20.md
  - explorations/prereg-trit-internal-successor-2026-07-20.md
  - explorations/63-persona-steelman-narratives-2026-07-20.md
  - tests/channel-swings/k1_reframe_probe.py
sources:
  - "P. Olum, Mappings of manifolds and the notion of degree (Ann. of Math. 1953): degree of a map of 3-dim lens spaces L(n,1) inducing multiplication by r on pi_1 is r^2 mod n; the weight-matched equivariant maps here descend to L(n,1) with r = 1, so every member is 1 mod n. Used at the same grade the original used it (cited theorem + per-rung witnesses); consistent with all witnessed degrees across five rungs including two members the original never ran (+13 at Z/6, +21 at Z/5)."
  - "Borsuk-Ulam (odd maps S^3 -> S^3 have odd degree; no continuous odd S^3 -> S^1), as in the original."
  - "Milnor/standard: right multiplication by a unit quaternion is an element of SO(4); degree +1 by det. Used as the preimage-free route to X2's class."
---

# Hostile verification: conditional forcing / minimal input (f513fcf)

**Assignment.** The result is blockbuster-adjacent ("the minimal input is one Z/6 anchor; the
bit is its cube"); house base rate says assume one asserted-but-never-checked error. Break it.
Independent probe: `tests/channel-swings/verify_conditional_forcing_probe.py` -- exit 0, ALL
PASS, 14 [E] + 2 [F] (setup [T] = 4), 286.2 s full breadth (deterministic; a labelled
`VCFP_FAST=1` reduced-breadth ladder runs in 247.7 s and divides only the Newton-counter start
counts -- every closed-form, linear-algebra, and exact-identity result is breadth-independent).
The original probe was re-run first: exit 0, ALL PASS, 238.6 s (doc says ~265 s) -- the
REPRODUCED baseline.

**Method separation (nothing decisive re-used).** A new signed-preimage counter (numerical
derivatives, Gram-Schmidt frames, own regular values W3/W4, own seeds, own sign rule),
power-certified on identity/antipodal/conjugation/cube before use -- the conjugation (-1)
control the original never ran. Closed-form join-map degree enumeration (bisection + explicit
phase roots; no Newton search) certifying degrees 3, 7, 9, 13, 21 with every preimage verified
individually. X2's class computed by exact linear algebra (right multiplication is orthogonal,
det = +1) -- no preimage counting anywhere on the decisive claim. Bookkeeping re-derived from
`order24(m) = 24/gcd(24, m)` and `gcd(24, 16c) = 8 gcd(3, c)`, checked to |c| <= 1000
(original: 60). X1.5 re-attacked under non-Gaussian reader and state laws, with the original's
own decisive cases independently re-evaluated on my regular values. The minimality lattice
re-attacked with two witnesses the original never constructed (join(13,1), join(21,1)).

**Method-integrity note (recorded, not hidden).** My first-pass Newton counter, at reduced
breadth, returned an even degree (+2) for a self-dual tau-flip form -- structurally impossible
for a deck-odd map (Borsuk-Ulam forces odd degree). That was a counter under-resolution on
high-degree clustered-preimage forms, NOT a finding: caught by the built-in oddness guard.
Resolution: the load-bearing independent results use breadth-immune machinery (closed-form join
enumeration; exact linear-algebra det for X2; exact identities); the auxiliary high-degree
self-dual/reader integers use the target's robust analytic-Jacobian root-finder on MY
independent regular values W3/W4 (independent value, robust method). No claim rests on the
fragile path; every reported integer is either closed-form/exact or agreed by two regular
values.

## Per-claim verdict table

| # | Claim (as staked) | Verdict | Receipt |
|---|---|---|---|
| 1 | Setup: count condition is mod-3; deck parity independent; order(J(64c)) = 3 iff 3 not \| c; 192 = 0 mod 24 -> order 1 | **CONFIRMED** | closed-form gcd re-derivation, all \|c\| <= 1000; the "192 bookkeeping" is right |
| 2 | X1 (bit alone) insufficient, three legs | **CONFIRMED** | leg A fresh seeds (gates sign-decoration-invariant); leg B my counter, my regular values (sigma-flip = exact global negation, rebuilt from -K_S kernels from first principles; class unchanged / tau-negated); leg C closed-form join(3,1) = +3, deck-odd 0.0 |
| 3 | X1.5 (bit + generic reader) passes both gates, fails "on class scatter INCLUDING the zero class" | **CONFIRMED but REVISED (MATERIAL framing)** | gates pass under non-Gaussian (uniform/Laplace) readers -- not a Gaussian artifact. But the KILL does NOT rest on generic scatter: my 8-case non-Gaussian sweep scattered only over {-1, +1}, and BOTH give order 3 (k = 8, 16 mod 24) -- under those laws X1.5 would appear to SUFFICE. The kill rests SOLELY on the c = 0 mod 3 order-killer, which I reproduced on the original's own Gaussian consumer-shape readers (deterministically rebuilt) via my independent regular values W3/W4: degrees `[(1,1),(-1,-1),(3,3),(3,3)]` -- the +3 order-killer confirmed. It is reader/draw-law-sensitive (absent in my non-Gaussian sweep). The original's phrasing "class is fixture noise INCLUDING the zero class" is true but its emphasis misleads: scatter alone is not the kill; the state-dependent order-KILLER is |
| 4 | X2 (Sp(1)-equivariant trivialization) suffices; equivariance forces right translation; degree +1 oracle-independent; G2 by exact identity | **CONFIRMED** | substitution proof (Phi(v) = v Phi(1)) at float grade (not just dyadic); degree +1 by det of the orthogonal right-multiplication matrix (40 random q0 + both orientations, preimage-free route); K_S C - C conj(K_S) = 0.0 re-verified, zero cross-sector leak, Gram orthonormal (my seeds) |
| 5 | Minimality ladder: Z/2, Z/3, Z/4 fail; Z/6 first sufficient; "the subgroup lattice between X1 and X2 is exhausted" | **REVISED (immaterial to the rung, material to the wording)** | Z/5 was NEVER EXAMINED -- the written exhaustion has a hole. Closed here: join(21,1) is Z/5-equivariant, exactly deck-odd, degree +21 by closed-form enumeration, 3 \| 21 -> order 1. With Sp(1)'s unique involution (q^2 = 1, \|q\| = 1 => q = +-1: no Klein group, no S_3), the order-<=-6 lattice is exactly {Z/2..Z/6} and exhaustion becomes genuinely complete -- one rung later than the original left it |
| 6 | Z/6 rung: every member 1 mod 6; class moves (+1, +7) but stays order-3 | **CONFIRMED, extended** | join(7,1) re-certified on independent machinery (+7, 7 enumerated preimages); NEW member join(13,1) = +13 = 1 mod 6, order 3; u1 generic member +1 on my counter; Olum congruence consistent with all eight witnessed degrees across five rungs |
| 7 | "The minimal X is ONE ORDER-SIX PHASE REFERENCE; the bit is exactly its cube" | **REVISED (MATERIAL)** | the accounting fork, below. Under the program's own gate semantics the minimal EXTERNAL input is ONE TRIT (Z/3); the Z/2 factor is native. The Z/6 headline holds only under a second semantics that contradicts the machinery the probe itself imports |
| 8 | "Its cube is the payload bit" as an identity of actions | **CONFIRMED as arithmetic; the NAMING is an unproven identification** | act(zeta6^3, v) = -v exactly (the anchor's cube IS the fiber deck action); but the target's own legs A/B prove the PROGRAM's payload bit (K_S/pin-plane orientation, "externally valued" per the probe's own X1 definition) is gate-inert and class-inert -- it never acts on the fiber at all. Equating the deck Z/2 with the payload Z/2 is exactly steelman question #4 (63-persona doc), marked OPEN there and silently assumed closed here |
| 9 | Planted weight-blind oracle rejected by G1 while passing the Z/2 shadow | **CONFIRMED** | rebuilt independently on the other complex axis: deck shadow 0.0, reach 0.0, 2.0 discontinuity jump |
| 10 | X1.5 receipt "43-run scout sweep across 3 readers" | **REPRODUCED-ONLY (receipt hygiene)** | no artifact of the sweep exists in the repo (comment-only); the probe itself runs 2 readers x 4 cases. The CONCLUSION survives anyway (my independent 8-case non-Gaussian sweep reproduces the scatter), but the 43-run/3-reader numbers are unverifiable as stated |

## A. The main finding: the accounting fork (claim 7)

The count condition is mod-3 and admissibility is parity -- the original says so itself
(Section 1). The question the headline turns on is WHO PAYS for the parity demand, and the
target is internally split on it:

- **Section 1 (the formal statement)** lists "deck admissibility: exact co-flip
  q(-v) = -q(v)" as a GATE, in the same bullet list as G1 and G2 -- conditions a transport
  must pass, not data the input must supply. The frozen inventory in the same sentence
  includes "the spin-lift family with verified co-flip deck -I": the double cover and its
  deck sign are NATIVE, verified structure.
- **The imported machinery agrees.** `k1_reframe_probe` (re-run live, all checks passing,
  inside both the original probe and mine) excludes the deck-even contraction variant
  natively -- its own check text: "excluded by the verified co-flip" -- and kills K1 partly
  BECAUSE its posit-free section restricts to deck +I, "NOT the verified co-flip -I". No
  external bit is charged for either exclusion. Both receipt checks are asserted live and
  passing in my probe.
- **The minimality ladder charges differently.** Z/3 is failed NOT on the count (its count
  side is conceded harmless) but because the type CONTAINS a deck-inadmissible member,
  (z1^4, z2). Under the Section-1 / k1 semantics that member is simply rejected by the gate
  -- exactly as the planted weight-blind oracle's G1 failure did not count against X2. The
  ladder quietly switches to a second semantics ("the anchor must itself supply deck parity")
  for exactly the one rung where the two semantics disagree.

The two semantics provably coincide everywhere else and provably fork at Z/3, because
(machine-witnessed on every witness in my probe):

    deck-odd  AND  Z/3-equivariant   <=>   Z/6-equivariant      (zeta6 = -zeta3^2)

So the map-set the original certifies as "the Z/6 type" IS the gate-passing part of the bare
Z/3 type. All its members have degree 1 mod 3 (Olum, r^2 = 1 for both generators -- the
original's own no-orientation-needed argument), hence 3 never divides c, hence order 3 forced;
the identity member witnesses non-emptiness. Therefore:

- **Under the program's own gate semantics: the minimal EXTERNAL input is ONE TRIT (Z/3).**
  The Z/2 half of the Z/6 is native bookkeeping (the verified co-flip), not external payload.
  The result gets STRONGER: the geometry is one trit short, not one sextet short.
- **Under the anchor-supplies-parity semantics: Z/6, as published.** But then the same
  semantics should have been applied throughout, and the native deck exclusions inside the
  imported k1 run would need re-pricing.

Either way the conditional forcing itself SURVIVES -- this is an attribution revision, not a
kill. But the headline sentence "the minimal input is one Z/6 anchor and the bit is its cube"
is not semantics-stable, and the sharpened claim it feeds (the pre-registered trit-internal
check, 6b384c5) inherits the instability -- see D.

## B. The second finding: the exhaustion hole (claim 5)

"Nothing below Z/6 works; the subgroup lattice between X1 and X2 is exhausted (Z/2, Z/3, Z/4
fail; Z/6 is the first sufficient rung)" -- written over a ladder that never examined Z/5.
Z/5 is below Z/6 in order and is a subgroup of neither Z/6 nor of any examined rung, so no
examined witness covers it. Closed here, against the gap and in favor of the rung:

- join(21,1): Z/5-equivariant at 1e-15 (21 = 1 mod 5), exactly deck-odd (both exponents odd),
  NOT Z/6-equivariant (defect O(1)), degree +21 by closed-form enumeration (21 preimages, each
  verified to map onto the regular value, all local signs +1). 3 | 21 -> k = 1344 = 0 mod 24,
  ORDER 1: an order-killer inside the admissible part of the type. Z/5 fails under BOTH
  semantics of Section A (its deck-breaking member join(6,1) also fails admissibility).
- Sp(1) has a unique involution (q^2 = 1, |q| = 1 => 2q0^2 = 2 and q0 u = 0 => q = +-1), so
  Z/2 x Z/2 and S_3 do not embed: every subgroup of order <= 7 is cyclic, and the order-<=-6
  lattice is exactly {Z/2, Z/3, Z/4, Z/5, Z/6}. With Z/5 closed, the exhaustion is complete.
- Non-cyclic candidates above order 6 cannot undercut the rung: a weight character w must send
  the unique involution to -1 for admissibility, and the finite subgroups of Sp(1) with
  noncyclic structure (Q8, dicyclic, binary polyhedral) either kill -1 in the character
  (deck-even, inadmissible type) or factor their forcing power through a cyclic image already
  covered. This closes the "non-cyclic weaker input" attack at the same grade the original
  claims (theorem-shaped argument + witnesses), though it is recorded here as argument, not
  as a new machine check.

## C0. The third finding: X1.5's kill is real but its stated basis is misframed (claim 3)

The original says X1.5 fails because "the class is fixture noise INCLUDING the zero class."
Independent re-attack shows the emphasis is wrong in a way that matters:

- Under my non-Gaussian readers (uniform, Laplace) and non-Gaussian/confined/sparse states,
  the class scattered over {-1, +1} only. But c = -1 -> k = 8 mod 24 and c = +1 -> k = 16 mod
  24 are BOTH order 3. So generic scatter over {+-1} does NOT kill forcing -- under those laws
  X1.5 would appear to SUFFICE.
- The kill therefore rests ENTIRELY on the existence of a c = 0 mod 3 (order-KILLING) member.
  I reproduced that member on the original's own Gaussian consumer-shape readers (rebuilt
  deterministically from their seeds) evaluated on MY independent regular values W3/W4:
  degrees came back `[(1,1), (-1,-1), (3,3), (3,3)]` -- the +3 order-killer confirmed, k = 192
  = 0 mod 24, order 1.
- Crucially, that order-killer is reader/draw-law-SENSITIVE: it did not appear once in my
  8-case non-Gaussian sweep. So the kill is genuine but NARROWER than the prose implies: it is
  "there exists a state (in the Gaussian consumer family) giving the zero class," not "the
  class is generically noise." The original's own adversarial-referee note ("the kill stands on
  class instability") is thus slightly off -- the load-bearing fact is the existence of one
  order-killer, and its frequency is law-dependent. Verdict: CONFIRMED (X1.5 insufficient),
  REVISED (material framing); the conclusion "reading is not anchoring" survives intact.

## C. What was attacked and did NOT break

- **X2 sufficiency** (surface B): the classification is a one-line substitution theorem
  (Phi(v) = v Phi(1)); verified at float grade on 500 random triples, not only on the
  original's dyadic points. The class +1 was re-derived with NO degree counter at all: right
  multiplication by any unit quaternion is orthogonal with det exactly +1 (40 random q0; both
  payload orientations identically, since det(-I_4) = +1). G2-by-identity re-verified with a
  sharper probe (zero cross-sector leak, all four generators, 12 confined draws, my seeds).
  G1 reach re-verified on my own samples (my fiber reach 0.936, state reach 0.589). Note: the
  doc's quoted bars (0.90 / 0.80) are the ORIGINAL run's witnessed values, and are draw-
  dependent -- on my independent draws the fiber bar 0.90 holds but the state bar 0.80 does
  NOT (0.589). This does not touch the claim: the probe's actual CODED gates are 0.5 / 0.1,
  which hold with margin; the 0.90/0.80 figures are run-specific witnesses, not thresholds.
  Recorded as a caption-vs-code slack, immaterial to the verdict.
- **X1's three legs** (surface C): all three re-derived; the sigma-flip-as-negation modeling
  was rebuilt from first principles (-K_S kernels give the exactly negated form tensor, 0.0),
  so the class-preservation needs no count (antipode on the S^3 target, degree +1).
- **The bookkeeping** (surface C attack "is 192 = 0 mod 24 right"): yes; re-derived in closed
  form and extended to |c| <= 1000.
- **The cube arithmetic** (surface E): act(zeta6^3, v) = -v exactly; zeta6^2 = zeta3 exactly;
  Olum r^2 orientation-freedom arithmetic checked both mod 6 and mod 3.

## D. Convention couplings flagged for the pre-registered trit-internal check (6b384c5)

The sibling check runs tonight against f513fcf's battery "imported unmodified". Flags only
(not run here):

1. **The semantics coupling (largest).** The prereg hypothesis ("the minimal external input
   collapses to the payload bit alone") is stated INSIDE the Z/6 accounting. Under the gate
   semantics of Section A, the same computational outcome K-c would support the strictly
   stronger headline "GU + the N4 identification forces the count, no external payload bit
   needed at all" -- and outcome K-a/K-b boundaries move likewise. The executor should report
   which semantics the verdict is read in; the numbers themselves are semantics-neutral.
2. **The fiber-axis convention.** f513fcf's `act(u, v)` fixes the fiber-side U(1) embedding
   (weight (1,1), LEFT multiplication by scalar phases on the commutant side -- right
   multiplication would give weight (1,-1) and a different lens quotient). The original's own
   council noted the fiber-side axis is part of X. If the N4-derived trit is matched through
   this same `act()` for free, that is a smuggled choice and should trigger K-a accounting.
3. **Shared fixtures.** W1/W2 regular values, the 20260722/99 reader seeds, and the
   `u1_oracle` member family are f513fcf's; the prereg controls (scrambled-character trit,
   reader scatter, planted oracle) inherit them. My run demonstrates the decisive quantities
   are stable under independent values/seeds, so this coupling is low-risk -- but the
   scrambled-character control's POWER should be re-demonstrated under the executor's own
   seed, not assumed from f513fcf's.
4. **Receipt hygiene inherited.** The "43-run scout sweep / 3 readers" X1.5 receipt has no
   repo artifact; the prereg's control 4 cites the X1.5 scatter -- it should cite the probe's
   deterministic 4-case subset (or this verification's 8-case independent sweep), not the
   sweep numbers.

## E. Verdict

- Claims 1, 2, 4, 6, 9: **CONFIRMED** (several strengthened) on independent routes.
- Claim 3 (X1.5): **CONFIRMED (insufficient) but REVISED (material framing)** -- the kill rests
  on a state-dependent, law-sensitive c = 0 mod 3 order-killer (reproduced), not on generic
  scatter (which over {+-1} would suffice). Conclusion "reading is not anchoring" stands.
- Claim 5 (exhaustion wording): **REVISED, immaterial to the conclusion** (Z/5 hole closed
  here in the rung's favor).
- Claim 7 (the headline: minimal X = Z/6): **REVISED, MATERIAL** -- semantics-unstable
  attribution; under the program's own gate semantics the minimal external input is ONE TRIT,
  with the Z/2 native. No computation in the original is wrong; the quantifier switch at the
  Z/3 rung is the asserted-but-never-checked step.
- Claim 8 (the cube = the payload bit): **REVISED, MATERIAL** -- true as fiber arithmetic,
  unproven as the claimed identification with the program's payload bit (the target's own
  legs A/B show that bit acting trivially; the identification is steelman question #4, open).
- Claim 10: **REPRODUCED-ONLY** (unverifiable sweep receipt; conclusion independently
  re-established).

**FINAL: NOT-DRY** -- zero computational refutations (every number the original staked
reproduced and survived independent re-derivation, including the +3 order-killer on independent
regular values), but the headline carries one material attribution fork (Z/6 vs trit + native
parity, claim 7), one material unproven identification (deck Z/2 = payload bit, claim 8), one
material X1.5 framing revision (kill is a law-sensitive existence claim, not generic scatter,
claim 3), and one closed exhaustion hole (Z/5, claim 5). The conditional-forcing core
("inventory + a small phase anchor => order 3 forced"; bit-alone and reader-alone provably
insufficient) is solid and, if anything, the fork makes it STRONGER (one trit short, not one
sextet short). The kill attempt failed on the math and succeeded on the accounting.

## Receipts

- Independent probe: `tests/channel-swings/verify_conditional_forcing_probe.py` -- exit 0,
  ALL PASS, 14 [E] + 2 [F] (setup [T] = 4), 286.2 s full breadth (247.7 s reduced-breadth
  ladder, `VCFP_FAST=1`). HEADLINE: "HOSTILE VERIFICATION COMPLETE -- zero computational
  refutations, one MATERIAL attribution fork, one exhaustion gap closed... X1.5 insufficiency
  CONFIRMED but REFRAMED... the minimal EXTERNAL input is ONE TRIT... 'the bit is the cube'
  becomes an identity about native bookkeeping, not about the external payload bit."
- Original probe re-run (inside the verifier): exit 0, ALL PASS; native X0 scatter
  {-1,+1,+3,+5}; counter certificates +1/+3 reproduced.
- Independent machinery power certificates (this run): my Newton counter id +1, antipodal +1,
  conjugation -1, cube +3 (both my regular values); closed-form join(3,1) = +3 with 3
  enumerated preimages, map defect 1.2e-15.
- Key exact identities reproduced: K_S C - C conj(K_S) = 0.0; commutant cross-sector leak 0.0;
  Gram defect 4.4e-16; A(-K_S) + A(K_S) = 0.0; right-mult orthogonality 4.4e-16, |det - 1|
  5.6e-16; zeta6^3 = -1 and act(zeta6^3, v) = -v at 3.7e-16; cube map / Newton agreement.
- Witnessed degree table (this run): X2 all +1 (linear-algebra det, 40 random q0 + both
  orientations); X1 tau-flip +1 (= -base -1); X1 leg C join(3,1) +3; Z/6 join(7,1) +7,
  join(13,1) +13 (NEW), u1 generic member +1; Z/5 join(21,1) +21 (NEW, order-killer); Z/4
  join(9,1) +9; X1.5 non-Gaussian sweep {-1,+1}, original decisive cases {+1,-1,+3,+3}
  reproduced on W3/W4. Full separated set this run: {-1, 1, 3, 7, 9, 13, 21}.
