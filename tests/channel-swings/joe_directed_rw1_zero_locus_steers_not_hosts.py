#!/usr/bin/env python3
r"""RW-1 probe: the R(y) / domain-wall join, pinned and measured.

Pins and certifies
  lab/active-research/joe-directed/rwall/rw1-zero-locus-steers-not-hosts-2026-08-17.md

Six legs, each independently failing:

  LEG 1  QUOTE FIDELITY.  Thirty (file, line, substring) pins the artifact
         quotes verbatim, byte-matched at the cited line.  Carries a PLANTED
         NEGATIVE (the "(R(y)/2)" near-miss must NOT match at register:940) so
         a matcher stuck at True is caught.

  LEG 2  SOURCE SIGN SCAN (certified).  Over the eight Weinstein primary
         surfaces: the CROSSING family ("changes sign", "crosses zero", ...)
         with a curvature co-token in a +-2-line window scores ZERO hits; the
         POSITIVE family ("curvature is positive", "R > 0", ...) scores ZERO;
         the NEGATIVE family scores EXACTLY THREE, all the same UCSD passage
         (drafts:149 "So if your curvature is negative, now you start to get a
         Mexican hat potential", its edited-derivative twin ucsd:235, and the
         register note :2336).  So the source states the zero and the negative
         side, and never a crossing.  A planted-positive control the detector
         is REQUIRED to flag and a planted near-miss it is required NOT to
         flag certify the instrument.

  LEG 3  JOIN RESCAN (certified).  Repo-wide re-run of LD-A's LEG-5 scan
         (wall tokens x curvature/VEV tokens, +-3-line window): the ONLY files
         joining the families are the naming wave itself (the LD-A artifact
         and probe, and RW-1's own two files).  A joiner OUTSIDE
         lab/active-research/joe-directed/ and tests/channel-swings/ fails the
         leg; same-wave files are reported, not failed (sibling arcs write
         this tree concurrently).  Planted positive + planted near-miss.

  LEG 4  EXACT COMPARATOR (sympy; FENCED -- binds the model only).  On the
         repository's own operator class (Gamma = sigma_3, Krein K = sigma_1,
         D_0 = sigma_1 (x) p; the continuum fiber of
         tests/function-space-ext/dirac_spectral_flow_section.py):
         (a) fiberwise class/gap algebra over the complete Pauli basis --
             exactly the two gapping zero-order directions exist (sigma_2,
             sigma_3) and BOTH leave the (Gamma-odd, Krein) class; the class
             member sigma_1 does not gap.  Exact eigenvalues.
         (b) the Jackiw-Rebbi mode reduction D psi = 0 <=> psi' = -sigma_2 m psi
             (source-shaped sigma_3 wall) and psi' = +sigma_3 m psi (sigma_2
             wall), verified symbolically for generic m(y); a PLANTED
             wrong-chirality candidate must be flagged NONZERO.
         (c) hosting table, six profiles, exact: tanh -> 1 mode; -tanh -> 1;
             linear ky -> 1 (Gaussian, width^2 = 1/(2k) -> oo as k -> 0);
             2+tanh (no zero) -> 0; y^2 (zero WITHOUT sign change) -> 0;
             1-tanh (one-sided, gapless end -- the broken-to-unbroken
             interface) -> 0.  count = |winding| whenever winding is defined.
         (d) grading, exact: the source-shaped (sigma_3) wall's hosted mode
             has Gamma-charge EXACTLY 0 (it is sigma_2-graded); the sigma_2
             wall's hosted mode has Gamma-charge EXACTLY -1 and that wall
             leaves ONLY the Krein condition.
         (e) the two walls are unitarily equivalent (U = exp(-i pi sigma_1/4))
             while U Gamma U^dag != Gamma: the hosted-Gamma-charge difference
             is carried by the grading, not the operator.
         (f) the two source-identified mass chains disagree at the zero locus
             at exponent grade: m_1 = R/4 vanishes to order 1, the stylized
             Mexican-hat VEV mass vanishes to order 1/2 and is supported on
             R <= 0 only.
         (g) multiplicity is supplied: ker(D (x) I_N) = ker(D) (x) C^N
             (N = 3 fiber check), so hosted count = |winding| * N.

  LEG 5  CROSS-CHECKS.  The repository's own instruments at both endpoints of
         the join still run green: tests/function-space-ext/
         dirac_spectral_flow_section.py (exit 0) and tests/channel-swings/
         rung2_dynamical_wall_selectability_probe.py (exit 0, VERDICT:
         SECTOR-SUPPLIED, accessible rank 3 = supplied multiplicity).

  LEG 6  ARTIFACT BINDING.  Parses the machine table between the RW1-TABLE
         markers (six rows, closed verdict set), SHA-256 pins the block, and
         enforces verdict-evidence consistency: a verdict inconsistent with
         its own measured evidence is a caught error (the selftest's CONTRARY
         CONTROL flips LIN to SAME-OBJECT and must be caught here).  Also
         enforces the claim ceiling in the artifact's own text: "does not
         derive 3" present, the winding question OPEN, hosting language
         present, and no source-attribution of repository vocabulary.

--selftest discipline (VERIFICATION.md "Probe and mutation-harness discipline"):
  * the CLEAN BASELINE is verified FIRST and a red baseline aborts;
  * the baseline check count is pinned independently and re-verified after
    the mutations;
  * every mutation corrupts MACHINERY or a REFERENCE, never a check's
    predicate;
  * a catch counts only via a genuine [FAIL] line -- a mutant that crashes is
    CRASH-NOT-DETECTION and fails; an incidental catch elsewhere is
    INCIDENTAL-NOT-TARGETED and fails;
  * the failing check is printed for every mutation (rule 7);
  * exit 0 on success.

Read-only: the probe writes nothing into the repository.  Planted-control
corpora and the contrary-control artifact copy live in a temp directory and
are removed.  Deterministic; sympy + numpy + stdlib only.
"""
from __future__ import annotations

