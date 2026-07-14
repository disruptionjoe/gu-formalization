"""Source-action requirements spec: cross-consistency checks (2026-07-13).

Companion test for explorations/source-action-requirements-spec-2026-07-13.md.

This is a CONSOLIDATION test, not new physics. Every check reproduces or
cross-checks arithmetic already established in the cited repo artifacts, to
certify that the requirements collected in the spec are mutually consistent
at the level of established dimension counts, residues, and windows:

  A. Soldering/connection collapse: codim-8165 == "image is so(9,5)"
     (wave34; one datum, not two).
  B. Sector bookkeeping: the g=1 ker-Gamma cure (RS sector, spinor-valued
     1-forms) and the k=0 Yukawa channel (Dirac spinor sector) live on
     different Hom spaces; the dimension arithmetic of both closes
     (wave17/wave35 + yukawa-scoping checksum).
  C. Count residues: -42 % 3 = 0 (carrier A, cannot select),
     -38 % 3 = 1 (carrier B, index-changing) (H39).
  D. Cure uniqueness: leakage(g) = (1-g) C2 has the unique root g = 1
     (wave35 minimal-basis leakage law, reproduced as arithmetic).
  E. FN mod-3 sterility + the larger-symmetry escape: for ALL 27 charge
     assignments q in (Z/3)^3 every Z/3-invariant Yukawa entry has FN
     exponent 0 mod 3 (sterile), while an integer lift (charges beyond
     mod 3) reducing to rho = (0,2,1) exists and DOES grade invariant
     entries -- i.e. requirement SA-Y5's escape route is arithmetically
     open and does not contradict the built Z/3 (yukawa-scoping).
  F. mu_DW window closure: the track2 floor band [~3.4, ~4.8] meV
     reproduces from the argued sub-mm boundary band [45, 52] um and
     m2_eff in [5/6, 5/4]; the refused H36 point (2.94 meV, c_L = 3/8)
     lands in the excluded lambda band [60.0, 73.6] um (tests/track2/T2A).
  G. Class tallies of the spec's requirements table (FORCED/DECLARATION/
     FIT counts match the spec's stated counts).

Deterministic, stdlib only, exit 0 on success.
"""

import math

FAILURES = []


def check(name, cond):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}")
    if not cond:
        FAILURES.append(name)


# ---------------------------------------------------------------- A
dim_sp64H = 64 * (2 * 64 + 1)          # 8256
dim_so95 = 14 * 13 // 2                # 91
check("A1 dim sp(64,H) = 8256", dim_sp64H == 8256)
check("A2 dim so(9,5) = 91", dim_so95 == 91)
check("A3 soldering codim 8165 = 8256 - 91 (items collapse to one datum)",
      dim_sp64H - dim_so95 == 8165)

# ---------------------------------------------------------------- B
dim_S = 128                            # Cl(9,5) Dirac module
dim_V = 14
dim_RS = dim_V * dim_S                 # spinor-valued 1-forms
rank_Gamma = dim_S                     # gamma-trace surjects onto spinors
ker_Gamma = dim_RS - rank_Gamma
check("B1 RS carrier dim 14*128 = 1792", dim_RS == 1792)
check("B2 ker Gamma = 1664 (wave35 rank(Pi_RS))", ker_Gamma == 1664)
check("B3 generation triplet 192 = 3*64 fits inside ker Gamma",
      192 == 3 * 64 and 192 <= ker_Gamma)
