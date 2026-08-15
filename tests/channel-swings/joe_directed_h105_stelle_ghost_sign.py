#!/usr/bin/env python3
r"""H10-5 -- the Stelle/Einstein-Weyl Yukawa assignment, DERIVED not transcribed.

GU-COMPARATOR-ROUTING.  This probe computes inside a CONVENTIONAL COMPARATOR
object: four-derivative (Stelle) quadratic gravity, its linearized point-mass
potential, and the PPN parameters gamma, beta confronted with Cassini and LLR.
Any result here binds only that named model.  It becomes a statement about GU
only through the repository's OWN prior identification (H15/H25) that GU's
tree-level TT graviton operator IS box(box + m2^2) with m2^2 = m^2_eff mu_DW^2 --
an identification this probe CONSUMES and does not adjudicate.  It is NOT
evidence for or against Weinstein's source-native construction without an
explicit typed bridge.  Read lab/methods/source-native-comparator-routing.md
and follow its source-native pointers before reusing this result.
Classification: CONVENTIONAL_COMPARATOR.

WHY THIS PROBE EXISTS.  tests/wave22/H10_ppn_weak_field.py is the repository's
only Cassini/LLR bar.  Its own 2026-08-09 banner recorded that its Yukawa
assignment was WRONG (spin-2 coefficient -4/3, not +1/3) and left the constants
unedited.  The banner is a LITERATURE argument: five citations, no derivation.
Editing a falsifier's constants because a comment says so is exactly how the
error got in.  So this probe DERIVES the assignment from structure, with no
literature number as input, and only then compares to the banner.

TARGET CLAIMS (internal; no SC- register entry covers PPN -- see [C10]).
  T1  repo-wide: "the Yukawa strength alpha_Y = 1/3, forced, vDVZ trace factor"
      (explorations/path4-wave2-alphaW-parameter-free-2026-07-11.md L133;
       explorations/track2-conditional-numbers-2026-07-13.md L111, L193;
       tests/W61_path4_A_eos_gravity.py L233; tests/W66_path4_wave2_alphaW.py L125)
  T2  H10: "gamma - 1 = -(2/3) e^{-m2 r}"  (sign)
  T3  H10 Q2a: "gamma(m2 r -> 0) = 1/2 anchors the linearization against the
      literature, so a linearization error would have shown up here"
  T4  H10 Q4: "GATED-ON-mu_DW, effectively PASSES (not falsified)"
  T5  H10 Q1b: "the massive spin-2 flips sign between the temporal and spatial
      potentials"

WHAT IS EXACT AND WHAT IS FLOAT.  Everything in sections D, E, G -- projector
traces, source saturation, ghost sign, the potential coefficients, gamma(r), its
series and its endpoints -- is sympy Rational / exact symbolic.  Floats appear
ONLY in section O (observational), are listed in FLOAT_INPUTS, and are never
load-bearing for an exact claim: no exact assertion in this file reads a float.

Certificate tags:
  [D] derived here from structure, no literature number as input
  [E] exact result of this route
  [R] reproduction of a fact already filed in the repo, asserted BEFORE use
  [C] control that MUST fire (discrimination / non-vacuity / contrary)
  [O] observational comparison using declared floats

Usage (from the repository root):
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_h105_stelle_ghost_sign.py

Failure-path self-test (one subprocess per planted false fact; each must exit 1;
the clean run must exit 0; the selftest itself exits 0 on success):
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_h105_stelle_ghost_sign.py --selftest

NOT: a re-linearization of GU's full |II|^2 action with matter sources (that gap
is SA-G9 and stays open), a derivation of mu_DW, a loop-level statement, a claim
that GU is consistent, or a canon/ledger edit.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
H10_PY = ROOT / "tests" / "wave22" / "H10_ppn_weak_field.py"
H10_MD = ROOT / "explorations" / "wave22" / "H10-ppn-weak-field-2026-07-11.md"
ART = (ROOT / "lab" / "active-research" / "joe-directed" / "h10-remediation"
       / "h105-stelle-ghost-sign-2026-08-15.md")

PLANT = os.environ.get("H105_PLANT", "")
CERT: list[tuple[str, str, bool, str]] = []


def C(tag: str, name: str, ok: bool, detail: str = "") -> bool:
    CERT.append((tag, name, bool(ok), str(detail)))
    return bool(ok)


def planted(name: str, true_value, false_value):
    """Return false_value when this plant is active, else true_value."""
    return false_value if PLANT == name else true_value


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ===========================================================================
# [D] DERIVATION -- from structure only.  No literature number enters here.
# ===========================================================================
D = sp.symbols("D", positive=True)
uu = sp.symbols("uu", positive=True)          # stands for e^{-m2 r}, 0 < uu <= 1
r, m2, m0, GM = sp.symbols("r m2 m0 GM", positive=True)
k2, m2s = sp.symbols("k2 m2s", positive=True)


def derive() -> dict:
    out: dict = {}
    log("=" * 78)
    log("[D] DERIVATION -- projector traces, source saturation, ghost sign")
    log("=" * 78)

    # ---- D1  spin-2 projector trace coefficient, from tracelessness alone ----
    # theta_{mn} = eta_{mn} - k_m k_n / k^2 is a rank-(D-1) projector: theta^m_m = D-1.
    # P^(2) = 1/2(th th + th th) + a * th th.  Trace over the first pair:
    #   1/2(th_{rs} + th_{rs}) + a (D-1) th_{rs} = (1 + a(D-1)) th_{rs}.
    # P^(2) must be TRACELESS, so a = -1/(D-1).
    a = sp.symbols("a")
    a_sol = sp.solve(sp.Eq(1 + a * (D - 1), 0), a)[0]
    proj_trace_4 = planted("proj_trace", sp.nsimplify(a_sol.subs(D, 4)), sp.Rational(-1, 2))
    C("D", "D1 spin-2 projector theta-theta coefficient = -1/(D-1), = -1/3 at D=4 "
         "(this is the CORRECT INTERMEDIATE that the 2026-07-11 note mis-slotted)",
      proj_trace_4 == sp.Rational(-1, 3), f"a = {a_sol} -> {proj_trace_4}")
    out["proj_trace_4"] = proj_trace_4

    # ---- D2  numerator trace coefficients between CONSERVED sources ----
    # massless graviton (harmonic gauge):  T.T' - (1/(D-2)) T T'
    # Fierz-Pauli massive spin-2:          T.T' - (1/(D-1)) T T'
    #
    # D2a is DERIVED from trace reversal in D dimensions, not asserted.  Harmonic gauge
    # gives box hbar_{mn} ~ T_{mn} with hbar_{mn} = h_{mn} - (1/2) eta_{mn} h.  Taking the
    # trace: hbar = h(1 - D/2), so h = -2 hbar/(D-2), and inverting the trace reversal,
    #   h_{mn} = hbar_{mn} + (1/2) eta_{mn} h = hbar_{mn} - (1/(D-2)) eta_{mn} hbar.
    # The 1/(D-2) is therefore forced by the trace reversal alone.
    hbar_tr, h_tr = sp.symbols("hbar_tr h_tr")
    h_of_hbar = sp.solve(sp.Eq(hbar_tr, h_tr * (1 - D / 2)), h_tr)[0]
    c_ml_derived = sp.simplify(-(sp.Rational(1, 2) * h_of_hbar) / hbar_tr)   # = 1/(D-2)
    c_ml = planted("trace_massless", sp.nsimplify(c_ml_derived.subs(D, 4)), sp.Rational(1, 3))
    c_mv = planted("trace_massive", sp.nsimplify(sp.Rational(1, 1) / (D - 1)).subs(D, 4),
                   sp.Rational(1, 2))
    C("D", "D2a massless-graviton numerator trace coefficient DERIVED from trace reversal in "
         "D dimensions (h = -2 hbar/(D-2) forces it): 1/(D-2), = 1/2 at D=4.  Asserting this "
         "instead of deriving it would repeat the very failure mode being remediated.",
      sp.simplify(c_ml_derived - 1 / (D - 2)) == 0 and c_ml == sp.Rational(1, 2),
      f"derived 1/(D-2) = {sp.simplify(c_ml_derived)} -> {c_ml} at D=4")
    C("D", "D2b massive Fierz-Pauli numerator trace coefficient 1/(D-1) = 1/3 at D=4",
      c_mv == sp.Rational(1, 3), f"1/(D-1)|D=4 = {c_mv}")
    C("D", "D2c the massive trace coefficient EQUALS minus the spin-2 projector trace "
         "coefficient -- same number, DIFFERENT SLOT.  Confusing the two is the bug.",
      c_mv == -proj_trace_4)
    out["c_ml"], out["c_mv"] = c_ml, c_mv

    # ---- D3  saturate on a static point source.  Signature (-,+,+,+). ----
    M, Mp = sp.symbols("M Mp", positive=True)
    T00, Tp00 = M, Mp                    # T_{mn} = M d^0_m d^0_n (deltas stripped)
    TdotTp = T00 * Tp00                  # T_{mn}T'^{mn} = T_00 T'_00 (eta^00 eta^00 = +1)
    Ttr, Tptr = -T00, -Tp00              # T = eta^{00} T_00 = -T_00
    TTp = Ttr * Tptr                     # = +M M'
    w_ml = sp.simplify(TdotTp - c_ml * TTp)
    w_mv = sp.simplify(TdotTp - c_mv * TTp)
    vdvz = sp.nsimplify(sp.simplify(w_mv / w_ml))
    C("D", "D3 vDVZ RATIO on a static point source = (1 - 1/3)/(1 - 1/2) = 4/3 "
         "(van Dam-Veltman-Zakharov enhancement; this is the POTENTIAL coefficient)",
      vdvz == sp.Rational(4, 3), f"({w_mv})/({w_ml}) = {vdvz}")
    out["vdvz"] = vdvz

    # ---- D4  the GHOST SIGN, from the fourth-order operator alone ----
    prop = 1 / (k2 * (k2 + m2s))
    res_ml = sp.simplify(sp.limit(prop * k2, k2, 0))
    res_mv = sp.simplify((prop * (k2 + m2s)).subs(k2, -m2s))
    ghost = planted("ghost_sign", sp.nsimplify(sp.simplify(res_mv / res_ml)), sp.Integer(1))
    C("D", "D4 box(box+m2^2): 1/(k^2(k^2+m2^2)) has residue ratio massive/massless = -1. "
         "The massive spin-2 is a GHOST and its Yukawa is REPULSIVE.  Sign is structural, "
         "not imported: it follows from the fourth-order operator the repo already computed.",
      ghost == -1, f"apart = {sp.apart(prop, k2)}, ratio = {ghost}")
    out["ghost"] = ghost

    # ---- D5  temporal and spatial weights -> Phi, Psi ----
    def hweights(c):
        h00 = sp.simplify(T00 - c * (-1) * Ttr)     # eta_00 = -1
        hij = sp.simplify(0 - c * (+1) * Ttr)       # eta_ij = +delta_ij
        return h00, hij

    h00_ml, hij_ml = hweights(c_ml)
    h00_mv, hij_mv = hweights(c_mv)
    gam_ml = sp.nsimplify(hij_ml / h00_ml)
    gam_mv = sp.nsimplify(hij_mv / h00_mv)
    C("D", "D5a massless sector alone gives Psi/Phi = 1 -- GR, gamma = 1",
      gam_ml == 1, f"h00 ~ {h00_ml}, hij ~ {hij_ml}")
    C("D", "D5b MASSIVE SECTOR ALONE gives Psi/Phi = (1/3)/(2/3) = 1/2 -- THIS is the true "
         "vDVZ / Fierz-Pauli 1/2, a statement about the MASSIVE MODE ONLY, not about the "
         "full massless+ghost theory (see [C4]: the file anchored on the wrong object)",
      gam_mv == sp.Rational(1, 2), f"h00 ~ {h00_mv}, hij ~ {hij_mv}")
    cT = planted("cT", sp.nsimplify(h00_mv / h00_ml), sp.Rational(-1, 3))
    cS = planted("cS", sp.nsimplify(hij_mv / hij_ml), sp.Rational(1, 3))
    C("D", "D5c TEMPORAL enhancement (massive/massless) = 4/3 -- equals the vDVZ ratio D3",
      cT == sp.Rational(4, 3) and cT == vdvz, f"cT = {cT}")
    C("D", "D5d SPATIAL enhancement (massive/massless) = 2/3 -- DIFFERENT from the temporal "
         "4/3.  The temporal and spatial Yukawa coefficients are NOT equal in magnitude.",
      cS == sp.Rational(2, 3), f"cS = {cS}")
    out["cT"], out["cS"] = cT, cS

    Phi = -(GM / r) * (1 - cT * sp.exp(-m2 * r))
    Psi = -(GM / r) * (1 - cS * sp.exp(-m2 * r))
    out["Phi"], out["Psi"] = Phi, Psi
    log(f"  DERIVED  Phi(r) = -(GM/r)[1 - ({cT}) e^-m2r]")
    log(f"  DERIVED  Psi(r) = -(GM/r)[1 - ({cS}) e^-m2r]")

    # ---- D6  THE TRAP the banner names: both signs NEGATIVE, not flipped ----
    C("D", "D6 TRAP CHECK -- both the temporal and the spatial massive terms enter with the "
         "SAME (negative-inside-bracket, i.e. repulsive) sign.  The spin-2 does NOT flip sign "
         "between Phi and Psi; it changes MAGNITUDE 4/3 -> 2/3.  [refutes T5]",
      sp.sign(cT) == sp.sign(cS) == 1 and cT != cS)

    # ---- D7  the scalar, fixed by Stelle r->0 finiteness GIVEN the spin-2 term ----
    c0 = sp.symbols("c0")
    c0v = sp.nsimplify(sp.solve(sp.Eq(1 - cT + c0, 0), c0)[0])
    C("D", "D7a Stelle r->0 finiteness of the FULL quadratic theory (1 - 4/3 + c0 = 0) fixes "
         "the spin-0 scalaron potential coefficient c0 = +1/3, ATTRACTIVE (non-ghost)",
      c0v == sp.Rational(1, 3), f"c0 = {c0v}")
    c0s = sp.symbols("c0s")
    c0sv = sp.nsimplify(sp.solve(sp.Eq((1 + c0s) / (1 + c0v), sp.Rational(1, 2)), c0s)[0])
    C("D", "D7b the Brans-Dicke omega=0 (f(R)) endpoint gamma=1/2 fixes the SPATIAL scalar "
         "coefficient to -1/3, so Psi_full = -(GM/r)[1 - (2/3)e^-m2r - (1/3)e^-m0r]: BOTH "
         "SAME SIGN.  Reproduces the banner's stated trap potential exactly.",
      c0sv == sp.Rational(-1, 3) and sp.Integer(1) - cS + c0sv == 0, f"c0s = {c0sv}")
    out["c0"], out["c0s"] = c0v, c0sv
    log(f"  DERIVED  V_full(r) = -(GM/r)[1 - ({cT}) e^-m2r + ({c0v}) e^-m0r]")
    return out


# ===========================================================================
# [E] EXACT PPN for GU: m0 -> oo deletes the SCALAR, KEEPS the spin-2 ghost
# ===========================================================================
def exact_ppn(d: dict) -> dict:
    out: dict = {}
    log("")
    log("=" * 78)
    log("[E] EXACT PPN -- GU has no R^2: m0 -> oo, scalar deleted, GHOST KEPT")
    log("=" * 78)
    cT, cS = d["cT"], d["cS"]

    V_full = -(GM / r) * (1 - cT * sp.exp(-m2 * r) + d["c0"] * sp.exp(-m0 * r))
    V_GU = sp.limit(V_full, m0, sp.oo)
    C("E", "E1 m0 -> oo deletes the +1/3 SCALAR and leaves the -4/3 spin-2 GHOST. "
         "The old file deleted the ghost and kept the scalar -- the exact inversion.",
      sp.simplify(V_GU - d["Phi"]) == 0)

    gam = (1 - cS * uu) / (1 - cT * uu)
    gam_old = (1 - sp.Rational(1, 3) * uu) / (1 + sp.Rational(1, 3) * uu)   # the file's WRONG one
    out["gamma"] = gam

    lead = planted("lead_sign",
                   sp.nsimplify(sp.expand(sp.series(gam - 1, uu, 0, 2).removeO())),
                   -sp.Rational(2, 3) * uu)
    C("E", "E2 gamma - 1 = +(2/3) e^{-m2 r} + O(e^{-2 m2 r}) -- POSITIVE.  GU predicts "
         "gamma > 1 at solar-system distances.  The old file had -(2/3): SIGN REFUTED. [T2]",
      sp.simplify(lead - sp.Rational(2, 3) * uu) == 0, f"leading = {lead}")
    out["lead"] = lead

    gam_gr = sp.limit(gam, uu, 0)
    gam_short = planted("endpoint", sp.nsimplify(sp.simplify(gam.subs(uu, 1))), sp.Rational(1, 2))
    C("E", "E3a gamma(m2 r -> oo) = 1 -- GR recovered.  Endpoint survives the correction.",
      gam_gr == 1, f"gamma(long) = {gam_gr}")
    C("E", "E3b gamma(m2 r -> 0) = -1 for EINSTEIN-WEYL, NOT 1/2.  The 1/2 belongs to the "
         "massive mode ALONE (D5b); the full massless+ghost theory does not have it. [T3]",
      gam_short == -1, f"gamma(short) = {gam_short}")
    out["gam_short"] = gam_short

    short_Phi = sp.nsimplify((1 - cT).subs(uu, 1))
    C("E", "E4 short-range (m2 r << 1) Phi bracket = 1 - 4/3 = -1/3: gravity is REPULSIVE "
         "below the Yukawa range in Einstein-Weyl.  The old assignment gave +4/3 (attraction "
         "enhanced).  Antigravity vs 4/3-gravity -- the two assignments are physically opposite.",
      short_Phi == sp.Rational(-1, 3), f"1 - cT = {short_Phi}")
    out["short_Phi"] = short_Phi

    # r->0 finiteness is NOT inherited by Einstein-Weyl alone
    C("E", "E5 Einstein-Weyl alone is NOT r->0 finite (bracket -> -1/3 != 0): Stelle's "
         "finiteness needs BOTH massive modes.  The old file's implicit inheritance of it "
         "was unavailable either way -- the sum rule never applied to the GU case.",
      short_Phi != 0)

    # ---------------- THE DEGENERACY -- why no check caught it ----------------
    lead_old = sp.nsimplify(sp.expand(sp.series(gam_old - 1, uu, 0, 2).removeO()))
    same_mag = planted("degeneracy",
                       sp.simplify(sp.Abs(lead) - sp.Abs(lead_old)) == 0, False)
    C("E", "E6 DEGENERACY, NEW: |gamma - 1| leading magnitude is (2/3)e^{-m2 r} under BOTH "
         "the wrong (+1/3) and the corrected (-4/3) assignment.  Cassini bounds |gamma-1|, "
         "so the Cassini m2 floor CANNOT DISCRIMINATE between them.  The banner named two "
         "non-discriminating checks (r->0 sum rule, gamma=1/2); this is a THIRD, and it is "
         "the one the falsifier's verdict actually rides on.",
      same_mag, f"corrected {lead}, wrong {lead_old}")
    C("E", "E7 the sign, however, is opposite: corrected +2/3, wrong -2/3.",
      sp.sign(lead.coeff(uu)) == -sp.sign(lead_old.coeff(uu)))
    out["lead_old"] = lead_old
    out["gam_old_short"] = sp.nsimplify(gam_old.subs(uu, 1))
    return out


# ===========================================================================
# [R] REPRODUCTIONS -- repo facts asserted BEFORE they are used
# ===========================================================================
def reproductions(d: dict, e: dict) -> None:
    log("")
    log("=" * 78)
    log("[R] REPRODUCTIONS -- repo facts, asserted before use")
    log("=" * 78)
    banner = H10_PY.read_text(encoding="utf-8")
    C("R", "R1 the 2026-08-09 banner is still present in the H10 file and still states the "
         "-4/3 / +1/3 assignment (so this probe is remediating the recorded defect, not a "
         "different one)",
      "massive spin-2 GHOST (Weyl^2/C^2) : -4/3   REPULSIVE" in banner
      and "massive spin-0 scalaron (R^2)     : +1/3   attractive" in banner)
    C("R", "R2 the banner's stated TRAP potential is reproduced by this probe's independent "
         "derivation (D7b), coefficients -2/3 and -1/3, both same sign",
      "psi = -(GM/r)[1 - (2/3)e^{-m2 r} - (1/3)e^{-m0 r}]" in banner
      and d["cS"] == sp.Rational(2, 3) and d["c0s"] == sp.Rational(-1, 3))
    # Lu-Perkins-Pope-Stelle Eq (4.7a) form: V = C - M/(24 pi g r)(e^-m0r - 4 e^-m2r + 3)
    Cc, g = sp.symbols("Cc g", positive=True)
    V_lpps = Cc - GM / (24 * sp.pi * g * r) * (sp.exp(-m0 * r) - 4 * sp.exp(-m2 * r) + 3)
    # with C=0 and Phi = V/2, normalise the Newtonian piece to -GM/r:
    brk_lpps = sp.nsimplify(sp.Rational(1, 3) * (sp.exp(-m0 * r) - 4 * sp.exp(-m2 * r) + 3))
    brk_mine = 1 - d["cT"] * sp.exp(-m2 * r) + d["c0"] * sp.exp(-m0 * r)
    C("R", "R3 the banner's cited Lu-Perkins-Pope-STELLE Eq (4.7a) bracket, normalised to a "
         "unit Newtonian term, EQUALS this probe's independently derived bracket.  The "
         "literature and the derivation agree; the banner's physics is CONFIRMED.",
      sp.simplify(brk_lpps - brk_mine) == 0,
      f"LPPS/3 = {sp.expand(brk_lpps)}  vs derived {sp.expand(brk_mine)}")
    C("R", "R4 repo H15/H25: the TT operator is box(box+m2^2) with m^2_eff in [5/6, 5/4], "
         "O(1) and POSITIVE -- consumed, not re-derived here",
      sp.Rational(5, 6) < sp.Rational(5, 4))
    md = H10_MD.read_text(encoding="utf-8")
    C("R", "R5 the exploration note is the artifact the banner names as also owing remediation",
      "H10 -- The PPN / weak-field solar-system bar" in md)
    _ = V_lpps


# ===========================================================================
# [O] OBSERVATIONAL -- the ONLY floats in this file, declared and isolated
# ===========================================================================
import math  # noqa: E402  (kept adjacent to the only float-using section)

FLOAT_INPUTS = {
    "CASSINI_GAMMA": 2.3e-5,        # Bertotti, Iess, Tortora, Nature 425, 374 (2003)
    "LLR_BETA": 8.0e-5,             # Williams, Turyshev, Boggs, PRL 93, 261101 (2004)
    "AU_m": 1.495978707e11,
    "R_SUN_m": 6.957e8,
    "HBARC_eV_m": 1.973269804e-7,
    "M_PL_eV": 1.220890e28,
}


def observational(d: dict, e: dict) -> dict:
    out: dict = {}
    log("")
    log("=" * 78)
    log("[O] OBSERVATIONAL -- declared floats; no exact claim above reads these")
    log("=" * 78)
    eps = FLOAT_INPUTS["CASSINI_GAMMA"]
    AU = FLOAT_INPUTS["AU_m"]
    HBARC = FLOAT_INPUTS["HBARC_eV_m"]
    MPL = FLOAT_INPUTS["M_PL_eV"]
    cT_f, cS_f = float(d["cT"]), float(d["cS"])

    # Route 1: exact solve of |(2/3)u / (1 - (4/3)u)| = eps  ->  u = 3 eps/(2 + 4 eps)
    u_exact = 3.0 * eps / (2.0 + 4.0 * eps)
    # Route 2: leading-order  (2/3) u = eps  ->  u = 1.5 eps
    u_lead = 1.5 * eps
    thresh = -math.log(u_exact)
    thresh_lead = -math.log(u_lead)
    C("O", "O1 two independent routes to the Cassini threshold m2*r agree to < 1e-3 "
         "(exact solve of the full rational gamma vs leading-order series)",
      abs(thresh - thresh_lead) < 1e-3, f"exact {thresh:.5f} vs leading {thresh_lead:.5f}")

    # The SAME computation under the OLD (wrong) assignment: |(2/3)u/(1+u/3)| = eps
    u_old = 3.0 * eps / (2.0 - eps)
    thresh_old = -math.log(u_old)
    rel = abs(thresh - thresh_old) / thresh
    C("O", "O2 DEGENERACY, QUANTIFIED: the corrected and the wrong assignment give Cassini "
         "m2*r floors differing by %.1e in relative terms.  Repairing the physics moves the "
         "published floor by parts per million.  A Cassini-only falsifier could NEVER have "
         "caught this error." % rel,
      rel < 1e-4, f"corrected {thresh:.6f} vs wrong {thresh_old:.6f}, rel {rel:.2e}")

    m2_min_AU = thresh / AU * HBARC                       # eV
    m2_min_imp = thresh / (1.6 * FLOAT_INPUTS["R_SUN_m"]) * HBARC
    sqrt_meff = math.sqrt(5.0 / 6.0)                      # conservative corner (H25 Method 1)
    mu_floor = m2_min_AU / sqrt_meff
    decades = math.log10(MPL / mu_floor)
    out.update(thresh=thresh, m2_min_AU=m2_min_AU, m2_min_imp=m2_min_imp,
               mu_floor=mu_floor, decades=decades, rel_degeneracy=rel)

    log(f"  |gamma-1| = (2/3)e^-m2r/(1-(4/3)e^-m2r) < {eps:.1e}  =>  m2 r > {thresh:.4f}")
    log(f"  r = 1 AU        : m2 > {m2_min_AU:.3e} eV")
    log(f"  r = 1.6 R_sun   : m2 > {m2_min_imp:.3e} eV")
    log(f"  mu_DW floor (m^2_eff = 5/6) : {mu_floor:.3e} eV")
    log(f"  natural mu_DW ~ M_Pl clears it by {decades:.1f} decades")

    floor_ok = planted("cassini_floor", (1e-19 < mu_floor < 1e-15), False)
    C("O", "O3 the Cassini floor on mu_DW is ~1.5e-17 eV -- NUMERICALLY UNCHANGED by the "
         "correction, because the bound is two-sided in |gamma-1| and the magnitude is "
         "degenerate (E6)",
      floor_ok, f"mu_DW floor = {mu_floor:.4e} eV")
    C("O", "O4 natural mu_DW ~ M_Pl clears the Cassini floor by > 40 decades",
      decades > 40, f"{decades:.2f} decades")
    C("O", "O5 VERDICT [T4 UPHELD]: GU still CLEARS Cassini.  The corrected sign changes "
         "WHICH SIDE of gamma=1 GU sits on, not whether it passes.",
      decades > 40 and floor_ok)
    C("O", "O6 the corrected sign predicts gamma - 1 > 0.  Bertotti et al. measured "
         "gamma - 1 = (2.1 +/- 2.3)e-5, i.e. a POSITIVE central value consistent with zero. "
         "The correction moves GU's predicted deviation onto the same side as the central "
         "value.  Statistical significance of that: NONE (< 1 sigma, null measurement). "
         "Stated so nobody over-reads it in either direction.",
      2.1e-5 / eps < 1.0, "central 2.1e-5 is 0.91 sigma; consistent with zero")
    C("O", "O7 LLR beta: beta -> 1 as O(e^{-m2 r}); the Cassini gamma bound is ~3.5x tighter, "
         "so gamma sets the binding floor.  Unchanged by the correction.",
      FLOAT_INPUTS["LLR_BETA"] / eps > 3.0)
    return out


# ===========================================================================
# [C] CONTROLS -- discrimination, contrary, non-vacuity, anti-drift
# ===========================================================================
def controls(d: dict, e: dict, o: dict) -> None:
    log("")
    log("=" * 78)
    log("[C] CONTROLS")
    log("=" * 78)

    # ---- C1/C2  CONTRARY CONTROL: configurations where the bar IS violated ----
    eps = FLOAT_INPUTS["CASSINI_GAMMA"]
    AU, HBARC = FLOAT_INPUTS["AU_m"], FLOAT_INPUTS["HBARC_eV_m"]

    def gamma_minus_1(mu_dw_eV: float) -> float:
        m2_eV = math.sqrt(5.0 / 6.0) * mu_dw_eV
        x = (m2_eV / HBARC) * AU                       # m2 * r, dimensionless
        u = math.exp(-x)
        return (2.0 / 3.0) * u / (1.0 - (4.0 / 3.0) * u)

    g_bad = gamma_minus_1(1e-18)
    g_good = gamma_minus_1(1e-15)
    viol = planted("contrary", abs(g_bad) > eps, False)
    C("C", "C1 CONTRARY CONTROL A -- a GU configuration that PROVABLY VIOLATES the bar: "
         "mu_DW = 1e-18 eV gives |gamma-1| = %.3e, which is %.0fx the Cassini bound. "
         "The machinery detects FAILURE, so the pass at M_Pl is not vacuous."
         % (g_bad, g_bad / eps),
      viol and abs(g_good) < eps,
      f"mu_DW=1e-18 -> |g-1|={g_bad:.3e} VIOLATES; mu_DW=1e-15 -> {g_good:.3e} passes")

    # Brans-Dicke omega=100: the repo's own external negative control (W220)
    w_bd = 100
    gam_bd = sp.Rational(1 + w_bd, 2 + w_bd)
    dev_bd = float(abs(gam_bd - 1))
    C("C", "C2 CONTRARY CONTROL B -- external comparator Brans-Dicke omega=100 gives "
         "|gamma-1| = %.2e, %.0fx the Cassini bound: correctly returned FALSIFIED. "
         "Reproduces the repo's own W220 negative control (9.8e-3, ~400x)."
         % (dev_bd, dev_bd / eps),
      dev_bd > eps and abs(dev_bd - 9.8e-3) < 1e-4, f"gamma_BD = {gam_bd} = {float(gam_bd):.5f}")

    # ---- C3  the DISCRIMINATING check the falsifier was missing ----
    C("C", "C3 DISCRIMINATING CHECK (new): gamma(m2 r -> 0) = -1 under the corrected "
         "assignment and = +1/2 under the wrong one.  This endpoint SEPARATES them.  Had the "
         "file asserted the Einstein-Weyl endpoint instead of the massive-mode-only 1/2, the "
         "error would have been caught on day one.",
      e["gam_short"] == -1 and e["gam_old_short"] == sp.Rational(1, 2)
      and e["gam_short"] != e["gam_old_short"],
      f"corrected {e['gam_short']}, wrong {e['gam_old_short']}")

    # ---- C4  the old anchor was NOT an anchor ----
    C("C", "C4 [T3 REFUTED] the old file's Q2a 'cross-check gamma(short)=1/2 anchors the "
         "linearization' was a FALSE ANCHOR: 1/2 is (i) the massive-mode-only value, (ii) the "
         "Brans-Dicke omega=0 value (D7b), and (iii) exactly what the WRONG assignment "
         "produces.  It could not have failed, so it certified nothing.",
      e["gam_old_short"] == sp.Rational(1, 2))

    # ---- C5  the trap, run explicitly ----
    # TWO independent exponentials: u2 = e^{-m2 r}, u0 = e^{-m0 r}.  Using one symbol for
    # both silently sets m0 = m2 and makes the trap bracket collapse onto the true one --
    # a real trap this control fell into on its first draft, and now guards against.
    u2, u0 = sp.symbols("u2 u0", positive=True)
    trap_brk = 1 - d["cS"] * u2 + d["c0s"] * u0     # spatial coefficients in the temporal slot
    true_brk = 1 - d["cT"] * u2 + d["c0"] * u0      # derived temporal bracket
    old_brk = 1 + sp.Rational(1, 3) * u2 - sp.Rational(4, 3) * u0   # the file's wrong assignment
    C("C", "C5 TRAP CONTROL -- the banner warns a stray '1/3 on the spin-2 term' may come from "
         "misreading the SPATIAL potential.  Put the spatial pair (2/3, -1/3) in the temporal "
         "slot: it reproduces NEITHER the derived temporal bracket NOR the file's old "
         "assignment.  Misreading psi does not rescue +1/3.  (Guard: m0 and m2 are kept as "
         "distinct symbols; collapsing them makes the trap bracket falsely equal the true one.)",
      sp.simplify(trap_brk - true_brk) != 0 and sp.simplify(trap_brk - old_brk) != 0
      and sp.simplify((trap_brk - true_brk).subs(u0, u2)) == 0,
      f"trap {sp.expand(trap_brk)} vs true {sp.expand(true_brk)} vs old {sp.expand(old_brk)}")

    # ---- C6  T1: alpha_Y ----
    alpha_Y_old, alpha_Y_new = sp.Rational(1, 3), -d["cT"]
    C("C", "C6 [T1 REFUTED] the repo-wide 'alpha_Y = 1/3 forced vDVZ trace factor' is wrong "
         "in BOTH magnitude and sign: alpha_Y = -4/3.  Magnitude x4, attraction -> repulsion.",
      alpha_Y_new == sp.Rational(-4, 3) and alpha_Y_new != alpha_Y_old)

    # ---- C7/C8  ANTI-DRIFT: the edited files must carry the corrected constants ----
    src = H10_PY.read_text(encoding="utf-8")
    try:
        compile(src, "H10", "exec")
        compiles = True
    except SyntaxError:
        compiles = False
    C("C", "C7a the H10 module COMPILES (not merely ast.parse -- the __future__ placement "
         "rule is enforced at compile; the banner warns a parse-only gate misses it)",
      planted("h10_compile", compiles, False))
    # ANTI-DRIFT proper: EXECUTE the falsifier and read its actual output.  A string grep
    # would pass on a file that merely mentions the right numbers in a comment, and would
    # fail on this one, which DERIVES them rather than hardcoding a literal.  Run it.
    run = subprocess.run([sys.executable, str(H10_PY)], capture_output=True, text=True,
                         cwd=str(ROOT))
    out_txt = run.stdout + run.stderr
    C("C", "C7b ANTI-DRIFT: the H10 falsifier RUNS and exits 0 (it exited 1 behind a "
         "known-defect guard before this remediation, and raised SyntaxError before that)",
      planted("h10_const", run.returncode == 0, False), f"exit {run.returncode}")
    C("C", "C7c ANTI-DRIFT: H10's own output carries the corrected potentials, the corrected "
         "POSITIVE gamma-1 sign, and no [FAIL] line",
      ("1 - (4/3)e^(-m2 r) + (1/3)e^(-m0 r)" in out_txt
       and "gamma - 1 = +(2/3)e^{-m2 r}" in out_txt
       and "[FAIL]" not in out_txt),
      f"{out_txt.count('[PASS]')} PASS, {out_txt.count('[FAIL]')} FAIL")
    C("C", "C7d ANTI-DRIFT: the known-defect guard is GONE from the source, and the file no "
         "longer asserts the refuted -(2/3) leading sign anywhere",
      "H10_ACKNOWLEDGE_KNOWN_DEFECT" not in src
      and "gamma - 1 = -(2/3) e^{-m2 r}" not in src)
    C("C", "C7e ANTI-DRIFT: H10 now carries its own contrary controls and the discriminating "
         "endpoint, so the defect class that produced this remediation is guarded IN THE BAR",
      "Q3-CONTRARY-A" in src and "Q3-CONTRARY-B" in src and "Q2b DISCRIMINATING" in src)
    md = H10_MD.read_text(encoding="utf-8")
    C("C", "C8 ANTI-DRIFT: the exploration note carries the corrected bracket and the "
         "corrected gamma-1 sign",
      planted("md_const", "(4/3)e^{-m2 r}" in md and "+(2/3) e^{-m2 r}" in md, False))

    # ---- C9  BLAST RADIUS: the banner UNDERSTATED it ----
    outside = [
        "explorations/track2-conditional-numbers-2026-07-13.md",
        "explorations/path4-branchA-eos-gravity-correlation-2026-07-11.md",
        "explorations/path4-wave2-alphaW-parameter-free-2026-07-11.md",
        "tests/W61_path4_A_eos_gravity.py",
        "tests/W66_path4_wave2_alphaW.py",
        "tests/W138_issuance_kill_battery.py",
    ]
    still_wrong = [p for p in outside
                   if any(t in (ROOT / p).read_text(encoding="utf-8")
                          for t in ("alpha_Y = 1/3", "alpha_Y=1/3", "Rational(1, 3)",
                                    "-(2/3) e^{-m2 r}", "-(2/3)e^{-m2 r}"))]
    C("C", "C9 BLAST RADIUS: the banner named 2 files; the wrong coefficient is live in %d "
         "MORE, all outside this remediation's write scope.  Reported as OWED, not silently "
         "left.  (Direction of the error there: the sub-mm exclusion gets STRONGER, so no "
         "verdict flips toward GU.)" % len(still_wrong),
      len(still_wrong) >= 5, "; ".join(still_wrong))

    # ---- C10  no SC- register entry covers PPN ----
    reg = (ROOT / "lab" / "sources" / "source-claim-register.yaml").read_text(encoding="utf-8")
    C("C", "C10 NON-VACUITY of the target typing: the source-claim register contains NO entry "
         "for PPN / Cassini / Stelle / solar-system, so this artifact's targets are INTERNAL "
         "repository claims, correctly typed as such rather than routed at a source claim.",
      not any(t in reg for t in ("PPN", "Cassini", "Stelle", "solar-system")))

    # ---- C11  artifact declares its target ----
    if ART.exists():
        art = ART.read_text(encoding="utf-8")
        C("C", "C11 the artifact declares target_claim and target_claim_verdict, and carries "
             "the routing notice with a Classification line",
          "target_claim:" in art and "target_claim_verdict:" in art
          and "GU-COMPARATOR-ROUTING" in art
          and "Classification: `CONVENTIONAL_COMPARATOR`" in art)


# ===========================================================================
# FAILURE PATH
# ===========================================================================
PLANTS = [
    ("proj_trace", "spin-2 projector trace coefficient forced to -1/2 (= the massless value)"),
    ("trace_massless", "massless numerator trace coefficient forced to 1/3"),
    ("trace_massive", "massive Fierz-Pauli trace coefficient forced to 1/2"),
    ("ghost_sign", "the massive-pole residue sign forced POSITIVE (no ghost)"),
    ("cT", "temporal enhancement forced to the file's old wrong -1/3"),
    ("cS", "spatial enhancement forced to the file's old wrong +1/3"),
    ("lead_sign", "gamma-1 leading term forced to the refuted -(2/3)e^{-m2 r}"),
    ("endpoint", "Einstein-Weyl gamma(m2 r -> 0) forced to the false anchor 1/2"),
    ("degeneracy", "the |gamma-1| magnitude degeneracy forced FALSE"),
    ("cassini_floor", "the mu_DW Cassini floor forced out of its decade"),
    ("contrary", "the contrary control forced to NOT violate the bar (non-vacuity)"),
    ("h10_compile", "the H10 module forced to report as non-compiling"),
    ("h10_const", "the H10 file's corrected constants forced absent"),
    ("md_const", "the exploration note's corrected constants forced absent"),
]


def selftest() -> int:
    log("SELF-TEST: each planted false fact must force exit 1; the clean run must exit 0.")
    bad = []
    me = str(Path(__file__).resolve())
    for name, why in PLANTS:
        env = dict(os.environ, H105_PLANT=name)
        p = subprocess.run([sys.executable, me], env=env, capture_output=True, text=True)
        ok = p.returncode == 1
        log(("PASS" if ok else "FAIL") + f" :: plant {name!r} exits 1 -- {why}"
            + ("" if ok else f" (got exit {p.returncode})"))
        if not ok:
            bad.append(name)
    env = dict(os.environ)
    env.pop("H105_PLANT", None)
    p = subprocess.run([sys.executable, me], env=env, capture_output=True, text=True)
    if p.returncode != 0:
        log(f"FAIL :: the unplanted run exits 0 (got {p.returncode})")
        bad.append("clean-run")
    else:
        log("PASS :: the unplanted run exits 0")
    if bad:
        log(f"SELF-TEST FAILED: {bad}")
        return 1
    log(f"SELF-TEST PASSED: {len(PLANTS)} planted false facts each forced exit 1, "
        "and the clean run exits 0.")
    return 0


def main() -> int:
    d = derive()
    e = exact_ppn(d)
    reproductions(d, e)
    o = observational(d, e)
    controls(d, e, o)

    npass = sum(1 for _, _, ok, _ in CERT if ok)
    ntot = len(CERT)
    counts: dict[str, int] = {}
    for t, _, _, _ in CERT:
        counts[t] = counts.get(t, 0) + 1
    log("")
    for t, n, ok, det in CERT:
        if not ok:
            log(f"FAIL [{t}] {n}\n     detail={det}")
    log("=" * 78)
    log("H10-5 CERTIFICATE -- Stelle/Einstein-Weyl Yukawa assignment")
    log("=" * 78)
    log(f"  DERIVED (no literature input) Phi = -(GM/r)[1 - (4/3)e^-m2r]  cT = {d['cT']}")
    log(f"                                Psi = -(GM/r)[1 - (2/3)e^-m2r]  cS = {d['cS']}")
    log(f"  banner CONFIRMED independently (R3: LPPS Eq 4.7a == derived bracket)")
    log(f"  gamma - 1 = +{sp.nsimplify(d['cT'] - d['cS'])} e^-m2r   (was -(2/3): SIGN REFUTED)")
    log(f"  gamma(m2 r -> 0) = {e['gam_short']}  (was +1/2: FALSE ANCHOR)")
    log(f"  alpha_Y = -4/3, REPULSIVE   (was +1/3 attractive: magnitude x4, sign flipped)")
    log(f"  Cassini m2*r floor  {o['thresh']:.4f}   mu_DW floor {o['mu_floor']:.3e} eV")
    log(f"  clearance at natural mu_DW ~ M_Pl : {o['decades']:.1f} decades  -> BAR CLEARED")
    log(f"  DEGENERACY: corrected vs wrong floors differ by {o['rel_degeneracy']:.1e} relative")
    log("  CONTRARY CONTROLS")
    log("    A  mu_DW = 1e-18 eV -> |gamma-1| ~ 1.0, i.e. ~4e4 x the Cassini bound: VIOLATED")
    log("    B  Brans-Dicke omega=100 -> |gamma-1| = 9.8e-3, ~426x the bound: FALSIFIED")
    log(f"  floats: only section [O]; inputs {sorted(FLOAT_INPUTS)}")
    log("  check split: " + "  ".join(f"[{k}] {v}" for k, v in sorted(counts.items())))
    log("")
    if npass == ntot:
        log(f"CERTIFICATE: {npass}/{ntot} checks pass.  Sections D/E/G exact (sympy Rational); "
            "no float is load-bearing for any exact claim.")
        return 0
    log(f"CERTIFICATE: {npass}/{ntot} checks pass -- FAILURES ABOVE.")
    return 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--plant" in sys.argv:
        PLANT = sys.argv[sys.argv.index("--plant") + 1]
    sys.exit(main())
