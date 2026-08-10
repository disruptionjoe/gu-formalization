---
title: "Six-move workflow results: all six executed, zero kill conditions fired, and EVERY hostile verify returned SCOPED — the arithmetic holds everywhere and the framings were overstated everywhere, including one of my own published claims which is now RETRACTED"
artifact_type: run_receipt
created: 2026-08-09
status: SIX_OF_SIX_COMPLETED__ALL_SIX_VERIFIES_SCOPED_UPHELD__24ROOT2_INTERPRETATION_REFUTED__MU_ASYMMETRY_DEFLATED_TO_TRIVIALITY__NO_INDEX_THEORY_APPLIES_CLAIM_SCOPED_BY_A_LITERATURE_FIND__ONE_CONFIRMED_COEFFICIENT_ERROR_FOUND_IN_REPO
grade: "EXECUTED, 12 agents, 0 errors, ~1.57M subagent tokens, 446 tool uses. Every move paired with an
  adversarial verify that independently recomputed rather than quoted. All six verifies returned SCOPED /
  upheld=true: no arithmetic was refuted anywhere, and no headline survived at its stated strength."
method: "Pre-flighted per move by tailored specialist panels (inline), then executed read-only against the
  Cl(9,5) substrate, then hostile-verified by a second agent per move."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Six-move workflow: results

> ### ONE ITEM RETRACTED, SAME DAY.
>
> This receipt records the `24 sqrt(2)` frame-charge result as *sharpening* the non-quantization finding.
> **That interpretation is RETRACTED.** A gamma-scramble test showed `NET-SD` is a **pure dimension count with
> zero Dirac content** — `n_SD * sqrt(DIM) = 3*sqrt(128)` analytically, bit-identical even with all 14 gammas
> replaced by zero matrices — and the "`sqrt(2)` is generator normalization" reading is specifically refuted
> (it is the leftover of `sqrt(128) = 8 sqrt(2)`). See the retraction banner on
> `frame-charge-is-24-root-2-exactly-2026-08-09.md`. Everything else in this receipt stands.


**Every agent was read-only.** Another agent was writing in this repo concurrently; no workflow agent
created, edited, or committed any repo file. All scratch went to `/tmp`.

## The uniform outcome

**Six moves, six completions, zero kill conditions fired — and six hostile verifies all returning
`SCOPED / upheld = true`.** Not one arithmetic result was refuted. Not one headline survived at its stated
strength. That pattern is the single most useful thing this run produced.

## Move by move

### M-SCRAMBLE — **REFUTES A CLAIM I PUBLISHED THIS SESSION**

`NET-SD` is a **pure dimension count with ZERO Dirac content**. It equals `n_SD * sqrt(DIM) = 3*sqrt(128)`
**analytically**, and is **bit-identical under every gamma scramble, including replacing all 14 gammas with
zero matrices.**

And the specific reading I proposed is refuted: **the `sqrt(2)` is NOT generator normalization** — it is the
leftover of `sqrt(128) = 8*sqrt(2)`. So "the integer content is 24" is dead; the 24 is `3 x 8`, carrying no
geometric content. **`step7_integer_freeness.py`'s verdict stands unchallenged.** Retraction banner applied
to `explorations/frame-charge-is-24-root-2-exactly-2026-08-09.md`. Also flagged `already_in_repo: true`.

### M-1472-KREIN — question well-posed, prediction hit exactly, but it is a corollary

K-orthogonality **holds exactly and structurally** (the Casimir is K-self-adjoint, so distinct-eigenvalue
eigenspaces are K-orthogonal; max off-diagonal `2.933e-15`). Kill condition did not fire.

Signatures, matching the panel prediction to the digit: `640 -> (+320,-320,0)`, `832 -> (+416,-416,0)`,
`192 -> (+96,-96,0)`, total `(+832,-832,0)`, `1472 -> (736,736)`. **Every Gram eigenvalue is exactly +/-1**;
zero null directions.

**But the balance is forced, not discovered.** `{K, chir} = 0.000e+00` exactly — K *swaps* the chirality
halves — so `K|sector = [[0,B],[B^dag,0]]` with `B` unitary, and signature `(r,r,0)` follows. Genuinely new:
the "each chirality half is totally isotropic" property, previously recorded only for the 192, **now holds
for the 640 and 832 as well**. Robust on `(7,7)` and under the alternative `K_T` convention. A sensitivity
control confirmed the pipeline does detect imbalance when present.

**New structural fact worth keeping:** under the full base `so(4)`, `832` is **not** irreducible —
`832 = 640[(1/2,0)] + 192[(1/2,1)]`, and that second `192` is the **exact anti-self-dual mirror of the
generation carrier `(1,1/2)`**. The whole decomposition is SD <-> ASD symmetric.

