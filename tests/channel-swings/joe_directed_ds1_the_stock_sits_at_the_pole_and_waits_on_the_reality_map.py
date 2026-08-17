#!/usr/bin/env python3
"""DS-1 probe — the sigma_2-direction shop (GB1-SIGMA2-DIRECTION-SUPPLY).

Certifies the artifact
  lab/active-research/joe-directed/grading-bridge/
  ds1-the-stock-sits-at-the-pole-and-waits-on-the-reality-map-2026-08-17.md

LEG 1  QUOTE FIDELITY.  34 (file, line, substring) pins byte-matched at cited
       lines, plus a planted negative the pin machinery must flag.

LEG 2  CLASS / CENSUS ARITHMETIC (exact integers).  eps-slot Z/4 classes
       (2k mod 4, odd k -> class 2) [R TR-1]; the per-grade K-parity censuses
       as binomial identities at both horns; census symmetries; five planted
       false propositions each observed False.

LEG 3  THE Cl(14) INSTRUMENT (exact matrix identities on C^128).  TR-1's own
       gamma construction re-run and its parity facts re-verified [R]; LD-B's
       beta_S per horn; {beta_S, Gamma_amb} = 0 at odd q; the t-parity rule
       (odd-grade monomial anticommutes with beta_S iff its timelike index
       count is odd) swept over every odd grade at both horns, exhaustive at
       grade 1; the volume-word K-parity flip; signature-true squares vs the
       closed form (-1)^(k(k-1)/2 + t); the transverse-symbol rule; both
       exemplar certificates; middle-half nilpotency (M^2 = 0, rank 64) and
       K-parity mixedness; the branch-flip witness (same component, opposite
       Krein-self-adjointness verdicts under M^dag = +/-M); a planted
       Krein-BREAKING control the classifier must flag and a planted
       PRESERVING control it must pass.

LEG 4  THE FREEZE SEAM (model face; FENCED — binds the lattice model).  The
       pole family D(m) = sigma_1 (x) P + m sigma_2 (x) I is Gamma-odd with
       graded trace 0 at machine zero along the sweep; the sigma_3 contrast
       moves it; operator SUMS of odd-grade elements stay Gamma-odd while
       PRODUCTS of two go Gamma-even (the sum-vs-product seam fact).

LEG 5  INSTRUMENTS RE-RUN.  Four subprocess re-runs with pinned agreement
       strings: dirac_spectral_flow_section.py, krein_spectral_flow_probe.py,
       the GB-1 probe ("VERDICT: GREEN (114 checks)"), the TR-1 probe
       ("90/90 checks pass").

LEG 6  CERTIFIED ABSENCES (planted-positive controls on every absence).
       (a) "middle form"/"middle-form" absent from lab/sources/*.md;
       (b) the result phrasings absent repo-wide outside this arc's files;
       (c) REQUIRED-PRESENT: the vg_v8_t5 prior-art line (attribution pin).

LEG 7  ARTIFACT BINDING.  SHA-pinned verdict table, closed verdict
       vocabulary, claim-ceiling strings, the register-title quote, both
       kill-target quotes.

--selftest: verifies the CLEAN BASELINE FIRST (count pinned) and aborts red;
then 10 mutations, each corrupting machinery or a reference (never a check),
each REQUIRED to be caught by its targeted check via a genuine [FAIL]; a
crash is CRASH-NOT-DETECTION; an untargeted catch is INCIDENTAL-NOT-TARGETED;
baseline re-verified after.  Exit 0 iff green.  Tolerances: all load-bearing
comparisons are exact-integer-valued (norm thresholds 1e-9 against violations
of integer size), so no tolerance can absorb a plant.
"""

from __future__ import annotations

import copy
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from math import comb

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PY = sys.executable

ARTIFACT = ("lab/active-research/joe-directed/grading-bridge/"
            "ds1-the-stock-sits-at-the-pole-and-waits-on-the-reality-map-2026-08-17.md")

EXPECTED_CHECKS = 107          # pinned independently of the live run counter
TABLE_SHA = "e01e8d5262d2976ec8c37064e4b6154af19674617d9a78482afbfc7bd30583ce"

GB1 = "lab/active-research/joe-directed/grading-bridge/gb1-the-bridge-is-one-angle-and-one-missing-arrow-2026-08-17.md"
TR1 = "lab/active-research/joe-directed/spectral-transport/tr1-transport-and-selection-are-opposite-parities-2026-08-17.md"
RSC1 = "lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md"
RW1 = "lab/active-research/joe-directed/rwall/rw1-zero-locus-steers-not-hosts-2026-08-17.md"
WB1 = "lab/active-research/joe-directed/wall-bill/wb1-crossing-is-a-sector-datum-r-cannot-supply-2026-08-17.md"
LDB = "lab/active-research/joe-directed/lens-digs/ldb-bit2-direction-and-krein-parity-2026-08-17.md"
SN1 = "lab/active-research/joe-directed/majorana-126-neutrino/sn1-observed-neutrino-mass-pencil-2026-08-16.md"
ST1 = "lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md"
UPR = "lab/process/upgrade-program-register.yaml"
CRR = "lab/process/correction-registry.yaml"
SCR = "lab/sources/source-claim-register.yaml"
HOM = "lab/process/homonym-register.yaml"
EXT1112 = "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"
EXT9 = "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
BASECAT = "lab/methods/gu-base-categories.md"
INSTR = "tests/function-space-ext/dirac_spectral_flow_section.py"
KPROBE = "tests/function-space-ext/krein_spectral_flow_probe.py"
GB1P = "tests/channel-swings/joe_directed_gb1_the_bridge_is_one_angle_and_one_missing_arrow.py"
TR1P = "tests/channel-swings/joe_directed_tr1_transport_and_selection_are_opposite_parities.py"
VG = "tests/big-swing/vg_v8_t5_map_attempt.py"


