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

from itertools import combinations
from math import factorial
import sympy as sp
from flint import arb,ctx
ctx.prec=256
# Exact all-subset enumeration is a finite check of the written universal path inequality.
for d in range(4,13):
 good=True
 for count in range(1,d+1):
  sums=[sum(k+1 for k in ks) for ks in combinations(range(d),count)]
  good &= max(sums)==count*(2*d-count+1)//2
 ck('all_increasing_paths_d'+str(d),good)
ctrl('allowing_repeated_index_breaks_triangle',sum([8]*8)>8*9//2)
for d in range(4,16):
 good=True
 for B in [F(0),F(1,3),F(1),F(3)]:
  for C in [F(1),F(3,2),F(2)]:
   exact=sum(B**j*d**(3*j+1)*C**((j+1)*(2*d-j)//2) for j in range(d))
   new=max(1,B)**(d-1)*d**(3*d-1)*C**(d*(d+1)//2)
   old=max(1,B)**(d-1)*d**(3*d-1)*C**(d*d)
   good &= exact<=new<=old
 ck('finite_norm_majorization_d'+str(d),good)
# Exact block recurrence with two offdiagonal steps, preserving the inherited filtration.
for d in [4,6,9]:
 D=sp.diag(*[sp.Rational(d)*2**(k+1) for k in range(d)])
 N=sp.zeros(d)
 for k in range(d):
  if k+1<d:N[k+1,k]=sp.Rational(k+1,3)
  if k+2<d:N[k+2,k]=-sp.Rational(k+2,5)
 R=sum(((-D*N)**j*D for j in range(d)),sp.zeros(d))
 ck('two_step_inverse_'+str(d),(D.inv()+N)*R==sp.eye(d) and (D*N)**d==sp.zeros(d))
 ctrl('wrong_sign_fails_'+str(d),(D.inv()+N)*sum(((D*N)**j*D for j in range(d)),sp.zeros(d))!=sp.eye(d))
# The countermodel is explicitly not original hook tensor evidence.
for n in [1,2,4,8,16]:
 C=F(2);v=[C]
 for k in range(1,n+1):v.append(-F(n-k+1,k+1)*C**(k+1)*v[-1])
 ck('countermodel_full_equations_'+str(n),v[0]/C==1 and all(F(k+1)*C**(-(k+1))*v[k]+(n-k+1)*v[k-1]==0 for k in range(1,n+1)))
 ctrl('denominators_still_quadratic_'+str(n),abs(v[-1])==C**((n+1)*(n+2)//2)/F(n+1))
# Factorial summability controls; universal inequality is in the note.
for d in [4,8,16,32,64]:
 fact=arb(factorial(d));ee=arb(1).exp()
 ck('factorial_radius_'+str(d),fact>(arb(d)/ee)**d)
oldlog=arb(2).log();A=oldlog*arb(3)/4
ck('new_nonempty_Gaussian_window',A>oldlog/2 and A<oldlog)
ctrl('fixed_loss_not_geometric',F(2)**(64*65//2)>F(1000)**64)
deps=['lab/process/k2446-augmented-diagonal-estimate.json','lab/process/k2452-partial-analytic-hook-inverse.json','lab/process/k2455-mixed-compatibility-filtration.json','lab/process/k2470-mixed-hook-syzygies.json']
for p in deps:ck('authenticated_'+Path(p).stem,authenticate(p))
finish('k2473-mixed-inverse-growth',{'universal':'monotone block paths, original compatible filtration and analytic coefficient summation','finite':'exact subset paths, rational two-step inverse matrices, denominator countermodel and interval factorial checks','reused':'original K2446/K2452/K2455/K2470 operator evidence authenticated, not rerun or counted as new tensors','ceiling':'sufficient bound for constructed inverse; no general analytic or nonlinear closure'},deps,{'quadratic_exponent':'d*(d+1)/2','gaussian_sufficient':'A>log(C)/2'})
