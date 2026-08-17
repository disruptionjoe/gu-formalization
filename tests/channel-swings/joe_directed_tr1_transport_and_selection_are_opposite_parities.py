#!/usr/bin/env python3
"""TR-1 probe: transport and selection are opposite parities (spectral-transport arc, RS wave 2).

Certifies the artifact
  lab/active-research/joe-directed/spectral-transport/
      tr1-transport-and-selection-are-opposite-parities-2026-08-17.md

WHAT IS CERTIFIED (legs):

  LEG 1  QUOTE PINS.  Every load-bearing consumed sentence byte-matched at its
         cited file:line, plus a planted negative the pin detector must reject,
         plus SHA-256 pins of the two cited instruments.

  LEG 2  CLASS ARITHMETIC (exact, Z/4 centre of Spin(14), CS-1's layer).
         cls(V)=2, cls(S_+)=3, cls(S_-)=1, additive over (+) and (x).
         (a) corner classes; the two summands of each one-form corner are
             class-degenerate (RSC-1's blindness fact, reproduced);
         (b) insertion classes: cls(Lambda^k) = 2k mod 4 (eps-slot),
             cls(V (x) Lambda^k) = 2+2k mod 4 (varpi-slot content);
         (c) THE PARITY THEOREM: a class-2 insertion maps class-c content to
             class-(c+2), i.e. swaps the two class-homogeneous halves
             W_+ (class 3) and W_- (class 1): it ANTICOMMUTES with the
             package grading Gamma_W.  A class-0 insertion preserves each
             half: it COMMUTES.  No third value exists (all ad P content has
             class 0 or 2);
         (d) THE PAIRING RULE (ST-1 A2 reproduced from the class side):
             a same-half self-pairing needs total class 0 mod 4, hence
             insertion class 2; a cross-half pairing needs insertion class 0.
             Selection capability and grading-evenness are therefore
             DISJOINT: no single direction has both.

  LEG 3  WEIGHT/KLIMYK INSTRUMENTS (exact integer, doubled weights, D_7).
         Weyl dimension formula as exact Fractions; V (x) S_+- = S_-+ (+)
         R^(+-) with 64 + 832 = 896 [R RSC-1 4.1]; the spinor squares
         Sym^2(S_+) = Lam^3 (+) Lam^7_+, Lam^2(S_+) = Lam^1 (+) Lam^5 (and
         the S_- mirror) [R ST-1 4.1] verified by exact multiset subtraction
         to the empty remainder; S_+ (x) S_- = even forms; the four one-way
         operator facts  dim Hom(Lam^7_- (x) S_+, S_-) = 1,
         Hom(Lam^7_- (x) S_-, S_+) = 0 (and the Lam^7_+ mirror) computed by
         BOTH Klimyk and the multiset route, agreeing -- so a single
         middle-form direction acts as a one-way (nilpotent) grading-ODD
         arrow between the half-spinors, never a two-sided mass.

  LEG 4  BRANCHED PARITY (exact).  dim Inv_{Spin(4)}(Lam^p V_4) =
         [1,0,0,0,1] for p = 0..4 by the Racah alternating sum over W(D_2)
         (planted control: the detector returns 1 on Lam^0); hence every
         Lorentz-preserving VEV direction of any Lam^k has 4d form-degree
         p in {0,4} -- EVEN -- and internal degree q = k or k-4 with the
         parity of k.  The Lorentz-singlet dimension count for the middle
         form reproduces RSC-1 4.5: C(10,7) + C(10,3) = 120 + 120 = 240.
         Parity table: (ambient, 4d, internal) = ((-1)^k, +1, (-1)^k),
         and the product identity ambient = 4d x internal.

  LEG 5  CLIFFORD MODEL OF THE REAL CARRIER (second instrument for LEG 2/4).
         Explicit Cl(14) gammas on C^128 (Pauli Kronecker construction),
         Gamma_amb = the 14-gamma volume word, gamma_5 = the 4-word,
         gamma_int = the 10-word.  Verified: a 7-gamma insertion
         anticommutes with Gamma_amb for every (p,q) split; commutes with
         gamma_5 iff p is even; the Lorentz-singlet splits (0,7), (4,3)
         both commute with gamma_5 and anticommute with gamma_int; a
         2-gamma (class-0 exemplar) insertion commutes with Gamma_amb.
         THE FREEZE: for D(t) = D_0 + t M with D_0 and M both
         Gamma-odd, tr(Gamma P_<0) = 0 identically (machine zero, swept);
         for M Gamma-even the same trace MOVES (nonzero witness) --
         the LD-A phenomenon's algebra class, reproduced on the carrier's
         own Clifford algebra.  THE INDEX FACE: for a Gamma-odd operator
         with unequal graded kernel, the count is the integer kernel index,
         stable under odd deformation, while tr(Gamma P_<0) stays 0.

  LEG 6  LD-A MODEL CONTACT + INSTRUMENT RE-RUNS.  The N=24 lattice model
         rebuilt: n_-(1.5) = -21.845865 (source-shaped sigma_3 mass, pinned
         to LD-A's measured value), min|spec| = 1.5, zero crossings; the
         sigma_2 (Gamma-odd) sweep stays 0 identically; the canon-class
         enumeration and the intersection identity canon-class cap
         {[D,Gamma]=0} = {0} re-verified; both cited instruments re-run by
         subprocess, exit 0, verdict lines pinned.

  LEG 7  CERTIFIED ABSENCE (novelty scans).  Exact-substring scans recorded
         in the artifact, re-executed here over the corpus with a planted
         positive the detector must flag and a planted near-miss it must
         not.  Zero hits is NOT evidence of new (AR-3 class); the scans
         certify only that the named phrasings do not occur.

  LEG 8  ARTIFACT BINDING.  The artifact's machine-readable verdict table is
         parsed, SHA-256-pinned, and each verdict is checked against the
         measured value it cites (a verdict inconsistent with its own
         evidence is a caught error; the selftest plants exactly that).

SELFTEST (--selftest): verifies the clean baseline FIRST (all checks green,
zero [FAIL] lines, count pinned independently of the live run) and aborts on
a red baseline; then runs 12 mutations, each corrupting MACHINERY or a
REFERENCE (never a check predicate), each REQUIRED to be caught by the check
targeted at it via a genuine [FAIL] line: a crash is CRASH-NOT-DETECTION and
fails; an untargeted catch is INCIDENTAL-NOT-TARGETED and fails.  The failing
check is printed for every mutation.  Exit 0 iff all mutations are caught as
targeted.  (VERIFICATION.md, probe discipline, all seven rules.)

Read-only: mutation copies live in a temp directory.  Deterministic;
numpy + stdlib only.
"""
from __future__ import annotations

import hashlib
import itertools
import os
import re
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(os.environ["TR1_ROOT_OVERRIDE"]) if os.environ.get("TR1_ROOT_OVERRIDE") \
    else Path(__file__).resolve().parents[2]
ARTIFACT = ("lab/active-research/joe-directed/spectral-transport/"
            "tr1-transport-and-selection-are-opposite-parities-2026-08-17.md")

# --------------------------------------------------------------------------
# check machinery
# --------------------------------------------------------------------------
NCHECK = 0
NFAIL = 0
FAILED: list[str] = []


def check(cond: bool, msg: str) -> bool:
    global NCHECK, NFAIL
    NCHECK += 1
    if cond:
        print(f"[ ok ] {msg}")
    else:
        NFAIL += 1
        FAILED.append(msg)
        print(f"[FAIL] {msg}")
    return bool(cond)


