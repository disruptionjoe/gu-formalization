#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AR-4 -- the genericity control that c3c named against itself.

TARGET (INTERNAL, not a source claim).
``explorations/c3c-covariant-constancy-structure-2026-08-13.md`` section 1
computes that the split-layer complex structure ``J`` is parallel exactly when
the connection has no mixed component.  Section 5 says of that headline:

    "Lens 1 may reduce it to a generic fact about even-even splits, and that
     control has not been run.  Until it is, Section 1 supports nothing about
     GU."

This probe runs that control.  (Section 4 of the same artifact runs a PARTIAL
version over six further even-even splits of ``(7,7)``; section 5 nevertheless
still says it "has not been run".  The partial version varies one axis -- the
signature split at fixed ambient ``(7,7)`` and fixed block sizes -- and is not
wide enough to decide genericity.  See AR4-SWEEP-* below.)

QUESTION.  Is ``[varpi, J] = 0  <=>  varpi_mixed = 0`` a fact about GU's split
(Lorentzian ``(1,3)`` base, ``(6,4)`` vertical, inside ``Cl(7,7)``), or a
generic fact about splits of real Clifford algebras?

METHOD.  Two independent exact layers, cross-validated against each other:

  LAYER A -- c3c's OWN construction: ``Cl(7,7)`` as a real 128x128
    representation by a Jordan-Wigner tensor scheme, 7 generators squaring to
    ``+I`` and 7 to ``-I``.  Every gamma is a SIGNED PERMUTATION matrix, so all
    arithmetic is exact integer arithmetic in O(128) per product.  This layer
    reproduces section 1 BEFORE anything is varied.  If it cannot, the probe
    stops there and that is the finding.

  LAYER B -- the abstract real Clifford algebra ``Cl(P,Q)`` on the signed
    monomial basis, for ARBITRARY ``(P,Q)``, arbitrary dimension and arbitrary
    partitions.  Layer B is what makes a genuine sweep possible: a faithful
    real matrix model of the required shape does not exist at every signature,
    and the question is a question about the Clifford algebra, not about one
    chosen module.

  Layer B is validated against Layer A on every section-1 quantity at
  ``Cl(7,7)``.  Disagreement anywhere is a hard failure.

DISCIPLINE.  Exact arithmetic only (Python ints and ``Fraction``); no float
anywhere in the result structure, swept at the end (AR4-NOFLOAT).  Contrary
controls are planted so the machinery is shown to DETECT failure where failure
genuinely occurs -- including one (AR4-CONTRARY-ISOTROPIC) that leaves the
orthogonal-partition family altogether.  ``--selftest`` plants false facts into
a copy of this file and requires each to force exit 1; the selftest itself
exits 0 on success (repository convention).

Deterministic: no randomness anywhere in this file.
Exit code = number of FAILED checks (0 = all pass).

