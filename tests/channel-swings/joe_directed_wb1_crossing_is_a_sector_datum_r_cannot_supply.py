#!/usr/bin/env python3
r"""WB-1 probe: W1's crossing requirement for the VEV-orientation wall,
pinned and measured.

Pins and certifies
  lab/active-research/joe-directed/wall-bill/wb1-crossing-is-a-sector-datum-r-cannot-supply-2026-08-17.md

Five legs, each independently failing:

  LEG P  QUOTE FIDELITY.  Fifty (file, line, substring) pins byte-match the
         load-bearing sentences at their cited lines -- rung-2's T-DEG wording
         and frozen sector-input lines especially (prereg:51-52, probe:137-138,
         probe:271-273), RW-1's W1/P7/join-disposition lines, the source's
         quartic/quadratic/negative-curvature and decreased-VEV lines, the
         canon external rows, and the four prior-art loci (VG-V5 connected D,
         Kibble-Zurek steelman, adapter Z/2 sector datum, shard-cycle w_1).
         Carries a PLANTED NEGATIVE ("The orientation is a Z/3" must NOT match
         at rung-2 probe:272) so a matcher stuck at True is caught.

  LEG S  VEV-ORIENTATION SCAN (certified; the phi-side mirror of RW-1 LEG 2).
         Over the eight Weinstein primary surfaces: the VEV-FLIP family
         ("changes sign", "both orientations", "either sign", ... with a VEV
         co-token in a +-2-line window) scores ZERO; the VEV-NEGATIVE family
         scores ZERO; the VEV-MAGNITUDE family ("significantly above zero",
         "decreased vev") scores EXACTLY FIVE, all the same two one-sided
         utterances across surfaces (drafts:158, ucsd:244, extraction:138,
         register:923, register:1805).  A planted positive the detector is
         REQUIRED to flag and two planted near-misses it is required NOT to
         flag (family token without VEV co-token; VEV co-token without family
         token) certify the instrument.

  LEG C  EXACT COMPARATOR (sympy + numpy; FENCED -- binds the rung-2
         standard-field wall system only, prereg:43-45 transport fence):
         (a) the evenness identity: I(-phi) - I(phi) = -2 g(y) phi for
             ARBITRARY lambda(y), v(y), g(y); with g = 0 (the source-stated
             quartic + R-set quadratic class) the difference is identically
             zero, so NO R profile steering the even channel can prefer or
             force an orientation; the phi-odd rung-2 instrument term is
             REQUIRED to be flagged nonzero.
         (b) composite hosting inside one-signed R < 0 (R = -4(2+tanh y),
             exact: R <= -4): the chain-2 phi-kink m = tanh y hosts EXACTLY 1
             (mode sech y, integral of sech^2 = 2) while chain-1's
             m = R/4 = -(2+tanh y) hosts EXACTLY 0 (no zero); count =
             |winding| in both rows.  The crossing burden lives in phi.
         (c) the sector-parity identity: (strict sign alternations) mod 2 =
             [ends in different components], verified EXHAUSTIVELY over all
             sign sequences of length 2..12 (8,188 sequences) plus seeded
             random renderings with pinned ends and an equal-ends control;
             and the rung-2 winding functional (probe:173 reimplemented)
             consumes ONLY the endpoints (interior scramble invariance;
             endpoint flip sensitivity).  The crossing datum IS the sector
             datum.
         (d) even modulation lambda(y) = 1 + 0.3 tanh(y/2) on the rung-2
             grid: location spread > 1e-3 (steering works through the even
             channel) while E[-phi] - E[phi] == 0.0 EXACTLY (bitwise) for
             every shifted wall; the phi-odd tilt g y phi splits kink from
             antikink (> 1e-3).  Even steering selects location, never
             orientation.

  LEG R  RUNG-2 RE-RUN.  The repository's own instrument
         tests/channel-swings/rung2_dynamical_wall_selectability_probe.py
         re-run live: exit 0, "VERDICT: SECTOR-SUPPLIED", "provably cannot
         fix", "accessible rank 3" all present.

  LEG B  ARTIFACT BINDING.  Parses the machine table between the WB1-TABLE
         markers (six rows, closed verdict set), SHA-256 pins the block, and
         enforces verdict-evidence consistency (the selftest's CONTRARY
         CONTROL flips W1 to DISCHARGED-BY-RUNG2 and must be caught here).
         Also enforces the claim ceiling in the artifact's own text: "does
         not derive 3", the |winding| = 1 null and OPEN, the routing notice
         and classification, canonical_effect pending_integration, the
         currency-records section header, the CC-05 subtractive fence, and
         both gu-typed-objects blocks.

--selftest discipline (VERIFICATION.md "Probe and mutation-harness
discipline (adopted 2026-08-17)", all seven rules):
  * the CLEAN BASELINE is verified FIRST and a red baseline aborts;
  * the baseline check count is pinned independently (BASELINE_COUNT) and
    re-verified after the mutations;
  * every mutation corrupts MACHINERY or a REFERENCE, never a check's
    predicate;
  * a catch counts only via a genuine [FAIL] line -- a mutant that crashes is
    CRASH-NOT-DETECTION and fails; an incidental catch is
    INCIDENTAL-NOT-TARGETED and fails; overspill beyond the declared target
    set fails;
  * planted-positive controls guard every absence check, and tolerances are
    pinned so they cannot absorb the plants;
  * the failing check is printed for every mutation (rule 7);
  * exit 0 on success.

Read-only: the probe writes nothing into the repository.  Planted-control
corpora and the contrary-control artifact copy live in a temp directory and
are removed.  Deterministic; sympy + numpy + stdlib only.
"""
from __future__ import annotations

