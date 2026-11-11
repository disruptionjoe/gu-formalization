"""Exact finite controls for a separately proved infinite-dimensional theorem."""
from pathlib import Path
import json,sys
import sympy as s
checks=[];contrary=[]
def check(name,value,negative=False):
    assert bool(value),name
    (contrary if negative else checks).append(name)
def zero(a):return all(s.simplify(x)==0 for x in a)
def run():
    checks.clear();contrary.clear()
    I=s.eye(2);sx=s.Matrix([[0,1],[1,0]]);sz=s.diag(1,-1);c=s.Matrix([[0,1],[-1,0]])
    l,k=s.symbols('lambda k',real=True);A=l*sz;Q=A+k*sx
    check('Q squared scalar polynomial',zero(Q*Q-(l*l+k*k)*I))
    check('normal skew unitary',c.T==-c and c*c==-I)
    check('normal anticommutes with repaired operator',zero(c*Q+Q*c))
    check('grading commutes with original adapted operator',zero(sz*A-A*sz))
    check('repair breaks grading for nonzero mass',not zero(sz*Q-Q*sz),True)
    for a,b in [(s.Rational(3,5),s.Rational(4,5)),(-s.Rational(3,5),s.Rational(4,5)),(0,1),(1,0),(-1,0)]:
        P=(I+a*sz+b*sx)/2
        check(f'projection {a},{b}',zero(P*P-P) and P.T==P)
        check(f'Green complement {a},{b}',zero(c*P-(I-P)*c))
    P0=(I+sx)/2
    check('zero crossing repair fails grading',not zero(sz*P0-P0*sz),True)
    check('high positive mode unchanged',(I+sz)/2==s.diag(1,0))
    check('high negative mode unchanged',(I-sz)/2==s.diag(0,1))
    n,t=s.symbols('n t',real=True);lam=lambda n,t:n+t+s.Rational(1,2)
    check('correct clutch shifts Fourier label down',s.expand(lam(n,1)-lam(n+1,0))==0)
    check('wrong clutch direction rejected',s.expand(lam(n,1)-lam(n-1,0))!=0,True)
    check('one upward crossing away from endpoints',lam(-1,s.Rational(1,2))==0 and lam(-1,0)<0 and lam(-1,1)>0)
    check('antilinear reflection includes minus and offset',s.expand(lam(-n,t)+lam(n,-t-1))==0)
    check('scalar conjugation is not generic fixed parameter symmetry',s.expand(lam(-n,t)-lam(n,t))!=0,True)
    # Exact finite window trace defect; no cyclic wraparound is admitted.
    for N in [2,4,8]:
        q=lambda j:int(j>=0)
        defect=sum(q(j+1)-q(j) for j in range(-N,N+1))
        check(f'one rank crossing in window{N}',defect==1)
    labels=list(range(-3,4));diag=[int(j>=0) for j in labels]
    check('cyclic truncation erases defect spuriously',sum(diag[1:]+diag[:1])-sum(diag)==0,True)
    # Representation multiplicities, not just dimensions.
    cases=[([1,0],[1,0],True),([1,0],[0,1],False),([2,1],[1,2],False),([2,3],[2,3],True)]
    for plus,minus,ok in cases:
        check(f'isotypic criterion {plus},{minus}',all(a-b==0 for a,b in zip(plus,minus))==ok)
    check('equal total dimensions insufficient',sum(cases[1][0])==sum(cases[1][1]) and cases[1][2] is False,True)
    plus,minus=[2,1],[1,2];balanced=[3,5]
    check('balanced stabilization preserves every defect',[a-b for a,b in zip(plus,minus)]==[a+x-b-x for a,b,x in zip(plus,minus,balanced)])
    # A nontrivial multiplicity intertwiner executes the actual repair formula.
    T=s.Matrix([[0,1],[-1,0]]);Z=s.zeros(2);A4=s.diag(l,l,-l,-l)
    M=s.BlockMatrix([[Z,T.T],[T,Z]]).as_explicit();Q4=A4+k*M
    check('intertwining mass squared exact',zero(Q4*Q4-(l*l+k*k)*s.eye(4)))
    rho_plus=s.diag(1,-1);rho_minus=T*rho_plus*T.T;rho=s.diag(rho_plus,rho_minus)
    check('nontrivial equivariant repair',zero(rho*Q4-Q4*rho))
    badrho=s.diag(1,1,-1,-1)
    check('mismatched representations reject mass',not zero(badrho*Q4-Q4*badrho),True)
    return dict(schema_version='1.0',artifact='p3-equivariant-spectral-sections',supporting_checks=checks,contrary_controls=contrary,claim_effect='none',proof_scope='Finite symbolic controls only. Infinite spectral-section obstruction, smooth functional calculus and uniform gap are proved in the note; no GU domain or count realization.')
if __name__=='__main__':
    data=run();p=Path(__file__).resolve().parents[2]/'lab/process/p3-equivariant-spectral-sections.json'
    if '--write' in sys.argv:p.write_text(json.dumps(data,indent=2)+'\n')
    else:assert json.loads(p.read_text())==data
    print(f'{len(checks)} supporting checks; {len(contrary)} contrary controls')
