#!/usr/bin/env python3
"""Design certificate: SIGNATURE-AMBIENT relative-sign resolver route.

Certifies, in exact rational arithmetic, every numeric claim in the design
packet explorations/signature-ambient-relative-sign-resolver-design-packet-2026-08-11.md:

  T1  The DeWitt-family G_lam(h,h) = <h,h>_g - lam*(tr_g h)^2 on the
      10-dimensional Sym^2 fiber over a Lorentzian 4-base has plus-first
      signature (7,3) for lam < 1/4 and (6,4) for lam > 1/4, with the
      traceless sector fixed at (6,3).  Achievable set: {(7,3), (6,4)}.
  T2  Every G_lam is EVEN in g (bit-identical Gram under g -> -g), while the
      horizontal block g^{-1} is ODD (flips sign), on both Lorentzian
      conventions.
  T3  Under POSITIVE normalization the achievable set is mirror-asymmetric:
      {(7,3),(6,4)} vs mirror {(3,7),(4,6)} disjoint.  Corroboration only --
      see T6 for the caveat that demotes label-typing.
  T4  THE LOAD-BEARING INVARIANT -- uniform-sum balances: the draft display
      (1,3)+(6,4)=(7,7) balances to |p-q|=0 as written AND mirrored; the
      transcript blocks (4,6)+(1,3) balance to |p-q|=4 as written AND
      mirrored.  Balances are invariant under uniform relabeling, so each
      source display wears its relative-sign bit on its face.  The planted
      mixed-notation sum reaches balance 0 and must be CAUGHT by any audit.
  T5  Label typing under positive normalization (corroboration only, per
      T6): transcript labels {(3,7),(3,6),(4,6)} are family-members only
      minus-first; draft label (6,4) only plus-first; planted (5,5) is
      NOT-IN-FAMILY either way.
  T6  The caveat, certified: with a free overall sign the full portrait
      {(7,3),(6,4),(3,7),(4,6)} is mirror-symmetric, so bare labels do NOT
      fix a convention -- which is why T4's balances, not T5's labels, carry
      the packet.  Also certified: on 14 dimensions balance 0 pins the
      unordered pair {7,7} and balance 4 pins {9,5} -- exactly the registry's
      two horns, and {7,7} is self-mirror.
"""

from fractions import Fraction as F
import itertools, sys

def sym_basis(n=4):
    return [(a, b) for a in range(n) for b in range(a, n)]

def gram_dewitt(ginv, lam, n=4):
    """Exact Gram matrix of G_lam on Sym^2 coordinates h_ab (a<=b)."""
    basis = sym_basis(n)
    def G(h1, h2):
        # <h1,h2>_g = ginv[a][c] ginv[b][d] h1_ab h2_cd  (full index sums)
        s = F(0)
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    for d in range(n):
                        s += ginv[a][c] * ginv[b][d] * h1[a][b] * h2[c][d]
        t1 = sum(ginv[a][b] * h1[a][b] for a in range(n) for b in range(n))
        t2 = sum(ginv[a][b] * h2[a][b] for a in range(n) for b in range(n))
        return s - lam * t1 * t2
    mats = []
    for (a, b) in basis:
        m = [[F(0)] * n for _ in range(n)]
        m[a][b] = F(1); m[b][a] = F(1)  # symmetric basis element
        mats.append(m)
    return [[G(mi, mj) for mj in mats] for mi in mats]

def signature(M):
    """Exact (pos, neg, zero) via symmetric row/col pivoting (Lagrange)."""
    M = [row[:] for row in M]; n = len(M); pos = neg = zero = 0
    for _ in range(n):
        n_cur = len(M)
        if n_cur == 0: break
        piv = next((i for i in range(n_cur) if M[i][i] != 0), None)
        if piv is None:
            found = None
            for i in range(n_cur):
                for j in range(i + 1, n_cur):
                    if M[i][j] != 0: found = (i, j); break
                if found: break
            if found is None:
                zero += n_cur; M = []; break
            i, j = found
            for r in range(n_cur): M[r][i] += M[r][j]
            for c in range(n_cur): M[i][c] += M[j][c]
            piv = i
        d = M[piv][piv]
        if d > 0: pos += 1
        else: neg += 1
        rows = [r for r in range(len(M)) if r != piv]
        M = [[M[r][c] - M[r][piv] * M[piv][c] / d for c in rows] for r in rows]
    return pos, neg, zero

def diag(*e):
    n = len(e); return [[F(e[i]) if i == j else F(0) for j in range(n)] for i in range(n)]

ok = True
def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and cond

# Lorentzian bases, both conventions (g diagonal => ginv = diag(1/e_i)).
g_mostly_plus  = (-1, 1, 1, 1)   # repo (3,1): 3 positive, 1 negative
g_mostly_minus = (1, -1, -1, -1) # repo (1,3)
inv = lambda e: diag(*[F(1, x) for x in e])

