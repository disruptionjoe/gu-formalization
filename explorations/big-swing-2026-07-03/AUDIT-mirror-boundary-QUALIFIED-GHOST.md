---
artifact_type: exploration
status: exploration
created: 2026-07-04
title: "Mirror-Boundary Hypothesis audit: is the -96 of GU's (+96,-96,0) cross-chirality Krein firewall a physical parity-flipped mirror Standard Model (dark sector) realized as the non-orientable Klein-bottle monodromy of Y14 = Met(X4)? HONEST OUTCOME: PARTIAL, leaning GHOST. The mirror-SM reading FAILS on the repo's own K-null counter-evidence — the chirality -96 = W_- is totally K-null (carries no inner product of its own; ‖K|W_-‖ = 1.75e-14, signature (0,0,96)), and the only positive-definite '-96' is the trivial universal -K sign-flip on a DIFFERENT (45°), VECTORLIKE subspace the repo removes as ghosts. The Klein mechanism is CONTRADICTED: w1(Y14)=0 is a FORCED unconditional theorem, the RP^3-fiber monodromy is verified trivial, and the swap C=J_quat·G is a pure internal-fiber endomorphism with tangent-frame charge exactly 0. Wall-consistency HOLDS but is permissive-only. NO target imported."
grade: "exploration / strong. The crux computation is proof-grade finite-dim linear algebra, reproduced independently here on the repo's own gu_triplet_KGamma builder in both physical signatures. Every load-bearing canon citation was grep-verified (w1(Y14)=0 unconditional; RP^3 monodromy trivial by explicit bundle isomorphism; swap tangent-frame charge 0.00e+00; synthesis line 136 verbatim). Honest limitation: the whole module sits on the SOFT (9,5) signature (could be (7,7) — reproduced identically), and 'not ABSOLUTELY null' means the qualified-ghost verdict is decidable only by unbuilt ghost-parity dynamics [P_ghost,S]=0; but no positive-norm parity-mirror SM is exhibited under any reading. Verdict does NOT derive the generation count and imports no target (no 3/8/24/chi(K3)/Ahat)."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - canon/w2-y14-spin-structure.md
  - canon/boundary-eta-of-mu-RESULTS.md
  - canon/antilinear-bound-RESULTS.md
scripts:
  - tests/generation-sector/ghost_parity_krein.py
  - tests/generation-sector/net_chiral_index_invariant.py
---

# Mirror-Boundary Hypothesis: is the -96 a physical mirror-SM, or the ghost the Krein form excludes?

**The swing.** GU's self-dual generation triplet (the j=1 Rarita-Schwinger module of Cl(9,5), 192-dim)
carries a cross-chirality Krein form `K = eta_V ⊗ beta_S` of signature **(+96, -96, 0)**. The
Mirror-Boundary Hypothesis proposes three things at once: (1) the **-96 is not a mathematical ghost** but a
**parity-flipped mirror Standard Model** with its OWN positive-norm Hilbert space, living "outside the
boundary" as a physical dark sector; (2) the mechanism is a **NON-ORIENTABLE (Klein-bottle) closure** of the
space-of-metrics `Y14 = Met(X4)`, whose orientation-reversal monodromy **IS** the `C = J_quat·G`
particle-hole / `S+ <-> S-` chirality swap the repo already flagged as its only count-escape; and (3) the
picture is wall-consistent. Success (`MIRROR_BOUNDARY_COHERENT`) requires **all three**.

**Honest outcome: PARTIAL, leaning GHOST.** Two of the three legs FAIL on the repo's own evidence, and the
third HOLDS only permissively. This does not become the strong dark-sector prediction the hypothesis hoped
for. It also does not collapse to an *absolute* ghost — the module is a bona fide Krein space and the
physical/ghost split is basis-dependent — so the landing is a **qualified ghost**: a consistently-removable
negative-Krein-norm cross-partner, **never** an exhibited positive-norm parity-mirror SM.

---

## The crux (do not fudge it): is the -96 definite or null?

The hypothesis lives or dies on ONE question: restrict GU's Krein form to the -96 carrier and ask whether it
is **definite** (a physical mirror-SM Hilbert space) or **null** (a ghost). The decisive move is refusing to
conflate two *different* "-96"s:

- **(A) the CHIRALITY -96 = W_-** — the eigenspace of the chirality grading `Gamma` with eigenvalue -1. This
  is the *actual object the hypothesis names*: the parity-flipped mirror family.
- **(B) the KREIN-NEGATIVE -96** — the negative-eigenvalue eigenspace of `K` itself (the negative-norm half).

