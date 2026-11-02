"""Literal graph contractions, full ten-component Fourier matrix and scoped controls."""
from pathlib import Path
import sympy as s
import itertools,json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not checks[k]:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not controls[k]:raise AssertionError(k)
q=s.Rational;g=s.diag(1,-1,-1,-1);pairs=[(i,j) for i in range(4) for j in range(i,4)];E=[]
for i,j in pairs:
 h=s.zeros(4);h[i,j]=h[j,i]=1;E.append(h)
def pair(h,j):return s.trace(g*h*g*j)-s.trace(g*h)*s.trace(g*j)/2
V=s.Matrix(10,10,lambda a,b:pair(E[a],E[b]));Vi=V.inv()
Z={(i,j):sum((-sum(Vi[A,B]*E[B][i,j] for B in range(10))*E[A]/2 for A in range(10)),s.zeros(4)) for i,j in itertools.product(range(4),repeat=2)}
Ztr=sum((g[i,i]*Z[i,i] for i in range(4)),s.zeros(4))
ck('literal_II_norm',sum(g[i,i]*g[j,j]*pair(Z[i,j],Z[i,j]) for i,j in itertools.product(range(4),repeat=2))==2)
ck('literal_mean_norm',pair(Ztr,Ztr)==-1)
ck('literal_receiver_all100_entries',all(-2*pair(Z[i,j],E[A])==E[A][i,j] for A in range(10) for i,j in pairs))
ck('vertical_inertia',sum(mult for ev,mult in V.eigenvals().items() if ev>0)==6 and sum(mult for ev,mult in V.eigenvals().items() if ev<0)==4)
alpha,beta=s.symbols('alpha beta');ck('stationarity_and_second_order_intersection',s.solve([2*alpha-beta,alpha+beta],[alpha,beta])=={alpha:0,beta:0})
# Explicit ordinary derivatives of constant-section density, retaining measure.
eps=s.symbols('eps',real=True)
for A,H in enumerate(E):
 Y=g+eps*H;density=(alpha-beta/2)*s.sqrt(-Y.det());der=s.diff(density,eps).subs(eps,0)
 ck('full_constant_Euler_component_'+str(A),s.simplify(der-(2*alpha-beta)*s.trace(g*H)/4)==0)
def invs(H,k):
 w=(k.T*g*k)[0];a=s.trace(g*H);d=s.trace(g*H*g*H);b=(k.T*g*H*g*k)[0];c=(k.T*g*H*g*H*g*k)[0]
 return w,a,d,b,c,d-a*a/2
def Q(H,k):
 w,a,d,b,c,v=invs(H,k);return s.expand(3*w*w*v+a*b/2-w*d/4+w*a*a/2)
def bil(H,J,k):
 w=(k.T*g*k)[0];C=3*w*w-w/4;D=-3*w*w/2+w/2;a=s.trace(g*H);aj=s.trace(g*J);b=(k.T*g*H*g*k)[0];bj=(k.T*g*J*g*k)[0]
 return s.expand(C*s.trace(g*H*g*J)+D*a*aj+(a*bj+aj*b)/4)
def matrix(k):return s.Matrix(10,10,lambda i,j:bil(E[i],E[j],k))
def direct_gradient_phase(H,k,omit_projection=False):
 # Actual ambient acceleration, normal projection, and inverse-induced-metric correction.
 v=pair(H,H);u=g*k
 B={(i,j):g*H*(k[i]*s.eye(4)[:,j]+k[j]*s.eye(4)[:,i])/2 for i,j in itertools.product(range(4),repeat=2)}
 D={(i,j):-k[i]*k[j]*H*g*H for i,j in itertools.product(range(4),repeat=2)}
 C={(i,j):s.Matrix([(k[i]*H[m,j]+k[j]*H[m,i]-k[m]*H[i,j])/2 for m in range(4)]) for i,j in itertools.product(range(4),repeat=2)}
 ii=sum(g[i,i]*g[j,j]*((B[i,j].T*g*B[i,j])[0]+2*pair(Z[i,j],D[i,j])-(0 if omit_projection else (C[i,j].T*g*C[i,j])[0])) for i,j in itertools.product(range(4),repeat=2))
 ii-=2*v*sum(u[i]*u[l]*g[j,j]*pair(Z[i,j],Z[l,j]) for i,l,j in itertools.product(range(4),repeat=3))
 bt=sum((g[i,i]*B[i,i] for i in range(4)),s.zeros(4,1));dt=sum((g[i,i]*D[i,i] for i in range(4)),s.zeros(4));ct=sum((g[i,i]*C[i,i] for i in range(4)),s.zeros(4,1));zz=sum((u[i]*u[j]*Z[i,j] for i,j in itertools.product(range(4),repeat=2)),s.zeros(4))
 hm=(bt.T*g*bt)[0]+2*pair(Ztr,dt-v*zz)-(0 if omit_projection else (ct.T*g*ct)[0])
 return s.expand(ii),s.expand(hm)
