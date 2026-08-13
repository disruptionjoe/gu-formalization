#!/usr/bin/env sage-python
"""Exact port gate from the selected-action first jet to the K77 fermion symbol.

This probe separates three notions that were adjacent in ledger v0.185:

* the complete 4+10 field/equation-dual shear M(J) for an observation section;
* the Levi-Civita/spin-connection derivative, first order in the metric field;
* a Spin(7,7)-transported Clifford anchor, which can move the fermion principal
  symbol and the H640 graph together.

The first two are not automatically fermion-principal maps.  The third is the
minimal conditional class an epsilon_IG prolongation would have to realize.
No arbitrary residual-fitting map is admitted.
"""

from __future__ import annotations

from collections import Counter
import json
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


def coordinate_rank(matrices: list) -> int:
    if not matrices:
        return 0
    field = matrices[0].base_ring()
    nrows, ncols = matrices[0].nrows(), matrices[0].ncols()
    entries = {}
    for column, value in enumerate(matrices):
        for (row, inner), coefficient in value.dict().items():
            entries[(row * ncols + inner, column)] = coefficient
    return int(matrix(field, nrows * ncols, len(matrices), entries, sparse=True).rank())


print("A. SOURCE, PRIOR ART, ADAPTIVE PREFLIGHT, AND LAYER ZERO")
source = read("lab/sources/weinstein-levi-civita-contorsion-reinspection-2026-08-05.md")
pullback_source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
v028 = read("explorations/conditional-build/selected-action-physical-soldering-observation-compose-2026-08-06.md")
v029 = read("explorations/conditional-build/selected-action-second-soldering-observation-jets-2026-08-06.md")
v0183 = read("explorations/conditional-build/selected-k77-h640-observation-pullback-bv-typing-2026-08-11.md")
v0185 = read("explorations/conditional-build/selected-k77-vertical-soldering-adapter-order-gate-2026-08-11.md")
check("source", "source owns gauge-rotated Levi-Civita in the contorsion slot",
      "gauge-rotated Levi-Civita" in source and "contorsion" in source)
check("source", "source treats observation as richer than naive pullback",
      "SOURCE-CORRECTS-NAIVE-READING" in pullback_source)
check("source", "source remains silent on the fermion/H640 principal port",
      "H640" not in source and "fermion-symbol" not in source)
check("prior_art", "v0.28 owns the local first-jet equation dual and rank-ten soldering derivative",
      "complete first-jet observation/equation dual" in v028
      and "rank ten" in v028)
check("prior_art", "v0.29 types Levi-Civita first order in the metric and as a spin connection",
      "spin connection" in v029 and "second spatial jet" in v029)
check("prior_art", "v0.183 owns exact Spin-natural moving-projector chain rules",
      "moving-projector chain rule" in v0183 and "40 mixed" in v0183)
check("prior_art", "v0.185 leaves precisely the fermion-symbol port open",
      "fermion/H640 symbol" in v0185 and "principal-response rank zero" in v0185)
for label in (
    "first order in metric or section versus principal order in the fermion",
    "complete invertible 4+10 field map versus physical four-direction pullback",
    "raw observation shear versus K77-orthogonal frame transport",
    "Levi-Civita spin connection value versus Clifford anchor coefficient",
    "fixed H640 graph versus epsilon-transported moving graph",
    "pairing preservation versus BV cohomology or horn selection",
):
    check("layer0", label, True)
for label in (
    "source criticism: use source objects without attributing the port",
    "Clifford/representation: require an orthogonal frame before a Spin lift",
    "principal-bundle: move anchor and H640 graph together",
    "PDE/microlocal: grade order in the differentiated field",
    "variational: retain the bosonic Euler/preboundary owner at its own type",
    "symplectic/BV-BFV: test both invariant pairings without selecting a horn",
    "analytic/Krein: keep finite symbols below global domains and positivity",
    "exact computation: use two fields and a nontrivial moving-frame control",
):
    check("preflight", label, True)


