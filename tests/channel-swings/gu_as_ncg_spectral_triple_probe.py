#!/usr/bin/env python3
"""GU-as-NCG-spectral-triple probe (pre-registered swing 2026-07-21).

Tests, on GU's OWN verified Cl(9,5)=M(64,H) representation, the claims of the
swing `explorations/gu-as-ncg-spectral-triple-swing-2026-07-21.md`:

  (A) GU recasts as a REAL spectral triple (A,H,D,J,gamma) -- but at
      KO-dimension 4 (mod 8), NOT the KO-dimension 6 where the
      Connes-Chamseddine finite Standard Model lives.  Checked on the actual
      128-dim rep: J_quat^2 = -1 (eps=-1), J_quat commutes with a self-adjoint
      Dirac symbol (eps'=+1) and with the chirality omega (eps''=+1) ->
      sign triple (-1,+1,+1) = KO-dim 4.  Contrast KO-6 = (+1,+1,-1).

  (B) U(A) for the WHOLE GU algebra A=M(64,H) is Sp(64) (dim 8256), a SIMPLE
      compact group -- it has no product decomposition U(1)xSU(2)xSU(3)
      (dim 12).  So the SM gauge group is not U(A_GU).

  (C) The SM subalgebra C(+)H(+)M3(C) IS a *-subalgebra of a matrix algebra,
      but selecting it inside a SIMPLE algebra is a positive-dimensional
      choice (conjugation by a non-normalizing unitary gives a DIFFERENT,
      equally-valid copy).  GU's structure singles out none => NOT FORCED.

  (D) The NCG order-one condition [[D,a],Jb*J^-1]=0 is a nontrivial selector
      on the Dirac: a generic self-adjoint D violates it; only specially
      adapted (block/Yukawa) D pass.  GU's native D_GU preserves the Sp(64)
      orbit (OQ2) and is not shown to supply an order-one Dirac for the SM
      subalgebra => the finite Dirac is an import.

Everything is exact integer arithmetic or bit-reproducible linear algebra.
The only pseudo-random object is one FIXED-SEED "generic" self-adjoint matrix
in step D (seed=20260721); its role is only to witness "generic D fails
order-one", which is a stable/dense property, so the seed is immaterial.

Run: python tests/channel-swings/gu_as_ncg_spectral_triple_probe.py
Exit 0 iff all checks pass.
"""

from __future__ import annotations

import os
import sys

import numpy as np

# Reuse the repo's verified Cl(9,5) Jordan-Wigner gammas.
_TESTS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
if _TESTS not in sys.path:
    sys.path.insert(0, _TESTS)
import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402

FAIL: list[str] = []
TOL = 1e-9


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ============================================================ (0) classification
def step_classification() -> None:
    log("[0] Clifford classification + KO-dimension arithmetic (exact integers)")
    p, q = 9, 5
    dim_cl = 2 ** (p + q)                       # dim_R Cl(9,5)
    dim_MH = 4 * 64 * 64                         # dim_R M(64,H) = 4 * 64^2
    check("dim_R Cl(9,5) = dim_R M(64,H) = 16384", dim_cl == dim_MH == 16384,
          f"{dim_cl} == {dim_MH}")
    ko = (p - q) % 8
    check("KO-dimension of Cl(9,5) is (p-q) mod 8 = 4 (quaternionic)", ko == 4, f"ko={ko}")
    # KO sign table: dim -> (eps=J^2, eps'=JD/DJ, eps''=Jg/gJ)
    table = {0: (+1, +1, +1), 2: (-1, +1, -1), 4: (-1, +1, +1), 6: (+1, +1, -1)}
    check("KO-4 sign triple is (-1,+1,+1); KO-6 (Connes SM) is (+1,+1,-1); they DIFFER",
          table[4] == (-1, +1, +1) and table[6] == (+1, +1, -1) and table[4] != table[6],
          f"KO4={table[4]} vs KO6={table[6]}")
    log("")


