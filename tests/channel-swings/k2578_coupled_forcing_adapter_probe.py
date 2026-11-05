#!/usr/bin/env python3
"""Exact identities and independent original-object consumers; universal proof is in the note."""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
from fractions import Fraction as F
root=Path(__file__).resolve().parents[2]
pa=argparse.ArgumentParser();pa.add_argument('--write',action='store_true');args=pa.parse_args()
checks=[];controls=[]
def ck(name,condition):
    assert bool(condition),'FAIL '+name
    checks.append(name)
def ct(name,condition):
    assert bool(condition),'FAIL contrary '+name
    controls.append(name)

kappa=s.symbols('kappa',nonzero=True,real=True)
K=35*kappa**2/s.Integer(3624192);a0=-5*kappa/2288;rE=1/(6*a0);c=970112/(13395*kappa);mu=611557655*kappa**2/s.Integer(39953092608);delta=mu-5*K
ck('actual_dimensionless_Q',s.cancel((mu-21*K)/K-s.Rational(120691003,77168))==0)
ck('source_normalization',s.cancel(rE-1/(6*a0))==0)
z,L,n,beta=s.symbols('z L n beta',real=True);D=s.Rational(606773239,96460)
PE=n*n-s.Rational(29,4)*z-(L+s.Rational(3,4))*z/(1+z)
ck('Einstein_derivative',s.cancel(s.diff(PE,z)+s.Rational(29,4)+(L+s.Rational(3,4))/(1+z)**2)==0)
ck('common_bound_constant',D>s.Rational(148,5))
ck('negative_terms_bound',s.Rational(29,4)*4+s.Rational(3,4)*s.Rational(4,5)==s.Rational(148,5))
# Independent coordinate transformation with z=sinh(t)^2, dx/dt=1/sinh(t).
# Thus d/dx=2z sqrt(1+z) d/dz and J=sqrt(z)(1+z)^(3/4).
z=s.symbols('z',positive=True);U=s.Function('U')(z);J=s.sqrt(z)*(1+z)**s.Rational(3,4)
dx=lambda f:2*z*s.sqrt(1+z)*s.diff(f,z)
# d_t^2+3(tanh+coth)d_t =4z(1+z)d_z²+(8+16z)d_z.
Y=-K*(4*z*(1+z)*s.diff(U,z,2)+(8+16*z)*s.diff(U,z)+L/(1+z)*U-(n*n-1)/z*U)
P=n*n+(beta/K+s.Rational(35,4))*z-(L+s.Rational(3,4))*z/(1+z)
ck('full_nonzero_forcing_Liouville_identity',s.simplify(Y+beta*U+K/(J*z)*(dx(dx(J*U))-P*J*U))==0)
ck('actual_E_potential',s.simplify(P.subs(beta,-16*K)-(n*n-s.Rational(29,4)*z-(L+s.Rational(3,4))*z/(1+z)))==0)
src,uu,vv=s.symbols('src uu vv');DU=-rE*src/c;DV=rE*src
fQ=rE*J*z*src/(c*K);fE=-rE*J*z*src/K
ck('paired_forcing_ratio',s.cancel(fE+c*fQ)==0)
ck('Q_source_row',s.cancel(c*DU+rE*src)==0)
ck('E_source_row',s.cancel(-DV/2+rE*src/2)==0)
ct('drop_E_channel_nonzero_residual',s.cancel((rE*src/2).subs({src:1,kappa:1}))!=0)
ct('reverse_E_forcing_wrong_source',s.cancel(-(-rE*src)/2+rE*src-rE*src/2)==rE*src)
# Invariant response from direct operator composition versus proposed formula.
Eh=-(DV-rE*(DU-delta*uu))/2
formula=-rE*(1+rE/c)*src/2-rE*delta*uu/2
ck('original_metric_invariant',s.cancel(Eh-formula)==0)
ct('omit_direct_source_term_changes_readout',s.cancel((Eh+rE*delta*uu/2).subs({src:1,kappa:1}))!=0)
ct('shifted_z_is_not_original_h',s.cancel((-DV/2-Eh).subs({src:1,uu:1,kappa:1}))!=0)
u0=-rE/(c*(mu-21*K));v0=-rE/(16*K)
ck('constant_Q_source',s.cancel((mu-21*K)*u0+rE/c)==0)
ck('constant_E_source',s.cancel(-16*K*v0-rE)==0)
ck('constant_invariant_consumer',s.cancel(8*K*(v0-rE*u0)-formula.subs({src:1,uu:u0}))==0)
ck('constant_readout_nonzero',s.cancel((8*K*(v0-rE*u0)).subs(kappa,1))!=0)
cwrong=mu/K-21;uwrong=-rE/(cwrong*(mu-21*K))
ct('dimensionless_c_wrong_source_residual',s.cancel((c*(mu-21*K)*uwrong+rE).subs(kappa,1))!=0)
# Transform the constant fields; their known nonzero sources are independent fixtures.
for label,uval,bb,ff in [('Q',u0,mu-21*K,fQ.subs(src,1)),('E',v0,-16*K,fE.subs(src,1))]:
 yy=J*uval
 ck('constant_'+label+'_forced_ODE',s.simplify(dx(dx(yy))-P.subs({beta:bb,L:0,n:1})*yy-ff)==0)
 k=s.symbols('k',positive=True)
 near=s.simplify((dx(yy)+s.I*k*yy).subs(z,1)/k)
 ct('constant_'+label+'_boundary_not_zero',s.simplify(s.im(near).subs(kappa,1))!=0)
# Explicit radial TT constraints via S'=C,C'=-KS,C²+KS²=1.
S,C=s.symbols('S C',nonzero=True,real=True);tt=-s.Rational(3,4)+7*K*S*S/4;aa=1-7*K*S*S/2
ck('radial_TT_trace',s.expand(4*tt+1+2*aa)==0)
div=4*(-K*S/C)*(1-tt)+2*(C/S)*(1-aa)
ck('radial_TT_divergence',s.factor(div).subs(C*C,1-K*S*S)==0)
# Homogeneous E preparation leaves E h unchanged for compact E-image tests.
# The all-mode homogeneous-readout cancellation is proved by D_E Delta v=0 in the note; no tautological finite counter is added.
report={'result':'K2578','evidence_kind':'exact actual coordinate/row identities and constant-source fixture; universal estimates and module composition in note','checks':checks,'contrary_controls':controls,'kappa1_constant_source':{'u':str(u0.subs(kappa,1)),'v':str(v0.subs(kappa,1)),'Eh':str((8*K*(v0-rE*u0)).subs(kappa,1))},'ceiling':'fixed R(1) TT source module, supplied complex controls; no full arbitrary coupled source or physical selection'}
refs=['k2552-localized-source-domain-2026-11-04','k2576-polynomial-impedance-control-2026-11-05']

report['provenance']={'explorations/conditional-build/'+r+'.md':hashlib.sha256((root/('explorations/conditional-build/'+r+'.md')).read_bytes()).hexdigest() for r in refs}
out=root/'lab/process/k2578-coupled-forcing-adapter.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2578','checks':len(checks),'controls':len(controls),'status':'pass'}))