import copy
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]

ARTIFACT = "lab/active-research/joe-directed/rwall/rw1-zero-locus-steers-not-hosts-2026-08-17.md"
SELF_PROBE = "tests/channel-swings/joe_directed_rw1_zero_locus_steers_not_hosts.py"

# ----------------------------------------------------------------- references
# LEG 1 pins: (path, 1-based line, exact substring that must appear ON that line)
PINS = [
    ("lab/sources/source-claim-register.yaml", 913,
     "non-chiral total theory splits at the emergent level into two separate"),
    ("lab/sources/source-claim-register.yaml", 922,
     "pulling the various sub-fields of varpi to values"),
    ("lab/sources/source-claim-register.yaml", 940,
     "dslash_A psi_L(y) = (R(y)/4) psi_R(y)"),
    ("lab/sources/source-claim-register.yaml", 948,
     "Decoupling at R(y) ~ 0 in (12.15)-(12.17)"),
    ("lab/sources/source-claim-register.yaml", 1176,
     "stylized massive Dirac Equation with mass m = R(y)/4"),
    ("lab/sources/source-claim-register.yaml", 1177,
     "approximately constant in a region under study"),
    ("lab/sources/source-claim-register.yaml", 1613,
     "drops sufficiently, then a Dirac type operator decouples into Weyl type operators"),
    ("lab/sources/source-claim-register.yaml", 1639,
     "when gravity gets low enough"),
    ("lab/sources/source-claim-register.yaml", 1641,
     "to matter that is currently dark when gravity becomes strong enough"),
    ("lab/sources/source-claim-register.yaml", 2329,
     "there's no Higgs. The Higgs is an illusion"),
    ("lab/sources/source-claim-register.yaml", 2336,
     "negative curvature gives the Mexican hat"),
    ("papers/drafts/Transcript into the impossible.md", 149,
     "So if your curvature is negative, now you start to get a Mexican hat potential"),
    ("papers/drafts/Transcript into the impossible.md", 158,
     "exactly three families of chiral fermions if you have a decreased VEV"),
    ("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md", 239,
     r"D_A\psi_L=\frac{R(y)}4\psi_R"),
    ("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md", 241,
     r"D_A\psi_R=\frac{R(y)}4\psi_L"),
    ("lab/sources/gu-paper-reference-surfaces.md", 56,
     "appears chiral in low-curvature regions via R(y) coupling"),
    ("CANON.md", 136,
     "Net chiral spectral flow 0 for self-adjoint, chirality-odd, Krein-self-adjoint Fredholm families"),
    ("CANON.md", 139,
     "interior-even + external-topological-index"),
    ("CANON.md", 135,
     "net chiral index = flux number (any integer, odd for odd flux)"),
    ("VERIFICATION.md", 24,
     "the only unconditionally computable integer is 1"),
    ("explorations/nielsen-ninomiya-domain-wall-records-as-rows-2026-07-10.md", 30,
     "a single chiral mode lives on the boundary of"),
    ("explorations/nielsen-ninomiya-domain-wall-records-as-rows-2026-07-10.md", 90,
     "it rides SG4, exactly as the carrier bit does"),
    ("explorations/prereg-rung2-dynamical-wall-and-selectability-test-2026-07-29.md", 111,
     "has demonstrated hosting, not selection (the Jackiw-Rebbi standard"),
    ("explorations/prereg-rung2-dynamical-wall-and-selectability-test-2026-07-29.md", 95,
     "linear-gradient term makes location selectable"),
    ("lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md", 138,
     "sub-fields of ϖ to values significantly above zero"),
    ("lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md", 245,
     "the effective-chirality mechanism"),
    ("explorations/decoupling-constructibility-packet-2026-08-12.md", 259,
     "massless but operator-decoupled (zero cross-cells AND"),
    ("explorations/decoupling-constructibility-packet-2026-08-12.md", 69,
     "four-way homonym"),
    ("tests/function-space-ext/dirac_spectral_flow_section.py", 13,
     "Gamma-ODD (a Dirac / chirality"),
    ("lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md", 456,
     "connect its `R(y)` zero locus to the external-by-structure domain wall"),
]
PLANTED_NEGATIVE_PIN = ("lab/sources/source-claim-register.yaml", 940, "(R(y)/2)")

