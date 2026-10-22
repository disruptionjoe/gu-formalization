"""Exact controls for the analytic approximate-channel shell stability theorem."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

def target(fault=None):
    vs=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1])/s.sqrt(2),s.Matrix([1,s.I])/s.sqrt(2)]
    if fault=='phase':vs[3]=s.conjugate(vs[3])
    return vs

def rounding(p,q,fault=None):
    d=len(p)
    alpha=(1-q)*p[0]+q*p[-1]+2*sum(min((1-q)*p[n],q*p[n-1]) for n in range(1,d))
    if fault=='scalar_weight':alpha/=2
    removed={0,d-1}
    for n in range(1,d):
        if fault!='adjacency':removed.add(n if p[n]<=p[n-1] else n-1)
    S=set(range(d))-removed
    return alpha,S,sum(p[n] for n in removed)

def calculate(fault=None):
    n=0
    def ck(x,label):
        nonlocal n
        assert bool(x),label;n+=1
    rt=s.sqrt(2);h=4+rt;delta=6-4*rt;c0=delta/(16*h)
    vs=target(fault);V=s.Matrix.hstack(*vs)
    B=s.Matrix([[-1,-1,rt,0],[-1,-s.I,0,rt]])
    C=s.Matrix(4,4,lambda j,l:(vs[l].H*vs[j])[0])
    ck(s.simplify(V*B.T)==s.zeros(2,2),'complex target null relations')
    ck(s.simplify(s.trace(B.H*B*C))==0,'normalized Choi target witness')
    ck(set((B*B.H).eigenvals())=={4-rt,4+rt},'witness norm')
    ck(s.Matrix.hstack(*[s.Matrix(list(v*v.H)) for v in vs]).rank()==4,'extreme target tomography')
    ck(s.simplify(16*h/delta-1/c0)==0,'scalar mass error coefficient')
    ck(s.simplify((1+rt)**2-(3+2*rt))==0,'residual norm coefficient')
    # Independent-shell positive decomposition, including asymmetric populations.
    for a,b in [(F(0),F(1,3)),(F(1,9),F(2,9)),(F(2,5),F(1,7)),(F(1,4),F(1,4))]:
        m=min(a,b);excess=(a-m,b-m)
        ck(min(excess)>=0 and min(excess)==0,'positive rank-one excess')
        ck(2*m+sum(excess)==a+b,'scalar/excess trace identity')
    cases=0
    for d in range(1,7):
        for raw in product(range(3),repeat=d):
            if not sum(raw):continue
            p=[F(x,sum(raw)) for x in raw]
            for q in (F(1,10),F(1,3),F(1,2)):
                alpha,S,eta=rounding(p,q,fault)
                ck(eta<=alpha/q,'rounding lost mass bound')
                ck(all(0<a<d-1 and a+1 not in S and a-1 not in S for a in S),'internal independent support')
                cases+=1
    # Residual/overlap identities on genuinely complex contractions.
    samples=[(vs[0],vs[1],vs[2],vs[3]),
             (s.Matrix([s.Rational(3,5),s.Rational(4,5)]),s.Matrix([s.I/2,0]),s.Matrix([s.Rational(1,3),0]),s.Matrix([0,s.I/3])),
             (s.Matrix([1,0]),s.Matrix([1,0]),s.Matrix([1,0]),s.Matrix([s.I,0]))]
    for x1,x2,x3,x4 in samples:
        z=(x1.H*x2)[0];n1=(x1.H*x1)[0];n2=(x2.H*x2)[0]
        y3=(x1+x2)/rt;y4=(x1+s.I*x2)/rt
        ck(s.simplify((y3.H*y3)[0]-(n1+n2)/2-s.re(z))==0,'real overlap identity')
        ck(s.simplify((y4.H*y4)[0]-(n1+n2)/2+s.im(z))==0,'imaginary overlap sign')
        for y,x,u in [(y3,x3,s.re(z)),(y4,x4,-s.im(z))]:
            gap=s.simplify(u-(2-n1-n2)/2);R=s.simplify(((x-y).H*(x-y))[0])
            if gap.is_positive:ck(s.simplify((3+2*rt)*R-gap**2).is_nonnegative,'positive-part residual inequality')
        gram=s.Matrix([[n1,z],[s.conjugate(z),n2]]);bound=1+s.Abs(z)
        ck(all(s.simplify(bound-e).is_nonnegative for e in gram.eigenvals()),'rank-one support eigenvalue bound')
    # Algebra of the accumulated constants, separately from any numerical example.
    eta,e,L=s.symbols('eta e L',real=True)
    drop=(1-eta)-((1-eta)/2+L/2+e+eta)
    ck(s.expand(drop.subs(L,8*e+2*eta)- (s.Rational(1,2)-5*e-s.Rational(5,2)*eta))==0,'support probability bookkeeping')
    return {'exact_checks':n,'rounding_cases':cases,'half_diamond_error':'epsilon',
            'bound':'max(0,1/2-2*(1+sqrt(2))*sqrt((4+sqrt(2))*epsilon)-5*epsilon-(5/2)*min(1,epsilon/(q*c0)))',
            'c0':'(6-4*sqrt(2))/(16*(4+sqrt(2)))',
            'fixed_input':'(|1><1|+|2><2|)/2',
            'scope':'finite faithful thermal qubit; nondegenerate catalyst; exact additive conservation; arbitrary coherent preparation',
            'universal_proof':'analytic; finite controls are supplementary'}

def report():
    data=calculate();data['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();return data
if __name__=='__main__':
    import sys
    data=report()
    if '--write' in sys.argv:(ROOT/'lab/process/k1931-thermal-qubit-channel-stability.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data))
