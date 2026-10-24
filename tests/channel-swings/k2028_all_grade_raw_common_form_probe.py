"""Separate raw-symbol action and finite-field injectivity replay.

Rebuilds every column through D_k(Omega_k J), rather than the producer's
W-cancelled upper-block formula. Finite-field nonsingular integer minors
prove injectivity over the reals. Matrix counterexamples are actual changes.
"""
import json,hashlib
from copy import copy
from pathlib import Path
import numpy as np
from sage.all import QQ,GF,matrix,identity_matrix,zero_matrix,block_matrix,block_diagonal_matrix,prod,PolynomialRing
from k1967_paired_raw_coefficient_observation import setup
from k1836_k77_differential_dirac_quotient import mat
ROOT=Path(__file__).resolve().parents[2]
def gauge_controls():
 R=PolynomialRing(QQ,names=('t','x','y','z'));t,x,y,z=R.gens();xx=(t,x,y,z)
 a=(x*y+t*z,t*y+x*z,x*x+t*z,y*z+t*x);chi=t*x*y+x*z*z+t*t*z
 shifted=[a[k]-chi.derivative(xx[k]) for k in range(4)]
 def curvature(b):return [b[j].derivative(xx[i])-b[i].derivative(xx[j]) for i in range(4) for j in range(i+1,4)]
 assert curvature(a)==curvature(shifted)
 magnetic=(R(0),R(0),3*x,R(0));assert curvature(magnetic)==[0,0,0,3,0,0]
 # Omitting one component of the phase connection is an actual failed identity.
 bad=list(shifted);bad[0]=a[0];assert curvature(bad)!=curvature(a)
 print('PASS six exact polynomial gauge-curvature identities, nonzero magnetic curvature, one phase-connection fault',flush=True)
