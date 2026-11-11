"""Exact endpoint and clutching controls; not a continuum proof by sampling."""
import json
from pathlib import Path
import sympy as s

checks=[];contrary=[]
def check(name,value,negative=False):
    assert bool(value),name
    (contrary if negative else checks).append(name)
def zero(m): return all(s.simplify(v)==0 for v in m)
def run():
    checks.clear();contrary.clear()
    x,t=s.symbols('x t',real=True)
    V=s.eye(2);E=s.zeros(2,0);u=V[:,0];v=V[:,1]
    cases=[('free',V,V,2,0),('mixed',E,V,0,0),('relative',E,E,0,2),
           ('same line',u,u,1,1),('complement',u,v,0,0),('oblique',u,u+v,0,0)]
    for name,U,W,h0,h1 in cases:
        T=(-U).row_join(W)
        check(name+' exact cohomology dimensions',T.cols-T.rank()==h0 and 2-T.rank()==h1)
        check(name+' Euler index',h0-h1==U.cols+W.cols-2)
    check('zero scalar index leaves cohomology',cases[3][3]-cases[3][4]==0 and cases[3][3]>0,True)
    # Independent polynomial test of graph-space decomposition, including endpoints.
    c=s.Matrix([2,0]);w=s.Matrix([0,3]);g=s.Matrix([2*x-1,6*x*x-2])
    check('input fluctuation has zero mean',zero(s.integrate(g,(x,0,1))))
    path=c+x*(w-c)+s.integrate(g.subs(x,t),(t,0,x))
    check('graph reconstruction endpoints',path.subs(x,0)==c and path.subs(x,1)==w)
    check('graph reconstruction differential',zero(path.diff(x)-(w-c)-g))
    check('graph reconstruction inverse',zero(path.diff(x)-(path.subs(x,1)-path.subs(x,0))-g))
    P=s.Matrix([[1,-1],[0,0]]) # U=e1, W=e1+e2
    f=s.Matrix([x*x+2*x,x+1]);mean=s.integrate(f,(x,0,1))
    h=-P*mean+s.integrate(f.subs(x,t),(t,0,x))
    check('oblique inverse left endpoint',h.subs(x,0)[1]==0)
    end=h.subs(x,1);check('oblique inverse right endpoint',end[0]==end[1])
    check('right contraction identity',zero(h.diff(x)-f))
    p=s.Matrix([1+x*x,2*x*x]);mean2=s.integrate(p.diff(x),(x,0,1))
    check('left contraction identity',zero(-P*mean2+s.integrate(p.diff(x).subs(x,t),(t,0,x))-p))
    # Family of endpoint subspaces in homogeneous coordinates, exact complex algebra.
    a,b=s.symbols('a b',real=True);z=a+s.I*b
    north=s.Matrix([1,z]);south=s.Matrix([1/z,1])
    check('tautological clutching relation',zero(north-z*south))
    check('fixed-line family has isolated rank drop',s.simplify((-north).row_join(u).det())==z)
    theta=s.symbols('theta',real=True);transition=s.exp(s.I*theta)
    winding=s.integrate(s.simplify(s.diff(transition,theta)/transition),(theta,0,2*s.pi))/(2*s.pi*s.I)
    check('transition winding detects reduced class',s.simplify(winding)==1)
    check('pointwise zero index does not erase clutching',1+1-2==0 and winding!=0,True)
    orth=s.Matrix([-s.conjugate(z),1]);norm=1+a*a+b*b
    check('complement family orthogonality',zero(north.conjugate().T*orth))
    check('complement family determinant never zero',s.simplify(north.row_join(orth).det()-norm)==0)
    proj=north*north.conjugate().T/norm
    check('global projector idempotent and Hermitian',zero(proj*proj-proj) and zero(proj.conjugate().T-proj))
    check('complement is projector kernel',zero(proj*orth) and zero(proj*north-north))
    hf=-proj*mean+s.integrate(f.subs(x,t),(t,0,x))
    check('family inverse domain endpoints',zero((s.eye(2)-proj)*hf.subs(x,0)) and zero(proj*hf.subs(x,1)))
    check('family inverse differential',zero(hf.diff(x)-f))
    Gamma=s.diag(1,-1);plus=s.Matrix([1,1]);minus=s.Matrix([1,-1])
    check('ungraded pair is complementary',plus.row_join(minus).det()!=0)
    check('ungraded contraction does not preserve supplied grading',plus.row_join(Gamma*plus).rank()==2 and minus.row_join(Gamma*minus).rank()==2,True)
    return dict(schema_version='1.0',artifact='p3-auxiliary-domain-family',supporting_checks=checks,contrary_controls=contrary,
                claim_effect='none',proof_scope='Finite exact endpoint/projector/clutching controls; graph-space and family proofs are written separately.')

if __name__=='__main__':
    import sys
    data=run();path=Path(__file__).resolve().parents[2]/'lab/process/p3-auxiliary-domain-family.json'
    if '--write' in sys.argv:path.write_text(json.dumps(data,indent=2)+'\n')
    else:assert json.loads(path.read_text())==data
    print(f"PASS {len(checks)} supporting checks; {len(contrary)} contrary controls; saved report replay")