# Whole quadratic on each of three causal types, using basis and polarization sums.
ks=[s.Matrix([2,1,0,0]),s.Matrix([0,1,0,0]),s.Matrix([1,1,0,0])]
fixtures=E+[E[i]+E[j] for i,j in itertools.combinations(range(10),2)]
for ki,k in enumerate(ks):
 ok=[]
 for H in fixtures:
  w,a,d,b,c,v=invs(H,k);ii,hm=direct_gradient_phase(H,k)
  ok.append(s.simplify(ii-(2*c-5*w*d/4+w*a*a/2))==0 and s.simplify(hm-(3*w*d/2+a*b-w*a*a/2))==0)
 ck('all55_gradient_phase_polarizations_causal_type_'+str(ki),all(ok))
 print('gradient phase',ki,'55 exact polarizations PASS',flush=True)
# Different route at cos=1: literal Y inverse and density, no derivative ansatz.
fixture_H=[s.diag(1,2,3,4),E[1]+E[5],g,E[0]+2*E[6]-E[8]]
for n,(H,k) in enumerate(zip(fixture_H,[ks[0],ks[1],ks[2],s.Matrix([1,2,1,0])])):
 Y=g+eps*H;Yi=Y.inv();wy=(k.T*Yi*k)[0];ay=s.trace(Yi*H);vy=s.trace(Yi*H*Yi*H)-ay*ay/2
 ii=2+eps*(k.T*Yi*H*Yi*k)[0]+eps**2*wy**2*vy;hm=-1+eps*wy*ay+eps**2*wy**2*vy
 f=s.sqrt(-Y.det())*(ii+2*hm)/2
 coef=s.simplify(s.diff(f,eps,2).subs(eps,0)/2);w,a,d,b,c,v=invs(H,k)
 ck('direct_value_phase_'+str(n),s.simplify(coef-(-2*c-3*a*b/2-2*w*d+w*a*a+3*w*w*v)/2)==0)
 iig,hmg=direct_gradient_phase(H,k)
 ck('full_two_phase_Fourier_coefficient_'+str(n),s.simplify((coef+(iig+2*hmg)/2)/2-Q(H,k)/4)==0)
# Full10 matrix and exact determinant in a rest frame; all entries literal bilinear form.
w=s.symbols('w',real=True);krest=s.Matrix([s.sqrt(w),0,0,0]);M=matrix(krest)
ck('full_matrix_symmetric',M==M.T)
expected=w**10*(12*w-1)**8*(12*w*w-10*w+1);det=s.factor(M.det());ratio=s.cancel(det/expected)
ck('complete_determinant_identity',not ratio.has(w) and ratio!=0)
x,y=s.symbols('x y',real=True);Hs=s.diag(x,y/3,y/3,y/3);Ms=s.Matrix([[3*w/2+q(3,4),3*w/2-q(3,4)],[3*w/2-q(3,4),-w/2+q(5,12)]])
ck('scalar_block_from_full_symbol',s.expand(Q(Hs,krest)-w*(s.Matrix([[x,y]])*Ms*s.Matrix([x,y]))[0])==0)
ck('scalar_determinant',s.expand(Ms.det()+3*w*w-q(5,2)*w+q(1,4))==0)
ck('eight_component_shell_rank',M.subs(w,q(1,12)).rank()==2)
for i,root in enumerate([(5-s.sqrt(13))/12,(5+s.sqrt(13))/12]):
 Mr=M.subs(w,root).applyfunc(s.simplify);ck('scalar_shell_rank_'+str(i),Mr.rank()==9)
 Hker=3*root**2*g-s.diag(root,0,0,0);vec=s.Matrix([Hker[i,j] for i,j in pairs]);ck('explicit_scalar_kernel_'+str(i),all(s.simplify(v)==0 for v in Mr*vec))
