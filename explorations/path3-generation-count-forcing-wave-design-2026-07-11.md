# Path 3: the generation-count forcing theorem -- scope + blind-branch wave design

**Status:** SETUP (deploying). Blockbuster path 3 from the strategy map. GU-INDEPENDENT by design -- "why three
generations?" is a famous open problem; the value must not require accepting GU. Serves the count leg of the GU
program (H6/H29/H37-H40) but is written so a skeptic who rejects GU still has a reason to read it.

## 1. The problem, stated GU-independently

Why are there exactly **three** generations of fermions? No accepted first-principles derivation exists. The
"located, not forced" line of work (this repo's count arc, and the boundary/cobordism literature) has established
a sharp partial picture:
- The count lives in the **3-primary (odd-primary) arena**: the relevant homotopy is `Z/3 subset pi_3^s = Z/24`,
  and `3 = dim Lambda^2_+(R^4)` (the self-dual 2-forms on the 4-base).
- A **Z-valued index** (Atiyah-Singer / Dirac) provably CANNOT force it: `Hom(Z/3, Z) = 0`. This is the H6
  theorem's core -- a selector forcing a 3-primary count must have nonzero 3-Sylow image, so no integer index or
  2-group selector reaches it. "Odd" (mod-2) is the WRONG framing; the rigorous statement is **mod-3**.
- The count is a **boundary / anomaly-inflow** quantity (Nielsen-Ninomiya; Callan-Harvey; Kaplan), localized in
  the odd-primary summand.
- Prior art locates (not forces) the count in the 3-primary summand via cobordism: Garcia-Etxebarria-Montero
  (arXiv:1808.00009), Wan-Wang-Yau.

**The honest target (NOT "prove 3" naively).** The count arc has repeatedly found the count *located-not-forced*
at `{1,3}` (ceiling `dim Lambda^2_+ = 3`, realized rank in `{1,3}`). So the target of this wave is:
1. find the **strongest forcing statement that IS provable** from stated first principles (the count must be
   odd / 3-primary / boundary-quantized / bounded by 3), and
2. characterize **exactly what extra input pins it to 3** (a bordism-class choice, a representation choice, a
   physical admissibility condition), or
3. prove that **no first-principles selector can pin it** -- making "located, not forced" a THEOREM (the number
   of generations is irreducible data given those principles), which is itself a real, publishable result.
Any of the three is a genuine, GU-independent contribution to a famous problem.

### The decidable sub-questions (report a graded verdict on each)
- **Q-force:** does the construction FORCE a specific count (3), or only CONSTRAIN it (odd / 3-primary / <=3)?
- **Q-extra:** if it only constrains, what is the MINIMAL extra input that pins 3, and is that input a
  first-principles consistency condition or a free choice?
- **Q-nogo:** can one prove no first-principles selector of this kind forces 3 (the located-not-forced theorem),
  and is that no-go construction-specific or class-wide?

## 2. Why the blind-branch method fits

The construction-fork discipline (this repo's standing rule) is already VALIDATED on exactly this problem: the H6
result is the statement that a Z-index construction provably cannot reach a Z/3 torsion-class construction --
i.e. the answer's reachability depends on which construction of "the count" you use. So the branches ARE rival
constructions of what the count IS (an index vs a boundary anomaly vs a cobordism class vs a homotopy torsion
class), and a no-go in one construction does NOT transfer to another. Running them blind prevents defaulting to
the index picture (where the count famously cannot be forced) and missing that a torsion/cobordism construction
might reach it. This is the fork discipline operationalized as a wave.

## 3. The five branches (each a rival construction of "what forces the count"; each blind)

**Branch A -- Atiyah-Singer index / Dirac.** The classic route: net chirality = a Dirac index. Establish
precisely what the index route FORCES (net-chirality-zero-without-a-boundary; the anomaly-free content) and
precisely WHERE it dies for the count (`Hom(Z/3,Z)=0`), and test whether any TWISTED / EQUIVARIANT / family index
evades the death (an index valued in a torsion group, e.g. a mod-k index or a KO-theoretic index). Verdict target:
Q-force (expected: index CONSTRAINS, does not FORCE 3) + a sharp statement of what it does force.

**Branch B -- Anomaly inflow / boundary localization (Callan-Harvey / Kaplan / Nielsen-Ninomiya).** The count as
a boundary-localized quantity via anomaly inflow from a higher-dimensional bulk. Test whether the inflow
structure forces the count to be odd / 3-primary / equal to a specific boundary invariant, and whether the
"no net chirality without a boundary" result sharpens to a forcing. Verdict target: Q-force via the boundary
invariant; Q-extra (what bulk/boundary data pins 3).

**Branch C -- K-theory / cobordism (Garcia-Etxebarria-Montero / Wan-Wang-Yau).** The count as a cobordism
invariant / K-theory class. Compute (or characterize) the relevant bordism group's 3-primary summand and test
whether its structure FORCES 3 or only LOCATES it. Identify the exact extra input (a choice of bordism class /
generator) needed to pin 3, and whether that choice is a consistency condition or free. Verdict target: Q-force
+ Q-extra via the bordism group structure.

**Branch D -- 3-primary homotopy torsion (`pi_3^s = Z/24`, the `Z/3` summand).** The count as a torsion class in
the 3-primary part of stable homotopy, with `3 = dim Lambda^2_+`. Test whether the homotopy structure forces the
realized rank to 3, or only bounds it (ceiling 3, realized in `{1,3}`), and what selects `{1,3} -> 3`. This is
the construction where the count is REACHABLE (nonzero 3-Sylow), so it is the most likely to force -- test it
hardest. Verdict target: Q-force (does the `Z/3` action on `Lambda^2_+` as `SO(3)` force rank 3?) + Q-extra.

**Branch E -- Adversarial no-go (make "located, not forced" a theorem).** Do NOT try to force 3; try to PROVE it
CANNOT be forced from first principles. Show that any first-principles selector leaves a residual freedom (the
`{1,3}` degeneracy, a bordism-class choice, a representation choice) that no symmetry or consistency condition
removes. A successful no-go is a real theorem: the number of generations is irreducible data given the stated
principles. State whether the no-go is construction-specific (some construction escapes it) or class-wide.
Verdict target: Q-nogo.

Blindness matters: A famously cannot force (index), D is where forcing is reachable (torsion), and E wants
everything to fail. If D forces 3 and survives E, that is the blockbuster. If E shows the `{1,3}` residual is
irreducible across A-D, that is the located-not-forced theorem.

## 4. Team composition (each branch = one worker running a bespoke 5-persona team INLINE)

Per the standing rule (personas always inline, never fanned per-agent): each branch is ONE agent running five
personas sequentially in one context. Five agents total (A-E), parallel, mutually blind.

The 5-persona template (specialize persona 1 per branch's formalism; 2-5 constant):
1. **The formalism specialist** -- the index theorist (A); the anomaly-inflow theorist (B); the
   cobordism/K-theory computer (C); the stable-homotopy/torsion theorist (D); the no-go/rigidity theorist (E).
2. **The math referee** -- demands rigor; grades each claim (theorem / argument / conjecture); flags where a
   result LOCATES vs FORCES, and where a torsion vs integer distinction is being blurred.
3. **The adversary** -- attacks the branch's own emerging forcing claim ("here is the extra choice you smuggled
   in that a skeptic would not grant").
4. **The cross-checker** -- independent second derivation / known-case check (reproduce a literature result:
   Garcia-Etxebarria-Montero's 3-primary location for C; the `Hom(Z/3,Z)=0` obstruction for A; von
   Staudt-Clausen / Adams for D).
5. **The synthesizer** -- states the branch verdict on {Q-force, Q-extra, Q-nogo}, a confidence grade, the single
   load-bearing assumption, WHICH construction of "the count" it used, and the one thing that would overturn it.

Each team must: (a) state its construction of "the count" and "forcing" (fork discipline); (b) grade honestly
(theorem / located-only / conjecture); (c) name the minimal extra input its construction needs to pin 3.

## 5. Wave protocol
1. Deploy A-E parallel, blind. Each returns a graded verdict on {Q-force, Q-extra, Q-nogo} + its construction +
   its minimal-extra-input + a durable artifact (exploration + deterministic test where a computation was done).
2. Orchestrator synthesis (inline, science-council lens): which constructions force vs locate, what each forces,
   and the cross-test -- does E's residual-freedom obstruction kill any A-D forcing? does D's torsion route
   evade it?
3. Cross-share decision + wave-2 design (deeper on the forcing construction, or a focused kill on the contested
   residual).
4. Re-rank + capture any method move.

## 6. Honest pre-registration (fixed BEFORE the wave)
- **A-D find a genuine forcing to 3 surviving E:** the generation number derived from first principles -- a
  blockbuster, GU-independent.
- **E proves a class-wide no-go:** "the count is provably NOT forced from these first principles" -- located-not-
  forced becomes a theorem; the number of generations is irreducible data. Real and publishable; and it says
  exactly what new physics WOULD be needed to force it.
- **Split / strongest-provable-is-weaker-than-3 (most likely):** a MAP -- the count is forced to be
  odd/3-primary/boundary-quantized/`<=3`, with the realized value in `{1,3}` requiring a named extra input.
  Honestly weaker than "3" but a genuine sharpening of a famous problem; sets the wave-2 target.
- **All inconclusive:** report the specific technical wall; do not dress it as progress.

DEPLOYMENT: this wave is being deployed now (Joe's Go).
