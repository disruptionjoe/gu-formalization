#!/usr/bin/env python3
"""Exact controls for the tensor normalization wave; no analytic proof claimed."""
import json
import sympy as s

g=s.diag(-1,1,1,1); I=s.eye(4)
checks={}
def check(name, ok):
    checks[name]=bool(ok)
    assert checks[name], name

def eq(a,b): return all(s.simplify(x)==0 for x in a-b)
def zero(a): return eq(a,s.zeros(*a.shape))
boosts=[]; rotations=[]
for i in range(1,4):
    b=s.zeros(4); b[0,i]=b[i,0]=1; boosts.append(b)
for i in range(1,4):
    for j in range(i+1,4):
        b=s.zeros(4); b[i,j]=1; b[j,i]=-1; rotations.append(b)
lie=boosts+rotations
check('lorentz_lie_generators',all(zero(a.T*g+g*a) for a in lie))
coords=s.symbols('y0:10'); Y=s.zeros(4); n=0
for i in range(4):
    for j in range(i,4): Y[i,j]=Y[j,i]=coords[n]; n+=1
vec=lambda m: s.Matrix(list(m))
M=s.Matrix.vstack(*[vec(b.T*Y+Y*b).jacobian(coords) for b in boosts])
check('infinitesimal_three_boost_rank9',M.rank()==9)
check('infinitesimal_fixed_line_g',len(M.nullspace())==1 and eq(s.Matrix([g[i,j] for i in range(4) for j in range(i,4)]),M.nullspace()[0]))
finite=[]
for i in range(1,4):
    a=I.copy(); a[0,0]=a[i,i]=s.Rational(5,4); a[0,i]=a[i,0]=s.Rational(3,4); finite.append(a)
