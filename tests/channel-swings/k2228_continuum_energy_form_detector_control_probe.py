#!/usr/bin/env python3
"""Exact supporting controls; continuum form/domain theorem is written proof."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

def controls(fault=None):
 c={}
 def ck(name,value): c[name]=bool(value)
 W=s.diag(1,9);nu=s.Integer(3);f=s.Matrix([1,1])/s.sqrt(2)
 h=(s.sqrt(nu)*W**s.Rational(-1,2)+W**s.Rational(1,2)/s.sqrt(nu))*f/2
 j=(s.sqrt(nu)*W**s.Rational(-1,2)-W**s.Rational(1,2)/s.sqrt(nu))*f/2
 if fault=='drop_creation': j=s.zeros(2,1)
 norm=lambda v:s.simplify((v.T*v)[0])
 hh=norm(h);jj=norm(j)
 ck('canonical_CCR',s.simplify(hh-jj)==1)
 ck('same_optimized_mode_h',h==s.Matrix([2,2])/s.sqrt(6))
 ck('same_optimized_mode_j',j==s.Matrix([1,-1])/s.sqrt(6))
 ck('same_thermal_N',jj==s.Rational(1,3))
 u=s.sqrt((h.T*W**-1*h)[0])+s.sqrt((j.T*W**-1*j)[0])
 vacuum=0 if fault=='omit_creation_vacuum' else jj
 B2=s.simplify(u*u+vacuum)
 eta=s.sqrt((h.T*W*h)[0])+s.sqrt((j.T*W*j)[0])
 ck('energy_B_squared',B2==2)
 ck('energy_eta_squared',s.simplify(eta*eta)==15)
 ck('energy_A_squared',s.simplify(eta*eta*(B2+1))==45)
 # Bogoliubov complement d_i=a_i-h_i b+j_i b*; [d_i,b]=[d_i,b*]=0.
 sign=-1 if fault=='complement_sign' else 1
 for i in range(2):
  ck('complement_commutes_b_'+str(i),s.simplify(j[i]-sign*j[i]*(hh-jj))==0)
  ck('complement_commutes_bdag_'+str(i),s.simplify(h[i]-h[i]*(hh-jj))==0)
 # Whole arbitrary spectator frequencies cancel from the energy constants.
 z=s.symbols('z',positive=True)
 WS=s.diag(1,9,z);hs=h.col_join(s.zeros(1,1));js=j.col_join(s.zeros(1,1))
 ck('UV_spectator_h_energy',(hs.T*WS*hs)[0]==(h.T*W*h)[0])
 ck('UV_spectator_j_energy',(js.T*WS*js)[0]==(j.T*W*j)[0])
 ck('UV_spectator_h_inverse',(hs.T*WS**-1*hs)[0]==(h.T*W**-1*h)[0])
 ck('UV_spectator_j_inverse',(js.T*WS**-1*js)[0]==(j.T*W**-1*j)[0])
 # Exact occupation shifts on interior sectors; no truncated CCR claim.
 Y=s.Matrix([[0,-s.I],[s.I,0]]);I=s.eye(2)
 angles=[0,s.pi/6,s.pi/2,s.pi/3]
 Us=[s.cos(t)*I-s.I*s.sin(t)*Y for t in angles]
 for n in range(1,4):
  old=Us[n] if fault=='ignore_number_shift' else Us[n-1]
  comm=s.sqrt(n)*(Us[n]-old)
  gram=(comm.conjugate().T*comm).applyfunc(s.simplify)
  expected=2*n*(1-s.cos(angles[n]-angles[n-1]))*I
  ck('adjacent_number_shift_gram_'+str(n),(gram-expected).applyfunc(s.simplify)==s.zeros(2))
 # Positive oscillator matrix generates claimed b flow.
 x=s.symbols('x',positive=True)
 a=(x+1/x)/2;v=(x-1/x)/2
 M=s.Matrix([[-s.I*a,-s.I*v],[s.I*v,s.I*a]])
 ck('quadratic_generator_squared',s.simplify(M*M)==-I)
 ck('Bogoliubov_CCR_flow_generator',(M*s.diag(1,-1)+s.diag(1,-1)*M.conjugate().T).applyfunc(s.simplify)==s.zeros(2))
 quarter=s.Matrix([[0,1/x],[-x,0]]);rot=s.Matrix([[0,1],[-1,0]])
 pulse=quarter*rot**3 if fault=='squeeze_order' else rot**3*quarter
 ck('same_squeeze_order',pulse==s.diag(x,1/x))
 for value in [s.Rational(2,3),s.Rational(7,5),s.Integer(1)]:
  av=a.subs(x,value);vv=v.subs(x,value);r=max(value,1/value)
  ck('generator_row_norm_'+str(value),av+abs(vv)==r)
  ck('positive_quadratic_'+str(value),value>0 and 1/value>0)
 # Form-bound constants and switching exchange algebra.
 Lam,L,E,T0=s.symbols('Lambda L E T0',positive=True)
 ck('speed_error_vanishes',s.limit(2*L*(E+1)*T0/Lam,Lam,s.oo)==0)
 A0,A1,A2=s.symbols('a0 a1 a2',positive=True)
 ck('absolute_switch_twice_each',A0+(A0+A1)+(A1+A2)+A2==2*(A0+A1+A2))
 e0,e1,e2,e3=s.symbols('e0 e1 e2 e3')
 ck('net_work_telescopes',s.simplify((e1-e0)+(e2-e1)+(e3-e2))==e3-e0)
 return c

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--scratch',action='store_true');args=ap.parse_args()
 checks=controls();assert all(checks.values()),[k for k,v in checks.items() if not v]
 faults={}
 for name in ['drop_creation','omit_creation_vacuum','complement_sign','ignore_number_shift','squeeze_order']:
  faults[name]=[k for k,v in controls(name).items() if not v];assert faults[name],name
 if args.scratch:
  print(json.dumps(dict(passed=len(checks),faults_rejected=len(faults),faults=faults)));return
 deps=['explorations/conditional-build/k2228-continuum-energy-form-detector-control-2026-10-28.md','explorations/conditional-build/k2223-stable-detector-resource-realization-2026-10-28.md','explorations/conditional-build/k2225-positive-drift-detector-control-2026-10-28.md','explorations/conditional-build/k2160-outcome-conditioned-squeezing-2026-10-27.md']
 out=dict(result='K2228',scope='same fixed canonical-mode continuum energy-form drift control; finite algebra supports written proof',checks=checks,faults=faults,probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps})
 target=ROOT/'lab/process/k2228-continuum-energy-form-detector-control.json'
 if args.write:target.write_text(json.dumps(out,indent=2)+'\n')
 else:assert json.loads(target.read_text())==out,'stale certificate'
 print(json.dumps(dict(passed=len(checks),faults_rejected=len(faults))))
if __name__=='__main__':main()
