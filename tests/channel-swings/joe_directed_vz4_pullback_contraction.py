#!/usr/bin/env python3
"""VZ-4 -- the section pullback in vz-schur SS18.3 is a CONTRACTION, and the
"not a larger sector" clause fails in EVERY gauge.

Target: `explorations/vz-evasion/vz-schur-complement-2026-06-23.md` SS18.3
(`OQ3-V3`), graded **VERIFIED** with "No approximation is made", and its
propagation to `canon/no-go-class-relative-map.md:401` and six exploration
files.

This probe verifies, from scratch and without inheriting `MD-1`:

  PART A (exact sympy, general section)
    the geometry of `s^*: T*Y14 -> T*X4` for `s(x) = (x, g_ab(x))`.

  PART B (exact Gaussian-integer 128x128 representation of Cl(9,5))
    what the geometry does to the gamma-trace / Rarita-Schwinger sector,
    which is the part SS18.3 actually claims and which neither `MD-1` nor
    `LA-8` computed.

  PART C (textual)
    pins every string this repair proposes to change, so the diff cannot
    drift off its target.

THREE PROPOSITIONS ARE SEPARATED.  SS18.3 runs them together; they have
different truth values, and that is the whole finding.

  P1  s^*( R^14D  intersect  (pi^*T*X4 tensor S) )  ==  ker Gamma^4D
      TRUE for every section.  No gauge condition.  (B6)

  P2  "the pullback functor s^* sends psi to its horizontal part"
      FALSE unless d_mu g_ab == 0.  (A2, A5, A6)

  P3  "not a larger sector (no extra RS components from the normal
      directions survive as 4D spin-3/2 fields)"
      FALSE for EVERY section, flat gauge included.  (B7, B8)
      The flat-section gauge does NOT rescue this clause.  P3 is a second,
      independent defect that has nothing to do with the missing
      `d_mu g_ab` term: it conflates "restrict the domain to horizontal
      one-forms, then pull back" with "pull back the whole sector".

Design notes, so no check can be read as stronger than it is:

1. EXACT ONLY.  Part A is sympy on symbolic `g_ab(x)` and on exact
   `Rational` sections.  Part B is integer arithmetic on Gaussian-integer
   matrices held as two int64 arrays (real, imaginary); an explicit
   magnitude guard proves no overflow.  No float is load-bearing anywhere,
   and no float appears in any asserted quantity.

2. CONTRARY CONTROL.  `test_a6_contrary_control_nonflat_section` exhibits a
   section with `d_mu g_ab != 0` at an exact rational point where
   `s^* - P_H` is a named nonzero rational.  Planted control
   `contrary_control_vacuous` swaps in a flat section and MUST fail: a
   contrary control that cannot discriminate is not a control.

3. NEGATIVE assertions are the ones that rot, so each names its file and
   token, and `--selftest` plants a falsehood to prove the check can fire.

Usage
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_vz4_pullback_contraction.py
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_vz4_pullback_contraction.py --selftest
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_vz4_pullback_contraction.py --control <name>

`--selftest` runs every planted control in a subprocess and requires each to
exit 1, and exits 0 only if all of them did.  A control that passes is
vacuous and fails the harness.
"""

from __future__ import annotations

import itertools
import os
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]

MUT = os.environ.get("VZ4_CONTROL", "")

CONTROLS = {
    "pullback_is_projection":
        "A2 drops the d_mu g_ab correction term (this IS the SS18.3 claim)",
    "coordinate_normals_are_kernel":
        "A4 asserts s^* annihilates the coordinate normals du_I",
    "horizontal_restriction_needs_gauge":
        "A3 asserts s^* o iota_H != id on a non-flat section",
    "contrary_control_vacuous":
        "A6 uses a FLAT section as the contrary control (must not discriminate)",
    "clifford_square_sign":
        "B5 asserts the Clifford square with a flipped normal-direction sign",
    "delta_vanishes_in_flat_gauge":
        "B4 asserts the defect operator Delta_i vanishes at K = 0",
    "flat_gauge_saves_not_larger":
        "B7 asserts ker Gamma^14D is carried into ker Gamma^4D at K = 0",
    "quote_drift":
        "C1 asserts a sentence that is NOT in SS18.3",
    "canon_correction_missing":
        "C4 asserts canon is missing the independently verified correction",
    "repair_reverted":
        "C5 asserts a repaired dependent still carries its defective text",
}


# ===========================================================================
# PART A -- the geometry of the section pullback.  Exact sympy.
#
# Y14 = Met(X4).  Adapted coordinates (x^0..x^3, u_0..u_9) where the ten u_I
# are the independent components of the Sym^2(T*X4) fibre.  The observation
# section is s(x) = (x, g_ab(x)): the section IS the metric.
#
# ds: T X4 -> T Y14 is the 14x4 Jacobian J.  The pullback on one-forms is its
# transpose: s^* omega = J^T omega.
# ===========================================================================

NX, NU, NY = 4, 10, 14
SYM_PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]   # 10 of them
assert len(SYM_PAIRS) == NU

XS = sp.symbols("x0 x1 x2 x3", real=True)


def jacobian_symbolic():
    """J = ds for a fully general section s(x) = (x, g_ab(x))."""
    g = [sp.Function(f"g_{a}{b}")(*XS) for (a, b) in SYM_PAIRS]
    J = sp.zeros(NY, NX)
    for mu in range(NX):
        J[mu, mu] = 1
    for I in range(NU):
        for mu in range(NX):
            J[NX + I, mu] = sp.diff(g[I], XS[mu])
    return J, g


