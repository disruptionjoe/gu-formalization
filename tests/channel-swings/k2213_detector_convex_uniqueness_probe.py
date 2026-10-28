#!/usr/bin/env python3
"""Uniform all-tail Schur consumer on an explicitly convex enclosure.
Reuses the unchanged boundary existence certificate, not its optimizer premise.
"""
import sys
sys.dont_write_bytecode=True
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from k2210_detector_stationary_certificate_probe import *
import k2210_detector_stationary_certificate_probe as old
ROOT=Path(__file__).resolve().parents[2]
def inherited():
    report=json.loads((ROOT/'lab/process/k2210-detector-stationary-certificate.json').read_text())
    assert hashlib.sha256((ROOT/'tests/channel-swings/k2210_detector_stationary_certificate_probe.py').read_bytes()).hexdigest()==report['probe_sha256']
    for p,h in report['dependency_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    return report['certificate']
def uniform_certificate():
    prior=inherited()
    ss=[IV(c-RADIUS,c+RADIUS) for c in CENTER]
    e,f,u=inputs(profile_at(F(0),F(0)),True)
    # Outward exported U is a valid inherited upper bound. Recompute fresh
    # slightly wider boxes and their entire residual certificate, so there is
    # no transfer of old bounds to an unjustified larger enclosure.
    U=F(prior['feasible_energy_upper']);eps=U-dual(ss,u).a
    assert 0<eps<F(1253,10**15)
    boxes=[prof.coordinate_box(n,u[0][n],u[1][n],eps,ss[0].a,ss[1].a) for n in range(7)]
    L=F(3,20);SIG=F(1,3);RHO=F(2,3)
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
    assert epsj[0]<F(812767,10**6) and epsj[1]<F(7597256,10**6)
    assert 1-boxes[2].b>F(6534,100000) and 1-boxes[2].a<F(6536,100000)
    assert all(d.b<30 for d in ds)
    assert all(S[i][i].a-F(1,100)*ds[i].b>absiv(S[i][1-i]) for i in range(2))
    assert kappa>F(1,50)
    assert all(d.a>F(3,4) for d in ds)
    pair=lambda v:[str(v.a),str(v.b)]
    return dict(coordinate_boxes=[pair(v) for v in boxes],squeeze_boxes=[pair(v) for v in ss],
      uniform_gap=str(eps),kappa=str(kappa),kappa_y=str(ky),D=[pair(v) for v in ds],
      schur_lower=[[pair(v) for v in row] for row in S],margin=str(margin),
      eta='1/100',weight_growth='1/20000',squeeze_growth='3/1600',
      trial_support_last=m,trials=[list(map(str,v)) for v in trials],
      residual_squared_upper=list(map(str,epsj)),junction_included=m+1,tail_from=start,
      envelope_global=['e>=3/20','f_next>=f/9','f_next<=4*f/9'],
      envelope_tail='f_next<=f/4 for n>=2')
def controls(fault=None):
    cs={}
    def ck(k,v):cs[k]=bool(v)
    # Linear inequalities, checked algebraically by coefficient identities.
    # Two endpoints and a rational convex weight exercise every boundary.
    for t in [F(0),F(1,3),F(1,2),F(1)]:
      for lo,hi in [(F(1,9),F(4,9)),(F(1,9),F(1,4))]:
       a,b=F(1,5),F(1,7);an,bn=lo*a,hi*b
       x=t*a+(1-t)*b;y=t*an+(1-t)*bn
       actual_hi=F(1,2) if fault=='unsquared_ratio' else hi
       ck(f'lower_{t}_{lo}_{hi}',y-lo*x==t*(an-lo*a)+(1-t)*(bn-lo*b) and y>=lo*x)
       ck(f'upper_{t}_{lo}_{hi}',actual_hi*x-y==t*(hi*a-an)+(1-t)*(hi*b-bn) and y<=hi*x)
    ck('D_x_bound',F(41,3)*F(9,160)>F(3,4))
    ck('D_y_bound',F(41,3)*F(3,10)>F(3,4))
    ck('hessian_weight',F(1,200)*F(1,50)==F(1,10000))
    factor=F(1) if fault=='missing_integration_half' else F(1,2)
    ck('integrated_weight',factor*F(1,10000)==F(1,20000))
    ck('integrated_squeeze',factor*F(3,800)==F(3,1600))
    # Different geometric complement rates obey the same ratio range yet
    # their mutual relative-cap distance is unbounded. This is a control,
    # not a claimed pair of exact-contrast optimizers.
    ck('different_tail_rates',F(1,9)<F(1,4) and F(1,4)<=F(4,9))
    for n in [1,4,12]:
      f=F(1,4)**n;g=F(1,9)**n
      ck('unbounded_cap_'+str(n),(f-g)/g==F(9,4)**n-1)
    # Segment cap bound holds without assuming mutually cap-close endpoints.
    for t in [F(1,100),F(1,2),F(99,100)]:
      for a,b in [(F(0),F(1)),(F(1,8),F(7,8)),(F(1,9),F(1,4))]:
       x=(1-t)*a+t*b;ck(f'segment_cap_{t}_{a}_{b}',abs(b-a)<=max(1/t,1/(1-t))*min(x,1-x))
    return cs
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    cs=controls();assert all(cs.values()),cs
    cert=uniform_certificate()
    faults={f:[k for k,v in controls(f).items() if not v] for f in ['unsquared_ratio','missing_integration_half']}
    assert all(faults.values())
    deps=['lab/process/k2210-detector-stationary-certificate.json','tests/channel-swings/k2210_detector_stationary_certificate_probe.py','explorations/conditional-build/k2204-detector-infinite-stability-certificate-2026-10-28.md','explorations/conditional-build/k2207-detector-nonlinear-stability-2026-10-28.md','explorations/conditional-build/k2213-detector-convex-uniqueness-2026-10-28.md']
    report=dict(result_id='K2213',status='unique_compact_box_minimizer_and_convex_envelope_growth',checks=cs,fault_failures=faults,certificate=cert,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='New universal convex-chord proof, fresh outward exact residual consumer on exported exact intervals, finite algebraic controls; unchanged boundary existence certificate reused by hashes, no global optimum claim.')
    dst=ROOT/'lab/process/k2213-detector-convex-uniqueness.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report,'report drift'
    print(json.dumps(dict(result='K2213',controls=len(cs),faults=len(faults),margin_float=float(F(cert['margin'])))))
if __name__=='__main__':main()
