"""Exact two-stage cancellation and rigorous complete-sector echo comparison."""
import sympy as sy
from flint import arb,acb,acb_mat,ctx
ctx.prec=256
from pathlib import Path
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def finish(st,details,evidence,deps):
 deps=[f'explorations/conditional-build/{st}-2026-10-30.md',str(Path(__file__).relative_to(R))]+deps
 out=dict(result_id=st.split('-')[0].upper(),checks=len(checks),check_names=list(checks),evidence_kind=evidence,mutation_failed_checks=faults,details=details,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
 assert faults and all(faults.values())
 p=R/f'lab/process/{st}.json'
 if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps({'result':out['result_id'],'checks':len(checks),'faults':len(faults)}))
I=acb(0,1);pi=arb.pi();J=arb(1)/10**6
basis=[(p,r,e,f) for p in range(3) for r in range(3) for e in range(2) for f in range(2) if p+r+e+f<=2];dim=len(basis);idx={v:k for k,v in enumerate(basis)}
check('complete_excitation_sector',dim==13)
def diagonal(vals):
 M=acb_mat(dim,dim)
 for k,v in enumerate(vals):M[k,k]=v
 return M
L=diagonal([p+e for p,r,e,f in basis]);Pf=diagonal([f for p,r,e,f in basis]);LZ=diagonal([(p+e)*(1-2*f) for p,r,e,f in basis]);C=diagonal([e*(1-2*f)+f for p,r,e,f in basis])
B=acb_mat(dim,dim);Xe=acb_mat(dim,dim);Xf=acb_mat(dim,dim)
for j,(p,r,e,f) in enumerate(basis):
 if p:
  B[idx[(p-1,r+1,e,f)],j]=arb(p*(r+1)).sqrt()
  if not e:
   k=idx[(p-1,r,1,f)];Xe[k,j]=Xe[j,k]=arb(p).sqrt()
  if not f:
   k=idx[(p-1,r,e,1)];Xf[k,j]=Xf[j,k]=arb(p).sqrt()
comm=L*B-B*L+B
check('tone_commutator',all(comm[i,j].contains(0) and comm[i,j].abs_upper()<arb('1e-60') for i in range(dim) for j in range(dim)))
def probability(w,flag):return sum((w[k,0].real**2+w[k,0].imag**2 for k,z in enumerate(basis) if z[3]==flag),arb(0))
def run(D,phase_duration=arb(0),kind='micro',Delta=arb(10)):
 H0=diagonal([Delta*e for p,r,e,f in basis])+Xe;root=(Delta*Delta+4).sqrt();c=((1+Delta/root)/2).sqrt();ss=((1-Delta/root)/2).sqrt();omega=(Delta-root)/2;u=J/c;td=pi*D/2;tau=pi/(4*J)
 psi=acb_mat(dim,1);psi[idx[(1,0,0,1)],0]=c;psi[idx[(0,0,1,1)],0]=-ss
 def phase(a):return diagonal([(I*a*(p+e)).exp() for p,r,e,f in basis])
 def contact(ds):
  if kind=='ideal':V=((-I*td)*(H0-LZ/ds)).exp()
  else:
   H=H0+ds*Pf+Xf-(0 if kind=='no_compensator' else (-1 if kind=='reverse_compensator' else 1))*C/ds
   V=(diagonal([acb(1) for z in basis]) if kind=='omit_first_phase' and ds>0 else diagonal([(I*ds*td*f).exp() for p,r,e,f in basis]))*((-I*td)*H).exp()
  return ((-I*phase_duration)*H0).exp()*V
 def pulse(start,ep):
  H=H0-omega*L+u*ep*B+u*ep.conjugate()*B.transpose()
  return phase(-omega*(start+tau))*((-I*tau)*H).exp()*phase(omega*start)
 W=pulse(2*(td+phase_duration)+tau,I)*contact(-D)*pulse(td+phase_duration,acb(-1))*contact(D)
 return W,psi

