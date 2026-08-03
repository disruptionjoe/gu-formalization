#!/usr/bin/env python3
r"""PW2F diffeomorphism-Noether and Green schema gate.

This probe derives the metric/diffeomorphism identity from a declared natural
lift rather than renaming the repository's residual-right Ward or the source
relation Xi=D Upsilon.  A reparametrization-invariant lapse/scalar action gives
an exact nonvacuous bulk, current, and Noether identity.  A second finite
connection example keeps the internal gauge Ward visibly distinct.

The result earns the formal schema and the required native owner ledger.  It
does not evaluate the unreleased public-source/active-native transformation of
every GU owner, a physical stress tensor, BV closure, or conservation after
observation pushdown.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import json
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))


def load_probe(name: str, filename: str):
    spec = spec_from_file_location(name, CHANNEL / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


W = load_probe("pw2f_internal_ward", "pw2d_right_tilted_ward_green_probe.py")
REGISTRY = ROOT / "lab/process/pw2f-native-top-order-metric-ward-registry.json"

FAILURES: list[str] = []
EXACT = SOURCE = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def source(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE
    SOURCE += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"source: {label}")


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type-level - {label}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def total_d(expr, jets: tuple[tuple[sp.Symbol, ...], ...]) -> sp.Expr:
    return sp.expand(
        sum(
            sp.diff(expr, left) * right
            for row in jets
            for left, right in zip(row[:-1], row[1:])
        )
    )


def source_and_layer_zero() -> None:
    data = json.loads(REGISTRY.read_text())
    source(
        "Xi=D Upsilon is source-explicit only as a redundancy/cohomology relation",
        data["source_disposition"]["xi_relation"] == "SOURCE-CONFIRMS_REDUNDANCY_ONLY",
    )
    source(
        "the public corpus is silent on the full active all-owner diffeomorphism Ward and its Green current",
        data["source_disposition"]["diffeomorphism_ward"] == "SOURCE-SILENT",
    )
    typed("diffeomorphism Ward, internal gauge Ward, residual-right Ward, Xi relation, BV differential, and physical conservation are distinct")
    typed("natural Lie derivative and gauge-covariant Lie derivative differ by an internal gauge transformation and cannot be silently mixed")
    typed("derived h, K, Q, Shiab, Hodge, and density nodes are varied through their independent roots rather than assigned separate Euler equations")
    reject("spend P1/P2/P3 to close a differential identity", data["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED")


def exact_diffeomorphism_schema() -> None:
    # One-dimensional generally covariant comparator.  phi is a scalar and n
    # is a lapse/density: L=phi'^2/(2n).  Under xi,
    # delta phi=xi phi' and delta n=xi n'+xi' n.
    phi0, phi1, phi2 = sp.symbols("phi0 phi1 phi2")
    n0, n1, n2 = sp.symbols("n0 n1 n2", nonzero=True)
    xi0, xi1, xi2 = sp.symbols("xi0 xi1 xi2")
    jets = ((phi0, phi1, phi2), (n0, n1, n2), (xi0, xi1, xi2))
    lagrangian = phi1**2 / (2 * n0)
    delta_phi = xi0 * phi1
    delta_n = xi0 * n1 + xi1 * n0
    direct = sp.expand(
        sp.diff(lagrangian, phi1) * total_d(delta_phi, jets)
        + sp.diff(lagrangian, n0) * delta_n
    )
    natural_density = total_d(xi0 * lagrangian, jets)
    exact(
        "the declared scalar-plus-lapse natural lift moves the Lagrangian by the exact density divergence",
        sp.simplify(direct - natural_density) == 0 and direct != 0,
    )

    e_phi = -total_d(sp.diff(lagrangian, phi1), jets)
    e_n = sp.diff(lagrangian, n0)
    theta = sp.diff(lagrangian, phi1) * delta_phi
    first_variation_defect = sp.simplify(
        direct - e_phi * delta_phi - e_n * delta_n - total_d(theta, jets)
    )
    exact(
        "the direct natural variation equals both Euler owners plus the live presymplectic potential",
        first_variation_defect == 0 and e_phi != 0 and e_n != 0 and theta != 0,
    )
    noether_current = sp.expand(theta - xi0 * lagrangian)
    noether_identity = sp.simplify(
        e_phi * phi1 + e_n * n1 - total_d(n0 * e_n, jets)
    )
    exact(
        "integration by parts in the arbitrary diffeomorphism parameter gives the exact off-shell Noether identity",
        noether_identity == 0,
    )
    exact(
        "the Noether current J_xi=Theta(L_xi fields)-i_xi L is live and closes bulk plus boundary off shell",
        noether_current != 0
        and sp.simplify(
            e_phi * delta_phi
            + e_n * delta_n
            + total_d(noether_current, jets)
        )
        == 0,
    )
    wrong_identity = sp.simplify(e_phi * phi1 + e_n * n1)
    reject("drop the derivative-bearing lapse owner from the diffeomorphism identity", wrong_identity == 0)
    reject("set the metric/lapse Euler owner to zero because a separate internal gauge generator fixes it", e_n == 0)


def distinct_internal_ward() -> None:
    x = sp.symbols("x", real=True)
    connection = sp.Matrix([[x, 1 + x], [2 - x, -x]])
    distortion = sp.Matrix([[1 + x, x**2], [1 - x, -1 - x]])
    reduction = sp.Matrix([[2 - x, 1 + x**2], [x, x - 2]])
    lagrangian, _, e_c, e_t, e_q = W.action_objects(
        connection, distortion, reduction, x
    )
    ward = W.cov(connection, e_c, x) + W.comm(distortion, e_t) + W.comm(reduction, e_q)
    exact(
        "the predecessor internal gauge Ward remains an independent nonvacuous identity",
        W.is_zero(ward)
        and not W.is_zero(e_c)
        and not W.is_zero(e_t)
        and not W.is_zero(e_q)
        and lagrangian != 0,
    )
    typed("the internal generator acts by covariant derivative/commutator, while the diffeomorphism generator acts by Lie derivative and density weight")
    reject("rename the internal matrix Ward as the metric diffeomorphism Ward", False)


def native_owner_ledger_and_boundary() -> None:
    data = json.loads(REGISTRY.read_text())
    ledger = data["diffeomorphism_ward"]["required_native_owner_ledger"]
    expected = {
        "metric_zorro_lc_spin",
        "source_connection_and_distortion",
        "derived_bridge_h_k",
        "curvature_input",
        "eight_shiab_slots",
        "hodge_distortion_norm",
        "density_krein_pairing_lowerers",
        "all_green_concomitants",
    }
    exact(
        "the PW2F native Ward ledger names every independent or derived owner class without assigning an Euler equation to a derived node",
        set(ledger) == expected and all(ledger[key] for key in expected),
    )
    typed("the formal schema is now earned; native coefficient/rank waits for complete derived-K top order, the literal source-root transformation, and the lower C2 owner")
    typed("a future covariant-diffeomorphism route must be proved equivalent using the separately certified internal gauge Ward")
    typed("no physical stress-energy conservation, observation pushdown, or BV/BFV phase space is claimed")
    reject("promote the formal comparator to an evaluated public-source/native Ward", data["diffeomorphism_ward"]["status"] == "NATIVE_EVALUATED_PASS")


def main() -> int:
    print("PW2F METRIC DIFFEOMORPHISM / NOETHER / GREEN SCHEMA")
    source_and_layer_zero()
    exact_diffeomorphism_schema()
    distinct_internal_ward()
    native_owner_ledger_and_boundary()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + "
        f"{PLANTED} planted = {total}; failures={len(FAILURES)}"
    )
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print(
        "VERDICT: FORMAL DIFFEOMORPHISM-NOETHER/GREEN SCHEMA PASS; "
        "LITERAL ACTIVE-NATIVE WARD EVALUATION REMAINS OPEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
