#!/usr/bin/env python3
"""Reproducible conditional controls; universal proof boundaries in companion note."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]

from math import isqrt
STEM='k2282-centered-positive-control';NOTE=f'explorations/conditional-build/{STEM}-2026-10-29.md'
DEPS=['explorations/conditional-build/k2276-structured-detector-implementation-2026-10-29.md','explorations/conditional-build/k2278-calibrated-pump-detector-2026-10-29.md','explorations/conditional-build/k2279-uniform-pump-energy-2026-10-29.md']
checks={}
mu,delta,k=s.symbols('mu delta k',positive=True)
def poisson(poly):
    out=0
    for (power,),coef in s.Poly(s.expand(poly),k).terms():
        out+=coef*sum(s.functions.combinatorial.numbers.stirling(power,j,kind=2)*mu**j for j in range(power+1))
    return s.expand(out)
C=(2*(k-mu)+delta)**2
variance=s.expand(poisson(C*C)-poisson(C)**2)
checks['centered_poisson_variance']=s.expand(variance-16*(2*mu**2+mu*(delta+1)**2))==0
checks['skewness_optimal_center']=s.diff(variance,delta).subs(delta,-1)==0 and s.diff(variance,delta,2)==32*mu
checks['vacuum_centered_mean']=poisson(C).subs(delta,-1)==4*mu+1
w=s.symbols('w',positive=True)
checks['universal_majorant_stationary']=s.diff(s.sqrt(2)*w**R(3,2)-w*w,w).subs(w,R(9,8))==0
checks['universal_majorant_peak']=(s.sqrt(2)*w**R(3,2)-w*w).subs(w,R(9,8))==R(27,64)
# Actual finite-shell trilinear matrices, including all pump-vacuum boundaries.
def shell(t,z=s.Integer(2),m=3,shift=True,weight=2):
    basis=[(i,j,l) for l in range(t//2+1) for i in range(t-2*l+1) for j in [t-2*l-i]]
    H=s.zeros(len(basis));index={v:i for i,v in enumerate(basis)}
    for col,(i,j,l) in enumerate(basis):
        if l and (i+1,j+1,l-1) in index:
            row=index[(i+1,j+1,l-1)];H[row,col]=s.I*z*s.sqrt((i+1)*(j+1)*l);H[col,row]=s.conjugate(H[row,col])
    h=isqrt(m+2);h+=h*h<m+2;d=2*h*(m+2)+1
    B=H+(4*((t-m)**2+d) if shift else 0)*s.eye(len(basis))
    Q=s.diag(*[i+j+weight*l for i,j,l in basis])
    return H,B,Q
for t in range(9):
 H,B,Q=shell(t)
 checks[f'Hermitian_shell_{t}']=H==H.conjugate().T
 checks[f'charge_shell_{t}']=Q*H==H*Q
 # strictly diagonal dominant Hermitian => positive definite; exact finite control
 checks[f'positive_shell_{t}']=all(bool(B[i,i]>sum(s.Abs(B[i,j]) for j in range(B.cols) if j!=i)) for i in range(B.rows))
for m in range(4):checks[f'integer_periodicity_{m}']=all(s.exp(-2*s.pi*s.I*(t-m)**2)==1 for t in range(8))
M=10**28;m=2*M+1;h=isqrt(m+2);h+=h*h<m+2
checks['exact_large_integer_center']=h*h>=m+2 and (h-1)**2<m+2
base=R(600)*(1+R(1,10**17))/10**14+R(440,2**50+1)+3600*R(1,10**17)+22*1000*R(1,10**17)+260100*R(1,10**17)
extra=6*M*R(1,10**42)+2*10**14*R(1,10**28) # sqrt32<6
checks['total_centered_instrument_budget']=bool(base+extra<R(1,10**11))
checks['positive_compensator_area']=R(80)*R(11,10)/10**14<6 # 2pi>6
checks['scalar_positivity_offset']=s.expand((w-s.symbols('eta')/(2*s.symbols('aa')))**2*s.symbols('aa')-(s.symbols('aa')*w*w-s.symbols('eta')*w+s.symbols('eta')**2/(4*s.symbols('aa'))))==0
q,eps,estimate,center=s.symbols('q eps estimate center')
residual=eps*(q+2)**2-2*(center+2)*estimate*q
expected=eps*(q-center)**2+2*(center+2)*(eps-estimate)*q+eps*(4-center**2)
checks['old_error_estimation_decomposition']=s.expand(residual-expected)==0
shift=s.symbols('shift')
checks['center_error_linear_transport']=s.expand((q-center-shift)**2-(q-center)**2+2*shift*q-2*center*shift-shift**2)==0
assert all(checks.values()),[k for k,v in checks.items() if not v]
faults={}
H,B,Q=shell(4,shift=False);faults['missing_positive_shift']=not all(bool(B[i,i]>sum(s.Abs(B[i,j]) for j in range(B.cols) if j!=i)) for i in range(B.rows))
H,B,Q=shell(4,weight=1);faults['wrong_conserved_charge_weight']=Q*H!=H*Q
faults['lost_poisson_skewness']=s.expand(variance-16*(2*mu**2+mu*delta**2))!=0
faults['noninteger_center_breaks_periodicity']=s.exp(-2*s.pi*s.I*(R(1,3))**2)!=1
faults['uncentered_residual_substitution']=s.expand(poisson((2*k+2)**4)-poisson((2*k+2)**2)**2-32*mu**2)!=0
faults['inflated_centered_area_error']=base+6*M*R(1,10**30)>=R(1,10**11)

def finish(result_id,stem,note,deps,checks,faults,extra):
    assert all(checks.values()), [k for k,v in checks.items() if not v]
    assert all(faults.values()), [k for k,v in faults.items() if not v]
    paths=[note,str(Path(__file__).relative_to(ROOT)),*deps]
    data=dict(schema_version='1.0',result_id=result_id,claim_ceiling='conditional supplied model; no native GU, empirical confidence or hardware claim',evidence_kind='exact algebra/finite operator controls plus separately identified interval and resource certificates; universal proofs in note',checks=len(checks),check_names=list(checks),faults_caught=list(faults),dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
    out=ROOT/'lab/process'/f'{stem}.json'
    if '--write' in sys.argv: out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else: assert json.loads(out.read_text())==data,'stored report stale'
    print(json.dumps(dict(result=result_id,checks=len(checks),faults=len(faults),certificates=extra),default=str))

finish('K2282',STEM,NOTE,DEPS,checks,faults,dict(resource_certificates={'core_error_upper':str(base),'additional_phase_upper':str(extra),'full_error_upper':str(base+extra),'center':str(m),'ceil_sqrt_center_plus_two':str(h),'positive_pump_pulses':20,'positive_compensators':1}))
