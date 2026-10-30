"""Exact local identities plus labeled finite numerical compiler controls.
Universal reachability and exposure use the written proof, not sampled N.
"""
from pathlib import Path
import json,hashlib,sys
import sympy as s
import mpmath as mp
ROOT=Path(__file__).resolve().parents[2]
mp.mp.dps=160

def compile_target(target,gamma,J=mp.mpf(1),fault=None):
    N=len(target)-1; v=mp.matrix(target); pulses=[]; residuals=[]
    nu=mp.sqrt(J*J-gamma*gamma/16)
    for k in range(N,0,-1):
        x,y=v[k-1],v[k]
        numerator=nu*y;denominator=J*x-gamma*y/4
        angle=mp.atan(numerator/denominator) if fault=='atan_wrong_branch' else mp.atan2(numerator,denominator)
        t=angle/nu
        B=mp.zeros(N+1);B[k-1,k]=J;B[k,k-1]=-J
        G=B+mp.diag([gamma*j/2 for j in range(N+1)])
        if fault=='omit_spectator_filter':
            for j in range(k-1):G[j,j]=0
        v=mp.expm(G*t)*v
        # Check before projecting an analytically zero component; later anti-loss
        # would exponentially amplify roundoff in already eliminated levels.
        residuals.append(abs(v[k])/mp.norm(v))
        v[k]=0
        pulses.append((k,t));
    out=mp.zeros(N+1,1);out[0]=1
    order=pulses if fault=='wrong_pulse_order' else list(reversed(pulses))
    for k,t in order:
        B=mp.zeros(N+1);B[k-1,k]=J;B[k,k-1]=-J
        G=(-B if fault!='wrong_control_sign' else B)-mp.diag([gamma*j/(1 if fault=='double_loss' else 2) for j in range(N+1)])
        out=mp.expm(G*t)*out
    return v,out,pulses,residuals