import hashlib
import itertools
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]

ARTIFACT = ("lab/active-research/joe-directed/wall-bill/"
            "wb1-crossing-is-a-sector-datum-r-cannot-supply-2026-08-17.md")
RW1 = "lab/active-research/joe-directed/rwall/rw1-zero-locus-steers-not-hosts-2026-08-17.md"
PREREG = "explorations/prereg-rung2-dynamical-wall-and-selectability-test-2026-07-29.md"
RUNG2 = "tests/channel-swings/rung2_dynamical_wall_selectability_probe.py"
DRAFTS = "papers/drafts/Transcript into the impossible.md"
EXTRACTION = "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"
REGISTER = "lab/sources/source-claim-register.yaml"
SYNTHESIS = "canon/external-by-structure-synthesis-RESULTS.md"
NN = "explorations/nielsen-ninomiya-domain-wall-records-as-rows-2026-07-10.md"
VGV5 = "explorations/big-swing-2026-07-06/VG-V5-breaking-coset-topology.md"
KZ = "explorations/time-as-finality-crosswalk/ten-perspective-steelman-live-dark-observer-sheaf-2026-07-15.md"
ADAPTER = "explorations/adapter-assumed-four-leg-swing-2026-07-19.md"
SHARD = "explorations/shard-cycle-prong1-geometry-2026-07-21.md"
PACKET = "explorations/decoupling-constructibility-packet-2026-08-12.md"

# ------------------------------------------------------------------ LEG P pins
PINS = [
    (RW1, 260, "W1 — a sign-crossing zero (the load-bearing missing item)"),
    (RW1, 427, "P7 — the existence condition for Wall-2 is already proved in the"),
    (RW1, 431, "is NOT proved: that domains of both orientations are realized"),
    (RW1, 457, "VEV-orientation (Z/2) domain walls inside the broken region, steered by"),
    (RW1, 458, "existence condition = the unfixable orientation Z/2 (P7)"),
    (RW1, 525, "TYPED-TARGET-VEV-ORIENTATION-WALL-R-STEERED"),
    (RW1, 267, "Status: OPEN,"),
    (PREREG, 44, "transferred to the `(9,5)` Krein / gimmel / `ker Gamma` carrier"),
    (PREREG, 46, "The triplet is **supplied**, inherited from Rung 1, and no result here derives"),
    (PREREG, 51, "Double-well potential `V(phi) = lambda (phi^2 - v^2)^2`; boundary sector"),
    (PREREG, 52, "`phi(-L) = -v`, `phi(+L) = +v`"),
    (PREREG, 63, "unselected because `phi -> -phi` is an exact symmetry of the potential, so kink"),
    (PREREG, 64, "and antikink are exactly degenerate"),
    (PREREG, 95, "linear-gradient term makes location selectable"),
    (PREREG, 109, "|winding| = 1**: generic single-defect energetics select a unit wall"),
    (PREREG, 111, "has demonstrated hosting, not selection (the Jackiw-Rebbi standard"),
    (RUNG2, 137, "phi = sign * V * np.sign(x)          # sector-respecting seed, not a solution"),
    (RUNG2, 138, "phi[0], phi[-1] = -sign * V, sign * V"),
    (RUNG2, 168, "A = D + np.diag(y * phi)"),
    (RUNG2, 173, "winding = int(np.sign(phi[-1]) - np.sign(phi[0])) // 2"),
    (RUNG2, 222, "(This same term also breaks translation invariance; noted, not hidden.)"),
    (RUNG2, 271, "So a dynamical source at this rung determines the PROFILE but not the"),
    (RUNG2, 272, "sector, the location, or the orientation.  The orientation is a Z/2 the"),
    (RUNG2, 273, "action provably cannot fix, which is the SAME TYPE of object as the"),
    (DRAFTS, 146, "They both have a Klein Gordon kinetic term. They both have a quartic term."),
    (DRAFTS, 149, "So if your curvature is negative, now you start to get a Mexican hat potential"),
    (DRAFTS, 149, "which is a quadratic"),
    (DRAFTS, 158, "exactly three families of chiral fermions if you have a decreased VEV"),
    (EXTRACTION, 138, "sub-fields of ϖ to values significantly above zero"),
    (REGISTER, 913, "non-chiral total theory splits at the emergent level into two separate"),
    (REGISTER, 922, "pulling the various sub-fields of varpi to values"),
    (REGISTER, 940, "dslash_A psi_L(y) = (R(y)/4) psi_R(y)"),
    (REGISTER, 2336, "negative curvature gives the Mexican hat"),
    (REGISTER, 1611, "It coaxes this thing out of the vacuum that then plays the role of a fundamental mass scale"),
    (REGISTER, 1613, "drops sufficiently, then a Dirac type operator decouples into Weyl type operators"),
    (REGISTER, 1638, "we have a non-chiral world where there were two chiral"),
    ("CANON.md", 135, "net chiral index = flux number (any integer, odd for odd flux)"),
    ("CANON.md", 136, "Net chiral spectral flow 0 for self-adjoint, chirality-odd, Krein-self-adjoint Fredholm families"),
    ("CANON.md", 139, "interior-even + external-topological-index"),
    (SYNTHESIS, 60, "any ODD generation count is necessarily external"),
    (NN, 90, "it rides SG4, exactly as the carrier bit does"),
    (NN, 107, "Not a derivation of three (or any) generations"),
    (VGV5, 75, "every orbit is open, D is connected (it retracts, below)"),
    (VGV5, 239, "D is a candidate coset"),
    (VGV5, 240, "vacuum manifold with D is unproven"),
    (KZ, 106, "separated by walls (Kibble"),
    (ADAPTER, 32, "p2c just showed a Z2 sector datum can live"),
    (SHARD, 125, "w_1(L_time) = 1 != 0"),
    (PACKET, 69, "four-way homonym"),
    (PACKET, 70, '"the VEV"'),
]
PLANTED_NEGATIVE_PIN = (RUNG2, 272, "The orientation is a Z/3")

