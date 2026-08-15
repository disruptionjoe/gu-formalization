---
artifact_type: exploration
status: exploration
doc_type: ledger-delta
created: 2026-08-15
work_item: LA-8
channel: conditional_ledger_advancement
base_revision: a148ed80
ledger_base: lab/process/conditional-physics-ledger-v0.258.json
axis: REPRESENTATION
rows: [RA-E2, RA-E1, RA-E3, RA-E4]
delta_kind: VERSIONLESS_DELTA__NOT_A_LEDGER_EDIT
target_claim: "CB-A:E2 -- the repo-internal derived shape constraint 'in an adjoint-valued one-form Omega^1(Y,ad) the Lorentz-scalar components are exactly those with both legs vertical: V*_10 (x) Lambda^2 V_10 = 10 (x) 45, which hosts 6 (1,2,+1/2) and 6 (1,2,-1/2)'. NOT a Weinstein source claim; the source supplies neither the sector nor the count."
canonical_effect: pending_integration
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
title: "LA-8: RA-E2's shape constraint is refuted at the FORM leg, which is the settled leg, so MD-1's open SOLDERED-AD fork is NOT load-bearing for this row -- the vertical form leg's Lorentz-trivial component is 1, not 10, so CB-A:E2's 10 (x) 45 sector is 45-dimensional (INERT-AD) or exactly 1-dimensional (SOLDERED-AD, dim Inv_so(3,1)(V (x) Lambda^2 V) = 1), and hosts 0 + 0 colour-singlet weak doublets on BOTH horns instead of the printed 6 + 6. The named adapter is built, not missing: RA-E2 is DIFFERS/STRUCTURAL_DIFFERENCE, not NEEDS/MISSING_CONSTRUCTION. The packet's live res_s^V route is FORCED through the same 1-dimensional trace line, so owning it does not restore the count. RA-E4 prints the same refuted sector (12 of its 18 doublets) but its DIFFERS survives; RA-E3's revival trigger is unfireable through observation; RA-E1 inherits the shape premise underneath its own rank-196/rank-0 compatibility failure."
grade: "EXACT throughout: fractions.Fraction / integer linear algebra over Q, exact sympy symbolic differentiation against a general metric section, and one nullity bounded by INTEGER arithmetic mod two primes (rank_p <= rank_Q, so nullity_Q <= nullity_p) with a matching hand-constructed exact Fraction witness for the lower bound. No float is load-bearing anywhere; assert_no_float sweeps the result dict. 78/78, exit 0, via tests/channel-swings/joe_directed_ledger_rae2_form_leg_typing.py. Certificate splits as 12 [L] ledger reproductions, 12 [S] exact source substrings, 7 [A] source-native symbolic results, 8 [B] Lorentz-typing results, 13 [C] comparator branching results, 10 [D] soldered-horn results, 16 [E] E-block incidence results, of which 10 are controls that MUST fire. The harness independently reproduces three numbers CB-A printed by hand -- E1's 1+1, E3's 0, E2's 6+6 -- before it corrects the fourth. NOT: a source action, a vacuum, a Higgs mechanism verdict, a decision of SOLDERED-AD, a statement about the spinor sector, a statement about composites, a ledger edit, or any claim-status movement."
disposition: FORM_LEG_REFUTES_THE_SHAPE_CONSTRAINT__TRIVIAL_COMPONENT_1_NOT_10__ZERO_DOUBLETS_ON_BOTH_FORK_HORNS__SOLDERED_AD_NOT_LOAD_BEARING_FOR_THIS_ROW__ADAPTER_BUILT_NOT_MISSING__EQUIVARIANT_PROJECTOR_FORCED_THROUGH_THE_TRACE_LINE__RA_E2_NEVER_MIGRATED_IN_258_VERSIONS_AND_IS_IN_NO_WORK_QUEUE__ROUTING_METHOD_ASSERTS_THE_REFUTED_STEP_AT_ITS_OWN_LINE_62
rows_assessed:
  retyping_proposed:
    - RA-E2
  premise_inheritance_checked:
    - RA-E1
    - RA-E3
    - RA-E4
  verdict_confirmed_not_moved:
    - RA-E3
    - RA-E4
  escalated:
    - RA-E2
  seam_flagged_offaxis:
    - lab/methods/source-native-comparator-routing.md
depends_on:
  - lab/process/conditional-physics-ledger-v0.258.json
  - lab/methods/source-native-comparator-routing.md
  - lab/process/source-native-comparator-routing-registry.json
  - explorations/conditional-build/cb-a-representation-content-2026-08-05.md
  - lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md
  - explorations/unified-source-datum-packet-v0-2026-07-30.md
  - lab/active-research/joe-directed/ledger-advancement/la4-representation-axis-has-13-grants-and-a-one-vertex-cut-2026-08-15.md
  - papers/drafts/Transcript into the impossible.md
  - lab/process/perspective-passes/01-foundational-math-lenses/08-higher-dim-kk.md
scripts:
  - tests/channel-swings/joe_directed_ledger_rae2_form_leg_typing.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
> Classification: **`BRIDGE_OR_SEMANTIC_BOUNDARY`.**
>
> Internal routing of this artifact, stated once so it cannot be flattened:
> **§3.1 (the contraction) is `SOURCE_NATIVE`.** **§3.2–§3.4 (the SO(10)→SM
> branching and the Kaluza-Klein projection reading) are `CONVENTIONAL_COMPARATOR`
> and bind only the disavowed KK route** — they are used to correct a number
> `CB-A:E2` itself computed inside that comparator, never to adjudicate a
> source-native object. Report their content as `CONVENTIONAL_ROUTE_EXCLUDED`.