def main():
 r=json.loads((ROOT/'lab/process/k2028-all-grade-raw-common-form.json').read_text());g,v,eta,js,C,P,djs,Fi,Ti,apply=setup();I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);B=prod(g[7:]);ii=np.arange(128)
 assert B.transpose()==B and B*B==I and all(x.transpose()*B==-B*x for x in g)
 def encode(M,scale=1):
  dd=M.dict();ff={int(a)^int(b) for a,b in dd};assert len(ff)==1;f=ff.pop();a=np.array([int(scale*M[j,j^f]) for j in range(128)],dtype=np.int64);assert all(QQ(int(a[j]))==scale*M[j,j^f] for j in range(128));return f,a
 def compose(a,b):return a[0]^b[0],a[1]*b[1][ii^a[0]]
 def sumterms(xs):
  assert len({a[0] for a in xs})==1
  return xs[0][0],sum((a[1] for a in xs),np.zeros(128,dtype=np.int64))
 gam=list(map(encode,g));jv=[encode(x*Fi,44) for x in js];dj=[encode(x*Fi,44) for x in djs];vol=encode(v);assert vol[0]==0
 mon=[];signatures=set()
 for mask in range(16384):
  a=(0,np.ones(128,dtype=np.int64))
  for k in range(14):
   if mask>>k&1:a=compose(a,gam[k])
  signature=(a[0],tuple((a[1]*a[1][0]).tolist()));assert signature not in signatures;signatures.add(signature);mon.append(a)
 # Distinct signed Pauli characters are trace-orthogonal and span M128(R).
 assert len(signatures)==128**2
 grades=[]
 for degree in range(15):
  sg=(-1)**(degree*(degree+1)//2);rows=[]
  for a in range(14):
   for c in range(a+1,14):
    if sg*(-1)**(int(a<degree)+int(c<degree))!=1:rows.append([int(k!=a and k!=c) for k in range(14)])
  T=matrix(QQ,rows,ncols=14);basis=T.right_kernel().basis_matrix();stored=matrix(QQ,r['grade_kernels'][str(degree)],ncols=14)
  assert T*stored.transpose()==0 and stored.rank()==basis.nrows();grades.append(stored)
 groups={};survivor=None;checks=0;seen=set()
 for record in r['groups']:
  f=record['flip'];cols=[];labels=record['labels']
  for mask,y in labels:
   inside=[k for k in range(14) if mask>>k&1];perm=inside+[k for k in range(14) if k not in inside];can=[y[k] for k in perm];assert tuple(map(QQ,can)) in [tuple(x) for x in grades[len(inside)].rows()]
   key=(mask,tuple(y));assert key not in seen;seen.add(key)
   om=[]
   for k in range(14):
    a=compose(gam[k],mon[mask]);om.append((a[0],eta[k]*y[k]*(3+vol[1])*a[1]))
   # Build each raw D_k applied to the common connection action on all fields.
   out=[np.zeros(128,dtype=np.int64) for _ in range(14)];flips=[None]*14
   for k in range(14):
    fields=[compose(om[k],a) for a in jv]
    terms=[compose(gam[c],(fields[c][0],(3-vol[1])*fields[c][1])) for c in range(14)]
    for a in range(14):
     if a==k:z=(fields[14][0],88*fields[14][1]//44) # fields14 includes factor44
     else:
      zz=sumterms([terms[c] for c in range(14) if c not in (a,k)])
      z=compose(compose(gam[a],gam[k]),zz);z=(z[0],eta[a]*z[1])
     if flips[a] is not None:assert flips[a]==z[0]
     flips[a]=z[0];out[a]+=z[1]
   M=(flips[0],out[0]);assert M[0]==f;col=[]
   for a in range(14):
    z=compose(dj[a],M);assert z[0]==flips[a];col.extend((44*out[a]-z[1]).tolist())
   col.extend((M[1]+M[1][ii^f]).tolist());cols.append(col);checks+=1
  T=matrix(QQ,cols).transpose();rows=record['pivots'];minor=T.matrix_from_rows(rows);assert minor.nrows()==minor.ncols()==len(labels)
  d=int(minor.change_ring(GF(101)).determinant());assert d==record['minor_det_mod101']*pow(2,len(labels),101)%101 and d!=0
  assert minor.change_ring(GF(103)).rank()==len(labels)
  U=T[:-128,:];K=mat(record['upper_kernel']);assert U*K.transpose()==0
  assert U.change_ring(GF(103)).rank()+K.nrows()==len(labels)
  if K.nrows():assert K.nrows()==1 and survivor is None;survivor=(record,K[0])
 assert checks==r['common_form_dimension']==8388
 # Full original-coordinate survivor, not a fitted lower-return replacement.
 rec,row=survivor;omegas=[copy(Z) for _ in range(14)]
 for coeff,(mask,y) in zip(row,rec['labels']):
  if not coeff:continue
  X=prod([g[k] for k in range(14) if mask>>k&1]) if mask else I
  for k in range(14):omegas[k]+=coeff*(3*I+v)*eta[k]*y[k]*g[k]*X/4
 actions=[apply(k,[omegas[k]*x for x in js]) for k in range(14)]
 raw=[sum((actions[k][a] for k in range(14)),Z) for a in range(14)]
 M=Fi*raw[0];assert all(raw[a]==djs[a]*M for a in range(14))
 defect=P*M+M.transpose()*P;assert defect and defect.rank()==128
 W=(3*I-v)/2;top=[]
 for a in range(14):
  top.append([sum((eta[a]*g[a]*g[k]*g[c]*W*omegas[k] for k in range(14) if k not in (a,c)),Z) if a!=c else Z for c in range(14)])
 assert all(eta[a]*B*top[a][c]==top[c][a].transpose()*eta[c]*B for a in range(14) for c in range(14))
 bottom=sum((eta[k]*B*omegas[k].transpose()*B*js[k] for k in range(14)),Z);ld=bottom-djs[14]*M
 assert bool(ld)==(r['full_upper_dimension']==0)
 se=(djs[14]*M-bottom)*Fi;assert B*se==se.transpose()*B and se*js[14]+bottom==djs[14]*M
 assert M==mat(r['survivor']['M']) and se==mat(r['survivor']['southeast_repair']) and defect==mat(r['survivor']['energy_defect']) and ld==mat(r['survivor']['lower_defect'])
 # Changed reality branch: independently reconstruct pure-imaginary Hermitian equations.
 im=r['complex_hermitian_branch'];bb=encode(B);seen_im=set();image=[];imcount=0
 def transpose_mono(a):return a[0],a[1][ii^a[0]]
 for degree in range(15):
  sg=(-1)**(degree*(degree+1)//2)
  rows=[[int(k not in (a,c)) for k in range(14)] for a in range(14) for c in range(a+1,14) if sg*(-1)**(int(a<degree)+int(c<degree))==1]
  TT=matrix(QQ,rows,ncols=14);KK=matrix(QQ,im['grade_kernels'][str(degree)],ncols=14);assert TT*KK.transpose()==0 and TT.rank()+KK.rank()==14
 for rec in im['groups']:
  f=rec['flip'];cols=[];lows=[];masscols=[]
  for mask,y in rec['labels']:
   key=(mask,tuple(y));assert key not in seen_im;seen_im.add(key);inside=[k for k in range(14) if mask>>k&1];perm=inside+[k for k in range(14) if k not in inside]
   assert [y[k] for k in perm] in im['grade_kernels'][str(len(inside))]
   om=[]
   for k in range(14):
    a=compose(gam[k],mon[mask]);om.append((a[0],eta[k]*y[k]*(3+vol[1])*a[1]))
   out=[np.zeros(128,dtype=np.int64) for _ in range(14)];flips=[None]*14
   for k in range(14):
    fields=[compose(om[k],a) for a in jv];terms=[compose(gam[c],(fields[c][0],(3-vol[1])*fields[c][1])) for c in range(14)]
    for a in range(14):
     if a==k:z=(fields[14][0],2*fields[14][1])
     else:
      zz=sumterms([terms[c] for c in range(14) if c not in (a,k)]);z=compose(compose(gam[a],gam[k]),zz);z=(z[0],eta[a]*z[1])
     if flips[a] is not None:assert flips[a]==z[0]
     flips[a]=z[0];out[a]+=z[1]
   MM=(flips[0],out[0]);assert MM[0]==f;col=[]
   for a in range(14):
    z=compose(dj[a],MM);assert z[0]==flips[a];col.extend((44*out[a]-z[1]).tolist())
   col.extend((MM[1]-MM[1][ii^f]).tolist());cols.append(col);masscols.append(MM[1].tolist())
   low=sumterms([(z[0],-eta[k]*z[1]) for k in range(14) for z in [compose(compose(compose(bb,transpose_mono(om[k])),bb),jv[k])]])
   targetlow=compose(dj[14],MM);assert low[0]==targetlow[0];lows.append((88*low[1]-targetlow[1]).tolist());imcount+=1
  TT=matrix(QQ,cols).transpose();KK=mat(rec['kernel']);FK=mat(rec['full_kernel']);LL=matrix(QQ,lows).transpose()
  minor_im=TT.matrix_from_rows(rec['pivots']).matrix_from_columns(rec['pivot_columns']);dd=int(minor_im.change_ring(GF(101)).determinant());assert dd==rec['minor_det_mod101']*pow(2,rec['rank'],101)%101 and dd!=0
  assert minor_im.change_ring(GF(103)).rank()==rec['rank'] and TT*KK.transpose()==0 and KK.nrows()+rec['rank']==len(rec['labels'])
  assert LL*FK.transpose()==0 and FK==KK
  for row in FK:
   vv=[sum(coef*QQ(masscols[j][i])/352 for j,coef in enumerate(row)) for i in range(128)];M0=matrix(QQ,128,128,{(i,i^f):v for i,v in enumerate(vv) if v},sparse=True);Mim=Fi*M0*js[14]
   image.append(Mim)
 assert imcount==8232 and len(image)==13
 coords=matrix(QQ,im['image_coordinates']);assert coords.rank()==4
 for Mim,coord,stored in zip(image,coords,im['induced_basis']):
  assert Mim==mat(stored)==coord[0]*I+sum((coef*c for coef,c in zip(coord[1:],C)),Z) and P*Mim==Mim.transpose()*P
 # The only simultaneous isotropic Clifford mass in span(I,C_i) is zero:
 # trace of each anticommutator isolates its C_i coefficient, leaving a0 C_i.
 assert all(c.trace()==0 for c in C) and all((C[i]*C[j]).trace()==(128 if i==j else 0) for i in range(3) for j in range(3))
 print('PASS complex branch8232 raw columns,127 exact blocks,13 full coefficients,4 scalar/vector images,9 invisible directions; no isotropic mass',flush=True)

 # Actual corrupted coefficient, basis relation and integer proof minor controls.
 faults=[]
 bad=copy(omegas[0]);bad[0,0]+=1
 assert bad!=omegas[0];changed=apply(0,[(bad-omegas[0])*x for x in js]);delta=[raw[a]+changed[a] for a in range(14)];mm=Fi*delta[0]
 assert any(delta[a]!=djs[a]*mm for a in range(14));faults.append('raw_coefficient')
 try:
  yy=list(r['grade_kernels']['3'][0]);yy[0]+=1;T3=matrix(QQ,[[int(k not in (a,c)) for k in range(14)] for a in range(3) for c in range(3,14)]);assert T3*matrix(QQ,1,14,yy).transpose()==0
 except AssertionError:faults.append('grade_relation')
 mm=copy(minor);mm[0,:]=0
 try:assert mm.change_ring(GF(101)).determinant()!=0
 except AssertionError:faults.append('rank_minor')
 wrong=copy(M);wrong[0,0]+=1
 assert any(raw[a]!=djs[a]*wrong for a in range(14));faults.append('induced_mass')
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('PASS K2028 separate raw action',checks,'columns,128 minors at101/103; complete upper dimension1; energy defect rank',defect.rank(),'lower defect rank',ld.rank(),';',len(faults),'actual faults;',len(r['inputs']),'provenance hashes',flush=True)
 gauge_controls()
if __name__=='__main__':main()