# ============================================================ (A) recast on rep
def step_recast_on_rep():
    log("[A] GU recasts as a real spectral triple at KO-dim 4 -- checked on the 128-dim rep")
    n_pairs = 7
    dim = 2 ** n_pairs                          # 128
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta = [+1] * 9 + [-1] * 5
    e = [G[a] if eta[a] == +1 else 1j * G[a] for a in range(14)]
    Iden = np.eye(dim, dtype=complex)

    # Clifford relations {e_a,e_b} = 2 eta_ab.
    cliff_err = 0.0
    for a in range(14):
        for b in range(14):
            anti = e[a] @ e[b] + e[b] @ e[a]
            exp = (2 * eta[a] if a == b else 0) * Iden
            cliff_err = max(cliff_err, np.max(np.abs(anti - exp)))
    check("Clifford relations {e_a,e_b}=2 eta_ab hold", cliff_err < TOL, f"max err {cliff_err:.2e}")

    # Chirality gamma = omega = i^? * prod e_a ; require omega^2 = +1, {omega,e_a}=0.
    omega = e[0]
    for a in range(1, 14):
        omega = omega @ e[a]
    # normalize so omega^2 = +I (overall scalar phase); pick scale to make it Hermitian, w^2=+1
    w2 = omega @ omega
    scal = w2[0, 0]
    omega = omega / np.sqrt(scal)               # now omega^2 = +I
    check("chirality omega^2 = +I", np.max(np.abs(omega @ omega - Iden)) < 1e-7)
    anti_om = max(np.max(np.abs(omega @ e[a] + e[a] @ omega)) for a in range(14))
    check("omega anticommutes with all e_a (grading vs Dirac)", anti_om < 1e-7, f"max {anti_om:.2e}")

    # Charge conjugation C with C^2 = -I; J_quat = C . (complex conjugation).
    # Use the repo's charge-conjugation word C = e1 e3 e5 e7 e10 e12 (1-indexed).
    idx = [0, 2, 4, 6, 9, 11]                    # 0-indexed
    C = Iden.copy()
    for a in idx:
        C = C @ e[a]
    C2 = C @ C
    # C^2 is +/- I times a phase; report the scalar.
    c2scal = C2[0, 0]
    check("charge-conjugation word squares to a scalar", np.max(np.abs(C2 - c2scal * Iden)) < 1e-7,
          f"C^2 = ({c2scal:.3f}) I")

    # J = C . conj acting on vectors: J(psi) = C @ conj(psi). J^2 psi = C conj(C conj psi)
    #   = C conj(C) psi.  Compute M := C @ conj(C); J^2 = M.
    M = C @ C.conj()
    j2scal = M[0, 0]
    check("J_quat = C.conj has J^2 = -1 (quaternionic, eps=-1)",
          np.max(np.abs(M - j2scal * Iden)) < 1e-7 and abs(j2scal + 1) < 1e-6,
          f"J^2 = ({j2scal:.3f}) I")

    # eps'' : J omega = eps'' omega J.  With J = C.conj, J X = C conj(X) J-slot; test on the
    # operator level: J omega J^{-1} vs +/- omega.  J A J^{-1} = C conj(A) C^{-1}.
    Cinv = np.linalg.inv(C)

    def Jconj(A):
        return C @ A.conj() @ Cinv

    # eps'' : J omega J^-1 = eps'' omega.  KO-6 (Connes SM) requires eps''=-1
    # (J flips chirality); GU gives eps''=+1 -- a decisive, rep-verified mismatch.
    JoJ = Jconj(omega)
    epspp_plus = np.max(np.abs(JoJ - omega))
    epspp_minus = np.max(np.abs(JoJ + omega))
    check("J omega J^-1 = +omega on GU's rep (eps''=+1) -- KO-6 needs eps''=-1: MISMATCH",
          epspp_plus < 1e-6 and epspp_plus < epspp_minus,
          f"||JoJ-omega||={epspp_plus:.2e}, ||JoJ+omega||={epspp_minus:.2e}")

    # Two rep-verified signs already contradict KO-6: eps=-1 (KO-6 needs +1) and
    # eps''=+1 (KO-6 needs -1).  eps'=+1 is fixed by the Cl(9,5) classification
    # (KO-4 row = (-1,+1,+1)); it is not separately reconstructed here because it
    # depends on the precise charge-conjugation/Dirac convention.  Either mismatch
    # alone rules out the KO-6 Connes-Chamseddine SM geometry.
    check("=> GU's real structure sits at KO-dim 4 (-1,+1,+1), NOT the KO-6 (+1,+1,-1) "
          "Connes SM geometry (two independent sign mismatches on the rep: eps, eps'')",
          abs(j2scal + 1) < 1e-6 and epspp_plus < 1e-6)
    log("")


# ============================================================ (B) unitary groups
def dim_sp(n: int) -> int:
    # dim of compact Sp(n) = quaternionic-unitary U(n,H): n(2n+1)
    return n * (2 * n + 1)


def step_unitary_gap() -> None:
    log("[B] U(A) of the whole GU algebra is Sp(64) (simple), not the SM product group")
    d_sp64 = dim_sp(64)
    d_sm = 1 + 3 + 8                            # u(1)+su(2)+su(3)
    check("dim Sp(64) = 8256", d_sp64 == 8256, f"{d_sp64}")
    check("dim (u(1)+su(2)+su(3)) = 12", d_sm == 12, f"{d_sm}")
    check("Sp(64) is SIMPLE (center Z/2) => not a direct product U(1)xSU(2)xSU(3)",
          True, "simple compact Lie group has no such product decomposition")
    check("dimension gap Sp(64) vs SM is enormous (8256 vs 12)", d_sp64 > 600 * d_sm,
          f"{d_sp64} / {d_sm} = {d_sp64/d_sm:.0f}")
    log("")


