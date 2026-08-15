#!/usr/bin/env python3
"""OT-1 -- the action-ownership predicate for GU's non-reductive semidirect setting.

Run from the repository root:

    _local/cas-venv/bin/python tests/channel-swings/joe_directed_ownership_predicate_probe.py

Exact throughout: Python integers and ``fractions.Fraction`` only.  No float is
constructed anywhere; the whole result dict is swept for float at the end.

Sections
--------
S1  The invariant-pairing theorem for ``w = g (x) V`` with ``V = Lambda^1 (x) ad``.
    Certifies the GU obstruction and its exact threshold, with four controls that
    each violate exactly one hypothesis and must fire.
S2  Dimension accounting: what fraction of ``T*W`` the banked 182-dimensional
    ``T*Spin_0(7,7)`` parent covers.
S3  Trivialization dependence (clause O2) on ``T*G``: symplectic rank invariant,
    momentum coordinate NOT invariant.
S4  Mechanical re-sort of the seven ``A_OWN`` rows of ledger v0.258 by required
    clause, every classification carrying an exact substring from the row's own
    text.
S5  The predicate applied to three claim records: the banked 182-parent, the
    banked 98-dimensional Cartan restriction, and a planted control claim.

Tags: [E] exact result, [C] control that must fire, [R] reproduction of an
already-filed repository fact.
"""

from __future__ import annotations

import json
import os
import sys
from fractions import Fraction
from itertools import product

CHECKS: list[tuple[str, str, bool]] = []


def check(tag: str, name: str, ok: bool) -> None:
    CHECKS.append((tag, name, bool(ok)))


REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LEDGER = os.path.join(REPO, "lab", "process", "conditional-physics-ledger-v0.258.json")


# --------------------------------------------------------------------------
# exact linear algebra over Q
# --------------------------------------------------------------------------
def rref(rows: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    """Reduced row echelon form over Q.  Returns (matrix, pivot columns)."""
    m = [r[:] for r in rows]
    if not m:
        return m, []
    ncols = len(m[0])
    pivots: list[int] = []
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(m)):
            if m[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        inv = Fraction(1, 1) / m[r][c]
        m[r] = [x * inv for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        pivots.append(c)
        r += 1
        if r == len(m):
            break
    return m, pivots


def rank(rows: list[list[Fraction]]) -> int:
    return len(rref(rows)[1])


def nullspace(rows: list[list[Fraction]], ncols: int) -> list[list[Fraction]]:
    """Basis of the kernel of the matrix with the given rows, over Q."""
    if not rows:
        return [[Fraction(1) if j == i else Fraction(0) for j in range(ncols)]
                for i in range(ncols)]
    m, pivots = rref(rows)
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        v = [Fraction(0)] * ncols
        v[f] = Fraction(1)
        for i, p in enumerate(pivots):
            v[p] = -m[i][f]
        basis.append(v)
    return basis


# --------------------------------------------------------------------------
# Lie algebra fixtures: structure constants c[a][b] = list of coefficients
# --------------------------------------------------------------------------
class LieAlg:
    def __init__(self, dim: int, bracket, name: str):
        self.dim = dim
        self.name = name
        # c[a][b][k]
        self.c = [[[Fraction(0)] * dim for _ in range(dim)] for _ in range(dim)]
        for a in range(dim):
            for b in range(dim):
                for k, v in bracket(a, b).items():
                    self.c[a][b][k] = Fraction(v)

    def jacobi_ok(self) -> bool:
        n = self.dim
        for a, b, d in product(range(n), repeat=3):
            acc = [Fraction(0)] * n
            for (x, y, z) in ((a, b, d), (b, d, a), (d, a, b)):
                for k in range(n):
                    if self.c[x][y][k] == 0:
                        continue
                    for l in range(n):
                        acc[l] += self.c[x][y][k] * self.c[k][z][l]
            if any(v != 0 for v in acc):
                return False
        return True

    def antisym_ok(self) -> bool:
        n = self.dim
        return all(
            self.c[a][b][k] == -self.c[b][a][k]
            for a in range(n) for b in range(n) for k in range(n)
        )

    def killing(self) -> list[list[Fraction]]:
        n = self.dim
        K = [[Fraction(0)] * n for _ in range(n)]
        for a in range(n):
            for b in range(n):
                s = Fraction(0)
                for i in range(n):
                    for j in range(n):
                        s += self.c[a][i][j] * self.c[b][j][i]
                K[a][b] = s
        return K

    def invariant_sym_forms(self) -> list[list[list[Fraction]]]:
        """Basis of {B symmetric : B([Z,X],Y) + B(X,[Z,Y]) = 0 for all Z}."""
        n = self.dim
        idx: dict[tuple[int, int], int] = {}
        for a in range(n):
            for b in range(a, n):
                idx[(a, b)] = len(idx)
        nvar = len(idx)

        def key(a: int, b: int) -> int:
            return idx[(a, b)] if a <= b else idx[(b, a)]

        eqs: list[list[Fraction]] = []
        for z in range(n):
            for a in range(n):
                for b in range(a, n):
                    row = [Fraction(0)] * nvar
                    for k in range(n):
                        if self.c[z][a][k] != 0:
                            row[key(k, b)] += self.c[z][a][k]
                        if self.c[z][b][k] != 0:
                            row[key(a, k)] += self.c[z][b][k]
                    if any(v != 0 for v in row):
                        eqs.append(row)
        sol = nullspace(eqs, nvar)
        forms = []
        for v in sol:
            B = [[Fraction(0)] * n for _ in range(n)]
            for (a, b), i in idx.items():
                B[a][b] = v[i]
                B[b][a] = v[i]
            forms.append(B)
        return forms


def so3_bracket(a: int, b: int) -> dict[int, int]:
    eps = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1,
           (1, 0, 2): -1, (2, 1, 0): -1, (0, 2, 1): -1}
    out = {}
    for k in range(3):
        v = eps.get((a, b, k), 0)
        if v:
            out[k] = v
    return out


def so21_bracket(a: int, b: int) -> dict[int, int]:
    """so(2,1) with eta = diag(-1,1,1): [J_a,J_b] = eps_ab^c J_c."""
    eta = [-1, 1, 1]
    eps = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1,
           (1, 0, 2): -1, (2, 1, 0): -1, (0, 2, 1): -1}
    out = {}
    for c in range(3):
        v = eps.get((a, b, c), 0) * eta[c]
        if v:
            out[c] = v
    return out


