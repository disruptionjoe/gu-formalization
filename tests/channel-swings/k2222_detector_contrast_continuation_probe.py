#!/usr/bin/env python3
"""K2222 exact uniform-contrast consumer.
Reuses K2219 free input bank; fresh interval admission/Schur and full exterior.
"""
import sys
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
import k2219_detector_global_capture_probe as capture
from k2219_detector_global_capture_probe import *
import json,hashlib,argparse
EPSILON=F(1,10**18)
UPPER_LIPSCHITZ=F(100)

def dual_eta(ss,u):
    return -(aa(ss[0])-aa(ss[1]))/2+C*(ss[0]*u[0][0]-ss[1]*u[1][0])/2

def repair_profile(ee,h,fault=None):
    repaired=ee[:];repaired[0]+=h/p(0) if fault=='repair_sign' else -h/p(0)
    return repaired

def contrast_shift(eta,h,fault=None):
    return (-1 if fault=='dual_sign' else 1)*eta*h

def upper_loss(epsilon,fault=None):
    return (0 if fault=='upper_loss' else UPPER_LIPSCHITZ)*epsilon

def uniform_constants(fault=None):
    ds=IV(F(1,2)-EPSILON,F(1,2)+EPSILON)
    wl=(ds-F(1,4))/2
    rxlo=3*ds/4-F(5,48); rxhi=(5-3*ds)/6
    ryhi=F(15,16)-3*ds/4
    # These are interval overbounds, not claims that interval dependencies vanish.
    ratio1=1-sqr(wl/rxlo)/4
    ratio0=1-sqr((1-wl)/ryhi)/4
    low=(ds+4*wl)/(2*ds+5*wl)
    cs={}
    ck=lambda k,v:cs.__setitem__(k,bool(v))
    ck('positive_interior_contrast',ds.a>F(1,4) and ds.b<F(3,4))
    ck('squeeze_lower0',F(17,25)**4<F(9,41))
    ck('squeeze_upper1',ap(F(111,100))>0 and ap(F(111,100))**2>C*C*ratio1.b)
    ck('squeeze_upper0',ap(F(91,100))>0 and ap(F(91,100))**2>C*C*ratio0.b)
    ck('squeeze_lower1',ap(F(9,10))<C*low.a)
    ck('Hessian1',rxhi.b*app(F(9,10))<16)
    ck('Hessian0',ryhi.b*app(F(17,25))<32)
    # Exact feasible d-family: repair only e0 by -h/p0. Tail remains unchanged.
    ee,ff,u=inputs(profile_at(F(0),F(0)),True)
    base_contrast=sum((3*n-1)*p(n)*ee[n] for n in range(N))+3*N*F(4)**-N*ee[N]
    ck('inherited_exact_contrast',base_contrast==F(1,2))
    for h in [-EPSILON,EPSILON]:
        repaired=repair_profile(ee,h,fault)
        actual=sum((3*n-1)*p(n)*repaired[n] for n in range(N))+3*N*F(4)**-N*repaired[N]
        ck('exact_contrast_repair_'+str(h),actual==F(1,2)+h)
    eta_test=dual_eta(CENTER,u)
    small_u=[v[:2] for v in u]
    dual0=old.dual(*CENTER,*small_u,eta_test,F(1,2))
    dual_plus=old.dual(*CENTER,*small_u,eta_test,F(1,2)+EPSILON)
    ck('independent_dual_contrast_sign',eta_test!=0 and dual_plus-dual0==contrast_shift(eta_test,EPSILON,fault))
    e0=IV(ee[0]-EPSILON/p(0),ee[0]+EPSILON/p(0))
    ck('feasible_head_cap',e0.a>F(3,20) and e0.b<F(1,5))
    ck('center_squeeze_bounds',all(F(2,3)<s<F(113,100) for s in CENTER))
    # dE/dx0=DeltaA/2-C/2*(s1 sqrt(x1/x0)-s0 sqrt(y1/y0)).
    # x1/x0 <=5/3 <(4/3)^2, y1/y0<=5/16<(3/5)^2.
    # A(s)<=13 on [2/3,113/100], so |DeltaA|<=13.
    ck('A_upper',max(aa(F(2,3)),aa(F(113,100)))<13)
    ck('root_ratio_bounds',F(5,3)<F(4,3)**2 and F(5,16)<F(3,5)**2)
    derivative_bound=F(13,2)+C/2*F(113,100)*(F(4,3)+F(3,5))
    ck('feasible_upper_Lipschitz',derivative_bound*EPSILON<upper_loss(EPSILON,fault))
    # Optional uniform C1 Taylor bound on all head-repaired optimizing profiles:
    # x0>=9/80,y0>=3/5; sqrt(x1),sqrt(y1)<=1/2; s_j<=113/100.
    second_bound=C/8*F(113,100)*(F(80,9)**2+F(5,3)**2)
    ck('head_second_derivative_bound',second_bound<200)
    return dict(checks=cs,head_energy_derivative_bound=str(derivative_bound),head_second_derivative_bound=str(second_bound),contrast_interval=[str(ds.a),str(ds.b)])

