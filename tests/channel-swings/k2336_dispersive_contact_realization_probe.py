#!/usr/bin/env python3
"""Finite exact/numerical controls for the analytic K2336 contact theorem."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
import mpmath as mp
R=Path(__file__).resolve().parents[2];ST='k2336-dispersive-contact-realization'
def comm(A,B):return A*B-B*A
def matrices(N,truncate=False):
 M=N+1;states=[(n,r,e,f) for n in range(M+1) for r in range(M+1) for e in (0,1) for f in (0,1) if n+r+e+f<=M and (not truncate or n+r+e<=N)]
 ix={x:i for i,x in enumerate(states)};d=len(states)
 n=s.diag(*[x[0] for x in states]);nr=s.diag(*[x[1] for x in states]);pe=s.diag(*[x[2] for x in states]);pf=s.diag(*[x[3] for x in states]);z=s.eye(d)-2*pf
 A=s.zeros(d);B=s.zeros(d);J=s.zeros(d)
 for x,j in ix.items():
  nn,rr,e,f=x
  if nn and not f and (nn-1,rr,e,1) in ix:A[ix[(nn-1,rr,e,1)],j]=s.sqrt(nn)
  if nn and not e and (nn-1,rr,1,f) in ix:B[ix[(nn-1,rr,1,f)],j]=s.sqrt(nn)
  if e and not f and (nn,rr,0,1) in ix:J[ix[(nn,rr,0,1)],j]=1
 return states,n,nr,pe,pf,z,A,B,J

def exact(fault=None):
 out=[]
 def ck(n,v):out.append((n,bool(v)))
 N=2;st,n,nr,pe,pf,z,A,B,J=matrices(N,fault=='drop_extra_photon');d=len(st);D=s.Integer(101);h=s.Integer(3);g=s.Rational(7,10);Delta=s.Integer(2)
 X=A+A.T;Y=A-A.T;S=h/D*Y;H0=Delta*pe+g*(B+B.T);chi=-h*h/D
 if fault=='wrong_dispersive_sign':chi=-chi
 if fault=='discard_mediator_exchange':H0=Delta*pe
 C=chi*(pe*z+pf)
 if fault=='omit_mediator_matching':C=chi*pf
 if fault=='omit_local_counterterm':C=chi*pe*z
 microscopic=D*pf+H0+h*X+C
 ck('total contact excitation commutes with actual Hamiltonian',comm(n+nr+pe+pf,microscopic)==s.zeros(d))
 ck('anti-Hermitian generator',S.T==-S)
 ck('first exchange cancellation',comm(S,D*pf)==-h*X)
 ck('second-order exact dispersive operator',comm(S,h*X)/2==h*h/D*(pf-n*z))
 ck('compensated second-order matched LZ',comm(S,h*X)/2+C==chi*(n+pe)*z)
 cross=comm(S,H0)
 ck('actual JC cross commutator retained',cross==h*g/D*(J+J.T))
 ck('compensator norm is abs chi',max(abs(x) for x in C.diagonal())==abs(chi))
 ck('enlarged physical boundary included',(N+1,0,0,0) in st)
 # Actual neutral Ising/CNOT/SWAP/phase circuits, including a missing-entangler fault.
 Z=s.diag(1,-1);I=s.eye(2);H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
 ZZ=s.kronecker_product(Z,Z);ZI=s.kronecker_product(Z,I);IZ=s.kronecker_product(I,Z)
 pulse=s.eye(4) if fault=='omit_neutral_entangler' else (-s.I*s.pi*ZZ/4).exp()
 cz=s.exp(-s.I*s.pi/4)*(s.I*s.pi*ZI/4).exp()*(s.I*s.pi*IZ/4).exp()*pulse
 cz=cz.applyfunc(s.simplify);target_cz=s.diag(1,1,1,-1)
 ck('actual Ising plus local phases CZ',cz==target_cz)
 cn=s.kronecker_product(I,H)*cz*s.kronecker_product(I,H);cn=cn.applyfunc(s.simplify)
 target_cn=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
 ck('actual neutral CNOT circuit',cn==target_cn)
 swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
 rev=s.kronecker_product(H,I)*cz*s.kronecker_product(H,I)
 ck('actual three CNOT SWAP circuit',(cn*rev*cn).applyfunc(s.simplify)==swap)
 theta=s.pi/3;phase=lambda a:s.diag(1,s.exp(s.I*a))
 controlled=s.kronecker_product(phase(theta/2),phase(theta/2))*cn*s.kronecker_product(I,phase(-theta/2))*cn
 ck('actual two CNOT controlled phase',(controlled-s.diag(1,1,1,s.exp(s.I*theta))).applyfunc(s.simplify)==s.zeros(4))
 # Exact rational upper bound for simultaneous rate fixture in note.
 # sqrt3<2, exp(2s)<1/(1-2s), pi<22/7; all deliberately conservative.
 N=2;M=3;q=2;contacts=6;g=s.Rational(7,10);D=10**16;h=10**8;chi=s.Integer(1);g1=10**12;Jzz=10**12
 su=s.Rational(2,10**8);ru=(s.Rational(7,10**9)+s.Rational(16,10**8))/(1-2*su)
 td=s.Rational(11,4)*s.Rational(22,7);ec=2*contacts*su+td*ru
 # gap=2g^4/(4+4g^2N)^(3/2)>2g^4/27 since 7.92<9.
 gaplo=2*g**4/27
 Au=16*N*(N+1)/gaplo*(1+s.Rational(22,28)*(3+2*2)) # sqrtN>=1 and <=2
 BNup=N*s.Rational(22,7)/2;line=4*q+2
 G=(2*line+1)*(34*N*q+2*q*q+8*q)+2*line*(N+q)
 Jamp=s.Rational(1,10**8);lam0=s.Rational(6,10**24);lamc=s.Rational(8,10**24)
 bound=Au*Jamp+lam0*BNup/Jamp+ec+lamc*td+lam0*(G*(3*s.Rational(22,7)/(4*Jzz)+12*s.Rational(22,7)/g1)+contacts*s.Rational(22,7)/g1)
 ck('fixed coupling actual chi',s.Rational(h*h,D)==1)
 ck('small exponential majorant domain',2*su<1)
 ck('exact full apparatus certificate below one percent',bound<s.Rational(1,100))
 ck('hopping cap gBS one satisfies J/bk',Jamp<s.Rational(1,2))
 return out,{'full_rate_fixture_rational_upper_bound':str(bound),'full_rate_fixture_decimal_upper_bound':str(s.N(bound,20)),'contact_error_upper_bound':str(s.N(ec,20)),'neutral_gate_bound':G,'contact_count':contacts}

def mm(A):return mp.matrix([[mp.mpf(str(s.N(z,85))) for z in A.row(i)] for i in range(A.rows)])
def opnorm(A):
 vals=mp.eighe(A.transpose_conj()*A,eigvals_only=True);return mp.sqrt(max(mp.mpf(0),max(vals)))
def numerical():
 mp.mp.dps=70;out=[];values={}
 def ck(n,v):out.append((n,bool(v)))
 N=1;states,n,nr,pe,pf,z,A,B,J=matrices(N);n,nr,pe,pf,z,A,B,J=map(mm,(n,nr,pe,pf,z,A,B,J));g=mp.mpf('.7');Delta=mp.mpf(2);h=mp.mpf(100)
 for sign in [1,-1]:
  D=sign*mp.mpf(100003);chi=-h*h/D;t=mp.mpf('.37')/abs(chi);H0=Delta*pe+g*(B+B.T);S=h/D*(A-A.T);C=chi*(pe*z+pf)
  H=D*pf+H0+h*(A+A.T)+C;Heff=D*pf+H0+chi*(n+pe)*z
  small=abs(h/D)*mp.sqrt(N+1);rb=mp.exp(2*small)*(abs(h*g/D)+2*abs(h)**3*mp.sqrt(N+1)*(N+2)/D**2)
  dressed=mp.expm(S)*H*mp.expm(-S);res=opnorm(dressed-Heff)
  U=mp.expm(-1j*t*H);phase=mp.expm(1j*D*t*pf);V=mp.expm(-1j*t*(H0+chi*(n+pe)*z))
  err=opnorm(phase*U-V);bound=2*small+t*rb;omit=opnorm(U-V)
  ck(f'D sign {sign} remainder bound',res<=rb);ck(f'D sign {sign} corrected propagator bound',err<=bound);ck(f'D sign {sign} omitted phase is a genuine failure',omit>bound)
  values[str(sign)]={'time':str(t),'remainder':str(res),'remainder_bound':str(rb),'corrected_error':str(err),'error_bound':str(bound),'omitted_phase_error':str(omit)}
 # Exact 2x2 microscopic counterexample at its actual long time. No boolean mutation.
 D=mp.mpf(100);h=mp.mpf(1);H=mp.matrix([[0,h*mp.sqrt(2)],[h*mp.sqrt(2),D-h*h/D]])
 vals,vecs=mp.eigsy(H);delta=vals[0]+2*h*h/D;time=mp.pi/delta
 U=mp.expm(-1j*time*H);bare=mp.matrix([1,0]);actual=U*bare;idealphase=mp.exp(1j*2*h*h/D*time)
 # superpositions with orthogonal vacuum: overlap=(1+e^-i idealphase * actual_00)/2
 overlap=(1+mp.conj(idealphase)*actual[0])/2;distance=mp.sqrt(max(0,1-abs(overlap)**2))
 ck('long-time phase defect strictly positive',delta>0);ck('long-time actual pure-state trace distance near one',distance>mp.mpf('.99'));ck('long-time leakage remains small',abs(actual[1])<mp.mpf('.03'))
 values['long_time_counterexample']={'h_over_D':str(h/D),'energy_defect':str(delta),'time':str(time),'state_trace_distance':str(distance),'leakage_amplitude':str(abs(actual[1]))}
 return out,values

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();checks,fixture=exact();assert all(v for _,v in checks),checks
 faults=[]
 for f in ['wrong_dispersive_sign','omit_mediator_matching','omit_local_counterterm','drop_extra_photon','discard_mediator_exchange','omit_neutral_entangler']:
  out,_=exact(f);bad=[n for n,v in out if not v];assert bad,f;faults.append({'changed_operator':f,'detected_by':bad})
 num,values=numerical();assert all(v for _,v in num),num
 report={'result':'K2336','status':'pass','exact_controls':checks,'finite_70digit_controls':num,'changed_operator_faults':faults,'numerical_omitted_phase_faults':2,'rate_fixture':fixture,'numerical_values':values,'scope':'Finite exact matrices/rational rate bound and finite high-precision propagators. Universal bounds rest on written BCH and channel-telescoping proofs; no interval, empirical, hardware or native GU certificate.'}
 deps=[f'tests/channel-swings/{ST.replace("-","_")}_probe.py',f'explorations/conditional-build/{ST}-2026-10-30.md','explorations/conditional-build/k2334-microscopic-neutral-transfer-2026-10-30.md','lab/process/k2334-microscopic-neutral-transfer.json']
 report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}
 if a.write:(R/f'lab/process/{ST}.json').write_text(json.dumps(report,indent=2)+'\n')
 print('PASS',len(checks),'exact;',len(num),'finite70digit;',len(faults),'changed-operator faults and2 omitted-phase faults');print(json.dumps(fixture));print(json.dumps(values))
if __name__=='__main__':main()
