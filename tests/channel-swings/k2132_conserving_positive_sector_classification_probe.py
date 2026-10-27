"""Actual native frame identities and exact noncommuting graph controls; see written classification proof."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
import sympy as s
import k2123_same_current_potential_dynamics_probe as n
q=n.q;G=Path(__file__).resolve().parents[2]
def clean(a):return {ij:s.expand(v) for ij,v in a.items() if s.expand(v)!=0}
def mul(a,b):return clean(q.mul(a,b))
def add(*xs):return clean(q.add(*xs))
def frame(fault=None,c=F(5,3),sh=F(4,3)):
 cs,m,f,t,z,r,p=n.native();tt=add((s.I,t));S=add((s.I,f));Q={(i,i^4):F((-1)**((i&72).bit_count())) for i in range(128)}
 if fault=='native-Q-sign':Q[min(Q)]*=-1
 E=add((F(1,4),mul(add((1,q.I),(1,tt)),add((1,q.I),(1,z)))))
 if fault=='hyperbolic-normalization':c=F(4,3)
 Y=mul(add((1,q.I),(c,r),(sh,Q)),E);dY=mul(add((sh,r),(c,Q)),E)
 if fault=='frame-derivative':dY=mul(Q,E)
 return cs,m,S,tt,z,r,Q,E,Y,dY,c,sh

def checks(fault=None):
 cs,m,S,t,z,r,Q,E,Y,dY,c,sh=frame(fault);a=F(9,280);ck={}
 ck['native-Q-involution']=n.adj(Q)==Q and mul(Q,Q)==q.I
 ck['native-Q-commutant']=all(not n.comm(Q,x) for x in cs+[m,z,r]) and not add((1,mul(Q,t)),(1,mul(t,Q)))
 ck['joint-projector-rank32']=n.adj(E)==E and mul(E,E)==E and sum(v for (i,j),v in E.items() if i==j)==32
 ck['hyperbolic-identity']=c*c-sh*sh==1
 ck['frame-Euclidean-Gram']=mul(n.adj(Y),Y)==add((2*c*c,E))
 ck['frame-current']=mul(n.adj(Y),mul(S,Y))==add((2*a,E))
 ck['frame-current-derivative']=not mul(n.adj(Y),mul(S,dY))
 ck['frame-intertwining']=all(mul(x,Y)==mul(Y,x) for x in cs+[m])
 P=add((1/(2*c*c),mul(Y,n.adj(Y))))
 ck['projector-current']=mul(P,P)==P and mul(P,mul(S,P))==add((a/(c*c),P))
 ck['outside-positive-t-half']=bool(mul(add((1,q.I),(-1,t)),Y))
 # Two-dimensional noncommuting graph block, repeated four times to reach multiplicity8.
 I=s.eye(2);B=s.diag(s.Rational(3,5),0);C=s.Rational(3,5)*s.Matrix([[0,1],[1,0]]);U=s.Matrix([[s.Rational(3,5),s.Rational(-4,5)],[s.Rational(4,5),s.Rational(3,5)]]);D=s.diag(1,s.Rational(4,5));A=U*D
 if fault=='polar-order':A=D*U
 Z=I-A.H*A+B.H*B-C.H*C;T=I+A.H*A-B.H*B-C.H*C
 ck['noncommuting-graph-isotropy']=Z==s.zeros(2)
 ck['noncommuting-graph-positive-current']=T==s.Rational(32,25)*I
 rr=s.Rational(6,5);zp=1-rr**2;tp=1+rr**2
 ck['positive-not-conserving-countercontrol']=tp+3*zp>0 and tp-3*zp>0 and zp!=0
 cb=I if fault!='strict-boundary' else s.Rational(3,5)*I
 ck['strict-boundary-zero-not-positive']=I-cb.H*cb==s.zeros(2)
 return ck
FAULTS=['native-Q-sign','hyperbolic-normalization','frame-derivative','polar-order','strict-boundary']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();ck=checks();assert all(ck.values()),ck;bad={}
 for f in FAULTS:
  b=checks(f);bad[f]=[k for k,v in b.items() if not v];assert bad[f],f;print('[FAIL detected]',f,bad[f][0])
 inp=['tests/channel-swings/k2123_same_current_potential_dynamics_probe.py','lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1967-paired-raw-coefficient-observation.json']
 out=dict(result_id='K2132',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=ck,fault_failures=bad,native_Q=dict(flip=4,character=72),graph_real_dimension=320,scope='Maximum-dimension constant Cl4 invariant conserving complex sectors, not source selection or all smaller inclusion-maximal sectors.',inputs={p:hashlib.sha256((G/p).read_bytes()).hexdigest() for p in inp})
 path=G/'lab/process/k2132-conserving-positive-sector-classification.json'
 if args.write:path.write_text(json.dumps(out,indent=2)+'\n')
 else:assert json.loads(path.read_text())==out
 print('PASS K2132',len(ck),'exact checks;',len(bad),'genuine faults')
if __name__=='__main__':main()
