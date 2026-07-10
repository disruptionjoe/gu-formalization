#!/usr/bin/env python3
# -*- coding: ascii -*-
"""HOSTILE REFEREE independent verification of LEG-4 (verdict leg / decision table).

Independence from the leg's script:
  R1  indices re-derived by CHARACTERISTIC-CLASS INTEGRATION (A-hat * ch, symbolic p1),
      not by the additivity inputs (indDT = -40 was an INPUT there; here it is derived).
  R2  multipliers via the MINIMAL POLYNOMIAL x^2 + x + 1 (zeta + zeta^2 = -1), not radicals.
  R3  decision-table distribution re-derived in CLOSED FORM from the .md's stated rules
      (products of outcome-space cardinalities), never running the leg's enumerator.
  R4  the leg's verdict() is then extracted from its file and probed at ONE adversarial
      point (mb_closed=False) to test claim (b)'s word "only".
  R5  class algebra re-done from the canon LEG-D statement alone.

FIREWALL: sigma(K3) = -16 is the only geometric input; chi(K3) never appears; A-hat
derived = 2; no dynamics touched (58.72 / 343.73 absent from code).
"""
from sympy import Rational, Integer, symbols, expand, Poly
from fractions import Fraction

fails = []
N = [0]
def chk(name, got, want):
    N[0] += 1
    ok = (got == want)
    print(("PASS " if ok else "FAIL ") + name + ": " + str(got) + ("" if ok else "  (want " + str(want) + ")"))
    if not ok:
        fails.append(name)

print("== R1. indices by A-hat * ch integration (independent route) ==")
p1 = symbols("p1")                       # symbolic first Pontryagin number placeholder
sigma = Integer(-16)                     # ONLY geometric input
p1_val = 3 * sigma                       # signature theorem
chk("p1 = 3 sigma = -48", p1_val, Integer(-48))
# On a closed spin 4-manifold: ind(D (x) V) = [A-hat * ch(V)]_4 = rk(V)*(-p1/24) + ch2(V)
# For V = T_C (complexification of a real rank-4 bundle, c1 = 0): ch2 = p1, rk = 4.
def ind_twist(rk, ch2_coeff_of_p1):
    # returns coefficient of p1, exact
    return Rational(-rk, 24) + ch2_coeff_of_p1
indD_coeff  = ind_twist(1, 0)                       # trivial line: -p1/24
indDT_coeff = ind_twist(4, 1)                       # T_C: -4 p1/24 + p1 = 5 p1/6
chk("ind D = -p1/24 -> 2", indD_coeff * p1_val, Integer(2))
chk("ind D_T = 5 p1/6 -> -40 (DERIVED here, was an input in the leg)", indDT_coeff * p1_val, Integer(-40))
A_coeff  = indDT_coeff - indD_coeff                 # T_C - 1
B_coeff  = indDT_coeff + indD_coeff                 # T_C + 1
D2_coeff = indDT_coeff - 2 * indD_coeff             # T_C - 2
chk("carrier A = 7 p1/8 -> -42", (A_coeff, A_coeff * p1_val), (Rational(7, 8), Integer(-42)))
chk("carrier B = 19 p1/24 -> -38", (B_coeff, B_coeff * p1_val), (Rational(19, 24), Integer(-38)))
chk("bare = 5 p1/6 -> -40", indDT_coeff * p1_val, Integer(-40))
chk("double = 11 p1/12 -> -44", (D2_coeff, D2_coeff * p1_val), (Rational(11, 12), Integer(-44)))
Ahat = -sigma / 8
chk("A-hat = 2 (never 3)", Ahat, Integer(2))
chk("A = -21 A-hat; B = -19 A-hat (HS Prop 3.1(i) fetched: 'ind Q = -19 A-hat')",
    (A_coeff * p1_val / Ahat, B_coeff * p1_val / Ahat), (Integer(-21), Integer(-19)))
chk("sigma-register: 21 sigma/8 = -42; 19 sigma/8 = -38",
    (Rational(21, 8) * sigma, Rational(19, 8) * sigma), (Integer(-42), Integer(-38)))
chk("mod-3 residues (A,B,bare,double) = (0,1,2,1)",
    tuple(int(x * p1_val) % 3 for x in (A_coeff, B_coeff, indDT_coeff, D2_coeff)), (0, 1, 2, 1))
chk("fork B - A = 2 ind D = 4", (B_coeff - A_coeff) * p1_val, Integer(4))
chk("LEG-3 target gap |(-42) - (-44)| = ind D = 2", abs(-42 - (-44)), 2)

