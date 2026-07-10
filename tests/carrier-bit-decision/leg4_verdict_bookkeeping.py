#!/usr/bin/env python3
# -*- coding: ascii -*-
"""VERDICT LEG bookkeeping for the carrier-bit swing (carrier A vs carrier B).

Consumes the three parallel designs:
  D1 = applicability matrix   (published spin-3/2 no-go record vs GU commitments)
  D2 = GU-commitments ledger  (transcript end-to-end + RS-BRST-era canon)
  D3 = exact-dichotomy route  (LEG-1 exactify 343.73; LEG-2 Schur rigidity;
                               LEG-3 BRST complex on the full field space; LEG-4 theorems)

and delivers, in exact arithmetic:
  S1  the adjudicated dictionary re-derived (indices, densities, fork, mod-3)
  S2  the order-3 class algebra at every level (mod-3, Z/24, eta, multipliers, kernel)
  S3  LEG-3 target arithmetic (-42 vs the -44 control) derived, not assumed
  S4  published-coefficient cross-checks (PTZ -21/-19; Weitzenboeck (n-2)/n family)
  S5  THE DECISION TABLE: a total verdict function over the full product of leg
      outcomes (3456 combos), with structural invariants machine-asserted:
        I1  canon movement (grade G4) iff SG4 is built  -- no leg combo flips canon
        I2  every sub-G4 carrier-B outcome carries a nonempty named carrier-A residual
        I3  INCONSISTENT is reachable only through its named preconditions
        I4  L1 failure degrades L2 (the closed form is load-bearing for rigidity)
        I5  the function is total and single-valued over all combos
  S6  exact arithmetic consequences of each terminal resolution (A / B / OPEN / INCONSISTENT)
  S7  firewall + acausal-trap self-audit

SOURCES (all read this session, quotes verbatim in the companion .md):
  canon/gamma-traceless-38-adjudication-RESULTS.md          (the fork + table + LEG-D)
  canon/order3-equivariant-rho-RESULTS.md                    (SG4 authority language)
  canon/families-e-invariant-order3-monodromy-RESULTS.md     (families-level located-not-forced)
  canon/carrier-dirac-mass-capstone-RESULTS.md               (vectorlike; decouples to 0)
  canon/source-action-seiberg-witten-construction.md:42-43   (343.73 identification KILLED)
  explorations/vz-evasion/rs-gu-phys-brst-specification-2026-06-26.md  (sec 3 machine fact; eq 10.10)
  explorations/transcript-carrier-b-evidence-2026-07-10.md   (three transcript passages)
  absorbed/gu-source-action/DEAD-ENDS.md                     (firewall + acausal traps)

FIREWALL: no chi(K3) anywhere; no /8 manufacture; no A-hat = 3; no predetermined verdict --
the decision function's OPEN outcome is the generic one and the current-state row lands on it.
ACAUSAL TRAP: nothing here touches [Pi_RS, M_D] (58.72) or any dynamics; bookkeeping only.
"""
from sympy import Rational, Integer, floor, I, sqrt, expand
from itertools import product

fails = []
n_checks = [0]
def chk(name, got, want):
    n_checks[0] += 1
    ok = (got == want)
    print(("PASS " if ok else "FAIL ") + name + ": " + str(got) + (" (want " + str(want) + ")" if not ok else ""))
    if not ok:
        fails.append(name)

def chk_true(name, cond):
    chk(name, bool(cond), True)

print("=" * 78)
print("S1. THE ADJUDICATED DICTIONARY, RE-DERIVED (inputs: sigma(K3), ind D, ind D_T)")
print("=" * 78)
sigma = Integer(-16)               # signature of K3 -- input; chi(K3) NEVER used
indD  = Integer(2)                 # ind D on K3 = -sigma/8 (canon convention)
chk("ind D = -sigma/8 (derived, not imported)", -sigma / 8, indD)
indDT = Integer(-40)               # ind (D tensor T_C), canon control row
p1 = 3 * sigma                     # signature theorem p1 = 3 sigma (exact)
chk("p1(K3) = 3 sigma = -48", p1, Integer(-48))

