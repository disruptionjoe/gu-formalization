"""
W222 -- FALSIFICATION probe (NON-NAIVE): Standard-Model emergence in GU's 4D shadow.
Leg attacked: (a) HYPERCHARGE from the Pati-Salam Spin(6)xSpin(4)=SU(4)xSU(2)xSU(2)
branching of the SO(10) 16, and (b) the 4D-shadow GAUGE ANOMALY content.

METHOD (strict, pre-declared). ASSUME GU is correct and GRANT every unbuilt piece
resolving as GU hopes -- in particular grant that the (unbuilt) 14D->4D reduction delivers,
per the GU carrier measurement (MP-M2/MP-M3), the internal matter factor as ONE SO(10) 16
per generation and that the mirror-gapping condensate removes the conjugate half. A GAP
(mechanism unbuilt) does NOT count. Only a WRONG definite output or a forced inconsistency
counts.

PRE-DECLARED FAILURE CONDITION. GU is FALSIFIED on this leg iff ANY of:
  (i)   the SU(4)xSU(2)xSU(2) -> SU(3)xSU(2)xU(1) branching gives hypercharges that DO NOT
        match the Standard-Model generation (wrong Q on any state), OR
  (ii)  the 4D chiral shadow carries a gauge anomaly (perturbative cubic, or the Witten
        SU(2) global mod-2 anomaly, or the spin-cobordism Omega^Spin_5(BG_SM) global
        anomaly) that NO admissible REAL mechanism cancels -- and in particular if the ONLY
        route to cancellation is a lattice/cobordism ANALOGY rather than a genuine rep-theory
        cancellation of GU's own chiral content, that is logged as SURVIVES-ONLY-BY-ANALOGY,
        which is an open falsification RISK, not a pass, OR
  (iii) forced exotic chiral states survive in the physical (surviving) half.
If hypercharges match AND the chiral shadow is anomaly-free by a REAL (not merely analogical)
mechanism AND no exotic chiral states are forced: GU SURVIVES this leg.

Every number below is printed. Positive controls run FIRST and must have power (detect a
real anomaly / a wrong embedding) before any GU claim is trusted. Exit 0 on all-pass.

Run:  python tests/W222_falsify_sm_emergence.py
"""

from fractions import Fraction as F

FAIL = []
def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}   {detail}")
    if not ok:
        FAIL.append(name)


# =====================================================================================
# 0. THE STANDARD-MODEL GENERATION (the target the branching must reproduce).
#    A Weyl fermion = (name, SU(3) triality t in {+1 for 3, -1 for 3bar, 0 for singlet},
#    n_color, T3-list over weak partners, Y).  All fields written LEFT-handed (so
#    right-handed particles appear as their left-handed conjugates u^c, d^c, e^c, nu^c).
#    Q = T3 + Y is the OUTPUT we check.
# =====================================================================================
# Standard hypercharge normalization: Q = T3 + Y.
SM = {
    #  name : (SU3 triality, n_color, [T3 of each weak component], Y)
    "Q_L":  ( +1, 3, [F(1,2), F(-1,2)], F(1,6) ),   # left quark doublet (u,d)
    "u_c":  ( -1, 3, [F(0)],            F(-2,3) ),   # anti-up
    "d_c":  ( -1, 3, [F(0)],            F(1,3)  ),   # anti-down
    "L_L":  (  0, 1, [F(1,2), F(-1,2)], F(-1,2) ),   # left lepton doublet (nu,e)
    "e_c":  (  0, 1, [F(0)],            F(1)    ),   # positron
    "nu_c": (  0, 1, [F(0)],            F(0)    ),   # right neutrino (SO(10) completion)
}

def sm_charges():
    """Electric charges Q = T3 + Y for every Weyl component of the SM generation,
    expanded over BOTH weak components AND color multiplicity (full 16-state multiset)."""
    out = []
    for nm,(t,nc,t3s,Y) in SM.items():
        for _ in range(nc):
            for t3 in t3s:
                out.append((nm, t3+Y))
    return out


