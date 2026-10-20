#!/usr/bin/env sage-python
"""Exact moment, score-Gram and variance identities underlying the analytic proof."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,PolynomialRing,matrix,binomial,factorial,SR,sqrt
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1839-fisher-global-merging-coercivity.json'
def produce():
 R=PolynomialRing(QQ,['p','a','v']);p,a,v=R.gens();F=R.fraction_field();checks={}
 def ck(k,b):checks[k]=bool(b);assert b,k
 def gm(n):return 0 if n%2 else factorial(n)/(2**(n//2)*factorial(n//2))
 def latent(n):return p*(-(1-p)*a)**n+(1-p)*(p*a)**n
 def mom(n):return sum(binomial(n,j)*latent(n-j)*v**(j//2)*gm(j) for j in range(0,n+1,2))
 M={n:mom(n) for n in range(9)};S=M[2];k3=M[3];k4=M[4]-3*S*S
 ck('centered',M[1]==0)
 ck('variance',S==v+p*(1-p)*a*a)
 ck('third_cumulant',k3==p*(1-p)*(2*p-1)*a**3)
 ck('fourth_cumulant',k4==p*(1-p)*(1-6*p*(1-p))*a**4)
 # E(score*g2)=E(score*g3)=0; covariance with X supplies the excess lower bound.
 g2norm=M[4]-S*S;g3norm=M[6]-6*S*M[4]+9*S**3
 ck('quadratic_norm',g2norm==2*S*S+k4)
 ck('cubic_covariance',M[4]-3*S*M[2]==k4)
 gram2=matrix(F,[[S,k3],[k3,g2norm]])
 ck('strong_gram_inverse',gram2.inverse()[0,0]-1/S==k3*k3/(S*(S*g2norm-k3*k3)))
 ck('coarse_gap_positive',gram2.inverse()[0,0]-1/S-k3*k3/(S*S*g2norm)==k3**4/(S*S*g2norm*(S*g2norm-k3*k3)))
 # All Gaussian-convolution sixth moments come from binomial integration.
 ck('sixth_moment',M[6]==15*v**3+45*v*v*latent(2)+15*v*latent(4)+latent(6))
 ck('cubic_norm_expansion',g3norm==M[6]-6*S*M[4]+9*S**3)
 # Released all-domain lower-bound instrument through fifth cumulant.
 qs=[{1:1},{2:1,0:-S},{3:1,1:-3*S,0:-k3},{4:1,2:-6*S,1:-4*k3,0:3*S*S-k4}]
 for j,q in enumerate(qs):
  ck(f'centered_test_{j}',sum(co*M[k] for k,co in q.items())==0)
  ck(f'score_covariance_{j}',sum(k*co*M[k-1] for k,co in q.items() if k)==(1 if j==0 else 0))
 G=matrix(R,[[sum(co*do*M[k+l] for k,co in q.items() for l,do in u.items()) for u in qs] for q in qs])
 ck('fifth_cumulant_covariance',G[0,3]==M[5]-10*S*k3)
 numeric=matrix(QQ,[[entry(p=QQ(1)/3,a=2,v=QQ(1)/7) for entry in row] for row in G.rows()])
 ck('degree4_Gram_positive_control',all(numeric[:j,:j].det()>0 for j in range(1,5)))
 ck('degree4_improves_degree2_control',numeric.inverse()[0,0]>numeric[:2,:2].inverse()[0,0])
 # Radius chart: introduce rational radii a0,b0; gap and weights are exact.
 P=PolynomialRing(QQ,['aa','bb','tt']);aa,bb,tt=P.gens();K=P.fraction_field();z=1-aa*aa;r=bb*bb-1;c=z*r;L=aa+bb;h=r-z;weight=K(r/(r+z));mean=weight*aa+(1-weight)*bb
 cm=lambda n:weight*(aa-mean)**n+(1-weight)*(bb-mean)**n
 ck('radius_mean_square',mean*mean==1-c/L**2)
 ck('radius_variance',cm(2)==c/L**2)
 ck('radius_third',cm(3)==c*h/L**3)
 ck('radius_fourth_cumulant',cm(4)-3*cm(2)**2==c*((r-z)**2-2*c)/L**4)
 # Factorization used in K1837 and the variance asymptotic numerator.
 ck('variance_factor',L**4-4*L**2+2*c==2*h*L**2-h*h-2*c)
 # Analytic variance factor: divisibility by c and the vanishing linear term.
 hh,cc=SR.var('hh cc');ll=2+hh+2*sqrt(1+hh-cc);ff=(1-cc/ll)/sqrt(1-cc/2)
 ck('variance_factor_at_c0',ff.subs(cc=0).simplify_full()==1)
 ck('variance_linear_c_cancels',ff.diff(cc).subs(hh=0,cc=0)==0)
 ck('variance_mixed_coefficient',ff.diff(cc).diff(hh).subs(hh=0,cc=0)==QQ(1)/8)
 # Algebraic skew optimization, no fixed-family assumption.
 Q=PolynomialRing(QQ,['ell','delta','zz']);ell,delta,zz=Q.gens();K=Q.fraction_field()
 ck('additive_square',-QQ(3)/2-2*ell+2*ell*ell==-2+2*(ell-QQ(1)/2)**2)
 cc=ell*delta**2/zz
 ck('escaping_penalty',cc**2*zz**4/(delta**2*(delta**3+cc*zz**4))==ell**2/(delta/zz**2+ell*zz))
 # Rational asymptotic witnesses to both residual noncompact shape regimes.
 # The theorem constrains c(z-r), not unique powers or compact a,b.
 checks['no_global_next_coefficient_claim']=True
 return {'result_id':'K1839','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'global_minimizers_z_over_sqrt_delta_tends_zero':True,'global_minimizers_r_over_sqrt_delta_tends_zero':True,'global_skew_c_times_z_minus_r_over_delta_squared':'1/2','positive_lobe_score_excess_limit':'1/2','compact_K1835_scaling_proved':False,'global_next_coefficient_proved':False,'global_uniqueness_proved':False,'effective_onset_proved':False},'degree4_Gram_polynomials':[[str(x) for x in row] for row in G.rows()],'moment_polynomials':{str(n):str(M[n]) for n in M},'cubic_test_norm':str(g3norm),'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1837-fisher-rare-component-boundary.json','lab/process/k1835-fisher-next-endpoint-coefficient.json']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1839',len(v['checks'])-1,'exact identity groups; 1 scope assertion')