check('finite_boosts_preserve_g',all(eq(a.T*g*a,g) and a.det()==1 for a in finite))
MF=s.Matrix.vstack(*[vec(a.T*Y*a-Y).jacobian(coords) for a in finite])
check('actual_finite_boost_rank9',MF.rank()==9)
check('finite_and_infinitesimal_fixed_line_equal',MF.nullspace()==M.nullspace())
c=s.symbols('a0:6'); L=sum((c[i]*lie[i] for i in range(6)),s.zeros(4))
def stabilizer(v): return 6-vec(L*v).jacobian(c).rank()
u=s.Matrix([1,0,0,0]); w=s.Matrix([0,1,0,0]); n=s.Matrix([1,1,0,0]); m=s.Matrix([1,-1,0,0])
check('timelike_stabilizer_dim3',stabilizer(u)==3)
check('spacelike_stabilizer_dim3',stabilizer(w)==3)
check('null_stabilizer_dim3',stabilizer(n)==3)
check('spacelike_stabilizer_contains_boost',zero(boosts[1]*w))
# A null rotation fixes n, is nonzero nilpotent; exp(tN) is unbounded.
nullrot=boosts[1]+rotations[0]
check('null_rotation_fixes_null_vector',zero(nullrot*n))
check('null_rotation_nonzero_nilpotent',not zero(nullrot) and zero(nullrot**3) and not zero(nullrot**2))
check('ordered_null_pair_stabilizer_dim1',6-s.Matrix.vstack(vec(L*n).jacobian(c),vec(L*m).jacobian(c)).rank()==1)
check('null_pair_sum_timelike',((n+m).T*g*(n+m))[0]<0)
S=s.diag(3,1,1,1)
check('scalar_flat_Ricci_nonzero',s.trace(g*S)==0 and S!=s.zeros(4))
check('Ricci_stabilizer_dim3',6-vec(L.T*S+S*L).jacobian(c).rank()==3)
check('Ricci_stabilizer_exact_rotations',all(zero(a.T*S+S*a) for a in rotations) and all(not zero(a.T*S+S*a) for a in boosts))
eps=s.symbols('eps'); mixed=g*(S+eps*g); Pt=(mixed-(1+eps)*I)/(-4)
check('Ricci_spectral_projector_independent_scalar',eq(Pt,s.diag(1,0,0,0)))
check('Ricci_positive_auxiliary_metric',eq(g-2*g*Pt,I))
check('scalar_changes_without_symmetry_restoration',s.trace(mixed)==4*eps)
# Coframe action k e A^-1: infinitesimal k-a at e=Id.
k=s.symbols('k0:6'); K=sum((k[i]*lie[i] for i in range(6)),s.zeros(4))
J=vec(K-L).jacobian(c+k)
check('coframe_bare_stabilizer_trivial',vec(-L).jacobian(c).rank()==6)
check('coframe_joint_stabilizer_dim6',12-J.rank()==6)
check('coframe_projected_joint_stabilizer_full',s.Matrix.hstack(*[v[:6,0] for v in J.nullspace()]).rank()==6)
R=lambda a,b,c,d:(g[a,c]*S[b,d]+g[b,d]*S[a,c]-g[a,d]*S[b,c]-g[b,c]*S[a,d])/2
check('curvature_pair_symmetries',all(R(a,b,c,d)==-R(b,a,c,d)==-R(a,b,d,c)==R(c,d,a,b) for a in range(4) for b in range(4) for c in range(4) for d in range(4)))
check('curvature_Bianchi',all(R(a,b,c,d)+R(a,c,d,b)+R(a,d,b,c)==0 for a in range(4) for b in range(4) for c in range(4) for d in range(4)))
Ric=s.Matrix(4,4,lambda b,d:sum(g[a,c]*R(a,b,c,d) for a in range(4) for c in range(4)))
check('curvature_contracts_to_S',eq(Ric,S))
# Compute the exact scalar-flat FLRW geometric countercontrol directly.
t,x1,x2,x3=s.symbols('t x1 x2 x3',positive=True); xs=[t,x1,x2,x3]; metric=s.diag(-1,t,t,t); inv=metric.inv()
Gamma=[[[s.simplify(sum(inv[a,d]*(s.diff(metric[d,c],xs[b])+s.diff(metric[d,b],xs[c])-s.diff(metric[b,c],xs[d])) for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
RicFL=s.Matrix(4,4,lambda b,d:s.simplify(sum(s.diff(Gamma[a][b][d],xs[a])-s.diff(Gamma[a][b][a],xs[d])+sum(Gamma[a][a][c]*Gamma[c][b][d]-Gamma[a][d][c]*Gamma[c][b][a] for c in range(4)) for a in range(4))))
check('explicit_FLRW_Ricci',eq(RicFL,s.diag(3/(4*t*t),1/(4*t),1/(4*t),1/(4*t))))
check('explicit_FLRW_scalar_zero',s.simplify(s.trace(inv*RicFL))==0)
check('explicit_FLRW_orthonormal_Ricci',eq(s.diag(1,1/s.sqrt(t),1/s.sqrt(t),1/s.sqrt(t))*RicFL*s.diag(1,1/s.sqrt(t),1/s.sqrt(t),1/s.sqrt(t)),S/(4*t*t)))
v=s.Matrix([s.Rational(5,4),s.Rational(3,4),0,0]); ell=s.Matrix([1,1,0,0]); a=s.symbols('a',real=True)
check('unit_future_clocks', (v.T*g*v)[0]==-1 and v[0]>0)
check('ell_is_null',(ell.T*g*ell)[0]==0)
y=g+a*ell*ell.T
check('rank_one_null_metric_determinant',s.simplify(y.det()-g.det())==0)
check('rank_one_null_inverse',eq(y.inv(),g-a*g*ell*ell.T*g))
def Q(clock):
    h=g+2*(g*clock)*(g*clock).T; hi=h.inv(); dy=y-g; di=y.inv()-g
    return s.simplify(s.trace(hi*dy*hi*dy)+s.trace(h*di*h*di))
check('clock_Q_null_formula_u',s.simplify(Q(u)-8*a*a*(ell.dot(u))**4)==0)
check('clock_Q_null_formula_v',s.simplify(Q(v)-8*a*a*(ell.dot(v))**4)==0)
check('different_clocks_different_density_shape',s.simplify(Q(u)-Q(v))!=0)
check('conformal_ray_fixed_control',all(eq(A.T*(a*g)*A,a*g) for A in finite))
print(json.dumps({'schema':'tensor-normalization-exact-controls-v1','checks':checks,'passed':len(checks),'scope':'Exact finite-dimensional algebra and geometric controls only; analytic compactness, integration and weak limits remain reviewed written proofs.','mutations_rejected':['scalar-zero implies full isotropy','equal stabilizer dimension implies equal compactness','bare coframe stabilizer decides gauge-invariant measure','all finite invariant measures impossible','clock direction yields path-independent regular restoration']},indent=2))
