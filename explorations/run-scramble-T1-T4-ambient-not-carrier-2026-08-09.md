---
title: "Scramble test on the Krein/chirality results: T1-T4 ALL BREAK (so they do carry internal-Clifford content, unlike the Casimir) — but random chirality-graded subspaces pass them all, so the content belongs to the AMBIENT operators K and chir, not to the 192. The carrier-identification gap is NOT closed."
artifact_type: exploration_result
created: 2026-08-09
status: THIRD_OUTCOME__T1_T4_BREAK_UNDER_SCRAMBLE_SO_THEY_HAVE_INTERNAL_CONTENT__BUT_RANDOM_GRADED_SUBSPACES_PASS_THEM_UNSCRAMBLED_SO_BREAKING_IS_NECESSARY_NOT_SUFFICIENT__CONTENT_IS_AMBIENT_NOT_CARRIER__GAP_NOT_CLOSED
grade: "EXECUTED, read-only. 32 scrambled runs (Haar and Hermitian-involution U), positive control (global
  unitary conjugation) and two negative controls, all passing. NOT hostile-verified -- launched without a
  verify pass, which is itself recorded below as a process lapse."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# The scramble test: a third outcome

## The question

The prior note offered two outcomes: T1-T4 survive the internal-gamma scramble (whole sector is base-side),
or they break (**the first discriminating criterion for the carrier has been found**).

**Neither holds. The answer is a third thing, and it is better posed than the question.**

## (a) They ALL break

`e_a = (s3 (x) s3) (x) R_a` verified at residual `0.00e+00`; internal gammas replaced by
`(s3 (x) s3) (x) U_random`; **K and chir REBUILT from the scrambled gammas each run**. Internal destruction
confirmed: `max ||{e_a,e_b}||` over internal pairs `16.29-17.11`. Base-base and base-internal
anticommutators preserved at `0.00e+00`, so `ker = 1664`, the split `640/832/192`, and `su(2)_+` closure all
reproduce.

| | baseline | all-ten scrambled | verdict |
|---|---|---|---|
| **T1** eigenvalues all `+/-1` | `1.09e-14` | `0.916 - 0.990` | **BREAKS** |
| **T1** signature | `(+96,-96,0)` | wanders: `(96,96)`, `(102,90)`, `(90,102)`, `(108,84)` | **not preserved** |
| **T2** isotropy of both halves | `1.38e-15` | `0.456 - 0.538` | **BREAKS** |
| **T3** `{K,chir} = 0` | **exactly `0.00e+00`** | `0.685 - 0.718` | **BREAKS** |
| **T4** `\|Tr(chir\|192)\|` | `7.77e-15` | `1.21 - 12.42` | **BREAKS** |

So unlike the Casimir identification, **these results DO carry internal-Clifford content.**

## (b) But breaking is NECESSARY, NOT SUFFICIENT — and that kills the inference

The agent ran the control the prior note's logic required and the brief did not specify. **On the
UNSCRAMBLED substrate, T1-signature, T2, T3 and T4 are passed at `~1e-15` by:** the ASD `192` mirror, the
`832`, the `640`, **and random chirality-graded 192-dim subspaces** of `ker(Gamma)`, of the 512 block, and of
the full 1792.

The only quantity separating canonical sectors from random ones is T1's `+/-1` (`<=1.9e-14` vs
`0.988-0.997`) — and **all four sectors pass it equally**, so it does not single out the carrier either.

