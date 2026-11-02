from fractions import Fraction as F
from itertools import product
import json, hashlib, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STEM='k2481-complete-retry-instrument'
checks={};controls={}
def ctrl(k,v):
    assert v,k
    controls[k]=bool(v)
def ck(k,v):
    assert v,k
    checks[k]=bool(v)
def mat(a,b,c,d):return ((F(a),F(b)),(F(c),F(d)))
I=mat(1,0,0,1);Z=mat(0,0,0,0);P0=mat(1,0,0,0);P1=mat(0,0,0,1)
def add(a,b):return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def scale(a,t):return tuple(tuple(F(t)*a[i][j] for j in range(2)) for i in range(2))
def sub(a,b):return add(a,scale(b,-1))
def tr(a):return a[0][0]+a[1][1]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def psd(a):return a[0][1]==a[1][0] and a[0][0]>=0 and a[1][1]>=0 and det(a)>=0
def rec(N,A,m):
    acc=Z;t=A
    for k in range(m):acc=add(acc,t);t=N(t)
    return acc
Ew=scale(P1,F(1,2));Ec=scale(P0,F(1,2));En=scale(I,F(1,2))
Ng=lambda X:scale(I,X[0][0]/2)
Nb=lambda X:scale(I,X[1][1]/2)
ck('complete_equal_effects',add(add(Ew,Ec),En)==I and Ng(I)==Nb(I)==En)
ck('two_attempt_same_povm_wrong_different',rec(Ng,Ew,2)[0][0]==0 and rec(Nb,Ew,2)[0][0]==F(1,4))
B2=rec(Ng,add(Ew,Ec),2)
ck('two_attempt_ratio',B2==scale(I,F(3,4)) and rec(Nb,Ew,2)[0][0]/B2[0][0]==F(1,3))
Ag=Ew;Ab=add(Ew,scale(I,F(1,2)))
ck('infinite_good_fixed_equation',Ag==add(Ew,Ng(Ag)))
ck('infinite_bad_fixed_equation',Ab==add(Ew,Nb(Ab)) and Ab[0][0]==F(1,2))
D=mat(1,1,1,-1)
Nh=lambda X:scale(mul(mul(D,X),D),F(1,4))
Ah2=rec(Nh,Ew,2);AhInf=mat(F(1,6),-F(1,6),-F(1,6),F(5,6))
ck('coherent_two_attempt',Ah2==mat(F(1,8),-F(1,8),-F(1,8),F(5,8)))
ck('coherent_resolvent',add(Ew,Nh(AhInf))==AhInf)
ck('coherent_generalized_polynomial',scale(Ah2,F(4,3))==AhInf and tr(AhInf)==1 and det(AhInf)==F(1,9))
A=mat(F(1,4),0,0,0);B=mat(F(1,2),F(1,4),F(1,4),F(1,2))
ck('nontrivial_generalized_bound',psd(sub(scale(B,F(2,3)),A)) and det(sub(scale(B,F(2,3)),A))==0)
v=(F(2),F(-1))
def quadratic(a,v):return sum(v[i]*a[i][j]*v[j] for i in range(2) for j in range(2))
ck('nontrivial_generalized_attainment',quadratic(A,v)/quadratic(B,v)==F(2,3))
ck('singular_support',psd(sub(P0,scale(P0,F(1,3)))) and quadratic(P0,(F(0),F(1)))==0)
Nd=lambda X:mul(mul(P1,X),P1)
ck('dark_fixed_survival',Nd(P1)==P1 and Nd(I)==P1)
# |1> goes to |0> without output; |0> outputs correctly. One-step floor0, two-step floor1.
Nblock=lambda X:scale(P1,X[0][0])
ck('block_floor_without_one_step',Nblock(I)==P1 and Nblock(Nblock(I))==Z)
# A simple adaptive retry-label tree, maps with distinct replacement children.
N0=lambda X:scale(I,X[0][0]/4)
N1=lambda X:scale(I,X[1][1]/4)
rootW=scale(P1,F(1,10));rootO=scale(I,F(1,2))
child0W=scale(P0,F(1,5));child1W=scale(P1,F(1,3))
child0O=scale(I,F(2,3));child1O=scale(I,F(3,4))
At=add(rootW,add(N0(child0W),N1(child1W)));Bt=add(rootO,add(N0(child0O),N1(child1O)))
ck('adaptive_tree_complete',add(rootO,add(N0(I),N1(I)))==I)
ck('adaptive_tree_wrong',At==add(rootW,scale(I,F(2,15))))
ck('adaptive_tree_output',Bt==scale(I,F(41,48)) and psd(sub(Bt,At)))
# Exhaustive small rational terminal laws independently attack TV ratio lemma.
N=20;eta=F(1,4);b=F(1,2);eps=F(1,10);r=eta+eps/b
laws=[(F(w,N),F(c,N),F(N-w-c,N)) for w in range(N+1) for c in range(N+1-w)]
pairs=0
for old in laws:
    if old[0]+old[1]<b or old[0]>eta*(old[0]+old[1]):continue
    for new in laws:
        tv=sum(abs(x-y) for x,y in zip(old,new))/2
        if tv<=eps:
            pairs+=1
            assert new[0]+new[1]>0 and new[0]<=r*(new[0]+new[1])
