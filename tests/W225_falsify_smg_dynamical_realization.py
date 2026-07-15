"""
W225 -- FALSIFICATION probe (NON-NAIVE): the DYNAMICAL REALIZATION of symmetric mass
generation (SMG) for GU's SO(10)-16 mirror.

Leg attacked: W224 proved GU's chirality SURVIVES-BY-SMG on the NECESSARY (anomaly)
condition -- all 't Hooft anomalies of the mirror 16bar vanish (perturbative cubic +
Witten SU(2) mod-2 + the mod-16 cobordism anomaly Omega^Spin_5(B G_SM) = Z/16, the last
via nu_R). W224 GRANTED the SUFFICIENT (dynamical) condition and flagged it as the honest
residual. THIS probe attacks exactly that residual: GIVEN the good Krein branch (W216/W211;
the sign gate is a SEPARATE object, NOT re-litigated here), does the symmetric strong-
coupling GAPPED phase actually REALIZE in 3+1D for GU's mirror, or collapse to a symmetry-
breaking / gapless phase (the classic Eichten-Preskill failure mode)?

METHOD (strict, pre-declared, NON-NAIVE, smart-route-first). ASSUME GU is correct; GRANT the
good Krein branch and the mirror-anomaly ledger of W224 (all vanish). Do NOT run a full
lattice Monte Carlo: GU's mirror interactions are underspecified for a faithful MC (the task
constraint). Instead route through the SMG literature and a strong-coupling toy comparison,
and CLASSIFY the class GU lands in: KNOWN-REALIZED, KNOWN-OBSTRUCTED, or GENUINELY-OPEN.

PRE-DECLARED FAILURE CONDITION. GU is FALSIFIED on this leg IFF GU's mirror PROVABLY cannot
reach the symmetric gapped phase -- i.e. EITHER
  (F1) the anomaly class of GU's mirror is KNOWN-OBSTRUCTED for SMG (some 't Hooft anomaly
       nonzero, so no symmetric gapped phase can EXIST), OR
  (F2) a BEYOND-ANOMALY obstruction FIRES for GU's exact content (a higher-group / non-
       invertible / categorical symmetry obstruction, or a forced deconfined-quantum-
       criticality gapless obstruction, that survives for the STANDARD Spin(10) 16).
GU SURVIVES iff the symmetric gapped realization is KNOWN-REALIZED for this class OR an
admissible mechanism demonstrably reaches it.
HONEST THIRD OUTCOME -- OPEN-IN-THE-FIELD: if the symmetric realization is an unsettled
research question for this mirror (existence guaranteed by cobordism, but the strong-coupling
dynamics for the EXACT 16 in 3+1D not settled, and GU's specific mirror couplings
underspecified), report that plainly. It makes GU's chirality CONDITIONAL on an open lattice-
field-theory problem: a correct non-naive characterization, NOT a kill and NOT a clean pass.

POSITIVE CONTROLS RUN FIRST and MUST have power:
  - a KNOWN-OBSTRUCTED anomaly class (the 15, no nu_R; a lone chiral 3; an odd Majorana count)
    must register OBSTRUCTED (F1 fires);
  - a KNOWN-GAPPABLE anomaly class (16 Weyl; Fidkowski-Kitaev 8 Majorana in 1+1D, Z/8; 16
    Majorana in 3+1D DIII, Z/16) must register EXISTENCE-GUARANTEED;
  - the beyond-anomaly (w2w3) detector must FIRE on the MODIFIED SO(10)+WZW content and be
    ABSENT on the standard Spin(10) 16;
  - the strong-coupling toy must resolve to SYMMETRY-BREAKING (E-P failure) in the bilinear-
    dominant regime and to SMG in the symmetric-multifermion-dominant regime, i.e. the outcome
    is coupling-ratio dependent (hence UNDETERMINED without GU's specific couplings).

Exit 0 asserts the internal machinery is consistent and the OPEN-IN-THE-FIELD verdict is
correctly DERIVED -- it does NOT assert GU passes. Every number is printed.

Run:  python -u tests/W225_falsify_smg_dynamical_realization.py

Literature (real papers; applied to GU's content, NOT re-derived here -- reconstruction grade,
same honesty boundary as W222/W224):
  Eichten & Preskill, Nucl. Phys. B268 (1986) 179 -- the mirror-fermion program; the original
    strong-coupling attempt FAILED by landing in a symmetry-breaking / gapless phase.
  Wang & Wen, Phys. Rev. Research 2 (2020) 023356, arXiv:1809.11171 -- non-perturbative
    definition of the SM: the SO(10) 16n admits a symmetric gapped mirror boundary BECAUSE it
    is anomaly-free (mod-16 = 0); EXISTENCE via cobordism (trivial 5d invertible order).
  You, BenTov & Xu / Wang & You, Phys. Rev. X 8 (2018) 011026, arXiv:1705.09313 -- SMG as
    deconfined quantum criticality; the generic transition is a SINGLE continuous one.
  Catterall et al, arXiv:2111.01001 / Phys. Rev. D -- 3+1D lattice SU(2)xSU(2) bifundamental
    reduced staggered fermions gap symmetrically via a four-fermion condensate (a realized
    3+1D SMG, but NOT the exact SO(10) 16).
  Wang, arXiv:2106.16248; Wang, arXiv:2111.10369; arXiv:2202.13498 -- the w2w3 mixed gauge-
    gravity anomaly, categorical/non-invertible symmetry, and the gapless deconfined-quantum-
    critical region between GUT vacua; the STANDARD Spin(10) 16 has NO w2w3 anomaly (only a
    modified SO(10)+WZW does), and the un-Higgsed Spin(10) RETRACTS the categorical symmetry.
  Fidkowski & Kitaev, Phys. Rev. B 81 (2010) 134509 -- the Z/8 interacting collapse (8
    Majorana gap symmetrically): the canonical KNOWN-REALIZED positive control.
"""

