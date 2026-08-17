---
artifact_type: exploration
status: exploration
doc_type: construction_result
created: 2026-08-17
work_item: Z3R1
channel: z3-receptacle
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
grade: "EXACT F_2/integer arithmetic throughout; no float anywhere (swept).
  62/62 checks, exit 0: the universal splitting-principle identity
  w(Sym^2 Q) = 1+(w1^2+w2)+(w1*w2+w3) is verified as an EXACT multivariate
  F_2 polynomial identity (3 formal roots), not a single substitution; w(nu)
  is computed by TWO independent, disjoint methods -- splitting principle on
  Q's derived classes, and a trivialization argument via Sym^2(R^4) genuinely
  trivial + RP^3 =~ SO(3) parallelizable -- asserted to agree exactly.
  CONTRARY CONTROLS prove the machinery discriminates: Q's own classes
  (w1=a, w2=a^2, w3=a^3, the SAME code path) are all NONZERO, and a FORMAL
  rank-3 bundle with independent classes gives a nonzero Sym^2 class,
  proving nu's vanishing is a fact about RP^3's specific Q, not a vacuous
  algebraic identity. 6 planted-false facts observed False inside the
  normal run. Part 4 of tests/dim13/mh7_dim13_link_receptacle_probe.py is
  REPRODUCED [R] independently (not copy-pasted) and the computed
  orientation bit programmatically SELECTS branch A, matching that probe's
  own certified Betti sequence exactly. --selftest: clean baseline verified
  FIRST (33/33), then 10/10 machinery-corruption mutations each drive a
  genuine named [FAIL] line (none crash). 24 file-level textual checks read
  exact substrings from the packet, register M-H5, CURRENT-STATE.yaml,
  GEOMETER-VS-PHYSICS-OBJECTS.md, the source-claim register, AR-1, and
  (mid-flight addition) hinge-panel-synthesis, HE-1, CR-B and ST-1."