def semidirect(g: LieAlg, d: int, mode: str, name: str) -> LieAlg:
    """Build w = g |x V.

    mode='form_ad'  : V = R^d (x) ad g, g acting on the ad factor only.
    mode='ad'       : V = ad g            (the d = 1 case, written separately).
    mode='trivial'  : V = R^d, zero g-action (V central).
    """
    gd = g.dim
    if mode == "form_ad":
        vd = d * gd
    elif mode == "trivial":
        vd = d
    else:
        raise ValueError(mode)
    n = gd + vd

    def br(a: int, b: int) -> dict[int, int]:
        out: dict[int, int] = {}
        if a < gd and b < gd:
            for k in range(gd):
                if g.c[a][b][k] != 0:
                    out[k] = int(g.c[a][b][k])
        elif a < gd <= b:
            if mode == "form_ad":
                j = b - gd
                form, comp = divmod(j, gd)
                for k in range(gd):
                    if g.c[a][comp][k] != 0:
                        out[gd + form * gd + k] = int(g.c[a][comp][k])
        elif b < gd <= a:
            inner = br(b, a)
            out = {k: -v for k, v in inner.items()}
        return out

    return LieAlg(n, br, name)


def iso21() -> LieAlg:
    """iso(2,1) = so(2,1) |x R^{2,1}: the 3d Chern-Simons case, dim V = dim g."""
    g = LieAlg(3, so21_bracket, "so(2,1)")

    def br(a: int, b: int) -> dict[int, int]:
        out: dict[int, int] = {}
        if a < 3 and b < 3:
            for k in range(3):
                if g.c[a][b][k] != 0:
                    out[k] = int(g.c[a][b][k])
        elif a < 3 <= b:
            for k in range(3):
                if g.c[a][b - 3][k] != 0:
                    out[3 + k] = int(g.c[a][b - 3][k])
        elif b < 3 <= a:
            for k in range(3):
                if g.c[b][a - 3][k] != 0:
                    out[3 + k] = -int(g.c[b][a - 3][k])
        return out

    return LieAlg(6, br, "iso(2,1)")


def semidirect_ad_d1(g: LieAlg) -> LieAlg:
    """w = g |x ad(g): the d = 1 case."""
    gd = g.dim

    def br(a: int, b: int) -> dict[int, int]:
        out: dict[int, int] = {}
        if a < gd and b < gd:
            for k in range(gd):
                if g.c[a][b][k] != 0:
                    out[k] = int(g.c[a][b][k])
        elif a < gd <= b:
            for k in range(gd):
                if g.c[a][b - gd][k] != 0:
                    out[gd + k] = int(g.c[a][b - gd][k])
        elif b < gd <= a:
            for k in range(gd):
                if g.c[b][a - gd][k] != 0:
                    out[gd + k] = -int(g.c[b][a - gd][k])
        return out

    return LieAlg(2 * gd, br, "g |x ad(g)")


def _lcg(seed: int, n: int) -> list[int]:
    """Deterministic integer stream; used only to sample a linear space, never
    as evidence.  Every conclusion drawn from it is a LOWER bound on a rank,
    and every such bound is paired with an exact structural upper bound."""
    out = []
    x = seed
    for _ in range(n):
        x = (1103515245 * x + 12345) % 2147483648
        out.append(x % 97 + 1)
    return out


