---
artifact_type: exploration
status: exploration
created: 2026-07-11
title: "H39 (Wave 16 / SG4): which K-class the source action names on the RS generation carrier -- NARROWED (B-leaning), the count does NOT collapse to exactly 3, selecting it does NOT break gravity's [P,S]=0, and the K-class is a genuine postulate. The count is now a conditional-theorem twin of gravity on ONE coherent residual."
grade: "COMPUTED (exact K-theory backbone reproduced two independent ways each; actual (9,5) derived Z/3 triplet on the verified Cl(9,5) rep; Q3 arena-orthogonality + Krein-self-adjoint positive control exact) / ARGUED (the field-space declaration is arithmetic-undecidable per the prior mutual-exclusion certificate; the B-lean is GU-commitment + published-theorem grade). Reconstruction-tier, internal. No canon promotion; no generation-count movement; SG4 unchanged. External publication pauses for Joe."
depends_on:
  - tests/wave16/H39_sourceaction_kclass.py
  - tests/wave15/H38_z3_chiral_selector.py
  - canon/gamma-traceless-38-adjudication-RESULTS.md
  - canon/carrier-bit-decision-campaign-RESULTS.md
  - canon/ghost-parity-krein-synthesis.md
  - papers/candidates/one-residual-complete-picture/one-residual-complete-picture-2026-07-11.md
scripts:
  - tests/wave16/H39_sourceaction_kclass.py
---

# H39 -- SG4, the count's decider: which K-class, select-vs-permit, gravity coherence, forced-vs-postulate

Test: `tests/wave16/H39_sourceaction_kclass.py` (deterministic, fixed seeds, exact; 14/14 PASS, exit 0, ~7 s).

Wave 15 (H38) proved the count decider must be **3-primary AND index-changing** (a ghost-parity
condition is 2-primary and index-preserving, so it permits the vectorlike 3+3 but never selects a
chiral 3). H39 attacks the single object that carries that requirement: the K-class the unbuilt GU
source-action operator names on the Rarita-Schwinger (spin-3/2) generation carrier -- the repo's SG4.
The load-bearing new result is **Q3**: selecting the count and clearing gravity's ghost live in
arithmetically orthogonal arenas, so they are coherent on one residual (they do not trade off).

## The four verdicts

### Q1 -- which K-class? NARROWED, B-LEANING (not forced) [COMPUTED backbone + ARGUED name]

The two published RS carriers are reproduced exactly, each by two independent routes:

| carrier | twist | index on K3 | route 1 (density) | route 2 (additivity) | mod 3 | order-3 rho |
|---|---|---|---|---|---|---|
| **A** ghost-subtracted | `T_C - 1_C` | **-42** | `21 sigma/8` | `-40 + 2(-1)` | **0** | `(0,0,0)` ZERO |
| **B** geometric gamma-traceless | `T_C + 1_C` | **-38** | `19 sigma/8` | `-40 + 2(+1)` | **1** | `(0,2,1)/3` NONZERO |
| bare (control) | `T_C` | -40 | `5 p1/6` | `-40 + 0` | 2 | `(0,1,2)` |
| double (control) | `T_C - 2_C` | -44 | `11 p1/12` | `-40 + 2(-2)` | 1 | `(0,2,1)` |

(`sigma_K3 = -16`, `p1 = 3 sigma = -48`; no `chi(K3)` imported.) The order-3 rho is reproduced two
independent ways that agree: (i) the exhaustively-verified class law `rho_j = -(j/3) ind (mod Z)`,
and (ii) the Nikulin multiplier `c = tr(g|T_C) +/- 1` with `tr(g|T_C) = -2` computed from the
order-3 fixed-point rotation `diag(zeta, zeta)` on the holomorphic tangent -- `c_A = -3 = 0 (mod 3)`
kills the class, `c_B = -1 != 0` keeps it.

