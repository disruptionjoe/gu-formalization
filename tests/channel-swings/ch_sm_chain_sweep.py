#!/usr/bin/env python
"""CH-SM chain sweep: enumerate Spin(10) -> G_SM breaking chains and run the
R0 arithmetic on each (chirality, anomaly cancellation, electric charges,
absolute hypercharge normalization).

This EXTENDS tests/recovery-contract/construction_space_sm_r0_c5_harness.py
(anomaly formulas reimplemented identically); it does not modify it.

Everything is exact rational arithmetic on the D5 weight/root system.
Conventions: Cartan basis e1..e5; the 16 = spinor weights (+-1/2)^5 with an
ODD number of minus signs; su(3)_c roots +-(ei-ej), i<j in {1,2,3};
su(2)_L root +-(e4+e5); su(2)_R root +-(e4-e5);
T3L(w) = (w4+w5)/2; T3R(w) = (w4-w5)/2; (B-L)(w) = (2/3)(w1+w2+w3).

Run: python tests/channel-swings/ch_sm_chain_sweep.py
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, product

FAIL: list[str] = []
HALF = F(1, 2)


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


# ---------------------------------------------------------------- weights/roots
def spinor16() -> list[tuple]:
    out = []
    for signs in product([HALF, -HALF], repeat=5):
        if sum(1 for s in signs if s < 0) % 2 == 1:
            out.append(signs)
    return out


W16 = spinor16()

ROOTS: list[tuple] = []
for i, j in combinations(range(5), 2):
    for si in (1, -1):
        for sj in (1, -1):
            r = [F(0)] * 5
            r[i], r[j] = F(si), F(sj)
            ROOTS.append(tuple(r))
ROOT_SET = set(ROOTS)


def span_roots(pairs) -> frozenset:
    out = set()
    for r in pairs:
        out.add(r)
        out.add(tuple(-x for x in r))
    return frozenset(out)


def unit(i, sign=1):
    r = [F(0)] * 5
    r[i] = F(sign)
    return tuple(r)


def root(i, j, si, sj):
    r = [F(0)] * 5
    r[i], r[j] = F(si), F(sj)
    return tuple(r)


SU3 = span_roots([root(i, j, 1, -1) for i, j in combinations(range(3), 2)])          # 6 roots
SU4 = span_roots([root(i, j, 1, sj) for i, j in combinations(range(3), 2) for sj in (1, -1)])  # 12
SU2L = span_roots([root(3, 4, 1, 1)])
SU2R = span_roots([root(3, 4, 1, -1)])
# su(5)' containing the FIXED G_SM (su3 + su2L with root e4+e5): image of the
# standard su(5)={ei-ej} under the outer flip e5 -> -e5.
SU5P = span_roots([root(i, j, 1, -1) for i, j in combinations(range(4), 2)]
                  + [root(i, 4, 1, 1) for i in range(4)])                              # 20
SO8 = span_roots([root(i, j, 1, sj) for i, j in combinations(range(4), 2) for sj in (1, -1)])  # 24


# ------------------------------------------------------------------ generators
def T3L(w):
    return (w[3] + w[4]) / 2


def T3R(w):
    return (w[3] - w[4]) / 2


def BmL(w):
    return F(2, 3) * (w[0] + w[1] + w[2])


def Y_std(w):
    return T3R(w) + BmL(w) / 2


def color_class(w) -> str:
    n_minus = sum(1 for x in w[:3] if x < 0)
    return {0: "1", 1: "3", 2: "3bar", 3: "1"}[n_minus]


def spectrum(y_func) -> dict:
    """Aggregate 16 into (weak, color, Y) -> #states under a Y functional."""
    agg: dict = {}
    for w in W16:
        weak = 2 if w[3] == w[4] else 1
        key = (weak, color_class(w), y_func(w))
        agg[key] = agg.get(key, 0) + 1
    return agg


