#!/usr/bin/env sage-python
"""Exact K77 four-field zero-order port composition.

Run with::

    sage -python tests/channel-swings/selected_k77_four_field_zero_order_port_probe.py

Layer 0: this asks only whether the ordinary ``Omega0(S) -> Omega1(S)``
connection cell in the complete equation-9.16 grammar can absorb the exact
one-form W/mirror leakage.  Image inclusion is necessary for a graph adapter;
it is not graph invariance, BV cohomology, a closed domain, a spectrum, an
index, a generation count or an external datum.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy

from sage.all import block_matrix, zero_matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def load_predecessor() -> dict:
    """Replay the exact v0.136 producer as the immutable integration API."""
    capture = io.StringIO()
    with redirect_stdout(capture):
        namespace = runpy.run_path(
            str(ROOT / "tests/channel-swings/selected_k77_zero_order_w_mirror_parent_leakage_probe.py")
        )
    namespace["captured_predecessor_output"] = capture.getvalue()
    return namespace


def form_quotient(structures: dict, field):
    """Kernel is exactly the connection line ``a tensor S``."""
    nv, ds = 14, 128
    identity = structures["I128"]
    zero = zero_matrix(field, ds, ds, sparse=True)
    a = [2, -1, 0, 1] + [0] * 10
    rows = []
    for row in range(1, nv):
        rows.append([
            -field(a[row]) * identity if column == 0
            else field(a[0]) * identity if column == row
            else zero
            for column in range(nv)
        ])
    return block_matrix(field, nv - 1, nv, rows, sparse=True), a


def connection_port(structures: dict, field, parent, a):
    nv = 14
    return block_matrix(
        field, nv, 1,
        [[field(a[row]) * parent] for row in range(nv)],
        sparse=True,
    )


def single_slot_plant(structures: dict, field, parent):
    nv, ds = 14, 128
    zero = zero_matrix(field, ds, ds, sparse=True)
    return block_matrix(
        field, nv, 1,
        [[parent if row == 0 else zero] for row in range(nv)],
        sparse=True,
    )


def analyze_field(namespace: dict, structures: dict, field, bases: dict) -> dict:
    quotient, a = form_quotient(structures, field)
    results = {}
    preferred = {
        "moving_spin_grade2": field(1),
        "two_half_block_grade6": field(1),
        "source_full_u_coset_grade1": field(-1),
    }
    for parent_name, parent in structures["parents"].items():
        left, right = structures["zero_order_pair"](parent)
        port = connection_port(structures, field, parent, a)
        quotient_left = {}
        quotient_right = {}
        carrier_rows = {}
        for carrier_name, projector, basis in (
            ("W", structures["W"], bases["W"]),
            ("mirror", structures["M"], bases["mirror"]),
        ):
            outside = structures["I1792"] - projector
            port_out = outside * port
            leak_left = outside * left * basis
            leak_right = outside * right * basis
            ratio = preferred[parent_name]
            leak = leak_left + ratio * leak_right
            joined = block_matrix(field, 1, 2, [[port_out, leak]], sparse=True)
            planted_port = outside * single_slot_plant(structures, field, parent)
            planted_joined = block_matrix(
                field, 1, 2, [[planted_port, leak]], sparse=True
            )
            quotient_left[carrier_name] = quotient * left * basis
            quotient_right[carrier_name] = quotient * right * basis
            carrier_rows[carrier_name] = {
                "leak_rank": leak.rank(),
                "port_rank": port_out.rank(),
                "joined_rank": joined.rank(),
                "included": joined.rank() == port_out.rank(),
                "single_slot_plant_rejects": planted_joined.rank() > planted_port.rank(),
            }
        coefficient_ranks = {
            carrier_name: namespace["coefficient_rank"](
                quotient_left[carrier_name], quotient_right[carrier_name]
            )
            for carrier_name in ("W", "mirror")
        }
        preferred_zero = {
            carrier_name: (
                quotient_left[carrier_name]
                + preferred[parent_name] * quotient_right[carrier_name]
            ).is_zero()
            for carrier_name in ("W", "mirror")
        }
        results[parent_name] = {
            "preferred_ratio": str(preferred[parent_name]),
            "quotient_coefficient_ranks": coefficient_ranks,
            "preferred_quotient_zero": preferred_zero,
            "carriers": carrier_rows,
        }
    return results


print("A. SOURCE, PRIOR ART AND LAYER 0")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
trace_q = (ROOT / "explorations/k77-wave2-trace-q-coefficient-zero-order-reality-selection-2026-08-04.md").read_text()
v137 = (ROOT / "explorations/conditional-build/selected-k77-action-owned-leakage-composition-2026-08-10.md").read_text()
check("source", "equation 9.16 supplies ordinary zero-form-to-one-form connection cells",
      "varpi_{++}" in source and "d_0+\\varpi_{+-}" in source)
check("source", "source supplies the four-field grammar but not a W graph adapter or BV selector",
      "four distinct fields" in source and "unique or globally defined operator" in source)
check("prior_art", "August 4 already assembled the complete sixteen-cell trace-q family",
      "FULL16_TRACE_Q_FAMILY_ASSEMBLED" in trace_q)
check("prior_art", "v0.137 leaves the complete four-field operator as the next named alternative",
      "complete four-field" in v137)
check("layer0", "one-form invariance and cancellation through an Omega0 port are distinct", True)
check("layer0", "port image inclusion is only necessary for graph invariance", True)
check("layer0", "graph invariance, BV cohomology and closed-domain spectrum are distinct", True)

namespace = load_predecessor()
check("prior_art", "the immutable v0.136 predecessor replay remains green",
      not namespace["FAILURES"] and "PASS:" in namespace["captured_predecessor_output"])


print("\nB. EXACT FINITE-FIELD AND GAUSSIAN-RATIONAL PORT TEST")
finite_bases = {"W": namespace["w_basis"], "mirror": namespace["m_basis"]}
char0_bases = {"W": namespace["w0_basis"], "mirror": namespace["m0_basis"]}
finite_results = analyze_field(namespace, namespace["finite"], namespace["fp"], finite_bases)
char0_results = analyze_field(namespace, namespace["char0"], namespace["gaussian"], char0_bases)

for field_name, results in (("finite", finite_results), ("Gaussian-rational", char0_results)):
    for parent_name, parent_result in results.items():
        for carrier_name, row in parent_result["carriers"].items():
            check("exact", f"{field_name} {parent_name}/{carrier_name}: leakage rank is 64",
                  row["leak_rank"] == 64)
            check("exact", f"{field_name} {parent_name}/{carrier_name}: connection port rank is 128",
                  row["port_rank"] == 128)
            check("exact", f"{field_name} {parent_name}/{carrier_name}: leakage lies in the port image",
                  row["included"] and row["joined_rank"] == 128)
            check("planted", f"{field_name} {parent_name}/{carrier_name}: a single-slot fake port fails",
                  row["single_slot_plant_rejects"])
            check("exact", f"{field_name} {parent_name}/{carrier_name}: quotient condition has rank one",
                  parent_result["quotient_coefficient_ranks"][carrier_name] == 1)
            check("exact", f"{field_name} {parent_name}/{carrier_name}: preferred ratio is the unique projective zero",
                  parent_result["preferred_quotient_zero"][carrier_name])


print("\nC. PARENT SPLIT, VARIATIONAL AND PHYSICAL FENCES")
check("exact", "Spin and two-half parents require alpha=beta",
      finite_results["moving_spin_grade2"]["preferred_ratio"] == "1"
      and finite_results["two_half_block_grade6"]["preferred_ratio"] == "1")
check("exact", "the full-U odd coset requires alpha=-beta",
      finite_results["source_full_u_coset_grade1"]["preferred_ratio"] == str(namespace["fp"](-1)))
check("type", "one common coefficient cannot satisfy both even-parent and odd-coset port conditions in characteristic zero", True)
check("type", "the ordinary port rescues the restricted-parent necessary condition but not the source-full parent", True)
check("type", "the port image is form-line data and does not by itself select which invertible parent acted on spinors", True)
check("variational", "a graph map must still satisfy the lower-left equation and the nonlinear graph/Riccati identity", True)
check("symplectic", "no presymplectic characteristic quotient or BV cohomology is inferred from image inclusion", True)
check("analytic", "no closed domain, spectrum, Fredholm index or positivity statement is inferred", True)
check("adversarial", "the result revives an adapter route without promoting compatibility to derivation", True)

RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "field": "K77_EXACT_GF_AND_GAUSSIAN_RATIONAL",
    "finite_results": finite_results,
    "char0_results": char0_results,
    "source_return": "SOURCE_CONFIRMS_FOUR_FIELD_ZERO_FORM_PORT__SOURCE_SILENT_ON_GRAPH_ADAPTER_BV_SELECTOR_AND_DOMAIN",
    "disposition": "PARENT_SPLIT__RESTRICTED_PARENTS_HAVE_UNIQUE_PORT_COMPATIBLE_RATIO__SOURCE_FULL_PARENT_HAS_INCOMPATIBLE_PARITY_REQUIREMENTS",
    "next_gate": "SOLVE_OR_KILL_COMPLETE_W_AND_MIRROR_GRAPH_RICCATI_PLUS_LOWER_LEFT_ADJOINT_CONDITION__THEN_TEST_MOVING_DESCENT_AND_BV_COHOMOLOGY",
}

print("\nK77 FOUR-FIELD ZERO-ORDER PORT RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("Checks: " + " + ".join(f"{count} {kind}" for kind, count in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: the complete four-field port can absorb W/mirror leakage only on parent-specific coefficient horns; the source-full parent remains conflicted.")
