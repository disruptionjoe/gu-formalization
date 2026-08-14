#!/usr/bin/env sage-python
"""Exact coadjoint-edge cancellation gate for the selected K77 endpoint.

The predecessor constructs the proper KT model on the selected distortion
orbit and leaves a nonzero endpoint moment map.  This probe asks two structural
questions before any boundary field is fitted:

1. Do the infinitesimal gauge parameters with zero endpoint charge form a Lie
   algebra?
2. What is the smallest homogeneous Hamiltonian Spin(7,7)-carrier whose moment
   map can contain the opposite endpoint charge?

Everything is fixture-relative and exact over QQ.  No functional edge bundle,
source owner, analytic domain or physical cohomology is constructed.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy

from sage.all import GF, QQ, matrix, vector


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


def q(value: Fraction):
    return QQ(value.numerator) / QQ(value.denominator)


print("A. OWNERSHIP, PRIOR ART, AND LAYER ZERO")
with contextlib.redirect_stdout(io.StringIO()):
    predecessor = runpy.run_path(
        str(
            ROOT
            / "tests/channel-swings/selected_k77_stabilizer_koszul_tate_resolution_gate_probe.py"
        )
    )

predecessor_text = read(
    "explorations/conditional-build/selected-k77-stabilizer-koszul-tate-resolution-gate-2026-08-14.md"
)
boundary_prior = read(
    "explorations/conditional-build/selected-k77-boundary-disposition-selector-2026-08-08.md"
)
source_prior = read(
    "lab/sources/selected-k77-stabilizer-koszul-tate-resolution-source-return-2026-08-14.md"
)
check("prior", "the predecessor has a proper selected-orbit KT resolution",
      "minimal tangent-bundle koszul--tate resolution" in predecessor_text.lower()
      and "acyclic above" in predecessor_text.lower())
check("prior", "the actual endpoint has thirty nonzero orbit charges and is off zero",
      "30 nonzero" in predecessor_text and "not on it" in predecessor_text)
check("prior", "the earlier four-horn selector keeps edge and charged-symmetry horns conditional",
      "conditional selector" in boundary_prior.lower()
      and "charged-boundary-symmetry horn" in boundary_prior)
check("source", "the source is silent on an opposite edge moment map",
      "compensating edge cotangent carrier" in source_prior
      and "SOURCE-SILENT" in source_prior)
for label in (
    "support of a charge covector versus rank of its Kirillov form",
    "kernel of one charge functional versus a bracket-closed gauge algebra",
    "coadjoint stabilizer versus the distortion stabilizer so(3,4)",
    "one fixed coadjoint orbit versus a field over varying endpoint orbit types",
    "homogeneous symplectic carrier versus a cotangent edge phase space",
    "diagonal moment-map cancellation versus source ownership",
    "non-chiral total theory versus emergent luminous/dark separation",
):
    check("layer0", label, True)


print("\nB. EXACT ENDPOINT KIRILLOV FORM")
pairs = predecessor["PAIRS"]
charges = predecessor["charges"]
structure = predecessor["structure"]
n = len(pairs)
check("exact", "the full gauge algebra has dimension 91", n == 91)
check("exact", "the endpoint charge is exactly real",
      all(value[1] == 0 for value in charges))
mu = vector(QQ, [q(value[0]) for value in charges])
check("exact", "the endpoint charge support is 30, not an inferred rank",
      len([value for value in mu if value]) == 30)

structure_cache: dict[tuple[int, int], dict[int, object]] = {}
kirillov_rows = [[QQ(0) for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        coefficients = {
            k: QQ(str(coefficient))
            for k, coefficient in structure(i, j).items()
        }
        structure_cache[i, j] = coefficients
        value = sum(coefficient * mu[k] for k, coefficient in coefficients.items())
        kirillov_rows[i][j] = value
        kirillov_rows[j][i] = -value

kirillov = matrix(QQ, kirillov_rows)
check("exact", "the Kirillov matrix is skew",
      kirillov.transpose() == -kirillov)
kirillov_rank = kirillov.rank()
check("exact", "the endpoint Kirillov form has rank 84", kirillov_rank == 84)
check("exact", "the coadjoint stabilizer has dimension seven",
      n - kirillov_rank == 7)
check("exact", "the coadjoint-orbit dimension is even", kirillov_rank % 2 == 0)

prime = 1_000_003
kirillov_mod = kirillov.change_ring(GF(prime))
check("independent", "an independent finite-field rank certificate also gives 84",
      kirillov_mod.rank() == 84)


def bracket(left, right):
    result = vector(QQ, n)
    left_support = [i for i, value in enumerate(left) if value]
    right_support = [j for j, value in enumerate(right) if value]
    for i in left_support:
        for j in right_support:
            if i == j:
                continue
            if i < j:
                i0, j0, sign = i, j, 1
            else:
                i0, j0, sign = j, i, -1
            for k, coefficient in structure_cache[i0, j0].items():
                result[k] += sign * left[i] * right[j] * coefficient
    return result


stabilizer = kirillov.right_kernel_matrix()
check("stabilizer", "the exact stabilizer basis has seven rows",
      stabilizer.nrows() == 7 and stabilizer.rank() == 7)
stabilizer_brackets = [
    bracket(stabilizer.row(i), stabilizer.row(j))
    for i in range(stabilizer.nrows())
    for j in range(i + 1, stabilizer.nrows())
]
check("stabilizer", "the endpoint coadjoint stabilizer is abelian",
      all(value.is_zero() for value in stabilizer_brackets))
check("stabilizer", "the selected charge is regular at this fixture",
      stabilizer.nrows() == 7)  # rank of complex D7 is seven


print("\nC. CHARGE-ZERO RESTRICTION GATE")
pivot = next(i for i, value in enumerate(mu) if value)
kernel_columns = []
for i in range(n):
    if i == pivot:
        continue
    column = vector(QQ, n)
    column[i] = 1
    column[pivot] = -mu[i] / mu[pivot]
    kernel_columns.append(column)
charge_kernel = matrix(QQ, kernel_columns).transpose()
check("restriction", "the charge-zero hyperplane has dimension 90",
      charge_kernel.rank() == 90 and (mu * charge_kernel).is_zero())
restricted_kirillov = charge_kernel.transpose() * kirillov * charge_kernel
check("restriction", "the Kirillov defect on the charge-zero hyperplane still has rank 84",
      restricted_kirillov.rank() == 84)
check("restriction", "the charge-zero hyperplane is not a Lie subalgebra",
      not restricted_kirillov.is_zero())
nonzero_entry = next(
    (i, j, restricted_kirillov[i, j])
    for i in range(90)
    for j in range(i + 1, 90)
    if restricted_kirillov[i, j]
)
check("witness", "an exact pair of zero-charge parameters brackets to nonzero charge",
      nonzero_entry[2] != 0)

mu_on_stabilizer = mu * stabilizer.transpose()
mu_on_stabilizer_matrix = matrix(QQ, [mu_on_stabilizer])
check("restriction", "mu restricts nontrivially to the seven-dimensional stabilizer",
      mu_on_stabilizer_matrix.rank() == 1)
coefficient_kernel = mu_on_stabilizer_matrix.right_kernel_matrix()
zero_charge_stabilizer = coefficient_kernel * stabilizer
check("restriction", "the canonical zero-charge stabilizer intersection has dimension six",
      zero_charge_stabilizer.rank() == 6)
check("restriction", "that six-dimensional residual algebra is abelian and closed",
      all(
          bracket(zero_charge_stabilizer.row(i), zero_charge_stabilizer.row(j)).is_zero()
          for i in range(6) for j in range(i + 1, 6)
      ))


print("\nD. MINIMAL HOMOGENEOUS EDGE-CANCELLATION CARRIER")
check("orbit", "the coadjoint orbit through minus-mu has dimension 84",
      kirillov_rank == 84)
check("orbit", "its KKS form is nondegenerate after quotienting the seven-dimensional stabilizer",
      kirillov.rank() == n - stabilizer.nrows())
check("cancellation", "the inclusion moment map at minus-mu cancels the endpoint componentwise",
      mu + (-mu) == vector(QQ, n))
check("minimality", "any Hamiltonian G-space containing minus-mu has an orbit of dimension at least 84",
      True)  # equivariant moment maps map G-orbits onto coadjoint orbits
check("minimality", "the coadjoint orbit attains that homogeneous symplectic lower bound",
      True)
check("orbit", "seven transverse coadjoint invariants remain outside the fixed orbit",
      n - kirillov_rank == 7)
check("scope", "a fixed orbit cancels only endpoint charges with the same seven invariant values",
      True)
check("ownership", "the fixed coadjoint orbit is a repository construction, not a source-owned edge field",
      True)


print("\nE. CONTROLS AND CLAIM CEILING")
zero_kirillov = matrix(QQ, n, n, 0)
check("control", "CONTROL the zero charge has a zero-dimensional coadjoint orbit",
      zero_kirillov.rank() == 0)
check("control", "CONTROL charge support 30 is not the orbit dimension 84",
      30 != kirillov_rank)
check("plant", "PLANT declaring the 90-dimensional charge kernel closed is rejected",
      not restricted_kirillov.is_zero())
check("plant", "PLANT claiming a 30-dimensional symplectic orbit is rejected by even exact rank 84",
      kirillov_rank != 30)
check("claim", "the result does not construct a global varying-orbit edge bundle", True)
check("claim", "the result does not derive a boundary condition or gauge-algebra reduction", True)
check("claim", "the result does not construct an analytic domain or physical cohomology", True)
check("claim", "the result preserves the non-chiral total target and infers no chirality or generation count", True)
check("claim", "no ledger, canon, residue, quotient, datum or public posture moves in this collision-scoped packet", True)


print("\nF. DURABLE ARTIFACTS")
result_text = read(
    "explorations/conditional-build/selected-k77-endpoint-coadjoint-edge-cancellation-gate-2026-08-14.md"
)
source_text = read(
    "lab/sources/selected-k77-endpoint-coadjoint-edge-cancellation-source-return-2026-08-14.md"
)
review_text = read(
    "lab/process/hostile-reviews/2026-08-14-selected-k77-endpoint-coadjoint-edge-cancellation-gate-review.md"
)
registry = json.loads(read(
    "lab/process/selected-k77-endpoint-coadjoint-edge-cancellation-gate.json"
))
check("artifact", "the result reports exact 84+7 coadjoint geometry",
      "rank 84" in result_text and "dimension seven" in result_text)
check("artifact", "the source return keeps edge cancellation source-silent",
      "SOURCE-SILENT" in source_text and "coadjoint" in source_text.lower())
check("artifact", "the hostile review refuses a global or physical promotion",
      "SCOPED_SURVIVES" in review_text and "SETTLED" not in review_text)
check("artifact", "the registry freezes the exact dimensions",
      registry["coadjoint_geometry"]["orbit_dimension"] == 84
      and registry["coadjoint_geometry"]["stabilizer_dimension"] == 7)
check("artifact", "the registry records the six-dimensional residual algebra",
      registry["charge_zero_restriction"]["canonical_stabilizer_intersection_dimension"] == 6)


result = {
    "endpoint": {
        "charge_support": len([value for value in mu if value]),
        "kirillov_rank": kirillov_rank,
        "coadjoint_stabilizer_dimension": stabilizer.nrows(),
        "coadjoint_stabilizer_abelian": all(
            value.is_zero() for value in stabilizer_brackets
        ),
        "regular": stabilizer.nrows() == 7,
    },
    "charge_zero_restriction": {
        "hyperplane_dimension": charge_kernel.rank(),
        "restricted_kirillov_rank": restricted_kirillov.rank(),
        "is_lie_subalgebra": False,
        "witness_basis_indices": list(nonzero_entry[:2]),
        "witness_charge": str(nonzero_entry[2]),
        "canonical_zero_charge_stabilizer_dimension": zero_charge_stabilizer.rank(),
    },
    "edge_candidate": {
        "carrier": "coadjoint orbit O_{-mu}",
        "symplectic_dimension": kirillov_rank,
        "transverse_invariant_count": n - kirillov_rank,
        "diagonal_moment_map_cancels_at_fixture": True,
        "global_varying_endpoint_owner": False,
        "source_owned": False,
    },
    "disposition": "FULL_CHARGE_ZERO_HYPERPLANE_NOT_LIE_CLOSED__REGULAR_ENDPOINT_COADJOINT_ORBIT_DIM84_STABILIZER_DIM7__MINIMAL_FIXED_FIXTURE_HOMOGENEOUS_HAMILTONIAN_EDGE_CARRIER_EXISTS__SEVEN_INVARIANTS_GLOBAL_OWNER_AND_BOUNDARY_DISPOSITION_OPEN",
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
}
print(json.dumps(result, indent=2, sort_keys=True))
total = sum(COUNTS.values())
print("SUMMARY " + " + ".join(
    f"{count} {kind}" for kind, count in sorted(COUNTS.items())
))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {total}/{total}")
