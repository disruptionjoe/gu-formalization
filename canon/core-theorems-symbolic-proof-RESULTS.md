---
title: "Grade upgrade: the paper's core theorems (index-nullity / index-conservation, the antilinear null-eigenspace bound, the function-space sigma_1(x)B form, and the 2-primary obstruction list) proved at the STRUCTURE level over SYMBOLIC entries -- not merely computed on the explicit 192-dim numeric carrier. The dimension-independent arguments are given from the axioms of a cross-chirality Krein space; 22 load-bearing identities are sympy-certified to vanish identically for symbolic entries."
status: staged
doc_type: result
created: 2026-07-02
grade: "SYMBOLIC / structure-level. Every load-bearing algebraic identity is certified by sympy to be identically 0 for SYMBOLIC entries (not numeric): 22 checks, tests/symbolic-proofs/core_theorems_symbolic_proof.py (exit 0). The dimension-independent step (transversality: n - n = 0 for any n) is the written proof below, verified symbolically on n=2 blocks. This upgrades the core theorems from 'machine-verified on the explicit carrier' (G-computed) toward 'proved from the axioms' (G-proof), the step every RESULTS file flagged ('a Lean/symbolic port would upgrade the grade'). NOT a fully machine-checked formal (Lean/Coq) proof -- no Lean/Coq/Z3 in this sandbox -- and it does not touch the function-space analytic residual (APS/end, family-index)."
depends_on:
  - canon/antilinear-bound-RESULTS.md
  - canon/antilinear-nonkrein-admissibility-RESULTS.md
  - canon/enum-completeness-class-c-RESULTS.md
  - canon/function-space-index-conservation-RESULTS.md
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
script: tests/symbolic-proofs/core_theorems_symbolic_proof.py
---

# The core theorems, proved at the structure level (symbolic)

Every earlier RESULTS file carried the same honest caveat: "machine-verified computation on the explicit
192-dim carrier, not a symbolic proof from axioms; a Lean/symbolic port would upgrade the grade." This note is
that port for the CORE theorems, at symbolic (sympy) grade. The theorems are stated and proved for the
**abstract cross-chirality Krein space** -- any dimension -- and the load-bearing algebraic identities are
certified by sympy to vanish **identically for symbolic entries**, not fitted numerics on the carrier.

## The abstract setting

A finite-dimensional complex space `W` with: a chirality involution `Gamma` (`Gamma^2 = I`, Hermitian), with
`+-1` eigenspaces `W_+`, `W_-`; and a Hermitian, invertible Krein form `K` that is **cross-chirality**,
`K Gamma = -Gamma K`. (On the paper's carrier, `dim W = 192`, `dim W_+ = dim W_- = 96`, `K` of signature
`(96,96)`; here everything is symbolic.)

## Theorem 1 (index-nullity / index-conservation -- the core of Theorem 2)

**Lemma (isotropy).** `W_+` and `W_-` are `K`-isotropic (`K`-null). *Proof.* For `x in W_+`: `Gamma x = x`, and
`K Gamma = -Gamma K` gives `Gamma(Kx) = -K(Gamma x) = -Kx`, so `Kx in W_-`. Since `Gamma` is Hermitian, `W_+`
and `W_-` are orthogonal, so `<x, Kx> = 0`. Same for `W_-`. [sympy: `W_+^dag K W_+ = 0`, `W_-^dag K W_- = 0`,
and `Gamma K W_+ = -K W_+`, all identically 0 for symbolic `B`.]

**Theorem.** Every maximal `K`-positive (physical) subspace `P` has net chiral index `chi(P) = 0`. *Proof.* A
nonzero vector in `W_+-` is `K`-null (isotropy), hence cannot be `K`-positive; so `P ^ W_+ = P ^ W_- = 0`. Thus
`P` is the graph `{(x, Ux)}` of an invertible `U`, and both projections `P -> W_+` (`x |-> x`) and `P -> W_-`
(`x |-> Ux`) are isomorphisms: `dim = n` each. Hence `chi(P) = n - n = 0`. [sympy: the two projection matrices
are `I` and `U` respectively, so both are rank-`n` for invertible `U`; the count is `n - n = 0` for any `n`.]