**Computation** (reusing `tests/generation-sector/net_chiral_index_invariant.py::gu_triplet_KGamma`, both
physical signatures):

```
=== (9,5) ===
cross-chirality residual ||GK+KG|| = 4.97e-14
(A) chirality W_- (mirror candidate): ||K|W_-|| = 1.75e-14   signature (+0,-0,0:96)
    ||K|W_+|| = 1.76e-14    cross-pairing ||K(W_+,W_-)|| = 9.80
(B) Krein-negative -96 via -K: min eig = 1.0000, max eig = 1.0000
    mean chirality of Krein-negative half = +0.0000
(A vs B) principal angles cos: min=0.7071 max=0.7071
=== (7,7) === (identical structure: ||K|W_-||=1.82e-14, -K eig=1.0000, mean chir=-0.0000, cos=0.7071)
```

Reading the numbers honestly:

1. **`K` is purely cross-chirality** (`‖ΓK+KΓ‖ ≈ 5e-14`): all the form's content is in the `W_+ ↔ W_-`
   pairing (`‖K(W_+,W_-)‖ = 9.80`), nothing in the diagonal blocks.
2. **The chirality -96 = W_- is TOTALLY K-NULL.** `‖K|W_-‖ = 1.75e-14`, signature `(0,0,96)`. The
   parity-flipped mirror candidate carries **no inner product of its own**. Because GU's internal group is
   **non-compact `so(p,q)`**, `K` is *the* invariant form (Weyl unitarian trick fails); there is no invariant
   positive-definite metric to put on a null Lagrangian. A Hilbert structure on `W_-` would have to be
   **imported** — data GU does not supply. **So reading (b), a mirror-SM with its own positive-norm space, is
   NOT exhibited.**
3. **The only positive-definite "-96" is the trivial `-K` sign-flip on (B),** with `-K` restricted to the
   Krein-negative eigenspace equal to the identity (`eig = 1.0000`). But this is the *universal* ghost
   sign-flip available to **every** Krein space, not an exhibited second Hilbert space. And (B) is a
   **DIFFERENT subspace** from (A): principal angles are all `cos = 0.7071` (**exactly 45°**), and (B) is
   **VECTORLIKE** (mean chirality `0.0000`, a 50/50 `W_+/W_-` graph), **not** a single-chirality mirror.

**Conclusion of the crux:** no sector is simultaneously **positive-definite AND single-chirality**. The
object that could be a parity-flipped mirror (W_-) carries nothing of its own; the object with a positive
form (the `-K` half) is the generic sign-flipped ghost — vectorlike, 45° away, and the repo's own synthesis
files it as *"three mirrors are negative-norm ghosts, not physical mirror fermions"*
(`ghost-parity-krein-synthesis.md`, line 136). The strong mirror reading is **wishful relabeling of a
ghost**. It is *not* absolutely null either: the physical/ghost assignment within each hyperbolic pair is
basis-dependent, fixed only by an **unbuilt** ghost-parity-preserving dynamics `[P_ghost,S]=0` — which even
if built yields physical+ghost per pair, never a positive-norm mirror-SM. Hence **QUALIFIED GHOST**.

---

## The Klein mechanism is contradicted (orientability is FORCED, not declared)

The hypothesis needs a non-orientable closure of `Y14` whose orientation-reversal monodromy IS the swap.
Three independent facts kill this:

- **`w1(Y14) = 0` is an unconditional THEOREM, forced.** `canon/w2-y14-spin-structure.md` derives it from the
  Whitney sum: `w1(Y14) = w1(TV) + π*w1(X4) = 2·π*w1(X4) = 0 (mod 2)` (line 138). The `det=-1` GL(4,ℝ)
  component acts orientation-reversingly on the RP^3 fiber, but it enters as `w1(TV) = π*w1(X4)` and
  **cancels** in the sum. "Y14 is always orientable — unconditional" (line 23); it "survives the W2-01
  retraction" that killed only the weaker w2/**spin** claim (line 149: *"unconditional (correct, unaffected by
  W2-01)"*). Crucially, `w1(Y14)=0` is **more forced** than the `(9,5)` signature, which is itself
  convention-soft (could be `(7,7)`). So the escape-hatch symmetry between the two inputs is false: the
  orientability input is the robust one, and it points *against* the hypothesis.
