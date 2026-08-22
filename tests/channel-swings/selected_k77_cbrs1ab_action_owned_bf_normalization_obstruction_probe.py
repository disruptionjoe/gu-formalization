#!/usr/bin/env sage -python
"""Exact CBRS-1AB source/action owner and field-redefinition audit."""

from __future__ import annotations

from collections import Counter
import itertools
import json
from math import comb
from pathlib import Path

import sympy as sp
import yaml


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PREDECESSOR AND LAYER ZERO", flush=True)
predecessor = json.loads(read(
    "lab/process/selected-k77-cbrs1aa-covariant-odd-momentum-operator-obstruction.json"
))
check("prior", "CBRS-1AA carries its exact 57-of-57 certificate",
      predecessor["probe_result"] == "PASS_57_OF_57")
check("prior", "CBRS-1AA opens the action-owned normalization audit",
      "AUDIT_THE_CANONICAL_HODGE_DE_RHAM_BF_RAY" in predecessor["next_gate"])
check("prior", "the CBRS-1AA core replay retains both raw BF basis maps",
      predecessor["first_order_basis"] == [
          "d_B:Lambda1_TO_Lambda2", "delta_B:Lambda3_TO_Lambda2"])
check("type", "the BF ray remains a nonzero raw endpoint map",
      predecessor["bf_action"]["raw_endpoint_variation_map_nonzero"] is True)
check("type", "the audit starts from the full 378-dimensional odd carrier",
      predecessor["carriers"]["odd_auxiliary_dimension"] == 378)
selected_action = json.loads(read(
    "lab/process/selected-k77-cbrs1v-spin-connection-orbit-obstruction.json"
))
check("horn", "CBRS-1AA filed the auxiliary on Spin(9,5)",
      predecessor["carriers"]["base_space"] == "V=R(9,5)")
check("horn", "the selected K77 connection action is Spin(7,7)",
      "Spin(7,7)" in selected_action["frozen_class"]["connection"])


print("B. RELEASED SOURCE/ACTION INVENTORY", flush=True)
claims = yaml.safe_load(read("lab/sources/source-claim-register.yaml"))
claim_by_id = {row["id"]: row for row in claims["claims"]}
for claim_id in ("SC-ACT-01", "SC-ACT-02", "SC-ACT-03", "SC-ACT-04", "SC-ACT-05"):
    check("source", f"the released action register contains {claim_id}", claim_id in claim_by_id)
check("source", "SC-ACT-01 owns I1B augmented torsion",
      "augmented torsion" in claim_by_id["SC-ACT-01"]["claim"])
check("source", "SC-ACT-04 owns the I2B residual norm square",
      "I^B_2" in claim_by_id["SC-ACT-04"]["claim"] and
      "Upsilon" in claim_by_id["SC-ACT-04"]["claim"])
check("source", "SC-ACT-05 owns a total Euler residual rather than a new boson",
      "total Euler residual" in claim_by_id["SC-ACT-05"]["claim"])
scact1_notes = claim_by_id["SC-ACT-01"]["notes"]
check("source", "the printed Xi_omega is D_omega Upsilon_omega",
      "Xi = D_omega Upsilon_omega" in scact1_notes)
grammar_return = read(
    "lab/sources/selected-k77-i2b-source-action-grammar-exhaustion-source-return-2026-08-13.md"
)
check("source", "the checked grammar is silent on another zero-fermion bosonic owner",
      "SOURCE_SILENT_ADDITIONAL_ZERO_FERMION_BOSONIC_CANCELLATION_OWNER" in grammar_return)
check("source", "the grammar does not select a relative I1B/I2B coefficient",
      "relative `I1B/I2B` coefficient" in grammar_return)


print("C. EXACT EXISTING-TORSION IRREDUCIBLE HOST", flush=True)
n = 14
d2 = comb(n, 2)
d3 = comb(n, 3)
tensor_dim = n * d2
hook_dim = tensor_dim - n - d3
check("module", "the existing V tensor Lambda2 torsion carrier has dimension 1274",
      tensor_dim == 1274)
check("module", "the vector trace summand has dimension 14", n == 14)
check("module", "the total-alternation summand has dimension 364", d3 == 364)
check("module", "the Cartan hook complement has dimension 896", hook_dim == 896)

