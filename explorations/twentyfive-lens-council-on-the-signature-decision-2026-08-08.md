---
artifact_type: exploration_result
created: 2026-08-08
status: COUNCIL_CONVERGES_ON_PARITY__(7,7)_IS_THE_ONLY_HORN_WHERE_THREE_IS_REACHABLE__SIGNATURE_BLINDNESS_IS_A_THEOREM__FOUR_LENSES_DISSENT
grade: "MIXED BY CONSTRUCTION and labelled per lens. Each lens self-declares ACTUAL
  MATH or ANALOGY and a confidence. The mod-8 / Kramers / Majorana-Weyl content is
  exact and certified in tests/majorana_weyl_forces_the_seven_seven_horn.py. The
  networking, distributed-systems and MMO lenses are ANALOGY and are marked as
  such; they are included for process diagnosis, not physics."
canon_verdict_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - tests/majorana_weyl_forces_the_seven_seven_horn.py
  - lab/sources/curt-iceberg-77-primary-transcript-fetch-2026-08-08.md
---

# Twenty-five lenses on the `(7,7)` vs `(9,5)` decision

The decision: fibre pinned at `(6,4)`; base `(3,1)` gives ambient `(9,5) = M(64,ℍ)`
quaternionic; base `(1,3)` gives `(7,7) = M(128,ℝ)` real. Weinstein says base
`(1,3)`; the repository computes on `(3,1)`.

Each lens declares **ACTUAL MATH** or **ANALOGY**, and a confidence.

---

## Cluster A — reality, parity, and the count (the spine)

**1. Clifford algebraist.** `p−q mod 8` is a complete invariant of the real class.
`(7,7)→0→M(ℝ)`; `(9,5)→4→M(ℍ)`. Not real-isomorphic; nothing transfers.
→ **ACTUAL MATH, confidence very high.**

**2. Majorana–Weyl / spinor reality.** Real chiral spinors exist iff `p−q ≡ 0 mod 8`.
Among the horns GU's 4+10 split can reach — `(9,5)`, `(7,7)`, `(5,9)` — only `(7,7)`
qualifies. With the fibre pinned, **the MW requirement forces the horn outright.**
→ **ACTUAL MATH, very high.** *This is the strongest single result in the council.*

**3. Kramers / antiunitary structure.** `J² = −1` forces even-dimensional
eigenspaces. On `(9,5)` every GU-native Hermitian carrier has even signature —
already canon (`no-go-quaternionic-parity-generation-sector.md`). On `(7,7)`, real
structure means `J² = +1` and the doubling does not apply.
→ **ACTUAL MATH, very high.**

**4. Parity arithmetic (the punchline).** Three generations is an **odd** count.
Quaternionic ⇒ even ⇒ **3 is structurally unreachable on `(9,5)`**. Real ⇒ odd
permitted ⇒ 3 is reachable on `(7,7)`. The two horns are not
aesthetically different; **one of them forbids the target number.**
→ **ACTUAL MATH, high.** The residual is whether GU's count really is this index.

**5. KO-theory / Bott.** Mod-8 periodicity is why any of this is discrete.
`KO⁰` gives a `ℤ`-valued index; the quaternionic class lands in an even subgroup.
Same conclusion as 3–4 from a different direction, which is worth something.
→ **ACTUAL MATH, high** on periodicity; **medium** on the precise index-group label.

**6. Random matrix theory (Dyson).** Real symmetric = β=1 (GOE); quaternionic
self-dual = β=4 (GSE), where **every level is Kramers-doubled**. The fork is a
Dyson-class fork, and β=4's doubling is the same even-parity fact again.
→ **ACTUAL MATH** for the classification, **ANALOGY** for any spectral-statistics
claim about GU. **Medium.**

**7. Condensed-matter topological classification (Altland–Zirnbauer).** Which
topological invariants exist — `ℤ`, `ℤ₂`, `2ℤ`, or nothing — is fixed by the
reality class. A count living in `2ℤ` can never be 3. This is the tenfold way
making the same point as 4, and it is the standard machinery for exactly this
question.
→ **ACTUAL MATH, high** in general; **medium** that GU's count sits in this table.