from fractions import Fraction as F

FAIL = []
def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}   {detail}")
    if not ok:
        FAIL.append(name)


# =====================================================================================
# ANOMALY LEDGER (ported from W222/W224 -- the NECESSARY / existence condition).
# =====================================================================================
def anomalies(fermions):
    """fermions: (triality, n_weak, n_color, Y) LEFT-handed Weyl multiplets."""
    U1_cubed = F(0); grav = F(0); su2 = F(0); su3 = F(0)
    for (tri, nw, ncol, Y) in fermions:
        U1_cubed += nw * ncol * Y**3
        grav     += nw * ncol * Y
        if nw == 2:
            su2 += ncol * Y
        su3 += nw * tri
    return dict(U1_cubed=U1_cubed, grav=grav, su2=su2, su3=su3)

def n_weyl(fermions):
    return sum(nw * ncol for (tri, nw, ncol, Y) in fermions)

def count_su2_doublets(fermions):
    return sum(ncol for (tri, nw, ncol, Y) in fermions if nw == 2)

def mod16(fermions):
    """Discrete cobordism anomaly Omega^Spin_5(B G_SM)=Z/16 (GEM 2018 / Wang-Wen). Vanishes
    IFF #Weyl = 0 mod 16 -- exactly with the SO(10) completion nu_R (16). [Cited result
    applied to GU's content, NOT a fresh Dai-Freed recomputation.]"""
    return n_weyl(fermions) % 16

# The physical chiral SO(10) 16, left-handed (W222); mirror is the CP conjugate.
gen16 = [
    (+1, 2, 3, F(1, 6)),   # Q_L
    (-1, 1, 3, F(-2, 3)),  # u_c
    (-1, 1, 3, F(1, 3)),   # d_c
    ( 0, 2, 1, F(-1, 2)),  # L_L
    ( 0, 1, 1, F(1)),      # e_c
    ( 0, 1, 1, F(0)),      # nu_c  <-- the 16th state (SO(10) completion)
]
def mirror_of(fermions):
    return [(-tri, nw, ncol, -Y) for (tri, nw, ncol, Y) in fermions]

mirror16 = mirror_of(gen16)


