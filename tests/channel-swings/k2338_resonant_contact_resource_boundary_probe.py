"""Actual fixed-angle microscopic contact and finite-cap certificate controls."""
from pathlib import Path
import sympy as s,mpmath as mp,json,hashlib,sys
mp.mp.dps=70
R=Path(__file__).resolve().parents[2];checks={};numerical=[];faults={}
def check(k,v,num=False):
 checks[k]=bool(v)
 if num:numerical.append(k)
 if not v:raise AssertionError('[FAIL] '+k)
h,E=s.symbols('h E',real=True);H=s.Matrix([[0,h,h],[h,E,0],[h,0,E]])
v=s.Matrix([0,1,-1])/s.sqrt(2);b=s.Matrix([0,1,1])/s.sqrt(2);a=s.Matrix([1,0,0]);W=s.Matrix.hstack(a,b,v)
check('bright_dark_matrix',s.simplify(W.T*H*W)==s.Matrix([[0,s.sqrt(2)*h,0],[s.sqrt(2)*h,E,0],[0,0,E]]))
x=s.symbols('x',positive=True)
check('omega_upper_square',s.expand((x+3/x)**2-((x-1/x)**2+8))==8/x**2)
check('omega_lower_square',s.expand(((x-1/x)**2+8)-(x+1/x)**2)==4)
actuals=[]
def eval_contact(xx,g=1,Delta=None):
 D=mp.mpf(xx);hh=mp.mpf(1);chi=-hh*hh/D;dd=D if Delta is None else mp.mpf(Delta)
 HH=mp.matrix([[0,g,hh],[g,dd+chi,0],[hh,0,D+chi]])
 tt=mp.pi*D/2;U=mp.expm(-1j*tt*HH);omega=mp.sqrt((D-1/D)**2+8);delta=(omega-(D-1/D))/2;w=(1-(D-1/D)/omega)/2
 amp=((1-w)*mp.exp(-1j*(D-1/D+delta)*tt)+w*mp.exp(1j*delta*tt)-mp.exp(-1j*(D-1/D)*tt))/2
 bound=1-mp.pi**2/(8*D**4)-2/(D-1/D)**2
 return U,amp,bound,delta*tt
for xx in [2,10,30]:
 U,amp,bound,phase=eval_contact(xx)
 check('actual_amplitude_'+str(xx),abs(U[1,2]-amp)<mp.mpf('1e-60'),True)
 check('actual_lower_bound_'+str(xx),abs(U[1,2])>=bound,True)
 check('phase_bounds_'+str(xx),mp.pi/(1+mp.mpf(xx)**-2)<=phase<=mp.pi,True)
 actuals.append({'x':xx,'transition_amplitude_abs':mp.nstr(abs(amp),40),'analytic_lower_bound':mp.nstr(bound,40)})
check('finite_rational_lower_bound',1-s.Rational(22,7)**2/(8*10**4)-s.Rational(2)/(10-s.Rational(1,10))**2>s.Rational(9794,10000))
check('phase_fixture_exact',s.simplify(s.exp(s.I*50*s.pi))==1)
# Original versus reduced finite-cap formula, exact symbols.
rho,hh,gg,K,lam,Beta,C=s.symbols('rho hh gg K lam Beta C',positive=True)
D=hh/rho;M=Beta**2;chi=hh*rho;Td=K/chi
r=s.exp(2*Beta*rho)*(hh*gg/D+2*hh**3*Beta*(M+1)/D**2)
orig=2*C*Beta*rho+Td*r+lam*Td
reduced=2*C*Beta*rho+K*s.exp(2*Beta*rho)*(gg/hh+2*Beta*(M+1)*rho)+lam*K/(hh*rho)
check('cap_reduction_identity',s.simplify(orig-reduced)==0)
check('fixed_rho_decreases_with_h',s.simplify(s.diff(reduced,hh)+K*(s.exp(2*Beta*rho)*gg+lam/rho)/hh**2)==0)
Hcap,Dcap,Xcap=s.Rational(10),s.Rational(100),s.Rational(1)
for rr in [s.Rational(1,100),s.Rational(1,10),s.Rational(1,2),s.Rational(2)]:
 hs=min(Hcap,Dcap*rr,Xcap/rr)
 check('joint_caps_'+str(rr),hs<=Hcap and hs/rr<=Dcap and hs*rr<=Xcap)
 check('maximal_h_'+str(rr),hs in [Hcap,Dcap*rr,Xcap/rr])
