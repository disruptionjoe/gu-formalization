"""Standalone exact full-symbol polynomial-response probe; no stationary Jacobian.
Native imports from the declared GU checkout; prints coefficient witnesses.
"""
import json,argparse
from pathlib import Path
from fractions import Fraction as Q
import source_action_deep_geometry as geo
from source_action_deep_algebra import Engine,add,scale
from source_action_metric_symbol_probe import metric_symbol,matrix_unit,wedge_xi,symbols
E=Engine(geo)
from itertools import combinations_with_replacement
xi=[Q(0)]*14;xi[0]=xi[3]=Q(1)
flips=[0,1,8,9]
def paired_label(key):
    e,c=key;return min((e^c)^f for f in flips)
def component(label):
    return sorted((1<<i,(1<<i)^label^z) for i in range(14) for z in flips if (((1<<i)^label^z).bit_count()%4 in (1,2)))
def rr_rect(A,bs):
 a=[list(r)+list(v) for r,v in zip(A,bs)];m=len(a);n=len(A[0]);nr=len(bs[0]);row=0;piv=[]
 for col in range(n):
  k=next((k for k in range(row,m) if a[k][col]),None)
  if k is None:continue
  a[row],a[k]=a[k],a[row];v=a[row][col];a[row]=[x/v for x in a[row]]
  for k in range(m):
   if k!=row and a[k][col]:
    v=a[k][col];a[k]=[x-v*y for x,y in zip(a[k],a[row])]
  piv.append(col);row+=1
 failed=[j for j in range(nr) if any(z[n+j] for z in a[row:])]
 sol=[[Q(0)]*nr for _ in range(n)]
 for i,c in enumerate(piv):sol[c]=a[i][n:]
 return row,failed,sol

# Interpolation coefficient inverses for degrees<=3, samples0,1,-1,2.
def interp(vals):
 v0,v1,vm,v2=vals;a0=v0;a2=(v1+vm)/2-v0;odd=(v1-vm)/2
 a3=(v2-v0-4*a2-2*odd)/6;a1=odd-a3;return[a0,a1,a2,a3]

ps=[matrix_unit(i,j) for i,j in combinations_with_replacement(range(4),2)]
samples=[]
for s in [Q(0),Q(1),Q(-1),Q(2)]:
 xx=[Q(0)]*14;xx[0]=s;xx[3]=Q(1)
 sample=[]
 for p in ps:
  _,b=metric_symbol([Q(1),Q(1),Q(1),Q(-1,2)],p,xx)
  sample.append(E.Phi(wedge_xi(xx,b)))
 samples.append(sample)
labels=sorted({paired_label(k) for sm in samples for pp in sm for k in pp})
allout=[];exports=[]
for lab in labels:
 basis=component(lab);n=len(basis);Ks=[]
 for axis in [3,0]:
  xx=[Q(0)]*14;xx[axis]=Q(1)
  cols=[symbols(E,xx,{key:Q(1)})[0] for key in basis]
  assert all(all(k in basis for k in col) for col in cols)
  Ks.append([[col.get(key,Q(0)) for col in cols] for key in basis])
 rhs=[[[interp([samples[z][j].get(key,Q(0)) for z in range(4)])[d] for j in range(len(ps))] for key in basis] for d in range(4)]
 A=[];B=[]
 for d in range(4):
  for i in range(n):
   A.append([Ks[d-k][i][j] if d-k in [0,1] else Q(0) for k in range(3) for j in range(n)])
   B.append([-v for v in rhs[d][i]])
 rank,failed,sol=rr_rect(A,B)
 assert not failed
 assert all(sum(A[i][k]*sol[k][j] for k in range(len(sol)))==B[i][j] for i in range(len(A)) for j in range(len(ps)))
 assert all(not any(row) or basis[k%n][1].bit_count()%2==0 for k,row in enumerate(sol))
 exports.append({'label':lab,'basis':basis,'solution_coefficients':[[[k//n,basis[k%n][0],basis[k%n][1],str(row[j])] for k,row in enumerate(sol) if row[j]] for j in range(len(ps))]})
 allout.append({'label':lab,'dimension':n,'polynomial_system_rank':rank,'failed_metric_amplitudes':failed})

# Independent exact r controls; the written degree argument makes the
# r-affine and homogeneous frequency extension universal in this family.
for j,p in enumerate(ps):
 xx=[Q(0)]*14;xx[0]=xx[3]=Q(1)
 for r in (Q(1),Q(3)):
  _,b=metric_symbol([Q(1),Q(1),Q(1),-1/r],p,xx)
  assert E.Phi(wedge_xi(xx,b))==scale(r-1,samples[1][j])
result={'basis_amplitudes':list(combinations_with_replacement(range(4),2)),
 'scope':'xi=(u,0,0,v); base=(1,1,1,-a),r=1/a; multiply responses by(r-1); degree2 coefficient s=u/v homogeneous extension',
 'coefficient_residual_checks':sum(4*r['dimension']*len(ps)for r in allout),
 'r_affinity_controls':20,'blocks':allout,'solutions':exports,
 'claim_ceiling':'leading coupled principal equations only; no subprincipal Schur reduction or physical stability'}
p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args();text=json.dumps(result,indent=2)+'\n'
if args.output:args.output.write_text(text)
else:print(text)
