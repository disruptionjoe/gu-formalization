---
title: "Three-seam swing, PRONG B — the no-fourth-generation 'theorem', hostile-verified: B-FAILS. GU does NOT force exactly three same-signature generations and does NOT forbid a fourth. The two council arguments are TWO different (CRT-disjoint) constructions, not one theorem, and each rests on a category error (order-3 class vs integer-3; dim(Λ²₊)=3=dim su(2) as a cardinal). The actual computed multiplicities on the substrate — j=1 mult 64, Spin(10)-16 branch 2/4, quaternionic EVEN-index wall — make a fourth same-signature generation CONSTRUCTIBLE."
status: active_research
doc_type: exploration
created: 2026-07-21
prereg: explorations/prereg-three-seam-swing-2026-07-21.md
outcome: B-FAILS
inputs:
  - explorations/prereg-three-seam-swing-2026-07-21.md
  - explorations/council-committed-constructions-math-2026-07-21.md
  - canon/three-generations-locate-not-force-CRT-RESULTS.md
  - canon/source-action-seiberg-witten-construction.md
  - explorations/decision-tree-Q3-one-anchor-vs-two-2026-07-21.md
  - tests/generation-sector/h1_selfdual_family_kill.py
  - tests/generation-sector/ghost_parity_krein.py
  - tests/generation-sector/leg4_branching_multiplicity_search.py
  - tests/generation-sector/step11_gu_native_parity_theorem.py
probe: tests/channel-swings/prongB_no_fourth_generation_probe.py (foreground, numpy-only, two-run-identical, EXIT 0; kill conditions declared before computation)
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_actions: none
kill_conditions_declared_before_computation: true
---

# Prong B — the no-fourth-generation theorem, hostile-verified

**Verdict: B-FAILS.** The strongest experimental-contact prediction — "GU forbids a fourth
generation with identical Krein signature `(+32,-32,0)`" — does **not** hold as a theorem. When
the two council arguments are made precise and checked against GU's own committed computations,
neither forces exactly three same-signature generations and neither forbids a fourth. A fourth
same-signature generation is **constructible** in the framework (three independent constructions
below). The pre-registered kill condition is met, honestly.

This is a real finding, not a failure to find one: **GU would then NOT forbid a fourth generation.**
The prediction that contacts experiment most directly is the one that fails on hostile verify.

Adversarial posture per the prereg: a "theorem" here contacts experiment, so I hostile-verified my
own reasoning and did not overclaim the grade. Because a kill is a strong claim, I also steelmanned
"no fourth" as hard as I could before landing the kill (§6, the B-CONDITIONAL shell).

---

## 0. The two arguments, stated precisely

**(i) TOPOLOGICAL (Member 2, algebraic topologist).** The generation label is the odd-torsion
summand `Z/3 ⊂ π₃ˢ = Z/24 = Z/8 ⊕ Z/3` (the third stable stem). "A fourth generation would require
a `Z/4` the stable stem does not contain."

**(ii) REPRESENTATION-THEORETIC (Member 3, Clifford geometer).** The three generations are the
weights `m = -1, 0, +1` of the `j=1` `su(2)₊` triplet inside `ker Γ` of `Cl(9,5) = M(64,ℍ)`, all
carrying identical Krein signature `(+32,-32,0)`. "There is no `j=3/2` quadruplet in the
decomposition, so there is no fourth generation."

The decisive question the prereg poses: **does GU FORCE the generation-carrying representation to be
exactly three-dimensional (⇒ no fourth), or does it merely HOST three with room for more?** A
rigorous no-fourth needs the former. The answer, computed on the substrate, is the latter — and
worse, the committed structure actively points at counts other than three.

---

## 1. Are they ONE theorem or TWO? — TWO, and CRT-disjoint

They are **two independent constructions living in the two arithmetically disjoint arenas** the repo's
own canon already separated (`canon/three-generations-locate-not-force-CRT-RESULTS.md`):

| | argument (i) topological | argument (ii) rep-theoretic |
|---|---|---|
| carrier | `Z/3 ⊂ π₃ˢ = Z/24` (stable homotopy) | `j=1` triplet of `su(2)₊ = Λ²₊` on `ker Γ ⊂ Cl(9,5)` |
| the "3" is a… | **ORDER** of a torsion class (mod-3) | **DIMENSION** `dim Λ²₊ = dim su(2) = 3` (a cardinal) |
| CRT arena | odd-torsion **3-primary** `Z/3`, tangent-frame/homotopy side | **2-primary / internal-fiber** side (`M(64,ℍ)` factor) |
| what it forbids | an order-4 *label* in the `Z/3` summand | a `j=3/2` (dim-4) *irrep* |

