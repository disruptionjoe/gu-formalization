---
title: "Why Distler-Garibaldi does not apply to GU: a scope-exit / category-error defense"
subtitle: "Standalone referee-defense note (hardening pass A2b)"
date: 2026-07-03
status: draft
doc_type: referee_defense_note
draft_only: true
verdict: "EVASION BY SCOPE EXIT — DG inapplicable to GU (category error to invoke it), NOT contradicted or circumvented within its domain."
depends_on:
  - canon/no-go-class-relative-map.md            # sec 2.4 precision carve-out
  - explorations/cycle-gates-and-audits/distler-garibaldi-precision-carveout-2026-06-23.md
  - explorations/cycle-gates-and-audits/distler-garibaldi-functor-audit-2026-06-23.md
  - canon/six-axis-candidate-krein-positivity-dg.md
  - canon/swing-ghost-parity-no-chiral-selection.md
cert:
  - papers/drafts/hardening-pass-2026-07-03/certs/dg_scope_exit_structural_cert.py  # PASS, exit 0
---

# Why Distler-Garibaldi does not apply to GU

**A standalone, referee-checkable scope-exit defense**

> **What this note claims, and what it does NOT claim.**
> Distler-Garibaldi (DG) is a **correct theorem**. This note does **not** claim GU
> "defeats," "refutes," or "circumvents" it. The claim is strictly one of
> **inapplicability**: GU's Clifford / Sp(64) reconstruction is **not an object of the
> category DG's theorem quantifies over**, so invoking DG against GU is a **category
> error**. Where GU's construction does produce a DG-shaped object (its 4D
> representation-theoretic "shadow"), it **reproduces** DG's null/vectorlike answer
> rather than contradicting it. The disagreement is over **domain of applicability**,
> not over the truth of DG.

> **Firewall (read before the generation count is mentioned anywhere).**
> The scope-exit verdict below is **independent of the value of `ind_H(D_GU)`** — the
> GU generation-count invariant, which is **OPEN** (a separate, unfinished index
> computation; see §7). Nothing in the DG defense derives, requires, or divides by
> "3 generations," "24," "8," "16," or "32." Those numbers are quarantined to §7 and
> are load-bearing **nowhere** in the argument. If any step below silently needed the
> count, that would be a contamination and is flagged as such (it does not occur).

---

## 0. Citation correction (recorded up front)

The correct identifier for the DG paper is:

> J. Distler and S. Garibaldi, *"There is no 'Theory of Everything' inside E8,"*
> Communications in Mathematical Physics **298** (2010) 419-436,
> **arXiv:0905.2658** [math.RT].

**Discrepancy flagged:** the source note
`explorations/cycle-gates-and-audits/distler-garibaldi-precision-carveout-2026-06-23.md`
(§1, line 23) cites the paper as **arXiv:0905.2483**, which is **wrong**. The canon map
(`canon/no-go-class-relative-map.md`) and the six-axis file
(`canon/six-axis-candidate-krein-positivity-dg.md`) use the correct **0905.2658**. This
note uses **0905.2658** throughout and records the drift for correction in a later
editing pass (not made here — this is a draft-only note; no canon edits).

---

## 1. The Distler-Garibaldi theorem, stated precisely as a 7-assumption package

DG proves: there is no real Lie group `E` together with subgroups `SL(2,C)` (Lorentz)
and `G` (internal) such that a "Theory of Everything" embedding exists inside `E8`.
Concretely, DG show there is no way to embed `SL(2,C) x G` into (complex or any real
form of) `E8` such that the resulting fermion content is chiral. We package the
theorem's hypotheses into the object it quantifies over. Call an object satisfying all
seven a **DG-object**, and the category of DG-objects **`DG_E8`**.

