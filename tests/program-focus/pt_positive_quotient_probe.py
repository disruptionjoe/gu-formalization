#!/usr/bin/env python3
"""Actual K95 decay/readout and quotient controls; no physical norm chosen.

Exact sparse native Phi checks plus finite algebra. Open-packet, form-domain
and coarea implications are written proofs, not consequences of test counts.
"""
from pathlib import Path
import argparse,hashlib,json,sys,time
sys.dont_write_bytecode=True
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/program-focus'))
from printed_equation_jets_symbol_probe import engine
from source_action_deep_algebra import add,scale
from cw_fullsystem_domain_probe import compact_symbol,trace_mode,theta_amplitude,conjugate,boost_field,ell
CERT=ROOT/'lab/process/pt-positive-quotient-certificates.json'
D=[-1,1,1,1]+[1]*6+[-1]*4
FACTORS=[1,12,22,30,36,40,42]+list(range(-1,-13,-1))
def clean(x):return {k:s.expand(v)for k,v in x.items()if s.expand(v)!=0}
def rec(x):return [[a,b,str(v)]for (a,b),v in sorted(x.items())]
def build():
 e=engine(D);checks=[]
 def ck(name,value):
  assert value,name
  checks.append(name)
 def sym(z,v):return clean(e.Phi(e.wedge({(1<<j,0):a for j,a in z.items()},v)))
 def residual(z,v):return clean(add(scale(12,v),sym(z,v)))
 beta={(2,2):s.Integer(1),(4,4):s.Integer(-1)}
 tau={(0,1):s.Integer(-1)} # c(tau), raised with D00=-1
 Atbeta=clean(e.wedge(tau,beta))
 modes=[]
 for n,lam in [(s.Integer(10),s.Integer(8)),(s.Rational(15,2),s.Rational(9,2)),(s.Rational(25,4),s.Rational(7,4))]:
  z={0:-lam,10:s.I*n};gam={(0,1<<j):a/D[j]for j,a in z.items()}
  v=clean(add(scale(12,beta),scale(2,e.wedge(gam,beta))))
  ck('decay dispersion '+str(n),n*n-lam*lam==36)
  ck('actual native decay kernel '+str(n),not residual(z,v))
  ck('compact/native symbol agreement '+str(n),sym(z,v)==compact_symbol(z,v))
  ck('literal observed component '+str(n),v[(2,2)]==12)
  ck('primary-minus grades '+str(n),all(b.bit_count()in(1,2)for a,b in v))
  ck('real conjugate decay '+str(n),not residual({0:-lam,10:-s.I*n},conjugate(v)))
  ck('Theta converts decay to growth '+str(n),not residual({0:lam,10:-s.I*n},theta_amplitude(v)))
  modes.append({'n':str(n),'lambda':str(lam),'readout':'12','mode':rec(v)})
 # Actual regular hook frame x=q B_n+2p A, N(q,p)=(p,delta q).
 n=s.Integer(6);Bn=clean(add(scale(12,beta),scale(2,e.wedge({(0,1024):-s.I*n},beta))))
 C=lambda v:residual({10:s.I*n},v)
 ck('visible threshold eigenvector',not C(Bn) and Bn[(2,2)]==12)
 ck('actual native Jordan chain',not clean(add(C(scale(2,Atbeta)),sym({0:s.Integer(1)},Bn))))
 # Check the full two-vector descriptor, including a stable-side fixture.
 for n in [s.Integer(3),s.Integer(6),s.Integer(10)]:
  delta=n*n-36;Bn=clean(add(scale(12,beta),scale(2,e.wedge({(0,1024):-s.I*n},beta))))
  ck('regular q-column '+str(n),not clean(add(residual({10:s.I*n},Bn),sym({0:s.Integer(1)},scale(2*delta,Atbeta)))))
  ck('regular p-column '+str(n),not clean(add(residual({10:s.I*n},scale(2,Atbeta)),sym({0:s.Integer(1)},Bn))))
 # Threshold radical/readout plus a named minimal quotient interaction.
 dep='lab/process/printed-state-completion-certificates.json';d=json.loads((ROOT/dep).read_text())
 ck('owned state certificate hash',hashlib.sha256((ROOT/dep).read_bytes()).hexdigest()=='ec0aafeace76b0d47f9ec9a7b142be29b6c7349e2c3397283029d14fe3e88977')
 for p,h in d['dependencies'].items():ck('owned dependency '+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
 rr={(a,b):s.sympify(v)for a,b,v in d['native_response_checks']['resonant']['obstructing_projection']}
 rr=clean(scale(s.Rational(1,26112),rr));ck('radical eigenvector actual kernel',not residual({10:6*s.I},rr))
 ck('radical literal observation nonzero',rr[(1,2)]==1)
 u=trace_mode({0:9,1:10,10:-4});ck('retained commonCW mode',not residual({0:9*s.I,1:10*s.I,10:-4*s.I},u) and 100-16>36)
 force=clean(e.Phi(add(e.wedge(rr,u),e.wedge(u,rr))))
 ck('actual polarized quotient defect',force==clean(e.Phi(e.wedge(rr,u,'comm'))))
 ck('nonzero quotient defect receiver',force[(4,4)]==s.Rational(13448,13))
 outz={0:9*s.I,1:10*s.I,10:2*s.I}
 outq=s.expand(sum(a*a/D[j] for j,a in outz.items()))
 ck('output retained away from all thresholds',outq==-15 and 100-4>36 and all(144-4*a*outq!=0 for a in FACTORS))
 # Theta-fixed actual common-CW resonant history, not the rotated core pair.
 xp={0:s.Rational(26,3),1:s.Rational(28,3),10:s.Integer(3)}
 xm={0:-s.Rational(26,3),1:-s.Rational(28,3),10:s.Integer(3)}
 vp,vm=trace_mode(xp),trace_mode(xm)
 ck('fixed-history input kernels',not residual({j:s.I*v for j,v in xp.items()},vp) and not residual({j:s.I*v for j,v in xm.items()},vm))
 ck('fixed-history actual amplitude exchange',theta_amplitude(vp)==conjugate(vm) and theta_amplitude(vm)==conjugate(vp))
 fixed_force=clean(e.Phi(add(e.wedge(vp,vm),e.wedge(vm,vp))))
 ck('fixed-history actual receiver',ell(boost_field(fixed_force,-1))==104448)
 ck('fixed-history force not canceled',theta_amplitude(fixed_force)==conjugate(fixed_force) and bool(fixed_force))
 k=(s.Rational(28,3),3);l=(-s.Rational(28,3),3);neg=lambda x:tuple(-a for a in x);xs=[k,l,neg(k),neg(l)]
 hits=[(i,j)for i,x in enumerate(xs)for j,y in enumerate(xs)if tuple(a+b for a,b in zip(x,y))==(0,6)]
 ck('unique fixed-history output pair',hits==[(0,1),(1,0)])
 ck('fixed-history commonCW margin',k[0]**2-9==s.Rational(703,9) and k[0]**2-9>36)
 ck('fixed-history phase submersion',-2*s.Integer(3)/s.Rational(26,3)==-s.Rational(9,13))
 # Hermitian symmetrizer: conserved means N*G+GN=0, not Hamiltonian energy positivity.
 A,B,u0,v0,w=s.symbols('A B u v w',real=True)
 G=s.Matrix([[A,u0+s.I*v0],[u0-s.I*v0,B]]);N=s.Matrix([[0,1],[-w*w,0]])
 ck('stable Hermitian equations',(N.T*G+G*N).applyfunc(s.expand)==s.Matrix([[-2*u0*w*w,A-B*w*w],[A-B*w*w,2*u0]]))
 J=s.Matrix([[0,1],[0,0]])
 ck('Jordan Hermitian equations',(J.T*G+G*J).applyfunc(s.expand)==s.Matrix([[0,A],[A,2*u0]]))
 ck('Jordan PSD forces offdiagonal zero',G.det().subs({A:0,u0:0})==-v0*v0)
 ck('positive oscillator control',N.T*s.diag(w*w,1)+s.diag(w*w,1)*N==s.zeros(2))
 ck('readout faithful weighted control',N.T*s.diag(1,1/w**2)+s.diag(1,1/w**2)*N==s.zeros(2))
 ck('semidefinite quotient control',J.T*s.diag(0,1)+s.diag(0,1)*J==s.zeros(2))
 ck('dissipative positive control',s.Matrix([[-8]]).T+s.Matrix([[-8]])==s.Matrix([[-16]]))
 c,omega=s.symbols('c omega',positive=True);PU=s.Matrix([[0,-c],[-c,-c/omega]])
 ck('PU displayed overlap indefinite',s.factor(PU.det())==-c*c)
 ck('indefinite Jordan conserved control',J.T*s.Matrix([[0,s.I],[-s.I,0]])+s.Matrix([[0,s.I],[-s.I,0]])*J==s.zeros(2))
 deps=['tests/program-focus/source_action_deep_algebra.py','tests/program-focus/printed_equation_jets_symbol_probe.py','tests/program-focus/cw_fullsystem_domain_probe.py',dep,'lab/process/cw-fullsystem-domain-certificates.json','explorations/conditional-build/cw-one-sided-boundary-2026-11-27.md']
 return {'status':'PASS','checks':len(checks),'check_names':checks,'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in deps},'decay_modes':modes,'minimal_quotient':{'radical':rec(rr),'retained_input':rec(u),'force':rec(force),'receiver_theta2_gamma2':'13448/13','output_q':str(outq),'output_spatial_square':96},'theta_fixed':{'receiver':'104448','phase_derivative':'-9/13','pair_hits':[list(pair) for pair in hits]},'scope':'Exact sparse native identities and finite Hermitian controls. Packet/domain, PSD radical, coarea and nonlinear descent arguments require the accompanying reviewed proof. No physical norm, source quotient or GU verdict is certified.'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True);g.add_argument('--write-certificate',action='store_true');g.add_argument('--verify',action='store_true');a=ap.parse_args();t=time.monotonic();d=build()
 if a.write_certificate:CERT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(CERT.read_text())==d,'Certificate differs'
 print(json.dumps({'status':'PASS','checks':d['checks'],'seconds':time.monotonic()-t}))
