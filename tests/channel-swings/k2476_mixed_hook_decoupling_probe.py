"""Universal proof is in the paired note; finite controls and dependency authentication here."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def authenticate(p):
 data=json.loads((ROOT/p).read_text())
 return all(hashlib.sha256((ROOT/q).read_bytes()).hexdigest()==h for q,h in data['dependencies'].items())
def finish(st,evidence,deps,extra=None):
 deps=[f'explorations/conditional-build/{st}-2026-11-01.md',str(Path(__file__).relative_to(ROOT)),*deps]
 report={'result_id':st.split('-')[0].upper(),'checks':checks,'controls':controls,'evidence_kinds':evidence,'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},**(extra or {})}
 out=ROOT/f'lab/process/{st}.json'
 if '--check' in sys.argv:assert json.loads(out.read_text())==report
 else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(st,len(checks),'check groups',len(controls),'contrary controls PASS')


import math
import sympy as sp
for d in range(4,13):
 n=d-1;C=F(2);B=F(3,2);bound=max(1,B)**(d-1)*math.factorial(d)*C**(d*(d+1)//2)
 for k in range(d):
  total=F(0)
  for j in range(n-k+1):
   exponent=(j+1)*(k+1)+j*(j+1)//2
   falling=math.factorial(n-k)//math.factorial(n-k-j)
   total+=B**j*falling*C**exponent
   ck(f'path_exponent_{d}_{k}_{j}',exponent<=d*(d+1)//2)
  ck(f'column_bound_{d}_{k}',total<=bound)
 ck(f'borderline_cancellation_{d}',bound/(math.factorial(d)*C**(d*(d+1)//2))==max(1,B)**(d-1))
# Exact derivative-transfer model: a finite control, not an original-hook lower bound.
for n in [3,5,8]:
 C=sp.Rational(2);L0=sp.diag(*[C**(-(k+1)) for k in range(n+1)]);N=sp.zeros(n+1)
 for k in range(n):N[k+1,k]=n-k
 RR=L0.inv();T=RR*N;O=sum([(-T)**j*RR for j in range(n+1)],sp.zeros(n+1))
 ck(f'telescoping_{n}',(L0+N)*O==sp.eye(n+1))
 ck(f'last_coefficient_{n}',O[n,0]==(-1)**n*math.factorial(n)*C**((n+1)*(n+2)//2))
 ctrl(f'wrong_sign_{n}',(L0+N)*sum([T**j*RR for j in range(n+1)],sp.zeros(n+1))!=sp.eye(n+1))
 ctrl(f'decoupling_alone_not_geometric_{n}',abs(O[n,0])>C**(n+1))
# Independently chosen ordinary/scalar blocks expose the exact splitting requirements.
D=sp.Matrix([[1,0,0],[0,1,0]]);J=sp.Matrix([[2,3,5]]);S=sp.Matrix([0,0,sp.Rational(1,5)])
O=sp.Matrix([[1,0],[0,1],[7,-4]])
for q in [sp.Matrix([1,2]),sp.Matrix([-3,4]),sp.Matrix([0,1])]:
 for g in [sp.Rational(0),sp.Rational(2,3)]:
  v=O*q+S*(sp.Matrix([g])-J*O*q)
  ck('split_'+str((tuple(q),g)),D*v==q and J*v==sp.Matrix([g]))
  ctrl('omit_scalar_residual_'+str((tuple(q),g)),J*(O*q+S*g)!=sp.Matrix([g]))
badS=sp.Matrix([1,0,sp.Rational(-1,5)])
ck('bad_lift_scalar_identity',J*badS==sp.ones(1,1))
ctrl('scalar_identity_without_full_kernel',D*(O*sp.Matrix([1,2])+badS*(sp.Matrix([0])-J*O*sp.Matrix([1,2])))!=sp.Matrix([1,2]))
deps=['lab/process/k2443-hook-quantitative-symbol.json','lab/process/k2446-augmented-diagonal-estimate.json','lab/process/k2455-mixed-compatibility-filtration.json','lab/process/k2470-mixed-hook-syzygies.json','lab/process/k2473-mixed-inverse-growth.json']
for p in deps:ck('authenticate_'+p,authenticate(p))
finish('k2476-mixed-hook-decoupling',{'universal':'original ordinary compatible filtration, one full-kernel scalar correction, falling-factorial norm proof and analytic coefficient summation','finite':'exact path bounds and rational model matrices; not fresh original tensor proof','reused':'original ordinary inverse, compatibility and full scalar lift authenticated','ceiling':'sufficient linear classes and analytic solvability equivalence; no full analytic or nonlinear construction'},deps,{'ordinary_bound':'b^(d-1)*d!*C^[d(d+1)/2]','borderline_factorial_power':1})