# --------------------------------------------------------------- machinery
def default_cfg() -> dict:
    return {
        # LEG 1 pins: (file, line, substring)
        "pins": [
            # PINS REFRESHED 2026-08-17 (integrator): register items closed
            # with receipts above this row shifted :270/:271 -> :321/:322.
            (UPR, 321, "- id: GB1-SIGMA2-DIRECTION-SUPPLY"),
            (UPR, 322, "The W3 missing arrow: a source-native supply of the Gamma-odd, Krein-breaking mass direction"),
            (UPR, 322, "the Gamma-odd stock is exactly the class-2 rows (odd-k epsilon directions)"),
            (UPR, 322, "If the carrier offers no such direction, W3 dies at this arrow"),
            (UPR, 326, "shop TR-1's class-2 inventory first"),
            (GB1, 396, "Link D — THE MISSING ARROW (exactly one, typed)"),
            (GB1, 397, "MISSING-ARROW-W3-DIRECTION"),
            (GB1, 397, "a source-attested or repository-"),
            (GB1, 400, "Krein-breaking, i.e. anticommuting with BOTH the kinetic symbol and the"),
            (GB1, 279, "residual `2|cos(phi)|`"),
            (GB1, 286, "canon-graded charge iff the exit is Krein-only"),
            (TR1, 358, "Λ^k, k odd — Λ¹, Λ³, Λ⁵, **Λ⁷_± (the source's chirality mechanism)**"),
            (TR1, 365, "**The parity theorem.**"),
            (TR1, 419, "hence `tr(Γ P_<0) = 0` — not conserved:"),
            (TR1, 441, "**For class-2 families the count is a kernel index or it is"),
            (TR1, 558, "- **TB-4 — ENDPOINT EXISTENCE.**"),
            (TR1, 560, "the induced form has rank ≤ 128 on"),
            (TR1, 697, "shop in: the Γ-odd stock is exactly the class-2 rows of §3.2 (odd-k ε"),
            (TR1, 400, "A SINGLE middle-form direction is therefore a nilpotent one-way map between"),
            (TR1, 113, "(self-adjoint D, unitary Hermitian Gamma) — the count object"),
            (RSC1, 341, "zeta_+ = Omega^1(S_+) = V (x) S_+ = S_-  (+)  R^(+)      896 = 64 + 832"),
            (RSC1, 395, "Lam^3   |   0   ,   1    |       1       |   0   ,   2   ||   1   ,   4"),
            (RSC1, 444, "`rank ≤ 2·64 = 128`, at least `832 − 64 = 768` directions of `R` stay"),
            (RSC1, 604, "RS-1  ambient gamma-traceless  V_14 (x) S_+-  = R^(+-)   dim 832"),
            (RW1, 276, "- **W3 — the grading bridge (measured, and it is the sharpest item).**"),
            (RW1, 839, "first-class result of the same rank as this join."),
            (LDB, 188, "`K = eta_V (x) beta_S` with `beta_S` the"),
            (LDB, 189, "product of the spacelike gammas"),
            (LDB, 211, "`{K, chi} = 0` exactly at odd `q`"),
            (SN1, 208, "does not supply the global Hodge/Krein/reality adjoint"),
            (SN1, 214, "Majorana status: UNDEFINED_WITHOUT_REALITY_MAP"),
            (SCR, 940, "verbatim: dslash_A psi_L(y) = (R(y)/4) psi_R(y)"),
            (ST1, 456, "the class-2 insertion count must be ODD"),
            (WB1, 9, "RELOCATED to an external Z/2 sector datum"),
        ],
        # AIM REFRESHED 2026-08-17 (integrator): the register title row this
        # near-miss control targets moved :271 -> :322; the control stays
        # aimed at the live row so its no-match keeps meaning something.
        "planted_negative_pin": (UPR, 322, "the carrier supplies the direction unconditionally"),
        # horns: index sets (4d = 0..3, internal = 4..13)
        "horns": {
            "(9,5)": {"space": [0, 1, 2] + list(range(4, 10)), "time": [3] + list(range(10, 14))},
            "(7,7)": {"space": [0] + list(range(4, 10)), "time": [1, 2, 3] + list(range(10, 14))},
        },
        "odd_grades": [1, 3, 5, 7, 9, 11, 13],
        # closed form for the signature-true monomial square sign
        "square_sign": lambda k, t: (-1) ** (k * (k - 1) // 2 + t),
        # census: number of grade-k monomials with timelike count of given parity
        "census": lambda p, q, k, parity: sum(
            comb(p, k - t) * comb(q, t)
            for t in range(0, min(k, q) + 1)
            if k - t <= p and t % 2 == parity),
        # exemplars: index tuples (grade-7 and grade-3), each with exactly one
        # timelike index (10) at BOTH horns and no 4d index
        "exemplar7": [4, 5, 6, 7, 8, 9, 10],
        "exemplar3": [4, 5, 10],
        # freeze-seam lattice family: the pole mass direction (sigma_2)
        "pole_mass_pauli": "s2",
        "contrast_mass_pauli": "s3",
        # subprocess re-runs: (path, required stdout substring, expect exit 0)
        # GB-1's probe: at DS-1's landing it read 114/1 (DS-1's mount-required
        # artifact tripped GB-1's L5-dest-artifact uniqueness pin — deviation
        # D5 in the artifact).  The owed pin refresh was applied by the
        # integrator on 2026-08-17 (GB-1's uniqueness check now names the
        # DS-1 sibling explicitly), so GB-1 is pinned GREEN again here; any
        # OTHER GB-1 movement still fails loudly.
        "subprocs": [
            (INSTR, "hard asserts passed: 20", True),
            (KPROBE, "VERDICT: in this finite-Galerkin model", True),
            (GB1P, "VERDICT: GREEN (114 checks)", True),
            (TR1P, "90/90 checks pass", True),
        ],
        # absence scans
        "absence_sources_tokens": ["middle form", "middle-form"],
        "absence_repo_tokens": ["K-parity-mixed", "signature-true square",
                                "sits at the pole and waits on the reality map"],
        "prior_art_pin": (VG, 493, "odd-timelike-count channel is P-ODD"),
        "artifact": ARTIFACT,
        "table_sha": TABLE_SHA,
        "verdict_vocab": {
            "ENUM": "EIGHT-ROWS-SEVEN-GRADES-ALL-REPO-DERIVED-AT-DIRECTION-GRADE",
            "POLE": "RESIDUAL-IDENTICALLY-ZERO-WHOLE-CLASS-AT-KREIN-ONLY-POLE",
            "KPAR": "TIMELIKE-PARITY-COMPONENTWISE-EVERY-ROW-MIXED-STOCK-NONEMPTY",
            "KREIN": "CONDITIONAL-UNDEFINED-WITHOUT-REALITY-MAP",
            "GAP": "TB4-O2-BITE-PURE-CROSS-ROWS-ONLY-SQUARES-PLUS-AT-3-MOD-4",
            "SEAM": "CONSISTENT-FREEZE-ROUTES-TO-KERNEL-INDEX-FACE",
            "SHOP": "CONDITIONAL-NOT-PAID-NOT-DEAD-NO-KILL",
        },
        "ceiling_strings": [
            "No claim status moves",
            "bit 2 stays the selector, OPEN",
            "SHOPPED TO A CONDITIONAL — NOT ARROW-PAID, NOT ARROW-DIES, NO KILL",
            "MISSING-ARROW-W3-DIRECTION",
            "finding either unsuppliable would be a",
            "UNDEFINED_WITHOUT_REALITY_MAP",
        ],
    }


class Run:
    def __init__(self) -> None:
        self.results: list[tuple[bool, str, str]] = []

    def check(self, cid: str, cond: bool, msg: str) -> bool:
        tag = "PASS" if cond else "FAIL"
        print(f"[{tag}] {cid} {msg}")
        self.results.append((bool(cond), cid, msg))
        return bool(cond)

    @property
    def n(self) -> int:
        return len(self.results)

    @property
    def failures(self) -> list[str]:
        return [cid for ok, cid, _ in self.results if not ok]


def read_lines(rel: str) -> list[str]:
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read().splitlines()


def pin_ok(rel: str, line_no: int, needle: str) -> bool:
    lines = read_lines(rel)
    return line_no - 1 < len(lines) and needle in lines[line_no - 1]


# ------------------------------------------------------- Clifford machinery
def cl14_gammas() -> list[np.ndarray]:
    """TR-1 LEG 5's construction, re-run: 14 anticommuting Hermitian
    involutions on C^128 (Pauli Kronecker)."""
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    eye = np.eye(2, dtype=complex)
    gs = []
    for a in range(7):
        for s in (s1, s2):
            ops = [s3] * a + [s] + [eye] * (7 - a - 1)
            g = ops[0]
            for o in ops[1:]:
                g = np.kron(g, o)
            gs.append(g)
    return gs


def prod(ms: list[np.ndarray]) -> np.ndarray:
    out = ms[0]
    for m in ms[1:]:
        out = out @ m
    return out


def nrm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a))


