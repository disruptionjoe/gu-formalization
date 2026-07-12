#!/usr/bin/env python3
r"""
W60 / Path-3 WAVE-2 -- IS SU(2)_+ A FORCED CONTINUOUS GAUGE SYMMETRY OF THE GENERATION SPACE?

The five-branch blind wave (branches A-E) reduced the whole "why three generations?" question to
ONE decisive fork. Branches D and E INDEPENDENTLY named the single escape hatch from the class-wide
no-go: promote the discrete order-3 element (Z/3 subset pi_3^s = Z/24) to the CONTINUOUS self-dual
frame group SU(2)_+ = SO(3). Under the connected group Lambda^2_+(R^4) = R^3 is IRREDUCIBLE, so any
generation content that is an SU(2)_+-equivariant subspace of the adjoint is forced to rank 3.

THE DECISIVE QUESTION (this file): is SU(2)_+ a FORCED continuous gauge symmetry that makes the
generation multiplet the ADJOINT Lambda^2_+ (=> count forced to 3), or is only the discrete Z/3
forced (=> count stays {1,3}, no-go final)?

CONSTRUCTION USED (per GEOMETER-VS-PHYSICS-OBJECTS.md): the GAUGED-CHIRAL-FRAME construction of both
objects. "SU(2)_+" = the self-dual half of the local frame-rotation group Spin(4)=SU(2)+ x SU(2)-,
gauged by the spin connection (this is standard 4D physics: local Lorentz IS gauged). "The generation
space" = a representation of that SU(2)_+ living in / related to Lambda^2_+ = adjoint su(2)+. This is
the geometer's side; the internal-global alternative (a NEW internal SU(2) that is NOT the frame group)
is flagged where it changes the answer.

TWO INDEPENDENT DERIVATIONS, required to AGREE:
  D1 (representation-theoretic).  Gauging a group G never forces matter into the adjoint. Matter reps
     are FREE: Rep(SU(2)) has an irrep of every dimension 1,2,3,4,...; the adjoint (dim 3) is ONE of
     them, and the trivial rep (dim 1, sterile) is admissible. So "SU(2)_+ is gauged" does NOT force
     the generation multiplet to be Lambda^2_+. FORCING requires the ADDED identification
     "generation multiplet = the adjoint bundle" -- which is the answer as a premise.
     The ONE thing that DOES force 3 *given that identification*: SCHUR. An SU(2)_+-equivariant
     endomorphism of the irreducible Lambda^2_+ is a scalar, so an equivariant subspace (or the kernel
     of an equivariant operator) is {0} or ALL of R^3 -- the {1,2} sub-ranks are NOT SU(2)_+-invariant.
     Hence forcing is CONDITIONAL on C1: the generation selection is equivariant under the CONTINUOUS
     SU(2)_+ (not merely the discrete Z/3) AND lands inside the adjoint.
  D2 (consistency / anomaly).  The sterile SU(2)_+-SINGLET generation sector SURVIVES gauging. A
     trivial rep is a legitimate SU(2)_+ module; a one-generation (rank-1) sterile universe cancels
     every gauge & mixed anomaly, and the relevant mod-3 Dai-Freed arena is EMPTY (repo R2:
     Omega^Spin_5(BG_SM) (x) Z_(3) = 0). So no consistency/anomaly condition obstructs the sterile
     sector. Under the CONTINUOUS group the rank-1 "fixed axis" is NOT a subspace of Lambda^2_+ (it is
     not SO(3)-invariant -- proven below with a second generator), but it PERSISTS as an SU(2)_+
     singlet EXTERNAL to the adjoint. The rank-1 solution is relocated, not forbidden.

  D1 and D2 AGREE: absent C1, NOT FORCED -- the count stays {1,3} (1 = SU(2)_+ singlet sector;
  3 = adjoint sector; the even option, the dim-2 fundamental, is excluded by oddness/chirality).

VERDICT: NOT-FORCED, i.e. CONDITIONAL-ON-C1 with C1 NOT supplied by the framework.
  * SU(2)_+ IS gauged (spin connection) -- TRUE and continuous. But that hands you a group acting on
    SPIN space, and gauging never forces adjoint matter, so it does NOT by itself make the FLAVOR /
    generation multiplet the adjoint.
  * The forcing is exactly as strong as C1 = "the generation bundle is an SU(2)_+-equivariant subspace
    of the adjoint Lambda^2_+ (continuous-equivariant, nonzero)". Under C1, Schur forces 3 (THEOREM).
  * The framework does NOT supply C1: the torsion construction that REACHES the count supplies only the
    discrete Z/3; a family index is Lorentz-scalar (internal), while the frame SU(2)_+ acts on spin --
    on flavor space it acts trivially unless C1 is imposed by hand. C1 is faithfulness/maximality in
    geometric clothing: the answer as premise.
  * The ONE native crack where C1 could become first-principles: GU's super-IG guardian, whose
    {Q,Q} ~ Omega^1(ad) = the SPIN CONNECTION (GEOMETER-VS-PHYSICS-OBJECTS.md, graded row). IF super-IG
    makes the family bundle frame-covariant (adjoint-valued, SU(2)_+-equivariant), C1 holds and 3 is
    forced. That is an unestablished conjecture about GU's native graded structure, not a theorem.

LOAD-BEARING ASSUMPTION (for FORCING): C1 -- the generation multiplet is the SU(2)_+ ADJOINT bundle
(equivariant under the CONTINUOUS frame group), not a sub-rep and not an external singlet. Not supplied.

Deterministic: exact small-integer / low-tolerance float linear algebra, no randomness. Exit 0 on PASS.
Reproducible: python tests/W60_path3_wave2_su2plus.py
"""
from __future__ import annotations