# ------------------------------------------------------------------ LEG S scan
SCAN_SCOPE = [
    DRAFTS,
    "lab/sources/transcripts/toe-weinstein-gu-40-years.md",
    "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md",
    "lab/literature/weinstein-ucsd-2025-04-transcript.md",
    EXTRACTION,
    "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md",
    "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md",
    REGISTER,
]
SCAN_FAMILIES = {
    # VEV-FLIP needs a VEV co-token within +-2 lines (co-token discipline)
    "VEV-FLIP": ["changes sign", "change of sign", "sign change", "flips sign",
                 "sign flip", "sign-change", "crosses zero", "either sign",
                 "both signs", "opposite sign", "both orientations",
                 "opposite orientation"],
    # self-contained families (the VEV word is inside the token)
    "VEV-NEGATIVE": ["negative vev", "vev is negative", "vev becomes negative",
                     "vev < 0", "negative vacuum expectation"],
    "VEV-MAGNITUDE": ["significantly above zero", "decreased vev"],
}
VEV_COTOKENS = ["vev", "vacuum expectation", "varpi", "ϖ"]
COTOKEN_FAMILIES = {"VEV-FLIP"}
EXPECTED_MAGNITUDE_HITS = {
    (DRAFTS, 158),
    ("lab/literature/weinstein-ucsd-2025-04-transcript.md", 244),
    (EXTRACTION, 138),
    (REGISTER, 923),
    (REGISTER, 1805),
}

# ------------------------------------------------------------------ LEG B pins
TABLE_BEGIN = "<!-- WB1-TABLE-BEGIN -->"
TABLE_END = "<!-- WB1-TABLE-END -->"
TABLE_SHA256 = "918408feab68df11dcb1b8e288a1e973b67d96b6d0a3a2d205a6689689211d60"
VERDICT_SET = {
    "VACUUM-COMPONENT-LABEL-OF-PHI-NOT-SIGN-OF-R",
    "VEV-FLIP-ABSENT-MAGNITUDE-ONLY",
    "DEGENERACY-AND-UNSELECTABILITY-NOT-REALIZATION",
    "EVEN-MODULATION-STEERS-LOCATION-NEVER-ORIENTATION",
    "RELOCATED-TO-EXTERNAL-SECTOR-DATUM-PI0-GATE-OPEN",
    "NAMED-NOT-FIRED-PI0-NATIVE-UNCOMPUTED",
    # contrary tokens kept in the closed set so the BINDING leg (not a
    # vocabulary error) is what catches a flipped table:
    "DISCHARGED-BY-RUNG2",
    "R-MUST-CROSS-ZERO",
    "REALIZATION-PROVED",
    "FLIP-ASSERTED",
}
EXPECTED_VERDICTS = {
    "CROSS": "VACUUM-COMPONENT-LABEL-OF-PHI-NOT-SIGN-OF-R",
    "SCAN": "VEV-FLIP-ABSENT-MAGNITUDE-ONLY",
    "RUNG2": "DEGENERACY-AND-UNSELECTABILITY-NOT-REALIZATION",
    "STEER": "EVEN-MODULATION-STEERS-LOCATION-NEVER-ORIENTATION",
    "W1": "RELOCATED-TO-EXTERNAL-SECTOR-DATUM-PI0-GATE-OPEN",
    "KILL": "NAMED-NOT-FIRED-PI0-NATIVE-UNCOMPUTED",
}

