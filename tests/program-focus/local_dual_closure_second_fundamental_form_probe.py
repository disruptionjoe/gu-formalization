#!/usr/bin/env python3
"""Exact finite-field minor certificate for the actual native shape cross block.

Native complex coefficients lie in Q(i,sqrt2,sqrt3). Reduction uses p=97,
i=22, sqrt2=14, sqrt3=10; all geometric denominators are invertible.
A nonzero reduced 512-column minor proves the characteristic-zero rank512.
The universal II-vanishing theorem is the companion written Clifford proof.
No floating-point rank, source action, domain or physical barred map is made.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
import argparse, importlib.util, json
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import numpy as np

ap=argparse.ArgumentParser()
ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
ap.add_argument('--output',type=Path)
args=ap.parse_args()
p=97
checks=[]
def check(name,condition):
    checks.append({'name':name,'pass':bool(condition)})
    if not condition: raise AssertionError(name)
def fp(v):
    v=F(v)
    return (v.numerator*pow(v.denominator%p,-1,p))%p
path=args.repo/'tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py'
spec=importlib.util.spec_from_file_location('native_shape_geometry',path)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.MUT=''
T,D=m.adapted_congruence(m.dewitt(F(1,2)))
normals=[m.vec_to_sym([T[r][i] for r in range(10)]) for i in range(10)]
check('actual normal Gram and signature',[D[i][i] for i in range(10)]==[2,2,2,2,6,12,-2,-2,-2,-4])
check('number-field residue roots',22**2%p==p-1 and 14**2%p==2 and 10**2%p==3)
# Integral Pauli realization; all nonzero gamma entries are monomial.
I2=np.eye(2,dtype=np.int64);X=np.array([[0,1],[1,0]],dtype=np.int64)
Y=np.array([[0,-22],[22,0]],dtype=np.int64)%p;Z=np.diag([1,-1]).astype(np.int64)%p
base=[]
for pos in range(7):
    for v in [X,Y]:
        A=np.array([[1]],dtype=np.int64)
        for a in [Z]*pos+[v]+[I2]*(6-pos): A=np.kron(A,a)%p
        base.append(A)
scales=[22,1,1,1,14,14,14,14,(14*10)%p,20,(22*14)%p,(22*14)%p,(22*14)%p,44]
gamma=[A*s%p for A,s in zip(base,scales)]
s=128
E=np.eye(s,dtype=np.int64)
perms=[];values=[]
for A in gamma:
    check('monomial Clifford matrix',np.all(np.count_nonzero(A,axis=0)==1) and np.all(np.count_nonzero(A,axis=1)==1))
    perm=np.argmax(A!=0,axis=1);perms.append(perm);values.append(A[np.arange(s),perm])
def left(i,A): return (values[i][:,None]*A[perms[i],:])%p
def product(i,j): return left(i,gamma[j])
signs=[-1,1,1,1]+[int(D[i][i]) for i in range(10)]
check('all native Clifford squares',all(np.array_equal(product(i,i),signs[i]*E%p) for i in range(14)))
check('all native Clifford anticommutators',all(not np.any((product(i,j)+product(j,i))%p) for i,j in combinations(range(14),2)))
eta=[-1,1,1,1]
# A_II(b)(n_i)=sum_mu eta_mu c_mu b(S_ni e_mu), S_v=-1/2 eta^-1 v.
A=[]
for i in range(10):
    row=[]
    for j in range(4):
        block=np.zeros((s,s),dtype=np.int64)
        for mu in range(4):
            coeff=-F(1,2)*eta[mu]*eta[j]*normals[i][j][mu]
            block=(block+fp(coeff)*gamma[mu])%p
        row.append(block)
    A.append(row)
def project(A):
    traces=[]
    for j in range(4):
        tr=np.zeros((s,s),dtype=np.int64)
        for i in range(10): tr=(tr+fp(1/D[i][i])*left(i+4,A[i][j]))%p
        traces.append(tr)
    out=[[ (A[i][j]-fp(F(1,10))*left(i+4,traces[j]))%p for j in range(4)] for i in range(10)]
    check('output is in actual normal gamma kernel',all(not np.any(sum((fp(1/D[i][i])*left(i+4,out[i][j]) for i in range(10)),np.zeros((s,s),dtype=np.int64))%p) for j in range(4)))
    return out
B=project(A)
full=np.vstack([np.hstack(row) for row in B])
# Modular Gaussian elimination, preserving original row labels. At each step
# a previously unused original row supplies the next pivot. Listed original
# rows in pivot order have determinant equal to the product of pivot entries.
def certificate(matrix):
    work=matrix.copy()%p
    rows=np.arange(work.shape[0]);rank=0;pivotrows=[];product_pivots=1
    for col in range(work.shape[1]):
        nz=np.flatnonzero(work[rank:,col])
        if len(nz)==0: continue
        index=rank+int(nz[0])
        if index!=rank:
            work[[rank,index],:]=work[[index,rank],:]
            rows[[rank,index]]=rows[[index,rank]]
        pivot=int(work[rank,col]);pivotrows.append(int(rows[rank]))
        product_pivots=product_pivots*pivot%p
        work[rank,col:]=work[rank,col:]*pow(pivot,-1,p)%p
        if rank+1<work.shape[0]:
            factors=work[rank+1:,col].copy()
            # Entries/factors/pivot rows are at most96, so int64 is far from overflow.
            work[rank+1:,col:]=(work[rank+1:,col:]-factors[:,None]*work[rank:rank+1,col:])%p
        rank+=1
        if rank==work.shape[0]:break
    return rank,pivotrows,product_pivots
rank,pivotrows,det=certificate(full)
check('native opposite block has maximal four-spinor input rank',rank==4*s)
check('recorded maximal minor has nonzero residue',det!=0 and len(pivotrows)==4*s and len(set(pivotrows))==4*s)
# Pure-mean and mean-zero second-fundamental-form controls use the same
# native Cl14 and K projection. The test only needs a nonzero block, not new ranks.
# Define II00=n0, II11=n0 with Lorentz eta=(-,+,+,+), so mean=0.
Amz=[[np.zeros((s,s),dtype=np.int64) for j in range(4)] for i in range(10)]
Amz[0][0]=fp(D[0][0])*gamma[0]%p
Amz[0][1]=fp(D[0][0])*gamma[1]%p
Bmz=project(Amz)
check('mean-zero nonzero shape still has opposite coupling',any(np.any(b) for row in Bmz for b in row))
Azero=[[np.zeros((s,s),dtype=np.int64) for j in range(4)] for i in range(10)]
Bzero=project(Azero)
check('totally-geodesic shape has zero opposite block',all(not np.any(b) for row in Bzero for b in row))
result={'status':'PASS','checks':checks,'checks_passed':len(checks),
 'coefficient_field':'Q(i,sqrt(2),sqrt(3))','prime':p,
 'residue_roots':{'i':22,'sqrt2':14,'sqrt3':10},
 'native_carrier_dimension':128,'cross_block_shape':list(full.shape),
 'rank_over_F97':rank,'rank_over_C':rank,'rank_argument':'Input dimension512 upper bound; nonzero reduction of a 512x512 minor gives characteristic-zero lower bound512.',
 'minor_original_row_order':pivotrows,'minor_column_order':list(range(4*s)),
 'minor_determinant_mod97':det,
 'claim_ceiling':'Canonical metric-spin dual and same tangential normal-jet reconstruction only; actual source barred map/full density-dual and analytic domain remain unselected.'}
if args.output:
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['minor_original_row_order','minor_column_order','checks']},indent=2))
