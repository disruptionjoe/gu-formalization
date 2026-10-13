#!/usr/bin/env python3
"""Hostile semantic mutations for K1719."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1719-joint-randomized-observation-closure.json").read_text())


def errors(x):
    j, r, q = x.get("joint_observation", {}), x.get("randomized_observation", {}), x.get("decision", {})
    out = []
    for key, needle in (("family", "arbitrary indexed family"), ("product_identity", "F_joint(z.x)"), ("formal_reuse", "equivariantMapEquivPi"), ("consequence", "No number")):
        if needle not in j.get(key, ""): out.append("joint_" + key)
    for key, needle in (("channel", "Markov kernel"), ("hypothesis", "trivially"), ("identity", "K(z.x)=z_*K(x)=K(x)"), ("consequence", "do not restore")):
        if needle not in r.get(key, ""): out.append("random_" + key)
    for key in ("indexed_products_preserve_blindness", "randomized_channels_preserve_blindness", "z_sensitive_target_could_reopen"):
        if not q.get(key): out.append(key)
    for key in ("private_randomness_recovers_sign", "source_measurement_constructed", "physical_observable_constructed", "protected_status_change"):
        if q.get(key): out.append(key)
    return out


def main():
    assert not errors(D)
    mutations = [
        ("family scope", lambda x: x["joint_observation"].__setitem__("family", "one map")),
        ("product identity", lambda x: x["joint_observation"].__setitem__("product_identity", "unknown")),
        ("formal product reuse", lambda x: x["joint_observation"].__setitem__("formal_reuse", "none")),
        ("product consequence", lambda x: x["joint_observation"].__setitem__("consequence", "maybe injective")),
        ("channel type", lambda x: x["randomized_observation"].__setitem__("channel", "untyped noise")),
        ("trivial action", lambda x: x["randomized_observation"].__setitem__("hypothesis", "unknown")),
        ("channel identity", lambda x: x["randomized_observation"].__setitem__("identity", "unknown")),
        ("random escape", lambda x: x["decision"].__setitem__("private_randomness_recovers_sign", True)),
        ("sensitive target closed", lambda x: x["decision"].__setitem__("z_sensitive_target_could_reopen", False)),
        ("source overclaim", lambda x: x["decision"].__setitem__("source_measurement_constructed", True)),
        ("physical overclaim", lambda x: x["decision"].__setitem__("physical_observable_constructed", True)),
        ("protected movement", lambda x: x["decision"].__setitem__("protected_status_change", True)),
    ]
    for i, (label, mutate) in enumerate(mutations, 1):
        x = copy.deepcopy(D); mutate(x); assert errors(x), label
        print(f"PASS {i:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