BASELINE_COUNT = 93  # pinned independently; selftest verifies before and after


# ---------------------------------------------------------------- infrastructure
def true_parity_counter(seq) -> int:
    """Number of adjacent STRICT sign alternations (a*b < 0)."""
    return sum(1 for a, b in zip(seq, seq[1:]) if a * b < 0)


def default_cfg():
    return {
        "pins": [tuple(p) for p in PINS],
        "planted_negative_pin": PLANTED_NEGATIVE_PIN,
        "scan_scope": list(SCAN_SCOPE),
        "scan_families": {k: list(v) for k, v in SCAN_FAMILIES.items()},
        "flip_sign": -1,                 # the phi -> -phi map; corrupted by M4
        "norm_requires_both_ends": True,  # normalizability judge; M5
        "parity_counter": None,           # None -> true counter; M6
        "rung2_path": RUNG2,              # M7
        "artifact_path": None,            # None -> the real artifact; M8
    }


class Run:
    def __init__(self):
        self.n = 0
        self.failures: list[str] = []

    def check(self, cid: str, cond: bool, msg: str = "") -> None:
        self.n += 1
        if cond:
            print(f"[PASS] {cid} {msg}")
        else:
            print(f"[FAIL] {cid} {msg}")
            self.failures.append(cid)


def read_lines(relpath):
    return (ROOT / relpath).read_text(errors="replace").splitlines()


# ---------------------------------------------------------------------- LEG P
def leg_pins(run, cfg):
    print("=" * 78)
    print("LEG P  QUOTE FIDELITY (byte pins at cited lines)")
    print("=" * 78)
    for i, (path, ln, sub) in enumerate(cfg["pins"], 1):
        lines = read_lines(path)
        ok = ln <= len(lines) and sub in lines[ln - 1]
        run.check(f"P-{i:02d}", ok, f"{path}:{ln} :: {sub[:48]!r}")
    path, ln, sub = cfg["planted_negative_pin"]
    lines = read_lines(path)
    run.check("P-neg", not (ln <= len(lines) and sub in lines[ln - 1]),
              f"planted negative: {sub!r} absent at {path}:{ln}")


# ---------------------------------------------------------------------- LEG S
def scan_vev(files_lines, families):
    """families -> {family: [(path, line_no), ...]}; VEV-FLIP hits require a
    VEV co-token within +-2 lines (co-token discipline)."""
    out = {k: [] for k in families}
    for path, lines in files_lines.items():
        low = [l.lower() for l in lines]
        for fam, toks in families.items():
            toks_l = [t.lower() for t in toks]
            for i, l in enumerate(low):
                if any(t in l for t in toks_l):
                    if fam in COTOKEN_FAMILIES:
                        lo, hi = max(0, i - 2), min(len(lines), i + 3)
                        ctx = " ".join(low[lo:hi])
                        if not any(c in ctx for c in VEV_COTOKENS):
                            continue
                    out[fam].append((path, i + 1))
    return out


