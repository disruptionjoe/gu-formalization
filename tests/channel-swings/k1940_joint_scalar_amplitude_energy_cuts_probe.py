"""Independent polynomial Green solution and continuum pulse reconstruction."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import sympy as s
import k1940_joint_scalar_amplitude_energy_cuts as p

def exact_green():
    x=s.symbols('x');r=s.Rational(11,20);I=s.S(0);J=s.S(0);pieces=[]
    for ell,cut in [(s.S(1),s.S(1)),(s.S(2),r),(s.S(1),s.S(0))]:
        a=(ell*cut-cut**2/2)/ell
        for lo,hi,v in [(s.S(0),cut,a*x-x*x/2),(cut,ell,a*x-(x*cut-cut*cut/2))]:
            if lo==hi:continue
            h=x*(ell-x)/2;pieces.append((lo,hi,v,h,hi<=cut))
            I+=s.integrate(v,(x,lo,hi))
            if hi<=cut:J+=s.integrate(v,(x,lo,hi))
    H=s.Rational(5,6);K=s.factor(J-I*I/H);area=norm=linear=s.S(0)
    for lo,hi,v,h,inside in pieces:
        g=v-I*h/H;area+=s.integrate(g,(x,lo,hi));norm+=s.integrate(s.diff(g,x)**2,(x,lo,hi))
        if inside:linear+=s.integrate(g,(x,lo,hi))
    assert s.simplify(area)==0,'projected zero area'
    assert s.simplify(norm-K)==s.simplify(linear-K)==0,'actual Green norm and cut functional'
    result=p.lower();assert K==s.Rational(result['riesz_norm_squared'])
    defect=s.Rational(result['defect']);lam=defect/K
    assert s.factor(4+lam*lam*norm)==s.Rational(result['energy_lower'])
    return 5

def independent_pulse(cert):
    h=F(cert['h']);n=int(6/h);m=int(15/h);flows=list(map(F,cert['flows']));M=F(cert['M_upper']);rows=[[F(0),F(0)] for _ in range(n)];cols=[F(0)]*m;k=0;count=0
    for i in range(n):
        u=-3+i*h
        for j in range(m):
            z=-3+j*h
            if not (0<=z-u-h and z+h-u<=9):continue
            aa,bb=flows[k:k+2];k+=2;left=2*aa/h**2;right=2*bb/h**2
            assert 2*max(abs(left),abs(right))<=M,'continuum affine maximum at endpoints'
            rows[i][0]+=h*left;rows[i][1]+=h*right;cols[j]+=h*(left+right)/2;count+=1
    assert k==len(flows) and all(z==0 for z in cols),'pointwise zero column'
    for i,(a,b) in enumerate(rows):
        u=-3+i*h
        assert (a,b)==(p.phi(u),p.phi(u+h)),'pointwise entire affine row';count+=1
    assert M<F(23,100);return count+2

def check():
    report=json.loads(p.REPORT.read_text());count=exact_green()+independent_pulse(report['affine_pulse'])
    assert report==p.calculate(),'exact report reproduction'
    print('PASS',count+1,'independent rational/polynomial continuum controls')
    for fault in ['flow','jacobian','projection']:
        try:
            if fault=='projection':p.lower(fault=fault)
            else:p.verify(report['affine_pulse'],fault)
        except AssertionError as ex:print('DETECTED mathematical input',fault,':',ex)
        else:raise AssertionError('undetected '+fault)
    for name,mut in [('report',dict(report,claim='wrong')),('pin',dict(report,source_sha256='0'*64))]:
        try:assert mut==report,'report or pin mismatch'
        except AssertionError as ex:print('DETECTED consistency',name,':',ex)
        else:raise AssertionError('undetected reporting fault')
if __name__=='__main__':check()