**Carrier B is the unique index-CHANGING published carrier** (`-38 != 0 mod 3`, nonzero rho); carrier
A is 2-primary (`-42 = 0 mod 3`). So *if* the source action names a carrier that can select the count,
it must name B. **But which carrier it names is a field-space DECLARATION that arithmetic provably
cannot decide** -- the carrier-bit mutual-exclusion certificate (prior canon): on the gamma-trace-
constrained field space no linear nilpotent ghost extension exists (`-> B`); on the full field space
an exact BRST 4-term complex exists (`-> A`). Both are internally coherent. The H23 fact that
`[P,S]=0` holds (`M_D` Krein-self-adjoint) is **sign-blind and 2-primary** (`3-part(2)=1`): it does
NOT name A vs B. GU's stated commitments -- ungauged massive RS matter, whose Porrati-Rahman causality
cure *is* the gamma-tracelessness constraint defining B's field space -- **B-lean** (three B-passages
vs one ambiguous A-passage), at evidence tier. **Verdict: NARROWED to B under GU's commitments, not
forced.**

### Q2 -- does index-changing SELECT rank-3, or merely permit odd? NARROWED, NOT SELECTED [COMPUTED]

On the actual `(9,5)` rep the derived Z/3 carrier is present exactly: `ker Gamma = 1664`, triplet
`192 = 3 x 64`, `3 = dim Lambda^2_+(R^4)` (Hodge-star `+1` eigenspace, derived, not imported).

The trap the task warned against, made explicit and avoided: **a net chiral index of exactly 3 has
residue `3 mod 3 = 0` -- which is carrier A's residue, not B's.** So no mod-3 residue can certify
"3". Carrier B's residue is `1` (nonzero, hence genuinely index-changing), and its rho `(0,2,1)`
engages 2 of the 3 Z/3 sectors. The number of chiral slots has a **derived ceiling** `dim Lambda^2_+
= 3`, but the realized odd rank is a free integer in `{1, 3}` (full vs partial chiralization, both
index-changing). **Verdict: the index-changing carrier B guarantees NONZERO, odd, 3-primary chiral
content -- a real narrowing -- but does NOT pin the count to exactly 3.** This is a NARROWING, not a
resolution. (Manufacturing a "forces 3" here would be exactly the Wave-14/15 trap.)

### Q3 -- gravity coherence: does selecting the count BREAK [P,S]=0? NO CLASH -- REINFORCING [COMPUTED]

This is the new load-bearing computation. The naive tension: an index-changing operator is "not
Krein-unitary", and gravity's ghost clears only if `[P,S]=0` (Krein-unitary dynamics) -- so does
selecting the count cost the clearance? **No, and the reason is exact:**

1. **Arena-orthogonality.** The count index is 3-primary; ghost parity `P` is 2-primary (`P^2=I`).
   `gcd(2,3)=1` and `|Hom(Z/2,Z/3)|=1` (the zero map), so the 2-primary Krein-unitarity constraint
   `[P,S]=0` imposes **zero** constraint on the 3-primary index. They cannot trade off.
2. **The premise is false (positive control).** "Index-changing => not Krein-unitary" conflates the
   OPERATOR with its FLOW. A Krein-self-adjoint operator `M` (whose flow `exp(iMt)` is Krein-UNITARY
   for all `t`) can carry a **nonzero** chiral index: built explicitly with `tr(gamma) = +1 != 0`
   while `exp(iMt)` stays unitary. Self-adjointness does **not** force index 0 (canonical witness:
   the K3 Dirac operator is formally self-adjoint with index `-2`). Krein-unitarity is a property of
   the flow (it preserves the 2-primary signature); the count is the generator's Fredholm index (a
   3-primary K-class datum) -- a different object.
3. **The two indices are distinct.** The Wave-15 physical `G5`-trace (fixed at `0` by `[P,S]=0`,
   reproduced here on the 6-dim cross-chirality Krein model, `[P,S]=2e-15`, Krein-unitarity residual
   `2e-15`) is the 2-primary index; the count is the orthogonal 3-primary K-class grading index.
   Preserving the former leaves the latter untouched.

**Verdict: NO CLASH. Selecting the count (carrier B, 3-primary, index-changing) and clearing gravity's
ghost (`[P,S]=0`, 2-primary, Krein-unitary) coexist on one source action -- arena-orthogonal and
mutually reinforcing.** This sharpens the one-residual thesis: the count face and the gravity face are
not two competing constraints on `M_D` but two arithmetically orthogonal readings of it.

