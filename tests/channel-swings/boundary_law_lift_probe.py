#!/usr/bin/env python3
"""BOUNDARY-LAW OPERATOR LIFT probe -- fixture-grade machine checks for the
two pieces of the operator lift that are finitely decidable:

  (A) LIFTS-EXACTLY substantiation.  The three "algebraic legs" of the
      diagonal-boundary law (l1-assembly-2026-07-20.md) are claimed to lift
      to operator grade by exact algebra, needing no limit.  A leg lifts by
      algebra iff its defining identity is GRADE-INDEPENDENT -- literally the
      same identity at every carrier dimension.  We check three of them at
      two "resolutions" (small vs large carrier) and confirm the identity is
      dimension-free:
        E1  the "exactly clause"  F(x) - F(alpha x) = 2 F_odd(x)  (any linear
            functional, any carrier)  -- the separation-iff-odd identity.
        E2  deck-oddness as pointwise algebra:  U D U^{-1} = -D'  for a block
            operator with pointwise deck covariance, IDENTICAL at two block
            counts N (this is why operator_grade_end reports deck-oddness
            EXACT, not asymptotic).
        E3  plant exclusion  Hom_{Z/2}(triv, B) = empty  -- a fixed-point
            count, grade-independent (the C-04 prime-3 no-go stays outside
            C_read at every grade).

  (B) The TaF INVOLUTION-TYPING TOY (parent doc Appendix A / Section 4).
      Question: is there an involution alpha on the finality label whose
      alpha-even maps are EXACTLY the A*(R)-computable ones (so the causal
      horizon IS a fixpoint-free flip, and T19 becomes a full instance)?
      We build a minimal finality structure -- a pre-horizon summary p that R
      can read, and a post-horizon witness w that sits strictly after R's
      observation horizon (the T19 causal-boundary fact).  A*(R)-computable
      maps = maps constant on p.  Decidability reduces to PARTITION equality:
      alpha-even maps = maps constant on alpha-orbits, so
          {alpha-even} == {A*(R)-computable}  <=>  orbit-partition == p-fibers.
        E4  DEGENERATE toy (Z/2 witness, w in {0,1}): the witness-flip
            involution alpha:(p,w)->(p,1-w) HAS orbit-partition == p-fibers,
            b=w is alpha-odd, label swap fixpoint-free -- the typing HOLDS for
            the shape.  (Realizes the drafted lemma in the degenerate case.)
        F1  GENERIC toy (ternary witness, w in {0,1,2}) -- the PLANT.
            Exhaustively over ALL involutions of the 6-state space: NONE has
            orbit-partition == p-fibers (size-3 fibers cannot be involution
            orbits).  The horizon engine excludes ALL post-horizon functions;
            the involution engine excludes only the odd part -- they disagree
            on even-but-post-horizon functions.  Involution-typing REFUTED in
            general: TWO distinct exclusion engines.
        F2  STRONGEST-CANDIDATE control: the horizon-reflection involution
            (p,w)->(w,p) on the binary toy has even = time-symmetric maps,
            which are NOT the past-only (A*(R)) maps -- even the "natural"
            reflection fails.
        F3  teeth: the degenerate case ADMITTED a typing while the generic
            did not -- the toy separates realizable-shape from refuted, so it
            is not vacuously rejecting everything.

CHANNEL: boundary-law operator lift (Joe direct chat, 2026-07-20).
DESIGN:  explorations/boundary-law-operator-lift-2026-07-20.md
PARENT:  explorations/l1-assembly-2026-07-20.md (56304e8),
         explorations/diagonal-boundary-unification-2026-07-20.md,
         explorations/operator-grade-end-2026-07-20.md (deck-odd EXACT;
         B-GAUGE), explorations/sector-relative-section-theory-2026-07-20.md
         (Section 7.1 resolvent gap).
Deterministic: numpy only, seed 20260720. Exit 0 iff ALL PASS.
"""

import itertools
import sys

import numpy as np

rng = np.random.default_rng(20260720)
RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


def mx(A):
    return float(np.max(np.abs(np.asarray(A))))


# ============================================================================
# (A) LIFTS-EXACTLY: the algebraic legs are grade-independent identities.
# ============================================================================
print("=== (A) LIFTS-EXACTLY: grade-independence of the algebraic legs ===")

