---
title: "SC-A: the best-supported reconstruction of 'the right chain' is a rank-10 normal-bundle reduction pattern, not a GUT subgroup tower"
created: "2026-08-15"
doc_type: construction_result
status: reconstruction_partial
canonical_effect: pending_integration
result: "R1/R2/R3 KILLED by exact group theory (12 > 10, and the largest centraliser of any Spin(3,2) in Spin(6,4) is 10). The best-supported reconstruction is Spin(6,4) > SU(3,2) > S(U(3)xU(2)), interpreted as a compatible complex/special-unitary reduction followed by a maximal-compact reduction on the same rank-10 vertical bundle. The embeddings construct fibrewise; they do not construct the global bundle reductions. Audio confirmation, the absent 2021 PDF, global complex/determinant reduction data, and the REDUCTION_EXTERNAL selector remain open. Register entry proposed, not written."
target_claim: "internal: the repository-written chain `Spin(6,4) -> Spin(3,2) -> maximal compact SU(3) x SU(2) x U(1)`, at explorations/wave14/H19-seven-seven-signature-branch-2026-07-11.md:114 and :157, and la6-the-lagrangian-axis-...-2026-08-15.md:918"
target_claim_verdict: "KILLED AS WRITTEN. dim so(3,2) = 10 and dim(su(3)+su(2)+u(1)) = 12, so the second arrow admits no injective homomorphism. SU(3,2) is the best-supported reconstruction of the middle slot because it makes the adjacent maximal-compact sentence consistent and matches the extraction-mediated 2021 equation, but the disputed audio was not checked and the 2021 PDF is absent. No source claim is killed; the literal repository nesting is."
test: tests/channel-swings/joe_directed_sca_right_chain.py
certificate: "85/85 checks, exit 0; --selftest: 4 planted false facts each force exit 1 and the clean run exits 0"
---

> [!CAUTION]
> **CORRECTION IV-20260815 — EVIDENCE AND GLOBALITY.** The original artifact
> repeatedly called the `SU(3,2)` chain “decided” and said the source supplies
> arrow 1. That was too strong. The exact algebra decides which literal readings
> are impossible and constructs the subgroup embeddings. It does not determine
> what was said on the unchecked audio, independently verify the absent 2021
> draft PDF, or construct a global reduction of the normal bundle. The
> `SU(3,2)` reading is the **best-supported reconstruction**: it is consistent
> with the adjacent transcript sentences and the registered draft extraction.
> Arrow 1 additionally needs a global compatible pseudo-Hermitian complex
> structure and the determinant data reducing `U(3,2)` to `SU(3,2)`; arrow 2
> remains `REDUCTION_EXTERNAL`. The original exact dimensions, centraliser
> obstruction, embeddings, and intersection calculations are preserved.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `SOURCE_NATIVE_ROUTE`.

`SOURCE_NATIVE_ROUTE` is the right value because the object under test is the
source's own sentence and the source's own reduction operation. The
Georgi-Glashow chain `Spin(10) > SU(5) > G_SM` appears here only as a contrast
class, and the artifact's headline is precisely that the source **refuses** that
comparator: *"There is no grand unification. It's just a normal bundle in your
ambient space."*

> [!IMPORTANT]
> **Registry consequence, named rather than dodged, and measured rather than
> assumed.** `doc_type: construction_result` puts this file inside
> `process_gates/source_native_comparator_routing_audit.py`'s derived scope. I
> may not edit `lab/process/source-native-comparator-routing-registry.json`, so
> the audit's `UNCLASSIFIED` count rises until the method owner adds the row
> `{"path": "lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md",
> "classification": "SOURCE_NATIVE_ROUTE"}`.
>
> **Measured, 2026-08-15:** the gate was **already red before this file
> existed** — 10 unclassified against a baseline of 9, because a concurrent
> agent added `lab/active-research/joe-directed/indefiniteness-typing/itc-positivity-rows-are-five-not-ten-2026-08-15.md`
> minutes earlier. This file takes it 10 → 11. So the honest statement is
> **+1 to an already-failing gate**, not "this file turned the gate red"; both
> rows are owed and neither is mine to write. The classification is declared
> in-file above, which is what the *method* asks for; the *gate* wants a
> registry row. Declaring `stewardship_record` would have hidden this by lying
> about what this file is.

---

# SC-A — reconstructing "the right chain"

Joe-directed, 2026-08-15. On 2026-08-15 a deleted sentence was restored to the
`primary_source` transcript at `[00:45:00]`. Verbatim, from
`papers/drafts/Transcript into the impossible.md:155`:

> *"But this is the right chain. **Spin six four, spin three comma two, s u three
> cross s u two cross u one,** Brian, in terms of the axis of evil in certain,
> Lorentz breaking directions in space."*

Read literally that is `Spin(6,4) > Spin(3,2) > SU(3)xSU(2)xU(1)`, and
`dim Spin(3,2) = 10 < 12 = dim SU(3)xSU(2)xU(1)`. This artifact tests what the
sentence can consistently mean instead.

---

## 0. PREFLIGHT

### 0.1 Retrieval, run BEFORE the work

Not before a novelty claim — before deciding what to compute. Every object and
every number I expected to produce was searched first, in its alternative
vocabularies. The sweep changed the shape of this artifact twice.

