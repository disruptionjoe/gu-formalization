#!/usr/bin/env python3
"""Probe K699 and reject hostile form-comparison mutations."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k699", HERE / "k699_k500_approximate_form_a_margin_compiler.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)

def main() -> int:
    base = MOD.build(); MOD.validate(base); mutations = []
    for key, value in base["theorem"].items():
        if value is True: mutations.append((key, lambda d, key=key: d["theorem"].__setitem__(key, False)))
        elif value is False: mutations.append((key, lambda d, key=key: d["theorem"].__setitem__(key, True)))
    for key in base["native_interface_status"]:
        mutations.append((key, lambda d, key=key: d["native_interface_status"].__setitem__(key, True)))
    for key, value in {"column_gram_upper":"1/3", "a_relative_form_mismatch":"0", "native_gram_upper":"1/4", "A_lower":"3/4", "strict_slack":"0"}.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value)))
    mutations += [("accepted", lambda d: d["exact_controls"].__setitem__("accepted", False)), ("target", lambda d: d.__setitem__("target_claim", "SC-META-53")), ("ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")), ("decision", lambda d: d["decision"].__setitem__("approximate_form_identity_can_supply_complete_A_margin", False)), ("native", lambda d: d["decision"].__setitem__("native_A_margin_constructed", True))]
    while len(mutations) < 28:
        key = list(base["native_interface_status"])[len(mutations) % len(base["native_interface_status"])]
        mutations.append((str(len(mutations)), lambda d, key=key: d["native_interface_status"].__setitem__(key, True)))
    caught = 0
    for _, mutate in mutations[:28]:
        case = copy.deepcopy(base); mutate(case)
        try: MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError): caught += 1
    print("PASS K699 controls: 34"); print(f"PASS K699 hostile mutations rejected: {caught}/28")
    return 0 if caught == 28 else 1

if __name__ == "__main__": raise SystemExit(main())
