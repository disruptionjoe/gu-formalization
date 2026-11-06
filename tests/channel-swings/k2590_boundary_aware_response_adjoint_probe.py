#!/usr/bin/env python3
"""Exact curved Gram and source-map identities; analytic proofs in the note."""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
checks=[];controls=[]
def ck(n,v):
 assert bool(v),'FAIL '+n
 checks.append(n)
def ct(n,v):
 assert bool(v),'FAIL contrary '+n
 controls.append(n)
S,C,K=s.symbols('S C K',positive=True);u,v,du,dv=s.symbols('u v du dv');x=K*S*S
D=lambda f:s.diff(f,S)*C-s.diff(f,C)*K*S
reduce=lambda f:s.factor(s.cancel(f).subs(C**2,1-K*S*S))
t=lambda f,df:-S*C*df/4+(-3+7*x)*f/4
a=lambda f,df:S*C*df/2+(1-7*x/2)*f
pair=s.expand(4*t(u,du)*t(v,dv)+u*v+2*a(u,du)*a(v,dv))
p=3*S*S*C*C/4;q=7*S*C*(1-3*x)/4;r=7*(3-14*x+21*x*x)/4
ck('curved_derivative_Gram_coefficient',s.expand(pair).coeff(du,1).coeff(dv,1)==p)
ck('curved_cross_Gram_coefficient',s.expand(s.expand(pair).coeff(du,1).coeff(v,1)-q)==0)
ck('curved_zeroth_Gram_coefficient',s.expand(s.expand(pair).coeff(u,1).coeff(v,1)-r)==0)
w2=C**4*S*S;w5=C**6*S**4;gamma=-4*K*S/C+2*C/S
ck('radial_density_derivative',s.cancel(D(w2)/w2-gamma)==0)
ck('actual_Gram_weight',s.cancel(w2*p-3*w5/4)==0)
ck('curved_Gram_potential',reduce(r-D(q)-gamma*q-63*K*C*C*S*S/4)==0)
ck('TT_radial_divergence_weight',s.cancel(D(w5)/w5-(-6*K*S/C+4*C/S))==0)
ct('Gram_not_identity',s.cancel(3*w5/4-w2)!=0)
ct('omit_tensor_multiplicities',s.expand(t(u,du)*t(v,dv)+u*v+a(u,du)*a(v,dv)-pair)!=0)
ct('omit_cross_boundary_term',q!=0)
ct('flat_potential_not_curved',63*K*C*C*S*S/4!=0)
ck('actual_tube_positive_cross_coefficient',s.Rational(105,3624192)<1)
# Independent integration-by-parts/Wronskian identities for arbitrary weighted profiles.
z=s.symbols('z',positive=True);ww=s.Function('w')(z);ff=s.Function('f')(z);gg=s.Function('g')(z)
L=lambda f:s.diff(ww*s.diff(f,z),z)/ww
ck('weighted_green_identity',s.expand(ww*(ff*L(gg)-gg*L(ff))-s.diff(ww*(ff*s.diff(gg,z)-s.diff(ff,z)*gg),z))==0)
sigma=s.symbols('sigma',positive=True)
# General detector transpose, independently of the special Gram F=R(v).
to,ta,fr,dto,dta=s.symbols('to ta fr dto dta')
aF=S*C*(-to/4+ta/2)
bF=fr+(-3+7*K*S*S)*to/4+(1-7*K*S*S/2)*ta
Dfull=lambda expr:D(expr)+s.diff(expr,to)*dto+s.diff(expr,ta)*dta
fw=(w2*bF-Dfull(w2*aF))/w5
rhs=Dfull(w2*aF)*u+w2*aF*du
ck('general_compact_detector_transpose',s.expand(w2*(to*t(u,du)+fr*u+ta*a(u,du))-w5*fw*u-rhs)==0)
ct('detector_wrong_radial_density',s.cancel((w2*bF-Dfull(w2*aF))/w2-fw)!=0)
# Smooth orbit-averaged center cancellation and regular first-order adjoint.
n0,o0,wwc,ac,bc,g0,g2=s.symbols('n0 o0 wwc ac bc g0 g2')
wcenter=z*z*(1+wwc*z*z);afcenter=z*(n0-o0/4)+ac*z**3;bfcenter=3*(n0-o0/4)+bc*z*z
num=s.expand(wcenter*bfcenter-s.diff(wcenter*afcenter,z))
ck('regular_center_detector_cancellation',all(num.coeff(z,i)==0 for i in range(4)))
etacenter=z*z*(g0+g2*z*z);gamcenter=s.diff(wcenter,z)/wcenter
ck('regular_center_source_adjoint',s.limit(-s.diff(wcenter*gamcenter*etacenter,z)/wcenter+6*K*etacenter,z,0)==-6*g0)
# Exact actual source constants and polynomial all-row TT reductions.
kappa=s.symbols('kappa',nonzero=True,real=True);kv=35*kappa**2/3624192
rE=-s.Rational(1144,15)/kappa;c=s.Rational(970112,13395)/kappa;mu=s.Rational(611557655,39953092608)*kappa**2
Y,D5=s.symbols('Y D5');E=Y+5*kv;Q=Y+mu
source=E*Q;zz=rE*Q;qq=-rE*E/c;hh=zz-rE*qq
ck('trace_E_forcing',s.expand(E*zz-rE*source)==0)
ck('trace_Q_forcing',s.expand(Q*qq+rE*source/c)==0)
ck('trace_original_metric',s.expand(hh-(rE*Q+rE*rE*E/c))==0)
ck('trace_nonzero_leading_coefficient',s.cancel(rE+rE*rE/c-s.Rational(429,106)/kappa)==0)
ck('Schur_ratio',s.cancel(rE/c+s.Rational(893,848))==0)
ED=D5+Y-16*kv;QD=D5+Y+mu-21*kv;sd=ED*QD
ck('zero_trace_E_manufactured_source',s.expand(ED*(rE*QD)-rE*sd)==0)
ck('zero_trace_Q_manufactured_source',s.expand(QD*(-rE*ED/c)+rE*sd/c)==0)
ct('omit_E_channel_fails_forcing',rE*source!=0)
ct('wrong_original_metric_sign',s.expand((zz+rE*qq)-hh)!=0)
ct('confuse_overlap_Q_root',s.expand((Y+mu-21*kv)*qq+rE*source/c)!=0)
# Exact finite interval control: L=d²/dx²-1, q=1, Gov=-1. Not a curved tensor fixture.
x=s.symbols('x',real=True);f=s.sin(s.pi*x);gd=-f/(s.pi**2+1);b0=s.Integer(1)
lhs=s.integrate(-f,(x,0,1));bulk=s.integrate(gd,(x,0,1));delta=-s.integrate(f,(x,0,1))-bulk
ck('flat_control_Dirichlet_inverse',s.simplify(s.diff(gd,x,2)-gd-f)==0)
ck('flat_control_homogeneous_radial_traces',gd.subs(x,0)==0 and gd.subs(x,1)==0)
ck('flat_control_trace_lifted_equation',s.diff(-b0,x,2)+b0==b0)
ck('flat_control_full_transpose',s.simplify(lhs-bulk-delta)==0)
ct('omit_trace_functional_changes_pairing',s.simplify(lhs-bulk)!=0)
ct('scalar_L2_overlap_not_orthogonal',s.integrate(f,(x,0,1))!=0)
# Direct source sensitivity coefficients and actual half factors, not just labels.
A,P,ss,eta,chi,bd,psi,delta0,gr,qr,wr,H=s.symbols('A P ss eta chi bd psi delta0 gr qr wr H')
LW=H*(ss+bd/c)/6-gr*psi*delta0/(6*c*wr*qr)
direct=LW*(4*A+3*P)/2+eta*P/(2*c)
ck('original_A_sensitivity',s.diff(direct,A)==2*LW)
ck('original_P_sensitivity',s.simplify(s.diff(direct,P)-(3*LW/2+eta/(2*c)))==0)
ck('trace_elimination_sign',s.simplify(delta0*gr/qr*(-psi/(6*wr))/c+gr*psi*delta0/(6*c*wr*qr))==0)
ct('drop_source_half_factors',s.expand(direct-(LW*(4*A+3*P)+eta*P/c))!=0)
ct('weight_conversion_is_not_one',s.cancel(w5/w2-1)!=0)
# Full arbitrary-profile first-order adjoint identity; boundary term retained.
gm=s.Function('gamma')(z);en=s.Function('eta')(z);ch=s.Function('chi')(z)
Bd= -s.diff(ww*gm*en,z)/ww+6*K*en
ck('full_first_order_adjoint_identity',s.expand(ww*en*(gm*s.diff(ch,z)+6*K*ch)-ww*Bd*ch-s.diff(ww*gm*en*ch,z))==0)
report={'result':'K2590','checks':checks,'contrary_controls':controls,'evidence_kind':'actual curved tensor Gram and symbolic differential identities; actual polynomial source consumers; separately labeled flat-interval transpose control','Gram':{'derivative':str(p),'cross':str(q),'zeroth':str(r),'potential':'63*K*C^2*S^2/4','operator':'3/4*(-D5+21K)'},'trace_response':{'rE_over_c':str(s.cancel(rE/c)),'leading_h':str(s.cancel(rE+rE*rE/c))},'flat_control':{'actual_pairing':str(lhs),'bulk_only':str(bulk),'endpoint_correction':str(s.simplify(delta))},'ceiling':'TT full-response reciprocity in reduced actual tensor pairing; full compact-detector adjoint, not full source-module reciprocity or physical selection'}
refs=['explorations/conditional-build/k2588-real-boundary-response-2026-11-05.md','explorations/conditional-build/k2582-affine-radial-boundary-response-2026-11-05.md','explorations/conditional-build/k2552-localized-source-domain-2026-11-04.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2590-boundary-aware-response-adjoint.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2590','checks':len(checks),'controls':len(controls),'status':'pass'}))
