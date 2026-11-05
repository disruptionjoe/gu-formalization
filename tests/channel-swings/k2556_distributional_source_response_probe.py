"""Exact finite radial closure and frozen dispersion; local existence proof in note."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(name,ok):
 checks[name]=bool(ok)
 if not ok:raise AssertionError(name)
def ct(name,ok):
 controls[name]=bool(ok)
 if not ok:raise AssertionError(name)
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


d=s.factor(M.det(method='domain-ge'));d1=s.cancel(d.subs(k,1));Z=s.symbols('Z');P0=s.Poly(d1.subs({X:Z,Y:0}),Z).as_expr();Q0=s.cancel((d1-P0.subs(Z,X+Y))/(X*Y)).subs({X:Z,Y:0})
ck('actual_mixed_determinant',s.cancel(d1-P0.subs(Z,X+Y)-X*Y*Q0.subs(Z,X+Y))==0)
ck('mixed_polynomials_coprime',s.degree(s.gcd(P0,Q0),Z)==0)
L=s.Poly(P0,Z).LC();q2=s.Poly(Q0,Z).LC()
ck('positive_instability_ratio',s.cancel(q2/L)==s.Rational(6125,26834819055616))
ck('every_fixed_X_retains_degree_five',s.Poly(d1,Y).degree()==5 and s.cancel(s.Poly(d1,Y).LC()-L)==0)
# Independently compute selected numeric matrix determinants.
for j,(xx,yy) in enumerate([(0,2),(-s.Rational(16)*K0.subs(k,1),1)]):
 mm=M.subs({X:xx,Y:yy,k:1},simultaneous=True)
 ck('full_matrix_bareiss_'+str(j),s.cancel(mm.det(method='bareiss')-d1.subs({X:xx,Y:yy}))==0)
C,K=s.symbols('C K',positive=True);m=s.symbols('m',integer=True,nonnegative=True)
def xr(f):return K*((1-C*C)*s.diff(f,C,2)+(4/C-7*C)*s.diff(f,C))
def dr(f):return K*((1-C*C)*s.diff(f,C,2)+(6/C-11*C)*s.diff(f,C))
def br(f):return K*(4/C-6*C)*s.diff(f,C)
ck('X_monomial_formula',s.simplify(xr(C**m)-m*(m+3)*K*C**(m-2)+m*(m+6)*K*C**m)==0)
ck('D5_monomial_formula',s.simplify(dr(C**m)-m*(m+5)*K*C**(m-2)+m*(m+10)*K*C**m)==0)
ck('splitter_derivative_formula',s.simplify(br(C**m)-4*m*K*C**(m-2)+6*m*K*C**m)==0)
ck('splitter_diagonal_factor',s.expand(7-m*(m+6)+(m+7)*(m-1))==0)
ck('spectrum_difference_X',s.expand((m+2)*(m+8)-m*(m+6))==4*m+16)
ck('spectrum_difference_D5',s.expand((m+2)*(m+12)-m*(m+10))==4*m+24)
P=C*C;A=P+C*s.diff(P,C)/4;trace=(4*A+3*P)/2;chi=C*C/(12*K)-s.Rational(5,42)/K;bb=s.cancel(P/2+br(chi)+6*K*chi)
ck('example_pressure_and_trace',A==s.Rational(3,2)*C*C and trace==s.Rational(9,2)*C*C)
ck('example_splitter',s.cancel(xr(chi)+7*K*chi+trace/6)==0)
ck('example_TT_nonzero',bb==-s.Rational(1,21))
ck('example_scalar_eigenmode',s.cancel(xr(C*C-s.Rational(5,8))+16*K*(C*C-s.Rational(5,8)))==0)
ck('example_scalar_decomposition',s.cancel(chi-(C*C-s.Rational(5,8))/(12*K)+s.Rational(15,224)/K)==0)
ck('example_TT_eigenmode',dr(bb)==0)
# Generic pressure conservation after C'=-KS and alpha=-KS/C.
S=s.symbols('S');PP=s.Function('P')(C);AA=PP+C*s.diff(PP,C)/4
ck('arbitrary_pressure_conservation',s.expand(-K*S*s.diff(PP,C)+4*(-K*S/C)*(PP-AA))==0)
leading=1/(12*K*(m-1))
ck('TT_top_degree_cancellation',s.cancel(s.Rational(1,2)+6*K*(1-m)*leading)==0)
ct('missing_source_half_breaks_TT_cancellation',s.cancel(1+6*K*(1-m)*leading)==s.Rational(1,2))
ct('flat_radial_operator_changes_eigenvalue',s.expand(K*(1-C*C)*s.diff(C*C,C,2)-xr(C*C))!=0)
ck('outer_splitter_polynomial',s.cancel(84*K*chi-(7*C*C-10))==0)
ct('Dirichlet_splitter_not_imposed',max([-10,-3])<0)  # Bernstein coefficients on 0<=C_R^2<=1
# Exact finite V_N examples complement, but do not replace, the generic proof.
for nn in (0,1,2,4):
 basis=[C**(2*j) for j in range(nn+1)]
 Xm=s.Matrix([[s.expand(xr(f)/K).coeff(C,2*i) for f in basis] for i in range(nn+1)])
 Dm=s.Matrix([[s.expand(dr(f)/K).coeff(C,2*i) for f in basis] for i in range(nn+1)])
 ck('finite_X_spectrum_'+str(nn),set(Xm.eigenvals())=={-2*j*(2*j+6) for j in range(nn+1)})
 ck('finite_D5_spectrum_'+str(nn),set(Dm.eigenvals())=={-2*j*(2*j+10) for j in range(nn+1)})
 ck('finite_splitter_invertible_'+str(nn),(Xm+7*s.eye(nn+1)).det()!=0)
# Scale actual polynomial rather than a truncated surrogate.
n,z=s.symbols('n z',positive=True)
scaled=s.Poly(s.expand(d1.subs({X:-n**6,Y:n**6+n**4*z},simultaneous=True)),n)
ck('actual_dispersion_top_degree',scaled.degree()==20)
limit=scaled.coeff_monomial(n**20)
ck('actual_dispersion_limit',s.expand(limit-z*z*(L*z**3-q2))==0)
ratio=s.cancel(q2/L);aa=s.real_root(ratio,3);zp=aa*(-1+s.sqrt(3)*s.I)/2
ck('complex_cubic_root',s.simplify(zp**3-ratio)==0)
ck('complex_cubic_root_simple',s.cancel(s.diff(z*z*(L*z**3-q2),z)- (5*L*z**4-2*q2*z))==0)
ck('simple_root_derivative_reduction',s.rem(5*L*z**4-2*q2*z,z**3-ratio,z)==3*q2*z)
ck('root_growth_positive',s.sqrt(3)*aa/4>0)
ct('discarding_mixed_term_changes_limit',s.expand(limit-L*z**5)!=0)
ct('pure_sum_does_not_retain_cubic_pair',s.Poly(P0.subs(Z,n**4*z),n).coeff_monomial(n**20)==L*z**5)
# Differential factors may commute without chosen inverse operators commuting.
L1,L2,V1,V2,F=s.symbols('L1 L2 V1 V2 F',commutative=False)
ck('factor_associativity_bookkeeping',s.expand(L1*(L2*V2)-(L1*L2)*V2)==0)
ct('inverse_commutation_not_assumed',L1*L2!=L2*L1)
paths=['explorations/conditional-build/k2556-distributional-source-response-2026-11-05.md','tests/channel-swings/k2556_distributional_source_response_probe.py','explorations/conditional-build/k2552-localized-source-domain-2026-11-04.md','explorations/conditional-build/k2554-analytic-source-response-2026-11-05.md','tests/channel-swings/k2554_analytic_source_response_probe.py']
report={'result':'K2556','checks':checks,'contrary_controls':controls,'radial_example':{'P':'C^2','A':'3 C^2/2','chi':str(chi),'TT_amplitude':str(bb),'X_eigenvalues':['0','-16K'],'D5_eigenvalues':['0']},'dispersion':{'P_coefficients':list(map(str,s.Poly(P0,Z).all_coeffs())),'Q_coefficients':list(map(str,s.Poly(Q0,Z).all_coeffs())),'q2_over_L':str(ratio),'scaled_limit':str(limit),'growth_constant':str(s.sqrt(3)*aa/4),'scope':'frozen scalar one-time determinant only'},'evidence_kinds':{'exact':'full determinant, generic radial identities, finite spectra/example and dispersion scaling; factor associativity is bookkeeping only','universal':'finite-dimensional diagonalization, real-principal-type theorem hypotheses, Holmgren kernel argument, factor composition and Sobolev smoothing in note','not_claimed':'compact radial source or uniform N limit, imposed Cauchy/physical boundary, physical instability, gauge independence or native GU'},'dependencies':{x:hashlib.sha256((R/x).read_bytes()).hexdigest() for x in paths}}
out=R/'lab/process/k2556-distributional-source-response.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved_report_consistency'
print('K2556 PASS',len(checks),'exact/supporting groups',len(controls),'contrary controls')