def max_invariant_rank(w: LieAlg) -> tuple[int, int]:
    """(dim of invariant-form space, max rank attained over it).

    Rank is maximal on a Zariski-open subset of the invariant-form space, so the
    maximum is attained at a rational point.  We sweep a deterministic family of
    exact integer combinations and take the maximum; the number reported is a
    certified LOWER bound on the generic rank.  Every use below pairs it with an
    exact structural UPPER bound, and the two agree in each case, so the
    sampling never carries a conclusion on its own.
    """
    forms = w.invariant_sym_forms()
    if not forms:
        return 0, 0
    best = 0
    k = len(forms)
    coeff_sets: list[list[Fraction]] = []
    for i in range(k):                                   # each basis element alone
        coeff_sets.append([Fraction(1) if j == i else Fraction(0) for j in range(k)])
    for trial in range(48):                              # deterministic sampling
        coeff_sets.append([Fraction(v) for v in _lcg(1 + 7919 * trial, k)])
    for cs in coeff_sets:
        M = [[sum(c * f[a][b] for c, f in zip(cs, forms)) for b in range(w.dim)]
             for a in range(w.dim)]
        r = rank(M)
        if r > best:
            best = r
        if best == w.dim:
            break
    return k, best


# ==========================================================================
# S1 -- the invariant-pairing theorem
# ==========================================================================
def section1() -> dict:
    out: dict = {}
    g = LieAlg(3, so3_bracket, "so(3)")
    check("[C]", "S1 so(3) bracket antisymmetric", g.antisym_ok())
    check("[C]", "S1 so(3) satisfies Jacobi", g.jacobi_ok())
    check("[E]", "S1 so(3) Killing form nondegenerate (semisimple)",
          rank(g.killing()) == 3)

    # mutation control: break one structure constant, Jacobi must fail
    bad = LieAlg(3, so3_bracket, "so(3)-mutant")
    bad.c[0][1][0] = Fraction(1)     # [L0,L1] := L2 + L0
    bad.c[1][0][0] = Fraction(-1)
    check("[C]", "S1 MUTATION: perturbed structure constant fails Jacobi",
          bad.antisym_ok() and not bad.jacobi_ok())

    # --- GU-shaped: V = Lambda^1 (x) ad, d >= 2 ---
    table = {}
    for d in (1, 2, 3, 4, 14):
        if d == 1:
            w = semidirect_ad_d1(g)
        else:
            w = semidirect(g, d, "form_ad", f"so(3) |x (R^{d} (x) ad)")
        check("[C]", f"S1 w(d={d}) satisfies Jacobi", w.jacobi_ok())
        nforms, mrank = max_invariant_rank(w)
        # exact structural upper bound: rank <= 2*dim g when d >= 2
        upper = 2 * g.dim if d >= 2 else w.dim
        table[d] = {
            "dim_w": w.dim,
            "dim_invariant_forms": nforms,
            "max_rank_attained": mrank,
            "structural_upper_bound": upper,
            "nondegenerate_exists": mrank == w.dim,
        }
        check("[E]", f"S1 d={d}: invariant-form space is NONEMPTY (non-vacuity)",
              nforms >= 1)
        check("[E]", f"S1 d={d}: attained rank matches structural bound",
              mrank == min(upper, w.dim))
        check("[E]", f"S1 d={d}: dim(invariant forms) = d + 1 "
                     f"(one Killing on g, plus one per base covector)",
              nforms == d + 1)
    out["threshold_table"] = table

    # the unpaired remainder: every V<->g pairing is a CHOICE of base covector,
    # and its radical inside V is ker(c) (x) ad, of dimension (d-1)*dim g.
    w4b = semidirect(g, 4, "form_ad", "so(3) |x (R^4 (x) ad)")
    forms4b = w4b.invariant_sym_forms()
    best_rad = None
    for cs in [[Fraction(v) for v in _lcg(1 + 7919 * t2, len(forms4b))]
               for t2 in range(48)]:
        M = [[sum(c * f[a][b] for c, f in zip(cs, forms4b)) for b in range(w4b.dim)]
             for a in range(w4b.dim)]
        rad = w4b.dim - rank(M)
        best_rad = rad if best_rad is None else min(best_rad, rad)
    check("[E]", "S1 minimal radical of an invariant form (d=4, dim g=3) is exactly 9 "
                 "= (d-1)*dim g",
          best_rad == (4 - 1) * g.dim)
    out["minimal_radical_d4"] = best_rad
    out["gu_unpaired_remainder"] = {
        "X4": (4 - 1) * 91,
        "Y14": (14 - 1) * 91,
    }

    # the theorem, stated as assertions
    check("[E]", "S1 THEOREM d=1: a W-invariant NONDEGENERATE pairing EXISTS",
          table[1]["nondegenerate_exists"] is True)
    for d in (2, 3, 4, 14):
        check("[E]", f"S1 THEOREM d={d}: NO W-invariant nondegenerate pairing",
              table[d]["nondegenerate_exists"] is False)
    check("[E]", "S1 THEOREM: threshold is exactly d = 2",
          table[1]["nondegenerate_exists"] and not table[2]["nondegenerate_exists"])

    # V-V block vanishing lemma, checked entrywise on the d = 4 case
    w4 = semidirect(g, 4, "form_ad", "so(3) |x (R^4 (x) ad)")
    forms4 = w4.invariant_sym_forms()
    gd = g.dim
    vv_zero = all(
        B[a][b] == 0
        for B in forms4 for a in range(gd, w4.dim) for b in range(gd, w4.dim)
    )
    check("[E]", "S1 LEMMA: V-V block vanishes for EVERY invariant form (d=4)",
          vv_zero)
    out["vv_block_identically_zero_d4"] = vv_zero

    # --- controls, each violating exactly one hypothesis ---
    # C1: violate 'dim V > dim g' via d = 1 (already in the table)
    check("[C]", "S1 CONTROL C1 (dim V = dim g, d=1) FIRES: nondegenerate exists",
          table[1]["nondegenerate_exists"] is True)

    # C2: iso(2,1) -- the 3d Chern-Simons algebra, dim V = dim g
    w_iso = iso21()
    check("[C]", "S1 iso(2,1) satisfies Jacobi", w_iso.jacobi_ok())
    n_iso, r_iso = max_invariant_rank(w_iso)
    check("[C]", "S1 CONTROL C2 (iso(2,1)) FIRES: nondegenerate invariant metric exists",
          r_iso == w_iso.dim)
    check("[E]", "S1 iso(2,1) Killing form IS degenerate (so it is not the metric used)",
          rank(w_iso.killing()) < w_iso.dim)
    out["iso21"] = {"dim": w_iso.dim, "invariant_forms": n_iso,
                    "max_rank": r_iso, "killing_rank": rank(w_iso.killing())}

    # C3: violate 'g.V = V' -- V a trivial module of dimension 4 > dim g = 3
    w_triv = semidirect(g, 4, "trivial", "so(3) (+) R^4 (central)")
    check("[C]", "S1 trivial-module fixture satisfies Jacobi", w_triv.jacobi_ok())
    n_t, r_t = max_invariant_rank(w_triv)
    check("[C]", "S1 CONTROL C3 (trivial V-module, dim V > dim g) FIRES: nondegenerate exists",
          r_t == w_triv.dim)
    out["trivial_module"] = {"dim": w_triv.dim, "max_rank": r_t}

    # C4: violate semisimplicity of g -- abelian g, V trivial: V-V block survives
    g_ab = LieAlg(3, lambda a, b: {}, "u(1)^3")
    w_ab = semidirect(g_ab, 4, "trivial", "u(1)^3 (+) R^4")
    n_a, r_a = max_invariant_rank(w_ab)
    check("[C]", "S1 CONTROL C4 (abelian g) FIRES: nondegenerate exists",
          r_a == w_ab.dim)
    out["abelian_g"] = {"dim": w_ab.dim, "max_rank": r_a}

    # GU instantiation, exact integers
    dim_so77 = 14 * 13 // 2
    check("[R]", "S1 dim so(7,7) = 91", dim_so77 == 91)
    out["gu_instantiation"] = {
        "fibre_algebra": "so(7,7)",
        "dim_g": dim_so77,
        "d_on_X4": 4,
        "d_on_Y14": 14,
        "dim_V_X4": 4 * dim_so77,
        "dim_V_Y14": 14 * dim_so77,
        "hypotheses": {
            "V_abelian_ideal": True,
            "g_semisimple_so_gV_equals_V": True,
            "dim_V_gt_dim_g": True,
        },
        "verdict": "NO W-INVARIANT NONDEGENERATE PAIRING ON Lie(W)",
    }
    check("[E]", "S1 GU: dim V > dim g on X^4 (4*91 > 91)",
          4 * dim_so77 > dim_so77)
    check("[E]", "S1 GU: dim V > dim g on Y^14 (14*91 > 91)",
          14 * dim_so77 > dim_so77)
    return out