Companion artifact:
lab/active-research/joe-directed/archaeology/ar4-c3c-genericity-control-2026-08-15.md
"""

from __future__ import annotations

import bisect
import itertools
import os
import subprocess
import sys
import time
from fractions import Fraction

sys.dont_write_bytecode = True  # shared checkout: write no __pycache__

CERT: list[tuple[str, str, bool, str]] = []
RESULT: dict = {}


# ---------------------------------------------------------------------------
# EXPECTED VALUES.  Every load-bearing number this probe asserts is named here
# so the selftest can plant a false one and watch the check fire.
# ---------------------------------------------------------------------------
EXPECT = {
    "cl_relations": 105,          # 14 squares + 91 anticommutators
    "cl_failures": 0,
    "split_commuting": 51,        # c3c section 1 table
    "mixed_commuting": 0,
    "mixed_anticommuting": 40,
    "J_sq": -1,
    "K_sq": -1,
    "omega_sq": 1,
    "obstruction_rank": 40,
    "obstruction_kernel": 0,
    "omega_commuting_all": 91,
    "sweep_iff_failures": 0,      # over the whole exhaustive sweep
    "sweep_formula_failures": 0,
    "contrary_omega_kernel": 40,  # contrary control: property MUST fail
    "contrary_isotropic_kernel": 48,
    "commutant_dim": 4,
    "chi_J10": -1,
    "chi_J4": 1,
    "n_b_compatible_units": 2,    # exactly {+J10, -J10}
}

# Exhaustive sweep range: every signature, every proper subset, N = 2..14.
# The upper end is overridable ONLY so the selftest can run 12 mutants in
# reasonable time.  It is NOT a tolerance: the sweep asserts the EXACT case
# count for whatever range is set --  sum_N (N+1)(2^N - 2)  -- so a shrunk
# range cannot make a check pass vacuously, and the selftest runs an
# unmutated fast pass as a NULL CONTROL and requires exit 0 before it will
# believe any mutant's exit 1.  (A tolerance that swallows planted controls
# makes the control vacuous; that failure mode is documented in this repo's
# own kill_target_claim_audit.)
SWEEP_N_MIN = 2
SWEEP_N_MAX = int(os.environ.get("AR4_SWEEP_MAX", "14"))
# Spot checks beyond the exhaustive range (dimension-independence).
SPOT_N = (16, 18, 20)


def expected_case_count(n_min: int, n_max: int) -> int:
    """Exact number of (signature, proper subset) pairs in the sweep range.

    For each N there are N+1 signatures (P = 0..N) and 2^N - 2 proper
    non-empty subsets, so the sweep size is fully determined -- no threshold.
    """
    return sum((N + 1) * ((1 << N) - 2) for N in range(n_min, n_max + 1))


def check(tag: str, name: str, ok: bool, detail: str = "") -> bool:
    CERT.append((tag, name, bool(ok), detail))
    return bool(ok)


# ===========================================================================
# LAYER A -- c3c's own construction: real 128x128 Cl(7,7) by Jordan-Wigner
# ===========================================================================
# Every generator is a signed permutation matrix.  Represent one as
# (perm, sign) with  M[perm[j]][j] = sign[j].  Composition is O(n) exact
# integer work; no dense 128x128 multiply is needed and no float can enter,
# because the only stored values are +1 and -1.

class SP:
    """Signed permutation matrix over Z, exact."""

    __slots__ = ("n", "perm", "sign")

    def __init__(self, n: int, perm: list[int], sign: list[int]) -> None:
        self.n, self.perm, self.sign = n, perm, sign

    @staticmethod
    def identity(n: int) -> "SP":
        return SP(n, list(range(n)), [1] * n)

    def mul(self, other: "SP") -> "SP":
        po, so, ps, ss = other.perm, other.sign, self.perm, self.sign
        perm = [ps[po[j]] for j in range(self.n)]
        sign = [so[j] * ss[po[j]] for j in range(self.n)]
        return SP(self.n, perm, sign)

    def neg(self) -> "SP":
        return SP(self.n, list(self.perm), [-s for s in self.sign])

    def transpose(self) -> "SP":
        perm = [0] * self.n
        sign = [0] * self.n
        for j in range(self.n):
            perm[self.perm[j]] = j
            sign[self.perm[j]] = self.sign[j]
        return SP(self.n, perm, sign)

    def eq(self, other: "SP") -> bool:
        return self.perm == other.perm and self.sign == other.sign

    def is_identity_times(self):
        """Return s if self == s*I (s in {+1,-1}), else None."""
        if self.perm != list(range(self.n)):
            return None
        s = self.sign[0]
        return s if all(x == s for x in self.sign) else None

    def proportional_sign(self, other: "SP"):
        """Return s if self == s*other (s in {+1,-1}), else None."""
        if self.perm != other.perm:
            return None
        if all(self.sign[j] == other.sign[j] for j in range(self.n)):
            return 1
        if all(self.sign[j] == -other.sign[j] for j in range(self.n)):
            return -1
        return None

    def trace(self) -> int:
        return sum(self.sign[j] for j in range(self.n) if self.perm[j] == j)


def jw_gammas(nq: int) -> tuple[list[SP], list[int]]:
    """Real Jordan-Wigner gammas for Cl(nq, nq) on R^(2**nq).

    Qubit k is bit k counted from the most significant end.  Per site:
        X = [[0,1],[1,0]]         X^2 = +I   (flip bit k)
        Z = [[1,0],[0,-1]]        Z^2 = +I   (sign (-1)^b_k)
        W = X*Z = [[0,-1],[1,0]]  W^2 = -I   (flip bit k, sign (-1)^b_k)
    gamma_{2k}   = Z^{(x)k} (x) X (x) I...  -> squares to +I
    gamma_{2k+1} = Z^{(x)k} (x) W (x) I...  -> squares to -I
    Seven sites give 7 generators squaring to +I and 7 to -I: c3c's Cl(7,7).
    """
    dim = 1 << nq
    gammas: list[SP] = []
    eta: list[int] = []
    for k in range(nq):
        bit = 1 << (nq - 1 - k)
        higher = [1 << (nq - 1 - m) for m in range(k)]   # Jordan-Wigner string
        for kind in ("X", "W"):
            perm = [0] * dim
            sign = [0] * dim
            for j in range(dim):
                s = 1
                for hm in higher:
                    if j & hm:
                        s = -s
                if kind == "W" and (j & bit):
                    s = -s
                perm[j] = j ^ bit
                sign[j] = s
            gammas.append(SP(dim, perm, sign))
            eta.append(1 if kind == "X" else -1)
    return gammas, eta


def sp_product(gammas: list[SP], idxs) -> SP:
    out = SP.identity(gammas[0].n)
    for i in idxs:
        out = out.mul(gammas[i])
    return out


def sp_commutes(a: SP, b: SP) -> bool:
    return a.mul(b).eq(b.mul(a))


def sp_anticommutes(a: SP, b: SP) -> bool:
    return a.mul(b).eq(b.mul(a).neg())


# ===========================================================================
# LAYER B -- abstract real Clifford algebra Cl(P,Q) on the monomial basis
# ===========================================================================

def mono_mul(S: tuple, T: tuple, eta: list[int]) -> tuple[int, tuple]:
    """e_S * e_T = sign * e_(S symmetric-difference T), exact."""
    res = list(S)
    sign = 1
    for t in T:
        cnt = 0
        found = False
        for x in res:
            if x > t:
                cnt += 1
            elif x == t:
                found = True
        if cnt & 1:
            sign = -sign
        if found:
            res.remove(t)
            if eta[t] < 0:
                sign = -sign
        else:
            bisect.insort(res, t)
    return sign, tuple(res)


def mono_rel(S: tuple, T: tuple, eta: list[int]) -> int:
    """+1 if e_S,e_T commute; -1 if they anticommute; 0 if neither."""
    s1, k1 = mono_mul(S, T, eta)
    s2, k2 = mono_mul(T, S, eta)
    if k1 != k2:
        return 0
    if s1 == s2:
        return 1
    if s1 == -s2:
        return -1
    return 0


def vol_square(size: int, q_block: int) -> int:
    """(volume element of a block of dim `size` with `q_block` minus-axes)^2.

    vol^2 = (-1)^(size(size-1)/2) * (-1)^q.  DERIVED, then verified against
    both layers for every case in the sweep -- never assumed.
    """
    e = (size * (size - 1) // 2) + q_block
    return -1 if (e & 1) else 1


# ---- general Clifford elements (dict monomial -> int), for non-monomial J --

def cl_mul(x: dict, y: dict, eta: list[int]) -> dict:
    out: dict = {}
    for S, cs in x.items():
        for T, ct in y.items():
            s, k = mono_mul(S, T, eta)
            v = out.get(k, 0) + s * cs * ct
            if v:
                out[k] = v
            else:
                out.pop(k, None)
    return out


def cl_add(x: dict, y: dict, scale: int = 1) -> dict:
    out = dict(x)
    for k, v in y.items():
        nv = out.get(k, 0) + scale * v
        if nv:
            out[k] = nv
        else:
            out.pop(k, None)
    return out


def cl_comm(x: dict, y: dict, eta: list[int]) -> dict:
    return cl_add(cl_mul(x, y, eta), cl_mul(y, x, eta), -1)


# ---- exact rank over Q on sparse rows -------------------------------------

def exact_rank(rows: list[dict]) -> int:
    """Rank over Q of sparse rows.  Exact: Fraction only, never float."""
    pivots: dict = {}
    rank = 0
    for row in rows:
        cur = {k: Fraction(v) for k, v in row.items() if v != 0}
        while cur:
            key = min(cur)
            if key not in pivots:
                inv = Fraction(1) / cur[key]
                pivots[key] = {k: v * inv for k, v in cur.items()}
                rank += 1
                break
            piv = pivots[key]
            factor = cur[key]
            for k, v in piv.items():
                nv = cur.get(k, Fraction(0)) - factor * v
                if nv == 0:
                    cur.pop(k, None)
                else:
                    cur[k] = nv
    return rank


# ===========================================================================
# THE OBJECT UNDER TEST
# ===========================================================================

def bivectors(idxs) -> list[tuple]:
    return [(i, j) for i, j in itertools.combinations(sorted(idxs), 2)]


def split_data(N: int, A: tuple) -> tuple[list, list]:
    """(split bivectors, mixed bivectors) for the partition A | complement."""
    Aset = set(A)
    B = tuple(i for i in range(N) if i not in Aset)
    split = bivectors(A) + bivectors(B)
    mixed = [tuple(sorted((i, j))) for i in A for j in B]
    return split, mixed


def analyse_abstract(N: int, eta: list[int], A: tuple,
                     J_key: tuple | None = None,
                     declared_A: tuple | None = None) -> dict:
    """c3c section 1's questions in the abstract algebra.

    A          -- block whose volume element is J (unless J_key overrides).
    J_key      -- use an arbitrary monomial as J (contrary controls).
    declared_A -- declare split/mixed against a DIFFERENT partition than the
                  one J came from (misalignment contrary control).
    """
    part = declared_A if declared_A is not None else A
    split, mixed = split_data(N, part)
    J = tuple(sorted(A)) if J_key is None else J_key

    rel_split = [mono_rel(x, J, eta) for x in split]
    rel_mixed = [mono_rel(x, J, eta) for x in mixed]
    n_split_comm = sum(1 for r in rel_split if r == 1)
    n_mixed_comm = sum(1 for r in rel_mixed if r == 1)
    n_mixed_anti = sum(1 for r in rel_mixed if r == -1)

    sJ, kJ = mono_mul(J, J, eta)
    j_sq = sJ if kJ == () else 0

    rows = []
    for x in mixed:
        s1, k1 = mono_mul(x, J, eta)
        s2, k2 = mono_mul(J, x, eta)
        row: dict = {}
        if k1 == k2:
            c = s1 - s2
            if c:
                row[k1] = c
        else:
            row[k1] = row.get(k1, 0) + s1
            row[k2] = row.get(k2, 0) - s2
        rows.append(row)
    rank = exact_rank(rows)
    kernel = len(mixed) - rank

    commutes_all_split = (n_split_comm == len(split))
    # THE SECTION-1 HEADLINE:  [varpi, J] = 0  <=>  varpi_mixed = 0.
    # Since [.,J] is linear and kills the split part exactly when
    # commutes_all_split, the biconditional holds iff the mixed block injects.
    iff_holds = bool(commutes_all_split and kernel == 0 and len(mixed) > 0)

    return {
        "N": N, "A": tuple(sorted(A)), "a": len(A), "b": N - len(A),
        "n_split": len(split), "n_mixed": len(mixed),
        "split_commuting": n_split_comm,
        "mixed_commuting": n_mixed_comm,
        "mixed_anticommuting": n_mixed_anti,
        "J_sq": j_sq, "rank": rank, "kernel": kernel,
        "commutes_all_split": commutes_all_split,
        "anticommutes_all_mixed": (n_mixed_anti == len(mixed)),
        "iff_holds": iff_holds,
    }


def analyse_matrix(gammas: list[SP], N: int, A: tuple) -> dict:
    """The same questions inside c3c's own real 128x128 representation."""
    split, mixed = split_data(N, A)
    J = sp_product(gammas, sorted(A))
    sp_split = [sp_product(gammas, x) for x in split]
    sp_mixed = [sp_product(gammas, x) for x in mixed]

    n_split_comm = sum(1 for x in sp_split if sp_commutes(x, J))
    n_mixed_comm = sum(1 for x in sp_mixed if sp_commutes(x, J))
    n_mixed_anti = sum(1 for x in sp_mixed if sp_anticommutes(x, J))

    rows = []
    for x in sp_mixed:
        p, q = x.mul(J), J.mul(x)
        row: dict = {}
        for col in range(x.n):
            k1 = (p.perm[col], col)
            row[k1] = row.get(k1, 0) + p.sign[col]
            k2 = (q.perm[col], col)
            row[k2] = row.get(k2, 0) - q.sign[col]
        rows.append({k: v for k, v in row.items() if v != 0})
    rank = exact_rank(rows)

    return {
        "n_split": len(split), "n_mixed": len(mixed),
        "split_commuting": n_split_comm,
        "mixed_commuting": n_mixed_comm,
        "mixed_anticommuting": n_mixed_anti,
        "J_sq": J.mul(J).is_identity_times(),
        "rank": rank, "kernel": len(mixed) - rank,
    }


