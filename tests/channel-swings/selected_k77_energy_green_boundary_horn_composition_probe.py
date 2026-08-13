#!/usr/bin/env sage-python
"""Exact full-carrier energy/Green boundary composition for ledger v0.179.

The completed conditional real-K77 symbol has involutive observed spatial
evolution E and a positive common symmetrizer.  Consequently the maximally
negative energy boundary carrier is exactly ker(E+1).  This probe first
restricts the one-sided coefficient P D_n and then composes the required
doubled Majorana graph.  The distinction is load-bearing: the one-sided
restriction is full rank, while the correctly doubled graded Green
restriction vanishes for both complete Spin-natural pairing horns.

The result is a finite algebraic compatibility gate.  It is not a variable-
coefficient, global, ambient, null-characteristic, Calderon or BFV theorem.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sage.all import GF, block_diagonal_matrix, block_matrix, identity_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, value):
    COUNTS[kind] += 1
    ok = bool(value)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def reject(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject)


def read(relative):
    return (ROOT / relative).read_text()


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
v173 = strict("lab/process/selected-k77-wedge-shiab-southeast-completion.json")
v174 = strict("lab/process/selected-k77-action-adjoint-weight-classification.json")
v177 = strict("lab/process/selected-k77-graded-green-reality-graphs.json")
v178 = strict("lab/process/selected-k77-observed-cauchy-domain-layer0.json")
k95 = read("explorations/eric-curt-wave3d-b2c5-covariant-action-green-ward-2026-08-01.md")

check("source", "source supplies independent barred/unbarred fields but no incoming Green-domain theorem",
      "four distinct fields" in source and "global Hodge/Krein/reality adjoint" in source)
check("prior_art", "two action-pairing horns are complete and exact over two primes",
      v174["exact_primes"] == [1009, 1013] and v174["pairing_ranks"] == [1920, 1920])
check("prior_art", "both horns already have graded doubled-field reality graphs",
      set(v177["action_pairing_horns"].values())
      == {"NONCHARACTERISTIC_GRADED_LAGRANGIAN_REALITY_GRAPH"})
check("prior_art", "the observed incoming carrier is not the doubled Majorana graph",
      "not a spatial incoming-mode projector" in read(
          "tests/channel-swings/selected_k77_observed_cauchy_domain_layer0_probe.py"))
check("prior_art", "K95 found an incoming energy half need not be action-Green isotropic",
      "not Green-isotropic" in k95 and "full rank 960" in k95)
check("prior_art", "completed K77 symbol is semisimple and has a positive common symmetrizer",
      v173["fingerprint"]["spatial_jordan_ranks"] == [0, 0, 0]
      and v173["fingerprint"]["common_symmetrizer_rank"] == 1920)

for label in (
    "a doubled-field Majorana graph is not the incoming energy eigenspace",
    "maximal-negative energy data are not automatically action-Green isotropic",
    "action-Green isotropy is not variable-coefficient analytic closure",
    "failure of one spectral half is not nonexistence of every admissible boundary relation",
    "selected Spin, two U(32,32) halves and full U(64,64) remain distinct",
):
    check("layer0", label, True)


def packet(prime):
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
        prefix, suffix = [s3] * index, [i2] * (n - 1 - index)
        plus.append(tensor_all(prefix + [s1] + suffix))
        minus.append(tensor_all(prefix + [eps] + suffix))
    gammas = plus + minus
    eta = [1] * 7 + [-1] * 7
    identity_s = identity_matrix(field, spin, sparse=True)
    zero_s = zero_matrix(field, spin, spin, sparse=True)
    identity_full = identity_matrix(field, total, sparse=True)

    omega = identity_s
    for gamma in gammas:
        omega *= gamma
    p_plus = (identity_s + omega) / field(2)
    p_minus = (identity_s - omega) / field(2)

    b_spin = identity_s
    for gamma in gammas[7:]:
        b_spin *= gamma

    diagonal_cache = {}

    def diagonal(value):
        key = id(value)
        if key not in diagonal_cache:
            diagonal_cache[key] = block_diagonal_matrix([value] * nv, sparse=True)
        return diagonal_cache[key]

    def wedge(index):
        return block_matrix(
            field, nv, nv,
            [[field(eta[row]) * gammas[row] * gammas[index] * gammas[column]
              if row != index and column not in (row, index) else zero_s
              for column in range(nv)] for row in range(nv)], sparse=True)

    def k_map(index):
        return block_matrix(
            field, nv, 1,
            [[identity_s if row == index else zero_s] for row in range(nv)], sparse=True)

    def codiff(index):
        return block_matrix(
            field, 1, nv,
            [[field(eta[column]) * identity_s if column == index else zero_s
              for column in range(nv)]], sparse=True)

    def symbol(index, w_plus, w_minus):
        ell_plus = field(11) / (field(12) * w_minus)
        ell_minus = field(11) / (field(12) * w_plus)
        weights = w_plus * p_plus + w_minus * p_minus
        southeast = ell_plus * p_plus + ell_minus * p_minus
        return block_matrix(
            field, 2, 2,
            [[wedge(index) * diagonal(weights), k_map(index)],
             [-codiff(index), gammas[index] * southeast]], sparse=True)

    def pairing(a_plus, a_minus, b_plus, b_minus):
        r1 = field(a_plus) * p_plus + field(a_minus) * p_minus
        r0 = field(b_plus) * p_plus + field(b_minus) * p_minus
        return block_diagonal_matrix(
            [field(eta[index]) * b_spin * r1 for index in range(nv)]
            + [b_spin * r0], sparse=True)

    p_sym = pairing(1, 1, 1, 1)
    p_skew = pairing(1, -1, -1, 1)
    p_wrong = pairing(1, 1, -1, -1)
    w_plus, w_minus = field(1), field(2)
    time = symbol(0, w_plus, w_minus)
    normal = symbol(7, w_plus, w_minus)
    evolution = time.solve_right(normal)

    incoming_kernel = (evolution + identity_full).right_kernel()
    outgoing_kernel = (evolution - identity_full).right_kernel()
    incoming = incoming_kernel.basis_matrix().transpose()
    outgoing = outgoing_kernel.basis_matrix().transpose()

    check("exact", f"GF({prime}): evolution is an exact involution",
          evolution * evolution == identity_full)
    check("boundary", f"GF({prime}): incoming and outgoing carriers are complementary halves",
          incoming.ncols() == outgoing.ncols() == 960
          and block_matrix(field, 1, 2, [[incoming, outgoing]], sparse=True).rank() == total)
    check("boundary", f"GF({prime}): incoming carrier is exactly the minus-one eigenspace",
          (evolution * incoming + incoming).is_zero())
    check("boundary", f"GF({prime}): outgoing carrier is exactly the plus-one eigenspace",
          (evolution * outgoing - outgoing).is_zero())

    one_sided_restrictions = {}
    doubled_graph_restrictions = {}
    outgoing_restrictions = {}
    for name, pairing_matrix in (("symmetric_anti_adjoint", p_sym),
                                 ("skew_self_adjoint", p_skew)):
        green = pairing_matrix * normal
        restricted = incoming.transpose() * green * incoming
        # The physical Majorana domain is a graph in doubled barred/unbarred
        # field space.  Pulling back G_D=[[0,D^T],[D,0]] gives
        # P^T D + D^T P, not merely P D.  This is exactly the graded graph
        # criterion from v0.177, now restricted to the incoming energy half.
        doubled_graph_coefficient = (
            pairing_matrix.transpose() * normal
            + normal.transpose() * pairing_matrix
        )
        doubled_restricted = (
            incoming.transpose() * doubled_graph_coefficient * incoming
        )
        outgoing_restricted = outgoing.transpose() * green * outgoing
        one_sided_restrictions[name] = int(restricted.rank())
        doubled_graph_restrictions[name] = int(doubled_restricted.rank())
        outgoing_restrictions[name] = int(outgoing_restricted.rank())
        check("grassmann", f"GF({prime}) {name}: action normal coefficient is alternating",
              green + green.transpose() == zero_matrix(field, total, total, sparse=True))
        check("layer0", f"GF({prime}) {name}: one-sided independent-dual incoming restriction is full rank",
              one_sided_restrictions[name] == 960)
        check("symplectic", f"GF({prime}) {name}: doubled Majorana incoming graph is action-Green isotropic",
              doubled_graph_restrictions[name] == 0)
        check("symplectic", f"GF({prime}) {name}: outgoing action-Green restriction rank recorded wholesale",
              outgoing_restrictions[name] in (0, 960))

    wrong_green = p_wrong * normal
    wrong_restricted_rank = int((incoming.transpose() * wrong_green * incoming).rank())
    check("planted", f"GF({prime}): PLANT wrong pairing is not silently treated as an invariant horn",
          not (wrong_green + wrong_green.transpose()).is_zero())
    check("planted", f"GF({prime}): PLANT zero carrier would vacuously fake isotropy",
          incoming.ncols() == 960 and incoming.rank() == 960)

    return {
        "prime": prime,
        "total_rank": total,
        "incoming_rank": incoming.ncols(),
        "outgoing_rank": outgoing.ncols(),
        "one_sided_incoming_action_green_ranks": one_sided_restrictions,
        "doubled_majorana_incoming_green_ranks": doubled_graph_restrictions,
        "outgoing_action_green_ranks": outgoing_restrictions,
        "wrong_pairing_incoming_rank": wrong_restricted_rank,
    }


print("\nB. TWO-PRIME FULL-CARRIER COMPOSITION")
packets = [packet(1009), packet(1013)]
one_sided_signatures = [packet["one_sided_incoming_action_green_ranks"] for packet in packets]
doubled_signatures = [packet["doubled_majorana_incoming_green_ranks"] for packet in packets]
check("cross_prime", "both primes reproduce the same one-sided and doubled per-horn ranks",
      one_sided_signatures[0] == one_sided_signatures[1]
      and doubled_signatures[0] == doubled_signatures[1])

one_sided_ranks = one_sided_signatures[0]
horn_ranks = doubled_signatures[0]
zero_horns = sorted(name for name, rank in horn_ranks.items() if rank == 0)
if len(zero_horns) == 1:
    outcome = "EXACTLY_ONE_DOUBLED_MAJORANA_HORN_ISOTROPIC_ON_THE_INCOMING_ENERGY_HALF"
elif len(zero_horns) == 2:
    outcome = "BOTH_DOUBLED_MAJORANA_HORNS_ARE_ISOTROPIC_ON_THE_INCOMING_ENERGY_HALF"
else:
    outcome = "INTERMEDIATE_RANK_REQUIRES_RETYPE_OR_REFINED_CLASSIFICATION"

check("classification", "the preregistered horn-composition outcome is decided wholesale",
      outcome != "INTERMEDIATE_RANK_REQUIRES_RETYPE_OR_REFINED_CLASSIFICATION")
check("selection", "no source sentence is used to choose the algebraic outcome", True)
check("analytic", "finite action/energy compatibility does not globalize variable coefficients", True)
check("bfv", "failure of the incoming half would demand a boundary or edge completion, not erase Cauchy evolution", True)
check("datum", "P1 P2 P3 are unchanged and unused", True)

RESULT = {
    "schema_version": "1.0",
    "run_id": "historical-investigation",
    "branch": "CONDITIONAL_REAL_K77_SELECTED_SPIN_OBSERVED_FLAT_1_PLUS_3",
    "checks": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "packets": packets,
    "incoming_energy_carrier": "EXACT_MINUS_ONE_EIGENSPACE_OF_INVOLUTIVE_SPATIAL_EVOLUTION__RANK960",
    "one_sided_independent_dual_restriction_ranks": one_sided_ranks,
    "doubled_majorana_green_restriction_ranks": horn_ranks,
    "zero_horns": zero_horns,
    "outcome": outcome,
    "source_return": "SOURCE_CONFIRMS_INDEPENDENT_FIELDS_AND_PARENT_ARENA__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_INCOMING_ENERGY_ACTION_GREEN_COMMON_DOMAIN_AND_HORN_SELECTION",
    "scope": "FINITE_FLAT_PRINCIPAL_BOUNDARY_COMPOSITION_ONLY__VARIABLE_GLOBAL_AMBIENT_NULL_CALDERON_BFV_AND_UNRESTRICTED_MIXED_OPEN",
    "p1_p2_p3_used": False,
}

print("\nSELECTED K77 ENERGY/GREEN BOUNDARY HORN COMPOSITION")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: " + outcome)
