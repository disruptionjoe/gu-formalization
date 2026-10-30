#!/usr/bin/env python3
"""Exact controls and separately typed certificates; universal proofs in companion note."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
checks={}
STEM='k2284-operational-clock-tolerance'
NOTE=f'explorations/conditional-build/{STEM}-2026-10-30.md'
DEPS=['explorations/conditional-build/k2282-centered-positive-control-2026-10-29.md', 'explorations/conditional-build/k2279-uniform-pump-energy-2026-10-29.md','explorations/conditional-build/k2238-finite-clock-thermal-circuit-2026-10-29.md']

mu,k,n=s.symbols('mu k n',positive=True)
def poisson(poly):
 out=0
 for (power,),c in s.Poly(s.expand(poly),k).terms():
  out+=c*sum(s.functions.combinatorial.numbers.stirling(power,j,kind=2)*mu**j for j in range(power+1))
 return s.expand(out)
C=(2*k-2*mu-1)**2;EC=poisson(C);Z=C-EC;var=poisson(Z**2);fourth=poisson(Z**4);iid=2*fourth+6*var**2
Zn=(2*k+n-2*mu-1)**2;Zn-=poisson(Zn)
checks['Poisson_mean']=EC==4*mu+1
checks['Poisson_variance']=var==32*mu**2
checks['fourth_centered']=fourth==2048*mu**2+36864*mu**3+15360*mu**4
checks['fourth_iid_difference']=iid==4096*mu**2+73728*mu**3+36864*mu**4
checks['field_number_block_variance']=poisson(Zn**2)==32*mu**2+16*mu*n**2
checks['shifted_block_center']=s.expand(Zn-Z-4*n*(k-mu))==0
checks['uniform_fourth_constant']=8*(4096+73728+36864+256*(2+12))==946176
checks['Taylor_lower_constant']=R(946176,24)==39424
checks['local_region_margin']=32-R(39424,2500)>16
checks['Markov_retained_weight']=1-R(128,5)/101==R(377,505)
checks['operational_coefficient']=4*R(377,505)==R(1508,505)
necessary=R(505,1508)*R(2,10**11)/10**28
checks['necessary_area_fixture']=necessary<R(670,10**42)
# Clock matrix uses an actual nontrivial unitary, then tests the same involution/positivity law.
U=s.diag(1,s.I,-1);I=s.eye(3);zero=s.zeros(3)
J=zero.row_join(U.conjugate().T).col_join(U.row_join(zero));H=s.eye(6)+J
checks['clock_involution']=J*J==s.eye(6)
checks['clock_hermitian']=J==J.conjugate().T
checks['clock_positive_spectrum']=set(H.eigenvals())=={0,2}
psi=s.Matrix([1,s.I,1])/s.sqrt(3);initial=psi.col_join(s.zeros(3,1));actual=-s.I*J*initial
checks['clock_exact_gate']=actual==s.zeros(3,1).col_join(-s.I*U*psi)
c,ss=s.symbols('c ss',real=True)
# Output at nominal+error, global phase removed: -ss|0>psi-i*c|1>Upsi.
state=(-ss*psi).col_join(-s.I*c*U*psi);density=state*state.conjugate().T
reduced=density[:3,:3]+density[3:,3:];rho=psi*psi.conjugate().T
checks['discarded_clock_channel']=s.simplify(reduced-c*c*U*rho*U.conjugate().T-ss*ss*rho)==s.zeros(3)
checks['clock_nontrivial_test_input']=U*rho*U.conjugate().T!=rho
checks['coherent_short_period_area_lower']=R(3,4)-R(80)*R(11,10)/10**14>R(1,2)
# Explicit support revivals; no global monotone timing lower bound.
for mm in [1,3,5]:checks[f'odd_center_even_Q_revival_{mm}']=all(s.simplify(s.exp(-s.I*s.pi*((2*j-mm)**2-1)/4))==1 for j in range(8))
def oracle(v=var,f=fourth,coeff=R(1508,505),clockJ=J,weight=R(377,505)):
 return {'variance':s.expand(v-poisson(Z**2))==0,'fourth':s.expand(f-poisson(Z**4))==0,'compression_weight':weight==1-R(128,5)/101,'coefficient':coeff==4*weight,'clock_involution':clockJ*clockJ==s.eye(6),'clock_hermitian':clockJ==clockJ.conjugate().T}
checks.update({'oracle_'+k:bool(v) for k,v in oracle().items()});assert all(checks.values())
badJ=J.copy();badJ[0,3]=2
mutants={'lost_centered_variance':dict(v=16*mu**2),'lost_Poisson_cubic':dict(f=fourth-36864*mu**3),'pure_dilation_transfer':dict(coeff=4),'unjustified_all_weight':dict(weight=s.Integer(1)),'wrong_clock_coupling':dict(clockJ=badJ)}
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

finish(dict(resource_certificates=dict(local_region='mu*abs(epsilon)<=1/50',mu_minimum=10000,necessary_area_upper=str(necessary),clock_scope='constant strength h*C_m only; supplied-unitary clock is contrary control',discarded_workspace_boundary='proved by total-field-number pinching, not pure dilation overlap')))
