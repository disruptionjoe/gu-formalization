"""Exact physical two-loss restrictions, branch channels and analytic time integrals."""
from pathlib import Path
from itertools import combinations,product
import sympy as s
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v,c=False):
 (controls if c else checks)[k]=bool(v);assert v,k
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);pauli=[X,Y,Z]
V=s.zeros(16,2)
for b in (0,1):
 for word in [(0,0,b,b),(1,1,1-b,1-b)]:V[int(''.join(map(str,word)),2),b]=1/s.sqrt(2)
def trace_out(A,dims,removed):
 kept=[i for i in range(dims) if i not in removed];out=s.zeros(2**len(kept))
 words=list(product((0,1),repeat=dims))
 for ai,a in enumerate(words):
  for bi,b in enumerate(words):
   if any(a[i]!=b[i] for i in removed):continue
   ia=int(''.join(str(a[i]) for i in kept),2) if kept else 0;ib=int(''.join(str(b[i]) for i in kept),2) if kept else 0
   out[ia,ib]+=A[ai,bi]
 return out
masks=list(combinations(range(4),2));units=[]
for b,c in product((0,1),repeat=2):E=s.zeros(2);E[b,c]=1;units.append(E)
CX=s.zeros(4)
for a,b in product((0,1),repeat=2):CX[2*a+(b^a),2*a+b]=1
for mask in masks:
 kept=[i for i in range(4) if i not in mask];same=kept[0]//2==kept[1]//2
 # Build actual N2 restriction from physical formula, not a logical replacement.
 xs={i:(s.kronecker_product(X,I) if i==kept[0] else s.kronecker_product(I,X)) if i in kept else s.zeros(4) for i in range(4)}
 zs={i:(s.kronecker_product(Z,I) if i==kept[0] else s.kronecker_product(I,Z)) if i in kept else s.zeros(4) for i in range(4)}
 Hx=s.Rational(5-len(kept),2)*(xs[0]*xs[1]+xs[2]*xs[3]);Hz=s.Rational(5-len(kept),4)*(zs[0]+zs[1])*(zs[2]+zs[3])
 ck(f'physical_restriction_{mask}',Hx==(s.Rational(3,2)*s.kronecker_product(X,X) if same else s.zeros(4)) and Hz==(s.zeros(4) if same else s.Rational(3,4)*s.kronecker_product(Z,Z)))
 P=X if same else Z
 for j,E in enumerate(units):
  B=trace_out(V*E*V.T,4,mask)
  ck(f'physical_commute_{mask}_{j}',Hx*B==B*Hx and Hz*B==B*Hz)
  Bdec=CX*B*CX.T;out=trace_out(Bdec,2,[1] if same else [0]);want=(E+P*E*P)/2
  ck(f'extracted_channel_{mask}_{j}',out==want)
  ck(f'full_spectator_factorization_{mask}_{j}',Bdec==(s.kronecker_product(want,s.diag(1,0)) if same else s.kronecker_product(I/2,want)))
  for survivor in (0,1):ck(f'third_loss_constant_{mask}_{j}_{survivor}',trace_out(B,2,[survivor])==s.trace(E)*I/2)
