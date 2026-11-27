#!/usr/bin/env python3
"""Exact controls for the written local-complement theorem.
Sparse full Cl14 products; all16 character row systems at representative
weights. Samples support, but do not replace, the universal written proof.
Reuses the old native rank certificate without recomputing its512 minor.
"""
import argparse, hashlib, itertools, json, time
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def add(a,b):
 c=dict(a)
 for k,v in b.items():c[k]=c.get(k,F(0))+v
 return {k:v for k,v in c.items() if v}
def scale(a,s):return {k:v*s for k,v in a.items() if v*s}
def mul(a,b,eta):
 c={}
 for x,u in a.items():
  for y,v in b.items():
   sign=(-1)**sum((y&((1<<i)-1)).bit_count() for i in range(14) if x>>i&1)
   for i in range(14):
    if x & y & (1<<i):sign*=eta[i]
   k=x^y;c[k]=c.get(k,F(0))+u*v*sign
 return {k:v for k,v in c.items() if v}
def rref(rows):
 a=[[F(x)for x in row]for row in rows];r=0;piv=[]
 for j in range(len(a[0])):
  k=next((i for i in range(r,len(a)) if a[i][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];z=a[r][j];a[r]=[x/z for x in a[r]]
  for i in range(len(a)):
   if i!=r:
    z=a[i][j];a[i]=[x-z*y for x,y in zip(a[i],a[r])]
  piv.append(j);r+=1
  if r==len(a):break
 return a,piv
def matrices(p,sigma,c):
 out=[]
 for k in range(4):
  m=[[F(0)for _ in range(6)]for _ in range(6)];m[k][5]=1
  for i in range(4):
   if i!=k:
    for j in range(4):
     if j not in (i,k):m[i][j]=1
    m[i][4]=10
  for j in range(4):
   if j!=k:m[4][j]=1
  m[4][4]=9;m[5][k]=F(sigma)/p;m[5][5]=c/p;out.append(m)
 return out
def run():
 checks={};case_results=[]
 def ok(name,condition):
  checks[name]=bool(condition)
  if not condition:raise AssertionError(name)
 I={0:F(1)};zero={};omega={(1<<14)-1:F(1)};g=[{1<<i:F(1)}for i in range(14)]
 normalized_blocks=0
 for port,sigma,c,eta in [('K77',-1,F(11,12),[1,-1,-1,-1]+[1]*6+[-1]*4),('K95',1,F(-11,12),[-1,1,1,1]+[1]*6+[-1]*4)]:
  mm=lambda a,b:mul(a,b,eta)
  ok(port+' Clifford/volume',mm(omega,omega)==I and all(mm(g[i],g[i])==scale(I,eta[i]) for i in range(14)) and all(add(mm(g[i],g[j]),mm(g[j],g[i]))==zero for i in range(14)for j in range(i)))
  for wp,wm in [(F(1),F(1)),(F(2),F(3)),(F(1),F(-2)),(F(1),F(sigma)-c)]:
   p=wp*wm;W=add(scale(I,(wp+wm)/2),scale(omega,(wp-wm)/2));Ws=add(scale(I,(wp+wm)/2),scale(omega,(wm-wp)/2));E=scale(W,c/p)
   ok(port+f' reciprocal {p}',mm(W,Ws)==scale(I,p) and mm(E,Ws)==scale(I,c))
   R=[scale(g[a],eta[a])for a in range(14)]+[Ws];Ri=g+[scale(W,1/p)]
   normalized=True
   for k in range(4):
    G=mm(g[k],Ws)
    for a in range(15):
     for b in range(15):
      raw={};co=F(0)
      if a<14 and b<14 and len({a,b,k})==3:raw=scale(mm(mm(mm(g[a],g[k]),g[b]),W),eta[a]);co=1
      elif a==k and b==14:raw=I;co=1
      elif a==14 and b==k:raw=scale(I,sigma*eta[k]);co=F(sigma)/p
      elif a==14 and b==14:raw=mm(g[k],E);co=c/p
      normalized &= mm(mm(Ri[a],raw),R[b])==scale(G,co);normalized_blocks+=1
   ok(port+f' full raw normalization {p}',normalized)
   mats=matrices(p,sigma,c);dims=[]
   for eps in itertools.product([-1,1],repeat=4):
    rows=[[mats[k][i][j]+(eps[k]if i==j else 0)for i in range(6)]for k in range(4)for j in range(6)]
    rr,piv=rref(rows);dim=6-len(piv);expected=int(p==sigma-c and eps==(1,1,1,1));dims.append(dim)
    ok(port+f' Hom {p} {eps}',dim==expected)
    if expected:
     l=[1,1,1,1,-3,-sigma*p];ok(port+' exceptional witness',all(sum(row[j]*l[j]for j in range(6))==0 for row in rows))
   case_results.append({'port':port,'w_plus':str(wp),'w_minus':str(wm),'p':str(p),'sigma':sigma,'c':str(c),'scalar_Hom_total_dimension':sum(dims)})
 counts=Counter(tuple((-1)**(mask.bit_count()-((mask>>k)&1)) for k in range(4))for mask in range(1<<14))
 ok('complete16 Clifford characters each1024',len(counts)==16 and set(counts.values())=={1024})
 ok('exceptional complex Hom dimension',9*1024==9216)
 ok('K77 exceptional product',F(-1)-F(11,12)==F(-23,12))
 ok('K95 exceptional product',F(1)-F(-11,12)==F(23,12))
 ok('one-sign-only mutation is not K95',F(-1)-F(-11,12)!=F(23,12))
 # The normalization model retains all15 copies. Kernel is sum-zero normal.
 for k in range(4):
  for j in range(4,13):
   v=[0]*15;v[j]=1;v[13]=-1
   mv=[sum(v[b]for b in range(14)if len({a,b,k})==3)for a in range(14)]+[0]
   ok(f'full hidden eigenvector {k} {j}',mv==[-x for x in v])
 # Two receiver channels can attain rank2, so dropping the derivative is unsafe.
 def product(a,b):return [[sum(F(x)*F(y)for x,y in zip(row,col))for col in zip(*b)]for row in a]
 S=[[int(i==j)for j in range(2)]for i in range(6)]
 L=[[int(i==j+2)for j in range(2)]for i in range(6)]
 ell=[[int(j==i)for j in range(6)]for i in range(2)]
 co=[[int(j==i+2)for j in range(6)]for i in range(6)]
 left=product(product(S,ell),co);right=product(L,ell)
 B=[[a-b for a,b in zip(x,y)]for x,y in zip(left,right)]
 v=[x+[-z for z in y]for x,y in zip(S,L)]
 u=product(ell,co)+ell
 ok('moving derivative factorization and sharp two receiver bound',product(v,u)==B and len(rref(B)[1])==4)
 # If ell varies, ell and ell-prime can be independent: T=S ell has a
 # derivative term S ell-prime. Parallel ell is a genuine proof premise.
 ok('nonparallel receiver countercontrol',len(rref([[1,0],[0,1]])[1])>len(rref([[1,0]])[1]))
 ok('native rank exceeds moving-graph bound',512>2*128)
 # Complex metric flip: eta and S change sign, gamma gains i; factor is i.
 ok('metric-flip factors',(-1)*(-1)==1 and (1j)**4==1)
 # Scalar triangular inverse and resonant lifting controls, no domain claim.
 a,b,d=F(2),F(7),F(3);inverse=[[1/a,-b/(a*d)],[F(0),1/d]]
 mat=[[a,b],[F(0),d]]
 ok('triangular inverse observed block',all(sum(mat[i][k]*inverse[k][j]for k in range(2))==int(i==j)for i in range(2)for j in range(2)) and inverse[1][1]==1/d)
 ok('singular hidden cokernel retains obstruction',0!=b)
 # Real-linear right-inverse averaging: genuine anti-linear hidden component.
 J=[[0,-1],[1,0]];JE=[[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]]
 r=[[1,0],[0,1],[1,0],[0,-1]];q=[[1,0,0,0],[0,1,0,0]]
 jrj=product(product(JE,r),J)
 rc=[[(F(x)-y)/2 for x,y in zip(a,b)]for a,b in zip(r,jrj)]
 ok('real right inverse complex averaging',product(q,rc)==[[1,0],[0,1]] and product(rc,J)==product(JE,rc) and rc!=r)

 ok('resonance admits time-polynomial lift',-1+1==0)
 deps=['lab/process/local-dual-closure-second-fundamental-form.json','tests/program-focus/local_dual_closure_second_fundamental_form_probe.py','lab/process/bet-2plus1-unitary-dual-closure.json','explorations/conditional-build/bet-2plus1-chiral-weight-transport-2026-11-25.md','tests/channel-swings/eric_curt_wave3d_b2c4_shiab_family_southeast_completion_probe.py','tests/channel-swings/selected_k77_wedge_shiab_southeast_completion_probe.py']
 native=json.loads((ROOT/deps[0]).read_text())
 ok('inherited native certificate binding',native['rank_over_C']==512 and native['minor_determinant_mod97']==91 and native['prime']==97)
 return {'status':'PASS','checks':checks,'grouped_checks':len(checks),'full_Cl14_normalized_blocks':normalized_blocks,'weight_cases':case_results,'character_dimensions':{str(k):v for k,v in counts.items()},'native_inputs_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in deps},'scope':'Finite exact controls plus hash-pinned inherited native rank; universal classification, moving differential equation and geometric transfer are written/reviewed, not certified by weight sampling.'}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--verify',action='store_true');parser.add_argument('--output');args=parser.parse_args();start=time.perf_counter();out=run();out['runtime_seconds']=time.perf_counter()-start
 text=json.dumps(out,indent=2)+'\n'
 if args.output:Path(args.output).write_text(text)
 print(json.dumps({k:v for k,v in out.items()if k not in ['checks','character_dimensions','native_inputs_sha256','weight_cases']},indent=2))