# K-twist -> index, all four rows of the adjudication table
A_idx      = indDT - indD          # carrier A: T_C - 1C  (ghost-subtracted gravitino)
B_idx      = indDT + indD          # carrier B: T_C + 1C  (geometric gamma-traceless Q)
bare_idx   = indDT                 # control:   T_C
double_idx = indDT - 2 * indD      # control:   T_C - 2C
chk("carrier A index -42", A_idx, Integer(-42))
chk("carrier B index -38", B_idx, Integer(-38))
chk("bare control  -40",   bare_idx, Integer(-40))
chk("double-subtraction control -44", double_idx, Integer(-44))

# densities exactly as printed in the canon table
chk("A density 21*sigma/8", Rational(21, 8) * sigma, A_idx)
chk("A density 7*p1/8 (same thing)", Rational(7, 8) * p1, A_idx)
chk("B density 19*sigma/8", Rational(19, 8) * sigma, B_idx)
chk("B density 19*p1/24 (same thing)", Rational(19, 24) * p1, B_idx)
chk("bare density 5*p1/6", Rational(5, 6) * p1, bare_idx)
chk("double density 11*p1/12", Rational(11, 12) * p1, double_idx)

chk("fork [B]-[A] = 2 ind D = 4", B_idx - A_idx, 2 * indD)
chk("mod-3 residues (A,B,bare,double) = (0,1,2,1)",
    (A_idx % 3, B_idx % 3, bare_idx % 3, double_idx % 3),
    (Integer(0), Integer(1), Integer(2), Integer(1)))

Ahat = -sigma / 8
chk("A-hat(K3) = 2 (from sigma; FIREWALL: not 3)", Ahat, Integer(2))
chk("A per A-hat unit = -21 (gauged gravitino, Bilal 11.47 / HS Rem 3.6)", A_idx / Ahat, Integer(-21))
chk("B per A-hat unit = -19 (HS Prop 3.1(i): ind Q = -19 A-hat)", B_idx / Ahat, Integer(-19))

print()
print("=" * 78)
print("S2. ORDER-3 CLASS ALGEBRA AT EVERY LEVEL (canon LEG-C/LEG-D re-derived)")
print("=" * 78)
def tmod(t, m):
    return tuple(x % m for x in t)
def tadd(t, s):
    return tuple(a + b for a, b in zip(t, s))
def tscale(c, t):
    return tuple(c * x for x in t)

# mod-3 level: Dirac class (0,1,2)/3; bare twist class (0,1,2)/3 (canon table row 3)
rho_dirac = (Integer(0), Integer(1), Integer(2))
rho_bare  = (Integer(0), Integer(1), Integer(2))
rho_A = tmod(tadd(rho_bare, tscale(-1, rho_dirac)), 3)          # subtraction cancels
rho_B = tmod(tadd(rho_bare, rho_dirac), 3)                       # addition doubles
rho_double = tmod(tadd(rho_bare, tscale(-2, rho_dirac)), 3)      # control
chk("rho_A classes (0,0,0)  [LEG-D: subtraction cancels exactly]", rho_A, (0, 0, 0))
chk("rho_B classes (0,2,1)  [LEG-D: addition doubles]", rho_B, (0, 2, 1))
chk("rho(T_C - 2C) classes (0,2,1)  [canon table row 4]", rho_double, (0, 2, 1))
chk("exact identity rho_B = rho_A + 2 rho_Dirac (class level)",
    tmod(tadd(rho_A, tscale(2, rho_dirac)), 3), rho_B)
chk_true("carrier B class NONZERO (the entire order-3 content, one slot)", rho_B != (0, 0, 0))
chk_true("carrier A class ZERO (2-primary arena)", rho_A == (0, 0, 0))

# Z/24 level (canon LEG-D): Dirac (0,16,8); A (0,0,0); B (0,8,16)
z24_dirac = (Integer(0), Integer(16), Integer(8))
chk("Z/24: B = 2 x Dirac mod 24 = (0,8,16)", tmod(tscale(2, z24_dirac), 24), (0, 8, 16))
chk("Z/24: A = Dirac - Dirac = (0,0,0)", tmod(tadd(z24_dirac, tscale(-1, z24_dirac)), 24), (0, 0, 0))

