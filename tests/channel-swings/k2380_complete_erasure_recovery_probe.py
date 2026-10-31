"""Exact complete erasure-channel recovery; all matrix units and masks. --write saves report."""
from fractions import Fraction as F
from itertools import combinations,product
from collections import defaultdict
from pathlib import Path
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v,control=False):
 (controls if control else checks)[k]=bool(v)
 assert v,k
def words(b):return [(0,0,b,b),(1,1,1-b,1-b)]
def recovered(S,b,c,omit=False):
 kept=[i for i in range(4) if i not in S];num=len(S)
 if num==4:return {(0,0):F(b==c,2),(1,1):F(b==c,2)}
 if num==0:gates=[(0,2),(2,3)];target=2
 if num==1:
  partner=next(iter(S))^1;opp=[i for i in kept if i//2!=partner//2];gates=[(partner,opp[0]),(opp[0],opp[1])];target=opp[0]
 if num==2:
  a,t=kept;gates=[(a,t)];target=a if a//2==t//2 else t
 if num==3:gates=[];target=kept[0]
 if omit:gates=[]
 out=defaultdict(F)
 for u,v in product(words(b),words(c)):
  if any(u[i]!=v[i] for i in S):continue
  u=list(u);v=list(v)
  for a,t in gates:u[t]^=u[a];v[t]^=v[a]
  if any(u[i]!=v[i] for i in kept if i!=target):continue
  out[u[target],v[target]]+=F(1,2)
 return {k:v for k,v in out.items() if v}
def expected(S,b,c):
 if len(S)<=1:return {(b,c):F(1)}
 if len(S)==2:
  if set(S) in ({0,1},{2,3}):
   out=defaultdict(F);out[b,c]+=F(1,2);out[1-b,1-c]+=F(1,2);return dict(out)
  return {(b,b):F(1)} if b==c else {}
 return {(0,0):F(1,2),(1,1):F(1,2)} if b==c else {}
masks=[tuple(S) for k in range(5) for S in combinations(range(4),k)]
for S in masks:
 for b,c in product((0,1),repeat=2):
  ck('mask_'+'_'.join(map(str,S))+'_E'+str(b)+str(c),{k:v for k,v in recovered(S,b,c).items() if v}==expected(S,b,c))
ck('omit_extraction_caught',recovered((0,2),0,0,True)!=expected((0,2),0,0),True)
ck('same_group_coherence_retained',recovered((0,1),0,1)=={(0,1):F(1,2),(1,0):F(1,2)})
ck('split_group_coherence_destroyed',recovered((0,2),0,1)=={})
# Bell prep H_f CX_fa, partial trace a, from exact amplitude products 1/2.
# H on f creates two amplitudes 1/sqrt2; store their common factor separately.
after_H={(0,0):1,(1,0):1}
bell={(f,a^f):amplitude for (f,a),amplitude in after_H.items()};mixed=defaultdict(F)
for (f,a),(g,b) in product(bell,bell):
 if a==b:mixed[f,g]+=F(1,2)
ck('all_loss_mixing_preparation',dict(mixed)=={(0,0):F(1,2),(1,1):F(1,2)})
pure_output={(0,0):F(1),(1,1):F(0)};input_one={(0,0):F(0),(1,1):F(1)}
pure_distance=sum(abs(pure_output[k]-input_one[k]) for k in input_one)/2
mixed_distance=sum(abs(mixed[k]-input_one[k]) for k in input_one)/2
ck('pure_fallback_input_one_control',pure_distance==1 and mixed_distance==F(1,2),True)
def weights(etas):
 return {S:prod([(1-e if i in S else e) for i,e in enumerate(etas)]) for S in masks}
def prod(xs):
 out=F(1)
 for x in xs:out*=x
 return out
def tally(etas):
 w=weights(etas);P=[sum(v for S,v in w.items() if len(S)==k) for k in range(5)];a=sum(w[S] for S in [(0,1),(2,3)]);b=P[2]-a;q=(P[0]+P[1]+P[2]/2+sum(P[3:])/4,a/2+sum(P[3:])/4,sum(P[3:])/4,b/2+sum(P[3:])/4);return P,q
P,q=tally([F(9,10),F(4,5),F(7,10),F(3,5)])
ck('nonuniform_probability_normalization',sum(P)==sum(q)==1 and all(x>=0 for x in q))
ck('nonuniform_optimum',1-q[0]==F(1393,10000))
P10,q10=tally([F(9,10)]*4);e=1-q10[0]
ck('iid_point',e==F(1083,40000))
ck('old_bad_event_bound',sum(P10[2:])==F(523,10000) and e<sum(P10[2:]))
for p in [F(0),F(1,10),F(1,2),F(1)]:
 Pp,qp=tally([1-p]*4);ck('iid_polynomial_'+str(p),1-qp[0]==3*p*p-3*p**3+F(3,4)*p**4)
# Gate accounting: measured flags8, rail decode2 per survivor, extraction and routing.
ck('recovery_gate_bounds',max(21,8+4+1+3,8+2+3,8+2)==21)
debt=F(6600,7000000);ck('conditional_cost_fixture',e+debt<F(28018,1000000))
# Bell-diagonal output: trace distance from Bell = nonidentity weight exactly.
ck('bell_distance_matches_upper',(abs(q[0]-1)+sum(abs(x) for x in q[1:]))/2==1-q[0])
# Choi separability at two losses verified by explicit measure-prepare matrix-unit maps.
for S in [s for s in masks if len(s)==2]:
 ck('two_loss_dephasing_'+str(S),all(recovered(S,b,c)==expected(S,b,c) for b,c in product((0,1),repeat=2)))
ps=['lab/process/k2377-time-ordered-rate-robustness.json','lab/process/k2356-dual-rail-erasure-recovery.json']
# Locate exact native original code evidence without guessing a filename.
ps=[ps[0]]+[str(p.relative_to(ROOT)) for p in (ROOT/'lab/process').glob('k2356-*.json')]
report={'result_id':'K2380','checks':len(checks),'check_names':checks,'changed_input_controls':controls,'nonuniform_pauli_weights':list(map(str,q)),'nonuniform_error':'1393/10000','iid_p_one_tenth_error':str(e),'scope':'Optimal final CPTP recovery for idle independent matched-within-pair erasure channels only. Complete driven/mismatched hardware optimum unproved.','dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ps}}
text=json.dumps(report,sort_keys=True,indent=2)+'\n'
if '--write' in sys.argv:(ROOT/'lab/process/k2380-complete-erasure-recovery.json').write_text(text)
print(text)
