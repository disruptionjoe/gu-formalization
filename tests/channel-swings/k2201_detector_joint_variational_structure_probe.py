#!/usr/bin/env python3
"""Finite detector Hessian identities and exact full-tail curvature witness."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
from k2168_finite_budget_moment_envelope_probe import IV,sqrtq,squeeze
C=F(40,3)
def p(n):return F(3,4)*F(1,4)**n
def ap(s):return F(41,3)*s-3/s**3
def app(s):return F(41,3)+9/s**4
def sq(v):
    if v.a>=0:return IV(v.a*v.a,v.b*v.b)
    if v.b<=0:return IV(v.b*v.b,v.a*v.a)
    return IV(0,max(v.a*v.a,v.b*v.b))
def tridiagonal_solve(diagonal,off,rhs):
    """Exact LDL solve, linear arithmetic and storage; SPD pivots are checked."""
    piv=[F(diagonal[0])];low=[];forward=[F(rhs[0])]
    for j in range(1,len(diagonal)):
        assert piv[-1]>0
        low.append(F(off[j-1])/piv[-1])
        piv.append(F(diagonal[j])-low[-1]*F(off[j-1]))
        forward.append(F(rhs[j])-low[-1]*forward[-1])
    assert piv[-1]>0
    out=[v/d for v,d in zip(forward,piv)]
    for j in range(len(out)-2,-1,-1):out[j]-=low[j]*out[j+1]
    return out
def branch(z,tail,w,fault=None):
    """z includes n=0..K. Retain edge K->K+1 and every constant-tail edge."""
    K=len(z)-1
    R=sum((F(n)+F(1,2))*v for n,v in enumerate(z))+tail*F(1,4)**(K+1)*(K+1+F(5,6))
    T=IV(tail*(F(K+1)+F(4,3))*F(1,4)**(K+1)/2)
    Tprime=IV(0);minus_Tsecond=IV(0)
    for n in range(K+1):
        nxt=z[n+1] if n<K else tail*p(K+1)
        wn=w[n+1] if n<K else F(0)
        radical=(n+1)*sqrtq(z[n]*nxt)
        T+=radical
        if fault=='omit_boundary' and n==K:continue
        Tprime+=radical*(w[n]/z[n]+wn/nxt)/2
        minus_Tsecond+=radical*(w[n]/z[n]-wn/nxt)**2/(2 if fault=='edge_factor' else 4)
    return R,T,Tprime,minus_Tsecond

def controls(fault=None):
    out={};ck=lambda k,v:out.__setitem__(k,bool(v));zero=lambda x:S.simplify(x)==0
    z,zp=S.symbols('z zp',positive=True);v,vp,t=S.symbols('v vp t',real=True)
    actual=S.diff(S.sqrt((z+t*v)*(zp+t*vp)),t,2).subs(t,0)
    coeff=S.Rational(1,2) if fault=='edge_factor' else S.Rational(1,4)
    ck('original_edge_second_derivative',zero(actual+coeff*S.sqrt(z*zp)*(v/z-vp/zp)**2))
    Q,b1,b0,d1,d0,t1,t0=S.symbols('Q b1 b0 d1 d0 t1 t0',nonzero=True)
    reduced=Q+ (1 if fault=='schur_sign' else -1)*(b1*b1/d1+b0*b0/d0)
    joint=Q+2*b1*t1+2*b0*t0+d1*t1*t1+d0*t0*t0
    ck('joint_square_completion',zero(joint-reduced-d1*(t1+b1/d1)**2-d0*(t0+b0/d0)**2))
    # True branch-optimized constant profile; the exact-contrast scores vanish.
    V=[[F(2),F(1),F(0)],[F(5),F(0),F(1)]]
    def flat(vv,omit=False):
        z=[p(n)/2 for n in range(4)];cur=F(0);dt=F(0)
        for n in range(2 if omit else 3):
            a=vv[n];b=vv[n+1] if n<2 else F(0)
            root=z[n]/2
            cur+=C*2*(n+1)*root*(a/z[n]-b/z[n+1])**2/4
            dt+=(n+1)*root*(a/z[n]+b/z[n+1])/2
        return cur,dt
    P=S.zeros(2)
    for i,vi in enumerate(V):
        rv=sum((F(n)+F(1,2))*w for n,w in enumerate(vi));qv=sum((3*n-1)*w for n,w in enumerate(vi))
        qi,dt=flat(vi,fault=='omit_boundary')
        b_one=ap(F(1))*rv-C*dt
        b_zero=-ap(F(1))*rv+(-C if fault=='complement_score' else C)*dt
        ck('flat_contrast_'+str(i),qv==0)
        ck('flat_stationary_scores_'+str(i),b_one==0 and b_zero==0)
        ck('flat_boundary_retained_'+str(i),qi==flat(vi)[0])
        P[i,i]=S.Rational(qi.numerator,qi.denominator)
    cross=(flat([a+b for a,b in zip(*V)])[0]-flat(V[0])[0]-flat(V[1])[0])/2
    P[0,1]=P[1,0]=S.Rational(cross.numerator,cross.denominator)
    ck('flat_positive_principal_minors',P[0,0]>0 and P.det()>0)
    # Independent exact linear-arithmetic constrained inverse algorithm.
    diag=[F(2),F(3),F(4)];off=[F(-1),F(-1)];LL=S.Matrix([[2,-1,0],[-1,3,-1],[0,-1,4]])
    qq=S.Matrix([-1,2,5]);VV=S.Matrix([[2,5],[1,0],[0,1]])
    bb=S.Matrix([[1,2,3],[-2,3,1]])
    columns=[tridiagonal_solve(diag,off,row) for row in [[-1,2,5],[1,2,3],[-2,3,1]]]
    for j,(rhs,sol) in enumerate(zip([qq,bb.row(0).T,bb.row(1).T],columns)):
        ck('tridiagonal_original_system_'+str(j),LL*S.Matrix(sol)==rhs)
    zz=S.Matrix(columns[0]);inverse=LL.inv()
    GG=inverse if fault=='omit_contrast_projection' else inverse-zz*zz.T/(qq.dot(zz))
    target=VV*(VV.T*LL*VV).inv()*VV.T
    ck('constrained_inverse_identity',GG==target)
    ck('constrained_inverse_annihilates_q',GG*qq==S.zeros(3,1))
    YY=S.Matrix.hstack(S.Matrix(columns[1]),S.Matrix(columns[2]))
    susceptibility=bb*YY-(bb*zz)*(bb*zz).T/(qq.dot(zz))
    ck('three_rhs_susceptibility',susceptibility==bb*target*bb.T)
    ck('constrained_susceptibility',bb*GG*bb.T==susceptibility)
    # Algebraic Schur/inertia controls. These are not profiles or optimizers.
    for name,bvals,expected in [('positive',[F(1,2),F(1,3)],(0,0)),('one_negative',[F(2),F(1,3)],(1,0)),('two_negative',[F(2),F(3)],(2,0)),('singular',[F(1),F(1,3)],(0,1))]:
        PP=S.diag(1,1,1);DD=S.eye(2);BB=S.Matrix([[bvals[0],0,0],[0,bvals[1],0]])
        MM=PP-BB.T*DD.inv()*BB;SS=DD-BB*PP.inv()*BB.T
        counts=lambda M:(sum(int(bool(v<0))*n for v,n in M.eigenvals().items()),sum(int(bool(v==0))*n for v,n in M.eigenvals().items()))
        ck('schur_inertia_'+name,counts(MM)==counts(SS)==expected)
        vv=S.Matrix(S.symbols('v0:3'));tt=S.Matrix(S.symbols('t0:2'))
        block=(vv.T*PP*vv+2*tt.T*BB*vv+tt.T*DD*tt)[0]
        ck('schur_congruence_'+name,zero(block-(vv+PP.inv()*BB.T*tt).dot(PP*(vv+PP.inv()*BB.T*tt))-tt.dot(SS*tt)))
    # Exact polynomially corrected recurrence, independent of any numerical tail.
    r,a,n=S.symbols('r a n',nonzero=True)
    k=1/r+r/4;c=-a/r**2+(r+a)/4
    residual=1/(r+a/(n-1))+(1+1/n)*(r+a/n)/4-k-c/n
    rhs=a*(a-r)/(r**2*n*(r*(n-1)+a))+a/(4*n*n)
    ck('tail_residual_identity',zero(residual-rhs))
    aa=r*r*(r+ (4 if fault=='tail_coefficient' else -4)*c)/(4-r*r)
    ck('tail_first_order_coefficient',zero(aa-a))
    ck('tail_exact_fixture',F(1,4)*F(1,2)/F(15,4)==F(1,30))
    ck('tail_squared_exponent',(1 if fault=='tail_exponent' else 2)*F(1,30)/F(1,2)==F(2,15))
    return out

def certificate():
    # Smooth K2184's fixed-mass/fixed-contrast chord; every occupation is positive.
    eps=F(1,10000);delta=F(1,10**20)
    u=[F(0),F(42,5120),F(0),F(0),F(0),F(0),F(33,5120)]
    v=[F(0),F(0),F(0),F(3,256),F(3,1024),F(0),F(0)]
    x=[delta*p(n)+eps*(a+b)/2 for n,(a,b) in enumerate(zip(u,v))]
    y=[p(n)-z for n,z in enumerate(x)];w=[eps*(b-a) for a,b in zip(u,v)]
    assert all(0<z<p(n) for n,z in enumerate(x)) and 0<delta<1
    assert sum(w)==sum(n*z for n,z in enumerate(w))==sum((3*n-1)*z for n,z in enumerate(w))==0
    assert sum((3*n-1)*eps*(a+b)/2 for n,(a,b) in enumerate(zip(u,v)))==F(129,1024)*eps
    pieces=[];curv=IV(0)
    for z,tail in [(x,delta),(y,1-delta)]:
        R,T,Tp,negTpp=branch(z,tail,w)
        ss=squeeze(C*T/R)
        assert (R*ap(IV(ss.a))-C*T).b<0 and (R*ap(IV(ss.b))-C*T).a>0
        positive=C*ss*negTpp
        response=C*C*sq(Tp)/(R*app(ss))
        curv+=positive-response
        pieces.append(dict(radius=str(R),coherence=T.pair(),coherence_derivative=Tp.pair(),negative_coherence_curvature=negTpp.pair(),squeeze=ss.pair(),positive_curvature=positive.pair(),response= response.pair()))
    assert curv.b<0,('not_certified',curv.pair())
    # Boundary omission must change the genuine positive form, not merely a hash.
    assert branch(x,delta,w)[3].a>branch(x,delta,w,'omit_boundary')[3].b
    return dict(epsilon=str(eps),delta=str(delta),contrast=str(F(129,1024)*eps),profile=list(map(str,x)),direction=list(map(str,w)),tail_effect=str(delta),branch_data=pieces,optimized_profile_curvature=curv.pair(),scope='Positive interior fixed-contrast and fixed-probability profile with truly optimized branch squeezes. Not effect-stationary, not a detector optimum. Full unchanged tail included.')

FAULTS=['edge_factor','schur_sign','complement_score','omit_boundary','omit_contrast_projection','tail_coefficient','tail_exponent']
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    checks=controls();assert all(checks.values()),[k for k,v in checks.items() if not v]
    failures={}
    for fault in FAULTS:
        bad=[k for k,v in controls(fault).items() if not v];assert bad,('undetected',fault);failures[fault]=bad
    witness=certificate()
    deps=['explorations/conditional-build/k2201-detector-joint-variational-structure-2026-10-28.md','explorations/conditional-build/k2184-global-detector-structure-2026-10-28.md','explorations/conditional-build/k2194-detector-optimizer-structure-2026-10-28.md','explorations/conditional-build/k2198-detector-profile-certificates-2026-10-28.md','tests/channel-swings/k2168_finite_budget_moment_envelope_probe.py']
    report=dict(result_id='K2201',status='conditional_exact_variational_structure',checks=checks,fault_failures=failures,negative_curvature_witness=witness,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal finite-support Hessian/Morse-index/Schur and tail-asymptotic proofs; exact symbolic controls; full-tail rational-interval negative-curvature witness. No full infinite Hessian inverse, joint uniqueness, or global optimality certificate.')
    dst=ROOT/'lab/process/k2201-detector-joint-variational-structure.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report
    print(json.dumps(dict(result='K2201',checks=len(checks),faults=len(failures),curvature_strictly_negative=True)))
if __name__=='__main__':main()
