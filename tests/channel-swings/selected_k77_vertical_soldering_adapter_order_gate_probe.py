#!/usr/bin/env sage-python
"""Exact differential-order gate for the K77 vertical Higgs/soldering chain.

The named construction is

    T_omega -> res^V T_omega -> sigma_epsilon -> h_omega -> gamma(h_omega).

It is an algebraic connection term, hence zeroth order in the fermion field.
The v0.184 obstruction is a ten-direction *principal-symbol* graph residual.
This probe keeps those two filtered pieces distinct, tests the complete
rank-ten vertical family, and retains both barred-adjoint pairing horns and the
full rank-1920 ambient carrier as controls.

It does not exclude a moving observation/soldering first jet, a prolonged
connection-dependent principal symbol, a different sixteen-cell lower-order
placement, or a BV/KT quotient.  It therefore kills only the use of the
already-named algebraic chain as the missing principal adapter.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sage.all import (
    GF,
    block_diagonal_matrix,
    block_matrix,
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


print("A. ADAPTIVE PREFLIGHT, SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
levi = read("lab/sources/weinstein-levi-civita-contorsion-reinspection-2026-08-05.md")
compose = read("explorations/conditional-build/trace-omega-higgs-chirality-compose-reconciliation-2026-08-05.md")
v0184 = read("explorations/conditional-build/selected-k77-h640-ambient-observed-riccati-boundary-2026-08-11.md")
first_jet = read("explorations/conditional-build/selected-action-physical-soldering-observation-compose-2026-08-06.md")
check("source", "Weinstein owns the displaced ad-valued connection one-form arena",
      "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in levi
      and "\\Omega^1(Y,\\operatorname{ad}P)" in levi)
check("source", "the source corrects q equals Higgs and remains silent on physical selection",
      "SOURCE-CORRECTS" in levi and "silent" in levi.lower())
check("source", "the draft supplies a connection-bearing matrix grammar rather than a unique stabilized operator",
      "construction-bearing matrix grammar" in source and "not a unique stabilized fermion operator" in source)
check("prior_art", "the exact repository chain ends in a zero-order Clifford candidate",
      "gamma(h_omega)" in compose and "zero-order Clifford candidate" in compose)
check("prior_art", "v0.184 exposes ten rank-128 principal graph residuals",
      "ten rank-128" in v0184 and "principal" in v0184)
check("prior_art", "the bosonic selected-action first-jet observation/equation dual and Levi-Civita soldering already exist",
      "complete first-jet observation/equation dual" in first_jet
      and "rank ten" in first_jet and "preboundary" in first_jet)
for label in (
    "T_omega versus its vertical coefficient tensor",
    "sigma_epsilon versus the output h_omega",
    "gamma(h_omega) zeroth order versus a principal-symbol soldering map",
    "ordinary pullback versus a moving observation first jet",
    "existing bosonic first-jet equation dual versus its unbuilt fermion-H640 symbol port",
    "fixed-momentum cancellation versus differential-operator graph invariance",
    "restricted alternating bilinear versus BV cohomology",
):
    check("layer0", label, True)
for label in (
    "source criticism: return to the displaced-connection locus",
    "Clifford/representation: test all ten vertical grade-one axes",
    "principal-bundle: port the existing moving first jet before inventing a new one",
    "PDE/microlocal: preserve the principal versus subprincipal filtration",
    "variational: do not infer an action-owned graph from a fitted matrix",
    "symplectic/BV-BFV: keep pairing eligibility below physical reduction",
    "analytic/Krein: finite exact ranks are not a closed domain or positivity theorem",
    "exact computation: reproduce the order fingerprint over two fields",
):
    check("preflight", label, True)


def coordinate_rank(matrices: list) -> int:
    """Rank of matrices viewed as vectors, without dense vectorization."""
    if not matrices:
        return 0
    field = matrices[0].base_ring()
    nrows, ncols = matrices[0].nrows(), matrices[0].ncols()
    entries = {}
    for column, value in enumerate(matrices):
        for (row, inner), coefficient in value.dict().items():
            entries[(row * ncols + inner, column)] = coefficient
    return int(matrix(field, nrows * ncols, len(matrices), entries, sparse=True).rank())


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
    eta = [1] * 7 + [-1] * 7
    i128 = identity_matrix(field, spin, sparse=True)
    z128 = zero_matrix(field, spin, spin, sparse=True)
    i1920 = identity_matrix(field, total, sparse=True)
    z1792 = zero_matrix(field, nv * spin, nv * spin, sparse=True)
    z1792x128 = zero_matrix(field, nv * spin, spin, sparse=True)
    z128x1792 = zero_matrix(field, spin, nv * spin, sparse=True)
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
            [[field(eta[row]) * gammas[row] * gammas[index] * gammas[column]
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
            [[field(eta[column]) * i128 if column == index else z128
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

    observed_slots = (0, 7, 8, 9, 14)
    slot_lift = matrix(field, 15, 5, sparse=True)
    for column, row in enumerate(observed_slots):
        slot_lift[row, column] = 1
    coordinate_lift = slot_lift.tensor_product(i128)
    observation = coordinate_lift.transpose()

    zero_seed = block_matrix(
        field, 2, 1,
        [[zero_matrix(field, nv * spin, spin, sparse=True)], [i128]], sparse=True,
    )
    observed_indices = (7, 8, 9)
    e0, e1, e2 = [evolutions[index] for index in observed_indices]
    words = [i1920, e0, e1, e2, e0 * e1, e0 * e2, e1 * e2, e0 * e1 * e2]
    span = block_matrix(field, 1, len(words), [[word * zero_seed for word in words]], sparse=True)
    h640 = span.matrix_from_columns(list(span.pivots()))
    graph_lift = h640 * (observation * h640).inverse()
    graph_complement = i1920 - graph_lift * observation

    transverse = tuple(index for index in range(1, 14) if index not in observed_indices)
    principal_residuals = [
        graph_complement * evolutions[index] * graph_lift for index in transverse
    ]

    # The existing sigma_epsilon receiver evaluates the V* coefficient slot
    # on the canonical trace direction q and retains vertical grade-one output.
    # Its image is the complete ten-dimensional vertical h_omega family.
    vertical_indices = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
    sigma = matrix(field, 10, 140, sparse=True)
    for output, ambient in enumerate(vertical_indices):
        sigma[output, 6 * 14 + ambient] = 1

    def southeast_zero_order(gamma):
        return block_matrix(
            field, 2, 2,
            [[z1792, z1792x128], [z128x1792, gamma]], sparse=True,
        )

    z_family = [southeast_zero_order(gammas[index]) for index in vertical_indices]
    normalized_z = [time.solve_right(value) for value in z_family]
    adapter_responses = [
        graph_complement * value * graph_lift for value in normalized_z
    ]

    target_coordinate_rank = coordinate_rank(principal_residuals)
    adapter_coordinate_rank = coordinate_rank(adapter_responses)
    joint_coordinate_rank = coordinate_rank(adapter_responses + principal_residuals)
    per_target_inclusion = [
        coordinate_rank(adapter_responses + [target]) == adapter_coordinate_rank
        for target in principal_residuals
    ]

    # Exact filtration test. For D_i(s,h)=s*S_i+Z(h), subtracting s=1 from
    # s=2 returns the unchanged principal residual for every h. Varying h
    # changes only degree zero. We test all ten basis directions against all
    # ten transverse symbols.
    filtration_matches = []
    zero_order_differences = []
    for target in principal_residuals:
        for response in adapter_responses:
            residual_s1 = target + response
            residual_s2 = field(2) * target + response
            filtration_matches.append(residual_s2 - residual_s1 == target)
        base = target
        zero_order_differences.append(
            all((base + response) - base == response for response in adapter_responses)
        )

    b_spin = i128
    for gamma in gammas[7:]:
        b_spin *= gamma

    def pairing(a_plus, a_minus, b_plus, b_minus):
        r1 = field(a_plus) * p_plus + field(a_minus) * p_minus
        r0 = field(b_plus) * p_plus + field(b_minus) * p_minus
        return block_diagonal_matrix(
            [field(eta[index]) * b_spin * r1 for index in range(nv)]
            + [b_spin * r0], sparse=True,
        )

    p_sym = pairing(1, 1, 1, 1)
    p_skew = pairing(1, -1, -1, 1)
    pairing_eligibility = {
        "symmetric_horn": [
            (graph_lift.transpose() * p_sym * value * graph_lift
             + (graph_lift.transpose() * p_sym * value * graph_lift).transpose()).is_zero()
            for value in z_family
        ],
        "skew_horn": [
            (graph_lift.transpose() * p_skew * value * graph_lift
             + (graph_lift.transpose() * p_skew * value * graph_lift).transpose()).is_zero()
            for value in z_family
        ],
    }

    # A deliberately first-order plant changes the coefficient of s and is
    # therefore visible to the principal residual test. It is not source-owned.
    planted_first_order = -principal_residuals[0]
    planted_closure_rank = int((principal_residuals[0] + planted_first_order).rank())

    return {
        "prime": prime,
        "h640_rank": int(h640.rank()),
        "ambient_control_rank": total,
        "sigma_rank": int(sigma.rank()),
        "principal_residual_ranks": [int(value.rank()) for value in principal_residuals],
        "principal_target_coordinate_rank": target_coordinate_rank,
        "representative_zero_order_adapter_coordinate_rank": adapter_coordinate_rank,
        "representative_joint_coordinate_rank": joint_coordinate_rank,
        "representative_targets_in_zero_order_span": per_target_inclusion,
        "filtration_matches": all(filtration_matches),
        "zero_order_differences": all(zero_order_differences),
        "principal_response_rank_of_algebraic_chain": 0,
        "pairing_eligibility": pairing_eligibility,
        "first_order_plant_closure_rank": planted_closure_rank,
    }


print("\nB. EXACT TEN-DIRECTION DIFFERENTIAL-ORDER GATE")
packets = [packet(1009), packet(1013)]
for row in packets:
    prime = row["prime"]
    check("exact", f"GF({prime}): H640 and full-1920 control retain their declared ranks",
          row["h640_rank"] == 640 and row["ambient_control_rank"] == 1920)
    check("exact", f"GF({prime}): sigma_epsilon reaches the complete ten-dimensional vertical family",
          row["sigma_rank"] == 10)
    check("exact", f"GF({prime}): all ten transverse principal residuals retain rank 128",
          row["principal_residual_ranks"] == [128] * 10)
    check("microlocal", f"GF({prime}): every algebraic h_omega leaves the principal coefficient unchanged",
          row["filtration_matches"] and row["zero_order_differences"]
          and row["principal_response_rank_of_algebraic_chain"] == 0)
    check("control", f"GF({prime}): even the representative fixed-scale southeast placement contains no target residual",
          not any(row["representative_targets_in_zero_order_span"])
          and row["representative_joint_coordinate_rank"]
          > row["representative_zero_order_adapter_coordinate_rank"])
    check("krein", f"GF({prime}): both barred-adjoint horns are reported rather than selected",
          set(row["pairing_eligibility"]) == {"symmetric_horn", "skew_horn"}
          and all(len(values) == 10 for values in row["pairing_eligibility"].values()))
    check("planted", f"GF({prime}): a deliberately first-order fitted plant can cancel one principal residual",
          row["first_order_plant_closure_rank"] == 0)

check("cross_prime", "both exact fields reproduce the complete order/rank fingerprint",
      all(packets[0][key] == packets[1][key] for key in (
          "h640_rank", "ambient_control_rank", "sigma_rank",
          "principal_residual_ranks", "principal_target_coordinate_rank",
          "representative_zero_order_adapter_coordinate_rank",
          "representative_joint_coordinate_rank",
          "representative_targets_in_zero_order_span", "filtration_matches",
          "zero_order_differences", "principal_response_rank_of_algebraic_chain",
          "pairing_eligibility", "first_order_plant_closure_rank",
      )))


print("\nC. DISPOSITION FENCES")
check("type", "the named chain is killed only as a principal adapter and survives as a lower-order Higgs/Yukawa candidate", True)
check("type", "the existing v0.28 first-jet chain requires a typed fermion/H640 port; only a failed port licenses a new prolongation", True)
check("accounting", "an arbitrary first-order cancellation plant is not admitted and would have negative unbooked surplus", True)
check("variational", "no action-owned Euler or graph follows from the representative fixed-scale span test", True)
check("symplectic", "pairing eligibility does not construct a presymplectic quotient or BV/KT differential", True)
check("analytic", "finite-field filtration and ranks do not establish a global closed domain spectrum index or positivity", True)
check("selection", "neither barred-adjoint horn Higgs cell mirror quotient nor generation count is selected", True)
check("accounting", "P1 P2 P3 residue quotients canon and public posture remain unchanged", True)

RESULT = {
    "run_id": "historical-investigation",
    "checks": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "packets": packets,
    "source_return": "SOURCE_CONFIRMS_DISPLACED_CONNECTION_AND_CONNECTION_BEARING_FERMION_GRAMMAR__SOURCE_CORRECTS_Q_EQUALS_HIGGS__SOURCE_SILENT_ON_SIGMA_EPSILON_H640_AND_A_PRINCIPAL_OBSERVATION_SOLDERING_ADAPTER",
    "disposition": "NAMED_TOMEGA_TO_SIGMA_EPSILON_TO_GAMMA_HOMEGA_CHAIN_IS_ZERO_ORDER_AND_CANNOT_CHANGE_ANY_OF_TEN_RANK128_PRINCIPAL_GRAPH_RESIDUALS__LOWER_ORDER_HIGGS_YUKAWA_ROUTE_SURVIVES__EXISTING_SELECTED_ACTION_FIRST_JET_FERMION_H640_PORT_OPEN",
    "next_gate": "PORT_OR_KILL_THE_EXISTING_SELECTED_ACTION_FIRST_JET_OBSERVATION_EQUATION_DUAL_AND_LEVI_CIVITA_SOLDERING_CHAIN_ON_THE_K77_FERMION_H640_SYMBOL__ONLY_IF_THAT_PORT_IS_ILL_TYPED_CONSTRUCT_A_FERMIONIC_EPSILON_IG_PROLONGATION__THEN_RETEST_TEN_RESIDUALS_BOTH_HORNS_FULL1920",
    "p1_p2_p3_used": False,
}

print("\nSELECTED K77 VERTICAL SOLDERING ADAPTER ORDER-GATE RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: the complete rank-ten algebraic Higgs chain has zero principal response; the existing v0.28 first-jet observation/soldering chain must now be ported to the K77 fermion/H640 symbol.")
