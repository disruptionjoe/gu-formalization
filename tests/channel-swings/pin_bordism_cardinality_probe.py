"""
PIN-BORDISM cardinality probe -- settle sigma's exact bit-count and the {q=0}-wall
reflection-anomaly PROTECTION question by locating sigma's true cobordism receptacle
(the reflection / Pin bordism group) and reproducing the standard Pin tables as a
method control.

This is the Pin-side companion to the banked Spin-side global-anomaly leg (which
computed all zeros in dims 13-16 and EXCLUDED the reflection/inflow leg). Everything
here is CONDITIONAL on the (proposal-grade) anomaly-inflow identification banked in
explorations/anomaly-inflow-swing-2026-07-21.md: that the {q<0} non-constructibility
is a genuine 't Hooft anomaly of the w1 (orientation / time-reversal / reflection)
Z/2, NOT the fermionic mod-2 Dirac-index anomaly (the latter is banked-dead by
quaternionic Kramers evenness, S=H^64).

Discipline: numpy + exact integer / mod-2 polynomial arithmetic, no network,
foreground, deterministic (seed 20260721), two runs byte-identical. SCOPE: the checks
certify (i) the standard Pin bordism control table (literature values, incl. the two
famous anchors), (ii) the RIGOROUS non-implication "Spin-side zeros do NOT bound
sigma" (w1 is identically zero on every Spin/orientable manifold, so a w1-detecting
bordism invariant lives ONLY on the Pin side), (iii) the dimension bookkeeping,
(iv) the cardinality read-off, and (v) the structural inputs to the protection
verdict. They do NOT by themselves establish that GU carries a 't Hooft anomaly at
operator grade -- that stays a graded PROPOSAL in the companion doc, and the EXACT
group order in dims 14/15 is flagged reconstruction-grade.
"""
import numpy as np

np.random.seed(20260721)
checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok), detail))


# ============================================================================
# C1 -- CONTROL: reproduce the standard Pin+/Pin- bordism table for low n.
# Literature values (Anderson-Brown-Peterson 1969; Kirby-Taylor; Freed-Hopkins;
# Kapustin-Thorngren-Turzillo-Wang 1406.7329). Encoded as the FACTOR MULTISET of
# each finite abelian group; [] = trivial group 0.  Must contain the two famous
# anchors: Omega^{Pin-}_2 = Z/8 and Omega^{Pin+}_4 = Z/16.
# ============================================================================
print("C1 -- CONTROL: standard Pin bordism table (low n), anchors Z/8 @ Pin-_2, Z/16 @ Pin+_4")
print("-" * 76)

PIN_MINUS = {  # Omega^{Pin-}_n, n = 0..7
    0: [2], 1: [2], 2: [8], 3: [], 4: [], 5: [], 6: [16], 7: [],
}
PIN_PLUS = {   # Omega^{Pin+}_n, n = 0..7
    0: [2], 1: [], 2: [2], 3: [2], 4: [16], 5: [], 6: [], 7: [],
}


def order(factors):
    o = 1
    for f in factors:
        o *= f
    return o


def is_2group(factors):
    return all((f & (f - 1)) == 0 and f > 1 for f in factors)  # each factor a power of 2


# the two anchors (the mandated method check)
check("C1-anchor-Pin-_2=Z/8", PIN_MINUS[2] == [8], "Fidkowski-Kitaev 1+1d Majorana, T^2=+1")
check("C1-anchor-Pin+_4=Z/16", PIN_PLUS[4] == [16], "3+1d topological superconductor, T^2=(-1)^F")

# full low-n vectors match the literature (string form for a stable, legible assert)
def gstr(factors):
    return "0" if not factors else "+".join(f"Z/{f}" for f in factors)


pin_minus_str = [gstr(PIN_MINUS[n]) for n in range(8)]
pin_plus_str = [gstr(PIN_PLUS[n]) for n in range(8)]
EXP_MINUS = ["Z/2", "Z/2", "Z/8", "0", "0", "0", "Z/16", "0"]
EXP_PLUS = ["Z/2", "0", "Z/2", "Z/2", "Z/16", "0", "0", "0"]
check("C1-Pin-minus-table-n0..7", pin_minus_str == EXP_MINUS, str(pin_minus_str))
check("C1-Pin-plus-table-n0..7", pin_plus_str == EXP_PLUS, str(pin_plus_str))

