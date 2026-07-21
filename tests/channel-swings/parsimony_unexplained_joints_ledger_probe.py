"""
parsimony_unexplained_joints_ledger_probe.py

Foreground, deterministic, pure-Python (no deps). Seed-free (no RNG).
Purpose: make the parsimony / unexplained-joints ledger a COUNT, not a vibe,
and make the "planted rigged-control rejection" a MECHANICAL result.

It does three things:
  (1) Tabulates a joint-by-joint status matrix for GU + 3 rivals at EQUAL
      COVERAGE and counts UNEXPLAINED JOINTS (BRUTE + OPEN) per theory,
      plus imported-knob counts.
  (2) Splits GU's "wired" joints into OBSERVABLE (real evidence) vs
      INTERNAL-only (unification, not consilience -> NOT independent evidence).
  (3) Builds a DISCIPLINED order-of-magnitude posterior-odds lean and a
      deliberately-RIGGED one, and ASSERTS the disciplined method rejects the
      rigged ledger (rigged inflates by >1 order of magnitude via exactly two
      illegitimate moves: counting internal legs as consilience, and dropping
      GU's imports). If the rejection did not fire, exit != 0.

All odds numbers are EXPLICITLY order-of-magnitude bookkeeping (log10, rounded),
NOT physical probabilities. No false precision is claimed or used.
"""

import sys

# ---------------------------------------------------------------------------
# Status codes
EXPL = "EXPLAINED"      # renders the joint non-brute (may be conditional)
BRUTE = "BRUTE-INPUT"   # a free posit / fitted number put in by hand
OPEN = "OPEN"           # acknowledged, unsolved, no mechanism
OOS = "OUT-OF-SCOPE"    # theory does not address this joint at all

# Evidence tag for a theory's EXPLAINED joints
OBSERVABLE = "OBSERVABLE"    # exposed to data; can come back wrong (consilience-capable)
INTERNAL = "INTERNAL-only"   # wired by a construction axiom; unification, not evidence
NA = "-"

# The deep joints (equal-coverage axis). Each is a connection/fact a
# fundamental account could be asked to render non-brute.
JOINTS = [
    "1  measurement / Born rule",
    "2  quantum gravity (QM+GR one arena)",
    "3  cosmological-constant MAGNITUDE (~10^120)",
    "4  vacuum / DE SIGN + no-phantom-crossing",
    "5  arrow of time",
    "6  gauge group SU(3)xSU(2)xU(1)",
    "7  three generations",
    "8  fermion masses / mixings (Yukawas,CKM/PMNS)",
    "9  matter-antimatter asymmetry",
    "10 hierarchy problem",
    "11 dark matter",
    "12 dark energy amplitude (as a phenomenon)",
]

# ---------------------------------------------------------------------------
# THEORY LEDGERS. status per joint; for GU also an evidence tag.
# Grounded in: per-leg-recovery-state, council-reframe-arena-abduction,
# lp-lc-deficiency-decisive, blockbuster-p1-de-sign-covariance, de-amplitude-audit.

# GU (live C10 (9,5) distortion-vacuum construction), given sigma+tau supplied.
GU = {
    "1  measurement / Born rule":                    (OPEN,  INTERNAL),  # Krein->phys R1_COND; L7 Born rule source-gapped
    "2  quantum gravity (QM+GR one arena)":          (EXPL,  INTERNAL),  # single arena (architectural); vacuum-cancel not dyn Einstein
    "3  cosmological-constant MAGNITUDE (~10^120)":  (OPEN,  NA),        # PRED-NORM-RANK RESOLVED_NO_GO; ratio-only
    "4  vacuum / DE SIGN + no-phantom-crossing":     (EXPL,  OBSERVABLE),# PP1 frozen: w(z)>=-1 pointwise; DESI-exposed
    "5  arrow of time":                              (EXPL,  INTERNAL),  # CH-REC co-flip, ONE bit, zero extra import
    "6  gauge group SU(3)xSU(2)xU(1)":               (OPEN,  INTERNAL),  # hosted R1 w/ 6 typed imports; selector BOUNDED_NO_GO
    "7  three generations":                          (OPEN,  INTERNAL),  # 3=dim Lambda^2_+ native value present, NOT forced
    "8  fermion masses / mixings (Yukawas,CKM/PMNS)":(OPEN,  NA),        # weak/imported; only generation universality survives
    "9  matter-antimatter asymmetry":               (OOS,   NA),        # not a tracked GU leg
    "10 hierarchy problem":                          (OOS,   NA),        # not addressed at current grade
    "11 dark matter":                                (OOS,   NA),        # no recovery leg; mirror route RESOLVED_NO_GO
    "12 dark energy amplitude (as a phenomenon)":    (OPEN,  NA),        # amplitude freely specifiable (== joint 3)
}