disposition: NU_IS_GENUINELY_TRIVIAL_RANK7_OVER_RP3__W1_W2_W3_ALL_ZERO_BY_TWO_INDEPENDENT_METHODS__ORIENTATION_BIT_W_DECIDED_UNTWISTED_NOT_LEFT_AS_OPEN_FORK__MOD3_FUNDAMENTAL_CLASS_EXISTS_ON_THE_MODEL__D1_AND_D2_CLOSED_D3_D4_D5_D6_REMAIN_FULLY_OPEN__RECEPTACLE_ADMISSIBILITY_BIT_NOT_A_COUNT__FIVE_HINGE_KILLS_SURVIVE_THE_POST_08_11_RECORD_UNTOUCHED__BRIDGE_FROM_BIT_TO_INTEGER_COUNT_NOW_CARRIES_TWO_NAMED_OBSTRUCTIONS_NOT_ONE
title: "Z3-R1: the referee bundle nu = R (+) Sym^2(Q*) over the RP^3 spine
  is GENUINELY TRIVIAL -- w1=w2=w3=0 exactly, by two independent methods --
  so the orientation bit `w` (design packet D1+D2, AR-1 row 6, register
  M-H5) is DECIDED UNTWISTED, not left as an open fork: the mod-3
  fundamental class exists on the model, closing D1+D2 and upgrading S3
  toward verified-on-the-model. This is a receptacle-ADMISSIBILITY bit, not
  a generation count, and presupposes neither SC-GEN-01 nor SC-GEN-04.
  Mid-flight addition (Joe, via the session owner): the packet's five
  hinge/2+1 kills (Rung-1 fence, coboundary theorem, Euler-degree kill,
  legb2's (0,0,0), PH-K1 vectorlike) all SURVIVE the post-08-11 record
  untouched -- HE-1/CR-B/ST-1 run a textually distinct, later,
  non-overlapping 2+1 mechanism (Pati-Salam 16/144 subtractive pairing,
  n_g -> n_g-1) that cites, supersedes, or even mentions none of the five;
  any future bridge from this Z/3 bit to an integer generation count now
  carries TWO obstructions, not one: Hom(Z/3,Z)=0, AND the source's own
  generation structure is ASYMMETRIC (2+1, a representation-theoretically
  distinct imposter), which a bare cyclic group with no privileged element
  cannot express without unbuilt extra structure."
depends_on:
  - explorations/z3-receptacle-design-packet-2026-08-11.md
  - explorations/mh7-dim13-restatement-2026-08-03.md
  - explorations/resolver-wave-c-rebased-q5-q6-mh7-2026-08-03.md
  - lab/process/improvement-register-2026-08-03.md
  - lab/process/hostile-reviews/2026-08-11-z3-receptacle-design-review.md
  - lab/active-research/joe-directed/archaeology/ar1-dropped-commitments-ledger-2026-08-15.md
  - CURRENT-STATE.yaml
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - lab/sources/source-claim-register.yaml
  - lab/process/hinge-panel-synthesis-2026-08-03.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md
  - lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md
  - lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md
  - lab/active-research/joe-directed/carrier-decl/fx2-typed-carrier-declaration-2026-08-16.md
  - lab/methods/source-native-comparator-routing.md
  - tests/dim13/mh7_dim13_link_receptacle_probe.py
scripts:
  - tests/channel-swings/joe_directed_z3r1_nu_trivial_w_untwisted.py
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
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY` — this file computes no
> conventional-physics comparator itself (it is a Stiefel-Whitney class
> computation on a normal bundle in the program's boundary differential
> topology). It borders the `SC-GEN-01`/`SC-GEN-04` disavowed comparator
> zone (the three-repeated-generations reading) because it is one gate of
> the Z/3 generation-count receptacle program, and §7 of this file resolves
> a direct question about whether it touches the source's 2+1/imposter
> structure. Neither disavowed claim is presupposed anywhere below (§0, §7).
>
> **REQUIRED REGISTRY WRITE, not performed here.** This pass is scoped to
> two paths on a shared, concurrently-written checkout, so it cannot edit
> `lab/process/source-native-comparator-routing-registry.json`. Without that
> edit, `process_gates/source_native_comparator_routing_audit.py`'s
> unclassified-artifact count rises from 5 (its current baseline) to 6 —
> the identical, already-precedented situation FX-2 and CR-B hit under the
> same two-file constraint. The integration owner needs one entry:
> ```json
> { "path": "lab/active-research/joe-directed/z3-receptacle/z3r1-nu-trivial-w-untwisted-2026-08-17.md",
>   "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY" }
> ```

# Z3-R1 — the referee bundle is trivial; the orientation bit is untwisted

## 0. What this is, and the claim ceiling that binds every line below

**The task.** `explorations/z3-receptacle-design-packet-2026-08-11.md` (D1+D2,
priced at register row M-H5, `lab/process/improvement-register-2026-08-03.md:155`,
"Verify ν decomposition (half-day); SW/triviality check (hours)") asks for
exactly one computation: verify `nu ~ R (+) Sym^2(Q*)`, rank 7, over the `RP^3`
spine, then compute `w1, w2, w3` of `nu`, deciding the orientation bit `w`
that "decides the entire mod-3 top-degree structure" (`explorations/mh7-dim13-restatement-2026-08-03.md`
Section 6, gap O3). This file does exactly that, and nothing more.

**The claim ceiling, stated before any computation, binding throughout.**

1. **This is a receptacle-ADMISSIBILITY bit, not a generation count.**
   `CURRENT-STATE.yaml`'s `next_condition` ends: *"Do not ... infer a
   generation count."* Nothing below outputs, suggests, or is usable as an
   integer generation count. The output is a Stiefel-Whitney class in
   `H^*(RP^3;F_2)` and a branch selector (untwisted/twisted) for an existing
   homology computation — both purely topological facts about a normal
   bundle, with the word "generation" appearing in this file only in
   sections that explicitly fence it off (§0, §7).
2. **This presupposes NEITHER `SC-GEN-01` NOR `SC-GEN-04`.** Both are
   `disavowed-by-source` in `lab/sources/source-claim-register.yaml`
   (`SC-GEN-01`: *"we do not believe that nature has simply repeated herself
   three times"*; `SC-GEN-04`: the imposter *"is not a true generation as it
   has a different representation structure"*). AR-1's own Lens 6 typed this
   exact work item: *"Neither row's work presupposes a disavowed claim ...
   the other is an orientation-bit computation on a normal bundle"*
   (`lab/active-research/joe-directed/archaeology/ar1-dropped-commitments-ledger-2026-08-15.md`,
   §1 Lens 6). §7.3 below re-verifies this by inspecting the actual
   construction line by line, per the mid-flight addition.
3. **The generation-count relation stays UNSETTLED.**
   `GEOMETER-VS-PHYSICS-OBJECTS.md`'s Generation-count row: *"The relation
   is **unsettled**, not a settled native-side win. `Hom(Z/3,Z)=0` blocks a
   direct additive identification, so a separately constructed integer
   observable and bridge would be required."* Nothing here settles it. §7.2
   adds a SECOND, independent obstruction any future bridge must clear.
4. **Scope: D1+D2 only.** D3 (stable parallelizability of the TRUE `S(nu)`
   bundle over the full 7-dim `P(TX^4)`), D4 (the reframing-orbit bound), D5
   (the corner type-check) and D6 (the non-additive dictionary) are
   untouched. §5 states precisely what this file's result does and does not
   feed into D3.

---

## 1. PREFLIGHT — six lenses, run inline before computing

**Lens 1 — characteristic classes over `F_2` (Stiefel-Whitney specialist).**
*Route:* compute `w(Sym^2 Q)` via the splitting principle on formal roots of
`Q`, as an exact multivariate polynomial identity first, substitute `Q`'s
actual classes second — never conflate the two steps, because an identity
verified only after substitution cannot distinguish "true for this `Q`" from
"true for every rank-3 bundle." *Prediction, staked before computing:* the
closed form will have NO degree-1 term for ANY rank-3 bundle (a structural
fact about `Sym^2`, `w_1(Sym^2 Q)` is always 0 for real bundles since the sum
of the roots doubles), while `w_2` and `w_3` will depend on `Q`'s actual
classes and need not vanish in general. *Cheapest kill:* if the identity
fails at even one monomial, the whole computation is void.

**Lens 2 — bundle arithmetic / vector-bundle classification.** *Route:*
Wave C's stated precondition (`explorations/resolver-wave-c-rebased-q5-q6-mh7-2026-08-03.md:255-258`)
names THREE things to prove: the decomposition itself, `w1=w2=w3=0`, and "the
relevant rank-at-least-four classification." The third is not decoration —
vanishing SW classes alone do not imply a bundle is trivial in general; the
cancellation theorem (rank of the bundle exceeds the dimension of the base)
is what upgrades "SW-trivial" to "trivial." *Prediction:* `rank(nu)=7` and
`dim(RP^3)=3` satisfy the hypothesis with room to spare, so if a genuinely
stably-trivial complement can be exhibited, the cancellation theorem closes
the gap for free. *Cheapest kill:* if no genuinely trivial complement to
`Sym^2(Q)` can be exhibited, only the weaker SW-vanishing survives and D1's
third clause stays open.

**Lens 3 — referee/spec compliance.** *Route:* the packet is binding per the
brief; read D1 and D2's exact sentences before computing anything, and check
after computing whether the delivered object matches the named object (`nu`
over the fixed-`x` `RP^3` spine, per M-H5's own "at fixed x" framing and the
existing probe's own scope) rather than silently substituting a related but
different bundle (e.g. the global `S(nu)` over the 7-dim `P(TX^4)`, which is
D3's, not D2's, object). *Cheapest kill:* if the packet's D2 prose, read
literally, names the global object and no fixed-`x` reading is defensible,
this file has silently narrowed the task and must say so plainly (§9 does).

**Lens 4 — supersession hygiene.** *Route:* before trusting AR-1's "row 6 is
LIVE" typing, re-verify it against the live tree rather than citing AR-1's
own claim uncritically — AR-1 itself measured a 40% first-pass error rate on
inherited rows. Check for artifacts dated after AR-1 (2026-08-15) that touch
row 6, M-H5, or the packet's disposition; run `novelty-check.py` on the exact
computational terms before calling anything new. *Cheapest kill:* a newer
artifact already computing `w(nu)` would make this whole file a duplicate.

**Lens 5 — adversarial reading of my own derivation.** *Route:* the
"genuinely trivial, not just SW-trivial" upgrade is the strongest claim in
this file and the one most likely to be quietly wrong. Attack it at three
seams before trusting it: (i) is `Q* =~ Q` an HONEST bundle isomorphism (not
merely a stable/K-theoretic one)? (ii) is "`RP^3 =~ SO(3)` hence
parallelizable" applying GENUINE (not merely stable) triviality of `T(RP^3)`?
(iii) does the cancellation-theorem citation actually require BOTH
`rank > dim(base)` AND a genuinely trivial stable complement, and do I have
both? *Cheapest kill:* if any of the three is only a stable statement, the
"genuinely trivial" upgrade silently collapses to "merely SW-trivial" and §5
must say so.

**Lens 6 — representation-theory / generation-structure auditor (mid-flight
addition).** *Route:* Joe's question, relayed by the session owner, asks
whether this file's construction smuggles an assumption that GU's three
generations are interchangeable, when the source's own stated structure is
asymmetric (2+1, one representation-theoretically distinct imposter). Do not
answer from memory of the packet's own fence (§56, "the classic trap") —
re-read `nu`'s actual construction line by line and check whether a fermion,
family index, or gauge/family representation appears ANYWHERE in it.
Separately, re-read HE-1/CR-B/ST-1 directly rather than trusting the
relayed paraphrase, because the standing correction in this repository is
that relays regress frames (`memory: "Relays carry claim IDs"`). *Cheapest
kill:* if `nu`'s construction references any fermion representation, the
claim-ceiling item 2 above is false and must be retracted, not patched.

**Pre-flight failure modes, and the mitigation applied.**

1. *Reading the SW-triviality result as bearing on the generation count.*
   Mitigated by claim-ceiling items 1-3, restated at every section boundary
   below (§4, §5, §7, §9).
2. *Silently answering D3 instead of D2, or claiming more of the outcome
   table than D1+D2 deliver.* Mitigated by §5's explicit non-claim and by
   never invoking the phrase "outcome (a)" without the D3 caveat attached.
3. *Resurrecting a dead route.* Mitigated by Lens 4's fresh AR-1 re-check
   (§2) and the `novelty-check.py` sweep (§8.4) — both run this session, not
   quoted from a prior one.
4. *The mid-flight addition read as license to reopen the hinge/2+1 route.*
   Mitigated explicitly: §7.1's SURVIVES findings are typed exactly as the
   session-owner instruction requires — "a dated flag for the integration
   owner, NOT a license to re-open the route" — and no disposition in this
   file touches the hinge count's status.
5. *Overclaiming the "two obstructions" argument in §7.2 as a proof.*
   Mitigated: it is typed as a STRUCTURAL OBSERVATION about `Aut(Z/3)`, not
   a theorem about GU, and is hostile-reviewed at §8.6.

---

## 2. AR-1 row 6 status, re-verified this session (not quoted from AR-1)

The brief requires confirming row 6 is still live given rows 5/7/8 are not.
Re-checked directly against
`lab/active-research/joe-directed/archaeology/ar1-dropped-commitments-ledger-2026-08-15.md`
this session (not merely cited):

- **Row 6, verbatim:** *"`Z/3` receptacle D1+D2: referee the normal-bundle
  decomposition and compute the orientation bit `w`. Named 2026-08-11 as
  hours-scale, register row `M-H5`. Zero follow-up: the packet is cited by
  exactly two files, the packet index and its own hostile review."* Typed
  `LIVE`, difficulty **S**.
- **AR-1's own hostile-review sample (§6 of that file) independently
  re-checked row 6 and confirmed it:** `| `Z/3` orientation bit `w` | LIVE |
  LIVE | correct |` — one of only 6/10 sampled rows the hostile pass did
  NOT retype.
- **AR-1 carries exactly three correction banners**, dated after the
  original 14:04 table: `CORRECTION IV-20260815` (closes rows 1,2,3,4,7,16),
  `CORRECTION AR1-CB-20260816` (retypes rows 5, 9, 12, 21), `CORRECTION
  AR1-R8-20260816` (closes row 8, the M-H17 overlap). **None of the three
  mentions row 6.** No sentence of the form "Row 6 is ..." appears anywhere
  in the file — the exact pattern by which rows 5, 8, 9, 12 and 21 WERE
  retyped is absent for row 6.
- **Swept the live tree for anything newer that touches row 6, M-H5, or the
  packet's disposition** (this session, not inherited): the only files
  touched after AR-1 that mention the receptacle at all are AR-1 itself,
  `global-anomaly-leg-2026-07-20.md` (pre-existing spin-wall citations,
  untouched), `frontier-design-packets-index-2026-08-11.md` (the packet
  index, unchanged since 08-11), `portfolio-correction-wave-2026-08-12.md`
  (a different receptacle-adjacent item, `PC-3`, already typed
  `DONE_ELSEWHERE` by AR-1 itself), and `conditional-build/cb-c-anomaly-conditions-2026-08-05.md`
  (pre-existing, cited by the packet, unchanged). None retypes row 6.

**Verdict: row 6 is confirmed LIVE, untouched, exactly as the brief states.**
This is the probe's `P8.ar1_row6_text`, `P8.ar1_row6_hostile`,
`P8.ar1_three_banners`, `P8.ar1_row6_untouched`, `P8.ar1_rows_5_8_touched`
and `P8.ar1_row7_closed` checks (§8).

---

## 3. The packet's D1+D2, taken as binding

Verbatim, `explorations/z3-receptacle-design-packet-2026-08-11.md`:

> **D1 — the nu-decomposition referee** ... Typed statement to verify: over
> the `RP^3` spine, `nu ~ R (+) Sym^2(Q*)` (from `Sym^2(T*) = Sym^2(l*) (+)
> l* (x) Q* (+) Sym^2(Q*)`), rank 7; then compute `w_1, w_2, w_3` of `nu`
> and the stated rank-at-least-four classification (Wave C: these are the
> exact preconditions before the sphere bundle may be called `RP^3 x S^6`
> even noncanonically). Kill condition: decomposition fails -> the link
> model collapses ... Control: a planted wrong-rank decomposition must be
> rejected.
>
> **D2 — the orientation bit `w`** ... Typed statement: compute the
> orientation character of the `S^6`-row of `S(nu)` over `P(TX^4)` in both
> orientation branches. Probe Part 4 (P5) already gives the exact fork:
> untwisted -> mod-3 homology of `S^3 x S^6` type with a mod-3 fundamental
> class; twisted -> `H_9 = 0`, no mod-3 fundamental class at all. This
> single bit "decides the entire mod-3 top-degree structure" ... Control:
> both branches must reproduce the probe's spine-transfer in degrees <= 5.

And the exact, still-unproved precondition Wave C names
(`explorations/resolver-wave-c-rebased-q5-q6-mh7-2026-08-03.md`, quoted in
full, not excerpted, because its scope matters):

> After choosing an auxiliary Riemannian reduction/Mostow-tubular model, the
> panel proposes at fixed x a normal bundle `nu_x = R plus Sym^2 Q*` over
> the metric-fibre RP3 spine. Before its sphere bundle may be called
> noncanonically `RP3 x S6`, one must prove the stated normal-bundle
> identification, `w1=w2=w3=0`, and the relevant rank-at-least-four
> classification.

Three things this quote settles about scope, read before computing:

1. **"At fixed x"** — the object is the bundle over the single `RP^3` fiber
   (`M-H5`'s own framing: "Verify ν decomposition ... SW/triviality check"),
   not the global bundle over the 7-dim `P(TX^4)` (that is D3's "obstruction
   computation for the true `S(nu)`-bundle over `P(TX^4)`" — a different,
   separately priced step). D2's own prose says "over `P(TX^4)`" in one
   place, but its cited instrument — Probe Part 4 — is the fixed-`x`,
   `RP^3`-fiber computation. §9 addresses this directly rather than
   silently picking a reading.
2. **Three things to prove, not one.** The decomposition; `w1=w2=w3=0`;
   AND the rank classification. D1's own kill condition ("decomposition
   fails") and control ("a planted wrong-rank decomposition must be
   rejected") are both honored below (§4.1, §4.6).
3. **The word "noncanonically."** Even a fully successful computation only
   licenses calling `S(nu)` "`RP^3 x S^6`" up to an unspecified
   isomorphism — it does not construct a canonical identification. Nothing
   below claims more than that.

---

## 4. The mathematics

### 4.1 The decomposition (D1, first clause)

Standard fact, reproduced not merely cited: for `RP^3 = P(V)`, `V = R^4` the
tangent space of `X^4` at a fixed point, with tautological line `l` and
quotient bundle `Q = V/l` (rank 3), the defining exact sequence `0 -> l -> V
-> Q -> 0` splits via any metric, giving `V = l (+) Q`. Since `Sym^2` is a
polynomial functor, `Sym^2(V) = Sym^2(l) (+) (l tensor Q) (+) Sym^2(Q)` for
ANY splitting of a rank-4 bundle into rank-1 + rank-3 pieces — a general
algebraic identity, ranks `1 + 3 + 6 = 10 = rank Sym^2(R^4)` (probe
`P5.SymV_rank_sum`). `V` here is the (fixed-`x`) tangent space, so this is
exactly the packet's `Sym^2(T*) = Sym^2(l*) (+) l* (x) Q* (+) Sym^2(Q*)`
(dualized; ranks are unaffected by dualizing). `Sym^2(l)` is a real line
bundle squared, hence CANONICALLY trivial (any real line bundle's transition
functions lie in `{+-1}`, which square to `1`) — this is where the packet's
`nu ~ R (+) Sym^2(Q*)` gets its `R` summand: it is the `Sym^2(l*)` term,
already identified as trivial before the formula is even written down. So
`nu := (l tensor Q)`'s normal-directions complement `= R (+) Sym^2(Q*)`,
rank `1 + 6 = 7`. **Verified**, probe Part 5 (`P5.rank_Sym2Q`, `P5.rank_nu`,
`P5.SymV_rank_sum`).

**D1's planted control** (a wrong-rank decomposition must be rejected): the
probe's `P5.rank_nu` check IS this control — `rank(Sym^2 Q) = C(3+1,2) = 6`
is asserted exactly, and mutation `wrong_rank_Sym2Q` (§6) proves a
corrupted rank formula (`3*3=9` instead of `6`) is caught, breaking both
`rank(nu)=7` and the `Sym^2(V)` rank-sum-to-10 check.

### 4.2 `w(Q)`, derived not assumed

`H^*(RP^3;F_2) = F_2[a]/(a^4)`, `a` the degree-1 generator. `gamma (+) Q = V`
trivial gives `w(gamma)*w(Q) = 1`; `w(gamma) = 1+a` (definition of the
tautological line bundle); solving in the truncated ring gives `w(Q) =
1+a+a^2+a^3` (verified by multiplying back: `(1+a)(1+a+a^2+a^3) = 1 +
2(a+a^2+a^3) + a^4 = 1` mod 2, mod `a^4=0` — probe `P2.gamma_Q_trivial`).
So **`w1(Q)=a`, `w2(Q)=a^2`, `w3(Q)=a^3` — all three NONZERO.** This is
`Q`'s own class, not `nu`'s, and it is the first contrary control (§4.6).

### 4.3 `w(Sym^2 Q)` — METHOD A, splitting principle

By the splitting principle, `w(Sym^2 Q) = product over i<=j of (1+x_i+x_j)`
for formal roots `x_1,x_2,x_3` of `Q`. Verified as an EXACT polynomial
identity in `F_2[x1,x2,x3]` (probe `P1.identity`, `P1.no_w1_term`), not
merely at one substitution:

```
w(Sym^2 Q)  =  1  +  (w1(Q)^2 + w2(Q))  +  (w1(Q)*w2(Q) + w3(Q))
```

with **identically zero degree-1 coefficient**, for ANY rank-3 real bundle
`Q` — a structural fact (the sum of `Sym^2`'s six roots is `2*(x1+x2+x3) = 0`
mod 2). Substituting `Q`'s actual classes (§4.2): `w1(Q)^2+w2(Q) = a^2+a^2 =
0`; `w1(Q)*w2(Q)+w3(Q) = a^3+a^3 = 0`. **`w(Sym^2 Q) = 1` identically.**

### 4.4 `w(Sym^2 Q)` — METHOD B, independent trivialization argument

Disjoint machinery from §4.3 (no splitting principle, no formal roots):
`Sym^2(V)` is the GENUINELY trivial rank-10 bundle (`V` itself is the fixed
tangent space, honestly trivial, not merely stably). `Sym^2(l)` is
genuinely trivial (§4.1). `l tensor Q =~ T(RP^3)` (the standard tangent-space
identification `T(P(V)) = Hom(l,Q) = l^* tensor Q =~ l tensor Q`, real line
bundles being self-dual via any metric) — and `T(RP^3)` is GENUINELY
trivial, not merely SW-trivial: `RP^3 = S^3/{+-1}`, and `S^3 = Sp(1)` is a
Lie group with `{+-1}` central, so `RP^3` inherits a Lie group structure
(`=~ SO(3)`) and Lie groups are parallelizable by left-translating a basis
of the Lie algebra. Independently, `w(T RP^3) = (1+a)^4 = 1+4a+6a^2+4a^3+a^4
= 1` mod 2 (binomial coefficients `4,6,4` all even, `a^4=0`) — probe
`P4.TRP3_trivial`, confirming the SW class is consistent with genuine
triviality. Solving `w(Sym^2 l) * w(l tensor Q) * w(Sym^2 Q) = w(Sym^2 V)`,
i.e. `1 * 1 * x = 1`, has the UNIQUE solution `x=1` in this ring (probe
`P4.methodB_unique_solution` — verified by exhaustive search over all 16
elements of `F_2[a]/(a^4)`, not asserted). **METHOD B independently forces
`w(Sym^2 Q) = 1`**, agreeing with METHOD A exactly (`P4.methodB`) without
sharing a single line of code with it.

Because `T(RP^3)`, `Sym^2(l)` and `Sym^2(V)` are each GENUINELY trivial (not
merely SW-trivial), and `Sym^2(Q) (+) [Sym^2(l) (+) l tensor Q] = Sym^2(V)`
is a genuine bundle isomorphism, `Sym^2(Q)` is STABLY trivial with an
explicit genuinely-trivial rank-4 complement. `rank(Sym^2 Q) = 6 >
dim(RP^3) = 3`: the standard cancellation theorem for vector bundles over a
CW complex (a real bundle of rank `k` over a base of dimension `n < k` is
determined up to isomorphism by its stable class — e.g. Husemoller, *Fibre
Bundles*, or Hatcher's *Vector Bundles and K-Theory* notes, the standard
stable-range result; cited as STANDARD, not re-derived here) upgrades
stable triviality to **genuine** triviality: `Sym^2(Q)` is an honestly
trivial rank-6 bundle. This is Wave C's "rank-at-least-four classification"
clause, discharged — probe `P5.rank_at_least_four` verifies the numeric
hypothesis (`7 >= 4`) exactly.

### 4.5 Assembling `nu`, and the answer

`nu = R (+) Sym^2(Q*)`. `Q* =~ Q` as real bundles: any Riemannian metric on
`Q` gives an HONEST (not merely stable) bundle isomorphism `Q -> Q^*`, `v
|-> g(v,-)` — `RP^3` is compact, so a metric exists. So `w(nu) = w(R) *
w(Sym^2 Q) = 1 * 1 = 1`.

```
  w1(nu) = 0        w2(nu) = 0        w3(nu) = 0
```

And more: since `Sym^2(Q)` is genuinely trivial (§4.4) and `R` is trivial by
definition, **`nu` itself is a genuinely trivial rank-7 bundle**, not merely
SW-trivial. `S(nu)` is therefore an ACTUAL product `RP^3 x S^6` (up to an
unspecified, "noncanonical" identification — §3 item 3), not merely a bundle
with vanishing characteristic classes that could still be twisted in a way
`F_2` cohomology cannot see.

### 4.6 Contrary controls — proving the machinery discriminates

A computation that always returns "trivial" is worthless. Two independent
demonstrations that it does not:

**(a) `Q` itself, same code path.** `w1(Q)=a`, `w2(Q)=a^2`, `w3(Q)=a^3` — ALL
THREE NONZERO (§4.2), computed by the identical ring arithmetic used for
`nu`. The machinery is not silently returning "trivial" for everything it
touches.

**(b) A formal contrary bundle.** Take a HYPOTHETICAL rank-3 real bundle
`Q'` with `w1(Q')=0`, `w2(Q')=b != 0`, `w3(Q')=0`, for a fresh formal
generator `b` with `b^2=0` (i.e. `Q'`'s classes do NOT satisfy the relations
`w2=w1^2`, `w3=w1*w2` that RP^3's actual `Q` happens to satisfy). Run the
IDENTICAL §4.3 closed form: `w2(Sym^2 Q') = w1(Q')^2+w2(Q') = 0+b = b != 0`.
**The vanishing found for RP^3's actual `Q` is a fact about `Q`'s specific
classes, not an algebraic tautology true of every rank-3 bundle** — probe
`P6b.contrary_formal`. This is the "bundle whose classes provably differ"
the brief's probe discipline asks for: same formula, different input,
different (nonzero) output.

