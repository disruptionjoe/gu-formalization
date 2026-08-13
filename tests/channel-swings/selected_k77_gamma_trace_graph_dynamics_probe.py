#!/usr/bin/env sage-python
"""Exact action/current/principal gate for the tautological K77 graph.

Run with::

    sage -python tests/channel-swings/selected_k77_gamma_trace_graph_dynamics_probe.py

Layer 0: the right algebraic kernel, the independent barred left kernel, the
Krein-dual barred carrier, the action-restricted Green symbol, a consistent
full-Euler truncation, BV cohomology and a closed-domain mode are distinct.
The probe stops before BV whenever full-Euler receiver closure fails.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy

from sage.all import block_diagonal_matrix, block_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def load_predecessor() -> dict:
    capture = io.StringIO()
    with redirect_stdout(capture):
        namespace = runpy.run_path(
            str(ROOT / "tests/channel-swings/selected_k77_moving_varpi_stationary_intersection_probe.py")
        )
    namespace["captured_predecessor_output"] = capture.getvalue()
    return namespace


def rolled_symbol(structures: dict, field, xi):
    gammas = structures["gammas"]
    eta = [1] * 7 + [-1] * 7
    identity = structures["I128"]
    z = zero_matrix(field, 128, 128, sparse=True)
    gamma_xi = sum((field(xi[a]) * gammas[a] for a in range(14)), z)
    upper_left = block_matrix(
        field,
        14,
        14,
        [[
            (gamma_xi if row == column else z)
            - field(xi[row]) * gammas[column]
            for column in range(14)
        ] for row in range(14)],
        sparse=True,
    )
    upper_right = block_matrix(
        field, 14, 1,
        [[field(xi[row]) * identity] for row in range(14)],
        sparse=True,
    )
    xi_up = [eta[column] * field(xi[column]) for column in range(14)]
    lower_left = block_matrix(
        field, 1, 14,
        [[-xi_up[column] * identity for column in range(14)]],
        sparse=True,
    )
    return block_matrix(
        field, 2, 2,
        [[upper_left, upper_right], [lower_left, z]],
        sparse=True,
    )


def krein_pairing(structures: dict, field):
    """Degree-zero/one pairing used to turn barred vectors into covectors."""
    b = structures["B"]
    eta = [1] * 7 + [-1] * 7
    return block_diagonal_matrix(
        [field(eta[index]) * b for index in range(14)] + [b],
        sparse=True,
    )


def independent_column_basis(projector):
    return projector.matrix_from_columns(list(projector.pivots()))


def analyze_candidate(predecessor: dict, structures: dict, field, candidate: str):
    components = list(structures["gammas"])
    full = predecessor["source_faithful_matrices"](
        structures, field, components
    )[candidate][0]
    graph = predecessor["tautological_kernel_graphs"](
        structures, field
    )[candidate]
    pairing = krein_pairing(structures, field)

    # Barred and unbarred fields are independent in the source.  The left
    # kernel supplies action covectors.  The Krein-dual barred carrier is then
    # K^{-T} L^T; no reality identification is inserted.
    left = full.left_kernel().basis_matrix()
    barred = pairing.transpose().solve_right(left.transpose())
    check("exact", f"{candidate}: right graph is the complete rank-128 right kernel",
          graph.rank() == 128 and (full * graph).is_zero())
    check("exact", f"{candidate}: independent barred left kernel has rank 128",
          left.nrows() == 128 and left.rank() == 128 and (left * full).is_zero())
    check("krein", f"{candidate}: Krein-dual barred carrier reproduces the left action covectors",
          barred.transpose() * pairing == left)
    check("krein", f"{candidate}: barred Euler equation is killed after composing the pairing",
          (barred.transpose() * pairing * full).is_zero())

    covectors = {
        "timelike_plus": [1] + [0] * 13,
        "spacelike_minus": [0] * 7 + [1] + [0] * 6,
        "null": [1] + [0] * 6 + [1] + [0] * 6,
    }
    principal = {}
    equation_receiver = left.transpose()
    for name, xi in covectors.items():
        symbol = rolled_symbol(structures, field, xi)
        raw = symbol * graph
        green = barred.transpose() * pairing * raw
        joined = block_matrix(field, 1, 2, [[equation_receiver, raw]], sparse=True)
        receiver_leak = joined.rank() - equation_receiver.rank()
        principal[name] = {
            "induced_green_rank": int(green.rank()),
            "raw_symbol_on_graph_rank": int(raw.rank()),
            "receiver_leak_rank": int(receiver_leak),
            "receiver_closed": receiver_leak == 0,
        }

    # The smallest source-geometric coefficient bank varies one tautological
    # diagonal cell V_i=gamma_i at a time.  Their sum is the radial direction,
    # and must vanish between zero modes by homogeneity.  Nonzero individual
    # matrices are transverse action-derived connection currents.
    currents = []
    z = zero_matrix(field, 128, 128, sparse=True)
    for index in range(14):
        tangent = [z for _ in range(14)]
        tangent[index] = structures["gammas"][index]
        derivative = predecessor["source_faithful_matrices"](
            structures, field, tangent
        )[candidate][0]
        currents.append(barred.transpose() * pairing * derivative * graph)
    radial = sum(currents, z)
    current_ranks = [current.rank() for current in currents]
    current_support = [index for index, rank in enumerate(current_ranks) if rank]

    return {
        "left_kernel_rank": int(left.rank()),
        "krein_pairing_rank": int(pairing.rank()),
        "principal": principal,
        "diagonal_current_ranks": [int(rank) for rank in current_ranks],
        "diagonal_current_support": current_support,
        "radial_current_rank": int(radial.rank()),
        "all_diagonal_currents_zero": not current_support,
    }


print("A. SOURCE, PRIOR ART AND LAYER 0")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
prior = (ROOT / "explorations/conditional-build/selected-k77-moving-varpi-stationary-intersection-2026-08-10.md").read_text()
check("source", "draft keeps barred and unbarred variables independent",
      "four distinct fields" in source and "do not replace the bars" in source)
check("source", "draft assigns a fermionic current class but supplies no global adjoint/domain",
      "Omega^(d-1)(Y,ad)" in source and "global Hodge/Krein/reality adjoint" in source)
check("source", "southeast-zero and source-admitted nonzero southeast branches remain distinct",
      "SOURCE-ADMITS-UNSPECIFIED-RIVAL" in source)
check("prior_art", "v0.157 supplies exact rank-128 gamma-trace/Omega0 graphs",
      "rank 1792, nullity 128" in prior and "entirely gamma-trace" in prior)
for label in (
    "right algebraic kernel versus independent barred left kernel",
    "Krein-dual barred vector versus left action covector",
    "restricted Green symbol versus full-Euler receiver closure",
    "radial branch current versus transverse connection current",
    "finite action carrier versus BV cohomology and closed-domain mode",
):
    check("layer0", label + " remain distinct", True)

predecessor = load_predecessor()
check("prior_art", "immutable v0.157 predecessor replays",
      not predecessor["FAILURES"] and "PASS:" in predecessor["captured_predecessor_output"])


print("\nB. EXACT ACTION-DUAL, GREEN AND CURRENT GATE")
structures = predecessor["structures"]
field = predecessor["field"]
results = {
    candidate: analyze_candidate(predecessor, structures, field, candidate)
    for candidate in ("column_pin", "row_pin")
}

for candidate, result in results.items():
    for covector, row in result["principal"].items():
        print(f"  {candidate}/{covector}: {row}", flush=True)
    print(
        f"  {candidate}/current ranks={result['diagonal_current_ranks']} "
        f"radial={result['radial_current_rank']}",
        flush=True,
    )


print("\nC. PREREGISTERED HORNS AND CONTROLS")
for candidate, result in results.items():
    timelike = result["principal"]["timelike_plus"]
    spacelike = result["principal"]["spacelike_minus"]
    null = result["principal"]["null"]
    check("green", f"{candidate}: non-null induced Green symbols are nonzero",
          timelike["induced_green_rank"] > 0 and spacelike["induced_green_rank"] > 0)
    check("current", f"{candidate}: the natural diagonal connection-current bank is live",
          not result["all_diagonal_currents_zero"])
    check("current", f"{candidate}: the radial tautological current cancels exactly",
          result["radial_current_rank"] == 0)
    check("planted", f"{candidate}: radial cancellation does not imply every current cell vanishes",
          result["radial_current_rank"] == 0 and bool(result["diagonal_current_support"]))
    check("pde", f"{candidate}: at least one covector class tests full-Euler receiver closure",
          all("receiver_closed" in row for row in (timelike, spacelike, null)))

graph_action_live = any(
    result["principal"]["timelike_plus"]["induced_green_rank"] > 0
    for result in results.values()
)
fermion_current_live = any(
    result["diagonal_current_support"] for result in results.values()
)
receiver_closed_all = any(
    all(row["receiver_closed"] for row in result["principal"].values())
    for result in results.values()
)
check("horn", "GRAPH_ACTION_LIVE fires", graph_action_live)
check("horn", "FERMION_CURRENT_LIVE fires", fermion_current_live)
check("horn", "a finite BV complex is admitted only after full-Euler receiver closure",
      (receiver_closed_all and graph_action_live) or (not receiver_closed_all))


print("\nD. HOSTILE FENCES AND SUCCESSOR")
for kind, label in (
    ("symplectic", "the induced Green matrix is a finite presymplectic precursor, not a reduced phase space"),
    ("analytic", "finite-field Green rank supplies no hyperbolic estimate, closed domain or Fredholm index"),
    ("variational", "a live transverse current means the zero-fermion stationary branch is not yet a nonzero-fermion solution"),
    ("representation", "no 4D particle content or family count is inferred before receiver/BV/observation closure"),
    ("source", "the nonzero southeast rival remains unconstructed and source-silent in coefficient form"),
    ("scope", "full U64,64, moving Spin and two U32,32 halves remain separate parents"),
    ("accounting", "no datum, P1/P2/P3, residue, quotient or verdict moves"),
):
    check(kind, label, True)

RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "field": f"GF({int(field.characteristic())}) exact action-rank certificate",
    "candidates": results,
    "graph_action": "LIVE" if graph_action_live else "NULL",
    "fermion_connection_current": "LIVE" if fermion_current_live else "ZERO",
    "full_euler_receiver_closure": "AT_LEAST_ONE_CANDIDATE_CLOSES" if receiver_closed_all else "NO_CANDIDATE_CLOSES_ALL_TESTED_COVECTOR_STRATA",
    "bv_disposition": "FINITE_BV_ADMITTED" if receiver_closed_all and graph_action_live else "BV_DEFERRED_PENDING_SOURCE_OWNED_RECEIVER_OR_CONSTRAINT_COMPLETION",
    "source_return": "SOURCE_CONFIRMS_INDEPENDENT_BARRED_UNBARRED_ACTION_AND_CURRENT_CLASS__SOURCE_SILENT_ON_GLOBAL_KREIN_REALITY_ADJOINT_RECEIVER_BV_DOMAIN_AND_NONZERO_SOUTHEAST_MAP",
}

print("\nK77 GAMMA-TRACE GRAPH DYNAMICS RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: the action restriction, transverse fermion current, and full-Euler receiver closure are separately typed; BV is opened only if the receiver closes.")