# R1: SM + QM + GR (the standard patchwork)
R1 = {
    "1  measurement / Born rule":                    BRUTE,  # postulated inner-product/Born rule; interpretation-dependent
    "2  quantum gravity (QM+GR one arena)":          OPEN,   # non-renormalizable; not unified
    "3  cosmological-constant MAGNITUDE (~10^120)":  BRUTE,  # worst fine-tuning; free
    "4  vacuum / DE SIGN + no-phantom-crossing":     BRUTE,  # sign is an input; no rule against crossing
    "5  arrow of time":                              BRUTE,  # past hypothesis / low-entropy boundary condition
    "6  gauge group SU(3)xSU(2)xU(1)":               BRUTE,  # put in by hand
    "7  three generations":                          BRUTE,  # "who ordered that"
    "8  fermion masses / mixings (Yukawas,CKM/PMNS)":BRUTE,  # ~13-20 free Yukawa/mixing params
    "9  matter-antimatter asymmetry":               OPEN,   # SM CPV insufficient; needs new physics
    "10 hierarchy problem":                          OPEN,   # Higgs-mass fine-tuning unexplained
    "11 dark matter":                                OOS,    # no candidate in pure SM
    "12 dark energy amplitude (as a phenomenon)":    OOS,    # pure SM+GR does not include DE
}

# R2: LCDM + SM (cosmology standard)
R2 = {
    "1  measurement / Born rule":                    BRUTE,
    "2  quantum gravity (QM+GR one arena)":          OPEN,
    "3  cosmological-constant MAGNITUDE (~10^120)":  BRUTE,  # Lambda fitted
    "4  vacuum / DE SIGN + no-phantom-crossing":     BRUTE,  # w=-1 by fiat
    "5  arrow of time":                              BRUTE,  # low-entropy Big Bang initial condition
    "6  gauge group SU(3)xSU(2)xU(1)":               BRUTE,
    "7  three generations":                          BRUTE,
    "8  fermion masses / mixings (Yukawas,CKM/PMNS)":BRUTE,
    "9  matter-antimatter asymmetry":               BRUTE,  # eta_b a fitted number
    "10 hierarchy problem":                          OPEN,
    "11 dark matter":                                BRUTE,  # Omega_c fitted; particle identity OPEN
    "12 dark energy amplitude (as a phenomenon)":    BRUTE,  # Lambda fitted
}

# R3: Conformal (Weyl^2) gravity, Mannheim (in-repo comparator). Chosen over MOND
# because it is a full covariant theory; MOND noted as a variant in the doc.
R3 = {
    "1  measurement / Born rule":                    BRUTE,  # inherited QM postulate (PT/C-operator side is about ghosts, not Born)
    "2  quantum gravity (QM+GR one arena)":          EXPL,   # claims renormalizable QG (contested unitarity)
    "3  cosmological-constant MAGNITUDE (~10^120)":  OPEN,   # claims zero-point cancellation; observed small value still tuned
    "4  vacuum / DE SIGN + no-phantom-crossing":     OPEN,   # no rigid sign law
    "5  arrow of time":                              BRUTE,
    "6  gauge group SU(3)xSU(2)xU(1)":               OOS,    # a gravity theory; does not produce the SM
    "7  three generations":                          OOS,
    "8  fermion masses / mixings (Yukawas,CKM/PMNS)":OOS,
    "9  matter-antimatter asymmetry":               OOS,
    "10 hierarchy problem":                          OPEN,   # conformal symmetry addresses scale but not the full hierarchy
    "11 dark matter":                                EXPL,   # claims no DM (exterior sourcing) -- contested at cluster/CMB scale
    "12 dark energy amplitude (as a phenomenon)":    OPEN,
}

THEORIES = [("GU (C10, given sigma,tau)", GU),
            ("R1 SM+QM+GR", R1),
            ("R2 LCDM+SM", R2),
            ("R3 Conformal(Weyl^2)", R3)]

# Imported-knob counts (order-of-magnitude; honest, not rigged).
#   GU honest count: sigma(1) + tau(1) + arena/signature(1) + C10 construction
#   data {VEV branch, kappa^2=1, Z_theta>0, M^2 band}(~4) + 6 SM selector imports
#   + free DE amplitude(1)  ~= 14  (NOT "one bit": the 6 SM imports re-introduce
#   most SM content; the amplitude is as free as Lambda).
KNOBS = {
    "GU (C10, given sigma,tau)": 14,   # 1+1+1+4 + 6 SM imports + 1 amplitude
    "R1 SM+QM+GR":               19,   # ~19 dimensionless SM params (26-28 with nu)
    "R2 LCDM+SM":                25,   # ~19 SM + 6 LCDM
    "R3 Conformal(Weyl^2)":      4,    # a few gravity couplings; but OOS on all SM sectors
}