The CRT canon proves these two sides are **decoupled** — obstructions and selectors live in the
2-primary `Z/8` arena, a homotopy count could only live in the disjoint `Z/3` arena, and "anomaly
inflow is the sole bridge" (unbuilt). They are not the same theorem; they cannot even interact
directly. **Fusing them into "one rigorous theorem" requires equating an order-3 torsion class with
a 3-dimensional irrep** — precisely the pun `canon/three-generations-locate-not-force-CRT-RESULTS.md`
already quarantined: *"dim(Λ²₊) = 3 = dim su(2) is a CARDINAL coincidence DISTINCT from the order-3
e-invariant it carries."* The requested fusion is the quarantined category error wearing a theorem's
clothes.

---

## 2. The multiplicity count (the decisive probe)

Probe: `tests/channel-swings/prongB_no_fourth_generation_probe.py` (foreground, numpy-only,
two-run-identical, **EXIT 0**). It reproduces, self-contained, the committed repo results
(`h1_selfdual_family_kill.py`, `ghost_parity_krein.py`, `leg4_branching_multiplicity_search.py`,
`step11_gu_native_parity_theorem.py`) and counts the admissible same-signature generation
multiplicity.

**Part A — `su(2)₊` decomposition of `ker Γ` in `Cl(9,5)` (computed, asserted):**

```
dim ker(Γ) = 1664
su(2)₊ STATE content : { j=0: 640,  j=1/2: 832,  j=1: 192 }
su(2)₊ IRREP MULT    : { j=0: ×640, j=1/2: ×416, j=1: ×64 }      (640·1 + 416·2 + 64·3 = 1664)
j=3/2 multiplicity   : 0
full j=1 sector Krein signature : (+96, -96, 0)
per-WEIGHT (m) Krein signature  : m=-1:(+32,-32,0)  m=0:(+32,-32,0)  m=+1:(+32,-32,0)
```

The decisive number: **`j=1` appears with multiplicity 64, not 1.** The "three generations = the three
weights of ONE triplet" is a choice of three `su(2)₊`-weight labels inside a **64-fold-degenerate**
sector. The three per-weight blocks each carry the identical `(+32,-32,0)` signature — confirming the
canon "identical Krein signature" claim — but that identity is exactly the *sameness* condition a
same-signature fourth generation must meet, and 64 identical triplet copies meet it.