| object searched (with alternatives) | verdict | where |
|---|---|---|
| `SU(3,2)`, `su(3,2)`, `s u three comma two`, `\mathfrak{su}(3,2)`, `SU_{3,2}` | **PRESENT**, 221 hits / 110 files | `tests/legs/forces_maximal_compact_is_sm.py`, `tests/one-residual/forces_maxcompact_independent.py`, `lab/sources/source-claim-register.yaml:358` (SC-GRP-03) |
| max compact of `su(3,2)` **is** the SM algebra | **PRESENT and machine-verified twice**, independent methods | `tests/legs/forces_maximal_compact_is_sm.py` (full Cartan-involution proof), `tests/one-residual/forces_maxcompact_independent.py` |
| SM as **maximal compact rather than symmetry breaking** | **PRESENT and already adjudicated `REDUCTION_EXTERNAL`** | `explorations/big-swing-2026-07-03/AUDIT-noncompact-compact-reduction-EXTERNAL.md:21-25` |
| `SU(3,2)` vs `Spin(3,2)` as the middle node | **SU(3,2) selected as the source-internally consistent reconstruction; audio not checked** | `lab/active-research/joe-directed/ledger-advancement/la7-...-2026-08-15.md:288-304` |
| `S(U(3)xU(2))`, `Z_6`, global form | **PRESENT**; `Baez`/`Huerta` **ABSENT** | `RESEARCH-STATUS.md:503`; `tests/anchored-leads/sm_z6_quotient_bridge.py` |
| `Spin(6,4)`, `Pati-Salam`, `Spin(6)xSpin(4)`, `(7,3) -> (6,4)` | **PRESENT, saturated** (3006 Pati-Salam hits) | `lab/active-research/pati_salam_chain_verification.py`, `canon/shiab-existence-cl95.md:31` |
| `Sp(4,R)` literal | **0 hits**; `so(3,2) ~= sp4(R)` present in 3 ledger files | `lab/process/selected-k80-rsap-a3-cross-real-form-incidence.json:38` |
| `Spin(3,2)` **as AdS_4 isometry / conformal group** | **ABSENT — the identification is never made** | `AdS_4` appears only in the Vasiliev comparison |
| **Killing form of `so(3,2)` has signature `(6,4)`** | **ABSENT** | nearest is `cc1-killing-signature-cannot-sign-lambda-2026-08-14.md`, which works the Killing form on the **adjoint 45**, a different object |
| realification `U(p,q) < SO(2p,2q)` as a stated embedding | **ABSENT as an embedding**; present only as the **commutant** direction | `tests/big-swing/vg_v3_j_commutant_conformal_native.py:419` computes `centralizer(J_0) in so(6,4) = 25 = dim u(3,2)` |
| Siegel parabolic / Levi / `gl(5) + Lambda^2` presentation of `SU(5) < Spin(10)` | **0 hits** | — |
| `45`, `24`, `21`, `12`, `25` as these dimensions | **PRESENT** individually | `pv2-...-2026-08-14.md:47` has `so(6,4) = 45 = k(21) (+) p(24)` |
| the chain in `lab/sources/`, `canon/`, `CANON.md`, `CURRENT-STATE.yaml` | **ABSENT — 0 hits, never promoted** | — |

**Two things the retrieval killed before I wrote a line.**

1. *"The SM is the maximal compact, not a broken subgroup"* is **not novel here.**
   It is a named, dated, audited result with the verdict `REDUCTION_EXTERNAL`.
   Had I led with it I would have made the eighth false-novelty claim of this
   channel. It is an **input** below, cited, not re-derived as mine.
2. *"The middle node is `SU(3,2)`, not `Spin(3,2)`"* was **selected this morning
   as the consistent transcript reconstruction** by LA-7 §1.4, using the
   arithmetic `dim K(SU(3,2)) = 12` vs
   `dim K(Spin(3,2)) = 4`. My contribution is **not** that decision. LA-7 tested
   the *adjacent sentence* ("what is the maximal compact subgroup of X"). Nobody
   has tested the **chain sentence**, whose obstruction is a different integer
   (`12 > 10`, not `12 != 4`), and nobody has decided what **kind** of chain it is.

**One thing the retrieval found that the brief did not know.** The textual
apparatus added to the transcript today asserts *"the chain occurs nowhere in
`lab/sources/`, `explorations/` or `canon/`."* The `lab/sources/` and `canon/`
halves are correct (0 hits, re-verified). The `explorations/` half is **wrong**:
`explorations/wave14/H19-seven-seven-signature-branch-2026-07-11.md:114` writes
`Spin(6,4) -> Spin(3,2) -> maximal compact SU(3) x SU(2) x U(1)` verbatim, and
`:157` repeats it. So the repository has not merely been blind to the chain — it
has been carrying a **group-theoretically impossible** version of it since
2026-07-11, sourced to `[00:43:47]-[00:45:00]`. That is this artifact's internal
target.

### 0.2 Five specialist lenses, run inline

**Lens 1 — Lie theory and real forms.** *What can actually sit inside what?* The
governing facts are dimension and centraliser, and both are computable exactly.
`dim so(p,q) = n(n-1)/2` depends only on `n = p+q`, so a signature relabelling
can never rescue a dimension obstruction — a sweep, not an assertion, must show
this. The one place real-form structure genuinely bites is that
`SU(3,2) < Spin(6,4)` is **not** a dimension coincidence but the realification
`U(p,q) < SO(2p,2q)` — the real form of the classical `SL(5,C) < SO(10,C)`. That
embedding is absent from the repo in the embedding direction and must be built,
not cited.

**Lens 2 — symmetry-breaking chain construction.** *Is this a breaking chain at
all?* Sharpened by the coordinator's mid-task material and it changed the
result. The source says *"There is no grand unification. It's just a normal
bundle in your ambient space"* and, immediately before, counts every GUT group by
the **10** it acts on: `SO(10)` is 10 real, `SU(5)` is 5 complex = 10 real,
Pati-Salam is `spin six ... cross spin four, six plus four, ten`. He is not
tracking containments, he is tracking **structure-group reductions of one
rank-10 bundle**. That reframes the whole sentence and it is the reason R6 below
is stated as reductions rather than as a subgroup tower.

**Lens 3 — conformal / AdS group theory.** *Is `Spin(3,2) ~ Sp(4,R)` really in
the picture?* The brief flags this as a strong constraint nobody has used and
tells me to test it rather than assume it. Two separate things must be checked:
whether the identification is **true** (it is, and the repo has never made it),
and whether it is **in evidence** (tested below; it is not). The brief also
contains an error I must correct rather than propagate.

**Lens 4 — primary-source philology.** *What is the evidence class of a single
ASR token?* The decisive question is not "which group is prettier" but "does this
transcript demonstrably corrupt this exact construction elsewhere?" That is a
falsifiable textual question with a yes/no answer inside the same speaker turn.

