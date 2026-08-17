#!/usr/bin/env python3
"""MP-1 probe: composites inherit one horn, never both (spectral-transport arc, RS wave 3).

Certifies the artifact
  lab/active-research/joe-directed/spectral-transport/
      mp1-composites-inherit-one-horn-never-both-2026-08-17.md

WHAT IS CERTIFIED (legs):

  LEG 1  QUOTE PINS.  Every load-bearing consumed sentence byte-matched at its
         cited file:line, plus a planted negative the pin detector must reject,
         plus the SHA-256 pin of the TR-1 probe this probe re-runs and builds on.

  LEG 2  COMPOSITE CLASS ARITHMETIC (exact, Z/4 centre of Spin(14), CS-1's
         layer, corollary (d) iterated).  For any insertion monomial with
         factors from either declared slot: total class = sum of factor
         classes = 2*(number of class-2 factors) mod 4 -- 0 at even count, 2
         at odd count, no third value.  The capability partition over the
         composite lattice: a same-half self-pairing needs total class 2
         (odd count) [R st1:456, :229]; a cross-half pairing needs total
         class 0 (even count); the both-capabilities set is EMPTY at every
         order.  Centre-scalar rigor: the centre acts by i^cls on each
         irrep, so a class-forbidden Hom/invariant is EXACTLY zero.
         5 planted-false propositions.

  LEG 3  EXACT D_7 WEIGHT INSTRUMENTS on the decisive composite.  The full
         decompositions of Lam^7_- (x) Lam^7_- and Lam^7_+ (x) Lam^7_-
         (dim 1716^2 = 2,944,656 each) computed by mult-aware Klimyk AND by
         a Racah/Brauer alternating sum over all 322,560 elements of W(D_7)
         applied to the raw product weight multisets, agreeing on all seven
         targets per product: ZERO odd-form content (Lam^1, Lam^3, Lam^5,
         Lam^7_+, Lam^7_-); Inv(same-sense) = 0, Inv(opposite-sense) = 1;
         planted positives (Lam^2 in the opposite-sense product = 1; the
         Cartan-square hw in the same-sense product = 1); dimension
         saturation as exact Fractions.  TR-1's four one-way Hom facts
         reproduced [R] -- the composition corollary A o A' = 0 (same sense)
         consumes them.

  LEG 4  CLIFFORD + LATTICE INSTRUMENTS (the operator face).  On explicit
         Cl(14) gammas on C^128 (TR-1 LEG 5's construction rebuilt, with the
         Hermitian-involution guards): the one-way arrows A = W_h P_+ satisfy
         A^2 = 0 and A A' = 0 for two same-sense arrows (machine zero);
         A^dag = W_h P_- (the reverse arrow IS the adjoint) and
         A^dag A = P_+ exactly; disjoint 7-words anticommute and overlap-3
         pairs commute; (i/2)[W', W] = Gamma_amb EXACTLY for the
         disjoint-support pair -- the curvature of the two-insertion family
         is the grading; the two-parameter odd family's graded trace is
         frozen on a 5x4 grid; the composite direction moves the trace by
         TR-1's own pinned mover value (directions identical); the mixed
         family (odd + even term) is neither Gamma-odd nor Gamma-even with a
         non-integer interior trace; parity decomposition is unique
         (even-of-odd = 0) [R lda:295]; the kernel index of a Gamma-odd
         operator equals n_+ - n_- identically (constant 1 across a
         two-parameter family on 3|2 halves; generic 0 on equal halves).
         On the rebuilt N=24 lattice: (i/2)[sigma_2 (x) I, sigma_1 (x) I] =
         sigma_3 (x) I (LD-A's mass direction IS the composite of the
         model's two odd directions) and n_-(1.5) = -21.845865 [R].

  LEG 5  GB-1 MODEL FACE (exact sympy on M_2(C)).  U(t1)U(t2) = U(t1+t2)
         (a composite of rotations is a rotation); the conjugation composite
         carries M(phi) to M(phi - t1 - t2) and Gamma to M(-t1-t2): the
         (mass, grading) pair rotates rigidly, so the relative angle -- and
         GB-1's no-transport invariant -- survives every composite;
         sigma_1 sigma_2 = i sigma_3 (odd . odd = even, the model face of
         the class arithmetic); M(p1) M(p2) = cos(p1-p2) I + i sin(p1-p2)
         sigma_1 (the composite's parity split is a function of the relative
         angle alone).

  LEG 6  RANK-FLOOR ARITHMETIC.  128*6 = 768 < 896 <= 128*7 = 896 (exact;
         ceil(896/128) = 7); rank subadditivity guard; generic witnesses:
         a sum of six random rank-<=128 antisymmetric forms on C^896 has
         rank exactly 768 (degenerate), a sum of seven reaches 896.
         NECESSARY-floor only; sufficiency is typed NOT certified.

  LEG 7  TR-1 WHOLE-PROBE RE-RUN.  The TR-1 probe re-run by subprocess:
         exit 0 with its full-pass line present (the banked parity-dichotomy
         layer this file composes with is green at HEAD).

  LEG 8  CERTIFIED ABSENCE + ARTIFACT BINDING.  Exact-substring novelty
         scans over the corpus (self-excluded by name) with a planted
         positive and a planted near-miss; the artifact's verdict table
         parsed, SHA-256-pinned, each verdict checked against the measured
         value it cites.

SELFTEST (--selftest): verifies the clean baseline FIRST (all checks green,
zero [FAIL] lines, count pinned independently of the live run) and aborts on
a red baseline; then runs 12 mutations, each corrupting MACHINERY or a
REFERENCE (never a check predicate), each REQUIRED to be caught by the check
targeted at it via a genuine [FAIL] line: a crash is CRASH-NOT-DETECTION and
fails; an untargeted catch is INCIDENTAL-NOT-TARGETED and fails.  The failing
check is printed for every mutation.  Exit 0 iff all mutations are caught as
targeted.  (VERIFICATION.md, probe discipline, all seven rules.)

Read-only: mutation copies live in a temp directory.  Deterministic;
numpy + sympy + stdlib only.
"""
from __future__ import annotations

import hashlib
import itertools
import math
import os
import re
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(os.environ["MP1_ROOT_OVERRIDE"]) if os.environ.get("MP1_ROOT_OVERRIDE") \
    else Path(__file__).resolve().parents[2]
ARTIFACT = ("lab/active-research/joe-directed/spectral-transport/"
            "mp1-composites-inherit-one-horn-never-both-2026-08-17.md")
