"""Finite identities/countercontrols only; analytic local-net proof is in K2130."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2130-stable-empty-vacuum-locality.json'

def checks(fault=None):
 ck={};put=lambda k,x:ck.__setitem__(k,bool(x))
 I=s.eye(2);W=s.diag(1,s.I)
 kp=(I+W)/2;km=(I-W)/(3 if fault=='kraus-normalization' else 2)
 E=km.H*km
 put('Kraus-normalization',s.simplify(kp.H*kp+km.H*km-I)==s.zeros(2))
 put('effect-real-Weyl',s.simplify(E-(I-(W+W.H)/2)/2)==s.zeros(2))
 rho=s.Matrix([[s.Rational(1,2),s.I/3],[-s.I/3,s.Rational(1,2)]])
 unread=kp*rho*kp.H+km*rho*km.H
 put('unread-random-unitary',s.simplify(unread-(rho+W*rho*W.H)/2)==s.zeros(2))
 # Positive-energy hopping gives immediate tails, not an exact metric cone.
 H=s.Matrix([[2,1],[1,2]])
 if fault=='spectral-stability':H-=2*s.eye(2)
 put('stable-hopping-control',min(H.eigenvals())>=0)
 t=s.symbols('t',real=True)
 U=s.exp(-2*s.I*t)*s.Matrix([[s.cos(t),-s.I*s.sin(t)],[-s.I*s.sin(t),s.cos(t)]])
 put('hopping-equation',s.simplify(s.I*s.diff(U,t)-H*U)==s.zeros(2))
 put('immediate-hopping-detection',s.simplify(abs(U[1,0])**2-s.sin(t)**2)==0)
 # Actual positive baseline characteristic functional and translated Weyl phase.
 r,phi=s.symbols('r phi',real=True)
 pf=(1-r*s.cos(phi))/2;p0=(1-r)/2
 if fault=='vacuum-subtraction':p0=s.Integer(0)
 put('baseline-subtracted-response',s.simplify(pf-p0-r*(1-s.cos(phi))/2)==0)
 put('zero-before-contact',s.simplify((pf-p0).subs(phi,0))==0)
 # Exact support and alternating-series first-term bounds from the written kernel.
 a=s.Rational(1,32);L=s.Rational(1,4);arr=s.Rational(1,2)
 if fault=='arrival-time':arr=s.Rational(1,8)
 put('all-pairs-inside-cone',arr>L+2*a)
 put('early-separated-interval',L-2*a==s.Rational(3,16))
 put('Bessel-small-argument',arr**2-(L-2*a)**2<=s.Rational(1,4))
 bessel_lower=1-s.Rational(1,2)**2/4
 put('strict-signal-interval',bessel_lower/2==s.Rational(15,32) and s.Rational(1,2)<2*s.pi)
 # No finite detector theorem is inferred from this two-qubit commutant example.
 omega=s.Matrix([1,0,0,2])/s.sqrt(5);E=s.kronecker_product(s.diag(1,0),I)
 bp=[s.kronecker_product(I,s.diag(s.sqrt(5),0)),s.kronecker_product(I,s.Matrix([[0,0],[s.sqrt(5),0]]))]
 V=s.Matrix.hstack(*(b*omega for b in bp));C2=s.Integer(10)
 if fault=='code-norm-budget':C2=s.Integer(1)
 put('code-isometry',V.H*V==s.eye(2))
 pzero=(omega.H*E*omega)[0];compressed=V.H*E*V
 put('fixed-code-commutant-bound',max(compressed.eigenvals())<=C2*pzero)
 put('commutant-locality',all(b*E==E*b for b in bp))
 return ck

FAULTS=['kraus-normalization','spectral-stability','vacuum-subtraction','arrival-time','code-norm-budget']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 good=checks();assert all(good.values()),good
 bad={f:[k for k,v in checks(f).items() if not v] for f in FAULTS};assert all(bad.values()),bad
 for f,errors in bad.items():print('[FAIL detected]',f,errors)
 inputs=['explorations/conditional-build/k2108-local-detector-tradeoffs-2026-10-26.md','explorations/conditional-build/k2125-local-two-field-collision-2026-10-27.md']
 result=dict(result_id='K2130',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=good,fault_failures=bad,evidence_kind='Finite matrix and algebraic witness controls, not spectral analyticity or continuum locality certification.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
 if args.write:OUT.write_text(json.dumps(result,indent=2)+'\n')
 else:assert result==json.loads(OUT.read_text())
 print('PASS K2130',len(good),'finite identity/witness checks;',len(bad),'genuine input faults')
if __name__=='__main__':main()
