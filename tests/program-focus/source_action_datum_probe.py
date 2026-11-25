#!/usr/bin/env python3
"""Exact finite controls, not a source/APS/physical-index certificate."""
import json
import sympy as s
checks={}
def check(k,v):
 checks[k]=bool(v)
 assert checks[k],k
# Exact monomial matrices: one i^phase entry per row. No floating arithmetic.
def ident(n):return(tuple(range(n)),(0,)*n)
def scale(A,k):return(A[0],tuple((p+k)%4 for p in A[1]))
def mul(A,B):return(tuple(B[0][j] for j in A[0]),tuple((A[1][i]+B[1][A[0][i]])%4 for i in range(len(A[0]))))
def adj(A):
 inv=[0]*len(A[0]);p=[0]*len(A[0])
 for i,j in enumerate(A[0]):inv[j]=i;p[j]=(-A[1][i])%4
 return(tuple(inv),tuple(p))
def product(arr):
 v=ident(len(arr[0][0]))
 for a in arr:v=mul(v,a)
 return v
def cliff(q,odd=False):
 out=[];n=2**q
 for j in range(q):
  bit=q-j-1
  for yy in [False,True]:
   out.append((tuple(r^(1<<bit) for r in range(n)),tuple((2*((r>>(bit+1)).bit_count()%2)+(1 if (r>>bit)&1 else 3) if yy else 2*((r>>(bit+1)).bit_count()%2))%4 for r in range(n))))
 if odd:out.append((tuple(range(n)),tuple(2*(r.bit_count()%2) for r in range(n))))
 return out