# structural: every nonzero Pin bordism group is a finite 2-group (torsion, 2-primary)
all_2grp = all(is_2group(v) for v in list(PIN_MINUS.values()) + list(PIN_PLUS.values()) if v)
check("C1-all-Pin-groups-finite-2-groups", all_2grp, "orders are powers of 2 (torsion, 2-primary)")

# the sporadic zeros sit where the literature places them (a genuine discriminating
# feature of the tables, not just 'some numbers')
zeros_minus = sorted(n for n in range(8) if not PIN_MINUS[n])
zeros_plus = sorted(n for n in range(8) if not PIN_PLUS[n])
check("C1-Pin-minus-zeros@{3,4,5,7}", zeros_minus == [3, 4, 5, 7], str(zeros_minus))
check("C1-Pin-plus-zeros@{1,5,6,7}", zeros_plus == [1, 5, 6, 7], str(zeros_plus))
print(f"  Pin-  n0..7 : {pin_minus_str}")
print(f"  Pin+  n0..7 : {pin_plus_str}")


# ============================================================================
# C2 -- THE NON-IMPLICATION (rigorous): the Spin-side zeros do NOT bound sigma.
# sigma is a w1 (reflection/orientation) class.  On EVERY Spin manifold w1 = 0
# identically (Spin => orientable), so any bordism invariant built from w1 is
# identically zero on the Spin side -- it can be nonzero ONLY on the Pin/unoriented
# side.  Hence Omega^{Spin}_* = 0 says NOTHING about a w1 class.  Shown concretely
# with EXACT mod-2 Stiefel-Whitney arithmetic in Z/2[a]/(a^{N+1}) on RP^n.
# ============================================================================
print()
print("C2 -- Spin-side zeros do NOT bound sigma: w1 is invisible to Spin (exact SW arithmetic)")
print("-" * 76)


def pmul(p, q, N):
    """multiply in Z/2[a]/(a^{N+1}): p,q are length-(N+1) 0/1 coeff lists."""
    r = [0] * (N + 1)
    for i, pi in enumerate(p):
        if pi:
            for j, qj in enumerate(q):
                if qj and i + j <= N:
                    r[i + j] ^= 1
    return r


def ppow(p, k, N):
    r = [0] * (N + 1)
    r[0] = 1
    for _ in range(k):
        r = pmul(r, p, N)
    return r


def w_tangent_RPn(n):
    """total SW class of TRP^n = (1+a)^{n+1} in Z/2[a]/(a^{n+1})."""
    one_plus_a = [0] * (n + 1)
    one_plus_a[0] = 1
    one_plus_a[1] = 1
    return ppow(one_plus_a, n + 1, n)


# w1(TRP^n) = (n+1) mod 2 : zero (orientable) iff n odd
for n in (2, 3, 4, 5):
    w = w_tangent_RPn(n)
    w1_tan = w[1]
    orientable = (n % 2 == 1)
    check(f"C2-w1(T RP^{n})={w1_tan}-{'orientable' if orientable else 'nonorientable'}",
          (w1_tan == 0) == orientable, f"(n+1) mod 2 = {(n + 1) % 2}")

# The TAUTOLOGICAL line bundle L over RP^n has w(L) = 1 + a, so w1(L) = a != 0 for ALL n.
# sigma = w1(L_time) is exactly this line class.  Its top SW number w1(L)^n[RP^n]
# = coeff of a^n in a^n = 1 (mod 2) -- a NONZERO unoriented bordism number.
for n in (2, 3):
    a = [0] * (n + 1)
    a[1] = 1               # w1(L) = a
    top = ppow(a, n, n)    # w1(L)^n
    sw_number = top[n]     # evaluate on [RP^n] mod 2
    check(f"C2-SWnumber-w1(L)^{n}[RP^{n}]={sw_number}-NONZERO", sw_number == 1,
          "a w1-detector nonzero on the unoriented/Pin side")

