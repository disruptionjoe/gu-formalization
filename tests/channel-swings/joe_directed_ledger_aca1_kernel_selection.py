#!/usr/bin/env python3
r"""LA-2 / AC-A1 : does granting "the source action selects a fermion content in the
rank-10 kernel" discharge the 14D degree-16 local anomaly row, and do AC-A2 / AC-A3
follow?

CHANNEL: conditional_ledger_advancement (Joe-directed).  Base revision a148ed80.
Ledger: lab/process/conditional-physics-ledger-v0.258.json.

WHAT THIS PROBE DECIDES (none of it is asserted, all of it is computed):

  (1) INDEPENDENT RE-VERIFICATION of AC-A7's lattice: rank 5, ker dim 10, Hodge
      symmetry D_p = D_(14-p), and the claimed 7-antisymmetric + 3-symmetric split.
      AC-A7 is the row the whole cascade leans on, so it is re-derived here rather
      than cited.

  (2) THE CASCADE, typed exactly.  Is every gauge-carrying degree-16 row an exact
      rational combination of the five gravitational rows (so A1 => A2 and A1 => A3),
      and is the converse FALSE (so A2 / A3 are strictly weaker than A1 and their
      truth is CONDITIONAL on A1's grant, not independent of it)?

  (3) THE HONEST RISK, decided.  Is the admissible set a distinguished point or a
      family?  The kernel is a rank-10 sublattice of Z^15, hence infinite; the sharp
      question is whether any natural minimality constraint (unit multiplicity, full
      support, non-negativity, bounded height, Hodge symmetry) cuts it to a point.
      Counted exactly, not estimated.

  (4) THE TRIVIAL POINT.  x = 0 -- the fully vectorlike / non-chiral total content
      that CURRENT-STATE.yaml:173 and AC-F2 already record -- lies in the kernel.
      If that is the operative content then AC-A1 needs no selection at all, and the
      row's `distance` field is pointing at the wrong object.

PRIOR ART, not re-claimed.  The matrix, its rank, its kernel dimension, W = 0 as a
derived rather than assumed statement, the necessity-not-sufficiency witness, and the
7 + 3 structure are ALL from
    explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md
and its script tests/anomaly/cb_c_anomaly_rank.py, which this probe IMPORTS rather
than reimplements.  The AGW degree-16 table, the C3 alternating-tower identity and
the 493/2419200 anchor are that artifact's validations and are re-run here as
inherited anchors, marked [T]/[R], never as new results.  What is NEW here is
sections 3, 4 and 5: the exact implication structure of the cascade, and the exact
enumeration of the admissible family under every minimality constraint.

GU-COMPARATOR-ROUTING.  The degree-16 local anomaly condition on GU's native arena
Omega^p(Y^14, /S) is a SOURCE_NATIVE object (the arena is program-native, draft
Sec 9.3).  But per lab/methods/source-native-comparator-routing.md fork 4, anomaly
cancellation is NOT automatically the owner of any selection claim, and per fork 1
the net-chirality functional W computed here is NOT a generation or chirality
verdict.  Nothing below may be promoted into a statement about generations, the
2+1 construction, or content selection.

Exact arithmetic only: fractions.Fraction and Python ints.  No floats anywhere.
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import sys
from fractions import Fraction as F
from math import comb

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CB_C = os.path.join(REPO, "tests", "anomaly", "cb_c_anomaly_rank.py")

_spec = importlib.util.spec_from_file_location("cb_c_anomaly_rank", CB_C)
cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cb)          # module level builds the char-class machinery
                                      # only; main() is __main__-guarded.

CHECKS: list[tuple[str, str, bool]] = []


def chk(tag: str, label: str, ok: bool) -> bool:
    CHECKS.append((tag, label, bool(ok)))
    print(f"  [{tag}] {label}: {'OK' if ok else 'FAIL'}")
    return bool(ok)


def banner(s: str) -> None:
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


# ---------------------------------------------------------------------------
# 0.  Rebuild the two matrices from the imported machinery.
# ---------------------------------------------------------------------------
DGRAV = {p: cb.to_p_basis(cb.AHAT_LAMBDA.get(p, {})) for p in range(15)}
DFULL = {
    p: (cb.to_p_basis(cb.pmul(cb.AHAT_LAMBDA.get(p, {}), cb.CH_S))
        if cb.AHAT_LAMBDA.get(p) else {})
    for p in range(15)
}

GRAV_MONS = sorted(cb.PMON.keys(), key=lambda k: (-k[0], -k[1]))
M_GRAV = [[DGRAV[p].get((mk, 0), F(0)) for p in range(15)] for mk in GRAV_MONS]

FULL_KEYS = sorted({k for p in range(15) for k in DFULL[p]},
                   key=lambda k: (k[1], -k[0][0], -k[0][1]))
M_FULL = [[DFULL[p].get(k, F(0)) for p in range(15)] for k in FULL_KEYS]

# gauge weight of each full-system row: k[1] is the power of Y = y^2, i.e. the number
# of gauge-Casimir powers.  weight 0 rows are the gravitational rows; weight 4 is the
# irreducible order-8 gauge Casimir (row A2); weights 1..3 are the mixed
# gauge-gravitational rows (row A3).
W0_ROWS = [i for i, k in enumerate(FULL_KEYS) if k[1] == 0]
W4_ROWS = [i for i, k in enumerate(FULL_KEYS) if k[1] == 4]
MIX_ROWS = [i for i, k in enumerate(FULL_KEYS) if 1 <= k[1] <= 3]


def apply_rows(M, x):
    """residual vector of the system M against content x; exact Fractions."""
    return [sum(M[i][p] * x[p] for p in range(15)) for i in range(len(M))]


def nnz(v):
    return sum(1 for c in v if c != 0)


def Wof(x):
    return sum(c * comb(14, p) for p, c in enumerate(x))


banner("LA-2 / AC-A1 -- section 1: inherited anchors, re-run (NOT new results)")

# [T] declared table input, [R] reproduction of a filed cb-c result.
AGW = {(4, 0, 0, 0): 381, (2, 1, 0, 0): -904, (0, 2, 0, 0): 208,
       (1, 0, 1, 0): 512, (0, 0, 0, 1): -192}
DEN = 464486400
agw_ok = True
for mk, want in AGW.items():
    got = DGRAV[0].get((mk, 0), F(0)) * DEN
    agw_ok = agw_ok and got.denominator == 1 and int(got) == want
chk("T", "D_0 = [A-hat(TY14)]_16 reproduces the AGW degree-16 table 5/5", agw_ok)

alt = {}
for p in range(15):
    for k, v in DGRAV[p].items():
        alt[k] = alt.get(k, F(0)) + ((-1) ** p) * v
chk("R", "alternating full Dirac-Kahler tower has identically zero degree-16 density",
    not {k: v for k, v in alt.items() if v != 0})

c0_p4 = DGRAV[0].get(((0, 0, 0, 1), 0), F(0)) - DGRAV[1].get(((0, 0, 0, 1), 0), F(0))
chk("R", f"honest C0 p4 coefficient = {c0_p4} (cb-c V3 anchor, per unit dim S)",
    c0_p4 != 0)

_, pivG = cb.rref(M_GRAV)
_, pivF = cb.rref(M_FULL)
chk("R", f"rank(gravitational system) = {len(pivG)} (cb-c: 5)", len(pivG) == 5)
chk("R", f"rank(gravity + gauge system) = {len(pivF)} (cb-c: 5)", len(pivF) == 5)
chk("R", f"dim ker on Z^15 = {15 - len(pivF)} (cb-c: 10)", 15 - len(pivF) == 10)
chk("R", "Hodge symmetry D_p = D_(14-p) holds for all p",
    all(DFULL[p] == DFULL[14 - p] for p in range(15)))

Wrow = [F(comb(14, p)) for p in range(15)]
_, pivW = cb.rref(M_FULL + [Wrow])
chk("R", "net-chirality functional W lies in the row space (W = 0 is DERIVED)",
    len(pivW) == len(pivF))


banner("LA-2 / AC-A1 -- section 2: AC-A7's lattice, RE-DERIVED not cited")

# 2a. the seven antisymmetric directions e_p - e_(14-p), p = 0..6
antisym = []
for p in range(7):
    v = [0] * 15
    v[p] = 1
    v[14 - p] = -1
    antisym.append(v)
    chk("E", f"antisymmetric direction e_{p} - e_{14-p} is in ker (12/12 coefficients zero)",
        nnz(apply_rows(M_FULL, v)) == 0)

_, pivA = cb.rref([[F(c) for c in v] for v in antisym])
chk("E", f"the seven antisymmetric directions are independent (rank {len(pivA)})",
    len(pivA) == 7)

# 2b. the Hodge-symmetric sector: 8 combinations s_p = x_p + x_(14-p), p = 0..7
SYM_BASIS = []
for p in range(8):
    v = [0] * 15
    v[p] += 1
    v[14 - p] += 1
    SYM_BASIS.append(v)          # note: p = 7 gives 2*e_7, a valid generator of the ray
M_SYM = [[sum(M_FULL[i][q] * SYM_BASIS[j][q] for q in range(15)) for j in range(8)]
         for i in range(len(M_FULL))]
_, pivS = cb.rref(M_SYM)
chk("E", f"rank on the 8 Hodge-symmetric combinations = {len(pivS)} (AC-A7 claims 5)",
    len(pivS) == 5)
chk("E", f"symmetric free directions = 8 - {len(pivS)} = {8 - len(pivS)} (AC-A7 claims 3)",
    8 - len(pivS) == 3)
chk("E", f"7 antisymmetric + {8 - len(pivS)} symmetric = {7 + 8 - len(pivS)} = dim ker",
    7 + (8 - len(pivS)) == 15 - len(pivF))

symker, _, _ = cb.kernel_basis(M_SYM, 8)
sym_lifted = []
for sv in symker:
    x = [F(0)] * 15
    for j, c in enumerate(sv):
        for q in range(15):
            x[q] += c * SYM_BASIS[j][q]
    sym_lifted.append(x)
    chk("E", "lifted symmetric kernel direction is in ker of the full system",
        nnz(apply_rows(M_FULL, x)) == 0)

allker = [[F(c) for c in v] for v in antisym] + sym_lifted
_, pivK = cb.rref(allker)
chk("E", f"7 antisymmetric + 3 symmetric span a rank-{len(pivK)} lattice (must be 10)",
    len(pivK) == 10)

print("\n  AC-A7 VERDICT: the rank-10 kernel and its 7 + 3 split are CONFIRMED by an")
print("  independent re-derivation from the imported characteristic-class machinery.")


banner("LA-2 / AC-A1 -- section 3: the cascade AC-A1 => AC-A2 / AC-A3, typed exactly")


def solve_in_rowspace(target, basis):
    """Return exact rational coefficients expressing `target` in span(basis), or None."""
    n = len(target)
    aug = [[basis[j][i] for j in range(len(basis))] + [target[i]] for i in range(n)]
    R, piv = cb.rref(aug)
    if (len(basis)) in piv:                     # augmented column is a pivot -> no solution
        return None
    coef = [F(0)] * len(basis)
    for r, pc in enumerate(piv):
        coef[pc] = R[r][len(basis)]
    for i in range(n):
        if sum(coef[j] * basis[j][i] for j in range(len(basis))) != target[i]:
            return None
    return coef


GRAV_BASIS = [M_FULL[i] for i in W0_ROWS]
chk("E", f"the full system has {len(W0_ROWS)} gauge-weight-0 (gravitational) rows",
    len(W0_ROWS) == 5)

# 3a.  every gauge-carrying row is an exact rational combination of the 5 grav rows.
all_in = True
for i in W4_ROWS + MIX_ROWS:
    coef = solve_in_rowspace(M_FULL[i], GRAV_BASIS)
    lab = "order-8 gauge Casimir (A2)" if i in W4_ROWS else "mixed gauge-grav (A3)"
    ok = coef is not None
    all_in = all_in and ok
    chk("E", f"row {FULL_KEYS[i][0]}*Y^{FULL_KEYS[i][1]} [{lab}] is in span(gravitational rows)",
        ok)
chk("E", "AC-A1 (all 5 gravitational conditions) IMPLIES AC-A2 and AC-A3, exactly",
    all_in)

# 3b.  CONTROL WITH POWER: the gauge rows must be NONZERO functionals, else 3a is vacuous.
for i in W4_ROWS:
    chk("C", f"order-8 gauge row {FULL_KEYS[i][0]}*Y^{FULL_KEYS[i][1]} is a NONZERO functional",
        any(c != 0 for c in M_FULL[i]))
chk("C", f"all {len(MIX_ROWS)} mixed gauge-gravitational rows are nonzero functionals",
    all(any(c != 0 for c in M_FULL[i]) for i in MIX_ROWS))

# 3c.  the CONVERSE FAILS: a content can satisfy A2 (and A3) and still violate A1.
#      Build it explicitly: take the kernel of the A2 row alone and find a member with
#      a nonzero gravitational residual.
a2row = M_FULL[W4_ROWS[0]]
kerA2, _, _ = cb.kernel_basis([a2row], 15)
witness_a2 = None
for v in kerA2:
    if nnz(apply_rows([GRAV_BASIS[k] for k in range(5)], v)) > 0:
        witness_a2 = v
        break
chk("E", "EXISTS a content satisfying the order-8 gauge condition but violating AC-A1",
    witness_a2 is not None)

mix_rows_only = [M_FULL[i] for i in MIX_ROWS]
kerA3, _, _ = cb.kernel_basis(mix_rows_only, 15)
witness_a3 = None
for v in kerA3:
    if nnz(apply_rows(GRAV_BASIS, v)) > 0:
        witness_a3 = v
        break
chk("E", "EXISTS a content satisfying ALL mixed gauge-grav conditions but violating AC-A1",
    witness_a3 is not None)

_, pivA2only = cb.rref([a2row])
_, pivA3only = cb.rref(mix_rows_only)
chk("E", f"rank(A2 row alone) = {len(pivA2only)} < 5 = rank(AC-A1): A2 is STRICTLY WEAKER",
    len(pivA2only) < 5)
chk("E", f"rank(A3 rows alone) = {len(pivA3only)} < 5 = rank(AC-A1): A3 is STRICTLY WEAKER",
    len(pivA3only) < 5)

print("\n  CASCADE VERDICT: AC-A2 and AC-A3 are entailed by AC-A1 and DO NOT entail it.")
print("  Their truth therefore carries exactly AC-A1's grant.  A ledger row that reads")
print("  `SAME / DERIVED` with `distance: none after AC-A1` is carrying an undeclared")
print("  condition -- the honest reason_kind is DERIVED_CONDITIONAL.")


banner("LA-2 / AC-A1 -- section 4: is the selection a POINT or a FAMILY?  (counted)")

# integral kernel basis: free slots p = 5..14, pivots p = 0..4, all entries integral.
kerQ, pivots, frees = cb.kernel_basis(M_FULL, 15)
KB = []
for v in kerQ:
    assert all(c.denominator == 1 for c in v), "kernel basis is not integral"
    KB.append([int(c) for c in v])
chk("E", f"free slots are p = {frees}; pivot slots p = {pivots}", frees == list(range(5, 15)))
chk("E", "the rational kernel basis is INTEGRAL, so it is a Z-basis of ker ∩ Z^15", True)

# x_k = A_k(a) - b_(14-k) for k = 0..4, with a = (x_5..x_9), b = (x_10..x_14).
COEF = [[KB[j][k] for j in range(5)] for k in range(5)]   # COEF[k][j] = contribution of a_(5+j) to x_k


def pivot_vals(a):
    return [sum(COEF[k][j] * a[j] for j in range(5)) for k in range(5)]


def content_from_free(a, b):
    x = [0] * 15
    for k in range(5):
        x[k] = sum(COEF[k][j] * a[j] for j in range(5)) - b[4 - k]
    # KB[5+m] puts -1 in pivot slot (4-m) and +1 in slot (10+m)
    for j in range(5):
        x[5 + j] = a[j]
        x[10 + j] = b[j]
    return x


# sanity: reconstruct each basis vector
recon_ok = True
for j in range(10):
    a = [KB[j][5 + t] for t in range(5)]
    b = [KB[j][10 + t] for t in range(5)]
    recon_ok = recon_ok and content_from_free(a, b) == KB[j]
chk("E", "free-coordinate parametrisation reconstructs all 10 kernel basis vectors", recon_ok)

# which b-slot pairs with which pivot: KB[5+m] has +1 at slot 10+m and -1 at pivot 4-m.
PAIR = {}
for m in range(5):
    row = KB[5 + m]
    pk = [k for k in range(5) if row[k] != 0]
    assert len(pk) == 1 and row[pk[0]] == -1
    PAIR[pk[0]] = m
chk("E", f"each pivot slot pairs with exactly one free slot: {{k: 10+m}} = "
         f"{{{', '.join(f'{k}:{10+v}' for k, v in sorted(PAIR.items()))}}}", len(PAIR) == 5)


def count_bounded(lo, hi):
    """Exact count of x in ker ∩ Z^15 with lo <= x_p <= hi for every p."""
    total = 0
    rng = range(lo, hi + 1)
    for a in itertools.product(rng, repeat=5):
        A = pivot_vals(a)
        prod = 1
        for k in range(5):
            b_lo = max(lo, A[k] - hi)
            b_hi = min(hi, A[k] - lo)
            c = b_hi - b_lo + 1
            if c <= 0:
                prod = 0
                break
            prod *= c
        total += prod
    return total


def enumerate_bounded(lo, hi, cap=100000):
    out = []
    rng = range(lo, hi + 1)
    for a in itertools.product(rng, repeat=5):
        A = pivot_vals(a)
        ranges = []
        for k in range(5):
            b_lo = max(lo, A[k] - hi)
            b_hi = min(hi, A[k] - lo)
            if b_hi < b_lo:
                ranges = None
                break
            ranges.append(range(b_lo, b_hi + 1))
        if ranges is None:
            continue
        for bt in itertools.product(*ranges):
            b = [0] * 5
            for k in range(5):
                b[PAIR[k]] = bt[k]
            out.append(content_from_free(list(a), b))
            if len(out) > cap:
                return out
    return out


zero = [0] * 15
chk("E", "x = 0 (fully vectorlike / non-chiral total content) lies in the kernel",
    nnz(apply_rows(M_FULL, zero)) == 0)

n_unit = count_bounded(-1, 1)
n_full = 0
full_sols = []
for x in enumerate_bounded(-1, 1):
    if all(c in (-1, 1) for c in x):
        n_full += 1
        full_sols.append(x)
n_nonneg = sum(1 for x in enumerate_bounded(0, 1))
print()
chk("E", f"|ker ∩ {{-1,0,1}}^15| = {n_unit}   (unit-multiplicity admissible contents)",
    n_unit > 1)
chk("E", f"|ker ∩ {{-1,+1}}^15| = {n_full}   (FULL-support unit-multiplicity contents)",
    n_full >= 1)
chk("E", f"|ker ∩ {{0,1}}^15| = {n_nonneg}   (non-negative unit-multiplicity contents)",
    n_nonneg >= 1)

growth = [(B, count_bounded(-B, B)) for B in (1, 2, 3, 4)]
print("\n  bounded-height growth of the admissible family:")
for B, n in growth:
    print(f"     |x_p| <= {B}:  {n} admissible integer contents")
chk("E", "the admissible set GROWS with height: it is an infinite family, not a point",
    all(growth[i][1] < growth[i + 1][1] for i in range(len(growth) - 1)))

DK = [(-1) ** p for p in range(15)]
chk("E", "the alternating Dirac-Kahler tower x_p = (-1)^p lies in the kernel",
    nnz(apply_rows(M_FULL, DK)) == 0)
dk_in = any(x == DK for x in full_sols)
chk("E", "the DK tower is among the full-support unit-multiplicity solutions", dk_in)
chk("E", f"full-support unit solutions number {n_full}; unique up to global sign iff 2",
    True)
if n_full == 2:
    print("     ==> the DK tower IS the unique full-support unit-multiplicity content,")
    print("         up to the overall chirality flip x -> -x.")
else:
    print(f"     ==> the DK tower is NOT distinguished: {n_full} full-support unit contents exist.")
    for x in full_sols[:8]:
        print("         " + str(x) + f"   W = {Wof(x)}")

hodge_unit = [x for x in enumerate_bounded(-1, 1) if all(x[p] == x[14 - p] for p in range(15))]
chk("E", f"|ker ∩ {{-1,0,1}}^15 ∩ {{Hodge-symmetric}}| = {len(hodge_unit)}", len(hodge_unit) >= 1)
chk("E", "even Hodge symmetry + unit multiplicity does not cut the family to a point",
    len(hodge_unit) > 1)


banner("LA-2 / AC-A1 -- section 5: controls that must have power")

for pc in (0, 7):
    v = [0] * 15
    v[pc] = 1
    chk("C", f"single chiral slot Omega^{pc} (x) S^+ is anomalous "
             f"({nnz(apply_rows(M_FULL, v))}/12 nonzero, must be > 0)",
        nnz(apply_rows(M_FULL, v)) > 0)

NAMED = {
    "C0  chiral truncation Om^0 S^+ + Om^1 S^-": [1, -1] + [0] * 13,
    "C4  Bianconi-style 0+1+2 alternating": [1, -1, 1] + [0] * 12,
    "C5c chiral 4-slot Hodge-paired": [1, -1] + [0] * 11 + [-1, 1],
    "kerGamma-refined C0 (2,-1)": [2, -1] + [0] * 13,
}
for name, x in NAMED.items():
    r = nnz(apply_rows(M_FULL, x))
    chk("C", f"{name}: W = {Wof(x):+d}, {r}/12 nonzero -> NOT in the kernel", r > 0)

for cut in (13, 12, 11):
    x = [(-1) ** p if p <= cut else 0 for p in range(15)]
    chk("C", f"proper truncation of the alternating tower at p <= {cut} is anomalous "
             f"({nnz(apply_rows(M_FULL, x))}/12 nonzero)",
        nnz(apply_rows(M_FULL, x)) > 0)

wit = [0] * 15
wit[0] = comb(14, 2)
wit[2] = -1
chk("C", f"necessity-not-sufficiency witness 91*e_0 - e_2: W = {Wof(wit)} but "
         f"{nnz(apply_rows(M_FULL, wit))}/12 nonzero",
    Wof(wit) == 0 and nnz(apply_rows(M_FULL, wit)) > 0)

# the discarded MOVE-1 convention would make every channel proportional to W: rank 1.
_, pivWonly = cb.rref([Wrow])
chk("C", f"the all-proportional-to-W convention would give rank {len(pivWonly)}, not 5",
    len(pivWonly) == 1)

# MUTATION TEST 1: perturb one matrix entry; the DK tower must stop cancelling.
M_MUT = [row[:] for row in M_FULL]
M_MUT[0][3] += F(1, DEN)
chk("C", "MUTATION: perturbing one degree-16 entry by 1/464486400 breaks DK-tower cancellation",
    nnz(apply_rows(M_MUT, DK)) > 0)

# MUTATION TEST 2: the mutated system must have a different rank or kernel dimension,
# so the rank-10 answer is not insensitive to the matrix.
_, pivMut = cb.rref(M_MUT)
chk("C", f"MUTATION: perturbed system has rank {len(pivMut)} (kernel dim {15 - len(pivMut)}), "
         f"differing from the true kernel dim 10",
    15 - len(pivMut) != 10)


banner("CERTIFICATE")
npass = sum(1 for _, _, ok in CHECKS if ok)
ntot = len(CHECKS)
kinds = {}
for tag, _, ok in CHECKS:
    kinds.setdefault(tag, [0, 0])
    kinds[tag][1] += 1
    kinds[tag][0] += 1 if ok else 0
for tag in sorted(kinds):
    p, t = kinds[tag]
    name = {"E": "exact result", "C": "control with power",
            "R": "reproduction of a filed cb-c result",
            "T": "declared table input"}[tag]
    print(f"  [{tag}] {name}: {p}/{t}")
print(f"\n  TOTAL: {npass}/{ntot}")
print("  Exact rational arithmetic throughout (fractions.Fraction / int). No floats.")
if npass != ntot:
    for tag, label, ok in CHECKS:
        if not ok:
            print(f"  FAILED [{tag}] {label}")
    sys.exit(1)
print("\n  exit 0")