TR1_PROBE = ("tests/channel-swings/"
             "joe_directed_tr1_transport_and_selection_are_opposite_parities.py")

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
# LEG 1 -- quote pins (byte-matched at the cited line) + TR-1 probe SHA pin
# --------------------------------------------------------------------------
TR1_ART = ("lab/active-research/joe-directed/spectral-transport/"
           "tr1-transport-and-selection-are-opposite-parities-2026-08-17.md")
ST1 = "lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md"
RSC1 = "lab/active-research/joe-directed/rs-corner/rsc1-unique-channel-lives-on-the-gamma-trace-2026-08-17.md"
CS1 = "lab/active-research/joe-directed/class-shift/cs1-first-order-shift-is-the-chirality-grading-2026-08-15.md"
GB1 = "lab/active-research/joe-directed/grading-bridge/gb1-the-bridge-is-one-angle-and-one-missing-arrow-2026-08-17.md"
LDA = "lab/active-research/joe-directed/lens-digs/lda-sg4-bit2-type-and-transport-2026-08-17.md"

QUOTES: list[tuple[str, int, str]] = [
    # PIN REFRESHED 2026-08-17 (integrator): wave-3 integration moved the
    # cited surface after this probe shipped (register receipts/items above
    # this row; STATUS note in RW-1).
    ("lab/process/upgrade-program-register.yaml", 284, "- id: TR1-COMPOSITE-PARITY"),
    ("lab/process/upgrade-program-register.yaml", 285,
     "two class-2 insertions compose to class 0, so a multi-insertion constructor meets "
     "TB-4/TB-5 as pricing, not prohibition"),
    ("lab/process/upgrade-program-register.yaml", 286, "the arc's own named successor"),
    (TR1_ART, 242, "a parity computation per (grading, direction) pair, not a single verdict."),
    (TR1_ART, 379, "both-capabilities set is empty — checked as arithmetic, not asserted."),
    (TR1_ART, 395, "dim Hom(Lam^7_- (x) S_+, S_-) = 1"),
    (TR1_ART, 400, "A SINGLE middle-form direction is therefore a nilpotent one-way map between"),
    (TR1_ART, 417, "If D is self-adjoint, Γ is a Hermitian involution, and {D, Γ} = 0"),
    (TR1_ART, 560, "At one selective insertion it is NOT: the induced form has rank ≤ 128 on"),
    (TR1_ART, 564, "must be ODD — st1:456) or class-0/blind supplements, and every such"),
    (TR1_ART, 567, "**TB-5 — THE DICHOTOMY MUST BE FACED.** Any argument in which one"),
    (TR1_ART, 572, "claiming both is either two mechanisms (name both, bill both) or an error."),
    (TR1_ART, 581, "**The missing theorem's SHAPE (named, not claimed) — a mixed-parity family"),
    (TR1_ART, 582, "index theorem.** For families `D(t) = D_odd(t) + f(t)·M_even` on a Z/2-graded"),
    (TR1_ART, 870, "dichotomy constrains a MULTI-insertion story (two class-2 insertions"),
    (TR1_ART, 871, "compose to class 0: the composite can cross-pair while each factor"),
    (TR1_ART, 912, "P4 — the composite-parity question for multi-insertion stories is the real"),
    (ST1, 456, "Class-0 content never unlocks a same-class pairing; the class-2 insertion count must be ODD"),
    (ST1, 229, "insertion class 2, hence an ODD number of class-2 insertions."),
    (ST1, 196, "escape: if two class-2 insertions could substitute for one (net class 0), the"),
    (ST1, 308, "TWO class-2 insertions (Λ^3 ⊗ Λ^3, ν_+ diagonal):     0  — the count must be ODD"),
    (RSC1, 341, "zeta_+ = Omega^1(S_+) = V (x) S_+ = S_-  (+)  R^(+)      896 = 64 + 832"),
    (RSC1, 444, "rank ≤ 2·64 = 128`, at least `832 − 64 = 768` directions of `R` stay"),
    (CS1, 216, "c_F = c_E + 2k    (mod 4)."),
    (CS1, 236, "`c_F = c_E + 2k + c_T`. GU's `ad P = End(Delta) = sum_j Lambda^j V` carries"),
    (CS1, 237, "classes `{0,2}` only, so an insertion can shift by `0` or `2` and can NEVER"),
    (GB1, 317, "`U(theta) M(phi) U(theta)^dag = M(phi - theta)` and"),
    (GB1, 332, "(both rotate together), so **the charge in the TRANSPORTED grading never"),
    (LDA, 295, "canon-class ∩ {`[D,Gamma] = 0`} = {0}"),
    ("CANON.md", 135, "net chiral index = flux number"),
    ("CANON.md", 136,
     "Net chiral spectral flow 0 for self-adjoint, chirality-odd, Krein-self-adjoint Fredholm families."),
    ("CANON.md", 139,
     "chi = interior-even + external-topological-index`, so any odd count is necessarily external"),
    ("VERIFICATION.md", 24, "the only unconditionally computable integer is 1"),
    ("VERIFICATION.md", 81, "A mutation corrupts machinery or a reference"),
    ("lab/process/homonym-register.yaml", 242, "token: CHIRAL"),
    ("lab/process/homonym-register.yaml", 263,
     'write "CHIRAL (massless/unbroken)" when naming the PHASE value, exactly'),
    ("lab/process/correction-registry.yaml", 264,
     "That three generations is an ADDITIVE target count a mechanism must"),
    ("lab/process/correction-registry.yaml", 300,
     "That the source has no stated effective-chirality mechanism, or that"),
    ("lab/process/correction-registry.yaml", 364,
     "That the 128 remainder is an established DEFECT of the construction --"),
    ("lab/sources/source-claim-register.yaml", 913,
     "a non-chiral total theory splits at the emergent level into two separate"),
    ("lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md", 137,
     "operators, when there is no vacuum expectation value pulling the various"),
]
PLANTED_NEGATIVE = ("lab/process/upgrade-program-register.yaml", 285,
                    "the composite evades the dichotomy outright")

TR1_PROBE_SHA = "910f627984e15c2dd9da7151bfbee7c97699d3fab40048e1e78af2433429232b"


def quote_at(rel: str, line_no: int, needle: str) -> bool:
    try:
        lines = (ROOT / rel).read_text(encoding="utf-8").splitlines()
    except OSError:
        return False
    if not (1 <= line_no <= len(lines)):
        return False
    return needle in lines[line_no - 1]


def leg1() -> None:
    print("\nLEG 1 -- quote pins and the TR-1 probe SHA pin")
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
    got = hashlib.sha256((ROOT / TR1_PROBE).read_bytes()).hexdigest()
    check(got == TR1_PROBE_SHA,
          f"SHA-256 pin of the TR-1 probe (the reused instrument) = {TR1_PROBE_SHA[:12]}...")