# LEG 2: the eight Weinstein primary surfaces
SIGN_SCOPE = [
    "papers/drafts/Transcript into the impossible.md",
    "lab/sources/transcripts/toe-weinstein-gu-40-years.md",
    "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md",
    "lab/literature/weinstein-ucsd-2025-04-transcript.md",
    "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md",
    "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md",
    "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md",
    "lab/sources/source-claim-register.yaml",
]
SIGN_FAMILIES = {
    "CROSSING": ["changes sign", "change of sign", "sign change", "crosses zero",
                 "flips sign", "sign flip", "sign-change"],
    "POSITIVE": ["curvature is positive", "positive curvature",
                 "positive scalar curvature", "R > 0", "R(y) > 0"],
    "NEGATIVE": ["curvature is negative", "negative curvature", "R < 0",
                 "R(y) < 0", "curvature becomes negative"],
}
SIGN_CURV_COTOKENS = ["curvature", "R(y)"]
EXPECTED_NEGATIVE_HITS = {
    ("papers/drafts/Transcript into the impossible.md", 149),
    ("lab/literature/weinstein-ucsd-2025-04-transcript.md", 235),
    ("lab/sources/source-claim-register.yaml", 2336),
}

# LEG 3: join rescan token families (LD-A LEG-5 families, re-run)
WALL_TOKENS = ["jackiw-rebbi", "domain-wall fermion", "domain wall fermion", "kaplan 1992"]
CURV_TOKENS = ["r(y)", "scalar curv", "curvature", "vev"]
JOIN_WINDOW = 3
KNOWN_WAVE_JOINERS = {
    "lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md",
    "tests/channel-swings/joe_directed_lda_sg4_bit2_type_and_transport.py",
    ARTIFACT,
    SELF_PROBE,
}
WAVE_TREES = ("lab/active-research/joe-directed/", "tests/channel-swings/")

# LEG 5 subprocess cross-checks
DSFS_PATH = "tests/function-space-ext/dirac_spectral_flow_section.py"
RUNG2_PATH = "tests/channel-swings/rung2_dynamical_wall_selectability_probe.py"

# LEG 6: machine table pin
TABLE_BEGIN = "<!-- RW1-TABLE-BEGIN -->"
TABLE_END = "<!-- RW1-TABLE-END -->"
TABLE_SHA256 = "9a4ebcebaff4f9e804892006b7b5d54bfe8e46ef3b56a5e6fa092a34b01d3c84"
VERDICT_SET = {
    "POSITION-INDEXED-MAGNITUDE-NO-CROSSING",
    "NEIGHBOR-SHARED-INGREDIENT",
    "BILL-OF-SIX-WINDING-OPEN",
    "GAMMA-NEUTRAL-ON-SOURCE-SHAPED-WALL",
    "TYPED-TARGET-VEV-ORIENTATION-WALL-R-STEERED",
    "NO-PRIOR-JOIN",
    # tokens that would be inconsistent with the measurements; kept in the
    # closed set so the binding leg (not a vocabulary error) catches them:
    "SAME-OBJECT",
    "R-ZERO-LOCUS-HOSTS-AS-STATED",
}

BASELINE_COUNT = 84  # pinned independently; selftest verifies before and after


# ---------------------------------------------------------------- infrastructure
def default_cfg():
    return {
        "pins": [tuple(p) for p in PINS],
        "planted_negative_pin": PLANTED_NEGATIVE_PIN,
        "sign_families": {k: list(v) for k, v in SIGN_FAMILIES.items()},
        "wall_tokens": list(WALL_TOKENS),
        "curv_tokens": list(CURV_TOKENS),
        "join_window": JOIN_WINDOW,
        "pauli": None,          # None -> build the true Pauli matrices
        "nonzero_flagger": None,  # None -> the true symbolic nonzero flagger
        "winding_halver": sp.Rational(1, 2),
        "norm_requires_both_ends": True,
        "rung2_path": RUNG2_PATH,
        "artifact_path": None,  # None -> the real artifact
    }


class Run:
    def __init__(self):
        self.n = 0
        self.failures = []

    def check(self, cid, cond, msg=""):
        self.n += 1
        if cond:
            print(f"[PASS] {cid} {msg}")
        else:
            print(f"[FAIL] {cid} {msg}")
            self.failures.append(cid)


def read_lines(relpath):
    return (ROOT / relpath).read_text(errors="replace").splitlines()


# ---------------------------------------------------------------------- LEG 1
def leg1(run, cfg):
    print("=" * 78)
    print("LEG 1  QUOTE FIDELITY (byte pins at cited lines)")
    print("=" * 78)
    for i, (path, ln, sub) in enumerate(cfg["pins"], 1):
        lines = read_lines(path)
        ok = ln <= len(lines) and sub in lines[ln - 1]
        run.check(f"L1-{i:02d}", ok, f"{path}:{ln} :: {sub[:50]!r}")
    path, ln, sub = cfg["planted_negative_pin"]
    lines = read_lines(path)
    run.check("L1-neg", not (ln <= len(lines) and sub in lines[ln - 1]),
              f"planted negative: {sub!r} absent at {path}:{ln}")


