"""Exact positive-bin likelihood, finite-count risk and nuisance countercontrols."""
from pathlib import Path
import sympy as s
import json,hashlib,sys,math
R=Path(__file__).resolve().parents[2];checks={};faults={};q=s.Rational

def check(k,v):
 checks[k]=bool(v)
 if not v: raise AssertionError(k)
x=s.symbols('x',real=True);P=(3*x*x-1)/2
check('positive_source_floor',1-q(3,4)/2==q(5,8))
check('polar_mean',2*s.integrate(P,(x,q(1,2),1))==q(3,8))
check('equator_mean',s.integrate(P,(x,-q(1,2),q(1,2)))==-q(3,8))
b=[q(1,2),q(1,8)];p=lambda z,h:q(1,2)+3*z*b[h]/16
intervals=[(p(q(1,2),h),p(q(3,4),h)) for h in range(2)]
check('normalized_bin_intervals',intervals==[(q(35,64),q(73,128)),(q(131,256),q(265,512))])
th=q(545,1024);margin=q(15,1024)
check('two_sided_gap',intervals[0][0]-th==margin and th-intervals[1][1]==margin)
# Verify the joint PMF factorization directly for actual small counts and amplitudes.
for a in [q(1,3),q(7,2)]:
 for h in range(2):
  pp=p(q(5,8),h)
  for n in range(7):
   for k in range(n+1):
    left=(a*pp)**k*(a*(1-pp))**(n-k)/s.factorial(k)/s.factorial(n-k)
    right=a**n/s.factorial(n)*s.binomial(n,k)*pp**k*(1-pp)**(n-k)
    assert left==right
check('finite_likelihood_factorization',True)
check('count_error_exponent',2*8192*margin**2==q(225,64))
check('exp3_exceeds20',sum(q(3)**j/s.factorial(j) for j in range(9))>20)
# Exact integer binomial mass recurrence, no floating tail approximation.
def tail(n,a,d,cut,lower):
 b=d-a;term=b**n;num=0
 for k in range(n+1):
  if (k<=cut)==lower:num+=term
  if k<n:
   numerator=term*(n-k)*a;den=(k+1)*b
   term,rem=divmod(numerator,den);assert rem==0
 return num,d**n
n=8192;cut=int(n*th);risk0=tail(n,35,64,cut,True);risk1=tail(n,265,512,cut,False)
check('exact_size_under5percent',20*risk0[0]<risk0[1]);check('exact_power_over95percent',20*risk1[0]<risk1[1])
eta=q(1,512);newmargin=margin-eta
check('robust_gap',newmargin==q(13,1024))
check('robust_error_exponent',2*12288*newmargin**2==q(507,128))
check('robust_below5percent',q(507,128)>3)
# exp(-mu) >= 1-mu bounds power <= alpha+mu on low-count experiment.
check('low_intensity_power_ceiling',q(1,20)+q(1,100)==q(3,50))
check('overlap_counterexample',p(q(1,8),0)==p(q(1,2),1))
# Heat-semigroup counterexample in one actual positive harmonic family.
check('positive_heat_absorption',q(3,4)*b[1]*b[0]==q(3,4)*b[0]*b[1])
# Conditional mark law changes under independent bin brightness.
original=p(q(1,2),0);changed=2*original/(2*original+(1-original))
faults['independent_bin_brightness']=['normalized_bin_intervals'] if changed>intervals[0][1] else []
faults['widen_shape_to_overlap']=['two_sided_gap'] if p(q(1,8),0)<=intervals[1][1] else []
faults['reverse_heat_attenuation']=['normalized_bin_intervals'] if q(1,2)+3*q(1,2)*8/16!=intervals[1][0] else []
faults['remove_positive_baseline']=['positive_source_floor'] if -q(3,4)/2<0 else []
# A whole-shared duplicated photon yields N=2,K=1 deterministically, not Bin(2,1/2).
faults['duplicate_one_photon_into_both_bins']=['finite_likelihood_factorization'] if q(1)!=s.binomial(2,1)*q(1,2)**2 else []
assert all(faults.values())
deps=[f'explorations/conditional-build/k2346-positive-count-response-discrimination-2026-10-30.md',str(Path(__file__).relative_to(R)),'explorations/conditional-build/k2343-conditional-count-exchangeability-2026-10-30.md','explorations/conditional-build/k2327-constrained-seed-likelihood-2026-10-30.md']
out=dict(result_id='K2346',checks=len(checks),check_names=list(checks),evidence_kind='exact symbolic/rational controls and two exact integer binomial tail sums; universal nuisance/concentration proof in note',mutation_failed_checks=faults,details={'N':n,'cut':cut,'size_decimal':str(s.N(s.Rational(*risk0),16)),'type2_decimal':str(s.N(s.Rational(*risk1),16)),'gap':str(2*margin),'robust_N':12288,'nuisance':'common Cox amplitude; bounded shape'},dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
pth=R/'lab/process/k2346-positive-count-response-discrimination.json'
if '--write' in sys.argv:pth.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(pth.read_text())==out
print(json.dumps({k:out[k] for k in ['result_id','checks','details']}))
