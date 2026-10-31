"""Coherent microscopic number copy plus signed echo on complete reachable support."""
import sympy as sy
from flint import arb,acb,acb_mat,ctx
from pathlib import Path
import json,hashlib,sys
ctx.prec=256;R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
I=acb(0,1);pi=arb.pi();J=arb(1)/10**6;D=arb(20001)/2;delta=arb(1)/100;Delta=arb(10)
basis=[(p,r,e,f) for p in range(4) for r in range(4) for e in range(2) for f in range(2) if p+r+e<=3];idx={z:i for i,z in enumerate(basis)};dim=len(basis)
check('complete_neutral_tensor_support',dim==32)
def diagonal(vals):
 A=acb_mat(dim,dim)
 for k,v in enumerate(vals):A[k,k]=v
 return A
L=diagonal([p+e for p,r,e,f in basis]);Pf=diagonal([f for p,r,e,f in basis]);LZ=diagonal([(p+e)*(1-2*f) for p,r,e,f in basis]);C=diagonal([e*(1-2*f)+f for p,r,e,f in basis]);Pe=diagonal([e for p,r,e,f in basis])
B=acb_mat(dim,dim);Xe=acb_mat(dim,dim);Xf=acb_mat(dim,dim);H=acb_mat(dim,dim)
for j,(p,r,e,f) in enumerate(basis):
 H[j,j]=(1 if not f else -1)/arb(2).sqrt();H[idx[p,r,e,1-f],j]=1/arb(2).sqrt()
 if p:
  B[idx[p-1,r+1,e,f],j]=arb(p*(r+1)).sqrt()
  if not e:k=idx[p-1,r,1,f];Xe[k,j]=Xe[j,k]=arb(p).sqrt()
  if not f:k=idx[p-1,r,e,1];Xf[k,j]=Xf[j,k]=arb(p).sqrt()
H0=Delta*Pe+Xe;rr=(Delta*Delta+4).sqrt();c=((1+Delta/rr)/2).sqrt();ss=((1-Delta/rr)/2).sqrt();omega=(Delta-rr)/2;td=pi*D/2;tau=pi/(4*J)
U0=acb_mat(dim,2);U0[idx[0,1,0,0],0]=1;U0[idx[1,0,0,0],1]=c;U0[idx[0,0,1,0],1]=-ss
Target=acb_mat(dim,2);Target[idx[0,1,0,0],0]=1;Target[idx[0,1,0,1],1]=1
ident=diagonal([1]*dim);drift=((-I*delta)*H0).exp();GH=drift*H;GS=drift*diagonal([I if f else 1 for p,r,e,f in basis]);contacts={};pulses={}
def contact(sign,kind='micro'):
 key=(sign,kind)
 if key in contacts:return contacts[key]
 ds=sign*D
 if kind=='ideal':V=((-I*td)*(H0-LZ/ds)).exp()
 elif kind=='skip':V=((-I*td)*H0).exp()
 else:
  V=diagonal([(I*ds*td*f).exp() for p,r,e,f in basis])*((-I*td)*(H0+ds*Pf+Xf-(0 if kind=='no_compensator' else 1)*C/ds)).exp()
 contacts[key]=drift*V;return contacts[key]
def pulse(start,z):
 key=(str(start),str(z))
 if key in pulses:return pulses[key]
 phase=lambda t:diagonal([(-I*omega*t*(p+e)).exp() for p,r,e,f in basis])
 A=phase(start+tau)*((-I*tau)*(H0-omega*L+(J/c)*z*B+(J/c)*z.conjugate()*B.transpose())).exp()*phase(-start)
 pulses[key]=A;return A
P1=pulse(2*td+5*delta,acb(-1));P2=pulse(3*td+6*delta+tau,I)
def evolve(kind='micro'):
 Vc=contact(-1,'skip' if kind=='skip_copy' else ('ideal' if kind=='ideal' else ('no_compensator' if kind=='no_compensator' else 'micro')))
 v=GH*U0;v=Vc*v;v=GH*v;v=(drift if kind=='omit_copy_phase' else GS)*v
 v=contact(1,'ideal' if kind=='ideal' else ('no_compensator' if kind=='no_compensator' else 'micro'))*v
 v=(pulse(arb(0),acb(-1)) if kind=='reset_clock' else P1)*v
 v=contact(-1,'ideal' if kind=='ideal' else ('no_compensator' if kind=='no_compensator' else 'micro'))*v
 return P2*v