def classify_krein(m: np.ndarray, k: np.ndarray) -> tuple[bool, bool]:
    """(breaks if realized self-adjoint, breaks if realized anti-self-adjoint).
    For M realized with M^dag = M:   Krein-s.a.  <=>  [M, K] = 0.
    For M realized with M^dag = -M:  Krein-s.a.  <=>  {M, K} = 0.
    The REALIZATION is the reality map's call (SN-1) — this classifier only
    types the two branches; it cannot and does not pick one."""
    commut = nrm(m @ k - k @ m)
    anti = nrm(m @ k + k @ m)
    return (commut > 1e-9, anti > 1e-9)


# ---------------------------------------------------------------- LEG 1
def leg1(run: Run, cfg: dict) -> None:
    print("=" * 78)
    print("LEG 1  QUOTE FIDELITY (byte pins at cited lines)")
    for i, (rel, ln, needle) in enumerate(cfg["pins"]):
        run.check(f"L1-pin-{i:02d}", pin_ok(rel, ln, needle),
                  f"{rel}:{ln} contains {needle[:48]!r}")
    rel, ln, needle = cfg["planted_negative_pin"]
    run.check("L1-planted-neg", not pin_ok(rel, ln, needle),
              "planted NEGATIVE pin is correctly absent (pin machinery has power)")


