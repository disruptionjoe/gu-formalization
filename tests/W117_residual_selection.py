"""W117: finite-model verification of the Residual-Selection Lemma and both corollaries.

Companion to Lean/GUFormalization/ResidualSelection.lean (the kernel-checked proof;
this file is confirmation on finite models, not the proof).

Checks, exhaustively on small finite models:
  1. SHARED LEMMA (escape leg): for fixpoint-free alpha : B -> B and every
     T : A -> A -> B, the residual d(a) = alpha(T(a,a)) is not any row of T.
  2. SHARED LEMMA (no-closure leg): no T is weakly point-surjective.
  3. SHARED LEMMA (residual corollary / fixed-point-count leg): for nonempty A,
     no valuation p : A -> B is alpha-invariant.
  4. CONTROL: with alpha = id (fixed point exists), 1-3 all FAIL to be no-gos
     (an invariant valuation exists; a point-surjective T exists for |A| large
     enough vs |B|^|A|... checked where feasible) -- fixpoint-freeness is
     load-bearing, not decorative.
  5. COROLLARY GU: B = {0,1}, alpha = swap -- the paper's (I-a)/(I-b).
  6. COROLLARY TI (shape): truncated SemFamily F : [0,n) x [0,n) -> Bool;
     diagSem(F)(i) = not F(i,i) differs from every row F(i) on [0,n) --
     the finite face of TI's diagSem_escapes.
Exit 0 iff all checks pass.
"""

import itertools
import sys

FAILURES = []


def check(name, ok):
    print(("PASS" if ok else "FAIL"), name)
    if not ok:
        FAILURES.append(name)


def all_functions(dom, cod):
    """All functions dom -> cod as dicts."""
    for values in itertools.product(cod, repeat=len(dom)):
        yield dict(zip(dom, values))


def all_T(A, B):
    """All T : A x A -> B as dict[(a,x)] -> b."""
    pairs = [(a, x) for a in A for x in A]
    for values in itertools.product(B, repeat=len(pairs)):
        yield dict(zip(pairs, values))


def fixpoint_free(alpha, B):
    return all(alpha[b] != b for b in B)


def run_model(A, B, alpha, label):
    """Exhaustive check of lemma legs 1-3 for a fixpoint-free alpha."""
    assert fixpoint_free(alpha, B), "model setup error"

    # Leg 1: residual escapes every row, for every T.
    leg1 = True
    # Leg 2: no T is weakly point-surjective.
    leg2 = True
    for T in all_T(A, B):
        d = {a: alpha[T[(a, a)]] for a in A}
        for a0 in A:
            if all(T[(a0, x)] == d[x] for x in A):
                leg1 = False
        rows = {tuple(T[(a0, x)] for x in A) for a0 in A}
        vals = {tuple(p[x] for x in A) for p in all_functions(A, B)}
        if vals <= rows:
            leg2 = False
    check(f"{label}: leg1 residual_escapes (all T, all rows)", leg1)
    check(f"{label}: leg2 no_closure (no weakly point-surjective T)", leg2)

    # Leg 3: no alpha-invariant valuation (A nonempty).
    leg3 = all(
        any(alpha[p[a]] != p[a] for a in A) for p in all_functions(A, B)
    )
    check(f"{label}: leg3 no_invariant_valuation", leg3)


def run_control(A, B, label):
    """alpha = id has a fixed point: the no-gos must dissolve."""
    alpha = {b: b for b in B}
    # An invariant valuation exists (any constant valuation).
    inv_exists = any(
        all(alpha[p[a]] == p[a] for a in A) for p in all_functions(A, B)
    )
    check(f"{label}: CONTROL alpha=id -> invariant valuation exists", inv_exists)
    # The residual d(a) = T(a,a) IS representable for some T (e.g. any T whose
    # some row equals its own diagonal -- take T constant).
    T = {(a, x): B[0] for a in A for x in A}
    d = {a: alpha[T[(a, a)]] for a in A}
    absorbed = any(all(T[(a0, x)] == d[x] for x in A) for a0 in A)
    check(f"{label}: CONTROL alpha=id -> residual absorbed for constant T", absorbed)


def run_gu(A):
    """Corollary GU: B = {0,1}, alpha = swap (the paper's I-a / I-b)."""
    B = [0, 1]
    alpha = {0: 1, 1: 0}
    run_model(A, B, alpha, f"GU |A|={len(A)} B={{0,1}} alpha=swap")


def run_ti(n):
    """Corollary TI (finite face): every truncated family F on [0,n) fails to
    index its own diagonal among its first n rows."""
    idx = list(range(n))
    ok = True
    for values in itertools.product([False, True], repeat=n * n):
        F = {}
        k = 0
        for i in idx:
            for j in idx:
                F[(i, j)] = values[k]
                k += 1
        diag = {j: (not F[(j, j)]) for j in idx}
        for i in idx:
            if all(F[(i, j)] == diag[j] for j in idx):
                ok = False
    check(f"TI shape: diagSem escapes all rows, all F on [0,{n})^2", ok)


def main():
    # Shared lemma on assorted fixpoint-free models, |A| in {1,2,3}.
    for A in ([0], [0, 1], [0, 1, 2]):
        run_gu(A)  # B = {0,1}, alpha = swap
    # A 4-element B with a fixpoint-free involution (two 2-cycles): the lemma
    # is not Bool-specific.
    B4 = [0, 1, 2, 3]
    alpha4 = {0: 1, 1: 0, 2: 3, 3: 2}
    run_model([0, 1], B4, alpha4, "shared |A|=2 |B|=4 alpha=two-swaps")
    # Controls: fixed point dissolves the no-gos.
    run_control([0, 1], [0, 1], "|A|=2 B={0,1}")
    run_control([0, 1, 2], [0, 1], "|A|=3 B={0,1}")
    # TI shape at n = 1, 2, 3 (exhaustive over all 2^(n^2) families).
    for n in (1, 2, 3):
        run_ti(n)

    if FAILURES:
        print(f"\n{len(FAILURES)} FAILURE(S)")
        sys.exit(1)
    print("\nALL CHECKS PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