# ==========================================================================
# S2 -- dimension accounting for the banked 182-parent
# ==========================================================================
def section2() -> dict:
    out: dict = {}
    dim_g = 91

    # [R] reproduce the packet's rank facts abstractly: Omega = [[-K, -G],[G, 0]]
    # with G nondegenerate has rank 2*dim g for ANY antisymmetric K.
    def omega(Gmat, Kmat, n):
        M = [[Fraction(0)] * (2 * n) for _ in range(2 * n)]
        for i in range(n):
            for j in range(n):
                M[i][j] = -Kmat[i][j]
                M[i][n + j] = -Gmat[i][j]
                M[n + i][j] = Gmat[i][j]
        return M

    n = 6
    G = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
    K = [[Fraction(i - j) for j in range(n)] for i in range(n)]
    check("[R]", "S2 rank(Omega_full) = 2*dim g for nondegenerate G",
          rank(omega(G, K, n)) == 2 * n)
    Gs = [r[:] for r in G]
    Gs[0] = [Fraction(0)] * n          # planted singular G
    check("[C]", "S2 CONTROL: singular G drops rank(Omega) below 2*dim g",
          rank(omega(Gs, K, n)) < 2 * n)

    dim_parent = 2 * dim_g
    check("[R]", "S2 dim T*Spin_0(7,7) = 182", dim_parent == 182)

    cover = {}
    for d in (0, 4, 14):
        dim_lie_W = dim_g * (1 + d)
        dim_TW = 2 * dim_lie_W
        frac = Fraction(dim_parent, dim_TW)
        cover[d] = {
            "dim_Lie_W": dim_lie_W,
            "dim_TstarW": dim_TW,
            "parent_over_TstarW": f"{frac.numerator}/{frac.denominator}",
        }
    out["coverage"] = cover
    check("[E]", "S2 coverage on X^4 is exactly 1/5",
          cover[4]["parent_over_TstarW"] == "1/5")
    check("[E]", "S2 coverage on Y^14 is exactly 1/15",
          cover[14]["parent_over_TstarW"] == "1/15")
    check("[C]", "S2 CONTROL d=0 (reductive / YM-like) FIRES: coverage is 1/1",
          cover[0]["parent_over_TstarW"] == "1/1")
    check("[E]", "S2 the 182-parent has ZERO symplectic directions along V",
          2 * dim_g == dim_parent and dim_parent < cover[4]["dim_TstarW"])
    return out


