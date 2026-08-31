"""Exact finite controls for split dependence and projector naturality."""

CHECKS = []


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def gamma(v):
    return v[1]


def split_zero(s):
    return (0, s)


def split_shear(s):
    return (s, s)


def projector(split, v):
    return sub(v, split(gamma(v)))


box = [(x, y) for x in range(-4, 5) for y in range(-4, 5)]
scalars = range(-4, 5)

check(
    "both supplied splittings are exact right inverses",
    all(gamma(split_zero(s)) == s and gamma(split_shear(s)) == s for s in scalars),
)
check(
    "the projector difference is exactly the split difference on the trace",
    all(
        sub(projector(split_zero, v), projector(split_shear, v))
        == sub(split_shear(gamma(v)), split_zero(gamma(v)))
        for v in box
    ),
)
check(
    "distinct right inverses give distinct projectors",
    split_zero(1) != split_shear(1)
    and any(projector(split_zero, v) != projector(split_shear, v) for v in box),
)
check(
    "both projectors land in and fix exactly the same kernel",
    all(gamma(projector(split_zero, v)) == 0 for v in box)
    and all(gamma(projector(split_shear, v)) == 0 for v in box)
    and all(
        (projector(split_zero, v) == v) == (gamma(v) == 0)
        and (projector(split_shear, v) == v) == (gamma(v) == 0)
        for v in box
    ),
)


def carrier_scale(v):
    return (2 * v[0], v[1])


def carrier_hostile_shear(v):
    return (v[0] + v[1], v[1])


check(
    "a contraction-and-split intertwiner commutes with correction",
    all(gamma(carrier_scale(v)) == gamma(v) for v in box)
    and all(carrier_scale(split_zero(s)) == split_zero(s) for s in scalars)
    and all(
        projector(split_zero, carrier_scale(v))
        == carrier_scale(projector(split_zero, v))
        for v in box
    ),
)
check(
    "a contraction intertwiner without split compatibility fails naturality",
    all(gamma(carrier_hostile_shear(v)) == gamma(v) for v in box)
    and carrier_hostile_shear(split_zero(1)) != split_zero(1)
    and any(
        projector(split_zero, carrier_hostile_shear(v))
        != carrier_hostile_shear(projector(split_zero, v))
        for v in box
    ),
)

print(f"corrected observation naturality: {len(CHECKS)}/{len(CHECKS)} exact checks passed")
for label in CHECKS:
    print(f"  PASS: {label}")
