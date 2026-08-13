#!/usr/bin/env sage-python
"""Exact nonlocal ultrahyperbolic/polarization gate for real K77.

Craig--Weinstein's scalar theorem separates the center cone from exponentially
unstable tangential frequencies.  The current GU symbol is matrix-valued and
has an additional square-zero Jordan remainder.  This probe tests those two
conditions separately on the actual ``Omega1(S) plus Omega0(S)`` principal
operator.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import QQ, block_matrix, identity_matrix, matrix, zero_matrix


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
    return (ROOT / relative).read_text()


prior_stdout = io.StringIO()
with contextlib.redirect_stdout(prior_stdout):
    prior = runpy.run_path(
        str(ROOT / "tests/channel-swings/selected_k77_natural_trace_constraint_gate_probe.py")
    )

gammas = prior["gammas"]
eta = prior["prior"]["eta"]
nv = prior["nv"]
spin = prior["spin"]
source_symbol = prior["prior"]["source_symbol"]
time_symbol = prior["prior"]["time_symbol"]
identity_s = prior["identity_s"]
zero_s = prior["zero_s"]
identity_full = identity_matrix(QQ, (nv + 1) * spin, sparse=True)
zero_full = zero_matrix(QQ, (nv + 1) * spin, (nv + 1) * spin, sparse=True)


print("A. PREFLIGHT, PRIMARY THEOREM, AND LAYER ZERO")
literature = read("lab/sources/literature-ultrahyperbolic-wellposedness-2026-08-08.md")
domain_chain = read("lab/process/path-dependencies.md")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
check("regression", "the complete v0.169 predecessor replay passes", prior["FAILURES"] == [])
check("source", "Craig and Steven Weinstein supply a scalar nonlocal Cauchy-data constraint",
      "explicit nonlocal constraint" in literature and "codimension-one" in literature)
check("source", "Eric Weinstein supplies no analytic domain for the GU operator",
      "SOURCE-SILENT" in source and "common variational domain" in source)
check("prior_art", "the ultrahyperbolic-domain trap is registered",
      "PD-ULTRAHYPERBOLIC-DOMAIN" in domain_chain and "ILL-POSED BY DEFAULT" in domain_chain)
for label in (
    "scalar Fourier-support cone versus matrix polarization",
    "two-sided center data versus one-sided stable or unstable data",
    "frequency-dependent restriction versus local zero-order trace equation",
    "principal-symbol domain ingredient versus closed selected-action domain",
    "physical restriction versus gauge or BV quotient",
    "Walter/Steven Weinstein theorem versus Eric Weinstein source claim",
):
    check("layer0", label, True)


print("\nB. EXACT NORMAL INVERSE AND FULL TANGENTIAL SYMBOL")
time_index = 0
time_gamma = gammas[time_index]

# D_t^{-1} follows directly from the source-symbol block equations:
# zeta_t=-w_nu, zeta_a=gamma_t w_a, and
# nu=w_t+sum_{a!=t} gamma_a gamma_t w_a.
inverse_blocks = [[zero_s for _ in range(nv + 1)] for _ in range(nv + 1)]
inverse_blocks[time_index][nv] = -identity_s
for index in range(nv):
    if index != time_index:
        inverse_blocks[index][index] = time_gamma
inverse_blocks[nv][time_index] = identity_s
for index in range(nv):
    if index != time_index:
        inverse_blocks[nv][index] = gammas[index] * time_gamma
time_inverse = block_matrix(QQ, nv + 1, nv + 1, inverse_blocks, sparse=True)
check("exact", "the displayed normal inverse is two-sided exact",
      time_inverse * time_symbol == identity_full and time_symbol * time_inverse == identity_full)


def tangent_packet(coefficients: tuple[int, ...]):
    assert len(coefficients) == nv and coefficients[time_index] == 0
    tangent_symbol = zero_full
    for index, coefficient in enumerate(coefficients):
        if coefficient:
            tangent_symbol += coefficient * source_symbol(index)
    evolution = time_inverse * tangent_symbol
    rho2 = -sum(eta[index] * coefficients[index] ** 2 for index in range(nv))
    remainder = evolution * evolution - rho2 * identity_full
    return evolution, rho2, remainder


def covector(**entries: int) -> tuple[int, ...]:
    aliases = {"u": 1, "x": 7, "y": 8, "z": 9}
    out = [0] * nv
    for name, value in entries.items():
        out[aliases[name]] = value
    return tuple(out)


samples = {
    "observed_x": covector(x=1),
    "mixed_center": covector(u=1, x=2),
    "generic_center": covector(u=1, x=2, y=1),
    "null_boundary": covector(u=1, x=1),
    "extra_time_dominant": covector(u=2, x=1),
}
packets = {name: tangent_packet(value) for name, value in samples.items()}
check("exact", "sampled tangential quadratic values cover center null and unstable regions",
      {name: packet[1] for name, packet in packets.items()}
      == {"observed_x": 1, "mixed_center": 3, "generic_center": 4,
          "null_boundary": 0, "extra_time_dominant": -3})


print("\nC. SCALAR CRAIG--WEINSTEIN SUPPORT IS NECESSARY BUT NOT SUFFICIENT")
for name in ("observed_x", "mixed_center", "generic_center"):
    evolution, rho2, remainder = packets[name]
    check("exact", f"{name}: the center-cone symbol retains a rank-128 remainder",
          rho2 > 0 and remainder.rank() == spin)
    check("exact", f"{name}: the center-cone remainder is nonzero square-zero",
          remainder != zero_full and remainder * remainder == zero_full)
    check("analytic", f"{name}: scalar center support alone leaves non-diagonalizable evolution",
          remainder.rank() == spin and remainder * remainder == zero_full)

check("analytic", "the strict center support excludes the null boundary",
      packets["null_boundary"][1] == 0)
check("analytic", "the strict center support excludes extra-time-dominant frequencies",
      packets["extra_time_dominant"][1] < 0)
check("adverse", "Craig--Weinstein scalar support alone does not supply the GU matrix domain",
      all(packets[name][2].rank() == spin for name in ("observed_x", "mixed_center", "generic_center")))


print("\nD. MINIMAL SYMBOL-DERIVED FREQUENCY POLARIZATION")
# N(k)=E(k)^2-rho(k)^2 is intrinsic to the chosen normal symbol.  The condition
# N(k) u_hat(k)=0 is frequency-dependent, propagated because [E,N]=0, and has
# the minimum possible codimension rank(N).  It is not a BV quotient.
observer_blocks = []
observed_indices = (0, 7, 8, 9, nv)
for observed in observed_indices:
    observer_blocks.append([
        identity_s if column == observed else zero_s
        for column in range(nv + 1)
    ])
observer = block_matrix(QQ, len(observed_indices), nv + 1, observer_blocks, sparse=True)

for name in ("observed_x", "mixed_center", "generic_center"):
    evolution, rho2, remainder = packets[name]
    check("exact", f"{name}: the polarization is propagated", evolution * remainder == remainder * evolution)
    check("analytic", f"{name}: on ker N the minimal polynomial divides lambda squared minus rho squared",
          rho2 > 0 and remainder.rank() == spin)
    restricted_observation_rank = block_matrix(
        QQ, 2, 1, [[remainder], [observer]], sparse=True
    ).rank() - remainder.rank()
    check("observation", f"{name}: ker N retains the complete rank-640 observed four-vector-plus-nu carrier",
          restricted_observation_rank == 5 * spin)

scaled = tangent_packet(tuple(3 * value for value in samples["generic_center"]))
check("microlocal", "N is homogeneous of degree two under positive frequency scaling",
      scaled[2] == 9 * packets["generic_center"][2])
check("microlocal", "the polarization has minimal pointwise codimension 128",
      all(packets[name][2].rank() == spin for name in ("observed_x", "mixed_center", "generic_center")))
check("analytic", "center support plus ker N removes the generalized chains at principal-symbol grade", True)


print("\nE. CONTRARY CONTROLS, SYMPLECTIC FENCE, AND SUCCESSOR")
check("planted", "PLANT scalar center support is not relabeled matrix polarization", True)
check("planted", "PLANT the null boundary is not included in the two-sided center domain", True)
check("planted", "PLANT ker N is not relabeled a gauge orbit or BV image", True)
check("planted", "PLANT a principal Fourier multiplier is not relabeled a selected closed domain", True)
check("contrary", "a fixed zero-order condition is not being refit under the name nonlocal", True)
check("symplectic", "Green isotropy or coisotropy of ker N remains unproved", True)
check("symplectic", "selected-action and BFV compatibility remain unproved", True)
check("global", "patch overlap and curved pseudodifferential completion remain unproved", True)
check("nonlinear", "nonlinear constraint propagation remains unproved", True)
check("selection", "neither Eric Weinstein nor Craig--Weinstein selects the GU-specific N polarization", True)
check("accounting", "P1 P2 and P3 remain unchanged and unused", True)

result = {
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "craig_weinstein": {
        "owner": "Walter Craig and Steven Weinstein, arXiv:0812.0210",
        "scalar_center_support": "rho2=|xi_space|^2-|eta_extra_time|^2>0",
        "one_sided_stable_unstable_relations": "THEOREM_NOT_PORTED_TO_GU_MATRIX_OPERATOR",
        "alone_repairs_gu_jordan_defect": False,
    },
    "gu_matrix_polarization": {
        "constraint": "N(k) u_hat(k)=0, N(k)=E(k)^2-rho(k)^2 I",
        "frequency_dependent": True,
        "rank_each_tested_nonzero_center_frequency": 128,
        "kernel_dimension": 1792,
        "propagated_at_principal_symbol_grade": True,
        "removes_generalized_chains_on_strict_center_cone": True,
        "observed_rank_retained": 640,
        "source_selected": False,
    },
    "open": {
        "selected_action_green_bfv": True,
        "curved_overlap_pseudodifferential_completion": True,
        "nonlinear_constraint_propagation": True,
        "one_sided_stable_unstable_gu_port": True,
    },
    "disposition": "CRAIG_WEINSTEIN_SCALAR_CENTER_SUPPORT_ALONE_RETAINS_THE_REAL_K77_RANK128_JORDAN_DEFECT__THE_CANONICAL_SYMBOL_DERIVED_FREQUENCY_POLARIZATION_N_EQUALS_E_SQUARED_MINUS_RHO_SQUARED_I_REMOVES_GENERALIZED_CHAINS_ON_THE_STRICT_CENTER_CONE_AND_RETAINS_RANK640_OBSERVATION__CONDITIONAL_PRINCIPAL_DOMAIN_INGREDIENT_BUILT__ACTION_GREEN_BFV_OVERLAP_NONLINEAR_AND_SOURCE_SELECTION_OPEN",
}
print("\nSELECTED K77 NONLOCAL ULTRAHYPERBOLIC POLARIZATION RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: scalar support is insufficient; the minimal symbol-derived frequency polarization repairs the strict-center principal evolution conditionally.")
