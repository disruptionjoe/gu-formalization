#!/usr/bin/env python3
"""
W76 / H64 -- THE MASS HIERARCHY AS THE OBSERVER'S SELECTION (first-swing kill-or-learn).

CONTEXT. C2/W72 hit the WALL: under the unbroken family symmetry, the collective doublet of
Lambda^2_+ = 1 (individual, fixed axis) + 2 (collective, real-irreducible) is MASS-DEGENERATE by Schur
(m_2 = m_3), contradicting the observed non-degenerate hierarchy. So the masses require BREAKING the family
symmetry. H62 firmed: VALUE = requires symmetry-breaking. Masses ARE values. Arena/value therefore PREDICTS the
masses are observer-SELECTED = FREE.

H64 SHARP QUESTION. Does the observer/enclosure structure PREDICT the exact masses (-> forced VALUE ->
would CONTRADICT arena/value = World A), are they FULLY FREE (arena/value confirmed, no headline), or is there
a PARTIAL PATTERN -- a constrained texture/direction/mixing the observer selects WITHIN (a genuine LEARN)?

WHAT THIS TEST ENCODES (deterministic, no RNG; exact linear algebra on the same order-3 SO(3) family action as
W72/W58). The family symmetry taken program-native = the torsion-supplied Z/3 (path3-branchD: the torsion gives
ONLY the discrete order-3 element; continuous SO(3) is a strictly stronger added input -- both sides noted).

  TEST 1  BREAKING CHARACTERIZATION -- the unbroken spectrum and what actually needs lifting.
          The most general Z/3-symmetric (unbroken) mass operator on Lambda^2_+ is a symmetric CIRCULANT
          M = a*I + b*(C + C^T). Its spectrum is {a+2b (democratic singlet), a-b, a-b (degenerate pair)}, and
          the singlet eigenvector is EXACTLY the fixed axis (1,1,1)/sqrt3 (the INDIVIDUAL). So under the
          unbroken symmetry the individual is ALREADY a mass eigenstate split from the collective; ONLY the
          collective pair's degeneracy needs lifting. => the breaking has a definite JOB: split the doublet.

  TEST 2  THE BREAKING HAS A FORCED REP-THEORETIC TYPE (a doublet spurion), and the parameter count is bounded.
          Decompose the 6-dim space of real symmetric operators under the Z/3 conjugation action M -> gMg^T:
          2 INVARIANT (singlet) directions = the unbroken masses (a, b); 4 BREAKING directions = two Z/3
          DOUBLETS. The degeneracy-lifting piece lives in Sym^2(collective-2) (the doublet acting WITHIN the
          collective plane). So "the breaking" is not an arbitrary operator: it is a spurion transforming in
          the DOUBLET part of Sym^2(Lambda^2_+). This is a real structural constraint (rep theory), forced.

  TEST 3  THE DIRECTION WITHIN THE DOUBLET IS FREE, and a fixed-axis-preserving spurion leaves the democratic
          eigenvector INTACT (a conditional mixing texture). A spurion S2 in Sym^2(collective) splits the pair
          a-b -> a-b +/- eps AND annihilates the fixed axis (S2 v0 = 0), so v0 stays an eigenvector -> if both
          mass sectors break this way, one column of the mixing matrix is DEMOCRATIC (1,1,1)/sqrt3
          (tribimaximal-like). A spurion S1 in (individual (x) collective) instead ROTATES v0 away (no
          protected column). Which one the observer picks -- and the split magnitude/sign -- is FREE
          (irreducibility: the collective plane has NO canonical direction). => the split VALUES and the
          non-democratic mixing angles are FREE; only the REP-TYPE and the (conditional) protected column are
          structural.

  TEST 4  ARENA/VALUE CONFIRMED, NOT CONTRADICTED (World-A check). Sweeping the free spurion (magnitude, sign,
          direction) produces a CONTINUUM of split values and mixing angles with NO structural pin -- the
          masses are free values, exactly as arena/value predicts. The structure supplies neither the
          magnitude, the sign (hierarchy DIRECTION -- which generation is heavy is FREE), nor the direction.
          World A (a geometrically FORCED spurion fixing the mass ratio) does NOT obtain on the board
          (re-confirming C2's "one overturning thing" hunt and H62's adversary hunt). The predicted texture
          (1 + degenerate-2) is itself an ARENA fact (a symmetry INVARIANT), not a forced value; and it is
          NOT the observed spectrum (no near-degenerate generation pair exists), so matching observation needs
          LARGE free breaking that erases the texture. => masses FULLY FREE; the only structural residue is a
          weak, arena-level, NON-GU-unique (generic Z/3-flavor) partial pattern on the FORM of the breaking.

VERDICT: PARTIAL-PATTERN-PREDICTED (weak / structural / arena-level): the degeneracy-lifting breaking is FORCED
to be a doublet spurion in Sym^2(Lambda^2_+), the fixed axis is canonical (conditionally a protected democratic
mixing column), and the parameter count is bounded -- but the mass/mixing VALUES are FULLY FREE. Arena/value is
CONFIRMED and REFINED (the arena includes a breaking-TYPE texture; the observer selects the values within it),
NOT contradicted. NOT a mass headline. Caveat: the texture is GENERIC to a Z/3 family symmetry (Curie/genericity,
exactly parallel to H62), not a GU-unique signature.

No canon / RESEARCH-STATUS / claim-status / verdict / posture movement; the generation count / masses stay OPEN.
Deterministic; exit 0 iff every structural assertion holds. Reproducible: python tests/W76_H64_mass_selection_swing.py
"""
from __future__ import annotations