# ---------------------------------------------------------------- LEG 2
def leg2(run: Run, cfg: dict) -> None:
    print("=" * 78)
    print("LEG 2  CLASS / CENSUS ARITHMETIC (exact integers)")
    eps_cls = {k: (2 * k) % 4 for k in range(15)}
    run.check("L2-class2", all(eps_cls[k] == 2 for k in cfg["odd_grades"]),
              "[R TR-1] every odd eps grade has Z/4 class 2")
    run.check("L2-class0", eps_cls[0] == 0 and eps_cls[14] == 0 and eps_cls[2] == 0,
              "[R TR-1] Lambda^0 / Lambda^2 / Lambda^14 are class 0 (not in the shop)")
    census = cfg["census"]
    expected = {  # (horn, k) -> (anti = t odd, comm = t even); artifact section 4.2
        ("(9,5)", 1): (5, 9), ("(9,5)", 3): (190, 174), ("(9,5)", 5): (991, 1011),
        ("(9,5)", 7): (1716, 1716), ("(9,5)", 9): (1011, 991),
        ("(9,5)", 11): (174, 190), ("(9,5)", 13): (9, 5),
        ("(7,7)", 1): (7, 7), ("(7,7)", 3): (182, 182), ("(7,7)", 5): (1001, 1001),
        ("(7,7)", 7): (1716, 1716), ("(7,7)", 9): (1001, 1001),
        ("(7,7)", 11): (182, 182), ("(7,7)", 13): (7, 7),
    }
    for hname, h in cfg["horns"].items():
        p, q = len(h["space"]), len(h["time"])
        for k in cfg["odd_grades"]:
            na = census(p, q, k, 1)
            nc = census(p, q, k, 0)
            ok = (na, nc) == expected[(hname, k)] and na + nc == comb(14, k)
            run.check(f"L2-census-{hname}-{k}", ok,
                      f"{hname} k={k}: anti={na} comm={nc} (sum={comb(14, k)})")
    run.check("L2-nonempty",
              all(census(len(h["space"]), len(h["time"]), k, 1) > 0
                  and census(len(h["space"]), len(h["time"]), k, 0) > 0
                  for h in cfg["horns"].values() for k in cfg["odd_grades"]),
              "every odd grade is K-parity-MIXED with NONEMPTY sigma_2 stock at both horns")
    sq = cfg["square_sign"]
    run.check("L2-square-mod4",
              all((sq(k, 1) == 1) == (k % 4 == 3) for k in cfg["odd_grades"]),
              "sigma_2-stock (t odd) squares +1 exactly at grades k = 3 mod 4 ({3,7,11})")
    planted_false = [
        eps_cls[7] == 0,                                   # 'middle grade is class 0'
        census(9, 5, 1, 1) == 0,                           # 'Lambda^1 sigma_2 stock empty at (9,5)'
        census(9, 5, 7, 1) == comb(14, 7),                 # 'Lambda^7 is K-homogeneous'
        sq(1, 1) == 1,                                     # 'k=1 sigma_2 components square +1'
        sq(7, 0) == 1,                                     # 't-even middle components square +1'
    ]
    run.check("L2-planted-false", not any(planted_false),
              "5 planted false propositions each observed False")