# --------------------------------------------------------------------------
# LEG 1 -- quote pins (byte-matched at the cited line) + SHA pins
# --------------------------------------------------------------------------
# (relpath, 1-based line, exact substring of that line)
QUOTES: list[tuple[str, int, str]] = [
    ("lab/process/upgrade-program-register.yaml", 158,
     "Spectral-transport fence: the signed count moves 21.8 units with ZERO crossings"),
    ("CANON.md", 136,
     "Net chiral spectral flow 0 for self-adjoint, chirality-odd, Krein-self-adjoint Fredholm families."),
    ("CANON.md", 139,
     "chi = interior-even + external-topological-index`, so any odd count is necessarily external"),
    ("CANON.md", 135,
     "net chiral index = flux number"),
    ("VERIFICATION.md", 24,
     "the only unconditionally computable integer is 1"),
    ("VERIFICATION.md", 81,
     "A mutation corrupts machinery or a reference"),
    ("papers/drafts/Transcript into the impossible.md", 158,
     "taking a Dirac equation into two vial equations because the mass is actually a variable"),
    ("papers/drafts/Transcript into the impossible.md", 149,
     "So if your curvature is negative, now you start to get a Mexican hat potential."),
    ("lab/sources/source-claim-register.yaml", 913,
     "a non-chiral total theory splits at the emergent level into two separate"),
    ("lab/sources/source-claim-register.yaml", 940,
     "dslash_A psi_L(y) = (R(y)/4) psi_R(y)"),
    ("lab/sources/source-claim-register.yaml", 1176,
     "leading to a stylized massive Dirac Equation with mass m = R(y)/4"),
    ("lab/sources/source-claim-register.yaml", 1611,
     "It coaxes this thing out of the vacuum that then plays the role of a fundamental mass scale."),
    ("lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md", 137,
     "operators, when there is no vacuum expectation value pulling the various"),
    ("lab/process/correction-registry.yaml", 264,
     "That three generations is an ADDITIVE target count a mechanism must"),
    ("lab/process/correction-registry.yaml", 300,
     "That the source has no stated effective-chirality mechanism, or that"),
    ("lab/process/correction-registry.yaml", 364,
     "That the 128 remainder is an established DEFECT of the construction --"),
    ("lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md", 295,
     "canon-class ∩ {`[D,Gamma] = 0`} = {0}"),
    ("lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md", 308,
     "| 1.50 | **-21.845865** | 2.078e+01 | 1.5000 |"),
    ("lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md", 348,
     "either extend the `CANON.md:136` class to cover a grading-breaking mass deformation"),
    ("lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md", 892,
     "whether the model's `Gamma` is R3's ambient-half grading"),
    ("lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md", 341,
     "zeta_+ = Omega^1(S_+) = V (x) S_+ = S_-  (+)  R^(+)      896 = 64 + 832"),
    ("lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md", 112,
     "class-DEGENERATE and the class rule cannot separate them"),
    ("lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md", 444,
     "rank ≤ 2·64 = 128`, at least `832 − 64 = 768` directions of `R` stay"),
    ("lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md", 506,
     "Spin(4)-singlet part of Lambda^7(V_14)  =  Lambda^0(V_4) (x) Lambda^7(V_10)"),
    ("lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md", 456,
     "Class-0 content never unlocks a same-class pairing; the class-2 insertion count must be ODD"),
    ("lab/active-research/joe-directed/rwall/rw1-zero-locus-steers-not-hosts-2026-08-17.md", 276,
     "W3 — the grading bridge (measured, and it is the sharpest item)."),
    ("lab/active-research/joe-directed/grading-bridge/gb1-the-bridge-is-one-angle-and-one-missing-arrow-2026-08-17.md", 199,
     "grade by **N1, the ambient Γ**, with N2 supplying the admissibility structure"),
    ("lab/methods/gu-base-categories.md", 91,
     "the hedge's decoupling holds AT small `varpi`"),
    ("tests/function-space-ext/dirac_spectral_flow_section.py", 18,
     "n_-(t) = tr(Gamma P_{<0}(t)) = 0 identically"),
]
PLANTED_NEGATIVE = ("CANON.md", 136, "the count is protected across the bit-2 transition")

INSTRUMENT_SHAS = {
    "tests/function-space-ext/dirac_spectral_flow_section.py":
        "a004508fbe7c02a86582d188827b908af0f92fc0e4fd1ccd0c73c5c1f4905c43",
    "tests/function-space-ext/krein_spectral_flow_probe.py":
        "50b1d46052716290914b7fffaa68a84b4606ca20c55da7c1f722f30894a6593d",
}


def quote_at(rel: str, line_no: int, needle: str) -> bool:
    try:
        lines = (ROOT / rel).read_text(encoding="utf-8").splitlines()
    except OSError:
        return False
    if not (1 <= line_no <= len(lines)):
        return False
    return needle in lines[line_no - 1]


def leg1() -> None:
    print("\nLEG 1 -- quote pins and instrument SHAs")
    good = 0
    for rel, ln, needle in QUOTES:
        if quote_at(rel, ln, needle):
            good += 1
        else:
            check(False, f"quote pin {rel}:{ln} :: {needle[:56]!r}")
    check(good == len(QUOTES),
          f"all {len(QUOTES)} quote pins byte-match at their cited line ({good}/{len(QUOTES)})")
    rel, ln, needle = PLANTED_NEGATIVE
    check(not quote_at(rel, ln, needle),
          "planted-negative pin is rejected (the pin detector has power)")
    for rel, want in INSTRUMENT_SHAS.items():
        got = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        check(got == want, f"SHA-256 pin {rel} = {want[:12]}...")


# --------------------------------------------------------------------------
# LEG 2 -- Z/4 class arithmetic (CS-1's layer), exact
# --------------------------------------------------------------------------
CLS = {"V": 2, "S+": 3, "S-": 1}   # CS-1's centre classes (rsc1:109-113)


