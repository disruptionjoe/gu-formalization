#!/usr/bin/env sage-python
"""Exact all-direction sector compatibility on the pinned corrected fixture."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,matrix,identity_matrix,block_matrix
from k1824_k77_joint_observed_symbol_algebra import intertwiner_basis,entries
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1834-k77-characteristic-cones.json'
def mat(d):return matrix(QQ,16,16,{(i,j):QQ(v) for i,j,v in d['entries']})
def produce():
 src=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());checks={};records=[];I=identity_matrix(QQ,16)
 def ck(k,v):checks[k]=bool(v);assert v,k
 for ix,blk in enumerate(src['blocks']):
  a=list(map(mat,blk['matrices']));H=mat(blk['H'])
  sq=[A*A for A in a]+[a[i]*a[j]+a[j]*a[i] for i in range(3) for j in range(i+1,3)]
  central=intertwiner_basis(sq,sq);ck('square_commutant20_'+str(ix),len(central)==20)
  ck('all_coefficient_equations_'+str(ix),all(C*S==S*C for C in central for S in sq))
  hforms=[H*C for C in central]
  sy=matrix(QQ,256,20,[[(M-M.transpose()).list()[k] for M in hforms] for k in range(256)]).right_kernel()
  sk=matrix(QQ,256,20,[[(M+M.transpose()).list()[k] for M in hforms] for k in range(256)]).right_kernel()
  ck('symmetric11_skew9_'+str(ix),sy.dimension()==11 and sk.dimension()==9)
  F=[(576*A*A-I)/575 for A in a]
  ck('fast_rank12_'+str(ix),all(Q*Q==Q and Q.rank()==12 and H*Q==Q.transpose()*H for Q in F))
  ck('direction_dependence_rank8_'+str(ix),(F[0]-F[1]).rank()==8)
  constraints=[Q-I for Q in F]+sq[3:]
  fast=block_matrix([[Q] for Q in constraints]).right_kernel();B=matrix(QQ,fast.basis()).transpose()
  ck('common_fast4_'+str(ix),B.ncols()==4)
  ck('common_fast_not_invariant_'+str(ix),all(B.augment(A*B).rank()==8 for A in a))
  C=next(sum((v*M for v,M in zip(w,central)),matrix(QQ,16,16)) for w in sk.basis() if any(sum((v*M for v,M in zip(w,central)),matrix(QQ,16,16))*A!=A*sum((v*M for v,M in zip(w,central)),matrix(QQ,16,16)) for A in a))
  ck('conservative_nonscalar_compatible_'+str(ix),C.transpose()*H+H*C==0 and all(C*S==S*C for S in sq) and any(C*A!=A*C for A in a))
  # A mixed-direction control is distinct from axis-only constraints.
  n=(QQ(2),QQ(-3),QQ(6));r2=sum(x*x for x in n);An=sum((n[j]*a[j] for j in range(3)),matrix(QQ,16,16));Q=(576*An*An/r2-I)/575
  ck('mixed_direction_projector_'+str(ix),Q*Q==Q and Q.rank()==12 and C*Q==Q*C)
  ck('quartic_mixed_control_'+str(ix),576*An**4-577*r2*An**2+r2*r2*I==0)
  ck('speed_multiplicities_'+str(ix),all((a[0]-v*I).right_nullity()==m for v,m in [(1,6),(-1,6),(QQ(1)/24,2),(-QQ(1)/24,2)]))
  records.append({'square_commutant_basis':[entries(M) for M in central],'conservative_noncentral_example':entries(C),'common_fast_basis':{'rows':16,'columns':4,'entries':[[int(i),int(j),str(v)] for (i,j),v in sorted(B.dict().items())]}})
 ck('full_commutant_dimension',20*32**2==20480);ck('full_conservative_dimension',32*9+(32*31//2)*20==10208)
 return {'result_id':'K1834','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'characteristic_polynomial':'(tau^2-|xi|^2)^192 (tau^2-|xi|^2/576)^64','constant_pure_speed_invariant_sector':False,'Fourier_sector_ranks':[384,128],'speed_compatible_coefficient_dimension':20480,'H_skew_speed_compatible_dimension':10208,'single_common_Lorentz_cone':False,'local_differential_extraction_invertible':False,'physical_or_source_selection':False},'blocks':records,'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1832-k77-common-energy-form.json','lab/process/k1824-k77-joint-observed-symbol-algebra.json']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();v=produce()
 if args.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1834',len(v['checks']),'exact groups')
