---
title: "SESSION INDEX 2026-08-09 — retrieval surface for the day's work: what was established, what was retracted, and what is owed"
artifact_type: session_index
created: 2026-08-09
status: INDEX__NOT_A_RESULT__POINTS_AT_EVERYTHING_FROM_THIS_SESSION
grade: "INDEX ONLY. Establishes nothing. Exists because the day's findings otherwise live only in
  explorations/, which is archival rather than encountered. Each row points at the artifact that owns the
  claim and its grade."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Session index, 2026-08-09

**Why this file exists.** Nearly everything below went into `explorations/`, where nothing points at it.
`NEXT-STEPS.md` carries a pointer to this index; this index carries pointers to the work.

---

## A. ESTABLISHED (new this session)

| finding | artifact |
|---|---|
| **The generation-carrier identification is NON-DISCRIMINATING.** `Casimir = -11.25` is exactly a scalar on the whole 128; a **random 192-dim subspace** of the `(base-4)(x)128` block passes the identical test. Enabling fact already in repo at `tests/oq_rk1_j_restriction_probe.py:316`, never connected. | `run-fast-sweep-carrier-identification-non-discriminating-2026-08-09.md` |
| **T1-T4 are AMBIENT, not carrier.** Krein signature, isotropy, `{K,chir}=0`, net chirality all BREAK under internal scramble (so they carry Clifford content) -- but random chirality-graded subspaces pass them unscrambled. Content belongs to `K` and `chir`, not the 192. | `run-scramble-T1-T4-ambient-not-carrier-2026-08-09.md` |
| **40 SM-neutral states in `ker(Gamma)`** (32 at `-11.25`, 8 at `-21.25`). Found by a hostile verifier REFUTING its own executing agent's "dark sector is dead". | `run-fast-sweep-carrier-...-2026-08-09.md` |
| The `640/832/192` split is **pure `so(4)` branching arithmetic**, to the digit, zero Dirac input. `832 = 640[(1/2,0)] + 192[(1/2,1)]`; second `192` is the exact ASD mirror. | same |
| **The monodromy `Z/2` is `pi_0(O(3,1))` TIME REFLECTION**, not the spinor double cover -- which is provably inert (`chi` quadratic, deck element `+1`). Layer-0 homonym. | `run-monodromy-frame-charge-preflight-hostile-2026-08-09.md` |
| **H10-01 RESOLVED**: Stelle's coefficients are swapped in-repo. Spin-2 **ghost** = `-4/3` (repulsive), spin-0 = `+1/3`. Sourced to Lu-Perkins-Pope-**Stelle** arXiv:1508.00010 Eq. (4.7a) + 3 independent confirmations. | banner in `tests/wave22/H10_ppn_weak_field.py` |
| `Q(B)` is **not** an observational discriminator -- lands inside Stelle quadratic gravity. | `run-six-move-workflow-results-2026-08-09.md` |
| **An index framework for arbitrary signature EXISTS** (van den Dungen, arXiv:1807.11856 Prop 4.5). "No index theory applies" was too strong; blocker relocates to the non-canonical spacelike reflection. | same |
| The four `C`s are **four different objects**; ghost parity is a **LINEAR** involution, not the antilinear chiralizer. | same |
| All of `ker(Gamma)` is Krein-balanced; balance **forced** by `{K,chir}=0`. Carrier-projected ghost-parity frame charge = **0**. | same / fast-sweep |

## B. RETRACTED or CORRECTED (this session)

