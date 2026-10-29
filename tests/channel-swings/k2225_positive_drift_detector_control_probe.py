#!/usr/bin/env python3
"""Finite exact controls for the written positive-control/domain theorem."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

def controls(fault=None):
 c={}
 def ck(k,v):c[k]=bool(v)
 I=s.eye(2);J=s.Matrix([[0,s.I],[-s.I,0]])
 beam=(0 if fault=='beam_shift' else 1)*I+J
 ck('beam_positive',all(x>=0 for x in beam.eigenvals()))
 ck('beam_spectrum',set(beam.eigenvals())=={0,2})
 theta=s.pi/3
 # One-particle equality lifts by second quantization to all occupations.
 U=s.exp(-s.I*theta*beam)
 phase=theta if fault=='phase_sign' else 2*s.pi-theta
 V=s.exp(-s.I*phase)*U
 target=s.cos(theta)*I-s.I*s.sin(theta)*J
 ck('exact_phase_compensated_beam',(V-target).applyfunc(s.expand_complex).applyfunc(s.simplify)==s.zeros(2))
 ck('beam_upper_2N',all(x>=0 for x in (2*I-beam).eigenvals()))
 Y=s.Matrix([[0,-s.I],[s.I,0]])
 for e,angle in [(0,0),(s.Rational(1,4),s.pi/6),(1,s.pi/2)]:
  H=angle*Y+(0 if fault=='measurement_shift' else s.pi/2)*I
  ck('measurement_positive_'+str(e),all(x>=0 for x in H.eigenvals()))
  rot=s.cos(angle)*I-s.I*s.sin(angle)*Y
  ck('positive_root_'+str(e),rot[:,0]==s.Matrix([s.sqrt(1-e),s.sqrt(e)]))
 q=s.symbols('q',positive=True);R=s.Matrix([[0,1/q],[-q,0]]);R1=s.Matrix([[0,1],[-1,0]])
 squeeze=R*R1**3 if fault=='squeeze_order' else R1**3*R
 ck('squeeze_order',squeeze==s.diag(q,1/q))
 ck('symplectic',s.simplify(squeeze*R1*squeeze.T)==R1)
 for q in [s.Rational(2,3),s.Rational(7,5),s.Integer(1)]:
  B=s.diag(q,1/q);flow=R1*B
  rate=abs(q-1/q);der=flow+flow.T
  ck('number_rate_'+str(q),all(x>=0 for x in (rate*I-der).eigenvals()) and all(x>=0 for x in (rate*I+der).eigenvals()))
  ck('positive_oscillator_'+str(q),all(x>0 for x in B.eigenvals()))
 # Actual finite compression identity even though squeezing changes number.
 G=s.diag(s.Rational(1,2),s.Rational(3,2),s.Rational(5,2),s.Rational(7,2))
 K=s.Matrix([[2,0,1,0],[0,3,0,2],[1,0,4,0],[0,2,0,5]])
 P=s.diag(1,1,1,0)
 comm=lambda a,b:a*b-b*a
 ck('squeeze_need_not_commute_cutoff',comm(P,K)!=s.zeros(4))
 rhs=s.zeros(4) if fault=='cutoff_commutes' else P*comm(G,K)*P
 ck('compressed_number_commutator',comm(G,P*K*P)==rhs)
 z,t,k,D,L,g0=s.symbols('z t k D L g0',positive=True)
 integral=2*(s.exp(k*t/2)-1)/k
 ck('overlap_integral',s.simplify(s.diff(integral,t)-s.exp(k*t/2))==0)
 ck('zero_k_limit',s.limit(integral,k,0)==t)
 ck('speed_limit',s.limit(integral.subs(t,1/z),z,s.oo)==0)
 energies=s.symbols('E0 E1 E2 E3 E4');work=[energies[i+1]-energies[i] for i in range(4)]
 ck('signed_work_telescopes',s.simplify(sum(work)-energies[-1]+energies[0])==0)
 # Positive plateaus dominate their absolute values; bound two endpoint occurrences.
 a=s.symbols('a0:4',positive=True)
 ck('absolute_switch_coefficient',sum(a[i]+a[i+1] for i in range(3))+a[0]+a[-1]==2*sum(a))
 x=s.symbols('x',real=True)
 ck('pi_rational_upper_identity',s.integrate(x**4*(1-x)**4/(1+x*x),(x,0,1))==s.Rational(22,7)-s.pi)
 rate=s.Rational(55,42)
 ck('L_less_than_four',1+rate+rate**2/(2*(1-rate/3))<4)
 speed=s.Integer(10)**12; Tmax=20/speed
 ck('joint_consumer_duration',6*s.Rational(22,7)+1<20)
 ck('joint_consumer_exp_bounds',1/(1-Tmax)<2 and 1/(1-2*Tmax)<2)
 ck('joint_consumer_delta',72*Tmax<s.Rational(1,25000)**2)
 ck('joint_consumer_A',6+s.Rational(22,7)+s.Rational(3,2)+1<12)
 from fractions import Fraction as F
 from math import comb
 reset=sum((F(comb(101,j)*3**(101-j),4**101) for j in range(51,102)),F(0))
 ck('joint_consumer_reset',reset<F(32581,10**12))
 ck('joint_consumer_total',F(1,25000)+reset<F(40032581,10**12))
 ck('joint_consumer_work',2*speed*12*2*4*s.Rational(3,2)==288*speed)
 return c

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 c=controls();assert all(c.values()),[k for k,v in c.items() if not v]
 faults={}
 for f in ['beam_shift','phase_sign','measurement_shift','squeeze_order','cutoff_commutes']:
  failed=[k for k,v in controls(f).items() if not v];assert failed,f;faults[f]=failed
 deps=['explorations/conditional-build/k2225-positive-drift-detector-control-2026-10-28.md','explorations/conditional-build/k2154-uncompensated-detector-control-2026-10-27.md','explorations/conditional-build/k2223-stable-detector-resource-realization-2026-10-28.md']
 out=dict(result='K2225',scope='finite-chain positive additive controls; written universal proof plus finite exact controls',checks=c,faults=faults,probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps})
 if args.write:(ROOT/'lab/process/k2225-positive-drift-detector-control.json').write_text(json.dumps(out,indent=2)+'\n')
 else:assert json.loads((ROOT/'lab/process/k2225-positive-drift-detector-control.json').read_text())==out, 'stale certificate; regenerate after final changes'
 print(json.dumps(dict(passed=len(c),faults_rejected=len(faults))))
if __name__=='__main__':main()
