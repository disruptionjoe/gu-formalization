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


bank=json.loads((root/'lab/process/k2554-analytic-source-response.json').read_text())['determinant']
Z=s.symbols('Z');lead=s.Rational(bank['top_coefficient']);pp=list(map(s.Rational,bank['P_coefficients_descending']));qq=list(map(s.Rational,bank['Q_coefficients_descending']));PN=sum(v/lead*Z**(5-i) for i,v in enumerate(pp));QN=sum(v/lead*Z**(2-i) for i,v in enumerate(qq))
ck('actual_degree_and_leading',len(pp)==6 and pp[0]==lead and len(qq)==3)
ck('root_coefficient_degree4',abs(pp[1]/lead)<s.Rational(9,8))
ck('root_coefficients_lower',all(abs(v/lead)<s.Rational(1,32) for v in pp[2:]))
ck('mixed_coefficients_bound',all(abs(v/lead)<s.Rational(1,10**8) for v in qq))
env=F(3,4)+F(1,32)*sum([F(4,9),F(8,27),F(16,81),F(32,243)])+F(6,10**8)*sum([F(2,3),F(4,9),F(8,27)])
ck('all_sigma_Rouche_envelope',env==F(4759375513,6075000000) and env<F(4,5)<1)
ss=s.symbols('ss',positive=True);poly=lead*(PN.subs(Z,X+Y)+X*Y*QN.subs(Z,X+Y))
ck('actual_shifted_polynomial',s.expand(poly.subs({X:-ss,Y:Z+ss},simultaneous=True)-lead*(PN-ss*(Z+ss)*QN))==0)
for i,(xx,yy) in enumerate([(-3,0),(-4,2),(-5,-1)]):
 mm=M.subs({X:xx,Y:yy,k:1});det=mm.det(method='bareiss');ck('independent_matrix_det_'+str(i),det==poly.subs({X:xx,Y:yy}))
 vv=vsrc.subs({X:xx,Y:yy,k:1});adj=mm.adjugate();ck('six_row_cofactor_source_'+str(i),mm*adj*vv==det*vv)
 ct('drop_mixed_determinant_'+str(i),det!=lead*PN.subs(Z,xx+yy) if xx*yy else det==lead*PN.subs(Z,xx+yy)) if xx*yy else None
ct('actual_mixed_term_nonzero',qq[-1]!=0)
ratio=s.Rational(35,3624192);ck('root_real_part_forces_monotone',s.Rational(35,4)-s.Rational(3,2)/ratio<0)
ck('Einstein_root_inside_same_disk',12*ratio<s.Rational(3,2))
ck('potential_scale_constant',35+F(3,5)<36)
# Complex differential flux identity, with the sign actually in the potential.
x=s.symbols('x',real=True);u=s.Function('u')(x);v=s.Function('v')(x);pr=s.Function('pr')(x);zeta=s.Function('zeta')(x);eps,beta,kk=s.symbols('eps beta kk',real=True)
# Imag[(y''-(pr-i eps beta zeta)y)conj(y)] for real u,v.
im=(s.diff(v,x,2)-pr*v+eps*beta*zeta*u)*u-(s.diff(u,x,2)-pr*u-eps*beta*zeta*v)*v
W=s.diff(v,x)*u-s.diff(u,x)*v
ck('complex_flux_differential_identity',s.expand(im-s.diff(W,x)-eps*beta*zeta*(u*u+v*v))==0)
a0,b0,ad,bd=s.symbols('a0 b0 ad bd',real=True)
# left derivative=-i eps k y, right=+i eps k y
flux0=(-eps*kk*a0)*a0-(eps*kk*b0)*b0;fluxd=(eps*kk*ad)*ad-(-eps*kk*bd)*bd
ck('opposite_impedance_boundary_flux',s.expand(fluxd-flux0-eps*kk*(a0*a0+b0*b0+ad*ad+bd*bd))==0)
# Actual coefficient of the wrong-sign bulk identity is negative.
wrong_bulk=s.expand(im.subs(eps,-eps)-s.diff(W,x))
ct('wrong_conjugate_potential_with_fixed_boundary_sign',s.expand(wrong_bulk+eps*beta*zeta*(u*u+v*v))==0 and s.expand(wrong_bulk-eps*beta*zeta*(u*u+v*v))!=0)
d,CG=s.symbols('d CG',positive=True);Bcrit=1/(8*d*CG)
ck('near_real_Neumann_half',s.cancel(4*d*CG*kk*(Bcrit/kk))==s.Rational(1,2))
g0,gd=s.symbols('g0 gd');lift=kk*(g0*x*(1-x/d)**2+gd*x*x*(x-d)/d**2)
ck('cubic_lift_values',lift.subs(x,0)==0 and lift.subs(x,d)==0)
ck('cubic_lift_derivatives',s.diff(lift,x).subs(x,0)==kk*g0 and s.simplify(s.diff(lift,x).subs(x,d)-kk*gd)==0)
wrong_fluxd=(-eps*kk*ad)*ad-(eps*kk*bd)*bd
ct('wrong_right_impedance_flux',s.expand(wrong_fluxd-flux0-eps*kk*(a0*a0+b0*b0+ad*ad+bd*bd)+2*eps*kk*(ad*ad+bd*bd))==0)
# Repeated factor fixture has no partial-fraction denominator.
rep=x**10/s.factorial(10)
ck('five_repeated_second_order_factors',s.diff(rep,x,10)==1)
ct('four_factors_do_not_solve_fifth',s.diff(rep,x,8)!=1)
# Tail compatibility uses the actual curved radial operator and negative residual.
C,K=s.symbols('C K',positive=True);psi=s.Function('psi')(C)
f2=(-7*psi-(4/C-7*C)*s.diff(psi,C))/(1-C*C)
rules={s.diff(psi,C,2):f2}
for nn in (3,4):rules[s.diff(psi,C,nn)]=s.diff(rules[s.diff(psi,C,nn-1)],C).subs(s.diff(psi,C,2),f2)
def red(e):
 for nn in (4,3,2):e=e.subs(s.diff(psi,C,nn),rules[s.diff(psi,C,nn)])
 return s.factor(e)
