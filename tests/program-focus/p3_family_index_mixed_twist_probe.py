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
from itertools import product
# Integral exterior algebra on x,beta,a,b; multiplication computes all Koszul signs.
def add(*vs):
    out={}
    for v in vs:
        for k,c in v.items():out[k]=out.get(k,0)+c
    return {k:c for k,c in out.items() if c}
def mul(v,w):
    out={}
    for a,c in v.items():
        for b,d in w.items():
            if a&b:continue
            swaps=sum(1 for i in range(4) for j in range(4) if a>>i&1 and b>>j&1 and i>j)
            out[a|b]=out.get(a|b,0)+c*d*(-1)**swaps
    return {k:c for k,c in out.items() if c}
def push(v):return {k^3:c for k,c in v.items() if k&3==3}
def scale(n,v):return {k:n*c for k,c in v.items() if n*c}
one={0:1};X={1:1};beta={2:1};a={4:1};b={8:1};ab=mul(a,b);alpha=mul(X,beta)
check("circle products anticommute",mul(a,b)==scale(-1,mul(b,a)))
check("circle squares vanish",mul(a,a)=={} and mul(b,b)=={})
xi=mul(beta,a);W=mul(X,b)
check("mixed sign has two cancellations",mul(xi,W)==mul(alpha,ab))
check("untwisted family index zero",push(xi)=={})
check("mixed family class nonzero",push(mul(xi,W))==ab)
control("rank-only formula loses mixed class",push(mul(xi,W))!=push(xi))
# General six-coefficient formula via exterior multiplication, with independent expanded result.
for values in [(2,3,5,7,11,13,17,19),(-1,2,3,-5,7,0,-2,4),(0,0,1,0,0,0,0,1)]:
    A0,A1,Ba,Bb,u0,u1,wa,wb=values
    A={0:A0,12:A1};B1={4:Ba,8:Bb};u={0:u0,12:u1};w={4:wa,8:wb}
    xi=add(mul(alpha,A),mul(beta,B1));W=add(u,mul(X,w))
    expected=add({0:A0*u0},{12:A0*u1+A1*u0+Ba*wb-Bb*wa})
    check('complete product '+str(values),push(mul(xi,W))==expected)
    control('omitting mixed term '+str(values),Ba*wb-Bb*wa!=0 and push(mul(xi,W))!=mul(A,u))
check("nondegenerate odd pairing",mul(a,b)==ab and mul(b,a)==scale(-1,ab))
control("nonconstant base twist also violates scalar rank",push(mul(alpha,add(one,ab)))!=push(alpha))
for N in [1,7]:
    # Formal stabilization identity; existence of actual E at sufficient rank is a separate proof.
    check('stabilized virtual identity '+str(N),push(mul(mul(beta,a),add(scale(N,one),mul(X,b))))==ab)
check("pullback constant-rank repair",push(mul(add(alpha,mul(beta,a)),scale(5,one)))=={0:5})
control("point evaluation misses reduced K class",ab.get(0,0)==0 and ab!={})
finish('p3-family-index-mixed-twist',dict(generator_order=['x','beta7','a','b'],mixed_product=push(mul(mul(beta,a),mul(X,b))),formula='A*u+B1*w',torsion='eta terms handled by written Kunneth/torsion-free target proof',actual_bundle_realization='stable existence proved in note, no small-rank construction asserted'))
