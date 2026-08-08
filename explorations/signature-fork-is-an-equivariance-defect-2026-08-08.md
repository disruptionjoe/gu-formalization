---
artifact_type: exploration_result
created: 2026-08-08
status: FORK_IS_NON_EQUIVARIANCE__RETYPING_PROPOSED_NOT_EXECUTED__ONE_PRIOR_CLAIM_CORRECTED__SOURCE_CONVENTION_DIVERGENCE_NAMED
grade: "EXACT for everything computed. tests/signature_fork_equivariance_defect.py
  is green: Levi-Civita invariance under g -> -g at residual 0.00e+00, DeWitt
  invariance at 0.00e+00, causal cone identical on 4000 samples, ABS Clifford
  classes from the table, fibre signatures by eigenvalue count. The TT-positivity
  criterion in test (4) is an IMPORTED PHYSICAL INPUT, labelled as such, not a
  consequence of GU's action. The RETYPING is proposed and NOT executed."
run_id: GUH-20260808T060000Z-register-side-track
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/signature-ambient-is-a-sign-convention-2026-08-08.md
  - explorations/mh9-tier1-mechanism-falsified-2026-08-08.md
---

# The signature fork is an equivariance defect

Produced by a divergent-persona sweep over the session's own output, looking for
what was missed. Five personas returned something; the source critic returned the
one that changes a verdict type.

## The correction, first

`signature-ambient-is-a-sign-convention-2026-08-08.md:57` stated
`Cl(3,1) = M(2,H)` and `Cl(1,3) = M(4,R)`. **Those are swapped.** By the
Atiyah–Bott–Shapiro table on `(p−q) mod 8`:

```text
Cl(3,1)  p-q = +2  ->  M(R)     REAL          Cl(3,1) = M(4,R)
Cl(1,3)  p-q = -2  ->  M(H)     QUATERNIONIC  Cl(1,3) = M(2,H)
```

`mh9-tier0-and-register-triage-2026-08-08.md:91` states it **correctly**, so the
repository contradicted itself within a few hours on the same day. The paragraph's
argument survives — it turns on the two algebras *differing*, not on which is
which — but the file was wrong and is now bannered and fixed.

**Structural fact that fell out of checking it.** The `(6,4)` fibre has
`p−q = +2`, and `+2 mod 8` toggles class `2↔4` and `6↔0` — that is exactly
`REAL ↔ QUATERNIONIC`. So **the fibre always flips the reality type**, and base
and ambient never agree:

```text
base (3,1) = R  + fibre (6,4) = R  ->  ambient (9,5) = H
base (1,3) = H  + fibre (6,4) = R  ->  ambient (7,7) = R
```

## The finding

Yesterday's conclusion was *"the fork reduces to the base sign convention"*, filed
as still-open. That is one step short of a stable position, and the missing step
changes the row's type.

**Step 1 — the relabeling is geometrically empty, more so than was claimed.**
Beyond the causal cone (identical on 4000 samples), the Levi-Civita connection is
*literally invariant*: `Γ = ½g⁻¹(∂g + ∂g − ∂g)` carries one `g⁻¹` and one `∂g`, so
the two sign flips cancel. Residual `0.00e+00`. **Geodesics, curvature and
parallel transport are identical.** `g` and `−g` are the same geometry in every
sense that a connection sees.

**Step 2 — the fibre form does not follow the relabeling.** `G(−g) = G(g)`
exactly, so the fibre is `(6,4)` on both bases. This is what the registry already
records: *"the fibre is (6,4) both ways."*

**Step 3 — therefore the construction is not equivariant.**

```text
same geometry in  ->  base (3,1) -> ambient (9,5) = M(64,H)
                  ->  base (1,3) -> ambient (7,7) = M(128,R)
```

A pure relabeling cannot change the real Clifford class. So `g ↦ g ⊕ G(g)` is
**defective as a construction** — not under-determined by evidence.

## The repair, and what it does to the fork

A well-posed construction transports **both** blocks: `g ↦ g ⊕ ε·G(g)` with `ε`
tied to the base convention. Then:

```text
base (3,1) + fibre (6,4) = (9,5) = M(H)
base (1,3) + fibre (4,6) = (5,9) = M(H)
```

Both `M(ℍ)`, because `p−q = +4` and `−4` are the same class mod 8. The relabeling
becomes invisible, as it must be. **On the repair, `(7,7)` is not a sign horn at
all** — it would require a genuinely different fibre form, not a relabeled one.

## The remaining bit is pinned by physics, and it is imported

The overall sign of `G` is the one genuinely free bit. It is fixed the way it is
fixed in Wheeler–DeWitt:

```text
+G : TT (graviton) norm +2, conformal mode -4   <- standard conformal-factor problem
-G : TT norm -2, conformal mode +4              <- physical gravitons are ghosts
```

`+G` gives fibre `(6,4)`; `−G` gives `(4,6)`.

**Stated plainly because it matters:** TT-positivity is *physics imported from
outside GU*, not a consequence of GU's action, and it is itself
convention-relative — under a global flip, what counts as positive kinetic norm
flips too. So it pins the fibre sign **relative to the base**, which is precisely
what the repair needs, and it does **not** independently select a horn.

## What the source critic found, and nobody had checked

**The source declares the base convention, repeatedly, and it is not the
repository's.**

