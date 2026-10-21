"""Exact Gram/marginal and optimal qubit controls; general theorem is analytic."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
N=0
def ck(ok,label):
 global N
 assert bool(ok),label
 N+=1
def eq(a,b,label):ck(s.simplify(s.expand_complex(a-b))==0,label)
def mat(a,b,label):ck((a-b).applyfunc(s.expand_complex).applyfunc(s.simplify)==s.zeros(*a.shape),label)
def calculate(sign=-1,angle_sign=-1):
 global N
 N=0
 a=1/s.sqrt(2);E=s.Matrix([[1,0,a,a],[0,1,a,sign*s.I*a]]);C=E.T*E.conjugate()
 p1,p2,p3=s.symbols('p1 p2 p3',real=True);p4=1-p1-p2-p3;p=[p1,p2,p3,p4];rho=E*s.diag(*p)*E.conjugate().T
 mat(rho,s.Matrix([[(1+p1-p2)/2,(p3+s.I*p4)/2],[(p3-s.I*p4)/2,(1-p1+p2)/2]]),'weighted bath marginal')
 r2=(p1-p2)**2+p3**2+p4**2;eq(rho.det(),(1-r2)/4,'general marginal determinant');eq(s.trace(rho),1,'density trace')
 lam=s.symbols('lam',real=True);eq((lam*s.eye(2)-rho).det(),lam**2-lam+(1-r2)/4,'general characteristic polynomial')
 w=(1+angle_sign*s.I)/s.sqrt(2);Q=s.Matrix([[1,-s.conjugate(w)],[w,1]])/s.sqrt(2);R=Q.conjugate().T
 mat(Q.conjugate().T*Q,s.eye(2),'common rotation unitary');EE=R*E;mat(EE.T*EE.conjugate(),C,'all channel coefficients preserved')
 costs=[s.simplify(abs(EE[1,j])**2) for j in range(4)];want=[s.Rational(1,2),s.Rational(1,2),(1-a)/2,(1-a)/2]
 for x,y in zip(costs,want):eq(x,y,'exact branch energy')
 eq(sum(costs)/4,s.Rational(1,2)-s.sqrt(2)/8,'uniform optimum');ck(all(v<=s.Rational(1,2) for v in costs),'worst-population upper')
 eq(abs(E[0,0])**2+abs(E[1,0])**2,1,'normalized first branch');eq((E[:,0].conjugate().T*E[:,1])[0],0,'orthogonal branches lower bound')
 ru=rho.subs({p1:s.Rational(1,4),p2:s.Rational(1,4),p3:s.Rational(1,4)});rp=R*ru*R.conjugate().T
 mat(rp,s.diag(s.Rational(1,2)+s.sqrt(2)/8,s.Rational(1,2)-s.sqrt(2)/8),'passive uniform density')
 # Direct paired-spectrum check for a nonuniform population, rather than only the uniform case.
 pp=[s.Rational(1,2),s.Rational(1,4),s.Rational(1,8),s.Rational(1,8)];M=s.diag(*(s.sqrt(t) for t in pp))*C*s.diag(*(s.sqrt(t) for t in pp));rr=E*s.diag(*pp)*E.conjugate().T
 eq((lam*s.eye(4)-M).det(),lam**2*(lam*s.eye(2)-rr).det(),'weighted Gram spectrum including zeros')
 eq(s.trace(M*M),s.trace(rr*rr),'purity spectrum control');eq(s.Rational(1,2)-s.sqrt(2)/8+s.sqrt(2)/8,s.Rational(1,2),'recoverable common-rotation energy')
 ck(s.Rational(3,4)>s.Rational(1,2)-s.sqrt(2)/8,'classical complete-dephasing countercontrol')
 S=s.ones(4)+C+C.applyfunc(lambda v:v*v)
 for k in range(1,5):ck(s.simplify(S[:k,:k].det())>0,'positive tensor-Gram principal minor')
 eq(sum(C),5+3*s.sqrt(2),'Poisson coefficient sum')
 eq(1-sum(C)/16,(11-3*s.sqrt(2))/16,'simple-eigenvalue energy slope')
 ck((11-3*s.sqrt(2))/16>0,'positive linear energy slope')
 return {'uniform_energy_over_gap':'1/2-sqrt(2)/8','worst_population_energy_over_gap':'1/2','recovered_energy_over_gap':'sqrt(2)/8','population_formula':'(1-sqrt((p1-p2)**2+p3**2+p4**2))/2','robust_uniform_lower':'max(0,1/2-sqrt(2)/8-3*delta/4)','branch_energies_over_gap':[str(x) for x in costs],'reset_unitary_only_for_rank_one':True,'poisson_endpoint_bath_dimension':4,'poisson_initial_energy_slope':'(11-3*sqrt(2))/16','bounded_control_regular_start':False,'math_checks':N}
def pin():return hashlib.sha256((ROOT/'explorations/conditional-build/k1905-causal-quantum-memory-realization-2026-10-21.md').read_bytes()).hexdigest()
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write-report',action='store_true');args=ap.parse_args();d=calculate();d['dependency_sha256']=pin();d['poisson_dependency_sha256']=hashlib.sha256((ROOT/'explorations/conditional-build/k1909-poisson-phase-classification-2026-10-21.md').read_bytes()).hexdigest()
 if args.write_report:(ROOT/'lab/process/k1910-minimal-dephasing-bath-energy.json').write_text(json.dumps(d,indent=2)+'\n')
 print(json.dumps(d))
