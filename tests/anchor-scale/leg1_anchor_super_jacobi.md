# LEG-1 (anchor swing) — Question 1: anchor-scale super-Jacobi for the graded IG algebra

**Posture.** The north star is *understanding the object*, not adjudicating GU. "Closes at
anchor" and "fails at anchor" are equally-valuable findings; this note uses weakest-defensible
wording and takes no side.

**Question (corners campaign, named gap 1).** Does the graded/fermionic extension of
`IG = G semidirect Omega^1(ad)` close super-Jacobi on the *honest* fiber — `G` a unitary-type
group on the `Cl(9,5)` spinor space (the campaign named `u(64,64)` as the honest unitary anchor
w.r.t. the Krein form), `Omega^1(ad)` the `4 x dim(ad)` translation slot, the odd generators in the
scalar-spinor channel that closed at toy scale? And does the FORCED-shape finding
(`{odd,odd}` lands only in the gauge-potential slot) survive the scale-up from `so(4)` on `Cl(4,0)`?

## Verdict

**CLOSES**, exact-arithmetic certified, on the honest `Cl(9,5) = M(64,H)` fiber (spinor dim 128).
The toy's existence and FORCED-shape results **transfer** to the anchor, with two anchor-specific
refinements that are themselves the interesting findings:

1. The odd module is the spinor `S` **as a real `u(64,64)`-module** `S_R`; the `{odd,odd}` bracket is
   the **sesquilinear Krein pairing** `M(Q,P) = i(Q P^† β_S + P Q^† β_S)`, not the toy's
   complex-bilinear charge-conjugation pairing. This is the anchor's genuine departure and is the
   point of contact with Question 2 (real/Krein form).
2. FORCED-shape holds in the minimal ansatz for the **entire** gauge algebra (semisimple part *and*
   the `u(1)` center). In the *extended* ansatz the anchor admits **one** structure with no toy
   analogue: a central-`u(1)` component of `{odd,odd}` on a **single 1-parameter locus**
   `t = -128 · Σ_μ w_μ q_μ`, exactly compensated by a phase-type `[transl, odd]` — available only
   because `u(64,64)` has a center that `so(4)` lacks. The semisimple bulk stays forced.

Two independent code paths agree (see *Corroboration*). No canon row moves; SG4 remains the decider.

## Object built (exact, memory-conscious)

- **`Cl(9,5)` gammas**: exact Gaussian-rational Jordan–Wigner, ported from
  `tests/generation-sector/`. 14 gammas, dim 128, `{γ_a,γ_b}=2 η_ab`, signature `(9,5)` — exact,
  sparse signed permutations. The `16384`-dim gauge algebra and `65536`-dim translation slot are
  **never** densely enumerated.
- **Krein form** `β_S` = product of the 9 spacelike gammas: Hermitian, `β_S²=I`, `tr β_S = 0` ⇒
  signature **`(64,64)`** (exact; eigenvalues `±1`, balanced). This is the campaign's
  adversarially-verified spinor Krein metric, here re-derived exactly.
- **Anchor gauge algebra** `u_β = {X : β_S X + X^† β_S = 0}` (the `u(64,64)`-type anchor,
  `dim_R = 128² = 16384`). The 91 `so(9,5)` spin generators `σ_ab` are `β_S`-pseudo-anti-Hermitian
  ⇒ `so(9,5) ⊂ u(64,64)` (exact, all 91) — so the semisimple sub-anchor sits inside the honest
  unitary anchor.
- **Translation slot** `T = R^4 ⊗ u_β` (`Omega^1(ad)`, abelian ideal, form index inert = RG regime).
- **Odd** = the scalar-spinor channel `S` as the **real** `u_β`-module `S_R` (`dim_R = 256`).

## Super-Jacobi identity classes — complete list and how each is certified

For `s = (u_β ⊕ T)_even ⊕ (S_R)_odd`, `{odd,odd} ⊆ T`, `[T,odd]=0` (minimal ansatz), the graded
Jacobi splits into exactly these classes (all certified with **exact** arithmetic, zero floats):

| class | content | certification |
|---|---|---|
| C1a | (g,g,g) even Jacobi | symbolic word-cert **W2** (all matrices) + exact witnesses |
| C1b | (g,g,T) ad-module | blockwise from W2 + exact witnesses |
| C1c/d | (g,T,T),(T,T,T) | `T` abelian by construction + exact witnesses |
| C2a | (g,g,Q) spinor module | symbolic word-cert **W3** (all `X,Y,Q`) + exact witnesses |
| C2b | (g,T,Q) | `tr[X,A]=0` telescoping + exact witnesses |
| C2c | (T,T,Q) | `[T,odd]=0`, `T` abelian + exact witnesses |
| C3a | (g,Q,P) **equivariance** | symbolic word-certs **W4/W5** (all `X∈u_β`) + exact witnesses |
| C3b | (T,Q,P) **forced-shape** | exact kill-witnesses (below) |
| C4  | (Q,Q,Q) cubic | exact witnesses (minimal) + the central-balance analysis |

The **word-algebra certificates W1–W6** are the load-bearing move: each is a `*`-algebra identity
proved from the *single* defining relation `X^† β = -β X` of `u_β`, so it holds for **every** element
of `u(64,64)` and every spinor at once. This replaces the toy's exhaustive basis loops (infeasible at
`dim 128`) with **no** loss of exactness and **no** rank scouting. W4 (`[X,M(Q,P)] = M(XQ,P)+M(Q,XP)`)
is the anchor analog of the toy's equivariant-pairing certificate.

## FORCED-shape retest at anchor