def leg_scan(run, cfg, tmp):
    print("=" * 78)
    print("LEG S  VEV-ORIENTATION SCAN over the eight Weinstein primary surfaces")
    print("=" * 78)
    files_lines = {p: read_lines(p) for p in cfg["scan_scope"]}
    hits = scan_vev(files_lines, cfg["scan_families"])
    run.check("S-01", len(hits["VEV-FLIP"]) == 0,
              f"VEV-FLIP family: {len(hits['VEV-FLIP'])} hits (must be 0) {hits['VEV-FLIP'][:3]}")
    run.check("S-02", len(hits["VEV-NEGATIVE"]) == 0,
              f"VEV-NEGATIVE family: {len(hits['VEV-NEGATIVE'])} hits (must be 0) {hits['VEV-NEGATIVE'][:3]}")
    got_mag = set(hits["VEV-MAGNITUDE"])
    run.check("S-03", got_mag == EXPECTED_MAGNITUDE_HITS,
              f"VEV-MAGNITUDE family: exactly the 5 one-sided loci: {sorted(got_mag)}")
    # instrument power: planted positive must be flagged, near-misses must not
    planted = tmp / "planted_vev_flip_positive.md"
    planted.write_text("toy control\nthe vev changes sign across the wall between varpi domains\n")
    near_a = tmp / "planted_nearmiss_no_cotoken.md"
    near_a.write_text("toy control\nthe metric changes sign across the horizon in this convention\n")
    near_b = tmp / "planted_nearmiss_no_family_token.md"
    near_b.write_text("toy control\nthe vev sets the fundamental mass scale in this region\n")
    aug = dict(files_lines)
    for f in (planted, near_a, near_b):
        aug[str(f)] = f.read_text().splitlines()
    aug_hits = scan_vev(aug, cfg["scan_families"])
    run.check("S-04", any(p == str(planted) for p, _ in aug_hits["VEV-FLIP"]),
              "planted VEV-FLIP positive is flagged (detector has power)")
    run.check("S-05", not any(p == str(near_a) for fam in aug_hits.values() for p, _ in fam),
              "near-miss A (family token, no VEV co-token in window) is NOT flagged")
    run.check("S-06", not any(p == str(near_b) for fam in aug_hits.values() for p, _ in fam),
              "near-miss B (VEV co-token, no family token) is NOT flagged")


