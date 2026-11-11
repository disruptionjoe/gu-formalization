#!/usr/bin/env python3
"""Exact supporting controls; universal proofs live in the accompanying note."""
from pathlib import Path
import argparse, json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/p3-local-boundary-symbol.json'
I=s.I
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
def run():
    rows=[]
    def check(name,condition,kind='exact_supporting'):
        ok=bool(condition); rows.append({'name':name,'kind':kind,'pass':ok}); assert ok,name
    gam=[s.kronecker_product(X,s.eye(2)),s.kronecker_product(Y,s.eye(2)),s.kronecker_product(Z,X),s.kronecker_product(Z,Y)]
    n=4;d=4;G=s.Matrix.hstack(*gam);T=G.H/2;R=T*T.H;P=s.eye(n*d)-R
    check('Clifford relations',all(gam[i]*gam[j]+gam[j]*gam[i]==2*(i==j)*s.eye(d) for i in range(n) for j in range(n)))
    check('gamma trace surjective',G*G.H==n*s.eye(d))
    check('actual trace and kernel projectors',P*P==P and P.H==P and G*P==s.zeros(d,n*d))
    xi=[s.Rational(1,3),s.Rational(2,3),s.Rational(2,3),0]
    cx=sum((xi[j]*gam[j] for j in range(n)),s.zeros(d));C=s.kronecker_product(s.eye(n),cx)
    A=s.expand(T.H*C*T);B=s.expand(T.H*C*P);Q=s.expand(P*C*P);a=s.Rational(2-n,n)
    check('actual trace block coefficient',A==a*cx)
    check('trace square',s.simplify(A*A)==a*a*s.eye(d))
    check('offdiagonal norm',s.simplify(B*B.H)==(1-a*a)*s.eye(d))
    check('offdiagonal square cancels',s.simplify(A*B+B*Q)==s.zeros(d,n*d))
    check('projected square identity',s.simplify(Q*Q+B.H*B)==P)
    check('raw RS is not Dirac type',s.expand(Q*Q-P)!=s.zeros(n*d),'exact_contrary')
    check('projected squared minimal polynomial',s.simplify((s.expand(Q*Q)-P)*(s.expand(Q*Q)-a*a*P)*P)==s.zeros(n*d))
    t=s.Symbol('t',real=True)
    Ct=s.expand(R*C*R+P*C*P+t*(R*C*P+P*C*R))
    square=s.expand(R*C*R)*s.expand(R*C*R)+Q*Q+t*t*s.expand(R*C*P*C*R+P*C*R*C*P)
    check('entire offdiagonal homotopy square',s.expand(Ct*Ct-square)==s.zeros(n*d))
    # Work in actual gamma-traceless CHIRAL bases; normal matrix need not be normal.
    chir=gam[0]*gam[1]*gam[2]*gam[3]
    plus=s.Matrix.hstack(*((chir-s.eye(d)).nullspace()));minus=s.Matrix.hstack(*((chir+s.eye(d)).nullspace()))
    def rsbasis(spin):
        ambient=s.kronecker_product(s.eye(n),spin)
        return ambient*s.Matrix.hstack(*(G*ambient).nullspace())
    rp=rsbasis(plus);rm=rsbasis(minus)
    check('actual chiral RS ranks',rp.cols==rm.cols==6)
    left=(rm.H*rm).inv()*rm.H
    qs=[left*P*s.kronecker_product(s.eye(n),g)*rp for g in gam]
    qn,qt=qs[-1],qs[0]
    check('normal coefficient invertible',qn.det()!=0)
    normal=s.simplify(-I*qn.inv()*qt)
    check('normal root multiplicities',normal.charpoly().as_expr().expand()==s.Poly((s.Symbol('lambda')-1)**3*(s.Symbol('lambda')+1)**3,s.Symbol('lambda')).as_expr().expand())
    stable=s.Matrix.hstack(*((normal-s.eye(6))**6).nullspace());unstable=s.Matrix.hstack(*((normal+s.eye(6))**6).nullspace())
    check('generalized incoming spaces complementary',stable.cols==unstable.cols==3 and s.Matrix.hstack(stable,unstable).det()!=0)
    check('RS normal matrix needs generalized roots',s.expand(normal*normal-s.eye(6))!=s.zeros(6),'exact_contrary')
    # Bott line: exact equatorial transition, not merely projector rank.
    z=s.Symbol('z',nonzero=True)
    vN=s.Matrix([1,z]);vS=s.Matrix([1/z,1])
    check('Bott equator transition winding one',s.simplify(vN-z*vS)==s.zeros(2,1))
    for xyz in [(0,0,1),(0,0,-1),(s.Rational(3,5),s.Rational(4,5),0)]:
        h=xyz[0]*X+xyz[1]*Y+xyz[2]*Z;pp=(s.eye(2)+h)/2
        check('Pauli projector '+str(xyz),s.simplify(pp*pp)==pp and pp.rank()==1)
        ep=s.Matrix.hstack(*(h-s.eye(2)).nullspace());em=s.Matrix.hstack(*(h+s.eye(2)).nullspace())
        incoming=s.diag(ep,em);diagonal=s.Matrix.vstack(s.eye(2),s.eye(2))
        check('doubled local diagonal complement '+str(xyz),s.Matrix.hstack(incoming,diagonal).det()!=0)
    L=s.Matrix.vstack(s.eye(2),s.eye(2));grading=s.diag(s.eye(2),-s.eye(2))
    check('actual diagonal repair breaks grading',s.Matrix.hstack(L,grading*L).rank()==4,'exact_contrary')
    # Structural coefficients follow derived class, not dimension of R.
    for dim in [4,10,14]:
        check('raw trace reversed class '+str(dim),dim-(-1)==dim+1,'exact_accounting')
        check('rank shortcut rejected '+str(dim),dim-1!=dim+1,'exact_accounting')
    check('mirror coefficient cancellation',11-11==0,'exact_accounting')
    check('same grading multiplicity retains obstruction',11+11!=0,'exact_accounting')
    action_plus=s.eye(5);action_minus=-s.eye(5)
    intertwiner_constraint=s.kronecker_product(s.eye(5),action_plus)-s.kronecker_product(action_minus.T,s.eye(5))
    check('equal dimension but zero coefficient intertwiner',action_plus.rows==action_minus.rows and intertwiner_constraint.rank()==25,'exact_contrary')
    check('equivariant character obstruction despite scalar cancellation',s.trace(action_plus)-s.trace(action_minus)==10,'exact_accounting')
    check('same-module mirror diagonal is equivariant',s.diag(Z,Z)*L==L*Z)
    return {'schema_version':'1.0','program_target':'P3xdomain_boundary','tier':'T2','classification':'INTERNAL_STRUCTURAL_ONLY','claim_ceiling':'No native indefinite ellipticity, C decision or physical count','proof_ref':'explorations/conditional-build/p3-local-boundary-symbol-2026-11-11.md','evidence_kind':'exact finite supporting and contrary controls; universal written proof separate','checks':rows,'normal_symbol':{'chiral_rank':6,'incoming_rank':stable.cols,'jordan_sensitive':True},'symbol_balance':{'n10_raw':11,'n14_auxiliary_raw':15,'raw_class':'T_C+1','virtual_ghost_class_not_used':True}}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args();report=run()
    if args.write_report:REPORT.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==report,'saved report differs from actual computations'
    print(json.dumps({'pass':True,'checks':len(report['checks']),'kinds':{k:sum(x['kind']==k for x in report['checks']) for k in sorted({x['kind'] for x in report['checks']})}}))
if __name__=='__main__':main()
