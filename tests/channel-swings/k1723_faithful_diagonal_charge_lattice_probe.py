#!/usr/bin/env python3
"""Hostile spectral mutations for K1723."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1723-faithful-diagonal-charge-lattice.json").read_text())


def errors(x):
    s, q = x.get("faithful_spectrum", {}), x.get("decision", {})
    out = []
    for key, needles in (("restricted_kernel", ("core_K(M)", "Z(K)", "{1}")), ("hilbert_faithfulness", ("H_ps=L2(K/M)", "faithful")), ("integer_spectrum", ("integer charge spaces",)), ("gcd_kernel", ("2 pi/d",)), ("primitive_lattice", ("gcd{q:H_q(D) nonzero}=1",)), ("odd_charge", ("at least one odd charge",))):
        if not all(n in s.get(key, "") for n in needles): out.append(key)
    for key in ("faithful_on_K_over_M", "faithful_on_full_H_ps", "charge_lattice_gcd_one", "odd_charge_exists"):
        if not q.get(key): out.append(key)
    for key in ("specific_physical_K_type_identified", "protected_status_change"):
        if q.get(key): out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("kernel intersection", lambda x: x["faithful_spectrum"].__setitem__("restricted_kernel", "unknown")),
        ("Hilbert lift", lambda x: x["faithful_spectrum"].__setitem__("hilbert_faithfulness", "one K-type")),
        ("integer spectrum", lambda x: x["faithful_spectrum"].__setitem__("integer_spectrum", "continuous labels")),
        ("gcd law", lambda x: x["faithful_spectrum"].__setitem__("gcd_kernel", "none")),
        ("primitive lattice", lambda x: x["faithful_spectrum"].__setitem__("primitive_lattice", "gcd two")),
        ("odd charge", lambda x: x["faithful_spectrum"].__setitem__("odd_charge", "all even")),
        ("space faithfulness", lambda x: x["decision"].__setitem__("faithful_on_K_over_M", False)),
        ("Hilbert faithfulness", lambda x: x["decision"].__setitem__("faithful_on_full_H_ps", False)),
        ("gcd decision", lambda x: x["decision"].__setitem__("charge_lattice_gcd_one", False)),
        ("physical K-type overclaim", lambda x: x["decision"].__setitem__("specific_physical_K_type_identified", True)),
        ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D); mutate(x); assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
