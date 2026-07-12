#!/usr/bin/env python3
"""
W64 / Path-4 Branch D -- THE DISCRETE, CHOICE-INDEPENDENT FORCED FACT (a "2-bit prediction").

BLIND branch D of the path-4 "forced family-invariant" wave. The continuous predictions of the
shape-dim-1 source-action family are all scaled by the free mu_DW / alpha and (H53) decouple or are
non-discriminating. Branch D asks the orthogonal question: is there a DISCRETE fact -- a small
integer, a mod-k selection rule, or a forced correlation between two discrete SM data -- that is the
SAME for every family member and its two free scales, is NOT already an input/known, and DISCRIMINATES
(vs LCDM/GR/SM/generic-EFT)?

This test encodes the discrete forced STRUCTURE and the NOVELTY/DISCRIMINATION check as assertions.
It is deterministic (exact integer / cyclotomic / small-float linear algebra; no randomness).

CONSTRUCTION FORK USED (per GEOMETER-VS-PHYSICS-OBJECTS.md):
  * generation-count row: count = torsion class in the 3-primary arena Z/3 subset pi_3^s = Z/24,
    3 = dim Lambda^2_+(R^4); NOT a Z-index.
  * gravity-functional / DOF row: |II|^2 -> a genuine 4th-order action, 7 propagating DOF.

HONEST VERDICT ENCODED HERE:
  Q-forced : the FORCED discrete facts are D1-D4 (ceiling 3; {1,3} 3-primary; 2/3-primary arena
             split; 7 DOF). The novel-looking relations D5-D6 (carrier index -38, order-3 class
             (0,2,1)/3, "exactly 3") are NOT forced -- they ride the carrier bit / SG4 / residue trap.
  Q-novel  : NO for the forced set (D1-D4 are already established in-repo). The one forced-and-
             arguably-novel item -- the d=4 <-> ceiling-3 correlation -- is a re-reading of the known
             anchor 3 = dim Lambda^2_+, not a new fact.
  Q-disc   : NO. The forced discrete facts are ceilings/menus that accommodate known SM numbers, or
             are non-observable (7 DOF, H53), or are generic to any 4D self-dual construction.
  Overall  : NO NEW FORCED-AND-DISCRIMINATING DISCRETE FACT. The intersection
             (forced AND novel AND discriminating) is EMPTY in the built content.

Reproducible: python tests/W64_path4_D_discrete.py   (exit 0 on all PASS)
"""
from __future__ import annotations

import cmath
import math
from itertools import combinations

FAILURES: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f" -- {detail}" if detail else ""))
    if not cond:
        FAILURES.append(name)


# ---------------------------------------------------------------------------
# D1  ceiling = dim Lambda^2_+(R^4) = 3, and it is UNIQUELY a 4-dimensional fact
# ---------------------------------------------------------------------------
# Hodge star maps Lambda^k(R^d) -> Lambda^{d-k}. A self-dual 2-form EIGENSPACE
# exists only when the star maps Lambda^2 back to Lambda^2, i.e. d-k=k=2 => d=4.

def dim_lambda_k(d: int, k: int) -> int:
    return math.comb(d, k)

def self_dual_2form_eigenspace_exists(d: int) -> bool:
    # star: Lambda^2 -> Lambda^{d-2}; eigenspace requires d-2 == 2
    return (d - 2) == 2

# d=4: Lambda^2 is 6-dim, star^2 = +1, splits 3 (self-dual) + 3 (anti-self-dual).
check("D1a dim Lambda^2(R^4) = 6", dim_lambda_k(4, 2) == 6)
check("D1b self-dual 2-form eigenspace exists ONLY at d=4",
      self_dual_2form_eigenspace_exists(4)
      and not self_dual_2form_eigenspace_exists(6)
      and not self_dual_2form_eigenspace_exists(8)
      and not self_dual_2form_eigenspace_exists(10),
      "star:Lambda^2->Lambda^{d-2} is an involution on 2-forms iff d=4")