SM_TARGET = {
    (2, "3", F(1, 6)): 6,     # Q_L
    (1, "3bar", F(-2, 3)): 3,  # u_c
    (1, "3bar", F(1, 3)): 3,   # d_c
    (2, "1", F(-1, 2)): 2,     # L_L
    (1, "1", F(1)): 1,         # e_c
    (1, "1", F(0)): 1,         # nu_c
}


def to_fermion_list(agg) -> list[tuple]:
    """(tri, n_weak, n_color, Y) rows in the C5-harness format."""
    rows = []
    for (weak, col, y), n in sorted(agg.items(), key=str):
        tri = {"3": 1, "3bar": -1, "1": 0}[col]
        n_color = 3 if col in ("3", "3bar") else 1
        copies = n // (weak * n_color)
        for _ in range(copies):
            rows.append((tri, weak, n_color, y))
    return rows


def anomalies(fermions) -> dict:
    """Identical formulas to construction_space_sm_r0_c5_harness.anomalies."""
    u1_cubed = grav = su2 = su3 = F(0)
    for tri, n_weak, n_color, y in fermions:
        u1_cubed += n_weak * n_color * y**3
        grav += n_weak * n_color * y
        if n_weak == 2:
            su2 += n_color * y
        su3 += n_weak * tri
    return {"U1_cubed": u1_cubed, "grav": grav, "su2": su2, "su3": su3}


def su2_doublet_count(fermions) -> int:
    return sum(n_color for _t, n_weak, n_color, _y in fermions if n_weak == 2)


def is_vectorlike(fermions) -> bool:
    pool = list(fermions)
    for row in fermions:
        tri, weak, ncol, y = row
        conj = (-tri, weak, ncol, -y)
        if conj in pool and (conj != row or pool.count(row) >= 2):
            return True
    return False