| # | Assumption | Precise statement (a DG-object must satisfy all of these) |
|---|---|---|
| **DG-A1** | Single finite-dim simple group | `E` is complex `E8` or a real form of `E8` (dim 248, rank 8). The whole symmetry lives in **one** such `E8`. |
| **DG-A2** | Lorentz embeds **inside** `E` | There is an injective homomorphism `i_L: SL(2,C) -> E`; spacetime Lorentz symmetry sits **inside the gauge group**. |
| **DG-A3** | Internal group compact, centralizes Lorentz | `G` is connected, **compact**, and `[G, i_L(SL(2,C))] = 0` in `E`. |
| **DG-A4** | All matter from `Lie(E)` branching | Matter = the subspaces `V_{m,n}` in the `SL(2,C) x G` decomposition of the adjoint `Lie(E)`. |
| **DG-A5** | Low-spin condition | `V_{m,n} = 0` for `m + n > 4` (no higher-spin junk in the adjoint). |
| **DG-A6** | Chirality = **reality type** of `V_{2,1}` | Chirality is detected by whether `V_{2,1}` is **complex** as a `G`-representation (vs. real/quaternionic ⇒ vectorlike). |
| **DG-A7** | Finite-dim rep theory only | No bundle data, no compactification, no flux, no infinite-dimensional / operator-analytic extension. |

**DG conclusion.** No object of `DG_E8` is chiral: for every DG-object, the candidate
`V_{2,1}` matter rep comes out **real (vectorlike)**, so no chiral Standard-Model
generation structure survives. Equivalently: **the full subcategory of `DG_E8`
satisfying the "ToE" chirality condition is empty.** This is what killed, e.g., Lisi's
`E8` model (its `SU(5)` fermion assignment is exactly a DG-object that fails the
chirality test).

The scope of the theorem is **exactly `DG_E8`**. A theorem's hypotheses *are* its domain;
DG says nothing about objects outside `DG_E8`.

---

## 2. GU's relevant structural data (what a referee needs to check membership)

The following are established GU structural facts (see canon; independent of the
generation count):

- **Gauge group:** `Sp(64) = U(64,H)` — the compact symplectic group of `64 x 64`
  quaternionic-unitary matrices — arising from `Cl(9,5) ≅ M(64,H)` acting on the
  spinor module `S = H^{64}`. Structural constants: `dim_R Sp(64) = 8256`, rank `64`
  (certificate §6).
- **Base geometry:** `Y^{14} = Met(X^4)`, the **non-compact** bundle of Lorentzian
  metrics over spacetime `X^4`, with non-compact fibers `GL(4,R)/O(3,1)`.
- **Lorentz action:** `SL(2,C) ≅ Spin(3,1)` acts on `X^4` via the **tangent-bundle /
  structure-group** data of `Y^{14}` — i.e. it acts on the **base**, external to the
  gauge group.
- **Chirality carrier:** the **operator index** `ind_H(D_GU) ∈ KSp^0` of the
  H-linear Dirac-DeRham operator `D_GU` on the Clifford-module bundle over `Y^{14}`.
  (Its *value* is OPEN — §7. The scope-exit argument uses only the fact that **this
  invariant, not a reality type, is the chirality carrier**.)

---

## 3. Which DG assumptions GU violates, and why a referee can check each

GU is **not** a DG-object. It fails **four** of the seven defining assumptions
(DG-A1, A2, A6, A7), plus a fifth (DG-A3) on the separate Krein sub-route (§5). Any
one failure already places GU outside `DG_E8`; four independent failures make the
category-membership question unambiguous.

### 3.1 DG-A1 fails — the gauge group is Sp(64), not a real form of E8

**Claim.** No Lie-type embedding `Sp(64) -> (real form of) E8` exists, so GU's symmetry
group cannot be the `E` of a DG-object.

**Referee-checkable reasons (two independent obstructions; either suffices):**

1. **Dimension.** `dim_R Sp(64) = 64·(2·64+1) = 8256`. A subalgebra of `e8` has real
   dimension `≤ dim e8 = 248`. Since `8256 > 248`, `sp(64)` is not isomorphic to any
   subalgebra of any real form of `e8`. Hence no injective Lie homomorphism
   `Sp(64) -> E8` of the same Lie type.
2. **Rank.** `rank Sp(64) = 64`. The real rank of **any** real form of `E8` is at most
   the rank of complex `E8`, which is `8` (the split form `E8(8)` attains 8; the
   compact form has real rank 0). A maximal (split) torus of a subgroup injects into a
   maximal (split) torus of the ambient group, so a subgroup's rank is `≤` the ambient
   rank. Since `64 > 8`, no such subgroup embedding exists.

