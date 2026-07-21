#!/usr/bin/env python3
"""Hostile verification of the uniformity execution.

This probe does not recompute the committed fixed-delta carrier slopes.  It
checks the two assumptions that the committed adjudication actually needs:

1. Gate power is measured in the delta -> 0 variable, using a grid-resolved
   matched ladder delta_N ~ |q'(s*)| h_N.  The observable is the weighted
   norm of the resolvent Cauchy difference R(delta_N)-R(2 delta_N), in the
   same norm-resolvent metric as the target.
2. The numerical two-block carrier must be the section-symbol product whose
   algebra was settled in Stage 1.  The current cheap shared-factor surrogate
   is audited directly against M_2^2=(q_A+q_B)I.

The result separates the single-carrier numerical question from the stronger
shared theorem, whose product clause cannot inherit evidence from an
algebraically different surrogate.
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import uniformity_execution_probe as U  # noqa: E402


LADDER = (65, 129)
Y = 1.0
ITERS = 12
T0 = time.time()


def log(message: str) -> None:
    print(f"    .. {message}  [t={time.time() - T0:6.1f}s]", flush=True)


def logslope(values: list[float]) -> float:
    return U.logslope(LADDER, values)


def weighted_resolvent_difference(
    n_lo: sp.csr_matrix,
    n_hi: sp.csr_matrix,
    nres: int,
    bs: int,
    weight: np.ndarray,
) -> float:
    """||W[(N_lo-iY)^-1-(N_hi-iY)^-1]W|| by power iteration."""
    size = n_lo.shape[0]
    ident = sp.identity(size, format="csr", dtype=complex)
    lu_lo = U.BlockTriLU((n_lo - 1j * Y * ident).tocsr(), nres, bs=bs)
    lu_hi = U.BlockTriLU((n_hi - 1j * Y * ident).tocsr(), nres, bs=bs)

    def mv(v: np.ndarray) -> np.ndarray:
        wv = weight * v
        return weight * (lu_lo.solve(wv) - lu_hi.solve(wv))

    def rmv(v: np.ndarray) -> np.ndarray:
        wv = weight * v
        return weight * (
            lu_lo.solve(wv, trans="H") - lu_hi.solve(wv, trans="H")
        )

    operator = spla.LinearOperator(
        (size, size), matvec=mv, rmatvec=rmv, dtype=complex
    )
    return U.opnorm(operator, iters=ITERS)


def single_family(label: str, s_lo: float, s_hi: float, exponent: float):
    absolute = []
    cauchy = []
    deltas = []
    for nres in LADDER:
        ops = U.build_ops(U.A_DN, U.T_OP, s_lo, s_hi, nres)
        # Scope obligation 6: remain in the grid-resolved window while
        # actually approaching delta=0 as the grid is refined.
        delta_lo = abs(U.QPRIME) * ops["h"]
        delta_hi = 2.0 * delta_lo
        deltas.append((delta_lo, delta_hi))

        def normalized(delta: float) -> sp.csr_matrix:
            if exponent == 0.5:
                factors = U.fvec(ops["qs"], delta)
            else:
                factors = 1.0 / (ops["qs"] + 1j * delta) ** exponent
            return U.scale_cols(ops["M_op"], factors)

        n_lo = normalized(delta_lo)
        n_hi = normalized(delta_hi)
        weight = U.weight_vec(ops["sj"], 256)
        rnorm = U.resolvent_norm(
            n_lo, 1j * Y, nres, 256, weight=weight, iters=ITERS
        )
        dnorm = weighted_resolvent_difference(
            n_lo, n_hi, nres, 256, weight
        )
        absolute.append(rnorm)
        cauchy.append(dnorm)
        log(
            f"{label} N={nres}: delta=({delta_lo:.5f},{delta_hi:.5f}) "
            f"U_w={rnorm:.6f} Cauchy_w={dnorm:.6f}"
        )
    return {
        "absolute": absolute,
        "cauchy": cauchy,
        "absolute_tau": logslope(absolute),
        "cauchy_tau": logslope(cauchy),
        "deltas": deltas,
    }


def shared_product_algebra_audit():
    """Audit the exact object used by build_product, not Stage 1's surrogate."""
    rows = []
    for s in (U.S_STAR - 0.15, U.S_STAR, U.S_STAR + 0.12):
        def symbol(t: float):
            d = U.cvec(U.xi_of(t, U.ray(U.A_DN, float(s))))
            cs, _ct, p, _t, q = U.sec_parts(d)
            return (U.K_S @ cs / np.sqrt(p)) @ d, q

        a, qa = symbol(U.T_OP)
        b, qb = symbol(U.T2)
        shared = np.kron(a, U.TAU1) + np.kron(b, U.TAU3)
        target = (qa + qb) * np.eye(shared.shape[0], dtype=complex)
        commutator = float(np.linalg.norm(a @ b - b @ a, 2))
        defect = float(np.linalg.norm(shared @ shared - target, 2))
        rows.append((s, commutator, defect))
        log(
            f"shared product s={s:.6f}: ||[A,B]||={commutator:.6e} "
            f"||M2^2-q2I||={defect:.6e}"
        )
    return rows


