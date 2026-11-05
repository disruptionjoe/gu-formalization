#!/usr/bin/env python3
"""Exact geometry and Green-interface checks; universal proofs in note."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import sympy as s
root=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
checks=[];controls=[]
def ck(name,condition):
    assert bool(condition),'FAIL '+name
    checks.append(name)
def ct(name,condition):
    assert bool(condition),'FAIL contrary '+name
    controls.append(name)


t,K=s.symbols('t K',positive=True);zeta=s.sinh(t)**2;J=s.sinh(t)*s.cosh(t)**s.Rational(3,2)
x=s.log(s.tanh(t/2));dx=s.simplify(s.diff(x,t));ck('actual_coordinate_derivative',s.trigsimp(dx-1/s.sinh(t))==0)
volume=K**(-s.Rational(7,2))*s.cosh(t)**3*s.sinh(t)**3
W=s.simplify(volume/dx);ck('actual_density',s.simplify(W-K**(-s.Rational(7,2))*J**2*zeta)==0)
forcing=s.simplify(-J*zeta/(K*W));ck('invariant_point_forcing',s.simplify(forcing+K**s.Rational(5,2)/J)==0)
ct('coordinate_delta_wrong',s.simplify(-J*zeta/K-forcing)!=0)
ct('missing_dt_dx_wrong',s.simplify(volume-W)!=0)
# Noncommuting resolvent identity: order matters, no simultaneous diagonalization.
L0=s.Matrix([[3,1],[1,2]]);V=s.Matrix([[0,2],[0,1]]);L=L0+V;G0=L0.inv();G=L.inv();mu=s.Matrix([2,-1])
sol=G0*mu-G*V*G0*mu
ck('actual_resolvent_cancellation',L*sol==mu and sol==G*mu)
ct('wrong_resolvent_sign',L*(G0*mu+G*V*G0*mu)!=mu)
ct('inverses_do_not_commute',G*G0!=G0*G)
ct('misordered_resolvent_product',L*(G0*mu-G0*G*V*mu)!=mu)
# Exact regular-ODE outgoing fixture. This checks interfaces, not the curved theorem.
x,y,dd,kk=s.symbols('x y dd kk',real=True,positive=True)
gleft=s.exp(s.I*kk*(y-x))/(2*s.I*kk);gright=s.exp(s.I*kk*(x-y))/(2*s.I*kk)
ck('green_homogeneous_left',s.simplify(s.diff(gleft,x,2)+kk**2*gleft)==0)
ck('green_homogeneous_right',s.simplify(s.diff(gright,x,2)+kk**2*gright)==0)
ck('green_continuity',s.simplify((gright-gleft).subs(x,y))==0)
ck('unit_distribution_jump',s.simplify((s.diff(gright,x)-s.diff(gleft,x)).subs(x,y))==1)
ck('left_complex_trace',s.simplify((s.diff(gleft,x)+s.I*kk*gleft).subs(x,0))==0)
ck('right_complex_trace',s.simplify((s.diff(gright,x)-s.I*kk*gright).subs(x,dd))==0)
ck('bilinear_symmetry',s.simplify(gleft-gright.subs({x:y,y:x},simultaneous=True))==0)
ct('Hermitian_symmetry_false',s.simplify(gleft-s.conjugate(gright.subs({x:y,y:x},simultaneous=True)))!=0)
ct('omit_green_normalization_jump',s.simplify((s.diff(2*s.I*kk*gright,x)-s.diff(2*s.I*kk*gleft,x)).subs(x,y))!=1)
ck('source_derivative_left',s.simplify(s.diff(gleft,y)-s.I*kk*gleft)==0)
ck('source_derivative_right',s.simplify(s.diff(gright,y)+s.I*kk*gright)==0)
ct('wrong_endpoint_sign',s.simplify((s.diff(gleft,x)-s.I*kk*gleft).subs(x,0))!=0)
# Mollifier cannot be passed through an L2 bound with a uniform norm.
eps=s.symbols('eps',positive=True)
ck('unit_box_mollifier_mass',s.integrate(1/(2*eps),(x,-eps,eps))==1)
ck('box_mollifier_L2_diverges',s.integrate(1/(4*eps**2),(x,-eps,eps))==1/(2*eps))
# Exact max-index shells for spherical multiplicities (normalizing sphere volumes omitted).
p=s.symbols('p',integer=True,positive=True)
shell=s.expand(2*p*p*p*(p+1)*(2*p+1)/6-p**4)
ck('angular_shell_exact',s.factor(shell-(s.Rational(2,3)*p**5+s.Rational(1,3)*p**3))==0)
ck('angular_shell_bound',s.expand(2*p**5-shell-p**3*(4*p**2-1)/3)==0)
for N in [1,2,4,8]:
 actual=sum(i*i*j*j for i in range(1,N+1) for j in range(1,N+1) if max(i,j)==N)
 ck('multiplicity_shell_'+str(N),actual==shell.subs(p,N))
ct('omit_multiplicity_changes_measure',sum(i*i*j*j for i in range(1,4) for j in range(1,4))!=9)
# Lattice norm a^2=i^2+j^2-1 >=max(i,j)^2. H^-4 shell <=2p^-3.
i,j=s.symbols('i j',positive=True);ck('joint_weight',s.expand(1+(i-1)*(i+1)+(j-1)*(j+1))==i*i+j*j-1)
r2,a2=s.symbols('r2 a2');ck('separated_scale_bound',s.expand(37*r2*a2-(30+a2+6*r2)-(37*(r2-1)*(a2-1)+31*(r2-1)+36*(a2-1)))==0)
ck('cofactor_loss',5+4*2==13)
ck('point_sobolev_loss',4+13+26==43)
ck('source_displacement_loss',4+14+26==44 and 5+13+26==44)
ck('radial_inputs',30+13==43 and 30+14==44)
ck('radial_continuity_margin',30-26>F(5,2))
ck('conserved_test_margin',44+2==46)
# Verify actual matrix entry degrees from unchanged predecessor reconstruction algebra.
# Extract only its symbolic matrix construction, no predecessor checks or output replay.
pre=(root/'tests/channel-swings/k2584_scalar_spectral_boundary_inverse_probe.py').read_text()
start=pre.index('k=s.symbols');end=pre.index('\n\nbank=')
source=pre[start:end];source='\n'.join(line for line in source.splitlines() if not line.startswith(('ck(','for i in range(5):ck(')))
ns={'s':s,'F':F};exec(compile(source,'inherited_matrix_definition','exec'),ns)
M=ns['M'];X,Y=ns['X'],ns['Y'];degrees=[s.Poly(s.cancel(v),X,Y).total_degree() for v in M]
ck('actual_matrix_degree_at_most2',max(degrees)==2)
ck('actual_source_column_degree1',max(s.Poly(v,X,Y).total_degree() for v in ns['vsrc'])==1)
ck('derived_safe_reconstruction_degree',2*(5*max(degrees)+1)+2+1==25<26)
E=ns['E'];vsrc=ns['vsrc'];s0=ns['s0'];la=ns['la']
for q in range(5):ck('unchanged_full_Einstein_row_'+str(q),s.cancel((E*s0)[q]-vsrc[q]*(X+Y+2*la))==0)
ct('drop_direct_source_column',E*s0!=s.zeros(5,1))
report={'result':'K2586','checks':checks,'contrary_controls':controls,'evidence_kind':'exact density, algebra, Green-interface and finite multiplicity checks; universal measure/synthesis proof in note','losses':{'first_measure_factor':5,'cofactor':13,'point_B_negative_order':43,'regularization_B_negative_order':44,'detector_potential_order':46},'ceiling':'fixed-annulus specified point/measure response and weak regularization, no pointwise fields, physical selection or arbitrary B distributions'}
refs=['explorations/conditional-build/k2584-scalar-spectral-boundary-inverse-2026-11-05.md','explorations/conditional-build/k2582-affine-radial-boundary-response-2026-11-05.md','explorations/conditional-build/k2562-parameter-dependent-response-2026-11-05.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2586-fixed-annulus-point-response.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':report['result'],'checks':len(checks),'controls':len(controls),'status':'pass'}))
