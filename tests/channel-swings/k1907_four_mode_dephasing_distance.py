"""Exact finite controls; analytic distance arguments are in the research note."""
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

def calculate(rate=s.Rational(1,2),phase=1):
 global N
 N=0
 a=1/s.sqrt(2);e=s.symbols('e',real=True)
 f=e*(a+e)-(a-e)**4
 ck(f.subs(e,s.Rational(13,100))<0,'root lower rational sign')
 ck(f.subs(e,s.Rational(14,100))>0,'root upper rational sign')
 eq(s.diff(f,e),a+2*e+4*(a-e)**3,'strict derivative identity')
 x1,x2,x3,x4=s.symbols('x1 x2 x3 x4',real=True);v=[x1,x2,x3,x4]
 g=lambda j,k:(v[j]-v[k])**2/2
 eq(g(0,2)+g(0,3)+g(1,2)+g(1,3)-g(0,1)-g(2,3),(x1+x2-x3-x4)**2/2,'general parallelogram identity')
 x,y=s.symbols('x y',positive=True);v=[s.Matrix([-x,0]),s.Matrix([x,0]),s.Matrix([0,y]),s.Matrix([0,-y])]
 M=s.Matrix(4,4,lambda j,k:((v[j]-v[k]).dot(v[j]-v[k]))/2)
 eq(M[0,1],2*x*x,'modulus long diagonal');eq(M[2,3],2*y*y,'modulus short diagonal')
 for j,k in [(0,2),(0,3),(1,2),(1,3)]:eq(M[j,k],(x*x+y*y)/2,'modulus cross edge')
 u=s.sqrt(s.pi)/2;l=s.Matrix([-u,u,0,-phase*s.I*u]);h=[0,0,0,s.pi/4]
 G=s.Matrix(4,4,lambda j,k:l[j]*s.conjugate(l[k])-rate*(abs(l[j])**2+abs(l[k])**2)-s.I*(h[j]-h[k]))
 want={(0,1):-s.pi/2,(0,2):-s.pi/8,(1,2):-s.pi/8,(0,3):-s.pi/4,(1,3):-s.pi/4+s.I*s.pi/2,(2,3):-s.pi/8+s.I*s.pi/4}
 for pair,value in want.items():eq(G[pair[0],pair[1]],value,'actual generator entry '+str(pair))
 for j in range(4):eq(G[j,j],0,'population conservation')
 eq(s.exp(-2*s.log(2)),s.Rational(1,4),'quarter long-pair attainment')
 eq(s.exp(-s.log(2)/2),a,'exact target arms')
 ck(s.Rational(56,81)>s.Rational(69,100) and s.Rational(25,36)<s.Rational(7,10),'logarithm rational brackets')
 ck(s.Rational(49,50)>11*s.sqrt(2)/16,'phase cosine rational margin')
 return {'lower_equation':'e*(1/sqrt(2)+e)=(1/sqrt(2)-e)**4','root_bracket':['13/100','14/100'],'upper':'1/4','previous_valid_upper':'1/sqrt(2)-exp(-pi/4)','modulus_optimum_attained':True,'complex_lower_equality_attained':False,'exact_complex_optimum_claimed':False,'math_checks':N}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args();d=calculate();d['dependency_sha256']=pin('explorations/conditional-build/k1906-dephasing-divisibility-boundary-2026-10-21.md')
 if args.write_report:(ROOT/'lab/process/k1907-four-mode-dephasing-distance.json').write_text(json.dumps(d,indent=2)+'\n')
 print(json.dumps(d))
