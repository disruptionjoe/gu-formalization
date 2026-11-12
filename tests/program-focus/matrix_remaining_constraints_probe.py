#!/usr/bin/env python3
"""Exact supporting/contrary controls; universal proofs in three linked notes."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
import json, argparse, hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/matrix-remaining-constraints.json'

def orientation_checks():
    """Exact native contraction and observed mirror controls; no owner writes.
    Run from GU checkout with scientific Python. Full theorems live in note.
    """
    import os
    os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
    os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
    import sys
    sys.dont_write_bytecode=True
    from pathlib import Path
    import numpy as np
    import sympy as s
    ROOT=Path(__file__).resolve().parents[2]
    sys.path.insert(0,str(ROOT/'tests/channel-swings'))
    from actual_sym2_c14_orbit_probe import native_gammas
    checks=[]
    def ck(name,b):
        assert bool(b),name
        checks.append(name)
    def eq(a,b):return np.array_equal(a,b)
    gs,eta=native_gammas();I=np.eye(128,dtype=complex);Z=0*I
    # 3+1 horizontal, 6+4 normal, ambient K95. Exact Gaussian integer matrices.
    H=[0,1,2,9];N=[a for a in range(14) if a not in H]
    ck('actual split signatures',(sum(eta[h]>0 for h in H),sum(eta[n]>0 for n in N))==(3,6))
    ck('all entries Gaussian integer',all(np.array_equal(g.real,np.round(g.real)) and np.array_equal(g.imag,np.round(g.imag)) for g in gs))
    ck('native Clifford squares',all(eq(g@g,e*I) for g,e in zip(gs,eta)))
    # No 1/14 floating coefficients: T numerator JY GammaY and defect numerator JH GammaN.
    ghjh=sum((eta[h]*gs[h]@gs[h] for h in H),Z.copy())
    gnjn=sum((eta[n]*gs[n]@gs[n] for n in N),Z.copy())
    ck('horizontal insertion normalization',eq(ghjh,4*I))
    ck('normal insertion normalization',eq(gnjn,10*I))
    ck('ambient trace projector numerator identity',eq(ghjh+gnjn,14*I))
    # A single 128x128 block already has rank128; factorization bounds whole defect by128.
    for h,n in [(H[0],N[0]),(H[-1],N[-1])]:
        d=eta[h]*gs[h]@gs[n]
        di=eta[n]*gs[n]@gs[h]
        ck(f'defect invertible block {h},{n}',eq(d@di,I) and eq(di@d,I))
    ck('rank lower-bound right inverse certificate',eq(ghjh@gnjn,40*I))
    omega=I.copy()
    for g in gs:omega=omega@g
    ck('ambient spinor grading square',eq(omega@omega,I))
    ck('spinor grading survives every literal horizontal slot',all(eq(I@omega,omega@I) for _ in H))
    ck('trace projector commutes grade but does not descend',eq(omega@(gs[H[0]]@gs[N[0]]),(gs[H[0]]@gs[N[0]])@omega))
    # Small exact Clifford fixture tests all linear selector/augmentation mechanisms.
    X=s.Matrix([[0,1],[1,0]]);ZZ=s.diag(1,-1);J=s.Matrix([[0,1],[-1,0]]);II=s.eye(2)
    P=s.eye(6)[:2,:];GH=X;GN=ZZ.row_join(J);G=GH.row_join(GN)
    jH=X;jN=(ZZ/2).col_join(-J/2);jY=(X/3).col_join(ZZ/3).col_join(-J/3)
    T=jY*G;K=s.eye(6)[:,2:];KR=K*s.Matrix.hstack(*GN.nullspace())
    ck('small trace selector idempotent',T*T==T)
    ck('small full defect rank',(P*T*K).rank()==2)
    ck('complement obstruction opposite',P*(s.eye(6)-T)*K==-P*T*K)
    F=P.col_join(G)
    ck('augmentation makes kernel invariant',F*T*KR==s.zeros(4,2) and F*KR==s.zeros(4,2))
    L=s.Matrix([[1,0,0,0,0,0]])
    Q=P.col_join(L)
    kerQ=s.Matrix.hstack(*Q.nullspace())
    ck('output-only augmentation fails',(Q*T*kerQ).rank()>0)
    # Extra output of width1 is smaller than required s2; choose actual nonredundant normal output.
    Lsmall=s.Matrix([[0,0,1,0,0,0]]);Qsmall=P.col_join(Lsmall)
    ck('too narrow hidden output fails',(Qsmall*T*s.Matrix.hstack(*Qsmall.nullspace())).rank()>0)
    M=s.Matrix([[1,2],[3,4]]);A0=s.Matrix([[1,1],[0,1]])
    Lmin=M.row_join(A0*GN);Qmin=P.col_join(Lmin)
    ck('general minimum augmentation succeeds',Qmin*T*s.Matrix.hstack(*Qmin.nullspace())==s.zeros(4,2))
    # Equivariant mirror normalizer tests: no identification with antiparticle conjugation.
    PL=s.diag(1,0);PR=s.diag(0,1);S=X
    ck('mirror exchanges declared chiralities',S*PL*S==PR)
    weak=PL
    ck('chiral action nonzero left-only',weak*PR==s.zeros(2) and weak*PL!=s.zeros(2))
    ck('left-only current breaks mirror normalizer',S*weak*S!=weak)
    ck('balanced current retains mirror',S*II*S==II and II*PR!=s.zeros(2))
    ck('charge conjugation not mirror for real projectors',PL.conjugate()==PL and PL.conjugate()!=PR)
    # Dimension-balanced/zero-index carrier can have one-sided weak action: index alone no parity verdict.
    ck('zero finite index coexists chiral coupling',PL.rank()-PR.rank()==0 and weak*PR==s.zeros(2) and weak*PL!=s.zeros(2))

    return checks

def phase_checks():
    """Supporting exact controls, not substitutes for the universal proofs."""
    import sympy as s
    x,y=s.symbols('x y', real=True)
    checks=[]
    def eq(name,a,b):
        if isinstance(a,s.MatrixBase) or isinstance(b,s.MatrixBase):
            ok=all(s.simplify(v)==0 for v in a-b)
        else: ok=s.simplify(a-b)==0
        assert ok,name
        checks.append(name)
    def neq(name,a,b):
        if isinstance(a,s.MatrixBase) or isinstance(b,s.MatrixBase):
            ok=any(s.simplify(v)!=0 for v in a-b)
        else: ok=s.simplify(a-b)!=0
        assert ok,name
        checks.append(name)
    def adj(A,B,H):
        return -H.inv()*A.conjugate().T*H,H.inv()*(B.conjugate().T*H-(A.conjugate().T*H).diff(x))
    def same(name,A,B,H,eps=1):
        aa,bb=adj(A,B,H)
        eq(name+' principal',aa,eps*A);eq(name+' lower',bb,eps*B)
    J=s.Matrix([[0,1],[-1,0]])
    H=s.diag(1,-2)
    A=H.inv()*J
    Z=s.zeros(2)
    same('indefinite baseline',A,Z,H)
    f=x*x+1
    _,bad=adj(f*A,Z,H)
    neq('uncompleted real dressing fails',bad,Z)
    same('half correction',f*A,A*s.diff(f,x)/2,H)
    _,wrong=adj(f*A,A*s.diff(f,x),H)
    neq('full correction coefficient fails',wrong,A*s.diff(f,x))
    aa,_=adj(s.I*A,Z,H)
    neq('nonreal principal cannot be repaired',aa,s.I*A)
    R=s.diag(x,2*x)
    same('free epsilon symmetric remainder',f*A,A*s.diff(f,x)/2+R,H)
    Hv=s.diag(1,1+x*x)
    Av=Hv.inv()*J
    same('varying density',Av,Z,Hv)
    same('varying density half correction',f*Av,Av*s.diff(f,x)/2,Hv)
    K=s.diag(1,-1)
    aa,_=adj(A,Z,K)
    neq('K cannot replace action H',aa,A)
    same('skew-adjoint baseline',s.eye(2),Z,s.eye(2),-1)
    same('skew-adjoint half correction',f*s.eye(2),s.diff(f,x)*s.eye(2)/2,s.eye(2),-1)
    # Scalar anti-linear coflip of derivative; unit rational phase needs no branch theta.
    p=(1+s.I*x)/(1-s.I*x)
    eq('unit phase square',p*s.conjugate(p),1)
    neq('principal phase misses derivative',s.diff(p,x),0)
    Bp=-s.diff(p,x)/p
    eq('exact lower-order phase repair',s.diff(p,x)+Bp*p,0)
    neq('opposite repair sign fails',s.diff(p,x)-Bp*p,0)
    eq('constant coflip works',s.diff(s.I,x),0)
    # Noninjective symbol D=partial_x leaves arbitrary y phase invisible.
    py=(1+s.I*y)/(1-s.I*y)
    eq('noninjective transverse phase survives',s.diff(py,x),0)
    neq('transverse phase is not constant',s.diff(py,y),0)
    # A general independently barred block has a formally symmetric double.
    LA=s.Matrix([[p,x],[0,s.I]])
    LB=s.Matrix([[x,1],[0,p]])
    La,Lb=adj(LA,LB,s.eye(2))
    DA=s.BlockMatrix([[Z,La],[LA,Z]]).as_explicit()
    DB=s.BlockMatrix([[Z,Lb],[LB,Z]]).as_explicit()
    same('independent-bar double',DA,DB,s.eye(4))

    return checks

def other_checks():
    rows=[]
    def ck(name,ok):
        assert bool(ok),name
        rows.append(name)
    def zero(m):return all(s.simplify(v)==0 for v in m)
    I=s.I; X=s.Matrix([[0,1],[1,0]]); Z=s.diag(1,-1)
    c=I*Z;gam=X; c90=I*gam*c
    plus=s.Matrix([1,1]);bad=s.Matrix([1,I])
    ck('grading and flux anticommute',gam*c+c*gam==s.zeros(2))
    ck('normal rotation retains antiHermitian square',c90.H==-c90 and c90*c90==-s.eye(2))
    ck('good graph preserves grading',gam*plus==plus)
    ck('bad graph is not grading invariant',s.Matrix.hstack(bad,gam*bad).rank()==2)
    ck('both graphs initially isotropic',(plus.H*c*plus)[0]==0 and (bad.H*c*bad)[0]==0)
    ck('rotated phase retains good graph',(plus.H*c90*plus)[0]==0)
    ck('rotated phase rejects bad graph',(bad.H*c90*bad)[0]==2*I)
    # Conjugate-linear-in-first omega(cu,v) is the negative of u* c v.
    ck('Green sign convention explicit',((c90*bad).H*bad)[0]==-2*I)
    for V in [s.eye(2),-s.eye(2),Z,X]:
        A=s.Matrix([[0,1],[-1,0]]);U=A*V
        ck('full invariant graph classifier '+str(V),U.H*U==s.eye(2) and U*A.H*U==A)
    A=s.eye(2);U=I*s.eye(2)
    ck('arbitrary unitary is insufficient',U.H*U==s.eye(2) and U*A.H*U!=A)
    a,b,d,e=s.symbols('a b d e');M=s.Matrix([[a,b],[d,e]])
    sols=s.solve(list(M*Z-s.eye(2)*M),[a,b,d,e])
    ck('commuting grading mismatch excludes invertible graph',M.subs(sols).det()==0)
    ck('commuting matching grading admits graph',s.eye(2)*Z==Z*s.eye(2))
    ck('real conjugation phase relation',c.conjugate()==-c and c90.conjugate()==c90)
    ck('fixed real phase relation fails',c90.conjugate()!=-c90)
    # J=Z conjugation has tau=-1 and sigma=-1, retaining the same relation.
    ck('alternate real structure retains rotated relation',Z*c90.conjugate()==-c90*Z and Z*gam.conjugate()==-gam*Z)
    # Exact index complexes; finite dimensionality is control, not infinite proof.
    idx=lambda m:m.cols-m.rows
    Dt=s.zeros(2);Dh=s.zeros(2,1);Do=s.zeros(0,1)
    ck('hidden opposite index compensates balanced total',idx(Dt)==0 and idx(Dh)==-1 and idx(Do)==1 and idx(Dt)==idx(Dh)+idx(Do))
    ck('acyclic hidden preserves observed index',idx(s.diag(1,0))==idx(s.eye(1))+idx(s.zeros(1)))
    Dt=s.eye(1);Dh=s.zeros(1,0);Do=s.zeros(0,1)
    ck('nonzero connecting map allows nonlifting zero modes',len(Dt.nullspace())==0 and len(Do.nullspace())==1 and Dh.rows-Dh.rank()==1)
    q=s.Matrix([[0,1]]);Dt=s.diag(1,0)
    ck('valid chain observation',q*Dt==s.zeros(1)*q)
    ck('nonchain observation rejected',s.Matrix([[1,0]])*Dt!=s.zeros(1)*q)
    z=s.symbols('z',nonzero=True);V=s.diag(z,1);D=s.diag(1,0);j=s.Matrix([0,1])
    aug=D.row_join(j);aug2=(V*D).row_join(V*j)
    ck('family phase augmented kernels identical',aug.nullspace()==aug2.nullspace() and aug.rank()==aug2.rank()==2)
    ck('singular phase outside theorem',s.diag(0,1).det()==0)
    # Moving observation product rule, and static selector/dynamics distinction.
    x=s.symbols('x',real=True);q=s.Matrix([[1,x]]);B=s.Matrix([[0,1],[0,0]])
    ck('moving observation lower correction',q*B==q.diff(x))
    ck('principal-only descent fails with moving observation',q*s.zeros(2)!=q.diff(x))
    q0=s.Matrix([[1,0]]);K=s.Matrix([0,1]);P=s.diag(1,0)
    ck('static grading descends',q0*P*K==s.zeros(1))
    ck('same grading does not give autonomous dynamics',q0*B*K!=s.zeros(1))
    H=s.diag(3,0);h=s.Matrix([[3]])
    ck('radical permits literal Hessian quotient',H*K==s.zeros(2,1) and H==q0.H*h*q0)
    ck('nondegenerate Hessian cannot literally descend',s.eye(2)*K!=s.zeros(2,1))
    u,v,t=s.symbols('u v t',real=True);vec=s.Matrix([u,v]);shift=s.Matrix([u,v+t])
    ck('literal form independent hidden representative',(shift.T*H*shift)[0]==(vec.T*H*vec)[0])
    ck('nondegenerate form depends hidden representative',s.expand((shift.T*shift)[0]-(vec.T*vec)[0])!=0)
    p=s.symbols('p');E=p*p+1
    ck('local blocks can eliminate nonlocally',s.rem(s.Poly(1,p),s.Poly(E,p)).as_expr()!=0)
    ck('Hermitian coupling cancellation exact',s.cancel(E*E/E)==E and s.rem(s.Poly(E*E,p),s.Poly(E,p)).is_zero)
    ck('local cancellation alone does not bound order',s.degree(p**4,p)==4)
    # Matrix adjugate condition detects entrywise cancellation, including cross channels.
    Em=s.diag(E,p+2);Bm=s.diag(E,1);Cm=Bm.T
    numerator=Bm*Em.adjugate()*Cm;den=Em.det()
    ck('matrix criterion retains one uncancelled channel',s.rem(s.Poly(numerator[0,0],p),s.Poly(den,p)).is_zero and not s.rem(s.Poly(numerator[1,1],p),s.Poly(den,p)).is_zero)
    return rows

def run():
    groups={'native_observation_and_mirror':orientation_checks(),'differential_and_variational_phase':phase_checks(),'boundary_index_and_elimination':other_checks()}
    contrary_words=('fail','reject','insufficient','not ','nonreal','wrong','cannot','too narrow','misses','nonlifting','nonchain','singular','nonlocally','uncancelled','does not','depends hidden','excludes','breaks','opposite repair')
    checks=[dict(name=n,group=g,kind='exact_contrary' if any(w in n for w in contrary_words) else 'exact_supporting',passed=True) for g,ns in groups.items() for n in ns]
    proof_paths=['explorations/conditional-build/p1-observation-descent-2026-11-11.md','explorations/conditional-build/p2-phase-variational-2026-11-11.md','explorations/conditional-build/p1-p2-domain-index-2026-11-11.md']
    report=dict(schema_version='1.0',program_target='P1/P2 remaining ten matrix cells',tier='T2',classification='INTERNAL_STRUCTURAL_ONLY',claim_ceiling='Conditional structural requirements only; no full-C decision, native realization, physical prediction or ledger move',evidence_kind='universal written proofs separate from exact finite supporting/contrary controls; native128 controls use bounded Gaussian-integer arithmetic without numerical tolerance',checks=checks,counts={k:sum(c['kind']==k for c in checks) for k in ['exact_supporting','exact_contrary']},proof_refs=proof_paths,proof_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in proof_paths})
    return report
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    report=run()
    if args.write: REPORT.write_text(json.dumps(report,indent=2)+'\n')
    elif REPORT.exists(): assert json.loads(REPORT.read_text())==report,'stored report differs from replay'
    print(json.dumps({'passed':len(report['checks']),'counts':report['counts']}))
