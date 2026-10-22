#!/usr/bin/env python3
"""Independent rational polynomial integrator, no producer/SymPy import."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def integ(p,D):return sum((v*D**(i+1)/Q(i+1) for i,v in enumerate(p)),Q(0))
def deriv(p):return [i*v for i,v in enumerate(p)][1:]
def mul(p,q):
    r=[Q(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r
def val(p,x):return sum((a*x**i for i,a in enumerate(p)),Q(0))
def energy(p,D):return integ(mul(deriv(p),deriv(p)),D)
def profile(width_factor=3,area_factor=6):
    h=Q(1);a=Q(1);b=Q(2);L=Q(4);eps=Q(1,10);tau=width_factor*eps/h
    A0=h*(b-a)/2;A=A0+eps;D=L-b-tau
    segments=[([0,-area_factor*A/D**2,area_factor*A/D**3],D),([0,0,h/tau**2],tau),([h],b-a),([h,-2*h/tau,h/tau**2],tau),([0],a-tau)]
    primitive=Q(0);en=Q(0);values=[primitive];prior=Q(0)
    for p,length in segments:
        assert length>0,'positive segment length'
        assert val(p,0)==prior,'phase join'
        prior=val(p,length);primitive+=integ(p,length);en+=energy(p,length);values.append(primitive)
    assert prior==0,'center phase zero'
    assert values==[0,-A,-A0,A0,A,A],'global primitive values'
    assert 2*en==16*h**3/(9*eps)+24*A*A/D**3,'full energy'
    assert 2*en<20 and 3*A/(2*D)<h,'finite energy and peak slack'
    assert 2*(A0+Q(16,9)/20)==Q(53,45),'finite lower coefficient'
    # Each segment has fixed sign, hence endpoint values certify its primitive extrema.
    assert all(-A<=v<=A for v in values),'primitive obstacle'
    return {'energy':str(2*en),'A':str(A),'segments':len(segments)}
def reflect(sign=-1):
    # F=(1-u^2)^2(2+u), phi coefficients; integration is independent of symbolic library.
    F=list(map(Q,[2,1,-4,-2,2,1]));phi=deriv(F)
    reflection=[v*((-1)**i) for i,v in enumerate(phi)]
    po=[(x+sign*y)/2 for x,y in zip(phi,reflection)]
    Fo=[(v+v*((-1)**i))/2 for i,v in enumerate(F)]
    assert deriv(Fo)==po,'primitive reflection sign'
    return True
def strip():
    L=Q(4);d=Q(3);u=Q(-2);z=Q(-1)
    up=-u;zp=d-z
    assert 0<zp-up<d and -L<up<L,'strip image'
    assert (-up,d-zp)==(u,z),'strip involution'
    assert zp-up==d-(z-u),'time difference reversal'
    return True
def reports(mutate=False,pin=False):
    r=json.loads((ROOT/'lab/process/k1917-scalar-energy-primitive-frontier.json').read_text())
    if mutate:r['formulas']['C']='theta**3/9'
    if pin:r['dependencies'][next(iter(r['dependencies']))]='0'*64
    assert r['formulas']['C']=='2*theta**3/9','reported coefficient'
    for p,h in r['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency pin'
def rejected(fn,label):
    try:fn()
    except AssertionError as ex:
        assert str(ex),'empty failed check';print('CAUGHT',label,':',ex);return
    raise AssertionError('missed mutation '+label)
if __name__=='__main__':
    print('BASELINE',profile());reflect();strip();reports()
    rejected(lambda:profile(width_factor=2),'mathematical transition width')
    rejected(lambda:profile(area_factor=5),'mathematical connector area')
    rejected(lambda:reflect(sign=1),'mathematical reflection sign')
    rejected(lambda:reports(mutate=True),'report coefficient')
    rejected(lambda:reports(pin=True),'dependency pin')
    print('PASS K1917 independent exact profile/reflection/strip checks; 3 math faults, 1 report fault, 1 pin fault')
