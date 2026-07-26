#!/usr/bin/env python3
r"""W246: matched CFS measures and self-adjointization selector ambiguity.

W245 stopped because the GU branch generators did not yet define universal
measures in one common causal-action problem.  This probe attempts the
smallest natural repair.

Positive attempt 1 lowers the generator with its declared adjoint metric,
then fixes the local trace:

    x(J,H) = c I + JH - tr(JH) I / 2.

Positive attempt 2 uses a faithful Hermitian dilation:

    Phi_lam(H) = c I_4 + [[0, H + lam H^dagger],
                          [H^dagger + lam H, 0]].

For lam != +/-1 the off-diagonal block determines H exactly.  Phi_lam is
unitary-equivariant, self-adjoint, branch-blind as a rule, and gives every
support point the same local trace and signature bound.

The decisive result is hostile: at the same rational parameters and with the
same causal Lagrangian, Phi_(7/10) favors the W216 good branch whereas
Phi_(9/10) favors the pathological branch.  Both maps are faithful and remain
inside one connected admissible signature sector.  Thus causal-action
ordering is not representation-independent until a physical construction
selects the local-correlation map.

Reproduce:
    python3 tests/W246_cfs_self_adjointization_selector_ambiguity.py
"""

from __future__ import annotations

from fractions import Fraction
import math

import numpy as np


TOL = 1.0e-9
A = Fraction(1, 2)
DELTA = Fraction(1, 1)
C = Fraction(1, 10)
LAMBDA_LEFT = Fraction(7, 10)
LAMBDA_RIGHT = Fraction(9, 10)
COMMON_BOUNDEDNESS_CEILING = 1000.0

I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
ZERO2 = np.zeros((2, 2), dtype=complex)
TAU1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
TAU2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
TAU3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)

checks: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    checks.append((name, bool(passed), detail))
    suffix = f" -- {detail}" if detail else ""
    print(f"[{'PASS' if passed else 'FAIL'}] {name}{suffix}")


def good_generator(xi: float, delta: float) -> np.ndarray:
    return xi * TAU3 + delta * TAU1


def bad_generator(xi: float, delta: float) -> np.ndarray:
    return xi * TAU3 + 1.0j * delta * TAU2


def causal_lagrangian(
    left: np.ndarray, right: np.ndarray, spin_dimension: int
) -> float:
    spectral_weights = np.abs(np.linalg.eigvals(left @ right))
    return float(
        np.sum(spectral_weights**2)
        - np.sum(spectral_weights) ** 2 / (2.0 * spin_dimension)
    )


def measure_action(
    support: list[np.ndarray],
    weights: list[float],
    spin_dimension: int,
) -> float:
    return float(
        sum(
            weights[i]
            * weights[j]
            * causal_lagrangian(
                support[i], support[j], spin_dimension
            )
            for i in range(len(support))
            for j in range(len(support))
        )
    )


def boundedness_functional(
    support: list[np.ndarray], weights: list[float]
) -> float:
    return float(
        sum(
            weights[i]
            * weights[j]
            * np.sum(np.abs(np.linalg.eigvals(support[i] @ support[j])))
            ** 2
            for i in range(len(support))
            for j in range(len(support))
        )
    )


def hermitian_residual(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix - matrix.conj().T)))


def signature(matrix: np.ndarray) -> tuple[int, int, int]:
    eigenvalues = np.linalg.eigvalsh(
        0.5 * (matrix + matrix.conj().T)
    )
    positive = int(np.sum(eigenvalues > TOL))
    negative = int(np.sum(eigenvalues < -TOL))
    zero = len(eigenvalues) - positive - negative
    return positive, negative, zero


def fixed_trace_metric_lowering(
    metric: np.ndarray,
    generator: np.ndarray,
    local_trace_half: float,
) -> np.ndarray:
    lowered = metric @ generator
    traceless = lowered - 0.5 * np.trace(lowered) * I2
    return local_trace_half * I2 + traceless


def phi_lambda(
    generator: np.ndarray, lam: float, local_trace_quarter: float
) -> np.ndarray:
    transported = generator + lam * generator.conj().T
    return local_trace_quarter * I4 + np.block(
        [[ZERO2, transported], [transported.conj().T, ZERO2]]
    )


