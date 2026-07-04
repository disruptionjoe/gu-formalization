#!/usr/bin/env python3
"""Base-sign selector audit for the (9,5) vs (7,7) signature caveat.

This is a bounded follow-up to the 2026-07-04 signature decide-tournament.
It tests the named cheap lever from NEXT-STEPS: whether three GU-native proxy
surfaces distinguish the physically equivalent base metric convention
g -> -g:

  1. observerse tautological metric/fiber form,
  2. the canon shiab contraction channel,
  3. the RS constraint bridge anchors from gen_sector_bridge.

It does not prove that no future selector can exist. It proves that these
repo-owned finite proxies carry no selector signal: the fiber form is
unchanged, the shiab contraction remains nonzero with the same norm, and the
RS anchors/ranks are identical. J^2 changes only because the total signature
was supplied as input.
"""
from __future__ import annotations

import numpy as np

N = 14
DIM = 128
XI = np.array(
    [1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7, 1.1, 0.3, 2.2, 1.7, 0.9, 1.3],
    dtype=complex,
)


def jw(n: int) -> list[np.ndarray]:
    """Jordan-Wigner generators for the complexified 14D Clifford carrier."""
    eye = np.eye(2, dtype=complex)
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    generators = []
    for k in range(n):
        left = [s3] * k
        right = [eye] * (n - 1 - k)
        for s in (s1, s2):
            out = np.array([[1 + 0j]])
            for m in left + [s] + right:
                out = np.kron(out, m)
            generators.append(out)
    return generators


G7 = jw(7)


def symmetric_basis_4() -> list[np.ndarray]:
    basis = []
    for i in range(4):
        for j in range(i, 4):
            m = np.zeros((4, 4), dtype=float)
            m[i, j] = 1.0
            m[j, i] = 1.0
            basis.append(m)
    return basis


def dewit_form_matrix(base_diag: np.ndarray) -> np.ndarray:
    """Trace-reversed Frobenius/DeWitt form on Sym^2(T*X)."""
    ginv = np.diag(1.0 / base_diag)
    basis = symmetric_basis_4()
    gram = np.zeros((len(basis), len(basis)), dtype=float)
    for i, h in enumerate(basis):
        for j, k in enumerate(basis):
            trace_hk = np.trace(ginv @ h @ ginv @ k)
            trace_h = np.trace(ginv @ h)
            trace_k = np.trace(ginv @ k)
            gram[i, j] = trace_hk - 0.5 * trace_h * trace_k
    return gram


def signature_counts(gram: np.ndarray) -> tuple[int, int]:
    ev = np.linalg.eigvalsh(0.5 * (gram + gram.T))
    tol = 1e-9 * max(np.abs(ev).max(), 1.0)
    return int((ev > tol).sum()), int((ev < -tol).sum())


def clifford_for_signature(p: int, q: int) -> tuple[list[np.ndarray], np.ndarray]:
    eta = np.array([1.0] * p + [-1.0] * q)
    e = [G7[a] if eta[a] > 0 else 1j * G7[a] for a in range(N)]
    return e, eta


def constraint_anchors(p: int, q: int) -> dict[str, float | int]:
    e, _eta = clifford_for_signature(p, q)
    gamma = np.hstack(e)
    pi_rs = np.eye(N * DIM, dtype=complex) - gamma.conj().T @ np.linalg.inv(
        gamma @ gamma.conj().T
    ) @ gamma
    q_rs = np.eye(N * DIM, dtype=complex) - pi_rs
    cxi = sum(XI[a] * e[a] for a in range(N))
    m_d = np.kron(np.eye(N, dtype=complex), cxi)
    return {
        "rank_gamma": int(round(np.trace(q_rs).real)),
        "ker_gamma": int(round(np.trace(pi_rs).real)),
        "bare_commutator": float(np.linalg.norm(pi_rs @ m_d - m_d @ pi_rs)),
        "C2": float(np.linalg.norm(gamma @ m_d @ pi_rs)),
    }


def j2_sign(p: int, q: int) -> float:
    e, eta = clifford_for_signature(p, q)

    def phi(u: np.ndarray) -> np.ndarray:
        out = np.zeros_like(u)
        for a in range(N):
            out += eta[a] * (e[a] @ u @ e[a].conj())
        return out / N

    rng = np.random.default_rng(1)
    u = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(200):
        u = 0.5 * (u + phi(u))
        nrm = np.linalg.norm(u)
        if nrm < 1e-14:
            return 0.0
        u /= nrm
    us, _s, vs = np.linalg.svd(u)
    u = us @ vs
    return float((np.trace(u @ u.conj()) / DIM).real)


