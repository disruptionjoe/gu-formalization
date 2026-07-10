# LEG-B2 — the graded-IG upstairs door: shadow/subtraction bookkeeping (CORNER (b), leg 4)

**Leg of:** corners swing (the two PARTIAL corners of `canon/carrier-bit-decision-campaign-RESULTS.md`).
**Runnable:** `LEG-B2-shadow-restriction.py` (51/51 checks, exit 0, this session; exact `Fraction` + sympy only).
**Conditionality (updated after B1 landed):** this leg is conditional on LEG-B1 (does a
graded/fermionic extension of the inhomogeneous gauge group exist as a super-Lie algebra?). At this
run, LEG-B1's artifacts ARE present and were machine-read (script PART 7, monotone-stable string
asserts): `run2.log` contains verbatim "PARTS 1-5 complete: 96 checks" and "ALL FOUR candidates
close as super-Lie algebras in BOTH regimes with {odd,odd} valued in the translation slot
Omega^1(ad)" — **the B1-YES existence core is machine-complete at toy grade (minimal ansatz)**;
`run1.log` shows checks through [102] passed (extended-ansatz / gravitino-shadow / locality parts)
then a `StopIteration` crash in B1's PART 7 — so those claims are **prefix-evidenced, not
exit-0-final**, at this leg's run time (B1 was still running in this shared session). BOTH branches
remain explicit below: B1-NO is retained but RELOCATED — post-B1 it can live only at anchor scale
(Cl(9,5)/M(64,H) untested), at derivative level (the odd tau_plus homomorphism, B1 honest limit 1),
or over R (real/Krein form unselected, B1 honest limit 2). Nothing here decides the bit; SG4 (the
unbuilt source action's field-space declaration) remains the sole decider.
**Story-shopping guard (inverted):** the exciting outcome is corners-CLOSED (B-tilt hardens). The
corner-OPEN case (door open toward carrier A) is therefore carried at full strength in §5.

---

## 1. The question and the standing rows

If GU's graded IG is gauged with a local fermionic (odd) parameter in representation R, BRST gives
a spin-statistics-flipped ghost in R (commuting spinor), whose index/anomaly contribution enters
with a MINUS sign. What does that ghost subtract in the X4-restricted matter sector? Compare
against the adjudicated rows on K3 (all re-derived in the script from `sigma(K3) = -16` alone;
`p1 = 3*sigma = -48` by the signature theorem, `A-hat = -sigma/8 = 2`; no chi(K3), no A-hat = 3):

| row | K-twist | ind | per-Dirac | order-3 classes |
|---|---|---|---|---|
| carrier A (ghost-subtracted) | `T_C - 1C` | -42 = 21σ/8 | -21 | (0,0,0) |
| bare (control) | `T_C` | -40 | -20 | (0,1,2) |
| carrier B (geometric) | `T_C + 1C` | -38 = 19σ/8 | -19 | (0,2,1) |

The PTZ physics-register arithmetic (`-19 = -21 + 2`; `-21 = -20 - 1`; `-19 = -20 + 1`; PRD 106
(2022) 025022, cached `carrier-bit-swing/ptz-rsa.txt`, quoted verbatim in
`tests/carrier-bit-decision/leg1_applicability_matrix.md` Row 7) is reproduced exactly as the
per-Dirac ratios of these rows (script check 1.6). Order-3 classes throughout are computed by the
adjudication's exhaustively verified class law `rho_k == -(k/3)·ind mod Z`
(`canon/gamma-traceless-38-adjudication-RESULTS.md`, LEG-C; kernel-independent route) — law-grade
for the hypothetical rows, since no equivariant multiplier data exists for an unbuilt upstairs ghost.

## 2. What GU states (verbatim, `papers/drafts/Transcript into the impossible.md`)

- **The extension exists as a commitment** — [00:49:16]: "Then what you do is you take the
  inhomogeneous gauge group on that group and you extend it to through supersymmetry. Now that's a
  mouthful, but it's also the entire universe without making any choices."
- **The candidate odd parameter space** — [00:49:16] (same block): "It's zero forms and one forms
  valued either in add or in the spinners, and that's it."
- **The fermionic extension produces the families** — [00:46:02]: "We will never find space time
  Susie... Feed it the space of connections. Then the Lorentz group is the gauge group. The space
  of four momentum becomes the space of gauge potentials. And what you find is the fermionic
  extension gives you exactly three families of chiral fermions if you have a decreased VEV in the
  total space taking a Dirac equation into two vial equations because the mass is actually a
  variable."
- **The matter content** — [00:32:46]: "if you pull back ordinary spinners, zero forms valued in
  the positive spinners, direct sum one forms valued in the negative spinners on that top space,
  you're gonna get three generations of standard model fermions."
- **The third-generation mechanism** — [00:39:18]: "Rarita v tensor spinners on w, spinners on v,
  tensor Rarita Schwinger on w ... plus spinners on v, tensor spinners on w. So that's where you
  get your third generation of matter from."
- **The IG construction** — [00:18:03]: "you have a map, tau, which takes the ordinary gauge group,
  let's make it tau plus, into the inhomogeneous extension where g goes to tau plus of g equal to
  g... which is d aleph g, and then I premultiply by g inverse." (The tau+-twisted odd action
  `eps -> D_aleph eps` — the gravitino shape — is LEG-1's steelman S3.)
- **The chimeric signature** — [00:43:47 block]: "You trace reverse the Frobenius metric along the
  fibers, which gets you from a seven three signature to a six four." Script check 3.1:
  (3,1)+(6,4) = (9,5) and dim S(4)·dim S(10) = 4·32 = 128 = the repo Cl(9,5) rep dimension — the
  transcript's chimeric bundle is dimensionally the repo substrate. Check 3.2: the RS product rule
  dims close exactly (1664 = 384 + 1152 + 128), and the ADDED `S(V)⊗S(W)` slot (dim 128) is the
  imposter/third-generation slot — the ±1C slot the carrier fork is about.

## 3. BRANCH B1-YES — the shadow table (all exact; script Part 4)

Ghost = statistics-flipped field in R; subtraction is per-unit against the carrier package
(`T_C`-twist), the assignment grounded in LEG-2's 4-term complex living on the RS fiber.

| odd parameter R | ghost subtracts | net row | ind | classes | verdict vs the door |
|---|---|---|---|---|---|
| `Omega^0(S)` scalar-spinor (variation `eps -> D_aleph eps`) | `[1C]` | `T_C - 1C` | **-42** | (0,0,0) | **== CARRIER A EXACTLY → OPEN-toward-A** |
| Y14-spinor pulled back (`S(V)⊗S(W)`) | `[1C]⊗F`, F = S(W)_C | `(T_C - 1C)⊗F` | -42·rk F + 3·ch2 F | (0,0,0) for ALL F | same as above, per-unit; A-shape is F-independent |
| `Omega^1(S)` full RS-type (shift symmetry) | `[T_C]` | 0 | 0 | (0,0,0) | RESHAPED (new row) — whole carrier pure gauge; the DECOUPLING SHAPE (DEAD-ENDS-flagged, not adopted); deletes the stated third-gen mechanism [00:39:18] |
| `ker(Gamma)` RS-type | `[T_C + 1C]` | `-1C` | -2 | (0,2,1) | RESHAPED (new row; not A, not B, not bare) |
| full odd part `Omega^0(S) ⊕ Omega^1(S)` | `[1C + T_C]` | 0 on all matter | 0 | (0,0,0) | RESHAPED — kills the three SM generations [00:32:46]; dead as a GU reading |
| `S ⊗ ad`, ad nontrivial | `[ad_C]` (gaugino slot) | RS rows unchanged | — | — | CLOSED for the RS sector (misses); index-mimicry `2r + c = 2` exists but slot identity forces `ch(ad_C) = ch(1C)` → the u(1) case, which IS row 1 |
| even part `Omega^{0,1}(ad)` | bosonic slot | RS rows unchanged | — | — | CLOSED (misses; standard gauge ghosts) |

**Three structural findings (exact):**

1. **The A-shape is the UNIQUE clean landing.** Exactly one odd-parameter channel reproduces a
   standing row, and it reproduces carrier A on the nose: same K-twist, index, per-Dirac -21, and
   (0,0,0) classes (check Y1) — and it does so for EVERY internal multiplicity F, because
   `ind(D⊗(T_C-1C)⊗F) = -42·rk F + 3·ch2 F ≡ 0 mod 3` identically (check Y1''). If the door opens
   A-shaped, the order-3 arena dies regardless of the unbuilt internal bundle. (Honest
   counterweight, same check: carrier B's liveness IS multiplicity-dependent — `rk F ≡ 0` and
   `ch2 F ≡ 0 mod 3` would kill B's classes too.)
2. **Every other channel is RESHAPED-to-dead or misses.** Gauging the RS slot itself or the whole
   odd sector annihilates GU's own stated matter (rows with ind 0) — the decoupling shape the
   firewall forbids reading as a fix — and ad-valued or even parameters never touch the
   `T_C`-package rows (K-slot orthogonality, checks Y4/Y4'/Y5).
3. **Cross-leg note for corner (a) (check 2.4, flagged, not decided here):** the transcript's own
   chirality assignment [00:32:46] — 0-forms in S^+ ⊕ 1-forms in S^- — has total-matter K-class
   `(1 - T_C)([S+]-[S-])` = MINUS carrier A's twist: A-shaped arithmetic (|ind| = 42, classes
   (0,0,0)) with NO ghost anywhere, purely from the flipped relative chirality of the one-form
   slot. Uniform chirality instead gives carrier B's class exactly (= HS eq (11):
   "ind Q = Â(TM)(ch(TM_C) + 1)[M] = ind D_TM + ind D", cached `symbol-swing/hs_paper.txt` line
   316, verified this session). The word "flipped" in [00:40:27] ("one family of 16 flipped chiral
   spin three halves particles") may be doing exactly this work; handed to the corner-(a) legs.

## 4. Interaction with the mutual-exclusion certificate (script Part 5)

The LEG-2 certificate (`tests/carrier-bit-decision/leg2_obstruction_hardening.py`, TEST A):
off the null cone, ANY linear ghost map `h: Xi -> ker Gamma` with `sigma_Q . h = 0` vanishes —
any parameter space, any xi-dependence, no equivariance. Its assumptions: (i) target = ker Gamma;
(ii) h linear in the parameter; (iii) off-cone; (iv) h acts on the RS fiber variables.

**Which assumption would an upstairs evasion evade?** Exhaustive trichotomy on the linearized X4
shadow h of any upstairs odd invariance (check 5.1):

- **h = 0 on the RS fiber** (the "different variables" evasion — the gauging acts on
  connection-space variables `Omega^1(ad)`, evading assumption (iv)): certificate vacuously
  satisfied, but then NOTHING is subtracted in the RS rows. No A-door.
- **h ≠ 0 into ker Gamma:** DEAD off-cone by the certificate (sigma_Q is a bijection on
  ker Gamma). No evasion available.
- **im(h) ⊄ ker Gamma:** the declared field space must contain the orbit, so it exceeds
  ker Gamma. Full vector-spinor = carrier A DECLARED — this "evades" assumption (i) only by
  flipping the declaration, which IS the SG4 bit itself. (Intermediate spaces `ker Gamma ⊕ E`
  would be an unpublished RESHAPED row family; GU names no such E — BLOCKED.)
- **Nonlinear evasion** (assumption (ii)): collapses at shadow grade — the index subtraction
  counts zero modes of the LINEARIZED ghost operator, and the linearization-in-parameter of any
  local fermionic invariance is again a pointwise linear h; only an identically vanishing
  linearization escapes, and it subtracts nothing (check 5.2).
- **Characteristic-supported evasion** (assumption (iii); LEG-2 C3's real witness): EMPTY on
  Riemannian K3 — the fiber quadratic form is a sum of squares, `q(xi) = 0 ⟹ xi = 0` (check
  3.6). A named Lorentzian-only hole.

**The sharpest new link (check 3.4/3.5):** in the exact Cl(4,0) model, `c(xi)` is invertible for
all real `xi ≠ 0` (`det c = q²`, q positive definite), so `Gamma(xi ⊗ eps) = c(xi)eps ≠ 0`: the
gravitino-shaped odd orbit is NEVER tangent to ker Gamma. **Gauging a scalar-spinor odd parameter
does not merely make carrier A available — it FORCES the full vector-spinor field space** (a gauge
orbit must lie inside the declared field space). There is no route to an A-shaped subtraction that
keeps carrier B's constrained declaration (check 5.5).

## 4b. Conditioning on LEG-B1's ACTUAL outcome (script Parts 7-8, added after B1 landed)

**The candidate → row map (check 7.3): B1's four closed algebras land on exactly the four computed
rows — B1-YES introduces NO row beyond the Part-3 table.**

| B1 closed candidate (dim, recomputed check 7.2) | shadow row | verdict |
|---|---|---|
| (i) `Omega^0(S)` (4) | Y1: subtracts `[1C]` → `T_C − 1C`, ind −42, (0,0,0) | **== carrier A → the OPEN channel** |
| (ii) `Omega^1(S)` (16) | Y2a: subtracts `[T_C]` → net 0 | RESHAPED-dead (decoupling shape; deletes [00:39:18] mechanism) |
| (iii) `ad⊗S` (24) | Y4: gaugino slot; RS rows untouched | CLOSED (misses; u(1) sub-case → Y1) |
| (iv) full column (20) | Y3: subtracts `[1C + T_C]` → net 0 on all matter | RESHAPED-dead (kills the SM generations [00:32:46]) |

**Three post-B1 sharpenings:**

1. **The gravitino split is algebraically available (check 7.4).** B1's candidate (i) closes ON ITS
   OWN — `Omega^0(S)` alone is a closed odd subspace with `{O0,O0} ⊆ transl`. So gauging eps while
   keeping `Omega^1(S)` physical (the standard gravitino split — the only channel that opens toward
   A without deleting GU's stated matter) is a closed-SUBALGEBRA gauging, not an ad-hoc truncation.
   This removes the pre-B1 containment's "which GU nowhere states" from ALGEBRA (the split exists)
   and leaves it purely at ACTION grade (which sub-slot the action gauges is SG4).
2. **One-level BRST spectrum (checks 8.1-8.2).** Gauging B1's closed algebra gives three ghosts:
   `c_g` (integer-spin, adjoint), `c_t` (integer-spin, `Omega^1(ad)`), `c_odd` (commuting spinor in
   R). Only `c_odd` touches the fermion index rows (Y5 covers the rest), and there is NO spinor
   ghost-for-ghost: `{M,M} ⊆ Omega^1(ad)` feeds the EXISTING integer-spin translation ghost
   (`s c_t ~ {c_odd,c_odd}`). The Part-3 one-unit-per-parameter subtraction is the complete
   fermionic ghost bookkeeping at one level.
3. **Self-containment (check 8.3).** `{M,M}` lands in a slot IG already gauges — the odd gauging
   needs no new bosonic gauge field, unlike super-Poincare where `{Q,Q} = P` forces gravity. This
   is the transcript's own claim shape ("The space of four momentum becomes the space of gauge
   potentials" [00:46:02] L158, verified this session), which B1 proved FORCED (its R2: the
   g-valued anticommutator is dead) rather than chosen.

## 5. Door verdicts + the corner-OPEN case at full strength

**BRANCH B1-YES (now the EVIDENCED branch, toy grade, checks 1-96 machine-complete):** door
**OPEN-toward-A in exactly one channel** — the scalar-spinor odd parameter (equivalently its Y14
pullback, equivalently the u(1) case of `S⊗ad`), whose variation is the tau+-shape
`eps -> D_aleph eps` GU itself supplies [00:18:03], and which post-B1 is available as a
closed-subalgebra (gravitino-split) gauging. All other channels: RESHAPED (ind-0 rows that delete
GU's own stated matter — dead as GU readings) or CLOSED (miss the RS sector).
**BRANCH B1-NO (retained explicitly; post-B1 it can live only at anchor scale, derivative level, or
real form):** door **CLOSED** — no ghost, no subtraction, rows stand, and the B-tilt's "no GU
license for ghost subtraction" hardens; but the honest pressure of a hard NO is toward the FOURTH
outcome (GU-as-stated inconsistent), because GU commits to the extension verbatim [00:49:16] — not
automatically toward B.

**THE CORNER-OPEN CASE (strongest honest form — and its first premise is now toy-evidenced).**
LEG-B1 HAS landed YES (toy grade, machine-complete core) on brackets whose odd part contains a
scalar-spinor summand — candidates (i) and (iv) both close. Therefore: (1) the transcript's group
reading of [00:49:16] ("you take the inhomogeneous gauge group... and you extend it to through
supersymmetry" — an extension OF THE GROUP, whose odd directions are then local gauge directions
demanding ghosts) gives ghost subtraction exactly the GU-native license the decision campaign found
missing — with no spacetime SUSY, honoring [00:46:02], and B1's R4 makes the parameter LOCAL at
zero cost (the bracket is pointwise; localizing eps does not force gravity, unlike super-Poincare);
(2) the shadow is not approximately A but EXACTLY A — same K-twist, same -42 = 21σ/8, same -21 per
Dirac, same (0,0,0) classes, for every internal multiplicity F; (3) the gauging auto-declares
carrier A's field space (the odd orbit is never inside ker Gamma), so SG4 would resolve A as a
consequence rather than a further choice; (4) the referee-corrected honest count already carries
L158 [00:46:02] as transcript-tier support for this A-door, the variation shape is GU's own tau+
construction, and post-B1 the gravitino split (gauge eps, keep psi physical) is a closed-subalgebra
choice, not a truncation GU would have to invent. On this branch-and-channel the B-tilt would flip:
order-3 arena (0,0,0), generation count 2-primary, for any F.
**What contains it (also honest):** (a) the same group reading, applied to the WHOLE stated odd
field content, subtracts GU's three SM generations to zero (row Y3) — the A-door needs the action
to gauge the scalar-spinor SUB-slot while keeping `Omega^1(S)` physical; B1 shows this split EXISTS
as algebra, but GU nowhere STATES it, and [00:46:02] equally reads as the odd fields being physical
MATTER ("gives you exactly three families of chiral fermions"), i.e. the fermionic extension as a
field-content statement, not a gauged-invariance statement; (b) the open channel still rides B1's
three named gaps — anchor scale, the derivative-level odd tau_plus homomorphism (the gravitino
shape `eps -> D_aleph eps` is verified only as its frozen algebraic shadow `[a, eps]`), and the
real/Krein form; (c) B1's extended/locality checks are prefix-evidenced (crashed run), not
exit-0-final. Which reading the action takes is SG4.

## 6. BLOCKED items (named, honest)

1. LEG-B1's FINAL exit-0 run — at this leg's run time B1's minimal-ansatz core (checks 1-96) is
   machine-complete in `run2.log`, but its extended-ansatz / gravitino-shadow / locality parts are
   prefix-evidenced only (`run1.log` passed through check [102] then crashed, StopIteration; run2
   still grinding PART 6). Both branches carried explicitly; the YES branch conditioning is pinned
   to the verbatim strings asserted in script checks 7.1a-7.1d.
2. Equivariant (order-3) multiplier data for any actual upstairs ghost and for internal bundles F
   — classes for hypothetical rows are class-law-grade only; Z/24-arena values for the new rows
   not computed (no published law used beyond mod-3).
3. The intermediate field spaces `ker Gamma ⊕ E` (RESHAPED row family) — no GU statement names
   any E; not computed beyond naming.
4. Which sub-slot of the odd sector GU's action would gauge vs keep physical — SG4 itself.
5. `ch2(ad_C)[K3]` and `ch2(S(W)_C)[K3]` for GU's actual internal bundles — unbuilt; all internal
   dependence carried symbolically as (rk F, ch2 F).

## 7. Sources

- `papers/drafts/Transcript into the impossible.md` — [00:18:03], [00:32:46], [00:39:18],
  [00:40:27], [00:43:47], [00:46:02], [00:49:16], all read this session, quoted verbatim above.
- `canon/gamma-traceless-38-adjudication-RESULTS.md` — rows, class law, multipliers (c_A = -3,
  c_B = -1), kernel data; read this session.
- `canon/carrier-bit-decision-campaign-RESULTS.md` — B-tilt state, referee corrections (incl.
  super-Higgs -40 reachability), read this session.
- `tests/carrier-bit-decision/leg2_obstruction_hardening.py` — the mutual-exclusion certificate
  (TEST A/B/C), read this session; `leg1_applicability_matrix.md` (GP/GPvN hypotheses, steelman
  S3), `leg3_ungauged_consistency.md` (VZ fork), read this session.
- Homma-Semmelmann arXiv:1804.10602, cached `symbol-swing/hs_paper.txt` — eq (11) line 316 and
  Rem 3.6 ("discarding zero modes that can be gauged away...") re-verified verbatim this session.
- PTZ PRD 106 (2022) 025022, cached `carrier-bit-swing/ptz-rsa.txt` (via leg1's verbatim quotes).
- `absorbed/gu-source-action/DEAD-ENDS.md` — firewall + acausal trap, read this session.
- `canon/source-action-seiberg-witten-RESULTS.md` — vectorlike carrier, Krein (+96,-96); read
  this session.
- LEG-B1 artifacts (this swing, shared directory): `LEG-B1-graded-IG-algebra.md` (results +
  honest limits), `run1.log` (checks through [102] then StopIteration), `run2.log` ("PARTS 1-5
  complete: 96 checks"; closure statement verbatim) — machine-read by script PART 7 this session.
