---
artifact_type: novelty_assessment
created: 2026-08-08
subject: "Two 2026-08-08 candidates checked against the literature"
verdict: NEITHER_IS_NOVEL__DO_NOT_SEED__BOTH_RETAINED_AS_INTERNAL_SCREENING_RULES
method: "Targeted web search, three queries, plus one abstract fetch. NOT exhaustive."
---

# Novelty check: the `{J,K}` dichotomy and the sign-visibility note

The 2026-08-08 blockbuster council allocated **one hour, not more** to check
whether either of the day's two externally-facing candidates is already known.
Done. **Neither is. Do not seed either to the drafting factory.**

---

## Candidate 1 — the `{J,K}` dichotomy

**The claim.** For `M` K-self-adjoint with real spectrum and antilinear `J`
(`J² = −1`) commuting with `M`: `{J,K} = 0` forces exactly K-balanced
eigenspaces, so the C-operator is never dynamics-determined; `[J,K] = 0` leaves
signatures maximally informative and C determined.

**Verdict: NOT NOVEL.** Every ingredient is in the literature, and the framework
that parametrises exactly this dichotomy already exists.

- **Metric-operator non-uniqueness is textbook**, not a discovery. There are
  always an *infinite* class of positive-definite inner products satisfying the
  unitarity condition, each defining a separate physical Hilbert space with its
  own complete set of observables.
- **C-operator non-uniqueness is known AND explained** — there is a paper
  devoted to it (arXiv:0906.1011), attributing the ambiguity to the chosen
  normalisation of left/right eigenvectors.
- **The anticommutation → degeneracy link is already stated**: pseudo-Hermitian
  Hamiltonians with even PT-symmetry admit a degeneracy structure when `PT`
  anticommutes with the metric operator. That is the substance of the
  dichotomy's non-trivial half.
- **The commutation SIGN is already a classification parameter.** Krein spaces
  with Real structures are classified by `(η, τ)` where the second symmetry
  satisfies `S² = η·1` and **`JS = τSJ`** — `τ = ±1` is precisely
  commuting-vs-anticommuting — and the *signature* consequences for
  `J`-hermitian operators in that setting are the subject of published work
  (arXiv:1601.03992).

**What survives:** nothing publishable. The result is correct and was arrived at
independently, but it is a rediscovery.

## Candidate 2 — "what can see a metric sign flip"

**The claim.** Complexification cannot see a base sign flip; nor can the
isometry group, maximal compact, Levi-Civita connection, geodesics, curvature or
causal structure; the Clifford algebra can.

**Verdict: NOT NOVEL — it is textbook.** The literature states the exact
contrast this note was built around:

> Clifford algebras of opposite signature are not isomorphic, **but Spin groups
> of opposite signature ARE isomorphic**.

That is candidate 2's entire content, already standard. `Cl(p,q)` and `Cl(q,p)`
are graded-opposite algebras; `Spin(p,q) ≅ Spin(q,p)`. The complexification
half — `Cl(p,q) ⊗ ℂ` depending only on `p+q` — is likewise elementary.

---

## What this closes, and what it does not

**Closes:** both drafting-factory lines. Neither gets seeded. The council's hour
is spent and it bought a clean negative, which is what it was for.

**Does NOT close — and this is the part worth keeping.** Both results remain
valuable *internally as screening rules*, and their internal value never
depended on novelty:

- **Signature-blindness** retroactively explains `M-H9`'s failure (a
  complexified Racah–Speiser module was named as the fork's resolver while being
  provably incapable of discriminating) and forbids that whole category of
  future attempt.
- **The base-sign exclusion** tells every future resolver attempt that it must
  reach the Clifford/spinor layer, which is why the declared-base route was dead
  on arrival and why Majorana–Weyl was at least in the right class.

**The lesson worth recording is about the repository, not the mathematics.**
Both facts are standard, and neither had been applied here. Two failed
approaches on 2026-08-08 would have been avoided by knowing textbook Clifford
reality theory. That is an argument for consulting standard references *before*
building a resolver, not for writing new ones.

## Method limits, stated

Three targeted web searches and one abstract fetch. **Not an exhaustive
review.** For a negative verdict — "this is already known" — that is adequate,
because finding prior art proves the point. It would NOT be adequate to support
a positive novelty claim.

## Sources

- Nonuniqueness of the C operator: <https://arxiv.org/pdf/0906.1011>
- Signatures for J-hermitians and J-unitaries on Krein spaces with Real
  structures: <https://arxiv.org/pdf/1601.03992>
- Pseudo-Hermiticity, PT symmetry and the metric operator (Mostafazadeh):
  <https://www.researchgate.net/publication/239634067_Pseudo-Hermiticity_PT_symmetry_and_the_metric_operator>
- Krein-space formulation of PT symmetry, CPT inner products, pseudo-Hermiticity:
  <https://www.researchgate.net/publication/239634104_Krein-space_formulation_of_PT_symmetry_CPT-inner_products_and_pseudo-Hermiticity>
- Clifford algebras and spin groups (lecture notes):
  <https://www.math.columbia.edu/~woit/LieGroups-2012/cliffalgsandspingroups.pdf>