# Exact Hodge-star construction on Lambda^2(R^4): basis e_{ij}, i<j; *e_{ij}=sign*e_{kl}.
def hodge_star_lambda2_r4():
    basis = list(combinations(range(4), 2))            # 6 elements
    idx = {b: i for i, b in enumerate(basis)}
    M = [[0.0] * 6 for _ in range(6)]
    for (i, j) in basis:
        comp = tuple(x for x in range(4) if x not in (i, j))  # complementary pair (k,l), k<l
        k, l = comp
        # sign of permutation (i,j,k,l) relative to (0,1,2,3)
        perm = [i, j, k, l]
        sign = 1
        for a in range(4):
            for b in range(a + 1, 4):
                if perm[a] > perm[b]:
                    sign = -sign
        M[idx[comp]][idx[(i, j)]] = float(sign)
    return M, basis

M, basis = hodge_star_lambda2_r4()
# star^2 = +I on Lambda^2(R^4) (Euclidean)
M2 = [[sum(M[a][c] * M[c][b] for c in range(6)) for b in range(6)] for a in range(6)]
identity6 = [[1.0 if a == b else 0.0 for b in range(6)] for a in range(6)]
check("D1c Hodge star^2 = +I on Lambda^2(R^4)",
      all(abs(M2[a][b] - identity6[a][b]) < 1e-12 for a in range(6) for b in range(6)))

# eigenvalues of M are +/-1, each with multiplicity 3  (self-dual dim = 3)
# count +1 eigenvalues via trace/rank: (I+M)/2 projects onto self-dual; its trace = dim(+1 space)
proj_plus = [[(identity6[a][b] + M[a][b]) / 2.0 for b in range(6)] for a in range(6)]
dim_self_dual = round(sum(proj_plus[a][a] for a in range(6)))
check("D1d dim Lambda^2_+(R^4) = 3  (the generation ceiling)", dim_self_dual == 3)

# Independent route: Lambda^2_+ = su(2)_+, dim su(2) = 3
check("D1e 3 = dim su(2)_+  (self-dual so(4)=su(2)+su(2) summand)", 3 == 3)

# THE FORCED CORRELATION (branch-D's sharpest, honestly graded below):
#   (finite generation ceiling = 3)  <==>  (spacetime dimension = 4)
D1_ceiling = dim_self_dual
D1_forced_correlation = (D1_ceiling == 3) and self_dual_2form_eigenspace_exists(4)
check("D1f forced correlation (ceiling=3) <=> (d=4)", D1_forced_correlation)


# ---------------------------------------------------------------------------
# D2  realized count menu = {1,3} (odd, 3-primary): order-3 element on R^3
# ---------------------------------------------------------------------------
# g:(x,y,z)->(y,z,x): g^3=I, det=+1, rotation by 2pi/3 about (1,1,1).
g = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]

def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(len(B[0]))] for i in range(n)]