print("\n== R2. multipliers via minimal polynomial (zeta^2 + zeta + 1 = 0) ==")
# tr(g|T_C) at a Nikulin fixed point: tangent eigenvalues (zeta, zeta^2) complex, so
# T_C = T + Tbar has eigenvalues {zeta, zeta^2, zeta^2, zeta}: tr = 2(zeta + zeta^2) = 2*(-1) = -2.
zeta_sum = Integer(-1)                    # zeta + zeta^2 = -1 from x^2 + x + 1
trTC = 2 * zeta_sum
chk("tr(g|T_C) = -2", trTC, Integer(-2))
chk("c_A = -3 == 0 mod 3 (A's structural kill); c_B = -1 != 0 mod 3",
    (trTC - 1, (trTC - 1) % 3, trTC + 1, (trTC + 1) % 3 != 0), (Integer(-3), 0, Integer(-1), True))

print("\n== R3. distribution counts in CLOSED FORM (never running the leg's enumerator) ==")
# outcome-space cardinalities: SG4 4, L1 3, L2 3, L3 3, mb 2, mv 2, mf 2, vz 2, D2 2
TOT = 4 * 3 * 3 * 3 * 2 * 2 * 2 * 2 * 2
chk("total = 3456", TOT, 3456)
per_SG4 = TOT // 4                                   # 864 combos per SG4 value
# Stated rules (.md sec 2 + rows): CONSTRAINED_NO_GAUGE -> B/G4 always.
B_G4 = per_SG4
# FULL_GAUGED -> A/G4 always.
A_G4 = per_SG4
# CONSTRAINED_WITH_EQ_GAUGE -> INCONSISTENT iff L2 effectively PROVEN (L2=PROVEN and L1 != FAIL).
free_after_L1L2 = 3 * 2 * 2 * 2 * 2 * 2              # L3, mb, mv, mf, vz, D2 = 96
INC_G4 = 2 * 1 * free_after_L1L2                     # L1 in {2 non-FAIL} x L2=PROVEN
chk("INCONSISTENT at G4 = 192", INC_G4, 192)
OPEN_G4 = per_SG4 - INC_G4
chk("OPEN at G4 = 672", OPEN_G4, 672)
# UNBUILT (priority: m_forced, then vz_bites, then D2, then generic):
u_mf = per_SG4 // 2                                  # mf=True: 432
inc_mf = 2 * 1 * 3 * (2 * 2 * 2 * 2)                 # L1 non-FAIL x L2=PROVEN x L3 x (mb,mv,vz,D2)
chk("INCONSISTENT via m_forced = 96", inc_mf, 96)
A_G3_mf = u_mf - inc_mf                              # 336
u_vz = per_SG4 // 4                                  # mf=False, vz=True: 216
inc_vz = 2 * 1 * 3 * (2 * 2 * 2)                     # (mb,mv,D2)
chk("INCONSISTENT via vz_bites = 48", inc_vz, 48)
A_G3_vz = u_vz - inc_vz                              # 168
u_dsg = per_SG4 // 8                                 # mf=F, vz=F, D2=DRAFT_SURPRISE: 108
A_G3_dsg = u_dsg // 3                                # L3 = A42 -> G3
A_G2_dsg = u_dsg - A_G3_dsg                          # 72
u_gen = per_SG4 // 8                                 # mf=F, vz=F, D2=MATTER_STANDS: 108
OPEN_G3 = u_gen // 4                                 # mb AND mv -> G3: 27
OPEN_G2 = u_gen - OPEN_G3                            # 81
A_total = A_G4 + A_G3_mf + A_G3_vz + A_G3_dsg + A_G2_dsg
OPEN_total = OPEN_G4 + OPEN_G3 + OPEN_G2
INC_total = INC_G4 + inc_mf + inc_vz
chk("A total = 1476 (G4 864 / G3 540 / G2 72)",
    (A_total, A_G4, A_G3_mf + A_G3_vz + A_G3_dsg, A_G2_dsg), (1476, 864, 540, 72))
chk("OPEN total = 780 (G4 672 / G3 27 / G2 81)", (OPEN_total, OPEN_G4, OPEN_G3, OPEN_G2), (780, 672, 27, 81))
chk("INCONSISTENT total = 336", INC_total, 336)
chk("B total = 864, all at G4 = all CONSTRAINED_NO_GAUGE combos", B_G4, 864)
chk("partition sums to 3456", A_total + OPEN_total + INC_total + B_G4, TOT)
chk("B resolves in ZERO SG4-unbuilt combos (B count == exactly the NO_GAUGE block)", B_G4 == per_SG4, True)