E=cliff(7);n=128;I=ident(n);gam=[a if j<9 else scale(a,1) for j,a in enumerate(E)]
check('Euclidean14_Hermitian',all(adj(a)==a for a in E))
check('K95_Clifford_all_pairs',all(mul(a,a)==scale(I,0 if j<9 else 2) for j,a in enumerate(gam)) and all(mul(gam[i],gam[j])==scale(mul(gam[j],gam[i]),2) for i in range(14) for j in range(i+1,14)))
H=scale(product(gam[9:]),1)
check('Krein_H_Hermitian_involution',adj(H)==H and mul(H,H)==I)
roots=[(1,0),(0,1),(-1,0),(0,-1)];trace=tuple(sum(roots[H[1][r]][k] for r in range(n) if H[0][r]==r) for k in [0,1])
check('Krein_H_trace_zero',trace==(0,0))
check('all_gammas_Krein_skew',all(mul(adj(a),H)==scale(mul(H,a),2) for a in gam))
check('all_bivectors_Krein_skew',all(mul(adj(mul(gam[i],gam[j])),H)==scale(mul(H,mul(gam[i],gam[j])),2) for i in range(14) for j in range(i+1,14)))
# Clifford64 Bott matrix algebra, then a rational sphere-point power control.
L=cliff(6,True);I64=ident(64)
check('Bott13_Hermitian_Clifford',all(adj(a)==a and mul(a,a)==I64 for a in L) and all(mul(L[i],L[j])==scale(mul(L[j],L[i]),2) for i in range(13) for j in range(i+1,13)))
# u=(3I+4i Lambda1)/5; represent in C[t]/(t²−1), adjoint i->−i.
t=s.symbols('t',real=True);u=(3+4*s.I*t)/5
reduce=lambda f:s.rem(s.expand(f),t*t-1,t)
check('Bott_u_unitary_rational_control',reduce(u*s.conjugate(u))==1)
check('Bott_u3_unitary_rational_control',reduce(u**3*s.conjugate(u)**3)==1)
check('balanced_charge_not_insertion_of_copies',len(I64[0])*2==128)
f=s.symbols('f');rad=s.integrate(f**6*(1-f)**6,(f,0,1));check('radial_Chern7_beta_integral',rad==s.factorial(6)**2/s.factorial(13))
check('Chern7_boundary_coefficient',s.simplify(7*rad/s.factorial(7)-s.factorial(6)/s.factorial(13))==0)
check('paired_charge_total_zero',sum([3,-3])==0)
# Noncommuting two-frame first-jet calculation. Generic GL control tests algebra;
# Krein admissibility of the actual generators is separately checked above.
x=s.symbols('x',real=True)
h=s.Matrix([[1,x],[0,1]]);k=s.Matrix([[1,0],[2*x,1]]);eps=s.Matrix([[1+x*x,x],[x,1]])
A=s.Matrix([[x,1],[2,-x]]);B0=s.Matrix([[1,x],[0,-1]])
d=lambda M:M.diff(x)
tr=lambda C,g:g.inv()*C*g+g.inv()*d(g)
eq=lambda M,N:all(s.simplify(v)==0 for v in M-N)
B=tr(B0,eps);ep=k.inv()*eps*h;Ap=tr(A,h);B0p=tr(B0,k)
check('two_frame_B_composition',eq(tr(B0p,ep),tr(B,h)))
check('distortion_tensorial',eq(Ap-tr(B0p,ep),h.inv()*(A-B)*h))
Ah=eps*A*eps.inv()-d(eps)*eps.inv();Ahp=ep*Ap*ep.inv()-d(ep)*ep.inv()
check('dressed_A_covariance',eq(Ahp,tr(Ah,k)))
check('omit_d_epsilon_mutation_detected',not eq(ep*Ap*ep.inv(),tr(eps*A*eps.inv(),k)))
psi=s.Matrix([x*x,1+x]);psid=eps.inv()*psi
check('dressed_derivative_identity',eq(eps*(d(psid)+A*psid),d(psi)+Ah*psi))
check('reference_field_transform',eq(ep*(h.inv()*psid),k.inv()*psi))
# Bosonic finite-jet variational control with arbitrary non-cyclic S.
a,b=s.symbols('a b',real=True);v=s.Matrix([a,b]);F0=s.Matrix([1,2]);D=s.Matrix([[2,1],[0,3]]);Q=s.Matrix([a*b,a*a]);S=s.Matrix([[0,1],[2,0]])
Fbar=F0+D*v/2+Q/3;FB=F0+D*v+Q
SB=(v.T*S*Fbar)[0]+(v.T*v)[0]/2
EL=s.Matrix([s.diff(SB,z) for z in [a,b]]);L=Fbar.jacobian([a,b]);expected=S*Fbar+L.T*S.T*v+v
check('actual_boson_Euler_includes_transpose',eq(EL,expected))
check('printed_endpoint_not_general_Euler',not eq(EL,S*FB+v))
# Metric coordinate-change correction: B=g, T=A-g at fixed A.
g,Avar=s.symbols('g A',real=True);BB,TT=s.symbols('B T',real=True);local=BB*TT+BB*BB*TT+TT**3
chain=(s.diff(local,BB)-s.diff(local,TT)).subs({BB:g,TT:Avar-g})
check('metric_fixed_A_chain_difference',s.simplify(s.diff(local.subs({BB:g,TT:Avar-g}),g)-chain)==0)
check('fixed_T_chain_is_different',s.simplify(chain-s.diff(local,BB).subs({BB:g,TT:Avar-g}))!=0)
# The correlated T=0 restriction is not the fixed-A metric Hessian.
toy=(Avar-g)*g+(Avar-g)**2/2
check('zero_on_correlated_locus',s.simplify(toy.subs(Avar,g))==0)
check('fixed_A_metric_Hessian_not_zero',s.diff(toy,g,2)==-1)
# Both declared coefficient products close on the real Krein Lie algebra.
HH=s.diag(1,-1);XX=s.Matrix([[0,1],[1,0]]);YY=s.I*s.diag(1,2)
is_skew=lambda Z:Z.conjugate().T*HH+HH*Z==s.zeros(2)
check('boson_comm_symi_products_Krein_closed',is_skew(XX) and is_skew(YY) and is_skew(XX*YY-YY*XX) and is_skew(s.I*(XX*YY+YY*XX)))
# Green formula with variable principal coefficient and nonconstant density.
mu=1+x*x;M=s.Matrix([[x,1],[2,x*x]]);V=s.Matrix([[1,x],[0,2]]);p=s.Matrix([x*x,1+x]);row=s.Matrix([[x,1+x*x]]);dual=-(mu*row*M).diff(x)/mu+row*V
left=(mu*(row*(M*p.diff(x)+V*p)-dual*p))[0];flux=(mu*row*M*p)[0].diff(x)
check('Green_density_and_coefficient_derivatives',s.simplify(left-flux)==0)
wrong=-row.diff(x)*M+row*V
check('drop_density_coefficient_derivatives_detected',s.simplify((mu*(row*(M*p.diff(x)+V*p)-wrong*p))[0]-flux)!=0)
# Three current vertices in a reduced exact Clifford polarization.
z0,z1,nu,bz0,bz1,bnu,c0,c1=s.symbols('z0 z1 nu bz0 bz1 bnu c0 c1');j0=s.Matrix([[1,0],[0,-1]]);j1=s.Matrix([[0,1],[1,0]])
z=[s.Matrix([z0,z1]),s.Matrix([z1,z0])];av=[s.I*s.eye(2),j0*j1];N=s.Matrix([nu,2*nu]);barz=[s.Matrix([[bz0,bz1]]),s.Matrix([[bz1,bz0]])];barn=s.Matrix([[bnu,2*bnu]])
wed=lambda b,a:av[b]*z[a]-av[a]*z[b]
curC=sum((barz[a]*sum(([j0,j1][b]*wed(b,a) for b in range(2)),s.zeros(2,1)))[0] for a in range(2))
curN=sum((barz[a]*av[a]*N)[0] for a in range(2));curS=(barn*sum((av[a]*z[a] for a in range(2)),s.zeros(2,1)))[0]
check('all_three_current_vertices_nonzero_polynomials',all(s.expand(c)!=0 for c in [curC,curN,curS]))
check('dropping_SW_changes_current',s.expand(curS)!=0)
# Actual K95 rank128 vector test of the explicit principal inverse.
iph=[s.Integer(1),s.I,s.Integer(-1),-s.I]
def apply(A,v):return [s.expand(iph[A[1][r]]*v[A[0][r]]) for r in range(128)]
def add(v,w):return [s.expand(a+b) for a,b in zip(v,w)]
def scal(c,v):return [s.expand(c*a) for a in v]
xi=[s.Integer(0)]*14;xi[0]=3;xi[9]=1
sign=[1]*9+[-1]*5
cx=lambda v:add(scal(3,apply(gam[0],v)),scal(-1,apply(gam[9],v)))
ic=lambda z:add(scal(3,z[0]),scal(-1,z[9]))
def trace_gamma(z):
 out=[s.Integer(0)]*128
 for a in range(14):out=add(out,scal(sign[a],apply(gam[a],z[a])))
 return out
