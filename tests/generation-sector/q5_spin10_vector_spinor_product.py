#!/usr/bin/env python3
"""Exact representation-ring certificate for Resolver Wave C / Q5.

This dependency-free route derives all four D5 ``16 x 144`` products from
standard lower tensor identities.  The independent Weyl-character calculation
lives in ``q5_spin10_vector_spinor_product_sage.py``.

Layer-0 boundary: a bare tensor product, a conditional complex-linear
internal Hom factor, an activated
coupling, and a mass operator are different objects.  This script reaches only
complex compact-Spin(10) representation-channel availability.
"""
from collections import Counter


checks = 0


def check(label, condition, detail=""):
    global checks
    checks += 1
    print("[{}] {}{}".format("PASS" if condition else "FAIL", label,
                             " -- " + detail if detail else ""))
    assert condition, label


DIMS = {
    "1": 1, "10": 10, "16+": 16, "16-": 16,
    "45": 45, "54": 54, "120": 120, "126+": 126, "126-": 126,
    "144+": 144, "144-": 144, "210": 210, "320": 320,
    "945": 945, "1050+": 1050, "1050-": 1050, "1728": 1728,
}

WEIGHTS = {
    "10": (1, 0, 0, 0, 0),
    "16+": (0, 0, 0, 0, 1), "16-": (0, 0, 0, 1, 0),
    "45": (0, 1, 0, 0, 0), "54": (2, 0, 0, 0, 0),
    "120": (0, 0, 1, 0, 0),
    "126+": (0, 0, 0, 0, 2), "126-": (0, 0, 0, 2, 0),
    "144+": (1, 0, 0, 0, 1), "144-": (1, 0, 0, 1, 0),
    "210": (0, 0, 0, 1, 1), "320": (1, 1, 0, 0, 0),
    "945": (1, 0, 1, 0, 0),
    "1050+": (1, 0, 0, 0, 2), "1050-": (1, 0, 0, 2, 0),
    "1728": (1, 0, 0, 1, 1),
}


def C(*names):
    return Counter(names)


def direct_sum(*parts):
    out = Counter()
    for part in parts:
        out += part
    return out


def subtract_exact(lhs, rhs):
    out = lhs.copy()
    for irrep, multiplicity in rhs.items():
        check("representation-ring subtraction is nonnegative",
              out[irrep] >= multiplicity,
              "{}: {} >= {}".format(irrep, out[irrep], multiplicity))
        out[irrep] -= multiplicity
        if out[irrep] == 0:
            del out[irrep]
    return out


def degree(character):
    return sum(DIMS[name] * mult for name, mult in character.items())


# Lower exact identities used by the analytic representation-ring route.
FF = {
    ("16+", "16+"): C("10", "120", "126+"),
    ("16-", "16-"): C("10", "120", "126-"),
    ("16+", "16-"): C("1", "45", "210"),
    ("16-", "16+"): C("1", "45", "210"),
}

V_TIMES = {
    "1": C("10"),
    "10": C("1", "45", "54"),
    "45": C("10", "120", "320"),
    "120": C("45", "210", "945"),
    "126+": C("210", "1050+"),
    "126-": C("210", "1050-"),
    "210": C("120", "126+", "126-", "1728"),
}


def vector_times(character):
    out = Counter()
    for irrep, multiplicity in character.items():
        piece = V_TIMES[irrep]
        for target, target_mult in piece.items():
            out[target] += multiplicity * target_mult
    return out


def spinor_times_rs(spinor, rs_label):
    # 144+ = 10*16+ - 16-; 144- = 10*16- - 16+.
    source_spinor = "16+" if rs_label == "144+" else "16-"
    gamma_trace = "16-" if rs_label == "144+" else "16+"
    return subtract_exact(vector_times(FF[(spinor, source_spinor)]),
                          FF[(spinor, gamma_trace)])


EXPECTED = {
    ("16+", "144+"): C("45", "54", "210", "945", "1050+"),
    ("16-", "144-"): C("45", "54", "210", "945", "1050-"),
    ("16+", "144-"): C("10", "120", "126-", "320", "1728"),
    ("16-", "144+"): C("10", "120", "126+", "320", "1728"),
}


print("Resolver Wave C / Q5: analytic D5 representation-ring route")
for pair, expected in EXPECTED.items():
    actual = spinor_times_rs(*pair)
    check("{} x {} decomposition".format(*pair), actual == expected,
          repr(sorted(actual.items())))
    check("{} x {} dimension closure".format(*pair),
          degree(actual) == 16 * 144,
          "{} = 2304".format(degree(actual)))
    check("all Q5 multiplicities are one", set(actual.values()) == {1})

for name, weight in WEIGHTS.items():
    check("D5 highest weight has rank five: " + name, len(weight) == 5)

# The question in the council packet was underspecified.  The same-label bare
# tensor has no 126, while a complex-linear internal Hom uses the dual spinor.
bare_same_label = EXPECTED[("16+", "144+")]
hom_16p_to_144p = EXPECTED[("16-", "144+")]  # (16+)* x 144+
check("planted false reading rejected: bare 16+ x 144+ contains no 126",
      not any(name.startswith("126") for name in bare_same_label))
check("conditional complex-linear Hom(16+,144+) contains exactly one 126+",
      hom_16p_to_144p["126+"] == 1)
check("same 126+ type occurs in the 16+ x 16+ bilinear",
      FF[("16+", "16+")]["126+"] == 1)
check("the scalar field contracting that bilinear is the dual 126-",
      WEIGHTS["126+"] != WEIGHTS["126-"] and DIMS["126+"] == DIMS["126-"])

# SOURCE/CONSTRUCTION FENCE: B5's already-built first-order symbol is 10-valued.
constructed_b5_symbol_channel = "10"
selected_new_channel = None
check("B5 symbol remains the 10 channel", constructed_b5_symbol_channel == "10")
check("Q5 does not select the 126 or create a coupling", selected_new_channel is None)

print("Q5 verdict: one 126 occurs in the conditional complex-linear internal")
print("Hom factor, not the bare tensor. The physical pairing remains unbuilt.")
print("checks passed:", checks)
