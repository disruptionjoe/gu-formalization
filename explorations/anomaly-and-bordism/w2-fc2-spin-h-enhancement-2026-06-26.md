---
title: "W2-FC2 — Spin^h enhancement of Y14: existence, canonicity, index preservation"
status: exploration
doc_type: failure_condition_attempt
date: 2026-06-26
verdict: CONDITIONALLY_RESOLVED
opened_by: "W2-FC1 (DERIVATION-PROGRESS.md, 2026-06-26)"
parent_correction: "W2-01 (canon/w2-y14-spin-structure.md)"
---

# W2-FC2 — Does Y14 admit a canonical Spin^h structure that preserves the generation count?

Reconstruction-grade. Discipline tags: `[verified]` standard math fact; `[reconstruction]`
plausible re-derivation not independently refereed; `[speculation]` heuristic.

## 0. The question (verbatim framing)

Opened by W2-FC1. After CORRECTION W2-01 (`w2(Y14) = pi*w2(X4)`, so **Y14 spin iff X4 spin**),
W2-FC1 established that the U(1) spin-c twist `S tensor_C L^{1/2}` does NOT rescue GU's
quaternionic index: it breaks H-linearity and shifts the index off `Â(K3)=2`. W2-FC1 flagged
the **only** structure that could relax "X4 spin" while keeping a quaternionic `ind_H` as a
**Spin^h structure** (`Spin^h(n) = (Spin(n) x Sp(1))/Z2`, the quaternionic analog of spin-c),
and asked:

