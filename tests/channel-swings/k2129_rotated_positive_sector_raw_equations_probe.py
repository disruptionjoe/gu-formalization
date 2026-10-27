"""Exact all-grade raw32 derivative obstruction; no float ranks. Requires numpy, sympy, python-flint."""
from pathlib import Path
import sys,json,time
import numpy as np
import sympy as s
from fractions import Fraction as F
G=Path(__file__).resolve().parents[2]
import k2123_same_current_potential_dynamics_probe as n
q=n.q;cs,m,fc,t,z,r,p=n.native();p=q.add((F(1,4),q.mul(q.add((1,q.I),(s.I,t)),q.add((1,q.I),(F(3,5),r),(s.I*F(4,5),q.mul(z,r))))));J=[]
import k1967_paired_raw_coefficient_observation_probe as old
J,_,_,dj,_=old.build();Fi={(j,i):1/v for (i,j),v in J[14].items()};Jn=[q.mul(a,Fi) for a in J];DJ=[q.mul({(i,j):v for i in range(128) for j,v in dj(a*128+i).items()},Fi) for a in range(15)]
idx=np.arange(128)
def mono(A,scale=1):
 flips={i^j for i,j in A};assert len(flips)==1;f=flips.pop();vals=[A.get((i,i^f),0)*scale for i in range(128)];assert all(v==int(v) for v in vals);return f,np.array(vals,dtype=np.int64)
def mul(A,B):return A[0]^B[0],A[1]*B[1][idx^A[0]]
def trans(A):return A[0],A[1][idx^A[0]]
def add(As):
 f=As[0][0];assert all(a[0]==f for a in As);return f,sum((a[1] for a in As),np.zeros(128,dtype=np.int64))
gs=[mono(q.gamma(k)) for k in range(14)];vs=mono(q.J);js=[mono(a,44) for a in Jn];ds=[mono(a,44) for a in DJ];B=mono(q.B);ws=3+vs[1]
Pn=q.mul(J[14],q.mul(p,Fi));Zn=q.mul(J[14],q.mul(z,Fi))
# P is complex, encode real/imaginary integer numerators over common denominator.
den=s.ilcm(*[s.denom(s.re(v)) for v in Pn.values()],*[s.denom(s.im(v)) for v in Pn.values()]);den=int(den);Pr=np.zeros((128,128),dtype=np.int64);Pi=Pr.copy()
for (i,j),v in Pn.items():Pr[i,j]=int(s.re(v)*den);Pi[i,j]=int(s.im(v)*den)
# A common scalar norm factor cancels: Fi*Fi is diagonal. Exact current positive norm is checked in original coordinates later.
metric=q.mul(n.adj(Fi),Fi);md=int(s.ilcm(*[s.denom(v) for v in metric.values()]));gr=np.array([int(metric.get((i,i),0)*md) for i in range(128)],dtype=np.int64);assert all(i==j for i,j in metric)
def dense(a):
 out=np.zeros((128,128),dtype=np.int64);out[idx,idx^a[0]]=a[1];return out
# Normalize rows by common scalar gcd later. Use sparse P multiplication via four permutation diagonals.
def rightP(A):
 outR=np.zeros_like(A);outI=np.zeros_like(A)
 for flip in {i^j for i,j in Pn}:
  rr=Pr[idx,idx^flip];ii=Pi[idx,idx^flip]
  outR[:,idx^flip]+=A*rr[None,:];outI[:,idx^flip]+=A*ii[None,:]
 return outR,outI

def mm(a,b):
 bound=a.shape[1]*int(np.max(np.abs(a)))*int(np.max(np.abs(b)))
 assert bound < 2**50, ('int64 bound',bound)
 return a@b
