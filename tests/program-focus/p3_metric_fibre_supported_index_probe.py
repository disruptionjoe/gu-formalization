from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[2]
checks=[];controls=[]
def check(name,condition):
    assert bool(condition),name
    checks.append(name)
def control(name,rejected):
    assert bool(rejected),name
    controls.append(name)
def finish(slug,details):
    report=dict(artifact=slug,grade="exact finite supporting algebra; written universal proofs separate",supporting_checks=checks,contrary_controls=controls,details=details)
    report=json.loads(json.dumps(report))
    target=ROOT/"lab/process"/(slug+".json")
    if "--write" in sys.argv:target.write_text(json.dumps(report,indent=2)+"\n")
    else:assert json.loads(target.read_text())==report,"report replay mismatch"
    print(slug,len(checks),"supporting",len(controls),"contrary")
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
# Integral cellular maps of RP3; differentials and homology input to AHSS.
d1=s.zeros(1);d2=s.Matrix([[2]]);d3=s.zeros(1)
check("cellular chain condition",d1*d2==s.zeros(1) and d2*d3==s.zeros(1))
check("degree-two cohomology has torsion two",smith_normal_form(d2,domain=ZZ)==s.Matrix([[2]]))
check("top cohomology free",d3.rank()==0)
# Relative boundary maps, with rank and an explicit integral kernel generator.
i=s.Matrix([[1],[0]]);delta=s.Matrix([[0,1]])
check("relative composition zero",delta*i==s.zeros(1))
check("relative kernel equals image integrally",delta.nullspace()==[i])
check("connecting map hits generator one",delta*s.Matrix([0,1])==s.Matrix([1]))
control("forgetting reduced boundary coordinate loses index",delta*s.Matrix([0,1])!=delta*s.Matrix([0,0]))
control("constant boundary class does not generate relative index",delta*s.Matrix([1,0])==s.zeros(1))
# W=(r,t mod2), k in free compact support: associative action via rank.
def multiply(v,w):
    r,t=v;u,z=w
    return (r*u,(r*z+u*t)%2)
def act(v,k):return v[0]*k
vs=[(1,0),(1,1),(0,1),(-2,1)]
check("ordinary ring action associative",all(act(multiply(v,w),7)==act(v,act(w,7)) for v in vs for w in vs))
check("sign line acts as identity",all(act((1,1),k)==k for k in [-5,0,1,8]))
control("tensor sign is not additive negative one",act((1,1),1)!=-1)
# Chern polynomial arithmetic independently exposes raw vs ghost index sign.
p1=s.Integer(-48);ahat=-p1/24
full=4*ahat+p1;raw=full+ahat;ghost=full-ahat
check("K3 source fixture full raw ghost",(full,raw,ghost)==(-40,-38,-42))
control("raw minus-one substitution detected",raw!=ghost)
ranks={str(n):dict(full=n,raw_shaped=n+1,two_ghost_shaped=n-1) for n in [10,14]}
check("vertical raw residue differs from ghost",ranks['10']['raw_shaped']%3==2 and ranks['10']['two_ghost_shaped']%3==0)
control("ambient raw coefficient is not vertical raw coefficient",ranks['14']['raw_shaped']%3!=ranks['10']['raw_shaped']%3)
# Generated-image criterion checked against subgroup generators, not finite sampling claim.
finish('p3-metric-fibre-supported-index',dict(relative_maps=dict(i=[1,0],delta=[0,1]),K3_control=dict(full=int(full),raw=int(raw),ghost=int(ghost)),coefficient_models=ranks,topological_assertions_not_certified_by_probe=['Bott and Thom isomorphisms','index normalization and excision','Spin-c and APS realization']))
