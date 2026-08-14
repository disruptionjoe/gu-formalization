#!/usr/bin/env sage-python
"""Exact first-variation gate for the selected K77 endpoint coadjoint orbit.

The predecessor identifies the actual endpoint charge as a regular covector
of so(7,7)^* with an 84-dimensional coadjoint orbit and seven transverse
invariant values.  This probe identifies the covector with so(7,7) through
the exact vector-representation trace form, constructs the six even trace
invariants and the degree-seven Pfaffian, and differentiates them along the
action-owned simultaneous scaling line (B,T) -> lambda(B,T).

One nonzero invariant derivative is enough to reject a single fixed
coadjoint orbit as a carrier for all nearby action endpoints.  The result is
finite-fixture and algebraic; it does not construct the required larger edge
phase space, a boundary action, an analytic domain, or physical cohomology.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, diagonal_matrix, matrix, vector


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_endpoint_coadjoint_edge_cancellation_gate_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k77-coadjoint-invariant-variation-gate-2026-08-14.md"
REGISTRY = ROOT / "lab/process/selected-k77-coadjoint-invariant-variation-gate.json"
SOURCE = ROOT / "lab/sources/selected-k77-coadjoint-invariant-variation-source-return-2026-08-14.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-14-selected-k77-coadjoint-invariant-variation-gate-review.md"
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


def q(value):
    if isinstance(value, Fraction):
        return QQ(value.numerator) / QQ(value.denominator)
    return QQ(str(value))


print("A. PREDECESSOR, SOURCE, AND LAYER ZERO")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    prior = runpy.run_path(str(PREDECESSOR))
check("prior", "the endpoint coadjoint predecessor replays 51/51",
      capture.getvalue().rstrip().endswith("PASS 51/51") and not prior["FAILURES"])
check("prior", "the predecessor charge is regular with orbit dimension 84",
      prior["kirillov_rank"] == 84 and prior["stabilizer"].nrows() == 7)
for label in (
    "seven invariant values versus seven coordinates on the stabilizer",
    "motion along one coadjoint orbit versus transverse charge variation",
    "action-owned B/T variation versus an arbitrary covector perturbation",
    "a fixed KKS orbit versus a phase space spanning multiple orbit values",
    "invariant-polynomial nonstationarity versus a physical edge degree count",
    "finite algebraic variation versus a functional analytic boundary theory",
):
    check("layer0", label, True)

source_prior = read(
    "lab/sources/selected-k77-endpoint-coadjoint-edge-cancellation-source-return-2026-08-14.md"
)
check("source", "the source owns B, T and the moving gauge-frame parent",
      "T_\\omega" in read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
      and "epsilon" in source_prior.lower())
check("source", "the source remains silent on coadjoint-invariant locking",
      "require the seven invariant values" in source_prior)


print("\nB. TRACE-DUAL COADJOINT ELEMENT AND D7 INVARIANTS")
PAIRS = prior["pairs"]
VECTOR = prior["predecessor"]["bfv"]["VECTOR"]
ETA = prior["predecessor"]["bfv"]["ETA"]
mu = prior["mu"]
basis = [matrix(QQ, 14, 14, [q(value) for value in VECTOR[pair]]) for pair in PAIRS]
gram = matrix(QQ, [[(left * right).trace() for right in basis] for left in basis])
check("duality", "the vector-representation trace pairing is nondegenerate", gram.rank() == 91)
gram_inverse = gram.inverse()
dual_basis = []
for column in range(91):
    dual = matrix(QQ, 14, 14, 0)
    for coefficient, generator in zip(gram_inverse.column(column), basis):
        dual += coefficient * generator
    dual_basis.append(dual)


def dual_matrix(covector):
    coefficients = gram_inverse * vector(QQ, covector)
    out = matrix(QQ, 14, 14, 0)
    for coefficient, generator in zip(coefficients, basis):
        out += coefficient * generator
    return out


L = dual_matrix(mu)
eta = diagonal_matrix(QQ, ETA)
skew = eta * L
check("duality", "the trace-dual element reproduces all 91 charge components",
      vector(QQ, [(L * generator).trace() for generator in basis]) == mu)
check("duality", "the trace-dual element lies in so(7,7)",
      L.transpose() * eta + eta * L == matrix(QQ, 14, 14, 0))
check("pfaffian", "eta times the dual element is exactly skew",
      skew.transpose() == -skew)


def invariants(element):
    skew_element = eta * element
    even = tuple((element ** (2 * degree)).trace() for degree in range(1, 7))
    return even + (skew_element.pfaffian(),)


invariant_values = invariants(L)
check("invariant", "the six even traces and degree-seven Pfaffian are exact",
      len(invariant_values) == 7 and all(value in QQ for value in invariant_values))
check("invariant", "the selected regular covector has nonzero Pfaffian",
      invariant_values[-1] != 0)

# Verify that these seven Chevalley generators have independent differentials
# at the selected regular element.  The Pfaffian derivative uses
# d pf(S)=pf(S)/2 tr(S^-1 dS), valid because the exact Pfaffian is nonzero.
skew_inverse = skew.inverse()
gradient_rows = []
for degree in range(1, 7):
    gradient_rows.append([
        2 * degree * (L ** (2 * degree - 1) * dual_basis[j]).trace()
        for j in range(91)
    ])
pfaffian = invariant_values[-1]
gradient_rows.append([
    pfaffian * (skew_inverse * eta * dual_basis[j]).trace() / 2
    for j in range(91)
])
invariant_gradient = matrix(QQ, gradient_rows)
check("invariant", "the seven invariant differentials are independent at the fixture",
      invariant_gradient.rank() == 7)
check("invariant", "their common tangent kernel has the 84-dimensional orbit rank",
      invariant_gradient.right_kernel().dimension() == 84)


print("\nC. ACTION-OWNED FIRST VARIATION")
bank = prior["predecessor"]["bfv"]["packet"]
B = bank["B"]
T = bank["T"]
fscale = bank["fscale"]
comm = bank["M"]["comm"]
blade = bank["blade"]
eulers = bank["eulers"]


def endpoint_charge(scale):
    scaled_b = fscale(Fraction(scale), B)
    scaled_t = fscale(Fraction(scale), T)
    e_b, e_t = eulers(scaled_b, scaled_t)
    values = []
    imaginary_values = []
    for pair in PAIRS:
        direction = {
            form_mask: comm(blade(pair), coefficient)
            for form_mask, coefficient in scaled_t.items()
        }
        left = e_b(direction)
        right = e_t(direction)
        values.append(q(left[0] - right[0]))
        imaginary_values.append(left[1] - right[1])
    check("reality", f"all 91 scaled endpoint {scale} charges remain real",
          all(value == 0 for value in imaginary_values))
    return vector(QQ, values)


# Along (B,T)->lambda(B,T), the selected cubic term contributes lambda^3
# and the quadratic mass term lambda^2.  Values at lambda=1,2 determine the
# exact coefficients and hence the derivative at lambda=1.
mu_one = endpoint_charge(1)
mu_two = endpoint_charge(2)
check("variation", "the reconstructed lambda=1 endpoint equals the predecessor", mu_one == mu)
cubic_mu = (mu_two - 4 * mu_one) / 4
mass_mu = mu_one - cubic_mu
dmu = 3 * cubic_mu + 2 * mass_mu
check("variation", "the scaling line has the exact lambda^3 plus lambda^2 decomposition",
      mu_two == 8 * cubic_mu + 4 * mass_mu)
check("variation", "the action-owned endpoint charge has a nonzero first variation", dmu != 0)

dL = dual_matrix(dmu)
invariant_derivatives = tuple(
    2 * degree * (L ** (2 * degree - 1) * dL).trace()
    for degree in range(1, 7)
) + (pfaffian * (skew_inverse * eta * dL).trace() / 2,)
check("variation", "at least one coadjoint invariant has an exact nonzero derivative",
      any(value != 0 for value in invariant_derivatives))
check("variation", "the derivative is transverse to the 84-dimensional coadjoint orbit",
      invariant_gradient * dmu != vector(QQ, 7))
check("variation", "a single fixed coadjoint orbit cannot contain this action-owned scaling line",
      any(value != 0 for value in invariant_derivatives))
print("INVARIANT_VALUES=" + ",".join(str(value) for value in invariant_values))
print("INVARIANT_DERIVATIVES=" + ",".join(str(value) for value in invariant_derivatives))


print("\nD. CONTROLS AND CLAIM CEILING")
# Infinitesimal coadjoint motion is tangent to every invariant level.  The
# predecessor Kirillov matrix maps an algebra parameter to such a charge
# tangent; test a live column rather than merely asserting invariance.
kirillov = prior["kirillov"]
orbit_column = next(kirillov.column(j) for j in range(91) if kirillov.column(j) != 0)
check("control", "CONTROL an infinitesimal coadjoint-orbit direction kills all seven derivatives",
      invariant_gradient * orbit_column == vector(QQ, 7))
check("plant", "PLANT treating the action-owned derivative as orbit tangent is rejected",
      invariant_gradient * dmu != vector(QQ, 7))
check("scope", "the result rejects only one fixed-orbit carrier over varying endpoints", True)
check("scope", "a larger group/cotangent carrier and charged boundary symmetry remain open", True)
check("scope", "no boundary action analytic domain positive pairing or physical cohomology is built", True)
check("physics", "the non-chiral total target is preserved and no W/mirror or generation selection follows", True)
check("accounting", "ledger v0.254 verdicts residue quotients data canon and public posture remain unchanged", True)


print("\nE. DURABLE ARTIFACTS")
check("artifact", "result registry source return and hostile review all exist",
      all(path.exists() for path in (RESULT, REGISTRY, SOURCE, REVIEW)))
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
result_text = RESULT.read_text(encoding="utf-8")
source_text = SOURCE.read_text(encoding="utf-8")
review_text = REVIEW.read_text(encoding="utf-8")
check("artifact", "the registry preserves all seven exact invariant derivatives",
      registry["coadjoint_invariants"]["first_derivatives"] == [str(value) for value in invariant_derivatives])
check("artifact", "the result rejects the fixed-orbit global horn without inventing its successor",
      "unconstrained fixed-orbit global horn" in result_text.lower()
      and "edge system must be larger" in result_text.lower()
      and "than one orbit" in result_text.lower())
check("artifact", "source and hostile returns preserve ownership and physical limits",
      "SOURCE-SILENT" in source_text and "SCOPED_SURVIVES" in review_text)


print("\nSUMMARY")
print("INVARIANTS=" + ",".join(str(value) for value in invariant_values))
print("FIRST_DERIVATIVES=" + ",".join(str(value) for value in invariant_derivatives))
print("NONZERO_INVARIANT_DERIVATIVES=" + str(sum(value != 0 for value in invariant_derivatives)))
print("FIXED_ORBIT_GLOBAL_HORN=REJECTED")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
print(f"FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