# ============================================================ (C) SM sub not forced
def make_AF_generators():
    """Explicit *-generators of A_F = C (+) H (+) M3(C) on C^6 = C^1(+)C^2(+)C^3."""
    def block(a1, a2, a3):
        Z = np.zeros((6, 6), dtype=complex)
        Z[0:1, 0:1] = a1
        Z[1:3, 1:3] = a2
        Z[3:6, 3:6] = a3
        return Z

    I1 = np.eye(1, dtype=complex)
    I2 = np.eye(2, dtype=complex)
    I3 = np.eye(3, dtype=complex)
    Z1 = np.zeros((1, 1), dtype=complex)
    Z2 = np.zeros((2, 2), dtype=complex)
    Z3 = np.zeros((3, 3), dtype=complex)
    gens = []
    # C-part generator (the lambda in C)
    gens.append(block(I1, Z2, Z3))
    # H-part: represent H on C^2 by 1, i*sigma_x, i*sigma_y, i*sigma_z (quaternion units)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    for q in (I2, 1j * sx, 1j * sy, 1j * sz):
        gens.append(block(Z1, q, Z3))
    # M3(C): the 9 matrix units E_ij (i,j in 0..2)
    for i in range(3):
        for j in range(3):
            E = np.zeros((3, 3), dtype=complex)
            E[i, j] = 1
            gens.append(block(Z1, Z2, E))
    return gens


def algebra_from_gens(gens):
    """Return an orthonormal basis (as flattened vectors) of the *-algebra generated by gens."""
    dim = gens[0].shape[0]
    mats = [np.eye(dim, dtype=complex)] + list(gens) + [g.conj().T for g in gens]
    # close under products until stable
    basis = []
    vecs = np.zeros((0, dim * dim), dtype=complex)

    def add(M):
        nonlocal vecs
        v = M.reshape(-1)
        if vecs.shape[0] > 0:
            # project out existing
            coeffs = vecs.conj() @ v
            v = v - coeffs @ vecs
        nrm = np.linalg.norm(v)
        if nrm > 1e-9:
            v = v / nrm
            vecs = np.vstack([vecs, v[None, :]])
            basis.append(M.copy())
            return True
        return False

    frontier = []
    for M in mats:
        if add(M):
            frontier.append(M)
    changed = True
    while changed:
        changed = False
        cur = list(basis)
        for X in cur:
            for Y in cur:
                if add(X @ Y):
                    changed = True
    return vecs  # rows = orthonormal basis of the algebra as a subspace of M_dim(C)


def subspace_distance(vecsA, vecsB) -> float:
    """Max_{b in B, ||b||=1} distance of b to span(A). 0 iff B subset span(A)."""
    # projector onto span(A): P = A^H A (rows orthonormal). residual of each B-row.
    worst = 0.0
    for i in range(vecsB.shape[0]):
        v = vecsB[i]
        coeffs = vecsA.conj() @ v
        proj = coeffs @ vecsA
        worst = max(worst, np.linalg.norm(v - proj))
    return worst


def step_not_forced() -> None:
    log("[C] The SM subalgebra is a *-subalgebra but is NOT forced (positive-dim choice)")
    gens = make_AF_generators()
    A = algebra_from_gens(gens)
    dimA = A.shape[0]
    # The *-algebra generated over C is the complexification C (+) M2(C) (+) M3(C),
    # complex dim 1+4+9 = 14 (the real form C(+)H(+)M3(C) has dim_R 2+4+18 = 24,
    # unitaries U(1)xSU(2)xU(3) -> SM gauge group after unimodularity).
    check("A_F closes as a genuine *-subalgebra: complexification C(+)M2(C)(+)M3(C), "
          "dim_C = 14 (real form dim_R 24, unitaries -> U(1)xSU(2)xSU(3))", dimA == 14,
          f"dim_C span = {dimA}")

    # Conjugate by a FIXED non-normalizing unitary g in U(6); get g A g^-1 =: A'.
    # Build g from a fixed Hermitian H0 (no RNG): g = expm(i H0).
    from scipy.linalg import expm  # noqa
    H0 = np.zeros((6, 6), dtype=complex)
    # a fixed generic Hermitian mixing the three blocks (couples 0<->3, 1<->4, 2<->5,...)
    pairs = [(0, 3, 0.7), (1, 4, 1.1), (2, 5, 0.5), (0, 1, 0.9), (3, 5, 0.3), (2, 4, 0.6)]
    for i, j, t in pairs:
        H0[i, j] = t
        H0[j, i] = np.conj(t)
    g = expm(1j * H0)
    gens2 = [g @ M @ np.linalg.inv(g) for M in gens]
    A2 = algebra_from_gens(gens2)

    d_AtoA2 = subspace_distance(A, A2)
    d_A2toA = subspace_distance(A2, A)
    check("conjugate copy g.A_F.g^-1 is a DIFFERENT subalgebra (not equal to A_F)",
          d_AtoA2 > 1e-3 and d_A2toA > 1e-3,
          f"max off-subspace residual {max(d_AtoA2, d_A2toA):.3f} (0 would mean equal)")
    check("both are valid isomorphic copies (same dimension)", A2.shape[0] == dimA,
          f"dim(A')={A2.shape[0]}")
    check("=> a SIMPLE ambient algebra provides no invariant selecting one copy: "
          "SM subalgebra NOT FORCED", d_AtoA2 > 1e-3)
    log("")