print("\n== R4. adversarial probe of the leg's verdict(): claim (b)'s 'only' ==")
import re, io, os
leg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leg4_verdict_bookkeeping.py")  # repo-relocated path (was ../LEG-4-verdict-bookkeeping.py in scratchpad)
src = open(leg_path, "r", encoding="ascii").read()
m = re.search(r"(A_DOOR = \(.*?\n\n)?(def verdict\(.*?)(?=\n# ---- enumerate)", src, re.S)
seg = re.search(r"A_DOOR = \(.*?\"\)\n", src, re.S).group(0) + re.search(r"def verdict\(.*?(?=\n# ---- enumerate)", src, re.S).group(0)
ns = {}
exec(seg, ns)
verdict = ns["verdict"]
# their headline current-state row:
cur = verdict("UNBUILT", "PASS_BOTH", "PROVEN", "A42", True, True, False, False, "MATTER_STANDS")
chk("headline row: (OPEN, G3)", (cur["bit"], cur["grade"]), ("OPEN", "G3"))
# their named degradation route (VZ PARTIAL pressed -> mv_viable False):
c_mv = verdict("UNBUILT", "PASS_BOTH", "PROVEN", "A42", True, False, False, False, "MATTER_STANDS")
chk("mv_viable=False -> G2 (the leg's named route)", (c_mv["bit"], c_mv["grade"]), ("OPEN", "G2"))
# COUNTEREXAMPLE to 'degrading to G2 ONLY if the VZ mass-hypothesis PARTIAL is pressed':
c_mb = verdict("UNBUILT", "PASS_BOTH", "PROVEN", "A42", False, True, False, False, "MATTER_STANDS")
chk("COUNTEREXAMPLE: mb_closed=False (GP-side pressed) ALSO -> G2, VZ untouched",
    (c_mb["bit"], c_mb["grade"]), ("OPEN", "G2"))
# and the I1 wording probe: built EQ_GAUGE without rigidity -> G4 but NO canon movement
c_eq = verdict("CONSTRAINED_WITH_EQ_GAUGE", "PASS_BOTH", "WEAKENED", "A42", True, True, False, False, "MATTER_STANDS")
chk("I1 wording probe: SG4 built (EQ_GAUGE) yet canon_movement=False (so 'movement iff built' is sloppy)",
    (c_eq["grade"], c_eq["canon_movement"]), ("G4", False))

print("\n== R5. class algebra from canon LEG-D alone ==")
mod3 = lambda t: tuple(x % 3 for x in t)
dirac = (0, 1, 2); bare = (0, 1, 2)
A_cls = mod3(tuple(b - d for b, d in zip(bare, dirac)))
B_cls = mod3(tuple(b + d for b, d in zip(bare, dirac)))
chk("A class (0,0,0); B class (0,2,1) = 2 x Dirac", (A_cls, B_cls, mod3(tuple(2 * d for d in dirac))),
    ((0, 0, 0), (0, 2, 1), (0, 2, 1)))
z24 = lambda t: tuple(x % 24 for x in t)
chk("Z/24: B = 2x(0,16,8) = (0,8,16); A = (0,0,0)",
    (z24((0, 32, 16)), z24((0, 0, 0))), ((0, 8, 16), (0, 0, 0)))
eta = (Fraction(0), Fraction(2, 3), Fraction(-2, 3))
chk("eta (0,2/3,-2/3) mod Z = (0, 2/3, 1/3) = (0,2,1)/3", tuple(e - (e // 1) for e in eta),
    (Fraction(0), Fraction(2, 3), Fraction(1, 3)))
chk("kernel 2h11 - 2 = 38; equivariant 2x(7,6,6) = (14,12,12) sums 38",
    (2 * 20 - 2, tuple(2 * x for x in (7, 6, 6)), sum(2 * x for x in (7, 6, 6))), (38, (14, 12, 12), 38))
chk("PTZ bookkeeping: -19 = -21 + 2 = -20 + 1; -21 = -20 - 1",
    (-21 + 2, -20 + 1, -20 - 1), (-19, -19, -21))
chk("Weitzenboeck: (12/14, (2/4)**2) = (6/7, 1/4)", (Fraction(12, 14), Fraction(2, 4) ** 2),
    (Fraction(6, 7), Fraction(1, 4)))

print("\nTOTAL " + str(N[0]) + " checks; failures: " + str(fails if fails else "none"))
raise SystemExit(1 if fails else 0)