# ---------------------------------------------------------------------- LEG C
def leg_comparator(run, cfg):
    print("=" * 78)
    print("LEG C  EXACT COMPARATOR -- FENCED: binds the rung-2 wall system only")
    print("=" * 78)
    s = cfg["flip_sign"]
    y = sp.Symbol("y", real=True)
    phi, phip = sp.symbols("phi phip", real=True)
    lam = sp.Function("lam")(y)
    vv = sp.Function("v")(y)
    g = sp.Function("g")(y)

    # (a) the evenness identity, arbitrary steering profiles
    print("-- (a) evenness identity for arbitrary lambda(y), v(y), g(y)")
    integrand = phip**2 / 2 + lam * (phi**2 - vv**2)**2 + g * phi
    flipped = integrand.subs([(phi, s * phi), (phip, s * phip)], simultaneous=True)
    diff = sp.expand(flipped - integrand)
    run.check("C-a-01", sp.simplify(diff + 2 * g * phi) == 0,
              "I(-phi) - I(phi) = -2 g(y) phi exactly (the ONLY orientation-odd door is g)")
    integrand0 = phip**2 / 2 + lam * (phi**2 - vv**2)**2
    flipped0 = integrand0.subs([(phi, s * phi), (phip, s * phip)], simultaneous=True)
    run.check("C-a-02", sp.simplify(flipped0 - integrand0) == 0,
              "g = 0 (source-stated quartic + R-set quadratic): phi -> -phi exact "
              "for EVERY lambda(y), v(y) -- no R profile can prefer an orientation")
    run.check("C-a-03", sp.simplify(diff) != 0,
              "the phi-odd rung-2 instrument term g y phi IS flagged asymmetric "
              "(planted-odd control: a stuck-at-even checker fails here)")

    # (b) composite hosting inside one-signed R < 0
    print("-- (b) composite hosting: R = -4(2 + tanh y) < 0 everywhere")
    tt = sp.Symbol("t", real=True)
    Rt = -4 * (2 + tt)
    run.check("C-b-01",
              Rt.subs(tt, -1) == -4 and Rt.subs(tt, 1) == -12 and sp.diff(Rt, tt) == -4,
              "R(t) = -4(2+t) is linear decreasing with max -4 < 0 on t = tanh(y) in [-1,1]: "
              "R one-signed, never crossing")

    def winding(mexpr):
        a = sp.limit(mexpr, y, +sp.oo)
        b = sp.limit(mexpr, y, -sp.oo)
        if a == 0 or b == 0:
            return None
        return sp.Rational(1, 2) * (sp.sign(a) - sp.sign(b))

    def normalizable(f):
        Lp = sp.limit(f, y, +sp.oo)
        if not cfg["norm_requires_both_ends"]:
            # corrupted judge (selftest M5): plus-end limit only
            return Lp == 0
        Lm = sp.limit(f, y, -sp.oo)
        if Lp != 0 or Lm != 0:
            return False
        return bool(sp.integrate(f**2, (y, -sp.oo, sp.oo)).is_finite)

    def hosted(mexpr):
        F = sp.integrate(mexpr, y)
        assert sp.simplify(sp.diff(F, y) - mexpr) == 0
        return int(normalizable(sp.exp(-F))) + int(normalizable(sp.exp(+F)))

    m2 = sp.tanh(y)                    # chain 2: the phi-kink (y_Yuk = 1)
    w2, c2 = winding(m2), hosted(m2)
    run.check("C-b-02", w2 == 1 and c2 == 1 and c2 == abs(w2),
              f"chain 2 (phi-kink inside broken region): winding {w2}, hosted {c2} "
              "= |winding| -- the crossing is phi's")
    run.check("C-b-03",
              sp.integrate(1 / sp.cosh(y)**2, (y, -sp.oo, sp.oo)) == 2,
              "the hosted mode is sech(y) = 1/cosh(y): integral of sech^2 = 2, exact")
    m1 = -(2 + sp.tanh(y))             # chain 1: m = R/4 on the same region
    w1, c1 = winding(m1), hosted(m1)
    run.check("C-b-04", w1 == 0 and c1 == 0 and c1 == abs(w1),
              f"chain 1 (m = R/4, R one-signed): winding {w1}, hosted {c1} "
              "-- one-signed R hosts nothing via the direct chain")

    # (c) sector parity + the winding functional's endpoint-only dependence
    print("-- (c) sector-parity identity and the endpoint-only winding functional")
    counter = cfg["parity_counter"] or true_parity_counter
    exhaustive_ok, n_seq = True, 0
    for n in range(2, 13):
        for signs in itertools.product((-1.0, 1.0), repeat=n):
            n_seq += 1
            odd = counter(signs) % 2 == 1
            if odd != (signs[0] * signs[-1] < 0):
                exhaustive_ok = False
    run.check("C-c-01", exhaustive_ok and n_seq == 8188,
              f"parity identity EXHAUSTIVE over all sign sequences n = 2..12 "
              f"({n_seq} sequences): alternations mod 2 = [ends differ]")
    rng = np.random.default_rng(20260817)
    N = 241
    ok_pinned = True
    for _ in range(200):
        p = rng.normal(size=N)
        p[p == 0.0] = 1e-12
        p[0], p[-1] = -1.0, 1.0
        if counter(p) % 2 != 1:
            ok_pinned = False
    run.check("C-c-02", ok_pinned,
              "200 seeded renderings with pinned opposite ends: crossing count ODD every time")
    ok_equal = True
    for _ in range(200):
        p = rng.normal(size=N)
        p[p == 0.0] = 1e-12
        p[0], p[-1] = 1.0, 1.0
        if counter(p) % 2 != 0:
            ok_equal = False
    run.check("C-c-03", ok_equal,
              "equal-ends control: crossing count EVEN every time (the plant the parity "
              "identity must not absorb)")

    def rung2_winding(p):
        # reimplementation of rung-2 probe:173
        return int(np.sign(p[-1]) - np.sign(p[0])) // 2

    x = np.linspace(-12.0, 12.0, N)
    kinklike = np.tanh(x)
    w_base = rung2_winding(kinklike)
    scrambled = kinklike.copy()
    scrambled[1:-1] = scrambled[1:-1][rng.permutation(N - 2)]
    flipped_end = kinklike.copy()
    flipped_end[-1] = -flipped_end[-1]
    run.check("C-c-04",
              w_base == 1 and rung2_winding(scrambled) == w_base
              and rung2_winding(flipped_end) != w_base,
              "the rung-2 winding functional consumes ONLY the endpoints: interior "
              "scramble invariant, endpoint flip sensitive -- the crossing datum IS "
              "the sector datum")

    # (d) even modulation steers location, never orientation (numeric)
    print("-- (d) even modulation on the rung-2 grid: location yes, orientation never")
    lam_y = 1.0 + 0.3 * np.tanh(x / 2.0)

    def energy_even(p):
        dp = np.gradient(p, x)
        return float(np.trapezoid(0.5 * dp**2 + lam_y * (p**2 - 1.0)**2, x))

    walls = [np.tanh(x - shift) for shift in (-2.0, 0.0, 2.0)]
    energies = [energy_even(p) for p in walls]
    spread = max(energies) - min(energies)
    run.check("C-d-01", spread > 1e-3,
              f"even modulation selects LOCATION: energy spread {spread:.3e} > 1e-3 "
              "(rung-2's N2 conclusion through the source-licensed even channel)")
    ori_diffs = [abs(energy_even(s * p) - energy_even(p)) for p in walls]
    run.check("C-d-02", all(d == 0.0 for d in ori_diffs),
              f"orientation difference EXACTLY 0.0 (bitwise) for every shifted wall: "
              f"{ori_diffs} -- even steering can never prefer an orientation")

    def energy_tilt(p):
        return energy_even(p) + 0.05 * float(np.trapezoid(x * p, x))

    kink = walls[1]
    tilt_split = abs(energy_tilt(s * kink) - energy_tilt(kink))
    run.check("C-d-03", tilt_split > 1e-3,
              f"the phi-odd instrument term g y phi splits kink from antikink "
              f"({tilt_split:.3e} > 1e-3): only the odd door touches orientation")