1. **(i) Existence.** Does Y14 admit a Spin^h structure for non-spin X4?
2. **(ii) Canonicity.** Is there a *canonical* choice (one singled out by GU's own data)?
3. **(iii) Index.** Does a non-trivial Sp(1) twist preserve the spin-1/2 leg `8·Â(K3)=16`,
   or does the Sp(1)/instanton class shift `Â(K3)=2` and hence the generation count?

## 1. Verdict

**CONDITIONALLY_RESOLVED — Spin^h exists but does NOT canonically relax the spin precondition.**

Decomposed:

- **(i) Existence: YES, unconditionally.** Y14 is Spin^h for *any* orientable X4 (including
  non-spin CP2). This follows immediately from the established result that Y14 is Spin-c
  (`W3(Y14)=0`, W2-FC1) plus the standard inclusion `Spin^c(n) ⊂ Spin^h(n)`. So existence is
  RESOLVED-grade; it is NOT the hard part.
- **(ii) Canonicity: NO.** GU's data does not single out a non-trivial Spin^h structure. The one
  natural quaternionic structure (the right-`H` action on `S = H^64`) is the **trivial** Sp(1)
  bundle (`c2 = 0`), whose `w2` is `0` — it matches `w2(Y14)=pi*w2(X4)` only when X4 is spin,
  i.e. exactly the case where Spin^h is not needed. Every Spin^h structure that actually covers a
  non-spin base requires an *extra, non-canonical* choice of an SO(3)/Sp(1) bundle with
  `w2 = pi*w2(X4)`.
- **(iii) Index: H-linearity is RESTORED, but index-value preservation is NOT — and is generically
  violated.** A genuine (quaternionic) Sp(1) twist keeps the Dirac operator right-`H`-linear (the
  one real improvement over the bare spin-c twist of W2-FC1), so `ind_H` is well-defined. But the
  Spin^h index is `ind = rank · (Â + δ)` with `δ` the Sp(1)/instanton correction
  (`δ ∝ ⟨c2(V), internal-4-cycle⟩`); a non-trivial twist shifts the spin-1/2 leg off `8·Â(K3)=16`.
  Whether a twist can simultaneously satisfy `w2 = pi*w2(X4)` AND keep `δ=0` on the internal cycle
  is **not** answerable in current GU because it depends on the (separately OPEN) compact-K3
  reduction. **No canonical generation-count-preserving Spin^h structure is exhibited.**

Net effect on the program: **the spin precondition of W2-01/W2-FC1 STANDS.** Spin^h does not give
a free relaxation. This is a TIGHTENING, in the same conservative direction as W2-01 and W2-FC1.

The single genuine advance: Spin^h **isolates** the real obstruction. W2-FC1 listed two objections
to the spin-c rescue (broken H-linearity *and* index shift). Spin^h repairs the first and leaves
the second. So the load-bearing barrier is now precisely the **index shift**, not H-linearity.

## 2. (i) Existence — Y14 is Spin^h for any orientable X4

**Standard facts used.**

- `Spin^h(n) := (Spin(n) x Sp(1)) / Z2`, `Z2 = {(1,1),(-1,-1)}`. A Spin^h structure on an oriented
  `M^n` is a lift of the `SO(n)` frame bundle to `Spin^h(n)`. Via `Spin^h(n) -> SO(3) = Sp(1)/±1`
  it carries an auxiliary SO(3) bundle `E`; the lift exists **iff** there is an SO(3) bundle `E`
  with `w2(TM) = w2(E)` (equivalently `TM ⊕ E` is spin). `[verified — Albanese–Milivojević,
  "Spin^h and further generalisations of spin", J. Geom. Phys. 168 (2021)]`
- `Spin^c(n) = (Spin(n) x U(1))/Z2 ⊂ Spin^h(n)` via `U(1) ↪ Sp(1)` (unit complex ↪ unit
  quaternions); `-1 ↦ -1`, so the diagonal Z2 maps compatibly. **Every Spin^c structure induces a
  Spin^h structure.** `[verified — group inclusion]`
- **Dimension caveat (and why it does not bite):** Albanese–Milivojević prove every orientable
  manifold of `dim ≤ 7` is Spin^h, with non-Spin^h examples first in `dim 8`. Y14 has `dim 14 ≥ 8`,
  so the low-dimensional theorem gives NOTHING here — existence must be argued from Y14's specific
  structure, not its dimension. `[verified — A–M Thm; dimension count]`

**Argument.** W2-FC1 established `W3(Y14) = beta(w2(Y14)) = pi*beta(w2(X4)) = pi*W3(X4) = 0` (every
oriented 4-manifold is Spin-c, so `W3(X4)=0`, and `w2(Y14)=pi*w2(X4)` has no vertical W3 piece).
Hence Y14 is Spin-c, hence **Spin^h, for any orientable X4 — including non-spin X4 (e.g. CP2).**
`[reconstruction — chains W2-FC1's Spin-c result with Spin^c ⊂ Spin^h]`

**Concrete witness on a non-spin base (CP2).** `w2(CP2) = H mod 2` (`H` the hyperplane class).
Take complex line `L` with `c1(L)=H`; `E0 = R ⊕ L_R` is an oriented rank-3 bundle with
`w2(E0) = c1(L) mod 2 = w2(CP2)`, `w1(E0)=0`. Pull back: `E = pi*E0` on Y14 has
`w2(E) = pi*w2(CP2) = w2(Y14)`. So `TY14 ⊕ E` is spin ⇒ Y14 is Spin^h. `[reconstruction]`

**Caveat on the witness (honesty).** This `E0` has `w2 ≠ 0`, so it does **not** lift to an honest
SU(2)=Sp(1) principal bundle on its own (`beta w2(E0) = W3 = 0` here, so a lift does exist, but the
`U(1)`-reduced `E0 = R ⊕ L_R` is the spin-c-type witness). Existence of *a* Spin^h structure is thus
real but cheap; it is the spin-c-induced one, which is exactly the structure W2-FC1 already found
insufficient (see §4). The substantive question is whether a *better* (genuinely quaternionic,
canonical) one exists — §3, §4.

## 3. (ii) Canonicity — no GU-distinguished non-trivial Spin^h structure

A Spin^h structure that covers a non-spin base needs an SO(3)/Sp(1) bundle `E` (equivalently a
`C^2 = H` "twist" bundle `V`) with `w2(E) = pi*w2(X4) ≠ 0`. Candidates:

1. **Spin-c-induced (`U(1)`-reducible) twist.** `V = L ⊕ L^{-1}` for a complex line `L` with
   `c1(L) ≡ pi*w2(X4)` mod 2. **Not canonical:** depends on the choice of `L` (any `L` with the
   right mod-2 reduction works; they differ by 2-torsion-free shifts), and its index behaviour is
   the spin-c behaviour (§4). `[reconstruction]`
2. **GU's intrinsic quaternionic structure.** `S = H^64` (from `Cl(9,5) = M(64,H)`) carries a
   natural **right-`H` action**, i.e. a *global* `Sp(1)` = unit-quaternion symmetry. This is the
   obvious GU-canonical Sp(1) — but it is the **trivial** principal Sp(1) bundle: `w2 = 0`, `c2 = 0`.
   Its `w2` matches `w2(Y14)=pi*w2(X4)` **only when X4 is spin**. So GU's intrinsic Sp(1) does NOT
   provide the non-trivial twist required for a non-spin base. `[reconstruction]`
3. **A GU-derived non-trivial Sp(1) bundle.** Would have to come from a distinguished sub-bundle of
   the `Sp(64)` gauge/Clifford data with `w2 = pi*w2(X4)`. **No such canonical sub-bundle is
   identified in the current formalization.** `[OPEN]`

**Conclusion (ii).** The only canonical object (the global right-`H` action) is the trivial twist
that needs X4 spin anyway; every non-trivial Spin^h structure requires a non-canonical extra choice.
**There is no canonical quaternionic relaxation of the spin precondition.** `[reconstruction]`

## 4. (iii) Index — H-linearity restored, value not preserved

**4.1 H-linearity is genuinely restored (the one real win).** The Spin^h spinor bundle is locally
`W = Δ_n ⊗_C V`, `V` = the `Sp(1)`-fundamental `C^2 ≅ H`. `Sp(1)` acts on `H` by LEFT multiplication,
which **commutes with right-`H` multiplication**; an `Sp(1)`-connection preserves the right-`H`
structure, so the Spin^h Dirac operator `D^h` is **right-`H`-linear** and `ind_H(D^h)` is well-defined.

This is exactly the defect spin-c could not fix. W2-FC1's spin-c twist is `S ⊗_C L^{1/2}` — a tensor
**over C** with a genuinely complex line; the `j ∈ H` action does not descend, so H-linearity dies.
Spin^h twists by a **quaternionic** line (`Sp(1)`), staying in `H`-land. **So Spin^h repairs the
H-linearity objection of W2-FC1.** `[reconstruction — Sp(1) left-mult vs right-H commutation]`

This does NOT contradict canon: W2-FC1's "breaks H-linearity" statement was about the literal
`⊗_C L^{1/2}` spin-c twist, which is correct. W2-FC2's content is that the *Spin^h completion* of
that twist restores H-linearity. No correction to W2-FC1 is implied.

**4.2 But the index value still shifts.** Compact Spin^h index (Atiyah–Singer, treating the twist
`ch(V)` formally; valid where a compact model applies):

```
ind_C(D^h) = ∫_M Â(M) · ch(V),    V the C^2 = H twist,  c1(V)=0,  ch(V) = 2 + ch_2(V) + ...
                                   ch_2(V) = -c2(V)
```

On a compact 4-manifold internal factor (the compact-K3 toy model, dim 4):

```
ind_C(D ⊗ V)|_{K3} = ∫_{K3} (1 + Â_4)(2 + ch_2(V))
                   = 2 · ∫_{K3} Â_4  +  ∫_{K3} ch_2(V)
                   = 2 · Â(K3)  -  ⟨c2(V), [K3]⟩
                   = 4 - k,       k := ⟨c2(V),[K3]⟩  (the Sp(1) instanton number)
```

So `k ≠ 0` shifts the index. Packaged with GU's Clifford rank factor (spin-1/2 leg
`8·Â(K3) = 16`, the `8 = rank_H S(6,4)`):