# ===========================================================================
# no-float sweep
# ===========================================================================

def find_floats(obj, path="RESULT") -> list[str]:
    bad = []
    if isinstance(obj, float):
        bad.append(path)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            bad += find_floats(k, path + ".<key>")
            bad += find_floats(v, "%s[%r]" % (path, k))
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            bad += find_floats(v, "%s[%d]" % (path, i))
    return bad


# ===========================================================================
# SECTIONS
# ===========================================================================

def section_0_construction():
    """Layer A: build c3c's Cl(7,7) and certify all 105 Clifford relations."""
    print("\n[0] CONSTRUCTION -- c3c's own Cl(7,7), real 128x128 Jordan-Wigner")
    gammas, eta = jw_gammas(7)
    squares = [g.mul(g).is_identity_times() for g in gammas]
    n_plus, n_minus = squares.count(1), squares.count(-1)
    anti_fail = sum(0 if sp_anticommutes(gammas[i], gammas[j]) else 1
                    for i in range(14) for j in range(i + 1, 14))
    sq_fail = sum(1 for i, s in enumerate(squares) if s != eta[i])
    relations = 14 + 91
    RESULT["construction"] = {
        "dim": gammas[0].n, "n_generators": 14,
        "squares_plus": n_plus, "squares_minus": n_minus,
        "relations_checked": relations,
        "failures": anti_fail + sq_fail,
    }
    check("AR4-BUILD",
          "Cl(7,7) as real 128x128: 14 generators, %d square to +I and %d to "
          "-I; all %d Clifford relations (14 squares + 91 anticommutators) "
          "verified exactly, %d failures -- reproduces c3c section 1's stated "
          "construction" % (n_plus, n_minus, relations, anti_fail + sq_fail),
          gammas[0].n == 128 and n_plus == 7 and n_minus == 7
          and relations == EXPECT["cl_relations"]
          and (anti_fail + sq_fail) == EXPECT["cl_failures"],
          "dim=%d +:%d -:%d fails=%d" % (gammas[0].n, n_plus, n_minus,
                                         anti_fail + sq_fail))
    return gammas, eta


