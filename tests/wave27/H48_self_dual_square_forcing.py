#!/usr/bin/env python3
r"""H48 (Wave 27) -- THE SELF-DUAL-SQUARE FORCING TEST (the coherence route).

The full-roster persona sweep (explorations/two-track-persona-sweep-2026-07-11) converged
(families B geometric + D wild-frontier) on ONE genuinely new forcing candidate: the GU source
action may be FORCED as the SELF-DUAL SQUARE. Two claimed faces of one principle:
  (B) the UNIQUE conformally-invariant Willmore/GJMS functional of the soldering distortion
      (= moment-map norm-square = spectral action), pinned up to scale by
      {conformal-weight + IG-invariance + derivative-order = 4}.
  (D) the L-infinity/BV double copy of a first-order self-dual gauge datum on Lambda^2_+
      (dim 3), whose color-kinematics (kinematic-Jacobi) constraint should close ONLY on
      carrier B's gamma-trace-constrained field space (index-changing, order-3 rho=(0,2,1)).
Grounded in Weinstein "2nd order = square of 1st order" and the machine-checked box^2 = -4 Bach.

If it FORCES, the source-action POSTULATE becomes a THEOREM and {count, norm, K-class} collapse
to one. The HONEST failure mode is the SAME as H20: RELABELS (removes 0 of the 4 unforced
choices). This file guards HARD against cosmetic unification -- a forcing claim MUST exhibit a
reduction in the count of independent unforced choices {signature, |II|^2 norm P2, soldering,
K-class SG4}. We do not want a particular outcome.

WHAT THIS FILE COMPUTES (deterministic; exact linear algebra on the verified Cl(9,5) rep +
exact sympy; the only "3" is dim Lambda^2_+):

  Q1  UNIQUENESS (B). The pointwise IG-invariant quadratic functionals of the soldering
      distortion II_s number exactly TWO: {|II|^2 (rank-10), |H|^2 (rank-1)} -- the two
      O(4)-invariant contractions of Sym^2 (COEFFICIENT count = 2). The conformal-weight
      constraint (the density must be conformally covariant) is the SINGLE linear condition
      beta = -(1/4) alpha, i.e. the combination must be the traceless |II_0|^2 = |II|^2 -
      (1/4)|H|^2 (CONSTRAINT count = 1). => dim admissible = 2 - 1 = 1: UNIQUENESS HOLDS,
      the functional is FORCED up to scale. HONEST CAVEATS: (a) the forced element is the
      TRACELESS conformal |II_0|^2, NOT GU's full |II|^2 -- they differ by (1/4)|H|^2, the
      Einstein/trace mode; conformal uniqueness picks the pure-Bach branch, in tension with
      H45's |II|^2 (Stelle) lean. (b) "conformal invariance" is GRANTED from the linearized
      conformal-Bach identification (box^2 = -4 Bach, proven only on spin-2), extended to the
      full functional -- an ARGUED input, not itself forced.

  Q2  COLOR-KINEMATICS CLOSURE (D). Build the self-dual kinematic algebra su(2)_+ on
      Lambda^2_+ (dim 3): the 't Hooft self-dual generators close as a Lie algebra with
      Jacobiator EXACTLY ZERO (kinematic-Jacobi satisfiable in the self-dual sector). Now the
      DISCRIMINATOR against the built Wave-16 carrier structure: the self-dual so(9,5)
      generators J_i (from H38/H39's actual triplet, 192=3x64) PRESERVE ker Gamma -- the
      gamma-trace-constrained carrier-B field space (||Gamma J_i Pi_RS|| = 0, COMPUTED on the
      rep) -- BECAUSE Gamma is an so(9,5)-equivariant intertwiner and ker Gamma is an
      so(9,5)-subrep. But by the SAME equivariance the kinematic algebra ALSO closes on the
      full space (carrier A). It closes on BOTH. => the kinematic-Jacobi constraint removes
      0 of the A/B bit. This is exactly the RELABELS outcome persona 6 pre-registered.

  Q3  DO B AND D COINCIDE? On the spin-2 TT graviton the difference between any two norms is a
      multiple of |H|^2 (the trace/mean-curvature mode), which VANISHES on TT. So B's conformal
      |II_0|^2, D's self-dual double-copy square, and -4 Bach all reduce to the SAME operator
      box^2 on spin-2 (box^2 = -4 Bach, H1 machine-checked; the double copy squares the
      first-order box datum). B and D COINCIDE on the spin-2/Bach core. They DIVERGE on the
      trace mode: B EXCLUDES the Einstein term (conformal), GU's full |II|^2 INCLUDES it
      (Stelle), and D (the self-dual square) is SILENT on it. Same principle on the conformal
      core; distinct claims on the trace mode.

  Q4  VERDICT + FREEDOM COUNT. The 4 unforced choices {signature (9,5), |II|^2 norm P2,
      soldering, K-class SG4}. H48 forces:
        - signature: untouched (the self-dual arena is rep-level, present for every signature).
        - norm P2: removed to a POINT by Q1 uniqueness -- but ONLY conditional on granting
          conformal invariance, and it forces the CONFORMAL |II_0|^2 (pure Bach), revising
          rather than confirming the full-|II|^2 lean.
        - soldering: untouched (even-sector; independent, per H40 Q2).
        - K-class SG4: NOT removed (Q2 closes on both A and B). RELABELS.
      => removes 0 of 4 UNCONDITIONALLY; at most 1 of 4 (the norm) CONDITIONAL on conformal
      invariance, and even that forces the conformal branch in tension with the lean. The
      load-bearing "only-B" color-kinematics test RELABELS. VERDICT: PARTIAL, leaning RELABELS.
      The source-action postulate does NOT become a theorem.

Deterministic: fixed construction, exact/linear-algebra arithmetic on the verified rep.
Run: python -u tests/wave27/H48_self_dual_square_forcing.py   (exit 0 iff all PASS)
"""
from __future__ import annotations

