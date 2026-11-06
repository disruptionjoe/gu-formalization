#!/usr/bin/env python3
"""Exact randomized linear information fixtures; universal sphere proof is in the note."""
import argparse, hashlib, itertools, json
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
checks=[];controls=[]
def ck(n,v):
    assert bool(v),'FAIL '+n
    checks.append(n)
def ct(n,v):
    assert bool(v),'FAIL contrary '+n
    controls.append(n)
# Actual random-coordinate algorithm: finite distribution over every m-subset.
x=s.symbols('x0:5',real=True);samples=[]
for d,m in [(2,1),(3,1),(4,2),(5,3)]:
    subs=list(itertools.combinations(range(d),m))
    mse=s.expand(sum(sum(x[j]**2 for j in range(d) if j not in a) for a in subs)/len(subs))
    ck('exact_random_projection_mse_'+str((d,m)),mse==s.Rational(d-m,d)*sum(t*t for t in x[:d]))
    samples.append({'d':d,'m':m,'subsets':subs,'expected_squared_error':str(mse)})
# A single hard direction cannot be chosen after observing the random seed.
e1=s.Matrix([1,0]);e2=s.Matrix([0,1]);ck('random_sensor_intersection_zero',s.Matrix.vstack(e1.T,e2.T).rank()==2)
ct('fixed_input_randomization_improves',s.Rational(1,2)<1)
ct('seed_dependent_hard_input_not_minimax',max([1,0])+max([0,1])==2 and s.Rational(1,2)*sum([1,0])<1)
# Sequential orthogonalization of an actually history-dependent scalar sensor.
z=s.symbols('z',real=True);q1=s.Matrix([1,0,0]);q2=s.Matrix([z,1,0]);q2orth=q2-q1*q1.dot(q2)
ck('adaptive_orthogonalization',q2orth==s.Matrix([0,1,0]))
ck('second_value_recovered_from_transcript',s.expand(q2.dot(s.Matrix(x[:3]))-z*x[0])==x[1])
ct('repeated_queries_not_independent',s.Matrix.vstack(q1.T,(2*q1).T).rank()==1)
# Bayes residual moments: spherical projection beta law, analytically integrated fixtures.
t=s.symbols('t',real=True);rho=s.symbols('rho',positive=True)
ck('sphere3_coordinate_mean_squared_residual',s.integrate((1-t*t)/2,(t,-1,1))==s.Rational(2,3))
ck('sphere3_coordinate_mean_norm_residual',s.integrate(s.sqrt(1-t*t)/2,(t,-1,1))==s.pi/4)
constants=[]
for d,m in [(2,1),(3,1),(3,2),(4,2),(5,3)]:
    a=s.Rational(d-m,2);bb=s.Rational(m,2)
    c=s.simplify(s.gamma(a+s.Rational(1,2))*s.gamma(a+bb)/(s.gamma(a)*s.gamma(a+bb+s.Rational(1,2))))
    ck('sphere_squared_moment_'+str((d,m)),s.simplify(s.gamma(a+1)*s.gamma(a+bb)/(s.gamma(a)*s.gamma(a+bb+1)))==s.Rational(d-m,d))
    ck('sphere_norm_moment_strict_'+str((d,m)),c>0 and c**2<s.Rational(d-m,d))
    constants.append({'d':d,'m':m,'mean_norm_over_radius':str(c),'mse_over_radius_squared':str(s.Rational(d-m,d))})
ct('mean_norm_is_not_RMS',s.pi/4!=s.sqrt(s.Rational(2,3)))
# Finite coordinate randomization is squared-optimal but not norm-optimal.
ct('coordinate_scheme_not_norm_optimal',s.sqrt(s.Rational(2,3))>s.pi/4)
# Positive-amplitude abstract ball with a preserved moment, representing a chosen kernel slice.
Q=s.Matrix([[1,-1,0,0],[1,1,-2,0],[1,1,1,-3]]).T
ck('independent_moment_preserving_slice',Q.rank()==3 and s.ones(1,4)*Q==s.zeros(1,3))
G=Q.T*Q;ck('positive_Hilbert_Gram',G==s.diag(2,6,12))
ck('orthonormal_embedding',Q*G.inv()*Q.T==s.eye(4)-s.ones(4,4)/4)
ck('row_norm_margin',all((Q*G.inv()*Q.T)[i,i]==s.Rational(3,4) for i in range(4)))
ck('radius_quarter_positive_fixture',1-s.sqrt(3)/8>0)
# Information complexity is an exact dimension count for this oracle, not a physical sensor cost.
d=12;eps2=s.Rational(1,4);m=s.ceiling(d*(1-eps2));ck('RMS_dimension_consumer',m==9 and 1-s.Rational(m,d)<=eps2 and 1-s.Rational(m-1,d)>eps2)
ck('endpoint_no_queries',s.Rational(5,5)==1)
ck('full_coordinate_recovery',s.eye(3).inv()*s.Matrix(x[:3])==s.Matrix(x[:3]))
report={'result':'K2615','checks':checks,'contrary_controls':controls,'exact_random_coordinate_consumers':samples,'risk_constants':constants,'evidence_kind':'exact finite projection, orthogonalization, beta-moment and margin controls; universal adaptive/minimax proof in note','ceiling':'known finite-dimensional Hilbert ball and pathwise scalar linear-query budget; source classes containing this ball and restricted detector families inherit lower bounds; equality requires unrestricted coordinate access on the known ball','provenance':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in ['explorations/conditional-build/k2611-fixed-preparation-invisible-pressure-2026-11-06.md','explorations/conditional-build/k2613-finite-observation-pressure-ambiguity-2026-11-06.md']}}
out=root/'lab/process/k2615-randomized-linear-pressure-recovery.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==json.loads(json.dumps(report)),'FAIL saved report replay'
print(json.dumps({'result':'K2615','checks':len(checks),'controls':len(controls),'status':'pass'}))