def basin_certificate():
    prior=inherited()
    ss=[IV(c-BASIN_RADIUS,c+BASIN_RADIUS) for c in CENTER]
    e,f,u=inputs(profile_at(F(0),F(0)),True)
    # Outward exported U is a valid inherited upper bound. Recompute fresh
    # slightly wider boxes and their entire residual certificate, so there is
    # no transfer of old bounds to an unjustified larger enclosure.
    U0=F(prior['feasible_energy_upper']);U=U0+upper_loss(EPSILON)
    eta_center=dual_eta(CENTER,u)
    eps=U-dual(CENTER,u).a+abs(eta_center)*EPSILON+capture_loss(BASIN_RADIUS)
    assert 0<eps<F(1,10**12)
    boxes=[prof.coordinate_box(n,u[0][n],u[1][n],eps,CENTER[0],CENTER[1]) for n in range(7)]
    # Admission applies to actual global minima and the inherited K2210
    # fixed-d minimizers; no continued stationary candidate is assumed.
    eta=out(C/4*(ss[0]*sqrtiv(boxes[1]/boxes[0])-ss[1]*sqrtiv((1-boxes[1])/(1-boxes[0])))-(aa(ss[0])-aa(ss[1]))/2)
    da=out(aa(ss[0])-aa(ss[1]));kv=out((F(5,4)*ss[0]-(da-3*eta)/C)/ss[1]);cv=out(ss[0]/(4*ss[1])-(da/2+eta)/(C*ss[1]))
    rt=sqrtq(boxes[2].a,bits=300).a
    knlo=kv.a-(ss[0]/ss[1]).b*(1-rt)-max(-cv.a,F(0))/3
    knhi=kv.b+(ss[0]/ss[1]).b/3*(1/rt-1)+max(cv.b,F(0))/3
    assert prof.barrier(knlo,knhi,2,F(1,3),F(1,2))
    L=F(3,20);SIG=F(1,3);RHO=F(2,3)
    for n in [0,1]:
     ratio=sqrtiv((1-boxes[n+1])/(1-boxes[n]));assert ratio.a>SIG and ratio.b<RHO
    assert boxes[0].a>L and boxes[0].b<F(1,5)
    kappa=C*min(ss[0].a*L,ss[1].a*SIG)*(1-RHO**2)**2/32
    ky=complementary_coercivity(kappa,1-boxes[0].b,RHO,ss[1].a)
    def z(n,j):return out(p(n)*(boxes[n] if j==0 else 1-boxes[n]))
    def h(n,j,s):return 0 if n<0 else out(C*s*(n+1)*sqrtiv(z(n,j)*z(n+1,j))/4)
    def coef(m,s):
     diag=[out(sum((h(n-1,j,s[j])+h(n,j,s[j]))/(z(n,j)**2) for j in range(2))) for n in range(m+1)]
     off=[out(-sum(h(n,j,s[j])/(z(n,j)*z(n+1,j)) for j in range(2))) for n in range(m)]
     return diag,off
    # For approximate solve use a single midpoint profile, not entrywise unrelated coefficients.
    midboxes=boxes[:]; midpoint_effects=[mid(e) for e in boxes]
    def score(n,j,s):
     g=(n*sqrtiv(z(n-1,j)/z(n,j)) if n else 0)+(n+1)*sqrtiv(z(n+1,j)/z(n,j))
     ans=out(ap(s)*(n+F(1,2))-C*g/2)
     return ans if j==0 else -ans
    m=3
    saved=boxes;boxes=[IV(v) for v in midpoint_effects];sm=[IV(mid(s)) for s in ss]
    dd,oo=coef(m,sm);dd=list(map(mid,dd));oo=list(map(mid,oo));qq=[F(3*n-1) for n in range(m+1)]
    uq=tridiagonal_solve(dd,oo,qq);trials=[];lams=[]
    def dot(v,w):return sum(a*b for a,b in zip(v,w))
    for j in range(2):
     b=[mid(score(n,j,sm[j])) for n in range(m+1)];un=tridiagonal_solve(dd,oo,b);lam=dot(qq,un)/dot(qq,uq)
     w=[F(((a-lam*b)*(1<<110)).__floor__(),1<<110) for a,b in zip(un,uq)]
     w[0]=sum(qq[n]*w[n] for n in range(1,m+1));trials.append(w);lams.append(F((lam*(1<<110)).__floor__(),1<<110))
    boxes=saved
    # Full moments, using complement ratio1/2 from n>=2 for sharper tail.
    hr=F(1,16);start=5
    r0lo=sum((n+F(1,2))*z(n,1).a for n in range(start))
    r0hi=sum((n+F(1,2))*z(n,1).b for n in range(start))+z(start,1).b*((start+F(1,2))/(1-hr)+hr/(1-hr)**2)
    rs=[IV(F(5,6)-r0hi,F(5,6)-r0lo),IV(r0lo,r0hi)]
    ds=[out(rs[j]*app(ss[j])) for j in range(2)]
    dd,oo=coef(m+1,ss)
    def matvec(d,a,v):return [out(d[n]*v[n]+(a[n-1]*v[n-1] if n else 0)+(a[n]*v[n+1] if n+1<len(v) else 0)) for n in range(len(v))]
    Ms=[absiv(ap(ss[0]))+C*(1+1/(4*sqrtq(L,bits=300).a)),absiv(ap(ss[1]))+C*(1/SIG+RHO/4)]
    epsj=[]
    for j in range(2):
     lv=matvec(dd,oo,trials[j]+[F(0)]); rr=[out(score(n,j,ss[j])-lams[j]*(3*n-1)-lv[n]) for n in range(m+2)]
     head=head_norm(rr,[z(n,1).b for n in range(m+2)])
     yt=z(start,1).b*((start+1)/(1-hr)+hr/(1-hr)**2)
     tailerr=(Ms[j]+3*abs(lams[j]))**2*yt
     epsj.append((head+tailerr)/ky)
    def form(v,w):
     a=v+[F(0)];b=w+[F(0)];ans=IV(0)
     for n in range(m+1):
      for j in range(2):ans=out(ans+h(n,j,ss[j])*(a[n]/z(n,j)-a[n+1]/z(n+1,j))*(b[n]/z(n,j)-b[n+1]/z(n+1,j)))
     return ans
    scores=[[score(n,j,ss[j]) for n in range(m+1)] for j in range(2)]
    tt=[[out(dot(scores[i],trials[j])+dot(scores[j],trials[i])-form(trials[i],trials[j])) for j in range(2)] for i in range(2)]
    delta=sum(epsj)
    S=[[out((ds[i] if i==j else IV(0))-tt[i][j]-(delta if i==j else 0)) for j in range(2)] for i in range(2)]
    margin=min(S[i][i].a-absiv(S[i][1-i]) for i in range(2))
    assert margin>F(1,3)
    assert epsj[0]>0 and epsj[1]>0
    assert 1-boxes[2].b>F(6534,100000) and 1-boxes[2].a<F(6536,100000)
    assert all(d.b<30 for d in ds)
    assert all(S[i][i].a-F(1,100)*ds[i].b>absiv(S[i][1-i]) for i in range(2))
    assert kappa>F(1,50)
    assert all(d.a>F(3,4) for d in ds)
    pair=lambda v:[str(v.a),str(v.b)]
    return dict(tail_K_lower=str(knlo),tail_K_upper=str(knhi),center_dual=str(dual(CENTER,u).a),upper=str(U),coordinate_boxes=[pair(v) for v in boxes],squeeze_boxes=[pair(v) for v in ss],
      uniform_gap=str(eps),kappa=str(kappa),kappa_y=str(ky),D=[pair(v) for v in ds],
      schur_lower=[[pair(v) for v in row] for row in S],margin=str(margin),
      contrast_multiplier_interval=[str(eta.a),str(eta.b)],eta='1/100',weight_growth='1/20000',squeeze_growth='3/1600',
      trial_support_last=m,trials=[list(map(str,v)) for v in trials],
      residual_squared_upper=list(map(str,epsj)),junction_included=m+1,tail_from=start,
      envelope_global=['e>=3/20','f_next>=f/9','f_next<=4*f/9'],
      envelope_tail='f_next<=f/4 for n>=2')