---

## Cluster B — the math Joe named as absent

**8. Complex analysis / Wick rotation.** Each rotated coordinate shifts `p−q` by
±2. `(9,5)` and `(7,7)` differ by 4, so they are **exactly two Wick rotations
apart** — not adjacent, not the same point. Reality type changes across it, so
this continuation is *not* innocuous.
→ **ACTUAL MATH** for the count; **ANALOGY** for physical meaning. **High/low.**

**9. Signature-blindness (the sharpest negative result).** `Cl(p,q) ⊗ ℂ` depends
only on `p+q`. **Both horns complexify to `M(128,ℂ)`.** Therefore *any* complexified
computation is provably incapable of deciding this fork. That is why the
Racah–Speiser module returned bit-identical output on both horns — **a theorem, not
a bug**, and `M-H9` was mis-specified for a reason that was predictable in advance.
→ **ACTUAL MATH, very high.** *Most immediately useful lens for triage.*

**10. Steepest descent / Picard–Lefschetz.** The conformal mode carries negative
norm (computed: spatial block `(5,1)`), and the standard treatment is the
Gibbons–Hawking–Perry contour rotation of exactly that mode. **Curt's "the trace
contributes either `(1,0)` or `(0,1)` depending on a choice" is that same conformal
direction.** So the trace-line choice may be a *contour* choice, not a signature
choice — which would reframe the fork entirely.
→ **ANALOGY, but a load-bearing one. Medium confidence, high value.** The single
most promising unexplored lead here.

**11. Path-integral measure.** The DeWitt measure on `Met(X)` is built from the
supermetric whose sign is the fork. Whether the measure is even well-defined
differs between horns. Nobody has written it.
→ **ANALOGY** as applied; **medium-low.**

**12. Stochastic processes.** A probability measure needs Euclidean signature.
**Both horns are indefinite, so neither admits one.** This lens honestly does
*not* discriminate — and saying so is its contribution.
→ **ACTUAL MATH, high confidence — that it does not decide.**

**13. Constructive/Osterwalder–Schrader.** Reflection positivity is a *reality*
condition on a real pairing. It is the kind of axiom that can see the fork, and it
has never been attempted here.
→ **ACTUAL MATH** in principle, **unapplied. Low** confidence, **high** value.

---

## Cluster C — physics

**14. General relativity / ADM.** The `(5,1)` spatial block is the classical
Wheeler–DeWitt supermetric signature, recovered exactly. Strong evidence the
construction is standard and the fibre `(6,4)` is right.
→ **ACTUAL MATH, high.**

**15. Supergravity.** MW spinors are the standard chirality carrier; `(7,7)`
supplying `64+64` real halves is the familiar pattern, and 64 is the draft's own
printed multiplicity.
→ **ACTUAL MATH** for the dimensions; **ANALOGY** for the inference. **Medium-high.**

**16. Anomalies.** Real vs quaternionic changes which anomalies can appear at all.
An anomaly-cancellation condition would be a *physical* discriminator, unlike any
convention argument. Not attempted.
→ **ACTUAL MATH** in principle. **Low** confidence, **high** value.

**17. Pati–Salam / GUT.** Weinstein's own stated criterion: the trace sign is the
one making `Spin(6)×Spin(4)` natural "rather than the `Spin(10)`, `SU(5)` line."
`Spin(6)×Spin(4)` against a `(6,4)` fibre is not a coincidence.
→ **ACTUAL MATH** that the groups match; **ANALOGY** that this selects. **Medium.**

**18. Cosmology / signature change.** Literature exists on dynamical signature
change (Hartle–Hawking, Ellis). If the horn were dynamical rather than fixed, the
fork dissolves into a different question.
→ **ANALOGY. Low.** Included because nobody has asked it.

**19. Effective field theory.** A UV convention that leaves no IR trace is not
physics. **Ask what observable differs between horns** — and the parity of the
generation count is precisely that. This lens says lens 4 is the *only* one that
has produced a real observable so far.
→ **ACTUAL MATH** as a criterion. **High.**

---

## Cluster D — pure math