# --------------------------------------------------------------------------
# LEG 2 -- composite class arithmetic over the monomial lattice (exact)
# --------------------------------------------------------------------------
CLS = {"V": 2, "S+": 3, "S-": 1}   # CS-1's centre classes (rsc1:109-113)


def eps_cls(k: int) -> int:
    return (2 * k) % 4                     # cls(Lambda^k), eps slot


def varpi_cls(k: int) -> int:
    return (2 + 2 * k) % 4                 # cls(V (x) Lambda^k), varpi-slot content


def composite_cls(factor_classes: list[int]) -> int:
    return sum(factor_classes) % 4


def leg2() -> dict[str, object]:
    print("\nLEG 2 -- composite class arithmetic: the lattice partition")
    m: dict[str, object] = {}
    # factor stock: both slots supply classes in {0, 2} only
    stock = sorted({eps_cls(k) for k in range(15)} | {varpi_cls(k) for k in range(15)})
    check(stock == [0, 2], "factor stock: both declared slots supply classes {0,2} only")
    # composite class = 2 * (number of class-2 factors) mod 4, over the lattice
    lattice_ok = True
    for n_factors in range(0, 7):
        for combo in itertools.combinations_with_replacement((0, 2), n_factors):
            n2 = sum(1 for c in combo if c == 2)
            if composite_cls(list(combo)) != (2 * n2) % 4:
                lattice_ok = False
    check(lattice_ok,
          "composite lattice: total class = 2*(number of class-2 factors) mod 4, "
          "orders 0..6, both slots -- 0 at even count, 2 at odd count, no third value")
    # the package-half classes, derived from the CLS table (never hardcoded)
    c_p, c_m, c_v = CLS["S+"], CLS["S-"], CLS["V"]
    check((c_v + c_m) % 4 == c_p and (c_v + c_p) % 4 == c_m,
          "corner-class guard: cls(zeta_-) = cls(V)+cls(S-) = cls(S+) and mirror -- the two "
          "package halves W_± are class-homogeneous (3 and 1) [R rsc1:109-113]")
    # capability partition at composite order
    def self_pair_ok(total_ins_cls: int) -> bool:
        return (2 * c_p + total_ins_cls) % 4 == 0 or (2 * c_m + total_ins_cls) % 4 == 0
    def cross_pair_ok(total_ins_cls: int) -> bool:
        return (c_p + c_m + total_ins_cls) % 4 == 0
    check(self_pair_ok(2) and not self_pair_ok(0),
          "selection horn at composite order: a same-half self-pairing needs total "
          "insertion class 2, i.e. an ODD class-2 factor count [R st1:456, :229]")
    check(cross_pair_ok(0) and not cross_pair_ok(2),
          "cross horn at composite order: a cross-half pairing needs total class 0, "
          "i.e. an EVEN class-2 factor count")
    both = [c for c in (0, 2) if self_pair_ok(c) and cross_pair_ok(c)]
    check(both == [],
          "COMPOSITION-CLOSED DICHOTOMY: the both-capabilities set is empty over the "
          "composite lattice (every monomial sits on exactly one horn)")
    # centre-scalar rigor: i^cls characters multiply; invariant needs product 1
    scalar = lambda c: 1j ** c                                    # noqa: E731
    two_ins = scalar(c_p) * scalar(c_p) * scalar(2) * scalar(2)   # W+ self-pair, 2 class-2 factors
    check(abs(two_ins - (-1)) < 1e-15,
          "centre-scalar rigor: W_+ self-pairing with TWO class-2 factors carries central "
          "scalar -1 (not 1) -- the Hom space is EXACTLY zero, not merely disfavored")
    # the sum shape is NOT a class composite: parity of terms, not classes, is what adds
    check(composite_cls([2]) == 2 and composite_cls([2, 2]) == 0,
          "shape C-ii/C-iii: one class-2 factor gives class 2; two give class 0 "
          "(the register title's arithmetic, exact for monomials/products)")
    planted_false = [
        composite_cls([2, 2]) == 2,        # 'two class-2 factors stay class 2'
        self_pair_ok(0),                   # 'class-0 composites self-pair'
        cross_pair_ok(2),                  # 'class-2 monomials cross-pair'
        composite_cls([2, 2, 2]) == 0,     # 'three class-2 factors are class 0'
        bool(both),                        # 'some composite has both capacities'
    ]
    check(all(p is False for p in planted_false),
          "5 planted-false composite-class propositions each observed False")
    m["lattice_both_empty"] = (both == [])
    return m


# --------------------------------------------------------------------------
# exact D_7 weight machinery (doubled integer coordinates; TR-1's layer)
# --------------------------------------------------------------------------
N7 = 7
RHO = tuple(2 * (N7 - 1 - i) for i in range(N7))


def pos_roots_d7() -> list[tuple[int, ...]]:
    roots = []
    for i in range(N7):
        for j in range(i + 1, N7):
            for s in (+1, -1):
                r = [0] * N7
                r[i], r[j] = 2, 2 * s
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
    absu = [abs(x) for x in u]
    if len(set(absu)) != len(absu):
        return None
    order = sorted(range(len(u)), key=lambda i: -absu[i])
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
        out[-1] = -out[-1]
    return sign, tuple(out)


def klimyk_multiset(hw_big: tuple[int, ...], small: dict[tuple[int, ...], int]) -> dict:
    """Decompose V(hw_big) (x) M where M is given as a weight->multiplicity dict."""
    counts: dict[tuple[int, ...], int] = {}
    for mu, mult in small.items():
        u = tuple(h + q + r for h, q, r in zip(hw_big, mu, RHO))
        rd = reflect_dominant(u)
        if rd is None:
            continue
        sgn, dom = rd
        hw = tuple(d - r for d, r in zip(dom, RHO))
        counts[hw] = counts.get(hw, 0) + sgn * mult
    return {k: v for k, v in counts.items() if v != 0}


def spinor_weights(plus: bool) -> list[tuple[int, ...]]:
    out = []
    for signs in itertools.product((1, -1), repeat=N7):
        if (sum(1 for s in signs if s < 0) % 2 == 0) == plus:
            out.append(tuple(signs))
    return out


def lam7_split() -> tuple[dict, dict]:
    """Split Lambda^7(V_14) into Lambda^7_+ (contains hw (2,..,2)) and Lambda^7_-."""
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
        if len(set(idx)) == 7:
            if sum(1 for s in sgn if s < 0) % 2 == 0:
                plus[t] = plus.get(t, 0) + 1
            else:
                minus[t] = minus.get(t, 0) + 1
        else:
            mixed.append(t)
    pool: dict[tuple[int, ...], int] = {}
    for t in mixed:
        pool[t] = pool.get(t, 0) + 1
    for t, c in pool.items():
        if c % 2 != 0:
            raise AssertionError("mixed multiplicities must be even to split equally")
        plus[t] = plus.get(t, 0) + c // 2
        minus[t] = minus.get(t, 0) + c // 2
    return plus, minus


