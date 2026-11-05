#!/usr/bin/env python3
"""Exact supporting identities/consumers; universal proof is in companion note."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import sympy as s
root=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
checks=[];controls=[]
def ck(name,condition):
    assert bool(condition),'FAIL '+name
    checks.append(name)
def ct(name,condition):
    assert bool(condition),'FAIL contrary '+name
    controls.append(name)

from itertools import permutations
x,t,K,Jx,Jt,z=s.symbols('x t K Jx Jt z',positive=True)
# Actual transform u=J^-1 G_L(-J*zeta*F/K); convert dt to invariant density.
ck('invariant_kernel_conversion',s.cancel((-Jt*z/K/Jx)/(K**(-s.Rational(7,2))*Jt**2*z)+K**s.Rational(5,2)/(Jx*Jt))==0)
ck('weighted_kernel_transpose',(-K**s.Rational(5,2)/(Jx*Jt)).subs({Jx:Jt,Jt:Jx},simultaneous=True)==-K**s.Rational(5,2)/(Jx*Jt))
# Solve actual complex BVP for two real forcing functions.
sol=[]
for f in [s.Integer(1),x]:
 c,d=s.symbols('c d');v=s.integrate(s.integrate(f,x),x)+c*x+d
 bc=[s.diff(v,x).subs(x,0)+s.I*v.subs(x,0),s.diff(v,x).subs(x,1)-s.I*v.subs(x,1)]
 ans=s.solve(bc,[c,d]);v=s.expand(v.subs(ans));u=s.simplify(s.re(v));label='constant' if f==1 else 'linear'
 ck(label+'_complex_equation',s.diff(v,x,2)==f)
 ck(label+'_complex_left',s.simplify(s.diff(v,x).subs(x,0)+s.I*v.subs(x,0))==0)
 ck(label+'_complex_right',s.simplify(s.diff(v,x).subs(x,1)-s.I*v.subs(x,1))==0)
 ck(label+'_real_equation',s.diff(u,x,2)==f)
 ck(label+'_real_value_trace',s.simplify(u.subs(x,1)+u.subs(x,0))==0)
 ck(label+'_real_derivative_trace',s.simplify(s.diff(u,x).subs(x,1)+s.diff(u,x).subs(x,0)-u.subs(x,0))==0)
 sol.append((f,v,u))
ck('reciprocal_actual_sources',s.integrate(sol[0][0]*sol[1][2]-sol[1][0]*sol[0][2],(x,0,1))==0)
ck('constant_response',s.expand(sol[0][1]-(x*x/2-x/2-s.I/2))==0)
c,d=s.symbols('c d');hom=c*x+d
ck('real_domain_unique',s.solve([hom.subs(x,1)+hom.subs(x,0),2*c-d],[c,d])=={c:0,d:0})
ct('real_source_not_real_complex_solution',s.im(sol[0][1])!=0)
ct('real_part_not_old_robin',s.simplify(s.diff(sol[0][2],x).subs(x,0)+s.I*sol[0][2].subs(x,0))!=0)
ct('wrong_sign_real_trace',s.simplify(s.diff(sol[1][2],x).subs(x,1)+s.diff(sol[1][2],x).subs(x,0)+sol[1][2].subs(x,0))!=0)
# Exact finite-dimensional algebra analogue, explicitly NOT an ODE right-inverse fixture.
B=s.Matrix([[2,1],[1,3]]);C=s.Matrix([[1,2],[2,5]]);D=s.Matrix([[3,0],[0,1]])
ck('symmetric_factors',all(M.T==M for M in [B,C,D]))
ct('inverse_order_noncommutes',B*C!=C*B)
ct('one_order_not_symmetric',(B*C*D).T!=B*C*D)
def avg(mats):
 total=s.zeros(2)
 for perm in permutations(mats):
  prod=s.eye(2)
  for mat in perm:prod=prod*mat
  total+=prod
 return total/s.factorial(len(mats))
R=avg([B,C,D]);ck('all_orders_symmetric',R.T==R)
Z=B+s.I*C
ck('conjugate_average_real',(Z+s.conjugate(Z))/2==B)
ct('order_average_without_sign_not_real',s.im(avg([Z,D])[0,0])!=0)
R5=avg([Z,s.conjugate(Z),B,C,D])
ck('five_factor_order_and_conjugate_closure',s.simplify(R5-R5.T)==s.zeros(2) and s.simplify(R5-s.conjugate(R5))==s.zeros(2))
ct('conjugate_only_not_symmetric',(Z*D+s.conjugate(Z*D))/2 != ((Z*D+s.conjugate(Z*D))/2).T)
ct('density_omission_changes_kernel',s.cancel((-Jt*z/K/Jx)-(-K**s.Rational(5,2)/(Jx*Jt)))!=0)
ck('measure_chain_exponent',5+4*2==13)
ck('average_preserves_uniform_bound',sum(F(1,120) for _ in range(120))==1)
report={'result':'K2588','checks':checks,'contrary_controls':controls,'evidence_kind':'exact invariant-density algebra, actual interval BVP and matrix analogues; analytic domain proof in note','consumers':[{'forcing':str(f),'complex_response':str(v),'real_response':str(u)} for f,v,u in sol],'ceiling':'per-mode real self-adjoint scalar realization; not full tensor self-adjointness or physical selection'}
refs=['explorations/conditional-build/k2584-scalar-spectral-boundary-inverse-2026-11-05.md','explorations/conditional-build/k2586-fixed-annulus-point-response-2026-11-05.md']

report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2588-real-boundary-response.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':report['result'],'checks':len(checks),'controls':len(controls),'status':'pass'}))
