#!/usr/bin/env python3
"""Hostile mutations for K823."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path

P = Path(__file__).with_name("k823_sc_act_06_stationarity_transport_gate.py")
S = importlib.util.spec_from_file_location("k823", P); M = importlib.util.module_from_spec(S); S.loader.exec_module(M)

def main() -> int:
    mutations = [
        ("collapse rows", lambda x: x["stationarity_transport_theorem"].__setitem__("stationarity_equation", "F_t(x_t)=0")),
        ("infer stationarity", lambda x: x["stationarity_transport_theorem"].__setitem__("zero_locus_transport_implies_stationarity_transport", True)),
        ("skip stationarity", lambda x: x["stationarity_transport_theorem"].__setitem__("stationarity_is_required_before_action_hessian_credit", False)),
        ("promote jets", lambda x: x["stationarity_transport_theorem"].__setitem__("passing_first_and_second_stationarity_jets_proves_a_full_family", True)),
        ("wrong control residual", lambda x: x["exact_controls"].__setitem__("nonstationary_first_jet_residual", 0)),
        ("false control pass", lambda x: x["exact_controls"].__setitem__("nonstationary_stationarity_transport_passes", True)),
        ("stationary residual", lambda x: x["exact_controls"].__setitem__("stationary_second_jet_residual", 1)),
        ("source invented", lambda x: x["decision"].__setitem__("actual_source_action_family_constructed", True)),
        ("zero locus promoted", lambda x: x["decision"].__setitem__("zero_locus_packet_promoted_to_action_stationarity", True)),
        ("global verdict", lambda x: x["decision"].__setitem__("global_sc_act_06_proved_or_refuted", True)),
        ("wrong target", lambda x: x.__setitem__("target_claim", "NONE")),
        ("ledger moved", lambda x: x.__setitem__("source_and_ledger_effect", "MOVED")),
    ]
    for name, mutate in mutations:
        q = copy.deepcopy(M.build()); mutate(q)
        try: M.validate(q)
        except AssertionError: continue
        raise AssertionError(name)
    print("K823 hostile mutations rejected: 12/12"); return 0

if __name__ == "__main__": raise SystemExit(main())
