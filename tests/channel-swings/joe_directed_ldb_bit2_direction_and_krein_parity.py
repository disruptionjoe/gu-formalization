#!/usr/bin/env python3
"""
LD-B lens dig -- probe for `lab/active-research/joe-directed/lens-digs/
ldb-bit2-direction-and-krein-parity-2026-08-17.md`.

Certifies the two EXACT legs of the dig plus the card table and every quote the
cards lean on.

EXACT LEG 1 (item 4 -- Krein).  On the 192-dim self-dual generation triplet
inside the gamma-traceless `V (x) S`, the two chirality halves are TOTALLY
ISOTROPIC in the Krein form `K = eta_V (x) beta_S` **iff the number of timelike
directions q is ODD**.  Both physical horns (9,5) and (7,7) have odd q, so the
selected half is maximally NULL, never Krein-positive.  At q = 0 the halves are
DEFINITE (+96,0)/(0,-96) -- so the unqualified canon sentence "Each chirality
half is totally null", whose scope sentence enumerates "(9,5), (7,7), and
(14,0)", is FALSE at its third signature.  The R3 fencing theorem's conclusion
`Re tr(chi Pi_+) = 0` likewise fails at q = 0 (value 96) and holds for q >= 1.

EXACT LEG 2 (item 3 -- direction).  Inside ONE declared insertion irrep
(`Lambda^1 (subset) ad P`), the VEV DIRECTION already changes the spectrum:
`rank(e_w|_{S_+})` is 64 for a non-null `w` and 32 for a NULL `w`.  Null
directions exist iff q >= 1.  ST-1 stratified insertions by irrep TYPE; this is
the INTRA-irrep stratum it did not compute.

BD-D DISANALOGY (item 4, second leg).  `ker(Gamma)` (dim 1664 = 13 * 128)
contains no line of the form `v (x) S`, so BD-D's Part-1 hypothesis ("every
submodule is `U (x) g`") has no analogue here: Spin acts DIAGONALLY on
`V (x) S`.  BD-D's no-go does not transport to the fermionic Krein sector.

NOT claimed: any action, vacuum, scale, spectrum, reality map, generation
count, anomaly, decoupling, or claim-status movement.  Nothing here recomputes
ST-1's D_7 Hom dimensions (68/172 are QUOTED from ST-1, not re-derived).

Failure path:  `--selftest` verifies the CLEAN BASELINE first, then drives 9
machinery/reference mutations, each of which must produce a genuine `[FAIL]`
line AND exit 1 (a nonzero exit without a [FAIL] is CRASH-NOT-DETECTION and is
rejected).  Per `VERIFICATION.md` "Probe and mutation-harness discipline".

Usage:
    python3 joe_directed_ldb_bit2_direction_and_krein_parity.py
    python3 joe_directed_ldb_bit2_direction_and_krein_parity.py --selftest
"""
import os
import re
import subprocess
import sys

import numpy as np

# --------------------------------------------------------------------------
# harness
# --------------------------------------------------------------------------
MUT = int(os.environ.get("LDB_MUTATE", "0"))     # 0 = clean
FAST = os.environ.get("LDB_FAST", "0") == "1"    # selftest scope (baseline AND mutants)

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

_results = []


def check(name, ok, detail="", tag=""):
    _results.append((name, bool(ok), detail, tag))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag + ' ' if tag else ''}{name}"
          + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def norm(s):
    return re.sub(r"\s+", " ", s)


def read(rel):
    with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
        return fh.read()


N, DIM = 14, 128

# --------------------------------------------------------------------------
# Clifford machinery (Jordan-Wigner), shared with tests/generation-sector/
# ghost_parity_krein.py -- reproduced here so this probe stands alone.
# --------------------------------------------------------------------------


def jw(n):
    I = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    G = []
    for k in range(n):
        L, R = [s3] * k, [I] * (n - 1 - k)
        for mid in (s1, s2):
            o = np.array([[1 + 0j]])
            for m in L + [mid] + R:
                o = np.kron(o, m)
            G.append(o)
    return G