ck('spacelike_full_rank',matrix(ks[1]).rank()==10)
ck('generic_timelike_full_rank',matrix(ks[0]).rank()==10)
ck('nonzero_null_rank_two',matrix(ks[2]).rank()==2)
ck('zero_covector_rank_zero',matrix(s.zeros(4,1))==s.zeros(10))
ct('rest_frame_zero_limit_does_not_describe_null_rank',M.subs(w,0).rank()==0 and matrix(ks[2]).rank()==2)
# Fourth-order part exact under k rescaling, with declared full graph field space.
r=s.symbols('r');principal=matrix(r*ks[0]).applyfunc(lambda x:s.expand(x).coeff(r,4));w0=(ks[0].T*g*ks[0])[0]
ck('full_matrix_principal_part',principal==3*w0**2*V)
ct('dropping_mean_term_changes_principal',3*w0**2*V!=w0**2*V)
v=s.Matrix([1,2,0,0]);Hg=ks[0]*v.T+v*ks[0].T;vg=s.Matrix([Hg[i,j] for i,j in pairs]);ct('pure_section_diffeomorphism_not_kernel',matrix(ks[0])*vg!=s.zeros(10,1))
ii1,hh1=direct_gradient_phase(fixture_H[0],ks[0]);ii2,hh2=direct_gradient_phase(fixture_H[0],ks[0],True);ct('omitting_normal_projection_changes_operator',ii1+2*hh1!=ii2+2*hh2)
ct('highest_order_alone_misses_nonnull_shell',3*q(1,12)**2*V!=M.subs(w,q(1,12)))
ct('scalar_only_test_misses_eight_dimensional_shell',Ms.subs(w,q(1,12)).det()!=0 and M.subs(w,q(1,12)).det()==0)
ct('stationary_does_not_imply_second_order',3*alpha!=0 and s.simplify((alpha+beta).subs(beta,2*alpha))==3*alpha)
ct('independent_ambient_moment_remains_nonzero',any((Z[i,j]+2*g[i,j]*Ztr)!=s.zeros(4) for i,j in pairs))
# Released static response of the actual differential operator on one conserved source.
vstatic=s.symbols('vstatic',positive=True);ksstatic=s.Matrix([0,0,0,s.sqrt(vstatic)]);Mstatic=matrix(ksstatic);den=vstatic*(12*vstatic+1)*(12*vstatic**2+10*vstatic+1)
A0=3*(8*vstatic**2+10*vstatic+1)/den;Ap=(4*vstatic+1)*(6*vstatic+1)/den;Al=(2*vstatic+1)/(vstatic*(12*vstatic**2+10*vstatic+1))
response=s.diag(A0,Ap,Ap,Al);responsevec=s.Matrix([response[i,j] for i,j in pairs]);source=s.zeros(10,1);source[0]=1
ck('full_static_inverse_on_conserved_source',all(s.cancel(x)==0 for x in Mstatic*responsevec-source))
ck('static_source_conservation',ksstatic[0]==0)
ratio_response=s.factor((A0+Ap)/A0);expected_ratio=4*(12*vstatic**2+10*vstatic+1)/(3*(8*vstatic**2+10*vstatic+1))
ck('actual_transverse_light_motion_ratio',s.cancel(ratio_response-expected_ratio)==0)
ck('actual_same_source_difference',s.cancel(Ap-A0+2*(10*vstatic+1)/den)==0)
ck('all_static_denominators_positive',den.is_positive is True)
ck('static_IR_UV_response_limits',s.limit(ratio_response,vstatic,0,dir='+')==q(4,3) and s.limit(ratio_response,vstatic,s.oo)==2)
ck('static_ratio_strictly_increasing',s.factor(s.diff(ratio_response,vstatic)).is_positive is True)
ct('GR_like_ratio_not_recovered_at_finite_static_momentum',s.factor(2-ratio_response).is_positive is True)
ct('principal_only_response_has_wrong_finite_ratio',s.cancel(ratio_response-2)!=0)
krot=s.Matrix([0,1,2,2]);vv=s.Integer(9);sp=krot[1:4,0];Tsp=Ap.subs(vstatic,vv)*(s.eye(3)-sp*sp.T/vv)+Al.subs(vstatic,vv)*sp*sp.T/vv
Hr=s.diag(A0.subs(vstatic,vv),Tsp);vr=s.Matrix([Hr[i,j] for i,j in pairs]);ck('actual_rotated_static_inverse',matrix(krot)*vr==source)
ct('discarding_longitudinal_field_breaks_full_equation',Mstatic*s.Matrix([A0 if ij==(0,0) else Ap if ij in [(1,1),(2,2)] else 0 for ij in pairs])!=source)
ck('longitudinal_difference_retained',s.cancel(Al-Ap-4*vstatic/den)==0)
mu=s.symbols('mu',real=True);angle_diff=Ap-A0+(Al-Ap)*mu**2
ck('fixed_direction_response_formula',s.cancel(angle_diff-(-20*vstatic-2+4*vstatic*mu**2)/den)==0)
ck('fixed_direction_strict_sign_bound',(-16*vstatic-2).is_negative is True)
aa=(5-s.sqrt(13))/12;bb=(5+s.sqrt(13))/12
pf=3/vstatic-q(8,3)/(vstatic+q(1,12))+(-q(1,6)-7*s.sqrt(13)/78)/(vstatic+aa)+(-q(1,6)+7*s.sqrt(13)/78)/(vstatic+bb)
ck('exact_Coulomb_Yukawa_partial_fractions',s.simplify(A0-pf)==0)
ck('positive_static_Yukawa_scales',aa>0 and bb>0)
ck('exact_transverse_light_kernel',s.cancel(A0+Ap-4*(1/vstatic-1/(vstatic+q(1,12))))==0)
rad,mass=s.symbols('rad mass',positive=True);kernel=s.exp(-mass*rad)/(4*s.pi*rad)
ck('Yukawa_radial_equation_away_from_origin',s.simplify(-s.diff(kernel,rad,2)-2*s.diff(kernel,rad)/rad+mass**2*kernel)==0)
ck('Yukawa_unit_origin_flux',s.limit(-4*s.pi*rad**2*s.diff(kernel,rad),rad,0,dir='+')==1)
ck('static_IR_local_integrability_order',s.limit(vstatic*A0,vstatic,0,dir='+')==3 and s.limit(vstatic*Ap,vstatic,0,dir='+')==1 and s.limit(vstatic*Al,vstatic,0,dir='+')==1)
ct('compact_source_need_not_have_zero_mass',s.limit(vstatic*A0,vstatic,0,dir='+')!=0)
st='k2525-metric-bundle-section-action';deps=[f'explorations/conditional-build/{st}-2026-11-02.md',str(Path(__file__).relative_to(R)),'explorations/conditional-build/k2345-curved-bundle-ricci-obstruction-2026-10-30.md','explorations/conditional-build/k2523-coupled-receiver-variation-2026-11-02.md','explorations/W136-issuance-declaration-propagation-2026-07-14.md','explorations/W130-native-graviton-oneloop-block-2026-07-14.md','explorations/conditional-build/w154-w229-k77-action-owner-qualification-2026-08-24.md']
out={'result_id':'K2525','checks':checks,'contrary_controls':controls,'evidence_kind':'written universal tensor expansion and principal-symbol argument; exact finite metric contractions, 165 polarized gradient controls, four direct value-phase controls and full matrix determinant/rank; no physical Green theorem','static_response':{'h00':str(A0),'h_perp':str(Ap),'h_parallel':str(Al),'light_motion_ratio':str(ratio_response),'h00_partial_fractions':str(pf)},'determinant_basis_constant':str(ratio),'rest_frame_full_matrix':[[str(x) for x in row] for row in M.tolist()],'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}}
f=R/f'lab/process/{st}.json'
if '--write' in sys.argv:f.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(f.read_text())==out
print(json.dumps({'result':'K2525','exact_check_groups':len(checks),'contrary_controls':len(controls)}))