# ---------------------------------------------------------------- LEG 3
def leg3(run: Run, cfg: dict) -> None:
    print("=" * 78)
    print("LEG 3  Cl(14) INSTRUMENT (exact identities on C^128; fiber algebra, FENCED)")
    g = cl14_gammas()
    dim = 128
    eye = np.eye(dim)
    rel_ok = all(nrm(g[i] @ g[j] + g[j] @ g[i] - (2.0 if i == j else 0.0) * eye) < 1e-9
                 for i in range(14) for j in range(i, 14))
    run.check("L3-clifford", rel_ok, "{g_i, g_j} = 2 delta_ij on C^128 (TR-1's construction)")
    gamb = 1j * prod(g)
    run.check("L3-gamb", nrm(gamb - gamb.conj().T) < 1e-9 and nrm(gamb @ gamb - eye) < 1e-9,
              "Gamma_amb Hermitian involution (graded objects non-vacuous)")
    # [R] TR-1 LEG 5 parity facts, re-run on the same construction
    ins07 = prod(g[4:11])
    ins43 = prod(g[:4] + g[4:7])
    ins2 = prod(g[4:6])
    g4 = prod(g[:4])
    run.check("L3-R-tr1", nrm(ins07 @ gamb + gamb @ ins07) < 1e-9
              and nrm(ins43 @ gamb + gamb @ ins43) < 1e-9
              and nrm(ins07 @ g4 - g4 @ ins07) < 1e-9
              and nrm(ins2 @ gamb - gamb @ ins2) < 1e-9,
              "[R TR-1] (0,7)/(4,3) middle splits ambient-ODD and gamma_5-EVEN; 2-gamma class-0 commutes")
    for hname, h in cfg["horns"].items():
        sp, tm = h["space"], h["time"]
        p, q = len(sp), len(tm)
        beta = prod([g[i] for i in sp])
        run.check(f"L3-flip-{hname}", nrm(beta @ gamb + gamb @ beta) < 1e-9,
                  f"{hname}: {{beta_S, Gamma_amb}} = 0 (odd q — LD-B's parity, insertion face)")
        # exhaustive at grade 1
        ex_ok = all((nrm(g[a] @ beta + beta @ g[a]) < 1e-9) == (a in tm) for a in range(14))
        run.check(f"L3-k1-exhaustive-{hname}", ex_ok,
                  f"{hname}: ALL 14 grade-1 monomials: anticommute with beta_S iff timelike")
        # the t-parity rule swept over every odd grade, every feasible t
        rule_ok, gamma_ok = True, True
        for k in cfg["odd_grades"]:
            for t in range(0, min(k, q) + 1):
                j = k - t
                if j > p:
                    continue
                idx = sp[:j] + tm[:t]
                c = prod([g[a] for a in idx])
                anti = nrm(c @ beta + beta @ c) < 1e-9
                comm = nrm(c @ beta - beta @ c) < 1e-9
                if anti == comm or anti != (t % 2 == 1):
                    rule_ok = False
                if nrm(c @ gamb + gamb @ c) > 1e-9:
                    gamma_ok = False
        run.check(f"L3-trule-{hname}", rule_ok,
                  f"{hname}: t-parity rule holds at every odd grade, every feasible t")
        run.check(f"L3-godd-{hname}", gamma_ok,
                  f"{hname}: every sampled odd-grade component is Gamma_amb-ODD (residual 0: the pole is free)")
        # volume-word flip on a witness
        c1 = prod([g[a] for a in (sp[:0] + tm[:1])])  # one timelike gamma: anticommutes
        cdual = c1 @ gamb
        run.check(f"L3-hodge-{hname}",
                  nrm(c1 @ beta + beta @ c1) < 1e-9 and nrm(cdual @ beta - beta @ cdual) < 1e-9,
                  f"{hname}: multiplying by the volume word FLIPS the K-parity")
        # signature-true squares: time gammas get i (square -1)
        gt = [(1j * g[a] if a in tm else g[a]) for a in range(14)]
        sq_ok = True
        for k in cfg["odd_grades"]:
            for t in range(0, min(k, q) + 1):
                j = k - t
                if j > p:
                    continue
                idx = sp[:j] + tm[:t]
                ct = prod([gt[a] for a in idx])
                if nrm(ct @ ct - cfg["square_sign"](k, t) * eye) > 1e-9:
                    sq_ok = False
        run.check(f"L3-squares-{hname}", sq_ok,
                  f"{hname}: signature-true monomial squares match (-1)^(k(k-1)/2 + t) at every (k, t)")
        # exemplar certificates
        for name, idx in (("exemplar7", cfg["exemplar7"]), ("exemplar3", cfg["exemplar3"])):
            k = len(idx)
            t = sum(1 for a in idx if a in tm)
            c = prod([g[a] for a in idx])
            ct = prod([gt[a] for a in idx])
            cert = (t % 2 == 1
                    and nrm(c @ gamb + gamb @ c) < 1e-9
                    and nrm(c @ beta + beta @ c) < 1e-9
                    and nrm(ct @ ct - eye) < 1e-9
                    and all(nrm(c @ g[n] + g[n] @ c) < 1e-9 for n in range(4) if n not in idx))
            run.check(f"L3-{name}-{hname}", cert,
                      f"{hname} {name} {idx}: Gamma-odd, K-anticommuting, square +1, "
                      "anticommutes with every base-normal symbol")
    # middle-half nilpotency + K-mixedness (horn (9,5) beta)
    h = cfg["horns"]["(9,5)"]
    beta = prod([g[i] for i in h["space"]])
    c7 = prod([g[a] for a in cfg["exemplar7"]])
    pplus = 0.5 * (np.eye(dim) + gamb)
    m_half = c7 @ pplus
    run.check("L3-nilpotent", nrm(m_half @ m_half) < 1e-9
              and np.linalg.matrix_rank(m_half, tol=1e-9) == 64,
              "[R TR-1 3.3 face] a half-projected middle direction is NILPOTENT (M^2 = 0), rank 64")
    run.check("L3-mixed", nrm(m_half @ beta - beta @ m_half) > 1e-6
              and nrm(m_half @ beta + beta @ m_half) > 1e-6,
              "duality-half middle direction has NONZERO commutator AND anticommutator with K (parity-entangled)")
    # branch-flip witness: same component, opposite Krein-s.a. verdicts under M^dag = +/-M
    a_h = 1j * c7                      # Hermitian realization of the k=7, t=1 component
    b_ah = c7                          # anti-Hermitian realization of the SAME component
    run.check("L3-witness-herm", nrm(a_h - a_h.conj().T) < 1e-9
              and nrm(b_ah + b_ah.conj().T) < 1e-9,
              "the two realizations of the witness component are Hermitian / anti-Hermitian "
              "(the branch pair is well-formed, not vacuous)")
    sa_breaks = nrm(beta @ a_h @ beta - a_h.conj().T) > 1e-6      # K M K vs M^dag (K^2 = I)
    asa_breaks = nrm(beta @ b_ah @ beta - b_ah.conj().T) > 1e-6
    run.check("L3-branch-flip", sa_breaks and not asa_breaks,
              "branch flip: the SAME K-anticommuting component BREAKS Krein-s.a. realized "
              "Hermitian and PRESERVES it realized anti-Hermitian — the verdict is the "
              "reality map's (SN-1), not the algebra's")
    # planted controls the classifier must handle (self-adjoint branch)
    t_odd = 1j * c7                    # Hermitian, K-anticommuting  -> must flag BREAKS
    idx_even = h["space"][:5] + h["time"][:2]      # k=7, t=2: K-commuting
    c_even = prod([g[a] for a in idx_even])
    t_even = 1j * c_even
    run.check("L3-plant-herm", nrm(t_even - t_even.conj().T) < 1e-9,
              "the planted preserving control's Hermitian realization is well-formed")
    br_odd = classify_krein(t_odd, beta)[0]
    br_even = classify_krein(t_even, beta)[0]
    run.check("L3-planted-breaking", br_odd,
              "planted Krein-BREAKING control (t odd, Hermitian branch): classifier FLAGS it")
    run.check("L3-planted-preserving", not br_even,
              "planted Krein-PRESERVING control (t even, Hermitian branch): classifier PASSES it")


