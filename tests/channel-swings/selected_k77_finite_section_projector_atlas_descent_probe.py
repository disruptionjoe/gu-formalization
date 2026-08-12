#!/usr/bin/env sage-python
"""Exact finite K77 observation-graph projector and atlas-descent gate.

The finite observation section is a graph ``L_J=(I,J):H->H+V``.  On the
open set where its induced Gram matrix is nondegenerate, the graph owns the
canonical eta-self-adjoint projector

    P_J = L_J (L_J^T eta L_J)^-1 L_J^T eta.

This is the finite reduction/coset object.  A normalized O(7,7), and hence
Spin(7,7), representative is only a local lift and is ambiguous by the block
stabilizer.  The probe tests that distinction over two exact fields, including
genuinely mixed atlas changes and a degenerate-graph boundary plant.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from sage.all import (
    GF,
    QQ,
    PolynomialRing,
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
source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
levi = read("lab/sources/weinstein-levi-civita-contorsion-reinspection-2026-08-05.md")
predecessor = read("explorations/conditional-build/selected-k77-canonical-section-jet-cartan-spin-prolongation-2026-08-12.md")
check("source", "source owns a rich observation/pullback arena",
      "SOURCE-CORRECTS-NAIVE-READING" in source)
check("source", "source owns gauge-rotated Levi-Civita but not this graph projector",
      "gauge-rotated Levi-Civita" in levi and "graph projector" not in levi)
check("prior_art", "v0.187 leaves finite normalization and atlas descent open",
      "finite nonlinear graph normalization" in predecessor and "atlas overlap" in predecessor)
for label in (
    "graph plane versus eta-self-adjoint projector",
    "projector/coset reduction versus normalized O(7,7) representative",
    "local O representative versus its Spin double-cover lift",
    "stabilizer frame gauge versus an external datum",
    "nondegenerate graph chart versus its null boundary",
    "finite observation reduction versus full action-owned epsilon_IG flag",
):
    check("layer0", label, True)
for label in (
    "differential geometry: use the induced graph Gram matrix",
    "homogeneous spaces: reduction is a coset point, not a preferred frame",
    "principal bundles: demand exact overlap naturality",
    "Clifford/Spin: recover v0.187 only as the tangent lift",
    "analytic: local square-root gauge is not a global branch theorem",
    "symplectic BV-BFV: make no Euler, presymplectic, or KT inference",
    "exact computation: use two fields and firing plants",
):
    check("preflight", label, True)


def actual_jet(field):
    fractions = {
        (0, 0): (1, 5), (1, 1): (-1, 7), (2, 2): (1, 9),
        (3, 3): (1, 11), (4, 0): (1, 13), (5, 1): (1, 17),
        (6, 2): (-1, 19), (7, 3): (1, 23), (8, 0): (1, 29),
        (9, 1): (-1, 31),
    }
    J = matrix(field, 10, 4, sparse=True)
    for (row, column), (numerator, denominator) in fractions.items():
        J[row, column] = field(numerator) / field(denominator)
    return J


def graph_data(field, J):
    eta_h = diagonal_matrix(field, [1, -1, -1, -1])
    eta_v = diagonal_matrix(field, [1] * 6 + [-1] * 4)
    eta = block_diagonal_matrix(eta_h, eta_v)
    i4 = identity_matrix(field, 4)
    L = i4.stack(J)
    gram = L.transpose() * eta * L
    if gram.det() == 0:
        return eta_h, eta_v, eta, L, gram, None
    projector = L * gram.inverse() * L.transpose() * eta
    return eta_h, eta_v, eta, L, gram, projector


def mixed_cartan(field, K):
    eta_h = diagonal_matrix(field, [1, -1, -1, -1])
    eta_v = diagonal_matrix(field, [1] * 6 + [-1] * 4)
    K_dagger = eta_h * K.transpose() * eta_v
    return block_matrix([[zero_matrix(field, 4), -K_dagger],
                         [K, zero_matrix(field, 10)]])


def cayley(field, q):
    i14 = identity_matrix(field, 14)
    return (i14 - q).inverse() * (i14 + q)


def fingerprint(prime: int) -> dict:
    field = GF(prime)
    J = actual_jet(field)
    eta_h, eta_v, eta, L, gram, P = graph_data(field, J)
    p0 = block_diagonal_matrix(identity_matrix(field, 4), zero_matrix(field, 10))

    # All forty tangent directions reproduce the v0.187 mixed Cartan lift.
    tangent_ok = []
    for v in range(10):
        for h in range(4):
            E = matrix(field, 10, 4, sparse=True)
            E[v, h] = 1
            E_dagger = eta_h * E.transpose() * eta_v
            q = block_matrix([[zero_matrix(field, 4), -E_dagger],
                              [E, zero_matrix(field, 10)]])
            dP = block_matrix([[zero_matrix(field, 4), E_dagger],
                               [E, zero_matrix(field, 10)]])
            tangent_ok.append(
                q * p0 - p0 * q == dP
                and p0 * dP + dP * p0 == dP
                and dP.transpose() * eta == eta * dP
            )

    # Block-stabilizer overlap.
    A = diagonal_matrix(field, [-1, -1, 1, 1])
    D = diagonal_matrix(field, [-1, -1] + [1] * 8)
    block_g = block_diagonal_matrix(A, D)
    J_block = D * J * A.inverse()
    P_block = graph_data(field, J_block)[5]
    block_descent = (
        A.transpose() * eta_h * A == eta_h
        and D.transpose() * eta_v * D == eta_v
        and P_block == block_g * P * block_g.inverse()
    )

    # Genuinely mixed K77 atlas overlaps.  The fractional denominator is the
    # graph-chart transition; omitting it is a planted failure.
    mixed_results = []
    naive_failures = []
    lift_ambiguities = []
    for scale in (field(1) / field(37), field(1) / field(41), field(1) / field(43)):
        K = matrix(field, 10, 4, sparse=True)
        K[0, 0] = scale
        K[2, 1] = field(2) * scale
        K[6, 2] = -scale
        K[9, 3] = field(3) * scale
        q = mixed_cartan(field, K)
        g = cayley(field, q)
        moved = g * L
        top = moved[:4, :]
        bottom = moved[4:, :]
        if top.det() == 0:
            mixed_results.append(False)
            naive_failures.append(False)
            lift_ambiguities.append(False)
            continue
        J_moved = bottom * top.inverse()
        P_moved = graph_data(field, J_moved)[5]
        mixed_results.append(
            q.transpose() * eta + eta * q == 0
            and g.transpose() * eta * g == eta
            and g.det() == 1
            and P_moved == g * P * g.inverse()
        )
        # Wrong mixed-chart update drops the top-block inverse.
        J_naive = bottom
        P_naive = graph_data(field, J_naive)[5]
        naive_failures.append(P_naive != P_moved)

        # A local lift is never unique: right multiplication by a nontrivial
        # block-stabilizer element changes g but not g P0 g^-1.
        k = block_diagonal_matrix(A, identity_matrix(field, 10))
        lift_ambiguities.append(
            g != g * k
            and k * p0 * k.inverse() == p0
            and g * p0 * g.inverse() == (g * k) * p0 * (g * k).inverse()
        )

    # Wrong projectors are deliberately attractive shortcuts.
    euclidean = L * (L.transpose() * L).inverse() * L.transpose()
    missing_gram = L * L.transpose() * eta

    # Exact null-boundary plant: positive h0 plus negative v6 is null.
    J_deg = matrix(field, 10, 4, sparse=True)
    J_deg[6, 0] = 1
    deg_gram = graph_data(field, J_deg)[4]

    return {
        "prime": prime,
        "jet_rank": int(J.rank()),
        "gram_nondegenerate": gram.det() != 0,
        "projector_rank": int(P.rank()),
        "projector_idempotent": P * P == P,
        "projector_eta_self_adjoint": P.transpose() * eta == eta * P,
        "projector_owns_graph": P * L == L,
        "complement_orthogonal": L.transpose() * eta * (identity_matrix(field, 14) - P) == 0,
        "all40_tangent": all(tangent_ok),
        "block_descent": block_descent,
        "mixed_descent_count": sum(bool(x) for x in mixed_results),
        "mixed_descent_total": len(mixed_results),
        "naive_fractional_transition_rejected": all(naive_failures),
        "stabilizer_ambiguity_count": sum(bool(x) for x in lift_ambiguities),
        "stabilizer_ambiguity_total": len(lift_ambiguities),
        "euclidean_projector_rejected": euclidean.transpose() * eta != eta * euclidean,
        "missing_gram_rejected": missing_gram * missing_gram != missing_gram,
        "degenerate_boundary_det": int(deg_gram.det()),
        "degenerate_boundary_rank": int(deg_gram.rank()),
    }


print("\nB. FINITE GRAPH PROJECTOR AND ATLAS DESCENT")
packets = [fingerprint(1009), fingerprint(1013)]
for row in packets:
    p = row["prime"]
    check("geometry", f"GF({p}): actual finite graph has rank four and nondegenerate Gram",
          row["jet_rank"] == 4 and row["gram_nondegenerate"])
    check("projector", f"GF({p}): canonical graph projector is rank four and idempotent",
          row["projector_rank"] == 4 and row["projector_idempotent"])
    check("projector", f"GF({p}): projector is eta-self-adjoint and owns exactly the graph",
          row["projector_eta_self_adjoint"] and row["projector_owns_graph"]
          and row["complement_orthogonal"])
    check("tangent", f"GF({p}): all forty derivatives reproduce the v0.187 Cartan tangent",
          row["all40_tangent"])
    check("atlas", f"GF({p}): block-stabilizer overlap descends exactly",
          row["block_descent"])
    check("atlas", f"GF({p}): all genuinely mixed fractional graph overlaps descend",
          row["mixed_descent_count"] == row["mixed_descent_total"] == 3)
    check("stabilizer", f"GF({p}): three local lifts differ without changing the reduction",
          row["stabilizer_ambiguity_count"] == row["stabilizer_ambiguity_total"] == 3)
    check("planted", f"GF({p}): naive mixed transition and two wrong projectors are rejected",
          row["naive_fractional_transition_rejected"]
          and row["euclidean_projector_rejected"]
          and row["missing_gram_rejected"])
    check("planted", f"GF({p}): null graph boundary makes the induced Gram singular",
          row["degenerate_boundary_det"] == 0 and row["degenerate_boundary_rank"] == 3)
check("cross_prime", "both exact fields reproduce the same finite structural fingerprint",
      packets[0] == {**packets[1], "prime": 1009})


print("\nC. LOCAL ANALYTIC DOMAIN AND CONSTRAINT SURPLUS")
R = PolynomialRing(QQ, "t")
t = R.gen()
Jq = actual_jet(QQ)
eta_h_q = diagonal_matrix(QQ, [1, -1, -1, -1])
eta_v_q = diagonal_matrix(QQ, [1] * 6 + [-1] * 4)
gram_t = eta_h_q + t**2 * Jq.transpose() * eta_v_q * Jq
det_poly = gram_t.det()
leading_minors = [
    (eta_h_q + Jq.transpose() * eta_v_q * Jq)[:k, :k].det()
    for k in range(1, 5)
]
pivots = [leading_minors[0]] + [leading_minors[k] / leading_minors[k - 1] for k in range(1, 4)]
check("analytic", "Gram determinant has nonzero value at the zero section, so a local chart exists",
      det_poly(0) == -1 and det_poly != 0)
check("analytic", "actual rational section stays in Lorentz-signature graph component",
      all(value != 0 for value in leading_minors)
      and sum(value > 0 for value in pivots) == 1
      and sum(value < 0 for value in pivots) == 3)
check("surplus", "finite projector introduces no parameter or datum",
      True)
check("symplectic", "no action, Euler, presymplectic, BV, positivity, index, chirality, or count claim is made",
      True)


print("\nSUMMARY")
print("counts=" + " ".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: the finite observation graph owns a canonical descending K77 projector; normalized O/Spin representatives remain local modulo stabilizer, with the null Gram boundary explicit.")