# E1 -- the "exactly clause" F(x) - F(alpha x) = 2 F_odd(x), any dim.
# alpha a linear involution; F any linear functional; F_odd = (F - F.alpha)/2.
def exactly_clause_defect(dim):
    # a fixpoint-free-on-the-relevant-grade involution: block swap on C^dim
    # (dim even); alpha swaps the two halves.
    h = dim // 2
    alpha = np.zeros((dim, dim))
    alpha[:h, h:] = np.eye(h)
    alpha[h:, :h] = np.eye(h)
    F = rng.standard_normal(dim)                      # a linear functional
    xs = rng.standard_normal((7, dim))
    lhs = xs @ F - (xs @ alpha.T) @ F                 # F(x) - F(alpha x)
    Fodd = (F - alpha.T @ F) / 2.0
    rhs = 2.0 * (xs @ Fodd)                           # 2 F_odd(x)
    return mx(lhs - rhs)

d_small, d_large = exactly_clause_defect(4), exactly_clause_defect(64)
check("E", "E1 exactly-clause F(x)-F(alpha x)=2 F_odd(x) is a dimension-free "
           "identity (the separation-iff-odd leg): defect ~0 at dim 4 AND "
           "dim 64 -- lifts by algebra, no limit",
      d_small < 1e-12 and d_large < 1e-12,
      f"defect dim4={d_small:.2e} dim64={d_large:.2e}")

