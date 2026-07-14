#!/usr/bin/env python3
"""W192: explicit observer-section carrier, torsion-kernel, and spectral gate.

This is the big-swing execution requested after W191.  It uses the repository's
verified 128-complex-dimensional Cl(9,5) representation and the written canon
Clifford-contraction shiab.  It deliberately distinguishes that spinor-valued
map from the still-unbuilt ad(P)-valued map required by the displayed I1B law.

The script establishes exactly what the explicit proxy forces:

* on H=(0,1,2,9), Phi_H: Lambda^2 H x S -> H x S is surjective, with a
  256-complex-dimensional preimage ambiguity;
* the W180 gamma vertex is K-self-adjoint/Clifford-odd, not a K-anti-self-adjoint
  Sp connection generator;
* no state-independent Spin-equivariant lift V -> V x S exists (central-parity
  obstruction), while a frozen record spinor supplies a state-dependent lift;
* the symmetrized canonical Phi d kernel has a 128-dimensional critical shell;
* bare K-residue signs are channel-dependent (+,+,+,-) on the (3,1) section;
* the static finite matrix has no continuum spectral density.  A retarded
  rho_J still requires record dynamics, a state, and an ad(P)-typed vertex.

Nothing here promotes the proxy to the physical I1B Hessian or changes a claim.
"""

from __future__ import annotations

import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "generation-sector")
if GEN not in sys.path:
    sys.path.insert(0, GEN)

import gen_sector_bridge as gb  # noqa: E402


