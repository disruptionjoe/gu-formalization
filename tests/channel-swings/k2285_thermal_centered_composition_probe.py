#!/usr/bin/env python3
"""Exact controls and separately typed certificates; universal proofs in companion note."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
checks={}
STEM='k2285-thermal-centered-composition'
NOTE=f'explorations/conditional-build/{STEM}-2026-10-30.md'
DEPS=['explorations/conditional-build/k2281-thermal-pump-preparation-2026-10-29.md', 'explorations/conditional-build/k2282-centered-positive-control-2026-10-29.md', 'explorations/conditional-build/k2279-uniform-pump-energy-2026-10-29.md','explorations/conditional-build/k2273-positive-control-energy-2026-10-29.md']

mu,n,t,dd=s.symbols('mu n t dd',positive=True)
v=s.exp(t)-1;cg=-s.log(1-n*v)+mu*v/(1-n*v)
cumulants=[s.expand(s.diff(cg,t,j).subs(t,0)) for j in range(1,5)]
k1,k2,k3,k4=cumulants
expected=[mu+n,mu*(1+2*n)+n*(n+1),mu*(1+6*n+6*n*n)+n*(n+1)*(2*n+1),mu*(1+14*n+36*n*n+24*n**3)+n*(n+1)*(1+6*n+6*n*n)]
for j,(got,want) in enumerate(zip(cumulants,expected)):checks[f'cumulant_{j+1}']=s.expand(got-want)==0
# Independent raw moments from exp(cumulant-generating function), not the claimed variance.
mgf=s.exp(cg);raw=[s.expand(s.diff(mgf,t,j).subs(t,0)) for j in range(5)]
x=s.symbols('x');center=2*k1-dd;poly=(2*x-center)**2
mean=lambda p:s.expand(sum(c*raw[power[0]] for power,c in s.Poly(s.expand(p),x).terms()))
var=s.expand(mean(poly*poly)-mean(poly)**2);formula=16*(k4+2*k2*k2+2*dd*k3+dd*dd*k2)
checks['raw_moment_variance']=s.expand(var-formula)==0
checks['real_optimal_center']=s.simplify(s.diff(var,dd).subs(dd,-k3/k2))==0
checks['nearest_integer_penalty']=s.expand(s.diff(var,dd,2)/8-4*k2)==0
therm=s.expand(var.subs({n:1,dd:-4}));coh=s.expand(var.subs({n:0,dd:-1}))
checks['thermal_centered_variance']=therm==288*mu**2+688*mu+288
checks['coherent_limit']=coh==32*mu**2
checks['thermal_centered_mean']=s.expand(mean(poly).subs({n:1,dd:-4}))==12*mu+24
checks['thermal_linear_variance']=s.expand(4*k2.subs(n,1))==12*mu+8
# Algebraic nearest-integer domain: ratio3.5<(13mu+6)/(3mu+2)<4.5 for mu>=1.
checks['center_lower_boundary']=s.expand(2*(13*mu+6)-7*(3*mu+2))==5*mu-2
checks['center_upper_boundary']=s.expand(9*(3*mu+2)-2*(13*mu+6))==mu+6
M=4*10**28;VC=therm.subs(mu,M);VQ=12*M+8
checks['tight_centered_sqrt_bound']=VC<(17*M+100)**2
checks['tight_linear_sqrt_bound']=VQ<(7*10**14)**2
base=R(600)*(1+R(1,10**17))/10**14+R(440,2**50+1)+(3600+22000+260100)*R(1,10**17)
extra=(17*M+100)*R(1,10**42)+7*10**14*R(1,10**28);total=base+extra
checks['complete_instrument_budget']=bool(total<R(1,10**11))
checks['energy_continuity']=6300000*R(1,10**11)<R(8,1000)**2
checks['pump_depletion_half_width']=R(8,1000)/2==R(4,1000)
# Actual parity spectrum after changing the center; phase revival remains integral.
for m in [2,4,6]:checks[f'even_center_even_Q_revival_{m}']=all(s.exp(-s.I*s.pi*(2*j-m)**2/2)==1 for j in range(8))
# Nontrivial trilinear shell: |0,0,1> <-> |1,1,0>.
H=s.Matrix([[0,-s.I],[s.I,0]])
def commutes(weight):
 Q=s.diag(weight,2)
 return Q*H==H*Q
checks['thermal_short_period_area_lower']=R(3,2)-R(80)*R(11,10)/(2*10**14)>1
checks['actual_trilinear_charge_commutes']=commutes(2)
def oracle(v=therm,center_offset=6,eps=R(1,10**42),linear=VQ,charge_weight=2):
 return {'variance':s.expand(v-var.subs({n:1,dd:2-center_offset}))==0,'nearest_center':center_offset==6,'linear_variance':linear==4*k2.subs({n:1,mu:M}),'full_budget':bool(base+(17*M+100)*eps+7*10**14*R(1,10**28)<R(1,10**11)),'conserved_charge':commutes(charge_weight)}
checks.update({'oracle_'+k:bool(v) for k,v in oracle().items()});assert all(checks.values()),[k for k,v in checks.items() if not v]
mutants={'coherent_variance_on_thermal':dict(v=32*mu**2),'coherent_center_on_thermal':dict(center_offset=1),'lost_thermal_linear_variance':dict(linear=4*M),'too_large_area_error':dict(eps=R(1,10**40)),'wrong_charge_weight':dict(charge_weight=1)}
failed_checks={name:[k for k,v in oracle(**kw).items() if not v] for name,kw in mutants.items()};faults={k:bool(v) for k,v in failed_checks.items()}

def finish(extra):
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    assert all(faults.values()),faults
    paths=[NOTE,str(Path(__file__).relative_to(ROOT)),*DEPS]
    data=dict(schema_version='1.0',result_id=STEM.split('-')[0].upper(),claim_ceiling='conditional supplied model; no native GU, empirical confidence or hardware claim',evidence_kind='exact algebra/finite matrix controls; interval/resource certificates separately typed; universal proofs in companion note',checks=len(checks),check_names=list(checks),faults_caught=list(faults),mutation_failed_checks=failed_checks,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
    out=ROOT/'lab/process'/f'{STEM}.json'
    if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else:assert json.loads(out.read_text())==data,'stored report stale'
    print(json.dumps(dict(result=data['result_id'],checks=len(checks),faults=len(faults),certificates=extra)))

finish(dict(resource_certificates=dict(displacement_intensity=str(M),thermal_occupation=1,integer_center=str(2*M+6),centered_variance=str(VC),linear_variance=str(VQ),core_upper=str(base),phase_upper=str(extra),full_upper=str(total),margin_to_1e_minus11=str(R(1,10**11)-total),field_moment_upper=6300000)))
