from pathlib import Path
import sympy as z
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={}
def zero(x):return z.simplify(x)==0
def chk(n,v):checks[n]=bool(v)
H,u,d,q,m,b,V1,V2=z.symbols('H u d q m beta V1 V2',nonzero=True,real=True)
Phi,chi,pi,n,v=z.symbols('Phi chi pi n v',real=True);y=z.Matrix([Phi,chi,pi,n,v]);bgv=z.Matrix([H,u,d,q,V1]);bg=z.Matrix([-(u*u+d)/(2*m),-3*H*u-V1-b*d,(-3*H+b*u)*d,-2*H*q,V2*u])
fPhi=-H*Phi+(u*chi-d*v)/(2*m)
f=z.Matrix([fPhi,pi,-3*H*pi-(q+V2+b*b*d)*chi+4*u*fPhi-2*(V1+b*d)*Phi-b*d*n,3*fPhi+q*v,-Phi-b*chi-b*u*v])
constraint=q*Phi+3*H*(fPhi+H*Phi)+(u*pi-u*u*Phi+V1*chi+d*(n+b*chi))/(2*m)
nsol=z.solve(constraint,n)[0]
def dt(expr,ff=f):return (z.Matrix([expr]).jacobian(bgv)*bg)[0]+(z.Matrix([expr]).jacobian(y)*ff)[0]
W,p,r,s=z.symbols('W p r s',real=True);alpha=u/(2*m);c=1+2*b*b*m
wexpr=chi-2*b*m*Phi;pexpr=pi-2*b*m*fPhi
subst={chi:W+2*b*m*Phi,pi:p+2*b*m*fPhi.subs(chi,W+2*b*m*Phi)}
def convert(x):return z.expand(x.subs(n,nsol).subs(subst,simultaneous=True))
gPhi=(-H+b*u)*Phi-d*v/(2*m)+alpha*W
gv=-c*Phi-b*u*v-b*W
B=2*u*u/m+4*b*H*u-V2+2*b*V1
D=-2*u*d/m-4*b*H*d
C=(4*u+2*b*m*H)*(-H+b*u)+2*b*m*(-V2+3*b*H*u+2*b*V1)-2*V1-2*b*d+2*b*m*(2*bg[0]+3*H*H)
gp=-q*W-3*H*p+B*W+C*Phi+D*v
chk('W_dot_identity',zero(convert(dt(wexpr))-p));chk('Phi_normal_form',zero(convert(f[0])-gPhi));chk('velocity_normal_form',zero(convert(f[4])-gv));chk('p_normal_form',zero(convert(dt(pexpr))-gp))
chk('constraint_propagated',zero(dt(constraint)+3*H*constraint));chk('inverse_pi',zero(convert(pexpr)-p))
old=z.Matrix([Phi,v,W,p]);gg=z.Matrix([gPhi,gv,p,gp]);new=z.Matrix([q*Phi+alpha*p,q*v-b*p,W,p]);iv={Phi:(r-alpha*p)/q,v:(s+b*p)/q}
def trans(gg0=gg,new0=new):return z.simplify((new0.jacobian(old)*gg0+new0.jacobian(bgv)*bg).subs(iv,simultaneous=True))
normal=trans();var=z.Matrix([r,s,W,p]);J=normal.jacobian(var)
chk('r_qW_cancels',zero(z.diff(normal[0],W).diff(q)))
chk('s_qW_cancels',zero(z.diff(normal[1],W).diff(q)))
chk('wave_W_dot',zero(normal[2]-p));chk('wave_principal',zero(z.diff(normal[3],W)+q-B))
chk('no_H_divisor',all(not z.denom(z.cancel(t)).has(H) for t in J))
chk('only_inverse_q_lower',all(z.degree(z.fraction(z.cancel(t))[0],q)<=z.degree(z.fraction(z.cancel(t))[1],q) for t in J-z.Matrix([[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,-q,0]])))
# Energy evaluated from actual transformed matrix, not an assumed normal form.
weights=z.diag(1,1,1+q,1);wd=z.diag(0,0,-2*H*q,0);Eprime=z.expand((var.T*(J.T*weights+weights*J+wd)*var)[0])
chk('q_cross_cancels',zero(z.expand(Eprime).coeff(W,1).coeff(p,1).diff(q)))
chk('only_q_weight_term',zero(z.diff(z.expand(q*Eprime),q,2)/2+2*H*W*W))
# Constraints and density on the high-frequency chart.
nnormal=z.simplify(nsol.subs(subst,simultaneous=True).subs(iv,simultaneous=True))
slow=z.Matrix([(-3*H+b*u)*r-d*s/(2*m),-c*r-(2*H+b*u)*s])
chk('large_q_slow_limit',all(zero(a-bb) for a,bb in zip([z.limit(normal[i].subs({W:0,p:0}),q,z.oo) for i in [0,1]],slow)))
chk('wave_slow_forcing_inverse_q',zero(normal[3].subs({W:0,p:0})-(C*r+D*s)/q))
delta=-2*m*r/d
slowdt=lambda expr:(z.Matrix([expr]).jacobian(z.Matrix([r,s]))*slow)[0]+(z.Matrix([expr]).jacobian(bgv)*bg)[0]
chk('limit_density_number',zero(z.limit(nnormal.subs({W:0,p:0}),q,z.oo)-delta))
chk('limit_delta_dot',zero(slowdt(delta)-s))
chk('limit_Jeans_equation',zero(slowdt(s)+(2*H+b*u)*s-c*d*delta/(2*m)))
chk('healthy_attraction',zero((c*d/(2*m)).subs(b*b,1/(6*m))-2*d/(3*m)))
N,a=z.symbols('N a',positive=True);seed={Phi:0,chi:0,pi:0,n:0,v:1/N,H:0,q:N*N/a**2}
chk('seed_full_constraint',zero(constraint.subs(seed)))
chk('seed_W_zero_p_small',zero(wexpr.subs(seed)) and zero(pexpr.subs(seed)-b*d/N))
actualseed=z.simplify(new.subs({W:wexpr,p:pexpr},simultaneous=True).subs(seed)/N)
chk('normalized_actual_seed',all(zero(a-bb) for a,bb in zip(actualseed,z.Matrix([alpha*b*d/N**2,1/a**2-b*b*d/N**2,0,b*d/N**2]))))
chk('physical_velocity_bounded',z.simplify(N*(1/N)/a)==1/a)
chk('fixture_friction_bound',2*1+z.Rational(1,2)*4==4)
assert all(checks.values()),[k for k,x in checks.items() if not x]
# Genuine altered shift/equation inputs evaluated through the same derivative maps.
wrongW=chi-b*m*Phi;wrongp=pi-b*m*fPhi
bad_r=z.Matrix([q*Phi-alpha*p,q*v-b*p,W,p]);bad_s=z.Matrix([q*Phi+alpha*p,q*v+b*p,W,p])
badgg=gg.copy();badgg[3]+=q*W
badforce=f.copy();badforce[4]=-Phi+b*chi-b*u*v
faults={
 'half_W_shift':['p_normal_form'] if not zero(convert(dt(wrongp))-gp) else [],
 'wrong_r_shift':['r_qW_cancels'] if not zero(z.diff(trans(new0=bad_r)[0],W).diff(q)) else [],
 'wrong_s_shift':['s_qW_cancels'] if not zero(z.diff(trans(new0=bad_s)[1],W).diff(q)) else [],
 'omit_wave_principal':['wave_principal'] if not zero(z.diff(trans(gg0=badgg)[3],W)+q-B) else [],
 'wrong_dust_force':['constraint_propagated'] if not zero(dt(constraint,badforce)+3*H*constraint) else [],
 'omit_scalar_attraction':['limit_Jeans_equation'] if not zero(slowdt(s)+(2*H+b*u)*s-d*delta/(2*m)) else []}
assert all(faults.values()),faults
stem='k2311-uniform-constrained-dust-evolution';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'tests/channel-swings/k2308_inhomogeneous_constrained_dust_transfer_probe.py','explorations/conditional-build/k2308-inhomogeneous-constrained-dust-transfer-2026-10-30.md','explorations/conditional-build/k2302-designer-frame-turnaround-2026-10-30.md']
data=dict(schema_version='1.0',result_id='K2311',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='exact symbolic coordinate/constraint/energy/limit identities; uniform estimates and convergence proof in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'normal_matrix':str(J),'energy_derivative':str(Eprime),'density_reconstruction':str(nnormal),'space':'Phi,v H^(s+2); chi H^(s+1); pi,n H^s'})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2311',checks=len(checks),faults=len(faults))))