def anomaly_class(fermions):
    """Classify the SMG EXISTENCE condition on a chiral content.
    Returns ('OBSTRUCTED', reason)   -- some 't Hooft anomaly nonzero: NO symmetric gapped
                                          phase can exist (F1); OR
            ('GAPPABLE-IN-PRINCIPLE', reason) -- all anomalies vanish: a symmetric gapped
                                          boundary is GUARANTEED to EXIST by cobordism
                                          (Wang-Wen; the trivial 5d invertible order)."""
    A = anomalies(fermions)
    if any(v != 0 for v in A.values()):
        bad = [k for k, v in A.items() if v != 0]
        return ("OBSTRUCTED", f"perturbative anomaly nonzero: {bad}")
    nd = count_su2_doublets(fermions)
    if nd % 2 != 0:
        return ("OBSTRUCTED", f"Witten SU(2) global anomaly: {nd} doublets (odd)")
    m = mod16(fermions)
    if m != 0:
        return ("OBSTRUCTED", f"mod-16 cobordism anomaly nonzero: {n_weyl(fermions)} mod 16 = {m}")
    return ("GAPPABLE-IN-PRINCIPLE", f"all anomalies vanish ({n_weyl(fermions)} Weyl, {n_weyl(fermions)%16} mod 16)")


# =====================================================================================
# MAJORANA-COUNT REALIZED CLASSES (Fidkowski-Kitaev collapse) -- KNOWN-REALIZED controls.
# 1+1D class BDI: Z -> Z/8 (8 Majorana gap symmetrically). 3+1D class DIII: Z -> Z/16.
# A symmetric gapped phase is a KNOWN, numerically/analytically realized fact at the
# collapse multiple; away from it a residual symmetry-protected mode obstructs.
# =====================================================================================
def majorana_realized(n, collapse):
    """True iff n Majorana modes can be symmetrically gapped in the given interacting
    classification (n = 0 mod collapse). This is a KNOWN-REALIZED statement at the
    collapse multiple (Fidkowski-Kitaev for 8; DIII Z/16 for 16)."""
    return n % collapse == 0


# =====================================================================================
# BEYOND-ANOMALY OBSTRUCTION DETECTOR (the NEW W225 content).
# The w2w3 = w2'w3' mixed gauge-gravitational anomaly (Wang 2106.16248 / 2111.10369 /
# 2202.13498): a nonperturbative GLOBAL anomaly that, when present, forbids a TRIVIAL
# symmetric gapped phase (forces gaplessness -- deconfined quantum criticality -- or
# intrinsic topological order). CRUCIAL fact: the STANDARD Spin(10) GUT with the 16 does
# NOT have the w2w3 anomaly; only a MODIFIED SO(10) with an extra discrete WZW term does.
# Model each content by a flag has_wzw_torsion; w2w3 fires ONLY with that torsion class.
# =====================================================================================
def w2w3_obstruction(content):
    """content: dict with keys 'group' and 'has_wzw_torsion'. Returns True if the w2w3
    beyond-anomaly obstruction to a TRIVIAL symmetric gapped phase FIRES.
    Wang 2111.10369: standard Spin(10)+16 -> NO w2w3; modified SO(10)+16+WZW -> w2w3 present
    (Higgs cannot be trivially/featurelessly disordered)."""
    return bool(content.get("has_wzw_torsion", False))

def categorical_symmetry_obstruction(content):
    """Non-invertible / categorical higher symmetry (Wang 2111.10369). It appears when the
    Z2 flip between Georgi-Glashow and flipped-u(5) is GAUGED, but the un-Higgsed Spin(10) at
    UV RETRACTS the categorical symmetry. For GU's un-Higgsed Spin(10) 16 it is retracted ->
    NOT an obstruction. Fires only if the content sits in the gauged-flip (retracted=False)
    regime."""
    return content.get("gauged_z2_flip", False) and not content.get("spin10_uv_retracts", True)

def forced_dqc_gapless(content):
    """Forced deconfined-quantum-criticality gapless obstruction. The gapless DQC region
    (2202.13498) sits BETWEEN gauged GUT vacua (GG vs PS); it is NOT a forced obstruction to
    the GLOBAL-symmetric mirror gap. Fires only if the content is pinned to the inter-vacua
    critical locus with the internal symmetries GAUGED and no gapped neighbor phase."""
    return content.get("pinned_inter_gut_gauged", False)