def shiab_contraction_norm(p: int, q: int) -> float:
    """Norm of the canon contraction channel before chirality projection."""
    e, _eta = clifford_for_signature(p, q)
    total = 0.0
    for a in range(N):
        for i in range(N):
            for j in range(i + 1, N):
                w = np.zeros((DIM, DIM), dtype=complex)
                if a == i:
                    w += e[j]
                if a == j:
                    w -= e[i]
                total += float(np.linalg.norm(w) ** 2)
    return total ** 0.5


def omega_square_error(p: int, q: int) -> float:
    e, _eta = clifford_for_signature(p, q)
    omega = np.eye(DIM, dtype=complex)
    for ea in e:
        omega = omega @ ea
    return float(np.linalg.norm(omega @ omega - np.eye(DIM)))


def main() -> dict[str, object]:
    mostly_plus = np.array([1.0, 1.0, 1.0, -1.0])
    mostly_minus = -mostly_plus

    fiber_plus = dewit_form_matrix(mostly_plus)
    fiber_minus = dewit_form_matrix(mostly_minus)
    fiber_sig_plus = signature_counts(fiber_plus)
    fiber_sig_minus = signature_counts(fiber_minus)
    fiber_diff = float(np.linalg.norm(fiber_plus - fiber_minus))

    # Base (3,1) + fiber (6,4) -> (9,5); base (1,3) + fiber (6,4) -> (7,7).
    total_plus = (3 + fiber_sig_plus[0], 1 + fiber_sig_plus[1])
    total_minus = (1 + fiber_sig_minus[0], 3 + fiber_sig_minus[1])

    anchors_plus = constraint_anchors(*total_plus)
    anchors_minus = constraint_anchors(*total_minus)
    shiab_plus = shiab_contraction_norm(*total_plus)
    shiab_minus = shiab_contraction_norm(*total_minus)
    omega_plus = omega_square_error(*total_plus)
    omega_minus = omega_square_error(*total_minus)
    j2_plus = j2_sign(*total_plus)
    j2_minus = j2_sign(*total_minus)

    print("=" * 88)
    print("BASE-SIGN SELECTOR AUDIT: g -> -g on three GU-native proxy surfaces")
    print("=" * 88)
    print(f"observerse fiber signature mostly-plus:  {fiber_sig_plus}")
    print(f"observerse fiber signature mostly-minus: {fiber_sig_minus}")
    print(f"fiber form ||B(g)-B(-g)||: {fiber_diff:.2e}")
    print(f"total signatures: mostly-plus -> {total_plus}; mostly-minus -> {total_minus}")
    print()
    print("RS constraint anchors")
    for key in ("rank_gamma", "ker_gamma", "bare_commutator", "C2"):
        print(f"  {key:16s} plus={anchors_plus[key]} minus={anchors_minus[key]}")
    print()
    print("Shiab and chirality proxies")
    print(f"  shiab contraction norm plus={shiab_plus:.6f} minus={shiab_minus:.6f}")
    print(f"  omega^2 error plus={omega_plus:.2e} minus={omega_minus:.2e}")
    print(f"  J^2 readout plus={j2_plus:+.3f} minus={j2_minus:+.3f}")
    print()
    print("Verdict: no selector signal in these bounded proxies.")
    print("J^2 changes only because the total signature is supplied as input; the")
    print("observerse fiber form, shiab contraction, and RS anchors are unchanged.")

    assert fiber_sig_plus == (6, 4)
    assert fiber_sig_minus == (6, 4)
    assert fiber_diff < 1e-10
    assert total_plus == (9, 5)
    assert total_minus == (7, 7)
    assert anchors_plus["rank_gamma"] == anchors_minus["rank_gamma"] == 128
    assert anchors_plus["ker_gamma"] == anchors_minus["ker_gamma"] == 1664
    assert abs(anchors_plus["bare_commutator"] - anchors_minus["bare_commutator"]) < 1e-8
    assert abs(anchors_plus["C2"] - anchors_minus["C2"]) < 1e-8
    assert abs(shiab_plus - shiab_minus) < 1e-8 and shiab_plus > 0
    assert omega_plus < 1e-8 and omega_minus < 1e-8
    assert j2_plus < -0.9 and j2_minus > 0.9

    return {
        "fiber_signature": fiber_sig_plus,
        "fiber_form_diff": fiber_diff,
        "total_plus": total_plus,
        "total_minus": total_minus,
        "anchors_plus": anchors_plus,
        "anchors_minus": anchors_minus,
        "shiab_norm": shiab_plus,
        "j2_plus": j2_plus,
        "j2_minus": j2_minus,
        "verdict": "no selector signal in observerse fiber, shiab contraction, or RS anchors",
    }


if __name__ == "__main__":
    main()