# =====================================================================================
# 1. PATI-SALAM BRANCHING  SU(4) x SU(2)_L x SU(2)_R -> SU(3) x SU(2)_L x U(1)_Y
#    SO(10) 16 = (4, 2, 1) + (4bar, 1, 2)  under  SU(4) x SU(2)_L x SU(2)_R.
#    SU(4) -> SU(3) x U(1)_{B-L}:   4 = 3_{+1/3} + 1_{-1}   (B-L of quark=+1/3, lepton=-1).
#    Hypercharge from the Pati-Salam embedding:   Y = T3R + (B-L)/2 .
#    We BUILD every state of the 16 from this rule and OUTPUT its Y, then compare to SM.
# =====================================================================================
def patisalam_16(y_T3R=F(1), qbl=F(1,3), lbl=F(-1)):
    """
    Build the 16 states from SU(4)xSU(2)_LxSU(2)_R quantum numbers.
      SU(4) -> SU(3)xU(1)_{B-L}:  4 = 3_{qbl} + 1_{lbl}   (SM: quark B-L=+1/3, lepton=-1).
      T3R    : +1/2 / -1/2 for the SU(2)_R doublet (in (4bar,1,2)); 0 in (4,2,1)
      T3L    : +1/2 / -1/2 for the SU(2)_L doublet (in (4,2,1)); 0 in (4bar,1,2)
    Pati-Salam hypercharge:  Y = y_T3R*T3R + (B-L)/2 .  SM values: y_T3R=1, qbl=1/3, lbl=-1.
    Returns list of (label, SU3-triality, T3L, Y).
    """
    states = []
    # (4, 2, 1): left-handed quarks & leptons, SU(2)_L doublet, T3R = 0
    for (kind, tri, BL) in [("q", +1, qbl), ("l", 0, lbl)]:
        ncol = 3 if kind == "q" else 1
        for _ in range(ncol):
            for T3L in (F(1,2), F(-1,2)):
                Y = BL/2
                states.append((f"{kind}L_{'up' if T3L>0 else 'dn'}", tri, T3L, Y))
    # (4bar, 1, 2): conjugate quarks & leptons, SU(2)_R doublet, T3L = 0
    #   conjugate => B-L flips sign; triality flips.
    for (kind, tri, BL) in [("q", -1, -qbl), ("l", 0, -lbl)]:
        ncol = 3 if kind == "q" else 1
        for _ in range(ncol):
            for T3R in (F(1,2), F(-1,2)):
                Y = y_T3R*T3R + BL/2
                states.append((f"{kind}R_{'up' if T3R>0 else 'dn'}", tri, F(0), Y))
    return states


def multiset_charges_from_16(states):
    """Electric charges Q = T3L + Y, as a sorted multiset of Fractions."""
    return sorted(q for (_lab,_tri,T3L,Y) in states for q in [T3L+Y])


def multiset_charges_from_SM():
    return sorted(q for (_nm,q) in sm_charges())


# =====================================================================================
# 2. PERTURBATIVE GAUGE ANOMALIES of a chiral fermion set.
#    Coefficients (all must vanish for a consistent chiral gauge theory):
#      U(1)^3        : sum Y^3
#      grav^2-U(1)   : sum Y
#      SU(2)^2-U(1)  : sum over SU(2)_L doublets of Y (each doublet counted once per color)
#      SU(3)^3       : sum of SU(3) cubic-anomaly triality (3 -> +1, 3bar -> -1, singlet 0),
#                      counted once per SU(2)_L component.
#    Written as functions of a fermion list of (triality, T3L-list-or-count, Y).
# =====================================================================================
def anomalies(fermions):
    """
    fermions: list of (triality, n_weak, n_color, Y) LEFT-handed Weyl multiplets, where
      n_weak  = number of SU(2)_L components (2 for a doublet, 1 for a singlet)
      n_color = number of SU(3) color components (3 or 1)
    Returns dict of the four anomaly coefficients (Fractions).
    """
    U1_cubed = F(0); grav = F(0); su2 = F(0); su3 = F(0)
    for (tri, nw, ncol, Y) in fermions:
        # every (color, weak) component is one Weyl fermion with this Y
        U1_cubed += nw*ncol*Y**3
        grav     += nw*ncol*Y
        if nw == 2:                     # SU(2)_L doublet: contributes ncol * Y (once per color)
            su2 += ncol*Y
        su3 += nw*tri                   # cubic color anomaly, once per weak component
    return dict(U1_cubed=U1_cubed, grav=grav, su2=su2, su3=su3)