# ---------------------------------------------------------------- LEG 4
def leg4(run: Run, cfg: dict) -> None:
    print("=" * 78)
    print("LEG 4  THE FREEZE SEAM (lattice model face; binds the model)")
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    pauli = {"s1": s1, "s2": s2, "s3": s3}
    n = 24
    a = 2 * np.pi / n
    p = np.zeros((n, n), dtype=complex)
    for j in range(n):
        p[j, (j + 1) % n] += -1j / (2 * a)
        p[j, (j - 1) % n] += 1j / (2 * a)
    p = 0.5 * (p + p.conj().T)
    inn = np.eye(n, dtype=complex)
    gamma = np.kron(s3, inn)

    def n_minus(d: np.ndarray) -> float:
        w, v = np.linalg.eigh(d)
        sel = v[:, w < -1e-9]
        return float(np.real(np.trace(sel.conj().T @ gamma @ sel)))

    mp = pauli[cfg["pole_mass_pauli"]]
    mc = pauli[cfg["contrast_mass_pauli"]]
    frozen = 0.0
    odd_ok = True
    for m in (0.0, 0.35, 0.8, 1.5):
        d = np.kron(s1, p) + m * np.kron(mp, inn)
        if nrm(d @ gamma + gamma @ d) > 1e-9:
            odd_ok = False
        frozen = max(frozen, abs(n_minus(d)))
    run.check("L4-pole-odd", odd_ok,
              "the pole family sigma_1 (x) P + m sigma_2 (x) I is Gamma-ODD at every m")
    run.check("L4-freeze", frozen < 1e-9,
              f"THE FREEZE at the pole: tr(Gamma P_<0) = 0 along the sweep (max {frozen:.1e})")
    moved = abs(n_minus(np.kron(s1, p) + 1.5 * np.kron(mc, inn)))
    run.check("L4-contrast", moved > 0.5,
              f"[R LD-A shape] the Gamma-ALIGNED mass MOVES the trace ({moved:.3f} at m=1.5)")
    # sum-vs-product seam fact on the Cl(14) side
    g = cl14_gammas()
    gamb = 1j * prod(g)
    ca = prod([g[a] for a in (4, 5, 10)])
    cb = prod([g[a] for a in (6, 7, 11)])
    run.check("L4-sum-odd", nrm((ca + cb) @ gamb + gamb @ (ca + cb)) < 1e-9,
              "operator SUM of two odd-grade elements stays Gamma-odd (multi-insertion walls stay class-2)")
    run.check("L4-prod-even", nrm((ca @ cb) @ gamb - gamb @ (ca @ cb)) < 1e-9,
              "operator PRODUCT of two odd-grade elements is Gamma-EVEN (TR1-COMPOSITE-PARITY's "
              "flank concerns insertion counts in pairings — a DIFFERENT composition)")


# ---------------------------------------------------------------- LEG 5
def leg5(run: Run, cfg: dict) -> None:
    print("=" * 78)
    print("LEG 5  INSTRUMENTS RE-RUN (subprocess, pinned agreement strings)")
    for rel, needle, expect_green in cfg["subprocs"]:
        try:
            r = subprocess.run([PY, os.path.join(ROOT, rel)], cwd=ROOT,
                               capture_output=True, text=True, timeout=600)
            ok = needle in r.stdout and (r.returncode == 0 or not expect_green)
        except Exception as exc:                      # noqa: BLE001
            ok = False
            print(f"       (subprocess exception: {exc})")
        want = "exit 0 and" if expect_green else "(pinned post-landing state)"
        run.check(f"L5-{os.path.basename(rel)}", ok,
                  f"{rel}: {want} stdout contains {needle!r}")


# ---------------------------------------------------------------- LEG 6
def scan_files(files: list[str], tokens: list[str]) -> list[tuple[str, str]]:
    hits = []
    for rel in files:
        try:
            with open(rel, encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except OSError:
            continue
        for tok in tokens:
            if tok in text:
                hits.append((rel, tok))
    return hits


def repo_md_py(exclude_frags: list[str]) -> list[str]:
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in ("_local", ".git", ".lake", "node_modules")]
        for fn in filenames:
            if fn.endswith((".md", ".py")):
                full = os.path.join(dirpath, fn)
                if any(frag in full for frag in exclude_frags):
                    continue
                out.append(full)
    return out


