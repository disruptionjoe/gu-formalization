#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
LEG-B: INDEX BOOKKEEPING on K3 for the RS symbol-adjudication swing (-38 thread).

Task: assuming EACH possible outcome of LEG-A (both branches explicit), do the
exact index bookkeeping on K3:
  * ind(D tensor T_C) = -40 from characteristic classes alone
    (inputs: sigma = -16; p1 = 3*sigma = -48 via the signature theorem; NO chi import)
  * embedded REVERSED-chirality spin-1/2 block contributes ind = -ind(D) = -2
  * additivity (LEG-A branch 1)  =>  ind(Q) = -40 - (-2) = -38
    vs the pinned proxy (same-chirality ghost subtraction) -42 = -40 - (+2)
  * densities 19*p1/24 vs 7*p1/8; mod-3 residues; negative-control table of all
    four candidate conventions (-42, -44, -40, -38) with the gate selecting each
  * cross-check against the literature leg's published values
    (HS Prop 3.1(i): ind Q = -19*Ahat = 19*sigma/8; Bilal 11.47 / CD: 21*sigma/8)

House style: exact arithmetic only (fractions + Z[zeta] integer pairs),
check()-asserts, exit 0.  BLOCKED items are reported honestly and are NOT failures.

FIREWALL: no chi(K3)=24 input, no /8 manufacture (all sigma/8 densities arise as
p1/24-multiples via p1 = 3*sigma), no A-hat = 3, no predetermined 3.
"""

import sys
from fractions import Fraction as F

FAILED = []
N_CHECK = [0]

def check(name, cond):
    N_CHECK[0] += 1
    if not cond:
        FAILED.append(name)
        print("  FAIL  [%03d] %s" % (N_CHECK[0], name))
    return cond

BLOCKED = []
def blocked(item):
    BLOCKED.append(item)

print("=" * 78)
print("LEG-B: exact index bookkeeping on K3  (RS -38 adjudication, index leg)")
print("=" * 78)

# ---------------------------------------------------------------------------
# SECTION 0 -- firewall-audited inputs
# ---------------------------------------------------------------------------
print("\n[0] Inputs (firewall-audited)")

sigma = -16                  # K3 signature (pin; from intersection form, prior canon)
p1 = 3 * sigma               # Hirzebruch signature theorem p1 = 3*sigma; NOT an import
n_fix = 6                    # order-3 Nikulin fixed points (prior verified)
nu_D4 = F(1, 3)              # per-point untwisted Dirac defect (prior verified)
ORDER = 3                    # |G| = 3

check("p1 = 3*sigma = -48 (signature theorem, no chi)", p1 == -48)
check("firewall: chi(K3) never defined/used", "chi" not in globals() and "chi_K3" not in globals())

# ---------------------------------------------------------------------------
# SECTION 1 -- exact Z[zeta] arithmetic for the equivariant multipliers
#              (zeta primitive 3rd root of unity; element (a,b) = a + b*zeta)
# ---------------------------------------------------------------------------
print("\n[1] Z[zeta] multiplier arithmetic")

def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])

def zmul(x, y):
    a, b = x
    c, d = y
    # zeta^2 = -1 - zeta
    return (a * c - b * d, a * d + b * c - b * d)

zeta = (0, 1)
zeta2 = zmul(zeta, zeta)
check("zeta^2 = -1 - zeta", zeta2 == (-1, -1))
check("zeta^3 = 1", zmul(zeta2, zeta) == (1, 0))
check("1 + zeta + zeta^2 = 0", zadd((1, 0), zadd(zeta, zeta2)) == (0, 0))

# local weights (zeta, zeta^{-1}) on T^{1,0}; T_C = T^{1,0} + T^{0,1}
# tr(g^m|T_C) = 2*(zeta^m + zeta^{-m})
tr_TC_by_m = {}
for m in (1, 2):
    zm = zeta if m == 1 else zeta2
    zim = zeta2 if m == 1 else zeta
    s = zadd(zm, zim)
    check("zeta^%d + zeta^-%d = -1 exactly (rational)" % (m, m), s == (-1, 0))
    tr_TC_by_m[m] = 2 * s[0]
check("tr(g^m|T_C) = -2 for both m", tr_TC_by_m == {1: -2, 2: -2})
tr_TC = -2

# spin lift traces (prior verified pin: S+ g-trivial; S- weights zeta, zeta^2)
trSp = 2
trSm = zadd(zeta, zeta2)
check("tr(g|S-) = -1 exactly", trSm == (-1, 0))
check("tr(g|S+) - tr(g|S-) = 3", trSp - trSm[0] == 3)
check("multiplier identity: (trS+ - trS-)*(tr T_C + 1) = -3 = tr(g|V+) - tr(g|V-)",
      3 * (tr_TC + 1) == -3)

# ---------------------------------------------------------------------------
# SECTION 2 -- characteristic-class indices (exact fractions; NO chi anywhere)
#
#   Ahat(K3) degree-4 term: -p1/24        => ind(D) = -p1/24
#   ch(T_C) = 4 + p1 (real bundle complexified, c1 = 0, ch2 = p1)
#   ind(D tensor T_C) = [Ahat * ch(T_C)]_4 = 1*p1 + (-p1/24)*4 = (5/6)*p1
# ---------------------------------------------------------------------------
print("\n[2] Characteristic-class indices")

Ahat_K3 = F(-p1, 24)
ind_D = Ahat_K3
check("ind(D) = -p1/24 = 2", ind_D == 2)
check("ind(D) = -sigma/8 DERIVED via p1=3*sigma (not manufactured)",
      ind_D == F(-sigma, 8) and F(-p1, 24) == F(-3 * sigma, 24))
check("firewall: Ahat(K3) = 2, not 3", Ahat_K3 == 2 and Ahat_K3 != 3)

# [Ahat * ch(T_C)]_4 = 1*p1 + (-p1/24)*4
ind_D_TC = F(p1, 1) + 4 * F(-p1, 24)
check("ind(D tensor T_C) = (5/6)*p1 = -40  (NO chi import)",
      ind_D_TC == F(5, 6) * p1 and ind_D_TC == -40)

# embedded spin-1/2 block of the twistor splitting has REVERSED chirality:
ind_embedded_reversed = -ind_D      # D: S- -> S+
ind_embedded_same = ind_D           # physics ghost subtraction uses SAME chirality
check("embedded reversed-chirality block: ind = -ind(D) = -2", ind_embedded_reversed == -2)

# ---------------------------------------------------------------------------
# SECTION 3 -- LEG-A branch determination (exact certificate re-check)
#
#   Straight-line homotopy determinant: det sigma_t = f(t) * q^4,
#   f(t) = (1/16) * (1 + 3*(1-t)^2)^2      [Design-1 form; Design-3's alpha-form
#   is the same polynomial with alpha = 1-t, up to overall sign convention of det]
#   A real root requires (1-t)^2 = -1/3 : impossible over R.
# ---------------------------------------------------------------------------
print("\n[3] LEG-A branch determination (homotopy certificate, exact)")

def f_cert(t):
    u = 1 - t
    return F(1, 16) * (1 + 3 * u * u) ** 2

root_requirement = F(-1, 3)   # (1-t)^2 would have to equal this
f_has_root_in_R = (root_requirement >= 0)
check("f(t)=0 requires (1-t)^2 = -1/3 < 0: no real root of the certificate", not f_has_root_in_R)
check("f(0) = 1 (full twisted symbol)", f_cert(F(0)) == 1)
check("f(1) = 1/16 = block-diagonal value (detA*detE/q^4)", f_cert(F(1)) == F(1, 16))
grid = [F(k, 24) for k in range(25)]
check("f > 0 on rational grid over [0,1] (24 subdivisions + endpoints)",
      all(f_cert(t) > 0 for t in grid))
check("min of f on [0,1] is f(1) = 1/16 (grid-consistent)",
      min(f_cert(t) for t in grid) == F(1, 16))

LEG_A_BRANCH = 1 if not f_has_root_in_R else 2
check("LEG-A actual outcome = branch 1 (homotopy stays elliptic)", LEG_A_BRANCH == 1)

# ---------------------------------------------------------------------------
# SECTION 4 -- BOTH branches of the index bookkeeping, explicitly
# ---------------------------------------------------------------------------
print("\n[4] Index bookkeeping under BOTH LEG-A branches")

# Literature imports (verified by the literature leg; flagged as imports here):
LIT_HS_indQ_Ahat_form = -19 * Ahat_K3        # HS Prop 3.1(i): ind Q = -19*Ahat(M)
LIT_HS_indQ_sigma_form = F(19, 8) * sigma    # ... = (19/8)*sigma(M)
LIT_Bilal_AGW_pinned = F(21, 8) * sigma      # Bilal eq 11.47 / Christensen-Duff: 21*sigma/8
LIT_BM_dimker_Q_K3 = 38                      # Baer-Mazzeo Rem 5.3: RS(K3) = 38 (sharp)

# ---- BRANCH 1 (ACTUAL): homotopy through elliptic symbols certified =>
#      index additivity: ind(D tensor T_C) = ind(Q) + ind(embedded reversed block)
indQ_branch1 = ind_D_TC - ind_embedded_reversed
check("BRANCH 1: ind(Q) = -40 - (-2) = -38 (derived, additivity)", indQ_branch1 == -38)
check("BRANCH 1: equivalently ind(Q) = ind(D_TM) + ind(D) [HS eq (11) form]",
      indQ_branch1 == ind_D_TC + ind_D)
check("BRANCH 1: derived -38 == published -19*Ahat (HS Prop 3.1(i))",
      indQ_branch1 == LIT_HS_indQ_Ahat_form)
check("BRANCH 1: derived -38 == published (19/8)*sigma", indQ_branch1 == LIT_HS_indQ_sigma_form)
check("BRANCH 1: |ind Q| = 38 consistent with BM dim ker Q(K3) = 38, one chirality",
      abs(indQ_branch1) == LIT_BM_dimker_Q_K3)

# pinned proxy (branch-independent: it is a density definition, not a homotopy output)
indRS_pinned = ind_D_TC - ind_embedded_same
check("pinned proxy: ind = -40 - (+2) = -42 (same-chirality ghost subtraction)",
      indRS_pinned == -42)
check("pinned proxy == published 21*sigma/8 (Bilal 11.47 / CD gate)",
      indRS_pinned == LIT_Bilal_AGW_pinned)
check("fork size: candidate B - candidate A = 2*ind(D) = 4 exactly",
      indQ_branch1 - indRS_pinned == 2 * ind_D == 4)
check("K-theory: [T_C + 1] - [T_C - 1] = 2*[1]  (index avatar of the class identity)",
      (ind_D_TC + ind_D) - (ind_D_TC - ind_D) == 2 * ind_D)

# ---- BRANCH 2 (COUNTERFACTUAL, documented explicitly): certificate root in [0,1]
#      => the straight-line path leaves elliptic symbols => additivity UNCERTIFIED
#      by this path => the in-house derivation of ind(Q) is BLOCKED (not false).
branch2 = {
    "status": "UNCERTIFIED (counterfactual: did NOT occur; f > 0 on [0,1])",
    "indQ_derived_inhouse": None,          # BLOCKED under this branch
    "indQ_literature_import": LIT_HS_indQ_Ahat_form,   # HS applies AS directly to Q's
    "provenance": "HS Prop 3.1(i) import only (AS on Q's compressed symbol; "
                  "no additivity needed on their side)",
    "pinned_minus42": indRS_pinned,        # unaffected: density definition
    "mod3_fork": "survives via literature import + class law, provenance downgraded",
}
check("BRANCH 2 bookkeeping: literature import equals branch-1 derived value "
      "(counterfactual changes provenance, not the number)",
      branch2["indQ_literature_import"] == indQ_branch1)
check("BRANCH 2 bookkeeping: in-house derivation marked BLOCKED (None), never fabricated",
      branch2["indQ_derived_inhouse"] is None)
check("BRANCH 2 bookkeeping: pinned -42 unaffected by homotopy failure",
      branch2["pinned_minus42"] == -42)
blocked("BRANCH-2 (counterfactual only; did not occur): had the homotopy certificate "
        "had a root in [0,1], the in-house additivity route to ind(Q) would be "
        "BLOCKED; -38 would rest solely on the HS Prop 3.1(i) literature import.")

# ---------------------------------------------------------------------------
# SECTION 5 -- densities, residues, class law
# ---------------------------------------------------------------------------
print("\n[5] Densities, mod-3 residues, class law")

check("density B: ind(Q) = (19/24)*p1", indQ_branch1 == F(19, 24) * p1)
check("density A: ind(pinned) = (7/8)*p1 = (21/24)*p1",
      indRS_pinned == F(7, 8) * p1 and F(7, 8) == F(21, 24))
check("density bare: ind(D tensor T_C) = (5/6)*p1 = (20/24)*p1",
      ind_D_TC == F(5, 6) * p1 and F(5, 6) == F(20, 24))
check("density Dirac: ind(D) = (-1/24)*p1", ind_D == F(-1, 24) * p1)
check("densities in sigma: 19/8 vs 21/8 vs 5/2 vs -1/8 (all via p1=3*sigma, no /8 input)",
      indQ_branch1 == F(19, 8) * sigma and indRS_pinned == F(21, 8) * sigma
      and ind_D_TC == F(5, 2) * sigma and ind_D == F(-1, 8) * sigma)

check("residue: -38 == 1 mod 3", (-38) % 3 == 1)
check("residue: -42 == 0 mod 3", (-42) % 3 == 0)
check("residue: -40 == 2 mod 3", (-40) % 3 == 2)
check("residue: -44 == 1 mod 3", (-44) % 3 == 1)

def classes_mod3(ind):
    # class law (referee-derived, verified prior swing): rho_k == -(k/3)*ind mod Z
    return tuple((-k * ind) % 3 for k in range(3))

check("class law: ind -38 -> classes (0,2,1)/3  NONZERO", classes_mod3(-38) == (0, 2, 1))
check("class law: ind -42 -> classes (0,0,0)/3  ZERO", classes_mod3(-42) == (0, 0, 0))
check("class law: ind -40 -> classes (0,1,2)/3", classes_mod3(-40) == (0, 1, 2))
check("class law: ind -44 -> classes (0,2,1)/3", classes_mod3(-44) == (0, 2, 1))
check("class law: Dirac ind +2 -> classes (0,1,2)/3 (matches prior verified Dirac rho)",
      classes_mod3(2) == (0, 1, 2))

# rho relation at class level: rho_B = rho_A + 2*rho_Dirac (mod 3 classes)
clA, clB, clD = classes_mod3(-42), classes_mod3(-38), classes_mod3(2)
check("class relation: classes(B) = classes(A) + 2*classes(Dirac) mod 3",
      tuple((a + 2 * d) % 3 for a, d in zip(clA, clD)) == clB)

# sign-convention robustness (Design-1 risk 1): if published sign flipped, +38:
check("sign-robustness: +38 -> classes (0,1,2), still NONZERO; residue swaps 1<->2 only",
      classes_mod3(38) == (0, 1, 2) and (38 % 3 != 0) and ((-38) % 3 != 0))

# ---------------------------------------------------------------------------
# SECTION 6 -- equivariant cross-checks (Atiyah-Bott; additivity equivariantly)
# ---------------------------------------------------------------------------
print("\n[6] Equivariant cross-checks")

def ind_phi_twist(mult):
    # ind_phi = n_fix * nu_D4 * tr(g|twist);  nu_D4 = 1/3, 6 points => 2*mult
    v = n_fix * nu_D4 * mult
    assert v.denominator == 1
    return int(v)

ind_phi_D = ind_phi_twist(1)
ind_phi_D_TC = ind_phi_twist(tr_TC)
ind_phi_Q = ind_phi_twist(tr_TC + 1)
ind_phi_pinned = ind_phi_twist(tr_TC - 1)
check("ind_phi(D) = 6*(1/3)*1 = 2 (matches prior verified pin)", ind_phi_D == 2)
check("ind_phi(D tensor T_C) = 6*(1/3)*(-2) = -4", ind_phi_D_TC == -4)
check("ind_phi(Q) = 6*(1/3)*(-1) = -2 (multiplier c_B = tr T_C + 1 = -1)", ind_phi_Q == -2)
check("ind_phi(pinned) = 6*(1/3)*(-3) = -6 (multiplier c_A = tr T_C - 1 = -3)",
      ind_phi_pinned == -6)
check("structural kill: c_A = -3 == 0 mod 3; c_B = -1 not== 0 mod 3",
      (tr_TC - 1) % 3 == 0 and (tr_TC + 1) % 3 != 0)
check("equivariant additivity: ind_phi(Q) = ind_phi(D tensor T_C) - ind_phi(rev block) "
      "= -4 - (-2) = -2", ind_phi_Q == ind_phi_D_TC - (-ind_phi_D))
check("equivariant pinned: ind_phi = -4 - (+2) = -6", ind_phi_pinned == ind_phi_D_TC - ind_phi_D)

# ---------------------------------------------------------------------------
# SECTION 7 -- negative-control table: all four candidate conventions + Dirac
# ---------------------------------------------------------------------------
print("\n[7] Negative-control table (which gate selects each candidate)")

rows = [
    # (name, twist class, index, equivariant multiplier)
    ("A pinned/AGW ghost-sub", "T_C - 1", ind_D_TC - ind_D, tr_TC - 1),
    ("B geometric RS (Q)",     "T_C + 1", ind_D_TC + ind_D, tr_TC + 1),
    ("bare twisted Dirac",     "T_C",     ind_D_TC,          tr_TC),
    ("double subtraction",     "T_C - 2", ind_D_TC - 2 * ind_D, tr_TC - 2),
    ("Dirac baseline",         "1",       ind_D,             1),
]

expected = {
    "A pinned/AGW ghost-sub": (-42, F(7, 8),  0, (0, 0, 0), -6),
    "B geometric RS (Q)":     (-38, F(19, 24), 1, (0, 2, 1), -2),
    "bare twisted Dirac":     (-40, F(5, 6),  2, (0, 1, 2), -4),
    "double subtraction":     (-44, F(11, 12), 1, (0, 2, 1), -8),
    "Dirac baseline":         (2,   F(-1, 24), 2, (0, 1, 2), 2),
}

gate_21s8_hits, gate_19s8_hits = [], []
hdr = "%-24s %-8s %6s %10s %6s %10s %7s %8s %8s" % (
    "candidate", "twist", "ind", "ind/p1", "res3", "classes", "i_phi", "orb_int", "gate")
print("  " + hdr)
print("  " + "-" * len(hdr))
for name, twist, ind, mult in rows:
    ind_int = int(ind)
    dens = F(ind_int, p1) if p1 != 0 else None
    res = ind_int % 3
    cls = classes_mod3(ind_int)
    iphi = ind_phi_twist(mult)
    e_ind, e_dens, e_res, e_cls, e_iphi = expected[name]
    check("table[%s]: ind = %d" % (name, e_ind), ind_int == e_ind)
    check("table[%s]: density = %s * p1" % (name, e_dens), ind == e_dens * p1)
    check("table[%s]: residue mod 3 = %d" % (name, e_res), res == e_res)
    check("table[%s]: classes = %s" % (name, str(e_cls)), cls == e_cls)
    check("table[%s]: ind_phi = %d" % (name, e_iphi), iphi == e_iphi)
    # orbifold integrality: (ind + ind_phi(g) + ind_phi(g^2))/3 in Z (traces rational => equal)
    orb = F(ind_int + 2 * iphi, 3)
    check("table[%s]: orbifold integrality (ind + 2*ind_phi)/3 in Z" % name,
          orb.denominator == 1)
    # residue-multiplier law: ind == 2*mult mod 3 (from orbifold integrality)
    check("table[%s]: residue law ind == 2*multiplier mod 3" % name,
          ind_int % 3 == (2 * mult) % 3)
    g21 = (ind == F(21, 8) * sigma)
    g19 = (ind == F(19, 8) * sigma)
    if g21:
        gate_21s8_hits.append(name)
    if g19:
        gate_19s8_hits.append(name)
    gate = "21s/8" if g21 else ("19s/8" if g19 else "none")
    print("  %-24s %-8s %6d %10s %6d %10s %7d %8s %8s" % (
        name, twist, ind_int, str(dens), res, str(cls), iphi, str(int(orb)), gate))

check("gate 21*sigma/8 (physics/AGW/CD) selects EXACTLY the pinned candidate A",
      gate_21s8_hits == ["A pinned/AGW ghost-sub"])
check("gate 19*sigma/8 (HS Prop 3.1(i) mathematics) selects EXACTLY the geometric Q",
      gate_19s8_hits == ["B geometric RS (Q)"])
check("the two published gates select DIFFERENT candidates: the fork is real and "
      "two-sided-published; neither gate is unique anymore",
      gate_21s8_hits != gate_19s8_hits)
check("negative controls -40 and -44 pass NO published gate",
      all(n not in gate_21s8_hits + gate_19s8_hits
          for n in ("bare twisted Dirac", "double subtraction")))

# ---------------------------------------------------------------------------
# SECTION 8 -- BLOCKED items (honest, non-fatal) and firewall audit
# ---------------------------------------------------------------------------
print("\n[8] BLOCKED items and firewall audit")

blocked("CARRIER IDENTIFICATION (SG4 MISSING-CARRIER): whether the GU generation-arena "
        "operator is (A) the ghost-subtracted gravitino complex (-42, classes (0,0,0)) "
        "or (B) the geometric gamma-traceless RS operator Q (-38, classes (0,2,1)) is "
        "an identification question, NOT arithmetic; this leg computes both and selects "
        "neither.")
blocked("LITERATURE IMPORTS: -19*Ahat = 19*sigma/8 (HS Prop 3.1(i)), 21*sigma/8 "
        "(Christensen-Duff via Bilal eq 11.47), dim ker Q(K3) = 38 (BM Rem 5.3) are "
        "gates verified by the literature leg's fetches; this leg cross-checks against "
        "them but does not re-derive the papers.")
blocked("AGW PRIMARY (Nucl. Phys. B 234, 1984) remains unfetched (paywalled); the -42 "
        "attribution rides two verified secondaries (Bilal 11.47; HS Remark 3.6) plus "
        "the prior adversarially-verified canon pin.")

print("  BLOCKED (%d items, reported not failed):" % len(BLOCKED))
for i, b in enumerate(BLOCKED, 1):
    print("   B%d. %s" % (i, b))

print("\n  FIREWALL AUDIT: inputs = {sigma=-16, p1=3*sigma (signature thm), 6 Nikulin")
print("  fixed points, weights (zeta,zeta^-1), nu_D4=1/3, |G|=3, spin-lift traces}.")
print("  chi(K3)=24 never used; Ahat=2 (checked, not 3); every sigma/8 density arose")
print("  as a p1/24 multiple via p1=3*sigma; -38 was DERIVED as -40+2, never imported")
print("  (the imports were used only as gates, after derivation).")

# ---------------------------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("SUMMARY")
print("=" * 78)
print("  LEG-A actual branch: 1 (certificate f(t) = (1/16)(1+3(1-t)^2)^2 > 0 on [0,1])")
print("  BRANCH 1 (actual):   ind(Q) = ind(D x T_C) - ind(rev spin-1/2 block)")
print("                             = -40 - (-2) = -38 = (19/24)p1 = 19*sigma/8")
print("                       matches HS Prop 3.1(i) = -19*Ahat = -38.  Residue 1 mod 3,")
print("                       classes (0,2,1)/3 NONZERO;  ind_phi(Q) = -2 (c_B = -1).")
print("  BRANCH 2 (counterfactual, did not occur): in-house additivity BLOCKED;")
print("                       -38 would stand on the HS import alone; pinned -42 intact.")
print("  PINNED PROXY:        -42 = -40 - (+2) = (7/8)p1 = 21*sigma/8 (Bilal/CD gate),")
print("                       residue 0 mod 3, classes (0,0,0), c_A = -3 == 0 mod 3.")
print("  FORK:                B - A = 2*ind(D) = 4; classes(B) = classes(A)+2*classes(D).")
print("  Negative controls:   -40 (bare) and -44 (double-sub) pass no published gate.")
print("  Checks: %d run, %d failed." % (N_CHECK[0], len(FAILED)))

if FAILED:
    print("\nFAILED CHECKS:")
    for nm in FAILED:
        print("  - " + nm)
    sys.exit(1)
print("\nALL CHECKS PASS  (exit 0; %d BLOCKED items reported above, none fabricated)"
      % len(BLOCKED))
sys.exit(0)
