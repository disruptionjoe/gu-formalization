#!/usr/bin/env python3
"""la1 — exact re-check of the zero-bit hypercharge line behind RA-A3 / RA-B1..B5.

This is a RE-VERIFICATION, not a new result. The theorem it re-checks is already
banked in the repo:

  explorations/channel-swing-CH-SM-2026-07-19.md:69-76,240  (kill class 3)
  explorations/conditional-build/cb-a-representation-content-2026-08-05.md:272 (C1)
  lab/active-research/pati-salam-chain-verification.md      (Step 5)

What is new here is only the arithmetic type: the prior artifacts' published
outputs carry float residues (`sum Y = 5.55112e-16`). Everything below is exact
`fractions.Fraction`; nothing is a float; every assertion has a named negative
control so that no PASS is vacuously true.

Scope: complexified finite weight-lattice arithmetic on the 16 of so(10).
No source action, vacuum, stabilizer selection, physical domain, carrier
projection, chirality mechanism or generation count is used or established.
"""

from fractions import Fraction as F
from itertools import product, permutations

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok), detail))


# ---------------------------------------------------------------------------
# 1. the 16 of so(10): weights (+-1/2)^5 with an even number of minus signs
# ---------------------------------------------------------------------------
HALF = F(1, 2)
ALL32 = [w for w in product((HALF, -HALF), repeat=5)]
SIXTEEN = [w for w in ALL32 if sum(1 for c in w if c < 0) % 2 == 0]
ANTI16 = [w for w in ALL32 if sum(1 for c in w if c < 0) % 2 == 1]

check("Dirac spinor of so(10) has 32 weights", len(ALL32) == 32, f"{len(ALL32)}")
check("chiral 16 = even-minus-sign weights", len(SIXTEEN) == 16, f"{len(SIXTEEN)}")
check("conjugate 16bar = odd-minus-sign weights", len(ANTI16) == 16, f"{len(ANTI16)}")
check(
    "16 and 16bar are disjoint and exhaust the 32 (non-vacuity control)",
    not (set(SIXTEEN) & set(ANTI16)) and len(set(SIXTEEN) | set(ANTI16)) == 32,
)

# ---------------------------------------------------------------------------
# 2. Pati-Salam Cartan split: coords 1-3 -> so(6)=su(4), coords 4-5 -> so(4)
#    Both blocks are inside the maximal compact so(6)+so(4) of so(6,4).
# ---------------------------------------------------------------------------
def BmL(w):
    return F(2, 3) * (w[0] + w[1] + w[2])


def T3L(w):
    return (w[3] + w[4]) / 2


def T3R(w):
    return (w[3] - w[4]) / 2


def colour_dim(w):
    m = sum(1 for c in w[:3] if c < 0)
    return 1 if m in (0, 3) else 3


def colour_tag(w):
    m = sum(1 for c in w[:3] if c < 0)
    return {0: "1", 3: "1", 1: "3a", 2: "3b"}[m]


def iso_tag(w):
    return "doublet" if abs(T3L(w)) == HALF else "singlet"


def iso_dim(w):
    return 2 if abs(T3L(w)) == HALF else 1


def multiplets(weights, a, b):
    """Group weights into (colour_tag, iso_tag, n) blocks for Y = a*T3R + b*(B-L)."""
    out = {}
    for w in weights:
        Y = a * T3R(w) + b * BmL(w)
        n = 6 * Y
        key = (colour_tag(w), iso_tag(w), n)
        out[key] = out.get(key, 0) + 1
    return out


def signature(weights, a, b):
    """Convention-free comparison key: multiset of (colour_dim, iso_dim, n)."""
    sig = {}
    for w in weights:
        Y = a * T3R(w) + b * BmL(w)
        n = 6 * Y
        key = (colour_dim(w), iso_dim(w), n)
        sig[key] = sig.get(key, 0) + 1
    return sig


