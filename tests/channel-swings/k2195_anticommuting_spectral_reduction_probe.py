#!/usr/bin/env python3
"""Exact trace census, Pfaffian pairing controls and nonzero-trace eliminations."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from itertools import combinations
import argparse,hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2];Q=S.Rational

def algebra(fault=None):
 out={};ck=lambda k,v:out.__setitem__(k,bool(v))
 a,c,r,s,x,e=S.symbols('a c r s x e');n,m,k=S.symbols('n m k',integer=True);l=32-n-m-k
 E=245*r*r+(1276 if fault=='e_cross' else 1275)*r*s+270*s*s+(98*a-294*c)*r+(510*a-810*c)*s
 mixed=S.expand(E.subs(r,(99*s-28*a-252*c)/21));ck('mixed_factor',S.factor(mixed-Q(8,63)*(-49*a-693*c+270*s)*(-49*a-441*c+342*s))==0)
 types=[((-2*a+6*c)/5,0),(0,(-17*a+27*c)/9),((-43*a+9*c)/90,(49*a+693*c)/270),(-25*(a+9*c)/38,49*(a+9*c)/342)]
 tr1=S.expand(sum(w*rs[0] for w,rs in zip([n,m,k,l],types))-32*a);tr2=S.expand(sum(w*rs[1] for w,rs in zip([n,m,k,l],types))-32*c)
 mat=S.Matrix([[tr1.coeff(a),tr1.coeff(c)],[tr2.coeff(a),tr2.coeff(c)]])
 poly=1875*k*m+98*k*n-(12321 if fault=='census_coefficient' else 12320)*k+1875*m*m+2125*m*n-70800*m+98*n*n+1568*n+53760
 ck('trace_determinant',S.expand(mat.det()-Q(2,285)*poly)==0)
 found=[]
 for nn in range(33):
  for mm in range(33-nn):
   for kk in range(33-nn-mm):
    pp=1875*kk*mm+98*kk*nn-(12321 if fault=='census_coefficient' else 12320)*kk+1875*mm*mm+2125*mm*nn-70800*mm+98*nn*nn+1568*nn+53760
    if pp==0:found.append((nn,mm,kk,32-nn-mm-kk))
 ck('complete_6545_census',found==[(18,8,6,0),(20,0,12,0)])
 for counts,ratio in [((18,8,6,0),Q(333,631)),((20,0,12,0),Q(27,49))]:
  ma=mat.subs({n:counts[0],m:counts[1],k:counts[2]});ck('trace_kernel_'+str(counts),ma.rank()==1 and ma*S.Matrix([ratio,1])==S.zeros(2,1))
  for j,count in enumerate(counts):
   if count:
    rr=S.sympify(types[j][0]).subs({a:ratio,c:1});ss=S.sympify(types[j][1]).subs({a:ratio,c:1});ck(f'invertible_D_{counts}_{j}',49*rr+225*ss!=0)
 ck('first_H_pair_square',Q(96*1680,631**2)==(48*S.sqrt(70)/631)**2)
 ck('second_X_pair_square',-Q(8,3)/(-Q(8,49))==Q(49,3))
 A=245-1275*x*x+270*x**4;B=98*a-294*c-(510*a-810*c)*x*x;C0=21*x+99*x**3;D0=(28*a+252*c)*x+392*e-1800*e*x*x
 F=1080*e*x**4+(-129*a+27*c)*x**3-(5101 if fault=='quartic_coefficient' else 5100)*e*x*x+(49*a+693*c)*x+980*e
 ck('quartic_elimination',S.expand(C0*B-A*D0-2*(225*x*x-49)*F)==0)
 V=(-43*a+9*c)/90+4*e*x-Q(14,9)*e/x;T=(49*a+693*c)/270-Q(52,3)*e*x+Q(98,27)*e/x
 ck('V_first_identity',S.cancel(A*V+B-(18*x*x-7)*F/(18*x))==0)
 ck('V_second_identity',S.cancel(C0*V+D0-Q(11,30)*F)==0)
 ck('T_identity_mod_F',S.rem(S.together(x*x*V+T)*x,F,x)==0)
 ga,gb,g=S.gcdex(A,C0,x);ck('unique_V_bezout',S.expand(ga*A+gb*C0)==1 and g==1)
 mx,mi=S.symbols('mx mi');av=Q(24,7)*mx-Q(6,5)*mi;cv=Q(32,3)*mx-Q(98,45)*mi
 ck('trace_inverse_map',S.expand((-49*av+27*cv)/120-mx)==0 and S.expand((-28*av+9*cv)/14-mi)==0)
 ck('single_root_E',S.factor(E.subs({r:a,s:c}).subs(a,-Q(217,49)*c))==-416*c*c)
 # Characteristic square trace / Vieta: four roots with equal weights, repeats allowed.
 mxv=(129*a-27*c)/4320;miv=-(49*a+693*c)/3920
 ck('balanced_trace1',S.expand(mxv-(-49*a+27*c)/120-(631*a-333*c)/1440)==0)
 ck('balanced_trace_inverse',S.expand(miv-(-28*a+9*c)/14-Q(3,560)*(371*a-153*c))==0)
 ck('balanced_h_trace_gap',4*Q(85,36)-Q(23,9)==Q(62,9))
 # Reconstruct the two-root equations, including every zero-denominator branch.
 y,z,ss=S.symbols('y z ss',nonzero=True);pairs=[]
 for nn in range(1,5):
  mu1=(nn*y+8-nn)*ss/8;mui=(nn/y+8-nn)/(8*ss);mu2=(nn*y*y+8-nn)*ss*ss/8
  aa=Q(24,7)*mu1-Q(6,5)*mui;cc=Q(32,3)*mu1-Q(98,45)*mui
  h=S.cancel(4*mu2+(-43*aa+9*cc)*mu1/90-Q(23,9));hz=S.cancel(h.subs(ss**2,z))
  raw=S.Poly(S.fraction(hz)[0],z);raw_a=raw.coeff_monomial(z);raw_b=raw.coeff_monomial(1)
  ba,bb,gg=S.gcdex(raw_a,raw_b,y)
  ck('raw_h_denominator_'+str(nn),raw.degree()==1 and gg==1 and S.expand(ba*raw_a+bb*raw_b)==1)
  dd=8-nn
  intended=z*(nn*(56-nn)*y*y-2*nn*dd*y+dd*(56-dd))/112+((nn*y+dd)*(nn+dd*y)-460*y)/(180*y)
  ck('raw_h_identity_'+str(nn),S.cancel(hz-intended)==0)
  sol=S.solve(hz,z)[0];num,den=S.fraction(sol)
  bn,bd,bg=S.gcdex(num,den,y);ck('two_root_denominator_'+str(nn),S.expand(bn*num+bd*den)==1 and bg==1)
  polys=[]
  for root in [ss,y*ss]:
   ff=S.cancel(F.subs({a:aa,c:cc,e:1,x:root}));fz=S.Poly(S.fraction(ff)[0],ss)
   assert all(power[0]%2==0 for power,coef in fz.terms())
   gz=sum(coef*z**(power[0]//2) for power,coef in fz.terms());pp=S.Poly(S.fraction(S.cancel(gz.subs(z,sol)))[0],y).primitive()[1].as_expr();polys.append(pp)
  f,g=polys;bf,bg,gg=S.gcdex(f,g,y);ck('two_root_quintic_bezout_'+str(nn),S.degree(f,y)==5 and S.degree(g,y)==5 and gg==1 and S.expand(bf*f+bg*g)==1)
  pairs.append(dict(n=nn,z=str(sol),polynomials=list(map(str,polys)),bezout=[str(bf),str(bg)]))
 return out,found,pairs

def fock(fault=None):
 out={};ck=lambda k,v:out.__setitem__(k,bool(v));gam=[]
 for sign in [1,-1]:
  for j in range(5):
   G=S.zeros(32)
   for mask in range(32):
    parity=(-1)**((mask&((1<<j)-1)).bit_count())
    if not mask&(1<<j):G[mask|(1<<j),mask]=parity
    else:G[mask^(1<<j),mask]=sign*parity
   gam.append(G)
 gam[4]=S.I*gam[4] # complex realization of signature(4,6)
 B=S.zeros(32)
 for mask in range(32):
  comp=31^mask;bits=mask.bit_count();swaps=sum((comp&((1<<j)-1)).bit_count() for j in range(5) if mask&(1<<j))
  B[mask,comp]=(-1)**(bits*(bits-1)//2+swaps)
 if fault=='pairing_sign':B[0,31]=-B[0,31]
 ck('symmetric_opposite_chiral_pairing',B==B.T and B.det()!=0)
 I=S.eye(32);grades=[1]*4+[-1]*6
 for j,G in enumerate(gam):
  ck('gamma_square_'+str(j),G*G==grades[j]*I)
  ck('gamma_adjoint_'+str(j),G.T*B==B*G)
 for i,j in combinations(range(10),2):ck(f'gamma_anticommutator_{i}_{j}',gam[i]*gam[j]+gam[j]*gam[i]==S.zeros(32))
 for i,j,k in combinations(range(10),3):
  W=gam[i]*gam[j]*gam[k];ck(f'trivector_skew_{i}_{j}_{k}',W.T*B==(-1 if fault!='trivector_sign' else 1)*B*W)
 A=gam[0]*gam[1]*gam[2];D=gam[0]*gam[3]*gam[5];w=A+2*D;u=3*A-D
 IN=S.eye(32)
 for G in gam:IN=IN*G
 P=7*IN*w-15*S.I*u;X=u*w.inv();parity=S.diag(*[(-1)**m.bit_count() for m in range(32)])
 ck('fixture_commuting',w*u==u*w);ck('fixture_invertible',w.det()!=0 and P.det()!=0)
 ck('fixture_X_commutes_P',P*X==X*P);ck('odd_P',P*parity==-parity*P)
 ids0=[m for m in range(32) if m.bit_count()%2==0];ids1=[m for m in range(32) if m.bit_count()%2]
 x=S.symbols('x');cp0=X.extract(ids0,ids0).charpoly(x).as_expr();cp1=X.extract(ids1,ids1).charpoly(x).as_expr()
 ck('fixture_chiral_characteristic_equal',cp0==cp1)
 ck('fixture_chiral_square_multiplicities',all(power%2==0 for f,power in S.factor_list(cp0,x)[1]))
 ck('fixture_full_fourth_multiplicities',all(power%4==0 for f,power in S.factor_list(cp0*cp1,x)[1]))
 return out,str(S.factor(cp0))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 cs,found,pairs=algebra();fc,char=fock();cs.update(fc);assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={}
 for f in ['e_cross','census_coefficient','quartic_coefficient']:
  bad=[k for k,v in algebra(f)[0].items() if not v];assert bad,('undetected',f);faults[f]=bad
 for f in ['pairing_sign','trivector_sign']:
  bad=[k for k,v in fock(f)[0].items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2195-anticommuting-spectral-reduction-2026-10-28.md','explorations/conditional-build/k2193-noncommuting-clifford-constraints-2026-10-28.md','tests/channel-swings/k2193_noncommuting_clifford_constraints_probe.py','lab/process/k2193-noncommuting-clifford-constraints.json']
 report=dict(result_id='K2195',status='conditional_exact_exclusions',checks=cs,fault_failures=faults,trace_census=dict(compositions=6545,survivors=[list(row) for row in found]),two_root_bezout=pairs,fixture_chiral_characteristic=char,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written joint-triangular trace proof and Chevalley/Pfaffian/chiral-transfer argument; complete finite census and exact elimination certificates. Fock fixtures are controls, not a search over all forms. Nonzero-J three-root and unequal four-root spectra and original-row reconstruction remain open.')
 dst=ROOT/'lab/process/k2195-anticommuting-spectral-reduction.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2195',controls=len(cs),faults={k:len(v) for k,v in faults.items()},census=6545,quintic_pairs=len(pairs),fixture=char)))
if __name__=='__main__':main()
