"""Actual inherited Gram/current and factorized full-carrier completion identities."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import sympy as s
import k2123_same_current_potential_dynamics_probe as n
q=n.q;adj=n.adj
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2131-common-form-selector-completion.json'

def mul(a,b):
 # Expand exact complex arithmetic before structural dictionary comparison.
 return {key:v for key,w in q.mul(a,b).items() if (v:=s.expand(w))!=0}

def checks(fault=None):
 cs,m,fc,t,z,r,p=n.native();J={}
 for k,b in enumerate(json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks']):
  for (row,col),v in mul(n.dec(b['basis']),n.dec(b['section'])).items():J[b['coordinates'][row],4*k+col]=v
 ck={};put=lambda key,x:ck.__setitem__(key,bool(x));G=mul(adj(J),J);d=F(1573,9800)
 put('native-Gram-spectrum',set(map(str,G.values()))=={'121/980','242/1225'} and all(i==j for i,j in G))
 put('Gram-commutes-TZ',not n.comm(G,t) and not n.comm(G,z))
 put('Gram-reflection-identity',q.add((1,G),(1,mul(r,mul(G,r))))==q.add((2*d,q.I)))
 # Non-special rational angle; all-angle theorem uses the structural identities above.
 p=q.add((F(1,4),mul(q.add((1,q.I),(s.I,t)),q.add((1,q.I),(F(3,5),r),(s.I*F(4,5),mul(z,r))))))
 put('rotated-projector',adj(p)==p and mul(p,p)==p and n.tr(p)==32)
 put('compressed-Gram',mul(p,mul(G,p))==q.add((d,p)))
 put('same-inherited-current',mul(p,mul(q.add((s.I,fc)),p))==q.add((F(9,280),p)))
 X=mul(J,p);L=q.add(((1/d if fault!='left-inverse-scale' else 2/d),mul(p,adj(J))))
 LX=mul(L,X);put('actual-left-inverse',LX==p)
 B=q.add((2,q.I),(3,cs[0]),(-1,cs[1]),(4,cs[2]));Qa=q.add((5,q.I),(-2,cs[0]),(3,cs[1]),(1,cs[2]))
 A=q.add((7,m),(s.I,Qa),((F(-1,2) if fault=='real-gradient' else -s.I/2),mul(z,B)))
 AP=mul(A,p);Y=mul(q.raw(0),mul(J,AP));HY=mul(q.H,Y)
 C=mul(adj(X),HY);put('compressed-compatibility',C==adj(C))
 vv=mul(mul(cs[0],cs[1]),cs[2]);wanted=q.add((-s.I*F(9,280)*7,mul(p,mul(m,p))),(F(9,280),mul(p,mul(Qa,p))),(-s.I*F(27,560),mul(p,mul(vv,mul(B,p)))))
 put('actual-compatibility-formula',C==wanted)
 # QX evaluated through the exact low-rank factors. Never assume interpolation.
 correction=0 if fault=='omit-interpolation-subtraction' else -1
 QX=q.add((1,mul(HY,LX)),(1,mul(adj(L),mul(adj(Y),mul(q.H,X)))),(correction,mul(adj(L),mul(C,LX))))
 put('full-carrier-interpolation',mul(q.H,QX)==Y)
 # Q-Q*=-L*(C-C*)L, first two summands pair by adjoint.
 put('Hermitian-defect-on-injection',not mul(adj(LX),mul(q.add((1,C),(-1,adj(C))),LX)))
 put('original-H-Hermitian-involution',adj(q.H)==q.H and mul(q.H,q.H)=={(j,j):1 for j in range(1920)})
 wrong=q.add((1,AP),(s.I,mul(z,p))) if fault=='gradient-sign' else AP
 leakage=mul(q.add((1,q.I),(-1,p)),wrong)
 required=q.add((-s.I/2,mul(z,mul(B,p))))
 put('selected-gradient-cancellation',leakage==required)
 return ck

FAULTS=['left-inverse-scale','real-gradient','omit-interpolation-subtraction','gradient-sign']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 good=checks();assert all(good.values()),good
 bad={f:[k for k,v in checks(f).items() if not v] for f in FAULTS};assert all(bad.values()),bad
 for f,errors in bad.items():print('[FAIL detected]',f,errors)
 inputs=['lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1967-paired-raw-coefficient-observation.json','tests/channel-swings/k2123_same_current_potential_dynamics_probe.py','tests/channel-swings/k2021_common_degree_dual_operator.py']
 result=dict(result_id='K2131',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=good,fault_failures=bad,evidence_kind='Exact native sparse rational/complex identities and factorized full-carrier interpolation. Universal extension and PDE domain scope use the written proof.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
 if args.write:OUT.write_text(json.dumps(result,indent=2)+'\n')
 else:assert result==json.loads(OUT.read_text())
 print('PASS K2131',len(good),'exact native identities;',len(bad),'genuine coefficient faults')
if __name__=='__main__':main()