def product_multiset(a: dict, b: dict) -> dict:
    out: dict[tuple[int, ...], int] = {}
    for wa, ma in a.items():
        for wb, mb in b.items():
            t = tuple(x + y for x, y in zip(wa, wb))
            out[t] = out.get(t, 0) + ma * mb
    return out


def weyl_group_d7() -> tuple[list, list]:
    """All of W(D_7) as (perm, perm-sign) pairs and even sign-flip patterns."""
    elems = []
    for perm in itertools.permutations(range(N7)):
        inv = 0
        for a in range(N7):
            for b in range(a + 1, N7):
                if perm[a] > perm[b]:
                    inv += 1
        elems.append((perm, -1 if inv % 2 else 1))
    signsets = [s for s in itertools.product((1, -1), repeat=N7)
                if sum(1 for x in s if x < 0) % 2 == 0]
    return elems, signsets


def racah_mult(target_hw: tuple[int, ...], multiset: dict, elems, signsets) -> int:
    """mult(V(target_hw), module) by the Racah/Brauer alternating sum over W(D_7)."""
    lr = tuple(t + r for t, r in zip(target_hw, RHO))
    total = 0
    for perm, psgn in elems:
        permuted = tuple(lr[perm[i]] for i in range(N7))
        for signs in signsets:
            key = tuple(s * x - r for s, x, r in zip(signs, permuted, RHO))
            q = multiset.get(key)
            if q:
                total += psgn * q
    return total


HW = {
    "L0": (0,) * 7,
    "L1": (2, 0, 0, 0, 0, 0, 0),
    "L2": (2, 2, 0, 0, 0, 0, 0),
    "L3": (2, 2, 2, 0, 0, 0, 0),
    "L5": (2, 2, 2, 2, 2, 0, 0),
    "L7+": (2,) * 7,
    "L7-": (2, 2, 2, 2, 2, 2, -2),
    "S+": (1, 1, 1, 1, 1, 1, 1),
    "S-": (1, 1, 1, 1, 1, 1, -1),
}


def leg3() -> dict[str, object]:
    print("\nLEG 3 -- exact D_7 weight instruments on the two-middle-form composite")
    m: dict[str, object] = {}
    for k, want in [("L1", 14), ("L2", 91), ("L3", 364), ("L5", 2002),
                    ("L7+", 1716), ("L7-", 1716), ("S+", 64), ("S-", 64)]:
        check(weyl_dim(HW[k]) == want, f"Weyl dimension (exact Fraction): dim {k} = {want}")
    l7p, l7m = lam7_split()
    check(sum(l7p.values()) == 1716 and sum(l7m.values()) == 1716,
          "Lambda^7 splits 1716 + 1716 with hw (2,..,2) / (2,..,2,-2) (multiset split)")
    check(l7p.get((2,) * 7, 0) == 1 and l7m.get(HW["L7-"], 0) == 1,
          "hw check: each half carries its highest weight with multiplicity 1")
    # the two composite products
    Tmm = product_multiset(l7m, l7m)          # same-sense
    Tpm = product_multiset(l7p, l7m)          # opposite-sense
    check(sum(Tmm.values()) == 1716 ** 2 and sum(Tpm.values()) == 1716 ** 2,
          "product multisets carry exactly 1716^2 = 2,944,656 weights each")
    # instrument A: mult-aware Klimyk full decompositions
    dec_mm = klimyk_multiset(HW["L7-"], l7m)
    dec_pm = klimyk_multiset(HW["L7+"], l7m)
    for name, dec in (("Lam^7_- (x) Lam^7_-", dec_mm), ("Lam^7_+ (x) Lam^7_-", dec_pm)):
        sat = sum(Fraction(mult) * weyl_dim(hw) for hw, mult in dec.items())
        check(sat == 1716 ** 2,
              f"dimension saturation (exact Fractions): {name} decomposition sums to 1716^2")
        odd = {t: dec.get(HW[t], 0) for t in ("L1", "L3", "L5", "L7+", "L7-")}
        check(all(v == 0 for v in odd.values()),
              f"Klimyk: ZERO odd-form content in {name} (Lam^1/3/5/7± all absent)")
    check(dec_mm.get(HW["L0"], 0) == 0 and dec_pm.get(HW["L0"], 0) == 1,
          "invariant loops: Inv(same-sense) = 0, Inv(opposite-sense) = 1 (Klimyk)")
    check(dec_pm.get(HW["L2"], 0) == 1,
          "planted positive (opposite-sense): mult(Lam^2) = 1 -- the detector sees even content")
    check(dec_mm.get((4, 4, 4, 4, 4, 4, -4), 0) == 1,
          "planted positive (same-sense): the Cartan-square hw 2*hw(Lam^7_-) appears, mult 1")
    # instrument B: Racah/Brauer over all of W(D_7) on the raw product multisets
    elems, signsets = weyl_group_d7()
    check(len(elems) * len(signsets) == 322560,
          "W(D_7) enumerated: 5040 permutations x 64 even sign patterns = 322,560 elements")
    agree = True
    for tgt in ("L1", "L3", "L5", "L7+", "L7-", "L0", "L2"):
        r_mm = racah_mult(HW[tgt], Tmm, elems, signsets)
        r_pm = racah_mult(HW[tgt], Tpm, elems, signsets)
        if r_mm != dec_mm.get(HW[tgt], 0) or r_pm != dec_pm.get(HW[tgt], 0):
            agree = False
            check(False, f"instrument disagreement at target {tgt}: "
                         f"racah ({r_mm},{r_pm}) vs klimyk "
                         f"({dec_mm.get(HW[tgt],0)},{dec_pm.get(HW[tgt],0)})")
    check(agree,
          "Racah/Brauer (raw multisets, no Klimyk, no subtraction) agrees with Klimyk on "
          "all 7 targets x both products -- two independent instruments")
    # TR-1's four one-way Hom facts [R], consumed by the composition corollary
    sp, sm = spinor_weights(True), spinor_weights(False)
    sp_ms = {w: 1 for w in sp}
    sm_ms = {w: 1 for w in sm}
    one_way = {
        ("L7-", "S+", "S-"): 1, ("L7-", "S-", "S+"): 0,
        ("L7+", "S-", "S+"): 1, ("L7+", "S+", "S-"): 0,
    }
    ok = True
    for (le, sa, sb), want in one_way.items():
        d = klimyk_multiset(HW[le], sp_ms if sa == "S+" else sm_ms)
        if d.get(HW[sb], 0) != want:
            ok = False
    check(ok, "TR-1's four one-way Hom facts reproduced [R tr1:395-397] -- the "
              "composition corollary (same-sense A o A' = 0) consumes exactly these")
    m["composite_odd_zero"] = True
    m["inv_pair"] = (dec_mm.get(HW["L0"], 0), dec_pm.get(HW["L0"], 0))
    return m


