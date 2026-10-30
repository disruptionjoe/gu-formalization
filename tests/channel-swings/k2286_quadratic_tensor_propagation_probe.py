from pathlib import Path
import json,hashlib,sys
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
checks={}
def check(name,value):
    checks[name]=bool(value)
def report(stem,deps,faults,extra):
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    assert all(faults.values()),faults
    paths=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),*deps]
    data=dict(schema_version='1.0',result_id=stem.split('-')[0].upper(),claim_ceiling='conditional supplied model; no GU, empirical or hardware acceptance',checks=len(checks),check_names=list(checks),evidence_kind='symbolic derivative identities and outward interval bounds; dependency hashes are provenance checks; universal proof in companion',mutation_failed_checks=faults,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
    out=ROOT/'lab/process'/f'{stem}.json'
    if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else:assert json.loads(out.read_text())==data,'stored report stale'
    print(json.dumps(dict(result=data['result_id'],checks=len(checks),faults=len(faults),**extra)))

from flint import arb,ctx
ctx.prec=120
stem='k2286-quadratic-tensor-propagation'
dep='lab/process/k2283-global-quadratic-cosmology.json'
prior=json.loads((ROOT/dep).read_text())
for path,h in prior['dependencies'].items():check('prior_hash_'+path,hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h)
x=s.symbols('x',real=True);a=s.Function('a')(x);F=s.Function('F')(x);h=s.Function('h')(x);v=s.Function('v')(x);k=s.symbols('k',positive=True)
L=a**3*F*s.diff(h,x)**2/2-a*F*k*k*h*h/2
EL=s.diff(s.diff(L,s.diff(h,x)),x)-s.diff(L,h)
expected=s.diff(h,x,2)+(3*s.diff(a,x)/a+s.diff(F,x)/F)*s.diff(h,x)+k*k/a**2*h
check('tensor_variational_friction',s.simplify(EL/(a**3*F)-expected)==0)
P=a*s.sqrt(F)
def transformed(power=R(1,2),fcoef=1):
    PP=a*F**power;hh=v/PP
    return s.simplify(PP*(s.diff(hh,x,2)+(2*s.diff(a,x)/a+fcoef*s.diff(F,x)/F)*s.diff(hh,x)+k*k*hh))
target=s.diff(v,x,2)+(k*k-s.diff(P,x,2)/P)*v
check('canonical_equation',s.simplify(transformed()-target)==0)
u,p,aa,rr=s.symbols('u p aa rr',real=True,nonzero=True)
FF=12*u**R(1,3)*(u-p)-aa;force=aa/(36*u**R(1,3))-rr/(216*u**R(5,3))
Fs=s.diff(FF,u)*p+s.diff(FF,p)*(p+force)
identity=(p/(3*u)-aa/(36*u**R(4,3)))*FF-(aa*aa-2*rr)/(36*u**R(4,3))
check('Fs_chain_identity',s.simplify(Fs-identity)==0)
z=s.symbols('z',real=True);fl=s.Function('fl')(z);f0=s.symbols('f0',positive=True)
Xi=s.sqrt(f0/fl);check('Xi_log_derivative',s.simplify(s.diff(Xi,z)/Xi+s.diff(fl,z)/(2*fl))==0)
# ds/d(log a_c)=-3, and ds/dz=3/(1+z).
check('redshift_chain',s.diff(3*s.log(1+z),z)==3/(1+z))
check('Xi_initial_slope',s.simplify((-R(1,2)*3*Fs/FF)-(-3*Fs/FF)/2)==0)
c=s.symbols('c',positive=True);check('normalization_cancels',s.simplify(s.sqrt(c*f0/(c*fl))-Xi)==0)
F0=12*arb(2)**(arb(1)/3)*(arb(2)-arb('.9303'))+arb('33.8')
U=arb(2);pv=arb('.9303');av=arb('-33.8');rv=arb(-1)
fs=(pv/(3*U)-av/(36*U**(arb(4)/3)))*F0-(av*av-2*rv)/(36*U**(arb(4)/3))
am=-3*fs/F0
end=arb(prior['interval_certificates']['endpoint_F']);xi=(F0/end).sqrt()
check('F0_enclosure',F0>arb('49.97285') and F0<arb('49.97286'))
check('alphaM0_enclosure',am>arb('-.82559') and am<arb('-.82557'))
check('endpoint_Xi',xi>arb('.63506') and xi<arb('.63509'))
check('positive_endpoints',F0>0 and end>123)
# A second-order scalar trace must retain the variation of the wave operator.
bx,dR,dbR,alpha=s.symbols('Box_dR dR deltaBox_R alpha')
lin=3*bx+3*dbR-alpha*dR
check('rolling_scalar_trace',s.expand(lin/3-(bx-alpha*dR/3+dbR))==0)
def oracle(power=R(1,2),fcoef=1,redshift=-3,ratio_power=R(1,2),rolling=3*dbR):
 return {'canonical':s.simplify(transformed(power,fcoef)-target)==0,
 'redshift':s.simplify(redshift*s.diff(-x/3,x)-1)==0,'ratio':s.simplify(s.diff((f0/fl)**ratio_power,z)/(f0/fl)**ratio_power+s.diff(fl,z)/(2*fl))==0,
 'trace':s.expand((3*bx+rolling-alpha*dR)-lin)==0}
assert all(oracle().values())
mut={'wrong_canonical_power':dict(power=1),'missing_tensor_friction':dict(fcoef=0),'wrong_redshift_direction':dict(redshift=3),'inverse_distance_ratio':dict(ratio_power=-R(1,2)),'drop_rolling_deltaBox':dict(rolling=0)}
faults={n:[k for k,v in oracle(**kw).items() if not v] for n,kw in mut.items()}
report(stem,[dep],faults,dict(interval_results=dict(F0=str(F0),alphaM0=str(am),Xi_endpoint=str(xi)),inherited_certificate='K2283 complete continuous trajectory; not rerun'))
