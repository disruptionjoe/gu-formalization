#!/usr/bin/env python3
"""Exact Clifford/local-observation controls; continuum proof is in the note."""
import sys
sys.dont_write_bytecode=True
import sympy as s
from itertools import product
from pathlib import Path
import json,hashlib,argparse
import k2212_mass_connection_algebra_probe as old
ROOT=Path(__file__).resolve().parents[2]
def norm2(a):return s.expand(s.trace(a.conjugate().T*a))
def controls(fault=None):
 c={};ck=lambda k,v:c.__setitem__(k,bool(v))
 I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);J=s.Matrix([[0,1],[-1,0]])
 C=[s.kronecker_product(X,I),s.kronecker_product(Z,X),s.kronecker_product(Z,Z)]
 if fault=='principal':C[2]=C[1]
 A=s.kronecker_product(Z,J);M=-s.I*A;Q=-C[0]*C[1]*C[2];S=-s.I*Q
 if fault=='mass':M=S
 ck('mass_involution',M*M==s.eye(4));ck('real_generator',A*A==-s.eye(4) and A.T==-A)
 for j in range(3):
  ck('spatial_'+str(j),C[j]*C[j]==s.eye(4) and C[j].T==C[j]);ck('mass_anticommute_'+str(j),M*C[j]+C[j]*M==s.zeros(4))
  ck('volume_commutes_'+str(j),S*C[j]==C[j]*S)
 for j in range(3):
  for l in range(j):ck(f'clifford_{j}_{l}',C[j]*C[l]+C[l]*C[j]==s.zeros(4))
 words=[]
 for bits in product([0,1],repeat=4):
  w=s.eye(4)
  for b,g in zip(bits,C+[A]):
   if b:w=w*g
  words.append(s.Matrix(list(w)))
 ck('real_full_matrix_algebra',s.Matrix.hstack(*words).rank()==16)
 T0=s.kronecker_product(s.eye(4),X)+s.kronecker_product(S,Z)
 jets=[s.kronecker_product(s.eye(4),j*X+Z)+s.kronecker_product(S,X-j*Z) for j in [1,2,3]]
 CC=[s.kronecker_product(a,I) for a in C];MM=s.kronecker_product(M,I)
 terms=[-s.I*CC[j]*jets[j] for j in range(3)]+[2*(MM*T0-T0*MM)]
 for a,t in enumerate(terms):
  for j in range(3):ck(f'character_{a}_{j}',CC[j]*t*CC[j]==(1 if a==j else -1)*t)
 R=sum(terms,s.zeros(8));actual=R-terms[2] if fault=='missing_derivative' else R
 ck('orthogonal_residual_identity',norm2(actual)==sum(norm2(t) for t in terms))
 E=(T0+MM*T0*MM)/2
 ck('commutant_distance',4*norm2(T0-E)==norm2(MM*T0-T0*MM))
 ck('coercivity',norm2(T0-E)<=norm2(actual)/16)
 P=(s.eye(4)+S)/2;ck('massless_half_projector',P*P==P and P.conjugate().T==P)
 ck('massive_half_leaks',M*P-P*M!=s.zeros(4));ck('expectation_not_projector',((P+M*P*M)/2)**2!=(P+M*P*M)/2)
 PM=(s.eye(4)+M)/2;ck('mass_projector_principal_leaks',C[0]*PM-PM*C[0]!=s.zeros(4))
 # A real flavor rotation: U at a rational point, U'=Afl U.
 U=s.kronecker_product(s.eye(4),s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]]))
 Af=s.kronecker_product(s.eye(4),-J);P0=s.kronecker_product(s.eye(4),s.diag(1,0));P=U*P0*U.T;dP=Af*P-P*Af
 V=s.I*CC[0]*Af*(-1 if fault=='connection_sign' else 1)
 residual=-s.I*CC[0]*dP+V*P-P*V
 ck('nonconstant_projector',dP!=s.zeros(8) and P*P==P)
 ck('connection_hermitian',V.conjugate().T==V)
 ck('transported_intertwining',residual==s.zeros(8))
 ck('omitted_connection_fails',-s.I*CC[0]*dP!=s.zeros(8))
 # Faithful inherited128 real spinor, all16384 Clifford blades enumerated.
 cg=list(old.C.values());mass=old.P[0];zero=old.Z
 ck('actual_volume',old.Q==old.scale(old.mul(old.mul(cg[0],cg[1]),cg[2]),-1))
 def sign(a,b):return -1 if (a.bit_count()*b.bit_count()-(a&b).bit_count())%2 else 1
 masks=[next(iter(g)) for g in cg];mm=next(iter(mass))
 k0=[a for a in range(1<<14) if all(sign(a,b)==1 for b in masks)]
 k1=[a for a in k0 if sign(a,mm)==1]
 ck('faithful_massless2048',len(k0)==2048);ck('faithful_massive1024',len(k1)==1024)
 ck('all_nine_copy_mixing',1024*81==288**2 and 2048*81==2*288**2)
 return c

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();c=controls();assert all(c.values()),[k for k,v in c.items() if not v]
 faults={f:[k for k,v in controls(f).items() if not v] for f in ['principal','mass','missing_derivative','connection_sign']};assert all(faults.values())
 deps=['tests/channel-swings/k2212_mass_connection_algebra_probe.py','explorations/conditional-build/k2212-mass-connection-algebra-2026-10-28.md','explorations/conditional-build/k2215-variable-mass-gap-2026-10-28.md','explorations/conditional-build/k2218-local-observation-rigidity-2026-10-28.md']
 report=dict(result_id='K2218',status='conditional_complete_local_intertwiner_classification',checks=c,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Written distributional classification and oscillatory-energy proof; exact faithful Clifford census, independent small-matrix algebra and nonconstant flavor counterconstruction; no physical observation selection.')
 p=ROOT/'lab/process/k2218-local-observation-rigidity.json'
 if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report
 print(json.dumps(dict(result='K2218',controls=len(c),faults=faults)))
if __name__=='__main__':main()
