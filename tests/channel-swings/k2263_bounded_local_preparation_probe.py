#!/usr/bin/env python3
"""Exact norm, singular-cost, moment and actual band-constant controls.
Finite tests do not certify the continuum singular spectrum or tail theorem.
"""
from fractions import Fraction as F
from math import comb,factorial
import sympy as s
FAULTS=['omit_g','wrong_inverse','wrong_regularizer','omit_reflection','wrong_volume','wrong_taylor_factorial','wrong_moment_weight']
def controls(fault=None):
 out={}
 def ck(k,v):out[k]=bool(v)
 # Non-Euclidean output metric: test actual adjoint via independent pairing.
 G=s.diag(4,9);A=s.diag(s.Rational(1,2),s.Rational(1,6));u=s.Matrix([2,-3]);y=s.Matrix([1,2])
 adj=A.T*(s.eye(2) if fault=='omit_g' else G)
 ck('G_adjoint_pairing',(A*u).dot(G*y)==u.dot(adj*y))
 # A's G-singular values are1,1/2; left singular basis normalized in G.
 U=s.diag(s.Rational(1,2),s.Rational(1,3));sv=[s.Integer(1),s.Rational(1,2)]
 ck('left_G_orthonormal',U.T*G*U==s.eye(2));ck('weighted_singular_factorization',A==U*s.diag(*sv))
 coeff=s.Matrix([s.Rational(3,5),s.Rational(4,5)]);target=U*coeff
 exact=s.Matrix([coeff[i]*(sv[i] if fault=='wrong_inverse' else 1/sv[i]) for i in range(2)])
 ck('exact_preparation',A*exact==target);ck('exact_cost',exact.dot(exact)==s.Rational(73,25))
 alpha=s.Rational(1,4);den=lambda v:v+alpha if fault=='wrong_regularizer' else v*v+alpha
 reg=s.Matrix([sv[i]*coeff[i]/den(sv[i]) for i in range(2)])
 ck('normal_equation',(A.T*G*A+alpha*s.eye(2))*reg==A.T*G*target)
 err=A*reg-target
 ck('regularized_error_formula',(err.T*G*err)[0]==sum(alpha**2*coeff[i]**2/(sv[i]**2+alpha)**2 for i in range(2)))
 ck('regularized_cost_formula',reg.dot(reg)==sum(sv[i]**2*coeff[i]**2/(sv[i]**2+alpha)**2 for i in range(2)))
 # Reflection on two frequencies, metric respecting the reflection.
 Pi=s.eye(2) if fault=='omit_reflection' else s.ones(2)/2
 ck('reflected_odd_mode_removed',Pi*s.Matrix([1,-1])==s.zeros(2,1))
 ck('projection_HS_contraction',s.trace(Pi.T*Pi)<=2)
 # Tail weight |x|^4 and Plancherel multi-index coefficients.
 x,z=s.symbols('x z',real=True)
 weight=x**4+(1 if fault=='wrong_moment_weight' else 2)*x*x*z*z+z**4
 ck('moment_multinomial',s.expand(weight-(x*x+z*z)**2)==0)
 # Actual13-dimensional two-ball volume coefficient: recurrence V_d=2pi/d V_(d-2).
 vol=2
 for d in range(3,14,2):vol=s.Rational(2,d)*s.pi*vol
 claimed=(64 if fault=='wrong_volume' else 128)*s.pi**6/s.Integer(135135)
 ck('unit_ball_13_volume',s.simplify(vol-claimed)==0)
 g=F(6063,574);om=F(17,8);delta=F(287,64)
 ck('lambda_margin',F(5)-F(1,2)-F(1,64)==delta)
 ck('G_bound',(1+F(19,2)**2/delta)/2==g)
 h2=F(1344,135135)*g*om**4/F(3**7*8**13)
 ck('actual_band_HS_bound_below_1e13',h2<F(1,10**13))
 ck('half_error_cost_exceeds_million',4*h2<F(1,10**12))
 ck('free_copy_Frobenius_constant',8*128*(1+16+25)==43008)
 # Taylor coefficients checked against independently differentiated exp.
 t=s.symbols('t');N=5
 poly=sum((-s.I*t)**j/s.Integer(factorial(j if fault!='wrong_taylor_factorial' else max(j-1,0))) for j in range(N+1))
 for j in range(N+1):ck('taylor_derivative_'+str(j),s.diff(poly,t,j).subs(t,0)==(-s.I)**j)
 for N in range(5):
  count=sum(1 for i in range(N+1) for j in range(N+1) for k in range(N+1) if i+j+k<=N)
  ck('rank_monomial_control_'+str(N),count==comb(N+3,3))
 # Genuine diagonal ill-conditioning witness; cost growth and capacity bound.
 for n in [2,4,8,16]:
  ss=[F(1,2**j) for j in range(1,n+1)];eps=F(1,2);cost=(1-eps)/ss[-1]
  ck('unit_target_cost_'+str(n),cost==2**(n-1))
  ck('capacity_trace_'+str(n),n*(1-eps)**2<=cost*cost*sum(v*v for v in ss))
 return out
RESULT='K2263'
REPORT='lab/process/k2263-bounded-local-preparation.json'
DEPS=['explorations/conditional-build/k2263-bounded-local-preparation-2026-10-29.md','explorations/conditional-build/k2261-band-quotient-local-observation-2026-10-29.md','explorations/conditional-build/k2258-variable-local-preparation-2026-10-29.md']

def main():
 import argparse,hashlib,json
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 root=Path(__file__).resolve().parents[2];checks=controls()
 assert all(checks.values()),[k for k,v in checks.items() if not v]
 faults={}
 for f in FAULTS:
  failed=[k for k,v in controls(f).items() if not v]
  assert failed,('undetected changed input',f)
  faults[f]=failed
 report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds='Finite exact controls only. Universal analytic and control statements are written proofs; report hashes are provenance.',dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 p=root/REPORT
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'report drift'
 print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
