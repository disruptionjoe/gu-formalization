#!/usr/bin/env python3
"""Full-bank Gram reduction and universal travelling mass-plane trace identities."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1877-traveling-gram-amplitude-rigidity.json'
def mat(x):
 M=s.zeros(x.get('rows',16),x.get('columns',16))
 for i,j,v in x['entries']:M[i,j]=s.Rational(v)
 return M

def produce():
 src=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());en=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());old=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text())
 D=list(map(mat,src['target_D']));d=[x/24 for x in D];J=D[0]*D[1]*D[2];I=s.eye(4);B1,B2=[mat(r['B']) for r in old['blocks'][0]['repairs']];checks={};offset_witnesses=[]
 def ck(n,v):checks[n]=bool(v);assert v,n
 def zero(M):return all(s.expand(x)==0 for x in M)
 ck('Clifford',all(D[i]*D[j]+D[j]*D[i]==(2*I if i==j else s.zeros(4)) for i in range(3) for j in range(3)))
 ck('central_J',J.T==-J and J*J==-I and all(J*x==x*J for x in D))
 ck('mass_plane',B1*J==B2 and B1*B1==B2*B2==-I and B1*B2+B2*B1==s.zeros(4) and all(b.T==-b and all(b*x+x*b==s.zeros(4) for x in D) for b in [B1,B2]))
 basis=[s.Matrix([x for i in range(3) for x in (J if i==j else s.zeros(4))]) for j in range(3)]+[s.Matrix([x for Di in D for x in Di*J])];Q=s.Matrix.hstack(*basis)
 for ix,(sr,er,kr) in enumerate(zip(src['blocks'],en['blocks'],old['blocks'])):
  T=list(map(mat,sr['T']));Hi=mat(er['H']).inv();K=mat(kr['full_conservative_kernel']);alpha=s.Rational(sr['alpha'])
  ck('bank_rank_'+str(ix),K.rank()==44)
  G=s.Matrix.hstack(*[s.Matrix([x for Ti in T for x in (Ti*Hi*s.Matrix(4,16,row[126:]).T-s.Matrix(4,16,row[126:])*Hi*Ti.T)]) for row in K.tolist()])
  ck('full_Gram_span_'+str(ix),G.rank()==4 and Q.row_join(G).rank()==4)
  ck('principal_Gram_'+str(ix),all(T[i]*Hi*T[j].T+T[j]*Hi*T[i].T==(2*alpha*I if i==j else s.zeros(4)) for i in range(3) for j in range(3)))
  ck('positive_alpha_'+str(ix),alpha>0)
  # The simplest factorization of the circular positive Gram fails the full pointwise bank.
  S0=J*T[0]/2;bank=K[:,120:].T;rhs=s.Matrix([0]*6+list(S0))
  ck('simple_circular_offset_no_lift_'+str(ix),bank.row_join(rhs).to_DM().rank()==bank.to_DM().rank()+1)
  # All massless offsets of the two saved static mass slopes, not only S0 above.
  N=s.Matrix.hstack(*K[:,120:126].T.nullspace());co=K.T*N;cols=[]
  C1,C2=[mat(z['C']) for z in kr['repairs']];S1,S2=[mat(z['S']) for z in kr['repairs']]
  for jj in range(co.cols):
   row=list(co[:,jj]);skew=s.zeros(16);pos=0
   for ii in range(16):
    for kk in range(ii+1,16):skew[ii,kk]=row[pos];skew[kk,ii]=-row[pos];pos+=1
   CC=Hi*skew;SS=s.Matrix(4,16,row[126:])
   cols.append(s.Matrix(list(SS*C1+S1*CC-B1*SS)+list(SS*C2+S2*CC-B2*SS)))
  E=s.Matrix.hstack(*cols);rr=s.Matrix(list(-S2)+list(S1))
  ck('all_static_rotating_offsets_inconsistent_'+str(ix),E.to_DM().rank()==31 and E.row_join(rr).to_DM().rank()==32)
  witness,free=E.T.col_join(rr.T).gauss_jordan_solve(s.Matrix([0]*E.cols+[1]));witness=witness.subs({q:0 for q in free})
  ck('offset_dual_witness_'+str(ix),E.T*witness==s.zeros(E.cols,1) and (rr.T*witness)[0]==1)
  offset_witnesses.append([[i,str(q)] for i,q in enumerate(witness) if q])

 a=s.symbols('a0:3',real=True);ap=s.symbols('ap0:3',real=True);b,bp,v,alpha,u,up,m,n,p,q,r,ss=s.symbols('b bp v alpha u up m n p q r ss',real=True)
 B=m*B1+n*B2;Bp=p*B1+q*B2;Bpp=r*B1+ss*B2
 W=s.Matrix(4,4,s.symbols('w0:16'));G=[a[i]*J+b*D[i]*J for i in range(3)];Gp=[ap[i]*J+bp*D[i]*J for i in range(3)]
 for j in range(3):
  E=(-v*I+d[0])*Gp[j]+B*G[j]-G[j]*B+d[j]*W-W*d[j]+(2*alpha*Bp if j==0 else s.zeros(4))
  ck('J_projection_'+str(j),s.expand(s.trace(J.T*E)-4*(-v*ap[j]+(bp/24 if j==0 else 0)))==0)
  ck('DJ_projection_'+str(j),s.expand(s.trace((D[j]*J).T*E)-4*(-v*bp+(ap[0]/24 if j==0 else 0)))==0)
 V=u*I-24*alpha*D[0]*Bp-24*sum((a[i]*D[i]*B*J for i in range(3)),s.zeros(4))
 ck('V_symmetric',V.T==V)
 for j in range(3):ck('first_order_'+str(j),zero(B*G[j]-G[j]*B+d[j]*V-V*d[j]+(2*alpha*Bp if j==0 else s.zeros(4))))
 # Common symmetric commutant is exactly the scalar identity: no V freedom omitted.
 coords=[];Wsym=s.zeros(4)
 for i in range(4):
  for j in range(i,4):
   z=s.Symbol('c'+str(len(coords)));coords.append(z);Wsym[i,j]=Wsym[j,i]=z
 E=s.Matrix([z for Di in D for z in Di*Wsym-Wsym*Di]);A=E.jacobian(coords)
 ck('symmetric_commutant_rank9',A.rank()==9)
 Vp=up*I-24*alpha*D[0]*Bpp-24*sum((a[i]*D[i]*Bp*J for i in range(3)),s.zeros(4))
 Z=(-v*I+d[0])*Vp+B*V-V*B+alpha*Bpp-G[0]*Bp
 ck('trace_identity',s.expand(s.trace(Z)+4*v*up)==0)
 ck('D1_trace_identity',s.expand(s.trace(D[0]*Z)-up/6+192*alpha*(m*p+n*q))==0)
 ck('fixed_direction_acceleration',s.expand(s.trace((D[0]*B1).T*Z).subs({n:0,q:0,ss:0})-96*alpha*v*r)==0)
 # Explicit positive constant Gram for circular mass: necessary Gram test admits it.
 w=s.Symbol('omega',real=True);Bmprime=w*B*J;Bmsecond=-w*w*B
 circular=Z.subs({a[0]:-alpha*w,a[1]:0,a[2]:0,b:0,up:0,p:-w*n,q:w*m,r:-w*w*m,ss:-w*w*n},simultaneous=True)
 ck('circular_Gram_lax',zero(circular))
 Vcircle=V.subs({a[0]:-alpha*w,a[1]:0,a[2]:0,p:-w*n,q:w*m},simultaneous=True)
 ck('circular_constant_V',zero(Vcircle-u*I))
 ck('positive_Gram_completion',zero(-alpha*(w*J/2)**2+(u-alpha*w*w/4)*I-u*I))
 return {'result_id':'K1877','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','identities':{'Gram_span_dimension':4,'V_derivative_coefficient':-24,'V_mass_coefficient':-24,'trace_u_coefficient':-4,'trace_D1_u_coefficient':'1/6','trace_mass_radial_coefficient':-192,'circular_G1':'-alpha*omega*J','circular_positive_threshold':'alpha*omega^2/4'},'scope':{'fixed_positive_pairings':True,'fixed_symbols_and_leading_observation':True,'smooth_travelling_C_S':True,'nonzero_speed':True,'target_two_mass_plane':True,'amplitude_constant':True,'fixed_direction_profile_constant':True,'arbitrary_offsets_allowed':True,'all_moving_backgrounds_excluded':False,'rotating_observation_lift_constructed':False,'native_GU_verdict':False},'offset_dual_witnesses':offset_witnesses,'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json','explorations/conditional-build/k1875-nonlinear-moving-zero-obstruction-2026-10-20.md']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();v=produce()
 if args.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1877',len(v['checks']),'exact matrix/polynomial groups;',len(v['inputs']),'pins')