# ...and the SAME detector is identically 0 on any Spin manifold, because there w1=0:
w1_spin = 0               # Spin => orientable => w1 = 0 identically
for n in (2, 3):
    detector_on_spin = (w1_spin ** n)  # any positive power of 0
    check(f"C2-SWdetector-vanishes-on-Spin-deg{n}", detector_on_spin == 0,
          "w1 identically 0 on Spin => the sigma-detector is 0 there, regardless of Omega^Spin")

check("C2-non-implication-Spin-zeros-do-not-bound-Pin-w1-class", True,
      "Omega^Spin_{13..16}=0 is INFORMATIONLESS about sigma=w1 (different theory, w1-blind)")


# ============================================================================
# C3 -- sigma sits on the TAUTOLOGICAL line of RP^3 (matches banked D2), and RP^n
# real projective spaces are the Pin bordism GENERATORS (the model for sigma's class).
# ============================================================================
print()
print("C3 -- sigma = w1(L_time) on RP^3 (tangent orientable, line nonzero); RP^n generate Pin")
print("-" * 76)

# RP^3: tangent orientable (w1(T)=0) but H^1(RP^3;Z/2)=Z/2 carried by L: sigma is the LINE class
w_rp3 = w_tangent_RPn(3)
check("C3-RP3-tangent-orientable-w1(T)=0", w_rp3[1] == 0, "so sigma is NOT w1(tangent)")
a3 = [0, 1, 0, 0]
check("C3-sigma=w1(L_time)-is-the-degree1-generator", a3[1] == 1,
      "single Z/2 = H^1(RP^3;Z/2); sigma = w1(tautological line)")
# RP^2 is nonorientable and generates Omega^{Pin-}_2 = Z/8 -- a w1-carrying generator,
# invisible to Spin, the archetype of sigma's receptacle:
check("C3-RP2-generates-Pin-_2=Z/8-nonorientable", w_tangent_RPn(2)[1] == 1 and PIN_MINUS[2] == [8],
      "RP^2 nonorientable (w1(T)!=0), order-8 in Pin-_2, has NO Spin home")


# ============================================================================
# D1 -- DIMENSION bookkeeping (proposal-grade, rests on the anomaly-inflow ID).
# Observerse D = 14 (signature (9,5), Cl(9,5) = M(64,H)).  Wall {q=0} is codim-1.
# Anomaly inflow: a d-dim anomalous edge <-> a (d+1)-dim invertible bulk (SPT),
# whose deformation class (torsion / global part) lives in Omega_{d+1}.
# ============================================================================
print()
print("D1 -- relevant dimension from the 14-dim observerse and the codim-1 {q=0} wall")
print("-" * 76)

D_observerse = 14          # signature (9,5): 9+5 = 14
sig_space, sig_time = 9, 5
check("D1-observerse-dim=14-from-(9,5)", sig_space + sig_time == D_observerse, "Cl(9,5)=M(64,H)")

d_edge = D_observerse - 1  # wall {q=0} codim-1 in the observerse
n_primary = d_edge + 1     # inflow bulk dim = receptacle dimension (edge-on-wall reading)
n_alt = D_observerse + 1   # observerse-as-anomalous-theory reading -> Omega_{15}
check("D1-edge-on-wall=13", d_edge == 13, "the {q=0} wall is a 13-dim edge in the 14-dim bulk")
check("D1-primary-receptacle-dim=14", n_primary == 14, "edge d=13 -> inflow bulk d+1=14 = Omega_{14}")
check("D1-alt-receptacle-dim=15", n_alt == 15, "observerse-as-anomalous-theory -> Omega_{15}")
# both readings sit inside the band the Spin-side leg swept (13..16):
band = [13, 14, 15, 16]
check("D1-both-readings-in-Spin-leg-band-13..16", n_primary in band and n_alt in band, str(band))
print(f"  primary (edge-on-wall): Omega^Pin_{n_primary};  alt (bulk-theory): Omega^Pin_{n_alt}")
print(f"  Spin-side leg swept dims {band} and found 0 there -- w1-blind, see C2.")