def exterior_certificate():
    prior_cert=inherited();U=F(prior_cert['feasible_energy_upper'])
    rects=partition(LEAF_KEYS);margins=[];chosen=[]
    for key,q in rects.items():
        candidates=[]
        for center,u in free_inputs(q,key):
            d0=dual(center,u).a;eta=dual_eta(center,u)
            margin=d0-taylor_loss((q[1]-q[0])/2,(q[3]-q[2])/2)-U-(upper_loss(EPSILON)+abs(contrast_shift(eta,EPSILON)))
            candidates.append((margin,eta))
        margin,eta=max(candidates,key=lambda pair:pair[0])
        assert margin>0,('uniform_exterior',key,str(margin))
        margins.append(margin);chosen.append(dict(key=key,eta=str(eta),margin=str(margin)))
    return dict(leaves=len(rects),minimum_margin=str(min(margins)),selected_slopes=chosen)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    constants=uniform_constants();assert all(constants['checks'].values()),constants
    faults={f:[k for k,v in uniform_constants(f)['checks'].items() if not v] for f in ['repair_sign','dual_sign','upper_loss']}
    assert all(faults.values()),faults
    # Production partition parser must reject a real missing branch, not a crash.
    partition(LEAF_KEYS)
    try:partition(LEAF_KEYS[1:])
    except AssertionError as exc:
        assert str(exc)=='missing exterior branch',str(exc)
        faults['missing_leaf']=[str(exc)]
    else:raise AssertionError('missing leaf accepted')
    basin=basin_certificate();ext=exterior_certificate()
    deps=['tests/channel-swings/k2219_detector_global_capture_probe.py','lab/process/k2219-detector-global-capture.json','tests/channel-swings/k2210_detector_stationary_certificate_probe.py','lab/process/k2210-detector-stationary-certificate.json','explorations/conditional-build/k2222-detector-contrast-continuation-2026-10-28.md']
    report=dict(result_id='K2222',status='conditional_uniform_unique_global_contrast_branch',epsilon=str(EPSILON),checks=constants['checks'],constants=constants,basin=basin,exterior=ext,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='New exact interval all-tail Schur and221 exterior margins; reused partition/free inputs/existence; written compactness and envelope-derivative proof. No infinite IFT or profile derivative.')
    target=ROOT/'lab/process/k2222-detector-contrast-continuation.json'
    if args.write:target.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(target.read_text())==report
    print(json.dumps(dict(result='K2222',controls=len(report['checks']),leaves=ext['leaves'],schur_margin=float(basin['margin'] and F(basin['margin'])),faults=faults)))
if __name__=='__main__':main()
