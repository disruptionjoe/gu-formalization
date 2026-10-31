"""Rigorous acb full eight-state echo, absolute-clock phases and reachable input."""
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
basis=[(p,r,e,f) for p in range(3) for r in range(3) for e in range(2) for f in range(2) if p+r+e+f==2];dim=len(basis);idx={v:k for k,v in enumerate(basis)}
check('complete_excitation_sector',dim==8)
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
def run(D,phase_duration=arb(0),kind='micro',truncate=False):
 Delta=D;H0=diagonal([Delta*e for p,r,e,f in basis])+Xe;root=(D*D+4).sqrt();c=((1+D/root)/2).sqrt();ss=((1-D/root)/2).sqrt();omega=(D-root)/2;u=J/c;td=pi*D/2;tau=pi/(4*J)
 psi=acb_mat(dim,1);psi[idx[(1,0,0,1)],0]=c;psi[idx[(0,0,1,1)],0]=-ss
 def phase(a):return diagonal([(I*a*(p+e)).exp() for p,r,e,f in basis])
 def contact(ds):
  if kind=='ideal':V=((-I*td)*(H0-LZ/ds)).exp()
  else:
   H=H0+ds*Pf+(Xf if kind!='no_exchange' else acb_mat(dim,dim))-C/ds
   if truncate:
    Q=diagonal([int(p+r+e<=1) for p,r,e,f in basis]);H=Q*H*Q
   V=diagonal([(I*ds*td*f).exp() for p,r,e,f in basis])*((-I*td)*H).exp()
  return ((-I*phase_duration)*H0).exp()*V
 def pulse(start,ep):
  H=H0-omega*L+u*ep*B+u*ep.conjugate()*B.transpose()
  return phase(-omega*(start+tau))*((-I*tau)*H).exp()*phase(omega*start)
 w=contact(D)*psi;first=probability(w,0);w=pulse(td+phase_duration,acb(-1))*w;w=contact(-D)*w;w=pulse(2*(td+phase_duration)+tau,I)*w
 return probability(w,0),first,probability(w,0)+probability(w,1),w
p,first,norm,w=run(arb(10));check('certified_full_echo_failure',p>arb('0.98710') and p<arb('0.98711'));check('norm_encloses_one',norm.contains(1));check('first_contact_failure',first>arb('.98'))
pi0,_,ni,wi=run(arb(10),kind='ideal');check('ideal_contact_flag_preserved',pi0.abs_upper()<arb('1e-50'));park=wi[idx[(0,1,0,1)],0];parkprob=park.real**2+park.imag**2;check('ideal_full_echo_parking',parkprob>arb('.999'))
pn,_,_,_=run(arb(10),kind='no_exchange');check('removed_exchange_flag_preserved',pn.abs_upper()<arb('1e-50'))
pt,_,_,_=run(arb(10),truncate=True);check('bad_truncation_erases_leak',pt.abs_upper()<arb('1e-50'))
pd,_,nd,_=run(arb(10),phase_duration=arb(1)/100);check('finite_phase_duration_failure',pd>arb('.98') and nd.contains(1))
pnon,_,nn,_=run(arb(101)/10);check('noninteger_counterphase_failure',pnon>arb('.98') and nn.contains(1))
# Perturb physical Hamiltonians BEFORE acceptance. These are counterexample-mechanism faults, not alternative device claims.
faults['replace_with_ideal_matched_contacts']=['certified_full_echo_failure'] if pi0.abs_upper()<arb('.01') else []
faults['remove_actual_neutral_exchange']=['certified_full_echo_failure'] if pn.abs_upper()<arb('.01') else []
faults['truncate_reachable_intermediates']=['certified_full_echo_failure'] if pt.abs_upper()<arb('.01') else []
finish('k2341-reachable-microscopic-echo',{'precision_bits':ctx.prec,'basis':[list(state) for state in basis],'wrong_flag_probability':str(p),'first_contact_wrong_flag':str(first),'ideal_parking_probability':str(parkprob),'finite_phase_duration_wrong_flag':str(pd),'noninteger_D_wrong_flag':str(pnon)},'rigorous256bit Arb complex-ball matrix exponentials and event bounds; complete finite conserved carrier',['explorations/conditional-build/k2334-microscopic-neutral-transfer-2026-10-30.md','explorations/conditional-build/k2336-dispersive-contact-realization-2026-10-30.md','explorations/conditional-build/k2338-resonant-contact-resource-boundary-2026-10-30.md'])