**Lens 5 — epistemics of attribution.** *Which direction is the mis-attribution
risk running?* Both ways, and they are asymmetric. Reading repository proposals
back as source content is the failure the brief warns of; but **overriding the
source's spoken word with a prettier group** is the mirror failure, and it is the
one this artifact is at risk of. The mitigation is structural: the register
`verbatim` field must carry `spin three comma two` exactly as spoken, and the
adjudication must live in `notes`, where it is visibly an inference.

**Lens 6 — representation branching / centraliser theory.** *How do you kill a
factorisation reading exhaustively rather than by failing to find one?* Not by
searching for embeddings, but by bounding the centraliser over **all** module
structures. Complexifying makes the enumeration finite and signature-blind, which
converts "I could not construct it" into "it does not exist."

---

## 1. THE COMPUTATION

All of §1 is `tests/channel-swings/joe_directed_sca_right_chain.py` — **85/85,
exit 0**, exact integers and `fractions.Fraction` throughout, `assert_no_float`
sweeping the whole result structure. Every Lie algebra is built from an explicit
integer basis and checked for bracket closure before any dimension is read off; no
dimension below is a formula lookup.

### 1.0 Positive controls first

`dim so(p,q)` from explicit bases for `(3,0), (2,1), (5,0), (3,2), (6,4)` = `3, 3,
10, 10, 45`, each closing under bracket. `dim u(3,2) = 25`, `dim su(3,2) = 24`,
realified from `{0, +-1, +-i}` entries. The exact congruence-signature routine is
power-tested on a diagonal form, on a **zero-diagonal hyperbolic pair** (the path
that breaks naive implementations), on a degenerate form, and on the Killing
forms of `so(3)` → `(0,3)` and `so(2,1)` → `(2,1)`.

### 1.1 R1, the literal nesting — KILLED by one integer

```text
dim so(3,2)                    = 10      (explicit basis, bracket-closed)
dim su(3) + su(2) + u(1)       = 12      (built as the theta-fixed part of su(3,2))
12 > 10  ->  no injective homomorphism  g_SM -> so(3,2)  exists
```

**Sweep, so this is not an artefact of the signature.** Every `so(p,q)` with
`p+q = 5` has dimension 10: `so(0,5), so(1,4), so(2,3), so(3,2), so(4,1),
so(5,0)` all → 10. The smallest orthogonal algebra of dimension `>= 12` is
`n = 6`, at dimension 15. So **no** relabelling of `(3,2)` rescues the arrow.
Among the `(3,2)`-labelled real forms, `so(3,2) = 10`, `su(3,2) = 24`,
`u(3,2) = 25` — only the unitary ones clear 12.

### 1.2 R2, the commuting factorisation — KILLED by exhaustion

The brief's second candidate: not a nesting but a factorisation, `Spin(3,2)`
alongside `SU(3)xSU(2)xU(1)` rather than above it. This is killed by bounding the
**centraliser**, over all possibilities.

*Why the enumeration is exhaustive.* A real subalgebra `h_0 < g_0` has centraliser
`z_0` cut out by real linear equations, so `z_0 (x) C` is the centraliser of
`h_0 (x) C` in `g_0 (x) C` and the dimensions agree. `so(3,2) (x) C = so(5,C)` and
`so(6,4) (x) C = so(10,C)` **independent of signature**, so the count below covers
every real embedding at once.

Irreducible `so(5,C) = sp(4,C)` modules of dimension `<= 10`, from the Weyl
dimension formula on `C_2` with Frobenius-Schur type read off the central
character `(-1)^a`:

| highest weight | dim | type |
|---|---:|---|
| `(0,0)` | 1 | orthogonal |
| `(1,0)` | 4 | **symplectic** |
| `(0,1)` | 5 | orthogonal |
| `(2,0)` | 10 | orthogonal (the adjoint) |

and nothing else at or below 10. Now enumerate every way `C^10` can be such a
module carrying a **nondegenerate** invariant symmetric form. A symplectic-type
isotypic block needs **even** multiplicity, otherwise the symmetric form restricts
to zero there and degenerates. Centraliser dimension is
`m(m-1)/2` per orthogonal-type block and `m(m+1)/2` per symplectic-type block:

| decomposition of `C^10` | centraliser dim |
|---|---:|
| `10` (adjoint) | 0 |
| `5 (+) 5` | 1 |
| `4 (+) 4 (+) 1 (+) 1` | 4 |
| `5 (+) 1^5` | **10** |

```text
max centraliser of ANY Spin(3,2) in Spin(6,4)  = 10
dim SU(3) x SU(2) x U(1)                       = 12
12 > 10   ->  R2 KILLED
```

**Contrary control — the machinery must accept a true case.** The same predicate
**accepts** a commuting `Spin(3,2) x Spin(3,2) < Spin(6,4)` at the `5 (+) 1^5`
row, and the artifact then **exhibits it explicitly**: two block-diagonal copies
of `so(3,2)` on `R^{3,2} (+) R^{3,2}`, each of dimension 10, verified to commute
elementwise and verified to satisfy `X^T eta_{6,4} + eta_{6,4} X = 0` after
reordering the basis. So the test discriminates: it rejects `Spin(3,2) x G_SM`
and accepts `Spin(3,2) x Spin(3,2)`, which differ only in the second factor.

**Planted failing controls.** `5 (+) 4 (+) 1` is rejected — odd multiplicity of
the symplectic `4` makes the invariant symmetric form degenerate. `1^10` is
rejected — `so(5,C)` would act trivially and is then not a subalgebra of `so(V)`
at all.

### 1.3 R3 / R4, the spacetime and AdS readings

```text
dim so(3,2) = 10 = dim of the isometry algebra of a maximally symmetric 4-manifold
dim so(4,2) = 15
dim so(1,3) = 6
```