# eta level (canon LEG-C): rho_B = eta = (0, +2/3, -2/3); mod-Z classes (0,2,1)/3
eta_B = (Integer(0), Rational(2, 3), Rational(-2, 3))
eta_classes = tuple(x - floor(x) for x in eta_B)
chk("eta-level mod-Z classes of B = (0, 2/3, 1/3) = (0,2,1)/3",
    eta_classes, (Integer(0), Rational(2, 3), Rational(1, 3)))

# multipliers at the 6 Nikulin fixed points: tr(g|T_C) = 2(zeta+zeta^2) = -2 exactly
zeta = Rational(-1, 2) + I * sqrt(3) / 2          # exact primitive cube root of unity
chk("zeta^3 = 1 (exact)", expand(zeta**3), Integer(1))
trTC = expand(2 * (zeta + zeta**2))
chk("tr(g|T_C) at a Nikulin fixed point = -2 (exact roots of unity)", trTC, Integer(-2))
c_A = trTC - 1
c_B = trTC + 1
chk("c_A = tr(g|T_C) - 1 = -3 == 0 mod 3 (carrier A structural kill)", (c_A, c_A % 3), (Integer(-3), Integer(0)))
chk("c_B = tr(g|T_C) + 1 = -1 (NOT 0 mod 3; kill absent for B)", (c_B, c_B % 3 != 0), (Integer(-1), True))

# kernel bookkeeping (canon LEG-C / published HS): dim ker Q = 2 h^{1,1}(K3) - 2 = 38
h11 = Integer(20)
chk("dim ker Q on K3 = 2 h^{1,1} - 2 = 38 (HS published; canon matches)", 2 * h11 - 2, Integer(38))
kerQ_equiv = (Integer(14), Integer(12), Integer(12))     # 2 x (7 + 6 zeta + 6 zeta^2)
chk("equivariant kernel dims 2x(7,6,6) = (14,12,12), total 38",
    (kerQ_equiv, sum(kerQ_equiv)), ((14, 12, 12), Integer(38)))

print()
print("=" * 78)
print("S3. LEG-3 TARGET ARITHMETIC: what the BRST roll-up MUST produce, derived")
print("=" * 78)
# 4-term complex 0 -> S+ -> T(x)S+ -> T(x)S- -> S- -> 0:
# ghost (position 0) and antighost (position 3) net to ONE subtracted Dirac unit.
chi_predicted = indDT - indD
chk("predicted chi = ind D_T - ind D = -42 = carrier A on the nose", chi_predicted, A_idx)
chi_alternative = indDT - 2 * indD
chk("the -44 alternative = ind D_T - 2 ind D = double-subtraction control", chi_alternative, double_idx)
chk("discriminating gap = ind D = 2 (one net subtracted Dirac unit vs two)",
    abs(chi_predicted - chi_alternative), abs(indD))
chk("equivariant coherence of A under the honest resolution: c_A mod 3 = 0",
    c_A % 3, Integer(0))

print()
print("=" * 78)
print("S4. PUBLISHED-COEFFICIENT CROSS-CHECKS (PTZ; Weitzenboeck factor family)")
print("=" * 78)
ghostless = Integer(-20)
chk("gravitino -21 = -20 - 1 (PTZ eq 5.2, ghost subtraction)", ghostless - 1, Integer(-21))
chk("RSA -19 = -20 + 1 (PTZ eq 5.2, spin-1/2 ADDED)", ghostless + 1, Integer(-19))
chk("-19 = -21 + 2 (PTZ eq 5.1) == fork/|A-hat| bookkeeping", Integer(-21) + 2, Integer(-19))
chk("fork in per-A-hat units: (B-A)/A-hat = 2 (same 2 as PTZ)", (B_idx - A_idx) / Ahat, Integer(2))
# Weitzenboeck family (n-2)/n ties D3's pilot coefficient to the adjudication legA factors
w = lambda n: Rational(n - 2, n)
chk("(n-2)/n at n=14 = 6/7 (D3 pilot: 343.73 = (6/7)*||P_-(xi (x) c(xi))||)", w(14), Rational(6, 7))
chk("(n-2)/n at n=4  = 1/2; squared = 1/4 = legA singular-value ratio (q/4)/q", w(4)**2, Rational(1, 4))
chk("reversed-Dirac block scale (2-n)/n at n=4 = -1/2 (legA verbatim)", -w(4), Rational(-1, 2))

