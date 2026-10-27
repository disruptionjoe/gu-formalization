"""Exact all-grade raw32 derivative obstruction; no float ranks. Requires numpy, sympy, python-flint."""
from pathlib import Path
import sys,json,time
import numpy as np
import sympy as s
from fractions import Fraction as F
G=Path(__file__).resolve().parents[2]
import k2123_same_current_potential_dynamics_probe as n
q=n.q;cs,m,fc,t,z,r,p=n.native();J=[]
import k2132_conserving_positive_sector_classification_probe as nf
Q=nf.frame(c=1,sh=0)[6];E=nf.frame(c=1,sh=0)[7]
def target(mu):
 return nf.add((F(-1,2),nf.mul(Q,nf.mul(E,nf.mul(nf.add((1,q.I),(1,r)),([q.I]+cs)[mu])))))
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
Pn=q.mul(J[14],q.mul(p,Fi));Zn=q.mul(J[14],q.mul(z,Fi));assert set(map(str,Pn.values()))=={'1/4','-1/4','I/4','-I/4'}
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
# Projector shifts have four unit numerators: rightP<2**29; denominator4
# and metric1225 then keep all additions/scalings below2**42. Dense products
# also receive the independent bound in mm before execution.
assert den==4 and set(map(int,gr))=={1225}
assert all(int(np.max(np.abs(a[1])))<=1 for a in gs+[vs,B])
assert all(int(np.max(np.abs(a[1])))<=44 for a in js+ds)

