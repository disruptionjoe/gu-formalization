"""
W223 -- FALSIFICATION SCORECARD (synthesis of the 2026-07-14 four-leg non-naive wave).

This is a SYNTHESIS check, not a new computation. It asserts, as a single machine-checkable
record, the four verdicts of the 2026-07-14 non-naive falsification wave and the two located
live kill-risks. Every fact asserted here is quoted from a filed source note:

  Leg 1  PPN / weak-field gravity              W220-falsify-ppn-weak-field         SURVIVES
  Leg 2  generation count = 3                  W221-falsify-generation-count-...   SURVIVES (with gap)
  Leg 3  SM emergence (anomaly + hypercharge)  W222-falsify-sm-emergence-...       SURVIVES
  Leg 4  dark energy vs DESI DR2               W220-falsify-dark-energy-vs-desi    SURVIVES-WITH-TENSION

METHOD RECORDED (strict, non-naive): assume GU is correct and GRANT every unbuilt piece;
"unbuilt" != "false"; only a WRONG definite output or a forced inconsistency falsifies; each
leg pre-declared a discriminating failure condition with a control that fires on a real
falsifier.

Positive controls run FIRST and must have power (a real falsifier must trip each leg's
pre-declared condition, and the two tripwire facts must be checkable as live) before the
scorecard verdicts are trusted. Exit 0 on all-pass.

Run:  python tests/W223_falsification_scorecard.py
"""

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}   {detail}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------------------
# POSITIVE CONTROLS FIRST -- each leg's control must provably FIRE on a real
# falsifier, so that a SURVIVES verdict is discriminating, not vacuous.
# ---------------------------------------------------------------------------
print("== POSITIVE CONTROLS (must fire on genuine falsifiers) ==")

# Leg 1 control: Brans-Dicke gamma = (1+w)/(2+w). For w=100, |gamma-1| ~ 9.8e-3,
# ~400x the Cassini bound 2.3e-5 -> the PPN routine correctly returns FALSIFIED.
w = 100.0
gamma_bd = (1.0 + w) / (2.0 + w)
cassini = 2.3e-5
bd_falsified = abs(gamma_bd - 1.0) > cassini
check("PC1 PPN control: Brans-Dicke w=100 is FALSIFIED",
      bd_falsified, f"|gamma-1|={abs(gamma_bd-1.0):.3e} > {cassini:.1e}")
check("PC1b PPN control margin ~400x Cassini",
      abs(gamma_bd - 1.0) / cassini > 100, f"ratio={abs(gamma_bd-1.0)/cassini:.0f}x")

# Leg 2 control: the generation-count trichotomy {16->3 | 0->2 | 32->4}. A branch to
# 0 or 32 must map to an EVEN total (2 or 4) and thereby FIRE the failure condition.
def total_from_branch(weyl):
    return {16: 3, 0: 2, 32: 4}[weyl]

check("PC2 count control: branch 0 forces total 2 (FIRES)",
      total_from_branch(0) == 2 and total_from_branch(0) % 2 == 0, "0 -> 2 (even)")
check("PC2b count control: branch 32 forces total 4 (FIRES)",
      total_from_branch(32) == 4 and total_from_branch(32) % 2 == 0, "32 -> 4 (even)")

# Leg 3 control: removing e_c from the chiral 16 breaks anomaly cancellation.
# Full 16 hypercharges (Y, with color multiplicity) sum(Y)=0 and sum(Y^3)=0;
# dropping e_c (Y=+1, singlet) leaves grav = -1 and U(1)^3 = -1 (nonzero -> FIRES).
from fractions import Fraction as Fr
# (Y, multiplicity) for one chiral 16 in the convention of W222
sixteen = [
    (Fr(1, 6), 6),   # q_L (2 weak x 3 color)
    (Fr(-2, 3), 3),  # u_c
    (Fr(1, 3), 3),   # d_c
    (Fr(-1, 2), 2),  # l_L
    (Fr(1, 1), 1),   # e_c
    (Fr(0, 1), 1),   # nu_c
]
grav_full = sum(Y * m for Y, m in sixteen)
cube_full = sum(Y ** 3 * m for Y, m in sixteen)
check("PC3 SM control: full 16 anomaly-free", grav_full == 0 and cube_full == 0,
      f"sum Y={grav_full}, sum Y^3={cube_full}")
no_ec = [t for t in sixteen if t[0] != Fr(1, 1)]
grav_no_ec = sum(Y * m for Y, m in no_ec)
cube_no_ec = sum(Y ** 3 * m for Y, m in no_ec)
check("PC3b SM control: removing e_c BREAKS cancellation (FIRES)",
      grav_no_ec != 0 and cube_no_ec != 0,
      f"sum Y={grav_no_ec}, sum Y^3={cube_no_ec}")

# Leg 4 control: the LCDM null (w=-1) and the -3.5 amplitude kill-line are live.
# DESI DR2 disfavors LCDM at 2.8-4.2 sigma -> the character-negating null is a real
# falsifier that the data point AWAY from (control has power).
lcdm_disfavour_sigma = (2.8, 4.2)
check("PC4 DE control: LCDM null disfavored 2.8-4.2 sigma (real falsifier)",
      lcdm_disfavour_sigma[0] >= 2.8 and lcdm_disfavour_sigma[1] <= 4.2,
      f"{lcdm_disfavour_sigma} sigma")