def leg6(run: Run, cfg: dict, tmp: str) -> None:
    print("=" * 78)
    print("LEG 6  CERTIFIED ABSENCES (planted-positive controls) + attribution pin")
    src_dir = os.path.join(ROOT, "lab", "sources")
    src_files = [os.path.join(src_dir, f) for f in os.listdir(src_dir) if f.endswith(".md")]
    hits = scan_files(src_files, cfg["absence_sources_tokens"])
    run.check("L6-source-absence", not hits,
              f"'middle form'/'middle-form': ZERO hits over {len(src_files)} lab/sources files "
              "(the middle-form DIRECTION is repo-derived, not source-named — deviation D1)")
    planted = os.path.join(tmp, "planted-source.md")
    with open(planted, "w", encoding="utf-8") as f:
        f.write("a planted middle form sentence\n")
    run.check("L6-source-planted", bool(scan_files([planted], cfg["absence_sources_tokens"])),
              "planted positive: the detector flags a synthetic source file carrying the token")
    near = os.path.join(tmp, "nearmiss-source.md")
    with open(near, "w", encoding="utf-8") as f:
        f.write("a middling formation, not the token\n")
    run.check("L6-source-nearmiss", not scan_files([near], cfg["absence_sources_tokens"]),
              "planted near-miss: 'middling formation' is NOT flagged")
    self_ex = ["ds1-the-stock-sits-at-the-pole", "joe_directed_ds1_the_stock_sits_at_the_pole"]
    corpus = repo_md_py(self_ex)
    hits2 = scan_files(corpus, cfg["absence_repo_tokens"])
    wave_frags = (os.path.join("lab", "active-research", "joe-directed"),
                  os.path.join("tests", "channel-swings"))
    outside = [h for h in hits2 if not any(w in h[0] for w in wave_frags)]
    inside = [h for h in hits2 if any(w in h[0] for w in wave_frags)]
    if inside:
        print(f"       SAME-WAVE (reported, not failed; concurrent sibling arcs — "
              f"GB-1's precedent): {sorted(set(os.path.relpath(p, ROOT) for p, _ in inside))}")
    run.check("L6-novelty-absence", not outside,
              f"result phrasings: ZERO hits over {len(corpus)} repo files outside the wave trees "
              f"(SELF-EX; wave-tree hits reported, not failed)"
              + (f" — hits: {outside[:3]}" if outside else ""))
    planted2 = os.path.join(tmp, "planted-repo.md")
    with open(planted2, "w", encoding="utf-8") as f:
        f.write("the stock is K-parity-mixed here\n")
    run.check("L6-novelty-planted", bool(scan_files([planted2], cfg["absence_repo_tokens"])),
              "planted positive: the phrasing detector fires on a synthetic file")
    near2 = os.path.join(tmp, "nearmiss-repo.md")
    with open(near2, "w", encoding="utf-8") as f:
        f.write("a signature-truthful square and a K-parity mix, neither the token\n")
    run.check("L6-novelty-nearmiss", not scan_files([near2], cfg["absence_repo_tokens"]),
              "planted near-miss: adjacent phrasings are NOT flagged")
    rel, ln, needle = cfg["prior_art_pin"]
    run.check("L6-prior-art-present", pin_ok(rel, ln, needle),
              f"REQUIRED-PRESENT attribution pin: {rel}:{ln} carries the odd-timelike prior-art line")


# ---------------------------------------------------------------- LEG 7
def leg7(run: Run, cfg: dict) -> None:
    print("=" * 78)
    print("LEG 7  ARTIFACT BINDING (verdict-evidence consistency)")
    art_path = os.path.join(ROOT, cfg["artifact"])
    ok_exists = os.path.exists(art_path)
    run.check("L7-artifact-exists", ok_exists, f"{cfg['artifact']} exists")
    if not ok_exists:
        return
    with open(art_path, encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"<!-- DS1-TABLE-BEGIN -->(.*?)<!-- DS1-TABLE-END -->", text, re.S)
    run.check("L7-table-found", m is not None, "machine verdict table present between markers")
    if not m:
        return
    block = m.group(1)
    sha = hashlib.sha256(block.encode("utf-8")).hexdigest()
    run.check("L7-table-sha", sha == cfg["table_sha"],
              f"table SHA-256 pinned ({sha[:12]}... == {cfg['table_sha'][:12]}...)")
    rows = {}
    for line in block.strip().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[0] not in ("id", "") and not set(cells[0]) <= set("-"):
            rows[cells[0]] = cells[2]
    vocab = cfg["verdict_vocab"]
    run.check("L7-verdicts", rows == vocab,
              "all seven verdicts present and byte-equal to the closed vocabulary "
              "(SHOP = CONDITIONAL-NOT-PAID-NOT-DEAD-NO-KILL)")
    for i, s in enumerate(cfg["ceiling_strings"]):
        run.check(f"L7-ceiling-{i}", s in text, f"claim-ceiling / kill-target string present: {s[:44]!r}")
    reg_title = ("the Gamma-odd stock is exactly the class-2 rows (odd-k epsilon directions); "
                 "the Krein leg of each candidate is reality-map-gated (SN-1)")
    run.check("L7-register-quote", reg_title in text,
              "the register title's inventory sentence is quoted verbatim in the artifact")


# --------------------------------------------------------------- drivers
LEGS = {"1": leg1, "2": leg2, "3": leg3, "4": leg4, "5": leg5, "6": leg6, "7": leg7}


def run_legs(cfg: dict, which: list[str]) -> Run:
    run = Run()
    tmp = tempfile.mkdtemp(prefix="ds1_probe_")
    try:
        for w in which:
            fn = LEGS[w]
            if w == "6":
                fn(run, cfg, tmp)
            else:
                fn(run, cfg)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return run


def run_live() -> int:
    cfg = default_cfg()
    run = run_legs(cfg, ["1", "2", "3", "4", "5", "6", "7"])
    print("=" * 78)
    print(f"RESULT: {run.n - len(run.failures)}/{run.n} checks pass; {len(run.failures)} failures {run.failures}")
    if run.n != EXPECTED_CHECKS:
        print(f"[FAIL] CHECK-COUNT check count {run.n} != pinned {EXPECTED_CHECKS}")
        return 1
    return 0 if not run.failures else 1


