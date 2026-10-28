#!/usr/bin/env python3
"""Exact full-tail noise counterexample, optimized interval consumer and faults."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import sympy as S
from k2184_global_detector_structure_probe import moments,optimized,ap,C,HI,LO
from k2178_effective_detector_approximation_probe import p,A,sqrt_iv,ivadd,scale,point,contrast
ROOT=Path(__file__).resolve().parents[2]
RP=F(5,6);TP=F(2,3)
def Ep(s):return RP*A(s)-C*s*TP+F(35,18)
def data(N,fault=None):
    r=F(1,2**N);L=r*r/(1+r*r);U=1/(1+r*r);tau=F(1,4)**(N+1)
    edge=F(N+1)*p(N)/2;rt=tau*(N+F(11,6));tt=tau*(F(N,2)+(F(2,3) if fault=='tail_offset' else F(7,6)))
    cross=r/(1+r*r)*edge*(0 if fault=='interface' else 1)
    rz=L*(RP-rt)+U*rt;tz=L*(TP-edge-tt)+cross+U*tt;ty=U*(TP-edge-tt)+cross+L*tt
    delta=edge*(r+1/r-2)/2;hu=C*edge*(1-r)**2/(1+r*r)
    return dict(N=N,r=r,L=L,U=U,Rz=rz,Tz=tz,Ty=ty,delta=delta,Hu=hu,d=(U-L)*3*(N+1)*tau)
def energy(N,L,U):
    rx,tx=moments([L*p(n) for n in range(N+1)],U)
    ry,ty=moments([(1-L)*p(n) for n in range(N+1)],1-U)
    return ivadd(ivadd(optimized(rx,tx),optimized(ry,ty)),point(F(35,18)))
def derivative_p(N,L,U):
    # Independent finite changed-edge plus exact geometric untouched tail.
    vals=[L*p(n) for n in range(N+1)]+[U*p(N+1)]
    total=point(F(0))
    for n in range(N+1):
        ratio=sqrt_iv(vals[n+1]/vals[n]);term=ivadd(ratio,(1/(4*ratio[1]),1/(4*ratio[0])))
        total=ivadd(total,scale(F(n+1)*p(n)/2,term))
    tau=F(1,4)**(N+1);tail=F(1,2)*tau*(N+F(7,3))
    return ivadd(total,point(tail))
def controls(fault=None):
    cs={};ck=lambda n,v:cs.__setitem__(n,bool(v))
    s=S.symbols('s',positive=True);aa=S.Rational(41,6)*s*s+S.Rational(3,2)/s**2
    ep=S.Rational(5,6)*aa-S.Rational(80,9)*s+S.Rational(35,18)
    ck('Ep_zero',ep.subs(s,1)==0 and S.diff(ep,s).subs(s,1)==0)
    ck('Ep_strict_convexity',S.simplify(S.diff(ep,s,2)-S.Rational(5,6)*(S.Rational(41,3)+9/s**4))==0)
    # Derive the optimized directional identity from two homogeneous branches.
    beta,sz,sy,dz,dy,gz,gy,az,ay=S.symbols('beta sz sy dz dy gz gy Az Ay')
    raw=beta*(S.Rational(5,6)*az-S.Rational(40,3)*sz*dz)+(1-beta)*(S.Rational(5,6)*ay-S.Rational(40,3)*sy*dy)-gz-gy
    term=(beta if fault!='noise_bias' else 1-beta)*(S.Rational(5,6)*az-S.Rational(80,9)*sz+S.Rational(35,18))+(1-beta)*(S.Rational(5,6)*ay-S.Rational(80,9)*sy+S.Rational(35,18))-S.Rational(40,3)*(beta*sz*(dz-S.Rational(2,3))+(1-beta)*sy*(dy-S.Rational(2,3)))-(gz+gy+S.Rational(35,18))
    ck('noise_derivative_identity',S.expand(raw-term)==0)
    for N in [3,6,10,12]:
        d=data(N,fault);L,U=d['L'],d['U']
        ck(f'positive_caps_{N}',0<L<U<1 and L+U==1)
        rx,tx=moments([L*p(n) for n in range(N+1)],U);ry,ty=moments([U*p(n) for n in range(N+1)],L)
        ck(f'exact_R_{N}',rx==d['Rz'] and rx+ry==RP)
        ck(f'full_Tz_{N}',tx[0]<=d['Tz']<=tx[1]);ck(f'full_Ty_{N}',ty[0]<=d['Ty']<=ty[1])
        for label,l,u in [('z',L,U),('y',U,L)]:
            dp=derivative_p(N,l,u);ck(f'tangent_p_{label}_{N}',dp[0]<=TP+d['delta']<=dp[1])
        ck(f'interface_energy_{N}',C*(TP-d['Tz']-d['Ty'])==d['Hu'])
        direct=sum((3*n-(0 if fault=='contrast_weight' else 1))*L*p(n) for n in range(N+1))+U*3*(N+1)*F(1,4)**(N+1)
        ck(f'contrast_full_tail_{N}',direct==d['d'])
    d=data(10,fault);L,U=d['L'],d['U']
    ck('N10_radius',d['Rz']==F(95420345,26388304232448));ck('N10_coherence',d['Tz']==F(6959471,3298538029056))
    ck('N10_contrast',d['d']==F(34602975,4398050705408));ck('N10_delta',d['delta']==F(34535457,17179869184))
    ck('N10_Hupper',d['Hu']==F(57559095,1099512676352))
    station=ap(F(9,10))-C*d['Tz']/d['Rz']
    if fault=='stationarity_sign':station=ap(F(9,10))+C*d['Tz']/d['Rz']
    ck('squeeze_bracket',station==F(18784071701,46374287670)>0)
    ck('Ep_ninetenths',Ep(F(9,10))==F(649,6480))
    bound=Ep(F(9,10))/2-C*HI*d['delta']-d['Hu']
    ck('fair_derivative_lower',bound==F(72000341772103349,3647919177093611520)>F(1,64))
    # Actual infinite-tail optimized energies, rather than the upper estimate alone.
    e0=energy(10,L,U);t=F(1,10**8);beta=F(1,2);lnew=(1-t)*L+t*beta;unew=(1-t)*U+t*beta
    en=energy(10,lnew,unew);gap=ivadd(en,scale(-1,e0))
    ck('initial_energy_positive',e0[0]>F(1,20000));ck('optimized_upper',e0[1]<d['Hu'])
    ck('finite_noise_energy_increases',gap[0]>0)
    ck('finite_noise_contrast_decreases',contrast([lnew*p(n) for n in range(11)],unew)==(1-t)*d['d']<d['d'])
    end=energy(10,F(1,2),F(1,2));ck('fair_endpoint_zero',end[0]<=0<=end[1] and end[1]-end[0]<F(1,10**25))
    ck('finite_quasiconvexity_failure',en[0]>e0[1]>end[1])
    # Asymptotics are a written limit proof; these are exact scaled formula controls.
    for N in [10,20,40]:
        dd=data(N);ck(f'scaled_radii_{N}',F(1,4)<dd['Rz']/(N*F(1,4)**N)<F(1,2))
        ck(f'scaled_coherence_{N}',F(1,8)<dd['Tz']/(N*F(1,4)**N)<F(1,4))
    return cs,dict(initial_energy=e0,noisy_energy=en,finite_gap=gap,derivative_lower=bound,noise_t=t)
FAULTS=['tail_offset','interface','noise_bias','contrast_weight','stationarity_sign']
def main():
    ap_=argparse.ArgumentParser();ap_.add_argument('--write',action='store_true');args=ap_.parse_args()
    cs,w=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
    faults={}
    for fault in FAULTS:
        bad=[n for n,v in controls(fault)[0].items() if not v];assert bad,('undetected',fault);faults[fault]=bad
    deps=['explorations/conditional-build/k2186-detector-contrast-descent-2026-10-28.md','explorations/conditional-build/k2184-global-detector-structure-2026-10-28.md','explorations/conditional-build/k2180-detector-contrast-frontier-2026-10-28.md','tests/channel-swings/k2184_global_detector_structure_probe.py','tests/channel-swings/k2178_effective_detector_approximation_probe.py']
    report=dict(result_id='K2186',status='conditional_exact_controls',checks=cs,fault_failures=faults,witness={k:list(map(str,v)) if isinstance(v,tuple) else str(v) for k,v in w.items()},dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written full-tail derivative and fixed-beta limit proof; rational finite counterexample and optimized intervals. No frontier monotonicity, optimizer uniqueness or apparatus accounting claim.')
    dst=ROOT/'lab/process/k2186-detector-contrast-descent.json'
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dst.read_text())==report
    print(json.dumps(dict(result='K2186',checks=len(cs),faults=len(faults),finite_gap=[float(x) for x in w['finite_gap']])))
if __name__=='__main__':main()