ck('terminal_tv_grid',pairs>100)
# Scalar CP laws saturate all stated finite-horizon and shared-calibration bounds.
scalar_cases=0
for p,eta,delta,m,z in product([F(1,3),F(1,2),F(3,4)],[F(0),F(1,20),F(1,3)],[F(0),F(1,100)],[1,2,3,9],[F(0),F(1,1000),F(1,10)]):
    b=1-(1-p)**m;eps=delta*b/p;rr=eta+delta/p
    w=(eta*p+delta)*sum((1-p)**k for k in range(m))
    scalar_cases+=1
    assert w==b*rr and (z+(1-z)*w)/(z+(1-z)*b)==(z+(1-z)*b*rr)/(z+(1-z)*b)
ck('scalar_sharpness_family',scalar_cases==3*3*2*4*3)
p=F(1,2);eta=F(1,20);delta=F(1,100);m=3;z=F(1,1000);b=1-(1-p)**m;rr=eta+delta/p
bound=(z+(1-z)*b*rr)/(z+(1-z)*b)
ck('reset_consumer',b==F(7,8) and rr==F(7,100) and bound==F(49751,700100))
ck('reset_budget',F(1,200)+F(1,200)==delta)
ck('naive_bound_strictly_weaker',rr<(eta*p+delta)/(p-delta))

