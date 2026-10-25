"""Exact symbolic small-factor controls. Universal classification uses written proof."""
from pathlib import Path
import json,hashlib,argparse
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[2]

def produce():
 import sympy as s
 from k2056_common_dual_successor import gamma,product,identity,mul,add,trans
 checks=[]
 def ck(name,value):assert value,name;checks.append(name)
 gs=[gamma(k) for k in range(14)];ii=identity(128);B=product(gs[7:]);G=mul(B,gs[0]);V=product(gs);W=add((F(3,2),ii),(F(1,2),V));FF=add((-1,mul(G,W)));M=product([gs[i] for i in [0,1,2,10]])
 ck('actual_mass_skew',trans(M)==add((-1,M)));ck('actual_mass_square',mul(M,M)==add((-1,ii)));ck('actual_mass_commutes_F',mul(M,FF)==mul(FF,M));ck('actual_mass_commutes_W',mul(M,W)==mul(W,M))
 for k in [7,8,9]:
  C=mul(gs[0],gs[k]);ck(f'actual_C{k}_symmetric',trans(C)==C);ck(f'actual_C{k}_square',mul(C,C)==ii);ck(f'actual_C{k}_commutes_F',mul(C,FF)==mul(FF,C));ck(f'actual_C{k}_anticommutes_mass',not add((1,mul(C,M)),(1,mul(M,C))))
 a=(s.sqrt(641)-19)/2;b=a+19
 ck('a_minimal_polynomial',s.simplify(a*a+19*a-70)==0)
 ck('six_disjoint_frequencies',3<a<s.Rational(7,2) and 22<b<s.Rational(45,2) and len({1,2,a,2*a,b,2*b})==6)
 mult=[288,288,32,32,32,32];ck('real_dimension',sum(2*x for x in mult)==1408);ck('generator_dimension',sum(x*x for x in mult)==169984)
 J=s.Matrix([[0,1],[-1,0]]);I=s.eye(2);rows=[]
 for r in [s.Rational(1),s.Rational(2),a,2*a,b,2*b]:
  T=-r*J
  for c,d in [(s.Rational(1),s.Rational(0)),(s.Rational(5,4),s.Rational(3,4)),(s.Rational(17,8),s.Rational(15,8))]:
   P=r*(c*I+s.I*d*J);A=-s.I*T.inv()*s.conjugate(P)
   ck('Hermitian',P.H==P);ck('positive',r>0 and c>abs(d));ck('kinetic',s.simplify(A.T*T-s.I*P)==s.zeros(2));ck('antisquare',s.simplify(A*s.conjugate(A)+I)==s.zeros(2));ck('conservation',s.simplify(T.T*P+P*T)==s.zeros(2));rows.append([str(r),str(c),str(d)])
 P=s.diag(2,s.Rational(1,2));T=J;A=-s.I*T.inv()*P
 ck('anisotropic_kinetic_survivor',A*s.conjugate(A)==-I);ck('anisotropic_fails_allowed_generator',T.T*P+P*T!=s.zeros(2))
 # Noncentral skew coupling between distinct frequencies defeats fixed Pstar.
 T=s.diag(J,2*J);P=s.diag(1,1,2,2);N=s.zeros(4);N[0,2]=1;N[2,0]=-1
 ck('arbitrary_skew_not_enough',N.T==-N and N.T*P+P*N!=s.zeros(4) and T*N!=N*T)
 # Full spin-factor dispersion control at a nontrivial rational momentum.
 cs=[mul(gs[0],gs[k]) for k in [7,8,9]]
 for j in range(3):
  for k in range(j):ck('spatial_Clifford_anticommutator',not add((1,mul(cs[j],cs[k])),(1,mul(cs[k],cs[j]))))
 momenta=[F(1,2),F(-3,4),F(5,8)];mass=F(7,4)
 X=add(*[(v,c) for v,c in zip(momenta,cs)])
 ck('actual_Fourier_H_squared',add((1,mul(X,X)),(-mass*mass,mul(M,M)))==add((sum(v*v for v in momenta)+mass*mass,ii)))
 ck('actual_Fourier_cross_term',not add((1,mul(X,M)),(1,mul(M,X))))
 pins={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k2038-observed-action-compression-2026-10-24.md','explorations/conditional-build/k2056-common-dual-successor-2026-10-25.md']}
 return dict(scope='conditional observed graph changed coefficient class only',frequencies=['1','2','a','2a','b','2b'],unitary_multiplicities=mult,real_frequency_dimensions=[2*x for x in mult],complexified_frequency_dimensions=[2*x for x in mult],generator_dimension=169984,universal_metric_parameters=6,real_universal_metric='Pstar unique',rows=rows,checks=checks,inputs=pins)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();r=produce();dest=ROOT/'lab/process/k2058-universal-positive-dynamics.json'
 if args.write:dest.write_text(json.dumps(r,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==r
 print('PASS',len(r['checks']),'exact factor/control obligations')
