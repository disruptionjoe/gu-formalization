"""Exact finite-tail family construction. No floating optimizer or global optimum claim."""
from pathlib import Path
import sympy as s,json,hashlib
R=Path(__file__).resolve().parents[2];q=s.Rational
BITS=[0,1,1,1,0,0,0,0,1]
def basis():
 T=s.zeros(10);T[0,0]=q(2,5);T[-1,-1]=q(1,10)
 for i,b in enumerate(BITS):
  col=i if b else i+1;w=q(1,5) if b else q(4,5);T[i,col]+=w/2;T[i+1,col]+=w/2
 M=s.eye(10)-T;rhs=s.zeros(10,2);rhs[1,0]=1;rhs[8,1]=1
 return M,M.inv()*rhs

def family(N,E):
 M,B=basis();rows=[B.row(i) for i in range(10)]+[B.row(9)*q(1,9)**(i-9) for i in range(10,N)]
 mat=s.Matrix([[sum(row[j] for row in rows) for j in range(2)],[sum((2*i+1)*row[j] for i,row in enumerate(rows)) for j in range(2)]])
 xy=mat.inv()*s.Matrix([1,E]);p=[s.factor((row*xy)[0]) for row in rows]
 return p,s.factor(sum(xy)),xy

def formula(N,r,E):return 135*(-36*E*r+2228*E+72*N*r+45*r-91213)/(34824*N*r-20223*r-41518097)

def produce():
 E,n,r,h=s.symbols('E n r h');M,B=basis();mi=s.Matrix([[sum(B[:,j])+B[9,j]/8 for j in range(2)],[sum((2*i+1)*B[i,j] for i in range(10))+q(85,32)*B[9,j] for j in range(2)]])
 mat=mi-s.Matrix([r/8,(8*n+5)*r/32])*B.row(9);xy=mat.inv()*s.Matrix([1,E]);F=s.factor(sum(xy));assert s.factor(F-formula(n,r,E))==0
 delta=s.factor(F.subs({n:n+1,r:r/9})-F)
 expected=4320*r*(1451*E-3499)*(4456*n+9*r-88985)/((11608*n*r+4867*r-124554291)*(34824*n*r-20223*r-41518097))
 assert s.factor(delta-expected)==0
 # Uniform feasible rectangle: r=9^{-(N-10)}, h=(N-10)r in[0,1/9].
 # Fractional expressions linear in h and r at fixed E. Check corners after
 # making the denominator positive, then multiaffine interpolation proves all.
 den=41518097-34824*n*r+20223*r
 pop=B*xy
 quantities=list(pop)+list(xy)
 for i,bit in enumerate(BITS):quantities.append((pop[i]/4-pop[i+1])*(1 if bit else -1))
 controls=0
 for expr in quantities:
  num=s.factor(expr*den).expand().subs(n*r,h+10*r).expand()
  assert not num.has(n),num
  for ee in [q(249,100),q(251,100)]:
   for rr in [0,1]:
    for hh in [0,q(1,9)]:
     assert num.subs({E:ee,r:rr,h:hh})>=0,('uniform feasibility',num,ee,rr,hh);controls+=1
 # Entire N20 feasible energy interval by exact affine inequalities.
 p,val,xy20=family(20,E);exprs=p+list(xy20)
 for i,bit in enumerate(BITS+[1]*10):exprs.append((p[i]/4-p[i+1])*(1 if bit else -1))
 left=s.S(0);right=None
 for expr in exprs:
  aa=expr.subs(E,0);bb=s.diff(expr,E)
  if bb>0:left=max(left,-aa/bb)
  elif bb<0:right=-aa/bb if right is None else min(right,-aa/bb)
  else:assert aa>=0
 assert left<q(5,2)<right
 f20=s.factor(val.subs(E,q(5,2)));old=q(11561805,41518097)
 assert f20<old
 # Exact all-N sign argument: denominators negative, n*r<=10;
 # factor4456n+9r-88985 is negative n<=19 and positive n>=20.
 assert 4456*19+9-88985<0 and 4456*20-88985>0
 assert 34824*10<41518097 and 11608*10+4867<124554291
 pins={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['lab/process/k2059-energy-aware-thermal-tail.json','lab/process/k2066-thermal-terminal-response.json','tests/channel-swings/k2059_energy_aware_thermal_tail_probe.py']}
 return dict(id='K2068',scope='explicit two-deficit odd-ladder population family only; no unrestricted optimum or minimum dimension',inputs=pins,formula=str(F),difference=str(delta),basis=[[str(x) for x in row] for row in B.tolist()],uniform_feasible_interval=['249/100','251/100'],all_integer_N_minimizer=20,occupied_support=list(range(1,40,2)),physical_spectrum=list(range(41)),population_affine=[[str(x.subs(E,0)),str(s.diff(x,E))] for x in p],energy_interval=list(map(str,[left,right])),line=[str(val.subs(E,0)),str(s.diff(val,E))],population=list(map(str,[x.subs(E,q(5,2)) for x in p])),value=str(f20),prior_upper=str(old),gain=str(old-f20),relative_gap_gain=str((old-f20)/(old-q(549971760412002337513926417,1976871225373814177206100780))),uniform_corner_controls=controls,negative_scout='Floating 24-level MILP suggested a much larger improvement; exact active-system and shell checks did not certify it. No numerical optimum claim retained.')
if __name__=='__main__':
 import argparse
 a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');args=a.parse_args();d=produce();dest=R/'lab/process/k2068-thermal-population-construction.json'
 if args.write:dest.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==d
 print('PASS symbolic family/difference, all-N minimum, corners',d['uniform_corner_controls'],'upper',d['value'],'gain',d['gain'],'interval',d['energy_interval'])
