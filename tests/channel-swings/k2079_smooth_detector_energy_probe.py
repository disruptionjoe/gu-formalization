"""Same-author exact algebra and finite controls, not continuum proof certification."""
from fractions import Fraction as F
from copy import deepcopy
from math import factorial
from pathlib import Path
import json, importlib.util
import sympy as s
import numpy as np
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("producer",Path(__file__).with_name("k2079_smooth_detector_energy.py"));p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
def validate(d,noncommuting=False):
    b=d["bounds"];t=F(b["tau"]);th=F(b["theta_upper"]);G=F(b["gradient_over_m"])
    assert F(b["rms_over_m"])==2+th*G*t,"graph-tail coefficient"
    assert F(b["signed_work_over_m"])==th*G*t*t,"two supported tails"
    assert F(b["negative_mean_over_m"])==2*t*(2+th*G*t),"sector first moment"
    assert F(b["absolute_mean_change_over_m"])==th*G*t*t+4*t*(2+th*G*t),"absolute versus signed energy"
    assert F(b["record_error"])==4*t*t,"record tail squared"
    x=F(4,3);N=12;partial=sum(x**k/F(factorial(k)) for k in range(N+1));tail=x**(N+1)/F(factorial(N+1))/(1-x/F(N+2))
    assert partial+tail<4,"rigorous exponential envelope"
    q=d["smooth_pulse"];assert q["peak_factor"]==8 and q["derivative_factor"]==128,"smooth normalization"
    assert q["field_temporal_factor"]==q["derivative_factor"]**2,"field temporal square"
    assert q["field_spatial_factor"]==q["peak_factor"]**2,"field spatial square"
    for row in d["species_dimensions"]:
        n=row["modes"];assert row["two_species"]==2**(2*n) and row["shared_memory"]==2**(n+1),"species-memory dimensions"
    I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
    alpha=[s.kronecker_product(X,X),s.kronecker_product(X,Y),s.kronecker_product(X,Z)];beta=s.kronecker_product(Z,I)
    B=s.kronecker_product(beta if noncommuting else s.eye(4),Y)
    for a in alpha+[beta]:
        aa=s.kronecker_product(a,I);assert aa*B-B*aa==s.zeros(8),"bounded commutator requires Clifford commutant"
    for row in range(1,7):
        # Numerical corroboration of graph estimate for finite Hermitian controls.
        h=np.array((row*alpha[0]+beta).tolist(),dtype=complex);v=np.diag([.2,-.1,.3,-.4]);T=row/9
        psi=np.array([1,2j,3,-1j],complex);psi/=np.linalg.norm(psi);u=expm(-1j*T*(h+v))@psi
        assert np.linalg.norm(h@u)<=np.linalg.norm(h@psi)+T*np.linalg.norm(h@v-v@h,2)+1e-12,"finite graph estimate"
    for path,digest in d["evidence"].items():assert p.pin(path)==digest,"inherited input pin"
    return "exact resource identities, Clifford commutant, exp series, 8 dimension rows; 6 finite numerical graph controls"
def main():
    d=p.build();assert d==json.loads((ROOT/"lab/process/k2079-smooth-detector-energy.json").read_text()),"serialized producer mismatch"
    print("PASS baseline",validate(d));faults=[]
    for field in ["signed_work_over_m","negative_mean_over_m","absolute_mean_change_over_m","record_error"]:
        bad=deepcopy(d);bad["bounds"][field]=str(F(bad["bounds"][field])/2)
        try:validate(bad)
        except AssertionError as e: print("DETECTED",field,str(e));faults.append(field)
        else:raise AssertionError("undetected "+field)
    bad=deepcopy(d);bad["smooth_pulse"]["field_temporal_factor"]=128
    try:validate(bad)
    except AssertionError as e:print("DETECTED field_square",str(e));faults.append("field_square")
    else:raise AssertionError("undetected field_square")
    try:validate(d,True)
    except AssertionError as e:print("DETECTED noncommuting_control",str(e));faults.append("noncommuting_control")
    else:raise AssertionError("undetected noncommuting_control")
    assert len(faults)==6;print("PASS 6 faults; coefficient mutations are reporting/algebra controls, not continuum proof review")
if __name__=="__main__":main()