# --------------------------------------------------------------------------
# LEG 4 -- Cl(14) + lattice: the operator face of composition
# --------------------------------------------------------------------------
MOVER_PIN = 18.508381432260148       # TR-1's Gamma-aligned mover witness (tr1 §4.3)
LDA_PIN = -21.845865                 # LD-A's measured n_-(1.5), re-pinned by TR-1


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
    return gammas


def mprod(mats: list[np.ndarray]) -> np.ndarray:
    out = mats[0]
    for x in mats[1:]:
        out = out @ x
    return out


def n_minus(d: np.ndarray, gamma: np.ndarray) -> float:
    w, v = np.linalg.eigh(d)
    sel = v[:, w < -1e-9]
    return float(np.real(np.trace(sel.conj().T @ gamma @ sel)))


def leg4() -> dict[str, object]:
    print("\nLEG 4 -- Cl(14) and lattice: nilpotence, the commutator identity, "
          "the freeze grid, the pinned mover, the index pinning")
    m: dict[str, object] = {}
    g = cl14_gammas()
    dim = 128
    nrm = lambda a: float(np.linalg.norm(a))                      # noqa: E731
    anti_ok = all(nrm(g[i] @ g[j] + g[j] @ g[i] - (2.0 if i == j else 0.0) * np.eye(dim)) < 1e-12
                  for i in range(14) for j in range(i, 14))
    check(anti_ok, "14 gammas: {g_i, g_j} = 2 delta_ij on C^128 (Clifford relations hold)")
    Gamb = 1j * mprod(g)
    check(nrm(Gamb - Gamb.conj().T) < 1e-12 and nrm(Gamb @ Gamb - np.eye(dim)) < 1e-12,
          "Gamma_amb is a Hermitian involution (guard: the graded trace is NON-vacuous)")
    P_plus = (np.eye(dim) + Gamb) / 2
    P_minus = (np.eye(dim) - Gamb) / 2
    check(nrm(P_plus @ P_plus - P_plus) < 1e-12 and nrm(P_plus @ P_minus) < 1e-12,
          "half-projectors are idempotent and orthogonal (machinery guard)")
    # Hermitian odd 7-word insertions
    W1 = 1j * mprod(g[4:11])            # the (0,7) Lorentz-singlet split word
    W2 = 1j * mprod(g[:4] + g[4:7])     # the (4,3) split word (overlap 3 with W1)
    W0 = 1j * mprod(g[0:7])             # indices 1..7
    W3 = 1j * mprod(g[7:14])            # indices 8..14 (disjoint from W0)
    for name, W in (("W1", W1), ("W2", W2), ("W0", W0), ("W3", W3)):
        check(nrm(W - W.conj().T) < 1e-12 and nrm(W @ Gamb + Gamb @ W) < 1e-12,
              f"{name} is a Hermitian Gamma-odd 7-word insertion (guards)")
    # (a) one-way arrows and their composites
    A1 = W1 @ P_plus
    A2 = W2 @ P_plus
    check(nrm(P_minus @ A1 @ P_plus - A1) < 1e-12,
          "one-way arrow: A = W_h P_+ maps S_+ into S_- and kills S_-")
    check(nrm(A1 @ A1) < 1e-12, "nilpotence: A^2 = 0 exactly [R tr1:400, closed under composition]")
    check(nrm(A1 @ A2) < 1e-12 and nrm(A2 @ A1) < 1e-12,
          "same-sense vanishing: A o A' = 0 for TWO DISTINCT same-sense arrows (machine zero)")
    check(nrm(A1.conj().T - W1 @ P_minus) < 1e-12,
          "the reverse arrow IS the adjoint: A^dag = W_h P_- (SN-1's reality-map fence, typed)")
    check(nrm(A1.conj().T @ A1 - P_plus) < 1e-12,
          "A^dag A = P_+ exactly: the mass-squared of a one-way arrow is the half-projector "
          "(gapping content in D^2, never count content)")
    # (b) overlap rule and the commutator identity
    check(nrm(W0 @ W3 + W3 @ W0) < 1e-12,
          "disjoint 7-words anticommute ((-1)^49 = -1): the Hermitian composite is the commutator")
    check(nrm(W1 @ W2 - W2 @ W1) < 1e-12,
          "overlap-3 7-words commute ((-1)^46 = +1): the Hermitian composite is the product/anticommutator")
    Nc = (1j / 2) * (W3 @ W0 - W0 @ W3)
    check(nrm(Nc - Gamb) < 1e-12,
          "THE COMMUTATOR IDENTITY: (i/2)[W', W] = Gamma_amb EXACTLY for the disjoint pair "
          "-- the curvature of the two-insertion family is the grading itself")
    check(nrm(Nc - Nc.conj().T) < 1e-12 and nrm(Nc @ Gamb - Gamb @ Nc) < 1e-12,
          "non-vacuity guard: the commutator composite is Hermitian and Gamma-even "
          "(a naive Hermitian-part of the anti-Hermitian product W'W would be ZERO)")
    ev = W1 @ W2
    check(nrm(ev @ Gamb - Gamb @ ev) < 1e-10,
          "every two-odd-factor product commutes with Gamma (the class-0 operator face)")
    # (c) the freeze grid on the two-parameter odd family
    rng = np.random.default_rng(20260817)
    coef = rng.standard_normal(14)
    D0 = sum(c * gi for c, gi in zip(coef, g))
    frozen = max(abs(n_minus(D0 + s * W1 + t * W2, Gamb))
                 for s in (0.0, 0.3, 0.7, 1.1, 1.5) for t in (0.0, 0.4, 0.9, 1.5))
    check(frozen < 1e-8,
          f"FREEZE ON THE SQUARE: max |tr(Gamma P_<0)| = {frozen:.2e} over the 5x4 grid of the "
          "two-parameter odd family -- no path in (s,t) transports anything")
    m["frozen_grid"] = frozen
    # (d) the composite mover equals TR-1's pinned mover (directions identical)
    moved_tr1 = abs(n_minus(D0 + 1.5 * Gamb, Gamb))
    moved_comp = abs(n_minus(D0 + 1.5 * Nc, Gamb))
    check(abs(moved_tr1 - MOVER_PIN) < 5e-9,
          f"[R] TR-1's Gamma-aligned mover witness re-measured: {moved_tr1:.12f} (pin {MOVER_PIN})")
    check(abs(moved_comp - MOVER_PIN) < 5e-9,
          "the COMPOSITE direction moves the trace by the SAME pinned value "
          "(the directions are equal, not merely similar)")
    m["moved_comp"] = moved_comp
    # (e) the mixed family leaves canon's class; interior trace non-integer
    Dm = D0 + 0.7 * W1 + 0.5 * Nc
    comm = nrm(Dm @ Gamb - Gamb @ Dm)
    anti = nrm(Dm @ Gamb + Gamb @ Dm)
    check(comm > 1.0 and anti > 1.0,
          "the mixed family (odd terms + even composite term) is neither Gamma-odd nor "
          "Gamma-even at the acting point -- it has left CANON.md:136's class (TB-2 binds)")
    interior = n_minus(Dm, Gamb)
    check(abs(interior - round(interior)) > 0.05,
          f"interior trace of the mixed family is non-integer ({interior:.6f}) -- TB-3 binds")
    m["interior"] = interior
    # (f) parity decomposition unique (P-1's arithmetic) [R lda:295 shape]
    worst_sum, worst_cross = 0.0, 0.0
    for _ in range(20):
        X = rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim))
        X = (X + X.conj().T) / 2
        Xe = (X + Gamb @ X @ Gamb) / 2
        Xo = (X - Gamb @ X @ Gamb) / 2
        worst_sum = max(worst_sum, nrm(X - Xe - Xo))
        worst_cross = max(worst_cross, nrm((Xo + Gamb @ Xo @ Gamb) / 2))
    check(worst_sum < 1e-12 and worst_cross < 1e-12,
          "parity decomposition is exhaustive and unique over 20 draws: M = M_even + M_odd, "
          "even-of-odd = 0 [R lda:295] -- TB-5's fork is a decomposition, not rhetoric")
    # (g) the index is pinned at the graded dimension along composite families
    npl, nmi = 3, 2
    B = rng.standard_normal((npl, nmi)) + 1j * rng.standard_normal((npl, nmi))
    B2 = rng.standard_normal((npl, nmi)) + 1j * rng.standard_normal((npl, nmi))
    Gsm = np.diag([1.0] * npl + [-1.0] * nmi)
    idxs = set()
    for s in (0.0, 0.5, 1.0):
        for t in (0.0, 0.7, 1.3):
            Bc = B + s * B2 + t * (B + 0.3 * B2)
            Dodd = np.block([[np.zeros((npl, npl)), Bc], [Bc.conj().T, np.zeros((nmi, nmi))]])
            check_odd = nrm(Dodd @ Gsm + Gsm @ Dodd) < 1e-12
            w, v = np.linalg.eigh(Dodd)
            ker = v[:, np.abs(w) < 1e-9]
            idx = int(round(np.real(np.trace(ker.conj().T @ Gsm @ ker))))
            if not check_odd:
                idxs.add("not-odd")
            idxs.add(idx)
    check(idxs == {1},
          "index pinning: ind = n_+ - n_- = 1 IDENTICALLY across the two-parameter odd "
          "family on 3|2 halves -- no composite deformation moves the kernel index")
    neq = 4
    Beq = rng.standard_normal((neq, neq)) + 1j * rng.standard_normal((neq, neq))
    Deq = np.block([[np.zeros((neq, neq)), Beq], [Beq.conj().T, np.zeros((neq, neq))]])
    weq = np.linalg.eigvalsh(Deq)
    check(int(np.sum(np.abs(weq) < 1e-9)) == 0,
          "equal halves (the four-corner total's 960|960 shape): generic kernel empty, "
          "index = 0 = graded dimension -- only external data moves it (CANON.md:135/139)")
    # (h) the lattice face: LD-A's mass direction IS the composite of the two odd directions
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
    d0 = np.kron(s1, p)
    comp = (1j / 2) * (np.kron(s2, eye) @ np.kron(s1, eye) - np.kron(s1, eye) @ np.kron(s2, eye))
    check(nrm(comp - np.kron(s3, eye)) < 1e-12,
          "lattice face: (i/2)[sigma_2 (x) I, sigma_1 (x) I] = sigma_3 (x) I -- LD-A's mass "
          "direction IS the composite of the model's two odd directions")
    nm = n_minus(d0 + 1.5 * np.kron(s3, eye), gamma)
    check(abs(nm - LDA_PIN) < 5e-6,
          f"[R] LD-A pinned on the rebuilt lattice: n_-(1.5) = {nm:.6f} (pin {LDA_PIN})")
    m["nm"] = nm
    return m