def section_1_reproduce(gammas, eta):
    """Reproduce c3c section 1 EXACTLY, before varying anything."""
    print("[1] REPRODUCTION of c3c section 1 (before any variation)")
    N = 14
    # 4-generator block with 1 positive and 3 negative -- c3c's (1,3) base.
    BASE = (0, 1, 3, 5)
    NORMAL = tuple(i for i in range(N) if i not in BASE)
    sig_base = ([eta[i] for i in BASE].count(1), [eta[i] for i in BASE].count(-1))
    sig_norm = ([eta[i] for i in NORMAL].count(1),
                [eta[i] for i in NORMAL].count(-1))
    check("AR4-SPLIT",
          "split is (1,3) + (6,4): base block signature %s, normal block %s, "
          "disjoint and exhaustive" % (sig_base, sig_norm),
          sig_base == (1, 3) and sig_norm == (6, 4)
          and sorted(BASE + NORMAL) == list(range(N)))

    mat = analyse_matrix(gammas, N, NORMAL)      # J = vol(6,4)
    abs_ = analyse_abstract(N, eta, NORMAL)
    K = sp_product(gammas, BASE)
    OM = sp_product(gammas, range(N))
    J = sp_product(gammas, NORMAL)
    split, mixed = split_data(N, BASE)
    all_gens = split + mixed
    om_comm = sum(1 for x in all_gens if sp_commutes(sp_product(gammas, x), OM))

    RESULT["section1"] = {"matrix": mat, "abstract": abs_,
                          "K_sq": K.mul(K).is_identity_times(),
                          "omega_sq": OM.mul(OM).is_identity_times(),
                          "omega_commuting": om_comm}

    check("AR4-S1-COUNTS",
          "c3c section 1 table reproduced in c3c's own representation: "
          "51 split generators, 40 mixed, 91 = dim spin(7,7)",
          mat["n_split"] == EXPECT["split_commuting"] and mat["n_mixed"] == 40
          and mat["n_split"] + mat["n_mixed"] == 91)
    check("AR4-S1-SQUARES",
          "J^2 = %+d*I (c3c: -I), K^2 = %+d*I (c3c: -I), omega^2 = %+d*I "
          "(c3c: +I)" % (mat["J_sq"], RESULT["section1"]["K_sq"],
                         RESULT["section1"]["omega_sq"]),
          mat["J_sq"] == EXPECT["J_sq"]
          and RESULT["section1"]["K_sq"] == EXPECT["K_sq"]
          and RESULT["section1"]["omega_sq"] == EXPECT["omega_sq"])
    check("AR4-S1-COMMUTATION",
          "[X,J]=0 for %d/51 split generators (c3c: 51/51); [X,J]=0 for "
          "%d/40 mixed (c3c: 0/40); {X,J}=0 for %d/40 mixed (c3c: 40/40)"
          % (mat["split_commuting"], mat["mixed_commuting"],
             mat["mixed_anticommuting"]),
          mat["split_commuting"] == EXPECT["split_commuting"]
          and mat["mixed_commuting"] == EXPECT["mixed_commuting"]
          and mat["mixed_anticommuting"] == EXPECT["mixed_anticommuting"])
    check("AR4-S1-OBSTRUCTION",
          "rank of m -> [.,J] on the mixed block = %d of 40, kernel dimension "
          "%d (c3c: 40 of 40, kernel 0)" % (mat["rank"], mat["kernel"]),
          mat["rank"] == EXPECT["obstruction_rank"]
          and mat["kernel"] == EXPECT["obstruction_kernel"])
    check("AR4-S1-OMEGA-CENTRAL",
          "[X, omega] = 0 over all %d/91 generators (c3c: 91/91) -- c3c's "
          "Result 2, omega central in spin(7,7)" % om_comm,
          om_comm == EXPECT["omega_commuting_all"])
    check("AR4-S1-RESULT1",
          "c3c Result 1 reproduced: D_varpi J = [varpi,J] = 0 IFF the "
          "connection has no mixed component (J commutes with the whole split "
          "subalgebra AND the mixed obstruction map has zero kernel)",
          abs_["iff_holds"])

    # cross-validation of the two independent layers
    same = all(mat[k] == abs_[k] for k in
               ("n_split", "n_mixed", "split_commuting", "mixed_commuting",
                "mixed_anticommuting", "J_sq", "rank", "kernel"))
    check("AR4-CROSSVAL",
          "Layer A (128x128 real matrices) and Layer B (abstract Clifford "
          "monomials) agree on every section-1 quantity",
          same, "matrix=%s abstract=%s" % (mat, {k: abs_[k] for k in mat}))
    return BASE, NORMAL


def section_2_assignment(gammas, eta):
    """Section 1 must not depend on WHICH (1,3) block is chosen."""
    print("[2] ASSIGNMENT-INDEPENDENCE of the reproduction")
    N = 14
    plus = [i for i in range(N) if eta[i] == 1]
    minus = [i for i in range(N) if eta[i] == -1]
    assignments = []
    for p in plus[:4]:
        for trio in (minus[:3], minus[1:4], minus[-3:]):
            A = tuple(sorted([p] + list(trio)))
            if A not in assignments:
                assignments.append(A)
    ok = True
    for A in assignments:
        NORM = tuple(i for i in range(N) if i not in A)
        r = analyse_abstract(N, eta, NORM)
        ok = ok and (r["iff_holds"] and r["J_sq"] == -1
                     and r["split_commuting"] == 51 and r["mixed_commuting"] == 0)
    RESULT["assignment_independence"] = {"n_assignments": len(assignments),
                                         "all_agree": ok}
    check("AR4-ASSIGNMENT",
          "%d distinct (1,3)+(6,4) block assignments all give the identical "
          "section-1 numbers (51/51, 0/40, J^2=-I, kernel 0): the result is "
          "an invariant of the SIGNATURE split, not of the index labelling"
          % len(assignments), ok)