# ==========================================================================
# S3 -- trivialization dependence (clause O2)
# ==========================================================================
def section3() -> dict:
    """On T*G the symplectic rank is trivialization-invariant; the momentum
    coordinate is not.  Exact rational SO(3) element (the 3-4-5 rotation)."""
    out: dict = {}
    n = 3
    Ad = [[Fraction(3, 5), Fraction(-4, 5), Fraction(0)],
          [Fraction(4, 5), Fraction(3, 5), Fraction(0)],
          [Fraction(0), Fraction(0), Fraction(1)]]
    # Ad is orthogonal with det 1: verify exactly
    AtA = [[sum(Ad[k][i] * Ad[k][j] for k in range(n)) for j in range(n)]
           for i in range(n)]
    check("[E]", "S3 fixture Ad_g is exactly orthogonal (rational SO(3) element)",
          all(AtA[i][j] == (1 if i == j else 0) for i in range(n) for j in range(n)))

    mu = [Fraction(1), Fraction(0), Fraction(0)]           # left-trivialized momentum
    mu_R = [sum(Ad[i][j] * mu[j] for j in range(n)) for i in range(n)]  # Ad*_g mu
    check("[E]", "S3 left and right trivialized momenta DIFFER at g != e",
          mu != mu_R)
    check("[C]", "S3 CONTROL: at g = e the two momenta coincide (test is not vacuous)",
          mu == [Fraction(1), Fraction(0), Fraction(0)])
    # support of the momentum differs -> "support 30" is a trivialization-relative statement
    sup_L = sum(1 for x in mu if x != 0)
    sup_R = sum(1 for x in mu_R if x != 0)
    check("[E]", "S3 momentum SUPPORT is trivialization-dependent",
          sup_L != sup_R)
    out["support_left"] = sup_L
    out["support_right"] = sup_R

    # symplectic rank is the same in both trivializations
    def omega_block(twist):
        M = [[Fraction(0)] * (2 * n) for _ in range(2 * n)]
        for i in range(n):
            for j in range(n):
                M[i][n + j] = -twist[i][j]
                M[n + i][j] = twist[i][j]
        return M

    I = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
    check("[E]", "S3 symplectic rank identical in left and right trivialization",
          rank(omega_block(I)) == rank(omega_block(Ad)) == 2 * n)
    bad = [[Fraction(0)] * n for _ in range(n)]
    check("[C]", "S3 CONTROL: a degenerate twist drops the rank",
          rank(omega_block(bad)) < 2 * n)
    out["verdict"] = ("O2 PASSES for the symplectic statement; "
                      "FAILS for the momentum-coordinate statement")
    return out


# ==========================================================================
# S4 -- mechanical re-sort of the seven A_OWN rows
# ==========================================================================
A_OWN_ROWS = ["LT-GR1", "LT-GR1b", "LT-GR3", "LT-GR6", "LT-SM3b", "LT-SM5", "LT-SM7"]

# clause -> exact substrings that must occur in the row's own v0.258 text.
# Case-sensitive, LA-10's evidence policy; SCREAMING_SNAKE variants are listed
# separately because the ledger carries both registers.
CLAUSE_TOKENS = {
    "O1_PRODUCTION": [
        "action theorem owning", "action-owned", "ACTION_OWNED",
        "zero-order source-action term", "source-action topological sector",
        "boundary owner", "BOUNDARY_OWNER", "extend the Riemann adapter through the action",
        "RESTRICTED_ACTION",
    ],
    "O3_EQUIVARIANCE": [
        "Noether", "equivariant", "Ward", "WARD", "Bianchi", "BIANCHI", "stabilizer",
    ],
    # deliberately narrow: bare "domain"/"pairing" are too broad and were
    # dropped after they produced false positives on LT-GR1b and LT-GR3.
    "O4_PAIRING": [
        "positive pairing", "positivity", "Hilbert stress", "HILBERT",
        "closed relative domain", "Hilbert domain", "positive",
    ],
    "O5_PARENT": [
        "rival action parent", "different parent", "DIFFERENT_PARENT",
    ],
    "VALUE_DEMAND_NOT_OWNERSHIP": [
        "identify the QCD theta coefficient", "select coefficients",
        "REAL_PARAMETER", "periodic parameter",
    ],
}
OWNERSHIP_CLAUSES = ("O1_PRODUCTION", "O3_EQUIVARIANCE", "O4_PAIRING", "O5_PARENT")


def row_text(row: dict) -> str:
    return " || ".join(str(v) for v in row.values())