# ---------------------------------------------------------------------- LEG R
def leg_rung2(run, cfg):
    print("=" * 78)
    print("LEG R  RUNG-2 RE-RUN (the repository's own instrument)")
    print("=" * 78)
    r = subprocess.run([sys.executable, str(ROOT / cfg["rung2_path"])],
                       capture_output=True, text=True, cwd=ROOT)
    run.check("R-01", r.returncode == 0,
              f"rung-2 dynamical-wall probe exits 0 (got {r.returncode})")
    run.check("R-02", "VERDICT: SECTOR-SUPPLIED" in r.stdout,
              "rung-2 verdict is SECTOR-SUPPLIED (the sector -- the crossing datum -- "
              "is an input the action cannot select)")
    run.check("R-03", "provably cannot fix" in r.stdout,
              "the T-DEG sentence is on the live run's face ('a Z/2 the action provably cannot fix')")
    run.check("R-04", "accessible rank 3" in r.stdout,
              "supplied multiplicity 3 -> accessible rank 3 (N supplied, never derived)")


# ---------------------------------------------------------------------- LEG B
def parse_table(text):
    m = re.search(re.escape(TABLE_BEGIN) + r"(.*?)" + re.escape(TABLE_END), text, re.S)
    if not m:
        return None, None
    block = m.group(1)
    rows = []
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[0] not in ("id", "---"):
            if set(cells[0]) != {"-"}:
                rows.append(cells)
    return block, rows


def leg_binding(run, cfg):
    print("=" * 78)
    print("LEG B  ARTIFACT BINDING (verdict-evidence consistency)")
    print("=" * 78)
    apath = cfg["artifact_path"] or (ROOT / ARTIFACT)
    text = Path(apath).read_text(errors="replace")
    block, rows = parse_table(text)
    run.check("B-01", block is not None and rows is not None and len(rows) == 6,
              f"machine table parsed: {0 if rows is None else len(rows)} rows (need 6)")
    if not rows:
        return
    verdicts = {r[0]: r[2] for r in rows}
    run.check("B-02", all(r[2] in VERDICT_SET for r in rows),
              "all verdict tokens drawn from the closed set")
    sha = hashlib.sha256(block.encode()).hexdigest()
    run.check("B-03", sha == TABLE_SHA256,
              f"table SHA-256 pinned ({sha[:16]}... vs {TABLE_SHA256[:16]}...)")
    for i, key in enumerate(("CROSS", "SCAN", "RUNG2", "STEER", "W1", "KILL"), 4):
        run.check(f"B-{i:02d}", verdicts.get(key) == EXPECTED_VERDICTS[key],
                  f"{key} verdict consistent with its measured evidence "
                  f"(got {verdicts.get(key)})")
    run.check("B-10", "does not derive 3" in text,
              "artifact states on its face that it does not derive 3")
    run.check("B-11", "|winding| = 1" in text and "OPEN" in text,
              "artifact carries the rung-2 hosting null and leaves the open items OPEN")
    run.check("B-12", "GU-COMPARATOR-ROUTING" in text
              and "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text,
              "routing notice and classification present")
    run.check("B-13", "canonical_effect: pending_integration" in text,
              "canonical_effect declared pending_integration")
    run.check("B-14", "Canonical-currency check records (for the integrator; WB-1 edits no sidecar)"
              in text,
              "the currency-records section is present under its mandated header")
    run.check("B-15", "SUBTRACTIVE 2+1" in text and "N SUPPLIED" in text,
              "the CC-05 fence is applied in the artifact's own words")
    run.check("B-16", "RELOCATED is not DISCHARGED" in text,
              "the claim ceiling separates RELOCATED from DISCHARGED explicitly")
    run.check("B-17", "target_claim:" in text and "target_claim_verdict:" in text,
              "target_claim and target_claim_verdict frontmatter present")
    run.check("B-18", text.count("```gu-typed-objects") == 2,
              "both gu-typed-objects blocks present (typed-carrier gate surface)")


# --------------------------------------------------------------------- driver
def run_live(cfg):
    run = Run()
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        leg_pins(run, cfg)
        leg_scan(run, cfg, tmp)
        leg_comparator(run, cfg)
        leg_rung2(run, cfg)
        leg_binding(run, cfg)
    print("-" * 78)
    print(f"checks: {run.n}  failures: {len(run.failures)} {run.failures}")
    return run