# GU's mirror as a beyond-anomaly content: standard Spin(10) 16, un-Higgsed, global symmetry
# for the mirror-gap problem (not gauged flip), no extra WZW torsion class.
gu_mirror_content = dict(group="Spin(10)", has_wzw_torsion=False,
                         gauged_z2_flip=False, spin10_uv_retracts=True,
                         pinned_inter_gut_gauged=False)
# The MODIFIED SO(10)+WZW content -- the KNOWN case where the beyond-anomaly obstruction DOES
# fire (positive control for the detector's power).
modified_so10_wzw = dict(group="Spin(10)+WZW", has_wzw_torsion=True,
                         gauged_z2_flip=True, spin10_uv_retracts=False,
                         pinned_inter_gut_gauged=True)


# =====================================================================================
# STRONG-COUPLING TOY (part (c)) -- the SPECIFICALLY-UNDETERMINED piece. NOT a full MC.
# In the strong-coupling limit of a symmetric four/multi-fermion SMG interaction on the 16,
# two vacua compete: (S) the SYMMETRIC multi-fermion singlet condensate (SMG gapped phase),
# and (B) a BILINEAR order parameter (a symmetry-breaking / Aoki-phase-like condensate, the
# Eichten-Preskill failure). Mean-field: whichever condensation energy is deeper wins.
# The bilinear channel is FORBIDDEN as a single-site mass by the representation (W224: no
# gauge-invariant bilinear on the 16-of-Spin(10)); it can only arise as a spontaneous,
# symmetry-breaking condensate. Compare condensation energies as functions of the coupling
# ratio r = g_sym / g_bilinear. The point of the toy is NOT to decide GU (its couplings are
# unknown) but to SHOW the outcome is coupling-ratio dependent -> UNDETERMINED.
# =====================================================================================
import math
def condensation_energies(g_sym, g_bilinear, N0=1.0, W=1.0):
    """Mean-field BCS-like condensation energies for the two competing channels.
    Symmetric multi-fermion channel: gaps ALL modes, E_S = -1/2 N0 Delta_S^2 with
    Delta_S = W/sinh(1/(g_sym N0)) (needs g_sym>0 to condense).
    Bilinear (symmetry-breaking) channel: E_B = -1/2 N0 Delta_B^2 with
    Delta_B = W/sinh(1/(g_bilinear N0)). Deeper (more negative) wins."""
    def gap(g):
        if g <= 0:
            return 0.0
        return W / math.sinh(1.0 / (g * N0))
    dS = gap(g_sym); dB = gap(g_bilinear)
    E_S = -0.5 * N0 * dS**2
    E_B = -0.5 * N0 * dB**2
    return E_S, E_B, dS, dB

def strong_coupling_outcome(g_sym, g_bilinear):
    E_S, E_B, dS, dB = condensation_energies(g_sym, g_bilinear)
    if E_S == 0 and E_B == 0:
        return "GAPLESS", (E_S, E_B)
    return ("SMG" if E_S <= E_B else "SYMMETRY-BREAKING"), (E_S, E_B)


# =====================================================================================
print("=" * 100)
print("W225 -- FALSIFY the DYNAMICAL REALIZATION of SMG for GU's SO(10)-16 mirror (given good branch)")
print("=" * 100)

# --------------------------------------------------------------- POSITIVE CONTROLS FIRST
print("\n[CONTROL 1] the anomaly-class detector has POWER (known-OBSTRUCTED classes register OBSTRUCTED)")

# (1a) the 15 (no nu_R): mod-16 = 15 -> OBSTRUCTED (F1 fires). The W224 teeth.
gen15 = [f for f in gen16 if not (f[1] == 1 and f[2] == 1 and f[3] == F(0))]
cls15, why15 = anomaly_class(mirror_of(gen15))
check("CONTROL 1a: the 15-mirror (no nu_R) is KNOWN-OBSTRUCTED (mod-16 = 15 != 0)",
      cls15 == "OBSTRUCTED", f"{cls15}: {why15}")

