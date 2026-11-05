#!/usr/bin/env python3
"""Exact supporting identities and original-object consumers; universal proofs in note."""
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

kappa=s.symbols('kappa',positive=True);K=35*kappa**2/s.Integer(3624192)
rE=-s.Rational(1144,15)/kappa;c=s.Rational(970112,13395)/kappa;mu=s.Rational(611557655,39953092608)*kappa**2
A=s.cancel((mu-21*K)/K+s.Rational(35,4));gap=5*kappa**2
ck('actual_Q_coefficient',A==s.Rational(121366223,77168))
weight=1-s.Rational(11,3)*s.Rational(35,3624192)
ck('weight_lower_bound',weight==s.Rational(988381,988416) and weight>s.Rational(1,2))
ck('Q_radial_gap_margin',s.cancel(A-gap/K)==-s.Rational(39831726385,77168))
ck('E_radial_gap_margin',s.cancel(-16-gap/K+s.Rational(35,4))==-s.Rational(14496971,28))
r,R=s.symbols('r R',positive=True)
ck('radial_Poincare_integral',s.integrate(r**4*(r**-3-R**-3)/3,(r,0,R))==R**2/10)
z,L,n,sigma=s.symbols('z L n sigma',positive=True)
PQ=n*n+(A-sigma/K)*z-(L+s.Rational(3,4))*z/(1+z)
PE=n*n+(-s.Rational(29,4)-sigma/K)*z-(L+s.Rational(3,4))*z/(1+z)
ck('Q_monotonicity_identity',s.cancel(s.diff(PQ,z)-(A-sigma/K-(L+s.Rational(3,4))/(1+z)**2))==0)
ck('E_monotonicity_identity',s.cancel(s.diff(PE,z)-(-s.Rational(29,4)-sigma/K-(L+s.Rational(3,4))/(1+z)**2))==0)
ck('uniform_potential_constant',s.Rational(29,4)*4+s.Rational(3,4)*s.Rational(4,5)==s.Rational(148,5)<30)
ct('wrong_radial_sign_loses_monotonicity',s.diff(PQ,z).subs({sigma:-gap,L:0,kappa:1,z:1})>0)
ct('fixed_R1_not_globally_monotone',s.diff(PQ,z).subs({sigma:0,L:0,kappa:1,z:1})>0)
q,a=s.symbols('q a',positive=True)
D5=lambda f:4*q*(1-K*q)*s.diff(f,q,2)+(10-24*K*q)*s.diff(f,q)
DQ=lambda f:s.expand(D5(f)+(mu-21*K)*f)
DE=lambda f:s.expand(D5(f)-16*K*f)
W=(q-a)**5;u=DE(W);v=-c*DQ(W);src=-c/rE*DQ(DE(W))
ck('nonconstant_radial_Q_row',s.cancel(c*DQ(u)+rE*src)==0)
ck('nonconstant_radial_E_row',s.cancel(DE(v)-rE*src)==0)
ck('operator_commutation',s.expand(DQ(DE(W))-DE(DQ(W)))==0)
ck('Dirichlet_u_and_v',s.simplify(u.subs(q,a))==0 and s.simplify(v.subs(q,a))==0)
ck('source_in_form_domain',s.simplify(src.subs(q,a))==0)
ck('source_nonconstant',s.Poly(src,q).degree()>0)
T=lambda f:-q*(1-K*q)*s.diff(f,q)/2-s.Rational(3,4)*f+7*K*q*f/4
B=lambda f:q*(1-K*q)*s.diff(f,q)+(1-s.Rational(7,2)*K*q)*f
for name,f in [('source',src),('Q',u),('E',v)]:
 ck(name+'_TT_trace',s.expand(4*T(f)+f+2*B(f))==0)
 div=s.diff(f,q)-2*K/(1-K*q)*(f-T(f))+(f-B(f))/q
 ck(name+'_TT_divergence',s.cancel(div)==0)
 ck(name+'_regular_center',s.expand((f-B(f)).subs(q,0))==0)
h=v-rE*u;Eh=-DE(h)/2;direct=-rE*(1+rE/c)*src/2-rE*(mu-5*K)*u/2
ck('original_metric_observation',s.expand(Eh-direct)==0)
ck('nonzero_readout',s.Poly(Eh,q).degree()>=1)
ct('drop_E_breaks_source',s.Poly(rE*src,q).degree()>=1)
ct('shifted_metric_readout_wrong',s.expand(-DE(v)/2-Eh)!=0)
ct('omit_source_term_wrong',s.expand(Eh+rE*(mu-5*K)*u/2)!=0)
badsrc=-c/rE*DQ(DE((q-a)**3))
ct('smooth_not_zero_trace',s.simplify(badsrc.subs(q,a))!=0)
ct('amplitude_not_full_tensor_Dirichlet',s.simplify(T(src).subs(q,a))!=0)
report={'result':'K2580','evidence_kind':'exact gap and operator identities, actual nonconstant source fixture; universal spectral proof in note','checks':checks,'contrary_controls':controls,'weight_lower':str(weight),'uniform_k_squared':'1+n^2+L+4sigma/K+30','fixture':'W=(S(r)^2-S(R)^2)^5','ceiling':'fixed amplitude-Dirichlet/annular complex-impedance TT domain only'}
refs=['k2552-localized-source-domain-2026-11-04','k2576-polynomial-impedance-control-2026-11-05','k2578-coupled-forcing-adapter-2026-11-05']

report['provenance']={'explorations/conditional-build/'+r+'.md':hashlib.sha256((root/('explorations/conditional-build/'+r+'.md')).read_bytes()).hexdigest() for r in refs}
out=root/'lab/process/k2580-radial-angular-source-domain.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2580','checks':len(checks),'controls':len(controls),'status':'pass'}))