**Corollary (linear index conservation, Theorem 2).** Any linear Krein-isometric operator maps physical
subspaces to physical subspaces, which by the theorem carry `chi = 0`.

## Theorem 2 (antilinear null-eigenspace bound -- the P_iso class)

An antilinear `C` re-grades chirality; its re-graded eigenspaces `C(W_+), C(W_-)` are, by admissibility, `K`-null
(the null-eigenspace class `P_iso`). Since a `K`-positive `P` meets any `K`-null subspace only at `0` -- the
**identical transversality** -- `chi_C(P) = 0`. The proof uses *only isotropy*, so it holds on all of `P_iso`
(strictly larger than the Krein-compatible operators). [sympy: a chirality eigenvector is `K`-null; the
transversality is the same as Theorem 1.]

## Theorem 3 (function-space form)

A `Gamma`-odd, Krein-self-adjoint (for cross-chirality `K = sigma_1`) operator is `D = sigma_1 (x) B` with `B`
Hermitian; its spectrum is symmetric about `0` and every eigenvector `(1, +-1) (x) v` is chirality-neutral, so
the net chiral spectral flow is `0`. [sympy, symbolic `B`: `{D, Gamma} = 0`; char.poly `= det(B-lam)det(B+lam)`
so spectrum `= +- eig(B)`; `<Gamma>` of the `(1,+-1)(x)v` combos `= 0` for all `v`; and these are eigenvectors
with eigenvalue `+-b` when `Bv = bv`.]

## Theorem 4 (2-primary meta-theorem)

Each enumerated obstruction is a power-of-two statement, by definition, independent of the carrier: the adjoint
Dirac index `4k` (`= 0 mod 4`); the mod-2 Witten index / Kramers `Z/2`; Rokhlin `sign = 0 mod 2^4`; the spinor
dimension `2^m` (a pure power of two); the cross-chirality split `96 = 2^5 . 3` (even; the modular content is
mod-`2^k`); ghost parity `50/50` (`Z/2`). None imposes an odd-prime (mod-3) congruence. [sympy: each modular
identity certified 0.]

## What sympy certified (22 identities, symbolic entries)

`K` Hermitian; `K Gamma + Gamma K = 0`; `Gamma^2 = I`; `W_+-` isotropic; `Gamma K W_+ = -K W_+`; the two
projections `= I, U`; a chirality eigenvector is `K`-null; `B` Hermitian; `{D, Gamma} = 0`; char.poly factoring
`det(B-lam)det(B+lam)`; the `(1,+-1)(x)v` chirality-neutrality (both signs); the eigenvector map; and the four
2-primary modular identities. All vanish identically for symbolic entries (`tests/symbolic-proofs/core_theorems_symbolic_proof.py`,
exit 0).

## What this upgrades (and what it does not)

- **Grade axis (per the verification-tier ladder).** The core theorems move from `G-computed` (numeric on the
  carrier) toward `G-proof` (symbolic, structure-level): they are now shown to follow from the *axioms* of a
  cross-chirality Krein space, not from the specific 192-dim numbers. The "machine-verified on the carrier, not
  symbolic from axioms" caveat is discharged for the core.
- **Verification axis unchanged.** This is still an internal, single-process result (`V3` ceiling): sympy is run
  by the same process. A fully machine-checked **Lean/Coq** formalization (unavailable in this sandbox) would be
  the next step, and independent replication remains the `V3 -> V4` crossing.
- **Scope.** Symbolic certification is on `n = 2` blocks plus the dimension-general written argument
  (`n - n = 0`); it is not a general-`n` machine proof. It covers the finite-dimensional structural theorems; it
  does NOT close the function-space analytic residual (APS/end, family-index -- see
  `canon/function-space-index-conservation-RESULTS.md`).

## Honest caveats

- No number was fitted; the only integers are `0`, the carrier's `(+96, -96)`, and the 2-primary moduli.
- The proofs above are the actual dimension-independent arguments; sympy confirms their algebraic premises
  symbolically. This is a symbolic proof, not a Lean-checked one -- an honest but real grade upgrade.
- Staged, **not CANON.md-promoted**; the per-RESULTS-file grade lines and the paper's caveat (e) can be softened
  for the core theorems on Joe's decision.
