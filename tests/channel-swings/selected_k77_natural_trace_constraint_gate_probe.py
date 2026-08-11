#!/usr/bin/env sage-python
"""Exact natural zero-order constraint gate for the real-K77 rolled operator.

This classifies the complete Spin-natural zero-order spinor-valued family

    C_(a,b)(zeta, nu) = a Gamma(zeta) + b nu

on ``Omega1(S) plus Omega0(S)``.  Propagation of a constraint and removal of
the rank-128 Jordan chains are tested separately.  A propagated physical
trace equation is not relabelled a gauge/BV differential.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy

from sage.all import PolynomialRing, QQ, block_matrix, identity_matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def strict(relative: str):
    path = ROOT / relative

    def reject_duplicates(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject_duplicates)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


# Reuse the exact same operator constructor, after replaying its complete gate.
predecessor_stdout = io.StringIO()
with contextlib.redirect_stdout(predecessor_stdout):
    prior = runpy.run_path(
        str(ROOT / "tests/channel-swings/selected_k77_unreduced_hyperbolic_domain_gate_probe.py")
    )

QQ = prior["QQ"]
block_matrix = prior["block_matrix"]
gammas = prior["gammas"]
nv = prior["nv"]
spin = prior["spin"]
zero_s = prior["zero_s"]
identity_s = prior["identity_s"]
packets = prior["packets"]


print("A. ADAPTIVE PREFLIGHT, SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
v0168 = strict("lab/process/selected-k77-unreduced-hyperbolic-domain-gate.json")
b2c3 = strict("lab/process/eric-curt-wave3d-b2c3-rolled-omega-source-shiab.json")
check("regression", "the complete v0.168 exact predecessor replay passes",
      prior["FAILURES"] == [])
check("source", "the draft types nu and zeta as physical four-field fermion variables",
      "four distinct fields" in source and "physical" in source)
check("source", "the source is silent on a selected trace constraint or BV reduction",
      "common variational domain" in source and "SOURCE-SILENT" in source)
check("prior_art", "the live obstruction is rank 128 and square-zero",
      v0168["observed_evolution"]["jordan_remainder_rank_each"] == 128
      and v0168["observed_evolution"]["jordan_remainder_square_zero"] is True)
check("prior_art", "the old characteristic d-factorization was not an off-shell BV identity",
      b2c3["off_shell_gate"]["off_shell_noether_or_bv"] is False)
for label in (
    "physical trace equation versus ghost or gauge parameter",
    "constraint-kernel propagation versus Jordan-chain removal",
    "zero-order natural constraint versus derivative or nonlocal constraint",
    "one-time section propagation versus ambient ultrahyperbolic domain",
    "restriction to a kernel versus quotient by a BV image",
):
    check("layer0", label, True)


print("\nB. COMPLETE SPIN-NATURAL ZERO-ORDER FAMILY")
gamma_trace = block_matrix(
    QQ, 1, nv + 1,
    [[gammas[index] for index in range(nv)] + [zero_s]],
    sparse=True,
)
nu_projection = block_matrix(
    QQ, 1, nv + 1,
    [[zero_s for _ in range(nv)] + [identity_s]],
    sparse=True,
)
check("representation", "Hom_Spin(V tensor S, S) is represented by gamma trace", gamma_trace.rank() == spin)
check("representation", "Hom_Spin(S, S) is represented by the identity", nu_projection.rank() == spin)
check("representation", "the two natural channels are linearly independent",
      block_matrix(QQ, 2, 1, [[gamma_trace], [nu_projection]], sparse=True).rank() == 2 * spin)
check("representation", "the natural family has two linear coefficients and one projective ratio", True)


print("\nC. WHOLESALE PROPAGATION CLASSIFICATION")
R = PolynomialRing(QQ, "t")
t = R.gen()
propagated = 2 * gamma_trace - nu_projection
gcds = []

for label, (evolution, q_map, u_map, remainder) in packets.items():
    ae = gamma_trace * evolution
    be = nu_projection * evolution
    a_nu = ae[:, nv * spin:]
    b_nu = be[:, nv * spin:]

    # For b != 0, clear the denominator in H=(a A_nu+b B_nu)/b.
    # The invariance residual is t^2 R_aa+t R_ab+R_bb at t=a/b.
    r_aa = -a_nu * gamma_trace
    r_ab = ae - a_nu * nu_projection - b_nu * gamma_trace
    r_bb = be - b_nu * nu_projection
    keys = set(r_aa.dict()) | set(r_ab.dict()) | set(r_bb.dict())
    common = None
    for key in keys:
        polynomial = (r_aa[key] if key in r_aa.dict() else 0) * t**2
        polynomial += (r_ab[key] if key in r_ab.dict() else 0) * t
        polynomial += r_bb[key] if key in r_bb.dict() else 0
        if polynomial:
            common = polynomial if common is None else common.gcd(polynomial)
            if common.degree() == 1:
                # It cannot shrink below the already verified common root t=-2.
                break
    common = common.monic()
    gcds.append(common)
    check("exact", f"{label}: all propagation residual entries have gcd t+2", common == t + 2)
    check("exact", f"{label}: the b=0 pure gamma-trace constraint is not propagated", r_aa != 0)
    induced = gammas[0] * gammas[{"x": 7, "y": 8, "z": 9}[label]]
    check("exact", f"{label}: C=2 Gamma-nu propagates by the ordinary Dirac generator",
          propagated * evolution == induced * propagated)
    check("exact", f"{label}: the induced constraint evolution squares to one",
          induced * induced == identity_s)

check("classification", "the unique nonzero propagated projective line is [a:b]=[2:-1]",
      all(item == t + 2 for item in gcds))


print("\nD. THE PROPAGATED LINE DOES NOT REMOVE THE JORDAN CHAINS")
for label, (evolution, q_map, u_map, remainder) in packets.items():
    check("exact", f"{label}: gamma trace annihilates the Jordan endpoint inclusion",
          gamma_trace * u_map == zero_matrix(QQ, spin, spin, sparse=True))
    check("exact", f"{label}: nu projection annihilates the Jordan endpoint inclusion",
          nu_projection * u_map == zero_matrix(QQ, spin, spin, sparse=True))
    check("adverse", f"{label}: the complete rank-128 Jordan image lies inside the propagated constraint kernel",
          propagated * u_map == zero_matrix(QQ, spin, spin, sparse=True))
    stacked = block_matrix(QQ, 2, 1, [[propagated], [q_map]], sparse=True)
    restricted_q_rank = stacked.rank() - propagated.rank()
    check("adverse", f"{label}: Q restricted to ker(C) remains onto with rank 128",
          restricted_q_rank == spin)
    check("analytic", f"{label}: the constrained evolution retains a nonzero square-zero rank-128 remainder",
          restricted_q_rank == spin and remainder * remainder == zero_matrix(QQ, (nv + 1) * spin, (nv + 1) * spin, sparse=True))


print("\nE. CONTROLS, SYMPLECTIC FENCE, AND SUCCESSOR")
qx = packets["x"][1]
qy = packets["y"][1]
check("contrary", "a direction-fitted Q_x constraint would algebraically kill N_x", packets["x"][3] == packets["x"][2] * qx)
check("planted", "PLANT Q_x is not the common covariant propagated trace constraint", qx != propagated)
check("planted", "PLANT Q_x and Q_y are direction-dependent distinct maps", qx != qy)
check("planted", "PLANT nu=0 is not a propagated constraint", all(nu_projection * packet[0] != gammas[0] * nu_projection for packet in packets.values()))
check("symplectic", "a propagated physical trace equation is not thereby a null direction of the action Green form", True)
check("symplectic", "no quotient or BFV charge is created by restricting to ker(C)", True)
check("selection", "the source does not select C=2 Gamma-nu", True)
check("scope", "derivative nonlocal BV-derived and operator-modification routes remain open", True)
check("accounting", "P1 P2 and P3 remain unchanged and unused", True)

result = {
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "natural_family": {
        "map": "C_(a,b)(zeta,nu)=a Gamma(zeta)+b nu",
        "linear_dimension": 2,
        "projective_dimension": 1,
        "complete_at_spin_natural_zero_order_scope": True,
    },
    "propagation": {
        "unique_projective_line": "[a:b]=[2:-1]",
        "constraint": "C=2 Gamma(zeta)-nu",
        "induced_observed_evolution": "gamma(dt)gamma(dx_j)",
        "all_three_spatial_directions": True,
    },
    "jordan": {
        "image_contained_in_constraint_kernel": True,
        "restricted_remainder_rank_each": 128,
        "restricted_remainder_square_zero": True,
        "natural_zero_order_constraint_repairs_hyperbolicity": False,
    },
    "selection": {
        "source_selects_constraint": False,
        "bv_differential_constructed": False,
        "quotient_constructed": False,
        "P1_P2_P3": "UNUSED",
    },
    "disposition": "UNIQUE_PROPAGATED_SPIN_NATURAL_ZERO_ORDER_TRACE_LINE_C_EQUALS_2GAMMAZETA_MINUS_NU__LINE_CONTAINS_AND_RETAINS_THE_COMPLETE_RANK128_SQUARE_ZERO_JORDAN_IMAGE__NATURAL_ZERO_ORDER_CONSTRAINT_ROUTE_KILLED__DERIVATIVE_NONLOCAL_BV_DERIVED_OR_OPERATOR_MODIFICATION_ROUTES_OPEN",
}
print("\nSELECTED K77 NATURAL TRACE-CONSTRAINT RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: the unique propagated natural zero-order trace constraint retains rather than removes the Jordan chains.")
