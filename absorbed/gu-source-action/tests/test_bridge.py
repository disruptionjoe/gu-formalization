#!/usr/bin/env python3
"""Smoke test: the bridge to gu-formalization loads and reproduces the verified anchors.

Run: python tests/test_bridge.py
"""

import os
import sys

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import gu_bridge  # noqa: E402


def main():
    a = gu_bridge.anchors()
    print("gu-formalization:", a["gu_path"])
    print(f"bare ||[Pi_RS, M_D]|| = {a['bare_commutator']:.4f}   (expect 58.7215)")
    print(f"C2 = ||Gamma M_D Pi_RS|| = {a['C2']:.4f}   (expect 155.3625)")
    assert abs(a["bare_commutator"] - 58.7215) < 1e-2, "bridge anchor (commutator) mismatch"
    assert abs(a["C2"] - 155.3625) < 1e-2, "bridge anchor (C2) mismatch"
    # degree-1 homogeneity sanity (C2 is a symbol-norm, not an index)
    import numpy as np
    assert abs(gu_bridge.C2(2 * gu_bridge.XI) / a["C2"] - 2.0) < 1e-3, "C2 should be degree-1 homogeneous"
    print("BRIDGE OK — verified foundation imported; anchors reproduced; C2 degree-1 homogeneous confirmed.")


if __name__ == "__main__":
    main()