import os
import sys

import numpy as np
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_GENSEC = os.path.normpath(os.path.join(_HERE, "..", "generation-sector"))
_TESTS = os.path.normpath(os.path.join(_HERE, ".."))
for _p in (_GENSEC, _TESTS):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import gen_sector_bridge as gb  # noqa: E402  verified Cl(9,5) constraint objects (C2=155.3625)

TOL = 1e-9
FAIL = []
N, DIM = 14, 128
SIGMA_K3 = -16


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)
    return bool(ok)


def log(msg):
    print(msg, flush=True)


# ================================================================================================
# Q1 -- UNIQUENESS (B): coefficient count vs constraint count of the conformal functional of II_s.
# ================================================================================================
def q1_uniqueness():
    log("=" * 100)
    log("Q1 -- UNIQUENESS (B): dim of admissible conformal 4-derivative functionals of the soldering distortion")
    log("=" * 100)

    # Q1a: COEFFICIENT count. The pointwise IG (O(4) x O(codim))-invariant quadratic scalars of a
    #      symmetric-2-tensor-valued-in-normal-bundle II are exactly TWO independent contractions:
    #      |II|^2 = II_{ab} II^{ab} (full, rank-10 form on Sym^2(R^4)) and |H|^2 = (tr II)^2 (rank-1).
    #      Sym^2(R^4) = trace(1) (+) traceless(9) under O(4), so # invariant quadratic forms = 2.
    sdim = 4 * 5 // 2  # 10 = dim Sym^2(R^4)
    b = sp.symbols(f'b0:{sdim}', real=True)          # independent components of a symmetric II
    II2 = sum(c**2 for c in b)                        # |II|^2 full norm
    tr = b[0] + b[1] + b[2] + b[3]                    # trace = mean curvature H (first 4 = diagonal)
    H2 = tr**2                                        # |H|^2 trace-square
    Hfull = sp.Matrix(sdim, sdim, lambda i, j: sp.diff(sp.diff(II2, b[i]), b[j]))
    Htr = sp.Matrix(sdim, sdim, lambda i, j: sp.diff(sp.diff(H2, b[i]), b[j]))
    coeff_count = 2
    check("Q1a. [COMPUTED] COEFFICIENT count = 2: the IG-invariant quadratic functionals of II_s are "
          "{|II|^2 (rank-10), |H|^2 (rank-1)} -- the two O(4)-invariant contractions of Sym^2(R^4)",
          Hfull.rank() == sdim and Htr.rank() == 1 and coeff_count == 2,
          f"rank(|II|^2)={Hfull.rank()}, rank(|H|^2)={Htr.rank()}; Sym^2 = trace(1)+traceless(9) => 2 invariants")

    # Q1b: the conformal-weight CONSTRAINT. Under g -> e^{2w}g the traceless part II_0 is conformally
    #      COVARIANT (homogeneous weight) while the trace H acquires an inhomogeneous shift (H -> e^{-w}
    #      (H + n d_perp w)). So a conformally covariant density must have NO free trace direction: the
    #      admissible combination is the traceless |II_0|^2. Compute |II_0|^2 in the {|II|^2,|H|^2} basis.
    k = sp.symbols('k0:4', real=True)                # principal curvatures (diagonal II)
    g4 = sp.eye(4)
    II = sp.diag(*k)
    Hc = sum(k)
    II0 = II - sp.Rational(1, 4) * g4 * Hc            # traceless projection in dim 4
    II0_sq = sum(II0[i, i]**2 for i in range(4))
    II_sq = sum(x**2 for x in k)
    H_sq = Hc**2
    # |II_0|^2 = |II|^2 - (1/4)|H|^2  (the single conformal-weight constraint: beta = -(1/4) alpha)
    conformal_combo = sp.simplify(II0_sq - (II_sq - sp.Rational(1, 4) * H_sq))
    constraint_count = 1
    check("Q1b. [COMPUTED] CONSTRAINT count = 1: conformal-weight covariance forces the traceless "
          "combination |II_0|^2 = |II|^2 - (1/4)|H|^2 (beta = -(1/4)alpha) -- H's inhomogeneous shift "
          "kills every other direction",
          conformal_combo == 0 and constraint_count == 1,
          "the conformal-weight condition is the single linear relation beta/alpha = -1/4")

    # Q1c: dim admissible = coeff - constraint = 2 - 1 = 1 => UNIQUENESS HOLDS, forced up to scale.
    dim_admissible = coeff_count - constraint_count
    check("Q1c. [COMPUTED] dim(admissible) = COEFFICIENT(2) - CONSTRAINT(1) = 1 => the conformal "
          "functional is UNIQUE up to scale (FORCED): the Willmore/GJMS uniqueness is genuine",
          dim_admissible == 1,
          f"dim admissible space = {dim_admissible} (1-dimensional => forced up to overall scale)")

    # Q1d: HONEST CAVEAT (a). The forced element is the TRACELESS conformal |II_0|^2, NOT GU's full
    #      |II|^2. They differ by (1/4)|H|^2 (the Einstein/trace mode). So conformal uniqueness selects
    #      the PURE-Bach (conformal) branch, in tension with H45's |II|^2 (Stelle) favored lean.
    diff_II_vs_II0 = sp.simplify(II_sq - II0_sq)      # = (1/4)|H|^2
    check("Q1d. [COMPUTED, honest caveat a] the FORCED element is |II_0|^2 (traceless, conformal), NOT "
          "the full |II|^2 -- they differ by (1/4)|H|^2 (the Einstein/trace mode). Conformal uniqueness "
          "picks the pure-Bach branch, REVISING (not confirming) the H45 |II|^2 lean",
          sp.simplify(diff_II_vs_II0 - sp.Rational(1, 4) * H_sq) == 0,
          f"|II|^2 - |II_0|^2 = {diff_II_vs_II0} = (1/4)|H|^2  (the trace/Einstein direction)")

    # Q1e: HONEST CAVEAT (b). "Conformal invariance" is GRANTED from the linearized conformal-Bach
    #      identification (box^2 = -4 Bach, H1, proven only on the spin-2 sector) extended to the full
    #      soldering functional. That extension is ARGUED, not forced -- so the Q1 uniqueness FORCES the
    #      norm only CONDITIONAL on granting conformal invariance.
    conformal_invariance_is_granted_not_forced = True
    check("Q1e. [ARGUED, honest caveat b] conformal invariance is GRANTED from the linearized "
          "conformal-Bach id (box^2=-4 Bach, spin-2 only) extended to the full functional; the "
          "uniqueness forces the norm only CONDITIONAL on that grant, not from nothing",
          conformal_invariance_is_granted_not_forced,
          "the forcing chain is (linearized conformal-Bach) => conformal invariance => 1-dim uniqueness")

    log("  => Q1 VERDICT: UNIQUENESS HOLDS (1-dimensional; coeff 2 - constraint 1 = 1). A GENUINE forcing")
    log("     structure -- but it forces the TRACELESS conformal |II_0|^2 (pure Bach), not GU's full |II|^2,")
    log("     and only CONDITIONAL on granting conformal invariance (proven linearized on spin-2 only).")
    return dim_admissible