### 4.7 Reproducing [R] the existing Part-4 branch computation and selecting the branch

`tests/dim13/mh7_dim13_link_receptacle_probe.py` Part 4 already computed
BOTH orientation branches' mod-3 homology of the fiber-link `L^9` (via the
`RP^3` `Z[Z/2]`-complex tensored with `F_3`, Serre-SS collapse certified by
exhaustive index enumeration) — but never decided which branch is real; it
left "the orientation bit `w`" as an open fork with the fiber-orientable
branch labeled `A` and the fiber-orientation-twisted branch labeled `B`.
This file's probe REPRODUCES that computation independently (same method,
freshly coded, not copy-pasted — probe `P7.R_rp3_triv`, `P7.R_rp3_sign`,
`P7.R_branchA`, `P7.R_branchB`, matching the prior probe's own certified
values exactly), then uses §4.5's result to SELECT the branch
programmatically rather than assuming it:

```
  w1(nu) = 0  =>  trivial local coefficient system on H^*(fiber)
              =>  BRANCH A (untwisted / "fiber-orientable, w trivial")
```

This is not a relabeling — `w1` of a rank-7 bundle over `RP^3` IS exactly
the classifying homomorphism `pi_1(RP^3) = Z/2 -> Z/2` that determines
whether holonomy around the generating loop preserves or reverses
orientation on `nu`, hence on `S(nu)`'s fiber `S^6`; that homomorphism
is the local system Part 4's own Serre spectral sequence used. Branch A is
selected (probe `P7.branch_selected`), and its Betti sequence
`[1,0,0,1,0,0,1,0,0,1]` matches the prior probe's certified value exactly
(`P7.branch_matches_prior_certificate`): **`H_9(L^9;F_3) = F_3 != 0` — the
mod-3 fundamental class EXISTS on the model** (`P7.H9_nonzero`). D2's
own control — "both branches must reproduce the probe's spine-transfer in
degrees <= 5" — holds for the selected branch by construction, since Branch
A's degrees 0-5 are unchanged from the reproduction.

