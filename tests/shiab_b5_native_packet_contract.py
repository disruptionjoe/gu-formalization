#!/usr/bin/env python3
"""Fail-closed ingress contract for the unresolved B5 native packet.

This certificate intentionally cannot choose a coflip, phase, Green form, or
domain.  It proves instead that a downstream exactness test receives all five
named native fields and rejects the familiar silent substitutions.
"""
from copy import deepcopy

REQUIRED = (
    "slot_pairing_phases", "coflip_linearity_and_phases",
    "formal_adjoint_sign", "green_boundary_form", "common_closed_domain",
)

UNFROZEN = {key: None for key in REQUIRED}

def admit(packet):
    assert set(packet) == set(REQUIRED), "packet must have exactly five native fields"
    assert all(packet[key] is not None for key in REQUIRED), "unfrozen field"
    assert packet["coflip_linearity_and_phases"]["kind"] in {"linear", "antilinear"}
    assert packet["green_boundary_form"]["construction"] == "program_native"
    assert packet["common_closed_domain"]["symmetry_compatible"] is True
    return packet

def hostile_controls():
    for key in REQUIRED:
        bad = deepcopy(UNFROZEN)
        bad.update({
            "slot_pairing_phases": {"source": "native"},
            "coflip_linearity_and_phases": {"kind": "antilinear"},
            "formal_adjoint_sign": "+",
            "green_boundary_form": {"construction": "program_native"},
            "common_closed_domain": {"symmetry_compatible": True},
        })
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
            "common_closed_domain": {"symmetry_compatible": True},
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
    print("B5 native packet contract: PASS (no native selection admitted)")

if __name__ == "__main__":
    main()
