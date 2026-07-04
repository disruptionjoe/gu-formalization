#!/usr/bin/env python3
"""C-07 quaternionic-Kramers wall: standing per-generator J-commutation regression.

Closes the one remaining verification gap of the C-07 THEOREM
(explorations/big-swing-2026-07-03/BIG-SWING-C07-quaternionic-kramers-wall-THEOREM.md):
the prior claim that the GU-native primitives are H-linear (commute with the
quaternionic structure J_quat of Cl(9,5)=M(64,H)) was only checked to ~1e-11
numerically / as a double-commutant *class* argument. This script converts that
into an EXACT, PER-GENERATOR machine-precision certificate.

What is verified here (hard asserts):

  (0) The quaternionic structure U on the 128-dim spinor module of Cl(9,5).
      U is antilinear: U = C.K with K = complex conjugation and C a fixed
      128x128 matrix. We take, from the repo's own verified rep, the explicit
      analytic charge-conjugation matrix
          C = e_1 e_3 e_5 e_7 e_10 e_12
      (the product of exactly the Clifford generators e_a whose reality sign is
      -1, i.e. bar(e_a) = -e_a). Then:
        * C is unitary               -> U is antiunitary,
        * bar(C) = C and C^2 = -I    -> U^2 = C bar(C) = -I,
        * e_a C = C bar(e_a) for all a -> U commutes with the Clifford action.
      p - q = 9 - 5 = 4 (mod 8) is exactly what makes U^2 = -I (quaternionic).

  (1) PER-GENERATOR exact J-commutation. For every named GU-native primitive A
      the antilinear commutation condition [A, J_quat] = 0 reads, on the linear
      part C (with J = C.K):
          A C = C conj(A)      i.e.   residual = || A C - C conj(A) ||_F
      For operators on the 128-dim spinor factor we use C; for operators on the
      full 1792 = 14 x 128 space we use J_full = id_14 (x) C. Every primitive
      must hit machine-zero (<= ATOL), per-generator, not as a class.

      Primitives (all GU-native, from tests/generation-sector/gen_sector_bridge.py
      and the verified rep tests/oq_rk1_cl95_explicit_rep.py):
        - the 14 Clifford generators e_a (timelike ones are i*G_a),
        - all 91 bilinears sigma_ab = [e_a,e_b]/2 (this contains so(4)+so(10)),
        - the so(4) block (a,b in {0,1,2,3}) and so(10) block (a,b in {4..13})
          reported explicitly,
        - the full chirality omega = e_0 e_1 ... e_13 (= "Gamma_15"),
        - the Rarita-Schwinger projector Pi_RS   (on the 1792 space),
        - the twisted Dirac form M_D = id_14 (x) c(xi) (on the 1792 space).

      HONEST DIAGNOSTIC [1b]: the alternative "i*Gamma_a" Hermitian rescaling
      h_a = -i e_a (a>=9) does NOT commute with J for the timelike directions
      (residual ~2.3e1), because -i is a J-antilinear scalar. This is the named
      "scalar-i" trap and is reported, not asserted to zero -- it proves the
      certificate is discriminating (only the genuine H-linear GU primitives,
      the Clifford generators e_a themselves, hit machine-zero).

  (2) The Kramers MECHANISM (not even-dim triviality). On the even-dim module:
        * a J-commuting Hermitian has EVEN kernel dimension (nullity) -> even
          signature (every eigenspace is a quaternionic module);
        * a NON-J-commuting Hermitian on the SAME even-dim space CAN have ODD
          nullity -> ODD signature.
      Both are demonstrated, plus the table-free parity identity
      sig == nullity (mod 2) on even dim.

No target constants are imported (no 3, 8, 24, chi(K3), Ahat). Honest residuals.

Run:  python tests/big-swing/c07_kramers_regression.py   ; echo exit=$?
"""
from __future__ import annotations

import os
import sys

import numpy as np