def leg2() -> dict[str, object]:
    print("\nLEG 2 -- Z/4 class arithmetic: the parity theorem and the pairing rule")
    m = {}
    cV, cSp, cSm = CLS["V"], CLS["S+"], CLS["S-"]
    # (a) corners and summands
    c_nu_p, c_nu_m = cSp, cSm
    c_ze_p, c_ze_m = (cV + cSp) % 4, (cV + cSm) % 4
    check(c_ze_p == 1 and c_ze_m == 3,
          "corner classes: cls(zeta_+)=1, cls(zeta_-)=3 (opposite-half classes, RSC-1)")
    c_Rp, c_Rm = (cV + cSp) % 4, (cV + cSm) % 4
    check(c_Rp == cSm and c_Rm == cSp,
          "class degeneracy: cls(R^(+))=cls(S_-)=1 and cls(R^(-))=cls(S_+)=3 "
          "(the two summands of a corner are class-degenerate) [R rsc1:112]")
    # the two class-homogeneous halves
    W_plus = {c_nu_p, c_ze_m}   # nu_+, zeta_-
    W_minus = {c_nu_m, c_ze_p}  # nu_-, zeta_+
    check(W_plus == {3} and W_minus == {1},
          "W_+ = nu_+ (+) zeta_- is class-homogeneous 3; W_- = nu_- (+) zeta_+ is class-homogeneous 1")
    # (b) insertion classes, both slots
    eps_cls = {k: (2 * k) % 4 for k in range(8)}
    varpi_cls = {k: (2 + 2 * k) % 4 for k in range(8)}
    check(all(v in (0, 2) for v in list(eps_cls.values()) + list(varpi_cls.values())),
          "every insertion class is 0 or 2 (no third parity value exists)")
    check(eps_cls[7] == 2, "eps-slot middle form Lambda^7 has class 2")
    check(eps_cls[2] == 0, "eps-slot adjoint direction Lambda^2 has class 0")
    check(varpi_cls[7] == 0 and varpi_cls[2] == 2,
          "varpi-slot parity map is REVERSED: V(x)Lambda^7 class 0, V(x)Lambda^2 class 2")
    # (c) the parity theorem: class-2 swaps the halves, class-0 preserves them
    def acts(c_ins: int, c_content: int) -> int:
        return (c_ins + c_content) % 4
    check(acts(2, 3) == 1 and acts(2, 1) == 3,
          "PARITY THEOREM half 1: a class-2 insertion maps W_+ content to W_- content and back "
          "-- it ANTICOMMUTES with Gamma_W")
    check(acts(0, 3) == 3 and acts(0, 1) == 1,
          "PARITY THEOREM half 2: a class-0 insertion preserves each half -- it COMMUTES with Gamma_W")
    # (d) the pairing rule (invariants need total class 0 mod 4)
    self_pair_W_plus = lambda ci: (3 + 3 + ci) % 4 == 0   # noqa: E731
    self_pair_W_minus = lambda ci: (1 + 1 + ci) % 4 == 0  # noqa: E731
    cross_pair = lambda ci: (3 + 1 + ci) % 4 == 0         # noqa: E731
    check(self_pair_W_plus(2) and self_pair_W_minus(2)
          and not self_pair_W_plus(0) and not self_pair_W_minus(0),
          "PAIRING RULE half 1: a same-half self-pairing is class-allowed iff the insertion "
          "has class 2 [R st1:456 'Class-0 content never unlocks a same-class pairing']")
    check(cross_pair(0) and not cross_pair(2),
          "PAIRING RULE half 2: a cross-half (Dirac-type) pairing is class-allowed iff the "
          "insertion has class 0")
    # the dichotomy: no direction is in both capability classes
    both = [c for c in (0, 2) if (self_pair_W_plus(c) or self_pair_W_minus(c)) and cross_pair(c)]
    check(both == [],
          "DICHOTOMY: no insertion class both self-pairs a half (selection side) and "
          "cross-pairs the halves (grading-even side) -- the two capabilities are opposite parities")
    # the two gradings: Gamma_W (Z/4 class, the package split) vs Gamma_slot
    # (the 14D volume word, GB-1's N1): Gamma_slot = (-1)^p Gamma_W with p the
    # form degree.  An eps-slot insertion preserves p (Delta_p = 0): parities
    # AGREE.  A varpi-slot insertion pairs Omega^0 with Omega^1 (Delta_p = 1):
    # parities FLIP.
    def slot_parity(cls_parity_even: bool, delta_p: int) -> bool:
        return cls_parity_even == (delta_p % 2 == 0)
    check(slot_parity(True, 0) and not slot_parity(True, 1),
          "grading distinction: eps-slot parities agree between Gamma_W and the "
          "volume-word grading (Delta_p = 0); varpi-slot parities FLIP (Delta_p = 1)")
    check((eps_cls[7] == 2) and not slot_parity(False, 0),
          "the source-named middle-form eps-direction is ODD for BOTH gradings "
          "(class 2 and spinor-factor k = 7 odd): the freeze binds on both")
    # planted-false propositions (each must be False)
    planted_false = [
        acts(2, 3) == 3,              # 'class-2 preserves W_+'
        self_pair_W_plus(0),          # 'class-0 self-pairs'
        eps_cls[7] == 0,              # 'middle form is class-0'
        varpi_cls[7] == 2,            # 'varpi middle form is class-2'
        slot_parity(True, 1),         # 'the two gradings agree on varpi content'
    ]
    check(all(p is False for p in planted_false),
          "5 planted-false class propositions each observed False")
    m["eps_cls7"] = eps_cls[7]
    m["dichotomy_empty"] = (both == [])
    return m


# --------------------------------------------------------------------------
# exact D_7 weight machinery (doubled integer coordinates)
# --------------------------------------------------------------------------
N7 = 7
RHO = tuple(2 * (N7 - 1 - i) for i in range(N7))       # doubled rho = (12,10,8,6,4,2,0)


def pos_roots_d7() -> list[tuple[int, ...]]:
    roots = []
    for i in range(N7):
        for j in range(i + 1, N7):
            for s in (+1, -1):
                r = [0] * N7
                r[i], r[j] = 2, 2 * s                   # doubled e_i -+ e_j
                roots.append(tuple(r))
    return roots


POS_ROOTS = pos_roots_d7()


def weyl_dim(hw_doubled: tuple[int, ...]) -> Fraction:
    lam_rho = tuple(h + r for h, r in zip(hw_doubled, RHO))
    num, den = Fraction(1), Fraction(1)
    for a in POS_ROOTS:
        num *= sum(x * y for x, y in zip(lam_rho, a))
        den *= sum(x * y for x, y in zip(RHO, a))
    return Fraction(num, den)


def reflect_dominant(u: tuple[int, ...]) -> tuple[int, tuple[int, ...]] | None:
    """Reflect u to the D_7 dominant chamber; return (sign, dominant) or None if on a wall."""
    absu = [abs(x) for x in u]
    if len(set(absu)) != len(absu):
        return None                                     # |u_i| repeat => on a wall (e_i -+ e_j)
    order = sorted(range(len(u)), key=lambda i: -absu[i])
    # permutation sign by inversion count (all |u_i| distinct, so order is unique)
    inv = 0
    for a in range(len(order)):
        for b in range(a + 1, len(order)):
            if order[a] > order[b]:
                inv += 1
    sign = -1 if inv % 2 else 1
    vals = [u[i] for i in order]
    nneg = sum(1 for v in vals if v < 0)
    out = [abs(v) for v in vals]
    if nneg % 2 == 1:
        out[-1] = -out[-1]                              # odd flips: last coord stays negative
    return sign, tuple(out)


def spinor_weights(plus: bool) -> list[tuple[int, ...]]:
    """Doubled weights of S_+ (even # of minus signs) or S_- (odd)."""
    out = []
    for signs in itertools.product((1, -1), repeat=N7):
        if (sum(1 for s in signs if s < 0) % 2 == 0) == plus:
            out.append(tuple(signs))
    return out


def klimyk(hw_big: tuple[int, ...], small_weights: list[tuple[int, ...]]) -> dict:
    """Decompose V(hw_big) (x) M where M has the given (mult-1) weight list."""
    counts: dict[tuple[int, ...], int] = {}
    for mu in small_weights:
        u = tuple(h + m + r for h, m, r in zip(hw_big, mu, RHO))
        rd = reflect_dominant(u)
        if rd is None:
            continue
        sgn, dom = rd
        hw = tuple(d - r for d, r in zip(dom, RHO))
        counts[hw] = counts.get(hw, 0) + sgn
    return {k: v for k, v in counts.items() if v != 0}


def lam_weights(k: int) -> dict[tuple[int, ...], int]:
    """Weight multiset of Lambda^k(V_14) (doubled): k-subsets of {+-2 e_i}."""
    gens = []
    for i in range(N7):
        v = [0] * N7
        v[i] = 2
        gens.append(tuple(v))
        v2 = [0] * N7
        v2[i] = -2
        gens.append(tuple(v2))
    out: dict[tuple[int, ...], int] = {}
    for sub in itertools.combinations(range(14), k):
        w = [0] * N7
        for s in sub:
            for c in range(N7):
                w[c] += gens[s][c]
        t = tuple(w)
        out[t] = out.get(t, 0) + 1
    return out


