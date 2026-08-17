#!/usr/bin/env python3
r"""GB-1 probe: the W3 grading bridge — one exact angle, one missing arrow.

Pins and certifies
  lab/active-research/joe-directed/grading-bridge/
      gb1-the-bridge-is-one-angle-and-one-missing-arrow-2026-08-17.md

Six legs, each independently failing:

  LEG 1  QUOTE FIDELITY.  43 (file, line, substring) pins byte-matched at
         their cited lines — the W3 target text (rw1:276-286, :368-375,
         :824-825), the canon count rows (CANON.md:135/136/139), the doorway
         sentences (instrument:29, synthesis:56/60), the count object
         (instrument:18, lda:9/:301), LD-B's parity rows (ldb:198/200/211),
         the four-way homonym (packet:69 twice, 77-rerun:59/:201), the
         register fences (homonym-register:242/:263/:1186, NAMES.md:18), the
         LA1/W6 boundary (gu-base-categories:89/:106/:291), the source rows
         (register:913/:940) and the correction-registry operative sentences
         (:267/:302/:305/:367).  Planted negative: "Net chiral spectral
         flow 1" must NOT match at CANON.md:136.

  LEG 2  RW-1 REPRODUCTION (exact sympy; FENCED — binds the model only).
         Pinned re-runs of rw1 §4 (a)(b)(d)(e) on the continuum fiber of
         tests/function-space-ext/dirac_spectral_flow_section.py: the
         class/gap table over the complete Pauli basis; the Jackiw-Rebbi
         reduction for generic m(y) on both walls; ambient Gamma-charges
         EXACTLY 0 (sigma_3 wall) and EXACTLY -1 (sigma_2 wall); hosted-mode
         K-charges 0; U = exp(-i pi sigma_1/4) unitary, kinetic-commuting,
         sigma_3 -> +-sigma_2, NOT Gamma-preserving.  A planted
         wrong-chirality candidate must be flagged NONZERO.

  LEG 3  THE CIRCLE (exact sympy, generic angle AND generic profile).
         M(phi) = cos(phi) sigma_3 + sin(phi) sigma_2; wall grading
         G(phi) = M(phi + pi/2); v_+- = U(-phi) chi_+- are exact zero modes
         exp(-+int m) v_+-; hosted Gamma-charge = -sin(phi) (anti-kink
         +sin(phi)); K-charge = 0 at every angle with K v_+ = i v_- and
         {K, G(phi)} = 0; {M,Gamma} = 2 cos(phi) I; [M,K]^H[M,K] = 4I
         (uniform Krein exit); charge^2 + cos^2 = 1 (full charge iff
         Krein-only exit); commutant of sigma_1 is span{I, sigma_1}; the
         kinetic-preserving circle is a Krein isometry rotating mass and
         grading jointly (relative angle invariant; transported-grading
         charge stays 0; fixed-Gamma charge of the transported source wall
         = sin(theta)); ker(D (x) I_3) = ker(D) (x) C^3 at generic phi; the
         commuting-K contrast (K' = Gamma, the q-even/(14,0) face) has
         zero-order class exactly {0}.

  LEG 4  INSTRUMENTS.  Both repository instruments re-run green with pinned
         verdict strings: dirac_spectral_flow_section.py (exit 0,
         "(EXACTLY 0)") and krein_spectral_flow_probe.py (exit 0, paired
         flow "+0", one-sided control "+1", "WC-FUNCTION-SPACE-EXT remains
         open").

  LEG 5  CERTIFIED ABSENCES.  (a) "now quantified" is absent from the RW-1
         artifact (deviation D1); (b) the novelty tokens ("gapping circle",
         "wall angle", "relative angle", "charge is minus sine") have zero
         hits repo-wide outside this arc's own two files, with joiners
         inside the concurrent wave trees reported-not-failed; (c) the
         destination carries no duplicate gb1 seed.  Each absence carries a
         planted-positive control the detector is REQUIRED to flag.

  LEG 6  ARTIFACT BINDING.  Parses the machine table between the GB1-TABLE
         markers (eight rows, closed verdict set), SHA-256 pins the block,
         enforces verdict-evidence consistency (the CIRCLE row is cross-
         linked to the symbolic charge law; the selftest's contrary control
         flips W3 to DISCHARGED and must be caught here), and enforces the
         claim ceiling in the artifact's own text.

--selftest discipline (VERIFICATION.md:70 "Probe and mutation-harness
discipline (adopted 2026-08-17)", all seven rules):
  * the CLEAN BASELINE is verified FIRST and a red baseline aborts;
  * the baseline check count is pinned independently and re-verified after
    the mutations;
  * every mutation corrupts MACHINERY or a REFERENCE, never a check's
    predicate;
  * a catch counts only via a genuine [FAIL] line — a mutant that crashes is
    CRASH-NOT-DETECTION and fails; a catch with empty intersection with the
    mutation's targeted checks is INCIDENTAL-NOT-TARGETED and fails;
  * tolerances cannot absorb plants: every LEG 2/3 statement is symbolic;
  * the failing checks are printed for every mutation (rule 7);
  * exit 0 on success.

Read-only: the probe writes nothing into the repository.  Planted-control
files and the contrary-control artifact copy live in a temp directory and are
removed.  Deterministic; sympy + stdlib (numpy only inside the re-run
instruments).
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]

ARTIFACT = ("lab/active-research/joe-directed/grading-bridge/"
            "gb1-the-bridge-is-one-angle-and-one-missing-arrow-2026-08-17.md")
SELF_PROBE = ("tests/channel-swings/"
              "joe_directed_gb1_the_bridge_is_one_angle_and_one_missing_arrow.py")
RW1 = "lab/active-research/joe-directed/rwall/rw1-zero-locus-steers-not-hosts-2026-08-17.md"

# ----------------------------------------------------------------- LEG 1 pins
PINS = [
    (RW1, 276, "W3 — the grading bridge (measured, and it is the sharpest item)"),
    (RW1, 278, "source-shaped mass direction that charge is EXACTLY ZERO in the ambient"),
    (RW1, 280, "cross-chirality Krein grading of `CANON.md:136/139`), a typed bridge from"),
    (RW1, 285, "by a grading-rotating unitary (§4e) — the count is a grading question,"),
    (RW1, 368, "ambient Gamma-charge EXACTLY 0 (chi_+-^dag sigma_3 chi_+- = 0, exact)"),
    (RW1, 370, "Gamma eigenstate with charge EXACTLY -1, and that wall's class exit is"),
    (RW1, 371, "Krein-only — precisely the exit canon's control says a nonzero net count"),
    (RW1, 372, "The source's stylized toy does not distinguish these two mass"),
    (RW1, 375, "**(e) Grading transport.** U = exp(-i pi sigma_1/4) is unitary, commutes"),
    (RW1, 824, "W1 and W3 are the two items on"),
    ("CANON.md", 135, "net chiral index = flux number (any integer, odd for odd flux)"),
    ("CANON.md", 136,
     "Net chiral spectral flow 0 for self-adjoint, chirality-odd, Krein-self-adjoint Fredholm families"),
    ("CANON.md", 139, "interior-even + external-topological-index"),
    ("VERIFICATION.md", 70, "Probe and mutation-harness discipline (adopted 2026-08-17)"),
    ("canon/external-by-structure-synthesis-RESULTS.md", 56, "breaks the interior Krein-self-adjoint"),
    ("canon/external-by-structure-synthesis-RESULTS.md", 60, "necessarily external"),
    ("tests/function-space-ext/dirac_spectral_flow_section.py", 8, "Gamma = sigma_3 (x) I_N"),
    ("tests/function-space-ext/dirac_spectral_flow_section.py", 9, "K     = sigma_1 (x) I_N"),
    ("tests/function-space-ext/dirac_spectral_flow_section.py", 18,
     "n_-(t) = tr(Gamma P_{<0}(t)) = 0 identically"),
    ("tests/function-space-ext/dirac_spectral_flow_section.py", 29,
     "Nonzero flow requires leaving the Krein-Dirac class"),
    ("lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md", 9,
     "graded chirality trace tr(Gamma P_<0)"),
    ("lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md", 301,
     "graded trace `n_-(m) = tr(Gamma P_{<0})`"),
    ("lab/active-research/joe-directed/lens-digs/ldb-bit2-direction-and-krein-parity-2026-08-17.md", 198,
     "(9,5)"),
    ("lab/active-research/joe-directed/lens-digs/ldb-bit2-direction-and-krein-parity-2026-08-17.md", 198,
     "<- PHYSICAL"),
    ("lab/active-research/joe-directed/lens-digs/ldb-bit2-direction-and-krein-parity-2026-08-17.md", 200,
     "(7,7)"),
    ("lab/active-research/joe-directed/lens-digs/ldb-bit2-direction-and-krein-parity-2026-08-17.md", 211,
     "`{K, chi} = 0` exactly at odd `q`"),
    ("explorations/decoupling-constructibility-packet-2026-08-12.md", 69, "four-way homonym"),
    ("explorations/decoupling-constructibility-packet-2026-08-12.md", 69,
     "PH-K1-PHYSICAL's open map — never silently identified"),
    ("explorations/chirality-grading-and-77-rerun-2026-08-03.md", 59, "HOMONYM (four-way, ruling R5)"),
    ("explorations/chirality-grading-and-77-rerun-2026-08-03.md", 201,
     "every internal chirality half appears with both base-side chiralities in equal multiplicity"),
    ("lab/process/homonym-register.yaml", 242, "token: CHIRAL"),
    ("lab/process/homonym-register.yaml", 263,
     'write "CHIRAL (massless/unbroken)" when naming the PHASE value'),
    ("lab/process/homonym-register.yaml", 1186, "token: Rarita-Schwinger"),
    ("lab/process/NAMES.md", 18, "the Krein form `K = eta_V (x) beta_S`"),
    ("lab/methods/gu-base-categories.md", 89, "NOT injective"),
    ("lab/methods/gu-base-categories.md", 106, "N2 | inverse observation L2 -> L1"),
    ("lab/methods/gu-base-categories.md", 291, "(s^* omega)_mu = omega_mu + omega_(ab) d_mu g_ab"),
    ("lab/sources/source-claim-register.yaml", 913, "non-chiral total theory splits at the emergent"),
    ("lab/sources/source-claim-register.yaml", 940, "dslash_A psi_L(y) = (R(y)/4) psi_R(y)"),
    ("lab/process/correction-registry.yaml", 267, "FORCED and SUBTRACTIVE"),
    ("lab/process/correction-registry.yaml", 302, "when observed chirality is VEV-CONDITIONAL"),
    ("lab/process/correction-registry.yaml", 305, "selector is SG4 bit 2, OPEN by design"),
    ("lab/process/correction-registry.yaml", 367, "partner-placement / decoupling OBLIGATION"),
]
PLANTED_NEGATIVE_PIN = ("CANON.md", 136, "Net chiral spectral flow 1")

# ----------------------------------------------------------------- LEG 4 refs
DSFS_PATH = "tests/function-space-ext/dirac_spectral_flow_section.py"
KREIN_PATH = "tests/function-space-ext/krein_spectral_flow_probe.py"

# ----------------------------------------------------------------- LEG 5 refs
NOVELTY_TOKENS = ["gapping circle", "wall angle", "relative angle", "charge is minus sine"]
WAVE_TREES = ("lab/active-research/joe-directed/", "tests/channel-swings/")
SELF_FILES = {ARTIFACT, SELF_PROBE}

# ----------------------------------------------------------------- LEG 6 refs
TABLE_BEGIN = "<!-- GB1-TABLE-BEGIN -->"
TABLE_END = "<!-- GB1-TABLE-END -->"
TABLE_SHA256 = "0515a2591521b2bbda2fba5693f608ef4551b9cdd35cafc92c44ee0628060294"
VERDICT_SET = {
    "FOUR-NODES-TYPED-KREIN-IS-DOOR-NOT-SENSE",
    "AMBIENT-GAMMA-IN-CROSS-KREIN-REALIZATION",
    "REPRODUCED-EXACT",
    "CHARGE-IS-MINUS-SINE-RELATIVE-ANGLE",
    "FULL-CHARGE-IFF-KREIN-ONLY-EXIT",
    "TRANSPORT-CANNOT-DIRECTION-MUST",
    "ONE-MISSING-ARROW-NOT-DISCHARGED-NOT-OBSTRUCTED",
    "HANDOFF-AT-LA1-UNTYPED-NOT-ABSORBED",
    # inconsistent-with-measurement tokens kept in the closed set so the
    # BINDING leg (not a vocabulary error) catches them:
    "DISCHARGED",
    "OBSTRUCTED-KILL",
}
EXPECTED_VERDICTS = {
    "ENUM": "FOUR-NODES-TYPED-KREIN-IS-DOOR-NOT-SENSE",
    "COUNT": "AMBIENT-GAMMA-IN-CROSS-KREIN-REALIZATION",
    "REPRO": "REPRODUCED-EXACT",
    "CIRCLE": "CHARGE-IS-MINUS-SINE-RELATIVE-ANGLE",
    "DOOR": "FULL-CHARGE-IFF-KREIN-ONLY-EXIT",
    "UNIT": "TRANSPORT-CANNOT-DIRECTION-MUST",
    "W3": "ONE-MISSING-ARROW-NOT-DISCHARGED-NOT-OBSTRUCTED",
    "W6": "HANDOFF-AT-LA1-UNTYPED-NOT-ABSORBED",
}

BASELINE_COUNT = 114  # pinned independently; the selftest verifies before AND after


# ---------------------------------------------------------------- machinery
def default_cfg():
    return {
        "pins": [tuple(p) for p in PINS],
        "planted_negative_pin": PLANTED_NEGATIVE_PIN,
        "pauli": None,            # None -> the true Pauli matrices
        "nonzero_flagger": None,  # None -> the true symbolic nonzero flagger
        "charge_law": None,       # None -> the true law  phi -> -sin(phi)
        "circle_gen": None,       # None -> sigma_1 (the kinetic direction)
        "contrast_kprime": None,  # None -> sigma_3 (the commuting-K' contrast form)
        "novelty_tokens": list(NOVELTY_TOKENS),
        "krein_probe_path": KREIN_PATH,
        "artifact_path": None,    # None -> the real artifact
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


def charge_law(cfg):
    if cfg["charge_law"] is not None:
        return cfg["charge_law"]
    return lambda ph: -sp.sin(ph)


# ---------------------------------------------------------------------- LEG 1
def leg1(run, cfg):
    print("=" * 78)
    print("LEG 1  QUOTE FIDELITY (byte pins at cited lines)")
    print("=" * 78)
    for i, (path, ln, sub) in enumerate(cfg["pins"], 1):
        lines = read_lines(path)
        ok = ln <= len(lines) and sub in lines[ln - 1]
        run.check(f"L1-{i:02d}", ok, f"{path}:{ln} :: {sub[:46]!r}")
    path, ln, sub = cfg["planted_negative_pin"]
    lines = read_lines(path)
    run.check("L1-neg", not (ln <= len(lines) and sub in lines[ln - 1]),
              f"planted negative: {sub!r} absent at {path}:{ln}")


# ---------------------------------------------------------------------- LEG 2
def leg2(run, cfg):
    print("=" * 78)
    print("LEG 2  RW-1 REPRODUCTION (exact sympy) -- FENCED: binds the model only")
    print("=" * 78)
    s0, s1, s2, s3 = pauli(cfg)
    Z2, Z21 = sp.zeros(2, 2), sp.zeros(2, 1)
    y, p, m = sp.symbols("y p m", real=True)

    # (a) class/gap algebra
    expected = {"s0": (False, True, False), "s1": (True, True, False),
                "s2": (True, False, True), "s3": (False, False, True)}
    for name, M in [("s0", s0), ("s1", s1), ("s2", s2), ("s3", s3)]:
        godd = sp.simplify(M * s3 + s3 * M) == Z2
        krein = sp.simplify(M.H * s1 - s1 * M) == Z2
        evs = list((s1 * p + m * M).eigenvals().keys())
        gapped = all(sp.simplify(e - sp.sqrt(p**2 + m**2)) == 0 or
                     sp.simplify(e + sp.sqrt(p**2 + m**2)) == 0 for e in evs)
        run.check(f"L2-a-{name}", (godd, krein, gapped) == expected[name],
                  f"{name}: Gamma-odd={godd} Krein-ok={krein} gapped={gapped}")

    # (b) mode reduction, generic m(y), both walls
    mfun, F = sp.Function("m"), sp.Function("F")
    sub = {sp.Derivative(F(y), y): mfun(y)}
    chip = sp.Matrix([1, sp.I]) / sp.sqrt(2)
    chim = sp.Matrix([1, -sp.I]) / sp.sqrt(2)
    e1, e2 = sp.Matrix([1, 0]), sp.Matrix([0, 1])

    def D3(psi):
        return -sp.I * s1 * psi.diff(y) + mfun(y) * s3 * psi

    def D2w(psi):
        return -sp.I * s1 * psi.diff(y) + mfun(y) * s2 * psi

    ok3 = (sp.simplify(D3(sp.exp(-F(y)) * chip).subs(sub)) == Z21 and
           sp.simplify(D3(sp.exp(+F(y)) * chim).subs(sub)) == Z21)
    run.check("L2-b-red3", ok3, "sigma_3 wall: exp(-+int m) chi_+- are exact zero modes")
    ok2 = (sp.simplify(D2w(sp.exp(-F(y)) * e2).subs(sub)) == Z21 and
           sp.simplify(D2w(sp.exp(+F(y)) * e1).subs(sub)) == Z21)
    run.check("L2-b-red2", ok2, "sigma_2 wall: exp(-+int m) e_2/e_1 are exact zero modes")
    flag = nonzero_flagger(cfg)
    rw = sp.simplify(D3(sp.exp(-F(y)) * chim).subs(sub))
    run.check("L2-b-flag", flag(rw), "PLANTED wrong-chirality candidate flagged NONZERO")

    # (d) charges
    run.check("L2-d-charge0",
              sp.simplify((chip.H * s3 * chip)[0]) == 0 and sp.simplify((chim.H * s3 * chim)[0]) == 0,
              "source-shaped wall modes: ambient Gamma-charge EXACTLY 0")
    run.check("L2-d-charge1", sp.simplify((e2.T * s3 * e2)[0]) == -1,
              "sigma_2 wall mode: ambient Gamma-charge EXACTLY -1")
    run.check("L2-d-knull",
              sp.simplify((chip.H * s1 * chip)[0]) == 0 and sp.simplify((e2.T * s1 * e2)[0]) == 0,
              "both hosted modes: K-charge EXACTLY 0")

    # (e) the RW-1 unitary
    U = sp.cos(sp.pi / 4) * s0 - sp.I * sp.sin(sp.pi / 4) * s1
    run.check("L2-e-unitary", sp.simplify(U * U.H - s0) == Z2, "U = exp(-i pi sigma_1/4) unitary")
    run.check("L2-e-kinetic", sp.simplify(U * s1 * U.H - s1) == Z2, "U commutes with kinetic sigma_1")
    c3 = sp.simplify(U * s3 * U.H)
    run.check("L2-e-rot", c3 == s2 or c3 == -s2, "U rotates sigma_3 into +-sigma_2")
    run.check("L2-e-notGamma", sp.simplify(U * s3 * U.H - s3) != Z2, "U does NOT preserve Gamma")


# ---------------------------------------------------------------------- LEG 3
def leg3(run, cfg):
    print("=" * 78)
    print("LEG 3  THE CIRCLE (exact sympy, generic angle, generic profile)")
    print("=" * 78)
    s0, s1, s2, s3 = pauli(cfg)
    Z2, Z21 = sp.zeros(2, 2), sp.zeros(2, 1)
    y, phi, theta = sp.symbols("y phi theta", real=True)
    K, Gamma = s1, s3
    gen = cfg["circle_gen"] if cfg["circle_gen"] is not None else s1

    def Mdir(a):
        return sp.cos(a) * s3 + sp.sin(a) * s2

    def Ucirc(t):
        return sp.cos(t / 2) * s0 - sp.I * sp.sin(t / 2) * gen

    M = Mdir(phi)
    G = sp.cos(phi) * s2 - sp.sin(phi) * s3
    run.check("L3-quarter", sp.simplify(G - Mdir(phi + sp.pi / 2)) == Z2,
              "wall grading G(phi) = M(phi + pi/2), the quarter-turned mass direction")

    chip = sp.Matrix([1, sp.I]) / sp.sqrt(2)
    chim = sp.Matrix([1, -sp.I]) / sp.sqrt(2)
    vplus = sp.simplify(Ucirc(-phi) * chip)
    vminus = sp.simplify(Ucirc(-phi) * chim)
    run.check("L3-G-eigplus", sp.simplify(G * vplus - vplus) == Z21, "G v+ = +v+ at generic phi")
    run.check("L3-G-eigminus", sp.simplify(G * vminus + vminus) == Z21, "G v- = -v- at generic phi")

    mfun, F = sp.Function("m"), sp.Function("F")
    sub = {sp.Derivative(F(y), y): mfun(y)}

    def D(psi):
        return -sp.I * s1 * psi.diff(y) + mfun(y) * M * psi

    run.check("L3-solve-plus", sp.simplify(D(sp.exp(-F(y)) * vplus).subs(sub)) == Z21,
              "exp(-int m) v+ is an exact zero mode at generic phi, generic m(y)")
    run.check("L3-solve-minus", sp.simplify(D(sp.exp(+F(y)) * vminus).subs(sub)) == Z21,
              "exp(+int m) v- is an exact zero mode at generic phi, generic m(y)")
    flag = nonzero_flagger(cfg)
    rwg = sp.simplify(D(sp.exp(-F(y)) * vminus).subs(sub))
    run.check("L3-flag-generic", flag(rwg),
              "PLANTED wrong-chirality candidate at generic phi flagged NONZERO")

    law = charge_law(cfg)
    qG = sp.simplify((vplus.H * s3 * vplus)[0])
    qGm = sp.simplify((vminus.H * s3 * vminus)[0])
    run.check("L3-charge-plus", sp.simplify(qG - law(phi)) == 0,
              f"hosted Gamma-charge(v+) = {law(phi)} exactly")
    run.check("L3-charge-minus", sp.simplify(qGm + law(phi)) == 0,
              "anti-kink Gamma-charge(v-) = +sin(phi) exactly")
    run.check("L3-knull",
              sp.simplify((vplus.H * s1 * vplus)[0]) == 0 and
              sp.simplify((vminus.H * s1 * vminus)[0]) == 0,
              "K-charge of both hosted modes EXACTLY 0 at every angle")
    run.check("L3-cross", sp.simplify(K * vplus - sp.I * vminus) == Z21,
              "K v+ = i v-: K cross-pairs the hosted mode with its mirror partner")
    run.check("L3-KG-anticommute", sp.simplify(K * G + G * K) == Z2,
              "{K, G(phi)} = 0 at every angle (the odd-q cross structure)")

    anti = sp.simplify(M * Gamma + Gamma * M)
    comm = sp.simplify(M * K - K * M)
    run.check("L3-gammaodd-residual", sp.simplify(anti - 2 * sp.cos(phi) * s0) == Z2,
              "{M(phi), Gamma} = 2 cos(phi) I exactly")
    run.check("L3-krein-uniform", sp.simplify(comm.H * comm - 4 * s0) == Z2,
              "[M(phi), K]^H [M(phi), K] = 4 I: the Krein exit is UNIFORM (norm 2)")
    run.check("L3-pythagoras", sp.simplify(qG**2 + sp.cos(phi)**2 - 1) == 0,
              "charge^2 + ({M,Gamma}/2)^2 = 1 exactly")
    vp2 = sp.simplify(vplus.subs(phi, sp.pi / 2))
    run.check("L3-eigenstate-iff",
              sp.simplify(s3 * vp2 + vp2) == Z21 and
              sp.simplify(anti.subs(phi, sp.pi / 2)) == Z2 and
              qG.subs(phi, 0) == 0 and sp.simplify(anti.subs(phi, 0) - 2 * s0) == Z2,
              "poles: phi=pi/2 Gamma-eigenstate + Krein-only; phi=0 charge 0 + Gamma-oddness broken")

    # commutant of sigma_1: kinetic-preserving operators are span{I, sigma_1}
    a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22")
    Ugen = sp.Matrix([[a11, a12], [a21, a22]])
    commut = sp.simplify(Ugen * s1 - s1 * Ugen)
    solc = sp.solve([commut[i, j] for i in range(2) for j in range(2)], [a12, a21, a22], dict=True)
    # semantic, convention-independent: the one solution family lies in span{I, sigma_1}
    ok_comm = False
    if len(solc) == 1:
        Usub = sp.simplify(Ugen.subs(solc[0]))
        ok_comm = sp.simplify(Usub - (Usub[0, 0] * s0 + Usub[0, 1] * s1)) == Z2
    run.check("L3-commutant", ok_comm,
              "commutant of the kinetic direction is span{I, sigma_1} (computed)")

    run.check("L3-U-kinetic", sp.simplify(Ucirc(theta) * s1 * Ucirc(theta).H - s1) == Z2,
              "the circle preserves the kinetic term")
    run.check("L3-U-krein", sp.simplify(Ucirc(theta).H * K * Ucirc(theta) - K) == Z2,
              "the circle is a KREIN ISOMETRY (U^H K U = K exactly)")
    run.check("L3-U-rotM",
              sp.simplify(Ucirc(theta) * M * Ucirc(theta).H - Mdir(phi - theta)) == Z2,
              "U(theta) M(phi) U^H = M(phi - theta)")
    run.check("L3-U-rotG",
              sp.simplify(Ucirc(theta) * Gamma * Ucirc(theta).H - Mdir(-theta)) == Z2,
              "U(theta) Gamma U^H = M(-theta): mass and grading rotate together")
    vpt = sp.simplify(Ucirc(theta) * chip)
    qGt = sp.simplify((vpt.H * s3 * vpt)[0])
    run.check("L3-U-fixed-charge", sp.simplify(qGt - sp.sin(theta)) == 0,
              "fixed-Gamma charge of the transported source-shaped wall's mode = sin(theta)")
    Gam_t = sp.simplify(Ucirc(theta) * Gamma * Ucirc(theta).H)
    run.check("L3-U-invariant", sp.simplify((vpt.H * Gam_t * vpt)[0]) == 0,
              "charge in the TRANSPORTED grading stays 0: the relative angle is invariant")
    Upi = Ucirc(sp.pi)
    run.check("L3-U-flip", sp.simplify(Upi * Gamma * Upi.H + Gamma) == Z2,
              "theta = pi negates Gamma: the circle's Gamma-stabilizer is discrete")

    v1_, v2_, v3_ = sp.symbols("v1 v2 v3")
    okm = all(sp.simplify(D(sp.exp(-F(y)) * vplus * v).subs(sub)) == Z21 for v in (v1_, v2_, v3_))
    run.check("L3-mult", okm,
              "ker(D (x) I_3) = ker(D) (x) C^3 at generic phi: internal-blind, N SUPPLIED")

    kprime = cfg["contrast_kprime"] if cfg["contrast_kprime"] is not None else s3
    a, b, c, d = sp.symbols("a b c d", real=True)
    Mgen = a * s0 + b * s1 + c * s2 + d * s3
    eq1 = sp.simplify(Mgen * s3 + s3 * Mgen)
    eq2 = sp.simplify(Mgen * kprime - kprime * Mgen)
    sol = sp.solve([eq1[i, j] for i in range(2) for j in range(2)] +
                   [eq2[i, j] for i in range(2) for j in range(2)], [a, b, c, d], dict=True)
    run.check("L3-contrast", sol == [{a: 0, b: 0, c: 0, d: 0}],
              "commuting-K' contrast (K' = Gamma, the q-even face): zero-order class is exactly {0}")


# ---------------------------------------------------------------------- LEG 4
def leg4(run, cfg):
    print("=" * 78)
    print("LEG 4  INSTRUMENTS: both repository spectral-flow instruments re-run")
    print("=" * 78)
    r1 = subprocess.run([sys.executable, str(ROOT / DSFS_PATH)],
                        capture_output=True, text=True, cwd=ROOT)
    run.check("L4-dirac-exit0", r1.returncode == 0,
              f"dirac_spectral_flow_section.py exits 0 (got {r1.returncode})")
    run.check("L4-dirac-str", "(EXACTLY 0)" in r1.stdout,
              "net chiral spectral flow printed EXACTLY 0")
    kp = cfg["krein_probe_path"]
    try:
        r2 = subprocess.run([sys.executable, str(ROOT / kp)],
                            capture_output=True, text=True, cwd=ROOT)
        rc2, out2 = r2.returncode, r2.stdout
    except OSError:
        rc2, out2 = 127, ""
    run.check("L4-krein-exit0", rc2 == 0,
              f"krein_spectral_flow_probe.py exits 0 (got {rc2})")
    run.check("L4-krein-flow0", "net chiral spectral flow = +0" in out2,
              "paired K-compatible family: net chiral spectral flow +0")
    run.check("L4-krein-ctrl", "net chiral spectral flow = +1" in out2,
              "one-sided control: +1, and it leaves the modeled Krein class")
    run.check("L4-krein-open", "WC-FUNCTION-SPACE-EXT remains open" in out2,
              "instrument's own ceiling line present")


# ---------------------------------------------------------------------- LEG 5
def scan_for_tokens(files_lines, tokens):
    hits = []
    toks = [t.lower() for t in tokens]
    for path, lines in files_lines.items():
        low = " \n".join(lines).lower()
        if any(t in low for t in toks):
            hits.append(path)
    return hits


def repo_corpus():
    corpus = {}
    for p in ROOT.rglob("*"):
        if p.suffix not in (".md", ".py"):
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith("_local/") or rel in SELF_FILES:
            continue
        try:
            corpus[rel] = p.read_text(errors="replace").splitlines()
        except OSError:
            continue
    return corpus


def leg5(run, cfg, tmp):
    print("=" * 78)
    print("LEG 5  CERTIFIED ABSENCES (planted-positive controls on every absence)")
    print("=" * 78)
    # (a) deviation D1: "now quantified" absent from RW-1
    rw1_lines = {RW1: read_lines(RW1)}
    nq = scan_for_tokens(rw1_lines, ["now quantified"])
    run.check("L5-nq-absent", nq == [],
              "deviation D1: 'now quantified' does not occur in the RW-1 artifact")
    planted_nq = tmp / "planted_nq.md"
    planted_nq.write_text("control\nthe four-way chirality homonym, now quantified\n")
    aug = {str(planted_nq): planted_nq.read_text().splitlines()}
    run.check("L5-nq-plant", scan_for_tokens(aug, ["now quantified"]) == [str(planted_nq)],
              "planted positive for the D1 scan is flagged (detector has power)")
    # (b) novelty tokens repo-wide, self-excluded, wave trees reported-not-failed
    corpus = repo_corpus()
    print(f"  corpus: {len(corpus)} files (md/py outside _local, self-excluded)")
    joiners = scan_for_tokens(corpus, cfg["novelty_tokens"])
    outside = [j for j in joiners if not j.startswith(WAVE_TREES)]
    inside = [j for j in joiners if j.startswith(WAVE_TREES)]
    if inside:
        print(f"  SAME-WAVE (reported, not failed; concurrent sibling arcs): {sorted(inside)}")
    run.check("L5-novelty-outside", outside == [],
              f"novelty tokens: zero hits outside the wave trees (found {sorted(outside)[:5]})")
    planted_nov = tmp / "planted_novelty.md"
    planted_nov.write_text("control\nthe gapping circle parametrization\n")
    aug2 = {str(planted_nov): planted_nov.read_text().splitlines()}
    run.check("L5-novelty-plant",
              scan_for_tokens(aug2, cfg["novelty_tokens"]) == [str(planted_nov)],
              "planted positive for the novelty scan is flagged (detector has power)")
    # (c) destination duplicates
    gdir = sorted((ROOT / "lab/active-research/joe-directed/grading-bridge").glob("*.md"))
    run.check("L5-dest-artifact",
              [p.relative_to(ROOT).as_posix() for p in gdir] == [ARTIFACT],
              "grading-bridge/ holds exactly the GB-1 artifact (no duplicate seed)")
    gprobe = sorted((ROOT / "tests/channel-swings").glob("joe_directed_gb1_*.py"))
    run.check("L5-dest-probe",
              [p.relative_to(ROOT).as_posix() for p in gprobe] == [SELF_PROBE],
              "channel-swings/ holds exactly the GB-1 probe under the gb1 prefix")


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
    run.check("L6-parse", block is not None and rows is not None and len(rows) == 8,
              f"machine table parsed: {0 if rows is None else len(rows)} rows (need 8)")
    if not rows:
        return
    verdicts = {r[0]: r[2] for r in rows}
    run.check("L6-vocab", all(r[2] in VERDICT_SET for r in rows),
              "all verdict tokens drawn from the closed set")
    sha = hashlib.sha256(block.encode()).hexdigest()
    run.check("L6-sha", sha == TABLE_SHA256,
              f"table SHA-256 pinned ({sha[:16]}... vs {TABLE_SHA256[:16]}...)")
    for rid, expect in EXPECTED_VERDICTS.items():
        run.check(f"L6-{rid}", verdicts.get(rid) == expect,
                  f"{rid} verdict consistent with its measurement (got {verdicts.get(rid)})")
    # cross-link: the CIRCLE verdict token must agree with the machine-checked law
    s0, s1, s2, s3 = pauli(cfg)
    phi = sp.Symbol("phi", real=True)
    gen = cfg["circle_gen"] if cfg["circle_gen"] is not None else s1
    Um = sp.cos(-phi / 2) * s0 - sp.I * sp.sin(-phi / 2) * gen
    chip = sp.Matrix([1, sp.I]) / sp.sqrt(2)
    vplus = sp.simplify(Um * chip)
    qG = sp.simplify((vplus.H * s3 * vplus)[0])
    law = charge_law(cfg)
    run.check("L6-circle-lawlink",
              verdicts.get("CIRCLE") == "CHARGE-IS-MINUS-SINE-RELATIVE-ANGLE"
              and sp.simplify(qG - law(phi)) == 0,
              "CIRCLE verdict cross-linked to the symbolic charge law")
    run.check("L6-ceiling-3", "does not derive 3" in text,
              "artifact states on its face that it does not derive 3")
    run.check("L6-ceiling-w6", "NOT absorbed" in text and "UNTYPED" in text,
              "W6 handoff present: UNTYPED, not absorbed")
    run.check("L6-routing", "GU-COMPARATOR-ROUTING" in text
              and "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in text,
              "routing notice and classification present")
    run.check("L6-pending", "canonical_effect: pending_integration" in text,
              "canonical_effect declared pending_integration")
    run.check("L6-sg4open", "SG4 bit 2 stays OPEN" in text,
              "the artifact carries the CC-06 frame: SG4 bit 2 stays OPEN, split never assumed")
    run.check("L6-typedobj", text.count("```gu-typed-objects") == 2,
              "two gu-typed-objects blocks present (typed-carrier gate surface)")
    run.check("L6-target", "target_claim:" in text and "rw1-zero-locus-steers-not-hosts" in text,
              "target_claim frontmatter present and names the RW-1 artifact")


# --------------------------------------------------------------------- driver
def run_live(cfg):
    run = Run()
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        leg1(run, cfg)
        leg2(run, cfg)
        leg3(run, cfg)
        leg4(run, cfg)
        leg5(run, cfg, tmp)
        leg6(run, cfg)
    print("-" * 78)
    print(f"checks: {run.n}  failures: {len(run.failures)} {run.failures}")
    return run


# mutations: every one corrupts MACHINERY or a REFERENCE, never a predicate.
def mutations():
    def m1(cfg):  # pin reference off by one line
        cfg["pins"][1] = (cfg["pins"][1][0], cfg["pins"][1][1] + 1, cfg["pins"][1][2])

    def m2(cfg):  # corrupted Gamma constant
        s0 = sp.eye(2)
        s1 = sp.Matrix([[0, 1], [1, 0]])
        s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
        s3 = sp.Matrix([[1, 0], [0, -2]])
        cfg["pauli"] = (s0, s1, s2, s3)

    def m3(cfg):  # residual flagger stuck at "zero"
        cfg["nonzero_flagger"] = lambda M: False

    def m4(cfg):  # charge-law reference corrupted
        cfg["charge_law"] = lambda ph: -sp.cos(ph)

    def m5(cfg):  # unitary-circle generator corrupted
        cfg["circle_gen"] = sp.Matrix([[0, -sp.I], [sp.I, 0]])

    def m6(cfg):  # novelty-scan detector loses its tokens
        cfg["novelty_tokens"] = []

    def m7(cfg):  # CONTRARY CONTROL: artifact copy claims W3 DISCHARGED
        src = (ROOT / ARTIFACT).read_text()
        mut = src.replace(
            "| W3 | the bill item | ONE-MISSING-ARROW-NOT-DISCHARGED-NOT-OBSTRUCTED |",
            "| W3 | the bill item | DISCHARGED |")
        assert mut != src, "contrary-control substitution failed to apply"
        tmpf = Path(tempfile.mkstemp(suffix=".md")[1])
        tmpf.write_text(mut)
        cfg["artifact_path"] = tmpf

    def m8(cfg):  # instrument runner mispointed
        cfg["krein_probe_path"] = "tests/function-space-ext/DOES_NOT_EXIST_gb1.py"

    def m9(cfg):  # contrast reference corrupted (K' = sigma_2, not Gamma)
        cfg["contrast_kprime"] = sp.Matrix([[0, -sp.I], [sp.I, 0]])

    return [
        ("M1 pin reference off by one", m1, {"L1-02"}),
        ("M2 corrupted Gamma constant", m2,
         {"L2-a-s3", "L2-d-charge0", "L2-d-charge1", "L3-quarter", "L3-charge-plus"}),
        ("M3 residual flagger stuck at zero", m3, {"L2-b-flag", "L3-flag-generic"}),
        ("M4 charge-law reference corrupted", m4,
         {"L3-charge-plus", "L3-charge-minus", "L6-circle-lawlink"}),
        ("M5 unitary generator corrupted", m5,
         {"L3-G-eigplus", "L3-U-kinetic", "L3-U-krein", "L3-U-rotM", "L3-U-fixed-charge"}),
        ("M6 novelty-scan tokens lost", m6, {"L5-novelty-plant"}),
        ("M7 CONTRARY CONTROL: W3 DISCHARGED", m7, {"L6-W3", "L6-sha"}),
        ("M8 instrument runner mispointed", m8,
         {"L4-krein-exit0", "L4-krein-flow0", "L4-krein-ctrl", "L4-krein-open"}),
        ("M9 contrast form corrupted", m9, {"L3-contrast"}),
    ]


def selftest():
    print("#" * 78)
    print("# SELFTEST: clean baseline FIRST, then 9 machinery/reference mutations")
    print("#" * 78)
    base = run_live(default_cfg())
    if base.failures or base.n != BASELINE_COUNT:
        print(f"RED BASELINE: {len(base.failures)} failures, {base.n} checks "
              f"(pinned {BASELINE_COUNT}) -- aborting; no mutation result is meaningful.")
        return 1
    print(f"# baseline GREEN: {base.n}/{BASELINE_COUNT} checks, 0 failures\n")
    all_ok = True
    for name, mut, targets in mutations():
        print("#" * 78)
        print(f"# MUTATION {name}  (targets: {sorted(targets)})")
        print("#" * 78)
        cfg = default_cfg()
        try:
            mut(cfg)
            r = run_live(cfg)
            caught = set(r.failures) & targets
            if not r.failures:
                print(f"# NOT CAUGHT: {name} produced a fully green run")
                all_ok = False
            elif not caught:
                print(f"# INCIDENTAL-NOT-TARGETED: {name} failed only {sorted(set(r.failures))}")
                all_ok = False
            else:
                print(f"# CAUGHT by targeted check(s) {sorted(caught)}; "
                      f"all failures: {sorted(set(r.failures))}")
        except Exception as exc:  # noqa: BLE001
            print(f"# CRASH-NOT-DETECTION: {name} crashed ({type(exc).__name__}: {exc})")
            all_ok = False
        finally:
            ap = cfg.get("artifact_path")
            if ap is not None:
                Path(ap).unlink(missing_ok=True)
    print("#" * 78)
    base2 = run_live(default_cfg())
    if base2.failures or base2.n != BASELINE_COUNT:
        print("# BASELINE NOT RESTORED after mutations -- selftest FAILS")
        return 1
    print(f"# baseline re-verified after mutations: {base2.n}/{BASELINE_COUNT}, 0 failures")
    if not all_ok:
        print("# SELFTEST FAILED: at least one mutation was not properly caught")
        return 1
    print("# SELFTEST PASSED: baseline green before and after; 9/9 mutations caught "
          "by their targeted checks via genuine [FAIL] lines")
    return 0


def main():
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    r = run_live(default_cfg())
    if r.failures:
        print("VERDICT: RED")
        sys.exit(1)
    print(f"VERDICT: GREEN ({r.n} checks)")
    sys.exit(0)


if __name__ == "__main__":
    main()
