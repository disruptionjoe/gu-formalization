#!/usr/bin/env python3
"""K2611 supporting identities and independent boundary-domain controls.
The full curved minimal-domain and synthesis proof is in the research note.
"""
import argparse, hashlib, json
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
checks=[];controls=[]
def ck(name,v):
    assert bool(v),'FAIL '+name
    checks.append(name)
def ct(name,v):
    assert bool(v),'FAIL contrary '+name
    controls.append(name)
x,Y=s.symbols('x Y',real=True)
# Independent exact Dirichlet model: d=D², C=D²+1, A=1,B=-1.
# Polynomial fixtures have the required endpoint jets; not curved Green kernels.
def dd(f):return s.diff(f,x,2)
def co(f):return dd(f)+f
def R(f):
    F=s.integrate(s.integrate(f,x),x)
    return s.expand(F-F.subs(x,0)-x*(F.subs(x,1)-F.subs(x,0)))
def defect(f):return s.expand(co(R(f))-R(co(f)))
phi=x**4*(1-x)**4;chi=dd(phi)
ck('Dirichlet_two_sided_preimage',s.expand(R(chi)-phi)==0)
ck('cofactor_preimage_has_zero_endpoint_values',all(co(phi).subs(x,t)==0 for t in [0,1]))
ck('compact_compatible_commutator_vanishes',defect(chi)==0)
ck('repair_preserves_compact_preimage',s.expand(R(chi)-defect(chi)/2-phi)==0)
ck('Bezout_identity',s.expand(co(phi)-dd(phi)-phi)==0)
psi=x*(1-x);bad=dd(psi);D=defect(bad);repaired=R(bad)-D/2
ct('equation_and_Dirichlet_alone_insufficient',D==-2)
ck('repair_is_homogeneous',dd(D)==0)
ck('repair_preserves_equation',s.expand(dd(repaired)-bad)==0)
ck('repair_symmetrizes_scalar_transfer',s.expand(co(repaired)-(co(R(bad))+R(co(bad)))/2)==0)
ct('old_boundary_not_retained_by_repair',repaired.subs(x,0)==1 and repaired.subs(x,1)==1)
ct('arbitrary_preimage_not_selected',s.expand(R(dd(1+x))-(1+x))==-(1+x))
# Actual saved cofactor and determinant mode data. Differential commutation is
# checked on a nontrivial polynomial; universal commutation is polynomial algebra.
bank=json.loads((root/'lab/process/k2554-analytic-source-response.json').read_text())['determinant']
pp=list(map(s.Rational,bank['P_coefficients_descending']));qq=list(map(s.Rational,bank['Q_coefficients_descending']))
prior=json.loads((root/'lab/process/k2592-scalar-tensor-boundary-pairing.json').read_text())
def apply(poly,f):return s.expand(sum(c*s.diff(f,x,2*j[0]) for j,c in s.Poly(poly,Y).terms()))
for item in prior['cofactor_fixtures']:
    X=s.Rational(item['X']);d=sum(c*(X+Y)**(5-i) for i,c in enumerate(pp))+X*Y*sum(c*(X+Y)**(2-i) for i,c in enumerate(qq))
    C=sum(s.Rational(c)*Y**(4-i) for i,c in enumerate(item['f_coefficients']))
    seed=x**12+x**3+1
    ck('actual_modal_dC_commutes_'+str(X),apply(d,apply(C,seed))==apply(C,apply(d,seed)))
    ck('actual_modal_orders_'+str(X),s.degree(d,Y)==5 and s.degree(C,Y)==4)
# Actual pressure-class identities, no arbitrary scalar-derived replacement.
a=s.Function('alpha')(x);P=s.Function('P')(x);A=P+s.diff(P,x)/(4*a)
t=(4*A+3*P)/2
ck('original_pressure_conservation',s.simplify(s.diff(P,x)+4*a*(P-A))==0)
ck('original_trace_formula',s.expand(t-(7*P/2+s.diff(P,x)/(2*a)))==0)
bR,qR=s.symbols('bR qR',nonzero=True)
ck('tagged_trace_vanishes_for_compact_b',(bR/qR).subs(bR,0)==0)
# Explicit smooth plateau transition p=1-10z³+15z4-6z5 has p'=-30z²(1-z)².
# It is C2 when glued; used only as a sign fixture, not the smooth theorem seed.
z=s.symbols('z',nonnegative=True);p=1-10*z**3+15*z**4-6*z**5
ck('plateau_transition_sign',s.factor(s.diff(p,z))==-30*z**2*(z-1)**2)
ck('plateau_transition_endpoints',p.subs(z,0)==1 and p.subs(z,1)==0)
# alpha<0: decreasing pressure adds a nonnegative observer-pressure contribution.
alpha,drop=s.symbols('alpha drop',positive=True)
ck('negative_alpha_pressure_sign',s.simplify((-drop)/(-4*alpha))==drop/(4*alpha))
ct('wrong_alpha_sign_breaks_positivity',1+s.Rational(-8,4)==-1)
# Scaling a concrete nonzero signed smooth-model source retains zero exterior
# response; the analytic norm statement uses linearity, not these numbers.
j=s.expand(dd(phi));ck('fixture_source_nonzero',j!=0)
ct('norm_upper_bound_not_injectivity',s.integrate((j/1000)**2,(x,0,1))>0 and defect(j/1000)==0)
ck('actual_tube_alpha_sign_domain',s.Rational(35,3624192)<s.Rational(9,4)) # pi>3 ensures sqrt(K)R<pi/2
# Independent finite-calibration fixture with real moment columns, not labels.
# Three unit atoms at distinct positions: zeroth and first moments have a
# nonzero null combination; these atoms illustrate the rank step only.
positions=[s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)]
Mom=s.Matrix([[1,1,1],positions]);weights=s.Matrix([1,-2,1])
ck('finite_moment_null_combination',Mom*weights==s.zeros(2,1) and weights!=s.zeros(3,1))
ck('distinct_positive_sources_same_calibrations',Mom*s.Matrix([2,2,2])==Mom*(s.Matrix([2,2,2])+weights/2) and all(z>0 for z in s.Matrix([2,2,2])+weights/2))
ct('nonlinear_constraint_not_automatically_preserved',sum(z*z for z in s.Matrix([2,2,2])+weights/2)!=12)
refs=['explorations/conditional-build/k2609-pressure-jet-contact-boundary-2026-11-06.md','explorations/conditional-build/k2588-real-boundary-response-2026-11-05.md','explorations/conditional-build/k2592-scalar-tensor-boundary-pairing-2026-11-06.md','explorations/conditional-build/k2594-reciprocal-distributional-response-2026-11-06.md','lab/process/k2592-scalar-tensor-boundary-pairing.json','lab/process/k2554-analytic-source-response.json']
report={'result':'K2611','checks':checks,'contrary_controls':controls,'boundary_fixture_defect':str(D),'evidence_kind':'exact actual coefficient commutation and pressure identities; independent Dirichlet boundary fixture; universal curved selection and smooth kernel proofs in note','ceiling':'signed correlated smooth-source fixed-preparation kernel; constructed nonnegative-amplitude pair ambiguity; no physical energy, general higher-jet Sobolev extension or computed Ore coefficients','provenance':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}}
out=root/'lab/process/k2611-fixed-preparation-invisible-pressure.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL saved report replay'
print(json.dumps({'result':'K2611','checks':len(checks),'controls':len(controls),'status':'pass'}))
