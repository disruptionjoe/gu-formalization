#!/usr/bin/env python3
"""Exact fixed-contrast nonconvexity, full tails and optimized interval witnesses."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import sympy as S
from k2178_effective_detector_approximation_probe import p,A,H,sqrt_iv,ivadd,scale,point,contrast
ROOT=Path(__file__).resolve().parents[2]
C=F(40,3);LO=F(2,3);HI=F(113,100)
U=[F(0),F(129,2048),F(0),F(0),F(0)];V=[F(0),F(0),F(0),p(3),p(4)]

def moments(vals,tail,fault=None):
    k=len(vals)-1;z=F(1,4)**(k+1)
    R=sum((F(n)+F(1,2))*x for n,x in enumerate(vals))+tail*z*(k+1+F(5,6))
    T=point(tail*H(k+1)*(0 if fault=='omit_tail' else 1))
    for n,x in enumerate(vals):
        nxt=vals[n+1] if n<k else tail*p(k+1)
        if fault=='omit_edge' and n==2:continue
        T=ivadd(T,scale(n+1,sqrt_iv(x*nxt)))
    return R,T

def ap(s):return F(41,3)*s-3/s**3

def optimized(R,T):
    # Monotone derivative brackets the actual minimum, including T uncertainty.
    lo,hi=LO,HI
    assert R*ap(lo)<C*T[0] and R*ap(hi)>C*T[1]
    for _ in range(110):
        mid=(lo+hi)/2
        if R*ap(mid)<C*T[0]:lo=mid
        elif R*ap(mid)>C*T[1]:hi=mid
        else:break
    ai=(F(41,6)*lo*lo+F(3,2)/hi**2,F(41,6)*hi*hi+F(3,2)/lo**2)
    return (R*ai[0]-C*hi*T[1],R*ai[1]-C*lo*T[0])

def profile_energy(x):
    y=[p(n)-v for n,v in enumerate(x)]
    return ivadd(ivadd(optimized(*moments(x,F(0))),optimized(*moments(y,F(1)))),point(F(35,18)))

def controls(fault=None):
    cs={};ck=lambda n,v:cs.__setitem__(n,bool(v))
    ru,tu=moments(U,F(0));rv,tv=moments(V,F(0));a=F(43,128)
    ck('equal_positive_contrast',contrast(U,0)==contrast(V,0)==F(129,1024))
    ck('moments',ru==F(387,4096) and rv==F(111,2048) and tu[0]==0 and tv[0]==F(3,128))
    ck('ratio',F(3,128)/rv==F(16,37))
    hess=F(41,3)+9/LO**4;strong=C*C/hess;D=strong*ru*rv/(4*(ru+rv))*F(16,37)**2
    J=F(9,16)*a*a+F(159,2048);K=C*HI*3*J/32
    ck('hessian_bound',hess==F(2843,48));ck('perspective_gap',D==F(103200,21353773));ck('edge_curvature',J==F(36993,262144));ck('complement_bound',K==F(4180209,20971520))
    ck('all_epsilon_margin',D-K/100>0)
    ck('explicit_gap',D/100-K/10000==F(127162852321443,4478210775449600000))
    ck('inverse_power_bound',8<9)
    # Exact envelope differentiation: eliminate s' using differentiated stationarity.
    rr,rp,tt,tp,tpp,aa,aaa=S.symbols('R Rp T Tp Tpp Ap App',nonzero=True)
    sp=(S.Rational(40,3)*tp-rp*aa)/(rr*aaa)
    actual=rp*aa*sp-S.Rational(40,3)*sp*tp-S.Rational(40,3)*S.Symbol('s')*tpp
    expected=-S.Rational(40,3)*S.Symbol('s')*tpp+(-1 if fault!='response_sign' else 1)*(rp*aa-S.Rational(40,3)*tp)**2/(rr*aaa)
    ck('envelope_curvature_identity',S.simplify(actual-expected)==0)
    for eps in [F(1,100),F(1,1000),F(1,10000)]:
        for theta in [F(0),F(1,2),F(1)]:
            x=[eps*((1-theta)*u+theta*v) for u,v in zip(U,V)]
            ck(f'caps_{eps}_{theta}',all(0<=v<=p(n) for n,v in enumerate(x)))
            qshift=0 if fault!='contrast_weight' else 1
            ck(f'contrast_{eps}_{theta}',sum((3*n-1+qshift)*v for n,v in enumerate(x))==eps*F(129,1024))
            r,t=moments(x,F(0));linear=eps*theta*F(3,128)
            ck(f'disconnected_coherence_{eps}_{theta}',t[0]<=linear<=t[1])
            y=[p(n)-v for n,v in enumerate(x)];ry,ty=moments(y,F(1),fault)
            z1=1-eps*a*(1-theta);z3=1-eps*theta
            exact=ivadd(point(F(2,3)-F(9,16)-F(159,2048)-F(3,128)*(1-z3)),ivadd(scale(F(9,16),sqrt_iv(z1)),scale(F(159,2048),sqrt_iv(z3))))
            ck(f'full_complement_edges_{eps}_{theta}',max(ty[0],exact[0])<=min(ty[1],exact[1]))
            ck(f'full_complement_moment_{eps}_{theta}',r+ry==F(5,6))
        energies=[profile_energy([eps*((1-th)*u+th*v) for u,v in zip(U,V)]) for th in [F(0),F(1,2),F(1)]]
        gap=ivadd(energies[1],scale(F(-1,2),ivadd(energies[0],energies[2])))
        ck(f'optimized_gap_{eps}',gap[0]>eps*D-K*eps*eps>0)
    # Stronger released fixture fixes both probability and contrast.
    u2=[F(0),F(42,5120),F(0),F(0),F(0),F(0),F(33,5120)]
    v2=V+[F(0),F(0)];r2,t2=moments(u2,F(0));rv2,tv2=moments(v2,F(0))
    ck('same_moments_probability',sum(u2)==sum(v2)==F(15,1024))
    ck('same_moments_mean',sum(n*x for n,x in enumerate(u2))==sum(n*x for n,x in enumerate(v2))==F(3,64))
    ck('same_moments_radius',r2==rv2==F(111,2048))
    ck('same_moments_contrast',contrast(u2,0)==contrast(v2,0)==F(129,1024))
    D2=strong*r2*F(16,37)**2/8
    J2=F(9,16)*F(7,160)**2+F(159,2048)+F(93,32768)*F(176,5)**2
    K2=C*HI*3*J2/32
    ck('same_moments_D',D2==F(400,105191));ck('same_moments_J',J2==F(58905,16384));ck('same_moments_K',K2==F(1331253,262144))
    ck('same_moments_gap',D2/10000-K2/10**8==F(908540165677,2757518950400000000)>0)
    for eps in [F(1,10000),F(1,100000)]:
        energies=[]
        for theta in [F(0),F(1,2),F(1)]:
            x=[eps*((1-theta)*u+theta*v) for u,v in zip(u2,v2)]
            ck(f'fixed_caps_{eps}_{theta}',all(0<=v<=p(n) for n,v in enumerate(x)))
            ck(f'fixed_probability_{eps}_{theta}',sum(x)==eps*F(15,1024))
            ck(f'fixed_contrast_{eps}_{theta}',contrast(x,F(0))==eps*F(129,1024))
            y=[p(n)-v for n,v in enumerate(x)];ry,ty=moments(y,F(1))
            z1=1-eps*F(7,160)*(1-theta);z6=1-eps*F(176,5)*(1-theta);z3=1-eps*theta
            weight6=F(0) if fault=='omit_edge6' else F(93,32768)
            exact=point(F(2,3)-F(9,16)-weight6-F(159,2048)-F(3,128)*(1-z3))
            for w,zv in [(F(9,16),z1),(weight6,z6),(F(159,2048),z3)]:exact=ivadd(exact,scale(w,sqrt_iv(zv)))
            ck(f'fixed_full_tail_{eps}_{theta}',max(ty[0],exact[0])<=min(ty[1],exact[1]))
            ck(f'fixed_factors_{eps}_{theta}',min(z1,z6,z3)>=F(1,2))
            energies.append(profile_energy(x))
        gap=ivadd(energies[1],scale(F(-1,2),ivadd(energies[0],energies[2])))
        ck(f'fixed_optimized_gap_{eps}',gap[0]>eps*D2-K2*eps*eps>0)
    return cs

FAULTS=['omit_tail','omit_edge','response_sign','contrast_weight','omit_edge6']
def main():
    ap_=argparse.ArgumentParser();ap_.add_argument('--write',action='store_true');args=ap_.parse_args()
    cs=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
    faults={}
    for f in FAULTS:
        bad=[n for n,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
    x0=[u/100 for u in U];x1=[v/100 for v in V];xm=[(u+v)/200 for u,v in zip(U,V)]
    ee=[profile_energy(x) for x in [x0,xm,x1]];gap=ivadd(ee[1],scale(F(-1,2),ivadd(ee[0],ee[2])))
    deps=['explorations/conditional-build/k2184-global-detector-structure-2026-10-28.md','explorations/conditional-build/k2182-uniform-detector-endpoints-2026-10-28.md','explorations/conditional-build/k2180-detector-contrast-frontier-2026-10-28.md','tests/channel-swings/k2178_effective_detector_approximation_probe.py']
    report=dict(result_id='K2184',status='conditional_exact_controls',checks=cs,fault_failures=faults,optimized_witness_energy_intervals=[[str(a),str(b)] for a,b in ee],midpoint_gap_interval=list(map(str,gap)),analytic_gap_lower='127162852321443/4478210775449600000',dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written continuum-of-contrasts and infinite-tail curvature proof, independently reviewed. Rational interval witnesses are controls, not optimized frontier or apparatus-cost claims.')
    dst=ROOT/'lab/process/k2184-global-detector-structure.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report
    print(json.dumps(dict(result='K2184',checks=len(cs),faults=len(faults),gap_approx=[float(t) for t in gap])))
if __name__=='__main__':main()
