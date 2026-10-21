"""Exact phase-witness coefficients; global inequalities are proved in the note."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
N=0
def ck(ok,label):
 global N
 assert bool(ok),label
 N+=1
def eq(a,b,label): ck(s.simplify(s.expand_complex(a-b))==0,label)
def mat(a,b,label): ck((a-b).applyfunc(s.expand_complex).applyfunc(s.simplify)==s.zeros(*a.shape),label)
def pin(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

def calculate(weight=6,phase=-1):
 global N
 N=0
 R=s.Matrix([[-s.Rational(1,2),-s.Rational(1,2),1,0],[-(1+s.I)/2,(-1+s.I)/2,0,1]])
 b=s.Matrix([[-s.Rational(1,2),s.Rational(1,2),0,0]]);l=s.Matrix([-1,1,0,phase*s.I])
 W=(weight*R.conjugate().T*R-b.conjugate().T*b).applyfunc(s.simplify)
 mat(R*s.ones(4,1),s.zeros(2,1),'vacuum annihilation');mat(R*l,s.zeros(2,1),'noise direction annihilation');eq((b*l)[0],1,'negative noise direction')
 G=s.Matrix(4,4,lambda j,k:l[j]*s.conjugate(l[k])-(abs(l[j])**2+abs(l[k])**2)/2)
 mat(G,G.conjugate().T,'Hermitian coefficient array')
 for j in range(4):eq(G[j,j],0,'fixed population')
 eq(s.trace(W*s.ones(4)),0,'classical tangent point');eq(s.trace(W*G),-1,'negative derivative')
 B=s.simplify(sum(abs(W[k,j])*abs(G[j,k])**2 for j in range(4) for k in range(4))/2)
 eq(B,s.Rational(3,2)+s.sqrt(193)+12*s.sqrt(2),'Taylor bound coefficient')
 ck(B<33,'strict rational bound');eq(sum(abs(x)**2 for x in W),s.Rational(961,4),'Frobenius norm squared')
 eq(-s.Rational(1,66)+33*s.Rational(1,66)**2,-s.Rational(1,132),'finite time margin')
 q=s.sqrt(2);V=s.Matrix([[1,0,1/q,1/q],[0,1,1/q,s.I/q]]);C=V.conjugate().T*V
 eq(s.trace(W*(C-s.ones(4))),s.Rational(41,2)-12*q,'old Poisson inconclusive derivative')
 P=s.eye(4)-s.ones(4)/4;mat(P*G*P,P*l*l.conjugate().T*P,'projected rank one generator');ck((P*G*P).rank()==1,'rank one')
 eq(2*(s.Rational(1,7)**4+2*s.Rational(1,7)**2+3*s.Rational(1,7)),s.Rational(2256,2401),'late time positive density margin')
 return {'generator':['-1','1','0','-I'],'classical_phase_witness_weight':6,'derivative':-1,'certified_time_interval':'0<t<1/33','time':'1/66','witness_upper':'-1/132','output_trace_distance_lower':'1/16896','old_poisson_classification':'classical for t>=log(12)/(1-1/sqrt(2)); earlier times not decided','late_classical_threshold':'2*log(7)','late_phase_histories':81,'W':[[str(x) for x in W.row(j)] for j in range(4)],'math_checks':N}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args();d=calculate();d['dependency_sha256']=pin('explorations/conditional-build/k1906-dephasing-divisibility-boundary-2026-10-21.md')
 if args.write_report:(ROOT/'lab/process/k1908-quantum-markov-phase-noise.json').write_text(json.dumps(d,indent=2)+'\n')
 print(json.dumps(d))