Both obstructions are verified by the **executable certificate**
`certs/dg_scope_exit_structural_cert.py` (PASS, exit 0; §6). **Proof-grade.** These are
elementary invariant-theoretic facts about fixed groups; they import no physical target.

*(Aside, not needed for the argument: even setting Lie-type aside, there is no
interesting continuous homomorphism `Sp(64) -> E8` at all, since a compact simple group
admits no nontrivial homomorphism into a group too small to contain its image; but the
dim/rank obstructions above are the clean, fully checkable statements.)*

### 3.2 DG-A2 fails — Lorentz does not embed inside the gauge group

**Claim.** GU has no `i_L: SL(2,C) -> Sp(64)` playing DG's role; Lorentz acts on the
**base**, not inside the gauge group.

**Referee-checkable reason.** In GU, `SL(2,C) ≅ Spin(3,1)` is the structure group of the
tangent bundle of `X^4`; it acts on `Y^{14} = Met(X^4)` through the base geometry (the
fibers `GL(4,R)/O(3,1)` are literally the coset of frames modulo Lorentz). The gauge
group `Sp(64)` acts on the **spinor-module fiber** `S = H^{64}`. These are actions on
**different spaces** (base vs. fiber). DG-A2 requires spacetime Lorentz to sit as a
subgroup *inside* the single gauge Lie group `E`; GU's Lorentz is a **spacetime /
tangent-frame** symmetry that is structurally external to `Sp(64)`. There is therefore
no candidate `i_L` at all — not "an `i_L` that fails to centralize `G`," but **no
Lorentz-inside-gauge embedding in the construction to begin with**.

**Grade: structural / reconstruction-grade.** The statement "Lorentz acts on the base,
gauge acts on the fiber" is a clean architectural fact of the `Y^{14} = Met(X^4)` setup;
it does not depend on any unfinished computation. It is not "proof-grade" only in the
sense that it is a description of the construction's architecture rather than a theorem
with a machine-checkable certificate.

### 3.3 DG-A6 fails — chirality is an operator index, not a reality type

**Claim.** GU's chirality carrier is the **quaternionic operator index** `ind_H(D_GU)`,
a `KSp^0` / Atiyah-Singer-type invariant of the Dirac-DeRham operator on `Y^{14}` — not
the reality type ("complex vs. real as a `G`-rep") of any `V_{2,1}` branch inside a Lie
algebra.

**Referee-checkable reason.** DG-A6 is a statement about representation theory: take
the adjoint `Lie(E)`, branch under `SL(2,C) x G`, look at the piece `V_{2,1}`, and ask
whether it is complex as a `G`-rep. GU has **no `Lie(E)` to branch** (DG-A1 already
fails) and locates chirality in a **different mathematical object**: the index of a
differential operator on a bundle. `ind_H(D_GU)` is defined by kernel/cokernel of a
Fredholm operator (analysis + topology of `X^4` / `Y^{14}`), not by the decomposition
of a fixed finite-dimensional Lie algebra. The two "chirality tests" live in different
categories — representation reality type vs. elliptic-operator index — and there is no
map from one to the other (see §4).

> **Firewall check (the sharp target-import trap for this item).** DG-A6's failure is a
> statement about **which kind of invariant** carries chirality (an operator index vs. a
> reality type). It does **not** assert, and does **not** need, any particular *value* of
> `ind_H(D_GU)`. The sentence "GU's chirality is an operator index" is true whether that
> index is 0, 24, 32, or undetermined. **No `ind_H(D_GU) = 24` claim is used here.** A
> referee should reject any version of this argument that reads "GU evades DG because it
> gives 3 generations" — that would be a target import and is *not* what is claimed. (See
> §7 for the honest status of the value, and §8 for why the verdict survives it being
> open.)

**Grade: structural.** That the carrier is an index and not a reality type is a
definitional feature of GU's chirality mechanism. The *computation* of that index is
open; the *identity of the invariant* is what DG-A6 is about, and it plainly differs.

### 3.4 DG-A7 fails — GU is geometric bundle data on a non-compact space