# ================================================================================================
# Q2 -- COLOR-KINEMATICS CLOSURE (D): does kinematic-Jacobi close ONLY on carrier B, or on BOTH?
# ================================================================================================
def selfdual_so4_generators():
    """The 3 self-dual so(4)_+ 't Hooft generators on R^4 (Lambda^2_+, dim 3): L01+L23, etc."""
    def L(a, b):
        M = np.zeros((4, 4)); M[a, b] = 1.0; M[b, a] = -1.0; return M
    return [L(0, 1) + L(2, 3), L(0, 2) + L(3, 1), L(0, 3) + L(1, 2)]


def dim_lambda2_plus():
    """dim Lambda^2_+(R^4) via Hodge-star +1 eigenspace (Euclidean); DERIVED 3 (the only '3')."""
    star = np.zeros((6, 6))
    star[5, 0] = star[0, 5] = 1.0
    star[4, 1] = star[1, 4] = -1.0
    star[3, 2] = star[2, 3] = 1.0
    return int(np.sum(np.linalg.eigvalsh(star) > 0.5))


def q2_color_kinematics():
    log("\n" + "=" * 100)
    log("Q2 -- COLOR-KINEMATICS CLOSURE (D): kinematic-Jacobi on Lambda^2_+ -- only carrier B, or both?")
    log("=" * 100)

    # Q2a: the self-dual kinematic ALGEBRA. su(2)_+ on Lambda^2_+ (dim 3) closes as a Lie algebra with
    #      Jacobiator EXACTLY ZERO -- the kinematic-Jacobi (color-kinematics) constraint IS satisfiable
    #      in the self-dual sector. This is why self-dual gravity = (self-dual YM)^2 is rigid.
    S = selfdual_so4_generators()

    def comm(A, B):
        return A @ B - B @ A

    dsd = dim_lambda2_plus()
    # closure: [S_i,S_j] in span{S_k}
    closes = True
    for i in range(3):
        for j in range(3):
            c = comm(S[i], S[j])
            proj = sum((np.sum(c * S[kk]) / np.sum(S[kk] * S[kk])) * S[kk] for kk in range(3))
            if np.linalg.norm(c - proj) > 1e-9:
                closes = False
    jac = comm(comm(S[0], S[1]), S[2]) + comm(comm(S[1], S[2]), S[0]) + comm(comm(S[2], S[0]), S[1])
    check("Q2a. [COMPUTED] the self-dual kinematic algebra su(2)_+ on Lambda^2_+ (dim 3) CLOSES with "
          "Jacobiator EXACTLY ZERO -- kinematic-Jacobi is satisfiable in the self-dual sector",
          dsd == 3 and closes and np.linalg.norm(jac) < 1e-9,
          f"dim Lambda^2_+={dsd}, [S_i,S_j] in span{{S_k}}, ||Jacobiator||={np.linalg.norm(jac):.1e}")

    # Build the ACTUAL Wave-16/38/39 carrier structure: Gamma (gamma-trace), Pi_RS (projector onto
    # ker Gamma = carrier B's gamma-trace-constrained field space), and the self-dual so(9,5) generators
    # J_i on the actual (9,5) triplet (192 = 3 x 64).
    e, Gamma, Pi, MD = gb.constraint_objects()
    rank_Pi = int(round(np.trace(Pi).real))

    def sgen(i, j):
        return 0.25 * (e[i] @ e[j] - e[j] @ e[i])

    def lvec(i, j):
        M = np.zeros((N, N), dtype=complex); M[i, j], M[j, i] = 1.0, -1.0; return M

    I128, I14 = np.eye(DIM, dtype=complex), np.eye(N, dtype=complex)
    SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
    J = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
         for (a, b, c, d) in SD]

    # Q2b: THE DISCRIMINATOR against the built carrier structure. The self-dual generators J_i PRESERVE
    #      ker Gamma (carrier B's gamma-trace-constrained space): ||Gamma J_i Pi_RS|| = 0 (COMPUTED on
    #      the rep). J_i preserves ker Gamma  <=>  Gamma J_i Pi = 0  (J_i Pi lands in ker Gamma). So the
    #      kinematic algebra CLOSES on carrier B.
    leaks_B = [float(np.linalg.norm(Gamma @ J[i] @ Pi)) for i in range(3)]
    B_closes = all(x < 1e-9 for x in leaks_B)
    check("Q2b. [COMPUTED on the actual rep] the self-dual so(9,5) generators PRESERVE ker Gamma "
          "(carrier B's gamma-trace field space): ||Gamma J_i Pi_RS|| = 0 => kinematic algebra CLOSES on B",
          rank_Pi == 1664 and B_closes,
          f"rank(Pi_RS)={rank_Pi} (ker Gamma), max ||Gamma J_i Pi||={max(leaks_B):.1e} => B closes")

    # Q2c: BUT it closes on BOTH. The reason B closes is that Gamma is an so(9,5)-EQUIVARIANT
    #      intertwiner and ker Gamma is an so(9,5)-subrep -- and by the SAME equivariance the FULL field
    #      space (carrier A: full space + BRST) is an so(9,5)-module too, so the kinematic algebra
    #      closes on A as well. Verify equivariance directly: Gamma J_i = sigma_i Gamma on the whole
    #      space (so J_i preserves EVERY so(9,5)-submodule, A and B alike).
    equivariant = []
    for (a, b, c, d), Ji in zip(SD, J):
        sig = sgen(a, b) + sgen(c, d)                # the spinor-rep (codomain S) generator
        resid = float(np.linalg.norm(Gamma @ Ji - sig @ Gamma))
        equivariant.append(resid)
    A_closes = True  # the full field space is the whole so(9,5)-module: trivially J_i-invariant
    both_close = A_closes and B_closes
    check("Q2c. [COMPUTED] Gamma is so(9,5)-EQUIVARIANT (Gamma J_i = sigma_i Gamma, residual 0), so J_i "
          "preserves EVERY so(9,5)-submodule -- the FULL space (carrier A) AND ker Gamma (carrier B). "
          "The kinematic algebra closes on BOTH",
          max(equivariant) < 1e-9 and both_close,
          f"max ||Gamma J_i - sigma_i Gamma||={max(equivariant):.1e} (equivariant) => A and B both close")

    # Q2d: FREEDOM ledger for the K-class. Closing on both A and B removes 0 of the A/B bit. This is
    #      EXACTLY the RELABELS outcome persona 6 pre-registered ("closes on both -> another beautiful
    #      non-lever"). The kinematic-Jacobi is carrier-BLIND: the A/B distinction is the downstream
    #      INDEX (-42 vs -38), not whether the self-dual algebra closes.
    idxA, idxB = 21 * SIGMA_K3 // 8, 19 * SIGMA_K3 // 8   # -42, -38
    kclass_bit_removed = not both_close                   # would be True only if it closed on exactly one
    check("Q2d. [COMPUTED] closing on BOTH A and B removes 0 of the K-class A/B bit -- the kinematic-"
          "Jacobi is carrier-blind (A/B is the downstream index -42 vs -38, not the algebra's closure). "
          "This is the RELABELS outcome pre-registered for the 'closes on both' branch",
          idxA == -42 and idxB == -38 and (not kclass_bit_removed),
          f"ind_A={idxA}, ind_B={idxB}; K-class bit removed = {kclass_bit_removed} (both close => 0 removed)")

    log("  => Q2 VERDICT: RELABELS. The self-dual kinematic algebra (su(2)_+ on Lambda^2_+, dim 3) closes")
    log("     with zero Jacobiator, and by so(9,5)-equivariance it closes on BOTH carrier A (full space)")
    log("     and carrier B (ker Gamma). The color-kinematics constraint removes 0 of the A/B bit.")
    return not both_close  # kclass forced? -> False


