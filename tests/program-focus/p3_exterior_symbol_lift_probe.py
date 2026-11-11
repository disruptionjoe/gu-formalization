"""Exact supporting controls; universal classification is proved in the note."""
import json
from pathlib import Path
import sympy as s

checks = []
contrary = []
def check(name, value, negative=False):
    assert bool(value), name
    (contrary if negative else checks).append(name)
def zero(m):
    return all(s.simplify(x) == 0 for x in m)
def run():
    checks.clear(); contrary.clear()
    x,y=s.symbols('x y', real=True)
    def cov(f,A,B): return (f.diff(x)+A*f,f.diff(y)+B*f)
    def curl(v,C,D): return -v[0].diff(y)+v[1].diff(x)+C*v[0]+D*v[1]
    # Independently compose generic matrix operators on arbitrary second jets.
    A=s.Matrix(2,2,s.symbols('a:4'));B=s.Matrix(2,2,s.symbols('b:4'))
    C=s.Matrix(2,2,s.symbols('c:4'));D=s.Matrix(2,2,s.symbols('d:4'))
    jets=s.symbols('j:12')
    f=s.Matrix([jets[6*i]+jets[6*i+1]*x+jets[6*i+2]*y+
                jets[6*i+3]*x*x/2+jets[6*i+4]*x*y+jets[6*i+5]*y*y/2 for i in range(2)])
    expr=curl(cov(f,A,B),C,D).subs({x:0,y:0})
    first=[s.expand(v).coeff(j) for v in expr for j in (jets[1],jets[2],jets[7],jets[8])]
    sols=s.solve(first,list(C)+list(D),dict=True)
    check('unique lower completion from independent first jets',len(sols)==1 and len(sols[0])==8)
    check('completion equals induced exterior connection',C.subs(sols[0])==-B and D.subs(sols[0])==A)
    check('zero jet leaves curvature commutator',zero(expr.subs(sols[0])-(A*B-B*A)*s.Matrix([jets[0],jets[6]])))
    check('arbitrary second jets cancel',all(not v.has(j) for v in expr for j in (jets[3],jets[4],jets[5],jets[9],jets[10],jets[11])))
    G=s.Matrix([[1,x*y],[0,1]]);Ax=G.inv()*G.diff(x);Ay=G.inv()*G.diff(y)
    params=[s.Matrix([1,x+y]),s.Matrix([x*x+y,x*y*y]),s.Matrix([x*y,x*x*y+y*y])]
    for i,f in enumerate(params): check(f'nonconstant flat composition {i}',zero(curl(cov(f,Ax,Ay),-Ay,Ax)))
    check('changing lower correction breaks first jet',not zero(curl(cov(params[1],Ax,Ay),-Ay+s.eye(2),Ax)),True)
    f=params[1]
    check('nonflat identical symbol gives value obstruction',zero(curl(cov(f,s.zeros(2),x*s.eye(2)),-x*s.eye(2),s.zeros(2))-f))
    check('principal syzygy alone is insufficient',not zero(f),True)
    N=s.Matrix([[0,0],[1,0]]);P=s.diag(0,1);Ax=N;Ay=x*P+x*x*N/2
    F=Ay.diff(x)-Ax.diff(y)+Ax*Ay-Ay*Ax
    e1=s.Matrix([1,0]);e2=s.Matrix([0,1])
    check('nonparallel control curvature',F==P)
    check('curvature kernel has constant rank one',F.rank()==1 and F*e1==s.zeros(2,1))
    check('truncated arbitrary parameter identity',zero(curl(cov(e1*(x*x*y+y*y),Ax,Ay),-Ay,Ax)))
    check('kernel coefficient subbundle not preserved',Ax*e1==e2,True)
    check('covariant curvature derivative rejects flat subbundle',(Ax*F-F*Ax)*e1==-e2,True)
    theta=s.symbols('theta',real=True)
    parallel=s.exp(-s.I*theta/2)
    check('local parallel section solves connection equation',s.simplify(s.diff(parallel,theta)+s.I*parallel/2)==0)
    check('flat holonomy is minus one',s.simplify(parallel.subs(theta,2*s.pi))==-1)
    check('local flat frame is not periodic',parallel.subs(theta,0)!=s.simplify(parallel.subs(theta,2*s.pi)),True)
    return dict(schema_version='1.0',artifact='p3-exterior-symbol-lift',supporting_checks=checks,contrary_controls=contrary,
                claim_effect='none',proof_scope='Exact finite symbolic controls; all-completion and global proofs are in the note.')

if __name__=='__main__':
    import sys
    data=run();path=Path(__file__).resolve().parents[2]/'lab/process/p3-exterior-symbol-lift.json'
    if '--write' in sys.argv: path.write_text(json.dumps(data,indent=2)+'\n')
    else: assert json.loads(path.read_text())==data
    print(f"PASS {len(checks)} supporting checks; {len(contrary)} contrary controls; saved report replay")
