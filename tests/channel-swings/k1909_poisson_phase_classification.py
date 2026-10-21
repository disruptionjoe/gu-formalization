"""Exact rational SOS certificate; its global implication is proved in the note."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k1909-poisson-phase-classification.json'
N=0
def ck(ok,label):
 global N
 assert bool(ok),label
 N+=1
def matrix(a,b,label):ck((a-b).applyfunc(s.simplify)==s.zeros(*a.shape),label)
def calculate(w,g):
 global N
 N=0
 W=s.Matrix(w).applyfunc(s.sympify);G=s.Matrix(g).applyfunc(s.sympify)
 matrix(W,W.conjugate().T,'Hermitian witness');matrix(W*s.ones(4,1),s.zeros(4,1),'zero tangent value');matrix(G,G.T,'symmetric Gram')
 x=s.symbols('x y z',real=True);den=[1+t*t for t in x]+[1];pl=[(1+s.I*t)**2 for t in x]+[1];mi=[(1-s.I*t)**2 for t in x]+[1]
 p=sum(W[j,k]*(s.prod(den) if j==k else mi[j]*pl[k]*s.prod(den[h] for h in range(4) if h not in [j,k])) for j in range(4) for k in range(4))
 m=s.Matrix([x[0],x[1],x[2],x[0]*x[1],x[0]*x[2],x[1]*x[2],s.prod(x)])
 ck(s.expand(p-(m.T*G*m)[0])==0,'all polynomial coefficients')
 L,D=G.LDLdecomposition();matrix(L*D*L.T,G,'exact LDL reconstruction')
 for a in D.diagonal():ck(a>0,'positive rational LDL pivot')
 a=1/s.sqrt(2);V=s.Matrix([[1,0,a,a],[0,1,a,s.I*a]]);C=V.conjugate().T*V;A=C-s.ones(4)
 d=s.simplify(-s.trace(W*A));ck(s.simplify(d-(159*s.sqrt(2)/125-s.Rational(1777,1000)))==0,'negative derivative')
 ck(s.Rational(707,500)**2<2,'lower sqrt2 bound');ck(159*s.Rational(707,500)/125-s.Rational(1777,1000)>s.Rational(1,50),'derivative rational margin')
 B=s.simplify(sum((abs(s.re(W[j,k]))+abs(s.im(W[j,k])))*abs(A[k,j])**2 for j in range(4) for k in range(4))/2)
 ck(s.simplify(B-(891-451*s.sqrt(2))/250)==0,'remainder coefficient');ck((891-451*s.Rational(707,500))/250<s.Rational(11,10),'remainder rational upper')
 ck(s.simplify(s.trace(W*W))==s.Rational(424611,125000),'witness Frobenius squared');ck(s.Rational(424611,125000)<4,'operator norm upper')
 t=s.Rational(1,110);ck(-t/50+s.Rational(11,10)*t*t==-s.Rational(1,11000),'uniform-time margin');ck(s.trace(W)==s.Rational(282,125),'noisy derivative coefficient')
 ck(5*s.sqrt(2)/10<1,'eta 9/10 Fourier phase law positive')
 return {'derivative':str(-d),'remainder_l1':str(B),'interval':'0<t<1/55','test_time':'1/110','witness_upper':'-1/11000','output_trace_distance_lower':'1/176000','all_time_classical_phase_process':False,'intermediate_times':'unclassified','noisy_phase_jump_sufficient':'eta>=1-1/(5*sqrt(2))','math_checks':N,'LDL_pivots':[str(v) for v in D.diagonal()]}
def pin():return hashlib.sha256((ROOT/'explorations/conditional-build/k1908-quantum-markov-phase-noise-2026-10-21.md').read_bytes()).hexdigest()
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args();data=json.loads(REPORT.read_text());result=calculate(data['W'],data['G']);data.update(result,dependency_sha256=pin())
 if args.write_report:REPORT.write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps(result))