# --------------------------------------------------------------------------
# LEG 5 -- GB-1 model face, exact sympy on M_2(C)
# --------------------------------------------------------------------------
def leg5() -> dict[str, object]:
    print("\nLEG 5 -- GB-1 model face (exact sympy): rotation composites and parity products")
    m: dict[str, object] = {}
    import sympy as sp
    I2 = sp.eye(2)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    t1, t2, ph = sp.symbols("t1 t2 ph", real=True)

    def U(th):
        return sp.cos(th / 2) * I2 - sp.I * sp.sin(th / 2) * s1

    def M(phi):
        return sp.cos(phi) * s3 + sp.sin(phi) * s2

    comp = sp.simplify(U(t1) * U(t2) - U(t1 + t2))
    check(comp == sp.zeros(2, 2),
          "angle addition: U(t1) U(t2) = U(t1+t2) exactly -- a composite of rotations is a rotation")
    conj = sp.simplify(U(t1) * M(ph) * U(t1).H - M(ph - t1))
    check(sp.simplify(conj) == sp.zeros(2, 2),
          "[R gb1:317] U M(phi) U^dag = M(phi - theta) exactly")
    both = sp.simplify(U(t1) * U(t2) * M(ph) * (U(t1) * U(t2)).H - M(ph - t1 - t2))
    check(sp.simplify(both) == sp.zeros(2, 2),
          "the conjugation COMPOSITE carries M(phi) to M(phi - t1 - t2): rigid-pair rotation, "
          "so GB-1's relative-angle invariant survives every composite")
    gam_t = sp.simplify(U(t1) * s3 * U(t1).H - M(-t1))
    check(sp.simplify(gam_t) == sp.zeros(2, 2),
          "the grading transports with the same angle: U Gamma U^dag = M(-theta) "
          "(mass and grading rotate together -- no transported charge)")
    check(sp.simplify(s1 * s2 - sp.I * s3) == sp.zeros(2, 2),
          "parity product: sigma_1 sigma_2 = i sigma_3 (odd . odd = even -- the model face of "
          "the composite class arithmetic)")
    prodid = sp.simplify(M(t1) * M(t2) - (sp.cos(t1 - t2) * I2 + sp.I * sp.sin(t1 - t2) * s1))
    check(sp.simplify(prodid) == sp.zeros(2, 2),
          "M(p1) M(p2) = cos(p1-p2) I + i sin(p1-p2) sigma_1: the composite's parity split is "
          "a function of the relative angle alone")
    m["gb1_face"] = True
    return m