- **Noncentral kill** (C3b): a semisimple-gauge-valued `{odd,odd}` component `s·M_sl` violates the
  `(T,Q,P)` Jacobi — `[a,{Q,P}_g] ≠ 0` while the RHS `= 0` (exact witness). `ρ` does not enter this
  LHS, so the kill survives the extended ansatz. → forced out of the semisimple bulk, exactly as the
  toy kill lemma.
- **Central kill** (minimal, C4): a central `t·M_0` component violates the cubic — residual
  `3 i t · s(Q,Q) · Q ≠ 0` on `Q1=Q2=Q3` (exact; requires a Krein-non-null `Q`).
- **Central escape** (extended): with a real phase-type `[transl,odd]` switched on, the cubic residual
  is **exactly linear in `t`** and vanishes on the single locus `t* = -128 · Σ_μ w_μ q_μ`; the balanced
  algebra then closes **all** classes (verified on fresh exact triples), while `t*+1` fails. This is a
  1-parameter locus, not a free direction — the `su(n|1)`-type Fierz balance of the `{odd,odd}` central
  charge against the trace-`ρ` of its translation part. It exists because `u(64,64)` has a center;
  `so(4)` did not, which is why the toy saw a clean forced-shape and the anchor sees a
  center-only refinement.

**Reading:** the transcript's "the space of four momentum becomes the space of gauge potentials"
survives at anchor for the whole gauge algebra in the minimal ansatz; the only anchor-scale loosening
is a single central-`u(1)` direction under the extended ansatz.

## Two reconciled routes (coherent picture of the object)

- **Complex route, semisimple sub-anchor `g = so(9,5)`** (independent `clif95` leg): the
  complex-bilinear ad-channel pairing exists — the antisymmetric charge conjugation `C_+` (unique of
  the two, `C_+ σ_ab` **symmetric**, all 91) gives a symmetric `Sym²(S) → so(9,5)` bracket, and C3a
  equivariance holds for **all 91** generators (certified by the `C_+` spin-intertwiner
  `σ^T C_+ + C_+ σ = 0` for all m,m', and directly on the 128-dim spinor rep). Signature subtlety
  caught and fixed: the intrinsic `so(9,5)` element needs the `η`-metric to raise indices — invisible
  in the Euclidean toy, load-bearing at the Lorentzian anchor.
- **Real route, full anchor `g = u(64,64)`** (parallel LEG-1 file): the complex-bilinear map into the
  adjoint is **killed** by the `u(1)`-center charge constraint (`z=iId` acts as `+i` on `S`, so
  `Sym²S` has charge `+2` and cannot map equivariantly to the charge-0 adjoint). Only the
  **sesquilinear** Krein pairing survives, on the real form `S_R`.

These are consistent and complementary: the same obstruction (the center) that removes the complex
channel at the full unitary anchor is *absent* at the semisimple sub-anchor, where the complex channel
exists. **Either way the graded extension closes.** The complex route says the object exists over `C`
on the semisimple anchor; the real route says the honest full-`u(64,64)` object exists over `R` via the
Krein form. The `so(9,5) ⊂ u(64,64)` inclusion (exact) links them.

## Exact-certified vs argued/sampled (honest labelling)

- **Exact-certified, all-element (strongest):** Clifford/Krein/`β_S` facts; `so(9,5) ⊂ u(64,64)`;
  the equivariance/module/closure classes via the symbolic word-certs W1–W6; the complex-route C3a via
  the `C_+` intertwiner. These are proofs, not samples.
- **Exact-arithmetic on random witnesses (strong, sampled):** the ansatz-specific closures — the cubic
  C4, the `(T,Q,P)` C3b, and the central-balance locus — verified on 3–4 fresh exact random witnesses
  each and **independently reproduced on a second codebase** (`clif95`, 9 checks). Exact arithmetic
  throughout (no floats); formally sampling of polynomial identities, not all-element proofs.
- **Argued via representation theory (weakest, no exhaustive computation):** ansatz *completeness*
  (channel dims `2/8/16`) via Schur + an `sl(128)`-irreducibility argument whose premises (structure
  constants on 432 index tuples, root distinctness, generation chains) are machine-verified but whose
  glue is classical; and the RD-regime impossibility (`sl(128)` simple ⇒ no 4-dim rep). These replace
  the toy's exact-rank certificates and are the least-hard part of the leg — flagged as *argued*.

## Honest residuals (not closed here)

- **Real/Krein form selection (Question 2):** this leg establishes the sesquilinear pairing on `S_R`
  *closes*; whether `M(64,H)`'s quaternionic structure canonically supplies that real form (and whether
  it is the physically selected one) is Question 2's finer remit. A sibling LEG-2 ran in parallel.
- **Derivative-level odd `τ_plus` (Question 3):** untouched here; all structure maps are pointwise
  (locality proxy passes), so the toy's `R^4` locality transfers, but the derivative in the `τ_plus`
  embedding is a separate check.
- **Extended-ansatz `[transl,odd] ≠ 0` beyond the central locus:** the noncentral matrix-type `ρ` is
  killed exactly; the surviving extended structure is the single real phase-type `ρ` giving the central
  balance. A full extended-ansatz Gröbner sweep (as the toy did at Part 6/7) is not re-run at anchor.

## Firewall

`sigma`/Clifford inputs only. No `chi(K3)=24`, no `/8` manufacture, no `A-hat=3`, no topology imports;
the bare `58.72` commutator is never formed or moved. This leg computes super-Jacobi identities and
spinor-bilinear structure only.

## Artifacts

- `LEG-1-anchor-super-jacobi.py` — primary script (64 checks, exit 0, `leg1_run.log`).
- `clif95.py` + `leg1_crosscheck.py` — independent sparse-exact infrastructure and cross-check
  (9 checks, exit 0, `leg1_crosscheck.log`), corroborating every load-bearing + central-escape claim.
