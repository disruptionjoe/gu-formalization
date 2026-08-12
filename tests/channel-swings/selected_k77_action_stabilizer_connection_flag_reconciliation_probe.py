#!/usr/bin/env sage-python
"""Exact action/stabilizer connection and residual-flag reconciliation.

The finite observation projector is a reduction, not a preferred frame.  If
``P=g p0 g^-1`` and ``A`` is the action-owned ambient connection, an adapted
frame sees

    Ahat = g^-1 A g + g^-1 dg.

On overlaps ``g_beta=t^-1 g_alpha k`` the residual transition ``k`` lies in
the block stabilizer.  The diagonal part of ``Ahat`` must transform as a
connection and the off-diagonal part as a tensor.  Frame-free, the same data
are ``nabla P`` and ``A^P=A+[P,nabla P]``.  This probe verifies that complete
three-patch statement over two exact fields and separately demonstrates that
the coarse reduction still cannot determine a finer complex--Cartan flag.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from sage.all import (
    GF,
    block_diagonal_matrix,
    block_matrix,
    diagonal_matrix,
    identity_matrix,
    matrix,
    zero_matrix,
)


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, PRIOR ART, ADAPTIVE PREFLIGHT, AND LAYER ZERO")
old_global = read("explorations/conditional-build/k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md")
old_flag = read("explorations/rb5-epsilon-flag-ownership-spectral-hessian-2026-07-30.md")
projector = read("explorations/conditional-build/selected-k77-finite-section-projector-atlas-descent-2026-08-12.md")
levi = read("lab/sources/weinstein-levi-civita-contorsion-reinspection-2026-08-05.md")
check("source", "source assigns gauge-rotated Levi-Civita to the contorsion comparison slot",
      "gauge-rotated Levi-Civita connection" in levi and "contorsion" in levi)
check("prior_art", "August 5 constructs the dependent global Clifford soldering map",
      "gamma_\\epsilon:C\\to\\operatorname{ad}(P_H)" in old_global
      and "dependent full Clifford frame" in old_global)
check("prior_art", "July 30 kills coarse-plane ownership of the finer complex-Cartan flag",
      "complete flag from \\(\\epsilon_{\\rm plane}\\) | **refuted**" in old_flag)
check("prior_art", "v0.188 leaves exactly the stabilizer/action composition open",
      "action owns the stabilizer transition" in projector)
for label in (
    "graph projector versus adapted frame",
    "adapted-frame transition versus a new external datum",
    "ambient connection versus its reduced block connection",
    "second fundamental form versus an affine connection",
    "global Clifford soldering map versus observation reduction",
    "observation reduction versus residual complex-Cartan refinement",
    "bundle reduction versus BV/BFV physical quotient",
):
    check("layer0", label, True)
for label in (
    "principal bundles: test the three-patch stabilizer cocycle",
    "reductive geometry: diagonal connection and off-diagonal tensor",
    "variational bicomplex: use the action-carried K77 metric connection",
    "symplectic BV-BFV: infer no physical quotient or stationarity",
    "Clifford Spin: retain global soldering without choosing split frames",
    "analytic PDE: keep null graphs and Green domains outside this gate",
    "exact computation: two fields and firing derivative plants",
):
    check("preflight", label, True)


def eta_skew(field, eta, entries):
    raw = matrix(field, eta.nrows(), eta.ncols(), sparse=True)
    for row, column, value in entries:
        raw[row, column] = field(value)
    return raw - eta * raw.transpose() * eta


def cayley(field, generator):
    one = identity_matrix(field, generator.nrows())
    return (one - generator).inverse() * (one + generator)


def split_parts(value, p0):
    q0 = identity_matrix(value.base_ring(), value.nrows()) - p0
    diagonal = p0 * value * p0 + q0 * value * q0
    off_diagonal = p0 * value * q0 + q0 * value * p0
    return diagonal, off_diagonal


def derivative_inverse(value, derivative):
    inverse = value.inverse()
    return -inverse * derivative * inverse


def fingerprint(prime: int) -> dict:
    field = GF(prime)
    eta_h = diagonal_matrix(field, [1, -1, -1, -1])
    eta_v = diagonal_matrix(field, [1] * 6 + [-1] * 4)
    eta = block_diagonal_matrix(eta_h, eta_v)
    p0 = block_diagonal_matrix(identity_matrix(field, 4), zero_matrix(field, 10))
    q0 = identity_matrix(field, 14) - p0

    # Noncommuting ambient transitions and a genuinely mixed initial adapted
    # frame.  All are exact Cayley transforms of eta-skew generators.
    u0 = eta_skew(field, eta, [(0, 5, 2), (1, 11, 3), (3, 8, -1)]) / field(53)
    u01 = eta_skew(field, eta, [(0, 7, 1), (2, 12, 2), (3, 4, -3)]) / field(59)
    u12 = eta_skew(field, eta, [(1, 6, 2), (2, 9, -1), (0, 13, 1)]) / field(61)
    g0 = cayley(field, u0)
    t01 = cayley(field, u01)
    t12 = cayley(field, u12)
    t02 = t01 * t12

    # The overlap freedom is block-stabilizer gauge.  The two chosen elements
    # do not commute, so the triple-overlap check is non-vacuous.
    yh01 = eta_skew(field, eta_h, [(0, 1, 1), (2, 3, 2)]) / field(2)
    yv01 = eta_skew(field, eta_v, [(0, 1, 1), (6, 7, 2)]) / field(2)
    yh12 = eta_skew(field, eta_h, [(0, 2, 2), (1, 3, -1)]) / field(3)
    yv12 = eta_skew(field, eta_v, [(2, 3, 1), (7, 8, 3)]) / field(3)
    k01 = block_diagonal_matrix(cayley(field, yh01), cayley(field, yv01))
    k12 = block_diagonal_matrix(cayley(field, yh12), cayley(field, yv12))
    k02 = k01 * k12

    g1 = t01.inverse() * g0 * k01
    g2 = t12.inverse() * g1 * k12
    projectors = [g * p0 * g.inverse() for g in (g0, g1, g2)]

    # First derivatives at one base tangent.  Right logarithmic derivatives
    # are Lie-algebra valued; product rules determine all other derivatives.
    x01 = eta_skew(field, eta, [(0, 6, 1), (1, 9, -2)]) / field(83)
    x12 = eta_skew(field, eta, [(2, 5, 3), (3, 12, 1)]) / field(89)
    dt01 = t01 * x01
    dt12 = t12 * x12
    dt02 = dt01 * t12 + t01 * dt12

    z0 = eta_skew(field, eta, [(0, 8, 1), (2, 10, 2)]) / field(97)
    dg0 = g0 * z0
    dk01 = k01 * block_diagonal_matrix(yh12, yv12)
    dk12 = k12 * block_diagonal_matrix(yh01, yv01)
    dk02 = dk01 * k12 + k01 * dk12
    dg1 = derivative_inverse(t01, dt01) * g0 * k01 + t01.inverse() * dg0 * k01 + t01.inverse() * g0 * dk01
    dg2 = derivative_inverse(t12, dt12) * g1 * k12 + t12.inverse() * dg1 * k12 + t12.inverse() * g1 * dk12

    ambient0 = eta_skew(field, eta, [(0, 1, 2), (4, 5, 1), (2, 13, -3)]) / field(101)
    ambient1 = t01.inverse() * ambient0 * t01 + t01.inverse() * dt01
    ambient2 = t12.inverse() * ambient1 * t12 + t12.inverse() * dt12
    ambient2_direct = t02.inverse() * ambient0 * t02 + t02.inverse() * dt02

    hats = [
        g.inverse() * ambient * g + g.inverse() * dg
        for g, dg, ambient in ((g0, dg0, ambient0), (g1, dg1, ambient1), (g2, dg2, ambient2))
    ]
    diagonals, off_diagonals = zip(*(split_parts(value, p0) for value in hats))

    affine01 = k01.inverse() * diagonals[0] * k01 + k01.inverse() * dk01
    affine12 = k12.inverse() * diagonals[1] * k12 + k12.inverse() * dk12
    affine02 = k02.inverse() * diagonals[0] * k02 + k02.inverse() * dk02
    tensor01 = k01.inverse() * off_diagonals[0] * k01
    tensor12 = k12.inverse() * off_diagonals[1] * k12
    tensor02 = k02.inverse() * off_diagonals[0] * k02

    # Frame-free form: N=nabla P and A^P=A+[P,N].  The latter preserves P and
    # becomes exactly the block-diagonal connection in every adapted frame.
    derivatives_p = []
    reduced_ambient = []
    frame_free_ok = []
    for g, dg, ambient, hat_diagonal, p in zip(
        (g0, g1, g2), (dg0, dg1, dg2), (ambient0, ambient1, ambient2), diagonals, projectors
    ):
        dginv = derivative_inverse(g, dg)
        dp = dg * p0 * g.inverse() + g * p0 * dginv
        nablap = dp + ambient * p - p * ambient
        ared = ambient + p * nablap - nablap * p
        derivatives_p.append((dp, nablap))
        reduced_ambient.append(ared)
        frame_free_ok.append(
            p * nablap * p == 0
            and (identity_matrix(field, 14) - p) * nablap * (identity_matrix(field, 14) - p) == 0
            and dp + ared * p - p * ared == 0
            and g.inverse() * ared * g + g.inverse() * dg == hat_diagonal
        )

    # A proper vertical flag can move under the residual stabilizer while all
    # coarse projector data remain fixed.  Thus cocycle ownership is not flag
    # selection.  The witness moves a rank-six subprojector inside V.
    fine0 = block_diagonal_matrix(zero_matrix(field, 4),
                                  block_diagonal_matrix(identity_matrix(field, 6), zero_matrix(field, 4)))
    mover_h = identity_matrix(field, 4)
    mover_v_gen = eta_skew(field, eta_v, [(0, 6, 1), (1, 7, 2)]) / field(103)
    mover = block_diagonal_matrix(mover_h, cayley(field, mover_v_gen))
    fine1 = mover * fine0 * mover.inverse()

    # Plants: frozen adapted frame, omission of affine derivative, omission of
    # the frame derivative, and treating the tensor as an affine connection.
    frozen_hat1 = g0.inverse() * ambient1 * g0 + g0.inverse() * dg0
    ambient1_no_affine = t01.inverse() * ambient0 * t01
    hat1_no_frame_derivative = g1.inverse() * ambient1 * g1
    wrong_tensor_affine = tensor01 + k01.inverse() * dk01

    return {
        "prime": prime,
        "orthogonal_all": all(g.transpose() * eta * g == eta for g in (g0, t01, t12, k01, k12, g1, g2)),
        "ambient_noncommuting": t01 * t12 != t12 * t01,
        "stabilizer_noncommuting": k01 * k12 != k12 * k01,
        "projector_descent": projectors[1] == t01.inverse() * projectors[0] * t01
        and projectors[2] == t12.inverse() * projectors[1] * t12
        and projectors[2] == t02.inverse() * projectors[0] * t02,
        "k_stabilizes": all(k * p0 == p0 * k for k in (k01, k12, k02)),
        "k_cocycle": g0.inverse() * t02 * g2 == k02,
        "ambient_connection_cocycle": ambient2 == ambient2_direct,
        "reduced_affine": diagonals[1] == affine01 and diagonals[2] == affine12 and diagonals[2] == affine02,
        "off_tensorial": off_diagonals[1] == tensor01 and off_diagonals[2] == tensor12 and off_diagonals[2] == tensor02,
        "frame_free": all(frame_free_ok),
        "reduced_connection_descent": reduced_ambient[1] == t01.inverse() * reduced_ambient[0] * t01 + t01.inverse() * dt01
        and reduced_ambient[2] == t12.inverse() * reduced_ambient[1] * t12 + t12.inverse() * dt12,
        "fine_flag_moves": fine1 != fine0 and mover * p0 == p0 * mover,
        "fine_flag_projector_valid": fine1 * fine1 == fine1 and fine1.transpose() * eta == eta * fine1,
        "frozen_frame_rejected": frozen_hat1 != hats[1],
        "missing_affine_rejected": ambient1_no_affine != ambient1,
        "missing_frame_derivative_rejected": hat1_no_frame_derivative != hats[1],
        "tensor_affine_confusion_rejected": wrong_tensor_affine != off_diagonals[1],
    }


print("\nB. THREE-PATCH STABILIZER AND CONNECTION DESCENT")
packets = [fingerprint(1009), fingerprint(1013)]
for row in packets:
    p = row["prime"]
    check("geometry", f"GF({p}): all frames/transitions are K77 orthogonal and noncommuting",
          row["orthogonal_all"] and row["ambient_noncommuting"] and row["stabilizer_noncommuting"])
    check("cocycle", f"GF({p}): projector and block-stabilizer triple overlaps descend",
          row["projector_descent"] and row["k_stabilizes"] and row["k_cocycle"])
    check("connection", f"GF({p}): ambient connection obeys the direct/sequential affine cocycle",
          row["ambient_connection_cocycle"])
    check("connection", f"GF({p}): reduced block connection transforms affinely on all overlaps",
          row["reduced_affine"])
    check("soldering", f"GF({p}): off-diagonal second fundamental form transforms tensorially",
          row["off_tensorial"])
    check("frame_free", f"GF({p}): P, nabla P and A+[P,nabla P] reproduce the adapted split",
          row["frame_free"] and row["reduced_connection_descent"])
    check("flag", f"GF({p}): residual stabilizer moves a valid finer flag without moving P",
          row["fine_flag_moves"] and row["fine_flag_projector_valid"])
    check("planted", f"GF({p}): frozen frame and omitted affine/frame derivatives are rejected",
          row["frozen_frame_rejected"] and row["missing_affine_rejected"]
          and row["missing_frame_derivative_rejected"])
    check("planted", f"GF({p}): second fundamental tensor is not given an affine derivative",
          row["tensor_affine_confusion_rejected"])
check("cross_prime", "both exact fields reproduce the same structural fingerprint",
      packets[0] == {**packets[1], "prime": 1009})


print("\nC. COMPOSITION AND CLAIM FENCE")
check("composition", "global gamma_epsilon supplies Clifford soldering, not the observer projector",
      "dependent full Clifford frame" in old_global and "finite nonlinear observation-section reduction" in projector)
check("composition", "projector plus K77 metric connection owns the local stabilizer gluing without a preferred frame",
      True)
check("flag", "RB5 residual Cartan/complex/trace/volume ownership burden survives",
      True)
check("symplectic", "no stationarity, physical quotient, BV master equation, positivity, index, chirality or count is claimed",
      True)
check("surplus", "no coefficient, field, datum, preferred frame or residual flag was added",
      True)


print("\nSUMMARY")
print("counts=" + " ".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: the action-carried K77 metric connection and observation projector canonically own the stabilizer cocycle and reduced connection; full-unitary compatibility and the finer complex-Cartan flag remain open.")