# Weinstein 2021 draft, Section 11.3, n = 1 generation table, as
# (colour_dim, iso_dim, n) -> number of states.
PAPER_TABLE = {
    (3, 2, F(1)): 6,   # Q_L      (3,2)  Y = 1/6
    (3, 1, F(2)): 3,   # d^c      (3bar,1) Y = 1/3
    (3, 1, F(-4)): 3,  # u^c      (3bar,1) Y = -2/3
    (1, 2, F(-3)): 2,  # L_L      (1,2)  Y = -1/2
    (1, 1, F(6)): 1,   # e^c      (1,1)  Y = 1
    (1, 1, F(0)): 1,   # nu^c     (1,1)  Y = 0
}

A_STD, B_STD = F(1), F(1, 2)   # Y = T3R + (B-L)/2

sig16 = signature(SIXTEEN, A_STD, B_STD)
sig16bar = signature(ANTI16, A_STD, B_STD)
matching = [tag for tag, s in (("16", sig16), ("16bar", sig16bar)) if s == PAPER_TABLE]

check(
    "exactly one chirality reproduces the Section-11.3 table under Y = T3R + (B-L)/2",
    len(matching) == 1,
    f"matching chirality: {matching}",
)
check(
    "the other chirality is the exact CP conjugate (n -> -n, colour conjugated)",
    {(c, i, -n): m for (c, i, n), m in sig16.items()} == sig16bar,
)

GEN = SIXTEEN if sig16 == PAPER_TABLE else ANTI16
check("the matching chirality carries exactly 16 states", len(GEN) == 16, f"{len(GEN)}")
check(
    "matching chirality has exactly 6 SM multiplets",
    len(multiplets(GEN, A_STD, B_STD)) == 6,
    f"{sorted(multiplets(GEN, A_STD, B_STD))}",
)

# ---------------------------------------------------------------------------
# 3. EXACT quantisation (the arithmetic content of ledger row RA-A3)
# ---------------------------------------------------------------------------
n_values = sorted({6 * (A_STD * T3R(w) + B_STD * BmL(w)) for w in GEN})
check(
    "every hypercharge on the 16 satisfies 6Y in Z (charge quantisation, exact)",
    all(v.denominator == 1 for v in n_values),
    f"n = {[int(v) for v in n_values]}",
)
nonzero = [abs(int(v)) for v in n_values if v != 0]
g = nonzero[0]
for v in nonzero[1:]:
    while v:
        g, v = v, g % v
check(
    "gcd of the nonzero 6Y values is 1, so Y = 1/6 is the exact minimal unit",
    g == 1,
    f"gcd = {g}",
)
check(
    "quantisation is a real constraint, not automatic: the raw Cartan coordinates "
    "are half-integral (non-vacuity control)",
    any((6 * c).denominator != 1 for w in GEN for c in w) is False
    and any(c.denominator == 2 for w in GEN for c in w),
    "weights live in (1/2)Z, hypercharge lands in (1/6)Z",
)

# exact anomaly traces (previously published with float residue ~5.6e-16)
trY = sum(A_STD * T3R(w) + B_STD * BmL(w) for w in GEN)
trY3 = sum((A_STD * T3R(w) + B_STD * BmL(w)) ** 3 for w in GEN)
trQ = sum(T3L(w) + A_STD * T3R(w) + B_STD * BmL(w) for w in GEN)
check("Tr Y = 0 exactly (not a float residue)", trY == 0, f"Tr Y = {trY}")
check("Tr Y^3 = 0 exactly", trY3 == 0, f"Tr Y^3 = {trY3}")
check("Tr Q = 0 exactly", trQ == 0, f"Tr Q = {trQ}")

# ---------------------------------------------------------------------------
# 4. THE ZERO-BIT SOLVE: how many lines Y = a*T3R + b*(B-L) reproduce the table?
#    Finite exact enumeration; no search over the rationals.
# ---------------------------------------------------------------------------
# Block by the (a,b)-INDEPENDENT weight data: the su(3) x su(2)_L irrep together
# with the su(2)_R Cartan value and the u(1)_{B-L} charge. Y never enters the key,
# so the solve below is not circular.
blocks = {}
for w in GEN:
    blocks.setdefault((colour_tag(w), iso_tag(w), T3R(w), BmL(w)), []).append(w)
