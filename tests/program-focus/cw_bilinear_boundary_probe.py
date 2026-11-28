#!/usr/bin/env python3
"""Finite exact controls for the actual local bilinear boundary estimate.
The change-of-variable/functional-analysis proof is written and reviewed.
"""
from pathlib import Path
import argparse,hashlib,json,sys,time
sys.dont_write_bytecode=True
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/cw-bilinear-boundary-certificates.json'
PINS={
'explorations/conditional-build/cw-one-sided-boundary-2026-11-27.md':'220b44e29aa64ba32906141215dc17c77d3d08005117bc90ac6566dd5d3cdc05',
'lab/process/cw-one-sided-boundary-certificates.json':'f4e6666601b25a18bb1288d2fa19493df432e6b3f194fe17b301cf70d81e0ea2',
}
def build():
 checks=[]
 def ck(n,v):
  assert v,n
  checks.append(n)
 deps=dict(PINS);old=json.loads((ROOT/'lab/process/cw-one-sided-boundary-certificates.json').read_text());deps.update(old['dependencies'])
 for p,h in deps.items():ck('reuse '+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
 ck('owned actual full receiver',old['actual_threshold']['ell_b_F']==104448)
 x,y,u,v=s.symbols('x y u v',real=True);omega=s.sqrt(u*u-v*v-3)
 delta=-(x+u)**2+(y+v)**2-36
 nu=s.sqrt(x*x-y*y-3)-omega
 jac=s.Matrix([[s.diff(delta,z)for z in(u,v)],[s.diff(nu,z)for z in(u,v)]])
 ck('actual nonlinear Jacobian',s.simplify(jac.det()-2*(y*u-x*v)/omega)==0)
 center={x:s.Rational(28,3),y:3,u:-s.Rational(28,3),v:3}
 J=jac.subs(center);ck('exact active center matrix',J==s.Matrix([[0,12],[s.Rational(14,13),s.Rational(9,26)]]))
 ck('center Jacobian nonzero',J.det()==-s.Rational(168,13))
 ck('actual threshold and resonance',delta.subs(center)==0 and nu.subs(center)==0)
 ck('common stable input',s.Rational(703,9)>36 and s.Rational(703,9)-3==s.Rational(676,9))
 a,b,c=s.symbols('a b c',real=True)
 M=s.Matrix([[1,0,0,0],[0,1,0,0],[0,c,0,c],[a,-b,a,b]])
 ck('paired CS Jacobian',s.factor(M.det())==-a*c)
 M2=s.Matrix([[0,0,1,0],[0,0,0,1],[1,0,1,0],[0,1,0,1]])
 ck('second paired map determinant',M2.det()==1)
 ck('spectator dimension accounting',13-2==11 and 13+13+13+2+11==2*26)
 # Kernel controls. Delta is an output distance, not a frozen constant.
 la,D,t,z=s.symbols('lambda D t z',positive=True,real=True)
 w2=s.pi/la
 ck('Cauchy kernel integrated in nu',s.integrate(1/(la*la+z*z),(z,-s.oo,s.oo))==w2)
 ck('boundary collar squared norm',s.integrate(2*la*w2,(la,0,s.sqrt(D)))==2*s.pi*s.sqrt(D))
 ck('old double divisor fails',s.integrate(2*la*s.pi/(2*la**3),(la,0,s.sqrt(D)))==s.oo)
 # Fourier transform of (lambda^2+nu^2)^-2, derived by differentiating
 # pi exp(-lambda t)/lambda with respect to lambda.
 fc=s.simplify(-s.diff(s.pi*s.exp(-la*t)/la,la)/(2*la))
 ck('squared resolvent cosine integral',fc==s.pi*(1+la*t)*s.exp(-la*t)/(2*la**3))
 It=s.simplify(s.pi/(2*la**3)*(1+s.exp(-2*la*t))-2*s.exp(-la*t)*fc)
 ck('displacement kernel nu integral',s.simplify(It-s.pi*(1-(1+2*la*t)*s.exp(-2*la*t))/(2*la**3))==0)
 phi=1-(1+z)*s.exp(-z)
 ck('moment integral derivative',s.simplify(s.diff(phi,z)-z*s.exp(-z))==0)
 ck('moment integral lower boundary',s.limit(phi/z,z,0,dir='+')==0)
 ck('moment integral upper boundary',s.limit(phi/z,z,s.oo)==0)
 ck('moment integral after parts',s.integrate(s.exp(-z),(z,0,s.oo))==1)
 ck('global displacement rescaling',s.simplify((2*la*It).subs(la,z/(2*t))/(2*t)-2*s.pi*t*phi/z**2)==0)
 ck('weighted displacement collar control',s.integrate(2*la*4*s.pi/(2*la),(la,0,s.sqrt(D)))==4*s.pi*s.sqrt(D))
 # Exact harmonic reconstruction; no growth lower bound inferred.
 n,g0,g1=s.symbols('nu g0 g1',real=True)
 K=(s.exp(s.I*n*t)-s.exp(-la*t))/(la*la+n*n)
 q=(g1+s.I*n*g0)*K;p=s.diff(q,t)+g0*s.exp(s.I*n*t)
 ck('full regular forced second row',s.simplify(s.diff(p,t)-la*la*q+g1*s.exp(s.I*n*t))==0)
 ck('regular representative q0',q.subs(t,0)==0)
 ck('initial boundary condition',s.simplify(p.subs(t,0)-(g1+la*g0)/(la-s.I*n))==0)
 ck('future boundary component',s.simplify(p+la*q-(g1+la*g0)*s.exp(s.I*n*t)/(la-s.I*n))==0)
 # General positive-factor threshold: opposite norm signs prevent collinearity.
 factors=[1,12,22,30,36,40,42,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12]
 for A in factors:
  if A>0:ck('negative spatial norm at positive threshold '+str(A),-s.Rational(36,A)<0)
 # A genuine rank-loss location not covered by the new bound; NOT a failure.
 Ksq=s.Integer(18);ksq=s.Rational(25,4)*Ksq;lsq=s.Rational(9,4)*Ksq
 ck('rankloss both inputs stable',ksq>36 and lsq>36)
 ck('rankloss input frequencies match',ksq-36==lsq+36==s.Rational(153,2))
 ck('rankloss output minus2 threshold',Ksq==s.Rational(36,2))
 ck('rankloss momentum addition',s.Rational(5,2)-s.Rational(3,2)==1)
 # In any positive active line, delta=18-(k+l)^2, nu=sqrt(k^2-36)-sqrt(l^2+36).
 kk,ll=s.symbols('k l',real=True);kp=s.Rational(5,2)*s.sqrt(18);lp=-s.Rational(3,2)*s.sqrt(18)
 ck('rankloss phase zero',s.sqrt(kp*kp-36)-s.sqrt(lp*lp+36)==0)
 ck('rankloss rows collinear',s.Matrix([[-2*s.sqrt(18),0],[-lp/s.sqrt(lp*lp+36),0]]).rank()==1)
 return {'schema':'gu-cw-bilinear-boundary-v1','status':'PASS','probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':deps,'check_count':len(checks),'check_names':checks,'actual_geometry':{'active_jacobian':'2(k_eta*l_sigma-k_sigma*l_eta)/omega(l)','center_determinant':'-168/13','spectator_dimensions':11},'estimate':{'kernel_squared_norm_upper':'2*pi*sqrt(D)','threshold_tail_operator_bound':'C*epsilon^(1/4)','scope':'Sufficiently small actual compact patches; all massive common-CW input channels at each of seven positive-factor output thresholds.'},'forward':{'displacement_kernel_squared_norm':'2*pi*t','weighted_kernel_squared_norm_upper':'4*pi*sqrt(D)','meaning':'Upper bound O(1+sqrt(t)), not actual growth or nonlinear stability.'},'rank_loss_candidate':{'output_factor':-2,'kappa':12,'K_squared':18,'k_over_K':'5/2','l_over_K':'-3/2','input_factors':[-1,1],'common_omega_squared':'153/2','state':'UNDETERMINED: kinematics only; actual vertex and estimate untested.'},'limits':['No source-selected state law, physical positive norm or complete nonlinear invariant domain.','No negative-factor threshold or all-output uniform completion theorem.','Exact controls supplement reviewed change-of-variables and norm proof; no new Lean claim.']}
if __name__=='__main__':
 p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true');a=p.parse_args();t0=time.monotonic();d=build()
 if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(OUT.read_text())==json.loads(json.dumps(d)),'certificate mismatch'
 print(json.dumps({'status':'PASS','checks':d['check_count'],'seconds':time.monotonic()-t0}))
