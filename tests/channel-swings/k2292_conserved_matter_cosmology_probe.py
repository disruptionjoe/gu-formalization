from pathlib import Path
import json,hashlib,sys
import sympy as s
from fractions import Fraction as R
ROOT=Path(__file__).resolve().parents[2]
checks={}
def check(name,value): checks[name]=bool(value)
def verify_prior(path):
 data=json.loads((ROOT/path).read_text())
 for p,h in data['dependencies'].items():check('hash_'+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
 return data
def finish(stem,deps,faults,extra):
 assert all(checks.values()),[k for k,v in checks.items() if not v]
 assert all(faults.values()),faults
 paths=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),*deps]
 data=dict(schema_version='1.0',result_id=stem.split('-')[0].upper(),claim_ceiling='conditional supplied models; no GU empirical or hardware acceptance',checks=len(checks),check_names=list(checks),evidence_kind='exact symbolic identities; hashes provenance only; global continuation and integrating-factor proofs in companion',mutation_failed_checks=faults,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
 out=ROOT/'lab/process'/f'{stem}.json'
 if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(out.read_text())==data,'stored report stale'
 print(json.dumps(dict(result=data['result_id'],checks=len(checks),faults=len(faults),**extra)))

stem='k2292-conserved-matter-cosmology'
dep='lab/process/k2283-global-quadratic-cosmology.json';verify_prior(dep)
u,p,a,v,q,w=s.symbols('u p a v q w',positive=True);h=u**2;curv=12*u*(u**3-p);F=a+curv
pd=p-a/(36*u)+(v+2*q)/(216*u**5)
flow=lambda x,force=pd,qd=(1+w)*q:s.diff(x,u)*p/(3*u*u)+s.diff(x,p)*force+s.diff(x,q)*qd
zero=lambda x:s.factor(x)==0
Fs=flow(F);fried=3*F*h*h-q-curv**2/4-v/2-9*h*h*Fs
check('full00_constraint',zero(fried))
A=p/(3*u**3)+a/(36*u**4);B=(a*a+2*v+4*q)/(36*u**4)
check('F_integrating_factor_identity',zero(Fs-A*F+B))
E=p*p/2+a*u*u/24+(v+2*q)/(144*u*u)
check('nonautonomous_energy',zero(flow(E)-p*p-(1+w)*q/(72*u*u)))
check('energy_majorant',zero(2*E-flow(E)-(a*u*u/12+(v+(1-w)*q)/(72*u*u))))
time=lambda x:-3*h*flow(x)
boxR=-time(time(curv))-3*h*time(curv)
check('conserved_matter_trace',zero(3*boxR-a*curv+2*v-(-1+3*w)*q))
check('Hdot_curvature',zero(curv-6*(2*h*h+time(h))))
vacforce=pd.subs(q,0)
check('same_vacuum_with_matter_fails00',zero(3*F*h*h-q-curv**2/4-v/2-9*h*h*flow(F,vacforce)+q))
check('radiation_trace_zero',s.simplify((-1+3*w).subs(w,s.Rational(1,3)))==0)
check('radiation_force_nonzero',zero(pd-vacforce-q/(108*u**5)))
z,qd0,qr0=s.symbols('z qd0 qr0',real=True);qd=qd0*s.exp(z);qr=qr0*s.exp(4*z/3)
check('dust_conservation',zero(s.diff(qd,z)-qd))
check('radiation_conservation',zero(s.diff(qr,z)-4*qr/3))
check('F_zero_downcrossing',zero(Fs.subs(p,u**3+a/(12*u))+B))
# Algebraic force residuals are independent equations, not copied output labels.
def oracle(matter=2,energy_q=2,cross=4,trace_source=True):
 force=p-a/(36*u)+(v+matter*q)/(216*u**5)
 FF=flow(F,force)
 energy=p*p/2+a*u*u/24+(v+energy_q*q)/(144*u*u)
 target_trace=(-1+3*w)*q if trace_source else 0
 return {'full00':zero(3*F*h*h-q-curv**2/4-v/2-9*h*h*FF),
 'energy_derivative':zero(flow(energy,force)-p*p-(1+w)*q/(72*u*u)),
 'F_source':zero(FF-A*F+(a*a+2*v+cross*q)/(36*u**4)),
 'trace_source':zero(3*boxR-a*curv+2*v-target_trace)}
assert all(oracle().values())
mut={'omit_matter_force':dict(matter=0),'reverse_matter_force':dict(matter=-2),'omit_matter_energy':dict(energy_q=0),'wrong_F_source':dict(cross=2),'vacuum_trace_for_dust':dict(trace_source=False)}
faults={n:[k for k,vv in oracle(**kw).items() if not vv] for n,kw in mut.items()}
finish(stem,[dep],faults,dict(scope='all finite s>=0 for alpha,rho_v>0 and nonnegative conserved fluids -1<=w<=1; positive F still needs endpoint check; no new fit'))
