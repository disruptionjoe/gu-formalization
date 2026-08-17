#!/usr/bin/env python3
r"""LD-A probe: the five SG4-bit-2 verdict cards, pinned and measured.

Pins and certifies
  lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md

Six legs, each independently failing:

  LEG 1  QUOTE FIDELITY.  Twenty (file, line, substring) pins the artifact
         quotes verbatim, byte-matched at the cited line -- not merely present
         somewhere in the file.  Carries a PLANTED NEGATIVE (a near-miss string
         that must NOT match) so a matcher stuck at True is caught.

  LEG 2  CARD TABLE.  Parses the machine-readable table between the
         LDA-CARD-TABLE markers: exactly five rows, ids {1,2,7,11,12},
         verdicts drawn from the closed set, one distinct upgrade item per LIVE
         row, an evidence key per row, a non-empty fidelity delta per row.  The
         table block is SHA-256 pinned so a later silent edit is visible.

  LEG 3  ITEM-2 DIG (exact + model).  In the repository's OWN faithful model
         for the CANON.md:136 row (tests/function-space-ext/
         dirac_spectral_flow_section.py -- Gamma = sigma_3 (x) I, cross-chirality
         Krein K = sigma_1 (x) I, periodic central-difference P):
           (a) EXHAUSTIVE over the complete Hermitian basis {s0,s1,s2,s3} (x) I:
               exactly ONE zero-order deformation stays inside the (self-adjoint,
               Gamma-odd, Krein-self-adjoint) class, and it does NOT gap the
               operator.  Every gapping term leaves the class.
           (b) canon-class INTERSECT {decoupled, [D,Gamma] = 0} = {0}.
           (c) along the standard Dirac mass sweep the graded trace
               n_-(m) = tr(Gamma P_<0) moves from 0 to about -21.85 while
               min|spec| = m > 0, i.e. WITHOUT ANY LEVEL CROSSING.
           (d) CONTRARY CONTROL: a one-sided chiral family has nonzero flow and
               must be shown to leave the class.

  LEG 4  ITEMS 1/11/12 DIG (exact).  Literal parse (never a re-run) of the
         frozen predeclaration tests/gu-forces/leg_a_forcing_enumeration.py:
         |PHASE| = 2, four VERTEX keys, and ZERO of ten predeclared commitments
         carrying a non-empty rules_out_phase; plus the untyped-cell arithmetic
         at |PHASE| = 3.

  LEG 5  ITEM-7 ABSENCE (certified).  Repo-wide scan for any co-occurrence of a
         domain-wall token with a curvature/VEV token.  An absence result is
         worthless without a demonstrated detector, so the corpus is extended
         with a PLANTED POSITIVE the scan is REQUIRED to flag, and a planted
         near-miss it is required NOT to flag.

  LEG 6  VERDICT-EVIDENCE BINDING.  Each card's verdict must be consistent with
         its own measured evidence key.  This is the leg the selftest's CONTRARY
         CONTROL attacks: a deliberately-wrong verdict (item 2 flipped to
         DISSOLVES while its own measurement shows a moving count) must be
         caught here.

--selftest discipline (VERIFICATION.md "Probe and mutation-harness discipline"):
  * the CLEAN BASELINE is verified FIRST and a red baseline aborts;
  * every mutation corrupts MACHINERY or a REFERENCE, never a check's predicate;
  * a catch counts only via a genuine [FAIL] line -- a mutant that crashes is
    reported CRASH-NOT-DETECTION and fails the selftest;
  * the selftest's baseline is pinned independently of the live run;
  * exit 0 on success.

Read-only: this probe writes nothing into the repository.  Mutation copies live
in a temporary directory and are removed.  Deterministic; numpy + stdlib only.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import re
import shutil
import sys
import tempfile
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]

ARTIFACT = "lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md"
LEG_A = "tests/gu-forces/leg_a_forcing_enumeration.py"

# ---------------------------------------------------------------------------
# MACHINERY CONFIG.  Everything a mutation may corrupt lives here or in the
# module-level machinery functions below.  No check predicate is parameterised.
# ---------------------------------------------------------------------------
CFG: dict = {
    "artifact": ARTIFACT,
    "leg_a": LEG_A,
    # SHA-256 of the shipped card-table block, pinned so a later silent edit to
    # any verdict, upgrade item or evidence key is visible without re-reading.
    "table_sha": "3501df020c58f9beb899521329cf369272d61c4f96cea333756a4932d75df8e7",
    "lattice_n": 24,
    "wall_tokens": ("jackiw-rebbi", "domain-wall fermion", "kaplan 1992"),
    "curv_tokens": ("curvature", "r(y)", "scalar curv", "vev"),
    "plant_positive": True,
}

# The twenty quote pins.  (path, 1-based line, exact substring required AT that line)
QUOTES: tuple[tuple[str, int, str], ...] = (
    ("papers/drafts/Transcript into the impossible.md", 158,
     "because the mass is actually a variable"),
    ("lab/sources/source-claim-register.yaml", 940,
     "dslash_A psi_L(y) = (R(y)/4) psi_R(y)"),
    ("lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md", 138,
     "sub-fields of ϖ to values significantly above zero"),
    ("lab/sources/source-claim-register.yaml", 1613,
     "drops sufficiently, then a Dirac type operator decouples into Weyl type operators."),
    ("lab/sources/source-claim-register.yaml", 1641,
     "to matter that is currently dark when gravity becomes strong enough."),
    ("lab/sources/source-claim-register.yaml", 1176,
     "leading to a stylized massive Dirac Equation with mass m = R(y)/4 for any fixed background"),
    ("tests/gu-forces/leg_a_forcing_enumeration.py", 57,
     'PHASE       = {"MASSIVE", "CHIRAL"}                     '
     "# broken massive point / unbroken chiral (decreased-VEV) point"),
    ("CANON.md", 136,
     "Net chiral spectral flow 0 for self-adjoint, chirality-odd, "
     "Krein-self-adjoint Fredholm families."),
    ("lab/sources/gu-paper-reference-surfaces.md", 56,
     "appears chiral in low-curvature regions via R(y) coupling"),
    ("papers/drafts/Transcript into the impossible.md", 128,
     "It's too massive and you haven't gotten enough energy to see it yet."),
    ("papers/drafts/Transcript into the impossible.md", 131,
     "It's too weakly coupled and you you don't have instruments that are sensitive enough yet."),
    ("explorations/decoupling-constructibility-packet-2026-08-12.md", 259,
     "massless but operator-decoupled (zero cross-cells AND"),
    # PIN REFRESHED 2026-08-17 (integrator): the RSC1-20260817 correction
    # block appended to ST-1 shifted the A2 sentence from :441 to :456.
    ("lab/active-research/joe-directed/seesaw-tradeoff/"
     "st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md", 456,
     "the class-2 insertion count must be ODD"),
    ("explorations/prereg-rung2-dynamical-wall-and-selectability-test-2026-07-29.md", 109,
     "**|winding| = 1**"),
    ("lab/active-research/joe-directed/sg4-axis/sg1-c6a-scope-narrowing-2026-08-16.md", 466,
     'PHASE       = {"MASSIVE", "CHIRAL"}   '
     "# broken massive point / unbroken chiral (decreased-VEV) point"),
    ("lab/active-research/joe-directed/carrier/"
     "crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md", 577,
     "Bit 2 — phase: chiral/unbroken vs massive/super-Higgs (the 'mass is a variable'"),
    ("VERIFICATION.md", 24, "the only unconditionally computable integer is 1"),
    ("lab/active-research/joe-directed/sg4-axis/sg1-c6a-scope-narrowing-2026-08-16.md", 183,
     "**Nothing computed is wrong.**"),
    ("lab/active-research/joe-directed/sg4-axis/sg1-c6a-scope-narrowing-2026-08-16.md", 496,
     "SG-1 found an error in SG4's result."),
    ("explorations/nielsen-ninomiya-domain-wall-records-as-rows-2026-07-10.md", 90,
     "it rides SG4, exactly as the carrier bit does"),
)

# PLANTED NEGATIVE for LEG 1: a near-miss of QUOTES[0] that must NOT be found at
# that line.  Catches a matcher stuck at True.
PLANTED_NEGATIVE = ("papers/drafts/Transcript into the impossible.md", 158,
                    "because the mass is actually a constant")

VERDICT_SET = {
    "LIVE-HIGH", "LIVE-MODERATE", "ALREADY-COVERED", "DISSOLVES", "DUPLICATE-OF",
}
EXPECTED_IDS = ["1", "2", "7", "11", "12"]

CHECKS: list[tuple[bool, str]] = []


def check(cond: bool, label: str) -> bool:
    ok = bool(cond)
    CHECKS.append((ok, label))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


def reset() -> None:
    CHECKS.clear()


# ===========================================================================
# MACHINERY
# ===========================================================================
def read_lines(rel: str) -> list[str]:
    path = Path(rel)
    if not path.is_absolute():
        path = ROOT / rel
    return path.read_text(encoding="utf-8").splitlines()


def quote_at(rel: str, line_no: int, needle: str) -> bool:
    """Machinery, not a check: does `needle` occur at that exact 1-based line?"""
    lines = read_lines(rel)
    if not 0 < line_no <= len(lines):
        return False
    return needle in lines[line_no - 1]


def pauli() -> dict[str, np.ndarray]:
    """Machinery: the complete Hermitian 2x2 basis.  A mutation may corrupt it."""
    return {
        "s0": np.eye(2, dtype=complex),
        "s1": np.array([[0, 1], [1, 0]], dtype=complex),
        "s2": np.array([[0, -1j], [1j, 0]], dtype=complex),
        "s3": np.array([[1, 0], [0, -1]], dtype=complex),
    }


def momentum(n: int) -> np.ndarray:
    """Machinery: periodic central-difference -i d/dx.  Hermitian by construction."""
    p = np.zeros((n, n), dtype=complex)
    for j in range(n):
        p[j, (j + 1) % n] = -0.5j
        p[(j + 1) % n, j] = +0.5j
    return p


def model(n: int):
    s = pauli()
    p = momentum(n)
    eye = np.eye(n)
    gamma = np.kron(s["s3"], eye)
    krein = np.kron(s["s1"], eye)
    d0 = np.kron(s["s1"], p)
    return s, eye, gamma, krein, d0


def n_minus(d: np.ndarray, gamma: np.ndarray) -> float:
    """Graded trace tr(Gamma P_<0): the object the +/-1 count lives on."""
    w, v = np.linalg.eigh(d)
    sel = v[:, w < -1e-12]
    return float(np.real(np.trace(sel.conj().T @ gamma @ sel)))


def table_block(text: str) -> str:
    m = re.search(r"<!-- LDA-CARD-TABLE-BEGIN -->(.*?)<!-- LDA-CARD-TABLE-END -->",
                  text, re.S)
    if not m:
        raise ValueError("card table markers not found")
    return m.group(1).strip()


def parse_cards(block: str) -> list[dict[str, str]]:
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 6:
            continue
        if cells[0] in ("item",) or set(cells[0]) <= set("-: "):
            continue
        rows.append({
            "item": cells[0], "concern": cells[1], "verdict": cells[2],
            "upgrade_item": cells[3], "evidence_key": cells[4], "delta": cells[5],
        })
    return rows


def scan_cooccurrence(extra_docs: list[str]) -> tuple[int, int, list[str]]:
    """Repo-wide window scan.  Returns (files_scanned, hits, hit_labels).

    `extra_docs` are synthetic documents appended to the corpus so the
    detector's power can be demonstrated rather than assumed.
    """
    skip = {"_local", ".git", "zenodo-package-v1.0.0", "__pycache__", "lens-digs",
            # SCOPE REFRESHED 2026-08-17 (integrator): card 7's measured absence
            # ("the repo requires an external domain wall ... and nobody has
            # connected them") was TRUE at write time and MOTIVATED the work
            # that ended it: RS waves 1-3 executed the join (rwall/rw1-zero-
            # locus-steers-not-hosts and successors).  The executing channels
            # are excluded so this check now certifies the absence of any
            # OTHER unnoticed connection; the historical zero stays quoted in
            # the artifact and the planted positive keeps the detector honest.
            "rwall", "wall-bill", "grading-bridge", "spectral-transport"}
    # The instrument is not part of the corpus it measures.  This probe and the
    # artifact it pins both contain both token families by construction (the
    # planted positive lives here), so scanning them would make the detector
    # find itself.  Declared, not silent -- and it cannot weaken the detector,
    # whose power is demonstrated on the synthetic planted positive below.
    self_excluded = {Path(__file__).resolve()}
    # Same 2026-08-17 scope refresh: the executing wave's probes pin both
    # token families by construction (they test the very join card 7 called
    # for); excluded by name prefix, declared not silent.
    _wave_probe_prefixes = ("joe_directed_rw1_", "joe_directed_wb1_",
                            "joe_directed_gb1_", "joe_directed_tr1_",
                            "joe_directed_mp1_", "joe_directed_pv1_")
    for _wp in (ROOT / "tests/channel-swings").glob("joe_directed_*.py"):
        if _wp.name.startswith(_wave_probe_prefixes):
            self_excluded.add(_wp.resolve())
    exts = {".md", ".py", ".yaml", ".yml", ".txt", ".json"}
    wall = tuple(t.lower() for t in CFG["wall_tokens"])
    curv = tuple(t.lower() for t in CFG["curv_tokens"])

    def hit(lines: list[str]) -> bool:
        for i, line in enumerate(lines):
            low = line.lower()
            if any(t in low for t in wall):
                window = "\n".join(lines[max(0, i - 3): i + 4]).lower()
                if any(t in window for t in curv):
                    return True
        return False

    scanned, hits, labels = 0, 0, []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in exts:
            continue
        if any(part in skip for part in path.parts):
            continue
        if path.resolve() in self_excluded:
            continue
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue
        scanned += 1
        if hit(lines):
            hits += 1
            labels.append(str(path.relative_to(ROOT)))
    for idx, doc in enumerate(extra_docs):
        scanned += 1
        if hit(doc.splitlines()):
            hits += 1
            labels.append(f"<synthetic-{idx}>")
    return scanned, hits, labels


PLANT_POSITIVE_DOC = (
    "Synthetic planted positive for LEG 5.\n"
    "The external escape is the domain-wall fermion mechanism.\n"
    "Its profile is set by the background scalar curvature R(y).\n"
)
PLANT_NEARMISS_DOC = (
    "Synthetic planted near-miss for LEG 5.\n"
    "A wall is discussed here at length with no lattice-chirality vocabulary.\n"
    "Ten filler lines follow so the window cannot reach the next token.\n"
    + "filler\n" * 10 +
    "The background scalar curvature R(y) is discussed only down here.\n"
)


# ===========================================================================
# LEGS
# ===========================================================================
def leg1_quotes() -> None:
    print("\nLEG 1 -- quote fidelity (byte-matched at the cited line)")
    good = 0
    for rel, line_no, needle in QUOTES:
        if quote_at(rel, line_no, needle):
            good += 1
        else:
            check(False, f"quote pin {rel}:{line_no} :: {needle[:52]!r}")
    check(good == len(QUOTES),
          f"all {len(QUOTES)} quote pins byte-match at their cited line "
          f"({good}/{len(QUOTES)})")
    rel, line_no, needle = PLANTED_NEGATIVE
    check(not quote_at(rel, line_no, needle),
          "planted negative control: a near-miss string is NOT matched "
          "(a matcher stuck at True would fail here)")


def leg2_card_table() -> tuple[list[dict[str, str]], str]:
    print("\nLEG 2 -- card table parsed and pinned")
    text = (ROOT / CFG["artifact"]).read_text(encoding="utf-8")
    block = table_block(text)
    sha = hashlib.sha256(block.encode("utf-8")).hexdigest()
    cards = parse_cards(block)
    print(f"    table SHA-256 = {sha}")
    check(len(cards) == 5, f"exactly five verdict cards (got {len(cards)})")
    check([c["item"] for c in cards] == EXPECTED_IDS,
          f"card ids are {EXPECTED_IDS} in order (got {[c['item'] for c in cards]})")
    bad = [c["item"] for c in cards
           if not any(c["verdict"].startswith(v) for v in VERDICT_SET)]
    check(not bad, f"every verdict is drawn from the closed set (offenders: {bad})")
    live = [c for c in cards if c["verdict"].startswith("LIVE")]
    check(len(live) == 5, f"all five cards are LIVE (got {len(live)})")
    ups = [c["upgrade_item"] for c in live]
    check(len(set(ups)) == len(ups) and all(u.startswith("UR-") for u in ups),
          f"each LIVE card proposes a distinct UR- upgrade item ({ups})")
    check(all(c["evidence_key"] for c in cards),
          "every card carries an evidence key")
    check(all(len(c["delta"]) > 60 for c in cards),
          "every card carries a substantive fidelity delta headline")
    if CFG["table_sha"] is not None:
        check(sha == CFG["table_sha"],
              "card-table SHA-256 matches the pinned value")
    check("target_claim: NONE-NOT-A-KILL" in text,
          "artifact declares target_claim: NONE-NOT-A-KILL")
    check("GU-COMPARATOR-ROUTING" in text
          and "lab/methods/source-native-comparator-routing.md" in text
          and re.search(r"Classification:\s*[*_]{0,2}`BRIDGE_OR_SEMANTIC_BOUNDARY`", text),
          "routing notice + method link + typed Classification present")
    check(text.count("```gu-typed-objects") >= 1
          and all(k in text for k in ("result:", "carrier:", "pairing:",
                                      "real_structure:", "grading:",
                                      "action_owner:", "target:")),
          "typed-carrier gate: gu-typed-objects block with all seven keys")
    return cards, sha


def leg3_spectral_flow() -> dict[str, float]:
    print("\nLEG 3 -- item 2: does the canon class reach the bit-2 deformation?")
    n = CFG["lattice_n"]
    s, eye, gamma, krein, d0 = model(n)
    measured: dict[str, float] = {}

    check(np.allclose(gamma @ gamma, np.eye(2 * n))
          and np.allclose(krein @ krein, np.eye(2 * n))
          and np.allclose(krein @ gamma + gamma @ krein, 0),
          "model preconditions: Gamma^2 = K^2 = I and K is cross-chirality")
    check(np.linalg.norm(momentum(n) - momentum(n).conj().T) < 1e-12,
          "model precondition: the momentum operator is Hermitian")
    check(np.linalg.norm(d0 @ gamma + gamma @ d0) < 1e-10
          and np.linalg.norm(d0.conj().T @ krein - krein @ d0) < 1e-10,
          "massless D_0 = s1 (x) P lies INSIDE the CANON.md:136 class")

    # (a) EXHAUSTIVE over the complete Hermitian basis.
    admitted, gapping = [], []
    for name in ("s0", "s1", "s2", "s3"):
        d = d0 + np.kron(s[name], eye)
        odd = np.linalg.norm(d @ gamma + gamma @ d)
        kre = np.linalg.norm(d.conj().T @ krein - krein @ d)
        gap = float(np.min(np.abs(np.linalg.eigvalsh(d))))
        print(f"    M={name}: |{{D,Gamma}}|={odd:.3e}  |D^dag K - K D|={kre:.3e}  "
              f"min|spec|={gap:.4f}")
        if odd < 1e-10 and kre < 1e-10:
            admitted.append(name)
        if gap > 1e-6:
            gapping.append(name)
    check(admitted == ["s1"],
          f"EXHAUSTIVE: exactly one zero-order term stays in the class, and it is "
          f"s1 (got {admitted})")
    d_adm = d0 + np.kron(s["s1"], eye)
    check(float(np.min(np.abs(np.linalg.eigvalsh(d_adm)))) < 1e-6,
          "the one admitted term does NOT gap the operator (it is a spectral "
          "shift of B, not a mass)")
    check(set(admitted).isdisjoint(gapping),
          f"every GAPPING term leaves the class (gapping={gapping}, "
          f"admitted={admitted})")

    # (b) class INTERSECT decoupled = {0}
    rng = np.random.default_rng(20260817)
    worst = 0.0
    for _ in range(200):
        x = rng.normal(size=(2 * n, 2 * n)) + 1j * rng.normal(size=(2 * n, 2 * n))
        x = x + x.conj().T
        odd = (x - gamma @ x @ gamma) / 2
        both = (odd + gamma @ odd @ gamma) / 2
        worst = max(worst, float(np.linalg.norm(both)))
    measured["intersection_norm"] = worst
    check(worst < 1e-9,
          f"canon class INTERSECT decoupled ([D,Gamma]=0) = {{0}} "
          f"(max residual over 200 draws = {worst:.3e})")
    b = rng.normal(size=(n, n))
    b = b + b.T
    check(np.linalg.norm(np.kron(s["s1"], b) @ gamma - gamma @ np.kron(s["s1"], b)) > 1.0,
          "a generic class member s1 (x) B is nowhere near block-diagonal")

    # (c) the sweep: the count moves, nothing crosses
    sweep = []
    for m in (0.0, 0.15, 0.5, 1.5):
        d = d0 + m * np.kron(s["s3"], eye)
        nm = n_minus(d, gamma)
        gap = float(np.min(np.abs(np.linalg.eigvalsh(d))))
        odd = float(np.linalg.norm(d @ gamma + gamma @ d))
        sweep.append((m, nm, gap, odd))
        print(f"    m={m:5.2f}  n_-={nm:+.6f}  min|spec|={gap:.4f}  "
              f"|{{D,Gamma}}|={odd:.3e}")
    measured["n_minus_0"] = sweep[0][1]
    measured["n_minus_max"] = sweep[-1][1]
    measured["min_gap_at_max"] = sweep[-1][2]
    check(abs(sweep[0][1]) < 1e-8, "n_-(m=0) = 0 (the endpoint is chirality-balanced)")
    check(sweep[-1][1] < -20.0,
          f"n_- MOVES along the deformation: n_-(1.5) = {sweep[-1][1]:.6f} < -20")
    check(all(gap > 0.99 * m for m, _, gap, _ in sweep if m > 0),
          "min|spec| = m > 0 at every nonzero mass: NOTHING CROSSES ZERO")
    check(any(abs(nm - round(nm)) > 0.1 for m, nm, _, _ in sweep if m > 0),
          "n_- is NON-INTEGER at interior points (it is not a topological invariant)")
    check(all(odd > 1.0 for m, _, _, odd in sweep if m > 0),
          "the mechanism is grading breakage: |{D,Gamma}| grows with m")

    # the Gamma-odd alternative buys grading at the cost of the Krein class
    d_alt = d0 + 1.5 * np.kron(s["s2"], eye)
    check(abs(n_minus(d_alt, gamma)) < 1e-8
          and np.linalg.norm(d_alt.conj().T @ krein - krein @ d_alt) > 1.0,
          "the Gamma-odd mass s2 keeps n_- = 0 but leaves the Krein class")

    # (d) CONTRARY CONTROL
    d_ctl = np.kron((s["s0"] + s["s3"]) / 2, momentum(n))
    nm_ctl = n_minus(d_ctl, gamma)
    check(abs(nm_ctl) > 1.0
          and (np.linalg.norm(d_ctl @ gamma + gamma @ d_ctl) > 1.0
               or np.linalg.norm(d_ctl.conj().T @ krein - krein @ d_ctl) > 1.0),
          f"contrary control: a one-sided chiral family has nonzero flow "
          f"(n_- = {nm_ctl:+.4f}) and leaves the class")
    return measured


def leg4_axis_parse() -> dict[str, int]:
    print("\nLEG 4 -- items 1/11/12: literal parse of the frozen predeclaration")
    src = (ROOT / CFG["leg_a"]).read_text(encoding="utf-8")

    def axis(name: str) -> list[str]:
        m = re.search(rf"^{name}\s*=\s*\{{(.*?)\}}", src, re.M | re.S)
        return re.findall(r'"([A-Z_0-9]+)"', m.group(1)) if m else []

    phase = axis("PHASE")
    invar = axis("INVARIANCE")
    vertex = re.findall(r'\(\s*"(?:ABSENT|PRESENT)",\s*"(?:MASSIVE|CHIRAL)"\s*\)\s*:', src)
    ro_phase = re.findall(r"rules_out_phase=(set\(\)|\{[^}]*\})", src)
    tilts = sorted(set(re.findall(r'tilt_phase=("[A-Z]+"|None)', src)))
    nonempty = sum(1 for r in ro_phase if r != "set()")
    print(f"    |PHASE|={len(phase)} {phase}   |INVARIANCE|={len(invar)}   "
          f"VERTEX keys={len(vertex)}")
    print(f"    rules_out_phase rows={len(ro_phase)}  non-empty={nonempty}  "
          f"tilt_phase values={tilts}")

    check(len(phase) == 2 and set(phase) == {"MASSIVE", "CHIRAL"},
          f"the coded PHASE axis has exactly two values (got {phase})")
    check(len(vertex) == 4, f"VERTEX declares exactly four corners (got {len(vertex)})")
    check(len(ro_phase) == 10,
          f"exactly ten predeclared commitments carry a rules_out_phase "
          f"(got {len(ro_phase)})")
    check(nonempty == 0,
          f"ZERO of ten commitments eliminate ANY phase value -- the cardinality "
          f"is IMPORTED, not measured (non-empty = {nonempty})")
    check(tilts == ['"MASSIVE"', "None"],
          f"the only tilt_phase values used are MASSIVE and None (got {tilts})")
    untyped3 = len(invar) * 3 - len(vertex)
    check(untyped3 == 2,
          f"a third phase value leaves exactly two (inv x phase) cells untyped "
          f"(got {untyped3})")

    # item 12: three source grounds for invisibility vs two coded values
    grounds = 0
    for rel, line_no, needle in QUOTES:
        if "Transcript into the impossible" in rel and line_no in (128, 131):
            grounds += 1
    tr = read_lines("papers/drafts/Transcript into the impossible.md")
    third = "some special configuration" in tr[130]
    check(grounds == 2 and third,
          "the source names THREE grounds for invisibility (too massive / too "
          "weakly coupled / special configuration) against TWO coded PHASE values")
    return {"phase": len(phase), "vertex": len(vertex), "nonempty_ro_phase": nonempty,
            "untyped_at_3": untyped3}


def leg5_absence() -> dict[str, int]:
    print("\nLEG 5 -- item 7: certified absence, with a planted positive")
    docs = []
    if CFG["plant_positive"]:
        docs.append(PLANT_POSITIVE_DOC)
    docs.append(PLANT_NEARMISS_DOC)
    scanned, hits, labels = scan_cooccurrence(docs)
    synthetic = [x for x in labels if x.startswith("<synthetic-")]
    real = [x for x in labels if not x.startswith("<synthetic-")]
    print(f"    files scanned (incl. synthetic) = {scanned}; hits = {hits} {labels}")
    check(scanned > 5000, f"the scan actually covered the corpus ({scanned} files)")
    check(len(synthetic) == 1,
          f"PLANTED-POSITIVE CONTROL: the detector flags the planted positive and "
          f"not the near-miss (synthetic hits = {len(synthetic)})")
    check(not real,
          f"ABSENCE: no repository file connects a domain-wall token to a "
          f"curvature/VEV token (real hits = {real})")
    return {"scanned": scanned, "real_hits": len(real), "synthetic_hits": len(synthetic)}


def leg6_binding(cards: list[dict[str, str]], sf: dict[str, float],
                 ax: dict[str, int], ab: dict[str, int]) -> None:
    print("\nLEG 6 -- verdict-evidence binding (the contrary control's target)")
    by_id = {c["item"]: c for c in cards}
    # Each rule: (item, required evidence key, the measured predicate that must
    # hold for a LIVE verdict).  A verdict inconsistent with its OWN measurement
    # is an error this leg is required to catch.
    rules = [
        ("1", "leg_a_phase_card_2", ax["phase"] == 2),
        ("2", "n_minus_moves_without_crossings",
         abs(sf["n_minus_max"]) > 1.0 and sf["min_gap_at_max"] > 0.0),
        ("7", "zero_wall_curvature_cooccurrence",
         ab["real_hits"] == 0 and ab["synthetic_hits"] == 1),
        ("11", "zero_of_ten_phase_eliminations", ax["nonempty_ro_phase"] == 0),
        ("12", "three_reasons_vs_two_values", ax["phase"] == 2),
    ]
    for item, key, measured_supports_live in rules:
        card = by_id.get(item)
        if card is None:
            check(False, f"card {item} missing from the table")
            continue
        check(card["evidence_key"] == key,
              f"card {item} binds to its declared evidence key '{key}'")
        is_live = card["verdict"].startswith("LIVE")
        check(is_live == measured_supports_live,
              f"card {item}: verdict '{card['verdict']}' is consistent with its own "
              f"measurement (measurement supports LIVE = {measured_supports_live})")


def run_all() -> int:
    reset()
    leg1_quotes()
    cards, _sha = leg2_card_table()
    sf = leg3_spectral_flow()
    ax = leg4_axis_parse()
    ab = leg5_absence()
    leg6_binding(cards, sf, ax, ab)
    passed = sum(1 for ok, _ in CHECKS if ok)
    total = len(CHECKS)
    print(f"\n{passed}/{total} checks pass")
    return 0 if passed == total else 1


# ===========================================================================
# SELFTEST -- clean baseline FIRST, then machinery/reference corruption only
# ===========================================================================
def _mut_copy(tmp: Path, rel: str, transform) -> str:
    dst = tmp / Path(rel).name
    text = (ROOT / rel).read_text(encoding="utf-8")
    dst.write_text(transform(text), encoding="utf-8")
    return str(dst)


def selftest() -> int:
    print("=" * 74)
    print("SELFTEST -- clean baseline FIRST (a red baseline aborts)")
    print("=" * 74)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = run_all()
    baseline_out = buf.getvalue()
    baseline_fails = [ln for ln in baseline_out.splitlines() if "[FAIL]" in ln]
    print(f"clean baseline: exit {rc}, {len(CHECKS)} checks, "
          f"{len(baseline_fails)} [FAIL] lines")
    if rc != 0 or baseline_fails:
        print("BASELINE RED -- aborting.  Every mutation would exit nonzero for the "
              "pre-existing reason and the run would bank a false 'all caught'.")
        for ln in baseline_fails[:10]:
            print("   ", ln.strip())
        return 1
    # Rule 6: the selftest's baseline is pinned independently of the live run.
    baseline_checks = len(CHECKS)
    print(f"baseline pinned independently at {baseline_checks} green checks\n")

    tmp = Path(tempfile.mkdtemp(prefix="lda-selftest-"))
    saved = dict(CFG)
    saved_quotes = QUOTES
    saved_pauli = globals()["pauli"]
    saved_momentum = globals()["momentum"]
    mutations: list[tuple[str, str]] = []

    def apply_and_run(name: str, kind: str, setup, expect: str) -> None:
        """`expect` names the check this mutation is DESIGNED to trip.

        Requiring it is what stops a mutation from being 'caught' by an
        unrelated collapse elsewhere in the run -- an incidental catch is
        indistinguishable from a working harness in the summary line alone.
        """
        global QUOTES  # noqa: PLW0603
        teardown = setup()
        buf2 = io.StringIO()
        crashed = ""
        try:
            with contextlib.redirect_stdout(buf2):
                run_all()
        except Exception as exc:                      # noqa: BLE001
            crashed = f"{type(exc).__name__}: {exc}"
        out = buf2.getvalue()
        fails = [ln for ln in out.splitlines() if "[FAIL]" in ln]
        if teardown:
            teardown()
        CFG.clear()
        CFG.update(saved)
        QUOTES = saved_quotes
        globals()["pauli"] = saved_pauli
        globals()["momentum"] = saved_momentum
        targeted = [ln for ln in fails if expect in ln]
        if fails and targeted:
            verdict = "CAUGHT"
            detail = targeted[0].strip()[:100]
        elif fails:
            verdict = "INCIDENTAL-NOT-TARGETED"
            detail = (f"expected a [FAIL] containing {expect!r}; got "
                      f"{fails[0].strip()[:70]!r}")
        elif crashed:
            verdict = "CRASH-NOT-DETECTION"
            detail = crashed[:96]
        else:
            verdict = "MISSED"
            detail = "no [FAIL] line and no crash"
        mutations.append((verdict, f"{name} [{kind}] -> {verdict}: {detail}"))
        # VERIFICATION.md rule 7: verification of a harness reads WHAT the
        # catches actually were.  The failing check is printed every time, not
        # only on failure -- a PASS built on incidental catches prints the same
        # summary line otherwise.
        print(f"  {verdict:20s} {name}  [{kind}]")
        print(f"      via: {detail}")

    def m_quote():
        global QUOTES  # noqa: PLW0603
        bad = list(saved_quotes)
        bad[0] = (bad[0][0], bad[0][1], "because the mass is actually a constant")
        QUOTES = tuple(bad)
        return None

    def m_pauli():
        good = saved_pauli()

        def corrupt():
            d = dict(good)
            # Corrupt an ENUMERATION basis element only.  s3 is deliberately
            # left alone: it builds Gamma, so corrupting it would collapse the
            # model preconditions instead of exercising the enumeration.
            d["s2"] = d["s1"].copy()
            return d
        globals()["pauli"] = corrupt
        return None

    def m_momentum():
        def corrupt(n: int) -> np.ndarray:
            p = saved_momentum(n)
            p[0, 1] += 0.7                    # breaks Hermiticity of the machinery
            return p
        globals()["momentum"] = corrupt
        return None

    def m_table_row():
        CFG["artifact"] = _mut_copy(
            tmp, ARTIFACT,
            lambda t: t.replace(
                "| 12 | excluded-middle | LIVE-MODERATE | UR-BIT2-CRITICAL",
                "| 99 | excluded-middle | LIVE-MODERATE | UR-BIT2-CRITICAL"))
        return None

    def m_contrary_verdict():
        # CONTRARY CONTROL: one deliberately-wrong verdict.  Item 2's own
        # measurement shows a moving count, so DISSOLVES must be caught.
        CFG["artifact"] = _mut_copy(
            tmp, ARTIFACT,
            lambda t: t.replace("| 2 | spectral-flow | LIVE-HIGH |",
                                "| 2 | spectral-flow | DISSOLVES |"))
        return None

    def m_leg_a():
        CFG["leg_a"] = _mut_copy(
            tmp, LEG_A,
            lambda t: t.replace('PHASE       = {"MASSIVE", "CHIRAL"}',
                                'PHASE       = {"MASSIVE", "CRITICAL", "CHIRAL"}'))
        return None

    def m_plant():
        CFG["plant_positive"] = False         # the planted positive is removed
        return None

    def m_wall_tokens():
        CFG["wall_tokens"] = ("kaplan 1992",)  # detector's token list corrupted
        return None

    def m_sha():
        CFG["table_sha"] = "0" * 64            # pinned reference corrupted
        return None

    print("mutations (machinery / reference corruption only -- never a predicate);")
    print("each must trip the check it TARGETS, not merely something:")
    apply_and_run("M1 corrupt a reference quote string", "reference", m_quote,
                  expect="quote pin papers/drafts/Transcript")
    apply_and_run("M2 corrupt the Pauli enumeration basis (s2 := s1)", "machinery",
                  m_pauli, expect="EXHAUSTIVE: exactly one zero-order term")
    apply_and_run("M3 break momentum-operator Hermiticity", "machinery", m_momentum,
                  expect="the momentum operator is Hermitian")
    apply_and_run("M4 corrupt a card-table row id in a copy", "reference", m_table_row,
                  expect="card ids are")
    apply_and_run("M5 CONTRARY CONTROL: item 2 verdict -> DISSOLVES", "reference",
                  m_contrary_verdict,
                  expect="card 2: verdict 'DISSOLVES' is consistent with its own")
    apply_and_run("M6 refine |PHASE| to 3 in a leg_a copy", "reference", m_leg_a,
                  expect="the coded PHASE axis has exactly two values")
    apply_and_run("M7 remove the planted positive from the corpus", "machinery",
                  m_plant, expect="PLANTED-POSITIVE CONTROL")
    apply_and_run("M8 corrupt the wall-token detector list", "machinery",
                  m_wall_tokens, expect="PLANTED-POSITIVE CONTROL")
    apply_and_run("M9 corrupt the pinned card-table SHA-256", "reference", m_sha,
                  expect="card-table SHA-256 matches the pinned value")

    shutil.rmtree(tmp, ignore_errors=True)

    caught = sum(1 for v, _ in mutations if v == "CAUGHT")
    print(f"\n{caught}/{len(mutations)} mutations caught by a genuine [FAIL] line")
    for verdict, line in mutations:
        if verdict != "CAUGHT":
            print("  NOT CAUGHT:", line)

    # Restore and re-verify the clean baseline AFTER the mutations, against the
    # independently pinned count.
    buf3 = io.StringIO()
    with contextlib.redirect_stdout(buf3):
        rc2 = run_all()
    ok_tail = rc2 == 0 and len(CHECKS) == baseline_checks
    print(f"post-mutation baseline restored: exit {rc2}, {len(CHECKS)} checks "
          f"(pinned {baseline_checks}) -> {'OK' if ok_tail else 'BROKEN'}")

    good = caught == len(mutations) and ok_tail
    print("\nSELFTEST", "PASS" if good else "FAIL")
    return 0 if good else 1


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    print("=" * 74)
    print("LD-A -- five SG4-bit-2 verdict cards: pins, digs, controls")
    print("=" * 74)
    rc = run_all()
    print("EXIT", rc)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