**And it deflated my own "cheapest entry point."** The `mu`-coupling asymmetry is a **triviality**:
`Cas_+ = sum_k J_k^dag J_k` is PSD, so `mu` vanishes on the `su(2)_+` invariants **by construction**. No
story to attach. Correction applied to the 1472 note.

### M-ULTRAHYPERBOLIC — scopes a load-bearing claim, including one of mine

An index-theoretic framework covering ultrahyperbolic `(9,5)` **does exist**: van den Dungen's 2019 Addendum
(arXiv:1807.11856) Prop 4.5, an indefinite spectral triple in **arbitrary** signature `(t,s)` with no
Lorentzian and no parallel-time restriction. The verify **independently fetched and confirmed the quote
verbatim**.

So the repo's "no index theory applies to a non-elliptic operator" — which I promoted to a **Tier-1 salvage
item** — is **too strong as stated**. The blocker relocates rather than vanishing: it becomes the
**45-dimensions-per-point non-canonical choice of spacelike reflection**, which is precisely GU's own
already-proved "no invariant Riemannian metric / no invariant `J`" no-go.

**Verify SCOPED it hard:** "refuted" overstates, **one numeric certificate is arithmetically false as
written**, and at least four in-repo prior hits were under-reported, one strictly subsuming the headline
number. Treat the literature find as real and the framing as unreliable.

### M-LAYER0-C — the four `C`s are four different objects

The **ghost parity is a LINEAR involution** (the Krein form `K = eta_V (x) beta_S` implementing the Cartan
involution) — **not** the antilinear chiralizer `C = J_quat . G`. So **the `0.00e+00` frame charge does not
transfer**, and the planned follow-up is **NOT redundant** on those grounds. Its full-space version is
answerable by reading alone (also zero, for a different structural reason); only the **carrier-projected**
version is live. Verify: SCOPED — core survives, headline's second half fails, one verdict cell wrong.

### M-MODULI-SHIAB — both answers are structural, as the panel predicted

The admissible `C`s form a **group orbit**, exactly as the pre-flight anticipated: a product of noncompact
symmetric spaces `U(p,q)/(U(p) x U(q))`, coset dimension `sum_l 2 p_l q_l` — `18432` at the exactly-scalar
cores (already in repo), `9216 / 6144 / 3072` elsewhere. So "dimension of the moduli" was never a
computation; it is a structural statement.

New: the SHIAB family is **two Schur channels per chirality block**, with a **second wall** (contract+wedge)
at which the shiab's image is entirely the 64-dim Clifford-trace summand and its **coupling to the 192-dim
generation carrier is EXACTLY ZERO**. Net-SD frame charge and the complex-closure selector are hard,
well-explained nulls. Verify: SCOPED — three "new" items survive, **one is a sixth false-novelty claim**, and
the lead headline is "a dimension-only tautology dressed as a generation-sector statement."

### M-QB-SHAPE — not a discriminator, and it found a real repo error

**NO.** `Q(B)` lands **exactly inside Stelle quadratic gravity**, whose ppE / PPN / short-range constraints
are already published and should be **read off, not derived**. The advertised "shape feature" (GU on the
`m_0 = m_2` locus, PPN `gamma(r) = 1` identically) does **not** survive verify — and its content was
"indistinguishable from GR" anyway.

**The real value of that run is a byproduct:** checking it **exposed a load-bearing sign/assignment error in
the repo's own `alpha_Y = 1/3` Yukawa chain**, and the verify **CONFIRMED it** as genuinely new. That is an
owed correction to canon and the most actionable single output of the workflow.

## What the run establishes

1. **My `24 sqrt(2)` finding is dead** and its interpretation refuted. Retracted.
2. **The `mu`-asymmetry is a triviality.** My "cheapest entry point" framing was wrong. Corrected.
3. **"No index theory applies" is too strong** — a framework exists; the blocker relocates onto GU's own
   invariant-`J` no-go. Tier-1 salvage item 5 needs scoping.
4. **The ghost parity is linear**, so the frame-charge follow-up survives as live (carrier-projected only).
5. **All of `ker(Gamma)` is Krein-balanced**, with total nondegeneracy, and totally-isotropic chirality
   halves now established beyond the 192.
6. **A confirmed coefficient error** in the `alpha_Y = 1/3` Yukawa chain — owed to canon.
7. **`Q(B)` is not an observational discriminator.** Stop treating it as one.

## The methodological result

**Six independent hostile verifies, six SCOPED verdicts, zero refuted computations.** The consistent failure
mode across every move — mine and the agents' — is **summary outrunning artifact**: correct numbers wrapped
in a claim one level stronger than they support. Two of the six also carried a false-novelty claim, bringing
this session's total to six.

The pre-flight panels earned their cost again: they predicted the group-orbit structure (M-MODULI), the
non-discriminator verdict (M-QB), and the scramble design flaw that would otherwise have manufactured a
false null (M-SCRAMBLE).
