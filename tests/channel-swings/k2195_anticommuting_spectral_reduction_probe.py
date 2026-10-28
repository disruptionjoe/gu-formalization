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

def four_root_exclusions():
 out={};ck=lambda k,v:out.__setitem__(k,bool(v));cert={}
 A,C,k,p,q,r,s=S.symbols('A C k p q r s');t,h,d=S.symbols('t h d',nonzero=True)
 B=-Q(85,18);E=Q(49,54);R=Q(124,9)
 # Trace inversion in monic quartic coefficients: A=-mu1/7+4mu_-1/45,
 # C=7mu1-196mu_-1/135; h trace is mu2+A*mu1=23/36.
 m1=(-A+4*t)/8;mi=(-C/E+4/t)/8;m2=(A*A-2*B+4*t*t)/8
 sol=S.solve([A+m1/7-Q(4,45)*mi,C-7*m1+Q(196,135)*mi],[A,C])
 ck('four_5111_A',S.cancel(sol[A]+4*t/31-Q(16,279)/t)==0)
 ck('four_5111_C',S.cancel(sol[C]-140*t/31+Q(812,837)/t)==0)
 ck('four_5111_root',S.cancel((t**4+A*t**3+B*t*t+C*t+E).subs(sol)-(486*t**4-83*t*t-35)/558)==0)
 ck('four_5111_moment',S.cancel((m2+A*m1-Q(23,36)).subs(sol)-(972*t*t+1273)/2232)==0)
 z=-Q(1273,972);ck('four_5111_contradiction',486*z*z-83*z-35!=0)
 # Two pairs, weights3 and1. Reduce original traces only by qs=E.
 m1=(3*p+r)/8;mi=(3*p/q+r/s)/8;m2=(3*(p*p-2*q)+r*r-2*s)/8
 eq1=S.cancel((-p-r)+m1/7-Q(4,45)*mi);eq2=S.cancel((-p*s-r*q)-7*m1+Q(196,135)*mi)
 ck('four_3311_moment',S.expand(m2+(-p-r)*m1-Q(23,36)+(18*p*r+27*q+9*s+23)/36)==0)
 # These two linear equations are an invertible constant row combination of
 # original trace numerators after qs=E; verify reduction directly.
 raw=[S.expand(S.fraction(e0)[0]) for e0 in [eq1,eq2]]
 # Use division by q*s-E, no assumptions on root reality.
 target1=(12985+504*s)*p+(13475+168*q)*r
 target2=(12*s+217)*p+(12*q+203)*r
 ck('four_3311_trace1',S.rem(S.together(eq1*q*s+target1/Q(15120)),q*s-E,s)==0)
 # Once trace1 holds, trace2 is equivalent to target2 (checked via rank).
 rawmat=S.Matrix([[S.cancel(eq.coeff(p)) if False else S.diff(eq,p),S.diff(eq,r)] for eq in [eq1,eq2]])
 targetmat=S.Matrix([[12985+504*s,13475+168*q],[12*s+217,12*q+203]])
 # Direct fixed row combination found algebraically; its determinant is nonzero.
 trans=S.simplify(targetmat*rawmat.inv());trans=trans.applyfunc(lambda x:S.factor(x.subs(s,E/q)))
 ck('four_3311_trace_equivalence',all(not x.has(q) for x in trans) and trans.det()!=0)
 det=S.rem(S.expand(targetmat.det().subs(s,q-Q(62,9))),q*q-Q(62,9)*q-E,q)
 ck('four_3311_determinant',det==59976*q+124656)
 ck('four_3311_no_rank_loss',S.gcd(det,q*q-Q(62,9)*q-E)==1)
 ck('four_3311_contradiction',(Q(13,12))**2-Q(62,9)*Q(13,12)-E!=0)
 # Weights3,2,2,1: distinguished roots sum k,difference d,product h.
 m1=(2*k+d+2*p)/8;mi=((2*k-d)/h+2*p/q)/8
 ck('four_3221_trace1_coordinates',S.expand(m1-(-2*(-k-p)+d)/8)==0)
 ck('four_3221_inverse_coordinates',S.cancel(mi-(-2*(-h*p-k*q)/(h*q)-d/h)/8)==0)
 m2=(2*k*k-4*h+k*d+2*p*p-4*q)/8
 ck('four_3221_moment_coordinates',S.expand(8*(m2+(-k-p)*m1-Q(23,36))+d*p+4*(h+q+k*p)+Q(46,9))==0)
 U=(81*h+28)/(1350*h);W=49*(9*h+2)/(270*h)
 m1=(-2*A+d)/8;mi=(-2*C/E-d/h)/8
 sol=S.solve([A+m1/7-Q(4,45)*mi,C-7*m1+Q(196,135)*mi],[A,C])
 ck('four_3221_trace_solution',S.cancel(sol[A]+d*U)==0 and S.cancel(sol[C]-d*W)==0)
 Z=h+R*U+E/h-B
 f=S.together(R**2*(W+U*E/h)-R*(E/h-h)*Z)
 g=S.together(R**2*(U*U-1)+(-U*R-3*h+E/h-B)*Z)
 # Trace gives p=R/d,k=d*U-R/d; B gives d² Z=R².
 ck('four_3221_B',S.cancel((h+E/h+(d*U-R/d)*R/d-B)-(Z-R**2/d**2))==0)
 ck('four_3221_C',S.cancel((d*W+h*R/d+(d*U-R/d)*E/h)*d-(d*d*(W+U*E/h)-R*(E/h-h)))==0)
 ck('four_3221_difference',S.cancel(((d*U-R/d)**2-d*d-4*h)-(d*d*(U*U-1)-2*U*R+R*R/d**2-4*h))==0)
 def bezout(label,f,g):
  f=S.Poly(S.fraction(S.cancel(f))[0],h).primitive()[1].as_expr();g=S.Poly(S.fraction(S.cancel(g))[0],h).primitive()[1].as_expr()
  u,v,gg=S.gcdex(f,g,h);ck(label,gg==1 and S.expand(u*f+v*g)==1)
  cert[label]=dict(polynomials=[str(f),str(g)],bezout=[str(u),str(v)])
 bezout('four_3221_bezout',f,g)
 # Weights4,2,1,1. Distinguished roots distinct => d!=0; h!=0.
 qh=E/h;f0=k+d-p;g0=(k-d)/h-p/qh
 m1=(3*k+d+p)/8;mi=((3*k-d)/h+p/qh)/8
 ck('four_4211_trace_coordinates',S.expand(m1-(-2*A+f0)/8).subs(A,-k-p)==0)
 ck('four_4211_inverse_coordinates',S.cancel((mi-(-2*C/E+g0)/8).subs(C,-h*p-k*qh))==0)
 sol=S.solve([A+m1/7-Q(4,45)*mi,C-7*m1+Q(196,135)*mi],[A,C])
 # Original trace system, after Vieta substitution, equivalent to the following.
 tr1=S.expand(-k-p+3*f0/50-Q(14,675)*g0)
 tr2=S.expand(-h*p-k*qh-49*f0/30+Q(49,135)*g0)
 direct=[S.expand(x) for x in [(-k-p)+m1/7-Q(4,45)*mi,(-h*p-k*qh)-7*m1+Q(196,135)*mi]]
 m=S.Matrix([[S.diff(x,k),S.diff(x,p),S.diff(x,d)] for x in direct]);n=S.Matrix([[S.diff(x,k),S.diff(x,p),S.diff(x,d)] for x in [tr1,tr2]])
 transform=S.simplify(n[:,:2]*m[:,:2].inv());ck('four_4211_trace_equivalence',all(S.cancel(x)==0 for x in transform*m-n) and transform.det()!=0)
 m2=(Q(3,2)*(k*k+d*d)+k*d+p*p-2*qh)/8
 ck('four_4211_moment_coordinates',S.expand((8*(m2+(-k-p)*m1-Q(23,36))).subs(d*d,k*k-4*h)+4*(h+qh+k*p)+d*p-(2*qh-2*h-Q(46,9)))==0)
 mat=S.Matrix([[x.coeff(k),x.coeff(p)] for x in [tr1,tr2]]);delta=1566*h*h-3732*h-707
 ck('four_4211_determinant',S.cancel(mat.det()-7*delta/(8100*h))==0)
 aug=mat.row_join(S.Matrix([-tr1.coeff(d),-tr2.coeff(d)]));minors=[S.fraction(S.factor(aug[:,ij].det()))[0] for ij in [(0,1),(0,2),(1,2)]]
 bezout('four_4211_singular_rank',minors[0],minors[1])
 sol=S.solve([tr1,tr2],[k,p]);alpha=S.cancel(sol[k]/d);beta=S.cancel(sol[p]/d);rr=R+2*qh-2*h
 ck('four_4211_alpha',S.cancel(alpha-2*(27*h*h+957*h+203)/delta)==0)
 ck('four_4211_beta',S.cancel(beta+7*(2430*h*h+657*h+28)/(9*h*delta))==0)
 # Multiply dp=rr with k=alpha*d,p=beta*d and d²=k²-4h.
 # Never divide by beta or rr: their zero branches are retained.
 bezout('four_4211_bezout',alpha*rr-(B-h-qh),rr*(alpha*alpha-1)-4*h*beta)
 return out,cert

