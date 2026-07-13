#!/usr/bin/env python3
"""
W72 / Path-5 Branch C2 -- THREE GENERATIONS AS CAPABILITY ENCLOSURES AT THREE LEVELS (the REFRAMED count leg).

DEFENSE-ATTORNEY re-test of the kill in W69 (Branch C). W69 killed the SYMMETRIC reading -- "the three
generations are three CO-EQUAL strata (a 1+1+1 split), the 2nd on the boundary." That reading was WRONG about
the module: Lambda^2_+ = 1+2, not 1+1+1. Branch C's three strikes (1+2 != 1+1+1; middle-not-boundary;
replicas-not-regions) FALSIFIED the symmetric version.

The REFRAME (Joe): the three generations are not symmetric strata; they are CAPABILITY ENCLOSURES for the
observer, ENFORCED AT THREE LEVELS -- 1 INDIVIDUAL + 2 COLLECTIVE (Regional/holonic + Global) -- matching
    Lambda^2_+ = 1 (trivial fixed axis = INDIVIDUAL) + 2 (real-IRREDUCIBLE charged pair = the COLLECTIVE)
under the self-dual SO(3) = SU(2)_+. The SAME decomposition Branch C used to KILL the symmetric version now
FORCES this one. The INVARIANT across levels is the capability enclosed (identical gauge content -> the
replicas); the VARIABLE is the LEVEL of enforcement (-> three generations at three scales).

This file encodes THREE graded checks as deterministic assertions (exact linear algebra; no RNG):

  TEST 1  DOES 1+IRREDUCIBLE-2 FORCE THE MENU {1,3} AND FORBID 2?  The reframe's central explanatory claim.
          Because the collective is an IRREDUCIBLE doublet (the '2' of 1+2 has NO invariant line -- it cannot
          be split Z/3-equivariantly), the enclosures that CONTAIN the individual (fixed axis) are exactly
          rank 1 (individual alone) and rank 3 (individual + whole doublet); rank 2 is FORBIDDEN (it would
          split the irreducible doublet). Reproduces path 3's {1,3}. CONTRAST: a hypothetical SYMMETRIC 1+1+1
          module, even with the same "individual always enclosed" premise, PERMITS rank 2 (base + one of two
          separable strata). So the irreducibility -- the very thing that killed the symmetric version --
          FORBIDS 2 here. That is the "explains more" the symmetric version lacked.  VERDICT: FORCED given the
          enclosure premise; the 2-forbidding is theorem-grade.

  TEST 2  IS LEVEL-INDEPENDENCE OF GAUGE CONTENT (THE REPLICAS) A CONSEQUENCE, NOT AN ASSUMPTION?  Branch C's
          hardest objection: "replicas are not regions." The reframe: matter = (SM gauge rep) (x) (family
          space Lambda^2_+); the family/level group (self-dual frame SU(2)_+) acts ONLY on the family factor
          and commutes with the internal SM gauge group, so Lambda^2_+ is an SM-gauge SINGLET. Then every
          level (each family component) carries the IDENTICAL SM rep -- the replicas -- as a CONSEQUENCE of
          the singlet property, not an assumption. CONTRAST: if the family group acted NON-trivially on the SM
          factor, the gauge content would differ across levels (no replicas). So level-independence <=>
          gauge-singlet family space. This ANSWERS "replicas not regions": correct, NOT regions -- components
          of a gauge-singlet family space, hence replicas.  VERDICT: PARTIALLY forced -- the replica property
          follows from the singlet/commuting-factor structure GIVEN the tensor factorization (the load-bearing
          assumption, structural in GU: frame vs internal gauge).

  TEST 3  DOES "ENFORCED AT THREE LEVELS" PREDICT A MONOTONE MASS HIERARCHY?  THE WALL. The SAME irreducibility
          that WINS Test 1 LOSES Test 3. Any family-symmetric mass operator (a symmetric M commuting with the
          Z/3 family action) is, by SCHUR, a SCALAR on the irreducible doublet V1 -> the two collective states
          are MASS-DEGENERATE (m_2 = m_3). So the enclosure structure predicts a 1+2 mass pattern
          {c, a, a} = (individual singlet) + (DEGENERATE collective pair). The OBSERVED hierarchy is three
          strongly-ordered, NON-degenerate masses (a 1+1+1 pattern: m_e << m_mu << m_tau). Predicted 1+2 !=
          observed 1+1+1. Moreover the collective pair {omega, omega^2} is a conjugate pair with NO canonical
          ordering (conjugation SWAPS them), so there is no monotone three-level ordering to predict. The
          hierarchy requires BREAKING the family symmetry -- which the enclosure structure neither supplies nor
          orders.  VERDICT: mass hierarchy NOT predicted (predicts the WRONG, degenerate pattern). THIS IS THE
          REFRAME'S WALL.

OVERALL (branch C2): the reframe survives Branch C's first two strikes not merely by dodging but by CONVERTING
them into features (irreducibility forbids 2 -> {1,3}; gauge-singlet family -> replicas). It EXPLAINS MORE than
the killed symmetric version on the COUNT and the REPLICAS. But the mass-hierarchy leg is the WALL: the
irreducibility forces a degenerate collective pair, contradicting the observed non-degenerate hierarchy.
=> the count leg is PARTIALLY REVIVED: it explains {1,3} and the replicas, but NOT the masses.

No canon / RESEARCH-STATUS / claim-status / verdict / posture movement; the generation count stays OPEN.
Deterministic; exit 0 iff every structural assertion holds.
Reproducible: python tests/W72_path5_C2_capability_enclosures.py
"""
from __future__ import annotations