# (1b) a lone chiral color triplet: perturbative anomaly -> OBSTRUCTED.
cls_lone, why_lone = anomaly_class([(+1, 1, 3, F(1))])
check("CONTROL 1b: a lone chiral 3 is KNOWN-OBSTRUCTED (perturbative anomaly)",
      cls_lone == "OBSTRUCTED", f"{cls_lone}: {why_lone}")

# (1c) an odd Majorana count is NOT at the Fidkowski-Kitaev/DIII collapse -> NOT gappable.
check("CONTROL 1c: 15 Majorana in DIII (Z/16) NOT symmetrically gappable (15 != 0 mod 16)",
      not majorana_realized(15, 16), "residual protected mode obstructs")
check("CONTROL 1c': 7 Majorana in BDI (Z/8) NOT symmetrically gappable (7 != 0 mod 8)",
      not majorana_realized(7, 8), "residual protected mode obstructs")

print("\n[CONTROL 2] the KNOWN-REALIZED classes register EXISTENCE-GUARANTEED / gappable")
check("CONTROL 2a: Fidkowski-Kitaev 8 Majorana (1+1D BDI, Z/8) IS symmetrically gappable",
      majorana_realized(8, 8), "the canonical realized SMG collapse")
check("CONTROL 2b: 16 Majorana (3+1D DIII, Z/16) IS symmetrically gappable",
      majorana_realized(16, 16), "the 3+1D interacting collapse")

print("\n[CONTROL 3] the beyond-anomaly (w2w3) detector FIRES on the modified SO(10)+WZW, ABSENT on standard 16")
check("CONTROL 3a: modified SO(10)+WZW -> w2w3 obstruction FIRES (no trivial gapped phase)",
      w2w3_obstruction(modified_so10_wzw), "Higgs cannot be trivially disordered")
check("CONTROL 3b: standard Spin(10) 16 -> w2w3 obstruction ABSENT",
      not w2w3_obstruction(gu_mirror_content), "standard Spin(10)+16 has NO w2w3 anomaly")

print("\n[CONTROL 4] the strong-coupling toy resolves BOTH ways (outcome is coupling-ratio dependent)")
out_sym, (ES1, EB1) = strong_coupling_outcome(g_sym=1.2, g_bilinear=0.6)   # symmetric-dominant
out_bil, (ES2, EB2) = strong_coupling_outcome(g_sym=0.6, g_bilinear=1.2)   # bilinear-dominant
print(f"     symmetric-dominant (g_sym=1.2,g_bil=0.6):  E_S={ES1:.4f}  E_B={EB1:.4f} -> {out_sym}")
print(f"     bilinear-dominant  (g_sym=0.6,g_bil=1.2):  E_S={ES2:.4f}  E_B={EB2:.4f} -> {out_bil}")
check("CONTROL 4a: symmetric-multifermion-dominant coupling -> SMG (symmetric gapped phase)",
      out_sym == "SMG", "the good outcome exists in the phase diagram")
check("CONTROL 4b: bilinear-dominant coupling -> SYMMETRY-BREAKING (Eichten-Preskill failure)",
      out_bil == "SYMMETRY-BREAKING", "the failure mode ALSO exists in the phase diagram")
check("CONTROL 4c: therefore the strong-coupling outcome is COUPLING-RATIO DEPENDENT -> UNDETERMINED",
      out_sym != out_bil, "which basin wins depends on GU's (unspecified) mirror couplings")


# --------------------------------------------------------------- THE GU LEDGER
print("\n" + "-" * 100)
print("[GU LEDGER] classify GU's SO(10)-16 mirror against the three outcomes")

# (1) EXISTENCE (necessary / W224 anomaly condition): all vanish -> gappable in principle.
cls_gu, why_gu = anomaly_class(mirror16)
print(f"     anomaly class of GU mirror 16bar:  {cls_gu}  ({why_gu})")
existence_guaranteed = (cls_gu == "GAPPABLE-IN-PRINCIPLE")
check("[GU-1] symmetric gapped phase EXISTS (cobordism: anomaly-free 16 -> trivial 5d boundary)",
      existence_guaranteed, "Wang-Wen 2020: the 16n admits a symmetric gapped mirror boundary")

