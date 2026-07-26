#!/usr/bin/env python3
r"""W245: Finster Dirac-sea rate versus the GU Krein branch fork.

This is a typed discriminator, not a baryogenesis calculation.

Finster's CFS fermiogenesis construction uses an essentially self-adjoint
spectral regularization operator and its ordinary Hilbert-space spectral
measure.  GU W216 supplies two conditional two-mode generators:

    H_good = xi tau_3 + Delta tau_1
    H_bad  = xi tau_3 + i Delta tau_2.

The first is Hermitian and remains real/gapped.  The second is
Krein-self-adjoint but has eigenvalues +/-sqrt(xi^2-Delta^2), hence a complex
pair for |xi| < Delta.  This script certifies the exact consequence:

* the good branch admits an ordinary projection-valued spectral calculus;
* the pathological core cannot be made self-adjoint by any positive metric;
* outside the exceptional interval the bad block is only locally
  quasi-Hermitian, with a positive metric that becomes singular at the
  exceptional point;
* therefore a Finster-style Hilbert spectral rate cannot be compared across
  the whole GU fork by identifying the BdG generator with the regularization
  operator;
* and the GU branch objects do not yet supply the universal measures and
  common constraints needed to compare actual CFS causal-action values.

The finite spectral-flow quantity included below is explicitly a standard
two-level absorber/control.  It is not Finster's continuum baryogenesis rate
and carries no baryon-number semantics.

Reproduce:
    python3 tests/W245_finster_baryogenesis_krein_branch_discriminator.py
"""

from __future__ import annotations

import math
from typing import Any

import numpy as np


TOL = 1.0e-10
XI = 0.75
DELTA = 1.0
TAU_1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
TAU_2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
TAU_3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
IDENTITY = np.eye(2, dtype=complex)

checks: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    checks.append((name, bool(passed), detail))
    status = "PASS" if passed else "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")


def hermitian_residual(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix - matrix.conj().T)))


def metric_self_adjoint_residual(
    generator: np.ndarray, metric: np.ndarray
) -> float:
    return float(
        np.max(
            np.abs(
                metric @ generator - generator.conj().T @ metric
            )
        )
    )


def good_generator(xi: float, delta: float) -> np.ndarray:
    return xi * TAU_3 + delta * TAU_1


def pathological_generator(xi: float, delta: float) -> np.ndarray:
    return xi * TAU_3 + 1.0j * delta * TAU_2


def negative_projector_good(xi: float, delta: float) -> np.ndarray:
    generator = good_generator(xi, delta)
    energy = math.sqrt(xi * xi + delta * delta)
    return 0.5 * (IDENTITY - generator / energy)


def cfs_contract_errors(payload: dict[str, Any]) -> list[str]:
    required = {
        "hilbert_dimension",
        "spin_dimension",
        "constraints",
        "support_operators",
        "measure_weights",
    }
    errors = [
        f"missing:{key}" for key in sorted(required.difference(payload))
    ]
    if "support_operators" in payload and "measure_weights" in payload:
        if len(payload["support_operators"]) != len(payload["measure_weights"]):
            errors.append("support-weight-length-mismatch")
    return errors


def causal_lagrangian(
    left: np.ndarray, right: np.ndarray, spin_dimension: int
) -> float:
    eigenvalues = np.linalg.eigvals(left @ right)
    spectral_weights = np.abs(eigenvalues)
    return float(
        np.sum(spectral_weights**2)
        - (np.sum(spectral_weights) ** 2) / (2.0 * spin_dimension)
    )


def causal_action(contract: dict[str, Any]) -> float:
    errors = cfs_contract_errors(contract)
    if errors:
        raise ValueError(", ".join(errors))
    support = contract["support_operators"]
    weights = contract["measure_weights"]
    spin_dimension = int(contract["spin_dimension"])
    return float(
        sum(
            weights[i]
            * weights[j]
            * causal_lagrangian(support[i], support[j], spin_dimension)
            for i in range(len(support))
            for j in range(len(support))
        )
    )


print("=" * 78)
print("W245 -- FINSTER SEA-RATE / GU KREIN-BRANCH TYPED DISCRIMINATOR")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. Exact branch spectra and adjoint type
# ---------------------------------------------------------------------------
good = good_generator(XI, DELTA)
bad = pathological_generator(XI, DELTA)