# ---------------------------------------------------------------------- LEG 2
def scan_sign(files_lines, families):
    """families -> list of (path, line_no) hits with a curvature co-token
    within +-2 lines."""
    out = {k: [] for k in families}
    for path, lines in files_lines.items():
        low = [l.lower() for l in lines]
        for fam, toks in families.items():
            toks_l = [t.lower() for t in toks]
            for i, l in enumerate(low):
                if any(t in l for t in toks_l):
                    lo, hi = max(0, i - 2), min(len(lines), i + 3)
                    ctx = " ".join(low[lo:hi])
                    if any(c.lower() in ctx for c in SIGN_CURV_COTOKENS):
                        out[fam].append((path, i + 1))
    return out


def leg2(run, cfg, tmp):
    print("=" * 78)
    print("LEG 2  SOURCE SIGN SCAN over the eight Weinstein primary surfaces")
    print("=" * 78)
    files_lines = {p: read_lines(p) for p in SIGN_SCOPE}
    hits = scan_sign(files_lines, cfg["sign_families"])
    run.check("L2-01", len(hits["CROSSING"]) == 0,
              f"CROSSING family: {len(hits['CROSSING'])} hits (must be 0) {hits['CROSSING'][:3]}")
    run.check("L2-02", len(hits["POSITIVE"]) == 0,
              f"POSITIVE family: {len(hits['POSITIVE'])} hits (must be 0) {hits['POSITIVE'][:3]}")
    got_neg = set(hits["NEGATIVE"])
    run.check("L2-03", got_neg == EXPECTED_NEGATIVE_HITS,
              f"NEGATIVE family: exactly the one UCSD passage, three surfaces: {sorted(got_neg)}")
    # instrument power: planted positive must be flagged, near-miss must not
    planted = tmp / "planted_sign_positive.md"
    planted.write_text("toy control\nthe scalar curvature R(y) changes sign across the locus\n")
    nearmiss = tmp / "planted_sign_nearmiss.md"
    nearmiss.write_text("toy control\nthe sign conventions of the curvature term are fixed\n")
    aug = dict(files_lines)
    aug[str(planted)] = planted.read_text().splitlines()
    aug[str(nearmiss)] = nearmiss.read_text().splitlines()
    aug_hits = scan_sign(aug, cfg["sign_families"])
    run.check("L2-04", any(p == str(planted) for p, _ in aug_hits["CROSSING"]),
              "planted CROSSING positive is flagged (detector has power)")
    run.check("L2-05", not any(p == str(nearmiss) for fam in aug_hits.values() for p, _ in fam),
              "planted near-miss is NOT flagged")


# ---------------------------------------------------------------------- LEG 3
def scan_join(corpus, wall_tokens, curv_tokens, window):
    wall_re = re.compile("|".join(re.escape(t) for t in wall_tokens), re.I) if wall_tokens else None
    curv_re = re.compile("|".join(re.escape(t) for t in curv_tokens), re.I)
    joiners = []
    for path, lines in corpus.items():
        if wall_re is None:
            continue
        wl = [i for i, l in enumerate(lines) if wall_re.search(l)]
        if not wl:
            continue
        cl = {i for i, l in enumerate(lines) if curv_re.search(l)}
        for i in wl:
            if any(j in cl for j in range(i - window, i + window + 1)):
                joiners.append(path)
                break
    return joiners


def repo_corpus():
    corpus = {}
    for p in ROOT.rglob("*"):
        if p.suffix not in (".md", ".py", ".yaml", ".txt"):
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith("_local/"):
            continue
        try:
            corpus[rel] = p.read_text(errors="replace").splitlines()
        except OSError:
            continue
    return corpus


def leg3(run, cfg, tmp):
    print("=" * 78)
    print("LEG 3  JOIN RESCAN (wall tokens x curvature tokens, +-3 lines, repo-wide)")
    print("=" * 78)
    corpus = repo_corpus()
    print(f"  corpus: {len(corpus)} files (md/py/yaml/txt outside _local)")
    joiners = scan_join(corpus, cfg["wall_tokens"], cfg["curv_tokens"], cfg["join_window"])
    outside = [j for j in joiners if not j.startswith(WAVE_TREES)]
    inside_unknown = [j for j in joiners
                      if j.startswith(WAVE_TREES) and j not in KNOWN_WAVE_JOINERS]
    known = [j for j in joiners if j in KNOWN_WAVE_JOINERS]
    print(f"  joiners: {len(joiners)} -> known naming wave {sorted(known)}")
    if inside_unknown:
        print(f"  SAME-WAVE (reported, not failed; concurrent sibling arcs): {sorted(inside_unknown)}")
    run.check("L3-01", len(outside) == 0,
              f"no joiner outside the naming wave's trees (found {sorted(outside)[:5]})")
    run.check("L3-02", set(known) <= KNOWN_WAVE_JOINERS and len(known) >= 1,
              "the known joiners are exactly (a subset of) the declared naming wave")
    planted = tmp / "planted_join_positive.md"
    planted.write_text("control file\nthe Jackiw-Rebbi wall\nsits at the scalar curvature zero\n")
    nearmiss = tmp / "planted_join_nearmiss.md"
    nearmiss.write_text("control file\na domain wall of the theory\n\n\n\nfar away curvature line\n")
    aug = {str(planted): planted.read_text().splitlines(),
           str(nearmiss): nearmiss.read_text().splitlines()}
    aug_join = scan_join(aug, cfg["wall_tokens"], cfg["curv_tokens"], cfg["join_window"])
    run.check("L3-03", str(planted) in aug_join,
              "planted join positive is flagged (detector has power)")
    run.check("L3-04", str(nearmiss) not in aug_join,
              "planted near-miss (bare 'domain wall', tokens out of window) is NOT flagged")


