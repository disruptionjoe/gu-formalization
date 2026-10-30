from pathlib import Path
import json,hashlib,sys
import sympy as s
from flint import arb,ctx
ctx.prec=160
R=s.Rational
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
 data=dict(schema_version='1.0',result_id=stem.split('-')[0].upper(),claim_ceiling='conditional supplied models; no GU empirical or hardware acceptance',checks=len(checks),check_names=list(checks),evidence_kind='symbolic identities and rational or outward interval bounds; hashes provenance only; universal arguments in companion',mutation_failed_checks=faults,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
 out=ROOT/'lab/process'/f'{stem}.json'
 if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(out.read_text())==data,'stored report stale'
 print(json.dumps(dict(result=data['result_id'],checks=len(checks),faults=len(faults),**extra)))

stem='k2291-rolling-scalar-applicability'
dep='lab/process/k2286-quadratic-tensor-propagation.json';prior=verify_prior(dep)
trajectory=verify_prior('lab/process/k2283-global-quadratic-cosmology.json')
f,a,rho,mp,ref=s.symbols('f a rho mp ref',positive=True)
V=mp**2*ref/4*(1-2*a/f+(a*a+2*rho)/f**2)
dphi=lambda expr:s.diff(expr,f)*s.sqrt(R(2,3))*f/mp
vp=dphi(V);vpp=dphi(vp)
check('potential_first',s.simplify(vp-mp*ref/s.sqrt(6)*(a/f-(a*a+2*rho)/f**2))==0)
check('potential_second',s.simplify(vpp-ref/3*(-a/f+2*(a*a+2*rho)/f**2))==0)
vel,H,Vp,Vpp=s.symbols('vel H Vp Vpp',real=True,nonzero=True)
veldot=-3*H*vel-Vp;Hdot=-vel**2/(2*mp**2)
expanded=Vpp-(3*H*vel**2/H+2*vel*veldot/H-vel**2*Hdot/H**2)/mp**2
formula=Vpp+3*vel**2/mp**2+2*vel*Vp/(mp**2*H)-vel**4/(2*mp**4*H**2)
check('constraint_mass_expansion',s.expand(expanded-formula)==0)
check('deSitter_countercontrol',s.simplify(vpp.subs(f,(a*a+2*rho)/a)-ref*a*a/(3*(a*a+2*rho)))==0)
# Rational flow in u=U^(1/3) avoids a numerical derivative oracle.
u,p=s.symbols('u p',positive=True)
flow=lambda expr:s.diff(expr,u)*p/(3*u*u)+s.diff(expr,p)*(p-a/(36*u)+rho/(216*u**5))
FF=12*u*(u**3-p)+a;b=-3*flow(FF)/FF
xx=s.sqrt(6)*b/(b+2);yy=(a-(a*a+2*rho)/FF)/(s.sqrt(6)*u**4*(1+b/2)**2);ww=(-a+2*(a*a+2*rho)/FF)/(3*u**4*(1+b/2)**2)
mass=ww+2*(b/(b+2))*(a-(a*a+2*rho)/FF)/(u**4*(1+b/2)**2)+18*(b/(b+2))**2-18*(b/(b+2))**4
j=b/(b+2);ell=-6/(b+2)
# Substitute exact parameters before differential evaluation, then compare at U=2.
sub={a:R(169,5),rho:1};jf=s.cancel(j.subs(sub));lf=s.cancel(ell.subs(sub))
def fl(expr):return s.diff(expr,u)*p/(3*u*u)+s.diff(expr,p)*(p-R(169,5)/(36*u)+R(1,216)/u**5)
adiab=-(lf*lf*fl(fl(jf))+(lf*fl(lf)-3*jf*jf*lf+3*lf)*fl(jf))/jf
# Exact expression-tree evaluation in QQ(cuberoot(2)) avoids huge expanded polynomials.
from functools import cache
K=s.QQ.algebraic_field(2**R(1,3));root=K.from_sympy(2**R(1,3))
@cache
def exact(expr):
 if expr==u:return root
 if expr==p:return K.from_sympy(R(9303,10000))
 if expr==a:return K.from_sympy(R(169,5))
 if expr==rho:return K.one
 if expr.is_Rational:return K.from_sympy(expr)
 if expr.is_Add:return sum((exact(v) for v in expr.args),K.zero)
 if expr.is_Mul:
  out=K.one
  for v in expr.args:out*=exact(v)
  return out
 if expr.is_Pow and expr.exp.is_Integer:return exact(expr.base)**int(expr.exp)
 raise ValueError(str(expr))
check('independent_adiabatic_identity',exact(mass)==exact(adiab))
# Evaluator over Arb using exact rational expression trees, no float conversion.
def ev(expr,vals):
 if expr in vals:return vals[expr]
 if expr.is_Rational:return arb(int(expr.p))/int(expr.q)
 if expr.is_Add:return sum((ev(v,vals) for v in expr.args),arb(0))
 if expr.is_Mul:
  out=arb(1)
  for v in expr.args:out*=ev(v,vals)
  return out
 if expr.is_Pow:return ev(expr.base,vals)**ev(expr.exp,vals)
 raise ValueError(str(expr))
vals={u:arb(2)**(arb(1)/3),p:arb('0.9303'),a:arb('33.8'),rho:arb(1)}
mm=ev(mass,vals);pot=ev(ww,vals);bb=ev(b,vals);ad=ev(adiab,vals)
check('mass_negative_interval',mm>arb('-8.532') and mm<arb('-8.531'))
check('potential_positive_interval',pot>arb('4.604') and pot<arb('4.605'))
check('independent_interval_overlap',mm.overlaps(ad))
check('initial_Einstein_expansion',1+bb/2>0)
crit=2*(arb('33.8')**2+2)/arb('33.8');end=arb(trajectory['interval_certificates']['endpoint_F']);f0=ev(FF,vals)
check('potential_concavity_crossing',crit>f0 and crit<end)
def oracle(cross=2,quartic=-R(1,2),potential_only=False,ds_sign=-1):
 candidate=Vpp if potential_only else Vpp+3*vel**2/mp**2+cross*vel*Vp/(mp**2*H)+quartic*vel**4/(mp**4*H**2)
 return {'constrained_mass':s.expand(candidate-expanded)==0,'redshift_Einstein_chain':s.simplify(ds_sign*6/(b+2)-ell)==0}
assert all(oracle().values())
mut={'missing_metric_cross':dict(cross=0),'wrong_Hdot_sign':dict(quartic=R(1,2)),'potential_as_mass':dict(potential_only=True),'wrong_time_orientation':dict(ds_sign=1)}
faults={n:[k for k,v in oracle(**kw).items() if not v] for n,kw in mut.items()}
finish(stem,[dep],faults,dict(interval_results=dict(constrained_mass_over_HE2=str(mm),potential_curvature_over_HE2=str(pot),adiabatic_mass_over_HE2=str(ad),potential_inflection_F=str(crit)),scope='instantaneous flat-gauge mass; no global instability verdict'))
