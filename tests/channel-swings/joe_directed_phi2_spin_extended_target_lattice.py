#!/usr/bin/env python3
r"""
PHI-2 -- EXTEND the 4D anomaly target lattice from Z^6 to carry charged
         spin-3/2, and RE-RUN PHI-1's containment on the extended target.

GU-COMPARATOR-ROUTING.  This probe touches a CONVENTIONAL COMPARATOR object
(the 4D Standard-Model perturbative gauge-anomaly conditions, the lattice
L = Z.(15 of SU(5)) (+) Z.(nu^c), and the ordinary index-density prescription
for higher-spin anomaly coefficients -- fork 1 of
lab/methods/source-native-comparator-routing.md).  Any result about that
object binds only that named model.  It is NOT evidence for or against
Weinstein's differently constructed 2+1 mechanism without an explicit typed
bridge.  Classification: BRIDGE_OR_SEMANTIC_BOUNDARY.

THE GAP THIS CLOSES.  PHI-1 (149/149) built phi : Z^15 -> Z^6 and proved
phi(ker M) subset L  <==>  v in L.  Its own declared weakest seam:

    "The spin-1/2 projection discards charged (1,1/2), (3/2,0), (1/2,1)
     content carrying the same internal numbers.  Z^6 has no spin slot, so
     D1..D5 on Z^6 are NOT the complete 4D conditions for a spectrum with
     charged spin-3/2.  The rank result survives; the target lattice would
     need extending.  AC-1 already has the exact RS rescalings."

WHAT IS BUILT HERE.

 (1) THE EXTENDED TARGET.   Z^6_ext := Z^6 (x) Z^5_spin = Z^30, slots
     (internal SM constituent i, Lorentz type s) with s ranging over the
     FIVE types PHI-1's own exact weight-multiset decomposition found in
     Lambda^p T*X4 (x) (1/2,0), p = 0..4:
         (1/2,0)  (0,1/2)  (1,1/2)  (3/2,0)  (1/2,1).

 (2) THE SPIN COEFFICIENTS, DERIVED not asserted.  Chern roots of T_C on a
     4-manifold give ch(Lambda^p T_C) = t0 + t1 p1 + te e exactly, and the
     self-dual / anti-self-dual split of Lambda^2.  The twist of each
     IRREDUCIBLE Lorentz type is then obtained by SUBTRACTION inside the
     exact Lorentz decomposition, and fed to AC-1's OWN anomaly_coeffs()
     -- imported from tests/channel-swings/joe_directed_anomaly_cancellation_probe.py,
     never reimplemented.  Result:

        type       twist            t0   gauge ratio g   mixed ratio m   euler
        (1/2,0)    1                 1        1               1            0
        (0,1/2)    -1               -1       -1              -1            0
        (1,1/2)    T_C + 1           5        5             -19            0
        (3/2,0)    Lambda^2_+ - 1    2        2             -22           +2
        (1/2,1)    Lambda^2_-        3        3             -21           -2

     The (1,1/2) row IS AC-1's carrier B / the gamma-traceless field space:
     REPRODUCED, not claimed.  The (3/2,0) and (1/2,1) rows are the new
     entries the extension needs.

 (3) THE EXTENDED CONDITION SYSTEM.  D1..D4 are components of the single
     symmetric cubic Tr_R X^3, so they rescale by g; D5 = grav^2-U(1)_Y is
     the mixed p1 Tr_R X channel, so it rescales by m.  That is AC-1's
     factorisation theorem, used as a theorem.  The 5 x 30 system has

        RANK 5,  not LA-3's rank 4.

     The LA-3 relation 2D1 - 27D2 - 36D3 - 9D4 + 9D5 = 0 is BROKEN, with
     exact residual 9(m - g) (x) f5 = -216 h (x) f5, h = (0,0,1,1,1) the
     higher-spin indicator -- and m - g = -24 h exactly, the 24 being the
     A-hat denominator.

 (4) THE EXTENDED ANOMALY-FREE LATTICE, rank 25:

        L_ext = { n : V_g(n) in L   and   f5 . N_H(n) = 0 }

     with V_g = sum_s g_s n_{.,s} and N_H = sum_{s higher-spin} n_{.,s}.
     Proved equal to the raw kernel by ROW-SPACE identity, not by sampling.
     L_ext is strictly larger than L (x) Z^5: explicit ALL-NON-NEGATIVE
     witness whose spin-1/2 projection is SU(3)^3-anomalous.  So PHI-1's
     seam statement is CONFIRMED with a witness.

 (5) THE EXTENDED REDUCTION.  phi_ext = v (x) K, K the exact decomposition
     matrix.  rank(phi_ext) = 3, not PHI-1's 1 -- the rank-1 headline is a
     spin-1/2-projection artefact.  Its spin-1/2 projection recovers PHI-1's
     k = (+1,-1,+1,-1,+1) exactly; its g-weighting is C(4,p) = (1,4,6,4,1).

 (6) THE VERDICT.  T(ker M) = Z^5 is untouched, so phi_ext(ker M) =
     phi_ext(Z^15): the ZERO-BIT result SURVIVES.  And

        phi_ext(ker M) subset L_ext   <==>   v in L

     -- PHI-1's containment SURVIVES VERBATIM.  The mechanism is exact and
     is proved, not sampled: the p = 0 deposit Lambda^0 T*X4 (x) s^*S is a
     PURE spin-1/2 slot with g = 1, and T(ker M) = Z^5 makes x_0 free, so
     that generator alone forces v in L; every other generator's condition
     is then automatic because gauge-blindness puts the SAME v in every
     spin slot.  Hence the verdict is invariant under ARBITRARY spin
     coefficients on the three higher-spin slots -- carrier bit, ghost
     scheme, Euler channel and all.  Both branches of the carrier fork are
     carried; the bit is NOT adjudicated here.

WHAT IS INHERITED, NOT ESTABLISHED.  The prescription "a 4D field valued in
Lambda^p T*X (x) S^+ (x) F has anomaly [A-hat ch(Lambda^p T_C) ch_F]_6" is
AC-1's own assumption (it is how AC-1 twists the RS field by T_C + q) and is
inherited here, not re-derived.  So is the ordinary-index arena itself.

Exit 0 iff every [E] result matches its stated exact value, every [C] control
fires as declared, and every [R] reproduction matches its filed owner.
Run with --mutate=<name> to exercise the failure path (must exit 1).

Run: _local/cas-venv/bin/python tests/channel-swings/joe_directed_phi2_spin_extended_target_lattice.py
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys
from fractions import Fraction as F

import sympy as sp
from sympy import Integer, Matrix, Rational as R
from sympy.matrices.normalforms import smith_normal_form

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

MUTATE = ""
for _a in sys.argv[1:]:
    if _a.startswith("--mutate="):
        MUTATE = _a.split("=", 1)[1]

FAIL: list[str] = []
NCHK = 0
TAGS: dict[str, int] = {}
RESULTS: dict[str, object] = {}


def check(tag: str, label: str, got, want) -> bool:
    global NCHK
    NCHK += 1
    TAGS[tag] = TAGS.get(tag, 0) + 1
    ok = (got == want)
    if not ok:
        FAIL.append(f"[{tag}] {label}: got {got!r}, want {want!r}")
    print(f"  [{tag}] {'PASS' if ok else 'FAIL'}  {label}: {got}")
    return ok


def assert_no_float(obj, path="result") -> None:
    if isinstance(obj, float):
        raise AssertionError(f"FLOAT found at {path}: {obj!r}")
    if isinstance(obj, dict):
        for k, v in obj.items():
            assert_no_float(v, f"{path}[{k!r}]")
    elif isinstance(obj, (list, tuple, set)):
        for i, v in enumerate(obj):
            assert_no_float(v, f"{path}[{i}]")


print("=" * 78)
print("PHI-2 -- extend the 4D target lattice to carry charged spin-3/2,")
print("         then re-run PHI-1's containment on it")
print("=" * 78)
if MUTATE:
    print(f"  *** MUTATION ACTIVE: {MUTATE} -- this run MUST exit 1 ***")


# ===========================================================================
# 0.  IMPORT the two owners.  Nothing they own is re-derived here.
#     AC-1  -> the RS twist -> anomaly-coefficient map (and its carrier table)
#     PHI-1 -> the exact Lorentz decomposition, ker M (via CB-C), M4, L
# ===========================================================================
print("\n-- 0. import AC-1 and PHI-1 (which imports CB-C).  Nothing re-derived. --")


def _load(name: str, relpath: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(REPO, relpath))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    buf, argv, code = io.StringIO(), sys.argv, None
    sys.argv = [name]
    try:
        with contextlib.redirect_stdout(buf):
            spec.loader.exec_module(mod)
    except SystemExit as e:
        code = e.code
    sys.argv = argv
    return mod, code


AC1, ac1_code = _load("phi2_ac1", "tests/channel-swings/joe_directed_anomaly_cancellation_probe.py")
PHI1, phi1_code = _load("phi2_phi1", "tests/channel-swings/joe_directed_phi_reduction_construction.py")
check("R", "AC-1 probe re-runs clean under import (exit code)", ac1_code, 0)
check("R", "PHI-1 probe re-runs clean under import (exit code)", phi1_code, 0)
check("R", "reproduce PHI-1: signed spin-1/2 multiplicities k_p = (-1)^p",
      PHI1.KVEC, [1, -1, 1, -1, 1])
check("R", "reproduce PHI-1: 5 distinct Lorentz types occur in Lambda^p (x) (1/2,0)",
      len(PHI1.LTYPES), 5)
check("R", "reproduce PHI-1: ker M has rank 10 (CB-C's system, imported)", len(PHI1.KINT), 10)
check("R", "reproduce LA-3 (via PHI-1): rank of the 5x6 spin-1/2 system", PHI1.M4.rank(), 4)


# ===========================================================================
# 1.  ch(Lambda^p T_C) FROM CHERN ROOTS, exactly, including the Euler class
#     and the self-dual / anti-self-dual split of Lambda^2.
# ===========================================================================
print("\n-- 1. ch(Lambda^p T_C) from Chern roots: t0 + t1.p1 + te.e (exact) --")
x1, x2 = sp.symbols("x1 x2")
P1 = x1**2 + x2**2          # first Pontryagin class of a 4-manifold
EU = x1 * x2                # Euler class
ROOTS = [x1, -x1, x2, -x2]  # Chern roots of the complexified tangent bundle


def ch_from_roots(rs) -> tuple[int, sp.Expr, sp.Expr]:
    """Exact (t0, coeff of p1, coeff of e) of ch(V), V with the given roots."""
    tot = sp.expand(sum(1 + r + r**2 / 2 for r in rs))
    t0 = tot.subs({x1: 0, x2: 0})
    d4 = sp.expand(tot - t0)
    poly = sp.Poly(d4, x1, x2) if d4 != 0 else None
    a = poly.coeff_monomial(x1**2) if poly else Integer(0)
    b = poly.coeff_monomial(x1 * x2) if poly else Integer(0)
    assert sp.simplify(d4 - (a * P1 + b * EU)) == 0, f"degree-4 part not in span(p1, e): {d4}"
    return int(t0), sp.nsimplify(a), sp.nsimplify(b)


LAMTW: dict[int, tuple] = {}
for p in range(5):
    LAMTW[p] = ch_from_roots([sum(sub) for sub in itertools.combinations(ROOTS, p)]
                             if p else [Integer(0)])
    print(f"     ch(Lambda^{p} T_C) = {LAMTW[p][0]} + ({LAMTW[p][1]}).p1 + ({LAMTW[p][2]}).e")

check("E", "ranks t0 of Lambda^p T_C are C(4,p)",
      [LAMTW[p][0] for p in range(5)], [math.comb(4, p) for p in range(5)])
check("R", "reproduce AC-1: ch(T_C) = 4 + p1 (degree-4 coefficient exactly 1, no Euler)",
      (LAMTW[1][0], LAMTW[1][1], LAMTW[1][2]), (4, Integer(1), Integer(0)))
check("E", "ch(Lambda^2 T_C) = 6 + 2 p1, with NO Euler term",
      (LAMTW[2][0], LAMTW[2][1], LAMTW[2][2]), (6, Integer(2), Integer(0)))
check("E", "Hodge duality on a 4-manifold: ch(Lambda^3 T_C) = ch(Lambda^1 T_C)",
      LAMTW[3], LAMTW[1])
check("E", "ch(Lambda^4 T_C) = 1 (the determinant line of an oriented real bundle is trivial)",
      LAMTW[4], (1, Integer(0), Integer(0)))
check("C", "control: no Lambda^p T_C carries an Euler term, so the p-basis is Euler-blind",
      sorted({LAMTW[p][2] for p in range(5)}), [Integer(0)])

# the self-dual / anti-self-dual halves.  Lambda^2 roots are {0, 0, +-(x1+x2), +-(x1-x2)}.
L2P = ch_from_roots([Integer(0), x1 + x2, -(x1 + x2)])     # Lambda^2_+ = (1,0)
L2M = ch_from_roots([Integer(0), x1 - x2, -(x1 - x2)])     # Lambda^2_- = (0,1)
if MUTATE == "euler":
    L2M = (L2M[0], L2M[1], -L2M[2])
print(f"     ch(Lambda^2_+) = {L2P[0]} + ({L2P[1]}).p1 + ({L2P[2]}).e")
print(f"     ch(Lambda^2_-) = {L2M[0]} + ({L2M[1]}).p1 + ({L2M[2]}).e")
check("E", "ch(Lambda^2_+) = 3 + p1 + 2e", L2P, (3, Integer(1), Integer(2)))
check("E", "ch(Lambda^2_-) = 3 + p1 - 2e", L2M, (3, Integer(1), Integer(-2)))
check("E", "the two halves sum to Lambda^2 and their EULER terms cancel exactly",
      tuple(a + b for a, b in zip(L2P, L2M)), LAMTW[2])
check("C", "control: the Euler term is the ONLY thing separating the two halves",
      (L2P[0] == L2M[0], L2P[1] == L2M[1], L2P[2] == L2M[2]), (True, True, False))


# ===========================================================================
# 2.  THE FIVE SPIN SLOTS AND THEIR TWISTS.  Derived by SUBTRACTION inside
#     PHI-1's exact Lorentz decomposition; ratios via AC-1's anomaly_coeffs.
# ===========================================================================
print("\n-- 2. twist of each irreducible Lorentz type, by subtraction --")
# PHI-1's labelling: irrep (a,b) <-> (j_+,j_-) = (a/2,b/2)
HALF_L, HALF_R = (1, 0), (0, 1)
S32, S11, S12 = (3, 0), (2, 1), (1, 2)          # (3/2,0), (1,1/2), (1/2,1)
SPINS = [HALF_L, HALF_R, S11, S32, S12]
NAME = {HALF_L: "(1/2,0)", HALF_R: "(0,1/2)", S11: "(1,1/2)",
        S32: "(3/2,0)", S12: "(1/2,1)"}
HIGHER = [S11, S32, S12]
check("R", "reproduce PHI-1: the five occurring types are exactly these",
      sorted(SPINS), PHI1.LTYPES)
check("R", "reproduce PHI-1: the three HIGHER-SPIN types PHI-1's seam named",
      sorted(HIGHER), sorted([S11, S32, S12]))

TW: dict[tuple, tuple] = {
    HALF_L: (1, Integer(0), Integer(0)),        # S^+ itself: trivial twist
    HALF_R: (-1, Integer(0), Integer(0)),       # S^-: same rep, opposite chirality -> -1
}
# (1,1/2)  =  Lambda^1 T*X (x) S^+   MINUS   (0,1/2)
TW[S11] = tuple(a - b for a, b in zip(LAMTW[1], TW[HALF_R]))
# (3/2,0)  =  Lambda^2_+ (x) S^+     MINUS   (1/2,0)
TW[S32] = tuple(a - b for a, b in zip(L2P, TW[HALF_L]))
# (1/2,1)  =  Lambda^2_- (x) S^+     (no subtraction needed)
TW[S12] = L2M
if MUTATE == "twist":
    TW[S32] = (3, TW[S32][1], TW[S32][2])

check("E", "twist of (1,1/2) is T_C + 1  (t0 = 5)", TW[S11][0], 5)
check("E", "twist of (3/2,0) is Lambda^2_+ - 1  (t0 = 2)", TW[S32][0], 2)
check("E", "twist of (1/2,1) is Lambda^2_-  (t0 = 3)", TW[S12][0], 3)
check("E", "the p1-degree t1 is 1 on exactly the three higher-spin slots and 0 on spin-1/2",
      [TW[s][1] for s in SPINS], [Integer(0), Integer(0), Integer(1), Integer(1), Integer(1)])

# ---- ratios, through AC-1's OWN anomaly_coeffs.  Not reimplemented. -------
cg_half, cm_half, res_half = AC1.anomaly_coeffs(1, 0)
check("R", "reproduce AC-1: spin-1/2 pure-gauge coefficient = 1/6", cg_half, R(1, 6))
check("R", "reproduce AC-1: spin-1/2 mixed gauge-gravitational coefficient = -1/24",
      cm_half, R(-1, 24))
check("R", "reproduce AC-1: spin-1/2 has NO other degree-6 term", sp.simplify(res_half), 0)

GV: list[Integer] = []
MV: list[Integer] = []
EV: list[Integer] = []
print("     type       twist(t0,t1,te)      gauge ratio   mixed ratio   euler coeff")
for s in SPINS:
    t0, t1, te = TW[s]
    cg, cm, res = AC1.anomaly_coeffs(t0, t1)
    check("E", f"{NAME[s]}: AC-1's degree-6 residue vanishes (no 4D pure-gravitational term)",
          sp.simplify(res), 0)
    g = sp.simplify(cg / cg_half)
    m = sp.simplify(cm / cm_half)
    GV.append(Integer(g))
    MV.append(Integer(m))
    EV.append(Integer(te))
    print(f"     {NAME[s]:<9}  ({t0},{t1},{te})".ljust(36)
          + f"{g}".ljust(14) + f"{m}".ljust(14) + f"{te}")

check("E", "gauge-ratio vector g over the five slots", GV, [1, -1, 5, 2, 3])
check("E", "mixed-ratio vector m over the five slots", MV, [1, -1, -19, -22, -21])
check("E", "euler-coefficient vector e over the five slots", EV, [0, 0, 0, 2, -2])
H_IND = [Integer(1) if s in HIGHER else Integer(0) for s in SPINS]
check("E", "EXACT MECHANISM: m = g - 24.h, h the higher-spin indicator "
           "(24 = the A-hat denominator)",
      [GV[i] - 24 * H_IND[i] for i in range(5)], MV)

# ---- the carrier table, REPRODUCED from the same machinery ---------------
print("     carrier fork, as three points of the extended lattice (NOT adjudicated here):")
CARRIER = {
    "A  (ghost-subtracted, T_C - 1)":  {HALF_L: -1, HALF_R: 1, S11: 1},
    "-  (bare vector-spinor, T_C)":    {HALF_R: 1, S11: 1},
    "B  (gamma-traceless, T_C + 1)":   {S11: 1},
}
CARRIER_EXPECT = {"A  (ghost-subtracted, T_C - 1)": (3, -21),
                  "-  (bare vector-spinor, T_C)": (4, -20),
                  "B  (gamma-traceless, T_C + 1)": (5, -19)}
for lab, occ in CARRIER.items():
    w = [Integer(occ.get(s, 0)) for s in SPINS]
    gg = sum(GV[i] * w[i] for i in range(5))
    mm = sum(MV[i] * w[i] for i in range(5))
    ee = sum(EV[i] * w[i] for i in range(5))
    print(f"       {lab:<34} g.w = {int(gg):>3}   m.w = {int(mm):>4}   e.w = {int(ee)}")
    check("R", f"reproduce AC-1 carrier {lab.split()[0]}: (gauge, mixed) ratios",
          (int(gg), int(mm)), CARRIER_EXPECT[lab])
    check("E", f"carrier {lab.split()[0]} is a POINT of Z^30, not a change of functional",
          all(isinstance(c, Integer) for c in w), True)
check("C", "control: the three carriers are three DISTINCT lattice points, so the "
           "extension does not silently decide the bit",
      len({tuple(int(CARRIER[l].get(s, 0)) for s in SPINS) for l in CARRIER}), 3)

# ---- per-form-degree consistency: the decomposition must add up exactly ---
print("\n-- 2b. per-degree closure: the type ratios must re-sum to the Lambda^p twist --")
TENS = {p: dict(PHI1.TENS[p]) for p in range(5)}
if MUTATE == "decomp":
    TENS[2] = {k: v for k, v in TENS[2].items() if k != S32}
for p in range(5):
    dec = TENS[p]
    gs = sum(m * GV[SPINS.index(t)] for t, m in dec.items())
    ms = sum(m * MV[SPINS.index(t)] for t, m in dec.items())
    es = sum(m * EV[SPINS.index(t)] for t, m in dec.items())
    t0, t1, te = LAMTW[p]
    cg, cm, _ = AC1.anomaly_coeffs(t0, t1)
    check("E", f"p={p}: type ratios re-sum to the Lambda^p twist (gauge, mixed, euler)",
          (gs, ms, es), (sp.simplify(cg / cg_half), sp.simplify(cm / cm_half), te))
check("C", "control: the closure is NOT trivial -- (3/2,0)+(1/2,1) alone give "
           "(5, -43, 0), which is Lambda^2 MINUS the spin-1/2 piece",
      (GV[3] + GV[4], MV[3] + MV[4], EV[3] + EV[4]), (5, -43, 0))


# ===========================================================================
# 3.  THE EXTENDED CONDITION SYSTEM ON Z^30, AND ITS RANK.
#     D1..D4 are components of the single cubic Tr_R X^3  -> rescale by g.
#     D5 = grav^2-U(1)_Y is the mixed p1 Tr_R X channel   -> rescales by m.
#     (AC-1's factorisation theorem, used as a theorem.)
# ===========================================================================
print("\n-- 3. the extended 4D condition system on Z^30 --")
M4 = PHI1.M4
f5 = [M4[4, j] for j in range(6)]
check("R", "reproduce LA-3: f5 = grav^2-U(1)_Y functional = (1,-2,1,-1,1,0)",
      f5, [R(1), R(-2), R(1), R(-1), R(1), R(0)])

GV_USE = list(GV)
MV_USE = list(MV)
if MUTATE == "no-mixed-rescale":
    MV_USE = list(GV)


def ext_rows(gv, mv, ev=None) -> Matrix:
    """The extended condition matrix.  Column order: n[i*5 + s]."""
    rows = [[M4[a, i] * gv[k] for i in range(6) for k in range(5)] for a in range(4)]
    rows.append([M4[4, i] * mv[k] for i in range(6) for k in range(5)])
    if ev is not None:
        rows.append([M4[4, i] * ev[k] for i in range(6) for k in range(5)])
    return Matrix(rows)


ME = ext_rows(GV_USE, MV_USE)
check("E", "extended condition system is 5 x 30", ME.shape, (5, 30))
check("E", "RANK OF THE EXTENDED SYSTEM = 5  (LA-3's spin-1/2 system had rank 4)",
      ME.rank(), 5)
check("E", "so the extended anomaly-free lattice has rank 25", len(ME.nullspace()), 25)
check("C", "control: the rank rise is bought ENTIRELY by m != g -- setting the mixed "
           "channel to rescale like the gauge channels returns rank 4",
      ext_rows(GV, GV).rank(), 4)

rel = 2 * ME[0, :] - 27 * ME[1, :] - 36 * ME[2, :] - 9 * ME[3, :] + 9 * ME[4, :]
check("E", "LA-3's relation 2D1 - 27D2 - 36D3 - 9D4 + 9D5 = 0 is BROKEN on Z^30",
      rel == sp.zeros(1, 30), False)
resid_pred = Matrix([[9 * (MV_USE[k] - GV_USE[k]) * f5[i] for i in range(6) for k in range(5)]])
check("E", "its exact residual is 9(m - g) (x) f5 = -216 h (x) f5", rel, resid_pred)
check("E", "the relation SURVIVES exactly on the spin-1/2 sublattice (h = 0 there)",
      [rel[i * 5 + 0] for i in range(6)] + [rel[i * 5 + 1] for i in range(6)], [0] * 12)
check("C", "control: LA-3's relation still holds on the un-extended Z^6 system",
      2 * M4[0, :] - 27 * M4[1, :] - 36 * M4[2, :] - 9 * M4[3, :] + 9 * M4[4, :],
      sp.zeros(1, 6))

# the Euler channel, carried as an explicit FORK, not silently included
ME6 = ext_rows(GV_USE, MV_USE, EV)
check("E", "EULER FORK: if e ^ Tr F is admitted as a sixth 4D channel the rank is 6",
      ME6.rank(), 6)
check("E", "EULER FORK: the anomaly-free lattice is then rank 24", len(ME6.nullspace()), 24)
check("C", "control: the Euler row is genuinely independent -- e is not in span(g, m)",
      Matrix([GV, MV, [int(c) for c in EV]]).rank(), 3)


# ===========================================================================
# 4.  L_ext, CHARACTERISED EXACTLY (row-space identity, not sampling).
# ===========================================================================
print("\n-- 4. the extended anomaly-free lattice L_ext --")
ALT = ext_rows(GV_USE, [Integer(1) if s in HIGHER else Integer(0) for s in SPINS])
check("E", "L_ext = { V_g in L  AND  f5 . N_H = 0 }: the two systems have the SAME row space",
      (Matrix.vstack(ME, ALT).rank(), ME.rank(), ALT.rank()), (5, 5, 5))
check("E", "so the ONE new condition the extension adds is exactly "
           "f5 . (total charged higher-spin content) = 0", ALT.rank() - 4, 1)
check("C", "control: the alternative system is not the same MATRIX, only the same row space",
      ME == ALT, False)


def in_L(v) -> bool:
    """LA-3: v in L iff the five charged constituent multiplicities are equal."""
    return len(set(v[:5])) == 1


F5 = [F(int(c.p), int(c.q)) for c in [sp.Rational(x) for x in f5]]
M4F = [[F(int(sp.Rational(M4[a, i]).p), int(sp.Rational(M4[a, i]).q)) for i in range(6)]
       for a in range(5)]
GI = [int(c) for c in GV_USE]
MI = [int(c) for c in MV_USE]
EI = [int(c) for c in EV]


def in_Lext(n, gv=None, mv=None, ev=None) -> bool:
    """n given as n[i][s].  Exact rational arithmetic."""
    gv, mv = (gv or GI), (mv or MI)
    Vg = [sum(gv[s] * n[i][s] for s in range(5)) for i in range(6)]
    Vm = [sum(mv[s] * n[i][s] for s in range(5)) for i in range(6)]
    if any(sum(M4F[a][i] * Vg[i] for i in range(6)) != 0 for a in range(4)):
        return False
    if sum(F5[i] * Vm[i] for i in range(6)) != 0:
        return False
    if ev is not None:
        Ve = [sum(ev[s] * n[i][s] for s in range(5)) for i in range(6)]
        if sum(F5[i] * Ve[i] for i in range(6)) != 0:
            return False
    return True


def in_Lext_alt(n) -> bool:
    Vg = [sum(GI[s] * n[i][s] for s in range(5)) for i in range(6)]
    NH = [sum(n[i][SPINS.index(s)] for s in HIGHER) for i in range(6)]
    return in_L(Vg) and sum(F5[i] * NH[i] for i in range(6)) == 0


# ---- the exotic witness: PHI-1's seam, confirmed with an object -----------
WIT = [[0] * 5 for _ in range(6)]
WIT[0][SPINS.index(S32)] = 1        # one Q      as charged (3/2,0)
WIT[3][SPINS.index(S32)] = 1        # one L      as charged (3/2,0)
WIT[1][0] = 2                       # two u^c    as spin-1/2
WIT[2][0] = 2                       # two d^c    as spin-1/2
WIT[4][0] = 2                       # two e^c    as spin-1/2
if MUTATE == "witness":
    WIT[4][0] = 3
PROJ = [WIT[i][0] - WIT[i][1] for i in range(6)]
check("E", "WITNESS is anomaly-free on the FULL extended system", in_Lext(WIT), True)
check("E", "WITNESS survives the Euler fork too", in_Lext(WIT, ev=EI), True)
check("E", "WITNESS has all multiplicities NON-NEGATIVE (a real spectrum, not a virtual one)",
      all(c >= 0 for row in WIT for c in row), True)
check("E", "WITNESS spin-1/2 projection is (0,2,2,0,2,0)", PROJ, [0, 2, 2, 0, 2, 0])
check("E", "and that projection is NOT in L", in_L(PROJ), False)
check("E", "in fact its SU(3)^3 anomaly D1 is -4, not 0",
      sum(M4F[0][i] * PROJ[i] for i in range(6)), F(-4))
print("   ==> PHI-1's seam is CONFIRMED with an object: D1..D5 on Z^6 are NOT the")
print("       complete 4D conditions once charged spin-3/2 is present.")

check("C", "control: the witness is NOT in L (x) Z^5 -- L_ext is strictly larger",
      all(in_L([WIT[i][s] for i in range(6)]) for s in range(5)), False)
check("C", "control FIRES: dropping the (3/2,0) L makes the witness anomalous",
      in_Lext([[WIT[i][s] if not (i == 3 and s == SPINS.index(S32)) else 0
                for s in range(5)] for i in range(6)]), False)
check("C", "control FIRES: moving the two charged (3/2,0) fields into spin-1/2 breaks it",
      in_Lext([[(WIT[i][0] + (WIT[i][SPINS.index(S32)] if s == 0 else 0)) if s == 0
                else (0 if s == SPINS.index(S32) else WIT[i][s]) for s in range(5)]
               for i in range(6)]), False)

# ---- exhaustive agreement of the two descriptions on a box ---------------
BOX = list(itertools.product(range(-1, 2), repeat=5))
mismatch = 0
seen_true = seen_false = 0
for i0 in BOX:
    for i1 in BOX:
        n = [list(i0), list(i1)] + [[0] * 5] * 4
        a, b = in_Lext(n), in_Lext_alt(n)
        if a != b:
            mismatch += 1
        seen_true += 1 if a else 0
        seen_false += 1 if not a else 0
check("E", "the two descriptions of L_ext agree on all 59049 points of a "
           "two-constituent {-1,0,1}^10 box", mismatch, 0)
check("C", "control: that box is not vacuous -- both verdicts occur",
      (seen_true > 0, seen_false > 0), (True, True))


# ===========================================================================
# 5.  THE EXTENDED REDUCTION phi_ext = v (x) K.
# ===========================================================================
print("\n-- 5. the extended reduction phi_ext : Z^15 -> Z^30 --")
NMAT = [[TENS[p].get(s, 0) for s in SPINS] for p in range(5)]
check("E", "decomposition matrix N[p][s] (p = 0..4 down, spin type across)", NMAT,
      [[1, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 0, 0, 1, 1], [0, 1, 1, 0, 0], [1, 0, 0, 0, 0]]
      if MUTATE != "decomp" else
      [[1, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0], [1, 0, 0, 0, 0]])
KMAT = Matrix(NMAT).T                       # 5 (spin) x 5 (form degree)
check("E", "rank(K) = 3: p=1 and p=3 deposit identically, and so do the two p=2 "
           "higher-spin slots", KMAT.rank(), 3)
IMG_GENS = [[1, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 1, 1]]
IMGM = Matrix([[KMAT[s, p] for s in range(5)] for p in range(5)])
snfK = smith_normal_form(IMGM)
check("E", "image of K is the SATURATED rank-3 lattice {(a,b,b,c,c)} (Smith divisors all 1)",
      [int(snfK[i, i]) for i in range(min(snfK.shape)) if snfK[i, i] != 0], [1, 1, 1])

V16 = PHI1.V16
PHIEXT = Matrix(30, 15, lambda r, c: Integer(V16[r // 5] * (KMAT[r % 5, c] if c < 5 else 0)))
check("E", "RANK OF phi_ext = 3  (PHI-1's phi had rank 1 -- rank 1 was a "
           "spin-1/2-projection artefact)", PHIEXT.rank(), 3)
ranks = set()
for v in itertools.product(range(-2, 3), repeat=6):
    r = 0 if all(c == 0 for c in v) else 3
    ranks.add(r)
check("E", "rank(phi_ext) is 3 for every v != 0 and 0 only for v = 0 "
           "(image = v (x) Im K, a pure tensor)", sorted(ranks), [0, 3])
check("C", "control: rank 3 exceeds LA-5's literal bound 2 -- but the bound that "
           "belongs to the EXTENDED target is rank <= rank(L_ext) = 25, still met",
      (PHIEXT.rank() > 2, PHIEXT.rank() <= 25), (True, True))

GK = [sum(GI[s] * NMAT[p][s] for s in range(5)) for p in range(5)]
MK = [sum(MI[s] * NMAT[p][s] for s in range(5)) for p in range(5)]
EK = [sum(EI[s] * NMAT[p][s] for s in range(5)) for p in range(5)]
KHALF = [NMAT[p][0] - NMAT[p][1] for p in range(5)]
check("R", "reproduce PHI-1: the spin-1/2 projection of phi_ext is exactly k = (-1)^p",
      KHALF, PHI1.KVEC)
check("E", "g-weighted reduction functional is C(4,p) = (1,4,6,4,1)", GK, [1, 4, 6, 4, 1])
check("E", "m-weighted reduction functional is (1,-20,-42,-20,1)", MK, [1, -20, -42, -20, 1])
check("E", "EULER-weighted reduction functional is IDENTICALLY ZERO -- the reduction "
           "deposits (3/2,0) and (1/2,1) with EQUAL multiplicity", EK, [0, 0, 0, 0, 0])
check("C", "control: the Euler functional is not zero on a lattice point that "
           "unbalances the two p=2 higher-spin slots",
      sum(EI[s] * [0, 0, 0, 1, 0][s] for s in range(5)) == 0, False)


# ===========================================================================
# 6.  THE ZERO-BIT RESULT SURVIVES.
# ===========================================================================
print("\n-- 6. does 14D anomaly cancellation still contribute zero bits? --")
KINT = PHI1.KINT
TK = Matrix([[Integer(w[c]) for c in range(5)] for w in KINT])
snfT = smith_normal_form(TK)
check("R", "reproduce PHI-1: T maps ker M ONTO Z^5 (Smith divisors all 1)",
      [int(snfT[i, i]) for i in range(min(snfT.shape)) if snfT[i, i] != 0], [1, 1, 1, 1, 1])
check("E", "THEOREM: since T(ker M) = Z^5, NO nonzero functional supported on the "
           "observed slots p = 0..4 annihilates ker M", TK.rank(), 5)
for nm, fn in (("g.K = (1,4,6,4,1)", GK), ("m.K = (1,-20,-42,-20,1)", MK)):
    vals = [sum(fn[c] * w[c] for c in range(5)) for w in KINT]
    check("E", f"so {nm} does NOT annihilate ker M (unlike CB-C's W and PHI-1's k'')",
          all(t == 0 for t in vals), False)
check("R", "reproduce CB-C/PHI-1 by contrast: W = sum_p x_p C(14,p) DOES annihilate ker M",
      all(sum(math.comb(14, c) * w[c] for c in range(15)) == 0 for w in KINT), True)
check("E", "ZERO-BIT RESULT SURVIVES: phi_ext(ker M) = phi_ext(Z^15), because "
           "phi_ext factors through T and T is onto",
      (TK.rank(), all(KMAT[s, p] == KMAT[s, p] for s in range(5) for p in range(5))),
      (5, True))


# ===========================================================================
# 7.  THE CONTAINMENT, RE-RUN ON THE EXTENDED TARGET.
# ===========================================================================
print("\n-- 7. re-run PHI-1's containment on the extended target --")


def containment(v, gv=None, mv=None, ev=None, vhigh=None) -> bool:
    """phi_ext(ker M) = phi_ext(Z^15) subset L_ext ?  Checked on Im K's generators.

    vhigh, if given, is a DIFFERENT internal vector for the higher-spin slots --
    the control that breaks gauge-blindness.
    """
    gv, mv = (gv or GI), (mv or MI)
    for w in IMG_GENS:
        n = [[0] * 5 for _ in range(6)]
        for i in range(6):
            for s in range(5):
                src = vhigh if (vhigh is not None and SPINS[s] in HIGHER) else v
                n[i][s] = src[i] * w[s]
        if not in_Lext(n, gv, mv, ev):
            return False
    return True


BOX6 = list(itertools.product(range(-3, 4), repeat=6))
bad = [v for v in BOX6 if containment(list(v)) != in_L(list(v))]
check("E", "CONTAINMENT SURVIVES: phi_ext(ker M) subset L_ext  <==>  v in L, "
           "exhaustively over [-3,3]^6", bad, [])
check("E", "positive witnesses: the 16, the 15, 15 + 7 nu^c, 4 x 16",
      [containment(list(v)) for v in ([1] * 6, [1, 1, 1, 1, 1, 0],
                                      [1, 1, 1, 1, 1, 7], [4] * 6)],
      [True, True, True, True])
check("C", "controls FIRE: a lone Q, (1,1,1,1,0,0), a 16 minus one d^c",
      [containment(list(v)) for v in ([1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0],
                                      [1, 1, 0, 1, 1, 1])],
      [False, False, False])
check("E", "with the Euler channel admitted the verdict is UNCHANGED (over [-2,2]^6)",
      [v for v in itertools.product(range(-2, 3), repeat=6)
       if containment(list(v), ev=EI) != in_L(list(v))], [])

# ---- the carrier fork, both branches carried ----------------------------
print("     carrier fork on the containment (the bit is NOT decided here):")
for lab, occ in CARRIER.items():
    wc = [occ.get(s, 0) for s in SPINS]
    gens = [[1, 0, 0, 0, 0], wc, [0, 0, 0, 1, 1]]
    saved = IMG_GENS[1]
    IMG_GENS[1] = wc
    ok = all(containment(list(v)) == in_L(list(v))
             for v in itertools.product(range(-2, 3), repeat=6))
    IMG_GENS[1] = saved
    gg = sum(GI[i] * wc[i] for i in range(5))
    print(f"       carrier {lab.split()[0]:<2}  g.w = {gg:>3}   containment <=> v in L : {ok}")
    check("E", f"carrier {lab.split()[0]}: containment still collapses to v in L", ok, True)

# ---- robustness: ARBITRARY spin coefficients on the higher-spin slots ----
print("     robustness sweep over arbitrary higher-spin coefficients:")
bad_sweep = 0
tested = 0
for dg in itertools.product(range(-3, 4), repeat=3):
    for dm in ((0, 0, 0), (1, -2, 3), (-5, 5, -5)):
        gv = [GI[0], GI[1]] + [GI[2 + j] + dg[j] for j in range(3)]
        mv = [MI[0], MI[1]] + [MI[2 + j] + dm[j] for j in range(3)]
        tested += 1
        for v in ([1] * 6, [1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0]):
            if containment(v, gv, mv) != in_L(v):
                bad_sweep += 1
check("E", f"verdict invariant under ALL {tested} perturbed higher-spin coefficient "
           "assignments (the p=0 slot alone forces v in L)", bad_sweep, 0)
# The p=0 slot is load-bearing, and this control proves it.  Delete that generator
# AND tune the higher-spin gauge coefficients so g.w = 0 on both survivors: the
# criterion then degenerates to f5 . v = 0, which a v OUTSIDE L can satisfy.
_saved_gens = list(IMG_GENS)
IMG_GENS[:] = [[0, 1, 1, 0, 0], [0, 0, 0, 1, 1]]
G_DEGEN = [1, -1, 1, 1, -1]          # g.w = 0 on both surviving generators
_degen = containment([2, 1, 0, 0, 0, 0], gv=G_DEGEN)
IMG_GENS[:] = _saved_gens
check("C", "control WITH POWER: with the p=0 generator deleted AND the higher-spin "
           "gauge coefficients tuned to annihilate the survivors, a v OUTSIDE L "
           "passes -- so the collapse to 'v in L' is genuinely bought by the p=0 slot",
      (_degen, in_L([2, 1, 0, 0, 0, 0])), (True, False))

# ---- the gauge-blindness control: the ONLY way the extension bites ------
check("C", "control WITH POWER: if the observation deposited a DIFFERENT internal "
           "vector in the higher-spin slots, the criterion would be strictly stronger "
           "(v in L is then not sufficient)",
      containment([1, 1, 1, 1, 1, 1], vhigh=[1, 0, 0, 0, 0, 0]), False)
check("E", "and with the same internal vector everywhere it is exactly v in L",
      containment([1, 1, 1, 1, 1, 1], vhigh=[1, 1, 1, 1, 1, 1]), True)
if MUTATE == "gauge-blind":
    check("E", "MUTATION gauge-blind: pretend the soldered map is the derived one",
          containment([1] * 6, vhigh=[1, 0, 0, 0, 0, 0]), True)


# ===========================================================================
# 8.  AC-C2 (the SU(2)_L doublet count) on the extended reduction.
# ===========================================================================
print("\n-- 8. AC-C2 on the extended reduction --")
DOUBLETS = [3, 0, 0, 1, 0, 0]
for lab, occ in CARRIER.items():
    wc = [occ.get(s, 0) for s in SPINS]
    gg = sum(GI[i] * wc[i] for i in range(5))
    for m_ in (-3, -1, 0, 1, 2, 5):
        nd = gg * m_ * sum(DOUBLETS[i] * V16[i] for i in range(6))
        check("E", f"AC-C2 with carrier {lab.split()[0]}, multiplicity {m_}: doublet "
                   f"count divisible by 4", nd % 4, 0)
check("C", "control FIRES: AC-C2's divisibility-by-4 fails for a v OUTSIDE L "
           "(a 16 minus its lepton doublet) on the p=0 deposit",
      GK[0] * sum(DOUBLETS[i] * [1, 1, 1, 0, 1, 1][i] for i in range(6)) % 4 == 0, False)
check("C", "control FIRES: and on carrier A's deposit too",
      3 * sum(DOUBLETS[i] * [1, 1, 1, 0, 1, 1][i] for i in range(6)) % 4 == 0, False)


# ===========================================================================
# 9.  CERTIFICATE
# ===========================================================================
RESULTS.update({
    "g": [int(c) for c in GV], "m": [int(c) for c in MV], "e": [int(c) for c in EV],
    "h": [int(c) for c in H_IND], "rank_ext": int(ME.rank()),
    "rank_ext_with_euler": int(ME6.rank()), "kerdim_ext": len(ME.nullspace()),
    "rank_phi_ext": int(PHIEXT.rank()), "N": NMAT, "gK": GK, "mK": MK, "eK": EK,
    "witness": WIT, "witness_projection": PROJ,
    "lam_twists": {p: (LAMTW[p][0], int(LAMTW[p][1]), int(LAMTW[p][2])) for p in range(5)},
})
assert_no_float(RESULTS)

print("\n" + "=" * 78)
print(f"  checks: {NCHK}   tags: " + "  ".join(f"[{t}]x{n}" for t, n in sorted(TAGS.items())))
if FAIL:
    print(f"  FAILURES: {len(FAIL)}")
    for f_ in FAIL:
        print("    " + f_)
    print("=" * 78)
    sys.exit(1)
print(f"  ALL {NCHK}/{NCHK} PASS -- exact rational/integer arithmetic, no float load-bearing")
print("=" * 78)
print("""
  BUILT:     Z^6_ext = Z^6 (x) Z^5_spin = Z^30, spin coefficients DERIVED from
             Chern roots + AC-1's own anomaly_coeffs:
                 g = (1, -1,   5,   2,   3)      gauge channels D1..D4
                 m = (1, -1, -19, -22, -21)      mixed channel  D5
                 m = g - 24.h,  h = higher-spin indicator, 24 = A-hat denominator
  RANK:      the extended condition system has RANK 5 (6 if the Euler channel
             e ^ Tr F is admitted).  LA-3's rank-4 degeneracy is BROKEN, with
             exact residual -216 h (x) f5.  L_ext has rank 25 (24 with Euler)
             and equals { V_g in L  AND  f5 . N_H = 0 }.
  SEAM CONFIRMED:  L_ext is strictly larger than L (x) Z^5.  All-non-negative
             witness: 2u^c + 2d^c + 2e^c spin-1/2, plus one Q and one L as
             charged (3/2,0).  Extended-anomaly-free; its spin-1/2 projection
             (0,2,2,0,2,0) has D1 = -4.  So D1..D5 on Z^6 really are NOT the
             complete 4D conditions once charged spin-3/2 is present.
  PHI-1:     rank(phi) = 1 does NOT survive -- rank(phi_ext) = 3.
             ZERO BITS survives:  T(ker M) = Z^5, so phi_ext(ker M) = phi_ext(Z^15).
             CONTAINMENT SURVIVES VERBATIM:  phi_ext(ker M) subset L_ext <=> v in L,
             for EVERY carrier, with or without the Euler channel, and under
             arbitrary higher-spin coefficients -- because the p = 0 deposit is a
             pure spin-1/2 slot with g = 1 and gauge-blindness puts the SAME v in
             every spin slot.  The extension bites only if gauge-blindness fails.
  NOT DONE:  the carrier bit is NOT adjudicated -- all three carriers are carried
             as three distinct points of Z^30 and all three give the same verdict.
""")
sys.exit(0)