### Q4 -- forced or postulate? GENUINE POSTULATE [COMPUTED + adversarial]

Neither carrier is excluded by `(9,5)` + positivity + no-import: both are coherent field-space
declarations (mutual-exclusion certificate). GU's commitments B-lean but do not force. Adversarial
firewall clean: nothing imported -- the only `3` is `dim Lambda^2_+` (computed); B's residue `1`
rides `ind = -38 = 19 sigma/8` with `sigma = -16` from K3; no `3 / 24 / (24-8) / 155.36` anywhere.
**Verdict: SG4 is a genuine postulate -- the fermion twin of H27's gravity soldering.** The count is
a conditional theorem modulo one K-class declaration; a forced build is the only resolver, and a free
build p-hacks the carrier.

## COMPUTED vs ARGUED ledger

- **COMPUTED (exact):** the four carrier indices (two routes each); the mod-3 residues; the order-3
  rho classes (class law + Nikulin multiplier, agreeing); the actual `(9,5)` derived Z/3 triplet
  `192=3x64` and `dim Lambda^2_+ = 3`; the residue-vs-"3" trap arithmetic; Q3's `gcd`/`Hom` arena
  facts, the Krein-self-adjoint-with-nonzero-index positive control, and the preserved 2-primary
  `G5`-trace under a genuine `[P,S]=0` Krein-unitary; the no-import firewall.
- **ARGUED (evidence/theorem tier, not machine-decided):** which carrier the built action *names*
  (arithmetic-undecidable per the mutual-exclusion certificate; the B-lean rides GU commitments +
  published theorems); that Q3's arena-orthogonality transfers from the toy 2-primary/3-primary
  factorization to the true fibered RS/`Y14` operator (the factorization is exact in the arenas,
  in-house for the globalized operator).

## Honest limits (do not overclaim)

1. **No carrier is named by computation.** Q1 does not resolve A-vs-B; it re-confirms (on a fresh
   route) that B is the *only* index-changing option and that the choice is a declaration. A "the
   source action names B" claim would require building the action -- which a free build p-hacks.
2. **Q2 does not produce a 3.** The index-changing carrier guarantees odd/nonzero 3-primary content
   with a derived ceiling of 3 slots, but the realized rank is not pinned to 3. Reading `residue 1`
   or `rho (0,2,1)` as "3 generations" would be the trap; and note a *net index* of 3 would sit in
   residue 0 (carrier A's), so the mod-3 datum cannot even in principle certify the target.
3. **Q3's coherence is arena-level.** It proves the count-selector and the ghost-clearance do not
   compete arithmetically and that self-adjointness permits nonzero index; it does not prove the
   *same* built `M_D` simultaneously realizes both -- that too rides the unbuilt action. What is
   excluded is the naive tension ("index-changing costs the clearance"); what remains open is the
   joint realization, which is the one unbuilt object.
4. **The B-lean is evidence, not verdict** (carrier-bit campaign grade): three B-passages vs one
   ambiguous A-passage; the graded-IG A-door stays live at toy grade.

## RE-RANK signal

**H39: NARROWED (not resolved).** The count decider is now pinned to a single, sharply-named object
-- the K-class the source-action operator names on the RS carrier -- with B the unique index-changing
candidate and a B-lean at GU-commitment grade; and the two long-standing faces of the residual (the
count and the gravity soldering) are shown **coherent on one residual** (Q3: selecting the count
preserves `[P,S]=0`; arena-orthogonal, reinforcing).

- **The count is now a conditional theorem twin of gravity:** located-not-forced *modulo one K-class
  declaration*, exactly as gravity is Stelle-clear *modulo one soldering postulate* (H27). Q3 upgrades
  the relationship from "same unbuilt object" (prior) to "same object, and the two selections do not
  conflict".
- **Single next object:** a **forced** construction of the source-action field-space declaration
  (gauged/BRST full field space `-> A` vs gamma-trace-constrained `-> B`) -- the *same* unbuilt object
  as gravity's soldering. The mutual-exclusion certificate guarantees no cheaper computation
  substitutes; a free build p-hacks the carrier.
- **No canon movement, no generation-count movement, no public-posture change.** SG4 unchanged; the
  generation count stays OPEN (located, not forced, maximally hardened).
