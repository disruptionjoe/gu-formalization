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
PINS=['lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json','lab/process/k1897-smooth-pulse-energy.json']
def calculate():
    d=json.loads((ROOT/PINS[0]).read_text());D=list(map(mat,d['target_D']))
    v,w,c,rr=s.symbols('v w c r',real=True,nonzero=True)
    N=D[2];V=v*D[0]+w*D[1];alpha=s.I*V/(4*c*rr**2)
    ck(alpha.H==-alpha,'antihermitian endpoint generator')
    comm=N*alpha-alpha*N
    eq(s.trace(comm.H*comm),(v*v+w*w)/(c*c*rr**4),'actual target symbol trace')
    ck(N*V+V*N==s.zeros(4),'perpendicular Clifford cancellation')
    ck(N*N==s.eye(4),'unit direction')
    # Non-axis rational direction and arbitrary gradient test.
    n=[s.Rational(2,3),s.Rational(1,3),s.Rational(2,3)];g=[2,-1,4]
    nd=sum((n[j]*D[j] for j in range(3)),s.zeros(4));dot=sum(n[j]*g[j] for j in range(3))
    vp=[g[j]-n[j]*dot for j in range(3)];vd=sum((vp[j]*D[j] for j in range(3)),s.zeros(4))
    a=s.I*vd/4;b=nd*a-a*nd
    eq(s.trace(b.H*b),sum(z*z for z in vp),'rotated actual symbol')
    z=s.symbols('z',real=True);angular=2*s.pi*s.integrate(1-z*z,(z,-1,1))
    eq(angular,8*s.pi/3,'sphere transverse integral')
    coeff=s.simplify(angular/(4*(2*s.pi)**3))
    eq(coeff,1/(12*s.pi**2),'log coefficient without c')
    R,L=s.symbols('R L',positive=True)
    eq(s.integrate(1/R,(R,1,L)),s.log(L),'energy logarithm')
    eq(s.integrate(1/R**2,(R,1,s.oo)),1,'number convergence')
    eq(s.integrate(R**s.Rational(-3,2),(R,1,s.oo)),2,'half moment convergence')
    eq(s.integrate(1/R**3,(R,1,s.oo)),s.Rational(1,2),'zero potential endpoint energy remainder')
    ell=s.symbols('ell',positive=True)
    gn=s.simplify(4*s.pi/ell**4*s.integrate(R**4*s.exp(-R*R/ell**2),(R,0,s.oo)))
    eq(gn,3*s.pi**s.Rational(3,2)*ell/2,'3D Gaussian gradient')
    eq(gn*coeff/ell,1/(8*s.sqrt(s.pi)),'Gaussian log coefficient')
    eq(coeff*24,2/s.pi**2,'actual speed coefficient')
    return dict(result_id='K1899',coefficients=dict(symbol_trace_factor=1,angular_factor='8/3',log_factor='1/12',gaussian_factor='1/8',threshold=1,raw_remainder='O(sqrt(log L))'),checks=14,source_pins={p:sha(p) for p in PINS},scope='fixed free sea, outgoing momentum cutoff; continuum proof in note; not renormalized stress energy')
if __name__=='__main__':
    d=calculate()
    if '--write' in sys.argv:(ROOT/REPORT).write_text(json.dumps(d,indent=2)+'\n')
    else:ck(d==json.loads((ROOT/REPORT).read_text()),'report consistency')
    print('PASS K1899: 14 exact matrix/integral controls; report and 3 pins')
