"""Independent exact phase integration, resource inequalities and correction identities."""
from fractions import Fraction as F
from pathlib import Path
from copy import deepcopy
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1946-quantitative-smooth-pulse.json'
def inspect(v):
    seed=json.loads((ROOT/v['seed_ref']).read_text())['pulse'];h=F(seed['h']);y=list(map(F,seed['phase_nodes']));L=max(abs(y[i+1]-y[i])/h for i in range(len(y)-1));A=max(map(abs,y));count=0
    for r in v['family']+[v['construction']]:
        e=F(r['radius']);p=[tuple(map(F,x)) for x in r['flattened_knots']];assert 0<e<F(1,4),'admissible compression'
        assert all(a[0]<b[0] for a,b in zip(p,p[1:])),'strictly ordered exact knots'
        assert dict(p)=={-x:-z for x,z in p},'odd phase gives exact zero area';count+=3
        # Check each inherited free-interval knot by inverse affine coordinates.
        for a,b in [(F(-3),F(-2)),(F(-1),F(1)),(F(2),F(3))]:
            for i,Y in enumerate(y):
                u=-3+i*h
                if a<=u<=b:
                    moved=a+e+(u-a)*(b-a-2*e)/(b-a)
                    assert moved in dict(p) and dict(p)[moved]==Y,'lossless flattened phase';count+=1
        for a,b,z in [(-3,-3+e,0),(-2-e,-1+e,1),(1-e,2+e,-1),(3-e,3,0)]:
            assert all(Y==z for u,Y in p if a<=u<=b),'flat support and plateau margins';count+=1
        energy=sum((z2-z1)**2/(u2-u1) for (u1,z1),(u2,z2) in zip(p,p[1:]));area=sum((z1+z2)*(u2-u1)/2 for (u1,z1),(u2,z2) in zip(p,p[1:]));assert area==0,'exact integrated area'
        assert energy==F(r['phase_energy_upper'])<F(401,100),'smooth energy via convolution contraction';count+=2
        eta=e*(A+F(21,4)*L);T=F(9,2);G=16/T;G1=128/T**2;G2=10240/T**3
        peak=F(seed['amplitude'])+(3*G1+G)*eta
        assert peak==F(r['pulse_amplitude_upper'])<F(23,100),'strict amplitude from residual construction';count+=1
        assert F(r['residual_sup_bound'])==eta,'uniform residual bound'
        assert e/4<e and 2*e<F(9,2)*e and e<3*e,'phase and pulse mollifier fit open support';count+=2
        rp=L/(1-2*e)+L
        assert F(r['spatial_derivative_upper'])==32*F(seed['amplitude'])/e+G1*eta/2+G*rp,'spatial derivative chain rule'
        assert F(r['time_derivative_upper'])==32*F(seed['amplitude'])/e+(3*G2+F(3,2)*G1)*eta+G*rp,'time derivative chain rule';count+=2
    return count

def correction(sign=-1):
    # A polynomial test is an algebraic control, not a numerical pulse certificate.
    t,u,z,c=s.symbols('t u z c',positive=True);r=u**3-u;primitive=sign*(u*u-1)**2/(8*c);g=30*t**2*(1-t)**2
    V=s.diff(g,t)*primitive+g*r
    assert s.expand(s.integrate(V,(t,0,1))-r)==0,'right phase correction'
    assert s.simplify(s.integrate(V.subs(u,z-2*c*t),(t,0,1)))==0,'opposite phase exact cancellation'
    return 2

def pins(v):
    assert v['result_id']=='K1946','report identity'
    assert hashlib.sha256((ROOT/v['seed_ref']).read_bytes()).hexdigest()==v['seed_sha256'],'seed pin'
    assert hashlib.sha256((ROOT/'tests/channel-swings/k1946_quantitative_smooth_pulse.py').read_bytes()).hexdigest()==v['source_sha256'],'producer pin'

def main():
    v=json.loads(REPORT.read_text());pins(v);count=inspect(v)+correction();caught=[]
    bad=deepcopy(v);bad['construction']['flattened_knots'][2][1]='2'
    try:inspect(bad)
    except AssertionError as e:caught.append(str(e))
    bad=deepcopy(v);bad['construction']['radius']='1/10'
    try:inspect(bad)
    except AssertionError as e:caught.append(str(e))
    try:correction(1)
    except AssertionError as e:caught.append(str(e))
    assert len(caught)==3,'actual phase/radius/correction faults caught'
    consistency=[]
    for k in ['result_id','seed_sha256']:
        bad=deepcopy(v);bad[k]='bad'
        try:pins(bad)
        except AssertionError as e:consistency.append(str(e))
    assert len(consistency)==2,'report/pin controls'
    print('PASS K1946',count,'independent exact controls; mathematical faults:',caught,'consistency:',consistency)
if __name__=='__main__':main()