# ------------------------------------------------------- selftest mutations
def mutations() -> list[tuple[str, str, list[str], object]]:
    """(name, required failing check id prefix, legs to run, cfg mutator).
    Every mutation corrupts MACHINERY or a REFERENCE, never a predicate."""

    def m1(cfg):
        rel, _ln, needle = cfg["pins"][6]          # the MISSING-ARROW pin
        cfg["pins"][6] = (rel, 999, needle)        # wrong line number

    def m2(cfg):
        cfg["census"] = lambda p, q, k, parity: sum(
            comb(p, k) * comb(q, t)                # broken binomial (reference corrupted)
            for t in range(0, min(k, q) + 1) if t % 2 == parity)

    def m3(cfg):
        cfg["horns"]["(9,5)"]["space"] = cfg["horns"]["(9,5)"]["space"][:-1]  # beta_S loses a gamma

    def m4(cfg):
        cfg["square_sign"] = lambda k, t: (-1) ** (k * (k - 1) // 2 + t + 1)  # sign flipped

    def m5(cfg):
        cfg["_corrupt_gamma"] = True               # picked up by the harness below

    def m6(cfg):
        cfg["exemplar7"] = [4, 5, 6, 7, 8, 10, 11]  # t = 2: certificate must fail

    def m7(cfg):
        cfg["absence_sources_tokens"] = ["zzz-token-never-present"]  # detector defanged

    def m8(cfg):
        cfg["subprocs"] = [(INSTR, "hard asserts passed: 999", True)]  # pin string corrupted

    def m9(cfg):
        cfg["pole_mass_pauli"] = "s3"              # freeze family's mass matrix corrupted

    def m10(cfg):
        cfg["_flip_artifact"] = True               # contrary control: verdict flipped in a copy

    return [
        ("M1 pin line number", "L1-pin-06", ["1"], m1),
        ("M2 census binomial", "L2-census", ["2"], m2),
        ("M3 beta_S index set", "L3-", ["3"], m3),
        ("M4 square-sign form", "L2-square-mod4", ["2"], m4),
        ("M5 gamma construction", "L3-clifford", ["3"], m5),
        ("M6 exemplar indices", "L3-exemplar7", ["3"], m6),
        ("M7 absence detector", "L6-source-planted", ["6"], m7),
        ("M8 subprocess pin", "L5-", ["5"], m8),
        ("M9 freeze family", "L4-", ["4"], m9),
        ("M10 artifact verdict flip", "L7-", ["7"], m10),
    ]


def selftest() -> int:
    print("SELFTEST: verifying the CLEAN BASELINE FIRST")
    base = run_legs(default_cfg(), ["1", "2", "3", "4", "5", "6", "7"])
    if base.failures or base.n != EXPECTED_CHECKS:
        print(f"[ABORT] baseline not clean ({base.n} checks, failures {base.failures}) — "
              "a red baseline would make every mutation exit nonzero for the wrong reason")
        return 1
    print(f"baseline OK: {base.n}/{EXPECTED_CHECKS} green\n")

    global cl14_gammas                            # M5 corrupts the construction
    orig_gammas = cl14_gammas
    caught = 0
    for name, want_prefix, legs, mut in mutations():
        cfg = default_cfg()
        # deep-copy mutable structures so mutators cannot leak across runs
        cfg["pins"] = copy.deepcopy(cfg["pins"])
        cfg["horns"] = copy.deepcopy(cfg["horns"])
        mut(cfg)
        tmpdir = None
        if cfg.pop("_flip_artifact", False):
            tmpdir = tempfile.mkdtemp(prefix="ds1_flip_")
            src = os.path.join(ROOT, ARTIFACT)
            dst = os.path.join(tmpdir, "flipped.md")
            with open(src, encoding="utf-8") as f:
                text = f.read()
            with open(dst, "w", encoding="utf-8") as f:
                f.write(text.replace("CONDITIONAL-NOT-PAID-NOT-DEAD-NO-KILL", "ARROW-PAID"))
            cfg["artifact"] = os.path.relpath(dst, ROOT)
        if cfg.pop("_corrupt_gamma", False):
            def bad_gammas():
                gs = orig_gammas()
                gs[3] = gs[2].copy()               # duplicate generator: relations break
                return gs
            cl14_gammas = bad_gammas
        try:
            run = run_legs(cfg, legs)
            crashed = False
        except Exception as exc:                   # noqa: BLE001
            crashed = True
            run = None
            print(f"       (exception during mutated run: {exc})")
        finally:
            cl14_gammas = orig_gammas
            if tmpdir:
                shutil.rmtree(tmpdir, ignore_errors=True)
        if crashed:
            print(f"[SELFTEST-FAIL] {name}: CRASH-NOT-DETECTION")
            return 1
        hit = [cid for cid in run.failures if cid.startswith(want_prefix)]
        if not run.failures:
            print(f"[SELFTEST-FAIL] {name}: mutation NOT caught")
            return 1
        if not hit:
            print(f"[SELFTEST-FAIL] {name}: INCIDENTAL-NOT-TARGETED "
                  f"(failures {run.failures}, wanted prefix {want_prefix})")
            return 1
        caught += 1
        print(f"[SELFTEST-OK] {name}: caught by targeted {hit} (all failing: {run.failures})\n")

    print("re-verifying the clean baseline AFTER the mutations")
    base2 = run_legs(default_cfg(), ["1", "2", "3", "4", "5", "6", "7"])
    if base2.failures or base2.n != EXPECTED_CHECKS:
        print("[SELFTEST-FAIL] baseline dirty after mutations")
        return 1
    print(f"\nSELFTEST: {caught}/10 mutations caught, each via its targeted genuine [FAIL]; "
          "0 crash-only; 0 missed; baseline re-verified. exit 0")
    return 0


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    return run_live()


if __name__ == "__main__":
    sys.exit(main())