**The brief's identification is half right and I must correct the half that is
wrong.** `Spin(3,2) ~ Sp(4,R)` is **correct**: `so(3,2)` has real rank
`min(3,2) = 2` equal to its rank 2, so it is **split**; `sp(4,R)` is split of rank
2 and dimension 10; `B_2 = C_2` and split real forms are unique, so they are
isomorphic. `SO(3,2)` **is** the AdS_4 isometry group. But it is **not** "the
`3+1` conformal group": the conformal algebra of `R^{3,1}` is `so(4,2)`, of
dimension **15**, not 10. `so(3,2)` is the conformal algebra of `2+1` Minkowski.
The repo has never made either identification, and the wrong half should not enter
it.

**Is it in evidence? No.** The source's spacetime factor is `Spin(1,3)` — that is
what draft-2021 eq (4.6) prints (`Spin(1,3) x Spin(6,4) -> Spin(7,7)`, register
`SC-GRP-03`), and `dim so(1,3) = 6 < 10`, so `so(3,2)` does not fit the spacetime
slot. The chain's ambient is the **vertical** rank-10 fibre, whose structure
algebra `so(6,4)` has dimension 45. Nothing in the passage mentions AdS,
conformal symmetry, or `Sp(4,R)`. **R4 is a true identity that is not in
evidence**, and importing it would be exactly the "read repository proposals back
as source content" failure. It is recorded as an unused observation, not as a
finding.

### 1.4 R5 — why the token `(3,2)` and the fibre `(6,4)` are the same space

This is the one place where the literal reading is not merely a garble, and it is
new to the repository.

```text
Killing form of so(3,2):  dimension 10,  signature (6,4)     <- EXACT
```

**Sweep over all real forms with `p+q = 5`:**

| algebra | dim | Killing signature |
|---|---:|---|
| `so(5,0)` | 10 | `(0,10)` |
| `so(4,1)` (de Sitter) | 10 | `(4,6)` |
| **`so(3,2)`** | 10 | **`(6,4)`** |
| `so(2,3)` | 10 | `(6,4)` |
| `so(1,4)` | 10 | `(4,6)` |
| `so(0,5)` | 10 | `(0,10)` |

**`(3,2)` is the unique signature in dimension 5 whose orthogonal algebra carries
a Killing form of signature `(6,4)`** — the exact signature of the trace-reversed
Frobenius metric on GU's rank-10 vertical space. So the adjoint representation
gives a genuine embedding `Spin(3,2) < Spin(6,4)`: `ad` is injective (image
dimension 10, computed) and every `ad(X)` is skew for the Killing matrix `K`
(`ad^T K + K ad = 0`, verified on every generator).

This matters as a repository reconstruction because Weinstein discusses the
Killing form **in the same breath**:
*"we wanted to avoid indefinite signature on the killing form ... how nature
handles the indeterminacy of the killing form."* The 10-dimensional `(6,4)` space
under discussion can be modelled, as an orthogonal space, by
`(so(3,2), B_Killing)`. The source does not state that adjoint identification.

**But R5 does not rescue R1.** The centraliser of the adjoint copy inside
`so(6,4)` is exactly **0** (computed; Schur, the adjoint is irreducible), so
nothing at all — least of all a 12-dimensional `g_SM` — commutes with it. R5 is
real structure and a plausible reason the token `(3,2)` is in his mouth. It is not
a chain step.

### 1.5 R6 — the best-supported reading, built fibrewise

```text
Spin(6,4)  ---(1)-->  SU(3,2)  ---(2)-->  S(U(3) x U(2)) = (SU(3)xSU(2)xU(1))/Z_6
```

**Step (1) has a genuine subgroup embedding and is the algebraic model for a
complex/special-unitary reduction.**
Realify `C^5` with a Hermitian form of signature `(3,2)`: `Re(h)` is a real
symmetric form of signature `(6,4)` on `R^10`. The artifact builds `u(3,2)` and
`su(3,2)` from `{0, +-1, +-i}` entries, realifies, and **verifies**
`X^T eta_{6,4} + eta_{6,4} X = 0` for every generator, with the image dimensions
still 25 and 24 (injective). So `SU(3,2) < Spin(6,4)`, `24 <= 45`. This is the
indefinite real form of the classical `SL(5,C) < SO(10,C)` — i.e. of the
Georgi-Glashow embedding — and the repo had only the **commutant** direction of
it (`vg_v3_j_commutant_conformal_native.py:419`), never the embedding.

The source mentions a distinguished direction and a complex structure in the
**next sentence after the chain**: *"If you take the one dimension that's
distinguished in the space of all metrics and **this has a complex
structure**..."* That is evidence for the reconstruction, not a construction of
the reduction datum. A global arrow needs a section of the associated
`SO(6,4)/U(3,2)` bundle plus determinant/trivialisation data for the further
`U(3,2) -> SU(3,2)` reduction; neither is supplied here.

**Step (2) is a maximal-compact reduction, and the source names the operation.**
The `theta`-fixed part of `su(3,2)` has dimension **12**, derived algebra
dimension **11** (`su(3) + su(2)`), and centre dimension **1** (hypercharge) — all
computed, not asserted. On `u(3,2)` the same reduction gives **13 = 12 + 1**. The
source's named operation, `[00:46:40]`: *"reduce maximal compact subgroups along
the fibers."*

**And the reading reproduces the register's written claim numerically.**
`SC-GRP-03` (draft-2021 p.29 eq (4.6)) says the SM group *"is found within the
intersection of the simultaneous reductions up to a reductive factor of `U(1)` if
the special unitary group `SU(3,2)` is not privileged over the full unitary group
`U(3,2)`."* Computed here for the first time as an actual intersection of
subspaces inside `so(6,4)`:

```text
dim( so(6)+so(4)  n  su(3,2) )  = 12      <- exactly the Standard Model algebra
dim( so(6)+so(4)  n   u(3,2) )  = 13      <- "up to a reductive factor of U(1)"
dim( so(6)+so(4)  n  so(3,2) )  =  4      <- the garble reading, PLANTED CONTROL
dim( so(6)+so(4) )              = 21      <- Pati-Salam
```

