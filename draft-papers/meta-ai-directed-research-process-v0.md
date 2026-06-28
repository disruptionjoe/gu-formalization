---
title: "Directing an AI research process toward serious mathematics: a case study in the matter sector of Geometric Unity"
status: draft-v0
doc_type: meta_paper
created: 2026-06-28
complete_after: "the object-level generation-sector result stabilizes (multiplicity theorem / Krein synthesis / six-axis candidate)"
audience: "to decide -- blog essay first, with an arXiv note + an AI-for-science venue paper as spin-outs (see Sec. 7)"
---

# Directing an AI research process toward serious mathematics

*Draft v0. This is a scaffold to be completed once the object-level result it reports on has stabilized.
The object-level mathematics is reconstruction-grade and conditional; this paper's claim is about the
**process**, not about Geometric Unity being right. Every section marked TODO is a placeholder.*

## 0. The claim (hedged on purpose)

I built and directed an AI-assisted research process that **appears capable of producing serious
mathematical work**. "Appears" and "serious" are both load-bearing and both deliberately weak:

- **Appears** -- this is a single case study, not a controlled result. It is evidence that the process can
  do real work, not proof that it reliably does, and not a claim that it did so unsupervised.
- **Serious** -- the strongest evidence is not that the process produced a striking positive claim. It is
  that the process **killed its own headline claim** when an external reviewer pointed at the weak spot,
  and then found something more interesting underneath. Self-refutation under adversarial pressure is the
  behavior that distinguishes research from generation.

The case study is an audit of the matter (generation) sector of Geometric Unity (GU). I am not a
physicist; I directed the process, set its discipline, supplied the adversarial reviews, and made the
judgment calls. The process did the computation and the proof-search.

## 1. Why this case is a fair test

GU is a good stress environment for the claim precisely because it is **hard and unsettled**: it has no
complete published formalization, its strongest critic (Nguyen) has a live unanswered critique, and the
relevant no-go theorems (Distler-Garibaldi) are real obstructions. A process that only paraphrases
settled results would have nothing to bite on here. The questions are open, the failure modes are
many, and an overclaim is easy to make and easy to catch.

The discipline I imposed, stated once and held throughout: **compute, then adversarially verify, then
land only what survives. Attack, do not defend. Honesty over hype.** Concretely, every candidate claim
was attacked -- by the process against itself, and by independent external review agents -- until it
either survived re-checking or was falsified and retracted.

## 2. What the process actually produced (the evidence)

TODO: finalize once the object-level result stabilizes. Current state of the artifacts:

- **A machine-checked reconstruction** of GU's Rarita-Schwinger sector as a real `Cl(p,q)` Clifford
  module (`p+q=14`), carrying the verified Pati-Salam `Spin(2k)` chain that fixes the structure of one
  Standard-Model generation. Anchored by two scalar invariants asserted as guards in every script.
- **A sharp multiplicity theorem** ("GU fixes one generation's structure but not the count; a count of 3
  is equivalent to importing the prime 3") -- which the process then **refuted** (see Sec. 3).
- **The replacement, more interesting finding**: GU's own self-dual geometry (the rank-3 `Lambda^2_+` of
  any 4-base) carries a multiplicity-3 generation family natively; the count was never the issue, the
  *chirality* of the family is.
- **A synthesis** linking the resulting structure (an indefinite-metric / Krein matter space with
  generation-mirror "ghost" pairs) to Turok-Bateman's independently-proposed ghost-parity quantization of
  quadratic gravity. The matter-sector chirality problem and the quantum-gravity positivity problem turn
  out to be the same problem.
- **A typed no-go candidate**: the first inside-the-single-group-class candidate evasion of
  Distler-Garibaldi the program had, via a state-space-positivity axis -- adversarially verified, and
  honestly carrying its own most-likely-to-kill condition.

All numerical claims are reproducible scripts under `tests/generation-sector/`; all prose claims carry an
explicit solid / conditional / refuted scope.

## 3. The load-bearing episode: the process killed its own result

The centerpiece of the case is not a theorem. It is a retraction.

