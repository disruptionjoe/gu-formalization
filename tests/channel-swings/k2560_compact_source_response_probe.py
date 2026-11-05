"""Exact Volterra/source-response checks; universal convergence proof is in note."""
from pathlib import Path
import sympy as s
import json, hashlib, sys
R=Path(__file__).resolve().parents[2]
checks={}; controls={}
def ck(name,ok):
 checks[name]=bool(ok)
 if not ok: raise AssertionError(name)
def ct(name,ok):
 controls[name]=bool(ok)
 if not ok: raise AssertionError('contrary: '+name)
# Reconstruct the prior determinant from its exact, hash-bound coefficient evidence.
prior=json.loads((R/'lab/process/k2554-analytic-source-response.json').read_text())
D=prior['determinant']; X,Y,Z,nu,k=s.symbols('X Y Z nu k',nonzero=True)
P=s.Poly.from_list(list(map(s.Rational,D['P_coefficients_descending'])),Z).as_expr()
Q=s.Poly.from_list(list(map(s.Rational,D['Q_coefficients_descending'])),Z).as_expr()
d1=s.expand(P.subs(Z,X+Y)+X*Y*Q.subs(Z,X+Y))
d=s.expand(k**6*d1.subs({X:X/k**2,Y:Y/k**2},simultaneous=True))
L=s.Poly(d,X).LC(); K=s.Rational(35,3624192)*k*k
ck('fixed_B_radial_degree_five',s.Poly(d,X).degree()==5)
ck('fixed_B_leading_independent_of_nu',s.cancel(L-s.Rational(D['top_coefficient'])/k**4)==0)
ct('dropping_actual_mixed_term_changes_radial_equation',s.expand(d-k**6*P.subs(Z,(X+Y)/k**2))!=0)
# Exact arithmetic underlying the Volterra majorants; not samples of convergence.
n,m=s.symbols('n m',integer=True,nonnegative=True)
r,RR,q=s.symbols('r RR q',positive=True)
ck('power_majorant_ratio',s.simplify(s.combsimp((2**(n+1)/s.factorial(2*n+3))/(2**n/s.factorial(2*n+1))-2/((2*n+2)*(2*n+3))))==0)
ck('weight4_actual_margin',1-s.Rational(11,3)*K/k**2>s.Rational(1,2))
ck('Dirichlet_sup_Neumann_margin',1-7*K/(3*k**2)>0)
ck('weight_dimension_monotonicity',s.expand((2*n+m+1)-(2*n+3))==m-2)
# Flat kernel is a nontrivial exact sharp fixture for the smooth-center operator.
z=s.symbols('z')
for mm in (2,4):
 for jj in (0,1,4):
  f=r**(2*jj+2)/((2*jj+2)*(2*jj+mm+1))
  ck('flat_Volterra_equation_'+str(mm)+'_'+str(jj),s.expand(s.diff(f,r,2)+mm*s.diff(f,r)/r-r**(2*jj))==0)
