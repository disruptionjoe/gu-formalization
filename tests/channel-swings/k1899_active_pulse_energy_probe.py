from pathlib import Path
import json,hashlib,sys,copy
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def ck(b,label):
    if not b:raise AssertionError('[FAIL] '+label)
def eq(a,b,label):ck(s.simplify(a-b)==0,label)
def mat(d):
    a=s.zeros(d['rows'],d['columns'])
    for i,j,v in d['entries']:a[i,j]=s.Rational(v)
    return a
REPORT='lab/process/k1899-active-pulse-energy.json'
PIN='lab/process/k1897-smooth-pulse-energy.json'
def derive(mass=3,denominator=2,hole_factor=2):
    t,a,b,z=s.symbols('t a b z',real=True)
    # Direct momentum-space projector trace with p radial, q=p-k.
    cos=(1-z*t+mass**2*t*t)/s.sqrt((1+mass**2*t*t)*(1-2*z*t+(a*a+b*b+z*z+mass**2)*t*t))
    uv=s.expand(s.series(1-cos,t,0,3).removeO()).coeff(t,2)
    eq(uv,(a*a+b*b)/2,'projector overlap asymptotic')
    # Leading time endpoint amplitude divided by c(Ep+Eq); coefficient c=1 here.
    born=s.simplify(uv*hole_factor/denominator**2)
    eq(born,(a*a+b*b)/4,'Born radial energy factor')
    u=s.symbols('u',real=True)
    return s.simplify(2*s.pi*s.integrate((1-u*u)/4,(u,-1,1))/(2*s.pi)**3)
def audit(d):
    C=d['coefficients'];x=derive();eq(x,s.sympify(C['log_factor'])/s.pi**2,'independent Born log coefficient')
    eq(derive(mass=0),x,'massless high momentum control')
    eq(derive(mass=7),x,'mass independence')
    eq(s.sympify(C['angular_factor']),s.Rational(8,3),'angular reporting')
    eq(s.sympify(C['gaussian_factor']),s.Rational(3,2)*s.sympify(C['log_factor']),'Gaussian reporting')
    # Independent Fourier cutoff integral of the isotropic Gaussian momentum density.
    q=s.symbols('q',positive=True)
    g=s.integrate(4*s.pi*q**4*s.exp(-q*q),(q,0,s.oo))
    eq(g/(12*s.pi**2),s.sympify(C['gaussian_factor'])/s.sqrt(s.pi),'Fourier Gaussian coefficient')
    ck(C['threshold']==1,'weighted threshold reporting')
    ck(C['raw_remainder']=='O(sqrt(log L))','full remainder ceiling')
    ck(d['source_pins'][PIN]==sha(PIN),'dependency pin')
def reject(fn,label):
    try:fn()
    except AssertionError as e:ck('[FAIL]' in str(e),'assertion detection');print('CAUGHT',label,str(e))
    else:raise AssertionError('[FAIL] mutation survived '+label)
if __name__=='__main__':
    d=json.loads((ROOT/REPORT).read_text());audit(d);print('BASELINE PASS K1899 probe')
    reject(lambda:derive(denominator=1),'missing energy-sum factor')
    reject(lambda:derive(hole_factor=1),'omitted holes')
    for key,val in [('log_factor','1/6'),('gaussian_factor','1/4'),('raw_remainder','O(1)')]:
        q=copy.deepcopy(d);q['coefficients'][key]=val;reject(lambda:audit(q),key)
    q=copy.deepcopy(d);q['source_pins'][PIN]='0'*64;reject(lambda:audit(q),'pin')
    print('PASS K1899 probe: independent asymptotic/Born/Fourier checks; 2 mathematical input, 3 report and 1 pin faults')
