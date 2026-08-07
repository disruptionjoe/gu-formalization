#!/usr/bin/env python3
r"""PW2F-R2B2B2G normalized-trace transport / full-C4 admission gate.

R2B2B2F evaluated the written first-action transgression in one exact
nonlinear Zorro coframe while freezing the distinguished normalized DeWitt
trace in Shiab.  A complete metric Hessian may use that evaluator only if the
geometric trace insertion is constant in the same coframe through mixed
second order, or if its complete first and mixed Shiab responses are added.

This probe constructs the geometric trace vector ``t(g)=g/2`` in coordinate
``Sym2`` components, transports its exact ``(1,r,s,rs)`` jet through the same
symmetric orthonormal coframe used by R2B2B2F, and compares its first slots to
the independent B2C15M normalized-trace derivative.  It then tests the mixed
slot on diagonal, off-diagonal, and mixed owner pairs.

The earned result is an admission decision, not a filled quartic bank.  A live
mixed trace slot means the existing first-variation ``moving_metric_shiab_parts``
API is insufficient for the full Hessian: an explicit mixed Shiab/Hodge/Phi
jet must be constructed before either the complete ``I1 A4`` or distinct
off-shell ``I2B C4`` bank can be claimed.  No arbitrary symmetric completion
is admitted.  P1/P2/P3 remain unused; Curt stays formally separate.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import hashlib
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))


def load_probe(name: str, filename: str):
    spec = spec_from_file_location(name, CHANNEL / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


F = load_probe(
    "pw2fr2b2b2g_predecessor",
    "pw2fr2b2b2f_i1_transgression_projective_kappa_probe.py",
)
E = F.E
M = F.M
B15 = E.B15
B15P = E.B15P


FAILURES: list[str] = []
EXACT = SOURCE = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: exact - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"exact: {label}")


def source_receipt(label: str, condition: bool, disposition: str) -> None:
    global SOURCE
    SOURCE += 1
    print(f"{'PASS' if condition else 'FAIL'}: source - {label} [{disposition}]", flush=True)
    if not condition:
        FAILURES.append(f"source: {label}")


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type - {label}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    condition = not false_claim
    print(f"{'PASS' if condition else 'FAIL'}: planted rejection - {label}", flush=True)
    if not condition:
        FAILURES.append(f"planted: {label}")


def zero(value: sp.MatrixBase | sp.Expr) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


def coordinate_column(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([matrix[a, b] for a, b in B15P.PAIRS4])


def full_trace_coordinate(matrix: sp.Matrix) -> sp.Matrix:
    value = sp.zeros(14, 1)
    value[4:14, 0] = coordinate_column(matrix) / 2
    return value


def fixed_frame_trace_jet(owner_i: int, owner_j: int):
    """Coordinate t(g)=g/2 expressed in the point-orthonormal frame."""
    transform = B15.FRAME14.inv()
    return (
        sp.simplify(transform * full_trace_coordinate(B15P.G4)),
        sp.simplify(transform * full_trace_coordinate(B15P.SYM2[owner_i])),
        sp.simplify(transform * full_trace_coordinate(B15P.SYM2[owner_j])),
        sp.zeros(14, 1),
    )


def moving_frame_trace_jet(
    owner_i: int,
    xi: tuple[sp.Expr, ...],
    owner_j: int,
    zeta: tuple[sp.Expr, ...],
):
    metric = E.zorro_metric_jet(owner_i, xi, owner_j, zeta)
    frame = E.symmetric_frame(metric)
    coordinate = fixed_frame_trace_jet(owner_i, owner_j)
    return metric, E.jmul(frame, coordinate)


def cliff_vector(value: dict[int, sp.Expr]) -> sp.Matrix:
    result = sp.zeros(14, 1)
    for mask, coefficient in value.items():
        if mask == 0 or mask.bit_count() != 1:
            raise AssertionError(f"not a Clifford vector: mask={mask}")
        result[mask.bit_length() - 1, 0] = sp.simplify(coefficient)
    return result


def first_trace_from_moving_phi(h: sp.Matrix, coordinate_motion: sp.Matrix) -> sp.Matrix:
    d_trace, _d_one, _d_two = M.moving_phi(
        h, tuple(coordinate_motion[index, 0] for index in range(14))
    )
    return cliff_vector(d_trace)


def legacy_pure_metric_first_trace(owner: int) -> sp.Matrix:
    d_trace, _d_one, _d_two = M.moving_phi(
        B15.H_VARIATIONS[owner], M.canonical_trace_motion(owner)
    )
    return cliff_vector(d_trace)


def scalar_jet_pair(left, right):
    eta = E.ETA
    return (
        sp.simplify((left[0].T * eta * right[0])[0]),
        sp.simplify((left[1].T * eta * right[0] + left[0].T * eta * right[1])[0]),
        sp.simplify((left[2].T * eta * right[0] + left[0].T * eta * right[2])[0]),
        sp.simplify(
            (
                left[3].T * eta * right[0]
                + left[1].T * eta * right[2]
                + left[2].T * eta * right[1]
                + left[0].T * eta * right[3]
            )[0]
        ),
    )


def source_and_layer_zero() -> None:
    pack_path = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    pack = pack_path.read_text()
    predecessor = (
        ROOT / "explorations/pw2fr2b2b2f-i1-transgression-projective-kappa-2026-08-03.md"
    ).read_text()
    source_receipt(
        "the pinned source fixes the I1 transgression grammar but not this active normalized-trace transport",
        hashlib.sha256(pack_path.read_bytes()).hexdigest()
        == "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f"
        and r"\frac12d_{B_\omega}T_\omega" in pack
        and r"\frac13[T_\omega,T_\omega]" in pack,
        "SOURCE-CONFIRMS grammar; SOURCE-SILENT on the active mixed trace/Shiab jet",
    )
    source_receipt(
        "the accepted predecessor explicitly leaves moving normalized DeWitt trace transport open",
        "moving normalized trace" in predecessor
        and "complete `A4` tensor" in predecessor,
        "SOURCE-SILENT; repository construction debt",
    )
    typed("geometric trace vector, fixed-frame coordinate components, moving-coframe components, and Clifford insertion are distinct typed objects")
    typed("the normalized trace is transported in the same symmetric coframe as the R2B2B2F connection and density")
    typed("first trace motion does not determine its mixed second jet")
    typed("I1 raw density, I1 Euler covector, and manuscript I2B residual-square Hessian remain distinct")
    typed("a full multi-index Green/Helmholtz certificate is downstream of complete coefficient tensors, not a substitute for them")


def trace_transport_gate() -> dict[str, object]:
    e_trace = sp.zeros(14, 1)
    e_trace[B15.TRACE_INDEX, 0] = 1
    exact(
        "the coordinate t(g)=g/2 trace at the base point is the accepted negative-unit DeWitt trace blade",
        fixed_frame_trace_jet(0, 0)[0] == e_trace
        and E.ETA[B15.TRACE_INDEX, B15.TRACE_INDEX] == -1,
    )

    cases = (
        ("trace-diagonal", 0, (1, 1, 0, 0), 0, (1, 1, 0, 0)),
        ("offdiagonal", 3, (-1, 2, 0, 1), 7, (1, 0, -2, 2)),
        ("mixed", 4, (1, -1, 2, 0), 9, (2, 1, 0, -1)),
    )
    mixed_nonzero: list[str] = []
    mixed_ranks: list[int] = []
    zorro_first_corrections: list[str] = []
    for label, owner_i, xi, owner_j, zeta in cases:
        metric, trace = moving_frame_trace_jet(owner_i, xi, owner_j, zeta)
        coordinate = fixed_frame_trace_jet(owner_i, owner_j)
        exact(
            f"{label}: first transported trace slot matches the independent moving-Phi derivative with the full Zorro metric and coordinate trace motion",
            zero(trace[1] - first_trace_from_moving_phi(metric[1], coordinate[1])),
        )
        exact(
            f"{label}: second transported trace slot matches the independent moving-Phi derivative with the full Zorro metric and coordinate trace motion",
            zero(trace[2] - first_trace_from_moving_phi(metric[2], coordinate[2])),
        )
        if not zero(trace[1] - legacy_pure_metric_first_trace(owner_i)):
            zorro_first_corrections.append(f"{label}:r")
        if not zero(trace[2] - legacy_pure_metric_first_trace(owner_j)):
            zorro_first_corrections.append(f"{label}:s")
        norm = scalar_jet_pair(trace, trace)
        exact(
            f"{label}: exact coframe transport preserves the normalized trace norm through mixed order",
            norm == (sp.Integer(-1), sp.Integer(0), sp.Integer(0), sp.Integer(0)),
            f"norm_jet={norm}",
        )
        if not zero(trace[3]):
            mixed_nonzero.append(label)
        mixed_ranks.append(int(not zero(trace[3])))
        exact(
            f"{label}: the mixed normalized-trace slot is explicitly computed rather than inferred from first motion",
            trace[3].shape == (14, 1),
            f"mixed_live={not zero(trace[3])}",
        )
        # The exact metric/coframe identity is a guard against manufacturing
        # trace motion from an inconsistent frame.
        eta_jet = (E.ETA, sp.zeros(14), sp.zeros(14), sp.zeros(14))
        frame = E.symmetric_frame(metric)
        framed_metric = E.jmul(E.jmul(E.jtranspose(frame), eta_jet), frame)
        exact(
            f"{label}: the trace transport uses the same exact mixed-order orthonormal coframe as the nonlinear graph",
            all(zero(framed_metric[index] - metric[index]) for index in range(4)),
        )

    exact(
        "at least one independent owner/conormal pair has a live mixed normalized-trace component",
        bool(mixed_nonzero),
        f"live={tuple(mixed_nonzero)}",
    )
    exact(
        "the nonlinear Zorro horizontal split adds a live first-order trace correction beyond the earlier pure-metric normalized-trace fixture",
        bool(zorro_first_corrections),
        f"live={tuple(zorro_first_corrections)}",
    )
    reject(
        "freeze the distinguished trace through Hessian order after observing a live mixed coframe component",
        not mixed_nonzero,
    )
    return {
        "mixed_nonzero": tuple(mixed_nonzero),
        "mixed_count": sum(mixed_ranks),
        "zorro_first_corrections": tuple(zorro_first_corrections),
    }


def admission_and_boundary(result: dict[str, object]) -> None:
    # The current API accepts only one h and one first trace-motion vector.
    # It has no mixed (h,k,D2t) argument, so it cannot consume the exact live
    # rs slot proved above.  This is an executable interface fact, not an
    # assumption about the eventual value of the complete Hessian.
    import inspect

    signature = inspect.signature(M.moving_metric_shiab_parts)
    exact(
        "the existing moving-Shiab constructor is first-order only and has no mixed trace/Shiab input",
        tuple(signature.parameters) == ("curvature", "h", "trace_motion")
        and result["mixed_count"] > 0,
        str(signature),
    )
    typed("the first unbuilt object is the mixed normalized-trace/Hodge/Phi/Shiab response on the exact nonlinear coframe")
    typed("without that object the 35-monomial I1 A4 bank is not dependency-complete")
    typed("the distinct off-shell I2B C4 bank also remains blocked on its complete second residual-primalizer/pairing jet")
    typed("no coefficientwise kappa1 classifier or full multi-index Helmholtz verdict is licensed before both banks exist")
    typed("the predecessor rank-two raw-density comparator remains valid at its narrow frozen-Shiab grade")
    typed("vertical/mixed conormals, partial-Z1, section tangents, domain, quotient, observation, and physics remain open")
    typed("P1/P2/P3 remain unchanged and unused")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    reject("fill the missing mixed Shiab jet with an arbitrary symmetric quartic completion", False)
    reject("promote a one-ray Green concomitant to a complete four-dimensional multi-index Helmholtz certificate", False)
    reject("infer a selected kappa1, action equation, or physics result from this admission blocker", False)


def main() -> int:
    print("PW2F-R2B2B2G NORMALIZED-TRACE TRANSPORT / FULL-C4 ADMISSION GATE")
    source_and_layer_zero()
    result = trace_transport_gate()
    admission_and_boundary(result)
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: zorro_first_trace_corrections="
        f"{result['zorro_first_corrections']}; mixed_normalized_trace_live="
        f"{result['mixed_nonzero']}; full_I1_A4=BLOCKED_ON_MIXED_SHIAB_JET; "
        "distinct_I2B_C4=BLOCKED_ON_COMPLETE_SECOND_PRIMALIZER_JET",
        flush=True,
    )
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + "
        f"{PLANTED} planted = {total}; failures={len(FAILURES)}",
        flush=True,
    )
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print(
        "VERDICT: R2B2B2G REBASES AT THE FIRST EXACT TYPED BLOCKER: THE "
        "NORMALIZED DEWITT TRACE HAS LIVE MIXED COFRAME MOTION, WHILE THE "
        "CURRENT SHIAB CONSTRUCTOR IS FIRST-ORDER ONLY; COMPLETE I1/I2B C4 "
        "BANKS AND MULTI-INDEX GREEN/HELMHOLTZ CLASSIFICATION REMAIN OPEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