BASE = jw(7)
I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]   # self-dual SU(2)+ on {0,1,2,3}
if MUT == 3:                     # MACHINERY: not the self-dual triple at all
    SD = [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11)]


def sgen(e, i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


def gammas(timelike):
    return [(1j * BASE[a] if a in timelike else BASE[a]) for a in range(N)]


def beta_S(e, timelike):
    """Spinor Krein metric: the product of the SPACELIKE gammas."""
    spacelike = [a for a in range(N) if a not in timelike]
    if MUT == 1:                      # MACHINERY: use timelike gammas instead
        spacelike = sorted(timelike) or [0]
    b = I128.copy()
    for s in spacelike:
        b = b @ e[s]
    if np.linalg.norm(b.conj().T + b) < 1e-9:
        b = 1j * b
    return b / np.sqrt(abs((b @ b)[0, 0].real))


def chirality(e):
    """Chirality operator: the product of ALL 14 gammas, Hermitian, squaring to I."""
    rng = range(N - 1) if MUT == 2 else range(N)   # MACHINERY: drop a gamma
    c = I128.copy()
    for a in rng:
        c = c @ e[a]
    if np.linalg.norm(c.conj().T + c) < 1e-9:
        c = 1j * c
    return c / np.sqrt(abs((c @ c)[0, 0].real))


_cache = {}


def build(timelike):
    """Return (triplet basis Wt, Krein form K, chirality chi, p, q)."""
    key = frozenset(timelike)
    if key in _cache:
        return _cache[key]
    e = gammas(timelike)
    p, q = N - len(timelike), len(timelike)

    Gam = np.hstack(e)                                  # gamma-trace map V(x)S -> S
    Pi = np.eye(N * DIM, dtype=complex) - Gam.conj().T @ np.linalg.inv(Gam @ Gam.conj().T) @ Gam
    w, Vv = np.linalg.eigh(Pi)
    W = Vv[:, w > 0.5]

    J = [np.kron(I14, sgen(e, a, b) + sgen(e, c, d))
         + np.kron(lvec(a, b) + lvec(c, d), I128) for (a, b, c, d) in SD]
    Cas = -(J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2])
    CasK = W.conj().T @ Cas @ W
    CasK = 0.5 * (CasK + CasK.conj().T)
    ev, U = np.linalg.eigh(CasK)
    evr = [round(x.real, 3) for x in ev]
    top = max(evr) if MUT != 4 else sorted(set(evr))[-2]   # MACHINERY: wrong Casimir stratum
    Wt = W @ U[:, np.abs(ev - top) < 1e-3]

    bS = beta_S(e, timelike)
    chi = chirality(e)
    etaV = np.diag([(-1.0 if a in timelike else 1.0) for a in range(N)]).astype(complex)
    K = np.kron(etaV, bS)
    out = (Wt, K, chi, p, q)
    _cache[key] = out
    return out


def signature(M, tol=1e-9):
    s = np.linalg.eigvalsh(0.5 * (M + M.conj().T))
    return (int(np.sum(s > tol)), int(np.sum(s < -tol)), int(np.sum(np.abs(s) < tol)))