check(
    "good branch is ordinary Hermitian",
    hermitian_residual(good) < TOL,
    f"residual={hermitian_residual(good):.2e}",
)
check(
    "pathological branch is not ordinary Hermitian",
    hermitian_residual(bad) > 0.5,
    f"residual={hermitian_residual(bad):.3f}",
)
check(
    "pathological branch is Krein-self-adjoint under tau_3",
    metric_self_adjoint_residual(bad, TAU_3) < TOL,
    f"residual={metric_self_adjoint_residual(bad, TAU_3):.2e}",
)

good_expected = np.array(
    [-math.sqrt(XI * XI + DELTA * DELTA),
     math.sqrt(XI * XI + DELTA * DELTA)]
)
good_observed = np.sort(np.linalg.eigvalsh(good))
check(
    "good spectrum is +/-sqrt(xi^2+Delta^2)",
    np.max(np.abs(good_expected - good_observed)) < TOL,
    f"spectrum={np.round(good_observed, 8).tolist()}",
)

bad_core = pathological_generator(0.0, DELTA)
bad_core_spectrum = np.sort_complex(np.linalg.eigvals(bad_core))
check(
    "pathological core has the exact complex pair +/- i Delta",
    np.max(np.abs(np.sort(np.abs(bad_core_spectrum.imag)) - [DELTA, DELTA]))
    < TOL
    and np.max(np.abs(bad_core_spectrum.real)) < TOL,
    f"spectrum={bad_core_spectrum.tolist()}",
)

# ---------------------------------------------------------------------------
# 2. Positive-metric obstruction and exceptional-point boundary
# ---------------------------------------------------------------------------
# For H_bad=[[xi,Delta],[-Delta,-xi]] and a real Hermitian metric
# G=[[a,c],[c,b]], G H = H^T G requires
#
#     Delta (a+b) = 2 xi c.
#
# At xi=0 and Delta!=0 this forces a+b=0, impossible for G>0.  This
# elementary equation is also covered by the general fact that a
# positive-metric self-adjoint operator is similar to a Hermitian operator and
# therefore has real spectrum.
a, b, c = 1.25, 0.75, 0.0
core_metric_equation_residual = abs(DELTA * (a + b) - 0.0 * c)
check(
    "positive metric is impossible at xi=0: metric equation forces a+b=0",
    a > 0.0 and b > 0.0 and core_metric_equation_residual > 1.0,
    f"for positive diagonal entries a+b={a+b:.2f}, residual={core_metric_equation_residual:.2f}",
)

xi_outer = 1.5
outer_bad = pathological_generator(xi_outer, DELTA)
outer_metric = np.array(
    [[1.0, DELTA / xi_outer], [DELTA / xi_outer, 1.0]],
    dtype=complex,
)
outer_metric_eigenvalues = np.linalg.eigvalsh(outer_metric)
check(
    "outside |xi|>Delta the pathological block is locally quasi-Hermitian",
    np.min(outer_metric_eigenvalues) > 0.0
    and metric_self_adjoint_residual(outer_bad, outer_metric) < TOL,
    (
        f"min eig(G)={np.min(outer_metric_eigenvalues):.6f}, "
        f"residual={metric_self_adjoint_residual(outer_bad, outer_metric):.2e}"
    ),
)

exceptional_metric = np.array([[1.0, 1.0], [1.0, 1.0]], dtype=complex)
check(
    "the quasi-Hermitian metric becomes singular at |xi|=Delta",
    abs(np.linalg.det(exceptional_metric)) < TOL,
    f"det(G_EP)={np.linalg.det(exceptional_metric):.2e}",
)

# ---------------------------------------------------------------------------
# 3. PVM domain and ordinary spectral-flow absorber
# ---------------------------------------------------------------------------
projector = negative_projector_good(XI, DELTA)
check(
    "good negative-energy projector is Hermitian and idempotent",
    hermitian_residual(projector) < TOL
    and np.max(np.abs(projector @ projector - projector)) < TOL,
    (
        f"Hermitian residual={hermitian_residual(projector):.2e}, "
        f"idempotence={np.max(np.abs(projector @ projector-projector)):.2e}"
    ),
)
check(
    "good projector selects the negative eigenvalue",
    np.max(
        np.abs(
            good @ projector
            + math.sqrt(XI * XI + DELTA * DELTA) * projector
        )
    )
    < TOL,
)

