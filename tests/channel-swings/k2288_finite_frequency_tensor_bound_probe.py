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
    data=dict(schema_version='1.0',result_id=stem.split('-')[0].upper(),claim_ceiling='conditional supplied model; no GU, empirical or hardware acceptance',checks=len(checks),check_names=list(checks),evidence_kind='symbolic identities and rational bounds plus finite numerical wave controls; dependency hashes are provenance checks; universal proof in companion',mutation_failed_checks=faults,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
    out=ROOT/'lab/process'/f'{stem}.json'
    if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else:assert json.loads(out.read_text())==data,'stored report stale'
    print(json.dumps(dict(result=data['result_id'],checks=len(checks),faults=len(faults),**extra)))

from flint import arb,ctx
ctx.prec=120
stem='k2288-finite-frequency-tensor-bound'
a,H,F,Hd,Fd,Fdd=s.symbols('a H F Hd Fd Fdd',positive=True)
# Cosmic derivatives; conformal second derivative is a²(Pdd+H Pdot).
P=a*s.sqrt(F)
def dt(e):return s.diff(e,a)*a*H+s.diff(e,H)*Hd+s.diff(e,F)*Fd+s.diff(e,Fd)*Fdd
raw=s.simplify(a*a*(dt(dt(P))+H*dt(P))/P)
expected=a*a*(Hd+2*H*H+R(3,2)*H*Fd/F+Fdd/(2*F)-Fd*Fd/(4*F*F))
check('differentiate_P_twice',s.simplify(raw-expected)==0)
qvac=s.simplify(raw.subs(Fdd,H*Fd-2*F*Hd));target=a*a*H*H*(2+2*Fd/(H*F)-(Fd/(H*F))**2/4)
check('vacuum_potential_identity',s.simplify(qvac-target)==0)
check('T_below37',(1+R('2.33'))**3<37)
check('U_bound',2+4*(37-1)==146 and 146<6**3)
check('p_bound',4*37==148)
check('F_uniform_lower',R(123,222)>R(1,2))
check('Delta_bound',R('33.8')**2+2<1145)
check('Fs_relative_bound',R(148,3)+1+R(1145,18)<114)
check('alphaM_bound',3*114==342)
check('potential_bound',2+2*342+R(342**2,4)<30000)
check('U_two_thirds_bound',146**2<36**3)
z=s.symbols('z',nonnegative=True)
check('conformal_integral',s.integrate(1/(1+z)**2,(z,0,R('2.33')))==R(233,333))
check('J_bound',30000*36==1080000)
x=R(1080000,10**10);eps=x/(1-x)
check('epsilon_fraction',eps==R(27,249973) and eps<R(109,10**6))
check('finite_lower',R('.63506')/(1+eps)>R('.6349'))
check('finite_upper',R('.63509')/(1-eps)<R('.6352'))
prior=json.loads((ROOT/'lab/process/k2283-global-quadratic-cosmology.json').read_text())
for path,h in prior['dependencies'].items():check('prior_hash_'+path,hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h)
check('certified_endpoint',arb(prior['interval_certificates']['endpoint_F'])>123)
check('exp_majorant_at_budget',((arb(str(x.p))/arb(str(x.q))).exp()-1)<arb(str(eps.p))/arb(str(eps.q)))
# Nonzero constant q exact solution exercises the Duhamel bound, with complex initial data.
import cmath,math
for kval,qval,length in [(7.,2.,.4),(8.,-3.,.25),(3.,1.,.2)]:
 w=math.sqrt(kval*kval-qval);actual=cmath.cos(w*length)-1j*kval/w*cmath.sin(w*length)
 error=abs(actual-cmath.exp(-1j*kval*length));bound=math.exp(abs(qval)*length/kval)-1
 check('constant_potential_'+str(qval),0<error<bound)
def oracle(fdd=H*Fd-2*F*Hd,exponent=R(-2),alpha_factor=-3,endpoint=R(123),xi_lower=R('.63506'),xi_upper=R('.63509')):
 return {'potential':s.simplify(raw.subs(Fdd,fdd)-target)==0,'conformal_measure':s.simplify((1+z)**exponent-((1+z)**-1)**2)==0,'redshift':s.simplify(alpha_factor*s.diff(-s.log(1+z),z)-s.diff(3*s.log(1+z),z))==0,
 'F_positive':endpoint/222>R(1,2),'transfer_lower':xi_lower/(1+eps)>R('.6349'),'transfer_upper':xi_upper/(1-eps)<R('.6352')}
assert all(oracle().values())
mut={'wrong_spatial_sign':dict(fdd=H*Fd+2*F*Hd),'missing_conformal_weight':dict(exponent=0),'wrong_redshift_factor':dict(alpha_factor=-1),'endpoint_positivity_without_margin':dict(endpoint=R(1)),'inverted_transfer':dict(xi_lower=R(1)/R('.63509'),xi_upper=R(1)/R('.63506'))}
faults={n:[k for k,v in oracle(**kw).items() if not v] for n,kw in mut.items()}
report(stem,['lab/process/k2283-global-quadratic-cosmology.json','lab/process/k2286-quadratic-tensor-propagation.json'],faults,dict(rational_bound=dict(J_over_Hstar_less_than=1080000,k_over_Hstar_at_least=10**10,epsilon_upper=str(eps),transfer_lower='.6349',transfer_upper='.6352'),evidence_reuse='K2283 first-exit continuous tube and endpoint, unchanged'))
