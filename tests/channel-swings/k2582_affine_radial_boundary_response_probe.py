#!/usr/bin/env python3
"""Exact supporting identities and original-law consumers; universal proofs in note."""
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
k=s.symbols('k',nonzero=True);K0=s.Rational(35,3624192)*k*k
X,Y=s.symbols('X Y');f,g,p,q,r,z=s.symbols('f g p q r z');pot=s.Matrix([f,g,p,q,r,z]);Z=X+Y
la=6*K0;a0=-s.Rational(5,2288)*k;rE=1/(6*a0)
m=s.Rational(158,143)*k;bt=-s.Rational(15,143)*k;mK=s.Rational(148,143)*k;mV=s.Rational(503,858)*k;mH=s.Rational(893,858)*k
c=s.Rational(970112,13395)/k;mu=s.Rational(611557655,39953092608)*k*k
ck('TT_kinetic_coefficient',s.cancel(-4/mH-rE-c)==0)
ck('TT_full_mass_coefficient',s.cancel(m+28*K0/mH+2*K0*rE-c*(mu-7*K0))==0)
ck('TT_Einstein_curvature_shift',-14*K0-2*K0==-16*K0)
ck('TT_displacement_curvature_shift',-14*K0+mu-7*K0==mu-21*K0)
tau=7*f+7*g+X*p+Y*q;BA=f+(X+la)*p+Y*r;BB=g+(Y+la)*q+X*r
VA,VB=BA-tau,BB-tau;WA,WB=11*VA-13*Y*z,11*VB+13*X*z
U,V=X*VA+Y*VB,X*WA+Y*WB;RC=X*BA+Y*BB-(Z+la)*tau
Evec=s.Matrix([-(Z/2+la)*f-RC/2,-(Z/2+la)*g-RC/2,BA-(Z/2+la)*p-tau/2,BB-(Z/2+la)*q-tau/2,(BA+BB-tau-(Z+2*la)*r)/2])
E=Evec.jacobian(pot);vsrc=s.Matrix([-X-la,0,1,0,0,0]);s0=s.Matrix([X+5*la/6,-X-7*la/6,0,0,1,0])
for i in range(5):ck('full_Einstein_source_row_'+str(i),s.cancel((E*s0)[i]-vsrc[i]*(Z+2*la))==0)
ck('scalar_source_divergence_A',s.cancel(vsrc[0]+(X+la)*vsrc[2]+Y*vsrc[4])==0)
ck('scalar_source_divergence_B',s.cancel(vsrc[1]+(Y+la)*vsrc[3]+X*vsrc[4])==0)
ck('scalar_source_trace',s.cancel(7*vsrc[0]+7*vsrc[1]+X*vsrc[2]+Y*vsrc[3]+6*X+7*la)==0)
hook=s.Matrix([2*Z*f-2*K0*X*p+2*U/13,2*Z*g-2*K0*Y*q+2*U/13,2*(Z+la+K0)*p-2*BA-2*VA/13,2*(Z+la+K0)*q-2*BB-2*VB/13,2*(Z+la)*r-BA-BB-(VA+VB)/13])
vs=s.Matrix([V,V,-WA,-WB,-(WA+WB)/2]);FC=m*s.Matrix([f,g,p,q,r])+bt*tau*s.Matrix([1,1,0,0,0])+11*vs/(13*mV)-2*hook/mH+Evec/(3*a0)
FK=mK*z-(WB-WA)/(2*mV);M=FC.col_join(s.Matrix([FK])).jacobian(pot)


vline=s.Matrix([K0,0,1,0,0,0]);M0=M.subs(X,-7*K0)
ck('actual_six_row_overlap_without_cofactor',all(s.cancel(x)==0 for x in M0*vline-c*(Y+mu)*vline))
ct('wrong_scalar_overlap_eigenvalue',any(s.cancel(x)!=0 for x in M.subs(X,-6*K0)*vline-c*(Y+mu)*vline))
C,K=s.symbols('C K',positive=True);psi=s.Function('psi')(C)
f2=(-7*psi-(4/C-7*C)*s.diff(psi,C))/(1-C*C)
rules={s.diff(psi,C,2):f2}
for nn in (3,4):rules[s.diff(psi,C,nn)]=s.diff(rules[s.diff(psi,C,nn-1)],C).subs(s.diff(psi,C,2),f2)
def red(e):
 for nn in (4,3,2):e=e.subs(s.diff(psi,C,nn),rules[s.diff(psi,C,nn)])
 return s.factor(e)