def evaluate(fault=None):
    exact={};numeric={}
    def ck(name,v):exact[name]=bool(v)
    def nk(name,v):numeric[name]=bool(v)
    J,g,k,t=s.symbols('J g k t',positive=True);u=s.symbols('u',real=True)
    C=s.Matrix([[-g/4,J],[-J,g/4]])
    ck('centered_square',C*C==-(J*J-g*g/16)*s.eye(2))
    vec=s.Matrix([s.cos(u),s.sin(u)]);raw=s.Matrix([[0,J],[-J,0]])*vec+s.diag(g*(k-1)/2,g*k/2)*vec
    ang=s.simplify(-s.sin(u)*raw[0]+s.cos(u)*raw[1])
    pred=-J+(g/(2 if fault=='angle_loss_factor' else 4))*s.sin(2*u)
    ck('backward_angle',s.simplify(ang-pred)==0)
    q,mu=s.symbols('q mu',positive=True)
    qdot=-g*mu*q*(1-q);ck('tail_loss',s.simplify(qdot.subs(q,s.sin(u)**2)/(2*s.sin(u)*s.cos(u))+g*mu*s.sin(2*u)/4)==0)
    ck('critical_quadratic_zero',s.limit((1-s.sin(2*u))/(u-s.pi/4)**2,u,s.pi/4)==2)
    ck('exposure_symmetry',s.simplify(s.sin(u)**2+s.sin(s.pi/2-u)**2)==1)
    N=s.symbols('N',integer=True,positive=True)
    ck('sum_stage_exposure',s.summation(k-s.Rational(1,2),(k,1,N))==N*N/2)
    L=s.symbols('L',positive=True)
    rate=4*L/(s.pi*N*N+L)
    ck('sufficient_rate',s.simplify(rate*s.pi*N*N/(4-rate)-L)==0)
    tau,gamma,norm=s.symbols('tau gamma norm',positive=True)
    ck('renewal_charge',s.simplify((2 if fault!='omit_charge_two' else 1)*L/norm-2*L/norm)==0)
    for NN in [1,2,3,4]:
        a=s.pi/(NN+2);cs=[s.sqrt(s.Rational(2,NN+2))*s.sin((j+1)*a) for j in range(NN+1)]
        ck('sine_norm_'+str(NN),s.trigsimp(sum(x*x for x in cs))==1)
        ck('sine_mean_'+str(NN),s.simplify(sum(j*x*x for j,x in enumerate(cs))-s.Rational(NN,2))==0)
    # Independent full matrix exponentials test the explicit timing recurrence.
    for NN,gg in [(1,'0'),(2,'.4'),(3,'2.4'),(5,'3.9')]:
        gam=mp.mpf(gg);tar=mp.matrix([mp.sqrt(mp.mpf(2)/(NN+2))*mp.sin((j+1)*mp.pi/(NN+2)) for j in range(NN+1)])
        back,out,pulses,residuals=compile_target(tar,gam,fault=fault)
        normout=mp.norm(out);p=normout**2
        nk(f'endpoint_N{NN}_g{gg}',mp.norm(out/normout-tar)<mp.mpf('1e-48'))
        nk(f'inverse_N{NN}_g{gg}',mp.norm(out-tar/back[0])/mp.norm(out)<mp.mpf('1e-48'))
        nk(f'positive_times_N{NN}_g{gg}',all(tt>=0 for _,tt in pulses))
        nk(f'elimination_residual_N{NN}_g{gg}',max(residuals)<mp.mpf('1e-48'))
        taumax=(mp.pi/2+mp.asin(gam/4))/mp.sqrt(1-gam*gam/16)
        nk(f'time_bound_N{NN}_g{gg}',sum(tt for _,tt in pulses)<=NN*taumax+mp.mpf('1e-45'))
        nk(f'survival_bound_N{NN}_g{gg}',mp.log(p)>=-gam*NN*NN*taumax/2-mp.mpf('1e-48') and mp.log(p)<=mp.mpf('1e-48'))
    # Lost preparation survivors must be pretilted for known later storage.
    NN=3;gam=mp.mpf('.7');storage=mp.mpf('.6')
    tar=mp.matrix([mp.sqrt(mp.mpf(2)/(NN+2))*mp.sin((j+1)*mp.pi/(NN+2)) for j in range(NN+1)])
    tilt=mp.matrix([tar[j]*mp.exp(gam*j*storage/2) for j in range(NN+1)]);Z=mp.norm(tilt);tilt/=Z
    b,o,_,_=compile_target(tar if fault=='omit_storage_pretilt' else tilt,gam)
    final=mp.diag([mp.exp(-gam*j*storage/2) for j in range(NN+1)])*o
    nk('storage_endpoint',mp.norm(final/mp.norm(final)-tar)<mp.mpf('1e-48'))
    nk('storage_probability',abs(mp.norm(final)**2-mp.norm(o)**2/(Z*Z))<mp.mpf('1e-48'))
    # Reference corruption demonstrates that normalized success alone cannot erase failures.
    p=s.Rational(171,172);p0=s.Rational(43,45)
    ck('all_launch_probability',(p if fault!='discard_failures' else 1)*p0==s.Rational(19,20))
    return exact,numeric

base=evaluate();assert all(all(d.values()) for d in base),base
faults={}
for name in ['atan_wrong_branch','omit_spectator_filter','wrong_pulse_order','wrong_control_sign','double_loss','angle_loss_factor','omit_charge_two','omit_storage_pretilt','discard_failures']:
    e,n=evaluate(name);bad=[k for d in (e,n) for k,v in d.items() if not v];assert bad,'undetected '+name;faults[name]=bad
stem='k2322-protected-reference-compiler';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)), 'explorations/conditional-build/k2320-lossy-selective-calibration-2026-10-30.md','explorations/conditional-build/k2312-relational-finite-calibration-2026-10-30.md']
data=dict(schema_version='1.0',result_id='K2322',checks=sum(map(len,base)),exact_check_names=list(base[0]),numerical_check_names=list(base[1]),mutation_failed_checks=faults,evidence_kind='exact local symbolic identities; 160-digit finite matrix controls are numerical evidence only; universal arbitrary-stock/control-class proof in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'reachability':'gamma<4J iff finite-time exact sine target','exposure_upper':'N**2*tau_max/2','exposure_lower':'N**2/(8*J)','full_instrument':'immediate flag and instantaneous ideal subsequent instrument, or separately compensated pure-loss storage with final flag'})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps({'result':'K2322','exact':len(base[0]),'numerical':len(base[1]),'faults':len(faults)}))