```
ind_H(D^h_{1/2}) = 8 · (Â(K3) + δ),     δ = -k / (normalization),
generations = ind_H / 8 = Â(K3) + δ = 2 + δ.
```

**A non-trivial Sp(1) twist (`k ≠ 0`) moves the generation count directly by `δ`.** For a
`U(1)`-reducible twist `V = L ⊕ L^{-1}`, `c2(V) = -c1(L)^2`, so `k = -⟨c1(L)^2,[K3]⟩` — recovering
exactly the spin-c shift `(c1^2 - σ)/8` flagged in W2-FC1. So the index objection is identical
for spin-c and for `U(1)`-reduced Spin^h; only the H-linearity differs. `[reconstruction —
Â·ch(V); SU(2)-fundamental Chern character]`

**4.3 Could a clever twist keep `δ = 0`?** The constraint is `w2(E) = pi*w2(X4)` (degree 2,
pulled from the spacetime base). The index shift `δ` is governed by `c2(V)` restricted to the
**internal 4-cycle** (degree 4). These are independent: `w2 ≠ 0` does not force `c2|_{internal} ≠ 0`.
So a `δ = 0` twist is not *a priori* excluded — BUT exhibiting one and showing it is canonical
requires the **compact-K3 reduction** that identifies the internal 4-cycle and pushes the Y14
problem to a K3 computation. That reduction is itself **OPEN / heuristic** (no-go map §2.4: "the
compact APS/K3 formula `ind_H = 8·Â(K3)+8 = 24` is a compact-toy-model heuristic; Atiyah–Singer is
the COMPACT theorem and does not apply on non-compact Y14"). **So the index-preservation question
is conditional on an unestablished reduction; it cannot be settled affirmatively in current GU.**
`[OPEN — depends on the compact-K3 reduction, separately OPEN]`

**4.4 Deepest honesty point.** Even the BASELINE `8·Â(K3) = 16` is OPEN (reconstruction-grade,
compact-toy-model heuristic per no-go map §2.4 and `canon/w2-y14-spin-structure.md`). W2-FC2 asks
whether a Spin^h twist preserves an **already-unestablished** number. The most that can be claimed:
Spin^h does not *automatically* fix the value, and offers no canonical zero-shift choice.

## 5. Answer to W2-FC2

| Sub-question | Answer | Grade |
|---|---|---|
| (i) Spin^h exists on Y14 for non-spin X4? | **YES**, unconditionally (Spin-c ⊂ Spin^h; `W3(Y14)=0`) | RESOLVED |
| (ii) Canonical (GU-distinguished) choice? | **NO** — only canonical Sp(1) is the trivial one (needs X4 spin) | reconstruction |
| (iii) Preserves `ind_H` (H-linearity)? | **YES** — Sp(1) right-action keeps `D^h` H-linear | reconstruction |
| (iii) Preserves the VALUE `8·Â(K3)=16`? | **NO / not establishable** — non-trivial twist shifts by `8δ`; `δ=0` needs the OPEN compact-K3 reduction | OPEN |
| Net: does Spin^h relax "X4 spin"? | **NO** (no canonical generation-preserving structure) | CONDITIONALLY_RESOLVED |

**The spin precondition (W2-01 / W2-FC1) stands.** Spin^h's contribution is to *isolate* the real
barrier: it repairs H-linearity, leaving the **index shift** as the sole, sharper obstruction.

## 6. Failure conditions (falsifiers of this disposition)

1. **(FC-A — existence wrong).** If `W3(Y14) ≠ 0` for some orientable X4 (contradicting W2-FC1's
   `W3(Y14)=pi*W3(X4)=0`), then Spin-c ⊄ existence and the §2 existence claim fails. Test: recompute
   `beta(w2(Y14))` directly; check no vertical `W3` piece was dropped (same error-class as W2-01).
2. **(FC-B — canonical twist exists).** If a distinguished non-trivial Sp(1) sub-bundle of the
   `Sp(64)`/Clifford data with `w2 = pi*w2(X4)` is exhibited (e.g. forced by the gimmel field or the
   solution locus), then (ii) flips to "canonical exists" and the relaxation may go through. Test:
   search GU's bundle data for an `Sp(1)` reduction with the required `w2`; check it is unique/forced.
3. **(FC-C — zero-shift twist on the internal cycle).** If, under a *valid* compact reduction, a
   Spin^h twist can satisfy `w2 = pi*w2(X4)` with `⟨c2(V), internal-4-cycle⟩ = 0`, then `δ = 0` and
   the count is preserved — overturning the "generically shifted" reading of (iii). Test: identify
   the internal 4-cycle from the reduction and compute `c2(V)|_cycle` for the minimal admissible twist.
4. **(FC-D — H-linearity claim wrong).** If the Spin^h `D^h` is in fact NOT right-`H`-linear for a
   `U(1)`-reducible twist (i.e. the §4.1 left-mult/right-mult commutation fails in the GU module
   `M(64,H)`), the one claimed advance evaporates and Spin^h is no better than spin-c. Test: explicit
   matrix check that the `Sp(1)` connection commutes with right-`H` on `H^64` (cf. the FC-EPSILON
   discipline of MO-05).
5. **(FC-E — baseline collapse).** If the compact-K3 reduction underlying `8·Â(K3)=16` is shown
   invalid (no-go map GC-FC4), then "preserve the value" is vacuous and W2-FC2 dissolves into the
   prior OPEN index problem rather than resolving. Test: status of the non-compact→compact-K3 gate.

## 7. What this does NOT establish

- It does NOT establish `ind_H(D_GU) = 24` or 3 generations (that is OPEN regardless; baseline
  `8·Â(K3)=16` is a compact-toy heuristic, Atiyah–Singer inapplicable on non-compact Y14).
- It does NOT prove that *no* canonical Spin^h structure can ever exist — only that none is present
  in the current formalization (FC-B remains the live reopener).
- It does NOT compute the actual non-compact Spin^h index (the APS/L²/Fredholm framework that
  actually applies on open Y14 is untouched here; this section is compact-model heuristic).
- It does NOT change the spacetime spin precondition: GU's generation machinery still requires X4
  spin; Spin^h relabels, not removes, the obstruction.

## 8. Proposed DERIVATION-PROGRESS entry

> ### W2-FC2 — CONDITIONALLY_RESOLVED — Spin^h exists but does not canonically relax X4-spin (2026-06-26)
>
> **Opened by:** W2-FC1. **Question:** does Y14 admit a canonical Spin^h structure preserving
> `ind_H` and `8·Â(K3)=16`?
>
> **(i) Existence — YES, unconditional.** Y14 is Spin-c (`W3(Y14)=0`, W2-FC1) and `Spin^c ⊂ Spin^h`,
> so Y14 is Spin^h for any orientable X4 (incl. non-spin CP2). The `dim ≤ 7 ⇒ Spin^h` theorem does
> NOT apply (Y14 is 14-dim); existence comes from the specific Spin-c result.
> **(ii) Canonicity — NO.** GU's only canonical Sp(1) is the global right-`H` action on `S=H^64`,
> which is the TRIVIAL twist (`w2=c2=0`) and matches `w2(Y14)=pi*w2(X4)` only when X4 is spin. Every
> non-spin-base Spin^h structure needs a non-canonical extra Sp(1)/SO(3) bundle with `w2=pi*w2(X4)`.
> **(iii) Index — H-linearity restored, value not.** A genuine Sp(1) twist keeps `D^h` right-`H`-linear
> (the one improvement over the spin-c twist of W2-FC1), so `ind_H` is defined. But
> `ind = 8·(Â(K3)+δ)`, `δ ∝ ⟨c2(V), internal-4-cycle⟩`; a non-trivial twist shifts off 16 (for a
> `U(1)`-reducible twist `δ` recovers the spin-c shift `(c1^2-σ)/8`). Whether a `δ=0` twist with the
> required `w2` exists/is canonical depends on the OPEN compact-K3 reduction — not establishable in
> current GU.
> **Net: the X4-spin precondition STANDS.** Spin^h's real contribution is to ISOLATE the barrier —
> it fixes H-linearity, leaving the index shift as the sole, sharper obstruction. Verdict:
> **W2-FC2 CONDITIONALLY_RESOLVED** (≥3 failure conditions FC-A..FC-E). Reopen via FC-B (a GU-forced
> canonical Sp(1)) or FC-C (a zero-shift internal-cycle twist under a valid reduction).
> Exploration: `explorations/anomaly-and-bordism/w2-fc2-spin-h-enhancement-2026-06-26.md`.

## References

- Albanese, M. & Milivojević, A., "Spin^h and further generalisations of spin", J. Geom. Phys. 168
  (2021) 104297. (`Spin^h(n)=(Spin(n)xSp(1))/Z2`; obstruction `w2(TM)=w2(E)`; dim ≤ 7 always Spin^h.)
- Atiyah, M. & Singer, I., "The index of elliptic operators III", Ann. Math. 87 (1968). (Twisted
  Dirac index `∫ Â·ch(V)`.)
- `canon/w2-y14-spin-structure.md` (W2-01: `w2(Y14)=pi*w2(X4)`).
- `DERIVATION-PROGRESS.md` W2-FC1 (Spin-c exists but does not rescue GU; spin precondition).
- `canon/no-go-class-relative-map.md` §2.4 (compact-K3 toy-model heuristic; `8·Â(K3)=16`; GC-FC4).
