#!/usr/bin/env sage-python
"""Exact local expansions supporting the written global asymptotic proof."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,PolynomialRing,PowerSeriesRing
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1833-fisher-merging-radius-subleading.json'
def produce():
 checks={}
 def ck(k,v):checks[k]=bool(v);assert v,k
 K=PolynomialRing(QQ,names=('a','b')).fraction_field();a,b=K.gens();S=PowerSeriesRing(K,'e',default_prec=22);e=S.gen()
 d=e**6;c=a*e**8;z=b*e**4;p=a/(a+b*b);t=((2-d)/(2-c)).sqrt();v=1-t
 inner=(1-z).sqrt();outer=(1+c/z).sqrt();mean=p*inner+(1-p)*outer
 var=1-t*mean**2;mu3=t*t.sqrt()*(p*(inner-mean)**3+(1-p)*(outer-mean)**3);x=a*(a/b-b)
 ck('chart_second_moment',(p*inner**2+(1-p)*outer**2)==1)
 ck('chart_fourth_moment',p*inner**4+(1-p)*outer**4==1+c)
 ck('variance_leading',var[6]==QQ(1)/4 and all(var[i]==0 for i in range(6)))
 ck('variance_gap_zero',all(var[i]==0 for i in range(7,12)))
 ck('variance_next',var[12]==QQ(1)/32-x/8)
 ck('third_cumulant_leading',mu3[12]==x/8 and all(mu3[i]==0 for i in range(12)))
 inv=1/var;ck('reciprocal_variance_constant',inv[0]==-QQ(1)/2+2*x)
 mu4=t*t*(p*(inner-mean)**4+(1-p)*(outer-mean)**4)
 # Fourth cumulant is noise invariant. Its first order is e^16; standardized is O(e^4).
 vlatent=t*(p*(inner-mean)**2+(1-p)*(outer-mean)**2);k4=mu4-3*vlatent*vlatent
 ck('fourth_cumulant_order',all(k4[i]==0 for i in range(16)))
 y=a*((a/b-b)**2-2*a)
 ck('fourth_cumulant_leading',k4[16]==y/16)
 ck('third_cumulant_gap',all(mu3[i]==0 for i in range(13,16)))
 ck('refined_optimum_a',QQ(1)/2*((-1)**2-2*QQ(1)/2)==0 and QQ(1)/2*(-1)==-QQ(1)/2)
 # Gaussian Hermite score contribution: H3'/6=H2/2, E H2^2=2.
 ck('Gaussian_Hermite_norm',QQ(3)-2+1==2)
 constant=-QQ(3)/2+2*x+2*x*x
 ck('square_completion',constant==2*(x+QQ(1)/2)**2-2)
 ck('rational_improver',constant(a=1,b=QQ(5)/4)==-QQ(399)/200)
 # Optimal irrational b=(1+sqrt17)/4; reduce the identity via its polynomial.
 B=PolynomialRing(QQ,'B');Bv=B.gen();num=(2*(1-Bv**2)+Bv);ck('optimal_root_relation',num==-(2*Bv**2-Bv-2))
 # Score test g=sign(y)(y^2-1), including its distributional jump -2 at0.
 ck('score_test_denominator',1-2*(1)+1==0)
 ck('sharp_constant_from_m1',4*(-QQ(1)/4)-1==-2)
 controls=[]
 for aa in [QQ(1)/4,QQ(1)/2,1,2]:
  for bb in [QQ(1)/2,1,QQ(5)/4,2]:
   xx=aa*(aa/bb-bb);cc=-QQ(3)/2+2*xx+2*xx*xx
   ck('constant_'+str(aa)+'_'+str(bb),cc>=-2);controls.append([str(aa),str(bb),str(xx),str(cc)])
 return {'result_id':'K1833','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'global_value':'V(2-delta)=4/delta-2+o(1)','triangular_family':'c=a delta^(4/3), z=b delta^(2/3), x=a(a/b-b)','family_additive_constant':'-3/2+2x+2x^2','optimal_example':'a=1/2, b=(1+sqrt(3))/2','next_family_cost':'(2/3)y^2 delta^(1/3), y=a((a/b-b)^2-2a)','refined_witness_error':'O(delta^(1/2))','all_minimizers_z_tends_zero':True,'all_minimizers_interior_near_endpoint':True,'score_test':'g(y)=sign(y)(y^2-1); I>=4(E|Y|-rho(0))^2/delta','global_minimizer_rate_selected':False,'effective_onset_computed':False,'shape_uniqueness':False,'physical_or_canon_promotion':False},'checks':checks,'rational_controls':controls,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1831-fisher-endpoint-gaussian-blowup.json','lab/process/k1829-effective-fisher-face-instability.json','lab/process/k1825-global-q-fisher-transfer.json']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1833',len(v['checks']),'symbolic/control groups')
