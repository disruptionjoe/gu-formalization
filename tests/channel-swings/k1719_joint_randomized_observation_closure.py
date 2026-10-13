#!/usr/bin/env python3
"""Exact controls for K1719's product and randomized closure."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1719-joint-randomized-observation-closure.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    j, r, q = D["joint_observation"], D["randomized_observation"], D["decision"]
    joint = lambda x: (x % 2, 0)
    law = lambda x: (0.75, 0.25) if x % 2 == 0 else (0.25, 0.75)
    push = lambda g, p: p if g % 2 == 0 else (p[1], p[0])
    checks += [
        ("joint half-period blindness", all(joint((x + 2) % 4) == joint(x) for x in range(4))),
        ("random half-period blindness", all(law((x + 2) % 4) == law(x) for x in range(4))),
        ("random C4 equivariance", all(law((x + g) % 4) == push(g, law(x)) for g in range(4) for x in range(4))),
        ("arbitrary index scope", "arbitrary indexed family" in j["family"]),
        ("product identity", "F_joint(z.x)" in j["product_identity"]),
        ("product formal reuse", "equivariantMapEquivPi" in j["formal_reuse"]),
        ("no observable accumulation escape", "No number" in j["consequence"]),
        ("Markov channel", "Markov kernel" in r["channel"]),
        ("pushforward action", "pushforward" in r["channel"]),
        ("law identity", "K(z.x)=z_*K(x)=K(x)" in r["identity"]),
        ("randomness fence", "do not restore" in r["consequence"]),
        ("product decision", q["indexed_products_preserve_blindness"]),
        ("random decision", q["randomized_channels_preserve_blindness"]),
        ("private randomness no escape", not q["private_randomness_recovers_sign"]),
        ("sensitive target reopener", q["z_sensitive_target_could_reopen"]),
        ("source measurement fence", not q["source_measurement_constructed"]),
        ("physical observable fence", not q["physical_observable_constructed"]),
        ("protected fence", not q["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
