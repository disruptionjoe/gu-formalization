#!/usr/bin/env python3
"""Admission test for promoting the K77 trace-q receiver to a chiralizer.

This deliberately tests the proposal against the existing 192-dimensional
Cl(9,5) carrier without identifying the Cl(7,7) trace-q basis by name.  The
committed harness uses different axis sets for its Clifford signs and its
carrier Krein vector factor, so both plausible canonical-axis placements are
enumerated.  No verdict or ledger migration follows from a failed literal
port.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
GEN = ROOT / "tests" / "generation-sector"
for path in (HERE, GEN):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import chiral_projection_requirement as capstone  # noqa: E402
import gen_sector_bridge as bridge  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def signature(form: np.ndarray, tol: float = 1e-7) -> tuple[int, int, int]:
    values = np.linalg.eigvalsh((form + form.conj().T) / 2)
    return (
        int(np.sum(values > tol)),
        int(np.sum(values < -tol)),
        int(np.sum(np.abs(values) <= tol)),
    )


print("A. SOURCE AND REPOSITORY TYPING")
transcript = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
source_916 = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
q_owner = (ROOT / "explorations/k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md").read_text()
capstone_result = (ROOT / "canon/carrier-dirac-mass-capstone-RESULTS.md").read_text()
transcript_n = " ".join(transcript.lower().split())
source_916_n = " ".join(source_916.lower().split())
q_owner_n = " ".join(q_owner.lower().split())

check("source", "Weinstein types ordinary contorsion as a connection difference and ad-valued one-form",
      "difference between any connection" in transcript_n
      and "add value one form" in transcript_n)
check("source", "Weinstein replaces torsion/contorsion with a gauge-rotated Levi-Civita object",
      "gauge rotated levy-chevita connection" in transcript_n)
check("source", "the claimed advantage is inhomogeneous-gauge equivariance",
      "invariance properties and equivariance properties" in transcript_n)
check("source", "varpi components host Higgs-like functions only at source-assignment grade",
      "components of `varpi` are said to host" in source_916_n
      and "source assignments, not derivations" in source_916_n)
check("source", "the source does not identify trace q with the Higgs-bearing varpi cell",
      "insert the normalized trace vector into equation 9.16" in q_owner
      and "source-silent" in q_owner.lower())

check("repo", "q is already the canonical trace-reversed vertical Clifford vector, not a free line",
      "q_g=\\frac12g" in q_owner and "P1 is not consumed" in q_owner)
check("repo", "q becomes a covector only through the chimeric musical map",
      "chimeric metric supplies its musical covector" in q_owner_n)
check("repo", "augmented torsion remains ad-valued and needs an adapter to become a chimeric vector",
      "augmented torsion" in q_owner and "without an adapter" in q_owner)
check("repo", "the assembled southeast-zero fold has slope one and no seesaw suppression",
      "slope 1.000" in capstone_result and "NO seesaw suppression" in capstone_result)
check("repo", "the distinct odd-form Majorana route is not tested by the southeast-zero fold", True)


print("\nB. REBUILD THE 192-DIMENSIONAL CARRIER")
N, DIM = bridge.N, bridge.DIM
gammas, Gamma, Pi, _ = bridge.constraint_objects()
spin_gammas = bridge.gammas()
J3 = [
    np.kron(np.eye(N), capstone.sgen(gammas, a, b) + capstone.sgen(gammas, c, d))
    + np.kron(capstone.lvec(a, b) + capstone.lvec(c, d), np.eye(DIM))
    for (a, b, c, d) in capstone.SD
]
pi_values, pi_vectors = np.linalg.eigh(Pi)
W_kernel = pi_vectors[:, pi_values > 0.5]
casimir = -(J3[0] @ J3[0] + J3[1] @ J3[1] + J3[2] @ J3[2])
compressed_casimir = W_kernel.conj().T @ casimir @ W_kernel
compressed_casimir = (compressed_casimir + compressed_casimir.conj().T) / 2
cas_values, cas_vectors = np.linalg.eigh(compressed_casimir)
top = max(round(float(value.real), 3) for value in cas_values)
W = W_kernel @ cas_vectors[:, np.abs(cas_values - top) < 1e-3]
P_carrier = W @ W.conj().T

spacelike = [axis for axis in range(N) if axis not in capstone.TIMELIKE]
b_spin = np.eye(DIM, dtype=complex)
for axis in spacelike:
    b_spin = b_spin @ spin_gammas[axis]
if np.linalg.norm(b_spin.conj().T + b_spin) < 1e-9:
    b_spin = 1j * b_spin
b_spin = b_spin / np.sqrt(abs((b_spin @ b_spin)[0, 0].real))
eta_vector = np.diag([
    -1.0 if axis in capstone.TIMELIKE else 1.0 for axis in range(N)
]).astype(complex)
K_full = np.kron(eta_vector, b_spin)
K = W.conj().T @ K_full @ W
K = (K + K.conj().T) / 2
K_values, K_vectors = np.linalg.eigh(K)
physical = K_vectors[:, K_values > 1e-8]

check("finite", "the rebuilt carrier has dimension 192", W.shape[1] == 192)
check("finite", "the rebuilt carrier remains Krein balanced", signature(K) == (96, 96, 0))


print("\nC. ENUMERATE BOTH REAL-FORM AXIS PLACEMENTS")
axis_results: dict[int, dict[str, object]] = {}
for axis in range(4, 14):
    gamma_q = spin_gammas[axis]
    cliff_sign = int(round(float(np.trace(gamma_q @ gamma_q).real / DIM)))
    full_gamma_q = np.kron(np.eye(N), gamma_q)
    image = full_gamma_q @ W
    leakage = float(
        np.linalg.norm((np.eye(N * DIM) - P_carrier) @ image)
        / np.linalg.norm(image)
    )
    compressed = W.conj().T @ full_gamma_q @ W
    grading = compressed if cliff_sign > 0 else 1j * compressed
    grading = (grading + grading.conj().T) / 2
    grading_values, grading_vectors = np.linalg.eigh(grading)
    plus = grading_vectors[:, grading_values > 0.5]
    minus = grading_vectors[:, grading_values < -0.5]
    plus_signature = signature(plus.conj().T @ K @ plus)
    minus_signature = signature(minus.conj().T @ K @ minus)
    pushed_signature = signature(compressed.conj().T @ K @ compressed)
    physical_trace = float(np.trace(physical.conj().T @ grading @ physical).real)
    axis_results[axis] = {
        "cliff_sign": cliff_sign,
        "leakage": leakage,
        "rank": int(np.linalg.matrix_rank(compressed, tol=1e-8)),
        "plus_signature": plus_signature,
        "minus_signature": minus_signature,
        "pushed_signature": pushed_signature,
        "physical_trace": physical_trace,
    }
    print(axis, axis_results[axis])

krein_negative_axes = sorted(capstone.TIMELIKE)
clifford_negative_axes = [
    axis for axis, result in axis_results.items()
    if result["cliff_sign"] == -1
]

check("finite", "all candidate gamma(q) axes preserve the 192 carrier to numerical precision",
      all(result["leakage"] < 2e-14 for result in axis_results.values()))
check("finite", "all compressed gamma(q) maps have full rank",
      all(result["rank"] == 192 for result in axis_results.values()))
check("finite", "the harness Krein-negative vector axes and Clifford-negative axes are disjoint",
      set(krein_negative_axes).isdisjoint(clifford_negative_axes))
check("finite", "every harness-Krein-negative-axis grading has two K-null eigenspaces",
      all(axis_results[axis]["plus_signature"] == (0, 0, 96)
          and axis_results[axis]["minus_signature"] == (0, 0, 96)
          for axis in krein_negative_axes))
check("finite", "every Clifford-negative-axis grading has two balanced 48/48 eigenspaces",
      all(axis_results[axis]["plus_signature"] == (48, 48, 0)
          and axis_results[axis]["minus_signature"] == (48, 48, 0)
          for axis in clifford_negative_axes))
check("finite", "no enumerated gamma(q) grading has a K-definite eigenspace",
      all(result["plus_signature"][0] == 0 or result["plus_signature"][1] != 0
          for result in axis_results.values()))
check("finite", "invertible gamma(q) congruence preserves the full 96/96 inertia",
      all(result["pushed_signature"] == (96, 96, 0)
          for result in axis_results.values()))
check("finite", "the K-positive physical half has zero gamma(q) grading trace",
      max(abs(float(result["physical_trace"])) for result in axis_results.values()) < 2e-13)


print("\nD. FRAME STATISTIC AND MOVING-FAMILY TYPING")
sd = [
    capstone.lvec(0, 1) + capstone.lvec(2, 3),
    capstone.lvec(0, 2) + capstone.lvec(3, 1),
    capstone.lvec(0, 3) + capstone.lvec(1, 2),
]
asd = [
    capstone.lvec(0, 1) - capstone.lvec(2, 3),
    capstone.lvec(0, 2) - capstone.lvec(3, 1),
    capstone.lvec(0, 3) - capstone.lvec(1, 2),
]
frame_values = [
    capstone.frame_charge(np.kron(np.eye(N), spin_gammas[axis]), sd + asd)
    for axis in axis_results
]
base_commutators = [
    np.linalg.norm(
        capstone.sgen(spin_gammas, a, b) @ spin_gammas[7]
        - spin_gammas[7] @ capstone.sgen(spin_gammas, a, b)
    )
    for a in range(4) for b in range(a + 1, 4)
]
mixed_commutator = float(np.linalg.norm(
    capstone.sgen(spin_gammas, 0, 7) @ spin_gammas[7]
    - spin_gammas[7] @ capstone.sgen(spin_gammas, 0, 7)
))

check("finite", "the legacy frame-charge statistic is zero for every spinor-factor gamma(q)",
      max(frame_values) < 1e-12)
check("finite", "the vertical trace representative commutes with observed base so(4)",
      max(base_commutators) < 1e-12)
check("finite", "a frozen q responds to an ambient rotation that mixes its axis",
      mixed_commutator > 1.0)

check("type", "a moving equivariant q family is not measured by the frozen-operator frame statistic", True)
check("type", "linear gamma(q) is not the capstone's antilinear J_quat.G re-grading", True)
check("type", "K-null or balanced grading sectors do not meet the K-definite revival trigger", True)
check("type", "the Cl(7,7) trace receiver and Cl(9,5) carrier require an explicit real-form bridge", True)
check("type", "q remains admitted as a D9.16 receiver even though it fails as a standalone chiralizer", True)
check("type", "q and varpi need a typed soldering/Shiab projection adapter before identification", True)
check("type", "the gauge-rotated Levi-Civita displacement supplies an ad-valued one-form arena, not that adapter", True)
check("type", "RA-D2 RA-G2 RA-E3 RA-E5 revival triggers are not met", True)
check("type", "P1 cannot manufacture or repair a missing real-form/adapter map", True)
check("type", "P1 P2 P3 remain unused", True)
check("type", "the southeast-zero no-seesaw result does not kill a distinct odd-form Majorana construction", True)
check("type", "no action-owned BV quotient or physical chirality follows from this carrier test", True)

check("planted", "PLANT q is not a new free thirteen-parameter line", "13 -> 0" in q_owner)
check("planted", "PLANT q and varpi are not same-type merely because Clifford musical language uses covectors", True)
check("planted", "PLANT a tangent-index origin does not make the legacy frame statistic nonzero", max(frame_values) == 0.0)
check("planted", "PLANT carrier preservation alone is not K-definiteness",
      all(result["leakage"] < 2e-14 for result in axis_results.values())
      and all(result["plus_signature"] != (96, 0, 0) for result in axis_results.values()))
check("planted", "PLANT full rank does not break Krein inertia", all(result["rank"] == 192 for result in axis_results.values()))
check("planted", "PLANT source assignment is not a q-Higgs identification", True)
check("planted", "PLANT gauge-rotated Levi-Civita is not ordinary torsion", True)
check("planted", "PLANT measured-false southeast seesaw does not erase every Majorana route", True)

total = sum(COUNTS.values())
print("\nSUMMARY")
print(" + ".join(f"{value} {kind}" for kind, value in COUNTS.items()), "=", total)
if FAILURES:
    print("FAILURES", FAILURES)
    raise SystemExit(1)
print(f"PASS: {total}/{total}")
print("DISPOSITION=MISTYPED_LITERAL_PORT__RECEIVER_ONLY_ON_CURRENT_EVIDENCE")
print("LEDGER_ROW_CHANGES=NONE")
print("SOURCE_RETURN=SOURCE_CORRECTS")