Two simultaneous reductions of one `Spin(6,4)` bundle — maximal-compact
(Pati-Salam) and complex (`U(3,2)`) — meeting in the Standard Model. The `12` vs
`13` reproduces the eq (4.6) sentence's own `U(1)` proviso to the integer, from a
completely independent construction. **The registered extraction of the 2021
written edition therefore corroborates the reconstructed middle term as
`SU(3,2)`/`U(3,2)`.** The PDF itself is absent from this checkout, so this
artifact does not claim an independent visual check of the typeset equation.

### 1.6 The philological control — a same-frame transcription hypothesis

Counted exactly in `papers/drafts/Transcript into the impossible.md`:

| string | count | where |
|---|---:|---|
| `s u three comma two` | **2** | `[00:43:47]`, the paragraph immediately before the chain |
| `spin three comma two` | **1** | inside the chain sentence itself |

So in a 90-second window the source says the unitary form **twice** and the
orthogonal form **once**, and the twice-spoken version is attached to a statement
that is **true** (`max compact of SU(3,2) = SU(3)xSU(2)xU(1)`, machine-verified
twice in this repo) while the once-spoken version makes the chain **impossible**.

**The mechanism-compatible transcription hypothesis.** The same speaker turn
contains:

> *"it's the maximal compact subgroup of **spin six comma spin four**"*

which names **no group at all** — the second slot of a signature is an integer,
not a group. The intended object is `Spin(6,4)`, whose maximal compact is indeed
`Spin(6) x Spin(4)`. The transcript therefore contains one demonstrably
malformed `spin X comma spin Y` frame in the same paragraph. That makes `spin
three comma two` for `s u three comma two` a plausible same-mechanism
transcription defect; it does not prove that the audio contains the latter
substitution. Audio confirmation remains the decider between an ASR defect and
a source-side slip.

Also verified in the source text, and load-bearing for what follows: *"There is no
grand unification"* (present), *"It's just a normal bundle in your ambient space"*
(present), the 10-counting of GUT groups (*"It's spin six, which is s u four,
cross spin four, six plus four, ten"*, present), *"reduce maximal compact subgroups
along the fibers"* (present), *"this has a complex structure"* (present), *"births
its own 14 dimensional ambient space"* (present — `Y^14` is endogenous, not
Kaluza-Klein), `Krein` **0 occurrences**, `ghost` **0 occurrences**, and *"I don't
know what to do because we're in a maximally compact subgroup"* (present).

---

## 2. THE BEST-SUPPORTED RECONSTRUCTION

| reading | verdict | the group theory |
|---|---|---|
| **R1** literal nesting `Spin(6,4) > Spin(3,2) > G_SM` | **KILLED** | `12 > 10`; swept over all `p+q=5` |
| **R2** commuting factors `Spin(3,2) x G_SM < Spin(6,4)` | **KILLED** | max centraliser `= 10 < 12`, exhaustive over `C^10` module structures |
| **R3** `Spin(3,2)` as the spacetime factor | **KILLED for this sentence** | spacetime slot is `Spin(1,3)`, `dim 6 < 10`; the chain's ambient is the vertical fibre |
| **R4** `Spin(3,2) ~ Sp(4,R) ~ AdS_4` in the picture | **identity TRUE, not in evidence** | brief's "3+1 conformal group" is wrong: that is `so(4,2)`, `dim 15` |
| **R5** the `(6,4)` fibre **is** `(so(3,2), B_Killing)` | **SURVIVES as structure** | unique in dim 5; adjoint embedding exists; centraliser `0`, so not a chain step |
| **R7** lossy transcription of a longer chain | **not excluded** | but any completion must still route through a `>= 12`-dimensional node, i.e. through `SU(3,2)` or `U(3,2)` |
| **R6** `Spin(6,4) > SU(3,2) > S(U(3)xU(2))` | **BEST-SUPPORTED RECONSTRUCTION** | subgroup embeddings construct fibrewise; `24 <= 45`, `12 <= 24`; intersection `12`/`13` reproduces the registered eq (4.6) extraction; global reductions remain unbuilt |

**The reconstruction, stated once.** The best-supported reading of *"the right
chain"* is
`Spin(6,4) > SU(3,2) > S(U(3)xU(2))`, and its two arrows are **not** symmetry
breakings. They are **structure-group reductions of one rank-10 bundle** — the
vertical/normal bundle of `X^4` in the space of metrics, carrying the
trace-reversed Frobenius metric of signature `(6,4)`. Arrow 1 is a
complex-structure reduction (`R^{6,4} -> C^{3,2}`); arrow 2 is a maximal-compact
(Cartan) reduction. At the algebraic/fibrewise level the three groups can be
successive structure groups of the **same** 10-dimensional object, which fits how
the source counts them
way he does — `SO(10)` is 10 real, `SU(5)` is 5 complex, Pati-Salam is `6 + 4`,
and `SU(3,2)` is `3 + 2` complex. He is not walking down a subgroup tower. He is
saying the same 10 four different ways. Promoting this pattern to a global
bundle statement requires the reduction sections and determinant data named in
the correction above.

**And that is why the GUT frame was the wrong frame all along.** *"There is no
grand unification. It's just a normal bundle in your ambient space."* The
dimension obstruction the brief handed me (`12 > 10`) is not a puzzle to be solved
by finding a cleverer nesting; it is what you get when you try to read a chain of
**reductions** as a chain of **subgroups**. The reduction chain has no
`Spin(3,2)` in it because a reduction to a real orthogonal `(3,2)` structure on a
rank-10 bundle is not one of the reductions available — `so(3,2)` acts on `R^5`,
not on `R^{10}`, except through the adjoint (R5), which centralises nothing.

**`Spin(3,2)` is therefore NOT the spacetime factor.** The brief asked what it
would constrain if it were. Answer: it would have to be, and it cannot be. The
source's spacetime factor is `Spin(1,3)` (`dim 6`), printed in eq (4.6) and
registered as `SC-GRP-03`; `so(3,2)` (`dim 10`) does not embed in it. Had
`Spin(3,2)` been the spacetime factor, GU would be committed to an AdS_4 /
3d-conformal spacetime symmetry with a cosmological constant of definite sign —
a very strong and very testable constraint. **It is not committed to that**, and
this artifact closes that door rather than opening it.