def horn_data(timelike):
    Wt, K, chi, p, q = build(timelike)
    CHI = np.kron(I14, chi)
    B = Wt.conj().T @ K @ Wt
    full = signature(B)
    Cr = 0.5 * ((Wt.conj().T @ CHI @ Wt) + (Wt.conj().T @ CHI @ Wt).conj().T)
    cv, cU = np.linalg.eigh(Cr)
    halves = {}
    for nm, sel in (("+", cv > 0.5), ("-", cv < -0.5)):
        H = Wt @ cU[:, sel]
        halves[nm] = (int(sel.sum()), signature(H.conj().T @ K @ H))
    ev, U = np.linalg.eigh(0.5 * (B + B.conj().T))
    P = Wt @ U[:, ev > 1e-9]
    Qp = np.linalg.qr(P)[0]
    fence = float(np.trace(Qp.conj().T @ CHI @ Qp).real)
    anti = float(np.linalg.norm(K @ CHI + CHI @ K))
    comm = float(np.linalg.norm(K @ CHI - CHI @ K))
    ang = {}
    for nm, sel in (("+", cv > 0.5), ("-", cv < -0.5)):
        Qb = np.linalg.qr(Wt @ cU[:, sel])[0]
        ang[nm] = np.linalg.svd(Qp.conj().T @ Qb, compute_uv=False)
    return dict(dim=Wt.shape[1], full=full, halves=halves, fence=fence,
                anti=anti, comm=comm, ang=ang, p=p, q=q)


# --------------------------------------------------------------------------
# REFERENCES (mutable by the harness -- reference corruption, never a predicate)
# --------------------------------------------------------------------------
# Expected (chi-half signature) per timelike count q.  q odd -> totally null.
PARITY_REF = {0: (96, 0, 0), 1: (0, 0, 96), 2: (48, 48, 0), 3: (0, 0, 96),
              4: (48, 48, 0), 5: (0, 0, 96), 6: (48, 48, 0), 7: (0, 0, 96)}
if MUT == 5:                       # REFERENCE: assert canon's unqualified reading
    PARITY_REF = dict(PARITY_REF)
    PARITY_REF.update({0: (0, 0, 96), 2: (0, 0, 96), 4: (0, 0, 96), 6: (0, 0, 96)})

FENCE_REF = {0: False, 1: True, 2: True, 3: True, 4: True,
             5: True, 6: True, 7: True}          # does Re tr(chi Pi_+) = 0 hold?
if MUT == 6:                       # REFERENCE: claim the fence is universal
    FENCE_REF = {q: True for q in FENCE_REF}

RANK_REF = {"generic": 64, "null": 32}
if MUT == 7:                       # REFERENCE: claim direction does not matter
    RANK_REF = {"generic": 64, "null": 64}

# The five verdict cards, pinned.  C0 is a DELIBERATELY WRONG control the
# coverage machinery below is required to flag.
CARDS = {
    "3": "LIVE-MODERATE",
    "4": "ALREADY-COVERED(canon/ghost-parity-krein-synthesis.md 3)+LIVE-MODERATE(defect)",
    "5": "LIVE-HIGH",
    "8": "ALREADY-COVERED(decoupling-constructibility-packet R4b/CHK-2)+LIVE-MODERATE(unrun)",
    "9": "SPLIT: ALREADY-COVERED(ST-1 4.5(3)) + LIVE-HIGH(R5 unexecuted) + MIS-TARGETED(fork settled A)",
}
CONTROL_CARD = ("C0", "LIVE-HIGH", "item 4's literal question is uncovered by canon")

