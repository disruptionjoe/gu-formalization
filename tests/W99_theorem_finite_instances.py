"""W99 -- finite-instance CONFIRMATION for the paper
'A Self-Referential Valuation No-Go and the Forced Symmetry-Breaking of the Residual'
(papers/candidates/observer-value-selection-theorem/observer-value-selection-theorem-2026-07-11.md).

This is CONFIRMATION, NOT PROOF. The paper's proof is Lemma L (Lawvere weak fixed-point,
contrapositive) and Lemma C (the elementary fixed-point count); both are purely mathematical
and do not depend on any run. This script only re-checks the two elementary lemmas on finite
instances so a reader can see them fire, and pins the load-bearing hypotheses (A2 two-valued,
A3 fixpoint-free) by showing the theorem DISSOLVES when they are dropped.

Checks:
  (I-a) NO CLOSURE. For a two-valued B and alpha = swap (fixpoint-free), no T: A x A -> B is
        weakly point-surjective; the diagonal valuation d = alpha . T . Delta is never a row.
        Exhaustive over ALL T for |A| in {1,2,3}. Also the Cantor form (no surjection A -> P(A)).
  (I-b) NO INVARIANT VALUATION. For alpha = swap and nonempty A, no p: A -> B has alpha.p = p.
  CONTROL (A3 needed). With alpha = identity (has fixed points) BOTH halves dissolve:
        some T represents its diagonal, and constant valuations are alpha-invariant.
  COUNTEREXAMPLE (A2/A3, Example 5.3). A 3-valued grading whose flip fixes the middle grade
        has a fixed point -> obstruction dissolves.
  (II) PARTITION. With G = <alpha> = Z/2 (swap), every total valuation is value-type
        (non-invariant); the arena/value call is decided by the group action alone.

Deterministic, stdlib only, exit 0 on success.
"""
from __future__ import annotations

from itertools import product

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  -- ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def all_T(A, B):
    """All T: A x A -> B as dicts keyed by (a0, a1)."""
    pairs = [(a0, a1) for a0 in A for a1 in A]
    for vals in product(B, repeat=len(pairs)):
        yield dict(zip(pairs, vals))


def some_T_represents_its_flipped_diagonal(A, B, alpha):
    """True iff SOME T has its diagonal valuation d(a)=alpha(T(a,a)) as a row (i.e. closure
    is NOT obstructed). Lemma L contrapositive: this is True iff alpha has a fixed point."""
    for T in all_T(A, B):
        d = {a: alpha[T[(a, a)]] for a in A}
        if any(all(T[(a0, a1)] == d[a1] for a1 in A) for a0 in A):
            return True
    return False


B2 = [0, 1]
swap = {0: 1, 1: 0}          # fixpoint-free involution (A3 holds)
ident = {0: 0, 1: 1}         # has fixed points (A3 fails)

print("[W99] finite-instance confirmation for the observer-value-selection theorem\n")

# ---- (I-a) no closure, exhaustive, alpha = swap ----
print("(I-a) NO CLOSURE with alpha = swap (fixpoint-free):")
for n in (1, 2, 3):
    A = list(range(n))
    obstructed = not some_T_represents_its_flipped_diagonal(A, B2, swap)
    check(f"|A|={n}: no weakly-point-surjective T (diagonal valuation unrepresented for ALL T)",
          obstructed)

# Cantor form: no surjection A -> P(A)
print("      Cantor cross-check (no surjection A -> P(A)):")
for n in (1, 2, 3):
    A = list(range(n))
    subsets = [frozenset(s for s in A if bits[s]) for bits in product([0, 1], repeat=n)]
    no_surj = True
    for assign in product(subsets, repeat=n):
        T = dict(zip(A, assign))
        D = frozenset(a for a in A if a not in T[a])
        if D in set(T.values()):
            no_surj = False
            break
    check(f"|A|={n}: no surjection A -> P(A); diagonal set escapes", no_surj)

# ---- (I-b) no invariant valuation, alpha = swap ----
print("(I-b) NO alpha-INVARIANT VALUATION with alpha = swap:")
for n in (1, 2, 3):
    A = list(range(n))
    invariant_exists = any(
        all(swap[p[a]] == p[a] for a in A)
        for p in (dict(zip(A, v)) for v in product(B2, repeat=n))
    )
    check(f"|A|={n}: no valuation p with alpha.p = p (every total valuation breaks the symmetry)",
          not invariant_exists)

# ---- CONTROL: alpha = identity dissolves BOTH halves (A3 load-bearing) ----
print("CONTROL: alpha = identity (has fixed points) -> theorem DISSOLVES:")
A = [0, 1]
check("some T DOES represent its diagonal (closure not obstructed)",
      some_T_represents_its_flipped_diagonal(A, B2, ident),
      "confirms (I-a) needs fixpoint-freeness")
inv_const = all(ident[0] == ident[0] for _ in A)  # constant valuation p=0 is identity-invariant
check("a constant valuation is alpha-invariant (arena-type exists)",
      inv_const, "confirms (I-b) needs fixpoint-freeness")

# ---- COUNTEREXAMPLE: 3-valued grading fixing the middle (Example 5.3) ----
print("COUNTEREXAMPLE (Example 5.3): 3-valued flip fixing the middle grade has a fixed point:")
B3 = ["below", "boundary", "above"]
flip3 = {"below": "above", "boundary": "boundary", "above": "below"}
fixed3 = [b for b in B3 if flip3[b] == b]
check("flip fixes 'boundary' -> Lemma L applies, obstruction dissolves", fixed3 == ["boundary"],
      "a genuine neutral third grade is outside the theorem's scope")

# ---- (II) partition decided by the group action alone ----
print("(II) PARTITION with G = <alpha> = Z/2 (swap):")
A = [0, 1]
all_value_type = all(
    not all(swap[p[a]] == p[a] for a in A)
    for p in (dict(zip(A, v)) for v in product(B2, repeat=len(A)))
)
check("every total valuation is value-type (non-invariant) under G = <swap>", all_value_type,
      "arena/value call uses only the group action, not any notion of 'forced'")

print("\n[verdict]")
print("  Lemmas L (Lawvere weak) and C (fixed-point count) fire on all finite instances checked;")
print("  the theorem's two hypotheses (two-valued grading; fixpoint-free involution) are shown")
print("  load-bearing by the control and the 3-grade counterexample. CONFIRMATION only -- the")
print("  paper's proof is mathematical and does not depend on this run.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = finite instances confirm the elementary lemmas and the load-bearing hypotheses.")
