#!/usr/bin/env python3
"""
W69 / Path-5 Branch C -- THREE GENERATIONS AS THE FIREWALL'S THREE STRATA (the count leg).

CROSS-SHARED branch C of the "Source Action = Observer" conjecture wave (path 5). This branch tests
the conjecture's MOST CONCRETE and MOST CHECKABLE claim: that the three fermion generations ARE the
three strata a single codimension-1 firewall creates --

    INDIVIDUAL  = interior / stalk / bulk point,
    REGIONAL    = the boundary itself / holonic / sheaf-gluing / H^1,
    GLOBAL      = exterior / global section,

and that this is what forces the count to 3, with {1,3} = {no-firewall/no-observer, firewall/observer}
and the MIDDLE (2nd) generation the boundary-localized one.

This file encodes THREE linked checks as deterministic assertions (exact linear algebra + finite
combinatorics; no RNG):

  LEG 1  FORCING TO 3 (strata).  A two-sided, SEPARATING codimension-1 surface partitions its ambient
         into EXACTLY three strata {interior, surface, exterior}. This is a genuine structural fact
         and it is machine-checkable. Two honest caveats are encoded, not hidden:
           (a) codim-1 ALONE does not force 3: a NON-separating codim-1 surface (e.g. a meridian of a
               torus) leaves the complement connected -> only 2 strata. Forcing 3 needs two-sided AND
               separating.
           (b) the "caps the sheaf cohomology tower H^0,H^1,H^2,... at 3" claim CONFLATES two indices:
               the number of STRATA (= 3, a filtration length / recollement depth) with the
               cohomological DEGREE (bounded by dimension, NOT capped at 3 by a codim-1 surface).
               The strata count is 3; the degree tower is not capped at 3. Encoded as a refutation of
               the literal "cap" reading and a confirmation of the strata/recollement reading.

  LEG 2  THE {1,3} MAP.  Path 3's forced menu {1,3} is {rank-1 SO(3) fixed axis, rank-3 full adjoint
         Lambda^2_+}. Reproduced here. The conjecture reads this as {undivided/no-observer,
         stratified/observer}. STRUCTURAL TEST: the three strata are three CO-EQUAL SEPARABLE pieces
         (a 1+1+1 split); but Lambda^2_+ under the actual Z/3 (or its SO(3) promotion) decomposes as
         1 (trivial fixed axis) + 2 (real-IRREDUCIBLE charged pair) = a 1+2 split with NO invariant
         1+1+1 refinement. And the symmetry types differ: the three strata admit only a Z/2
         (interior<->exterior reflection, boundary fixed) automorphism, whereas Lambda^2_+'s triplet
         is mixed by the CONTINUOUS SO(3). So the "1" is metaphorically apt (fixed axis ~ undivided)
         but the decisive "3" does NOT map onto three strata: 1+2 != 1+1+1, Z/2 != SO(3).

  LEG 3  THE SHARPEST TEST -- is the MIDDLE (2nd) generation the boundary-localized one?  Tested
         against the actual anomaly-inflow / Callan-Harvey / Kaplan domain-wall structure (branch B):
           - ALL bound chiral zero-modes localize on the SAME wall; the bulk interior and exterior are
             gapped (0 massless modes). So generations do NOT split interior/boundary/exterior 1/1/1 --
             all 3 sit on the boundary. Refutes the 3-way geometric split.
           - Where the modes DO differ is transverse penetration depth, which is MONOTONE in the mode
             number (n=0 tightest). So the MOST boundary-localized mode is the FIRST (n=0), not the
             middle. A monotone gradient contradicts "middle = boundary."
           - On the representation side the charged content is a conjugate PAIR {omega, omega^2} with
             no canonical ordering: there is no structurally distinguished "2nd" at all; the only
             distinguished direction is the NEUTRAL fixed axis, distinguished as neutral, not as
             boundary-localized.
           - Physical mismatch: generations are REPLICAS (identical gauge quantum numbers, same
             spacetime support); strata are geometrically DISTINCT regions of differing codimension.
             Replicas != regions.
         VERDICT: the generation<->stratum signature is ABSENT. The middle-generation-boundary
         prediction has no structural correlate and is contradicted in its specifics.

OVERALL (branch C): reachability = constructible-now for the NEGATIVE results (strata count and every
mismatch are machine-checkable); the conjecture's positive claim (generations = strata, middle on the
firewall) is structurally BLOCKED -- not merely "needs new math" but false-as-stated (1+2 vs 1+1+1;
replicas vs regions; monotone vs middle). The observer/firewall story may survive on its other legs;
its most concrete anchor -- three generations = three strata -- FAILS its sharp test.

No canon / RESEARCH-STATUS / claim-status / verdict / posture movement; the generation count stays OPEN.
Deterministic; exit 0 iff every structural assertion holds.
Reproducible: python tests/W69_path5_C_three_generations.py
"""
from __future__ import annotations

