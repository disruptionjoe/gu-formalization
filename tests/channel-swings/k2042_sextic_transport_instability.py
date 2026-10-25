"""Exact sextic vector field, saddle, and complete transfer reduction."""
from pathlib import Path
import sympy as s
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2042-sextic-transport-instability.json'
def produce():
 x,y,a,b=s.symbols('x y a b',real=True);u=s.Matrix([x,y,a,b]);z=x+s.I*y;w=a+s.I*b
 V=s.expand(s.re(z**2*s.conjugate(w)**4));J=s.Matrix([[0,-1],[1,0]])
 T=s.diag(J,2*J);f=-T.inv()*s.Matrix([s.diff(V,c) for c in u])
 assert s.expand((u.T*f)[0])==0
 h=s.symbols('h',positive=True);B=s.simplify(f.jacobian(u).subs({x:0,y:0,a:h,b:0}))
 assert B==s.Matrix([[0,2*h**4,0,0],[2*h**4,0,0,0],[0,0,0,0],[0,0,0,0]])
 X,Y=s.symbols('X Y',real=True);reduced=s.simplify(f.subs({x:X/s.sqrt(2),y:X/s.sqrt(2),a:Y,b:0}))
 assert reduced==s.Matrix([s.sqrt(2)*X*Y**4,s.sqrt(2)*X*Y**4,-2*X**2*Y**3,0])
 q,M=s.symbols('q M',positive=True);H=s.log(q/(1-q))+1/(1-q)
 assert s.simplify(s.diff(H,q)*4*M**2*q*(1-q)**2)==4*M**2
 assert s.expand(2*X*(2*X*Y**4)+2*Y*(-2*X**2*Y**3))==0
 assert s.diff(2*X*Y**4,X)==2*Y**4 and s.diff(2*X*Y**4,Y)==8*X*Y**3
 assert s.diff(-2*X**2*Y**3,X)==-4*X*Y**3 and s.diff(-2*X**2*Y**3,Y)==-6*X**2*Y**2
 # Fourier mode is transport plus real saddle, with no high-frequency growth rate.
 k,c,lam=s.symbols('k c lam',real=True)
 symbol=B-s.I*c*k*s.eye(4)
 assert s.expand((lam*s.eye(4)-symbol).det()-(lam+s.I*c*k)**2*((lam+s.I*c*k)**2-4*h**8))==0
 inputs=['explorations/conditional-build/k2038-observed-action-compression-2026-10-24.md','lab/process/k2038-observed-action-compression.json','explorations/conditional-build/k2040-nonlinear-resonance-selection-2026-10-24.md']
 return dict(result_id='K2042',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',potential=str(V),variables=['x','y','a','b'],vector_field=[str(s.expand(v)) for v in f],equilibrium=['0','0','h','0'],jacobian=[[str(v) for v in row] for row in B.tolist()],growth_rate='2*h**4',reduction=['Xdot=2*X*Y**4','Ydot=-2*X**2*Y**3'],transfer=dict(norm='M=X**2+Y**2',fraction='q=X**2/M',ode='4*M**2*q*(1-q)**2',primitive='log(q/(1-q))+1/(1-q)',range='0<q<1; complete heteroclinic transfer as t ranges over R'),pde=dict(domain='R x T^2 or T^3; fields depend on first coordinate in two selected same-speed complex eigenlines',solution='u(t,x)=Phi_t(u0(x-c*t)), c=+1 or -1',gradient_bound='exp(30*R**4*abs(t))*abs(u0_prime(x-c*t))',opposite_speed_real_plane=dict(equations=['X_t+X_x=2*X*Y**4','Y_t-Y_x=-2*X**2*Y**3'],forward_global=True,backward_global_claim=False,bounds=['abs(Y(t,x))<=sup_abs_Y0','abs(X(t,x))<=sup_abs_X0*exp(2*sup_abs_Y0**4*t)']),general_three_dimensional_global_existence=False),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},scope='Conditional real commuting classical model. Exponential and nonlinear instability of a nonzero equilibrium; complete bounded homogeneous and selected characteristic solutions. No source/physical parity, quantum positivity, generic PDE blowup or novelty claim.')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2042 exact gradient/current/saddle/reduced transfer identities')