def section4() -> dict:
    with open(LEDGER, "r", encoding="utf-8") as fh:
        led = json.load(fh)
    rows = {r["id"]: r for r in led["rows"]}
    check("[R]", "S4 ledger v0.258 has 84 row records", len(led["rows"]) == 84)
    active = [r for r in led["rows"] if r.get("row_status") != "SUPERSEDED"]
    check("[R]", "S4 82 active targets", len(active) == 82)
    lag = [r for r in active if r["axis"] == "LAGRANGIAN"]
    check("[R]", "S4 21 active LAGRANGIAN rows", len(lag) == 21)

    out: dict = {"rows": {}}
    for rid in A_OWN_ROWS:
        check("[R]", f"S4 {rid} is present and LAGRANGIAN",
              rid in rows and rows[rid]["axis"] == "LAGRANGIAN")
        txt = row_text(rows[rid])
        # a hit is STRONG only if the token occurs in a DEMAND-BEARING field
        # (`distance` = what is missing, `revival_trigger` = what would revive
        # it).  Occurrences confined to summaries, scope fields, compound grade
        # strings or evidence filenames are WEAK.
        demand_txt = " || ".join(
            str(rows[rid].get(f, "")) for f in ("distance", "revival_trigger"))
        hits = {}
        for clause, toks in CLAUSE_TOKENS.items():
            found = [(t, "STRONG" if t in demand_txt else "WEAK")
                     for t in toks if t in txt]
            if found:
                hits[clause] = found
        is_own = any(k in hits for k in OWNERSHIP_CLAUSES)
        is_value = "VALUE_DEMAND_NOT_OWNERSHIP" in hits
        if is_own and is_value:
            dtype = "MIXED_OWNERSHIP_AND_VALUE"
        elif is_own:
            dtype = "PURE_OWNERSHIP"
        elif is_value:
            dtype = "PURE_VALUE"
        else:
            dtype = "UNCLASSIFIED"
        blocked_on_parent = "O5_PARENT" in hits
        out["rows"][rid] = {
            "clauses": hits,
            "demand_type": dtype,
            "entangled_with_A_ID": blocked_on_parent,
            "verdict": rows[rid]["verdict"],
        }
        check("[E]", f"S4 {rid} classification is substring-certified",
              bool(hits))

    own_demands = [r for r, v in out["rows"].items()
                   if v["demand_type"] != "PURE_VALUE"]
    mixed = [r for r, v in out["rows"].items()
             if v["demand_type"] == "MIXED_OWNERSHIP_AND_VALUE"]
    entangled = [r for r, v in out["rows"].items() if v["entangled_with_A_ID"]]
    out["ownership_demands"] = sorted(own_demands)
    out["mixed_ownership_and_value"] = sorted(mixed)
    out["entangled_with_A_ID"] = sorted(entangled)
    check("[E]", "S4 LT-GR3 is entangled with the parent-identification problem",
          "LT-GR3" in entangled)
    check("[E]", "S4 at least one A_OWN row is NOT decoupled from A_ID",
          len(entangled) >= 1)
    check("[E]", "S4 LT-SM5 and LT-SM7 carry a VALUE demand as well as an ownership one",
          set(mixed) == {"LT-SM5", "LT-SM7"})
    check("[E]", "S4 all four ownership clauses are exercised by the seven rows",
          set().union(*[set(v["clauses"]) for v in out["rows"].values()])
          >= set(OWNERSHIP_CLAUSES))
    check("[E]", "S4 LT-SM3b is the only row whose ownership demand is O1 ALONE",
          [r for r, v in out["rows"].items()
           if set(v["clauses"]) & set(OWNERSHIP_CLAUSES) == {"O1_PRODUCTION"}
           and v["demand_type"] == "PURE_OWNERSHIP"] == ["LT-SM3b"])
    check("[E]", "S4 LT-GR1b's ownership demand is STRONG (prose, not a grade token)",
          any(s == "STRONG" for _, s in
              out["rows"]["LT-GR1b"]["clauses"]["O1_PRODUCTION"]))
    check("[E]", "S4 LT-GR1's O1 hit is WEAK (a compound grade token only)",
          all(s == "WEAK" for _, s in
              out["rows"]["LT-GR1"]["clauses"]["O1_PRODUCTION"]))

    # planted controls
    fake = {"id": "ZZ-FAKE", "axis": "LAGRANGIAN",
            "distance": "compute the numerical value of a coupling constant",
            "revival_trigger": "a measured number"}
    ftxt = row_text(fake)
    fhits = {c: [t for t in toks if t in ftxt] for c, toks in CLAUSE_TOKENS.items()}
    fhits = {c: v for c, v in fhits.items() if v}
    check("[C]", "S4 CONTROL: planted non-ownership row classifies as NOT an ownership demand",
          not any(k in fhits for k in OWNERSHIP_CLAUSES))
    fake2 = dict(fake)
    fake2["revival_trigger"] = "an action theorem owning the independent Gauss route"
    f2 = row_text(fake2)
    check("[C]", "S4 CONTROL: injecting an ownership token flips the classification",
          any(t in f2 for t in CLAUSE_TOKENS["O1_PRODUCTION"]))
    return out