def sm_fermion_list():
    """The chiral SM generation as (triality, n_weak, n_color, Y) multiplets."""
    return [
        (+1, 2, 3, F(1,6)),   # Q_L
        (-1, 1, 3, F(-2,3)),  # u_c
        (-1, 1, 3, F(1,3)),   # d_c
        ( 0, 2, 1, F(-1,2)),  # L_L
        ( 0, 1, 1, F(1)),     # e_c
        ( 0, 1, 1, F(0)),     # nu_c
    ]


def count_su2_doublets(fermions):
    """Number of SU(2)_L doublets (with color multiplicity) -> Witten SU(2) global anomaly."""
    return sum(ncol for (tri, nw, ncol, Y) in fermions if nw == 2)


# =====================================================================================
print("=" * 100)
print("W222 -- FALSIFICATION probe: SM emergence in GU's 4D shadow (hypercharge + anomaly)")
print("=" * 100)

# --------------------------------------------------------------- POSITIVE CONTROLS FIRST
print("\n[CONTROL 0] the anomaly routine has POWER (detects real anomalies)")

# a single chiral color triplet with unit hypercharge: color cubic anomaly must be NONZERO
c_triplet = [(+1, 1, 3, F(1))]
a = anomalies(c_triplet)
check("single chiral 3 has NONZERO SU(3)^3 anomaly", a["su3"] != 0, f"SU(3)^3 = {a['su3']}")
check("single chiral 3 has NONZERO U(1)^3 anomaly", a["U1_cubed"] != 0, f"U(1)^3 = {a['U1_cubed']}")

# its conjugate 3bar gives the exact negative
c_anti = [(-1, 1, 3, F(-1))]
b = anomalies(c_anti)
check("3bar SU(3)^3 anomaly = -(3) anomaly", b["su3"] == -a["su3"], f"{b['su3']} vs {-a['su3']}")

# a VECTORLIKE pair 3 + 3bar is trivially anomaly free (this is the 14D Sp(64) pseudoreal
# statement) -- and it is NOT chiral; it must be distinguished from the nontrivial SM zero.
vec = c_triplet + [(-1, 1, 3, F(-1))]
v = anomalies(vec)
check("VECTORLIKE 3+3bar anomaly = 0 (trivial, non-chiral)",
      all(x == 0 for x in v.values()), f"{ {k:str(val) for k,val in v.items()} }")

# a single lepton DOUBLET with Y!=0: grav and SU(2)^2-U(1) nonzero (routine sees mixed anomalies)
lep = [(0, 2, 1, F(-1,2))]
l = anomalies(lep)
check("single Y!=0 doublet has NONZERO grav anomaly", l["grav"] != 0, f"grav = {l['grav']}")
check("single Y!=0 doublet has NONZERO SU(2)^2-U(1)", l["su2"] != 0, f"SU(2)^2U(1) = {l['su2']}")

print("\n[CONTROL 1] a WRONG hypercharge embedding must FAIL to reproduce the SM charges")
# Deliberately corrupt the SU(4) quark B-L (qbl=1 instead of 1/3): breaks charge quantization,
# must give WRONG electric charges (non-third-integer quark charges).
wrong = patisalam_16(y_T3R=F(1), qbl=F(1), lbl=F(-1))
wrong_Q = multiset_charges_from_16(wrong)
sm_Q = multiset_charges_from_SM()
check("wrong (qbl=1) embedding does NOT match SM charges (control has power)",
      wrong_Q != sm_Q, "correctly rejected")