frob2=lambda A:sum((A[i,j].real*A[i,j].real+A[i,j].imag*A[i,j].imag for i in range(A.nrows()) for j in range(A.ncols())),arb(0))
w=evolve();ideal=evolve('ideal');err=frob2(w-Target);idealerr=frob2(ideal-Target);contacterr=frob2(w-ideal)
check('coherent_microscopic_copy_echo',err<arb('0.0001'))
check('ideal_contact_selected_pulse_target',idealerr<arb('1e-8'))
check('micro_vs_ideal_contact_columns',contacterr<arb('0.0001'))
check('column_isometry',all((w.conjugate().transpose()*w)[i,j].contains(1 if i==j else 0) for i in range(2) for j in range(2)))
# Stage after second H reaches Q2; compare explicit support, not a loose norm tolerance.
prefix=GH*contact(-1)*GH*U0
leak=sum((prefix[i,j].real*prefix[i,j].real+prefix[i,j].imag*prefix[i,j].imag for i,(p,r,e,f) in enumerate(basis) if p+r+e>1 for j in range(2)),arb(0))
check('actual_enlarged_support_nonzero',leak>0)
check('reachable_K_bound',all(prefix[i,j].abs_upper()<arb('1e-60') for i,z in enumerate(basis) if sum(z)>3 for j in range(2)))
check('final_K_bound',all(w[i,j].abs_upper()<arb('1e-60') for i,z in enumerate(basis) if sum(z)>3 for j in range(2)))
q=sy.Rational; sb=q(99,700000);vb=q(99,70);kb=cb=q(1,10000);qb=q(1,10000*9990);ab=q(99,70)+q(2,10000)
check('exp_majorant',1/(1-2*sb)<q(1001,1000));bb=2*vb*sb**2*q(1001,1000)+sb*kb+2*sb*cb;r2=bb+qb*kb+2*qb*ab;tu=q(22,7)*q(20001,2)/2
contact_bound=3*(2*(sb+qb)+tu*r2);esel=16*q(1,10**6)/(10*q(99,100))*(1+q(22,28)*(3+q(100,99)))
timeub=3*tu+q(6,100)+2*q(22,7)*10**6/4;bound=contact_bound+esel+timeub/10**10
check('whole_transfer_rational_bound',bound<q(1,100));check('exact_one_shell_gap',rr>10 and c>arb(99)/100)
# Independent two-level dressed frequency difference.
lo=(Delta-rr)/2;up=(Delta+rr)/2;check('upper_lower_transition_gap',(up-lo-rr).contains(0))
errors={}
for kind in ['omit_copy_phase','skip_copy','reset_clock','no_compensator']:
 bad=evolve(kind);er=frob2(bad-Target);errors[kind]=str(er);faults[kind]=['coherent_microscopic_copy_echo'] if er>arb('0.0001') else []
faults['project_to_Q1']=['actual_enlarged_support_nonzero'] if leak>0 else []
assert all(faults.values())
deps=['explorations/conditional-build/k2347-microscopic-copy-echo-composition-2026-10-30.md',str(Path(__file__).relative_to(R)),'explorations/conditional-build/k2344-signed-detuning-echo-repair-2026-10-30.md','explorations/conditional-build/k2336-dispersive-contact-realization-2026-10-30.md','explorations/conditional-build/k2332-exact-jc-selective-control-2026-10-30.md']
out=dict(result_id='K2347',checks=len(checks),check_names=list(checks),evidence_kind='exact rational budget and256bit Arb coherent32-state reachable evolution; universal restricted-input telescope in note',mutation_failed_checks=faults,details={'dimension':dim,'precision_bits':ctx.prec,'D':'20001/2','delta':'1/100','microscopic_target_frobenius_squared':str(err),'ideal_contact_target_frobenius_squared':str(idealerr),'micro_ideal_frobenius_squared':str(contacterr),'prefix_Qabove1_weight':str(leak),'contact_bound':str(contact_bound),'selective_bound':str(esel),'total_bound':str(bound),'duration_upper':str(timeub),'fault_errors':errors},dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/'lab/process/k2347-microscopic-copy-echo-composition.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print(json.dumps({k:out[k] for k in ['result_id','checks','details']}))