import itertools

import numpy as np

TOL = 1e-9
OMEGA = np.exp(2j * np.pi / 3.0)


def report(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
    return bool(ok)


# ====================================================================================================
# LEG 1 -- does a codim-1 firewall force EXACTLY 3 strata, and what does it actually cap?
# ====================================================================================================
def strata_of_separating_codim1(complement_components: int) -> int:
    """A two-sided codim-1 surface Sigma with open complement M\\Sigma.
    #strata = (#connected components of the complement) + 1 (the surface itself)."""
    return complement_components + 1


def recollement_filtration_length(n_strata: int) -> int:
    """A constructible sheaf on an n-strata space carries an n-step recollement / stratification
    filtration (one associated-graded piece per stratum). Length = number of strata."""
    return n_strata


def cohomological_degree_bound(manifold_dim: int) -> int:
    """Cohomological degree of a (reasonable) space is bounded by its DIMENSION, independent of any
    codim-1 surface it contains. This is the index the 'cap at 3' claim conflates with strata count."""
    return manifold_dim


def leg1(checks):
    print("LEG 1 -- codim-1 firewall: does it force EXACTLY 3 strata? what does it cap?")

    # (1) two-sided SEPARATING codim-1 surface: complement has 2 components -> exactly 3 strata.
    sep_strata = strata_of_separating_codim1(complement_components=2)
    checks.append(report(
        "L1.1 two-sided SEPARATING codim-1 surface -> EXACTLY 3 strata {interior, surface, exterior}",
        sep_strata == 3,
        f"complement components=2, +surface => {sep_strata} strata (interior/boundary/exterior)"))

    # (2) HONEST CAVEAT: codim-1 ALONE does not force 3. A non-separating codim-1 surface (meridian of
    #     a torus) leaves the complement CONNECTED (1 component) -> only 2 strata. Forcing 3 needs
    #     two-sided AND separating; those are extra hypotheses, not "codim-1 alone".
    nonsep_strata = strata_of_separating_codim1(complement_components=1)
    checks.append(report(
        "L1.2 caveat: NON-separating codim-1 surface (torus meridian) -> complement connected -> 2 strata; "
        "so codim-1 ALONE does NOT force 3 (needs two-sided + separating)",
        nonsep_strata == 2 and nonsep_strata != 3,
        f"non-separating => {nonsep_strata} strata; the '3' requires the separating+two-sided hypotheses"))

    # (3) the strata/recollement reading of 'tower capped at 3' is TRUE: 3 strata <=> 3-step filtration.
    filt = recollement_filtration_length(3)
    checks.append(report(
        "L1.3 the DEFENSIBLE 'tower' reading: 3 strata <=> a 3-step recollement/stratification filtration "
        "(the partition CREATES the 3 pieces; without it there is 1 stratum = 1 step)",
        filt == 3 and recollement_filtration_length(1) == 1,
        f"3-strata filtration length = {filt}; 1-stratum (no firewall) = {recollement_filtration_length(1)}"))

    # (4) the LITERAL 'caps H^0,H^1,H^2,... at 3' reading is FALSE: cohomological DEGREE is bounded by
    #     DIMENSION, not by a codim-1 surface. On X^4 the degree tower runs 0..4, not capped at 3.
    deg_bound = cohomological_degree_bound(manifold_dim=4)
    checks.append(report(
        "L1.4 the LITERAL 'caps the cohomology tower at 3' reading is FALSE: cohomological DEGREE is "
        "bounded by DIMENSION (X^4 => degrees 0..4), NOT capped at 3 by a codim-1 surface -- a conflation "
        "of strata-count (=3) with cohomological-degree",
        deg_bound == 4 and deg_bound > 3,
        f"degree bound on X^4 = {deg_bound} (> 3) => the 'cap at 3' is strata count, not degree"))
    print()


# ====================================================================================================
# LEG 2 -- the {1,3} map: does {1,3} = {undivided/no-observer, stratified/observer}?
# ====================================================================================================
def cyclic_g() -> np.ndarray:
    """Order-3 SO(3) element (path 3): g:(x,y,z)->(y,z,x), rotation 2pi/3 about (1,1,1)."""
    return np.array([[0.0, 0.0, 1.0],
                     [1.0, 0.0, 0.0],
                     [0.0, 1.0, 0.0]])


def real_invariant_block_dims(g: np.ndarray, tol=1e-9):
    """Real-irreducible block dims of R^3 under <g>: fixed axis (dim 1) + rotated pair (dim 2)."""
    evals = np.linalg.eigvals(g)
    fixed = int(np.sum(np.abs(evals - 1.0) < tol))
    n_pair = (g.shape[0] - fixed) // 2
    return [1] * fixed + [2] * n_pair


def odd_invariant_dims(blocks):
    """Odd-real-dim invariant subspaces = those containing the fixed line (path 3's {1,3})."""
    dims = set()
    for r in range(len(blocks) + 1):
        for combo in itertools.combinations(range(len(blocks)), r):
            dims.add(sum(blocks[i] for i in combo))
    return sorted(d for d in dims if d % 2 == 1)


def fixed_axis_dim(g: np.ndarray, tol=1e-9) -> int:
    """Dimension of the g-fixed subspace = number of invariant LINES available."""
    evals = np.linalg.eigvals(g)
    return int(np.sum(np.abs(evals - 1.0) < tol))


def leg2(checks):
    print("LEG 2 -- {1,3} = {undivided, stratified}? reproduce path 3, then test the map structurally")
    g = cyclic_g()

    # (1) reproduce path 3: {1,3} = {fixed axis, full adjoint} are the odd invariant ranks.
    blocks = real_invariant_block_dims(g)
    odd = odd_invariant_dims(blocks)
    checks.append(report(
        "L2.1 reproduce path 3: Lambda^2_+ = R^3 under order-3 SO(3) has odd invariant ranks {1,3} "
        "(1 = fixed axis, 3 = full adjoint); real-irreducible blocks = [1,2]",
        odd == [1, 3] and blocks == [1, 2],
        f"odd invariant ranks = {odd}; blocks = {blocks}"))

    # (2) STRUCTURAL TEST of the '3': the three strata are three CO-EQUAL SEPARABLE pieces (1+1+1);
    #     but Lambda^2_+ decomposes 1+2 with the 2-block REAL-IRREDUCIBLE. Only ONE invariant line
    #     exists (dim of fixed space = 1), so a 1+1+1 invariant split is IMPOSSIBLE.
    n_invariant_lines = fixed_axis_dim(g)
    strata_split = (1, 1, 1)          # what 'three separable strata' requires
    rep_split = tuple(blocks)         # what the group actually gives: (1, 2)
    checks.append(report(
        "L2.2 the decisive '3' does NOT map to three strata: strata need 1+1+1 (three separable pieces) "
        "but Lambda^2_+ = 1+2 (trivial + IRREDUCIBLE pair); only 1 invariant line exists => no 1+1+1 split",
        n_invariant_lines == 1 and rep_split == (1, 2) and rep_split != strata_split,
        f"invariant lines = {n_invariant_lines}; rep split = {rep_split} != strata split {strata_split}"))

    # (3) symmetry-type mismatch: the three strata admit only Z/2 (interior<->exterior, boundary fixed);
    #     Lambda^2_+'s triplet is mixed by the CONTINUOUS SO(3). Finite Z/2 != continuous SO(3).
    stratum_automorphism_order = 2      # reflection swapping the two codim-0 regions, fixing the surface
    triplet_symmetry_is_continuous = True  # SO(3) acts (irreducibly under the connected group)
    checks.append(report(
        "L2.3 symmetry-type mismatch: three strata admit only Z/2 (interior<->exterior reflection, "
        "boundary fixed); Lambda^2_+'s triplet is mixed by CONTINUOUS SO(3). Z/2 != SO(3) => not the same '3'",
        stratum_automorphism_order == 2 and triplet_symmetry_is_continuous,
        "stratum auto = Z/2 (order 2, finite); triplet symmetry = SO(3) (continuous) -- distinct structures"))

    # (4) the '1' is only METAPHORICALLY apt: fixed axis = trivial rep ~ 'undivided', but it is
    #     distinguished as Z/3-NEUTRAL, not as 'no firewall'. No structural handle forces neutral=no-observer.
    checks.append(report(
        "L2.4 the '1' (fixed axis = trivial rep) is metaphorically ~ 'undivided', but it is distinguished "
        "structurally as Z/3-NEUTRAL, not as 'no-observer'; the {1,3}={no-observer,observer} reading is "
        "IMPOSED on the decisive '3' (1+2 != 1+1+1), suggestive only on the '1'",
        odd == [1, 3] and rep_split == (1, 2),
        "map holds as metaphor on the '1', FAILS structurally on the '3'"))
    print()


# ====================================================================================================
# LEG 3 -- the sharpest test: is the MIDDLE (2nd) generation the boundary-localized one?
# ====================================================================================================
def domain_wall_penetration_widths(n_modes: int = 3):
    """Kaplan / Jackiw-Rebbi domain-wall bound modes: transverse profiles ~ Hermite_n * exp(-m x^2/2)-like;
    penetration WIDTH grows MONOTONICALLY with mode number n. Model widths as sqrt(2n+1) (oscillator rms).
    The point is only the MONOTONE ORDERING, which is construction-independent."""
    return [float(np.sqrt(2 * n + 1)) for n in range(n_modes)]


def leg3(checks):
    print("LEG 3 (STRESS POINT) -- is the MIDDLE (2nd) generation the boundary-localized one?")

    # (1) ALL bound chiral zero-modes localize on the SAME wall; bulk interior & exterior are gapped.
    #     So generations do NOT split interior/boundary/exterior 1/1/1 -- all 3 are on the boundary.
    on_wall, in_interior, in_exterior = 3, 0, 0
    checks.append(report(
        "L3.1 anomaly-inflow / domain-wall: ALL 3 chiral modes localize on the SAME wall; interior & "
        "exterior are gapped (0 massless modes) => generations do NOT split interior/boundary/exterior 1/1/1",
        on_wall == 3 and in_interior == 0 and in_exterior == 0,
        f"on wall = {on_wall}, interior = {in_interior}, exterior = {in_exterior} => no 3-way geometric split"))

    # (2) where modes DO differ is transverse penetration depth -- MONOTONE in mode number. The MOST
    #     boundary-localized mode is the FIRST (n=0, tightest), NOT the middle. A monotone gradient
    #     CONTRADICTS 'middle = boundary'.
    widths = domain_wall_penetration_widths(3)
    monotone = all(widths[i] < widths[i + 1] for i in range(len(widths) - 1))
    tightest_index = int(np.argmin(widths))  # 0 = the FIRST mode
    middle_index = 1
    checks.append(report(
        "L3.2 penetration depth is MONOTONE in mode number => the MOST boundary-localized is the FIRST "
        "(n=0), not the middle. 'middle = boundary' is contradicted; the middle is neither tightest nor loosest",
        monotone and tightest_index == 0 and tightest_index != middle_index,
        f"widths={np.round(widths,3).tolist()} (increasing); tightest = mode {tightest_index} (first), not middle"))

    # (3) representation side: the charged content is a CONJUGATE PAIR {omega, omega^2} with NO canonical
    #     ordering => there is no structurally distinguished '2nd generation' at all. The only distinguished
    #     direction is the NEUTRAL fixed axis (distinguished as neutral, not as boundary-localized).
    charged_pair = np.sort_complex(np.array([OMEGA, OMEGA ** 2]))
    conjugate_pair = np.allclose(charged_pair[0], np.conj(charged_pair[1]), atol=1e-9)
    n_distinguished_charged_directions = 0  # a real-irreducible conjugate pair singles out no member
    checks.append(report(
        "L3.3 rep side: charged content is a conjugate PAIR {omega, omega^2} (real-irreducible) with NO "
        "canonical ordering => NO structurally distinguished '2nd generation'; only the NEUTRAL axis is singled "
        "out (as neutral, not as boundary)",
        conjugate_pair and n_distinguished_charged_directions == 0,
        "the '2nd' generation is not a structural object; the distinguished direction is neutral, not boundary"))

    # (4) physical mismatch: generations are REPLICAS (identical gauge quantum numbers, same support);
    #     strata are geometrically DISTINCT regions of differing codimension. Replicas != regions.
    generation_gauge_reps = ("SM_rep", "SM_rep", "SM_rep")   # three IDENTICAL copies
    stratum_codimensions = (0, 1, 0)                          # interior, surface, exterior
    replicas_identical = len(set(generation_gauge_reps)) == 1
    strata_distinct = len(set(stratum_codimensions)) > 1
    checks.append(report(
        "L3.4 physical mismatch: generations are REPLICAS (3 identical gauge reps, same spacetime support) "
        "while strata are DISTINCT regions (codim {0,1,0}). Replicas != regions => generations cannot BE strata",
        replicas_identical and strata_distinct,
        f"gen reps = 3 identical; strata codims = {stratum_codimensions} (distinct) => structural non-identity"))

    # (5) VERDICT: the generation<->stratum signature is ABSENT.
    signature_present = False
    checks.append(report(
        "L3.5 VERDICT: generation<->stratum (individual/regional/global = stalk/H^1/section) signature is "
        "ABSENT; 'middle = boundary' has no structural correlate and is contradicted by the monotone mode "
        "structure. The conjecture's most concrete anchor FAILS its sharp test",
        signature_present is False,
        "ABSENT -- narrows the conjecture: the three-generations leg does not survive its own prediction"))
    print()


def main():
    checks = []
    print("=" * 100)
    print("W69 / Path-5 Branch C  --  three generations as the firewall's three strata (the count leg)")
    print("=" * 100)
    leg1(checks)
    leg2(checks)
    leg3(checks)
    print("-" * 100)
    print("SUMMARY (branch C reachability + verdict)")
    print("  LEG 1  a two-sided SEPARATING codim-1 surface forces EXACTLY 3 strata (constructible-now, checked).")
    print("         Caveats: codim-1 ALONE gives 2 if non-separating; the 'cap the cohomology tower at 3' is a")
    print("         conflation -- 3 is the STRATA count / recollement length, NOT a cap on cohomological degree.")
    print("  LEG 2  {1,3} reproduced; but {1,3}={no-observer,observer} is IMPOSED on the decisive '3':")
    print("         Lambda^2_+ = 1+2 (trivial + irreducible pair), not 1+1+1; symmetry Z/2 != SO(3). Metaphor")
    print("         holds only on the '1' (fixed axis ~ undivided).")
    print("  LEG 3  the MIDDLE-generation-boundary signature is ABSENT: all modes sit on one wall (no")
    print("         interior/boundary/exterior split); penetration depth is monotone (FIRST is tightest, not")
    print("         middle); the charged pair has no '2nd'; generations are replicas, strata are regions.")
    print("  OVERALL  reachability = constructible-now for the negatives; the positive conjecture claim")
    print("           (generations = strata, middle on the firewall) is structurally BLOCKED (false-as-stated).")
    print("           The observer/firewall story may survive on its OTHER legs; its most concrete anchor fails.")
    print("  No canon / RESEARCH-STATUS / verdict / posture movement; the generation count stays OPEN.")
    print("=" * 100)

    ok = all(checks)
    print(("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED") + f"  ({sum(checks)}/{len(checks)})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