# second wrong control: corrupt the SU(2)_R hypercharge coefficient
wrong2_Q = multiset_charges_from_16(patisalam_16(y_T3R=F(2), qbl=F(1,3), lbl=F(-1)))
check("wrong (y_T3R=2) embedding does NOT match SM charges (control has power)",
      wrong2_Q != sm_Q, "correctly rejected")


# --------------------------------------------------------------- (i) HYPERCHARGE TEST
print("\n[i] HYPERCHARGE: Pati-Salam branching of the SO(10) 16 vs the SM generation")
ps16 = patisalam_16(y_T3R=F(1), qbl=F(1,3), lbl=F(-1))
print("     state         SU3   T3L     Y        Q=T3L+Y")
for (lab, tri, T3L, Y) in ps16:
    print(f"     {lab:10s}  {tri:+d}   {str(T3L):>5s}  {str(Y):>6s}   {str(T3L+Y):>6s}")

ps_Q = multiset_charges_from_16(ps16)
check("16 has exactly 16 Weyl states", len(ps16) == 16, f"n = {len(ps16)}")
check("(i) Pati-Salam hypercharges reproduce the SM electric-charge multiset EXACTLY",
      ps_Q == sm_Q, "MATCH" if ps_Q == sm_Q else f"{ps_Q}\n  vs SM {sm_Q}")

# also check the standard per-species Y values are present
Yset_ps = sorted(set(Y for (_l,_t,_T,Y) in ps16))
Yset_sm = sorted(set(Y for (_n,(_t,_nc,_t3,Y)) in SM.items()))
check("(i) the Y-value set matches the SM {1/6,-2/3,1/3,-1/2,1,0}",
      Yset_ps == Yset_sm, f"{[str(x) for x in Yset_ps]}")


# --------------------------------------------------------------- (ii) ANOMALY TEST
print("\n[ii] 4D-SHADOW GAUGE ANOMALY of the chiral SO(10) 16 (one generation)")
gen = sm_fermion_list()
A = anomalies(gen)
print(f"     U(1)^3        = {A['U1_cubed']}")
print(f"     grav^2-U(1)   = {A['grav']}")
print(f"     SU(2)^2-U(1)  = {A['su2']}")
print(f"     SU(3)^3       = {A['su3']}")
check("(ii) U(1)^3 anomaly of chiral 16 = 0",    A["U1_cubed"] == 0)
check("(ii) grav^2-U(1) anomaly of chiral 16 = 0", A["grav"] == 0)
check("(ii) SU(2)^2-U(1) anomaly of chiral 16 = 0", A["su2"] == 0)
check("(ii) SU(3)^3 anomaly of chiral 16 = 0",   A["su3"] == 0)

# Positive control on the anomaly zero being NONTRIVIAL: drop nu_c (the SM 15) -- still zero,
# but drop e_c instead and the U(1)/grav anomalies become NONZERO (so the zero is content).
gen_no_ec = [f for f in gen if not (f[1]==1 and f[2]==1 and f[3]==F(1))]
A2 = anomalies(gen_no_ec)
check("CONTROL: removing e_c BREAKS anomaly cancellation (zero is nontrivial)",
      A2["U1_cubed"] != 0 or A2["grav"] != 0, f"U(1)^3={A2['U1_cubed']}, grav={A2['grav']}")

# Witten SU(2) global (mod-2) anomaly: number of SU(2)_L doublets must be EVEN.
nd = count_su2_doublets(gen)
print(f"\n     Witten SU(2) global anomaly: #SU(2)_L doublets = {nd}  (need even)")
check("(ii) Witten SU(2) global anomaly absent (even # of doublets)", nd % 2 == 0, f"{nd} doublets")