---

## 5. What this does and does not decide, against the packet's own outcome table

The packet's outcome table row (a) reads: *"D1 green, D2 untwisted, D3
parallelizable -> receptacle route ALIVE; wave routes to D4 (O4/O5); S3
upgrades from REFEREE_CONJECTURE toward verified on the model."*

**Delivered here: D1 (green) and D2 (untwisted).** Both exactly, both by
exact computation, both cross-checked two independent ways.

**NOT delivered, and not claimed:** D3 — "stable parallelizability" of the
TRUE `S(nu)`-bundle over the full 7-dimensional `P(TX^4)` (varying over the
`X^4` base, not just at one fixed `x`), including `S^6`'s own stable normal
triviality (a separate, standard, uncomputed-here fact) and the "first
Pontryagin/Stiefel-Whitney obstructions against the fibration `S^6 -> L^13
-> P(TX^4)`" that D3(ii) names. This file's result is a NECESSARY input to
D3(i)'s "the model `RP^3 x S^6` is stably parallelizable" clause (it now
supplies GENUINE, not merely stable, parallelizability of the `RP^3` factor
— stronger than D3(i) asks for on that factor) but does not touch D3(ii)'s
global obstruction computation at all. D4 (the reframing-orbit bound), D5
(the corner type-check) and D6 (the non-additive dictionary) are entirely
untouched.

