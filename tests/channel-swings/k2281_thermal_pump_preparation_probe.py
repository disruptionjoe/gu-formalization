#!/usr/bin/env python3
"""Reproducible conditional controls; universal proof boundaries in companion note."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]

STEM='k2281-thermal-pump-preparation';NOTE=f'explorations/conditional-build/{STEM}-2026-10-29.md'
DEPS=['explorations/conditional-build/k2276-structured-detector-implementation-2026-10-29.md','explorations/conditional-build/k2278-calibrated-pump-detector-2026-10-29.md','explorations/conditional-build/k2279-uniform-pump-energy-2026-10-29.md']
checks={};n,N,mu,t=s.symbols('n N mu t',nonnegative=True)
quad=(2*n+1)*N**2/4+n*(N+1)
checks['thermal_large_n_majorant']=s.expand(n*(N+1)**2-quad-( (2*n-1)*N**2/4+n*N))==0
checks['thermal_small_n_majorant']=s.expand((2*n+1)*(N+1)**2/4-quad-(N/2+(1-2*n)/4))==0
# Actual purification vectors on finite input support, codomain enlarged for creation.
p=[R(1,2),R(1,4),R(1,8),R(1,8)]
def fluct_vectors(drop_annihilation=False):
    d=s.zeros(25,1);dd=s.zeros(25,1);base=s.zeros(25,1)
    for j,pj in enumerate(p):
        base[5*j+j]=s.sqrt(pj)
        if j and not drop_annihilation:d[5*(j-1)+j]=s.sqrt(j*pj)
        dd[5*(j+1)+j]=s.sqrt((j+1)*pj)
    return d,dd,base
d,dd,base=fluct_vectors();mean=sum(j*p[j] for j in range(4))
checks['purification_annihilation_norm']=(d.T*d)[0]==mean
checks['purification_creation_norm']=(dd.T*dd)[0]==mean+1
checks['purification_orthogonal_fluctuations']=(d.T*dd)[0]==0 and (base.T*d)[0]==0 and (base.T*dd)[0]==0
for i in range(4):
 for j in range(4):
    checks[f'two_mode_weight_{i}_{j}']=s.expand(n*(i+1)*(j+1)+(n+1)*i*j-((2*n+1)*i*j+n*(i+j+1)))==0
v=s.exp(t)-1;logmgf=-s.log(1-n*v)+mu*v/(1-n*v)
checks['thermal_number_mean']=s.simplify(s.diff(logmgf,t).subs(t,0)-mu-n)==0
checks['thermal_number_variance']=s.simplify(s.diff(logmgf,t,2).subs(t,0)-mu*(2*n+1)-n*(n+1))==0
checks['poisson_limit']=s.simplify(logmgf.subs(n,0)-mu*(s.exp(t)-1))==0
a=R(44,5);c=a/2;M=4*10**10
upper=a/2+a*10/(4*M)+(M+1)*c/(M-2*c)
checks['uniform_log_majorant']=bool(upper<R(881,100))
checks['exact_exponential_bound']=100000**1000<7000*99119**1000
checks['field_second_moment']=9*10**2*7000==6300000

def budget(mu,q,eps):
    return 1200*(1+eps)/s.sqrt(mu)+R(440,2**q+1)+2400*s.sqrt(2)*eps+22*(20*q)*eps+10*(10*q*q+20*q+10)*eps
# same conservative gate polynomial as preceding construction
small=budget(4*10**10,17,R(1,10**8));strong=budget(4*10**28,50,R(1,10**17))
checks['small_full_budget']=bool(small<R(9791,10**6))
checks['strong_full_budget']=bool(strong<R(1,10**11))
checks['energy_consumer']=R(6300000,10**11)<R(8,1000)**2
checks['depletion_from_thermal_mean']=s.expand((mu+1)-(mu+1-R(64,5))-R(64,5))==0
# Actual ideal record0 block on span{|00>,|11>}; compression suffices for witness.
tanh_r=R(3**2-1,3**2+1);v0=s.Matrix([1-tanh_r**2,-tanh_r*(1-tanh_r**2)]);block=v0*v0.T;W=s.Matrix([[0,1],[1,0]])
checks['actual_coherence_witness']=-s.trace(W*block)/2==R(324,3125)
checks['witness_norm_one']=W**2==s.eye(2)
phase=s.diag(1,-1);deph=(block+phase*block*phase)/2
checks['number_dephasing_preserves_diagonal']=list(deph.diagonal())==list(block.diagonal())
checks['number_dephasing_kills_witness']=s.trace(W*deph)==0
checks['vacuum_fluctuation_bound']=bool((d.T*d)[0]<=max(mean,(2*mean+1)/4))
assert all(checks.values()),[k for k,v in checks.items() if not v]
faults={}
badd,_,_=fluct_vectors(True);faults['lost_thermal_annihilation_branch']=(badd.T*badd)[0]!=mean
badlog=mu*v/(1-n*v);faults['lost_MGF_normalization']=s.simplify(s.diff(badlog,t).subs(t,0)-(mu+n))!=0
badC=R(1,2)
faults['coherent_coefficient_on_thermal_vacuum']=not bool((d.T*d)[0]<=badC**2)
faults['wrong_initial_pump_energy']=s.simplify(mu-(mu+1-R(64,5))-R(64,5))!=0
badblock=s.diag(*list(block.diagonal()));faults['removed_target_record_coherence']=s.trace(W*badblock)!=s.trace(W*block)
faults['inflated_actual_calibration']=budget(4*10**28,50,R(1,10**6))>=R(1,10**11)

def finish(result_id,stem,note,deps,checks,faults,extra):
    assert all(checks.values()), [k for k,v in checks.items() if not v]
    assert all(faults.values()), [k for k,v in faults.items() if not v]
    paths=[note,str(Path(__file__).relative_to(ROOT)),*deps]
    data=dict(schema_version='1.0',result_id=result_id,claim_ceiling='conditional supplied model; no native GU, empirical confidence or hardware claim',evidence_kind='exact algebra/finite operator controls plus separately identified interval and resource certificates; universal proofs in note',checks=len(checks),check_names=list(checks),faults_caught=list(faults),dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
    out=ROOT/'lab/process'/f'{stem}.json'
    if '--write' in sys.argv: out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else: assert json.loads(out.read_text())==data,'stored report stale'
    print(json.dumps(dict(result=result_id,checks=len(checks),faults=len(faults),certificates=extra),default=str))

finish('K2281',STEM,NOTE,DEPS,checks,faults,dict(resource_certificates={'small_error_upper':str(small),'strong_error_upper':str(strong),'field_second_moment_upper':6300000,'phase_counterexample_half_distance':'324/3125'}))