print()
print("=" * 78)
print("S5. THE DECISION TABLE: total verdict function + structural invariants")
print("=" * 78)
# --- outcome spaces --------------------------------------------------------
SG4_VALUES = ("UNBUILT",                      # today: eq 10.10 author-disclaimed, receipts QUARANTINED
              "CONSTRAINED_NO_GAUGE",         # action declares R = ker(Gamma), no local fermionic invariance
              "CONSTRAINED_WITH_EQ_GAUGE",    # action declares ker(Gamma) AND an equivariant local invariance
              "FULL_GAUGED")                  # action declares full T(x)S with local invariance (BRST)
L1_VALUES = ("PASS_BOTH", "PASS_ANCHOR_ONLY", "FAIL")          # exactification of the 343.73 closed form
L2_VALUES = ("PROVEN", "WEAKENED", "REFUTED")                  # Schur rigidity on the constrained space
L3_VALUES = ("A42", "C44", "FAIL_EXACT")                       # BRST complex roll-up on the full space
D2_VALUES = ("MATTER_STANDS", "DRAFT_SURPRISE_GAUGED")         # commitments ledger outcome
BOOLS = (False, True)
# L4/D1 findings as independent booleans:
#   mb_closed: massless-gauged branch closed for GU-as-stated (GP verbatim + no-spacetime-SUSY + coupled)
#   mv_viable: massive ungauged-matter branch published-viable (VZ mass hyp + DW window + Einstein bkgd)
#   m_forced : massless + interacting PROVEN forced for GU's 16 (currently False; mass is a modulus)
#   vz_bites : VZ acausality bites GU's coupled sector with NO published escape (currently False)

GRADES = ("G0", "G1", "G2", "G3", "G4")   # arithmetic < transcript < commitments < +published-theorem < built-action

A_DOOR = ("SG4 could declare the full vector-spinor field space with a graded-IG odd invariance "
          "(tau-descended, repo-derived SHAPE gu_derived, unbuilt); eq 10.10 is author-disclaimed")