# A stored tensor column is (a,(b,c)) with b<c. The trace pivot for output c
# repeats a in the two-form pair; its alternation is zero. The alternation
# pivot for output i<j<k is (i,(j,k)); its trace is zero. The two pivot
# families are disjoint and give signed coordinate vectors in the direct-sum
# codomain, certifying full rank without a numerical rank oracle.
trace_pivots: dict[int, tuple[int, tuple[int, int]]] = {}
for c in range(n):
    a = (c + 1) % n
    trace_pivots[c] = (a, tuple(sorted((a, c))))
alt_pivots = {triple: (triple[0], (triple[1], triple[2]))
              for triple in itertools.combinations(range(n), 3)}
check("module", "there is one distinct trace pivot for every vector output",
      len(set(trace_pivots.values())) == n)
check("module", "there is one distinct alternation pivot for every three-form output",
      len(set(alt_pivots.values())) == d3)
check("module", "trace pivots have a repeated tensor index and zero alternation",
      all(a in pair for a, pair in trace_pivots.values()))
check("module", "alternation pivots have three distinct indices and zero trace",
      all(a not in pair for a, pair in alt_pivots.values()))
check("module", "the trace and alternation pivot families are disjoint",
      set(trace_pivots.values()).isdisjoint(set(alt_pivots.values())))
combined_rank = len(trace_pivots) + len(alt_pivots)
check("module", "the combined trace-plus-alternation quotient has rank 378",
      combined_rank == 378)
check("module", "its exact kernel is the 896-dimensional hook",
      tensor_dim - combined_rank == hook_dim == 896)


print("D. NOTATION AND VARIATIONAL-ROLE SEPARATION", flush=True)
registry = json.loads(read(
    "lab/process/selected-k77-cbrs1ab-action-owned-bf-normalization-obstruction.json"
))
horn = registry["signature_horn_audit"]
check("horn", "the audit preserves the two distinct real signature horns",
      horn["filed_auxiliary_horn"] == "Spin(9,5)" and
      horn["selected_action_horn"] == "Spin(7,7)")
check("horn", "no canonical real equivariant bridge is claimed",
      horn["canonical_real_equivariant_bridge"] is False)
check("horn", "complexification is not promoted to a real typed bridge",
      horn["complexification_is_real_typed_bridge"] is False)
check("horn", "the exterior decomposition is explicitly horn-robust",
      horn["abstract_exterior_dimensions_are_signature_robust"] is True)
inventory = registry["released_action_inventory"]
check("owner", "source Xi_omega is recorded as an Euler companion",
      "EULER_COMPANION" in inventory["source_xi_omega"])
check("owner", "source Xi_omega is not a configuration field",
      inventory["source_xi_omega_is_configuration_field"] is False)
check("owner", "source Xi_omega is not identified with CBRS Xi",
      inventory["source_xi_omega_equals_cbrs_auxiliary"] is False)
check("owner", "the released inventory contains no independent Wodd field",
      inventory["independent_wodd_field"] is False)
check("owner", "the released inventory contains no independent BF coefficient",
      inventory["independent_bf_coefficient"] is False)
check("owner", "only the native Spin(7,7) retyping is a component of existing T77",
      registry["torsion_decomposition"]["filed_wodd95_is_selected_T77_component"] is False and
      registry["torsion_decomposition"]["native_retyped_wodd77_is_existing_T77_component"] is True)
check("owner", "Wodd is not recorded as a second released field",
      registry["torsion_decomposition"]["wodd_is_independent_released_field"] is False)


print("E. COMPLETE FIELD-REDEFINITION CERTIFICATE", flush=True)
k_t, k_x, t, x, c = sp.symbols("k_t k_x t x c", nonzero=True)
complete = sp.expand(sp.Rational(1, 2) * k_t * (t + c * x) ** 2)
check("redefinition", "the complete shift has cross coefficient k_t*c",
      complete.coeff(t * x) == k_t * c)
check("redefinition", "the complete shift has induced coefficient k_t*c^2/2",
      complete.coeff(x ** 2) == sp.Rational(1, 2) * k_t * c ** 2)
hessian = sp.hessian(complete, (t, x))
check("redefinition", "the redundant two-field Hessian determinant is zero",
      sp.factor(hessian.det()) == 0)
check("redefinition", "the redundant two-field Hessian has rank one",
      hessian.rank() == 1)
check("redefinition", "undoing the full shift returns the original action",
      sp.expand(complete.subs(t, t - c * x) - sp.Rational(1, 2) * k_t * t ** 2) == 0)

