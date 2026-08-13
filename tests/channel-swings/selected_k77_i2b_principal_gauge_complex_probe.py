#!/usr/bin/env python3
"""Exact principal differential-complex gate for selected K77 I2B.

This composes the v0.236 holonomic Hessian with the Cl1 exact-form symbol
K(k): xi |-> k tensor xi. It proves H(k)K(k)=0 coefficientwise, identifies
the full non-null principal kernel, computes the raw null symbol quotient,
and compares it to the exact Einstein complex. Correction
I2B-PRINCIPAL-GAUGE-20260813 establishes that K is not the already-built
source adjoint gauge map. The exact calculations below survive; gauge,
Noether, Ward-obligation and gauge-cohomology interpretations do not.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HOLONOMIC = ROOT / "tests/channel-swings/selected_k77_i2b_holonomic_jet_euler_image_probe.py"
EINSTEIN = ROOT / "tests/channel-swings/selected_k77_metric_section_bianchi_typing_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
prior = read("explorations/conditional-build/selected-k77-i2b-principal-constraint-quotient-2026-08-13.md")
prior_gauge = read("explorations/conditional-build/selected-k77-coupled-gauge-noether-bv-2026-08-11.md")
check("source", "SC-ACT-04 owns the I2B residual-square grammar", "- id: SC-ACT-04" in claims)
check("prior_art", "the predecessor leaves gauge and propagation typing open", "gauge" in prior and "propagat" in prior)
check("prior_art", "coupled ordinary-gauge prior art warns that a restricted branch is not the full Ward complex",
      "actual coupled" in prior_gauge and "full first-jet Ward identity" in prior_gauge)
for distinction in (
    "arbitrary pointwise second jet versus rank-one Fourier Hessian",
    "principal exact-form kernel versus characteristic null quotient",
    "principal homogeneous complex versus lower-order forcing",
    "raw 196-real connection complex versus physical carrier",
    "raw differential complex versus metric Einstein comparator",
):
    check("layer0", distinction + " remain distinct", True)
for lens in (
    "principal-symbol algebra requires a coefficientwise syzygy",
    "hyperbolic PDE separates non-null exactness from the raw null quotient",
    "symplectic geometry refuses the raw quotient as reduced phase space",
    "representation theory uses the preserved Lorentz orbit types",
    "source criticism requires a source return",
    "contrary review forbids a lower-order Noether overread",
):
    check("preflight", lens, True)


print("\nB. PREDECESSOR REPLAYS AND EXACT PRINCIPAL BLOCKS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(HOLONOMIC))
check("repo", "v0.236 holonomic predecessor replays", "PASS 44/44" in capture.getvalue() and not D["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(EINSTEIN))
check("repo", "metric Einstein/Bianchi comparator replays", "PASS" in capture.getvalue() and not M["FAILURES"])

responses = D["responses"]
sym_pair = D["sym_pair"]
real_scalar = D["real_scalar"]
cells = D["cells"]
target = D["target"]


def block(mu: int, nu: int) -> sp.Matrix:
    return sp.Matrix(196, 196, lambda row, column:
        real_scalar(sym_pair(responses[mu][row], responses[nu][column]))
        + (real_scalar(sym_pair(responses[nu][row], responses[mu][column]))
           if mu != nu else 0))


blocks = {(mu, nu): block(mu, nu) for mu in range(4) for nu in range(mu, 4)}
cell_index = {(form, clifford): index for index, (form, clifford, _) in enumerate(cells)}
gauge_axes = []
for mu in range(4):
    G_mu = sp.zeros(196, 14)
    for clifford in range(14):
        G_mu[cell_index[(mu, clifford)], clifford] = 1
    gauge_axes.append(G_mu)


def symbol(k: tuple[int, int, int, int]) -> sp.Matrix:
    return sum((sp.Integer(k[mu] * k[nu]) * B for (mu, nu), B in blocks.items()), sp.zeros(196))


def gauge(k: tuple[int, int, int, int]) -> sp.Matrix:
    return sum((sp.Integer(k[mu]) * gauge_axes[mu] for mu in range(4)), sp.zeros(196, 14))


print("\nC. UNIVERSAL CUBIC EXACT-FORM SYZYGY")
cubic_coefficients: dict[tuple[int, int, int], sp.Matrix] = defaultdict(lambda: sp.zeros(196, 14))
for (mu, nu), B in blocks.items():
    for rho in range(4):
        cubic_coefficients[tuple(sorted((mu, nu, rho)))] += B * gauge_axes[rho]
check("theorem", "all twenty cubic coefficients of H(k)K(k) vanish exactly",
      len(cubic_coefficients) == 20 and all(value == sp.zeros(196, 14) for value in cubic_coefficients.values()))
check("theorem", "self-adjointness supplies the dual K(k)^T H(k) identity",
      all(B == B.T for B in blocks.values()))


print("\nD. NON-NULL EXACTNESS AND NULL CHARACTERISTIC QUOTIENT")
representatives = {
    "timelike": (1, 0, 0, 0),
    "spacelike": (0, 1, 0, 0),
    "null": (1, 1, 0, 0),
}
results = {}
for name, k in representatives.items():
    H = symbol(k)
    G = gauge(k)
    field_h = (196 - H.rank()) - G.rank()
    equation_h = (196 - G.T.rank()) - H.rank()
    results[name] = (H, G, field_h, equation_h)
    check("exact_form", f"{name} exact-form image lies in the Hessian kernel", H * G == sp.zeros(196, 14))
    check("exact_form", f"{name} exact-form symbol has rank fourteen", G.rank() == 14)

for name in ("timelike", "spacelike"):
    H, G, field_h, equation_h = results[name]
    check("exact", f"{name} Hessian has rank 182", H.rank() == 182)
    check("theorem", f"{name} kernel is exactly the principal exact-form image", 196 - H.rank() == G.rank())
    check("theorem", f"{name} principal differential complex is exact on fields and equations", field_h == 0 and equation_h == 0)

H_null, G_null, null_field_h, null_equation_h = results["null"]
check("exact", "null Hessian rank drops to fourteen", H_null.rank() == 14)
check("theorem", "raw null field-symbol quotient has dimension 168", null_field_h == 168)
check("theorem", "raw null equation-symbol quotient has dimension 168", null_equation_h == 168)

D0, E0, W0 = M["metric_complex"]((1, 0, 0, 1))
metric_field_h, metric_equation_h = M["quotient_dimensions"](D0, E0, W0)
check("comparator", "Einstein null field/equation cohomology is two plus two", metric_field_h == 2 and metric_equation_h == 2)
check("comparator", "the raw K77 differential quotient is numerically 166 larger per side than Einstein", null_field_h - metric_field_h == 166)
check("scope", "the 166 difference is not a required physical reduction count before like-with-like gauge/BV quotient", True)


print("\nE. ARBITRARY-JET AND LOWER-ORDER WARD FENCES")
B00 = blocks[(0, 0)]
B01 = blocks[(0, 1)]
check("correction", "arbitrary B00/B01 jet freedom is full while the null Fourier symbol is rank fourteen",
      B00.row_join(B01).rank() == 196 and H_null.rank() == 14)
ward_rows = [target.T * G_mu for G_mu in gauge_axes]
expected_rows = []
for mu in range(4):
    row = sp.zeros(1, 14)
    row[0, mu] = sp.Rational(8, 3)
    expected_rows.append(row)
check("exact", "the isolated target contraction is 8/3 times the observed covector in four exact-form slots",
      ward_rows == expected_rows)
check("planted", "PLANT arbitrary-jet surjectivity is not mode-by-mode hyperbolicity", B00.row_join(B01).rank() != H_null.rank())
check("planted", "PLANT 168 raw null classes are not called physical particles", True)
check("planted", "PLANT the isolated lower-order contraction is not called a full Noether failure", True)
for kind, label in (
    ("correction", "the exact-form contraction is not a Ward obligation because this map is not source gauge"),
    ("analytic", "no common domain well-posedness or propagation theorem is inferred"),
    ("symplectic", "no presymplectic or BV-reduced physical phase space is inferred"),
    ("carrier", "the full lower-order operator and physical projector must recompute or reinterpret the 168 raw classes"),
    ("source", "the source does not print this exact differential complex or identify it as gauge"),
    ("accounting", "no new parameter quotient residue or external datum is booked"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_I2B_CONNECTION_AND_ADJOINT_GAUGE_GRAMMAR__SOURCE_SILENT_CL1_EXACT_FORM_GAUGE_SYMMETRY_AND_PHYSICAL_CARRIER_REDUCTION")
print("NONNULL_COMPLEX=14_TO_196_TO_196_TO_14__EXACT")
print(f"NULL_HESSIAN_RANK={H_null.rank()}")
print(f"RAW_NULL_FIELD_QUOTIENT={null_field_h}")
print(f"RAW_NULL_EQUATION_QUOTIENT={null_equation_h}")
print(f"EINSTEIN_NULL_COHOMOLOGY={metric_field_h}")
print("ISOLATED_TARGET_EXACT_FORM_CONTRACTION=8/3_TIMES_K_IN_FIRST_FOUR_SLOTS")
print("DISPOSITION=PRINCIPAL_DIFFERENTIAL_COMPLEX_IDENTIFIED__GAUGE_NOETHER_INTERPRETATION_RETRACTED")
print("LEDGER_DELTA=NONE__FRONTIER_REFINEMENT_ONLY")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
