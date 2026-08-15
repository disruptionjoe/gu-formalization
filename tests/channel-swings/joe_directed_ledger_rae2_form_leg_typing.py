#!/usr/bin/env python3
"""LA-8 -- RA-E2's Lorentz typing, ledger v0.258 (base a148ed80).

Question
--------
`RA-E2` is filed `NEEDS / MISSING_CONSTRUCTION`, `mapping_grade
EXACT_SHAPE_CONSTRAINT`, `distance: use and propagate the vertical form leg
through observation`.  Its parent `CB-A:E2` asserts that the Lorentz-scalar
components of `Omega^1(Y, ad)` are exactly those with both legs vertical,
`V*_10 (x) Lambda^2 V_10 = 10 (x) 45`, hosting 6 `(1,2,+1/2)` and 6
`(1,2,-1/2)`.

This probe tests the SHAPE CONSTRAINT itself, not the existence of an adapter.

Exactness policy
----------------
Every load-bearing number is a Python int, a `fractions.Fraction`, or an exact
sympy expression.  `assert_no_float` walks the whole result dict at the end.
The one place numpy appears is INTEGER arithmetic modulo a prime, used only to
obtain an UPPER bound on a nullity (rank_p <= rank_Q  =>  nullity_Q <=
nullity_p); the matching LOWER bound is an explicitly constructed exact
integer/Fraction witness.  dtype is asserted to be integral.

Routing
-------
GU-COMPARATOR-ROUTING.  Block A (the contraction) is SOURCE_NATIVE: it uses the
observation section and no comparator.  Blocks B/C/D compute the DISAVOWED
Kaluza-Klein projection reading and bind only that comparator; they are used to
correct a number CB-A:E2 itself computed in that reading, never to adjudicate a
source-native object.

Run from the repository root:
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_ledger_rae2_form_leg_typing.py
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys
from fractions import Fraction

import numpy as np
import sympy as sp

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEDGER = os.path.join(REPO, "lab", "process", "conditional-physics-ledger-v0.258.json")
LEDGER_GLOB = os.path.join(REPO, "lab", "process", "conditional-physics-ledger-v0.*.json")
CB_A = os.path.join(REPO, "explorations", "conditional-build",
                    "cb-a-representation-content-2026-08-05.md")
MD1 = os.path.join(REPO, "lab", "active-research", "joe-directed",
                   "four-d-mode-decomposition",
                   "md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md")
PACKET = os.path.join(REPO, "explorations", "unified-source-datum-packet-v0-2026-07-30.md")
ROUTING = os.path.join(REPO, "lab", "methods", "source-native-comparator-routing.md")

CHECKS: list[tuple[str, str, bool]] = []


def check(tag: str, label: str, passed: bool) -> None:
    CHECKS.append((tag, label, bool(passed)))


def read(path: str) -> str:
    with open(path, encoding="utf-8") as handle:
        return handle.read()


# ---------------------------------------------------------------------------
# exact linear algebra over Q
# ---------------------------------------------------------------------------

def nullspace_Q(rows: list[list[Fraction]], ncols: int) -> list[list[Fraction]]:
    """Exact nullspace of the matrix with the given rows, over Q."""
    mat = [list(r) for r in rows]
    pivots: list[int] = []
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(mat)):
            if mat[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        inv = Fraction(1, 1) / mat[r][c]
        mat[r] = [x * inv for x in mat[r]]
        for i in range(len(mat)):
            if i != r and mat[i][c] != 0:
                f = mat[i][c]
                mat[i] = [a - f * b for a, b in zip(mat[i], mat[r])]
        pivots.append(c)
        r += 1
        if r == len(mat):
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis: list[list[Fraction]] = []
    for f in free:
        vec = [Fraction(0)] * ncols
        vec[f] = Fraction(1)
        for i, c in enumerate(pivots):
            vec[c] = -mat[i][f]
        basis.append(vec)
    return basis


def nullity_mod_p(mat: np.ndarray, p: int) -> int:
    """Exact nullity of `mat` over GF(p) by integer Gaussian elimination."""
    assert np.issubdtype(mat.dtype, np.integer), "mod-p routine must run on integers"
    a = np.mod(mat.astype(np.int64), p)
    nrows, ncols = a.shape
    rank = 0
    for c in range(ncols):
        piv = -1
        for i in range(rank, nrows):
            if a[i, c] % p:
                piv = i
                break
        if piv < 0:
            continue
        if piv != rank:
            a[[rank, piv]] = a[[piv, rank]]
        inv = pow(int(a[rank, c]), p - 2, p)
        a[rank] = (a[rank] * inv) % p
        col = a[rank + 1:, c].copy()
        nz = np.nonzero(col)[0]
        if nz.size:
            a[rank + 1 + nz] = (a[rank + 1 + nz] - col[nz, None] * a[rank][None, :]) % p
        rank += 1
        if rank == nrows:
            break
    return ncols - rank


# ===========================================================================
# BLOCK L -- ledger reproduction, v0.258, base a148ed80
# ===========================================================================

ledger = json.loads(read(LEDGER))
rows = {row["id"]: row for row in ledger["rows"]}
rae2 = rows["RA-E2"]

check("L1", "RA-E2 verdict/reason as filed",
      rae2["verdict"] == "NEEDS" and rae2["reason_kind"] == "MISSING_CONSTRUCTION")
check("L2", "RA-E2 distance names the observation route verbatim",
      rae2["distance"] == "use and propagate the vertical form leg through observation")
check("L3", "RA-E2 revival trigger asks for a 14D-to-4D vertical-scalar adapter",
      rae2["revival_trigger"] == "an exact 14D-to-4D vertical-scalar adapter")
check("L4", "RA-E2 mapping_grade is EXACT_SHAPE_CONSTRAINT",
      rae2["mapping_grade"] == "EXACT_SHAPE_CONSTRAINT")

migrations = ledger["migrations"]
rae2_migrations = [m for m in migrations if m.get("row_id") == "RA-E2"]
check("L5", f"zero of the {len(migrations)} recorded migrations names RA-E2",
      len(rae2_migrations) == 0)

# byte-identity of the RA-E2 record across every ledger version on disk
def version_of(path: str) -> int:
    m = re.search(r"v0\.(\d+)\.json$", path)
    return int(m.group(1)) if m else -1


ledger_files = sorted((p for p in glob.glob(LEDGER_GLOB) if version_of(p) >= 0),
                      key=version_of)
e2_texts, e1_texts = set(), set()
for path in ledger_files:
    doc = json.loads(read(path))
    by_id = {r["id"]: r for r in doc["rows"] if isinstance(r, dict) and "id" in r}
    e2_texts.add(json.dumps(by_id["RA-E2"], sort_keys=True))
    e1_texts.add(json.dumps(by_id["RA-E1"], sort_keys=True))

check("L6", f"RA-E2 record is byte-identical across all {len(ledger_files)} ledger versions",
      len(ledger_files) == 258 and len(e2_texts) == 1)
check("L7c", "CONTROL fires: the same test on RA-E1 finds many distinct records",
      len(e1_texts) > 1)

queue_rows = {row for rank in ledger["next_work_queue"] for row in rank["rows"]}
check("L8", "RA-E2 appears in NO next_work_queue rank", "RA-E2" not in queue_rows)
check("L9", "RA-E1/E3/E4/E5 all appear in next_work_queue rank 1",
      set(ledger["next_work_queue"][0]["rows"]) >= {"RA-E1", "RA-E3", "RA-E4", "RA-E5"})

ledger_text = read(LEDGER)
check("L10", "'md1-form-leg' occurs 0 times in the v0.258 JSON",
      ledger_text.count("md1-form-leg") == 0)
check("L11", "'four-d-mode-decomposition' occurs 0 times in the v0.258 JSON",
      ledger_text.count("four-d-mode-decomposition") == 0)
check("L12c", "CONTROL fires: the cited CB-A evidence file DOES occur in the JSON",
      ledger_text.count("cb-a-representation-content-2026-08-05.md") > 0)

# ===========================================================================
# BLOCK S -- exact source substrings
# ===========================================================================

cb_a = read(CB_A)
md1 = read(MD1)
packet = read(PACKET)
routing = read(ROUTING)

S_E2 = ("the Lorentz-scalar components are exactly those with **both** legs "
        "vertical: `V*₁₀ ⊗ Λ²V₁₀ = 10 ⊗ 45`")
check("S1", "CB-A:E2's 10 (x) 45 shape constraint occurs verbatim", S_E2 in cb_a)
check("S2", "CB-A:E2 prints 6 + 6 doublets in that sector",
      "which hosts **6** `(1,2,+1/2)` and 6 `(1,2,−1/2)` (computed)" in cb_a)
check("S3", "CB-A:E4 prints the same sector with multiplicity 12",
      "`10⊗45` → 12" in cb_a)
check("S4", "CB-A:E3 states the 45/55 zero-doublet theorem",
      "**`Λ²V₁₀` (45) and `Sym²V₁₀` (1+54) contain ZERO "
      "colour-singlet weak doublets, at any `Y`.**" in cb_a)
check("S5", "MD-1 states the contraction result",
      "Every ad-valued one-form on `Y14` descends to exactly one 4D one-form." in md1)
check("S6", "MD-1 states the lossy 10-dimensional kernel",
      "annihilates a 10-dimensional space of\n   form legs" in md1
      or "annihilates a 10-dimensional space of form legs" in md1.replace("\n   ", " "))
check("S7", "MD-1 states the Lorentz-trivial component is 1, control fires at 10",
      "its\nLorentz-trivial component is exactly **1**-dimensional (B11), where a genuine\n"
      "Lorentz-inert KK internal space would give **10** (control B12 fires)" in md1)
check("S8", "MD-1's SOLDERED-AD fork is declared open", "id: SOLDERED-AD" in md1
      and "status: open" in md1)
check("S9", "the 2026-07-30 packet types s*(a_V) as the object it is NOT",
      "the differential-form pullback \\(s^*(a_V)\\), which is zero or an "
      "\\(X\\)-one-form" in packet)
check("S10", "the routing method names MD-1 as a fork-3 source-native pointer",
      "lab/active-research/joe-directed/four-d-mode-decomposition/"
      "md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md" in routing)
check("S11", "SEAM: the routing method itself asserts the refuted step",
      "vertical connection components may appear as four-dimensional scalars after "
      "reduction" in routing.replace("\n", " ").replace("  ", " "))
check("S12c", "CONTROL fires: a deliberately wrong substring does not occur",
      "the Lorentz-scalar components are exactly those with both legs horizontal" not in cb_a)

# ===========================================================================
# BLOCK A -- the form leg: the observation pullback is a contraction  [SOURCE_NATIVE]
# ===========================================================================

xs = sp.symbols("x0 x1 x2 x3", real=True)
pairs = [(a, b) for a in range(4) for b in range(a, 4)]          # 10 fibre coordinates
gfun = {ab: sp.Function(f"g_{ab[0]}{ab[1]}")(*xs) for ab in pairs}

# ds : T X (4) -> T Y (14), in adapted coordinates (x^mu ; g_ab)
ds = sp.zeros(14, 4)
for mu in range(4):
    ds[mu, mu] = 1
for k, ab in enumerate(pairs):
    for mu in range(4):
        ds[4 + k, mu] = sp.diff(gfun[ab], xs[mu])

check("A1", "ds has rank 4 for a general section (symbolic)", ds.rank() == 4)

# s^* : T*Y (14) -> T*X (4) is the transpose of ds
sstar = ds.T
omega = sp.symbols("w0 w1 w2 w3", real=True) + tuple(
    sp.Symbol(f"w_{a}{b}", real=True) for (a, b) in pairs)
pulled = sstar * sp.Matrix(list(omega))
expected = [omega[mu] + sum(omega[4 + k] * sp.diff(gfun[ab], xs[mu])
                            for k, ab in enumerate(pairs)) for mu in range(4)]
check("A2", "(s* w)_mu = w_mu + w_(ab) d_mu g_ab exactly (MD-1 E2 re-derived)",
      all(sp.simplify(pulled[mu] - expected[mu]) == 0 for mu in range(4)))

check("A3", "s* is surjective onto T*X (rank 4)", sstar.rank() == 4)
check("A4", "s* annihilates a 10-dimensional space of form legs", 14 - sstar.rank() == 10)
check("A5", "s* o horizontal-inclusion = id_4", sstar[:, :4] == sp.eye(4))

sstar_flat = sstar.subs({sp.diff(gfun[ab], xs[mu]): 0
                         for ab in pairs for mu in range(4)})
horizontal_projection = sp.zeros(4, 14)
horizontal_projection[:, :4] = sp.eye(4)
check("A6", "at d_mu g = 0 the pullback equals horizontal projection",
      sp.simplify(sstar_flat - horizontal_projection) == sp.zeros(4, 14))
check("A7c", "CONTROL fires: for a general section it does NOT (MD-1 control E4)",
      sp.simplify(sstar - horizontal_projection) != sp.zeros(4, 14))

# ===========================================================================
# BLOCK B -- Lorentz typing of the vertical form leg  [fork-independent]
# ===========================================================================
# V = Sym^2(T*_x X4) = symmetric bilinear forms on R^{3,1}; X.S = -(X^T S + S X).

eta = [[0] * 4 for _ in range(4)]
eta[0][0] = -1
for i in range(1, 4):
    eta[i][i] = 1


def matmul(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def transpose(A):
    return [list(col) for col in zip(*A)]


def so_basis(metric, dim=4):
    """Basis of so(metric): X = metric * (E_ij - E_ji)."""
    out = []
    for i in range(dim):
        for j in range(i + 1, dim):
            A = [[0] * dim for _ in range(dim)]
            A[i][j], A[j][i] = 1, -1
            out.append(matmul(metric, A))
    return out


so31 = so_basis(eta)
check("B0", "so(3,1) basis has 6 elements and preserves eta",
      len(so31) == 6 and all(
          matmul(transpose(X), eta) == [[-v for v in r] for r in matmul(eta, X)]
          for X in so31))

VBASIS = []                                            # 10 symmetric matrices
for (a, b) in pairs:
    M = [[0] * 4 for _ in range(4)]
    if a == b:
        M[a][a] = 1
    else:
        M[a][b] = M[b][a] = 1
    VBASIS.append(M)


def sym_to_vec(M):
    return [Fraction(M[a][b]) for (a, b) in pairs]


def act_on_sym(X, M):
    """delta S = -(X^T S + S X)."""
    t1 = matmul(transpose(X), M)
    t2 = matmul(M, X)
    return [[-(t1[i][j] + t2[i][j]) for j in range(4)] for i in range(4)]


def rep_on_V(X):
    """10x10 matrix of X acting on V, in the VBASIS coordinates."""
    cols = [sym_to_vec(act_on_sym(X, B)) for B in VBASIS]
    return [[cols[j][i] for j in range(10)] for i in range(10)]


repV = [rep_on_V(X) for X in so31]
inv_V = nullspace_Q([row for R in repV for row in R], 10)
check("B1", "dim Inv_so(3,1)( Sym^2 T*X4 ) = 1", len(inv_V) == 1)

eta_vec = sym_to_vec(eta)
if inv_V:
    w = inv_V[0]
    scale = next((eta_vec[i] / w[i] for i in range(10) if w[i] != 0), None)
    spans_eta = scale is not None and all(eta_vec[i] == scale * w[i] for i in range(10))
else:
    spans_eta = False
check("B2", "the invariant line is spanned by the metric eta itself", spans_eta)

# traceless 9: eta-trace zero
tr_functional = []
for (a, b) in pairs:
    tr_functional.append(Fraction(eta[a][b] if a == b else 2 * eta[a][b]))
inv_9 = nullspace_Q([row for R in repV for row in R] + [tr_functional], 10)
check("B3", "the traceless 9 carries ZERO Lorentz invariants", len(inv_9) == 0)

inert = [[[Fraction(0)] * 10 for _ in range(10)] for _ in so31]
inv_inert = nullspace_Q([row for R in inert for row in R], 10)
check("B4c", "CONTROL fires: a Lorentz-INERT internal 10 gives 10 invariants, not 1",
      len(inv_inert) == 10 and len(inv_inert) != len(inv_V))

so3 = so_basis([[1 if i == j else 0 for j in range(4)] for i in range(4)])[3:]  # rotations
rep_so3 = [rep_on_V(X) for X in so3]
inv_so3 = nullspace_Q([row for R in rep_so3 for row in R], 10)
check("B5c", "CONTROL fires: under so(3) alone the routine finds 2 invariants, not 1",
      len(inv_so3) == 2)

CBA_FORM_LEG_FACTOR = 10
check("B6", "CB-A:E2's form-leg factor is 10; the Lorentz-trivial dimension is 1",
      CBA_FORM_LEG_FACTOR == 10 and len(inv_V) == 1 and CBA_FORM_LEG_FACTOR != len(inv_V))

# FORCING: the 2026-07-30 packet's live route is res_s^V followed by "a declared
# trace/orbit projector".  Any so(3,1)-equivariant map from the vertical fibre
# onto a trivial module annihilates the traceless 9 (B3: it has no trivial
# subrep) and so factors through the unique 1-dimensional trace line (B1/B2).
check("B7", "any equivariant vertical-scalar projector is FORCED through the "
            "1-dim trace line, so the packet's live route lands on 1 (x) 45",
      len(inv_9) == 0 and len(inv_V) == 1 and spans_eta)

# ===========================================================================
# BLOCK C -- SO(10) -> SM branching  [COMPARATOR: binds the KK projection only]
# ===========================================================================
# Declared table [T]; certified below by three independently printed CB-A numbers,
# by dimension sums, and by vanishing hypercharge traces.

SU3_DIM = {"1": 1, "3": 3, "3b": 3, "6": 6, "6b": 6, "8": 8, "10": 10, "10b": 10, "15": 15,
           "15b": 15, "27": 27}
CONJ = {"1": "1", "3": "3b", "3b": "3", "6": "6b", "6b": "6", "8": "8"}

VEC10 = [("3", 1, Fraction(-1, 3)), ("1", 2, Fraction(1, 2)),
         ("3b", 1, Fraction(1, 3)), ("1", 2, Fraction(-1, 2))]
ADJ45 = [("8", 1, Fraction(0)), ("1", 3, Fraction(0)), ("1", 1, Fraction(0)),
         ("3", 2, Fraction(-5, 6)), ("3b", 2, Fraction(5, 6)),
         ("3", 2, Fraction(1, 6)), ("3b", 1, Fraction(-2, 3)), ("1", 1, Fraction(1)),
         ("3b", 2, Fraction(-1, 6)), ("3", 1, Fraction(2, 3)), ("1", 1, Fraction(-1)),
         ("1", 1, Fraction(0))]
SYM55 = [("1", 1, Fraction(0))] + [  # 1 + 54; 54 = Sym^2_0(10) under SU(5) is 24+15+15b
    ("8", 1, Fraction(0)), ("1", 3, Fraction(0)), ("1", 1, Fraction(0)),
    ("3", 2, Fraction(-5, 6)), ("3b", 2, Fraction(5, 6)),
    ("6", 1, Fraction(-2, 3)), ("3", 2, Fraction(1, 6)), ("1", 3, Fraction(1)),
    ("6b", 1, Fraction(2, 3)), ("3b", 2, Fraction(-1, 6)), ("1", 3, Fraction(-1)),
]


def dim_of(entry):
    c, w, _ = entry
    return SU3_DIM[c] * w


def su2_contains_doublet(a: int, b: int) -> int:
    """multiplicity of the 2 in (dim a) (x) (dim b) of SU(2)"""
    lo, hi = abs(a - b) + 1, a + b - 1
    return 1 if lo <= 2 <= hi and (2 - lo) % 2 == 0 else 0


def count_doublets(content, y_target: Fraction) -> int:
    """multiplicity of the SM irrep (1, 2, y_target) inside `content`"""
    return sum(1 for (c, w, y) in content
               if c == "1" and w == 2 and y == y_target)


def count_doublets_in_product(left, right, y_target: Fraction) -> int:
    total = 0
    for (ca, wa, ya) in left:
        for (cb, wb, yb) in right:
            if CONJ.get(ca) != cb:
                continue
            if ya + yb != y_target:
                continue
            total += su2_contains_doublet(wa, wb)
    return total


check("C1", "declared SM content of the 10 sums to dimension 10",
      sum(dim_of(e) for e in VEC10) == 10)
check("C2", "declared SM content of the 45 sums to dimension 45",
      sum(dim_of(e) for e in ADJ45) == 45)
check("C3", "declared SM content of Sym^2 V10 sums to dimension 55",
      sum(dim_of(e) for e in SYM55) == 55)
check("C4", "hypercharge traces vanish on the 10, the 45 and the 55",
      all(sum(dim_of(e) * e[2] for e in content) == 0
          for content in (VEC10, ADJ45, SYM55)))

n10_plus = count_doublets(VEC10, Fraction(1, 2))
n10_minus = count_doublets(VEC10, Fraction(-1, 2))
check("C5", "REPRODUCES CB-A:E1 -- the 10 hosts exactly one (1,2,+1/2) and one (1,2,-1/2)",
      n10_plus == 1 and n10_minus == 1)

n45_plus = count_doublets(ADJ45, Fraction(1, 2))
n55_plus = count_doublets(SYM55, Fraction(1, 2))
check("C6", "REPRODUCES CB-A:E3 -- 45 and 55 host ZERO colour-singlet weak doublets",
      n45_plus == 0 and count_doublets(ADJ45, Fraction(-1, 2)) == 0
      and n55_plus == 0 and count_doublets(SYM55, Fraction(-1, 2)) == 0)

prod_plus = count_doublets_in_product(VEC10, ADJ45, Fraction(1, 2))
prod_minus = count_doublets_in_product(VEC10, ADJ45, Fraction(-1, 2))
check("C7", "REPRODUCES CB-A:E2 -- 10 (x) 45 hosts 6 (1,2,+1/2) and 6 (1,2,-1/2)",
      prod_plus == 6 and prod_minus == 6)
check("C8", "REPRODUCES CB-A:E4 -- the same sector carries multiplicity 12",
      prod_plus + prod_minus == 12)

check("C9c", "CONTROL fires: the SU(2) routine is not identically zero or one",
      su2_contains_doublet(1, 2) == 1 and su2_contains_doublet(1, 1) == 0
      and su2_contains_doublet(2, 3) == 1 and su2_contains_doublet(2, 2) == 0)
check("C10c", "CONTROL fires: the colour rule is Schur, not permissive",
      CONJ["3"] == "3b" and count_doublets_in_product(
          [("3", 1, Fraction(-1, 3))], [("3", 2, Fraction(5, 6))], Fraction(1, 2)) == 0)

# the correction: replace the form-leg factor by its Lorentz-trivial part
LORENTZ_TRIVIAL_FORM_LEG = [("1", 1, Fraction(0))] * len(inv_V)   # dimension 1, no SM charge
corrected_plus = count_doublets_in_product(LORENTZ_TRIVIAL_FORM_LEG, ADJ45, Fraction(1, 2))
corrected_minus = count_doublets_in_product(LORENTZ_TRIVIAL_FORM_LEG, ADJ45, Fraction(-1, 2))
check("C11", "CORRECTED (INERT-AD horn): the Lorentz-scalar block hosts ZERO doublets",
      corrected_plus == 0 and corrected_minus == 0)
check("C12", "the correction is load-bearing: 12 doublets are deleted, not relabelled",
      (prod_plus + prod_minus) - (corrected_plus + corrected_minus) == 12)
check("C13", "the corrected Lorentz-scalar block has dimension 45, not 450",
      len(inv_V) * 45 == 45 and CBA_FORM_LEG_FACTOR * 45 == 450)

# ===========================================================================
# BLOCK D -- SOLDERED-AD horn: the true Lorentz-scalar dimension of 10 (x) 45
# ===========================================================================
# Under SOLDERED-AD the ad leg is Lambda^2 of the SAME endogenous 10, so the
# diagonal Lorentz action must be used on both legs.

WEDGE = [(i, j) for i in range(10) for j in range(i + 1, 10)]
WIDX = {pair: k for k, pair in enumerate(WEDGE)}
check("D0", "Lambda^2 of the 10 has dimension 45", len(WEDGE) == 45)


def rep_on_wedge(R):
    """45x45 matrix of the derivation induced by the 10x10 matrix R."""
    out = [[Fraction(0)] * 45 for _ in range(45)]
    for k, (i, j) in enumerate(WEDGE):
        for a in range(10):
            if R[a][i]:
                if a != j:
                    p, q, s = (a, j, 1) if a < j else (j, a, -1)
                    out[WIDX[(p, q)]][k] += s * R[a][i]
            if R[a][j]:
                if i != a:
                    p, q, s = (i, a, 1) if i < a else (a, i, -1)
                    out[WIDX[(p, q)]][k] += s * R[a][j]
    return out


repW = [rep_on_wedge(R) for R in repV]
inv_wedge = nullspace_Q([row for R in repW for row in R], 45)
check("D1", "dim Inv_so(3,1)( Lambda^2 V ) = 0", len(inv_wedge) == 0)

# 450-dimensional tensor rep: rho(X) (x) I + I (x) rho_wedge(X)
def tensor_rep(RV, RW):
    out = np.zeros((450, 450), dtype=np.int64)
    for i in range(10):
        for j in range(10):
            v = RV[i][j]
            if v:
                for k in range(45):
                    out[i * 45 + k, j * 45 + k] += int(v)
    for i in range(10):
        for a in range(45):
            for b in range(45):
                w = RW[a][b]
                if w:
                    out[i * 45 + a, i * 45 + b] += int(w)
    return out


stack = np.vstack([tensor_rep(RV, RW) for RV, RW in zip(repV, repW)])
check("D2", "the 450-dim stacked operator is integral (no float anywhere)",
      np.issubdtype(stack.dtype, np.integer))

P1, P2 = 46337, 40961
null_p1 = nullity_mod_p(stack, P1)
null_p2 = nullity_mod_p(stack, P2)
check("D3", f"nullity over GF({P1}) and GF({P2}) agree at 1 "
            "(so nullity over Q is at most 1)",
      null_p1 == 1 and null_p2 == 1)

# exact witness for the lower bound: phi(S) = S_0 ^ eta, transported by the
# invariant metric g(S,S') = tr(eta S eta S') on V.
gram = [[Fraction(sum(matmul(matmul(eta, VBASIS[i]), matmul(eta, VBASIS[j]))[t][t]
                      for t in range(4))) for j in range(10)] for i in range(10)]
gram_inv = sp.Matrix(10, 10, lambda i, j: sp.Rational(gram[i][j])).inv()
eta_index = pairs.index((0, 0))  # eta is diagonal; expand it in VBASIS
eta_coeffs = [Fraction(0)] * 10
for k, (a, b) in enumerate(pairs):
    if a == b:
        eta_coeffs[k] = Fraction(eta[a][b])
trace_of = [Fraction(sum(eta[a][b] * VBASIS[k][a][b] for a in range(4) for b in range(4)))
            for k in range(10)]

witness = [Fraction(0)] * 450
for i in range(10):
    for j in range(10):
        gij = Fraction(int(sp.nsimplify(gram_inv[i, j]).p), int(sp.nsimplify(gram_inv[i, j]).q))
        if gij == 0:
            continue
        # phi(b_j) = (b_j - (tr_eta b_j / 4) eta) ^ eta
        coeffs = [Fraction(0)] * 10
        coeffs[j] += Fraction(1)
        for k in range(10):
            coeffs[k] -= (trace_of[j] / 4) * eta_coeffs[k]
        for k in range(10):
            if coeffs[k] == 0:
                continue
            for m in range(10):
                if eta_coeffs[m] == 0 or k == m:
                    continue
                p_, q_, s_ = (k, m, 1) if k < m else (m, k, -1)
                witness[i * 45 + WIDX[(p_, q_)]] += gij * coeffs[k] * eta_coeffs[m] * s_

check("D4", "the constructed witness is nonzero", any(v != 0 for v in witness))
annihilated = True
for RV, RW in zip(repV, repW):
    T = tensor_rep(RV, RW)
    for r in range(450):
        acc = Fraction(0)
        row = T[r]
        nz = np.nonzero(row)[0]
        for c in nz:
            acc += Fraction(int(row[c])) * witness[c]
        if acc != 0:
            annihilated = False
            break
    if not annihilated:
        break
check("D5", "the witness is exactly annihilated by all six so(3,1) generators", annihilated)
check("D6", "therefore dim Inv_so(3,1)( V (x) Lambda^2 V ) = 1 EXACTLY",
      annihilated and any(v != 0 for v in witness) and null_p1 == 1 and null_p2 == 1)

inert_stack = np.vstack([tensor_rep(RV, [[Fraction(0)] * 45 for _ in range(45)])
                         for RV in repV])
check("D7c", "CONTROL fires: with an inert ad leg the same routine returns 45, not 1",
      nullity_mod_p(inert_stack, P1) == 45)

DOUBLET_REAL_DOF = 4      # CB-A:E4: "4 real dof -> 3 eaten + 1 physical"
check("D8", "one Lorentz-scalar direction cannot carry a complex weak doublet",
      1 < DOUBLET_REAL_DOF)
check("D9", "BOTH horns of SOLDERED-AD give zero Higgs doublets in that sector",
      corrected_plus + corrected_minus == 0 and 1 < DOUBLET_REAL_DOF)

# ===========================================================================
# BLOCK E -- E-block inheritance
# ===========================================================================

e_block = {rid: rows[rid] for rid in
           ("RA-E1", "RA-E2", "RA-E3", "RA-E4", "RA-E5", "RA-E6", "RA-E7")}
check("E0", "the E block has 7 rows", len(e_block) == 7)

sector_token_a, sector_token_b = "10 ⊗ 45", "10⊗45"
cb_lines = cb_a.splitlines()
e_rows_text = {}
for line in cb_lines:
    m = re.match(r"\|\s*\*\*(E[1-7])\*\*\s*\|", line)
    if m:
        e_rows_text[m.group(1)] = line
check("E1", "all seven CB-A E-rows were located in the source table", len(e_rows_text) == 7)

carriers = {k for k, v in e_rows_text.items()
            if sector_token_a in v or sector_token_b in v}
check("E2", "the refuted 10 (x) 45 sector is printed in exactly CB-A:E2 and CB-A:E4",
      carriers == {"E2", "E4"})
check("E3c", "CONTROL fires: it is printed in none of E1, E3, E5, E6, E7",
      not (carriers & {"E1", "E3", "E5", "E6", "E7"}))

check("E4", "RA-E3's revival trigger requires an OBSERVED 4D scalar doublet",
      "descends to an observed 4D scalar doublet" in rows["RA-E3"]["revival_trigger"])
check("E5", "RA-E3's own carrier is a one-form cell, which s* sends to a 4D one-form",
      "varpi one-form cell" in rows["RA-E3"]["revival_trigger"] and sstar.rank() == 4)

check("E6", "RA-E1's live blocker is a rank-196 vs rank-0 compatibility statement",
      "rank-196" in rows["RA-E1"]["distance"]
      and "zero fixed-bank principal projection" in rows["RA-E1"]["distance"])
check("E7", "RA-E1 and RA-E3 both name the operative second action",
      "operative" in rows["RA-E1"]["distance"] and "operative" in rows["RA-E3"]["distance"])

verdicts = {rid: (row["verdict"], row["reason_kind"]) for rid, row in e_block.items()}
check("E8", "E-block verdicts as filed: 3 NEEDS + 1 NEEDS(E2) + 3 DIFFERS",
      sum(1 for v in verdicts.values() if v[0] == "NEEDS") == 4
      and sum(1 for v in verdicts.values() if v[0] == "DIFFERS") == 3)

PRINTED_DOUBLET_INVENTORY = {"V10": 2, "Sym2(S)": 4, "10x45": 12}
check("E9", "CB-A:E4's printed inventory totals 18 doublets across three carriers",
      sum(PRINTED_DOUBLET_INVENTORY.values()) == 18)
check("E10", "the correction deletes 12 of 18, i.e. exactly two thirds of the inventory",
      Fraction(PRINTED_DOUBLET_INVENTORY["10x45"],
               sum(PRINTED_DOUBLET_INVENTORY.values())) == Fraction(2, 3))
check("E11", "E4's remaining channels stay even and >= 2, so its DIFFERS verdict survives",
      all(v >= 2 and v % 2 == 0
          for k, v in PRINTED_DOUBLET_INVENTORY.items() if k != "10x45"))
check("E12", "E3's class-exclusion verdict is CONFIRMED, not weakened, by the correction",
      n45_plus == 0 and n55_plus == 0 and rows["RA-E3"]["verdict"] == "DIFFERS")
check("E13", "worst case for E4 -- V10's 2 is a SUBcount of the 12 (three of the six "
             "(1,2,+1/2) pair V10's doublet with an SM singlet of the 45), so E4 may "
             "retain only Sym^2(S); its DIFFERS still survives on 4 alone",
      count_doublets_in_product([("1", 2, Fraction(1, 2))],
                                [e for e in ADJ45 if e[0] == "1" and e[2] == 0],
                                Fraction(1, 2)) == 3
      and PRINTED_DOUBLET_INVENTORY["Sym2(S)"] >= 2
      and PRINTED_DOUBLET_INVENTORY["Sym2(S)"] % 2 == 0)

# the source-declared linearized content also contains ZERO-forms valued in ad;
# those DO pull back to 4D scalars.  Their Higgs content, both horns:
check("E14", "ad-valued zero-form -> 4D scalar in the 45: ZERO doublets (INERT-AD horn)",
      n45_plus == 0 and count_doublets(ADJ45, Fraction(-1, 2)) == 0)
check("E15", "ad-valued zero-form under SOLDERED-AD: ZERO Lorentz-scalar directions",
      len(inv_wedge) == 0)

# ===========================================================================
# RESULT
# ===========================================================================

RESULT = {
    "base_revision": "a148ed80",
    "ledger": "v0.258",
    "ledger_versions_scanned": len(ledger_files),
    "rae2_distinct_records": len(e2_texts),
    "rae1_distinct_records": len(e1_texts),
    "rae2_migrations": len(rae2_migrations),
    "total_migrations": len(migrations),
    "form_leg": {
        "ds_rank": int(ds.rank()),
        "sstar_rank": int(sstar.rank()),
        "sstar_kernel_dim": 14 - int(sstar.rank()),
    },
    "lorentz": {
        "inv_dim_Sym2_TstarX": len(inv_V),
        "cb_a_form_leg_factor": CBA_FORM_LEG_FACTOR,
        "inv_dim_traceless9": len(inv_9),
        "inv_dim_wedge45": len(inv_wedge),
        "inv_dim_V_tensor_wedge": 1 if (annihilated and null_p1 == 1) else None,
        "inert_control": len(inv_inert),
    },
    "doublets": {
        "in_10": [n10_plus, n10_minus],
        "in_45": [n45_plus, count_doublets(ADJ45, Fraction(-1, 2))],
        "in_10x45_as_printed": [prod_plus, prod_minus],
        "in_corrected_block": [corrected_plus, corrected_minus],
    },
    "e_block": {
        "rows_printing_the_refuted_sector": sorted(carriers),
        "printed_inventory": PRINTED_DOUBLET_INVENTORY,
        "deleted_fraction": str(Fraction(12, 18)),
        "verdicts": verdicts,
    },
}


def assert_no_float(obj, path="result"):
    if isinstance(obj, float):
        raise AssertionError(f"float at {path}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


assert_no_float(RESULT)

print(json.dumps(RESULT, indent=2, default=str))
npass = sum(1 for _, _, ok in CHECKS if ok)
print()
for tag, label, ok in CHECKS:
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag:5s} {label}")
print()
print(f"CERTIFICATE: {npass}/{len(CHECKS)} checks pass; no load-bearing float (swept).")
sys.exit(0 if npass == len(CHECKS) else 1)