# LA-8 — RA-E2 fails at the settled leg, so the open fork does not protect it

## Result first

**`RA-E2` is mis-typed, and the defect is real, not vocabulary.** The row is
filed `NEEDS / MISSING_CONSTRUCTION`, `mapping_grade: EXACT_SHAPE_CONSTRAINT`,
`distance: use and propagate the vertical form leg through observation`. Three
things are wrong with that, each exactly certified:

1. **The construction is not missing.** The adapter the row names —
   propagation of the vertical form leg through observation — is built, twice
   (`unified-source-datum-packet-v0-2026-07-30.md:128`, five days before CB-A
   wrote the row; and MD-1, 2026-08-14, 67/67). Re-derived here symbolically
   against a general metric section: `s^*` is surjective onto `T*X` with a
   10-dimensional kernel, and it returns a 4D **one-form**.
2. **The shape constraint is not exact; it is wrong by a factor of ten.**
   `CB-A:E2`'s form-leg factor is the full `10`. The Lorentz-trivial component
   of `Sym^2(T*X4)` is **1**, computed here as an exact rational nullspace, with
   a control that fires at `10` for a genuinely inert internal space.
3. **The `SOLDERED-AD` fork is not load-bearing for this row.** LA-4 escalated
   rather than adjudicated because MD-1 leaves that fork open. But `CB-A:E2`'s
   `10` lives on the **form** leg, and the form leg's Lorentz typing is forced
   by `Y14 = Met(X4)` alone — it is *not* the fork, which is about the **ad**
   leg. Running both horns to the end:

```text
                                  Lorentz-scalar    colour-singlet weak
                                  dimension          doublets hosted
  CB-A:E2 as printed              10 x 45 = 450      6 (+) 6   = 12
  corrected, INERT-AD horn         1 x 45 =  45      0 (+) 0   =  0
  corrected, SOLDERED-AD horn      exactly     1      0         =  0
```

  `dim Inv_so(3,1)( V (x) Lambda^2 V ) = 1` exactly (mod-`46337` and mod-`40961`
  upper bound, exact `Fraction` witness lower bound; control returns `45` when
  the ad leg is made inert). One real direction cannot carry a complex weak
  doublet, whose real dof `CB-A:E4` itself puts at `4`.

**Both horns of the open fork give zero.** That is the whole reason this row can
be adjudicated today when LA-4 could not adjudicate it yesterday.

**Proposed migration: `NEEDS / MISSING_CONSTRUCTION` → `DIFFERS /
STRUCTURAL_DIFFERENCE`.** Full field text at §6.

**E-block verdict: the premise is shared but no other verdict moves.** `RA-E4`
prints the same refuted sector and loses 12 of its 18 doublets, yet stays
`DIFFERS` on its remaining even channel. `RA-E3`'s exclusion theorem is
*confirmed* by the same computation, while its revival trigger becomes
unfireable through observation. `RA-E1` inherits the shape premise underneath a
different and prior blocker.

---

## 0. PREFLIGHT — six specialist lenses, run inline, work list re-derived

### Lens P1 — ledger archivist: re-derive the work list from v0.258 itself

Re-derived from `rows`, not inherited from the brief. Findings, all certified
`[L1]`–`[L12c]`:

| brief said | v0.258 says | delta |
|---|---|---|
| `RA-E2` "has not migrated since v0.174" | **`RA-E2` has never migrated at all.** Zero of the **244** recorded migrations names it, and its row record is byte-identical across **all 258** ledger files, `v0.1` through `v0.258` | the true statement is strictly stronger. **Correction to LA-4 §2.1.** Control: the same test on `RA-E1` finds **42** distinct records |
| `md1-form-leg` occurs zero times in the ledger | confirmed; `four-d-mode-decomposition` also occurs zero times | — |
| — | **`RA-E2` appears in no rank of `next_work_queue`**, while `RA-E1`, `RA-E3`, `RA-E4`, `RA-E5` are all rank 1 | new. The one E-row whose route is refuted is also the one nobody is scheduled to touch |

What moved since LA-4 was banked (07:30 today): `la5` and `la6` landed, and the
channel README was rewritten. Neither mentions `RA-E2`; neither cites MD-1. The
ledger head is unchanged at `v0.258`/`a148ed80`. **Nothing in my work list
moved.** MD-1 is cited by exactly two artifacts in the repository:
`lab/methods/source-native-comparator-routing.md` and LA-4.

### Lens P2 — routing officer: decide MD-1's status BEFORE using it

Route proposed: settle §5 of the brief before touching physics, because if MD-1
is comparator-typed I may not discharge a source-native row with it absent a
six-item typed bridge. Three independent tests, run before computing:

1. **The method document itself names MD-1 as a source-native pointer.**
   `source-native-comparator-routing.md:89` lists
   `md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md` under fork 3's
   *"Read first"* block. The document's own "Required artifact notice" defines
   those blocks as the *"source-native pointers"* an agent must follow before
   reusing a comparator result. That is a routing determination by the method's
   author, at the same date, and it is decisive.
2. **The registry does not contradict it; it does not reach it.** MD-1 is not
   among the registry's 32 entries, and it should not be: the audit's
   `discovered_artifacts()` enumerates seven `joe-directed` channel tokens and
   `four-d-mode-decomposition` is not one of them. Silence from an audit whose
   discovery set excludes the file is not a classification. *(Coverage gap
   recorded at §5; not actionable from this channel — the audit asserts registry
   equality, so adding MD-1 would fail it, and neither file is writable here.)*