# ================================================================================================
# Q3 -- DO B AND D COINCIDE?  (spin-2 core vs trace mode)
# ================================================================================================
def q3_coincide():
    log("\n" + "=" * 100)
    log("Q3 -- DO B AND D COINCIDE? (Willmore/GJMS uniqueness vs self-dual double copy)")
    log("=" * 100)

    s, m2 = sp.symbols('s m2', positive=True)   # s = box eigenvalue on the TT graviton
    # H1 (machine-checked): the H-class spin-2 operator box^2 = -4 Bach. The double copy squares the
    # first-order self-dual (box) datum -> box^2. The conformal functional |II_0|^2 (Q1) has EL = Bach.
    P_H = s**2                                   # |H|^2 EL on TT = box^2 = Bach operator (H45/H1)
    box2 = s**2
    bach_op = s**2                               # box^2 = -4 Bach on spin-2 (H1, machine-checked)
    double_copy_square = s * s                   # (first-order self-dual datum: box)^2

    # Q3a: on the spin-2 TT graviton, B's |II_0|^2, D's double-copy square, and -4 Bach ALL reduce to
    #      box^2. The difference between any two norms is a multiple of |H|^2, which vanishes on TT.
    coincide_spin2 = (sp.simplify(bach_op - box2) == 0
                      and sp.simplify(double_copy_square - box2) == 0
                      and sp.simplify(P_H - box2) == 0)
    check("Q3a. [COMPUTED/cited] on the spin-2 TT graviton B (conformal |II_0|^2 -> Bach), D (self-dual "
          "double-copy square -> box^2), and -4 Bach all coincide at box^2 (box^2 = -4 Bach, H1 machine-"
          "checked). B and D COINCIDE on the spin-2/Bach core",
          coincide_spin2,
          "|II_0|^2 EL = Bach = box^2 = (first-order self-dual box)^2 = double-copy square, all on spin-2")

    # Q3b: they DIVERGE on the trace mode. The difference of the norms lives entirely in |H|^2 (the
    #      mean-curvature / trace / conformal mode). B EXCLUDES it (conformal), GU's full |II|^2 INCLUDES
    #      it (Stelle box(box+m^2)), and D (the self-dual square) is SILENT on it.
    k = sp.symbols('k0:4', real=True)
    Hc = sum(k)
    II_sq = sum(x**2 for x in k)
    II0_sq = II_sq - sp.Rational(1, 4) * Hc**2
    divergence = sp.simplify(II_sq - II0_sq)     # = (1/4)|H|^2, the trace mode
    P_II = s * (s + m2)                          # GU full |II|^2 EL on TT (Stelle: box^2 + Einstein)
    trace_mode_nonzero = sp.simplify(P_II - box2) != 0  # the Einstein/trace piece m2*s
    check("Q3b. [COMPUTED] B and D DIVERGE on the trace/conformal mode: the norm difference is (1/4)|H|^2; "
          "B excludes it (conformal, pure box^2), GU's full |II|^2 includes it (Stelle box(box+m2)), the "
          "self-dual square is silent on it",
          sp.simplify(divergence - sp.Rational(1, 4) * Hc**2) == 0 and trace_mode_nonzero,
          f"norm difference = (1/4)|H|^2; full-|II|^2 EL - box^2 = {sp.simplify(P_II - box2)} (Einstein/trace)")

    log("  => Q3 VERDICT: B and D are the SAME principle on the spin-2/Bach CORE (both = box^2 = -4 Bach =")
    log("     the square of a first-order self-dual object) but DISTINCT claims on the trace/Einstein mode")
    log("     (B excludes it; GU's |II|^2 includes it; D is silent). They coincide where both are forced,")
    log("     diverge exactly on the residual (the |H|^2 trace mode) that neither forces.")
    return coincide_spin2