independent = sp.expand(complete + sp.Rational(1, 2) * k_x * x ** 2)
independent_hessian = sp.hessian(independent, (t, x))
check("redefinition", "an independent Xi norm makes the Hessian determinant k_t*k_x",
      sp.factor(independent_hessian.det() - k_t * k_x) == 0)
r = sp.symbols("r", nonzero=True)
check("normalization", "c^2/k_x survives Xi field rescaling",
      sp.simplify((c / r) ** 2 / (k_x / r ** 2) - c ** 2 / k_x) == 0)
check("normalization", "kappa1 cannot name a coefficient absent from the inventory",
      inventory["existing_torsion_coefficient"] == "kappa1" and
      inventory["independent_bf_coefficient"] is False)


print("F. MULTIPLIER AND EULER-SQUARED HORNS", flush=True)
e, u = sp.symbols("e u")
pure_bf = c * e * u
check("multiplier", "the pure BF term has only a mixed algebraic Hessian",
      sp.hessian(pure_bf, (e, u)).det() != 0)
# The bilinear BF Hessian is nondegenerate for c!=0, but each Euler equation
# constrains the other field without a quadratic propagation owner. Record the
# multiplier fact through the equations, not through Hessian singularity.
check("multiplier", "pure BF variation in e imposes the Xi map",
      sp.diff(pure_bf, e) == c * u)
check("multiplier", "pure BF variation in Xi imposes the primitive map",
      sp.diff(pure_bf, u) == c * e)

q, lam = sp.symbols("q lam")
M = q ** 2 - 1
euler_squared = -sp.Rational(1, 2) * lam * M ** 2
variation = sp.diff(euler_squared, q)
check("effective", "the residual-squared variation factors through M",
      sp.factor(variation / M) == -2 * lam * q)
check("effective", "the residual-squared variation vanishes on both old-shell roots",
      variation.subs(q, 1) == 0 and variation.subs(q, -1) == 0)
check("effective", "the registry classifies source Xi_omega as the wrong variational role",
      "WRONG_VARIATIONAL_ROLE" in registry["owner_horns"]["source_Xi_omega"])
check("effective", "the registry preserves the Euler-squared ceiling",
      "VANISHING_TO_FIRST_ORDER" in registry["owner_horns"]["I2B_or_residual_square"])


print("G. PROPAGATION AND CLAIM CEILING", flush=True)
check("propagation", "the registry closes the released-action owner quotient",
      registry["verdict"]["released_action_owned_nonredundant_normalization_quotient_dimension"] == 0)
check("propagation", "the odd route has an explicit new-evidence wake",
      registry["verdict"]["odd_auxiliary_route"] ==
      "CLOSED_UNTIL_GENUINELY_NEW_SOURCE_ACTION_EVIDENCE")
check("propagation", "the sigma route retains its independent-invariant wake",
      registry["verdict"]["sigma_route"] ==
      "CLOSED_UNTIL_INDEPENDENT_PRE_DENSITY_INVARIANT")
check("propagation", "CBRS-2 remains unadmitted",
      registry["verdict"]["cbrs2_admitted"] is False)
check("propagation", "current state records the CBRS-1AB result",
      "CBRS-1AB" in read("CURRENT-STATE.yaml") and
      "owner quotient" in read("CURRENT-STATE.yaml"))
check("propagation", "the agenda records owner exhaustion rather than a synthetic successor",
      "CBRS-1AB" in read("lab/process/RESEARCH-AGENDA.json") and
      "synthetic CBRS-1AC" in read("lab/process/RESEARCH-AGENDA.json"))
check("propagation", "NEXT-STEPS carries the exact reopen conditions",
      "CBRS-1AB CLOSES" in read("NEXT-STEPS.md") and
      "independent pre-density invariant" in read("NEXT-STEPS.md"))
check("scope", "no ledger canon source-ownership or public-posture change follows",
      all(registry[key] == "none" for key in (
          "ledger_verdict_change", "source_ownership_change", "canon_verdict_change",
          "public_posture_change")))
check("scope", "the ceiling remains bounded to checked released action ownership",
      "NO_UNIVERSAL_NO_GO" in registry["claim_ceiling"])


RESULT = {
    "disposition": registry["status"],
    "torsion_irrep_rank": combined_rank,
    "torsion_hook_dimension": hook_dim,
    "released_action_owner_quotient_dimension": registry["verdict"]["released_action_owned_nonredundant_normalization_quotient_dimension"],
    "next_gate": registry["next_gate"],
    "counts": dict(COUNTS),
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{sum(COUNTS.values())}: {FAILURES}")
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
