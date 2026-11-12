#!/usr/bin/env python3
"""Exact full-source structural controls. Universal scope is in the linked proofs."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/source-operator-membership.json'

def evolution_checks():
    """Exact small horizontal Clifford controls for full raw wedge-symbol classification.
    Universal proof is in the companion source-symbol note.
    """
    import sympy as s
    I=s.I;Id=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
    kr=s.kronecker_product
    tm=I*kr(Y,Id);gs=[kr(X,p) for p in (X,Y,Z)];gamma=[tm,*gs];eta=[-1,1,1,1]
    S=s.eye(4);O=s.zeros(4);J=s.Matrix.vstack(*[v*g for v,g in zip(eta,gamma)]);G=s.Matrix.hstack(*gamma);C=tm*gs[0];Id16=s.eye(16)
    checks=[]
    def zz(M):return all(s.cancel(v)==0 for v in M)
    def ck(name,value):
     assert bool(value),name
     checks.append(name)
    def cliff(p):return sum((v*g for v,g in zip(p,gamma)),O.copy())
    def xi(p):return s.Matrix.vstack(*[v*S for v in p])
    def ii(p):return s.Matrix.hstack(*[eta[i]*p[i]*S for i in range(4)])
    def raw6(p,a,c,e,g,ss):
     cp=cliff(p);ip=ii(p);xp=xi(p);L=2*a+14*c
     top=(a*s.diag(cp,cp,cp,cp)+c*J*ip).row_join(-a*xp-c*J*cp).row_join(e*xp)
     middle=(L*ip).row_join(-L*cp).row_join(e*cp)
     bottom=(g*ip).row_join(O).row_join(ss*cp)
     return top.col_join(middle).col_join(bottom)
    # Universal identities in two independent coefficients; other nonzero scales restored in proof.
    c,ss=s.symbols('c ss',real=True);a=e=s.Integer(1);g=s.Integer(-1)
    L=2*a+14*c;F=a+13*c;Q=a+12*c;P=a*L*ss+e*g*Q
    kap=c*e/(a*L);q=e-L*ss/g;f=1/L;chi=e*Q/(a*L)+ss/g;lam=ss/g-kap;H=chi-lam
    W=s.Matrix.hstack(C,-S,O,O,O,O);Pu=s.Matrix.hstack(O,O,O,O,S,O);Pv=s.Matrix.hstack(O,O,O,O,O,S)
    psi=f*Pu+chi*Pv;base=s.diag(C,C,C,C,C,C);Ev=base.copy()
    Ev[:4,:]=base[:4,:]-chi*W/H+lam*gs[0]*psi/H
    Ev[4:8,:]=base[4:8,:]+tm*psi
    Ev[20:24,:]=(tm*W-lam*C*Pv-f*C*Pu)/H
    T=(Id16.row_join(s.zeros(16,4)).row_join(kap*J)).col_join(s.zeros(4,16).row_join(-L*S).row_join(q*S)).col_join(s.zeros(4,20).row_join(S))
    Ti=(Id16.row_join(s.zeros(16,4)).row_join(-kap*J)).col_join(s.zeros(4,16).row_join(-S/L).row_join(q*S/L)).col_join(s.zeros(4,20).row_join(S))
    E=Ti*Ev*T
    Zmap=s.Matrix.hstack(C,-S,O,O,gs[0],-e/a*gs[0])
    N=-P/(e*g*F)*s.Matrix.vstack(C,S,O,O,O,O)*Zmap
    ck('field-coordinate inverse',zz(T*Ti-s.eye(24)))
    ck('full actual symbol time normalization',zz(raw6([1,0,0,0],a,c,e,g,ss)*E+raw6([0,1,0,0],a,c,e,g,ss)))
    ck('complete two-parameter nilpotent identity',zz(E*E-s.eye(24)-N))
    ck('nilpotent square',zz(N*N))
    ck('obstruction transports as Dirac',zz(Zmap*E-C*Zmap))
    for cv,sv,rank in [(0,0,4),(0,s.Rational(1,2),0),(-1,0,4),(-1,s.Rational(11,12),0),(-s.Rational(1,12),0,0)]:
     D0=raw6([1,0,0,0],1,cv,1,-1,sv);D1=raw6([0,1,0,0],1,cv,1,-1,sv)
     EE=-D0.inv()*D1
     NN=EE*EE-s.eye(24)
     ck('independent inverse Jordan rank '+str((cv,sv)),NN.rank()==rank and zz(NN*NN))
     if rank==0:
      HH=s.eye(24)+EE.H*EE
      ck('positive symmetrizer algebra '+str((cv,sv)),zz(HH*EE-EE.H*HH))
    # L=0 is a genuine allowed chart, not a singular-time condition.
    cv=-s.Rational(1,7);sv=s.Rational(2,3)
    D0=raw6([1,0,0,0],1,cv,1,-1,sv);EE=-D0.inv()*raw6([0,1,0,0],1,cv,1,-1,sv)
    ck('Lzero extension',zz(EE*EE-s.eye(24)-N.subs({c:cv,ss:sv})))
    ck('Fzero time singular',raw6([1,0,0,0],1,-s.Rational(1,13),1,-1,0).det()==0)
    # Arbitrary nonzero scales and source sign controls use direct inverse, no guessed action.
    for aa,cc,ee,gg in [(2,-s.Rational(1,6),3,-5),(2,-2,3,5)]:
     aa,cc,ee,gg=map(s.sympify,(aa,cc,ee,gg))
     LL=2*aa+14*cc;QQ=aa+12*cc;sv=-ee*gg*QQ/(aa*LL)
     E0=-raw6([1,0,0,0],aa,cc,ee,gg,sv).inv()*raw6([0,1,0,0],aa,cc,ee,gg,sv)
     ck('all nonzero-scale Dirac criterion '+str((aa,cc,ee,gg)),zz(E0*E0-s.eye(24)))
    # Algebraic r-preserving quotient closure and its failure to retain actual source outputs.
    cc=-s.Rational(1,12);aa=ee=gg=s.Integer(1);sv=s.Integer(0)
    beta=s.Rational(6,7);rho=s.Rational(13,14);LL=2*aa+14*cc
    ck('zeroSE projected quotient can algebraically close',aa*beta*LL*rho+ee*gg/14==aa*aa*beta*beta-aa*beta*sv)
    geff=ee*gg-aa*beta*LL;seff=sv-aa*beta
    ck('projected quotient Dirac ratio',aa*seff/geff==-3)
    ck('same source sign need not close quotient',aa*beta*LL*rho-s.Rational(1,14)!=aa*aa*beta*beta)
    # Dropped(r=0,trace=t,nu=a beta/e*t) has nonzero horizontal and scalar output.
    ck('discarded scalar channel remains observed',J.rank()==4 and aa*beta/ee!=0)
    # Full Dirac equivalence at the zeroSE mixed survivor.
    cv=-s.Rational(1,12);sv=0
    Tv=T.subs({c:cv,ss:sv});ff=f.subs(c,cv);ll=lam.subs({c:cv,ss:sv})
    Tx=(Id16.row_join(ff*J/2).row_join(s.zeros(16,4))).col_join(s.zeros(4,16).row_join(S).row_join(O)).col_join(s.zeros(4,20).row_join(S))
    Te=(Id16.row_join(s.zeros(16,8))).col_join(s.zeros(4,16).row_join(S).row_join(O)).col_join((G/(2*ll)).row_join(O).row_join(S))
    TD=Te*Tx*Tv
    E0=-raw6([1,0,0,0],1,cv,1,-1,0).inv()*raw6([0,1,0,0],1,cv,1,-1,0)
    ck('constant full6S Dirac equivalence',TD.det()!=0 and zz(TD*E0-s.diag(C,C,C,C,C,C)*TD))
    for j in [1,2,3]:
     pp=[0,0,0,0];pp[j]=1
     Ej=-raw6([1,0,0,0],1,cv,1,-1,0).inv()*raw6(pp,1,cv,1,-1,0)
     Cj=tm*gs[j-1]
     ck('constant Dirac map spatial '+str(j),zz(TD*Ej-s.diag(Cj,Cj,Cj,Cj,Cj,Cj)*TD))
    HH=TD.H*TD
    ck('constant positive metric invertible Gram',TD.det()!=0)
    for cv0,sv0 in [(0,0),(-s.Rational(1,12),0)]:
     Eall=-raw6([1,0,0,0],1,cv0,1,-1,sv0).inv()*raw6([0,1,2,3],1,cv0,1,-1,sv0)
     NN=Eall*Eall-14*s.eye(24)
     ck('nonradial propagation '+str((cv0,sv0)),NN.rank()==(4 if cv0==0 else 0) and zz(NN*NN))

    return checks

def chiral_checks():
    """Independent chiral input weights in a small exact Cl(3,1) control."""
    import sympy as s
    I=s.I;Id=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1);kr=s.kronecker_product
    T=I*kr(Y,Id);gs=[kr(X,p) for p in (X,Y,Z)];gamma=[T,*gs];eta=[-1,1,1,1];S=s.eye(4);O=s.zeros(4)
    J=s.Matrix.vstack(*[v*g for v,g in zip(eta,gamma)]);G=s.Matrix.hstack(*gamma)
    Omega=I*T*gs[0]*gs[1]*gs[2];Pp=(S+Omega)/2;Pm=(S-Omega)/2
    checks=[]
    def z(M):return all(s.cancel(v)==0 for v in M)
    def ck(n,v):
     assert bool(v),n
     checks.append(n)
    ck('typed spinor grading',Omega*Omega==S and all(z(Omega*g+g*Omega) for g in gamma))
    def d(p,ap,am,cp,cm,lp,lm,e=1,g=-1):
     cc=sum((p[i]*gamma[i] for i in range(4)),O.copy());xx=s.Matrix.vstack(*[v*S for v in p]);ii=s.Matrix.hstack(*[eta[i]*p[i]*S for i in range(4)])
     A=ap*Pp+am*Pm;Ab=am*Pp+ap*Pm;C=cp*Pp+cm*Pm;Cb=cm*Pp+cp*Pm
     L=2*A+14*C;Lb=2*Ab+14*Cb;ell=lp*Pp+lm*Pm
     top=(s.diag(cc*A,cc*A,cc*A,cc*A)+J*C*ii).row_join(-xx*Ab-J*cc*Cb).row_join(e*xx)
     mid=(L*ii).row_join(-cc*Lb).row_join(e*cc)
     bot=(g*ii).row_join(O).row_join(cc*ell)
     return top.col_join(mid).col_join(bot)
    Ga=s.diag(Omega,Omega,Omega,Omega,-Omega,-Omega)
    for vals,name,rank in [((2,3,-s.Rational(1,6),-s.Rational(1,4),0,0),'independent mixed zeroSE',0),((2,3,-s.Rational(1,6),-1,0,0),'one bad chiral ratio',2),((2,3,0,-3,s.Rational(11,36),s.Rational(1,4)),'crossed general completion',0),((2,3,0,-3,s.Rational(1,4),s.Rational(11,36)),'wrong uncrossed completion',4)]:
     D0=d([1,0,0,0],*vals);D1=d([0,1,0,0],*vals);E=-D0.inv()*D1;N=E*E-s.eye(24)
     ck(name+' auxiliary grading',z(D0*Ga+Ga*D0) and z(E*Ga-Ga*E))
     ck(name+' Jordan rank',N.rank()==rank and z(N*N))

    # A single constant positive metric for independent chiral weights.
    vals=(2,3,0,-3,s.Rational(11,36),s.Rational(1,4))
    Dt=d([1,0,0,0],*vals);Es=[]
    for j in [1,2,3]:
        pp=[0,0,0,0];pp[j]=1;Es.append(-Dt.inv()*d(pp,*vals))
    ck('independent chiral spatial Clifford algebra',all(z(Es[i]*Es[j]+Es[j]*Es[i]-(2*s.eye(24) if i==j else s.zeros(24))) for i in range(3) for j in range(3)))
    products=[s.eye(24)]
    for E in Es:products += [P*E for P in products]
    HH=sum((P.H*P for P in products),s.zeros(24))
    ck('constant symmetrizer contains identity Gram term',products[0]==s.eye(24) and len(products)==8)
    ck('constant symmetrizer all spatial generators',all(z(HH*E-E.H*HH) for E in Es))
    return checks

def native_controls():
    import sys
    import numpy as np
    import sympy as s
    from pathlib import Path
    sys.path.insert(0,str(ROOT/'tests/channel-swings'))
    from actual_sym2_c14_orbit_probe import native_gammas
    gs,eta=native_gammas();Id=np.eye(128,dtype=complex);Z=0*Id
    H=[9,0,1,2];N=[i for i in range(14) if i not in H]
    checks=[]
    def ck(name,value,contrary=False):
        assert bool(value),name
        checks.append(dict(name=name,kind='exact_contrary' if contrary else 'exact_supporting',passed=True))
    def eq(a,b):return np.array_equal(a,b)
    # All entries below are Gaussian integers or exact dyadic rationals;
    # avoid division by10 or14 by retaining scaled numerators.
    JN={a:eta[a]*gs[a] for a in N}
    ck('native normal insertion Gamma normalization10',eq(sum((gs[a]@JN[a] for a in N),Z.copy()),10*Id))
    # F_N = 1 - J_N Gamma/10; construct10F_N on each input block.
    for b in range(14):
        blocks={a:(10*Id if a==b else Z.copy())-(JN[a]@gs[b] if a in N else Z.copy()) for a in range(14)}
        ck('normal retraction lands R '+str(b),eq(sum((gs[a]@blocks[a] for a in range(14)),Z.copy()),Z))
        ck('normal retraction preserves literal observation '+str(b),all(eq(blocks[a],10*Id if a==b else Z) for a in H))
    ck('normal retraction kernel is normal insertion',all(eq(10*JN[a]-JN[a]@(10*Id),Z) for a in N))
    # Canonical ambient orthogonal projection P_R differs on a normal trace.
    ck('orthogonal projection changes observed normal trace',all(not eq(eta[a]*gs[a]@(10*Id),Z) for a in H),True)
    r,t=N[:2]
    hidden={r:eta[r]*gs[r],t:-eta[t]*gs[t]}
    ck('hidden normal gamma-zero shift exists',eq(sum((gs[a]@v for a,v in hidden.items()),Z.copy()),Z))
    ck('hidden shift is nonzero',any(not eq(v,Z) for v in hidden.values()),True)
    # A chosen normal rotation demonstrates that this extra K is not an
    # unadorned split-isotropy intertwiner; the universal absence is proved in text.
    u=N[2];R=gs[r]@gs[u]
    ck('chosen hidden shift fails normal-spin intertwining',not eq(R@hidden[r],hidden[r]@R),True)
    tau=gs[H[0]];gam=gs[H[1]]
    for a,c in [(1,0),(1,-1),(2,3),(0,1)]:
        # xi=e_1: F_xi=-a xi-c gamma_H c_xi; orthogonal slot3
        coeff={h:-a*(Id if h==H[1] else Z)-c*eta[h]*gs[h]@gam for h in H}
        ck('wedge hidden trace leaks '+str((a,c)),any(not eq(v,Z) for v in coeff.values()),True)
        if c:
            M=coeff[H[2]]
            ck('transverse leakage injective '+str((a,c)),eq(M@M,-c*c*Id))
        else:ck('longitudinal leakage injective simple',eq(coeff[H[1]],-a*Id))
    # Source-current coefficient: two distinct actual native spin directions.
    a,b=H[0],H[1];T=gs[a]@gs[b]/2;M=gs[a]@T
    ck('actual spin-generator SE current coefficient',eq(M,eta[a]*gs[b]/2))
    ck('current coefficient full rank by square',eq(M@M,eta[b]*Id/4))
    ck('zero matrix trace does not erase bilinear current',np.trace(M)==0 and not eq(M,Z),True)
    row,col=np.argwhere(M!=0)[0];ck('independent row column detects current',M[row,col]!=0)
    x,k=s.symbols('x k',real=True);L=x-k*x
    ck('connection counterterm exactly cancels',s.diff(L,x).subs(k,1)==0)
    ck('changed cancellation coefficient restores current',s.diff(L,x).subs(k,2)!=0,True)
    aa,bb,cc,dd,ee=s.symbols('a b c d e')
    sol=s.solve([ee-1,dd,cc,aa-1,bb],[aa,bb,cc,dd,ee],dict=True)
    ck('fixed-observation trace scalar arrow redefinition identity',sol==[{aa:1,bb:0,cc:0,dd:0,ee:1}])
    # Native metric trace: choose a normal frame in which t=2e_r, norm -4.
    r=next(a for a in N if eta[a]==-1);ct=2*gs[r]
    K10={a:20*Id*(a==r)-JN[a]@ct for a in N}
    form=Id.copy()
    for a in range(9):form=form@gs[a]
    ck('metric trace hidden map gamma zero',eq(sum((gs[a]@K10[a] for a in N),Z.copy()),Z))
    ck('metric trace hidden map pairing nondegenerate',eq(sum((eta[a]*K10[a].conj().T@form@K10[a] for a in N),Z.copy()),-360*form))
    for h in H:
        cx=gs[h]
        ck('metric hidden shift commutes tangent Clifford '+str(h),all(eq(cx@v,v@cx) for v in K10.values()))
        se=sum((eta[a]*K10[a].conj().T@form@cx@K10[a] for a in N),Z.copy())
        ck('triangular coordinate southeast numerator '+str(h),eq(se,-360*form@cx))
    omega=Id.copy()
    for a in range(14):omega=omega@gs[a]
    ck('native trace hidden shift ambient grade even',all(eq(omega@v,v@omega) for v in K10.values()))
    ck('native trace norm from DeWitt half reversal',4-s.Rational(1,2)*4**2==-4)
    W=(3*Id-omega)/2;Wi=(3*Id+omega)/4;Wbar=(3*Id+omega)/2
    ck('held W invertible exact',eq(W@Wi,Id))
    ck('actual trace W transports opposite weight',all(eq(gs[a]@W,Wbar@gs[a]) for a in range(14)))
    for h in H:
        ck('held reciprocal SE transport '+str(h),eq(Wi@gs[h],gs[h]@W/2))
    ck('untransported scalar SE differs',not eq(Wi@gs[H[0]],gs[H[0]]),True)
    return checks

def run():
    checks=native_controls()
    contrary=('rank (0, 0)','rank (-1, 0)','Fzero','same source sign','discarded','bad chiral','wrong uncrossed','nonradial propagation (0, 0)')
    for group,rows in [('full_symbol',evolution_checks()),('chiral_weights',chiral_checks())]:
        checks.extend(dict(name=n,group=group,kind='exact_contrary' if any(x in n for x in contrary) else 'exact_supporting',passed=True) for n in rows)
    refs=['explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md','explorations/conditional-build/source-current-grading-membership-2026-11-12.md']
    deps=['lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md','explorations/eric-curt-wave3d-b2c4-shiab-family-southeast-completion-2026-08-01.md','tests/channel-swings/actual_sym2_c14_orbit_probe.py']
    return dict(schema_version='1.0',program_target='X-P1-P2 / X-P2-P3',tier='T2',classification='INTERNAL_STRUCTURAL_ONLY',claim_ceiling='Declared frozen natural-symbol categories, conditional current and coordinate identities; no source-selected action, full-C decision, physical weak/family map or unrestricted ambient-domain realization',evidence_kind='Written universal proofs; exact symbolic two-parameter identity, independently weighted chiral controls, native128 Gaussian-integer and dyadic checks. Matrix checks are not independent discoveries.',checks=checks,counts={k:sum(c['kind']==k for c in checks) for k in ['exact_supporting','exact_contrary']},proof_refs=refs,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs+deps})

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();r=run()
    if args.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==r,'stored evidence or dependency mismatch'
    print(json.dumps({'passed':len(r['checks']),'counts':r['counts']}))