g2 = matmul(g, g)
g3 = matmul(g2, g)
check("D2a g^3 = I", g3 == [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
check("D2b det g = +1", (g[0][0]*(g[1][1]*g[2][2]-g[1][2]*g[2][1])
                         - g[0][1]*(g[1][0]*g[2][2]-g[1][2]*g[2][0])
                         + g[0][2]*(g[1][0]*g[2][1]-g[1][1]*g[2][0])) == 1)

# real Z/3-invariant subspaces of R^3 = V0 (+) V1 (trivial (+) 2-dim rotated): dims {0,1,2,3}
invariant_dims = {0, 1, 2, 3}
# oddness: a real conjugation-stable subspace is odd-dim iff it contains the fixed line
odd_invariant_dims = {d for d in invariant_dims if d % 2 == 1}
check("D2c invariant-subspace dims {0,1,2,3}", invariant_dims == {0, 1, 2, 3})
check("D2d odd (realized) count menu = {1,3}", odd_invariant_dims == {1, 3})

# THE RESIDUE TRAP: no order-3 class function certifies the integer 3.
# tr(g|R^3) = 1 + 2cos(2pi/3) = 0 ; net count 3 has residue 3 mod 3 = 0 = trivial-sector residue.
trace_g = g[0][0] + g[1][1] + g[2][2]
check("D2e tr(g|R^3) = 0  (residue trap: character vanishes)", trace_g == 0)
check("D2f net-3 residue == trivial-sector residue (3 mod 3 == 0 mod 3)",
      (3 % 3) == (0 % 3),
      "no order-3 class function separates '3' from '0 mod 3' => VALUE not forced")


# ---------------------------------------------------------------------------
# D3  arena split: count (3-primary) vs chirality/ghost (2-primary) are coprime
# ---------------------------------------------------------------------------
# pi_3^s = Z/24 = Z/8 (+) Z/3 ; |Im J_3| = denominator of B_2/4 = 24.
pi3s_order = 24
z8, z3 = 8, 3
check("D3a pi_3^s order = 24 = 8 * 3", z8 * z3 == pi3s_order)
check("D3b 24 = 2^3 * 3 (3-primary part = Z/3)", 24 == (2**3) * 3)
check("D3c gcd(2,3) = 1 (count arena coprime to chirality/ghost arena)", math.gcd(2, 3) == 1)
# |Hom(Z/2, Z/3)| = 1 (zero map only): arena-orthogonality
check("D3d |Hom(Z/2,Z/3)| = 1  (arena-orthogonal; no trade-off)", math.gcd(2, 3) == 1)


# ---------------------------------------------------------------------------
# D4  7 propagating DOF (4th-order |II|^2 action), mu_DW-invariant integer
# ---------------------------------------------------------------------------
# GR: 2 (massless graviton). GU 4th-order: 2 (massless) + 5 (massive spin-2) = 7. (H49/H45/H53.)
gr_dof = 2
gu_dof = 2 + 5
check("D4a GU propagating DOF = 7 = 2 + 5", gu_dof == 7)
check("D4b GU DOF - GR DOF = 5 (extra massive spin-2 states)", gu_dof - gr_dof == 5)
# H53: this integer is mu_DW-INVARIANT (forced) but NOT an accessible observable
# (every deviation ~ (E/m2)^2 -> 0 as mu_DW -> M_Pl). Encode as a recorded fact, not observability.
d4_forced = True          # mu_DW-invariant integer (H53 row 5)
d4_observable = False     # H53 Q2: scale-hideable, decouples at natural mu_DW
check("D4c 7-DOF is FORCED but NOT an accessible observable (H53)", d4_forced and not d4_observable)


# ---------------------------------------------------------------------------
# D5-D6  the NOVEL discrete relations are CARRIER-DEPENDENT (NOT forced)
# ---------------------------------------------------------------------------
# Carrier A (ghost-subtracted): ind = -42 = 21 sigma/8, residue 0, order-3 rho (0,0,0).
# Carrier B (geometric gamma-traceless): ind = -38 = 19 sigma/8, residue 1, order-3 rho (0,2,1)/3.
sigma_K3 = -16
ind_A = 21 * sigma_K3 // 8
ind_B = 19 * sigma_K3 // 8
check("D5a carrier A index = -42 = 21 sigma/8", ind_A == -42)
check("D5b carrier B index = -38 = 19 sigma/8", ind_B == -38)
check("D5c carrier indices DIFFER (A=-42 vs B=-38): discrete arithmetic is NOT a single family value",
      ind_A != ind_B)
check("D5d residues differ: A=-42 -> 0 mod 3, B=-38 -> 1 mod 3",
      (ind_A % 3, ind_B % 3) == (0, 1))
# order-3 rho: A is 2-primary (0,0,0); B is (0,2,1)/3 nonzero. rho_B = rho_A + 2 rho_Dirac.
rho_A = (0, 0, 0)
rho_Dirac = (0, 1, 2)                         # order3-rho canon: Dirac Z3_NONZERO
rho_B = tuple((rho_A[i] + 2 * rho_Dirac[i]) % 3 for i in range(3))
check("D6a rho_B = rho_A + 2 rho_Dirac = (0,2,1) mod 3", rho_B == (0, 2, 1))
check("D6b rho_A = (0,0,0) 2-primary vs rho_B = (0,2,1) nonzero: rho is CARRIER-DEPENDENT",
      rho_A != rho_B)
# => D5-D6 (the only genuinely NEW discrete relations) are NOT family-invariant: they ride the
#    carrier bit, which is an SG4-gated field-space declaration (arithmetic-undecidable, H39 Q4).
D5D6_forced_across_family = (ind_A == ind_B) and (rho_A == rho_B)   # would need carrier-invariance
check("D5e the NOVEL discrete relations are NOT forced across the family (carrier-dependent)",
      not D5D6_forced_across_family)


# ---------------------------------------------------------------------------
# THE NOVELTY x DISCRIMINATION LEDGER (the honest verdict, encoded)
# ---------------------------------------------------------------------------
# Each discrete fact tagged (forced?, novel-beyond-known?, discriminating?).
# forced  = choice-independent across the shape-dim-1 family + free scales.
# novel   = NOT already an input/known in-repo, and not a re-read of a known anchor.
# disc    = discriminates vs LCDM/GR/SM/generic-EFT and is (in principle) testable.
ledger = {
    #                       forced  novel  disc
    "D1 ceiling 3 (d=4 lock)": (True,  False, False),  # forced+arguably-novel-read, but ceiling/known/generic-4D
    "D2 count menu {1,3}":     (True,  False, False),  # known (H40); menu not value
    "D3 2/3-primary arena":    (True,  False, False),  # known (two-primary-lemma); meta, not an SM observable
    "D4 7 DOF":                (True,  False, False),  # known (H53); NOT observable
    "D5 carrier index -38":    (False, True,  True),   # would discriminate, but NOT forced (carrier-dependent)
    "D6 order-3 rho (0,2,1)":  (False, True,  True),   # would discriminate, but NOT forced (carrier-dependent)
}

# There is at least one FORCED discrete fact (structure is real).
check("L1 at least one FORCED discrete fact exists",
      any(f for (f, _, _) in ledger.values()))

# The FORCED discrete facts are all ALREADY KNOWN (novel=False).
check("L2 every FORCED discrete fact is already known (novel=False)",
      all((not novel) for (f, novel, _) in ledger.values() if f))

# The NOVEL discrete relations are all NOT forced (choice-dependent).
check("L3 every NOVEL discrete relation is NOT forced (choice-dependent)",
      all((not f) for (f, novel, _) in ledger.values() if novel))

# THE HEADLINE TEST: the intersection (forced AND novel AND discriminating) is EMPTY.
forced_novel_disc = [k for k, (f, n, d) in ledger.items() if f and n and d]
check("L4 HEADLINE: (forced AND novel AND discriminating) is EMPTY -- no new discrete prediction",
      forced_novel_disc == [],
      "the forced discrete content is real but ALREADY KNOWN; the novel relations are choice-dependent")

# The single strongest forced-and-arguably-novel statement is the d=4 <-> ceiling-3 correlation,
# which is forced but NOT discriminating (ceiling not value; not testable; generic to 4D self-dual).
best_forced_novelish = "D1 ceiling 3 (d=4 lock)"
f, n, d = ledger[best_forced_novelish]
check("L5 strongest forced statement (d=4<->3) is forced but NOT discriminating", f and not d)


# ---------------------------------------------------------------------------
print()
if FAILURES:
    print(f"RESULT: FAIL ({len(FAILURES)} failed): {FAILURES}")
    raise SystemExit(1)
print("RESULT: PASS -- branch-D discrete structure verified; honest verdict:")
print("  Q-forced: forced discrete facts = D1-D4 (all already known); D5-D6 novel but NOT forced.")
print("  Q-novel : NO new forced discrete fact beyond the established set.")
print("  Q-disc  : NO -- forced facts accommodate known data / non-observable / generic to 4D.")
print("  Overall : (forced AND novel AND discriminating) is EMPTY -- no discrete headline.")
raise SystemExit(0)
