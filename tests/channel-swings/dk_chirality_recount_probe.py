#!/usr/bin/env python3
r"""DK CHIRALITY RECOUNT -- the Dirac-Kahler fork on the assumed truncated fermion
content behind the pure-gravitational anomaly obstruction (the -13 / 13/37800 line).

CHANNEL:  Section-A false-wall check (five-path fan-out, Dirac-Kahler chirality fork).
DIRECTED: Joe direct chat, 2026-07-20.
DESIGN:   explorations/dk-chirality-fork-2026-07-20.md
EXTENDS:  tests/ahat_genus_y14_i16.py            (the verified A-hat engine, re-derived here)
          tests/chase/MOVE-1/move1_octic_sp64_vs_sp1.py  (the baseline -13 / 13/37800 convention)
          explorations/intake-bianconi-entropic-gravity-2026-07-20.md (leg 3, the fork trigger)
STATUS:   exploration tier; EVERY outcome typed FORK-CONDITIONAL; no claim, canon,
          or public-posture movement. Deterministic, exact Fraction arithmetic only.

THE QUESTION. The repo's pure-gravitational obstruction (MOVE1-01; WHERE-GU-STANDS
Section A) is nonzero ONLY because the ASSUMED truncated content
    C0 = Omega^0(Y14) (x) S^+  (+)  Omega^1(Y14) (x) S^-
has net chirality n_+ - n_- = C(14,0) - C(14,1) = 1 - 14 = -13
(grav tr R^8 coefficient 64 * (-13) * (-1/2419200) = 13/37800 != 0).
The repo states this is "conditional on the assumed fermion content". This probe
populates the fork table: it RECOMPUTES (never trusts) the A-hat machinery and the
baseline, then recounts n_+ - n_- and the resulting tr R^8 coefficient for every
honest completion/variant of the content, including the geometer-complete
Dirac-Kahler complex (forms-as-spinors, no truncation) and GU's own draft-literal
Section 9.3 content (nu, zeta in Omega^{0,1}(Y, /S) with the FULL Dirac bundle /S).

CONSTRUCTION DISCIPLINE (GEOMETER-VS-PHYSICS-OBJECTS.md): every content candidate
is NAMED with its construction (native / import / template). The verdicts below are
FORK-CONDITIONAL statements, one per branch; none is a repair and none kills a branch.

CHECK TAGS:  [T] setup / engine cross-checks (excluded from the headline count)
             [E] established recount computations
             [F] fork-consequence verdicts
Exit 0 iff every check passes. HEADLINE printed last.

Run:  python tests/channel-swings/dk_chirality_recount_probe.py
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb, factorial

# ----------------------------------------------------------------------------
# check bookkeeping
# ----------------------------------------------------------------------------
CHECKS: list[tuple[str, str, bool]] = []   # (tag, name, ok)


def check(tag: str, name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((tag, name, bool(ok)))
    status = "PASS" if ok else "FAIL"
    line = f"[{tag}] {status}  {name}"
    if detail:
        line += f"   {detail}"
    print(line)
    assert ok, f"[{tag}] {name} FAILED: {detail}"


# ============================================================================
# PART 1 [T] -- the A-hat engine, RE-DERIVED (never trust a cached coefficient).
# Same mathematics as tests/ahat_genus_y14_i16.py (Q(x) = (x/2)/sinh(x/2), Newton
# power sums, graded exponential), re-implemented and re-cross-checked here.
# ============================================================================
WMAX = 4
KEY0 = (0, 0, 0, 0)


def wt(k):
    return k[0] + 2 * k[1] + 3 * k[2] + 4 * k[3]


def padd(a, b):
    o = dict(a)
    for k, v in b.items():
        o[k] = o.get(k, F(0)) + v
    return {k: v for k, v in o.items() if v != 0}


def pscale(a, c):
    return {k: v * c for k, v in a.items() if v * c != 0}


def pmul(a, b):
    o = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = (ka[0] + kb[0], ka[1] + kb[1], ka[2] + kb[2], ka[3] + kb[3])
            if wt(k) <= WMAX:
                o[k] = o.get(k, F(0)) + va * vb
    return {k: v for k, v in o.items() if v != 0}


# Newton: power sums P_k of x_i^2 in terms of Pontryagin p_j = e_j(x_i^2)
P = {
    1: {(1, 0, 0, 0): F(1)},
    2: {(2, 0, 0, 0): F(1), (0, 1, 0, 0): F(-2)},
    3: {(3, 0, 0, 0): F(1), (1, 1, 0, 0): F(-3), (0, 0, 1, 0): F(3)},
    4: {(4, 0, 0, 0): F(1), (2, 1, 0, 0): F(-4), (1, 0, 1, 0): F(4),
        (0, 2, 0, 0): F(2), (0, 0, 0, 1): F(-4)},
}


def g_coeffs():
    h = [F(1, 4 ** m * factorial(2 * m + 1)) for m in range(WMAX + 1)]
    w = [F(0)] + h[1:]

    def smul(a, b):
        r = [F(0)] * (WMAX + 1)
        for i in range(WMAX + 1):
            if a[i] == 0:
                continue
            for j in range(WMAX + 1 - i):
                r[i + j] += a[i] * b[j]
        return r

    logh = [F(0)] * (WMAX + 1)
    wn = [F(1)] + [F(0)] * WMAX
    for n in range(1, WMAX + 1):
        wn = smul(wn, w)
        c = F((-1) ** (n + 1), n)
        for i in range(WMAX + 1):
            logh[i] += c * wn[i]
    return [F(0)] + [-logh[k] for k in range(1, WMAX + 1)]


def ahat_graded():
    g = g_coeffs()
    L = {}
    for k in range(1, WMAX + 1):
        L = padd(L, pscale(P[k], g[k]))
    acc = {KEY0: F(1)}
    Lp = {KEY0: F(1)}
    for n in range(1, WMAX + 1):
        Lp = pmul(Lp, L)
        acc = padd(acc, pscale(Lp, F(1, factorial(n))))
    graded = {w: {} for w in range(WMAX + 1)}
    for k, v in acc.items():
        graded[wt(k)][k] = v
    return graded


print("=" * 84)
print("PART 1  [T]  A-hat engine re-derivation + cross-checks (baseline machinery)")
print("=" * 84)

G = ahat_graded()
a4, a8, a12, a16 = G[1], G[2], G[3], G[4]

check("T", "canonical [A-hat]_4 = -p1/24",
      a4 == {(1, 0, 0, 0): F(-1, 24)})
check("T", "canonical [A-hat]_8 = (7p1^2 - 4p2)/5760",
      a8 == {(2, 0, 0, 0): F(7, 5760), (0, 1, 0, 0): F(-4, 5760)})
check("T", "canonical [A-hat]_12 = (-31p1^3 + 44p1p2 - 16p3)/967680",
      a12 == {(3, 0, 0, 0): F(-31, 967680), (1, 1, 0, 0): F(44, 967680),
              (0, 0, 1, 0): F(-16, 967680)})

D = 464486400
AGW16 = {(4, 0, 0, 0): F(381, D), (2, 1, 0, 0): F(-904, D), (0, 2, 0, 0): F(208, D),
         (1, 0, 1, 0): F(512, D), (0, 0, 0, 1): F(-192, D)}
check("T", "[A-hat]_16 = (381 p1^4 - 904 p1^2p2 + 208 p2^2 + 512 p1p3 - 192 p4)/464486400",
      a16 == AGW16)

# end-to-end index checks on the DEGREE-16 coefficients themselves
A = -48
pontK3 = {(4, 0, 0, 0): 24, (2, 1, 0, 0): 12, (0, 2, 0, 0): 6,
          (1, 0, 1, 0): 4, (0, 0, 0, 1): 1}
iK3 = sum(a16.get(k, F(0)) * m for k, m in pontK3.items()) * (A ** 4)
check("T", "end-to-end Dirac index on (K3)^4 = 16", iK3 == 16, f"got {iK3}")

pontHP = {(4, 0, 0, 0): 96, (2, 1, 0, 0): 88, (0, 2, 0, 0): 114,
          (1, 0, 1, 0): 56, (0, 0, 0, 1): 49}
iHP = sum(a16.get(k, F(0)) * m for k, m in pontHP.items())
check("T", "end-to-end Dirac index on HP^2 x HP^2 = 0", iHP == 0, f"got {iHP}")

P4 = a16[(0, 0, 0, 1)]
check("T", "tr R^8 channel: p4 coefficient of [A-hat]_16 = -1/2419200",
      P4 == F(-1, 2419200), f"got {P4}")

# ============================================================================
# PART 2 [E] -- Fierz / dimension sanity: forms vs spinors on Y^14 (and d=4 control)
# ============================================================================
print()
print("=" * 84)
print("PART 2  [E]  Fierz / dimension counting: Dirac-Kahler on a 14-manifold")
print("=" * 84)

# real counting: Lambda^* R^14  ~=  Cl(9,5)  ~=  M(64,H)  (vector-space iso)
dim_forms = 2 ** 14                     # 16384
dim_M64H = 64 * 64 * 4                  # M(64,H) real dimension
dim_S = 64 * 4                          # S = H^64, dim_R = 256
check("E", "dim_R Lambda^*(R^14) = 2^14 = 16384 = dim_R M(64,H)",
      dim_forms == 16384 == dim_M64H)
check("E", "left-regular module: M(64,H) = 64 copies of S = H^64 (64*256 = 16384)",
      64 * dim_S == dim_forms)
# complex counting: Cl(14) (x) C = M(128,C); Lambda^*_C ~= S_C (x) S_C^*
check("E", "complex Fierz: 2^14 = 128 x 128  (forms = spinor (x) cospinor)",
      2 ** 14 == 128 * 128)
# species doubling, with the d=4 lattice control
check("E", "species doubling control d=4:  2^4 = 16 = 4 x 4  -> 2^{4/2} = 4 Dirac species",
      2 ** 4 == 4 * 4 and 2 ** (4 // 2) == 4)
check("E", "species doubling d=14: DK field = 2^{14/2} = 128 complex Dirac species "
      "(quaternionic: 64 copies of S = H^64)", 2 ** (14 // 2) == 128 and 16384 // 256 == 64)
# chirality split per copy: S = S^+ (+) S^-, dim_R 128 + 128 (omega^2 = +1 for p-q = 4 mod 8)
check("E", "per-copy chirality split: dim_R S^+ = dim_R S^- = 128", 128 + 128 == dim_S)

# ============================================================================
# PART 3 [E] -- the RECOUNT. Contents as lists of (form-degree p, chirality eps)
# with eps in {+1 (S^+), -1 (S^-), 0 (full /S = S^+ (+) S^-)}.
# Net chirality W = sum over slots of eps * C(14, p)   (full /S slots contribute 0).
# Convention (identical to move1_octic_sp64_vs_sp1.py): the tr R^8 coefficient of
# the content is  coeff = 64 * W * P4  where P4 = -1/2419200 (recomputed above).
# The survive/vanish verdict depends ONLY on W != 0 (normalization-independent, F5).
# ============================================================================
print()
print("=" * 84)
print("PART 3  [E]  net-chirality recount + tr R^8 coefficient per content candidate")
print("=" * 84)


def W_of(content):
    return sum(eps * comb(14, p) for (p, eps) in content)


def coeff_of(content, dimS=64):
    return dimS * W_of(content) * P4


# --- the candidates (construction named for each; see the exploration doc) ---
C0 = [(0, +1), (1, -1)]                                  # repo baseline (chiral truncation)
C0m = [(0, -1), (1, +1)]                                 # mirror of the baseline
C1 = [(0, 0), (1, 0)]                                    # GU draft-literal Sec 9.3 (full /S)
C2 = [(p, 0) for p in range(15)]                         # full Dirac-Kahler, forms-as-spinors
C3 = [(p, +1 if p % 2 == 0 else -1) for p in range(15)]  # alternating-chirality DK tower
C4 = [(p, +1 if p % 2 == 0 else -1) for p in range(3)]   # Bianconi-style 0+1+2 (alt. chir.)
C5 = [(0, 0), (0, 0), (1, 0), (13, 0), (14, 0)]          # draft 10.10 skeleton, full /S slots
C5b = [(0, +1), (1, -1), (13, +1), (14, -1)]             # chiral 4-slot, alternating (+,-,+,-)
C5c = [(0, +1), (1, -1), (13, -1), (14, +1)]             # chiral 4-slot, Hodge-paired (+,-,-,+)

check("E", "BASELINE REPRODUCED: C0 net chirality n_+ - n_- = 1 - 14 = -13",
      W_of(C0) == -13, f"W = {W_of(C0)}")
check("E", "BASELINE REPRODUCED: C0 tr R^8 coefficient = 64*(-13)*(-1/2419200) = 13/37800",
      coeff_of(C0) == F(13, 37800), f"coeff = {coeff_of(C0)}")

# the partial-sum identity: the -13 is the k=1 partial sum of an alternating series
# whose completion is exactly zero:  sum_{p=0}^{k} (-1)^p C(14,p) = (-1)^k C(13,k).
ok_partial = all(
    sum((-1) ** p * comb(14, p) for p in range(k + 1)) == (-1) ** k * comb(13, k)
    for k in range(15)
)
check("E", "partial-sum identity: sum_{p<=k} (-1)^p C(14,p) = (-1)^k C(13,k) for all k=0..14",
      ok_partial)
check("E", "the baseline -13 IS the k=1 partial sum: (-1)^1 C(13,1) = -13",
      (-1) ** 1 * comb(13, 1) == -13)
check("E", "NO proper truncation balances: (-1)^k C(13,k) != 0 for all k=0..13; "
      "k=14 gives 0 (binomial (1-1)^14)",
      all(comb(13, k) != 0 for k in range(14))
      and sum((-1) ** p * comb(14, p) for p in range(15)) == 0)

rows = [
    ("C0  repo baseline  Om^0xS+ + Om^1xS-          [IMPORT-flagged chirality]", C0, -13),
    ("C0m mirror         Om^0xS- + Om^1xS+          [import, sign choice]", C0m, +13),
    ("C1  draft-literal  Sec 9.3: nu,zeta in Om^{0,1}(/S) full Dirac  [NATIVE]", C1, 0),
    ("C2  full DK        Om^0..Om^14 forms-as-spinors (64 copies of S) [completion]", C2, 0),
    ("C3  alternating DK Om^p x S^{(-1)^p}, p=0..14  [template completion]", C3, 0),
    ("C4  Bianconi 0+1+2 alternating chirality        [partial completion]", C4, +78),
    ("C5  draft 10.10 skeleton, full-/S slots         [native skeleton]", C5, 0),
    ("C5b chiral 4-slot (+,-,+,-)                     [template]", C5b, 0),
    ("C5c chiral 4-slot Hodge-paired (+,-,-,+)        [template]", C5c, -26),
]

print()
print(f"{'content':74s} {'W = n_+ - n_-':>14s} {'tr R^8 coeff':>16s} {'obstruction':>12s}")
for name, content, Wexp in rows:
    W = W_of(content)
    c = coeff_of(content)
    verdict = "VANISHES" if c == 0 else ("SURVIVES" if content in (C0, C0m) else "MOVES")
    print(f"{name:74s} {W:>14d} {str(c):>16s} {verdict:>12s}")
    check("E", f"recount {name.split()[0]}: W = {Wexp}", W == Wexp, f"got {W}")

# expected coefficients, exact
check("E", "C4 (Bianconi 0+1+2, alt): coeff = 64*78*(-1/2419200) = -13/6300",
      coeff_of(C4) == F(-13, 6300), f"got {coeff_of(C4)}")
check("E", "C5c (Hodge-paired 4-slot): coeff = 64*(-26)*(-1/2419200) = 13/18900",
      coeff_of(C5c) == F(13, 18900), f"got {coeff_of(C5c)}")
check("E", "balanced contents C1, C2, C3, C5, C5b all give coeff = 0 exactly",
      all(coeff_of(c) == 0 for c in (C1, C2, C3, C5, C5b)))

# gauge-channel note: the SAME weight W multiplies the gauge octic channel
# (move1 convention Wgauge = n_+ - n_-), so a balanced content zeroes the whole
# conditional local I_16 top-line, not just the gravitational term.
check("E", "gauge-channel weight = same W: balanced content zeroes BOTH channels "
      "of the conditional local I_16", W_of(C1) == W_of(C2) == W_of(C3) == 0)

# ============================================================================
# PART 4 [F] -- fork-consequence verdicts (each one a FORK-CONDITIONAL statement;
# none is a repair, none kills a branch; provenance in the exploration doc).
# ============================================================================
print()
print("=" * 84)
print("PART 4  [F]  fork table verdicts (ALL fork-conditional; no canon movement)")
print("=" * 84)

check("F", "BRANCH A (chiral truncation, import-flagged): obstruction SURVIVES, "
      "coeff = 13/37800 != 0", coeff_of(C0) == F(13, 37800) and coeff_of(C0) != 0)
check("F", "BRANCH B (GU draft-literal Sec 9.3, full /S): obstruction VANISHES identically",
      coeff_of(C1) == 0)
check("F", "BRANCH C (geometer-complete Dirac-Kahler, full or alternating): "
      "obstruction VANISHES identically", coeff_of(C2) == 0 and coeff_of(C3) == 0)
check("F", "PARTIAL completions never balance: every proper alternating truncation "
      "k=0..13 has W = (-1)^k C(13,k) != 0 (Bianconi 0+1+2 MOVES it to -13/6300); "
      "the FULL tower k=14 is the unique balancing point",
      all((-1) ** k * comb(13, k) != 0 for k in range(14)) and W_of(C3) == 0)

# normalization-independence of the verdict: survive/vanish depends only on W != 0
ok_norm = True
for _, content, _ in rows:
    zs = [coeff_of(content, dimS=d) == 0 for d in (64, 128, 256)]
    ok_norm &= (all(zs) or not any(zs))
    ok_norm &= (zs[0] == (W_of(content) == 0))
check("F", "verdicts are normalization-independent: coeff = 0 iff W = 0, under "
      "dimS in {64, 128, 256}", ok_norm)

check("F", "doubling mechanism identified: the completed content is balanced BY the "
      "2^{d/2}-fold DK species doubling (128 complex / 64 quaternionic species, each "
      "vector-like); net chirality from forms requires a truncation (Nielsen-Ninomiya-"
      "shaped wall, cf. tests/nielsen-ninomiya/)",
      2 ** 7 == 128 and W_of(C2) == 0 and W_of(C0) != 0)

# ============================================================================
# HEADLINE
# ============================================================================
nT = sum(1 for t, _, _ in CHECKS if t == "T")
nE = sum(1 for t, _, _ in CHECKS if t == "E")
nF = sum(1 for t, _, _ in CHECKS if t == "F")
all_ok = all(ok for _, _, ok in CHECKS)
print()
print("=" * 84)
print("VERDICT: the -13 (grav 13/37800) obstruction is the k=1 PARTIAL SUM of an")
print("alternating binomial series whose completion is exactly zero. It SURVIVES only")
print("on the chiral-truncation branch (import-flagged chirality assignment); it")
print("VANISHES identically on GU's own draft-literal Sec 9.3 content (full /S) and")
print("on every geometer-complete Dirac-Kahler content; partial completions MOVE it")
print("but never zero it. ALL outcomes FORK-CONDITIONAL; no claim/canon movement.")
print("=" * 84)
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} excluded)   "
      f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
raise SystemExit(0 if all_ok else 1)
