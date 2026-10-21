"""Exact cut/primal and continuous integral controls, not a continuum grid proof."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def capacity(cap,A,B):return sum(cap[i][j] for i in range(len(cap)) for j in range(len(cap[0])) if A[i]!=B[j])
def optimum(cap,phi):
    best=F(0)
    for A in product([0,1],repeat=len(cap)):
        val=abs(sum(phi[i] for i in range(len(cap)) if A[i]))
        for B in product([0,1],repeat=len(cap[0])):
            cut=capacity(cap,A,B)
            if not cut:assert not val,'zero capacity imbalance'
            else:best=max(best,F(val,cut))
    return best

def calculate(jacobian=2, middle=3):
    checks=0
    def ck(x,label):
        nonlocal checks
        assert bool(x),label
        checks+=1
    cap=[[1,0,0],[1,1,0],[0,1,1],[0,0,1]];phi=[1,2,-2,-1]
    flow=[[1,0,0],[-1,middle,0],[0,-middle,1],[0,0,-1]]
    ck([sum(row) for row in flow]==phi,'primal row demands')
    ck([sum(row[j] for row in flow) for j in range(3)]==[0,0,0],'zero column demands')
    ck(all(abs(flow[i][j])<=3*cap[i][j] for i in range(4) for j in range(3)),'primal edge capacity')
    ck(optimum(cap,phi)==3,'global all-cut optimum')
    ck(max(F(abs(phi[i]),sum(cap[i])) for i in range(4))==1,'local row checks miss obstruction')
    ck(capacity(cap,[1,1,0,0],[1,0,0])==1,'bottleneck certificate')
    ck(optimum(cap,[-v for v in phi])==3,'sign symmetry')
    ck(optimum(cap,[0]*4)==0,'zero phase')
    z,L,d,c,T,m=s.symbols('z L d c T m',positive=True)
    short=s.integrate(z,(z,0,d/2))+s.integrate(d-z,(z,d/2,d))
    ck(s.simplify(short-d*d/4)==0,'short-duration cut area')
    long=s.integrate(z,(z,0,L))+L*(d-2*L)+s.integrate(d-z,(z,d-L,d))
    ck(s.simplify(long-L*(d-L))==0,'long-duration cut area')
    u=s.symbols('u',real=True)
    row=s.integrate(m,(z,-u,d+u));area=s.integrate(row,(u,-L,0))
    ck(s.simplify(area-m*long)==0,'continuous saturating primal equals cut')
    ck(s.simplify(jacobian*c/(short.subs(d,2*c*T))-2/(c*T*T))==0,'amplitude Jacobian and T-square scaling')
    # Threshold coarea identities on a nontrivial finite signed pair.
    f=[-2,0,1,3];g=[-1,2,0];levels=range(-3,3)
    rhs=sum(cap[i][j]*abs(f[i]+g[j]) for i in range(4) for j in range(3))
    cuts=sum(capacity(cap,[int(x>t) for x in f],[int(-x>t) for x in g]) for t in levels)
    ck(rhs==cuts,'threshold absolute-value identity')
    ck(sum(f[i]*phi[i] for i in range(4))==sum(sum(phi[i] for i in range(4) if f[i]>t) for t in levels),'zero-total threshold numerator')
    alpha=s.symbols('alpha',positive=True)
    ck(s.simplify(alpha*d+(1-alpha)*d/2-(1+alpha)*d/2)==0,'interior strip upper margin')
    ck(s.simplify(d/2-alpha*d/2-(1-alpha)*d/2)==0,'interior strip lower margin identity')
    t,y,z=s.symbols('t y z',real=True)
    g=6*t*(T-t)/T**3;f=-y**2/(4*c);r=y
    pulse=s.diff(g,t)*f+g*r
    ck(s.simplify(s.integrate(pulse,(t,0,T))-r)==0,'right characteristic exact correction')
    left=pulse.subs(y,z-2*c*t)
    ck(s.simplify(s.integrate(left,(t,0,T)))==0,'left characteristic exact cancellation')
    return {'finite_optimum':3,'local_row_lower_bound':1,'finite_primal':flow,'short_cut_area':'d^2/4 for d<=L','long_cut_area':'L*(d-L) for d>=2L','exact_class':'bounded measurable pulses at fixed real phase lift','smooth_exact_endpoint':'strict amplitude slack; fixed compact smooth phase','math_checks':checks}
def pins():
    p='explorations/conditional-build/k1902-fixed-support-scalar-noise-2026-10-21.md';return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');a=ap.parse_args();r=calculate();r['dependency_sha256']=pins()
    if a.write_report:(ROOT/'lab/process/k1914-scalar-control-transport-cuts.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r))