### 2.1 What is mine and what is not

| ingredient | owner |
|---|---|
| `max compact of su(3,2) = su(3)+su(2)+u(1)` | **prior art**, `tests/legs/forces_maximal_compact_is_sm.py` + an independent second method |
| "SM as maximal compact rather than breaking", typed `REDUCTION_EXTERNAL` | **prior art**, `AUDIT-noncompact-compact-reduction-EXTERNAL.md`, 2026-07-04 |
| middle node is `SU(3,2)` not `Spin(3,2)` (adjacent sentence, by dimension) | **prior art, dated today**, LA-7 §1.4 |
| `Spin(6)xSpin(4)` = Pati-Salam maximal compact | **prior art**, saturated |
| the **chain sentence** obstruction `12 > 10` | this artifact |
| exhaustive kill of the **factorisation** reading (max centraliser 10) | this artifact |
| the **frame**: reductions of a rank-10 normal bundle, not a GUT tower | this artifact |
| explicit realification embedding `SU(3,2) < Spin(6,4)` | this artifact (repo had only the commutant) |
| eq (4.6) intersection computed as `12` / `13` | this artifact |
| Killing form of `so(3,2)` is `(6,4)`, uniquely in dim 5 | this artifact |
| `Spin(3,2) ~ Sp(4,R) ~ AdS_4`, and the correction to `so(4,2)` | this artifact |
| the impossible chain sitting in `explorations/` since 2026-07-11 | this artifact |

---

## 3. THE PROPOSED REGISTER ENTRY

**I did not write this.** `lab/sources/source-claim-register.yaml` is out of scope
for this artifact. `SC-GRP-50` is free — `SC-GRP` has no 50-series at all, and the
50-block is the register's convention for spoken-edition claims. Nothing exists at
`ucsd-seminar-2025` timestamps `00:43`–`00:46`; the nearest row is `SC-GEO-58` at
`00:42:42`, one paragraph short.

```yaml
- id: SC-GRP-50
  polarity: ASSERTS
  claim: The best-supported reconstruction of the chain is Spin(6,4), then the
    (3,2)-signature unitary form, then SU(3)xSU(2)xU(1) -- offered as a reading of
    the replacement for the Spin(10) chain, whose definite Killing form the author
    says wasted the 1970s work.
  verbatim: But this is the right chain. Spin six four, spin three comma two, s u three
    cross s u two cross u one, Brian, in terms of the axis of evil in certain, Lorentz
    breaking directions in space.
  locus:
    source: ucsd-seminar-2025
    timestamp: 00:45:00
    extraction: papers/drafts/Transcript into the impossible.md:155
  grade: transcript-uncertain
  notes: '[ASR] TRANSCRIPTION-UNCERTAIN on the middle term. As transcribed the chain is
    group-theoretically impossible: dim Spin(3,2) = 10 < 12 = dim SU(3)xSU(2)xU(1), so the
    second arrow admits no injective homomorphism, and no factorisation rescues it either --
    the largest centraliser of any Spin(3,2) in Spin(6,4) is 10 (exhaustive over so(5,C)
    module structures on C^10). The middle term is read as SU(3,2) on four independent
    grounds: (i) the author says "s u three comma two" TWICE at 00:43:47, one clause earlier,
    attached to the true statement that its maximal compact is SU(3)xSU(2)xU(1); (ii) the same
    speaker turn contains the provable ASR corruption "the maximal compact subgroup of spin
    six comma spin four", which names no group -- a spurious "spin" inserted into the same
    "X comma Y" frame; (iii) draft-2021 p.29 eq (4.6) writes SU(3,2)/U(3,2) (see SC-GRP-03),
    so the registered written-edition extraction corroborates across four years (the PDF is
    absent from this checkout); (iv) with SU(3,2) both subgroup embeddings are constructible
    fibrewise -- SU(3,2) < Spin(6,4) by realification of a Hermitian (3,2) form, and
    S(U(3)xU(2)) < SU(3,2) as the maximal compact, dims 24 <= 45 and 12 <= 24. The two arrows
    model STRUCTURE-GROUP REDUCTIONS of the rank-10 vertical bundle, not symmetry breakings;
    the global reduction sections are not constructed here:
    the author denies the GUT frame outright at 00:38:09 ("There is no grand unification. It
    is just a normal bundle in your ambient space") and names the operation at 00:46:40
    ("reduce maximal compact subgroups along the fibers"). Machine-verified in
    tests/channel-swings/joe_directed_sca_right_chain.py (85/85, exit 0). NOT claimed by the
    author and NOT to be attributed to him: any mechanism for the indefinite Killing form. He
    declares it OPEN in this same passage -- "I do not know what to do because we are in a
    maximally compact subgroup", "we are shielded experimentally". "Krein" and "ghost" occur
    ZERO times in this source.'
  core: hard-core
  provenance_caveat: 'The primary_source copy lab/literature/weinstein-ucsd-2025-04-transcript.md
    had this sentence DELETED (replaced by the single word "So,") until 2026-08-15. The
    restoration follows papers/drafts/Transcript into the impossible.md on the evidence that
    the primary_source copy is an EDITED DERIVATIVE -- it normalises speech in three places
    (Stuckelberg, gauge invariance, Weyl spinors) -- and NOT on independent authority.
    CONFIRMATION AGAINST THE ACTUAL RECORDING IS STILL OWED and has not been performed. Until
    it is, this row is evidence about two text files, not about the audio. If the recording
    shows the author said "S U three comma two", the verbatim above should be corrected and
    the [ASR] note in `notes` retired; if it shows he said "spin three comma two", the
    verbatim stands and the row records a source-side slip rather than a transcription defect
    -- in EITHER case the mathematics of the notes field is unchanged, because it is the
    adjacent sentence and the registered 2021 extraction that support the reconstruction,
    not this token.'
  adherence:
    adherence: PARTIAL
    evidence:
    - lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md
    - lab/active-research/joe-directed/ledger-advancement/la7-lt-sm7-moves-t0-to-t2-and-the-lt-sm1-split-is-banked-2026-08-15.md:288-300
    - tests/legs/forces_maximal_compact_is_sm.py
    - explorations/big-swing-2026-07-03/AUDIT-noncompact-compact-reduction-EXTERNAL.md:21-25
    pinned_at: UNPINNED-propose-only
    date: '2026-08-15'
    note: PARTIAL, not ADHERED, for reasons beyond the transcription. The subgroup embeddings
      are constructible and machine-verified, but arrow 1 still needs a global compatible
      pseudo-Hermitian complex structure plus determinant data, and the non-compact -> compact
      reduction that makes step 2 happen is typed REDUCTION_EXTERNAL
      (AUDIT-noncompact-compact-reduction-EXTERNAL, 2026-07-04) -- it is the Weyl unitarian
      trick, not a GU-forced selection, and GU's native invariant form is Krein. The claim is
      carried with both datum costs named. The register
      has no `provenance_caveat` field today; if the schema is not extended, fold that block
      into `notes` verbatim rather than dropping it.
```