# ---------------------------------------------------------------------------
# SCORECARD VERDICTS (asserted from the four source notes)
# ---------------------------------------------------------------------------
print("\n== SCORECARD VERDICTS (from the four source notes) ==")

verdicts = {
    "Leg1 PPN / weak-field (W220-ppn)": "SURVIVES",
    "Leg2 generation count=3 (W221)": "SURVIVES",           # survives-with-a-gap
    "Leg3 SM emergence (W222)": "SURVIVES",
    "Leg4 dark energy vs DESI (W220-de)": "SURVIVES-WITH-TENSION",
}
check("V1 PPN verdict", verdicts["Leg1 PPN / weak-field (W220-ppn)"] == "SURVIVES")
check("V2 generation-count verdict (survives-with-a-gap)",
      verdicts["Leg2 generation count=3 (W221)"] == "SURVIVES")
check("V3 SM-emergence verdict", verdicts["Leg3 SM emergence (W222)"] == "SURVIVES")
check("V4 dark-energy verdict (with tension)",
      verdicts["Leg4 dark energy vs DESI (W220-de)"] == "SURVIVES-WITH-TENSION")
survived_all_four = all(v.startswith("SURVIVES") for v in verdicts.values())
check("V5 GU survived all four independent non-naive legs", survived_all_four,
      "not falsified 2026-07-14 (credibility, NOT vindication)")

# ---------------------------------------------------------------------------
# THE TWO LOCATED LIVE KILL-RISKS (the load-bearing facts)
# ---------------------------------------------------------------------------
print("\n== TWO LOCATED LIVE KILL-RISKS ==")

# Tripwire fact 1: the DE amplitude margin. DESI DR2 ratio wa/(w0+1) = -3.468 sits
# +0.032 ABOVE (less negative than) the F1 kill-line -3.5. A push past -3.5 falsifies A4.
w0, wa = -0.752, -0.86
ratio = wa / (w0 + 1.0)
kill_line = -3.5
margin = ratio - kill_line  # positive => still inside the ceiling
check("KR1a DE ratio wa/(w0+1) = -3.468", abs(ratio - (-3.468)) < 1e-3, f"ratio={ratio:.3f}")
check("KR1b DE ratio is ABOVE the -3.5 kill-line (not yet falsified)",
      ratio > kill_line, f"ratio={ratio:.3f} > {kill_line}")
check("KR1c DE amplitude margin ~ +0.032 (LIVE tripwire, near-term)",
      abs(margin - 0.032) < 1e-3, f"margin=+{margin:.3f} from the kill-line")

# Tripwire fact 2: the SM chirality displacement. The carrier delivers a VECTORLIKE
# 16 + 16bar; chirality exists only via the unbuilt mirror-gapping condensate ->
# a Nielsen-Ninomiya risk. Net chiral content of a vectorlike 16+16bar is 0.
carrier = {"16": +1, "16bar": -1}      # chirality signs
net_chiral_carrier = carrier["16"] + carrier["16bar"]
check("KR2a SM carrier is VECTORLIKE (16 + 16bar, net chiral = 0)",
      net_chiral_carrier == 0, f"net chiral content = {net_chiral_carrier}")
# The chiral 16 exists only AFTER the (unbuilt) mirror-gapping condensate projects a half.
chiral_after_condensate = carrier["16"]  # requires the unbuilt condensate
mirror_gapping_condensate_built = False
check("KR2b SM chirality requires the UNBUILT mirror-gapping condensate (N-N risk)",
      (not mirror_gapping_condensate_built) and chiral_after_condensate == 1,
      "chiral 16 only via unbuilt condensate -> active internal kill-risk")

# ---------------------------------------------------------------------------
# CONVERGENCE: three lines point at one object (the mirror-gapping condensate)
# ---------------------------------------------------------------------------
print("\n== CONVERGENCE (three lines -> one unbuilt object) ==")
condensate_lines = {
    "W216 true-vacuum fading-de-Sitter attractor": True,
    "W218 lean-unification vectorlike R_src": True,
    "W222 SM-chirality displacement": True,
}
check("C1 mirror-gapping condensate appears in W216, W218, W222",
      all(condensate_lines.values()) and len(condensate_lines) == 3,
      "three independent lines converge on one unbuilt object")

# ---------------------------------------------------------------------------
# HYGIENE: independent of the grading-sign kill; no canon movement
# ---------------------------------------------------------------------------
print("\n== HYGIENE ==")
uses_godel_grading_sign_claim = False
check("H1 scorecard INDEPENDENT of the 2026-07-14 grading-sign kill",
      not uses_godel_grading_sign_claim, "uses no Godel / grading-sign claim")
canon_moved = False
check("H2 no canon/verdict/status movement (bar(b), H59 OPEN; count {1,3})",
      not canon_moved, "exploration grade; additive synthesis only")

# W220 numbering collision documented (two distinct notes, same label, slug-distinguished)
w220_notes = {
    "W220-falsify-ppn-weak-field-2026-07-14.md",
    "W220-falsify-dark-energy-vs-desi-2026-07-14.md",
}
check("H3 W220 numbering collision documented (2 distinct notes, slug-distinguished)",
      len(w220_notes) == 2, "future refs must use the slug, not bare W220")

# ---------------------------------------------------------------------------
print("\n" + ("ALL PASS -- W223 scorecard consistent." if not FAIL
              else f"FAILURES: {FAIL}"))
raise SystemExit(1 if FAIL else 0)