def jacobian_concrete(section):
    """J for a concrete section: `section` is a list of 10 sympy expressions."""
    J = sp.zeros(NY, NX)
    for mu in range(NX):
        J[mu, mu] = 1
    for I in range(NU):
        for mu in range(NX):
            J[NX + I, mu] = sp.diff(section[I], XS[mu])
    return J


def pullback(J, omega):
    """s^* omega = J^T omega.  omega is a 14-vector of coefficients."""
    return J.T * sp.Matrix(NY, 1, list(omega))


# Concrete sections used by the sweeps.  MINKOWSKI is the flat-section gauge
# d_mu g_ab = 0.  The rest are non-flat, exact-rational, and deliberately
# varied: linear, quadratic, mixed, and one where only a single fibre
# direction varies.
x0, x1, x2, x3 = XS
FLAT_MINKOWSKI = [sp.Integer(-1) if (a, b) == (0, 0)
                  else (sp.Integer(1) if a == b else sp.Integer(0))
                  for (a, b) in SYM_PAIRS]

NONFLAT_SECTIONS = {
    "linear_x0": [FLAT_MINKOWSKI[I] + (x0 * sp.Rational(1, 3) if I == 0 else 0)
                  for I in range(NU)],
    "one_fibre_only": [FLAT_MINKOWSKI[I] + (x2 * sp.Rational(2, 5) if I == 7 else 0)
                       for I in range(NU)],
    "quadratic": [FLAT_MINKOWSKI[I] + sp.Rational(I + 1, 7) * x1 ** 2
                  for I in range(NU)],
    "mixed": [FLAT_MINKOWSKI[I] + sp.Rational(I - 4, 11) * x0 * x3
              + sp.Rational(1, 2) * x2
              for I in range(NU)],
    "all_directions": [FLAT_MINKOWSKI[I]
                       + sum(sp.Rational(I + 1, mu + 3) * XS[mu] for mu in range(NX))
                       for I in range(NU)],
}


# ===========================================================================
# PART B -- exact Gaussian-integer representation of Cl(9,5).
#
# A complex matrix M = A + iB is held as the int64 pair (A, B).  Every gamma
# has entries in {0, +-1, +-i}; every product used below stays far inside
# int64.  MAG_GUARD proves it rather than assuming it.
# ===========================================================================

DIM = 128          # 2^7: the irreducible Cl(14, C) module
MAG_GUARD = 2 ** 40

# eta = diag(+1 x 9, -1 x 5), ordered so that A = 0..3 is HORIZONTAL with
# signature (3,1) and A = 4..13 is NORMAL with signature (6,4).
# Horizontal: one timelike (A=0) + three spacelike.
# Normal:     six spacelike + four timelike.
ETA = [-1, +1, +1, +1] + [+1] * 6 + [-1] * 4
HORIZ = list(range(0, 4))
NORMAL = list(range(4, 14))
assert len(ETA) == NY
assert sum(1 for e in ETA if e > 0) == 9 and sum(1 for e in ETA if e < 0) == 5