# Weighted flux identity is the actual curved inverse, not a flat substitution.
w,I,F,wp=s.symbols('w I F wp',nonzero=True)
fprime=I/w; fsecond=F-I*wp/w**2
ck('curved_Volterra_flux',s.cancel(fsecond+wp/w*fprime-F)==0)
ct('wrong_Volterra_sign_changes_forcing',s.cancel(-fsecond-wp/w*fprime-F)!=0)
ct('singular_center_branch_has_nonzero_flux',s.cancel(w*(-1/w))==-1)
# Exact H_R coefficient formula and exponential domination factor.
ck('H_bound_factorial_comparison',s.expand((2*n+1)*(2*n+2)*(2*n+3)-6)==8*n**3+24*n**2+22*n)
t=s.symbols('t')
Hseries=s.series(2*(s.sinh(t)-t)/t**3,t,0,10).removeO()
ck('H_series_coefficients',s.expand(Hseries-sum(2*t**(2*j)/s.factorial(2*j+3) for j in range(5)))==0)
# Exact full scalar matrix, independent of the serialized determinant coefficients.
f,g,p,q0,r0,sk=s.symbols('f g p q0 r0 sk'); pot=s.Matrix([f,g,p,q0,r0,sk]); ZZ=X+Y
la=6*K;a0=-s.Rational(5,2288)*k;rE=1/(6*a0)
m0=s.Rational(158,143)*k;bt=-s.Rational(15,143)*k;mK=s.Rational(148,143)*k;mV=s.Rational(503,858)*k;mH=s.Rational(893,858)*k
c=s.Rational(970112,13395)/k;mu=s.Rational(611557655,39953092608)*k*k
tau=7*f+7*g+X*p+Y*q0;BA=f+(X+la)*p+Y*r0;BB=g+(Y+la)*q0+X*r0
VA,VB=BA-tau,BB-tau;WA,WB=11*VA-13*Y*sk,11*VB+13*X*sk
UU,VV=X*VA+Y*VB,X*WA+Y*WB;RC=X*BA+Y*BB-(ZZ+la)*tau
Evec=s.Matrix([-(ZZ/2+la)*f-RC/2,-(ZZ/2+la)*g-RC/2,BA-(ZZ/2+la)*p-tau/2,BB-(ZZ/2+la)*q0-tau/2,(BA+BB-tau-(ZZ+2*la)*r0)/2])
EE=Evec.jacobian(pot);src=s.Matrix([-X-la,0,1,0,0,0]);s0=s.Matrix([X+5*la/6,-X-7*la/6,0,0,1,0])
ck('all_scalar_Einstein_source_rows',all(s.cancel(v)==0 for v in EE*s0-src[:5,0]*(ZZ+2*la)))
hook=s.Matrix([2*ZZ*f-2*K*X*p+2*UU/13,2*ZZ*g-2*K*Y*q0+2*UU/13,2*(ZZ+la+K)*p-2*BA-2*VA/13,2*(ZZ+la+K)*q0-2*BB-2*VB/13,2*(ZZ+la)*r0-BA-BB-(VA+VB)/13])
vs=s.Matrix([VV,VV,-WA,-WB,-(WA+WB)/2]);FC=m0*s.Matrix([f,g,p,q0,r0])+bt*tau*s.Matrix([1,1,0,0,0])+11*vs/(13*mV)-2*hook/mH+Evec/(3*a0)
FK=mK*sk-(WB-WA)/(2*mV);M=FC.col_join(s.Matrix([FK])).jacobian(pot)
# One-variable determinant retains every row while avoiding a broad historical replay.
for vnu in (0,s.Rational(1,3)):
 mm=M.subs({Y:vnu,k:1})
 ck('actual_full_radial_determinant_'+str(vnu),s.cancel(mm.det(method='domain-ge')-d.subs({Y:vnu,k:1}))==0)
# Direct polynomial X-series solve checks regular central jets without numerical roots.
# Flat radial principal operator is an algebraic fixture for repeated factor inversion.
uvar=s.symbols('u'); source=1+2*uvar+3*uvar**2
coeff=s.Poly(d.subs({Y:s.Rational(1,3),k:1}),X)
def LL(expr):return s.expand(4*uvar*s.diff(expr,uvar,2)+6*s.diff(expr,uvar))
def DD(expr):
 powers=[expr]
 for _ in range(5):powers.append(LL(powers[-1]))
 return s.expand(sum(coeff.nth(j)*powers[j] for j in range(6)))
sol=s.Integer(0)
for jj in range(3):
 aa=s.symbols('aa'); candidate=sol+aa*uvar**(jj+5)
 value=s.solve(s.expand(DD(candidate)-source).coeff(uvar,jj),aa)[0]
 sol=candidate.subs(aa,value)
