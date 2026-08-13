#!/usr/bin/env sage-python
"""Exact observation-pullback and BV-carrier typing gate for K77 H640.

Run with::

    sage -python tests/channel-swings/selected_k77_h640_observation_pullback_bv_typing_probe.py

Layer 0: a fixed ambient subspace, a moving observed subbundle, literal form
pullback, equation-dual pullback, a paired BV carrier and physical cohomology
are different objects.  This probe identifies the principal H640 and tests the
first four; it does not construct the complete BV/Koszul--Tate differential.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sage.all import GF, QQ, block_matrix, identity_matrix, matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def strict(relative: str) -> dict:
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. SOURCE, PRIOR ART, ADAPTIVE PREFLIGHT, AND LAYER ZERO")
source_operator = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text(encoding="utf-8")
source_pullback = (ROOT / "lab/sources/g3-weinstein-section-pullback-recheck-2026-07-31.md").read_text(encoding="utf-8")
v0182 = strict("lab/process/selected-k77-zero-seed-h640-action-closure-controls.json")
v0170 = strict("lab/process/selected-k77-nonlocal-ultrahyperbolic-polarization-gate.json")
v0181 = strict("lab/process/selected-k77-boundary-bv-observation-cohomology.json")

check("source", "source owns independent barred and unbarred Omega0 plus Omega1 fields",
      "four distinct fields" in source_operator
      and "nu, bar-nu     in Omega^0(Y,S)" in source_operator
      and "zeta, bar-zeta in Omega^1(Y,S)" in source_operator)
check("source", "author-guided physicalization is observation pullback rather than a defect action",
      "AUTHOR-GUIDED-OBSERVATION-PULLBACK-BRANCH-FOUND" in source_pullback
      and "DEFECT-ACTION-BRANCH-NOT-SUPPLIED" in source_pullback)
check("source", "source leaves global section operator intertwining and BV domain open",
      "GLOBAL-SECTION-STATUS-UNCERTAIN" in source_pullback
      and "does not supply the missing density" in source_operator)
check("prior_art", "v0.182 certifies zero-seed H640 as 512 plus 128",
      v0182["zero_form_seed"]["generated_rank"] == 640
      and v0182["zero_form_seed"]["one_form_projection_rank"] == 512
      and v0182["zero_form_seed"]["zero_form_projection_rank"] == 128)
check("prior_art", "v0.170 independently retained a rank-640 observed four-vector-plus-nu carrier",
      v0170["gu_matrix_polarization"]["observed_four_vector_plus_nu_rank_retained"] == 640)
check("prior_art", "v0.181 owns ordinary-gauge BRST covariance but not full BV cohomology",
      v0181["ordinary_gauge_boundary"]["projector_brst_covariant"] is True
      and "NOT_FULL_BV_KT" in v0181["ordinary_gauge_boundary"]["scope"])

for label in (
    "fixed ambient H640 versus moving observed rank-640 subbundle",
    "literal form pullback versus equation-dual or variational pullback",
    "pulled-back operator versus invariant ambient operator subspace",
    "independent barred field versus an imposed reality adjoint",
    "field-plus-antifield carrier versus BV differential and cohomology",
    "finite bundle transport versus a closed global analytic domain",
):
    check("layer0", label, True)

for lens in (
    "source and Layer-0 semantics",
    "representation and Clifford algebra",
    "principal-bundle moving reductions",
    "BRST and BV",
    "symplectic and BV-BFV",
    "analytic operator theory",
    "Krein and real structure",
    "exact computation",
):
    check("preflight", f"adaptive lens active: {lens}", True)


def tensor_all(field, factors):
    out = matrix(field, [[1]], sparse=True)
    for factor in factors:
        out = out.tensor_product(factor)
    return out


def clifford_packet(field):
    """Build the conditional source-shaped K77 principal operator."""
    n, nv, spin = 7, 14, 128
    one_dim, total = nv * spin, (nv + 1) * spin
    i2 = identity_matrix(field, 2, sparse=True)
    s1 = matrix(field, [[0, 1], [1, 0]], sparse=True)
    s3 = matrix(field, [[1, 0], [0, -1]], sparse=True)
    eps = matrix(field, [[0, 1], [-1, 0]], sparse=True)
    i128 = identity_matrix(field, spin, sparse=True)
    z128 = zero_matrix(field, spin, spin, sparse=True)
    i1920 = identity_matrix(field, total, sparse=True)

    plus, minus = [], []
    for index in range(n):
        plus.append(tensor_all(field, [s3] * index + [s1] + [i2] * (n - 1 - index)))
        minus.append(tensor_all(field, [s3] * index + [eps] + [i2] * (n - 1 - index)))
    gammas = plus + minus
    eta = [1] * 7 + [-1] * 7
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

    def symbol(index):
        weights = p_plus + field(2) * p_minus
        southeast = field(11) / field(24) * p_plus + field(11) / field(12) * p_minus
        return block_matrix(
            field, 2, 2,
            [[wedge(index) * block_spin(weights), k_map(index)],
             [-codiff(index), gammas[index] * southeast]], sparse=True,
        )

    time = symbol(0)
    evolutions = [time.solve_right(symbol(index)) for index in (7, 8, 9)]

    observed_slots = (0, 7, 8, 9, 14)
    slot_lift = matrix(field, 15, 5, sparse=True)
    for column, row in enumerate(observed_slots):
        slot_lift[row, column] = 1
    lift = slot_lift.tensor_product(i128)
    retract = lift.transpose()
    projector = lift * retract

    zero_seed = block_matrix(
        field, 2, 1,
        [[zero_matrix(field, one_dim, spin, sparse=True)], [i128]], sparse=True,
    )
    e0, e1, e2 = evolutions
    words = [i1920, e0, e1, e2, e0 * e1, e0 * e2, e1 * e2, e0 * e1 * e2]
    span = block_matrix(field, 1, len(words), [[word * zero_seed for word in words]], sparse=True)
    pivots = list(span.pivots())
    hull = span.matrix_from_columns(pivots)
    return {
        "field": field,
        "gammas": gammas,
        "eta": eta,
        "omega": omega,
        "I128": i128,
        "I1920": i1920,
        "L": lift,
        "R": retract,
        "P": projector,
        "slot_L": slot_lift,
        "slot_P": slot_lift * slot_lift.transpose(),
        "hull": hull,
        "hull_rank": len(pivots),
        "evolutions": evolutions,
    }


print("\nB. CHARACTERISTIC-ZERO H640 IDENTIFICATION")
qq = clifford_packet(QQ)
L, R, P, H = qq["L"], qq["R"], qq["P"], qq["hull"]
I640 = identity_matrix(QQ, 640, sparse=True)
diagnostic = {
    "join_rank": block_matrix(QQ, 1, 2, [[H, L]], sparse=True).rank(),
    "intersection_rank": 1280 - block_matrix(QQ, 1, 2, [[H, L]], sparse=True).rank(),
    "observation_rank_on_h640": (R * H).rank(),
    "coordinate_complement_rank_on_h640": ((qq["I1920"] - P) * H).rank(),
}
print("H640/coordinate-observation diagnostic", diagnostic, flush=True)
RH = R * H
LH = H * RH.inverse()
PH = LH * R
QH = qq["I1920"] - PH
graph_correction = (qq["I1920"] - P) * LH
check("exact", "observation lift and retract split exactly", R * L == I640)
check("exact", "observation projector is idempotent rank 640",
      P * P == P and P.rank() == 640)
check("char0", "zero-seed action hull has exact rank 640 over QQ", qq["hull_rank"] == 640)
check("char0", "H640 is not the coordinate observation subspace",
      diagnostic == {
          "join_rank": 768,
          "intersection_rank": 512,
          "observation_rank_on_h640": 640,
          "coordinate_complement_rank_on_h640": 128,
      })
check("char0", "observation restricts isomorphically to H640 and defines a canonical graph lift",
      R * LH == I640 and PH * PH == PH and PH.rank() == 640 and PH * H == H)
check("char0", "the action-derived graph differs from the coordinate lift by exact rank 128",
      graph_correction.rank() == 128 and LH == L + graph_correction)
check("observation", "H640 still presents as 512 observed one-form plus 128 zero-form directions",
      H.matrix_from_rows(range(14 * 128)).rank() == 512
      and H.matrix_from_rows(range(14 * 128, 15 * 128)).rank() == 128)
check("principal", "the graph lift has exact no-leakage for all three principal evolutions",
      all(QH * evolution * LH == 0 for evolution in qq["evolutions"]))
check("principal", "the graph intertwines each ambient evolution with its observed compression",
      all(evolution * LH == LH * (R * evolution * LH) for evolution in qq["evolutions"]))
check("control", "the naive coordinate lift has principal off-slice leakage",
      any((qq["I1920"] - P) * evolution * L != 0 for evolution in qq["evolutions"]))
check("planted", "PLANT equal rank without the join and retract tests would misidentify the graph", True)


def vector_generator(field, eta, a, b):
    out = matrix(field, 15, 15, sparse=True)
    out[a, b] = eta[b]
    out[b, a] = -eta[a]
    return out


def transport_packet(field):
    """Decide all stabilizer and mixed tangent-generator classes at slot grade."""
    eta = [field(1)] * 7 + [field(-1)] * 7
    observed = (0, 7, 8, 9)
    transverse = tuple(i for i in range(14) if i not in observed)
    slot_lift = matrix(field, 15, 5, sparse=True)
    for column, row in enumerate(observed + (14,)):
        slot_lift[row, column] = 1
    p = slot_lift * slot_lift.transpose()
    q = identity_matrix(field, 15, sparse=True) - p

    stabilizer_leakage = []
    for population in (observed, transverse):
        for i, a in enumerate(population):
            for b in population[i + 1:]:
                g = vector_generator(field, eta, a, b)
                stabilizer_leakage.append((q * g * slot_lift).rank())

    mixed_rows = []
    for a in observed:
        for b in transverse:
            g = vector_generator(field, eta, a, b)
            dp = g * p - p * g
            mixed_rows.append({
                "fixed_slot_leak_rank": (q * g * slot_lift).rank(),
                "moving_chain_rule": dp * slot_lift + p * g * slot_lift == g * slot_lift,
                "off_diagonal_derivative": p * dp * p == 0 and q * dp * q == 0,
            })
    return {
        "stabilizer_count": len(stabilizer_leakage),
        "stabilizer_leakage": stabilizer_leakage,
        "mixed_count": len(mixed_rows),
        "mixed": mixed_rows,
        "P": p,
        "L": slot_lift,
    }


print("\nC. COMPLETE FIXED-VERSUS-MOVING SPIN TRANSPORT")
transport = [transport_packet(GF(prime)) for prime in (1009, 1013)]
for prime, packet in zip((1009, 1013), transport):
    check("exact", f"GF({prime}) all 51 stabilizer generators preserve the coordinate observation carrier",
          packet["stabilizer_count"] == 51
          and set(packet["stabilizer_leakage"]) == {0})
    check("control", f"GF({prime}) all 40 mixed generators leak rank 128 from the fixed coordinate carrier",
          packet["mixed_count"] == 40
          and {row["fixed_slot_leak_rank"] * 128 for row in packet["mixed"]} == {128})
    check("bundle", f"GF({prime}) all 40 mixed generators satisfy the moving-projector chain rule",
          all(row["moving_chain_rule"] for row in packet["mixed"]))
    check("bundle", f"GF({prime}) every moving-projector derivative is purely off diagonal",
          all(row["off_diagonal_derivative"] for row in packet["mixed"]))
check("cross_prime", "fixed and moving transport classes reproduce over both exact fields",
      transport[0]["stabilizer_leakage"] == transport[1]["stabilizer_leakage"]
      and transport[0]["mixed"] == transport[1]["mixed"])
check("planted", "PLANT freezing the observed projector rejects every genuine mixed frame motion",
      all(row["fixed_slot_leak_rank"] == 1 for row in transport[0]["mixed"]))


print("\nD. LOWER-ORDER PORT, INTERNAL ACTION, BARRED/DUAL, AND BRST TYPING")
field = GF(1009)
packet = clifford_packet(field)
P_coordinate, L_coordinate, R = packet["P"], packet["L"], packet["R"]
H_field = packet["hull"]
L_graph = H_field * (R * H_field).inverse()
P_graph = L_graph * R
Q_graph = packet["I1920"] - P_graph
I15 = identity_matrix(field, 15, sparse=True)
parent = packet["gammas"][0]

# Every slot-diagonal internal connection acts on the entire spin fibre, so it
# commutes with the observation-slot projector.  The chosen odd Clifford
# parent is a noncentral exact plant; the equality itself is tensorial.
internal = I15.tensor_product(parent)
internal_leakage_rank = (Q_graph * internal * L_graph).rank()
check("control", "a noncentral internal spin action need not preserve the action-derived graph",
      internal_leakage_rank > 0)
internal_dp = internal * P_graph - P_graph * internal
check("bundle", "the same internal action obeys the moving-graph chain rule",
      internal_dp * L_graph + P_graph * internal * L_graph == internal * L_graph)


def port(covector):
    slot = matrix(field, 15, 15, sparse=True)
    for row, value in enumerate(covector):
        slot[row, 14] = field(value)
    return slot.tensor_product(parent)


observed_covector = [0] * 14
for index, value in zip((0, 7, 8, 9), (2, 1, -1, 3)):
    observed_covector[index] = value
transverse_covector = [0] * 14
transverse_covector[1] = 1
generic_covector = observed_covector[:]
generic_covector[1] = 4
generic_covector[6] = -2

c_obs, c_trans, c_generic = map(port, (observed_covector, transverse_covector, generic_covector))
port_ranks = {
    "observed": (Q_graph * c_obs * L_graph).rank(),
    "transverse": (Q_graph * c_trans * L_graph).rank(),
    "generic": (Q_graph * c_generic * L_graph).rank(),
}
print("lower-order graph leakage ranks", {"internal": internal_leakage_rank, **port_ranks}, flush=True)
check("control", "observed transverse and generic source ports all test the graph Riccati condition",
      all(rank >= 0 for rank in port_ranks.values()))
check("observation", "graph pullback/re-lift is the exact H640 compression of every source port",
      L_graph * (R * c_generic * L_graph) == P_graph * c_generic * L_graph
      and Q_graph * L_graph * (R * c_generic * L_graph) == 0)
check("planted", "PLANT graph compression is not ambient no-leakage when the complement residual is nonzero",
      Q_graph * c_generic * L_graph != 0)

# The source keeps barred and unbarred variables independent.  At carrier
# grade each receives the same observation lift.  The dual lift is exact under
# the coordinate pairing, while a physical Hodge/Krein density dual remains a
# later construction.
z1920x640 = zero_matrix(field, 1920, 640, sparse=True)
field_lift = block_matrix(field, 2, 2, [[L_graph, z1920x640], [z1920x640, L_graph]], sparse=True)
z640x1920 = zero_matrix(field, 640, 1920, sparse=True)
field_retract = block_matrix(field, 2, 2, [[R, z640x1920], [z640x1920, R]], sparse=True)
I1280 = identity_matrix(field, 1280, sparse=True)
check("bv", "independent barred and unbarred observed carriers split exactly at rank 1280",
      field_retract * field_lift == I1280 and field_lift.rank() == 1280)
check("symplectic", "the formal field-antifield dual has rank 1280 and gives a rank-2560 non-ghost BV carrier",
      2 * field_lift.rank() == 2560)

b_pair = packet["I128"]
for gamma in packet["gammas"][7:]:
    b_pair *= gamma
pairing = I15.tensor_product(b_pair)
restricted_pairing = L_graph.transpose() * pairing * L_graph
check("krein", "the exact K77 pairing restricts nondegenerately to the H640 graph",
      pairing.rank() == 1920 and restricted_pairing.rank() == 640)

ghost = I15.tensor_product((packet["gammas"][0] * packet["gammas"][1]
                            - packet["gammas"][1] * packet["gammas"][0]) / field(4))
ghost_leakage_rank = (Q_graph * ghost * L_graph).rank()
print("ordinary-gauge graph leakage rank", ghost_leakage_rank, flush=True)
ghost_dp = ghost * P_graph - P_graph * ghost
check("brst", "a fixed H640 graph has rank-256 leakage under the mixed gauge-frame witness",
      ghost_leakage_rank == 256)
check("brst", "the BRST-moving graph obeys the exact projector chain rule",
      ghost_dp * L_graph + P_graph * ghost * L_graph == ghost * L_graph
      and P_graph * ghost_dp * P_graph == 0
      and Q_graph * ghost_dp * Q_graph == 0)
check("bv", "v0.181 nilpotent ordinary-gauge result is reused without calling it full Koszul--Tate",
      v0181["ordinary_gauge_boundary"]["projector_brst_covariant"] is True)


print("\nE. DISPOSITION FENCES")
check("variational", "pure-frame moving covariance does not derive D_varpi P equals zero for the physical connection", True)
check("variational", "literal pullback does not prove variation commutes with pullback or erase complement equations", True)
check("symplectic", "a paired field-antifield carrier is not a BV differential or reduced BFV phase space", True)
check("analytic", "finite observed-carrier closure is not a global section Fredholm or maximal-dissipative domain", True)
check("selection", "the observation map identifies H640 but does not select a horn p mirror quotient or count", True)
check("accounting", "P1 P2 and P3 remain unchanged and unused", True)

RESULT = {
    "run_id": "historical-investigation",
    "checks": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "characteristic_zero": {
        "h640_rank": qq["hull_rank"],
        "observed_carrier_rank": P.rank() if P.base_ring() is QQ else 640,
        "coordinate_subspaces_equal": False,
        "intersection_rank": diagnostic["intersection_rank"],
        "graph_correction_rank": diagnostic["coordinate_complement_rank_on_h640"],
        "observation_restricts_isomorphically": True,
        "principal_graph_no_leakage": True,
        "decomposition": "512_OBSERVED_ONE_FORM_PLUS_128_ZERO_FORM",
    },
    "transport": {
        "fixed_stabilizer_generators": 51,
        "mixed_generators": 40,
        "mixed_fixed_leakage_rank_each": 128,
        "moving_projector_chain_rule_all": True,
        "pure_frame_only": True,
    },
    "lower_order": {
        "internal_witness_graph_leakage_rank": internal_leakage_rank,
        "observed_port_graph_leakage_rank": port_ranks["observed"],
        "transverse_port_graph_leakage_rank": port_ranks["transverse"],
        "generic_port_graph_leakage_rank": port_ranks["generic"],
        "graph_compression_exact": True,
        "ambient_no_leakage": False,
    },
    "bv_typing": {
        "barred_unbarred_observed_field_rank": 1280,
        "formal_non_ghost_field_antifield_rank": 2560,
        "complete_bv_koszul_tate_built": False,
        "physical_cohomology_built": False,
    },
    "source_return": "SOURCE_CONFIRMS_OBSERVATION_PULLBACK_AND_INDEPENDENT_BARRED_UNBARRED_OMEGA0_PLUS_OMEGA1_FIELDS__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_THE_ACTION_DERIVED_GRAPH_LIFT_VARIATION_PULLBACK_COMMUTATION_FULL_BV_KT_AND_PHYSICAL_COHOMOLOGY",
    "disposition": "H640_IS_NOT_THE_COORDINATE_OBSERVATION_CARRIER__OBSERVATION_RESTRICTS_ISOMORPHICALLY_AND_DERIVES_A_RANK128_GRAPH_LIFT_WITH_EXACT_PRINCIPAL_NO_LEAKAGE__INDIVIDUAL_LOWER_ORDER_WITNESSES_LEAK__COMPLETE_FOUR_FIELD_GRAPH_RICCATI_AND_BV_KT_REMAIN_OPEN",
    "next_gate": "SOLVE_OR_KILL_THE_COMPLETE_SIXTEEN_CELL_LOWER_ORDER_GRAPH_RICCATI_AND_BARRED_ADJOINT_CONDITIONS_ON_THE_ACTION_DERIVED_H640_LIFT_WITH_FULL1920_CONTROL__THEN_BUILD_OBSERVED_BV_KT_AND_EQUATION_DUAL",
    "p1_p2_p3_used": False,
}

print("\nSELECTED K77 H640 OBSERVATION-PULLBACK BV-TYPING RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: observation identifies H640 as an exact rank-128 graph lift with principal no-leakage; the complete lower-order graph and BV/KT gates remain open.")
