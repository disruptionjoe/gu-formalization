#!/usr/bin/env python3
"""Exact Clifford and ordered original-row controls; universal proofs in K2189."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import sympy as S
import k2187_affine_clifford_exclusion_probe as p
from k2179_commuting_nonscalar_descent_probe import trace_certificate
k=p.k;ix=p.ix;ROOT=Path(__file__).resolve().parents[2]
def controls(fault=None):
 cs={};ck=lambda n,v:cs.__setitem__(n,bool(v));I=k.I
 # Genuine nonzero nilpotent geometry: two independent null directions.
 l1=k.add(ix(1),ix(5));l2=k.add(ix(2),ix(6));B=k.add(k.mm(l1,ix(3)),k.mm(l2,ix(4)));D=k.mm(B,B)
 ck('nilpotent_B_nonzero',bool(B));ck('nilpotent_D_nonzero_grade4',bool(D) and k.grade(D,4)==D)
 ck('nilpotent_B4_zero',not k.mm(D,D));ck('nilpotent_scalar_B2_zero',k.scalar(D)==0)
 # Nilpotent upper-triangular component affects no diagonal even if nonzero.
 J=S.Matrix([[0,1],[0,0]]);hh=S.Matrix([[2,3],[0,2]])
 ck('nonzero_Jordan_component',J!=S.zeros(2) and J**2==S.zeros(2) and J*hh==hh*J)
 for label,U,kap in [('h4',8*J-(5 if fault=='weight' else 6)*hh,-6),('h8',2*hh-8*J,2)]:
  ck(label+'_diagonal_transfer',list(U.diagonal())==list((kap*hh).diagonal()))
 # Independently reconstruct determinant from scalar Euler equations.
 a,c,V,T,m,n=S.symbols('a c V T m n');X=S.Matrix([[-S.Rational(2,5),S.Rational(6,5)],[0,0]]);Y=S.Matrix([[0,0],[-S.Rational(17,9),3]])
 for kap in [2,-6]:
  sol=S.solve([10*V+(16+3*kap)*T+4*a-12*c,(142+7*kap)*V+36*T+68*a-108*c],(V,T))
  Z=S.Matrix([[S.diff(sol[v],q) for q in [a,c]] for v in [V,T]])
  dim=31 if fault=='trace_dimension' else 32
  det=S.factor((S.eye(2)-(m*X+n*Y+(dim-m-n)*Z)/dim).det())
  expected=(32*m*n+329*m-2935*n+32480)/30720 if kap==2 else (m*n-30*m-132*n+2304)/960
  ck('diagonal_determinant_'+str(kap),S.cancel(det-expected)==0)
 # Chiral anticommutation forces offdiagonal coefficients; vector product has simple grade2.
 aa,bb,cc,dd,beta=S.symbols('aa bb cc dd beta');BM=S.diag(beta,-beta);WM=S.Matrix([[aa,bb],[cc,dd]])
 ck('chiral_anticommutator',BM*WM+WM*BM==S.diag(2*beta*aa,-2*beta*dd))
 av=k.add(ix(5),k.scale(ix(6),2));bv=k.add(ix(7),k.scale(ix(8),3));HH=k.grade(k.mm(av,bv),2)
 ck('vector_product_decomposable',not k.grade(k.mm(HH,HH),4));ck('simple_H_square_scalar',not p.nonscalar(k.mm(HH,HH)))
 # Invertible six-blade distinguishes inside from outside components.
 C6=ix(1,2,3,4,5,6);win=ix(1,2,5);wout=ix(1,2,7)
 ck('sixblade_nonnull',bool(k.mm(C6,C6)));ck('inside_anticommutes',not k.add(k.mm(C6,win),k.mm(win,C6)))
 ck('outside_commutes',not k.comm(C6,wout));ck('outside_not_anticommuting',bool(k.add(k.mm(C6,wout),k.mm(wout,C6))))
 ck('sixblade_Gram_sign',k.mm(C6,C6)==k.scale(I,1 if fault=='Gram_sign' else -1))
 # Block intertwining: a nonsemisimple square algebra can still be faithful4.
 A=S.diag(2,3,4,5);V4=S.Matrix([[1,1,0,0],[0,1,0,0],[0,0,2,1],[0,0,0,2]]);T4=V4**2
 VP=A.inv()*V4*A;TP=A.inv()*T4*A;zero=S.zeros(4);P=S.BlockMatrix([[zero,A],[A.inv(),zero]]).as_explicit();VV=S.diag(V4,VP);TT=S.diag(T4,TP);vol=S.diag(*([1]*4+[-1]*4))
 ck('invertible_odd_intertwiner',P.det()!=0 and P*vol+vol*P==S.zeros(8) and P*VV==VV*P and P*TT==TT*P)
 ck('trace8_equals_trace4',S.trace((VV+TT)**2)/8==S.trace((V4+T4)**2)/4)
 ck('Jordan_radical_preserved',(V4-S.eye(4))*(V4-2*S.eye(4))!=S.zeros(4))
 # Two actual full-Cl77 fixtures: central nonaffine and noncentral six-plane.
 al=ix(1,3);be=k.add(ix(2,3),ix(1,4))
 fixtures=[('central',k.add(k.mm(al,ix(5)),k.mm(be,ix(6))),k.add(k.mm(be,ix(5)),k.scale(k.mm(al,ix(6)),2))),('general',k.add(ix(1,2,3),ix(2,4,5)),k.add(ix(1,3,4),k.scale(ix(2,5,6),2)))]
 rows={}
 for label,w,u in fixtures:
  v=k.mm(k.blade(k.N),w);t=k.mm(k.OM,u);z=k.add(v,t);r=k.add(v,k.scale(t,3));PP=k.add(k.scale(v,7),k.scale(t,-15));pi=k.inv(PP);A0=k.neg(k.mm(pi,v));ts={j:k.scale(k.mm(pi,k.port(r)[j]),-k.ETA[j]) for j in k.N};L=k.N[:6];R=k.N[6:]
  sl=k.add(*(k.mm(k.bar(ts[b]),k.port(k.bar(r))[b]) for b in L));ss=k.add(sl,k.scale(k.mm(k.bar(A0),v),3 if fault=='complement_S' else 4))
  qr=k.add(k.scale(k.mm(t,A0),4),k.neg(v),k.scale(k.mm(k.bar(A0),z if fault=='bar_z' else k.bar(z)),7),k.scale(k.mm(ss,A0),2),k.scale(k.add(*(k.mm(k.bar(ts[b]),k.port(v)[b]) for b in L)),2),k.scale(k.mm(k.bar(A0),v),4 if fault=='complement_row' else 6))
  original={j:k.RR(ts,*k.C(k.port(z),*k.kernel(ts,j)))[1] for j in k.N}
  ck(label+'_pencil_two_sided',k.mm(PP,pi)==I and k.mm(pi,PP)==I)
  ck(label+'_S_identity',ss==k.add(*(k.mm(k.bar(ts[b]),k.port(k.bar(r))[b]) for b in k.N)))
  for j in R:
   ck(label+'_adapter_'+str(j),ts[j]==k.scale(k.mm(A0,k.G[j]),k.ETA[j]))
   ck(label+'_complement_row_'+str(j),original[j]==k.scale(k.mm(qr,k.G[j]),k.ETA[j]))
  for j in L:
   reduced=k.add(k.scale(k.mm(t,ts[j]),4),k.scale(k.port(z)[j],-k.ETA[j]),k.scale(k.mm(k.bar(ts[j]),z),7),k.scale(k.mm(ss,ts[j]),2),k.scale(k.add(*(k.mm(k.bar(ts[b]),k.comm(k.port(z)[b],k.G[j])) for b in L)),k.ETA[j]),k.scale(k.mm(k.bar(A0),k.port(v)[j]),(6 if fault=='L_row' else 8)*k.ETA[j]))
   ck(label+'_L_row_'+str(j),original[j]==reduced)
  rows[label]=sum(bool(q) for q in original.values());ck(label+'_original_rows_reject',rows[label]>0)
  if label=='central':
   h=k.mm(v,t);h4=k.grade(h,4);h8=k.grade(h,8);V=k.mm(v,v);T=k.mm(t,t);s4=k.mm(h4,h4)
   ck('central_commutes',not k.comm(v,t) and not k.comm(k.K(h),v) and not k.comm(k.K(h),t))
   ck('central_h4_square_nonzero_scalar',bool(s4) and not p.nonscalar(s4))
   ck('central_sector_trace_V',k.scalar(k.mm(h4,V))==0);ck('central_sector_trace_T',k.scalar(k.mm(h4,T))==0);ck('central_sector_trace_h8',k.scalar(k.mm(h4,h8))==0)
   ck('central_nonaffine',S.Matrix([[I.get(m,0),V.get(m,0),T.get(m,0)] for m in sorted(set(I)|set(V)|set(T))]).rank()==3)
 return cs,dict(original_nonzero_rows=rows)
FAULTS=['weight','trace_dimension','Gram_sign','complement_S','bar_z','complement_row','L_row']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();cs,details=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[n for n,v in controls(f)[0].items() if not v];assert bad,('undetected',f);faults[f]=bad
 census=trace_certificate();details['inherited_trace_census']={k:{x:v[x] for x in ['count','minimum_absolute_determinant','zero_pairs']} for k,v in census.items()}
 deps=['explorations/conditional-build/k2189-nonaffine-clifford-reduction-2026-10-28.md','explorations/conditional-build/k2179-commuting-nonscalar-descent-2026-10-28.md','explorations/conditional-build/k2187-affine-clifford-exclusion-2026-10-28.md','tests/channel-swings/k2187_affine_clifford_exclusion_probe.py','tests/channel-swings/k2179_commuting_nonscalar_descent_probe.py','tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py']
 report=dict(result_id='K2189',status='conditional_exact_controls',checks=cs,fault_failures=faults,details=details,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written simultaneous triangularization, chiral decomposability, six-plane localization, faithful square-algebra and ordered six-plus-one row arguments. Finite controls and inherited1122 integer cases are separate; no physical, proof-assistant or general nonaffine existence/exclusion claim.')
 dest=ROOT/'lab/process/k2189-nonaffine-clifford-reduction.json'
 if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==report
 print(json.dumps(dict(result='K2189',checks=len(cs),faults=len(faults),details=details)))
if __name__=='__main__':main()