3. **MD-1's own load-bearing content is source-native, and it fences its one
   comparator step explicitly.** Its map is the observation pullback `s^*`,
   source-confirmed via `g3-weinstein-section-pullback-recheck-2026-07-31.md`
   and `selected-k77-h640-*` (`SOURCE_CONFIRMS_Y14_OPERATOR_AND_OBSERVATION_PULLBACK`);
   its Lens 1 *rejects* the KK comparator on source grounds before running; and
   its imported-assumption 5 declares the KK-style projection step used "*only*
   to compute what the disavowed map would give," labelled and not used for any
   conclusion about GU.

**Verdict: MD-1 is `SOURCE_NATIVE_ROUTE` on its form-leg result and carries one
declared, fenced `CONVENTIONAL_COMPARATOR` sub-computation.** No bridge is owed,
for a reason worth stating precisely: I never transport a comparator failure
onto a source-native object. The source-native route is closed by a source-native
computation (§3.1), and the comparator number is used only to correct
`CB-A:E2`'s own comparator number (§3.2), which is legal in both directions
because both sides of that correction sit inside the same disavowed KK reading.

**Cheapest kill-or-switch:** had the routing document classified MD-1 as a
comparator, or had the registry typed it `CONVENTIONAL_COMPARATOR`, I would have
been limited to §3.1 alone — which, note, still refutes the row, because §3.1 is
the source-native half.

### Lens P3 — representation theorist: where does the `10` actually live?

Route proposed: do not argue about adapters; audit the number. `CB-A:E2` writes
the sector as `V*_10 (x) Lambda^2 V_10`. The first factor is the **vertical form
leg**; the second is the **ad** leg. Since `Y14 = Met(X4)`, the vertical fibre is
`Sym^2(T*X4)`, so the physical Lorentz group acts on the first factor by `Sym^2`
of the vector representation — *by functoriality of `Met`, with no assumption
about `P_H`*. Compute the trivial isotypic component. **This is the decisive
route and it is fork-free.** **Cheapest kill-or-switch:** if the trivial
component is `10`, the row's arithmetic stands and MD-1 is irrelevant to it; if
it is `1`, the row's printed count is wrong by construction. **Contrary route:**
deny `Y14 = Met(X4)` — the only escape, and it is repo canon plus source-supported.

### Lens P4 — bundle geometer: is the row's own map even the map MD-1 computed?

Route proposed: the brief allows the row to survive if the adapter it names is
not the one MD-1 computed. Test it textually and then structurally. The row's
`distance` says *"through observation"* and its `revival_trigger` asks for a
*"14D-to-4D vertical-scalar adapter"*. MD-1 computes exactly the observation map.
So the row does not survive on that escape. **But** the 2026-07-30 packet names a
*different* live object — `res_s^V(A - A_0)` followed by a *declared trace/orbit
projector* — which is a coefficient restriction, not a differential-form
pullback, and is genuinely unowned. **Cheapest kill-or-switch:** run that live
object to the end and see whether it restores the count. It does not, and the
reason is forcing rather than contingent — see `[B7]`.

### Lens P5 — source-fidelity reader: what does the declared content actually offer as a 4D scalar?

Route proposed: refuse to supply field content and read what is declared. The
transcript declares *"zero forms and one forms valued either in add or in the
spinners, and that's it"* (`Transcript into the impossible.md:173`). So there
**is** a genuine 4D-scalar channel that the row never considers: an ad-valued
**zero**-form pulls back under `s^*` to an honest 4D scalar. Compute its Higgs
content on both horns. **Cheapest kill-or-switch:** if that channel hosts a
doublet, the row is repairable by retargeting rather than retyping. It does not
— `[E14]`, `[E15]`. **Contrary route:** the *nonlinear* or *composite* content may
exceed the linearized declaration; this artifact does not reach it, and says so
in the ceiling.

### Lens P6 — honesty auditor: pre-register the failure modes

Three pre-registered, before computing:

1. **Laundering a grant.** The result must not quietly promote
   `SECTION-VS-OBSERVERSE` or `CARRIER-SPLIT` from grant to derivation.
   Pre-commitment: state at §7 exactly which grants are load-bearing and show
   that `CB-A:E2` needs the *same* ones — a shared grant is not a differential
   grant. Also pre-committed: `VERTICAL-FROBENIUS-TRACE` must **not** appear,
   because the endogenous `Sym^2` action needs no fibre metric; if it appears in
   the derivation, the derivation is wrong.
2. **Quoting one horn of an open fork as the result** — MD-1's own named
   overclaim. Pre-commitment: compute *both* horns to a number and report the
   row as adjudicated only if they agree.
3. **The forbidden summary.** "GU has no Higgs" / "the GU Higgs mechanism is
   excluded" are forbidden sentences under the routing method's summary grammar.
   Pre-commitment: the allowed sentence names the sector and the reduction and
   stops there. Checked at §5.

---

## 1. PRIOR ART — what exists, and what is attributed

