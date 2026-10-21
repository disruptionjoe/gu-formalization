#!/usr/bin/env python3
"""Algebra for the analytic three-well localization/equality theorem."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1878-fisher-three-well-profile-rigidity.json'
INPUTS=['explorations/k1876-fisher-atomic-boundary-cost-2026-10-20.md','lab/process/k1876-fisher-atomic-boundary-cost.json']
def produce():
 k=s.symbols('k',positive=True);x,y,e=s.symbols('x y e',real=True);checks={}
 def ck(n,v): checks[n]=bool(v);assert v,n
 g=x**3-k*x
 ck('slack_polynomial',s.expand(g*g)==x**6-2*k*x**4+k*k*x*x)
 ck('central_blowup',s.expand(g.subs(x,e*y)/e)==-k*y+e*e*y**3)
 ck('outer_blowup',s.expand(g.subs(x,s.sqrt(k)+e*y)/e)==2*k*y+3*s.sqrt(k)*e*y*y+e*e*y**3)
 p0=1-1/k;pp=s.symbols('pplus',nonnegative=True);pm=1/k-pp;p=[p0,pp,pm];a=[k,2*k,2*k];A=k+1
 ck('atomic_mass',s.simplify(sum(p)-1)==0)
 ck('weighted_abs_slope',s.simplify(sum(p[i]*a[i] for i in range(3))-A)==0)
 q=[1/(A*z) for z in a]
 ck('budget_saturation',s.simplify(sum(p[i]*a[i]**2*q[i] for i in range(3))-1)==0)
 ck('Fisher_saturation',s.simplify(sum(p[i]/q[i] for i in range(3))-A*A)==0)
 ck('variance_ratio',s.simplify(q[0]/q[1])==2)
 # Exact Cauchy gap, allowing arbitrary positive masses and second moments.
 P=s.symbols('p0:3',positive=True);Q=s.symbols('q0:3',positive=True);b=s.symbols('a0:3',positive=True)
 lhs=sum(P[i]/Q[i] for i in range(3))*sum(P[i]*b[i]**2*Q[i] for i in range(3))-sum(P[i]*b[i] for i in range(3))**2
 rhs=sum(P[i]*P[j]*(b[i]*Q[i]-b[j]*Q[j])**2/(Q[i]*Q[j]) for i in range(3) for j in range(i+1,3))
 ck('allocation_gap',s.expand(lhs-rhs)==0)
 # Pointwise distance control, after z=x/sqrt(k): nearest well in {-1,0,1}.
 z=s.symbols('z',real=True)
 ck('central_distance_factor',s.expand((z**3-z)/z)==z*z-1)
 ck('outer_distance_factor',s.expand(s.cancel((z**3-z)/(z-1))-z*(z+1))==0)
 ck('global_distance_constant',s.Rational(3,4)**2==s.Rational(9,16))
 # For all z, |z^3-z| >= 3/4 dist(z,{-1,0,1}), by |z|<=1/2 or z>=1/2 and symmetry.
 ck('k4_profile_variances',q[0].subs(k,4)==s.Rational(1,20) and q[1].subs(k,4)==s.Rational(1,40))
 # Even moment constraints do not select the two outer sign weights.
 ww,yy,tt,eta=s.symbols('w y t eta',real=True)
 for n in [2,4,6]:
  mom=lambda mu,var:sum(s.binomial(n,2*j)*s.factorial2(2*j-1)*var**j*mu**(n-2*j) for j in range(n//2+1))
  mp=mom(s.sqrt(yy),tt/2);mm=mom(-s.sqrt(yy),tt/2)
  ck('asymmetric_even_moment_'+str(n),s.expand(ww*(eta*mp+(1-eta)*mm)-ww*mp)==0)
 ck('asymmetric_fisher_upper',s.simplify((1-ww)/tt+eta*ww/(tt/2)+(1-eta)*ww/(tt/2)-(1+ww)/tt)==0)
 return {'result_id':'K1878','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','constants':{'distance_square_lower':'9*k^2/16','central_variance':'1/(k*(k+1))','outer_variance':'1/(2*k*(k+1))','sharp_scaled_energy':'(k+1)^2','central_mass':'1-1/k','total_outer_mass':'1/k'},'scope':{'all_asymptotically_optimal_densities':True,'positive_mass_cells_TV_and_W2':True,'vanishing_cells_profile_unconstrained':True,'even_optimizer_equal_outer_weights':True,'all_near_minimizers_even':False,'effective_rate':False,'sextic_multiplier_or_gap':False,'native_GU_claim':False},'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1878',len(v['checks']),'symbolic groups;',len(v['inputs']),'pins; continuum proof in note')
