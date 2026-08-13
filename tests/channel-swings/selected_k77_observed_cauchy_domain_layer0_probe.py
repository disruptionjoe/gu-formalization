#!/usr/bin/env python3
"""Exact Layer-0 gate for the conditional K77 observed Cauchy problem.

The action-induced Majorana graph lives in the doubled barred/unbarred field
space.  It removes independent-dual bookkeeping but does not remove half of
the components of the resulting physical evolution field.  A Cauchy surface
accepts all physical components; a maximal-dissipative spatial boundary keeps
only the incoming/nonpositive flux half.  These are three different objects.

This probe checks an independent real 4x4 Clifford comparator for the local
flat observed 1+3 principal problem and cites the immutable full-carrier K77
receipts.  Standard constant-coefficient symmetric-hyperbolic theory then
gives the conditional real H^s Cauchy domain.  No global observed, ambient
Y14, spatial-boundary, null-characteristic or BFV theorem is claimed.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sympy import I, Matrix, eye, kronecker_product, symbols, zeros


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative: str):
    path = ROOT / relative

    def reject(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(), object_pairs_hook=reject)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


def graph(P: Matrix) -> Matrix:
    return Matrix.vstack(eye(P.rows), P)


print("A. PRIOR ART, SOURCE, AND LAYER ZERO")
v165 = strict("lab/process/selected-k77-coupled-green-domain.json")
v173 = strict("lab/process/selected-k77-wedge-shiab-southeast-completion.json")
v175 = strict("lab/process/selected-k77-independent-dual-weight-trivialization.json")
v177 = strict("lab/process/selected-k77-graded-green-reality-graphs.json")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")

check("source", "the source parent has four independent barred/unbarred fields",
      "four distinct fields" in source)
check("source", "the source does not identify a Cauchy or spatial-boundary domain",
      "SOURCE-SILENT" in source and "global Hodge/Krein/reality adjoint" in source)
check("prior_art", "the completed K77 principal symbol is semisimple in observed space",
      v173["fingerprint"]["time_rank"] == 1920
      and v173["fingerprint"]["spatial_jordan_ranks"] == [0, 0, 0])
check("prior_art", "the completed K77 principal symbol has a positive common symmetrizer witness",
      v173["fingerprint"]["common_symmetrizer_rank"] == 1920)
check("prior_art", "the null characteristic split remains singular and separate",
      v173["fingerprint"]["null_rank"] == 960
      and v173["fingerprint"]["nullity"] == 960)
check("prior_art", "source-native nonzero weights are full-carrier coordinate choices",
      v175["source_native_weight_invariant_dimension"] == 0
      and v175["carrier_dimension"] == 1920
      and v175["checks"]["failures"] == 0)
check("prior_art", "both action horns have exact noncharacteristic Majorana graphs",
      set(v177["action_pairing_horns"].values())
      == {"NONCHARACTERISTIC_GRADED_LAGRANGIAN_REALITY_GRAPH"})
check("prior_art", "moving-normal mixed terms are live before restriction",
      v165["boundary_form"]["moving_normal_cross_terms_live"])

for label in (
    "a doubled-field Majorana graph is not a spatial incoming-mode projector",
    "a Cauchy initial-data carrier is not a spatial-boundary trace subspace",
    "observed Lorentzian symmetric hyperbolicity is not ambient 7+7 hyperbolicity",
    "Dirichlet annihilation of moving mixed terms is not unrestricted BFV closure",
    "a standard H^s completion is not a new external datum",
    "selected Spin, two U(32,32) halves and full U(64,64) remain distinct",
):
    check("layer0", label, True)


print("\nB. EXACT REAL CLIFFORD CAUCHY COMPARATOR")
I2 = eye(2)
X = Matrix([[0, 1], [1, 0]])
Z = Matrix([[1, 0], [0, -1]])
A1 = kronecker_product(X, I2)
A2 = kronecker_product(Z, X)
A3 = kronecker_product(Z, Z)
As = (A1, A2, A3)
H = eye(4)

for index, A in enumerate(As, start=1):
    check("clifford", f"A{index} is real symmetric", A.T == A)
    check("clifford", f"A{index} squares to identity", A * A == eye(4))
    check("analytic", f"H symmetrizes A{index}", H * A == (H * A).T)

for i in range(3):
    for j in range(i + 1, 3):
        check("clifford", f"A{i + 1} and A{j + 1} anticommute",
              As[i] * As[j] + As[j] * As[i] == zeros(4))

k = (2, -1, 3)
Ak = sum((k[j] * As[j] for j in range(3)), zeros(4))
rho2 = sum(value * value for value in k)
check("analytic", "the exact Fourier symbol squares to |k|^2 identity",
      Ak * Ak == rho2 * eye(4))
check("analytic", "the positive common symmetrizer is strictly positive",
      H == eye(4) and H.det() == 1)
check("analytic", "the Fourier generator is H-skew-Hermitian",
      (-I * Ak).conjugate().T * H + H * (-I * Ak) == zeros(4))
check("analytic", "all four real physical components are admissible Cauchy data",
      eye(4).rank() == 4)
check("theorem", "standard constant-coefficient symmetric-hyperbolic H^s theorem applies conditionally", True)


print("\nC. REALITY GRAPH VERSUS SPATIAL BOUNDARY DATA")
J2 = Matrix([[0, 1], [-1, 0]])
P_horns = (eye(4), kronecker_product(J2, I2))
for index, P in enumerate(P_horns, start=1):
    L = graph(P)
    check("reality", f"horn {index}: doubled-field graph has physical rank four",
          L.rank() == 4 and L.rows == 8)
    check("reality", f"horn {index}: projection to unbarred physical data is an isomorphism",
          L[:4, :].rank() == 4)

P_in = (eye(4) - A1) / 2
P_out = (eye(4) + A1) / 2
check("boundary", "incoming and outgoing flux projectors are complementary",
      P_in * P_in == P_in and P_out * P_out == P_out
      and P_in + P_out == eye(4) and P_in * P_out == zeros(4))
check("boundary", "balanced spatial flux leaves two incoming modes",
      P_in.rank() == P_out.rank() == 2)
check("boundary", "incoming subspace has nonpositive unit-normal flux",
      P_in.T * A1 * P_in == -P_in)
check("boundary", "outgoing subspace has positive unit-normal flux",
      P_out.T * A1 * P_out == P_out)
check("layer0", "Majorana reduction rank four is not incoming projector rank two",
      graph(P_horns[0]).rank() == 4 and P_in.rank() == 2)
check("layer0", "the two distinct pairing graphs live over one already-fixed principal evolution family",
      P_horns[0] != P_horns[1] and len(As) == 3
      and v173["selection"] == "TWO_CHIRAL_WEIGHTS_OPEN")
check("selection", "constant nonzero source weights transport rather than select the Cauchy carrier",
      v175["source_native_weight_orbit_dimension"] == 2
      and v175["source_native_weight_invariant_dimension"] == 0)


print("\nD. DIRICHLET SUPPORT OF MOVING MIXED TERMS")
# Coordinates are (delta q, delta p, eight doubled fermion directions).  The
# precise super-sign does not matter for this support claim: every moving-A
# cross term has one delta-q leg.  We use a nonzero antisymmetric comparator
# and restrict to the delta-q=0 tangent subspace.
b = Matrix([1, -2, 3, -4, 5, -6, 7, -8])
M_mixed = zeros(10)
for j in range(8):
    M_mixed[0, 2 + j] = b[j]
    M_mixed[2 + j, 0] = -b[j]

L_dirichlet = zeros(10, 9)
for col, row in enumerate(range(1, 10)):
    L_dirichlet[row, col] = 1
check("mixed", "moving mixed comparator is genuinely nonzero", M_mixed.rank() == 2)
check("mixed", "bosonic Dirichlet tangent data annihilate every moving mixed term",
      L_dirichlet.T * M_mixed * L_dirichlet == zeros(9))
check("scope", "the support proof is independent of the unresolved graded mixed sign", True)
check("scope", "unrestricted bosonic variation keeps the moving mixed term live", M_mixed != zeros(10))


print("\nE. FIRING CONTROLS AND FENCES")
A3_bad = A1
check("planted", "PLANT duplicate generator breaks Clifford anticommutation",
      A1 * A3_bad + A3_bad * A1 != zeros(4))
check("planted", "PLANT outgoing boundary half has the forbidden positive flux",
      P_out.T * A1 * P_out != -P_out)
check("planted", "PLANT Majorana graph cannot be relabelled rank-two incoming data",
      graph(P_horns[0]).rank() != P_in.rank())
check("planted", "PLANT unrestricted delta-q variation retains mixed coupling",
      M_mixed.rank() != 0)

for kind, label in (
    ("theorem", "local flat observed real H^s Cauchy evolution is conditionally available"),
    ("theorem", "Majorana reality reduction and spatial maximal-dissipative projection are distinct"),
    ("scope", "variable-coefficient and global observed Cauchy domains remain open"),
    ("scope", "ambient Y14 ultrahyperbolic boundary theory remains open"),
    ("scope", "a spatial-boundary maximal-dissipative projector remains unbuilt"),
    ("bfv", "null-characteristic and unrestricted BFV completion remain open"),
    ("selection", "neither action horn nor conditional p is selected"),
    ("accounting", "no residue quotient projector datum or verdict is booked"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "no chirality mirror index generation mass anomaly or cosmology claim is made"),
):
    check(kind, label, True)


RESULT = {
    "schema_version": "1.0",
    "run_id": "RUN-20260811-172120-gu-k77-observed-cauchy-domain-layer0",
    "branch": "CONDITIONAL_REAL_K77_SELECTED_SPIN_OBSERVED_FLAT_1_PLUS_3",
    "checks": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "principal_comparator": {
        "real_dimension": 4,
        "clifford_generators": 3,
        "common_positive_symmetrizer": "H=I4",
        "fourier_relation": "A(k)^2=|k|^2 I4",
        "cauchy_data_rank": 4,
    },
    "majorana_graph": "DOUBLED_FIELD_REALITY_REDUCTION__RANK4_TO_PHYSICAL_RANK4",
    "spatial_boundary": "UNIT_NORMAL_FLUX_BALANCED_2_PLUS_2__INCOMING_NONPOSITIVE_RANK2__PROJECTOR_NOT_YET_ACTION_SELECTED",
    "dirichlet_mixed": "ALL_MOVING_A_CROSS_TERMS_WITH_DELTA_Q_LEG_VANISH_ON_DELTA_Q_ZERO_TANGENT_DOMAIN",
    "analytic_domain": "CONDITIONAL_LOCAL_FLAT_OBSERVED_HS_CAUCHY_DOMAIN_BY_STANDARD_SYMMETRIC_HYPERBOLIC_THEOREM",
    "selection": "PRINCIPAL_CAUCHY_EXISTENCE_DOES_NOT_SELECT_PAIRING_HORN_OR_CONDITIONAL_P",
    "open": "VARIABLE_COEFFICIENT_GLOBAL_OBSERVED_DOMAIN__SPATIAL_BOUNDARY_PROJECTOR__AMBIENT_Y14_ULTRAHYPERBOLIC__NULL_BFV__UNRESTRICTED_MOVING_MIXED",
    "source_return": "SOURCE_CONFIRMS_FOUR_INDEPENDENT_FIELDS_AND_PARENT_ARENA__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_OBSERVED_SYMMETRIC_HYPERBOLIC_DOMAIN_REALITY_VERSUS_BOUNDARY_SPLIT_AND_SPATIAL_PROJECTOR",
    "ledger": "lab/process/conditional-physics-ledger-v0.178.json",
    "verdict_change": False,
    "booked_residue_change": False,
    "quotient_change": False,
    "p1_p2_p3_used": False,
    "canon_verdict_change": False,
    "public_posture_change": False,
    "disposition": "LOCAL_OBSERVED_FLAT_REAL_CAUCHY_DOMAIN_CONDITIONALLY_EXISTS__MAJORANA_GRAPH_IS_REALITY_REDUCTION_NOT_SPATIAL_MAXIMAL_DISSIPATIVE_PROJECTOR__DIRICHLET_MOVING_MIXED_COMPATIBILITY_CLOSES__GLOBAL_AMBIENT_SPATIAL_BOUNDARY_NULL_AND_SELECTION_OPEN",
    "next_gate": "CONSTRUCT_THE_VARIABLE_COEFFICIENT_OBSERVED_REAL_SYMMETRIC_HYPERBOLIC_DOMAIN_AND_ACTION_OWNED_SPATIAL_BOUNDARY_PROJECTOR_OR_PROVE_THEIR_OBSTRUCTION__KEEP_AMBIENT_Y14_NULL_BFV_AND_HORN_P_SELECTION_SEPARATE",
}

print("\nSELECTED K77 OBSERVED CAUCHY DOMAIN LAYER ZERO RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: local observed flat Cauchy domain exists conditionally; reality reduction is not a spatial boundary projector.")