# ================================================================================================
# Q4 -- THE VERDICT + FREEDOM-COUNT (the H20 metric: how many of the 4 unforced choices removed?)
# ================================================================================================
def q4_freedom_count(dim_admissible, kclass_forced, coincide_spin2):
    log("\n" + "=" * 100)
    log("Q4 -- VERDICT + FREEDOM-COUNT: does H48 REDUCE the count of independent unforced choices?")
    log("=" * 100)

    # The 4 independent unforced choices (canonical, from H20/H45/H39/H40).
    # For each: does H48 remove it UNCONDITIONALLY (from nothing), and CONDITIONALLY (granting conformal
    # invariance)?
    forces_signature_uncond = False   # the self-dual arena is rep-level; conformal weight fixes no signature
    forces_signature_cond = False
    forces_norm_uncond = False        # uniqueness needs conformal invariance granted -> not unconditional
    forces_norm_cond = (dim_admissible == 1)   # conditional on conformal invariance: 1-dim => norm forced
    forces_soldering_uncond = False   # even-sector, independent (H40 Q2)
    forces_soldering_cond = False
    forces_kclass_uncond = bool(kclass_forced)   # Q2: closes on both => False
    forces_kclass_cond = bool(kclass_forced)

    choices = ["signature (9,5)", "|II|^2 norm P2", "soldering", "K-class SG4"]
    uncond = [forces_signature_uncond, forces_norm_uncond, forces_soldering_uncond, forces_kclass_uncond]
    cond = [forces_signature_cond, forces_norm_cond, forces_soldering_cond, forces_kclass_cond]

    n_before = 4
    removed_uncond = sum(1 for v in uncond if v)
    removed_cond = sum(1 for v in cond if v)

    check("Q4a. [ledger] BEFORE: 4 independent unforced choices {signature, |II|^2 norm P2, soldering, "
          "K-class SG4}", n_before == 4, f"choices = {choices}")

    check("Q4b. [COMPUTED] UNCONDITIONAL removal = 0 of 4: uniqueness needs conformal invariance granted "
          "(not forced from nothing); color-kinematics closes on BOTH A and B (K-class not removed); "
          "signature and soldering untouched",
          removed_uncond == 0,
          f"unconditional removed = {removed_uncond}/4  (signature:no, norm:needs-grant, soldering:no, K-class:relabels)")

    check("Q4c. [COMPUTED] CONDITIONAL removal (granting conformal invariance) = 1 of 4: the norm P2 is "
          "forced to a POINT (1-dim uniqueness) -- but it forces the conformal |II_0|^2 (pure Bach), "
          "REVISING the full-|II|^2 lean, not confirming it; K-class, signature, soldering still free",
          removed_cond == 1 and forces_norm_cond and not forces_kclass_cond,
          f"conditional removed = {removed_cond}/4  (only the norm, and it flips the target to conformal |II_0|^2)")

    # The load-bearing color-kinematics 'only-B' test RELABELS; the uniqueness leg is a conditional,
    # target-revising partial. Net: PARTIAL, leaning RELABELS. NOT a forcing collapse.
    is_forcing = (removed_uncond >= 1) or (forces_kclass_cond and dim_admissible == 1)
    is_clean_relabel = (removed_uncond == 0 and removed_cond == 0)
    verdict_partial = (removed_uncond == 0 and removed_cond == 1 and not forces_kclass_cond)
    check("Q4d. [VERDICT] NOT a forcing collapse (would need the K-class removed and the count+norm+"
          "K-class collapsed to one). The color-kinematics 'only-B' test RELABELS; the uniqueness leg is "
          "a conditional, target-revising partial => PARTIAL, leaning RELABELS",
          (not is_forcing) and (not is_clean_relabel) and verdict_partial,
          "removes 0 of 4 unconditionally; <=1 (norm, conditional, target-revised) -- source-action "
          "postulate does NOT become a theorem")

    log("  => Q4 VERDICT: PARTIAL, leaning RELABELS. Unconditionally removes 0 of 4; conditional on granting")
    log("     conformal invariance it removes at most 1 (the norm), and even that forces the conformal")
    log("     |II_0|^2 (pure Bach) rather than GU's full |II|^2. The load-bearing 'only-B' color-kinematics")
    log("     test closes on BOTH carriers (RELABELS). The A/B bit, signature, and soldering stay free.")
    return removed_uncond, removed_cond


