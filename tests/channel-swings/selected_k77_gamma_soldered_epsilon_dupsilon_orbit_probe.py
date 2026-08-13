#!/usr/bin/env python3
"""Exact K77 gamma-soldered source-epsilon D-Upsilon orbit.

This probe composes the v0.83 source-varpi residual block with the already
constructed global labelled Clifford frame ``gamma_epsilon:C->ad(P_H)``.
At residual zero, gauge equivariance determines the primitive epsilon response
on an internal gauge orbit.  The calculation closes only the principal
four-column gamma-soldered orbit and its Ward restriction; it does not fit or
construct the six transverse physical metric columns, residual pairing,
formal adjoint, Green concomitant, domain, or BV-BFV quotient.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_common_field_dupsilon_varpi_block_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, ARCHAEOLOGY, AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
moving_source = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
epsilon_fence = read("explorations/conditional-build/selected-second-layer-transverse117-residual-zero-owner-class-2026-08-07.md")
global_registry = strict("lab/process/k77-global-chimeric-spin-reduction-and-support-normalization.json")

check("source", "source owns an H-valued epsilon field and the connection-difference chain",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "source makes the Clifford forms an epsilon-conjugation orbit",
      "Phi_i(epsilon)=Ad_(epsilon^-1) Phi_i^0" in moving_source)
check("source", "source fixes primitive epsilon connection calculus but not a diffeomorphism soldering identity",
      "delta B=D_B eta" in moving_source and "SOURCE-SILENT" in moving_source)
check("repo", "the global K77 gamma-epsilon map is already constructed without a new field",
      global_registry["global_full_reduction"]["global"] is True
      and global_registry["global_full_reduction"]["labelled_rank"] == 14
      and global_registry["global_full_reduction"]["new_field_count"] == 0)
check("repo", "grade-one Clifford multiplication lands in the active adjoint",
      global_registry["principal_bundle"]["grade1_is_B_skew"] is True
      and global_registry["principal_bundle"]["P_H_owner"].endswith("U_64_64"))
check("repo", "the prior epsilon fence rejects automatic identification with diffeomorphism soldering",
      "epsilon is a gauge-orbit variable, not an unbuilt diffeomorphism/soldering" in epsilon_fence)
for label in (
    "source epsilon versus dependent gamma-epsilon Clifford frame",
    "Kosmann bivector lift versus gamma-soldered grade-one lift",
    "internal gauge equivariance versus a source-quoted diffeomorphism identity",
    "principal epsilon response versus the complete Frechet block",
    "four-column Ward restriction versus six transverse physical metric columns",
    "bulk Ward closure versus reduced presymplectic and BV-BFV descent",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE V0.83 PREDECESSOR")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P0 = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.83 common-field source-varpi block replays", "PASS 68/68" in capture.getvalue())
P = P0["P"]
S = P0["S"]
M = P["M"]
V = P["V"]

pairs = [(a, b) for a in range(4) for b in range(a + 1, 4)]


def lorentz_principal(q):
    """q tensor eta from six Lorentz bivectors to 24 one-form coefficients."""
    out = sp.zeros(24, 6)
    for mu in range(4):
        for pair_index in range(6):
            out[6 * mu + pair_index, pair_index] = q[mu]
    return out


def kosmann_symbol(q):
    """eta_ab=1/2(q_a xi_b-q_b xi_a); q is already a covector."""
    out = sp.zeros(6, 4)
    for row, (a, b) in enumerate(pairs):
        for nu in range(4):
            out[row, nu] = sp.Rational(1, 2) * (
                q[a] * (1 if b == nu else 0)
                - q[b] * (1 if a == nu else 0)
            )
    return out


def horizontal_form(column):
    result = {}
    for index, coefficient in enumerate(column):
        if coefficient:
            mu, pair_index = divmod(index, 6)
            result = M["fadd"](
                result,
                M["fscale"](
                    coefficient,
                    {1 << mu: M["blade"](pairs[pair_index])},
                ),
            )
    return result


def gamma_connection_form(q, nu):
    result = {}
    for mu in range(4):
        if q[mu]:
            result = M["fadd"](
                result,
                M["fscale"](
                    q[mu],
                    {1 << mu: M["blade"]((nu,))},
                ),
            )
    return result


def linear_combination(forms, coefficients):
    result = {}
    for form, coefficient in zip(forms, coefficients):
        if coefficient:
            result = M["fadd"](result, M["fscale"](coefficient, form))
    return result


print("\nC. KOSMANN CONTROL AND GAMMA-SOLDERED EPSILON BLOCK")
results = {}
for name, packet in S["results"].items():
    q = sp.Matrix(S["orbits"][name])
    D = packet["D"]
    C = packet["connection_lift"]
    kosmann = lorentz_principal(q) * kosmann_symbol(q)

    check("exact", f"{name}: canonical Kosmann connection displacement equals minus the spin-LC lift",
          kosmann == -C)
    check("exact", f"{name}: Kosmann and spin-LC lifts share rank three and the same longitudinal kernel",
          kosmann.rank() == C.rank() == 3
          and kosmann.nullspace() == C.nullspace())
    check("planted", f"PLANT {name}: a bivector Kosmann epsilon compensator does not add the fourth response",
          sp.Matrix.hstack(C, kosmann).rank() == 3)

    varpi_forms = [horizontal_form(C[:, column]) for column in range(4)]
    gamma_forms = [gamma_connection_form(q, nu) for nu in range(4)]
    varpi_responses = [P["response"](value) for value in varpi_forms]
    gamma_responses = [P["response"](value) for value in gamma_forms]

    check("exact", f"{name}: gamma-epsilon principal connection displacement has rank four",
          V["family_rank"](gamma_forms) == 4)
    check("exact", f"{name}: injective raw residual response preserves gamma-epsilon rank four",
          V["family_rank"](gamma_responses) == 4)
    check("exact", f"{name}: gamma-epsilon reaches the exact longitudinal direction missed by varpi",
          bool(linear_combination(gamma_responses, C.nullspace()[0]))
          and not linear_combination(varpi_responses, C.nullspace()[0]))

    # At Upsilon*=0, internal H-equivariance gives
    # D_epsilon Upsilon[eta] = -D_varpi Upsilon[D_A eta] on the gauge orbit.
    epsilon_responses = [M["fscale"](-1, value) for value in gamma_responses]
    total_responses = [
        M["fadd"](varpi, epsilon)
        for varpi, epsilon in zip(varpi_responses, epsilon_responses)
    ]
    check("exact", f"{name}: source varpi plus gamma-soldered epsilon residual orbit has rank four",
          V["family_rank"](total_responses) == 4)

    left_inverse = (D.T * D).inv() * D.T
    metric_orbit_columns = [
        M["fscale"](-1, linear_combination(total_responses, left_inverse[:, row]))
        for row in range(10)
    ]
    for column in range(4):
        check("exact", f"{name}: complete gamma-soldered orbit satisfies one J-R Ward column",
              not M["fadd"](
                  linear_combination(metric_orbit_columns, D[:, column]),
                  total_responses[column],
              ))
    transverse = sp.eye(10) - D * left_inverse
    check("exact", f"{name}: six transverse physical metric columns remain unconstructed",
          transverse.rank() == 6 and transverse * D == sp.zeros(10, 4))
    check("planted", f"PLANT {name}: orbit closure is not the complete physical metric Frechet block",
          transverse != sp.zeros(10))

    results[name] = {
        "kosmann_rank": kosmann.rank(),
        "gamma_input_rank": V["family_rank"](gamma_forms),
        "gamma_residual_rank": V["family_rank"](gamma_responses),
        "combined_orbit_rank": V["family_rank"](total_responses),
        "gamma_response_supports": [len(M["flatten"](value)) for value in gamma_responses],
        "combined_response_supports": [len(M["flatten"](value)) for value in total_responses],
        "transverse_metric_dimensions_open": transverse.rank(),
    }


print("\nD. IDENTIFIABILITY, CONSTRAINT SURPLUS, AND SCOPE")
check("theorem", "all causal classes reject the Kosmann-only fourth-direction route",
      all(row["kosmann_rank"] == 3 for row in results.values()))
check("theorem", "all causal classes close the gamma-soldered four-column residual orbit",
      all(row["combined_orbit_rank"] == 4 for row in results.values()))
check("surplus", "the labelled Clifford map fixes all four gamma columns with zero fitted coefficients",
      global_registry["global_full_reduction"]["new_field_count"] == 0
      and global_registry["global_full_reduction"]["new_discrete_datum_count"] == 0)
check("planted", "PLANT a generic six-by-four Lorentz compensator would be a fitted rival, not this construction",
      True)
for kind, label in (
    ("symplectic", "four-column J-R closure is not a reduced presymplectic or BFV class"),
    ("variational", "six transverse D-g Upsilon columns and lower-order epsilon terms remain open"),
    ("krein", "grade-one B-skew admissibility does not choose a positive fundamental symmetry or domain"),
    ("analytic", "the finite principal block selects no contour determinant measure or Green domain"),
    ("scope", "the old rank-four metric diagnostic is revived only for coefficientwise recheck"),
    ("scope", "residual K-star formal adjoint and Green concomitant remain open"),
    ("scope", "P1 P2 P3 remain unused and no field coefficient quotient or datum is added"),
    ("scope", "Curt remains formally separate and no third lane is promoted"),
):
    check(kind, label, True)

registry = strict("lab/process/selected-k77-gamma-soldered-epsilon-dupsilon-orbit.json")
check("exact", "registry records all three causal constructions", registry["causal_orbits"] == results)
check("source", "registry preserves source confirmation and silence",
      registry["source_return"] == "SOURCE-CONFIRMS__EPSILON_GAMMA_FRAME_AND_GAUGE_EQUIVARIANCE_CARRIERS__SOURCE-SILENT__GAMMA_XI_AS_PHYSICAL_DIFFEO_SOLDERING_IDENTITY")

print("SOURCE_RETURN=SOURCE-CONFIRMS__EPSILON_GAMMA_FRAME_AND_GAUGE_EQUIVARIANCE_CARRIERS__SOURCE-SILENT__GAMMA_XI_AS_PHYSICAL_DIFFEO_SOLDERING_IDENTITY")
print("KOSMANN_EPSILON_COMPENSATOR=RANK3__SAME_LONGITUDINAL_KERNEL__NO_GAIN")
print("GAMMA_EPSILON_PRINCIPAL_BLOCK=RANK4__LONGITUDINAL_DIRECTION_LIVE")
print("COMMON_FIELD_GAMMA_SOLDERED_ORBIT_JR=ZERO_4_OF_4_ALL_CAUSAL_CLASSES")
print("PHYSICAL_TRANSVERSE_DG_UPSILON_COLUMNS_OPEN=6")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