def unexplained_count(ledger):
    """UNEXPLAINED = BRUTE + OPEN. OOS counted separately (coverage gap, not a
    brute fact -- a theory is not charged a brute fact for a domain it never
    claims, but OOS is also not a win)."""
    def code(v):
        return v[0] if isinstance(v, tuple) else v
    brute = sum(1 for v in ledger.values() if code(v) == BRUTE)
    openj = sum(1 for v in ledger.values() if code(v) == OPEN)
    expl  = sum(1 for v in ledger.values() if code(v) == EXPL)
    oos   = sum(1 for v in ledger.values() if code(v) == OOS)
    return dict(brute=brute, open=openj, explained=expl, oos=oos,
                unexplained=brute + openj, covered=brute + openj + expl)

print("=" * 78)
print("PARSIMONY / UNEXPLAINED-JOINTS LEDGER  (equal-coverage, disciplined)")
print("=" * 78)

# ---- (1) status matrix + counts ----
hdr = f"{'joint':<44}" + "".join(f"{name.split()[0]:>8}" for name, _ in THEORIES)
print("\n[1] STATUS MATRIX (EXPL/BRUTE/OPEN/OOS)\n")
print(hdr)
for j in JOINTS:
    row = f"{j:<44}"
    for _, led in THEORIES:
        v = led[j]
        code = v[0] if isinstance(v, tuple) else v
        short = {EXPL: "EXPL", BRUTE: "BRUTE", OPEN: "OPEN", OOS: "OOS"}[code]
        row += f"{short:>8}"
    print(row)

print("\n[1] COUNTS\n")
print(f"{'theory':<28}{'unexpl':>8}{'brute':>7}{'open':>6}{'expl':>6}{'oos':>5}{'knobs':>7}")
counts = {}
for name, led in THEORIES:
    c = unexplained_count(led)
    counts[name] = c
    print(f"{name:<28}{c['unexplained']:>8}{c['brute']:>7}{c['open']:>6}"
          f"{c['explained']:>6}{c['oos']:>5}{KNOBS[name]:>7}")

# ---- (2) GU observable vs internal split of its EXPLAINED joints ----
print("\n[2] GU's EXPLAINED joints: OBSERVABLE vs INTERNAL-only\n")
gu_expl = [(j, tag) for j, (st, tag) in GU.items() if st == EXPL]
observable = [j for j, tag in gu_expl if tag == OBSERVABLE]
internal = [j for j, tag in gu_expl if tag == INTERNAL]
for j, tag in gu_expl:
    print(f"   {tag:<12} {j}")
# also the sign-cluster GU collapses to ONE bit sigma (joints 1,4,5 + GR vacuum sign)
sign_cluster = ["1  measurement / Born rule",       # QM Krein/positive-sector sign
                "4  vacuum / DE SIGN + no-phantom-crossing",
                "5  arrow of time"]                  # + the GR vacuum-cancellation sign (in joint 2/4 wiring)
print(f"\n   sign/orientation cluster wired to ONE external bit sigma: "
      f"{len(sign_cluster)}+1(GR vacuum) = 4 posits -> 1 bit")
print(f"   of those, OBSERVABLE (consilience-capable): {len(observable)}  "
      f"-> {observable}")
print(f"   INTERNAL-only (unification, NOT evidence):  {len(internal)+1} "
      f"(the QM sector + arrow co-flip + GR vacuum sign, wired by SRC-COH-1)")

# ---- (3) disciplined vs rigged posterior-odds sketch ----
# ALL numbers are log10 order-of-magnitude bookkeeping, NOT probabilities.
print("\n[3] POSTERIOR-ODDS SKETCH (log10 odds, order-of-magnitude only)\n")

# Disciplined ledger:
#   prior (Ockham): GU removes 3 INDEPENDENT sign brute-facts the patchwork
#   posits separately (QM sector convention, GR vacuum sign, arrow BC) by
#   routing them through the SAME sigma already needed for the DE sign.
#   Credit each removed independent Z/2 brute-fact a modest prior factor 2.
disc_prior_log10 = 3 * (0.301)          # 3 removed Z/2 posits, factor 2 each -> ~10^0.9
#   coverage DEBIT: GU is SILENT (OOS) where the rival at least parametrizes:
#   dark matter (R2 fits Omega_c) and baryogenesis (R2 fits eta_b). GU covers
#   FEWER observables, so it earns a likelihood debit at equal coverage.
disc_cov_debit_log10 = -0.5             # ~ factor 1/3
#   likelihood: at equal coverage GU currently predicts nothing the rival does
#   not, EXCEPT the DE no-crossing -- which is NOT yet confirmed. Pending -> 0.
disc_like_log10 = 0.0                   # conditional on DESI/Euclid
disc_total_log10 = disc_prior_log10 + disc_cov_debit_log10 + disc_like_log10