**Claim.** GU is explicitly bundle / geometric data on the **non-compact** `Y^{14}`,
which DG-A7 forbids.

**Referee-checkable reason.** DG-A7 restricts DG-objects to **finite-dimensional
representation theory of one Lie group** — no bundles, no compactification, no flux, no
operator-analytic extension. GU's core data are: a **non-compact fiber bundle**
`Y^{14} = Met(X^4)`; a canonical bundle metric (the "gimmel" metric) on it; a
**Clifford-module bundle** `S = H^{64}`; and an elliptic-type operator `D_GU` on
sections of that bundle. Every one of these is exactly the kind of object DG-A7 excludes.
The generation invariant lives in the analysis/topology of these bundles, not in a
finite-dimensional adjoint.

**Grade: structural.** This is a direct read-off of the construction's data type.

### 3.5 Summary of §3

| DG assumption | GU status | Why (referee handle) | Grade |
|---|---|---|---|
| DG-A1 (one E8) | **VIOLATED** | `Sp(64)`: dim 8256, rank 64 vs. E8 dim 248, rank 8 — no embedding (cert, PASS) | proof-grade (cert) |
| DG-A2 (Lorentz inside E) | **VIOLATED** | Lorentz acts on base `X^4` / fibers `GL(4,R)/O(3,1)`; gauge acts on fiber `S`. No `i_L` exists | structural |
| DG-A3 (G compact) | violated on Krein sub-route only | Krein/ghost route needs non-compact `SO(5,5)` (Weyl trick) — see §5 | structural |
| DG-A4/A5 (adjoint branching, low spin) | **moot** | no `Lie(E)` to branch once A1 fails | n/a |
| DG-A6 (chirality = reality type) | **VIOLATED** | carrier is `ind_H(D_GU)` (operator index), not reality type of `V_{2,1}` | structural |
| DG-A7 (no bundles/flux) | **VIOLATED** | GU is bundle data on non-compact `Y^{14}` | structural |

Four independent violations (A1, A2, A6, A7); each alone removes GU from `DG_E8`.

---

## 4. Why there is no "hidden DG-object" inside GU (the functor test)

A referee's natural challenge: *"Maybe GU secretly contains a DG-object as a shadow, and
DG applies to that shadow."* The correct response is: to apply DG to GU one must exhibit
a **functor** `F_DG: GU_data -> DG_E8` that (a) accepts GU objects, (b) lands in `DG_E8`
(preserving the Lorentz-embedding and compact-centralizer structure), and (c) **preserves
the chirality invariant** GU uses. The dedicated functor audit
(`explorations/cycle-gates-and-audits/distler-garibaldi-functor-audit-2026-06-23.md`)
tested the natural candidate collapse maps and found **none** works:

- The defensible collapse maps land in **coarse branch data**, **4D EFT data**, or a
  **spectral/Clifford shadow** — **not** in `DG_E8`.
- None preserves the generation/chirality invariant: `ind_H(D_GU)` depends on global
  analytic data (Fredholmness, zero-mode spectrum, `X^4` topology) that is **absent** from
  any single-`E8` adjoint branch table. So `ind_H(D_GU)` does **not factor through** any
  DG-shadow.

Consequently DG cannot be applied to GU "by analogy" either. The **only** way to reopen a
DG obligation is precisely to **construct** such an `F_DG` landing in `DG_E8` and
preserving the chirality invariant. Absent that, there is **no residual DG obligation**.

**Reproduction, not contradiction.** Where GU *does* admit a crude representation-theoretic
shadow (impose a positive-definite metric, forget the operator/bundle data), that shadow
returns DG's **null/vectorlike** answer — consistent with the theorem. GU does not claim
the shadow is chiral; it claims the shadow is **the wrong object** to read GU's chirality
off of. This is exactly the DG mirror obstruction reproduced, not evaded.

---

## 5. The separate DG-A3 sub-route (Krein / ghost-parity) is *also* a scope exit

A distinct line of attack (the Krein / indefinite-metric / ghost-parity route,
`canon/six-axis-candidate-krein-positivity-dg.md`) once framed itself as an *inside-class*
enrichment of DG — a shadow living **inside** the single-`E8` class. That framing was
**RETRACTED** by the A0 audit (2026-06-28) and must be cited as retracted:

> **Weyl unitarian trick.** A finite-dimensional representation of a **compact** group
> always admits an invariant positive-definite form. So the indefinite **Krein** form the
> route relies on exists **only** if the internal group is taken **non-compact** —
> `SO(5,5)`, not compact `SO(10)`. Dropping Hilbert positivity is therefore logically the
> **same move** as negating **DG-A3** (compact internal `G`). The route cannot both "keep
> `G` compact" and "use an indefinite form"; those are the same step read twice.

Hence the Krein route is **not** an inside-class enrichment; it is **another scope exit**,
joining DG-A1/A2/A6/A7 via **DG-A3**. Two honesty riders (from the source files, preserved
here so a referee is not misled):

1. The Krein kinematics **reproduces** DG's answer on the shadow: net chiral asymmetry is
   exactly `0` on the 192-dim self-dual triplet in every signature; the triplet is
   genuinely **vectorlike**. DG's reality-type conclusion is **untouched and agreed**.
2. Whether GU's (unbuilt) dynamics realizes the ghost parity as a symmetry, and whether
   any chiral selection actually fires, is **OPEN**; index conservation makes the **null**
   outcome the *favored* one. So this route yields **no** chiral claim — do **not** resurrect
   it as a live "first inside-class shadow."

**Grade: structural (retraction is definitive).** DG-A3's status as a scope exit rests on
the Weyl trick, which is elementary and checkable.

---

## 6. Executable certificate (structural facts only, no target import)

Script: `papers/drafts/hardening-pass-2026-07-03/certs/dg_scope_exit_structural_cert.py`

**What it verifies** (all fixed-group structural constants; **no** generation target):

- `dim_R Sp(64) = 8256` (closed form `n(2n+1)` **and** independently `rank + #roots`,
  cross-checked), `rank Sp(64) = 64`.
- `dim E8 = 248` (cross-checked `rank + #roots = 8 + 240`), `rank E8 = 8`.
- **Obstruction I (dim):** `8256 > 248` ⇒ `sp(64)` is not a subalgebra of `e8`.
- **Obstruction II (rank):** `64 > 8` ⇒ `Sp(64)` is not a subgroup (rank bound).
- Therefore **no Lie-type embedding `Sp(64) -> (real form of) E8`** ⇒ **DG-A1
  unsatisfiable for GU.**

**Run result (verbatim):**

```
$ python papers/drafts/hardening-pass-2026-07-03/certs/dg_scope_exit_structural_cert.py
Sp(64)=U(64,H)  dim_R (closed form n(2n+1)) = 8256
Sp(64)=U(64,H)  dim_R (rank + #roots)       = 8256
Sp(64)=U(64,H)  rank                        = 64
E8              dim                          = 248
E8              dim (rank + #roots)          = 248
E8              rank                         = 8
Obstruction I  (dim):  dim Sp(64)=8256 > dim E8=248  -> True
Obstruction II (rank): rank Sp(64)=64 > rank E8=8  -> True
VERDICT: No Lie-type embedding Sp(64) -> (real form of) E8 exists.
         DG-A1 (gauge group is a real form of E8) is UNSATISFIABLE for GU.
RESULT: PASS
EXIT=0
```