| prior result | where | relation to LA-8 |
|---|---|---|
| the vertical scalar is **not** `s^*(a_V)`, which "is zero or an `X`-one-form" | `explorations/unified-source-datum-packet-v0-2026-07-30.md:128`, Layer-0 register, five days before CB-A | **first statement of the typing.** Full credit. LA-8 adds only that its "live" object is *forced* through a 1-dimensional line |
| the reduction is a **contraction, not a projection**; `s^*` surjective onto `T*X`; kernel 10-dimensional; those ten "do not become 4D scalars" | MD-1 §2 (`E1`,`E2`,`E3`,`F4`,`F4b`), 67/67 | **the computational result.** Full credit. LA-8 re-derives `E1/E2/E3/F4/F4b` and control `E4` independently in sympy as `[A1]`–`[A7c]` and reproduces every one |
| `Sym^2(T*X4)`'s Lorentz-trivial component is **1**, control fires at **10** | MD-1 `B11`/`B12` | **the decisive number.** Full credit. LA-8 re-derives it as an exact rational nullspace `[B1]`, adds `[B2]` (the line is `eta`), `[B3]` (the 9 has no trivial), and a second firing control `[B5c]` |
| `SOLDERED-AD` vs `INERT-AD` named and left open; ad-leg verdict `NOT-DETERMINED` | MD-1 `fork_declared` | **respected.** LA-8 does **not** decide it. LA-8's contribution is showing it is *not load-bearing for this row* |
| the author-stated Layer-0 correction WG-B06, *"the relevant map is a contraction, not a projection"* | `O 01:34:49`, via MD-1 Lens 2 | the source warrant. Not re-claimed |
| `Y14 = Met(X4)` is **not** a KK compactification | `perspective-passes/01-foundational-math-lenses/08-higher-dim-kk.md` | independent geometric block on the same comparator. Not re-claimed |
| `RA-E2`'s route is refuted by two uncited artifacts; the row should migrate `distance` + `mapping_grade` and carry `SOLDERED-AD`; `RA-E1/E3/E4` should be checked against MD-1 in the same pass | **LA-4 §2.1**, today, 37/37 | **LA-4 owns the escalation and the framing.** LA-8 executes it, and goes past it in exactly three places: (i) the row's **verdict and reason kind**, not only its distance, are wrong; (ii) the fork LA-4 deferred to is **not load-bearing**, because both horns give zero; (iii) `RA-E2` has **never** migrated, not "not since v0.174" |
| `Lambda^2 V_10` (45) and `Sym^2 V_10` (1+54) contain **zero** colour-singlet weak doublets at any `Y` | **CB-A:E3**, and banked as `RA-E3` `EXACT_CLASS_EXCLUSION` | **used as a banked theorem, and independently reproduced** `[C6]`. The corrected count leans on CB-A's own result, not on an import |
| `10 (x) 45` hosts 6 + 6; the 10 hosts 1 + 1 | **CB-A:E2**, **CB-A:E1** | reproduced exactly `[C5]`,`[C7]`,`[C8]` from one declared branching table **before** the table is used to correct anything. Harness validation, not a new claim |

Nothing above is re-claimed. New in LA-8: (i) the fork-independence of the
refutation, with both horns computed to a number; (ii)
`dim Inv_so(3,1)(V (x) Lambda^2 V) = 1`; (iii) the forcing statement `[B7]` that
any equivariant vertical-scalar projector factors through the trace line; (iv)
the ad-valued **zero**-form channel and its zero count on both horns; (v) the
proposed verdict/reason-kind retyping; (vi) the ledger facts at §0/P1; (vii) the
routing-method seam at §5.

---

## 2. THE OBJECT UNDER TEST

`CB-A:E2` (`cb-a-representation-content-2026-08-05.md:407`), verbatim, and this
is the target claim:

> in an adjoint-valued one-form `Ω¹(Y, ad)`, the Lorentz-scalar components are
> exactly those with **both** legs vertical: `V*₁₀ ⊗ Λ²V₁₀ = 10 ⊗ 45`, which
> hosts **6** `(1,2,+1/2)` and 6 `(1,2,−1/2)` (computed). Any component with a
> spacetime form leg is a **vector**, not a scalar

The last sentence is right and is not under test. The first is under test, and
it decomposes into two separable assertions:

- **(i) form-leg assertion.** A form leg lying in the vertical `V*_10` yields a
  4D Lorentz **scalar**, with all ten directions counting.
- **(ii) ad-leg assertion.** The ad factor contributes the full `45` with its
  SO(10)→SM branching intact.

Assertion (i) sits on the **form** leg, which MD-1 settles. Assertion (ii) sits
on the **ad** leg, which MD-1 leaves `NOT-DETERMINED`. The row fails on (i).

---

## 3. THE SWING

### 3.1 The source-native half: observation returns a one-form  `[SOURCE_NATIVE]`

The observation section is `s: X4 -> Y14`, `s(x) = (x, g_ab(x))`. Symbolically,
against a general `g_ab(x)` (sympy, exact):

```text
ds(d_mu) = d_mu + (d_mu g_ab) d/d(g_ab)                    rank 4        [A1]
(s^* omega)_mu = omega_mu + omega_(ab) d_mu g_ab                         [A2]
s^* is surjective onto T*X                                 rank 4        [A3]
dim ker(s^*) on the 14 form legs                                 = 10    [A4]
s^* o horizontal-inclusion = id_4                                        [A5]
at d_mu g = 0, s^* equals horizontal projection                          [A6]
CONTROL FIRES: for a general section it does NOT                         [A7c]
```

`[A2]` is MD-1's `E2` re-derived from scratch; `[A7c]` is MD-1's control `E4`.
Consequence, and it is the source-native statement of this artifact:

> **Under the source-declared reduction there is no "both legs vertical → 4D
> scalar" channel at all.** Vertical form legs are *contracted into* the same 4D
> one-form, weighted by `d_mu g_ab`; the 10-dimensional kernel is not read by
> observation. The route `RA-E2`'s `distance` prescribes has been executed and
> returns a one-form.

Nothing in §3.1 uses a comparator, a Higgs, an SO(10) branching or a fork horn.

### 3.2 The comparator half: even the disavowed projection gives 1, not 10  `[CONVENTIONAL_COMPARATOR]`

Grant the disavowed KK projection anyway, because that is the reading in which
`CB-A:E2`'s own number was computed. Then the question is the Lorentz-trivial
content of the vertical fibre. Exact rational nullspaces:

```text
dim Inv_so(3,1)( Sym^2 T*X4 )                                    = 1     [B1]
   the invariant line is spanned by eta itself                          [B2]
dim Inv_so(3,1)( traceless 9 )                                   = 0     [B3]
CONTROL FIRES: a Lorentz-INERT internal 10 gives                 = 10    [B4c]
CONTROL FIRES: under so(3) alone the routine finds               = 2     [B5c]
```

`[B4c]` is MD-1's control `B12`. `[B5c]` is new and answers a different worry:
that the routine simply cannot find invariant spaces larger than one. It can.

This is fork-free. The Lorentz action on the vertical fibre is *functoriality of
`Met`* — it follows from `Y14 = Met(X4)` and nothing else. `SOLDERED-AD` asks
whether `ad(P_H)` is soldered; it does not ask whether `T*Y` is.

### 3.3 The count, reproduced and then corrected  `[CONVENTIONAL_COMPARATOR]`

One declared SO(10)→SM branching table, certified three ways before use
(dimension sums `[C1]`–`[C3]`, vanishing hypercharge traces `[C4]`, and
reproduction of CB-A's independently printed numbers):

```text
REPRODUCTIONS OF CB-A                                       printed   here
  10  hosts (1,2,+1/2) and (1,2,-1/2)          CB-A:E1        1,1     1,1   [C5]
  45 and 55 host colour-singlet weak doublets  CB-A:E3        0       0     [C6]
  10 (x) 45 hosts (1,2,+1/2), (1,2,-1/2)       CB-A:E2        6,6     6,6   [C7]
  the same sector's multiplicity               CB-A:E4        12      12    [C8]

CORRECTION
  Lorentz-scalar block, INERT-AD horn      1 (x) 45 = 45 dim; doublets 0,0  [C11]
  doublets deleted, not relabelled                                   12     [C12]
  block dimension: printed 450, corrected 45                                [C13]
```

The corrected count is `0` for a reason that is *CB-A's own banked theorem*: the
Lorentz-trivial form-leg factor is an SM-inert line, so the block's SM content is
the SM content of the `45` alone, and `RA-E3` already books that at zero.

### 3.4 The soldered horn, run to a number  `[CONVENTIONAL_COMPARATOR]`

Under `SOLDERED-AD` the ad factor is `Lambda^2` of the *same* endogenous 10, so
the diagonal Lorentz action must be used on both legs:

```text
dim Inv_so(3,1)( Lambda^2 V )                                    = 0     [D1]
nullity of the 450-dim stacked operator over GF(46337), GF(40961)= 1     [D3]
   (rank_p <= rank_Q, so nullity over Q is at most 1)
exact Fraction witness, annihilated by all six generators, nonzero       [D4,D5]
=> dim Inv_so(3,1)( V (x) Lambda^2 V )                           = 1     [D6]
CONTROL FIRES: with an inert ad leg the same routine returns     = 45    [D7c]
one direction < 4 real dof of a complex doublet (CB-A:E4's own arithmetic)[D8]
```

So the most generous soldered reading leaves **exactly one** Lorentz-scalar
direction in the entire 450, and it cannot be a weak doublet.

### 3.5 The packet's live route does not restore the count — and this is forced

LA-4 correctly identified the live object as `res_s^V(A - A_0)` followed by *"a
declared trace/orbit projector"*, and correctly called it unowned. Owning it
does not help, and the reason is structural rather than contingent:

> `res_s^V` returns, per ad direction, an element of `Sym^2(T*X4)`, which under
> the physical Lorentz group is `9 + 1`. Any **equivariant** projector onto 4D
> scalars annihilates the traceless `9` (`[B3]`: it has no trivial subrep) and
> therefore **factors through the unique 1-dimensional trace line** (`[B1]`,
> `[B2]`). `[B7]`

So the packet's declared *trace* projector lands precisely on the corrected
block of §3.3, with zero doublets. An *orbit* projector escapes this only by
being non-equivariant — in which case its output is not a Lorentz scalar and the
row's requirement is not met by definition.

### 3.6 The channel the row never considered

The source declares the linearized content as *"zero forms and one forms valued
either in add or in the spinners"*. A **zero**-form valued in ad does pull back
to an honest 4D scalar. Its Higgs content:

```text
INERT-AD horn:    4D scalar valued in the 45; colour-singlet weak doublets = 0  [E14]
SOLDERED-AD horn: Lorentz-scalar directions inside the 45                  = 0  [E15]
```

Both horns, zero. This is the constructive part of the finding: it tells the row
where the source-declared scalar channel actually is, and that it is empty of the
target object — which is a far more useful `distance` than "use and propagate the
vertical form leg."

### 3.7 The typing

| | filed | correct |
|---|---|---|
| verdict | `NEEDS` | **`DIFFERS`** |
| reason kind | `MISSING_CONSTRUCTION` | **`STRUCTURAL_DIFFERENCE`** |
| grade | `EXACT_SHAPE_CONSTRAINT` | the shape constraint is exact and **refuted** |

`MISSING_CONSTRUCTION` is false as filed: the construction exists. `DIFFERS`
because GU, on its own declared reduction, *determines something* here — it
determines that the vertical form leg does not descend to 4D scalars — and that
determination differs from what the SM requirement needs. `STRUCTURAL_DIFFERENCE`
rather than `ROUTE_KILLED` because the row's underlying requirement (a Lorentz
scalar) is not itself killed; only the named carrier is excluded, and §3.6 names
a live successor question. The canonical owner may reasonably prefer
`DIFFERS / ROUTE_KILLED` if the row is read as owning the adapter rather than the
requirement; that alternative is named here and not silently foreclosed.