"No `j=3/2`" is **TRUE** (the decomposition tops out at `j=1`) but **irrelevant** to the no-fourth
question: a fourth *family* is not a four-dimensional `su(2)₊` irrep, it is a **second copy of the
same `j=1` object**, of which 63 spares exist. The "no `j=3/2` ⇒ no fourth generation" inference is a
non-sequitur (it answers "is there a spin-3/2 generation?", not "is there a second spin-1
generation?"). The `m=±2` weight is absent because `Λ²₊` of a 4-manifold is 3-dimensional — a fixed
geometric fact, identical for **every** 4-manifold regardless of physics, not a bound on fermion
families.

**Part B — branching multiplicity of the ACTUAL generation object (`Spin(10)` 16):**

```
half-spinor 64  → Spin(10)×Spin(4):  16 multiplicity = 2   (a Spin(4) DOUBLET)
Dirac spinor 128 → Spin(10)×Spin(4): 16 multiplicity = 4   (a FOURTH identical-16 copy is PRESENT)
```

The family multiplicity GU actually *branches* is a **power of two** (2 in the matter half-spinor, 4
in the full Dirac 128) — never a forced-and-capped 3. In the Dirac spinor the Spin(10) 16 literally
appears **four** times, identical. And GU's own cleanest verified result, the Pati–Salam `Spin(7,7)`
chain, isolates **one** anomaly-free generation. The committed computations point at `{1, 2, 4}`;
none of them is a hard cap at three, and one of them (`4`) *is* a fourth same-signature copy.

**Part C — the quaternionic Kramers wall (`step11` reproduced):** every GU-native Hermitian carrier
lies in `M(64,ℍ)` (quaternionic-linear, Kramers `J² = -1`), hence has **EVEN** signature/index. An
odd count such as 3 requires importing a non-quaternionic object; even counts are native. So the
quaternionic structure **forbids the odd count 3 and makes a fourth (even) generation MORE natural
than a third** — the opposite of "GU forbids a fourth."

---

## 3. The B-FAILS construction (the fourth, exhibited)

Three independent constructions of a fourth same-signature generation, from committed structure only:

1. **A second `j=1` triplet.** `ker Γ` contains `j=1` with multiplicity **64**; every copy carries the
   identical `(+32,-32,0)` per-weight signature and identical `Spin(10)` Casimir. Select any second of
   the 64 — a same-signature "generation" object with 62 further spares. Nothing in the committed
   structure (the Casimir, the `Γ`-trace projection, the Krein form) singles out one, three, or any
   specific number of these as "the generations."
2. **The fourth 16 in the Dirac spinor.** The `Spin(10)` 16 branches with multiplicity **4** in the
   128 (Part B). The fourth copy is present, identical to the first three.
3. **Even-index preference.** The quaternionic wall (Part C) *forbids* the odd count 3 and makes even
   counts (2, 4, …) the native ones — so a fourth is admitted where a third is not.

Any one of these refutes "GU forbids a fourth same-signature generation." Together they make the kill
robust.

---

## 4. Controls (pre-declared) — both PASS, and both EXPOSE the arguments

**Control (a): "the same argument forbids the observed THIRD generation" must be REJECTED; a genuine
theorem must forbid the 4th while permitting EXACTLY 3.**
Reading "generation = an `su(2)₊` irrep indexed by dimension," the dimensions present in `ker Γ` are
`{1, 2, 3}` (`j = 0, 1/2, 1`). So:
- `forbids_third = FALSE` → the planted "forbids the third" is **REJECTED** (the third is permitted). ✓
- `permits_exactly_three = FALSE` → the argument **also** permits 1 and 2, so it does **not force
  exactly three**. The only readings under which it cleanly "permits 3, forbids 4" are the pun/
  category-error readings (generation = self-dual weight), which mis-define the fourth.

**Control (b): "a fifth is forbidden but a fourth is allowed" — does the argument forbid exactly-3, or
some other count?**
`su(2)₊` irrep dim 4 (`j=3/2`) is absent; dim 5 (`j=2`) is absent — **both, equally**. The asymmetric
"fourth allowed, fifth forbidden" is `FALSE` → **REJECTED**. The argument's real content is "no
`su(2)₊` irrep of dim ≥ 4," which forbids `4, 5, 6, …` all at once and permits `{1, 2, 3}`. That is
**not** an "exactly three" statement.

Both controls fire correctly and, in doing so, demonstrate the arguments are count-blind (topological)
or copy-permissive (rep-theoretic) rather than "exactly-three" forcing.

**Topological control (Part D):** `Z/24 = Z/8 ⊕ Z/3` **does** contain a `Z/4` — the elements `{6, 18}`
have order 4. So "Z/24 has no Z/4 to host a fourth" is **false about the group `Z/24`**. What is true:
the `Z/3` summand `{0, 8, 16}` has element orders `{1, 3}` only. Per the prereg's own warning,
absence of an order-4 element in `Z/3` forbids an order-4 **label**, not a fourth **copy** — and the
order-3 class is homotopy-fixed (identical for a universe with 1 or 5 generations, per CRT canon), so
it is **count-blind**: it neither forces exactly three nor forbids a fourth.

---

## 5. Why the identical `(+32,-32,0)` signature makes it worse, not better

The prediction's own phrasing — "a fourth generation *with identical Krein signature*" — is where it
self-defeats. The probe confirms all three weight-blocks (and, by the 64-fold triplet multiplicity,
all 64 triplet copies) carry the **identical** `(+32,-32,0)` signature. Identical signature is exactly
the condition a same-signature fourth generation must satisfy — so the Krein structure, far from
forbidding a fourth, **guarantees ≥ 63 candidate same-signature copies**. The signature is a *sameness*
invariant across the sector, not a *selector* that picks out a unique triplet. (This is consistent
with, and independent of, the `Q3-TWO-INDEPENDENT` result: `σ` = the Krein *orientation* bit is a
separate external datum from the generation structure; it does not count generations either.)

---

## 6. The honest B-CONDITIONAL shell (steelman, then why it does not rescue the theorem)

The strongest surviving true statement is: **"the self-dual 2-form `Λ²₊` on a 4-manifold has exactly
three components (no fourth), with identical Krein signature across them."** This is rep-exact and
correct. It becomes a no-fourth-generation statement **only** under the extra posit

> **(P)** *physical generations ≡ the three self-dual components (`m = -1, 0, +1` weights) of `Λ²₊`.*

Under **(P)**, no fourth follows trivially (`Λ²₊` is 3-dimensional). That is the **B-CONDITIONAL**:
the prediction holds *only* under assumption **(P)**. But **(P)** is:
- **not GU-derived** — it is the identification `canon/three-generations-locate-not-force-CRT-RESULTS.md`
  explicitly quarantines as a cardinal pun (`dim Λ²₊ = 3` is not a family count);
- **contradicted by GU's own branching** — the family index branches as a `Spin(4)` **doublet**
  (multiplicity 2), not the self-dual triplet; the self-dual "3" is the Lorentz/gauge index carried by
  *each* generation, not a family label;
- **contradicted by GU's verified physics** — the Pati–Salam chain gives **one** generation, and the
  quaternionic wall makes the native counts **even**.

So the conditional is not merely unproven; its named assumption **tilts against**. A theorem resting on
a canon-rejected, physics-contradicted identification is not a theorem.

---

## 7. Verdict and grade

- **Outcome: B-FAILS.** GU does **not** force exactly three same-signature generations and does **not**
  forbid a fourth. A fourth same-signature generation is constructible (§3).
- **Does GU force exactly three?** No. The committed computations give `{1 (Pati–Salam), 2 (branch),
  4 (Dirac 128), 64 (triplet multiplicity)}`, and the quaternionic wall forbids odd 3 outright. "Three"
  appears only as the cardinal `dim Λ²₊ = dim su(2) = 3` (a self-dual-2-form fact) or as an order-3
  torsion class (homotopy-fixed, count-blind) — never as a forced, capped family count.
- **Does GU forbid a fourth?** No. "No `j=3/2`" forbids only a spin-3/2 (dim-4 irrep) generation, which
  is not what a fourth family is; "no `Z/4`" is false of `Z/24` and, restricted to the `Z/3` summand,
  forbids only an order-4 label. Neither touches a *second identical copy*, which exists with
  multiplicity 2–64.
- **Grade of the kill: operator/fixture grade (robust).** The load-bearing facts —
  `dim ker Γ = 1664`; `j=1` multiplicity `64`; no `j=3/2`; per-weight signature `(+32,-32,0)`;
  `Spin(10)`-16 branch multiplicity `2/4`; `Z/24 ⊃ Z/4`; quaternionic even-index — are all computed and
  asserted in the probe (two-run-identical, EXIT 0) and match four independent exit-tested repo tests.
- **Grade of the surviving positive: B-CONDITIONAL, on an against-tilting assumption.** "No fourth"
  survives only under the canon-quarantined posit **(P)** "generation ≡ self-dual 2-form component,"
  which GU's own branching and Pati–Salam results contradict.
- **The two arguments are two theorems, not one** (§1), CRT-disjoint and of different *kind* (an order
  vs a dimension); the requested fusion is the quarantined category error.

Consistent with the CRT canon's standing verdict ("GU **locates**, does not **force**; tilts toward
one"), Prong B finds the sharpest experimental-contact prediction of the swing to be **false as a
theorem**: GU does not predict "no fourth generation." The truthful deliverable is the kill plus its
exact mechanism.

---

## Boundary

Exploration tier. Only this artifact and its probe
(`tests/channel-swings/prongB_no_fourth_generation_probe.py`, foreground, numpy-only,
two-run-identical, **EXIT 0**, kill conditions declared before computation) were written. GU otherwise
read-only. No commit, no push. No edit to any canon, LANE-STATE, research-portfolio, NEXT-STEPS,
prereg, decision tree, ledger, claim/verdict file, or any other agent's artifact. No claim-status,
canon-verdict, paper-status, or public-posture change. Ran synchronously in one pass (no Monitor, no
background children, python foreground). The `Q3-TWO-INDEPENDENT` result and the CRT two-arena canon
are honored, not moved.
