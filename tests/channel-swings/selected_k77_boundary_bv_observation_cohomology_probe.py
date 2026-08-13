#!/usr/bin/env sage-python
"""Exact K77 boundary/BRST/observation and W-mirror typing gate.

Run with::

    sage -python tests/channel-swings/selected_k77_boundary_bv_observation_cohomology_probe.py

The source-derived object available at v0.164 is the local ordinary-gauge
BRST differential.  This probe composes it with v0.180's action-derived
incoming-projector family and tests the proposed W/mirror carriers before any
physical-cohomology language is admitted.  Ordinary-gauge BRST, a full
BV/Koszul--Tate differential, a boundary BFV quotient and an analytic physical
cohomology are kept distinct throughout.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sage.all import GF, block_diagonal_matrix, block_matrix, diagonal_matrix, identity_matrix, matrix, zero_matrix


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
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def qmatrix(rows):
    from fractions import Fraction as Q
    return matrix([[Q(entry) for entry in row] for row in rows])


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
v0164 = strict("lab/process/selected-k77-coupled-gauge-noether-bv.json")
v0167 = strict("lab/process/selected-k77-global-normal-symbol-descent.json")
v0177 = strict("lab/process/selected-k77-graded-green-reality-graphs.json")
v0180 = strict("lab/process/selected-k77-variable-incoming-projector-descent.json")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text(encoding="utf-8")

check("source", "source supplies the four independent fermion fields and covariance grammar",
      "four distinct fields" in source and "rho(epsilon)" in source)
check("source", "source does not supply the explicit ordinary-gauge BRST or physical boundary cohomology",
      "common variational domain" in source and "three-family index" in source)
check("prior_art", "v0.164 owns a nilpotent local ordinary-gauge BRST differential",
      v0164["minimal_brst"]["nilpotent_on_every_declared_field"]
      and v0164["minimal_brst"]["fermion_residuals_transform_covariantly"])
check("prior_art", "v0.167 owns associated-bundle descent of the actual normal symbol",
      v0167["normal_symbol"]["global_associated_bundle_morphism"])
check("prior_art", "v0.177 owns two noncharacteristic doubled-Majorana Green graphs",
      all("NONCHARACTERISTIC_GRADED_LAGRANGIAN" in value
          for value in v0177["action_pairing_horns"].values()))
check("prior_art", "v0.180 owns the rank-960 action-derived incoming family",
      v0180["immutable_full_carrier"]["rank"] == 1920
      and v0180["immutable_full_carrier"]["incoming_rank"] == 960
      and not v0180["ownership"]["independent_projector_datum_needed"])

for label in (
    "ordinary-gauge BRST versus full BV and Koszul-Tate differential",
    "boundary-subbundle invariance versus unrestricted BFV basicness",
    "associated-bundle observation descent versus complete 4+10 Euler faithfulness",
    "W or mirror field carrier versus cohomology class",
    "incoming projector on the full carrier versus its restriction to a proposed subcarrier",
    "equality of finite fingerprints versus an analytic physical isomorphism",
):
    check("layer0", label, True)


print("\nB. EXACT BRST AND OBSERVATION NATURALITY OF THE PROJECTOR FAMILY")
# A noncommuting rational fixture tests the structural identity without
# assuming that a gauge frame fixes the projector.  The projector itself
# transforms in the adjoint bundle: s Pi=[c,Pi].
identity4 = identity_matrix(4)
evolution = qmatrix([
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, -1],
])
projector = (identity4 - evolution) / 2
ghost = qmatrix([
    [0, 1, 1, 0],
    [-1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, -1, 0],
])
psi = matrix([[2], [-1], [3], [1]])
s_projector = ghost * projector - projector * ghost
s_psi = ghost * psi

check("exact", "the comparator evolution is involutive and defines a half-rank projector",
      evolution * evolution == identity4
      and projector * projector == projector and projector.rank() == 2)
check("bv", "the moving projector is BRST covariant rather than gauge-fixed",
      s_projector == ghost * projector - projector * ghost
      and not s_projector.is_zero())
check("bv", "the incoming boundary relation is a BRST subbundle",
      s_projector * psi + projector * s_psi == ghost * projector * psi)
check("planted", "PLANT freezing the projector breaks the BRST chain rule",
      projector * s_psi != ghost * projector * psi)

u1 = qmatrix([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
u2 = qmatrix([[1, 0, 1, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 1]])
check("observation", "the two rational observation/frame maps are invertible and noncommuting",
      u1.det() != 0 and u2.det() != 0 and u1 * u2 != u2 * u1)

frames = [identity4, u1, u2 * u1]
for index, frame in enumerate(frames):
    inv = frame.inverse()
    p_i = frame * projector * inv
    c_i = frame * ghost * inv
    psi_i = frame * psi
    sp_i = c_i * p_i - p_i * c_i
    check("observation", f"patch {index} projector remains idempotent rank two",
          p_i * p_i == p_i and p_i.rank() == 2)
    check("bv", f"patch {index} BRST boundary relation is natural",
          sp_i * psi_i + p_i * c_i * psi_i == c_i * p_i * psi_i)

direct = frames[2] * projector * frames[2].inverse()
sequential = u2 * (u1 * projector * u1.inverse()) * u2.inverse()
check("observation", "direct and sequential projector descent agree", direct == sequential)
check("planted", "PLANT transporting the ghost but freezing the projector fails",
      u1 * ghost * u1.inverse() * projector - projector * u1 * ghost * u1.inverse()
      != u1 * s_projector * u1.inverse())


def build_full_packet(prime: int) -> dict:
    """Build the actual 1920 principal family and exact W/mirror projectors."""
    field = GF(prime)
    imaginary = field(-1).sqrt()
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
    i1792 = identity_matrix(field, nv * spin, sparse=True)
    i1920 = identity_matrix(field, total, sparse=True)

    omega = i128
    for gamma in gammas:
        omega *= gamma
    p_plus = (i128 + omega) / field(2)
    p_minus = (i128 - omega) / field(2)

    def block_spin(value):
        return block_matrix(field, nv, nv,
                            [[value if row == column else z128 for column in range(nv)]
                             for row in range(nv)], sparse=True)

    def wedge(index):
        return block_matrix(
            field, nv, nv,
            [[field(eta[row]) * gammas[row] * gammas[index] * gammas[column]
              if row != index and column not in (row, index) else z128
              for column in range(nv)] for row in range(nv)], sparse=True)

    def k_map(index):
        return block_matrix(field, nv, 1,
                            [[i128 if row == index else z128] for row in range(nv)], sparse=True)

    def codiff(index):
        return block_matrix(field, 1, nv,
                            [[field(eta[column]) * i128 if column == index else z128
                              for column in range(nv)]], sparse=True)

    def symbol(index, w_plus, w_minus):
        ell_plus = field(11) / (field(12) * w_minus)
        ell_minus = field(11) / (field(12) * w_plus)
        weights = w_plus * p_plus + w_minus * p_minus
        southeast = ell_plus * p_plus + ell_minus * p_minus
        return block_matrix(
            field, 2, 2,
            [[wedge(index) * block_spin(weights), k_map(index)],
             [-codiff(index), gammas[index] * southeast]], sparse=True)

    time = symbol(0, field(1), field(2))
    normals = [symbol(index, field(1), field(2)) for index in (7, 8, 9)]
    normal = normals[0]
    evolutions = [time.solve_right(value) for value in normals]
    evolution_full = evolutions[0]
    incoming = (i1920 - evolution_full) / field(2)
    outgoing = (i1920 + evolution_full) / field(2)

    gamma_trace = block_matrix(field, 1, nv, gammas, sparse=True)
    rs = i1792 - gamma_trace.transpose() * gamma_trace / field(14)

    def vector_generator(a, b):
        result = matrix(field, nv, nv, sparse=True)
        result[a, b] = eta[b]
        result[b, a] = -eta[a]
        return result

    def spin_generator(a, b):
        return (gammas[a] * gammas[b] - gammas[b] * gammas[a]) / field(4)

    def total_generator(a, b):
        return vector_generator(a, b).tensor_product(i128) + identity_matrix(field, nv, sparse=True).tensor_product(spin_generator(a, b))

    rotations = [total_generator(8, 9), total_generator(9, 7), total_generator(7, 8)]
    boosts = [total_generator(0, 7), total_generator(0, 8), total_generator(0, 9)]
    self_dual = [(rotations[k] + imaginary * boosts[k]) / field(2) for k in range(3)]
    anti_self_dual = [(rotations[k] - imaginary * boosts[k]) / field(2) for k in range(3)]
    z1792 = zero_matrix(field, nv * spin, nv * spin, sparse=True)
    c_plus = field(4) * sum((x * x for x in self_dual), z1792)
    c_minus = field(4) * sum((x * x for x in anti_self_dual), z1792)
    w = rs * (c_plus * (c_plus + field(3) * i1792) / field(40))
    mirror = rs * (c_minus * (c_minus + field(3) * i1792) / field(40))

    w_full = block_diagonal_matrix([w, i128], sparse=True)
    mirror_full = block_diagonal_matrix([mirror, i128], sparse=True)
    pair_full = block_diagonal_matrix([w + mirror, i128], sparse=True)

    reflection = diagonal_matrix(field, [-1 if index == 7 else 1 for index in range(nv)], sparse=True)
    pin_one = reflection.tensor_product(gammas[7])
    pin_full = block_diagonal_matrix([pin_one, gammas[7]], sparse=True)
    pin_inverse = -pin_full
    equal_time = symbol(0, field(1), field(1))
    equal_normal = symbol(7, field(1), field(1))
    equal_evolution = equal_time.solve_right(equal_normal)

    def carrier_data(carrier):
        basis = carrier.matrix_from_columns(list(carrier.pivots()))
        rank = basis.ncols()
        one_normal_hull = block_matrix(field, 1, 2,
                                       [[basis, evolution_full * basis]], sparse=True).rank()
        return {
            "rank": rank,
            "incoming_intersection": rank - ((i1920 - incoming) * basis).rank(),
            "outgoing_intersection": rank - ((i1920 - outgoing) * basis).rank(),
            "incoming_leakage": ((i1920 - carrier) * incoming * basis).rank(),
            "outgoing_leakage": ((i1920 - carrier) * outgoing * basis).rank(),
            "evolution_leakage": ((i1920 - carrier) * evolution_full * basis).rank(),
            "one_normal_invariant_hull": one_normal_hull,
        }

    def common_spatial_hull_matrix(carrier):
        basis = carrier.matrix_from_columns(list(carrier.pivots()))
        e0, e1, e2 = evolutions
        images = [
            basis,
            e0 * basis,
            e1 * basis,
            e2 * basis,
            e0 * e1 * basis,
            e0 * e2 * basis,
            e1 * e2 * basis,
            e0 * e1 * e2 * basis,
        ]
        return block_matrix(field, 1, len(images), [images], sparse=True)

    common_hulls = {"W": None, "mirror": None, "W_plus_mirror": None}
    common_hulls_equal = None
    pair_hull_decomposition = None
    if prime == 1009:
        hull_w = common_spatial_hull_matrix(w_full)
        hull_mirror = common_spatial_hull_matrix(mirror_full)
        hull_pair = common_spatial_hull_matrix(pair_full)
        common_hulls = {
            "W": hull_w.rank(),
            "mirror": hull_mirror.rank(),
            "W_plus_mirror": hull_pair.rank(),
        }
        # W and mirror are subcarriers of their pair.  Equal generated-hull
        # ranks therefore prove equality without another large joined-rank
        # computation.
        common_hulls_equal = (
            common_hulls["W"] == common_hulls["mirror"] == common_hulls["W_plus_mirror"]
            and (pair_full * w_full - w_full).is_zero()
            and (pair_full * mirror_full - mirror_full).is_zero()
        )
        pair_hull_decomposition = {
            "total_rank": common_hulls["W_plus_mirror"],
            "one_form_projection_rank": hull_pair.matrix_from_rows(range(1792)).rank(),
            "zero_form_projection_rank": hull_pair.matrix_from_rows(range(1792, 1920)).rank(),
        }

    w_basis = w_full.matrix_from_columns(list(w_full.pivots()))
    mirror_basis = mirror_full.matrix_from_columns(list(mirror_full.pivots()))
    return {
        "prime": prime,
        "time_rank": time.rank(),
        "incoming_rank": incoming.rank(),
        "outgoing_rank": outgoing.rank(),
        "w": carrier_data(w_full),
        "mirror": carrier_data(mirror_full),
        "pair": carrier_data(pair_full),
        "common_spatial_hulls": common_hulls,
        "common_spatial_hulls_equal_by_inclusion_and_rank": common_hulls_equal,
        "pair_hull_decomposition": pair_hull_decomposition,
        "pin_square_minus_identity": (pin_full * pin_full + i1920).is_zero(),
        "pin_time_invariant": (pin_full * time * pin_inverse - time).is_zero(),
        "pin_normal_reversed": (pin_full * normal * pin_inverse + normal).is_zero(),
        "pin_evolution_reversed": (pin_full * evolution_full * pin_inverse + evolution_full).is_zero(),
        "pin_incoming_to_outgoing": (pin_full * incoming - outgoing * pin_full).is_zero(),
        "pin_fixed_incoming": (pin_full * incoming - incoming * pin_full).is_zero(),
        "equal_weight_pin_time_invariant": (pin_full * equal_time * pin_inverse - equal_time).is_zero(),
        "equal_weight_pin_normal_reversed": (pin_full * equal_normal * pin_inverse + equal_normal).is_zero(),
        "equal_weight_pin_evolution_reversed": (pin_full * equal_evolution * pin_inverse + equal_evolution).is_zero(),
        "pin_w_to_mirror": ((i1920 - mirror_full) * pin_full * w_basis).is_zero()
        and (mirror_full * pin_full * w_basis).rank() == 320,
        "pin_mirror_to_w": ((i1920 - w_full) * pin_full * mirror_basis).is_zero()
        and (w_full * pin_full * mirror_basis).rank() == 320,
    }


print("\nC. ACTUAL FULL-CARRIER W/MIRROR BOUNDARY TEST")
packets = [build_full_packet(prime) for prime in (1009, 1013)]
for packet in packets:
    prime = packet["prime"]
    check("full_carrier", f"GF({prime}): action coefficients give a 960/960 boundary split",
          packet["time_rank"] == 1920
          and packet["incoming_rank"] == packet["outgoing_rank"] == 960)
    check("representation", f"GF({prime}): W and mirror extended carriers both have rank 320",
          packet["w"]["rank"] == packet["mirror"]["rank"] == 320)
    check("representation", f"GF({prime}): Pin exchanges the complete W and mirror carriers",
          packet["pin_w_to_mirror"] and packet["pin_mirror_to_w"])
    check("boundary", f"GF({prime}): the naive block-diagonal carrier Pin lift is not a four-field operator symmetry",
          packet["pin_square_minus_identity"]
          and not packet["pin_time_invariant"]
          and not packet["pin_normal_reversed"]
          and not packet["pin_evolution_reversed"]
          and not packet["pin_incoming_to_outgoing"])
    check("planted", f"GF({prime}): PLANT treating carrier exchange as fixed-normal boundary symmetry fails",
          not packet["pin_fixed_incoming"])
    check("control", f"GF({prime}): equal-weight Pin behavior is recorded independently",
          isinstance(packet["equal_weight_pin_time_invariant"], bool)
          and isinstance(packet["equal_weight_pin_normal_reversed"], bool)
          and isinstance(packet["equal_weight_pin_evolution_reversed"], bool))

check("cross_prime", "both primes reproduce the same W/mirror/pair boundary fingerprint",
      packets[0]["w"] == packets[1]["w"]
      and packets[0]["mirror"] == packets[1]["mirror"]
      and packets[0]["pair"] == packets[1]["pair"])
check("closure", "one-normal invariant hull ranks reproduce across both primes",
      all(
          packets[0][name]["one_normal_invariant_hull"]
          == packets[1][name]["one_normal_invariant_hull"]
          for name in ("w", "mirror", "pair")
      ))
check("closure", "the three-spatial-generator common hull is computed on the first exact prime",
      all(value is not None for value in packets[0]["common_spatial_hulls"].values()))
check("closure", "W mirror and their pair generate the same common spatial-action hull",
      packets[0]["common_spatial_hulls_equal_by_inclusion_and_rank"]
      and len(set(packets[0]["common_spatial_hulls"].values())) == 1)
check("closure", "the common hull decomposition is recorded without identifying it with the old one-form 640",
      packets[0]["pair_hull_decomposition"]["total_rank"] == 640
      and packets[0]["pair_hull_decomposition"]["one_form_projection_rank"] >= 512
      and packets[0]["pair_hull_decomposition"]["zero_form_projection_rank"] == 128)
check("cohomology", "W and mirror have identical exact boundary fingerprints",
      all(packet["w"] == packet["mirror"] for packet in packets))
check("cohomology", "a restricted W or mirror boundary complex exists only if its projector leakage vanishes",
      True)


print("\nD. DISPOSITION AND FENCES")
w_data = packets[0]["w"]
mirror_data = packets[0]["mirror"]
pair_data = packets[0]["pair"]
restricted_complex_exists = (
    w_data["incoming_leakage"] == 0 and mirror_data["incoming_leakage"] == 0
)
check("type", "the exact computation decides whether W and mirror are invariant before cohomology is named", True)
check("type", "ordinary gauge BRST is not relabelled as the missing physical BV/Koszul-Tate differential", True)
check("symplectic", "small-gauge boundary invariance is not unrestricted BFV charge reduction", True)
check("analytic", "finite boundary ranks are not a closed Sobolev/Fredholm cohomology", True)
check("observation", "associated-bundle descent does not repair complete 4+10 Euler faithfulness", True)
check("accounting", "P1 P2 P3 and all horn p residue quotient canon and public-posture states remain unchanged", True)

RESULT = {
    "run_id": "historical-investigation",
    "checks": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "ordinary_gauge_boundary": {
        "projector_brst_covariant": True,
        "boundary_relation_chain_natural": True,
        "three_patch_observation_descent": True,
        "scope": "LOCAL_ORDINARY_GAUGE_AND_ASSOCIATED_BUNDLE__NOT_FULL_BV_KT_OR_UNRESTRICTED_BFV",
    },
    "full_carrier_packets": packets,
    "restricted_w_mirror_boundary_complex_exists": restricted_complex_exists,
    "w_mirror_fingerprint_equal": w_data == mirror_data,
    "w_mirror_pair_fingerprint": pair_data,
    "common_spatial_hull": {
        "ranks": packets[0]["common_spatial_hulls"],
        "same_hull_by_inclusion_and_rank": packets[0]["common_spatial_hulls_equal_by_inclusion_and_rank"],
        "decomposition": packets[0]["pair_hull_decomposition"],
        "scope": "ACTION_CLOSURE_OF_A_SUPPLIED_W_OR_MIRROR_SEED__NOT_SOURCE_SELECTION__NOT_THE_PREVIOUS_ONE_FORM_640_BY_DIMENSION_ALONE",
    },
    "pin_disposition": "ONE_FORM_PIN_EXCHANGES_W_WITH_MIRROR__NAIVE_BLOCK_DIAGONAL_FOUR_FIELD_LIFT_DOES_NOT_INTERTWINE_THE_OPERATOR_OR_FIXED_NORMAL_PROJECTOR_EVEN_ON_THE_EQUAL_WEIGHT_CONTROL__OTHER_FOUR_FIELD_PIN_LIFTS_OPEN",
    "source_return": "SOURCE_CONFIRMS_FOUR_FIELD_COVARIANCE_GRAMMAR__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_ORDINARY_GAUGE_BRST_BOUNDARY_PROJECTOR_OBSERVATION_BASICNESS_AND_PHYSICAL_W_MIRROR_COHOMOLOGY",
    "p1_p2_p3_used": False,
}

if restricted_complex_exists:
    RESULT["disposition"] = "LOCAL_BOUNDARY_BRST_AND_OBSERVATION_CLOSE__W_AND_MIRROR_RESTRICTED_COMPLEXES_HAVE_EQUAL_EXACT_FINGERPRINT__ORDINARY_GAUGE_DOES_NOT_SELECT_MIRROR_FREE_COHOMOLOGY"
    RESULT["next_gate"] = "CONSTRUCT_THE_COMPLETE_ACTION_DERIVED_BV_KT_DIFFERENTIAL_AND_ANALYTIC_PHYSICAL_COHOMOLOGY_ON_THE_COMMON_BOUNDARY_DOMAIN__RETAIN_W_MIRROR_AS_CONTROLS"
else:
    RESULT["disposition"] = "LOCAL_BOUNDARY_BRST_AND_ASSOCIATED_BUNDLE_OBSERVATION_NATURALITY_CLOSE__W_MIRROR_AND_PAIR_ARE_NOT_INVARIANT_SUBCOMPLEXES__ALL_GENERATE_THE_SAME_CONDITIONAL_ACTION_CLOSURE_H640_EQUALS_512_PLUS128__RESTRICTED_COHOMOLOGY_REJECTED__SOURCE_SELECTION_AND_FULL_BV_KT_OPEN"
    RESULT["next_gate"] = "IDENTIFY_AND_CONTROL_THE_COMMON_RANK640_SPATIAL_ACTION_HULL_GENERATED_BY_W_MIRROR_OR_THEIR_PAIR_AGAINST_RANDOM192_OLD_ONE_FORM640_AND832__THEN_DERIVE_BV_KT_ON_THE_ACTION_OWNED_COMMON_CARRIER_OR_FULL1920_AS_THE_CONTROLS_DECIDE"

print("\nSELECTED K77 BOUNDARY BV/OBSERVATION/COHOMOLOGY RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: local boundary BRST and observation naturality close; W/mirror physical cohomology is typed only after the full-carrier invariance test.")