# dim Lambda^2_+(R^4) = 3 (the only derived '3')
check("B4 dim Lambda^2_+(R^4) = 3", math.comb(4, 2) // 2 == 3)
# End(S) = sum_k Lambda^k(V14), multiplicity 1: checksum saturation, which
# is what makes the non-form-carrier Yukawa no-go exact (yukawa-scoping).
check("B5 Yukawa channel checksum sum_k C(14,k) = 16384 = 128^2",
      sum(math.comb(14, k) for k in range(15)) == 16384 == dim_S ** 2)
# Sector disjointness (the SA-C2 vs SA-Y2 coexistence check): the cure acts
# on Hom spaces over the RS bundle (dim 1792), the scalar Yukawa channel on
# Hom(S x S, Lambda^0) over the spinor module (dim 128). Distinct carriers,
# no shared Hom space; both dimension books close independently.
check("B6 cure sector (1792) and Yukawa sector (128) are distinct carriers",
      dim_RS != dim_S and ker_Gamma + rank_Gamma == dim_RS)

# ---------------------------------------------------------------- C
check("C1 carrier A index -42 is 3-divisible (cannot select)",
      (-42) % 3 == 0)
check("C2 carrier B index -38 is index-changing mod 3", (-38) % 3 == 1)
check("C3 controls: bare -40 -> 2, double -44 -> 1",
      (-40) % 3 == 2 and (-44) % 3 == 1)
check("C4 residue trap: a net chiral index of exactly 3 has residue 0",
      3 % 3 == 0 == (-42) % 3)

# ---------------------------------------------------------------- D
C2 = 155.3625
leak = lambda g: (1.0 - g) * C2
check("D1 leakage(0) = C2 (built minimal operator leaks)",
      abs(leak(0.0) - C2) < 1e-12)
check("D2 leakage(1/2) = C2/2 (linear law)",
      abs(leak(0.5) - C2 / 2) < 1e-12)
check("D3 unique causal root g = 1 (full ker-Gamma projection)",
      leak(1.0) == 0.0 and all(leak(g) != 0.0
                               for g in (0.0, 0.25, 0.5, 0.75, 0.99)))
check("D4 degree-1 homogeneity marker: 155.3625/24 is non-integer "
      "(symbol norm, not an index)", abs(C2 / 24 - round(C2 / 24)) > 0.1)

# ---------------------------------------------------------------- E
rho = (0, 2, 1)  # carrier B order-3 spectral labels (H39)
# charges-add fork: invariant entries (i,j) have (q_i + q_j) % 3 == 0
inv_support = [(i, j) for i in range(3) for j in range(3)
               if (rho[i] + rho[j]) % 3 == 0]
check("E1 Z/3-invariant Yukawa support = {(0,0),(1,2),(2,1)}, dim 3",
      sorted(inv_support) == [(0, 0), (1, 2), (2, 1)])
# FN sterility: for ALL 27 mod-3 assignments, every invariant entry has
# FN exponent 0 mod 3 (a mod-3 flavon grades nothing that survives).
sterile = all(
    all((q[i] + q[j]) % 3 == 0
        for i in range(3) for j in range(3) if (q[i] + q[j]) % 3 == 0)
    for q in [(a, b, c) for a in range(3) for b in range(3)
              for c in range(3)]
)
check("E2 FN sterility: all 27 mod-3 charge assignments are sterile "
      "(tautologically: invariant = charge sum 0)", sterile)
# Larger-symmetry escape (SA-Y5): an integer lift reducing to rho mod 3
# exists and produces NONZERO integer FN exponents on non-democratic
# invariant entries -> a genuine hierarchy engine is arithmetically open.
q_lift = (0, 2, 4)   # reduces mod 3 to (0, 2, 1) = rho
check("E3 integer lift (0,2,4) reduces to rho mod 3",
      tuple(x % 3 for x in q_lift) == rho)
exps = {(i, j): q_lift[i] + q_lift[j] for (i, j) in inv_support}
check("E4 lift grades the cross-paired invariant entries (exponent 6) "
      "while the democratic entry stays ungraded (exponent 0)",
      exps[(0, 0)] == 0 and exps[(1, 2)] == 6 and exps[(2, 1)] == 6)
eps = 1e-2
check("E5 lifted charges give genuine suppression eps^6 = 1e-12 "
      "(hierarchy engine possible ONLY beyond mod 3)",
      abs(eps ** exps[(1, 2)] - 1e-12) < 1e-24)

# ---------------------------------------------------------------- F
hbar_c_eV_m = 1.9732698e-7  # eV * m
m2_lo, m2_hi = 5.0 / 6.0, 5.0 / 4.0


def lam_um(mu_eV, m2_eff):
    return hbar_c_eV_m / (math.sqrt(m2_eff) * mu_eV) * 1e6


# H36 point (mu_DW = 2.94 meV, c_L = 3/8): excluded band [60.0, 73.6] um
check("F1 H36 point reproduces lambda ~ 60.0 um (m2_eff = 5/4)",
      abs(lam_um(2.94e-3, m2_hi) - 60.0) < 0.5)
check("F2 H36 point reproduces lambda ~ 73.6 um (m2_eff = 5/6)",
      abs(lam_um(2.94e-3, m2_lo) - 73.6) < 0.5)


def mu_floor_meV(boundary_um, m2_eff):
    return hbar_c_eV_m / (math.sqrt(m2_eff) * boundary_um * 1e-6) * 1e3


check("F3 weakest-corner floor ~3.4 meV (boundary 52 um, m2_eff 5/4)",
      abs(mu_floor_meV(52.0, m2_hi) - 3.4) < 0.1)
check("F4 strictest-corner floor ~4.8 meV (boundary 45 um, m2_eff 5/6)",
      abs(mu_floor_meV(45.0, m2_lo) - 4.8) < 0.1)
check("F5 refused H36 point sits BELOW the floor band (falsified, "
      "consistent with keeping mu_DW free)", 2.94 < 3.4)
check("F6 m2_eff window nonempty", m2_lo < m2_hi)

# ---------------------------------------------------------------- G
# The spec's requirements table, (ID, class). Must match the document.
TABLE = [
    ("SA-Y1", "FORCED"), ("SA-Y2", "DECLARATION"), ("SA-Y3", "FIT"),
    ("SA-Y4", "FIT"), ("SA-Y5", "DECLARATION"), ("SA-Y6", "DECLARATION"),
    ("SA-Y7a", "FORCED"), ("SA-Y7b", "FIT"), ("SA-Y8", "DECLARATION"),
    ("SA-G1", "DECLARATION"), ("SA-G2", "FIT"), ("SA-G3", "FIT"),
    ("SA-G4", "FIT"), ("SA-G5", "FIT"), ("SA-G6", "FIT"),
    ("SA-G7", "FIT"), ("SA-G8", "FIT"), ("SA-G9", "FORCED"),
    ("SA-C1", "DECLARATION"), ("SA-C2", "FORCED"),
    ("SA-C3", "DECLARATION"), ("SA-C4", "FORCED"),
    ("SA-U1", "FORCED"), ("SA-U2", "DECLARATION"), ("SA-U3", "FORCED"),
    ("SA-U4", "FORCED"), ("SA-U5", "DECLARATION"),
]
counts = {}
for _id, cls in TABLE:
    counts[cls] = counts.get(cls, 0) + 1
check("G1 27 requirement rows", len(TABLE) == 27)
check("G2 FORCED count = 8", counts.get("FORCED") == 8)
check("G3 DECLARATION count = 9", counts.get("DECLARATION") == 9)
check("G4 FIT count = 10", counts.get("FIT") == 10)
check("G5 IDs unique", len({i for i, _ in TABLE}) == len(TABLE))

# ----------------------------------------------------------------
print()
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s): {FAILURES}")
    raise SystemExit(1)
print(f"ALL checks passed ({len(TABLE)} table rows; "
      "consistency certified at arithmetic level).")
raise SystemExit(0)
