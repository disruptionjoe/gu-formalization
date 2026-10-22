"""Recompute derivative annihilation and all diagonal products, without producer code."""
import json,hashlib
from copy import deepcopy
from pathlib import Path
from sage.all import QQ,matrix,vector
from k1945_energy_compatible_raw_columns_probe import inspect as inspect_upstream
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'lab/process/k1948-variable-observation-rigidity.json'
def m(x):return matrix(QQ,x.get('rows',16),x.get('columns',16),{(i,j):QQ(v) for i,j,v in x['entries']})
def inspect(v,r):
 count=0;w=m(v['functional']);ob=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());d=[m(x)/24 for x in ob['target_D']];all_weights=[]
 def ck(x,s):
  nonlocal count
  assert x,s
  count+=1
 def ell(t,X):return sum(w[t,16*i+j]*X[i,j] for i in range(4) for j in range(16))
 for typ in range(4):
  ts=list(map(m,ob['blocks'][typ]['T']));triples=[tuple(m(x[k]) for k in ['C','B','S']) for x in r['observation'][typ]['triples']]
  for C,B,S in triples:
   ck(ell(typ,S)==0,'time derivative cancellation')
   for i in range(3):ck(ell(typ,ts[i]*C-d[i]*S)==0,'spatial derivative cancellation')
  vals=[]
  for i in range(3):
   for j in range(i,3):
    C,B,S=triples[i];D,G,T=triples[j];q=S*D-B*T
    if i!=j:q+=T*C-G*S
    x=ell(typ,q);ck(x>0 if i==j else x==0,'local recomputed quadratic positivity');vals.append(str(x))
    if i==j:all_weights.append(x)
  ck(vals==v['local_coefficients'][typ],'local coefficient report')
 for row,report in zip(r['cross_copy'],v['pair_coefficients']):
  a,b=row['types'];bs=[next(z for z in r['blocks'] if z['type']==t) for t in [a,b]];q=[m(z['Q']) for z in bs];n=[m(z['H']).inverse()*qi.transpose() for z,qi in zip(bs,q)];tri=[]
  for values in row['kernel']:
   x=list(map(QQ,values));Z=matrix(QQ,4,4,x[:16]);B=matrix(QQ,4,4,x[16:32]);S=matrix(QQ,4,16,x[32:96]);T=matrix(QQ,4,16,x[96:]);tri.append((n[0]*Z*q[1],-n[1]*Z.transpose()*q[0],B,-B.transpose(),S,T))
  vals=[]
  for i in range(4):
   for j in range(i,4):
    x=QQ(0)
    for k,l in [(i,j)]+([(j,i)] if i!=j else []):
     C,D,B,G,S,T=tri[k];Cc,Dd,Bb,Gg,Ss,Tt=tri[l];x+=ell(a,S*Dd-B*Tt)+ell(b,T*Cc-G*Ss)
    ck(x>0 if i==j else x==0,'cross-copy recomputed quadratic positivity');vals.append(str(x))
    if i==j:all_weights.append(x)
  ck(report['types']==[a,b] and report['coefficients']==vals,'pair coefficient report')
 mu=min(all_weights);norm2=sum(sum(w[b['type'],j]**2 for j in range(64)) for b in r['blocks']);ck(QQ(v['minimum_square_weight'])==mu,'minimum actual coefficient');ck(QQ(v['full_functional_frobenius_norm_squared'])==norm2,'full Frobenius norm');ck(QQ(v['residual_coercivity_squared_constant'])==norm2/mu**2,'Cauchy Schwarz bound')
 return count
def pins(v):
 assert v['result_id']=='K1948','report identity'
 for p,d in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d,'upstream pin'
def main():
 v=json.loads(P.read_text());r=json.loads((ROOT/'lab/process/k1945-energy-compatible-raw-columns.json').read_text());pins(v);prior=inspect_upstream(r);n=inspect(v,r);caught=[]
 for kind in ['functional','source','correction','pair']:
  x=deepcopy(v);u=deepcopy(r)
  if kind=='functional':x['functional']['entries'][0][2]='0'
  elif kind=='source':
   # Choose a coefficient actually read by the derivative functional.
   W=m(v['functional']);L=matrix(QQ,4,16,list(W.row(0)));T=m(r['blocks'][0]['T'][0]);A=T.transpose()*L;ij=next(iter(A.dict()));C=m(u['observation'][0]['triples'][0]['C']);C[ij]+=1
   u['observation'][0]['triples'][0]['C']={'rows':16,'columns':16,'entries':[[i,j,str(t)] for (i,j),t in C.dict().items()]}
  elif kind=='correction':
   S=m(u['observation'][0]['triples'][0]['S']);S[0,3]+=1;u['observation'][0]['triples'][0]['S']={'rows':4,'columns':16,'entries':[[i,j,str(t)] for (i,j),t in S.dict().items()]}
  else:u['cross_copy'][0]['kernel'][0]=['0']*160
  try:inspect(x,u)
  except AssertionError as e:caught.append(str(e))
 assert len(caught)==4,'actual derivative/product faults detected'
 consistency=[]
 for kind in ['report','pin']:
  x=deepcopy(v)
  if kind=='report':x['result_id']='K0'
  else:x['inputs'][next(iter(x['inputs']))]='0'*64
  try:pins(x)
  except AssertionError as e:consistency.append(str(e))
 assert len(consistency)==2
 print('PASS K1948',n,'independent new controls plus',prior,'reused upstream completeness controls; mathematical faults:',caught,'consistency:',consistency)
if __name__=='__main__':main()