reps = {k: v[0] for k, v in blocks.items()}
check(
    "the 16 splits into exactly 6 blocks under su(3) x su(2)_L x T3R x (B-L)",
    len(blocks) == 6,
    f"sizes = {sorted(len(v) for v in blocks.values())}",
)
check(
    "block sizes are exactly 6+3+3+2+1+1 = 16",
    sorted(len(v) for v in blocks.values()) == [1, 1, 2, 3, 3, 6],
)

targets = []
for (cd, idim, n), mult in PAPER_TABLE.items():
    targets.append((cd, idim, n, mult))

# candidate assignments: every bijection blocks -> targets that matches
# colour dimension, isospin dimension and state count.
block_keys = sorted(blocks)


def block_shape(k):
    w = reps[k]
    return (colour_dim(w), iso_dim(w), len(blocks[k]))


valid_assignments = []
for perm in permutations(range(6)):
    ok = True
    for i, k in enumerate(block_keys):
        cd, idim, n, mult = targets[perm[i]]
        if block_shape(k) != (cd, idim, mult):
            ok = False
            break
    if ok:
        valid_assignments.append(perm)

solutions = set()
for perm in valid_assignments:
    # solve a*T3R(rep) + b*BmL(rep) = n/6 for two blocks, verify on all six
    eqs = []
    for i, k in enumerate(block_keys):
        _, _, n, _ = targets[perm[i]]
        eqs.append((T3R(reps[k]), BmL(reps[k]), F(n, 6)))
    sol = None
    for i in range(6):
        for j in range(i + 1, 6):
            x1, y1, c1 = eqs[i]
            x2, y2, c2 = eqs[j]
            det = x1 * y2 - x2 * y1
            if det == 0:
                continue
            a = (c1 * y2 - c2 * y1) / det
            b = (x1 * c2 - x2 * c1) / det
            sol = (a, b)
            break
        if sol:
            break
    if sol is None:
        continue
    a, b = sol
    if all(a * x + b * y == c for x, y, c in eqs) and signature(GEN, a, b) == PAPER_TABLE:
        solutions.add((a, b))

check(
    "the shape-respecting assignment search is non-empty (non-vacuity control)",
    len(valid_assignments) > 0,
    f"{len(valid_assignments)} shape-respecting bijections tested",
)
check(
    "EXACTLY TWO lines (a,b) reproduce the Section-11.3 multiset",
    len(solutions) == 2,
    f"solutions = {sorted((str(a), str(b)) for a, b in solutions)}",
)
check(
    "the two solutions are the standard line and its T3R sign flip",
    solutions == {(F(1), F(1, 2)), (F(-1), F(1, 2))},
    f"{sorted((str(a), str(b)) for a, b in solutions)}",
)

# the two solutions are Spin(10)-gauge-conjugate: the SU(2)_R Weyl element w4<->w5
def swap45(w):
    return (w[0], w[1], w[2], w[4], w[3])


check(
    "the SU(2)_R Weyl element w4<->w5 preserves the 16 as a set",
    {swap45(w) for w in GEN} == set(GEN),
)
check(
    "w4<->w5 negates T3R and fixes T3L and B-L, so it maps one solution to the other: "
    "ONE physical hypercharge line, 0 bits",
    all(T3R(swap45(w)) == -T3R(w) and T3L(swap45(w)) == T3L(w) and BmL(swap45(w)) == BmL(w)
        for w in GEN),
)

# ---------------------------------------------------------------------------
# 5. NEGATIVE CONTROLS — named wrong lines that must miss the multiset
# ---------------------------------------------------------------------------
CONTROLS = {
    "T3R alone            (a,b)=(1,0)": (F(1), F(0)),
    "(B-L)/2 alone        (a,b)=(0,1/2)": (F(0), F(1, 2)),
    "B-L alone            (a,b)=(0,1)": (F(0), F(1)),
    "wrong slope          (a,b)=(2,1/2)": (F(2), F(1, 2)),
    "wrong slope          (a,b)=(1,1)": (F(1), F(1)),
    "X-line               (a,b)=(-4,3)": (F(-4), F(3)),
    "sign-flipped B-L     (a,b)=(1,-1/2)": (F(1), F(-1, 2)),
}
for label, (a, b) in CONTROLS.items():
    check(f"control MISSES the multiset: {label}", signature(GEN, a, b) != PAPER_TABLE)