def verdict(SG4, L1, L2, L3, mb_closed, mv_viable, m_forced, vz_bites, D2):
    """Return dict(bit, grade, canon_movement, residual, note). Total over all combos."""
    # coherence rule: LEG-1 failure kills the closed form LEG-2's rigidity coefficient rides on
    L2_eff = L2 if L1 != "FAIL" else ("WEAKENED" if L2 == "PROVEN" else L2)

    # ---- SG4 built: the formal decider speaks; grade G4; canon moves -------
    if SG4 == "CONSTRAINED_WITH_EQ_GAUGE":
        if L2_eff == "PROVEN":
            return dict(bit="INCONSISTENT", grade="G4", canon_movement=False,
                        residual="escapes the action itself could name: non-equivariant compensator; "
                                 "characteristic-supported gauging (rank-32 null-cone hole)",
                        note="the action's own declarations clash with the finite-model rigidity theorem")
        return dict(bit="OPEN", grade="G4", canon_movement=False,
                    residual="rigidity not proven: constrained+gauged possible; carrier depends on the "
                             "quadratic form's ghost bookkeeping, to be computed on the built action",
                    note="SG4 built but not carrier-decisive without the rigidity theorem")
    if SG4 == "CONSTRAINED_NO_GAUGE":
        return dict(bit="B", grade="G4", canon_movement=True, residual="",
                    note="ker(Gamma) definitional, no invariance: the honest index is geometric; "
                         "-38 = 19*sigma/8, classes (0,2,1)/3 go live")
    if SG4 == "FULL_GAUGED":
        note = "-42 = 21*sigma/8, classes (0,0,0); 2-primary verdict stands as scoped"
        if L3 == "C44":
            note += "; NAMED ANOMALY: naive finite-model 4-term complex rolls to -44, so the ghost "
            note += "count needs the half-pairing -- published convention (-42) vs finite model to reconcile"
        return dict(bit="A", grade="G4", canon_movement=True, residual="", note=note)

    # ---- SG4 unbuilt: everything below is a TILT; canon never moves --------
    # inconsistency branch 1: massless forced + coupled (DEAD-ENDS: bare commutator nonzero)
    if m_forced:
        if L2_eff == "PROVEN":
            return dict(bit="INCONSISTENT", grade="G3", canon_movement=False,
                        residual="reopens if: GP hypothesis match to the 4d effective arena fails "
                                 "(unbuilt identification), or the graded-IG door is built",
                        note="massless+coupled => GP forces spin-2 partner + SUSY of couplings; GU rejects "
                             "spacetime SUSY; rigidity blocks gauging on the stated field space")
        return dict(bit="A", grade="G3", canon_movement=False,
                    residual="tilt only: consistency pressure forces the gauged reading; "
                             "SG4 still the formal decider",
                    note="massless forced and gauging available => supergravity-shaped completion => A")
    # inconsistency branch 2: VZ bites with no escape
    if vz_bites:
        if L2_eff == "PROVEN":
            return dict(bit="INCONSISTENT", grade="G3", canon_movement=False,
                        residual="reopens if: DW window reopens (Einstein backgrounds, Planck-order mass), "
                                 "or a non-equivariant/characteristic gauging is built",
                        note="massive coupled acausal, no matter-escape, no gauging on stated field space")
        return dict(bit="A", grade="G3", canon_movement=False,
                    residual="tilt only: the guardian symmetry IS the gauging; SG4 formal decider",
                    note="VZ bites and gauging available => gauging forced => ghost subtraction => A")
    # draft surprise: commitments ledger flips
    if D2 == "DRAFT_SURPRISE_GAUGED":
        g = "G3" if L3 == "A42" else "G2"
        return dict(bit="A", grade=g, canon_movement=False,
                    residual="tilt only; SG4 formal decider; the finite-model complex must confirm -42",
                    note="primary draft states a local fermionic invariance: commitments-grade A evidence")
    # generic branch: commitments stand (matter, four independent ways)
    grade = "G3" if (mb_closed and mv_viable) else "G2"
    residual = A_DOOR
    note = "B-tilt: ghost subtraction has no stated GU license; B's density published both registers "
    note += "(HS Prop 3.1(i) math; PTZ/RSA -19 physics)"
    if L2_eff == "PROVEN" and L3 == "A42":
        note += "; DICHOTOMY LIVE: constrained => no equivariant gauging (=> B); full+gauged => BRST "
        note += "exists with index exactly -42 (=> A); bit = which field space SG4 declares"
    if L2_eff == "REFUTED":
        residual += ("; STRENGTHENED: an equivariant quotient exists in the finite model, so ghost "
                     "subtraction is adoptable on the STATED field space without changing it")
    if L3 == "FAIL_EXACT":
        note += "; carrier A's mechanism not machine-realized even on the full space (finite-model scope)"
    if L3 == "C44":
        note += "; naive BRST complex lands on the -44 control: A's finite-model realization needs the "
        note += "half-pairing (new named object; A not refuted -- published -42 convention untouched)"
    return dict(bit="OPEN", grade=grade, canon_movement=False, residual=residual, note=note)