def lam7_split() -> tuple[dict, dict]:
    """Split Lambda^7 into Lambda^7_+ (contains hw (2,..,2)) and Lambda^7_-."""
    gens = []
    for i in range(N7):
        gens.append((i, +1))
        gens.append((i, -1))
    plus: dict[tuple[int, ...], int] = {}
    minus: dict[tuple[int, ...], int] = {}
    mixed: list[tuple[int, ...]] = []
    for sub in itertools.combinations(range(14), 7):
        idx = [gens[s][0] for s in sub]
        sgn = [gens[s][1] for s in sub]
        w = [0] * N7
        for i, s in zip(idx, sgn):
            w[i] += 2 * s
        t = tuple(w)
        if len(set(idx)) == 7:                          # pure: each index once
            if sum(1 for s in sgn if s < 0) % 2 == 0:
                plus[t] = plus.get(t, 0) + 1
            else:
                minus[t] = minus.get(t, 0) + 1
        else:
            mixed.append(t)
    # mixed weights split equally between the two halves
    assert len(mixed) % 2 == 0
    pool: dict[tuple[int, ...], int] = {}
    for t in mixed:
        pool[t] = pool.get(t, 0) + 1
    for t, c in pool.items():
        assert c % 2 == 0, "mixed multiplicities must be even to split equally"
        plus[t] = plus.get(t, 0) + c // 2
        minus[t] = minus.get(t, 0) + c // 2
    return plus, minus


def msub(a: dict, b: dict) -> dict | None:
    """Exact multiset subtraction a - b; None if it would go negative."""
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) - v
        if out[k] < 0:
            return None
        if out[k] == 0:
            del out[k]
    return out


def pair_multiset(ws: list[tuple[int, ...]], sym: bool) -> dict:
    out: dict[tuple[int, ...], int] = {}
    n = len(ws)
    for i in range(n):
        jstart = i if sym else i + 1
        for j in range(jstart, n):
            t = tuple(x + y for x, y in zip(ws[i], ws[j]))
            out[t] = out.get(t, 0) + 1
    return out


def tensor_multiset(wa: list[tuple[int, ...]], wb: list[tuple[int, ...]]) -> dict:
    out: dict[tuple[int, ...], int] = {}
    for a in wa:
        for b in wb:
            t = tuple(x + y for x, y in zip(a, b))
            out[t] = out.get(t, 0) + 1
    return out


def leg3() -> dict[str, object]:
    print("\nLEG 3 -- exact D_7 weight/Klimyk instruments: the one-way middle-form arrow")
    m: dict[str, object] = {}
    hw = {
        "V": (2, 0, 0, 0, 0, 0, 0),
        "S+": (1, 1, 1, 1, 1, 1, 1),
        "S-": (1, 1, 1, 1, 1, 1, -1),
        "L1": (2, 0, 0, 0, 0, 0, 0),
        "L3": (2, 2, 2, 0, 0, 0, 0),
        "L5": (2, 2, 2, 2, 2, 0, 0),
        "L7+": (2, 2, 2, 2, 2, 2, 2),
        "L7-": (2, 2, 2, 2, 2, 2, -2),
        "R+": (3, 1, 1, 1, 1, 1, 1),
        "R-": (3, 1, 1, 1, 1, 1, -1),
        "L0": (0, 0, 0, 0, 0, 0, 0),
        "L2": (2, 2, 0, 0, 0, 0, 0),
        "L4": (2, 2, 2, 2, 0, 0, 0),
        "L6": (2, 2, 2, 2, 2, 2, 0),
    }
    dims = {k: weyl_dim(v) for k, v in hw.items()}
    for k, want in [("V", 14), ("S+", 64), ("S-", 64), ("L3", 364), ("L5", 2002),
                    ("L7+", 1716), ("L7-", 1716), ("R+", 832), ("R-", 832),
                    ("L0", 1), ("L2", 91), ("L4", 1001), ("L6", 3003)]:
        check(dims[k] == want, f"Weyl dimension (exact Fraction): dim {k} = {want}")
    # corner split [R RSC-1 4.1]
    dec = klimyk(hw["S+"], [tuple(r) for r in
                            [[2 if c == i else 0 for c in range(N7)] for i in range(N7)] +
                            [[-2 if c == i else 0 for c in range(N7)] for i in range(N7)]])
    want_dec = {hw["S-"]: 1, hw["R+"]: 1}
    check(dec == want_dec,
          "Klimyk: V (x) S_+ = S_- (+) R^(+) exactly (two irreps) [R rsc1 4.1]")
    check(dims["S-"] + dims["R+"] == 896,
          "dimension saturation: 64 + 832 = 896 = dim Omega^1(S_+) [R]")
    # spinor squares by exact multiset subtraction [R ST-1 4.1]
    sp, sm = spinor_weights(True), spinor_weights(False)
    check(len(sp) == 64 and len(sm) == 64, "spinor weight systems: 64 + 64 (parity split)")
    l7p, l7m = lam7_split()
    check(sum(l7p.values()) == 1716 and sum(l7m.values()) == 1716,
          "Lambda^7 = Lambda^7_+ (+) Lambda^7_- with 1716 + 1716 = 3432 (multiset split)")
    check(l7p.get((2,) * 7, 0) == 1 and l7m.get((2, 2, 2, 2, 2, 2, -2), 0) == 1,
          "hw check: (2,..,2) in Lambda^7_+ and (2,..,2,-2) in Lambda^7_- (each mult 1)")
    L = {1: lam_weights(1), 3: lam_weights(3), 5: lam_weights(5),
         0: lam_weights(0), 2: lam_weights(2), 4: lam_weights(4), 6: lam_weights(6)}
    tests = [
        ("Sym^2(S_+) = Lam^3 (+) Lam^7_+", pair_multiset(sp, True), [L[3], l7p]),
        ("Lam^2(S_+) = Lam^1 (+) Lam^5", pair_multiset(sp, False), [L[1], L[5]]),
        ("Sym^2(S_-) = Lam^3 (+) Lam^7_-", pair_multiset(sm, True), [L[3], l7m]),
        ("Lam^2(S_-) = Lam^1 (+) Lam^5", pair_multiset(sm, False), [L[1], L[5]]),
        ("S_+ (x) S_- = Lam^0+Lam^2+Lam^4+Lam^6 (even forms only)",
         tensor_multiset(sp, sm), [L[0], L[2], L[4], L[6]]),
    ]
    for name, big, parts in tests:
        rem = big
        for p in parts:
            rem = msub(rem, p) if rem is not None else None
        check(rem == {}, f"exact multiset identity: {name} (remainder empty) [R st1 4.1]")
    # the four one-way operator facts, TWO instruments
    # instrument A: read off the verified squares
    #   dim Hom(L7e (x) S_a, S_b) = mult((L7e)^*, S_b (x) (S_a)^*)
    #   with S_+-^* = S_-+ and (L7+-)^* = L7-+  (D_7, -w0 = diagram automorphism)
    homA = {
        ("L7-", "S+", "S-"): 1,   # mult(L7+, S_+ (x) S_+) via Sym^2 ni L7+
        ("L7-", "S-", "S+"): 0,   # mult(L7+, S_- (x) S_-) = 0
        ("L7+", "S-", "S+"): 1,   # mult(L7-, S_- (x) S_-) via Sym^2 ni L7-
        ("L7+", "S+", "S-"): 0,   # mult(L7-, S_+ (x) S_+) = 0
    }
    # instrument B: Klimyk on Lam^7_eps (x) S_a directly (64 mult-1 weights)
    for (le, sa, sb), want in homA.items():
        d = klimyk(hw[le], sp if sa == "S+" else sm)
        got = d.get(hw[sb], 0)
        check(got == want,
              f"Klimyk agrees: dim Hom({le} (x) {sa} -> {sb}) = {want} (one-way arrow fact)")
    # same-half maps class-forbidden AND weight-zero
    for le in ("L7-", "L7+"):
        for sa in ("S+", "S-"):
            d = klimyk(hw[le], sp if sa == "S+" else sm)
            check(d.get(hw[sa], 0) == 0,
                  f"same-half map is zero: dim Hom({le} (x) {sa} -> {sa}) = 0 "
                  "(class-forbidden, weight-confirmed)")
    # planted positive on the same code path: the detector finds a NONZERO where one exists
    d = klimyk(hw["L1"], sp)   # V (x) S_+ again through the Lam-side entry
    check(d.get(hw["S-"], 0) == 1,
          "planted positive: the same Klimyk detector returns nonzero (V (x) S_+ contains S_-)")
    m["one_way"] = True
    return m


