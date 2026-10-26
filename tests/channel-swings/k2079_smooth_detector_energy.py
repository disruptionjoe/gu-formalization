from pathlib import Path
from fractions import Fraction as F
import json, hashlib, argparse
ROOT=Path(__file__).resolve().parents[2]
def pin(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

def build():
    tau=F(1,500); theta=F(11,7); G=F(2); M=2+theta*G*tau
    return dict(status="INTERNALLY_REVIEWED_CONDITIONAL_MATHEMATICS",scope="conditional massive1408 with supplied controls",
        bounds={"tau":str(tau),"theta_upper":str(theta),"gradient_over_m":str(G),"rms_over_m":str(M),
        "signed_work_over_m":str(theta*G*tau*tau),"negative_mean_over_m":str(2*tau*M),
        "absolute_mean_change_over_m":str(theta*G*tau*tau+4*tau*M),"record_error":str(4*tau*tau)},
        smooth_pulse={"peak_factor":8,"derivative_factor":128,"field_temporal_factor":16384,"field_spatial_factor":64},
        species_dimensions=[dict(modes=n,two_species=2**(2*n),shared_memory=2**(n+1)) for n in range(1,9)],
        evidence={p:pin(p) for p in ["explorations/conditional-build/k2077-controlled-detector-response-2026-10-25.md","explorations/conditional-build/k1897-smooth-pulse-energy-2026-10-21.md"]},
        limitations=["No external or proof-assistant certification","No apparatus backreaction","No source-real completion","Species scattering is not a shared memory"])
if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");args=a.parse_args();d=build()
    if args.write:(ROOT/"lab/process/k2079-smooth-detector-energy.json").write_text(json.dumps(d,indent=2)+"\n")
    print(json.dumps(d,indent=2))
