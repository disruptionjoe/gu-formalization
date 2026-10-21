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

def calculate():
    x,t,c,l,T,a,sigma=s.symbols('x t c l T a sigma',positive=True)
    theta=s.exp(-x*x/(2*l*l))
    norm=s.integrate(s.diff(theta,x)**2,(x,-s.oo,s.oo));eq(norm,s.sqrt(s.pi)/(2*l),'Gaussian derivative energy')
    shift=s.symbols('shift',real=True)
    overlap=s.sqrt(s.pi)*l*s.exp(-shift**2/(4*l*l))
    # Complete the square, then integrate by translation.
    eq(theta*s.exp(-(x+shift)**2/(2*l*l)),s.exp(-(x+shift/2)**2/l**2)*s.exp(-shift**2/(4*l*l)),'overlap square completion')
    eq(s.integrate(s.exp(-x*x/l**2),(x,-s.oo,s.oo)),s.sqrt(s.pi)*l,'Gaussian overlap normalization')
    Fnorm=2*(s.sqrt(s.pi)*l-overlap.subs(shift,c*T))/c**2
    energy=s.simplify(a*a*c/s.pi*Fnorm)
    expected=2*a*a*l/(s.sqrt(s.pi)*c)*(1-s.exp(-c*c*T*T/(4*l*l)))
    eq(energy,expected,'binary energy')
    eq(s.limit(energy/T**2,T,0),a*a*c/(2*s.sqrt(s.pi)*l),'small-time quadratic energy')
    eq(s.limit(energy,T,s.oo),2*a*a*l/(s.sqrt(s.pi)*c),'saturation')
    white=c*sigma**2*T/s.pi*norm
    eq(white,c*sigma**2*T/(2*s.sqrt(s.pi)*l),'white energy')
    k=s.symbols('k',positive=True);q=s.symbols('q',real=True)
    eq(s.integrate(c*(q+k),(q,-k,0)),c*k*k/2,'crossing positive energy')
    eq(s.integrate(-c*q,(q,-k,0)),c*k*k/2,'crossing hole energy')
    # One r has one crossing direction for particles, the opposite for holes.
    n=s.symbols('n',integer=True,positive=True)
    eq(2*3/s.pi**2*s.summation(n**-2,(n,1,s.oo)),1,'heavy-tail probability normalization')
    check(s.summation(s.Integer(1),(n,1,s.oo))==s.oo,'amplitude second moment diverges')
    C=s.Matrix([[2,1],[1,3]]);v=s.Matrix([2,-1]);eq((v.T*C*v)[0],7,'correlated Gaussian variance')
    check(C.det()>0 and C[0,0]>0,'positive covariance');eq((v.T*s.diag(2,3)*v)[0],11,'independent noise discriminator')
    # Characteristic phase derivative, for an arbitrary smooth profile.
    z=s.symbols('z');f=s.Function('f');g=s.Function('g')
    for sign in [-1,1]:
        Phi=s.Integral(g(z)*f(x-sign*c*(t-z)),(z,0,t))
        eq(s.diff(Phi,t)+sign*c*s.diff(Phi,x),g(t)*f(x),'characteristic transport '+str(sign))
    return {'artifact':'K1898','coefficients':{'per_direction_energy':'1/2','both_white_energy':1,'binary_gaussian_prefactor':2,'gaussian_exponent_denominator':4,'gaussian_budget_factor':1,'white_budget_factor':2,'heavy_tail_sign_probability':3,'covariance_test_variance':7},'evidence_kind':'16 exact analytic/symbolic controls; full stochastic proof in exploration','source_pins':{PIN:sha(PIN)},'scope':'massless rank-four R1 control; mean excitation energy, not 3D noise limit'}
def main():
    data=calculate()
    if '--write' in sys.argv:REPORT.write_text(json.dumps(data,indent=2)+'\n')
    else:check(json.loads(REPORT.read_text())==data,'serialized report and dependency pin')
    print('PASS K1898: 16 exact controls; report/pin consistency')
if __name__=='__main__':main()
