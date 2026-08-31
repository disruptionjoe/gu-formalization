"""Exact finite controls for family/owner identifiability.

This reproduces the two-copy exchange algebra and keeps the family-selection
question separate from the independent 54/210 owner coordinates.
"""

CHECKS = []


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


def swap(packet):
    return (packet[1], packet[0])


def invariant(packet):
    return swap(packet) == packet


def selects_exactly_one(packet):
    return (packet[0] != 0 and packet[1] == 0) or (
        packet[0] == 0 and packet[1] != 0
    )


samples = ((0, 0), (1, 1), (-3, -3), (1, 0), (0, 1), (2, -2))
check(
    "swap invariance is exactly equality of family coefficients",
    all(invariant(packet) == (packet[0] == packet[1]) for packet in samples),
)
check(
    "no invariant packet selects exactly one equivalent family",
    all(not selects_exactly_one(packet) for packet in samples if invariant(packet)),
)
check(
    "hostile asymmetric packets violate family exchange invariance",
    all(not invariant(packet) for packet in ((1, 0), (0, 1), (2, -2))),
)

owner54_only = {"54": (1, 1), "210": (0, 0)}
owner210_only = {"54": (0, 0), "210": (1, 1)}
check(
    "the 54-only and 210-only owner packets are separately family invariant",
    all(invariant(packet) for packet in owner54_only.values())
    and all(invariant(packet) for packet in owner210_only.values()),
)
check(
    "family symmetry leaves the two quadratic owner axes distinct",
    owner54_only != owner210_only
    and {owner for owner, packet in owner54_only.items() if packet != (0, 0)} == {"54"}
    and {owner for owner, packet in owner210_only.items() if packet != (0, 0)} == {"210"},
)
check(
    "the supplied symmetric owner support remains exactly 54 and 210",
    set(owner54_only) == {"54", "210"} == set(owner210_only),
)

print(f"source-native family/owner identifiability: {len(CHECKS)}/{len(CHECKS)} exact checks passed")
for label in CHECKS:
    print(f"  PASS: {label}")
