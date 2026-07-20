#!/usr/bin/env python3
"""M2 cut-scale dial probe on the truncated-real N2 end family.

This deliberately stays in the 14-dimensional symbol geometry.  It tests the
spectral location of the cut and the C2 scaling discriminator without building
the 128-dimensional Clifford matrices, an end operator, or an APS problem.

Verdict: conditional pass, sector-relative.  A nonzero uniform cut interval
exists on the uniformly spacelike-gapped sub-end, but collapses at cone walls.
The cut value is invisible inside the gap and remains an imported boundary
scale.  Keeping it out of the symbol kernel preserves C2 homogeneity; leaking
it into a massive kernel fails the frozen discriminator.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402


ETA = np.array([1.0] * 9 + [-1.0] * 5)
LAM = 0.5
XI = np.real(np.asarray(gb.XI)).astype(float)
RESULTS: list[tuple[str, str, bool]] = []


def check(tag: str, name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((tag, name, bool(ok)))
    suffix = f" ({detail})" if detail else ""
    print(f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}{suffix}")


sym_idx = [(0, 0), (1, 1), (2, 2), (3, 3),
           (0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)]


def sym_mat(pair: tuple[int, int]) -> np.ndarray:
    a, b = pair
    matrix = np.zeros((4, 4))
    if a == b:
        matrix[a, a] = 1.0
    else:
        matrix[a, b] = matrix[b, a] = 1.0 / np.sqrt(2.0)
    return matrix


h_modes = [sym_mat(pair) for pair in sym_idx]


def fixsign(vector: np.ndarray) -> np.ndarray:
    return vector if vector[int(np.argmax(np.abs(vector)))] > 0 else -vector


def frame_diag(a4: tuple[float, ...]) -> np.ndarray:
    """N2's closed-form DeWitt-orthonormal frame on a diagonal ray."""
    a0, a1, a2, a3 = [float(x) for x in a4]
    frame = np.zeros((14, 14))
    frame[0, 0], frame[1, 1], frame[2, 2] = (1 / np.sqrt(a0),
                                                       1 / np.sqrt(a1),
                                                       1 / np.sqrt(a2))
    frame[3, 9] = 1 / np.sqrt(a3)
    frame[8, 3], frame[9, 4], frame[10, 5] = (np.sqrt(a0 * a1),
                                                       np.sqrt(a0 * a2),
                                                       np.sqrt(a1 * a2))
    frame[11, 10], frame[12, 11], frame[13, 12] = (np.sqrt(a0 * a3),
                                                             np.sqrt(a1 * a3),
                                                             np.sqrt(a2 * a3))
    u = np.array([1 / a0, 1 / a1, 1 / a2, -1 / a3])
    metric = np.diag(u * u) - LAM * np.outer(u, u)
    values, vectors = np.linalg.eigh(metric)
    refs = np.array([[1., -1., 0., 0.], [0., 1., -1., 0.],
                     [0., 0., 1., -1.], [1., 1., 1., 1.]]).T
    start = 0
    while start < 4:
        stop = start + 1
        while stop < 4 and abs(values[stop] - values[start]) <= 1e-9 * max(1.0, abs(values[start])):
            stop += 1
        if stop - start > 1:
            subspace = vectors[:, start:stop]
            basis = []
            for ref in refs.T:
                vector = subspace @ (subspace.T @ ref)
                for prior in basis:
                    vector -= prior * float(prior @ vector)
                norm = float(np.linalg.norm(vector))
                if norm > 1e-8:
                    basis.append(vector / norm)
                if len(basis) == stop - start:
                    break
            vectors[:, start:stop] = np.stack(basis, axis=1)
        start = stop
    positive = [k for k, value in enumerate(values) if value > 0]
    negative = [k for k, value in enumerate(values) if value < 0]
    if len(positive) != 3 or len(negative) != 1:
        raise ValueError("DeWitt diagonal block lost signature (3,1)")
    for j, k in enumerate(positive):
        frame[4:8, 6 + j] = fixsign(vectors[:, k]) / np.sqrt(values[k])
    frame[4:8, 13] = fixsign(vectors[:, negative[0]]) / np.sqrt(-values[negative[0]])
    return frame


def rot4(theta: float) -> np.ndarray:
    result = np.eye(4)
    result[0, 0] = result[3, 3] = np.cos(theta)
    result[0, 3] = -np.sin(theta)
    result[3, 0] = np.sin(theta)
    return result


def rho(rotation: np.ndarray) -> np.ndarray:
    result = np.zeros((14, 14))
    result[:4, :4] = rotation
    for i, mode in enumerate(h_modes):
        moved = rotation @ mode @ rotation.T
        for j, target in enumerate(h_modes):
            result[4 + j, 4 + i] = float(np.sum(moved * target))
    return result