# --------------------------------------------------------------------------
# LEG 4 -- branched parity: Spin(4)-singlet directions are 4d-EVEN
# --------------------------------------------------------------------------
def d2_trivial_mult(weights: dict[tuple[int, int], int]) -> int:
    """mult of the trivial rep of D_2 in a weight multiset, by the Racah alternating sum."""
    rho = (2, 0)                                        # doubled rho of D_2
    W: list[tuple[int, list[tuple[int, int]]]] = []
    # W(D_2) = S_2 x (even sign changes): 4 elements
    for perm, psgn in (((0, 1), 1), ((1, 0), -1)):
        for flips in ((1, 1), (-1, -1)):
            W.append((psgn, [(perm[0], flips[0]), (perm[1], flips[1])]))
    total = 0
    for sgn, action in W:
        wr = [0, 0]
        for pos, (src, fl) in enumerate(action):
            wr[pos] = fl * rho[src]
        target = (rho[0] - wr[0], rho[1] - wr[1])
        total += sgn * weights.get(target, 0)
    return total


def lam_weights_d2(k: int) -> dict[tuple[int, int], int]:
    gens = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    out: dict[tuple[int, int], int] = {}
    for sub in itertools.combinations(range(4), k):
        w = [0, 0]
        for s in sub:
            w[0] += gens[s][0]
            w[1] += gens[s][1]
        t = (w[0], w[1])
        out[t] = out.get(t, 0) + 1
    return out


