from pathlib import Path
from fractions import Fraction as F
import json, hashlib, argparse
ROOT=Path(__file__).resolve().parents[2]
def pin(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

def build():
    tau=F(1,500)
    return dict(status="PROVISIONAL_PENDING_SPECIALIST_REVIEW",scope="massive1408 CAR sea; algebraic instruments, no point-local apparatus",
        constants={"number_lipschitz":2,"spin_lipschitz":4,"chsh_lipschitz":16,"rational_chsh_error":120,
        "tail":str(tau),"bell_lower":str(F(14,5)-120*tau),"vacuum_A_upper":str(tau*tau),"vacuum_B_upper":str(16*tau*tau),
        "single_mode_excitation_number_upper":str(4*tau*tau),"single_mode_energy_over_m_upper":str(F(201,12500)),"radius_m":2001,"separation_m":4003},
        covariance={"vacuum":"nu","electron":"nu+a^2","spin_variance":"2*nu*(1-nu)","subtracted_minimum":"-nu"},
        evidence={p:pin(p) for p in ["explorations/conditional-build/k2077-controlled-detector-response-2026-10-25.md","explorations/conditional-build/k2060-positive-energy-localization-2026-10-25.md"]},
        limitations=["No specialist acceptance","No state preparation theorem","No finite-duration point-local instrument","No GU source verdict"])
if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");args=a.parse_args();d=build()
    if args.write:(ROOT/"lab/process/k2080-local-car-detector.json").write_text(json.dumps(d,indent=2)+"\n")
    print(json.dumps(d,indent=2))