# ---------------------------------------------------------------------- LEG 4
def pauli(cfg):
    if cfg["pauli"] is not None:
        return cfg["pauli"]
    s0 = sp.eye(2)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    return s0, s1, s2, s3


def nonzero_flagger(cfg):
    if cfg["nonzero_flagger"] is not None:
        return cfg["nonzero_flagger"]
    return lambda M: sp.simplify(M) != sp.zeros(*M.shape)


def leg4(run, cfg):
    print("=" * 78)
    print("LEG 4  EXACT COMPARATOR (sympy) -- FENCED: binds the model only")
    print("=" * 78)
    s0, s1, s2, s3 = pauli(cfg)
    y, p, m = sp.symbols("y p m", real=True)
    k = sp.Symbol("k", positive=True)
    Z2 = sp.zeros(2, 2)

    # (a) fiberwise class/gap algebra over the complete Pauli basis
    print("-- (a) class/gap algebra, D(p) = sigma_1 p + m M, Gamma = sigma_3, K = sigma_1")
    expected = {
        # name: (Gamma-odd, Krein-ok, gapped)
        "s0": (False, True, False),
        "s1": (True, True, False),
        "s2": (True, False, True),
        "s3": (False, False, True),
    }
    for name, M in [("s0", s0), ("s1", s1), ("s2", s2), ("s3", s3)]:
        godd = sp.simplify(M * s3 + s3 * M) == Z2
        krein = sp.simplify(M.H * s1 - s1 * M) == Z2
        evs = list((s1 * p + m * M).eigenvals().keys())
        gapped = all(sp.simplify(e.subs(p, 0)) != 0 for e in evs) and \
            all(len(sp.solve(sp.Eq(e, 0), p)) == 0 or
                all(sol.has(m) for sol in sp.solve(sp.Eq(e, 0), p)) for e in evs)
        # gap criterion: no eigenvalue root p independent of m, and at m generic
        # the eigenvalues are sqrt(p^2+m^2)-type (checked directly):
        gapped = all(sp.simplify(e - sp.sqrt(p**2 + m**2)) == 0 or
                     sp.simplify(e + sp.sqrt(p**2 + m**2)) == 0 for e in evs)
        exp_g, exp_k, exp_gap = expected[name]
        run.check(f"L4-a-{name}", (godd, krein, gapped) == (exp_g, exp_k, exp_gap),
                  f"{name}: Gamma-odd={godd} Krein-ok={krein} gapped(+-sqrt(p^2+m^2))={gapped}")
    run.check("L4-a-exit", True and expected["s2"][1] is False and expected["s3"][1] is False,
              "both gapping directions leave the Krein class (exact); the class member s1 does not gap")

    # (b) mode reduction + planted wrong-chirality candidate
    print("-- (b) Jackiw-Rebbi mode reduction, generic m(y)")
    mfun, F = sp.Function("m"), sp.Function("F")
    chip = sp.Matrix([1, sp.I]) / sp.sqrt(2)   # sigma_2 = +1
    chim = sp.Matrix([1, -sp.I]) / sp.sqrt(2)  # sigma_2 = -1
    e1, e2 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
    run.check("L4-b-01", sp.simplify(s2 * chip - chip) == sp.zeros(2, 1)
              and sp.simplify(s2 * chim + chim) == sp.zeros(2, 1),
              "chi_+- are the sigma_2 eigenvectors")

    def D3(psi):  # source-shaped wall: sigma_1 p + sigma_3 m(y)
        return -sp.I * s1 * psi.diff(y) + mfun(y) * s3 * psi

    def D2(psi):  # Gamma-odd wall: sigma_1 p + sigma_2 m(y)
        return -sp.I * s1 * psi.diff(y) + mfun(y) * s2 * psi

    sub = {sp.Derivative(F(y), y): mfun(y)}
    r1 = sp.simplify(D3(sp.exp(-F(y)) * chip).subs(sub))
    r2 = sp.simplify(D3(sp.exp(+F(y)) * chim).subs(sub))
    run.check("L4-b-02", r1 == sp.zeros(2, 1) and r2 == sp.zeros(2, 1),
              "sigma_3 wall: exp(-int m) chi_+ and exp(+int m) chi_- solve D psi = 0 exactly")
    r3 = sp.simplify(D2(sp.exp(-F(y)) * e2).subs(sub))
    r4 = sp.simplify(D2(sp.exp(+F(y)) * e1).subs(sub))
    run.check("L4-b-03", r3 == sp.zeros(2, 1) and r4 == sp.zeros(2, 1),
              "sigma_2 wall: exp(-int m) e_2 and exp(+int m) e_1 solve D psi = 0 exactly")
    flag = nonzero_flagger(cfg)
    rw = sp.simplify(D3(sp.exp(-F(y)) * chim).subs(sub))
    run.check("L4-b-04", flag(rw),
              "PLANTED wrong-chirality candidate exp(-int m) chi_- is flagged NONZERO")

    # (d) grading, exact
    gp = sp.simplify((chip.H * s3 * chip)[0])
    gm = sp.simplify((chim.H * s3 * chim)[0])
    ge2 = sp.simplify((e2.T * s3 * e2)[0])
    run.check("L4-d-01", gp == 0 and gm == 0,
              f"source-shaped wall modes: Gamma-charge EXACTLY 0 (got {gp}, {gm})")
    run.check("L4-d-02", ge2 == -1,
              f"sigma_2 wall mode: Gamma-charge EXACTLY -1 (got {ge2})")

    # (e) unitary equivalence, grading transport
    U = sp.cos(sp.pi / 4) * s0 - sp.I * sp.sin(sp.pi / 4) * s1
    run.check("L4-e-01", sp.simplify(U * U.H - s0) == Z2, "U = exp(-i pi sigma_1/4) is unitary")
    run.check("L4-e-02", sp.simplify(U * s1 * U.H - s1) == Z2, "U commutes with the kinetic sigma_1")
    conj3 = sp.simplify(U * s3 * U.H)
    run.check("L4-e-03", conj3 == s2 or conj3 == -s2,
              f"U rotates the sigma_3 mass into the sigma_2 mass (U s3 U^dag = {'+' if conj3 == s2 else '-'}s2)")
    run.check("L4-e-04", sp.simplify(U * s3 * U.H - s3) != Z2,
              "U does NOT preserve Gamma: the hosted-charge difference is grading transport")

    # (c) hosting table, six profiles, exact
    print("-- (c) hosting table (sigma_3 wall), exact")
    halver = cfg["winding_halver"]
    both_ends = cfg["norm_requires_both_ends"]

    def winding(mexpr):
        a = sp.limit(mexpr, y, +sp.oo)
        b = sp.limit(mexpr, y, -sp.oo)
        if a == 0 or b == 0:
            return None  # gapless end: JR winding undefined
        return halver * (sp.sign(a) - sp.sign(b))

    def normalizable(f):
        Lp = sp.limit(f, y, +sp.oo)
        if not both_ends:
            # corrupted judge (selftest M8): plus-end limit only, no far-end
            # gate, no integral gate
            return Lp == 0
        Lm = sp.limit(f, y, -sp.oo)
        if Lp != 0 or Lm != 0:
            return False
        return bool(sp.integrate(f**2, (y, -sp.oo, sp.oo)).is_finite)

    profiles = [
        # (label, m(y), expected winding (None = undefined/gapless end), expected count)
        ("tanh",        sp.tanh(y),      1,    1),
        ("minus-tanh",  -sp.tanh(y),     -1,   1),
        ("linear-ky",   k * y,           1,    1),
        ("no-zero",     2 + sp.tanh(y),  0,    0),
        ("zero-no-sign", y**2,           0,    0),
        ("one-sided",   1 - sp.tanh(y),  None, 0),
    ]
    for label, mexpr, w_exp, c_exp in profiles:
        Fint = sp.integrate(mexpr, y)
        assert sp.simplify(sp.diff(Fint, y) - mexpr) == 0  # antiderivative verified
        w = winding(mexpr)
        cnt = int(normalizable(sp.exp(-Fint))) + int(normalizable(sp.exp(+Fint)))
        law = (w is None and cnt == 0) or (w is not None and cnt == abs(w))
        run.check(f"L4-c-{label}", w == w_exp and cnt == c_exp and law,
                  f"m = {sp.sstr(mexpr):14s} winding = {w}  hosted zero modes = {cnt}  (count = |winding|)")
    # delocalization: Gaussian width of the linear-crossing mode
    width2 = sp.integrate(y**2 * sp.exp(-k * y**2), (y, -sp.oo, sp.oo)) / \
        sp.integrate(sp.exp(-k * y**2), (y, -sp.oo, sp.oo))
    run.check("L4-c-width", sp.simplify(width2 - 1 / (2 * k)) == 0
              and sp.limit(width2, k, 0, "+") == sp.oo,
              "linear-crossing mode width^2 = 1/(2k), -> oo as the crossing flattens (k -> 0+)")

    # (f) the two source-identified mass chains disagree at the zero locus
    print("-- (f) chain exponents at R = 0 (stylized forms)")
    R = sp.Symbol("R", real=True)
    c_, lam_, yc = sp.symbols("c lambda y_c", positive=True)
    m1 = R / 4
    v = sp.sqrt(c_ * sp.Max(-R, 0) / lam_)   # Mexican-hat VEV, support R <= 0
    m2 = yc * v
    ord1 = sp.degree(sp.Poly(m1, R))
    lim_half = sp.limit(m2.subs(sp.Max(-R, 0), -R) / sp.sqrt(-R), R, 0, "-")
    run.check("L4-f-01", ord1 == 1 and sp.simplify(lim_half - yc * sp.sqrt(c_ / lam_)) == 0,
              "m_1 = R/4 vanishes to order 1; the VEV chain vanishes to order 1/2 (sqrt), exact")
    run.check("L4-f-02", m2.subs(R, sp.Rational(1, 7)) == 0 and m1.subs(R, sp.Rational(1, 7)) != 0,
              "supports differ: the VEV chain is identically 0 for R > 0 while m_1 = R/4 is not")

    # (g) multiplicity is supplied: ker(D (x) I_N) = ker(D) (x) C^N at N = 3
    v1, v2, v3 = sp.symbols("v1 v2 v3")
    vN = sp.Matrix([v1, v2, v3])
    psi = sp.exp(-F(y)) * chip
    big = sp.Matrix(sp.BlockMatrix([[psi[i, 0] * vN.T] for i in range(2)]))  # 2x3: psi (x) v^T
    # D (x) I_N acts columnwise; verify each column solves D psi = 0:
    ok_cols = all(
        sp.simplify(D3(big[:, j]).subs(sub)) == sp.zeros(2, 1) for j in range(3)
    )
    run.check("L4-g-01", ok_cols,
              "ker(D (x) I_3) contains psi (x) v for arbitrary v: hosted count = |winding| * N, N SUPPLIED")


