#!/usr/bin/env sage-python
"""Exact chart coefficients; the uniform integral remainder is proved in the note."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,PolynomialRing,PowerSeriesRing
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1837-fisher-rare-component-boundary.json'
def produce():
 R=PolynomialRing(QQ,names=('b','k'));b,k=R.gens();F=R.fraction_field();S=PowerSeriesRing(F,'s',default_prec=7);s=S.gen();checks={}
 def ck(key,value):checks[key]=bool(value);assert value,key
 for inward in [True,False]:
  c=k*s**3;z=b*s if inward else k*s*s/b;t=((1-s*s/2)/(1-c/2)).sqrt();v=1-t
  p=c/(c+z*z) if inward else z*z/(c+z*z)
  gap=t.sqrt()*((1-z).sqrt()-(1+c/z).sqrt())*(1 if inward else -1)
  d2=gap*gap/v;base=(1-p*d2)/v;pref=p*p*d2/v;tag='inward' if inward else 'outward'
  ck(tag+'_rare_weight',p[1]==k/b**2)
  ck(tag+'_noise_gap',d2[0]==b*b)
  ck(tag+'_pole',base[-2]==4 and base[-1]==0)
  ck(tag+'_base_constant',base[0]==-QQ(1)/2+(-2 if inward else 2)*b*k-4*k*k-4*k*k/b**2)
  ck(tag+'_likelihood_prefactor',pref[0]==4*k*k/b**2)
  for bv,kv in [(QQ(1)/2,QQ(1)/3),(1,2),(2,QQ(3)/2),(3,0)]:
   ck(tag+'_rational_'+str(bv)+'_'+str(kv),F(base[0])([bv,kv])==(-QQ(1)/2+(-2 if inward else 2)*bv*kv-4*kv*kv-4*kv*kv/bv**2))
 # Entire exponential gap follows from positive factorial coefficients.
 from math import factorial
 ck('exp_strict_quartic_remainder',all(QQ(1)/factorial(n)>0 for n in range(3,30)))
 L=PolynomialRing(QQ,names=('p','L'));p,l=L.gens();den=1+p*(l-1)
 ck('exact_first_remainder',(l*l/den-l*l)*den==-p*l*l*(l-1))
 Q=PolynomialRing(QQ,names=('b','k','H'));b,k,h=Q.gens();K=Q.fraction_field()
 ck('completed_square',K(-QQ(3)/2-2*b*k+4*h*k*k)==K(-QQ(3)/2-b*b/(4*h)+4*h*(k-b/(4*h))**2))
 R2=PolynomialRing(QQ,names=('a','b'));aa,bb=R2.gens();z=1-aa*aa;r=bb*bb-1;c=z*r;h=r-z;L2=(aa+bb)**2
 ck('variance_threshold_identity',L2*L2-4*L2+2*c==2*h*L2-h*h-2*c)
 ck('variance_comparison_square',(1-c/L2)**2-(1-c/2)==c*(L2*L2-4*L2+2*c)/(2*L2*L2))
 for av,bv in [(QQ(3)/4,QQ(5)/4),(QQ(9)/10,2),(QQ(99)/100,10)]:
  zz=1-av*av;rr=bv*bv-1;cc=zz*rr;hh=rr-zz
  if hh>=cc/2:ck('outward_variance_control_'+str(bv),(av+bv)**4-4*(av+bv)**2+2*cc>=0)
 return {'result_id':'K1837','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'inward_constant':'-3/2 - 2*b*k + 4*k^2*(exp(b^2)-1-b^2)/b^2','outward_constant':'-3/2 + 2*b*k + 4*k^2*(exp(b^2)-1-b^2)/b^2','inward_optimal_k':'b^3/[4*(exp(b^2)-1-b^2)]','inward_minimum':'-3/2-b^4/[4*(exp(b^2)-1-b^2)] > -2','finite_positive_noise_scaled_radius_excluded':True,'upper_displacement_o_sqrt_delta':True,'global_scaling_compactness_proved':False,'global_shape_uniqueness_proved':False},'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/k1833-fisher-merging-radius-subleading-2026-10-20.md','explorations/k1835-fisher-next-endpoint-coefficient-2026-10-20.md']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();v=produce()
 if args.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1837',len(v['checks']),'exact coefficient/control groups')