**Mechanism, all machine-exact zeros:**
`||K^2 - I|| = ||[K,J_k]|| = ||[K,Pi]|| = ||{K,chir}|| = ||chir^2 - I|| = 0.00e+00`.
Every Casimir eigenspace is K-invariant, hence inherits an involution (T1's `+/-1`); and `{K,chir} = 0`
globally plus equal chirality halves gives T2/T3/T4 for **any** graded subspace. `{K,chir} = 0` is elementary
parity: `beta_S` is a product of **nine (odd)** gammas, and `omega` anticommutes with every single gamma in
even dimension 14.

> **T1-T4 have genuine internal-Clifford content, but that content belongs to the AMBIENT operators `K` and
> `chir` — not to the 192. The carrier-identification gap is NOT closed.**

## (c) Three sharpenings

**T1 is blind to half the internal gammas.** `beta_S` is a product of *spacelike* gammas, so scrambling all
five **timelike**-internal gammas leaves it bit-unchanged (Hermiticity defect `0.00e+00`) and T1 survives
exactly, signature `(96,96)` in 6/6 runs. **One spacelike**-internal gamma breaks it. T2/T3/T4 break under
**any** single internal gamma, either kind.

**CODE DEFECT — the scrambled "signature" is manufactured.** `K|192`'s anti-Hermitian fraction goes
`1.7e-16 -> 0.97-1.05`, and `tests/generation-sector/ghost_parity_krein.py:76` silently applies
`B = 0.5*(B + B^dag)` — **producing integer signatures from a matrix that is no longer a Hermitian form.**
Any signature reported by that path on a perturbed input should be distrusted. Same for the net-chirality
count once `||chir^2 - I||/||I|| = 1.35-1.41`.

**T4's mechanism is exact:** `Tr(chir|192) = 6 x Tr(Omega_int)` (6 = base-side dimension of the 192, verified
to 4 digits in 4 independent cases). The Clifford algebra forces `Tr(Omega_int) = 0`; scrambled it is `O(1)`.

## (d) Controls

Positive (global unitary conjugation, 5 runs): everything invariant, T1 `(96,96)` maxdev `<=1.51e-14`, T2
`<=2.34e-15`, T3 `<=4.47e-15`, T4 `<=2.99e-14`. Negative 1 (all gammas zero): `ker 1792 != 1664`, detected.
Negative 2 (all 14 -> Haar U(128)): sector collapses to dim 1, detected. **Pipeline sound.**

## (e) Prior art — EIGHTH instance, and my own novelty tool failed to find it

`explorations/chirality-grading-and-77-rerun-2026-08-03.md:281` already records
`"omega beta + beta omega = 0 exactly, both omega-halves totally isotropic (1.6e-16), signature (832,832)"`
on the full 1664, and calls the neutrality **FORCED**. MOVE-5 (`RESEARCH-STATUS.md:1263`) already forces net
chiral index 0 `Psi`-independently. **The ambient-not-carrier character of T2/T3 was already in the repo.**

Genuinely new here: the scramble behaviour, the spacelike/timelike split, the `T4 = 6 Tr(Omega_int)`
mechanism, and the random-graded-subspace comparison.

> **METHOD FAILURE.** `lab/process/novelty-check.py` returned **0 hits for all 10 term sets tried**, including
> `"totally isotropic chirality halves"`, while the file above contains exactly that fact in paraphrase. The
> prior art was found **by hand**. The tool used exact-substring matching, so any rephrasing defeated it — a
> required step that yields false negatives is worse than none, because it *licenses* novelty claims. Fixed
> the same day: word-level co-occurrence search added, regression-tested against this exact miss.

## (f) What this does NOT establish

1. **The mass results were NOT tested** (vectorlike, `{+64,0,-64}`, massive-decouples-to-zero). Scoped out of
   the brief. **That leg remains open and is now the only untested one.**
2. This scramble preserves base-internal anticommutation exactly by construction; a scramble breaking that
   too would break more, but would also destroy `su(2)_+` and the `j=1` label.
3. The random comparators are chirality-graded 96/96 by construction. The null is specifically: *among*
   graded 96/96 subspaces, T2/T3/T4 carry no information.
4. **Scrambled signature integers are not signatures** (see the code defect above).
5. Scramble run in `(9,5)` only.
6. **This result was not hostile-verified.** It was launched as a bare agent without a verify pass, on a day
   when every verify returned SCOPED or REFUTED. Treat accordingly.