- **The RP^3-fiber monodromy is verified trivial.** `π₁(GL(4,ℝ)) → ℤ/2` acting on `H*(RP^3; ℤ/2)` is trivial
  by explicit tautological-line-bundle isomorphism (line 70: *"the bundle map … is a well-defined bundle
  isomorphism γ¹ → g*(γ¹) … the monodromy on α is trivial"*). There is no orientation-reversal cycle for a
  Klein closure to **be**.
- **The swap is an internal-fiber endomorphism, so it cannot be a base monodromy regardless.**
  `boundary-eta-of-mu-RESULTS.md` (line 32) shows `C = J_quat·G` has **tangent-frame charge exactly
  `0.00e+00`** (`max‖[J_quat, any tangent-frame so(9,5) rotation]‖ = 0`): it lives entirely in the internal
  `M(64,ℍ)` factor and is **identity on the base tangent frame**. It fixes the spacetime frame; it is not a
  spacetime orientation reversal. Identifying it with a Y14 base-orientation monodromy is a **category error
  the repo already ruled out** ("different bundles, orthogonal by construction", line 45).

A Klein-bottle `Y14` appears **nowhere** in the repo (grep is empty) and is structurally blocked.

---

## Wall-consistency: holds, but permissive only

C-07 forces GU-native net chirality **even/zero** (`J_quat` forces even signature; the metric-connection
generation index is identically 0). A chiral SM `(+96)` plus a parity-flipped mirror `(-96)` is
**VECTORLIKE**, net chirality **exactly 0** — machine-confirmed: `K` is purely cross-chirality
(`‖ΓK+KΓ‖ ≈ 5e-14`), so every maximal K-positive physical subspace is the graph of a chirality-exchanging
isometry with net chiral index `chi = 96 - 96 = 0`. This is **fully consistent** with the wall; a mirror
picture giving net-NONZERO chirality would violate it and be wrong — this one does not.

**But the consistency is permissive, not confirmatory.** Net-0 is *equally* the signature of "no chiral
selection at all." The Euclidean `(14,0)` control is grading-aligned and gives `|chi| = 96`, proving `chi`
genuinely detects chirality — so C-07 *permits* the mirror reading without *supporting* it. An **observable**
chiral `+96` still needs the separate, **unbuilt** chiral-selection ingredient (ghost parity / external
topological index or flux).

---

## Firewall reinterpretation: it fails

The hypothesis wanted to recast the `(+96,-96,0)` **firewall** as a physical dark/mirror **prediction**. That
recasting does **not** survive the repo's own K-null counter-evidence: the chirality -96 carries no inner
product of its own, and the only positive-definite -96 is the trivial ghost sign-flip on a different,
vectorlike subspace the repo removes. **The firewall stays a firewall** — a consistently-removable
negative-Krein-norm cross-partner — not a physical dark sector. The generation **count** is untouched: the
swap is the count-*killer* (PHS forces `eta(D_Sigma)=0`, generation index 0), not a count-generator, and it
is frame-trivial, so it cannot revive the count either. The count remains **OPEN** — external, located but not
forced. Nothing here derives it, and no target (`3`, `8`, `24`, `chi(K3)`, `Ahat`) was imported.

## Cosmology note (honest)

Even granting a mirror, GU as reconstructed supplies the **constrained (BBN-disfavored) symmetric** case, not
the viable colder one. The `(+96,-96)` structure is maximally symmetric — generation↔mirror is an exact
cross-pairing isometry (50/50, defect ~1e-14). GU supplies **no** dynamics, mass spectrum, or
temperature/entropy asymmetry (the source action is unbuilt); BBN and `ΔN_eff` are nowhere discussed. On its
face this is the **BBN-excluded** symmetric mirror (~doubled light dof, large `ΔN_eff`), with no `T'/T < 1`
mechanism. The only escape is self-defeating: a genuinely ghost-removed -96 is never thermally populated
(evading `ΔN_eff`) — but then it is **not dark matter at all**. Separately, GU's *own* stated dark content
(Weinstein transcript) is a **spin-3/2** chirality-flipped conjugate-of-the-internal-rep family plus a
high-energy-reunifying "imposter" generation — a **different object** from the hypothesis's spin-1/2 Lee-Yang
mirror SM; the two must not be conflated.

---

## What this settles, and what it does not

**Settles.** The strong "boundary is a physical mirror-SM" claim does **not** survive. Leg (1) fails (W_- is
K-null; a genuine mirror needs imported metric data GU does not supply). Leg (2) is contradicted (w1(Y14)=0
forced, monodromy trivial, swap is a frame-trivial internal endomorphism). Leg (3) holds but only permissively.
Verdict: **PARTIAL, leaning GHOST** — a qualified ghost.

**Does NOT settle.** The -96 is not proven *absolutely* null: the module is a legitimate Krein space
(Turok-Bateman-type) with a consistent positive-norm physical sector, and the physical/ghost assignment
within each hyperbolic pair is fixed only by an unbuilt `[P_ghost,S]=0` dynamics. But no reading of that
dynamics yields a positive-norm parity-mirror SM.

**Concrete next steps.**
1. **Exhibit-or-refute the second metric** on W_- (none exists for non-compact `so(p,q)`); if a mirror is
   wanted the extra positive metric must be *imported* and documented as such, not relabeled onto the null half.
2. **Build the ghost-parity dynamics** `[P_ghost,S]=0` and check whether it can ever select a single-chirality
   positive-norm sector (the computation says it yields physical+ghost per pair — vectorlike — never a chiral
   mirror-SM).
3. **State the swap↔monodromy category gap as a lemma:** `C=J_quat·G` (tangent-frame charge 0) is orthogonal
   to any `Y14` base-orientation class, so no Klein closure can realize it.
4. **Pursue chiral selection separately** (external topological index / flux) to turn net-0 vectorlike into an
   observable chiral `+96` — the genuinely unbuilt piece, independent of the mirror question.
5. **If a mirror is ever exhibited, model the cosmology** (a `T'/T<1`/asymmetric mechanism); absent that,
   record the symmetric-doubling case as BBN-excluded.
6. **External-check flag:** the crux and the orientability-forcing both rest on the soft `(9,5)` signature;
   re-run if it is pinned or revised (already reproduced identically in `(7,7)`).

**Not promoted.** Exploration-grade. Does not edit canon/CANON.md/RESEARCH-STATUS.md/NEXT-STEPS.md/papers and
is not committed. The generation-count verdict remains **OPEN**.
---

## Verifier's note (main-loop review, 2026-07-04)

Synthesis of an 18-agent audit (`wf_70038338-bd7`; 1 agent errored on schema retries, and — flagged honestly —
audit-angle-5's subagent ran `taskkill /F /FI "IMAGENAME eq python.exe"`, which kills ALL python on the machine,
not just its own process (security-policy warning). The load-bearing computations were reproduced on the repo's
own `gu_triplet_KGamma` builder, so the conclusion does not depend on that agent.)

Main-loop honesty review — the exciting mirror/Klein/CPT hypothesis **does not survive**, on three independent grounds:
- **The `-96` is a qualified GHOST, not a physical mirror.** The chirality `W_- = -96` is totally `K`-null
  (`‖K|W_-‖ ~ 1.8e-14`, signature `(0,0,96)`) — it carries NO inner product of its own. Non-compact `so(p,q)`
  has no invariant positive-definite form (Weyl unitarian trick), so a positive-norm mirror Hilbert space would
  have to be IMPORTED. The only positive-definite `-96` (via `-K`) is the universal Krein ghost sign-flip — a
  different subspace (45°) and vectorlike, not single-chirality. No sector is both positive-definite AND
  single-chirality. Reading (b) is not exhibited.
- **Orientability is FORCED, against the hypothesis (independently verified in canon).** `w1(Y14)=0` is an
  unconditional theorem (`canon/w2-y14-spin-structure.md` line 23/138; the `RP^3`-fiber orientation-reversal
  `w1(TV)=π*w1(X4)` cancels), surviving W2-01. So **no Klein/non-orientable closure of `Y14` is admissible** —
  there is no orientation-reversal cycle for the swap to be. Orientability is strictly MORE forced than the
  signature; the hoped-for symmetry between the two inputs is false.
- **Category error:** the swap `C = J_quat·G` is an internal-fiber `M(64,H)` endomorphism with tangent-frame
  charge exactly 0 — orthogonal to any base-orientation class — so it cannot be a `Y14` base monodromy. The
  repo already ruled this out ("different bundles, orthogonal by construction"). And it is the count-KILLER
  (forces index 0), not a generator.

**What survives (the honest residue):** the `(+96,-96)` firewall stays a firewall — a consistently-removable
negative-Krein cross-partner — NOT a physical dark sector. Wall-consistency HOLDS but is permissive (net-0 is
equally "no chiral selection"). Cosmologically GU supplies only the BBN-disfavored symmetric mirror, and GU's
own dark content (spin-3/2 conjugate + "imposter") is a DIFFERENT object from a Lee-Yang spin-1/2 mirror SM.

**Bottom line (main-loop concurrence):** the mirror-boundary / Klein / CPT synthesis is REFUTED on the repo's
own evidence — an honest, valuable negative. It converges with the cross-repo panel's independent B- "mitten,
not glove" verdict. Count untouched, OPEN; no target imported.