`PROVEN_UNSUPPLYABLE` and `PROVEN_UNABLE_BY_CURRENT_ACTION` are both **refused**:
MD-1 explicitly leaves open whether the 10-dimensional `s^*`-kernel reappears as
independent 4D fields once the action and the section's own equation of motion
are supplied, and this artifact computes no action.

---

## 4. E-BLOCK INHERITANCE

The refuted sector is printed in **exactly two** CB-A rows — `E2` and `E4`
(`[E2]`, with `[E3c]` firing to confirm it is in none of E1/E3/E5/E6/E7).

**`RA-E4` — inherits quantitatively; verdict survives.** `CB-A:E4`'s inventory is
`V₁₀ → 2`, `Sym²(S) → 4`, `10⊗45 → 12`, total 18. The correction deletes the 12,
i.e. **two thirds** `[E9]`,`[E10]`. Worse for the row's bookkeeping: three of the
six `(1,2,+1/2)` in `10⊗45` are exactly `V₁₀`'s doublet paired with an SM singlet
of the `45` `[E13]` — so the "`V₁₀ → 2`" entry is partly a *subcount* of the 12,
not an independent carrier, and `CB-A:E4` is summing over three carriers with
three different Lorentz typings without typing any of them. Even in the worst
case, where only the spinor-bilinear `Sym²(S) → 4` survives, `4` is still even
and `>= 2`, so **`RA-E4`'s `DIFFERS(multi-doublet forced)` verdict stands**
`[E11]`. Its `distance` should record that its own inventory has lost its largest
term and now rests on a single carrier.

**`RA-E3` — verdict *confirmed*; revival trigger becomes unfireable.** The same
branching that corrects E2 reproduces E3's exclusion exactly `[C6]`,`[E12]`: the
`45` and the `55` host zero doublets. Nothing weakens. But `RA-E3`'s
`revival_trigger` reads *"a selected varpi one-form cell whose sigma_epsilon
image descends to an **observed 4D scalar doublet**"* `[E4]`, and §3.1 types the
observed image of a one-form cell as a 4D **one-form** `[E5]`. That trigger is
therefore unfireable through observation as written — a distinct failure mode
from LA-4's six triggers that quantify over the empty set: this one quantifies
over a non-empty set of objects of the wrong Lorentz type.

**`RA-E1` — inherits the premise, underneath a prior and different blocker.**
`RA-E1`'s live `distance` is a rank-196 observed holonomic image against a rank-0
fixed-bank principal projection `[E6]` — LA-4's characterisation of that as a
*compatibility* failure rather than a *search* failure is not disturbed here and
is not re-derived here. The inheritance is that `RA-E1`'s connection-sector offer
is a doublet in `V₁₀`, which is a **Higgs** only if the vertical form leg carries
a Lorentz scalar. So `RA-E1` is now two-deep: repair the action compatibility,
**and** supply a scalar channel that observation does not supply. Its
`Sym²(S) = 10 ⊕ 126` offer is the spinor-bilinear sector, which this artifact does
not touch.

**`RA-E5`, `RA-E6`, `RA-E7` — not assessed.** E5's doublet-triplet statement
rides on `V₁₀`'s internal structure and inherits the same open question; E7's
channel is the spinor `10`. Neither is in scope and neither is claimed.

**The E-block verdict.** The premise is genuinely shared, and it is genuinely
refuted — but **no verdict other than `RA-E2`'s moves, and none moves toward
`SAME`.** The correction deletes channels; deletions strengthen `DIFFERS`
exclusions and cannot rescue `NEEDS` rows. This is a larger finding than one row
in the sense that it re-grades the E-block's *inventory*, and a smaller one in
the sense that the ledger's E-block verdict counts are unchanged.

---

## 5. POSTFLIGHT — inline hostile review

**Strongest overclaim available in this artifact.** Reading §3.6 as *"GU has no
Higgs."* It is not, and that sentence is explicitly forbidden by the routing
method's summary grammar. What §3.6 supports is narrower on four axes at once:
*linearized* declared content, the *connection* sector only, the *observation*
reduction only, and *elementary* fields only. Composites, the nonlinear content,
the fate of the `s^*`-kernel under the action, and the entire spinor sector are
all untouched. The allowed sentence is: *the both-legs-vertical sector of
`Omega^1(Y, ad)` hosts no colour-singlet weak doublet under the source-declared
reduction, on either horn of `SOLDERED-AD`; the curvature-induced connection
mechanism is a distinct object and remains governed by its own gates.*