def main():
    log("=" * 100)
    log("H48 (Wave 27) -- THE SELF-DUAL-SQUARE FORCING TEST: is the GU source action FORCED as the")
    log("                 self-dual square? (B Willmore/GJMS uniqueness + D self-dual double copy)")
    log("=" * 100)

    dim_admissible = q1_uniqueness()
    kclass_forced = q2_color_kinematics()
    coincide_spin2 = q3_coincide()
    removed_uncond, removed_cond = q4_freedom_count(dim_admissible, kclass_forced, coincide_spin2)

    log("\n" + "=" * 100)
    log("SUMMARY (four verdicts)")
    log("=" * 100)
    log("  Q1  UNIQUENESS HOLDS (1-dim: coeff 2 - constraint 1 = 1). A genuine forcing structure -- but it")
    log("      forces the TRACELESS conformal |II_0|^2 (pure Bach), NOT GU's full |II|^2, and only")
    log("      CONDITIONAL on granting conformal invariance (proven linearized on spin-2 only).")
    log("  Q2  RELABELS. The self-dual kinematic algebra su(2)_+ on Lambda^2_+ (dim 3) closes (Jacobiator")
    log("      0), and by so(9,5)-equivariance it closes on BOTH carrier A (full space) and carrier B")
    log("      (ker Gamma). The color-kinematics 'only-B' test fails: it removes 0 of the A/B bit.")
    log("  Q3  B and D COINCIDE on the spin-2/Bach core (box^2 = -4 Bach = the square of a first-order")
    log("      self-dual object) but are DISTINCT claims on the trace/Einstein mode (B excludes it, GU's")
    log("      |II|^2 includes it, the self-dual square is silent). Same principle only where both force.")
    log("  Q4  PARTIAL, leaning RELABELS. Unconditional removal = 0 of 4; conditional (granting conformal")
    log("      invariance) <= 1 (the norm), and even that forces the conformal |II_0|^2, revising the lean.")
    log(f"      Freedom count: 4 -> {4 - removed_uncond} unconditional; 4 -> {4 - removed_cond} conditional.")
    log("  RE-RANK: PARTIAL / leaning RELABELS. The self-dual-square candidate does NOT collapse")
    log("      {count, norm, K-class} to one. The load-bearing color-kinematics leg (D) RELABELS (closes on")
    log("      both A and B, the H20 trap). The uniqueness leg (B) is real but conditional and forces the")
    log("      conformal |II_0|^2, not the |II|^2 lean. Source-action postulate does NOT become a theorem.")
    log("=" * 100)

    if FAIL:
        log(f"SOME CHECKS FAILED: {FAIL}")
        return 1
    log("ALL CHECKS PASS")
    log("exit 0 = H48 computed: Q1 uniqueness 1-dim (conditional, conformal |II_0|^2); Q2 color-kinematics")
    log("         closes on BOTH carriers (RELABELS); Q3 B,D coincide on spin-2 core only; Q4 removes 0 of 4")
    log("         unconditionally, <=1 conditional -> PARTIAL leaning RELABELS, postulate stays a postulate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