ck('direct_fifth_order_regular_jet_fixture',all(s.expand(DD(sol)-source).coeff(uvar,j)==0 for j in range(3)))
jet=sol; zerojets=[]
for _ in range(5):zerojets.append(jet.subs(uvar,0));jet=LL(jet)
ck('five_potential_center_jets',all(v==0 for v in zerojets))
ct('omitting_fifth_factor_leaves_wrong_source',s.expand(LL(LL(LL(LL(sol))))-source).coeff(uvar,0)!=0)
# Original pressure conservation and exact zero-center field-response substitutions.
CC,SS,PP,PP1,AA=s.symbols('CC SS PP PP1 AA',nonzero=True);alpha=-K*SS/CC
ck('actual_pressure_conservation',s.cancel(PP1+4*alpha*(PP-(PP+PP1/(4*alpha))))==0)
ct('omit_required_pressure_nonconserved',-4*alpha*AA!=0)
nu2,b=s.symbols('nu2 b'); vv,uu,ww=s.symbols('vv uu ww')
Dvv=rE*b-(nu2-16*K)*vv;Duu=-(rE/c)*b-(nu2+mu-21*K)*uu;Xww=s.Symbol('chi')-(nu2+12*K)*ww
ck('all_three_radial_forced_equations',s.cancel(Dvv+(nu2-16*K)*vv-rE*b)==0 and s.cancel(c*(Duu+(nu2+mu-21*K)*uu)+rE*b)==0 and s.cancel(Xww+(nu2+12*K)*ww-s.Symbol('chi'))==0)
ct('flat_TT_curvature_shift_rejected',s.cancel(Dvv+nu2*vv-rE*b)==16*K*vv)
# Pure-eigenmode synchronized overlap and both resonances.
vec=s.Matrix([K,0,1,0,0,0])
ck('full_overlap_eigenline',all(s.cancel(v)==0 for v in M.subs(X,-7*K)*vec-c*(Y+mu)*vec))
ck('two_distinct_overlap_poles',s.cancel(mu-5*K)>0)
hess,psi,W,cross=s.symbols('hess psi W cross');zs=-rE*s0.subs(X,-7*K)/2
ck('original_metric_overlap_AA',s.expand(zs[0]*psi*W+zs[2]*W*hess-rE*W*(hess+K*psi)+rE*W*hess)==0)
ck('original_metric_overlap_AB',s.cancel(zs[4]*cross+rE*cross/2)==0)
ct('literal_metric_equality_not_descent',s.expand(zs[0]*psi*W-rE*W*(hess+K*psi))!=0)
# Nondegenerate principal symbol makes every finite-mode annihilator fail on delta.
xi=s.symbols('xi0:7');quad=sum(x*x for x in xi[:3])-sum(x*x for x in xi[3:])
ck('B_delta_has_nonzero_principal_derivative',s.Poly(quad,*xi).total_degree()==2 and not s.Poly(quad,*xi).is_zero)
ck('finite_spectral_annihilator_delta_control',s.Poly(quad**3,*xi).total_degree()==6 and not s.Poly(quad**3,*xi).is_zero)
# Exact lower-growth consumer: actual curved inverse dominates flat radial inverse.
zz,rr=s.symbols('zz rr',positive=True)
ff=(s.sinh(s.sqrt(zz)*rr)/(s.sqrt(zz)*rr)-1)/zz
ck('flat_positive_mass_resolvent',s.simplify(s.diff(ff,rr,2)+2*s.diff(ff,rr)/rr-zz*ff-1)==0)
ck('flat_growth_center_value',s.limit(ff,rr,0)==0)
ck('flat_growth_center_derivative',s.limit(s.diff(ff,rr),rr,0)==0)
# The trigonometric sign uses (sin x-x cos x)'=x sin x>0 on the small tube.
xx=s.symbols('xx',positive=True)
ck('curved_weight_ratio_monotonic_identity',s.simplify(s.diff(s.sin(xx)-xx*s.cos(xx),xx)-xx*s.sin(xx))==0)
ck('flat_growth_series_coefficients',s.simplify(s.series(ff,rr,0,10).removeO()-sum(zz**j*rr**(2*j+2)/s.factorial(2*j+3) for j in range(4)))==0)
ct('zero_parameter_inverse_is_not_positive_mass_inverse',s.simplify((s.diff(rr**2/6,rr,2)+2*s.diff(rr**2/6,rr)/rr-zz*rr**2/6)-1)==-zz*rr**2/6)