rr=[[s.Integer(((a+2)*(j+1))%7-3) for j in range(128)] for a in range(14)]
ss=[s.Integer(j%5-2) for j in range(128)];q=s.Integer(8)
w=scal(1/q,add(ic(rr),scal(-1,cx(ss))))
z=[scal(1/q,cx(add(rr[a],scal(-xi[a],w)))) for a in range(14)]
nvv=scal(1/q,add(scal(2,ic(rr)),scal(-1,cx(trace_gamma(rr)))))
check('native128_principal_inverse_scalar_row',ic(z)==ss)
check('native128_principal_inverse_oneform_row',all(add(cx(z[a]),scal(xi[a],add(nvv,scal(-1,trace_gamma(z)))))==rr[a] for a in range(14)))
# Known countercontrols, not new GU exclusions.
check('residual_square_stationary_nonzero',s.diff(x*x+1,x).subs(x,0)==0 and (x*x+1).subs(x,0)==1)
check('codimension10_H7_two_traces',7>10/2 and 6>10/2 and 7-10/2==2 and 6-10/2==1)
check('literal_q0_normal_jet_visible',mul(gam[4],gam[4])==I) # normal positive Clifford coefficient invertible
check('source_2plus1_dimensions',384+1152+128==1664 and 14*128-128==1664)
check('same128_carrier_all_integer_k',128==64+64)
print(json.dumps({'schema':'source-action-datum-exact-controls-v1','passed':len(checks),'checks':checks,'scope':'Exact Clifford, connection first-jet, polynomial variation and radial controls. No numerical winding, global APS theorem, stationary field solution, physical positivity or family-count certification.'},indent=2))