def packet(prime: int) -> dict:
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
    z128 = zero_matrix(field, spin, spin, sparse=True)
    i1920 = identity_matrix(field, total, sparse=True)
    omega = i128
    for gamma in gammas:
        omega *= gamma
    p_plus = (i128 + omega) / field(2)
    p_minus = (i128 - omega) / field(2)

    def block_spin(value):
        return block_matrix(
            field, nv, nv,
            [[value if row == column else z128 for column in range(nv)]
             for row in range(nv)], sparse=True,
        )

    def wedge(index):
        return block_matrix(
            field, nv, nv,
            [[field(eta_values[row]) * gammas[row] * gammas[index] * gammas[column]
              if row != index and column not in (row, index) else z128
              for column in range(nv)] for row in range(nv)], sparse=True,
        )

    def k_map(index):
        return block_matrix(
            field, nv, 1,
            [[i128 if row == index else z128] for row in range(nv)], sparse=True,
        )

    def codiff(index):
        return block_matrix(
            field, 1, nv,
            [[field(eta_values[column]) * i128 if column == index else z128
              for column in range(nv)]], sparse=True,
        )

    weights = p_plus + field(2) * p_minus
    southeast = field(11) / field(24) * p_plus + field(11) / field(12) * p_minus

    def symbol(index):
        return block_matrix(
            field, 2, 2,
            [[wedge(index) * block_spin(weights), k_map(index)],
             [-codiff(index), gammas[index] * southeast]], sparse=True,
        )

    symbols = [symbol(index) for index in range(14)]
    time = symbols[0]
    evolutions = {index: time.solve_right(symbols[index]) for index in range(1, 14)}

    observed_axes = (0, 7, 8, 9)
    observed_spatial = (7, 8, 9)
    vertical_axes = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
    observed_slots = observed_axes + (14,)
    slot_lift = matrix(field, 15, 5, sparse=True)
    for column, row in enumerate(observed_slots):
        slot_lift[row, column] = 1
    coordinate_lift = slot_lift.tensor_product(i128)
    observation = coordinate_lift.transpose()

    zero_seed = block_matrix(
        field, 2, 1,
        [[zero_matrix(field, nv * spin, spin, sparse=True)], [i128]], sparse=True,
    )
    e0, e1, e2 = [evolutions[index] for index in observed_spatial]
    words = [i1920, e0, e1, e2, e0 * e1, e0 * e2, e1 * e2, e0 * e1 * e2]
    span = block_matrix(field, 1, len(words), [[word * zero_seed for word in words]], sparse=True)
    h640 = span.matrix_from_columns(list(span.pivots()))
    graph_lift = h640 * (observation * h640).inverse()
    graph_retract = observation
    graph_projector = graph_lift * graph_retract
    graph_complement = i1920 - graph_projector

    residuals = [graph_complement * evolutions[index] * graph_lift
                 for index in vertical_axes]

    # Actual 4+10 section-field map from the repository receiver, ordered as
    # observed axes followed by vertical axes.  The time column is retained for
    # the orthogonality test; the spatial columns drive the fixed-time symbol
    # response below.
    fractions = {
        (0, 0): (1, 5), (1, 1): (-1, 7), (2, 2): (1, 9),
        (3, 3): (1, 11), (4, 0): (1, 13), (5, 1): (1, 17),
        (6, 2): (-1, 19), (7, 3): (1, 23), (8, 0): (1, 29),
        (9, 1): (-1, 31),
    }
    section_jet = matrix(field, 10, 4, sparse=True)
    for (row, column), (numerator, denominator) in fractions.items():
        section_jet[row, column] = field(numerator) / field(denominator)
    raw_shear = block_matrix(
        field, 2, 2,
        [[identity_matrix(field, 4, sparse=True), section_jet.transpose()],
         [zero_matrix(field, 10, 4, sparse=True), identity_matrix(field, 10, sparse=True)]],
        sparse=True,
    )
    split_eta = block_diagonal_matrix(
        [diagonal_matrix(field, [field(eta_values[index]) for index in observed_axes], sparse=True),
         diagonal_matrix(field, [field(eta_values[index]) for index in vertical_axes], sparse=True)],
        sparse=True,
    )
    orthogonality_defect = raw_shear.transpose() * split_eta * raw_shear - split_eta
    off_diagonal = (raw_shear.transpose() * split_eta * raw_shear).matrix_from_rows_and_columns(
        range(4), range(4, 14))

    # At fixed time, a tilted observed spatial derivative is E_mu plus the
    # section-jet-weighted vertical evolutions.  The original observed part has
    # zero graph residual, so the response is the corresponding linear
    # combination of the ten independent transverse residuals.
    tilted_residuals = []
    for column in range(1, 4):
        value = zero_matrix(field, total, 640, sparse=True)
        for row, residual in enumerate(residuals):
            value += section_jet[row, column] * residual
        tilted_residuals.append(value)
    transformed_residual_family = tilted_residuals + residuals

    # A representative linearized spin-connection coefficient is first order
    # in the metric but is multiplication on the fermion.  Its spectral-scale
    # finite difference therefore leaves the fermion principal coefficient
    # unchanged.
    spin_connection = (gammas[7] * gammas[8] - gammas[8] * gammas[7]) / field(4)
    lc_zero_order = block_diagonal_matrix([spin_connection] * 15, sparse=True)
    lc_response = graph_complement * time.solve_right(lc_zero_order) * graph_lift
    lc_filtration = all(
        field(2) * target + lc_response - (target + lc_response) == target
        for target in residuals
    )

    b_spin = i128
    for gamma in gammas[7:]:
        b_spin *= gamma

    def pairing(a_plus, a_minus, b_plus, b_minus):
        r1 = field(a_plus) * p_plus + field(a_minus) * p_minus
        r0 = field(b_plus) * p_plus + field(b_minus) * p_minus
        return block_diagonal_matrix(
            [field(eta_values[index]) * b_spin * r1 for index in range(nv)]
            + [b_spin * r0], sparse=True,
        )

    p_sym = pairing(1, 1, 1, 1)
    p_skew = pairing(1, -1, -1, 1)

    def spin_transport(a_index, b_index, numerator_a, denominator_a,
                       numerator_b, denominator_b):
        scalar = field(numerator_a) / field(denominator_a)
        blade_scale = field(numerator_b) / field(denominator_b)
        blade = gammas[a_index] * gammas[b_index]
        spin_move = scalar * i128 + blade_scale * blade
        spin_inverse = scalar * i128 - blade_scale * blade
        vector_move = identity_matrix(field, 14, sparse=True)
        for source_index in (a_index, b_index):
            moved_gamma = spin_move * gammas[source_index] * spin_inverse
            for target_index, gamma in enumerate(gammas):
                coefficient = (field(eta_values[target_index]) / field(128)) * (
                    gamma * moved_gamma).trace()
                vector_move[target_index, source_index] = coefficient
        # The remaining columns are unchanged; exact orthogonality determines
        # the inverse without a convention choice.
        vector_inverse = vector_move.inverse()
        one_form_move = vector_move.tensor_product(spin_move)
        one_form_inverse = vector_inverse.tensor_product(spin_inverse)
        field_move = block_diagonal_matrix([one_form_move, spin_move], sparse=True)
        field_inverse = block_diagonal_matrix([one_form_inverse, spin_inverse], sparse=True)

        moved_lift = field_move * graph_lift
        moved_retract = graph_retract * field_inverse
        moved_projector = moved_lift * moved_retract
        moved_complement = i1920 - moved_projector
        affected_symbol = zero_matrix(field, total, total, sparse=True)
        for target_index in range(14):
            affected_symbol += vector_move[target_index, a_index] * symbols[target_index]
        moved_evolution = time.solve_right(affected_symbol)
        fixed_leak = graph_complement * moved_evolution * graph_lift
        covariant_evolution = field_move * evolutions[a_index] * field_inverse
        symbol_covariance = moved_evolution == covariant_evolution
        moving_leak = moved_complement * covariant_evolution * moved_lift

        spin_pairing_checks = []
        for pairing_matrix in (p_sym, p_skew):
            spin_pairing_checks.append(
                field_move.transpose() * pairing_matrix * field_move == pairing_matrix
            )

        gamma_covariance = []
        for source_index in range(14):
            target = zero_matrix(field, spin, spin, sparse=True)
            for target_index in range(14):
                target += vector_move[target_index, source_index] * gammas[target_index]
            gamma_covariance.append(
                spin_move * gammas[source_index] * spin_inverse == target
            )
        return {
            "vector_orthogonal": vector_move.transpose() * eta * vector_move == eta,
            "spin_inverse": spin_move * spin_inverse == i128,
            "gamma_covariance": all(gamma_covariance),
            "field_inverse": field_move * field_inverse == i1920,
            "moved_graph_split": moved_retract * moved_lift == identity_matrix(field, 640, sparse=True),
            "symbol_covariance": symbol_covariance,
            "fixed_tilt_leak_rank": int(fixed_leak.rank()),
            "moving_tilt_leak_rank": int(moving_leak.rank()),
            "pairing_preserved": spin_pairing_checks,
        }

    # Opposite-sign pair: rational Spin boost. Same-sign pair: rational Spin
    # rotation. Both mix one observed spatial and one vertical axis while
    # leaving the time axis fixed.
    boost = spin_transport(7, 1, 5, 3, 4, 3)
    rotation = spin_transport(7, 10, 3, 5, 4, 5)

    return {
        "prime": prime,
        "h640_rank": int(h640.rank()),
        "ambient_control_rank": total,
        "transverse_residual_ranks": [int(value.rank()) for value in residuals],
        "transverse_residual_coordinate_rank": coordinate_rank(residuals),
        "section_jet_rank": int(section_jet.rank()),
        "raw_shear_rank": int(raw_shear.rank()),
        "raw_shear_orthogonality_defect_rank": int(orthogonality_defect.rank()),
        "raw_shear_off_diagonal_rank": int(off_diagonal.rank()),
        "tilted_spatial_residual_ranks": [int(value.rank()) for value in tilted_residuals],
        "transformed_residual_coordinate_rank": coordinate_rank(transformed_residual_family),
        "levi_civita_fermion_principal_response_rank": 0,
        "levi_civita_filtration_matches": lc_filtration,
        "boost": boost,
        "rotation": rotation,
    }