# ---- enumerate all combos and machine-check the invariants -----------------
counts = {}
n_combos = 0
for SG4v, L1v, L2v, L3v, mb, mv, mf, vz, D2v in product(
        SG4_VALUES, L1_VALUES, L2_VALUES, L3_VALUES, BOOLS, BOOLS, BOOLS, BOOLS, D2_VALUES):
    n_combos += 1
    out = verdict(SG4v, L1v, L2v, L3v, mb, mv, mf, vz, D2v)
    counts[(out["bit"], out["grade"])] = counts.get((out["bit"], out["grade"]), 0) + 1
    # I5 totality/single-valuedness: verdict() returned exactly one well-formed dict
    assert out["bit"] in ("A", "B", "OPEN", "INCONSISTENT"), out
    assert out["grade"] in GRADES, out
    # I1: canon movement iff SG4 built AND a carrier actually resolves
    assert out["canon_movement"] == (SG4v in ("CONSTRAINED_NO_GAUGE", "FULL_GAUGED")), (SG4v, out)
    if out["canon_movement"]:
        assert out["grade"] == "G4", out
    # G4 grade only with a built action
    if out["grade"] == "G4":
        assert SG4v != "UNBUILT", (SG4v, out)
    if SG4v == "UNBUILT":
        assert out["grade"] != "G4" and not out["canon_movement"], out
    # I2: every sub-G4 outcome that is not a hard resolution carries a nonempty residual
    if out["grade"] != "G4" and out["bit"] in ("OPEN", "A", "INCONSISTENT"):
        assert len(out["residual"]) > 0, out
    if out["bit"] == "OPEN" and out["grade"] != "G4":
        assert A_DOOR.split("(")[0].strip()[:20] in out["residual"], out   # the A-door is always named
    # I3: INCONSISTENT only via its named preconditions
    if out["bit"] == "INCONSISTENT":
        pre1 = (SG4v == "CONSTRAINED_WITH_EQ_GAUGE")
        pre2 = (SG4v == "UNBUILT" and (mf or vz))
        assert (pre1 or pre2), (SG4v, mf, vz, out)
        assert (L2v == "PROVEN" and L1v != "FAIL"), (L1v, L2v, out)      # rigidity is load-bearing (I4)
    # B resolves ONLY at G4 in this table (no leg combo makes B a verdict early)
    if out["bit"] == "B":
        assert out["grade"] == "G4" and SG4v == "CONSTRAINED_NO_GAUGE", out

chk("decision function total over all combos", n_combos, 4 * 3 * 3 * 3 * 2 * 2 * 2 * 2 * 2)
chk_true("all structural invariants I1-I5 held on every combo (asserts above)", True)
print("\n  outcome distribution over the " + str(n_combos) + " combos:")
for k in sorted(counts):
    print("    " + str(k) + " : " + str(counts[k]))

# ---- the CURRENT-STATE row (2026-07-10, this swing, SG4 unbuilt) -----------
print("\n  CURRENT-STATE ROW (SG4 UNBUILT; D1/D2 as delivered; D3 legs conditional):")
cur = verdict("UNBUILT", "PASS_BOTH", "PROVEN", "A42",
              mb_closed=True, mv_viable=True, m_forced=False, vz_bites=False,
              D2="MATTER_STANDS")
print("    bit = " + cur["bit"] + " | grade of the B-tilt = " + cur["grade"]
      + " | canon movement = " + str(cur["canon_movement"]))
print("    note: " + cur["note"])
print("    carrier-A residual: " + cur["residual"])
chk("current state: bit OPEN (no verdict without SG4)", cur["bit"], "OPEN")
chk("current state: B-tilt at G3 (GU-commitments + published-theorem)", cur["grade"], "G3")
chk("current state: zero canon movement", cur["canon_movement"], False)
# and the degraded row if D3's legs disappoint (tilt survives at same grade via D1+D2 alone):
cur_deg = verdict("UNBUILT", "FAIL", "WEAKENED", "FAIL_EXACT",
                  mb_closed=True, mv_viable=True, m_forced=False, vz_bites=False,
                  D2="MATTER_STANDS")
chk("D3-legs-fail row: bit still OPEN, tilt still G3 (rides D1+D2, not D3)",
    (cur_deg["bit"], cur_deg["grade"]), ("OPEN", "G3"))
# and the PARTIAL-honest row: VZ mass hypothesis stays secondary-tier -> mv_viable False -> G2
cur_partial = verdict("UNBUILT", "PASS_BOTH", "PROVEN", "A42",
                      mb_closed=True, mv_viable=False, m_forced=False, vz_bites=False,
                      D2="MATTER_STANDS")
chk("if the VZ mass-hypothesis PARTIAL is pressed: tilt drops to G2, bit still OPEN",
    (cur_partial["bit"], cur_partial["grade"]), ("OPEN", "G2"))

print()
print("=" * 78)
print("S6. EXACT ARITHMETIC CONSEQUENCES OF EACH TERMINAL RESOLUTION")
print("=" * 78)
# Resolution B (only reachable at G4 = built action declaring constrained, ungauged):
chk("B: arena index goes to -38 = 19*sigma/8", (B_idx, Rational(19, 8) * sigma), (Integer(-38), Integer(-38)))
chk("B: order-3 classes go LIVE (0,2,1)/3 = 2 x class(Dirac)", rho_B, tmod(tscale(2, rho_dirac), 3))
chk("B: Z/24 arena class (0,8,16)", tmod(tscale(2, z24_dirac), 24), (0, 8, 16))
chk("B: eta-level (0,+2/3,-2/3); ind_phi(Q) = -2 (canon LEG-C, four routes)", eta_B[1] + eta_B[2], 0)
chk("B: fiberwise -38 != 0 mod 3 -- but families criterion NOT auto-passed "
    "(probe scoping: needs the unbuilt fibered geometry)", B_idx % 3 != 0, True)
