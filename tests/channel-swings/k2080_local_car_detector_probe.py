"""Exact finite CAR constructions plus rational consumer bounds. No continuum claim by sampling."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import json,importlib.util
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("producer",Path(__file__).with_name("k2080_local_car_detector.py"));p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
def annihilators(n,omit_sign=False):
    Z=s.diag(1,-1);I=s.eye(2);low=s.Matrix([[0,1],[0,0]])
    return [s.kronecker_product(*[(I if omit_sign else Z) if j<i else low if j==i else I for j in range(n)]) for i in range(n)]
def inner(u,v):return (u.conjugate().T*v)[0]
def normsq(u):return s.simplify(inner(u,u))
def number(a):return a.conjugate().T*a
def validate(d,omit_sign=False,subtract=False,omit_noise=False):
    a=annihilators(4,omit_sign);I=s.eye(16);O=s.zeros(16)
    for i in range(4):
        for j in range(4):
            assert a[i]*a[j]+a[j]*a[i]==O,"fermion annihilator sign"
            assert a[i]*a[j].conjugate().T+a[j].conjugate().T*a[i]==(I if i==j else O),"CAR mixed sign"
    vacuum=s.zeros(16,1);vacuum[0]=1
    sea=a[0].conjugate().T*vacuum;electron=a[1].conjugate().T*sea
    f=s.Rational(3,5)*a[0]+s.Rational(4,5)*a[1];N=number(f);nu=s.Rational(9,25)
    assert N*N==N,"number projection"
    effect=N-nu*I if subtract else N
    assert all(e>=0 for e in effect.eigenvals()),"vacuum subtraction is not positive"
    assert inner(sea,N*sea)==(0 if omit_noise else nu),"sea click"
    assert inner(electron,N*electron)==1,"electron click nu plus overlap"
    assert inner(sea,(N-nu*I)**2*sea)==nu*(1-nu),"vacuum variance"
    # Direct field-channel density calculation, compared with independent one-particle reflection.
    R=I-2*N;rho=sea*sea.conjugate().T;out=(rho+R*rho*R)/2
    electron_count=number(a[1]);hole_count=I-number(a[0])
    assert s.trace(out*electron_count)==2*nu*(1-nu),"measurement particles"
    assert s.trace(out*hole_count)==2*nu*(1-nu),"measurement holes"
    # Unequal positive/negative energies avoid hiding a factor by symmetry.
    hp=s.Rational(7,3);hm=s.Rational(5,2)
    energy=s.trace(out*(hp*electron_count+hm*hole_count))
    eplus=hp*s.Rational(16,25);eminus=hm*s.Rational(9,25)
    assert energy==2*nu*eplus+2*(1-nu)*eminus,"measurement energy without sea subtraction"
    fv=s.Matrix([s.Rational(3,5),s.Rational(4,5)]);rr=s.eye(2)-2*fv*fv.T;qq=s.diag(1,0);cc=(qq+rr*qq*rr)/2
    assert cc[1,1]==s.trace(out*electron_count) and 1-cc[0,0]==s.trace(out*hole_count),"reflection covariance"
    # Four independent modes: two filled negative modes and two empty positive modes.
    sea2=a[0].conjugate().T*a[2].conjugate().T*vacuum
    fup=s.Rational(3,5)*a[0]+s.Rational(4,5)*a[1];fdown=s.Rational(3,5)*a[2]+s.Rational(4,5)*a[3]
    spin=number(fup)-number(fdown)
    assert inner(sea2,spin*sea2)==0 and inner(sea2,spin**2*sea2)==2*nu*(1-nu),"spin noise is nonzero"
    # A before B, with up/down at indices0,1 and2,3.
    singlet=(a[0].conjugate().T*a[3].conjugate().T-a[1].conjugate().T*a[2].conjugate().T)*vacuum/s.sqrt(2)
    assert normsq(singlet)==1,"singlet normalization"
    def sz(i):return number(a[i])-number(a[i+1])
    def sx(i):return a[i].conjugate().T*a[i+1]+a[i+1].conjugate().T*a[i]
    AZ,AX=sz(0),sx(0);BZ,BX=sz(2),sx(2)
    for aa in [AZ,AX]:
        for bb in [BZ,BX]:assert aa*bb==bb*aa,"even locality"
    bell=AZ*(BZ+BX)/s.sqrt(2)+AZ*(BZ-BX)/s.sqrt(2)+AX*(BZ+BX)/s.sqrt(2)-AX*(BZ-BX)/s.sqrt(2)
    assert s.simplify(inner(singlet,bell*singlet))==-2*s.sqrt(2),"all-outcome Bell"
    plus=(AZ**2+AZ)/2;minus=(AZ**2-AZ)/2;zero=I-AZ**2
    assert plus+minus+zero==I and zero*zero==zero,"complete ternary instrument"
    assert sum((k*BZ*k for k in [plus,minus,zero]),O)==BZ,"nonselective no-signaling"
    c=d["constants"];t=F(c["tail"])
    assert c["number_lipschitz"]==2 and c["spin_lipschitz"]==4 and c["chsh_lipschitz"]==16,"product expansion constants"
    assert F(c["bell_lower"])==F(14,5)-120*t>2,"Bell consumer arithmetic"
    assert c["rational_chsh_error"]==120,"sum over four correlations"
    assert c["separation_m"]>2*c["radius_m"],"disjoint compact supports"
    assert F(c["vacuum_B_upper"])==16*t*t,"orthogonalized tail"
    assert F(c["single_mode_excitation_number_upper"])==4*t*t,"measurement excitation bound"
    assert F(c["single_mode_energy_over_m_upper"])==4*F(201,100)*t,"measurement energy bound"
    assert (2+2*t)**2<F(201,100)**2*(1-t*t),"cutoff H1 norm"
    for j in range(1,101):
        t=F(j,400);assert 9/(1-4*t*t)<16,"Gram-Schmidt tail inequality"
        # 2(1-sqrt(1-t^2)) <= 2t^2 by squaring 1-t^2 <= sqrt(1-t^2).
        assert (1-t*t)**2<=1-t*t,"normalized cutoff bound"
    for path,digest in d["evidence"].items():assert p.pin(path)==digest,"inherited input pin"
    return "exact 4-mode CAR/sea/spin/singlet/instrument/reflection-energy algebra; 200 rational tail controls; consumer constants/pins"
def main():
    d=p.build();assert d==json.loads((ROOT/"lab/process/k2080-local-car-detector.json").read_text()),"serialized producer mismatch"
    print("PASS baseline",validate(d));count=0
    for name,kwargs in [("omit_fermion_sign",dict(omit_sign=True)),("subtract_vacuum",dict(subtract=True)),("omit_vacuum_noise",dict(omit_noise=True))]:
        try:validate(d,**kwargs)
        except AssertionError as e:print("DETECTED",name,str(e));count+=1
        else:raise AssertionError("undetected "+name)
    for name,key,value in [("bell_error","bell_lower","14/5"),("radius_overlap","separation_m",4001),("tail_orthogonalization","vacuum_B_upper","1/250000"),("measurement_energy","single_mode_energy_over_m_upper","0")]:
        bad=deepcopy(d);bad["constants"][key]=value
        try:validate(bad)
        except AssertionError as e:print("DETECTED",name,str(e));count+=1
        else:raise AssertionError("undetected "+name)
    assert count==7;print("PASS 7 faults; finite algebra and reporting checks distinguished from continuum proof")
if __name__=="__main__":main()