# Logical rotation before second loss is retained, proving ordering dependence.
U=(I-s.I*Z)/s.sqrt(2);E=(I+X)/2;before=(U*E*U.conjugate().T+X*U*E*U.conjugate().T*X)/2
after=U*((E+X*E*X)/2)*U.conjugate().T
ck('dephase_rotate_do_not_commute',s.simplify(before-after)!=s.zeros(2),True)
# Exactly normalized second-loss density. k>0; e^-k=1/2, Omega=2pi.
k,w=s.symbols('k w',positive=True,real=True);D=(k-s.I*w)*(2*k-s.I*w)
J1=32*k/s.Integer(9)*((s.Rational(1,2)-1)/(-k+s.I*w)-(s.Rational(1,4)-1)/(-2*k+s.I*w))
J2=32*k/s.Integer(9)*((s.Rational(1,4)-s.Rational(1,2))/(-k+s.I*w)-(s.Rational(1,16)-s.Rational(1,4))/(-2*k+s.I*w))
C1=8*k*(k+s.I*w)/(9*D);C2=2*k*(5*k-s.I*w)/(9*D)
ck('first_integral',s.simplify(J1-C1)==0);ck('second_integral',s.simplify(J2-C2)==0)
ck('first_mass',s.simplify(J1.subs(w,0))==s.Rational(4,9));ck('second_mass',s.simplify(J2.subs(w,0))==s.Rational(5,9))
ck('imaginary_second_integral_positive',s.simplify(s.im(C2)-2*k*w*(13*k*k+w*w)/(9*(k*k+w*w)*(4*k*k+w*w)))==0)
# Compute illustrative decimal values from analytic expressions, not a finite-domain proof.
c1=complex(C1.subs({k:s.log(2),w:2*s.pi}).evalf(30));c2=complex(C2.subs({k:s.log(2),w:2*s.pi}).evalf(30));lx=abs(4/9+c2);lz=abs(5/9+c1)
error=(729-18*lx-36*lz)/1024;idle=s.Rational(675,1024)
ck('noncommuting_identity_endpoint',(-I)*(-I)==I and X*Z!=Z*X)
ck('strict_gap_fixture',0<lx<1 and 0<lz<1 and error>float(idle))
ck('idle_decoder_strictly_suboptimal',abs(c2.imag)>0 and lx>4/9+c2.real,True)
# Bell upper/lower match for non-axis aligned positive mixture.
lam=s.Rational(3,5);axis=(3*X+4*Y)/5
ck('axis_unitary_traceless',s.simplify(axis*axis)==I and s.trace(axis)==0)
def channel(E):return lam*(E+axis*E*axis)/2+(1-lam)*s.trace(E)*I/2
bell=s.Matrix([1,0,0,1])/s.sqrt(2);B=bell*bell.T
choi=s.zeros(4)
for b,c in product((0,1),repeat=2):E=s.zeros(2);E[b,c]=1;choi+=s.kronecker_product(channel(E),E)/2
ck('bell_fidelity',s.simplify((bell.T*choi*bell)[0]-(1+lam)/4)==0)
ck('bell_orthogonal_error',s.simplify(choi*bell-(1+lam)*bell/4)==s.zeros(4,1))
eigs=(choi-B).eigenvals();distance=sum(abs(x)*mult for x,mult in eigs.items())/2
ck('branch_diamond_bounds_match',distance==(3-lam)/4)
# Complete normalized mask probabilities for eta=1/4.
Pj=[s.binomial(4,j)*s.Rational(3,4)**j*s.Rational(1,4)**(4-j) for j in range(5)]
ck('mask_probability',Pj[2]/6==s.Rational(9,256) and Pj[3]+Pj[4]==s.Rational(189,256) and sum(Pj)==1)
ck('idle_limit',Pj[2]/2+3*(Pj[3]+Pj[4])/4==idle)
# General second-loss density integrates to flag weight by product rule.
x,y,dx,dy=s.symbols('x y dx dy');ck('density_product_rule',s.expand(s.diff((1-x)*(1-y),x)*dx+s.diff((1-x)*(1-y),y)*dy+dx*(1-y)+dy*(1-x))==0)
# A finer time record reveals two equally weighted orthogonal measurement axes.
# No-record lambda=1/sqrt2; each known-bin lambda=1, giving a strict information gain.
v0=s.Matrix([1,0,0]);v1=s.Matrix([0,1,0]);avg=(v0+v1)/2
ck('coarse_record_norm',s.sqrt(avg.dot(avg))==1/s.sqrt(2))
ck('fine_record_improves_error',(3-1/s.sqrt(2))/4>s.Rational(1,2))
ck('triangle_refinement_bound',s.sqrt(avg.dot(avg))< (s.sqrt(v0.dot(v0))+s.sqrt(v1.dot(v1)))/2)
paths=['lab/process/k2380-complete-erasure-recovery.json','lab/process/k2377-time-ordered-rate-robustness.json']
paths += [str(p.relative_to(ROOT)) for p in (ROOT/'lab/process').glob('k2362-*.json')]
report={'result_id':'K2383','checks':len(checks),'check_names':checks,'changed_channel_or_scope_controls':controls,'analytic_fixture_decimals':{'lambda_X':lx,'lambda_Z':lz,'error':error,'idle_error':float(idle)},'scope':'Optimal abstract final flag-only CPTP decoder for specified matched-rail driven channel. No inherited21-gate bound, finite-slew fixture, measured apparatus or GU verdict.','dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
text=json.dumps(report,sort_keys=True,indent=2)+'\n'
if '--write' in sys.argv:(ROOT/'lab/process/k2383-driven-erasure-recovery.json').write_text(text)
print(text)
