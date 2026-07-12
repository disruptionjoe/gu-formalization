"""W63 -- Path 4 Branch C (B2): the observerse / issuance bridge, graded.

This test encodes the GRADED STATUS of the observerse/issuance-bridge candidate, not a
positive physics claim. It has two jobs:

  PART A -- recompute the FORCED geometric core (family-invariant, from B1). These are real
            assertions on real numbers: the constant (vacuum) section of Met(X4) is NOT totally
            geodesic (II != 0), its mean curvature lies along the pure-trace / conformal
            direction, and that direction has NEGATIVE DeWitt norm (|H|^2_V = -1) while the full
            |II|^2_V = +2. Signature of the DeWitt/gimmel metric only; nothing fit to f_0.

  PART B -- encode the STRUCTURAL CRITERIA the observerse statement would have to meet to be a
            forced theorem, and assert the CURRENT STATUS of each honestly (as booleans that are
            KNOWN today). This is the "encode the precise structural criterion + assert current
            status" instruction from the brief: the bridge is NOT yet a theorem, and the test
            makes that machine-checkable so the claim cannot silently drift upward.

Construction (GEOMETER-VS-PHYSICS-OBJECTS.md): program-native -- DeWitt/gimmel metric-on-metrics,
Krein ghost-clearance. No positive-Hilbert default.

Verdict encoded: NO forced novel theorem. Forced geometric core = YES (and family-invariant).
Observerse BRIDGE (P, the issuance-rate reading, the CAP mapping) = NOT forced / analogy / false-
as-a-rate. Exit 0 = the graded status is exactly as claimed in the exploration doc.

Run: python tests/W63_path4_C_observerse.py
"""
from __future__ import annotations

import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ===========================================================================
# PART A -- the FORCED geometric core (family-invariant). Recomputed from the
# DeWitt vertical SFF of the constant section, exactly as in
# tests/threads/B_constant_section_background_curvature.py. Depends only on the
# DeWitt/gimmel metric + eta -- NOT on beta/alpha, mu_DW, alpha (the residual family data).
# ===========================================================================
print("[W63] Path 4 Branch C -- observerse/issuance bridge, graded status\n")
print("PART A -- forced geometric core (family-invariant; DeWitt signature only):")

n = 4
eta = sp.diag(-1, 1, 1, 1)
etaU = eta.inv()


def sym2(A, i, j, k, l):
    return sp.Rational(1, 2) * (A[i, k] * A[j, l] + A[i, l] * A[j, k])


def B(mu, nu, a, b):
    # Vertical SFF of the constant section (ii-s-coordinate-formula sec 6.1).
    return -sp.Rational(1, 2) * (sym2(eta, a, b, mu, nu) - sp.Rational(1, 2) * eta[a, b] * eta[mu, nu])


def Vup(a, b, c, d):
    # Raised DeWitt vertical metric (trace-reversed Frobenius).
    return sym2(etaU, a, b, c, d) - sp.Rational(1, 2) * etaU[a, b] * etaU[c, d]


# II != 0: the vacuum section is NOT totally geodesic (the "non-collapse" geometric datum).
nonzero = any(sp.simplify(B(mu, nu, a, b)) != 0
              for mu in range(n) for nu in range(n) for a in range(n) for b in range(n))
check("vacuum section NOT totally geodesic (II != 0) -- the forced geometric 'non-collapse' datum",
      nonzero)

# Mean curvature H_ab = eta^{mu nu} B_{mu nu, ab}, and it is pure-trace (~ eta_ab): the conformal dir.
H = sp.zeros(n, n)
for a in range(n):
    for b in range(n):
        H[a, b] = sp.simplify(sum(etaU[mu, nu] * B(mu, nu, a, b) for mu in range(n) for nu in range(n)))
c_base = sp.simplify(H[1, 1] / eta[1, 1])
pure_trace = all(sp.simplify(H[a, b] - c_base * eta[a, b]) == 0 for a in range(n) for b in range(n))
check("mean curvature lies along the PURE-TRACE / conformal direction (H_ab = (1/2) eta_ab)",
      pure_trace and c_base == sp.Rational(1, 2), f"coeff = {c_base}")

# The load-bearing sign facts: |H|^2_V = -1 (NEGATIVE, conformal ghost) ; |II|^2_V = +2 (positive).
H2 = sp.simplify(sum(Vup(a, b, c, d) * H[a, b] * H[c, d]
                     for a in range(n) for b in range(n) for c in range(n) for d in range(n)))
II2 = 0
for mu in range(n):
    for nu in range(n):
        for rho in range(n):
            for sig in range(n):
                for a in range(n):
                    for b in range(n):
                        for c in range(n):
                            for d in range(n):
                                II2 += (etaU[mu, rho] * etaU[nu, sig] * Vup(a, b, c, d)
                                        * B(mu, nu, a, b) * B(rho, sig, c, d))
II2 = sp.simplify(II2)
print(f"    |H|^2_V = {H2}   |II|^2_V = {II2}")
check("|H|^2_V = -1 (NEGATIVE-norm conformal mode: GHP ghost, forced by DeWitt signature)", H2 == -1)
check("|II|^2_V = +2 (POSITIVE full shape-energy)", II2 == 2)
check("the sign of the non-collapse cost is set by the H-vs-II (OQ2-A) choice -- H negative, II positive",
      H2 < 0 < II2,
      "the observerse 'non-collapse cost' is Krein-indefinite: sign is a functional choice, not fixed by geometry")