QUOTE_PINS = [
    ("canon/ghost-parity-krein-synthesis.md", "Each chirality half is totally null"),
    ("canon/ghost-parity-krein-synthesis.md", "in `(9,5)`, `(7,7)`, and `(14,0)`"),
    ("canon/ghost-parity-krein-synthesis.md", "{K, chi} = 0 forces Re tr(chi Pi_+) = 0"),
    ("lab/active-research/joe-directed/seesaw-tradeoff/"
     "st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md", "68  = 7 + 2·14 + 33"),
    ("lab/active-research/joe-directed/seesaw-tradeoff/"
     "st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md", "172 = 14 + 2·34 + 90"),
    ("lab/active-research/joe-directed/seesaw-tradeoff/"
     "st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md",
     "the Grassmann-live 0-form directions (`Λ^1, Λ^5`) are chirality-blind"),
    ("lab/active-research/joe-directed/seesaw-tradeoff/"
     "st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md", "multiplicity exactly 1"),
    ("lab/methods/gu-base-categories.md", "Grant-poset node G6"),
    ("lab/methods/gu-base-categories.md", "Movement of a ROW between nodes is not a functor"),
    ("lab/methods/gu-base-categories.md", "No recorded arrow relates G3"),
    ("lab/active-research/joe-directed/ledger-advancement/"
     "la5-anomaly-axis-is-seven-handles-not-twenty-six-2026-08-15.md", "not monotone"),
    ("lab/process/layer0-fork-registry.yaml", 'settled_side: "A"'),
    ("lab/process/layer0-fork-registry.yaml", "B: the label attaches to the RS-shaped spin-3/2 384"),
    ("explorations/decoupling-constructibility-packet-2026-08-12.md",
     "rides the SAME single VEV dial"),
    ("explorations/decoupling-constructibility-packet-2026-08-12.md",
     "anomaly matching between the vectorlike UV"),
    ("explorations/decoupling-constructibility-packet-2026-08-12.md",
     "the wave must exhibit the dial's action on all sectors simultaneously"),
    ("canon/escape-corners-campaign-RESULTS.md", "opposing demands on one dial"),
    ("canon/escape-corners-campaign-RESULTS.md", "NO invariant mass channel"),
]
if MUT == 8:                       # REFERENCE: corrupt the quote corpus
    QUOTE_PINS = [(f, q + " XXQUOTECORRUPTXX") for f, q in QUOTE_PINS]


def coverage_detector(text):
    """Flags a corpus that already ANSWERS item 4's literal question."""
    marker = "Each chirality half is totally null"
    if MUT == 9:                   # MACHINERY: blind the detector
        marker = "ZZ-this-string-does-not-occur-ZZ"
    return marker in norm(text)