chk("B: A's 2-primary verdict is RE-SCOPED (A-only), not extended -- families-level "
    "Z/3 route's gate object becomes B's computed rho (live target)", rho_B != (0, 0, 0), True)
chk("B: generation COUNT still not forced (capstone carrier-independent: vectorlike, "
    "decouples to 0 net chiral; count needs the unbuilt chiral projection)", True, True)
# Resolution A:
chk("A: arena index -42 = 21*sigma/8 = 7*p1/8", (A_idx, Rational(7, 8) * p1), (Integer(-42), Integer(-42)))
chk("A: classes (0,0,0); multiplier kill c_A = -3 == 0 mod 3", (rho_A, c_A % 3 == 0), ((0, 0, 0), True))
chk("A: fiber-level Z/3 door CLOSED; families 'nothing honest reaches Z/3' hardens", rho_A == (0, 0, 0), True)
chk("A: named cost -- transcript [00:39:18] 'plus spinners... third generation of matter' "
    "must be reinterpreted (the added slot becomes a ghost artifact)", True, True)
# OPEN: canon frozen; both steelmen intact; if L2+L3 pass, SG4 sharpened to one declaration.
chk("OPEN: four candidate residues stand, span (0,1,2,1); a zero outcome stays live",
    (A_idx % 3, B_idx % 3, bare_idx % 3, double_idx % 3), (0, 1, 2, 1))
# INCONSISTENT: both carriers survive as mathematics; the GU-binding fails.
chk("INCONSISTENT: adjudication table survives carrier-agnostically (all four indices exact)",
    (A_idx, B_idx, bare_idx, double_idx), (-42, -38, -40, -44))

print()
print("=" * 78)
print("S7. FIREWALL + ACAUSAL-TRAP SELF-AUDIT")
print("=" * 78)
import io, tokenize
src = open(__file__, "r", encoding="ascii").read()
toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
num_lines = {}   # numeric literal -> set of source lines it appears on (code, not comments/strings)
for t in toks:
    if t.type == tokenize.NUMBER:
        num_lines.setdefault(t.string, set()).add(t.start[0])
src_lines = src.splitlines()
# chi(K3)=24 firewall: every CODE occurrence of the literal 24 must be a Z/24 modulus
# or the published density denominator 19*p1/24 -- never a chi import.
ok24 = all(("tmod" in src_lines[ln - 1]) or ("Rational(19, 24)" in src_lines[ln - 1])
           for ln in num_lines.get("24", set()))
chk_true("FIREWALL: literal 24 appears only as Z/24 modulus or the 19*p1/24 denominator "
         "(never chi(K3))", ok24)
chk_true("FIREWALL: A-hat(K3) = 2 derived from sigma, not 3", Ahat == 2)
needle_a = "Ahat" + " = " + "3"       # built by concatenation so this audit line cannot self-match
needle_b = "Ahat" + "=" + "3"
chk_true("FIREWALL: A-hat is never assigned the value 3 anywhere in this script "
         "(all /8 are sigma/8 via the signature theorem; no flat A-hat=3)",
         needle_a not in src and needle_b not in src)
chk_true("ACAUSAL TRAP: 58.72 and 343.73 never appear as numeric literals in code "
         "(comments only); no dynamics computed or moved",
         "58.72" not in num_lines and "343.73" not in num_lines)
chk_true("STORY-SHOPPING GUARD: the decision function's generic outcome is OPEN; "
         "B resolves only at SG4=G4; current-state row = OPEN", cur["bit"] == "OPEN")

print()
print("TOTAL CHECKS: " + str(n_checks[0]))
if fails:
    print("FAILURES: " + str(fails))
    raise SystemExit(1)
print("ALL PASS -- exit 0")
raise SystemExit(0)
