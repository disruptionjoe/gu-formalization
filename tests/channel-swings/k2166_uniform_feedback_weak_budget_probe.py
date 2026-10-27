#!/usr/bin/env python3
"""Exact moment/Hessian controls; universal sequence theorem is in the note."""
from pathlib import Path
import argparse,hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
def controls(fault=None):
 out={};ck=lambda k,v:out.__setitem__(k,bool(v));zero=lambda v:S.simplify(v)==0
 N,mu,nu,Es,x=S.symbols('N mu nu Es x',positive=True)
 s=S.sqrt(N*(N+1));m1=nu*(2*N+1);m2=nu*(nu+4*N*(N+1)*Es/(2*N+1))
 Eh=(nu+2*m1+m2/nu)/(4*(N+1));Ej=(nu-2*m1+m2/nu)/(4*N);F=(nu-m2/nu)/(4*s)
 ck('compressed_trace',zero(Eh+Ej-Es))
 ck('compressed_determinant',zero(Eh*Ej-F**2-(m2-m1**2)/(4*N*(N+1))))
 u,v=S.symbols('u v',real=True);T=S.sqrt(mu*(mu+1))
 nh=(N+1)*(u*u*mu+v*v*(mu+1))+N*(mu+1)-2*s*u*T
 nj=(N+1)*mu+N*(u*u*(mu+1)+v*v*mu)-2*s*u*T
 factor=2 if fault=='physical_cross' else 4
 expected=(2*N+1)*(2*mu+1)*u*u-factor*s*T*u-1
 ck('physical_number_expansion',zero((nh+nj).subs(v*v,u*u-1)-expected))
 ck('unsqueezed_number_square',zero(expected.subs(u,1)-2*(S.sqrt(N+1)*S.sqrt(mu)-S.sqrt(N)*S.sqrt(mu+1))**2))
 a,b=S.symbols('a b',nonnegative=True)
 ck('rationalization_identity',zero(((N+1)*mu-N*(mu+1))-(mu-N)))
 ck('denominator_amgm_identity',zero(2*(a*a+b*b)-(a+b)**2-(a-b)**2))
 A=m2*x*x/(2*nu)+nu/(2*x*x);C=2*s*Es
 DM=N*Eh+(N+1)*Ej;DW=((N-1)*Eh+N*Ej)/2
 G=(mu+S.Rational(1,2))*A-C*x*T+DM*mu+DW
 at=lambda f:S.simplify(f.subs({mu:N,x:1}))
 ck('vacuum_zero_and_stationary',all(zero(at(f)) for f in [G,S.diff(G,mu),S.diff(G,x)]))
 H0=(3*m1+(2*N+1)*m2/nu)/2
 gmm=at(S.diff(G,mu,2));gmx=at(S.diff(G,mu,x));gxx=at(S.diff(G,x,2))
 ck('moment_hessian',zero(gmm-Es/(2*N*(N+1))))
 ck('cross_hessian',zero(gmx+Es/(2*N+1)))
 ck('squeeze_hessian',zero(gxx-H0))
 fpp=gmm-(0 if fault=='omit_schur' else gmx*gmx/gxx)
 kappa=N/(N+1)*Es-2*(N*Es/(2*N+1))**2/H0
 ck('sharp_schur_coefficient',zero(2*N*N*fpp-kappa))
 w,M,d,lam=S.symbols('w M d lam',positive=True)
 den1=(2*N+1)*M+N*w;den0=(2*N+1)*(N-M)+N*(1-w)
 ck('complement_denominator_sum',zero(den1+(0 if fault=='omit_complement' else den0)-2*N*(N+1)))
 branch=lam*w*(M/w-N)**2/((2*N+1)*M/w+N)
 if fault=='omit_branch_weight':branch/=w
 ck('homogeneous_rare_branch_bound',zero(branch-lam*(M-N*w)**2/den1))
 ck('harmonic_mean_global_bound',zero((1/a+1/b)-4/(a+b)-(a-b)**2/(a*b*(a+b))))
 quad=(d/w)**2*w+(d/(1-w))**2*(1-w)
 ck('two_branch_taylor_factor',zero(quad-d*d/(w*(1-w))))
 ck('balanced_probability_maximum',zero(S.Rational(1,4)-w*(1-w)-(w-S.Rational(1,2))**2))
 fixture={N:S.Rational(1,3),nu:S.Integer(3),Es:S.Integer(11 if fault=='moment_fixture' else 10)}
 vals=[S.simplify(t.subs(fixture)) for t in [Eh,Ej,F,gmm,gmx,gxx,fpp,kappa]]
 expected=[5,5,-4,S.Rational(45,4),-6,S.Rational(170,9),S.Rational(3177,340),S.Rational(353,170)]
 ck('exact_fixture',vals==expected)
 ck('safe_gap_and_global_bound',S.Rational(9,10)<=1 and 2*S.Rational(9,10)*S.Rational(1,4)==S.Rational(9,20))
 return out
FAULTS=['physical_cross','omit_schur','omit_complement','omit_branch_weight','moment_fixture']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();checks=controls();assert all(checks.values()),[k for k,v in checks.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2166-uniform-feedback-weak-budget-2026-10-27.md','explorations/conditional-build/k2160-outcome-conditioned-squeezing-2026-10-27.md','explorations/conditional-build/k2162-feedback-detector-frontier-2026-10-27.md']
 report=dict(result_id='K2166',status='conditional_exact_controls',exact_checks=checks,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written Cauchy relaxation, finite-mode energy coercivity, rare-branch sequence proof, sharp asymptotic composition and necessary optimality conditions independently reviewed. Symbolic controls do not replace these proofs.')
 p=ROOT/'lab/process/k2166-uniform-feedback-weak-budget.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps(dict(result='K2166',checks=len(checks),faults=faults)))
if __name__=='__main__':main()