def system(direction):
 rec=json.loads((G/'lab/process/k2028-all-grade-raw-common-form.json').read_text());
 targets=[0,1] if direction==0 else [2,3]
 target_native=[nf.mul(J[14],nf.mul(target(mu),Fi)) for mu in targets]
 coset={fl^h for T in target_native for i,j in T for fl in [i^j] for h in [0,1,62,63]}

 labels=[(im,g['flip'],mask,y) for im,br in [(False,rec),(True,rec['complex_hermitian_branch'])] for g in br['groups'] if g['flip'] in coset for mask,y in g['labels']]
 # All common-H basis labels are inherited from the exact K2028 exhaustion.
 # Their full target-coset union is selected; do not assume old circle cardinality.
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


 rhslist=[]
 for target_matrix in target_native:
  br=np.zeros((128,128),dtype=np.int64);bi=br.copy()
  for ij,vv in target_matrix.items():
   vr=s.re(vv)*176*den*den;vi=s.im(vv)*176*den*den
   assert vr==int(vr) and vi==int(vi)
   br[ij]=int(vr);bi[ij]=int(vi)
  rhs={30*128*128+i:int(v) for i,v in enumerate(br.ravel()) if v};rhs.update({31*128*128+i:int(v) for i,v in enumerate(bi.ravel()) if v});rhslist.append(rhs)
 rows=sorted(set().union(*(set(r) for r in rhslist),*(set(c) for c in cols)))
 A=np.zeros((len(rows),len(cols)+len(targets)),dtype=np.int64);ri={r:i for i,r in enumerate(rows)}
 for j,c in enumerate(cols):
  for r0,val in c.items():A[ri[r0],j]=val
 for j,rhs in enumerate(rhslist):
  for r0,val in rhs.items():A[ri[r0],len(cols)+j]=val
 from math import gcd
 def primitive(array):
  unique={}
  for row in array:
   vals=list(map(int,row));gg=0
   for vv in vals:gg=gcd(gg,vv)
   if gg:
    if next(vv for vv in vals if vv)<0:gg=-gg
    unique[tuple(vv//gg for vv in vals)]=None
  return list(unique)
 from flint import fmpq_mat,nmod_mat
 def certificate(E):
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
  return dict(rows=len(E),coefficient_rank=rankA,augmented_rank=rankAug,rhs_count=len(targets),nullity=len(free),kernel=kernel,minor_prime=prime,minor_det=det,minor_rows=selected,minor_columns=selectedcols,equations_sha256=__import__('hashlib').sha256(json.dumps(E,separators=(',',':')).encode()).hexdigest())
 exact=certificate(primitive(A))
 upper=certificate(primitive(A[[i for i,r0 in enumerate(rows) if r0//(128*128) not in [28,29]],:]))
 print('direction',targets,'columns',len(cols),'ranks',exact['coefficient_rank'],exact['augmented_rank'],'without lower',upper['coefficient_rank'],upper['augmented_rank'],flush=True)
 return dict(directions=targets,coset=sorted(coset),columns=len(cols),full=exact,without_lower=upper)

def transport(fault=None):
 cs,m,S,tt,z,r,Q,E,Y,dY,c,sh=nf.frame(c=F(5,3),sh=F(4,3))
 JJ={}
 for k,bl in enumerate(json.loads((G/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks']):
  for (rr,cc),vv in nf.mul(n.dec(bl['basis']),n.dec(bl['section'])).items():JJ[bl['coordinates'][rr],4*k+cc]=vv
 gram=nf.mul(n.adj(JJ),JJ);diag=nf.add((1,gram),(2*c*c-1,nf.mul(r,nf.mul(gram,r))))
 assert all(i==j for i,j in diag) and all(v>0 for v in diag.values())
 inv={(i,i):1/diag[i,i] for i in range(128)}
 X=nf.mul(JJ,Y);L=nf.mul(inv,nf.mul(E,n.adj(X)))
 if fault=='left-inverse-scale':L=nf.add((2,L))
 jet=nf.add((2,q.I),(3,cs[0]),(-1,cs[1]),(4,cs[2]));qa=nf.add((5,q.I),(-2,cs[0]),(3,cs[1]),(1,cs[2]))
 AP=nf.add((7,nf.mul(m,Y)),(s.I,nf.mul(qa,Y)),((-1 if fault!='transport-sign' else 1),nf.mul(dY,jet)))
 N=nf.mul(q.raw(0),nf.mul(JJ,AP));HN=nf.mul(q.H,N);CC=nf.mul(n.adj(X),HN);LX=nf.mul(L,X)
 want=nf.add((-2*s.I*F(9,280)*7,nf.mul(m,E)),(2*F(9,280),nf.mul(qa,E)))
 # Sign error leaves compressed compatibility intact: test the full moving equation separately.
 ck={'actual-noncircle-left-inverse':LX==E,'native-Gram-formula':nf.mul(n.adj(X),X)==nf.mul(diag,E),'compressed-common-H-compatible':CC==n.adj(CC) and CC==want}
 QX=nf.add((1,nf.mul(HN,LX)),(1,nf.mul(n.adj(L),nf.mul(n.adj(N),nf.mul(q.H,X)))),((-1 if fault!='omit-subtraction' else 0),nf.mul(n.adj(L),nf.mul(CC,LX))))
 ck['full1920-factor-interpolation']=nf.mul(q.H,QX)==N
 ck['moving-equation-cancellation']=nf.add((1,AP),(1,nf.mul(dY,jet)))==nf.add((7,nf.mul(m,Y)),(s.I,nf.mul(qa,Y)))
 return ck

def main():
 import argparse,hashlib
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 systems=[system(d) for d in [0,2]]
 ck=transport();bad={}
 for f in ['left-inverse-scale','transport-sign','omit-subtraction']:
  bad[f]=[k for k,v in transport(f).items() if not v];assert bad[f];print('[FAIL detected]',f,bad[f])
 for i,rec in enumerate(systems):
  ck['joint-target-obstruction-'+str(i)]=rec['full']['augmented_rank']-rec['full']['coefficient_rank']==2
  ck['upper-only-obstruction-'+str(i)]=rec['without_lower']['augmented_rank']-rec['without_lower']['coefficient_rank']==2
 assert all(ck.values()),ck
 inputs=['lab/process/k2028-all-grade-raw-common-form.json','tests/channel-swings/k2132_conserving_positive_sector_classification_probe.py','tests/channel-swings/k2126_positive_sector_raw_coefficients_probe.py','lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1967-paired-raw-coefficient-observation.json']
 out=dict(result_id='K2134',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=ck,fault_failures=bad,systems=systems,scope='Actual noncircle hyperbolic family: changed-upper common-H transport at all real u by proof; raw first-jet obstruction tested at u=0 only. Raw class completeness inherited K2028, not re-exhausted.',inputs={x:hashlib.sha256((G/x).read_bytes()).hexdigest() for x in inputs})
 path=G/'lab/process/k2134-noncircle-current-transport.json'
 if args.write:path.write_text(json.dumps(out,indent=2)+'\n')
 else:assert json.loads(path.read_text())==out
 print('PASS K2134',len(ck),'checks;',len(bad),'genuine faults')
if __name__=='__main__':main()