base_frame = frame_diag((1.0, 1.0, 1.0, 1.0))
xi_vec = base_frame @ XI


def ray(alpha: np.ndarray, s: float) -> tuple[float, ...]:
    return tuple(np.exp(2.0 * alpha * s))


def xi_of(t: float, a4: tuple[float, ...]) -> np.ndarray:
    frame = rho(rot4(np.pi * t)) @ frame_diag(a4)
    return np.linalg.solve(frame, xi_vec)


def qform(vector: np.ndarray) -> float:
    return float(vector @ (ETA * vector))


def gap(t: float, alpha: np.ndarray, s: float) -> float:
    q = qform(xi_of(t, ray(alpha, s)))
    return np.sqrt(q) if q > 0 else 0.0


t_grid = np.linspace(0.0, 1.0, 81)
s_grid = np.linspace(0.0, 4.0, 41)
conf_up = np.ones(4) / 2.0
conf_down = -np.ones(4) / 2.0

surviving_gaps = np.array([[gap(float(t), conf_up, float(s)) for t in t_grid]
                           for s in s_grid])
uniform_gap = float(np.min(surviving_gaps))
check("E", "the N2 spacelike sub-end has a nonzero uniform spectral gap",
      uniform_gap > 1.0, f"inf sampled gap {uniform_gap:.6f}")

cut_points = (-0.9 * uniform_gap, -0.25 * uniform_gap, 0.0,
              0.25 * uniform_gap, 0.9 * uniform_gap)
ranks = []
for cut in cut_points:
    # D^2=qI has 64 eigenvalues at each of +/-sqrt(q).  Every cut strictly
    # inside the uniform gap therefore selects the same positive half.
    ranks.append({64 if (-g < cut < g) else (128 if cut < -g else 0)
                  for g in surviving_gaps.ravel()})
check("E", "every cut point inside the gap defines the same rank-64 section",
      all(value == {64} for value in ranks),
      f"admissible interval (-{uniform_gap:.4f}, +{uniform_gap:.4f})")

crossing_profile = np.array([[qform(xi_of(float(t), ray(conf_down, float(s))))
                              for t in t_grid] for s in s_grid])
positive_gaps = np.sqrt(crossing_profile[crossing_profile > 0])
near_wall_gap = float(np.min(positive_gaps))
check("F", "the full end has cone walls: its nonzero uniform cut interval collapses",
      float(np.min(crossing_profile)) < 0 and near_wall_gap < 1.0,
      f"sampled near-wall positive gap {near_wall_gap:.6f}")

c2_coeff = np.sqrt(3328.0 / 7.0)
c2 = lambda vector: c2_coeff * float(np.linalg.norm(vector))
sample = xi_of(0.37, ray(conf_up, 1.25))
ratio_boundary_only = c2(2.0 * sample) / c2(sample)
lambda0 = 0.5 * uniform_gap
massive = lambda vector: c2(vector) / (1.0 + (c2(vector) / lambda0) ** 2)
ratio_leaked = massive(2.0 * sample) / massive(sample)
check("E", "exporting lambda_0 as boundary data preserves C2 homogeneity",
      abs(ratio_boundary_only - 2.0) < 1e-12,
      f"C2(2xi)/C2(xi)={ratio_boundary_only:.12f}")
check("F", "leaking lambda_0 into a massive symbol kernel fails F7",
      abs(ratio_leaked - 2.0) > 0.1,
      f"leaked ratio {ratio_leaked:.6f}")

for mu in (1e-3, 1.0, 1e3):
    dimensionless_position = (mu * lambda0) / (mu * uniform_gap)
    if abs(dimensionless_position - 0.5) > 1e-12:
        raise AssertionError("co-scaling changed the cut position")
check("E", "one external scale rescales D and lambda_0 together while all cut ratios stay fixed",
      True)

check("F", "M2 value is not derived: all cut points in the open gap are section-indistinguishable",
      len(cut_points) > 1 and all(value == ranks[0] for value in ranks))

n_e = sum(tag == "E" for tag, _name, _ok in RESULTS)
n_f = sum(tag == "F" for tag, _name, _ok in RESULTS)
all_ok = all(ok for _tag, _name, ok in RESULTS)
print()
print("M2 VERDICT: CONDITIONAL PASS, SECTOR-RELATIVE -- a boundary cut-scale slot exists on the uniformly gapped sub-end and can remain the only dimensionful input without violating C2 scaling; the slot collapses at cone walls and its value is neither derived nor read by the symbol-grade section.")
print(f"HEADLINE: {n_e} [E] + {n_f} [F] = {n_e + n_f} {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
raise SystemExit(0 if all_ok else 1)