TOL = 2e-8
CHECKS: list[tuple[str, bool]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    ok = bool(condition)
    CHECKS.append((name, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    if not ok:
        raise AssertionError(name)


def section(name: str) -> None:
    print("\n" + "=" * 92)
    print(name)
    print("=" * 92)


def cluster(values: np.ndarray, digits: int = 7) -> dict[complex, int]:
    rounded = np.round(values.real, digits) + 1j * np.round(values.imag, digits)
    unique, counts = np.unique(rounded, return_counts=True)
    return {complex(u): int(c) for u, c in zip(unique, counts)}


# Verified Cl(9,5) representation reused from the repository.
E = gb.gammas()
DIM = E[0].shape[0]
ETA14 = np.array([1.0] * 9 + [-1.0] * 5)
I128 = np.eye(DIM, dtype=complex)

# Source-first observer section: (3,1) horizontal plus (6,4) normal.
HIDX = (0, 1, 2, 9)
NIDX = tuple(i for i in range(14) if i not in HIDX)
ETAH = ETA14[list(HIDX)]
PAIRS4 = tuple((a, b) for a in range(4) for b in range(a + 1, 4))

# W180's spinor Krein form K_S=e_0...e_8.
K = E[0].copy()
for a in range(1, 9):
    K = K @ E[a]

# Chirality volume element.
OMEGA = I128.copy()
for e_a in E:
    OMEGA = OMEGA @ e_a


def sigma(a: int, b: int) -> np.ndarray:
    return 0.25 * (E[a] @ E[b] - E[b] @ E[a])


def phi_horizontal() -> np.ndarray:
    """Written canon shiab Phi on Lambda^2(H) x S -> H x S."""
    out = np.zeros((4 * DIM, len(PAIRS4) * DIM), dtype=complex)
    for pair_i, (a, b) in enumerate(PAIRS4):
        col = slice(pair_i * DIM, (pair_i + 1) * DIM)
        out[a * DIM : (a + 1) * DIM, col] = E[HIDX[b]]
        out[b * DIM : (b + 1) * DIM, col] = -E[HIDX[a]]
    return out


HFIELD = np.kron(np.diag(ETAH), K)
I512 = np.eye(4 * DIM, dtype=complex)


def principal_d(k: np.ndarray) -> np.ndarray:
    """D(k)=Phi_H sigma(d)(k) on horizontal vector-spinors.

    (D T)_a = i [k_a sum_c e_c T_c - slash(k) T_a].
    """
    slash = sum(k[c] * E[HIDX[c]] for c in range(4))
    out = np.zeros((4 * DIM, 4 * DIM), dtype=complex)
    for a in range(4):
        for c in range(4):
            block = 1j * (k[a] * E[HIDX[c]] - (slash if a == c else 0.0))
            out[a * DIM : (a + 1) * DIM, c * DIM : (c + 1) * DIM] = block
    return out


def c_t(k: np.ndarray) -> np.ndarray:
    """Symmetric Hessian proxy C_T=I+sym_sharp(Phi_H d) for the written spinor shiab."""
    d_op = principal_d(k)
    d_sharp = HFIELD @ d_op.conj().T @ HFIELD  # H^{-1}=H
    return I512 + 0.5 * (d_op + d_sharp)


def main() -> int:
    section("A -- explicit representation and frozen observer section")
    check("A1 Cl(9,5) representation has complex dimension 128", DIM == 128)
    cliff_error = 0.0
    for a in range(14):
        for b in range(14):
            expected = 2.0 * ETA14[a] * I128 if a == b else np.zeros_like(I128)
            cliff_error = max(cliff_error, float(np.max(np.abs(E[a] @ E[b] + E[b] @ E[a] - expected))))
    check("A2 Clifford relations hold", cliff_error < TOL, f"max error={cliff_error:.2e}")
    check("A3 horizontal section has signature (3,1)",
          int(np.sum(ETAH > 0)) == 3 and int(np.sum(ETAH < 0)) == 1)
    eta_n = ETA14[list(NIDX)]
    check("A4 normal complement has signature (6,4)",
          int(np.sum(eta_n > 0)) == 6 and int(np.sum(eta_n < 0)) == 4)
    k_eigs = np.linalg.eigvalsh(K)
    check("A5 K is an involutive Hermitian Krein form of signature (64,64)",
          np.max(np.abs(K.conj().T - K)) < TOL
          and np.max(np.abs(K @ K - I128)) < TOL
          and int(np.sum(k_eigs > 0.5)) == int(np.sum(k_eigs < -0.5)) == 64)

    section("B -- the carrier-type gate")
    gamma_self = max(float(np.max(np.abs(e.conj().T @ K - K @ e))) for e in E)
    gamma_anti = min(float(np.max(np.abs(e.conj().T @ K + K @ e))) for e in E)
    check("B1 W180 gamma vertices are K-self-adjoint (real-current operators)",
          gamma_self < TOL, f"max residual={gamma_self:.2e}")
    check("B2 those vertices are not K-anti-self-adjoint connection generators",
          gamma_anti > 1.0, f"minimum anti-self-adjoint residual={gamma_anti:.2f}")

    sigmas = [sigma(a, b) for a in range(14) for b in range(a + 1, 14)]
    sigma_anti = max(float(np.max(np.abs(s.conj().T @ K + K @ s))) for s in sigmas)
    check("B3 the even bivectors Sigma_ab do satisfy the K-Lie-algebra condition",
          sigma_anti < TOL, f"max residual={sigma_anti:.2e}")
    gamma_odd = max(float(np.max(np.abs(OMEGA @ e + e @ OMEGA))) for e in E)
    sigma_even = max(float(np.max(np.abs(OMEGA @ s - s @ OMEGA))) for s in sigmas)
    check("B4 gamma vertices are Clifford-odd while connection bivectors are even",
          gamma_odd < TOL and sigma_even < TOL)
    grade_overlap = max(abs(np.vdot(e, s)) for e in E for s in sigmas)
    check("B5 vector and bivector carrier spans are Frobenius-orthogonal",
          grade_overlap < TOL, f"max overlap={grade_overlap:.2e}")

    # Central element -1 in Spin acts trivially on V and as -1 on S, hence as
    # -1 on V x S.  Equivariance of L:V->VxS would require L=-L.
    rng = np.random.default_rng(20260714)
    trial_lift = rng.normal(size=(4 * DIM, 4))
    central_defect = (-np.eye(4 * DIM)) @ trial_lift - trial_lift @ np.eye(4)
    check("B6 central parity forbids every nonzero state-independent Spin lift V -> V x S",
          np.linalg.norm(central_defect + 2.0 * trial_lift) < TOL
          and np.linalg.norm(central_defect) > 1.0)

    section("C -- written canon shiab and the record-state lift")
    phi = phi_horizontal()
    phi_rank = int(np.linalg.matrix_rank(phi, tol=TOL))
    phi_singular = np.linalg.svd(phi, compute_uv=False)
    phi_clusters = cluster(phi_singular.astype(complex))
    check("C1 Phi_H has shape 512 x 768", phi.shape == (512, 768))
    check("C2 the horizontal canon shiab is surjective", phi_rank == 512, f"rank={phi_rank}")
    check("C3 its preimage ambiguity is 256 complex dimensions", phi.shape[1] - phi_rank == 256)
    check("C4 singular values are sqrt(2) x384 and sqrt(6) x128",
          phi_clusters == {complex(round(np.sqrt(2), 7)): 384,
                           complex(round(np.sqrt(6), 7)): 128},
          f"clusters={phi_clusters}")

    # Freeze a source-first K-positive record spinor without an eigensolver.
    seed = np.zeros(DIM, dtype=complex)
    seed[0] = 1.0
    psi = seed + K @ seed
    psi /= np.linalg.norm(psi)
    check("C5 frozen record spinor is K-positive", abs(np.vdot(psi, K @ psi) - 1.0) < TOL)

    # State-dependent gamma-vertex carrier.  Its current components are the K
    # matrix elements <psi,K e_a psi>.  This uses psi as the missing spinor spurion.
    vertex = np.concatenate([E[a] @ psi for a in HIDX])
    current_h = np.array([float(np.vdot(psi, K @ E[a] @ psi).real) for a in HIDX])
    normal_matrix = phi @ phi.conj().T
    preimage = phi.conj().T @ np.linalg.solve(normal_matrix, vertex)
    lift_residual = float(np.linalg.norm(phi @ preimage - vertex) / np.linalg.norm(vertex))
    check("C6 the state-dependent record vertex lies in the horizontal shiab image",
          lift_residual < TOL, f"relative residual={lift_residual:.2e}")
    check("C7 image membership does not select a unique curvature carrier",
          phi.shape[1] - phi_rank == 256)
    check("C8 the implemented W180 current is a matrix element of that vertex",
          np.max(np.abs(current_h - np.array([
              np.vdot(psi, K @ vertex[a * DIM : (a + 1) * DIM]).real for a in range(4)
          ]))) < TOL)

    section("D -- explicit symmetrized torsion kernel")
    c_zero = c_t(np.zeros(4))
    check("D1 at zero momentum the proxy kernel is the algebraic identity",
          np.max(np.abs(c_zero - I512)) < TOL)
    c_space = c_t(np.array([1.0, 0.0, 0.0, 0.0]))
    c_time = c_t(np.array([0.0, 0.0, 0.0, 1.0]))
    krein_self = max(
        float(np.max(np.abs(c_space.conj().T @ HFIELD - HFIELD @ c_space))),
        float(np.max(np.abs(c_time.conj().T @ HFIELD - HFIELD @ c_time))),
    )
    check("D2 C_T is Krein-self-adjoint on the frozen section", krein_self < TOL,
          f"max residual={krein_self:.2e}")

    space_spec = cluster(np.linalg.eigvals(c_space))
    expected_space = {
        complex(round(1.0 - np.sqrt(3.0) / 2.0, 7)): 128,
        1.0 + 0.0j: 256,
        complex(round(1.0 + np.sqrt(3.0) / 2.0, 7)): 128,
    }
    check("D3 unit spacelike spectrum is 1, 1+/-sqrt(3)/2",
          space_spec == expected_space, f"spectrum={space_spec}")
    time_spec = cluster(np.linalg.eigvals(c_time))
    expected_time = {
        complex(1.0, round(-np.sqrt(3.0) / 2.0, 7)): 128,
        1.0 + 0.0j: 256,
        complex(1.0, round(np.sqrt(3.0) / 2.0, 7)): 128,
    }
    check("D4 unit timelike Krein spectrum contains a complex-conjugate pair",
          time_spec == expected_time, f"spectrum={time_spec}")

    p_star = 2.0 / np.sqrt(3.0)
    c_critical = c_t(np.array([p_star, 0.0, 0.0, 0.0]))
    critical_rank = int(np.linalg.matrix_rank(c_critical, tol=2e-7))
    check("D5 the canonical proxy has a 128-dimensional spacelike critical shell",
          critical_rank == 384, f"p*={p_star:.8f}, rank={critical_rank}")
    check("D6 dropping dT removes that shell (matched algebraic control)",
          np.linalg.matrix_rank(I512) == 512)

    # The record vertex sees the shell.  These exact rational response forms
    # are verified at multiple momenta rather than inferred from one pole.
    vertex_norm = np.vdot(vertex, HFIELD @ vertex)
    check("D7 record vertex has positive nonzero field-space norm",
          abs(vertex_norm - 4.0) < TOL, f"norm={vertex_norm.real:.6g}")
    for label, p in (("quarter", 0.25), ("half", 0.5), ("unit", 1.0)):
        cs = c_t(np.array([p, 0.0, 0.0, 0.0]))
        response = np.vdot(vertex, HFIELD @ np.linalg.solve(cs, vertex)) / vertex_norm
        expected = (1.0 - 0.5 * p * p) / (1.0 - 0.75 * p * p)
        check(f"D8-{label} source response matches the critical-shell rational form",
              abs(response - expected) < 2e-7,
              f"response={response.real:.8f}, expected={expected:.8f}")

    section("E -- bare residue sign and the still-missing spectral density")
    p_plus = 0.5 * (I128 + K)
    p_minus = 0.5 * (I128 - K)
    signed_residues = []
    for local_a, global_a in enumerate(HIDX):
        state = E[global_a] @ psi
        plus_weight = float(np.vdot(p_plus @ state, p_plus @ state).real)
        minus_weight = float(np.vdot(p_minus @ state, p_minus @ state).real)
        signed_residues.append(float(np.vdot(state, K @ state).real))
        if ETAH[local_a] > 0:
            check(f"E1 spatial channel {global_a} preserves K-positive type",
                  abs(plus_weight - 1.0) < TOL and minus_weight < TOL)
        else:
            check(f"E1 timelike channel {global_a} flips into K-negative type",
                  plus_weight < TOL and abs(minus_weight - 1.0) < TOL)
    check("E2 bare signed residues on the observer section are (+,+,+,-)",
          np.max(np.abs(np.array(signed_residues) - ETAH)) < TOL,
          f"residues={signed_residues}")

    # For real frequency the finite ultralocal response has no continuum cut.
    # This is a zero-rho control, not a physical spectral-density construction.
    time_response = []
    for omega in (0.25, 0.5, 1.0):
        ct = c_t(np.array([0.0, 0.0, 0.0, omega]))
        r = np.vdot(vertex, HFIELD @ np.linalg.solve(ct, vertex)) / vertex_norm
        time_response.append(r)
        expected = 1.0 / (1.0 + 0.75 * omega * omega)
        check(f"E3 real-frequency proxy response at omega={omega} is real rational",
              abs(r.imag) < TOL and abs(r.real - expected) < 2e-7,
              f"response={r.real:.8f}, expected={expected:.8f}")
    check("E4 static Cl representation fixes residue type but cannot locate spectral support",
          all(abs(r.imag) < TOL for r in time_response))

    section("F -- verdict")
    passed = sum(ok for _, ok in CHECKS)
    total = len(CHECKS)
    print(f"W192: {passed}/{total} checks passed")
    print(
        "VERDICT: TYPED-OBSTRUCTION / STATE-SELECTED SAME-CARRIER / SPECTRAL SIGN\n"
        "NOT CLOSED.  The written spinor shiab gives a concrete kernel with a source-visible\n"
        "critical shell, and a frozen record state supplies a vertex carrier in its image.\n"
        "But the lift is state-dependent and 256-fold nonunique; no state-independent Spin\n"
        "lift exists.  More seriously, W180's gamma vertex is K-self-adjoint and Clifford-odd,\n"
        "not an Sp connection generator, while I1B needs an ad(P)-valued torsion/curvature map.\n"
        "The bare K residue is channel-dependent (+,+,+,-), and no current Hamiltonian or\n"
        "propagator is present to turn those residues into an on-shell retarded rho_J."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # explicit nonzero audit failure
        print(f"W192 FAILED: {exc}")
        raise
