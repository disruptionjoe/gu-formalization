#!/usr/bin/env python3
"""Rational whole-tail Hessian certificate; no floating-point sign decisions."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, os
ROOT=Path(os.environ.get('GU_REPO_ROOT', str(Path(__file__).resolve().parents[2])))
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
from k2168_finite_budget_moment_envelope_probe import IV,squeeze
from k2201_detector_joint_variational_structure_probe import tridiagonal_solve
C=F(40,3)
LBOUND=F(9,25)
SIGMA=F(1,2)
RHO=F(10,17)

def p(n): return F(3,4)*F(1,4)**n
def q(n): return F(3*n-1)
def roots(n):
    t=F(1,2)**(n+1)
    return ((1-t*t)/(1+t*t),2*t/(1+t*t))
def z(n,j): return p(n)*roots(n)[j]**2
def ap(s): return F(41,3)*s-3/(s**3)
def app(s): return F(41,3)+9/(s**4)
def absolute(x):
    return max(abs(x.a),abs(x.b)) if isinstance(x,IV) else abs(x)
def midpoint(x): return (x.a+x.b)/2 if isinstance(x,IV) else x
def rnd(x,bits=110):
    den=1<<bits
    return F((x*den+F(1,2)).numerator//(x*den+F(1,2)).denominator,den)
def outward(x,bits=150):
    den=1<<bits
    aa=x.a*den;bb=x.b*den
    return IV(F(aa.numerator//aa.denominator,den),F(-((-bb.numerator)//bb.denominator),den))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def matvec(diag,off,v):
    return [diag[n]*v[n]+(off[n-1]*v[n-1] if n else 0)
            +(off[n]*v[n+1] if n+1<len(v) else 0) for n in range(len(v))]
def edge_h(n,j,s):
    if n<0:return 0
    return C*s*(n+1)*p(n)*roots(n)[j]*roots(n+1)[j]/8
def coefficients(m,squeezes,omit_boundary=False):
    diag=[];off=[]
    for n in range(m+1):
        diag.append(sum((edge_h(n-1,j,s)+(0 if omit_boundary and n==m else edge_h(n,j,s)))/z(n,j)**2 for j,s in enumerate(squeezes)))
        if n<m:off.append(-sum(edge_h(n,j,s)/(z(n,j)*z(n+1,j)) for j,s in enumerate(squeezes)))
    return diag,off
def score(n,j,s):
    a=roots(n)[j]
    g=(n*roots(n-1)[j]/a if n else 0)+(n+1)*roots(n+1)[j]/(4*a)
    ans=ap(s)*(F(n)+F(1,2))-C*g
    return ans if j==0 else -ans
def form(v,w,squeezes):
    m=max(len(v),len(w))-1
    v=list(v)+[F(0)]*(m+2-len(v))
    w=list(w)+[F(0)]*(m+2-len(w))
    return sum(edge_h(n,j,s)*(v[n]/z(n,j)-v[n+1]/z(n+1,j))
               *(w[n]/z(n,j)-w[n+1]/z(n+1,j))
               for n in range(m+1) for j,s in enumerate(squeezes))
def tail_moment(start): return (F(start)+F(4,3))*F(1,4)**start
def complementary_tail_moment(start):
    h=RHO**2/4
    return z(start,1)*((start+1)/(1-h)+h/(1-h)**2)
def branch_moments(j,M=60):
    rr=sum((F(n)+F(1,2))*z(n,j) for n in range(M+1))
    tt=sum((n+1)*p(n)*roots(n)[j]*roots(n+1)[j]/2 for n in range(M+1))
    start=M+1
    rtail=(F(start)+F(5,6))*F(1,4)**start
    ttail=tail_moment(start)/2
    return outward(IV(rr,rr+rtail)),outward(IV(tt,tt+ttail))
def galerkin(m,squeezes,project=True):
    diag,off=coefficients(m,squeezes)
    qq=[q(n) for n in range(m+1)]
    u=tridiagonal_solve(diag,off,qq)
    vv=[];ll=[]
    for j,s in enumerate(squeezes):
        bb=[score(n,j,s) for n in range(m+1)]
        y=tridiagonal_solve(diag,off,bb)
        lam=dot(qq,y)/dot(qq,u) if project else F(0)
        vv.append([a-lam*b for a,b in zip(y,u)])
        ll.append(lam)
    return vv,ll

def residual_head_norm(rr,omit_junction=False):
    stop=len(rr)-int(omit_junction)
    return sum(z(n,1)*absolute(rr[n])**2/(n+1) for n in range(stop))

def controls(fault=None):
    out={}
    def ck(name,value):out[name]=bool(value)
    e=roots(0)[0]**2;ep=roots(1)[0]**2
    f=1-e;t=(1-ep)/f
    u=F(3,7);up=F(-2,5)
    X=u/e-2*up/ep;w=u-2*up/t
    tcoef=2*t if fault=='inverse_factor' else t
    back=((e*ep*X-tcoef*e*w)/(1-t),
          (t*e*ep*X-t*ep*w)/(2*(1-t)))
    ck('inverse_edge_transform',back==(u,up))
    # Direct original Hessian edge against its transformed expression.
    vx=u;vnext=up/2
    original=sum(C/4*roots(0)[j]*roots(1)[j]/2
                 *(vx/(roots(0)[j]**2)-vnext/(roots(1)[j]**2/4))**2 for j in range(2))
    transformed=C/8*(roots(0)[0]*roots(1)[0]*X*X+roots(1)[1]/roots(0)[1]/f*w*w)
    ck('original_edge_identity',original==transformed)
    h=roots(1)[1]/(2*roots(0)[1])
    a0=F(3,7);a1=F(-2,5)
    va=a0*roots(0)[1];vb=a1*roots(1)[1]/2
    original_y=C/4*roots(0)[1]*roots(1)[1]/2*(va/f-vb/((1-ep)/4))**2
    recurrence_y=C/(2 if fault=='complementary_norm_factor' else 4)/h*(a1-h*a0)**2
    ck('complementary_weighted_recurrence',original_y==recurrence_y)
    rho=F(1,2) if fault=='false_tail_ratio' else RHO
    ck('rational_profile_ratio_certificate',roots(1)[1]/roots(0)[1]<=rho)
    ss=[F(1),F(1)];m=3
    vv,lam=galerkin(m,ss,project=fault!='omit_contrast')
    qq=[q(n) for n in range(m+1)]
    ck('actual_profile_constraint',all(dot(qq,v)==0 for v in vv))
    diag,off=coefficients(m,ss,omit_boundary=fault=='omit_boundary')
    probe=[F(0),F(0),F(0),F(1)]
    ck('actual_profile_last_edge',dot(probe,matvec(diag,off,probe))==form(probe,probe,ss))
    # The finite constrained exact Riesz solution supplies an independent
    # finite check of the residual identity for deliberately inexact trials.
    gg,_=galerkin(m,ss)
    trial=[[a/2 for a in g] for g in gg]
    kk=[[form(a,b,ss) for b in gg] for a in gg]
    for i in range(2):
        for j in range(2):
            bi=[score(n,i,ss[i]) for n in range(m+1)]
            bj=[score(n,j,ss[j]) for n in range(m+1)]
            sign=1 if fault=='gram_sign' else -1
            tij=dot(bi,trial[j])+dot(bj,trial[i])+sign*form(trial[i],trial[j],ss)
            erri=[a-b for a,b in zip(gg[i],trial[i])]
            errj=[a-b for a,b in zip(gg[j],trial[j])]
            ck('residual_gram_'+str(i)+str(j),kk[i][j]-tij==form(erri,errj,ss))
    start=7
    claimed=tail_moment(start+(1 if fault=='tail_off_by_one' else 0))
    direct=sum((n+1)*p(n) for n in range(start,start+8))+tail_moment(start+8)
    ck('exact_whole_tail_moment',claimed==direct)
    h=RHO**2/4
    geometric=sum((start+k+1)*z(start,1)*h**k for k in range(8))
    remainder=z(start,1)*h**8*((start+9)/(1-h)+h/(1-h)**2)
    ck('complementary_geometric_tail_identity',geometric+remainder==complementary_tail_moment(start))
    # Junction-only residual must contribute its actual positive norm bound.
    actual_diag,actual_off=coefficients(m+1,ss)
    actual_lv=matvec(actual_diag,actual_off,probe+[F(0)])
    junction_only=[F(0)]*(m+1)+[actual_lv[-1]]
    junction=residual_head_norm(junction_only,omit_junction=fault=='omit_residual_junction')
    ck('junction_residual_not_discarded',actual_lv[-1]!=0 and junction==z(m+1,1)*actual_lv[-1]**2/(m+2))
    return out

FAULTS=['inverse_factor','false_tail_ratio','omit_contrast','omit_boundary',
        'gram_sign','tail_off_by_one','omit_residual_junction','complementary_norm_factor']

def certify_at(m,ss,ds):
    center=[midpoint(s) for s in ss]
    vv,lam=galerkin(m,center)
    trial=[]
    for v in vv:
        w=[rnd(a) for a in v]
        w[0]=sum(q(n)*w[n] for n in range(1,len(w)))
        assert sum(q(n)*w[n] for n in range(len(w)))==0
        trial.append(w)
    lam=[rnd(a) for a in lam]
    kappa=C*min(ss[0].a*LBOUND,ss[1].a*SIGMA)*(1-RHO**2)**2/32
    kappa_y=(1-RHO**2)/(1/(kappa*(1-LBOUND))+8*RHO/(C*ss[1].a))
    Ms=[absolute(ap(ss[0]))+C*(1+F(5,12)),
        absolute(ap(ss[1]))+C*(1/SIGMA+RHO/4)]
    diag,off=coefficients(m+1,ss)
    eps=[];residuals=[]
    for j in range(2):
        w=trial[j]+[F(0)]
        lv=matvec(diag,off,w)
        rr=[score(n,j,ss[j])-lam[j]*q(n)-lv[n] for n in range(m+2)]
        head=residual_head_norm(rr)
        tail=(Ms[j]+3*abs(lam[j]))**2*complementary_tail_moment(m+2)
        eps.append((head+tail)/kappa_y)
        residuals.append(dict(prefix_sum=str(head),tail_sum=str(tail),junction=rr[-1].pair()))
    delta=sum(eps)
    tt=[]
    for i in range(2):
        row=[]
        for j in range(2):
            bi=[score(n,i,ss[i]) for n in range(m+1)]
            bj=[score(n,j,ss[j]) for n in range(m+1)]
            row.append(dot(bi,trial[j])+dot(bj,trial[i])-form(trial[i],trial[j],ss))
        tt.append(row)
    upper=[[((ds[i] if i==j else IV(0))-tt[i][j]) for j in range(2)] for i in range(2)]
    lower=[[upper[i][j]-(delta if i==j else 0) for j in range(2)] for i in range(2)]
    determinant=lower[0][0]*lower[1][1]-lower[0][1]*lower[1][0]
    decision='INDETERMINATE'
    witness=None
    if lower[0][0].a>0 and determinant.a>0:decision='STABLE'
    else:
        candidates=[[F(1),F(0)],[F(0),F(1)],[F(1),F(1)],[F(1),F(-1)]]
        a=midpoint(upper[0][0]);b=midpoint(upper[0][1])
        if a>0:candidates.append([-b/a,F(1)])
        for w in candidates:
            val=sum(w[i]*upper[i][j]*w[j] for i in range(2) for j in range(2))
            if val.b<0:
                decision='UNSTABLE';witness=dict(direction=list(map(str,w)),upper=val.pair());break
    return dict(support_last=m,decision=decision,kappa=str(kappa),kappa_y=str(kappa_y),
                epsilon_squared=list(map(str,eps)),delta=str(delta),
                susceptibility_lower=[[x.pair() for x in row] for row in tt],
                schur_lower=[[x.pair() for x in row] for row in lower],
                schur_upper=[[x.pair() for x in row] for row in upper],
                schur_lower_determinant=determinant.pair(),residuals=residuals,
                trials=[list(map(str,w)) for w in trial],lambdas=list(map(str,lam)),
                negative_witness=witness)

def certificate():
    ss=[];ds=[];moments=[]
    for j in range(2):
        rr,tt=branch_moments(j)
        s=squeeze(C*tt/rr)
        assert (rr*ap(IV(s.a))-C*tt).b<0
        assert (rr*ap(IV(s.b))-C*tt).a>0
        ss.append(s);ds.append(rr*app(s))
        moments.append(dict(radius=rr.pair(),coherence=tt.pair(),squeeze=s.pair()))
    attempts=[]
    for m in [4,8,12,16]:
        row=certify_at(m,ss,ds);attempts.append(row)
        if row['decision']!='INDETERMINATE':break
    last=attempts[-1]
    margin=F(6)
    released=None
    if last['decision']=='STABLE':
        for i in range(2):
            diagonal_lo=F(last['schur_lower'][i][i][0])
            off_abs=max(abs(F(x)) for x in last['schur_lower'][i][1-i])
            assert diagonal_lo-off_abs>margin
        assert sum(F(x) for x in last['epsilon_squared'])<F(53,50)
        released=dict(schur_lower_greater_than_identity_multiple=str(margin),
                      residual_delta_less_than='53/50')
    return dict(profile='t_n=2^(-n-1); e_n=((1-t_n^2)/(1+t_n^2))^2',
                is_optimizer=False,tail_constants=dict(L=str(LBOUND),sigma=str(SIGMA),rho=str(RHO)),
                moment_prefix_last=60,branches=moments,attempts=attempts,
                decision=attempts[-1]['decision'],
                released_rational_margins=released,
                scope='True branch-minimized curvature on every finite-support exact-contrast direction and its energy completion. Profile is not effect-stationary or an optimizer; no global-optimality claim.')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true')
    parser.add_argument('--output',type=Path);args=parser.parse_args()
    checks=controls();assert all(checks.values()),checks
    failures={}
    for fault in FAULTS:
        bad=[k for k,v in controls(fault).items() if not v]
        assert bad,('undetected',fault);failures[fault]=bad
    cert=certificate()
    deps=['explorations/conditional-build/k2201-detector-joint-variational-structure-2026-10-28.md',
          'explorations/conditional-build/k2198-detector-profile-certificates-2026-10-28.md',
          'explorations/conditional-build/k2196-detector-primal-dual-certificates-2026-10-28.md',
          'explorations/conditional-build/k2176-detector-certified-convergence-2026-10-27.md',
          'tests/channel-swings/k2168_finite_budget_moment_envelope_probe.py',
          'tests/channel-swings/k2201_detector_joint_variational_structure_probe.py']
    report=dict(result_id='K2204',status='conditional_energy_form_and_residual_certificate',
                checks=checks,fault_failures=failures,full_tail_fixture=cert,
                dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},
                probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                evidence_kinds='Written coercivity/Hilbert/finite-rank/residual proofs with convergence at strict Schur signs; exact algebraic controls; actual full-tail interval profile certificate at true minimizing squeezes. Bounded probe may return indeterminate. No singular-case decision, joint optimum, nonlinear smoothness, efficient complexity, source physics or external certification.')
    dst=args.output or ROOT/'lab/process/k2204-detector-infinite-stability-certificate.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report
    last=cert['attempts'][-1]
    print(json.dumps(dict(result='K2204',checks=len(checks),faults=len(failures),
                         decision=cert['decision'],support_last=last['support_last'],
                         epsilon_squared_display=[float(F(x)) for x in last['epsilon_squared']],
                         squeeze_display=[[float(F(x)) for x in b['squeeze']] for b in cert['branches']])))
if __name__=='__main__':main()
