#!/usr/bin/env python3
"""F2 cut relative-entropy probe at finite matrix grade.

Tests the bounded question named in
explorations/intake-bianconi-entropic-gravity-2026-07-20.md: can quantum
relative entropy between the two native Krein-compatible F2 cuts supply a
finite, scale-bearing, holonomy-odd functional?

The answer at this grade is no.  Native Krein projectors are oblique and are
not density matrices.  Hilbertizing their ranges produces positive density
matrices, but their Umegaki relative entropy is infinite because the supports
are distinct equal-rank subspaces.  Full-rank epsilon regularization is finite
but dimensionless, invariant under rescaling the Dirac symbol, and deck-even.

No claim, canon, or public-posture change.  Deterministic; NumPy only.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402


N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
TOL = 1e-8
RESULTS: list[tuple[str, str, bool]] = []


def check(tag: str, name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((tag, name, bool(ok)))
    suffix = f" ({detail})" if detail else ""
    print(f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}{suffix}")


e = gb.gammas()
xi = np.real(np.asarray(gb.XI)).astype(float)
identity = np.eye(DIM, dtype=complex)
K = e[0].copy()
for a in range(1, 9):
    K = K @ e[a]


def cvec(v: np.ndarray) -> np.ndarray:
    return sum(v[a] * e[a] for a in range(N_DIRS))


def qform(v: np.ndarray) -> float:
    return float(v @ (ETA * v))


def spectral_halves(D: np.ndarray, q: float) -> tuple[np.ndarray, np.ndarray]:
    plus = 0.5 * (identity + D / np.sqrt(q))
    return plus, identity - plus


def half_basis(projector: np.ndarray) -> np.ndarray:
    left, _singular, _right = np.linalg.svd(projector)
    return left[:, : DIM // 2]


def gram_parts(basis: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    gram = basis.conj().T @ K @ basis
    values, vectors = np.linalg.eigh(0.5 * (gram + gram.conj().T))
    return basis @ vectors[:, values > 0], basis @ vectors[:, values < 0]


def kproj(columns: np.ndarray) -> np.ndarray:
    gram = columns.conj().T @ K @ columns
    return columns @ np.linalg.solve(gram, columns.conj().T @ K)


def krein_cuts(D: np.ndarray, q: float):
    chi_plus, chi_minus = spectral_halves(D, q)
    p_pos, p_neg = gram_parts(half_basis(chi_plus))
    m_pos, m_neg = gram_parts(half_basis(chi_minus))
    w_plus = np.hstack([p_pos, m_pos])
    w_minus = np.hstack([p_neg, m_neg])
    return kproj(w_plus), kproj(w_minus), w_plus, w_minus


def hilbert_projector(columns: np.ndarray) -> np.ndarray:
    q, _r = np.linalg.qr(columns)
    return q @ q.conj().T


def logm_positive(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(0.5 * (matrix + matrix.conj().T))
    return (vectors * np.log(values)) @ vectors.conj().T


def relative_entropy(rho: np.ndarray, sigma: np.ndarray) -> float:
    return float(np.trace(rho @ (logm_positive(rho) - logm_positive(sigma))).real)


def regularized(projector: np.ndarray, eps: float) -> np.ndarray:
    return (projector + eps * identity) / (DIM // 2 + eps * DIM)


D = cvec(xi)
q = qform(xi)
Qp, Qm, Wp, Wm = krein_cuts(D, q)

native_herm = max(float(np.linalg.norm(Qp - Qp.conj().T)),
                  float(np.linalg.norm(Qm - Qm.conj().T)))
check("E", "native Q_+/Q_- are complementary K-self-adjoint projectors",
      float(np.max(np.abs(Qp + Qm - identity))) < TOL
      and float(np.max(np.abs(K @ Qp.conj().T @ K - Qp))) < TOL)
check("F", "native Krein projectors are not Hermitian density matrices",
      native_herm > 1e-3, f"Hermiticity defect {native_herm:.3f}")

Pp, Pm = hilbert_projector(Wp), hilbert_projector(Wm)
rho_p, rho_m = Pp / (DIM // 2), Pm / (DIM // 2)
check("T", "Hilbertized range projectors define positive trace-one states",
      abs(np.trace(rho_p).real - 1.0) < TOL
      and abs(np.trace(rho_m).real - 1.0) < TOL
      and float(np.min(np.linalg.eigvalsh(rho_p))) > -TOL
      and float(np.min(np.linalg.eigvalsh(rho_m))) > -TOL)

leak_pm = float(np.linalg.norm((identity - Pm) @ Pp))
leak_mp = float(np.linalg.norm((identity - Pp) @ Pm))
check("E", "equal-rank supports are distinct, so both unregularized Umegaki directions are infinite",
      leak_pm > 1e-3 and leak_mp > 1e-3,
      f"support leaks {leak_pm:.3f}, {leak_mp:.3f}")

eps_values = (1e-2, 1e-3, 1e-4)
ordered_deltas = []
finite_values = []
for eps in eps_values:
    rp, rm = regularized(Pp, eps), regularized(Pm, eps)
    d_pm = relative_entropy(rp, rm)
    d_mp = relative_entropy(rm, rp)
    finite_values.append((d_pm, d_mp))
    ordered_deltas.append(abs(d_pm - d_mp))
check("E", "epsilon-regularized relative entropy is deck-even, not holonomy-odd",
      max(ordered_deltas) < 1e-8,
      "max ordered-direction delta %.2e" % max(ordered_deltas))
check("E", "regularized values diverge as the support regulator is removed",
      finite_values[0][0] < finite_values[1][0] < finite_values[2][0],
      "D_eps=" + ", ".join(f"{pair[0]:.3f}" for pair in finite_values))

scale_defects = []
for scale in (0.25, 2.0, 7.0):
    Qps, Qms, Wps, Wms = krein_cuts(scale * D, scale * scale * q)
    Pps, Pms = hilbert_projector(Wps), hilbert_projector(Wms)
    scale_defects.append(max(float(np.linalg.norm(Qps - Qp)),
                             float(np.linalg.norm(Qms - Qm)),
                             float(np.linalg.norm(Pps - Pp)),
                             float(np.linalg.norm(Pms - Pm))))
check("E", "cut states are invariant under positive symbol rescaling; no scale is generated",
      max(scale_defects) < 1e-8,
      f"max rescaling defect {max(scale_defects):.2e}")

check("F", "the proposed entropy channel supplies no finite native scale-bearing holonomy-odd functional",
      native_herm > 1e-3 and leak_pm > 1e-3
      and max(ordered_deltas) < 1e-8 and max(scale_defects) < 1e-8)

nE = sum(tag == "E" for tag, _name, _ok in RESULTS)
nF = sum(tag == "F" for tag, _name, _ok in RESULTS)
nT = sum(tag == "T" for tag, _name, _ok in RESULTS)
all_ok = all(ok for _tag, _name, ok in RESULTS)
print()
print("F2 ENTROPY VERDICT: bounded negative at toy grade -- the native cuts are not density matrices; Hilbertization makes unregularized relative entropy infinite, while regularization is dimensionless, scale-blind, and deck-even.")
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF} (setup [T] = {nT} excluded) {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
raise SystemExit(0 if all_ok else 1)