**Second overclaim, subtler and more likely.** Reading this as a result *against
Weinstein*. It is not. `CB-A:E2` is a **repo-internal derived shape constraint**;
the source supplies neither the `10 (x) 45` sector nor the count of 6+6. The
disavowal runs the other way — the transcript rejects the Kaluza-Klein reading in
as many words (*"It's not Kaluza Klein"*), and `CB-A:E2`'s sector is a KK-split
object. **LA-8 is a repo self-correction. Its target claim is CB-A's, not
Weinstein's.**

**Strongest contrary reading, and it is real.** `SECTION-VS-OBSERVERSE` is
`status: open`. If the ambient theory is the physics and the pullback is merely a
readout, then "what is the 4D Lorentz type" is the wrong question, and §3.1's
force evaporates. MD-1 records this defence and does not defeat it; neither do I.
What blunts it here — and this is the load-bearing move against laundering — is
that **`CB-A:E2` needs the same horn.** A row asserting "the Higgs component is a
Lorentz scalar in this 4D sector" is already committed to the section-as-reduction
reading. Under the other horn the row is not `NEEDS/MISSING_CONSTRUCTION` either;
it is ill-posed. So the grant is *shared*, not differential, and the retyping does
not consume it. Second contrary reading: `[B7]`'s forcing assumes the projector is
`so(3,1)`-equivariant; a *gauge-fixed*, non-equivariant projector escapes it, at
the price of making the resulting "scalar" frame-dependent.

**Weakest seam — and it is not in this artifact.** It is
`lab/methods/source-native-comparator-routing.md:62-63`, which describes the
**source-native** side of fork 2 as including *"vertical connection components may
appear as four-dimensional scalars after reduction"* `[S11]`. That is the step
§3.1 refutes under the source-declared reduction — and the same document, at line
89, lists MD-1 as one of fork 3's source-native pointers. **The mandatory routing
method contains, inside its own definition of the source-native mechanism, the
step that one of its own cited pointers computes to be false.** Both files were
created 2026-08-14. This is a live internal inconsistency in a `doc_type:
mandatory_semantic_and_inference_boundary` document, and it is the single
highest-leverage thing in this delta, because every future agent reading that
paragraph will re-import the refuted step. **Escalated to the method's owner; not
actioned, and not writable from this channel.**

**Second seam, smaller.** The routing audit's `discovered_artifacts()` enumerates
seven channel tokens and omits `four-d-mode-decomposition`, so MD-1 — a file the
method itself cites — is outside the registry's coverage and carries no routing
notice. The audit asserts registry-equals-discovery, so this cannot be fixed by
adding a registry row alone.

**Reproducibility seam inside LA-8.** The SO(10)→SM branching table of §3.3 is a
**declared input** `[T]`, not a machine-derived branching. It is certified by
dimension sums, vanishing hypercharge traces, and reproduction of three numbers
CB-A printed independently — but a systematic error shared with CB-A's own
conventions would survive all four tests. What protects the *conclusion* is that
it does not depend on the table: the correction is driven by `[B1]`
(`1`, not `10`), which is pure `so(3,1)` linear algebra with no SO(10) content,
and by `[D6]`. The table only converts that into CB-A's own vocabulary.

**Non-vacuity.** Ten controls must fire and do: `[L7c]` (42 distinct `RA-E1`
records vs 1 for `RA-E2`), `[L12c]`, `[S12c]`, `[A7c]` (contraction ≠ projection
for a general section), `[B4c]` (inert ⇒ 10), `[B5c]` (so(3) ⇒ 2), `[C9c]`,
`[C10c]`, `[D7c]` (inert ad leg ⇒ 45), `[E3c]`.

---

## 6. THE DELTA — versionless, against `a148ed80` / `v0.258`

**This is not a ledger edit.** No file in `lab/process/` was modified.

### `RA-E2`

```yaml
verdict:        NEEDS               ->  DIFFERS
reason_kind:    MISSING_CONSTRUCTION -> STRUCTURAL_DIFFERENCE
distance: >
  The named adapter is built, not missing, and it returns the wrong Lorentz
  type. Observation is a contraction: s^* is surjective onto T*X with a
  10-dimensional kernel, so a vertical form leg is contracted into the same 4D
  one-form and never becomes a 4D scalar. Under the disavowed projection the
  vertical fibre Sym^2(T*X4) has Lorentz-trivial component 1, not 10, so
  CB-A:E2's 10 (x) 45 sector is 45-dimensional on the INERT-AD horn and exactly
  1-dimensional on the SOLDERED-AD horn, and hosts 0 colour-singlet weak
  doublets on both. Any equivariant vertical-scalar projector is forced through
  that same trace line, so owning the packet's res_s^V route does not restore
  the count. The ad-valued zero-form channel does give a 4D scalar and hosts 0
  doublets on both horns. Open successor: whether the 10-dimensional s^*-kernel
  reappears as independent 4D fields once the action and the section's equation
  of motion are supplied.
revival_trigger: >
  an exact 14D-to-4D vertical-scalar adapter
  ->
  a dynamical reappearance of the s^*-kernel as independent 4D fields under a
  named action, OR a declared non-equivariant projector whose output is
  nonetheless a Lorentz scalar
mapping_grade: >
  EXACT_SHAPE_CONSTRAINT
  ->
  EXACT_SHAPE_CONSTRAINT_REFUTED_AT_THE_FORM_LEG__OBSERVATION_IS_A_CONTRACTION_SURJECTIVE_ONTO_T_STAR_X_KERNEL_10__VERTICAL_FIBRE_LORENTZ_TRIVIAL_COMPONENT_1_NOT_10__SECTOR_45_INERT_AD_OR_1_SOLDERED_AD__ZERO_COLOUR_SINGLET_WEAK_DOUBLETS_ON_BOTH_HORNS__EQUIVARIANT_PROJECTOR_FORCED_THROUGH_THE_TRACE_LINE__AD_VALUED_ZERO_FORM_CHANNEL_ALSO_ZERO__S_STAR_KERNEL_DYNAMICS_OPEN
evidence: >
  cb-a-representation-content-2026-08-05.md:E2
  ->  + lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md
      + explorations/unified-source-datum-packet-v0-2026-07-30.md:128
      + lab/active-research/joe-directed/ledger-advancement/la8-...-2026-08-15.md
forks_carried: [SOLDERED-AD (declared; NOT load-bearing for this row -- both
                horns give zero), SECTION-VS-OBSERVERSE (shared with CB-A:E2)]
```