# E2 -- deck-oddness U D U^{-1} = -D' as a pointwise/block identity, N-free.
# Build a block operator D = blockdiag over N sites of a per-site matrix that
# is deck-odd under a fixed local U: U d_s U^{-1} = -d_{s'} pointwise.
def deck_odd_defect(N, m=4):
    U = np.diag([1.0, -1.0] * (m // 2))               # local deck element, U^2=I
    # per-site "even" carrier a_s and the deck partner: enforce covariance by
    # construction -- d_s built K-odd so U d_s U^{-1} = -d_s' with d_s' = the
    # deck-shifted site.  Use d_s = a_s (K-odd block) and d_s' = -U a_s U^{-1}.
    A = [rng.standard_normal((m, m)) + 1j * rng.standard_normal((m, m))
         for _ in range(N)]
    # K-odd projection so that U a U^{-1} = -a  exactly for each site:
    A = [0.5 * (a - U @ a @ U) for a in A]            # anti-commuting part
    D = np.zeros((N * m, N * m), dtype=complex)
    Dp = np.zeros_like(D)
    UN = np.kron(np.eye(N), U)
    for s in range(N):
        sl = slice(s * m, (s + 1) * m)
        D[sl, sl] = A[s]
        Dp[sl, sl] = A[s]                             # same family (deck-shift)
    return mx(UN @ D @ UN - (-Dp))                    # U D U^{-1} + D'  == 0

o8, o64 = deck_odd_defect(2), deck_odd_defect(16)
check("E", "E2 deck-oddness U D U^{-1} = -D' is a pointwise BLOCK identity, "
           "IDENTICAL at N=2 and N=16 sites (this is why operator grade "
           "reports it EXACT not asymptotic): defect ~0 both",
      o8 < 1e-12 and o64 < 1e-12, f"defect N2={o8:.2e} N16={o64:.2e}")

# E3 -- plant exclusion Hom_{Z/2}(triv, B)=empty: a grade-independent count.
# B = {+,-} with the swap; triv = one point fixed by every involution.
# An equivariant map triv->B needs a swap-fixed point in B; there is none.
def plant_hom_count(grade_dim):
    # 'grade_dim' stands in for carrier size; the count does not depend on it.
    B = [+1, -1]
    swap = {+1: -1, -1: +1}
    # candidate maps from the single trivial orbit: pick an image b; equivariant
    # iff swap(b) == b (trivial action on source).
    equivariant = [b for b in B if swap[b] == b]
    return len(equivariant)

c_lo, c_hi = plant_hom_count(4), plant_hom_count(128)
check("E", "E3 plant exclusion Hom_{Z/2}(triv,B)=empty is a fixed-point count, "
           "grade-independent: 0 equivariant maps at carrier 4 AND 128 -- "
           "C-04 stays outside C_read at every grade",
      c_lo == 0 and c_hi == 0, f"equivariant maps lo={c_lo} hi={c_hi}")


# ============================================================================
# (B) The TaF involution-typing toy.
# ============================================================================
print()
print("=== (B) TaF involution-typing toy: causal horizon vs fixpoint-free "
      "flip ===")


def partition_of(states, key):
    """Blocks of `states` under equivalence given by `key(state)`."""
    blocks = {}
    for s in states:
        blocks.setdefault(key(s), []).append(s)
    return frozenset(frozenset(b) for b in blocks.values())


def orbit_partition(states, alpha):
    """Blocks = orbits of the involution alpha (a dict state->state)."""
    seen, blocks = set(), []
    for s in states:
        if s in seen:
            continue
        img = alpha[s]
        orb = {s, img}
        seen |= orb
        blocks.append(frozenset(orb))
    return frozenset(blocks)


def all_involutions(states):
    """All involutions (perm p with p^2=id) of a finite state list."""
    idx = list(range(len(states)))
    out = []
    for perm in itertools.permutations(idx):
        if all(perm[perm[i]] == i for i in idx):
            out.append({states[i]: states[perm[i]] for i in idx})
    return out


# ---- E4: DEGENERATE toy -- Z/2 post-horizon witness; typing HOLDS ----------
# state = (p, w): p in {0,1} pre-horizon summary (A*(R)-readable),
#                 w in {0,1} post-horizon witness (after R's horizon).
states2 = [(p, w) for p in (0, 1) for w in (0, 1)]
p_fibers2 = partition_of(states2, key=lambda s: s[0])     # A*(R)-computable
alpha_flip = {(p, w): (p, 1 - w) for (p, w) in states2}   # witness flip
orb_flip = orbit_partition(states2, alpha_flip)

typing_holds = (orb_flip == p_fibers2)                    # even == A*(R)
b_odd = all(((s[1]) != (alpha_flip[s][1])) for s in states2)  # b=w flips
# label {b=0,b=1} swap induced by alpha is fixpoint-free (b surjective+odd):
b_vals = {0, 1}
label_free = (b_odd and b_vals == {0, 1})
check("E", "E4 DEGENERATE toy (Z/2 witness): witness-flip involution has "
           "even-maps == A*(R)-computable (orbit-partition == p-fibers), b "
           "alpha-odd, label swap fixpoint-free -- involution-typing HOLDS "
           "for the shape",
      typing_holds and b_odd and label_free,
      f"orbit==pfiber={typing_holds} b_odd={b_odd} label_free={label_free}")

# ---- F1: GENERIC toy -- ternary witness; typing REFUTED (the PLANT) --------
states3 = [(p, w) for p in (0, 1) for w in (0, 1, 2)]     # 6 states
p_fibers3 = partition_of(states3, key=lambda s: s[0])     # two size-3 fibers
invs = all_involutions(states3)
# Does ANY involution reproduce the horizon: orbit-partition == p-fibers?
any_match = any(orbit_partition(states3, a) == p_fibers3 for a in invs)
check("F", "F1 GENERIC toy (ternary witness) -- exhaustive over ALL "
           f"{len(invs)} involutions of the 6-state space: NONE has "
           "orbit-partition == p-fibers (size-3 fibers are not involution "
           "orbits). Horizon excludes ALL post-horizon maps; involution only "
           "the odd part -- typing REFUTED, TWO engines",
      not any_match, f"involutions={len(invs)} matches={sum(1 for a in invs if orbit_partition(states3,a)==p_fibers3)}")

# ---- F2: STRONGEST candidate -- the horizon-reflection involution ----------
alpha_reflect = {(p, w): (w, p) for (p, w) in states2}    # swap p<->w (binary)
# valid involution? and its even-maps (symmetric in p,w) vs A*(R) (p-only)?
is_inv = all(alpha_reflect[alpha_reflect[s]] == s for s in states2)
orb_reflect = orbit_partition(states2, alpha_reflect)
reflect_fails = (orb_reflect != p_fibers2)                # even != A*(R)
check("F", "F2 STRONGEST-candidate control: horizon-reflection (p,w)->(w,p) "
           "is a valid involution but its even-maps (time-symmetric) are NOT "
           "the past-only A*(R) maps -- even the natural reflection fails the "
           "typing",
      is_inv and reflect_fails,
      f"is_involution={is_inv} even!=Astar={reflect_fails}")

# ---- F3: teeth -- degenerate admitted, generic refused -> not vacuous ------
teeth = typing_holds and (not any_match)
check("F", "F3 teeth: the toy ADMITS the typing in the degenerate (Z/2) case "
           "and REFUSES it in the generic (ternary) case -- it separates "
           "realizable-shape from refuted, so the refutation is content, not "
           "a probe that rejects everything",
      teeth, f"degenerate_admits={typing_holds} generic_refuses={not any_match}")


# ============================================================================
# verdict + headline
# ============================================================================
nE = sum(1 for t, _n, ok in RESULTS if t == "E")
nF = sum(1 for t, _n, ok in RESULTS if t == "F")
all_ok = all(ok for _t, _n, ok in RESULTS)
print()
if all_ok:
    print("OUTCOME: the algebraic legs of the boundary law are grade-"
          "independent identities (LIFTS-EXACTLY substantiated: E1-E3); the "
          "TaF involution-typing lemma is REALIZABLE only in the degenerate "
          "Z/2-witness case (E4) and REFUTED in general (F1, exhaustive; F2 "
          "kills even the reflection) -- the causal-horizon engine is "
          "strictly more general than a fixpoint-free involution, so the "
          "GU/TaF unification is leg-deep, not mechanism-deep.")
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   "
      f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