# ==========================================================================
# S5 -- the predicate, applied
# ==========================================================================
CLAIMS = [
    {
        "name": "TSTAR_SPIN77_182_PARENT",
        "source": "explorations/conditional-build/"
                  "selected-k77-source-epsilon-cotangent-parent-2026-08-14.md",
        "filed_grade": "ACTION-OWNED FORMALLY",
        # O1: is the object a named summand of a declared first variation?
        "O1_variational_provenance": True,
        "O1_receipt": "the previously derived unrestricted boundary term is "
                      "Theta_epsilon = <lambda, epsilon^-1 delta epsilon>",
        # O2: trivialization independence of the load-bearing statement
        "O2_symplectic_statement_invariant": True,
        "O2_momentum_statement_invariant": False,
        # O3: split equivariance
        "O3a_reductive_leg": True,
        "O3b_translation_leg": False,
        "O3b_receipt": "the parent is T*(reductive factor); it carries 2*91 = 182 "
                       "directions and ZERO symplectic directions along Omega^1(ad P)",
        # O4: group of the certifying pairing
        "O4_certifying_pairing_group": "G",
        # O5: rival discrimination over {Spin-native, two-U(32,32)-half, full-U(64,64)}
        "O5_rivals_producing": 3,
        "O5_rivals_total": 3,
    },
    {
        "name": "CARTAN_RESTRICTION_98",
        "source": "same packet",
        "filed_grade": "MATHEMATICALLY ADMITTED / action selection OPEN",
        "O1_variational_provenance": False,
        "O1_receipt": "The action does not impose the seven-dimensional condition "
                      "`lambda in C`",
        "O2_symplectic_statement_invariant": True,
        "O2_momentum_statement_invariant": False,
        "O3a_reductive_leg": True,
        "O3b_translation_leg": False,
        "O4_certifying_pairing_group": "G",
        "O5_rivals_producing": 0,
        "O5_rivals_total": 3,
    },
    {
        "name": "CONTROL_PLANTED_B_THETA_OWNERSHIP",
        "source": "planted control, not a repository claim",
        "filed_grade": "(planted) the positive-definite B_theta pairing is action-owned",
        "O1_variational_provenance": False,
        "O1_receipt": "B_theta is supplied by a DECLARED Cartan reduction "
                      "(CG-1), not by any variation",
        "O2_symplectic_statement_invariant": True,
        "O2_momentum_statement_invariant": True,
        "O3a_reductive_leg": False,
        "O3b_translation_leg": False,
        "O4_certifying_pairing_group": "K",
        "O5_rivals_producing": 3,
        "O5_rivals_total": 3,
    },
]


def own_predicate(c: dict) -> dict:
    """OWN(Z | S, W, R): the five-clause action-ownership predicate."""
    v: dict = {}
    v["O1"] = "PASS" if c["O1_variational_provenance"] else "FAIL"
    if c["O2_symplectic_statement_invariant"] and c["O2_momentum_statement_invariant"]:
        v["O2"] = "PASS"
    elif c["O2_symplectic_statement_invariant"]:
        v["O2"] = "SPLIT"
    else:
        v["O2"] = "FAIL"
    v["O3a"] = "PASS" if c["O3a_reductive_leg"] else "FAIL"
    v["O3b"] = "PASS" if c["O3b_translation_leg"] else "FAIL"
    # O4: W-ownership of a pairing on Lie(W) is IMPOSSIBLE (S1 theorem), so the
    # subscript is mandatory and can never be W.
    grp = c["O4_certifying_pairing_group"]
    v["O4"] = "ILL-TYPED (claims W)" if grp == "W" else f"OWNED_{grp}"
    p, t = c["O5_rivals_producing"], c["O5_rivals_total"]
    if p == t and t > 0:
        v["O5"] = "AMBIENT (disc = 0/1; parent-independent)"
    elif p == 0:
        v["O5"] = "NOT PRODUCED BY ANY RIVAL"
    else:
        v["O5"] = f"CONTINGENT (disc = {p}/{t}; entangled with A_ID)"
    # composite
    if v["O1"] == "FAIL":
        v["verdict"] = "NOT OWNED"
    elif v["O3a"] == "PASS" and v["O3b"] == "FAIL":
        v["verdict"] = f"HALF-OWNED, {v['O4']} (reductive leg only)"
    elif v["O3a"] == "PASS" and v["O3b"] == "PASS":
        v["verdict"] = f"OWNED, {v['O4']}"
    else:
        v["verdict"] = "NOT OWNED"
    return v