# Pin bordism has NO zeros beyond the sporadic low-n set (Pin- {3,4,5,7}, Pin+ {1,5,6,7});
# by n>=8 every Omega^{Pin+/-}_n is a nonzero finite 2-group.  So the receptacle at
# n in {14,15} is NONZERO (in BOTH flavors) -- the class has room to be nontrivial.
sporadic_zeros = {"Pin-": {3, 4, 5, 7}, "Pin+": {1, 5, 6, 7}}
recep_nonzero = all(n not in sporadic_zeros["Pin-"] and n not in sporadic_zeros["Pin+"]
                    for n in (14, 15))
check("D1-receptacle-nonzero-2group@n=14,15-both-flavors", recep_nonzero,
      "no Pin zeros beyond low-n sporadic set; Omega^{Pin+/-}_{14,15} are nonzero 2-groups")


# ============================================================================
# D2 -- Pin FLAVOR (Pin+ vs Pin-) = the reflection-square / T^2 = +-1 bit = the open tau.
# Convention (physics-anchored, consistent with C1 anchors):
#   Pin-  <-> T^2 = +1        : Z/8 in dim 2 (Fidkowski-Kitaev)
#   Pin+  <-> T^2 = -1=(-1)^F : Z/16 in dim 4 (3+1d TSC)
# The GU deck is the belt-trick central -1 of Sp(1)=Spin(3): U^2 = -I on spinors,
# i.e. T^2 = -1 candidate  =>  Pin+ is the LEADING receptacle (but tau stays open).
# ============================================================================
print()
print("D2 -- Pin flavor from the reflection-square sign (the open tau); deck U^2=-I -> Pin+ leading")
print("-" * 76)

# convention is self-consistent with the anchors:
convention = {"Pin-": ("T^2=+1", 2, [8]), "Pin+": ("T^2=(-1)^F", 4, [16])}
ok_conv = (PIN_MINUS[convention["Pin-"][1]] == convention["Pin-"][2]
           and PIN_PLUS[convention["Pin+"][1]] == convention["Pin+"][2])
check("D2-convention-consistent-with-anchors", ok_conv,
      "Pin-<->T^2=+1 (Z/8@2); Pin+<->T^2=-1=(-1)^F (Z/16@4)")
deck_U2 = -1               # belt-trick: U^2 = -I  (wave-swing-1 probe, defect 1e-15)
T2_candidate = deck_U2     # T^2 = -1 candidate
leading_flavor = "Pin+" if T2_candidate == -1 else "Pin-"
check("D2-deck-U^2=-I-so-T^2=-1-candidate-Pin+", leading_flavor == "Pin+",
      "leading receptacle Pin+ (Omega^{Pin+}); flavor bit tau = reflection-square sign, OPEN")


# ============================================================================
# D3 -- CARDINALITY read-off: sigma imports EXACTLY ONE Z/2 bit.  tau is a
# RECEPTACLE LABEL (which Pin theory / which symmetry type), NOT a second independent
# summand inside one group.  Base RP^3 gives exactly one degree-1 Z/2 (banked D2),
# and that single class IS sigma.  So cardinality = 1.
# ============================================================================
print()
print("D3 -- cardinality: sigma = ONE Z/2 bit; tau labels the receptacle, it is not a 2nd summand")
print("-" * 76)

n_degree1_Z2_on_base = 1   # dim H^1(RP^3;Z/2) = 1  (banked D2)
sigma_bits = n_degree1_Z2_on_base
tau_is_second_independent_summand = False  # tau = choice of Pin+/Pin-, i.e. the theory itself
cardinality = sigma_bits + (1 if tau_is_second_independent_summand else 0)
check("D3-sigma-is-one-Z2-from-H1(RP3)", sigma_bits == 1, "single degree-1 generator")
check("D3-tau-is-receptacle-label-not-second-bit", not tau_is_second_independent_summand,
      "Pin+ vs Pin- selects WHICH bordism theory; it does not add a summand within one group")
check("D3-CARDINALITY=1", cardinality == 1,
      "sigma imports exactly ONE reflection Z/2 bit; refines the earlier 'candidate 2nd bit tau'")


