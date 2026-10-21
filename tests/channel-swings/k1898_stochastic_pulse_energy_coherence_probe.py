from pathlib import Path
import sys,json,hashlib,copy
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
PIN='lab/process/k1896-local-phase-vacuum-boundary.json'
REPORT=ROOT/'lab/process/k1898-stochastic-pulse-energy-coherence.json'
def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def check(b,label):
    if not b: raise AssertionError('[FAIL] '+label)
def eq(a,b,label): check(s.simplify(a-b)==0,label)

def audit(d):
    C=d['coefficients'];k,q=s.symbols('k q',positive=True)
    # Fourier transform of theta: sqrt(l) scaling; l=1 gives theta_hat=e^-k²/2.
    # Derivative norm from Fourier rather than real-space producer integral.
    v=s.symbols('v',real=True);fourier_norm=s.integrate(v*v*s.exp(-v*v),(v,-s.oo,s.oo))
    eq(fourier_norm,s.sqrt(s.pi)/2,'independent Fourier derivative norm')
    # Rank-two one-way crossing count and positive energy measure.
    cross=2/(2*s.pi)*s.integrate(q,(q,0,k))
    eq(cross,s.sympify(C['per_direction_energy'])*k*k/s.pi,'spin and energy factor')
    eq(2*s.sympify(C['per_direction_energy']),C['both_white_energy'],'both directions')
    # Gaussian Fourier pulse filter 2-2cos(k cT); evaluate at cT=2.
    direct=s.integrate(s.exp(-v*v)*(2-2*s.cos(2*v)),(v,-s.oo,s.oo))
    expected=C['binary_gaussian_prefactor']*s.sqrt(s.pi)*(1-s.exp(-4/s.Integer(C['gaussian_exponent_denominator'])))
    eq(direct,expected,'Fourier pulse filter')
    eq(C['gaussian_budget_factor'],2*s.sympify(C['per_direction_energy']),'one-channel Gaussian bound')
    eq(C['white_budget_factor'],2*C['both_white_energy'],'equal-channel white bound')
    eq(C['heavy_tail_sign_probability']*2*s.zeta(2)/s.pi**2,1,'tail probability')
    # Construct correlated random variables X=sqrt2 Z1,Y=Z1/sqrt2+sqrt(5/2)Z2.
    variance=(2*s.sqrt(2)-1/s.sqrt(2))**2+s.Rational(5,2)
    eq(C['covariance_test_variance'],variance,'independent covariance construction')
    check(d['source_pins'][PIN]==sha(PIN),'dependency pin')
    return 8

def main():
    d=json.loads(REPORT.read_text());n=audit(d)
    for key,val in [('per_direction_energy','1'),('gaussian_exponent_denominator',2),('white_budget_factor',1),('heavy_tail_sign_probability',6),('covariance_test_variance',11)]:
        x=copy.deepcopy(d);x['coefficients'][key]=val
        try:audit(x)
        except AssertionError as e:check('[FAIL]' in str(e),'not crash');print('CAUGHT',key,str(e))
        else:raise AssertionError('[FAIL] survived '+key)
    x=copy.deepcopy(d);x['source_pins'][PIN]='0'*64
    try:audit(x)
    except AssertionError as e:check('[FAIL] dependency pin' in str(e),'pin catch');print('CAUGHT pin')
    else:raise AssertionError('[FAIL] pin survived')
    print('PASS K1898 probe:',n,'exact controls + pin; 4 math + 1 report + 1 pin faults caught')
if __name__=='__main__':main()