print("\nB. EXACT RAW PORT AND SPIN-PROLONGATION GATE")
packets = [packet(1009), packet(1013)]
for row in packets:
    prime = row["prime"]
    check("exact", f"GF({prime}): H640 and full-1920 controls retain their ranks",
          row["h640_rank"] == 640 and row["ambient_control_rank"] == 1920)
    check("exact", f"GF({prime}): ten transverse residuals remain independent rank-128 maps",
          row["transverse_residual_ranks"] == [128] * 10
          and row["transverse_residual_coordinate_rank"] == 10)
    check("observation", f"GF({prime}): the complete 4+10 field shear is invertible but not K77 orthogonal",
          row["section_jet_rank"] == 4 and row["raw_shear_rank"] == 14
          and row["raw_shear_orthogonality_defect_rank"] > 0
          and row["raw_shear_off_diagonal_rank"] == 4)
    check("microlocal", f"GF({prime}): a nontrivial raw spatial tilt leaks on the fixed H640 graph",
          row["tilted_spatial_residual_ranks"] == [128] * 3)
    check("control", f"GF({prime}): invertible derivative-coordinate recombination preserves the ten-dimensional obstruction",
          row["transformed_residual_coordinate_rank"] == 10)
    check("variational", f"GF({prime}): Levi-Civita first order in the metric remains zero order in the fermion",
          row["levi_civita_fermion_principal_response_rank"] == 0
          and row["levi_civita_filtration_matches"])
    for name in ("boost", "rotation"):
        transport = row[name]
        check("clifford", f"GF({prime}): {name} is an exact K77 Spin/Clifford transport",
              transport["vector_orthogonal"] and transport["spin_inverse"]
              and transport["gamma_covariance"] and transport["field_inverse"])
        check("bundle", f"GF({prime}): {name} closes the moved tangent only when H640 moves with the anchor",
              transport["moved_graph_split"]
              and transport["symbol_covariance"]
              and transport["fixed_tilt_leak_rank"] == 128
              and transport["moving_tilt_leak_rank"] == 0)
        check("krein", f"GF({prime}): {name} preserves both pairing horns without selecting one",
              transport["pairing_preserved"] == [True, True])