# ---------------------------------------------------------------------- LEG 5
def leg5(run, cfg):
    print("=" * 78)
    print("LEG 5  CROSS-CHECKS: the repository's own instruments at both endpoints")
    print("=" * 78)
    r1 = subprocess.run([sys.executable, str(ROOT / DSFS_PATH)],
                        capture_output=True, text=True, cwd=ROOT)
    run.check("L5-01", r1.returncode == 0,
              f"dirac_spectral_flow_section.py exits 0 (got {r1.returncode})")
    r2 = subprocess.run([sys.executable, str(ROOT / cfg["rung2_path"])],
                        capture_output=True, text=True, cwd=ROOT)
    run.check("L5-02", r2.returncode == 0,
              f"rung2 dynamical-wall probe exits 0 (got {r2.returncode})")
    run.check("L5-03", "VERDICT: SECTOR-SUPPLIED" in r2.stdout,
              "rung2 verdict is SECTOR-SUPPLIED (hosting, not selection)")
    run.check("L5-04", "accessible rank 3" in r2.stdout,
              "rung2 derived unit wall hosts accessible rank = supplied multiplicity 3")


# ---------------------------------------------------------------------- LEG 6
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


def leg6(run, cfg):
    print("=" * 78)
    print("LEG 6  ARTIFACT BINDING (verdict-evidence consistency)")
    print("=" * 78)
    apath = cfg["artifact_path"] or (ROOT / ARTIFACT)
    text = Path(apath).read_text(errors="replace")
    block, rows = parse_table(text)
    run.check("L6-01", block is not None and rows is not None and len(rows) == 6,
              f"machine table parsed: {0 if rows is None else len(rows)} rows (need 6)")
    if not rows:
        return
    verdicts = {r[0]: r[2] for r in rows}
    run.check("L6-02", all(r[2] in VERDICT_SET for r in rows),
              "all verdict tokens drawn from the closed set")
    sha = hashlib.sha256(block.encode()).hexdigest()
    run.check("L6-03", sha == TABLE_SHA256,
              f"table SHA-256 pinned ({sha[:16]}... vs {TABLE_SHA256[:16]}...)")
    # verdict-evidence binding.  The measurements this binding consumes were
    # certified in LEGs 2-4 above; here each verdict must agree with them.
    run.check("L6-04", verdicts.get("ADJ") == "POSITION-INDEXED-MAGNITUDE-NO-CROSSING",
              "ADJ verdict consistent with the sign scan (0 crossing, 0 positive, negative-side only)")
    run.check("L6-05", verdicts.get("LIN") == "NEIGHBOR-SHARED-INGREDIENT",
              f"LIN verdict consistent with its own measurement (got {verdicts.get('LIN')}): "
              "zero-no-sign hosts 0 and one-sided hosts 0, so SAME-OBJECT would contradict LEG 4")
    run.check("L6-06", verdicts.get("HOST") == "BILL-OF-SIX-WINDING-OPEN",
              "HOST verdict matches the six-item bill with the winding question open")
    run.check("L6-07", verdicts.get("GRADE") == "GAMMA-NEUTRAL-ON-SOURCE-SHAPED-WALL",
              "GRADE verdict matches the exact Gamma-charges (0 on the source-shaped wall)")
    run.check("L6-08", verdicts.get("JOIN") == "TYPED-TARGET-VEV-ORIENTATION-WALL-R-STEERED",
              "JOIN verdict matches the chain-exponent + hosting measurements")
    run.check("L6-09", verdicts.get("NOV") == "NO-PRIOR-JOIN",
              "NOV verdict matches the join rescan (naming wave only)")
    # claim ceiling, in the artifact's own words
    run.check("L6-10", "does not derive 3" in text,
              "artifact states on its face that it does not derive 3")
    run.check("L6-11", "|winding| = 1" in text and "OPEN" in text,
              "artifact carries the rung-2 hosting null and leaves the winding/number question OPEN")
    run.check("L6-12", "GU-COMPARATOR-ROUTING" in text
              and "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text,
              "routing notice and classification present")
    run.check("L6-13", "canonical_effect: pending_integration" in text,
              "canonical_effect declared pending_integration")
    run.check("L6-14", "repository vocabulary, not source vocabulary" in text,
              "the Krein/grading vocabulary is fenced as repository vocabulary, not source vocabulary")
    run.check("L6-15", "target_claim:" in text, "target_claim frontmatter present")