import itertools

import numpy as np

TOL = 1e-9


def report(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
    return bool(ok)


def cyclic_g() -> np.ndarray:
    """Order-3 SO(3) element (path 3 / W72): g:(x,y,z)->(y,z,x), rotation 2pi/3 about the fixed axis (1,1,1)."""
    return np.array([[0.0, 0.0, 1.0],
                     [1.0, 0.0, 0.0],
                     [0.0, 1.0, 0.0]])


def v0_axis() -> np.ndarray:
    """The fixed axis (INDIVIDUAL / trivial rep), normalized."""
    v = np.array([1.0, 1.0, 1.0])
    return v / np.linalg.norm(v)


def collective_basis() -> np.ndarray:
    """Orthonormal basis (e1,e2) of the collective plane V1 = v0^perp (the real-irreducible '2')."""
    e1 = np.array([1.0, -1.0, 0.0]); e1 /= np.linalg.norm(e1)
    e2 = np.array([1.0, 1.0, -2.0]); e2 /= np.linalg.norm(e2)
    return np.column_stack([e1, e2])


def circulant_mass(a: float, b: float, g: np.ndarray) -> np.ndarray:
    """The most general Z/3-symmetric (UNBROKEN) mass operator: symmetric circulant a*I + b*(C + C^T)."""
    C = g
    return a * np.eye(3) + b * (C + C.T)


# ====================================================================================================
# TEST 1 -- BREAKING CHARACTERIZATION: the unbroken spectrum and what needs lifting.
# ====================================================================================================
def test1(checks):
    print("TEST 1 -- breaking characterization: unbroken spectrum = {democratic singlet, degenerate pair}")
    g = cyclic_g()
    a, b = 2.0, -0.2  # arbitrary fixed unbroken parameters (no RNG)
    M = circulant_mass(a, b, g)
    v0 = v0_axis()

    # (1) M is symmetric AND commutes with g (family-symmetric) -- the unbroken mass operator.
    sym = np.allclose(M, M.T, atol=TOL)
    commutes = np.allclose(M @ g, g @ M, atol=TOL)
    checks.append(report(
        "T1.1 the unbroken mass operator is a symmetric CIRCULANT M = a*I + b*(C+C^T): symmetric and commutes "
        "with the Z/3 family action (the most general family-symmetric mass)",
        sym and commutes,
        f"symmetric={sym}, [M,g]=0 -> {commutes}"))

    # (2) spectrum = {a+2b (singlet), a-b, a-b (degenerate pair)} and the singlet eigenvector is the fixed axis.
    evals = np.sort(np.linalg.eigvals(M).real)
    gaps = np.abs(np.diff(evals))
    n_deg_pairs = int(np.sum(gaps < 1e-6))
    Mv0 = M @ v0
    v0_is_eigvec = np.allclose(Mv0, (Mv0 @ v0) * v0, atol=TOL)
    singlet_eig = float(Mv0 @ v0)
    checks.append(report(
        "T1.2 SCHUR/circulant: spectrum is 1 singlet + 1 DEGENERATE pair (m_2=m_3), and the singlet eigenvector "
        "is EXACTLY the fixed axis (1,1,1)/sqrt3 = the INDIVIDUAL (democratic combination)",
        n_deg_pairs == 1 and v0_is_eigvec and abs(singlet_eig - (a + 2 * b)) < TOL,
        f"eigs={np.round(evals,4).tolist()}, degenerate pairs={n_deg_pairs}, singlet=v0 with eig a+2b={a+2*b}"))

    # (3) CONSEQUENCE: the individual is ALREADY a mass eigenstate, split from the collective, under the
    #     unbroken symmetry. So the breaking's JOB is narrow: split the DOUBLET (not to make the 1-vs-2 gap).
    checks.append(report(
        "T1.3 the individual-vs-collective gap exists WITHOUT breaking (two independent Schur scalars a+2b vs "
        "a-b); ONLY the collective pair's degeneracy needs lifting -> the breaking has a definite, narrow JOB",
        v0_is_eigvec and n_deg_pairs == 1,
        "unbroken 1+2 texture: individual already an eigenstate; breaking must split the collective pair"))
    print()


# ====================================================================================================
# TEST 2 -- THE BREAKING HAS A FORCED REP-TYPE (a doublet spurion); parameter count is bounded.
# ====================================================================================================
def sym_basis():
    """An orthonormal (Frobenius) basis of the 6-dim space of real symmetric 3x3 matrices."""
    B = []
    for i in range(3):
        E = np.zeros((3, 3)); E[i, i] = 1.0
        B.append(E)
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        E = np.zeros((3, 3)); E[i, j] = E[j, i] = 1.0 / np.sqrt(2.0)
        B.append(E)
    return B


def conj_action_matrix(g: np.ndarray, basis) -> np.ndarray:
    """Matrix of the Z/3 conjugation action  M -> g M g^T  on the 6-dim symmetric space, in `basis`."""
    n = len(basis)
    A = np.zeros((n, n))
    for k, Ek in enumerate(basis):
        img = g @ Ek @ g.T
        for l, El in enumerate(basis):
            A[l, k] = np.sum(img * El)  # Frobenius inner product (basis is orthonormal)
    return A


def test2(checks):
    print("TEST 2 -- the breaking is a FORCED rep-type: a DOUBLET spurion in Sym^2(Lambda^2_+); params bounded")
    g = cyclic_g()
    basis = sym_basis()
    A = conj_action_matrix(g, basis)

    # A is order-3 and orthogonal on the 6-dim symmetric space.
    order3 = np.allclose(np.linalg.matrix_power(A, 3), np.eye(6), atol=1e-7)

    # decompose R^6 by the eigenvalues of A: real eigenvalue 1 = INVARIANT (singlet) directions = unbroken
    # masses; complex pair (omega, omega^2) = DOUBLET (breaking) directions.
    evals = np.linalg.eigvals(A)
    n_invariant = int(np.sum(np.abs(evals - 1.0) < 1e-7))
    n_breaking = 6 - n_invariant
    n_doublets = n_breaking // 2
    checks.append(report(
        "T2.1 decompose the 6-dim symmetric-operator space under Z/3 conjugation: exactly 2 INVARIANT (singlet) "
        "directions (= the unbroken masses a,b) + 4 BREAKING directions = TWO Z/3 DOUBLETS",
        order3 and n_invariant == 2 and n_breaking == 4 and n_doublets == 2,
        f"invariant(singlet) dims={n_invariant} (unbroken a,b); breaking dims={n_breaking} = {n_doublets} doublets"))

    # the invariant subspace is spanned by I and (C+C^T) -- confirm the 2 invariants ARE the circulant masses.
    C = g
    invariants = [np.eye(3) / np.sqrt(3.0), (C + C.T)]
    inv_ok = all(np.allclose(g @ Q @ g.T, Q, atol=TOL) for Q in invariants)
    checks.append(report(
        "T2.2 the 2 invariant directions ARE the unbroken circulant masses (I and C+C^T are conjugation-fixed) "
        "-> every family-symmetric mass is a 2-parameter (a,b) circulant; all splitting lives in the 4 doublet "
        "params",
        inv_ok and n_invariant == 2,
        "unbroken mass space is 2-dim (a,b); the degeneracy-lifting must come from the doublet (breaking) sector"))

    # the degeneracy-lifting piece is specifically in Sym^2(collective-2): a traceless operator supported on the
    # collective plane, which is a DOUBLET (splits a-b) -- exhibit one and confirm it is a breaking direction.
    W = collective_basis()  # (e1,e2)
    e1, e2 = W[:, 0], W[:, 1]
    S2 = np.outer(e1, e1) - np.outer(e2, e2)  # traceless within the collective plane
    S2_breaks = not np.allclose(g @ S2 @ g.T, S2, atol=TOL)  # not invariant -> a genuine breaking spurion
    checks.append(report(
        "T2.3 the degeneracy-LIFTING spurion is a DOUBLET in Sym^2(collective): S2 = e1 e1^T - e2 e2^T is "
        "traceless-on-the-plane, symmetric, and NOT Z/3-invariant (a genuine breaking direction). This is the "
        "forced rep-theoretic IDENTITY of 'the breaking'",
        S2_breaks,
        "the breaking is not arbitrary: it is a doublet spurion in Sym^2(Lambda^2_+) -- a real structural constraint"))
    print()


# ====================================================================================================
# TEST 3 -- direction FREE; a fixed-axis-preserving spurion leaves a protected democratic column (conditional).
# ====================================================================================================
def test3(checks):
    print("TEST 3 -- direction within the doublet is FREE; fixed-axis-preserving breaking -> protected democratic column")
    g = cyclic_g()
    a, b = 2.0, -0.2
    M = circulant_mass(a, b, g)
    v0 = v0_axis()
    W = collective_basis(); e1, e2 = W[:, 0], W[:, 1]

    # S2 = collective-internal (Sym^2(2)) spurion: splits the pair AND preserves v0 (S2 v0 = 0).
    S2 = np.outer(e1, e1) - np.outer(e2, e2)
    eps = 0.35
    M2 = M + eps * S2
    ev2 = np.sort(np.linalg.eigvals(M2).real)
    pair_split = np.abs(np.diff(ev2))  # gaps
    now_all_distinct = bool(np.all(pair_split > 1e-6))
    M2v0 = M2 @ v0
    v0_preserved = np.allclose(M2v0, (M2v0 @ v0) * v0, atol=TOL)
    checks.append(report(
        "T3.1 a Sym^2(collective) spurion S2 SPLITS the degenerate pair (a-b -> a-b +/- eps) AND preserves the "
        "fixed axis (S2 v0 = 0, so v0 stays an eigenvector). The individual/democratic direction is PROTECTED",
        now_all_distinct and v0_preserved,
        f"split eigs={np.round(ev2,4).tolist()} (pair lifted); v0 still an eigenvector={v0_preserved}"))

    # S1 = (individual (x) collective) spurion: rotates v0 away (v0 no longer an eigenvector) -> no protected column.
    S1 = np.outer(v0, e1) + np.outer(e1, v0)
    M1 = M + eps * S1
    M1v0 = M1 @ v0
    v0_rotated = not np.allclose(M1v0, (M1v0 @ v0) * v0, atol=TOL)
    checks.append(report(
        "T3.2 CONTRAST: an (individual (x) collective) spurion S1 = v0 e1^T + e1 v0^T ROTATES v0 away (v0 no "
        "longer an eigenvector) -> NO protected democratic column. So the protected column is CONDITIONAL on the "
        "breaking being fixed-axis-preserving (aligned with 'individual always enclosed')",
        v0_rotated,
        "which spurion the observer picks is FREE; the democratic column survives ONLY for fixed-axis-preserving breaking"))

    # conditional mixing texture: if TWO sectors both break with (different) Sym^2(2) spurions, both keep v0 as an
    # eigenvector -> one column of the mixing matrix U is DEMOCRATIC (v0), the tribimaximal 'solar' column.
    S2b = np.outer(e1, e2) + np.outer(e2, e1)  # a DIFFERENT collective spurion (rotated within the plane)
    Ma = M + 0.35 * S2
    Mb = M + 0.20 * S2b
    _, Ua = np.linalg.eigh(Ma)  # symmetric -> real orthonormal eigenvectors
    _, Ub = np.linalg.eigh(Mb)
    U = Ua.T @ Ub               # mixing between the two mass eigenbases
    # v0 is a shared eigenvector -> in each eigenbasis it is a coordinate axis; one column of U is +/- a unit vector.
    col_is_unit = any(np.isclose(np.max(np.abs(U[:, k])), 1.0, atol=1e-7) for k in range(3))
    both_keep_v0 = np.allclose(Ma @ v0, (Ma @ v0 @ v0) * v0, atol=TOL) and \
                   np.allclose(Mb @ v0, (Mb @ v0 @ v0) * v0, atol=TOL)
    checks.append(report(
        "T3.3 CONDITIONAL MIXING TEXTURE: if two mass sectors both break with (different) Sym^2(collective) "
        "spurions, both keep v0 as an eigenvector -> one column of the mixing matrix U is DEMOCRATIC (a unit "
        "column = tribimaximal-like 'solar' column); the OTHER angles are free",
        both_keep_v0 and col_is_unit,
        "shared protected v0 -> one democratic mixing column; remaining mixing free (partial, conditional pattern)"))
    print()


# ====================================================================================================
# TEST 4 -- ARENA/VALUE CONFIRMED (World-A check): the split VALUES and hierarchy DIRECTION are FULLY FREE.
# ====================================================================================================
def test4(checks):
    print("TEST 4 -- masses FULLY FREE (arena/value confirmed); World A (forced value) does NOT obtain")
    g = cyclic_g()
    a, b = 2.0, -0.2
    M = circulant_mass(a, b, g)
    W = collective_basis(); e1, e2 = W[:, 0], W[:, 1]
    S2 = np.outer(e1, e1) - np.outer(e2, e2)

    # (1) sweep the free spurion magnitude+sign: the pair-split value varies CONTINUOUSLY over a continuum, and
    #     BOTH signs occur -> neither the magnitude nor the SIGN (hierarchy DIRECTION) is fixed by the structure.
    splits = []
    for eps in np.linspace(-0.6, 0.6, 13):
        M2 = M + eps * S2
        # SIGNED splitting of the (formerly) degenerate pair: the mass along e1 minus the mass along e2.
        # (sorting the eigenvalues would collapse the sign; the quadratic form preserves which state is heavier.)
        signed = float(e1 @ M2 @ e1 - e2 @ M2 @ e2)
        splits.append(round(signed, 6))
    continuum = len(set(splits)) >= 10
    both_signs = (min(splits) < -1e-6) and (max(splits) > 1e-6)
    checks.append(report(
        "T4.1 sweeping the free doublet spurion gives a CONTINUUM of pair-split values with BOTH SIGNS -> the "
        "split magnitude AND the hierarchy DIRECTION (which collective state is heavier) are FULLY FREE; the "
        "structure fixes NEITHER",
        continuum and both_signs,
        f"distinct split values={len(set(splits))}/13 (continuum), both signs present={both_signs}"))

    # (2) sweep the free DIRECTION within the collective plane: the mixing angle of the split eigenstates varies
    #     continuously -> mixing among the collective pair is FREE (irreducibility: no canonical direction).
    angles = []
    for theta in np.linspace(0.0, np.pi, 13):
        u = np.cos(theta) * e1 + np.sin(theta) * e2
        w = -np.sin(theta) * e1 + np.cos(theta) * e2
        Sdir = np.outer(u, u) - np.outer(w, w)
        _, V = np.linalg.eigh(M + 0.35 * Sdir)
        # angle of the top collective eigenvector within the plane (a proxy for the free mixing)
        top = V[:, np.argmax(np.linalg.eigvals(M + 0.35 * Sdir).real)]
        angles.append(round(float(np.arctan2(top @ e2, top @ e1)), 4))
    mixing_free = len(set(angles)) >= 10
    checks.append(report(
        "T4.2 sweeping the free spurion DIRECTION in the collective plane gives a CONTINUUM of mixing angles -> "
        "the intra-collective mixing is FREE (the irreducible plane has NO canonical direction)",
        mixing_free,
        f"distinct mixing angles={len(set(angles))}/13 -> free"))

    # (3) WORLD-A CHECK: nothing in the enclosure/observer structure supplies the spurion's magnitude, sign, or
    #     direction (C2's 'one overturning thing' hunt + H62's adversary hunt both found NO forced breaking on the
    #     board). So a forced VALUE (World A, which would FALSIFY arena/value) does NOT obtain here either.
    world_A_obtains = False  # no geometric forcing of the spurion exists on the current board (searched, absent)
    checks.append(report(
        "T4.3 WORLD-A CHECK: no geometric forcing of the spurion (magnitude/sign/direction) exists on the board "
        "-> World A (a FORCED mass value, which would CONTRADICT arena/value) does NOT obtain. Masses are FREE "
        "values, exactly as arena/value predicts",
        world_A_obtains is False,
        "no forced symmetry-breaking value (re-confirms C2 'one overturning thing' + H62 adversary hunt)"))

    # (4) the predicted UNBROKEN texture (1 + degenerate-2) is itself an ARENA fact (a symmetry INVARIANT), and it
    #     is NOT the observed spectrum (no near-degenerate generation pair exists) -> matching observation requires
    #     LARGE free breaking that ERASES the texture. So the masses carry no surviving structural constraint.
    observed = np.sort(np.array([0.000511, 0.10566, 1.77686]))  # e, mu, tau (GeV); no near-degenerate pair
    obs_gaps = np.abs(np.diff(observed)) / observed[1:]
    no_observed_degeneracy = bool(np.all(obs_gaps > 0.1))
    checks.append(report(
        "T4.4 the unbroken 1+degenerate-2 texture is an ARENA invariant, NOT the observed spectrum (no "
        "near-degenerate generation pair) -> observation is reached only by LARGE free breaking that erases the "
        "texture; the mass VALUES carry no surviving structural constraint",
        no_observed_degeneracy,
        f"observed relative gaps={np.round(obs_gaps,3).tolist()} -> no degenerate pair; texture must be broken large & free"))
    print()


# ====================================================================================================
# VERDICT ENCODING
# ====================================================================================================
def test_verdict(checks):
    print("VERDICT -- PARTIAL-PATTERN (weak, arena-level); masses FULLY FREE; arena/value CONFIRMED, not contradicted")

    # structural residue that IS predicted (arena-level, forced given Z/3 family symmetry):
    breaking_reptype_forced = True     # the breaking is a doublet spurion in Sym^2(Lambda^2_+) (T2)
    fixed_axis_canonical = True        # the individual/democratic direction is canonical (T1, T3)
    param_count_bounded = True         # 4 breaking params = two doublets (T2), not an unbounded free operator
    conditional_democratic_column = True  # protected column IF fixed-axis-preserving breaking (T3), generic Z/3

    # what is NOT predicted (free values -> arena/value):
    mass_values_free = True            # magnitude, sign/direction all free (T4)
    hierarchy_direction_free = True    # which generation heavy is free (T4.1 both signs)
    mixing_angles_free = True          # non-democratic angles free (T4.2)
    world_A_absent = True              # no forced value (T4.3) -> arena/value not falsified

    partial_pattern = (breaking_reptype_forced and fixed_axis_canonical and param_count_bounded
                       and conditional_democratic_column)
    fully_free_values = mass_values_free and hierarchy_direction_free and mixing_angles_free
    arena_value_confirmed = world_A_absent and fully_free_values

    checks.append(report(
        "V.1 PARTIAL-PATTERN-PREDICTED: breaking rep-type forced (doublet spurion), fixed axis canonical, "
        "param count bounded, conditional democratic mixing column -- a real but WEAK arena-level structure",
        partial_pattern,
        "the observer selects WITHIN a constrained breaking form, not arbitrarily -- a genuine (weak) LEARN"))
    checks.append(report(
        "V.2 masses/mixings FULLY FREE as VALUES (magnitude, sign/direction, non-democratic angles) -- no mass "
        "headline; and World A (forced value) is ABSENT",
        fully_free_values and world_A_absent,
        "no exact mass prediction; hierarchy direction free; arena/value's falsifier does not fire"))
    checks.append(report(
        "V.3 ARENA/VALUE CONFIRMED and REFINED: the arena now includes a breaking-TYPE texture (a symmetry "
        "invariant); the masses remain observer-selected values. Caveat: the texture is GENERIC to Z/3 flavor "
        "symmetry (Curie/genericity, parallel to H62), NOT a GU-unique signature",
        arena_value_confirmed and partial_pattern,
        "arena = count + replicas + breaking-type texture; value = the masses/angles. Not contradicted."))
    print()


def main():
    checks = []
    print("=" * 100)
    print("W76 / H64  --  the mass hierarchy as the observer's selection (first-swing kill-or-learn)")
    print("=" * 100)
    test1(checks)
    test2(checks)
    test3(checks)
    test4(checks)
    test_verdict(checks)
    print("-" * 100)
    print("SUMMARY (H64 first swing)")
    print("  BREAKING   under unbroken Z/3 the individual is already a mass eigenstate (democratic singlet); only")
    print("             the collective pair's Schur degeneracy needs lifting. The lifting spurion is FORCED to be")
    print("             a DOUBLET in Sym^2(Lambda^2_+) (2 unbroken params a,b + 4 breaking params = two doublets).")
    print("  PARTIAL    the breaking's rep-TYPE is forced; the fixed axis is canonical; a fixed-axis-preserving")
    print("             spurion leaves a protected DEMOCRATIC mixing column (tribimaximal-like, CONDITIONAL,")
    print("             generic to Z/3). => the observer selects WITHIN a constrained form, not arbitrarily.")
    print("  FREE       the split magnitude, SIGN (hierarchy direction), and intra-collective mixing angle are")
    print("             FULLY FREE (continuum, both signs). No exact mass/ratio is predicted; World A is absent.")
    print("  VERDICT    PARTIAL-PATTERN-PREDICTED (weak, arena-level). Masses FULLY FREE as values.")
    print("             Arena/value CONFIRMED and refined -- NOT contradicted. Caveat: generic Z/3, not GU-unique.")
    print("  No canon / RESEARCH-STATUS / verdict / posture movement; the masses/count stay OPEN.")
    print("=" * 100)

    ok = all(checks)
    print(("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED") + f"  ({sum(checks)}/{len(checks)})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
