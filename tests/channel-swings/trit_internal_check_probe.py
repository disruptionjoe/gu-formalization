#!/usr/bin/env python3
"""TRIT-INTERNAL CHECK: executes the pre-registered successor check bound by
explorations/prereg-trit-internal-successor-2026-07-20.md (commit 6b384c5).

HYPOTHESIS (bound): the trit half of the minimal Z/6 input is ALREADY
SUPPLIED by frozen structure -- the N4-identified Z/3 (commit 4f5a44c).
TEST (bound): construct the candidate trit anchor from the N4 identification
data ONLY (rho characters, Phi maps, the admissible inversion), run the EXACT
sufficiency battery of conditional_forcing_probe.py (imported UNMODIFIED),
with the bound controls. Allowed freedom: the inversion {Phi_D, Phi_B} ONLY.
OUTCOMES (bound): K-a NOT CANONICAL / K-b CANONICAL BUT INSUFFICIENT /
K-c CONFIRMS.

WHAT THE RUN FINDS (outcome named in the HEADLINE): the N4 data canonically
populates the TARGET side of the trit role -- the chain
chi = exp(2*pi*i * e_KO o Phi) lands exactly on the canonical cube roots of
unity in the C-linear commutant scalars, unique up to the inversion -- but
supplies NO fiber-side Z/3: the scalars pass through the spin-lift family
without moving the fiber parameter (the induced fiber action is the
IDENTITY), and the commutant's only family-preserving route (J-conjugation)
induces a Z/2 (v -> vbar), never a trit: order-3 elements of the family
normalizer are exactly the scalars. The two N4-only candidates fail the
battery (empty type / vacuous type with the degree-3 order-killer inside),
and occupying the role nontrivially demands a fiber axis the battery itself
provably cannot select (a conjugated axis passes the identical battery).
A new choice beyond the inversion is REQUIRED -> K-a.

Deterministic; no edits to any imported probe; exit 0 iff all checks pass.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import sys
import time
from fractions import Fraction as Fr
from itertools import product

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "generation-sector")))

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


def import_probe(fname):
    name = fname[:-3]
    spec = importlib.util.spec_from_file_location(name, os.path.join(_HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    t0 = time.time()
    code = 0
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            spec.loader.exec_module(mod)
    except SystemExit as ex:
        code = int(ex.code or 0)
    mod._captured_output = buf.getvalue()
    mod._exit_code = code
    return mod, time.time() - t0


t_start = time.time()
print("=" * 78)
print("SETUP  live imports: the N4 identification + the EXACT Z/6 battery")
print("=" * 78)

n4, dt_n4 = import_probe("n4_two_z3s_probe.py")
check("T", "n4_two_z3s_probe.py re-runs LIVE and clean (exit 0, all 27 "
           "checks): the identification data arrives frozen -- "
           "Phi_D = {0,8,16}, Phi_B = {0,16,8}, admissible set exactly "
           "{Phi_D, Phi_B} (the inversion, the ONLY allowed freedom)",
      n4._exit_code == 0 and not n4.FAILED
      and n4.PHI_D == {0: 0, 1: 8, 2: 16} and n4.PHI_B == {0: 0, 1: 16, 2: 8}
      and n4.admissible == {(0, 8, 16), (0, 16, 8)},
      f"exit {n4._exit_code}, {dt_n4:.1f} s")

cf, dt_cf = import_probe("conditional_forcing_probe.py")
cf_all = all(ok for _t, _n, ok in cf.RESULTS)
check("T", "conditional_forcing_probe.py re-runs LIVE and clean, UNMODIFIED "
           "(exit 0, all checks; k1 + phase0 nested inside): the EXACT Z/6 "
           "sufficiency battery is refreshed in this run -- generic Z/6 "
           "degrees [1, 1], twisted member +7 (all = 1 mod 6), and every "
           "power certificate of the degree counter is live",
      cf._exit_code == 0 and cf_all and cf.z6_degs == [1, 1] and cf.z6_eq_ok
      and cf.d71a == 7 and cf.d71b == 7,
      f"exit {cf._exit_code}, {dt_cf:.0f} s")

k1 = cf.k1
order24 = cf.order24
OMEGA = cf.zeta3                       # exp(2*pi*i/3), the canonical scalar
Z3Q = np.array([OMEGA.real, OMEGA.imag, 0.0, 0.0])
Z6Q = np.array([cf.zeta6.real, cf.zeta6.imag, 0.0, 0.0])
SQ3 = np.sqrt(3.0)

# =============================================================================
print()
print("=" * 78)
print("CONSTRUCTION  the candidate trit anchor from N4 data ONLY")
print("=" * 78)

EKO = {a: n4.m1(Fr(a, 24)) for a in range(24)}
CHI = {}
for tag_p, PHI in (("D", n4.PHI_D), ("B", n4.PHI_B)):
    CHI[tag_p] = {kk: complex(np.cos(2 * np.pi * float(EKO[PHI[kk]])),
                              np.sin(2 * np.pi * float(EKO[PHI[kk]])))
                  for kk in range(3)}
hom_ok = all(n4.m1(EKO[PHI[(kk + ll) % 3]])
             == n4.m1(EKO[PHI[kk]] + EKO[PHI[ll]])
             for PHI in (n4.PHI_D, n4.PHI_B)
             for kk, ll in product(range(3), repeat=2))
img_ok = all(
    min(abs(CHI[t][kk] - OMEGA ** m) for m in (0, 1, 2)) < 1e-12
    for t in ("D", "B") for kk in range(3)) and all(
    len({round(CHI[t][kk].real, 9) + 1j * round(CHI[t][kk].imag, 9)
         for kk in range(3)}) == 3 for t in ("D", "B"))
inv_ok = max(abs(CHI["B"][kk] - CHI["D"][kk].conjugate()) for kk in range(3))
olum = {(r * r) % 3 for r in (1, 2)}
check("E", "the N4 chain canonically populates the TARGET side of the trit "
           "role: chi = exp(2 pi i * e_KO o Phi) is an exact character "
           "(Fraction additivity, all 9 pairs, both Phi's) landing on the "
           "canonical cube roots {1, omega, omega^2} in the commutant "
           "scalars -- chi_D(alpha_1) = omega, chi_B(alpha_1) = omega^2, the "
           "two differ by EXACTLY the admissible inversion (complex "
           "conjugation); the trit slot of the Z/6 reference is the SQUARE "
           "of the sixth root (zeta_6^2 = zeta_3 exactly); Olum pinning "
           "r^2 = 1 mod 3 for BOTH generators: the inversion can never move "
           "the count -- the target-side matching needs no new choice",
      hom_ok and img_ok
      and abs(CHI["D"][1] - OMEGA) < 1e-15
      and abs(CHI["B"][1] - OMEGA ** 2) < 1e-15
      and inv_ok < 1e-15 and abs(cf.zeta6 ** 2 - OMEGA) < 1e-15
      and olum == {1},
      f"chi_D(a1) = omega, chi_B(a1) = omega^2; inversion defect {inv_ok:.1e}")

I128 = k1.I128
C = k1.C
PINS = k1.PINS
V_FIB = [np.array([0.36, 0.48, 0.6, -0.52]), np.array([0.6, 0.8, 0.0, 0.0]),
         np.array([0.5, 0.5, 0.5, 0.5])]
V_FIB = [v / np.linalg.norm(v) for v in V_FIB]
RNG = np.random.default_rng(20260720)
PSIS = []
for _ in range(3):
    psi = RNG.standard_normal(128) + 1j * RNG.standard_normal(128)
    PSIS.append(psi / np.linalg.norm(psi))

pass_through = 0.0
for pin in PINS:
    for v in V_FIB:
        L = k1.lam_v(v, pin)
        for psi in PSIS:
            for m in (1, 2):
                pass_through = max(pass_through, float(np.max(np.abs(
                    (OMEGA ** m) * (L @ psi) - L @ ((OMEGA ** m) * psi)))))
scal3 = sorted(round(abs(np.exp(2j * np.pi * kk / 3)
                         - OMEGA ** kk), 12) for kk in range(3))
check("E", "the operator realization of the N4 trit is the scalar pair "
           "{omega I, omega^2 I} (the C-linear commutant is scalars only -- "
           "N6 receipt; order-3 scalars are exactly the cube roots), and "
           "scalars transport across the spin-lift family WITHOUT moving "
           "the fiber parameter: omega^m (Lambda(v) psi) = Lambda(v) "
           "(omega^m psi) at machine identity (both pins, 3 v, 3 states) -- "
           "the induced action of the N4 trit on the fiber is the IDENTITY: "
           "no fiber-side Z/3 arrives with the identification",
      pass_through < 1e-14 and scal3 == [0.0, 0.0, 0.0],
      f"pass-through defect {pass_through:.1e}")


def J_op(psi):
    return C @ psi.conj()


def conj_span_residual(u_apply, u_inv_apply, pin, psi):
    """residual of u Lambda(v) u^{-1} psi against span{I, Q0, Q1, Q2} psi."""
    L = k1.lam_v(V_FIB[0], pin)
    w = u_apply(L @ u_inv_apply(psi))
    cols = np.stack([psi] + [Q @ psi for Q in k1.QFAM[pin]], axis=1)
    coef, *_ = np.linalg.lstsq(cols, w, rcond=None)
    return float(np.linalg.norm(cols @ coef - w)), coef


jbar_worst = 0.0
break_min = np.inf
c3, s3 = np.cos(2 * np.pi / 3), np.sin(2 * np.pi / 3)
for pin in PINS:
    for v in V_FIB:
        L = k1.lam_v(v, pin)
        vbar = np.array([v[0], -v[1], -v[2], -v[3]])
        Lbar = k1.lam_v(vbar, pin)
        for psi in PSIS[:2]:
            jbar_worst = max(jbar_worst, float(np.max(np.abs(
                J_op(L @ (-J_op(psi))) - Lbar @ psi))))
    al_g = (0.3 + 0.7j) / np.sqrt(0.99)
    be_g = (-0.5 + 0.4j) / np.sqrt(0.99)
    for psi in PSIS[:2]:
        r_gen, _ = conj_span_residual(
            lambda p: al_g * p + be_g * J_op(p),
            lambda p: np.conj(al_g) * p - be_g * J_op(p), pin, psi)
        r_u3, _ = conj_span_residual(
            lambda p: c3 * p + s3 * J_op(p),
            lambda p: c3 * p - s3 * J_op(p), pin, psi)
        break_min = min(break_min, r_gen, r_u3)
aJ_sq = 0.0
for psi in PSIS[:2]:
    a = 0.6 + 0.8j
    w = a * J_op(a * J_op(psi))          # (a J)(a J) psi
    aJ_sq = max(aJ_sq, float(np.max(np.abs(w + psi))))
check("E", "the conjugation route is EXHAUSTED and delivers no trit: "
           "J-conjugation preserves the family and acts as v -> vbar "
           "(quaternion conjugation, order TWO -- one more bit, never a "
           "trit; defect < 1e-13 both pins), while generic AND non-scalar "
           "order-3 (cos + sin J) commutant conjugations BREAK the family "
           "span (residual O(0.3-0.5)); J-coset elements square to -I "
           "exactly ((aJ)^2 = -|a|^2, order 4), so the order-3 elements of "
           "the family normalizer are EXACTLY the scalars -- which act "
           "trivially: no commutant route carries the N4 trit to the fiber",
      jbar_worst < 1e-13 and break_min > 0.3 and aJ_sq < 1e-13,
      f"J-conj vs Lambda(vbar) {jbar_worst:.1e}; span-break residual "
      f">= {break_min:.2f}; (aJ)^2 + 1 = {aJ_sq:.1e}")

# =============================================================================
print()
print("=" * 78)
print("BATTERY  the N4-only candidates against the exact sufficiency battery")
print("=" * 78)

f_gen = cf.u1_oracle([1.0, 0.7, -0.6, 0.5, 0.4, -0.8, 0.3])
t1_vals = []
for f in (cf.j31, f_gen, (lambda v: v)):
    for v in cf.V_TEST:
        t1_vals.append(float(np.linalg.norm(f(v) - cf.act(OMEGA, f(v)))))
check("E", "candidate T1 (trivial fiber action + N4 weight omega -- the "
           "identification transported literally): the equivariance demand "
           "f(v) = omega f(v) is INFEASIBLE for every sphere-valued map -- "
           "the defect is the CONSTANT |1 - omega| = sqrt(3) on every "
           "sampled member (identity, the degree-3 join, a generic Z/6 "
           "survivor): the type is EMPTY, no admissible transport exists, "
           "nothing is forced",
      min(t1_vals) > 1.73 and max(t1_vals) - min(t1_vals) < 1e-12
      and abs(min(t1_vals) - SQ3) < 1e-12,
      f"defect constant {min(t1_vals):.12f} = sqrt(3)")

check("E", "candidate T2 (trivial fiber action + trivial weight -- the "
           "identification as a vacuous constraint): the constrained type "
           "collapses to X1 (the bit alone), and the battery's own "
           "order-killer sits inside it LIVE: the join map (z1^3, z2) is "
           "exactly deck-odd with certified degree +3, k = 192 = 0 mod 24, "
           "order 1 -- the N4-only candidate cannot force the count "
           "(re-read from the unmodified imported run)",
      cf.deck_defect(cf.j31) == 0.0 and cf.d31a == 3
      and order24((64 * 3) % 24) == 1,
      f"deg(join(3,1)) = {cf.d31a:+d}; order(J(192)) = 1")

QR = np.array([1.0, 0.0, 1.0, 0.0]) / np.sqrt(2.0)
QRB = np.array([1.0, 0.0, -1.0, 0.0]) / np.sqrt(2.0)
U3P = k1.hamilton(QR, k1.hamilton(Z3Q, QRB))
U6P = k1.hamilton(QR, k1.hamilton(Z6Q, QRB))
u3p_cube = k1.hamilton(U3P, k1.hamilton(U3P, U3P))
d_ax = min(float(np.linalg.norm(U3P - Z3Q)),
           float(np.linalg.norm(U3P - k1.hamilton(Z3Q, Z3Q))))
act_is_left = max(float(np.max(np.abs(cf.act(OMEGA, v) - k1.hamilton(Z3Q, v))))
                  for v in cf.V_TEST)


def g_gen(v):
    return f_gen(k1.hamilton(QRB, v))


def g7(v):
    return cf.j71(k1.hamilton(QRB, v))


def eq2_defect(f, uq, weight):
    worst = 0.0
    for v in cf.V_TEST:
        worst = max(worst, float(np.max(np.abs(
            f(k1.hamilton(uq, v)) - cf.act(weight, f(v))))))
    return worst


ed_g = eq2_defect(g_gen, U6P, cf.zeta6)
ed_g7 = eq2_defect(g7, U6P, cf.zeta6)
ed_g7_ax1 = cf.eq_defect(g7, cf.zeta6, cf.zeta6)
dg1, _ = k1.degree_by_preimage(g_gen, cf.num_jac(g_gen), k1.W1, nstarts=4000)
dg2, _ = k1.degree_by_preimage(g_gen, cf.num_jac(g_gen), k1.W2, nstarts=4000)
d7a, n7a = k1.degree_by_preimage(g7, cf.num_jac(g7), k1.W1, nstarts=9000)
d7b, _ = k1.degree_by_preimage(g7, cf.num_jac(g7), k1.W2, nstarts=9000)
check("E", "occupying the role nontrivially REQUIRES a fiber axis, and the "
           "battery provably cannot select it: a conjugated axis (u' = "
           "q_r zeta_3 q_r^{-1}, exactly order 3, distance 1.22 from BOTH "
           "members of the canonical axis subgroup -- outside the inversion "
           "orbit, which never moves the axis) passes the IDENTICAL "
           "battery: composed members are axis-2 equivariant at < 1e-12 "
           "with the SAME canonical scalar weights, exactly deck-odd, "
           "certified degrees +1 (generic) and +7 (twisted; NOT axis-1 "
           "equivariant, defect O(1)) on two regular values via the "
           "unmodified power-certified counter -- every degree = 1 mod 6, "
           "order 3 forced in the axis-2 type exactly as in axis-1: the "
           "axis is invisible to every bound test, hence a genuinely free "
           "choice the N4 data does not make. K-a fires",
      float(np.max(np.abs(u3p_cube - np.array([1.0, 0, 0, 0])))) < 1e-12
      and d_ax > 1.2 and act_is_left == 0.0
      and ed_g < 1e-12 and ed_g7 < 1e-12 and ed_g7_ax1 > 0.01
      and cf.deck_defect(g_gen) == 0.0 and cf.deck_defect(g7) == 0.0
      and dg1 == 1 and dg2 == 1 and d7a == 7 and d7b == 7
      and order24(64 % 24) == 3 and order24((64 * 7) % 24) == 3,
      f"axis-2 degs {dg1},{dg2} and {d7a},{d7b} ({n7a} preimages); "
      f"eq defects {ed_g:.1e}/{ed_g7:.1e}; axis-1 defect {ed_g7_ax1:.2f}")

# =============================================================================
print()
print("=" * 78)
print("CONTROLS  the three bound controls")
print("=" * 78)

rho_fake = {0: Fr(0), 1: Fr(1, 3), 2: Fr(1, 3)}
ok_fake, _ = n4.is_identification(rho_fake)
scr_d1 = max(float(np.linalg.norm(
    f_gen(cf.act(OMEGA, v)) - cf.act(OMEGA, f_gen(v)))) for v in cf.V_TEST)
scr_d2 = min(float(np.linalg.norm(
    f_gen(cf.act(OMEGA ** 2, v)) - cf.act(OMEGA, f_gen(v))))
    for v in cf.V_TEST)
check("F", "CONTROL 1 -- the scrambled-character trit FAILS: (0, 1/3, 1/3) "
           "is rejected by the live N4 gate (not a homomorphism, not "
           "injective, no intertwiner), and at battery level its demand "
           "pair is internally contradictory: the honest equivariant member "
           "satisfies the k = 1 demand at 1e-15 while the scrambled k = 2 "
           "demand fails at |omega - omega^2| = sqrt(3) (any exact solution "
           "of both is forced to |f| = 0, off the sphere): demonstrated "
           "power -- the battery cannot be passed by a non-character trit",
      not ok_fake and not n4.is_hom(rho_fake) and not n4.is_inj(rho_fake)
      and scr_d1 < 1e-12 and abs(scr_d2 - SQ3) < 1e-9,
      f"demand-1 defect {scr_d1:.1e}; scrambled demand-2 defect "
      f"{scr_d2:.6f} = sqrt(3)")

check("F", "CONTROL 2 -- the X1.5 generic-reader scatter is UNCHANGED in "
           "the unmodified live run: witnessed degrees {-1, +1, +3} with "
           "the 3-divisible member on a fully generic draw (order 1): "
           "reading is still not anchoring",
      sorted(set(cf.deg_15)) == [-1, 1, 3] and cf.ok_cons
      and order24((64 * 3) % 24) == 1,
      f"degrees {cf.deg_15}")

check("F", "CONTROL 3 -- the planted weight-blind oracle is STILL REJECTED "
           "in the unmodified live run: passes the Z/2 deck shadow exactly "
           "(0.0), fails G1 exactly (commutant reach 0.0), Borsuk-Ulam "
           "discontinuity witnessed (2.0 jump across 2e-9)",
      cf.bl_deck == 0.0 and cf.bl_reach == 0.0 and cf.disc > 1.9,
      f"deck {cf.bl_deck:.1f}; reach {cf.bl_reach:.1f}; jump {cf.disc:.2f}")

# =============================================================================
print()
nT = sum(1 for t, _n, ok in RESULTS if t == "T")
nE = sum(1 for t, _n, ok in RESULTS if t == "E")
nF = sum(1 for t, _n, ok in RESULTS if t == "F")
fails = [(t, n) for t, n, ok in RESULTS if not ok]
all_ok = not fails
print(f"HEADLINE: TRIT-INTERNAL CHECK RESOLVED -- outcome K-a (NOT "
      f"CANONICAL). The N4 identification canonically supplies the TARGET "
      f"side of the trit role (chi = exp(2 pi i e_KO o Phi) lands exactly "
      f"on the canonical cube roots in the commutant scalars, unique up to "
      f"the admissible inversion, count inversion-invariant by Olum) but "
      f"supplies NO fiber-side Z/3: scalars cross the spin-lift family "
      f"without moving the fiber parameter (induced action = identity), "
      f"the commutant's only family-preserving route (J-conjugation) "
      f"induces a Z/2 (v -> vbar) -- one more bit, never a trit -- and the "
      f"order-3 elements of the family normalizer are exactly the "
      f"trivially-acting scalars. Both N4-only candidates fail the exact "
      f"battery (empty type at constant defect sqrt(3); vacuous type = X1 "
      f"with the deck-odd degree-3 order-killer inside), and nontrivial "
      f"occupancy requires a fiber axis the battery provably cannot select "
      f"(a conjugated axis passes the identical battery: degrees +1/+7, "
      f"all = 1 mod 6). A new choice beyond the inversion is REQUIRED: the "
      f"trit remains EXTERNAL, the minimal input stays Z/6, and the N4 "
      f"identification is arena-side only. "
      f"{nE} [E] + {nF} [F] = {nE + nF} (setup [T] = {nT} excluded)   "
      f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}   "
      f"({time.time() - t_start:.1f} s)")
if fails:
    for t, n in fails:
        print(f"  FAILED [{t}] {n}")
sys.exit(0 if all_ok else 1)