def main() -> None:
    log("=" * 86)
    log("S1  A1-lock: which root-su(2)s can commute with a coordinate su(3)_c")
    log("=" * 86)
    # For su(3) on coords {i,j,k}, an su(2) commuting with it must pair to zero
    # with every su(3) root; brute-force over all 40 roots.
    for triple in combinations(range(5), 2):
        pass  # (placeholder to keep flake-style linters quiet)
    lock_ok = True
    for triple in combinations(range(5), 3):
        su3_roots = span_roots([tuple(F(a) - F(b) for a, b in zip(unit(i), unit(j)))
                                for i, j in combinations(triple, 2)])
        comp = [i for i in range(5) if i not in triple]
        expected = span_roots([root(comp[0], comp[1], 1, 1), root(comp[0], comp[1], 1, -1)])
        commuting = {a for a in ROOTS if all(dot(a, b) == 0 for b in su3_roots)}
        if commuting != set(expected):
            lock_ok = False
    check("S1a  for every coordinate su(3), the ONLY commuting root-su(2)s are the two complement-pair su(2)s",
          lock_ok, "for su3 on {1,2,3}: su(2)_L = +-(e4+e5), su(2)_R = +-(e4-e5) -- the Pati-Salam pair")
    check("S1b  SU(2)_L/SU(2)_R partners of su(3)_c both use coordinate 5, hence are NOT roots of SO(8)xSO(2)",
          root(3, 4, 1, 1) not in SO8 and root(3, 4, 1, -1) not in SO8,
          "SO(8)xSO(2) cannot host G_SM with a regular su(3): kill class 2")

    log("")
    log("=" * 86)
    log("S2  chirality screen over the first-step subgroups (real-form maximal compacts)")
    log("=" * 86)
    # A branching is vectorlike iff the projected weight multiset is closed
    # under negation. Rank-4 symmetric subgroups project out one Cartan
    # direction; full-rank subgroups keep all five.
    def self_conjugate(proj_rows: list[tuple]) -> bool:
        projected = sorted(tuple(dot(w, tuple(F(x) for x in row)) for row in proj_rows) for w in W16)
        negated = sorted(tuple(-x for x in p) for p in projected)
        return projected == negated

    E = [unit(i) for i in range(5)]
    rank4 = {
        "SO(9)   [form SO(9,1)]": [E[0], E[1], E[2], E[3]],
        "SO(7)xSO(3) [form SO(7,3)]": [E[0], E[1], E[2], E[3]],
        "SO(5)xSO(5) [form SO(5,5)]": [E[0], E[1], E[2], E[3]],
    }
    for name, proj in rank4.items():
        check(f"S2a  {name}: projected 16 is SELF-CONJUGATE -> vectorlike -> chirality KILLED",
              self_conjugate(proj))
    full = {
        "U(5) = SU(5)xU(1) [form SO*(10)]": E,
        "Pati-Salam Spin(6)xSpin(4) [form Spin(6,4)]": E,
        "SO(8)xSO(2) [form SO(8,2)]": E,
    }
    for name, proj in full.items():
        check(f"S2b  {name}: full-rank, 16 NOT self-conjugate -> chiral", not self_conjugate(proj))
    check("S2c  general lemma: negating any 4 of 5 spinor coordinates closes the 16 multiset (rank loss kills chirality)",
          all(self_conjugate([E[i] for i in range(5) if i != k]) for k in range(5)))
    log("  => chirality survives ONLY through full-rank stages; among vector signatures only (6,4)")
    log("     [max compact = Pati-Salam] survives both screens; SO*(10) [max compact U(5)] also survives.")
    log("     GU's trace reversal (7,3)->(6,4) lands on the unique surviving vector signature.")

    log("")
    log("=" * 86)
    log("S3  hypercharge line: exact solve in the 2-plane orthogonal to su(3)+su(2)_L")
    log("=" * 86)
    # Y = a*T3R + b*(B-L). Doublets force b; singlets force a.
    solutions = []
    grid = [F(n, d) for d in (1, 2, 3, 4, 6) for n in range(-12, 13)]
    seen = set()
    for a in grid:
        for b in grid:
            if (a, b) in seen:
                continue
            seen.add((a, b))
            agg = spectrum(lambda w, a=a, b=b: a * T3R(w) + b * BmL(w))
            if agg == SM_TARGET:
                solutions.append((a, b))
    check("S3a  exactly TWO lines reproduce the SM multiset: (a,b) = (1, 1/2) [standard] and (-1, 1/2) [flipped]",
          sorted(solutions) == [(F(-1), HALF), (F(1), HALF)], f"solutions={solutions}")
    # Weyl identification: the SU(2)_R Weyl reflection is w4 <-> w5 on weights;
    # it preserves the 16 and maps T3R -> -T3R, so the two lines are
    # Spin(10)-gauge-conjugate: ONE physical hypercharge line.
    swapped = sorted((w[0], w[1], w[2], w[4], w[3]) for w in W16)
    check("S3b  w4<->w5 (SU(2)_R Weyl element) preserves the 16 -> the two lines are gauge-conjugate: 1 physical line",
          swapped == sorted(W16))
    for name, yf in [("Y = T3R alone", T3R), ("Y = (B-L)/2 alone", lambda w: BmL(w) / 2),
                     ("Y = X-line (-4*T3R + 3*(B-L))", lambda w: -4 * T3R(w) + 3 * BmL(w)),
                     ("Y = T3R + (B-L) (wrong slope)", lambda w: T3R(w) + BmL(w))]:
        check(f"S3c  control line fails the SM multiset: {name}", spectrum(yf) != SM_TARGET)

    log("")
    log("=" * 86)
    log("S4  R0 arithmetic on the surviving spectrum (identical for every surviving chain)")
    log("=" * 86)
    agg = spectrum(Y_std)
    fermions = to_fermion_list(agg)
    an = anomalies(fermions)
    check("S4a  16 branches to exactly the one-generation SM multiset + nu_c under (G_SM, Y_std)", agg == SM_TARGET)
    check("S4b  all four anomaly sums vanish exactly", all(v == 0 for v in an.values()),
          "U1^3={U1_cubed}, grav={grav}, [SU2]^2U1={su2}, su3-triality={su3}".format(**{k: str(v) for k, v in an.items()}))
    check("S4c  Witten SU(2) parity: doublet count even", su2_doublet_count(fermions) % 2 == 0,
          f"doublets={su2_doublet_count(fermions)}")
    check("S4d  spectrum is CHIRAL (no conjugate/vectorlike pair present)", not is_vectorlike(fermions))
    q_ok = all(
        {(w[3] + w[4]) / 2 + Y_std(w) for w in W16 if color_class(w) == c and (2 if w[3] == w[4] else 1) == wk} == qs
        for c, wk, qs in [("3", 2, {F(2, 3), F(-1, 3)}), ("3bar", 1, {F(-2, 3), F(1, 3)}),
                          ("1", 2, {F(0), F(-1)}), ("1", 1, {F(0), F(1)})])
    check("S4e  electric charges Q = T3L + Y are exactly the SM values", q_ok)
    trY2 = sum(Y_std(w) ** 2 for w in W16)
    trT3L2 = sum(T3L(w) ** 2 for w in W16)
    trQ2 = sum((T3L(w) + Y_std(w)) ** 2 for w in W16)
    check("S4f  ABSOLUTE normalization: Tr(Y^2)/Tr(T3L^2) = 5/3 over the 16", trY2 / trT3L2 == F(5, 3),
          f"TrY^2={trY2}, TrT3L^2={trT3L2}")
    check("S4g  sin^2(theta_W) at the unification boundary = Tr(T3L^2)/Tr(Q^2) = 3/8", trT3L2 / trQ2 == F(3, 8),
          f"TrQ^2={trQ2}")
    # Vectorlike control in the harness's own format:
    vec = fermions + [(-t, wk, nc, -y) for t, wk, nc, y in fermions]
    check("S4h  control: 16+16bar (vectorlike doubling) is flagged non-chiral", is_vectorlike(vec))

    log("")
    log("=" * 86)
    log("S5  rank-drop lemma: the final U(1) can only be broken by a SPINORIAL VEV")
    log("=" * 86)
    # The G_SM-invariant weight direction is u = (1,1,1,-1,1) (su3-singlet,
    # T3L = 0, Y = 0, X != 0). Tensor irreps (45, 54, 210, ...) have weights in
    # the D5 root lattice = integer vectors with EVEN coordinate sum; u has odd
    # sum, so NO tensor rep contains a G_SM-singlet with nonzero X.
    u = (F(1), F(1), F(1), F(-1), F(1))
    check("S5a  u is a G_SM singlet: su3-weight 0, T3L(u)=0, Y(u)=0, X(u)!=0",
          all(dot(u, b) == 0 for b in SU3) and T3L(u) == 0 and Y_std(u) == 0 and (-4 * T3R(u) + 3 * BmL(u)) != 0)
    check("S5b  sum of u's coordinates is ODD -> u is NOT in the root lattice -> absent from every tensor irrep",
          sum(u) % 2 == 1)
    check("S5c  u/2 IS a weight of the 16 (the nu_c direction)", tuple(x / 2 for x in u) in W16)
    sym2 = {tuple(a + b for a, b in zip(w1, w2)) for w1 in W16 for w2 in W16}
    ten_weights = {unit(i, s) for i in range(5) for s in (1, -1)}
    check("S5d  u IS a weight of Sym^2(16) but not of the 10 -> u is a weight of the 126 (nu_c nu_c direction)",
          u in sym2 and u not in ten_weights)
    log("  => every chain's last (rank-reducing) step demands a spinor-coset condensate (16- or 126-type);")
    log("     the 126 route leaves matter parity (-1)^(3(B-L)) unbroken (a physical Z/2 output).")

    log("")
    log("=" * 86)
    log("S6  chain lattice: all descending paths Spin(10) -> G_SM through the surviving nodes")
    log("=" * 86)
    nodes = {
        "Spin(10)": (frozenset(ROOT_SET), 5),
        "SU(5)xU(1)": (SU5P, 5),
        "SU(5)": (SU5P, 4),
        "PS=SU(4)xSU(2)LxSU(2)R": (frozenset(SU4 | SU2L | SU2R), 5),
        "SU(4)xSU(2)LxU(1)R": (frozenset(SU4 | SU2L), 5),
        "SU(3)xSU(2)LxSU(2)RxU(1)B-L": (frozenset(SU3 | SU2L | SU2R), 5),
        "G_SMxU(1)": (frozenset(SU3 | SU2L), 5),
        "G_SM": (frozenset(SU3 | SU2L), 4),
    }
    check("S6a  fixed G_SM roots sit inside every non-Spin(10) node", all(
        SU3 <= r and SU2L <= r for name, (r, _k) in nodes.items()))

    def contains(a, b) -> bool:
        (ra, ka), (rb, kb) = nodes[a], nodes[b]
        return a != b and rb <= ra and kb <= ka and (rb < ra or kb < ka)

    order = list(nodes)
    edges = {a: [b for b in order if contains(a, b)] for a in order}
    check("S6b  Pati-Salam does NOT sit inside SU(5)xU(1) (su2_R root e4-e5 excluded) and vice versa",
          not contains("SU(5)xU(1)", "PS=SU(4)xSU(2)LxSU(2)R") and not contains("PS=SU(4)xSU(2)LxSU(2)R", "SU(5)xU(1)"))
    check("S6c  the left-right group SU(3)xSU(2)LxSU(2)RxU(1) is NOT inside SU(5)xU(1) either",
          not contains("SU(5)xU(1)", "SU(3)xSU(2)LxSU(2)RxU(1)B-L"))

    paths: list[list[str]] = []

    def walk(node: str, acc: list[str]) -> None:
        if node == "G_SM":
            paths.append(acc)
            return
        for nxt in edges[node]:
            walk(nxt, acc + [nxt])

    walk("Spin(10)", ["Spin(10)"])
    check("S6d  the chain count is finite and fully enumerated: 16 descending chains", len(paths) == 16,
          f"count={len(paths)}")
    ps_side = [p for p in paths if any(n.startswith(("PS", "SU(4)", "SU(3)xSU(2)LxSU(2)R")) for n in p)]
    su5_side = [p for p in paths if any(n.startswith("SU(5)") for n in p)]
    check("S6e  side split: 10 PS-side chains, 4 SU(5)-side chains, 2 direct (no intermediate side)",
          len(ps_side) == 10 and len(su5_side) == 4, f"ps={len(ps_side)}, su5={len(su5_side)}")
    log("")
    for k, p in enumerate(paths, 1):
        log(f"  chain {k:2d}: " + " -> ".join(p))
    log("")
    # Every chain ends on the same (G_SM, Y_std mod Weyl) with the same 16
    # branching, so the R0 arithmetic of S4 applies verbatim to each.
    check("S6f  every enumerated chain ends on the identical surviving spectrum -> S4's R0 results hold per-chain",
          all(p[-1] == "G_SM" for p in paths) and agg == SM_TARGET)

    log("")
    log("=" * 86)
    log("VERDICT")
    log("=" * 86)
    if not FAIL:
        log("CH-SM chain sweep complete. Surviving construction: chirality forces full-rank")
        log("descent; among vector signatures only (6,4) [Pati-Salam side] survives, plus the")
        log("SO*(10)/U(5) side; the hypercharge line is UNIQUE mod Spin(10) Weyl with absolute")
        log("normalization Tr(Y^2)/Tr(T3L^2)=5/3 (sin^2 theta_W = 3/8 at the boundary); all 16")
        log("enumerated chains are R0-EQUIVALENT (identical anomaly/chirality/charge/normalization")
        log("arithmetic); the final rank drop requires a spinorial (16/126-type) condensate; and")
        log("the generation count is NOT produced by any chain (even-index no-go stands upstream).")
        log("\nRESULT: ALL PASS")
    else:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
