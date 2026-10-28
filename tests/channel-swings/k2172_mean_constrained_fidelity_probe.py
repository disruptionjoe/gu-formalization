#!/usr/bin/env python3
"""Mean-constrained fidelity identities and exact all-probability energy certificate."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import sympy as S
from k2168_finite_budget_moment_envelope_probe import IV,ll,sqrtq,aa
ROOT=Path(__file__).resolve().parents[2];N=F(1,3);Z=F(1,4);C=F(40,3);D=F(1,2)
def rho(w):return (2*w+1)/(8*w+1)
def floorq(x):return F((x*10**18).__floor__(),10**18)
def ceilq(x):return -floorq(-x)
def sqrtiv(x):return IV(sqrtq(x.a).a,sqrtq(x.b).b)
def overlap_bin(a,b):
 R=IV(rho(b),rho(a));x0=IV((8*a-1)/12,(8*b-1)/12);x1=IV((16*a+1)/48,(16*b+1)/48)
 u=sqrtiv(R*Z)
 return sqrtiv((1-R)*x0)+sqrtiv((1-R)*R*x1)+sqrtiv((1-R)*(1-Z))*(R*Z)/(1-u)
def witness(w=F(311154,10**6),eps=F(2666,10**6),s1=F(1055411,10**6),s0=F(860107,10**6)):
 x0=(8*w-1)/12-eps;x1=(16*w+1)/48+2*eps;x2=F(3,64)-eps;m=(w+D)/3
 assert 0<=x0<=F(3,4) and 0<=x1<=F(3,16) and 0<=x2<=F(3,64)
 t1=sqrtq(x0*x1)+2*sqrtq(x1*x2)+3*sqrtq(x2*F(3,256))+F(13,384)
 t0=sqrtq((F(3,4)-x0)*(F(3,16)-x1))+2*sqrtq((F(3,16)-x1)*(F(3,64)-x2))
 e=(m+w/2)*aa(s1)-C*s1*t1+F(25,3)*m-F(5,6)*w+(N-m+(1-w)/2)*aa(s0)-C*s0*t0+F(25,3)*(N-m)-F(5,6)*(1-w)
 return dict(w=str(w),epsilon=str(eps),click_squeeze=str(s1),no_click_squeeze=str(s0),energy=[str(floorq(e.a)),str(ceilq(e.b))])
def controls(fault=None):
 cs={};ck=lambda n,v:cs.__setitem__(n,bool(v));w=S.symbols('w',real=True)
 R=(2*w+1)/(8*w+1);x0=(8*w-1)/12;x1=(16*w+1)/48
 if fault=='wrong_mean':x1=(16*w+2)/48
 ck('profile_mass',S.simplify(x0+x1+S.Rational(1,16)-w)==0)
 ck('profile_mean',S.simplify(x1+S.Rational(7,48)-(w+S.Rational(1,2))/3)==0)
 ck('negative_multiplier_slope',S.simplify(x1-R*x0-(64*w*w+5)/(48*(8*w+1)))==0)
 ck('tail_cap_large_w',S.simplify(R*x1-S.Rational(3,64)-(128*w*w-5)/(192*(8*w+1)))==0)
 ck('small_w_radical_margin',2*sqrtq(10).b-sqrtq(20).a<2 and F(56,13)>2*sqrtq(3).b)
 ck('split_valid',F(128,25)>5)
 # Exact geometric tails and nearest-neighbor sums.
 z=S.symbols('z',positive=True)
 tailm=z*z*(2+z/(1-z));tt=S.sqrt(z)*z*z*(3+z/(1-z))
 if fault=='tail_index':tt*=z
 ck('geometric_tail_moments',tailm.subs(z,S.Rational(1,4))==S.Rational(7,48))
 ck('exact_T_tail',tt.subs(z,S.Rational(1,4))==S.Rational(5,48))
 # Pointwise dual maximization in variable a=sqrt(x) for t>0 (interior).
 g,t,p=S.symbols('g t p',positive=True);astar=g/(2*t)
 if fault=='dual_factor':astar=g/t
 ck('dual_stationary_point',S.simplify(g-2*t*astar)==0)
 ck('dual_value',S.simplify(g*astar-t*astar*astar-g*g/(4*t))==0)
 # Both endpoint profiles are exactly feasible and the lower endpoint has a zero.
 ck('endpoint_profiles',x0.subs(w,S.Rational(1,8))==0 and x1.subs(w,S.Rational(1,2))==S.Rational(3,16))
 # Affine upper certificate tail for negative nu: weighted geometric sum identity.
 K,lam,nu=S.symbols('K lam nu',real=True)
 exact=-lam*z**K-nu*z**K*(K+z/(1-z))
 bound=z**K*(-lam-nu*K-nu*z/(1-z))
 if fault=='omit_tail_mean':bound=z**K*(-lam-nu*K)
 ck('dual_negative_slope_tail',S.simplify(exact-bound)==0)
 # Feasible perturbation preserves both constraints and creates a new complement edge.
 eps=S.symbols('eps',positive=True);pert=[-eps,2*eps,-eps]
 if fault=='perturb_mean':pert=[-eps,eps,-eps]
 ck('perturbation_preserves_mass',S.simplify(sum(pert))==0)
 ck('perturbation_preserves_mean',S.simplify(sum(i*v for i,v in enumerate(pert)))==0)
 y=S.symbols('y',positive=True)
 ck('new_edge_square_root_leading',S.limit(2*S.sqrt((y-2*eps)*eps)/S.sqrt(eps),eps,0,dir='+')==2*S.sqrt(y))
 ck('perturbed_T_tail',(S.sqrt(z)*z**3*(4+z/(1-z))).subs(z,S.Rational(1,4))==S.Rational(13,384))
 # General terminal-tail perturbation, at any two earlier interior indices.
 ii,jj,kk=S.symbols('i j k',real=True)
 di=-(kk-jj)*eps/(jj-ii);dj=(kk-ii)*eps/(jj-ii);dk=-eps
 ck('general_tail_preserves_mass',S.simplify(di+dj+dk)==0)
 ck('general_tail_preserves_mean',S.simplify(ii*di+jj*dj+kk*dk)==0)
 # Energy residual coefficient must match exact T convention.
 eta,x,ww,mm,al,be=S.symbols('eta x ww mm al be',positive=True)
 actual=(mm+ww/2)*(al*x*x+be/x**2)-S.Rational(40,3)*x*(S.sqrt(mm*(mm+ww))-eta)
 relaxed=(mm+ww/2)*(al*x*x+be/x**2)-S.Rational(40,3)*x*S.sqrt(mm*(mm+ww))
 if fault=='energy_sign':actual-=2*S.Rational(40,3)*x*eta
 ck('energy_defect_coefficient',S.expand(actual-relaxed-S.Rational(40,3)*x*eta)==0)
 # Shift coefficient bound is decreasing for r in (0,1).
 r=S.symbols('r',positive=True);ck('shift_prefactor_monotone',S.simplify(S.diff((1-r)**2/(2*r),r)-(r*r-1)/(2*r*r))==0)
 return cs
FAULTS=['wrong_mean','tail_index','dual_factor','omit_tail_mean','energy_sign','perturb_mean']
def certificate(count=256):
 left=F(1,8);right=F(1,2);rows=[]
 for j in range(count):
  a=left+(right-left)*F(j,count);b=left+(right-left)*F(j+1,count);mid=(a+b)/2
  h=overlap_bin(a,b);hupper=ceilq(h.b)
  deficit=max(F(0),a-hupper*hupper)
  rhi=sqrtq(rho(a)).b;pref=(1-rhi)**2/(2*rhi)
  value,slope=ll(D,mid);moment=(value+slope*IV(a-mid,b-mid)).a
  bound=floorq(moment+C*F(2,3)*pref*deficit)
  rows.append(dict(a=str(a),b=str(b),H_upper=str(hupper),norm_deficit_lower=str(floorq(deficit)),moment_lower=str(floorq(moment)),energy_lower=str(bound)))
 assert F(rows[0]['a'])==left and F(rows[-1]['b'])==right
 assert all(x['b']==y['a'] for x,y in zip(rows,rows[1:]))
 lower=min(F(x['energy_lower']) for x in rows)
 return dict(delta='1/2',scope='exact contrast; every probability and infinite occupation covered',bins=rows,energy_lower=str(lower))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();cs=controls();assert all(cs.values()),cs
 faults={}
 for f in FAULTS:
  bad=[k for k,p in controls(f).items() if not p];assert bad,('undetected',f);faults[f]=bad
 cert=certificate();wit=witness();baseline=witness(eps=F(0));assert F(baseline['energy'][0])>F('1.0034');assert F(baseline['energy'][0])>F(wit['energy'][1]);assert F(cert['energy_lower'])>F('0.5498');assert F(wit['energy'][1])<F('0.84168')
 deps=['explorations/conditional-build/k2172-mean-constrained-fidelity-2026-10-27.md','tests/channel-swings/k2168_finite_budget_moment_envelope_probe.py','explorations/conditional-build/k2170-bounded-effect-energy-gap-2026-10-27.md','explorations/conditional-build/k2162-feedback-detector-frontier-2026-10-27.md']
 report=dict(result_id='K2172',status='conditional_exact_controls',checks=cs,fault_failures=faults,probability_certificate=cert,feasible_energy_witness=wit,unperturbed_same_squeezes=baseline,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Independent written mean dual, strict cap gap and exact constrained-fidelity profile proofs; rational intervals certify energy lower and feasible upper bounds, not actual energy optimum.')
 dest=ROOT/'lab/process/k2172-mean-constrained-fidelity.json'
 if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==report
 print(json.dumps(dict(result='K2172',checks=len(cs),faults=faults,lower=float(F(cert['energy_lower'])),upper=wit['energy'][1])))
if __name__=='__main__':main()