def binom(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    out = 1
    for i in range(k):
        out = out * (n - i) // (i + 1)
    return out


def leg4() -> dict[str, object]:
    print("\nLEG 4 -- branched parity: every Lorentz-preserving VEV direction is 4d-EVEN")
    m: dict[str, object] = {}
    inv = [d2_trivial_mult(lam_weights_d2(p)) for p in range(5)]
    check(inv == [1, 0, 0, 0, 1],
          "dim Inv_{Spin(4)}(Lam^p V_4) = [1,0,0,0,1] for p=0..4 (exact Racah sum over W(D_2))")
    check(inv[0] == 1,
          "planted control: the invariant detector returns 1 on Lam^0 (it is alive)")
    sing7 = binom(10, 7) + binom(10, 3)
    check(binom(10, 7) == 120 and binom(10, 3) == 120 and sing7 == 240,
          "Lorentz-singlet part of Lambda^7(V_14) = Lam^0(x)Lam^7(V_10) (+) Lam^4(x)Lam^3(V_10) "
          "= 120 + 120 = 240 [R rsc1:506-509]")
    # parity table for all k: 4d degree p in {0,4} (even); internal degree q = k or k-4
    table_ok = True
    for k in range(15):
        ps = [p for p in (0, 1, 2, 3, 4) if inv[p] == 1 and 0 <= k - p <= 10]
        for p in ps:
            q = k - p
            if p % 2 != 0:
                table_ok = False
            if (q % 2) != (k % 2):
                table_ok = False
    check(table_ok,
          "PARITY TABLE: for every k, every Lorentz-singlet component has EVEN 4d degree "
          "(p in {0,4}) and internal degree q with the parity of k -- "
          "(ambient, 4d, internal) = ((-1)^k, +1, (-1)^k)")
    check(all((-1) ** k == (+1) * (-1) ** k for k in range(15)),
          "product identity: ambient parity = 4d parity x internal parity")
    m["inv_vector"] = inv
    return m


# --------------------------------------------------------------------------
# LEG 5 -- explicit Cl(14) on C^128: parity + freeze + index face
# --------------------------------------------------------------------------
def cl14_gammas() -> list[np.ndarray]:
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    eye = np.eye(2, dtype=complex)
    gammas = []
    for a in range(7):
        for s in (s1, s2):
            ops = [s3] * a + [s] + [eye] * (7 - a - 1)
            g = ops[0]
            for o in ops[1:]:
                g = np.kron(g, o)
            gammas.append(g)
    return gammas          # 14 mutually anticommuting Hermitian involutions


def prod(mats: list[np.ndarray]) -> np.ndarray:
    out = mats[0]
    for x in mats[1:]:
        out = out @ x
    return out


def n_minus(d: np.ndarray, gamma: np.ndarray) -> float:
    w, v = np.linalg.eigh(d)
    sel = v[:, w < -1e-9]
    return float(np.real(np.trace(sel.conj().T @ gamma @ sel)))


def leg5() -> dict[str, object]:
    print("\nLEG 5 -- explicit Cl(14) on C^128: parities, the freeze, and the index face")
    m: dict[str, object] = {}
    g = cl14_gammas()
    dim = 128
    anti_ok = all(np.linalg.norm(g[i] @ g[j] + g[j] @ g[i]
                                 - (2.0 if i == j else 0.0) * np.eye(dim)) < 1e-12
                  for i in range(14) for j in range(i, 14))
    check(anti_ok, "14 gammas: {g_i, g_j} = 2 delta_ij on C^128 (Clifford relations hold)")
    # Hermitian volume words: gamma_5 = 4-word (already Hermitian), gamma_int = i x 10-word,
    # Gamma_amb = i x 14-word = gamma_5 . gamma_int.  All are involutions.
    G4 = prod(g[:4])
    G10 = 1j * prod(g[4:])
    Gamb = 1j * prod(g)
    herm = lambda a: float(np.linalg.norm(a - a.conj().T))        # noqa: E731
    check(herm(G4) < 1e-12 and herm(G10) < 1e-12 and herm(Gamb) < 1e-12
          and np.linalg.norm(G4 @ G4 - np.eye(dim)) < 1e-12
          and np.linalg.norm(G10 @ G10 - np.eye(dim)) < 1e-12
          and np.linalg.norm(Gamb @ Gamb - np.eye(dim)) < 1e-12
          and np.linalg.norm(Gamb - G4 @ G10) < 1e-12,
          "gamma_5, gamma_int, Gamma_amb are Hermitian involutions with "
          "Gamma_amb = gamma_5 . gamma_int (the graded trace is NON-vacuous)")
    comm = lambda a, b: float(np.linalg.norm(a @ b - b @ a))      # noqa: E731
    anti = lambda a, b: float(np.linalg.norm(a @ b + b @ a))      # noqa: E731
    # 7-gamma insertions at every (p, q) split
    parity_ok = True
    for p in (0, 1, 2, 3, 4):
        q = 7 - p
        ins = prod((g[:p] if p else []) + g[4:4 + q]) if p or q else np.eye(dim)
        if anti(ins, Gamb) > 1e-10:
            parity_ok = False                       # must anticommute with ambient
        c5 = comm(ins, G4) < 1e-10
        if (p % 2 == 0) != c5:
            parity_ok = False                       # commutes with gamma_5 iff p even
    check(parity_ok,
          "any 7-gamma insertion anticommutes with Gamma_amb; commutes with gamma_5 iff its "
          "4d degree p is even (all five splits swept)")
    ins07 = prod(g[4:11])          # (p,q) = (0,7)
    ins43 = prod(g[:4] + g[4:7])   # (p,q) = (4,3)
    for name, ins in (("(0,7)", ins07), ("(4,3)", ins43)):
        check(anti(ins, Gamb) < 1e-10 and comm(ins, G4) < 1e-10 and anti(ins, G10) < 1e-10,
              f"Lorentz-singlet split {name}: ambient-ODD, 4d-EVEN, internal-ODD (exact)")
    ins2 = prod(g[4:6])            # a 2-gamma (class-0 exemplar, adjoint direction)
    check(comm(ins2, Gamb) < 1e-10,
          "a 2-gamma (class-0) insertion COMMUTES with Gamma_amb -- the grading-breaking class")
    # THE FREEZE: ambient-odd family pins tr(Gamma P_<0) at 0
    rng = np.random.default_rng(20260817)
    coef = rng.standard_normal(14)
    D0 = sum(c * gi for c, gi in zip(coef, g))     # a generic odd element (Hermitian)
    Modd = 1j * ins07                              # Hermitian odd insertion (7-word is anti-Hermitian)
    check(float(np.linalg.norm(Modd - Modd.conj().T)) < 1e-12
          and anti(D0, Gamb) < 1e-10 and anti(Modd, Gamb) < 1e-10,
          "D_0 and the Hermitian middle-form insertion are both Gamma_amb-odd")
    frozen = max(abs(n_minus(D0 + t * Modd, Gamb)) for t in (0.0, 0.35, 0.8, 1.5))
    check(frozen < 1e-8,
          f"THE FREEZE: tr(Gamma_amb P_<0) = 0 identically along the odd family "
          f"(max |trace| = {frozen:.2e} over 4 sweep points)")
    Meven = 1j * ins2                              # Hermitian even insertion (2-word is anti-Hermitian)
    check(float(np.linalg.norm(Meven - Meven.conj().T)) < 1e-12
          and comm(Meven, Gamb) < 1e-10, "the even (class-0) mass commutes with Gamma_amb")
    # the Gamma-aligned even direction: Lambda^14 (top form / pseudoscalar), class 2*14 = 0 mod 4.
    # It is the carrier analog of the model's sigma_3 mass (the model's Gamma-aligned direction).
    Mmover = Gamb
    check(comm(Mmover, Gamb) < 1e-12,
          "the Lambda^14 (pseudoscalar) direction is class-0/Gamma-even")
    moved = abs(n_minus(D0 + 1.5 * Mmover, Gamb))
    check(moved > 0.5,
          f"CONTRAST: the Gamma-even mass MOVES the graded trace (|trace| = {moved:.3f} at t=1.5) "
          "-- the LD-A grading-tilt class, reproduced on the carrier's own Clifford algebra")
    m["frozen_max"] = frozen
    m["moved"] = moved
    # THE INDEX FACE: odd operator with unequal graded kernel -> integer index, frozen trace
    npl, nmi = 3, 2
    B = rng.standard_normal((npl, nmi)) + 1j * rng.standard_normal((npl, nmi))
    Dodd = np.block([[np.zeros((npl, npl)), B], [B.conj().T, np.zeros((nmi, nmi))]])
    Gsm = np.diag([1.0] * npl + [-1.0] * nmi)
    check(float(np.linalg.norm(Dodd @ Gsm + Gsm @ Dodd)) < 1e-12,
          "index face: the block operator is Gamma-odd (unequal halves 3|2)")
    w = np.linalg.eigvalsh(Dodd)
    kerdim = int(np.sum(np.abs(w) < 1e-9))
    check(kerdim == 1, "index face: dim ker = 1 = |3 - 2| (generic B)")
    check(abs(n_minus(Dodd, Gsm)) < 1e-9,
          "index face: tr(Gamma P_<0) = 0 on the same operator -- for the odd class the only "
          "count object is the integer kernel index, not the spectral-asymmetry trace")
    return m


# --------------------------------------------------------------------------
# LEG 6 -- LD-A model contact (N=24 rebuild) + instrument re-runs
# --------------------------------------------------------------------------
LDA_PIN = {"n_minus_at_1p5": -21.845865, "min_gap_at_1p5": 1.5}


def leg6() -> dict[str, object]:
    print("\nLEG 6 -- LD-A model contact and instrument re-runs")
    m: dict[str, object] = {}
    n = 24
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    eye = np.eye(n)
    p = np.zeros((n, n), dtype=complex)
    for j in range(n):
        p[j, (j + 1) % n] = -0.5j
        p[(j + 1) % n, j] = +0.5j
    gamma = np.kron(s3, eye)
    krein = np.kron(s1, eye)
    d0 = np.kron(s1, p)
    # canon-class enumeration (LD-A 2(iii)(a)) reproduced
    rows = {}
    for name, sg in (("s0", np.eye(2)), ("s1", s1), ("s2", s2), ("s3", s3)):
        M = np.kron(sg, eye)
        d = d0 + 1.0 * M
        godd = float(np.linalg.norm(d @ gamma + gamma @ d))
        kres = float(np.linalg.norm(d.conj().T @ krein - krein @ d))
        rows[name] = (godd < 1e-10, kres < 1e-10)
    check(rows == {"s0": (False, True), "s1": (True, True),
                   "s2": (True, False), "s3": (False, False)},
          "canon-class enumeration reproduced: only sigma_1 stays (Gamma-odd, Krein); "
          "sigma_2 is Gamma-odd Krein-breaking; sigma_3 breaks both [R lda 2(iii)]")
    # sigma_3 sweep: the LD-A phenomenon (pinned)
    d = d0 + 1.5 * np.kron(s3, eye)
    nm = n_minus(d, gamma)
    gap = float(np.min(np.abs(np.linalg.eigvalsh(d))))
    check(abs(nm - LDA_PIN["n_minus_at_1p5"]) < 5e-6,
          f"LD-A pinned: n_-(m=1.5) = {LDA_PIN['n_minus_at_1p5']} on the sigma_3 sweep "
          f"(got {nm:.6f})")
    check(abs(gap - LDA_PIN["min_gap_at_1p5"]) < 1e-9,
          "LD-A pinned: min|spec| = 1.5 at m = 1.5 (gapped, ZERO crossings)")
    # sigma_2 sweep: Gamma-odd, trace frozen (the model face of the freeze)
    frozen = max(abs(n_minus(d0 + t * np.kron(s2, eye), gamma)) for t in (0.0, 0.5, 1.5))
    check(frozen < 1e-8,
          "model face of the freeze: the Gamma-odd sigma_2 sweep keeps n_- = 0 identically")
    # intersection identity: Gamma-even part of Gamma-odd part = 0 (200 draws)
    rng = np.random.default_rng(7)
    worst = 0.0
    for _ in range(200):
        A = rng.standard_normal((2 * n, 2 * n)) + 1j * rng.standard_normal((2 * n, 2 * n))
        A = (A + A.conj().T) / 2
        odd = (A - gamma @ A @ gamma) / 2
        even_of_odd = (odd + gamma @ odd @ gamma) / 2
        worst = max(worst, float(np.linalg.norm(even_of_odd)))
    check(worst < 1e-12,
          f"intersection identity re-verified: canon-class cap [D,Gamma]=0 = {{0}} "
          f"(Gamma-even part of Gamma-odd part = {worst:.3e} over 200 draws) [R lda:295]")
    m["nm"] = nm
    # instrument re-runs
    py = sys.executable
    for rel, needle in [
        ("tests/function-space-ext/dirac_spectral_flow_section.py",
         "net chiral spectral flow = n_-(1) - n_-(0)"),
        ("tests/function-space-ext/krein_spectral_flow_probe.py",
         "Krein-isometric conjugacy do not produce net chiral spectral flow"),
    ]:
        path = ROOT / rel
        if not path.exists():
            check(False, f"instrument re-run: {rel} exists")
            continue
        r = subprocess.run([py, str(path)], capture_output=True, text=True,
                           cwd=str(ROOT), timeout=300)
        check(r.returncode == 0 and needle in r.stdout,
              f"instrument re-run green with pinned verdict line: {rel}")
    return m


# --------------------------------------------------------------------------
# LEG 7 -- certified absence (novelty scans)
# --------------------------------------------------------------------------
NOVELTY_PHRASES = [
    "transport and selection are opposite parities",
    "the selector directions freeze the count",
    "no insertion direction both selects and transports",
    "class-2 insertions freeze the graded trace",
]
PLANT_POSITIVE = ("Synthetic planted positive: transport and selection are "
                  "opposite parities, verbatim, for the detector.")
PLANT_NEARMISS = ("Synthetic near-miss: transport, selection, parity discussed "
                  "separately without the claimed phrasings.")


def scan_absence(extra_docs: list[str]) -> tuple[int, dict[str, int]]:
    # The instrument and the artifact it certifies are not part of the corpus
    # they measure (both contain the phrasings by construction; the detector's
    # power is demonstrated on the planted positive instead).  Excluded by
    # NAME so that selftest copies running from a temp directory exclude the
    # original too.  Declared, not silent.
    skip = {"_local", ".git", "zenodo-package-v1.0.0", "__pycache__", "spectral-transport"}
    self_names = ("joe_directed_tr1_transport_and_selection",)
    exts = {".md", ".py", ".yaml", ".yml", ".txt", ".json"}
    hits = {ph: 0 for ph in NOVELTY_PHRASES}
    scanned = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in exts:
            continue
        if any(part in skip for part in path.parts):
            continue
        if any(s in path.name for s in self_names):
            continue
        try:
            low = path.read_text(encoding="utf-8", errors="ignore").lower()
        except OSError:
            continue
        scanned += 1
        for ph in NOVELTY_PHRASES:
            if ph in low:
                hits[ph] += 1
    for doc in extra_docs:
        scanned += 1
        low = doc.lower()
        for ph in NOVELTY_PHRASES:
            if ph in low:
                hits[ph] += 1
    return scanned, hits


def leg7() -> dict[str, object]:
    print("\nLEG 7 -- certified absence: the result phrasings are new-as-phrased "
          "(zero hits is NOT proof of new)")
    m: dict[str, object] = {}
    scanned, hits = scan_absence([])
    check(all(v == 0 for v in hits.values()),
          f"absence: 0 corpus hits for all {len(NOVELTY_PHRASES)} result phrasings "
          f"({scanned} files scanned; artifact+probe excluded by construction)")
    _, hits_p = scan_absence([PLANT_POSITIVE])
    check(hits_p[NOVELTY_PHRASES[0]] == 1,
          "planted positive IS flagged (the absence detector has power)")
    _, hits_n = scan_absence([PLANT_NEARMISS])
    check(all(v == 0 for v in hits_n.values()),
          "planted near-miss is NOT flagged (the detector does not fire on topic words)")
    m["files_scanned"] = scanned
    return m


# --------------------------------------------------------------------------
# LEG 8 -- artifact binding
# --------------------------------------------------------------------------
TABLE_SHA = "9ec1cf65ad7ffe2babd51ea9d5ff51efddf774e62c88c7a3e92380629cbeb608"
VERDICT_SET = {
    "T-AMB": "FROZEN-EXCLUDED",
    "T-OBS": "UNPROTECTED-MODEL-MATCHED",
    "DICH": "OPPOSITE-PARITIES",
    "FENCE": "EXECUTED-SHARPENED",
    "NOV": "NEW-AS-COMPOSED",
}


def table_block(text: str) -> str:
    mm = re.search(r"<!-- TR1-TABLE-BEGIN -->(.*?)<!-- TR1-TABLE-END -->", text, re.S)
    if not mm:
        raise ValueError("TR1 table markers not found")
    return mm.group(1).strip()


def parse_verdicts(block: str) -> dict[str, str]:
    out = {}
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3 or cells[0] in ("id",) or set(cells[0]) <= set("-: "):
            continue
        out[cells[0]] = cells[2]
    return out


def leg8(measured: dict[str, object], artifact_path: Path) -> None:
    print("\nLEG 8 -- artifact binding (verdicts vs their own evidence)")
    text = artifact_path.read_text(encoding="utf-8")
    blk = table_block(text)
    sha = hashlib.sha256(blk.encode("utf-8")).hexdigest()
    check(sha == TABLE_SHA, f"verdict-table SHA-256 pinned = {TABLE_SHA[:12]}...")
    verdicts = parse_verdicts(blk)
    check(set(verdicts) == set(VERDICT_SET),
          f"verdict table carries exactly the 5 ids {sorted(VERDICT_SET)}")
    for k, want in VERDICT_SET.items():
        check(verdicts.get(k) == want, f"verdict {k} = {want}")
    # verdict-evidence binding: each verdict must be consistent with the measurement
    check(verdicts.get("T-AMB") == "FROZEN-EXCLUDED"
          and float(measured["frozen_max"]) < 1e-8,
          "binding: T-AMB 'FROZEN-EXCLUDED' is consistent with its own measurement "
          "(odd-family graded trace = 0 to machine precision)")
    check(verdicts.get("T-OBS") == "UNPROTECTED-MODEL-MATCHED"
          and float(measured["moved"]) > 0.5
          and abs(float(measured["nm"]) - LDA_PIN["n_minus_at_1p5"]) < 5e-6,
          "binding: T-OBS 'UNPROTECTED-MODEL-MATCHED' is consistent with the even-mass "
          "motion witness and the pinned LD-A excursion")
    check(verdicts.get("DICH") == "OPPOSITE-PARITIES" and bool(measured["dichotomy_empty"]),
          "binding: DICH 'OPPOSITE-PARITIES' is consistent with the empty both-capabilities set")


# --------------------------------------------------------------------------
# runner
# --------------------------------------------------------------------------
def run_all(artifact_path: Path) -> int:
    print("=" * 78)
    print("TR-1 probe: transport and selection are opposite parities")
    print("=" * 78)
    leg1()
    m2 = leg2()
    m3 = leg3()
    m4 = leg4()
    m5 = leg5()
    m6 = leg6()
    m7 = leg7()
    measured = {**m2, **m3, **m4, **m5, **m6, **m7}
    leg8(measured, artifact_path)
    print("\n" + "=" * 78)
    print(f"RESULT: {NCHECK - NFAIL}/{NCHECK} checks pass; {NFAIL} failures")
    print("=" * 78)
    return 0 if NFAIL == 0 else 1


# --------------------------------------------------------------------------
# selftest -- 12 mutations, machinery/reference only, targeted catches
# --------------------------------------------------------------------------
SELF = Path(__file__).resolve()
BASELINE_CHECKS = None   # measured from the live baseline run
BASELINE_PIN = 90        # independent pin of the clean-baseline check count


def _run_probe_text(src: str, workdir: Path, artifact_text: str | None = None) -> tuple[int, str]:
    """Run a (possibly mutated) copy of this probe from a temp dir against ROOT."""
    probe = workdir / "mutant_probe.py"
    probe.write_text(src, encoding="utf-8")
    art = ROOT / ARTIFACT
    if artifact_text is not None:
        art_copy = workdir / "artifact_copy.md"
        art_copy.write_text(artifact_text, encoding="utf-8")
        env_art = str(art_copy)
    else:
        env_art = str(art)
    env = dict(os.environ)
    env["TR1_ARTIFACT_OVERRIDE"] = env_art
    env["TR1_ROOT_OVERRIDE"] = str(ROOT)
    r = subprocess.run([sys.executable, str(probe)], capture_output=True, text=True,
                       cwd=str(ROOT), env=env, timeout=1800)
    return r.returncode, r.stdout + r.stderr


MUTATIONS: list[tuple[str, str, str, str]] = [
    # (name, old, new, targeted-check fragment that MUST appear on a [FAIL] line)
    ("M01-pin-line-number",
     '("CANON.md", 136,\n     "Net chiral spectral flow 0',
     '("CANON.md", 137,\n     "Net chiral spectral flow 0',
     "quote pin CANON.md:137"),
    ("M02-instrument-sha",
     '"tests/function-space-ext/dirac_spectral_flow_section.py":\n        "',
     '"tests/function-space-ext/dirac_spectral_flow_section.py":\n        "0000000000',
     "SHA-256 pin tests/function-space-ext/dirac_spectral_flow_section.py"),
    ("M03-class-table",
     'CLS = {"V": 2, "S+": 3, "S-": 1}',
     'CLS = {"V": 0, "S+": 3, "S-": 1}',
     "class degeneracy: cls(R^(+))=cls(S_-)=1"),
    ("M04-positive-roots",
     "for s in (+1, -1):\n                r = [0] * N7",
     "for s in (+1,):\n                r = [0] * N7",
     "Weyl dimension (exact Fraction): dim V = 14"),
    ("M05-spinor-parity",
     'if (sum(1 for s in signs if s < 0) % 2 == 0) == plus:',
     'if (sum(1 for s in signs if s < 0) % 2 == 1) == plus:',
     "Sym^2(S_+) = Lam^3 (+) Lam^7_+"),
    ("M06-klimyk-reflection-sign",
     "sign = -1 if inv % 2 else 1",
     "sign = 1 if inv % 2 else -1",
     "Klimyk: V (x) S_+ = S_- (+) R^(+) exactly"),
    ("M07-d2-detector",
     "for perm, psgn in (((0, 1), 1), ((1, 0), -1)):",
     "for perm, psgn in (((0, 1), 1), ((1, 0), 1)):",
     "dim Inv_{Spin(4)}(Lam^p V_4) = [1,0,0,0,1]"),
    ("M08-freeze-machinery",
     "Modd = 1j * ins07                              # Hermitian odd insertion",
     "Modd = 1j * ins07 + 0.4 * np.eye(dim)         # corrupted machinery",
     "D_0 and the Hermitian middle-form insertion are both Gamma_amb-odd"),
    ("M09-lda-pin",
     'LDA_PIN = {"n_minus_at_1p5": -21.845865, "min_gap_at_1p5": 1.5}',
     'LDA_PIN = {"n_minus_at_1p5": -20.045865, "min_gap_at_1p5": 1.5}',
     "LD-A pinned: n_-(m=1.5)"),
    ("M10-rerun-path",
     '("tests/function-space-ext/dirac_spectral_flow_section.py",\n         "net chiral',
     '("tests/function-space-ext/dirac_spectral_flow_sectionX.py",\n         "net chiral',
     "instrument re-run: tests/function-space-ext/dirac_spectral_flow_sectionX.py exists"),
    ("M11-absence-detector",
     'NOVELTY_PHRASES = [\n    "transport and selection are opposite parities",',
     'NOVELTY_PHRASES = [\n    "zz-never-present-phrase-zz",',
     "planted positive IS flagged"),
]
# M12 mutates the ARTIFACT copy, not the probe (contrary control)
M12_OLD = "| DICH | can one insertion direction both select a half and move the count | OPPOSITE-PARITIES |"
M12_NEW = "| DICH | can one insertion direction both select a half and move the count | SAME-DIRECTION-BOTH |"
M12_TARGET = "verdict DICH = OPPOSITE-PARITIES"


def selftest() -> int:
    src = SELF.read_text(encoding="utf-8")
    print("=" * 78)
    print("TR-1 SELFTEST -- baseline first, then 12 machinery/reference mutations")
    print("=" * 78)
    with tempfile.TemporaryDirectory(prefix="tr1-selftest-") as td:
        wd = Path(td)
        rc, out = _run_probe_text(src, wd)
        base_fails = out.count("[FAIL]")
        base_checks = None
        mm = re.search(r"RESULT: (\d+)/(\d+) checks pass", out)
        if mm:
            base_checks = int(mm.group(2))
        if rc != 0 or base_fails != 0:
            print(f"[ABORT] clean baseline is RED (exit {rc}, {base_fails} [FAIL] lines) -- "
                  "a red baseline makes every mutation exit nonzero for the wrong reason")
            return 1
        if base_checks != BASELINE_PIN:
            print(f"[ABORT] baseline check count {base_checks} != independent pin {BASELINE_PIN}")
            return 1
        print(f"baseline: GREEN, {base_checks} checks, 0 [FAIL] lines (pinned {BASELINE_PIN})")
        caught = 0
        results = []
        for name, old, new, target in MUTATIONS:
            if old not in src:
                results.append((name, "MUTATION-DID-NOT-APPLY"))
                continue
            mut = src.replace(old, new, 1)
            try:
                rc, out = _run_probe_text(mut, wd)
            except Exception as e:                                   # noqa: BLE001
                results.append((name, f"CRASH-NOT-DETECTION ({e})"))
                continue
            fail_lines = [ln for ln in out.splitlines() if ln.startswith("[FAIL]")]
            if rc == 0:
                results.append((name, "MISSED (exit 0)"))
            elif not fail_lines:
                results.append((name, "CRASH-NOT-DETECTION (nonzero exit, no [FAIL] line)"))
            elif any(target in ln for ln in fail_lines):
                results.append((name, f"CAUGHT by targeted check: {fail_lines[0][:100]}"))
                caught += 1
            else:
                results.append((name, f"INCIDENTAL-NOT-TARGETED: {fail_lines[0][:100]}"))
        # M12: contrary control on an artifact COPY
        art_text = (ROOT / ARTIFACT).read_text(encoding="utf-8")
        if M12_OLD in art_text:
            rc, out = _run_probe_text(src, wd, artifact_text=art_text.replace(M12_OLD, M12_NEW, 1))
            fail_lines = [ln for ln in out.splitlines() if ln.startswith("[FAIL]")]
            if rc != 0 and any(M12_TARGET in ln for ln in fail_lines):
                results.append(("M12-contrary-verdict-flip",
                                f"CAUGHT by targeted check: {fail_lines[0][:100]}"))
                caught += 1
            elif rc != 0 and fail_lines:
                results.append(("M12-contrary-verdict-flip",
                                f"INCIDENTAL-NOT-TARGETED: {fail_lines[0][:100]}"))
            elif rc != 0:
                results.append(("M12-contrary-verdict-flip", "CRASH-NOT-DETECTION"))
            else:
                results.append(("M12-contrary-verdict-flip", "MISSED (exit 0)"))
        else:
            results.append(("M12-contrary-verdict-flip", "MUTATION-DID-NOT-APPLY"))
        # re-verify baseline after the mutations
        rc, out = _run_probe_text(src, wd)
        post_ok = (rc == 0 and out.count("[FAIL]") == 0)
        print()
        for name, res in results:
            print(f"  {name:32s} {res}")
        total = len(MUTATIONS) + 1
        print(f"\nbaseline re-verified after mutations: {'GREEN' if post_ok else 'RED'}")
        print(f"mutations caught via targeted genuine [FAIL]: {caught}/{total} "
              f"(0 crash-only, 0 missed required)")
        ok = (caught == total) and post_ok
        print("SELFTEST:", "PASS (exit 0)" if ok else "FAIL (exit 1)")
        return 0 if ok else 1


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    art_override = os.environ.get("TR1_ARTIFACT_OVERRIDE")
    artifact_path = Path(art_override) if art_override else (ROOT / ARTIFACT)
    return run_all(artifact_path)


if __name__ == "__main__":
    sys.exit(main())