def three_root_exclusions():
 out={};cert={};ck=lambda k,v:out.__setitem__(k,bool(v))
 h=S.symbols('h',nonzero=True);k,p,d,j=S.symbols('k p d j');xs=[k,p,d,j]
 B=-Q(85,18);E=Q(49,54);q=E/h
 def numerator(f):return S.Poly(S.fraction(S.cancel(f))[0],h).primitive()[1].as_expr()
 def coprime(label,expressions,allow_h=False,expected=None):
  polys=[numerator(f) for f in expressions];g=polys[0];coeff=[S.Integer(1)]
  for f in polys[1:]:
   u,v,ng=S.gcdex(g,f,h);coeff=[S.cancel(u*c) for c in coeff]+[v];g=ng
  ck(label+'_identity',S.expand(sum(c*f for c,f in zip(coeff,polys))-g)==0)
  ck(label+'_excluded',(expected is not None and S.expand(g-expected)==0) or S.degree(g,h)==0 or (allow_h and S.Poly(g,h).terms()==[((S.degree(g,h),),S.Integer(1))]))
  cert[label]=dict(polynomials=list(map(str,polys)),bezout=list(map(str,coeff)),gcd=str(g),nonzero_h=allow_h)
 # Equal pair weights1,2,3 and distinguished supported/missing roots.
 for N,Delta,c in [(6,6,1),(4,4,2),(2,2,3)]:
  label='three_'+str(N)+str(c)+str(c)+'0'
  m1=(N*k+Delta*d+2*c*p)/16;mi=((N*k-Delta*d)/h+2*c*p/q)/16
  m2=(N*(k*k+d*d)+2*Delta*k*d+4*c*(p*p-2*q))/32
  # Universal h trace after d²=k²-4h and Vieta B.
  reduced=S.expand((m2+(-k-p)*m1-Q(23,36))*16).subs(d*d,k*k-4*h)
  ck(label+'_moment',S.expand(reduced+Delta*p*d+2*(N-4)*(h-q)+8*(h+q+k*p)+Q(92,9))==0)
  rows=[S.expand(-k-p+m1/7-Q(4,45)*mi),S.expand(-h*p-q*k-7*m1+Q(196,135)*mi)]
  M=S.Matrix([[S.diff(row,x) for x in [k,p]] for row in rows]);v=S.Matrix([-S.diff(row,d) for row in rows]);alpha,beta=map(S.cancel,M.inv()*v)
  ck(label+'_trace_solution',all(S.cancel(x)==0 for x in M*S.Matrix([alpha,beta])-v))
  fs=[4*h*alpha*beta-(B-h-q)*(alpha*alpha-1),4*h*Delta*beta-(Q(248,9)-2*(N-4)*(h-q))*(alpha*alpha-1)]
  coprime(label+'_generic',fs)
  aug=M.row_join(v);coprime(label+'_singular_nonzero_d',[aug[:,inds].det() for inds in [(0,1),(0,2),(1,2)]])
  # d=0 implies k²=4h!=0; p/k is fixed by Vieta B. No trace-rank division.
  coprime(label+'_zero_d',list(M*S.Matrix([1,(B-h-q)/(4*h)]))+[2*(N-4)*(h-q)-Q(248,9)])
 # Unequal pairs: exact two-chart elimination, valid even if missing root repeats.
 for weights in [(5,0,2,1),(4,0,3,1)]:
  n1,n2,n3,n4=weights;N1=n1+n2;D1=n1-n2;N2=n3+n4;D2=n3-n4;label='three_'+''.join(map(str,weights))
  m1=(N1*k+D1*d+N2*p+D2*j)/16;mi=((N1*k-D1*d)/h+(N2*p-D2*j)/q)/16
  m2=(N1*(k*k+d*d)+2*D1*k*d+N2*(p*p+j*j)+2*D2*p*j)/32
  rows=[-k-p+m1/7-Q(4,45)*mi,-h*p-q*k-7*m1+Q(196,135)*mi]
  mat=S.Matrix([[S.diff(row,x) for x in xs] for row in rows]);charts=[]
  for inds in [(0,1),(0,2)]:
   M=mat[:,inds];det=S.factor(M.det());free=[x for i,x in enumerate(xs) if i not in inds];rhs=-mat[:,[i for i in range(4) if i not in inds]]*S.Matrix(free)
   sol=M.inv()*rhs;subs={xs[ind]:S.cancel(sol[ii]) for ii,ind in enumerate(inds)}
   ck(label+'_chart_'+str(inds),all(S.cancel(row.subs(subs,simultaneous=True))==0 for row in rows))
   eqs=[k*p+h+q-B,d*d-k*k+4*h,j*j-p*p+4*q,m2+(-k-p)*m1-Q(23,36)]
   forms=[S.Poly(S.cancel(eq.subs(subs,simultaneous=True)),*free) for eq in eqs];mon=[free[0]**2,free[0]*free[1],free[1]**2]
   F=S.Matrix([[S.factor(z.coeff_monomial(m)) for m in mon]+[S.factor(z.coeff_monomial(1))] for z in forms])
   ck(label+'_quadratic_reconstruction_'+str(inds),all(S.cancel(sum(F[i,l]*mon[l] for l in range(3))+F[i,3]-forms[i].as_expr())==0 for i in range(4)))
   f=S.factor(F.det(method='domain-ge'));T=F[:3,:3];v=-T.adjugate()*F[:3,3];g=S.factor(v[1]*v[1]-v[0]*v[2])
   # F annihilates (u²,uv,v²,1); detF=0 and adjugate quadratic are
   # necessary even when T singular. No division by detT or free roots.
   charts.append((det,f,g,F))
  coprime(label+'_second_chart',charts[1][1:3],allow_h=True)
  coprime(label+'_trace_charts_cover',[charts[0][0],charts[1][0]])
  coprime(label+'_first_chart_at_second_singularity',[charts[0][1],charts[0][2],charts[1][0]],expected=h+Q(1,18) if n1==5 else None)
  if n1==5:
   F0=charts[0][3].subs(h,-Q(1,18));ck('three_5021_exceptional_rank',F0[:,:3].rank()==2 and F0.rank()==3)
   cert['three_5021_exceptional_rank']=dict(h='-1/18',matrix=[[str(x) for x in row] for row in F0.tolist()],coefficient_rank=2,augmented_rank=3)
 return out,cert

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
 cs,found,pairs=algebra();fc,char=fock();cs.update(fc);fcs,four=four_root_exclusions();tcs,three=three_root_exclusions();cs.update(fcs);cs.update(tcs);assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={}
 for f in ['e_cross','census_coefficient','quartic_coefficient']:
  bad=[k for k,v in algebra(f)[0].items() if not v];assert bad,('undetected',f);faults[f]=bad
 for f in ['pairing_sign','trivector_sign']:
  bad=[k for k,v in fock(f)[0].items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2195-anticommuting-spectral-reduction-2026-10-28.md','explorations/conditional-build/k2193-noncommuting-clifford-constraints-2026-10-28.md','tests/channel-swings/k2193_noncommuting_clifford_constraints_probe.py','lab/process/k2193-noncommuting-clifford-constraints.json']
 report=dict(result_id='K2195',status='conditional_exact_exclusions',checks=cs,fault_failures=faults,trace_census=dict(compositions=6545,survivors=[list(row) for row in found]),two_root_bezout=pairs,four_root_certificates=four,three_root_certificates=three,fixture_chiral_characteristic=char,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written joint-triangular trace proof and Chevalley/Pfaffian/chiral-transfer argument; complete finite census and exact elimination certificates. Fock fixtures are controls, not a search over all forms. All one/two/three/four-root weighted spectra are excluded, including singular charts, missing-root coincidences and Jordan structure. Every anticommuting adapter in the fixed normalized family is excluded; general noncommuting adapters remain open.')
 dst=ROOT/'lab/process/k2195-anticommuting-spectral-reduction.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2195',controls=len(cs),faults={k:len(v) for k,v in faults.items()},census=6545,quintic_pairs=len(pairs),fixture=char)))
if __name__=='__main__':main()