# Exact symbolic commutators on the same conserved basis, independent of ball exponentials.
q=sy.Rational;de,ds=sy.symbols('Delta Ds',nonzero=True)
def smat(vals):return sy.diag(*vals)
sPf=smat([f for p,r,e,f in basis]);sPe=smat([e for p,r,e,f in basis]);sLZ=smat([(p+e)*(1-2*f) for p,r,e,f in basis]);sC=smat([e*(1-2*f)+f for p,r,e,f in basis]);AE=sy.zeros(dim);AF=sy.zeros(dim);Y=sy.zeros(dim)
for j,(p,r,e,f) in enumerate(basis):
 if p and not e:AE[idx[p-1,r,1,f],j]=sy.sqrt(p)
 if p and not f:AF[idx[p-1,r,e,1],j]=sy.sqrt(p)
 if e and not f:Y[idx[p,r,0,1],j]=1
comm=lambda A,B:A*B-B*A
S=(AF-AF.T)/ds;X=AF+AF.T;K1=(Y+Y.T)/ds;TT=(Y-Y.T)/(ds*(ds-de));H0=de*sPe+AE+AE.T
check('first_fast_cancellation',sy.simplify(comm(S,ds*sPf)+X)==sy.zeros(dim))
check('exact_matching_compensator',sy.simplify(comm(S,X)/2-sC/ds+sLZ/ds)==sy.zeros(dim))
check('mediator_exchange_residual',sy.simplify(comm(S,H0)-K1)==sy.zeros(dim))
check('second_signed_cancellation',sy.simplify(comm(TT,ds*sPf+de*sPe)+K1)==sy.zeros(dim))
# Conservative exact upper bounds for both D signs; actual D=10000.5 only improves these.
sb=q(99,700000);vb=q(99,70);kb=cb=q(1,10000);qb=q(1,10000*9990);ab=q(99,70)+q(2,10000)
check('exponential_majorant',1/(1-2*sb)<q(1001,1000))
bb=2*vb*sb**2*q(1001,1000)+sb*kb+2*sb*cb
# use actual duration upper pi*D/2 with D=20001/2; denominators use lower D10000
r2=bb+qb*kb+2*qb*ab;tdub=q(22,7)*q(20001,2)/2;bound=2*(2*(sb+qb)+tdub*r2)
check('uniform_two_contact_bound',bound<q(1,200))
timeub=2*tdub+2*q(22,7)*10**6/4+q(2,100)
check('priced_noise_budget',bound+timeub/q(10**10)<q(1,100))
def frob2(A):return sum((A[i,j].real**2+A[i,j].imag**2 for i in range(A.nrows()) for j in range(A.ncols())),arb(0))
D=arb(20001)/2;delta=arb(1)/100
W,psi=run(D,delta);V,_=run(D,delta,kind='ideal');diff=W-V;f2=frob2(diff)
check('full13_coherent_interval_error',f2<arb('0.000025'))
# encoded vacuum-reference n0 branch plus lower-dressed n1 branch; spectator labels orthogonal.
zero=acb_mat(dim,1);zero[idx[(0,1,0,0)],0]=1
encoded=frob2(diff*zero)+frob2(diff*psi)
check('both_encoded_sectors_phase_sensitive',encoded<arb('0.000025'))
identity=acb_mat(dim,dim)
for i in range(dim):identity[i,i]=1
unit=W.conjugate().transpose()*W-identity
check('unitarity_enclosure',all(unit[i,j].contains(0) for i in range(dim) for j in range(dim)))
errors={}
for kind in ['no_compensator','reverse_compensator','omit_first_phase']:
 badW,_=run(D,delta,kind=kind);err=frob2(badW-V);errors[kind]=str(err)
 faults[kind]=['full13_coherent_interval_error'] if err>arb('0.000025') else []
Wr,_=run(arb(10),delta,Delta=arb(10));Vr,_=run(arb(10),delta,kind='ideal',Delta=arb(10));er=frob2(Wr-Vr)
faults['restore_resonance']=['full13_coherent_interval_error'] if er>arb('0.000025') else []
finish('k2344-signed-detuning-echo-repair',{'precision_bits':ctx.prec,'dimension':dim,'D':'20001/2','Delta':10,'phase_duration':'1/100','two_contact_bound':str(bound),'duration_upper':str(timeub),'noise_combined_upper':str(bound+timeub/q(10**10)),'full_frobenius_squared':str(f2),'encoded_error_squared':str(encoded),'fault_error_squared':errors,'resonant_error_squared':str(er)},'exact symbolic commutators/rational bounds and256bit Arb full13 matrices; uniform time-sensitive proof in note',['explorations/conditional-build/k2336-dispersive-contact-realization-2026-10-30.md','explorations/conditional-build/k2341-reachable-microscopic-echo-2026-10-30.md'])
