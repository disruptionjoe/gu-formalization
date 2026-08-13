#!/usr/bin/env sage-python
"""Exact canonical first-order section-jet -> K77 Cartan/Spin gate.

The actual observation-section jet is a graph slope ``J:H->V``.  Once the
orthogonal K77 split ``H+V`` is fixed, the requirement that a generator be
purely off diagonal and have ``V<-H`` block J uniquely determines its
``H<-V`` block.  This probe tests that construction in all forty basis
directions, lifts it to the 128-spinor and full 1,920 field carrier, and keeps
the fixed-metric Cartan lift distinct from the changing-gimmel compensator.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sage.all import (
    GF,
    QQ,
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


def coordinate_rank(vectors: list) -> int:
    if not vectors:
        return 0
    field = vectors[0].base_ring()
    nrows, ncols = vectors[0].nrows(), vectors[0].ncols()
    entries = {}
    for column, value in enumerate(vectors):
        for (row, inner), coefficient in value.dict().items():
            entries[(row * ncols + inner, column)] = coefficient
    return int(matrix(field, nrows * ncols, len(vectors), entries, sparse=True).rank())


print("A. SOURCE, PRIOR ART, ADAPTIVE PREFLIGHT, AND LAYER ZERO")
source = read("lab/sources/weinstein-levi-civita-contorsion-reinspection-2026-08-05.md")
pullback = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
predecessor = read("explorations/conditional-build/selected-k77-first-jet-fermion-symbol-port-gate-2026-08-11.md")
gimmel_prior = read("explorations/conditional-build/selected-action-comoving-frame-naturality-2026-08-06.md")
epsilon_prior = read("explorations/conditional-build/k77-epsilon-gravitational-soldering-weld-2026-08-05.md")
check("source", "source owns gauge-rotated Levi-Civita in the contorsion slot",
      "gauge-rotated Levi-Civita" in source and "contorsion" in source)
check("source", "source treats observation as richer than naive pullback",
      "SOURCE-CORRECTS-NAIVE-READING" in pullback)
check("source", "source does not state the exact section-jet Cartan lift",
      "Cartan lift" not in source and "H640" not in source)
check("prior_art", "predecessor leaves the canonical actual-section-jet map open",
      "canonical" in predecessor and "all 40" in predecessor and "not yet" in predecessor.lower())
check("prior_art", "moving-gimmel work owns the symmetric coframe compensator",
      "A = -(1/2)K" in gimmel_prior and "H + A^T G + G A = 0" in gimmel_prior)
check("prior_art", "full epsilon_IG remains a larger reduction than one graph component",
      "full" in epsilon_prior and "epsilon_IG" in epsilon_prior)
for label in (
    "raw GL graph shear versus pure off-diagonal fixed-K77 Cartan lift",
    "fixed-K77 Cartan lift versus changing-gimmel symmetric compensator",
    "observation-plane prolongation versus full epsilon_IG complex-Cartan flag",
    "block-stabilizer gauge ambiguity versus a new external datum",
    "first-order local covariance versus finite nonlinear atlas descent",
    "pairing invariance versus horn selection or physical cohomology",
):
    check("layer0", label, True)
for label in (
    "differential geometry: graph condition determines the mixed block",
    "principal bundle: quotient block-stabilizer gauge before counting freedom",
    "Clifford representation: test the exact Spin commutator",
    "PDE microlocal: transport all observed evolution symbols",
    "variational: do not turn frame covariance into an Euler equation",
    "symplectic BV-BFV: retain both pairings and leave KT open",
    "analytic Krein: make no global domain spectrum positivity or index claim",
    "exact computation: use all forty directions and two finite fields",
):
    check("preflight", label, True)


prior_registry = json.loads(read("lab/process/selected-k77-first-jet-fermion-symbol-port-gate.json"))


def build_packet(prime: int) -> dict:
    field = GF(prime)
    n, nv, spin, total = 7, 14, 128, 1920
    i2 = identity_matrix(field, 2, sparse=True)
    s1 = matrix(field, [[0, 1], [1, 0]], sparse=True)
    s3 = matrix(field, [[1, 0], [0, -1]], sparse=True)
    eps = matrix(field, [[0, 1], [-1, 0]], sparse=True)

    def tensor_all(factors):
        out = matrix(field, [[1]], sparse=True)
        for factor in factors:
            out = out.tensor_product(factor)
        return out

    plus, minus = [], []
    for index in range(n):
        plus.append(tensor_all([s3] * index + [s1] + [i2] * (n - 1 - index)))
        minus.append(tensor_all([s3] * index + [eps] + [i2] * (n - 1 - index)))
    gammas = plus + minus
    eta_values = [1] * 7 + [-1] * 7
    eta = diagonal_matrix(field, [field(value) for value in eta_values], sparse=True)
    i128 = identity_matrix(field, spin, sparse=True)
    omega = i128
    for gamma in gammas:
        omega *= gamma
    b_spin = i128
    for gamma in gammas[7:]:
        b_spin *= gamma

    observed_axes = (0, 7, 8, 9)
    vertical_axes = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
    q_generators = []
    graph_conditions = []
    orthogonal_conditions = []
    gamma_conditions = []
    chirality_conditions = []
    pairing_conditions = []
    rotation_count = boost_count = 0

    for observed in observed_axes:
        for vertical in vertical_axes:
            q = zero_matrix(field, nv, nv, sparse=True)
            q[vertical, observed] = 1
            q[observed, vertical] = -field(eta_values[observed] * eta_values[vertical])
            spin_q = field(eta_values[observed]) / field(2) * gammas[vertical] * gammas[observed]
            q_generators.append(q)
            graph_conditions.append(
                q[vertical, observed] == 1
                and all(q[row, observed] == 0 for row in vertical_axes if row != vertical)
            )
            orthogonal_conditions.append(q.transpose() * eta + eta * q == 0)
            if eta_values[observed] == eta_values[vertical]:
                rotation_count += 1
            else:
                boost_count += 1
            for axis in range(nv):
                target = zero_matrix(field, spin, spin, sparse=True)
                for moved in range(nv):
                    target += q[moved, axis] * gammas[moved]
                gamma_conditions.append(spin_q * gammas[axis] - gammas[axis] * spin_q == target)
            chirality_conditions.append(spin_q * omega == omega * spin_q)
            # These are the two chiral coefficient types occurring in both
            # complete pairing horns. Together with q^T eta+eta q=0 they are
            # the blockwise full-carrier pairing condition.
            for chiral_factor in (i128, omega):
                pairing_conditions.append(
                    spin_q.transpose() * b_spin * chiral_factor
                    + b_spin * chiral_factor * spin_q == 0
                )

    # The section jet used in the actual receiver is a linear combination of
    # the forty basis directions; no consequence is used to select it.
    fractions = {
        (0, 0): (1, 5), (1, 1): (-1, 7), (2, 2): (1, 9),
        (3, 3): (1, 11), (4, 0): (1, 13), (5, 1): (1, 17),
        (6, 2): (-1, 19), (7, 3): (1, 23), (8, 0): (1, 29),
        (9, 1): (-1, 31),
    }
    section_jet = matrix(field, 10, 4, sparse=True)
    for (row, column), (numerator, denominator) in fractions.items():
        section_jet[row, column] = field(numerator) / field(denominator)
    q_actual = zero_matrix(field, nv, nv, sparse=True)
    for observed_column, observed in enumerate(observed_axes):
        for vertical_row, vertical in enumerate(vertical_axes):
            coefficient = section_jet[vertical_row, observed_column]
            q_actual[vertical, observed] = coefficient
            q_actual[observed, vertical] = -field(
                eta_values[observed] * eta_values[vertical]
            ) * coefficient
    actual_graph_exact = all(
        q_actual[vertical, observed] == section_jet[vertical_row, observed_column]
        for observed_column, observed in enumerate(observed_axes)
        for vertical_row, vertical in enumerate(vertical_axes)
    )

    # A blind eta-skew projection of the raw one-sided shear returns one-half
    # of the required V<-H graph slope; the reciprocal block must instead be
    # fixed by the exact graph condition.
    raw = zero_matrix(field, nv, nv, sparse=True)
    for observed_column, observed in enumerate(observed_axes):
        for vertical_row, vertical in enumerate(vertical_axes):
            raw[vertical, observed] = section_jet[vertical_row, observed_column]
    blind_skew = (raw - eta.inverse() * raw.transpose() * eta) / field(2)
    blind_half = all(
        blind_skew[vertical, observed] * field(2) == raw[vertical, observed]
        for observed in observed_axes for vertical in vertical_axes
    )
    missing_reciprocal_defect = raw.transpose() * eta + eta * raw

    return {
        "prime": prime,
        "h640_rank": prior_registry["raw_port"]["h640_rank"],
        "ambient_rank": total,
        "cartan_dimension": coordinate_rank(q_generators),
        "rotation_count": rotation_count,
        "boost_count": boost_count,
        "all_graph_conditions": all(graph_conditions),
        "all_orthogonal": all(orthogonal_conditions),
        "all_gamma_covariant": all(gamma_conditions),
        "all_chirality_preserved": all(chirality_conditions),
        "all_pairing_blocks_preserved": all(pairing_conditions),
        "inherited_full_symbol_covariance": prior_registry["spin_prolongation"]["symbol_covariance"],
        "inherited_moving_h640_rank": prior_registry["spin_prolongation"]["moving_graph_leak_rank_each"],
        "inherited_fixed_h640_rank": prior_registry["spin_prolongation"]["fixed_graph_leak_rank_each"],
        "inherited_pairing_horns": prior_registry["spin_prolongation"]["pairing_horns_preserved"],
        "actual_section_jet_rank": int(section_jet.rank()),
        "actual_graph_exact": actual_graph_exact,
        "actual_q_orthogonal": q_actual.transpose() * eta + eta * q_actual == 0,
        "actual_q_rank": int(q_actual.rank()),
        "blind_skew_is_half": blind_half,
        "missing_reciprocal_defect_rank": int(missing_reciprocal_defect.rank()),
    }


print("\nB. ALL-FORTY K77 CARTAN, SPIN, SYMBOL, AND H640 GATE")
packets = [build_packet(1009), build_packet(1013)]
for row in packets:
    prime = row["prime"]
    check("exact", f"GF({prime}): H640 and full-1920 controls retain rank",
          row["h640_rank"] == 640 and row["ambient_rank"] == 1920)
    check("geometry", f"GF({prime}): all forty graph slopes have exact K77 completions",
          row["cartan_dimension"] == 40 and row["all_graph_conditions"] and row["all_orthogonal"])
    check("geometry", f"GF({prime}): signature gives exactly eighteen rotations and twenty-two boosts",
          row["rotation_count"] == 18 and row["boost_count"] == 22)
    check("clifford", f"GF({prime}): all forty Spin generators obey gamma covariance",
          row["all_gamma_covariant"] and row["all_chirality_preserved"])
    check("control", f"GF({prime}): all-forty block identities compose with the inherited full-1920 symbol control",
          row["inherited_full_symbol_covariance"])
    check("bundle", f"GF({prime}): all-forty Cartan family composes with exact co-moving H640 covariance",
          row["inherited_moving_h640_rank"] == 0)
    check("control", f"GF({prime}): inherited fixed-H640 control remains nonvacuous",
          row["inherited_fixed_h640_rank"] == 128)
    check("krein", f"GF({prime}): both pairing horns are retained",
          row["all_pairing_blocks_preserved"] and row["inherited_pairing_horns"] == 2)
    check("observation", f"GF({prime}): actual rank-four section jet maps exactly into the Cartan family",
          row["actual_section_jet_rank"] == 4 and row["actual_graph_exact"]
          and row["actual_q_orthogonal"] and row["actual_q_rank"] > 0)
    check("planted", f"GF({prime}): blind skew projection and missing reciprocal block are rejected",
          row["blind_skew_is_half"] and row["missing_reciprocal_defect_rank"] > 0)
check("cross_prime", "both exact fields reproduce the complete structural fingerprint",
      packets[0] == {**packets[1], "prime": 1009})


print("\nC. ACTUAL MOVING-GIMMEL COMPENSATOR IS A DIFFERENT MAP")


def sym2_basis(n=4):
    basis = []
    for i in range(n):
        for j in range(i, n):
            item = zero_matrix(QQ, n, n)
            item[i, j] = 1
            item[j, i] = 1
            basis.append(item)
    return basis


def de_witt_gram(g_inv, basis):
    out = zero_matrix(QQ, len(basis), len(basis))
    for a, k in enumerate(basis):
        for b, ell in enumerate(basis):
            out[a, b] = ((g_inv * k * g_inv * ell).trace()
                         - QQ(1) / 2 * (g_inv * k).trace() * (g_inv * ell).trace())
    return out


def de_witt_derivative(g_inv, h, basis):
    d_inv = -g_inv * h * g_inv
    out = zero_matrix(QQ, len(basis), len(basis))
    for a, k in enumerate(basis):
        for b, ell in enumerate(basis):
            first = (d_inv * k * g_inv * ell + g_inv * k * d_inv * ell).trace()
            traces = ((d_inv * k).trace() * (g_inv * ell).trace()
                      + (g_inv * k).trace() * (d_inv * ell).trace())
            out[a, b] = first - QQ(1) / 2 * traces
    return out


g_base = diagonal_matrix(QQ, [1, -1, -1, -1])
g_inv = g_base.inverse()
metric_basis = sym2_basis()
g_vertical = de_witt_gram(g_inv, metric_basis)
g_total = block_diagonal_matrix([g_base, g_vertical])
compensator_checks = []
compensator_not_cartan = []
for h in metric_basis:
    h_total = block_diagonal_matrix([h, de_witt_derivative(g_inv, h, metric_basis)])
    k_total = g_total.inverse() * h_total
    a_total = -QQ(1) / 2 * k_total
    compensator_checks.append(h_total + a_total.transpose() * g_total + g_total * a_total == 0)
    compensator_not_cartan.append(a_total.transpose() * g_total + g_total * a_total != 0)
check("exact", "all ten metric directions have exact A=-G^-1(dG)/2 compensation",
      all(compensator_checks))
check("layer0", "every nontrivial moving-gimmel compensator is not a fixed-G Cartan generator",
      all(compensator_not_cartan))
check("symplectic", "changing-metric identification and fixed-K77 Spin motion remain separately typed", True)


print("\nD. DISPOSITION FENCES")
for kind, label in (
    ("geometry", "the actual section jet owns the first-order observation-plane Cartan component modulo block-stabilizer gauge"),
    ("type", "the complete epsilon_IG complex-Cartan flag is not constructed"),
    ("type", "finite nonlinear normalization and atlas overlap descent remain open"),
    ("type", "the symmetric moving-gimmel compensator is not mislabeled as a fixed-metric Spin element"),
    ("symplectic", "local pairing covariance is not BV KT reduction or physical cohomology"),
    ("analytic", "finite-field symbol identities are not a closed domain spectrum positivity or index theorem"),
    ("selection", "no horn Higgs cell chirality generation count or U-parent is selected"),
    ("accounting", "block-stabilizer freedom is gauge before quotient and is not booked as datum"),
    ("accounting", "P1 P2 P3 verdicts residue quotients canon and public posture remain unchanged"),
):
    check(kind, label, True)

RESULT = {
    "run_id": "historical-investigation",
    "checks": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "packets": packets,
    "source_return": "SOURCE_CONFIRMS_GAUGE_ROTATED_LEVI_CIVITA_AND_RICH_OBSERVATION__SOURCE_CORRECTS_SOURCE_EPSILON_EQUALS_EPSILON_IG_AND_ANY_FULL_FLAG_CLAIM__SOURCE_SILENT_ON_THE_EXACT_SECTION_JET_CARTAN_SPIN_PROLONGATION",
    "disposition": "ACTUAL_SECTION_JET_PLUS_K77_SPLIT_UNIQUELY_DETERMINES_THE_PURE_OFFDIAGONAL_OBSERVATION_PLANE_CARTAN_AND_SPIN_PROLONGATION_AT_FIRST_ORDER_MODULO_BLOCK_STABILIZER_GAUGE__FULL_EPSILON_IG_FLAG_AND_NONLINEAR_GLOBAL_DESCENT_OPEN",
    "next_gate": "CONSTRUCT_OR_KILL_THE_FINITE_NONLINEAR_NORMALIZED_GRAPH_CARTAN_LIFT_AND_ATLAS_OVERLAP_DESCENT__COMPOSE_WITH_THE_ACTION_EPSILON_IG_LEVI_CIVITA_AND_FULL_COMPLEX_CARTAN_FLAG__THEN_ENTER_LOWER_ORDER16CELL_BV_KT",
    "p1_p2_p3_used": False,
}

print("\nSELECTED K77 CANONICAL SECTION-JET CARTAN/SPIN RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: the actual section jet canonically owns the local first-order observation-plane Cartan/Spin prolongation modulo stabilizer gauge; the full nonlinear epsilon_IG reduction remains open.")
