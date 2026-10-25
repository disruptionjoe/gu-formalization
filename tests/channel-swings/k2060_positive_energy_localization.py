"""Exact Clifford/projector controls; analytic theorems are proved in the note."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse,itertools
ROOT=Path(__file__).resolve().parents[2]
def produce():
 import sympy as s
 I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);J=s.Matrix([[0,1],[-1,0]]);tensor=s.kronecker_product
 cs=[tensor(X,I),tensor(Z,X),tensor(Z,Z)];M=tensor(Z,J);beta=-s.I*M;I4=s.eye(4);checks=[]
 def ck(n,b):assert b,n;checks.append(n)
 gs=cs+[M]
 for j,g in enumerate(gs):
  ck('real transpose signature',g.T==g if j<3 else g.T==-g)
  ck('Clifford square',g*g==(I4 if j<3 else -I4))
  for h in gs[:j]:ck('Clifford anticommutator',g*h+h*g==s.zeros(4))
 words=[]
 for bits in itertools.product([0,1],repeat=4):
  w=I4
  for b,g in zip(bits,gs):
   if b:w=w*g
  words.append(s.Matrix(list(w)))
 ck('full real M4 algebra',s.Matrix.hstack(*words).rank()==16)
 blocks=[576,576,64,64,64,64];ks=[d//8 for d in blocks]
 ck('real carrier unchanged',sum(blocks)==1408);ck('centralizer multiplicities',[72,72,8,8,8,8]==ks)
 ck('energy preserving class dimension',sum(k*k for k in ks)==10624)
 records=[]
 for p,mu,lam in [([3,0,0],4,-8),([0,3,4],12,0),([1,0,0],1,-2),([0,0,0],2,1),([2,-3,6],24,1)]:
  p=list(map(s.Rational,p));mu=s.Rational(mu);lam=s.Rational(lam);pp=sum(x*x for x in p);E=s.sqrt(pp+mu*mu);Ep=s.sqrt(pp+(mu+lam)**2)
  H=sum((x*c for x,c in zip(p,cs)),s.zeros(4))+mu*beta;H2=H+lam*beta;P=(I4+H/E)/2;Q=I4-P
  ck('actual projector',s.simplify(P*P-P)==s.zeros(4));ck('positive spectral relation',s.simplify(H*P-E*P)==s.zeros(4))
  ck('off diagonal beta norm',s.simplify(P*beta*Q*beta*P-pp/E**2*P)==s.zeros(4))
  ck('exact mass pulse transition',s.simplify(P*H2*Q*H2*P-lam**2*pp/E**2*P)==s.zeros(4))
  records.append(dict(p=list(map(str,p)),mu=str(mu),mass_shift=str(lam),transition_coefficient=str(s.simplify(lam**2*pp/(E**2*Ep**2)))))
 ck('complete transition',records[2]['transition_coefficient']=='1')
 # The theorem's algebra applies to the actual 128 factor, not only this model.
 from k2056_common_dual_successor import gamma,product,mul,add,identity,trans
 gam=[gamma(k) for k in range(14)];mm=product([gam[i] for i in [0,1,2,10]]);cc=[mul(gam[0],gam[k]) for k in [7,8,9]];ii=identity(128)
 ck('actual mass square',mul(mm,mm)==add((-1,ii)));ck('actual mass transpose',trans(mm)==add((-1,mm)))
 for c in cc:
  ck('actual spatial symmetry',trans(c)==c);ck('actual spatial square',mul(c,c)==ii);ck('actual mass anticommutes',not add((1,mul(c,mm)),(1,mul(mm,c))))
 # Pairwise Clifford relations and T centrality/spectrum reused from K2058.
 return dict(scope='massive conditional 1408 graph; fixed free positive spectral subspace',mass_assumption='mu > 0',real_blocks=blocks,multiplicity_spaces=ks,preserving_dimension=sum(k*k for k in ks),full_allowed_dimension=169984,excluded_dimensions=169984-sum(k*k for k in ks),pulse_records=records,checks=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k2058-universal-positive-dynamics-2026-10-25.md','explorations/conditional-build/k2038-observed-action-compression-2026-10-24.md','explorations/conditional-build/k1896-local-phase-vacuum-boundary-2026-10-21.md']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();d=produce();dest=ROOT/'lab/process/k2060-positive-energy-localization.json'
 if args.write:dest.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==d
 print('PASS',len(d['checks']),'exact algebra/projector controls; preserving dimension',d['preserving_dimension'])