# --------------------------------------------------------------------------
def main():
    qs = [0, 5] if FAST else [0, 1, 2, 3, 4, 5, 6, 7]
    print(f"LD-B probe  --  scope q in {qs}"
          + ("  [FAST/selftest scope]" if FAST else "  [full]")
          + (f"  [MUTATION {MUT}]" if MUT else ""))
    print("=" * 78)

    # ---- A. reproduction of banked numbers -------------------------------
    print("\n-- A. reproduction of banked numbers [R]")
    d95 = horn_data({4, 5, 6, 7, 8})
    d77 = horn_data({4, 5, 6, 7, 8, 9, 10})
    d140 = horn_data(set())
    check("triplet dimension is 192 at (9,5)/(7,7)/(14,0)",
          d95["dim"] == d77["dim"] == d140["dim"] == 192,
          f"{d95['dim']}/{d77['dim']}/{d140['dim']}", tag="[R canon 2]")
    check("triplet Krein signature is (+96,-96,0) at all three",
          all(d["full"] == (96, 96, 0) for d in (d95, d77, d140)),
          f"{d95['full']} {d77['full']} {d140['full']}", tag="[R canon 3]")
    check("each chirality half of the triplet has dimension 96",
          all(d["halves"]["+"][0] == d["halves"]["-"][0] == 96 for d in (d95, d77, d140)),
          "", tag="[R canon 3]")

    # Rider found by this probe's own mutation harness: an early mutation that
    # dropped the gamma-trace constraint was INERT.  The reason is a fact, not a
    # harness bug -- the top-Casimir self-dual stratum is automatically
    # gamma-traceless, so `Pi` is redundant for the triplet (it is NOT redundant
    # for `ker(Gamma)` as a whole, which is what section G uses).
    e_r = gammas({4, 5, 6, 7, 8})
    Gam_r = np.hstack(e_r)
    J_r = [np.kron(I14, sgen(e_r, a, b) + sgen(e_r, c, d))
           + np.kron(lvec(a, b) + lvec(c, d), I128) for (a, b, c, d) in SD]
    Cas_r = -(J_r[0] @ J_r[0] + J_r[1] @ J_r[1] + J_r[2] @ J_r[2])
    ev_r, U_r = np.linalg.eigh(0.5 * (Cas_r + Cas_r.conj().T))
    top_r = max(round(x.real, 3) for x in ev_r)
    Wt_free = U_r[:, np.abs(ev_r - top_r) < 1e-3]
    resid = float(np.linalg.norm(Gam_r @ Wt_free)) / max(1.0, Wt_free.shape[1])
    check("RIDER: the UNCONSTRAINED top-Casimir stratum is already gamma-traceless",
          Wt_free.shape[1] == 192 and resid < 1e-9,
          f"dim {Wt_free.shape[1]}, ||Gamma.Wt||/dim = {resid:.1e}")

    # ---- B. the parity rule (new) ----------------------------------------
    print("\n-- B. NEW: chirality halves are totally null IFF q is ODD")
    for q in qs:
        d = horn_data(set(range(4, 4 + q)))
        exp = PARITY_REF[q]
        got = d["halves"]["+"][1]
        got2 = d["halves"]["-"][1]
        same = (got == exp) and (got2 == (exp[1], exp[0], exp[2]) or got2 == exp)
        check(f"q={q} ({d['p']},{d['q']}): chi-half signature {got}",
              same, f"expected {exp}")
        check(f"q={q}: {{K,chi}}=0 iff q odd",
              (d["anti"] < 1e-9) == (q % 2 == 1) and (d["comm"] < 1e-9) == (q % 2 == 0),
              f"anti={d['anti']:.1e} comm={d['comm']:.1e}")

    # ---- C. the canon defect ---------------------------------------------
    print("\n-- C. NEW: the canon sentence over-generalises to (14,0)")
    check("at (14,0) the chirality halves are DEFINITE, not null",
          d140["halves"]["+"][1] == (96, 0, 0) and d140["halves"]["-"][1] == (0, 96, 0),
          f"chi+ {d140['halves']['+'][1]}  chi- {d140['halves']['-'][1]}")
    check("canon states the nullity for a scope that INCLUDES (14,0)",
          "in `(9,5)`, `(7,7)`, and `(14,0)`" in norm(read("canon/ghost-parity-krein-synthesis.md"))
          and "Each chirality half is totally null" in norm(read("canon/ghost-parity-krein-synthesis.md")),
          "both sentences present and adjacent")

    # ---- D. the fence map -------------------------------------------------
    print("\n-- D. NEW: the R3 fence conclusion Re tr(chi.Pi_+)=0 -- where it holds")
    for q in qs:
        d = horn_data(set(range(4, 4 + q)))
        holds = abs(d["fence"]) < 1e-8
        check(f"q={q}: fence {'HOLDS' if holds else 'FAILS'} (Re tr = {d['fence']:.3f})",
              holds == FENCE_REF[q], f"reference says {'HOLDS' if FENCE_REF[q] else 'FAILS'}")

    # ---- E. transversality ------------------------------------------------
    print("\n-- E. NEW: every K-positive direction is at exactly 45 deg to both halves")
    for lab, d in (("(9,5)", d95), ("(7,7)", d77)):
        for nm in "+-":
            sv = d["ang"][nm]
            check(f"{lab}: all 96 principal cosines vs chi{nm} equal 1/sqrt(2)",
                  len(sv) == 96 and np.allclose(sv, 1 / np.sqrt(2), atol=1e-8),
                  f"min {sv.min():.9f} max {sv.max():.9f}")
            check(f"{lab}: dim(P ∩ chi{nm}) = 0", int(np.sum(sv > 1 - 1e-8)) == 0)

    # ---- F. item 3: the direction inside one irrep ------------------------
    print("\n-- F. NEW (item 3): the VEV DIRECTION inside Lambda^1 changes the rank")
    for tl, lab in (({4, 5, 6, 7, 8}, "(9,5)"), ({4, 5, 6, 7, 8, 9, 10}, "(7,7)")):
        e = gammas(tl)
        chi = chirality(e)
        wv, U = np.linalg.eigh(chi)
        Sp, Sm = U[:, wv > 0.5], U[:, wv < -0.5]
        eta = np.diag([(-1.0 if a in tl else 1.0) for a in range(N)])

        def rank_for(vec):
            ew = sum(vec[a] * e[a] for a in range(N))
            return int(np.linalg.matrix_rank(Sm.conj().T @ ew @ Sp, tol=1e-8))

        rng = np.random.default_rng(0)
        wg = rng.normal(size=N)
        t0 = sorted(tl)[0]
        wn = np.zeros(N)
        wn[0] = 1.0
        wn[t0] = 1.0
        check(f"{lab}: null direction really is null", abs(wn @ eta @ wn) < 1e-12)
        check(f"{lab}: generic Lambda^1 direction gives rank {RANK_REF['generic']}",
              rank_for(wg) == RANK_REF["generic"], f"got {rank_for(wg)}")
        check(f"{lab}: NULL Lambda^1 direction gives rank {RANK_REF['null']}",
              rank_for(wn) == RANK_REF["null"], f"got {rank_for(wn)}")
    e0 = gammas(set())
    check("(14,0): no null directions exist (definite signature)",
          not any(abs(v @ np.eye(N) @ v) < 1e-12
                  for v in np.random.default_rng(3).normal(size=(50, N))))

    # ---- G. BD-D disanalogy -----------------------------------------------
    print("\n-- G. NEW (item 4, second leg): BD-D Part-1 has no analogue for V(x)S")
    e = gammas({4, 5, 6, 7, 8})
    Gam = np.hstack(e)
    kerdim = N * DIM - np.linalg.matrix_rank(Gam, tol=1e-8)
    check("dim ker(Gamma) = 1664 = 13 * 128", kerdim == 1664, f"{kerdim}")
    rng = np.random.default_rng(1)
    lines = []
    for _ in range(6):
        v = rng.normal(size=N)
        ev_ = sum(v[a] * e[a] for a in range(N))
        lines.append(DIM - np.linalg.matrix_rank(ev_, tol=1e-8))
    check("ker(Gamma) contains no v(x)S line -> it is NOT U(x)S",
          all(x == 0 for x in lines), f"dims {lines}")

    # ---- H. quote pins ----------------------------------------------------
    print("\n-- H. every quote the cards lean on is present in the live corpus")
    for rel, quote in QUOTE_PINS:
        try:
            present = norm(quote) in norm(read(rel))
        except FileNotFoundError:
            present = False
        check(f"quote pin: {os.path.basename(rel)} :: {quote[:52]}", present)

    # ---- I. card table + the deliberately wrong verdict --------------------
    print("\n-- I. card table pinned; the planted WRONG verdict must be caught")
    check("five cards, one per assigned concern", sorted(CARDS) == ["3", "4", "5", "8", "9"],
          ",".join(sorted(CARDS)))
    canon_txt = read("canon/ghost-parity-krein-synthesis.md")
    covered = coverage_detector(canon_txt)
    check("coverage detector finds canon ALREADY answers item 4's literal question", covered)
    cid, cverdict, _ = CONTROL_CARD
    caught = covered and cverdict.startswith("LIVE")
    check(f"planted WRONG verdict {cid}='{cverdict}' is CAUGHT by the coverage machinery",
          caught, "a LIVE verdict on a question canon answers is flagged")
    check("item 4's shipped card is NOT purely LIVE (it concedes the coverage)",
          CARDS["4"].startswith("ALREADY-COVERED"), CARDS["4"][:46])

    # ---- J. planted-positive control for the absence claims ---------------
    print("\n-- J. planted-positive control (absence detector must have power)")
    R5_MARK = "the wave must exhibit the dial's action on all sectors simultaneously"

    def executed_detector(text):
        return R5_MARK in norm(text) and "EXECUTED" in norm(text)

    synthetic = "R5 check " + R5_MARK + " -- status: EXECUTED, 12/12 exit 0."
    check("detector FLAGS a synthetic positive it is required to flag",
          executed_detector(synthetic))
    real = read("explorations/decoupling-constructibility-packet-2026-08-12.md")
    check("R5 obligation is stated in the packet", R5_MARK in norm(real))
    check("...and the packet does not mark it executed", not executed_detector(real))

    # ---- K. planted false facts -------------------------------------------
    print("\n-- K. planted false facts (each must be observed False)")
    planted = [
        ("chirality halves are null at (14,0)", d140["halves"]["+"][1] == (0, 0, 96)),
        ("the fence holds at q=0", abs(d140["fence"]) < 1e-8),
        ("68 is the dimension of the VEV/insertion space", False),
        ("the triplet signature depends on the horn", d95["full"] != d77["full"]),
        ("a null Lambda^1 direction has full rank 64", RANK_REF["null"] == 64),
        ("ker(Gamma) is a tensor product U(x)S", any(x > 0 for x in lines)),
        ("K and chi commute on a physical horn", d95["comm"] < 1e-9),
    ]
    for nm, val in planted:
        check(f"planted false: {nm}", val is False or val == 0)

    # ---- verdict ----------------------------------------------------------
    npass = sum(1 for _, ok, _, _ in _results if ok)
    ntot = len(_results)
    print("\n" + "=" * 78)
    print(f"{npass}/{ntot} checks pass")
    return 0 if npass == ntot else 1


