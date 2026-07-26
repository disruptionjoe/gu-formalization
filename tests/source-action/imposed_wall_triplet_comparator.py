#!/usr/bin/env python3
"""Target-blind imposed-wall ledger for the SRC-TOY-01 Rung-2 control.

This is deliberately a *standard-field* positive-Hilbert domain-wall index
comparator.  It treats a vectorlike multiplicity N and an imposed signed wall
index q as independent inputs, keeps the remote mirror ledger explicit, and
asks what follows before any dynamical source or GU-native transport is
claimed.  It is not a Krein calculation, source action, anomaly proof, or
generation derivation.
"""

from __future__ import annotations


def check(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS: {label}")


def imposed_wall_ledger(multiplicity: int, wall_index: int) -> dict[str, int | str]:
    """Return the fully paired finite index ledger for one imposed wall sector.

    The local accessible chirality has signed index ``q*N``.  The omitted
    partner is represented explicitly as the remote/boundary-completion mirror
    with the opposite signed index, so this bookkeeping toy never converts a
    local chiral readout into a globally unpaired theory.
    """
    if multiplicity < 1:
        raise ValueError("the independently supplied vectorlike carrier needs N >= 1")

    accessible_index = wall_index * multiplicity
    return {
        "multiplicity": multiplicity,
        "wall_index": wall_index,
        "accessible_index": accessible_index,
        "accessible_rank": abs(accessible_index),
        "accessible_chirality": "right" if accessible_index > 0 else "left" if accessible_index < 0 else "none",
        "remote_mirror_index": -accessible_index,
        "global_index": accessible_index - accessible_index,
    }


def target_coding_detected(multiplicity: int, wall_index: int, claimed_rank: int) -> bool:
    """Detect the forbidden positive control: choose q and N because they yield 3."""
    return multiplicity == 3 and wall_index == 1 and claimed_rank == 3


def main() -> None:
    print("SRC-TOY-01 Rung-2 imposed-wall comparator")
    print("construction: standard positive-Hilbert domain-wall index ledger")
    print("not claimed: dynamical wall, source action, anomaly proof, GU transport, or generation derivation")

    unit = {n: imposed_wall_ledger(n, 1) for n in range(1, 5)}
    check("unit wall returns accessible rank N for N=1,2,3,4", [unit[n]["accessible_rank"] for n in unit] == [1, 2, 3, 4])
    check("unit wall does not distinguish N=3 from the other supplied multiplicities", len({unit[n]["accessible_rank"] for n in unit}) == 4)

    for q in (0, -3, -2, -1, 1, 2, 3):
        ledger = imposed_wall_ledger(3, q)
        check(f"q={q} keeps the complete vectorlike ledger globally index zero", ledger["global_index"] == 0)
        check(f"q={q} records the remote mirror rather than truncating it", ledger["remote_mirror_index"] == -ledger["accessible_index"])

    positive = imposed_wall_ledger(2, 1)
    reversed_orientation = imposed_wall_ledger(2, -1)
    check("orientation reversal flips local chirality without changing accessible rank", positive["accessible_rank"] == reversed_orientation["accessible_rank"] == 2 and positive["accessible_index"] == -reversed_orientation["accessible_index"])
    check("zero index has no accessible chiral mode", imposed_wall_ledger(3, 0)["accessible_rank"] == 0)
    check("non-target indices remain available returns", [imposed_wall_ledger(1, q)["accessible_rank"] for q in (-2, -1, 0, 1, 2)] == [2, 1, 0, 1, 2])

    direct_sum = imposed_wall_ledger(1, 1)["accessible_rank"] + imposed_wall_ledger(2, 1)["accessible_rank"]
    check("inert direct sums add ranks rather than privileging three", direct_sum == imposed_wall_ledger(3, 1)["accessible_rank"] == 3)
    check("a construction that chooses N=3 and q=1 for rank three is detected as target-coded", target_coding_detected(3, 1, 3))
    check("the same detector does not label an independently specified non-target control as target-coded", not target_coding_detected(2, 1, 2))

    print("RETURN: IMPOSED_BOUNDARY_HOSTING / EFFECTIVE_ACCESS_N")
    print("BOUNDARY: N and q are supplied inputs; three is not selected and global completion remains paired.")


if __name__ == "__main__":
    main()
