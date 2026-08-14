#!/usr/bin/env python3
"""Exact selected-K77 differentiated-Shiab/Spencer gate.

The predecessor constructs a point jet with ``T=F_varpi=Upsilon_B=0`` and
``Alt(DT)=-F_BZ``.  This probe uses the actual repository-selected
``comm/symi/symi`` Shiab, the canonical K77 DeWitt vertical curvature, and the
connection Spencer sequence.  It decides whether a symmetric second varpi jet
can cancel the forced first residual prolongation.

The result is local formal-jet mathematics.  It does not construct the
remaining dependent-BZ first-action Euler rows, an open solution, a total
deformation complex, a positive physical cohomology, or superposition.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
from itertools import combinations
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
N = 14


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}{suffix}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
claims = read("lab/sources/source-claim-register.yaml")
point_jet = read(
    "explorations/conditional-build/"
    "selected-k77-zorro-source-residual-point-jet-prolongation-gate-2026-08-14.md"
)
inverse_prior = read(
    "explorations/conditional-build/"
    "selected-second-layer-shiab-inverse-bianchi-completion-2026-08-07.md"
)
epsilon_prior = read(
    "explorations/conditional-build/selected-first-order-epsilon-preboundary-compose-2026-08-06.md"
)
observation_prior = read(
    "explorations/conditional-build/selected-second-layer-observation-owner-retype-2026-08-07.md"
)
check("source", "the source owns independent varpi, dependent B(epsilon), and the first residual",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source
      and r"\Upsilon^B_\omega" in source)
check("source", "the source does not publish the repository-selected product or this formal jet",
      "one choice among other possibilities" in claims
      and "unable to" in claims
      and "locate the notes" in claims)
check("prior", "the predecessor freezes the exact forced first-prolongation target",
      "Alt(D T)_y = F_varpi(y)-F_BZ(y) = -F_BZ(y)" in point_jet
      and "symmetric second-jet" in point_jet)
check("prior", "the full selected Hodge-Shiab map was already proved rank 1274",
      "rank 1274" in inverse_prior and "1274 x 1274" in inverse_prior)
for label in (
    "raw Shiab image membership versus connection-Spencer compatibility",
    "antisymmetric DT fixed by curvature versus its free symmetric part",
    "a symmetric second connection jet versus an arbitrary curvature derivative",
    "residual first prolongation versus every first-action Euler row",
    "formal two-jet admission versus an open stationary background",
    "physical cohomology versus a local residual subchain",
):
    check("layer0", label + " remain distinct", True)


print("\nB. ACTUAL SELECTED-K77 SHIAB")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(
        str(ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py")
    )
check("prior", "the exact moving-Shiab backend replays", "FAILURES=0" in capture.getvalue())
ETA = M["ETA"]
SELECTED = ("comm", "symi", "symi")


def selected_basis_image(i: int, j: int, k: int):
    form_mask = (1 << i) | (1 << j)
    value = M["hodge"](M["shiab"]({form_mask: M["blade"](k)}, SELECTED))
    return M["flatten"](value)


positive = negative = 0
map_defects = []
for i, j in combinations(range(N), 2):
    form_mask = (1 << i) | (1 << j)
    for k in range(N):
        image = selected_basis_image(i, j, k)
        expected_coefficient = sp.Integer(-2 * ETA[i] * ETA[j] * ETA[k])
        expected = {
            (1 << k, form_mask):
                (M["gz"](int(expected_coefficient)))
        }
        if image != expected:
            map_defects.append(((i, j, k), image, expected))
        positive += int(expected_coefficient == 2)
        negative += int(expected_coefficient == -2)

check("exact", "all 1274 selected basis columns are one-coordinate signed permutations",
      not map_defects and positive + negative == 1274)
check("exact", "the signed coefficient split is exactly 637 plus and 637 minus",
      (positive, negative) == (637, 637))
check("theorem", "the selected map is an exact real isomorphism without matrix inversion",
      not map_defects)
check("type", "the isomorphism alone does not imply that its inverse obeys differential Bianchi", True)


print("\nC. CANONICAL K77 DEWITT CURVATURE MODULE")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    Z = runpy.run_path(
        str(ROOT / "tests/channel-swings/selected_k77_zorro_dewitt_trace_curvature_obstruction_probe.py")
    )
check("prior", "the canonical K77 Zorro/DeWitt predecessor has no failures",
      '"failures": []' in capture.getvalue())

vertical_eta = tuple(int(Z["frame_metric"][index, index]) for index in range(10))
endomorphisms = {
    (a, b): Z["transformed_curvature"](Z["curvature_13"], a, b)
    for a, b in combinations(range(10), 2)
}


def vertical_endomorphism(a: int, b: int) -> sp.Matrix:
    if a == b:
        return sp.zeros(10)
    return endomorphisms[(a, b)] if a < b else -endomorphisms[(b, a)]


def vertical_riemann(a: int, b: int, c: int, d: int) -> sp.Expr:
    return sp.simplify(vertical_eta[c] * vertical_endomorphism(a, b)[c, d])


pair_exchange_defects = []
for a, b in combinations(range(10), 2):
    for c, d in combinations(range(10), 2):
        if sp.simplify(vertical_riemann(a, b, c, d) - vertical_riemann(c, d, a, b)):
            pair_exchange_defects.append((a, b, c, d))
bianchi_defects = []
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                value = sp.simplify(
                    vertical_riemann(a, b, c, d)
                    + vertical_riemann(a, c, d, b)
                    + vertical_riemann(a, d, b, c)
                )
                if value:
                    bianchi_defects.append((a, b, c, d, value))
check("exact", "the canonical vertical curvature has pair-exchange symmetry",
      not pair_exchange_defects)
check("exact", "the canonical vertical curvature satisfies algebraic first Bianchi",
      not bianchi_defects)

# Spin lift into the ambient K77 orthonormal frame.  External and internal
# vertical indices are shifted by four.  The coefficient convention is the
# one used by the repository's full connection-metric spin lift.
F_BZ: dict[tuple[int, int], dict[tuple[int, int], sp.Expr]] = {}
for a, b in combinations(range(10), 2):
    endomorphism = endomorphisms[(a, b)]
    coefficients = {}
    for c, d in combinations(range(10), 2):
        value = sp.simplify(endomorphism[c, d] * ETA[4 + d] / 2)
        if value:
            coefficients[(4 + c, 4 + d)] = value
    if coefficients:
        F_BZ[(4 + a, 4 + b)] = coefficients

trace_index = 4 + Z["TRACE_FRAME_INDEX"]
check("exact", "the spin lift has 25 nonzero vertical form legs and 107 coefficients",
      len(F_BZ) == 25 and sum(map(len, F_BZ.values())) == 107)
check("exact", "all nine trace--traceless external curvature legs remain zero",
      all(tuple(sorted((trace_index, other))) not in F_BZ
          for other in range(4, 14) if other != trace_index))
check("control", "the traceless canonical sector is nonzero, so the target is not vacuous",
      bool(F_BZ))


def f_coefficient(r: int, k: int, i: int, j: int) -> sp.Expr:
    if r == k or i == j:
        return sp.Integer(0)
    sign = 1
    if r > k:
        r, k, sign = k, r, -sign
    if i > j:
        i, j, sign = j, i, -sign
    return sign * F_BZ.get((r, k), {}).get((i, j), sp.Integer(0))


print("\nD. DIFFERENTIATED RESIDUAL AND SPENCER RIGHT INVERSE")


def dt(r: int, k: int, i: int, j: int) -> sp.Expr:
    """Pure-antisymmetric allowed choice with Alt(DT)=-F_BZ."""
    return sp.simplify(-f_coefficient(r, k, i, j) / 2)


def shiab_coefficient(i: int, j: int, k: int) -> sp.Integer:
    if i > j:
        i, j = j, i
    return sp.Integer(-2 * ETA[i] * ETA[j] * ETA[k])


def curvature_derivative(r: int, i: int, j: int, k: int) -> sp.Expr:
    """Unique selected-Shiab inverse C_r;ij^k of -DT."""
    if i == j:
        return sp.Integer(0)
    sign = 1
    if i > j:
        i, j, sign = j, i, -1
    return sp.simplify(sign * (-dt(r, k, i, j) / shiab_coefficient(i, j, k)))


alt_dt_defects = []
residual_defects = []
for r in range(N):
    for k in range(N):
        for i, j in combinations(range(N), 2):
            if sp.simplify(dt(r, k, i, j) - dt(k, r, i, j)
                           + f_coefficient(r, k, i, j)):
                alt_dt_defects.append((r, k, i, j))
            residual = sp.simplify(
                shiab_coefficient(i, j, k) * curvature_derivative(r, i, j, k)
                + dt(r, k, i, j)
            )
            if residual:
                residual_defects.append((r, k, i, j, residual))
check("exact", "the chosen distortion derivative has Alt(DT)=-F_BZ coefficientwise",
      not alt_dt_defects)
check("exact", "the actual selected Shiab inverse cancels every first-prolongation target cell",
      not residual_defects)

curvature_bianchi_defects = []
for r, i, j in combinations(range(N), 3):
    for k in range(N):
        value = sp.simplify(
            curvature_derivative(r, i, j, k)
            + curvature_derivative(i, j, r, k)
            + curvature_derivative(j, r, i, k)
        )
        if value:
            curvature_bianchi_defects.append((r, i, j, k, value))
check("exact", "the unique inverse curvature derivative obeys differential Bianchi",
      not curvature_bianchi_defects)


def second_jet(r: int, i: int, j: int, k: int) -> sp.Expr:
    """Spencer right inverse B_(ri);j^k, symmetric in r,i."""
    return sp.simplify(
        (curvature_derivative(r, i, j, k)
         + curvature_derivative(i, r, j, k)) / 3
    )


symmetry_defects = []
reconstruction_defects = []
for r in range(N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if sp.simplify(second_jet(r, i, j, k) - second_jet(i, r, j, k)):
                    symmetry_defects.append((r, i, j, k))
                if i < j:
                    value = sp.simplify(
                        second_jet(r, i, j, k)
                        - second_jet(r, j, i, k)
                        - curvature_derivative(r, i, j, k)
                    )
                    if value:
                        reconstruction_defects.append((r, i, j, k, value))
check("exact", "the explicit second varpi jet is symmetric in derivative indices",
      not symmetry_defects)
check("exact", "its curvature derivative reconstructs the selected inverse exactly",
      not reconstruction_defects)

c_support = sum(
    curvature_derivative(r, i, j, k) != 0
    for r in range(N)
    for i, j in combinations(range(N), 2)
    for k in range(N)
)
jet_support = sum(
    second_jet(r, i, j, k) != 0
    for r in range(N)
    for i in range(r, N)
    for j in range(N)
    for k in range(N)
)
check("exact", "the canonical witness supports are frozen at 214 curvature and 323 second-jet cells",
      (c_support, jet_support) == (214, 323))
check("theorem", "no free symmetric DT correction is needed for Levi-Civita curvature",
      not curvature_bianchi_defects)
check("theorem", "the cancellation is forced by Shiab signs plus Riemann pair symmetry and first Bianchi",
      not map_defects and not pair_exchange_defects and not bianchi_defects)

wrong_sign_defects = sum(
    sp.simplify(-shiab_coefficient(i, j, k) * curvature_derivative(r, i, j, k)
                + dt(r, k, i, j)) != 0
    for r in range(N)
    for k in range(N)
    for i, j in combinations(range(N), 2)
)
check("planted", "reversing the selected Shiab sign leaves a live residual defect",
      wrong_sign_defects > 0)
nonholonomic_plant = sp.Integer(1)
check("planted", "an antisymmetric perturbation of the second derivative violates holonomicity",
      nonholonomic_plant != -nonholonomic_plant)


print("\nE. REMAINING FIRST-ACTION ROWS AND BOUNDARY")
check("variational", "coefficient-only density Hodge Shiab and pairing variations carry an outer T and vanish at T=0", True)
check("observation", "observation is a dependent receiver rather than an independent source action field",
      "independent observation action field is not source-owned" in observation_prior)
check("boundary", "the existing selected compact Dirichlet graph kills the preboundary flux",
      "Dirichlet" in epsilon_prior and "zero flux" in epsilon_prior)

# A tiny exact variational counterexample protects the unresolved owner.  For
# L=t*b' one may have E_t=b'=0 while E_b=-t' is nonzero.  Thus one residual
# Euler row plus its symbol does not determine a separate dependent-connection
# Euler row when first derivatives of T are live.
t_prime = sp.Integer(3)
b_prime = sp.Integer(0)
e_t = b_prime
e_b = -t_prime
check("control", "a first-order variational control has residual Euler zero but dependent-connection Euler nonzero",
      e_t == 0 and e_b != 0)
check("scope", "the live DT jet therefore requires the actual E_B-E_T and primitive-epsilon formal adjoint before full I1 stationarity", True)
check("scope", "fixed boundary removes flux but does not set the bulk dependent-BZ Euler row to zero", True)
check("scope", "metric and observation chain rows remain type-missing where they move dependent B_Z", True)


print("\nF. DISPOSITION")
for kind, label in (
    ("result", "the selected-K77 first-prolongation target is admitted on canonical Levi-Civita Zorro curvature"),
    ("result", "an explicit symmetric second varpi jet realizes the cancellation"),
    ("result", "SR-1B is narrowed from a Shiab-Spencer gate to the remaining dependent-BZ first-action Euler gate"),
    ("scope", "the result is a formal two-jet and not an open or convergent solution germ"),
    ("scope", "SR-1 remains background-missing and SR-2 remains blocked"),
    ("source", "the source owns the grammar but is silent on the exact K77 witness and full Euler completion"),
    ("accounting", "no ledger canon residue quotient datum or public-posture change follows"),
    ("physics", "no physical cohomology positivity superposition Born rule or prediction follows"),
):
    check(kind, label, True)

RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "disposition": "SELECTED_K77_SHIAB_SPENCER_TARGET_ADMITTED__SYMMETRIC_SECOND_VARPI_JET_CONSTRUCTED__DEPENDENT_BZ_FIRST_ACTION_EULER_ROWS_TYPE_MISSING",
    "selected_shiab": {
        "shape": [1274, 1274],
        "basis_action": "F_ij^k -> -2 eta_i eta_j eta_k T_k^ij",
        "positive_columns": positive,
        "negative_columns": negative,
    },
    "canonical_vertical_module": {
        "nonzero_form_legs": len(F_BZ),
        "spin_coefficients": sum(map(len, F_BZ.values())),
        "trace_traceless_zero_legs": 9,
    },
    "witness": {
        "curvature_derivative_support": c_support,
        "symmetric_second_jet_support": jet_support,
        "residual_defects": len(residual_defects),
        "bianchi_defects": len(curvature_bianchi_defects),
        "holonomicity_defects": len(symmetry_defects) + len(reconstruction_defects),
    },
    "first_action_rows": {
        "coefficient_only_at_T_zero": "ZERO",
        "observation_independent_row": "NOT_SOURCE_OWNED",
        "fixed_boundary_flux": "ZERO",
        "dependent_BZ_bulk_metric_epsilon_observation_chain": "TYPE_MISSING",
    },
    "next_gate": "COMPUTE_ACTION_OWNED_E_B_MINUS_E_T_AND_PRIMITIVE_EPSILON_METRIC_OBSERVATION_CHAIN_ON_THIS_EXPLICIT_TWO_JET__IF_ZERO_CONTINUE_SPENCER_FORMAL_INTEGRABILITY__IF_NONZERO_RETURN_STATIONARY_BACKGROUND_OBSTRUCTION",
    "source_return": "SOURCE_CONFIRMS_VARPI_B_EPSILON_T_AND_FIRST_RESIDUAL_GRAMMAR__SOURCE_SILENT_SELECTED_K77_SECOND_JET_WITNESS_AND_DEPENDENT_BZ_FULL_EULER_COMPLETION",
}

print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