**So: outcome-table row (a) is two-thirds delivered, not fully.** The
honest statement is narrower than "the receptacle route is ALIVE per row
(a)" — it is: *the orientation-bit gate of gap O3 is now DECIDED rather
than open, in the direction that keeps the route from being closed by K2 on
this particular gate; the remaining two-thirds of gap O3 (global stable
parallelizability) and all of gaps O1, O2, O4, O5, O7, O8 remain exactly as
open as before.*

**Register/canon consequence, named but not performed.** This result is
exactly the referee content M-H5 and `explorations/mh7-dim13-restatement-2026-08-03.md`
Section 6's S3 row ask for: *"nu ~ R (+) Sym^2(Q*), triviality over RP^3,
link model RP^3 x S^6, eta-form vanishing | M-H5 REFEREE_CONJECTURE."* This
pass discharges the "triviality over RP^3" and "link model RP^3 x S^6"
clauses of S3 exactly (not the eta-form-vanishing clause, which is M-H5's
separate reflection-lemma step, unaddressed here). The integration owner's
two recommended edits, **printed, not performed** (write-scope is two paths
on a shared checkout):

- `lab/process/improvement-register-2026-08-03.md:155` (M-H5 row): mark the
  "Verify ν decomposition (half-day); SW/triviality check (hours)" clause
  DONE, citing this file.
- `explorations/mh7-dim13-restatement-2026-08-03.md` Section 6, row S3:
  upgrade from `M-H5 REFEREE_CONJECTURE` to reflect that the `RP^3`-fiber
  triviality and orientation-bit halves are now VERIFIED-on-the-model,
  citing this file; the reflection-lemma clause stays REFEREE_CONJECTURE.

No K1-K5 kill condition fires (K2's specific route — the twisted branch with
no mod-3 fundamental class — is exactly what this result excludes). Nothing
is killed; `target_claim: NONE-NOT-A-KILL`.

---

## 6. Admissibility per home — the three surviving Z/3 homes

The design packet's Lens 1: *"exactly THREE homes remain live — (i) the
framed receptacle itself ..., (ii) tmf/String as detector-or-wall ..., and
(iii) the equivariant channel."* Per home:

| home | this file's effect | admissibility after this pass |
|---|---|---|
| **(i) framed receptacle** (`Ω_13^fr = Z/3`, burden O1-O5) | DIRECT: decides D2 for this home. Orientation bit `w` = UNTWISTED; the mod-3 fundamental class of the fiber-link exists on the model; K2's twisted-branch route to killing this home is EXCLUDED. | **ADMISSIBLE, unkilled — a gate that could have fired K2 did not.** Still far from occupied: O1 (radial boundary), O2 (compactness), the global two-thirds of O3, O4 (non-product framing), O5 (nonzero PT class), O7 (order-3-to-integer bridge) and O8 (framed-inflow theory) all remain fully open. No occupant, no count, no change to that status. |
| **(ii) tmf/String** (double-gated as wall; one literature fact from checkable as detector) | NONE. This file computes no String-ness, no tmf class, no Witten genus. | **UNCHANGED.** Orthogonal to this computation entirely; still double-gated as a wall, still one flagged literature fact from a checkable detector route. |
| **(iii) equivariant channel** (Nikulin carrier-B / SG4, K3-side spacetime geometry) | NONE. Explicitly "not a dim-13 route" (Lens 1); this file's entire construction lives on the dim-13 link's normal bundle, a disjoint object from the K3-side geometry SG4 addresses. | **UNCHANGED.** The named single decider, entirely unaffected by any dim-13 orientation-bit result. |

No home changes its OCCUPANCY status (none did before, none does now — the
receptacle stays EMPTY per the Layer-0 object table). What changes is home
(i)'s gate count: one previously-open fork (D2) is now closed in the
route-preserving direction, sharpening "located, not measurable" without
converting it into "occupied."

---

## 7. Mid-flight addition — Joe's question, via the session owner

*Does the Z/3 receptacle work carry the source's 2+1 imposter structure, or
presuppose three interchangeable generations?* Three typing-only items,
addressed in the order asked, no new computation, no scope growth.

### 7.1 Re-verifying the packet's five hinge/2+1 kills against the post-08-11 record