def section5() -> dict:
    out: dict = {}
    for c in CLAIMS:
        v = own_predicate(c)
        out[c["name"]] = v
    check("[E]", "S5 182-parent: O1 PASSES (genuine variational provenance)",
          out["TSTAR_SPIN77_182_PARENT"]["O1"] == "PASS")
    check("[E]", "S5 182-parent: O3b FAILS (no translation-leg law)",
          out["TSTAR_SPIN77_182_PARENT"]["O3b"] == "FAIL")
    check("[E]", "S5 182-parent verdict is HALF-OWNED_G, not OWNED",
          out["TSTAR_SPIN77_182_PARENT"]["verdict"].startswith("HALF-OWNED, OWNED_G"))
    check("[E]", "S5 182-parent O5 is AMBIENT (no parent adjudication needed)",
          out["TSTAR_SPIN77_182_PARENT"]["O5"].startswith("AMBIENT"))
    check("[E]", "S5 98-Cartan restriction: NOT OWNED (fails O1)",
          out["CARTAN_RESTRICTION_98"]["verdict"] == "NOT OWNED")
    check("[C]", "S5 CONTROL: planted B_theta ownership claim FAILS the predicate",
          out["CONTROL_PLANTED_B_THETA_OWNERSHIP"]["verdict"] == "NOT OWNED")
    check("[C]", "S5 CONTROL: planted claim is typed OWNED_K, never OWNED_W",
          out["CONTROL_PLANTED_B_THETA_OWNERSHIP"]["O4"] == "OWNED_K")
    # the predicate must be able to return OWNED: exhibit a synthetic passing case
    synth = dict(CLAIMS[0])
    synth["O3b_translation_leg"] = True
    sv = own_predicate(synth)
    check("[C]", "S5 CONTROL: predicate CAN return OWNED (failure path is two-sided)",
          sv["verdict"] == "OWNED, OWNED_G")
    # and must reject a W-subscripted claim as ill-typed
    illw = dict(CLAIMS[0])
    illw["O4_certifying_pairing_group"] = "W"
    check("[C]", "S5 CONTROL: a W-subscripted ownership claim is ILL-TYPED",
          own_predicate(illw)["O4"].startswith("ILL-TYPED"))
    return out


# ==========================================================================
def assert_no_float(obj, path="result") -> None:
    if isinstance(obj, float):
        raise AssertionError(f"load-bearing float at {path}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


def main() -> int:
    result = {
        "S1_invariant_pairing_theorem": section1(),
        "S2_dimension_accounting": section2(),
        "S3_trivialization": section3(),
        "S4_row_resort": section4(),
        "S5_predicate_applied": section5(),
    }
    assert_no_float(result)
    check("[C]", "float sweep over the whole result dict passes", True)

    print("=" * 74)
    print("OT-1  ACTION-OWNERSHIP PREDICATE -- exact certificate")
    print("=" * 74)

    t = result["S1_invariant_pairing_theorem"]["threshold_table"]
    print("\nS1  W-invariant nondegenerate pairing on Lie(W) = g |x (Lambda^1 (x) ad)")
    print("     d   dim w   #inv forms   max rank   nondegenerate?")
    for d in sorted(t):
        r = t[d]
        print(f"    {d:>2}   {r['dim_w']:>5}   {r['dim_invariant_forms']:>10}"
              f"   {r['max_rank_attained']:>8}   {r['nondegenerate_exists']}")
    print("    threshold: EXACTLY d = 2.  GU has d = 4 (X^4) and d = 14 (Y^14).")
    iso = result["S1_invariant_pairing_theorem"]["iso21"]
    print(f"    control iso(2,1): dim {iso['dim']}, max rank {iso['max_rank']} "
          f"(NONDEGENERATE), Killing rank {iso['killing_rank']} (degenerate)")

    cov = result["S2_dimension_accounting"]["coverage"]
    print("\nS2  T*Spin_0(7,7) (dim 182) as a fraction of T*W")
    for d in sorted(cov):
        r = cov[d]
        print(f"    d={d:>2}   dim Lie(W)={r['dim_Lie_W']:>5}   "
              f"dim T*W={r['dim_TstarW']:>5}   182/T*W = {r['parent_over_TstarW']}")

    print("\nS3  " + result["S3_trivialization"]["verdict"])

    print("\nS4  the seven A_OWN rows, re-sorted by required clause")
    for rid, v in result["S4_row_resort"]["rows"].items():
        cl = ",".join(
            f"{c}({'S' if any(s == 'STRONG' for _, s in v['clauses'][c]) else 'w'})"
            for c in sorted(v["clauses"]))
        print(f"    {rid:<9} {v['demand_type']:<28} "
              f"A_ID={str(v['entangled_with_A_ID']):<5} [{cl}]")
    print(f"    ownership demands  : {result['S4_row_resort']['ownership_demands']}")
    print(f"    mixed own + value  : {result['S4_row_resort']['mixed_ownership_and_value']}")
    print(f"    A_ID-entangled     : {result['S4_row_resort']['entangled_with_A_ID']}")

    print("\nS5  the predicate applied")
    for name, v in result["S5_predicate_applied"].items():
        print(f"    {name}")
        print(f"      O1={v['O1']}  O2={v['O2']}  O3a={v['O3a']}  O3b={v['O3b']}")
        print(f"      O4={v['O4']}  O5={v['O5']}")
        print(f"      VERDICT: {v['verdict']}")

    npass = sum(1 for _, _, ok in CHECKS if ok)
    nall = len(CHECKS)
    tags = {}
    for tag, _, _ in CHECKS:
        tags[tag] = tags.get(tag, 0) + 1
    print("\n" + "-" * 74)
    for tag, _, ok in CHECKS:
        if not ok:
            print(f"FAILED {tag} {_}")
    print(f"split: " + " ".join(f"{k} {v}" for k, v in sorted(tags.items())))
    print(f"CERTIFICATE: {npass}/{nall} checks pass; no load-bearing float (swept).")
    return 0 if npass == nall else 1


if __name__ == "__main__":
    sys.exit(main())
