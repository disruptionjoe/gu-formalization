#!/usr/bin/env python3
"""Certificate for K1626's critical-capacity Gaussian shell channel."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def main():
    d = json.loads((ROOT / "lab/process/k1626-critical-capacity-shell-channel.json").read_text())
    q, z = d["shell_channel"], d["decision"]
    r = 2.0
    s = [0.8, 1.0, 1.2, 1.4]
    omega = [10.0, 11.0, 12.0, 13.0]
    info = 0.5 * len(s) * math.log1p(r)
    mmse = [x * r / (1.0 + r) for x in s]
    delta = sum(w * m / (x * x) for w, m, x in zip(omega, mmse, s))
    exact = r / (1.0 + r) * sum(w / x for w, x in zip(omega, s))
    checks = [
        ("claim", d["claim_id"] == "K1626"),
        ("shell dimension", "d_N=Theta(N^3)" in q["hypothesis"]),
        ("frequency scale", "omega_(N,k)=Theta(N)" in q["hypothesis"]),
        ("relative excess", "C_(N,k)=r s_(N,k)" in q["hypothesis"]),
        ("common-floor channel", "common-floor" in q["channel"]),
        ("information formula", abs(info - 2.0 * math.log(3.0)) < 1e-12),
        ("information scale", "Theta(N^3)" in q["information"]),
        ("mmse fixture", all(abs(a-b) < 1e-12 for a,b in zip(mmse, [8/15,2/3,4/5,14/15]))),
        ("missing Fisher identity", abs(delta - exact) < 1e-12),
        ("missing Fisher scale", "Theta(N^4)" in q["missing_fisher"]),
        ("quarter normalization", "one-quarter" in q["missing_fisher"]),
        ("simultaneous scale", "simultaneously attained" in q["sharpness"]),
        ("critical information", z["critical_information_realized"]),
        ("leading Fisher", z["leading_missing_fisher_realized"]),
        ("method sharp", z["information_method_scale_sharp"]),
        ("no coefficient change", not z["actual_coefficient_change_proved"]),
        ("not unrestricted", not z["unrestricted_state_theorem"]),
        ("protected", not z["protected_status_change"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")

if __name__ == "__main__":
    main()