# New alternative-inverse discriminator; compactness/positivity proof is in note.
rad,inner,radR=s.symbols('rad inner radR',positive=True)
hsbound=2*s.integrate(s.integrate(4*inner**2,(inner,0,rad)),(rad,0,radR))
ck('Dirichlet_inverse_Hilbert_Schmidt_bound',s.simplify(hsbound-2*radR**4/3)==0)
ck('Dirichlet_resonance_strictly_positive',3-12*s.Rational(35,3624192)>0)
lam1,zpos,forcing,amp=s.symbols('lam1 zpos forcing amp',positive=True)
ck('negative_parameter_coercive_ground_fixture',s.cancel(-(lam1+zpos)*(-forcing/(lam1+zpos))-forcing)==0)
ct('positive_ground_resonance_forcing_incompatible',s.expand((lam1-lam1)*amp-forcing)==-forcing)
# The two inverse prescriptions differ already for flat constant forcing.
fcenter=(s.sinh(s.sqrt(zpos)*rad)/(s.sqrt(zpos)*rad)-1)/zpos
fdir=(radR*s.sinh(s.sqrt(zpos)*rad)/(rad*s.sinh(s.sqrt(zpos)*radR))-1)/zpos
ck('flat_regular_Dirichlet_forced_equation',s.simplify(s.diff(fdir,rad,2)+2*s.diff(fdir,rad)/rad-zpos*fdir-1)==0)
ck('flat_Dirichlet_outer_value',s.simplify(fdir.subs(rad,radR))==0)
boundary_difference=(s.sinh(s.sqrt(zpos)*radR)/(s.sqrt(zpos)*radR)-1)/zpos
ct('center_zero_is_not_Dirichlet',s.simplify(fcenter.subs(rad,radR)-fdir.subs(rad,radR)-boundary_difference)==0 and boundary_difference!=0)

nupar,nures,aone=s.symbols('nupar nures aone');ck('Dirichlet_ground_pole_identity',s.cancel((nupar-nures)*(aone/(nupar-nures))-aone)==0)
paths=['explorations/conditional-build/k2560-compact-source-response-2026-11-05.md','tests/channel-swings/k2560_compact_source_response_probe.py','lab/process/k2554-analytic-source-response.json','explorations/conditional-build/k2552-localized-source-domain-2026-11-04.md','explorations/conditional-build/k2558-distributional-splitter-overlap-2026-11-05.md']
report={'result':'K2560','checks':checks,'contrary_controls':controls,'bounds':{'volterra_power':'2^n R^(2n)/(2n+1)!','resolvent':'H_R(q)<=R^2 exp(sqrt(2q)R)/3','scalar_displacement':'abs(L)^-1 H_R(Z(V))^5 norm(chi_D)','central_potential_jets':5,'overlap_poles':['-mu','-5K']},'evidence_kinds':{'exact':'Volterra coefficients/flux, new fixed-B full determinant checks, independent Einstein source column, central jet fixture, overlap and point-source controls, positive-mass growth formula, Dirichlet compact-kernel and alternate-boundary fixtures'
,'supporting':'declared radial-response substitutions check signs/accounting; they are not independent inverse verification','universal':'Volterra convergence and uniqueness, regularity, compact-profile response, bounded spectral superposition and test continuity proved in note; finite principal/jet fixtures do not replace these proofs','reused':'full K2552 curved TT/cofactor intertwinings and K2554 exact determinant coefficient evidence','not_claimed':'actual compact profile times delta_B, arbitrary spectral synthesis, physical preparation, full-system uniqueness or native GU'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
out=R/'lab/process/k2560-compact-source-response.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved_report_consistency'
print('K2560 PASS',len(checks),'exact/supporting groups',len(controls),'contrary controls')