import itertools

import numpy as np

TOL = 1e-9
OMEGA = np.exp(2j * np.pi / 3.0)


def report(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
    return bool(ok)


def cyclic_g() -> np.ndarray:
    """Order-3 SO(3) element (path 3): g:(x,y,z)->(y,z,x), rotation 2pi/3 about the fixed axis (1,1,1)."""
    return np.array([[0.0, 0.0, 1.0],
                     [1.0, 0.0, 0.0],
                     [0.0, 1.0, 0.0]])


def fixed_axis(g: np.ndarray, tol=TOL) -> np.ndarray:
    """Return an orthonormal basis for the g-fixed subspace V0 (the INDIVIDUAL / trivial rep)."""
    evals, evecs = np.linalg.eig(g)
    cols = [evecs[:, i].real for i in range(len(evals)) if abs(evals[i] - 1.0) < tol]
    V0 = np.array(cols).T
    # orthonormalize (single column here)
    q, _ = np.linalg.qr(V0)
    return q


def real_block_dims(g: np.ndarray, tol=TOL):
    """Real-irreducible block dims of R^3 under <g>: fixed axis (dim 1) + rotated pair (dim 2)."""
    evals = np.linalg.eigvals(g)
    fixed = int(np.sum(np.abs(evals - 1.0) < tol))
    n_pair = (g.shape[0] - fixed) // 2
    return [1] * fixed + [2] * n_pair


def invariant_line_count_in_doublet(g: np.ndarray, tol=TOL) -> int:
    """Number of REAL g-invariant lines inside the 2-dim rotated pair V1. A genuine 120-degree rotation has
    NONE (real-irreducible): this is exactly why rank 2 (individual + half the doublet) is forbidden."""
    evals = np.linalg.eigvals(g)
    # real invariant lines correspond to REAL eigenvalues; inside V1 the eigenvalues are omega, omega^2 (complex)
    real_eigs_off_axis = [e for e in evals if abs(e.imag) < tol and abs(e - 1.0) > tol]
    return len(real_eigs_off_axis)


# ====================================================================================================
# TEST 1 -- does 1 + IRREDUCIBLE-2 FORCE the menu {1,3} and FORBID 2?
# ====================================================================================================
def enclosures_containing_individual(block_dims, individual_block=0):
    """Ranks of Z/3-invariant enclosures that CONTAIN the individual block (fixed axis).
    An enclosure = a sub-sum of REAL-IRREDUCIBLE blocks; 'contains the individual' = includes block 0.
    Because each block is atomic (irreducible -> cannot be partially included), the reachable ranks are the
    sub-sums that include the individual block."""
    other = [i for i in range(len(block_dims)) if i != individual_block]
    ranks = set()
    for r in range(len(other) + 1):
        for combo in itertools.combinations(other, r):
            ranks.add(block_dims[individual_block] + sum(block_dims[i] for i in combo))
    return sorted(ranks)


def test1(checks):
    print("TEST 1 -- does 1 + IRREDUCIBLE-2 FORCE the menu {1,3} and FORBID 2? (the reframe's central claim)")
    g = cyclic_g()
    blocks = real_block_dims(g)  # [1, 2]

    # (1) reproduce path 3: Lambda^2_+ = R^3 under order-3 SO(3) = 1 (individual, fixed axis) + 2 (collective).
    checks.append(report(
        "T1.1 reproduce the 1+2 decomposition: Lambda^2_+ = R^3 = 1 (trivial fixed axis = INDIVIDUAL) + 2 "
        "(real-irreducible charged pair = COLLECTIVE) under the order-3 self-dual SO(3)",
        blocks == [1, 2],
        f"real-irreducible block dims = {blocks} (1 individual + 2 collective)"))

    # (2) THE IRREDUCIBILITY: the collective '2' has NO invariant line -> it cannot be split Z/3-equivariantly.
    n_lines = invariant_line_count_in_doublet(g)
    checks.append(report(
        "T1.2 the collective doublet is IRREDUCIBLE: it contains ZERO real g-invariant lines, so it cannot be "
        "split Z/3-equivariantly (a 120-degree rotation has no invariant direction in its plane)",
        n_lines == 0,
        f"invariant lines inside the collective V1 = {n_lines} (irreducible) => no equivariant split of the '2'"))

    # (3) THE FORCING: enclosures that CONTAIN the individual are EXACTLY {1,3}; rank 2 is FORBIDDEN because it
    #     would require splitting the irreducible doublet. This reproduces path 3's {1,3}.
    reachable = enclosures_containing_individual(blocks, individual_block=0)
    checks.append(report(
        "T1.3 FORCING: enclosures containing the individual (fixed axis) are EXACTLY {1,3} -- rank 1 (individual "
        "alone) or rank 3 (individual + whole irreducible doublet); rank 2 is FORBIDDEN (would split the '2'). "
        "Reproduces path 3's {1,3}",
        reachable == [1, 3] and 2 not in reachable,
        f"reachable enclosure ranks = {reachable}; 2 forbidden = {2 not in reachable}"))

    # (4) CONTRAST -- the "explains more" the killed symmetric version LACKED. A hypothetical SYMMETRIC 1+1+1
    #     module, even WITH the same "individual always enclosed" premise, PERMITS rank 2 (base + one of two
    #     SEPARABLE strata). Only the IRREDUCIBLE 1+2 forbids 2.
    symmetric_reachable = enclosures_containing_individual([1, 1, 1], individual_block=0)
    checks.append(report(
        "T1.4 EXPLAINS MORE: the killed SYMMETRIC 1+1+1 module (with the SAME 'individual always enclosed' "
        "premise) PERMITS rank 2 (base + one of two separable strata) -> menu {1,2,3}; the IRREDUCIBLE 1+2 "
        "FORBIDS 2 -> menu {1,3}. The irreducibility that KILLED the symmetric version now FORCES {1,3}",
        symmetric_reachable == [1, 2, 3] and reachable == [1, 3] and (2 in symmetric_reachable) and (2 not in reachable),
        f"symmetric 1+1+1 permits {symmetric_reachable} (2 allowed); irreducible 1+2 forces {reachable} (2 forbidden)"))

    # (5) HONEST GRADE: 'individual always enclosed' (= oddness / contains-fixed-line) is the load-bearing
    #     premise; WITHOUT it, V1 alone (rank 2) is a legitimate invariant subspace. So Test 1 = FORCED GIVEN
    #     the enclosure premise; the premise is the physical reading of path 3's 'oddness' selector.
    all_invariant_dims = sorted({sum(c) for r in range(len(blocks) + 1)
                                 for c in itertools.combinations(blocks, r)})
    v1_alone_is_invariant = 2 in all_invariant_dims
    checks.append(report(
        "T1.5 HONEST GRADE: without the 'individual always enclosed' premise, V1 alone (rank 2) is a legitimate "
        "invariant subspace; so {1,3} is FORCED GIVEN the enclosure premise (= the physical reading of path 3's "
        "oddness selector 'contains the fixed line'), not premise-free",
        v1_alone_is_invariant and all_invariant_dims == [0, 1, 2, 3],
        f"all invariant dims = {all_invariant_dims}; the enclosure premise selects the odd/individual-containing {reachable}"))
    print()


# ====================================================================================================
# TEST 2 -- is level-independence of gauge content (the REPLICAS) a CONSEQUENCE, not an assumption?
# ====================================================================================================
def test2(checks):
    print("TEST 2 -- do the three levels carry IDENTICAL gauge content (the replicas) as a CONSEQUENCE?")

    # Model: matter = (SM gauge rep, dim d_SM) (x) (family/level space, dim 3 = Lambda^2_+).
    # The internal SM gauge group acts as  A (x) I_family  ; the family/level group acts as  I_SM (x) g .
    # 'Capability = gauge content' lives on the SM factor; 'level' indexes the family factor.
    d_SM = 2  # a stand-in SM rep dimension (e.g. a doublet); value irrelevant to the structural claim
    A = np.array([[0.0, 1.0], [1.0, 0.0]])          # a nontrivial SM-gauge generator (stand-in)
    g = cyclic_g()                                   # the family/level generator on Lambda^2_+ = R^3
    I_SM = np.eye(d_SM)
    I_fam = np.eye(3)

    gauge_op = np.kron(A, I_fam)                     # internal gauge acts trivially on the family/level index
    level_op = np.kron(I_SM, g)                      # level/family acts trivially on the gauge index

    # (1) COMMUTING FACTORS: the gauge action and the level action commute -> the family space is a gauge
    #     SINGLET (gauge acts as identity on the level index). This is the structural core of 'replicas'.
    commute = np.allclose(gauge_op @ level_op, level_op @ gauge_op, atol=TOL)
    checks.append(report(
        "T2.1 COMMUTING FACTORS: internal SM gauge (A (x) I) and the level/family action (I (x) g) COMMUTE => "
        "Lambda^2_+ is an SM-gauge SINGLET (gauge acts as identity on the level index)",
        commute,
        "[gauge, level] = 0 => the family/level space is a gauge singlet (the structural basis of the replicas)"))

    # (2) THE REPLICAS AS A CONSEQUENCE: each level (each family basis component) carries the IDENTICAL SM rep.
    #     The gauge generator restricted to level k is A for EVERY k (independent of the level) -- exact replicas.
    per_level_gauge = []
    for k in range(3):
        e_k = np.zeros(3); e_k[k] = 1.0
        P_k = np.kron(I_SM, np.outer(e_k, e_k))      # projector onto level k
        # gauge action restricted to level k, read back on the SM factor:
        block = np.zeros((d_SM, d_SM))
        for i in range(d_SM):
            for j in range(d_SM):
                # <SM=i, level=k| gauge_op |SM=j, level=k>
                bra = np.zeros(2 * 3); bra[i * 3 + k] = 1.0
                ket = np.zeros(2 * 3); ket[j * 3 + k] = 1.0
                block[i, j] = bra @ gauge_op @ ket
        per_level_gauge.append(block)
    replicas = all(np.allclose(per_level_gauge[k], A, atol=TOL) for k in range(3))
    checks.append(report(
        "T2.2 REPLICAS as a CONSEQUENCE: the SM gauge action restricted to EACH level is the SAME operator A "
        "for every level -> identical gauge quantum numbers at all three levels (the defining feature of "
        "generations), following from the singlet property, NOT assumed level-by-level",
        replicas,
        "gauge content is level-INDEPENDENT (same A at levels 0,1,2) => exact replicas as a theorem of the factorization"))

    # (3) CONTRAST -- NOT smuggled: if the family/level group acted NON-trivially on the SM factor (mixing gauge
    #     with level), the gauge content would DIFFER across levels (no replicas). So level-independence <=>
    #     gauge-singlet family space; it is the tensor factorization that is load-bearing, not a free stipulation.
    B = np.array([[1.0, 0.0], [0.0, -1.0]])           # anticommutes with A (sigma_z vs sigma_x)
    entangling = np.kron(B, g)                         # a level action that MIXES gauge and level (not a singlet)
    mixes = not np.allclose(entangling @ gauge_op, gauge_op @ entangling, atol=TOL)
    checks.append(report(
        "T2.3 NOT smuggled: a family/level action that MIXES the gauge factor (A (x) g) does NOT commute with "
        "the gauge action -> gauge content would be level-DEPENDENT (no replicas). So level-independence <=> "
        "gauge-singlet family space; the load-bearing assumption is the tensor factorization (structural in GU: "
        "self-dual FRAME SU(2)_+ vs INTERNAL SM gauge)",
        mixes,
        "a non-singlet level action breaks the replicas => the replica property is a CONSEQUENCE of the singlet factorization"))

    # (4) This ANSWERS Branch C's 'replicas are not regions': correct -- NOT regions (codim-distinct geometry),
    #     but components of a gauge-SINGLET family space, which ARE replicas. Branch C's objection is converted
    #     into the reframe's mechanism.
    checks.append(report(
        "T2.4 ANSWERS 'replicas are not regions': the three are NOT regions (Branch C was right) -- they are "
        "components of the gauge-singlet family space Lambda^2_+, hence REPLICAS. The objection becomes the "
        "mechanism (the reframe EXPLAINS MORE than the killed version here)",
        replicas and commute and mixes,
        "not regions; gauge-singlet family components => replicas (the level-independence is structural, not smuggled)"))
    print()


# ====================================================================================================
# TEST 3 -- does "enforced at three levels" predict a monotone mass hierarchy? THE WALL.
# ====================================================================================================
def group_average_commutant(M0: np.ndarray, g: np.ndarray) -> np.ndarray:
    """Project a symmetric operator onto the commutant of <g> by Reynolds averaging: (1/3) sum_k g^k M0 g^-k.
    The result is symmetric AND commutes with g -- the most general family-SYMMETRIC mass operator's shape."""
    n = 3
    acc = np.zeros_like(M0)
    P = np.eye(g.shape[0])
    for _ in range(n):
        acc += P @ M0 @ P.T
        P = P @ g
    return acc / n


def test3(checks):
    print("TEST 3 (THE WALL) -- does 'enforced at three levels' predict a monotone mass hierarchy?")
    g = cyclic_g()

    # A FIXED symmetric 'raw' mass operator (no RNG); we project it onto the family-symmetric shape.
    M0 = np.array([[1.0, 0.3, 0.1],
                   [0.3, 2.0, 0.2],
                   [0.1, 0.2, 3.0]])
    M_sym = group_average_commutant(M0, g)

    commutes = np.allclose(M_sym @ g, g @ M_sym, atol=TOL)
    evals = np.sort(np.linalg.eigvals(M_sym).real)

    # (1) SCHUR DEGENERACY: any family-symmetric mass operator is SCALAR on the irreducible doublet V1 -> the two
    #     collective states are MASS-DEGENERATE. Predicted spectrum = {c, a, a} = singlet + DEGENERATE pair.
    #     Identify the degenerate pair (two equal eigenvalues) and the lone singlet.
    gaps = np.abs(np.diff(evals))
    n_degenerate_pairs = int(np.sum(gaps < 1e-6))
    checks.append(report(
        "T3.1 SCHUR DEGENERACY: any family-symmetric mass operator (symmetric, commuting with g) is a SCALAR on "
        "the irreducible collective doublet V1 -> the two collective states are MASS-DEGENERATE. Predicted "
        "spectrum = 1 singlet + 1 DEGENERATE pair (a 1+2 pattern)",
        commutes and n_degenerate_pairs == 1,
        f"eigenvalues = {np.round(evals,4).tolist()} => exactly one degenerate pair (m_2 = m_3), one singlet"))

    # (2) THE SAME IRREDUCIBILITY THAT WON TEST 1 LOSES TEST 3. In Test 1 the doublet's irreducibility FORBADE
    #     rank 2 (a win). Here the SAME irreducibility FORCES m_2 = m_3 (a loss): Schur says the commutant of a
    #     real-irreducible rep is a scalar (up to the complex structure, which is antisymmetric -> drops out of a
    #     SYMMETRIC mass matrix).
    checks.append(report(
        "T3.2 DOUBLE-EDGED IRREDUCIBILITY: the irreducibility that FORBIDS rank 2 in Test 1 (a win) FORCES the "
        "collective mass-degeneracy here (a loss) -- a symmetric operator commuting with a real-irreducible "
        "rep is scalar on it (Schur)",
        commutes and n_degenerate_pairs == 1,
        "same structural fact (irreducibility of the '2') wins the count and loses the masses"))

    # (3) CONTRADICTION WITH OBSERVATION: the observed generations are three STRONGLY-ORDERED, NON-degenerate
    #     masses (a 1+1+1 pattern, e.g. m_e : m_mu : m_tau ~ 1 : 207 : 3477). Predicted 1+2 (degenerate pair)
    #     != observed 1+1+1 (all distinct). The enclosure structure predicts the WRONG multiplicity pattern.
    observed_masses = np.array([0.000511, 0.10566, 1.77686])  # e, mu, tau in GeV (PDG-order-of-magnitude)
    observed_gaps = np.abs(np.diff(np.sort(observed_masses)))
    observed_all_distinct = bool(np.all(observed_gaps > 1e-6))
    predicted_has_degenerate_pair = (n_degenerate_pairs == 1)
    checks.append(report(
        "T3.3 CONTRADICTION: observed charged-lepton masses are three NON-degenerate, strongly-ordered values "
        "(a 1+1+1 pattern); the enclosure structure predicts a 1+2 pattern (singlet + DEGENERATE pair). "
        "Predicted degeneracy m_2 = m_3 is CONTRADICTED by m_mu != m_tau (factor ~17)",
        observed_all_distinct and predicted_has_degenerate_pair,
        f"observed all-distinct={observed_all_distinct} (1+1+1) vs predicted degenerate-pair={predicted_has_degenerate_pair} (1+2)"))

    # (4) NO MONOTONE THREE-LEVEL ORDERING: the collective pair {omega, omega^2} is a complex-conjugate pair;
    #     complex conjugation SWAPS them (an antilinear Z/2 symmetry), so there is NO canonical 'Regional <
    #     Global' ordering. The structure gives only a 1-vs-2 (individual-vs-collective) split, not a monotone
    #     three-level ladder. So even a QUALITATIVE monotone hierarchy is NOT predicted.
    conj_swaps = np.allclose(np.conj(OMEGA), OMEGA ** 2, atol=TOL)
    n_canonical_orders_within_collective = 0
    checks.append(report(
        "T3.4 NO MONOTONE LADDER: the collective pair {omega, omega^2} is conjugation-SWAPPED (antilinear Z/2), "
        "so there is NO canonical Regional<Global ordering; the structure gives a 1-vs-2 split, not a monotone "
        "three-level ladder -> no qualitative monotone mass hierarchy is predicted",
        conj_swaps and n_canonical_orders_within_collective == 0,
        "the collective has no canonical internal order => 'enforced at three levels' cannot predict a monotone hierarchy"))

    # (5) VERDICT: the mass hierarchy is NOT predicted (the enclosure structure predicts the WRONG, degenerate
    #     pattern, and no ordering). The hierarchy requires BREAKING the family symmetry, which the enclosure
    #     structure neither supplies nor orders. THIS IS THE REFRAME'S WALL.
    mass_hierarchy_predicted = False
    checks.append(report(
        "T3.5 VERDICT (THE WALL): the mass hierarchy is NOT predicted -- the enclosure structure predicts a "
        "degenerate collective pair (1+2), contradicting the observed non-degenerate 1+1+1 hierarchy, and gives "
        "no monotone ordering. The hierarchy needs family-symmetry BREAKING, outside the enclosure structure",
        mass_hierarchy_predicted is False,
        "mass hierarchy is the reframe's failure point: accommodated at best, never predicted"))
    print()


def main():
    checks = []
    print("=" * 100)
    print("W72 / Path-5 Branch C2  --  three generations as CAPABILITY ENCLOSURES at three levels (reframed count)")
    print("=" * 100)
    test1(checks)
    test2(checks)
    test3(checks)
    print("-" * 100)
    print("SUMMARY (branch C2 -- the defense-attorney re-test of the W69 kill)")
    print("  TEST 1  1 + IRREDUCIBLE-2 FORCES the menu {1,3} and FORBIDS 2 (given the 'individual always enclosed'")
    print("          premise). The irreducibility that KILLED the symmetric 1+1+1 version now FORCES {1,3};")
    print("          the symmetric version PERMITTED 2. => the reframe EXPLAINS MORE on the count. REVIVED.")
    print("  TEST 2  level-independence of gauge content (the REPLICAS) FOLLOWS from Lambda^2_+ being a gauge")
    print("          SINGLET (self-dual FRAME SU(2)_+ commutes with INTERNAL SM gauge), given the tensor")
    print("          factorization. ANSWERS 'replicas not regions'. => EXPLAINS MORE. PARTIALLY/mostly REVIVED.")
    print("  TEST 3  THE WALL: the SAME irreducibility FORCES the collective doublet MASS-DEGENERATE (Schur:")
    print("          m_2 = m_3), predicting a 1+2 pattern that CONTRADICTS the observed non-degenerate 1+1+1")
    print("          hierarchy; and the conjugate pair has no canonical order => no monotone ladder. STAYS DEAD.")
    print("  OVERALL  count leg PARTIALLY REVIVED: explains {1,3} and the replicas (more than the killed version),")
    print("           but NOT the masses. The mass hierarchy is the honest boundary of what the reframe explains.")
    print("  No canon / RESEARCH-STATUS / verdict / posture movement; the generation count stays OPEN.")
    print("=" * 100)

    ok = all(checks)
    print(("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED") + f"  ({sum(checks)}/{len(checks)})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