def recover_generator_from_phi(
    encoded: np.ndarray, lam: float
) -> np.ndarray:
    transported = encoded[:2, 2:]
    return (
        transported - lam * transported.conj().T
    ) / (1.0 - lam * lam)


def exact_dilation_actions(
    lam: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    """Closed forms in the frozen sector used by the exact specimens."""
    p = 1 + lam
    q = 1 - lam
    good = 8 * C * C * p * p * (A * A + DELTA * DELTA)
    bad = (
        8
        * C
        * C
        * (p * p * A * A + 2 * q * q * DELTA * DELTA)
        + 8 * p * p * q * q * A * A * DELTA * DELTA
    )
    return good, bad, bad - good


def exact_metric_lowering_actions() -> tuple[Fraction, Fraction, Fraction]:
    good = 4 * C * C * (A * A + DELTA * DELTA)
    bad = 8 * C * C * DELTA * DELTA
    return good, bad, bad - good


def symmetric_support(
    branch: str,
    encoder,
) -> list[np.ndarray]:
    generator_fn = good_generator if branch == "good" else bad_generator
    return [
        encoder(generator_fn(sign * float(A), float(DELTA)))
        for sign in (1.0, -1.0)
    ]


print("=" * 78)
print("W246 -- MATCHED CFS MEASURES / SELF-ADJOINTIZATION SELECTOR AMBIGUITY")
print("=" * 78)

weights = [0.5, 0.5]

# ---------------------------------------------------------------------------
# 1. Positive attempt: metric lowering
# ---------------------------------------------------------------------------
metric_good = I2
metric_bad = TAU3
metric_support_good = symmetric_support(
    "good",
    lambda h: fixed_trace_metric_lowering(
        metric_good, h, float(C)
    ),
)
metric_support_bad = symmetric_support(
    "bad",
    lambda h: fixed_trace_metric_lowering(
        metric_bad, h, float(C)
    ),
)

check(
    "metric-lowered support is self-adjoint on both branches",
    all(
        hermitian_residual(item) < TOL
        for item in metric_support_good + metric_support_bad
    ),
)
check(
    "metric-lowered support has one common fixed local trace 2c",
    all(
        abs(float(np.trace(item).real) - 2.0 * float(C)) < TOL
        for item in metric_support_good + metric_support_bad
    ),
)
check(
    "metric-lowered support stays in spin-dimension-one signature (1,1)",
    all(
        signature(item) == (1, 1, 0)
        for item in metric_support_good + metric_support_bad
    ),
)

metric_good_exact, metric_bad_exact, metric_margin_exact = (
    exact_metric_lowering_actions()
)
metric_good_numeric = measure_action(
    metric_support_good, weights, spin_dimension=1
)
metric_bad_numeric = measure_action(
    metric_support_bad, weights, spin_dimension=1
)
check(
    "metric-lowered good action matches exact 1/20",
    abs(metric_good_numeric - float(metric_good_exact)) < TOL
    and metric_good_exact == Fraction(1, 20),
    f"numeric={metric_good_numeric:.8f}, exact={metric_good_exact}",
)
check(
    "metric-lowered bad action matches exact 2/25",
    abs(metric_bad_numeric - float(metric_bad_exact)) < TOL
    and metric_bad_exact == Fraction(2, 25),
    f"numeric={metric_bad_numeric:.8f}, exact={metric_bad_exact}",
)
check(
    "canonical metric-lowering attempt favors the good branch",
    metric_margin_exact == Fraction(3, 100)
    and metric_bad_numeric > metric_good_numeric,
    f"S_bad-S_good={metric_margin_exact}",
)

zero_trace_good = symmetric_support(
    "good",
    lambda h: fixed_trace_metric_lowering(metric_good, h, 0.0),
)
zero_trace_bad = symmetric_support(
    "bad",
    lambda h: fixed_trace_metric_lowering(metric_bad, h, 0.0),
)
check(
    "zero-local-trace null erases the metric-lowered action preference",
    abs(measure_action(zero_trace_good, weights, 1)) < TOL
    and abs(measure_action(zero_trace_bad, weights, 1)) < TOL,
    "both actions are zero",
)

# ---------------------------------------------------------------------------
# 2. Faithful Hermitian-dilation rival class
# ---------------------------------------------------------------------------
def dilation_support(branch: str, lam: Fraction) -> list[np.ndarray]:
    return symmetric_support(
        branch,
        lambda h: phi_lambda(h, float(lam), float(C)),
    )


all_dilation_support: dict[
    Fraction, dict[str, list[np.ndarray]]
] = {}
for lam in (LAMBDA_LEFT, LAMBDA_RIGHT):
    all_dilation_support[lam] = {
        "good": dilation_support("good", lam),
        "bad": dilation_support("bad", lam),
    }

check(
    "both dilation encodings are strictly inside the faithful range",
    all(lam not in (Fraction(-1), Fraction(1)) for lam in all_dilation_support),
)
check(
    "all dilation outputs are ordinary self-adjoint",
    all(
        hermitian_residual(item) < TOL
        for by_branch in all_dilation_support.values()
        for support in by_branch.values()
        for item in support
    ),
)
check(
    "all dilation outputs have identical fixed local trace 4c",
    all(
        abs(float(np.trace(item).real) - 4.0 * float(C)) < TOL
        for by_branch in all_dilation_support.values()
        for support in by_branch.values()
        for item in support
    ),
)
check(
    "all dilation outputs stay in spin-dimension-two signature (2,2)",
    all(
        signature(item) == (2, 2, 0)
        for by_branch in all_dilation_support.values()
        for support in by_branch.values()
        for item in support
    ),
)
check(
    "all universal measures have common unit volume",
    abs(sum(weights) - 1.0) < TOL,
)
check(
    "one common boundedness ceiling admits every candidate",
    all(
        boundedness_functional(support, weights)
        < COMMON_BOUNDEDNESS_CEILING
        for by_branch in all_dilation_support.values()
        for support in by_branch.values()
    ),
    f"ceiling={COMMON_BOUNDEDNESS_CEILING}",
)

# Exact injectivity with the fixed block grading.
recovery_errors = []
for lam, by_branch in all_dilation_support.items():
    for branch, support in by_branch.items():
        generator_fn = good_generator if branch == "good" else bad_generator
        for index, sign in enumerate((1.0, -1.0)):
            expected = generator_fn(
                sign * float(A), float(DELTA)
            )
            recovered = recover_generator_from_phi(
                support[index], float(lam)
            )
            recovery_errors.append(
                float(np.max(np.abs(expected - recovered)))
            )
check(
    "each admitted Phi_lambda is faithful given the fixed grading",
    max(recovery_errors) < TOL,
    f"max reconstruction error={max(recovery_errors):.2e}",
)

# Unitary equivariance control.
unitary = np.array(
    [[1.0, 1.0], [-1.0, 1.0]], dtype=complex
) / math.sqrt(2.0)
block_unitary = np.block(
    [[unitary, ZERO2], [ZERO2, unitary]]
)
equivariance_errors = []
for lam in (LAMBDA_LEFT, LAMBDA_RIGHT):
    for generator in (
        good_generator(float(A), float(DELTA)),
        bad_generator(float(A), float(DELTA)),
    ):
        left = phi_lambda(
            unitary @ generator @ unitary.conj().T,
            float(lam),
            float(C),
        )
        right = (
            block_unitary
            @ phi_lambda(generator, float(lam), float(C))
            @ block_unitary.conj().T
        )
        equivariance_errors.append(float(np.max(np.abs(left - right))))
check(
    "both admitted encodings are unitary-equivariant",
    max(equivariance_errors) < TOL,
    f"max equivariance error={max(equivariance_errors):.2e}",
)

# Action comparison, independently evaluated from product spectra and from
# exact closed forms.
action_receipts: dict[str, dict[str, object]] = {}
for lam, by_branch in all_dilation_support.items():
    good_numeric = measure_action(by_branch["good"], weights, 2)
    bad_numeric = measure_action(by_branch["bad"], weights, 2)
    good_exact, bad_exact, margin_exact = exact_dilation_actions(lam)
    key = str(lam)
    action_receipts[key] = {
        "good_numeric": good_numeric,
        "bad_numeric": bad_numeric,
        "good_exact": str(good_exact),
        "bad_exact": str(bad_exact),
        "margin_exact": str(margin_exact),
    }
    check(
        f"Phi_{key} numerical actions match the exact closed forms",
        abs(good_numeric - float(good_exact)) < TOL
        and abs(bad_numeric - float(bad_exact)) < TOL,
        (
            f"S_good={good_exact}, S_bad={bad_exact}, "
            f"margin={margin_exact}"
        ),
    )

left_good, left_bad, left_margin = exact_dilation_actions(LAMBDA_LEFT)
right_good, right_bad, right_margin = exact_dilation_actions(LAMBDA_RIGHT)
check(
    "Phi_7/10 favors the good branch",
    left_margin == Fraction(1517, 5000) and left_bad > left_good,
    f"S_bad-S_good={left_margin}",
)
check(
    "Phi_9/10 favors the pathological branch",
    right_margin == Fraction(-43, 200) and right_bad < right_good,
    f"S_bad-S_good={right_margin}",
)

# The complete interval [0.7,0.9] remains faithful and inside the same
# signature sector for the frozen parameters. Bisection locates the tie.
def margin_float(lam: float) -> float:
    p = 1.0 + lam
    q = 1.0 - lam
    a = float(A)
    delta = float(DELTA)
    c = float(C)
    return 8.0 * delta * delta * (
        c * c * (2.0 * q * q - p * p)
        + p * p * q * q * a * a
    )


lo, hi = float(LAMBDA_LEFT), float(LAMBDA_RIGHT)
for _ in range(80):
    mid = 0.5 * (lo + hi)
    if margin_float(lo) * margin_float(mid) <= 0.0:
        hi = mid
    else:
        lo = mid
lambda_tie = 0.5 * (lo + hi)
tie_support = (
    dilation_support("good", Fraction(lambda_tie)),
    dilation_support("bad", Fraction(lambda_tie)),
)
check(
    "ordering crosses continuously inside the common admissible sector",
    abs(margin_float(lambda_tie)) < 1.0e-10
    and all(
        signature(item) == (2, 2, 0)
        for support in tie_support
        for item in support
    ),
    f"lambda_tie={lambda_tie:.12f}",
)

# When Delta=0 the two branch generators are identical; every unchanged
# encoder must return equal action. This guards against branch labels in code.
for lam in (LAMBDA_LEFT, LAMBDA_RIGHT):
    null_good = [
        phi_lambda(
            good_generator(sign * float(A), 0.0),
            float(lam),
            float(C),
        )
        for sign in (1.0, -1.0)
    ]
    null_bad = [
        phi_lambda(
            bad_generator(sign * float(A), 0.0),
            float(lam),
            float(C),
        )
        for sign in (1.0, -1.0)
    ]
    check(
        f"Delta=0 branch-identity null passes for Phi_{lam}",
        abs(
            measure_action(null_good, weights, 2)
            - measure_action(null_bad, weights, 2)
        )
        < TOL,
    )

# Causal action itself remains invariant under a common unitary conjugation.
base_support = all_dilation_support[LAMBDA_LEFT]["good"]
rotated_support = [
    block_unitary @ item @ block_unitary.conj().T
    for item in base_support
]
check(
    "causal action is invariant under common unitary conjugation",
    abs(
        measure_action(base_support, weights, 2)
        - measure_action(rotated_support, weights, 2)
    )
    < TOL,
)

print("-" * 78)
passed = sum(int(item[1]) for item in checks)
print(f"checks: {passed}/{len(checks)}")
print(
    "VERDICT: MATCHED_CFS_TOYS_EXIST__ORDERING_REVERSES_UNDER_FAITHFUL_SELF_ADJOINTIZATION"
)
print(
    "SELECTOR: REPRESENTATION_SENSITIVE_NO_SELECTOR__PHYSICAL_LOCAL_CORRELATION_MAP_REQUIRED"
)
print(
    "NONCLAIM: NO_GU_SOURCE_ACTION__NO_UNRESTRICTED_CFS_MINIMIZER__NO_BARYOGENESIS_RATE"
)
if passed != len(checks):
    raise SystemExit(1)