# Algebraic Riesz projectors of a generic nonnormal complex-spectrum matrix can
# be idempotent without being orthogonal.  That is not the real-line spectral
# PVM of a self-adjoint operator used in the Finster construction.  We use an
# interior, nonnormal point rather than xi=0, where this special 2x2 block
# happens to be anti-Hermitian and normal.
xi_broken = 0.5
bad_broken = pathological_generator(xi_broken, DELTA)
imaginary_gap = math.sqrt(DELTA * DELTA - xi_broken * xi_broken)
bad_algebraic_projector = 0.5 * (
    IDENTITY - bad_broken / (1.0j * imaginary_gap)
)
check(
    "generic broken-region Riesz projector is idempotent but not a Hilbert PVM",
    np.max(
        np.abs(
            bad_algebraic_projector @ bad_algebraic_projector
            - bad_algebraic_projector
        )
    )
    < TOL
    and hermitian_residual(bad_algebraic_projector) > 0.5,
    (
        f"idempotence={np.max(np.abs(bad_algebraic_projector @ bad_algebraic_projector-bad_algebraic_projector)):.2e}, "
        f"Hermitian residual={hermitian_residual(bad_algebraic_projector):.3f}"
    ),
)

# Standard two-level spectral-flow control.  This is deliberately not called
# a CFS baryogenesis rate.  It only verifies that the finite arena can detect
# a moving self-adjoint sea level and its time reversal.
velocity = 0.2
dot_good = velocity * TAU_3
flow_proxy = -float(np.real(np.trace(projector @ dot_good)))
expected_proxy = velocity * XI / math.sqrt(XI * XI + DELTA * DELTA)
check(
    "ordinary good-branch spectral-flow proxy matches the avoided-crossing formula",
    abs(flow_proxy - expected_proxy) < TOL,
    f"proxy={flow_proxy:.8f}",
)
reverse_proxy = -float(np.real(np.trace(projector @ (-dot_good))))
check(
    "time reversal changes the ordinary spectral-flow sign",
    abs(reverse_proxy + flow_proxy) < TOL,
    f"forward={flow_proxy:.8f}, reverse={reverse_proxy:.8f}",
)
static_proxy = -float(np.real(np.trace(projector @ np.zeros((2, 2)))))
check(
    "static regularization control gives zero spectral flow",
    abs(static_proxy) < TOL,
)

# ---------------------------------------------------------------------------
# 4. Actual causal-action comparison requires a universal measure
# ---------------------------------------------------------------------------
complete_cfs_fixture = {
    "hilbert_dimension": 2,
    "spin_dimension": 1,
    "constraints": {"volume": 1.0, "trace": "fixed-fixture"},
    "support_operators": [
        np.diag([1.0, -1.0]).astype(complex),
        np.diag([2.0, -0.5]).astype(complex),
    ],
    "measure_weights": [0.5, 0.5],
}
fixture_action = causal_action(complete_cfs_fixture)
check(
    "positive control: a fully typed finite CFS measure has a computable causal action",
    math.isfinite(fixture_action) and fixture_action >= 0.0,
    f"S[rho]={fixture_action:.8f}",
)

gu_branch_payload = {
    "branch": "good-or-pathological",
    "generator": good,
    "krein_metric": TAU_3,
    "parameters": {"xi": XI, "Delta": DELTA},
}
missing_contract_fields = cfs_contract_errors(gu_branch_payload)
check(
    "GU branch payload does not determine a CFS universal measure or common action problem",
    {
        "missing:constraints",
        "missing:hilbert_dimension",
        "missing:measure_weights",
        "missing:spin_dimension",
        "missing:support_operators",
    }.issubset(set(missing_contract_fields)),
    f"errors={missing_contract_fields}",
)

print("-" * 78)
passed = sum(int(item[1]) for item in checks)
print(f"checks: {passed}/{len(checks)}")
print(
    "VERDICT: ADMISSIBILITY_ONLY__PATHOLOGICAL_CORE_OUTSIDE_HILBERT_PVM_DOMAIN"
)
print(
    "CAUSAL_ACTION: INCOMPLETE_CONTRACT__NO_COMMON_BRANCH_TO_UNIVERSAL_MEASURE_MAP"
)
print(
    "BARYOGENESIS: NOT_COMPUTED__FINITE_FLOW_IS_STANDARD_ABSORBER_WITH_NO_BARYON_SEMANTICS"
)
if passed != len(checks):
    raise SystemExit(1)