# Family-invariance witness: the core uses ONLY eta + the DeWitt metric; no residual family symbol
# (beta, alpha, mu_DW) appears. Encoded as: the computed quantities are pure rationals (scale-free).
core_is_scale_free = all(q.free_symbols == set() for q in (H2, II2, c_base))
check("forced core is family-INVARIANT (pure numbers; no beta/alpha, mu_DW, alpha enter)",
      core_is_scale_free)


# ===========================================================================
# PART B -- the observerse BRIDGE: structural criteria + honest current status.
# Each boolean is a fact KNOWN today (with its in-repo anchor). The test asserts the
# graded verdict so it cannot drift upward silently.
# ===========================================================================
print("\nPART B -- observerse bridge: structural criteria and CURRENT status (honest):")

# Criterion 1: is "f_0 is an issuance RATE" true? NO -- rate-independence finding.
# f_0/c_L/alpha_W enter STRUCTURAL field equations; a rate would be rate-independent and drop out.
f0_is_a_rate = False  # refuted by explorations/.../fr-series-synthesis + rate-independence-negative-finding
check("literal 'f_0 = issuance RATE' is FALSE (rate-independence: rates don't enter structural theorems)",
      f0_is_a_rate is False,
      "anchor: fr-series-synthesis-2026-06-22 (4 objects, 1 word); rate proper is absorbed / GU-irrelevant")

# Criterion 2: does the 'observerse CAP/FLP' mapping have CAP's structural engine? NO -- no agreement predicate.
observerse_cap_has_agreement_predicate = False  # same missing joint that KILLED count-as-consensus
check("'observerse CAP/FLP' is an ANALOGY, not a theorem (no agreement-under-partition predicate)",
      observerse_cap_has_agreement_predicate is False,
      "anchor: count-as-consensus-...-KILLED-2026-07-10 ('no cross-gen shared variable ... category error')")

# Criterion 3: is postulate P ('non-collapse iff II != 0') a THEOREM or a definition? Definition.
P_is_a_theorem = False  # would require the filtration->section map, which does not exist in this repo
check("postulate P (non-collapse <=> II != 0) is a DEFINITION, not a forced theorem",
      P_is_a_theorem is False,
      "the collapse<=>totally-geodesic equivalence is not proven; the map {F_tau} -> sections of Met(X4) is absent")

# Criterion 4: does the missing object exist that would upgrade P to a theorem? NO -- named, not built.
filtration_to_section_map_exists = False
check("the upgrade object (record filtration {F_tau} -> sections of Met(X4)) does NOT exist here",
      filtration_to_section_map_exists is False,
      "highest-leverage missing object; needs sibling-repo machinery (cross-repo, out of scope)")

# The conditional theorem that DOES survive: forced GIVEN P. Encode 'every link except P is forced'.
# Links: (i) II != 0 forced [PART A], (ii) H conformal [PART A], (iii) |H|^2_V<0 forced [PART A],
# (iv) => Krein required (ghost-clearance fork). All forced; only P is not.
conditional_links_all_forced_except_P = nonzero and pure_trace and (H2 < 0)
check("CONDITIONAL theorem 'non-collapse => Krein (given P)': every link EXCEPT P is forced & family-invariant",
      conditional_links_all_forced_except_P,
      "but Krein is ALSO forced by (9,5) signature alone -> the bridge may be re-deriving a known necessity")

# The graded verdict, encoded as the tuple the orchestrator consumes.
Q_forced = "PARTIAL"   # geometry forced & family-invariant; bridge (P, rate) NOT forced
Q_novel = "LOW-MED"    # forced core = GHP known physics; linkage medium/repo-novel, packaging not prediction
Q_disc = "LOW"         # |H|^2_V=-1 is definitional, not a discriminating prediction; no lab test on the bridge
is_theorem = False     # NOT an unconditional theorem; a conditional identity with a definitional postulate
print(f"\n    graded verdict: Q-forced={Q_forced}  Q-novel={Q_novel}  Q-disc={Q_disc}  unconditional_theorem={is_theorem}")
check("graded verdict recorded: forced core YES, forced BRIDGE NO -> no forced novel theorem",
      (Q_forced == "PARTIAL") and (is_theorem is False))

# ---------------------------------------------------------------------------
print("\n[verdict]")
print("  FORCED geometric core (family-invariant): the vacuum section of Met(X4) is not totally")
print("  geodesic (II != 0); its mean curvature is the conformal mode; |H|^2_V = -1 (negative,")
print("  the GHP ghost), |II|^2_V = +2. Signature fact, no f_0 imported.")
print("  OBSERVERSE BRIDGE: 'f_0 = issuance rate' is FALSE (rate-independence); 'observerse CAP' is")
print("  an ANALOGY (no agreement predicate); postulate P is a DEFINITION. The surviving statement is")
print("  a CONDITIONAL identity 'non-collapse => Krein, given P' -- forced in every link except P, but")
print("  Krein is already forced by (9,5), so the bridge is decorative until the {F_tau}->section map")
print("  is built. NO forced novel theorem. Graded, not inflated. No canon/status movement.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = graded status confirmed: forced geometric core real & family-invariant;")
print("         observerse/issuance bridge NOT forced (analogy/definition/false-as-rate).")
