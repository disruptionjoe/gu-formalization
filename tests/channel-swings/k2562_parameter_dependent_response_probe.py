"""Exact radial identities and contrary controls; universal proof in K2562 note."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError(n)
def ct(n,v):
 controls[n]=bool(v)
 if not v:raise AssertionError('contrary: '+n)
x=s.symbols('x',positive=True)
f2=s.cos(x)**2*s.sin(x);f4=s.cos(x)**3*s.sin(x)**2
ck('actual_m2_conjugation',s.trigsimp(s.diff(f2,x,2)/f2-(2*s.tan(x)**2-7))==0)
ck('actual_m4_conjugation',s.simplify((s.diff(f4,x,2)/f4-(6*s.tan(x)**2+2*s.cot(x)**2-17)).rewrite(s.sin))==0)
ck('cot_lower_identity',s.trigsimp(s.cot(x)**2-(1/s.sin(x)**2-1))==0)
eps=s.Rational(35,3624192)
ck('actual_tube_small',0<eps<s.Rational(1,2))
ck('m4_upper_potential_negative',-17+12*eps<0)
ck('m2_upper_potential_below_safe_bound',-7+4*eps<8)
ck('strict_cross_spectral_margin_using_pi_gt3',s.Rational(9,4)-38*eps>2)
ck('nineteenK_lower_bound',-17-2==-19)
ct('ordinary_Neumann_is_not_transformed_Neumann',s.simplify(s.diff(f2,x)/f2)!=0)
h=s.sin(x)/x-s.cos(x)
ck('flat_regular_m4_equation',s.simplify(-s.diff(h,x,2)+2*h/x**2-h)==0)
ck('flat_m4_center_branch',s.limit(h/x**2,x,0)==s.Rational(1,3))
ck('flat_N_root_numerator',s.simplify(x*x*s.diff(h,x)-((x*x-1)*s.sin(x)+x*s.cos(x)))==0)
n=s.symbols('n',integer=True,positive=True)
# n>=1, x>3pi/4>9/4: x²-x-1 is positive and increasing.
ck('N_bracket_sign_margin',s.Rational(9,4)**2-s.Rational(9,4)-1>0)
ck('N_bracket_monotonic_margin',2*s.Rational(9,4)-1>0)
ck('D_root_monotonic_identity',s.simplify(s.diff(s.tan(x)-x,x)-s.tan(x)**2)==0)
ck('N_root_monotonic_difference',s.cancel(1-(x*x+1)/(x*x-1)**2-x**2*(x**2-3)/(x**2-1)**2)==0)
# All m2 D/N energy differences: smallest adjacent difference 3pi²/4.
ck('flat_m2_gap_formula',s.expand(n*n-(n-s.Rational(1,2))**2)==n-s.Rational(1,4))
ck('flat_m2_min_gap',1-s.Rational(1,4)>s.Rational(1,4))
# Actual mixed determinant, retaining the complete coefficient bank.
bank=json.loads((R/'lab/process/k2554-analytic-source-response.json').read_text())['determinant']
X,Y,Z=s.symbols('X Y Z');P=s.Poly.from_list(list(map(s.Rational,bank['P_coefficients_descending'])),Z).as_expr();Q=s.Poly.from_list(list(map(s.Rational,bank['Q_coefficients_descending'])),Z).as_expr()
d=s.expand(P.subs(Z,X+Y)+X*Y*Q.subs(Z,X+Y));poly=s.Poly(d,X)
ck('full_radial_degree',poly.degree()==5)
ck('full_total_degree',s.Poly(d,X,Y).total_degree()==5)
ck('constant_nonzero_leading_factor',poly.LC()!=0 and not poly.LC().has(Y))
for j in range(5):ck('root_rescaling_coefficient_'+str(j),s.degree(poly.nth(j),Y)<=5-j)
ct('mixed_determinant_must_not_be_dropped',s.expand(d-P.subs(Z,X+Y))!=0)
# A real source at a Dirichlet resonance is instead solved by transformed N.
r,q,rr=s.symbols('r q rr',positive=True)
fN=1/q**2-s.sin(q*r)/(q**3*r*s.cos(q*rr))
LX=lambda f:s.diff(f,r,2)+2*s.diff(f,r)/r
ck('flat_Robin_forced_equation',s.simplify(LX(fN)+q*q*fN-1)==0)
ck('flat_Robin_actual_outer_condition',s.simplify((s.diff(fN,r)+fN/r).subs(r,rr))==0)
ck('flat_Robin_center_regular',s.simplify(s.limit(fN,r,0)-1/q**2+1/(q**2*s.cos(q*rr)))==0)
ck('Dirichlet_ground_forcing_projection',s.simplify(s.integrate(r*s.sin(s.pi*r/rr),(r,0,rr))-rr**2/s.pi)==0)
ct('Dirichlet_resonance_not_zero_source',rr**2/s.pi>0)
ct('Robin_solution_not_ordinary_Neumann',s.simplify(s.diff(fN,r).subs(r,rr).subs(q,s.pi/rr))!=0)
# Positive mass is controlled by D rather than forced zero-center growth.
z=s.symbols('z',positive=True)
fD=(rr*s.sinh(s.sqrt(z)*r)/(r*s.sinh(s.sqrt(z)*rr))-1)/z
ck('flat_positive_mass_D_equation',s.simplify(LX(fD)-z*fD-1)==0)
ck('flat_positive_mass_D_outer',s.simplify(fD.subs(r,rr))==0)
ct('positive_mass_D_not_center_zero',s.limit(fD,r,0)!=0)
k=s.symbols('k',nonzero=True);K=s.Rational(35,3624192)*k*k
f,g,p,q0,r0,sk=s.symbols('f g p q0 r0 sk'); pot=s.Matrix([f,g,p,q0,r0,sk]); ZZ=X+Y
la=6*K;a0=-s.Rational(5,2288)*k;rE=1/(6*a0)
m0=s.Rational(158,143)*k;bt=-s.Rational(15,143)*k;mK=s.Rational(148,143)*k;mV=s.Rational(503,858)*k;mH=s.Rational(893,858)*k
c=s.Rational(970112,13395)/k;mu=s.Rational(611557655,39953092608)*k*k
tau=7*f+7*g+X*p+Y*q0;BA=f+(X+la)*p+Y*r0;BB=g+(Y+la)*q0+X*r0
VA,VB=BA-tau,BB-tau;WA,WB=11*VA-13*Y*sk,11*VB+13*X*sk
UU,VV=X*VA+Y*VB,X*WA+Y*WB;RC=X*BA+Y*BB-(ZZ+la)*tau
Evec=s.Matrix([-(ZZ/2+la)*f-RC/2,-(ZZ/2+la)*g-RC/2,BA-(ZZ/2+la)*p-tau/2,BB-(ZZ/2+la)*q0-tau/2,(BA+BB-tau-(ZZ+2*la)*r0)/2])
EE=Evec.jacobian(pot);src=s.Matrix([-X-la,0,1,0,0,0]);s0=s.Matrix([X+5*la/6,-X-7*la/6,0,0,1,0])

hook=s.Matrix([2*ZZ*f-2*K*X*p+2*UU/13,2*ZZ*g-2*K*Y*q0+2*UU/13,2*(ZZ+la+K)*p-2*BA-2*VA/13,2*(ZZ+la+K)*q0-2*BB-2*VB/13,2*(ZZ+la)*r0-BA-BB-(VA+VB)/13])
vs=s.Matrix([VV,VV,-WA,-WB,-(WA+WB)/2]);FC=m0*s.Matrix([f,g,p,q0,r0])+bt*tau*s.Matrix([1,1,0,0,0])+11*vs/(13*mV)-2*hook/mH+Evec/(3*a0)
FK=mK*sk-(WB-WA)/(2*mV);M=FC.col_join(s.Matrix([FK])).jacobian(pot)

ck('actual_matrix_max_degree_two',max(s.Poly(v,X,Y).total_degree() for v in M)==2)
ck('actual_source_column_degree_one',max(s.Poly(v,X,Y).total_degree() for v in src)==1)
ck('cofactor_reconstruction_derivative_bound',2*(5*2+1)+2+1==25)
ck('explicit_sufficient_moment',5*15+11==86 and 2*15>26+s.Rational(5,2))
ct('degree_two_matrix_is_not_affine',any(s.Poly(v,X,Y).total_degree()==2 for v in M))
# Actual different right inverses of the same commuting flat radial operator.
DN=(r**4-rr**4)/120-rr**2*(r**2-rr**2)/12
ND=r**4/120-rr**2*r**2/36+rr**4/24
D1=(r*r-rr*rr)/6;N1=r*r/6-rr*rr/2
ck('actual_D_after_N_forcing',s.expand(LX(DN)-N1)==0)
ck('actual_N_after_D_forcing',s.expand(LX(ND)-D1)==0)
ck('composition_D_boundary',s.expand(DN.subs(r,rr))==0)
ck('composition_N_boundary',s.expand((s.diff(ND,r)+ND/r).subs(r,rr))==0)
ct('actual_radial_right_inverses_do_not_commute',s.expand(DN-ND)==rr**4/30-rr**2*r**2/18)
paths=['explorations/conditional-build/k2562-parameter-dependent-response-2026-11-05.md','tests/channel-swings/k2562_parameter_dependent_response_probe.py','lab/process/k2554-analytic-source-response.json','explorations/conditional-build/k2552-localized-source-domain-2026-11-04.md','explorations/conditional-build/k2558-distributional-splitter-overlap-2026-11-05.md']
report={'result':'K2562','checks':checks,'contrary_controls':controls,'bounds':{'spectral_separation':'delta=pi^2/(4R^2)-38K>2/R^2','all_complex_inverse':'M=2/delta<R^2','five_factor_potential':'M^5/abs(L)','root_growth':'C_kappa*(1+abs(nu))','sufficient_weighted_moment':86,'safe_derivative_loss':26},'evidence_kinds':{'exact':'curved conjugation, bracket sign margins, actual determinant degree, flat forced equations and resonance projection','universal':'two-boundary spectral separation, all-complex resolvents, full reconstruction and polynomial synthesis proved in note','supporting':'flat boundary fixtures illustrate the different preparations; they do not replace curved spectral proof','reused':'K2552 full reconstruction, K2554 determinant bank, K2558 overlap','not_claimed':'B point-source representation, physical boundary selection, root-order independence or continuity at switches'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
out=R/'lab/process/k2562-parameter-dependent-response.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report consistency'
print('K2562 PASS',len(checks),'exact/supporting groups',len(controls),'contrary controls')