# Exact Kraus/Choi data: Choi(E -> sigma) = E^T tensor sigma.
def kron(a,b):return tuple(tuple(a[i//2][j//2]*b[i%2][j%2] for j in range(4)) for i in range(4))
choig=kron(En,P0);choib=kron(En,P1)
ck('replacement_choi_positive',all(choig[i][i]>=0 and choib[i][i]>=0 for i in range(4)) and all(choig[i][j]==choib[i][j]==0 for i in range(4) for j in range(4) if i!=j))
ck('replacement_choi_trace_preservation',tuple(sum(choig[2*i+j][2*i+j] for j in range(2)) for i in range(2))==(F(1,2),F(1,2)))
# Adaptive expected costs, priced on each reached branch, not summed unweighted.
Xroot=scale(I,F(2));X0=scale(I,F(3));X1=scale(I,F(7));Xt=add(Xroot,add(N0(X0),N1(X1)))
ck('adaptive_cost_recursion',Xt==scale(I,F(9,2)))
# A state-dependent cost effect and a coherent memory map.
X=mat(1,0,0,3);CX=rec(Nh,X,2)
ck('coherent_cost_recursion',CX==mat(2,-F(1,2),-F(1,2),4))
# Sequential replacement before verification: triangle budget, same ideal state.
ck('complete_reset_budget',F(1,200)+F(1,200)==delta and delta<p)
# Block-floor survival and mean count on the explicit 2-step chain.
ck('block_tail_and_mean',rec(Nblock,I,2)==add(I,P1) and Nblock(Nblock(I))==Z)
# Concrete contrary controls reject the named shortcut at actual values.
ctrl('effects_do_not_determine_retry',Ng(I)==Nb(I) and rec(Ng,Ew,2)!=rec(Nb,Ew,2))
Nidentity=lambda X:scale(X,F(1,2))
ctrl('wrong_no_output_update',rec(Nidentity,Ew,2)[0][0]!=rec(Nb,Ew,2)[0][0])
ctrl('wrong_mass_is_not_conditional_risk',F(1,4)!=F(1,3))
ctrl('zero_output_not_zero_error',det(P0)==0 and quadratic(P0,(F(0),F(1)))==quadratic(scale(P0,F(1,3)),(F(0),F(1)))==0)
ctrl('dark_resolvent_invalid',Nd(P1)==P1 and P1!=Z)
ctrl('hidden_memory_evades_effect_calibration',Ng(I)==Nb(I) and sum(abs(choig[i][i]-choib[i][i]) for i in range(4))/4==F(1,2))
# Dropping coherent off-diagonals would give maximum5/6, which fails PSD domination.
ctrl('diagonalized_memory_risk_invalid',not psd(sub(scale(I,F(5,6)),AhInf)))
ctrl('unweighted_hybrid_overcharges',delta*b/p<m*delta)
ctrl('independent_ratio_worsening_is_loose',rr<(eta*p+delta)/(p-delta))
ctrl('omit_retry_reset_cost',3+5*sum((1-F(1,2))**k for k in range(3))>3+5)
actual_cost=(1-z)*sum((1-p+delta)**k for k in range(m))+z*m
ctrl('omit_bad_history_cost',actual_cost>(1-z)*sum((1-p+delta)**k for k in range(m)))
ctrl('one_step_floor_not_necessary',det(sub(I,Nblock(I)))==0 and Nblock(Nblock(I))==Z)
ctrl('wrong_shared_failure_reuse',bound!=z+(1-z)*rr and bound>rr)
# Near-saturation moves all remaining correct mass within the calibration radius.
ps,es,ds=F(1,2),F(9,10),F(1,10)
ck('saturation_attainment',(1-es)*ps<=ds and es+ds/ps>1)
summary={'result_id':'K2481','checks':checks,'controls':controls,'finite_counts':{'terminal_tv_pairs':pairs,'scalar_calibration_cases':scalar_cases},'reset_consumer':str(bound),'evidence_kinds':{'universal':'CP adjoint recurrence, generalized Rayleigh quotient, finite-dimensional survival contraction, stopped-channel telescoping and signed TV proof','finite':'exact Fraction matrices, adaptive trees, terminal-law grids and attained scalar controls','ceiling':'supplied complete positive-Hilbert instruments; no original Q/T implementation, physical GU or novelty claim'}}
if '--self-test' not in sys.argv:
    deps=[f'explorations/conditional-build/{STEM}-2026-11-01.md',str(Path(__file__).relative_to(ROOT)),'lab/process/k2478-heterogeneous-retry-design.json','lab/process/k2463-local-verifier-calibration.json','lab/process/k2457-local-verifier-phase-design.json']
    for dep in deps[2:]:
        old=json.loads((ROOT/dep).read_text())
        ck('authenticate_'+dep,all(hashlib.sha256((ROOT/q).read_bytes()).hexdigest()==h for q,h in old['dependencies'].items()))
    summary['dependencies']={dep:hashlib.sha256((ROOT/dep).read_bytes()).hexdigest() for dep in deps}
    out=ROOT/f'lab/process/{STEM}.json'
    if '--check' in sys.argv:assert json.loads(out.read_text())==summary
    else:out.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(STEM,len(checks),'check groups',len(controls),'contrary controls PASS',pairs,'terminal TV pairs',str(bound))