**Two schema notes for the register owner.** (a) `grade: transcript-uncertain` and
the `provenance_caveat` key are both **new**; the closest existing conventions are
the inline `[ASR]` and `TRANSCRIPTION-UNCERTAIN` markers in `notes` (10 and 2 uses
respectively). If the schema is not extended, `grade: transcript-verified` is
**wrong** here and the honest fallback is to keep the existing grade vocabulary and
carry both blocks inline in `notes`. (b) A companion row is worth opening at
`SC-GRP-51` for `[00:43:47]` — *"Standard model answers the question, what is the
maximal compact subgroup of s u three comma two? And that's s u three cross s u two
cross u one"* and its Pati-Salam twin. It is the **most-cited pair of sentences in
the repository** and it is unregistered, which is why the chain could be typed
neither way for a month.

---

## 4. HOSTILE REVIEW, inline

**H1 — "You are reading structure into a conversational aside."** The strongest
attack, and it is partly right. The sentence is an aside: it ends `"Brian,"` and
swerves into the CMB axis of evil, addressed to a cosmologist. Nobody delivers a
considered classification of real forms in a subordinate clause.

*What survives it.* I am not deriving the structure **from** the aside. The aside
is a **one-line summary of the two sentences before it**, which are not asides:
they state two maximal-compact facts explicitly, twice, and **both are true** and
machine-verified in this repository. The chain is the compression of an argument
he had just made at length. And the load-bearing corroborator is not spoken at
all — it is typeset in the 2021 draft at eq (4.6), registered as `SC-GRP-03`,
whose `U(1)` proviso this artifact reproduces to the integer (`12` vs `13`). An
aside that agrees with a four-year-old equation is not an aside I invented.

*What does not survive it.* R5 — the Killing-form observation — is exactly the
kind of pretty pattern that hostile review exists to catch. Nothing in the source
says "adjoint representation." I have typed it `SURVIVES AS STRUCTURE`, kept it
out of the register entry entirely, and computed its centraliser to be `0`
precisely so it cannot be quietly promoted into a chain step later. If it is ever
used, it must be used as a repository conjecture with the author's name off it.

**H2 — "You overrode the source's spoken word because the alternative was
prettier."** This is the mis-attribution failure running in the direction the
brief did not warn about, and it is the one I was actually at risk of. Mitigations,
all structural: the register `verbatim` field carries `spin three comma two`
**exactly as spoken**; the adjudication lives in `notes` where it is visibly an
inference; the `provenance_caveat` states what happens under **both** outcomes of
the audio check; and the `polarity` stays `ASSERTS` on what he said, not on what I
think he meant. If the recording says `spin`, the row still stands — it just
records a source-side slip instead of an ASR defect, and the mathematics is
unchanged either way, because the decision rests on the adjacent sentence and the
2021 draft, not on the disputed token.

**H3 — "LA-7 already did this, this morning."** Half true and I have said so
plainly in §2.1. LA-7 selected the **best-supported term** by testing the adjacent sentence
(`dim K(SU(3,2)) = 12` vs `dim K(Spin(3,2)) = 4`). It did not test the **chain**
sentence, whose obstruction is a different integer, it did not consider the
factorisation reading at all, and it did not reconstruct what **kind** of chain this
is — which is the thing the coordinator's `[00:38:09]` material makes decisive and
which changes the answer from "a GUT chain with a typo" to "not a GUT chain."

**H4 — "`REDUCTION_EXTERNAL` already makes step 2 not GU-forced, so the chain is
worth less than you are pricing it at."** Correct, and it is why the proposed
adherence is `PARTIAL` and not `ADHERED`. The counter-argument is also on record
(`curt-jaimungal-gu-iceberg-claim-reconciliation-2026-07-31.md:296-302`: every
subgroup step introduces new physics through breaking). This artifact supplies
the best-supported reconstruction of what the sentence **means**; it does not
upgrade what the sentence **buys**.

**H5 — "Your exhaustiveness claim in §1.2 rests on a representation-theory fact
you asserted."** Fair, and it is why the `C_2` irrep list is **computed** from the
Weyl dimension formula over `a, b in [0,12)` rather than quoted, and the
Frobenius-Schur types from the central character `(-1)^a`. The complexification
step is the real load-bearing move, and it is stated as a proof in the module
docstring rather than waved at: the centraliser is a real linear system, so its
complexification is the complex centraliser, so the enumeration is signature-blind.

**H6 — "You claim `Spin(3,2)` is absent from `lab/sources/` — did you check, or
did you trust the apparatus?"** I checked, and the apparatus is **wrong in one
third**. `lab/sources/` and `canon/` are indeed 0 hits. `explorations/` is not:
`H19-...:114` and `:157` carry the impossible chain. Trusting today's apparatus
note would have let me report a clean slate where there is a propagated defect.