assert DJ[0]==q.I
assert metric==q.add((F(1225,121),q.I))
# Pre-execution elementary-chain bounds: |gamma|,|volume|,|B|<=1;
# |44J|,|44DJ|<=44; |y|<=16 below. Hence |A|<=16, |4Omega|<=64,
# |T|<=9856, |U|<=11264, |raw numerator|<=588544<2**20,
# |lower numerator|<=39424, and |return numerator|<2**27.
# Rotated P has eight shifts, numerator absolute value<=5 and denominator20.
# Thus rightP<2**33; leakage sums<2**40; conservation with metric1225
# and eight second-projector terms<2**49. Dense products receive a stricter
# actual-input bound below before each int64 matrix multiplication. Dense products
# also receive the independent bound in mm before execution.
assert den==20 and set(map(int,gr))=={1225}
assert max(int(np.max(np.abs(Pr))),int(np.max(np.abs(Pi))))<=5
assert all(int(np.max(np.abs(a[1])))<=1 for a in gs+[vs,B])
assert all(int(np.max(np.abs(a[1])))<=44 for a in js+ds)

def system(direction):
 rec=json.loads((G/'lab/process/k2028-all-grade-raw-common-form.json').read_text());
 Ztarget=q.mul(J[14],q.mul(q.mul(z,([q.I]+cs)[direction]),Fi)); flips={i^j for i,j in Ztarget};assert len(flips)==1;f0=flips.pop();coset={f0^x for x in [0,1,62,63,15,14,49,48]}

 labels=[(im,g['flip'],mask,y) for im,br in [(False,rec),(True,rec['complex_hermitian_branch'])] for g in br['groups'] if g['flip'] in coset for mask,y in g['labels']]
 if False:
  expected=[]
  from math import gcd
  for mask in range(1<<14):
   fl=64
   for k in range(14):
    if mask>>k&1:fl ^= gs[k][0]
   if fl not in coset:continue
   deg=mask.bit_count();assert 3<=deg<=11
   sig=(-1)**(deg*(deg+1)//2);inside=13-deg;outside=-(deg-1);gg=gcd(inside,outside)
   yy=[(inside if mask>>k&1 else outside)//gg for k in range(14)]
   expected.append((sig==-1,mask,tuple(yy)))
  assert len(expected)==512==len(labels)
  bymask={(im,mask):yy for im,ff,mask,yy in labels}
  for im,mask,yy in expected:
   got=bymask[im,mask];ratio=F(got[0],yy[0]);assert ratio and all(F(a)==ratio*b for a,b in zip(got,yy))
 assert all(max(map(abs,y))<=16 for im,f,mask,y in labels)
 # For every candidate independently construct all raw outputs as signed monomials.
 def outputs(mask,y,im):
  X=mono(q.blade(tuple(k for k in range(14) if mask>>k&1)))
  AA=[(zz[0],q.ETA[k]*y[k]*zz[1]) for k in range(14) for zz in [mul(gs[k],X)]]
  Om=[(a[0],ws*a[1]) for a in AA]
  TT=[add([mul(mul(gs[c],AA[k]),js[c]) for c in range(14)]) for k in range(14)]
  out=[]
  for a in range(14):
   terms=[]
   for k in range(14):
    if k==a:continue
    u=TT[k][1]-mul(mul(gs[a],AA[k]),js[a])[1]-mul(mul(gs[k],AA[k]),js[k])[1]
    terms.append(mul(gs[k],(TT[k][0],u)))
   zz=mul(gs[a],add(terms));assert zz[0]==Om[a][0];out.append((zz[0],4*q.ETA[a]*zz[1]+44*Om[a][1]))
  low=add([(zz[0],q.ETA[k]*zz[1]) for k in range(14) for zz in [mul(mul(mul(B,trans(Om[k])),B),js[k])]])
  if im:low=(low[0],-low[1])
  return out+[low]

 # Two angle-independent coefficient kernels: Omega_k=(2i/3)I.
 # Reconstruct their stored basis coordinates and all15 normalized output rows.
 universal=[]
 for kk,target,masks,coeffs in ([(0,0,[1,16382],[F(1),F(-1,3)]),(7,1,[128,16255],[F(1),F(-1,3)])] if direction==0 else [(8,2,[256,16127],[F(1),F(1,3)]),(9,3,[512,15871],[F(1),F(-1,3)])]):
  yy=[int(k==kk) for k in range(14)]
  selected=[next(row for row in labels if row[0] and row[2]==mask and row[3]==yy) for mask in masks]
  om=q.add(*[(co*F(q.ETA[kk],4),q.mul(q.add((3,q.I),(1,q.J)),q.mul(q.gamma(kk),q.blade(tuple(k for k in range(14) if mask>>k&1))))) for mask,co in zip(masks,coeffs)])
  assert om==q.add((F(2,3),q.I)),('universal Omega',kk)
  cn=q.mul(J[14],q.mul(([q.I]+cs)[target],Fi))
  for aa in range(15):
   raw=[]
   for row,co in zip(selected,coeffs):
    oo=outputs(row[2],row[3],True)[aa]
    raw.append((co,{(i,i^oo[0]):F(int(oo[1][i]),176) for i in range(128) if oo[1][i]}))
   assert q.add(*raw)==q.add((F(2,3),q.mul(DJ[aa],cn))),('universal raw return',kk,aa)
  universal.append(dict(raw_index=kk,induced_direction=target,masks=masks,coefficients=list(map(str,coeffs))))
 # Independent direct raw contraction on four full output blocks for one real and one imaginary column.
 for imag in [False,True]:
  _,ff,mask,yy=next(row for row in labels if row[0]==imag)
  X=q.blade(tuple(k for k in range(14) if mask>>k&1))
  om=[q.add((F(q.ETA[k]*yy[k],4),q.mul(q.add((3,q.I),(1,q.J)),q.mul(q.gamma(k),X)))) for k in range(14)]
  fast=outputs(mask,yy,imag)
  for a in [0,3,7,14]:
   terms=[]
   if a==14:
    for k in range(14):terms.append((q.ETA[k]*(-1 if imag else 1),q.mul(q.B,q.mul(q.tr(om[k]),q.mul(q.B,Jn[k])))))
   else:
    terms=[(1,q.mul(om[a],Jn[14]))]
    for k in range(14):
     if k==a:continue
     for c in range(14):
      if c not in [a,k]:terms.append((q.ETA[a],q.mul(q.blade((a,k,c)),q.mul(q.W,q.mul(om[k],Jn[c])))))
   direct=q.add(*terms);f,vals=fast[a]
   expected={(i,i^f):F(int(vals[i]),176) for i in range(128) if vals[i]}
   assert direct==expected, ('raw contraction crosscheck',direction,imag,a)
 # Collect sparse vector conditions; only rows ever nonzero are materialized.
 cols=[];start=time.time()
 for ix,(im,f,mask,y) in enumerate(labels):
  outs=outputs(mask,y,im);M=outs[0];assert M[0]==f;blocks=[]
  assert max(int(np.max(np.abs(o[1]))) for o in outs)<2**30
  for a,o in enumerate(outs):
   dm=mul(ds[a],M);assert o[0]==dm[0];D=(o[0],44*o[1]-dm[1]);dr,di=rightP(dense(D));blocks += [dr,di] if not im else [-di,dr]
  # leakage equation (I-P) A P = -i ZP/2, numerators over176 den².
  mr,mi=rightP(dense(M));lr=den*mr-mm(Pr,mr)+mm(Pi,mi);li=den*mi-mm(Pr,mi)-mm(Pi,mr)
  if im:lr,li=-li,lr
  blocks += [lr,li]
  # Original norm conservation: P* G A P + adjoint =0. normalized metric.
  ar=mr*gr[:,None];ai=mi*gr[:,None]
  er=mm(Pr.T,ar)+mm(Pi.T,ai);ei=mm(Pr.T,ai)-mm(Pi.T,ar)
  if im:er,ei=-ei,er
  er,ei=er+er.T,ei-ei.T;blocks += [er,ei]
  vec=np.concatenate([b.ravel() for b in blocks]);nz=np.flatnonzero(vec);cols.append({int(i):int(vec[i]) for i in nz})


 targets=[0,1] if direction==0 else [2,3]
 rhslist=[]
 for target in targets:
  Ztarget=q.mul(J[14],q.mul(q.mul(z,([q.I]+cs)[target]),Fi))
  ZZ=np.zeros((128,128),dtype=np.int64)
  for ij,vv in Ztarget.items():assert vv==int(vv);ZZ[ij]=int(vv)
  zpr,zpi=rightP(ZZ);br=88*den*zpi;bi=-88*den*zpr
  rhs={30*128*128+i:int(v) for i,v in enumerate(br.ravel()) if v};rhs.update({31*128*128+i:int(v) for i,v in enumerate(bi.ravel()) if v});rhslist.append(rhs)
 rows=sorted(set().union(*(set(r) for r in rhslist),*(set(c) for c in cols)))
 A=np.zeros((len(rows),len(cols)+len(targets)),dtype=np.int64);ri={r:i for i,r in enumerate(rows)}
 for j,c in enumerate(cols):
  for r0,val in c.items():A[ri[r0],j]=val
 for j,rhs in enumerate(rhslist):
  for r0,val in rhs.items():A[ri[r0],len(cols)+j]=val
 from math import gcd
 def primitive(array,origins):
  unique={}
  for origin,row in zip(origins,array):
   vals=list(map(int,row));gg=0
   for vv in vals:gg=gcd(gg,vv)
   if gg:
    if next(vv for vv in vals if vv)<0:gg=-gg
    unique.setdefault(tuple(vv//gg for vv in vals),dict(original_row=int(origin),divisor=int(gg)))
  return list(unique),list(unique.values())
 from flint import fmpq_mat,nmod_mat
 def certificate(payload):
  E,provenance=payload
  MA=fmpq_mat([r0[:len(cols)] for r0 in E]);RA,rankA=MA.rref()
  aug=fmpq_mat(E);RR,rankAug=aug.rref()
  # Verify a full rational right-kernel basis as an exact rank upper certificate.
  piv=[]
  for i in range(rankA):piv.append(next(j for j in range(len(cols)) if RA[i,j]))
  free=[j for j in range(len(cols)) if j not in piv];kernel=[]
  for j in free:
   vv=[s.Rational(0)]*len(cols);vv[j]=s.Rational(1)
   for i,k in enumerate(piv):vv[k]=-s.Rational(str(RA[i,j]))
   assert all(sum(s.Rational(int(a))*b for a,b in zip(row[:len(cols)],vv))==0 for row in E)
   kernel.append({str(k):str(v) for k,v in enumerate(vv) if v})
  # Modular lower ranks independently agree; an augmented pivot minor is an exact nonzero witness.
  prime=101;transposed=nmod_mat([list(col) for col in zip(*E)],prime);mr,rankMod=transposed.rref()
  assert rankMod==rankAug
  selected=[next(j for j in range(mr.ncols()) if mr[i,j]) for i in range(rankMod)]
  colmat=nmod_mat([E[i] for i in selected],prime);cr,rank2=colmat.rref();assert rank2==rankAug
  selectedcols=[next(j for j in range(cr.ncols()) if cr[i,j]) for i in range(rank2)]
  minor=nmod_mat([[E[i][j] for j in selectedcols] for i in selected],prime);det=int(minor.det());assert det
  assert nmod_mat([r0[:len(cols)] for r0 in E],prime).rank()==rankA
  return dict(rows=len(E),coefficient_rank=rankA,augmented_rank=rankAug,rhs_count=len(targets),nullity=len(free),kernel=kernel,minor_prime=prime,minor_det=det,minor_rows=selected,minor_columns=selectedcols,minor_original_rows=[provenance[i]["original_row"] for i in selected],minor_fixed_row_divisors=[provenance[i]["divisor"] for i in selected],equations_sha256=__import__('hashlib').sha256(json.dumps(E,separators=(',',':')).encode()).hexdigest())
 exact=certificate(primitive(A,rows))
 upper=certificate(primitive(A[[i for i,r0 in enumerate(rows) if r0//(128*128) not in [28,29]],:],[r0 for r0 in rows if r0//(128*128) not in [28,29]]))
 print('direction',targets,'columns',len(cols),'ranks',exact['coefficient_rank'],exact['augmented_rank'],'without lower',upper['coefficient_rank'],upper['augmented_rank'],flush=True)
 return dict(directions=targets,coset=sorted(coset),columns=len(cols),universal_kernels=universal,full=exact,without_lower=upper)

def canonical(matrix):
 return {key:v for key,w in matrix.items() if (v:=s.expand(w))!=0}

def main():
 import argparse,hashlib
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 systems=[system(d) for d in [0,2]]
 ck={'rotated-projector':canonical(q.mul(p,p))==canonical(p) and n.adj(p)==p and n.tr(p)==32,'same-positive-current':canonical(q.mul(p,q.mul(q.add((s.I,fc)),p)))==canonical(q.add((F(9,280),p))),'two-universal-kernels-per-coset':all(len(x['universal_kernels'])==2 for x in systems)}
 for i,x in enumerate(systems):
  for key in ['full','without_lower']:
   ck[f'joint-rank-{i}-{key}']=x[key]['coefficient_rank']==x['columns']-2 and x[key]['augmented_rank']==x['columns']
   ck[f'fixed-original-minor-{i}-{key}']=len(x[key]['minor_original_rows'])==x['columns'] and all(x[key]['minor_fixed_row_divisors'])
 # Real input faults: wrong trigonometric normalization, phase, and raw kernel coefficient.
 bad={}
 for tag,rr in [('angle-normalization',q.add((F(4,5),r),(s.I*F(4,5),q.mul(z,r)))),('rotation-reality',q.add((F(3,5),r),(F(4,5),q.mul(z,r))))]:
  wrong=q.add((F(1,4),q.mul(q.add((1,q.I),(s.I,t)),q.add((1,q.I),(1,rr)))))
  failures=[]
  if canonical(q.mul(wrong,wrong))!=canonical(wrong):failures.append('projector equation')
  if n.adj(wrong)!=wrong:failures.append('Hermitian projector')
  assert failures;bad[tag]=failures
 om=q.add((F(q.ETA[0],4),q.mul(q.add((3,q.I),(1,q.J)),q.mul(q.gamma(0),q.gamma(0)))))
 assert om!=q.add((F(2,3),q.I));bad['omit-dual-grade-coefficient']=['actual Omega differs from2i/3 identity']
 assert all(ck.values()),ck
 inputs=['lab/process/k2028-all-grade-raw-common-form.json','tests/channel-swings/k2126_positive_sector_raw_coefficients_probe.py','tests/channel-swings/k2123_same_current_potential_dynamics_probe.py','tests/channel-swings/k1967_paired_raw_coefficient_observation_probe.py']
 result=dict(result_id='K2129',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=ck,fault_failures=bad,systems=systems,angle={'cos':'3/5','sin':'4/5'},scope='Exact non-special-angle ranks plus universal homogeneous raw kernels. Trigonometric-minor and C1 rigidity argument is written in note; exceptional pointwise jets are not classified.',inputs={p:hashlib.sha256((G/p).read_bytes()).hexdigest() for p in inputs})
 out=G/'lab/process/k2129-rotated-positive-sector-raw-equations.json'
 if args.write:out.write_text(json.dumps(result,indent=2)+'\n')
 else:assert result==json.loads(out.read_text())
 print('PASS K2129',len(ck),'exact certificate checks;',len(bad),'genuine input faults')
if __name__=='__main__':main()
