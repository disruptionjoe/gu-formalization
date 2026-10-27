"""First derivative of native raw residual; exact Q and finite-field elimination."""
from pathlib import Path
import json,hashlib,argparse,time
from fractions import Fraction as F
from math import lcm,gcd
import numpy as np
import sympy as s
from flint import fmpq_mat,nmod_mat
import k2141_full_graph_raw_tangent_probe as b
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2147-moving-raw-kernel-prolongation.json'
DEPS=['lab/process/k2144-raw-neighborhood-rank-budget.json','lab/process/k2141-full-graph-raw-tangent.json','lab/process/k2028-all-grade-raw-common-form.json','tests/channel-swings/k2141_full_graph_raw_tangent_probe.py','tests/channel-swings/k2134_noncircle_current_transport_probe.py','tests/channel-swings/k2132_conserving_positive_sector_classification_probe.py']
x=b.b;q=b.q;nf=x.nf;mul=nf.mul;add=nf.add;adj=b.n.adj
cs,m,S,t,z,r,Q,E,Y,dy,c,sh=nf.frame(c=1,sh=0)
P=x.p;Pd=add((F(1,2),mul(mul(Q,E),adj(Y))),(F(1,2),mul(Y,adj(mul(Q,E)))))
assert adj(Pd)==Pd and add((1,mul(Pd,P)),(1,mul(P,Pd)))==Pd
Pdn=mul(x.J[14],mul(Pd,x.Fi));dr=np.zeros((128,128),dtype=np.int64);di=dr.copy()
for ij,v in Pdn.items():
 assert s.re(v)*x.den==int(s.re(v)*x.den) and s.im(v)*x.den==int(s.im(v)*x.den)
 dr[ij]=int(s.re(v)*x.den);di[ij]=int(s.im(v)*x.den)
def rightD(A):return x.mm(A,dr),x.mm(A,di)
def derivative(label,fault=None):
 im,f,mask,y=label;outs=b.outputs(mask,y,im);M=outs[0];blocks=[]
 for a,o in enumerate(outs):
  dm=x.mul(x.ds[a],M);D=(o[0],44*o[1]-dm[1]);ar,ai=rightD(x.dense(D));blocks += [ar,ai] if not im else [-ai,ar]
 blocks += [np.zeros((128,128),dtype=np.int64)]*2
 mr,mi=x.rightP(x.dense(M));nr,ni=rightD(x.dense(M))
 lr=x.den*nr-x.mm(x.Pr,nr)+x.mm(x.Pi,ni)
 li=x.den*ni-x.mm(x.Pr,ni)-x.mm(x.Pi,nr)
 if fault!='drop_left_derivative':
  lr-=x.mm(dr,mr)-x.mm(di,mi);li-=x.mm(dr,mi)+x.mm(di,mr)
 if im:lr,li=-li,lr
 blocks += [lr,li]
 ar,ai=mr*x.gr[:,None],mi*x.gr[:,None];br,bi=nr*x.gr[:,None],ni*x.gr[:,None]
 er=x.mm(dr.T,ar)+x.mm(di.T,ai)+x.mm(x.Pr.T,br)+x.mm(x.Pi.T,bi)
 ei=x.mm(dr.T,ai)-x.mm(di.T,ar)+x.mm(x.Pr.T,bi)-x.mm(x.Pi.T,br)
 if im:er,ei=-ei,er
 blocks += [er+er.T,ei-ei.T]
 vec=np.concatenate([v.ravel() for v in blocks]);return {int(i):int(vec[i]) for i in np.flatnonzero(vec)}
def combine(labels,vec,fn):
 den=lcm(*[F(v).denominator for v in vec.values()]);out={}
 for j,c in vec.items():
  cc=int(F(c)*den)
  for k,v in fn(labels[int(j)]).items():out[k]=out.get(k,0)+cc*v
 return {k:v for k,v in out.items() if v}
def independent_derivative(labels,vec):
 den=lcm(*[F(v).denominator for v in vec.values()]);outs=[{} for _ in range(14)]
 for jj,cc in vec.items():
  im,ff,mask,y=labels[int(jj)];coef=F(cc)*den*(s.I if im else 1)/176
  for a,(flip,vals) in enumerate(b.outputs(mask,y,im)):
   outs[a]=add((1,outs[a]),(coef,{(i,i^flip):int(v) for i,v in enumerate(vals) if v}))
 M=outs[0];Pn=x.Pn;In=add((1,q.I),(-1,Pn))
 mats=[mul(add((1,outs[a]),(-1,mul(x.DJ[a],M))),Pdn) for a in range(14)]+[{},mul(In,mul(M,Pdn))]
 mats[15]=add((1,mats[15]),(-1,mul(Pdn,mul(M,Pn))))
 dcur=add((1,mul(Pdn,mul(M,Pn))),(1,mul(Pn,mul(M,Pdn))))
 mats += [add((1,dcur),(1,adj(dcur)))]
 out={}
 for a,mat in enumerate(mats):
  scale=176*44*x.den if a<14 else 176*x.den*x.den*(1225 if a==16 else 1)
  for (i,j),v in mat.items():
   for part,w in enumerate([s.re(v),s.im(v)]):
    value=s.simplify(w*scale);assert value==int(value)
    if value:out[(2*a+part)*128*128+i*128+j]=int(value)
 return out