### `RA-E4` — distance only, verdict unchanged

Append: *"CB-A:E4's printed inventory of 18 doublets loses its `10⊗45` term of
12; three of the six `(1,2,+1/2)` there are `V₁₀`'s doublet paired with an SM
singlet of the 45, so the `V₁₀ → 2` entry is partly a subcount rather than an
independent carrier. The multi-doublet verdict survives on `Sym²(S) → 4` alone,
which is even and `>= 2`."*

### `RA-E3` — revival trigger only, verdict unchanged, exclusion confirmed

Append to `distance`: *"the class exclusion is independently reproduced. The
revival trigger as written is unfireable through observation: `s^*` sends a
one-form cell to a 4D one-form, not to a 4D scalar doublet. Retarget it at a
non-observation descent or at the `s^*`-kernel's dynamics."*

### `RA-E1` — distance only, verdict unchanged

Append: *"beneath the rank-196/rank-0 compatibility failure, the connection-sector
`V₁₀` offer is a Higgs only if the vertical form leg carries a Lorentz scalar,
which observation does not supply. The `Sym²(S)` offer is a distinct
spinor-bilinear carrier and is not assessed here."*

---

## 7. CLAIM CEILING AND EVERY IMPORTED ASSUMPTION

**Ceiling.** Kinematic, representation-theoretic and linearized. LA-8 types
indices and counts multiplicities. It computes **no** action, potential, mass,
propagator, vacuum or quantization; it decides **no** fork; it moves no canon
entry, grade, current-state surface or ledger row. Its positive product is one
proposed retyping, three proposed distance appends, and two escalated seams.

Load-bearing grants, each named:

1. **`Y14 = Met(X4)` with fibre `Sym^2(T*_x X4)`.** Repository-derived
   (`canon/shiab-existence-cl95.md`), source-supported, not re-derived here.
   **This is the single point of failure of the whole result** — deny it and
   `[B1]` has no content.
2. **`SECTION-VS-OBSERVERSE`, section-as-reduction horn.** `status: open`.
   **Shared with `CB-A:E2`**, which cannot state its own claim without it. Under
   the other horn the row is ill-posed, not `NEEDS`.
3. **The physical local Lorentz group acts on the fibre by `Sym^2`.** Forced by
   (1); functoriality of `Met`. Not an assumption about `P_H` — that is the fork.
4. **`SOLDERED-AD` is not assumed either way.** Both horns are computed to a
   number and both give zero. This is why the row can be adjudicated.
5. **`VERTICAL-FROBENIUS-TRACE` is NOT used.** Pre-registered at §0/P6 and held:
   no fibre metric, no `lambda`, enters `[B1]`–`[B7]` or `[D1]`–`[D6]`. LA-8's
   form-leg conclusion therefore rests on strictly fewer grants than MD-1's full
   result does.
6. **`CARRIER-SPLIT` is not load-bearing.** Both horns share the internal block;
   every computation here lives inside it.
7. **The SO(10)→SM branching table is DECLARED**, certified four ways, and the
   conclusion does not depend on it (§5).
8. **The KK projection reading is a declared comparator**, used only to compute
   what the disavowed map would give, and only to correct a number computed in
   that same reading. Never used for a source-native conclusion.
9. **The spinor sector, composites, nonlinear content and the `s^*`-kernel's
   dynamics are out of scope** and no statement here bears on them.

**Rule-4 compliance (no count from a multiplicity without an index/grade map).**
The only counts asserted are dimensions of exactly computed invariant subspaces
and multiplicities inside a declared, reproduced branching. No physical particle
count is asserted anywhere.

## 8. NEXT GATE

Not more representation theory. In order:

1. **The routing-method seam (§5).** Highest leverage in this delta, and it is a
   one-paragraph fix in a mandatory document by its owner.
2. **The `s^*`-kernel's dynamics.** The only route by which `RA-E2`'s underlying
   requirement can still be met inside the connection sector. It requires the
   operative second action — the same object LA-4's vertex cut and LA-6's cover
   object already identify as the axis's bottleneck. `RA-E2` is not an exception
   to that cut after all; it is downstream of it by a different edge.
3. **The spinor sector**, where MD-1's own weakest seam (`vz-schur-complement`
   §18.3, graded VERIFIED, whose "`s^*` retains only horizontal components"
   holds only at `d_mu g = 0`) still propagates into
   `canon/no-go-class-relative-map.md:401` and five explorations. Owned by the VZ
   chain, not by this channel.

Selection stays inside this channel. No ledger, canon, current-state or public
surface moves.