# --- locate the bridge (verified Cl(9,5)=M(64,H) rep; N=14, DIM=128) ---
_HERE = os.path.dirname(os.path.abspath(__file__))
_GEN = os.path.normpath(os.path.join(_HERE, "..", "generation-sector"))
_TESTS = os.path.normpath(os.path.join(_HERE, ".."))
for p in (_GEN, _TESTS):
    if p not in sys.path:
        sys.path.insert(0, p)

import gen_sector_bridge as bridge  # noqa: E402

N = bridge.N        # 14
DIM = bridge.DIM    # 128
ATOL = 1e-10        # machine-zero threshold (float64 Frobenius over 128/1792 dim)

I128 = np.eye(DIM, dtype=complex)


# ----------------------------------------------------------------------------
# (0) quaternionic structure U = C . K  on the 128-dim spinor module
# ----------------------------------------------------------------------------
def build_C(e):
    """C = product of the generators e_a with reality sign bar(e_a) = -e_a.

    Those are a in {1,3,5,7,10,12}. Analytic facts (verified below):
    C is unitary, bar(C)=C, C^2=-I, and e_a C = C bar(e_a) for every a.
    """
    S = [1, 3, 5, 7, 10, 12]
    C = I128.copy()
    for a in S:
        C = C @ e[a]
    return C


def jcomm_residual(A, C):
    """|| A C - C conj(A) ||_F  for the antilinear J = C.K on the space of A."""
    return float(np.linalg.norm(A @ C - C @ np.conj(A)))


def signature_nullity(A, tol=1e-9):
    w = np.linalg.eigvalsh((A + A.conj().T) / 2.0)
    n_plus = int(np.sum(w > tol))
    n_minus = int(np.sum(w < -tol))
    nullity = int(np.sum(np.abs(w) <= tol))
    return n_plus - n_minus, nullity, n_plus, n_minus