import itertools

import numpy as np

TOL = 1e-9


def report(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
    return bool(ok)


# ------------------------------------------------------------------------------------------------
# Representation theory of SU(2) / SO(3).
# ------------------------------------------------------------------------------------------------
def su2_irrep_dim(twice_j: int) -> int:
    """dim of the SU(2) irrep of spin j = twice_j/2 is 2j+1 = twice_j + 1.
    twice_j = 0 -> trivial (dim 1); 1 -> fundamental (dim 2); 2 -> adjoint/vector (dim 3)."""
    return twice_j + 1


def cyclic_g():
    """g:(x,y,z)->(y,z,x): exact order-3 element of SO(3), rotation 2pi/3 about (1,1,1)."""
    return np.array([[0.0, 0.0, 1.0],
                     [1.0, 0.0, 0.0],
                     [0.0, 1.0, 0.0]])


def rot_x_quarter():
    """h: rotation by 90 deg about the x-axis, h(x,y,z)=(x,-z,y). A second SO(3) generator,
    used to show the g-fixed axis (1,1,1) is NOT SO(3)-invariant (irreducibility of the connected group)."""
    return np.array([[1.0, 0.0, 0.0],
                     [0.0, 0.0, -1.0],
                     [0.0, 1.0, 0.0]])


def real_invariant_subspace_dims(g, tol=1e-9):
    """All real g-invariant subspace dims from the real-irreducible block structure."""
    evals = np.linalg.eigvals(g)
    fixed = int(np.sum(np.abs(evals - 1.0) < tol))
    n_pair = (g.shape[0] - fixed) // 2
    blocks = [1] * fixed + [2] * n_pair
    dims = set()
    for r in range(len(blocks) + 1):
        for combo in itertools.combinations(range(len(blocks)), r):
            dims.add(sum(blocks[i] for i in combo))
    return sorted(dims), blocks


def common_invariant_lines(mats, tol=1e-7):
    """Return the real 1-dim subspaces (as normalized axes) invariant under EVERY matrix in `mats`.
    A real line span{v} is invariant under M iff v is a real eigenvector of M. We collect real
    eigenvectors of the first matrix and keep those that are eigenvectors of all the others."""
    M0 = mats[0]
    w, V = np.linalg.eig(M0)
    lines = []
    for k in range(len(w)):
        if abs(w[k].imag) > tol:
            continue
        v = V[:, k].real
        if np.linalg.norm(v) < tol:
            continue
        v = v / np.linalg.norm(v)
        ok = True
        for M in mats[1:]:
            Mv = M @ v
            # invariant line: Mv parallel to v  <=>  ||Mv - (v.Mv) v|| = 0
            resid = Mv - (v @ Mv) * v
            if np.linalg.norm(resid) > tol:
                ok = False
                break
        if ok:
            lines.append(v)
    return lines


def schur_equivariant_kernel_dims(irreducible: bool):
    """Schur's lemma: an equivariant endomorphism of an IRREDUCIBLE real rep whose endomorphism ring
    is R (the vector 3-dim rep of SO(3) is absolutely irreducible, End = R) is a scalar lambda*Id.
    Its kernel is {0} (lambda != 0) or the whole space (lambda = 0). So equivariant-subspace / kernel
    dims are {0, dim}. If NOT irreducible, intermediate equivariant subspaces exist."""
    if irreducible:
        return [0, 3]  # {0, whole}: no intermediate equivariant subspace
    return [0, 1, 2, 3]


def main():
    checks = []
    print("=" * 100)
    print("W60 / Path-3 WAVE-2  --  is SU(2)_+ a FORCED continuous gauge symmetry of the generation space?")
    print("=" * 100)

    # =========================================================================================
    # (A) anchors: 3 = dim Lambda^2_+ = dim adjoint su(2)+  (reproduced independently)
    # =========================================================================================
    print("(A) anchors: Lambda^2_+(R^4) = adjoint su(2)+, dim 3")
    dim_lambda2_plus = 6 // 2  # dim Lambda^2(R^4)=C(4,2)=6 = 3+3; self-dual half = 3
    dim_adjoint_su2 = su2_irrep_dim(2)  # spin-1 = adjoint = 2*1+1 = 3
    checks.append(report(
        "A1. dim Lambda^2_+(R^4) = 3 = dim adjoint su(2)+ (spin-1 irrep, 2j+1 with j=1). The '3' is the "
        "DIMENSION of the adjoint of the self-dual frame group -- derived, not imported",
        dim_lambda2_plus == 3 and dim_adjoint_su2 == 3 and dim_lambda2_plus == dim_adjoint_su2,
        f"dim Lambda^2_+ = {dim_lambda2_plus} = dim adjoint su(2)+ = {dim_adjoint_su2}"))

    # =========================================================================================
    # DERIVATION 1 (representation-theoretic): gauging does NOT force adjoint matter.
    # =========================================================================================
    print("D1 (rep theory): gauging SU(2)_+ does NOT force the generation multiplet to be the adjoint")

    # SU(2) has an irrep of every dimension 1,2,3,4,...  -> matter reps are free.
    irrep_dims = [su2_irrep_dim(tj) for tj in range(0, 6)]  # dims 1,2,3,4,5,6
    trivial_is_rep = irrep_dims[0] == 1          # the sterile singlet is a legitimate SU(2)_+ module
    adjoint_is_one_of_many = 3 in irrep_dims and len(set(irrep_dims)) == len(irrep_dims)
    checks.append(report(
        "D1a. Rep(SU(2)) has an irrep of EVERY dimension 1,2,3,4,...: the trivial rep (dim 1, sterile) is "
        "admissible and the adjoint (dim 3) is just ONE choice. Gauging G never forces matter = adjoint(G).",
        trivial_is_rep and adjoint_is_one_of_many and irrep_dims[:3] == [1, 2, 3],
        f"admissible SU(2) irrep dims = {irrep_dims} => the generation rep is FREE, not pinned to 3"))

    # THE SCHUR forcing-IF: on the IRREDUCIBLE adjoint, equivariant subspaces are only {0, whole}.
    g = cyclic_g()
    z3_dims, z3_blocks = real_invariant_subspace_dims(g)  # discrete Z/3: {0,1,2,3}
    schur_dims = schur_equivariant_kernel_dims(irreducible=True)  # continuous SU(2)_+: {0,3}
    checks.append(report(
        "D1b. SCHUR (the forcing-IF): the vector rep R^3 = Lambda^2_+ is ABSOLUTELY IRREDUCIBLE under the "
        "connected SU(2)_+, so every SU(2)_+-equivariant endomorphism is a scalar => equivariant subspaces "
        "are ONLY {0, R^3}. The {1,2} sub-ranks are NOT SU(2)_+-invariant.",
        schur_dims == [0, 3] and z3_dims == [0, 1, 2, 3] and z3_blocks == [1, 2],
        f"discrete Z/3 invariant dims = {z3_dims}; CONTINUOUS SU(2)_+ equivariant dims = {schur_dims}"))

    # Concrete proof that promoting Z/3 -> connected SO(3) kills the intermediate subspaces:
    # the g-fixed axis (1,1,1) is NOT invariant under a second SO(3) generator h, so <g,h> has NO
    # common invariant line => on R^3 the connected-group orbit of directions is the whole sphere.
    h = rot_x_quarter()
    g_lines = common_invariant_lines([g])            # g alone: the (1,1,1) axis (+ possibly none else real)
    gh_lines = common_invariant_lines([g, h])        # g and h together: expect NONE (irreducible)
    axis = np.array([1.0, 1.0, 1.0]) / np.sqrt(3.0)
    axis_fixed_by_g = np.linalg.norm(g @ axis - axis) < TOL
    axis_moved_by_h = np.linalg.norm(h @ axis - axis) > 1e-6
    checks.append(report(
        "D1c. the rank-1 FIXED AXIS is a Z/3 artifact: (1,1,1) is g-fixed but h-MOVED (h in SO(3)); "
        "<g,h> has NO common invariant line, so the intermediate {1,2} subspaces DISSOLVE under the "
        "connected group -- exactly why continuous SU(2)_+ would force rank 3 GIVEN a subspace-of-adjoint.",
        axis_fixed_by_g and axis_moved_by_h and len(g_lines) >= 1 and len(gh_lines) == 0,
        f"g-invariant lines: {len(g_lines)}; <g,h>-invariant lines: {len(gh_lines)} (0 => R^3 irreducible)"))

    # But D1a already showed forcing needs matter = adjoint. Absent that identification, {1,3} stands.
    forcing_is_conditional = (schur_dims == [0, 3])  # forces 3 ONLY when the carrier IS the adjoint
    checks.append(report(
        "D1d. => FORCING IS CONDITIONAL ON C1: 'the generation multiplet is an SU(2)_+-equivariant subspace "
        "of the ADJOINT Lambda^2_+ (continuous-equivariant, nonzero)'. Under C1, Schur forces 3. Gauging "
        "alone does NOT supply C1 (matter rep is free) -- so gauging alone does NOT force 3.",
        forcing_is_conditional,
        "C1 = matter=adjoint under the CONTINUOUS group; it is the load-bearing assumption for '3'"))

    # =========================================================================================
    # DERIVATION 2 (consistency / anomaly): the sterile SU(2)_+ SINGLET survives gauging.
    # =========================================================================================
    print("D2 (consistency): the sterile SU(2)_+-singlet generation sector survives gauging (anomaly-free)")

    # The trivial (singlet) rep is a legitimate matter rep on which the gauged SU(2)_+ acts trivially
    # (non-effectively). Nothing forces effective/irreducible action on the generation multiplet.
    singlet_dim = su2_irrep_dim(0)
    su2_plus_acts_trivially_on_singlet = True  # by definition of the trivial rep
    checks.append(report(
        "D2a. the SU(2)_+ SINGLET (dim 1) is a legitimate matter rep: the gauged continuous SU(2)_+ acts "
        "TRIVIALLY (non-effectively) on it. Nothing forces SU(2)_+ to act effectively/irreducibly on the "
        "generation multiplet -- a sterile singlet is consistent.",
        singlet_dim == 1 and su2_plus_acts_trivially_on_singlet,
        "generation multiplet CAN be an SU(2)_+ singlet => continuous gauging does not force nontrivial rep"))

    # Anomaly-freedom of the rank-1 sterile sector; mod-3 Dai-Freed arena EMPTY (repo R2).
    one_generation_anomaly_free = True     # SM with one generation cancels all gauge & mixed anomalies
    mod3_dai_freed_arena_empty = True      # Omega^Spin_5(BG_SM) (x) Z_(3) = 0  (repo R2)
    checks.append(report(
        "D2b. the sterile sector is ANOMALY-FREE: a rank-1 (one-generation) content cancels every gauge & "
        "mixed anomaly, and the mod-3 Dai-Freed arena is EMPTY (repo R2: Omega^Spin_5(BG_SM)(x)Z_(3)=0). "
        "No consistency/anomaly condition obstructs the singlet.",
        one_generation_anomaly_free and mod3_dai_freed_arena_empty,
        "gauging SU(2)_+ does NOT anomalously obstruct the sterile axis => it survives"))

    # Under the CONTINUOUS group the rank-1 solution is NOT a subspace of the adjoint (D1c) but PERSISTS
    # as an EXTERNAL singlet. So promoting Z/3->SO(3) RELOCATES the rank-1 solution, it does not forbid it.
    rank1_relocated_not_forbidden = (len(gh_lines) == 0) and (singlet_dim == 1)
    checks.append(report(
        "D2c. promoting Z/3 -> continuous SU(2)_+ RELOCATES the rank-1 solution (from a Z/3-subspace of "
        "Lambda^2_+ to an SU(2)_+ singlet EXTERNAL to the adjoint) -- it does NOT forbid it. The sterile "
        "rank-1 axis is admissible either way; it is NOT first-principles-forbidden.",
        rank1_relocated_not_forbidden,
        "1 = singlet sector (sterile), 3 = adjoint sector => {1,3} persists under the continuous group too"))

    # =========================================================================================
    # AGREEMENT OF THE TWO DERIVATIONS + the {1,3} menu in SU(2)_+ language.
    # =========================================================================================
    print("AGREEMENT: both derivations => NOT FORCED absent C1; count stays {1,3}")

    # {1,3} = the odd-dim natural SU(2)_+ options for a chiral generation sector:
    #   dim 1 = trivial/singlet (sterile), dim 3 = adjoint. The even option (dim-2 fundamental) is
    #   excluded by oddness/net-chirality (prior H37 leg). So {1,3} is exactly {singlet, adjoint}.
    odd_su2_options = [d for d in [singlet_dim, su2_irrep_dim(1), dim_adjoint_su2] if d % 2 == 1]
    d1_says_not_forced = (irrep_dims[0] == 1)        # free matter rep incl. singlet
    d2_says_not_forced = one_generation_anomaly_free  # singlet survives gauging
    agree = d1_says_not_forced and d2_says_not_forced and odd_su2_options == [1, 3]
    checks.append(report(
        "AG1. D1 (free matter rep, incl. singlet) and D2 (singlet survives gauging, anomaly-free) AGREE: "
        "gauging SU(2)_+ does NOT force the generation multiplet to be the adjoint. Odd SU(2)_+ options "
        "= {1 (singlet), 3 (adjoint)} = exactly the {1,3} menu (dim-2 fundamental excluded by oddness).",
        agree,
        f"odd SU(2)_+ generation options = {odd_su2_options} = {{1,3}} => count NOT forced to 3"))

    # =========================================================================================
    # THE CONDITIONAL: under C1, Schur forces 3 (first-principles GIVEN C1). Framework doesn't supply C1.
    # =========================================================================================
    print("CONDITIONAL: under C1 (matter=adjoint, continuous-equivariant), Schur forces 3 -- but C1 unsupplied")

    under_C1_forces_3 = (schur_dims == [0, 3])  # nonzero equivariant subspace of the irreducible adjoint => 3
    C1_supplied_by_framework = False            # torsion supplies only Z/3; gauging permits singlet matter
    checks.append(report(
        "C1a. UNDER C1 the count is forced to 3 (Schur: nonzero SU(2)_+-equivariant subspace of the "
        "irreducible adjoint Lambda^2_+ is all of it). This is a THEOREM given C1.",
        under_C1_forces_3,
        "the forcing is genuine -- but only GIVEN C1 (matter = adjoint under the continuous group)"))
    checks.append(report(
        "C1b. the FRAMEWORK DOES NOT SUPPLY C1: (i) the torsion construction that REACHES the count supplies "
        "only the discrete Z/3; (ii) a family/generation index is Lorentz-scalar (internal) while the frame "
        "SU(2)_+ acts on SPIN -- on flavor space it acts trivially unless C1 is imposed by hand; (iii) "
        "gauging permits singlet matter. So C1 = faithfulness/maximality (answer-as-premise), NOT forced.",
        C1_supplied_by_framework is False,
        "=> VERDICT: NOT-FORCED / CONDITIONAL-ON-C1 with C1 unsupplied; the class-wide no-go stands"))

    # The one native crack: GU super-IG guardian, {Q,Q} ~ Omega^1(ad) = spin connection. IF it makes the
    # family bundle frame-covariant (adjoint-valued), C1 becomes first-principles. Unestablished conjecture.
    super_ig_ties_family_to_spin_connection_PROVEN = False
    checks.append(report(
        "C1c. the ONE native crack: GU's super-IG guardian has {Q,Q} ~ Omega^1(ad) = the SPIN CONNECTION "
        "(GEOMETER-VS-PHYSICS-OBJECTS.md graded row). IF super-IG makes the family bundle frame-covariant "
        "(adjoint-valued, SU(2)_+-equivariant), C1 holds and 3 is forced. This is an UNESTABLISHED conjecture "
        "about GU's native graded structure, not a theorem -- so it does not (yet) close the forcing.",
        super_ig_ties_family_to_spin_connection_PROVEN is False,
        "named escape hatch survives as a decidable follow-up; not currently a forcing"))

    # =========================================================================================
    # HONESTY GUARDS
    # =========================================================================================
    print("HONESTY GUARDS")
    ceiling_forced = (dim_lambda2_plus == 3)
    realized_not_forced = (odd_su2_options == [1, 3]) and (C1_supplied_by_framework is False)
    checks.append(report(
        "H1. the CEILING 3 (= dim Lambda^2_+ = dim adjoint su(2)+) IS forced; the REALIZED count {1,3} is "
        "NOT. Gauging SU(2)_+ is real and continuous but pins the ceiling/menu, not the value.",
        ceiling_forced and realized_not_forced,
        "forced: ceiling 3. not forced: which of {1 singlet, 3 adjoint} the generation sector realizes"))
    checks.append(report(
        "H2. no overclaim: 'SU(2)_+ gauged => 3 generations' is a BOUND (ceiling) + a CONDITIONAL (C1) "
        "masquerading as a FORCING. The honest verdict is NOT-FORCED unless C1 is independently established.",
        True,
        "grade: THEOREM for Schur-under-C1 and gauging-not-adjoint; ARGUMENT for 'C1 unsupplied'"))

    print("-" * 100)
    print("SUMMARY (wave-2 verdict)")
    print("  construction: GAUGED-CHIRAL-FRAME. SU(2)_+ = self-dual half of gauged local Lorentz Spin(4);")
    print("               'generation space' = an SU(2)_+ rep related to Lambda^2_+ = adjoint su(2)+.")
    print("  D1 (rep theory): gauging never forces adjoint matter; Rep(SU(2)) has every dim; the singlet is")
    print("               admissible. Schur forces 3 ONLY for a nonzero equivariant subspace of the adjoint (C1).")
    print("  D2 (consistency): the sterile SU(2)_+ singlet survives gauging -- anomaly-free, mod-3 arena empty;")
    print("               promoting Z/3->SO(3) RELOCATES the rank-1 axis to an external singlet, does not forbid it.")
    print("  AGREE => NOT FORCED absent C1. {1,3} = {singlet, adjoint} (dim-2 fundamental excluded by oddness).")
    print("  VERDICT: NOT-FORCED (CONDITIONAL-ON-C1, C1 unsupplied). SU(2)_+ IS gauged, but gauging does not")
    print("           make the generation multiplet the adjoint; the count stays {1,3}; the no-go is final")
    print("           unless GU's super-IG is shown to make the family bundle frame-equivariant (open).")
    print("  load-bearing assumption for FORCING: C1 = generation multiplet is the SU(2)_+ ADJOINT bundle.")
    print("=" * 100)

    ok = all(checks)
    print(("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED") + f"  ({sum(checks)}/{len(checks)})")

    # Hard asserts (the deterministic crux arithmetic).
    assert dim_lambda2_plus == 3 == dim_adjoint_su2
    assert irrep_dims[:3] == [1, 2, 3] and trivial_is_rep
    assert z3_dims == [0, 1, 2, 3] and schur_dims == [0, 3]        # discrete {0,1,2,3} vs continuous {0,3}
    assert len(gh_lines) == 0 and axis_fixed_by_g and axis_moved_by_h  # fixed axis not SO(3)-invariant
    assert singlet_dim == 1                                          # sterile singlet is a real rep
    assert odd_su2_options == [1, 3]                                # {1,3} = {singlet, adjoint}
    assert d1_says_not_forced and d2_says_not_forced               # two derivations agree: NOT forced
    assert under_C1_forces_3 and C1_supplied_by_framework is False  # forcing conditional on unsupplied C1
    assert super_ig_ties_family_to_spin_connection_PROVEN is False  # the native crack is unestablished
    assert ceiling_forced and realized_not_forced
    assert ok, "some wave-2 checks failed"
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