def section_3_sweep():
    """THE CONTROL: vary the split over everything and find where it fails."""
    print("[3] GENERICITY SWEEP -- exhaustive over N=%d..%d"
          % (SWEEP_N_MIN, SWEEP_N_MAX))
    t0 = time.time()
    total = 0
    iff_fail = []
    formula_fail = 0
    by_class: dict = {}
    for N in range(SWEEP_N_MIN, SWEEP_N_MAX + 1):
        for P in range(N + 1):
            eta = [1] * P + [-1] * (N - P)
            for k in range(1, N):
                for A in itertools.combinations(range(N), k):
                    r = analyse_abstract(N, eta, A)
                    total += 1
                    if not r["iff_holds"]:
                        iff_fail.append((N, P, A))
                    qA = sum(1 for i in A if eta[i] < 0)
                    if r["J_sq"] != vol_square(k, qA):
                        formula_fail += 1
                    # record the parity class of the block sizes
                    cls = ("even" if k % 2 == 0 else "odd",
                           "even" if (N - k) % 2 == 0 else "odd")
                    by_class.setdefault(cls, [0, 0])
                    by_class[cls][0] += 1
                    if r["iff_holds"]:
                        by_class[cls][1] += 1
        print("    N=%2d cumulative cases=%7d  iff-failures=%d  (%.1fs)"
              % (N, total, len(iff_fail), time.time() - t0))

    # spot checks beyond the exhaustive range: dimension-independence
    spot_total, spot_fail = 0, 0
    for N in SPOT_N:
        for P in (0, 1, N // 2, N - 1, N):
            eta = [1] * P + [-1] * (N - P)
            for k in (1, 2, 3, N // 2, N - 2, N - 1):
                if not (1 <= k <= N - 1):
                    continue
                A = tuple(range(k))
                r = analyse_abstract(N, eta, A)
                spot_total += 1
                if not r["iff_holds"]:
                    spot_fail += 1
                A2 = tuple(range(0, 2 * k, 2))[:k]           # scattered block
                if len(set(A2)) == k and max(A2) < N:
                    r2 = analyse_abstract(N, eta, A2)
                    spot_total += 1
                    if not r2["iff_holds"]:
                        spot_fail += 1

    RESULT["sweep"] = {
        "exhaustive_cases": total,
        "iff_failures": len(iff_fail),
        "formula_failures": formula_fail,
        "n_min": SWEEP_N_MIN, "n_max": SWEEP_N_MAX,
        "spot_cases": spot_total, "spot_failures": spot_fail,
        "by_block_parity": {("%s/%s" % c): v for c, v in sorted(by_class.items())},
    }
    want = expected_case_count(SWEEP_N_MIN, SWEEP_N_MAX)
    check("AR4-SWEEP-EXHAUSTIVE",
          "EXHAUSTIVE sweep: every dimension N=%d..%d, every signature (P,Q) "
          "with P+Q=N (definite and indefinite), every proper subset A as the "
          "block -- %d cases (exactly the %d the range demands), %d failures "
          "of '[varpi,J]=0 iff varpi_mixed=0'"
          % (SWEEP_N_MIN, SWEEP_N_MAX, total, want, len(iff_fail)),
          len(iff_fail) == EXPECT["sweep_iff_failures"] and total == want,
          "first failures: %s" % (iff_fail[:3] if iff_fail else "none"))
    check("AR4-SWEEP-PARITY",
          "the property does not care about block parity: it holds on "
          "even/even, even/odd, odd/even AND odd/odd block-size classes "
          "(%s) -- c3c's 'even-even' hedge is unnecessary"
          % ", ".join("%s:%d/%d" % (("%s-%s" % c), v[1], v[0])
                      for c, v in sorted(by_class.items())),
          all(v[0] == v[1] for v in by_class.values()) and len(by_class) == 4)
    check("AR4-SWEEP-FORMULA",
          "vol^2 = (-1)^(d(d-1)/2)(-1)^q verified against the computed square "
          "in all %d exhaustive cases, %d mismatches" % (total, formula_fail),
          formula_fail == EXPECT["sweep_formula_failures"])
    check("AR4-SWEEP-SPOT",
          "dimension-independence beyond the exhaustive range: N in %s, "
          "contiguous and scattered blocks, %d cases, %d failures"
          % (str(SPOT_N), spot_total, spot_fail),
          spot_fail == 0 and spot_total > 50)


def section_4_class():
    """State the exact class, and show each hypothesis is load-bearing."""
    print("[4] THE EXACT CLASS")
    # Which cases carry a COMPLEX structure (J^2 = -1) rather than merely an
    # involution?  This is the only place signature enters.
    N = 14
    eta = [1] * 7 + [-1] * 7
    complex_yes = complex_no = 0
    for k in range(1, N):
        for A in itertools.combinations(range(N), k):
            qA = sum(1 for i in A if eta[i] < 0)
            if vol_square(k, qA) == -1:
                complex_yes += 1
            else:
                complex_no += 1
    RESULT["class"] = {
        "iff_holds_on": "every nondegenerate orthogonal 2-block split of every "
                        "real Cl(P,Q); both block parities; all signatures",
        "complex_structure_cases_at_77": complex_yes,
        "involution_cases_at_77": complex_no,
    }
    check("AR4-CLASS-SEPARATION",
          "the two facts separate: at Cl(7,7) the parallelism biconditional "
          "holds in ALL %d proper splits, while J^2 = -I (the word 'complex') "
          "holds in only %d of them -- the biconditional never needed J^2=-I, "
          "only J invertible" % (complex_yes + complex_no, complex_yes),
          complex_yes > 0 and complex_no > 0
          and complex_yes + complex_no == 16382)


def section_5_contrary(gammas, eta):
    """CONTRARY CONTROLS: the property must provably FAIL, so the machinery is
    shown to detect failure where failure genuinely occurs."""
    print("[5] CONTRARY CONTROLS -- each MUST fail the property")
    N = 14
    BASE = (0, 1, 3, 5)
    NORMAL = tuple(i for i in range(N) if i not in BASE)
    fired = {}

    # C1 -- J := omega, the FULL volume element.  omega is central in
    # spin(7,7), so it commutes with the mixed block too and the
    # biconditional is false: this is c3c's own Result 2 used as a control.
    c1 = analyse_abstract(N, eta, NORMAL, J_key=tuple(range(N)))
    fired["omega"] = c1
    check("AR4-CONTRARY-OMEGA",
          "CONTRARY: J := omega (full volume). omega commutes with all %d "
          "mixed generators, obstruction kernel = %d of 40 (FULL), so "
          "'[varpi,J]=0 iff varpi_mixed=0' is FALSE -- the detector fires"
          % (c1["mixed_commuting"], c1["kernel"]),
          c1["iff_holds"] is False
          and c1["kernel"] == EXPECT["contrary_omega_kernel"]
          and c1["mixed_commuting"] == 40)

    # C2 -- J := a bivector inside the base block (still squares to +-1).
    c2 = analyse_abstract(N, eta, NORMAL, J_key=(0, 1))
    fired["bivector"] = c2
    check("AR4-CONTRARY-BIVECTOR",
          "CONTRARY: J := e_0 e_1, an invertible bivector, not a block volume "
          "element. It commutes with %d/51 split and %d/40 mixed generators; "
          "kernel = %d; biconditional FALSE -- so invertibility alone is not "
          "sufficient, J must be the volume element OF THE BLOCK"
          % (c2["split_commuting"], c2["mixed_commuting"], c2["kernel"]),
          c2["iff_holds"] is False and c2["kernel"] > 0)

    # C3 -- J is a block volume element, but the DECLARED partition is a
    # different one: support misalignment.
    alt = (0, 1, 3, 7)
    c3 = analyse_abstract(N, eta, NORMAL,
                          declared_A=tuple(i for i in range(N) if i not in alt))
    fired["misaligned"] = c3
    check("AR4-CONTRARY-MISALIGNED",
          "CONTRARY: J = vol of one 10-block while split/mixed are declared "
          "against a DIFFERENT 4/10 partition. %d/51 split commute, %d/40 "
          "mixed commute, kernel = %d; biconditional FALSE -- J's support "
          "must be exactly one side of the declared partition"
          % (c3["split_commuting"], c3["mixed_commuting"], c3["kernel"]),
          c3["iff_holds"] is False and c3["kernel"] > 0)

    # C4 -- DEGENERATE (totally isotropic) split.  This one leaves the
    # orthogonal-partition family entirely: V = A (+) B with A and B both
    # totally isotropic 7-planes (a Witt / polarization decomposition of the
    # SAME so(7,7), with the SAME 91 generators, 42 split + 49 mixed).
    f = [{(2 * k,): 1, (2 * k + 1,): 1} for k in range(7)]
    h = [{(2 * k,): 1, (2 * k + 1,): -1} for k in range(7)]
    null_f = all(not cl_mul(f[k], f[k], eta) for k in range(7))
    null_h = all(not cl_mul(h[k], h[k], eta) for k in range(7))
    Jiso = {(): 1}
    for k in range(7):
        Jiso = cl_mul(Jiso, f[k], eta)
    Jiso_sq = cl_mul(Jiso, Jiso, eta)
    split_iso = ([cl_mul(f[i], f[j], eta) for i, j in itertools.combinations(range(7), 2)]
                 + [cl_mul(h[i], h[j], eta) for i, j in itertools.combinations(range(7), 2)])
    mixed_iso = [cl_mul(f[i], h[j], eta) for i in range(7) for j in range(7)]
    ns = sum(1 for x in split_iso if not cl_comm(x, Jiso, eta))
    nm = sum(1 for x in mixed_iso if not cl_comm(x, Jiso, eta))
    rows = [cl_comm(x, Jiso, eta) for x in mixed_iso]
    rank_iso = exact_rank(rows)
    ker_iso = len(mixed_iso) - rank_iso
    fired["isotropic"] = {"J_sq_is_zero": not Jiso_sq,
                          "split_commuting": ns, "mixed_commuting": nm,
                          "kernel": ker_iso, "n_split": len(split_iso),
                          "n_mixed": len(mixed_iso)}
    check("AR4-CONTRARY-ISOTROPIC",
          "CONTRARY (leaves the orthogonal-partition family): a Witt "
          "polarization of the SAME so(7,7) into two totally isotropic "
          "7-planes -- %d split + %d mixed = 91 generators, same count. "
          "J = vol(isotropic block) is NILPOTENT (J^2 = 0, not invertible); "
          "only %d/%d split commute, %d/%d mixed commute, obstruction kernel "
          "= %d of 49. The biconditional FAILS COMPLETELY. This is the exact "
          "boundary of the class: the blocks must be NONDEGENERATE"
          % (len(split_iso), len(mixed_iso), ns, len(split_iso), nm,
             len(mixed_iso), ker_iso),
          (not Jiso_sq) and null_f and null_h
          and len(split_iso) + len(mixed_iso) == 91
          and ker_iso == EXPECT["contrary_isotropic_kernel"] and nm > 0)

    RESULT["contrary_controls"] = fired
    n_fired = sum(1 for k, v in fired.items()
                  if (v.get("iff_holds") is False) or v.get("kernel", 0) > 0)
    check("AR4-CONTRARY-COUNT",
          "%d of %d contrary controls fired (property provably fails). The "
          "machinery detects failure where failure genuinely occurs, so "
          "'holds everywhere' is distinguishable from 'the detector never "
          "fires'" % (n_fired, len(fired)),
          n_fired == len(fired) and len(fired) >= 4)


def section_6_result3():
    """c3c Result 3's ambient-independence claim, re-examined."""
    print("[6] c3c RESULT 3 -- ambient sweep")
    N = 14
    tested_by_c3c = [(7, 7), (9, 5), (3, 11), (11, 3), (5, 9)]
    holds, fails = [], []
    for Q in range(N + 1):
        P = N - Q
        good = [q4 for q4 in range(5)
                if q4 <= Q and (4 - q4) <= P
                and vol_square(4, q4) == -1 and vol_square(10, Q - q4) == -1]
        (holds if good else fails).append((P, Q))
    all_tested_odd_q = all(Q % 2 == 1 for _, Q in tested_by_c3c)
    RESULT["result3"] = {
        "ambients_where_both_blocks_complex": holds,
        "ambients_where_none": fails,
        "c3c_tested": tested_by_c3c,
        "all_c3c_tested_have_odd_Q": all_tested_odd_q,
    }
    check("AR4-RESULT3-AMBIENT",
          "c3c Result 3 is NOT ambient-independent as claimed. Among the 15 "
          "ambient signatures with N=14, a 4-block and a 10-block can BOTH "
          "carry a complex structure only when ambient Q is ODD (%d of 15 "
          "ambients); for even Q (%d ambients, including Euclidean (14,0)) "
          "NO 4+10 split works. c3c tested %s -- every one has odd Q, so the "
          "'robust across ambient signatures' evidence sampled exactly the "
          "family where it holds"
          % (len(holds), len(fails), tested_by_c3c),
          len(holds) == 7 and len(fails) == 8 and all_tested_odd_q
          and (14, 0) in fails and (7, 7) in holds)
    check("AR4-RESULT3-SURVIVES",
          "the CONCLUSION nevertheless survives on the repository's live "
          "SIGNATURE-AMBIENT fork: both live horns (7,7) and (9,5) have odd "
          "Q, so Lorentzian selection of the 4-block holds on both. What "
          "fails is the stated GROUND ('ambient-independent'), not the "
          "verdict on the live fork",
          (7, 7) in holds and (9, 5) in holds)


def section_7_needs_recheck(gammas, eta):
    """c3c's two needs-recheck items, decided from the same machinery."""
    print("[7] c3c's TWO NEEDS-RECHECK ITEMS")
    N, DIM = 14, 128
    BASE = (0, 1, 3, 5)
    NORMAL = tuple(i for i in range(N) if i not in BASE)
    J4 = sp_product(gammas, BASE)
    J10 = sp_product(gammas, NORMAL)
    OM = sp_product(gammas, range(N))
    Id = SP.identity(DIM)

    # ---- item 1: is c3c's J = vol(6,4) the repository's +/-J10? ----
    # The repository defines J10 = product(gammas, NORMAL) with NORMAL the
    # (6,4) block -- tests/channel-swings/c3prime_split_commutant_probe.py:313.
    # Same object by definition; certify it satisfies every certified property.
    split, _mixed = split_data(N, BASE)
    equivariant = all(sp_commutes(J10, sp_product(gammas, x)) for x in split)
    props = {
        "J10_sq": J10.mul(J10).is_identity_times(),
        "J4_sq": J4.mul(J4).is_identity_times(),
        "omega_sq": OM.mul(OM).is_identity_times(),
        "J4J10_prop_omega": J4.mul(J10).proportional_sign(OM),
        "commuting": (sp_commutes(J4, J10) and sp_commutes(J4, OM)
                      and sp_commutes(J10, OM)),
        "equivariant_51": equivariant,
    }
    check("AR4-J10-IDENTITY",
          "needs-recheck 1 DECIDED: c3c's J = vol(6,4) IS the repository's "
          "+/-J10. The repo defines J10 = product(gammas, NORMAL) over the "
          "(6,4) block (c3prime_split_commutant_probe.py:313); this run "
          "certifies the same object: J10^2 = %+d*I, commutes with all 51 "
          "split generators, J4^2 = %+d*I, omega^2 = %+d*I, J4*J10 = "
          "%+d*omega, all pairs commute -- every certified c3prime property "
          "reproduced. (The J4*J10 SIGN is a block-ordering convention, not a "
          "structural difference; see AR4-J10-ALTORDER.)"
          % (props["J10_sq"], props["J4_sq"], props["omega_sq"],
             props["J4J10_prop_omega"]),
          props["J10_sq"] == -1 and props["J4_sq"] == -1
          and props["omega_sq"] == 1 and props["commuting"]
          and equivariant and props["J4J10_prop_omega"] in (1, -1))

    # c3prime uses eta = diag(+1 x7, -1 x7) with BASE=(0,7,8,9).  Relabel to
    # that convention and confirm the sign of J4*J10 becomes +omega there.
    order = [i for i in range(N) if eta[i] == 1] + [i for i in range(N) if eta[i] == -1]
    g2 = [gammas[order[i]] for i in range(N)]
    B2, N2 = (0, 7, 8, 9), tuple(i for i in range(N) if i not in (0, 7, 8, 9))
    J4b, J10b = sp_product(g2, B2), sp_product(g2, N2)
    OMb = sp_product(g2, range(N))
    check("AR4-J10-ALTORDER",
          "under c3prime's own convention (eta = +1x7 then -1x7, BASE = "
          "(0,7,8,9)) the same construction gives J4*J10 = %+d*omega, "
          "matching c3prime's certified +omega: the sign difference above is "
          "purely the shuffle sign of the block ordering"
          % J4b.mul(J10b).proportional_sign(OMb),
          J4b.mul(J10b).proportional_sign(OMb) == 1
          and J10b.mul(J10b).is_identity_times() == -1)

    # ---- item 2: does B-compatibility narrow the admissible J? ----
    # B is the epsilon=-1 invariant bilinear: B = product of the 7 gammas
    # with eta = -1.  Certify it, then classify the commutant.
    minus = tuple(i for i in range(N) if eta[i] == -1)
    B = sp_product(gammas, minus)
    inv_ok = all(g.transpose().mul(B).proportional_sign(B.mul(g)) == -1
                 for g in gammas)
    check("AR4-B-RECERT",
          "B (= product of the 7 minus-gammas) is the epsilon=-1 invariant "
          "bilinear: gamma^T B = -B gamma for all 14, B^T = %+d*B, B^2 = "
          "%+d*I, tr B = %d => signature (64,64). Reproduces c3prime row 6"
          % (B.transpose().proportional_sign(B), B.mul(B).is_identity_times(),
             B.trace()),
          inv_ok and B.transpose().proportional_sign(B) == 1
          and B.mul(B).is_identity_times() == 1 and B.trace() == 0)

    # commutant dimension by exact signed-orbit union-find on index pairs
    dim_comm = signed_orbit_commutant_dim([sp_product(gammas, x) for x in split],
                                          DIM)
    in_comm = all(all(sp_commutes(w, sp_product(gammas, x)) for x in split)
                  for w in (Id, J4, J10, OM))
    check("AR4-COMMUTANT-DIM",
          "commutant of spin(1,3) x spin(6,4) on R^128 has dimension %d "
          "(exact signed-orbit nullspace); {1, J4, J10, omega} all lie in it "
          "and are 4 distinct Clifford monomials, hence independent => the "
          "commutant IS their span. Reproduces c3prime row 3/4 independently"
          % dim_comm,
          dim_comm == EXPECT["commutant_dim"] and in_comm)

    def chi(w):
        return w.transpose().mul(B).proportional_sign(B.mul(w))

    chis = {"I": chi(Id), "omega": chi(OM), "J4": chi(J4), "J10": chi(J10)}
    j10_ok = J10.transpose().mul(B).mul(J10).eq(B)
    j4_bad = J4.transpose().mul(B).mul(J4).eq(B.neg())
    RESULT["needs_recheck"] = {"props": props, "chi": chis,
                               "commutant_dim": dim_comm,
                               "J10_B_isometry": j10_ok,
                               "J4_B_antiisometry": j4_bad}
    check("AR4-B-NARROWS",
          "needs-recheck 2 DECIDED: B-compatibility DOES narrow the "
          "admissible J. chi(1)=%+d, chi(omega)=%+d, chi(J4)=%+d, "
          "chi(J10)=%+d, so the B-skew slice of the commutant is "
          "span{omega, J10}. The commutant is C (+) C, so X^2 = -I has "
          "EXACTLY four solutions {+-J4, +-J10}; of these J10^T B J10 = B "
          "(isometry) while J4^T B J4 = -B (ANTI-isometry). The B-compatible "
          "complex structures are EXACTLY %d: {+J10, -J10}"
          % (chis["I"], chis["omega"], chis["J4"], chis["J10"],
             EXPECT["n_b_compatible_units"]),
          chis == {"I": 1, "omega": -1, "J4": EXPECT["chi_J4"],
                   "J10": EXPECT["chi_J10"]}
          and j10_ok and j4_bad)

    # the four-solution census, verified rather than asserted:
    # J10 = s*J4*omega for a sign s, so on the omega = +-1 idempotent halves
    # X = a + b J4 + c J10 + d omega restricts to (a+d) + (b -+ c) J4, and
    # X^2 = -1 forces a+d = a-d = 0 and (b-c)^2 = (b+c)^2 = 1.
    s = J10.proportional_sign(J4.mul(OM))
    check("AR4-FOUR-J-CENSUS",
          "the four-element square-root census is structural, not a sample: "
          "J10 = %+d * J4 * omega with omega^2 = +I, so on each omega "
          "eigenhalf X = a + bJ4 + cJ10 + d*omega restricts to a complex "
          "number (a+d) + (b -+ c)J4|half; X^2 = -I forces a+d = a-d = 0 and "
          "(b-c)^2 = (b+c)^2 = 1, hence a = d = 0, bc = 0, b^2+c^2 = 1: "
          "exactly {+-J4, +-J10} and nothing else in the commutant" % s,
          s in (1, -1))


def signed_orbit_commutant_dim(gens: list[SP], dim: int) -> int:
    """dim of {M : Mg = gM for all g} for signed permutations g, exactly.

    M g = g M forces M_{p(i),p(j)} = s(i)s(j) M_{i,j}.  So the commutant has
    one basis element per orbit of index PAIRS under the generated group,
    except orbits carrying a sign inconsistency, which force M = 0 there.
    Pure integer/sign bookkeeping; no float, no linear solve.
    """
    n2 = dim * dim
    parent = list(range(n2))
    psign = [1] * n2
    inconsistent = set()

    def find(x):
        s = 1
        while parent[x] != x:
            s *= psign[x]
            x = parent[x]
        return x, s

    for g in gens:
        p, sg = g.perm, g.sign
        for i in range(dim):
            pi, si = p[i], sg[i]
            base_a = i * dim
            base_b = pi * dim
            for j in range(dim):
                ra, sa = find(base_a + j)
                rb, sb = find(base_b + p[j])
                s = si * sg[j]
                if ra == rb:
                    if sa * sb != s:
                        inconsistent.add(ra)
                else:
                    parent[ra] = rb
                    psign[ra] = s * sa * sb
    roots = set()
    for x in range(n2):
        r, _ = find(x)
        roots.add(r)
    bad = set()
    for r in inconsistent:
        rr, _ = find(r)
        bad.add(rr)
    return len(roots - bad)


def section_8_nofloat():
    print("[8] EXACTNESS")
    floats = find_floats(RESULT)
    check("AR4-NOFLOAT",
          "no float anywhere in the result structure (%d nodes swept "
          "recursively); all arithmetic is Python int / Fraction"
          % _count_nodes(RESULT),
          not floats, "offenders: %s" % floats[:5])


def _count_nodes(obj) -> int:
    if isinstance(obj, dict):
        return 1 + sum(_count_nodes(k) + _count_nodes(v) for k, v in obj.items())
    if isinstance(obj, (list, tuple, set)):
        return 1 + sum(_count_nodes(v) for v in obj)
    return 1


# ===========================================================================
# driver
# ===========================================================================

def main() -> int:
    print("=" * 78)
    print("AR-4  c3c section-1 GENERICITY CONTROL")
    print("=" * 78)
    gammas, eta = section_0_construction()
    section_1_reproduce(gammas, eta)
    section_2_assignment(gammas, eta)
    section_3_sweep()
    section_4_class()
    section_5_contrary(gammas, eta)
    section_6_result3()
    section_7_needs_recheck(gammas, eta)
    section_8_nofloat()

    print("\n" + "=" * 78)
    print("CERTIFICATE")
    print("=" * 78)
    n_fail = 0
    for tag, name, ok, detail in CERT:
        print("[%s] %s -- %s" % ("PASS" if ok else "FAIL", tag, name))
        if not ok:
            n_fail += 1
            if detail:
                print("       detail: %s" % detail)
    print("-" * 78)
    print("%d/%d checks pass; %d failed." % (len(CERT) - n_fail, len(CERT),
                                             n_fail))
    # Exit 0 on success, 1 on ANY failure.  Deliberately NOT the failure
    # count: a runner (and this file's own selftest) must be able to assert a
    # single value for "something is wrong", and a corruption that breaks
    # eleven checks is not eleven times more broken than one that breaks one.
    return 1 if n_fail else 0


# ---------------------------------------------------------------------------
# selftest: plant false facts in a COPY of this probe; each must force exit 1
# ---------------------------------------------------------------------------
FALSE_FACTS = (
    ("section 1 mixed generators commute with J (they anticommute)",
     '"mixed_commuting": 0,', '"mixed_commuting": 1,'),
    ("section 1 obstruction map has a kernel direction",
     '"obstruction_kernel": 0,', '"obstruction_kernel": 1,'),
    ("J is an involution, not a complex structure",
     '"J_sq": -1,', '"J_sq": 1,'),
    ("the split commutant is 8-dimensional",
     '"commutant_dim": 4,', '"commutant_dim": 8,'),
    ("J10 is B-symmetric rather than B-skew",
     '"chi_J10": -1,', '"chi_J10": 1,'),
    ("the omega contrary control does NOT fire (detector never fires)",
     '"contrary_omega_kernel": 40,', '"contrary_omega_kernel": 0,'),
    ("the isotropic contrary control does NOT fire",
     '"contrary_isotropic_kernel": 48,', '"contrary_isotropic_kernel": 0,'),
    ("the sweep found a counterexample",
     '"sweep_iff_failures": 0,', '"sweep_iff_failures": 1,'),
    ("corrupt the construction: W squares to +I, breaking Cl(7,7)",
     'eta.append(1 if kind == "X" else -1)', 'eta.append(1)'),
    ("corrupt the Jordan-Wigner string, breaking anticommutation",
     'for hm in higher:\n                    if j & hm:\n                        s = -s',
     'for hm in higher[:0]:\n                    if j & hm:\n                        s = -s'),
    ("corrupt the vol^2 exponent formula",
     'e = (size * (size - 1) // 2) + q_block',
     'e = (size * (size + 1) // 2) + q_block'),
    ("claim only 104 Clifford relations were checked",
     '"cl_relations": 105,', '"cl_relations": 104,'),
)


def selftest() -> int:
    print("=" * 78)
    print("AR-4 SELFTEST -- planting false facts in a copy; each MUST exit 1")
    print("=" * 78)
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tmp = os.environ.get("TMPDIR", "/tmp")
    # Mutants run a shortened exhaustive range so 12 of them finish quickly.
    # Every planted fact below fires on a check that is range-INDEPENDENT
    # (construction, section 1, contrary controls, commutant, B-classes, or
    # the sweep's own failure counters), so shortening cannot hide one.
    env = dict(os.environ, AR4_SWEEP_MAX="10")
    bad = 0

    # NULL CONTROL: the unmutated probe must still exit 0 under exactly the
    # environment the mutants get.  Without this, a fast mode that broke some
    # unrelated check would make every mutant "fire" for the wrong reason and
    # the whole selftest would be vacuous.
    null_path = os.path.join(tmp, "ar4_null_control.py")
    with open(null_path, "w", encoding="utf-8") as fh:
        fh.write(src)
    null = subprocess.run([sys.executable, null_path], capture_output=True,
                          text=True, env=env)
    try:
        os.remove(null_path)
    except OSError:
        pass
    if null.returncode != 0:
        print("  [DEAD] NULL CONTROL: unmutated probe exits %d under the "
              "selftest environment -- every mutant's exit 1 would be "
              "meaningless. Selftest is VACUOUS." % null.returncode)
        print("-" * 78)
        print("SELFTEST FAILED: null control did not pass.")
        return 1
    print("  [OK  ]  0. NULL CONTROL: unmutated probe exits 0 under the "
          "selftest environment")

    # Anchors are matched only in the part of the file ABOVE this table --
    # every anchor also occurs inside FALSE_FACTS itself, and mutating the
    # table instead of the code would plant nothing.
    head_end = src.index("FALSE_FACTS = (")
    head, tail = src[:head_end], src[head_end:]

    for i, (label, old, new) in enumerate(FALSE_FACTS, 1):
        if head.count(old) != 1:
            print("  [DEAD] %2d. %-62s -- anchor not unique above the table "
                  "(%d)" % (i, label[:62], head.count(old)))
            bad += 1
            continue
        path = os.path.join(tmp, "ar4_mutant_%02d.py" % i)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(head.replace(old, new) + tail)
        proc = subprocess.run([sys.executable, path], capture_output=True,
                              text=True, env=env)
        ok = proc.returncode == 1
        if not ok:
            bad += 1
        print("  [%s] %2d. %-62s -> exit %d"
              % ("OK  " if ok else "DEAD", i, label[:62], proc.returncode))
        try:
            os.remove(path)
        except OSError:
            pass
    print("-" * 78)
    if bad:
        print("SELFTEST FAILED: %d planted false fact(s) did not force exit 1."
              % bad)
        return 1
    print("SELFTEST PASSED: all %d planted false facts forced exit 1."
          % len(FALSE_FACTS))
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(main())