**20. Number theory / quadratic forms.** Signature is a complete invariant over `ℝ`
but not over `ℚ`; and it is *invisible* after complexification (lens 9). So any
rational or complex method is the wrong tool by construction.
→ **ACTUAL MATH, high.**

**21. Category theory / functoriality.** The construction `g ↦ g ⊕ G(g)` is not
functorial in the base sign — the fibre does not follow. A construction that is not
natural in its input is a construction with an undeclared parameter.
→ **ACTUAL MATH, medium-high.** (Earlier over-read as a defect; the two-orbit
statement is the correct form.)

**22. Homogeneous spaces.** `O(3,1) = O(1,3)` as a subgroup condition, so `F ≃ RP³`
is the same on both horns — already filed. **The fibre is signature-robust; only
the ambient reality moves.** Usefully narrows where a discriminator can live.
→ **ACTUAL MATH, high.**

**23. Proof theory / logic.** The MW result is a **conditional**: *if* the carrier
must be real, *then* `(7,7)`. That is a well-formed ledger entry. The failure mode
all day has been promoting conditionals to settlements.
→ **NEITHER — methodological. High.**

---

## Cluster E — the technical lenses (all ANALOGY, and useful anyway)

**24. Network engineer — endianness.** The notation mirror is a **byte-order
problem**: `(p,q)` vs `(q,p)` is big- vs little-endian for signature, and mixing
them inside one sum is exactly a wire-format bug. Networking solved this by
defining a canonical order and converting at every boundary. **The repository has no
declared wire format for signature pairs, and that is precisely how Wave K's
mixed sum survived four days.**
→ **ANALOGY, but the prescription is concrete and correct. High value.**

**25. Distributed systems / MMO netcode.** Two replicas — the 2021 draft and the
iceberg transcript — held different states with no reconciliation protocol, and the
repository read from the wrong one. In MMO terms: **the expositor is client-side
prediction; the author is the authoritative server.** The repo treated a client
prediction as authoritative and never rolled back. `SIGNATURE_AMBIENT_K77` is a
**foreign-key violation** against the registry, and the red gate is the integrity
check firing correctly and being ignored.
→ **ANALOGY. Zero physics content. But it names the process failure exactly**, and
the fix — declare an authority, reconcile on divergence, honour the constraint —
is actionable today.

---

## Where the council converges

**On the math: `(7,7)`, and not narrowly.** Lenses 2, 3, 4, 5, 6, 7 reach it
independently through Majorana–Weyl, Kramers, parity, Bott, Dyson and AZ. The
convergence is not luck — they are all consequences of one mod-8 reality fact. The
decisive form is lens 4: **`(9,5)` forbids an odd generation count; `(7,7)` permits
it.** Weinstein's `(1,3)` and Curt's split are consistent with this, and the
repository's `(3,1)` is the horn on which three generations cannot exist.

**On coherence — the picture is missing three things.**

1. **A declared wire format for signature pairs** (lens 24). Cheapest, and it
   retires an entire error class.
2. **A discriminator that touches reality structure** (lens 9). Anything
   complexified is *provably* incapable. That kills a category of future attempts
   in advance and should be written into the register as a screening rule.
3. **The contour question** (lens 10). If the trace-line sign is a Picard–Lefschetz
   contour choice rather than a signature choice, the fork is not a fork. **This is
   the most valuable unexplored lead in the council** and sits in exactly the
   complex-analytic territory recorded as having zero prior coverage.

**Four lenses dissent or decline**, and they matter: **12** (stochastic — cannot
discriminate, both indefinite), **18** (cosmology — low), **11** (measure — low),
and **25** (netcode — no physics content). A council where everything agrees has
not been assembled honestly.

**Analogy vs actual math, tallied.** Nine lenses are actual math at high or very
high confidence (1, 2, 3, 4, 9, 12, 14, 20, 22). Six are actual math at medium (5,
6, 7, 15, 17, 21). Four are principled but unapplied, so low confidence and high
value (10, 13, 16, 18). Two are pure analogy (24, 25). One is methodological (23).
**The `(7,7)` conclusion rests entirely on the first group**; the analogies added
process diagnosis and one genuine research lead, and nothing else.