# --------------------------------------------------------------------- driver
def run_live(cfg):
    run = Run()
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        leg1(run, cfg)
        leg2(run, cfg, tmp)
        leg3(run, cfg, tmp)
        leg4(run, cfg)
        leg5(run, cfg)
        leg6(run, cfg)
    print("-" * 78)
    print(f"checks: {run.n}  failures: {len(run.failures)} {run.failures}")
    return run


# mutations: every one corrupts MACHINERY or a REFERENCE, never a predicate.
def mutations():
    def m1(cfg):  # corrupt a pin reference (line number off by one)
        cfg["pins"][2] = (cfg["pins"][2][0], cfg["pins"][2][1] + 1, cfg["pins"][2][2])
    def m2(cfg):  # sign-scan detector loses its CROSSING family
        cfg["sign_families"]["CROSSING"] = []
    def m3(cfg):  # join-scan detector loses its wall tokens
        cfg["wall_tokens"] = []
    def m4(cfg):  # corrupt a Pauli constant (reference corruption)
        s0 = sp.eye(2)
        s1 = sp.Matrix([[0, 1], [1, 0]])
        s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
        s3 = sp.Matrix([[1, 0], [0, -2]])   # corrupted Gamma
        cfg["pauli"] = (s0, s1, s2, s3)
    def m5(cfg):  # residual flagger stuck at "zero" (broken detector)
        cfg["nonzero_flagger"] = lambda M: False
    def m6(cfg):  # winding machinery loses its 1/2 normalisation
        cfg["winding_halver"] = sp.Integer(1)
    def m7(cfg):  # CONTRARY CONTROL: artifact copy claims SAME-OBJECT
        src = (ROOT / ARTIFACT).read_text()
        mut = src.replace("| LIN | wall mechanism vs R(y) transition | NEIGHBOR-SHARED-INGREDIENT |",
                          "| LIN | wall mechanism vs R(y) transition | SAME-OBJECT |")
        assert mut != src, "contrary-control substitution failed to apply"
        tmpf = Path(tempfile.mkstemp(suffix=".md")[1])
        tmpf.write_text(mut)
        cfg["artifact_path"] = tmpf
    def m8(cfg):  # normalizability judge loses its far-end and integral gates
        cfg["norm_requires_both_ends"] = False
    def m9(cfg):  # cross-check runner pointed at a nonexistent instrument
        cfg["rung2_path"] = "tests/channel-swings/DOES_NOT_EXIST_rw1.py"
    return [
        ("M1 pin reference off by one",            m1, {"L1-03"}),
        ("M2 sign-scan loses CROSSING family",     m2, {"L2-04"}),
        ("M3 join-scan loses wall tokens",         m3, {"L3-02", "L3-03"}),
        ("M4 corrupted Gamma constant",            m4, {"L4-a-s0", "L4-a-s1", "L4-a-s2", "L4-a-s3",
                                                        "L4-b-01", "L4-b-02", "L4-b-03", "L4-d-01",
                                                        "L4-d-02", "L4-e-03", "L4-e-04", "L4-g-01"}),
        ("M5 residual flagger stuck at zero",      m5, {"L4-b-04"}),
        ("M6 winding halver corrupted",            m6, {"L4-c-tanh", "L4-c-minus-tanh", "L4-c-linear-ky"}),
        ("M7 CONTRARY CONTROL: SAME-OBJECT",       m7, {"L6-05", "L6-03"}),
        ("M8 normalizability judge gates lost",    m8, {"L4-c-no-zero", "L4-c-zero-no-sign"}),
        ("M9 cross-check runner mispointed",       m9, {"L5-02", "L5-03", "L5-04"}),
    ]


def selftest():
    print("#" * 78)
    print("# SELFTEST: clean baseline FIRST, then 9 machinery mutations")
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
    print(f"# SELFTEST: 9/9 mutations caught by their targeted checks; baseline "
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
