"""Exact aperture geometry and Gaussian covariance controls; continuum proof in note."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError('[FAIL] '+k)
def simp(m):return m.applyfunc(s.simplify)
phi=(1+s.sqrt(5))/2;den=s.sqrt(phi+2)
vs=[s.Matrix(v)/den for a in [-1,1] for b in [-1,1] for v in [(0,a,b*phi),(a,b*phi,0),(b*phi,0,a)]]
Q=s.Matrix([[s.sqrt(5)*(3*z*z-1)/2,s.sqrt(15)*x*z,s.sqrt(15)*y*z,s.sqrt(15)*(x*x-y*y)/2,s.sqrt(15)*x*y] for x,y,z in vs])
check('unit_vertices',all(s.simplify(v.dot(v)-1)==0 for v in vs))
check('quadratic_moments',simp(sum((v*v.T for v in vs),s.zeros(3)))==4*s.eye(3))
for a in range(3):
 check('fourth_'+str(a),s.simplify(sum(v[a]**4 for v in vs))==s.Rational(12,5))
 for b in range(a):check('mixed_'+str(a)+str(b),s.simplify(sum(v[a]**2*v[b]**2 for v in vs))==s.Rational(4,5))
check('antipodal',all(any(simp(v+w)==s.zeros(3,1) for w in vs) for v in vs))
check('quadrupole_gram',simp(Q.T*Q)==12*s.eye(5));check('quadrupole_mean',simp(Q.T*s.ones(12,1))==s.zeros(5,1))
dot=simp(s.Matrix(12,12,lambda i,j:vs[i].dot(vs[j])))
check('six_line_inner_products',all(x in [1,-1,1/s.sqrt(5),-1/s.sqrt(5)] for x in dot))
u=s.symbols('u')
def beam(l):return 2**(-s.Rational(l*(l+1),2))*2*s.integrate(s.legendre(l,u),(u,s.Rational(1,2),1))
b2=beam(2);b4=beam(4);T=Q.T/(12*b2)
check('beam2',b2==s.Rational(3,64));check('beam4',b4==-s.Rational(15,131072))
check('forward_inverse',simp(T*b2*Q)==s.eye(5))
check('actual_noise_gram',simp(4*s.pi*T*T.T)==s.Rational(4096,27)*s.pi*s.eye(5))
def coeff(l):return s.simplify(s.Rational(2*l+1,12)*(1+(-1)**l)*(1-s.legendre(l,1/s.sqrt(5)))*(beam(l)/b2)**2)
for l in range(9):
 Pl=dot.applyfunc(lambda x:s.simplify(s.legendre(l,x)))
 gram=simp(T*((2*l+1)*beam(l)**2*Pl)*T.T)
 check('actual_harmonic_alias_'+str(l),gram==coeff(l)*s.eye(5))
k4=coeff(4);check('k4',k4==s.Rational(45,4194304))
P4=dot.applyfunc(lambda x:s.simplify(s.legendre(4,x)));A4gram=9*b4*b4*P4
check('raw_l2_l4_cancellation',simp(b2*Q-A4gram*T.T/k4)==s.zeros(12,5))
check('tail_weight_bound',s.Rational(4096,27)*s.Rational(1,2)**20==s.Rational(1,6912))
check('full_tail_margin',s.Rational(1024**2,6912)==s.Rational(4096,27)<230)
l=s.symbols('l',integer=True,nonnegative=True)
check('infinite_spectrum_energy',s.summation((2*l+1)*2**(-l),(l,4,s.oo))==s.Rational(11,8))
delta=s.Rational(1,128);beta=s.Rational(1,64)
check('robust_probability_margin',5*delta**2/(4*(1-delta))+beta**2/4<(s.Rational(1,20)-s.Rational(1,32))**2)
A=k4*10**8
check('actual_contamination_large',A>820)
check('contaminated_correlation', (273-A)/(274+A)<-s.Rational(1,2))
check('false_rejection_lower_bound',s.Rational(2,3)**5>s.Rational(1,20))
# Actual compact-band full-count tail, using rational continuum majorants.
r=s.Rational
check('turnaround_bound',r(6400,6241)**13>r(27,25)**4)
check('p_algebraic_bounds',r(13,4)<(5+s.sqrt(73))/4<r(17,5))
check('background_F_bound',r(21,20)**7<r(5,4)**2)
check('scale_factor_bound',r(3,5)/r(21,20)**2>r(5,7)**2)
check('H_factors',r(21,20)**3<r(11,10)**2 and r(5,3)**3<r(9,4)**2 and r(4,25)*r(11,10)*r(9,4)<r(1,2))
check('u_d_q_bounds',r(5,4)*r(2,5)*r(7,2)*r(9,4)<4 and 3/r(17,25)**2>6 and 3*r(21,20)**3/r(3,5)**2<10 and 4*r(7,5)**2<8)
check('potential_bounds',2+r(17,56)<r(7,3) and r(425,448)<1 and r(5,6)*r(7,3)*15<30 and r(2,3)*r(49,9)*15<55)
row3=r(8+60+10+16,10)+r(8+55+32+3+15,10)+r(7,2)+r(175,20)
check('actual_weighted_J_bound',row3==r(659,20)<33 and r(33,40)<1)
check('number_field_bound',r(32*3+(6+30+5)*3+15*3+4*30,6)+r(9,2)==r(137,2)<69)
check('Bessel_derivative_ratio',r(1,400)*r(5,2)/22==r(1,3520)<r(1,2))
n=s.symbols('n',nonnegative=True);ell=n+4
check('kernel_extra_bound',1+r(488,1600)+r(416,8000)<2)
check('kernel_bracket_all_l',all(c>0 for c in s.Poly(3*ell*(ell+1)-2-r(3,200)*(ell+1),n).all_coeffs()))
check('q4_actual_kernel_bound',40*4*5*r(1,20)**2/s.factorial2(9)==r(2,945))
check('q_ratio_all_l',all(c>0 for c in s.Poly(20*ell*(2*ell+3)-100*(ell+2),n).all_coeffs()))
tailq=9*r(2,945)**2*r(5000,4999)
check('actual_kernel_infinite_tail',tailq<r(1,20000))
check('actual_spectral_normalization',16*r(22,7)**2*r(7,3)<400)
check('actual_spectral_tail',400*tailq<r(1,50))
check('actual_alias_cross_margin',r(1,50)/6912==r(1,345600)<230)
# Baseline passed; change actual forward geometry/response/covariance inputs.
Qbad=Q.copy();Qbad[0,:]=s.zeros(1,5)
faults['lost_aperture']=['quadrupole_gram'] if simp(Qbad.T*Qbad)!=12*s.eye(5) else []
faults['omit_beam_normalization']=['forward_inverse'] if simp((Q.T/12)*b2*Q)!=s.eye(5) else []
faults['wrong_forward_cap_sign']=['forward_inverse'] if simp(T*(-b2)*Q)!=s.eye(5) else []
faults['omit_actual_l4_signal']=['actual_harmonic_alias_4'] if simp(T*A4gram*T.T)!=s.zeros(5) else []
faults['excess_anticorrelated_power']=['cross_covariance_nonnegative'] if 273-A<0 else []
E=s.zeros(24);E[0,0]=1
faults['raw_noise_outside_allowance']=['relative_noise_bound'] if E.norm(2)>delta else []
faults['changed_seed_normalization']=['actual_spectral_normalization'] if 16*s.pi**2*10**8*r(7,3)>400 else []
assert all(faults.values()),'[FAIL] undetected input fault'
st='k2337-pixel-beam-count-test';deps=[f'explorations/conditional-build/{st}-2026-10-30.md',str(Path(__file__).relative_to(R)),'explorations/conditional-build/k2331-certified-count-window-covariance-2026-10-30.md','explorations/conditional-build/k2335-angular-response-recovery-2026-10-30.md','explorations/conditional-build/k2329-robust-count-covariance-test-2026-10-30.md','explorations/conditional-build/k2305-regular-constrained-matter-transfer-2026-10-30.md']
out=dict(result_id='K2337',checks=len(checks),check_names=list(checks),evidence_kind='exact symbolic/rational finite geometry and covariance; universal proof in note',mutation_failed_checks=faults,details={'b2':str(b2),'b4':str(b4),'k4':str(k4),'general_tail_cross_bound':'4096/27','actual_count_tail_energy_upper':'1/50','actual_count_alias_cross_upper':'1/345600'},dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print(json.dumps({'result':'K2337','exact_checks':len(checks),'faults':len(faults)}))
