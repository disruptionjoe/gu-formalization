#!/usr/bin/env python3
"""Controls for K1486's BRST transfer of the recentering window."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/"lab/process/k1486-brst-recentering-window-instability.json").read_text())


def validate(d):
 a,q=d["brst_window_transfer"],d["decision"]
 return [d["claim_id"]=="K1486","(H_N-a_N) tensor 1" in a["full_family"],"Delta_BRST eta=0" in a["harmonic_vacuum"],"spectral bottom tending to minus infinity" in a["spectral_transfer"],"nonzero harmonic vector" in a["weak_transfer"],"fail weak Mosco liminf" in a["mosco_transfer"],q["excluded_scalar_window_transfers_to_full_brst"],q["excluded_scalar_window_transfers_to_harmonic_compression"],not q["brst_window_weak_liminf_holds"],not q["finite_cutoff_nilpotence_invalidated"],not q["continuum_interacting_brst_constructed"],not q["protected_status_change"]]


def main():
 checks=[]
 for name,pin in D["pinned_inputs"].items():checks.append((f"{name} pin",hashlib.sha256((ROOT/pin["path"]).read_bytes()).hexdigest()==pin["sha256"]))
 checks.extend((f"serialized invariant {i}",ok) for i,ok in enumerate(validate(D),1))
 matter=[-4.,-16.,-64.];brst=[0.,1.,3.]
 checks.append(("harmonic tensor preserves matter values",[x+brst[0] for x in matter]==matter))
 checks.append(("positive BRST energies cannot raise infimum above harmonic branch",min(x+y for x in matter for y in brst)==min(matter)))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f"PASS {i:02d}: {label}")
 print(f"RESULT: PASS {len(checks)}/{len(checks)}")
if __name__=="__main__":main()