The process had committed a paper whose sharp headline was "no GU-native mechanism produces the generation
count 3; a 3 must be imported from outside." Two independent external review agents were given the paper
and asked to break it. The second one found the load-bearing logical gap: the result leaned on a
total-dimension fact (`ker = 2^7 * 13`, which is 3-free) as if it controlled a *branching multiplicity*,
which it does not. It then named the exact computation that would kill the claim: a self-dual `SU(2)`
family symmetry whose triplet could carry a multiplicity of 3.

The process ran that computation against its own paper. The kill **landed**: the generation does sit in a
GU-native multiplicity-3 triplet. The headline was false. Rather than defend it, the process retracted the
sharp claim, recorded the refutation loudly in a tracker, and followed the new structure to the
Krein/ghost-parity synthesis -- a better result than the one it lost.

TODO: write this episode up in full, with the commit trail, as the spine of the paper. It is the single
most convincing piece of evidence for the "serious" claim, because a generator that cannot lose an
argument cannot do research.

## 4. What the human director actually did

Honesty about the division of labor is the whole point; the claim is about a *directed* process.

- Set and enforced the discipline (attack-don't-defend; land only what survives; no hype; no em dashes in
  public copy).
- Supplied the adversarial pressure -- including commissioning the external reviews and feeding their
  critiques back in as untrusted-until-checked input.
- Made the judgment calls: which thread to pursue, when a reframe was honest versus a dodge, when to
  retract, when to synthesize across fields (the Turok-Bateman connection came from a human-supplied
  pointer).
- Did **not** supply the mathematics. The Clifford reconstruction, the branching computations, the Krein
  signature proof, and the no-go-candidate drafting were done by the process.

TODO: be precise and unflattering about where the director's lack of domain expertise was a risk, and
where the discipline caught it anyway.

## 5. Honest scope and threats to the claim

- **Reconstruction-grade throughout.** GU is not a finished theory; the object under study is a
  reconstruction. The meta-claim survives this (the *process* worked) but the object-level results are
  conditional and must be read that way.
- **Single case, selected by the people reporting it.** No baseline, no control, survivorship risk.
- **The reviews were also AI.** The adversaries that broke the claim were themselves AI agents; this is a
  strength (it scales) and a weakness (correlated blind spots). At least one external *human* reviewer is
  needed before the "serious" claim is safe.
- **"Serious" is not "correct."** The process produced honest, well-scoped, reproducible, self-correcting
  work. Whether the surviving physics is *true* is a separate question that only the physics community
  settles.

## 6. Why this might matter beyond GU

If the discipline (compute, adversarially verify, retract on falsification, synthesize across fields) is
what made the difference -- rather than anything specific to GU -- then the transferable artifact is the
**process and its guardrails**, not the result. That is the claim worth testing on a second, independent
problem. TODO: name a candidate second case.

## 7. Where to publish this (open question -- recommendation in the cover note)

Three different artifacts, three different homes; do not force them into one:

1. **This essay** -- a first-person, narrative account of building and directing the process. Its natural
   home is a **blog / essay venue** (personal site, Substack, or a venue like LessWrong / the AI-for-science
   community), because journals will not take the "I built and directed" voice and the value is the candid
   methodology narrative. This is the piece the title describes.
2. **The object-level GU result** -- the multiplicity / Krein finding -- as a short **arXiv note**
   (gen-ph / math-ph), the credibility anchor the essay points to. Reconstruction-grade caps it at a note,
   not a journal result.
3. **The de-personalized methodology** -- "adversarial self-refutation as a discipline for AI-assisted
   research" -- as a **case-study / methodology paper** for an AI-for-science workshop or venue, if and only
   if a second case backs it up.

Recommended order: publish (1) as a blog essay once (2) is on arXiv as its anchor; pursue (3) only after a
second independent case exists. Full reasoning in the response that accompanies this draft.

---

*TODO before this leaves v0: (a) object-level result must stabilize; (b) at least one external human
review of the physics; (c) the Sec. 3 retraction episode written in full from the commit trail; (d) a
named second case for Sec. 6; (e) decide venue per Sec. 7.*