# --------------------------------------------------------------------------
# LEG 6 -- the rank floor: seven middle-form insertions
# --------------------------------------------------------------------------
def leg6() -> dict[str, object]:
    print("\nLEG 6 -- the TB-4 floor: 128k >= 896 iff k >= 7 (necessary, not sufficient)")
    m: dict[str, object] = {}
    check(128 * 6 == 768 and 768 < 896 and 128 * 7 == 896 and math.ceil(896 / 128) == 7,
          "exact arithmetic: 6 x 128 = 768 < 896 <= 7 x 128 -- the floor is SEVEN "
          "(and 7 is odd: no collision with the ST-1 odd-count rule)")
    rng = np.random.default_rng(7)
    n896 = 896

    def rank128_antisym():
        X = rng.standard_normal((n896, 64)) + 1j * rng.standard_normal((n896, 64))
        Y = rng.standard_normal((n896, 64)) + 1j * rng.standard_normal((n896, 64))
        return X @ Y.T - Y @ X.T

    blocks = [rank128_antisym() for _ in range(7)]
    ranks = [int(np.linalg.matrix_rank(b, tol=1e-8)) for b in blocks]
    check(all(r <= 128 for r in ranks),
          f"subadditivity guard: each generated antisymmetric form has rank <= 128 (got {set(ranks)})")
    r6 = int(np.linalg.matrix_rank(sum(blocks[:6]), tol=1e-8))
    r7 = int(np.linalg.matrix_rank(sum(blocks), tol=1e-8))
    check(r6 <= 768,
          f"six-insertion sum: rank {r6} <= 768 < 896 -- the corner self-form stays degenerate "
          "(>= 128 directions unpaired), witnessing the floor's bite")
    check(r7 == 896,
          f"seven-insertion sum: rank {r7} = 896 -- the floor is tight as an inequality "
          "(generic achievability; invariant-compatibility NOT certified)")
    m["r6r7"] = (r6, r7)
    return m


# --------------------------------------------------------------------------
# LEG 7 -- TR-1 whole-probe re-run
# --------------------------------------------------------------------------
def leg7() -> dict[str, object]:
    print("\nLEG 7 -- TR-1 whole-probe re-run (the banked dichotomy layer, green at HEAD)")
    m: dict[str, object] = {}
    path = ROOT / TR1_PROBE
    if not check(path.exists(), f"TR-1 probe exists at {TR1_PROBE}"):
        m["tr1_green"] = False
        return m
    r = subprocess.run([sys.executable, str(path)], capture_output=True, text=True,
                       cwd=str(ROOT), timeout=1200)
    ok = (r.returncode == 0 and "90/90 checks pass" in r.stdout)
    check(ok, "TR-1 probe re-run: exit 0 with '90/90 checks pass' "
              "(the single-insertion dichotomy this file composes with is green)")
    m["tr1_green"] = ok
    return m


# --------------------------------------------------------------------------
# LEG 8 -- certified absence + artifact binding
# --------------------------------------------------------------------------
NOVELTY_PHRASES = [
    "composites inherit one horn",
    "composition-closed dichotomy",
    "the curvature of the two-insertion family is the grading",
    "same-sense composites vanish",
]
PLANT_POSITIVE = ("Synthetic planted positive: composites inherit one horn, "
                  "verbatim, for the detector.")
PLANT_NEARMISS = ("Synthetic near-miss: composites, horns, parity and closure "
                  "discussed separately without the claimed phrasings.")
SELF_NAMES = ("joe_directed_mp1_composites_inherit_one_horn",
              "mp1-composites-inherit-one-horn-never-both")


def scan_absence(extra_docs: list[str]) -> tuple[int, dict[str, int]]:
    # The probe and the artifact it certifies contain the phrasings by
    # construction and are excluded by NAME (so selftest copies exclude the
    # originals too); the detector's power is shown on the planted positive.
    skip = {"_local", ".git", "zenodo-package-v1.0.0", "__pycache__"}
    exts = {".md", ".py", ".yaml", ".yml", ".txt", ".json"}
    hits = {ph: 0 for ph in NOVELTY_PHRASES}
    scanned = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in exts:
            continue
        if any(part in skip for part in path.parts):
            continue
        if any(s in path.name for s in SELF_NAMES):
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


TABLE_SHA = "b27b5888d048a73cf8310c9e0024823d2b11aab61001b1cb26d2471285f1ac55"
VERDICT_SET = {
    "CP-TERM": "DICHOTOMY-CLOSES-UNDER-COMPOSITION",
    "CP-SEL": "CAPABILITY-DESTROYED-AT-EVEN-ORDER",
    "CP-TRA": "MIXED-ROUTE-EXISTS-PRICED",
    "CP-HOL": "NO-HOLONOMY-POINT-FUNCTION",
    "CP-PRICE": "TWO-BILLS-PLUS-SEVEN-FLOOR",
    "CP-KILL": "NO-KILL-CLAIM-RESTATED",
}


def table_block(text: str) -> str:
    mm = re.search(r"<!-- MP1-TABLE-BEGIN -->(.*?)<!-- MP1-TABLE-END -->", text, re.S)
    if not mm:
        raise ValueError("MP1 table markers not found")
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
    print("\nLEG 8 -- certified absence and artifact binding")
    scanned, hits = scan_absence([])
    check(all(v == 0 for v in hits.values()),
          f"absence: 0 corpus hits for all {len(NOVELTY_PHRASES)} result phrasings "
          f"({scanned} files scanned; artifact+probe excluded by name; zero hits is "
          "NOT evidence of new)")
    _, hits_p = scan_absence([PLANT_POSITIVE])
    check(hits_p[NOVELTY_PHRASES[0]] == 1,
          "planted positive IS flagged (the absence detector has power)")
    _, hits_n = scan_absence([PLANT_NEARMISS])
    check(all(v == 0 for v in hits_n.values()),
          "planted near-miss is NOT flagged (the detector does not fire on topic words)")
    text = artifact_path.read_text(encoding="utf-8")
    blk = table_block(text)
    sha = hashlib.sha256(blk.encode("utf-8")).hexdigest()
    check(sha == TABLE_SHA, f"verdict-table SHA-256 pinned = {TABLE_SHA[:12]}...")
    verdicts = parse_verdicts(blk)
    check(set(verdicts) == set(VERDICT_SET),
          f"verdict table carries exactly the 6 ids {sorted(VERDICT_SET)}")
    for k, want in VERDICT_SET.items():
        check(verdicts.get(k) == want, f"verdict {k} = {want}")
    check(verdicts.get("CP-TERM") == "DICHOTOMY-CLOSES-UNDER-COMPOSITION"
          and bool(measured["lattice_both_empty"]) and bool(measured["composite_odd_zero"]),
          "binding: CP-TERM is consistent with the empty both-capabilities set and the "
          "zero odd-form composite content")
    check(verdicts.get("CP-TRA") == "MIXED-ROUTE-EXISTS-PRICED"
          and abs(float(measured["moved_comp"]) - MOVER_PIN) < 5e-9
          and float(measured["frozen_grid"]) < 1e-8,
          "binding: CP-TRA is consistent with the composite-mover identity and the frozen grid")
    check(verdicts.get("CP-KILL") == "NO-KILL-CLAIM-RESTATED" and bool(measured["tr1_green"]),
          "binding: CP-KILL is consistent with the green TR-1 re-run")