sub=[0,1,62,63]
def rowcoset(row):
 block,pos=divmod(row,128*128);f=pos//128 ^ pos%128
 if block<28:f ^=x.ds[block//2][0]
 return min(f^h for h in sub)
def rankmat(cols):
 rows=sorted(set().union(*(set(v) for v in cols)));unique={}
 for row in rows:
  vals=[v.get(row,0) for v in cols];g=0
  for v in vals:g=gcd(g,v)
  if g:
   if next(v for v in vals if v)<0:g=-g
   unique[tuple(v//g for v in vals)]=None
 eq=list(unique);return eq

def main():
 start=time.time();rec=json.loads((ROOT/DEPS[0]).read_text())['localized_kernel'];labels=rec['labels'];extras=[v['coefficients'] for v in rec['extra_maps']]
 D=[combine(labels,v,derivative) for v in extras];assert all(D)
 assert all(independent_derivative(labels,v)==d for v,d in zip(extras,D)), 'independent derivative product check'
 affected=sorted({rowcoset(k) for d in D for k in d});print('DERIVATIVE COSETS',affected,flush=True)
 bank=json.loads((ROOT/DEPS[2]).read_text());alllabels=[(im,g['flip'],mask,y) for im,br in [(False,bank),(True,bank['complex_hermitian_branch'])] for g in br['groups'] for mask,y in g['labels']]
 ts=b.targets();systems=[];shared=[]
 # Each affected coset is complete; shared target labels retained in final constraints.
 for co in affected:
  labs=[v for v in alllabels if min(v[1]^h for h in sub)==co];cols=[b.column(*v) for v in labs]
  assert all(rowcoset(k)==co for col in cols for k in col)
  tids=[j for j,tg in enumerate(ts) if any(rowcoset(k)==co for k in tg['rhs'])]
  tc=[{k:v for k,v in ts[j]['rhs'].items() if rowcoset(k)==co} for j in tids]
  dc=[{k:v for k,v in d.items() if rowcoset(k)==co} for d in D]
  eq=rankmat(cols+tc+dc);nr=len(cols);nt=len(tc)
  A=fmpq_mat([row[:nr] for row in eq]);AT=fmpq_mat([row[:nr+nt] for row in eq]);AD=fmpq_mat([row[:nr]+row[-3:] for row in eq]);full=fmpq_mat(eq)
  ranks=[A.rank(),AT.rank(),AD.rank(),full.rank()]
  assert [nmod_mat([row[:nr] for row in eq],101).rank(),nmod_mat([row[:nr+nt] for row in eq],101).rank(),nmod_mat([row[:nr]+row[-3:] for row in eq],101).rank(),nmod_mat(eq,101).rank()]==ranks
  rr,rank=full.rref()
  for i in range(ranks[0],rank):
   assert all(rr[i,j]==0 for j in range(nr));d={tids[j]:str(rr[i,nr+j]) for j in range(nt) if rr[i,nr+j]}
   d.update({1280+j:str(rr[i,nr+nt+j]) for j in range(3) if rr[i,nr+nt+j]});shared.append(d)
  systems.append(dict(coset=co,raw_columns=nr,target_columns=nt,rows=len(eq),ranks_A_AT_AD_ATD=ranks,equations_sha256=hashlib.sha256(json.dumps(eq,separators=(',',':')).encode()).hexdigest()))
  print('SYSTEM',systems[-1],time.time()-start,flush=True)
 mat=fmpq_mat([[row.get(j,'0') for j in range(1283)] for row in shared]);target=fmpq_mat([[row.get(j,'0') for j in range(1280)] for row in shared]);k=mat.rank()-target.rank()
 assert k==3 and systems[1]['ranks_A_AT_AD_ATD']==[519,559,522,562], 'clean prolongation rank failed'
 # Full independent native differential identities, not finite-difference ranks.
 ck={'independent_native_derivative_products':True,'selfadjoint_projector_derivative':adj(Pd)==Pd,'projector_product_rule':add((1,mul(Pd,P)),(1,mul(P,Pd)))==Pd,'three_base_vectors_are_homogeneous':all(not combine(labels,v,lambda z:b.column(*z)) for v in extras),'all_derivative_vectors_nonzero':all(D),'global_target_ids_coupled':mat.ncols()==1283,'exact_modular_ranks':True,'three_transverse_prolongation_classes':k==3}
 # Actual equation changes must break original native constraints after clean baseline.
 assert all(ck.values());bad=dict(extras[0]);bad['0']=str(F(bad.get('0','0'))+1)
 faults={'alter_base_coefficient':bool(combine(labels,bad,lambda z:b.column(*z))),'omit_leakage_product_term':any(combine(labels,v,lambda z:derivative(z,'drop_left_derivative'))!=d for v,d in zip(extras,D)),'drop_projector_product_term':mul(Pd,P)!=Pd}
 assert all(faults.values()),faults
 out=dict(result_id='K2147',status='conditional_exact_controls',derivative_cosets=affected,systems=systems,shared_affected_target_rank=target.rank(),shared_affected_target_derivative_rank=mat.rank(),derivative_obstruction_mod_affected_raw_and_targets=k,derivative_columns=[{str(k):v for k,v in sorted(d.items())} for d in D],exact_checks=ck,fault_failures={k:['native_equation_failure'] for k,v in faults.items()},dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='First homogeneous kernel prolongation along native hyperbola; affected complete raw cosets, globally shared target IDs; full graph claims require written analytic argument.')
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 if args.write:OUT.write_text(json.dumps(out,indent=2)+'\n')
 else:assert json.loads(OUT.read_text())==out
 print('FINAL',k,'checks',len(ck),'faults',len(faults),time.time()-start,flush=True)
if __name__=='__main__':main()
