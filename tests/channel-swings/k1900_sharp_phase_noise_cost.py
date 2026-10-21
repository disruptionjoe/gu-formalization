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
REPORT='lab/process/k1900-sharp-phase-noise-cost.json'
PIN='lab/process/k1898-stochastic-pulse-energy-coherence.json'
def calculate():
    u=s.symbols('u',positive=True);x=s.symbols('x',positive=True)
    eq(s.diff(s.cos(s.sqrt(u)),u,2).subs(u,x*x),(s.sin(x)-x*s.cos(x))/(4*x**3),'convexity derivative')
    eq(s.diff(s.sin(x)-x*s.cos(x),x),x*s.sin(x),'convex numerator derivative')
    eq(s.limit(s.diff(s.cos(s.sqrt(u)),u),u,s.pi**2,dir='-'),0,'convex join slope')
    theta=s.symbols('theta',real=True)
    eq((s.exp(s.I*theta)+s.exp(-s.I*theta))/2,s.cos(theta),'binary characteristic function')
    signs=[(1,1),(1,-1),(-1,1),(-1,-1)]
    vec=[s.Matrix([1,s.exp(s.I*a*s.pi/2),s.exp(s.I*(a+b)*s.pi/2)]) for a,b in signs]
    gram=sum((v*v.H/4 for v in vec),s.zeros(3)).applyfunc(s.simplify)
    ck(gram==s.eye(3),'four histories exact complete dephasing')
    binary=(vec[0]*vec[0].H+vec[3]*vec[3].H)/2
    ck(binary.rank()==2 and binary[0,2]==-1,'binary failure for third coherence')
    ps=s.symbols('p0:4',real=True)
    sol=s.solve([sum(ps)-1,ps[0]+ps[1]-ps[2]-ps[3],ps[0]+ps[2]-ps[1]-ps[3],ps[0]+ps[3]-ps[1]-ps[2]],ps)
    ck(all(sol[p]==s.Rational(1,4) for p in ps),'unique optimal increment law')
    a,b,g1,g2=s.symbols('a b g1 g2',positive=True)
    z=s.symbols('z',real=True)
    eq(s.integrate((a/g1)**2,(z,0,g1)),a*a/g1,'ramp Dirichlet cost')
    eq((s.pi/2)**2/(2*s.pi),s.pi/8,'three-mode energy coefficient')
    third=s.simplify((0+2*(2*s.pi/3)**2)/3)
    eq(third,8*s.pi**2/27,'three-history phase variance')
    eq(third/(s.pi/2)**2,s.Rational(32,27),'three-history control ratio')
    rho=s.ones(3)/3;out=s.matrix_multiply_elementwise(rho,gram)
    ck(out==s.eye(3)/3,'one-particle neutral density dephasing')
    # Explicit smooth moving-potential primitive along a characteristic.
    t,c=s.symbols('t c',real=True);phi=s.Function('phi');G=s.Function('G')
    phase=G(t)*phi(z);eq(s.diff(phase,t),s.diff(G(t),t)*phi(z),'moving-frame exact primitive')
    xx=s.symbols('xx',real=True);ff=s.Function('f');gg=s.Function('g')
    F=gg(t)*ff(xx-c*t);VV=s.diff(F,t)-c*s.diff(F,xx)
    right=VV.subs(xx,z+c*t).doit()
    eq(right,s.diff(gg(t),t)*ff(z)-2*c*gg(t)*s.diff(ff(z),z),'scalar right characteristic')
    left=F.subs(xx,z-c*t)
    eq(VV.subs(xx,z-c*t).doit(),s.diff(left,t),'scalar left total derivative')
    A,L=s.symbols('A L',positive=True);bump=s.Function('b')
    eq(s.diff(-A/L*bump(xx/L),xx),-A/L**2*s.Subs(s.diff(bump(z),z),z,xx/L),'zero-integral bump derivative scale')
    C=s.Matrix([[1,1,0],[1,1,1],[0,1,1]])
    ck(C.det()==-1,'infeasible requested coherence matrix')
    return dict(result_id='K1900',coefficients=dict(arbitrary_law_cost='acos(eta)**2',one_channel_factor='1/2',three_mode_factor='1/8',three_history_ratio='32/27'),optimal_increment_probabilities=['1/4']*4,three_mode_gram=[[int(gram[i,j]) for j in range(3)] for i in range(3)],checks=17,source_pins={PIN:sha(PIN)},scope='sharp scalar spacetime-potential infimum with unrestricted support/amplitude; zero-integral correction and characteristic construction')
if __name__=='__main__':
    d=calculate()
    if '--write' in sys.argv:(ROOT/REPORT).write_text(json.dumps(d,indent=2)+'\n')
    else:ck(d==json.loads((ROOT/REPORT).read_text()),'report consistency')
    print('PASS K1900: 17 exact controls; report/pin')