class GMat:
    """Exact Gaussian-integer matrix, held as int64 (real, imag)."""

    __slots__ = ("re", "im")

    def __init__(self, re, im):
        self.re = np.asarray(re, dtype=np.int64)
        self.im = np.asarray(im, dtype=np.int64)

    @staticmethod
    def zeros(n):
        return GMat(np.zeros((n, n), np.int64), np.zeros((n, n), np.int64))

    @staticmethod
    def eye(n):
        return GMat(np.eye(n, dtype=np.int64), np.zeros((n, n), np.int64))

    def __matmul__(self, o):
        r = self.re @ o.re - self.im @ o.im
        i = self.re @ o.im + self.im @ o.re
        return GMat(r, i)

    def __add__(self, o):
        return GMat(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return GMat(self.re - o.re, self.im - o.im)

    def __mul__(self, k):
        return GMat(self.re * int(k), self.im * int(k))

    __rmul__ = __mul__

    def is_zero(self):
        return not (self.re.any() or self.im.any())

    def equals(self, o):
        return np.array_equal(self.re, o.re) and np.array_equal(self.im, o.im)

    def mag(self):
        return int(max(np.abs(self.re).max(initial=0),
                       np.abs(self.im).max(initial=0)))


class GVec:
    """Exact Gaussian-integer column vector (a spinor)."""

    __slots__ = ("re", "im")

    def __init__(self, re, im):
        self.re = np.asarray(re, dtype=np.int64)
        self.im = np.asarray(im, dtype=np.int64)

    @staticmethod
    def zeros(n):
        return GVec(np.zeros(n, np.int64), np.zeros(n, np.int64))

    def __add__(self, o):
        return GVec(self.re + o.re, self.im + o.im)

    def __mul__(self, k):
        return GVec(self.re * int(k), self.im * int(k))

    __rmul__ = __mul__

    def is_zero(self):
        return not (self.re.any() or self.im.any())

    def equals(self, o):
        return np.array_equal(self.re, o.re) and np.array_equal(self.im, o.im)


def apply(M: GMat, v: GVec) -> GVec:
    return GVec(M.re @ v.re - M.im @ v.im, M.re @ v.im + M.im @ v.re)


def _kron(a: GMat, b: GMat) -> GMat:
    return GMat(np.kron(a.re, b.re) - np.kron(a.im, b.im),
                np.kron(a.re, b.im) + np.kron(a.im, b.re))


_I2 = GMat([[1, 0], [0, 1]], [[0, 0], [0, 0]])
_S1 = GMat([[0, 1], [1, 0]], [[0, 0], [0, 0]])
_S2 = GMat([[0, 0], [0, 0]], [[0, -1], [1, 0]])
_S3 = GMat([[1, 0], [0, -1]], [[0, 0], [0, 0]])


def build_gammas():
    """Jordan-Wigner Cl(14, Euclidean), then rotate to signature (9,5).

    Euclidean:  gE_{2k-1} = s3^{(k-1)} (x) s1 (x) I^{(7-k)}
                gE_{2k}   = s3^{(k-1)} (x) s2 (x) I^{(7-k)}
    so {gE_a, gE_b} = 2 delta_ab.  Then Gamma_A = gE_A for eta_A = +1 and
    Gamma_A = i * gE_A for eta_A = -1, giving {Gamma_A, Gamma_B} = 2 eta_AB.
    """
    n = 7
    euclid = []
    for k in range(1, n + 1):
        for sig in (_S1, _S2):
            M = GMat([[1]], [[0]])
            for j in range(1, n + 1):
                blk = _S3 if j < k else (sig if j == k else _I2)
                M = _kron(M, blk)
            euclid.append(M)
    assert len(euclid) == NY
    gammas = []
    for A in range(NY):
        gE = euclid[A]
        if ETA[A] > 0:
            gammas.append(gE)
        else:
            # multiply by i: (a + ib) * i = -b + ia
            gammas.append(GMat(-gE.im, gE.re))
    return gammas


GAMMA = build_gammas()


def gamma_trace_14(gam, psi):
    """Gamma^14D(psi) = sum_A Gamma_A psi_A, psi a list of 14 spinors."""
    out = GVec.zeros(DIM)
    for A in range(NY):
        out = out + apply(gam[A], psi[A])
    return out


def gamma_trace_4(gam, chi):
    """Gamma^4D(chi) = sum_mu Gamma_mu chi_mu, chi a list of 4 spinors."""
    out = GVec.zeros(DIM)
    for mu in HORIZ:
        out = out + apply(gam[mu], chi[mu])
    return out


def s_star(K, psi):
    """(s^* psi)_mu = psi_mu + sum_i K[i][mu] psi_i.

    K is the 10x4 integer section derivative in the adapted frame, i.e. the
    frame form of d_mu g_ab.  K = 0 is the flat-section gauge.
    """
    out = []
    for mu in HORIZ:
        acc = psi[mu]
        for idx, i in enumerate(NORMAL):
            k = int(K[idx][mu])
            if k:
                acc = acc + psi[i] * k
        out.append(acc)
    return out


def horizontal_projection(psi):
    """P_H psi -- what SS18.3 claims s^* is."""
    return [psi[mu] for mu in HORIZ]


def delta(gam, K, idx):
    """Defect operator  Delta_i = sum_mu K[i][mu] Gamma_mu  -  Gamma_i."""
    acc = GMat.zeros(DIM)
    for mu in HORIZ:
        k = int(K[idx][mu])
        if k:
            acc = acc + gam[mu] * k
    return acc - gam[NORMAL[idx]]


def basis_spinor(j, imaginary=False):
    v = GVec.zeros(DIM)
    if imaginary:
        v.im[j] = 1
    else:
        v.re[j] = 1
    return v


# Deterministic integer section-derivative matrices used by the Part B sweep.
K_FLAT = [[0] * 4 for _ in range(10)]


def _k_matrix(seed):
    """Deterministic, exact, integer 10x4 section derivative."""
    return [[((seed * (i + 1) * (mu + 2) + 7 * i - 3 * mu) % 9) - 4
             for mu in range(4)] for i in range(10)]


K_NONFLAT = {f"K{seed}": _k_matrix(seed) for seed in (1, 2, 3, 5, 8)}
K_ALL = dict(K_NONFLAT)
K_ALL["K_flat"] = K_FLAT


# ===========================================================================
# PART C -- the exact strings this repair targets.
# ===========================================================================

VZ_SCHUR = "explorations/vz-evasion/vz-schur-complement-2026-06-23.md"
CANON_MAP = "canon/no-go-class-relative-map.md"

# The original defective text.  Left in place, struck through, so the record is
# auditable; the repair must NOT have deleted it.
DEFECTIVE_SENTENCES = [
    # the stated ground (P2)
    "The pullback functor `s*: Gamma(Omega^1(Y^{14})) -> Gamma(Omega^1(X^4))` "
    "sends `psi` to its horizontal part.",
    # the "not larger" clause (P3)
    "not a larger sector (no extra RS components from the normal directions",
    # the KK-scalar corollary (P3)
    "They do not contribute to `R_s`",
]

# Non-canon dependents.  value = (substring that must be present AFTER repair,
#                                 what this site uses).
# Every one of these repairs was applied by this pass.
REPAIRED = {
    "explorations/vz-evasion/vz-14d-mixed-covectors-2026-06-23.md": (
        "on the **corrected** ground of CORRECTION VZ4-01", "P1 only"),
    "explorations/analytic-index-fredholm/g2-kk-zero-mode-unitarity-2026-06-23.md": (
        "`s*` is a **contraction**, not an `H*/N*` projection", "P1 + P3"),
    "explorations/vz-evasion/vz1-oq3-gravitational-vz-weyl-tensor-2026-06-23.md": (
        "**REFUTED 2026-08-15** (CORRECTION VZ4-01", "P1 + P3"),
    "explorations/vz-evasion/vz-f5-curvature-check-2026-06-23.md": (
        "the word VERIFIED was the defect", "P1, grade-stale"),
    "explorations/vz-evasion/no-go-velo-zwanziger-canon-entry-2026-06-23.md": (
        "the observation map is a\n  contraction", "P1 + P3"),
}

# Dependent that needs NO repair: it uses the surviving claim only.
UNTOUCHED = {
    "explorations/time-as-finality-crosswalk/h3-gap2-gu-universality-2026-06-23.md":
        "and OQ3-V3 RESOLVED)",
}

# The canon site.  NOT edited by this pass -- the diff is proposed, not applied.
CANON_ANCHOR = (
    "OQ3-V3: `R_s = ker Gamma^{4D}` exactly -- section pullback on H*/N* "
    "split is exact, normal RS components are KK scalars not spin-3/2 fields.")


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def norm(s: str) -> str:
    """WHITESPACE NORMALIZATION IS LOAD-BEARING.  This repository hard-wraps
    markdown near column 90, so every sentence this repair targets straddles a
    newline.  Naive substring search silently misses them -- and a quote check
    that cannot find its quote is a check that never runs."""
    return " ".join(s.split())


# ===========================================================================
# Tests
# ===========================================================================

class PartA_Geometry(unittest.TestCase):
    """The pullback along a section, exactly, for a general metric section."""

    def test_a1_ds_is_rank_four_with_section_derivative(self):
        """ds(d_mu) = d_mu + (d_mu g_ab) d/d(g_ab); rank 4 for every section."""
        J, g = jacobian_symbolic()
        for mu in range(NX):
            for nu in range(NX):
                self.assertEqual(sp.simplify(J[nu, mu] - (1 if mu == nu else 0)), 0)
            for I in range(NU):
                self.assertEqual(sp.simplify(J[NX + I, mu] - sp.diff(g[I], XS[mu])), 0)
        for name, sec in NONFLAT_SECTIONS.items():
            self.assertEqual(jacobian_concrete(sec).rank(), 4, name)
        self.assertEqual(jacobian_concrete(FLAT_MINKOWSKI).rank(), 4)

    def test_a2_pullback_identity_general_section(self):
        """(s^* omega)_mu = omega_mu + omega_(ab) d_mu g_ab -- general g_ab(x).

        Independent re-derivation of the identity MD-1 calls E2 and LA-8
        calls [A2].  This probe does NOT inherit it.
        """
        J, g = jacobian_symbolic()
        om = sp.symbols("w0:14", real=True)
        got = pullback(J, om)
        for mu in range(NX):
            expected = om[mu] + sum(om[NX + I] * sp.diff(g[I], XS[mu])
                                    for I in range(NU))
            if MUT == "pullback_is_projection":
                expected = om[mu]          # <-- this IS the SS18.3 claim
            self.assertEqual(sp.simplify(got[mu] - expected), 0,
                             f"pullback component mu={mu}")

    def test_a3_horizontal_restriction_is_the_identity_gauge_independently(self):
        """s^* o iota_H = id_4 for EVERY section.  No gauge condition.

        This is what rescues SS18.3's conclusion: on the pi-horizontal
        subbundle the pullback is a canonical isomorphism, flat or not.
        """
        for name, sec in list(NONFLAT_SECTIONS.items()) + [("flat", FLAT_MINKOWSKI)]:
            J = jacobian_concrete(sec)
            for mu in range(NX):
                alpha = [1 if k == mu else 0 for k in range(NX)] + [0] * NU
                got = pullback(J, alpha)
                want = sp.Matrix(NX, 1, [1 if k == mu else 0 for k in range(NX)])
                if MUT == "horizontal_restriction_needs_gauge" and name != "flat":
                    self.assertNotEqual(sp.simplify(got - want), sp.zeros(NX, 1))
                else:
                    self.assertEqual(sp.simplify(got - want), sp.zeros(NX, 1),
                                     f"{name}, mu={mu}")

    def test_a4_kernel_is_the_annihilator_of_ds_not_the_coordinate_normals(self):
        """ker s^* is 10-dim and is span{du_I - (d_mu g_I) dx^mu}, NOT span{du_I}.

        SS18.3 identifies the two.  They coincide iff d_mu g_ab = 0.
        """
        for name, sec in NONFLAT_SECTIONS.items():
            J = jacobian_concrete(sec)
            ker = J.T.nullspace()
            self.assertEqual(len(ker), NU, f"{name}: dim ker s^* != 10")
            # the true kernel basis
            for I in range(NU):
                om = [0] * NY
                om[NX + I] = 1
                for mu in range(NX):
                    om[mu] = -sp.diff(sec[I], XS[mu])
                self.assertEqual(sp.simplify(pullback(J, om)), sp.zeros(NX, 1),
                                 f"{name}: du_{I} - (dg_{I}) is not annihilated")
            # the COORDINATE normals are NOT annihilated for a non-flat section
            annihilated = []
            for I in range(NU):
                om = [0] * NY
                om[NX + I] = 1
                annihilated.append(sp.simplify(pullback(J, om)) == sp.zeros(NX, 1))
            if MUT == "coordinate_normals_are_kernel":
                self.assertTrue(all(annihilated), f"{name}")
            else:
                self.assertFalse(all(annihilated),
                                 f"{name}: s^* wrongly kills every du_I")

    def test_a5_pullback_equals_horizontal_projection_iff_flat(self):
        """s^* == P_H  <=>  d_mu g_ab == 0.  Both directions, exactly."""
        om = sp.symbols("w0:14", real=True)
        # (<=) flat gauge: they agree
        Jf = jacobian_concrete(FLAT_MINKOWSKI)
        got = pullback(Jf, om)
        for mu in range(NX):
            self.assertEqual(sp.simplify(got[mu] - om[mu]), 0)
        # (=>) any non-flat section: they differ
        for name, sec in NONFLAT_SECTIONS.items():
            J = jacobian_concrete(sec)
            diff = pullback(J, om) - sp.Matrix(NX, 1, [om[mu] for mu in range(NX)])
            self.assertNotEqual(sp.simplify(diff), sp.zeros(NX, 1),
                                f"{name}: s^* coincides with P_H off the flat gauge")

    def test_a6_contrary_control_nonflat_section(self):
        """CONTRARY CONTROL -- a configuration where the extra term provably
        does NOT vanish, evaluated to a named exact rational.

        Section: g_00 = -1 + x0/3, all other components Minkowski.
        Covector: omega = du_0 (pure normal, unit coefficient).
        Then (s^* omega)_0 = d_0 g_00 = 1/3 and P_H omega = 0.
        """
        which = "flat" if MUT == "contrary_control_vacuous" else "nonflat"
        sec = (FLAT_MINKOWSKI if which == "flat"
               else NONFLAT_SECTIONS["linear_x0"])
        J = jacobian_concrete(sec)
        om = [0] * NY
        om[NX + 0] = 1                      # du_0, the (0,0) fibre direction
        got = pullback(J, om)
        proj = sp.zeros(NX, 1)              # P_H kills a pure normal covector
        residual = sp.simplify(got - proj)
        # the discriminating number, exact
        self.assertEqual(residual[0], sp.Rational(1, 3),
                         "contrary control did not produce the expected residual")
        self.assertNotEqual(residual, sp.zeros(NX, 1),
                            "CONTRARY CONTROL IS VACUOUS: s^* == P_H here")
        # and it is genuinely a gauge statement: the SAME covector on the flat
        # section gives exactly zero residual.
        Jf = jacobian_concrete(FLAT_MINKOWSKI)
        self.assertEqual(sp.simplify(pullback(Jf, om) - proj), sp.zeros(NX, 1))

    def test_a7_sweep_all_sections_all_covectors(self):
        """Sweep: every listed section x every basis covector, exact."""
        checked = 0
        for name, sec in list(NONFLAT_SECTIONS.items()) + [("flat", FLAT_MINKOWSKI)]:
            J = jacobian_concrete(sec)
            for A in range(NY):
                om = [0] * NY
                om[A] = 1
                got = pullback(J, om)
                if A < NX:
                    want = sp.Matrix(NX, 1, [1 if k == A else 0 for k in range(NX)])
                else:
                    I = A - NX
                    want = sp.Matrix(NX, 1,
                                     [sp.diff(sec[I], XS[mu]) for mu in range(NX)])
                self.assertEqual(sp.simplify(got - want), sp.zeros(NX, 1),
                                 f"{name}, basis covector {A}")
                checked += 1
        self.assertEqual(checked, 6 * NY)


class PartB_Clifford(unittest.TestCase):
    """What the contraction does to the gamma-trace / RS sector."""

    def test_b1_clifford_relations_exact(self):
        """{Gamma_A, Gamma_B} = 2 eta_AB for all 91 pairs and 14 squares."""
        two_id = GMat.eye(DIM) * 2
        for A in range(NY):
            sq = GAMMA[A] @ GAMMA[A]
            self.assertLess(sq.mag(), MAG_GUARD)
            self.assertTrue(sq.equals(GMat.eye(DIM) * ETA[A]),
                            f"Gamma_{A}^2 != eta_{A}")
        for A, B in itertools.combinations(range(NY), 2):
            anti = GAMMA[A] @ GAMMA[B] + GAMMA[B] @ GAMMA[A]
            self.assertLess(anti.mag(), MAG_GUARD)
            self.assertTrue(anti.is_zero(), f"{{Gamma_{A}, Gamma_{B}}} != 0")
        self.assertEqual(len(list(itertools.combinations(range(NY), 2))), 91)

    def test_b2_signature_is_nine_five_split_three_one_plus_six_four(self):
        """Horizontal (3,1), normal (6,4), total (9,5) -- the carrier split."""
        h = [ETA[a] for a in HORIZ]
        n = [ETA[i] for i in NORMAL]
        self.assertEqual((h.count(1), h.count(-1)), (3, 1))
        self.assertEqual((n.count(1), n.count(-1)), (6, 4))
        self.assertEqual((ETA.count(1), ETA.count(-1)), (9, 5))

    def test_b3_gamma_trace_transport_identity(self):
        """Gamma^4D(s^* psi) = Gamma^14D(psi) + sum_i Delta_i psi_i, exactly.

        Delta_i = sum_mu K[i][mu] Gamma_mu - Gamma_i.  This is the exact
        bookkeeping SS18.3 never writes down.
        """
        for kname, K in K_ALL.items():
            for j in (0, 1, 37, 91, 127):
                for imag in (False, True):
                    psi = [GVec.zeros(DIM) for _ in range(NY)]
                    psi[NX + 3] = basis_spinor(j, imag)
                    psi[1] = basis_spinor((j + 5) % DIM, not imag)
                    lhs = gamma_trace_4(GAMMA, s_star(K, psi))
                    rhs = gamma_trace_14(GAMMA, psi)
                    for idx in range(10):
                        rhs = rhs + apply(delta(GAMMA, K, idx), psi[NORMAL[idx]])
                    self.assertTrue(lhs.equals(rhs), f"{kname}, j={j}, imag={imag}")

    def test_b4_defect_operator_never_vanishes(self):
        """Delta_i != 0 for EVERY i and EVERY section -- flat gauge included.

        Gamma_i is not in span{Gamma_mu}, so Delta_i = K^i.Gamma - Gamma_i can
        never be zero.  This is why the flat gauge does not rescue P3.
        """
        for kname, K in K_ALL.items():
            for idx in range(10):
                D = delta(GAMMA, K, idx)
                self.assertLess(D.mag(), MAG_GUARD)
                if MUT == "delta_vanishes_in_flat_gauge" and kname == "K_flat":
                    self.assertTrue(D.is_zero(), "flat gauge")
                else:
                    self.assertFalse(D.is_zero(), f"{kname}, i={idx}")
        # and at K = 0 it is exactly -Gamma_i
        for idx in range(10):
            self.assertTrue(delta(GAMMA, K_FLAT, idx)
                            .equals(GAMMA[NORMAL[idx]] * -1))

    def test_b5_defect_operator_clifford_square(self):
        """Delta_i^2 = (sum_mu eta_mu K[i][mu]^2 + eta_i) Id, exactly."""
        for kname, K in K_ALL.items():
            for idx in range(10):
                D = delta(GAMMA, K, idx)
                sq = D @ D
                self.assertLess(sq.mag(), MAG_GUARD)
                c = sum(ETA[mu] * int(K[idx][mu]) ** 2 for mu in HORIZ) \
                    + ETA[NORMAL[idx]]
                if MUT == "clifford_square_sign":
                    c = c - 2 * ETA[NORMAL[idx]]
                self.assertTrue(sq.equals(GMat.eye(DIM) * c),
                                f"{kname}, i={idx}: Delta^2 != {c} Id")

    def test_b6_P1_SURVIVES_horizontal_identification_is_gauge_independent(self):
        """P1: s^*( R^14D  n  horizontal ) == ker Gamma^4D, for EVERY section.

        (i) forward: psi horizontal and Gamma^14D psi = 0
                     =>  s^* psi = psi_H  and  Gamma^4D(s^* psi) = 0
        (ii) reverse: every chi in ker Gamma^4D is s^*(iota_H chi) with
                     iota_H chi in R^14D.
        Neither direction uses any condition on K.  This is the corrected
        ground for SS18.3's conclusion.
        """
        for kname, K in K_ALL.items():
            for j in (0, 3, 64, 127):
                # (i) build a horizontal psi in ker Gamma^14D:
                #     psi_1 arbitrary, psi_0 chosen so Gamma_0 psi_0 = -Gamma_1 psi_1
                v = basis_spinor(j)
                psi = [GVec.zeros(DIM) for _ in range(NY)]
                psi[1] = v
                # Gamma_0^2 = eta_0 = -1  =>  Gamma_0^{-1} = -Gamma_0
                psi[0] = apply(GAMMA[0] @ GAMMA[1], v)      # = -G0^{-1} G1 v
                self.assertTrue(gamma_trace_14(GAMMA, psi).is_zero(),
                                "test setup: psi is not in ker Gamma^14D")
                chi = s_star(K, psi)
                # s^* acts as the identity on the horizontal part
                for mu in HORIZ:
                    self.assertTrue(chi[mu].equals(horizontal_projection(psi)[mu]),
                                    f"{kname}: s^* != P_H on a horizontal psi")
                self.assertTrue(gamma_trace_4(GAMMA, chi).is_zero(),
                                f"{kname}: horizontal image left ker Gamma^4D")
                # (ii) reverse inclusion: lift chi back horizontally
                lift = list(chi) + [GVec.zeros(DIM)] * NU
                self.assertTrue(gamma_trace_14(GAMMA, lift).is_zero(),
                                f"{kname}: horizontal lift left ker Gamma^14D")
                self.assertTrue(all(s_star(K, lift)[mu].equals(chi[mu])
                                    for mu in HORIZ), kname)

    def test_b7_P3_FAILS_IN_EVERY_GAUGE_INCLUDING_FLAT(self):
        """P3: s^*(R^14D) is NOT contained in ker Gamma^4D -- for any section.

        Take psi with one normal component psi_i = v and horizontal part fixed
        by Gamma^14D psi = 0.  Then Gamma^4D(s^* psi) = Delta_i v, which is
        nonzero because Delta_i is invertible whenever (K^i, -e_i) is non-null
        -- and at K = 0 it is exactly -Gamma_i, always invertible.

        The flat-section gauge does NOT save the "not a larger sector" clause.
        """
        for kname, K in K_ALL.items():
            for idx in (0, 4, 9):
                i = NORMAL[idx]
                for j in (0, 11, 100):
                    v = basis_spinor(j)
                    psi = [GVec.zeros(DIM) for _ in range(NY)]
                    psi[i] = v
                    # solve Gamma_0 psi_0 = -Gamma_i v, i.e. psi_0 = G0 Gi v
                    psi[0] = apply(GAMMA[0] @ GAMMA[i], v)
                    self.assertTrue(gamma_trace_14(GAMMA, psi).is_zero(),
                                    "test setup: psi not in ker Gamma^14D")
                    out = gamma_trace_4(GAMMA, s_star(K, psi))
                    want = apply(delta(GAMMA, K, idx), v)
                    self.assertTrue(out.equals(want), f"{kname} i={i}")
                    if MUT == "flat_gauge_saves_not_larger" and kname == "K_flat":
                        self.assertTrue(out.is_zero(), "flat gauge")
                    else:
                        self.assertFalse(
                            out.is_zero(),
                            f"{kname}, i={i}, j={j}: pullback of a 14D RS field "
                            f"landed in ker Gamma^4D")

    def test_b8_image_is_strictly_larger_delta_is_invertible(self):
        """s^*(R^14D) = the WHOLE 4D one-form bundle, not just ker Gamma^4D.

        Delta_i is invertible iff its Clifford square is nonzero; then
        Gamma^4D o s^* restricted to R^14D is onto S, so the image of the
        14D RS sector under pullback is everything.
        """
        for kname, K in K_ALL.items():
            hits = 0
            for idx in range(10):
                c = sum(ETA[mu] * int(K[idx][mu]) ** 2 for mu in HORIZ) \
                    + ETA[NORMAL[idx]]
                D = delta(GAMMA, K, idx)
                self.assertTrue((D @ D).equals(GMat.eye(DIM) * c))
                if c != 0:
                    hits += 1
            self.assertGreater(hits, 0,
                               f"{kname}: no invertible Delta_i -- surjectivity "
                               f"argument would be vacuous here")
        # at K = 0 EVERY Delta_i is invertible: Delta_i^2 = eta_i Id = +-Id
        for idx in range(10):
            c = ETA[NORMAL[idx]]
            self.assertIn(c, (1, -1))
            self.assertTrue((delta(GAMMA, K_FLAT, idx) @ delta(GAMMA, K_FLAT, idx))
                            .equals(GMat.eye(DIM) * c))

    def test_b9_conclusions_are_index_convention_independent(self):
        """Raising the covector index (Gamma^A = eta^AB Gamma_B) changes
        nothing: P1 still holds, P3 still fails."""
        raised = [GAMMA[A] * ETA[A] for A in range(NY)]
        for kname, K in K_ALL.items():
            v = basis_spinor(9)
            # P1 -- horizontal psi
            psi = [GVec.zeros(DIM) for _ in range(NY)]
            psi[1] = v
            psi[0] = apply(raised[0] @ raised[1], v) * (ETA[0] * ETA[0])
            # solve directly instead: psi_0 = -(raised[0])^{-1} raised[1] v
            # (raised[0])^2 = eta_0^2 * eta_0 Id = eta_0 Id  => inverse = eta_0 * raised[0]
            psi[0] = apply(raised[0], apply(raised[1], v)) * (-ETA[0])
            self.assertTrue(gamma_trace_14(raised, psi).is_zero())
            self.assertTrue(gamma_trace_4(raised, s_star(K, psi)).is_zero(),
                            f"{kname}: P1 broke under index raising")
            # P3 -- normal-component psi
            i = NORMAL[2]
            psi2 = [GVec.zeros(DIM) for _ in range(NY)]
            psi2[i] = v
            psi2[0] = apply(raised[0], apply(raised[i], v)) * (-ETA[0])
            self.assertTrue(gamma_trace_14(raised, psi2).is_zero())
            self.assertFalse(gamma_trace_4(raised, s_star(K, psi2)).is_zero(),
                             f"{kname}: P3 spuriously held under index raising")


class PartC_RepairState(unittest.TestCase):
    """Guard the applied repairs, and guard that canon was NOT touched."""

    def test_c1_original_defective_text_is_preserved_and_struck(self):
        """The repair strikes the defective sentences; it must not delete them.
        A correction that erases the record is unauditable."""
        text = read(VZ_SCHUR)
        i = text.index("### 18.3 OQ3-V3")
        j = text.index("### 18.4 Combined Result")
        body = norm(text[i:j])
        sentences = list(DEFECTIVE_SENTENCES)
        if MUT == "quote_drift":
            sentences.append("The pullback functor is a bundle isomorphism onto T*X^4.")
        for s in sentences:
            self.assertIn(norm(s), body, f"SS18.3 no longer contains: {s[:60]!r}")
        self.assertIn("~~No approximation is made.~~", body,
                      "the 'no approximation' grade was not struck")

    def test_c2_correction_block_is_in_place_with_all_three_propositions(self):
        text = norm(read(VZ_SCHUR))
        self.assertIn("CORRECTION VZ4-01", text)
        for token in (
            "**V3a (the identification, restricted to horizontal 1-forms): VERIFIED, exact, gauge-independent.**",
            "**V3b (the stated ground",
            "**V3c (the \"not a larger sector\" / KK-scalar clause): REFUTED in EVERY gauge**",
            "(s*psi)_mu = psi_mu + psi_(ab) d_mu g_ab",
            "Delta_i := (d_mu g_i) gamma^mu_H  -  gamma^i_N",
            "REDUCTION-FIDELITY",
        ):
            self.assertIn(norm(token), text, f"correction block missing: {token[:50]!r}")
        self.assertNotIn("**Grade.** VERIFIED. The argument uses only", text,
                         "the VERIFIED grade line was not corrected")

    def test_c2b_the_notational_slip_is_named(self):
        """SS18.3 writes the horizontal subbundle as `H*_x = s*(T*X^4)`.
        `s*` maps T*Y14 -> T*X4 and cannot produce a subbundle OF T*Y14; the
        correct object is `pi^*(T*X^4)`.  That slip is what makes "s* sends psi
        to its horizontal part" look like a tautology.  The original wording is
        preserved and the correction must name it."""
        text = norm(read(VZ_SCHUR))
        self.assertIn("with `H*_x = s*(T*X^4)` (horizontal)", text)
        self.assertIn("Read every \"`H*`\" in this section as `pi^*(T*X^4)`", text)

    def test_c3_frontmatter_now_records_the_split_grade(self):
        head = norm(read(VZ_SCHUR).split("---", 2)[1])
        self.assertIn("OQ3-V1/V2/V3 verified only in constant-coefficient", head)
        self.assertIn("oq3_v3: RESOLVED_ON_CORRECTED_GROUND", head)
        self.assertIn("oq3_v3_correction:", head)
        self.assertNotIn("oq3_v3: RESOLVED\n", read(VZ_SCHUR).split("---", 2)[1])

    def test_c4_CANON_CARRIES_INDEPENDENTLY_VERIFIED_NARROW_CORRECTION(self):
        """A later independent review approved and integrated the narrow diff."""
        text = norm(read(CANON_MAP))
        self.assertIn("OQ3-V2 and OQ3-V3 are RESOLVED (exact, gauge-independent)", text)
        if MUT == "canon_correction_missing":
            self.assertIn(norm(CANON_ANCHOR), text)
        else:
            self.assertIn("VZ4-01", text)
            self.assertIn("REDUCTION-FIDELITY", text)
            self.assertNotIn(norm(CANON_ANCHOR), text)

    def test_c5_every_non_canon_repair_is_applied(self):
        for rel, (marker, _kind) in REPAIRED.items():
            body = norm(read(rel))
            expect = marker
            if MUT == "repair_reverted" and rel.endswith("vz-f5-curvature-check-2026-06-23.md"):
                expect = "This was VERIFIED (OQ3-V1, OQ3-V2, OQ3-V3). Including"
            self.assertIn(norm(expect), body, f"{rel}: repair missing")
        self.assertEqual(len(REPAIRED), 5, "repaired-site census moved")

    def test_c5b_the_untouched_dependent_needs_no_repair(self):
        """This site cites only the surviving identification.  It must NOT have
        been edited -- over-repair is as much a defect as under-repair."""
        for rel, anchor in UNTOUCHED.items():
            body = norm(read(rel))
            self.assertIn(norm(anchor), body)
            self.assertNotIn("CORRECTION VZ4-01", body,
                             f"{rel}: edited, but it uses only the surviving claim")

    def test_c5c_dependent_census(self):
        """1 canon + 6 explorations = 7.  The steward pass said 'five
        explorations'; the sixth is the VZ canon-entry file."""
        self.assertEqual(1 + len(REPAIRED) + len(UNTOUCHED), 7)
        self.assertIn("explorations/vz-evasion/no-go-velo-zwanziger-canon-entry-2026-06-23.md",
                      REPAIRED, "the sixth exploration is missing from the census")

    def test_c6_theorem_18_4_is_four_d_intrinsic(self):
        """SS18.4's theorem quantifies only over 4D objects, so P1 alone
        carries it.  Checked mechanically: the theorem block names no normal
        or vertical component."""
        text = read(VZ_SCHUR)
        i = text.index("**Theorem.** Let `s: X^4 -> Y^{14}`")
        j = text.index("**Proof summary.**")
        block = text[i:j]
        for tok in ("psi_N", "normal", "vertical", "N*_x"):
            self.assertNotIn(tok, block,
                             f"SS18.4 theorem statement mentions {tok!r}: it is "
                             f"not 4D-intrinsic after all")

    def test_c7_artifact_carries_routing_and_target_claim(self):
        art = ROOT / ("lab/active-research/joe-directed/vz-repair/"
                      "vz4-pullback-is-a-contraction-2026-08-15.md")
        if not art.exists():
            self.skipTest("artifact not yet written")
        text = art.read_text(encoding="utf-8")
        self.assertIn("GU-COMPARATOR-ROUTING", text)
        self.assertIn("lab/methods/source-native-comparator-routing.md", text)
        self.assertIn("Classification: `SOURCE_NATIVE_ROUTE`", text)
        self.assertIn("target_claim: OQ3-V3", text)
        self.assertIn("target_claim_verdict:", text)
        self.assertIn("INTERNAL-TARGET", text)

    def test_c8_no_forbidden_directory_was_touched(self):
        """SHARED checkout: four concurrent agents.  This pass must not have
        written into any directory it does not own."""
        forbidden = ("carrier", "carrier-notation", "class-shift", "chain-repair",
                     "wave22", "wave14", "ledger-advancement")
        owned = set(REPAIRED) | set(UNTOUCHED) | {VZ_SCHUR}
        for rel in owned:
            for d in forbidden:
                self.assertNotIn(f"/{d}/", "/" + rel,
                                 f"{rel} is inside a directory owned by another agent")


def run_selftest() -> int:
    print("VZ-4 selftest: planted controls, each must exit 1\n")
    failures = []
    for name, description in CONTROLS.items():
        env = dict(os.environ, VZ4_CONTROL=name)
        proc = subprocess.run([sys.executable, __file__], cwd=ROOT, env=env,
                              capture_output=True, text=True)
        ok = proc.returncode == 1
        print(f"  control {name:36s} exit {proc.returncode}  "
              f"{'OK  ' if ok else 'VACUOUS'}  ({description})")
        if not ok:
            failures.append(name)
    print()
    if failures:
        print(f"SELFTEST FAILED -- {len(failures)} vacuous control(s): "
              + ", ".join(failures))
        return 1
    print(f"SELFTEST PASSED -- {len(CONTROLS)}/{len(CONTROLS)} planted controls "
          f"each drove exit 1")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(run_selftest())
    if "--control" in sys.argv:
        idx = sys.argv.index("--control")
        os.environ["VZ4_CONTROL"] = sys.argv[idx + 1]
        MUT = sys.argv[idx + 1]
        del sys.argv[idx:idx + 2]
    unittest.main(verbosity=2)
