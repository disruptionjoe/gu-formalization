"""Exact physical restricted Kraus maps and coherent decoder under unequal damping."""
from pathlib import Path
from itertools import product
import sympy as S
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];st='k2368-unequal-rail-recovery';checks={};controls={};r=S.Rational

def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def control(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def words(b):return [(0,0,b,b),(1,1,1-b,1-b)]
# outcome -1=survival;0/1=occupied rail lost. Each output uses trits0/1/safe vacuum2.
def channel(etas):
 ans={}
 for event in product([-1,0,1],repeat=4):
  cols=[{},{}]
  for b in range(2):
   for w in words(b):
    if any(e>=0 and e!=x for e,x in zip(event,w)):continue
    prob=S.prod(etas[i][x] if e<0 else 1-etas[i][x] for i,(e,x) in enumerate(zip(event,w)))/2
    out=tuple(x if e<0 else 2 for e,x in zip(event,w));cols[b][out]=S.sqrt(prob)
  ans[event]=cols
 return ans
def inner(a,b):return S.simplify(sum(v*b.get(k,0) for k,v in a.items()))
def gram(a,b):return S.Matrix(2,2,lambda i,j:inner(a[i],b[j]))
def scalar(g):return g[0,1]==g[1,0]==0 and S.simplify(g[0,0]-g[1,1])==0
def good(event):return sum(x>=0 for x in event)<=1
etas=[(r(9,10),r(4,5)),(r(4,5),r(9,10)),(r(19,20),r(9,10)),(r(9,10),r(19,20))]
ch=channel(etas);gs={e:c for e,c in ch.items() if good(e)}
check('full_physical_completeness',sum((gram(v,v) for v in ch.values()),S.zeros(2))==S.eye(2))
for n,(e,a) in enumerate(gs.items()):
 for m,(f,bv) in enumerate(gs.items()):check(f'good_cross_KL_{n}_{m}',scalar(gram(a,bv)))
p0=gram(ch[(-1,)*4],ch[(-1,)*4])[0,0];p1=sum(gram(c,c)[0,0] for e,c in gs.items() if e!=(-1,)*4);bad=1-p0-p1
check('rational_nonmatched_probabilities',(p0,p1,bad)==(r(1539,2500),r(3231,10000),r(613,10000)))
check('nonmatched_rails',any(a!=b for a,b in etas));check('balanced_survival_products',etas[0][0]*etas[1][0]==etas[0][1]*etas[1][1] and etas[2][0]*etas[3][0]==etas[2][1]*etas[3][1])
# Fixed K2356 decoder. Extract erased bit from surviving repetition partner, then XOR groups.
def decode(w):
 erased=[i for i,x in enumerate(w) if x==2]
 if not erased:return w[0]^w[2],('none',w[0])
 j=erased[0];partner=j^1;s=w[partner];opp=2 if j<2 else 0
 return s^w[opp],(j,s)
for b,c in product(range(2),repeat=2):
 result=S.zeros(2)
 for cols in gs.values():
  for w,x in cols[b].items():
   bb,sy=decode(w)
   for v,y in cols[c].items():
    cc,sz=decode(v)
    if sy==sz:result[bb,cc]+=x*y
 result=result.applyfunc(S.simplify);target=S.zeros(2);target[b,c]=p0+p1
 check(f'recovered_matrix_unit_{b}_{c}',result==target)
matched=[(r(9,10),r(9,10)),(r(4,5),r(4,5)),(r(19,20),r(19,20)),(r(9,10),r(9,10))]
cm=channel(matched);mp0=S.prod(x[0] for x in matched);mp1=sum((1-matched[i][0])*S.prod(matched[j][0] for j in range(4) if j!=i) for i in range(4))
check('matched_prior_formula',sum((gram(c,c) for e,c in cm.items() if good(e)),S.zeros(2))==(mp0+mp1)*S.eye(2))
# Real altered channel: only first repeated group unbalanced; nojump deceptive pass.
one=list(etas);one[0]=(r(19,20),r(4,5));co=channel(one)
control('one_group_nojump_pass',scalar(gram(co[(-1,)*4],co[(-1,)*4])))
control('one_group_singleloss_failure',not scalar(gram(co[(-1,-1,0,-1)],co[(-1,-1,0,-1)])))
both=list(one);both[2]=(r(49,50),r(9,10));cb=channel(both)
control('both_groups_nojump_failure',not scalar(gram(cb[(-1,)*4],cb[(-1,)*4])))
control('two_loss_KL_failure',not scalar(gram(ch[(0,-1,0,-1)],ch[(0,-1,0,-1)])))
# Rational rates verify full reached-support scalar generators, including unmatched rails.
mu=[r(2),r(3),r(4),r(5)];delta=[r(1,3),-r(1,3),r(2,5),-r(2,5)];Gamma=sum(mu)
rate=lambda i,s:mu[i]+(-1)**s*delta[i]
for bit in range(2):
 for w in words(bit):
  check('code_rate_'+str((bit,w)),sum(rate(i,w[i]) for i in range(4))==Gamma)
  for j in range(4):check('loss_rate_'+str((bit,w,j)),sum(rate(i,w[i]) for i in range(4) if i!=j)==Gamma-rate(j,w[j]))
# Projection algorithm to balanced rates, preserving positivity and proving l1 equality on several signed cases.
def project(ds):
 out=list(ds)
 for inds in [(0,1),(2,3)]:
  total=sum(out[i] for i in inds);sgn=S.sign(total);left=abs(total)
  for i in inds:
   if sgn*out[i]>0:
    amount=min(abs(out[i]),left);out[i]-=sgn*amount;left-=amount
  assert left==0
 return out
for i,ds in enumerate([[r(1,2),r(1,3),-r(1,4),r(1,10)],[r(-1,2),r(-1,3),r(1,5),r(1,4)],delta]):
 dp=project(ds);check('balance_projection_'+str(i),dp[0]+dp[1]==dp[2]+dp[3]==0 and all(abs(a)<=abs(b) for a,b in zip(dp,ds)))
 check('balance_l1_'+str(i),sum(abs(a-b) for a,b in zip(dp,ds))==abs(ds[0]+ds[1])+abs(ds[2]+ds[3]))
check('serial_consumer_rational',bad+p1*r(1,32)==r(22847,320000))
deps=[f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R)),'lab/process/k2356-protected-erasure-record.json','lab/process/k2362-transparent-control-locality.json','lab/process/k2365-serial-transparent-control.json']
out=dict(result_id='K2368',checks=len(checks),check_names=list(checks),altered_input_controls=controls,evidence_kind='exact finite physical Kraus products and recovered logical matrix units, rational rates and resource consumers; all-rate theorem in note',details=dict(survival=[[str(v) for v in row] for row in etas],P0=str(p0),P1=str(p1),Bbad=str(bad),serial_theta_half_n32=str(bad+p1/32),criterion='delta1+delta2=delta3+delta4=0',robustness='2T(|A|+|B|)',scope='positive independent constant rates; zero/one-loss subchannel only'),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',len(checks),len(controls));print(json.dumps(out['details'],indent=2))