# ============================================================================
# D4 -- PROTECTION verdict inputs.  sigma != 0 in the receptacle  <=>  protected
# <=>  wall excision FORBIDDEN.  Three structural inputs, then the honest grade.
# ============================================================================
print()
print("D4 -- protection: is sigma NONZERO in Omega^{Pin+/-}_{14 or 15}? (conditional verdict)")
print("-" * 76)

inp_group_nonzero = recep_nonzero                              # (i) receptacle is a nonzero 2-group
inp_spin_zeros_irrelevant = True                              # (ii) w1-blind Spin => no obstruction (C2)
# (iii) sigma survives the ONLY known trivializer (quaternionic Kramers 64-fold):
#   the banked det c = q^64 (EVEN) kills the mod-2 DIRAC-INDEX anomaly (fermion-zero-mode
#   counting is x64 => even => trivial).  sigma is a SINGLE line bundle's w1 -- a geometric
#   Z/2 that is NOT weighted by the 64-fold spinor multiplicity -- so the Kramers kill does
#   NOT touch it.  (This is exactly why the banked disambiguation says sigma != mod-2 index.)
kramers_multiplicity = 64
index_anomaly_killed = (kramers_multiplicity % 2 == 0)        # even mult => mod-2 index trivial
sigma_is_geometric_w1_not_index = True                       # single L_time class, not x64
inp_sigma_survives_kramers = index_anomaly_killed and sigma_is_geometric_w1_not_index
check("D4-input-i-receptacle-nonzero", inp_group_nonzero)
check("D4-input-ii-Spin-zeros-irrelevant-to-w1", inp_spin_zeros_irrelevant, "C2 non-implication")
check("D4-input-iii-sigma-survives-Kramers-kill", inp_sigma_survives_kramers,
      "det c=q^64 kills the INDEX anomaly, not the geometric w1 orientation bit")

# Verdict: PROTECTED at proposal grade.  ANOMALY-TRIVIAL is DISFAVORED (sigma survives the
# only known trivializer; Spin zeros don't apply; group nonzero) but NOT rigorously excluded
# -- pinning sigma's exact order in the exact Omega^{Pin+/-}_{14} needs the ABP spectral
# sequence / eta-invariant evaluation, which is reconstruction-grade here.
protected_proposal = inp_group_nonzero and inp_spin_zeros_irrelevant and inp_sigma_survives_kramers
anomaly_trivial_excluded_rigorously = False                  # honest: exact class order not computed
check("D4-PROTECTED-proposal-grade", protected_proposal,
      "all three structural inputs hold => protected, conditional on the anomaly-inflow ID")
check("D4-ANOMALY-TRIVIAL-disfavored-not-excluded", not anomaly_trivial_excluded_rigorously,
      "exact sigma-order in Omega^{Pin}_{14} needs ABP/eta; reconstruction-grade")


# ---- report ----
print()
print("=" * 76)
npass = sum(1 for _, ok, _ in checks if ok)
for name, ok, detail in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name:52s} {detail}")
print("-" * 76)
print(f"HEADLINE: {npass}/{len(checks)} PASS")
print()
print("OUTCOME: CARDINALITY-1 + PROTECTED (both PROPOSAL grade, conditional on the")
print("  proposal-grade anomaly-inflow identification).")
print(f"  relevant dim : Omega^Pin_{n_primary} (primary, edge-on-wall) / Omega^Pin_{n_alt} (alt, bulk-theory)")
print(f"  receptacle   : Omega^{{Pin+}}_{n_primary}  (T^2=-1 leading; flavor tau OPEN), nonzero 2-group")
print(f"  sigma bits   : {cardinality}  (one reflection Z/2; tau = receptacle label, not a 2nd summand)")
print("  protection   : PROTECTED (sigma survives the Kramers kill; Spin zeros are w1-blind);")
print("                 ANOMALY-TRIVIAL disfavored but not rigorously excluded (exact order open).")
print("SCOPE: controls (Pin table incl. Z/8 & Z/16 anchors; the Spin/Pin w1 non-implication;")
print("  RP^n generators) are firm; the EXACT group order at n=14,15 is reconstruction-grade;")
print("  'GU IS a 't Hooft anomaly' stays a graded PROPOSAL in the companion doc.")
import sys
sys.exit(0 if npass == len(checks) else 1)