def main():
    print("=" * 78)
    print("C-07 quaternionic-Kramers wall : per-generator J-commutation regression")
    print(f"Cl(9,5) = M(64,H)  ;  N={N}  DIM={DIM}  (p-q = 9-5 = 4 mod 8 -> J^2=-1)")
    print("=" * 78)

    e = bridge.gammas()                 # 14 Clifford generators, 128x128
    assert len(e) == N and e[0].shape == (DIM, DIM)

    C = build_C(e)
    Jfull = np.kron(np.eye(N, dtype=complex), C)   # id_14 (x) C on 1792

    # --- (0) quaternionic-structure properties, to machine precision ---
    unit_err = float(np.linalg.norm(C.conj().T @ C - I128))     # C unitary => U antiunitary
    barC_err = float(np.linalg.norm(np.conj(C) - C))            # bar(C) = C
    Usq_err = float(np.linalg.norm(C @ np.conj(C) + I128))      # U^2 = C bar(C) = -I
    Csq_err = float(np.linalg.norm(C @ C + I128))               # C^2 = -I
    print("\n[0] Quaternionic structure U = C.K :")
    print(f"    C unitary  (=> U antiunitary) : ||C^H C - I|| = {unit_err:.3e}")
    print(f"    bar(C) = C                     : ||conj(C)-C|| = {barC_err:.3e}")
    print(f"    U^2 = C bar(C) = -I            : ||C conj(C)+I|| = {Usq_err:.3e}")
    print(f"    C^2 = -I                       : ||C^2 + I||    = {Csq_err:.3e}")
    assert unit_err <= ATOL, unit_err
    assert barC_err <= ATOL, barC_err
    assert Usq_err <= ATOL, Usq_err
    assert Csq_err <= ATOL, Csq_err

    # ----------------------------------------------------------------------
    # (1) PER-GENERATOR exact J-commutation certificate
    # ----------------------------------------------------------------------
    print("\n[1] Per-generator J-commutation residual  || A C - C conj(A) ||_F :")
    all_res = {}

    # (a) the 14 Clifford generators e_a  (timelike are i*G_a)
    gen_res = [jcomm_residual(e[a], C) for a in range(N)]
    for a in range(N):
        all_res[f"e_{a}"] = gen_res[a]
    print(f"    gammas e_a (14)                 : max = {max(gen_res):.3e}")

    # (c) bilinears sigma_ab = [e_a,e_b]/2  (all 91), plus so(4)+so(10) blocks
    sig_res = []
    so4_res = []
    so10_res = []
    for a in range(N):
        for b in range(a + 1, N):
            sab = (e[a] @ e[b] - e[b] @ e[a]) / 2.0
            r = jcomm_residual(sab, C)
            sig_res.append(r)
            all_res[f"sigma_{a}_{b}"] = r
            if a in (0, 1, 2, 3) and b in (0, 1, 2, 3):
                so4_res.append(r)
            if a in range(4, 14) and b in range(4, 14):
                so10_res.append(r)
    print(f"    bilinears sigma_ab (91)         : max = {max(sig_res):.3e}")
    print(f"      so(4) block {{0,1,2,3}} (6)      : max = {max(so4_res):.3e}")
    print(f"      so(10) block {{4..13}} (45)      : max = {max(so10_res):.3e}")

    # (d) full chirality omega = e_0 e_1 ... e_13  (= "Gamma_15")
    omega = I128.copy()
    for a in range(N):
        omega = omega @ e[a]
    om_res = jcomm_residual(omega, C)
    all_res["omega"] = om_res
    print(f"    chirality omega = e_0..e_13     :       {om_res:.3e}")

    # (e) full-space primitives on 1792 = 14 x 128 : Pi_RS and M_D
    _e, Gamma, Pi_RS, M_D = bridge.constraint_objects()
    pi_res = jcomm_residual(Pi_RS, Jfull)
    md_res = jcomm_residual(M_D, Jfull)
    all_res["Pi_RS"] = pi_res
    all_res["M_D"] = md_res
    print(f"    RS projector Pi_RS (1792)       :       {pi_res:.3e}")
    print(f"    Dirac form M_D = id14 (x) c(xi) :       {md_res:.3e}")

    worst_name = max(all_res, key=all_res.get)
    worst = all_res[worst_name]
    print(f"\n    WORST per-generator residual    : {worst:.3e}  ({worst_name})")
    print(f"    threshold (machine-zero) ATOL   : {ATOL:.1e}")

    # hard asserts, per-generator (not as a class)
    for name, r in all_res.items():
        assert r <= ATOL, f"J-commutation FAILED for {name}: residual {r:.3e} > {ATOL:.1e}"

    # ----------------------------------------------------------------------
    # (1b) HONEST DIAGNOSTIC: the "i*Gamma_a" Hermitian rescaling.
    # The GU-native Clifford generators e_a all commute with J exactly (above).
    # If instead one forces each generator Hermitian by the rescaling
    #     h_a = e_a  (a<9, already Hermitian)  ;  h_a = -i e_a = G_a  (a>=9),
    # the TIMELIKE ones pick up an imaginary scalar -i, which is J-ANTILINEAR
    # (conj flips its sign): h_a C - C conj(h_a) = -2i C conj(e_a) != 0.
    # This is exactly the named "scalar-i" trap. It is reported (not asserted to
    # zero) because it PROVES the certificate is discriminating: not everything
    # on this space commutes with J -- only the genuinely H-linear GU primitives.
    print("\n[1b] Diagnostic -- naive Hermitian rescaling h_a (a>=9 uses -i*e_a):")
    h = [e[a] if a < 9 else (-1j) * e[a] for a in range(N)]
    herm_res = [jcomm_residual(h[a], C) for a in range(N)]
    for a in range(N):
        assert np.linalg.norm(h[a] - h[a].conj().T) <= 1e-9  # each h_a Hermitian
    space_max = max(herm_res[a] for a in range(9))      # spacelike a<9
    time_min = min(herm_res[a] for a in range(9, 14))   # timelike a>=9
    print(f"    spacelike h_a (a<9, = e_a)      : max residual = {space_max:.3e} (commute)")
    print(f"    timelike  h_a (a>=9, = -i e_a)  : min residual = {time_min:.3e} (BREAK: scalar-i)")
    # positive assertion of the honest finding: spacelike commute, timelike do NOT
    assert space_max <= ATOL
    assert time_min > 1.0

    # ----------------------------------------------------------------------
    # (2) Kramers MECHANISM: even nullity/signature under J vs odd without J
    # ----------------------------------------------------------------------
    print("\n[2] Kramers mechanism (even nullity/signature under J vs odd without):")
    rng = np.random.default_rng(20260703)

    # J-commuting Hermitian on the 128-dim module:
    #   X = A + C conj(A) C^{-1}  commutes with J (C^2=-I => C^{-1}=-C) and is Hermitian.
    A0 = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    A0 = A0 + A0.conj().T
    Cinv = np.linalg.inv(C)
    X = A0 + C @ np.conj(A0) @ Cinv
    X = (X + X.conj().T) / 2.0
    x_jres = jcomm_residual(X, C)
    assert x_jres <= ATOL, x_jres

    # every eigenvalue of a J-commuting Hermitian has even multiplicity (Kramers)
    wX = np.linalg.eigvalsh(X)
    wX_sorted = np.sort(wX)
    # pair up consecutive eigenvalues; Kramers => they come in equal pairs
    pair_gap = float(np.max(np.abs(wX_sorted[0::2] - wX_sorted[1::2])))
    # force a kernel with even nullity: subtract a genuine eigenvalue lam (real)
    lam = float(wX_sorted[10])          # some eigenvalue (has even multiplicity)
    Xk = X - lam * I128
    sigX, nullX, _, _ = signature_nullity(Xk)
    print(f"    J-commuting Hermitian  : J-resid={x_jres:.3e}  "
          f"eigval pairing gap={pair_gap:.3e}")
    print(f"      Kramers-doubled kernel : nullity={nullX} (even={nullX % 2 == 0}), "
          f"signature={sigX} (even={sigX % 2 == 0})")
    assert pair_gap <= 1e-8, pair_gap                 # Kramers degeneracy
    assert nullX % 2 == 0 and nullX >= 2              # even, nontrivial kernel
    assert sigX % 2 == 0                              # even signature

    # NON-J-commuting Hermitian on the SAME even-dim space with ODD nullity:
    # a real-diagonal Hermitian with exactly one zero eigenvalue.
    d = rng.standard_normal(DIM)
    d[np.argmin(np.abs(d))] = 0.0                     # force exactly one zero
    d[d == 0.0] = 0.0
    # ensure exactly one zero
    nz = int(np.sum(d == 0.0))
    if nz != 1:
        d[0] = 0.0
        d[1:] = np.where(d[1:] == 0.0, 1.0, d[1:])
    Y = np.diag(d.astype(complex))
    y_jres = jcomm_residual(Y, C)
    sigY, nullY, _, _ = signature_nullity(Y)
    print(f"    non-J Hermitian (same dim {DIM}) : J-resid={y_jres:.3e} (NOT J-commuting)")
    print(f"      nullity={nullY} (odd={nullY % 2 == 1}), "
          f"signature={sigY} (odd={sigY % 2 == 1})")
    assert y_jres > 1.0                               # genuinely does NOT commute with J
    assert nullY % 2 == 1                             # ODD nullity possible without J
    assert sigY % 2 == 1                              # -> ODD signature

    # table-free parity identity sig == nullity (mod 2) on even dim (both cases)
    assert (sigX % 2) == (nullX % 2)
    assert (sigY % 2) == (nullY % 2)
    print(f"    parity identity sig == nullity (mod 2) on even dim : holds (both)")

    print("\n" + "=" * 78)
    print("RESULT: HAS_GAP CLOSED. Every named GU-native primitive commutes with the")
    print("quaternionic J_quat EXACTLY (per-generator, machine-zero). The Kramers")
    print("mechanism (even nullity under J; odd nullity reachable without J) is")
    print("demonstrated on the same even-dim module. No target constant imported.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