| item | where recorded |
|---|---|
| **`24 sqrt(2)` RETRACTED** -- pure dimension count `3*sqrt(128)`, bit-identical even with all gammas zeroed. My claim, same-day. | retraction banner in `frame-charge-is-24-root-2-exactly-2026-08-09.md` |
| **`mu`-coupling asymmetry is a TRIVIALITY** (`Cas_+` is PSD). My "cheapest entry point" was wrong. | `next-object-1472-non-generation-sector-2026-08-09.md` |
| "**domain UNIQUE and FORCED**" was refuted 2026-08-08 (moduli dim **346,112**, planted collar coefficient). I had published it as good news. | spec v1.5, `docs/y14-x4-systems-spec.md` |
| **APS residual is DISCHARGED**, not open. I said open while citing the file that closes it. | spec v1.1 |
| "**non-convex**" is the wrong diagnosis for `pi_!` -- it is non-compactness, and the deeper issue is **non-ellipticity**. | CORRECTION **SD-01** in canon |
| **D8** (`Met(X^4)` contractible = the Riemannian fact under the Lorentzian name) and **D9** (stale `CP^2` scope tag). | CORRECTION **NGM-01** in canon + `canon-met-x4-contractibility-type-defect-2026-08-09.md` |
| `SIGNATURE-AMBIENT` vs `REAL-CLIFFORD-FORM` **conflated** -- by this spec for 3 versions, and by canon before it. Ambient fork is **OPEN**, depth 10 over threshold. | spec v1.3/v1.4 |
| The **compact-core route to `pi_!`** -- proposed by me, already tried and killed on a degree argument. | `swing-pi-pushforward-compact-core-closed-2026-08-09.md` |
| **Registry misfiling** -- single-decider was under `survives_gu_independent`, moved to `needs_recheck`. | `lab/process/layer0-fork-registry.yaml` |
| **CC-01 self-correction** -- "provably cannot" overreached; correct form is "survived every scramble tried". | `carrier-criterion-what-can-discriminate-2026-08-09.md` |

## C. OWED — nobody owns these

1. **H10-01 remediation.** 9 sites in `tests/wave22/H10_ppn_weak_field.py` + 3 in its exploration note; re-run the wave22 suite. Diagnosis settled, fix not applied.
2. **`ghost_parity_krein.py:76` silently Hermitizes** (`B = 0.5*(B+B^dag)`), manufacturing integer signatures from non-Hermitian input.
3. **THE OPEN QUESTION: a discriminating criterion for the carrier.** Still open, and upstream of the sector.
4. **The carrier MASS results are the only untested leg** under scramble (vectorlike, `{+64,0,-64}`, massive-decouples-to-zero).
5. **`sigma` homonym** -- section vs orientation bit. Rename owed; bears on DU's `sigma = w1`.
6. **D6** -- canonical `(p,q)` wire format. Flagged 3x, still unwritten.
7. **`F_2`/UNSAT frustration test** -- specified 2026-07-15, never run. Decides unique-vs-domains.
8. **Exponential degeneracy vs coset dimension 18432** -- two characterizations of the admissible-`C` set, never compared.
9. **What ARE the 40 SM-neutral states?**
10. **van den Dungen route** -- pursue or formally close.
11. **Second SHIAB wall** (coupling to the 192 carrier exactly zero) -- no follow-up.
12. **ai-epistemology routing** for the method finding -- flagged, never filed.
13. **Dissolution-condition watcher** -- canon's own named gap; proposed twice, never built.

## D. PROCESS (measured, not asserted)

- **Eight false-novelty instances** in one session, orchestrator and subagents alike. `lab/process/novelty-check.py` built in response, **failed on first use** (exact-substring matching defeated by paraphrase), fixed same day with co-occurrence search.
- **Dominant failure mode: summary outrunning artifact** -- correct numbers wrapped one level stronger than they support. Every one of 6 hostile verifies returned SCOPED; one returned REFUTED and was right.
- **Two things shipped without pre-flight; both were walked back** (the `24 sqrt(2)` interpretation, and the H10 grade). Pre-flight caught kills *in advance* everywhere it was used.
- **Cross-distance convergence** is the strongest evidence type available here: non-ellipticity (PDE) and non-quantization (watching a knob move) were one finding in two languages, neither aware of the other.
- Mailbox proposals filed: `drafting-factory` (pre-registration methods seed), `dynamic-unity` (degenerate selection, indefinite-form convergence, the `w_1` result bearing on `sigma = w1`).
