#!/usr/bin/env python3
"""Fail-closed ingress contract for a B5 native packet.

The contract still rejects every incomplete or silently substituted packet.
The action-owned strict branch now supplies one complete packet at its exact
declared grade; the graph-mixing full-nine family does not.
"""
from copy import deepcopy

REQUIRED = (
    "slot_pairing_phases", "coflip_linearity_and_phases",
    "formal_adjoint_sign", "green_boundary_form", "common_closed_domain",
)

UNFROZEN = {key: None for key in REQUIRED}

STRICT_PACKET = {
    "slot_pairing_phases": {
        "source": "program_native_induced_vector_spinor_krein",
        "relative_phases": "actual_carrier_fixed",
        "absolute_scale": "convention",
    },
    "coflip_linearity_and_phases": {
        "kind": "antilinear",
        "relative_phases": "gamma_natural_all_equal",
        "absolute_phase": "local_system_trivialization",
    },
    "formal_adjoint_sign": {
        "sign": "ANTI",
        "grade": "principal_symbol_action_closed_einstein",
    },
    "green_boundary_form": {
        "construction": "program_native",
        "formula": "B_n=[[0,A_n^vee],[A_n,K_n]]",
        "grade": "formal_trace",
    },
    "common_closed_domain": {
        "model": "flat_B5_half_cylinder",
        "realization": "minimal_graph_closure",
        "closed": True,
        "common_to_formal_adjoint": True,
        "symmetry_compatible": True,
        "grade": "repository_constructed_nonnull_product_end",
    },
}

def admit(packet):
    assert set(packet) == set(REQUIRED), "packet must have exactly five native fields"
    assert all(packet[key] is not None for key in REQUIRED), "unfrozen field"
    assert packet["coflip_linearity_and_phases"]["kind"] in {"linear", "antilinear"}
    assert packet["green_boundary_form"]["construction"] == "program_native"
    assert packet["common_closed_domain"]["closed"] is True
    assert packet["common_closed_domain"]["common_to_formal_adjoint"] is True
    assert packet["common_closed_domain"]["symmetry_compatible"] is True
    return packet

def hostile_controls():
    for key in REQUIRED:
        bad = deepcopy(UNFROZEN)
        bad.update(deepcopy(STRICT_PACKET))
        bad[key] = None
        try:
            admit(bad)
        except AssertionError:
            continue
        raise AssertionError(f"missing {key} was admitted")
    for replacement in ("positive_hilbert", "unspecified"):
        bad = {
            "slot_pairing_phases": {"source": "native"},
            "coflip_linearity_and_phases": {"kind": "linear"},
            "formal_adjoint_sign": "+",
            "green_boundary_form": {"construction": replacement},
            "common_closed_domain": deepcopy(STRICT_PACKET["common_closed_domain"]),
        }
        try:
            admit(bad)
        except AssertionError:
            continue
        raise AssertionError("non-native Green form was admitted")

def main():
    try:
        admit(UNFROZEN)
    except AssertionError:
        pass
    else:
        raise AssertionError("unfrozen packet was admitted")
    hostile_controls()
    admit(STRICT_PACKET)
    for field in ("closed", "common_to_formal_adjoint", "symmetry_compatible"):
        bad = deepcopy(STRICT_PACKET)
        bad["common_closed_domain"][field] = False
        try:
            admit(bad)
        except AssertionError:
            continue
        raise AssertionError(f"domain with {field}=False was admitted")
    print("B5 native packet contract: PASS (strict action-owned packet admitted; incomplete and substituted packets rejected)")

if __name__ == "__main__":
    main()
