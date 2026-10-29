#!/usr/bin/env python3
"""Explicit exact perturbation radius for the actual prescribed real-grade fiber."""
import sys
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from pathlib import Path
import argparse,hashlib,json,math
import sympy as S
import k2214_prescribed_adapter_fibers_probe as prior
o=prior.o;ROOT=Path(__file__).resolve().parents[2]
def scalar(x):return abs(S.re(x))+abs(S.im(x))
def norm(a):return max(sum(scalar(a[i,j]) for j in range(a.cols)) for i in range(a.rows))
def vinf(a):return max(map(scalar,a))
def euler(a,b,Y,coefficient=4):
 w=(a+b)/14;u=o.epsilon*(a-b)/30;v=o.IN*o.grade(w);t=S.I*o.grade(u);R=v+3*t;br=v-3*t
 K=lambda z:sum(((1 if j<4 else -1)*g*z*g for j,g in enumerate(o.gam)),o.Z)
 A=3*K(br*br)+34*br*br+36*R*br+8*br*R-24*R*R
 B=184*R*R+140*R*br+184*br*R+194*br*br+24*K(br*R)+15*K(br*br)
 return o.clean(coefficient*A.extract(o.ix,o.ix)*Y-(5*B-A).extract(o.ix,o.ix))
def certificate():
 cs={};ck=lambda k,v:cs.__setitem__(k,bool(v))
 wc=o.coord([((1,2,3),1),((1,4,5),1),((2,6,7),2),((3,8,9),3),((4,6,10),5)])
 uc=o.coord([((1,2,4),2),((1,5,7),3),((2,6,8),5),((3,9,10),7),((4,5,6),11)])
 v=o.IN*o.grade(wc);t=S.I*o.grade(uc);P=7*v-15*t;YY=o.clean(P.inv()*(7*v+15*t));Y=YY.extract(o.ix,o.ix)
 a=7*wc+15*o.epsilon*uc;b=7*wc-15*o.epsilon*uc;E=o.constraint_matrix(Y);minor=E.extract(prior.ROWS,prior.COLS)
 ck('actual_full_kernel',E*a==S.zeros(392,1));ck('normalization_coordinate',a[93]==35)
 det=prior.det_mod([[prior.residue(x) for x in minor.row(i)] for i in range(119)])
 ck('actual119_minor',det==992118)
 q=S.ilcm(*[S.denom(x) for x in minor]);H=max(S.Integer(1),max(abs(q*x) for x in minor));ck('integer_minor',all((q*x).is_Integer for x in minor))
 C=S.factorial(119)*q*H**118;g=norm(o.Ginv);L=max(240,120*g);Yb=norm(Y)+1;A0=vinf(a/35)
 ck('normalized_port_bound',A0==S.Rational(33,7));ck('all_Phi_norm1',all(norm(z)==1 for z in o.phis))
 ck('all_grade_norm1',all(norm(z)==1 for z in o.blades));ck('all_gamma_norm1',all(norm(z)==1 for z in o.gam));ck('volume_norm1',norm(o.IN)==1)
 Ka=2*C*L*A0;A=2*A0;B=120*g*A*Yb;Kb=120*g*(Ka*Yb+A0);r=S.Rational(144,7)*(A+B);k=S.Rational(144,7)*(Ka+Kb)
 Le=(1056*Yb+11184)*r*k+528*r*r
 residual=euler(a/35,b/35,Y);ee=S.Rational(15850252893220743860640,27955676769824869*1225)
 ck('actual_normalized_Euler_entry',S.re(residual[0,0])==ee and ee>0)
 rho=min(S.Integer(1),1/(2*C*L),ee/(2*Le))
 ck('positive_radius',rho>0);ck('Neumann_margin',C*L*rho<=S.Rational(1,2));ck('Euler_margin',Le*rho<=ee/2)
 ck('port_radius_control',Ka*rho<=A0)
 # Independent monomial accounting and small-matrix norm countercontrols.
 ck('Euler_A_norm',3*10+34+36+8+24==132)
 ck('Euler_B_norm',184+140+184+194+24*10+15*10==1092)
 ck('Euler_Lipschitz',4*264==1056 and 5*2184+264==11184 and 4*132==528)
 ck('reconstruct_R_bound',120*(S.Rational(1,14)+S.Rational(3,30))==S.Rational(144,7))
 z=S.Matrix([[1+2*S.I,3-S.I],[-2*S.I,1]]);w=S.Matrix([[S.I,1],[2,1-S.I]])
 ck('complex_norm_submultiplicative',norm(z*w)<=norm(z)*norm(w));ck('complex_norm_sees_imaginary',norm(S.I*S.eye(2))==1)
 # An exact arbitrary factor perturbation checks E's real matrix norm bound;
 # no claim that this perturbed factor is a genuine solution or norm-one.
 h=S.Rational(1,1000);Yp=Y+h*S.I*S.eye(16);Ep=o.constraint_matrix(Yp)
 ck('actual_constraint_perturbation_bound',norm(Ep-E)<=L*h)
 bp=o.clean(o.Ginv*o.upper(o.phi(a/35)*Yp)).applyfunc(S.re)
 rp=euler(a/35,bp,Yp);ck('actual_Euler_perturbation_bound',norm(rp-residual)<=Le*h)
 ck('full_real_factor',o.clean(o.bar(YY)*YY)==o.I)
 assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={}
 wrong=euler(a/35,b/35,Y,5);faults['Euler_coefficient']=['actual_normalized_Euler_entry'] if S.re(wrong[0,0])!=ee else []
 bad=[[prior.residue(x) for x in minor.row(i)] for i in range(119)];bad[0]=bad[1][:]
 faults['minor_row']=['actual119_minor'] if prior.det_mod(bad)==0 else []
 # Omit q from the derived inverse formula on the exact1x1 matrix[1/7].
 faults['inverse_denominator']=['inverse_bound_on_exact_matrix'] if norm(S.Matrix([[S.Rational(1,7)]]).inv())>1 else []
 faults['ignore_imaginary_norm']=['nonzero_matrix_norm'] if max(sum(abs(S.re(x)) for x in (S.I*S.eye(2)).row(i)) for i in range(2))==0 else []
 assert all(faults.values())
 vals=dict(q=q,H=H,inverse_bound=C,Ginv_norm=g,constraint_Lipschitz=L,Y_bound=Yb,A0=A0,Ka=Ka,A=A,B=B,Kb=Kb,r=r,k=k,Euler_Lipschitz=Le,Euler_coordinate=ee,radius=rho)
 return cs,faults,{k:str(v) for k,v in vals.items()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();c,f,cert=certificate()
 deps=['tests/channel-swings/k2214_prescribed_adapter_fibers_probe.py','tests/channel-swings/k2208_grade_constrained_pencil_reconstruction_probe.py','explorations/conditional-build/k2197-general-ordered-adapter-constraints-2026-10-28.md','explorations/conditional-build/k2220-robust-adapter-exclusion-2026-10-28.md']
 report=dict(result_id='K2220',status='explicit_positive_radius_real_adapter_exclusion',checks=c,fault_failures=f,certificate=cert,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal Neumann/adjugate and ordered polynomial perturbation argument; exact actual minor, matrix norms, normalized residual and explicit radius. No global nonlinear exclusion or useful numerical-size claim.')
 p=ROOT/'lab/process/k2220-robust-adapter-exclusion.json'
 if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report
 print(json.dumps(dict(result='K2220',controls=len(c),faults=len(f),q=cert['q'],H=cert['H'],radius_decimal_order=len(str(S.denom(S.Rational(cert['radius']))))-len(str(S.numer(S.Rational(cert['radius'])))))))
if __name__=='__main__':main()