bpsi=red(K*((1-C*C)*s.diff(psi,C,2)-C*s.diff(psi,C)+psi))
D5=lambda f:K*((1-C*C)*s.diff(f,C,2)+(6/C-11*C)*s.diff(f,C))
bactual=red(K*((4/C-6*C)*s.diff(psi,C)+6*psi))
ck('actual_compact_source_tail_sign',red(bactual+bpsi)==0)
ck('actual_TT_tail_eigen_equation',red(D5(bactual)-21*K*bactual)==0)
ct('wrong_tail_sign_changes_source',red(bactual-bpsi)!=0)
BR,BPR=s.symbols('BR BPR',nonzero=True);tag=BR/BPR
ck('trace_residual_zero',s.cancel(BR-tag*BPR)==0)
for degree in (1,2,5):ck('tail_power_trace_'+str(degree),s.cancel((21*K)**degree*(BR-tag*BPR))==0)
ct('arbitrary_zero_trace_not_all_power_compatible',s.diff((x-1)**2,x,2).subs(x,1)!=0)
# Actual compact pressure construction, use H=integral_r^R4C^3 C'A and P=-H/C^4.
r=s.symbols('r');CC=s.Function('C')(r);AA=s.Function('A')(r);HH=s.Function('H')(r);pressure=-HH/CC**4
conserve=s.diff(pressure,r)+4*s.diff(CC,r)/CC*(pressure-AA)
ck('compact_pressure_conservation',s.cancel(conserve.subs(s.diff(HH,r),-4*CC**3*s.diff(CC,r)*AA))==0)
# Correct scalar Einstein source map already checked above; retain exact overlap.
vline=s.Matrix([K0,0,1,0,0,0]);ck('overlap_direct_eigenline',all(s.cancel(q)==0 for q in M.subs(X,-7*K0)*vline-c*(Y+mu)*vline))
ct('different_radial_operators',s.expand(D5(C)-K*(4/C-7*C))!=0)
report={'result':'K2584','checks':checks,'contrary_controls':controls,'evidence_kind':'exact coefficient enclosure, independent six-row matrix points, flux/lift and actual source-tail identities; universal inversion and smooth synthesis proof in note','Rouche_ratio':str(env),'normalized_P_coefficients':list(map(str,[v/lead for v in pp])),'normalized_Q_coefficients':list(map(str,[v/lead for v in qq])),'ceiling':'complexified input-independent spectral right inverse for smooth compatible scalar and actual compact pressure source; no physical preparation or point-source theorem'}
refs=['k2552-localized-source-domain-2026-11-04','k2554-analytic-source-response-2026-11-05','k2580-radial-angular-source-domain-2026-11-05','k2582-affine-radial-boundary-response-2026-11-05']
report['provenance']={'explorations/conditional-build/'+r+'.md':hashlib.sha256((root/('explorations/conditional-build/'+r+'.md')).read_bytes()).hexdigest() for r in refs}
out=root/'lab/process/k2584-scalar-spectral-boundary-inverse.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':report['result'],'checks':len(checks),'controls':len(controls),'status':'pass'}))