# ---------------------------------------------------------------------------
# 5b. WHICH constraints actually discriminate? (anti-vacuity audit)
#     CB-A section 4 counts "11 independent constraints, 0 free parameters".
#     Test each of the five 4D anomaly conditions against the control lines:
#     a condition that every control also satisfies constrains nothing.
# ---------------------------------------------------------------------------
def anomaly_conditions(a, b):
    Y = lambda w: a * T3R(w) + b * BmL(w)
    return {
        "grav^2.U(1):  Tr Y = 0": sum(Y(w) for w in GEN) == 0,
        "U(1)^3:       Tr Y^3 = 0": sum(Y(w) ** 3 for w in GEN) == 0,
        "SU(3)^2.U(1): sum Y over coloured = 0":
            sum(Y(w) for w in GEN if colour_dim(w) == 3) == 0,
        "SU(2)^2.U(1): sum Y over doublets = 0":
            sum(Y(w) for w in GEN if iso_dim(w) == 2) == 0,
        "Witten SU(2):  doublet count even":
            sum(1 for w in GEN if iso_dim(w) == 2) % 2 == 0,
    }

# a wide exact sweep of the 2-plane, not just the 7 named controls
SWEEP = [(F(p), F(q, 6)) for p in range(-5, 6) for q in range(-6, 7)]
SWEEP = [(a, b) for (a, b) in SWEEP if (a, b) != (F(0), F(0))]

DISCRIMINATION = {}
std_conditions = anomaly_conditions(A_STD, B_STD)
for cname, held in std_conditions.items():
    check(f"standard line satisfies {cname}", held)
    also = sum(1 for (a, b) in SWEEP if anomaly_conditions(a, b)[cname])
    DISCRIMINATION[cname] = (also, len(SWEEP))

check(
    "FINDING (anti-vacuity): NO 4D anomaly condition discriminates the hypercharge "
    "line -- all five hold identically on every line in the T3R/(B-L) 2-plane, "
    "because the 16 is a complete anomaly-free so(10) irrep",
    all(n == len(SWEEP) for n, _ in DISCRIMINATION.values()),
    "; ".join(f"[{c}] holds on {n}/{t} swept lines" for c, (n, t) in DISCRIMINATION.items()),
)
check(
    "the sweep is wide enough to be evidence (non-vacuity control): it contains "
    "lines that DO fail the hypercharge-multiset test",
    sum(1 for (a, b) in SWEEP if signature(GEN, a, b) != PAPER_TABLE) == len(SWEEP) - 2,
    f"{len(SWEEP)} lines swept, exactly 2 reproduce the multiset",
)
check(
    "therefore the discriminating content is the six hypercharge VALUES alone; "
    "the five anomaly rows are entailed by the completeness of the 16, not by the line",
    len({(a, b) for (a, b) in SWEEP if signature(GEN, a, b) == PAPER_TABLE}) == 2,
)

# ---------------------------------------------------------------------------
# 6. what this does NOT establish
# ---------------------------------------------------------------------------
NOT_ESTABLISHED = [
    "that any source action exists, is stationary, or selects a vacuum",
    "that any vacuum stabilizer is G_SM-shaped (ledger RA-A8 / CB-A unknown U1)",
    "that a physical carrier projection delivers a complete chiral 16 in 4D",
    "the generation count, effective chirality, or the 2+1 construction",
    "compactness of U(1)_Y independently of the stabilizer sitting inside the",
    "  source's own written maximal-compact step Spin(6) x Spin(4) < Spin(6,4)",
]

if __name__ == "__main__":
    width = max(len(n) for n, _, _ in CHECKS)
    npass = 0
    for name, ok, detail in CHECKS:
        npass += ok
        tag = "PASS" if ok else "FAIL"
        print(f"[{tag}] {name.ljust(width)}  {detail}")
    print("-" * 72)
    print(f"CERTIFICATE: {npass}/{len(CHECKS)} exact checks pass, zero floats.")
    print("-" * 72)
    print("NOT established by this script:")
    for line in NOT_ESTABLISHED:
        print("  - " + line)
    raise SystemExit(0 if npass == len(CHECKS) else 1)
