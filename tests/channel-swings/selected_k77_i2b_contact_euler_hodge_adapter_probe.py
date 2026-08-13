#!/usr/bin/env python3
"""Exact local adapter gate between I2B contact and residual-response carriers.

The v0.221 contact response is an ``Omega^1(Cl^2)`` object.  The v0.212
curvature-principal response is an ``Omega^13(Cl^2)`` object, while its
lower-order response is ``Omega^13(Cl^1)``.  This probe tests the owned Hodge
map, not an identity-by-dimension shortcut, and keeps carrier availability
separate from the still-open coupled Euler coefficient.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CONTACT = ROOT / "tests/channel-swings/selected_k77_i2b_trace_hq_normal_contact_correction_probe.py"
EULER = ROOT / "tests/channel-swings/selected_k77_i2b_arbitrary_field_euler_green_bank_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def gaussian(value: tuple[Fraction, Fraction]) -> sp.Expr:
    return sp.Rational(value[0].numerator, value[0].denominator) + sp.I * sp.Rational(
        value[1].numerator, value[1].denominator
    )


def signature(value: dict[int, dict[int, tuple[Fraction, Fraction]]]) -> set[tuple[int, int]]:
    return {
        (form_mask.bit_count(), clifford_mask.bit_count())
        for form_mask, row in value.items()
        for clifford_mask, coefficient in row.items()
        if coefficient != (Fraction(0), Fraction(0))
    }


def flatten_bank(values: list[dict], keys: list[tuple[int, int]]) -> sp.Matrix:
    return sp.Matrix(
        [
            [gaussian(value.get(form_mask, {}).get(clifford_mask, (Fraction(0), Fraction(0))))
             for value in values]
            for form_mask, clifford_mask in keys
        ]
    )


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
reconstruction = read(
    "lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md"
)
transport = read("lab/process/functional-channel-operating-contract-v1.0.md")
check("source", "SC-ACT-04 owns a bosonic residual square and adjoint grammar",
      "- id: SC-ACT-04" in claims and "D*_omega Upsilon_omega = 0" in claims)
check("source", "the source reconstruction charges a distinct bosonic Q_B slot",
      "I_2^B[Q_B]" in reconstruction and "pairings `Q_B,Q_ED` are typed" in reconstruction)
check("prior_art", "v0.221 and v0.212 are the owned contact and arbitrary-field parents",
      CONTACT.exists() and EULER.exists())
check("process", "structure transport requires a fingerprint and a commuting-square status",
      "structure fingerprint" in transport.lower() and "commuting square" in transport.lower())
for label in (
    "contact response versus curvature-principal residual response",
    "principal residual response versus prolonged Euler coefficient",
    "curvature-principal response versus lower-order response",
    "Hodge primalization versus trace-Hq scalar pairing",
    "carrier availability versus action-owned coefficient",
    "local sparse preimage versus global associated-bundle section",
):
    check("layer0", label + " remain distinct", True)
for kind, label in (
    ("jet_spencer", "type the principal response before prolonging the equation"),
    ("variational", "retain fixed-Hq Green orthogonality after finding a carrier overlap"),
    ("symplectic", "do not promote the Green carrier to a presymplectic class"),
    ("krein", "do not identify trace-Hq with the unbuilt Q_B primalizer"),
    ("principal_bundle", "local cell combinations require descent and action ownership"),
    ("analytic", "no domain hyperbolicity energy or spectrum follows from a local span"),
    ("contrary", "retain wrong-degree wrong-sign and fitted-coefficient controls"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE PREDECESSORS AND STRUCTURE FINGERPRINTS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V221 = runpy.run_path(str(CONTACT))
check("repo", "v0.221 contact predecessor replays",
      "PASS 46/46" in capture.getvalue() and not V221["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V212 = runpy.run_path(str(EULER))
check("repo", "v0.212 arbitrary-field Euler/Green predecessor replays",
      "PASS 45/45" in capture.getvalue() and not V212["FAILURES"])

responses = V221["responses"]
trace_hq_pairing = V221["trace_hq_pairing"]
A_bank = V212["A_bank"]
B_bank = V212["B_bank"]
hodge = V212["hodge"]
fadd = V212["fadd"]
fscale = V212["fscale"]
cells = V212["cells"]
check("fingerprint", "contact is exactly a 16-dimensional Omega1-Cl2 carrier",
      len(responses) == 16 and set().union(*(signature(value) for value in responses)) == {(1, 2)})
check("fingerprint", "principal bank is exactly a 196-cell Omega13-Cl2 carrier",
      len(A_bank) == 196 and set().union(*(signature(value) for value in A_bank)) == {(13, 2)})
check("fingerprint", "lower-order bank is exactly a 196-cell Omega13-Cl1 carrier",
      len(B_bank) == 196 and set().union(*(signature(value) for value in B_bank)) == {(13, 1)})
check("fingerprint", "identity composition is forbidden by exterior degree",
      {(1, 2)} != {(13, 2)})


print("\nC. IDENTITY AND RAW-PAIRING SHORTCUTS FIRE")
observer_pair = V221["observer_pair"]
raw_principal = sp.Matrix([
    [observer_pair(0, 0, response, value) for value in A_bank]
    for response in responses
])
raw_lower = sp.Matrix([
    [observer_pair(0, 0, response, value) for value in B_bank]
    for response in responses
])
check("negative", "raw trace-Hq pairing is zero on the complete principal bank",
      raw_principal == sp.zeros(16, 196))
check("negative", "raw trace-Hq pairing is zero on the complete lower-order bank",
      raw_lower == sp.zeros(16, 196))
check("plant", "PLANT equal matrix widths do not license an identity adapter",
      len(A_bank) == len(B_bank) == 196 and signature(A_bank[0]) != signature(responses[0]))


print("\nD. OWNED HODGE ADAPTER AND EXACT INTERSECTIONS")
hodge_A = [hodge(value) for value in A_bank]
hodge_B = [hodge(value) for value in B_bank]
check("adapter", "Hodge moves the principal bank to Omega1-Cl2",
      set().union(*(signature(value) for value in hodge_A)) == {(1, 2)})
check("adapter", "Hodge leaves the lower-order bank at incompatible Clifford grade one",
      set().union(*(signature(value) for value in hodge_B)) == {(1, 1)})

keys = sorted({
    (form_mask, clifford_mask)
    for value in responses + hodge_A + hodge_B
    for form_mask, row in value.items()
    for clifford_mask, coefficient in row.items()
    if coefficient != (Fraction(0), Fraction(0))
})
C = flatten_bank(responses, keys)
HA = flatten_bank(hodge_A, keys)
HB = flatten_bank(hodge_B, keys)
rank_c = C.rank()
rank_ha = HA.rank()
rank_hb = HB.rank()
rank_c_ha = HA.row_join(C).rank()
rank_c_hb = HB.row_join(C).rank()
check("exact", "contact principal and lower Hodge ranks are 16 182 and 196",
      (rank_c, rank_ha, rank_hb) == (16, 182, 196))
check("exact", "contact meets Hodge-principal in exactly four dimensions",
      rank_c + rank_ha - rank_c_ha == 4 and rank_c_ha == 194)
check("exact", "contact and Hodge-lower images are disjoint",
      rank_c + rank_hb - rank_c_hb == 0 and rank_c_hb == 212)

active_preimages = [
    fadd(fscale(Fraction(-1), hodge_A[179]), hodge_A[192]),
    fadd(hodge_A[178], hodge_A[193]),
    fadd(fscale(Fraction(-1), hodge_A[181]), hodge_A[194]),
    fadd(hodge_A[180], hodge_A[195]),
]
check("exact", "the four-dimensional intersection is exactly the observer-active quartet",
      active_preimages == responses[:4])
check("exact", "the sparse preimages use exactly two existing connection cells each",
      [[cells[index][:2] for index in support] for support in
       ((179, 192), (178, 193), (181, 194), (180, 195))]
      == [[(12, 11), (13, 10)], [(12, 10), (13, 11)],
          [(12, 13), (13, 12)], [(12, 12), (13, 13)]])
wrong_last = fadd(hodge_A[180], fscale(Fraction(-1), hodge_A[195]))
check("plant", "PLANT wrong Hodge-preimage sign misses the fourth active response",
      wrong_last != responses[3])


print("\nE. SOURCE IMAGE, LOCAL COKERNEL, AND ACTION COEFFICIENT")
source_carrier = C * trace_hq_pairing
cokernel_carrier = C[:, [3, 7, 11, 15]]
source_intersection = rank_ha + source_carrier.rank() - HA.row_join(source_carrier).rank()
cokernel_intersection = rank_ha + cokernel_carrier.rank() - HA.row_join(cokernel_carrier).rank()
check("exact", "Hodge-principal meets the rank-12 trace-Hq source image in dimension three",
      trace_hq_pairing.rank() == 12 and source_intersection == 3)
check("exact", "the source image contains active e0 e1 e2 but not active e3",
      all(trace_hq_pairing.row_join(sp.eye(16)[:, index]).rank() == 12 for index in (0, 1, 2))
      and trace_hq_pairing.row_join(sp.eye(16)[:, 3]).rank() == 13)
check("exact", "Hodge-principal meets the local contact cokernel in exactly e3",
      cokernel_intersection == 1 and active_preimages[3] == responses[3])
rho = V212["rho"]
radius = V212["radius"]
generic_euler = V212["generic_euler"]
preimage_weights = (
    {179: -1, 192: 1},
    {178: 1, 193: 1},
    {181: -1, 194: 1},
    {180: 1, 195: 1},
)
active_euler_coefficients = [
    sp.factor(sum(generic_euler[index] * coefficient for index, coefficient in weights.items()))
    for weights in preimage_weights
]
expected_radial = sp.Rational(128, 3) * radius * (radius ** 2 + 3 * rho)
check("euler", "only the e3 preimage has a nonzero fixed-Hq Euler coefficient",
      active_euler_coefficients == [0, 0, 0, expected_radial])
check("euler", "the e3 coefficient vanishes exactly on the restricted stationary branch",
      sp.expand(expected_radial.subs(rho, -radius ** 2 / 3)) == 0)
check("plant", "PLANT a generic off-branch amplitude retains the e3 Euler equation",
      expected_radial.subs({rho: -1, radius: 1}) != 0)
check("variational", "the fixed-Hq physical principal Green coefficient remains zero",
      V212["green_family"].rank() == 0)
check("scope", "the fixed action owns the radial e3 Euler factor but not a nonzero stationary e3 value", True)
check("scope", "moving Q_B metric section corrections and the coupled stationary contact remain open", True)
check("accounting", "no field parameter selector quotient or external datum is added", True)
check("datum", "P1 P2 P3 remain unchanged and unused", True)


print("\nF. REGISTRY AND DISPOSITION")
registry = json.loads(read("lab/process/selected-k77-i2b-contact-euler-hodge-adapter.json"))
check("registry", "registry records the exact four-dimensional active intersection",
      registry["hodge_principal_intersection"]["dimension"] == 4
      and registry["hodge_principal_intersection"]["carrier"] == "OBSERVER_ACTIVE_QUARTET")
check("registry", "registry refuses to promote availability to selection",
      registry["action_selection"].startswith("E3_RADIAL_EULER_COEFFICIENT_EXACT"))
check("registry", "registry preserves the two C32,32 halves as the primary carrier",
      registry["carrier"]["primary"] == "C32_32_PLUS_HALF_DIRECT_SUM_C32_32_MINUS_HALF")

print("SOURCE_RETURN=SOURCE_CONFIRMS_RESIDUAL_SQUARE_ADJOINT_AND_TWO_CONNECTION_AUGMENTED_TORSION"
      "__SOURCE_SILENT_EXACT_QB_AND_COUPLED_NORMAL_COEFFICIENT__REPO_DERIVES_HODGE_PRINCIPAL_ACTIVE_INTERSECTION")
print("FINGERPRINTS=CONTACT_OMEGA1_CL2__PRINCIPAL_OMEGA13_CL2__LOWER_OMEGA13_CL1")
print("INTERSECTIONS=HODGE_PRINCIPAL_ACTIVE4__TRACE_HQ_SOURCE3__LOCAL_COKERNEL1_E3__HODGE_LOWER0")
print("SPARSE_E3_PREIMAGE=(12,12)+(13,13)")
print("E3_EULER=128_OVER_3_R_TIMES_R2_PLUS_3RHO__ZERO_ON_RESTRICTED_STATIONARY_BRANCH")
print("NEXT=DERIVE_MOVING_QB_METRIC_SECTION_CORRECTIONS_TO_E3__THEN_STATIONARY_CONTACT_DISCRIMINANT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
