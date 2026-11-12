#!/usr/bin/env python3
"""Native symbol controls and exact coupled-parameter identities; see linked proofs."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/native-rs-joint-compatibility.json'

def evolution_checks():
    """Small exact Clifford control of canonical n14 RS observation evolution.
    No source action or infinite-dimensional assertion follows from this finite probe.
    """
    import sympy as s
    I=s.I;Id=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
    kron=s.kronecker_product
    tau=I*kron(Y,Id);gs=[kron(X,P) for P in (X,Y,Z)]
    g=[tau,*gs];eta=[-1,1,1,1];S=s.eye(4);a=s.Rational(1,7);r=a/(1-a)
    checks=[]
    def ck(n,v):
     assert bool(v),n
     checks.append(n)
    def z(M):return M==s.zeros(*M.shape)
    ck('Lorentz Clifford relations',all(g[i]*g[j]+g[j]*g[i]==(2*eta[i]*S if i==j else s.zeros(4)) for i in range(4) for j in range(4)))
    J=s.Matrix.vstack(*[e*c for e,c in zip(eta,g)])
    Gamma=s.Matrix.hstack(*g)
    ck('horizontal gamma normalization',Gamma*J==4*S)
    def d(coeff):
     c=sum((v*x for v,x in zip(coeff,g)),s.zeros(4))
     contraction=s.Matrix.hstack(*[eta[i]*coeff[i]*S for i in range(4)])
     return s.diag(c,c,c,c)-a*J*contraction
    Dt=d([1,0,0,0]);Dx=d([0,1,0,0]);E=-Dt.inv()*Dx
    C=tau*gs[0]
    W=s.Matrix.hstack(C,-S,s.zeros(4),s.zeros(4))
    formula=s.diag(C,C,C,C)+r*s.Matrix.vstack(S,C,tau*gs[1],tau*gs[2])*W
    ck('actual coefficient inversion matches formula',E==formula)
    N=E*E-s.eye(16)
    ck('full nilpotent formula',N==2*r*s.Matrix.vstack(C,S,s.zeros(4),s.zeros(4))*W)
    ck('rank spinor nilpotent',N.rank()==4 and z(N*N))
    ck('maximal semisimple kernel',len(N.nullspace())==12)
    ck('constraint propagates',W*E==C*W)
    K=s.Matrix.hstack(*W.nullspace())
    ck('restricted evolution componentwise Clifford',E*K==s.diag(C,C,C,C)*K)
    ck('positive principal Clifford Hermitian',C.H==C)
    ck('full evolution is not Hermitian',E.H!=E)
    ck('horizontal trace onto constrained spinor',(Gamma*K).rank()==4)
    jT=s.Matrix.vstack(s.zeros(4),s.zeros(4),gs[1]/2,gs[2]/2)
    ck('transverse trace retraction',Gamma*jT==S and z(W*jT))
    ck('transverse trace dynamics',E*jT==jT*C)
    ck('gamma trace autonomous on constraint',Gamma*E*K==C*Gamma*K)
    ck('constrained gamma kernel size',16-W.col_join(Gamma).rank()==8)
    ck('canonical horizontal trace insertion NOT constrained',not z(W*J))
    # All principal directions still need a separate coupled/lower-order preservation test.
    ck('unrestricted gamma kernel not invariant',not z(Gamma*Dx*s.Matrix.hstack(*Gamma.nullspace())))
    ck('literal Dirac a0 is diagonalizable contrary control',s.diag(C,C,C,C)**2==s.eye(16))
    for lam in [1,-1]:
     L=s.Matrix([[lam,-a],[a,(1-2*a)*lam]])/(1-a)
     M=L-lam*s.eye(2)
     ck('longitudinal Jordan '+str(lam),M.rank()==1 and z(M*M))
     t=s.symbols('t',real=True)
     exp=s.exp(I*lam*t)*(s.eye(2)+I*t*M)
     ck('exact growing propagator '+str(lam),z(s.simplify(s.diff(exp,t)-I*L*exp)))

    # General coupled scalar-arrow category, all nonzero A,e,g normalized.
    beta=s.Rational(1,14)
    def embed(coeff):return s.Matrix.vstack(*[v*S for v in coeff])
    def contraction(coeff):return s.Matrix.hstack(*[eta[i]*coeff[i]*S for i in range(4)])
    def c(coeff):return sum((v*x for v,x in zip(coeff,g)),s.zeros(4))
    def coupled(coeff,delta):
     cc=c(coeff);U=embed(coeff)-beta*J*cc
     return (d(coeff).row_join(U)).col_join(contraction(coeff).row_join(delta*cc))
    zero4=s.zeros(4);Id16=s.eye(16)
    delta=s.symbols('delta',real=True)
    kappa=beta*(1-2*delta);chi=1-2*kappa;lam=kappa-delta;den=lam+chi
    Wv=s.Matrix.hstack(C,-S,zero4,zero4,zero4)
    Pphi=s.Matrix.hstack(zero4,zero4,zero4,zero4,S)
    base=s.diag(C,C,C,C,C)
    # Evolution on v variables directly from independent coefficient equations.
    Ev=base.copy()
    Ev[:4,:]=base[:4,:]-chi*Wv/den-chi*lam*gs[0]*Pphi/den
    Ev[4:8,:]=base[4:8,:]+chi*tau*Pphi
    Ev[16:20,:]=(tau*Wv+lam*C*Pphi)/den
    T=(Id16.row_join(kappa*J)).col_join(s.zeros(4,16).row_join(S))
    Tinv=(Id16.row_join(-kappa*J)).col_join(s.zeros(4,16).row_join(S))
    Ec=Tinv*Ev*T
    Zmap=s.Matrix.hstack(C,-S,zero4,zero4,-gs[0])
    Nformula=-chi/den*s.Matrix.vstack(C,S,zero4,zero4,zero4)*Zmap
    def simpzero(M):return all(s.cancel(v)==0 for v in M)
    ck('general normalized coupled coefficient inversion',simpzero(coupled([1,0,0,0],delta)*Ec+coupled([0,1,0,0],delta)))
    ck('general coupled nilpotent formula',simpzero(Ec*Ec-s.eye(20)-Nformula))
    ck('general coupled nilpotent square',simpzero(Nformula*Nformula))
    ck('general transported obstruction',simpzero(Zmap*Ec-C*Zmap))
    for value in [0,2,s.Rational(1,2),-3]:
     Ex=Ec.subs(delta,value)
     Nx=Ex*Ex-s.eye(20)
     ck('coupled nilpotent rank '+str(value),Nx.rank()==(0 if value==-3 else 4))
     ck('coupled time coefficient invertible '+str(value),coupled([1,0,0,0],value).det()!=0)
    ck('Dirac locus all carrier semisimple',simpzero(Ec.subs(delta,-3)**2-s.eye(20)))
    ck('singular locus fails time inversion',coupled([1,0,0,0],s.Rational(13,12)).det()==0)
    # Principal syzygy at the singular coefficient, no claim of a full gauge identity.
    for coeff in [[1,0,0,0],[0,1,0,0],[1,1,0,0]]:
     syz=(-14*embed(coeff)+J*c(coeff)).col_join(12*c(coeff))
     ck('singular symbol syzygy '+str(coeff),z(coupled(coeff,s.Rational(13,12))*syz))
    # Dirac-equivalent full-Clifford coefficient control at delta=-3.
    kap=s.Rational(1,2);ll=s.Rational(7,2)
    field1=(Id16.row_join(kap*J)).col_join(s.zeros(4,16).row_join(S))
    field2=(Id16.row_join(s.zeros(16,4))).col_join((-Gamma/(2*ll)).row_join(S))
    TF=field2*field1
    ck('constant Dirac field transform invertible',TF.det()!=0)
    ck('constant Dirac field transform evolution',simpzero(TF*Ec.subs(delta,-3)-s.diag(C,C,C,C,C)*TF))
    Kc=s.Matrix.hstack(*Zmap.nullspace())
    ck('all nonDirac cases share maximal sector',Kc.cols==16 and all(z(Nformula.subs(delta,v)*Kc) for v in [0,2,s.Rational(1,2)]))
    ck('coupled sector dynamics independent parameter',simpzero((Ec-Ec.subs(delta,0))*Kc))
    return checks

def geometry_checks():
    import os
    os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
    os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
    import numpy as np
    import sympy as s
    import sys
    from pathlib import Path
    ROOT=Path(__file__).resolve().parents[2]
    sys.path.insert(0,str(ROOT/'tests/channel-swings'))
    from actual_sym2_c14_orbit_probe import native_gammas
    checks=[]
    def ck(n,b):
     assert bool(b),n
     checks.append(n)
    def eq(a,b):return np.array_equal(a,b)
    g,eta=native_gammas();I=np.eye(128,dtype=complex);Z=0*I;H=[9,0,1,2];N=[i for i in range(14) if i not in H]
    K=I.copy()
    for k in range(9):K=K@g[k]
    chi=1j*g[H[0]]@g[H[1]]@g[H[2]]@g[H[3]]
    ck('actual K95 K Hermitian involution',eq(K.conj().T,K) and eq(K@K,I))
    ck('actual gamma K-selfadjoints',all(eq(gg.conj().T@K,K@gg) for gg in g))
    ck('horizontal grading square and K skew',eq(chi@chi,I) and eq(chi.conj().T@K,-K@chi))
    # R10=10*r; no non-dyadic floating arithmetic anywhere.
    R={(a,b):(10*I if a==b else Z.copy()) if a in H else -eta[a]*g[a]@g[b] for a in range(14) for b in H}
    for b in H:
     ck('canonical lift gamma kernel '+str(b),eq(sum((g[a]@R[a,b] for a in range(14)),Z.copy()),Z))
     ck('coherent horizontal grading lift '+str(b),all(eq((1 if a in H else -1)*chi@R[a,b],R[a,b]@chi) for a in range(14)))
    ck('slotwise horizontal grading fails',not eq(sum((g[a]@chi@R[a,H[0]] for a in range(14)),Z.copy()),Z))
    G10={(a,b):10*eta[a]*K*(a==b)+g[a].conj().T@K@g[b] for a in H for b in H}
    for a in H:
     for b in H:
      gg=sum((eta[r]*R[r,a].conj().T@K@R[r,b] for r in range(14)),Z.copy())
      ck('actual induced pairing '+str((a,b)),eq(gg,10*G10[a,b]))
    # Distinct non-null and null tangent covectors; polynomial identities don't divide norms.
    for coeff in [(1,0,0,0),(0,1,0,0),(1,1,0,0),(1,2,3,0)]:
     c=sum((t*g[a] for t,a in zip(coeff,H)),Z.copy());xi=dict(zip(H,coeff))
     B7={(a,b):7*c*(a==b)-eta[a]*g[a]*eta[b]*xi[b] for a in H for b in H}
     for a in range(14):
      for b in H:
       left=7*c@R[a,b]-10*eta[a]*g[a]*eta[b]*xi[b]
       right=sum((R[a,h]@B7[h,b] for h in H),Z.copy())
       ck('exact Qr=rB '+str((coeff,a,b)),eq(left,right))
     for a in H:
      for b in H:
       left=sum((B7[h,a].conj().T@G10[h,b] for h in H),Z.copy())
       right=sum((G10[a,h]@B7[h,b] for h in H),Z.copy())
       ck('actual descended symbol pairing '+str((coeff,a,b)),eq(left,right))
     # U14=(14 xi insertion-J c), and G10 U14=140 contraction adjoint K.
     U14={a:14*xi[a]*I-eta[a]*g[a]@c for a in H}
     ck('actual projected insertion adjoint '+str(coeff),all(eq(sum((G10[a,h]@U14[h] for h in H),Z.copy()),140*eta[a]*xi[a]*K) for a in H))
    # Hidden normal vector w with ΓN w=0, finite pairing nonradical control.
    r,t=N[:2];hidden={r:eta[r]*g[r],t:-eta[t]*g[t]}
    ck('hidden gamma trace zero',eq(g[r]@hidden[r]+g[t]@hidden[t],Z))
    hiddenform=sum((eta[j]*v.conj().T@K@v for j,v in hidden.items()),Z.copy())
    ck('hidden inherited form is nonzero',not eq(hiddenform,Z))
    # Moving-section leakage from II_11^r=1, all other II zero. Mean curvature1.
    a=H[1];Lr=(-7+1)*g[a] # 7*L=-7 gamma_1 +gamma_a, because 2/m=1/7
    ck('actual moving shape leaks hidden kernel',not eq(Lr@hidden[r],Z))
    # Clifford factorization cannot identify different normal bivectors.
    ck('different normal bivector supports independent',not eq(g[H[1]]@g[N[0]],g[H[1]]@g[N[1]]))
    ck('n14 umbilic residual nonzero',s.Rational(2*4,14)-1!=0)
    ck('n8 umbilic exception retained',s.Rational(2*4,8)-1==0)
    # An adapted metric connection cancels off-diagonal splitting motion, not principal symbol.
    z=s.symbols('z',real=True);J=s.Matrix([[0,z],[-z,0]]);P=s.diag(1,0)
    ad=P*J*P+(s.eye(2)-P)*J*(s.eye(2)-P)
    ck('adapted metric connection preserves split',ad*P-P*ad==s.zeros(2) and ad.T==-ad)
    ck('uncorrected connection moves split',J*P-P*J!=s.zeros(2))
    x,y=s.symbols('x y');weights=[2*x,-2*x,2*y,-2*y,x+y,x-y,-x+y,-x-y,0,0]
    ck('metric-normal Pontryagin coefficient',s.expand(sum(w*w for w in weights)/2)==6*(x*x+y*y))
    p=s.symbols('p');ahat=1-p/24;spin=32+24*p
    trunc=lambda z:s.expand(z).coeff(p)
    obs=3*trunc(ahat*(4+p)*spin);hid=-3*trunc(ahat*(9+6*p)*spin);tot=3*trunc(ahat*(-5-5*p)*spin)
    ck('closed comparison exact index weights',(obs,hid,tot)==(368,-1188,-820))
    ck('graded index additivity with hidden sign',tot==obs+hid)
    scalar=3*trunc(ahat*spin)
    ck('trace companion scalar index68',scalar==68)
    ck('opposite scalar grade gives300 not436',obs-scalar==300 and obs+scalar==436)
    ck('wrong same-sign hidden transfer fails',tot!=obs-hid)
    # Five factors start at cohomological degree10: no degree4 term.
    t=s.symbols('t');roots=s.symbols('x1:6');diff=s.prod(2*s.sinh(t*x/2) for x in roots)
    ck('ambient spin difference has no degree4 part',s.series(diff,t,0,3).removeO()==0)
    return checks

def run():
    groups={'canonical_and_coupled_evolution':evolution_checks(),'native_pairing_geometry_grading':geometry_checks()}
    contrary=('fail','not ','nonzero','leak','wrong','independent','exception','nondegenerate','singular','contrary')
    checks=[dict(name=n,group=g,kind='exact_contrary' if any(x in n.lower() for x in contrary) else 'exact_supporting',passed=True) for g,rows in groups.items() for n in rows]
    refs=['explorations/conditional-build/native-rs-observed-compatibility-2026-11-11.md','explorations/conditional-build/native-rs-moving-section-index-2026-11-11.md']
    return dict(schema_version='1.0',program_target='X-P1-P2 / X-P2-P3',tier='T2',classification='INTERNAL_STRUCTURAL_ONLY',claim_ceiling='Declared native-symbol and connection categories only; no source-selected action, full class-C result, physical family index or positive quantum theory',evidence_kind='Universal written proofs and symbolic coupled-parameter identities; finite exact native Gaussian-integer controls use no tolerances. Individual matrix-block checks are not independent discoveries.',checks=checks,counts={k:sum(c['kind']==k for c in checks) for k in ['exact_supporting','exact_contrary']},proof_refs=refs,proof_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs})
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();r=run()
    if args.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    elif REPORT.exists():assert json.loads(REPORT.read_text())==r,'report/proof replay mismatch'
    print(json.dumps({'passed':len(r['checks']),'counts':r['counts']}))
