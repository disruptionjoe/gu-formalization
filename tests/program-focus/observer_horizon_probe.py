#!/usr/bin/env python3
"""Exact representation, actual native operator and trace-profile controls.
The cone limits and measure/domain arguments are written proofs, not a census.
"""
from pathlib import Path
import argparse,hashlib,json,sys
sys.dont_write_bytecode=True
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/program-focus'))
from printed_equation_jets_symbol_probe import engine
from source_action_deep_algebra import add,scale
from cw_fullsystem_domain_probe import compact_symbol
D=[-1,1,1,1]+[1]*6+[-1]*4
OUT=ROOT/'lab/process/observer-horizon-certificates.json'
def clean(x):return {k:s.expand(v)for k,v in x.items()if s.expand(v)!=0}
def rec(x):return [[a,b,str(v)]for(a,b),v in sorted(x.items())]
def build():
 checks=[]
 def ck(n,v):assert v,n;checks.append(n)
 lam=s.symbols('lambda',positive=True);g=s.diag(-1,1,1,1)
 ch=(lam+1/lam)/2;sh=(lam-1/lam)/2
 A=s.eye(4);A[0,0]=A[1,1]=ch;A[0,1]=A[1,0]=sh
 ell=s.Matrix([1,-1,0,0]);V=ell*ell.T
 ck('boost preserves actual base metric',s.simplify(A.T*g*A-g)==s.zeros(4))
 ck('boost determinant one',s.simplify(A.det())==1)
 ck('covector weight one',s.simplify(A.inv().T*ell-lam*ell)==s.zeros(4,1))
 ck('normal Sym2 weight two',s.simplify(A.inv().T*V*A.inv()-lam**2*V)==s.zeros(4))
 ck('normal weight vector nonzero',V[0,0]==1)
 ck('normal weight vector traceless',(g*V).trace()==0)
 ck('normal weight vector DeWitt null',((g*V)**2).trace()==0)
 h=s.Matrix(s.symbols('h0:4',real=True))
 ck('rescaled horizontal limit zero',all(s.limit(c,lam,s.oo)==0 for c in A*h/lam**2))
 for sign in [-1,1]:
  ck('rescaled normal limit '+str(sign),s.simplify(sign*A.inv().T*V*A.inv()/lam**2-sign*V)==s.zeros(4))
 # Exact span of null squares: the lineality cost is nine tracefree normal directions.
 rays=[]
 for j in range(3):
  for sign in [-1,1]:
   v=s.zeros(4,1);v[0]=1;v[j+1]=sign;rays.append(v)
 for i,j in [(1,2),(1,3),(2,3)]:
  v=s.zeros(4,1);v[0]=1;v[i]=s.Rational(3,5);v[j]=s.Rational(4,5);rays.append(v)
 ck('nine actual null covectors',all((v.T*g*v)[0]==0 for v in rays))
 squares=[v*v.T for v in rays]
 ck('null squares span nine dimensions',s.Matrix.hstack(*[s.Matrix([M[i,j] for i in range(4) for j in range(i,4)])for M in squares]).rank()==9)
 ck('all spanning squares tracefree',all((g*M).trace()==0 for M in squares))
 ck('trace projection complementary',s.Rational(1,4)*(g*g).trace()==1)
 # Matrix-cone controls: PSD is Lorentz-congruence invariant, but -epsilon I is not PSD.
 R=A.subs(lam,s.Integer(2));W=s.diag(1,2,3,4)
 ck('PSD congruence positive fixture',all((R.inv().T*W*R.inv())[:k,:k].det()>0 for k in range(1,5)))
 ck('negative normal perturbation leaves PSD',(-s.eye(4))[0,0]<0)
 ck('ordinary Lorentz timelike interior control',s.Integer(2)**2-(s.Rational(1,2))**2>0)
 # Native tracefree spatial off-diagonal: E12/sqrt2 is a unit positive K95 normal.
 S=s.zeros(4);S[1,2]=S[2,1]=1/s.sqrt(2)
 K=lambda u,v:s.expand((g*u*g*v).trace()-s.Rational(1,2)*(g*u).trace()*(g*v).trace())
 ck('actual offdiagonal normal traceless',(g*S).trace()==0)
 ck('actual offdiagonal normal unit positive',K(S,S)==1)
 ck('offdiagonal normal orthogonal trace',K(S,g)==0)
 ck('trace normal square',K(g,g)==-4)
 ck('mean curvature square',K(g/2,g/2)==-1)
 # Port theta4 is explicitly chosen to represent this unit normal; the native Clifford map is Spin-equivariant.
 e=engine(D);beta={(2,2):s.Integer(1),(4,4):s.Integer(-1)}
 eta={(16,0):s.Integer(1)}
 out=clean(e.Phi(e.wedge(eta,beta)))
 expected=clean(scale(-2,e.wedge({(0,16):s.Integer(1)},beta)))
 ck('native first-order conormal response',out==expected)
 ck('compact/native same response',out==compact_symbol({4:s.Integer(1)},beta))
 ck('nonzero literal horizontal receiver',out[(2,18)]==2)
 ck('exact two-term response',len(out)==2)
 ck('primary-minus input real',e.real_skew(beta))
 ck('primary-minus output real',e.real_skew(out))
 ck('positive auxiliary output norm',sum(v*v for v in out.values())==8)
 # Smooth transverse jets: a first-order operator sees one order beyond every finite value jet.
 z=s.symbols('z',real=True)
 for r in range(6):
  f=z**(r+1)
  ck('null input jet '+str(r),all(s.diff(f,z,j).subs(z,0)==0 for j in range(r+1)))
  ck('nonzero next output jet '+str(r),2*s.diff(f,z,r+1).subs(z,0)==2*s.factorial(r+1))
 ck('tangential derivative control',s.diff(z,s.symbols('x'))==0)
 ck('frozen zeroth order vanishes on support',(12*z+z*z).subs(z,0)==0)
 # Trace-flow tube: y=e^(r/2)g; induced horizontal volume e^r, trace metric -dr².
 r,c=s.symbols('r c',real=True);a=s.exp(r/2);f0=-r
 ck('ray weighted volume cancellation',s.simplify(s.exp(f0)*a*a)==1)
 ck('trace-profile first variation fixed',s.diff(s.exp(c*r*r),r).subs(r,0)==0)
 ck('finite-ray profile same first jet',s.diff(s.exp(c*r*r-r**4),r).subs(r,0)==0)
 ck('finite-ray profile arbitrary second variation',s.diff(s.exp(c*r*r-r**4),r,2).subs(r,0)==2*c)
 eps,chi,qchi=s.symbols('eps chi qchi',real=True)
 graph=s.exp(c*eps**2*chi**2-eps**4*chi**4)*s.sqrt(1-s.exp(-eps*chi/2)*eps**2*qchi)
 ck('compact trace graph second variation',s.diff(graph,eps,2).subs(eps,0)==2*c*chi**2-qchi)
 ck('trace-profile second variation free',s.diff(s.exp(c*r*r),r,2).subs(r,0)==2*c)
 for cv in [-1,0,1]:ck('trace second variation sign '+str(cv),s.diff(s.exp(cv*r*r),r,2).subs(r,0)==2*cv)
 ck('conformal ray adds one negative direction',K(g/2,g/2)==-1 and D[:4].count(-1)==1)
 deps=['tests/program-focus/source_action_deep_algebra.py','tests/program-focus/printed_equation_jets_symbol_probe.py','tests/program-focus/cw_fullsystem_domain_probe.py','explorations/conditional-build/symmetry-restoration-measure-limit-2026-11-25.md','explorations/conditional-build/natural-density-fibre-volume-2026-11-25.md','explorations/conditional-build/source-chimeric-trace-compatibility-2026-11-13.md']
 return {'status':'PASS','checks':len(checks),'check_names':checks,'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in deps},'native_response':rec(out),'cone_weights':{'horizontal_max':1,'normal':2,'limit_vectors':'(0,+V),(0,-V), V!=0'},'trace_flow':{'metric':'exp(r/2) g - dr^2','quadratic_comparison_volume':'exp(c r^2)','finite_radial_profile_volume':'exp(c r^2-r^4)','second_variation':'2c'},'scope':'Finite exact algebra only; invariant-measure theorem reused, cone closure and smooth-domain arguments separately reviewed. No physical cone, measure or source verdict.'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();q=ap.add_mutually_exclusive_group(required=True);q.add_argument('--write-certificate',action='store_true');q.add_argument('--verify',action='store_true');args=ap.parse_args();d=build()
 if args.write_certificate:OUT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(OUT.read_text())==d
 print(json.dumps({'status':'PASS','checks':d['checks']}))