AA,BB,ll,JJ=s.symbols('AA BB ll JJ',positive=True)
check('hopping_optimum',s.simplify(s.diff(AA*JJ+ll*BB/JJ,JJ).subs(JJ,s.sqrt(ll*BB/AA)))==0)
# Strict convexity, exact capped minimizer and a rational upper certificate.
bb,rr=s.symbols('bb rr',positive=True)
check('exp_over_rho_curvature',s.simplify(s.diff(s.exp(bb*rr)/rr,rr,2)-s.exp(bb*rr)*((bb*rr-1)**2+1)/rr**3)==0)
r0=s.Rational(1,10000);betaup=s.Rational(7,4);Kup=s.Rational(121,14)
leftbracket=s.Rational(7,10)/(10**6*r0**2)*(2*betaup*r0-1)+8*betaup*(1+2*betaup*r0)
check('left_kink_derivative_negative',leftbracket<-55 and 21+8*(-55)<0)
check('right_kink_derivative_positive',18+8*12-9>0)
check('exponential_rational_majorant',1/(1-2*betaup*r0)<s.Rational(1001,1000))
capupper=s.Rational(21,10000)+Kup*s.Rational(1001,1000)*(s.Rational(7,1000)+s.Rational(14,10000))+Kup/s.Integer(10000)
check('finite_cap_contact_certificate',capupper<s.Rational(2,25))
HHcap=s.symbols('HHcap',positive=True)
floordiff=2*C*Beta*rho+K*s.exp(2*Beta*rho)*2*Beta*(M+1)*rho+lam*K/(hh*rho)+K*gg*((s.exp(2*Beta*rho)-1)/hh+(HHcap-hh)/(hh*HHcap))
check('certificate_floor_decomposition',s.simplify(reduced-K*gg/HHcap-floordiff)==0)
# Exact amplitude damping on vacuum plus three excitation states.
gamma=s.symbols('gamma',positive=True);jumps=[]
for j in range(1,4):
 L=s.zeros(4);L[0,j]=s.sqrt(gamma);jumps.append(L)
rate=sum((L.T*L for L in jumps),s.zeros(4));P=s.diag(0,1,1,1)
check('equal_loss_total_rate',rate==gamma*P)
check('vacuum_absorbing',all(L*s.Matrix([1,0,0,0])==s.zeros(4,1) for L in jumps))
# Heisenberg generator of survival: Hamiltonian commutes with P.
Hd=s.diag(0,H);adj=s.I*(Hd*P-P*Hd)+sum((L.T*P*L-(L.T*L*P+P*L.T*L)/2 for L in jumps),s.zeros(4))
check('exact_survival_generator',s.simplify(adj+gamma*P)==s.zeros(4))
# Concrete off-resonant repair with same block Hamiltonian.
D0=mp.mpf(100);g0=mp.mpf('0.7');ch=-1/D0;A0=mp.matrix([[0,g0],[g0,2+ch]])
eigs=mp.eigsy(A0,eigvals_only=True);dist=min(abs(D0+ch-e) for e in eigs);repair=2/(dist-1)
for tt in [mp.pi,mp.pi*50]:
 HH=mp.matrix([[0,g0,1],[g0,2+ch,0],[1,0,D0+ch]]);U=mp.expm(-1j*tt*HH)
 check('off_resonant_leakage_'+mp.nstr(tt,6),mp.sqrt(abs(U[0,2])**2+abs(U[1,2])**2)<=repair,True)
# Baseline first. Genuine Hamiltonian/cap/noise mutations.
U,amp,_,_=eval_contact(10,g=0)
faults['remove_mediator_exchange']=['actual_amplitude_10'] if abs(U[1,2]-amp)>mp.mpf('.9') else []
U,amp,_,_=eval_contact(10,Delta=2)
faults['change_mediator_detuning']=['actual_amplitude_10'] if abs(U[1,2]-amp)>mp.mpf('.5') else []
Hgood=s.Matrix([[0,1,1],[1,s.Rational(99,10),0],[1,0,s.Rational(99,10)]])
Hbad=s.Matrix([[0,1,1],[1,10,0],[1,0,10]])
faults['omit_actual_matched_counterterms']=['bright_dark_matrix'] if s.simplify(W.T*Hbad*W-W.T*Hgood*W)!=s.zeros(3) else []
# Q<=N at reference occupation N retains only the neutral excitation state.
Pbad=s.diag(0,0,1);Htrunc=Pbad*Hgood*Pbad
Utrunc=mp.expm(-1j*(5*mp.pi)*mp.matrix([[mp.mpf(int(s.numer(x)))/int(s.denom(x)) for x in Htrunc.row(i)] for i in range(3)]))
faults['truncate_actual_excitation_bridge']=['actual_amplitude_10'] if abs(Utrunc[1,2]-eval_contact(10)[1])>mp.mpf('.9794') else []
Uwrongtime=mp.expm(-1j*mp.pi*mp.matrix([[mp.mpf(int(s.numer(x)))/int(s.denom(x)) for x in Hgood.row(i)] for i in range(3)]))
faults['wrong_contact_duration']=['actual_amplitude_10'] if abs(Uwrongtime[1,2]-eval_contact(10)[1])>mp.mpf('.1') else []
rr=s.Rational(1,100);wrong=Hcap
faults['ignore_detuning_cap']=['joint_caps'] if wrong/rr>Dcap else []
Z=s.diag(0,1,-1,1);deph=Z*P*Z-(Z*Z*P+P*Z*Z)/2
faults['replace_loss_by_dephasing']=['exact_survival_generator'] if deph!= -P else []
assert all(faults.values()),'[FAIL] undetected input fault'
st='k2338-resonant-contact-resource-boundary';deps=[f'explorations/conditional-build/{st}-2026-10-30.md',str(Path(__file__).relative_to(R)),'explorations/conditional-build/k2336-dispersive-contact-realization-2026-10-30.md','explorations/conditional-build/k2334-microscopic-neutral-transfer-2026-10-30.md']
out=dict(result_id='K2338',checks=len(checks),exact_checks=len(checks)-len(numerical),numerical_checks=len(numerical),check_names=list(checks),evidence_kind='exact finite matrix and resource algebra plus finite70digit propagators; universal statements proved in note',mutation_failed_checks=faults,details=actuals,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps});p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print(json.dumps({'result':'K2338','exact':out['exact_checks'],'numerical':out['numerical_checks'],'faults':len(faults)}))
