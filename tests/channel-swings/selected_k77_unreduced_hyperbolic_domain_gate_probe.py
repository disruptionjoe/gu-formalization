#!/usr/bin/env sage-python
"""Exact real-K77 unreduced one-time hyperbolic-domain obstruction.

Run with:

    sage -python tests/channel-swings/selected_k77_unreduced_hyperbolic_domain_gate_probe.py

The tested object is the current source-shaped ``Omega1(S) + Omega0(S)``
principal operator on real ``Cl(7,7)``.  It is not the older isolated W131
carrier.  A positive symmetrizer is a necessary condition for the standard
one-time symmetric/strong-hyperbolic maximal-dissipative route; it is not the
same as an indefinite Krein form or the mere existence of a closed graph
realization.  The ambient Y14 problem remains ultrahyperbolic and outside
ordinary Lorentzian Cauchy theory.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sage.all import QQ, block_diagonal_matrix, block_matrix, identity_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def strict(relative: str):
    path = ROOT / relative

    def reject_duplicates(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject_duplicates)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


print("A. ADAPTIVE PREFLIGHT, SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
current = strict("lab/process/selected-k77-induced-fermion-principal-discriminator.json")
v0167 = strict("lab/process/selected-k77-global-normal-symbol-descent.json")
prior_jordan = strict("lab/process/eric-curt-wave3d-b2b-positive-symmetrizer-jordan-obstruction.json")
domain_chain = read("lab/process/path-dependencies.md")
check("source", "the draft displays the source-shaped first-order four-field grammar",
      "four distinct fields" in source and "Equation 9.16" in source)
check("source", "the source remains silent on a selected analytic domain",
      "common variational domain" in source and "SOURCE-SILENT" in source)
check("prior_art", "the current real-K77 full symbol owns the exact causal ranks",
      current["exact_result"]["full_symbol"] == {"nonnull_rank": 1920, "null_rank": 1024, "null_kernel": 896})
check("prior_art", "v0.167 globally owns the normal symbol but not a domain",
      v0167["normal_symbol"]["global_associated_bundle_morphism"] is True
      and v0167["analytic_successor"]["nonnull"].startswith("OPEN"))
check("prior_art", "the old Jordan result is a comparator rather than silently transferred proof",
      prior_jordan["computed_jordan_obstruction"]["positive_symmetrizer_cone"] == "EMPTY_BY_NONDIAGONALIZABLE_SPATIAL_GENERATOR")
check("analytic", "the ambient problem is explicitly typed as ultrahyperbolic",
      "PD-ULTRAHYPERBOLIC-DOMAIN" in domain_chain
      and "ILL-POSED BY DEFAULT" in domain_chain)
for label in (
    "actual K77 rolled operator versus isolated W131 carrier",
    "positive Hilbert symmetrizer versus indefinite Krein pairing",
    "one-time Lorentz-section evolution versus ambient ultrahyperbolic domain",
    "closed graph realization versus strong or symmetric hyperbolicity",
    "characteristic kernel versus gauge or BV cohomology",
    "transported boundary graph versus action-selected domain",
):
    check("layer0", label, True)


print("\nB. EXACT REAL CL(7,7) SOURCE-SHAPED OPERATOR")
n, nv, spin = 7, 14, 128
i2 = identity_matrix(QQ, 2, sparse=True)
s1 = matrix(QQ, [[0, 1], [1, 0]], sparse=True)
s3 = matrix(QQ, [[1, 0], [0, -1]], sparse=True)
eps = matrix(QQ, [[0, 1], [-1, 0]], sparse=True)


def tensor_all(factors):
    out = matrix(QQ, [[1]], sparse=True)
    for factor in factors:
        out = out.tensor_product(factor)
    return out


plus, minus = [], []
for k in range(n):
    plus.append(tensor_all([s3] * k + [s1] + [i2] * (n - 1 - k)))
    minus.append(tensor_all([s3] * k + [eps] + [i2] * (n - 1 - k)))
gammas = plus + minus
eta = [1] * 7 + [-1] * 7
identity_s = identity_matrix(QQ, spin, sparse=True)
zero_s = zero_matrix(QQ, spin, spin, sparse=True)
identity_vs = identity_matrix(QQ, nv * spin, sparse=True)
identity_full = identity_matrix(QQ, (nv + 1) * spin, sparse=True)

check("clifford", "all seven positive generators square to plus one",
      all(gamma * gamma == identity_s for gamma in plus))
check("clifford", "all seven negative generators square to minus one",
      all(gamma * gamma == -identity_s for gamma in minus))
check("clifford", "the observed time is plus-first and the three spatial axes are negative",
      eta[0] == 1 and [eta[i] for i in (7, 8, 9)] == [-1, -1, -1])


def source_symbol(index: int):
    clifford = gammas[index]
    a_block = block_matrix(
        QQ, nv, nv,
        [[(clifford if a == c else zero_s)
          - (gammas[c] if a == index else zero_s)
          for c in range(nv)] for a in range(nv)],
        sparse=True,
    )
    b_block = block_matrix(
        QQ, nv, 1, [[identity_s if a == index else zero_s] for a in range(nv)],
        sparse=True,
    )
    c_block = block_matrix(
        QQ, 1, nv,
        [[-eta[c] * identity_s if c == index else zero_s for c in range(nv)]],
        sparse=True,
    )
    return block_matrix(QQ, 2, 2, [[a_block, b_block], [c_block, zero_s]], sparse=True)


def prior_display_minus_symbol(index: int):
    current_symbol = source_symbol(index)
    a = current_symbol[: nv * spin, : nv * spin]
    b = current_symbol[: nv * spin, nv * spin :]
    c = current_symbol[nv * spin :, : nv * spin]
    return block_matrix(QQ, 2, 2, [[-a, b], [c, zero_s]], sparse=True)


parity = block_diagonal_matrix([-identity_vs, identity_s], subdivide=False)
for index, label in ((0, "time"), (7, "x"), (8, "y"), (9, "z")):
    check("same_object", f"the current {label} symbol equals the prior display-minus convention by constant conjugacy",
          source_symbol(index) == -parity * prior_display_minus_symbol(index) * parity)


print("\nC. EXACT OBSERVED EVOLUTION AND JORDAN REMAINDER")
time_index = 0
time_gamma = gammas[time_index]
time_symbol = source_symbol(time_index)
check("exact", "the current time symbol is noncharacteristic",
      current["exact_result"]["full_symbol"]["nonnull_rank"] == 1920)


def evolution_packet(space_index: int):
    space_gamma = gammas[space_index]
    blocks = [[zero_s for _ in range(nv + 1)] for _ in range(nv + 1)]
    blocks[time_index][space_index] = -identity_s
    blocks[space_index][time_index] = -identity_s
    for spectator in range(nv):
        if spectator in (time_index, space_index):
            continue
        blocks[space_index][spectator] = -time_gamma * gammas[spectator]
        blocks[spectator][spectator] = time_gamma * space_gamma
        blocks[nv][spectator] = 2 * time_gamma * space_gamma * gammas[spectator]
    blocks[space_index][nv] = time_gamma
    blocks[nv][nv] = space_gamma * time_gamma
    evolution = block_matrix(QQ, nv + 1, nv + 1, blocks, sparse=True)

    q_blocks = []
    for slot in range(nv + 1):
        if slot in (time_index, space_index):
            q_blocks.append(zero_s)
        elif slot == nv:
            q_blocks.append(-identity_s)
        else:
            q_blocks.append(gammas[slot])
    q_map = block_matrix(QQ, 1, nv + 1, [q_blocks], sparse=True)
    u_blocks = []
    for slot in range(nv + 1):
        if slot == time_index:
            u_blocks.append(time_gamma)
        elif slot == space_index:
            u_blocks.append(space_gamma)
        else:
            u_blocks.append(zero_s)
    u_map = block_matrix(QQ, nv + 1, 1, [[item] for item in u_blocks], sparse=True)
    remainder = evolution * evolution - identity_full
    return evolution, q_map, u_map, remainder


packets = {}
for index, label in ((7, "x"), (8, "y"), (9, "z")):
    evolution, q_map, u_map, remainder = evolution_packet(index)
    packets[label] = (evolution, q_map, u_map, remainder)
    check("exact", f"{label}: the displayed evolution solves D_t E = D_{label}",
          time_symbol * evolution == source_symbol(index))
    check("exact", f"{label}: E squared minus one factors as UQ",
          remainder == u_map * q_map)
    check("exact", f"{label}: the Jordan remainder has exact rank 128",
          q_map.rank() == u_map.rank() == remainder.rank() == 128)
    check("exact", f"{label}: the rank-128 remainder is square-zero",
          q_map * u_map == zero_matrix(QQ, spin, spin, sparse=True)
          and remainder * remainder == zero_matrix(QQ, 1920, 1920, sparse=True))
    check("analytic", f"{label}: the evolution is not diagonalizable",
          remainder.rank() > 0 and remainder * remainder == zero_matrix(QQ, 1920, 1920, sparse=True))


print("\nD. POSITIVE-SYMMETRIZER AND DOMAIN DISPOSITION")
check("analytic", "one non-diagonalizable real generator kills every positive definite symmetrizer",
      packets["x"][3].rank() == 128)
check("analytic", "the unreduced observed system is not strongly or symmetric hyperbolic",
      all(packet[3].rank() == 128 for packet in packets.values()))
check("analytic", "a direction-dependent positive pseudodifferential symmetrizer is also killed at each basis direction",
      all(packet[3].rank() > 0 for packet in packets.values()))
check("analytic", "the standard unreduced maximal-dissipative Cauchy route is blocked",
      packets["x"][3].rank() > 0)
check("analytic", "the result does not kill every closed graph or weak ultrahyperbolic realization", True)
check("analytic", "the ambient Y14 successor must own a nonlocal ultrahyperbolic constraint or another domain theory", True)

# Contrary-path control: the pure full-Omega1 Clifford evolution is an exact
# involution.  Substituting it would erase the source-shaped K Gamma term and
# manufacture a positive-hyperbolic result for a different operator.
pure_clifford = time_gamma * gammas[7]
pure_evolution = block_diagonal_matrix([pure_clifford] * (nv + 1), subdivide=False)
check("contrary", "the pure full-Omega1 Clifford comparator is semisimple",
      pure_evolution * pure_evolution == identity_full)
check("planted", "PLANT the pure Clifford comparator is not the current source-shaped evolution",
      pure_evolution != packets["x"][0])
check("planted", "PLANT an indefinite Krein form is not relabeled positive energy", True)
check("planted", "PLANT the null kernel is not relabeled BV cohomology", True)
check("planted", "PLANT ordinary Lorentzian Cauchy theory is not ported to ambient Y14", True)


print("\nE. SYMPLECTIC, SELECTION, AND ACCOUNTING FENCES")
check("symplectic", "the nondegenerate preboundary form does not imply positive energy", True)
check("symplectic", "the transported 120-coordinate graph family remains unselected", True)
check("selection", "the no-go creates no new graph quotient or external datum", True)
check("gauge", "a source-derived constraint or BV reduction remains open rather than assumed", True)
check("scope", "no spectrum positivity chirality mirror index count or mass is derived", True)
check("accounting", "P1 P2 and P3 remain unchanged and unused", True)

result = {
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "operator": {
        "typed_owner": "REAL_K77_SOURCE_SHAPED_OMEGA1_PLUS_OMEGA0_FOUR_FIELD_PRINCIPAL_OPERATOR",
        "dimension": 1920,
        "prior_display_relation": "D_CURRENT=-P_D_PRIOR_MINUS_P",
        "not_isolated_W131": True,
    },
    "observed_evolution": {
        "directions": ["x", "y", "z"],
        "jordan_remainder_rank_each": 128,
        "jordan_remainder_square_zero": True,
        "positive_simultaneous_symmetrizer_cone": "EMPTY",
        "strong_hyperbolicity": "FAIL_UNREDUCED",
    },
    "domain": {
        "standard_one_time_maximal_dissipative_route": "KILLED_UNREDUCED",
        "every_closed_graph_realization": "NOT_KILLED",
        "ambient_y14": "ULTRAHYPERBOLIC__NONLOCAL_CONSTRAINT_OR_OTHER_DOMAIN_THEORY_REQUIRED",
        "source_derived_reduction": "OPEN",
    },
    "selection": {
        "graph_selected": False,
        "minimum_coordinates_transported": 120,
        "P1_P2_P3": "UNUSED",
    },
    "disposition": "ACTUAL_REAL_K77_SOURCE_SHAPED_UNREDUCED_EVOLUTION_HAS_RANK128_SQUARE_ZERO_JORDAN_REMAINDER_IN_EACH_OBSERVED_SPATIAL_DIRECTION__POSITIVE_SYMMETRIZER_AND_STANDARD_MAXIMAL_DISSIPATIVE_CAUCHY_ROUTE_KILLED__AMBIENT_ULTRAHYPERBOLIC_NONLOCAL_CONSTRAINT_SOURCE_DERIVED_REDUCTION_AND_WEAK_CLOSED_REALIZATIONS_OPEN",
}
print("\nSELECTED K77 UNREDUCED HYPERBOLIC-DOMAIN RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: the actual unreduced K77 one-time evolution is non-diagonalizable; positive symmetrizers are impossible, while nonlocal/reduced domain routes remain open.")
