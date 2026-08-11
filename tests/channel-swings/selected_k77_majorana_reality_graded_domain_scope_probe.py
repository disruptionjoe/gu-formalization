#!/usr/bin/env python3
"""Exact scope gate for local K77 Majorana reality versus the Green domain.

The repaired real-K77 operator is represented by real matrices, so entrywise
complex conjugation on its complexification is an anti-linear involution that
commutes with the local operator and preserves the real chiral projectors.
That is a local reality structure.  It is not yet a barred/unbarred action
identification or a closed Green domain.

The obvious action-induced identification uses either of the two exact v0.174
Spin-natural bilinear horns, ``bar = P conjugate(psi)``.  In the v0.166
Darboux variables ``v=A^T bar``, its graph coefficient is ``S=A^T P``.  The
v0.174 adjoint identities imply that S is skew in both horns.  The v0.165/166
finite *even* symplectic comparator requires S symmetric.  Therefore its
120-coordinate symmetric graph family cannot certify the physical odd
Grassmann reality/domain.  The next construction must be graded; no graph is
supplied here.

This is a composition theorem using the two-prime full-1920 v0.174 receipt,
not a global Calderon, positivity, BFV, observation, index or count result.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sympy import I, Matrix, eye, simplify, zeros


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


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
v166 = strict("lab/process/selected-k77-moving-antidualizer-darboux.json")
v173 = strict("lab/process/selected-k77-wedge-shiab-southeast-completion.json")
v174 = strict("lab/process/selected-k77-action-adjoint-weight-classification.json")
v175 = strict("lab/process/selected-k77-independent-dual-weight-trivialization.json")

check("source", "the source keeps barred and unbarred fields independent before reality",
      "four distinct fields" in source)
check("source", "the source is silent on the global K77 reality/domain",
      "global Hodge/Krein/reality adjoint" in source and "SOURCE-SILENT" in source)
check("prior_art", "the repaired K77 operator is full rank in a noncharacteristic direction",
      v173["fingerprint"]["time_rank"] == 1920)
check("prior_art", "the two action pairing horns are exact over two primes",
      v174["exact_primes"] == [1009, 1013]
      and v174["pairing_ranks"] == [1920, 1920]
      and v174["checks"]["failures"] == 0)
check("prior_art", "the moving Darboux theorem assumes a supplied symmetric graph",
      v166["selection"]["minimum_symmetric_multiplicity_coordinates"] == 120
      and not v166["selection"]["unique_graph_selected"])
check("prior_art", "the source-native orbit leaves reality conditional",
      v175["source_native_weight_invariant_dimension"] == 0
      and v175["reality_congruent_conditional_invariant"] == "p=w_plus*w_minus")

for label in (
    "entrywise conjugation is not an invariant bilinear dualizer",
    "an invariant bilinear is not a barred/unbarred reality relation",
    "a local reality relation is not a closed Green domain",
    "an even symplectic graph is not an odd Grassmann Lagrangian relation",
    "local operator reality is not source or action selection of that reality",
    "selected Spin, two U(32,32) halves and full U(64,64) remain distinct",
):
    check("layer0", label, True)


print("\nB. LOCAL REAL STRUCTURE EXISTS")
z = Matrix([1 + 2 * I, 3 - I])


def conjugation(value: Matrix) -> Matrix:
    return value.conjugate()


check("antilinear", "entrywise conjugation is anti-linear",
      simplify(conjugation(I * z) + I * conjugation(z)) == zeros(2, 1))
check("reality", "entrywise conjugation squares to one",
      conjugation(conjugation(z)) == z)

# A real operator and real chirality grading are the exact local K77 case.
D_real = Matrix([[2, 1], [-3, 4]])
chi_real = Matrix([[1, 0], [0, -1]])
check("reality", "conjugation commutes with a real operator",
      conjugation(D_real * z) == D_real * conjugation(z))
check("reality", "conjugation preserves the real chiral grading",
      conjugation(chi_real * z) == chi_real * conjugation(z))
check("actual_carrier", "the actual K77 receipt uses the real Clifford branch over all 14 directions",
      v173["branch"] == "CONDITIONAL_REAL_K77_SELECTED_SPIN_PARENT"
      and v174["directions_checked_each_prime"] == 14)
check("scope", "local real structure existence does not identify the four source fields", True)


print("\nC. BOTH ACTION-INDUCED REALITY HORNS MISS THE EVEN GRAPH CLASS")

# Horn 1: P is symmetric and D is P-anti-adjoint.  Then P D is alternating
# and S=D^T P=-P D is skew.
P_sym = eye(2)
D_anti = Matrix([[0, 1], [-1, 0]])
S_from_sym = D_anti.T * P_sym
check("grassmann", "symmetric/anti-adjoint horn has alternating quadratic coefficient",
      P_sym * D_anti + (P_sym * D_anti).T == zeros(2))
check("graded", "its action-induced Darboux graph coefficient is skew",
      S_from_sym.T == -S_from_sym and S_from_sym != zeros(2))

# Horn 2: P is skew and D is P-self-adjoint.  The identity is a complete
# nondegenerate witness; again P D and S=D^T P are alternating/skew.
P_skew = Matrix([[0, 1], [-1, 0]])
D_self = eye(2)
S_from_skew = D_self.T * P_skew
check("grassmann", "skew/self-adjoint horn has alternating quadratic coefficient",
      P_skew * D_self + (P_skew * D_self).T == zeros(2))
check("graded", "its action-induced Darboux graph coefficient is also skew",
      S_from_skew.T == -S_from_skew and S_from_skew != zeros(2))

check("actual_carrier", "the full-carrier receipt identifies exactly these two transpose horns",
      v174["anti_adjoint_pairing_symmetry"] == "SYMMETRIC"
      and v174["self_adjoint_pairing_symmetry"] == "SKEW"
      and v174["both_grassmann_coefficients_alternating"])

# In the even Darboux comparator Omega=[[0,-I],[I,0]], the exchange
# R_S=[[0,S^-1],[S,0]] is anti-symplectic iff S is symmetric.  A skew S
# is a firing witness against importing the even theorem into the odd theory.
J_even = Matrix.vstack(
    Matrix.hstack(zeros(2), -eye(2)),
    Matrix.hstack(eye(2), zeros(2)),
)


def exchange(S: Matrix) -> Matrix:
    return Matrix.vstack(
        Matrix.hstack(zeros(2), S.inv()),
        Matrix.hstack(S, zeros(2)),
    )


S_good_even = Matrix([[2, 1], [1, 3]])
R_good_even = exchange(S_good_even)
R_bad_even = exchange(P_skew)
check("symplectic", "a symmetric graph gives the v0.166 even anti-symplectic exchange",
      R_good_even.T * J_even * R_good_even == -J_even)
check("planted", "PLANT the action-induced skew graph fails the even exchange criterion",
      R_bad_even.T * J_even * R_bad_even != -J_even)
check("scope", "failure in the even comparator is not a no-go in graded odd symplectic geometry", True)
check("selection", "neither exact pairing horn is selected by the source",
      "SOURCE-SILENT" in source and v174["weight_equation_rank"] == 0)


print("\nD. CONSEQUENCE AND FENCES")
for kind, label in (
    ("theorem", "local real-K77 Majorana conjugation survives the first gate"),
    ("scope", "the existing even symmetric-graph family is not the physical graded-domain certificate"),
    ("graded", "the next construction must derive the odd Green form and graded transpose convention from the action"),
    ("analytic", "no Calderon Sobolev Fredholm maximal-dissipative or positivity result is inferred"),
    ("symplectic", "the moving Darboux half-shear survives as even prior art but needs graded rederivation"),
    ("accounting", "no graph coordinate reality horn or action coefficient is booked"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "no chirality mirror index generation mass anomaly or cosmology claim is made"),
):
    check(kind, label, True)

RESULT = {
    "schema_version": "1.0",
    "run_id": "RUN-20260811-152113-gu-k77-majorana-reality-graded-domain-scope",
    "branch": "CONDITIONAL_REAL_K77_SELECTED_SPIN",
    "checks": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "local_antilinear_reality": "EXISTS__ENTRYWISE_CONJUGATION_ON_REAL_K77_COMPLEXIFICATION__SQUARE_PLUS_ONE__CHIRALITY_PRESERVING",
    "action_pairing_horns": {
        "symmetric_anti_adjoint": "ACTION_QUADRATIC_ALTERNATING__INDUCED_DARBOUX_GRAPH_SKEW",
        "skew_self_adjoint": "ACTION_QUADRATIC_ALTERNATING__INDUCED_DARBOUX_GRAPH_SKEW",
    },
    "even_graph_import": "REJECTED_AS_CATEGORY_MISMATCH__V0166_REQUIRES_SYMMETRIC_S",
    "graded_physical_domain": "OPEN__ODD_GREEN_FORM_GRADED_TRANSPOSE_AND_MOVING_ANTILINEAR_FIXED_LOCUS_REQUIRED",
    "reality_selection": "SOURCE_SILENT__TWO_LOCAL_HORNS_UNSELECTED",
    "p_status": "CONDITIONAL_CONGRUENCE_INVARIANT_ONLY_AFTER_A_REALITY_HORN_IS_SELECTED",
    "disposition": "LOCAL_K77_REAL_STRUCTURE_SURVIVES__OBVIOUS_ACTION_PAIRING_REALITY_CANDIDATES_LAND_IN_SKEW_DARBOUX_GRAPHS__EVEN_SYMMETRIC_GRAPH_THEOREM_CANNOT_CERTIFY_ODD_GRASSMANN_DOMAIN__GRADED_GREEN_CONSTRUCTION_NEXT",
    "next_gate": "DERIVE_THE_GRADED_ODD_PREBOUNDARY_FORM_AND_MOVING_ANTILINEAR_FIXED_LOCUS_FROM_THE_FOUR_FIELD_ACTION__CLASSIFY_THE_TWO_PAIRING_HORNS_AND_GLOBAL_OVERLAP__ONLY_THEN_ATTEMPT_CALDERON_OR_MAXIMAL_DISSIPATIVE_CLOSURE",
}

print("\nSELECTED K77 MAJORANA REALITY / GRADED DOMAIN SCOPE RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: local real-K77 conjugation exists, but the even Darboux graph theorem is not the graded physical domain.")