The packet's kill list, verbatim (`lab/process/hinge-panel-synthesis-2026-08-03.md:107-111`):

> HINGE AS COUNT: dead FIVE ways — the standing Rung-1 fence; the coboundary
> theorem (the defect is δR, exact, class zero — no protected quantity can
> ever come from it, L9); the Euler-degree kill (the graded contribution
> lives in degree rank N = 10 > 4 = dim X, L9, modulo the :24 grading fork);
> legb2's computed (0,0,0) (L3); and phenomenologically PH-K1 (the block
> as-is gives a VECTORLIKE third family — two chiral + one vectorlike is
> anomalous and contradicted by measured V−A currents, L6).

Checked each against `he1-imposter-separation-invariant-2026-08-14.md`,
`crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md` and
`st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md` directly (read in
full this session, not from the relayed paraphrase):

| # | kill | ground | status |
|---|---|---|---|
| 1 | **Rung-1 fence** — net chiral index is grading-determined, unmoved by any coefficient; three RS blocks contribute zero | a fact about the RS/`ker Gamma` 4+10-split's THREE BLOCKS (`192+192/576+576/64+64`) | **SURVIVES.** Not mentioned, referenced, or recomputed by HE-1, CR-B or ST-1 — none of the three operates on the RS block decomposition at all. |
| 2 | **coboundary theorem** — the interface defect is `δR`, exact, class zero | a cohomological statement about the hinge/interface object | **SURVIVES.** A disjoint mathematical object (a coboundary class) from anything HE-1/CR-B/ST-1 compute (Pati-Salam branchings, `D_7` centre classes, `Sym^2/Λ^2` splits). Untouched. |
| 3 | **Euler-degree kill** — the graded contribution lives in degree `N=10 > 4=dim X` | a degree-counting argument on the hinge construction | **SURVIVES.** Same object family as #2; no post-08-11 file recomputes or references it. |
| 4 | **legb2's computed `(0,0,0)`** — cross-term index classes, identically 3-primary-inert | `tests/escape-corners/legb2` (2026-07-10), recorded in `hinge-panel-synthesis` | **SURVIVES — by silence, not reuse.** Checked directly: `legb2` is mentioned in NEITHER HE-1 NOR CR-B NOR ST-1 (grepped; zero hits in all three). It predates the packet by weeks and nothing in the post-08-11 record touches it. |
| 5 | **PH-K1 vectorlike** — the `Cl(9,5)` 128 block is kinematically vectorlike, `64+64` | `PH-K1-KINEMATIC`, draft §9 | **SURVIVES — and is independently REAFFIRMED, not superseded.** HE-1 explicitly cites it as a THIRD independent arrival at the same conclusion (*"corroborates ... the theme already established by `PH-K1-KINEMATIC` (draft §9) and the Witten-1983 class burden"*); CR-B's own prior-art table lists it `CONFIRMED`, unchanged. |