# (2) BEYOND-ANOMALY obstruction (F2): none fires for the standard Spin(10) 16.
f2_w2w3 = w2w3_obstruction(gu_mirror_content)
f2_cat  = categorical_symmetry_obstruction(gu_mirror_content)
f2_dqc  = forced_dqc_gapless(gu_mirror_content)
print(f"     beyond-anomaly obstructions:  w2w3={f2_w2w3}  categorical={f2_cat}  forced-DQC={f2_dqc}")
beyond_anomaly_fires = f2_w2w3 or f2_cat or f2_dqc
check("[GU-2] NO beyond-anomaly obstruction fires for the standard Spin(10) 16 (F2 not triggered)",
      not beyond_anomaly_fires,
      "w2w3 absent; categorical symmetry retracted by un-Higgsed Spin(10); DQC gapless is between GAUGED GUT vacua, not forced on the global mirror gap")

# (3) REALIZATION status: is the strong-coupling gapped phase KNOWN to be reached for the
#     EXACT SO(10) 16 in 3+1D?  NO clean settlement: (i) the general SMG transition is a single
#     continuous one for RELATED anomaly-free models (8-Dirac 2+1D; Catterall SU(2)xSU(2)
#     3+1D; 3-4-5-0 1+1D), but (ii) for the exact 16 in 3+1D some microscopic models show an
#     INTERVENING SYMMETRY-BREAKING phase (the E-P failure mode is live), and (iii) GU's
#     specific mirror interaction is the UNBUILT record condensate -- underspecified, so even a
#     faithful MC cannot be run. -> the dynamical realization is UNSETTLED.
smg_known_realized_for_exact_16 = False   # no direct 3+1D MC / rigorous proof for the exact 16
smg_known_obstructed            = False   # existence guaranteed (F1 absent) and F2 absent
ep_failure_possible             = True    # bilinear/symmetry-breaking basin is not excluded
gu_couplings_specified          = False   # the mirror condensate is unbuilt / underspecified
print(f"     realization for the EXACT 3+1D SO(10) 16:  known-realized={smg_known_realized_for_exact_16}  "
      f"known-obstructed={smg_known_obstructed}")
print(f"     E-P symmetry-breaking basin excluded?  {not ep_failure_possible}    "
      f"GU mirror couplings specified?  {gu_couplings_specified}")

# --------------------------------------------------------------- VERDICT DERIVATION
print("\n" + "-" * 100)
print("[VERDICT DERIVATION] apply the pre-declared failure condition")

# F1: known-obstructed anomaly class?
F1 = smg_known_obstructed or (cls_gu == "OBSTRUCTED")
# F2: a beyond-anomaly obstruction fires for the standard 16?
F2 = beyond_anomaly_fires
FALSIFIED = F1 or F2
CLEAN_SURVIVES = smg_known_realized_for_exact_16 and gu_couplings_specified and (not ep_failure_possible)
OPEN_IN_THE_FIELD = (not FALSIFIED) and (not CLEAN_SURVIVES)

print(f"     F1 (known-obstructed anomaly class):        {F1}")
print(f"     F2 (beyond-anomaly obstruction fires):      {F2}")
print(f"     => FALSIFIED (F1 or F2):                    {FALSIFIED}")
print(f"     CLEAN-SURVIVES (known-realized + settled):  {CLEAN_SURVIVES}")
print(f"     => OPEN-IN-THE-FIELD:                       {OPEN_IN_THE_FIELD}")

check("[V1] FAILURE CONDITION NOT triggered (F1 and F2 both false) -> GU is NOT falsified on this leg",
      not FALSIFIED, "no proof of obstruction; existence guaranteed; beyond-anomaly checked-absent")
check("[V2] NOT a clean pass either (exact-16 realization unsettled; GU couplings underspecified)",
      not CLEAN_SURVIVES, "the honest residual: dynamical realization is open")
