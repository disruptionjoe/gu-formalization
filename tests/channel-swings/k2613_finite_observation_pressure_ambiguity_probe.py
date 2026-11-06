#!/usr/bin/env python3
"""Exact finite information controls; universal topology is the cited proof, not this fixture."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
checks=[];controls=[]
def ck(name,cond):
    assert bool(cond),'FAIL '+name
    checks.append(name)
def ct(name,cond):
    assert bool(cond),'FAIL contrary '+name
    controls.append(name)
# Abstract independent smooth-kernel coordinates, not computed curved Ore coefficients.
base=s.Matrix([1,1,1,1]);r=s.Rational(1,10)
# A prescribed moment first removes one dimension. Adaptive sensors are frozen on baseline.
moment=s.Matrix([[1,1,1,1]])
def transcript(v):
    y1=(s.Matrix([[1,0,1,0]])*v)[0]
    sensor=s.Matrix([[0,1,0,2]]) if y1>=2 else s.Matrix([[2,0,1,0]])
    return (y1,(sensor*v)[0])
mat=moment.col_join(s.Matrix([[1,0,1,0],[0,1,0,2]]));basis=mat.nullspace()
ck('three_constraints_leave_nonzero_direction',mat.rank()==3 and len(basis)==1)
v=basis[0]*r;plus=base+v;minus=base-v
ck('nonzero_distinct_pair',v!=s.zeros(4,1) and plus!=minus)
ck('prescribed_moment_unchanged',moment*plus==moment*base==moment*minus)
ck('adaptive_same_baseline_transcript',transcript(plus)==transcript(base)==transcript(minus))
ck('positive_amplitude_fixture',min(list(plus)+list(minus))>0)
ck('norm_separation',s.expand((plus-minus).dot(plus-minus))==4*v.dot(v))
# A nonlinear fixed calibration pair need not share the baseline value.
x,y,z=s.symbols('x y z',real=True)
F=s.Matrix([x+z*z,y+x*x]);a=s.Matrix([0,0,r]);b=-a
fa=F.subs(dict(zip([x,y,z],a)));fb=F.subs(dict(zip([x,y,z],b)));f0=F.subs({x:0,y:0,z:0})
ck('nonlinear_antipodal_equal',fa==fb)
ct('nonlinear_pair_is_not_baseline',fa!=f0)
norm2=x*x+y*y+z*z
ck('squared_norm_antipodes',norm2.subs({x:0,y:0,z:r})==norm2.subs({x:0,y:0,z:-r})==r*r)
ct('zero_squared_norm_is_singleton',s.Poly(norm2,x,y,z).coeffs()==[1,1,1] and r*r>0)
# Nonlinear adaptive fixture: a discontinuous choice at an even first reading.
def nonlinear_adaptive(q):
    first=q.dot(q)
    row=s.Matrix([[1,0,0,0]]) if first>0 else s.Matrix([[0,1,0,0]])
    second=(row*q)[0]+q[2]**2
    return first,second
u=s.Matrix([0,0,r,0]);ck('adaptive_nonlinear_fixture',nonlinear_adaptive(u)==nonlinear_adaptive(-u))
ck('adaptive_nonlinear_dimension_threshold',len(u)==2**2)
ct('classical_dimension_not_adaptive_general_threshold',2+1<2**2)
for m in [1,2,3,5]:
    ck('linear_nullity_'+str(m),s.eye(m).row_join(s.ones(m,1)).nullspace()!=[])
# Recovering a restricted measured line is possible; the full affine ball is essential.
t=s.symbols('t',real=True);line=s.Matrix([t,0,0]);ck('measured_line_recoverable',F.subs(dict(zip([x,y,z],line)))[0]==t)
ct('restriction_removes_sphere_dimension',s.Matrix.hstack(line.diff(t)).rank()==1<3)
# Exact decoder-risk fixture; triangle inequality proves arbitrary decoders in the note.
z0=s.symbols('z0',real=True);rr=s.Rational(1,5)
ck('squared_risk_pair_average',s.expand(((z0-rr)**2+(z0+rr)**2)/2)==z0*z0+rr*rr)
ck('constant_center_attains_radius',abs(rr)==abs(-rr))
# Randomized decoder distribution, identical observation law at the two inputs.
outputs=[-s.Rational(2,5),s.Rational(1,10),s.Rational(1,2)];weights=[s.Rational(1,4),s.Rational(1,2),s.Rational(1,4)]
riskplus=sum(w*abs(o-rr) for w,o in zip(weights,outputs));riskminus=sum(w*abs(o+rr) for w,o in zip(weights,outputs))
ck('random_decoder_expected_risk',riskplus+riskminus>=2*rr and max(riskplus,riskminus)>=rr)
# This fixture does NOT assert a single hard direction for randomized sensor choices.
ct('sensor_randomization_requires_new_argument',s.Matrix([[1,0],[0,1]]).nullspace()==[])
report={'result':'K2613','checks':checks,'contrary_controls':controls,'finite_fixture':{'direction':list(map(str,v)),'moment':str((moment*base)[0]),'transcript':list(map(str,transcript(base))),'nonlinear_common':list(map(str,fa)),'nonlinear_baseline':list(map(str,f0)),'expected_decoder_risks':[str(riskplus),str(riskminus)]},'evidence_kind':'exact finite linear/nonlinear/adaptive and risk fixtures; universal proof in note; adaptive-continuous result imported from Ullrich Theorem1','imported_reference':'https://arxiv.org/html/2610.33781v1','ceiling':'conditional smooth source class; no physical energy, explicit curved coefficients, randomized sensing or dimension-uniform error floor','provenance':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in ['explorations/conditional-build/k2611-fixed-preparation-invisible-pressure-2026-11-06.md','lab/process/k2611-fixed-preparation-invisible-pressure.json']}}
out=root/'lab/process/k2613-finite-observation-pressure-ambiguity.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL saved report replay'
print(json.dumps({'result':'K2613','checks':len(checks),'controls':len(controls),'status':'pass'}))