# T1: lambda sweep on both conventions.
for tag, e in (("mostly-plus", g_mostly_plus), ("mostly-minus", g_mostly_minus)):
    for lam, want in ((F(0), (7, 3, 0)), (F(1, 8), (7, 3, 0)), (F(1), (6, 4, 0)),
                      (F(1, 2), (6, 4, 0)), (F(1, 4), (6, 3, 1))):
        got = signature(gram_dewitt(inv(e), lam))
        check(f"T1 {tag} lam={lam}: signature {got} == {want}", got == want)

# T1b: traceless sector fixed (6,3): read off from the lam=1/4 degenerate case
# (zero mode is the trace line), already checked above.

# T2: evenness of the fiber Gram under g -> -g (bit-identical), oddness of g^{-1}.
for lam in (F(0), F(1)):
    A = gram_dewitt(inv(g_mostly_plus), lam)
    B = gram_dewitt(inv(tuple(-x for x in g_mostly_plus)), lam)
    check(f"T2 fiber Gram bit-identical under g->-g (lam={lam})", A == B)
neg_inv = inv(tuple(-x for x in g_mostly_plus))
check("T2 horizontal block odd: (-g)^{-1} == -(g^{-1})",
      neg_inv == [[-v for v in row] for row in inv(g_mostly_plus)])

# T3: mirror-asymmetry of the achievable set.
ach = {(7, 3), (6, 4)}
check("T3 achievable set disjoint from its mirror",
      ach.isdisjoint({(b, a) for (a, b) in ach}) and (6, 3) != (3, 6))

# T4: uniform-convention sum tables (pairs as written; convention = reading).
def balance(pairs):
    p = sum(a for a, b in pairs); q = sum(b for a, b in pairs); return abs(p - q)
draft = [(1, 3), (6, 4)]        # TX^{1,3} + N^{6,4} as written
trans = [(1, 3), (4, 6)]        # spoken horizontal (1,3) + vertical (4,6)
check("T4 draft display balances to 0 as written", balance(draft) == 0)
check("T4 draft display balances to 0 mirrored",
      balance([(b, a) for (a, b) in draft]) == 0)
check("T4 transcript blocks balance to 4 as written", balance(trans) == 4)
check("T4 transcript blocks balance to 4 mirrored",
      balance([(b, a) for (a, b) in trans]) == 4)
# Planted mixed-sum control: transcript horizontal read in the OPPOSITE
# convention from the vertical reaches balance 0 -- the audit must flag it.
mixed = [(3, 1), (4, 6)]
check("T4 planted mixed-notation sum reaches balance 0 (must be flagged)",
      balance(mixed) == 0)

# T5: label typing against the family (raw/trace-flipped 10-dim members and
# the 9-dim traceless sector {(6,3)}).
fam10, fam9 = {(7, 3), (6, 4)}, {(6, 3)}
def types_as(label, fam):
    plus = label in fam; minus = (label[1], label[0]) in fam
    return ("plus-first" if plus else "") + ("minus-first" if minus else "")
check("T5 transcript raw (3,7) types minus-first", types_as((3, 7), fam10) == "minus-first")
check("T5 transcript traceless (3,6) types minus-first", types_as((3, 6), fam9) == "minus-first")
check("T5 transcript flipped (4,6) types minus-first", types_as((4, 6), fam10) == "minus-first")
check("T5 draft (6,4) types plus-first", types_as((6, 4), fam10) == "plus-first")
check("T5 planted (5,5) types as NOT-IN-FAMILY", types_as((5, 5), fam10) == "")

# T6 (two-parameter caveat, certified): with an arbitrary overall sign on the
# fiber form, the achievable portrait is mirror-symmetric -- a bare label does
# NOT self-type its convention. This is why the packet's load-bearing bit is
# the SUM BALANCE of each uniform display (T4), not label typing (T5).
def negate(M): return [[-v for v in row] for row in M]
ok2 = True
for lam, want in ((F(0), (3, 7, 0)), (F(1), (4, 6, 0))):
    got = signature(negate(gram_dewitt(inv(g_mostly_plus), lam)))
    good = got == want
    print(("PASS " if good else "FAIL ") + f"T6 negated family lam={lam}: {got} == {want}")
    ok2 = ok2 and good
full_portrait = {(7, 3), (6, 4), (3, 7), (4, 6)}
sym = full_portrait == {(b, a) for (a, b) in full_portrait}
print(("PASS " if sym else "FAIL ") + "T6 two-parameter portrait is mirror-symmetric (caveat certified)")
ok2 = ok2 and sym
# The self-mirror pin: balance 0 determines the unordered total {7,7} exactly.
pin = sorted([(7, 7)]) == sorted(set((p, q) for p in range(15) for q in range(15)
                                    if p + q == 14 and abs(p - q) == 0))
print(("PASS " if pin else "FAIL ") + "T6 balance-0 on 14 dims pins the unordered pair {7,7}")
ok2 = ok2 and pin
pin4 = sorted(set(tuple(sorted((p, q), reverse=True)) for p in range(15) for q in range(15)
               if p + q == 14 and abs(p - q) == 4)) == [(9, 5)]
print(("PASS " if pin4 else "FAIL ") + "T6 balance-4 on 14 dims pins the unordered pair {9,5}")
ok2 = ok2 and pin4
print("T6 GREEN" if ok2 else "T6 FAILED")
sys.exit(0 if (ok and ok2) else 1)