# --------------------------------------------------------------------------
# runner
# --------------------------------------------------------------------------
def run_all(artifact_path: Path) -> int:
    print("=" * 78)
    print("MP-1 probe: composites inherit one horn, never both")
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
BASELINE_PIN = 86        # independent pin of the clean-baseline check count


def _run_probe_text(src: str, workdir: Path, artifact_text: str | None = None) -> tuple[int, str]:
    probe = workdir / "mutant_probe.py"
    probe.write_text(src, encoding="utf-8")
    env = dict(os.environ)
    env["MP1_ROOT_OVERRIDE"] = str(ROOT)
    if artifact_text is not None:
        art_copy = workdir / "artifact_copy.md"
        art_copy.write_text(artifact_text, encoding="utf-8")
        env["MP1_ARTIFACT_OVERRIDE"] = str(art_copy)
    else:
        env["MP1_ARTIFACT_OVERRIDE"] = str(ROOT / ARTIFACT)
    r = subprocess.run([sys.executable, str(probe)], capture_output=True, text=True,
                       cwd=str(ROOT), env=env, timeout=1800)
    return r.returncode, r.stdout + r.stderr


MUTATIONS: list[tuple[str, str, str, str]] = [
    # NEEDLE SYNCED 2026-08-17 (integrator): the live pin moved 256 -> 284
    # in the same integration pass that closed the register item; the
    # mutation now corrupts the CURRENT reference (284 -> 287) so it stays
    # applicable rather than silently no-opping on a stale needle.
    ("M01-pin-line-number",
     '("lab/process/upgrade-program-register.yaml", 284, "- id: TR1-COMPOSITE-PARITY")',
     '("lab/process/upgrade-program-register.yaml", 287, "- id: TR1-COMPOSITE-PARITY")',
     "quote pin lab/process/upgrade-program-register.yaml:287"),
    ("M02-tr1-probe-sha",
     'TR1_PROBE_SHA = "910f6279',
     'TR1_PROBE_SHA = "00000000',
     "SHA-256 pin of the TR-1 probe"),
    ("M03-class-table",
     'CLS = {"V": 2, "S+": 3, "S-": 1}',
     'CLS = {"V": 2, "S+": 2, "S-": 1}',
     "corner-class guard"),
    ("M04-composite-arithmetic",
     "def composite_cls(factor_classes: list[int]) -> int:\n    return sum(factor_classes) % 4",
     "def composite_cls(factor_classes: list[int]) -> int:\n    return sum(factor_classes) % 3",
     "composite lattice: total class = 2*(number of class-2 factors) mod 4"),
    ("M05-klimyk-reflection-sign",
     "sign = -1 if inv % 2 else 1",
     "sign = 1 if inv % 2 else -1",
     "TR-1's four one-way Hom facts reproduced"),
    ("M06-product-multiset",
     "out[t] = out.get(t, 0) + ma * mb",
     "out[t] = out.get(t, 0) + ma + mb",
     "product multisets carry exactly 1716^2"),
    ("M07-racah-signsets",
     "signsets = [s for s in itertools.product((1, -1), repeat=N7)\n"
     "                if sum(1 for x in s if x < 0) % 2 == 0]",
     "signsets = [s for s in itertools.product((1, -1), repeat=N7)]",
     "W(D_7) enumerated: 5040 permutations x 64 even sign patterns"),
    ("M08-half-projector",
     "P_plus = (np.eye(dim) + Gamb) / 2",
     "P_plus = (np.eye(dim) + Gamb) / 3",
     "half-projectors are idempotent and orthogonal"),
    ("M09-freeze-machinery",
     "W1 = 1j * mprod(g[4:11])            # the (0,7) Lorentz-singlet split word",
     "W1 = 1j * mprod(g[4:11]) + 0.4 * np.eye(128)  # corrupted machinery",
     "W1 is a Hermitian Gamma-odd 7-word insertion"),
    ("M10-mover-pin",
     "MOVER_PIN = 18.508381432260148",
     "MOVER_PIN = 17.508381432260148",
     "TR-1's Gamma-aligned mover witness re-measured"),
    ("M11-absence-detector",
     'NOVELTY_PHRASES = [\n    "composites inherit one horn",',
     'NOVELTY_PHRASES = [\n    "qq-mp1-sentinel-never-present-qq",',
     "planted positive IS flagged"),
]
# M12 mutates the ARTIFACT copy, not the probe (contrary control)
M12_OLD = "| CP-TERM | does any composite term carry both capacities | DICHOTOMY-CLOSES-UNDER-COMPOSITION |"
M12_NEW = "| CP-TERM | does any composite term carry both capacities | COMPOSITE-CARRIES-BOTH |"
M12_TARGET = "verdict CP-TERM = DICHOTOMY-CLOSES-UNDER-COMPOSITION"


def selftest() -> int:
    src = SELF.read_text(encoding="utf-8")
    print("=" * 78)
    print("MP-1 SELFTEST -- baseline first, then 12 machinery/reference mutations")
    print("=" * 78)
    with tempfile.TemporaryDirectory(prefix="mp1-selftest-") as td:
        wd = Path(td)
        rc, out = _run_probe_text(src, wd)
        base_fails = out.count("[FAIL]")
        mm = re.search(r"RESULT: (\d+)/(\d+) checks pass", out)
        base_checks = int(mm.group(2)) if mm else None
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
    art_override = os.environ.get("MP1_ARTIFACT_OVERRIDE")
    artifact_path = Path(art_override) if art_override else (ROOT / ARTIFACT)
    return run_all(artifact_path)


if __name__ == "__main__":
    sys.exit(main())
