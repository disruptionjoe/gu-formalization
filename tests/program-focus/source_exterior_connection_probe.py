#!/usr/bin/env python3
"""Exact structural controls; general proofs and ceilings are in the linked notes."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/source-exterior-connection.json'

def lower_controls():
    import sympy as s


    def run():
        I=s.I; E=s.eye(2)
        x=s.Matrix([[0,1],[1,0]])
        y=s.Matrix([[0,-I],[I,0]])
        z=s.diag(1,-1)
        gamma=[]
        for pos in range(3):
            for pauli in (x,y):
                factors=[z]*pos+[pauli]+[E]*(2-pos)
                gamma.append(s.kronecker_product(*factors))
        eye=s.eye(8); zero=s.zeros(8); h=2; m=4; n=h+m
        def total(xs): return sum(xs,zero)
        for i in range(n):
            assert gamma[i].H==gamma[i]
            for j in range(n):
                assert gamma[i]*gamma[j]+gamma[j]*gamma[i]==(2*eye if i==j else zero)
        # II_00=n0, all other components zero; H=n0.
        ch=gamma[h]
        hidden=[zero]*h+[(eye if r==0 else zero)-gamma[h+r]*ch/m for r in range(m)]
        assert total(gamma[i]*hidden[i] for i in range(n))==zero
        zh=hidden[h]
        assert zh==(1-s.Rational(1,m))*eye
        G=[gamma[0]*zh,zero]
        def response(K):
            S=total(K[r]*hidden[r] for r in range(h,n))
            R=[total(gamma[r]*K[i]*hidden[r] for r in range(h,n)) for i in range(n)]
            W=total(gamma[i]*R[i] for i in range(n))
            return S,R,W
        tangent=[gamma[0]*ch/2,zero]
        normal=[gamma[r]*ch-(eye if r==h else zero) for r in range(h,n)]
        K=tangent+normal
        assert all(k.H==-k for k in K)
        S,R,W=response(K)
        assert S==zh
        assert all(R[a]==-G[a] for a in range(h))
        assert W==-(2*m-3)*zh
        assert W.det()!=0
        # A nontrivial full-parent homogeneous remainder has no scalar/W effect.
        F=I*eye+gamma[0]
        homogeneous=[zero]*h+[F*gamma[r] for r in range(h,n)]
        assert all(k.H==-k for k in homogeneous)
        Ss,Rs,Ws=response(homogeneous)
        assert Ss==zero and Ws==zero
        # Complexified paired-arrow escape: explicitly not skew / not fixed-adjoint.
        escape=tangent+[-gamma[r]*ch/(2*(m-2))
                        +s.Rational(m-1,m-2)*(eye if r==h else zero)
                        for r in range(h,n)]
        Se,Re,We=response(escape)
        assert Se==zh and We==zero
        assert all(Re[a]==-G[a] for a in range(h))
        assert escape[h].H==escape[h] and escape[h]!=zero
        # Trace formula of the natural wedge symbol, on arbitrary matrix-valued input.
        a=s.Integer(1); c=-s.Rational(1,12); L=2*a+n*c
        def symbol(mu,v):
            tr=total(gamma[k]*v[k] for k in range(n))
            return [a*(gamma[mu]*v[k]-(tr if k==mu else zero))
                    +c*gamma[k]*(v[mu]-gamma[mu]*tr) for k in range(n)]
        full=total(gamma[k]*total(symbol(i,[K[i]*q for q in hidden])[k]
                                for i in range(n)) for k in range(n))
        assert full==L*(S-W)
        # Mean-zero nonzero-II counterexample: II00=n0, II11=-n0.
        meanzero=[gamma[0]*ch/2,-gamma[1]*ch/2]+[zero]*m
        Sm,Rm,Wm=response(meanzero)
        assert Sm==zero and Wm==zero
        assert Rm[0]==-gamma[0]*zh and Rm[1]==gamma[1]*zh
        return {"scalar_spin_success":True,"unitary_joint_obstruction":True,
                "homogeneous_parent_remainder":True,"nonunitary_paired_escape":True,
                "complete_trace_identity":True,"mean_zero_spin_survivor":True}


    assert all(run().values())
    return True

def exterior_controls_suite():
    from fractions import Fraction as Q


    def grade_factor_support():
        # Multiplication by one nonnull Clifford basis vector permutes blade masks.
        # A factor M whose products M*c(n) all have grade2 can have only these masks.
        n, h = 14, 4
        admissible = [mask for mask in range(1 << n)
                      if all((mask ^ (1 << j)).bit_count() == 2 for j in range(h, n))]
        assert admissible == [1 << i for i in range(h)]
        # Low-normal-dimension contrary: three normal generators admit their volume.
        admissible3 = [mask for mask in range(1 << 5)
                       if all((mask ^ (1 << j)).bit_count() == 2 for j in range(2, 5))]
        assert (sum(1 << j for j in range(2, 5))) in admissible3


    def exterior_controls():
        # Reduced h2+n4 metric Clifford algebra: exact torsion/adjoint tradeoff.
        # Its gamma-kernel witness is not the universal128-rank claim.
        n, h = 6, 2
        r = n-h
        sig = [-1, 1, 1, 1, 1, -1]
        def add(*xs):
            out = {}
            for x in xs:
                for k, v in x.items(): out[k] = out.get(k,Q(0))+v
            return {k:v for k,v in out.items() if v}
        def scale(v, x): return {k:v*w for k,w in x.items() if v*w}
        def mul(x,y):
            out={}
            for a,va in x.items():
                for b,vb in y.items():
                    swaps=sum((b & ((1<<i)-1)).bit_count() for i in range(n) if a>>i&1)
                    s=Q((-1)**swaps)
                    for i in range(n):
                        if a&b&(1<<i): s*=sig[i]
                    k=a^b;out[k]=out.get(k,Q(0))+s*va*vb
            return {k:v for k,v in out.items() if v}
        def word(i): return {1<<i:Q(1)}
        def gamma(v): return add(*(scale(v[i],word(i)) for i in range(n)))
        def dot(v,w): return sum(sig[i]*v[i]*w[i] for i in range(n))
        def basis(i):return [Q(int(i==j)) for j in range(n)]
        t=[Q(0)]*n;t[5]=Q(2)
        mean=[x/2 for x in t]
        Ct=gamma(t)
        z=[]
        for i in range(n):
            if i<h:z.append({});continue
            z.append(add({0:sig[i]*t[i]},scale(-Q(1,r),mul(word(i),Ct))))
        def ev(v):return add(*(scale(v[i],z[i]) for i in range(n)))
        assert add(*(scale(sig[i],mul(word(i),z[i])) for i in range(n)))=={}
        assert ev(t)=={0:-Q(4)*(1-Q(1,r))}
        zh=ev(mean)
        II=[[[Q(0)]*n for j in range(h)] for i in range(h)]
        II[0][0]=[-x/2 for x in mean];II[0][0][2]+=1
        II[1][1]=[x/2 for x in mean];II[1][1][2]+=1
        II[0][1][3]=II[1][0][3]=Q(1)
        assert [sum(sig[i]*II[i][i][k] for i in range(h)) for k in range(n)]==mean
        for alpha in [Q(0),Q(1,r-1),Q(2,7)]:
            # B[i][j][k]=(B_ei ej)^k.
            B=[[[Q(0)]*n for j in range(n)] for i in range(n)]
            for i in range(h):
                for j in range(h):
                    B[i][j]=[-x for x in II[i][j]]
                for j in range(h,n):
                    for k in range(h): B[i][j][k]=sig[k]*sig[j]*II[i][k][j]
            for i in range(h,n):
                for j in range(h,n):
                    B[i][j]=[alpha*((sig[i] if i==j else 0)*mean[k]
                                     -sig[j]*mean[j]*int(k==i)) for k in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n): assert sig[k]*B[i][j][k]+sig[j]*B[i][k][j]==0
            w=[sum(sig[i]*B[i][i][k] for i in range(n)) for k in range(n)]
            assert w==[(-1+(r-1)*alpha)*x for x in mean]
            T=[[[B[i][j][k]-B[j][i][k] for k in range(n)] for j in range(n)] for i in range(n)]
            F=[[ev(T[i][j]) for j in range(n)] for i in range(n)]
            # Exact E1/E3 from full parallel jet D'=0: source one-form jet is z∘B.
            source_jet=[[ev(B[i][j]) for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):assert add(source_jet[i][j],scale(-1,source_jet[j][i]))==F[i][j]
            delta=scale(-1,add(*(scale(sig[i],source_jet[i][i]) for i in range(n))))
            assert delta==scale(-1,ev(w))
            CF=[add(*(scale(sig[i],mul(word(i),F[i][j])) for i in range(n))) for j in range(n)]
            GCF=add(*(scale(sig[j],mul(word(j),CF[j])) for j in range(n)))
            assert GCF==scale(2*alpha,zh)
            a=Q(1);c0=-Q(1,n-2);L=2*a+n*c0
            phi=[add(scale(a,CF[j]),scale(c0/2,mul(word(j),GCF))) for j in range(n)]
            Gphi=add(*(scale(sig[j],mul(word(j),phi[j])) for j in range(n)))
            assert Gphi==scale(L*alpha,zh)
            for j in range(h):assert phi[j]==scale(c0*alpha,mul(word(j),zh))
            sw=ev(w)
            assert sw==scale(-1+(r-1)*alpha,zh)
            if alpha==0:
                assert all(x=={} for x in phi)
                assert sw!={}
                # Weighted-adjoint survivor: grad_N f=mean exactly cancels SW.
                assert add(sw,ev(mean))=={}
            if alpha==Q(1,r-1):assert sw=={} and Gphi!={}


    def native_scalar_constants():
        normal_rank=10
        zt=Q(-4)*(1-Q(1,normal_rank))
        assert zt==-Q(18,5)
        assert -zt/2==Q(9,5)
        a=Q(1);c0=-a/12;L=2*a+14*c0
        assert L==Q(5,6)
        assert L*Q(1,9)!=0


    def density_controls():
        # Exact directional derivative of f=-1/2 log|det(g^-1 y)|.
        # A diagonal representative suffices as a supporting control; proof is tensorial.
        diag=[Q(-2),Q(3),Q(5),Q(7)]
        n=4
        for i in range(n):
            for j in range(i,n):
                v=[[Q(0)]*n for _ in range(n)]
                v[i][j]=v[j][i]=Q(1)
                tr=sum(v[k][k]/diag[k] for k in range(n))
                # K_y(t/2,v)=tr((I/2)y^-1v)-tr(I/2)tr(y^-1v)/2.
                pairing=tr/2-Q(n,4)*tr
                assert pairing==-tr/2
        # Horizontal lift has dy=Gamma^T*y+y*Gamma and same for g,
        # so logarithmic determinant ratio has derivative zero, including nonzero trGamma.
        Gamma=[[Q(1+2*i-j) for j in range(n)] for i in range(n)]
        for gd in [[Q(-1),Q(1),Q(1),Q(1)],diag]:
            derivative=[[Gamma[j][i]*gd[j]+gd[i]*Gamma[i][j] for j in range(n)] for i in range(n)]
            logderivative=sum(derivative[k][k]/gd[k] for k in range(n))
            assert logderivative==2*sum(Gamma[k][k] for k in range(n))


    grade_factor_support(); exterior_controls(); native_scalar_constants(); density_controls()
    return True

def joint_controls():
    import sympy as s
    I=s.I
    P=s.Matrix([[0,1],[1,0]])
    Q=s.Matrix([[0,-I],[I,0]])
    Z=s.diag(1,-1)
    E2=s.eye(2)
    kp=s.kronecker_product
    gamma=[kp(P,E2,E2),kp(Q,E2,E2),kp(Z,P,E2),kp(Z,Q,E2),kp(Z,Z,P),kp(Z,Z,Q)]
    h,m,n,d=2,4,6,8
    E=s.eye(d)
    zero=s.zeros(d,d*m)
    simp=lambda A:A.applyfunc(s.simplify)
    eq=lambda A,B: simp(A-B)==s.zeros(*A.shape)
    for i in range(n):
        for j in range(n):
            assert eq(gamma[i]*gamma[j]+gamma[j]*gamma[i],2*(i==j)*E)
    # Hidden projection columns span ker Gamma_N.
    z=[s.Matrix.hstack(*[(E if j==k else s.zeros(d))-gamma[h+j]*gamma[h+k]/m for k in range(m)]) for j in range(m)]
    assert eq(sum((gamma[h+j]*z[j] for j in range(m)),zero),zero)
    # Symmetric II with mean H=n_0 and an independent traceless normal component.
    ii=[[[s.Rational(1,2),1,0,0],[0,0,0,0]],[[0,0,0,0],[s.Rational(1,2),-1,0,0]]]
    cz=lambda v:sum((v[j]*gamma[h+j] for j in range(m)),s.zeros(d))
    zv=lambda v:sum((v[j]*z[j] for j in range(m)),zero)
    H=[1,0,0,0]
    cH=cz(H)
    w=zv(H)
    G=[sum((gamma[u]*zv(ii[u][a]) for u in range(h)),zero) for a in range(h)]
    KH=[-sum((cz(ii[a][b])*gamma[b]/2 for b in range(h)),s.zeros(d)) for a in range(h)]
    K0=[H[j]*E-cH*gamma[h+j] for j in range(m)]
    Kend=[H[j]*E+cH*gamma[h+j]/(2*(m-2)) for j in range(m)]
    def maps(K):
        S=sum((K[h+j]*z[j] for j in range(m)),zero)
        R=[sum((gamma[h+j]*K[i]*z[j] for j in range(m)),zero) for i in range(n)]
        W=sum((gamma[i]*R[i] for i in range(n)),zero)
        U=sum((gamma[i]*K[i] for i in range(n)),s.zeros(d))
        V=sum((gamma[h+j]*U*z[j] for j in range(m)),zero)
        assert eq(V,2*S-W)
        return S,R,W
    S,R,W=maps(KH+K0)
    assert eq(S,w)
    assert all(eq(R[a],-G[a]) for a in range(h))
    assert eq(W,-(2*m-3)*w)
    assert W!=zero
    assert all(eq(K+K.conjugate().T,s.zeros(d)) for K in KH+K0)
    # Homogeneous skew solutions cannot change W_N.
    chi=gamma[h]*gamma[h+1]*gamma[h+2]*gamma[h+3]
    for F in [I*E,chi,I*E+2*chi]:
        extra=[F*gamma[h+j] for j in range(m)]
        assert all(eq(K+K.conjugate().T,s.zeros(d)) for K in extra)
        Sp,Rp,Wp=maps(KH+[K0[j]+extra[j] for j in range(m)])
        assert eq(Sp,w) and eq(Wp,W)
    # Exact complex-End escape, inadmissible for this same Hermitian form.
    Se,Re,We=maps(KH+Kend)
    assert eq(Se,w) and eq(We,zero)
    assert all(eq(Re[a],-G[a]) for a in range(h))
    for j in range(m):
        assert eq(Kend[j]+Kend[j].conjugate().T,s.Rational(2*m-3,m-2)*H[j]*E)
    assert not eq(Kend[0]+Kend[0].conjugate().T,s.zeros(d))
    # Complete raw outputs; c is arbitrary here, a,g,L nonzero.
    a,c,g=s.Integer(1),-s.Rational(1,n-2),s.Integer(1)
    L=2*a+n*c
    assert L!=0
    for S,R,W,expect_zero in [(S,R,W,False),(Se,Re,We,True)]:
        top=[-a*(G[k]+R[k])+c*gamma[k]*(S-W-w) for k in range(h)]
        trace=L*(S-W-w)
        scalar=g*(S-w)
        if expect_zero:
            assert all(eq(x,zero) for x in top+[trace,scalar])
        else:
            assert not eq(trace,zero)
    # Same LC-normal-jet density escape: tangent Spin repair, no normal K.
    Sd,Rd,Wd=maps(KH+[s.zeros(d) for _ in range(m)])
    assert eq(Sd,zero) and eq(Wd,-w)
    assert all(eq(-a*(G[k]+Rd[k])+c*gamma[k]*(Sd-Wd-w),zero) for k in range(h))
    assert eq(L*(Sd-Wd-w),zero)
    assert eq(g*(Sd-w)+g*w,zero)
    # Nonunitary control fails the actual same-Hermitian-adjoint SW arrow.
    Sactual=-sum((Kend[j].conjugate().T*z[j] for j in range(m)),zero)
    assert eq(Sactual-Se,-s.Rational(2*m-3,m-2)*w)
    assert not eq(Sactual,w)
    pass
    return True

def density_current_controls():
    import sympy as s
    x,t=s.symbols('x t',real=True)
    Dt=s.Matrix([[2,1],[0,3]])
    Dx=s.Matrix([[1,2],[-1,1]])
    M=s.Matrix([[1,x],[2*x,0]])
    V=s.Matrix([[0,0],[t,0]])
    B=s.diag(2,3)
    rho=s.exp(t)
    # Geometric lower term has no derivative on the independent connection slice x.
    assert (B*(M+V)).diff(x)==(B*M).diff(x)
    assert (rho*B*(M+V)).diff(x)==rho*(B*M).diff(x)
    assert ((rho*B*(M+V)).diff(x)).subs(t,0)==(B*M).diff(x)
    # Intrinsic contraction is zero order and commutes with position-dependent spin wrappers.
    E2=s.Matrix([[1,x],[0,1]])
    E4=s.diag(E2,E2)
    V4=s.BlockMatrix([[s.zeros(2),s.zeros(2)],[t*s.eye(2),s.zeros(2)]]).as_explicit()
    assert s.simplify(E4*V4*E4.inv()-V4)==s.zeros(4)
    assert (E4*V4*E4.inv()).diff(x)==s.zeros(4)
    # Positive density row multiplication cancels from normalized principal AND lower operator.
    assert s.simplify((rho*B*Dt).inv()*(rho*B*Dx)-Dt.inv()*Dx)==s.zeros(2)
    assert s.simplify((rho*B*Dt).inv()*(rho*B*M)-Dt.inv()*M)==s.zeros(2)
    # Adding the lower term is an actual change; multiplying the density alone cannot supply it.
    assert s.simplify(Dt.inv()*V)!=s.zeros(2)
    # A varying density changes the formal divergence by its logarithmic derivative.
    u=x*x+1
    assert s.simplify(-s.exp(-x)*s.diff(s.exp(x)*u,x)+s.diff(u,x)+u)==0
    # Broader stable natural category cannot use L=0 to escape the trace equation.
    a,e,g=s.symbols('a e g',nonzero=True)
    c=-a/7
    L=2*a+14*c; Q=a+12*c
    assert L==0 and s.simplify(Q+5*a/7)==0
    assert s.simplify(e*g*Q)!=0
    pass
    return True

def run():
    suites=[]
    for name,fn,scope in [
        ('unitary_lower_image',lower_controls,'Exact reduced Clifford control of all-component response, skew homogeneous remainder, nonunitary comparison, complete trace identity and mean-zero Spin survivor'),
        ('exterior_and_density',exterior_controls_suite,'Native Cl14 blade-factor support, exact metric torsion/adjoint tradeoff, arbitrary-extension proof support and determinant-density gradient controls'),
        ('joint_full_receiver',joint_controls,'Full hidden-kernel Cl6 control, all-row obstruction, nonunitary paired-arrow escape and actual-adjoint failure, same-reference-jet gradient survivor'),
        ('density_current',density_current_controls,'Fixed-density primitive current preservation, weighted current scaling, density-only row-rescaling failure and stable-family trace nondegeneracy')]:
        assert fn();suites.append(dict(name=name,passed=True,scope=scope))
    refs=['explorations/conditional-build/source-lower-term-compatibility-2026-11-13.md', 'explorations/conditional-build/source-exterior-connection-2026-11-13.md']
    deps=['lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md','explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md','explorations/conditional-build/source-chimeric-trace-compatibility-2026-11-13.md','explorations/conditional-build/source-prescription-current-2026-11-13.md','tests/program-focus/source_exterior_connection_probe.py']
    return dict(schema_version='1.0',program_target='X-P1-P2 / X-P2-P3',tier='T2',classification='INTERNAL_STRUCTURAL_ONLY',claim_ceiling='Typed natural scalar-weight operator category, compatible Clifford adjoint, declared normal jets and receiver; gradient lower rival is explicit but not source selected; no effective2+1, action/class-C or global-domain verdict',evidence_kind='Written proofs plus four exact supporting/contrary suites; suite counts are not discovery counts',primary_source_sha256='3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4',suites=suites,proof_refs=refs,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs+deps})

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();r=run()
    if args.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert json.loads(REPORT.read_text())==r,'stored evidence/dependency mismatch'
    print(json.dumps({'passed_suites':len(r['suites']),'suites':[s['name'] for s in r['suites']]}))