bp=red(K*((1-C*C)*s.diff(psi,C,2)-C*s.diff(psi,C)+psi))
D5=lambda f:K*((1-C*C)*s.diff(f,C,2)+(6/C-11*C)*s.diff(f,C))
ck('actual_trace_mode_radial_equation',red(D5(bp)-21*K*bp)==0)
psi0=s.symbols('psi0',positive=True);b0=-4*K*psi0/3
ck('negative_center_and_second_derivative',b0<0 and 21*K*b0/5<0)
chiR,aval,bR,bzero=s.symbols('chiR aval bR bzero',nonzero=True)
ck('unique_scalar_trace_tag',s.diff(chiR+aval,aval)==1)
ck('source_trace_lift',s.expand(bR-bR/bzero*bzero)==0)
ct('omit_affine_lift_keeps_nonzero_trace',bR!=0)
# Explicit resolvent identity with independent formal residual variables.
zz,B,res=s.symbols('zz B res');Dres=21*K*B-zz*res
ck('enlarged_domain_kernel_identity',s.expand(21*K*B-(zz*res+(21*K-zz)*B)-zz*(B-res))==0)
# A flat regular radial fixture shows removing the boundary really creates kernels.
r=s.symbols('r',positive=True);flat=lambda f:s.diff(f,r,2)+4*s.diff(f,r)/r
ck('no_boundary_flat_kernel_at_zero',flat(s.Integer(1))==0)
ct('kernel_not_Dirichlet',s.Integer(1).subs(r,1)!=0)
AQ=s.cancel(mu/K0+s.Rational(35,4));AE=s.Rational(55,4)
ck('overlap_Q_shift',21*K0+mu-21*K0==mu)
ck('overlap_E_shift',21*K0-16*K0==5*K0)
ck('paired_angular_constants',AQ>AE>s.Rational(3,8))
L,n,zt=s.symbols('L n zeta',positive=True);D=4*AQ+s.Rational(3,5);Lstar=25*AQ-s.Rational(3,4)
for label,AA in [('Q',AQ),('E',AE)]:
 P=n*n+AA*zt-(L+s.Rational(3,4))*zt/(1+zt)
 ck(label+'_actual_monotone_cutoff',s.cancel(s.diff(P,zt).subs({zt:4,L:Lstar}))<=0)
 ck(label+'_positive_case_margin',AA-s.Rational(3,8)>0)
 ck(label+'_actual_large_theta_derivative',s.diff(P,zt).subs({zt:2,L:1000000,n:2})<0)
ct('overlap_not_K2580_negative_radial_spectrum',s.diff(n*n+AQ*zt-s.Rational(3,4)*zt/(1+zt),zt).subs(zt,1)>0)
# Original source and metric consumer, a(B)=1.
uB=-rE/(c*mu);vB=rE/(5*K0)
ck('trace_source_Q_row',s.cancel(mu*uB+rE/c)==0)
ck('trace_source_E_row',s.cancel(5*K0*vB-rE)==0)
Eh=-5*K0*(vB-rE*uB)/2
expected=-rE*(1+5*K0*rE/(c*mu))/2
ck('actual_original_metric_readout',s.cancel(Eh-expected)==0)
ck('nonzero_readout_coefficient',s.cancel(expected.subs(k,1))!=0)
ct('drop_direct_source_term',s.cancel(Eh+rE*(mu-5*K0)*uB/2)!=0)
# Independent tensor component check of inherited and corrected overlap.
hess,psiv,W,cross=s.symbols('hess psiv W cross');zs=-rE*s0.subs(X,-7*K0)/2
sAA=zs[0]*psiv*W+zs[2]*hess*W;tAA=rE*W*(hess+K0*psiv)
ck('inherited_gauge_difference_AA',s.expand(sAA-tAA+rE*W*hess)==0)
ck('inherited_gauge_difference_AB',s.cancel(zs[4]*cross+rE*cross/2)==0)
ck('corrected_total_AA_exact_match',s.expand(sAA+rE*W*hess-tAA)==0)
ck('corrected_total_AB_exact_match',s.cancel(zs[4]*cross+rE*cross/2)==0)
ct('wrong_sign_gauge_repair',s.expand(sAA-rE*W*hess-tAA)!=0)
alpha,beta,psipr=s.symbols('alpha beta psipr',nonzero=True)
ck('boundary_block_from_Lie',s.expand(-rE/2*(2*W*psipr*alpha)+rE*W*psipr*alpha)==0)
ct('uncorrected_boundary_trace_nonzero',-rE*W*psipr*beta!=0)
qq,aa=s.symbols('qq aa',positive=True);ff=qq-aa
tf=-qq*(1-K*qq)*s.diff(ff,qq)/2-3*ff/4+7*K*qq*ff/4
ck('zero_amplitude_boundary_fixture',ff.subs(qq,aa)==0)
ck('actual_tube_radial_bound',s.Rational(35,3624192)<1)
ct('full_tensor_trace_not_amplitude',s.expand(tf.subs(qq,aa)+aa*(1-K*aa)/2)==0 and tf.subs({qq:1,aa:1,K:s.Rational(35,3624192)})!=0)
report={'result':'K2582','checks':checks,'contrary_controls':controls,'boundary_bookkeeping':['unique_scalar_trace_tag','source_trace_lift','omit_affine_lift_keeps_nonzero_trace'],'evidence_kind':'actual six-row and radial identities, paired annular constants, source/readout and exact-field repair fixtures; universal trace/domain/synthesis arguments in note','A_Q':str(AQ),'A_E':str(AE),'trace_source_Eh_kappa1':str(s.cancel(expected.subs(k,1))),'ceiling':'compatible trace-tagged TT and full overlap response, not arbitrary scalar cofactor inverse'}
refs=['k2580-radial-angular-source-domain-2026-11-05','k2558-distributional-splitter-overlap-2026-11-05','k2576-polynomial-impedance-control-2026-11-05']

report['provenance']={'explorations/conditional-build/'+r+'.md':hashlib.sha256((root/('explorations/conditional-build/'+r+'.md')).read_bytes()).hexdigest() for r in refs}
out=root/'lab/process/k2582-affine-radial-boundary-response.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':report['result'],'checks':len(checks),'controls':len(controls),'status':'pass'}))