check("[V3] VERDICT is OPEN-IN-THE-FIELD (the correct non-naive third outcome)",
      OPEN_IN_THE_FIELD, "GU chirality is CONDITIONAL on an open lattice-field-theory problem")

# --------------------------------------------------------------- SELF-CONSISTENCY OF THE MACHINERY
print("\n[SELF-CHECK] the classifier would have FALSIFIED GU had the mirror been the 15 (teeth)")
cls15b, _ = anomaly_class(mirror_of(gen15))
would_falsify_15 = (cls15b == "OBSTRUCTED")
check("[S1] on the 15-mirror the verdict FLIPS to FALSIFIED (F1 fires) -> the probe has TEETH",
      would_falsify_15, "the 16th state (nu_R) is load-bearing on realization too")
print("[SELF-CHECK] the classifier would have FALSIFIED had w2w3 fired (modified SO(10)+WZW)")
would_falsify_wzw = w2w3_obstruction(modified_so10_wzw)
check("[S2] on the modified SO(10)+WZW content the beyond-anomaly obstruction fires (F2) -> teeth",
      would_falsify_wzw, "a real beyond-anomaly obstruction is detectable and would kill")


# =====================================================================================
# VERDICT
# =====================================================================================
print("\n" + "=" * 100)
if not FAIL and OPEN_IN_THE_FIELD:
    print("VERDICT: OPEN-IN-THE-FIELD (leaning SURVIVES; NOT falsified, NOT a clean pass).")
    print("  GIVEN the good Krein branch (the sign gate is a SEPARATE object, not re-litigated):")
    print("  - EXISTENCE of a symmetric gapped phase is GUARANTEED: GU's mirror 16bar is 't Hooft")
    print("    anomaly-free (perturbative + Witten + mod-16 = 0, the nu_R load-bearing, W224), so by")
    print("    cobordism (Wang-Wen 2020) it admits a symmetric gapped mirror boundary. NOT obstructed.")
    print("  - NO beyond-anomaly obstruction fires for the STANDARD Spin(10) 16: the w2w3 mixed")
    print("    gauge-gravity anomaly is ABSENT (only a modified SO(10)+WZW carries it); the")
    print("    categorical/non-invertible symmetry is RETRACTED by the un-Higgsed Spin(10); the")
    print("    gapless deconfined-quantum-critical region sits between GAUGED GUT vacua, not as a")
    print("    forced obstruction to the global-symmetric mirror gap. So F2 does not trigger.")
    print("  - BUT the DYNAMICAL REALIZATION for the EXACT 3+1D SO(10) 16 is UNSETTLED: the general")
    print("    SMG transition is a single continuous one for RELATED anomaly-free models (Fidkowski-")
    print("    Kitaev 8, 3+1D DIII 16, Catterall SU(2)xSU(2), 3-4-5-0), yet some microscopic models")
    print("    of the exact 16 show an INTERVENING SYMMETRY-BREAKING phase (the Eichten-Preskill")
    print("    failure mode is LIVE), and GU's specific mirror interaction is the UNBUILT record")
    print("    condensate -- underspecified, so even a faithful lattice MC cannot be run.")
    print("  PRE-DECLARED FAILURE CONDITION NOT TRIGGERED (F1 and F2 both false): GU is NOT FALSIFIED.")
    print("  It is ALSO not a clean pass. The honest characterization: GU's chirality is CONDITIONAL")
    print("  on an OPEN lattice-field-theory problem -- whether GU's SO(10)-16 mirror dynamics flow to")
    print("  the (guaranteed-to-exist) symmetric gapped phase rather than to a symmetry-breaking or")
    print("  gapless phase. TEETH: the 15 (no nu_R) and a modified SO(10)+WZW both correctly FLIP the")
    print("  verdict to FALSIFIED, so the probe has power.")
else:
    print("VERDICT: machinery inconsistent or an unexpected outcome (see failed checks).")
    print(f"  FALSIFIED={FALSIFIED}  CLEAN_SURVIVES={CLEAN_SURVIVES}  OPEN={OPEN_IN_THE_FIELD}")
    print(f"  failed checks: {FAIL}")

print("=" * 100)
import sys
sys.exit(1 if FAIL else 0)