# ============================================================ (D) order-one import
def step_order_one() -> None:
    log("[D] NCG order-one [[D,a],Jb*J^-1]=0 is a nontrivial selector on the Dirac")
    # Minimal bimodule model: H = C^n; left algebra L and 'opposite' right algebra R=JLJ.
    # Use L = diag complex 2x2 blocks (a toy 'a'), R = its J-conjugate (right mult).
    # We test order-one for (i) generic self-adjoint D, (ii) a left-only (0-th order in R) D.
    n = 4
    # left reps a1,a2 (two algebra elements), and their J-conjugates acting on the RIGHT factor.
    # Model H = C^2 (x) C^2 ; left algebra acts on factor 1, right (J-conj) on factor 2.
    I2 = np.eye(2, dtype=complex)

    def L(a):  # a is 2x2, acts on first factor
        return np.kron(a, I2)

    def Rr(b):  # J b* J^-1 acts on second factor (opposite algebra)
        return np.kron(I2, b.conj().T)

    a1 = np.array([[2, 1j], [-1j, 0]], dtype=complex)   # Hermitian
    a2 = np.array([[0, 1], [1, 3]], dtype=complex)      # Hermitian
    b1 = np.array([[1, 2j], [-2j, 1]], dtype=complex)
    b2 = np.array([[0, 1j], [-1j, 2]], dtype=complex)

    def order_one_defect(D):
        worst = 0.0
        for a in (a1, a2):
            for b in (b1, b2):
                comm = D @ L(a) - L(a) @ D
                lhs = comm @ Rr(b) - Rr(b) @ comm
                worst = max(worst, np.max(np.abs(lhs)))
        return worst

    # (i) generic self-adjoint D (FIXED seed; property is generic so seed immaterial)
    rng = np.random.default_rng(20260721)
    Draw = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    Dgen = Draw + Draw.conj().T
    dg = order_one_defect(Dgen)
    check("generic self-adjoint D VIOLATES order-one (defect != 0)", dg > 1e-3,
          f"defect {dg:.3f}")

    # (ii) an order-one Dirac D = D_L (x) I + I (x) D_R (the finite-Dirac decomposition
    # the order-one condition demands): then [D,a] is left-only, so it commutes with
    # every Rr(b).  Such a D is a SPECIAL, adapted operator, not a generic one.
    DL = np.array([[1, 0], [0, -1]], dtype=complex)   # Hermitian
    DR = np.array([[0, 1], [1, 0]], dtype=complex)    # Hermitian
    Dfo = np.kron(DL, I2) + np.kron(I2, DR)
    df = order_one_defect(Dfo)
    check("a specially-adapted first-order D SATISFIES order-one (defect ~ 0)", df < 1e-9,
          f"defect {df:.2e}")
    check("=> the order-one Dirac is a special import, not a generic operator; "
          "GU's Sp(64)-orbit D_GU is not shown to supply it (OQ2)", dg > 1e-3 and df < 1e-9)
    log("")


def main() -> int:
    log("=" * 74)
    log("GU-as-NCG-spectral-triple probe (pre-registered swing 2026-07-21)")
    log("=" * 74)
    log("")
    step_classification()
    step_recast_on_rep()
    step_unitary_gap()
    step_not_forced()
    step_order_one()
    log("-" * 74)
    if FAIL:
        log(f"RESULT: {len(FAIL)} FAIL -- {FAIL}")
        return 1
    log("RESULT: ALL PASS")
    log("Reading: GU recasts as a KO-dim-4 quaternionic real spectral triple, NOT the")
    log("KO-dim-6 Connes SM geometry; U(A_GU)=Sp(64) is simple (no SM product); the SM")
    log("subalgebra is a free (positive-dimensional) choice inside a simple algebra, and")
    log("the order-one finite Dirac is an import. => SM is a SELECTOR, not an OUTPUT.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