def analytic_jordan_control():
    """Known singular resolvent in exactly the measured norm.

    J^2=0 and A_delta=J/delta give
    (A_delta-iI)^-1=iI+J/delta, so both the resolvent norm and its
    delta-Cauchy difference grow like delta^-1.  This is a genuine planted
    singularity, unlike the rejected exponent-one GU-family normalization.
    """
    absolute = []
    cauchy = []
    deltas = []
    jordan = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    ident = np.eye(2, dtype=complex)
    collar_length = U.S_HI - U.S_LO
    for nres in LADDER:
        h = collar_length / (nres + 1)
        delta_lo = abs(U.QPRIME) * h
        delta_hi = 2.0 * delta_lo
        r_lo = np.linalg.inv(jordan / delta_lo - 1j * Y * ident)
        r_hi = np.linalg.inv(jordan / delta_hi - 1j * Y * ident)
        absolute.append(float(np.linalg.norm(r_lo, 2)))
        cauchy.append(float(np.linalg.norm(r_lo - r_hi, 2)))
        deltas.append((delta_lo, delta_hi))
        log(
            f"analytic Jordan N={nres}: delta=({delta_lo:.5f},"
            f"{delta_hi:.5f}) U={absolute[-1]:.6f} "
            f"Cauchy={cauchy[-1]:.6f}"
        )
    return {
        "absolute": absolute,
        "cauchy": cauchy,
        "absolute_tau": logslope(absolute),
        "cauchy_tau": logslope(cauchy),
        "deltas": deltas,
    }


def main() -> None:
    print("=== UNIFORMITY HOSTILE VERIFY ===", flush=True)

    # A fixed delta cannot be a planted delta->0 divergence control.  This
    # exact check records why the prior N-slope expectation was ill-typed.
    fixed = 0.3
    fixed_factors = [abs((1j * fixed) ** -1) for _ in LADDER]
    fixed_tau = logslope(fixed_factors)
    print(
        f"FIXED-DELTA CONTROL AUDIT: factors={fixed_factors} "
        f"N-slope={fixed_tau:+.6f} (analytic expectation 0)",
        flush=True,
    )

    gapped = single_family(
        "gapped exp=1/2", U.S_LO, U.S_STAR - 0.18, 0.5
    )
    crossing = single_family(
        "crossing exp=1/2", U.S_LO, U.S_HI, 0.5
    )
    singular = single_family(
        "over-singular exp=1", U.S_LO, U.S_HI, 1.0
    )
    jordan = analytic_jordan_control()
    product_rows = shared_product_algebra_audit()

    analytic_control_fires = jordan["cauchy_tau"] > 0.60
    rejected_geometric_control_fires = singular["cauchy_tau"] > 0.60
    gapped_regular = abs(gapped["absolute_tau"]) < 0.35
    crossing_regular = abs(crossing["absolute_tau"]) < 0.35
    crossing_cauchy = crossing["cauchy_tau"] < 0.0
    shared_product_valid = max(row[2] for row in product_rows) < 1e-8

    if not analytic_control_fires:
        single_outcome = "SINGLE-U-OBSTRUCTION: analytic control did not fire"
    elif gapped_regular and crossing_regular and crossing_cauchy:
        single_outcome = (
            "SINGLE-U-REGULAR-SUPPORTED: calibrated matched-window evidence"
        )
    else:
        single_outcome = (
            "SINGLE-U-SINGULAR-OR-UNRESOLVED: target failed a regularity gate"
        )

    if shared_product_valid and single_outcome.startswith("SINGLE-U-REGULAR"):
        shared_outcome = "U-REGULAR-CANDIDATE: product audit passed"
    else:
        shared_outcome = (
            "U-OBSTRUCTION: shared theorem product clause is not tested by "
            "the current noncommuting surrogate"
        )

    print("\n" + "=" * 76, flush=True)
    print(f"SINGLE OUTCOME -> {single_outcome}", flush=True)
    print(f"SHARED OUTCOME -> {shared_outcome}", flush=True)
    print(
        "SLOPES (absolute, Cauchy): "
        f"gapped=({gapped['absolute_tau']:+.3f},"
        f"{gapped['cauchy_tau']:+.3f}) "
        f"crossing=({crossing['absolute_tau']:+.3f},"
        f"{crossing['cauchy_tau']:+.3f}) "
        f"over-singular=({singular['absolute_tau']:+.3f},"
        f"{singular['cauchy_tau']:+.3f}) "
        f"Jordan=({jordan['absolute_tau']:+.3f},"
        f"{jordan['cauchy_tau']:+.3f})",
        flush=True,
    )
    print(
        "GATES: "
        f"analytic_control_fires={analytic_control_fires} "
        f"rejected_geometric_control_fires="
        f"{rejected_geometric_control_fires} "
        f"gapped_regular={gapped_regular} "
        f"crossing_regular={crossing_regular} "
        f"crossing_cauchy={crossing_cauchy} "
        f"shared_product_valid={shared_product_valid}",
        flush=True,
    )


if __name__ == "__main__":
    main()