**All five SURVIVE.** None is superseded. The reason is structural, not
coincidental: HE-1/CR-B/ST-1 run a DIFFERENT, LATER, non-overlapping
mechanism — a Pati-Salam branching of the `16` against a newly-constructed
`144` (HE-1's own object, source-attested via `WG-P03`), producing a
SUBTRACTIVE `n_g -> n_g-1` partition, entirely distinct from the hinge/RS
4+10-split "count from a locus" mechanism the five kills attack. HE-1's own
Fence 3 states this precisely: *"no count here is a generation count ...
The repository count remains at `{1, 3}` and is untouched."* This is a
**dated flag for the integration owner**, not a license to reopen the hinge
route: no disposition, register row, or canon status changes here, and this
file performs no re-litigation of any of the five.

### 7.2 The claim ceiling, with the layer structure and TWO named obstructions

**Layer.** The bit this file computes binds the RECEPTACLE question only —
whether a coefficient-group slot (`Ω_13^fr = Z/3`) stays gate-open — and
says nothing about occupancy, and nothing about which of the source's own
generation-structure layers (declared total / pullback / ± package /
observed-VEV-conditional, per CR-B's own four-layer vocabulary) a future
occupant would belong to.

**Two obstructions, not one, for any future bridge from this bit to an
integer generation count:**

1. **The banked one.** `Hom(Z/3,Z) = 0` (`GEOMETER-VS-PHYSICS-OBJECTS.md`,
   `canon/ko-degree-obstruction-ladder-RESULTS.md`): no additive map from a
   Z/3-valued class to an integer exists. A non-additive dictionary (the
   packet's B4/D6) would be needed, and none is built.
2. **The new one, from Joe's question.** The source's own generation
   structure is ASYMMETRIC: HE-1 computes a SUBTRACTIVE `n_g -> n_g-1`
   partition (2+1, one representation-theoretically distinguished,
   UNLABELLED block that is REMOVED, not made different-but-light); CR-B
   independently confirms the source declares an opposite-half PACKAGE with
   a distinct spin-3/2-adjacent imposter sector (`SC-GEN-56`, the source's
   own `Omega^0(S+) (+) Omega^1(S-)` reading), never three symmetric
   copies. But `Z/3` as a bare cyclic group carries NO privileged element:
   `Aut(Z/3) = Z/2` acts transitively on its two nonzero elements (swapping
   `1 <-> 2`, fixing `0`), so nothing internal to the group structure can
   distinguish "two alike + one different." **A symmetric receptacle
   cannot, by itself, express an asymmetric 2+1/imposter structure without
   additional structure nobody has built** — a representation, a marked
   point, or some finer invariant than group order. This is a structural
   observation about `Aut(Z/3)`, not a new theorem about GU; it is
   hostile-reviewed at §8.6 for overclaim.

Both obstructions are independent (neither implies the other: a
non-additive dictionary could in principle exist while still being
symmetric under `Aut(Z/3)`, and a `Z/3`-asymmetric structure could in
principle be built without solving `Hom(Z/3,Z)=0` — e.g. a bridge that
lands in a `Z/3`-REPRESENTATION rather than the bare group). Any future
work claiming to bridge this receptacle to "three generations" must clear
BOTH.

### 7.3 Does the referee decomposition or the three-home shortlist assume generation-interchangeability?

**Checked directly, not from memory of the packet's own fence. No.**

- **The decomposition (§4.1-4.5).** `nu`'s entire construction is built from
  `l` (the tautological line in `T_x X^4`) and `Q` (the quotient bundle) —
  the projectivization of a single 4-dimensional real vector space, namely
  the tangent space to SPACETIME at a point. No fermion field, no spinor
  bundle, no gauge-group representation, no family index, and no object
  indexed by "generation" appears anywhere in `nu`'s definition, in `Q`'s
  definition, in `Sym^2(Q^*)`'s definition, or in either derivation of
  `w(Sym^2 Q)` (§4.3, §4.4). This is differential topology of `Met(X^4)`'s
  fibration, entirely prior to and independent of any fermion content —
  exactly the packet's own Layer-0 table entry for "receptacle": *"the
  address where a homotopy-theoretic count datum could live ... identical
  in a one-generation universe."*
- **The three-home shortlist (§6).** Home (i) (`Ω_13^fr`) is a stable
  homotopy group of spheres — no representation content. Home (ii)
  (tmf/String) is a genus/bordism-detector question — the packet's own text
  flags, rather than assumes, the missing bridge (*"there is NO theorem
  equating the Witten genus with the net-chiral count"*). Home (iii) (the
  equivariant channel) is the one place generation-adjacent representation
  content genuinely enters (a `Z/3` action on K3-side spacetime geometry),
  and the packet explicitly TYPES it as out-of-scope for the receptacle
  program rather than folding it in silently: *"it is not a dim-13 route; a
  wave choosing it is choosing the decider, not the receptacle program."*
  That is a scope fence, not a smuggled assumption.

**Where I checked:** the packet's D1 statement and Layer-0 object table
(`explorations/z3-receptacle-design-packet-2026-08-11.md`, "receptacle"
row); the register M-H5 row and Wave C's own fixed-`x` framing
(§3 above); and Lens 1's three-home table in full. No sentence in any of
these introduces a fermion, a family, or an assumption that the three
generations are interchangeable.

---

## 8. Hostile review, inline

**Charge 1 — is "genuinely trivial" an overclaim relative to what D1 asked
for?** No: D1 explicitly asks for `w1=w2=w3=0` AND "the relevant
rank-at-least-four classification" — the packet itself frames the SW
computation as a step TOWARD triviality, not the end state. §4.4 supplies
the missing classification step (cancellation theorem, hypothesis verified
exactly: `7 > 3`) using STANDARD, cited (not re-derived) machinery. If
anything this delivers slightly MORE of D1 than the bare "compute w1,w2,w3"
reading requires, not less.

**Charge 2 — does reusing `T(RP^3)`'s parallelizability smuggle a fact
about `S^6` that hasn't been checked?** No — and this matters, because D3
explicitly flags `S^6`'s stable normal triviality as a SEPARATE, uncomputed
fact `[for independent citation-check]`. Nothing in §4.4 uses any property
of `S^6` at all; `S(nu)`'s fiber being `S^6` is a CONSEQUENCE of `nu`
having rank 7 (unit sphere in `R^7`), not an input to the triviality
argument. This file computes zero facts about `S^6` itself and claims none.

**Charge 3 — is the branch-selection argument (§4.7) circular, i.e. does it
assume the answer it derives?** No: the local-system/branch-selection rule
(`w1(nu)=0 => untwisted`) is stated and justified BEFORE `w1(nu)`'s value is
known (it is a general fact about any rank-7 bundle's sphere-bundle
monodromy over `pi_1=Z/2`), and `w1(nu)=0` is derived independently in §4.3
and §4.4 with no reference to the branch question. The mutation
`wrong_branch_selector` (§6, probe self-test) proves the selection logic is
load-bearing: inverting it (selecting B when `w1=0`) is caught by 3 failing
checks, confirming the selection is not vacuous.

**Charge 4 — does §7.2's `Aut(Z/3)` argument overclaim a theorem about GU?**
Checked directly. It does not assert GU's generation structure IS `Z/3`-typed
or that any specific bridge fails — it asserts a narrower, purely
group-theoretic fact (`Aut(Z/3)=Z/2` acts transitively on the nonzero
elements) and draws the conservative consequence: a bridge into the BARE
group cannot express asymmetric structure WITHOUT ADDITIONAL DATA. It
explicitly does not rule out a bridge into a `Z/3`-REPRESENTATION or some
other richer object (§7.2, penultimate paragraph) carrying that data. This
is typed as a structural observation, not a no-go, and no register/canon
disposition rests on it.

**Charge 5 — does §7.1's SURVIVES table quietly resurrect the hinge/2+1
route by cataloguing it favorably?** No: every row's "SURVIVES" verdict is
grounded in NON-CITATION (the post-08-11 files simply do not mention the
object), not in any re-verification or re-endorsement of the kills
themselves. This file re-derives nothing about the hinge construction,
recomputes no coboundary class, no Euler degree, and no `legb2` index. The
five kills are recorded as unmoved, which is the opposite of resurrecting
them.

**Charge 6 — the deepest available attack: is `Q^* =~ Q` really an honest
isomorphism, or does it hide a sign/orientation subtlety that would flip
`w1(nu)`?** Checked: SW classes are, by construction, insensitive to which
of the (many, metric-dependent) isomorphisms `Q -> Q^*` is chosen — `w_i(E)
= w_i(E^*)` for every real vector bundle `E`, a completely general fact
independent of the metric used (transition functions of `E^*` are the
INVERSE-TRANSPOSE of `E`'s; over `F_2`, `w_i` of a bundle and its dual
always coincide, with no sign ambiguity since there are no signs in `F_2`).
So even setting aside the specific metric-existence argument in §4.5, the
class-level conclusion `w(Q^*) = w(Q)` is unconditionally true. No seam
here.

**Strongest remaining seam, stated plainly.** The literal text of D2 says
"over `P(TX^4)`" — the full 7-dimensional total space, not the fixed-`x`
`RP^3` fiber this file (and the existing Part-4 probe it reproduces)
actually computes on. §3 and §9 address this as a scope clarification
rather than papering over it, but a reader who takes D2's prose at face
value without reading M-H5's "at fixed x" framing or Part 4's own scope
could reasonably expect a global computation this file does not deliver.

---

## 9. Was the packet's spec followed or reinterpreted? — blunt

**Followed, with one named scope clarification, not a silent
reinterpretation.** D1 is delivered exactly as written, and slightly
exceeded (genuine triviality, not just the bare `w1=w2=w3=0` request,
because the packet's own third clause — "the rank-at-least-four
classification" — asks for exactly that upgrade and I supplied it). D2's
SUBSTANCE — "Probe Part 4 (P5) already gives the exact fork ... this single
bit decides" — is delivered exactly: the fork is the existing Part-4
computation, reproduced independently, and the bit is `w1(nu)`, computed
and used to select the branch programmatically rather than by assertion.

The one place I diverged from D2's LITERAL prose is the "over `P(TX^4)`"
phrase, and I want to be direct about why rather than let it pass silently:
that phrase, read at face value, names the full 7-dimensional total space,
which is D3's object (priced separately, "model then bundle," and
explicitly NOT the object Probe Part 4 — the instrument D2 itself names as
already giving "the exact fork" — computes on). Probe Part 4 is scoped to
the fixed-`x` `RP^3` fiber; M-H5's own register pricing ("Verify ν
decomposition ... SW/triviality check") is fixed-`x`; and the packet's own
"hours-scale" cost estimate is affordable only for the fixed-`x`
computation, not a global obstruction sweep over `P(TX^4)` (that would be
D3, priced as "model then bundle," i.e. more expensive and explicitly a
later step). Given the instrument D2 itself cites is fixed-`x`, I read D2's
"over `P(TX^4)`" as the packet's own slight telescoping of the fiberwise
object into the global one it will eventually sit inside — a loose sentence
in an otherwise precise packet, not a second, larger task hidden inside D2.
I resolved it toward the object the packet's own cited instrument and
register pricing agree on, and I am saying so explicitly (here, and in §3
and §5) rather than letting a reader assume D2's global reading was
silently satisfied. If the executing wave's intent was in fact the full
global bundle, that is D3, unaddressed here, and this file's §5 already
states that boundary precisely.

The mid-flight addition (§7) was executed exactly as scoped by the
session-owner's three numbered items: typing only, no new computation
(§4's arithmetic is untouched by §7), and no scope growth (no register row,
canon entry, or disposition moves).

---

## 10. `gu-typed-objects` declaration

```gu-typed-objects
result:         w1(nu)=w2(nu)=w3(nu)=0 for nu=R(+)Sym^2(Q*), rank 7, over
                RP^3; orientation bit w = UNTWISTED (branch A); nu is
                GENUINELY trivial (not merely SW-trivial), by two
                independent methods.
carrier:        nu = R (+) Sym^2(Q*) over RP^3 = P(R^4), the metric-fiber
                spine at fixed x in X^4 (Wave C's nu_x, register M-H5)
                LAYER=ambient CHIRALITY=N/A
pairing:        NONE
real_structure: real vector bundle, F_2 (Stiefel-Whitney) coefficients
                throughout; no complex or quaternionic structure enters
                anywhere in the construction
grading:        H^*(RP^3;F_2) = F_2[a]/(a^4), cohomological degree 0..3
action_owner:   repository-construction (Wave C's typed normal-bundle
                referee target, register M-H5; this pass discharges the
                decomposition and SW/triviality clauses of it)
target:         total Stiefel-Whitney class w(nu) in H^*(RP^3;F_2), and the
                induced branch selector for the mod-3 homology of S(nu)
                MAP-TYPE=evaluation
```

---

## 11. POSTFLIGHT — six lenses, run after the build

**Lens 1 — measurement integrity.** Every number in this file is produced
by the probe (`tests/channel-swings/joe_directed_z3r1_nu_trivial_w_untwisted.py`),
not by hand-transcription: 62/62 checks in the normal run, 33/33 in the
clean self-test baseline, 10/10 mutations caught. No float is load-bearing
anywhere (the probe never introduces one; all arithmetic is over `F_2` or
plain integers). The rank arithmetic (`1+6=7`, `C(3+1,2)=6`, `1+3+6=10`) and
the polynomial identity (§4.3) are each asserted exactly, not approximated.

**Lens 2 — epistemic honesty about scope.** §5 states plainly that this
file delivers two of the outcome table's three row-(a) conditions, not all
three, and names exactly what D3/D4/D5/D6 still owe. §9 states plainly
where D2's literal text was read narrowly, and why, rather than letting a
generous reading pass unexamined.

**Lens 3 — actionability.** Two concrete, printed (not performed) register
edits are named in §5 for the integration owner. §7.1's per-kill table is a
worklist an integration owner can act on directly (nothing to do — all five
survive) without re-deriving anything.

**Lens 4 — non-interference.** This artifact writes exactly two files. It
moves no verdict, no register row, no canon entry, no priority, no
disposition of the hinge/2+1 count, and no status of `SC-GEN-53`/55/56.
`canonical_effect: pending_integration` throughout; `target_claim:
NONE-NOT-A-KILL` — nothing here kills anything, in the base task or the
mid-flight addition.

**Lens 5 — the hazard, re-checked at exit.** `SC-GEN-01` and `SC-GEN-04`
remain `disavowed-by-source`; re-reading this file's own §4 construction at
exit confirms (again, mechanically, via the probe's `P8.scgen01_*`/
`P8.scgen04_*` checks) that neither disavowed reading is asserted, quoted
approvingly, or presupposed anywhere. The receptacle stays EMPTY. No count
is derived, suggested, or upgraded — `CURRENT-STATE.yaml`'s fence holds.

**Lens 6 — decay.** This file's mathematical content (§4) will not go
stale — it is an exact, reproducible computation on a fixed bundle. Its
mid-flight section (§7) is explicitly a SNAPSHOT against the record as of
this session; if a future artifact supersedes HE-1, CR-B or ST-1, §7.1's
SURVIVES table would need re-running, exactly as this session re-ran AR-1's
row-6 typing rather than trusting it unchecked (§2). The probe is the
re-run mechanism: its file-level checks (§8 of the probe) will go red the
moment any of the quoted substrings changes underneath it.

---

## 12. Certificate

- Probe: `tests/channel-swings/joe_directed_z3r1_nu_trivial_w_untwisted.py`
- **62/62 checks, exit 0.** Breakdown: 2 splitting-principle identity
  checks (PART 1); 5 ring/derivation checks (PART 2-3); 4 independent
  cross-check checks (PART 4); 7 assembly/rank checks (PART 5); 2 contrary-
  control checks (PART 6); 5 planted-false-fact checks, all correctly
  observed False; 8 reproduction/branch-selection checks (PART 7); 24
  file-level textual verification checks (PART 8), spanning the packet,
  register, `CURRENT-STATE.yaml`, `GEOMETER-VS-PHYSICS-OBJECTS.md`, the
  source-claim register, Wave C, AR-1, `hinge-panel-synthesis`, HE-1, CR-B
  and ST-1 (5 of these 24 are the mid-flight addition's file-level checks).
- `--selftest`: clean baseline verified FIRST (33/33, the non-file-level
  checks), then **10/10 planted machinery-corruption mutations each drive
  a genuine named `[FAIL]` line — none crash.** Mutations: wrong `w(gamma)`,
  wrong closed-form coefficient, wrong `T(RP^3)` exponent, wrong
  `Sym^2` rank formula, spurious dual-class flip, inverted branch selector,
  mod-3 (not mod-2) polynomial engine, inverted degree-1 expectation,
  inverted contrary-control expectation, and a dropped mod-2 reduction in
  the ring multiplication.
- Prior art re-run fresh this session: `tests/dim13/mh7_dim13_link_receptacle_probe.py`
  — exit 0, all checks pass (the reproduction in §4.7/PART 7 above is
  verified against a LIVE, not stale, prior probe).
- `python3 lab/process/novelty-check.py "Sym^2(Q*) Stiefel-Whitney" "w1=w2=w3=0 nu RP3" "Sym^2 Q trivial RP^3"`
  run before any novelty claim: zero EXACT hits for the actual computation
  on any of the three phrasings; the only NEAR/co-occurrence hits are this
  file's own new probe and the packet/register files already cited as the
  computation's own source. What is claimed new is the EXECUTION of a
  previously-typed-but-unproved precondition (Wave C's own words: "one must
  prove ..."), not the underlying mathematics (splitting principle, `RP^n`
  characteristic classes, Lie-group parallelizability are all textbook).
- No git command was run. No file outside the two named paths was
  modified. The routing notice above is copied verbatim from
  `lab/methods/source-native-comparator-routing.md` (byte-checked by the
  probe's file-read machinery reading the same source this file quotes).
- **Repository gates re-run after writing, on the live shared checkout:**
  `typed_carrier_declaration_audit` — this file's `gu-typed-objects` block
  validates clean (not in the red list); gate reports 1 pre-existing RED on
  a concurrently-written sibling
  (`explorations/conditional-build/selected-k151-moving-distortion-pairing-adjoint-2026-08-17.md`),
  not this file's and not touched.
  `source_native_comparator_routing_audit` — goes from 5 to **6**
  UNCLASSIFIED (baseline 5), this file listed by name — the exact,
  precedented consequence of the two-file write scope (FX-2 hit "6
  unclassified > baseline 5" identically); the required registry line is
  printed verbatim at the top of this file, not performed.
  `kill_target_claim_audit` — 3 red, unchanged from the pre-existing
  scope-baseline of 3; this file is not among them (`target_claim:
  NONE-NOT-A-KILL` is honored).
  `certificate_shape_audit` — RED, but on `LIBRARY_ALLOWLIST` drift for
  `k149_sparse_differential_jet_api.py`/`k150_moving_selected_shiab_coordinate_adapter.py`
  (an unrelated subsystem this pass never touched); the same class of
  ambient, pre-existing gate drift `explorations/mh7-dim13-restatement-2026-08-03.md`
  itself already reported at clean HEAD ("independent of this work ...
  belongs to the active resolver thread whose commits created the drift").
  This file appears in none of its failure output.