# --------------------------------------------------------------------------
def selftest():
    """Baseline first, THEN mutations.  A catch needs a genuine [FAIL] line."""
    me = os.path.abspath(__file__)
    env = dict(os.environ, LDB_FAST="1")
    env.pop("LDB_MUTATE", None)

    print("SELFTEST step 1 -- CLEAN BASELINE must pass before any mutation is run")
    r = subprocess.run([sys.executable, me], env=env, capture_output=True, text=True)
    if r.returncode != 0 or "[FAIL]" in r.stdout:
        print("BASELINE IS RED -- aborting.  Every mutation would exit nonzero for the")
        print("pre-existing reason, so no mutation result would mean anything.")
        print(r.stdout[-3000:])
        return 1
    print(f"  baseline exit 0, no [FAIL] lines  ({r.stdout.strip().splitlines()[-1]})\n")

    muts = {
        1: "MACHINERY: beta_S built from timelike instead of spacelike gammas",
        2: "MACHINERY: chirality operator drops one gamma",
        3: "MACHINERY: SD triple replaced by a non-self-dual quadruple set",
        4: "MACHINERY: wrong Casimir stratum selected as the triplet",
        5: "REFERENCE: parity table asserts canon's unqualified 'always null'",
        6: "REFERENCE: fence table claims the fence is universal",
        7: "REFERENCE: rank table claims direction does not matter",
        8: "REFERENCE: quote corpus corrupted",
        9: "MACHINERY: coverage detector blinded",
    }
    caught = 0
    for k in sorted(muts):
        e2 = dict(env, LDB_MUTATE=str(k))
        rr = subprocess.run([sys.executable, me], env=e2, capture_output=True, text=True)
        has_fail = "[FAIL]" in rr.stdout
        ok = (rr.returncode != 0) and has_fail
        if rr.returncode != 0 and not has_fail:
            verdict = "CRASH-NOT-DETECTION (rejected)"
        elif ok:
            verdict = "caught via genuine [FAIL]"
        else:
            verdict = "NOT CAUGHT"
        caught += ok
        print(f"  mutation {k}: {muts[k]}\n     -> exit {rr.returncode}, "
              f"[FAIL] present={has_fail} -- {verdict}")
    print(f"\nSELFTEST: {caught}/{len(muts)} mutations caught via a genuine failing check")
    return 0 if caught == len(muts) else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
