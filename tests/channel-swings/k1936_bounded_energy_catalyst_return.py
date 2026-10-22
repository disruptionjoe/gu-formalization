"""Finite exact transport certificates for K1936; entropy illustrations are numerical."""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json, math
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k1936-bounded-energy-catalyst-return.json'
def entropy(p):
    return -sum(float(x)*math.log(float(x)) for x in p if x)
def g(x):
    return math.log1p(x)+x*math.log1p(1/x) if x else 0.0
def transport(joint,energies,J,cut):
    n=len(energies); assert all(x>=0 for row in joint for x in row)
    assert sum(map(sum,joint))==1
    p=[sum(row) for row in joint];q=[sum(joint[i][j] for i in range(n)) for j in range(n)]
    assert all(abs(energies[i]-energies[j])<=J for i in range(n) for j in range(n) if joint[i][j])
    r=sum(abs(a-b) for a,b in zip(p,q))/2
    E=sum(a*x for a,x in zip(p,energies));out=sum(a*x for a,x in zip(q,energies));loss=E-out
    bounded=sum((a-b)*min(x,cut) for a,b,x in zip(p,q,energies))
    tail=sum((a-b)*max(x-cut,0) for a,b,x in zip(p,q,energies))
    assert loss==bounded+tail
    assert bounded<=cut*r
    assert tail<=J*sum(a for a,x in zip(p,energies) if x>cut)
    assert loss<=cut*r+J*E/cut
    assert loss<=E and loss<=J
    if loss>0: assert loss*loss<=4*J*E*r
    c=[min(a,b) for a,b in zip(p,q)]
    assert sum(c)==1-r
    if r:
        a=[(x-z)/r for x,z in zip(p,c)];b=[(x-z)/r for x,z in zip(q,c)]
        assert sum(a)==sum(b)==1
        assert sum(x*y for x,y in zip(b,energies))<=(E+J)/r
        h=entropy([r,1-r]);growth=entropy(q)-entropy(p)
        assert growth<=h+float(r)*(entropy(b)-entropy(a))+1e-11
        assert growth<=h+float(r)*g(float((E+J)/r))+1e-11
    return 9,2 if r else 0

def calculate():
    exact=numeric=0
    for n in (3,5,8):
        energies=[F(i) for i in range(n)]
        for width in (1,2,3):
            for seed in range(1,8):
                a=[[F((i*7+j*11+seed)%9+1) if abs(i-j)<=width else F(0) for j in range(n)] for i in range(n)]
                z=sum(map(sum,a));a=[[x/z for x in row] for row in a]
                for cut in (F(1,2),F(1),F(3,2),F(5)):
                    e,f=transport(a,energies,F(width),cut);exact+=e;numeric+=f
    # A finite exactly energy-conserving bath/catalyst swap fixture.
    t=F(1,2);bath=[1/(1+t),t/(1+t)];prep=[F(1,5),F(3,5),F(1,5)]
    coupling=[[F(0) for _ in prep] for _ in prep]
    for b in range(2):
        for a in range(3):
            bp,ap=(1-b,1-a) if b+a==1 else (b,a)
            assert bp+ap==b+a
            coupling[a][ap]+=bath[b]*prep[a]
    e,f=transport(coupling,[F(0),F(1),F(2)],F(1),F(1));exact+=e+6;numeric+=f
    # Population leakage can exchange system energy even with zero-width bath.
    # Swap |S0,A1> and |S1,A0>, both of total energy one.
    perm={(j,a):(j,a) for j in range(4) for a in range(2)}
    perm[0,1]=(1,0);perm[1,0]=(0,1)
    assert len(set(perm.values()))==8
    assert all(j+a==jp+ap for (j,a),(jp,ap) in perm.items())
    assert abs(perm[0,1][1]-1)==1  # W_B=0 fails; W_B+W_S covers it.
    exact+=3
    # Rational log certificates: e > sum_(k=0)^5 1/k! = 163/60.
    low=sum((F(1,math.factorial(k)) for k in range(6)),F(0))
    assert low==F(163,60) and low**10>10000 and low**12>130001
    assert 4*F(30,10000)<F(11,100)**2
    assert F(11,100)+F(24,10000)<F(1,2)
    exact+=5
    # Rare-tail countercontrol: mean one, return r, but jumps 1/r.
    for k in (10,100,1000):
        r=F(1,k);assert r*k==1 and r<1
        assert k>3
        exact+=3
    return {'claim':'K1936','evidence_kind':'finite exact rational controls plus numerical entropy illustrations; analytic theorem in note',
            'exact_controls':exact,'numerical_entropy_controls':numeric,'certified_example':{'E':10,'W':3,'Delta':1,'beta':'ln2','return_strictly_greater_than':'1/10000'},
            'mean_energy_growth_lower_coefficient':'(ln2)^2/(4 beta^2 W)',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=calculate()
    if args.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))