**Independent re-derivation** is built in: `dim Sp(64)` is computed by the closed form
`n(2n+1)` and independently by `rank + #roots` (type `C_64`, `2·64^2` roots); `dim E8`
likewise against its 240-root count. Both agree. **No number in the certificate is a
generation count.** (For DG-A2 there is deliberately no certificate: "Lorentz acts on the
base" is architectural, not arithmetic — flagged as reconstruction-grade above.)

---

## 7. The generation count is OPEN — and firewalled from everything above

**Status of `ind_H(D_GU)` (the GU chirality invariant's *value*):** **OPEN.** Per canon
(`CANON.md` lists the three-generation count under *Not Yet Canon*;
`canon/no-go-class-relative-map.md` §2.4), the value is an **unfinished index
computation** with two live candidates and multiple firing failure conditions:

- **Candidate A:** `rank_H(S_RS^+) = 4 ⇒ ind_H(D_RS) = 8 ⇒ ind_H(D_GU) = 24`.
- **Candidate B:** `rank_H(S_RS^+) = 8 ⇒ ind_H(D_RS) = 16 ⇒ ind_H(D_GU) = 32`.
- Blocking gates **OQ-RK1** (first-principles RS gamma-trace-projector rank) and
  **OQ-RK2** (APS boundary conditions on a K3-type factor) are **OPEN**; the RS leg
  currently has **no** surviving analytic index derivation (kinematic support only).
- The spin-1/2 leg's "16" is a **compact-K3-model** expectation, conditional on an
  **unestablished** non-compact→compact reduction; standard Atiyah-Singer does **not**
  apply on the non-compact `Y^{14}`.

**This entire section is quarantined.** The numbers `24, 32, 16, 8`, and "3 vs. 4
generations" appear **only here**, describe an **open** problem, and are **not used** in
§§1-6. This is the deliberate structure of the defense: GU exits `DG_E8` via
DG-A1/A2/A6/A7 (and A3 on the Krein route) **regardless of what `ind_H(D_GU)` evaluates
to**.

---

## 8. Contamination self-audit (does the scope-exit secretly need the count?)

The honest-negative outcome to guard against: *does DG-A6's failure secretly require
asserting `ind_H(D_GU) = 24`?* If so, the scope exit would depend on the OPEN count and
would **not** stand independently. Audit:

- **DG-A1** failure: pure group dimension/rank arithmetic — count-free (certificate).
- **DG-A2** failure: base-vs-fiber architecture — count-free.
- **DG-A6** failure: the claim is *"the chirality carrier is an operator index, not a
  reality type."* This is a statement about the **type of invariant**, provable from the
  *definition* of `D_GU` (a Fredholm operator whose index lives in `KSp^0`), with **no
  reference to the index's value**. A referee can confirm: replacing "24" by "an unknown
  integer `ind_H(D_GU)`" everywhere in §3.3 changes **nothing** in the argument.
- **DG-A7** failure: data-type (bundle on non-compact base) — count-free.
- **DG-A3** (Krein): Weyl-trick / non-compact-form — count-free; and it *reproduces* the
  null answer.

**Result of the self-audit: NO contamination.** Each violated assumption is argued from
group structure, construction architecture, or invariant *type* — never from the value of
the generation count. The firewall holds. (Had it failed, this section would report the
contamination as an honest-negative result rather than paper over it; it does not fail.)

---

## 9. Rebuttal to the referee's "you're just moving the goalposts" objection

**Objection.** *"This is evasion by relabeling. You changed the subject from `E8` to
`Sp(64)`, redefined chirality as an index, and declared yourself out of scope. Any failed
theory could dodge any no-go this way."*

**Rebuttal.** A theorem's **own hypotheses define its domain**; staying outside that domain
is not evasion, it is how theorem scope works.

1. **DG correctly kills the things that *do* claim to be in its domain.** Lisi's `E8`
   model assigned Standard-Model fermions to an `SU(5) ⊂ E8` — an honest DG-object
   (Lorentz-in-`E8`, compact centralizer, matter from adjoint branching). DG's theorem
   is exactly what shows that assignment yields a **vectorlike** (non-chiral) spectrum.
   That is DG doing its job **inside** `DG_E8`. GU is **not** making that kind of claim.

2. **GU never claims to be a single-`E8` ToE.** GU's stated symmetry group is `Sp(64)`
   from `Cl(9,5) ≅ M(64,H)`; its chirality mechanism is an operator index on a bundle over
   a non-compact base. It makes **no** claim to embed Lorentz inside one `E8`, and **no**
   claim to read chirality off an `E8` adjoint. So the premises DG needs are simply absent.

3. **"Relabeling" would be swapping notation while keeping the structure DG assumes.** GU
   does the opposite: it changes the **structure** — different group (dim 8256 vs. 248),
   different chirality invariant (operator index vs. reality type), different data type
   (non-compact bundle vs. finite-dim adjoint). These are **checkable structural
   differences** (§3, §6), not cosmetic renamings. A referee can verify each without
   trusting GU's framing.

4. **The distinguishing test is objective.** "Is GU an object of `DG_E8`?" has a definite
   answer: it must satisfy DG-A1..A7. It fails four of them, verifiably. If a critic
   insists DG still applies, the burden is precise and stated (§4): **exhibit a functor
   `F_DG: GU_data -> DG_E8` that lands in the correct category and preserves the chirality
   invariant.** No such functor exists in the audited candidates. Until one is produced,
   "DG applies to GU" is an unsupported assertion.

5. **We concede everything DG actually proves.** On any DG-shadow of GU, the answer is
   vectorlike — DG's result reproduced (§4, §5). We are not claiming DG is wrong on its
   domain; we are claiming GU is not in that domain. Conceding the theorem while denying
   membership is the *opposite* of moving goalposts.

---

## 10. Verdict

> **EVASION BY SCOPE EXIT — Distler-Garibaldi is INAPPLICABLE to GU.**
>
> GU is **not** an object of the category `DG_E8` that DG's theorem quantifies over: it
> violates **DG-A1** (gauge group `Sp(64)`, not a real form of `E8` — dim 8256/rank 64 vs.
> 248/8, certificate PASS), **DG-A2** (Lorentz acts on the base `X^4` / fibers
> `GL(4,R)/O(3,1)`, not inside the gauge group), **DG-A6** (chirality carrier is the
> operator index `ind_H(D_GU) ∈ KSp^0`, not the reality type of a `V_{2,1}` branch), and
> **DG-A7** (GU is bundle data on the non-compact `Y^{14} = Met(X^4)`). The Krein/ghost
> sub-route is likewise a scope exit via **DG-A3** (needs non-compact `SO(5,5)` by the Weyl
> trick; retracted from its former "inside-class" framing).
>
> DG is a **correct theorem**; it is **reproduced, not contradicted**, on GU's
> representation-theoretic shadow. Invoking it against GU is a **category error**. There is
> **no residual DG obligation**. **Reopen only if** a functor `F_DG: GU_data -> DG_E8` is
> exhibited that lands in the correct category **and** preserves the chirality invariant.
>
> **Firewall confirmed:** this verdict is independent of the value of `ind_H(D_GU)`, which
> is **OPEN** (§7) and appears nowhere in the argument (self-audit §8, no contamination).

---

## 11. Grade ledger (reconstruction-grade vs. proof-grade, per step)

| Step | Content | Grade |
|---|---|---|
| §1 | DG stated as DG-A1..A7 + null conclusion | faithful restatement (proof-grade as a *statement*, sourced) |
| §3.1 / §6 | DG-A1 fails: no `Sp(64) -> E8` embedding (dim + rank) | **proof-grade** — executable certificate, PASS exit 0, independent re-derivation |
| §3.2 | DG-A2 fails: Lorentz on base, not in gauge | **reconstruction-grade** (architectural fact of `Y^{14}=Met(X^4)`; no certificate) |
| §3.3 | DG-A6 fails: chirality = operator index, not reality type | **reconstruction-grade** (invariant-*type* claim; value-independent, firewalled) |
| §3.4 | DG-A7 fails: bundle data on non-compact base | **reconstruction-grade** (data-type read-off) |
| §5 | DG-A3 scope exit (Krein / Weyl trick); retraction | **reconstruction-grade**; Weyl trick itself elementary; kinematics machine-checked in source |
| §4 | No functor `F_DG` into `DG_E8` preserving the invariant | **reconstruction-grade** (audit of natural candidates; not an exhaustive impossibility proof) |
| §7 | `ind_H(D_GU)` value | **OPEN** (not claimed) |
| §8 | Firewall / contamination self-audit | argued; **no contamination found** |

**Honest residual.** The single proof-grade pillar is DG-A1 (the certificate). DG-A2/A6/A7
are argued **structurally** from the construction's architecture, which is the appropriate
grade for "which category is this object in" — but a hostile referee could still demand a
fully formal definition of `GU_data` as a category and a proof that no forgetful functor to
`DG_E8` exists (§4 audits candidates; it is not an exhaustive non-existence theorem). That
gap is the honest open edge of this note. It does **not** touch the verdict's logic: four
independent assumption-failures, one of them certificate-backed, each removing GU from
`DG_E8`.