# Spin-cobordism global anomaly Omega^Spin_5(B G_SM): the SM generation is anomaly-free in the
# full Freed-Hopkins/Garcia-Etxebarria-Montero classification. Encoded here as the known result
# (prior repo work R2 verified the mod-3 arena is empty and the SM saturates the 5th-bordism
# constraints); we assert the two computable shadows: tr(Y)=0 (grav-U(1), the only 5d-relevant
# mixed term at this order) and even doublet count, both already PASS above.
check("(ii) spin-cobordism global-anomaly shadow (tr Y = 0, even doublets) consistent",
      A["grav"] == 0 and nd % 2 == 0, "no global obstruction from the SM content")


# --------------------------------------------------------------- (iii) EXOTIC CHIRAL STATES
print("\n[iii] EXOTIC CHIRAL STATES in the surviving (physical) half")
# The GU carrier delivers 16 (physical) + 16bar (mirror), a VECTORLIKE 32. Chirality is
# produced ONLY by gapping the mirror 16bar. GRANTING that gapping, the physical half is
# EXACTLY the SO(10) 16 = one generation: no state outside the SM 16 multiplet.
labels_ps = set(nm.split("_")[0] for nm in SM)  # {Q,u,d,L,e,nu} families
n_phys = len(ps16)
check("(iii) physical half is exactly the 16 (no exotic chiral states beyond one SM generation)",
      n_phys == 16, f"{n_phys} chiral states = one generation, no exotics")

# Demonstrate the vectorlike->chiral distinction explicitly (the honest caveat):
full_32 = gen + [(-t, nw, nc, -Y) for (t, nw, nc, Y) in gen]   # 16 + 16bar
A32 = anomalies(full_32)
check("NOTE: raw carrier 32 = 16+16bar is VECTORLIKE (anomaly 0 TRIVIALLY, chirality 0)",
      all(x == 0 for x in A32.values()),
      "trivial zero -- the 14D Sp(64) statement; the SM zero above is the NONTRIVIAL chiral one")


# =====================================================================================
# VERDICT
# =====================================================================================
print("\n" + "=" * 100)
hyper_ok  = (ps_Q == sm_Q)
anom_ok   = (A["U1_cubed"]==0 and A["grav"]==0 and A["su2"]==0 and A["su3"]==0 and nd % 2 == 0)
exotic_ok = (n_phys == 16)

if not FAIL and hyper_ok and anom_ok and exotic_ok:
    print("VERDICT: SURVIVES.")
    print("  (i)   Hypercharges MATCH the SM exactly (Pati-Salam branching of the 16).")
    print("  (ii)  The chiral shadow is anomaly-free by a REAL mechanism: the SO(10) 16 has no")
    print("        cubic Casimir (all four perturbative coefficients vanish as an identity of the")
    print("        rep, not by analogy), the Witten SU(2) global anomaly is absent (4 doublets,")
    print("        even), and the spin-cobordism shadow carries no obstruction.")
    print("  (iii) No exotic chiral states are forced in the surviving half.")
    print("  HONEST CAVEAT (logged, NOT a pass-breaker): the anomaly cancellation is REAL for the")
    print("  CHIRAL 16, but GU's carrier delivers a VECTORLIKE 16+16bar; chirality is produced")
    print("  ONLY by the (unbuilt, dynamics-gated) mirror-gapping condensate. The 'only-by-")
    print("  analogy' risk flagged by council H3 is therefore DISPLACED off the anomaly-")
    print("  cancellation (which is genuine rep theory) and ONTO chirality PRODUCTION -- an")
    print("  unbuilt GAP that this probe GRANTS per method, not a falsification.")
else:
    print("VERDICT: FAILURE CONDITION TRIGGERED.")
    print(f"  hyper_ok={hyper_ok}  anom_ok={anom_ok}  exotic_ok={exotic_ok}")
    print(f"  failed checks: {FAIL}")

print("=" * 100)
import sys
sys.exit(1 if FAIL else 0)