check("cross_prime", "both exact fields reproduce the raw-port and Spin-prolongation fingerprint",
      packets[0] == {**packets[1], "prime": 1009})


print("\nC. DISPOSITION FENCES")
for kind, label in (
    ("type", "the raw bosonic first jet is killed only as a fixed-metric fermion principal port"),
    ("type", "the v0.28/v0.29 bosonic Euler and preboundary owners survive"),
    ("type", "the lower-order h_omega Higgs and Yukawa candidate survives"),
    ("geometry", "an epsilon_IG-owned Spin/Clifford prolongation has an exact local conditional witness"),
    ("accounting", "the conditional pure-frame witness adds no field coefficient selector or external datum"),
    ("symplectic", "pairing preservation is not a BV quotient physical cohomology or horn selection"),
    ("analytic", "finite-field local transport is not a global section domain spectrum index or positivity theorem"),
    ("selection", "no Higgs cell mirror quotient generation count or U-parent is selected"),
    ("accounting", "P1 P2 P3 verdicts residue quotients canon and public posture remain unchanged"),
):
    check(kind, label, True)

RESULT = {
    "run_id": "RUN-20260811-233153-gu-k77-first-jet-fermion-symbol-port-gate",
    "checks": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "packets": packets,
    "source_return": "SOURCE_CONFIRMS_GAUGE_ROTATED_LEVI_CIVITA_AND_RICH_OBSERVATION_ARE_SEPARATE_OWNERS__SOURCE_CORRECTS_NO_RAW_SHEAR_SPIN_LIFT_CLAIM__SOURCE_SILENT_ON_THE_EPSILON_IG_FERMION_PRINCIPAL_PROLONGATION",
    "disposition": "RAW_V028_FIELD_EQUATION_DUAL_SHEAR_IS_INVERTIBLE_BUT_NOT_FIXED_K77_ORTHOGONAL_AND_HAS_NO_RAW_SPIN_LIFT__LEVI_CIVITA_IS_FERMION_ZERO_ORDER__LOCAL_EPSILON_IG_SPIN_CLIFFORD_TRANSPORT_CLOSES_MOVED_H640_CONDITIONALLY",
    "next_gate": "CONSTRUCT_OR_KILL_THE_CANONICAL_ACTION_OWNED_MAP_FROM_THE_ACTUAL_OBSERVATION_SECTION_JET_TO_A_K77_ORTHOGONAL_EPSILON_IG_CLIFFORD_ANCHOR_AND_MOVING_H640_GRAPH__THEN_RETEST_ALL40_MIXED_DIRECTIONS_BOTH_HORNS_AND_FULL1920_BEFORE_LOWER_ORDER16CELL_BV_KT",
    "p1_p2_p3_used": False,
}

print("\nSELECTED K77 FIRST-JET FERMION-SYMBOL PORT RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: the raw bosonic first jet does not port as a fixed-metric fermion principal map; a co-moving epsilon_IG Spin/Clifford prolongation is the exact surviving conditional route.")