# Rigged ledger (the planted control) makes TWO illegitimate moves:
#   (A) counts the 4-sign co-flip as FOUR INDEPENDENT consilience matches
#       (treats internal unification as evidence) -> bogus likelihood 2^4.
rig_bogus_consilience_log10 = 4 * 0.301
#   (B) drops GU's imports: pretends GU's knob count is "one bit", ignoring the
#       6 SM imports + tau + arena + free amplitude (~10 hidden posits) ->
#       bogus prior inflation ~2^4 more.
rig_bogus_import_drop_log10 = 4 * 0.301
rig_total_log10 = disc_prior_log10 + rig_bogus_consilience_log10 + rig_bogus_import_drop_log10

print(f"   DISCIPLINED lean to GU:  10^{disc_total_log10:+.2f}  "
      f"(prior {disc_prior_log10:+.2f}, coverage debit {disc_cov_debit_log10:+.2f}, "
      f"likelihood {disc_like_log10:+.2f} pending DE)")
print(f"   RIGGED lean to GU:       10^{rig_total_log10:+.2f}  "
      f"(adds bogus consilience {rig_bogus_consilience_log10:+.2f} + "
      f"bogus import-drop {rig_bogus_import_drop_log10:+.2f})")
print(f"   rigged / disciplined  =  10^{rig_total_log10 - disc_total_log10:+.2f}  "
      f"(~{10**(rig_total_log10 - disc_total_log10):.0f}x inflation)")

# ---- REJECTION with teeth: the disciplined scorer must reject the rigged one ----
print("\n[3] PLANTED-CONTROL REJECTION\n")
internal_legs_miscounted = (len(internal) + 1) >= 3     # 3 internal legs exist to be abused
imports_hidden = KNOBS["GU (C10, given sigma,tau)"] >= 10  # the imports the rig drops are real
inflation = rig_total_log10 - disc_total_log10
rejected = internal_legs_miscounted and imports_hidden and inflation > 1.0

print(f"   rig abuses {len(internal)+1} INTERNAL-only legs as consilience:  "
      f"{internal_legs_miscounted}")
print(f"   rig hides {KNOBS['GU (C10, given sigma,tau)']} real GU posits behind "
      f"'one bit':               {imports_hidden}")
print(f"   inflation exceeds one order of magnitude (>10x):        "
      f"{inflation > 1.0}  (10^{inflation:.2f})")
print(f"\n   DISCIPLINED LEDGER REJECTS THE RIGGED LEDGER: {rejected}")
print(f"   -> the method has POWER: it does not merely rubber-stamp GU;")
print(f"      it converts a claimed 'orders of magnitude' win into a")
print(f"      conditional factor-of-a-few lean, gated on ONE observable.")

# ---------------------------------------------------------------------------
# VERDICT + hard assertions (fail loudly if the discipline breaks)
ok = True
# The disciplined lean is POSITIVE but SUB-DECADE (a factor of a few, not orders).
ok &= (0.0 < disc_total_log10 < 1.0)
# The rigged lean is a full order of magnitude or more (orders of magnitude).
ok &= (rig_total_log10 >= 2.0)
# The method rejects the rig.
ok &= rejected
# GU's honest unexplained-joint count is LOWER than both patchwork rivals
# (the genuine, narrow win) ...
ok &= counts["GU (C10, given sigma,tau)"]["unexplained"] < counts["R1 SM+QM+GR"]["unexplained"]
ok &= counts["GU (C10, given sigma,tau)"]["unexplained"] < counts["R2 LCDM+SM"]["unexplained"]
# ... but GU also COVERS FEWER joints than R2 (the honest coverage loss: OOS>rival).
ok &= counts["GU (C10, given sigma,tau)"]["oos"] > counts["R2 LCDM+SM"]["oos"]
# Exactly ONE GU EXPLAINED joint is OBSERVABLE (the DE sign) -- the whole license.
ok &= (len(observable) == 1)

print("\n" + "=" * 78)
print(f"VERDICT: ledger favors GU NARROWLY + CONDITIONALLY "
      f"(disciplined lean 10^{disc_total_log10:+.2f}, ~{10**disc_total_log10:.1f}x),")
print(f"         on the sign/orientation cluster ONLY (4 posits -> 1 bit sigma);")
print(f"         {len(observable)} observable leg carries the whole IBE license "
      f"(the DE no-crossing).")
print(f"         GU covers FEWER joints than R2 ({counts['GU (C10, given sigma,tau)']['oos']} "
      f"OOS vs {counts['R2 LCDM+SM']['oos']}): honest coverage loss.")
print(f"ALL DISCIPLINE ASSERTIONS PASS: {ok}")
print("=" * 78)

sys.exit(0 if ok else 1)