| where | what it says |
|---|---|
| `claim-mining-toe-weinstein-complete-2026-07-31.md:90` (WG-A04) | "Input signature `(1,3)` generates a 14-dimensional total space" — `AUTHOR-STATED` |
| same, `:94` (WG-A08) | tower `(1,3)`, `(1,7)`, `(1,11)` — `AUTHOR-STATED` |
| `gu-2021-draft-s11-s12-extraction-2026-08-03.md:137` | "for `Spin(1,3)×Spin(6,4)`" |
| `transcripts/portal-special-gu-first-look-2020-04-02.md:525` | "we are trapped in the `(1,3)` sector" |
| `gu-paper-reference-surfaces.md:23–24` | `H = Spin(1,3)`, `N = ℝ^{1,3}` |

The repository runs `(6,4) + (3,1) = (9,5)`. **The source's declared base is the
other one.** No file had put the source's convention next to this fork.

**And the source's route to `(7,7)` uses the fibre sign the repo's own supermetric
rejects.** `curt-iceberg-7-7-reasoning-reinspection-2026-07-31.md` records the
spoken blocks as vertical `(4,6)` + horizontal `(1,3)`, which literally sums to
`(5,9)`, and notes that reaching the asserted `(7,7)` needs `(4,6) + (3,1)`. That
route takes the `(4,6)` fibre — the ghost-like sign. So:

- the source's **spoken arithmetic** gives `(5,9)`, which is the global flip of the
  repository's `(9,5)` — *the same physics, correctly*;
- the source's **asserted total** `(7,7)` requires mixing the two conventions.

That reinspection file had already flagged the arithmetic as `SOURCE-UNTYPED`.
What is new is that the mismatch is now **diagnosed** rather than noted: it is the
same non-equivariance, appearing in the source.

## The seventh homonym: `Cl(3,1)` itself

Chasing the swap turned up something larger than the swap. The **label** is
ambiguous even though the **algebras** are not. Certified three independent ways
(explicit real 4×4 construction, 60-restart randomized search, ABS table):

```text
THREE generators squaring to +1, ONE to -1   ->  M(4,R)   REAL
ONE   generator  squaring to +1, THREE to -1 ->  M(2,H)   QUATERNIONIC
```

Both repository usages are individually defensible and they **name opposite
algebras**:

| file | `Cl(3,1)` means | class |
|---|---|---|
| `generation-sector/oq-rk1-rs-rank-first-principles-2026-06-23.md:560` | mostly-minus `η = diag(+,−,−,−)`, one `+` | `M(2,ℍ)` |
| the `SIGNATURE-AMBIENT` line, incl. `(6,4)+(3,1)=(9,5)` | three `+` | `M(4,ℝ)` |

This is exactly the collision Layer-0 exists to catch, and it had not been
recorded. It also explains how the swap survived: both readings are in the
repository, so neither looks wrong locally.

**A separate, smaller error found inside that file, now bannered.** It computes
`(p−q) mod 8 = 2` and calls class 2 "quaternionic-split". Class 2 is `M(ℝ)`. The
file's **conclusion** `M(2,ℍ)` survives — it means the mostly-minus algebra, which
really is `M(2,ℍ)`, so `rank_ℍ(S^±) = 1` and everything downstream is unaffected —
but the index arithmetic it used to get there names the other algebra. The file is
already `verdict: OPEN` with its central step retracted as circular, so nothing
established rests on it.

## What the other personas returned

- **Historian.** The N1 audit derived the fibre `(7,3) → (6,4)` and then *added*
  base `(3,1)` to reach `(9,5)`. The fibre step is convention-invariant (shown
  today). The base was **assumed, not derived, and not declared**. `(9,5)` was
  always conditional on an undeclared convention.
- **Differential geometer.** "Same geometry" was under-claimed, not over-claimed.
  Levi-Civita invariance is stronger than the cone argument and was available.
- **Clifford algebraist.** Found the swap; supplied the mod-8 reason the fibre
  always toggles the reality type.
- **Layer-0 auditor.** "Signature" is carrying three objects — ambient, base,
  fibre. The row id says `AMBIENT`, so it is typed, and no homonym fires. Clean.

## What this does not do

- **It does not change the ledger row.** Retyping `SIGNATURE-AMBIENT` from
  *under-determined, awaiting a resolver* to *ill-posed as stated, awaiting a
  construction repair* is verdict-adjacent and takes the hostile-review path under
  the standing 2026-08-03 rule. Proposed here, not executed.
- **It does not adjudicate the source divergence.** That the source says `(1,3)`
  and the repository runs `(3,1)` is now named. Whether the repository should
  follow the source's convention is a separate decision with a wide blast radius —
  every `dim_H` restatement, the Kramers wall, every Majorana-availability
  statement is downstream of it.
- **It does not touch the count.** The generation-sector chain is unaffected.
- `REAL-CLIFFORD-FORM` is a **distinct row and stays settled.** The registry's own
  warning — *"Distinct from `REAL-CLIFFORD-FORM`, which IS settled"* — is
  respected here.

## Owed

`M-H9` was falsified this morning and the registry's `named_resolver` for this row
is `NONE`. If the retyping is accepted on review, the row does not need a
resolver, because it does not need resolving — it needs the construction fixed.
That is a smaller and much more tractable job than the depth-10 fork it is
currently filed as.