# mutations: every one corrupts MACHINERY or a REFERENCE, never a predicate.
def mutations():
    def m1(cfg):  # corrupt a pin reference (line number off by one)
        cfg["pins"][2] = (cfg["pins"][2][0], cfg["pins"][2][1] + 1, cfg["pins"][2][2])

    def m2(cfg):  # scan detector loses its VEV-FLIP family
        cfg["scan_families"]["VEV-FLIP"] = []

    def m3(cfg):  # scan scope loses the drafts surface (reference corruption)
        cfg["scan_scope"] = [p for p in cfg["scan_scope"] if p != DRAFTS]

    def m4(cfg):  # the phi -> -phi map corrupted to the identity
        cfg["flip_sign"] = +1

    def m5(cfg):  # normalizability judge loses its far-end and integral gates
        cfg["norm_requires_both_ends"] = False

    def m6(cfg):  # parity counter corrupted (off-by-one)
        cfg["parity_counter"] = lambda seq: true_parity_counter(seq) + 1

    def m7(cfg):  # rung-2 runner pointed at a nonexistent instrument
        cfg["rung2_path"] = "tests/channel-swings/DOES_NOT_EXIST_wb1.py"

    def m8(cfg):  # CONTRARY CONTROL: artifact copy claims DISCHARGED-BY-RUNG2
        src = (ROOT / ARTIFACT).read_text()
        mut = src.replace(
            "| W1 | the bill item's disposition | RELOCATED-TO-EXTERNAL-SECTOR-DATUM-PI0-GATE-OPEN |",
            "| W1 | the bill item's disposition | DISCHARGED-BY-RUNG2 |")
        assert mut != src, "contrary-control substitution failed to apply"
        tmpf = Path(tempfile.mkstemp(suffix=".md")[1])
        tmpf.write_text(mut)
        cfg["artifact_path"] = tmpf

    return [
        ("M1 pin reference off by one",           m1, {"P-03"}),
        ("M2 scan loses VEV-FLIP family",         m2, {"S-04"}),
        ("M3 scan scope loses the drafts surface", m3, {"S-03"}),
        ("M4 phi-flip map corrupted to identity", m4, {"C-a-01", "C-a-03", "C-d-03"}),
        ("M5 normalizability judge gates lost",   m5, {"C-b-04"}),
        ("M6 parity counter off-by-one",          m6, {"C-c-01", "C-c-02", "C-c-03"}),
        ("M7 rung-2 runner mispointed",           m7, {"R-01", "R-02", "R-03", "R-04"}),
        ("M8 CONTRARY CONTROL: DISCHARGED-BY-RUNG2", m8, {"B-03", "B-08"}),
    ]


def selftest():
    print("#" * 78)
    print("# SELFTEST: clean baseline FIRST, then 8 machinery mutations")
    print("#" * 78)
    base = run_live(default_cfg())
    if base.failures or base.n != BASELINE_COUNT:
        print(f"RED BASELINE: {len(base.failures)} failures, {base.n} checks "
              f"(pinned {BASELINE_COUNT}) -- aborting; no mutation result is meaningful.")
        return 1
    print(f"baseline green: {base.n}/{base.n} (pinned {BASELINE_COUNT}); running mutations")
    bad = 0
    for name, fn, targets in mutations():
        cfg = default_cfg()
        try:
            fn(cfg)
            r = run_live(cfg)
            caught = set(r.failures)
        except Exception as exc:  # noqa: BLE001
            print(f"[SELFTEST-FAIL] {name}: CRASH-NOT-DETECTION ({type(exc).__name__}: {exc})")
            bad += 1
            continue
        finally:
            ap = cfg.get("artifact_path")
            if ap is not None and Path(ap).exists() and str(ap).startswith(tempfile.gettempdir()):
                Path(ap).unlink()
        if not caught:
            print(f"[SELFTEST-FAIL] {name}: NOT CAUGHT (no failing check)")
            bad += 1
        elif not (caught & targets):
            print(f"[SELFTEST-FAIL] {name}: INCIDENTAL-NOT-TARGETED (caught {sorted(caught)}, "
                  f"target {sorted(targets)})")
            bad += 1
        elif not (caught <= targets):
            print(f"[SELFTEST-FAIL] {name}: OVERSPILL beyond declared target set "
                  f"(caught {sorted(caught)}, allowed {sorted(targets)})")
            bad += 1
        else:
            print(f"[SELFTEST-OK] {name}: caught by {sorted(caught)}")
    rebase = run_live(default_cfg())
    if rebase.failures or rebase.n != BASELINE_COUNT:
        print("RED RE-BASELINE after mutations -- machinery leaked state.")
        return 1
    print("#" * 78)
    if bad:
        print(f"# SELFTEST: {bad} mutation(s) NOT properly caught -- FAIL")
        return 1
    print(f"# SELFTEST: 8/8 mutations caught by their targeted checks; baseline "
          f"re-verified ({rebase.n}/{BASELINE_COUNT}) -- PASS")
    return 0


def main():
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    r = run_live(default_cfg())
    if r.failures:
        print("RESULT: FAIL")
        sys.exit(1)
    print("RESULT: PASS -- all legs green")
    sys.exit(0)


if __name__ == "__main__":
    main()