---

## 5. POSTFLIGHT

**Lens 1 — arithmetic discipline.** Every dimension is built from an explicit
integer basis and bracket-checked before it is read; every signature is an exact
congruence, power-tested on the zero-diagonal path that breaks naive
implementations; `assert_no_float` sweeps the result structure. The one place a
float could have entered — the Weyl dimension formula — returns a `Fraction` whose
denominator is asserted to be 1 before it is cast. **Clean.**

**Lens 2 — control discipline.** Positive controls run first (10 of them). Two
planted failing controls in the enumeration (`5+4+1` odd symplectic multiplicity;
`1^10` unfaithful), one planted failing control in the intersection block
(`so(3,2) n Pati-Salam = 4 < 12`), one planted failing textual control (the
`spin six comma spin four` garble), and **one contrary control that must pass** —
`Spin(3,2) x Spin(3,2) < Spin(6,4)`, accepted by the same predicate that rejects
`Spin(3,2) x G_SM`, and then exhibited explicitly with commuting brackets verified.
The two cases differ **only** in the second factor, so the discrimination is
sharp. `--selftest` plants 4 false facts; each forces exit 1; the clean run exits
0. **Clean.**

**Lens 3 — attribution auditor.** Checked in both directions. *Source → repo:* the
chain, the maximal-compact statements, the normal-bundle denial, the fibre
reduction, and the complex structure are all quoted verbatim with timestamps and
verified by exact substring match in the test. *Repo → source:* `Krein` = 0,
`ghost` = 0, verified in the test and stated in the register `notes`; the
indefinite-Killing-form problem is recorded as the author's **declared open
problem** in his own words; `Y^14` is endogenous, not Kaluza-Klein. The AdS/
conformal reading is explicitly typed **not in evidence** rather than being
quietly used. **Clean.**

**Lens 4 — novelty auditor.** Retrieval ran before the work, not before the
novelty sentence, and it demoted two things I would otherwise have claimed
(§0.1). §2.1 is an explicit ownership table. The two loudest-sounding results here
— "SM is a maximal compact" and "the middle node is `SU(3,2)`" — are **both**
credited to prior art, one from July and one from this morning. **Clean.**

**Lens 5 — gate and convention auditor.** `doc_type: construction_result`
(honest — this is a computation, and the dodge the brief named was declining it).
`target_claim` uses the internal-target form with `target_claim_verdict`, and
contains **no** `SC-[A-Z]+-\d+` pattern, so `kill_target_claim_audit.py` routes it
to `internal_targets` rather than looking up a register id that does not exist
yet. The `GU-COMPARATOR-ROUTING` notice is verbatim and the
``Classification: `SOURCE_NATIVE_ROUTE` `` line matches the prose. The registry
consequence is **measured, not assumed**: the routing audit was already red at 10
against baseline 9 before this file existed, and this file takes it to 11.
`kill_target_claim_audit.py` runs green (3 red = baseline 3; internal-target
kills 4, this file included). **Clean, with one owed registry row.**

**Lens 6 — propagation auditor: what does this break?** Three live sites carry the
killed chain and each needs a different disposition, none of which this artifact
may perform. `H19-...:114` and `:157` state it as *"Weinstein's own SM chain"* —
that attribution is wrong as written and should become `SU(3,2)`; H19's conclusion
is **unaffected**, because its argument is that the `(6,4)` fibre is common to
`(9,5)` and `(7,7)`, and the fibre is what it always was. `la6-...:918` uses the
chain for a **rank drop from 3 to 2**, which LA-7 has already re-derived on the
correct node (`S(U(3)xU(2))`, `rank pi_3 = 2`), so that conclusion also survives
the correction. `transcript-concordance-...:53` carries both readings in one
sentence and simply needs the reconciliation this artifact supplies. **No
downstream result is destroyed; three attributions are wrong.**

**Lens 7 — what would change my mind.** (a) The recording saying `spin` clearly and
the 2021 draft's eq (4.6) turning out to print something other than `SU(3,2)`/
`U(3,2)` — then the sentence would be a source-side error and the register row
should say so. (b) A rank-10 real bundle reduction to a genuinely `so(3,2)`
structure that I have missed — but the centraliser enumeration is exhaustive over
`C^10`, so this would require an error in that enumeration, which is the single
most attackable computation here. (c) Evidence that `"Brian,"` terminates the chain
**before** the third term, making it a two-term chain `Spin(6,4) > SU(3,2)` with
`SU(3)xSU(2)xU(1)` a separate remark — this would not change any group theory but
would weaken the register row's `claim` field to two terms.

---

## 6. CERTIFICATE

```text
tests/channel-swings/joe_directed_sca_right_chain.py
  85/85 checks PASS, exit 0
  --selftest: 4/4 planted false facts each force exit 1; clean run exits 0
      dim_so32     dim so(3,2) forced to 12  -> would resurrect R1
      max_cent     max centraliser forced to 12 -> would resurrect R2
      killing_sig  Killing signature forced to (4,6) -> would break the fibre match
      n_su32       the twice-spoken "s u three comma two" forced to 0 occurrences

  exact arithmetic only: integer matrices + fractions.Fraction
  assert_no_float sweeps the entire RESULT structure -- clean

  load-bearing integers
      dim so(3,2)                            = 10
      dim su(3) + su(2) + u(1)               = 12      -> R1 KILLED
      max centraliser of so(5,C) in so(10,C) = 10      -> R2 KILLED
      dim so(1,3)                            =  6      -> R3 KILLED
      dim so(4,2)  [the 3+1 conformal alg]   = 15      -> brief corrected
      Killing signature of so(3,2)           = (6,4)   -> R5 structure
      dim su(3,2) / u(3,2) / so(6,4)         = 24 / 25 / 45
      so(6)+so(4) n su(3,2)                  = 12      -> eq (4.6) computed
      so(6)+so(4) n  u(3,2)                  = 13      -> "up to a U(1)"
      so(6)+so(4) n so(3,2)                  =  4      -> planted control
```
